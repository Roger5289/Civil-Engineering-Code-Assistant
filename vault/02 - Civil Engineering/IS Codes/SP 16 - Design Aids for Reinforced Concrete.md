---
status: active
project: civil-engineering
type: reference
---
# SP 16:1980 — Design Aids for Reinforced Concrete to IS 456

Next in Code Design Assistant's roadmap after [[IS 456 - Plain and Reinforced Concrete]], [[IS 875 Part 1 - Dead Loads|IS 875]] (all parts), [[IS 1893 Part 1 - Earthquake Resistant Design]], and [[IS 13920 - Ductile Detailing for Seismic Forces]]. Source: `<your codes folder>\IS CODES\CED2-Cement and concrete\SP16.pdf` (252 pages). Extracted text: `<local extracted text>\SP16\SP16-fulltext.txt`.

## What this document actually is, and why this note is a navigation guide rather than a full reference

SP 16 is fundamentally **not a rulebook — it's a chart and table book.** It exists to let you skip the iterative hand-calculation that IS 456's formulas require (e.g. finding the neutral axis depth by trial) by reading a value straight off a pre-computed chart or table for your specific f_ck, f_y, and geometry. Concretely, it contains:
- **92 charts** — graphical interaction diagrams (beam design curves, column P-M interaction diagrams by steel arrangement and d'/D ratio). These are literally 2D graphs meant to be read visually; there is no meaningful way to convert a chart into text without either reproducing the whole image or throwing away the thing that makes it useful.
- **98 tables** — many of them dense grids (e.g. 30 separate slab moment-of-resistance tables, one per f_ck×f_y×thickness combination; 12 doubly-reinforced-beam tables per f_ck×f_y). A few tables spot-checked during this build (e.g. Table 64, development length by bar diameter × grade) showed the same multi-column scrambling under linear text extraction that caused real errors in the [[IS 875 Part 1 - Dead Loads|IS 875 audit]] — **these large numeric tables are deliberately not transcribed here**, consistent with that lesson.

So this note captures: (1) the compact, genuinely load-bearing formulas and small tables that **are** safe to transcribe and useful to have in one place, cross-checked against [[IS 456 - Plain and Reinforced Concrete]] where they overlap; and (2) an **index of which chart or table number to reach for**, by design scenario, so a real lookup in the source PDF is fast. **The actual numeric answer for a specific design always comes from opening the chart/table itself — this note gets you to the right page, not the right number.**

## How it relates to IS 456
SP 16 derives every chart/table from IS 456's own clauses (this edition references IS 456:1978, but the limit-state design philosophy, stress-strain assumptions, and partial safety factors are unchanged in IS 456:2000 — SP 16 remains the standard companion in current practice). Everything here should be, and largely was found to be, **consistent with [[IS 456 - Plain and Reinforced Concrete]]** — cross-checks below confirm rather than contradict that note.

## Material properties (Section 1) — confirms IS 456
- **γ_m:** concrete design strength = 0.67f_ck, then ÷1.5 → **0.446f_ck** design compressive stress. Steel design stress = f_y÷1.15 → **0.87f_y**. *(Matches IS 456 Cl 38.1 exactly.)*
- **E_s = 200,000 N/mm²** for all reinforcement grades. *(Matches IS 456 Cl 5.6.3.)*
- **Table B — x_u,max/d by steel grade:** Fe250 → **0.531**; Fe415 → **0.479**; Fe500 → **0.456**. *(These are the same values as IS 456's well-known 0.53/0.48/0.46, given here to one more decimal place — good cross-validation, no conflict.)*
- **Table A — cold-worked bar stress-strain points** (design stress at 0.80f_yd through 1.0f_yd, both strain and stress given) for Fe415 and Fe500 — small, clean table, useful for anyone doing a from-scratch M-φ (moment-curvature) calculation rather than relying on the standard block assumptions. Linear interpolation permitted between points.

## Column design (Section 3) — confirms IS 456
- **Short axial column: P_u = 0.4f_ck·A_c + 0.67f_y·A_sc.** *(Identical to IS 456 Cl 39.3.)*
- **Minimum eccentricity: e_min = l/500 + D/30, subject to ≥ 20 mm.** *(Identical to IS 456 Cl 25.4.)* SP 16's own worked example: e_min/D ≤ 0.05 in both directions is the trigger for using the simplified P_u formula above instead of full combined-bending design.
- Charts 24–26 (axial compression by grade) plot P_u/A_g against reinforcement % directly — genuinely useful for **preliminary column sizing** at the concept stage, per SP 16's own framing.

## Shear (Section 4) — adds the derivation behind IS 456's Table 19
- **τ_c formula (the one behind IS 456 Table 19's values): τ_c = 0.85√(0.8f_ck)·(√(1+5β) − 1)/(6β)**, where **β = 0.8f_ck/(6.89p_t)** (not less than 1.0), **p_t = 100·A_st/(bd)**. *(IS 456's Table 19 is just this formula pre-computed at p_t steps of 0.25%; Table 61 here gives it at finer 0.10% steps — pull that table by page if you need a p_t value between IS 456's own grid points.)*
- **Table J — τ_c,max, N/mm²:** M15→**2.5**, M20→**2.8**, M25→**3.1**, M30→**3.5**, M35→**3.7**, M40→**4.0**. *(Identical to IS 456 Table 20 — confirmed, no discrepancy.)*
- **Vertical stirrups: V_us = 0.87f_y·A_sv·d/s_v.** Inclined stirrups: multiply by (sinα+cosα) — works out to **×1.41 at 45°, ×1.37 at 60°**. Bent-up bars: V_us = 0.87f_y·A_sv·sinα (single bar/group at one section).
- **Torsion:** no separate charts/tables — convert to an equivalent shear (V_e = V_u + 1.6T_u/b) and equivalent moment (M_e1 = M_u + M_t), then reuse the ordinary shear/flexure charts. *(Same approach as IS 456 Cl 41.)*

## Development length & anchorage (Section 5)
- **L_d = φ·σ_s/(4τ_bd)** — same form as IS 456 Cl 26.2.1. Tables 64–66 tabulate this by bar diameter × concrete grade × steel grade, for both tension and compression bars — **not reproduced here** (this specific table showed clear multi-column scrambling on inspection; pull p.184–185 directly).
- **Standard hook (tension bars): anchorage value = 16φ equivalent straight length. 90° bend: 8φ.** *(Cross-checks cleanly against IS 456 Cl 26.2.2.1's "4φ per 45° bend" — two 45° increments = 8φ, consistent, not a conflict.)* Table 67 gives these by actual bar diameter.

## Navigation index — which chart/table to use, by scenario

| Design need | Charts | Tables |
|---|---|---|
| Singly reinforced rectangular beam, by f_ck (15/20 N/mm²) × f_y (250/415/500) × depth band | **1–18** | **1–4** (p_t by f_ck, all f_y) |
| Doubly reinforced rectangular beam | **19–20** (f_y=250 only) | **45–56** (all f_ck×f_y combos) |
| Deflection control (span/depth modification) | **21–23** | — |
| Slab moment of resistance, by f_ck×f_y×thickness (10–25 cm) | — | **5–44** |
| T-beam limiting moment factor | — | **57–59** |
| Column, axial only | **24–26** | — |
| Column, uniaxial bending, rectangular, steel on 2 faces | **27–38** (by f_y × d'/D) | — |
| Column, uniaxial bending, rectangular, steel on 4 faces | **39–50** (by f_y × d'/D) | — |
| Column, uniaxial bending, circular section | **51–62** (by f_y × d'/D) | — |
| Column, tension + bending, rectangular, 2 faces | **66–75** | — |
| Column, tension + bending, rectangular, 4 faces | **76–92** | — |
| P_uz for biaxial bending check | **63** | — |
| Biaxial bending interaction | **64** | — |
| Slender column additional-moment multiplier k | **65** | **58** (values of β_a) |
| Shear — τ_c at finer p_t steps | — | **61** |
| Shear — vertical stirrup capacity by size/spacing | — | **62** |
| Shear — bent-up bar capacity | — | **63** |
| Development length, tension/compression, plain/deformed bars | — | **64–66** |
| Hook/bend anchorage values | — | **67** |
| Working stress method — flexure, singly reinforced | **—** | **68–79** (by σ_cbc × σ_st) |
| Working stress method — shear | — | **80–82** |
| Working stress method — development length | — | **83–85** |
| Deflection — moment of inertia of T-beams, cracked section | **93–94** | **86–94** |
| Percentage/area/spacing of bars in slabs (quick reference) | **95** | **95–96** |
| Effective length of columns (sway/no-sway charts) | **96–97** | — |
| Fixed-end moments, deflection formulae, prismatic beams | — | **97–98** |

## Audit (2026-09-11)
Re-checked every formula/small table this note transcribed against the source PDF (rendered page 195 as an image for the shear section, since the linear extraction of Table J was garbled by OCR). All confirmed correct, no errors found: the τ_c formula and β/p_t definitions, **Table J** (τ_c,max: 2.5/2.8/3.1/3.5/3.7/4.0 for M15–M40 — matches IS 456 Table 20 exactly), the vertical-stirrup and bent-up-bar shear formulas, the inclined-stirrup multipliers (1.41 at 45°, 1.37 at 60°), **Table B** (x_u,max/d: 0.531/0.479/0.456 for Fe250/415/500), **Table A**'s stress-strain point structure (0.80f_y through 1.0f_y), the column P_u formula and e_min formula (both confirmed via the source's own worked example), and the 16φ/8φ hook/bend anchorage values. This is a cleaner result than SP 34's audit — likely because SP 16's transcribed content leans on well-known, load-bearing IS 456-derived values (already cross-verified once during this note's build) rather than a large one-off printed table.

## Cross-references
- [[IS 456 - Plain and Reinforced Concrete]] — SP 16 derives from and consistently matches this code everywhere checked (x_u,max/d, P_u formula, e_min, τ_c,max, hook anchorage). Use SP 16's charts/tables for speed; IS 456 remains the authoritative rule source.
- Parent plan: Code Design Assistant.
