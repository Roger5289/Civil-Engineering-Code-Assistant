---
status: active
project: civil-engineering
type: reference
---
# Part C, Section 1 — Loads and Load Effects

Covers dead load, imposed (live) load, wind load, earthquake load (by reference), snow load, special/accidental loads, load combinations and multi-hazard risk mapping for structural design. Based largely on IS 875 (Parts 1-5) and IS 4991 (blast). PDF pages 155-382. Foreword/scope: p.157-160.

## 2. Dead Load (p.163)
Weight of all permanent construction (walls, partitions, floors, roofs, finishes, cladding, fixed services). Unit weights: Annex A (below). Roof gardening/landscaping treated as dead load — use **saturated** soil/drainage weight when it adds to load, **dry** weight when it resists uplift (p.163).

## 3. Imposed (Live) Load — Floors (p.163-175)
**Table 1 (p.166-174) — Imposed Floor Loads by Occupancy** (UDL kN/m², concentrated load kN). Selected values (staircase-relevant rows called out; full table has ~10 occupancy classes: Residential, Educational, Institutional, Assembly, Business/Office, Mercantile, Industrial, Storage, Refuge areas, Datacentres):

| Occupancy | Corridors/passages/**staircases incl. fire escapes** | Balconies |
|---|---|---|
| Dwelling houses | 3.0 kN/m², 4.5 kN | 3.0 kN/m², 1.5 kN/m run at outer edge |
| Low-income dwelling units (IS 8888:2020) | 3.0 kN/m², 4.5 kN | 3.0 kN/m², 1.5 kN/m run |
| Hotels/hostels/dormitories | per floor serviced, min 3.0 kN/m², 4.5 kN | min 4.0 kN/m² |
| Educational | min 4.0 kN/m², 4.5 kN | min 4.0 kN/m² |
| Institutional | min 4.0 kN/m², 4.5 kN | min 4.0 kN/m² |
| Assembly | 4.0 kN/m², 4.5 kN | min 4.0 kN/m² |
| Business/Office | min 4.0 kN/m², 4.5 kN | min 4.0 kN/m² |
| Mercantile | 4.0 kN/m², 4.5 kN (5.0/4.5 if wheeled-load traffic) | min 4.0 kN/m² |
| Industrial | 4.0 kN/m², 4.5 kN | — |
| Storage | per floor serviced | — |

Other Table 1 rows worth knowing: dwelling rooms/kitchens 2.0 kN/m²; garages (cars ≤2.5 t) 2.5-5.0 kN/m², 9.0 kN conc.; roof-top solar panels 1.75 kN/m²; roof-top HVAC 9.0 kN/m²; datacentre data hall 7.2-12 kN/m² by tier; refuge area/disaster shelter 3.0 kN/m².

**Reduction for columns/walls/foundations (3.3.2.1, p.175):** by floors carried — 1 floor: 0%, 2: 10%, 3: 20%, 4: 30%, 5-10: 40%, >10: 50% (never below load for 5.0 kN/m² design). Beams: 5%/50m² supported, max 25% (3.3.2.2).

**Table 2 — Roof imposed loads (p.176):** flat/sloping ≤10°, access provided: 1.5 kN/m²; no access: 0.75 kN/m²; >10° slope: 0.75 − 0.02/degree over 10°, min 0.4 kN/m².

**Table 3 — Horizontal loads on parapets/balustrades/handrails (p.178-179)** — directly governs staircase/balcony railings:
| Usage | kN/m run | Conc. (per 3m) kN |
|---|---|---|
| Light access stairs ≤600mm wide | 0.25 | — |
| Light access stairs >600mm, **stairways/landings/balconies (private dwellings)** | 0.35 | — |
| **All other stairways, landings, balconies, roof parapets/handrails** | 0.75 | 0.89 |
| Assembly areas not overcrowded (restaurants, retail) | 1.5 | 1.5 |
| Assembly areas likely overcrowded (theatres, malls, worship) | 3.0 | 1.5 |
| Grab bars | — | 1.11 |
| Fixed ladders | — | 1.33 |
| Guardrail/handrail assemblies | 0.73 | 0.89 |

Impact allowance (3.6.1, p.180): lift/hoist frames 100% min; foundations for lifts 40%; light machinery supports 20%; reciprocating machinery 50%.
Crane loads, helipad design (3.7, p.182-184), fire tender/emergency vehicle loads (3.8, p.184): bare-slab loading 15-20 kN/m² absent other data, accidental-load partial factor 1.05.

## 4. Wind Load (p.185-244)
Master equations:
- Design wind speed: **Vz = Vb·k1·k2·k3·k4** (p.190) — k1 risk coefficient (Table 4, p.192, by structure design-life: general bldgs 1.0, temporary 0.67-0.82, important/hospitals 1.05-1.08), k2 terrain+height (Table 5, p.193), k3 topography (≥1.0, cliffs/hills, Annex F), k4 cyclonic-region importance (coastal belt: post-cyclone/emergency structures 1.30, industrial 1.15, others 1.00).
- Design wind pressure: **pd = Kd·Ka·Kc·pz**, where pz = 0.6Vz² (p.196-197); pd ≥ 0.70pz.
- Basic wind speed map: Fig.1 (p.194, 50-yr return period) — city/town table in **Annex D** (p.309-310; e.g. Delhi/Kolkata/Chennai/Mumbai region 44-50 m/s, Bengaluru/Mysuru 33 m/s — full ~120-city list on those pages).
- Wind load on individual elements: F = (Cpe − Cpi)·A·pd (4.5.3.1, p.198). Internal pressure coefficient ±0.2 (openings <5% wall area), ±0.5 (5-20%), ±0.7 (>20%).
- Force on structure as a whole: F = Cf·Ae·pd (4.5.4).
- **Tables 7-38 (p.200-236)** — area averaging factor, external/internal pressure coefficients (walls, pitched/monoslope/curved/canopy/multi-span/cylindrical roofs), force coefficients (clad buildings, hoardings, lattice towers, individual members, wires/cables, frames) — **these are rendered as diagram-images in the source, not machine-readable text/data**. Captions and clause references are indexed above; open the cited PDF page directly for the actual coefficient values/curves.
- Dynamic wind response (Gust Factor Method, along-wind p.239-242; across-wind p.242-244) for tall/flexible structures (height/width ≥5, or natural frequency <1 Hz). Damping coefficients (Table 39, p.242): welded steel 0.010, bolted steel/RCC 0.020, prestressed concrete 0.016.
- Interference effects (4.6, p.236-238): low-rise closely-spaced buildings up to +25% at 5b spacing; tall-building interference zones Z1-Z4 give IF 1.35/1.25/1.15/1.07.
- Vortex shedding, galloping, flutter, ovalling — qualitative design triggers, p.238-240.

## 5-6. Earthquake Effects (p.244)
This section does **not** itself give seismic design method — it refers out: masonry buildings → **Part C Sec 4 Masonry**; concrete → **Part C Sec 5 Structural Concrete**; steel → **Part C Sec 6A Steel**; general seismic zoning/analysis → IS 1893 (Part 1):2016 [good practice C-1(6)], noting IS 1893 itself was under revision at NBCS publication.

## 7. Snow Load (p.245-252)
s = μ·s₀ (design snow load = shape coefficient × ground snow load). Ground snow load s₀ for J&K/Ladakh/HP/Uttarakhand: **Annex H** (p.316-319) gives a zone-map formula s₀ = 1.624×(Z−0.5)×[1+(A/2677)²] kPa (Z = zone 1-5 from map, A = altitude); Sikkim uses a direct map (Fig.22). Applies only 1000-4000m altitude. Shape coefficients μ for mono/pitched/multilevel/curved roofs: 7.4.2 (p.246-252) and **Annex J** (p.320) for multilevel roofs. Ponding/rain-on-snow check required (7.3.4); water load due to ponding ≥0.24 kPa.

## 8. Special Loads (p.252-262)
Temperature effects (8.2), hydrostatic/soil pressure incl. uplift design and effective pillar width in sloping soil (8.3, Fig.11 p.253), fatigue (8.4), construction-stage loads (8.5), **accidental loads** (8.6): vehicle impact on structural elements (fictitious 400kg+12000kg vehicle model at 10 m/s, p.255), vehicle barriers in car parks (**F [kN] = 0.5·m·v² / (δc + δb)** — m in kg, v in m/s, δc = vehicle deformation & δb = barrier deflection in mm; defaults for cars ≤ 2500 kg: m = 1500 kg, v = 4.5 m/s, δc = 100 mm → rigid barrier (δb = 0) force **150 kN** at bumper height 375 mm; ramp barriers half this at 610 mm; ends of downward ramps > 20 m long take twice this; 8.6.1.2.2, p.256), crane buffer impact on buffer stop (Py = MV²/F, p.257), explosion in closed rooms (8.6.2, p.257-259), air-raid shelter loads (28-41 kN/m² by storeys, p.259), fire accidental loads (q=12·tb kJ/m², p.260). Landslide control good-practice pointers (8.10, p.260) and cyclone-resistant building pointers (8.11, p.261).

## 9. Load Combinations (p.261-262)
DL, IL, WL, EL, TL combined per relevant design code; snow replaces IL when present. Overturning: restoring moment ≥1.2×DL overturning + 1.4×IL overturning (only 0.9×DL if DL restores). Uplift factor of safety 1.2. Sliding factor of safety ≥1.4 (0.9×DL only). Wind vs bearing pressure: neglect if <25% of DL+IL pressure.

## 10. Multi-Hazard Risk by District (p.262-264, list in Annex M p.368-369)
Concept + criteria for EQ+Flood / Cyclone+Flood / EQ+Cyclone+Flood / EQ+Cyclone prone districts. Full district list (**Annex M/Table 61, p.368-369**) covers Andhra Pradesh, Assam, Bihar, Goa, Gujarat, Haryana, Kerala, Maharashtra, Orissa, Punjab, UP/Uttarakhand, West Bengal, Delhi — India total: 139 districts (EQ+Flood), 6 (Cyclone+Flood), 29 (EQ+Cyclone+Flood), 16 (EQ+Cyclone).

## 11. Documentation — Structural Design Basis Report, SDBR (p.264-265, full format Annex N p.370-374+)
SDBR mandatory with Building Permit application for high-rise/special buildings. Four parts: (1) General info/data — address, structure type, soil bearing capacity, dead/imposed load assumptions, wind speed & pressure, seismic zone/importance factor/zone factor/response reduction factor; (2) Load-bearing masonry buildings (IS 4326 seismic band/reinforcement checklist); (3) RCC buildings; (4) Steel/composite buildings. RC-frame SDBR Part 3 may be submitted up to 1 month before construction start with an undertaking.

## Annexes (reference tables, not fully transcribed here)
- **Annex A (p.265-304)** — Unit weights of building materials (Table 40) and stored/miscellaneous materials incl. angle of friction (Table 41). Alphabetical by material, ~50 categories, hundreds of line items (acoustics materials, aggregates, bricks, cement, concrete variants, metals/alloys, pipes by class/diameter, plaster, roofing, soils, stone, timber species — **~150 Indian timber species individually listed**, chemicals, fuels, ores, textiles). Selected commonly-needed values: PCC with sand/gravel aggregate 22.0-23.5 kN/m³; RCC (1-5% steel) 22.75-26.5 kN/m³; brick masonry (common burnt clay) 19.25 kN/m³; granite ashlar masonry 25.0 kN/m³; structural steel 78.5 kN/m³ (as density, sections per IS 808/4923/811/1173/2314). **For any specific material not listed here, open PDF pp.265-304 directly** — the table is too large to usefully duplicate.
- **Annex B (p.305)** — worked example, imposed-load reduction for a multi-storey column.
- **Annex C (p.306-308)** — full wind-load notation list.
- **Annex D (p.309-310)** — basic wind speed by city/town (~120 Indian cities, 33-55 m/s range).
- **Annex E (p.310-312)** — velocity profile at terrain-category changes.
- **Annex F (p.312-314)** — k3 (topography) factor derivation for cliffs/escarpments/hills/ridges.
- **Annex G (p.315-316)** — wind force on circular sections, Reynolds-number dependence.
- **Annex H (p.316-319)** — characteristic ground snow load procedure + zone maps (J&K/Ladakh/HP/Uttarakhand/Sikkim).
- **Annex J (p.320)** — extended shape-coefficient formula for multilevel roofs.
- **Annex K (p.320-322)** — vibration sources/serviceability verification approach (human, machine, wind, blast, traffic, earthquake induced).
- **Annex L (p.322-~369)** — **blast-resistant design**, large specialized annex: terminology, TNT-equivalence table (Table 42, p.329) for ~19 explosive types, structure importance categories (Table 43, p.330: Low = residential ≤50 occupants; Medium = larger residential/schools/offices/cinemas/continuous-occupancy industrial; High = lifeline structures + more), threat assessment, SDOF/MDOF blast response methodology, standoff-distance and scaled-distance (cube-root scaling) calculations. Only relevant if blast resistance is a determined credible threat (owner/authority decision) — **consult PDF directly pp.322-369** if a project actually requires this; not condensed further here given how specialized and rarely-applicable it is to normal building design.
- **List of Standards (p.375-382)** — full IS-code bibliography referenced throughout this section, keyed to inline [C-1(n)] citations.

## Cross-references found in text
- Earthquake design of masonry → **Part C Sec 4 Masonry** (p.244)
- Earthquake design of concrete → **Part C Sec 5 Structural Concrete** (p.244)
- Earthquake design of steel → **Part C Sec 6A Steel** (p.244)
- "This Section shall be read together with Sections 2 to 8 of Part C" (p.160)
- Blast design (Annex L) references IS 4991 (Part 1):2024 and works alongside other design standards, not replacing them (p.322)
