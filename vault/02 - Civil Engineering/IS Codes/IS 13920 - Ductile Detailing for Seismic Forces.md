---
status: active
project: civil-engineering
type: reference
---
# IS 13920:1993 — Ductile Detailing of Reinforced Concrete Structures Subjected to Seismic Forces

Next code in Code Design Assistant's roadmap after [[IS 456 - Plain and Reinforced Concrete]], [[IS 875 Part 1 - Dead Loads|IS 875]] (all parts), and [[IS 1893 Part 1 - Earthquake Resistant Design]]. Source: `<your codes folder>\IS CODES\CED39-Earthquake engineering\13920.pdf` (19 pages, Edition 1.2 incorporating Amendments 1 & 2, 2002). Extracted text: `<local extracted text>\IS 13920\IS-13920-fulltext.txt`.

**Edition note:** this is the **1993 original** (reaffirmed 1998, amended 2002) — IS 13920 got a substantial revision in **2016** that's not in this library. If a specific project needs current compliance, confirm whether the 2016 edition is available before relying on this note for anything beyond general understanding; the core confining-reinforcement philosophy is unlikely to have changed radically, but specific numbers may have.

**Audited 2026-09-11.** Cleaner risk profile than IS 875/IS 1893 from the start — this document is almost entirely clause-based prose and inline formulas, not the large multi-column tables that caused real errors in those two audits. The audit: (1) confirmed ρ_min = 0.24√f_ck/f_y by rendering the source page as an image (the plain-text extraction had rendered it ambiguously); (2) confirmed the column design-shear coefficient (1.4) and the confining-reinforcement A_sh formulas by reproducing the code's own worked numerical examples by hand — both matched exactly; (3) resolved all four formulas that hadn't survived the first draft's text extraction (coupling-beam diagonal-reinforcement trigger, the A_sd diagonal-reinforcement area formula, the construction-joint reinforcement ratio, the boundary-element axial-capacity formula, and the full Annex A shear-wall flexural-strength procedure) by rendering the relevant pages as images and reading them directly. Nothing was found wrong — every number in the first draft that could be checked, checked out; the audit's value here was completing the gaps, not fixing errors.

## Scope (Cl 1)
Applies to **monolithic RCC construction only**, mandatorily in **seismic Zones III, IV, and V** (per [[IS 1893 Part 1 - Earthquake Resistant Design]]'s zone map). Precast/prestressed members permitted only if they can match monolithic RCC's ductility. This is the code IS 1893 Part 1 itself points to whenever a structural system claims SMRF or ductile-shear-wall status for its Response Reduction Factor.

## General specification (Cl 5)
- Governed by IS 456 except where modified here.
- **Buildings > 3 storeys: minimum concrete grade M20** (f_ck = 20 MPa).
- **Steel: Fe 415 or lower grade**, OR thermo-mechanically-treated Fe 500/Fe 550 with **elongation > 14.5%** and otherwise IS 1786-compliant. (Ordinary high-yield bars above Fe 415 without that elongation performance are not permitted for ductile detailing.)

## 6. Flexural members (beams) — frame members resisting earthquake forces, designed for flexure

**Applicability trigger:** factored axial stress under earthquake loading **≤ 0.1 f_ck** (above that, treat as a column — Section 7 instead).

- **Geometry:** width/depth ratio preferably **> 0.3**; width **≥ 200 mm**; depth **preferably ≤ clear span/4**.
- **Longitudinal reinforcement:**
  - Top and bottom faces: **≥ 2 bars continuously** through the member length.
  - **Minimum tension steel ratio: ρ_min = 0.24√f_ck/f_y** (f_ck, f_y in MPa).
  - **Maximum steel ratio, any face, any section: ρ_max = 0.025.**
  - **Positive-moment steel at a joint face ≥ half the negative-moment steel at that face.**
  - Steel at any section along the span (top or bottom) **≥ 1/4 of the max negative-moment steel at either joint face.** (IS 456 moment redistribution applies only to vertical-load moments, never to lateral-load moments — don't combine the two.)
  - **Anchorage at an external joint:** development length in tension **+ 10× bar diameter − the 90° bend allowance**, for both top and bottom bars, beyond the column's inner face. At an **internal** joint, both face bars run continuously through the column.
  - **Splices:** only where hoops are provided over the **entire splice length at ≤ 150 mm spacing**; lap length ≥ tension development length; **never spliced** (a) within a joint, (b) within **2d** of a joint face, or (c) within a quarter-span length where flexural yielding may occur; **max 50% of bars spliced at one section.** Welded/mechanical splices per IS 456 Cl 25.2.5.2 follow the same 50%-at-one-section cap.
- **Web (shear) reinforcement:**
  - Vertical hoops (135° hook + 10-diameter extension, min 75 mm) — min diameter **6 mm**, or **8 mm if clear span > 5 m**.
  - **Design shear = the greater of:** (a) factored shear from analysis, or (b) shear from **plastic hinge formation at both beam ends** (hogging/sagging moment capacities per IS 456) **plus factored gravity load on the span** — this "capacity design" shear is very often the governing case, not the analysis shear.
  - Bent-up bars/inclined hoops **don't count** toward shear resistance.
  - **Hoop spacing over 2d from each joint face** (and over 2d either side of any expected flexural-yielding section): **≤ smallest of d/4, 8× smallest longitudinal bar diameter**, but **≥ 100 mm**. **First hoop ≤ 50 mm from the joint face.** Elsewhere along the beam: **≤ d/2.**

## 7. Columns and frame members under bending + axial load

**Applicability trigger:** factored axial stress **> 0.1 f_ck** (the beam/column boundary, mirroring Section 6's own trigger).

- **Geometry:** min dimension **≥ 200 mm**; **≥ 300 mm** if the frame has beams spanning > 5 m centre-to-centre, or columns with unsupported length > 4 m. Shortest-to-perpendicular dimension ratio preferably **≥ 0.4**.
- **Longitudinal reinforcement:** lap splices only in the **central half** of the member (tension-splice detailing), hoops over the entire splice length at **≤ 150 mm**, max **50%** spliced at one section. Architectural extensions > 100 mm beyond the confined core: if counted on for strength, detail per this code; if treated as non-structural, IS 456's ordinary minimums apply instead.
- **Transverse reinforcement:** rectangular hoops (135° hook + 10-diameter extension, min 75 mm) — parallel legs **≤ 300 mm centre-to-centre**; beyond that, add a crosstie or an overlapping hoop pair. **Hoop spacing ≤ half the least lateral dimension**, except where special confining reinforcement (below) governs instead.
- **Design shear = the greater of:** (a) factored shear from analysis, or (b) **V_u = 1.4 × (M_u,lim^bL + M_u,lim^bR)/h_st** — the sum of opposite-sign beam moment capacities framing into the column, divided by storey height, ×1.4. Same capacity-design philosophy as beams.
- **Special confining reinforcement (Cl 7.4)** — the core of column ductility detailing:
  - **Length l₀ from each joint face** (and either side of any expected yielding section): **≥ largest of** the member's larger lateral dimension, **clear span/6**, or **450 mm**.
  - Extend **≥ 300 mm into a footing/mat** where the column terminates there.
  - **Full column height** required where: the gravity+seismic contraflexure point falls outside the middle half of clear height; the column supports a discontinued stiff member (e.g. a wall) — extending the reinforcement above/below the discontinuity by the longitudinal bar's development length too; or the column has significant stiffness variation up its height (partial-height bracing, mezzanine, partial-height RC wall).
  - **Spacing: ≤ 1/4 of the minimum member dimension**, and **≥ 75 mm, ≤ 100 mm** (the 75–100 mm band is a hard floor/ceiling, not just a guideline).
  - **Area of confining bar, circular hoops/spiral: A_sh = 0.09 × S × D_k × (f_ck/f_y) × (A_g/A_k − 1).**
  - **Area of confining bar, rectangular hoops: A_sh = 0.18 × S × h × (f_ck/f_y) × (A_g/A_k − 1)** (h = longer confining-hoop dimension, ≤ 300 mm — use crossties/overlapping hoops to keep it under that).
  - *(Both formulas cross-checked against the code's own worked examples — a 300 mm circular column, M20/Fe415, S=75mm, D_k=236mm gives A_sh=47.28 mm², matching an 8mm bar; a 650×500mm rectangular column, M20/Fe415, S=100mm gives A_sh=64.47 mm², matching a 10mm bar or 8mm at 70mm c/c. Both check out arithmetically against the formulas above.)*

## 8. Joints
Special confining reinforcement continues through the joint **unless** beams frame into **all four vertical faces**, each beam **≥ 3/4 of the column width** — in which case the joint may use **half** the column-end confining reinforcement, at **≤ 150 mm** spacing.

## 9. Shear walls

- **Thickness:** preferably **≥ 150 mm**.
- **Effective flange width** (flanged sections): extends beyond the web face by the **smaller of** half the distance to an adjacent shear-wall web, or **1/10 of total wall height.**
- **Minimum reinforcement ratio: 0.0025** of gross area, each direction (longitudinal and transverse), uniformly distributed.
- **Two curtains required** if factored shear stress **> 0.25√f_ck**, OR wall thickness **> 200 mm.**
- **Bar diameter ≤ 1/10 of the thickness of that part of the wall.**
- **Max reinforcement spacing, either direction: smallest of l_w/5, 3t_w, 450 mm** (l_w = wall length, t_w = web thickness).
- **Shear strength:** nominal shear stress τ_v per the usual V_u/(t_w·d_w) form (d_w may be taken as **0.8·l_w** for rectangular sections); design shear strength τ_c from IS 456 Table 13; ceiling τ_c,max from IS 456 Table 14. Where τ_v > τ_c: **A_h = V_us/(0.87·f_y·d_w) per vertical spacing S_v**, where V_us = V_u − τ_c·t_w·d_w. Vertical reinforcement must be **≥** the horizontal reinforcement so calculated.
- **Flexural strength:** per IS 456 column-under-combined-bending-and-axial-load method, or the slender-rectangular-wall formulas in **Annex A** (resolved 2026-09-11 audit via page render — the first draft had these flagged as unreadable in the extraction). Cracked flexural strength must exceed uncracked flexural strength.

  **Annex A — moment of resistance, slender rectangular wall, uniformly-distributed vertical reinforcement:**
  - Shared terms: **ρ = A_st/(t_w·l_w)** (vertical reinforcement ratio); **φ = 0.87f_y·ρ/f_ck**; **λ = P_u/(f_ck·t_w·l_w)**; **β = 0.87f_y/(0.0035·E_s)**; **x_u/l_w = (φ+λ)/(2φ+0.36)**; **x*_u/l_w = 0.0035/(0.0035 + 0.87f_y/E_s)**.
  - **Case (a), x_u/l_w < x*_u/l_w (flexural tension governs):**
    M_uv/(f_ck·t_w·l_w²) = φ[(1 + λ/φ)(1/2 − 0.416·x_u/l_w) − (x_u/l_w)²(0.168 + β²/3)]
  - **Case (b), x*_u/l_w < x_u/l_w < 1.0 (flexural compression governs):**
    M_uv/(f_ck·t_w·l_w²) = α₁(x_u/l_w) − α₂(x_u/l_w)² − α₃ − λ/2
    where α₁ = 0.36 + φ(1 − β/2 − 1/(2β)); α₂ = 0.15 + (φ/2)(1 − β − β²/2 − 1/(3β)); α₃ = (φ/6β)(1/(x_u/l_w) − 3).
    The x_u/l_w value to use here comes from the quadratic **α₁(x_u/l_w)² + α₄(x_u/l_w) − α₅ = 0**, where α₄ = φ/β − λ and α₅ = φ/(2β).
  - These assume a rectangular wall (depth l_w, thickness t_w) under combined uniaxial bending + axial compression, vertical reinforcement modelled as an equivalent steel plate along the section length, IS 456's concrete stress-strain curve, and a bi-linear steel curve.
- **Walls without boundary elements:** concentrate vertical reinforcement at each end — **≥ 4 bars of 12 mm diameter, in ≥ 2 layers.**
- **Boundary elements (Cl 9.4):** required along vertical wall edges where extreme-fibre compressive stress (factored gravity + factored EL) **exceeds 0.2f_ck**; may discontinue once that stress drops **below 0.15f_ck** (calculated elastically on gross section). Must carry the factored gravity load **+** the seismic-induced additional compression as a short column, the latter calculated as **(M_u − M_uv)/C_w** (M_u = factored design moment on the entire wall section, M_uv = moment of resistance from the distributed vertical reinforcement, C_w = centre-to-centre distance between the boundary elements along the wall's two vertical edges). *(Formula confirmed 2026-09-11 audit via page render.)* **Gravity load factor = 0.8** where gravity load adds to wall strength (not the usual 1.5, since here more gravity load helps rather than hurts). **Vertical reinforcement: 0.8%–6%** of boundary-element area (**practical ceiling ~4%** to avoid congestion). Full-height special confining reinforcement per Cl 7.4 wherever boundary elements are required — **or** boundary elements can be omitted entirely if the whole wall section gets special confining reinforcement instead.
- **Coupled shear walls (Cl 9.5):** connected by ductile coupling beams. **If the earthquake-induced shear stress in the coupling beam exceeds 0.1·l_s·√f_ck/D** (l_s = coupling beam clear span, D = overall depth), the entire earthquake shear and flexure should preferably be carried by **diagonal reinforcement** instead of conventional stirrups. *(Resolved 2026-09-11 audit by rendering the source page as an image — this formula hadn't survived the text extraction in the first draft.)* Where diagonal reinforcement is used: area per diagonal **A_sd = V_u/(1.74·f_y·sin α)** (α = diagonal's angle to horizontal), **≥ 4 bars of 8 mm diameter along each diagonal**; enclosed by special confining reinforcement (Cl 7.4) at **≤ 100 mm** pitch/spacing; anchored into the adjacent walls at **1.5× tension development length.**
- **Openings in walls:** check shear strength on critical planes through the opening; edge reinforcement must replace the interrupted bars' area — vertical bars full storey height, horizontal bars with tension development length beyond the opening's sides.
- **Discontinuous walls:** supporting columns need full-height special confining reinforcement (same as Cl 7.4.4).
- **Construction joints:** vertical reinforcement ratio across a horizontal construction joint **≥ (0.92/f_y) × (τ_v − P_u/A_g)** (τ_v = factored shear stress at the joint, P_u = factored axial force, positive for compression; A_g = gross cross-sectional area of the joint). *(Resolved 2026-09-11 audit, same page render as the coupling-beam formula above.)*
- **Splicing in walls:** avoid splicing vertical flexural steel in the yielding zone (extends l_w above the wall base, or 1/6 of wall height, whichever is more — capped at 2l_w). Where unavoidable, **≤ 1/3** of the vertical reinforcement spliced at one section, adjacent splices staggered **≥ 600 mm**. Lapped bars **> 16 mm diameter** need lateral ties — tie diameter **≥ 1/4 of the spliced bar, ≥ 6 mm**, spacing **≤ 150 mm**.

## Cross-references
- [[IS 1893 Part 1 - Earthquake Resistant Design]] — this is the code IS 1893 Cl 4.15.2 and Table 7 point to for "Special RC moment-resisting frame (SMRF)" and "ductile shear wall" classification; a structure claiming R=5.0 (SMRF) or R=4.0 (ductile shear walls) must actually be detailed per this code to earn that response reduction factor.
- [[IS 456 - Plain and Reinforced Concrete]] — this code modifies/overrides IS 456 provisions specifically for seismic ductility; base design (moment capacity calculations, shear strength Tables 13/14, splice mechanics per Cl 25.2.5.2) still comes from IS 456 unless explicitly changed here.
- Parent plan: Code Design Assistant.
