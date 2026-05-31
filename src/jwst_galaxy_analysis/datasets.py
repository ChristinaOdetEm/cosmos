from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import requests
import yaml
from astropy.config.paths import set_temp_cache
from astropy.table import Table
from astroquery.vizier import Vizier

from .config import ensure_directories
from .io import load_table, write_parquet
from .provenance import ProvenanceTracker
from .transforms import drop_empty_rows, standardize_columns


@dataclass
class CatalogSpec:
    name: str
    kind: str
    description: str | None = None
    url: str | None = None
    urls: list[str] | None = None
    format: str | None = None
    filename: str | None = None
    filenames: list[str] | None = None
    catalog: str | None = None
    table_name: str | None = None
    row_limit: int | None = None


def load_registry(path: Path) -> dict[str, CatalogSpec]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    catalogs = payload.get("catalogs", {})
    return {
        name: CatalogSpec(name=name, **config)
        for name, config in catalogs.items()
    }


def list_catalogs(path: Path) -> list[CatalogSpec]:
    return list(load_registry(path).values())


def fetch_catalog_from_url(url: str, target_path: Path) -> Path:
    target_path.parent.mkdir(parents=True, exist_ok=True)
    response = requests.get(url, timeout=120)
    response.raise_for_status()
    target_path.write_bytes(response.content)
    return target_path


def fetch_catalog_from_vizier(
    catalog_id: str,
    target_path: Path,
    row_limit: int | None = None,
    table_name: str | None = None,
) -> Path:
    target_path.parent.mkdir(parents=True, exist_ok=True)
    cache_dir = target_path.parent.parent / "interim" / "astropy-cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    with set_temp_cache(cache_dir, delete=False):
        vizier = Vizier(row_limit=row_limit if row_limit is not None else -1)
        tables = vizier.get_catalogs(table_name or catalog_id)
    if len(tables) == 0:
        raise ValueError(f"No tables returned for VizieR catalog {catalog_id}")
    tables[0].write(target_path, overwrite=True)
    return target_path


def load_fits_hdu_dataframe(
    path: Path,
    *,
    hdu: str,
    columns: list[str] | None = None,
) -> pd.DataFrame:
    table = Table.read(path, hdu=hdu)
    names = [name for name in table.colnames if len(table[name].shape) <= 1]
    if columns is not None:
        names = [name for name in columns if name in names]
    return table[names].to_pandas()


def materialize_processed_dataset(
    raw_path: Path,
    output_name: str,
    *,
    fmt: str | None = None,
    project_root: Path | None = None,
) -> tuple[pd.DataFrame, Path, Path]:
    paths = ensure_directories(project_root)
    tracker = ProvenanceTracker(project_root)
    raw_df = load_table(raw_path, fmt=fmt)
    cleaned_df = drop_empty_rows(raw_df, tracker=tracker, input_name=raw_path.name, output_name=f"{output_name}_01")
    normalized_df = standardize_columns(
        cleaned_df,
        tracker=tracker,
        input_name=f"{output_name}_01",
        output_name=f"{output_name}_02",
    )
    processed_path = write_parquet(normalized_df, paths.data_processed / f"{output_name}.parquet")
    manifest_path = tracker.log(
        name="write_processed_dataset",
        description="Persist the cleaned dataset as the reproducible processed analysis artifact.",
        input_name=raw_path.name,
        output_name=output_name,
        before=raw_df,
        after=normalized_df,
        output_path=processed_path,
    )
    return normalized_df, processed_path, manifest_path


def materialize_public_jades_dr5_dataset(
    *,
    raw_paths: list[Path],
    spectroscopy_raw_path: Path | None = None,
    output_name: str,
    project_root: Path | None = None,
) -> tuple[pd.DataFrame, Path, Path]:
    paths = ensure_directories(project_root)
    tracker = ProvenanceTracker(project_root)
    region_frames: list[pd.DataFrame] = []
    for raw_path in raw_paths:
        filename = raw_path.name.lower()
        if "goods_s" in filename or "goods-s" in filename:
            region_name = "goods_s"
        elif "goods_n" in filename or "goods-n" in filename:
            region_name = "goods_n"
        else:
            raise ValueError(f"Could not infer JADES region from filename: {raw_path.name}")
        flag_df = load_fits_hdu_dataframe(
            raw_path,
            hdu="FLAG",
            columns=["ID", "RA", "DEC", "FLAG_ST", "FLAG_BS", "FLAG_BN"],
        )
        photoz_df = load_fits_hdu_dataframe(raw_path, hdu="PHOTOZ")
        if "z_spec" in photoz_df.columns:
            photoz_df = photoz_df.rename(columns={"z_spec": "z_spec_dr5"})
        merged_df = flag_df.merge(photoz_df, on="ID", how="inner", validate="one_to_one")
        merged_df["region"] = region_name
        region_frames.append(merged_df)

    raw_df = pd.concat(region_frames, ignore_index=True)
    if "z_spec_dr5" in raw_df.columns:
        raw_df["z_spec_dr5"] = raw_df["z_spec_dr5"].replace(-9999, np.nan)

    if spectroscopy_raw_path is not None:
        spectroscopy_df = load_fits_hdu_dataframe(
            spectroscopy_raw_path,
            hdu="Obs_info",
            columns=["Unique_ID", "NIRCam_DR5_ID", "Field", "z_phot", "z_Spec", "z_Spec_flag"],
        )
        spectroscopy_df = spectroscopy_df[spectroscopy_df["NIRCam_DR5_ID"] > 0].copy()
        spectroscopy_df["z_Spec"] = spectroscopy_df["z_Spec"].replace(-1, np.nan)
        for column in ["Unique_ID", "Field", "z_Spec_flag"]:
            spectroscopy_df[column] = spectroscopy_df[column].map(
                lambda value: value.decode("utf-8") if isinstance(value, bytes) else value
            )
        quality_order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        spectroscopy_df["quality_rank"] = spectroscopy_df["z_Spec_flag"].map(quality_order).fillna(99)
        spectroscopy_df["has_z_spec"] = spectroscopy_df["z_Spec"].notna().astype(int)
        spectroscopy_df = spectroscopy_df.sort_values(
            ["NIRCam_DR5_ID", "quality_rank", "has_z_spec", "Unique_ID"],
            ascending=[True, True, False, True],
        )
        spectroscopy_df = spectroscopy_df.drop_duplicates(subset=["NIRCam_DR5_ID"], keep="first")
        spectroscopy_df = spectroscopy_df.rename(
            columns={
                "Unique_ID": "dr4_unique_id",
                "NIRCam_DR5_ID": "ID",
                "Field": "dr4_field",
                "z_phot": "z_phot_dr4",
                "z_Spec": "z_spec",
                "z_Spec_flag": "z_spec_flag",
            }
        ).drop(columns=["quality_rank", "has_z_spec"])
        raw_df = raw_df.merge(spectroscopy_df, on="ID", how="left", validate="one_to_one")

    cleaned_df = drop_empty_rows(raw_df, tracker=tracker, input_name=output_name, output_name=f"{output_name}_01")
    normalized_df = standardize_columns(
        cleaned_df,
        tracker=tracker,
        input_name=f"{output_name}_01",
        output_name=f"{output_name}_02",
    )
    processed_path = write_parquet(normalized_df, paths.data_processed / f"{output_name}.parquet")
    manifest_path = tracker.log(
        name="write_processed_dataset",
        description="Persist the cleaned dataset as the reproducible processed analysis artifact.",
        input_name=";".join(
            [*(path.name for path in raw_paths), *([spectroscopy_raw_path.name] if spectroscopy_raw_path else [])]
        ),
        output_name=output_name,
        parameters={
            "raw_paths": [str(path) for path in raw_paths],
            "spectroscopy_raw_path": None if spectroscopy_raw_path is None else str(spectroscopy_raw_path),
        },
        before=raw_df,
        after=normalized_df,
        output_path=processed_path,
    )
    return normalized_df, processed_path, manifest_path


def fetch_from_spec(spec: CatalogSpec, *, project_root: Path | None = None) -> dict[str, Any]:
    paths = ensure_directories(project_root)
    filename = spec.filename or f"{spec.name}.{spec.format or 'csv'}"
    raw_path = paths.data_raw / filename
    if spec.kind == "url":
        if not spec.url:
            raise ValueError(f"Catalog {spec.name} is missing a URL")
        fetch_catalog_from_url(spec.url, raw_path)
    elif spec.kind == "vizier":
        if not spec.catalog:
            raise ValueError(f"Catalog {spec.name} is missing a VizieR identifier")
        fetch_catalog_from_vizier(
            spec.catalog,
            raw_path.with_suffix(".fits"),
            row_limit=spec.row_limit,
            table_name=spec.table_name,
        )
        raw_path = raw_path.with_suffix(".fits")
    elif spec.kind == "jades_dr5":
        if not spec.urls:
            raise ValueError(f"Catalog {spec.name} is missing source URLs")
        raw_filenames = spec.filenames or [Path(url).name for url in spec.urls]
        if len(raw_filenames) != len(spec.urls):
            raise ValueError(f"Catalog {spec.name} has mismatched URLs and filenames")
        raw_paths = []
        for url, raw_filename in zip(spec.urls, raw_filenames, strict=True):
            target_path = paths.data_raw / raw_filename
            fetch_catalog_from_url(url, target_path)
            raw_paths.append(target_path)
        spectroscopy_raw_path = None
        if spec.url:
            spectroscopy_filename = spec.filename or Path(spec.url).name
            spectroscopy_raw_path = paths.data_raw / spectroscopy_filename
            fetch_catalog_from_url(spec.url, spectroscopy_raw_path)
        _, processed_path, manifest_path = materialize_public_jades_dr5_dataset(
            raw_paths=raw_paths,
            spectroscopy_raw_path=spectroscopy_raw_path,
            output_name=spec.name,
            project_root=project_root,
        )
        return {
            "name": spec.name,
            "raw_paths": raw_paths,
            "spectroscopy_raw_path": spectroscopy_raw_path,
            "processed_path": processed_path,
            "manifest_path": manifest_path,
        }
    else:
        raise ValueError(f"Unsupported catalog kind: {spec.kind}")

    _, processed_path, manifest_path = materialize_processed_dataset(
        raw_path,
        output_name=spec.name,
        fmt=spec.format,
        project_root=project_root,
    )
    return {
        "name": spec.name,
        "raw_path": raw_path,
        "processed_path": processed_path,
        "manifest_path": manifest_path,
    }
