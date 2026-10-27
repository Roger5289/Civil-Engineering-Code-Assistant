---
status: active
project: civil-engineering
type: reference
---
# Fire Prevention & Protection Ruleset — NBC 2026 Part F

Continuation of Phase 1 (Code Design Assistant) after [[Egress Ruleset - Part F]] — the rest of [[Part F - Fire and Life Safety]] converted into checkable rules, now that egress validated the method. Covers applicability, occupancy classification, fire resistance ratings, general fire-prevention requirements, smoke control, compartmentation, gas supply, detection/alarm, fire protection installations, occupancy-specific fire rules, refuge, and the Annexes.

**Built from the already-audited section note, not re-derived from the raw PDF line by line** — Phase 0 (2026-09-05) verified [[Part F - Fire and Life Safety]] against the source and found/fixed the errors it was going to find.

**Completed 2026-09-11:** Tables 7A–7J (firefighting installations by occupancy), 7K/7M (protection-level base calcs), 8 (main sizes), and 9/10/11 (supplementary hazard-room protection) were originally left as reference-by-page — this session converted all of them into full rule tables (§G.1–G.4, §H), after finding a clean coordinate-based extraction of the source (`NBC-2026-fulltext.txt`) that held up well even for these R/NR and S/NS matrices. Two tables (10 and 11) needed page-image verification because their row labels and value-grids had separated during linear extraction — confirmed correct against the actual source pages before being written in. **Annexes A, B, C, and N remain reference-by-page** (§R below) — these are substantially larger (Annex N alone is ~52 pages of per-industry detail) and weren't converted this session; continue that conversion in a future session if wanted.

## 0. Applicability — When Part F Applies [Cl 1; p.2739]

| Occupancy | Height threshold | Floor area threshold | Notes |
|---|---|---|---|
| Residential | > 24 m | > 750 m² | |
| Educational | > 9 m | > 500 m² | |
| Institutional | > 15 m | > 500 m² | |
| Assembly | > 9 m | > 750 m² | |
| Business | > 15 m | > 750 m² | |
| Mercantile | > 15 m | > 1 000 m² | |
| Industrial, low/moderate hazard (G-1/G-2) | any height | total building area > 2 000 m² | |
| Industrial, high hazard (G-3) | > 15 m | > 500 m² | |
| Storage | > 9 m | > 500 m² | |
| Hazardous | > 9 m | > 500 m² | |
| Mixed use | > 15 m | > 1 000 m² | |

**Trigger conditions independent of the table above:** applies on **alteration over an area ≥ 1 000 m²**, or on **any change of occupancy**, regardless of size. Buildings below every threshold that still have only a single staircase must make that staircase a firefighting-shaft type (external periphery, ventilated lobby + stairwell, 2 h fire door to lobby, 1 h to stairwell) — being "below threshold" doesn't exempt a single-stair building from this. Performance-based design (Annex M) is a route **only for heritage buildings**; anything else needs state fire-authority sign-off, not a self-declared performance path.

## A. Occupancy Classification [Cl 3.1; p.2748–2752]

| Parameter | Condition | Threshold / Rule | Notes |
|---|---|---|---|
| Minor occupancy | Incidental use vs. main occupancy | **≤ 30%** of floor area → classified as the main occupancy | **> 30%** → the building becomes mixed occupancy instead — a hard trip point, not a gradient. |
| Mixed occupancy governance | Building with 2+ occupancy groups | Governed by the **most restrictive** provision among the constituent occupancies | Change to a more hazardous group → must comply with the new group's rules; certificate of occupancy required before the change. |
| Mixed-occupancy separation | Any two adjoining occupancy groups | **120 min** for most cross-pairs; **240 min** for higher-risk pairs (e.g. Business↔High-hazard-industrial, Moderate-industrial↔Hazardous, Storage↔Hazardous); **180 min** Moderate-industrial↔Storage; several pairs involving Hazardous/High-hazard-industrial are **NP (not permitted)** | This is a summary of the matrix, **not the full pair-by-pair table** — Cl 3.1.11.1, p.2752 has the complete matrix; pull the actual page for any specific pair not listed here. |

## B. Types of Construction & Fire Resistance — Table 1 [Cl 3.4.1/3.4.2/3.5.9; p.2754–2755]

| Element | Type 1 | Type 2 | Type 3 | Type 4 |
|---|---|---|---|---|
| Exterior bearing walls (separation < 3.7 m) | 240 | 120 | 120 | 60 |
| Exterior non-bearing walls (< 3.7 m) | 120 | 90 | 60 | 60 |
| Exterior non-bearing walls (3.7–9 m) | 90 | 60 | 60 | 60 |
| Exterior non-bearing walls (≥ 9 m) | 60 | 60 | 60 | 60 |
| Fire separation assemblies (fire check doors) | 120 | 120 | 120 | 120 |
| Fire enclosures of exits | 120 | 120 | 120 | 120 |
| Shafts (services, lift hoistway, refuse chutes) | 120 | 120 | 120 | 120 |
| Vertical separation, adjacent tenant spaces | 60 | 60 | 60 | 60 |
| Dwelling-unit separation (load-bearing / non-load-bearing) | 120 / 60 | 120 / 60 | 60 / 30 | 60 / 30 |
| Interior bearing walls/columns/beams/trusses, > 1 floor | 240 | 120 | 120 | 120 |
| ...supporting 1 floor or roof only | 180 | 90 | 60 | 60 |
| Walls supporting structural members | 180 | 90 | 60 | 60 |
| Floor construction | 120 | 90 | 60 | 60 |
| Roof construction (≤ 5 m to lowest member) | 120 | 90 | 60 | 60 |
| Roof construction (5–6.7 m) | 60 | 60 | 60 | 60 |
| Roof construction (≥ 6.7 m) | 0 | 0 | 0 | 0 |

All ratings in minutes. **Roof ≥ 6.7 m note:** the 0-min rating flips to **60 min where services/cables run near the roof** (e.g. airports) — don't read the "0" as unconditional.

**Related non-tabular rules from the same clause group:**

| Parameter | Condition | Threshold | Notes |
|---|---|---|---|
| Staircase enclosure walls | Non-combustible construction (Types 1–3) | **≥ 120 min** internal walls | |
| Load-bearing steel protection | Buildings with total covered area ≥ 500 m² | Beams/columns must be fire-protected against collapse | Rated materials + suppression; sizing in Annex C Tables 25 & 26. |
| False ceiling | Any | Ceiling + all suspension fixtures **non-combustible** | |
| Glazing rating | Glazing assembly | Rated to the construction type per Table 1 | Glass **not permitted** for exit enclosures/passageways regardless of rating. |
| Glazing, fire separation ≥ 9 m | Fully sprinklered building | Tempered glass in non-combustible assembly OK; sprinklers within 600 mm of facade | |
| Glazing, fire separation < 9 m | Same | Add ≥ 900 mm spandrel panel, 1 h rating | |

## C. General Requirements for All Occupancies [Cl 3.5; p.2755–2766]

| Parameter | Condition | Threshold | Notes |
|---|---|---|---|
| Openings in fire-resistant walls | Types 1–3 | Max **5.6 m²**, max height/width **2.75 m**, protected by **≥ 120 min** fire doors | Floor openings need ≥ 120 min vertical enclosures. |
| Escalator openings | Any | **450–600 mm** smoke barrier + sprinklers all sides, every floor | Sprinkler-to-barrier gap 150–300 mm. |
| Service ducts/shafts | Any | **≥ 120 min** | Electrical shaft inspection door ≥ 120 min with 30 min insulation. |
| Refuse chutes | Any | Non-combustible enclosure ≥ 120 min; opening ≥ 1 m above roof; inspection panels 60 min; sprinklered | **≥ 3 m from exits**; not inside staircase enclosure or service shafts. |
| Clear height, exit access | Any | **≥ 2 100 mm** | |
| Substation (independent) | Any | Walls & doors **≥ 120 min** | Accessible from outside, ground floor or first basement. |
| Substation (oil-filled) | Equipment > 2 000 litre oil | **240 min** baffle walls (≥ 600 mm above equipment, ≥ 300 mm each side) | Utility building/outdoor only, ≥ 6 m from adjoining buildings; transformers > 10 MVA → HV water spray/HP water mist mandatory. |
| Substation (dry-type) | Transformers inside buildings | Must be dry type; all walls/ceiling/floor/openings **120 min** | |
| DG sets | Any | Ground floor or first basement only; DG room **120 min** | Day oil tank in dyked enclosure ≥ 110% of tank volume + 300 mm sand. |
| Escape lighting | Floor-centreline | **≥ 10 lumen/m²** | Routes up to 2 m wide → 50% of width at ≥ 5 lumen/m²; assembly during performances ≥ 2 lux. |
| Emergency lighting | Any | On within **5 s** of failure, maintained **≥ 90 min** | Battery-pack lighting is **not** a substitute for DG. |
| Exit directional signage | Exit access | No point **> 30 m** from a visible sign | Sign at every direction change; green; illuminated on alternative supply. |
| Boiler room | Any | **180 min**, entry door 120 min composite | Dedicated ventilation, not through electrical room or exits. |
| Surface finishes | Class 1 (very low flame-spread) | Permitted anywhere | Class 2: anywhere except walls/facade/staircases/corridors. Class 3: only living/bed rooms, lining solid walls. Class 4: only ceiling lining ≥ 2.4 m above floor below, fire-retardant treated, **never** in kitchens/corridors/staircases. |
| ACP facade | If used at all | **≥ 70%** mineral core + pass ISO 3957/ISO 13785 | Source recommends avoiding ACP facades altogether — this is the fallback spec, not an endorsement. |
| Fire Command Centre | Any building requiring one | On the entrance floor, direct access, **120 min** walls + fire door | Houses main fire alarm panel, PA, all fire-safety-system controls; 2 laminated floor-plan + equipment-detail sets. |

## D. Smoke Control & Pressurisation [Cl 4.4.2.5, 4.6; Table 5 p.2782–2783]

| Parameter | Condition | Threshold | Notes |
|---|---|---|---|
| Staircase pressure | Pressurised staircase | **50 Pa** | |
| Lobby/corridor pressure | Pressurised lobby/corridor | **25–30 Pa** | Enclosed staircase adjacent to a lobby (pressurised or not) is still 50 Pa. |
| Segregation | Pressurised ↔ unpressurised areas | **120 min** fire-resistant wall | |
| Fresh-air intake | Pressurisation system | **≥ 4 m** from exhaust outlets | |
| Internal staircase, no external wall | Any height | Pressurised at all heights | Exception: residential apartment houses / one-or-two-family dwellings below 15 m. |
| Internal staircase, with external wall | < 15 m | Pressurised, except residential (as above), which may be naturally ventilated | |
| Internal staircase, with external wall | 15–30 m | Naturally ventilated **or** pressurised | |
| Internal staircase, with external wall | > 30 m | Cross-ventilated **or** pressurised | |
| Lift lobby | < 15 m | Not required at ground & above — but segregation + pressurisation still required if the lift serves a basement | |
| Lift lobby | 15–30 m | Naturally ventilated or pressurised | |
| Lift lobby | > 30 m | Cross-ventilated or pressurised | |
| Natural ventilation opening | Per landing | **0.5–1.5 m²** in external wall | Cross-ventilated stair needs 2 such openings in opposite/adjacent walls. |
| Above-ground smoke exhaust | Corridors of guest rooms/non-self-preservation patients/sleeping areas, theatres, large lobbies | **≥ 12 ACPH**, or pressurisation 25–30 Pa | Exit-passageway doors 120 min; smoke exhaust fans rated 250 °C/120 min; naturally cross-ventilated corridors exempt. |
| Below-ground smoke ventilation | Each basement | Natural vents **≥ 2.5%** of floor area round the perimeter, OR mechanical **12 ACPH** in fire/distress | Multi-level basements need masonry/RCC intake+exhaust shafts, back-draft dampers, fans in 120 min rooms. |

## E. Compartmentation — Table 6 [Cl 4.5.3; p.2784–2786]

| Building type | Max area, unsprinklered (m²) | Max area, sprinklered (m²) |
|---|---|---|
| Enclosed basement vehicle parking (most occupancies) | 750 | 5 000 |
| Basements other than car parking | 750 | 2 000 |
| Hospitals/nursing homes with sleeping patients | 750 | 2 000 |
| Custody/care of children/aged incapable of self-preservation | 750 | 1 500 |
| Mercantile / multistorey mercantile | 750 | not essential |
| Assembly, with or without atrium | 1 500 | not essential |
| Business occupancy | 750 | 3 000 |
| Datacentre buildings | must be sprinklered | 2 000 |
| Hotel building | 750 | 3 000 |
| Industrial < 6.7 m height | 1 500 | 10 000 |
| Hazardous / high-hazard | must be sprinklered | 500 |
| Warehouses < 5.0 m height | must be sprinklered | 5 000 |

| Parameter | Condition | Threshold | Notes |
|---|---|---|---|
| Critical utility rooms | Electrical room, server room, UPS, battery, lift machine rooms, IT/networking, MDF/IDF/MCR, telecom, janitor storage, chemical storage, QA/QC labs | **2 h fire-rated on all sides, regardless of size** | No area-based exemption — this overrides the "not essential above X sprinklered" pattern seen elsewhere in Table 6. |
| Live-cooking areas | Any fuel — induction, LPG, PNG — in hotels, IT parks, cafeterias, hostels, food courts, malls, commercial kitchens | **120 min** fire-rated segregation | |
| Guest rooms/corridors/banquets | Hotel-type occupancy | 60 m² fire-compartmented, 30 min fire doors | |
| Industrial/storage hazardous areas | Vehicle charging, ignitable/hazardous/flammable storage | Compartmented **regardless of size** | Exception: **≥ 30 m** from any occupied building removes the requirement. |
| Large-height-space exemption | Airports, exhibition halls, mall atria, warehouses > 5 m, industrial > 6.7 m, double-height lobbies | **Exempt** from compartmentation entirely | |

## F. Gas Supply & Hazardous Areas [Cl 4.7, 4.8; p.2766–2843 range]

| Parameter | Condition | Threshold | Notes |
|---|---|---|---|
| Gas pipe routing | Any building | Separate exclusive shafts on external walls, away from staircases; distribution pipes below false ceiling | |
| Gas lines exclusion zone | Any building | **Not through** enclosed staircases, electrical shafts, escape routes, refuge areas | |
| LPG kitchens | Basements | **Not permitted** | Induction/PNG/electric OK for incidental basement occupancy. |
| Gas-leak detection | Buildings > 100 m with LPG | Detectors at usage points, monitored from FCC | |
| Seismic shut-off valve | Mixed-use assembly (malls) + institutional above 15 m | Required at main distribution point | |
| Hazardous equipment rooms | High-pressure boilers, refrigeration machinery, transformers, explosion-prone equipment | **120 min** rating; not directly under/adjacent to fire exits; vented to outside air | Approved outside gas shut-off valve required per building. |

## G. Fire Detection & Alarm, and Firefighting Installation Requirements [Cl 4.9, 5.1; p.2766–2843 range]

### G.0 Fire Detection & Alarm [Cl 4.9; p.2766–2843 range]

| Parameter | Condition | Threshold | Notes |
|---|---|---|---|
| Self-certification eligibility | Buildings up to 500 m² area **AND** up to 24 m height | Self-certification by a certified State-approved professional is acceptable | **Both conditions required together** — exceeding either one alone removes eligibility. |
| Additional detector placement | Assembly & institutional buildings, and all buildings above 30 m | Detectors also inside electrical shafts and lift machine rooms | |
| Voice evacuation | Where fire alarm is provided | English + Hindi + vernacular, pre-recorded, integrated with fire alarm panel | Alerts the fire zone plus surrounding zones/floors. |
| Fire alarm panel wiring | Any | Peer-to-peer or redundant cables in different shafts | |
| Monitored parameters | Where automatic fire alarm is provided | Tank water levels, hydrant & sprinkler pressures per zone, pump ON/OFF, isolation-valve supervisory switches | |

### G.1 Firefighting Installation Requirements by Occupancy — Tables 7A–7J [Cl 5.1.1(a); p.2791–2819]

**Converted 2026-09-11 from a full re-read of the source (cross-checked against page images for the two tables whose row labels risked misalignment) — this replaces the earlier "reference-by-page only" treatment of these tables.**

**Applies to every row below:** buildings **≤ 500 m² AND ≤ the occupancy's stated height threshold** (both conditions together) may use **self-certification by a certified, State-approved building professional** instead of the installations below — this exemption is restated at the top of every one of Tables 7A–7J, not just once.

**Column legend:** FE = Fire Extinguisher · HR = First-Aid Hose Reel · DC = Down-Comer · WR = Wet Riser · YH = Yard Hydrant · SP = Automatic Wet Sprinkler System · DA = Automatic Detection & Alarm System (+ LPG/PNG gas detector for Residential specifically) · PA = Public Address & Voice Evacuation System. **R = Required, NR = Not Required.**

#### Residential (A) — Table 7A [p.2791–2794]

| Sub-type | Height / Area band | Class | FE | HR | DC | WR | YH | SP | DA | PA |
|---|---|---|---|---|---|---|---|---|---|---|
| A-I Lodging/rooming houses | 501–1000 m² (any height ≥24m, or <24m with this area) | HL-1 | R | R | NR | NR | NR | NR | R | NR |
| A-I Lodging/rooming houses | ≥1001 m² | HL-2 | R | R | R | NR | NR | NR | R | R |
| A-II Dormitories | 501–1000 m² | HL-1 | R | R | NR | NR | NR | NR | NR | NR |
| A-II Dormitories | ≥1001 m² | HL-2 | R | R | R | NR | NR | NR | R | NR |
| A-III Apartment houses | 24–60 m height, or <24m with 501–1000 m² | HL-2 | R | R | R | NR | NR | NR | NR | NR |
| A-III Apartment houses | ≥1001 m² (same height band) | HL-3 | R | R | NR | R | R | NR | R | R |
| A-III Apartment houses | Above 60 m | CL-4 | R | R | NR | R | R | R | R | R |
| A-IV Hotels | Up to 24 m, 501–1000 m² | HL-3 | R | R | R | NR | NR | NR | R | NR |
| A-IV Hotels | Up to 24 m, ≥1001 m² | CL-3 | R | R | NR | R | NR | R | R | R |
| A-IV Hotels | 24–60 m, or 3/4-star hotels | CL-4 | R | R | NR | R | R | R | R | R |
| A-IV Hotels | Above 60 m | — | See Note 5 (multi-level pumping/hydraulic calc) | | | | | | | |
| A-V Starred (5-star) hotels | Up to 60 m | CL-5 | R | R | NR | R | R | R | R | R |
| A-V Starred (5-star) hotels | Above 60 m | — | See Note 5 | | | | | | | |

**Notes (Table 7A):** 1 — kitchen present → HL-2 minimum. 2 — basement with sprinklers → CL-3 minimum. 3 — EV parking in podium/basement → sprinklers, CL-5 minimum. 4 — rate-of-rise heat sensors in EV areas; smoke sensors in all non-ICE basement areas; CO sensors + ventilation trigger for ICE parking. 5 — height >60 m → hydraulic-calc-based multi-level pumping/storage with gravity redundant down-comer, pumps ≤12 bar shut-off. 6 — pump pressure/quantity backed by hydraulic calculations. 7 — cluster of ≤5 buildings, ≥9 m apart → common 2,500 lpm @10 bar pumping + 2,55,000 L storage (closer than 9 m, or EV parking/charging present → CL-5 instead). 8 — cluster buildings >45 m → multi-level pumping/storage per SLD, +storage every 45 m. 9 — cluster >5 buildings → a second set of pumps/storage (max 2 sets), if hydraulically justified. 10 — see Tables 7K/7M for water-quantity basis.

#### Educational (B) — Table 7B [p.2795–2797]

| Height / Area band | Class | FE | HR | DC | WR | YH | SP | DA | PA |
|---|---|---|---|---|---|---|---|---|---|
| 24–45 m, or <24m with 501–1000 m² | HL-3 | R | R | NR | R | R | NR | R | R |
| 24–45 m, or <24m with ≥1001 m² | CL-4 | R | R | NR | R | R | R | R | R |
| 45–60 m | CL-4 | R | R | NR | R | R | R | R | R |
| Above 60 m | — | See Note 5 | | | | | | | |

**Notes (Table 7B):** 1 — labs/AV/computer rooms/auditoriums present → sprinklers, CL-3 minimum. 2 — basement with sprinklers → CL-3. 3 — EV parking → CL-5. 4 — EV rate-of-rise heat sensors + non-ICE basement smoke sensors + ICE CO sensors/ventilation. 5 — >60 m → hydraulic-calc multi-level pumping, ≤12 bar shut-off. 6 — pump pressure/quantity per hydraulic calc. 7 — cluster ≤5 buildings ≥9m apart → 2,500 lpm@10 bar + 2,55,000 L (else CL-5). 8 — cluster >45 m → SLD multi-level pumping + storage every 45 m. 9 — cluster >5 → second pump/storage set (max 2). 10 — see Tables 7K/7M.

#### Institutional (C) — Table 7C [p.2798–2801]

| Sub-type | Height / Area band | Class | FE | HR | DC | WR | YH | SP | DA | PA |
|---|---|---|---|---|---|---|---|---|---|---|
| Nursing homes/sanatoria | Above 15 m, or ≤15m with ≥501 m² | HL-3 | R | R | R | NR | NR | NR | R | NR |
| C-I Hospitals | ≤45 m, 501–1000 m² | CL-3 | R | R | NR | R | R | R | R | NR |
| C-I Hospitals | ≤45 m, ≥1001 m² | CL-4 | R | R | NR | R | R | R | R | R |
| C-I Hospitals | 45–60 m | CL-5 | R | R | NR | R | R | R | R | R |
| C-I Hospitals | Above 60 m | — | See Note 3 | | | | | | | |
| C-II/III Custodial, penal, mental | ≤45 m, 501–1000 m² | HL-2 | R | R | R | NR | NR | NR | NR | R |
| C-II/III Custodial, penal, mental | ≤45 m, ≥1001 m² | HL-3 | R | R | NR | R | R | NR | R | R |
| C-II/III Custodial, penal, mental | Above 45 m | HL-4 | R | R | NR | R | R | NR | R | R |

**Notes (Table 7C):** 1 — basement storage of oxygen/medical gases/gas fuel, laundry/linen/waste, transformer/HT rooms in-footprint or basement → sprinklers, CL-3. 2 — EV parking → CL-5. 3 — >60 m → hydraulic-calc multi-level pumping, ≤12 bar. 4 — supplementary protection per Table 9/10/11 for specific hazard/critical rooms. 5 — pump pressure/quantity per hydraulic calc. 6 — EV rate-of-rise + non-ICE smoke sensors + ICE CO sensors (parking/podium recommendation). 7 — cluster ≤5 buildings, 3785/2500 lpm@10 bar + 3,50,000/2,55,000 L per 45m height (else CL-5 if <9m apart or EV present). 8 — cluster >45m → SLD multi-level pumping, storage every 45m. 9 — cluster >5 → second set (max 2). 10 — height >30 m → hydraulic-calc system architecture. 11 — see Tables 7K/7M.

#### Assembly (D) — Table 7D [p.2802–2804]

| Height / Area band | Class | FE | HR | DC | WR | YH | SP | DA | PA |
|---|---|---|---|---|---|---|---|---|---|
| 9–15 m, or <9m with 501–1000 m² | HL-3 | R | R | NR | R | NR | NR | R | NR |
| 9–15 m, or <9m with ≥1001 m² | CL-4 | R | R | NR | R | R | R | R | NR |
| Above 15 m | CL-4 | R | R | NR | R | R | R | R | NR |

**Notes (Table 7D):** 1 — basement with sprinklers → CL-3. 2 — EV parking → CL-5. 3 — live-cooking kitchens, boiler/furnace, laundry/linen/waste, transformer/HT rooms in-footprint or basement → sprinklers, CL-4. 4 — pump pressure/quantity per hydraulic calc. 5 — EV rate-of-rise + non-ICE smoke sensors + ICE CO sensors (parking/podium). 6 — cluster ≤5 buildings ≥9m apart → 2,500 lpm@10 bar + 2,55,000 L (else CL-5). 7 — cluster >45m → SLD multi-level + storage every 45m. 8 — cluster >5 → second set (max 2). 9 — see Tables 7K/7M.

#### Business (E) — Table 7E [p.2804–2808]

| Sub-type | Height / Area band | Class | FE | HR | DC | WR | YH | SP | DA | PA |
|---|---|---|---|---|---|---|---|---|---|---|
| General business | 15–45 m, 500–1000 m² | CL-2 | R | R | R | NR | NR | R | R | R |
| General business | 15–45 m, 1001–3000 m² | CL-3 | R | R | NR | R | R | R | R | R |
| General business | 15–45 m, ≥3001 m² | CL-4 | R | R | NR | R | R | R | R | R |
| General business | 45–60 m | CL-5 | R | R | NR | R | R | R | R | R |
| General business | Above 60 m | — | See Note 4 | | | | | | | |
| Data centres (<15 m) | ≤1000 m² | — | R | R | NR | R | R | R | R | R |
| Data centres (<15 m) | ≥1001 m² | — | R | R | NR | R | R | R | R | R |
| Data centres (≥15 m) | ≤1000 m² | — | R | R | NR | R | R | R | R | R |
| Data centres (≥15 m) | ≥1001 m² | — | R | R | NR | R | R | R | R | R |

**Notes (Table 7E):** 1 — basement with sprinklers → CL-3. 2 — EV parking → CL-5. 3 — supplementary protection per Table 9/10/11 for hazard/critical rooms. 4 — height >60 m → hydraulic-calc multi-level pumping, ≤12 bar. 5 — pump pressure/quantity per hydraulic calc. 6 — cluster ≤5, ≥9m apart → 2500 lpm@10bar + 2,55,000L (else CL-5). 7 — cluster (3785 lpm variant) → 3785 lpm@10bar + 3,50,000L, ≥9m apart (else CL-5). 8 — cluster >45m → SLD + storage/45m. 9 — cluster >5 → second set (max 2). **10 — entire data-centre building: sprinklers, CL-5 minimum; IT/data hall may use clean-agent gas suppression only if racks lack BBUs >20 kWh backup.** **11 — all internet/hyperscale/colocation data centres: CL-6 minimum.** **12 — IT/data hall racks with Li-ion BBUs ≤20 kWh/rack: wet/dry sprinkler, pre-action, or 3rd-party-tested water mist; >20 kWh/rack: water mist NOT permitted.** 13 — cluster of ≤3 data-centre buildings: common pumping + storage may add a diesel-engine pump with double storage. **14 — any building with Li-ion energy storage >600 kWh/floor → CL-6.** **15 — Li-ion BESS rooms: wet/single-interlock pre-action sprinkler only, treating the entire room as the assumed area of operation; pump/storage sized by the higher of design or hydraulic calc.** 16 — see Tables 7K/7M.

#### Mercantile (F) — Table 7F [p.2809–2811]

| Height / Area band | Class | FE | HR | DC | WR | YH | SP | DA | PA |
|---|---|---|---|---|---|---|---|---|---|
| 15–30 m, or <15m with 501–1000 m² | HL-3 | R | R | R | NR | NR | NR | R | NR |
| 15–30 m, or <15m with ≥1001 m² | CL-4 | R | R | NR | R | R | R | R | NR |
| Above 30 m | — | See Note 5 | | | | | | | |
| Underground shopping complex | — | CL-5 | R | R | NR | R | R | R | R | R |

**Notes (Table 7F):** 1 — basement with sprinklers → CL-3. 2 — EV parking → CL-5. 3 — supplementary protection per Table 9/10/11. 4 — pump pressure/quantity per hydraulic calc. 5 — height >30 m → hydraulic-calc system architecture. 6 — height >60 m → multi-level pumping + gravity redundant down-comer, ≤12 bar. 7 — EV rate-of-rise + non-ICE smoke sensors + ICE CO sensors. 8 — see Tables 7K/7M.

#### Industrial (G) — Table 7G [p.2811–2815] — *see also Annex N for specific industries*

| Sub-type | Built-up area | Class | FE | HR | DC | WR | YH | SP | DA | PA |
|---|---|---|---|---|---|---|---|---|---|---|
| G-1 Low hazard | ≤1000 m² (incl. MSMEs) | HL-1 | R | R | NR | NR | NR | NR | NR | NR |
| G-1 Low hazard | 1001–2000 m² | HL-2 | R | R | R | NR | NR | NR | NR | NR |
| G-1 Low hazard | 2001–3000 m² | HL-3 | R | R | NR | NR | R | NR | R | NR |
| G-1 Low hazard | Above 3001 m² | HL-4 | R | R | NR | NR | R | NR | R | NR |
| G-2 Moderate hazard | ≤500 m² | HL-2 | R | R | R | NR | NR | NR | NR | NR |
| G-2 Moderate hazard | 501–2000 m² | HL-3 | R | R | NR | R | R | NR | R | NR |
| G-2 Moderate hazard | 2001–3000 m² | HL-4 | R | R | NR | R | R | NR | R | NR |
| G-2 Moderate hazard | Above 3001 m² | CL-5 | R | R | NR | R | R | R | R | NR |
| G-3 High hazard | ≤250 m² | CL-4 | R | R | NR | R | R | R | NR | NR |
| G-3 High hazard | 251–1000 m² | CL-5 | R | R | NR | R | R | R | R | NR |
| G-3 High hazard | Above 1001 m² | CL-6 | R | R | NR | R | R | R | R | R |

**Notes (Table 7G):** 1 — combustible storage/packing, fuel storage, boilers, furnaces present → CL-6 minimum. 2 — where water isn't a suitable agent, use an alternate suppression agent per relevant IS. 3 — oxidizing materials, ignitable liquids, water-reactive chemicals, explosives, aluminium dust, or other explosive environments treated **separately** (not covered by this table's baseline). 4 — supplementary protection per Table 9/10/11. 5 — pump pressure/quantity per hydraulic calc. 6 — cluster >5 → second pump/storage set (max 2). 7 — see Tables 7K/7M.

#### Storage (H) — Table 7H [p.2816–2818]

| Category | Built-up area / ridge height | Class | FE | HR | DC | WR | YH | SP | DA | PA |
|---|---|---|---|---|---|---|---|---|---|---|
| a–e (packaging, raw material, finished goods, misc, retail-shelf storage) | ≤500 m² | HL-4 | R | R | NR | R | NR | NR | R | NR |
| a–e (as above) | 501–1000 m² | HL-5 | R | R | NR | R | R | NR | R | NR |
| a–e (as above) | 1001–2000 m², or ridge ≤7.6 m | CL-6 | R | R | R | NR | R | R | R | NR |
| a–e (as above) | >2001 m², or ridge 7.6–9.0 m | CL-7 | R | R | NR | R | R | R | R | R |
| Any height, with rack storage | — | — | R | R | NR | R | R | R | R | R |

**Notes (Table 7H):** 1 — table applies only to ground-stored goods ≤3.7 m (excl. tyre storage), for categories (a) packaging (b) raw materials (c) finished goods (d) misc storage in manufacturing/assembly/packaging areas (e) retail shelf storage (excl. catwalk) — all also need supplementary protection per Table 9/10/11. 2 — rack storage with plastic/combustible packaging, water-reactive solids/liquids, lithium-battery storage, ignitable chemicals, retail catwalk storage, or oxidizing agents → follow relevant IS, justify pump/storage by hydraulic calc. 3 — cluster >5 → second set (max 2). 4 — see Tables 7K/7M.

#### Hazardous (J) — Table 7J [p.2818–2819]

| Height / Storeys | Class | FE | HR | DC | WR | YH | SP | DA | PA |
|---|---|---|---|---|---|---|---|---|---|
| ≤15 m, single storey | CL-7 | R | R | NR | R | R | R | R | NR |
| ≤15 m, more than one storey | CL-8 | R | R | NR | R | R | R | R | R |

**Notes (Table 7J):** 1 — deploy tailor-made systems (hydrant/sprinkler, dry chemical/powder, water mist, gas/wet-chemical suppression, foam, etc.) per relevant IS/international standards in consultation with local fire services or the AHJ — **this table is a floor, not a substitute for hazard-specific engineering.** 2 — pump pressure/quantity per hydraulic calc. 3 — see Tables 7K/7M.

### G.2 Base Calculations for Protection Systems — Tables 7K & 7M [Cl 5.1.1(a), D-6.1; p.2820–2821]

Feeds the CL/HL classification codes used throughout §G.1 above with actual sprinkler demand, hose-stream flow, and pump sizing.

**Table 7K — Combined system (sprinkler + hose stream):**

| Class | Hazard | Sprinkler demand (mm/min or L/min/m² per source) | Hose stream flow @3.5 bar (lpm) | No. of hose streams | Pump capacity | Duration (min) |
|---|---|---|---|---|---|---|
| CL-1 | Extra Low Hazard-1 | 2.25 | 84 | 50... | 2 | 379 lpm × 1 | 30–60 |
| CL-2 | Extra Low Hazard-2 | 4.1 | 140 | 170 | 2 | 946 lpm × 1 | 30–60 |
| CL-3 | Low Hazard | 6.1 | 230 | 285 | 3 | 1,892 lpm × 1 | 30–60 |
| CL-4 | Moderate Hazard-1 | 8.1 | 230 | 285 | 3 | 2,500 lpm × 1 | 60–120 |
| CL-5 | Moderate Hazard-2 | 12.2 | 230 | 475 | 3 | 3,785 lpm × 1 | 60–120 |
| CL-6 | Extra Hazard-1 | 16.3 | 230 | 475 | 3 | 4,731 lpm × 1 | 60–120 |
| CL-7 | Extra Hazard-2 | 18.3 | 280 | 670 | 4 | 7,570 lpm × 1 | 60–120 |
| CL-8 | High Hazard | 24.5 | 280 | 1,050 | 4 | 4,731 lpm × 2 | 60–120 |

**Pump-capacity worked example (source's own, CL-5):** (12.2 × 230) + (475 × 3) = 4,231 L; +20% overflow = 5,077.2 L; ÷140% = 3,627 lpm → rounds to nearest standard pump, **3,785 lpm**.

**Table 7M — Hose-stream-only system:**

| Class | Hazard | Hose stream flow (lpm) | No. of hose streams | Pump capacity | Duration (min) |
|---|---|---|---|---|---|
| HL-1 | Extra Light-1 | 50 | 4 | 379 lpm × 1 | 30–60 |
| HL-2 | Extra Light-2 | 170 | 4 | 946 lpm × 1 | 30–60 |
| HL-3 | Low Hazard | 270 | 4 | 1,514 lpm × 1 | 30–60 |
| HL-4 | Moderate-1 | 475 | 4 | 2,839 lpm × 1 | 60–120 |
| HL-5 | Moderate-2 | 670 | 5 | 4,731 lpm × 1 | 60–120 |
| HL-6 | Extra Hazard | 670 | 6 | 5,677 lpm × 1 | 60–120 |

**Pump-capacity worked example (HL-3):** 270 × 4 = 1,080 L; +40% overflow = 1,512 L; ÷140% = 1,514 lpm.

**Shared notes (both tables):** "Pump" implies one electric pump **plus a standby of equivalent capacity**, plus a jockey pump for pressure loss. Duration (30–120 min) is chosen per hazard/preparedness/local conditions. Water quantity may instead follow the relevant IS standard directly, where one exists, rather than these tables.

### G.3 Supplementary Protection for Specific Hazard/Critical Rooms — Tables 9, 10, 11 [Cl 3.5.5.4, 5.4, 5.5; p.2833–2839]

These sit **on top of** the occupancy-wide requirements in §G.1 — Table 9's own footnote language and the repeated "supplementary protection per Table 9/10/11" notes throughout §G.1 confirm this is additive, not alternative.

**Table 9 — detection & suppression systems for specific rooms, A–F occupancies** [p.2833–2835]. **S = Suitable, NS = Not Suitable** (this is a *feasibility* matrix, not a requirement matrix — it tells you which system types are viable for a room type, not which are mandatory):

| Room / hazard type | Pneumatic linear heat | Aspiration smoke | Gas/flame/video | Fuel leak | LHS cable | Water mist | Clean agent gas | Water pre-action sprinkler | Modular rack (heat tubing) | Water spray | Wet chemical (kitchen) | Aerosol |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| UPS room, no batteries | NS | S | S | NS | NS | S | S | S | NS | NS | NS | NS |
| UPS room, batteries (not Li-ion) | NS | S | S | NS | NS | S | S | S | NS | NS | NS | NS |
| Battery room, Li-ion | S | S | S | NS | NS | NS | NS | S | NS | S | NS | NS |
| Server room / data hall | NS | S | NS | NS | NS | S | S | S | NS | NS | NS | NS |
| Kitchen, any fuel (live cooking) | NS | NS | S | NS | S | S | NS | NS | NS | NS | NS | NS |
| Network/electrical rooms | NS | S | NS | NS | NS | S | S | S | NS | NS | NS | NS |
| Electrical/MCC panels | NS | S | NS | NS | NS | NS | S | NS | S | NS | NS | S |
| Cable cellar/trenches/trays >1.5 m wide | S | NS | NS | NS | S | S | NS | NS | NS | S | NS | S |
| Dry transformer, indoor | S | NS | S | NS | NS | NS | NS | NS | NS | NS | NS | NS |
| Oil transformer, outdoor >2.0 MVA or 2000 L oil | S | NS | S | NS | NS | NS | NS | NS | NS | S | NS | NS |
| DG rooms | S | NS | S | S | S | S | NS | NS | NS | S | NS | S |
| Cold/freezer rooms | S | S | NS | NS | NS | NS | NS | S | NS | NS | NS | NS |
| MRI/scanning rooms | NS | S | NS | NS | NS | S | NS | NS | NS | NS | NS | NS |
| Operation theatres | NS | S | NS | NS | NS | S | NS | S | NS | NS | NS | NS |
| Tunnel protection | S | NS | S | NS | S | S | NS | NS | NS | S | NS | NS |

**Notes (Table 9):** 1 — wet sprinklers are acceptable wherever pre-action sprinklers or closed water mist are suitable. 2 — DG rooms using water mist need total-flooding open nozzles. 3 — spray systems need suitable foam supplementation where ignitable/water-miscible liquids are present. 4/5 — water-mist and other listed systems must be selected on 3rd-party independent test results and certification for the specific application — **never on prescriptive assumption.**

**Table 10 — special detection systems, G–J occupancies** [p.2836–2837]. S/NS feasibility, columns: Pneumatic linear heat / Flame-gas-spark / High ceiling beam / LHS cable / Probe-type heat / Aspiration smoke:

| Hazard | Pneumatic linear | Flame/gas/spark | Ceiling beam | LHS cable | Probe heat | Aspiration smoke |
|---|---|---|---|---|---|---|
| Generator room | S | S | NS | S | S | NS |
| Water-reactive chemical store | S | S | NS | S | S | NS |
| Chemical store | S | S | NS | S | S | NS |
| Paint booth | S | S | NS | S | S | NS |
| Paint/varnish storage | S | S | NS | S | S | NS |
| Warehouse | NS | S | S | NS | NS | S |
| Above-ground fuel oil storage | S | S | NS | S | NS | NS |
| Oil transformers | S | S | NS | NS | NS | NS |
| Diesel/HSD tanks | S | S | NS | S | NS | NS |
| LPG bullets/Benzene/Xylene/Toluene tanks | NS | NS | NS | NS | NS | NS |
| Airport hangar | S | S | S | S | S | S |
| Hydrogenation rooms | NS | S | NS | S | S | S |
| Sulphur storage | S | S | NS | S | S | NS |
| Tanker loading/unloading bay | NS | S | NS | NS | NS | NS |
| Kitchen | S | S | NS | S | S | NS |
| Conveyors | S | S | NS | S | NS | NS |
| QA/QC labs | S | S | NS | S | S | NS |
| Open large atriums | NS | NS | NS | NS | NS | S |
| Floating roof tanks | S | S | NS | S | NS | NS |
| Oil-fired boiler room / oil quenching tank | S | S | NS | S | S | NS |
| Cooling tower | NS | NS | NS | S | NS | NS |
| MCC room | S | NS | NS | S | S | S |
| Cable cellar/trenches | S | NS | NS | S | S | NS |
| Electrical panels | S | NS | NS | S | NS | NS |

**Table 11 — special suppression systems, G–J occupancies** [p.2838–2839]. S/NS feasibility, columns: Water spray / Wet-dry pre-action / Nitrogen injection / Water mist / Foam sprinkler / Dry powder flooding / Clean agent total flooding / CO₂ flooding:

| Hazard | Water spray | Pre-action | N₂ injection | Water mist | Foam sprinkler | Dry powder | Clean agent | CO₂ flooding |
|---|---|---|---|---|---|---|---|---|
| Generator room | S | NS | NS | S | NS | NS | NS | NS |
| Water-reactive chemical store | NS | NS | NS | NS | NS | S | NS | S |
| Chemical store | S | NS | NS | S | S | NS | NS | NS |
| Paint booth | S | NS | NS | S | NS | NS | NS | NS |
| Paint/varnish storage | S | NS | NS | S | S | S | NS | NS |
| Warehouse | NS | NS | NS | NS | NS | NS | NS | NS |
| Above-ground fuel oil storage | S | NS | NS | NS | S | NS | NS | NS |
| Oil transformers | S | NS | S | S | NS | NS | NS | NS |
| Diesel/HSD tanks | S | NS | NS | NS | S | NS | NS | NS |
| LPG bullets/Benzene/Xylene/Toluene tanks | S | NS | NS | NS | NS | NS | NS | NS |
| Airport hangar | NS | NS | NS | NS | S | NS | NS | NS |
| Hydrogenation rooms | S | NS | NS | S | NS | NS | NS | NS |
| Sulphur storage | NS | NS | NS | S | NS | NS | NS | NS |
| Tanker loading/unloading bay | S | NS | NS | NS | NS | NS | NS | NS |
| Kitchen | NS | NS | NS | S | NS | NS | NS | NS |
| Conveyors | S | NS | NS | S | NS | NS | NS | NS |
| QA/QC labs | NS | S | NS | S | S | S | S | NS |
| Open large atriums | NS | NS | NS | S | NS | NS | NS | NS |
| Floating roof tanks | S | NS | NS | NS | S | NS | NS | NS |
| Oil-fired boiler room / oil quenching tank | S | NS | NS | S | S | NS | NS | NS |
| Cooling tower | S | NS | NS | NS | NS | NS | NS | NS |
| MCC room | NS | S | NS | S | NS | NS | S | S |
| Cable cellar/trenches | S | NS | NS | S | NS | NS | NS | S |
| Electrical panels | NS | NS | NS | NS | NS | NS | S | S |

**Notes (Table 11):** 1 — spray systems need foam supplementation for ignitable/water-miscible liquids. 2 — select the suppression agent per the material's MSDS. 3/4 — water-mist selection must be backed by 3rd-party test/certification, not prescriptive assumption. **5 — oxygen-reduction (inert-atmosphere) systems aren't listed in this table but are a valid proactive option for normally-unoccupied, highly sensitive spaces (heritage archive rooms, critical equipment rooms) — require full 3rd-party certification and AHJ approval, and are unsuitable for occupied spaces.**

### G.4 Key non-tabular checkable numbers from Cl 5.1

| Parameter | Condition | Threshold | Notes |
|---|---|---|---|
| Sprinkler + hydraulic calc trigger | Buildings > 60 m | Hydraulic calcs required, multi-level pumping + storage, gravity down-comer | Pumps ≤ 12 bar shut-off. |
| Cluster buildings | ≤ 5 buildings, ≥ 9 m apart | Common pumping 2 500 lpm at 10 bar + 2,55,000 litre storage | Water storage added every 45 m of height; if buildings are closer than 9 m, or a shared basement is used for EV parking/charging, revert to individual CL-5 protection instead. |
| Dry riser substitution | 24×7 municipal yard-hydrant supply meets demand, OR ambient < 4 °C | Dry riser may replace wet riser | Only for buildings up to 24 m; requires quarterly system-integrity checks. |
| EV parking protection | Podium/basement EV parking | Sprinklers + CL-5 minimum | Rate-of-rise heat detection for EV areas; smoke sensors in all other basement areas; CO sensors + ventilation trigger for ICE-vehicle parking. |
| Water storage tank sharing | Adjacent neighbouring properties, incl. industry clusters | Permitted, without hydraulic-effect loss | Standing remark repeated after every Table 7A–7J. |

## H. Fire Protection Installations [Cl 5.1; p.2822–2839 range]

### Table 8 — Size of Mains [Cl 5.1.1(a); p.2827]

| Main size | Landing valve | Occupancy | Height band |
|---|---|---|---|
| 100 mm | Single 63 mm | Residential — dormitories | Any height |
| 100 mm | Single 63 mm | Residential — apartments | Up to 15 m |
| 100 mm | Single 63 mm | Residential — hotels | Up to 15 m |
| 100 mm | Single 63 mm | Educational | Up to 15 m |
| 100 mm | Single 63 mm | Institutional | Up to 15 m |
| 100 mm | Single 63 mm | Assembly | Up to 15 m |
| 100 mm | Single 63 mm | Business | Up to 15 m |
| 100 mm | Single 63 mm | Mercantile | Up to 9 m |
| 100 mm | Single 63 mm | Industrial | Up to 9 m |
| 150 mm | Single 63 mm | Hotels | Above 15 m |
| 150 mm | Single 63 mm | Starred hotels | Any height |
| 150 mm | Single 63 mm | Institutional | Above 15 m |
| 150 mm | Single 63 mm | Business | Above 15 m |
| 150 mm | Single 63 mm | Industrial | 9–15 m *(reads as a continuation of the 100mm band's 9m cutoff above — not independently confirmed for what governs beyond 15 m; that likely falls to the >60m hydraulic-calc provision instead)* |
| 150 mm | Single 63 mm | Storage | Up to 15 m |
| 150 mm | Single 63 mm | Hazardous | Up to 15 m |

**Verified 2026-09-11 against a clean re-extraction of the source table — this replaces the earlier flag** ("the source's own prose summary of Table 8 reads ambiguously"), which was a limitation of the first-draft transcription, not the source itself.

| Parameter | Condition | Threshold | Notes |
|---|---|---|---|
| Hose reel diameter | First-aid hose reel | **≥ 19 mm** | Connected directly to riser/down-comer main. |
| Hydrant pressure | At the hydraulically remote hydrant and the highest hydrant | **≥ 3.5 bar, and must not exceed 7.0 bar** | Both bounds are hard limits — orifice plates/pressure-reducing devices needed at lower levels to stay under 7.0 bar. |
| Hydrant/hose reel placement | Floor hydrants near a fire-exit staircase | **Within 5 m** of the fire-exit door | |
| Underground fire water tank depth | From the fire-brigade draw-out connection level | **≤ 7 m** deep | Draw-out connection ≤ 5 m from the tank wall. |
| Tank cover slab load | On a fire-apparatus driveway | Withstand **45 tonne** vehicular load, 4-point | |
| Pump house location | Below ground | First basement preferred, **never below second basement** | Access via staircase or 120 min enclosed passageway; no negative-suction, no submersible pumps. |
| Sprinkler false-ceiling trigger | False-ceiling void | **> 800 mm** height → sprinklers required in the void | |
| Sprinkler system pressure | Any | **Must not exceed 12 bar** | Else requires high-pressure sprinklers instead. |
| Max area per sprinkler riser | Any floor | **4 500 m²** per riser/control valve | **Exception: industrial/hazardous has no fixed number — "consult Authorities" per the source.** Don't invent a substitute figure for those occupancies. |

## I. Occupancy-Specific Fire Prevention/Protection Rules [Cl 6.1–6.9; p.2840–2851]

Non-egress items from the same occupancy sections whose egress-only content is in [[Egress Ruleset - Part F]] §K.

| Occupancy | Parameter | Threshold | Notes |
|---|---|---|---|
| Residential A-IV (hotels) | Sprinklers, guest rooms/suites | Extended-throw or quick-response type **only** | Also audio-based detectors ≥ 75 dB. |
| Residential A-I | Flammable-liquid storage areas | **120 min** walls + fire doors marked 'FIRE DOOR — KEEP CLOSED' | |
| Assembly, mixed-use (malls) | Separation, assembly/mercantile portion vs. business/residential above 30 m | **240 min** | Cross-refs [[Egress Ruleset - Part F]] §K.4's independent-exit requirement for the same condition. |
| Assembly | Stage with fly galleries | Sprinklers over/under stage + fire-resisting proscenium curtain (withstand 4 kN/m² lateral, power-free emergency close) | Stage roof ventilator ≥ 1/8 of stage floor area. |
| Assembly (mall-like) | Car parking at upper levels adjacent to shops/food court/multiplex | **120 min** separation | |
| Business | Labs/clinics/libraries | Detection + CO2/foam-based fire protection | |
| Business | Datacentres, IT/telecom/broadcast/ATC | Detection + clean agents/mist; electrical panels CO2/inert gas flooding | |
| Industrial | Fire separating wall between hazard zones | **120 min**; petrochemical/explosives zones **240 min** | Screen wall (roof extension) ≥ 600 mm high, horizontal gap ≥ 6 m between segregated roofs; thickness ≥ 230 mm masonry / ≥ 150 mm RCC extension. |
| Industrial | Openings within 3 m of a fire separating wall | **≥ 60 min** fire doors/fire-resistant glass | |
| Industrial | Moderate/high-hazard storage | Two fire doors, each **180 min** | |
| Industrial | High-hazard occupancy | Automatic sprinkler protection **mandatory**, incl. explosion venting where applicable | |
| Storage/Hazardous | Volatile flammable substance rooms | No spark/glow/flame-generating device unless flameproof-enclosed; exhaust ventilation per Annex K | |
| Hazardous (Group J) | Wall vents | **≥ 100 cm²** each, near floor line, **≤ 1 800 mm apart** horizontally | Power-driven exhaust: full air change every 3 min. |

## J. Refuge Spaces & Refuge Areas — Annex D-4.2 [p.2872–2873]

Already pulled and delivered as a highlighted source page during live testing (2026-09-11) — formalised here.

| Parameter | Condition | Threshold | Notes |
|---|---|---|---|
| Refuge space | In firefighting-shaft lift lobby | **12 m², or 5% of floor occupants × 0.45 m²/person, whichever is higher** | This is the baseline requirement — applies regardless of the 24 m threshold below. |
| Refuge area | Buildings > 24 m | Two consecutive floors' occupants × **0.3 m²/person** + wheelchair space (0.9 m² per 200 occupants), or **15 m² minimum**, whichever is higher | On the periphery, open to air ≥ 1 side, sprinklered throughout, signed, kept clear. Provided at/immediately above 24 m, then every 15 m. |
| Refuge area exemption | High-rise apartments **with balconies** | **Not required at all** | Apartments **without** balconies must still provide refuge spaces or areas. |
| **⚠ Unresolved in the source** | Apartments with balconies, height **> 60 m** | Text says "when refuge areas are **preferred** over refuge spaces... should be provided around 60 m then every ~30 m" | Ambiguous whether this **overrides** the balcony exemption (mandatory above 60 m regardless of balcony) or is a **conditional** spacing rule for whoever chooses to provide one anyway. Confirmed with the maintainer as an AHJ-confirmation point (2026-09-11) — don't present either reading as settled. |

## K. Other Annex D — High-Rise Provisions [p.2872–2878]

| Parameter | Condition | Threshold | Notes |
|---|---|---|---|
| Firefighting shaft count | Residential tower / educational block / compartment of institutional/assembly/business/mercantile | **≥ 1** per unit; **≥ 3 compartments → ≥ 2 shafts** | |
| Door-opening force | Buildings > 60 m | **≤ 133 N** | |
| Sprinkler feed redundancy | Residential > 120 m; other occupancies > 60 m | Main + alternate/standby riser | |
| Height 150–175 m | Same | Fire water storage + pumps at 160–180 m and intermediate levels, each ≥ half the underground tank | One working + one standby pump, **2 850 lpm**; pump room 120 min. |
| Fire & life safety audit | All high-rise buildings | Mandatory, **third-party auditor, every 2 years** | |
| Helipad | Buildings > 200 m | Recommended | Helideck foam: low-expansion AFFF at 10 lpm/ft² for 10 min. |

## L. Annex E — Atrium [p.2881]

| Parameter | Condition | Threshold | Notes |
|---|---|---|---|
| Construction type | Atrium | **Type 1 or Type 2 only** | |
| Ceiling sprinklers | Ceiling > 17 m above floor | **Not required** at the atrium ceiling itself | Sprinklers still wet adjoining glass at 450–600 mm spacing. |
| Smoke extraction rate | Business occupancy | **6 ACPH** | Hotels & assembly: **8 ACPH**. For a height of 15 m from the top. |
| Smoke-layer interface | Any atrium | Kept **≥ 1 800 mm above the highest occupied floor** | For 1.5× egress time or 20 min, whichever is greater. |

## M. Annex F — Data Centres [p.2882–2887]

| Parameter | Condition | Threshold | Notes |
|---|---|---|---|
| Water routing | Data centre / UPS / comms rooms | **No water sources or pipelines** routed through or above | |
| Basement limit | Data centre building | **≤ 2 basements**, within the building line, total area ≤ ground-floor area | |
| Construction type | Data centre | **Type 1 only**; ground coverage ideally ≤ 60% | |
| Staircases | Data-centre-specific | Enclosed, fire-rated, positively pressurised, **≥ 1.5 m wide, 2 required** | Admin-building staircases follow the general Cl 4 rule (min 2) instead. |
| Suppression | Data halls, incl. under-floor/overhead | Clean agent (ozone-friendly, no residue) | Integrated with fire alarm + BMS. |

## N. Annex G — Car Parking [p.2885–2888]

| Parameter | Condition | Threshold | Notes |
|---|---|---|---|
| Separation from other use | Parking within/above/below/attached-to/within 3 m of another-use building | **120 min** walls and floors | Excludes cashier/attendant/toilet spaces ≤ 200 m² total. |
| Open-parking classification | Wall openings | **≥ 0.4 m² per linear metre** of exterior perimeter, over ≥ 40% of perimeter or 2 opposing sides; interior wall lines ≥ 20% open | Else classified as enclosed (triggers compartmentation). |
| Enclosed parking sprinklers | Any | Standard-response, **min K-factor 80, 9 m² coverage** | |
| Automated/mechanical/robotic parking sprinklers | All basements | **≥ K 115** quick-response, **≥ 2 per vehicle**, **≤ 7.2 m² coverage** each, area of operation **≥ 230 m²** | Applies to ICE + electric + hybrid. |
| Electric/hybrid stack parking | Any | **Not permitted** at any level | Absolute prohibition, not a design-around. |
| EV charging location | Basement | **Never below first basement** | Preferred at ground level; basement EV parking + charging compartment max **1 000 m²**. |

## O. Annex H — Metro Stations [p.2888–2921]

| Parameter | Condition | Threshold | Notes |
|---|---|---|---|
| Occupancy classification | Metro station | **Assembly occupancy**; Type 1 or Type 2 construction only | Non-transit occupancy within the station capped at ≤ 300 m². |
| Platform clearance time | Enclosed station | **≤ 4 min** | Open station: ≤ 5.5 min. **This is a different metric from the one below — don't conflate them.** |
| Remotest-person-to-safety time | Enclosed station | **≤ 6 min** | Open station: ≤ 8 min. |
| Max platform travel distance | To a means-of-egress route | **≤ 100 m** | |
| Stairway width, unenclosed | Unidirectional | **≥ 1 800 mm** | Bidirectional: ≥ 2 400 mm. Enclosed: ≥ 1 200 mm. |
| Escalator egress credit | Any | **≤ half** the egress capacity per level counted | Assume one out of service (worst case); a stopped escalator counts as a 1 m staircase. |
| Lifts as egress | Any | ≤ 50% of required capacity; min 60 min fire resistance (shaft 120 min) | One out of service + one reserved for fire service. |

## P. Annex K — Venting in Industrial Buildings [p.2913–2919]

Applies only to **single-storey factories/warehouses with large undivided floor areas.**

| Parameter | Condition | Threshold | Notes |
|---|---|---|---|
| Automatic fire vent trigger | Industrial/storage, moderate hazard or above | Floor area **> 750 m²** | Sprinklers (where provided) operate before vents. |
| Vent area ratio | Low heat release (G-1) | **1:150** | Moderate (G-2): 1:100. High (G-3): 1:30–1:50. |
| Min vent opening | Any | **≥ 1.25 m** in any direction | |
| Max vent spacing | Low hazard | **45 m** | Moderate: 36–37 m. High: 22.5–30 m. |

## Q. Annex M — Performance-Based Design [p.2919–2922]

| Parameter | Condition | Threshold | Notes |
|---|---|---|---|
| Eligibility | **Heritage buildings only**, where prescriptive exits would damage the heritage fabric | Route available with a registered professional; AHJ makes final determination | Every other case needs state fire-authority approval instead — this is not a general alternative-compliance path. |
| Acceptance criterion | Egress safety | **ASET > RSET**, via validated evacuation modelling | |
| Tenability, at 1.8 m above floor | Asphyxiant/irritant gases | **FED < 0.3, FEC < 0.3** | Convective heat ≤ 60 °C air temp; radiant heat ≤ 2.5 kW/m²; visibility ≥ 5–10 m through smoke. |

## S. Annex A — Calorific Values of Common Materials [p.2851–2853] (Table 12)

Guidance figures (Cl 3.1.8) for estimating fire load. Wood equivalent = calorific value ÷ 17.6×10³ kJ/kg (wood's own value), i.e. "how many kg of wood this material's heat release equals." Full ~80-material table, grouped as in the source:

**Solid fuels** (10³ kJ/kg, wood-equiv kg/kg): Anthracite 28.6/1.66 · Bituminous coal 30.8/1.75 · Charcoal 28.4/1.61 · Coke (avg) 27.5/1.56 · Peat 20.9/1.19 · Sub-bituminous coal 22.0/1.25 · Wood (hard/soft) 17.6/1.00

**Hydrocarbons:** Benzene 39.6/2.25 · Butane 47.1/2.68 · Ethane 49.1/2.79 · Ethylene 47.7/2.71 · Fuel oil 41.6/2.36 · Gas oil 42.9/2.44 · Hexane 44.9/2.55 · Methane (natural gas) 52.8/3.00 · Octane 45.3/2.58 · Paraffin 39.6–44.0/2.3–2.5 · Pentane 46.0/2.61 · Propane 47.3/2.69 · Propylene 46.2/2.63

**Alcohols:** Ethyl alcohol 28.4/1.61 · Methyl alcohol 21.1/1.20 · Propyl alcohol 31.9/1.81

**Polymers:** Casein 23.1/1.31 · Cellulose 16.5/0.94 · Cellulose acetate 17.8/1.01 · Polyethylene 48.4/2.75 · Polypropylene 48.4/2.75 · Polystyrene 41.8/2.38 · Polyvinylchloride 20.9/1.19 · Polymethyl methacrylate 24.6/1.40 · Polyurethane 35.2/2.00 · Polyamide (nylon) 22.0/1.25 · Polyester 22.0/1.25

**Common solids:** Asphalt 38.3/2.13 · Bitumen 33.4/1.90 · Carbon 32.1/1.83 · Cotton (dry) 15.8/0.90 · Flax 14.3/0.81 · Furs & skins 18.7/1.06 · Hair (animal) 20.9/1.19 · Leather 17.6/1.00 · Ozokerite (wax) 43.5/2.46 · Paper (avg) 15.4/0.88 · Paraffin wax 40.9/2.33 · Pitch 33.0/1.88 · Rubber 37.4/2.13 · Straw 13.2/0.75 · Tallows 37.6/2.14 · Tan bark 20.9/1.19 · Tar (bituminous) 35.2/2.00 · Wool (raw) 21.6/1.23 · Wool (scoured) 19.6/1.11

**Foodstuffs:** Barley 14.1/0.80 · Bran 11.0/0.63 · Bread 9.9/0.56 · Butter 29.5/1.68 · Cheese (Cheddar) 18.1/1.03 · Corn meal 14.1/0.80 · Flour 14.1/0.80 · Margarine 29.5/1.68 · Oatmeal 15.8/0.90 · Rice 13.9/0.79 · Soya bean flour 16.1/0.91 · Sugar 15.4/0.88 · Whole wheat 14.3/0.81

**Miscellaneous:** Acetone 29.7/1.69 · Acetaldehyde 25.1/1.43 · Formaldehyde 17.6/1.00 · Hydrogen 134.2/7.63 · Magnesium 24.0/1.36

*Note: 1 kJ ≈ 1 Btu, so these figures also read as Btu/kg.*

## T. Annex B — Industrial Occupancy Fire Hazard Classification [p.2854–2857]

Cl 3.1.8. Three-tier classification (G1 Low / G2 Moderate / G3 High); G3 splits into Sub-category A (flammable-liquid/gas and combustible-storage risk) and Sub-category B (bulk gas/chemical plant — the most severe). **NOTE 1 (source):** any occupancy not listed here is classified by resemblance to the nearest listed one — this is not an exhaustive list. **NOTE 2:** chemical-hazard/pollution classification is separate — refer state/central guidelines for that, this table is fire-hazard only.

**G1 — Low Hazard:** Abrasive Mfg · Aerated Water Factories · Agarbatti Mfg · Areca/Betel nut slicing · Analytical/QC Labs · Athletic Equipment Mfg · Asbestos Steam Packing & Lagging Mfg · Automobiles & other motor vehicles · Breweries · Brick Works · Canning Factories · Cardamom Factories · Cement/Asbestos/Concrete Products Mfg · Ceramic/Crockery/Stoneware Pipe Mfg · Clay Works · Clock & Watch Mfg · Coffee Curing/Roasting/Grinding · Condensed Milk/Milk Pasteurizing/Dairies · Confectionery Mfg · Cooling Towers · Electric Generating Houses (Hydroelectric) · Incandescent/Fluorescent/TV Picture Tube Mfg · Electro-plating Works · Engineering Workshops · Fruits/Vegetables Dehydrating & Drying · Fruit Products & Condiment Factories · Garages · Glass & Glass Fibre Mfg · Godowns/Warehouses (non-combustible goods only) · Green houses · Gold Thread/Gilding Factories · Gum/Glue/Gelatine Mfg · Ice/Ice Candy/Ice-cream Mfg · Ink (excl. Printing Ink) Factories · Mica Products Mfg · Multiple-block apartment buildings · Open Large Atriums · Pottery Works · Poultry Farms · QA/QC Laboratories · Salt Crushing Factories & Refineries · Stables · Sugar Candy Mfg · Tanneries/Leather Goods Mfrs · Umbrella Assembling Factories · Vermicelli Factories · Water Treatment/Filtration Plants & Pump Houses · Zinc/Copper Factories

**G2 — Moderate Hazard:** Aluminium Factories · Atta & Cereal Grinding units · Auto Components (excl. plastics/foam) Mfg · Bakeries & Biscuit Factories · Beedi Factories · Bobbin Factories · Bookbinders/Envelopes/Paper bag Mfg · Cable Mfg · Camphor Boiling · Candle Works · Carbon Paper/Typewriter Ribbon Mfg · Cardboard Box Mfg · Carpenters/Wood wool/Furniture Mfg · Carpet & Durries Factories · Cashewnut Factories · Chemical Mfg (flash point above 23 °C) · Chemical Store (non-water-reactive) · Cinema Films & TV Production Studios · Cigar & Cigarette Factories · Coal/Coke/Charcoal Ball & Briquettes Mfg · Coir Factories · Coir Carpets/Rugs/Tobacco/Hides & Skin Presses · Cold storage premises · Cold Freezer Room · Collieries · Conveyors · Cork products Mfg · Cotton Seed Cleaning/De-linting Factories · Distilleries · Dry Cleaning/Dyeing/Laundries · Duplicating/Stencil Paper Mfg · Electric substations/Distribution stations · Electric Generating stations (other than underground power houses) · Electric Lamps Mfg · Electrical Appliances Mfg · Electrical/Motor Control Centre (MCC) Panel Rooms · Electronic Products Mfg · Enamelware Factories · Filter & Wax paper Mfg · Flour Mills · Food Processing establishments · Garment Makers · Ghee Factories (other than vegetable) · Godowns/Warehouses (other than light/high-hazard A) · Grain/Seeds Disintegrating/Crushing Factories · Grease Mfg · Hosiery/Lace/Embroidery/Thread Factories · Incandescent Gas Mantle Mfg · Indoor Dry Transformer Room · Industrial Gas Mfg (inert/halogenated hydrocarbon gases) · Kitchen with any fuel (live cooking) · MRI/scanning room · Man-made Yarn/Fibre Mfg (other than acrylic) · Manure & Fertilizer Works (blending/mixing/granulating) · Mattress & Pillow Making · Mineral Oil Blending & Processing · Multiple-block business buildings · Multiple-block star hotel buildings · Musical Instruments Mfg · Network/electrical room · Oil & Leather Cloth Factories · Oil Terminals/Depots (other than High Hazard A) · Open storage of flammable liquids (drums/cans) · Operation Theatre Rooms · Optical Goods facilities · Oxygen Plants · Paper & Cardboard Mills (without raw material yards) · Pharmaceuticals · Piers/Wharves/Jetties/Dockyards (other than High Hazard A) · Plastic Goods Mfg · Plywood/Wood Veneering Factories · Printing Press Premises · Pulverising & Crushing Mills · Rice Mills · Rope Works · Rubber Goods Mfg · Rubber Tyres & Tubes Mfg · Semiconductors Mfg · Sulphur Storage · Sugar Factories & Refineries · Shellac Factories · Silk Filatures · Soaps & Glycerine Factories · Solar Cells & Modules Mfg · Sponge Iron Steel Plants (gas-based) · Starch Factories · Tea Factories · Textile Mills · Tobacco (Chewing) & Pan-Masala Making · Tobacco Grinding & Crushing · Tobacco Redrying Factories · UPS Room without batteries · Woollen Mills

**G3 — High Hazard, Sub-category (A):** Aircraft Hangers units · Aluminium/Magnesium Powder Plants · Auto Components (incl. plastics & foam) · Automobiles/motor vehicles powered by Lithium/Li-Ion Batteries Mfg · Battery Charging/Service Stations · Battery Mfg · Bituminized Paper/Hessian Cloth/Tar Felt Mfg · Chemical Store (water-reactive) · Cotton Waste Factories · Celluloid Goods Mfg · Chemical Mfg (flash point below 23 °C) · Cigarette Filter Mfg · Diesel Generator Room · Fire-works Mfg · Foam Plastics Mfg/Converting Plants · Godowns/Warehouses (storing combustible/flammable goods) · Grass/Hay/Fodder/Bhoosa Pressing Factories · Hydrogenation rooms (flammable hydrogen) · Industrial Gas Mfg (other than inert/halogenated hydrocarbon) · Jute mills & jute presses · Linoleum Factories · Lithium-Ion Battery Mfg Plants · LPG Bottling Plants (Mini) · Man-made Fibres (Acrylic) Mfg · Match Factories · Metal/Tin Printers (>50% floor area as Engineering Workshop → treat as Ordinary Hazard Risk) · Oil Mills · Oil Extraction Plants · Oil Fire Boiler Room/Oil Quenching Tank · Oil Terminals/Depots (flash point ≤23°C) · Oil Transformer Room · Paints & Varnish Factories · Paint Booths · Paint/Varnish Storage · Paper & Cardboard Mills (with raw material yards) · Piers/Wharfs & Jetties — Handling Extra Hazardous Materials · Printing Ink Mfg · Rosin Lamp black & Turpentine Factories · Saw Mills · Spray painting facilities · Server room · Surgical Cotton Mfg · Tanker Loading/Unloading Bay · Tarpaulin & Canvas Proofing Factories · Turpentine & Rosin Distilleries · Tyre Retreading & Resoling Factories · Tunnel Protection · UPS Room with batteries · Battery Room with Lithium-ion batteries

**G3 — High Hazard, Sub-category (B) — most severe:** Ammonia & Urea Synthesis Plants · Benzene/Xylene/Toluene Tanks · CNG Compressing & Bottling Plants · Coal-based Methane Plants · LPG bullets · Explosive Factories · Oil Storage (above ground) · Outdoor Oil Transformer Room

*NOTE (source): where a complex has separate plants of varying hazard, the AHJ decides the level of protection to apply.*

## U. Annex C — Fire Resistance Rating of Building Components [p.2858–2871] (Tables 13–29)

Cl 3.4.2, 3.4.3, F-2.1. Guidance minimum dimensions/thicknesses where no validated/certified rating exists. **Correction: the actual page range is 2858–2871 (14 pages), not 2858–2891 as earlier logged in [[Active Priorities]]** — Annex D (High Rise Buildings) starts at p.2872 and was already covered in §Annexes D–N built 2026-09-11. Every table below was verified against rendered source-page images (not just linear text extraction) — this Annex carries the same dense-numeric-grid risk as IS 875's tables, and one real extraction gap was caught: a Table 14 row's values were initially incomplete/misordered from linear text, corrected from the image. Figures are minimum **mm**, values listed in the fire-resistance-time order the source gives (stated per table); "–" = not applicable/no data at that rating.

**Table 13 — Masonry Walls, Solid** (LB & NLB at 60/90/120/180/240 min):
- RCC (≥1% vertical reinft): LB 120/140/160/200/240 (cover 25mm all ratings); NLB n/a
- Unreinforced cement concrete: LB 150/175/–/–/–; NLB n/a
- No-fines concrete (13mm cement/sand or gypsum/sand finish, either type): LB n/a; NLB 150 flat across all 5 ratings
- Bricks of clay — no finish: LB 90/100/100/170/170, NLB 75/90/100/170/170; +13mm LWA gypsum plaster: LB 90/90/90/100/100, NLB 75/90/90/90/100
- Bricks of sand lime — no finish: LB 90/100/100/190/190, NLB 75/90/100/170/170; +13mm LWA gypsum plaster: LB 90/90/90/100/100, NLB 75/90/90/90/100
- Blocks of concrete — no finish: LB 90/100/100/–/–, NLB 75/90/100/140/150; +13mm LWA gypsum: LB 90/90/90/100/100, NLB 75/75/75/90/100; +13mm cement/sand or gypsum/sand: LB n/a, NLB 75/90/90/100/140
- Blocks of lightweight concrete — no finish: LB 90/100/100/140/150, NLB 75/75/75/125/140; +13mm LWA gypsum: LB 90/90/90/100/100, NLB 50/63/75/75/75; +13mm cement/sand or gypsum/sand: LB n/a, NLB 75/75/75/90/100
- Blocks of aerated concrete — no finish: LB 90/100/100/140/180, NLB 50/63/63/75/100; +13mm LWA gypsum: LB 90/90/100/100/150, NLB n/a

**Table 14 — Masonry Walls, Hollow** (LB at 60/90/120/180/240; NLB at 30/60/90/120/180/240):
- Bricks of clay — no finish: LB 170/170/170/200/200, NLB 75/75/90/100/170/170; +13mm LWA gypsum plaster: LB 170/170/170/200/200, NLB 75/75/90/100/170/170
- Blocks of concrete — no finish: LB n/a, NLB 90/125/125/140/140/150; +13mm cement/sand or gypsum/sand: LB n/a, NLB 90/125/125/140/140/140; +13mm LWA gypsum plaster: LB 190/200/200/–/–, NLB 75/90/90/100/125/125
- Blocks of lightweight concrete — no finish: LB 100/100/100/–/–, NLB 75/90/90/100/140/150; +13mm cement/sand or gypsum/sand: LB n/a, NLB 75/75/75/100/140/140; +13mm LWA gypsum plaster: LB n/a, NLB 63/63/63/75/90/100

**Table 15 — Framed Construction, Load Bearing** (single rating, 60 min): plasterboard layers staggered, taped/filled = 25mm total/face · one 12.7mm plasterboard + LWA gypsum finish = 13mm · metal lath+plaster: sanded gypsum 22mm, LWA gypsum 13mm.

**Table 16 — Framed Construction, Non-Load Bearing** (30/60/90/120 min; Timber(T)/Steel(S) both unless noted): dry lining no plaster — 1 layer plasterboard taped/filled 12.7/–/–/–; 2 layers staggered 19/25/–/–; asbestos insulating board 9/12/–/–; wood wool slabs (Timber only) 25/–/–/–; chipboard/plywood 18/–/–/–. Lining w/ plaster finish — plasterboard 5mm gypsum finish 9.5/–/–/–; 13mm gypsum finish –/12.7/–/–. Wet finish, metal lath+plaster — sanded gypsum 13/–/–/–; LWA gypsum: Timber –/13/19/25, Steel –/13/–/–.

**Table 17 — Framed External Walls, Load Bearing** (60 min only): timber studs + plasterboard layers, outer joints taped/filled = 31mm total.

**Table 18 — Framed External Walls, Non-Load Bearing, fire from inside (A)** (30/60/90/120/180/240 min), steel frame + non-combustible cladding: metal lath+plaster sanded gypsum 13/13/–/–/–/–, LWA gypsum 10/13/15/15/15/19 · 2-layer plasterboard staggered 21/32/–/–/–/– · plasterboard 5mm gypsum finish 12.7/–/–/–/–/–, 13mm gypsum finish 9.5/–/–/–/–/–, 10mm LWA gypsum 9.5/–/–/–/–/– · asbestos insulating board 9/9/12/12/12/12 · wood/wool slabs –/50/–/–/–/– · compressed straw slabs (no finish) 50/–/–/–/–/–, (+5mm gypsum) –/50/–/–/–/– · aerated concrete blocks 50/50/63/63/75/100 · bricks of clay (no finish) 75/75/90/90/100/100, (+13mm LWA gypsum) –/–/75/75/90/90.

**Table 19 — Framed External Walls, Non-Load Bearing, fire from inside (B)** (single rating, up to 240 min), steel frame + sheet-steel cladding: metal lath sanded gypsum 13, LWA gypsum 10 · 1-layer plasterboard taped/filled 12.7 · plasterboard 5mm gypsum finish 9.5 · asbestos insulating board 9 · wood/wool slabs 25 · compressed straw slabs 50 · chipboard/plywood 18 · aerated concrete blocks 50 · bricks of clay 75 · mineral-fibre cavity fill (48 kg/m³, excl. glass) 50.

**Table 20 — Framed Walls, Non-Load Bearing, fire from inside (C)** (single rating, 90 min), timber frame + weatherboard/plywood cladding: plasterboard ≥9.5mm, gypsum plaster 13 / LWA gypsum 10; plasterboard ≥12.7mm, gypsum plaster 10 / LWA gypsum 10; asbestos insulating board 9 or 12 (source gives both figures against the same row without distinguishing sub-condition — flagged, not resolved further).

**Table 21 — Reinforced Concrete Columns** (30/60/90/120/180/240 min): fully exposed — width 150/200/250/300/400/450, cover 40 flat throughout. 50% exposed — width 125/160/200/200/300/350, cover 40 flat throughout. One face exposed — thickness 100/120/140/160/200/240, cover 40 flat throughout.

**Table 22 — Concrete Beams** (30/60/90/120/180/240 min; ¹ = spalling mitigation required): RC simply supported — width 200/200/200/200/240/280, cover 20/20/20/40/60¹/70¹. RC continuous — width 200/200/200/200/240/280, cover 20/20/20/30/40/50¹. Prestressed simply supported — width 100/120/150/200/240/280, cover 25/40/55¹/70¹/80¹/90¹. Prestressed continuous — width 80/100/120/150/200/240, cover 20/30/40/55¹/70¹/80¹.

**Table 23 — Concrete Floors** (30/60/90/120/180/240 min; ¹ = spalling mitigation required): RC simply supported — thickness 75/95/110/125/150/170, cover 20/20/25/35/45¹/55¹. RC continuous — thickness 75/95/110/125/150/170, cover 20/20/20/25/35/45¹.

**Table 24 — Concrete Floors, Ribbed Open Soffit** (30/60/90/120/180/240 min; ¹ = spalling mitigation required): RC simply supported — floor thickness 75/95/110/125/150/170, rib width 125/125/125/125/150/175, cover 20/20/35/45¹/55¹/65¹. RC continuous — thickness 75/95/110/125/150/170, width 125/125/125/125/150/175, cover 20/20/20/35/45¹/55¹.

**Table 25 — Encased Steel Columns, 203×203mm** (60/90/120/180/240 min, Cl 3.4.3): hollow protection, no air cavity over flanges — metal lathing+LWA gypsum plaster 13/15/20/32/– · plasterboard+wire binding (9.5mm board) 10/15/–/–/–, (19mm board) 10/13/20/–/– · asbestos insulating boards (single, 6mm cover fillets) –/19/25/–/–, (two layers) –/–/–/38/50 · solid brick/sand-lime (reinforced joints, plastered) 50/50/50/75/100 · aerated concrete blocks 60/60/60/–/– · solid lightweight-concrete blocks 50/50/50/60/75. Hollow, with air cavity over flanges — asbestos board on 25mm battens 12/19/–/–/–. Solid protection — concrete 1:2:4 unplastered, not load-bearing (reinforced) 25/25/25/50/75, load-bearing 50/50/50/75/75; lightweight concrete 1:2:4 unplastered, not load-bearing (reinforced) 25/25/25/40/60.

**Table 26 — Encased Steel Beams, 406×176mm, protection on 3 sides** (30/60/90/120/180/240 min, Cl 3.4.3): hollow, no air cavity beneath lower flange — metal lathing+LWA gypsum plaster 13/13/15/20/25/– · plasterboard+wire binding (9.5mm) 10/10/15/–/–/–, (19mm) 10/10/13/20/–/– · asbestos insulating boards (single, 6mm cover) –/–/19/25/–/–, (two layers) –/–/–/–/38/50. Hollow, with air cavity below lower flange — asbestos board on 25mm battens 9/12/–/–/–/–. Solid protection — concrete 1:2:4 unplastered 25/25/25/25/50/75; **flagged ambiguity:** the source visually attaches this same 25/25/25/25/50/75 row to the "unplastered" header rather than clearly to either the "not load-bearing (reinforced)" or "load-bearing" sub-line below it, sub-line "not load-bearing (reinforced)" separately reads 50/50/50/50/75/75, and "load-bearing" shows no distinct figures at all in the source layout — inconsistent with Table 25's cleaner equivalent structure (reinforced < load-bearing). Pull p.2868 directly before using this cell for a real design. Lightweight concrete 1:2:4 unplastered: 25/25/25/25/40/60.

**Table 27 — Timber Floors, T&G boarding/plywood/chipboard ≥21mm finished thickness** (30/60/120 min), 37mm min timber joists + ceiling: timber lathing+plaster 15/–/– · metal lathing+plaster (sanded gypsum) 15/–/–, (LWA gypsum) 13/13/25 · 1-layer plasterboard taped/filled 12.7/–/– · 2-layer plasterboard staggered 19/31/– · plasterboard ≥9.5mm (gypsum) 5/–/–, (sanded gypsum) 13/–/–, (LWA gypsum) 13/–/– · plasterboard ≥12.7mm (gypsum) 5/–/–, (LWA gypsum) 10/–/– · asbestos insulating board 9/12/–.

**Table 28 — same but ≥15mm finished thickness** (30/60/120 min): timber lathing+plaster 15/–/– · metal lathing+plaster (sanded gypsum) 15/–/–, (LWA gypsum) 13/13/25 · 1-layer plasterboard 12.7/–/– · 2-layer staggered 22/31/– · plasterboard ≥9.5mm (gypsum) 5/–/–, (sanded gypsum) 15/–/–, (LWA gypsum) 13/–/– · plasterboard ≥12.7mm (gypsum) 5/–/–, (LWA gypsum) 10/–/– · asbestos insulating board 9/12¹/– (¹finished on top with ≥25mm glass fibre/mineral wool between joints).

**Table 29 — Timber floors, any structurally suitable timber/lignocellulose flooring** (30/60 min only): timber lathing+plaster 15/– · metal lathing+plaster (sanded gypsum) 15/–, (LWA gypsum) 13/19 · 1-layer plasterboard taped/filled+backed by timber 12.7/– · 2-layer staggered 25/– · 2 layers ≥9.5mm each, outer gypsum finish 5/– · plasterboard ≥9.5mm (sanded gypsum) 13/–, (LWA gypsum) 15/– · plasterboard ≥12.7mm (sanded gypsum) 15/–, (LWA gypsum) 13/– · asbestos insulating board 12/–.

## V. Annex N — Per-Industry Fire Protection Requirements [p.2922–2964] (supplementary to Table 7G)

**Scoping decision (2026-09-12):** Annex N's header marks it **"(Informative)" / "Suggested Requirements"** — lower-stakes guidance, not a mandatory clause like Tables 7A–7M or Annexes A–C. It runs ~43 real pages (2922–2964; pages 2965–2974 are the Part's "List of Standards" IS-number bibliography, not fire-protection rules — reference-only, not reproduced here) and lists **150+ individual industries across 4 appendices**, each row following one of two highly repetitive boilerplate patterns with only occasional deviation. Full verbatim transcription of every row was judged not worth the volume/error-risk for informative content (same call as SP 16/SP 34's large numeric grids) — instead this section captures the **framework + default pattern per hazard tier + every deviation actually found while sampling + a name index with page numbers**, so a specific industry can be looked up fast and pulled by page for exact wording. The index below is not guaranteed 100% exhaustive (a handful of Sl Nos didn't isolate cleanly from linear text — e.g. Appendix 1 jumps xxxvii→xxxix, Appendix 2 has several gaps) — if an industry isn't listed, pull the appendix's page range directly rather than assuming it's absent from the source.

**Framework:** four hazard tiers, aligned with [[#T. Annex B — Industrial Occupancy Fire Hazard Classification|Annex B]]'s G1/G2/G3(A)/G3(B) (Note 13: Annex B's classification is indicative only — actual hydrant/sprinkler design must follow IS 13039/IS 15105). Each tier has an aggregate-built-up-area ladder; above the top band, "see Appendix N" for the full per-industry table.

- **Low Hazard** (Notes 1, 2a, 3, 4, 5, 13): licensed artisan/village/tiny-sector units → extinguishers+buckets only (IS 2190), nothing else required. <500 m² → extinguisher only. 500–<1500 m² → +hose reel, static tank 15,000 L, overhead tank 5,000 L, ground pump (Note 7a: 1 electric main pump ≥450 lpm @ 50m head + standby). 1500–<2500 m² → same package, static tank 25,000 L. **≥2500 m² → Appendix 1** (below). Buildings >9 m not permitted for the two smallest bands (Note 2a).
- **Ordinary Hazard** (Notes 1, 2b, 3, 5, 13): <500 m² → extinguisher+hose reel, static tank 20,000 L, overhead 5,000 L, pump (Note 7b: ≥900 lpm @ 50m). 500–<1500 m² → +yard hydrant, static tank 40,000 L, overhead 10,000 L, pump (Note 7c: ≥1620 lpm @ 70m + standby diesel + 180 lpm jockey pump). 1500–<2500 m² → +wet riser/down-comer, sprinkler, manual fire alarm, static tank 60,000 L, overhead 15,000 L, pump (Note 7c). **≥2500 m² → Appendix 2.** Buildings/plants >18 m generally not permitted (Note 2b, exception for tall process equipment with low occupant load).
- **High Hazard A** (Notes 2c, 5, 13): <1000 m² → full package (extinguisher, hose reel, wet riser, yard hydrant, sprinkler, manual + automatic fire alarm), static tank 75,000 L, overhead 10,000 L, pump (Note 7d: ≥2280 lpm @ 70m + standby diesel + jockey pump). 1000–<2500 m² → same package, static tank 1,00,000 L, overhead 15,000 L. **≥2500 m² → Appendix 3.** Buildings/plants >15 m generally not permitted (Note 2c, same tall-equipment exception).
- **High Hazard B** (Notes 2c, 6) — chemicals, petroleum, gas processing, petrochemicals, fertilizer plants, thermal power plants: **no area ladder — go straight to Appendix 4** at any size, plus compliance with OISD/PESO/PNGRB/OMR/CEA as applicable.
- Mixed-hazard complex → governed by the highest hazard present (Note 3). Multi-occupancy industrial estates in one building → treated as Ordinary, no High Hazard occupancy allowed in such buildings (Note 5). Water-reactive materials → substitute extinguishing system per relevant IS, not water (Note 11). R = Required, NR = Not Required.

**Appendices 1–3 share one 9-column structure** (Sl No · Description · Extinguisher · Hose Reel · Hydrant System · Sprinkler System [Process Blocks / Storage Blocks] · Fire Alarm System · Special Protection), one row per named industry, for facilities ≥2500 m² in that hazard tier. **Default pattern per tier** (most rows follow this unless flagged below):
- **Appendix 1 (Low)** — Extinguisher/Hose Reel/Hydrant all R; Sprinkler (Process) NR; Sprinkler (Storage) required only if packing-material/raw-material godowns exceed 2000 m²; Fire Alarm = manual, whole unit, only if the single largest building exceeds 2000 m²; Special Protection usually blank.
- **Appendix 2 (Ordinary)** — same base, but Sprinkler (Process) becomes required once a single un-compartmented area exceeds 2000 m² (not flat NR like Low Hazard) — the real Low→Ordinary distinction in this table.
- **Appendix 3 (High-A)** — sampled less deeply; Aircraft Hangers (item i) already deviates from any simple default ("Required in full" — pull p.2954 for exact wording), so treat Appendix 3 as needing a page pull per industry rather than assuming a default.

**Named deviations actually found** (not an exhaustive exception list — only what was read directly): Analytical/QC Laboratories (Appendix 1, no pilot plant) — Sprinkler (Process) required if combined floor area >5000 m² (not the 2000 m² godown trigger), Fire Alarm = automatic detection + manual call stations for the whole factory. Granite manufacturing (Appendix 1) — additional manual foam-spray system required where flammable liquids with flash point <65 °C are used. Engineering Workshops – Heavy and – Light (Appendix 1, items xxvi–xxvii) — long compound conditions on raw-material godown sprinklering (>20% of storage value in plastic/rubber) and spot-protection for specific operations (plastic/rubber components, spray painting, flammable-liquid use, wood working, engine testing) exceeding 10% of manufacturing area — pull p.2932–2933 for exact wording before applying.

**Appendix 1 — Low Hazard, ≥2500 m²** [p.2926–2939]. Industries indexed (Sl No — name — approx. source page): i Abrasive Mfg (2926) · ii Aerated Water/Mineral Water Factories (2926) · iii Agarbatti Mfg (2926) · iv Analytical/QC Labs, no pilot plant (2926, deviation above) · v Areca/Betel Nut Slicing (2927) · vi Asbestos Steam Packing & Lagging Mfg (2927) · vii Battery Charging/Service Stations (2927) · viii Battery Mfg (2927) · ix Breweries (2927) · x Brick Works (2927) · xi Canning Factories (2927) · xii Cardamom Factories (2927) · xiii Cement/Asbestos Factories (2928) · xiv Ceramic/Crockery/Stoneware Pipe Mfg (2928) · xv Clay Works (2928) · xvi Clock & Watch Mfg (2928) · xvii Coffee Curing/Roasting/Grinding (2928) · xviii Condensed Milk Factories (2929) · xix Confectionery Mfg (2929) · xx Crockery & Stoneware Pipe Mfg (2929) · xxi Electric Generating Houses (2929) · xxii Electric Lamps Mfg (2929) · xxiii Electric Sub-Station/Distribution (2930) · xxiv Electro Plating Works (2932) · xxv Electronic/Computer Equipment Assembly & Mfg (2932) · xxvi Engineering Workshops – Heavy (2932, deviation above) · xxvii Engineering Workshops – Light (2933, deviation above) · xxviii Fruits/Vegetables Dehydrating & Drying (2934) · xxix Fruit Products & Condiment Factories (2934) · xxx Glass & Glass Fibre Mfg (2934) · xxxi Gold Thread/Gilding Factories (2934) · xxxii Granite Mfg (2934, deviation above) · xxxiii Gum/Glue/Gelatine Mfg (2935) · xxxiv Ice Candy & Ice-Cream Mfg (2935) · xxxv Ice Factories (2935) · xxxvi Ink (excl. Printing Ink) Factories (2935) · xxxvii Laundries (2936) · xxxix Pottery Works (2937) · xl Poultry Farms (2937) · xli Salt Crushing Factories & Refineries (2937) · xlii Sugar Candy Mfg (2938) · xliii Sugar Factories (2938) · xliv Tanneries/Leather Goods Mfrs (2938) · xlv Tea Blending & Packing Factories (2938) · xlvi Umbrella Assembling Factories (2939) · xlvii Vermicelli Factories (2939) · xlviii Water Treatment/Filtration Plants (2939) · xlix Zinc/Copper/Aluminium Factories (2939).

**Appendix 2 — Ordinary Hazard, ≥2500 m²** [p.2940–2953]. Industries indexed: i Airport (2940) · ii Aluminium Factories (2940) · iii Bakeries (2940) · iv Beedi Factories (2940) · v Biscuit Factories (2940) · vi Bobbin Factories (2940) · vii Bookbinders/Envelopes/Paper Bag Mfrs (2941) · viii Cable Mfg (2941) · ix Carbon Paper/Typewriter Ribbon Mfrs (2941) · x Cardboard Box Mfg (2941) · xi Carpenters/Wood Wool/Furniture Mfg (2942) · xii Carpet Mfg (2942) · xiii Chemical Mfg (2942) · xiv Cigar & Cigarette Factories (2943) · xv Coffee Grinding (2943) · xvi Coir/Carpets/Rugs/Tobacco/Hides & Skin (2943) · xvii Cork Products Mfg (2943) · xix Electric Generating (2944) · xx Enamelware Factories (2945) · xxi Filter & Wax Paper Mfg (2945) · xxii Flour Mills (2945) · xxv Grain/Seed Disintegrating (2946) · xxx Industrial Gas Mfg (2949) · xxxi Linoleum Factories (2949) · xxxii Man-made Yarn/Fibre Mfg (2949) · xxxiv Mineral Oil Blending & Processing (2950) · xxxv Oil & Leather Cloth Factories (2951) · xxxvi Oxygen Plants (2951) · xxxvii Plywood Mfg/Wood Veneering (2951) · xxxviii Paper & Cardboard Mills (2951) · xxxix Plastic Goods Mfg — PTFE (2951) · xl Plastic Goods Mfg (2954) · xli Plastic Goods Mfg — other (2954) · xliv Pulverising/Crushing Mills (2954) · xlvi Rope Works (2954) · xlix Silk Filatures (2954) · l Spray Painting (2954) · li Soaps & Glycerine Factories (2954) · lii Starch Factories (2954) · liii Steel Plants (2954) · liv Tanneries/Leather Goods Mfrs (2954) · lv Tank Farms (2954) · lvi Textile Mills (2954) · lix Tobacco Grinding & Crushing (2954) · lx Tobacco Redrying (2954) · lxi Woollen Mills (2954). *(Several Sl Nos between these didn't isolate cleanly — pull the page range for anything not listed.)*

**Appendix 3 — High Hazard A, ≥2500 m²** [p.2954–2960]. Industries indexed: i Aircraft Hangers (2954, deviation above) · ii Aluminium/Magnesium Powder Plants (2954) · iii Bituminized Paper Mfg (2954) · iv Chemical Mfg (2954) · v Cotton Waste Factories (2954) · vi Coal/Coke/Charcoal Ball Briquettes Mfg (2954) · vii Celluloid Goods Mfg (2954) · viii Cigarette Filter Mfg (2954) · ix Cinema Films & TV Production Studios (2954) · x Cotton Seed Cleaning/De-linting (2954) · xi Distilleries (2955) · xii Duplicating/Stencil Paper Mfg (2955) · xiii Fire-works Mfg (2955) · xiv Foamed Plastics (2955) · xv Jute Mills (2955) · xvi LPG Bottling Plants (2955) · xvii Match Factories (2956) · xviii Man-made Fibres, Acrylic (2956) · xix Mattress Mfg (2956) · xx Metal/Tin Printers (2957) · xxi Oil Mills (2957) · xxii Oil Extraction Plants (2957) · xxiii Oil Terminals/Depots (2957) · xxiv Paints & Varnish Factories (2957) · xxv Printing Ink Mfg (2958) · xxvi Saw Mills (2958) · xxvii Solvent Extraction Plants (2958) · xxviii Surgical Cotton Mfg (2958) · xxix Tank Farms (2958) · xxx Tarpaulin & Canvas Proofing Factories (2958) · xxxi Turpentine & Rosin Distilleries (2958) · xxxii Tyre Retreading Factories (2959).

**Appendix 4 — High Hazard B** [p.2961–2964], structured differently: not by industry, but **by plant zone** within chemical/petroleum/gas/petrochemical/fertilizer/thermal-power facilities. 10 columns (Fire Extinguishers/Equipment · Hydrant System/Monitors/Hose Reels · Fire Alarm · Sprinkler · HVLR Monitors · Gas/HC/Fire/Heat Detection · Automatic Heat/Fire Detection & Suppression · Remarks). Zones indexed: i Process Units — columns/reactors etc. (2961) · ii Tank Farm Areas — liquid/gas storage (2961) · iii Pump House Area — pumps/compressors (2961) · iv Loading/Unloading Gantry (2961) · v LPG Filling Stations (2961) · vi Conveyor Belt Areas (2962) · vii Sub-station & Electrical Panels (2962) · viii Chlorination Plant (2962) · ix Transformers (2962) · x Cable Trenches/Racks/Galleries (2962) · xi Quality Control Lab (2962) · xii Admin Building (2963) · xiii Control Room (2963) · xiv Firefighting Pumps & Fire Water System (2963) · xv Fire Tenders — independent fire station, response time specified (2963). **Notes 1–16** [p.2964] set the underlying installation standards: fire-water hydrant/monitor network per OISD at multiple platform levels (N1); sprinklers on technological platforms (N2); elevated variable-flow monitors for tall structures (N3); gas/heat detectors at drain points (N4); fixed foam pourers for Class-A tank storage (N5); water-cooling sprinkler rings on storage tanks (N6); HVLR monitors 500–4000 gpm, 10,500 gpm for tanks >60 m dia, fire robots for multi-tank fires (N7); medium-expansion foam generators for dyke/spill fires (N8); automatic linear heat detection + foam suppression for EFR tank rim seals (N9); linear heat detection + water mist on conveyor belts (N10) and cable cellars/trenches (N11); linear heat detection + inert-gas suppression on electrical panels (N12); chlorine leak kit/suit/sensors/neutraliser (N13); water mist/deluge + nitrogen injection (NIFPS) for oil-filled transformers (N14); wireless heat/smoke detection with alarm notification (N15); clean-agent inert-gas suppression in control rooms (N16).

## R. Large Reference-Only Tables (not converted — pull by page)

Tables 7A–7M and 9/10/11 were converted into full rule tables in §G–H above (2026-09-11); Annexes A, B, C and N were converted in §S–V above (2026-09-12, N as framework + index rather than full verbatim — see §V's scoping note). **Part F's Annexes are now fully covered.** Remaining reference-only material: the Part's "List of Standards" IS-number bibliography (p.2965–2974, not fire-protection rules) and, within Appendices 1–3 of Annex N, the exact verbatim wording of any specific industry row not already flagged as a deviation in §V — pull by page for those.

## Cross-references

- Egress geometry, capacity, staircases, ramps, and the occupancy-specific exit-count overlay → [[Egress Ruleset - Part F]] (separate note — no duplication between the two).
- Parent reference: [[Part F - Fire and Life Safety]].
- Parent plan: Code Design Assistant.
