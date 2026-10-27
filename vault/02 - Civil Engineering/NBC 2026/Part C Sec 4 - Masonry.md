---
status: active
project: civil-engineering
type: reference
---
# Part C, Section 4 — Masonry

Structural design of unreinforced and reinforced load-bearing/non-load-bearing masonry walls (brick, block, stone), including earthquake-resistant detailing (prescriptive-band, confined, and reinforced masonry systems), rat-trap bond, and reinforced brick/RBC floors. Based primarily on IS 1905, IS 4326:2013, IS 17848:2022. PDF pages 661–796.

## 1 Scope (p. 665)
Covers structural design of unreinforced load-bearing/non-load-bearing walls; material selection and earthquake-resistant detailing for low-strength masonry; design of reinforced brick (RB) and reinforced brick concrete (RBC) floors/roofs; and reinforced load-bearing walls. **Does not apply to walls in mud mortar** (1.5, p. 665).

## 2 Terminology (p. 665–667)
Key definitions: **Pier** — thickened integral wall section, width ≤ 4× thickness (Fig. 1, p. 666). **Buttress** — projecting masonry pier decreasing in section base-to-top. **Curtain wall** — non-load-bearing, laterally loaded (Fig. 2, p. 666). **Cavity wall** — two leaves tied with metal ties. **Effective height/length/thickness** — the governing dimensions for slenderness ratio (see 4.3–4.5). **Slenderness ratio** — effective height or length ÷ effective thickness. **RB Slab / RBC Slab** — reinforced brick slab / reinforced brick + concrete-joint slab (Fig. 4, p. 668).

## 3 Materials (p. 667–670)
- Masonry units per Part B + accepted standards [C-4(1)]: common/fly-ash/PFA-lime/PFA-cement burnt clay bricks, stone, sand-lime bricks, concrete blocks, lime blocks, gypsum blocks (non-load-bearing only), AAC blocks, stabilized soil blocks (3.2.1, p. 669). Reused units not permitted unless cleaned and conforming (3.2.2).
- **Table 1 — Mortar grade minimum compressive strength (28 days)** (p. 669): H1=10, H2=6.0, M1=5.0, M2=3.0, M3=1.5, L1=0.7, L2=0.5 N/mm².
- **Table 2 — Mix proportions & strength of mortars** (p. 671–672): full cement:lime:pozzolana:sand ratio table for grades H1 through L2.
- Durability-driven mortar grade selection by exposure (3.4.2–3.4.7, p. 670): external walls exposed to rain w/o protection ≥ M2; internal load-bearing ≥ L1 (preferably M3); foundations below DPC per soil moisture (M3/M2/M1 escalating with dampness); machinery-vibration buildings ≥ M1; high parapets (h > 3t) ≥ M1; large-block bedding joints ≥ M1.

## 4 Design Considerations (p. 670–683)
- **4.2 Lateral support/stability**: lateral support must (a) limit slenderness, (b) resist overturning. Deemed-adequate anchoring details for RCC/timber floor bearing given in 4.2.1.2 with Fig. 5–7 (p. 673–674) — RCC slab bearing ≥ 90 mm, or metal ties 600 mm long, 6×30 mm section, ≤ 2 m spacing (≤1.25 m above 2 storeys).
- **4.2.2.2 Stability for ≤4-storey load-bearing buildings**: height:width ≤ 2; stiffening cross-walls per **Table 3** (p. 676): e.g. 100 mm wall → stiffening wall min 100 mm thick, max spacing 4.5 m (1–3 storeys); 200 mm wall → 6.0–8.0 m spacing depending on storeys.
- **4.2.2.6 Basement/plinth external walls**: brick crushing strength ≥ 5 N/mm², mortar ≥ M1, basement ceiling height ≤ 2.6 m, traffic surcharge ≤ 5 kN/m²; min thickness per **Table 4** (p. 677): up to 1.4–1.75 m ground height → 300 mm; up to 2–2.5 m → 400 mm (wall-loading dependent).
- **4.2.2.7 Free-standing/retaining walls**: stability moment ≥ 1.5× overturning moment if mortar can't take flexural tension.
- **4.3 Effective height** — **Table 5** (p. 678–679): full restraint top+bottom = 0.75H; full+partial = 0.85H; partial both ends = 1.00H; full at bottom only (parapets) = 1.50H.
- **4.4 Effective length** — **Table 6** (p. 681): continuous wall w/ cross-wall support = 0.8L up to 2.0L for free-one-end conditions.
- **4.5 Effective thickness**: solid/faced walls = actual thickness; stiffened walls use **Table 7** stiffening coefficient (p. 682, ratio Sp/tp-based, 1.0–2.0); cavity walls = ⅔ × sum of leaf thicknesses (4.5.4–4.5.5).
- **4.6 Slenderness ratio limits — Table 8** (p. 684): load-bearing wall ≤2 storeys: 27 (cement mortar) / 20 (lime mortar); >2 storeys: 27 / 13. **Columns: SR ≤ 12** (4.6.2).
- **4.7 Eccentricity**: no exact formula — engineering judgement per **Annex A** guidelines (p. 770).

## 5 Structural Design — Permissible Stresses (p. 683–689)
- **5.2 Design loads**: dead, imposed, wind, seismic — per Part C/Sec 1 (5.2.1).
- **5.3 Load dispersion**: max 30° from vertical (5.3.1). Lintel bearing ≥ 90 mm or L/10, whichever greater (5.3.3).
- **5.4.1 Permissible compressive stress** = basic stress (**Table 9**) × stress reduction factor ks × area reduction factor ka × shape modification factor kp.
  - **Table 9 — Basic compressive stress (N/mm², after 28 days)** (p. 685) — cross-checked against source PDF, verified accurate. By mortar type × unit crushing strength (3.5–40 N/mm²): e.g. H1 mortar: 0.35 (3.5 N/mm² unit) up to 3.05 (40 N/mm² unit); M2 mortar: 0.35–1.9; L2 mortar: 0.25–0.95. Valid for SR ≤ 6, zero eccentricity. Random rubble masonry = 75% of coursed value (Note 4).
  - ka = 0.7 + 1.5A (A = section area in m², when < 0.2 m²) (5.4.1.2).
  - **Table 10 — Stress reduction factor ks** (p. 686, verified) by slenderness ratio (6–27) × eccentricity/thickness ratio (0 to 1/3): ranges from 1.00 (SR 6) down to 0.22 (SR 27, e/t=1/6).
  - **Table 11 — Shape modification factor kp** (p. 687) by height:width of unit (up to 0.75 → 1.0; 2.0–4.0 → up to 1.8 for weak units).
  - 25% stress increase allowed for eccentricity ratio 1/24–1/6 (5.4.1.4).
- **5.4.2 Permissible tensile stress** (flexural only, never in water-retaining or earth-retaining structures): M1 mortar 0.07 N/mm² (vertical)/0.14 N/mm² (longitudinal); M2 mortar 0.05/0.10 N/mm².
- **5.4.3 Permissible shear stress**: fs = 0.1 + fd/6, capped at 0.5 N/mm² (mortar ≥ M1 only).
- **5.4.5–5.4.7**: specified compressive strength fm = 0.433·fb^0.64·fm0^0.36 (prism test per Annex B); elastic modulus Em = 550fm (clay) / 850fm (concrete block); shear modulus Gm = 0.2Em.
- **5.5 Design thickness**: solid, cavity (each leaf ≥75 mm, 5.5.1.2), faced, veneered wall rules (5.5.1.1–5.5.1.4). Free-standing walls (only in **Seismic Zone II**, mortar ≥ M1) may be sized without calculation from **Table 12 — max height:thickness ratio vs design wind pressure** (p. 689): ≤ 285 → **10**; 575 → **7**; 860 → **5**; 1 150 → **4**. *(The PDF prints the pressure column as "N/mm²" — that is a typo carried from IS 1905; the values are **N/m² (Pa)**, i.e. ~0.29–1.15 kN/m². Confirmed against PDF 2026-09-05.)* Height reckoned from 150 mm below ground level / top of footing; if a horizontal DPC near the base can't take vertical tension, use the greater of (ratio − 25 % from DPC level) or (ratio from the lower level).

## 6 General Requirements — Workmanship (p. 690–693)
- **6.3.4 Verticality tolerances**: deviation ≤ 6 mm/3 m storey height; total building height ≤ 12.5 mm; plan position ≤ 12.5 mm; inter-storey wall offset ≤ 6 mm; bed-joint level deviation ≤ 6 mm/12 m (max 12 mm).
- **6.5 Chases/recesses/holes**: vertical chase depth ≤ ⅓ wall thickness, horizontal ≤ ⅙ (6.5.3.2). Vertical chases: spacing ≥2 m apart, ≥345 mm from openings, ≥230 mm from stiffening cross walls (6.5.3.3). Horizontal chases: width ≤ 60 mm, only for SR ≤ 15, located in upper/lower middle third height, ≥600 mm from lateral support, max 1 m length, max 2 per wall, ≥500 mm mutual separation, total length ≤ ¼ wall length (6.5.3.4). No chase/recess/hole in half-brick load-bearing walls except minimum scaffolding holes (6.5.3.9).
- **6.6 Corbelling**: max projection ≤ ½ unit height; max horizontal projection ≤ ⅓ wall thickness; corbel load ≤ ½ load per unit length on wall above (6.6.1–6.6.2).

## 7 Reinforced Brick / RBC Floors and Roofs (p. 693)
Design/construction per good practice [C-4(7)] (IS 10440:1983).

## 8–11 Earthquake-Resistant Masonry (p. 693–768)
Four admissible earthquake-resisting systems: **MWB** (masonry walls with prescriptive bands), **MWBR** (+ vertical reinforcement), **CMW** (confined masonry walls), **RMW** (reinforced masonry walls). MWB/MWBR buildings capped at 15 m height / 4 storeys (p. 693).

**8.4.4 Building categories — Table 15** (p. 707): category B/C/D/E assigned by importance factor (1.0 or 1.5) × earthquake zone (II–V). E.g. Zone V + importance 1.0 → category E (max 3 storeys).

**8.4.4.1 Slenderness limits — Table 16** (p. 707): MWB/MWBR 15 (cat B/C) or 12 (cat D/E); CMW/RMW 15 (all categories); URM parapets 12 (B/C) or 6 (D/E).

**8.3.5 / 11.3.3 Staircases (earthquake detailing)** — directly relevant to general staircase design, p. 701:
- Stairs shall have sliding joints where they meet floors, to prevent the stair acting as unintended diagonal bracing that damages floors during shaking.
- Large stair halls should be separated from the rest of the building by separation/crumple sections.
- Three permitted construction types: (a) **Separated staircase** — one end on wall, other end on isolated columns/beams disconnected from floors, gap covered by sliding tread plate or crumple material (Fig. 18, p. 702); (b) **Built-in staircase** — cast monolithic with floors, protected by rigid walls enclosing the stair opening, extending full height to foundation (Fig. 19, p. 703); (c) **Sliding-joint staircase** — used where neither of the above is feasible.

**8.4.1–8.4.3 Design philosophy**: working stress method. **Table 14 — permissible stresses by wall type** (p. 705–706, verified against PDF) gives compression/tension/shear formulas per MWB/MWBR/CMW/RMW. Bands: 5 types — gable, roof, lintel, sill, plinth (8.4.2.1). Band width = wall thickness (min 200 mm), cover 20 mm, min depth 75 mm (2 bars) or 150 mm (4 bars) (8.4.2.2). Grade ≥ M25 concrete or 1:3 cement mortar reinforced brickwork.

**8.4.5, 8.5 Openings & reinforcement**: **Table 17** (p. 709) governs max opening ratio by building category/storeys (e.g. 1-storey: 0.60/0.55/0.50 for cat B/C/D,E). **Table 18** (p. 710) maps required strengthening measures (mortar grade, bands, vertical/jamb steel, bracing, dowels) to category × storeys. **Table 19** (p. 712) — longitudinal band steel: 2×8mm (span ≤5m, cat B) up to 4×12mm (span 8m, cat E). **Table 20** (p. 714) — vertical corner/junction steel diameter by storeys × category, up to 20 mm dia at bottom of 4-storey cat-E buildings.

**9 Confined Masonry Walls (CMW)** (p. 730–742): plan length:width ≤4, storey height <4m; ≥2 lines of walls each direction covering ≥50% of building dimension; wall thickness ≥110 mm, h/t ≤25; tie-columns at intersections, ≤1.5h or 4m spacing, and at free ends; tie-beams at every wall top, ≤4m spacing; horizontal lintel band mandatory if unsupported height >2.5m. Large opening (>10% panel area) handling per 9.1.6.2 — three tiered approaches by whether tie-columns confine the opening. Axial capacity formula (9.2.2.3) and shear (Table 26, p. 736) — *formulas in this subclause use math notation that didn't extract cleanly from the PDF (fractions/subscripts garbled) — **verify against PDF p. 731–741** before using for actual design calculations, don't rely on this note for the equations themselves.* Load combinations **Table 27** (p. 736): DL+IL; DL+EL; DL+0.8IL+0.8EL. Min longitudinal reinforcement in tie-columns/beams: 0.8% gross c/s area (2-storey: 0.6%) (9.2.2.13). Required Wall Index **Table 28** (p. 745): Zone II 0.7%, III 1.1%, IV 1.6%, V 2.4%.

**10 Reinforced Masonry Walls (RMW)** (p. 749–758): min wall thickness 230 mm; parapet ≥200 mm thick, height ≤3×thickness; SR ≤27 (walls), ≤15 (unreinforced column) / ≤20 (reinforced column); **Table 29** (p. 752) span:depth ratios by boundary condition. Steel allowable stresses (10.3.2): MS bars 140 MPa (≤20mm dia)/130 MPa (>20mm); HSD bars 0.55fy tension, 190 MPa compression. Min/max vertical reinforcement in columns: 0.25%–4% of net area, min 4 bars (10.3.8.3.1). **Table 30** (p. 758) permissible shear stress with/without web reinforcement. **Table 31** (p. 758–759) — three reinforced-wall grades RMB1/2/3 with R-values 2.5–3.0 by earthquake zone.

**11 Low-Strength Masonry Buildings** (p. 760–768): covers weak-mortar brickwork and random rubble/half-dressed stone. Not permitted for important buildings; avoid for category D, prohibited for category E. Brick compressive strength ≥3.5 MPa (11.6.2.1); mortar lime-sand 1:3 or clay mud (11.6.2.2). Height limits by category (11.6.2.4): cat B/C — 3 storeys flat roof / 2+attic pitched; cat D — 2 storeys / 1+attic. Stone masonry wall thickness ≤450 mm, preferably ~350mm (11.6.3.3); through-stones every 600mm lift, ≤1.2m apart (11.6.3.5). Opening limits **Table 32** (p. 766–767); strengthening measures **Table 33** (p. 767); vertical steel diameters **Table 34** (p. 768, up to 12mm dia).

## 12 Rat-Trap Bond Masonry (p. 769, detailed in Annex G, p. 783–790)
Applicable ≤2 storeys in seismic zones II–III only (non-load-bearing elsewhere). 80 mm cavity between staggered stretcher/header courses (Fig. 85, p. 784). Bricks ≥6.0 MPa compressive strength, mortar grade H2. Bed joint ≤12 mm thick. Compressive strength assessed via prism test, divided by 4 for basic compressive stress (G-4.4, G-7).

## 13 Sustainability (p. 769)
Embodied-carbon quantification per NBCS "Handbook on Approach to Sustainability" — no numeric targets given in this Section itself.

## Annexes (p. 770–792)
- **Annex A** (p. 770) — eccentricity-of-loading assessment guidelines (no formulas, judgement-based rules of thumb).
- **Annex B** (p. 770–771) — prism test method for compressive strength; **Table 35** correction factors for h/t ratio (0.73–1.37).
- **Annex C** (p. 771–772) — concentrated load dispersal & bed-block criteria (M20 grade bed blocks).
- **Annex D** (p. 772–774) — approximate design of non-load-bearing panel/curtain/partition walls; **Table 36/37** bending-moment coefficients by panel H/L ratio.
- **Annex E** (p. 774–778) — iterative method for walls under combined flexure+axial load. *Formulas extracted with heavily garbled sub/superscripts — **not usable from this note, go to PDF p. 774–778 directly** if you need this method.*
- **Annex F** (p. 780–782) — lateral force distribution in piers via relative rigidity (cantilever vs fixed-end formulas). *Same caveat — verify against PDF, symbols didn't extract cleanly.*
- **Annex G** (p. 783–790) — rat-trap bond construction detail (see §12 above).
- **Annex H** (p. 790–792) — notation/symbol glossary.
- **List of Standards** (p. 792–794) — ~30 IS standards referenced, mainly IS 1077 (bricks), IS 2185 (concrete blocks), IS 2250 (mortars), IS 2212 (brickwork practice), IS 4326:2013 (earthquake), IS 17848:2022 (confined masonry), IS 883:2016 (timber), IS 1904:2021 (foundations).

## Cross-references
- Materials → Part B "Building Materials" (3.1, p. 667).
- Loads, load combinations, seismic zone factors, importance factor, structural irregularities → Part C/Section 1 "Loads and Load Effects" (5.2.1, 8.1.6, 8.1.7, 8.2.4.1, 9.2.2.1, and throughout Section 8/9/10).
- Foundations design → Part C/Section 2 "Soils and Foundations" (8.3.3.1, 9.3.1).
- Ductile detailing, concrete stress-strain, structural concrete design, RCC bands/slabs → Part C/Section 5 "Structural Concrete" (8.2.7, 8.4.3, 9.2.2.8, 9.2.2.10, 10.3.5.4).
- Fire resistance of masonry walls → Part F "Fire and Life Safety" (6.2, 8.2.9, 11.2.5; also G-4.9 referencing separate good-practice standard).
- Thermal/sound insulation of walls → referenced good-practice standards, not this NBCS directly (6.2, G-4.8, G-4.10).
