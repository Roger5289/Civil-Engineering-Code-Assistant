---
status: active
project: civil-engineering
type: reference
---
# Part D — Section 3: Air-Conditioning, Heating and Mechanical Ventilation

Scope: planning, design, installation, testing, commissioning, handover, operation and maintenance of air-conditioning, heating and mechanical ventilation (HVAC) systems for buildings; also refrigeration for cold stores. **PDF pages 1861–2128** — pages 1861–1864 are the section's own Contents + Foreword; the actual clause text (clause 1 Scope) starts on **PDF page 1865**. Natural ventilation is not here — it lives in [[Part D Sec 1 - Lighting and Natural Ventilation]]. HVAC provisions for sustainable buildings sit in a separate BIS "Handbook on Sustainability in Buildings" (and the Energy Conservation and Sustainability Building Code, ECSBC 2024, is cross-referenced heavily for energy-efficiency numbers).

This is a very long section (19 numbered clauses, 44 tables). It reads more like an engineering design manual than a code — most of it is "should" guidance, with a smaller core of "shall" requirements and hard numbers. The design-critical, checkable content is flagged in **bold** below. Big lookup tables (city climate data, SET comfort tables, PECS device catalogue) are referenced by page, not transcribed — see [[NBC 2026]] "Notes on fidelity".

The running header on every page reads "PART D BUILDING SERVICES — SECTION 3 AIR CONDITIONING, HEATING AND MECHANICAL VENTILATION".

## 1 Scope · 2 Terminology (p. 1865–1870)

Clause 2 has 74 definitions plus refrigerant-specific terms. Worth knowing the ones that recur: **BMS** (building management system), **DOAS** (dedicated outdoor air system), **VRF** (variable refrigerant flow), **COP** (coefficient of performance — 4 variants), **GWP** (global warming potential, CO₂ = 1.0), **ODP** (ozone depletion potential, CFC-11 = 1.0), **SET** (standard effective temperature), fire damper / smoke damper / smoke barrier, stack effect, plenum, economizer.

## 3 Basis of Design (p. 1870–1904)

The design-brief clause. Key hard requirements:

- **Comfort sizing limits (clause 3.6):** size AC systems for **not more than 26 °C for cooling and not less than 18 °C for heating** at occupied level. **Relative humidity in occupied spaces should not fall below 30 percent nor exceed 70 percent.** **Air velocity should not exceed 1.5 m/s at the work plane.**
- **Adaptive thermal comfort:** recommended **SET range for Indian conditions is 23.5–25.5 °C at 80 percent acceptability**. Two paths — Path A (DBT/MRT model, see Part D Sec 1) and Path B (SET lookup, Tables 6 & 7).
- **Central AC plant room (3.4.1):** clear headroom below beam soffit **min 4.5 m for chillers ≥ 500 TR, min 3.6 m for smaller plants**. Anti-vibration supports or inertia bases. Floor loading per [[Part C Sec 1 - Loads and Load Effects]]. If in a basement: plan equipment-movement route, service ramp/hatch, fire egress and emergency battery-backup lighting for the operator.
- **AHU / package-unit rooms (3.4.2):** **fresh-air intake to exhaust-outlet separation 8 m preferably.** Exhaust from a dwelling unit must not enter another dwelling, a public corridor or a public stair. Fire-resistant door (see [[Part F - Fire and Life Safety]]), fire/smoke dampers at wall crossings, individual AHU per fire compartment desirable.
- **Duct supports (3.4.4):** designed for load + seismic; each straight run braced with ≥ 1 transverse + 1 longitudinal-transverse brace, spacing ≤ 12 m; false-ceiling supports independent of duct supports.
- **Cooling tower (3.4.5):** Range = entering − leaving water temp; Approach = leaving water temp − ambient wet-bulb temp. Floor area: natural draft 0.15–0.20 m²/3.516 kW, mechanical draft 0.07–0.10 m²/3.516 kW. Water losses: evaporation ~1 %, drift < 0.1 %, blow-down < 0.8 % of circulation. Make-up tank separate from drinking-water tank; treat water to hardness ≤ 50 ppm CaCO₃, treat if pH < 5.

Tables in clause 3 (referenced, not transcribed):
- **Table 1** (p. 1877) — acoustic comfort by building type: noise criterion, reverberation time, speech transmission index, Classes A (aspirational) / B (acceptable) / C (minimum acceptable).
- **Table 2** (p. 1879) — noise isolation criteria (Dw/NIC) between space types.
- **Table 3** (p. 1880–1889) — outdoor design conditions for 145 Indian cities (heating DB 99.6 %/99 %, cooling DB/MCWB 0.4/1/2 %, evaporation WB/MCDB). Use 1 %/99 % for normal comfort, 0.4 %/99.6 % for critical applications. Per IS 7896:2023.
- **Table 4 & 5** (p. 1891) — thermal comfort conditions and acceptable operative-temperature ranges.
- **Table 6** (p. 1893–1896) — calculated SET lookup grid.
- **Table 7 — Minimum Ventilation Rates in Breathing Zone** (p. 1897–1903, clause 3.6.1.2). The fresh-air table. Per occupancy category: people outdoor-air rate Rₚ (l/s·person) + area outdoor-air rate Rₐ (l/s·m²) + default occupant density + combined rate + air class (1–4). Must be used with its notes. Examples: office space Rₚ 2.5 / Rₐ 0.3; classrooms age 9+ Rₚ 5 / Rₐ 0.6; auditorium seating Rₚ 2.5 / Rₐ 0.3. Dwelling-unit default occupancy = 2 persons (studio/1BR) + 1 per extra bedroom; dwelling air never recirculated to other spaces.
- **Table 8 — Threshold Values for IAQ Pollutants** (p. 1904, clause 3.6.2), Classes A/B/C: CO₂ ambient +350 / +500 / +700 ppm; PM2.5 < 15 / < 25 / < 25 µg/m³; PM10 < 50 / < 100 / < 100; TVOC < 200 / < 400 / < 500 µg/m³; CO < 2 / < 9 / < 9 ppm (plus O₃, CH₂O, SO₂, NO₂).

## 4 HVAC System Types (p. 1904–1915)

- **Table 9** (p. 1906–1908) — HVAC system analysis & selection matrix comparing fixed-speed unitary / variable-speed unitary / VRF / central across 16 characteristics. A selection tool.
- **Centralized systems usually more cost-effective when total building load exceeds 350 kW (~100 TR).**
- Window ACs (4.1.1): residences, office cabins where rigid comfort not needed; not for clean rooms or high-fresh-air applications.
- Split ACs (4.1.2): rated at 35 °C ambient, derate above; for units up to ~10 500 W (~3 TR) horizontal indoor-outdoor distance should not exceed 10 m, total per manufacturer (generally max 30 m); not for precision AC, clean rooms, high occupancy.
- Ducted split / packaged DX (4.1.3): not where duct length > 30 m, vertical condenser distance > ~20 m (H + V sum within 25 m), or for operation theatres (100 % fresh air).
- VRF (4.1.4): DX multi-split, 2-pipe heat pump vs 3-pipe (simultaneous heat + cool with heat recovery); TFA-AHU for fresh air.
- Liquid chilling (4.1.5): prefer water-cooled where water available. Compressor part-load limits — centrifugal ≥ 40 % (surge), screw ~20 % (up to ~1400 kW / 400 TR), scroll up to ~425 kW, reciprocating nearly phased out for comfort AC (still used for cold storage).
- Vapour absorption/adsorption (4.2): LiBr/water; best where waste heat is available; solar-assisted possible.

## 5 Refrigerants (p. 1915–1924)

- **Table 10** (p. 1917) — safety group: toxicity (A lower / B higher) × flammability (1 none / 2L lower / 2 flammable / 3 higher) → A1, A2L, A2, A3 / B1, B2L, B2, B3.
- **Table 11** (p. 1917–1918) — ~24 common refrigerants with safety group, RCL (refrigerant concentration limit, g/m³) and LFL. e.g. R32 A2L RCL 77; R290 A3 RCL 9.5; R410A A1 RCL 420; R744 (CO₂) A1 RCL 72.
- **Table 12** (p. 1919–1920) — access categories: A general/least-restrictive (hospitals, prisons, theatres, supermarkets, schools, hotels, dwellings, restaurants, car parks), B supervised (offices, labs, general manufacturing), C authorised/most-restrictive (manufacturing, cold stores, plant rooms).
- **Refrigerant charge limits:** per IS 16678 except — institutional occupancy: safety factor 0.5 (50 % of calculated charge); residential: listed self-contained systems limited to **3 kg**; commercial: limited to **10 kg**.
- **High-probability direct systems for human comfort shall only use A1 and A2L refrigerants (5.10.5).**
- Do not mix refrigerants of different designations. Venting to atmosphere strictly prohibited; only technicians certified under Ozone Cell Regulations may handle refrigerant. India phase-down schedule: HCFCs prohibited in new RAC units after 1 Jan 2025; Kigali HFC phase-down 2032 → 2047.
- TEWI and LCCP formulas given for lifetime greenhouse impact.

## 6 Low Energy Cooling (p. 1924–1938)

- Evaporative air coolers: best in arid/semi-arid climates; space cooling needs **20–40 air changes per hour**; cooling only (no heating/dehumidification); needs potable-quality water.
- **Radiant cooling/heating (6.2):** only counts as "radiant" if **more than 50 percent of heat transfer is radiative**. Separate air system for ventilation + latent load. **No condensation allowed — radiant surface temperature min 2 °C above indoor dew point.** Water typically 15–20 °C. Types: RCP panels / TABS (thermally activated building system) / ESC (embedded surface cooling).
- Structural cooling (6.3): cooled water 15–30 °C in piping embedded in the structure, flushes solar heat from thermal mass; min water temp 15 °C for air-conditioned areas.
- Geothermal / ground-source heat pumps (6.4): 3–6 units of heat per unit of electricity; ground loop life 50+ years.
- Solar thermal cooling (6.5): absorption (VAM single/double/triple effect) or desiccant; ~0.4–0.6 kW/ton vs 1–1.4 kW/ton conventional.
- **Table 13** (p. 1930–1938) — Personal Environmental Control Systems (PECS) device catalogue: warmed seats, foot heaters, palm warmers, cooled garments, desk/ceiling fans, ventilated seats/garments etc, each with operating temperature ranges and air-velocity limits. Referenced by page.

## 7 District Cooling Systems (p. 1938–1949)

- **District cooling shall use recycled treated sewage effluent as cooling-tower make-up water.**
- **All new plants ≥ 10 000 TR shall include a thermal energy storage (TES) system.** Cluster developments with cumulative cooling demand > 5 000 TR should consider a district cooling system if feasible.
- Distribution network: carbon/mild-steel pipes with protective coating, **design life min 40 years**. Default design conditions — chilled water supply at plant 5 ± 1 °C, at consumer 6 ± 1 °C; return at consumer 15 ± 1 °C, at plant 14 ± 1 °C; **network design pressure 5–15 bar(g)**.
- Sizing: **system delta-T typically 8–11 °C**; **max flow velocity generally ≤ 2.5–3.0 m/s** (water hammer).
- **DC chiller plant efficiency shall not be less than 0.85 input kW per TR (ikW/TR).**
- Hydrostatic test at **1.5 × design operating pressure**. BTU meters per consumer, calibrated annually.
- **Table 14** benefits of DCS; **Table 15** (p. 1943) factors influencing DCS implementation; **Table 16** (p. 1947) recommended DCS performance benchmarks (kW/TR-h, water consumption 8 l/TR-h city / 11 l/TR-h recycled).
- Business model: Cooling-as-a-Service (CaaS) — connection charge + contract-capacity (availability) charge + consumption charge.

## 8 Supply Air Ducts and Return Air Ducts (p. 1949–1954)

- Rectangular duct **aspect ratio (height : width) kept within 1 : 4** for aerodynamics.
- **Table 17** (p. 1949) — pressure classification: low-pressure duct P ≤ +500 Pa (limits +1000 / −750); medium +500 < P ≤ +1000 (±1500); high +1000 < P ≤ +2500 (+3000 / −2500).
- **Table 18** (p. 1950) — recommended max duct velocities by application, noise-controlled vs friction-controlled, main vs branch, supply vs return (m/s). e.g. residences main supply 3 (noise) / 5 (friction); general offices 8/10/8/8/6; theatres & auditoriums 4/7/6/5/4; industrial 13/15/9/11/8.
- Duct construction/installation per IS 655:2006.
- **Occupied zone = floor level to 1.8 m above floor.** Air-distribution methods: fully mixed / fully stratified (displacement) / partially mixed (UFAD) / unidirectional (laminar, clean → dirty) / personalized (task/ambient).
  - Fully mixed (8.1.1): ΔT supply-to-room ~11–12 °C cooling, **≤ 8–9 °C for overhead heating**; SA outlet velocity 3.5–5.0 m/s; **resultant occupied-zone velocity 0.2–0.25 m/s cooling, ≤ 0.15 m/s heating**.
  - Fully stratified (8.1.2): ΔT 3–6 °C; supplementary cooling where internal gain > 120 W/m²; **SA outlets not closer than 1 m to any occupant**; not combined with mixed systems.
  - Partially mixed / UFAD (8.1.3): swirl-type outlets; **SA temp in access-floor cavity ≥ 16 °C** (condensation/fungal risk); not combined with mixed systems.
- **Tables 19–21** (p. 1954–1957) — ventilation effectiveness (Ez) by system, recommended SA-outlet selection, return-air-inlet face velocities (above occupied zone > 4 m/s; in zone not near seats 3–4; near seats 2–3; door/wall louvers 1–1.5).
- **System balancing (8.2): balance each space to within ± 5 percent of design** (note clause 17.6.1 later says ± 10 % for air systems — the tighter ± 5 % here is for the measurement method).
- VAV (8.4): straight inlet ≥ 3 duct diameters; **inlet velocity 2–12 m/s**; reheat discharge ≤ 8 °C above zone.
- Chilled/thermal beams (8.5): supply water at or above room dew point (no condensation).
- Air curtains (8.6): cover/overlap the full opening, **min 2 m/s projection at target surface**.

## 9 Air Filtration and Alternate Air Cleaning Methods (p. 1959–1965)

- Continuous IAQ monitoring: CO₂, TVOC, PM2.5, ozone in all regularly occupiable areas; sampling ≥ once per 5 min, 24-hour basis; missing data counts as an exceedance.
- **Breathing zone = between 1.1 m and 1.7 m above finished floor.** Sensors ≥ 0.9 m from exits/windows/AC vents. **General office/common areas: at least one device per 450 m² floor area.** Enclosed cabins/meeting rooms occupied ≥ 50 % of working hours get a dedicated device.
- Calibration: PM2.5 & TVOC sensors annually; CO₂ (auto-baseline-correction) and thermal-comfort sensors every 3 years.
- **Tables 22 & 23** (p. 1960–1962) — required sensor range/accuracy/resolution for continuous and periodic monitoring. Periodic monitoring (CO, SOx, NOx, HCHO) at least every 6 months by NABL labs.
- **Table 24** (p. 1962) — air-filter classification by particulate-matter efficiency (per IS 17570 / ISO 16890): ISO Coarse / ISO ePM10 / ISO ePM2.5 / ISO ePM1, each > 50 % of the named fraction; reported as ISO ePMx (y %).
- **Table 25** (p. 1963) — high-efficiency filters (per IS 16753 / ISO 29463): ISO 15E to ISO 75U; H group = HEPA (≥ 99.95 % at MPPS), U group = ULPA (≥ 99.999 %).
- Alternate cleaning: ESP (watch ozone; safety interlocks; upstream of cooling coils), UVGI (**occupied-zone UV intensity < 0.002 W/m²** to stay under 60 J/m² over 8 h; out of line of sight; "UVGI installed inside" stickers), PCO, PHI, bipolar/plasma ionization.

## 10 Other Components of Central HVAC System (p. 1965–1978)

- **Cooling tower (10.1):** raised **0.45–1.25 m above the mounting surface** (some text: pillars min 1 m — verify p. 1966–1968 before use); cool condenser water to within 2–3 °C of ambient wet-bulb (modern towers approach as low as 1 °C). **Table 26** (p. 1967) — approach & minimum efficiency (0.35 kW/LPS). Structural: mount on 4–6 RCC pillars, dynamic load transferred to building columns via epoxy-coated MS I-sections with vibration isolation pads; terrace install in consultation with the structural consultant. Post-install performance test: measured capability ≥ 95 % of manufacturer's curve. Legionella risk at ground-level installs — keep the public away.
- **Chilled/condenser water pumps (10.3):** radial-flow centrifugal; mono-block up to 7.5 kW, above that **IE3+ high-efficiency motors**; split-case horizontal for large duties. Select within **5 percent of the best efficiency point (BEP)**. NPSH available > required (cavitation). One pump per base/concrete block.
- **AHU (10.4):** per IS 18794:2024, third-party certified. Fans with motor power > 0.37 kW → **mechanical efficiency ≥ 65 %, motor IE3+** (or ESCBC, whichever stricter); fans with shaft power ≥ 2.5 kW → **fan energy index (FEI) > 1.1**. Reheat strongly discouraged unless recovered energy. **All hospitality and healthcare occupancies with energy recovery → min 60 percent recovery effectiveness at design.** Heat wheel: OACF 0.9–1.0, **EATR > 5 percent not acceptable**. Exhaust-air damper must never admit outdoor air.
- **AHU installation (10.5):** floor-mounted on precast PCC blocks (4–6 × 0.20 m cubes up to 10 000 m³/h; 6+ × 0.30 m cubes above); floor trap + sloped floor + U-trap on condensate drain; rubber/spring vibration isolators.
- **Thermal insulation (10.6):** fire-resistant, low-smoke/toxicity, non-hygroscopic; vapour seal on chilled-water pipes. Materials: closed-cell elastomeric foam, EPS/XPS, phenolic foam; fire rating Class 0 (fire propagation) + Class 1 (surface spread of flame). **Duct insulation must be anti-microbial; PUF/polyurethane shall not be used** on ducts. Acoustic duct lining: 25 mm resin-bonded fibreglass at 48 kg/m³ + 0.5 mm perforated aluminium (20–40 % perforation). Equipment-room acoustic lining leaves a 610 mm gap above floor for flood protection.
- **TES for critical facilities (10.8):** pressurised vertical cylindrical all-welded carbon-steel vessels (per ASME Section VIII Div 1) with radial disk diffusers to maintain stratification.

## 11 Heating (p. 1978–1982)

- Heating-equipment efficiency never exceeds 100 %; a heat pump's heating-mode COP exceeds its cooling-mode COP.
- Heat pumps (air-air, air-water, water-water), ground-source, reverse-cycle systems.
- Solar water heating: auxiliary backup activates below ~55 °C set point; heat-pump backup recommended.
- Solar air heating: once-through (fresh air heated to ~60–65 °C, space kept 18–22 °C) or recirculating.
- **Electric heating is highly energy-consuming — avoid to the maximum extent possible.** Where used, provide a manual-reset temperature-sensitive trip for fire safety.

## 12 Building Typology Related Considerations (p. 1982–2008)

Guidance for residential / office / campus / hospitality / healthcare / underground metro / airport / shopping complex / industrial / tall buildings. Common: north-south orientation preferred; **perimeter zone ≈ 4–6 m in from the external wall** (wide load swings, needs both summer cooling and winter heating); glass selected on SHGC / U-value / VLT (ECSBC 2024).

- **Hospitality (12.4):** each guest room/zone gets **at least one thermostat settable 20–30 °C**, operating both cooling and heating; adjustable dead band including a 12 °C setting between cooling and heating where auto-changeover is provided; thermostat on an inside wall.
- **Campus (12.3):** mixed-use campuses should consider district cooling.
- **Healthcare (12.5)** — the substantive typology:
  - Pressure: **negative in airborne-infection-isolation (AII) rooms; positive in operating theatres and protective-environment (PE) rooms.**
  - **Table 27** (p. 1991–1992) — HVAC design parameters by functional space: temperature, RH, minimum total air changes per hour, minimum outdoor ACH, pressure relation, exhaust-to-outdoors. Key rows:
    | Space | Temp °C | RH % | Total ACH | Outdoor ACH | Pressure |
    |---|---|---|---|---|---|
    | Operating theatres | 20–24 | 20–60 | 20 | 4 | Positive |
    | Cath labs / X-ray | 21–24 | ≤ 60 | 15 | 3 | Positive |
    | Delivery rooms | 20–24 | 20–60 | 20 | 4 | Positive |
    | Recovery / ICU / patient rooms | 21–24 | ≤ 60 | 6 | 2 | Equal |
    | Endoscopy / bronchoscopy | 20–23 | ≤ 60 | 12 | 2 | Negative |
    | Protective environment rooms | 21–24 | ≤ 60 | 12 | 2 | Positive |
    | Isolation (infectious disease) | 21–24 | ≤ 60 | 12 | 2 | Negative, exhausted to outdoors |
    | Toilets | – | – | 10 | – | Negative, exhausted |
    | Corridors | – | – | 2 | 2 | Negative |
    | Biochem/serology labs, pharmacy | 22–26 | ≤ 60 | 6 | 2 | Positive |
  - **Table 28** (p. 1992–1993) — minimum filter efficiency by category: Category 1 (orthopaedic/BMT/organ-transplant OTs, PE rooms, burns) = ISO Coarse 60 % + ISO ePM2.5 80 % + HEPA at outlets; Category 2 (general OT/delivery/ICU) = ISO Coarse 60 % + ISO ePM2.5 80 %; Categories 3–5 = ISO Coarse 60 % only.
  - Air distribution: VAV for critical areas (maintain pressure + minimum ventilation at minimum flow); coil face velocity 1.27–1.52 m/s; no evaporative pan humidifiers; **no fibrous acoustic duct lining in critical spaces** (external insulation only); redundant plenum fans; UVGI recommended in healthcare AHUs.
  - **Outside-air intakes ≥ 8 m from exhaust stacks / cooling tower / pollution source; intake bottom ≥ 2 m above ground and ≥ 1 m above roof terrace. Exhaust outlets ≥ 3 m above ground.** Supply near ceiling, return/exhaust near floor.
  - OT laminar flow (orthopaedic/cardiac): unidirectional vertical, **max velocity 0.13–0.18 m/s**; laminar grid extends **min 0.45 m beyond the operating-table footprint on all sides**; min 2 exhaust grilles at opposite corners **~0.2 m above finished floor**.
  - **AII rooms: minimum negative pressure 2.5 Pa** with respect to surroundings, all air exhausted to outdoors via HEPA. **PE rooms (bone-marrow / organ transplant): positive 2.5 Pa.** Pressure differentials of OT/PE/AII rooms verified and recorded semi-annually.
- **Underground metro stations (12.6):** design condition **platform/concourse 27 °C at 55 percent RH**; platform screen doors (full/half height); open mode (100 % outside air, "economiser cycle") vs closed mode; over-track and under-platform exhaust; full-height PSD needs separate compulsory smoke-extraction ducts and fans; fireman's and emergency staircase pressurisation per Part F.
- **Tall buildings (12.10):** **> 100 m = tall, > 300 m = super-tall, > 600 m = mega-tall.** Facade designed to limit solar gain to 10–20 % of incident radiation. **Facade air-leakage test of the completed building — recommended ≤ 2.0 l/s·m² at 75 Pa** (per IECC / ASHRAE 90.1; alternative 9.0 l/s·m²). Climate data at elevation: T = Tg − 0.00649·h. Neutral pressure level h = H / (1 + (A₁/A₂)²·Tᵢ/T₀). Loads calculated in ~100 m sections. Water piping zoned vertically with pressure breaks + heat exchangers + tertiary pumps; steel Sch 40 up to 250 mm dia, ≥ 300 mm → 9.5 mm wall.

## 13 Special Places in Buildings (p. 2008–2027)

- **Cleanroom (13.1):** surroundings less pressured than the cleanroom; airlocks + door interlocks; coving at all corners; separate M/F change rooms in series.
  - **Table 29** (p. 2009) — ISO 14644-1 airborne particulate cleanliness classes ISO 1–9 (max particle concentration at ≥ 0.1/0.2/0.3/0.5/1/5 µm).
  - **Table 30** (p. 2010) — legacy class meanings (Class 1 / 10 / 100 / 1 000 / 10 000 / 100 000).
  - **Table 31** (p. 2010) — air velocities and air changes: ISO 8 = 5–48 ACH, ISO 7 = 60–90, ISO 6 = 150–240, ISO 5 = 240–480, ISO 4 = 300–540, ISO 3 = 360–540.
  - **Table 32** (p. 2011) — filter classes H10–H14 (HEPA) and U15–U17 (ULPA).
  - **Table 33** (p. 2011) — test schedule: particle-count compliance every 6 months (≤ ISO 5) / 12 months (> ISO 5); airflow and pressure difference every 12 months; filter leakage / recovery / containment leakage every 24 months.
- **Cold stores (13.2):** food-temperature thermometer accurate to ± 0.5 °C; insulation panels per IS 661; prefer natural/low-GWP refrigerants (ammonia, CO₂, hydrocarbons).
  - **Safety (13.2.6):** UPS-powered audio alarm outside the room with a switch reachable inside; emergency exits openable from the inside even when locked from outside; rooms > 25 m → emergency doors at both ends with UPS-lit exit signs.
  - **Ammonia:** flammable 15–28 % by volume with an ignition source (582 °C) → explosion risk; emergency ventilation / dilution required; self-contained breathing apparatus + protective clothing above 50 ppm. GWP and ODP both zero. Per IS 17773.
  - Indicative storage ranges (13.2.7): horticulture +2 to +8 °C; hotels/restaurants +2 to +6; pharma +8 to −25; dairy +4 to −25; ice cream −20 to −25; ripening +12 to +20; controlled atmosphere +1 to +3. RH mostly 85–90 %+.
- **Supermarket refrigeration (13.3):** rack systems or individual condensing units; air-cooled (small) vs water-cooled (malls / basements without fresh-air access).
- **Data centre (13.4):**
  - Location: seismic zone map (IS 1893 Part 1); two independent power feeds from different substations; ≥ 2 diverse fibre paths; ≥ 10 years of historical weather data.
  - Redundancy: **N+1 for chillers** (2N for critical / hot climates), **N+1 for precision AHUs**, redundant A+B power feeds, N+1 cooling towers, redundant pumps with auto switchover.
  - **Inside conditions: temperature 18–27 °C** (prefer nearer 27 °C for efficiency); **RH 8–60 %** (upper limit may drop to 50 % or 35 % with corrosive gases present).
  - **Air distribution: hot/cold aisle containment mandatory; bypass airflow ideally below 5 percent; maintain a slight positive pressure of 2.5–5 Pa** between the data centre and surroundings; airlocks at entrances; CFD analysis in design.
  - Commissioning: independent commissioning agent; FAT → SAT → integrated system testing (normal / peak / simulated failure).
  - Electrical safety: earthing per IS 3043; **Type F RCD for 1-phase VFD equipment, Type B RCD for 3-phase VFD**; lightning protection per IS/IEC 62305-4 + surge protection devices.
  - Section 3's general AHU provisions (clause 10.4) do **not** apply to data-centre AHUs.

## 14 Ventilation Systems (p. 2027–2044)

Scope restricted to **mechanical** ventilation (natural ventilation is in Part D Sec 1).

- **Fan selection for new buildings (14.1.2.2): axial fans ≥ 2.0 kW shaft power → fan energy index (FEI) ≥ 1.00; centrifugal and mixed-flow fans ≥ 2.0 kW → FEI ≥ 1.10; at all duty points.** Dust-laden / contaminated air (industrial or kitchen exhaust) → keep the drive train outside the air stream. High-temperature air (smoke ventilation) → high-temperature-rated fan.
- **Table 34** (p. 2028–2029) — fan-type-vs-application matrix.
- Industrial ventilation (14.2): heat-control flow rate Qs (m³/h) = 3.462 × Hs (kcal/h) / ΔT (°C). Dilution vs local exhaust — decision by hazard level, particle size, source type, worker proximity. **Table 35** (p. 2033) — capture velocities (still air 0.25–0.5 m/s up to grinding/blasting 2.5–10 m/s). **Table 36** (p. 2034) — exhaust duct velocities (vapours/gases/smoke 5–10 m/s up to heavy moist dust 22.5+).
- **Underground car park ventilation (14.3):**
  - **CO maintained within 40 mg/m³ (35 ppm) for 1-hour exposure, max 29 mg/m³ (25 ppm) for 8-hour exposure.**
  - **Minimum 6 ACH** for enclosed underground car parks without natural ventilation; each compartment ventilated independently at ≥ 6 ACH.
  - Fans used for CO ventilation also serve fire smoke ventilation → rated for high temperature per Part F. Demand-control ventilation on CO level.
  - **CO sensors: max distance from any corner to the nearest sensor < 25 m; coverage ~400 m² per sensor; mounted 0.9–1.8 m above floor** (or just above 1.8 m to avoid vandalism).
- **Commercial kitchen ventilation (14.4):**
  - Type I hoods (grease + smoke + steam + heat, with grease filters/baffles + fire suppression) for ranges, fryers, broilers, griddles. Type II hoods (steam + heat only) for ovens, steamers, dishwashers.
  - **Table 37** (p. 2036) — hood exhaust flow rates by appliance category (light/medium/heavy/extra-heavy) and hood type, litres/s per linear metre. e.g. wall-mounted canopy: 309 / 463 / 618 / 850 l/s per m.
  - **Min 150 mm overhang on all open sides** of canopy hoods; heavy-duty appliances in the middle of a line; mount the hood as low as practical.
  - Exhaust ducts: grease-tight, no traps; **min 16 gauge mild steel or 18 gauge stainless**; all joints fully welded; lead directly to exterior, not interconnected with other ductwork; **2 % slope for horizontal runs < 23 m, 8 % for runs > 23 m**; **max velocity ~12.5 m/s, min 2.5 m/s**; **clean so the grease film stays ≤ 180 microns**; fire per Part F.
  - Terminations: **rooftop discharge min 4 m above the roof surface**; grease drained to a closed container.
  - Make-up air: **100 percent replacement with clean outside air**; kitchen slightly negative to adjoining spaces, slightly positive to outside if on an exterior wall.
- **Laboratory ventilation (14.5):**
  - Chemical labs: **minimum 6 ACH**; fume-hood face velocity sufficient to keep contaminant escape ≤ 0.01 ppm (verified by tracer-gas test); **negative pressure** vs corridors; **no openable windows**; exhaust duct velocity 5–10 m/s; exhaust duct not internally insulated (external only, STC/Rw ≥ 50 dB).
  - Biological labs (BSL3): **minimum 6 ACH at all times**; **negative pressure ≥ 12.5 Pa** below adjoining areas with monitoring and alarms; dedicated (not shared) exhaust with VFD + standby fan; stainless-steel welded ductwork; HEPA (bag-in/bag-out) close to containment.
  - Animal labs (conventional): **10–15 outside ACH for ABSL 1 & 2** (higher for ABSL 3), once-through, HEPA on supply and exhaust; airflow clean corridor → animal room → service corridor.
- **Tunnel ventilation (14.6, metro):** congested-operation design condition ~50 °C stratified tunnel air; components **rated min 250 °C for 1 hour** (increase per requirements); SCADA min SIL-2 with redundant comms/processor/power; simulation via SES / IDA Tunnel / CFD.

## 15 Automation and Controls (p. 2044–2054)

BMS integrates all MEP equipment across three architecture levels (unit/equipment, system/automation, management). Life-safety systems stay stand-alone but are monitored from the BMS; fire-alarm system and BMS seamlessly integrated.

- **Table 38** (p. 2046–2048, clauses 15.1.6 / 15.2.1 / 15.2.3) — controls-compliance requirement matrix for significant components (HVAC, lighting, electrical & vertical transportation, water management) at equipment and system level across three building tiers (base / energy-intensive / critical). Cross-references ECSBC Chapter 13.
- Open protocols: BACnet, Modbus, MQTT, OPC, M-Bus, Zigbee, Z-Wave, DLMS, GSM/GPRS, Wi-Fi. **Default usernames and passwords shall not be retained.** Medium buildings min WPA/WPA2. Cyber security addressed at all levels.
- Installation (15.7): field devices per manufacturer manual; enclosure panels electrically and IP rated for ambient; UPS power for controllers; screened/twisted/shielded control cables; BMS PC/server in an air-conditioned room; earthing per SP 30 (National Electrical Code) and [[Part D Sec 2 - Electrical and Allied Installations]].

## 16 Hydronic Piping Systems (p. 2054–2062)

- Materials: steel (high pressure), copper (refrigerant, DHW, hydronic heating), PVC (low-pressure drainage/vent/condensate), PEX (radiant), HDPE (buried/geothermal). Prefer long-radius elbows; **45° over 90° elbows** for offsets.
- Connections: threaded for **low pressure up to 6.9 kPa**; welded for high pressure and large diameter.
- Valves: gate (on/off, isolation), globe (throttling), ball, butterfly (large dia on/off), check, balancing, control. **Pressure-independent control valve (PICV)** recommended to replace balancing + control valve; **triple-duty valve** (check + balancing + isolation) recommended for chilled/hot-water systems.
- **Refrigerant piping (16.2):**
  - Keep pressure drop ≤ equivalent of 1.10 °C (~1.3–1.9 kPa suction line, ~4.0–6.0 kPa hot-gas and liquid lines) — verify against the refrigerant P-T chart.
  - **Oil return: refrigerant velocity in suction and hot-gas lines ≥ 3.8 m/s horizontal, ≥ 7.6 m/s vertical (upward).** Horizontal suction/hot-gas lines pitched down in the flow direction, gradient 1 : 200. U-trap at the bottom + inverted U-trap at the top of vertical risers; **U-trap every 3.5 m** where an upward riser exceeds 3.5 m. **Liquid-line velocity ≤ 1.5 m/s** (liquid hammer).
  - Materials: steel, copper, aluminium, copper-alloy tubes, rated for pressure. **Pressure test at 1.5 × operating high pressure, then vacuum to 500 microns held 4–6 hours.** Suction line insulated; hot-gas line insulated only where a burn risk exists; liquid line not insulated (unless a reversible heat/cool cycle → insulate all).

## 17 Installation and Commissioning of HVAC Systems / Equipment (p. 2062–2098)

Objectives: meet owner's project requirements (OPR), energy efficiency, reliability, safety, timeliness, optimum life-cycle cost, minimum noise & vibration.

**General planning (17.2):** equipment room close to the served area with good ventilation and natural light; large installs get a separate utility block + service tunnel; **condensate is never left in the open** (to drainage, or recovery/reuse for large installs); **openings in structural elements (beam/slab) only with the structural engineer's approval**; foundations structurally designed with epoxy-coated angle nosing, inertia blocks and seismic restraints where specified; duct terminated on a roof gets a swan's neck; equipment-room doors are double-leaf/shutter, open outward, with a sill against water ingress, and fan-room doors are airtight.

**Equipment-specific:**
- Window AC (17.3.1): **6–10 mm slope for condensate drainage.**
- Split AC (17.3.2): **copper refrigerant pipe, min bend radius 10 mm**; ODU on a flat firm surface + vibration isolators, not in direct sun, multiple ODUs not facing each other. **Pressure test 21 × 10⁴ kg/m² high side, 10 × 10⁴ kg/m² (or 1.5 × max operating) low side, min 6 h; then vacuum 500 microns Hg held 6 h before charging.**
- VRF (17.3.3): communication cable ≥ 300 mm from power cabling; ball valves for zoned isolation.
- Chiller (17.3.4): foundation transfers load to ground via beams/columns per the structural specialist, dynamic loading per IS 13301; plant-room floor-to-floor **3.6–4.5 m**; concrete foundation base **150–200 mm above floor**; electrical isolation ≤ 2 m from the chiller; air-cooled open installs → electrical enclosures IP 55+ per IS/IEC 60529. **Table 39** (p. 2070) — water quality limits (hardness, alkalinity, chloride, iron, silica, ammonia; pH 7.2–8.5 chilled/condenser, 6–8 make-up).
- Pumps (17.3.6): base frame on a concrete block + cork/rubber pads/AV mounts per IS 13301; one pump per base; alignment re-checked after piping; isolation valves both sides.
- Cooling tower (17.3.7): terrace load to beams/columns per the structural engineer; rests on hot-dip-galvanised MS I-sections per IS 4759; sump ≥ 300 mm above pump suction; basin leak-tested (held ≥ 2 h).
- AHU/HRU/FCU (17.3.8): **individual AHUs shall not serve more than one floor** (fire safety); exclusive AHU per fire compartment advisable, otherwise fire + smoke dampers on supply and return at floor/compartment crossings; not mounted above electrical or IT rooms.
- **Ducting (17.3.11):**
  - Duct-hanger upper attachment **safety factor 5**; vibration isolation min 6 mm between duct and angle supports; vertical ductwork supported at each floor; plenum access doors **450 mm × 450 mm**.
  - **Table 40** (p. 2075) — low-pressure (≤ 750 Pa) rectangular duct supports: larger side ≤ 1500 → 40×40×5 angle + 8 mm rod; 1501–2400 → 40×40×5 + 10 mm rod; ≥ 2401 → 65×65×5 + 12 mm rod. **Max spacing 2 400 mm** in all cases.
  - **Table 41** (p. 2075) — high-pressure (> 750 Pa): ≤ 1250 → 50×50×5 + 12 mm rod; 1251–2100 → 65×65×5 + 12 mm; ≥ 2101 → 75×75×5 + 15 mm. Max spacing 2 400 mm.
  - Sheet-metal ducts: galvanised iron, **min 180 GSM zinc coating**, lock-forming quality; lock-forming machines mandatory where project duct area > 600 m² or external static pressure > 250 Pa.
  - Flexible connection at fan/AHU: rubberised canvas, **100 mm long**, bonded and bolted.
  - **Dampers rated for 1.5 × the rated duct pressure class** (17.3.11.10); position indicator + locking device.
  - Fire / fire-smoke dampers at every fire-compartment barrier, in ducts, return-air passages and all floor crossings; access door each; motorised or fusible-link; factory sleeve at wall/floor crossings.
  - **No electrical heaters mounted inside ducts** (17.3.11.14).
  - VAV boxes factory-set to min airflow 10 % / max 110 % of design flow.
  - Fresh-air louvres: 1.6 mm × 100 mm wide extruded aluminium at **45° to vertical, min 60 percent net free opening**; 12 mm mesh bird screen; intermediate supports if length > 1 250 mm.
  - Kitchen exhaust ducting: 16 G MS CRCA, welded, access doors at 3 m intervals, sloped to the hood.
- Filters (17.3.12): stored in packing until upstream is cleaned; directional arrows to airflow; gasketed no-gap fit; DP gauge across filters; HEPA gasket side to frame; ESP "Caution – High Voltage Filters" sticker; UVGI lamps downstream of the cooling coil, ~300 mm from it; upper-zone UVGI units ≥ 2.2 m from floor.
- Piping install (17.3.13): weld per IS 10234; **chilled water on PUF/wooden gutties** (single for horizontal, double for vertical risers); condenser water on serrated rubber pads + U-clamps; auto-purge valves at the highest point of each loop; eccentric reducers; **hydraulic pressure test at 1.5 × working pressure for 24 h**; open pipe ends always kept closed.

**Vibration isolation & seismic protection (17.4):** isolation efficiency E = 100·[1 − 1/((fd/fn)² − 1)]. Seismic isolation of non-structural components (mechanical, electrical, fire protection, plumbing): components securely attached, life-safety equipment keeps functioning, and **critical applications keep operating** — healthcare facilities, airports, emergency response centres, critical defence installations, data centres. Position retention per IS 1946 Part 2.

**Painting & colour codes (17.5):** wire-brush clean + zinc chromate primer + finish, **DFT ≥ 250 microns**; **colour band 150 mm wide, spacing ≤ 4.0 m**; flow-direction arrows + lettering (HW / CHW / CDW / ST / CN). **Table 42** (p. 2092) — pipe colour code: cooling water sea green, chilled water sky blue, central heating dark blue, condensate drain black, vents white; belt guards black with yellow diagonal strips; machine/inertia bases charcoal grey.

**Testing & balancing (17.6):** **air system balanced to within ± 10 percent of design airflow** at fan discharge and all outlets, dampers locked after adjustment; water system by proportional (index/lowest-flow-ratio) balancing — PIBCV valves skip this and are set per manufacturer.

**Cleaning/flushing (17.7):** duct cleaned before commissioning; pipe flushed bypassing chiller/heat-exchanger tubes; **flushing velocity 1.0–1.25 m/s**; primary strainer mesh ≤ 3 mm; dynamic flushing in steps (primary ring → mains → floor horizontals, top floor down).

**Commissioning (17.8):** owner designates a commissioning authority (CxA — own team or independent agency), engaged for a minimum of one year from occupancy, responsible for resolving all non-conformances / warranty / seasonal issues. Flow: OPR → commissioning plan → basis of design → commissioning spec → design review → observe & test → system manual → conformance/NC resolution → training → commissioning report → post-commissioning operation (Fig. 40). Functional performance testing under low load / full load / varying ambient / power outage / distress / emergency. Recommend all individual loads > 15 kW monitored for energy management. Handover docs: systems manual, final commissioning report, as-built drawings, design calculations, spare-parts list, warranty records + escalation matrix, NC list with resolution, O&M manuals.

**HVAC safety (17.9):** follow the Indian Electricity Act and the AHJ's fire regulations; refrigerant is heavier than air (suffocation risk) — ventilate the plant room, store cylinders upright; pressure testing needs a work permit, barricading, calibrated gauges, air purged from water systems first, and a documented SOP.

## 18 Post Occupancy Operation and Maintenance (p. 2098–2116)

- Systems operations manual comprising the OPR + Current Facility Requirements (CFR), kept updated with every modification and its reasoning.
- **Minimum HVAC operator qualifications (18.1.6):** Engineer-in-Charge = degree/diploma in electrical/mechanical/HVAC + ≥ 5 years O&M experience; Supervisor = diploma + 3 years or ITI + 5 years; Technician = diploma + 1 year or ITI + 3 years; Operator = 10th/12th pass + a certificate course in refrigeration & air-conditioning from a recognised institute; Trainee = minimum 1 year supervised, not to operate systems alone.
- **Plant starting sequence (18.1.11):** mains on (check voltage) → AHU motors → condenser water pumps → cooling tower fan → chilled water pumps → compressor control switch → compressor motor. Stopping is the reverse.
- Maintenance schedules laid out day-to-day / weekly / monthly / quarterly / half-yearly / yearly (18.1.15). Yearly includes chiller oil sample lab test + replacement, condenser tube cleaning/de-scaling, vibration test of major equipment, IAQ test + duct cleaning.
- Predictive maintenance (18.2): vibration analysis, thermography, oil analysis, motor-current analysis, eddy-current, pressure; performance trending. Emergency management plan required (ISO 14001 EMS, ISO 45001 SMS).
- CMMS (18.3): asset mgmt, work-order mgmt, procurement/inventory, dashboard reporting; integrate with BAS/BMS; **52-week PPM planner** aligned with OEM manuals.
- **Energy monitoring (18.4):** main meters + **sub-metering for any application ≥ 10 percent of total building consumption** (chillers, pumps, cooling towers, AHUs, lighting, UPS). Annual HVAC health check by a professional HVAC engineer at peak load (summer). **Table 43** — maintenance classes A–E.
- **Benchmarking / M&V (18.5):** **overall HVAC system efficiency = overall HVAC consumption (kWh) / conditioned area (m²)**, measured monthly against a benchmark. Option 1 (retrofit isolation) / Option 2 (whole facility). **Table 44** — corrective measures.

## 19 Smoke Mitigation — Fire and Life Safety (p. 2116–2128)

Works alongside [[Part F - Fire and Life Safety]]. Three pressurisation scenarios: defend-in-place (1 door open), phased evacuation (3 doors open), assisted firefighting shaft (3 doors open).

- **Basement car park (19.1.1):**
  - Natural: each basement separately ventilated; **vents aggregate cross-section ≥ 2.5 percent of floor area**, spread evenly round the perimeter.
  - Mechanical: **12 ACPH in a fire / distress call** (normal per clause 3); fans in **120-minute fire-resisting rooms**; **smoke exhaust fans fire-rated 250 °C for 120 minutes**; jet-fan alternative needs power in a fire-safe zone, circuit-integrity cabling, CFD validation, and a smoke-gun test of at least one compartment; operates on sprinkler flow-switch + manual start-stop; supply air ≥ 5 m from any exhaust discharge. Stallboard/pavement lights marked "AIR INLET" / "SMOKE OUTLET". EV car parks: same.
- **Industrial (19.2):** where travel distance to an exit is ≥ 45 m, provide exit tunnels/passageways; **maximum travel to exit 65 m where smoke venting is provided.**
- **Smoke control of exits (19.3):**
  - **Pressurisation: staircases minimum 50 Pa; lobbies/corridors 25–30 Pa.** Enclosed staircase adjacent to a lobby (pressurised or not) = 50 Pa.
  - On emergency pressurisation: stop recirculation (all exhaust to atmosphere), stop supply to non-exit spaces.
  - Pressurised ↔ unpressurised areas segregated by a **120-minute fire-resistant wall.** Fresh-air intake for pressurisation **≥ 4 m from any exhaust outlet.**
  - Exit-access corridors (hospitality / healthcare / sleeping accommodation): **60-minute fire-resistant wall + 20-minute self-closing fire doors** (per IS 3614); smoke exhaust **min 12 ACPH** or pressurisation 25–30 Pa; smoke exhaust fans fire-rated 250 °C/120 min; exit-passageway doors **120-minute** rated.
  - Lift lobby: 25–30 Pa. Firefighting shaft (fire tower) = **120-minute** fire-resistance protected lobby + staircase + fireman's lift.
  - Hoistway: if there's no lift lobby at any level in AC buildings or flue-effect spaces → **hoistway pressurised at 50 Pa.**
  - **Buildings > 60 m: door-opening force limited to ≤ 133 N** to set the door leaf in motion.
- **Special occupancy (19.4):**
  - Atrium: **business occupancy 6 ACPH, hotels and assembly 8 ACPH** smoke extraction, for a height of 15 m from the top; fans 250 °C/120 min; makeup air below the smoke layer at **85–95 percent of the exhaust flow**, makeup air velocity **≤ 1.02 m/s** near the plume; keep the smoke layer **1 800 mm above the highest occupied floor** for 1.5 × egress time or 20 minutes, whichever is greater.
  - Commercial kitchens: flue through a compartment wall/floor encased in non-combustible construction with no damper; hood gaskets certified to 815.6 °C; hood steel ≥ 1.09 mm (SS ≥ 0.94 mm); grease filters ≥ 45° from horizontal, drip tray draining to a sealed metal container ≤ 3.8 litre; exhaust ducts carbon steel ≥ 1.37 mm (SS ≥ 1.09 mm); rooftop termination ≥ 3 m horizontal from adjacent buildings/property lines/air intakes, ≥ 1.5 m from combustible structure.
  - **Open parking structure definition (19.4.4): wall openings ≥ 0.4 m² per linear metre of exterior perimeter, distributed over ≥ 40 percent of the perimeter or two opposing sides; interior wall lines ≥ 20 percent open.** A stilt car park counts as open if any part is within 30 m of a permanent natural-ventilation opening and either 50 percent of the perimeter is open or ≥ 75 percent of the perimeter carries the 50 percent opening.
- **Ventilation for smoke mitigation (19.6):**
  - **Separate AHU per floor**; separate ducts per floor with no interconnection; separate AHU per compartment desirable. Shafts/ducts penetrating multiple floors → masonry with fire damper, or fire-rated ductwork with dampers at floor crossings, **120-minute** fire resistance. AHU filters non-combustible; AHU room holds no combustible storage.
  - Ductwork: not routed through exits / exit passageways / exit enclosures; exits and lift lobbies not used as return-air passages; **duct within a compartment min 30-minute fire resistance; a duct crossing an adjacent compartment/floor without fire dampers → 120-minute** fire-rated ductwork; non-combustible insulation only.
  - **Fire / fire-smoke dampers** at: the fire-separation wall; where ducts enter a vertical shaft; where ducts pass through floors; at the supply and return-air duct inlet of each compartment on every floor. Integrated with the fire-alarm panel, with manual operation available.
  - **Glass facade: openable fire-access panels on each floor, ≤ 10 m apart** (centre to centre) along the external wall; operable at **1.2–1.5 m from the floor**; panel size **≥ 1 000 mm × 1 000 mm**, opening outwards; marked "FIRE OPENABLE PANEL — OPEN IN CASE OF FIRE, DO NOT OBSTRUCT" in ≥ 25 mm letters.

## Cross-references found in this Section

- Natural ventilation, adaptive thermal comfort, climate zones → **[[Part D Sec 1 - Lighting and Natural Ventilation]]**
- Acoustics, sound insulation, noise limits, plant-room acoustic treatment → **[[Part D Sec 4 - Acoustics, Sound Insulation and Noise Control]]**
- Electrical installations, earthing, motors, switchgear, RCDs → **[[Part D Sec 2 - Electrical and Allied Installations]]** and SP 30 (National Electrical Code 2023)
- Floor loading, structural design of equipment foundations, seismic → **[[Part C Sec 1 - Loads and Load Effects]]** and Part C generally
- Fire resistance ratings, compartmentation, fire dampers, staircase pressurisation, travel distances, occupancy classification, fireman's lift → **[[Part F - Fire and Life Safety]]** (Section 3 clause 19 is the HVAC-side companion to Part F)
- Lifts, escalators, fireman's lift specifications → **[[Part D Sec 5 - Lifts, Escalators, Moving Walks and Power-Driven Parking]]**
- Sustainability, envelope U-value / SHGC / VLT, energy-efficiency numbers → "Handbook on Sustainability in Buildings" and ECSBC 2024 (external to this NBCS)
- Seismic zone map → IS 1893 (Part 1) : 2025
- Geotechnical service scope for large plant → IS 19235 : 2025 (via Part A)

## Topics for cross-index

Comfort temperature and humidity limits (26 °C cooling / 18 °C heating / RH 30–70 %) · fresh-air / outdoor-air ventilation rates by occupancy (Table 7) · IAQ pollutant thresholds and monitoring (CO₂, PM, TVOC, ozone) · breathing zone (1.1–1.7 m) and occupied zone (1.8 m) definitions · plant-room headroom (4.5 m / 3.6 m) · fresh-air-intake to exhaust separation (8 m) · duct velocities and pressure classes · duct support spacing (Tables 40, 41) · fire dampers and fire-rated ductwork (30 / 120 min) · smoke exhaust rates (12 ACPH basements & exit corridors, 6/8 ACPH atria) · staircase and lobby pressurisation (50 Pa / 25–30 Pa) · door-opening force (133 N over 60 m) · glass-facade fire-access panels · underground car park ventilation (6 ACH normal, 12 ACPH fire, CO limits) · open vs enclosed parking structure definition · commercial kitchen exhaust (hood flows, grease film 180 microns, duct gauges) · laboratory ventilation (6 ACH, fume-hood face velocity, negative pressure, BSL3 12.5 Pa) · healthcare space conditions and pressures (Tables 27, 28; AII/PE 2.5 Pa; OT laminar flow) · cleanroom classes and air changes (Tables 29–33) · cold-store safety and ammonia hazards · data-centre conditions (18–27 °C, RH 8–60 %, N+1 redundancy, 2.5–5 Pa positive) · tall-building thresholds (100 / 300 / 600 m) and facade leakage · refrigerant safety classification and charge limits (3 kg residential / 10 kg commercial) · refrigerant piping velocities and oil traps · fan energy index (FEI ≥ 1.00 axial / ≥ 1.10 centrifugal) · motor efficiency (IE3+) and AHU fan efficiency (65 %) · district cooling (10 000 TR TES trigger, 0.85 ikW/TR, 40-year pipe life) · commissioning authority (CxA) role · HVAC operator minimum qualifications · vibration isolation and seismic protection of non-structural components · pipe colour codes (Table 42) · testing pressures (1.5 × operating, vacuum 500 microns) · overall HVAC efficiency benchmark (kWh per conditioned m²).
