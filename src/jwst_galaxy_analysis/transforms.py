from __future__ import annotations

import pandas as pd

from .provenance import documented_transform


@documented_transform(
    name="standardize_columns",
    description="Normalize column names to lowercase snake_case for consistent downstream analysis.",
)
def standardize_columns(df: pd.DataFrame, *, output_name: str = "standardized_table") -> pd.DataFrame:
    renamed = {
        column: column.strip().lower().replace(" ", "_").replace("-", "_") for column in df.columns
    }
    return df.rename(columns=renamed)


@documented_transform(
    name="drop_empty_rows",
    description="Remove fully empty rows created by export or parsing artifacts.",
)
def drop_empty_rows(df: pd.DataFrame, *, output_name: str = "non_empty_table") -> pd.DataFrame:
    return df.dropna(how="all").reset_index(drop=True)

