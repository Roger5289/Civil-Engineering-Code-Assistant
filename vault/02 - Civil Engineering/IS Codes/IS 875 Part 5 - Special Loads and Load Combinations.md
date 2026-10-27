---
status: active
project: civil-engineering
type: reference
---
# IS 875 (Part 5):1987 — Special Loads and Load Combinations

Last of the five IS 875 parts in Code Design Assistant's roadmap — with this, **all of IS 875 is built.** Source: `<your codes folder>\IS CODES\CED37-Structural safety\875_5.pdf` (20 pages). Extracted text: `<local extracted text>\IS 875\IS-875-Part5-Special-Loads-fulltext.txt`.

**The Cl 8 load combination list is the highest daily-value content here** — it's the general "which load cases to even check" reference that IS 456's Table 18 (partial safety factors) then supplies numbers for.

## Scope (Cl 1)
Loads/effects **not** covered by Parts 1–4 or IS 1893: temperature changes, internally-generated stresses (creep, shrinkage, differential settlement), soil/hydrostatic pressure, accidental loads. Plus general load-combination guidance.

## Temperature effects (Cl 2)
- Provide expansion/contraction joints (per IS 3414) **or** design for the additional stress — one or the other.
- Max/min shade-air temperature by region: given as **maps (Fig. 1/2)**, not tabulated values — not reproducible as text; pull the actual figures for a specific site's design temperature range.
- **Material temperature range may differ from air temperature** (exposure condition, absorption/radiation rate) — account for this separately, don't just use the air-temp figures directly.
- Structural analysis must consider both the **mean temperature change** and the **temperature gradient through the section** (Cl 2.1.3) — assume linear distribution through single-leaf elements.
- Below-ground portions: temperature variation is "generally insignificant" **except during construction** while exposed.

## Hydrostatic & soil pressure (Cl 3)
- Below-ground structures (retaining walls, basement walls): account for soil and/or water pressure per established theory, **plus surcharge** from stationary/moving loads. Where soil is below the water table, use **soil weight diminished by buoyancy + full hydrostatic pressure** (not full soil weight + hydrostatic, which would double-count).
- **Foundation slabs/footings under water pressure:** design for **full hydrostatic uplift** as a UDL. Check overturning under submerged conditions using **buoyant** (not dry) foundation weight.
- **Effective width for lateral soil pressure on pillars in sloping soil** (Cl 3.2) — a ratio applied to actual member width:

  | Actual member width | Effective/actual width ratio |
  |---|---|
  | < 0.5 m | 3.0 |
  | 0.5–1 m | 3.0 → 2.0 (interpolate) |
  | > 1 m | 2.0 |

  **Relieving soil pressure in front of the member is generally not counted** — conservative by design.
- Overturning/sliding checks must **disregard any favourable imposed-load effect**, and account for soil possibly being permanently or temporarily removed.

## Fatigue (Cl 4)
- Cracks initiate at stress concentrations (bolt/rivet holes, welds, geometry changes) — avoid sudden shape changes in tension/local-bending regions.
- **Fatigue combinations use dead load + imposed load only** — wind and earthquake stresses **may be ignored** for fatigue purposes unless a specific design code says otherwise.
- No precise codal method given for estimating stress-cycle probability — engineering judgement based on available data on loading frequency (Cl 4's own note admits this limitation).

## Structural safety during construction (Cl 5)
Erection loads (storage/positioning of materials, erection equipment incl. its operation) must be carried by the structure + any temporary bracing, within normal permissible stresses. **Combine with:** dead load, wind load, and whatever portion of imposed load actually acts during erection.

## Accidental loads (Cl 6)
Low-probability, often short-duration, potentially severe — impacts/collisions, explosions, fire. Generally only the **principal load-bearing system** needs checking for these, not every member.

**Vehicle impact on structural elements (Cl 6.1.2):** fictitious vehicle strikes at **1.2 m height**, any direction, **10 m/s (36 km/h)**. Two-mass model: **m₁ = 400 kg** (C₁ = 10,000 kN/m compression stiffness), **m₂ = 12,000 kg** (C₂ = 300 kN/m) — m₁ brakes fully before m₂ begins braking. Corresponds to a maximum static force of **630 kN** (m₁) — safe to design for **630 kN** as the governing static equivalent, though the accompanying impact wave may still require more than a static check for some elements. Safety railings against road-traffic collision use the same 1.2m/10m/s basis.

**Crane impact on buffer stops (Cl 6.1.4):** formula-based (crane speed at half nominal value, buffer shortening 0.1m for cranes ≤50t flexible suspension / 0.2m otherwise, reduced crane mass from bridge+crab+load-capacity+span terms) — pull the formula from the page for an actual crane-runway design; not a number worth approximating from memory.

**Internal gas explosion in closed rooms (Cl 6.2.2):** for residential-scale rooms with window-glass ventilation, overpressure calc based on **window area / room volume ratio**; glass assumed to break at **4 kN/m²** (3–4mm machine-made glass) providing the pressure relief. Pressure-time relationship per Fig. 4/5 (graphical, not tabulated) — most unfavourable rise/fall times chosen within the figure's bounds.

**Air raid shelters, vertical load (Cl 6.3)** — for buildings with floor imposed load ≤ 5.0 kN/m², shelters below ground get a characteristic vertical action of:

| Building | Load |
|---|---|
| Up to 2 storeys | **28 kN/m²** |
| 3–4 storeys | **34 kN/m²** |
| > 4 storeys | **41 kN/m²** |
| Particularly stable construction (RCC in-situ load-bearing structure), any storey count | **28 kN/m²** |

If floor imposed load > 5.0 kN/m², **add the difference** between the average imposed action on all storeys above and 5.0 kN/m² to the base figure.

**Fire (Cl 6.4):** thermal effect via either a time-temperature curve + required fire-resistance rating, or the energy-balance method: **Q = 1.2 × t_b** (Q in **kJ/m²** floor area, t_b = required fire resistance in minutes per IS 1642). *(Corrected 2026-09-11 audit — confirmed against the source page; the first draft guessed "1.25" from a garbled extraction and also had the units wrong as MJ/m² instead of kJ/m².)*

## Other loads (Cl 7)
Anything not covered here (special process loads, moisture/shrinkage effects, etc.) — per the relevant design code or the structure's performance requirements. No specific numbers given.

## Load combinations (Cl 8) — the most generally useful section

**Twelve combinations** (Cl 8.1), check whichever produces the most unfavourable effect — simultaneous maximum wind + earthquake + imposed + snow is explicitly flagged as not realistic, so these aren't all summed together:

1. DL
2. DL + IL
3. DL + WL
4. DL + EL
5. DL + TL
6. DL + IL + WL
7. DL + IL + EL
8. DL + IL + TL
9. DL + WL + TL
10. DL + EL + TL
11. DL + IL + WL + TL
12. DL + IL + EL + TL

*(DL=dead, IL=imposed, WL=wind, EL=earthquake, TL=temperature.)*

- **Roofs: substitute snow load for IL** wherever snow applies (Note 1).
- Follow the relevant design code (e.g. [[IS 456 - Plain and Reinforced Concrete]]'s Table 18) for the actual permissible-stress or partial-safety-factor numbers per combination — this Part only says *which combinations to check*, not the factors.
- **IL+EL combination (Note 3):** use the *reduced* imposed load specified in IS 1893 for seismic mass calculation, consistently, in both the earthquake-effect evaluation and the combined-load check — **don't use the full Part 2 imposed load with EL.**
- **Overturning (Note 4):** restoring moment ≥ 1.2×DL overturning moment + 1.4×IL overturning moment; where DL is the restoring force, count only 0.9×DL; ignore any IL restoring contribution. *(Identical to IS 456 Cl 20.1 — same rule, same numbers, cross-confirmed between the two codes.)*
- **Sliding (Note 5):** factor of safety ≥ 1.4, counting only 0.9×DL as resisting. *(Also matches IS 456 Cl 20.2.)*
- **Soil bearing pressure from wind alone (Note 6):** if wind-alone bearing pressure < **25%** of the DL+IL bearing pressure, it may be neglected entirely. If it exceeds 25%, size the foundation so the combined DL+IL+WL pressure doesn't exceed the allowable bearing pressure by more than **25%**. For earthquake, the permissible bearing-pressure increase follows IS 1893 instead — **the reduced Part-2 imposed load must NOT be used in combination with earthquake forces** (restated from Note 3).

## Cross-references
- [[IS 456 - Plain and Reinforced Concrete]] — Table 18 partial safety factors supply the numbers for combinations 2, 3, 6 here (DL+IL, DL+WL, DL+IL+WL); its Cl 20.1/20.2 overturning/sliding rules are confirmed identical to this Part's Notes 4/5.
- [[IS 875 Part 1 - Dead Loads]], [[IS 875 Part 2 - Imposed Loads]], [[IS 875 Part 3 - Wind Loads]], [[IS 875 Part 4 - Snow Loads]] — the four load types this Part combines.
- IS 1893 (seismic) — not yet built; supplies EL and the seismic-specific imposed-load reduction referenced in Notes 3/6.
- Parent plan: Code Design Assistant.
