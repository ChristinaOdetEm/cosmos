from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import pandas as pd

from .config import ensure_directories
from .io import sha256_file


@dataclass
class TransformationRecord:
    name: str
    description: str
    input_name: str
    output_name: str
    parameters: dict[str, Any] = field(default_factory=dict)
    row_count_before: int | None = None
    row_count_after: int | None = None
    columns_before: list[str] = field(default_factory=list)
    columns_after: list[str] = field(default_factory=list)
    created_at_utc: str = field(
        default_factory=lambda: datetime.now(UTC).replace(microsecond=0).isoformat()
    )
    output_path: str | None = None
    output_sha256: str | None = None


class ProvenanceTracker:
    def __init__(self, project_root: Path | None = None) -> None:
        self.paths = ensure_directories(project_root)

    def log(
        self,
        *,
        name: str,
        description: str,
        input_name: str,
        output_name: str,
        parameters: dict[str, Any] | None = None,
        before: pd.DataFrame | None = None,
        after: pd.DataFrame | None = None,
        output_path: Path | None = None,
    ) -> Path:
        record = TransformationRecord(
            name=name,
            description=description,
            input_name=input_name,
            output_name=output_name,
            parameters=parameters or {},
            row_count_before=None if before is None else len(before),
            row_count_after=None if after is None else len(after),
            columns_before=[] if before is None else list(before.columns),
            columns_after=[] if after is None else list(after.columns),
            output_path=None if output_path is None else str(output_path),
            output_sha256=None if output_path is None else sha256_file(output_path),
        )
        manifest_path = self.paths.manifests / f"{output_name}.manifest.json"
        manifest_path.write_text(json.dumps(asdict(record), indent=2), encoding="utf-8")
        return manifest_path


def documented_transform(name: str, description: str):
    def decorator(func):
        def wrapper(df: pd.DataFrame, *args, **kwargs):
            tracker: ProvenanceTracker | None = kwargs.pop("tracker", None)
            input_name = kwargs.pop("input_name", "in_memory_table")
            output_name = kwargs.get("output_name", f"{name}_output")
            result = func(df.copy(), *args, **kwargs)
            if tracker is not None:
                tracker.log(
                    name=name,
                    description=description,
                    input_name=input_name,
                    output_name=output_name,
                    parameters={k: v for k, v in kwargs.items() if k != "output_name"},
                    before=df,
                    after=result,
                )
            return result

        return wrapper

    return decorator

