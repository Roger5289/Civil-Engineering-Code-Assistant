---
status: active
project: civil-engineering
type: reference
---
# Part C, Section 8 — Glass and Glazing

Selection, design, fabrication, installation, testing and maintenance of glass/glazing in buildings: type selection, energy/light performance, structural thickness design against wind/seismic loads, fire safety, human-impact safety (including balustrades/railings — directly relevant to staircases), and security glazing (bullet/blast/burglar resistance). PDF pages 1329–1524 (Vol 1's Index of Terms starts at p.1524, tail end of this range).

## 1 Scope (p.1333) & 2 Terminology (p.1333–1338)
Covers glass selection, energy/light guidance, wind/seismic/fire selection, human-impact safety, glazing-system design/fabrication/install/test/maintenance, and security glass. Does **not** cover patent glazing. ~98 defined terms (Annealed, Balustrade, Bite, Curtain Wall, Fenestration, Glazing Bite (min 10 mm, p.1334), Safety Glass, Toughened/Tempered, etc.) — see PDF pp.1333–1338 for exact wording of any term.

## 3 Application (p.1338) & 4 General Methodology for Selection (p.1338–1346)
- Selection driven by application, cost-benefit, and sustainability guidance (Handbook on 'Sustainability in Buildings').
- **Table 1 — Typical Properties of Various Types of Glass** (p.1341, Cl 4.2.1): modulus of rupture — Annealed/Float/Annealed Laminated 40 N/mm², Tempered/Toughened 120–200 N/mm²; density ~2400–2550 kg/m³; modulus of elasticity 70 GPa; compressive strength 1000 N/mm².
- Glass types: Annealed, Laminated Safety, Toughened/Tempered, Heat Strengthened (surface compression 31–52 MPa, p.1342), Coated, Insulating Glazing Unit (IGU), Rolled/Wired, Glass Fins.
- **Table 2 — Preformed Tape properties** (p.1343–1344).
- **Table 3 — Minimum Dimensions for Glazing Material** (edge clearance/cover/rebate depth by nominal thickness 3–25 mm) (p.1346, Cl 4.5.2.1/4.5.2.3).
- **Table 4 — Indicative accepted standards by glass type** (p.1349).
- Frame deflection limits per 6.3.6.2(c); jumbo/stock/split glass sizes (Cl 4.7.3–4.7.5).

## 5 Energy and Light (p.1346–1358)
Thermal/solar/daylight performance methodology (largely calculation-heavy, IS 16231-based) — U-value, SHGC/solar factor, light transmittance, UV-transmittance, glare, daylight analysis. Key practical tables:
- **Table 6 — U-value, single glazing** (4–12 mm: 5.8→5.5 W/m²K) (p.1365).
- **Table 7 — U-value, IGUs** (with/without Low-E coatings, air/argon fill) (p.1365–1366).
- **Table 8 — U-value, coupled glazing** (p.1366).
- **Table 9 — Thermal performance of shading devices** (plain glass, wire mesh, painted, heat-absorbing, venetian blind, % shaded) (p.1367).
- Tables 5, 10, 11 are spectral-distribution constants for solar/UV/light-transmittance calculations (p.1352–1373) — only needed if doing a from-first-principles optical calc; otherwise use manufacturer data.
- Annex B (below) gives the prescriptive minimum performance shortcuts instead of full calculation.
- **Note**: formulas in this clause involve integrals/summations over wavelength — open PDF directly if doing an actual energy calc rather than relying on a transcription here.

## 6 Structural Parameters and Fire Safety (p.1377–1424) — core design clause
### 6.1 Determination of Appropriate Glass Thickness
- Applies only if: ultimate limit state wind pressure ≤ 10 kPa; max panel area 15 m²; max span 4 m; aspect ratio > 1.5 (else step up thickness); factor of safety 2.5 (p.1377–1378).
- Design flexural tensile strength: 16.7 N/mm² (T ≤ 6 mm), 15.2 N/mm² (T > 6 mm).
- **Empirical relation**: Pnet·A = 200Tk (T ≤ 6mm) / 200Tk+1900 (T > 6mm) — **Table 13** gives k by nominal thickness (p.1378).
- **Table 14 — Strength factor Pf** (p.1380): Normal 1.00, Laminated 0.80, Tempered 2.50, Insulated 1.50, Heat strengthened 1.60, Wired 0.50.
- **Table 15 — Max aspect ratio (ARmax) by thickness** (3mm→7.3 down to 25mm→2.9) (p.1380).
- **6.1.6 Seismic design**: Pnet = pz·Cp, pz = 0.6 Vz², Vz = Vb·k1·k2·k3·k4 per wind-load good practice [C-8(15)] (India's wind load code). **Table 16** classifies architectural elements (glazing = Secondary response to acceleration, Primary to deformation; **Stairs = Primary to acceleration, Secondary to deformation**, p.1381).
- **6.1.9 / Tables 17–26 — glass thickness/area/span selection charts** (p.1383–1420, ~40 PDF pages of dense multi-page lookup tables): max allowable panel area vs design wind pressure (500–5000 N/m²) for Annealed (Tbl 17), Laminated (Tbl 18), Tempered (Tbl 19), Insulating (Tbl 20), Heat-strengthened (Tbl 21) glass fixed on all 4 sides; and max span for the same 4 glass types fixed on 2 opposite sides (Tbl 22–25). Table 26 = ultimate limit state design stresses by glass type/thickness at edge vs away-from-edge.
  **These are large multi-page numeric lookup tables — NOT transcribed here (transcription-error risk on safety-critical wind design data). For an actual design value, open the PDF at the page above and read the row for your design wind pressure/thickness directly, or use the empirical formula in 6.1.3 with Tables 13–14.**
- **6.2 Installation** (p.1414–1418): setting/location blocks, distance pieces, glazing beads, structural sealant application.
- **6.3 Design Criteria** (p.1418–1424): deflection limits — mullions Span/175 or 19mm; transoms Span/500(dead)/Span/175(wind); glass centre deflection Span/60 or 19mm (monolithic), Span/90 or 19mm (DGU); glass edge deflection ≤15mm (p.1419). Structural silicone bite formulas (6.3.8). Handling/transport/storage requirements.
- **6.4 Fire Safety** (p.1424–1425): fire-resistant glass types (wired, glass-ceramic, borosilicate, laminated, intumescent-interlayer, gel-filled, Low-E). Refers to **Part F Fire and Life Safety** for fire-rating criteria and general provisions.

## 7 Safety Related to Human Impact, Anti-Fallout, Window Restrictors, Dynamic Wind Restraint (p.1425–1432)
- **7.1.3 Critical Location**: glazing within **1.5 m above floor level** is deemed subject to human impact and needs safety glazing — explicitly including **"balustrades, stairs and floors"** (p.1426).
- **Table 27 — Type of glass by critical-location case** (p.1428–1430): Case 5 "**Glass acting as a Balustrade/Railing (human impact + risk of fall) → Laminated safety glass mandatory**"; Case 4 (horizontal/sloped glazing incl. stairs) → Laminated safety glass; Cases 1–3 (vertical walls by sill/fall height) → Any glass to Safety glass depending on Hs/Hf.
- **Table 28 — Minimum mechanical strength for fully toughened glass** (p.1432): Float 120 N/mm², Enamelled 75, Patterned 90.
- **7.2 Anti-fallout**: mandatory secondary device for open-out windows in buildings > 5 storeys (>15m); optional below.
- **7.3 Window restrictor for children**: max clear opening 100mm (250N force test); mandatory for residential apartments, recommended for commercial.
- **7.4 Dynamic wind restraint**: for open-out windows in buildings >15m with high dynamic wind.

## 8 Glazing System — design/fabrication/install/test/maintenance (p.1432–1444)
- **Table 29** cross-references every design consideration (structural, energy, safety, acoustics) to its governing clause/standard (p.1433–1435).
- Frame materials: Aluminium alloy (6063-T5/T6, 6060-T66, 6061/6105 for higher strength), Stainless steel (Type 304/316 general, 316 for coastal/high-corrosion, 430 interior-only), uPVC, Timber (p.1435–1437).
- **Table 30 — Testing of glazing systems** (air permeability, water penetration static/dynamic, wind resistance, structural load 100%/proof load 150% design wind, seismic racking (Annex F), fire resistance, bullet/blast resistance) (p.1441–1442).
- Maintenance: facade access (cradles, rail systems, fall-arrest), material-specific care for coated glass.

## 9 Security Glass (p.1444–1449)
- **Table 31 — Min glazing resistance class by burglar-resistance class** RC1–RC6 (p.1445).
- **Table 32 — Selection criteria by offender type/property type** (residential/commercial/high-risk) (p.1445–1446).
- **Table 33 — Bullet threat levels** 1–6 (ammunition, velocity, distance, strikes) (p.1447).
- **Table 34 — Blast threat levels** 1–6 (TNT-equivalent charge mass, standoff distance, height of burst) + damage categories A–F (p.1448–1449).

## Annexes (p.1449–1488)
- **Annex A** (p.1449–1453): curtain wall/storefront inter-storey drift test method (seismic Zones IV/V mandatory). Elastic design displacement default H/500 if unspecified.
- **Annex B** (p.1453–1454): prescriptive minimum performance shortcuts — max Window-Wall Ratio 70%, min visible-light-transmission by WWR band (0–0.3 WWR → 27% VLT down to 0.61–0.7 → 11%); air infiltration limits; smoke/heat exhaust venting guidance (cross-refs Part F).
- **Annex C** (p.1454+): test requirements for coated glass.
- **Annex D** (p.1459): deflection formula w = t·exp(r0+r1X+r2X²) with worked coefficients — used for checking actual panel deflection.
- **Annex E** (p.1459–1461): full worked example — 1200×1800mm annealed glass panel, Chennai wind load → 6mm thickness selected, deflection check 4mm < 19mm allowable. Good template for a real calc.
- **Annex F** (p.1462–1463): seismic racking test + Building Maintenance Unit (BMU) pull-out test (1.5 kN, 5 directions).
- **Annex G** (p.1463+): blast-resistant glazing test method — must be done by GoI-accredited labs only.
- **Annex H** (p.1467–1469): mirror installation (ventilation gaps 5mm <1m height / 10mm >1m; neutral-cure silicone only, no acetoxy).
- **Annex J — Glass Railings** (p.1470–1483, informative but Annex, cross-refs the whole staircase/balustrade picture):
  - Railing needed at level changes ≥600mm (dwellings) / ≥380mm (other buildings).
  - Gaps must not pass a 100mm sphere (child safety).
  - Design load applied at notional height 1.1m above floor regardless of actual railing height.
  - 5 railing types: Full Height, Glass Infill (vertical-edge/horizontal-edge/4-edge/patch-bolted), Free-Standing (laminated glass mandatory, min 100mm bottom embedment), Bracket systems.
  - **Table 35 — Minimum barrier heights** (p.1475): **stairs/landings/ramps/internal floor edges = 900mm** (all occupancies); windows 800–1200mm by floor count; balconies 1100–1200mm.
  - **Table 36 — Minimum horizontal imposed loads** (p.1478–1479): **stairs/landings/corridors/ramps (general) = 0.74 kN/m line load, 1.0 kN/m² infill UDL, 0.5 kN point load**; single-family-dwelling stairs = 0.36 kN/m / 0.5 / 0.25; light access stairs ≤600mm wide (offices) = 0.22 kN/m only; areas susceptible to overcrowding = 1.5–3.0 kN/m.
  - Deflection limit: railing displacement ≤ H/65 or 25mm, whichever smaller (p.1480).
  - J-4.6: in-fill/uniform/concentrated load test + shot bag impact test (45.4kg bag) sequence for railings in overcrowding-prone areas.
- **Annex K** (p.1487–1488): Conformity assessment checklist sheet (building typology, glass type/thickness/deflection vs calculated, safety compliance) — informative template for regulatory submission.

Volume 1's "Index of Terms" begins right at the tail of this range (p.1524, printed page numbering restarts there) — no further substantive Section 8 content after Annex K.

## Cross-references
- **Part F, Fire and Life Safety** — general fire provisions, fire-rating criteria, smoke/heat exhaust venting, fire-rated glass door/window testing (cited repeatedly: Cl 6.4.1, 6.4.2.3, 6.4.5, 7.2, Annex B-4).
- **Part C, Section 1 (Loads and Load Effects)** — referenced for seismic design force on architectural elements/utilities (Cl 6.1.6.3) and for general wind/imposed load good practice cited throughout as "[C-8(15)]", "[C-8(17)]", "[C-8(21)]", "[C-8(27)]" (India's wind-load and loads codes — these accepted-standard references are almost certainly to Part C Sec 1 of this same NBCS or its IS 875 lineage; worth confirming exact IS number against the accepted-standards list at the end of this Section, p.~1487+, when cross-checking Sec 1).
- **Part D, Building Services, Section 1 (Lighting and Natural Ventilation)** — lighting design considerations (Table 29 item ii-e).
- **Part D, Building Services, Section 4 (Acoustics)** — sound insulation for glazing systems (Cl 8.2.2.5).
- Handbook on 'Sustainability in Buildings' (external, not part of this NBCS) — cited repeatedly for WWR/energy prescriptive values, cost-benefit selection guidance.
- Handbook on 'Asset and Facility Management in Buildings' (external) — facade maintenance access.

## Fidelity notes
- Tables 17–26 (glass thickness/area/span wind-load charts, ~40 pages) and the optical-calculation constant tables (5, 10, 11) are referenced by page/scope only, not transcribed — pull the PDF page directly for an actual design value.
- No pdfplumber table cross-check was available for this page range (background extraction hadn't reached/found tables here) — treat every numeric value above as **verify against PDF** before using in real design work, especially Tables 13–28 and 31–36.
