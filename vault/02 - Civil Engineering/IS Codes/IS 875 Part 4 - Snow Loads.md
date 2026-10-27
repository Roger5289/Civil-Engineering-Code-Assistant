---
status: active
project: civil-engineering
type: reference
---
# IS 875 (Part 4):1987 — Snow Loads

Fifth of the five IS 875 parts. Source: `<your codes folder>\IS CODES\CED37-Structural safety\875_4.pdf` (10 pages — the smallest and narrowest-scope part of the five). Extracted text: `<local extracted text>\IS 875\IS-875-Part4-Snow-Loads-fulltext.txt`.

**Applicability check first:** this only matters for snow-fall regions — per the code's own note (Cl 1), that's parts of **Jammu & Kashmir (Baramulla, Srinagar, Anantnag, Ladakh districts), Punjab, Himachal Pradesh (Chamba, Kulu, Kinnaur, Mahasu, Mandi, Sirmur, Simla districts), and Uttar Pradesh (Dehra Dun, Tehri Garhwal, Almora, Nainital districts)**. Outside those regions, roofs are designed for [[IS 875 Part 2 - Imposed Loads]]'s Table 2 roof loads instead — this Part doesn't apply. Read this note if the maintainer ever takes on hill-station/Himalayan work; skip it otherwise.

## The core formula (Cl 3)
**S = μ × S₀**
- S = design snow load on roof (Pa)
- μ = shape coefficient (dimensionless, depends on roof geometry — Cl 4)
- S₀ = ground snow load (Pa)

**Roofs are designed for whichever is more severe: the actual snow load, or the Part 2 imposed roof load** (Cl 1.1) — not both added.

**Important gap in the code itself:** IS 875 Part 4 does **not** actually supply S₀ (ground snow load) values for different regions — the code's own foreword admits data was insufficient at time of writing, and directs users to contact the **Snow and Avalanches Study Establishment (DRDO), Manali, HP**, or the **India Meteorological Department, Pune**, for site-specific ground snow load. This Part only gives the shape coefficients to convert a ground load (however sourced) into a roof design load.

## Shape coefficients, μ (Cl 4.2) — by roof type
- **Simple flat/monopitch roofs, positive slope:** μ₁ = 0.8.
- **Simple pitched roofs:** μ varies by slope β — 0.8 for 0°≤β≤30°, tapering via 0.8+0.4×(β/30-1)-type interpolation through 30–60°, down toward 0 above 60°. *(Exact break-figures are diagram-based in the source, not fully text-extractable — pull p.3 for the precise curve.)*
- **Multilevel roofs (Cl 4.2.4):** the upper roof uses μ=0.8; the lower roof at the level change gets an additional **sliding-snow component (μs)** plus a **wind-drift component (μw)**, μw = (k·l₁)/S₀ bounded to **0.8 ≤ μw ≤ 4.0** (k = 2 kN/m³, drift length l₁ = 2h capped to 5–15 m). For lower-roof slope β > 15°: μs from an additional load = 50% of the max total load on the adjacent upper slope, distributed linearly. β < 15°: μs = 0.
- **Complex multilevel roofs and roofs with local projections/obstructions (Cl 4.2.5–4.2.6):** same drift-mechanics pattern, combined per Cl 4.2.1/4.2.2/4.2.4 — geometry-specific, pull by page.
- **Curved roofs (Cl 4.2.3):** two load cases must both be checked; restricted to h ≤ l/3, with μ=0 where slope β > 60° at the springing.

**Wind-exposure reduction (Cl 4.3):** shape coefficients may be cut by **25%** if the building is demonstrably in an exposed, open-level location (unobstructed by anything taller than the roof within 10× that obstruction's height, on all sides) AND has no parapet/projection that would trap snow. **Doesn't apply** in calm mountain valleys (snow layers accumulate without wind removal) or high-temperature areas where the max load comes from a single storm without appreciable wind.

**Appendix A** gives a more comprehensive multilevel-roof formula than Cl 4.2.4's simplified version, with roof-profile-dependent coefficients m₁/m₂ (0.5 for slopes <20°/shallow vaults; 0.3 for slopes >20°/steeper vaults) — pull by page for a real multilevel design.

## Ice load on wires (Cl 5)
For overhead electrical/communication lines, aerial masts, etc. in ice-forming zones: ice deposit thickness **3–10 mm** (site-dependent), ice density **0.9 g/cm³**. **Increase the wire/cable diameter used for wind-force calculation** ([[IS 875 Part 3 - Wind Loads]]) to account for the ice buildup.

## Cross-references
- [[IS 875 Part 2 - Imposed Loads]] — Table 2 roof loads are the fallback/comparison everywhere outside snow regions, and the "design for whichever is worse" rule always applies even inside them.
- [[IS 875 Part 3 - Wind Loads]] — ice-thickened wire diameters feed wind-force calculations.
- Parent plan: Code Design Assistant.
