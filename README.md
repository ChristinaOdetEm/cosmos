# JWST Galaxy Analysis Foundation

This repository is a reproducible starting point for working with public galaxy catalogs in a JWST-focused workflow. It is intentionally scoped to catalog acquisition, provenance, exploratory redshift analysis, and replication-oriented reporting. It does **not** search for anomalies yet.

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
|   |-- manifests/
|   `-- reports/
|-- research/
|   |-- observations/
|   |-- notes/
|   |-- questions/
|   `-- validations/
|-- src/jwst_galaxy_analysis/
|   |-- cli.py
|   |-- config.py
|   |-- datasets.py
|   |-- io.py
|   |-- provenance.py
|   |-- redshift.py
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
- Cross-catalog summaries and replication writeups should be saved under `outputs/reports/`.
- Observation and methodology records should be written under `research/`.

## Catalog ingestion

The foundation supports public catalog loading from:

- direct file URLs (`csv`, `tsv`, `parquet`, `fits`)
- VizieR catalog identifiers through `astroquery`
- a local YAML registry in `catalog_sources.yml`
- custom multi-file adapters for public releases that need region combination or cross-release joins

Example commands:

```powershell
jwst-galaxy catalogs list
jwst-galaxy catalogs fetch astrodeep_jwst --registry catalog_sources.yml
jwst-galaxy catalogs fetch ceers_jwst --registry catalog_sources.yml
jwst-galaxy catalogs fetch jades_dr5 --registry catalog_sources.yml
```

The current registry includes:

- `astrodeep_jwst`: ASTRODEEP-JWST Abell 2744 catalog from VizieR `J/A+A/691/A240/a2744p`
- `ceers_jwst`: CEERS catalog from VizieR `J/A+A/691/A240/ceersp`
- `jades_dr5`: combined JADES DR5 GOODS-S and GOODS-N photometric catalogs with public DR4 spectroscopic matches by `NIRCam_DR5_ID`

The JADES adapter preserves the raw DR5 region files and the raw DR4 spectroscopic catalog, then materializes a combined processed parquet for downstream analysis.

## Current outputs

The repository currently contains three JWST redshift baselines:

- ASTRODEEP
- CEERS
- JADES

Key replication artifacts include:

- `research/observations/OBS-005.md` and `OBS-006.md` for CEERS
- `research/observations/OBS-007.md` and `OBS-008.md` for JADES
- `outputs/reports/ceers_vs_astrodeep_redshift_comparison.md`
- `outputs/reports/jades_vs_ceers_vs_astrodeep.md`

## Next foundation steps

- add tests around catalog adapters and transformation manifests
- standardize a schema for photometry, redshift, and morphology columns

## License

This repository's code is released under the MIT License. See [LICENSE](LICENSE).

External datasets are not automatically covered by the repository license. Each public catalog should be checked and documented according to its own usage terms before redistribution.
