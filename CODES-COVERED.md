# Codes Covered

What's actually in `vault/02 - Civil Engineering/` right now, which edition, how deep, and what to double-check before relying on it. This list is only as current as its last update — check the date at the bottom.

**Every code here has been read in full (not sampled) and audited** — the note was re-checked against its own source PDF at least once after the initial build, and any dense/multi-column table was verified against a rendered page image, not just linear text extraction. See each note's own header for its specific audit findings.

## ⚠️ Known edition gaps — verify before relying on these for real design work

Three codes here are **not confirmed to be the current BIS edition**. The gap isn't a build mistake — these editions just aren't in the source library this project was built from. Check BIS's official portal (see README) for the current edition before using these for anything load-bearing.

| Code | Edition here | Suspected current edition | Notes |
|---|---|---|---|
| **IS 13920** (Ductile Detailing for Seismic Forces) | 1993 (amended 2002) | 2016 (Second Revision) | Confirmed the 2016 edition is genuinely not in the source library (not a filename mix-up). |
| **IS 1893 Part 1** (Earthquake Resistant Design) | 2002 (Fourth Revision) | 2016 (Sixth Revision) | A materially different seismic design basis, not a minor update. Checked the library specifically for a hidden 2016 copy — not there. |
| **IS 875 Part 3** (Wind Loads) | 1987 | 2015 (Third Revision) | Revised wind speed maps and methodology. Not sourced yet. |

## Full list

| Code | Edition | Sl. key (for `sources.json`) | Coverage |
|---|---|---|---|
| **NBC 2026** (National Building Construction Standards, SP 7:2026) | 4th Revision — current | `NBC2026` | All 21 Sections + cross-cutting Topic Index. Part F (Fire & Life Safety) additionally converted into structured rule tables (parameter/condition/threshold/source), including every Annex. |
| **IS 456** (Plain and Reinforced Concrete) | 2000 | `IS456` | Full code — materials, durability, general design, reinforcement/detailing (Cl 26), special members, limit state design. |
| **IS 875 Part 1** (Dead Loads) | 1987 | `IS875_1` | Full part. |
| **IS 875 Part 2** (Imposed Loads) | 1987 | `IS875_2` | Full part — occupancy floor loads (the most-used table in the set) rebuilt from word-level PDF coordinates after the audit found the linear extraction had scrambled it. |
| **IS 875 Part 3** (Wind Loads) | 1987 — ⚠️ see gap above | `IS875_3` | Full methodology (Vz → design pressure → coefficients); the dozens of shape-specific pressure-coefficient tables are reference-by-page, not transcribed (too geometry-dependent to compress safely). |
| **IS 875 Part 4** (Snow Loads) | 1987 | `IS875_4` | Full part (niche — J&K/HP/UP hill districts only; ground snow load values require IMD/DRDO data, not in the code itself). |
| **IS 875 Part 5** (Special Loads & Load Combinations) | 1987 | `IS875_5` | Full part. |
| **IS 1893 Part 1** (Earthquake Resistant Design) | 2002 — ⚠️ see gap above | `IS1893_1` | Full part. Zone-factor town list (Annex E) left reference-by-page (multi-column extraction risk). |
| **IS 13920** (Ductile Detailing for Seismic Forces) | 1993 + 2002 amendment — ⚠️ see gap above | `IS13920` | Full code including Annex A shear-wall flexural-strength procedure. |
| **SP 16** (Design Aids for Reinforced Concrete) | 1980 | `SP16` | Navigation guide, not full transcription — it's a chart/table lookup book (92 charts, 98 tables), not a rulebook. Small formulas/tables transcribed and cross-checked against IS 456; large numeric grids left reference-by-page. |
| **SP 34** (Handbook on Concrete Reinforcement and Detailing) | 1987 | `SP34` | Sections 1, 4, 5 in full depth; Sections 7, 9 sampled for standout rules; rest reference-by-page. Flags a real conflict: SP 34's column tie-diameter (5mm) is superseded by IS 456:2000's 16mm — IS 456 governs. |
| **IS 1200** (Method of Measurement, all 28 parts) | Various, 1971–1994 per part | `IS1200_1` … `IS1200_28` | Full depth, all 28 parts (BOQ/billing measurement rules, one part per trade). |
| **IS 800** (General Construction in Steel) | 2007 (3rd Revision) + Amendment 1 (2012) | `IS800` | Full code, all 17 Sections + Annexes A–H. The *only* current edition — the source library also holds the superseded 1984 working-stress edition; this project is built from 2007. |

## Telangana state building/development orders

Separate from the BIS codes above — these are Telangana Municipal Administration & Urban Development Dept. government orders, not national standards. Live in `vault/02 - Civil Engineering/Telangana Building Rules/`.

| Code | Edition | Sl. key (for `sources.json`) | Coverage |
|---|---|---|---|
| **G.O.Ms.No.168** (Telangana/Andhra Pradesh Building Rules, 2012) | 2012 base + 11 amendment G.O.s through 2026, all incorporated inline | `GO168` (base), `GO168_Amdt342_2013`, `GO168_Amdt7_2016`, `GO168_Amdt135_2017`, `GO168_Amdt50_2019`, `GO168_Amdt264_2019`, `GO168_Amdt62_2020`, `GO168_Amdt103_2021`, `GO168_Memo5544_2022`, `GO168_Amdt52_2022`, `GO168_Amdt235_2022`, `GO168_Amdt16_2026`, `GO168_Amdt95_2026` | Main Rules 1–29 + all Annexures III–XII, full structured ruleset. Every amendment found (as of 2026-09-13) is sourced and folded in inline, marked `[AMENDED BY G.O.___]` — several rules (Rule 15, Rule 17/TDR, Rule 26, Table IV) carry 3–5 layered amendments each, presented in date order since a later G.O. sometimes reverses an earlier one (see G.O.62/2020 vs. G.O.7/2016 on permit validity). Plus the full 141-town Annexure I/II locality gazetteer (`vault/.../GO 168 Annexure I-II - Locality Schedule.md`) — captured in full, not filtered to present-day Telangana, since the source predates the 2014 AP/Telangana split. |
| **G.O.Ms.No.105** (Telangana Municipal Land Development Layout & Sub-Division Rules, 2021) | 2021, current | `GO105` | Full code — a separate framework from G.O.168 governing layout/plot subdivision rather than buildings. Includes a related note on G.O.Ms.No.106/2020 (HMDA's own layout road-width amendment, `GO106_2020`). |

G.O.Ms.No.17/2025 (Mines & Geology Dept Environmental Impact Fee, `GO17_2025`) is noted inline in the G.O.168 note (Section U) since it's collected at the same building-approval stage, but isn't itself a Building Rules amendment.

## Not yet covered

Anything not listed above — ask the skill to build it if you have the source PDF (see SKILL.md's "Building a new reference note" section). IS 3370 (liquid-retaining structures) is a known next candidate, not started.

---
*Last updated: 2026-09-13*
