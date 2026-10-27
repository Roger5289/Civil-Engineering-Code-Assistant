---
status: active
project: civil-engineering
type: reference
---
# Part D — Section 5: Installation of Lifts, Escalators, Moving Walks and Power-Driven Parking Systems

Scope: planning, design, installation, operation, maintenance and inspection of lifts, escalators, moving walks and power-driven (mechanised) car parking systems. **PDF pages 2205–2458.** Split into three subsections:

- **5A — Lifts** (passenger, goods, hospital, automobile, service lifts, dumbwaiters). PDF 2205–2357.
- **5B — Escalators and Moving Walks.** PDF ~2364–2424.
- **5C — Power-Driven Parking Systems.** PDF ~2425–2458.

Read alongside [[Part F - Fire and Life Safety]] (fireman's lift, evacuation lift, escalator/parking fire requirements) and [[Part D Sec 2 - Electrical and Allied Installations]] (electrical work).

Checkable numbers are in **bold**. Big dimension/capacity tables are referenced by page.

## Subsection 5A — Lifts (PDF 2206–2357)

Covers planning, design, installation, operation, maintenance and inspection of passenger, goods, hospital/stretcher, automobile and service lifts plus dumbwaiters. 16 clauses + Annex A. Source read from a clean re-export of PDF pages 2206–2357 (`<local extracted text>\NBC 2026\NBC_2206-2357.pdf`) — the main fulltext file's copy of this subsection is corrupted (broken subset font), so re-verify any figure against that PDF, not the fulltext.

**Primary referenced standard: IS 17900 (Part 1):2022 "Lifts for the transport of persons and goods — Safety rules"** (replaces the old IS 14665 Part 1 for safety rules). Full standards list at the end of this subsection.

### 1–3 Scope, Terminology, General

- Installation per **Lifts Act and Rules** of the state (where in force); owner obtains Authority permission before and after installation and a **licence for public use**. Electrical work per **Electricity Act 2003 + CEA Regulations** and [[Part D Sec 2 - Electrical and Allied Installations]]. Fire per state fire acts and [[Part F - Fire and Life Safety]].
- **Selection criteria (clause 3.6):** intended use (load + speed for handling capacity / waiting time), system performance by building type, accessibility, environmental exposure, drive type (traction geared/gearless or hydraulic), civil constraints (machine room vs MRL), seismic strategy (protect / rescue-to-landing / both).
- Terminology (clause 2) is extensive — key definitions: **Evacuation Lift**, **Evacuation Exit Lobby (EEL)**, **Automatic Rescue Device (ARD)**, **MRL lift**, **Home Lift**, **Refuge Space** (bottom = pit, top = car roof), **Automobile Lift**, control types (VVVF/ACVVVF preferred), **PESSRAL** (programmable electronic safety systems), **Seismic Trigger Level / Seismic Mode**.
- **Energy efficiency (clause 3.8):** VVVF drives mandatory in practice (1- and 2-speed control **not recommended** for passenger lifts); car light + fan auto-off after no call for **≥ 90 s**; standby/sleep mode for at least one car of a bank off-peak; interconnected group control; LED car lighting; gearless machines; regenerative drives; motors ≥ **IE2**.

### 4 Planning and Design Guidelines (traffic analysis)

This is the design core for *how many lifts, what capacity, what speed*. It is a guideline, not a substitute for specialist traffic analysis; a badly-planned lift core cannot be fixed later.

- **Population:** ask owner/occupier first; else estimate from **net usable area (NUA)** (excludes circulation, structure, toilets/pantry/server/conference). **Table 1 — occupancy area per person in offices:** Premium 10 m² open / 12 m² cellular; Regular 8 / 10; Low-end 5 / 8; BPO 6–10 m².
- **Absenteeism:** office buildings only — reduce design population by **10 %–20 %** (never beyond 20 %). **Not applied** to residential, hotels or hospitals.
- **Quantity of service (Table 2, offices):** target 5-min handling capacity as % of population — multi-tenancy **10–15 %**, single-tenancy **15–25 %**.
- **Quality of service — interval (Table 3, offices):** Excellent < 25 s · Very good 25–<30 · Good 30–<35 · Fair 35–<40 · Poor 40–<45 · Unsatisfactory ≥ 45. Average waiting time ≈ **75–85 % of interval** at ~80 % car occupancy; beyond 80 % loading AWT rises exponentially. **Table 4:** AWT premium < 25 s, regular 25–35 s.
- **Round trip time (clause 4.2.5):** classical up-peak method; RTT = 2·H·tv + (S+1)(T − tv) + 2·P·tp, with separate down-peak and mid-day forms and a zoning/shuttle form for sky-lobby buildings. Interval INT = RTT / L (L = lifts in the group). 5-min handling capacity HC = 300·P·L·100 / (RTT·Population). Average car load **P = 0.8 × max actual car capacity**. Simulation must run **≥ 120 min covering ≥ 3 intervals of 5 min**.
- **Lift speed — Table 11** (avg floor height 3.0 m): up to 6 floors **0.6–1.0 m/s** · 7–15 **1.0–1.5** · 16–20 **1.5–1.75** · 21–30 **1.75–2.5** · 31–45 **3.0–4.0** · 46–60 **4.0–6.0** · above 60 **6.0 m/s and above**. Office avg floor height taken as 4.2 m. **Practical maximum passenger-lift speed = 10 m/s** (ear-pressure comfort, clause 11.1).
- **Nominal travel time:** offices/commercial/hotels (Table 5) Excellent ≤ 25 s / Good 25–35 / Satisfactory 35–45; residential (Table 10) high-end 25–35 / mid 36–45 / low 46–60.
- **Residential (clause 4.4.1):** peak is the morning **down-peak**; include service staff/drivers/deliveries. Population Table 6 (by bedrooms). **Table 7 handling capacity:** high-end > 8 %, mid 6–8 %, low 5–7 %. **Table 8 interval:** high-end ≤ 60 s, mid 61–80, low 81–100. At least one lift per building should be a **deep car that fits an ambulance stretcher**.
- Building-type notes: **hospitals** — load by volume not weight, arrival 10–15 %, interval 30–50 s, separate bed/stretcher lifts from staff/visitor lifts; **hotels** — check-in/out two-way peak, handling capacity > 12 %, interval < 40 s, AWT 30–40 s, dedicated lifts for public amenities; **banquets** — min lift capacity **1 360 kg / 20 pax**, door ≥ 1 000 mm; **retail/malls** — escalator-led, lifts for trolleys/wheelchairs/prams; **schools** — short sharp peaks, design for stairs, demand 12–15 %, interval 30–50 s; **car parking** — car-lift retrieval time ≤ 2 min; **24×7 buildings** — peak at shift change, high starts/stops.
- **Special building features:** basements served by main lifts hurt up-peak/down-peak (use separate shuttle lifts); multiple entry levels lose up to **15 % efficiency per extra level** (add 10 % entrance bias); reserved/VIP lifts excluded from the group; vertical zoning / sky lobbies for very tall buildings.

### 5 Lift Arrangements and Planning Dimensions

- **Arrangement:** group near the building centre, accessible from all entrances; **not more than 4 lifts in a straight line** (beyond that, use destination control); alcove arrangement recommended for > 3 lifts. For > 12 floors with passenger + service lifts in one lobby → group control.
- **Lift lobby depth (dual-line, cars facing):** **1.5 to 2.5 × the depth of one car** (quadruplex 1.5–2, octuplex 2–2.5); single-line ≈ half of that.
- **General Arrangement Drawings (GAD)** prepared by the lift manufacturer; architect provides finished sizes, floor heights, headroom, machine-room access/ventilation, pit depth, trimmer-joist and footing positions.
- **Pit refuge space & bottom clearances (clause 5.8.1, Table 12):** with the car at its lowest point, at least one refuge space on the pit floor — **upright 400 × 500 mm × 2 000 mm high**, or **crouching 500 × 700 × 1 000**, or **laying 700 × 1 000 × 500**; one extra refuge per extra person; a sign in the pit states the allowed number and posture. Free vertical distance pit-bottom to lowest car part **≥ 0.50 m** (reducible to **0.10 m** for the apron / vertically-sliding door parts within 0.15 m of the wall); to highest fixed pit items **≥ 0.30 m**.
- **Car-top refuge & headroom clearances (clause 5.8.2, Table 13):** with the car at its highest point — refuge **upright 400 × 500 × 2 000** or **crouching 500 × 700 × 1 000** on the car roof; clear distance to the well ceiling **≥ 0.50 m** over equipment, **≥ 0.10 m** over guide shoes / sliding-door headers within 0.40 m of the car projection, balustrade top **≥ 0.30 m** (within 0.40 m) / **≥ 0.50 m** (beyond).
- **Run-by (clause 5.9.4):** minimum bottom run-by for car and counterweight **≥ 150 mm**; maximum **≤ 300 mm**.
- **Minimum floor-to-floor height (clause 5.10.3.2):** horizontally-sliding doors **f + 750 mm**; vertical bi-parting doors **1.5 f + 250 mm** (f = clear entrance height).
- **Outline dimension tables — reference by page (all "recommended for architects/planners", variations by mutual agreement within Table 37/38 area limits):**
  - **Table 14** passenger & service lifts with machine room — car size, COPD door, shaft W×D by speed band (< 1 to 9–10 m/s), 4 pax (272 kg) up to 29 pax (1 972 kg). PDF **2245–2246**.
  - **Table 15** stretcher/hospital-bed lifts, 15–36 pax (1 020–2 448 kg), 2-panel telescopic door. PDF **2247**.
  - **Table 16** goods lifts with machine room, 1 000–5 000 kg. PDF **2249**. Goods-lift min rated load **≥ 3.45 kN/m²** of net car area.
  - **Table 17** machine-room height, overhead (HR) and pit depth vs speed 0.7–3.5 m/s. Typical: pit **~1 350 mm** (0.7 m/s) rising to **~2 200 mm** (2.5 m/s); overhead **CH + 1 900** to **CH + 2 800 mm**; machine-room height **~2 500 mm**. **Goods-lift minimum pit depth 1 600 mm.** PDF **2251** onward.
  - **Tables 18–26** automobile lifts / goods lifts (Series A & B, vertical and horizontal sliding doors). **Tables 27–32** machine-room-less (MRL) lifts — passenger, stretcher, goods, automobile, plus MRL pit depth (Table 29) and overhead (Table 30). PDF **~2255–2274**.
  - **Table 20** entrance types for horizontal / vertical sliding doors.

### 6 Civil and Electrical Requirements

**6.1 Civil:**
- **Lift well enclosure:** totally enclosed by imperforate walls/floor/ceiling, dust-free or painted, **minimum 120 min fire-resistant**. Partially-enclosed wells (atrium/observation): enclosure height **≥ 3.5 m at the landing-door side**; **≥ 2.5 m** on other sides where moving parts are ≥ 0.5 m away, reducible **to 1.1 m** progressively as the gap increases to 2 m; enclosure within 150 mm of the floor edge, imperforate, non-combustible.
- **Well lighting ≥ 50 lux** at 1 m above car roof and 1 m above pit floor, **≥ 20 lux** elsewhere, all doors closed; 2-way switching (pit + machine room/controller). **Landing lighting ≥ 50 lux at floor level** near landing doors.
- **Intermediate emergency landing** required so that the distance between consecutive landing-door sills **never exceeds 11 000 mm**.
- Well side walls: **RCC ≥ 150 mm or brick / equivalent fire-resisting material** (with tie beams for guide-rail fixing). Sill gap: car sill to landing sill **≤ 35 mm**; well enclosure to car sill edge **≤ 35 mm** in the landing zone (else finish flush; if enclosure > 130 mm from the car sill edge the car door needs a locking device). Projections chamfered **≥ 60° from horizontal**.
- Landing openings protected full height/width, **≥ 2 000 mm high × 700 mm clear wide**. **No common wall between lift well and any water tank/reservoir.**
- Wall strength: withstand **1 000 N over 0.09 m²** (no permanent deformation > 1 mm, no elastic > 15 mm). Glass panels → laminated, withstand 1 000 N / 0.09 m². Wire-grill partition between lifts in a common well: **≥ 2.2 mm steel wire**, a **25 mm ball must not pass**, deflection ≤ 15 mm under 450 N.
- **Pit:** dry/waterproofed, drained; floor supports **4·g·(P + Q)** under car buffer supports and **4·g·(P + q·Q)** (q ≈ 0.5) under counterweight buffer. Accessible space below the pit → base designed for **≥ 5 000 N/m²** *and* counterweight fitted with safety gear; double slab recommended. Access door, or a permanent ladder if pit depth **≤ 2.5 m**; pit stop switch accessible from the lowest landing and pit floor.
- **Machine room:** fire-resistant, weather-proof, air-conditioned or ventilated to keep **+5 °C to +40 °C**; **lighting ≥ 200 lux** around controller and machine; clear space around the machine **≥ 600 mm** on any two sides; entrance **≥ 1 000 mm wide × 2 000 mm high**; clear height **≥ 2 100 mm** at working/access areas, with **≥ 300 mm above rotating parts** and **≥ 1 000 mm** between the machine lifting point and the room hook; floor live load **≥ 10 kN/m²**; trap door supports **2 000 N over 0.20 × 0.20 m**, opens upward only, locked. Access stairs (or structural steps ≥ 1 000 mm wide). **No common wall/slab with any water reservoir.** Overhead beams: factor of safety **5 for steel, 7 for RCC**, deflection **≤ span / 1 500**; total beam load = resting equipment + **2 × suspended load**. Machinery in the well (MRL): clear height **≥ 2 000 mm**, lighting **≥ 200 lux at floor level**.
- **Well tolerance (dimension K, clause 6.1.3(d)):** 0–25 mm for wells up to 30 m; 0–35 mm up to 60 m; 0–50 mm up to 100 m (and per any 100 m portion above that).

**6.2 Electrical:**
- Per lift: one **415 V (−10 % / +6 %), 3-phase, 4-wire, 50 Hz** supply + one **230 V (−10 % / +6 %), 1-phase, 3-wire, 50 Hz** supply, provided independently; plus a separate **230 V** circuit for machine-room and shaft power/lighting sockets. Main and lighting cables run separately in each lift's own shaft. **FRLSH XLPE insulated armoured** main cables. Dedicated feeder, separate from other building services, with lock-out/tag-out.
- **Main switchgear** breaks all live conductors but must **NOT cut**: car lighting/ventilation, car-roof socket, machinery-space lighting, machinery/pit sockets, well+pit lighting, alarm device, **automatic rescue device**. Lockable in the open position. **No "no-volt" trip relay anywhere in the lift power supply.** Distribution box at **1.8–2.1 m** above floor (reset devices reachable, beyond children's reach).
- **Intercom / emergency communication** powered by emergency supply, connecting car ↔ outside ↔ emergency-operation point, required if **lift travel > 15 m** or direct acoustic contact is impossible. Alarm push in each car wired to a ground-floor terminal box.
- **Earthing:** motor/winding-machine/control-panel frame terminal **≥ 10 mm dia bolt/stud/screw**; door-interlock/contact/button/switch terminals **≥ 5 mm brass screw** with earth conductor **≥ 0.5 mm² copper**. Disconnection times per **Table 35** (e.g. 230 V a.c. TN 0.4 s / TT 0.2 s). Earthing per IS 3043 + Electricity Act/CEA. (The TN/TT/IT system theory in 6.2.3 duplicates [[Part D Sec 2 - Electrical and Allied Installations]].)

### 7 Fire Protection Requirements for Lifts and Evacuation Lifts

**7.1.1 Buildings over 15 m** (over and above clauses 6 and 8):
- Load-bearing elements, stairways, corridors, façades → **non-combustible**; interior finishes → very low flame spread.
- **Lift-well enclosure fire rating 2 h**; well **vent at top ≥ 0.2 m² per lift**.
- **Landing doors:** imperforate, **no collapsible doors**, **minimum 1 h fire-resistance (integrity)** per IS 17518 (Part 2). Car doors imperforate, non-collapsible.
- Telephone/communication in car and main lobby, linked to the fire control room. Photoluminescent "use stairs in case of fire" signs with a floor plan on every floor at the lift.
- **All lifts (fireman's and non-fireman's) get Phase I (grounding) operation** — initiated by individual/common switch or by smoke detector / fire alarm / BMS signal.
- **Fireman's lift:** **at least one per building**, and one **per wing / per bank of lifts / per zone** (buildings zoned height-wise; ≤ 600 m and > 600 m cases differ). Requirements:
  - **Fireman's switch** (two-position ON/OFF, glass-covered box) at the evacuation floor.
  - **Floor area ≥ 1.43 m²; rated load ≥ 544 kg (8-person lift).**
  - **Power-operated doors ≥ 0.8 m wide.**
  - **Speed ≥ 1.0 m/s**, such that it reaches the top floor (or top of its zone) from the fire-access level **within 1 min**.
  - Reliable **backup power** via automatic changeover; normal + backup feeders in **2 h fire-resistance-rated enclosures** up to the machine room/controller.
  - Sloped lift-lobby floor to keep firefighting water out of the shaft; "FIREMAN LIFT" in fluorescent paint at every landing.
  - **Phase I:** on switch/alarm — cancel all calls, return non-stop to the evacuation floor, park with doors open, audio/visual signal.
  - **Phase II:** car-operating-panel control only, no landing calls, door-reopening devices disabled, one car call at a time (nearest answered), doors held by continuous pressure.

**7.1.2 Buildings over 60 m** (additional):
- **Fireman's lift load ≥ 1 000 kg, floor area ≥ 2.35 m².**
- Electrical equipment within 1 m of a landing-door wall → **≥ IPX3**; switchgear < 1 m above pit floor → **IP67**; socket + lowest lamp **≥ 0.5 m above the highest permissible pit water level**; means to keep pit water below the fully-compressed car buffer.
- **Fire Command Centre (FCC) and/or BMS room**; CCTV in lift lobbies displayed in FCC/BMS.

**7.2 Evacuation Lifts** (mainly super-high-rise > 200 m; a fireman's lift is generally suitable as an evacuation lift):
- **Supplementary to stairs, never a replacement** — stairs remain available throughout.
- Three operation methods (one or a combination, per the building fire-evacuation strategy): **automatic**, **remote-assisted** (from FCC/BMS, subject to cybersecurity per IS 17805 Part 20), **manually-assisted** (attendant in the car). Manually-assisted overrides remote, which overrides automatic.
- **Pre-requisites:** sprinklers everywhere except lift machine rooms and shafts; each floor's lift lobby enclosed by a **smoke barrier**, **lift-lobby door 2 h fire-rated**, auto-closing on alarm; **lobby sized for ≥ 25 % of the floor population at 0.28 m² per person**; lobbies/stairs pressurized if required; CCTV to FCC/BMS; fire/smoke/temperature detectors throughout including shaft and machine room; **secondary power sized to run the evacuation lift(s) at rated load and speed for the full planned evacuation time** (car lighting on secondary power too); feeders in 2 h fire-rated enclosures; pit water sensor.
- **Evacuation Exit Lobby (EEL)** = destination floor. Audible signals **35–55 dBA** (typical 50). Announcements: "Evacuation Service — Enter the Car" at pickup floors, "Do Not Exit" for pass-through stops, "Exit Lift" at the EEL.
- **≥ 3-way communication** (car ↔ safe area ↔ FCC), single-button, hands-free. **Lift-car surveillance** terminal in the FCC showing the whole car floor area.

### 8 Minimum Technical and Safety Requirements

- **Minimum factor of safety for any lift part ≥ 5** (higher per IS 14665 Part 3).
- **Doors:** passenger lifts → **power-operated imperforate** car + landing doors. Door-reversal sensitive device; **force to prevent closing ≤ 150 N** (not measured in the first third of travel); full-length **infrared/light-curtain safety covering ≥ 1 600 mm of car-door height**. Reversal may be neutralised in the last **58 mm** of travel and during emergency fire operation.
- **Single- and two-speed drives shall not be used for new lifts** — VVVF only. **Regenerative-drive efficiency ≥ 0.8** in both modes; energy saving up to **40 %**. Stand-alone generator/UPS feeding a lift must have enough other load (or a UPS able to absorb) the regenerated energy.
- **Additional car operating panel** required when car width > **1 600 mm** and/or rated capacity **≥ 16 passengers**.
- **ARD (automatic rescue device):** battery-operated, on **all lifts** (optional only if a backup generator with AMF panel exists) — takes the car to the nearest landing on power/phase failure; battery good for **≥ 3 rescue operations** without recharge; audio + visual "you are being rescued" indicator in the car; emergency light + one fan run to the end of the rescue; **levelling accuracy ± 40 mm or better**; operates only with all safety circuits healthy.
- **Every building over 24 m: at least one stretcher lift** — car entrance width **≥ 800 mm**, car depth **≥ 2 100 mm**.
- **Every passenger lift: overload device.**
- **Capacity & loading (clause 8.3):** rated-load ↔ net car area by **W = 35.05 A² + 325.66 A** (W kg, A m²). **A person = 68 kg.** **Table 37** = min/max net inside area per passenger count, 4 pax (272 kg, 0.68–0.77 m²) to 36 pax (2 448 kg, 4.72–4.92 m²); beyond 36 pax add 0.109 m² (max) / 0.104 m² (min) per extra passenger. **Fireman lift minimum net car area 1.43 m².** Hospital/bed lifts treated as passenger lifts. **Table 38** = goods lifts, max area = rated load ÷ **3.45 kN/m²**; motor-vehicle lifts ÷ **1.45 kN/m²**. Class of loading: general / motor-vehicle / concentrated-with-truck (design car & frame for **150 % of rated load**) / heavy-concentration.
- **Flood sensors in the pit (clause 8.7):** two water-level switches — **Switch 1 at 50–100 mm** above the pit floor (alarm/hooter), **Switch 2 at 200–300 mm** above the pit floor (stop the lift at the nearest landing); may drive a pit pump.
- Emergency manual rescue: authorised persons only; warn occupants; kill the main switch first; gearless machines release/apply the brake at **0.5–1 s** intervals; if the car will not move down, the safety gear may have set — call a lift mechanic.

### 9 Special Technical Requirements

- **MRL lifts:** conform to **IS 15785**; emergency door on the upper hoistway **≥ 700 × 700 mm** with an electromechanical lock in the safety chain.
- **Home lifts:** private residence, **up to 5 stops, maximum rise 12 m**; rated capacity **min 208 kg (3 persons), max 272 kg (4 persons)**; **speed ≤ 0.2 m/s**; conform to **IS 15259**.
- **Hydraulic lifts:** preferably **hole-less**.
- **Accessibility:** all lifts open to the public per **IS 4963:2025**; lifts for persons with disabilities per **IS 15330:2020**.
- **Seismic:** protective measures apply where **design acceleration a_d > 1 m/s²** (a_d supplied by the building's structural designer — function of ground acceleration, soil, importance factor).
- **Automobile lifts:** entrance **≥ 2 400 mm wide × 2 300 mm high**; car inside **≥ 2 500 mm wide × 5 300 mm deep**, typically doors both sides (drive-through, no reversing); **load ≥ 2 500 kg**; rated load **≥ 1.45 kN/m²** of platform; light-curtain on car doors; barricades to bar oversized vehicles.
- **Car air-conditioning:** corrosion-resistant, ~10-year design life; single-phase **≤ 230 V a.c.** via a lockable RCCB in the machine room; ventilation noise **< 52 dBA** in the car; condensation shutdown logic (stop compressor at high water for 3 min, power off at 100 % for 1 min, manual reset).
- **BMS interface:** potential-free contacts = monitoring only (position, direction, load/overload, door status, mode); control signals (bring to lobby, park/shutdown, force fire/seismic/EMS mode) need a BA interface device.
- **CCTV in car:** "you are under CCTV surveillance" notice; trailing-grade cable; alert on signal loss.
- **EMS for hospitals:** medical hall switch → cancel car calls, reassign hall calls, return non-stop to the medical landing, doors open; second phase needs the in-car medical switch within **60 s**. Fire-service and EMS operation are mutually exclusive (whichever is active first wins).
- **DCS (destination control):** for a bank of **> 6 lifts** (or as the user decides); passengers enter the destination on landing panels, groups same-destination passengers, cuts stops and RTT. **≥ 2 terminals per floor.** Conventional control caps at **8 lifts / group, ≤ 4 in a row**; DCS extends to **10–16 lifts / group, ≤ 5 in a row**. Simulation car loading with DCS **≤ 80 %**.

### 10 Performance Requirements

- Ride quality (vibration + noise) measured per **IS 17615 (Part 1)** — during normal building conditions, after ≥ 1 h of normal operation, at the **geometric centre of the car**, dual expression (max peak-to-peak and A95 peak-to-peak).

### 11 Special Technical Requirements for Super Tall Buildings (> 200 m)

- **Air-pressure effect:** ear discomfort above landing speeds of ~10 m/s → **lifts offered up to 10 m/s max**.
- **Piston effect** (speed > 4 m/s): house high-speed lifts in a **common shaft with vent holes** in the party wall; eliminate common walls above 4 m/s (divider beams + wire mesh only); a standalone enclosed shaft for > 4 m/s → **increase shaft size 25–30 %**. Above 6 m/s: aerodynamic car exteriors, flush facia plates in front of landing doors.
- **Stack effect:** temperature-driven vertical airflow; differential pressure on landing doors (max at top/bottom, nil at the neutral pressure level); affects smoke movement — seal lift lobbies, park cars with doors closed.
- **Building sway:** wind-induced sway → rope/travelling-cable resonance; consider for buildings **> 200 m** (and slender buildings **> 150 m**, e.g. TV towers); sway detector slows or parks the lift; the building designer must share natural frequencies and displacement data with the lift designer early.
- **Ride comfort:** heavy-duty-rated guide rails, high-quality roller guides; guide system tolerant of building settlement and thermal movement.
- **Jump lifts:** self-climbing lift with a temporary machine room that rises with construction (starts ~7th floor).
- **High-density solutions:** two cars running independently in one shaft, or two cars mounted one above the other (double-deck) — DCS-controlled, hidden COP, **up to ~40 % more capacity / ~30–40 % less waiting time**; independent-cars system designed to **SIL 3 (PESSRAL, IS 17106 Part 1)**.
- **Fireman's lift for super-tall:** at least one **single-deck, 15-person / 1 000 kg** lift serving **all floors**, 1 h fire-rated landing doors, main-lobby-to-top travel **< 60 s**.

### 12–16 Tender, Acceptance, Site Coordination, Inspection, Maintenance

- **Clause 12 (enquiry / tender):** the particulars an architect must furnish — type, number, capacity (persons + kg), speed, travel + building height, floors served, control method, machine-room position/height, overhead, pit depth, hoistway W×D, counterweight position, car W×D, entrances (number/size/door type/through-car), electric supply, seismic and accessibility requirements.
- **Clause 14 (site coordination — builder's work before erection):**
  - Machine room: ventilation to **+5 to +40 °C**; access door **≥ 1 000 × 2 000 mm** MS two-panel outward-opening; **RCC machine-room slab 230 mm thick, ≥ 1 000 kg/m² UDL** plus GAD loads; hoisting beams/hooks with certified SWL; "440 V" caution notice.
  - Hoistway: **minimum clear plumb** GAD dimensions, no encroachment; **walls minimum 230 mm brick or 150 mm RCC**; no non-lift services in the well; front wall at ground/top floor built last; projections chamfered ≥ 60°; solid blocks/ISMC at guide-bracket levels; RCC lintels for landing-door headers/sills; smoke window with louvers below the overhead slab.
  - Pit: waterproofed, no seepage/debris, depth per lift speed; pedestals for car and counterweight buffers.
  - Shaft lighting **≥ 50 lux** 1 m above the pit floor / **≥ 20 lux** elsewhere / **50 lux** outside each landing; **double earthing** in the machine room.
  - Storage: unload within 50 m of storage; storage within **20 m** of the installation site; **minimum 35 m² storage per lift**, dry/lockable/weatherproof, 16 A power point, PCC floor.
- **Clause 15 (inspection & acceptance):** acceptance inspection + field tests before service, and after any major alteration; personal-safety rules; **Annex A** = the full visual & functional checklist (machine room, well, pit, car, doors, landing, safety gear, governor, buffers, ARD, signage) — reference by page, **PDF 2340–2356**.
- **Clause 16 (maintenance):** owner keeps the installation safe via a licensed maintenance organisation; **two-way car communication linked to a 24 h rescue service** at all times (remove the lift from service if it fails); owner self-monitoring (full ascent/descent ride check of doors, levelling, controls, communication, lighting, door reversal, signage); rescue only through landing doors, by trained authorised persons. Detailed maintenance guide = **IS 17900 (Part 6)**.

### Standards referenced by Subsection 5A (List of Standards, PDF 2356–2357)

| Ref | Standard | Subject |
|---|---|---|
| D-5A(1) | **IS 17900 (Part 1):2022** | Lifts — safety rules |
| D-5A(2) | IS 17900 (Part 2):2022 | Lifts — design rules, calculations, tests of components |
| D-5A(3) | IS 4963:2025 | Accessibility in the built environment |
| D-5A(4) | IS 12615:2018 | 3-phase a.c. motor efficiency classes (IE code) |
| D-5A(5) | IS 1950:1962 | Sound insulation of non-industrial buildings |
| D-5A(6) | IS 14665 (Part 2/Sec 1 & 2):2000 | Electric traction lifts — installation, O&M |
| D-5A(7) | IS 15105:2021 | Automatic sprinkler systems |
| D-5A(8) | IS 732:2019 | Electrical wiring installations |
| D-5A(9) | IS 3043:2018 | Earthing |
| D-5A(10) | IS 17518 (Part 2):2021 / ISO 3008-2 | Fire-resistance test — lift landing door assemblies |
| D-5A(11) | IS/IEC 60529:2001 | Degrees of protection by enclosures (IP code) |
| D-5A(12) | IS 17805 (Part 20):2024 / ISO 8102-20 | Lifts/escalators — cyber security |
| D-5A(13) | IS 14665 (Part 3/Sec 1 & 2):2000 | Electric traction lifts — safety rules |
| D-5A(14) | IS 2551:1982 | Danger notice plates |
| D-5A(15) | IS 15785:2007 | Lifts without conventional machine rooms (MRL) |
| D-5A(16) | IS 15259:2002 | Home lifts — installation & maintenance |
| D-5A(17) | IS 15330:2020 | Lifts for persons with disabilities |
| D-5A(18) | IS 17900-7-7 (under preparation) | Lifts under seismic conditions |
| D-5A(19) | IS 17615 (Part 1):2021 / ISO 18738-1 | Measurement of lift ride quality |
| D-5A(20) | IS 17106 (Part 1):2019 / ISO 22201-1 | PESSRAL — programmable electronic safety systems |
| D-5A(21) | IS 17900 (Part 5):2026 | Guide for inspection of lifts |
| D-5A(22) | IS 17900 (Part 6):2022 | Guide for maintenance of lifts |

---

## Subsection 5B — Escalators and Moving Walks (PDF 2364–2424)

### 1–3 Scope, Terminology, General

- **Escalators and moving walks are machines even when out of operation — they must NOT be used as, or considered, fixed staircases or fixed access.**
- Nominal speed = no-load speed; rated speed = speed under rated load.
- Conform to state Acts/Rules; owner obtains Authority permission before and after erection; a **licence for public use** is issued by state authorities. Electrical work per Electricity Act 2003 + CEA Regs 2023 + Part D Sec 2. Fire per state fire acts and [[Part F - Fire and Life Safety]].
- Maintenance by an authorized competent maintenance organisation holding a valid licence; maintenance schedule + logbook; statutory periodic examination; open pits barricaded (maintenance team only).
- Energy efficiency: stop mode with no passengers, or speed reduction to match demand via VVVF drives; LED lighting.

### 4 Design Guidelines

- **Table 1 — Escalator Duty Categories** (p.2371): Light ≤ 3 000 passengers/day; Medium ≤ 10 000; Heavy ≤ 20 000; Intensive > 20 000.
- **Escalator speeds:** most common rated speed **0.5 m/s** (0.65 and 0.75 m/s available). **Step widths 600 / 800 / 1 000 mm** (1 000 mm carries two columns).
- **Angle of inclination ≤ 30°**; may increase to **35° only for rise ≤ 6 m AND rated speed ≤ 0.5 m/s**.
- Rated speed ceiling: **0.5 m/s for inclination > 30° but ≤ 35°; 0.75 m/s for inclination ≤ 30°**.
- Recommended design handling capacity for normal peak: **3 200 to 6 400 persons/hour** by width.
- Theoretical capacity = 3 600 × (rated speed m/s × k) / 0.4, k = 1 / 1.5 / 2 for 0.6 / 0.8 / 1.0 m step widths. Practical Ce = 150 · V · k (k = 0.5 / 0.75 / 1.0). **Tables 2 & 3** give the capacity grids (persons/hour); Table 3 also shows IS 4591 values in brackets.
- **Moving walks:** inclination **6°–12°** (safest max generally **10°**); **inclination > 6° → nominal speed limited to 0.5 m/s**. Nominal widths: ≤ 6° inclination → 800 / 1 000 / 1 400 mm; > 6° → 800 / 1 000 mm.
- Shopping trolley / baggage cart width + contents **at least 400 mm less than the nominal pallet/belt width**. **Trolleys not permitted on escalators.**

### 5 Arrangement and Planning Dimensions

- Access only from adjacent corridors / landings / lobbies, not obstructing other circulation; space for queuing.
- **Boarding/alighting unrestricted area** = (distance between handrails + 160 mm) × depth **2.0–2.5 m**. Option 1: depth ≥ 2.5 m, width ≥ A + 160 mm. Option 2: depth ≥ 2.0 m, width ≥ 2A + 160 mm (A = distance between outer edges of handrails).
- Where the exit is blockable (shutter / fire gate / barrier): additional STOP button within reach from inside, **2.00–3.00 m before the comb intersection line**, **between 200 mm below and 400 mm above the handrail**; STOP button with shroud guard (covered STOP switch not permitted); shutter/gate interlocked to the safety circuit.
- **Flat/horizontal steps at boarding & alighting:** ≥ **2** for speeds ≤ 0.5 m/s; ≥ **3** for > 0.5 up to 0.65 m/s (rise > 6 m); ≥ **4** for > 0.65 m/s.
- Moving walks locking on trolleys → unrestricted landing area increased to **≥ 5 m**.
- **Escalators are NOT an accessible route** (persons with locomotor disability cannot use them) — a lift must be installed as an alternative accessible route. Tactile warning indicators at top and bottom; audible signals for the visually impaired. Moving walks for persons with disabilities → **max inclination 6°**; free of projections up to **2 100 mm**; **minimum illumination 100 lux**.

### 6 Space Requirement

- **6.1.1 Clear height above steps/pallets/belt ≥ 2.30 m** at all points (X4), extending to the end of the newel and over the unrestricted area.
- **6.1.2 Handrail-to-wall/obstacle clearance (Y10) ≥ 80 mm horizontal, 25 mm vertical** below the lower handrail edge (Y12). Height X12 from steps ≥ **2.10 m**.
- **6.1.3 Adjacent escalators (parallel or criss-cross): distance between handrails ≥ 160 mm** (Y11).
- **6.1.4 At floor intersections / criss-cross:** vertical deflector **≥ 0.30 m** high above handrail level, extending ≥ 25 mm below the lower handrail edge (imperforate triangle, no sharp edges). Not required if handrail-to-obstacle distance Y9 ≥ **400 mm**.
- **6.1.5 Successive escalators with intermediate landing without exits:** electrically interlocked to run the same direction, same capacity, and to stop the feeding unit if the one carrying passengers away stops.
- **6.1.8 Illumination ≥ 50 lux at the comb intersection line at floor level.**
- **6.2 Machinery spaces outside the truss:** lockable, authorized persons only; lighting ≥ **200 lux** in working areas, ≥ **50 lux** in access routes; emergency lighting; working height ≥ **2.00 m**; clear area in front of control panels — depth ≥ **0.70 m**, width ≥ **0.50 m** or full cabinet width; clear height for movement ≥ **1.80 m**, access ways ≥ 0.50 m (0.40 m where no moving parts); clear height in machinery spaces **never less than 2.0 m**.
- **6.3 Balustrade** on each side. **Vertical height from step nose / pallet / belt surface to top of handrail (X1): 0.90 m ≤ X1 ≤ 1.10 m.** Anti-climbing device at **1 000 ± 50 mm** above floor, length ≥ 1 000 mm. Anti-slide devices where wall-to-handrail-centreline > 300 mm — spaced ≤ 1 800 mm, height ≥ 20 mm. **Over a void: 1 100 mm balustrade preferred over 900 mm**; glass enclosures / guard rails where insufficient.
- **6.4 Installation:** intermediate supports recommended for travel height above **5 000 mm**; lifting-gear holes **100 mm dia** through the ceiling; threshold railings ≥ **80 mm** from the handrail, ≥ 160 mm between adjacent handrail edges; type-proofed oil separator (recess in the pit) for weather-exposed units.

### 6.5 Electrical

- PVC/XLPE-insulated flame-retardant armoured main cables. Per escalator: one **415 V (−10 %/+6 %), 3-phase, 4-wire, 50 Hz** + one **230 V, 1-phase, 3-wire, 50 Hz** supply outside the unit. Lighting & socket outlets on a separate circuit not cut by the inspection switch. Sub-circuit separate from other building services; lock-out/tag-out; cable route safe from fire.
- **Earthing:** V3F drives → leakage current > 3.5 mA → earthing conductor ≥ active-conductor cross-section and **≥ 10 mm²** (or two parallel conductors). MCB + RCD outside the unit near the machine.
- **3-phase:** MCB characteristic **'D'**. RCD with V3F: Type B (universal-current-sensitive), Type S (short-time-delayed), **300 mA** tripping, tolerant to 2 000 mA at higher frequencies. RCD without V3F: Type A/AC, non-delayed, **100 mA**.
- **1-phase (lighting):** MCB characteristic **'C'**; RCD Type A, non-delayed, **30 mA**, rated 16 A.
- RCD/RCBO mandatory for TT networks.

### 7 Fire Protection

Per [[Part F - Fire and Life Safety]]. Escalators/moving walks recommended non-combustible; outer/inner decking, truss, pallets/steps, track → **Class 3** flame spread [D-5B(3)]. **On a fire signal, escalator operation stops immediately**; recommended not used in emergencies. Escalator wellways may have fire shutter(s) actuated by temperature + smoke detectors to seal a floor's wellway.

### 8 Minimum Technical and Safety Requirements

- **8.2 Enclosure:** all moving parts fully enclosed within imperforate panels (except accessible steps/pallets/belt/handrail); **a 10 mm dia straight rigid rod must not pass through a ventilation aperture to touch a moving part**. Escalator inclination ≤ 30° (≤ 35° only for rise ≤ 6 m and nominal speed ≤ 0.5 m/s); moving-walk inclination ≤ 12°.
- **8.3 Width: step/pallet/belt ≥ 0.58 m and ≤ 1.10 m** (moving walks ≤ 6° inclination → up to **1.65 m**). **Step depth (direction of travel) ≥ 0.38 m; step height ≤ 0.24 m.** Step-tread grooves: width 5–7 mm, depth ≥ 10 mm, web 2.5–5 mm.
- **8.4 Driving machine & brake:** one driving machine drives **only one** unit; unloaded speed within **± 5 %** of nominal; flat belts not permitted.
  - **Auxiliary brake mandatory if:** drive connection not by shafts/gears/multiplex chains/>1 single chain; OR operational brake not electro-mechanical; OR **rise exceeds 6 m**; OR part of a public transport/service system.
- **8.5 Steps driven by at least two chains** (one each side).
- **8.7 Balustrade glass:** if glass used for the interior panel → toughened; single-layer safety (tempered) glass **min 6 mm**; multi-layer → laminated toughened, at least one layer ≥ 6 mm.
- **8.8 Skirting:** vertical, plain, rigid; horizontal clearance beside steps **≤ 4 mm each side** (or ≤ 7 mm sum of both sides); **skirt deflectors mandatory in escalators**.
- **8.9 Handrails:** move in the same direction & speed as steps within tolerance **0 to +2 %**; extend **≥ 300 mm** beyond the comb-plate teeth line at both landings; hand/finger guards at the balustrade entry. **Width 70–100 mm**; **≥ 80 mm horizontal / 25 mm vertical** from adjacent surfaces.
- **8.10 Landing:** secure foothold for **≥ 0.85 m** from the root of the comb teeth; steps move horizontally for **≥ 0.80 m** from point T1 at each landing. Moving walks > 6° → pallets/belt move for **≥ 0.40 m at max 6°** before/after the comb.
- **8.12 Speed governor:** switch off before speed exceeds **1.2 × nominal**; automatic stop on unintended direction reversal (escalators + inclined moving walks ≥ 6°).
- **8.13 Inspection control:** at least one portable manually-operated control device per unit.
- **8.14 Signage:** durable, conspicuous, English + local language; entrance safety signs (**minimum diameter 80 mm**); STOP devices red; machinery-space doors marked 'MACHINERY SPACE — DANGER' / 'ACCESS PROHIBITED TO UNAUTHORIZED PERSONS'.

### 9 Special Technical Requirements

- **9.1 Public-transport escalators** (part of a public transport system, or intensive use ~140 h/week with 100 % brake load for ≥ 0.5 h in any 3 h): **auxiliary brakes mandatory** (recommended even for rise < 6 m).
- **9.2/9.3 Semi-outdoor / outdoor units:** aluminium die-cast steps; **hot-dip galvanised truss (min 85 microns)** for fully outdoor; float switch at the lower machine room; control box IP54, inverter IP54, safety switches IP65; comb heating below 4 °C, band heating below 0 °C; SS 304+ for skirting/decking/balustrade; Class E electromagnet / Class F motor insulation.
- **9.4 Anti-trolley barriers:** at the entrance only; **free entrance width ≥ 500 mm** and less than the trolley width; **height 900–1 100 mm**; withstand a horizontal force of **3 000 N at 200 mm height** (160 kg trolley at 1.00 m/s). Fixed guiding barriers / traffic columns: min radius **500 mm** to any handrail point (reducible to 300 / 180 / 100 mm with an additional barrier); withstand **1 kN/m** at the top.
- **9.5 Seismic:** one fixed support + others horizontally movable, simply statically determinate; retained vertically so the unit can't jump off; **minimum compensation length of the movable support = maximum allowed storey drift**; truss designed for the region's design earthquake; interface to the building's seismic detector to stop the unit.
- **9.6 BMS interface:** monitoring only; **remote start/stop only if the unit is visible/monitored from the remote station.**

### 10–15 Performance, Tender, Inspection, Maintenance

- **10 Ride quality:** measured in both directions, unloaded, at all speeds; noise at **1.55 m ± 0.075 m** above the step surface.
- **14 Inspection:** before first use, after major modifications, at regular intervals, by a **competent person**. Acceptance test: visual + functional + electric-safety-device test + **no-load brake test against prescribed stopping distances**; **insulation resistance at 500 V DC > 0.5 MΩ**. Major modification = change of location / speed / electric safety devices / braking system / drive / control / step band / truss / balustrades.
- **15 Operation & Maintenance:** maintained per installer's instructions by a competent maintenance organisation; **24-hour, all-year-round call-out service for rescue of persons** mandatory; **annual inspection and safe-for-operation certification** by the maintenance organisation; logbook + layout + wiring diagram kept at the equipment. Handbook in SI units; "DANGER" alone not permitted as a sign.
- Annexes A–D: site inspection checklist, safety-device functional-test checklist, maintenance-check examples, risk-assessment elements. Standards: SP 30 (NEC 2023), IS 732, IS 3043, IS 16504 Part 1 / IEC 60204-1, IS/IEC 62305; IS 4591 for handling capacity.

---

## Subsection 5C — Power-Driven Parking Systems (PDF 2425–2458)

No Indian Standard exists yet — **EN 14010:2003 (Safety of machinery — Equipment for power-driven parking of motor vehicles)** referenced as specialist literature. Fire and structural requirements are in [[Part F - Fire and Life Safety]] Annex G (max EV parking compartment 1 000 m², K115 quick-response sprinklers ≥ 2 per vehicle ≤ 7.2 m² coverage, fire escape staircase ≥ 1 250 mm so no point > 45 m from one, riser limited to 24 m).

### 4 Parking System Types

- **Stack parking** — vehicles on platforms on vertical columns. Dependent (lower car removed to reach upper) or independent (each level independently accessible).
  - **Table 1** dependent stack (min height, mm): 2-level combined **3 400–3 800 mm** (upper 1 600; lower 1 600–2 000); 3-level combined **5 300–6 500 mm** (each level 1 600–2 000).
  - **Table 2** independent stack: 2-level required pit 1 850–2 250, combined 3 550–4 350; 3-level required pit 3 450–3 850, combined 4 950–5 550.
  - **RCC foundations minimum M25 grade**, anchoring depth 125–150 mm, concrete depth 200 mm. Emergency safety switch per operating panel; 'hold to run' operation; key lock per operating device; **IP 67 for outdoor installations**.
- **Puzzle parking** — semi-automatic grid of vertical + horizontal movements. **Table 3 — Retrieval time:** Excellent ≤ 90 s / Very good 90–100 / Good 100–120 / Acceptable 120–140 / Poor > 140. Flood sensors + warning hooter in the pit; pit waterproofed with a sump; whitewash before installation.
- **Automatic tower parking** (RCC shaft or free-standing) — central lift, configs 1/1…3/3. **~25–30 cars/hour; full fill/evacuate in ~3 h; capacity up to ~90 cars.** Light points every **6.0 m** in the shaft (3-phase 16 A switches); sound-isolation pads to RCC; **hot-dip galvanised, fire-resistant up to 120 min**; safety doors withstand **300 N perpendicular** over 500 mm².
- **Longitudinal parking** — lift at centre, front & back, for narrow set-back strips; ~30 cars; configs 1/1 or 2/2; no ramps/driveways; below-ground → no building doors/windows within the min 3.0 × 7.0 m area.
- **Chess parking (level parker)** — vertical lift + horizontal loop; slower, higher power.
- **Robotic parking** — X/Y/Z axes, with or without pallets, steel or RCC. With pallets → galvanised steel. Without pallets → cars on RCC slabs (quieter; **RCC slabs between levels aid fire-spread control**). Control-unit space ≥ 2.40 × 1.60 × 2.20 m near the transfer area.
- **Rotary parking** — vehicles in a vertical loop; free-standing, anchored; ground-level entry/exit with auto gate; ~20 cars.
- **Sliding platforms** — rails on the floor, cars moved sideways/longitudinally.

### 5 Planning and Design Guidelines

- **Nominal load capacity: vehicles minimum 2 000 kg and not more than 3 500 kg.**
- **Wheelset load distribution: 50 % of nominal load to front and rear wheelsets each.**
- **Individual wheel load: ~25 % of nominal load per wheel.**
- **Wheelbase: 2.90 m** (front-wheel centre to rear-wheel centre).
- **Track gauge: 1.5 m to 2.10 m.**
- **Tyre footprint: ~0.18 m × 0.18 m.**
- **Forces in the direction of travel: 1/7 of nominal load (kN). Transverse forces: 1/20 of nominal load (kN).**
- **Minimum operational life: 20 years.** Operation cycle: at least 1 park-in + 1 park-out per platform per day (2 cycles/space), 365 days/year.

### 6 Arrangement and Planning Dimensions

- **Maximum 4 rows.** Max grids: 1-row ≤ 15 (advisably ≤ 10); 2-row ≤ 10; 3-row ≤ 6; 4-row ≤ 4. Additional control panel after every max **5 grids**.
- **Clear width of a parking space: ≥ 2.7 m for small cars; ≥ 2.9 m for large cars (SUV).**
- **Curved/circular ramp or driveway inner radius 5.0 m** (~10.0 m preferred for safety).
- **Pedestrian walkway ≥ 0.8 m** next to driveways in large parking areas, raised or marked + illuminated.
- **Ramp slope: shall not exceed 15 % (1:8); recommended 1:10; public parking ≤ 10 %.** Ramp width ≥ 2.75 m (≥ 3.5 m circular/curved single-lane); start/end joint slope 3 %; ≥ 3.0 m extension in front of the ramp.
- **Car park length 5.0 m; parking alongside driveways ≥ 6.0 m wide.**
- **Minimum parking-space width: 2.3 m small cars / 2.5 m big cars; + 0.2 m each side for power-operated mechanised systems.** Small-car bay 2 300 × 5 000 mm; big-car 2 500 × 5 500 mm (+ 400 mm mechanised clearance). **Door-opening clearance ≥ 400 mm driver's side (1 000 mm for persons with disabilities).**
- **Accessible parking: 3 900 mm wide × 5 400 mm long; 1–2 % of spaces**, near the barrier-free entrance and passenger lifts.
- **Driveway width for 90° entry: ≥ 6.5 m in front of mechanised systems.** Single (unconnected) driveways ≥ 2.75 m; two-way ≥ 5.0 m.
- **Women's parking: 10 % of spaces** in large parking areas, column-free, near ramps/roads.
- **Clear passage height in pedestrian areas: 2.2 m.**
- **Escape routes: every medium & large parking area → at least two independent escape routes per floor** (second may be via a ramp); above-ground → one is sufficient; external staircases arranged.
- **Stairway: at least two staircases or exits to open air per floor**; **general lighting ≥ 20 lux in escape routes and driving aisles**.
- **Emergency lighting:** auto-on on power failure, ≥ **1 h** at ≥ **20 lux** (or equivalent fluorescent markings).

### 7 Safety Requirements

- **Safety doors** (pit-type systems): withstand **300 N** perpendicular over 500 mm² without permanent deformation; **height 2.0 m** (unless car height < 2.0 m); emergency access doors may be restricted to **0.65 m wide × 2.0 m high**. Interlock — load-carrying means can't move until the locking device engages **≥ 7 mm**; latch resists **1 000 N** in the door-opening direction. Electromagnets / pneumatic / hydraulic devices not used as retainers.
- **User must exit the car within 45 s.**
- Safety devices: limit switches, non-return valve (prevents unintended lowering on hydraulic failure), wheel stoppers at each bay end, locker in the vertical guide rail (stops descent on brake failure), electromagnetic locks, car-height sensor, car in/out sensor, emergency stopper.
- **Maintenance doors** (fully automatic systems): separate from the main door, openable only from outside with a key / from inside without a key; not opening inwards; opening it auto-stops the equipment; restart only when closed, by authorised personnel.
- **Separate external staircase, access at every alternate level for inspection.**
- **Illumination: working areas ≥ 100 lux; transfer area 40–60 lux.**
- **Safety railings ≥ 1 m height in stack and puzzle parking systems** around open spaces.

### 8 Ventilation and Fire Safety

- **Mechanical exhaust** required in closed medium & large parking areas. **Half-hourly mean CO concentration at 1.5 m above floor ≤ 100 ppm.** Deemed satisfied if exhaust ≥ **6 m³/h per m²** of usable parking area (low ingress/egress traffic) or ≥ **12 m³/h per m²** (other garages). At least **two equally-sized fans** per system, each on a separate dedicated circuit, auto-changeover on failure.
- **CO monitoring & warning** in large enclosed parking: acoustic + flashing signals to switch off engines if CO exceeds **250 ppm**; on backup power.
- **Notice at the entrance and on each floor:** "EXHAUST FUMES ENDANGERS HEALTH. AVOID PROLONGED STAY."
- **Fire safety:** per [[Part F - Fire and Life Safety]]. **Automatic parking areas with more than 20 spaces → sprinkler systems.** **Sprinkler system in all parking areas regardless of size**, covering all parked vehicles; sprinkler preferably eccentric from the top-area centre (S1/S3, not S2).
- **Ventilation for fully automatic systems: permanent ventilation openings/shafts, total free cross-section ≥ 0.15 m² per parking space, up to 2 m height.**
- **Motor vehicles shall not be parked in stairwells or generally accessible corridors (including ramps).**

### 9 Special Technical Requirements

Cantilever systems (within side margins — not suitable for long life) and suspended systems (hung from building beams — "not safe"). Both flagged as sub-optimal.

### 10 / List of Standards

Design for worst-case static + dynamic loads; service life 20 years. Standards: SP 30 (NEC 2023), IS 732, IS 3043, IS 16504 Part 1 / IEC 60204-1, IS/IEC 62305-1 & -4.

## Cross-references found in this Section

- Fireman's lift, evacuation lift, stretcher lift, lift fire-safety in high-rise buildings; escalator wellway fire shutters; car-parking (open/enclosed/automated/EV) fire & structural requirements; means of egress from parking floors → **[[Part F - Fire and Life Safety]]** (clause 2, Annex D, Annex G) and Part D/Sec 5A clauses 7.1–7.2.4
- All electrical work, earthing, RCD/MCB selection, lightning protection → **[[Part D Sec 2 - Electrical and Allied Installations]]** and SP 30 (National Electrical Code 2023)
- Structural stability of parking-tower / stack foundations, soil bearing → **[[Part C Sec 2 - Soils and Foundations]]**; seismic design of escalator trusses and parking structures → **[[Part C Sec 1 - Loads and Load Effects]]**
- Noise & vibration of escalators/lifts/parking machinery → **[[Part D Sec 4 - Acoustics, Sound Insulation and Noise Control]]**
- Accessibility (accessible route, reserved parking, barrier-free entrance) → IS 4963:2025

## Topics for cross-index

Escalator duty categories (Light/Medium/Heavy/Intensive) · escalator speed (0.5/0.65/0.75 m/s) and step width (600/800/1000 mm) · escalator inclination (30°, 35° for rise ≤ 6 m) · escalator handling capacity formulas + Tables 2/3 · flat steps at landings (2/3/4 by speed) · moving-walk inclination (6–12°, 10° max for accessibility) · boarding/alighting unrestricted area (2.0–2.5 m) · escalator clear height 2.30 m · handrail height 0.90–1.10 m, width 70–100 mm · handrail-to-wall clearance 80 mm / 25 mm · adjacent-handrail distance 160 mm · deflector at criss-cross (0.30 m) · machinery-space clearances and lighting (200/50 lux) · auxiliary brake triggers (rise > 6 m, public transport) · balustrade glass 6 mm · step depth 0.38 m / height 0.24 m · escalators not an accessible route (lift required) · escalator electrical (415 V / 230 V, MCB D/C, RCD 300/100/30 mA, earth ≥ 10 mm²) · escalator seismic (compensation length = storey drift) · 24-hour rescue call-out · annual inspection & certification · parking-system types (stack/puzzle/tower/longitudinal/chess/robotic/rotary/sliding) · stack parking heights (Tables 1/2) · puzzle retrieval time (≤ 90 s excellent) · tower parking (25–30 cars/h, 90-car capacity, 120 min fire resistance) · parking design loads (2 000–3 500 kg, 50 %/25 % wheelset/wheel, wheelbase 2.90 m, gauge 1.5–2.10 m, 1/7 and 1/20 nominal-load forces) · parking service life 20 years · parking rows/grids (max 4 rows, control panel per 5 grids) · parking-space width (2.7/2.9 m clear; 2.3/2.5 m bay + 0.2 m mechanised) · accessible parking bay 3 900 × 5 400 mm · ramp slope (15 % max, 10 % public) · parking escape routes (2 per floor, 20 lux, 1 h emergency lighting) · parking safety doors (300 N, 1 000 N latch, 7 mm interlock) · user exit within 45 s · parking safety railings ≥ 1 m · parking CO limits (100 ppm mean, 250 ppm warning) · parking exhaust rates (6 / 12 m³/h per m²) · automatic parking > 20 spaces → sprinklers · fully automatic parking ventilation (0.15 m² per space)

**5A Lifts:** lift traffic analysis (population, NUA, absenteeism 10–20% office-only, RTT/interval/handling-capacity equations) · office occupancy area per person (Table 1) · quantity of service 10–25% (Table 2) · interval quality of service (Table 3, <25 s excellent) · lift speed vs floors (Table 11, 0.6–1.0 up to 6 floors … 10 m/s practical max) · lobby depth 1.5–2.5× car depth · max 4 lifts in a straight line · pit refuge space (400×500×2000 upright) · bottom clearance 0.50 m / apron 0.10 m · car-top refuge & headroom clearance 0.50 m · run-by min 150 / max 300 mm · floor-to-floor height f+750 (horizontal) / 1.5f+250 (vertical bi-parting) · lift dimension Tables 14–32 (by page) · Table 17 pit/overhead/machine-room · well enclosure 120 min fire, 2 h over 15 m · well vent ≥ 0.2 m²/lift · landing doors 1 h fire, imperforate, no collapsible · well lighting 50/20 lux · landing sill gap ≤ 35 mm · intermediate landing if sill spacing > 11 000 mm · no common wall lift/water tank · pit buffer support 4g(P+Q) · accessible space below pit → 5000 N/m² + counterweight safety gear · machine room +5 to +40 °C, 200 lux, 600 mm clearance, entrance 1000×2000, height 2100 + 300 above rotating parts, floor 10 kN/m² · overhead beam FoS steel 5 / RCC 7, deflection ≤ span/1500 · well tolerance K (0–25/35/50 mm) · lift supply 415 V (−10/+6%) 3ph + 230 V 1ph · main switchgear must not cut car light/alarm/ARD · intercom if travel > 15 m · earthing motor ≥ 10 mm bolt / control ≥ 5 mm screw + 0.5 mm² Cu · fireman's lift ≥ 1 per building/wing/bank/zone, ≥ 1.43 m² & 544 kg (over 15 m), ≥ 1000 kg & 2.35 m² (over 60 m), doors ≥ 0.8 m, speed ≥ 1.0 m/s / top in 1 min, Phase I & II, 2 h fire-rated feeders · over 60 m: IPX3 near landing door, IP67 pit switchgear, FCC + lobby CCTV · evacuation lift (> 200 m): supplementary to stairs, 3 methods (auto/remote/manual), lobby 2 h door + smoke barrier + 25% floor pop at 0.28 m²/person, secondary power for full evacuation time, 35–55 dBA signals, 3-way comms, car surveillance in FCC · factor of safety ≥ 5 · door reversal force ≤ 150 N, light curtain ≥ 1600 mm · no 1-/2-speed drives · regen drive efficiency ≥ 0.8 (up to 40% saving) · extra COP if car > 1600 mm or ≥ 16 pax · ARD on all lifts (≥ 3 rescues, ± 40 mm levelling) · stretcher lift in every building > 24 m (≥ 800 mm entrance, 2100 mm depth) · capacity W = 35.05A² + 325.66A, person = 68 kg, Tables 37/38 · goods ÷ 3.45 kN/m², automobile ÷ 1.45 kN/m² · fireman lift min net area 1.43 m² · pit flood sensors (50–100 mm / 200–300 mm) · MRL emergency door 700×700 (IS 15785) · home lift ≤ 5 stops / 12 m rise / 208–272 kg / ≤ 0.2 m/s (IS 15259) · accessibility IS 4963 / IS 15330 · seismic if a_d > 1 m/s² · automobile lift 2400×2300 entrance, 2500×5300 car, ≥ 2500 kg · car AC ≤ 230 V, < 52 dBA · DCS for > 6 lifts, ≥ 2 terminals/floor, conventional max 8 lifts/4 per row → DCS 10–16 lifts/5 per row · ride quality IS 17615 at car geometric centre · super-tall: 10 m/s speed limit, piston effect (common shaft + vents / +25–30% standalone), stack effect, building sway (> 200 m, slender > 150 m), jump lifts, double-deck / 2-cars-per-shaft (SIL 3, +40% capacity) · site prep: machine-room slab 230 mm / ≥ 1000 kg/m², hoistway walls 230 mm brick / 150 mm RCC, storage ≥ 35 m²/lift within 20 m · 24 h rescue service · Annex A inspection checklist (PDF 2340–2356) · primary standard IS 17900 (Part 1):2022.
