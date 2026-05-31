from __future__ import annotations

import argparse
from pathlib import Path

from .config import ensure_directories
from .datasets import (
    CatalogSpec,
    fetch_catalog_from_url,
    fetch_catalog_from_vizier,
    fetch_from_spec,
    list_catalogs,
    load_registry,
    materialize_processed_dataset,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="jwst-galaxy")
    subparsers = parser.add_subparsers(dest="command", required=True)

    catalogs_parser = subparsers.add_parser("catalogs", help="Work with the local catalog registry.")
    catalogs_subparsers = catalogs_parser.add_subparsers(dest="catalogs_command", required=True)

    list_parser = catalogs_subparsers.add_parser("list", help="List catalog registry entries.")
    list_parser.add_argument("--registry", type=Path, default=Path("catalog_sources.yml"))

    fetch_parser = catalogs_subparsers.add_parser("fetch", help="Fetch a catalog from the registry.")
    fetch_parser.add_argument("name")
    fetch_parser.add_argument("--registry", type=Path, default=Path("catalog_sources.yml"))

    fetch_url_parser = subparsers.add_parser("fetch-url", help="Fetch a public table directly from a URL.")
    fetch_url_parser.add_argument("url")
    fetch_url_parser.add_argument("--name", required=True)
    fetch_url_parser.add_argument("--format", choices=["csv", "tsv", "parquet", "fits"], default=None)

    vizier_parser = subparsers.add_parser("vizier-fetch", help="Fetch a public table from VizieR.")
    vizier_parser.add_argument("catalog_id")
    vizier_parser.add_argument("--name", required=True)
    vizier_parser.add_argument("--row-limit", type=int, default=None)

    return parser


def command_catalogs_list(registry_path: Path) -> int:
    catalogs = list_catalogs(registry_path)
    for catalog in catalogs:
        print(f"{catalog.name}: kind={catalog.kind} description={catalog.description or '-'}")
    return 0


def command_catalogs_fetch(name: str, registry_path: Path) -> int:
    registry = load_registry(registry_path)
    result = fetch_from_spec(registry[name])
    print(f"Fetched {name}")
    raw_paths = result.get("raw_paths")
    if raw_paths is not None:
        for raw_path in raw_paths:
            print(f"Raw: {raw_path}")
        spectroscopy_raw_path = result.get("spectroscopy_raw_path")
        if spectroscopy_raw_path is not None:
            print(f"Raw: {spectroscopy_raw_path}")
    else:
        print(f"Raw: {result['raw_path']}")
    print(f"Processed: {result['processed_path']}")
    print(f"Manifest: {result['manifest_path']}")
    return 0


def command_fetch_url(url: str, name: str, fmt: str | None) -> int:
    paths = ensure_directories()
    extension = fmt or Path(url).suffix.lstrip(".") or "csv"
    raw_path = paths.data_raw / f"{name}.{extension}"
    fetch_catalog_from_url(url, raw_path)
    _, processed_path, manifest_path = materialize_processed_dataset(raw_path, name, fmt=fmt)
    print(f"Raw: {raw_path}")
    print(f"Processed: {processed_path}")
    print(f"Manifest: {manifest_path}")
    return 0


def command_vizier_fetch(catalog_id: str, name: str, row_limit: int | None) -> int:
    paths = ensure_directories()
    raw_path = paths.data_raw / f"{name}.fits"
    fetch_catalog_from_vizier(catalog_id, raw_path, row_limit=row_limit)
    _, processed_path, manifest_path = materialize_processed_dataset(raw_path, name, fmt="fits")
    print(f"Raw: {raw_path}")
    print(f"Processed: {processed_path}")
    print(f"Manifest: {manifest_path}")
    return 0


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "catalogs":
        if args.catalogs_command == "list":
            return command_catalogs_list(args.registry)
        if args.catalogs_command == "fetch":
            return command_catalogs_fetch(args.name, args.registry)
    elif args.command == "fetch-url":
        return command_fetch_url(args.url, args.name, args.format)
    elif args.command == "vizier-fetch":
        return command_vizier_fetch(args.catalog_id, args.name, args.row_limit)

    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
