---
status: active
project: civil-engineering
type: reference
---
# Part C, Section 3A — Timber

Structural design of timber in buildings: species classification and permissible stresses, permissible-stress modification factors, member design (beams, columns, ties), joint design (nails, bolts, connectors, glued/finger joints), plywood/sandwich/lamella construction, termite protection, and (new in this 2026 revision) cross-laminated timber, mass timber, and life-cycle assessment. PDF pages 493–606. Source: `NBC 2026- Vol-1 & 2.pdf`; full extracted text at `<local extracted text>\NBC 2026\NBC-2026-fulltext.txt`.

## 1 Scope (p.497)
Covers general principles of structural timber design in buildings, including fastener-connected elements. Design may be based on analytical/engineering principles or reliable test data; timber strength-group classification doesn't bar using better-substantiated data for a specific timber/grade.

## 2 Terminology (p.497–500)
Full glossary of ~35 structural terms (glulam, bressummer, diaphragm, finger joint, laminated veneer lumber, spaced column, stressed skin, etc.) and ~24 timber-defect terms (check, decay, knot types, shake, wane, warp) at p.497–500. Not reproduced here — open PDF at p.497 for exact wording of a specific definition.

## 3 Symbols (p.500–501)
Standard symbol list for the section's formulas (fb, fc, fcp, fcn, K1–K10, etc.) — see p.500–501 when working through a formula below.

## 4 Materials (p.501–536)

### 4.1 Species classification (Table 1, p.502–531) — **verify against PDF, do not use as final design values**
Table 1 lists ~150 Indian timber species (Groups A, B, C) with: locality tested, average density, moisture content, modulus of elasticity, permissible stresses (bending-tension, shear, compression parallel/perpendicular to grain — each split by Inside/Outside/Wet location), durability class, treatability grade, and seasoning behaviour class. This table spans 30 PDF pages in a dense 20-column layout — **extraction of individual cell values is high-risk for column misalignment**; the raw pdfplumber cross-check confirms the table exists at these pages but do not trust auto-extracted per-species numbers for real design work. For any specific species (e.g., Teak, Sal, Deodar), open PDF pp.502–531 directly or ask and it can be pulled fresh.

Group definition (4.1.1, p.528, this formula IS reliable):
- **Group A** — E > 12.6 kN/mm², fb > 18.0 N/mm²
- **Group B** — E 9.8–12.6 kN/mm², fb 12.0–18.0 N/mm²
- **Group C** — E 5.6–9.8 kN/mm², fb 8.5–12.0 N/mm²

### 4.3 Nail lateral strength — Tables 2 & 3 (p.528–532) — verify against PDF
Permissible lateral strength (double shear) of mild steel wire nails, by species, for two nail sizes (3.55/4mm dia and 5mm dia). ~100 species each table. Same column-misalignment caution as Table 1 — pull exact species value from PDF pp.528–532 when needed.

### 4.4 Moisture content — Table 4 (p.533)
India divided into 4 humidity zones (I <40%, II 40–50%, III 50–67%, IV >67% avg annual RH). Permissible moisture content:

| Use | Zone I | Zone II | Zone III | Zone IV |
|---|---|---|---|---|
| Structural elements | 12% | 14% | 17% | 20% |
| Doors/windows ≥50mm thick | 10% | 12% | 14% | 16% |
| Doors/windows <50mm thick | 8% | 10% | 12% | 14% |
| Flooring strips (general) | 8% | 10% | 10% | 12% |
| Flooring strips (tea gardens) | 12% | 12% | 14% | 16% |

### 4.5 Sawn timber sizes (Tables 5, 6, 7, p.533–534)
Preferred cut sizes (thickness × width, mm) for: roof trusses spans 3–20m (Table 5), purlins/rafters/floor beams (Table 6), partition framing/centering (Table 7). Tolerances: ±3/0mm (width/thickness ≤100mm), +6/−3mm (>100mm), +10/0mm (length).

### 4.6 Grading — Table 8 (p.535–536)
Three grades: Select, Grade I, Grade II, by permissible defects:
- **Wane**: ≤1/8 (Select), ≤1/6 (Grade I), ≤1/4 (Grade II) of surface width.
- **Slope of grain**: ≤1 in 20 (Select), ≤1 in 15 (Grade I), ≤1 in 12 (Grade II).
- **Live knots**: max size scales with face width — see Table 8 at p.535 for the full size table by face width (75–600mm) and grade.
- **Prohibited in all grades**: loose grains, splits, compression wood (conifers), heartwood/sap rot, crookedness, powder-post-beetle worm holes, pitch pockets.

### 4.7–4.9 Suitability, fastenings, other requirements (p.536–537)
Durability/treatability choice rules for permanent structures (first/second choice combos) and temporary structures; general fastening principles (nails, screws, bolts, timber connectors, adhesives).

## 5 Permissible Stresses (p.537–539)
- Base permissible stresses (Table 9, p.538, Grade I): by Group A/B/C — e.g. bending/tension inside location: A=18.0, B=12.0, C=8.5 N/mm²; compression parallel to grain inside: A=11.7, B=7.8, C=4.9 N/mm²; E: A=12.6, B=9.8, C=5.6 (×10³ N/mm²).
- Grade multipliers (5.3): Select ×1.16, Grade II ×0.84. Low-durability timber on outside locations: additional ×0.80.
- **K1 — slope of grain** (Table 10, p.538): 1 in 10 → 0.80 (beams)/0.74 (columns); 1 in 12 → 0.90/0.82; 1 in 14 → 0.98/0.87; 1 in 15+ → 1.00/1.00.
- **K2 — duration of load** (Table 11, p.539): continuous 1.0, 2 months 1.15, 7 days 1.25, wind/earthquake 1.33, instantaneous/impact 2.00.

## 6 Design Considerations (p.539–545)
Loads per Part C Sec 1 (Loads and Load Effects) — see [[Part C Sec 1 - Loads and Load Effects]]. Wind and seismic not considered simultaneously.
- **Flexural members**: min width ≥50mm or L/50; depth >3× width needs lateral restraint (spacing ≤50× width). Form factors K3 (rectangular), K4 (box/I-beam), K5=1.18 (circular), K6=1.414 (square, diagonal load).
- **Notching**: top/bottom notches ≤1/5 depth, ≤span/6 from support; holes ≤1/4 depth in middle third.
- **Bearing**: min 75mm length on masonry/concrete; K7 factor (Table 13, p.544) for bearings <150mm: 15mm→1.67 down to 150mm→1.00.
- **Deflection**: brittle finishes (gypsum/slate/tile/asbestos) ≤L/360; other members ≤L/240; cantilevers ≤L/150 of hanging length. Long-duration deflection check uses 2× dead load.
- **Columns**: short (S/d≤11), intermediate (11<S/d<K8), long (S/d>K8); S/d shall not exceed 50 (solid), 80 (spaced). Separate formulas for box columns (6.6.2) and spaced columns (6.6.3, restraint factor 2.5–3).
- **Combined bending+axial**: interaction check fac/fc + fab/fb ≤ 1 (compression); fat/ft + fab/fb ≤ 1 (tension).

## 7 Design of Common Steel Wire Nail Joints (p.547–555)
Mono-chord/split-chord construction up to 15m spans. Min member thickness: 30mm (mono-chord main), 20/25mm (split-chord web/chord). Nail diameter: 1/11 to 1/6 of thinnest member thickness. Spacing tables (Table 14, p.548) and figures (Figs. 4–6) for lengthening and node joints, keyed to nail shank diameter `n` (e.g. end distance 12n tension / 10n compression). Rigid joint minimum: 2 nails (nodal), 4 nails (lengthening).

## 8 Design of Nail Laminated Timber Beams (p.555–558)
Planks 20–30mm thick, max depth 250mm, max length 2000mm, staggered joints ≥300mm apart. Table 15 (p.556) gives plank count/thickness/nail size vs overall beam width (50–150mm). Deflection limits tighter than clause 6: brittle finishes L/480, other members L/360 (beams/joists), L/225 (cantilevers).

## 9 Design of Bolted Construction Joints (p.559–563)
Critical/net section = cross-section minus bolt-hole projected area. Bolt bearing strength depends on t'/d3 ratio (Table 16, p.559) and bolt diameter factor df (Table 17, p.560). Min thickness: 40mm (main, mono-chord), 20mm (side members). Min 2 bolts (nodal), 4 bolts (lengthening). Spacing per Fig. 9 (p.562): 4d3 in-row, 7d3/5d3/4d3 end distance (softwood tension/hardwood tension/compression). Retightening required after 1 year, then every 2–3 years.

## 10 Design of Timber Connector Joints (p.563–568)
Split-ring metal connectors and wooden disc-dowels for large-span heavy joints. Main member ≥57mm, side member ≥38mm thick. Strength governed by tension/compression/shear area at the connector (formulas p.565). Disc-dowel: thickness 25–35mm, diameter 3.25–3.5× thickness, edge clearance 12–20mm. Recommended dowel species: Babul, Dhaman, Irul, Sissoo, Rosewood, Sandal, Axle-wood, Padauk, Yon. All-timber joints (for chemical-corrosion environments): timber bolt = 66% of MS bolt safe load; bamboo pin = 56%.

## 11 Glued Laminated Construction (p.568–572)
BWP (boiling water proof) grade adhesives mandatory for Indian tropical/humid conditions. Manufacturing sequence: dry → plane → end-joint → machine → dry-assemble → glue → press → cure → finish. Design outline for horizontally laminated beams given step-by-step (p.570–571): assume b:d≈1:4, solve bd² = WL/8 × 6/fb, check deflection at 2×dead load + imposed load, target deflection ≈0.003×span. Typical camber = span/400.

## 12 Laminated Veneer Lumber (p.572–573)
Density 600–750 kg/m³. Strength requirements (Table 20, p.573): MOR ≥50 N/mm², MOE ≥7500 N/mm², compressive strength parallel to grain ≥35 N/mm², tensile strength parallel to grain ≥55 N/mm², horizontal shear ≥6/8 N/mm² (parallel/perpendicular to laminae).

## 13 Glued Finger Joints (p.573–577)
V-shaped tapered fingers, glued on side grain (shear-stressed glue line, not tension). Typical geometry: 50mm long, 12mm pitch, tip angle 6°. Interior use: melamine-formaldehyde-cross-linked PVA; exterior/humid: phenol-formaldehyde or resorcinol-formaldehyde.

## 14 Structural Use of Plywood (p.575–577)
6mm ply for sheathing/webs/stressed-skin; 9–12mm for beams/flooring diaphragms. PF/PRF adhesive for glued components.

## 15 Trussed Rafter (p.577–579)
Low-pitch trusses with nail-ply/bolt-ply plywood gusset joints, spaced closely, self-supporting at ends (no internal load-bearing walls needed). Design per Group C standard-grade timber, loads per Part C Sec 1. India-specific additions in this revision: match species to climatic zone (humid/dry/coastal), prefer local durable hardwoods (Teak, Sal, Neem), termite-resistant chemical treatment + fire-retardant coating recommended.

## 16 Structural Sandwiches (p.580–583)
Two thin high-strength facings bonded to a lightweight core (shear-carrying); design analogous to I-beam (facings = flanges, core = web). Table 22 (p.581–582) gives lateral nail-bearing strength for plywood-to-timber composite joints — verify against PDF for exact values (Sal/Chir species tabulated).

## 17 Lamella Roofing (p.583–591)
Arched roof of short bevelled/bolted timber planks ("lamellas") forming a two-hinged arch grid — full worked design method given (horizontal thrust via two methods, resultant thrust, max bending moment at crown and at 22.6° from centre line, lamella sizing, bolt sizing at nodal joints, steel washer sizing). Practical limits: lamella length 1.0–2.5m, thickness 25–50mm, width 100–250mm; skew angle 19–21° (diamond angle 38–42°), spacing per Table given for those angles.

## 18 Nail and Screw Holding Power of Timber (p.591–594)
Table 23 (p.592–594): composite nail/screw holding power (N) for ~70 Indian species, from standard test specimen (150×50×50mm, 50mm/2.5mm nail, No.8 screw, 25mm penetration). Verify against PDF for a specific species.

## 19 Protection Against Termite Attack in Buildings (p.594–595)
~12 of 250 recorded Indian termite species cause ~90% of building damage; subterranean termites are most destructive; 95% of damage is via internal upward travel from the ground rather than external entry. Chemical soil poisoning around/under foundations is standard practice. Non-chemical measures: periodic visual inspection of termite galleries, metal shields at plinth level, continuous floor slabs/apron floors/termite grooves at building periphery.

## 20 Cross-Laminated Timber — CLT (p.595–600) — new in this revision
≥3 layers solid-sawn/structural composite lumber, cross-oriented, adhesive-bonded, odd number of layers (3/5/7...). Kiln-dried to 12%±2% MC. Thickness 50–500mm; panels up to 18m × 3m. Delamination limits: total ≤10%, max ≤40%. Density range 5500–8500 kg/m³ depending on species (Table 26, p.597: Rubberwood, Melia dubia, Eucalyptus, Silver oak tested against Radiata pine benchmark — all comparable). Fire: charring rate 0.65 mm/min for load capacity during fire exposure; gypsum board encapsulation (≥13mm) is one accepted protection method — cross-ref [[Part F - Fire and Life Safety]]. Preservative treatment (bifenthrin, copper chrome borate) essentially eliminates termite degradation (Table 29, p.599: untreated CLT 100% degraded by 9 months; bifenthrin-treated 0% at 36 months).

## 21 Mass Timber (p.600–601) — new in this revision
Umbrella term covering CLT, glulam, NLT (nail-laminated timber), LVL used for primary structure (floors/walls/roofs/columns). Min dimensions: columns 200mm, beams 150mm, floor CLT 100mm, roof CLT 85mm, wall CLT/NLT 125mm. Design per Part C Sec 1 for all load types including seismic — timber's flexibility can aid seismic performance but connections must be robustly detailed. All steel connectors need fire protection (coating or encasement). Sustainability angle: carbon sequestration, better thermal insulation than steel/concrete allowing thinner wall assemblies.

## 22 Life Cycle Assessment (LCA) of Timber (p.601–603) — new in this revision
Required to cover: production/construction, use stage, end-of-life, and externalized impacts beyond system boundary. Impact categories: Global Warming Potential, Acidification Potential, Eutrophication Potential, Ozone Depletion Potential, Smog Formation Potential. Tools cited: SimaPro, MATLAB. Must document assumptions/methodology/conclusions for stakeholders.

## Annex A — Mechanical Properties of Foreign Timber Species (p.604) — new in this revision
Table 30: only 2 species tabulated so far (Douglas fir, Western hemlock — from USDA Wood Handbook), explicitly flagged as reference-only with **no Indian test data**; verify by lab testing before structural use in India.

## List of Standards (p.605–606)
Indian Standards underpinning this section include IS 707:2011 (glossary), IS 1708:1986 (test methods), IS 3629:1986 (structural timber spec), IS 401:2001 (preservation code), IS 2366:1983 (nail-jointed construction), IS 4983:1968 (nailed laminated beams), IS 11096:1984 (bolt-jointed construction), IS 4907:2004 (connector joint testing), IS 14616:1999 (LVL spec), IS 10701:2012 (structural plywood), IS 6313 Parts 1–3 (anti-termite measures). Full list with all ~20 references at p.605–606.

## Cross-references
- Loads/load combinations: Part C, Section 1 — Loads and Load Effects, p.155–382 → [[Part C Sec 1 - Loads and Load Effects]]
- Fire protection of timber buildings and CLT fire-resistance ratings: Part F — Fire and Life Safety → [[Part F - Fire and Life Safety]]
- Nail specification: Part B — Building Materials → [[Part B - Building Materials]]
- Section 3B — Bamboo begins immediately after this section (PDF p.607) → [[Part C Sec 3B - Bamboo]]
