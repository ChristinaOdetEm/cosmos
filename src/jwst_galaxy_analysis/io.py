from __future__ import annotations

import hashlib
from pathlib import Path

import pandas as pd


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def detect_table_format(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in {".csv"}:
        return "csv"
    if suffix in {".tsv", ".txt"}:
        return "tsv"
    if suffix == ".parquet":
        return "parquet"
    if suffix in {".fits", ".fit", ".fz"}:
        return "fits"
    raise ValueError(f"Unsupported table format for {path}")


def load_table(path: Path, fmt: str | None = None) -> pd.DataFrame:
    table_format = fmt or detect_table_format(path)
    if table_format == "csv":
        return pd.read_csv(path)
    if table_format == "tsv":
        return pd.read_csv(path, sep="\t")
    if table_format == "parquet":
        return pd.read_parquet(path)
    if table_format == "fits":
        from astropy.table import Table

        return Table.read(path).to_pandas()
    raise ValueError(f"Unsupported table format: {table_format}")


def write_parquet(df: pd.DataFrame, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)
    return path

