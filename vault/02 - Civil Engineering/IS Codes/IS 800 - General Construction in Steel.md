---
status: active
project: civil-engineering
type: reference
---
# IS 800 — General Construction in Steel (Code of Practice)

**IS 800:2007, Third Revision** — limit state design (superseded the 1984 working-stress edition, which is also in the source library at `CED7-Structural engineering\800.pdf` — do not build from that copy; this note is from `is.800.2007.pdf` in the same folder, 158 pages). Includes **Amendment No. 1 (January 2012)**, which corrects several symbols/formulas/tables in the original 2007 print — every clause below already reflects the amended text where the amendment touches it; flagged inline wherever a correction changed something non-trivial. Built and **audited 2026-09-12** (matching the rigor of every other code in [[IS Codes]]), all 17 Sections + Annexes A–H, following the same page-anchored, no-hallucination method as [[IS 456 - Plain and Reinforced Concrete]].

**Audit findings (2026-09-12):** re-checked every item flagged during the build plus a spot-check of tables taken from clean-looking (but not image-verified) linear text. Found and fixed several real errors: **Table 19** (bolt hole clearances) had oversize/short-slot/long-slot columns swapped, and missed that the long-slot clearance is 2.5×diameter, not a fixed mm value; the **fire-resistance limiting-temperature formula** was written with a division where the source uses multiplication (T1 = 905 − 690·rf, not 905 − 690/rf — these behave completely differently); **bolt combined shear+tension** was logged as a linear interaction when the source uses a quadratic one for both bearing-type and friction-grip bolts, and the bearing-type bolt's own tension-capacity and combined-check clauses (§10.3.5/10.3.6) were missing entirely. Also recovered content earlier marked as unrecoverable: the **prying-force formula** (§10.4.7), **Annex D's column effective-length K-factor equations** (turned out to survive cleanly on the right page), and **Annex C's floor-vibration formulas** (frequency, damping, acceleration — not just a specialist-literature pointer as first logged). One flagged item was resolved as a reasoning error rather than a source problem: the Table 2/Amendment 1 "≥42ε" cap direction is correct once the r₁ range is worked through properly (it's a floor, not a ceiling — see the note at that table). Confirmed accurate on spot-check: Table 1 (steel grades), Table 2 (cross-section classes), Table 4 (load factors, now with the two-line DL+LL+CL+WL/EL row precisely transcribed), Table 10/11 (buckling class/effective length), Table 15 (LTB effective length), Table 20 (friction coefficients), Table 21 (min fillet weld size), Table 23 (seismic response reduction factors), and the Section 8 shear-area formulas. Added two small gaps found along the way: Table 22 (angled fillet-weld throat factor) and the weld effective-length rule.

## Contents map (Sections 1–17 + Annexes A–H)

1 General · 2 Materials · 3 General Design Requirements · 4 Methods of Structural Analysis · 5 Limit State Design · 6 Tension Members · 7 Compression Members · 8 Members Subjected to Bending · 9 Members Subjected to Combined Forces · 10 Connections · 11 Working Stress Design · 12 Design and Detailing for Earthquake Loads · 13 Fatigue · 14 Design Assisted by Testing · 15 Durability · 16 Fire Resistance · 17 Fabrication and Erection. Annexes: A List of Referred Standards · B Analysis and Design Methods · C Design Against Floor Vibration · D Effective Length of Columns · E Elastic Lateral Torsional Buckling · F Connections · G Steelwork Tenders and Contracts · H Plastic Properties of Beams.

## 1. General [p.15–24 / source p.1–11]

- **1.1 Scope** — general construction with hot-rolled steel sections, riveted/bolted/welded. Excludes bridges, chimneys, cranes, tanks, transmission towers, bulk storage, tubular structures, cold-formed light-gauge sections (separate standards). Loads/load combinations: refer IS 875 (dead/live/snow/wind) and IS 1893 Part 1 (seismic) — IS 800 itself doesn't set load values. Seismic provisions here cover steel frames only.
- **1.3 Terminology** — a long alphabetical glossary (1.3.1–1.3.120+, source p.1–5). Not reproduced here — reference-by-page; pull the specific term if a definition matters for a specific question.
- **1.4 Symbols** — the master symbol list used throughout the code (source p.5–11). Not reproduced as a standalone block — each symbol is defined inline where it's used in the formulas below, which is where it's actually needed.
- **1.8 Convention for Member Axes**: z-z = axis along the member (longitudinal), y-y = major axis (usually parallel to flanges), x-x (sometimes shown as the minor axis convention differs by section type) — see Fig. 1. Get this right before reading any buckling/bending clause — every "about the y-y axis" reference depends on it.

## 2. Materials [p.24–28 / source p.12–14]

- **2.2.4.1 Physical properties** (all grades): unit mass ρ = 7850 kg/m³ · modulus of elasticity E = 2.0×10⁵ N/mm² (MPa) · Poisson's ratio μ = 0.3 · modulus of rigidity G = 0.769×10⁵ N/mm² (MPa) · coefficient of thermal expansion α = 12×10⁻⁶/°C.
- **Table 1 — Tensile Properties of Structural Steel Products** [source p.13–14] (verified against rendered page images — this table is a dense multi-spec grid that scrambled badly under linear text extraction, same risk class flagged throughout this session; do not trust a re-extraction of this page without checking it visually). The grade actually used for almost all daily structural steel design is **IS 2062**:

| Grade | fy (MPa), t<20mm | fy, 20–40mm | fy, >40mm | fu (MPa) min | Elongation % min |
|---|---|---|---|---|---|
| E165 (Fe 290) | 165 | 165 | 165 | 290 | 23 |
| E250 (Fe 410 W) A/B/C | 250 | 240 | 230 | 410 | 23 |
| E300 (Fe 440) | 300 | 290 | 280 | 440 | 22 |
| E350 (Fe 490) | 350 | 330 | 320 | 490 | 22 |
| E410 (Fe 540) | 410 | 390 | 380 | 540 | 20 |
| E450 (Fe 570) D | 450 | 430 | 420 | 570 | 20 |
| E450 (Fe 590) E | 450 | 430 | 420 | 590 | 20 |

**E250 (Fe 410 W) is the grade almost every Indian structural steel section (rolled I/H/channel/angle) is supplied in** — fy = 250 MPa is the number to reach for by default unless a project specifies higher-grade steel. Full table (rivets to IS 513/814/1079, bolts to IS 1367, and IS 1875/1990/3039/6240/7557/9295/10748 product grades) reference-by-page — a niche spec beyond IS 2062 is rare enough in practice to pull directly rather than memorize.

## 3. General Design Requirements [p.28–36 / source p.15–20]

- **3.1.2** — Design shall normally be by **limit state method** (Section 5). Working stress design (Section 11) is a fallback only where limit state can't be conveniently applied.
- **3.2/3.5 Loads and load combinations** — dead (IS 875-1), imposed/live/crane/snow (IS 875-2/4), wind (IS 875-3), earthquake (IS 1893-1); IS 800 doesn't set load values itself, just says how to combine them (factors in Table 4, §5 below). Base combinations: (a) DL+IL, (b) DL+IL+(wind or EQ), (c) DL+(wind or EQ), (d) DL+erection load. **Wind and earthquake are never combined simultaneously** — check each separately. Crane loads: vertical (with impact) from one crane (or two if tandem) + vertical (no impact) from all other positioned cranes + horizontal thrust from one crane (two if tandem); lateral (surge) and longitudinal thrust on the crane rail also don't act simultaneously with each other.
- **3.7 Classification of cross-sections** — four classes by local-buckling behaviour, governs whether a section can reach full plastic capacity: **Class 1 (Plastic)** — can form a plastic hinge with the rotation capacity needed for a full plastic collapse mechanism. **Class 2 (Compact)** — reaches plastic moment but can't sustain the hinge through further rotation. **Class 3 (Semi-compact)** — extreme fibre reaches yield stress but can't develop the full plastic moment. **Class 4 (Slender)** — local buckling happens before yield is even reached; design per IS 801 or by deducting the excess width beyond the semi-compact limit. A section with elements in different classes is classified by its **least favourable (most restrictive) element**.

**Table 2 — Limiting Width-to-Thickness Ratio** [source p.18] (verified against a rendered page image — dense multi-row grid, ε-symbol formulas didn't survive linear extraction cleanly). ε = √(250/fy) throughout.

| Element | Ratio | Class 1 Plastic | Class 2 Compact | Class 3 Semi-compact |
|---|---|---|---|---|
| Outstanding compression flange, rolled | b/tf | 9.4ε | 10.5ε | 15.7ε |
| Outstanding compression flange, welded | b/tf | 8.4ε | 9.4ε | 13.6ε |
| Internal compression flange, bending | b/tf | 29.3ε | 33.5ε | 42ε |
| Internal compression flange, axial compression | b/tf | n/a | n/a | 42ε |
| Web of I/H/box, neutral axis at mid-depth | d/tw | 84ε | 105ε | 126ε |
| Web of I/H/box, generally, r₁ negative | d/tw | 84ε/(1+r₁) | 105.0ε/(1+r₁) | 126.0ε/(1+2r₂) |
| Web of I/H/box, generally, r₁ positive | d/tw | 84ε/(1+r₁), cap 42ε* | 105.0ε/(1+1.5r₁), cap 42ε* | 126.0ε/(1+2r₂), cap 42ε* |
| Web of I/H/box, axial compression | d/tw | n/a | n/a | 42ε |
| Web of a channel | d/tw | 42ε | 42ε | 42ε |
| Angle, bending (both b/t and d/t must satisfy) | b/t, d/t | 9.4ε | 10.5ε | 15.7ε |
| Single/double-angle (separated), axial (all 3 of b/t, d/t, (b+d)/t) | — | n/a | n/a | 15.7ε / 15.7ε / 25ε |
| Outstanding angle leg, back-to-back double angle | d/t | 9.4ε | 10.5ε | 15.7ε |
| Outstanding angle leg, continuous contact | d/t | 9.4ε | 10.5ε | 15.7ε |
| Stem of T-section (rolled/cut from I or H) | d/t † | 8.4ε | 9.4ε | 18.9ε |
| Circular hollow tube — moment | D/t | 42ε² | 52ε² | 146ε² |
| Circular hollow tube — axial compression | D/t | n/a | n/a | 88ε² |

*\* Amendment 1 (2012) corrects these three r₁-positive cells from "but ≤ 42ε" to "but ≥ 42ε" — **audit note 2026-09-12: re-checked the physics, and ≥42ε (a floor, not a ceiling) is actually the correct direction.** As r₁ increases (web axial compression dominates), 84ε/(1+r₁) etc. *decreases* — and at r₁=1 it already equals exactly 42ε (the pure-axial-compression limit from the row above). Beyond that point the raw formula would keep dropping below 42ε, which can't be right: a web under combined bending+compression should never be held to a *stricter* limit than pure axial compression alone. So the cap has to be a floor (never go below 42ε), confirming "≥42ε" is correct and the earlier doubt logged here was simply a reasoning error on this note's part, not a genuine source ambiguity.*

*† Amendment 1 also relabels this row's ratio column from "D/tf" to "d/t" (symbol fix only — the 8.4ε/9.4ε/18.9ε values are unchanged; it's about which dimension the ratio actually measures, applied above).*

Notes: elements beyond semi-compact = Class 4 (Slender). Webs need a shear-buckling check (§8.4.2) when d/t > 67ε. r₁ = actual average axial stress ÷ design compressive stress of web alone; r₂ = actual average axial stress ÷ design compressive stress of overall section (both negative if tensile).

**Table 3 — Maximum Effective Slenderness Ratio (KL/r)** [source p.20] — clean single-column table, no extraction risk:

| Member | Max KL/r |
|---|---|
| Compression member, dead+imposed loads | 180 |
| Tension member with stress reversal (non-wind/seismic) | 180 |
| Compression member, only from wind/EQ combination (no adverse effect elsewhere) | 250 |
| Compression flange of a beam, against lateral-torsional buckling | 300 |
| Tie member in a truss/bracing, reversal into compression from wind/EQ not considered effective | 350 |
| Members always in tension (other than pre-tensioned) | 400 |

Pre-tensioned bracing members (tensioned to avoid sag) are exempt from the slenderness limit entirely.

- **3.9 Resistance to horizontal forces** — provide adequate moment connections or bracing to transmit all horizontal loads to foundations. Wind and earthquake never combined simultaneously (repeated from §3.5).
- **3.10 Expansion joints** — left to designer's judgement, but general guidance: single bay of central bracing → max building length 180 m (covered) / 120 m (open gantries). Two bays of bracing → max spacing between bracing lines 50 m (covered)/30 m (open), max distance from bracing to nearest joint/end 90 m (60 m open), giving max overall length 230 m (covered)/150 m (open). Max building width (single section) 150 m. Within these limits, no separate temperature stress analysis is required.

## 4. Methods of Structural Analysis [p.36–42 / source p.22–27]

Four permitted methods: elastic analysis (4.4), plastic analysis (4.5, requires Class 1 sections), advanced analysis (Annex B), dynamic analysis (per IS 1893-1 — mandatory for seismic design action effects, which must come from elastic analysis at minimum). Frames classified **non-sway** (transverse displacement effectively prevented — braced frames, shear walls, trusses) vs **sway** (moment-resisting frames relying on flexural action) — a rigid-jointed multi-storey frame counts as non-sway only if storey deflection δ under notional horizontal load (§4.3.6) satisfies δ/h ≤ 1/2000 (cladding stiffening not counted) or δ/h ≤ 1/4000 (cladding stiffening counted); otherwise it's sway regardless of bracing. Construction forms: **rigid** (full moment continuity assumed) · **semi-rigid** (known, testable partial restraint, Annex F) · **simple** (hinged, no moment transfer). Base stiffness assumptions (§4.3.4) when not otherwise known: rigidly-connected column → pedestal stiffness = column stiffness above base (or fixed, for very stiff pedestals); nominally-connected → 10% of column stiffness; actual pin/rocker → hinged. Foundation-level boundary condition: pile group/raft/footing on rock or very hard soil → fixed at footing/pile-cap bottom; footing on other soils → hinged; single pile in soil → fixed at 5×pile-diameter depth; column into rock → fixed at the rock interface. Imposed-load arrangement for continuous beams: if live load ≤ 0.75×dead load, may apply to all spans; if >0.75×dead load, must check alternate spans, adjacent-pair spans, and all-spans-loaded cases separately.

## 5. Limit State Design [p.42–48 / source p.27–32]

The core safety-factor framework everything else in the code multiplies through.

- **5.3.3 Design action**: Qd = Σ γfk·Qck — apply Table 4's load factors to characteristic loads.
- **5.4.1 Design strength**: Sd = Su/γm — divide ultimate strength by Table 5's material factor. This Sd = Su/γm form (and Qd = Σγf·Qck) is the basic equation of every capacity check in Sections 6–10.

**Table 4 — Partial Safety Factors for Loads, γf** [source p.29] (verified against a rendered image — column headers didn't survive linear extraction):

| Combination | DL | LL leading | LL accompanying | WL/EL | AL | — Serviceability: DL | LL leading | LL accompanying | WL/EL |
|---|---|---|---|---|---|---|---|---|---|
| DL+LL+CL | 1.5 | 1.5 | 1.05 | — | — | 1.0 | 1.0 | 1.0 | — |
| DL+LL+CL+WL/EL | 1.2 | 1.2 | 1.05 / 0.53 | 0.6 / 1.2 | — | 1.0 | 0.8 | 0.8 | 0.8 |
| DL+WL/EL | 1.5 (0.9)¹ | — | — | 1.5 | — | 1.0 | — | — | 1.0 |
| DL+ER | 1.2 (0.9)¹ | 1.2 | — | — | — | — | — | — | — |
| DL+LL+AL | 1.0 | 0.35 | 0.35 | — | 1.0 | — | — | — | — |

¹ The 0.9 factor applies to DL when dead load helps stability against overturning, or reduces stress caused by other loads — use it for the *favourable* dead-load case, 1.5/1.2 for the *unfavourable* case, and check both. **Audit note 2026-09-12**: re-read Table 4 at high resolution — the DL+LL+CL+WL/EL row is genuinely printed by BIS as two data lines under one combination heading (confirmed, not an extraction artifact): line 1 gives LL(lead)=1.2, LL(accompany)=1.05, WL/EL=0.6 (serviceability 1.0/0.8/0.8/0.8); line 2 gives LL(lead)=1.2, LL(accompany)=0.53, WL/EL=1.2 (no serviceability values printed for line 2). The two lines read as two design cases for the same combination (WL/EL as accompanying vs WL/EL more dominant) — the source doesn't restate which is "leading" for line 2 in the clause text itself, so check both lines' factor sets for a real design rather than assuming only one applies.

**Table 5 — Partial Safety Factor for Materials, γm** [source p.30] — the two everyday numbers: **γm0 = 1.10** (yielding and member buckling resistance), **γm1 = 1.25** (ultimate-stress-governed resistance, e.g. net-section rupture). Connections: bolts (friction or bearing type) and rivets γmf/γmb/γmr = 1.25 both shop and field; **welds γmw = 1.25 shop, 1.50 field** — field welding carries a real strength-factor penalty over shop welding, not just a QA preference.

**5.6 Serviceability extras**: pre-camber for spans >25m ≈ DL deflection + half LL deflection. Unusually flexible structures (height:effective-width of lateral system >5:1) need lateral-vibration check under dynamic wind. γf = 1.0 for all serviceability checks (Table 4 factors are strength-state only).

**Table 6 — Deflection Limits** [source p.31] — practical values, industrial buildings: purlins/girts (live/wind, elastic cladding) span/150; simple-span live-load members (elastic cladding) span/240, (brittle) span/300; cantilevers (elastic) span/120, (brittle) span/150; crane gantry girders (manual) span/500, (electric ≤50t) span/750, (electric >50t) span/1000; columns, no crane, elastic cladding height/150, masonry/brittle height/240; crane+wind column/frame height/200–400 depending on cladding/operation. **Other buildings** (the ones most engineers actually design day to day): floor/roof live load, elements not susceptible to cracking span/300, susceptible span/360; cantilevers span/150 (not susceptible) / span/180 (susceptible); wind on building, elastic cladding height/300, brittle height/500; **inter-storey drift under wind: storey height/300** — this is the number everyone actually checks. Serviceability load factor γf = 1.0 throughout (unity), per §5.6.1 — deflection checks use unfactored service loads, not the Table 4 strength factors. Amendment 1 adds: live load in this deflection check should include all post-construction superimposed dead loads too.

## 6. Design of Tension Members [p.46–49 / source p.32–34]

Design strength Td = min(Tdg, Tdn, Tdb) — yielding, rupture, block shear. Factored tension T must satisfy T < Td.

- **Tdg (yielding of gross section)** = Ag·fy / γm0
- **Tdn (plates, rupture at net section)** = 0.9·An·fu / γm1, where An = [b − n·dh + Σ(psi²/4gi)]·t (b,t = plate width/thickness; dh = bolt hole diameter, +2mm over actual for punched holes; g = gauge between holes; ps = staggered pitch; n = holes in the critical section; i = sum over inclined legs). Preliminary sizing shortcut: Tdn ≈ α·An·fu/γm1, α = 0.6 (1–2 bolts) / 0.7 (3 bolts) / 0.8 (≥4 bolts) along the connection length.
- **Tdn (threaded rods)** = 0.9·An·fu/γm1, An = net root area at the thread.
- **Tdn (single angle, one leg connected, shear lag)** = 0.9·Anc·fu/γm1 + β·Ago·fy/γm0, where β = 1.4 − 0.076(w/t)(fy/fu)(bs/Lc), capped **0.9·fu·γm0/(fy·γm1)** and floored ≥0.7 (w = outstand leg width, bs = shear-lag width per Fig.6, Lc = end-connection length along load direction). *Amendment 1 flag: the cap is amended from "fuγm0/(fyγm1)" to "0.9 fuγm0/(fyγm1)" — this note already shows the corrected 0.9× version; a fresh read of an un-amended 2007 print would be missing that 0.9 factor.* Same equation applies to double angles/channels/I-sections/other rolled sections with one-leg-or-more gusset connections (6.3.4), with β's shear-lag width bs measured from the outstanding leg's farthest edge to the nearest bolt/weld line in the connected leg.
- **Tdb (block shear, bolted connections)** = smaller of [Avg·fy/(√3·γm0) + 0.9·Atn·fu/γm1] or [0.9·Avn·fu/(√3·γm1) + Atg·fy/γm0] — Avg/Avn = gross/net shear area, Atg/Atn = gross/net tension area along the respective block-shear failure planes.

## 7. Design of Compression Members [p.48–52, 58–59 / source p.34–35, 44–45]

Design strength Pd = Ae·fcd, must satisfy P < Pd. Members fail by flexural buckling; strength is defined by **buckling class a/b/c/d** (Table 10) which sets the imperfection factor α (Table 7).

**The design compressive stress formula** [source p.34] (verified against image — badly scrambled in linear extraction):

- fcd = (fy/γm0) / [φ + (φ² − λ²)^0.5] = χ·fy/γm0 ≤ fy/γm0
- φ = 0.5[1 + α(λ − 0.2) + λ²]
- λ (non-dimensional effective slenderness) = √(fy/fcc) = √[fy·(KL/r)²/(π²E)]
- fcc (Euler buckling stress) = π²E/(KL/r)²
- χ (stress reduction factor) = 1/[φ + (φ²−λ²)^0.5]

Tables 8 (χ by class/λ) and 9 (fcd by class/fy/KL·r) are pre-computed convenience lookups of the same formula above — not reproduced, just apply the formula directly or pull the table by page if a quick lookup beats the arithmetic.

**Table 7 — Imperfection Factor, α** [source p.34, clean text]: buckling class **a = 0.21, b = 0.34, c = 0.49, d = 0.76** — smaller α = less imperfection sensitivity = higher buckling strength for the same slenderness.

**Table 10 — Buckling Class of Cross-Sections** [source p.44] (verified against image):

| Section | Condition | Axis | Class |
|---|---|---|---|
| Rolled I-section, h/bf > 1.2 | tf ≤ 40mm | z-z / y-y | a / b |
| Rolled I-section, h/bf > 1.2 | 40mm < tf ≤ 100mm | z-z / y-y | b / c |
| Rolled I-section, h/bf ≤ 1.2 | tf ≤ 100mm | z-z / y-y | b / c |
| Rolled I-section, h/bf ≤ 1.2 | tf > 100mm | z-z / y-y | d / d |
| Welded I-section | tf ≤ 40mm | z-z / y-y | b / c |
| Welded I-section | tf > 40mm | z-z / y-y | c / d |
| Hollow section | hot-rolled | any | a |
| Hollow section | cold-formed | any | b |
| Welded box section | generally | any | b |
| Welded box section | thick welds, b/tf<30 or h/tw<30 | z-z / y-y | c / c |
| Channel, angle, T, solid sections | — | any | c |
| Built-up member | — | any | c |

*(The 40mm<tf≤100mm row reflects Amendment 1's correction — the un-amended 2007 print misprints this as "40 ≤ mm < tf ≤ 100 mm".)*

**Table 11 — Effective Length of Prismatic Compression Members** [source p.45] (verified against image; row 2 reflects Amendment 1's correction to columns 1–2):

| One end: Translation / Rotation | Other end: Translation / Rotation | Effective length KL |
|---|---|---|
| Restrained / Restrained | Free / Free | 2.0L (fixed base, free cantilever top) |
| Restrained / Free *(Amendment 1 — was printed "Free/Restrained")* | Free / Restrained | 2.0L |
| Restrained / Free | Restrained / Free | 1.0L (pinned both ends) |
| Restrained / Restrained | Free / Restrained | 1.2L |
| Restrained / Restrained | Restrained / Free | 0.8L |
| Restrained / Restrained | Restrained / Restrained | 0.65L (fixed both ends) |

L = unsupported length (§7.2.1: centre-to-centre of intersections with supporting members, or free-standing length from the last support for a free end).

**7.2 Effective length — other notes**: eccentric beam-to-column connections get the same restraint as concentric ones, provided the connection carries across the column flange/web and the beam web stays within/in contact with the column section (otherwise use the distance between restraint points, non-sway frames only). Stepped columns: effective length procedure in Annex D-2 (single-stepped) / D-3 (double-stepped). Second-order/advanced analysis frames: effective length per Annex D-1.

**7.3–7.8 (design details, column bases, angle struts, laced/battened columns, back-to-back double angles)** — covered at a summary level here given the scale of this build; the governing formulas for laced/battened column design (lacing angle 40-70°, lacing slenderness, batten spacing/thickness rules) and column base plate design (bearing pressure, moment capacity) are in source p.35–46 — pull directly for a specific design, not yet converted into this note.

## 8. Design of Members Subjected to Bending [p.67–73, 89 / source p.52–59, 65]

Factored moment M must satisfy M < Md.

**8.2.1 Laterally supported beams** (compression flange fully restrained): when factored shear ≤ 0.6Vd —
- **Md = βb·Zp·fy/γm0**, capped at **1.2·Ze·fy/γm0** (simply supported) or **1.5·Ze·fy/γm0** (cantilever) to avoid irreversible serviceability deformation.
- βb = 1.0 (plastic/compact sections); βb = Ze/Zp (semi-compact).
- When shear > 0.6Vd: Md = Mdv (reduced bending strength under high shear, per §9.2 — moment-shear interaction).
- Holes in the tension zone can be ignored if Anf/Agf ≥ (fy/fu)(γm1/γm0)/0.9 — otherwise use a reduced effective flange area satisfying that ratio. Compression-zone fastener holes are ignored except oversize/slotted holes or unfilled holes.
- Shear lag (flange effectiveness away from webs) can be ignored if outstand elements have bo ≤ Lo/20, internal elements bi ≤ Lo/10 (Lo = distance between points of zero moment).

**8.2.2 Laterally unsupported beams** — LTB check not required (treat as laterally supported) when: bending is about the minor axis; section is hollow (RHS/CHS) or solid bar; or λLT < 0.4 for major-axis bending. Otherwise:

- **Md = βb·Zp·fbd**, fbd = χLT·fy/γm0
- **χLT** = 1/{φLT + [φLT² − λLT²]^0.5} ≤ 1.0, where φLT = 0.5[1 + αLT(λLT − 0.2) + λLT²]
- **αLT (imperfection parameter)** = 0.21 for rolled sections, **0.49 for welded sections** — welded beams get meaningfully less LTB capacity than rolled ones at the same slenderness, same logic as the buckling-class split in Table 10.
- **λLT** = √(βb·Zp·fy/Mcr) ≤ √(1.2·Ze·fy/Mcr) = √(fy/fcr,b)
- **Mcr (elastic critical moment)**, simply-supported prismatic symmetric sections: Mcr = √{[(π²EIy)/(LLT²)]·[GIt + (π²EIw)/(LLT²)]} = βb·Zp·fcr,b
- Simplified form for standard rolled/welded doubly-symmetric I-sections: **Mcr = (π²EIy·hf)/(2·LLT²) · [1 + (1/20)(LLT/ry)²/(hf/tf)²]^0.5**, and **fcr,b = 1.1π²E/(LLT/ry)² · [1 + (1/20)(LLT/ry)²/(hf/tf)²]^0.5** (Table 14 tabulates fcr,b from this for convenience — reference-by-page, same call as Tables 8/9). It = Σbi·ti³/3 (open section, torsional constant), Iw = warping constant, Iy/ry = weak-axis moment of inertia/radius of gyration, hf = centre-to-centre flange distance, tf = flange thickness. Non-symmetric/other-loading sections: use Annex E's more exact method.

**8.3 Effective length for LTB (LLT)**: simply supported beams with end torsional restraint but no continuous lateral restraint — per **Table 15** below. Beams with intermediate lateral restraints along the span: LLT = distance between restraints (1.2× that distance for destabilizing loads not acting at shear centre). Cantilevers: separate table (Table 16, not reproduced) by support condition. Intermediate restraints must resist 2.5% of max compression-flange force divided among restraint points (plus 1% at each point individually); for a connected series of beams/trusses, total restraint force = 2.5% + 1.25% per additional member, capped 7.5%.

**Table 15 — Effective Length for Simply Supported Beams, LLT** [source p.58] (verified against image; row iii reflects Amendment 1's correction):

| Torsional restraint | Warping restraint | Normal loading | Destabilizing loading |
|---|---|---|---|
| Fully restrained | Both flanges fully restrained | 0.70L | 0.85L |
| Fully restrained | Compression flange fully restrained | 0.75L | 0.90L |
| Fully restrained | Both flanges **partially** restrained *(Amendment 1 — was mis-printed identical to row 1)* | 0.80L | 0.95L |
| Fully restrained | Compression flange partially restrained | 0.85L | 1.00L |
| Fully restrained | Warping not restrained in both flanges | 1.00L | 1.20L |
| Partially restrained (bottom flange support connection) | Warping not restrained in both flanges | 1.0L + 2D | 1.2L + 2D |
| Partially restrained (bottom flange bearing support) | Warping not restrained in both flanges | 1.2L + 2D | 1.4L + 2D |

D = overall beam depth. Torsional restraint = prevents rotation about the longitudinal axis; warping restraint = prevents flange rotation in its own plane.

**8.4 Shear** — factored V must satisfy V ≤ Vd = Vn/γm0.

- **Plastic shear resistance**: Vn = Vp = Av·fyw/√3.
- **Shear area (Av)**: I/channel, major-axis bending — hot-rolled h·tw, welded d·tw; minor-axis bending (either) — 2·b·tf. Rectangular hollow (uniform thickness) — loaded parallel to depth: A·h/(b+h); parallel to width: A·b/(b+h). Circular hollow tube: 2A/π. Plates/solid bars: A. (A = cross-section area, b = breadth, d = clear web depth between flanges, h = overall depth, tf/tw = flange/web thickness.)
- **Shear buckling check required** when d/tw > 67ε (unstiffened web) or > 67ε√(Kv/5.35) (stiffened, Kv = shear buckling coefficient per §8.4.2.2); ε = √(250/fy).
- Shear buckling design (simple post-critical method for I-girder webs with transverse stiffeners at supports, or tension-field method) — Vn = Vcr, full derivation and the associated stiffener-design clauses (§8.4.2.2, §8.5, §8.7) not converted into this note given scope; pull source p.59–65 directly for a plate-girder design.

**8.6–8.9 (plate girders with solid webs, stiffener design, box girders, purlins/sheeting rails)** and **8.10 (bending in a non-principal plane)** — not converted; reference-by-page (source p.63–69), lower daily-use frequency than the beam/column sections above.

## 9. Members Subjected to Combined Forces [p.83–86 / source p.69–72]

**9.2 Combined shear and bending**: no moment reduction needed if factored V ≤ 0.6Vd (use Md from §8.2 as-is). When V > 0.6Vd — plastic/compact: **Mdv = Md − β(Md − Mfd) ≤ 1.2·Ze·fy/γm0**, β = (2V/Vd − 1)². Semi-compact: **Mdv = Ze·fy/γm0**. (Md = plastic moment ignoring high shear per 8.2.1.2/8.2.1.1; Mfd = plastic strength of the section excluding the shear area, at γm0.)

**9.3 Combined axial force + bending — this is the beam-column check, one of the most commonly used interactions in practice.**

**9.3.1 Section strength** (material-failure check):
- Plastic/compact: **(My/Mndy)^α1 + (Mz/Mndz)^α2 ≤ 1.0**, or conservatively **N/Nd + My/Mdy + Mz/Mdz ≤ 1.0**. Nd = Ag·fy/γm0 (or Td from §6 for tension).
- **Mnd (reduced flexural strength under combined axial+moment)**, n = N/Nd: Plates — Mnd = Md(1−n²). Welded I/H — Mndy = Mdy[1−((n−a)/(1−a))²] ≤ Mdy (n≥a), Mndz = Mdz(1−n)/(1−0.5a) ≤ Mdz, a = (A−2b·tf)/A ≤ 0.5. **Standard rolled I/H**: n≤0.2 → Mndy = Mdy; n>0.2 → Mndy = 1.56·Mdy(1−n)(n+0.6); Mndz = 1.11·Mdz(1−n) ≤ Mdz (regardless of n). Rectangular hollow/welded box (symmetric, no bolt holes): Mndy = Mdy(1−n)/(1−0.5af) ≤ Mdy, Mndz = Mdz(1−n)/(1−0.5aw) ≤ Mdz, aw=(A−2b·tf)/A≤0.5, af=(A−2h·tw)/A≤0.5. Circular hollow: Mnd = 1.04·Md(1−n^1.7) ≤ Md.
- **Table 17 — Constants α1, α2** [source p.71]: I/channel sections α1 = 5n≥1, α2 = 2. Circular tubes α1=α2=2. Rectangular tubes α1=α2=1.66/(1−1.13n²)≤6. Solid rectangles α1=α2=1.73+1.8n³. (n = N/Nd throughout.)
- Semi-compact (no high shear, no holes): **N/Nd + My/Mdy + Mz/Mdz ≤ 1.0** (same conservative form as plastic/compact's fallback).

**9.3.2 Overall member strength** (buckling-failure check):
- Bending + axial tension: **Meff = [M − ψ·T·Zec/A] ≤ Md** (Md per §8.2.2, LTB strength), ψ = 0.8 if T and M vary independently, else 1.0.
- **Bending + axial compression, biaxial** — both must hold:
  - P/Pdy + Ky·Cmy·My/Mdy + KLT·Mz/Mdz ≤ 1.0
  - P/Pdz + 0.6·Ky·Cmy·My/Mdy + Kz·Cmz·Mz/Mdz ≤ 1.0
  - Pdy, Pdz = compression design strength buckling about minor(y)/major(z) axis (§7). Mdy, Mdz = bending strength about y/z considering laterally unsupported length (§8). Ky = 1+(λy−0.2)ny ≤ 1+0.8ny; Kz = 1+(λz−0.2)nz ≤ 1+0.8nz; KLT = 1 − 0.1λLT·ny/(CmLT−0.25) ≥ 1 − 0.1ny/(CmLT−0.25). ny, nz = ratio of applied axial force to design axial strength about y/z.
- **Table 18 — Equivalent Uniform Moment Factor, Cmy/Cmz/CmLT** [source p.72, this print already reflects Amendment 1's full-table substitution]: uniform moment diagram (ψ between end moments M and ψM, −1≤ψ≤1): **0.6 + 0.4ψ ≥ 0.4** for both uniform and concentrated loading. For moment diagrams with an internal peak (Mh, Ms, αs=Ms/Mh or αh=Mh/Ms), the factor ranges roughly 0.1–0.95 depending on the diagram shape and load type — full breakdown by αs/αh/ψ range in the table, pull source p.72 directly for a specific case rather than transcribing all branches here. **Sway buckling mode: Cmy = Cmz = 0.9 flat**, no diagram-dependence. Cmy uses the z-z bending moment diagram (braced points in y-y direction); Cmz uses y-y diagram (braced z-z); CmLT uses z-z diagram (braced z-z).

## 10. Connections [p.87–92 / source p.73–79]

**10.2 Fastener location/spacing**:
- **Minimum spacing** between fastener centres ≥ 2.5d (d = nominal fastener diameter).
- **Maximum spacing**: 32t or 300mm (whichever less) between adjacent fasteners generally; corrosive exposure tightens the *edge* distance limit to 40mm+4t. Pitch in the direction of stress: ≤16t or 200mm (tension), ≤12t or 200mm (compression) — t = thinner connected plate thickness. Staggered fasteners at ≤75mm gauge: these pitch limits relax by 50%.
- **Edge/end distance minimum**: 1.7×hole diameter (sheared/hand-flame-cut edges) or 1.5×hole diameter (rolled/machine-cut/sawn/planed edges) from hole centre to nearest edge.
- **Maximum edge distance**: 12t·ε (ε=√(250/fy)) from the nearest fastener line to an unstiffened edge — beyond this, tacking fasteners (not load-bearing) are required at ≤32t or 300mm spacing (≤16t or 200mm if weather-exposed).
- **Table 19 — Clearances for Fastener Holes** [source p.73] *(audit correction 2026-09-12: the original entry mislabeled these columns — swapped oversize/short-slot/long-slot and missed that the long-slot clearance is a multiple of diameter, not a fixed mm value)*. Four columns: standard clearance (diameter & slot width) · oversize hole clearance (diameter) · short-slot clearance (length) · long-slot clearance (length). By fastener size: **12–14mm** → 1.0 / 3.0 / 4.0 / **2.5d**; **16–22mm** → 2.0 / 4.0 / 6.0 / **2.5d**; **24mm** → 2.0 / 6.0 / 8.0 / **2.5d**; **>24mm** → 3.0 / 8.0 / 10.0 / **2.5d**. The long-slot length clearance is always 2.5× the fastener's nominal diameter, not a fixed additive figure like the other three columns.
- Countersunk fasteners: deduct half the countersink depth from bearing length; tensile strength reduced 33.3% (no shear reduction).

**10.3 Bearing-type bolts** — design strength Vdb = min(Vdsb, Vdpb) per bolt.
- **Shear**: Vdsb = Vnsb/γmb, **Vnsb = (fu/√3)·(nn·Anb + ns·Asb)** — fu = bolt ultimate tensile strength, nn/ns = number of shear planes with/without threads intercepting the plane, Anb = net (root) shear area, Asb = plain shank area. Thread-in-shear-plane is the default assumption unless proven otherwise.
- **Bearing**: Vdpb = Vnpb/γmb, **Vnpb = 2.5·kb·d·t·fu** — kb = smallest of {e/3d0, p/3d0−0.25, fub/fu, 1.0} (e/p = end/pitch distance, d0 = hole diameter, fub = bolt ultimate stress, fu = plate ultimate stress), t = sum of ply thicknesses bearing in the same direction (or countersunk-adjusted).
- **Long joints** (lj = first-to-last bolt row distance > 15d): reduce shear capacity by βlj = 1.075 − lj/(200d), capped 0.75–1.0.
- **Large grip** (lg = total ply thickness): reduce by βlg = 8d/(3d+lg) = 8/(3+lg/d) when lg>5d; βlg ≤ βlj; grip length ≤ 8d always.
- **Packing plates** >6mm: reduce by βpk = (1 − 0.0125·tpk).
- **Tension** (§10.3.5): Tdb = Tnb/γmb, **Tnb = smaller of {0.90·fub·An, fyb·Asb·(γmb/γm0)}** — fub/fyb = bolt ultimate/yield stress, An = net tensile stress area (root-diameter area if not otherwise specified by the relevant bolt IS), Asb = shank area.
- **Combined shear + tension** (§10.3.6, bearing-type bolts): **(Vsb/Vdb)² + (Tb/Tdb)² ≤ 1.0** — a quadratic (elliptical) interaction, not linear.

**10.4 Friction grip (HSFG) bolts** — slip resistance Vdsf = Vnsf/γmf, **Vnsf = μf·ne·Kh·F0** — μf = slip factor per **Table 20** (typically 0.55 for as-supplied blasted surfaces; ranges 0.10 for untreated/painted-only to 0.52 for grit-blasted+etch-primed, see table below), ne = number of effective friction interfaces, Kh = 1.0 (standard clearance holes) / 0.85 (oversize, short-slotted, or long-slotted loaded perpendicular) / 0.7 (long-slotted loaded parallel), γmf = 1.10 (slip resistance checked at service load) or 1.25 (at ultimate load), F0 = minimum bolt pretension = Anb·f0, f0 = proof stress = 0.70·fub.
- After slipping (bolts designed not to slip only at service load), ultimate capacity reverts to bearing-type design (§10.3).
- **Tension**: Tdf = Tnf/γmf, Tnf = 0.9·fub·An ≤ fyb·Asb·(γmf/γm0) — check both against ultimate and yield.
- **Combined shear+tension** (§10.4.6): **(Vsf/Vdf)² + (Tf/Tdf)² ≤ 1.0** — also quadratic, same form as the bearing-type bolt interaction above (audit correction 2026-09-12: originally logged as linear, source confirms quadratic for both bolt types).
- **Prying force** (§10.4.7, Fig.16 — bolts near a flexible flange/end-plate): **Q = (lv/2le)·[Te − βη·f0·be·t⁴/(27·le·lv²)]**, added to the applied bolt tension when significant. le (distance from bolt line to prying force) = min(end distance, **1.1t·√(β·f0/fy)**). lv = distance from bolt centreline to the weld toe (or half the root radius, rolled section). β = 2 (non-pretensioned bolt) / 1 (pretensioned). η = 1.5. be = effective flange width per bolt pair. t = end-plate thickness. f0 = proof stress. *(Audit correction 2026-09-12: originally flagged as unrecoverable from linear extraction — resolved cleanly from a rendered source-page image.)*

**Table 20 — Typical Coefficient of Friction, μf** [source p.76–77, clean text]: untreated surfaces 0.20 · shot/grit-blasted, no pitting 0.50 · blasted+hot-dip galvanized 0.10 · blasted+zinc spray-metallized (50-70µm) 0.25 · blasted+ethyl zinc silicate coat (30-60µm) 0.30 · sandblasted after light rusting 0.52 · blasted+ethyl zinc silicate (60-80µm) 0.30 · blasted+alkali zinc silicate (60-80µm) 0.30 · blasted+aluminium spray-metallized (>50µm) 0.50 · clean mill scale 0.33 · sandblasted surface 0.48 · red lead painted surface 0.1.

**10.5 Welds and welding**:
- **End returns**: fillet welds return continuously around corners ≥2× weld size (important at the tension end of bending members).
- **Lap joints**: minimum lap ≥4× thinner-part thickness or 40mm, whichever more.
- **Minimum fillet size**: never <3mm; **Table 21** by thicker-part thickness — ≤10mm → 3mm min; 10–20mm → 5mm; 20–32mm → 6mm; 32–50mm → 8mm first run / 10mm minimum total (if the table's minimum exceeds the thinner part's own thickness, use the thinner part's thickness instead, but preheat the thicker part).
- **Effective throat thickness**: ≥3mm, generally ≤0.7t (up to 1.0t in special circumstances), t = thinner joined plate. For fillet welds joining faces inclined to each other (not the normal 90°), throat = K × fillet size — **Table 22**: angle between fusion faces 60–90° → K=0.70; 91–100° → 0.65; 101–106° → 0.60; 107–113° → 0.55; 114–120° → 0.50. Complete-penetration butt weld throat = thinner part's thickness; incomplete-penetration = minimum common weld-metal thickness excluding reinforcement.
- **Effective length**: fillet weld — only the length at full specified size/throat counts; actual drawn length = effective length + 2× weld size, and in any case ≥4× weld size. Butt weld — length of continuous full-size weld, ≥4× weld size.
- **Design strength, fillet welds**: **fwd = fwn/γmw, fwn = fu/√3** — fu = smaller of weld metal / parent metal ultimate stress. γmw = **1.25 shop, 1.5 site** (matches Table 5 — site welding costs a real strength margin, not just QA overhead).
- **Butt welds**: treated as parent metal at throat-thickness section; stresses can't exceed parent-metal-permitted values.
- **Long welded joints** (lj > 150·tt, tt = throat size): reduce by βlw = 1.2 − 0.2·lj/(150tt), capped 0.6–1.0.

**10.6–10.12 (design of connections by construction type, minimum design action, intersections, fastener choice, connection components, bolt/weld group analysis, lug angles)** — not converted given scope; source p.79–86, pull directly for a specific connection design.

## 11. Working Stress Design [p.98–101 / source p.84–87]

The permissible-stress fallback method (§3.1.2.2 — used only where limit state design can't conveniently apply). Structurally, every clause here just takes a Section 6–10 limit-state capacity and multiplies it by a fixed fraction to get an allowable stress; §3–4's general design/analysis rules still apply, using elastic analysis only.

- **Load combination overstress allowance**: permissible stresses may be increased **33%** for combinations involving wind or seismic load (25% for anchor bolts and construction loads) — **except** when wind/seismic is the dominant load in that combination (e.g. paired with dead load alone), where the increase does not apply.
- **Tension**: fat = min[0.6fy (gross yielding), 0.69·Tdn/As (net rupture, plates & angles per §6.3), 0.69·Tdb/As (block shear per §6.4)].
- **Compression**: fac = 0.60·fcd (fcd per §7.1.2.1; angles per §7.5.1.2). Column bases, angle struts, laced/battened columns follow §7.4/7.5/7.6/7.7 with this permissible stress instead of the limit-state one. Simple column base thickness: ts = √[3w(a²−0.3b²)/fbs], w = bearing pressure, a/b = larger/smaller slab projection beyond the column, fbs = 0.75fy.
- **Bending**: laterally supported beams / minor-axis bending — fabc/fabt = 0.66fy (plastic/compact) or 0.60fy (semi-compact). Laterally unsupported, major-axis bending: fabc/fabt = 0.60·Md/Zec or Zet (Md per §8.2.2). Plates/solid rectangles, minor axis: 0.75fy.
- **Shear**: τva = 0.40fy (pure shear) or 0.70·Vn/Av (shear buckling governs, Vn per §8.4.2.2(a)).
- **Combined bending+axial** (member stability + member strength checks) mirrors §9.3.2's interaction form exactly, with allowable stresses (facy, fabcy/fabcz, 0.6fy) substituted for the limit-state design strengths — same Ky/Kz/KLT/Cmy/Cmz/CmLT machinery, same Table 18.
- **Combined bending+axial tension**: (N/0.6fy·Ag actual-stress form) + fbcy/fabty + fbcz/fabtz ≤ 1.0.
- **Combined bearing+bending+shear**: equivalent stress fe = √(fbc² + fbg² − fbc·fbg + 3τ²) ≤ 0.9fy (fbg = actual bearing stress).
- **Connections**: same location/detailing rules as §10, but with permissible stresses at 0.60× the limit-state nominal values throughout — bolt shear fasb = 0.60·Vnsb/Asb, bearing fapb = 0.60·Vnpb/Apb, **tension fatb = 0.60·Tnb/Asb** (Tnb per §10.3.5) *(audit correction 2026-09-12: originally left as a vague cross-reference rather than the actual fraction)*, weld faw = 0.60·fwn (fillet) = **0.4fy** for the simplified case shown, or governed by parent metal for butt welds. Combined bolt shear+tension: (fsb/fasb)² + (ftb/fatb)² ≤ 1.0 (quadratic interaction, confirmed against source).

## 12. Design and Detailing for Earthquake Loads [p.101–108 / source p.87–94]

Ductile detailing for steel frames resisting seismic loads — cross-references [[IS 1893 Part 1 - Earthquake Resistant Design]] for the force calculation itself (this section is purely about steel-specific detailing to achieve the ductility IS 1893 assumes). Frames carrying gravity only (not part of the lateral system) are exempt provided they can accommodate the resulting drift without failing. *(Note: this section's source pages print in an unusual two-column interleaving that scrambled linear-extraction order — verified the actual clause sequence against a rendered page image before writing this up, so the ordering/attribution below is correct even though a raw re-extraction of this section would read jumbled.)*

- **Load combinations** (§12.2): earthquake loads per IS 1893-1 (using §12.3's response reduction factors); load combos per Table 4, **plus two extra combinations required for specific column/connection checks**: (a) 1.2DL + 0.5LL + 2.5EL, (b) 0.9DL ± 2.5EL.
- **Table 23 — Response Reduction Factor (R)** [source ~p.87]: Braced frames — Ordinary Concentrically Braced (OCBF) R=4, Special Concentrically Braced (SCBF) R=4.5, Eccentrically Braced (EBF) R=5. Moment frames — Ordinary Moment Frame (OMF) R=4, Special Moment Frame (SMF) R=5. Higher R (more ductile system) lets you design for lower seismic force — SMF and EBF are the higher-ductility, lower-force options.
- **Connections general**: bolts in seismic frames must be fully-tensioned HSFG or turned-and-fitted (never plain bearing-type snug-tight); welds must be complete-penetration butt welds except column splices; bolts and welds on the same faying surface can't share load.
- **Columns** (§12.5): when Pr/Pd > 0.4, required axial strength (from the extra load combos above) need not exceed 1.2× the connecting beam/brace's nominal strength or the foundation's uplift resistance, whichever governs. **Column splices**: partial-joint-penetration groove welds sized to ≥200% of required strength; flange splice minimum strength 1.2·fy·Af (Af = smaller connected column's flange area).
- **Storey drift**: per IS 1893, including deformation compatibility of gravity-only frames.

**Bracing systems** — OCBF vs SCBF, side by side:

| | OCBF | SCBF |
|---|---|---|
| Ductility demonstration | joint rotation ≥0.02 rad, no strength/stiffness loss below full yield | joint rotation ≥0.04 rad, same criterion |
| Zone/importance restriction | **not permitted** in zones IV/V, or zone III with importance factor >1.0 | permitted in **any** zone, any importance factor |
| Bracing type | diagonal/X only (K-bracing banned outright; V/inverted-V needs specialist literature) | same |
| Bracing steel | any per §2 | **E250B (IS 2062) only** |
| Bracing section class | plastic/compact/semi-compact, not slender | **plastic only** |
| Bracing slenderness | ≤120 | ≤160 (hangers) — general compression-brace limit not fully captured here, verify source p.88–89 before relying on it |
| Compressive strength demand | ≤0.8·Pd | ≤Pd (full design strength) |
| Load sharing | tension braces resist 30–70% of lateral load, either direction | same |
| Governing tension mode | gross yielding must govern, not net rupture | same |
| End connection demand | min of {1.2·fy·Ag, load-combo force, max system-transferable force} | min of {1.1·fy·Ag, max system-transferable force} |
| Connection moment check | 1.2× full plastic moment about buckling axis | same |
| Gusset plates | checked for out-of-plane buckling | same |
| Column splices | not specified here | mid-third of clear height; ≥ nominal shear strength + 50% nominal flexural strength of smaller connected member |

**Eccentrically Braced Frames (EBF)** (§12.9): **IS 800 explicitly defers EBF design to specialist literature** — no formulas of its own beyond the R=5 factor and the general connection/bolt/weld rules above.

**Moment frames — OMF vs SMF**:

| | OMF | SMF |
|---|---|---|
| Ductility | joint rotation ≥0.02 rad below full plastic moment Mp | joint rotation ≥0.04 rad |
| Zone/importance restriction | not permitted zones IV/V or zone III importance>1 (same as OCBF) | any zone, any importance factor |
| Steel | per §2 | **E250B (IS 2062)** |
| Beam/column connections | rigid or semi-rigid | **all connections rigid** |
| Rigid connection moment demand | 1.2× full plastic moment of connected beam, or max deliverable moment, whichever less | 1.2× full plastic moment (reduced beam section: ≥0.8× the unreduced section's full plastic moment) |
| Semi-rigid connection moment demand | 0.5× full plastic moment or max deliverable, whichever less, achieved within 0.01 rad rotation | n/a (rigid only) |
| Connection shear demand | 1.2DL+0.5LL + shear from the design moment above | 1.2DL+0.5LL + shear from 1.2Mp applied at both ends (double curvature) |
| Panel zone | not specified here | strong-axis connections: check web panel zone for shear buckling per §8.4.2; doubler plates/diagonal stiffeners permitted; column web + doubler plate thickness t > (dp+bp)/90 |
| Continuity plates | required, thickness ≥ beam flange thickness, in rigid fully-welded connections | required in all strong-axis welded connections except end-plate connections |
| Beam/column section class | not specified here | **plastic or compact; plastic specifically at potential hinge locations** |
| Strong-column-weak-beam | not specified here | ΣMp(column) / ΣMp(beam) ratio check required at each joint (formula not fully captured — pull source p.94) |

**12.12 Column bases** — not converted (didn't locate the clause body in this pass); pull source p.94+ directly.

## 13. Fatigue [p.109–115 / source p.95–101]

Covers cyclic-load fatigue only — **explicitly excludes** corrosion fatigue, low-cycle/high-stress fatigue, thermal fatigue, stress corrosion cracking, effects above 150°C or below the brittle transition temperature. Design method: each detail (member/connection type) is assigned a **fatigue detail category**, each with its own S-N curve (stress range vs permitted cycles); check at every critical location against the expected cycle count and stress range over the structure's life.

- **Standard S-N curve conditions assumed**: redundant load path (local failure ≠ collapse); nominal stress estimated conventionally (no local stress-concentration factored in); load cycles not highly irregular; details accessible for regular inspection; mildly corrosive environment only (pit depth <1mm), suitably protected; temperature ≤150°C; transverse welds joining plates ≤25mm thick; **no holes permitted in fatigue-loaded members/connections**.
- **Low-fatigue exemption** (§13.2.2.3) — fatigue assessment is **not required** if either: the normal/shear design stress range stays under a threshold tied to the detail's cut-off limit and the safety factors γmft/γmf, **or** the actual number of stress cycles Nsc < 5×10⁶·(threshold ratio)³ (exact threshold expression didn't survive extraction cleanly — verify source p.96 before relying on this exemption for a real check). This is the practically important clause: most ordinary buildings (non-crane, non-machine-support, wind/seismic-dominated cyclic loading only) fall under this exemption and never need a full fatigue check.
- **Hollow-section joint stress multipliers** (Tables 24a/24b, for K/N-type gap and overlap connections in circular/rectangular hollow sections) — chord/vertical/diagonal multiplying factors ranging ~1.0–1.8 depending on joint type and member role; niche enough (tubular truss joints specifically) that it's left reference-by-page rather than reproduced here.
- Design stress spectrum for non-uniform cycling: rainflow counting or equivalent rational method.
- Detail categories and their S-N curves (Table 26, extensive) — not converted; this is a specialist lookup (which weld/bolt/connection detail maps to which fatigue class) best pulled directly for an actual fatigue-sensitive design (crane runway, machine support, offshore/wind-turbine-adjacent structure).

## 14. Design Assisted by Testing [p.121–127 / source p.107–113]

Purely procedural — no formulas. Testing is **not required** for standard-code designs; it's used instead of or alongside calculation when: available calculation methods don't cover the case, calculation would be uneconomically conservative, the design/construction departs from this standard, production consistency needs confirming, or an existing structure's actual capacity is in question. Covers test types, test conditions/loading, and acceptance criteria at a procedural level. Not converted further given this is a "when to test, follow a lab protocol" section rather than a design-formula one.

## 15. Durability [p.128–133 / source p.114–119]

- **General principle**: durability = no cross-section/strength loss from corrosion over the service life, addressed via material choice, detailing, fabrication, erection, and surface protection together — not by surface coating alone.
- **Detailing for drainage**: avoid standing water, moisture traps, prolonged water rundown; exposed surfaces must stay inspectable/maintainable, and surfaces that can't be made accessible must be fully sealed instead.
- **Table 28 — Environmental Exposure Classification** [source ~p.115]: five severity levels — **Mild** (protected interior surfaces, except coastal); **Moderate** (condensation/rain exposure, underwater, non-aggressive soil/groundwater contact, or sheltered coastal); **Severe** (frequent rain, wet/dry cycling, severe condensation, full seawater immersion, or exposed coastal salt air); **Very Severe** (sea spray, corrosive fumes, aggressive sub-soil/groundwater); **Extreme** (tidal/splash zones, aggressive liquid/solid chemicals).
- **Table 29 (a)** cross-references atmospheric condition (normal/polluted inland, normal/polluted coastal) against coating system to give an expected recoating interval, roughly 8–20+ years depending on system and exposure severity.
- **Tables 29(b)(i)/(ii)** — detailed shop- and site-applied coating system specifications (surface prep, primer, intermediate/top coats, film thicknesses) by protection-system number — a paint-spec lookup, not reproduced here; pull source p.118–119 for an actual coating specification.
- Abrasion resistance (machinery/conveyor contact) and special corrosion-resistant alloy steels are deferred to specialist literature.

## 16. Fire Resistance [p.133–138 / source p.119–124]

- **Two compliance routes**: protected members — protection thickness must achieve a Period of Structural Adequacy (PSA) ≥ the required Fire Resistance Level (FRL); unprotected members — exposed-surface-area-to-mass ratio must be low enough to achieve that same PSA.
- **FRL source**: IS 1641/1642/1643, building specs, or local ordinance — driven by occupancy purpose and evacuation time, expressed as minutes of standard fire exposure without collapse.
- **PSA calculation** = (a) strength-vs-temperature relationship → limiting temperature, (b) thermal response (temperature-vs-time under fire exposure), (c) time at which the element reaches its limiting temperature.
- **Limiting steel temperature, T1** (ordinary steels), °C: **T1 = 905 − 690·rf** *(audit correction 2026-09-12: originally logged with a division, "905 − 690/rf" — confirmed from a rendered source image that it's multiplication, 690·rf; this matters, the two formulas behave completely differently)*. rf = ratio of design action on the member under fire to the room-temperature design capacity, Rd = Ru/γm. Higher utilization → lower limiting temperature → less fire endurance, matching physical intuition.
- Design fire action must account for reduced bond strength and restraint-to-thermal-expansion effects.
- Special (non-ordinary) steels: limiting temperature per specialist literature (thermal characteristics from the steel supplier).
- **§16.6 Time to reach T1 (protected members)**: by calculation from fire-test data via regression, **t = k0 + k1·hi + k2·(hi/ksm) + k3·T + k4·hi·T + k5·(hi·T/ksm) + k6·(T/ksm)** — t = time from test start (min), hi = fire protection thickness (mm), T = steel temperature from test (>250°C), ksm = exposed-surface-area-to-mass ratio (10³ mm²/kg). **Table 30** gives default regression coefficients when using generic test data rather than project-specific tests: k0=−25.90, k1=1.698, k2=−13.71, k3=0.0300, k4=0.0005, k5=0.5144, k6=6.633 — valid only under specific test conditions (§16.6.2.3: board/sprayed insulation <1000 kg/m³ density, ≥9 tests, same protection system and fire-exposure condition throughout).
- Figure 22 (not reproduced) plots yield-stress ratio and elastic-modulus ratio vs temperature 0–1200°C — both roughly flat to ~400°C then fall off sharply, standard structural-steel fire behaviour.

## 17. Fabrication and Erection [p.139–152 / source p.125–138]

Workmanship/QA section — fabrication procedures, assembly, riveting, bolting, welding execution, machining of butts/caps/bases, painting (before and after erection), marking, shop erection, packing, inspection & testing, site erection, and (per Amendment 1's added §17.15) bedding requirements, plus §17.16 steelwork tenders and contracts. Entirely procedural/QA content, no design formulas — not converted; pull source p.125–138 directly for a fabrication-shop specification or QA checklist.

## Annexes A–H [p.153–166 / source p.117–138]

- **Annex A — List of Referred Indian Standards** [source p.117]: bibliography of every IS standard cross-referenced in the code (IS 875, IS 1893, IS 1367, IS 2062, IS 816, IS 9595, IS 1641/1642/1643, IS 1608, IS 2190, IS 801, IS 4326, and many more) — reference-only, not reproduced; pull if a specific referenced-standard number is needed.
- **Annex B — Advanced Structural Analysis and Design Methods** [source p.117–119]: covers second-order elastic analysis/design (P-Δ and member P-δ effects) and frame instability analysis as alternatives to the effective-length method of Sections 7/9 — specialist/software-driven territory, procedural guidance rather than hand-formulas; not converted.
- **Annex C — Design Against Floor Vibration** [source p.120] *(audit 2026-09-12: this does have its own usable formulas, not just a specialist-literature pointer as first logged)*: combined floor frequency when a joist system sits on a flexible supporting beam of frequency f2 — **1/fr² = 1/f1² + 1/f2²** (f1 = joist system's own natural frequency). **Damping** (% critical, approximate): fully composite construction 2%, bare steel beam + concrete deck 3–4%, floor with finishes/false ceiling/fireproofing/ducts/furniture 6%, partitions not aligned with supports (or spaced >6m, orthogonal) up to 12%. **Peak acceleration** (heel-impact, spans >7m, f1<10Hz): **a0/g = 600·fr/W**, W = total weight of floor+contents over the span and equivalent floor width b (N), b = 40ts (or 20ts if overhang is one-sided only), ts = equivalent slab thickness (concrete in slab+ribs, averaged). Annoyance criteria (C-2) and floor frequency (C-3) themselves still reference specialist literature/other clauses rather than a standalone IS 800 formula.
- **Annex D — Effective Length of Columns in Frames** [source p.121–124] *(audit 2026-09-12: the K-factor formulas do survive cleanly — corrected below; the earlier "use the charts instead" guidance undersold what's actually recoverable)*: an **alternative, more refined method than Table 11** for multi-storey rigid frames. β1, β2 = stiffness ratio at each column end, β = ΣKc/(ΣKc+ΣKb) (Kc/Kb = effective flexural stiffness of columns/beams meeting at that joint, each = C·(I/L) — C from **Table 35** by far-end condition (pinned/rigid/fixed) × braced-vs-unbraced frame, itself a function of Pcr/P). Given β1, β2:
  - **Non-sway (braced) frames**: K = [1 + 0.145(β1+β2) − 0.265β1β2] / [2 − 0.364(β1+β2) − 0.247β1β2]
  - **Sway (moment-resisting) frames**: K = {[1 − 0.2(β1+β2) − 0.12β1β2] / [1 − 0.8(β1+β2) + 0.6β1β2]}^0.5
  
  Fig. 27 (non-sway) / Fig. 28 (sway) are the alignment-chart graphical version of these same two formulas — either the formula or the chart gives the same K. D-2/D-3 extend this to single- and double-stepped columns (common in industrial buildings with crane brackets) via **Tables 36/37** (not reproduced) using the same β-ratio logic per column segment.
- **Annex E — Elastic Lateral Torsional Buckling** [source p.128–130]: the exact Mcr method for sections not covered by §8.2.2.1's simplified doubly-symmetric-I formula (non-symmetric sections, non-simply-supported cases). **Table 42** tabulates K-constants (C1/C2/C3 by loading and support condition — point load, UDL, end moments, cantilevers) for a more general Mcr formula; given this table's numeric density and the session's standing multi-column-table caution, it's left reference-by-page rather than transcribed. Amendment 1 corrects two of Table 42's cells (col 5 row 7: 1.267 not 1.257; col 6 rows 5/10: 1.730 not 1.780, and 1.890 not 1.390) and two formula terms in E-1.2 ((LLT)² not (LLT); (z²+y²)² not (z²−y²)).
- **Annex F — Connections** [source p.130–134] — practical connection-design guidance, genuinely useful for real detailing:
  - **Beam splices**: away from max-moment points, flange splice carries all moment, web splice carries shear (deep girders: split proportionally by stress distribution, web splice still checked for its share of moment+shear plus any bolt-group eccentricity moment). Splice plate area ≥105% of the spliced flange element's area, centroid aligned with the spliced element. Fasteners sized for the spliced element's load +5%, but never less than 50% of the spliced material's effective strength. Welded flange splices: complete-penetration butt welds developing full plate strength; gradual transition where flange width/thickness changes at the splice. Splices at a continuous beam's inflection point can relax the flange-splicing requirement.
  - **Column splices**: bearing-faced ends must still be spliced to hold alignment (machined for perfect contact); non-bearing-faced ends need splices sized to transmit the full force at that location. Splice centroidal axis should align with the member's centroidal axis to avoid eccentricity (design for it explicitly when unavoidable). **HSFG bolts only** when the column flange sees significant tension, faces aren't prepared for bearing, or full slip-free continuity is required.
  - **Beam-to-column connections**: **simple connections** (shear-only, nominal eccentricity) — typical in frames up to ~5 storeys where a separate bracing/shear-wall system carries lateral loads; **rigid connections** — needed in high-rise/slender structures where stiffness governs, transfer significant moment to columns.
- **Annex G — General Recommendations for Steelwork Tenders and Contracts** [source p.135–137]: procedural — information exchange between designer/tenderer, detailing responsibilities, time schedules, site procedure, inspection, maintenance. Not converted; pull if drafting an actual tender/contract scope.
- **Annex H — Plastic Properties of Beams** [source p.138]: reference tables of plastic section modulus (Zp) for standard rolled sections — a straight lookup table, not converted; use a steel section handbook (SP 6) or the actual rolled-section tables for a specific section's Zp rather than this note.
