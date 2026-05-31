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

### 2026-05-31 22:06 Europe/Warsaw

- Agent: `Codex`
- Commit: `1b34ec1`
- Summary: Added a cross-catalog diagnostic note comparing selected `zphot` regions in ASTRODEEP-JWST and CEERS-JWST, including counts, flag concentration, spectroscopic coverage, and repeated-value behavior.
- Reason: Record descriptive catalog and photo-z reliability diagnostics for sparse redshift regions without moving into interpretation.

- Files:
  - `research/notes/NOTE-002.md`
  - `agent_handoff.md`

- Next:
  - Reuse this note as a descriptive baseline before adding any further cross-catalog validation records.
  - Keep follow-up work framed as catalog diagnostics unless a new question explicitly expands scope.

### 2026-05-31 21:07 Europe/Warsaw

- Agent: `Codex`
- Commit: `1e05247`
- Summary: Added the CEERS replication baseline by selecting a public CEERS photo-z catalog with documented provenance, ingesting the full dataset, creating acquisition and distribution observations, fitting the same exponential baseline model, and writing the first CEERS-vs-ASTRODEEP comparison report.
- Reason: Establish an independent JWST-field replication baseline before expanding beyond the ASTRODEEP Abell 2744 characterization.

- Files:
  - `.gitignore`
  - `catalog_sources.yml`
  - `data/raw/ceers_jwst.fits`
  - `data/processed/ceers_jwst.parquet`
  - `outputs/manifests/ceers_jwst.manifest.json`
  - `outputs/manifests/ceers_jwst_01.manifest.json`
  - `outputs/manifests/ceers_jwst_02.manifest.json`
  - `outputs/figures/ceers_jwst_zphot_distribution.png`
  - `outputs/figures/ceers_jwst_zphot_distribution_normalized.png`
  - `outputs/figures/ceers_jwst_zphot_fit.png`
  - `outputs/figures/ceers_jwst_zphot_residuals.png`
  - `outputs/reports/ceers_vs_astrodeep_redshift_comparison.md`
  - `research/observations/OBS-005.md`
  - `research/observations/OBS-006.md`
  - `agent_handoff.md`

- Next:
  - Use the CEERS and ASTRODEEP baselines for replication-only follow-up without promoting descriptive differences into hypotheses.

### 2026-05-31 20:48 Europe/Warsaw

- Agent: `Codex`
- Commit: `38bae52`
- Summary: Added the first methodological note capturing the completed ASTRODEEP sample-to-full replication lesson, including the distribution shift, fitted exponential summary, and replication takeaways.
- Reason: Preserve the first completed replication exercise as a reusable methodological reference before adding a second catalog.

- Files:
  - `research/notes/NOTE-001.md`
  - `agent_handoff.md`

- Next:
  - Reuse the note when evaluating whether future sample-based structures survive full-catalog replication.

### 2026-05-31 20:38 Europe/Warsaw

- Agent: `Codex`
- Commit: `90725b5`
- Summary: Generated a shared-bin `zphot` histogram comparison figure for the preserved 250-row sample and the full ASTRODEEP catalog, and linked the artifact into the full-ingest observation and report.
- Reason: Add a direct visual comparison between the sample and full `zphot` distributions without changing the underlying datasets.

- Files:
  - `.gitignore`
  - `outputs/figures/astrodeep_jwst_zphot_sample_vs_full.png`
  - `outputs/reports/astrodeep_jwst_sample_vs_full_report.md`
  - `research/observations/OBS-004.md`
  - `agent_handoff.md`

- Next:
  - Reuse the shared-bin comparison artifact when discussing sample-versus-full distribution differences.

### 2026-05-31 20:31 Europe/Warsaw

- Agent: `Codex`
- Commit: `218852b`
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
