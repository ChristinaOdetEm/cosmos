# JADES vs CEERS vs ASTRODEEP

Created: 2026-05-31

## Dataset Scale

| Metric | ASTRODEEP Abell 2744 | CEERS | JADES DR5 |
| --- | ---: | ---: | ---: |
| Row count | 42491 | 82547 | 485510 |
| Column count | 9 | 9 | 41 |
| Primary photometric redshift field | `zphot` | `zphot` | `z_a` |
| Photometric redshift available | 42414 | 82547 | 485510 |
| Spectroscopic redshift available | 1241 | 3677 | 3696 |

## Redshift Distribution

- Histogram shape:
  - ASTRODEEP peaks in the `z = 0.0` to `0.5` bin with `8219` counts.
  - CEERS peaks in the `z = 1.0` to `1.5` bin with `10577` counts.
  - JADES peaks in the `z = 0.0` to `0.5` bin with `69741` counts.
- Summary statistics:

| Metric | ASTRODEEP Abell 2744 | CEERS | JADES DR5 |
| --- | ---: | ---: | ---: |
| Mean | 2.592796 | 3.149182 | 2.777003 |
| Median | 2.000000 | 2.300000 | 2.180000 |
| Std | 2.526642 | 2.783018 | 2.608299 |
| Min | 0.025000 | 0.025000 | 0.010000 |
| Max | 20.000000 | 20.000000 | 21.990000 |

- Fitted exponential baselines:

| Metric | ASTRODEEP Abell 2744 | CEERS | JADES DR5 |
| --- | ---: | ---: | ---: |
| Equation | `count(z) = 5460.351640 * exp(-0.368615 * z)` | `count(z) = 13499.303538 * exp(-0.369723 * z)` | `count(z) = 69735.872929 * exp(-0.354353 * z)` |
| `A` | 5460.3516399044875 | 13499.303537689913 | 69735.87292877467 |
| `k` | 0.3686147062538369 | 0.3697230576443244 | 0.3543527039468166 |
| `R^2` count scale | 0.8268113076532897 | 0.8312035499918469 | 0.928467701477361 |
| `R^2` log scale | 0.8024170528122591 | 0.8075773639616397 | 0.9204017739196801 |
| `RMSE` | 746.8988975287913 | 1252.5562025089143 | 5084.04264864352 |

- Residual structure:
  - ASTRODEEP largest positive residual: bin center `0.25`, residual `3239.350586`; largest negative residual: bin center `4.25`, residual `-267.854492`.
  - CEERS largest positive residual: bin center `1.75`, residual `3300.680176`; largest negative residual: bin center `0.25`, residual `-4326.481445`.
  - JADES largest positive residual: bin center `1.75`, residual `15439.375000`; largest negative residual: bin center `7.75`, residual `-1544.888672`.

## Diagnostic Regions

| Region | ASTRODEEP Abell 2744 | CEERS | JADES DR5 |
| --- | ---: | ---: | ---: |
| `z ~= 0` | 8373 | 8246 | 69741 |
| `z ~= 6-8` | 2680 | 7970 | 29414 |
| `z ~= 14-16` | 29 | 39 | 1080 |
| `z > 16` | 239 | 422 | 2777 |

## Artifacts

- ASTRODEEP histogram: `outputs/figures/astrodeep_jwst_zphot_distribution.png`
- CEERS histogram: `outputs/figures/ceers_jwst_zphot_distribution.png`
- CEERS normalized histogram: `outputs/figures/ceers_jwst_zphot_distribution_normalized.png`
- CEERS fit: `outputs/figures/ceers_jwst_zphot_fit.png`
- CEERS residuals: `outputs/figures/ceers_jwst_zphot_residuals.png`
- JADES histogram: `outputs/figures/jades_dr5_z_a_distribution.png`
- JADES normalized histogram: `outputs/figures/jades_dr5_z_a_distribution_normalized.png`
- JADES fit: `outputs/figures/jades_dr5_z_a_fit.png`
- JADES residuals: `outputs/figures/jades_dr5_z_a_residuals.png`
