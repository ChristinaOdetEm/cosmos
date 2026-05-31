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
