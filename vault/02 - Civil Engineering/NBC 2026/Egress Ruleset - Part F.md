---
status: active
project: civil-engineering
type: reference
---
# Egress Ruleset — NBC 2026 Part F

Phase 1 deliverable for the Code Design Assistant — the first domain converted from prose into checkable rules (`parameter / condition / threshold / applicability / source clause + page`), per the domain locked 2026-09-11 (egress / staircases / exit widths). Built from [[Part F - Fire and Life Safety]], verified against the source PDF page-by-page (not just the section note) while building this.

**How to use this:** each row is a single checkable requirement. Where the source clause carries an exception or a soft/ambiguous word ("recommended," "preferred," undefined terms like "low occupant load"), it's called out in the Notes / Exceptions column rather than folded into the threshold — per the 2026-09-11 discipline rule: a table that smooths over an ambiguity is less trustworthy than the paragraph it replaced. **Fire ratings, refuge areas, pressurisation and suppression are out of scope here** — those are separate topics already covered in [[Part F - Fire and Life Safety]]; this note is egress geometry and capacity only.

## A. Occupant Load — Table 2 [Cl 4.3, 4.4.2.1; p.2769–2771]

The starting input for every capacity/exit-count calculation below — actual declared occupancy, but never less than this table.

| Occupancy | Load Factor (m²/person) | Notes / Exceptions |
|---|---|---|
| A Residential | 12.5 net | |
| B Educational | 3.0 net | |
| C Nursing home | 12.0 gross | |
| C Clinic (daycare) | 12.0 gross | |
| C Hospital inpatient (ward/sleeping) | 11.0 net | Dormitory-type sleeping accommodation (aged homes, orphanages etc.) uses 7.5 gross instead, per Table 2 Note 2. |
| C Hospital outpatient | 7.0 net | |
| D Assembly, concentrated, no fixed seating | 0.65 net | |
| D Assembly, less concentrated (pre-function, multipurpose) | 1.40 net | |
| D Assembly, fixed seating | seats × 1.2 | Not an area factor — multiply seat count directly. |
| D Dining / restaurants with seating & tables | 1.80 net | |
| D Gym / sports room / library with equipment, performance stages | 4.6 net | |
| D Swimming pool — water surface / deck | 3.5 / 2.0 net | |
| D Mall — basement or street sales floor | 2.1 net | |
| D Mall — upper sales floor | 4.3 net | |
| D Mall — food court | 1.8 gross | |
| D Storage/warehouse, receiving | 14.3 net | |
| F Mercantile — street floor & above | 2.1 gross | |
| F Mercantile — below street floor | 3.0 gross | |
| E Business | 7.1 net | |
| E Datacentre — admin areas | 10.0 gross | |
| E Datacentre — data hall / server / equipment room | 50.0 gross | See Annex G for parking-driven variants. |
| G Industrial — low hazard | 20.0 gross | |
| G Industrial — moderate hazard | 15.0 gross | |
| G Industrial — high hazard | 10.0 gross | |
| H Storage | 30.0 gross | |
| J Hazardous | 10.0 gross | |

**Cross-cutting notes (apply regardless of row):**
- Commercial kitchen (any occupancy above) → 9.3 m² net/person.
- Car parking, non-storage occupancy → 30 m²/person.
- Mezzanine occupant load is added to the floor it discharges to.
- **Gross is the recommended default over net** — the source text itself flags net as prone to underestimating total floor population (excludes corridors/closets/wall thickness where people still circulate). Net is only appropriate for specific predictable-layout rooms (classrooms, fixed-seat halls).
- Number of means of egress is computed **floor-by-floor**, not accumulated — but must never decrease along the direction of travel.

## B. Number & Arrangement of Exits

| Parameter | Condition / Applicability | Threshold | Notes / Exceptions | Source |
|---|---|---|---|---|
| Minimum number of fire exits | Any building | **Computed**, not a fixed number — driven by occupant load (Table 2) × width-per-person (Table 3), subject to max travel distance (Table 4) | Not a lookup value — this is the formula the rest of this ruleset feeds into. | Cl 4.4.2.1, p.2771–2772 |
| Minimum staircases | High-rise & special buildings (per Part F's applicability table — see [[Part F - Fire and Life Safety]] §1) | **≥ 2** | | Cl 4.4.2.4.3.1, p.2777 |
| Minimum basement exits | Any basement | **≥ 2** independent exits, sized per Cl 4.4.2.1 | | Cl 4.2.19.2, p.2768 |
| Staircase discharge arrangement | All exit staircases | ≥ 50% must discharge (a) directly, or (b) via exit passageway — not (c) via a large lobby only | Firefighting shafts: (a) preferred, (b) alternate, (c) **not allowed**. Residential & educational firefighting shafts: (a) **only**. | Cl 4.4.2.4.3.1, p.2777 |
| Firefighting shaft count | Building/floor with ≥ 3 compartments | **≥ 2** firefighting shafts | | Cl 4.4.2.4.3.1, p.2777 |
| Exit separation (remoteness) | Any building, two required exits | min separation = diagonal of served area **÷ 2** (unsprinklered) or **÷ 3** (sprinklered) | | Cl 4.4.2.2(d) / Fig. 10, p.2772–2773 |
| Dead-end corridor length | Educational / institutional / assembly | **≤ 6 m** | | Cl 4.4.2.2(c), p.2772 |
| Dead-end corridor length | All other occupancies | **≤ 15 m** | | Cl 4.4.2.2(c), p.2772 |

## C. Exit / Egress Capacity & Width

| Parameter | Condition / Applicability | Threshold | Notes / Exceptions | Source |
|---|---|---|---|---|
| Unit of exit width | Any egress component | **500 mm = 1 unit**; a clear 250 mm counts as an extra half-unit; < 250 mm not counted at all | | Cl 4.4.2.3(b), p.2772 |
| Width per person — stairways | Residential (A), Educational (B), Assembly (D), Business (E), Mercantile (F), Industrial (G), Storage (H) | **10 mm/person** | | Table 3, p.2774 |
| Width per person — stairways | Institutional (C) | **15 mm/person** | | Table 3, p.2774 |
| Width per person — stairways | Hazardous (J) | **18 mm/person** | | Table 3, p.2774 |
| Width per person — level components & ramps | Residential (A), Educational (B), Assembly (D), Business (E), Mercantile (F), Industrial (G), Storage (H) | **6.5 mm/person** | Worked example in the source: a 1 000 mm clear door at factor 6.5 serves 1000/6.5 ≈ 153 persons. | Table 3, p.2774 |
| Width per person — level components & ramps | Institutional (C) | **13 mm/person** | | Table 3, p.2774 |
| Width per person — level components & ramps | Hazardous (J) | **10 mm/person** | | Table 3, p.2774 |
| System capacity | Egress path with multiple components (door → corridor → stair, etc.) | Governed by the **most restrictive single component**, not summed or averaged | Capacity may never decrease along the path of travel, even though it's computed floor-by-floor. | Cl 4.4.2.3(d)/(e), p.2772–2773 |
| Corridor width | Corridor is the sole access to a fire exit | **≥ calculated exit width** required | | Cl 4.4.1(b), p.2771 |
| Corridor width (aggregate check) | Corridor feeding multiple exit doorways | **≥ calculated aggregate width** of the doorways leading from it | | Cl 4.4.2.4.2(a), p.2777 |

## D. Travel Distance — Table 4 [Cl 4.4.2.1, 4.4.2.2(a), 4.4.2.4.2(a), 6.8.1.1; p.2775–2776]

| Occupancy | Type 1&2, Unsprinklered (m) | Type 1&2, Sprinklered (m) | Type 3&4 (m) |
|---|---|---|---|
| Residential (A) | 30 | 60 | 22.5 |
| Educational (B) | 30 | 45 | 22.5 |
| Institutional (C) | 30 | 45 | 22.5 |
| Assembly (D) | 30 | 45 | 30 |
| Business (E), incl. datacentre admin | 30 | 60 | 30 |
| Datacentre building | N/A | 60 | N/A |
| Mercantile (F) | 30 | 45 | 30 |
| Industrial G-1, G-2 | 45 | 60 | not permitted |
| Industrial G-3 | 22.5 | 45 | — |
| Storage (H) | 30 | 90 | — |
| Hazardous (J) | 22.5 | 30 | — |

**Notes / Exceptions (all from the table's own footnotes — don't apply the headline numbers without checking these):**
- **Common path of travel ≤ 50%** of the value above.
- Ramps are **not counted as an exit** for basements below the first basement, in car parking.
- Utility/equipment service areas may be exempt from travel-distance measurement from within the room.
- Ceiling ≥ 10 m at ground floor (airports, exhibition halls, convention centres, mall atria, entrance lobbies) + sprinklered → **+100%** travel distance in those areas only — not applied to the Type 3&4 column.
- Same spaces at ceiling ≥ 17 m with a sprinkler exemption → also **+100%**, with smoke/heat venting recommended.

## E. Doorways [Cl 4.4.2.4.1; p.2774–2775]

| Parameter | Condition / Applicability | Threshold | Notes / Exceptions |
|---|---|---|---|
| Minimum doorway width | Any exit doorway | **≥ 1 000 mm** | Must also independently satisfy the Table 3 level-component width-per-person requirement — whichever is larger governs. |
| Minimum doorway width | Assembly buildings | **≥ 2 000 mm** | |
| Minimum doorway height | Any exit doorway | **≥ 2 000 mm** | |
| Operability | Exit doorway | Openable from the served side **without a key** | |
| Mirrors | Exit doors / exits | **Not permitted** | Avoids confusion about exit direction. |
| Revolving doors as egress | Used as an egress component | Book-fold collapse to ≥ 1 000 mm parallel paths; not within 3 m of stair/escalator foot or top; hinged door of equal capacity within 3 m of it | Counts for only **50 persons** of capacity regardless of its actual width. |
| Access-controlled / electromagnetic doors | Any | Auto-unlock on sprinkler/detection activation (stays unlocked until manual reset); auto-unlock on power loss; manual 'PUSH TO EXIT' device cuts lock power directly, independent of the access-control system | |
| Turnstiles | Restrict travel direction or collect fares | Must not obstruct required egress unless a door opening of required width is within 3 m; must disengage (auto or manual) for egress | |
| Folding-partition doors | Any | **Not acceptable** as a means of egress | |
| Central-corridor room doors | Rooms opening onto a central corridor that is part of exit access | Must open **inward** | Exception: rooms of assembly occupancy are excluded from this inward-opening requirement. |

## F. General Exit Requirements (door direction, ceiling height, walking surface) [Cl 4.2.9–4.2.18; p.2766–2767]

| Parameter | Condition / Applicability | Threshold | Notes / Exceptions |
|---|---|---|---|
| Exit door swing at a landing | Assembly (D) and Institutional (C-1) | Door must open onto a **landing**, never directly onto a flight of stairs | |
| Exit door swing at a landing | All other occupancies | An open door must not reduce the landing pathway by more than **half the staircase width** | Overhead/sliding doors not permitted in either case. |
| Exit-stair discharge | Buildings < 60 m | Firefighting shaft on the external wall, discharging directly outside | ≥ 50% of required exit stairs (rounded up) must discharge directly to exterior or via exit passageway. |
| Exit-stair discharge | Buildings ≥ 60 m | Firefighting shaft(s) discharge to exterior **via exit passageway** | Structural core often forces the shaft position at this height. |
| Clear ceiling height | Fire exits & exit passageways | **≥ 2.4 m** | |
| Fire-exit door height | Fire exit doors | **≥ 2.0 m** | |
| Level-change handling | Elevation change > 300 mm in an exit | Use a ramp, with handrails and a floor finish that contrasts with adjacent finishes | |
| Walking-surface slope, direction of travel | Exit access | **≤ 1 in 20**, unless it meets ramp requirements (§J below) | |
| Walking-surface cross-slope | Exit access | **≤ 1 in 48** | |
| Walking-surface finish | Exit access | Slip-resistant along the entire path | |

## G. Staircases — General & Internal [Cl 4.4.2.4.3.1–.2; p.2777–2778]

| Parameter | Condition / Applicability | Threshold | Notes / Exceptions |
|---|---|---|---|
| Construction | Internal staircase | Non-combustible, **≥ 120 min** fire resistance | |
| Layout | Internal staircase | Must not be arranged around a lift shaft | |
| Equipment exclusion | Staircase interior | No flue/chimney, electromechanical equipment, AC units, gas piping, or electrical panels | |
| Minimum tread width (no nosing) | Residential | **≥ 250 mm** | |
| Minimum tread width (no nosing) | Assembly, hotels, educational, institutional, business, and all other buildings | **≥ 300 mm** | Treads must also be maintained non-slip. |
| Maximum riser height | One/two-family dwellings | **≤ 175 mm** | |
| Maximum riser height | All other buildings | **≤ 150 mm** | |
| Risers per flight | Any staircase | **12 is the recommendation**; **15 is the hard cap** | Two different strengths of requirement in one sentence — 12 is advisory, 15 is the actual limit. Don't treat 12 as enforceable. |
| Handrail sides | Staircase width < 1 500 mm | One side | |
| Handrail sides | Staircase width ≥ 1 500 mm | Both sides | |
| Handrail projection | Any staircase | **≤ 90 mm** into the measured width | |
| Minimum headroom | Under a stair landing / under the staircase | **≥ 2.2 m** | |
| Access door rating | Access to a fire-exit staircase | **≥ 120 min** fire door | |
| Openings into staircase | Any staircase | No living space, store, or other fire-risk space opens directly into it; no electrical shafts/AC ducts/gas pipes through or opening into it | |
| Lift openings | Any staircase | Lifts must **not** open into the staircase or its mid-landings | |
| Finishes | Staircase interior | No combustible decoration or wall panelling | |
| Obstruction | Beams/columns/building features | Must not reduce the staircase's headroom or width | |
| Floor indication board | Inside the staircase, near the fire door | **≥ 300 × 200 mm**, showing staircase ID, floor number, direction to discharge | |
| Floor number signage | Outside the staircase, facing it | Individual floor numbers prominently marked | |
| Termination | All staircases | Must terminate at the exit-discharge level; **basement access via a separate staircase** | |
| Scissor staircases | Type where landings intermingle occupants, or both flights share airspace | **Not counted** as part of an exit | |

### G.1 Minimum staircase width by building typology [Cl 4.4.2.4.3.2(e), p.2778]

| Typology | Minimum Width | Notes / Exceptions |
|---|---|---|
| One/two-family dwelling | 1.00 m | Row housing, 2 storeys → 0.75 m. |
| Residential A-I / A-II / A-III | 1.25 m | |
| Residential hotel A-IV / A-V | 1.50 m | |
| Assembly building | 2.00 m | May reduce to 1.50 m if occupancy < 150 persons. |
| Educational | 1.50 m | |
| Institutional | 2.00 m | Also the maximum for hospital staircases specifically. |
| All other buildings | 1.50 m | |

Width > 2.00 m → central handrail **recommended**, not mandatory — don't flag this as a compliance failure if absent.

## H. Curved Stairs [Cl 4.4.2.4.3.3; p.2779]

| Parameter | Condition | Threshold | Notes / Exceptions |
|---|---|---|---|
| Use as means of egress | Curved stairs | **Not permitted** as part of a required exit | May still be used as *exit access* (not the exit itself) if: tread depth ≥ 280 mm at a point 350 mm from the narrow end, AND smallest radius ≥ 2 × stair width. |

## I. External Staircases [Cl 4.4.2.4.3.4; p.2779]

| Parameter | Condition / Applicability | Threshold | Notes / Exceptions |
|---|---|---|---|
| Ground connection | External staircase | Directly connected to the ground | |
| Entrance location | External staircase | Separate and remote from the internal staircase | |
| Nearby openings | Windows/doors within **3 m** of the external stair | Protect with fire-rated assemblies **≥ 60 min** | |
| Construction | External staircase | Non-combustible; doorway to it **≥ 120 min** | |
| Maximum inclination | External staircase | **≤ 45°** from horizontal | |
| Minimum flight width | External staircase | **≥ 1 500 mm**, straight flight | |
| Handrails | External staircase | Both sides, height **1 000–1 200 mm**, baluster gap **≤ 150 mm** | |
| Spiral staircase | External, as a means of egress | Building height **≤ 9 m**; diameter **≥ 1 500 mm**; adequate headroom | Also restricted to "low occupant load" — the source **does not define this numerically**. Treat as a flag for AHJ confirmation on any specific project, not a number to compute against. |

## J. Ramps as an Egress Component [Cl 4.4.2.4.3.5; p.2779–2780]

| Parameter | Condition / Applicability | Threshold | Notes / Exceptions |
|---|---|---|---|
| General compliance | Egress ramp | Meets all staircase requirements for enclosure, capacity, and limiting dimensions | Except where §6.1–6.9 (occupancy-specific rules) override it. |
| Maximum slope | Egress ramp | **≤ 1 in 12 (8%)** | |
| Surface | Egress ramp | Slip-resistant, securely attached, **no perforations** | |
| Direction-change landing | Where travel direction changes | **≥ 1.5 × 1.5 m** | |
| Width | Along the direction of egress | Must **not decrease** | |
| Landing placement | Egress ramp | At the top, at the bottom, and at every door opening onto the ramp | |
| Landing length | General | **≥ 1 500 mm** in the direction of travel | Reduces to ≥ 1 250 mm if the ramp is a straight run and not part of an accessible route. |
| Handrails | Egress ramp | Both sides | |
| **Scope exclusion** | **Basement car-parking ramps** | **These requirements do not apply** | Explicit carve-out in the source — don't apply ramp egress rules to basement car-park ramps. |

## K. Occupancy-Specific Exit & Egress Rules — Part F §6.1–6.9 [p.2840–2850]

These sit **on top of** everything above — Cl 4.4.2.4.3.1 says the general staircase-count rule is *supplemented* by these, not replaced. Only the egress-geometry/arrangement items are pulled in here; occupancy-specific fire-rating, suppression, and material-storage rules stay out of scope (see [[Part F - Fire and Life Safety]] §6 for those).

**⚠ Flagged conflict — read before using the common-path numbers below:** the general rule (§D above) computes common path of travel as **≤ 50% of the Table 4 travel distance**. For Institutional and for Assembly Type 1&2 unsprinklered, that Table 4 distance is 30 m, so the general rule computes to **≤ 15 m**. But two occupancy-specific clauses below (Institutional hospitals, and mall-like assembly) each state common path of travel as a flat **30 m** — double the general computation, with no cross-reference reconciling the two. This is a genuine, unresolved conflict in the source text, not a rounding difference. Don't pick one silently — confirm with the AHJ which governs for a specific hospital or mall project.

### K.1 Residential (Group A) [Cl 6.1; p.2840–2841]

| Parameter | Condition / Applicability | Threshold | Notes / Exceptions |
|---|---|---|---|
| Locking devices | A-I (lodging/rooming) | Chain-bolts, limited-opening sliding locks, and burglar locks that aren't easily quick-released are **prohibited** on any door that would impede exit | |
| Bathroom locks | A-I | Must be openable from outside in an emergency, **without a special key** | |
| Egress path | A-I (lodging/rooming house) | Sole means of egress must **not** pass through a non-residential occupancy in the same building | |
| Number of exits | A-I, floor area ≥ 500 m² on any floor | **≥ 2** separate means of exit, at least one with direct exit discharge | |
| Number of exit accesses | A-II (dormitories), sleeping rooms with occupancy > 10 persons | **≥ 2** separate, distinct exit accesses in different directions | Also inherits every A-I rule above. |
| Staircase fire doors | A-III (apartments/high-rise) | Naturally/cross-ventilated exit staircases **may skip** the fire door; all other staircases and any pressurised staircase **still need** one | Modifies §G's blanket "≥120 min fire door" staircase-access rule for this occupancy only. |
| Panic bars | A-IV (hotels) | Height **865–1 220 mm** from floor, in fire exits | |
| Door type | A-IV (hotels) | Horizontal-sliding doors **not permitted** across corridors | |

### K.2 Educational (Group B) [Cl 6.2; p.2841]

| Parameter | Condition / Applicability | Threshold | Notes / Exceptions |
|---|---|---|---|
| Doorways per room | Room capacity > 45 persons | **≥ 2** doorways, panic-bar operated | Classroom-to-outside doors may use ordinary classroom-type locks instead, provided there's no way to lock against egress from inside. |
| Small single-storey exception | Ground-floor-only building, ≤ 20 pupils | Classrooms may have **only 1 exit**, **≥ 900 mm** wide | Exterior walls < 900 mm from a property line must have no openings. |
| Grade placement | Pre-school / kindergarten / Grade 1 | Must be at **ground floor / exit-discharge level** | |
| Grade placement | Grade 2 | **≤ 1 floor** above ground/exit-discharge level | |
| Staircase fire doors | Any educational building | Naturally ventilated exit staircases **may skip** the fire door; other/pressurised staircases still need one | Same pattern as A-III residential above. |

### K.3 Institutional / Hospitals (Group C) [Cl 6.3; p.2841–2844]

| Parameter | Condition / Applicability | Threshold | Notes / Exceptions |
|---|---|---|---|
| Common path of travel | Institutional, incl. hospitals | **≤ 30 m** (as stated directly in this clause) | **See the flagged conflict above** — the general §D rule computes 15 m for this occupancy. |
| Dead-end corridor | Institutional | **≤ 6 m** | Consistent with the general rule in §B — no conflict here. |
| Compartment sizing (progressive horizontal evacuation) | Hospital compartment, holding its own + adjoining compartment's patients | **3.5 m²/person** bed-ridden | For ambulant (non-bed-ridden) patients, **0.6 m²/person is stated as "recommended,"** not a hard mandate — weaker requirement than the bed-ridden figure. |
| Corridor door width | Fire-resistant wall openings between compartments | **≥ 2.0 m**, double-swing double-leaf | |
| Patient movement routes | Aisles/corridors/ramps used to move patients | **≥ 2.4 m** throughout | Non-patient areas in the same facility: **≥ 1.5 m**. |
| Exit width | All exits from hospital/infirmary sections | **≥ 2.0 m** | |
| Patient-room door width | Single/double-occupancy room | **≥ 1.25 m** | |
| Patient-room door width | Ward, 3–5 beds | **≥ 1.50 m** | |
| Patient-room door width | Ward > 5 beds, or bed-evacuation areas (ICU, recovery, delivery) | **2.0 m** | May reduce to 1.5 m if two such doors are provided to the same area. |
| Doorways per room | Sleeping accommodation/suite > 100 m² | **≥ 2** doorways to the exit-access corridor | |
| Locked doors | Penal / mental institutions | **Permitted**, if reliable rapid-release means exist (remote lock control, or keys common to attendants) | Explicit carve-out (6.3.3) from the general "no locking devices impeding exit" principle — deliberate, not an oversight. |

### K.4 Assembly (Group D) [Cl 6.4; p.2844–2847]

| Parameter | Condition / Applicability | Threshold | Notes / Exceptions |
|---|---|---|---|
| Exit door width | Any assembly building | **≥ 2.0 m** | Matches the general doorway rule in §E — no conflict. |
| Number of exits (fixed-seat theatrical/theatre-type venues) | Baseline, any size | **≥ 2** exits, as remote as practicable | |
| Number of exits | Same venue type, capacity 600–1 000 persons | **≥ 3** exits, each **≥ 2.0 m** wide | |
| Number of exits | Same venue type, capacity > 1 000 persons | **≥ 4** exits, as remote as practicable | Width not separately restated at this tier — the ≥ 2.0 m general assembly doorway rule still applies. |
| Aisle width | At right angles to seating rows | **≥ 1.2 m** | No seat may be more than 7 seats from an aisle; a row open to an aisle on one end only ≤ 7 seats. |
| Cross-aisles | Where aisles don't directly reach exit doors | **≥ 1** per 10 rows, **≥ 1 m** wide | Steps not permitted in aisles unless gradient > 1 in 10. |
| Railings — box/balcony/gallery fascia | General | **≥ 1 000 mm** high | ≥ 1 100 mm at aisle ends; ≥ 1.2 m at the foot of steps. |
| Railings — cross-aisle | General | **≥ 900 mm** high | Exempt where seat backs on the aisle's front side already project ≥ 600 mm above the aisle floor. |
| Seat fastening | Assembly capacity > 300 persons | Seats must be securely fastened to the floor | Exception: boxes with level floors, ≤ 14 seats, need not be fastened. |
| Loose-chair density | Restaurants, night clubs, etc. (seats not fastened) | **≤ 1 seat per 1.4 m²** of seating-area floor (excludes dance floor/stage) | Rows between aisles ≤ 14 seats; rows open to an aisle at one end only ≤ 7 seats. |
| Seat row spacing | Loose-chair seating | **≥ 850 mm** back-to-back (or ≥ 700 mm + back thickness/incline) | **≥ 350 mm** clear between the back of one seat and the front of the next. |
| Mixed-use assembly/mercantile (mall-like), height | Assembly/mercantile portion of a mall building | **Preferably ≤ 30 m** | Above 30 m, the excess may be business/residential occupancy, but needs 240 min separation and independent exits that don't interface with the assembly/mercantile exits. |
| Common path of travel | Mall-like (assembly/mercantile/cinema/restaurant) occupancy | **30 m** (stated as a flat value, not "≤") | **See the flagged conflict above** — same 30 m-vs-15 m pattern as institutional hospitals. |
| Dead-end corridor | Mall-like occupancy | **≤ 6 m** | Consistent with the general rule — no conflict. |
| Exit passageway width | Mall-like occupancy | **≥ 2.0 m** | |

### K.5 Business (Group E) [Cl 6.5; p.2847]

| Parameter | Condition / Applicability | Threshold | Notes / Exceptions |
|---|---|---|---|
| Number of exits | Every floor, including basements used for office purposes | **≥ 2** | |

### K.6 Mercantile (Group F) [Cl 6.6; p.2847–2848]

| Parameter | Condition / Applicability | Threshold | Notes / Exceptions |
|---|---|---|---|
| Travel ways | Open-air mercantile operations (markets, petrol stations, roadside stands) | Must stay unobstructed, **no dead-ends** | |
| Occupancy reclassification | Mercantile stock that is predominantly highly hazardous goods | Treated as **Group J (Hazardous)** for this Part's purposes | Not a Group F exemption — it moves the whole occupancy classification. |

### K.7 Industrial (Group G) [Cl 6.7; p.2848–2849]

| Parameter | Condition / Applicability | Threshold | Notes / Exceptions |
|---|---|---|---|
| Travel distance override | Undivided floor areas (e.g. aircraft assembly) where distance to the nearest outside wall > 45 m | Satisfy via exit tunnels or overhead passageways | If genuinely impracticable, the Authority may permit other arrangements for single-storey buildings **only if** fully sprinklered and ceiling/curtain-board/roof-ventilation design controls smoke — but travel distance may **never exceed 65 m** even then. |
| Exit scope | Special-purpose industrial (machinery-only spaces) | Exits required only for **actually-employed persons** | Spaces with no human occupancy (pure machinery/equipment) may be excluded from the exit count entirely. |
| Unprotected vertical openings | Manufacturing operations needing them | Permitted beyond normal limits **only if** every floor level has direct access to enclosed stairways/exits protected against fire or smoke from the opening | |
| Number of exits | High-hazard industrial, every point on every floor | **≥ 2**, accessible in different directions | Where the floor is divided into rooms: ≥ 2 escape routes per room (small rooms/toilets shielded from hazard areas excepted). |
| Slide escapes | High-hazard industrial, upper floors | **Permitted** as required exits, new or existing buildings | |

### K.8 Storage (Group H) [Cl 6.8; p.2849–2850]

| Parameter | Condition / Applicability | Threshold | Notes / Exceptions |
|---|---|---|---|
| Exit proximity | Hazardous-commodity storage | Exit within **30 m** of any point (unsprinklered) | **35 m** if automatic sprinkler protection is provided. Matches Table 4's Storage row. |
| Number of exit-access doors | Storage area > 1 400 m² gross, OR > 10 persons normally present | **≥ 2**, readily openable, not lockable while occupied, not power-dependent | As remote from each other as practicable. |
| Exit spacing | Aircraft hangars, exterior walls | **≤ 45 m** intervals | ≥ 2 exits per storage/servicing area; horizontal exits through interior fire walls ≤ 30 m intervals; "dwarf/smash" aircraft doors acceptable; all exit doors unlocked in the direction of travel while occupied. |
| Mezzanine travel distance | Aircraft hangar mezzanines | **≤ 22.5 m** to nearest exit | Must lead directly to an enclosed stairwell discharging to exterior, a cut-off area, or outside fire-escape stairs. |
| Stair towers | Grain elevators | **≥ 1** dust-tight, non-combustible, enclosed stair tower, basement-to-first-floor and first-floor-to-top | Self-closing non-combustible doors at each floor landing; exterior fire escape (stair or basket-ladder type) from workhouse roof to ground/adjoining annexe, accessible from all floors above the first; a separate exterior fire escape from each storage annexe roof to ground. |

### K.9 Hazardous (Group J) [Cl 6.9; p.2850]

| Parameter | Condition / Applicability | Threshold | Notes / Exceptions |
|---|---|---|---|
| Number of exits | Any Group J occupancy | Same as high-hazard industrial (§K.7) — **≥ 2** in different directions | Cl 6.9.1 explicitly imports 6.7.2.3 wholesale rather than restating it. |

## Cross-references

- Parent reference: [[Part F - Fire and Life Safety]] — fire ratings, refuge areas, pressurisation, compartmentation, suppression (all out of scope here).
- Occupant load also feeds Annex H (metro stations), clause H-4.1(j) — not reproduced here, metro egress has its own dedicated figures (also in Annex H: platform evacuation times, stair/escalator/lift capacities — separate from this ruleset's building-egress focus).
- §K's occupancy-specific rules **supplement**, not replace, §A–J's general rules (Cl 4.4.2.4.3.1) — check both for any given building.
- Parent plan: Code Design Assistant.
