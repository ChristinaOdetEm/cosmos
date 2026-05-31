# ASTRODEEP Sample vs Full Comparison Report

Created: 2026-05-31

## Scope

This report compares the preserved 250-row ASTRODEEP-JWST Abell 2744 sample snapshot against the full `J/A+A/691/A240/a2744p` table ingested into the main repository artifacts.

- Preserved sample raw artifact: `data/raw/astrodeep_jwst_sample_250.fits`
- Preserved sample processed artifact: `data/processed/astrodeep_jwst_sample_250.parquet`
- Full raw artifact: `data/raw/astrodeep_jwst.fits`
- Full processed artifact: `data/processed/astrodeep_jwst.parquet`

## Size Comparison

| Metric | Preserved Sample | Full Dataset |
| --- | ---: | ---: |
| Rows | 250 | 42491 |
| Columns | 9 | 9 |
| Unique IDs | 250 | 42491 |
| Raw file size (bytes) | 25920 | 1886400 |
| Processed file size (bytes) | 15964 | 1438535 |

## Missing Values

| Metric | Preserved Sample | Full Dataset |
| --- | ---: | ---: |
| `zphot` missing | 1 | 77 |
| `zspec` missing | 248 | 41250 |

## `zphot` Summary

| Metric | Preserved Sample | Full Dataset |
| --- | ---: | ---: |
| Count | 249 | 42414 |
| Mean | 3.872514 | 2.592796 |
| Median | 3.200000 | 2.000000 |
| Std | 3.777501 | 2.526642 |
| Min | 0.050000 | 0.025000 |
| Max | 19.850000 | 20.000000 |

## Row Relationship Checks

| Check | Result |
| --- | --- |
| Preserved sample IDs are a subset of full dataset IDs | `True` |
| Overlapping IDs | 250 |
| IDs present only in full dataset | 42241 |
| First 250 ID sequence matches full dataset head | `True` |
| Preserved sample share of full dataset | 0.588360% |

## Artifact Notes

- The full ingest replaced the main `astrodeep_jwst` raw and processed artifacts.
- The original 250-row sample artifacts were preserved under `_sample_250` filenames for reproducibility.
