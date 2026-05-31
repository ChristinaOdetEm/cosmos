# CEERS vs ASTRODEEP Redshift Comparison

Created: 2026-05-31

## Dataset

| Metric | CEERS | ASTRODEEP Abell 2744 |
| --- | ---: | ---: |
| Row count | 82547 | 42491 |
| Column count | 9 | 9 |
| `zphot` missing | 0 | 77 |
| `zspec` missing | 78870 | 41250 |
| `zphot` available | 82547 | 42414 |
| `zspec` available | 3677 | 1241 |

## Distribution

- Histogram artifacts:
  - CEERS count histogram: `outputs/figures/ceers_jwst_zphot_distribution.png`
  - CEERS normalized histogram: `outputs/figures/ceers_jwst_zphot_distribution_normalized.png`
  - ASTRODEEP count histogram: `outputs/figures/astrodeep_jwst_zphot_distribution.png`
  - ASTRODEEP sample-vs-full comparison figure: `outputs/figures/astrodeep_jwst_zphot_sample_vs_full.png`
- Summary statistics:

| Metric | CEERS | ASTRODEEP Abell 2744 |
| --- | ---: | ---: |
| Mean `zphot` | 3.149182 | 2.592796 |
| Median `zphot` | 2.300000 | 2.000000 |
| Std `zphot` | 2.783018 | 2.526642 |
| Min `zphot` | 0.025000 | 0.025000 |
| Max `zphot` | 20.000000 | 20.000000 |

- Fitted exponential baselines:

| Metric | CEERS | ASTRODEEP Abell 2744 |
| --- | ---: | ---: |
| Equation | `count(z) = 13499.303538 * exp(-0.369723 * z)` | `count(z) = 5460.351640 * exp(-0.368615 * z)` |
| `A` | 13499.303537689913 | 5460.351639904487 |
| `k` | 0.3697230576443244 | 0.3686147062538369 |
| `R^2` count scale | 0.8312035156340162 | 0.8268113056697733 |
| `R^2` log scale | 0.8075773630348152 | 0.8024170456830859 |
| `RMSE` | 1252.5563299852672 | 746.898901805878 |

- Residual artifacts:
  - CEERS residuals: `outputs/figures/ceers_jwst_zphot_residuals.png`
  - CEERS fitted curve: `outputs/figures/ceers_jwst_zphot_fit.png`

## Replication Questions

- Does CEERS exhibit a similar exponential decay?
- Are residual structures observed in similar redshift ranges?
- Is high-redshift behavior comparable?
- Does `zspec` coverage differ significantly?
