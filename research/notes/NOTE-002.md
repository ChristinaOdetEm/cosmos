# Research Note

- ID: NOTE-002
- Title: Cross-Catalog Redshift Sparsity Diagnostics
- Purpose: Compare selected `zphot` regions in the processed ASTRODEEP-JWST and CEERS-JWST catalogs as catalog and photo-z reliability diagnostics.
- Status: Documented
- Created: 2026-05-31

## Scope

- Catalogs:
  - `data/processed/astrodeep_jwst.parquet`
  - `data/processed/ceers_jwst.parquet`
- `zphot` regions inspected:
  - `0.0-0.5`
  - `14.0-16.0`
  - `16.0-18.5`

## ASTRODEEP-JWST

- `0.0-0.5`
  - Object count: `8,219`
  - `zspec` available: `395`
  - Most frequent flags: `16:631`, `12:574`, `312:483`, `316:460`, `311:324`, `18:322`, `11:307`, `2:296`
  - Repeated `zphot` values are present. Most frequent values: `0.250:810`, `0.200:770`, `0.275:765`, `0.025:754`, `0.225:717`, `0.300:472`, `0.050:450`, `0.100:396`
  - Rounded-value counts: `1,785` values align with `0.1` steps and `3,793` values align with `0.05` steps
- `14.0-16.0`
  - Object count: `29`
  - `zspec` available: `0`
  - Most frequent flags: `16:6`, `116:3`, `27:2`, `326:2`, `28:2`; additional single-count flags include negative and high-valued codes
  - Repeated `zphot` values are limited but present. Most frequent values: `15.975:2`, `15.400:2`, `14.300:2`, `15.700:2`, `14.700:2`, `14.725:2`
  - Rounded-value counts: `11` values align with `0.1` steps and `15` values align with `0.05` steps
- `16.0-18.5`
  - Object count: `123`
  - `zspec` available: `0`
  - Most frequent flags: `16:12`, `100027:10`, `100028:9`, `100016:8`, `28:5`, `18:5`, `12:4`, `-26:3`
  - Repeated `zphot` values are present. Most frequent values: `17.300:10`, `17.400:8`, `17.275:7`, `17.350:6`, `16.925:6`, `17.200:5`, `17.175:4`, `17.375:4`
  - Rounded-value counts: `42` values align with `0.1` steps and `69` values align with `0.05` steps

## CEERS-JWST

- `0.0-0.5`
  - Object count: `7,981`
  - `zspec` available: `415`
  - Most frequent flags: `14:3089`, `314:1582`, `114:758`, `13:527`, `313:291`, `113:149`, `44:114`, `34:109`
  - Repeated `zphot` values are present. Most frequent values: `0.025:1587`, `0.200:685`, `0.275:427`, `0.075:420`, `0.325:420`, `0.350:389`, `0.225:362`, `0.050:361`
  - Rounded-value counts: `1,513` values align with `0.1` steps and `3,177` values align with `0.05` steps
- `14.0-16.0`
  - Object count: `38`
  - `zspec` available: `0`
  - Most frequent flags: `-14:6`, `14:4`, `100014:4`, `100064:3`, `100314:2`, `-114:2`, `100113:2`; additional single-count flags are also present
  - Repeated `zphot` values are limited but present. Most frequent values: `15.525:3`, `15.775:3`, `14.600:3`, `14.650:3`, `15.850:2`
  - Rounded-value counts: `7` values align with `0.1` steps and `19` values align with `0.05` steps
- `16.0-18.5`
  - Object count: `336`
  - `zspec` available: `0`
  - Most frequent flags: `100044:55`, `-14:44`, `100014:44`, `100064:13`, `-44:13`, `100024:12`, `14:11`, `100344:10`
  - Repeated `zphot` values are present. Most frequent values: `17.550:18`, `17.350:17`, `17.300:17`, `17.225:15`, `17.600:14`, `17.575:14`, `17.275:12`, `17.325:11`
  - Rounded-value counts: `77` values align with `0.1` steps and `175` values align with `0.05` steps

## Cross-Catalog Comparison

- The `14.0-16.0` region is sparse in both catalogs:
  - ASTRODEEP-JWST: `29`
  - CEERS-JWST: `38`
- The `16.0-18.5` region is also sparse relative to the `0.0-0.5` region in both catalogs, but it is not empty:
  - ASTRODEEP-JWST: `123`
  - CEERS-JWST: `336`
- None of the inspected regions are empty in either catalog.
- `zspec` availability is present in the `0.0-0.5` region in both catalogs and absent in the `14.0-16.0` and `16.0-18.5` regions in both catalogs.
- Repeated `zphot` values appear in all inspected regions in both catalogs.
- Rounded `zphot` values aligned to `0.05` increments appear in all inspected regions in both catalogs.
