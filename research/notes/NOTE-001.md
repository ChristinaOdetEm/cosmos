# Research Note

- ID: NOTE-001
- Title: First Sample-to-Full Catalog Replication Review
- Purpose: Capture what changed when the analysis moved from a 250-row sample to the full 42,491-row catalog.
- Status: Validated
- Created: 2026-05-31

## Initial Observations

- Apparently distinct drops were observed in the sample distribution around `z ~= 2.5` and `z ~= 7.5`.
- A high-redshift separation appeared visible in the sample histogram.
- The sample appeared skewed toward higher redshift values.

## Full Catalog Findings

- Full dataset size: `42,491` rows.
- Sample represented approximately `0.588%` of the full catalog.
- Mean `zphot` shifted from approximately `3.87` to `2.59`.
- Median `zphot` shifted from approximately `3.2` to `2.0`.
- The overall distribution remained strongly right-skewed.
- Several apparent sample structures weakened substantially when the full catalog was analyzed.

## Mathematical Characterization

- Fitted exponential model:

```text
count(z) = 5460.351640 * exp(-0.368615 * z)
```

- `R^2` on count scale: `0.826811307653`
- `R^2` on log scale: `0.802417053685`
- `RMSE`: `746.898897528791`

## Lessons Learned

- Visual patterns in small samples require replication.
- Histogram structure can change significantly with sample size.
- Full-catalog analysis should be preferred whenever practical.
- Candidate observations should not be treated as patterns until replication is attempted.
