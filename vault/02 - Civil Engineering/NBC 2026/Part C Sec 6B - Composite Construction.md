---
status: active
project: civil-engineering
type: reference
---
# Part C, Section 6B — Composite Construction in Structural Steel and Concrete

Design and construction of composite structures (structural steel + cast-in-situ/precast concrete acting integrally): composite beams, composite slabs with profiled steel decking, and composite columns. New in the 2026 edition — split out of the old combined "Section 6 Steel" chapter; based largely on IS 11384:2022, consistent with IS 456:2000 (concrete) and Part C/Sec 6A (steel). Limit-state design philosophy throughout. (Foreword, pp. 1071–1074)

## 1–4 Scope, terminology, symbols (pp. 1075–1077)
Applies to design/construction of composite steel-concrete beams, slabs and columns designed by limit-state method for simply supported and continuous systems. Key terms (cl. 3): composite action, shear connectors (flexible — studs/channels — vs rigid), m-k factors for slab decking interlock, design/factored load, differential shrinkage, fatigue limit state. Full symbol list in Annex A (pp. 1132–1136).

## 5 Materials and workmanship (pp. 1077–1080)
- **Structural steel**: unit mass 7850 kg/m³, E = 2.0×10⁵ MPa, shear modulus 0.769×10⁵ MPa, Poisson's ratio 0.30, thermal expansion 0.000012/°C (cl. 5.2.1, p. 1077).
- **Concrete**: min grade M20; design provisions valid M20–M75 (M20–M60 for lightweight concrete). Concrete strength classes: Ordinary (≤M20), Standard (M25–M55), High Strength (M60–M80, requires specialist literature) (cl. 5.3.2, p. 1078).
- **Table 1** (p. 1079) — density classes/design densities for lightweight concrete (ρ 1.0–2.0, plain vs reinforced density values 1050–2150 kg/m³).
- **Table 2/3** (p. 1079–1080) — reinforcement grades (MS Grade I, Fe415/500/550/600 series) with minimum yield stress, tensile strength, elongation. **Verify against PDF p.1080** — the strength values table has many columns and is worth double-checking visually before use in design.
- Seismic Zones III/IV/V: HYSD bars need min. 14.5% elongation; structural steel max yield strength shall not exceed specified minimum by more than 20% (Notes, p. 1080).

## 6 Structural analysis (pp. 1081–1087)
Covers section classification (plastic/compact/semi-compact/slender) for steel elements in composite action (cl. 6.1.1–6.1.2, incl. **Table 4** encased-I-section classification limits, p. 1083), joint modelling (hinged/rigid/semi-rigid, cl. 6.1.3), foundation support, first-order vs second-order analysis and when each applies (cl. 6.1.5, ratio Pcr/Pd ≥ 10 → first order OK), imperfections, shear lag/effective width, creep/shrinkage/temperature, cracking, sequence of construction. Global analysis methods: linear elastic (cl. 6.2.1, incl. overturning safety factors 1.2×DL+1.4×LL restoring vs overturning, sliding factor ≥1.4), **Table 5** limits on hogging moment redistribution (p. 1086, 10–40% depending on section class), non-linear (6.2.2), rigid-plastic (6.2.3, with detailed applicability conditions incl. span-length symmetry ≤50% difference, end span ≤115% of adjacent).

## 7 Limit state design — general philosophy (pp. 1087–1091)
Design Action ≤ Design Strength. Three limit-state categories: Ultimate, Serviceability, Fatigue (cl. 7.2). Ultimate limit states specific to composite: flexural/shear/bearing collapse, horizontal shear failure at steel-concrete interface, vertical separation of slab from beam, column shear/buckling failure. **Table 6** (p. 1090) — partial safety factors γf for load combinations (DL+LL+CL = 1.5/1.5; DL+LL+CL+WL/EL = 1.2 across the board; DL+WL/EL = 1.5(0.9); DL+ER = 1.2(0.9); DL+LL+AL = 1.0/0.35). **Table 7** (p. 1091) — partial safety factors γm for materials: structural steel yield 1.10, ultimate 1.25; reinforcement 1.15; shear connectors 1.25; bolts (friction/bearing/rivets/welds-shop) 1.25, welds-site 1.50; concrete 1.50. Accidental load combos: material γm = 1.0.

## 8 Design for ultimate limit states — composite beams (pp. 1091–1101)
Checks required: flexure, lateral-torsional buckling, web shear buckling, longitudinal shear. Key assumptions (8.1.1): max concrete compressive strain 0.0035, concrete tension ignored. Bending resistance equations for sagging/hogging moments given in Annex B depending on where the plastic neutral axis falls (slab / steel flange / steel web) — see Tables 16–19 there.
- Precast slab provisions (8.2): full-depth precast panels min. 150 mm thick, partial-depth min. 75 mm thick; bearing/joint/shear-connector detailing rules.
- Effective width of concrete slab (8.3.3, p. 1096): beff formula based on span length Le/4 or Le/8 per side, capped by actual geometric width.
- **Table 8** (p. 1098) — max depth of steel beams (unencased/encased) by steel grade (250–>400 MPa): ranges from 1000 mm (encased, 250 MPa I-section) down to 270/430 mm (>400 MPa parallel-flange).
- Shear design (8.3.6): plastic shear resistance vs shear buckling resistance; reduced bending resistance when V > 0.6Vd (formulas p. 1100–1101).

## 9 Serviceability limit states (pp. 1101–1103)
Un-propped vs propped vs non-composite construction stress/strain behaviour. Modular ratio m = Es/Ecm ≥ 7.5 (short-term) or Es/(Kc·Ecm) ≥ 15.0 (long-term, creep factor Kc=0.5). Limiting stresses: concrete ≤ ⅓ fck, reinforcement ≤ fyk/γk, steel ≤ fy/γm0. Deflection limits per good practice reference (no NBCS-specific numeric override given). Camber guidance: for spans >25 m, camber ≈ DL deflection + half LL deflection. Durability: zinc coating 275 g/m² for profiled sheeting in non-aggressive internal environments. Fire resistance addressed separately in cl. 15. Crack width control per IS 456 reference.

## 10 Fatigue limit state (p. 1103)
Excludes corrosion fatigue, low-cycle fatigue, thermal fatigue, stress-corrosion cracking, and temperature extremes (>150°C or below transition temp) from this section's scope — refer to Part C/Sec 6A for those.

## 11 Shear connectors (pp. 1103–1114) — key design section
- Stud connector design resistance Qd formula and channel connector formula given (p. 1105).
- **Table 9** (p. 1106) — ultimate static strength of shear connectors (studs 12–25mm dia, channels ISMC75/100/125) at fck 25/30/40/50 MPa — e.g. 25mm stud, 100mm height: 112–156 kN depending on concrete grade. **Verify against PDF p.1106** for exact cell alignment.
- Reduction factors kp/kt for studs used with profiled decking, ribs parallel or transverse to beam (11.2.3, pp. 1107–1108). **Table 10** (p. 1108) — upper limits kt,max by studs-per-rib and sheet thickness.
- **Table 11** (p. 1108) — fatigue strength Qr (kN) for headed studs φ16–25mm and channels, across 0.1–100 million cycles.
- Spacing formulas (11.3.1) for longitudinal shear (SL1, SL2) and fatigue (SR) — lowest of the three governs actual spacing.
- Partial shear connection (11.4): degree of connection Sc formulas, ductility limits by steel section flange ratio.
- Detailing: min 40mm cover above haunch reinforcement/stud top, clear cover to connectors ≥25mm vertical/50mm horizontal (11.6.2, p. 1111, Fig. 12); max spacing = lesser of 600mm / 3×slab thickness / 4×connector height; min stud spacing 75mm (11.6.3).
- Transverse reinforcement / transverse shear check (11.7–11.8, pp. 1112–1114): min transverse steel = 2.5Q/fyk (cm²/m).

## 12 Composite slabs with profiled steel sheeting (pp. 1114–1119)
- Prequalification (12.2.1): composite slab min overall depth 90mm (concrete above ribs ≥50mm); non-composite/non-stabilizing slab min 80mm (concrete above ribs ≥40mm).
- Min bearing lengths (12.2.2, Fig. 16): decking-on-steel/concrete Lbc=75mm/Lbs=50mm; on other materials Lbc=100mm/Lbs=70mm.
- Shrinkage strain default 0.0003 in absence of test data (12.2.3).
- Analysis methods for sheeting-as-shuttering and composite-slab stage (12.3): elastic, rigid-plastic (span ≤3.0m for no rotation-capacity check), elastic-plastic.
- Effective span (12.4.1): internal span 0.8L, external span 0.9L for continuous slabs treated as equivalent simply-supported.
- Construction-stage deflection limit for sheeting: L/180 (12.4.2).
- Punching shear (12.5.1, Fig. 17) and vertical shear (12.5.2) per IS 456, sheeting counted as tensile reinforcement if fully anchored.
- Crack width ≤0.3mm (12.6.1); 0.4% top steel (propped) / 0.2% (un-propped) normally avoids cracking. Deflection limit span/350 or 20mm (whichever less) per IS 456 — noted as potentially unrealistic for un-propped construction; span/depth 25–35 recommended instead.
- Fire resistance basis: thermal insulation + integrity criteria via adequate insulation thickness below decking (12.6.3).

## 13 Composite columns (pp. 1119–1131)
- Types: fully/partially concrete-encased steel sections, or concrete in-filled rectangular/circular hollow steel sections. Steel contribution ratio δ must be 0.2 ≤ δ ≤ 0.9 (13.1.1).
- Cover to encased steel: ≥40mm or ≥1/6 of flange breadth (13.2).
- Short column criteria: non-dim. slenderness λ ≤ 0.2, OR design load P < 0.1×Pcr (13.5.1).
- Local buckling limits (13.4.1): d/t ≤ 88ε² (circular filled tubes), h/t ≤ 50ε (rectangular filled tubes), bf/tf ≤ 43ε (partially encased I) — ε = √(250/fy).
- **Table 12** (p. 1123) — limiting λ for long-term loading effects to be ignored: encased 0.8 (braced)/0.5 (unbraced); filled sections formula-based.
- **Table 13** (p. 1124) — imperfection factor α by buckling curve (a0=0.13, a=0.21, b=0.34, c=0.49, d=0.76).
- **Table 14** (pp. 1126–1127) — equivalent uniform moment factor Cm by bending-moment-diagram shape.
- **Table 15** (p. 1127) — design shear strength τ at steel-concrete interface: fully encased 0.30 N/mm², concrete-filled circular HS 0.55, rectangular HS 0.40, partially-encased flanges 0.20, webs 0.00.
- Combined compression+bending interaction equations (13.7–13.8), biaxial bending checks, mechanical shear connection at load-introduction zones (13.9, incl. frictional resistance credit µ=0.5 for studs against encased web flanges), full shear-check (13.10).

## 14 Construction and erection (p. 1131)
Fabrication/erection specs deferred to Part C/Sec 6A (steel) provisions generally.

## 15 Fire resistance and fire design (pp. 1131–1133)
Composite sections can achieve meaningful fire resistance *without* applied fire protection due to steel-concrete interaction raising critical temperature — literature-supported but not quantified numerically in this section. FRL determined per Sec 6A design-fire provisions. Active fire protection (detectors, extinguishers, sprinklers, vehicle access) + passive (intumescent paints, vermiculite boards) both required per the applicable fire-resistant level. Post-fire: mandatory structural inspection by competent experts before re-occupancy declared safe. See also [[Part F - Fire and Life Safety]] for the building-wide fire code.

## 16 Testing (p. 1133) → Annex E
Push-out test procedure for shear studs: min. 3 tests, load applied to reach failure in ≥10 minutes, concrete strength within ±20% of specified fck at test time, nominal static strength = lowest of fck·P/fc across tests (Annex E, pp. 1169–1170, Fig. 48).

## Annexes (design procedure appendices — pp. 1136–1171)
These are dense derivation/formula annexes; rather than transcribe every equation (real risk of subscript/symbol transcription errors in something used for actual structural design), each is summarized by purpose — **pull the PDF page directly when doing a real calculation**:
- **Annex A** (pp. 1132–1136): full symbol list.
- **Annex B** (pp. 1136–1150): bending resistance of composite beams — sagging (Tables 16–17, parabolic vs rectangular stress block methods), partial shear connection degree formulas, hogging bending resistance for plastic/compact (Table 18) and non-compact (Table 19) sections, hybrid-section flange stress reduction factor Rh, lateral-torsional buckling resistance at construction stage (incl. U-frame action, Tables 20–21), filler-beam deck moment resistance.
- **Annex C** (pp. 1150–1158): composite slabs — decking profile types (dovetail/trapezoidal), shear transfer mechanisms, ponding effects, full-shear-connection bending resistance (Table 22), partial-shear-connection via m-k method or partial interaction method (Table 23).
- **Annex D** (pp. 1158–1169): plastic design resistance of symmetric composite columns — axial resistance (Table 24, incl. k-factors for Fe250/415/500 = 0.90/0.82/0.77), bending resistance, neutral-axis location tables (Table 25), interaction curve points A/B/C/D for combined compression+bending (Table 26).
- **Annex E** (pp. 1169–1171): testing (push-out test, see above).
- **Annex F** (p. 1171): concrete strength/elastic modulus table by grade M20–M75 — **useful standalone reference**: fck, mean compressive strength fcm, mean tensile strength fctm, characteristic tensile strength fctk(0.05), elastic modulus Ecm (28,608–39,100 MPa across M20–M75).

## List of Standards (pp. 1172–1176)
Primary references: IS 456:2000 (concrete), IS 800:2026 (steel — note this section cites the *2026* edition of IS 800, not 2007), IS 2062 (Part 1):2025 (structural steel grades), IS 11384:2022 (composite construction — the base document for this whole chapter), plus ~40 more IS standards for bolts, welding, wire ropes, reinforcement grades, etc.

## Cross-references
- Loads (dead/imposed/wind/seismic/snow) and load combinations → **Part C, Section 1 — Loads and Load Effects** (cited repeatedly, e.g. cl. 3.17, 7.4.1–7.4.3).
- Steel material/design provisions not covered here → **Part C, Section 6A — Steel** (cited as "[C-6B(3)]" throughout — the whole chapter leans on Sec 6A for steel-only design rules).
- Concrete material/design provisions → IS 456:2000 (cited as "[C-6B(2)]" throughout).
- Fire safety access/firefighting provisions → **Part F — Fire and Life Safety** (cl. 15.1).
- Registered professionals / general administrative requirements → implied reference to Part A/B (not explicitly re-cited in this section's text).
