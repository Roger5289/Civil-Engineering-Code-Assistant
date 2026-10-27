---
status: active
project: civil-engineering
type: reference
---
# SP 34(S&T):1987 — Handbook on Concrete Reinforcement and Detailing

Last of the current batch in Code Design Assistant's roadmap, alongside [[SP 16 - Design Aids for Reinforced Concrete]]. Source: `<your codes folder>\IS CODES\CED2-Cement and concrete\SP34.pdf` (286 pages). Extracted text: `<local extracted text>\SP34\SP34-fulltext.txt`.

**Nature of this document:** unlike SP 16 (pure chart/table lookup), SP 34 is a genuine **detailing practice handbook** — how to actually draw and schedule reinforcement, not just what the numbers are. Much of its content overlaps with (and confirms) [[IS 456 - Plain and Reinforced Concrete]] and [[IS 13920 - Ductile Detailing for Seismic Forces]], since it's the "how do I put this on a drawing" companion to those rule-sources. A significant fraction of the book is **bar-shape sketches and drawing figures** — inherently graphical, not usefully transcribed as text. This note covers Sections 1, 4, and 5 in real depth (materials, general detailing requirements, bar-bending-schedule practice — the most broadly applicable content), samples Sections 6–10 (member-specific detailing) for the standout practical rules not already in IS 456/13920, and treats Sections 11–14 and the appendices as lower-priority reference-by-page given the session's scope.

**⚠ Edition-currency flag — read before trusting a specific number here:** this is a **1987** handbook, built on IS 456:1978. Where it conflicts with the *current* IS 456:2000 or IS 13920:1993 (both already audited in this vault), **the newer code wins** — SP 34 hasn't been updated to match. One concrete case found in this build: SP 34's column-tie minimum diameter is given as **≥1/4 largest bar, minimum 5 mm** (Cl 7.2.6.2) — but IS 456:2000 Cl 26.5.3.2(c)(2) requires **minimum 16 mm**, confirmed in that note's own audit. **Use IS 456:2000's 16 mm, not SP 34's 5 mm.** Treat every other SP 34 number the same way: useful for practice/convention, but defer to the current rule-source code when the two disagree.

## Section 1 — Steel for reinforcement
- Permitted types: mild/medium-tensile steel bars (IS 432), high-strength deformed bars (IS 1786, grades Fe415/Fe500/Fe550), hard-drawn steel wire fabric (IS 1566).
- **Don't mix bar grades on the same job** (e.g. Fe415 and Fe500 side by side) — invites site confusion and error. Secondary reinforcement (ties/stirrups) may still be mild steel even where main bars are high-strength deformed.
- **Mild steel Grade II bars not recommended** where the design seismic coefficient is ≥ 0.05 (broadly Zones IV/V) or under dynamic loading.
- Max reinforcing bar length ex-stock: **13 m**.

## Section 4 — General detailing requirements

**Cover (Cl 4.1)** — matches IS 456 exactly: bar-end cover ≥ 25 mm or 2× bar diameter; column longitudinal bar ≥ 40 mm or bar diameter (25 mm allowed for columns ≤ 200mm with bars ≤ 12mm); beam longitudinal bar ≥ 25 mm or bar diameter; slab reinforcement ≥ 15 mm or bar diameter; other reinforcement ≥ 15 mm or bar diameter. Tolerance: actual cover must not fall short by more than **1/3 of specified cover or 5 mm**, whichever is less.
- **Aggressive exposure (chemicals, acid, saline, sulphurous smoke): +15 to +50 mm** over the base value, at Engineer-in-Charge's discretion, **never exceeding 75 mm total.**
- **Marine structures, fully immersed: +40 mm.** **Periodically immersed / sea spray: +50 mm.** Both capped at 75 mm total.
- **For M25 concrete and above, halve** the aggressive-exposure/marine additions above.

**Development length & anchorage (Cl 4.2–4.3)** — same formula as IS 456: **L_d = φ·σ_s/(4τ_bd)**. Design bond stress (plain bars, tension): M15→1.0, M20→1.2, M25→1.4, M30→1.5, M35→1.7, M40→1.9 N/mm² — **+60% for deformed bars, +25% for bars in compression** (identical to IS 456).
- **Table 4.1 — anchorage value of hooks/bends by bar diameter** (verified against a page-image render of the source, p.30: hook = 16×diameter, 90° bend = 8×diameter, matching the 16φ/8φ ratios derivable from IS 456's own 4φ-per-45°-bend rule — **except one cell**: the source itself prints **6.2 cm for the 8mm bar's 90° bend value**, not the 6.4 cm that the stated 8φ rule and every other row in the table gives. All 11 other cells match the 8φ formula exactly, so this reads as a genuine printing error in the 1987 original rather than a pattern — but it's what the book actually says, so it's reproduced as printed with this flag rather than silently corrected):

  | Bar dia (mm) | Hook value (cm) | 90° bend value (cm) |
  |---|---|---|
  | 6 | 9.6 | 4.8 |
  | 8 | 12.8 | 6.2 ⚠ (8φ formula gives 6.4 — see note above) |
  | 10 | 16.0 | 8.0 |
  | 12 | 19.2 | 9.6 |
  | 16 | 25.6 | 12.8 |
  | 18 | 28.8 | 14.4 |
  | 20 | 32.0 | 16.0 |
  | 22 | 35.2 | 17.6 |
  | 25 | 40.0 | 20.0 |
  | 28 | 44.8 | 22.4 |
  | 32 | 51.2 | 25.6 |
  | 36 | 57.6 | 28.8 |

  **Minimum internal bend radius factor k** (bend diameter = k × bar diameter): **mild steel k=2, cold-worked steel k=4.**
- **Tables 4.2–4.4 — full development-length tables** (bar diameter × concrete grade M15–M30, tension & compression, for plain bars/Fe415/Fe500) — spot-verified clean (cross-checked one value against the L_d formula by hand, matched exactly: 6mm plain bar, M15, tension = 32.6 cm ✓). Genuinely reliable, unlike some of the equivalent tables found scrambled elsewhere this session — **but not reproduced here** given their size (~300 values across the three tables); pull p.32–33 directly, or compute any single value from the formula above.
- **Splicing:** away from max-stress sections, staggered; **not more than 50% of bars spliced at one section** in flexural members, and not where moment exceeds 50% of the section's moment of resistance. Where more than half must be spliced, or splicing at max-stress points is unavoidable: increase lap length and/or add spiral/closely-spaced stirrups around the splice. **Bars > 28 mm diameter: lap splice must be fully enclosed by transverse reinforcement** (small compact stirrups or spirals), not just the standard confining stirrups.

## Section 5 — Bar bending schedules
A schedule must record: member ID, bar position, bar mark, diameter, count per member, total count, total straight length, shape/bending dimensions, chair details, and remarks. **No abbreviation without explanation.**
- **Standard bar-shape codes (Tables 5.1–5.7)** give length formulas for each standard bend configuration (e.g. simple bend: L = A+C+E; U-bar: L = I+2B) — these are inherently tied to accompanying sketches and **not usefully reproduced as text without the diagrams**; pull p.62 onward directly when building an actual BBS.
- **Slabs:** panels that are exactly identical should share one identifying mark in the schedule rather than being re-specified.
- **Welded wire fabric in slabs:** gets its own schedule format (mesh size, fitting details) — Table 5.9.

## Sampled member-specific detailing (Sections 6–10)

**Columns (Section 7)** — matches IS 456 on longitudinal steel (0.8–6%, practical ceiling 4% except at lap zones), min 4 bars (rectangular)/6 bars (circular helical), ≥12mm diameter, ≤300mm periphery spacing; tie pitch = least of (least lateral dimension, 16×smallest longitudinal bar dia, 48×tie dia). **Tie/link diameter: SP 34 says ≥1/4 largest bar or 5mm minimum — superseded by IS 456:2000's 16mm minimum, see the flag at the top of this note.** Helical reinforcement: pitch ≤75mm or 1/6 core diameter (whichever smaller), ≥25mm or 3×helix bar diameter (whichever greater); 1.5 extra anchorage turns, preferably with a 135° hook.
- **Practical guidance not in IS 456 itself:** at least 2 temporary fixing stirrups to hold splices in position during erection — don't remove the stirrups above a floor until the next column above is erected. Column splices should be staggered. For beams > 600 mm deep, U-bars are advisable at non-continuous ends. Corbels: main tension reinforcement **0.4–1.3%** of the section at the supporting face (note: this range differs from IS 13920's corbel-adjacent provisions — SP 34's corbel clause is a general IS 456-era rule, not seismic-specific).

**Floor slabs (Section 9)** — matches IS 456 on minimum reinforcement (0.15% plain bars / 0.12% HYSD or WWF), spacing (main ≤3d or 450mm; distribution ≤5d or 450mm), minimum bar diameter (8mm HYSD / 10mm plain main bars, 6mm distribution), max diameter ≤1/8 slab thickness.
- **Practical detailing rule not in IS 456 itself:** at midspan, **≥50% of main reinforcement should extend to the supports**; the remaining ≤50% may terminate within **0.1×span** of the support (one-way and two-way slabs both).
- Slab spans in one direction if supported on 2 opposite sides only, **or** on all 4 sides where l_y/l_x > 2 (design for the shorter span either way).

## Audit (2026-09-11)
Re-checked every number this note transcribed against the source PDF (rendered as page images where a table was involved, not just re-read as linear text). Confirmed accurate: Section 1 permitted-steel-types text, Cl 4.1 cover values and tolerance, Cl 4.2.2.1 bond-stress table, Cl 4.3.1.2 hook/bend anchorage rules (16φ hook, 4φ-per-45°-max-16φ bend) and the k-factor table, Cl 7.2.6.2's 5mm tie-diameter figure (confirmed it really is what the 1987 source says, not an extraction artifact — the IS 456:2000 conflict flagged above is real), Section 9's 0.15%/0.12% minimum slab reinforcement and the 50%-to-supports/0.1×span midspan rule. **One real finding:** Table 4.1's 90° bend value for an 8mm bar is printed as 6.2 cm in the source itself — inconsistent with the stated 8φ rule (which gives 6.4 cm) and with every other row in the table, which does follow 8φ exactly. Read as a genuine 1987 printing error, not a transcription mistake on this note's part — corrected in the table above to match the source with a flag, per the no-guessing rule (reproduce what the book says, don't silently "fix" it to what the formula implies).

## Cross-references
- [[IS 456 - Plain and Reinforced Concrete]] — the rule source SP 34's detailing conventions implement; confirmed consistent everywhere checked in this build **except** the column tie-diameter minimum (SP 34 5mm vs IS 456:2000's 16mm — use IS 456).
- [[IS 13920 - Ductile Detailing for Seismic Forces]] — the current, authoritative ductile-detailing source; SP 34's own Section 12 on ductility predates IS 13920 (1987 vs 1993) and wasn't read in depth for this note given IS 13920 supersedes it.
- [[SP 16 - Design Aids for Reinforced Concrete]] — SP 34 tells you how to *draw* what SP 16 helps you *calculate*.
- Parent plan: Code Design Assistant.
