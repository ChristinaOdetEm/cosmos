# Agent Handoff Log

This file is the shared handoff surface for external agents tracking repository changes.

## Active Assumptions

- `A-001` Public galaxy catalogs are sufficient for initial exploration
- `A-002` Questions drive analysis
- `A-003` No anomaly claims without baseline characterization
- `A-004` Reproducibility is more important than discovery speed

Future agents should review assumptions before proposing analyses or interpretations.

## How To Use

- Read the latest entry first.
- Treat commit hashes as the source of truth for the exact change set.
- Use `git show <commit>` for full implementation details.
- Keep entries short and factual.

## Entry Template

### YYYY-MM-DD HH:MM TZ

- Agent: `Codex`
- Commit: `<hash>`
- Summary: `<what changed>`
- Reason: `<why it changed>`

- Files:
  - `path/to/file`

- Next:
  - `<recommended follow-up>`

## Entries

### 2026-05-31 20:31 Europe/Warsaw

- Agent: `Codex`
- Commit: `<pending>`
- Summary: Replaced the main ASTRODEEP 250-row sample ingest with the full 42,491-row table, preserved the original sample artifacts under `_sample_250` names, and added a sample-vs-full comparison report plus a new full-ingest observation record.
- Reason: The repository needed the complete ASTRODEEP catalog as the primary dataset while keeping the earlier sample-based observations reproducible and comparable.

- Files:
  - `catalog_sources.yml`
  - `.gitignore`
  - `data/raw/astrodeep_jwst.fits`
  - `data/raw/astrodeep_jwst_sample_250.fits`
  - `data/processed/astrodeep_jwst.parquet`
  - `data/processed/astrodeep_jwst_sample_250.parquet`
  - `outputs/manifests/astrodeep_jwst.manifest.json`
  - `outputs/manifests/astrodeep_jwst_01.manifest.json`
  - `outputs/manifests/astrodeep_jwst_02.manifest.json`
  - `outputs/manifests/astrodeep_jwst_sample_250.manifest.json`
  - `outputs/manifests/astrodeep_jwst_sample_250_01.manifest.json`
  - `outputs/manifests/astrodeep_jwst_sample_250_02.manifest.json`
  - `outputs/reports/astrodeep_jwst_sample_vs_full_report.md`
  - `research/observations/OBS-001.md`
  - `research/observations/OBS-002.md`
  - `research/observations/OBS-003.md`
  - `research/observations/OBS-004.md`
  - `agent_handoff.md`

- Next:
  - Use the full `astrodeep_jwst` artifacts for future analysis unless a sample-specific comparison is required.
  - Keep sample-derived observations tied to the preserved `_sample_250` artifacts.

### 2026-05-31 20:17 Europe/Warsaw

- Agent: `Codex`
- Commit: `1629234`
- Summary: Added `OBS-003` for the `zphot > 10` subset, including a sorted object table plus scatter and multi-bin histogram outputs generated from the processed ASTRODEEP-JWST catalog.
- Reason: Record the high-`zphot` subset descriptively and preserve the exact visualization outputs used to inspect the apparent gap without adding interpretation.

- Files:
  - `outputs/figures/astrodeep_jwst_zphot_gt10_scatter.png`
  - `outputs/figures/astrodeep_jwst_zphot_gt10_histograms.png`
  - `research/observations/OBS-003.md`
  - `research/validations/VAL-100.md`
  - `agent_handoff.md`

- Next:
  - Keep future follow-up on this subset descriptive unless a new question or validation explicitly changes scope.

### 2026-05-31 20:02 Europe/Warsaw

- Agent: `Codex`
- Commit: `ce9cdc4`
- Summary: Generated the first validation output for `VAL-100` from the processed ASTRODEEP-JWST catalog, saved a `zphot` histogram, and recorded the observed summary statistics and missing-value counts in a new observation record.
- Reason: Establish a descriptive validation baseline for redshift completeness and distribution before any higher-level analysis.

- Files:
  - `outputs/figures/astrodeep_jwst_zphot_distribution.png`
  - `research/observations/OBS-002.md`
  - `research/validations/VAL-100.md`
  - `agent_handoff.md`

- Next:
  - Preserve the validation outputs as the baseline reference for future redshift-focused checks.
  - Avoid interpretation beyond descriptive catalog properties unless a new question or validation requires it.

### 2026-05-31 19:43 Europe/Warsaw

- Agent: `Codex`
- Commit: `7b9cd13`
- Summary: Shifted the research records from framework-building to evidence-building by defining the first active question, first candidate data-quality pattern, and first planned validation around the ASTRODEEP-JWST Abell 2744 redshift sample.
- Reason: The initial dataset contains redshift fields but not galaxy mass fields, so the active research set needed to align with the available evidence before further analysis.

- Files:
  - `research/observations/OBS-001.md`
  - `research/questions/Q-001.md`
  - `research/questions/Q-002.md`
  - `research/questions/Q-003.md`
  - `research/questions/Q-100.md`
  - `research/patterns/PAT-001.md`
  - `research/patterns/PAT-100.md`
  - `research/validations/VAL-100.md`
  - `agent_handoff.md`

- Next:
  - Validate whether `zphot` coverage and distribution support exploratory analysis.
  - Document the limitations introduced by the near-absence of `zspec`.

### 2026-05-31 19:10 Europe/Warsaw

- Agent: `Codex`
- Commit: `2544bdc`
- Summary: Added a lightweight research provenance framework under `research/` with staged record types for questions, observations, patterns, hypotheses, and validations.
- Reason: Create a reproducible reasoning layer without changing the existing data pipeline.

- Files:
  - `research/README.md`
  - `research/questions/TEMPLATE.md`
  - `research/questions/Q-001.md`
  - `research/questions/Q-002.md`
  - `research/questions/Q-003.md`
  - `research/observations/TEMPLATE.md`
  - `research/observations/OBS-001.md`
  - `research/patterns/TEMPLATE.md`
  - `research/patterns/PAT-001.md`
  - `research/hypotheses/TEMPLATE.md`
  - `research/hypotheses/HYP-001.md`
  - `research/validations/TEMPLATE.md`
  - `research/validations/VAL-001.md`
  - Removed `research/questions.md`

- Next:
  - Add new provenance records by extending the numbered files in each folder.
  - Update this handoff log after each meaningful repo change.
