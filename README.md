# JWST Galaxy Analysis Foundation

This repository is a reproducible starting point for working with public galaxy catalogs in a JWST-focused workflow. It is intentionally scoped to project setup, ingestion, provenance, and exploratory analysis. It does **not** search for anomalies yet.

## Goals

- reproducible Python environment
- clear folder structure
- public catalog ingestion utilities
- exploratory analysis notebooks
- documented transformations
- reproducible outputs

## Project layout

```text
.
|-- data/
|   |-- raw/
|   |-- interim/
|   `-- processed/
|-- notebooks/
|   |-- 00_project_overview.ipynb
|   `-- 01_catalog_eda_template.ipynb
|-- outputs/
|   |-- figures/
|   `-- manifests/
|-- src/jwst_galaxy_analysis/
|   |-- cli.py
|   |-- config.py
|   |-- datasets.py
|   |-- io.py
|   |-- provenance.py
|   `-- transforms.py
|-- catalog_sources.yml
`-- pyproject.toml
```

## Quick start

1. Create a virtual environment:

   ```powershell
   py -3.14 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install the project in editable mode:

   ```powershell
   python -m pip install --upgrade pip
   pip install -e .[dev]
   ```

3. Inspect the sample catalog registry:

   ```powershell
   jwst-galaxy catalogs list
   ```

4. Start Jupyter:

   ```powershell
   jupyter lab
   ```

## Reproducibility conventions

- Raw downloads are stored under `data/raw/`.
- Cleaned tables are written to `data/processed/` as Parquet.
- Each transformation writes a JSON manifest under `outputs/manifests/`.
- Each dataset write includes row counts, column names, hashes, timestamps, and transformation metadata.
- Notebook work should save durable outputs to `outputs/figures/` or `data/processed/`, not only to notebook state.

## Catalog ingestion

The foundation supports public catalog loading from:

- direct file URLs (`csv`, `tsv`, `parquet`, `fits`)
- VizieR catalog identifiers through `astroquery`
- a local YAML registry in `catalog_sources.yml`

Example commands:

```powershell
jwst-galaxy catalogs list
jwst-galaxy catalogs fetch demo_local --registry catalog_sources.yml
jwst-galaxy fetch-url "https://example.org/catalog.csv" --name example_catalog
jwst-galaxy vizier-fetch "J/ApJS/264/35/catalog" --name example_vizier
```

Replace the example identifiers with the public galaxy catalogs we decide to prioritize next.

The first registered real catalog is `astrodeep_jwst`, sourced from VizieR catalog `J/A+A/691/A240` with a small sample row limit for initial validation.

## Next foundation steps

- choose the first real public JWST-related catalogs to register
- add tests around catalog adapters and transformation manifests
- standardize a schema for photometry, redshift, and morphology columns
