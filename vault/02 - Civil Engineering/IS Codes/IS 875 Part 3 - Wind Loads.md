---
status: active
project: civil-engineering
type: reference
---
# IS 875 (Part 3):1987 — Wind Loads

Fourth of the five IS 875 parts in Code Design Assistant's roadmap, and the largest/most complex (63 pages). Source: `<your codes folder>\IS CODES\CED37-Structural safety\875_3.pdf`. Extracted text: `<local extracted text>\IS 875\IS-875-Part3-Wind-Loads-fulltext.txt`.

**How this note is scoped, and why:** unlike Parts 1–2, most of this document (roughly p.14–49) is dozens of building-shape-specific pressure-coefficient tables — walls, pitched/curved/canopy/multi-span roofs, circular silos, spherical structures, grandstands, each with its own geometry-dependent grid of Cpe values by wind angle and dimension ratio. These genuinely don't compress into prose or short tables without losing exactly the information that matters (which cell of which grid applies to your specific roof pitch and plan ratio) — several of the source tables didn't even reconstruct reliably from this extraction (multi-column grids, degrees-based headers). This note captures **the full calculation methodology** (which is stable, reusable, and the same for every project) in detail, and treats the shape-specific coefficient tables as **look up by page for the actual building geometry**, not transcribed here. Not yet independently audited the way IS 456 was.

## Scope (Cl 1)
Static and dynamic wind effects for design of buildings, structures, and components. Does **not** cover unconventional shapes/unusual locations without further investigation (Note 1), and explicitly flags special structures (chimneys, transmission towers, cooling towers) to specific companion IS codes used *alongside* this one.

## The core design methodology — the part that's reusable on every project

### Step 1: Design wind speed
**V_z = V_b × k1 × k2 × k3**

- **V_b — basic wind speed** at 10 m height, open terrain (Category 2), from the wind speed map (Fig. 1) or **Appendix A** (basic wind speed by city, 50-year return period). Representative values, m/s: **Delhi, Kanpur, Jaipur, Lucknow, Patna, Ludhiana, Chandigarh 47; Mumbai (Bombay), Hyderabad, Nagpur 44; Kolkata (Calcutta), Chennai (Madras), Bhopal→39(Bhopal is 39), Pondicherry, Nellore, Bhubaneshwar, Cuttack, Bhuj 50; Ahmedabad, Pune, Coimbatore, Ranchi 39; Bangalore, Mysore 33.** Full alphabetical list of ~150 cities/towns — pull by page for anything not listed here.
- **k1 — risk coefficient (Table 1, p.11)**, by design life and basic wind speed zone — **verified against the source page directly (2026-09-11 audit), one row was missing from the first draft:**
  - Standard 50-year life (all general buildings/structures): **k1 = 1.0** across every zone.
  - Temporary structures/construction-stage works (5-year life): **k1 = 0.82 (33 m/s zone) down to 0.67 (55 m/s zone)** — **higher wind-speed zones get the bigger discount, not lower zones** (corrected 2026-09-11 — the first draft had this backwards).
  - **Buildings presenting a low hazard to life/property — isolated towers in wooded areas, non-residential farm buildings (25-year life): k1 = 0.94 (33 m/s) down to 0.89 (55 m/s).** *(This entire row was missing from the first draft.)*
  - Important buildings — hospitals, communication towers/buildings, power plant structures (100-year life): **k1 = 1.05 (33 m/s) up to 1.08 (55 m/s)** — here the higher zones get the larger factor, opposite direction from the temporary/low-hazard rows.
  - A formula is given (Cl 5.3.1) for non-standard return periods (100–1000 years, for exceptionally important structures like nuclear plants).
- **k2 — terrain, height & structure-size factor (Table 2, p.12–13)**. **Four terrain categories:**
  - **Category 1** — exposed open terrain, obstruction height < 1.5 m (open sea coasts, flat treeless plains).
  - **Category 2** — open terrain, obstructions 1.5–10 m (this is the *reference* category the basic wind speed map itself is measured against — airfields, open parkland, undeveloped town outskirts).
  - **Category 3** — numerous closely-spaced obstructions up to 10 m (well-wooded areas, towns, partially-developed industrial areas). **Caution:** vegetation likely to blow down/defoliate in a cyclone can't be relied on to hold Category 3 — use an intermediate category or Category 2 instead in cyclone-prone areas.
  - **Category 4** — numerous large closely-spaced obstructions, generally > 25 m (large city centres, developed industrial complexes).
  
  Structures are also classed by size: **Class A** (max dimension < 20 m), **Class B** (20–50 m), **Class C** (> 50 m). k2 increases with height and terrain roughness, and decreases as structure class gets bigger (bigger structures average out local gusts less favourably — actually k2 is *lower* for Class C than Class A at the same height/terrain, since larger structures respond less to short-duration gusts). At 10 m height: Category 1 ranges ~0.99–1.05 across classes; Category 4 (not fully captured here) is lowest. **Full 4-terrain × 3-class × 13-height grid — pull Table 2 by page for the actual project's terrain/height/class combination; this is exactly the kind of number worth sourcing fresh, not transcribing.**
  - **Fetch and developed height (Table 3, Cl 5.3.2.4):** a terrain category's velocity profile doesn't develop to full height immediately — it grows with upwind fetch distance. For short fetches, use the less-rough terrain's profile or Appendix B's method instead.
- **k3 — topography factor**, Cl 5.3.3 + Appendix C. **= 1.0 for upwind slope ≤ 3°.** For slopes > 3°, k3 ranges **1.0 to 1.36** (accelerated wind near hill/cliff/ridge crests; decelerated in valleys/at the foot of cliffs) — method in Appendix C, and it varies with height (max near ground, back to 1.0 higher up).
- **Off-shore adjustment (Cl 5.5):** within 200 km of the coast, multiply the nearest coastal basic wind speed by **1.15** in the absence of definite offshore data (cyclonic storm influence already reflected in the onshore map up to ~60 km inland).
- Design wind speed is held **constant below 10 m height** (Note to Cl 5.3).

### Step 2: Design wind pressure
**p_z = 0.6 × V_z²** (p_z in N/m², V_z in m/s) — Cl 5.4. The 0.6 coefficient is fixed for average Indian atmospheric conditions (air density/pressure/temperature already baked in).

### Step 3: Apply pressure/force coefficients
- **On individual elements/cladding (Cl 6.2.1):** F = (C_pe − C_pi) × A × p_d — the *difference* between external and internal pressure coefficients matters, not just the external one. Positive = force toward the element; negative = away.
- **Internal pressure coefficients, C_pi (Cl 6.2.3)** — by cladding permeability, check both signs and take whichever governs:
  - **Openings ≤ 5% of wall area** (normal permeability — gaps around closed doors/windows, chimneys, vents): **C_pi = +0.2 and −0.2**, check both.
  - **Openings 5–20% of wall area:** **C_pi = +0.5 and −0.5.**
  - **Openings > 20%, or one open side:** **C_pi = +0.7 and −0.7.**
  - Roofs with no walls at all: treated per the external-pressure rules directly (Cl 6.2.3.3).
- **External pressure coefficients (C_pe)** — Table 4 onward (walls of rectangular buildings, p.14) through the many shape-specific tables (pitched roofs, curved roofs, canopy/butterfly roofs, multi-span roofs, circular silos, spherical structures, grandstands) spanning roughly **p.14–49**. Pull the table matching the actual building shape/wind angle/dimension ratio directly from the source — not reproduced here (see note above on why).
  - Local pressure-concentration coefficients (higher suction near ridges/eaves/cornices/90° corners) are given separately — use **only** for local cladding/fixing design, **never** for whole-roof or whole-structure load calculation (Note 2, Cl 6.2.2.2).
- **On the whole building/structure (Cl 6.3):** F = C_f × A_e × p_d, where C_f is the force coefficient (drag coefficient) and A_e the effective frontal area. Different tables give C_f for frames, lattice towers, walls, hoardings, and circular sections (Appendix D, accounting for Reynolds number and surface roughness).
- **Frictional drag (Cl 6.3.1):** add for rectangular clad buildings where the length/breadth-or-height ratio triggers it — **C_f′ = 0.02** for corrugated surfaces across the wind direction, **0.04** for ribbed surfaces.

## Dynamic effects (Cl 7) — when a structure needs more than the static method

**Trigger for investigating wind-induced oscillation:** height-to-minimum-lateral-dimension ratio **> 5.0**, OR first-mode natural frequency **< 1.0 Hz**. Fail *either* test → examine dynamic effects.

**Fundamental time period estimate** (Note 1, Cl 7.1), absent test/analysis data:
- Moment-resisting frames, no bracing/shear walls: **T = 0.1n** (n = number of storeys incl. basement).
- All other structures: **T = 0.09H/√d** (H = total height, d = max base dimension parallel to the wind force).

**Gust Factor / Gust Effectiveness Factor method (Cl 8):** an alternative to the static method for along-wind load on oscillation-prone structures — take whichever of the static or gust-factor estimate is more severe. Full hourly-mean-wind and along-wind-load procedure is in Cl 8.1–8.3 — pull by page if a specific structure trips the Cl 7.1 trigger; this isn't a calculation to approximate from memory.

## Cross-references
- [[IS 875 Part 1 - Dead Loads]], [[IS 875 Part 2 - Imposed Loads]] — companion load types; combine per IS 456 Table 18 or the eventual IS 875 Part 5 note.
- [[IS 456 - Plain and Reinforced Concrete]] — Cl 19.3 points here for wind load input; Table 18's WL factors (1.5/0.9 combinations) are where this plugs into RCC design.
- IS 1893 (seismic) — not yet built; wind and seismic are checked as alternative lateral load cases, not combined additively, in most ordinary building design.
- Parent plan: Code Design Assistant.
