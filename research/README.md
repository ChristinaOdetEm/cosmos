# Research Provenance Framework

This layer tracks research reasoning from question -> observation -> pattern -> hypothesis -> validation.

It is intentionally lightweight. The purpose is reproducibility of reasoning, not process overhead.

## Workflow

1. Start with a question record in `questions/`.
2. Add observations in `observations/` for things directly seen in the data.
3. Promote recurring relationships into patterns in `patterns/`.
4. Form falsifiable hypotheses in `hypotheses/`.
5. Record tests and outcomes in `validations/`.

## Linking Rules

- Questions may link to questions and observations.
- Observations may link to questions and patterns.
- Patterns may link to observations and hypotheses.
- Hypotheses may link to patterns and validations.
- Validations may link only to hypotheses.

## Conventions

- Use one markdown file per record.
- Keep IDs stable once assigned.
- Keep observations descriptive and non-interpretive.
- Mark illustrative examples clearly so they are not confused with active findings.

## Layout

```text
research/
|-- questions/
|   |-- TEMPLATE.md
|   `-- Q-001.md
|-- observations/
|   |-- TEMPLATE.md
|   `-- OBS-001.md
|-- patterns/
|   |-- TEMPLATE.md
|   `-- PAT-001.md
|-- hypotheses/
|   |-- TEMPLATE.md
|   `-- HYP-001.md
`-- validations/
    |-- TEMPLATE.md
    `-- VAL-001.md
```
