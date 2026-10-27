---
status: active
project: civil-engineering
type: reference
---
# IS 456:2000 — Plain and Reinforced Concrete, Code of Practice (Fourth Revision)

Phase 0-equivalent knowledge layer for the first IS code in Code Design Assistant's roadmap (locked 2026-09-11: NBC Part F completed, IS 456 next — it's the code NBC's own structural sections defer to for actual RCC design values). Source: `<your codes folder>\IS CODES\CED2-Cement and concrete\456.pdf` (107 pages). Extracted text: `<local extracted text>\IS 456\IS-456-fulltext.txt` (`===PDFPAGE N===` markers = real PDF page numbers).

**Coverage note:** built from a full read of the document (all 107 pages), then **independently re-audited 2026-09-11** (same discipline as NBC's Phase 0, which found 3 real errors). This audit found and fixed: **one real transcription error** (Table 11's M15 mean-strength floor, written as f_ck+3.5 instead of the source's f_ck+3), **one confusing/self-contradictory rewrite needed** (Table 18's serviceability factors), and **one significant completeness gap** — Clause 26 (development length, bond stress, bar spacing, nominal cover Tables 15/16/16A, and member-specific min/max reinforcement) had been read but omitted entirely from the first draft; it's now added below. Also resolved the cover-tolerance figure (Cl 12.3.2) by rendering the actual PDF page as an image, since the source font is genuinely corrupted at that spot — same failure mode already known from NBC's audit. **Two cells in Table 15 remain unresolved** even after checking the page's word layout (flagged in place) — pull the actual page for those specific values before use. Elsewhere, the source PDF's text layer has visible corruption in places (broken words, digit swaps) — **anywhere a number looks suspicious, re-verify against the actual PDF page before designing from it**, per the standing no-hallucination rule.

**Scope (Cl 1):** general structural use of plain and reinforced concrete. Explicitly **excludes** shells, folded plates, arches, bridges, chimneys, blast-resistant structures, hydraulic structures, liquid-retaining structures, and earthquake-resistant structures — those need their own standards used alongside this one (IS 1893 for seismic, etc).

## Document map

- **Section 1 — General** (Scope, References, Terminology, Symbols) — p.12–13
- **Section 2 — Materials, Workmanship, Inspection and Testing** (Cl 5–17) — p.14–31
- **Section 3 — General Design Considerations** (Cl 18–27) — p.32–51
- **Section 4 — Special Design Requirements for Structural Members and Systems** (Cl 28–34: corbels, deep beams, ribbed/hollow-block/voided slabs, flat slabs, walls, stairs, footings) — p.52–67
- **Section 5 — Structural Design (Limit State Method)** (Cl 35–43) — p.68–76
- **Annex A** — List of referred Indian Standards — p.78
- **Annex B** — Structural Design (Working Stress Method) — p.80–83 (legacy method; the code itself says limit state is now primary, working stress is the fallback "where limit state cannot be conveniently adopted," Cl 18.2.2)
- **Annex C** — Calculation of Deflection — p.85–86
- **Annex D** — Slabs Spanning in Two Directions (Table 26 coefficients) — p.90–92
- **Annex E** — Effective Length of Columns (Table 28) — p.92–94
- **Annex F** — Calculation of Crack Width — p.95
- **Annex G** — Moments of Resistance for Rectangular and T-Sections — p.96–97
- **Annex H** — Committee composition — p.98 (not covered here)

---

## Section 2 — Materials, Workmanship, Inspection and Testing

### Materials (Cl 5)
- **Cement:** 10 acceptable types listed (33/43/53 grade OPC, rapid-hardening, PSC, PPC fly-ash/calcined-clay, hydrophobic, low-heat, SRC) — p.14. **High alumina / supersulphated cement:** only with prior engineer-in-charge approval, special circumstances (Cl 5.1.2).
- **Aggregate size:** nominal max size ≤ **1/4 of minimum member thickness**; **20 mm** suitable for most work; **40 mm+** where flow isn't restricted; **10 mm** for thin sections/closely-spaced reinforcement/small cover (Cl 5.3.3). For heavily reinforced members: max aggregate size ≤ **5 mm less than minimum clear bar spacing or cover, whichever smaller** (Cl 5.3.3.1).
- **Water:** pH **≥ 6**; permissible solids limits in **Table 1** (organics 200 mg/l, inorganics 3000 mg/l, sulphates 400 mg/l, chlorides 2000 mg/l plain / 500 mg/l RCC, suspended matter 2000 mg/l) — p.15. Sea water **not recommended** for mixing/curing; only for plain concrete with no embedded steel, under unavoidable circumstances.
- **Reinforcement steel modulus of elasticity:** **200 kN/mm²** (Cl 5.6.3), fixed value regardless of grade.
- **Concrete grades — Table 2** [Cl 6.1, 9.2.2, 15.1.1, 36.1; p.16]: M10 through M80 in 5 steps. **Minimum grade for RCC work: M20** (Cl 6.1.3, restated in Table 5). Above **M55**, design parameters in this code "may not be applicable" — specialist literature needed.
- **Tensile strength estimate:** f_cr = 0.7√f_ck N/mm² (Cl 6.2.2, when not tested directly).
- **Creep coefficient** (Cl 6.2.5.1): **2.2** at 7-day loading, **1.6** at 28-day, **1.1** at 1-year — ultimate creep strain = coefficient × elastic strain at loading age.
- **Shrinkage strain** (no test data): **0.0003** (Cl 6.2.4.1).

### Workability (Cl 7) — p.18
Slump ranges by placing condition: very low (compacting factor 0.75–0.80) for blinding/pavements; **25–75 mm** low for mass concrete/lightly reinforced sections; **50–100 mm** medium for heavily reinforced sections/pumped concrete; **100–150 mm** high for trench fill/piling/tremie; very high measured by flow test.

### Durability (Cl 8) — p.17–22, the daily-use core of Section 2
- **Table 3 — Environmental Exposure Conditions** [Cl 8.2.2.1, 35.3.2; p.18]: five levels — **Mild** (protected surfaces, non-coastal), **Moderate** (sheltered from severe rain/freezing), **Severe** (condensation/rain exposure, buried in non-aggressive soil), **Very severe** (sea water contact, coastal spray, aggressive sub-soil), **Extreme** (fully immersed in sea water, tidal zone, direct contact with aggressive chemicals).
- **Table 4 — Sulphate Attack Requirements** [Cl 8.2.2.4, 9.1.2; p.19–20]: 5 classes by SO₃ concentration, each specifying cement type + min cement content (280–400 kg/m³) + max free w/c ratio (0.40–0.55). Class 5 (highest) needs SRC/supersulphated cement **plus a protective lining/coating**.
- **Table 5 — Minimum Cement Content, Max W/C Ratio and Min Grade by Exposure** [Cl 6.1.2, 8.2.4.1, 9.1.2; p.20] — **the single most-referenced durability table**:

  | Exposure | Plain: min cement (kg/m³) | Plain: max w/c | Plain: min grade | RCC: min cement (kg/m³) | RCC: max w/c | RCC: min grade |
  |---|---|---|---|---|---|---|
  | Mild | 220 | 0.60 | — | 300 | 0.55 | M20 |
  | Moderate | 240 | 0.60 | M15 | 300 | 0.50 | M25 |
  | Severe | 250 | 0.50 | M20 | 320 | 0.45 | M30 |
  | Very severe | 260 | 0.45 | M20 | 340 | 0.45 | M35 |
  | Extreme | 280 | 0.40 | M25 | 360 | 0.40 | M40 |

  Values are for 20 mm nominal max aggregate. **Table 6** adjusts min cement content for other sizes: **10 mm → +40 kg/m³; 40 mm → −30 kg/m³** (Cl 8.2.4.1).
- **Table 7 — Chloride Content Limits** [Cl 8.2.5.2]: **0.4 kg/m³** for concrete with embedded metal, steam-cured/prestressed; **0.6 kg/m³** general RCC/plain with embedded metal; **3.0 kg/m³** no embedded metal.
- **Sulphate limit:** total water-soluble SO₃ in the mix ≤ **4% by mass of cement** (Cl 8.2.5.3) — doesn't apply to supersulphated cement.
- **Cement content ceiling:** > **450 kg/m³** (excl. fly ash/GGBFS) needs special justification — cracking/thermal/ASR risk (Cl 8.2.4.2).
- **Sea water exposure:** min **M20** plain / **M30** RCC (Cl 8.2.8) — stricter than Table 5's general "extreme" minimums, this is sea-water-specific.

### Concrete Mix Proportioning (Cl 9) — p.22–23
- Design mix preferred; **nominal mix only permitted for M20 or lower** with engineer-in-charge permission (Cl 9.1.1).
- **Target mean strength = characteristic strength + 1.65 × standard deviation** (Cl 9.2.2).
- **Table 8 — Assumed Standard Deviation** [Cl 9.2.4.2; p.23]: **3.5 N/mm²** for M10–M15; **4.0 N/mm²** for M20–M25; **5.0 N/mm²** for M30 and above (site control must include proper storage/weigh-batching/moisture checks — else add 1 N/mm² to these).
- **Table 9 — Nominal Mix Proportions** [Cl 9.3; p.23]: cement content per 50 kg bag by grade (M5: 800 kg total aggregate; M20: 250 kg), water-cement ratio limits (fine:coarse generally 1:2, upper 1:1½, lower 1:2½).

### Production, Formwork, Reinforcement Assembly (Cl 10–12) — p.24–26
- **Batching accuracy:** cement **± 2%**, aggregate/admixture/water **± 3%** (Cl 10.2.2).
- **Mixing time:** minimum **2 min** (Cl 10.3.1). Admixture dosage caps: retarders **0.5%**, plasticisers **1.0%**, superplasticisers **2.0%** by cementitious mass (Cl 10.3.3), unless proven otherwise by test.
- **Formwork tolerances** (Cl 11.1): columns/beams cross-section **+12/−6 mm**; footing plan dimensions **+50/−12 mm**; footing eccentricity **≤ 0.02× footing width in the deviation direction, max 50 mm**; footing thickness **± 0.05× specified thickness**.
- **Stripping time** (Cl 11.3.1, ordinary Portland cement, ambient ≥ 15°C, adequate curing): vertical formwork (columns/walls/beam sides) **16–24 h**; slab soffit (props refixed immediately) **3 days**; beam soffit (props refixed immediately) **7 days**; props to slabs ≤ 4.5 m span **7 days**, > 4.5 m span **14 days**; props to beams/arches ≤ 6 m span **14 days**, > 6 m span **21 days**.
- **Reinforcement bend radius when re-bent at construction joints** (Cl 12.5): **≥ 4 bar diameters** plain mild steel, **≥ 6 bar diameters** deformed bars — for bars ≤ 12 mm (HYSD) / ≤ 16 mm (mild steel) only.
- **Placing tolerances** (Cl 12.3.1): effective depth ≤ 200 mm → **± 10 mm**; effective depth > 200 mm → **± 15 mm**.
- **Cover tolerance (Cl 12.3.2): +10 mm / −0 mm** — actual cover may exceed nominal by up to 10 mm but must never fall short. *(Confirmed 2026-09-11 by rendering the actual PDF page as an image and reading it visually — the text layer at this exact spot is genuinely corrupted in the source font, extracting as "+lz mm" rather than "+10/0 mm." Same failure mode already documented and handled in NBC's Phase 0 audit; the visual glyph on the rendered page is unambiguous even though the underlying character-encoding is broken.)*

### Curing, Sampling, Acceptance (Cl 13, 15–17) — p.26–31
- **Moist curing minimum:** **7 days** (OPC), **10 days** (mineral admixtures/blended cements), **10 days minimum** for hot/dry-weather exposure, recommended extension to **14 days** for blended-cement concrete (Cl 13.5.1).
- **Sampling frequency** (Cl 15.2.2): 1 sample per 1–5 m³, 2 per 6–15 m³, 3 per 16–30 m³, 4 per 31–50 m³, then +1 per additional 50 m³. **At least one sample per shift.**
- **Individual test variation:** ≤ **± 15%** of the average of 3 specimens, else the sample is invalid (Cl 15.4).
- **Table 11 — Acceptance Criteria** [Cl 16.1, 16.3]: mean of 4 consecutive results ≥ f_ck + 0.825×std-dev (rounded to 0.5 N/mm²) or **f_ck+4 (M20 and above) / f_ck+3 (M15)**, whichever greater; individual result ≥ **f_ck−4 (M20 and above) / f_ck−3 (M15)**. *(Corrected 2026-09-11 audit — first draft had the M15 floor as f_ck+3.5; source clearly states f_ck+3.)*
- **Core test acceptance** (Cl 17.4.3): average equivalent cube strength ≥ **85%** of specified grade strength; no individual core **< 75%**. Minimum **3 cores** tested.
- **Load test for flexural members** (Cl 17.6): full DL + 1.25×IL for **24 h**; must recover **≥ 75%** of imposed-load deflection within 24 h of load removal. If it doesn't, the test may be repeated after a 72 h lapse — the **retest** bar is stricter, requiring **≥ 80%** recovery to pass. *(These are two different checks, not an inconsistency — confirmed against source 2026-09-11.)* Recovery check is waived entirely if max deflection during the 24 h test is **< span²/(400×D)** (mm, D in mm, span in m).

---

## Section 3 — General Design Considerations

### Loads and stability (Cl 18–20) — p.32–34
- **Unit weights (Cl 19.2.1):** plain concrete **24 kN/m³**, RCC **25 kN/m³** (sand/gravel or crushed stone aggregate).
- **Overturning stability (Cl 20.1):** restoring moment ≥ **1.2×** DL overturning moment + **1.4×** IL overturning moment. Where DL provides the restoring moment, only **0.9×** characteristic DL counted; IL restoring moment always ignored.
- **Sliding (Cl 20.2):** factor of safety ≥ **1.4** under worst load combination, only 0.9× DL counted as resisting.
- **Lateral sway (Cl 20.5):** under transient wind load, top sway ≤ **H/500** (H = total building height). Seismic sway: refer IS 1893 instead.
- **Fire resistance (Cl 21):** governed by nominal cover (Cl 26.4.3 + Fig 1) and member dimensions. **Additional protection (fire-resistant finishes/false ceilings/sacrificial steel) required if nominal cover exceeds 40 mm (beams) or 35 mm (slabs)** — spalling risk (Cl 21.3.1).

### Analysis (Cl 22) — p.34–37
- **Table 12 — Bending Moment Coefficients** for uniform continuous beams (≥3 spans, span variation ≤15%), by unit total load × effective span: **DL+fixed IL** → near mid end-span +1/12, mid interior span +1/16, support next-to-end −1/10, other interior supports −1/12. **Not-fixed IL** → +1/10 / +1/12 / −1/9 / −1/9. **Redistribution not permitted where these coefficients are used** (Cl 22.5.1).
- **Table 13 — Shear Coefficients**, same conditions: DL+fixed → 0.4 (end outer) / 0.6 (end inner) / 0.55 (next-interior) / 0.5 (other interior). Not-fixed IL → 0.45/0.6/0.6/0.6.
- **T/L-beam effective flange width** (Cl 23.1.2): T-beam b_f = l₀/6 + b_w + 6D_f; L-beam b_f = l₀/12 + b_w + 3D_f (never exceeding actual width; l₀ ≈ 0.7× effective span for continuous beams/frames).

### Deflection control — the most-used daily check (Cl 23.2) — p.37–39
- **Final deflection limit:** span/**250** (all loads incl. creep/shrinkage/temperature, from as-cast level).
- **Post-finishes deflection limit:** span/**350** or **20 mm**, whichever smaller.
- **Basic span/effective-depth ratios** (spans ≤ 10 m): **Cantilever 7**, **Simply supported 20**, **Continuous 26**.
- Spans > 10 m: multiply by **10/span(m)** — except cantilevers, which need actual deflection calculation instead.
- Modify by **tension-reinforcement modification factor** (Fig 4, function of % steel and f_s = 0.58 f_y × (Ast required/Ast provided)) and **compression-reinforcement factor** (Fig 5) and, for flanged beams, the **web/flange width ratio factor** (Fig 6).
- **Quick two-way slab check** (mild steel, spans ≤ 3.5 m, loading ≤ 3 kN/m²): simply supported **35**, continuous **40** — **× 0.8 for Fe 415 bars**.
- **Beam lateral stability** (Cl 23.3): clear distance between lateral restraints ≤ **60b or 250b²/d** (whichever less); cantilever ≤ **25b or 100b²/d**.

### Columns (Cl 25) — p.41–42
- **Column/strut definition:** effective length > 3× least lateral dimension (else it's a pedestal).
- **Short column:** both slenderness ratios (l_ex/D and l_ey/b) **< 12**; otherwise slender.
- **Slenderness limit:** unsupported length ≤ **60× least lateral dimension**; if one end unrestrained, l ≤ **100b²/D**.
- **Minimum eccentricity (Cl 25.4):** unsupported length/**500** + lateral dimension/**30**, subject to a **minimum of 20 mm**. For biaxial bending, sufficient if eccentricity exceeds the minimum about one axis at a time.

### Reinforcement & Detailing (Cl 26) — p.42–51. **Added in the 2026-09-11 audit — this entire clause was read but omitted from the first draft, despite being core daily-use content.**

**Development length and anchorage (Cl 26.2):**
- Development length: L_d = φσ_s/(4τ_bd), where φ = bar diameter, σ_s = design stress in the bar, τ_bd = design bond stress.
- **Design bond stress τ_bd (plain bars in tension), N/mm²** [Cl 26.2.1.1]: **M20 → 1.2; M25 → 1.4; M30 → 1.5; M35 → 1.7; M40 and above → 1.9.** **Deformed bars (IS 1786): +60%** on these values. **Bars in compression: +25%** on the tension value (deformed or plain, applied after the deformed-bar increase if both apply).
- **Bundled bars:** development length of each bar increased **+10% (2 bars)**, **+20% (3 bars)**, **+33% (4 bars)** (Cl 26.2.1.2).
- **Bend/hook anchorage (Cl 26.2.2.1):** a 45° bend = **4× bar diameter**, capped at **16× diameter** total for the bend. A standard U-hook = **16× bar diameter** flat.
- **Stirrup/tie anchorage (Cl 26.2.2.4(b)):** 90° bend + continue **≥ 8 diameters**, OR 135° bend + continue **≥ 6 diameters**, OR 180° bend + continue **≥ 4 diameters**.
- **Curtailment (Cl 26.2.3.1):** reinforcement must extend **≥ effective depth or 12× bar diameter** (whichever greater) past the point it's no longer needed for flexure, except at simple supports/cantilever ends.
- **Positive-moment steel into supports (Cl 26.2.3.3):** ≥ **1/3** must extend into simple supports, ≥ **1/4** into continuous supports, length ≥ L_d/3.
- **Negative-moment steel past point of inflection (Cl 26.2.3.4):** ≥ **1/3** of the support steel must extend ≥ effective depth, 12×diameter, or **1/16 of clear span**, whichever greatest.
- **Lap splices (Cl 26.2.5.1):** **not permitted for bars > 36 mm** (weld instead, or lap with added spirals if welding impractical). Lap length = **L_d or 30×diameter, whichever greater** (flexural tension); **2×L_d or 30×diameter** (direct tension); straight length ≥ **15×diameter or 200 mm**. **×1.4 factor** if the lap is at the top of a section as cast with cover < 2×diameter, OR at a corner with cover < 2×diameter or adjacent-lap clear distance < 75mm/6×diameter (whichever greater) — **×2.0 if both conditions apply.** Compression lap length = development length in compression, **≥ 24×diameter**.
- **Bearing stress at bends** must not exceed **1.5f_ck/(1+2φ/a)** (limit state) — a is the centre-to-centre spacing between bars/groups perpendicular to the bend plane (or cover+φ at an edge bar).

**Spacing (Cl 26.3):**
- **Minimum clear distance between bars:** the greater of bar diameter (equal bars) / larger bar diameter (unequal) / **aggregate size + 5 mm**.
- **Table 15 — Max clear distance between bars in tension** [Cl 26.3.3, p.47], by redistribution % (−30% to +30%) and f_y — **verified directly against the PDF page's word layout 2026-09-11** rather than the linear text extraction, which had scrambled this table badly: **f_y=250 → 215 mm at −30%, 260 mm at −15%; f_y=415 → 125 mm at −30%, 155 mm at −15%, 180 mm at 0%; f_y=500 → 105 mm at −30%, 130 mm at −15%.** Spacing **increases** as redistribution moves from −30% toward 0% (my first read of the garbled extraction had this backwards). The 0%/+15%/+30% columns for f_y=250 and f_y=500, and +15%/+30% for f_y=415, didn't reconstruct unambiguously even from the page layout — **pull the actual page for those specific cells** rather than trust an interpolation. (Table doesn't apply where crack-width calc shows wider spacing acceptable, or in aggressive environments unless stress is capped at 300/165 N/mm² per the table's own note.)
- **Slabs:** main bars ≤ **3× effective depth or 300 mm** (whichever smaller); shrinkage/temperature bars ≤ **5× effective depth or 450 mm**.

**Nominal cover (Cl 26.4):**
- **Table 16 — Cover to Meet Durability, mm** [Cl 26.4.2, p.47] — **the daily-use companion to Table 5**: **Mild 20; Moderate 30; Severe 45; Very severe 50; Extreme 75.** Main bars ≤12mm under mild exposure: **−5 mm**. Severe/very severe with concrete ≥ M35: **−5 mm** allowed. Actual cover may exceed nominal by up to **+10 mm** but not fall short (**−0 mm**) unless otherwise specified.
- **Columns:** longitudinal bar cover **≥ 40 mm, and ≥ bar diameter** — except column min dimension ≤200mm with bars ≤12mm, where **25 mm** is permitted (Cl 26.4.2.1).
- **Footings:** minimum cover **50 mm** (Cl 26.4.2.2).
- **Table 16A — Cover to Meet Fire Resistance, mm** [Cl 26.4.3, p.47] by required fire rating (0.5–4 h): beams/slabs/ribs need as little as **20 mm** at 0.5–1 h, rising to **50–70 mm** at 4 h (simply supported); columns hold at **40 mm** across the whole range. Continuous members generally need less cover than simply-supported for the same rating. **This is the table that governs Cl 21.3.1's 40mm(beam)/35mm(slab) spalling-protection trigger** (see Section 3 above).

**Minimum/maximum reinforcement by member (Cl 26.5):**
- **Beams — tension steel:** minimum A_s/(bd) = **0.85/f_y** (i.e. A_s,min = 0.85bd/f_y); **maximum: 0.04bD** (both tension and compression steel independently capped at this).
- **Beams — side face reinforcement:** required when web depth **> 750 mm**; total ≥ **0.1%** of web area, split both faces, spacing ≤ **300 mm or web thickness**, whichever smaller.
- **Beams — max shear reinforcement spacing:** ≤ **0.75d** (vertical stirrups) or **d** (45° inclined stirrups), **never > 300 mm**.
- **Slabs:** minimum reinforcement (either direction) **0.15%** of gross area (mild steel), reducible to **0.12%** for HYSD bars or welded wire fabric. Max bar diameter ≤ **1/8 of slab thickness**.
- **Columns — longitudinal steel:** **0.8% to 6%** of gross cross-sectional area (practically ≤4% where bars lap with the column below). Minimum **4 bars** (rectangular) / **6 bars** (circular/helical), each **≥ 12 mm** diameter. Max spacing along periphery **300 mm**.
- **Columns — transverse ties:** pitch ≤ **least of: least lateral dimension / 16×smallest longitudinal bar diameter / 300 mm**. Tie diameter ≥ **whichever is larger of 1/4 the largest longitudinal bar diameter, or 16 mm**.
- **Helical reinforcement pitch:** ≤ **75 mm** (giving the 1.05× strength bonus), also ≤ **1/6 of core diameter**; ≥ **25 mm**, also ≥ **3× the helix bar diameter**.
- **Pedestals:** nominal reinforcement (not counted on for strength) ≥ **0.15%** of cross-section.

---

## Section 4 — Special Design Requirements

- **Corbels (Cl 28):** short cantilever where shear-span a_v < effective depth d at the root, AND outer-edge depth ≥ ½ root depth. Horizontal-force resistance ≥ **½ the design vertical load**. Shear reinforcement (horizontal links, upper 2/3 of depth) ≥ **½ the main tension reinforcement area**.
- **Deep beams (Cl 29):** effective-span/overall-depth ratio **< 2.0** (simply supported) or **< 2.5** (continuous) triggers deep-beam design — lever arm formulas differ from ordinary beams (z = 0.2(l+2D) or 0.6l for SS; 0.2(l+1.5D) or 0.5l for continuous, whichever governs by l/D).
- **Ribbed/hollow-block/voided slabs (Cl 30):** in-situ ribs **≥ 65 mm wide**, spaced **≤ 1.5 m**, depth (excl. topping) **≤ 4× width**. Filler block crushing strength **≥ 14 N/mm²** if structural.
- **Flat slabs (Cl 31):** **minimum thickness 125 mm**. Span/depth ratio per Cl 23.2 applies directly for slabs with drops; **× 0.9** for slabs without drops. Direct design method requires **≥ 3 continuous spans** each direction, panel aspect ratio **≤ 2.0**, column offset **≤ 10%** of span.
- **Walls (Cl 32):**
  - Minimum thickness **100 mm**.
  - Braced-wall max effective-height/thickness ratio: **30**.
  - Design axial strength: P_uw = 0.3(t − 1.2e − 2e_a)f_ck per unit length, where e_a = additional slenderness eccentricity = H_we²/(2500t).
  - Nominal shear stress must never exceed **0.17f_ck** (limit state) / **0.12f_ck** (working stress) — hard ceiling regardless of reinforcement.
  - **Minimum reinforcement ratio:** vertical **0.0012** (deformed bars ≤16mm, f_y≥415) or **0.0015** (other bars); horizontal **0.0020** (deformed ≤16mm, f_y≥415) or **0.0025** (other bars). Max spacing **3× wall thickness or 450 mm**, whichever smaller.
  - Walls **> 200 mm thick** need reinforcement in **two grids** (near each face).
- **Stairs (Cl 33):** effective span rules depend on support condition (beam-to-beam centres; going + landing allowance; or combined with landing as one slab). Open-well stairs: shared-span load split **½ each direction**. Embedded ends (≥110 mm into wall): deduct 150 mm from loaded width, add 75 mm to effective breadth.
- **Footings (Cl 34):**
  - Minimum edge thickness: **150 mm** (soil-bearing), **300 mm** (above pile tops).
  - Critical section for bending: **face of column/pedestal/wall**; for masonry walls, **halfway between centreline and edge**.
  - Critical section for one-way shear: **at effective depth d from the face**; two-way (punching) per Cl 31.6 (flat-slab shear rules).
  - **Bearing stress at column base:** ≤ **0.45f_ck** (limit state) / **0.25f_ck** (working stress), amplified by √(A₁/A₂) up to a max factor of **2**.
  - **Dowel/extended reinforcement:** ≥ **0.5%** of the supported column's cross-section, minimum **4 bars**.
  - **Nominal reinforcement for footings > 1 m thick:** **360 mm²/m** per face, each direction (doesn't override the tensile-reinforcement requirement from depth).
  - Two-way rectangular footing: central band (width = short-side dimension) carries **2/(β+1)** fraction of short-direction reinforcement, β = long/short side ratio.

---

## Section 5 — Structural Design (Limit State Method)

### Safety framework (Cl 35–37) — p.68–70
- **Table 18 — Partial Safety Factors (γ_f)** [p.69]. *(Rewritten as a table 2026-09-11 audit — the first draft's prose compressed this into a self-contradicting sentence, claiming "1.0 across the board" for serviceability while also giving 0.8 values in the same breath.)*

  | Load combination | Collapse: DL | Collapse: IL | Collapse: WL | Serviceability: DL | Serviceability: IL | Serviceability: WL |
  |---|---|---|---|---|---|---|
  | DL+IL | 1.5 | 1.5 | — | 1.0 | 1.0 | — |
  | DL+WL | 1.5 (or 0.9 where overturning/stress-reversal governs) | — | 1.5 | 1.0 | — | 1.0 |
  | DL+IL+WL | 1.2 | 1.2 | 1.2 | 1.0 | 0.8 | 0.8 |

  Substitute EL (earthquake load) for WL where seismic governs (Table 18 Note 1).
- **Material partial safety factors (γ_m):** concrete **1.5**, steel **1.15** (already baked into the design equations in this code).
- **Crack width limits (Cl 35.3.2):** general **0.3 mm**; weather/moisture/soil-exposed **0.2 mm**; "severe" category (Table 3) **0.1 mm**.
- **Moment redistribution (Cl 37.1.1):** resistance at any section ≥ **70%** of the elastic peak moment there; moment reduction at any section ≤ **30%** of the numerically largest elastic moment for that member; neutral-axis-depth check x_u/d + δM/100 ≤ **0.6**; **redistribution limited to 10% for sway frames over 4 storeys**; **not permitted at all** where Table 12/13 coefficients were used.

### Flexure (Cl 38) — p.70
- Max concrete compressive strain: **0.0035**. Design stress block: **0.36f_ck·x_u** area, centroid at **0.42x_u** from the compression face. Concrete design strength = **0.67f_ck**, γ_m=1.5 applied on top.
- **Limiting x_u,max/d ratio:** **0.53** (Fe250), **0.48** (Fe415), **0.46** (Fe500).

### Compression members (Cl 39) — p.70–73
- **Short axial column (min eccentricity ≤ 0.05× lateral dimension):** P_u = 0.4f_ck·A_c + 0.67f_y·A_sc.
- **Helical reinforcement:** column strength = **1.05×** an equivalent tied column, provided the helix-to-core volume ratio meets Cl 39.4.1's minimum.
- **Biaxial bending:** α_n interaction exponent — **1.0** for P_u/P_uz ≤ 0.2, linear **1.0→2.0** for 0.2–0.8, **2.0** above 0.8. P_uz = 0.45f_ck·A_c + 0.75f_y·A_sc.
- **Slender column additional moment:** M_a = P_u·D/2000 × (l_ex/D)² (major axis form) — added to the initial moment (≥ 0.4× larger end moment) for braced columns.
- **Sway/no-sway threshold (Annex E-2):** stability index Q ≤ **0.04** → no-sway column.

### Shear (Cl 40) — p.71–74, the most-used table in daily beam design
- **Table 19 — Design Shear Strength of Concrete, τ_c (N/mm²)** [p.73–74], by tension-steel % (0.15 to ≥3.00) and grade (M15–M40+): ranges from **0.28** (0.15% steel, M15) up to **1.01** (3.0%+, M40+). Governs whether minimum shear reinforcement suffices or design shear reinforcement is required.
- **Table 20 — Maximum Shear Stress, τ_c,max (N/mm²)** [p.73]: **2.5** (M15), **2.8** (M20), **3.1** (M25), **3.5** (M30), **3.7** (M35), **4.0** (M40+) — **absolute ceiling regardless of shear reinforcement provided.**
- **Solid-slab shear enhancement factor k** (Cl 40.2.1.1): **1.00** (≥300mm depth) up to **1.30** (≤150mm depth) — multiplies τ_c for thin slabs. Does not apply to flat slabs (Cl 31.6 governs those instead).
- **Minimum shear reinforcement** (Cl 26.5.1.6): A_sv/(b·s_v) ≥ 0.4/(0.87f_y).
- **Enhanced shear strength near supports** (Cl 40.5.1): sections within **2d of a support or concentrated load** may use an enhanced τ_c of 2d·τ_c/a_v (capped by Table 20), reflecting the steeper failure plane close to a support.

### Torsion (Cl 41) — p.74–75
- **Equivalent shear:** V_e = V_u + 1.6(T_u/b). **Equivalent bending moment:** M_e1 = M_u + M_t, where M_t = T_u(1+D/b)/1.7.
- If M_t > M_u, additional reinforcement needed on the flexural **compression** face too (M_e2 = M_t − M_u).
- Transverse reinforcement: two-legged closed hoops, area per Cl 41.4.3's formula combining T_u, V_u, and the stirrup spacing.

### Deflection & Cracking (Cl 42–43) — p.75–76
- Deflection: satisfied by the span/depth ratios in Cl 23.2.1, or explicit Annex C calculation against the Cl 23.2 limits.
- Cracking: spacing rules in Cl 26.3.2 generally sufficient; explicit crack-width check (Annex F) only if wider spacing is used.
- **Compression members carrying design axial load > 0.2f_ck·A_c need NOT be checked for cracking** — below that threshold, treat as a flexural member for crack control purposes.

---

## Annexes (B–G) — referenced by page, not fully converted here

- **Annex B — Working Stress Method** (p.80–83): permissible stresses in concrete/steel, permissible loads in compression members. The code's own framing (Cl 18.2.2) treats this as the fallback when limit state "cannot be conveniently adopted" — limit state is the primary method now. Pull by page if a working-stress check is genuinely needed.
- **Annex C — Deflection Calculation** (p.85–86): short-term + shrinkage + creep deflection components, for when the span/depth shortcut isn't enough and an explicit calculation is required.
- **Annex D — Slabs Spanning in Two Directions** (p.90–92): restrained-slab design (Cl D-1) with **Table 26** bending-moment coefficients for 9 standard panel/edge-condition cases, by l_y/l_x ratio — too large a matrix to reproduce here, pull by page. Key structural rules: **torsion reinforcement required at any corner where the slab is simply supported on both meeting edges** (top+bottom layers, each 3/4 of the mid-span reinforcement area, extending 1/5 of the shorter span); halved if only one edge is continuous; **not needed if both edges are continuous**. l_y/l_x > 2 → design as one-way instead.
- **Annex E — Effective Length of Columns** (p.92–94): **Table 28** gives theoretical/recommended effective-length factors by end-restraint condition (e.g. both-ends-fixed-no-sway: 0.50l theoretical / 0.65l recommended; one-end-rotation-restrained: matches next row). Sway-vs-no-sway determination is the Cl E-2 stability index Q (see Section 5 above).
- **Annex F — Crack Width Calculation** (p.95): formula-based, for the explicit check referenced in Cl 35.3.2/43.1 when spacing rules alone aren't judged sufficient.
- **Annex G — Moments of Resistance for Rectangular and T-Sections** (p.96–97): closed-form M_u formulas for singly/doubly-reinforced rectangular and flanged sections, built on the Cl 38 stress-block assumptions — useful for hand-checking without the full strain-compatibility iteration.

## Cross-references

- NBC 2026's own structural sections (Part C) explicitly defer to this code for real design values — e.g. [[Part C Sec 5 - Structural Concrete]] says limit-state design is "deferred to IS 456 (good practice C-5(2))." This is *why* IS 456 was prioritized over finishing NBC's structural Parts (locked decision, 2026-09-11) — see Code Design Assistant.
- Loads: IS 875 (Parts 1–5, dead/imposed/wind/snow/special) — not yet built.
- Seismic: IS 1893 — not yet built, next candidate per the original code-priority discussion.
- Ductile detailing: IS 13920 — modifies/overrides several of this note's reinforcement-detailing rules for seismic zones; not yet built, should be read alongside this note once built (Cl 26.1.2 already flags this).
- Design aids: SP 16 (design charts to this code) and SP 34 (detailing handbook) — not yet built, natural companions once this note is in daily use.
- Parent plan: Code Design Assistant.
