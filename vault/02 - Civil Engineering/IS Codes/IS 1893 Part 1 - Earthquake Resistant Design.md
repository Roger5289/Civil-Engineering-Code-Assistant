---
status: active
project: civil-engineering
type: reference
---
# IS 1893 (Part 1):2002 — Criteria for Earthquake Resistant Design of Structures, Part 1: General Provisions and Buildings

Next code in Code Design Assistant's roadmap after IS 456 and IS 875 (all parts). Source: `<your codes folder>\IS CODES\CED39-Earthquake engineering\1893_1.pdf` (41 pages, Fifth Revision, 2002). Extracted text: `<local extracted text>\IS 1893\IS-1893-Part1-fulltext.txt`.

**Edition note — important:** the same folder also has `1893.pdf`, the **1984 edition (Fourth Revision)** — that one is **superseded** and was not used. IS 1893 split into 5 parts in 2002 (Part 1 General/Buildings, Part 2 Liquid retaining tanks, Part 3 Bridges/retaining walls, Part 4 Industrial structures, Part 5 Dams/embankments) — only Part 1 exists in this library so far. Per the code's own note, Parts 2–5 not yet finalized at the time of the 2002 edition should fall back to the 1984 edition's relevant clauses for structures other than buildings — not relevant to the maintainer's building-design work.

**Lesson applied from the IS 875 audit:** Annex E (zone factors for ~180 individual towns) has the same multi-column layout that scrambled IS 875's tables under linear text extraction — it is **not reproduced here**; pull it by page for a specific project location rather than trust a reconstructed list.

**Audited 2026-09-11.** Much cleaner than IS 875's audit. Verified the two genuinely multi-column tables (Table 1 bearing-pressure-increase, Table 7 response-reduction-factor) against word-level PDF coordinates, and the core design-spectrum formulas against a clean re-extraction of that page. **Table 7 was perfect** — all 11 rows matched exactly. **Table 1 had one row missing** (piles not resting on rock — 25%/25% for medium/soft soil, no Type I value applies) — restored below. Everything else (zone factors, damping table, importance factor, imposed-load-% table, the S_a/g piecewise formulas) had already read cleanly as single-column data and is confirmed correct.

## Scope (Cl 1)
Seismic loads and earthquake-resistant design for buildings, elevated structures, industrial/stack-like structures, bridges, dams, embankments, retaining walls. Doesn't apply to temporary elements (scaffolding, temporary excavations) or cover *construction* features (detailing is IS 4326/13827/13828/13920/13935 territory instead).

## Key terminology (Cl 3–4)
- **Soft storey:** lateral stiffness < 70% of the storey above, or < 80% of the average of the 3 storeys above.
- **Weak storey:** lateral *strength* < 80% of the storey above.
- **Dual system:** shear walls (or braced frames) + moment frames, where the two share load per their relative stiffness AND the moment frames alone can resist ≥ 25% of the base shear independently.
- **Response Reduction Factor (R):** how much the elastic base shear gets cut down to get the design force, on the strength of ductile/frictional energy dissipation.
- **Seismic weight (W):** full dead load + the applicable fraction of imposed load (not the whole imposed load — see Table 8 below).

## Load combinations (Cl 6.3) — the direct daily-use companion to IS 456's Table 18
- **Plastic design of steel structures:** 1.7(DL+IL); 1.7(DL±EL); 1.3(DL+IL±EL).
- **Limit state design of RCC/PSC** *(confirms and extends [[IS 456 - Plain and Reinforced Concrete]]'s Table 18)*: **1.5(DL+IL); 1.2(DL+IL±EL); 1.5(DL±EL); 0.9DL±1.5EL.**
- **Orthogonal combination (Cl 6.3.2.2):** where lateral-resisting elements aren't aligned with orthogonal axes, design for 100% of EL in one direction + **30%** in the other, both signs: (±ELx ± 0.3ELy) and (±0.3ELx ± ELy).
- **Three-component combination (Cl 6.3.4):** when max response from one direction occurs, the other two are assumed at 30% of their max — check all sign combinations, or use SRSS: EL = √(ELx² + ELy² + ELz²) as an alternative.
- **Permissible stress increase (Cl 6.3.5.1):** elastic/working-stress method, **+1/3** on material permissible stresses when EL is combined with other loads — capped at yield stress for definite-yield steels, 80% of ultimate (or 0.2% proof stress, whichever smaller) for non-definite-yield steels, and 2/3 of modulus of rupture for prestressed concrete tensile fibre stress.
- **Table 1 — bearing pressure increase (Cl 6.3.5.2), % increase by foundation type × soil type** *(verified against source word coordinates 2026-09-11 audit — one row had been dropped from the first draft, now restored; every other value checked out exactly)*: piles resting on rock/hard soil (Type I): **50%** regardless of what soil the pile passes through. **Piles not covered under that case (i.e. not resting on Type I) — 25% for medium soil, 25% for soft soil** (no Type I value applies here by definition — *this whole row was missing from the first draft*). Raft foundations: **50%** across all three soil types. Isolated RCC footings with tie beams: 50% (rock/hard soil), **25%** (medium/soft soil). Isolated RCC footings *without* tie beams, or unreinforced strip foundations: 50% (rock), 25% (medium soil), **not permitted at all on soft soil** (this combination is explicitly disallowed, not just discounted). Well foundations: 50%/25%/25%.
  - **Liquefaction flag:** submerged loose sand (SP classification) with N < 15 (Zones III/IV/V) or N < 10 (Zone II) risks liquefaction — avoid such sites for new/important construction, or use deep piles into non-liquefiable strata.

## Design spectrum (Cl 6.4) — the core calculation

**Design horizontal seismic coefficient:**
**A_h = (Z·I)/(2·R) × (S_a/g)**, with a floor: for any structure with T < 0.1s, A_h shall not be taken less than **Z/2** regardless of I/R.

- **Z — Zone factor, Table 2:** four zones (Zone I was merged into II in this revision — only II/III/IV/V exist now).

  | Zone | Seismic intensity | Z |
  |---|---|---|
  | II | Low | **0.10** |
  | III | Moderate | **0.16** |
  | IV | Severe | **0.24** |
  | V | Very severe | **0.36** |

- **I — Importance Factor, Table 6:** **1.5** for hospitals, schools, monumental structures, emergency buildings (telephone exchange, TV/radio stations, railway/fire stations), large community halls (cinemas, assembly halls, subway stations), power stations. **1.0** for all other buildings. (Designer may choose higher values; doesn't apply to short-duration temporary structures.)
- **R — Response Reduction Factor, Table 7** (ratio I/R must never exceed 1.0):

  | System | R |
  |---|---|
  | Ordinary RC moment frame (OMRF) | **3.0** |
  | Special RC moment frame (SMRF) | **5.0** |
  | Steel frame, concentric braces | **4.0** |
  | Steel frame, eccentric braces | **5.0** |
  | Steel SMRF (per SP 6(6)) | **5.0** |
  | Load-bearing masonry — unreinforced | **1.5** |
  | Masonry + horizontal RC bands | **2.5** |
  | Masonry + horizontal bands + vertical corner/jamb bars | **3.0** |
  | Ordinary RC shear walls | **3.0** |
  | Ductile shear walls (per IS 13920) | **4.0** |
  | Dual: ordinary shear wall + OMRF | **3.0** |
  | Dual: ordinary shear wall + SMRF | **4.0** |
  | Dual: ductile shear wall + OMRF | **4.5** |
  | Dual: ductile shear wall + SMRF | **5.0** |

  R values apply to the building as a whole with its lateral system, not to isolated elements. **Ductile shear walls are prohibited in Zones IV and V** unless detailed per IS 13920.

- **S_a/g — average response acceleration coefficient**, piecewise by natural period T and founding-soil type (5% damping):

  | Soil type | 0.00 ≤ T ≤ 0.10 | mid-range | upper range |
  |---|---|---|---|
  | Rock / hard soil | 1+15T | **2.50** (0.10<T≤0.40) | 1.00/T (0.40<T≤4.00) |
  | Medium soil | 1+15T | **2.50** (0.10<T≤0.55) | 1.36/T (0.55<T≤4.00) |
  | Soft soil | 1+15T | **2.50** (0.10<T≤0.67) | 1.67/T (0.67<T≤4.00) |

  **Table 3 — damping multiplying factors** (to adjust S_a/g off the 5%-damping baseline): 0%→3.20, 2%→1.40, 5%→1.00, 7%→0.90, 10%→0.80, 15%→0.70, 20%→0.60, 25%→0.55, 30%→0.50. **Steel buildings: 2% damping. RCC buildings: 5% damping** (Cl 7.8.2.1) — for dynamic analysis specifically.
- **Depth adjustment (Cl 6.4.4):** underground structures/foundations at ≥ 30 m depth use **half** the Cl 6.4.2 value; between ground level and 30 m, linearly interpolate between A_h and 0.5A_h.
- **Vertical spectrum (Cl 6.4.5):** **2/3** of the horizontal spectrum value, when vertical effects need checking (large spans, stability-critical structures, prestressed/cantilevered members — Cl 6.1.1 flags these as the cases where vertical acceleration can't be assumed insignificant).

## Building irregularities (Cl 7.1, Tables 4–5) — trigger dynamic analysis and design attention

**Plan irregularities (Table 4):** torsional (max storey drift at one end > **1.2×** the average of both ends, with rigid diaphragms); re-entrant corners (both projections > **15%** of plan dimension); diaphragm discontinuity (cut-outs > **50%** of diaphragm area, or stiffness change > 50% floor-to-floor); out-of-plane offsets in the lateral system; non-parallel lateral-system/orthogonal-axis orientation.

**Vertical irregularities (Table 5):** soft storey (< 70% of storey above, or < 80% of 3-storeys-above average); **extreme soft storey** (< 60% / < 70% — e.g. stilt buildings); mass irregularity (any storey's seismic weight > **200%** of an adjacent storey's, roofs exempted); vertical geometric irregularity (lateral-system horizontal dimension > **150%** of the adjacent storey's); in-plane discontinuity in vertical lateral elements (offset greater than the element's own length); weak storey (lateral strength < 80% of the storey above).

## Design lateral force (Cl 7.5–7.7)

- **Design seismic base shear: V_B = A_h × W** (W = total seismic weight, Cl 7.4 — full dead load + Table 8's fraction of imposed load per floor, roof imposed load excluded entirely per Cl 7.3.2).
- **Table 8 — imposed load fraction for seismic weight:** floor UDL **≤ 3.0 kN/m² → 25%** counted; **> 3.0 kN/m² → 50%** counted. (This overrides — doesn't stack with — IS 875 Part 2's own storey-count-based imposed-load reduction; Cl 7.3.3 explicitly says no further Part-2 style reduction applies here.)
- **Fundamental natural period, T_a (Cl 7.6) — empirical, absent detailed analysis:**
  - Moment frame, **no infill**: **T_a = 0.075h⁰·⁷⁵** (RC frame) or **0.085h⁰·⁷⁵** (steel frame), h = height in m (excludes unconnected basements).
  - **All other buildings, including infilled moment frames:** **T_a = 0.09h/√d**, d = base dimension in the direction of the force.
- **Vertical distribution of base shear:** Q_i = V_B × (W_i·h_i²)/Σ(W_j·h_j²) — the classic h² weighting by floor seismic weight and height.
- **Rigid vs flexible diaphragm (Cl 7.7.2, Note 1):** a diaphragm is flexible if its max lateral displacement from the chord exceeds **1.5×** the diaphragm's average displacement. Monolithic RC slab-beam floors, or precast + topping screed, count as rigid.
- **Dynamic analysis is mandatory (Cl 7.8.1), not optional, for:**
  - Regular buildings **> 40 m** in Zones IV/V, or **> 90 m** in Zones II/III.
  - Irregular buildings (per Table 4/5) **> 12 m** in Zones IV/V, or **> 40 m** in Zones II/III.
  - (Recommended, though not mandatory, below the height triggers in Zones II/III if irregular.)
  - Whichever method (time history or response spectrum) is used, compare V_B against a base shear computed with the empirical T_a — if the dynamic-analysis base shear comes in lower, **scale all response quantities up** by the ratio to the empirical-T_a base shear (this is the "lower bound" rule).
  - Damping for the dynamic analysis itself: **2% steel, 5% RCC.**
  - **Modal combination:** CQC method generally; SRSS permitted only where modes aren't closely spaced (natural frequencies differing by ≤ 10% of the lower one count as "closely spaced" — Cl 3.2).
  - Modes considered must capture **≥ 90%** of total seismic mass, missing-mass-corrected beyond that.

## Torsion (Cl 7.9)
Design eccentricity at floor i, whichever is more severe:
**e_di = 1.5·e_si + 0.05·b_i**, or **e_si − 0.05·b_i**
(e_si = static eccentricity between centre of mass and centre of rigidity; b_i = floor plan dimension perpendicular to the force direction). The 1.5 factor is dynamic amplification; 0.05 is accidental eccentricity. **Negative torsional shear is neglected**, not netted off.

## Soft storey design (Cl 7.10)
Two alternative paths for a soft/open storey (e.g. stilt parking) once dynamic analysis (including infill stiffness effects) is done:
(a) design the soft storey's columns/beams for **2.5×** the storey shears and moments from the seismic analysis, or
(b) provide symmetrically-placed shear walls (as far from the building centre as feasible) designed for **1.5×** the calculated lateral storey shear, in addition to the ordinarily-designed columns.

## Deformation limits (Cl 7.11)
- **Storey drift limit: ≤ 0.004 × storey height**, under the design lateral force (no lower-bound Cl 7.8.2 floor applied for this specific check). No drift limit for a single-storey building specifically designed to accommodate its drift.
- **Building separation:** adjacent buildings/units need a gap ≥ **R × sum of the calculated storey displacements** of each — halve to R/2 if floor levels of the two units align.

## Miscellaneous design forces (Cl 7.12)
- **Vertical cantilever projections** above roof (towers, tanks, parapets, chimneys/smoke stacks): design for **5× A_h** — lump their weight with the roof weight in the main analysis. This increase is for the projection and its connection only, not the main structure.
- **Horizontal projections** (cornices, balconies), **Zones IV/V only**: design for **5× (10/3·A_h)** = 5× the vertical coefficient.
- **Compound walls:** use A_h with **I = 1.0** specifically (regardless of the importance factor that might apply to the main building).
- **Connections between parts** (beams-columns, columns-footings): must transmit ≥ **(Q_i/W_i) or 0.05×** (whichever greater) times the weight of the smaller connected part or its DL+IL reaction — **friction cannot be counted on** to satisfy this.
- **Foundations, Zones IV/V:** individual spread footings/pile caps must be tied together (per IS 4326 Cl 5.3.4.1) unless founded directly on rock; ties sized for **A_h/4 ×** the larger column/pile load in tension and compression.

## Annexes (not reproduced)
- Annex A/B/C — epicentre map, tectonic features, lithology (graphical, not table-extractable).
- **Annex D** — MSK-64 comprehensive intensity scale (Zone II↔VI-or-less, III↔VII, IV↔VIII, V↔IX-and-above).
- **Annex E** — zone factors for ~180 individual towns. Scrambled by the same multi-column extraction problem found in IS 875 — pull by page for a specific town rather than trust a reconstructed list here.

## Cross-references
- [[IS 456 - Plain and Reinforced Concrete]] — Cl 6.1.3 explicitly requires IS 456/IS 1343 shear-and-bond design and IS 13920 ductile detailing for RC members under this code; the RCC load combinations here (1.5(DL+IL) etc.) match and extend IS 456's Table 18.
- [[IS 875 Part 2 - Imposed Loads]] — Table 8 here (25%/50% imposed load fraction) explicitly overrides Part 2's storey-count reduction for seismic weight purposes; roof imposed load is dropped entirely.
- [[IS 875 Part 5 - Special Loads and Load Combinations]] — Note 3/6 there already flagged that the *reduced* Part 2 imposed load must not be combined with EL; this note's Table 8 is the actual seismic-specific rule that governs instead.
- IS 13920 (ductile detailing) — referenced throughout for anything claiming SMRF or ductile-shear-wall status; not yet built, natural next code.
- IS 4326, IS 13827, IS 13828, IS 13935 — construction/detailing guidance this Part explicitly defers to; not yet built.
- Parent plan: Code Design Assistant.
