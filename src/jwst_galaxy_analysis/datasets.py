from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd
import requests
import yaml
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
    format: str | None = None
    filename: str | None = None
    catalog: str | None = None
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


def fetch_catalog_from_vizier(catalog_id: str, target_path: Path, row_limit: int | None = None) -> Path:
    target_path.parent.mkdir(parents=True, exist_ok=True)
    vizier = Vizier(row_limit=row_limit if row_limit is not None else -1)
    tables = vizier.get_catalogs(catalog_id)
    if len(tables) == 0:
        raise ValueError(f"No tables returned for VizieR catalog {catalog_id}")
    tables[0].write(target_path, overwrite=True)
    return target_path


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
        fetch_catalog_from_vizier(spec.catalog, raw_path.with_suffix(".fits"), row_limit=spec.row_limit)
        raw_path = raw_path.with_suffix(".fits")
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

