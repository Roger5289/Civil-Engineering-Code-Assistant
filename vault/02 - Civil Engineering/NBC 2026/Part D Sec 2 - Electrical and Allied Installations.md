---
status: active
project: civil-engineering
type: reference
---
# Part D, Section 2 — Electrical and Allied Installations

Electrical wiring, substations, earthing, lightning protection, EV charging, solar PV, and allied services for buildings. PDF pages 1643–1860 of `NBC-2026- Vol-1 & 2.pdf`. Standards cited as `[D-2(n)]` refer to the section's own "List of Standards" (pp. 1849–1858) — open that range to resolve a specific `[D-2(n)]` reference.

## 1–2. Scope and Terminology (p. 1649–1663)
Covers general electrical installation requirements for efficient/safe electricity use, renewable sources, EV charging, lightning protection, allied installations. Clause 2.1 is a ~190-entry alphabetical glossary (p. 1649–1663) — not reproduced here; look up a term directly on that page range if needed. Notable defined voltage bands (2.1.191–194): ELV ≤ 50 V; LV > 50 V to 1000 V a.c./1500 V d.c.; HV > 1000 V a.c. to 33 kV; EHV > 33 kV.

## 3. General Requirements (p. 1663–1669)
- All installations must conform to the Indian Electricity Act 2003 and **CEA (Measures Relating to Safety and Electric Supply) Regulations, 2023** — referenced throughout as "CEA Regulations"; key extracts are reproduced in **Annex B** (p. 1809–1830).
- Stakeholders defined: owner/developer, architect, civil contractor, other service providers, electrical consultant, electrical contractor, electrical inspector, electricity supplier (p. 1665–1668) — each with listed responsibilities. An **electrical engineer on site** must be appointed as a registered building professional.
- Power factor: supply boards generally require ≥0.95 lag.

## 4. Planning of Electrical Installations (p. 1669–1686)
**Substation location (4.2.1, p. 1671–1675)** — key numeric rules:
- Avoid basement location; if unavoidable, floor level ≥0.6 m above lowest basement point.
- >2 basements: substation only in 1st/2nd basement, ≤10 m below adjoining ground level.
- Flood-prone areas: floor level ≥300 mm (general) or ≥300 mm above max flood (storm water) / ≥1000 mm trigger for single-feeder-only rule.
- Oil-filled equipment: ground floor or 1st basement only, ≥6 m clear distance from adjoining buildings, baffle walls of 4 h fire rating if oil >2000 L, day-tank/oil limits per Petroleum Act 1934.
- Dry-type substations may go on upper floors only for exceptional building types (ATC towers, high-rise >150 m, data centres) with a **base substation** at ground/1st basement feeding life-safety loads.
- Min clearance transformer-to-wall: 0.75 m (wall 2 sides) / 1.0 m (wall 3 sides) / 1.25 m (enclosed room) — Fig. 1A.
- Min substation room height: 1200 mm clearance from equipment top to beam soffit (Annex C note).
- Compact substation fencing: ≥750 mm (≤12 kV incomer), ≥1000 mm (12–24 kV).
- Switchboard clearances (5.3.6.7, Fig. 2): ≥1 m front; back space either <200 mm or >750 mm; if >750 mm, passage ≥1.8 m high; facing switchboards ≥2.0 m apart.

**Emergency DG sets (4.3, p. 1676–1678):** not above ground floor / below 1st basement (1st floor allowed if dedicated approach + fire compartment); DG room height ≤3000 mm above set height; day-oil tank <1000 L (with genset), <1500 L in adjacent room; vertical stacking discouraged (120 min fire barrier if unavoidable); horizontal stacking ≥1.2 m apart.

**Battery storage (Li-ion) (4.4):** ventilated room, 18 air changes/hour, gas monitoring.

**Diversity factors table (4.2.2.2, p. 1678–1680):** allowances by building type (individual household / small shops-offices / small hotels) for lighting (66–90%), heating/power, A/C, cooking, laundry, motors, lifts (100% cumulative — no diversity), water heaters, standard final circuits, socket-outlets.

## 5. Distribution of Supply and Cabling (p. 1686–1706)
- Nominal LV supply: 240 V single-phase / 415 V 3-phase, 50 Hz. Voltage drop ≤6% overall (3% DB→last point).
- Typical supply voltage by load: 240 V ≤5 kVA; 415 V 3-ph 5–100 kVA; 11/22 kV up to 5 MVA; 33 kV >5 MVA.
- EV charging >100 kVA on a >1000 kVA mixed-use site: independent dedicated transformer (≥200 kVA) recommended.
- Energy meters: height 750–1800 mm; >24 meters on one board → move to floor-wise metering with rising main taps.
- **Table 1A/1B (p. 1715, 1718):** max number of single-core copper cables permitted per rigid steel / non-metallic conduit size (20/25/32/40/50/63 mm), by conductor CSA 1.5–35 mm².
- Branch DB / RCD rule: **30 mA RCCB/RCD at DB incomer** for residential, schools, hospitals; **100 mA** for other buildings.
- Sub-circuit load limits: kitchen/bathroom sub-circuit ≤800 W or 10 points; lighting sub-circuit ≤800 W/20 points; 6 A socket sub-circuit ≤800 W/8 nos; power sub-circuit ≤2 sockets of 16 A on 4 mm² Cu; general LV sub-circuit ≤3000 W.
- **Minimum wire sizes (Table, p. 1700–1703):** lighting 1.5 mm²; 6 A/16 A socket-outlets, water heater <3 kW, permanently connected appliances >10 A: 2.5 mm²; heaters/range/AC ≥3 kW: 4 mm²; appliance 3–6 kW: 6 mm². Conductors ≤25 mm² must be copper (aluminium banned below this size).
- Lighting demand where unspecified: 13 W/m² (all built-up incl. balconies); covered parking 3.23 W/m²; power ≥55 W/m² (overall diversity ≤50%).
- Underground cable protection (Table, p. 1703): bricks 100 mm wide/25 mm thick + 100 mm sand cushion; concrete slabs ≥50 mm; PVC/plastic slabs ≥10 mm.

## 6–7. Wiring & Fittings (p. 1706–1723)
- Conductor: copper only for internal wiring; min 1.5 mm² (fan/light final sub-circuit), 2.5 mm² (power wiring), 1.5 mm² (flexible cord).
- Socket-outlet heights: general ≤1.2 m; accessible design (disabled/elderly) 800–1100 mm, ≥600–700 mm from internal corner; kitchen/bath/garage sockets NOT within 1 m of ground level (except exception: wall sockets/TV/phone points may go to 400 mm).
- Ceiling fan: bottom clearance ≥2.4 m above finished floor; ≥300 mm ceiling-to-blade clearance. Fan sweep options 900–1500 mm; typical spacing 3 m in long halls; one 1200/1400 mm fan covers ~9–10 m².
- Bare lamp minimum mounting height: 2.4 m above floor.

## 8. Earthing (p. 1723–1738)
- Systems: **TN** (TN-C / TN-S / TN-C-S), **TT**, **IT** (2.1.185, 8.1.4) — TN-S with equipotential bonding is the default deemed-compliant system (8.9).
- LV 3-ph neutral: earthed by ≥2 separate/distinct connections; neutral conductor sized ≥ phase conductor (not half, due to harmonics).
- **Table 2 (p. 1732–1733):** minimum earth-electrode dimensions by material (copper, hot-dip galvanized steel, stainless steel, copper-clad steel etc.) for corrosion/mechanical strength when embedded in soil/concrete.
- Standard maintenance-free earthing arrangement (Fig. 9/10): 100 mm CI pipe/copper rod electrode, 150 mm earth-enhancement compound layer, exothermic welding, inspection chamber.
- Earth enhancing compound: must not use NaCl (accelerates ferrous corrosion); must meet TCLP toxicity requirements.

## 9. Inspection, Testing, Commissioning (p. 1738–1745)
- Insulation resistance of installation: ≥ 50/(no. of points) MΩ, min 1 MΩ overall.
- Motor insulation resistance guide: Ri (MΩ) = 20×En / (1000+2P), at 25 °C.
- Testing periodicity: general electrical ≤6 months; LPS test joint opened to confirm total LPS resistance ≤10 Ω to earth (add down-conductors if exceeded).
- Full checklists (substation, HV/LV equipment, overhead lines, lighting circuits) at 9.2.2.1–9.2.2.4; blank test/commissioning forms in **Annex E** (p. 1833–1844, per-equipment: HV cable, HV panel, transformer, MV/LV panel) and completion certificate in **Annex F** (p. 1844–1847); design/construction/testing declarations in **Annex G** (p. 1849).

## 10. Allied/Miscellaneous Services (p. 1745–1762)
- **UPS (10.3.2):** dedicated IT-system neutral earth pit; 3-ph UPS → 4-pole CB, 1-ph → double-pole CB.
- **BMS (10.4):** integrates substation, HVAC, lighting, lifts, fire, security, car parking for central monitoring.
- **EV charging (10.7, p. 1749–1751) — key numbers:**
  - Target: 20% of parking area EV-ready (residential/office/institutional; ~40% of commercial); trending to 30% by 2030.
  - Charging permitted in open areas and up to 1st basement only (not last basement); two-wheelers restricted to ground floor only.
  - Two-wheeler groups: max 2 vehicles side-by-side, ≥1 m between groups; outlets grouped in 4s, 10 A 3-pin + 30 mA RCD; spacing 4–5 m.
  - Residential slow-charging: 2×15 kW single-phase + 2×15 kW three-phase outlets per point, MCCB + 30 mA RCD.
  - Public/commercial: 15/30/60 kW points, 30 mA RCD/RCBO; 1st basement capped at <15 kW.
  - Cables ≤50 mm² must be copper, 4-core.
  - Electric bus depots: ≥2 DC fast chargers ≥240 kW each (Level 3/4).
  - Residential EV charging safety (10.7.6): no extension cords; dedicated circuit installed by qualified electrician.
- **Solar PV (10.8, p. 1751–1758):** grid-tied vs off-grid systems; components table (modules, mounting structure, DC/AC distribution boxes IP65, inverter IP54, cables ≤2% voltage drop, earthing, LPS, net meter) at p. 1755–1756. BIPV (10.8.4) integrates PV into facade/roof/skylight as structural element.
- **Solar water heating (10.9):** 100–300 L residential; water heated 60–80 °C; must bond to LPS down-conductor.
- **Aviation obstacle lights (10.10):** required per ICAO Annex 14 based on height; spacing per Fig. 17 (45–90 m between lights <45 m tall, tighter for taller).
- **Electric/power fence (10.11):** fence height 1.5 m above wall, wire spacing 100 mm, posts ≤3 m apart, must withstand 120 kmph wind.

## 11. Lightning Protection of Buildings (LPS) (p. 1762–1792)
Based on IEC 62305 (2024 series). Four LPS classes I–IV (I = max protection).

**Table 3 — protection method parameters by class (p. 1763):**
| Class | Rolling sphere radius | Mesh size | 
|---|---|---|
| I | 20 m | 5×5 m |
| II | 30 m | 10×10 m |
| III | 45 m | 15×15 m |
| IV | 60 m | 20×20 m |

**Table 4 — min distance between down-conductors:** Class I/II: 10 m; III: 15 m; IV: 20 m. Min 2 down-conductors (diagonal) for buildings <100 m².

**Table 5 — min vertical earth electrode length by soil resistivity** (Class I: 2.5–40 m across 500–3000 Ω·m; Class III/IV: flat 2.5 m regardless of resistivity).

- RCC columns/foundation rebar can serve as natural down-conductors/earth electrodes if continuously welded/clamped (overall reinforcement resistance target ≤0.2 Ω) — this is standard practice and should be coordinated with the structural engineer **before construction starts**, not retrofitted.
- Buildings >60 m: side-strike risk on protruding elements (balconies, cameras) in the top 20% of height requires vertical air-terminals.
- Roof-mounted solar PV/water heaters/chillers need their own vertical air-terminals bonded to the mesh, plus Class I/II SPDs on DC (inverter/junction box) and AC (inverter output/mains) sides.
- Rooftop telecom towers: 2 extra down-conductors ≥150 mm² connecting tower to ring earth.
- **Table 7/8 (p. 1778–1780):** min cross-sections — air-termination/down-conductors 50 mm² (copper/aluminium/steel, various forms), earth rods 14–16 mm dia / 50–100 mm² conductor.
- **SPD selection (11.7.4):** Class I SPD Iimp ≥12.5 kA (10/350 µs) at line entrance if no risk analysis done; between N-PE, ≥50 kA (3-ph) / 25 kA (1-ph). Class II SPD In ≥5 kA at origin. Up ≤1.5 kV recommended for 240/415 V equipment (**Table 9**, p. 1785, gives full rated-impulse-voltage/overvoltage-category matrix).
- LPS testing: total resistance to earth must be ≤10 Ω (measured via test joint).
- **Fig. 35 + table (p. 1787–1789):** annual thunderstorm-days map and city-by-city data for India (risk-assessment input) — e.g. Delhi 30 days, Mumbai 26, Chennai 47, Kolkata 70, Guwahati-area highs like Dibrugarh 98.

## 12. Electrical Installations for Construction/Demolition Sites (p. 1792–1795)
- RCCB/RCD: ≤30 mA at socket outlets feeding plant; ≤100 mA for site-shed submains; portable RCDs push-button tested daily + performance-tested every 3 months; fixed RCDs performance-tested every 12 months (trip ≤6 s in both cases).
- Temporary switchboards: IP23 outdoors, door signage, ≥1.2 m clearance in front.
- Two dedicated earth pipe electrodes (4.2 m length, ≥2.5 m apart) minimum per source/generator.
- Construction wiring visual inspection interval: ≤6 weeks. Movable/portable plant test interval: 3 months; other plant: 6 months.

## 13. Protection of Human Beings from Electrical Hazards (p. 1795–1802)
- **30 mA RCCB/RCD** required at DB incomer for: residential, schools, hospitals, all bathroom circuits, sauna circuits, swimming pools/basins (24 V or less for lighting in contact with water), socket-outlets ≤20 A for ordinary use, mobile equipment ≤32 A outdoors, kitchen sockets.
- **100 mA RCCB** sufficient for other building types generally, and specifically for instant geysers (30 mA nuisance-trips).
- **300 mA RCD** at main DB recommended specifically against leakage-current fire risk (13.10) — distinct purpose from shock protection.
- Bathroom geyser switch: not accessible from wet area, located outside near entrance, ≥500 mm from plumbing connections.
- Shock physiology zones (Fig. 36, IEC time/current curve): Zone 3 = muscular contraction/reversible cardiac effects; Zone 4 = rising probability of ventricular fibrillation.

## Annexes
- **Annex A** (p. 1802–1808): electrical drawing symbols (switches, distribution boards, meters, wiring types, lamps, fans — 112 symbols).
- **Annex B** (p. 1809–1830): extracts of **CEA (Measures Relating to Safety and Electric Supply) Regulations, 2023** — the actual statutory clauses. Key ones for civil/building coordination:
  - **Reg 38** — buildings >15 m height (and airports/hospitals/hotels/stadiums/etc.): isolating device ≤1.7 m above ground; FRLS cables >15 m height, HFFR cables mandatory in airports/hospitals/hotels regardless of height; busbar trunking for floor distribution; no meter in staircase passage.
  - **Reg 39** — switchboard clearances (matches 5.3.6.7 above, stated as law here).
  - **Reg 43** — earthing (neutral earthing, equipotential bonding mandatory every building).
  - **Reg 46** — oil-filled substation rules: no substation in basement with >2000 L oil without draining; 4 h fire barrier; transformers ≥10 MVA / reactors ≥10 MVAR need automatic firefighting.
  - **Reg 60/62/63** — overhead line clearances from buildings/roads: LV lines 2.5 m vertical / 1.2 m horizontal from a building; HV >650 V–33 kV: 3.7 m vertical, 1.2–2.0 m horizontal (scaling +0.3 m per extra 33 kV band beyond 33 kV for both).
  - **Reg 119–128** — solar PV and EV charging station-specific safety (earthing, fencing, walkway widths, SPDs, testing/record-keeping — 7 years retention for EV charging records).
- **Annex C** (p. 1831): **substation/transformer room area table** by transformer capacity (160 kVA–3×1000 kVA) — e.g. 1×400 kVA → 16.5 m² transformer room / 93 m² total substation; 2×1000 kVA → 39 m² / 149 m².
- **Annex D** (p. 1832): **DG room area table** by genset capacity (25 kVA–2000 kVA) — e.g. 600 kVA → 110 m², 4.6 m clear height; 2000 kVA → 150 m², 6.5 m.
- **Annex E** (p. 1833–1844): blank inspection/commissioning checklist forms (HV cable, HV panel, transformer, MV/LV panel).
- **Annex F** (p. 1844–1847): completion certificate form template.
- **Annex G** (p. 1849): design/construction/inspection declaration templates.
- **List of Standards** (p. 1849–1858): ~82 numbered `[D-2(n)]` references (mostly IS/IEC standards) — resolve a specific in-text `[D-2(n)]` citation by searching this page range.

## Cross-references
- Part D Sec 1 (Lighting and Natural Ventilation) — for illumination/ventilation design coordination (4.1).
- Part D Sec 4 (Acoustics) — DG/transformer acoustic enclosures (4.2.1(aa), 4.3.3(c)).
- Part D Sec 6 (ICT Installations) — telecom/data cabling, FTTH (10.1).
- Part F (Fire and Life Safety) — throughout: substation fire compartments, oil-filled equipment barriers, emergency power to fire/life-safety systems (4.2.1(jj)), EV charging fire suppression, exhaust/smoke extraction.
- Part E (Plumbing Services) — electrical supply coordination for pumps etc. (mentioned generally, 4.1).
