from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ProjectPaths:
    root: Path
    data_raw: Path
    data_interim: Path
    data_processed: Path
    outputs: Path
    manifests: Path
    figures: Path


def discover_project_root(start: Path | None = None) -> Path:
    current = (start or Path.cwd()).resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "pyproject.toml").exists():
            return candidate
    return current


def get_paths(start: Path | None = None) -> ProjectPaths:
    root = discover_project_root(start)
    data_dir = root / "data"
    outputs_dir = root / "outputs"
    return ProjectPaths(
        root=root,
        data_raw=data_dir / "raw",
        data_interim=data_dir / "interim",
        data_processed=data_dir / "processed",
        outputs=outputs_dir,
        manifests=outputs_dir / "manifests",
        figures=outputs_dir / "figures",
    )


def ensure_directories(start: Path | None = None) -> ProjectPaths:
    paths = get_paths(start)
    for directory in [
        paths.data_raw,
        paths.data_interim,
        paths.data_processed,
        paths.outputs,
        paths.manifests,
        paths.figures,
    ]:
        directory.mkdir(parents=True, exist_ok=True)
    return paths

