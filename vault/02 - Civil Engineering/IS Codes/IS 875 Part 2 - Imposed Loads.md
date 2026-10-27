---
status: active
project: civil-engineering
type: reference
---
# IS 875 (Part 2):1987 — Imposed Loads

Third of the five IS 875 parts in Code Design Assistant's roadmap. Source: `<your codes folder>\IS CODES\CED37-Structural safety\875_2.pdf` (20 pages). Extracted text: `<local extracted text>\IS 875\IS-875-Part2-Imposed-Loads-fulltext.txt`.

**This is one of the highest daily-value documents in the whole roadmap** — Table 1 (occupancy floor loads) is used on essentially every building design.

**Audited 2026-09-11.** This was a serious finding, more so than the IS 456 audit: the first draft's Table 1 had real numeric errors (values swapped between adjacent rows, a rate-vs-minimum conflated into one wrong figure for Storage buildings) and was missing roughly half its rows entirely, because it was built from a linear text extraction where the source PDF's two-column table layout doesn't extract in reading order — UDL and concentrated-load values from different rows end up interleaved. Every row below was rebuilt by pulling word-level coordinates (and, for one badly-tangled cell, rendering the actual page as an image) directly from the source PDF rather than trusting the linear extraction — same discipline as the IS 456 Table 15 fix, applied to the whole table this time because the first pass showed the error wasn't a one-off.

## Scope & terminology (Cl 1–2)
Covers imposed ("live") loads from occupancy/use — excludes wind, seismic, snow, and loads from temperature/creep/shrinkage/settlement (those live in Parts 3–5 and IS 1893). **Occupancy classification** mirrors NBC's Groups: Assembly, Business, Educational, Industrial, Institutional, Mercantile, Residential (incl. Dwellings), Storage (Cl 2.2.1–2.2.8).

## Table 1 — Imposed floor loads by occupancy [Cl 3.1; p.7–12]

Both a **UDL** (uniformly distributed load, kN/m²) and a **concentrated load** (kN, over 0.3×0.3 m) are given per row — design for whichever is more adverse, **not both simultaneously**. Where "—" appears for concentrated load, the source gives none (UDL alone governs, per Note 1).

**i) Residential — dwelling houses**

| Space | UDL | Concentrated |
|---|---|---|
| All rooms and kitchens | 2.0 | 1.8 |
| Toilet and bath rooms | 2.0 | — |
| Corridors, passages, staircases incl. fire escapes and store rooms | 3.0 | 4.5 |
| Balconies | 3.0 | 1.5/m run at outer edge |

**i) Residential — dwelling units per IS 8888-1979**

| Space | UDL | Concentrated |
|---|---|---|
| Habitable rooms, kitchens, toilet, bathrooms | 1.5 | 1.4 |
| Corridors, passages, staircases incl. fire escapes | 1.5 | 1.4 |
| Balconies | 3.0 | 1.5/m run at outer edge |

**i) Residential — hotels, hostels, boarding houses, lodging houses, dormitories, residential clubs**

| Space | UDL | Concentrated |
|---|---|---|
| Living rooms, bed rooms, dormitories | 2.0 | 1.8 |
| Kitchens and laundries | 3.0 | 4.5 |
| Billiards room and public lounges | 3.0 | 2.7 |
| Store rooms | 5.0 | 4.5 |
| Dining rooms, cafeterias, restaurants | 4.0 | 2.7 |
| Office rooms | 2.5 | 2.7 |
| Rooms for indoor games | 3.0 | 1.8 |
| Baths and toilets | 2.0 | — |
| Corridors/passages/stairs/lobbies (excl. stores), per floor served, not less than | 3.0 | 4.5 |
| Balconies | same as rooms served, min 4.0 | 1.5/m run at outer edge |
| **Boiler rooms and plant rooms**, calculated, not less than | 5.0 | 6.7 |

**Garages**

| Space | UDL | Concentrated |
|---|---|---|
| Cars/vehicles ≤ 2.5 t gross (incl. access/ramps), calculated, not less than | 2.5 | 9.0 |
| Vehicles ≤ 4.0 t gross (incl. access/ramps), calculated, not less than | 5.0 | 9.0 |

**ii) Educational**

| Space | UDL | Concentrated |
|---|---|---|
| Classrooms/lecture rooms (not for assembly) | 3.0 | 2.1 |
| Dining rooms, cafeterias, restaurants | 3.0† | 2.7 |
| Offices, lounges, staff rooms | 2.5 | 2.7 |
| Dormitories | 2.0 | 2.7 |
| Projection rooms | 5.0 | — |
| Kitchens | 3.0 | 4.5 |
| Toilets and bathrooms | 2.0 | — |
| Store rooms | 5.0 | 4.5 |
| Libraries — stack room/stack area | **6.0 kN/m² for a minimum height of 2.2 m + 2.0 kN/m²/m beyond 2.2 m** | 4.5 |
| Libraries — reading rooms (without separate storage) | 4.0 | 4.5 |
| Libraries — reading rooms (with separate storage) | 3.0 | 4.5 |
| Boiler/plant rooms, calculated, not less than | 4.0 | 4.5 |
| Corridors/passages/lobbies/stairs (excl. storage & projection rooms), not less than | 4.0 | 4.5 |
| Balconies | same as rooms served, min 4.0 | 1.5/m run at outer edge |

**iii) Institutional**

| Space | UDL | Concentrated |
|---|---|---|
| Bed rooms, wards, dressing rooms, dormitories, lounges | 2.0 | 1.8 |
| Kitchens, laundries, laboratories | 3.0 | 4.5 |
| Dining rooms, cafeterias, restaurants | 3.0† | 2.7 |
| Toilets and bathrooms | 2.0 | — |
| X-ray rooms, operating rooms, general storage areas, calculated, not less than | 3.0 | 4.5 |
| Office rooms and OPD rooms | 2.5 | 2.7 |
| Corridors/passages/lobbies/stairs incl. fire escapes, per floor served, not less than | 4.0 | 4.5 |
| Boiler rooms and plant rooms, calculated, not less than | 5.0 | 4.5 |
| Balconies | same as rooms served, min 4.0 | 1.5/m run at outer edge |

**iv) Assembly**

| Space | UDL | Concentrated |
|---|---|---|
| Assembly areas — with fixed seats‡ | 4.0 | — |
| Assembly areas — without fixed seats | 5.0 | 3.6 |
| Restaurants (subject to assembly), museums, art galleries, gymnasia | 4.0 | 4.5 |
| Projection rooms | 5.0 | — |
| Stages | 5.0 | 4.5 |
| Office rooms, kitchens, laundries | 3.0 | 4.5 |
| Dressing rooms | 2.0 | 1.8 |
| Lounges and billiards rooms | 2.0 | 2.7 |
| Toilets and bathrooms | 2.0 | — |
| Corridors, passages, staircases incl. fire escapes | 4.0 | 4.5 |
| Balconies | same as rooms served, min 4.0 | 1.5/m run at outer edge |
| Boiler rooms and plant rooms, incl. weight of machinery | 7.5 | 4.5 |
| Corridors/passages subject to loads greater than crowds (wheeled vehicles, trolleys); corridors/stairs/passages in grandstands | 5.0 | 4.5 |

**v) Business and office** (see also Cl 3.1.2, partition load allowance)

| Space | UDL | Concentrated |
|---|---|---|
| Rooms, general use, with separate storage | 2.5 | 2.7 |
| Rooms without separate storage | 4.0 | 4.5 |
| Banking halls | 3.0 | 2.7 |
| Business computing machine rooms (fixed computers/similar equipment) | 3.5 | 4.5 |
| Records/files store rooms and storage space | 5.0 | 4.5 |
| Vaults and strong room, calculated, not less than | 5.0 | 4.5 |
| Cafeterias and dining rooms | 3.0† | 2.7 |
| Kitchens | 3.0 | 2.7 |
| Corridors/passages/lobbies/stairs incl. fire escapes (excl. stores), not less than | 4.0 | 4.5 |
| Bath and toilet rooms | 2.0 | — |
| Balconies | same as rooms served, min 4.0 | 1.5/m run at outer edge |
| Stationary stores | 4.0 per metre of storage height | *not captured cleanly in this extraction — verify against p.10* |
| Boiler rooms and plant rooms, calculated, not less than | 5.0 | *not captured cleanly — verify against p.10* |
| Libraries | see Educational (ii) above | |

**vi) Mercantile**

| Space | UDL | Concentrated |
|---|---|---|
| Retail shops | 4.0 | 3.6 |
| Wholesale shops, calculated, not less than | 6.0 | 4.5 |
| Office rooms | 2.5 | 2.7 |
| Dining rooms, restaurants, cafeterias | 3.0† | 2.7 |
| Toilets | 2.0 | — |
| Kitchens and laundries | 3.0 | 4.5 |
| Boiler rooms and plant rooms, calculated, not less than | 5.0 | 6.7 |
| Corridors/passages/stairs incl. fire escapes and lobbies | 4.0 | 4.5 |
| Corridors/passages/stairs subject to loads greater than crowds (wheeled vehicles etc.) | 5.0 | 4.5 |
| Balconies | same as rooms served, min 4.0 | 1.5/m run at outer edge |

**vii) Industrial**

| Space | UDL | Concentrated |
|---|---|---|
| Work areas without machinery/equipment | 2.5 | 4.5 |
| Work areas with machinery/equipment — light duty, calculated, not less than | 5.0 | 4.5 |
| — medium duty | 7.0 | 4.5 |
| — heavy duty§ | 10.0 | 4.5 |
| Boiler rooms and plant rooms, calculated, not less than | 5.0 | 6.7 |
| Cafeterias and dining rooms | 3.0† | 2.7 |
| Corridors, passages, staircases incl. fire escapes | 4.0 | 4.5 |
| Corridors/passages/stairs subject to machine loads, wheeled vehicles‖, calculated, not less than | 5.0 | 4.5 |
| Kitchens | 3.0 | 4.5 |
| Toilets and bathrooms | 2.0 | — |

**viii) Storage**

| Space | UDL | Concentrated |
|---|---|---|
| Storage rooms (other than cold storage)/warehouses, calculated on bulk density, not less than | **2.4 kN/m² per metre of storage height, min 7.5 kN/m²** | 7.0 |
| Cold storage, calculated, not less than | **5.0 kN/m² per metre of storage height, min 15 kN/m²** | 9.0 |
| Corridors/passages/stairs incl. fire escapes, per floor served, not less than | 4.0 | 4.5 |
| Corridors/passages subject to loads greater than crowds (wheeled vehicles etc.) | 5.0 | 4.5 |
| Boiler rooms and plant rooms | 7.5 | 4.5 |

**Footnotes:**
- **†** Where unrestricted assembly of persons is anticipated, increase UDL to **4.0 kN/m²** — attached to the "dining rooms/cafeterias/restaurants"-type rows above, not to "assembly areas without fixed seats" (that row already carries its own value and no † in the source).
- **‡** "With fixed seats" means removing the seating for other use is improbable — a definitional note, not a load modifier.
- **§** Industrial light/medium/heavy-duty labels carry "no special meaning in themselves" — they just describe whatever load the floor is actually designed for. If the real heavy-duty load exceeds **10 kN/m²**, design for the actual figure, not the table minimum.
- **‖** For mechanical handling equipment (warehouses, workshops, store rooms), ascertain the actual load from the equipment in use rather than relying on the table value alone.

**Concentrated load application (Cl 3.1.1):** for bending/shear, treat as a point load; for local effects (crushing/punching), treat as acting over **0.3 × 0.3 m**.

**Partition load allowance (Cl 3.1.2)**, where actual light-partition loads can't be assessed at planning stage: add a UDL of **≥ 33.3% of the finished partition weight per metre run**, subject to a **minimum of 1 kN/m²** — but only applies where partition weight ≤ **1.5 kN/m² of wall area** and ≤ **4.0 kN per metre length**. Outside those caps, calculate the actual load instead.

## Reduction in imposed loads (Cl 3.2)

**For columns/walls/piers/foundations (Cl 3.2.1)** — reduction in total imposed load carried, by number of floors (including roof) supported:

| Floors carried | Reduction |
|---|---|
| 1 | 0% |
| 2 | 10% |
| 3 | 20% |
| 4 | 30% |
| 5–10 | 40% |
| Over 10 | 50% |

**No reduction permitted** for plant/machinery specifically allowed for, or in storage buildings/warehouses/garages (Cl 3.2.1.1). For other buildings designed at ≥ 5.0 kN/m², the reduction is still permitted, but the assumed loading must never be less than if all floors had been designed at 5.0 kN/m² with no reduction. **If a lower floor's reduced load comes out less than the floor above's reduced load, use the upper floor's value instead** (the reduction schedule isn't allowed to produce a physically nonsensical lighter load lower in the building).

**For beams/girders/trusses (Cl 3.2.2):** where a single span supports ≥ 50 m² of floor at one level, reduce by **5% per 50 m², capped at 25%**. **Never reduced:** superimposed moving loads, actual machinery loads, partition-wall loads, impact/vibration. **Never applies to roof-supporting members** at all.

**Floor-capacity posting (Cl 3.3):** any floor in Assembly/Business/Mercantile/Industrial/Storage occupancy designed for UDL **> 3.0 kN/m²** needs a permanent posted notice (embossed/cast tablet, ≥ 0.25 m smallest dimension, mounted ≥ 1.5 m above floor, lettering ≥ 25 mm) stating the actual designed distributed and concentrated loading.

## Table 2 — Imposed loads on roofs [Cl 4.1; p.14]

| Roof type | UDL on plan | Minimum imposed load |
|---|---|---|
| Flat/sloping/curved, slope ≤ 10° — access provided | **1.5 kN/m²** | 3.75 kN over any 1m width of slab; 9 kN over any beam/truss/wall span |
| Flat/sloping/curved, slope ≤ 10° — access not provided (maintenance only) | **0.75 kN/m²** | 1.9 kN over 1m width; 4.5 kN over beam/truss/wall span |
| Sloping roof, slope > 10° | 0.75 kN/m² **− 0.02 kN/m² per degree over 10°** (roof membrane/purlins) | min 0.4 kN/m² |
| Curved roof, spring-to-crown slope > 10° | (0.75 − 0.52y) kN/m², y = h/l (h=rise, l=chord width) | min 0.4 kN/m² |

**Roof/snow-or-rain interaction:** design for whichever is greater — the Table 2 imposed load, or actual snow/rain accumulation load — **not both added together** (Note 1).

**Sloping-roof member reduction (Cl 4.5.1):** for slopes > 10°, trusses/beams/girders *supporting* the purlins may be designed for only **2/3 of the imposed load** actually on the purlins/sheets.

**Concentrated load on roof coverings (Cl 4.2):** **0.90 kN over 12.5 cm²**, positioned for maximum stress — doesn't apply to glass/fibreglass transparent sheeting. Members directly supporting roof covering (Cl 4.5) need the more severe of the transmitted covering load or this same 0.90 kN over 12.5 cm² (reducible to 0.5 kN where planks/ladders distribute the load across ≥ 2 members).

## Table 3 — Horizontal loads on parapets, parapet walls, balustrades [Cl 5.1; p.16]

| Usage | Horizontal load, kN/m run |
|---|---|
| Light access stairs/gangways ≤ 600mm wide | **0.25** |
| Light access stairs/gangways > 600mm wide; stairways, landings, balconies, parapets (private/dwellings) | **0.35** |
| All other stairways, landings, balconies, parapets/handrails to roofs | **0.75** |
| Assembly-occupancy parapets/balustrades (theatres, cinemas, schools, overcrowding-prone) | **2.25** |

Applied **at handrail/coping level**; also check vertically (not simultaneous with the horizontal case). **Grandstands/stadia (Cl 5.2):** 0.35 kN/m along the line of seats + 0.15 kN/m perpendicular (not simultaneous); seatless platforms: **0.25 kN/m² of plan area**.

## Impact & vibration (Cl 6)

- **Impact allowances** (increase over the static imposed load, absent better data): frames supporting lifts/hoists **100%**; light-machinery supporting structures/foundations **20%** (this is also the floor for any installed-machinery vibration allowance — never go below 20%); reciprocating-machinery/power-unit supports **50%**; foundations/footings/piers for lifts and hoisting apparatus **40%**. *(Reconstructed from a scrambled table region in the source extraction — the percentages are confirmed, but re-check the exact structure-type-to-percentage pairing against the actual page before using on a real lift/machinery foundation design.)*
- **Crane gantry girders/columns (Cl 6.3):** vertical impact **+25%** of max static load (girders, all crane classes); **+25%** for columns supporting Class III/IV cranes, **+10%** for Class I/II; **no addition** for foundation design. Hand-operated cranes: **+10%** (girders only). Horizontal transverse force: **10%** of crab+lifted weight (rigid-mast cranes) or **5%** (other overhead/hand cranes), distributed among wheels on one rail, applied one side of the frame at a time. Longitudinal tractive force along rails: **5%** of static wheel loads.
- **Crane combinations (Cl 6.4):** multi-crane aisles — tandem cranes at full load + overloading (Cl 6.3.1: **+10%** for ladle/charging cranes prone to overload); long-span gantries design for one fully-loaded+overloaded crane plus as many additional loaded cranes as the span accommodates (without the overload factor on those). Lateral surge and longitudinal tractive force **don't act simultaneously** — except with only one crane in the bay, where they may.

## Other loads (Cl 7) — cross-references only
Dead load → [[IS 875 Part 1 - Dead Loads]]. Wind → [[IS 875 Part 3 - Wind Loads]]. Seismic → IS 1893 (not yet built). Snow → [[IS 875 Part 4 - Snow Loads]]. Special loads/combinations → [[IS 875 Part 5 - Special Loads and Load Combinations]].

## Cross-references
- [[IS 875 Part 1 - Dead Loads]] — the companion load type; both feed IS 456's Cl 19 loads clause and Table 18 partial safety factors.
- [[IS 875 Part 3 - Wind Loads]], [[IS 875 Part 4 - Snow Loads]], [[IS 875 Part 5 - Special Loads and Load Combinations]] — the other three parts of the same code.
- [[IS 456 - Plain and Reinforced Concrete]] — Table 18 (γf factors) is where dead+imposed combine for design.
- Parent plan: Code Design Assistant.
