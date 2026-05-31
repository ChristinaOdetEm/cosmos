# Research Provenance Framework

This layer tracks research reasoning from assumption -> question -> observation -> pattern -> hypothesis -> validation.

It is intentionally lightweight. The purpose is reproducibility of reasoning, not process overhead.

External agents tracking repository changes should also read [../agent_handoff.md](../agent_handoff.md).

## Workflow

Assumption
|
v
Question
|
v
Observation
|
v
Pattern
|
v
Hypothesis
|
v
Validation

1. Start with an assumption record in `assumptions/` when a working foundation needs to be made explicit.
2. Define or refine a question record in `questions/`.
3. Add observations in `observations/` for things directly seen in the data.
4. Promote recurring relationships into patterns in `patterns/`.
5. Form falsifiable hypotheses in `hypotheses/`.
6. Record tests and outcomes in `validations/`.

Assumptions are not facts. They are currently accepted foundations that can later be challenged, replaced, or retired.

## Linking Rules

- Questions may link to questions and observations.
- Observations may link to questions and patterns.
- Patterns may link to observations and hypotheses.
- Hypotheses may link to patterns and validations.
- Validations may link only to hypotheses.

## Conventions

- Use one markdown file per record.
- Keep IDs stable once assigned.
- Treat assumptions as explicit working foundations, not proven truths.
- Keep observations descriptive and non-interpretive.
- Mark illustrative examples clearly so they are not confused with active findings.

## Layout

```text
research/
|-- assumptions/
|   |-- TEMPLATE.md
|   |-- A-001.md
|   |-- A-002.md
|   |-- A-003.md
|   `-- A-004.md
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
