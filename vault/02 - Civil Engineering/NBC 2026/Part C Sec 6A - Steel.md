---
status: active
project: civil-engineering
type: reference
---
# Part C, Section 6A — Steel

Structural design of steel buildings (hot-rolled sections, steel tubes) using limit state and plastic design methods — materials, general design requirements, member design (tension/compression/bending/combined forces), connections, seismic detailing, fatigue, fire resistance, fabrication and erection. Aligned with the (under-publication) IS 800:2026. Source: PDF pages 853–1070.

This section only gives general guidance on loads — actual load values/combinations are in [[Part C Sec 1 - Loads and Load Effects]] (cited throughout as "Part C/Section 1").

## 1–8: Scope, terminology, symbols, units, member axes (p. 857–865)
- Scope (Cl 1): hot-rolled sections + steel tubes, riveted/bolted/welded; limit state + plastic theory. Cold-formed light-gauge steel is covered elsewhere (not this section).
- Cl 3: Extensive terminology (p. 857–863) — buckling, ductility, fire-exposure conditions (three-sided vs four-sided, Cl 3.49), slenderness, limit states, etc.
- Cl 8 / Fig. 1 (p. 864): standard member axis convention (x-x along member, y-y, z-z, u-u, v-v).

## 9: Materials (p. 865–875)
- Physical properties (Cl 9.2.4.1, any grade): unit mass 7850 kg/m³; E = 2.0×10⁵ MPa; Poisson's ratio 0.3; shear modulus G = 0.769×10⁵ MPa; coefficient of thermal expansion 12×10⁻⁶/°C.
- **Table 1 (p. 867–874, 8 pages)** — Tensile properties (yield stress, ultimate tensile stress, elongation) for every accepted steel standard/grade used in Indian construction (structural mild steel grades E250–E450, weathering steels, fastener-grade steels, tube steels, etc.). Too large to reproduce here — open PDF p. 867 for the full grade table when selecting a specific steel grade.
- Rivets, bolts/nuts/washers, castings, welding consumables (Cl 9.3–9.6): each must conform to specific accepted IS standards referenced as [C-6A(n)] — see the standards list at the end of the section (not separately extracted here; look up the [C-6A(n)] reference number against the section's own reference list on the PDF's closing pages of this section if a specific IS number is needed).

## 10: General Design Requirements (p. 875–885)
- Cl 10.1: Design objective = acceptable probability of satisfactory performance over design life; limit state method is the default design basis.
- Cl 10.2: Loads to account for — dead, imposed (incl. crane/snow/dust/wave/earth pressure), wind, earthquake, fire, erection, accidental (blast/impact), secondary (thermal/settlement/eccentricity) — values from Part C/Section 1.
- Cl 10.3 Fire loads: imposed load during fire = 100% of characteristic value for storage areas, else 50%; no extra partial safety factors during fire (it's an extreme event).
- Cl 10.6 Load combinations: per Part C/Section 1; wind and earthquake are NOT combined simultaneously (Cl 10.6.2).
- Cl 10.8 Classification of cross-sections — **Class 1 Plastic / Class 2 Compact / Class 3 Semi-compact / Class 4 Slender**, governed by width-to-thickness ratio limits in **Table 2 (p. 879–880)**. Section classified by its most critical (least favourable) element.
- **Table 3 (p. 883)** — Max effective slenderness ratio KL/r: 180 (compression members under dead+imposed load), 180 (tension members w/ stress reversal, non-wind/seismic), 250 (compression under wind/EQ only), 300 (compression flange of beam vs lateral-torsional buckling), 350 (roof truss tie under wind/EQ reversal), 400 (members always in tension).
- Cl 10.11 Expansion joints (low-rise, ≤3 storeys): with one bay of central bracing, max building length 180 m (covered) / 120 m (open gantry); with multiple bracing bays, max length 230 m (covered) / 150 m (open gantry); max building width 150 m before an expansion joint is needed (Figs. 3–4, p. 885).

## 11: Methods of Structural Analysis (p. 885–892)
- Elastic, plastic (Annex B for advanced analysis), or dynamic analysis (per Part C/Section 1 for earthquake). Earthquake effects (Section 18) must be analyzed elastically — plastic analysis is NOT permitted for design earthquake shaking.
- Non-sway vs sway frame classification (Cl 11.1.2) based on storey deflection limits (hs/2000 clad, hs/4000 unclad, under notional horizontal load).
- Cl 11.3.6 Notional horizontal loads: 0.5% of factored (dead + vertical imposed) load at each floor/roof level, applied for sway-stability checks only — not combined with wind/EQ/temperature, not used for overturning checks.
- Cl 11.7 Second-order effects: may be neglected if λcr/λp ≥ 10 (clad) or ≥20 (unclad); amplification factor method for intermediate ratios; full second-order analysis required below λcr/λp = 4.6 (clad)/5.75 (unclad).

## 12: Limit State Design (p. 892–900)
- Two limit-state categories: strength (equilibrium/stability/rupture/fatigue/brittle fracture) and serviceability (deflection/vibration/fatigue cracking/durability/fire).
- **Progressive/disproportionate collapse avoidance (Cl 12.1.3)**: buildings must be tied together at each floor level with ties capable of resisting the larger of the tributary factored dead+imposed load or 75 kN; edge-column tie connections must resist ≥1% of the column's max axial compression; disproportionate collapse = >15% of a floor/roof area (of ≥70 m²) collapsing at one level plus an adjoining level.
- **Table 4 (p. 895) — Partial safety factors for loads (γf)** by combination (DL+IL+CL, +WL, +EL, +FL for fire, +AL for accidental) and limit state (strength vs serviceability). Key values: 1.5 (DL+IL, strength), 1.2 (combos with WL/EL), 1.0 (fire combos, no extra factor), all serviceability = 1.0 or 0.8.
- **Table 5 (p. 897) — Partial safety factors for materials (γm)**: yielding/buckling γm0 = 1.10; ultimate stress γm1 = 1.25; connections (bolts/rivets/welds) γm = 1.25 shop / 1.25–1.50 field.
- **Table 6 (p. 899) — Deflection limits**, e.g.: purlins/girts span/150–300 depending on cladding; floor/roof beams span/300 (elements not susceptible to cracking) or span/360 (susceptible); cantilevers span/150–180; crane gantry wheel deflection span/500–1000 depending on crane duty; lateral building drift under wind height/300–500; inter-storey drift under wind = storey height/300.

## 13: Design of Tension Members (p. 900–903)
- Design strength = lowest of: yielding of gross section (Tdg = Ag·fy/γm0), rupture of net section (Tdn = 0.9·An·fu/γm1, with shear-lag reduction for single angles), and block shear (Tdb).
- Fig. 5 (p. 901) — staggered bolt-hole net-area geometry; Fig. 6 — single-leg angle connections; Fig. 7 (p. 903) — block shear failure mode.

## 14: Design of Compression Members (p. 903–911)
- Design strength Pd = Ae·fcd, where fcd = χ·fy/γm0 and χ is the stress-reduction factor (function of buckling class, non-dimensional slenderness λ, and imperfection factor α).
- **Table 7 (p. 907) — Imperfection factor α** by buckling class: a0=0.13, a=0.21, b=0.34, c=0.49, d=0.76.
- **Table 8 (p. 907 onward, multi-page) and Table 9** — full lookup tables of χ / fcd vs KL/r and yield stress, for each buckling class — use directly from PDF for design (too large/precision-sensitive to safely reproduce here).
- **Table 10 (p. 3070/see slice)** — classifies standard cross-sections (I, channel, angle, tube, etc.) into buckling classes a0–d.
- **Table 11 — Effective length of prismatic compression members** by end-restraint condition (pinned/fixed/free combinations) — standard K-factor table, open PDF p.~925 for the full boundary-condition matrix.
- Cl 14.2.4 Truss members: effective length = 0.7–1.0× distance between connection centres depending on end restraint.
- Cl 14.3.3 Eccentricity for stanchions/columns: beam reactions assumed applied at 100 mm eccentricity from face of section (or centre of bearing, whichever is greater), except cap connections (at face) and simple roof-truss bearings (no eccentricity).
- Column bases (14.4), angle struts (14.5), laced columns (14.6, Fig. 10), battened columns (14.7, Fig. 11), back-to-back compound members (14.8) each have their own detailed geometric/design rules — see PDF p. 3182–3527 range (within this slice) for full clause text if designing one of these member types.

## 15: Design of Members Subjected to Bending (p. 911–924, within slice ~lines 3528–4753)
Covers: general flexural design, lateral-torsional buckling / effective length for LTB (Table 13 imperfection parameter αLT, Table 14 moment-gradient factor, Tables 15–16 effective length for simply-supported beams and cantilevers), shear design of webs, stiffened web panels including tension-field action (Figs. 12–14), plate girder/stiffener design (Fig. 15, Table 17), box girders, and bending in a non-principal plane. This is a design-calculation-heavy clause set with many interacting tables — for an actual beam/plate-girder design, work directly from PDF p.~925–975 rather than a condensed note.

## 16: Members Subjected to Combined Forces (p. ~975–980)
Combined shear+bending and combined axial+bending moment interaction checks (Table 18 interaction factors, Table 19 equivalent uniform moment factor).

## 17: Connections (p. 980–1000+)
- General principle: connections must be consistent with the analysis assumptions (rigid/semi-rigid/simple) and able to transmit the calculated design actions; mixing fastener types to carry the same force is generally disallowed except fully-tensioned HSFG bolts may share load with welds if pretensioned after welding.
- **Table 20 (p. ~1000) — Standard clearance/oversize/slotted hole sizes** by bolt diameter (e.g. M12–M14: 1.0 mm standard clearance; M16–M22: 2.0 mm; M24: 2.0 mm standard/6.0 oversize; >M24: 3.0 mm standard/8.0 oversize).
- Minimum fastener spacing: ≥2.5× nominal bolt diameter.
- Maximum spacing: lesser of 32t or 300 mm generally; lesser of 16t or 200 mm (tension members)/12t or 200 mm (compression members) along the line of stress; increasable 50% if staggered with gauge ≤75 mm.
- Edge/end distance minimums: 1.7× hole diameter (sheared/flame-cut edges), 1.5× hole diameter (rolled/machined/sawn edges). Max edge distance: 12tε generally, or 40 mm + 4t for corrosive exposure.
- Countersunk bolts: tensile strength reduced by 33.3%; no reduction for shear.
- **Table 21 — Coefficient of friction (µf) values** for friction-grip (HSFG) connections by surface treatment.
- **Tables 22–23 — Minimum fillet weld sizes** and weld strength factor K by angle between fusion faces.
- Figs. 16–21 (p. ~1000–1020): prying force, fillet weld geometry, partial-penetration groove welds, continuity plates.

## 18: Design and Detailing for Earthquake Effects (p. 973–980)
Steel seismic-resisting frames are classified **ordinary** (lower ductility) or **special** (higher ductility). **Seismic zones III and above require special frames only**; zone II permits ordinary moment frames (OMF) or ordinary concentrically braced frames (OCBF).

- Response reduction factors (R): OEBF = 4.5; OMF = 4.0; non-ductile frames (NDF) = 1.5 (permitted for single-storey industrial buildings with height:width ≤1.0, which are then exempt from the ductility-detailing clauses 18.4–18.12). SCBF/SEBF/SMF factors are given in Part C/Section 1.
- Extra load combinations for critical members (Cl 18.2.3): **1.2DL + 0.5IL ± 2.5E**, and **0.9DL ± 2.5E**.
- All bolts in critical (plastic hinge) zones must be fully-tensioned HSFG or turned-and-fitted bolts; welds in critical zones must be complete-penetration butt welds (except column splices).
- **OCBF**: not permitted in zone IV+ or in zone III with importance factor >1.0; K-bracing never permitted for seismic resistance; bracing slenderness ≤120; tension braces must carry 30–70% of lateral load in either direction.
- **SCBF**: permitted in any zone; bracing steel restricted to grade E250B; bracing cross-section must be Class 1 Plastic; bracing slenderness ≤160 (hangers only).
- **OMF/SMF**: beam-column connections must be rigid (SMF) or rigid/semi-rigid (OMF) and sized to withstand 1.2× the connected beam's full plastic moment (rigid) or 0.5× (semi-rigid, OMF only); strong-column/weak-beam ratio required at joints (ΣMPc/ΣMPb ≥ 1.2, Cl 18.11.3.2); panel-zone web/doubler-plate thickness ≥ (dP+bP)/90.
- Column bases: fixed bases + anchor bolts designed for 1.2× column's full plastic moment capacity.

## 19: Fatigue (p. ~980–1003)
Applies to structures under significant cyclic loading (excludes corrosion fatigue, low-cycle fatigue, thermal fatigue, stress-corrosion cracking, and temperature extremes >150°C or below brittle-transition). Detail categories and S-N curves (Figs. 22–23) define allowable stress range vs number of cycles; **Table 25 partial safety factors for fatigue strength**; Table 27 (variability of structural units).

## 20: Design Assisted by Testing (p. ~1003)
Covers when/how physical testing (proof testing, prototype testing) may substitute for or supplement calculation.

## 21: Durability (p. 1003–1004)
Factors: environment, exposure degree, member shape/detailing, protective measures, maintenance ease. **Table 28 — Environmental exposure conditions**; Table 29 — protection guidance by desired service life.

## 22: Fire Resistance (p. 1004–1008)
- Protected members: fire-protection thickness must give a Period of Structural Adequacy (PSA) ≥ the required Fire Resistance Level (FRL). Unprotected members: exposed-surface-area-to-mass ratio (ksm) must be ≤ the value giving PSA = required FRL.
- **Required FRL comes from [[Part F - Fire and Life Safety]]** (or city ordinance/client spec) based on building use and evacuation time.
- Yield stress and modulus of elasticity both degrade with temperature (Fig. 24, formulas in Cl 22.4) — **no yield-stress reduction below 215°C**.
- PSA determination: by calculation (limiting temperature method, Cl 22.5–22.7), by direct single fire test (Cl 22.6.3/22.8), or by validated rational analysis.
- **Table 30 (p. 1006) — regression coefficients** for temperature-vs-time curves from protected-member fire test series.
- Three-sided vs four-sided fire exposure distinguished throughout (member built into/against a wall or slab vs fully exposed) — three-sided members average temperature differently and must be grouped by concrete density (±25%) and effective thickness (±25%) tolerances (Cl 22.9).
- **Tables 31–32 — example FRL tables for a specific encased steel column (203×203mm) and encased steel beam (406×176mm)**, protection thickness vs required fire rating — illustrative worked examples, not general design tables; verify applicability to your actual member size before use.
- Connections must be protected to at least the maximum protection thickness required by any member framing into them (Cl 22.10.1), covering bolt heads, welds, and splice plates too.

## 23: Sustainable Steel Construction (p. ~1023–1028, new in this revision)
Material efficiency, design for deconstruction/reuse, responsible sourcing, embodied carbon (EPD) — a qualitative/process clause set, not numeric design requirements.

## 24: Fabrication and Erection (p. 1028–1040)
Fabrication procedures, assembly, riveting, bolting, welding, machining of butts/caps/bases, painting (before and after erection), marking, shop erection, packing, inspection/testing, site erection, bedding, and contract/tender requirements for steelwork. Largely procedural/quality-control clauses.

## Annexes (referenced, not separately extracted)
Annex A (symbols), Annex B (advanced/second-order analysis), Annex C (floor vibration), Annex D (effective length — stepped columns, D-1/D-2), Annex E (torsional-flexural buckling), Annex F (semi-rigid connection design), Annex G (corrugated web girder design, new in this revision) — go to the relevant annex on the PDF directly when a clause above cross-refers to it; not transcribed here as they're calculation procedures meant to be used interactively, not summarized.

## Tables requiring PDF verification (large/dense, cross-check before using numbers for real design)
Table 1 (steel grades, p.867–874), Table 8/9 (compression buckling curves, p.907+), Table 10 (buckling class by section, ~p.3070 in slice line-numbering), Tables 11–19 (effective length / LTB / interaction factors, spread through bending & compression clauses), Tables 31–32 (fire protection worked examples, p.~1006–1008). These are large numeric lookup tables where OCR/text-extraction column order is not fully trustworthy — **always read the actual PDF page before using a specific number from these tables in a real calculation.**

## Cross-references
- Loads, load combinations, wind/seismic zone factors, crane load effects, response reduction factors for SCBF/SEBF/SMF: → [[Part C Sec 1 - Loads and Load Effects]] (cited constantly as "Part C/Section 1", e.g. p.875, 885, 895, 974).
- Fire Resistance Level requirements by building use: → [[Part F - Fire and Life Safety]] (p.1005).
- Cold-formed light-gauge steel members: covered in a separate standard (IS 801), not this section (p.853).
- Steel tubes in general building construction: IS 806-based provisions (p.853), used until IS 806 itself moves to limit-state format.
