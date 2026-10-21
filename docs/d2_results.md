# D2 · Reference TLF reproduction

Environment: R 4.6.1 (arm64), current CRAN packages (renv.lock); original run used R 4.1.3, CRAN snapshot 2021-08-31.

| Output | Ran? | Numbers match original? | Notes |
|---|---|---|---|
| 14-2.01 Demographics | Yes | Yes (all values) | Format only: separators, decimals padded (76 → 76.00), alignment, timestamp |
| 14-3.01 ADAS-Cog ANCOVA | Yes | Yes (IDENTICAL text) | Needed striprtf; macOS textutil cannot read pharmaRTF output |
| 14-3.02 Glucose ANCOVA | Yes | Yes (IDENTICAL text) | |
| Figure 14-1 KM | Yes | Yes (numbers at risk identical) | visR update: legend title/labels changed; High/Low dose colors swapped |

Code changes needed:
- None to the programs. Runner must setwd() into the pilot repo: pilot1wrappers' startup.R searches upward for DESCRIPTION (infinite loop otherwise).
- visR not on CRAN; installed from GitHub (openpharma/visR 0.4.1).

Lessons for the comparator (D5):
1. Text diff is unreliable: identical numbers produced 33 "different" lines in 14-2.01.
2. Figures must be checked via underlying numbers and group-to-color mapping, not visually.

Hidden details the data profile must include (D7):
- 14-2.01: ITTFL
- 14-3.01: EFFFL + ITTFL + PARAMCD == "ACTOT" + ANL01FL == "Y"; model CHG ~ TRTPN + SITEGR1 + BASE
- 14-3.02: TRTPN %in% c(0, 81) only (Placebo vs High); AVISITN == 20; model CHG ~ BASE + TRTPN
- Figure 14-1: SAFFL; PARAMCD == "TTDE"; CNSR
