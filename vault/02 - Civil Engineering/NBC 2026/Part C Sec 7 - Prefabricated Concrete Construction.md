---
status: active
project: civil-engineering
type: reference
---
# Part C, Section 7 — Prefabricated Concrete Construction

PDF pages 1179–1524 span this Section (1179–1328 covered in this note); covers prefabrication systems, structural design of precast concrete, joints/connections, construction planning, manufacture/storage/transport/erection, QA/QC and testing for prefabricated concrete elements in buildings. Based on IS 15916:2026 (emulative detailing approach only — jointed/welded-bolted systems are **not** covered by this Section; clause 8.2.2 explicitly excludes jointed systems).

## 1 Scope (p. 1183)
Covers prefabrication systems, design, tolerances, joints, manufacture, storage, transport, erection. Limited to the **emulative detailing approach** (precast connected at site with wet concrete/grout, detailed to match cast-in-situ behaviour) — cl 1.2. Alternative jointed detailing needs competent-authority approval + testing (1.4).

## 3 Terminology (p. 1183–1186)
Key definitions: Basic Module = 50 mm (symbol M) (p. 1183); Emulative Detailing System vs Jointed Detailing System (jointed connections not allowed under this Section unless tested per cl 10 — p. 1184); full glossary of 3D-printing terms (extrusion-based printing, binder jetting, buildability, extrudability, pumpability, printability, open time, filament, layer, bond, shape stability, dead zone length) at 3.22, p. 1185–1186.

## 5 Materials (p. 1186–1192)
- **Cement/aggregates/water/admixtures**: per Part C Sec 5 (Structural Concrete) unless noted; chloride-bearing admixtures banned (5.1.5.2); for stitch joints <75 mm thick, max aggregate size = 10 mm (p. 1187).
- **Grout** (5.4): non-shrink non-metallic grout mandatory for structural joints <50 mm gap; grout strength ≥ joining member strength +5 MPa (whichever governs). Joints >50 mm: 10 mm aggregate concrete or self-compacting/micro concrete.
- **Moulds** (5.5): must hold tolerances through repeated use; jacking-against-mould designs must resist buckling.
- **Hardware/lifting devices** (5.6): lifting inserts sized by manufacturer safe working load; reinforcing bars used as main reinforcement **shall not** double as lifting hooks (5.6.2.3). Sealants: polyurethane/hybrid — elongation ≥200% (grouted joints) or ≥400% (non-grouted) (5.6.3.7).
- **Insulation**: rigid foam (EPS/XPS/PU) strength >10 MPa allowed in flooring; mineral wool for fire/acoustic performance.
- **Connections** (5.7): wire loop/loop-box systems are non-structural, gravity/durability use only (5.7.1.1); grouted couplers (5.7.2), grout-filled/dowel tubes (5.7.3), headed bars/terminators (5.7.4), metal inserts (5.7.5), shims — plastic ≤40 mm, metal >40 mm tack-welded (5.7.6).

## 6 Precast Concrete Systems (p. 1193–1208)
- **6.2** System selection via **Table 1** (p. 1193, verified against pdfplumber tables file, TABLEPAGE 1195) — moment frame, structural wall, dual, and cell systems, each split ordinary/ductile. Key seismic notes: OMRF response reduction factor R=2 for cantilever column systems (Note 1); **OMRF not permitted in Seismic Zone III and above** (Note 2) — ductile detailing mandatory there; **Seismic Zone IV+ precast systems need institute-of-repute approval** (Note 8).
- **6.3.4 Skeletal frames**: 5 beam-column connection types (Fig. 1, p. 1196–1199) — Type A (A1–A4 subsystems, corbel-supported), Type B (beams through columns, spliced at contraflexure), Type C (monolithic cruciform/portal units, C1–C3).
- **6.3.6 Floor/roof diaphragm systems**: minimum structural topping = **75 mm** (Seismic Zone III+) or **50 mm** (Zone II), min 6 mm rebar, welded wire mesh avoided in Zone III+ (6.3.6.1, p. 1196). Hollow-core slab (HCS), double-tee, solid slab, and one/two-way composite slab systems described (Fig. 7–8, p. 1202–1204). **See also Annex H for mandatory HCS detailing.**
- **6.4 Hybrid systems**: PRESSS (post-tensioned precast seismic system, Systems 1 & 2, Fig. 9–10) and mixed cast-in-situ/precast or steel systems (Fig. 11) — both require full-scale testing + competent-authority approval.
- **6.5 Advanced systems**: 3D-printed (→ Annex B), Cell/volumetric systems (→ Annex C, PPVC), DFMA (→ Annex D).

## 7 Structural Analysis (p. 1208–1244)
- **7.2 Loads**: per Part C Sec 1 (Loads and Load Effects). Minimum construction/traffic load = **1.0 kN/m²** if unspecified (7.2.1.2/7.2.1.4). Notional horizontal load ≥ **1.5% of characteristic dead load** (7.2.1.6, Fig. 12).
- **7.6 Stability**: overturning/sliding per Sec 5; grout must reach ≥50% design strength before further loading (7.6.1g).
- **7.7 Durability / Table 2 Nominal Cover** (p. 1215, **verified against extracted table data**):

| Exposure | Elements | Min cover (mm) |
|---|---|---|
| Mild | All | 20 |
| Moderate | Slabs and walls | 25 |
| Moderate | Ties/stirrups, beams & columns, exposed to weather | 25 |
| Moderate | Ties/stirrups, beams & columns, not exposed | greater of bar dia. or 20 |
| Severe | All | 40 |
| Very Severe | All | 45 |
| Extreme | All | 70 |

  (These are *lower* than IS 456 cover values — permitted only because precast is produced in a controlled environment, cl 7.7.4 note 1.)
- **7.8 Fire resistance**: expressed in hours per good practice; joints >50 mm wide follow standard fire provisions; structural-wall joints ≤50 mm need grout ≥50 MPa (or +5 MPa over element strength).
- **7.9 Structural design of components**: footings, walls, shear walls, floors/slabs, columns, beams, **staircase/landing (7.9.7, p. 1218 — design per Part C Sec 5, connections per cl 8)**, composite construction, insulated/sandwich panels (min wythe thickness 50 mm), composite floors, others.
- **7.10 Diaphragm design**: rigid vs flexible diaphragm criteria (7.10.4/7.10.5 — flexible if lateral displacement >1.5× average); min topping grade **M40** (7.10.9.2); collectors (7.10.13); max reinforcement spacing = lesser of 5×diaphragm thickness or 450 mm.
- **7.11 Bearing design**: net bearing width ≥40 mm; effective bearing length = least of actual length, ½ length+100mm, or 600mm (7.11.3); design ultimate bearing stress = 0.4fck (dry), 0.6fck (mortar-bedded), 0.8fck (steel plate) (7.11.4). **Table 3/4 spalling allowances** (p. 1226, verified) — e.g. concrete <M30 support: 25 mm ineffective distance; steel: 0. Construction-inaccuracy allowances (7.11.10): 15mm/3mm-per-m (steel/precast), 20mm/4mm-per-m (masonry), 25mm/5mm-per-m (in-situ concrete). Dapped ends (7.11.15, Fig. 22–24) and ledges (7.11.16, Fig. 25–27) have detailed shear/hanger reinforcement formulas — **these are calculation-heavy; consult PDF directly (p. 1229–1237) for the actual design when applying to a real member.** Corbel design (7.11.17, Fig. 28): aᵥ/d ≤1, Nᵤ≤Vᵤ limits.
- **7.12 Shear friction** (p. 1239–1240): **Table 5/6 verified** — coefficient of friction μ: monolithic concrete = 1.4; hardened+intentionally roughened (≥6mm amplitude) = 1.0; hardened, not roughened = 0.6; against as-rolled steel with studs/welded bars = 0.7.
- **7.14 Handling/demoulding design — key tables (verified)**:
  - **Table 7** (demoulding load factors, p. 1241): flat/no rebate 1.2–1.3; flat with rebates 1.3–1.4; fluted 1.4–1.6; sculptured 1.5–1.7.
  - **Table 8** (dynamic handling factors, p. 1242): yard handling 1.2; transportation 1.5; erection 1.2.
  - **Table 9** (min concrete strength for lifting, p. 1242): unspecified/non-prestressed 10 MPa*; high-impact lifting 15 MPa*; concentrically prestressed 20 MPa; eccentrically prestressed 25 MPa; highly stressed prestressed 30 MPa (*depends on insert/anchor).
  - **Table 10** (lifting insert factors of safety, p. 1243): bracing members 2; bracing connections/inserts 3; lifting inserts normal use 4; lifting inserts multi-use 5; rebar inserts single-use 2, multi-use 4.

## 8 Joints and Connections (p. 1244–1259)
- **8.1** Force transfer categories: compression (8.1.1 — dowel spacing ≤¼ wall length or 450mm; column ≥4 corner bars 12mm+ continuous foundation-to-roof via Class H coupler), tension (8.1.2), shear (8.1.3 — adhesive bond never counted), moment (8.1.4).
- **8.3.5 Table 11 bond coefficient β** (p. 1248, verified): plain bar 0.28 (tension)/0.35 (compression); deformed bar 0.4/0.63.
- **8.5 Structural integrity / progressive collapse — mandatory tie forces (p. 1250–1258)**:
  - Peripheral tie: within 1.2 m of building edge, force = lesser of 60 kN or (20+4N) kN, N=storeys.
  - Internal ties: two directions, formula-based, at least Ft.
  - Horizontal ties to columns/walls: greater of 2Ft (or Ls×Ft/2.5 for walls) or 3% of ultimate vertical load.
  - Vertical ties: ≥50 kN per horizontal metre of wall; ≥2 integrity ties per wall panel; columns need tensile strength 1.4×Ag (gross area, min ½ Ag for oversized columns).
  - **Vehicle impact load: 27 kN un-factored, any direction, at 450–700mm height, on ≤300×300mm area** (8.5.11f) — relevant for ground-floor precast columns near traffic.
  - Key element check (8.5.12, buildings ≥5 storeys): if failure of an element would collapse >70 m² or 15% of storey area, design that element for **36 kN/m²**.
- **8.6 Joint sealants/widths**: min practical sealant joint = 10 mm; min widths — 10mm unspecified, 20mm walls, 30mm columns, ≤50mm larger elements (8.6.2.1).

## 9 Construction Planning (p. 1259–1265) — pre-engineering, resource/production/haulage/crane planning, on-site surveying, BIM tracking. Largely procedural, no binding numeric limits beyond project-specific factors (e.g., typical trailer capacity 25–35 MT, height clearance 3.6–4m, per 9.3.1 — indicative, not mandatory).

## 10 Construction, Manufacture, Storage, Transport, Erection (p. 1265–1278)
- **10.2.2 Table 14 casting tolerances** (p. 1270–1271, verified) — varies by product key (19 product types); length tolerances range ±2mm (short cellular slabs) to ±15mm (foundation units/drains); full table in PDF, cite by Key No. when applying.
- **10.2.3** Mould wall slope: ideally 1:6, minimum 1:12.
- **10.3 Accelerated curing**: steam curing max heating rate 30°C/h to 75–80°C (low pressure) with max concrete-to-ambient ΔT of 60°C (≤M30) or 75°C (≥M45); vacuum treatment suction ≤70% atmosphere for 20–30 min/cm thickness.
- **10.3.9 Stacking**: vertical stacking limited to 6–10 units; ground bearing capacity min 5 t/m² (unpaved), max 15 t/m² (compacted), max 30 t/m² (PCC layer); A-frame slope 75°–80°.
- **10.7.6 Table 15 erection tolerances** (p. 1276, **corrected via verified table data** — the plain-text extraction jumbled this table's rows): level differences/plumb/bearing/joint dimensions all ±5mm; **max accumulated deviation: ≤10-storey buildings = 1/1250 of height/length or ±20mm (lesser); >20-storey = 1/1250 or ±50mm (lesser)**; plan location ±10mm (columns), ±15mm (beams).
- **10.8 Design considerations**: demoulding not allowed until concrete reaches ≥1.25× the stress it will see at demoulding.
- **10.10 Mixed/composite construction**: combinations with steel, timber, masonry; hybrid core+precast frame for high-rises.

## 11 Quality Assurance / 12 Testing (p. 1278–1286)
- **12.1 Sampling — Table 16** (p. 1281, verified): lot ≤100 → sample 5, first-rejection 2; 101–300 → 8/2; 301–500 → 13/2; ≥501 → 20 (first)/20(second), rejection 3/4.
- **12.2 Load testing individual units**: 24h at 1.25× (dead+imposed) design load; deflection recovery ≥75% (non-prestressed) or ≥85% (prestressed, within 3h).
- **12.3 Table 17 cyclic test for grouted couplers** (p. 1283, LFRS use): Stage I 0.95fy tension/0.5fy compression ×20 cycles; Stage II 2εy/0.5fy ×4; Stage III 5εy/0.5fy ×4; Stage IV load to failure. LFRS grout strength ≥90 MPa.
- **12.4 Floor load testing**: 24h at 1.25× design imposed load; recovery ≥75% (retest at 72h if not, must reach ≥80% or strengthen); prestressed ≥85%.
- **12.5 Water-tightness — Table 18** (p. 1285, verified): test frequency by building height — ≤10 storeys: 5 tests; ≤20: 10; ≤30: 15; ≤40: 20; ≤50: 25 joints. Floor/roof/toilet slabs: 5% tested by 4h ponding, depth ≥25mm or joint-thickness+10mm.

## Annexes (p. 1286–1327)
- **Annex A** — Symbols/notation (p. 1286).
- **Annex B** — 3D-printed concrete structures: extrusion-based only; load-bearing 3D-printed walls limited to **≤12 m building height** without special approval (B-4.4); min wall thickness 100 mm.
- **Annex C** — Prefabricated Prefinished Volumetric Construction (PPVC): module dimensions typically 3–12 m (L) × 2.5–3.5 m (W) × 2.5–4.5 m (H); transport max width 2.5m, height 4.5m (incl. truck), length 18m; min 20mm joint at foundation.
- **Annex D** — Design for Manufacturing & Assembly (DFMA) guidance, facade/structural standardization principles (non-mandatory).
- **Annex E** — Common precast connection details, Fig. 44–56 (illustrative only).
- **Annex F** — **Table 19 common defects/causes/remedies** (p. 1313–1319): dimensional deviation, cracks, chip-off, honeycombing, missing details, strand slippage, alignment — each with recommended mould-thickness guidance (steel mould: 4.5mm up to 50 casts, 6mm to 100, 9mm to 200) and remedy procedures.
- **Annex G** — Sustainability: recycled aggregates, renewable energy in factories, waste/pollution reduction, SCMs, geopolymer concrete.
- **Annex H** — **Mandatory HCS (hollow-core slab) detailing** (p. 1322–1323): HCS must be simply supported only (no continuous flooring use, H-2.1); structural topping mandatory; only the topping counts toward diaphragm action, never the HCS itself (H-2.3); min bearing = **80 mm** (H-3.3); starter bars extend 600mm from support face, 8mm dia (slabs ≤300mm depth) or 10mm (>300mm), spacing ≤250mm; min 2 cores opened 600mm at both span ends, filled with topping; linking slab length ≥6× topping thickness.

## List of Standards (p. 1324–1326)
40 referenced IS standards, cross-referenced throughout as [C-7(n)] — notably IS 13920:2016 (ductile detailing), IS 456:2000 (RCC code), IS 1343:2012 (prestressed concrete), IS 16172:2023 (rebar couplers), IS 4326:2013 (earthquake-resistant construction), IS 1641/1642:2013 (fire safety). Full list in PDF p. 1324–1326 if a specific standard number is needed.

## Cross-references
- Loads/load combinations, seismic zones, response reduction factor R → **Part C Sec 1 (Loads and Load Effects)** — cited constantly throughout (materials, stability, diaphragm design, notional loads).
- Concrete mix design, durability, crack width, reinforcement detailing, footings/walls/columns/beams baseline design → **Part C Sec 5 (Structural Concrete)** — the primary "good practice" reference [C-7(2)], cited in nearly every clause.
- Lateral force resisting system steel detailing → **Part C Sec 6A (Steel)**.
- Fire resistance ratings/general fire safety → **Part F (Fire and Life Safety)**.
- Electrical/lightning protection for PPVC modules → **Part D Sec 2 (Electrical and Allied Installations)**.
- Water supply/drainage for PPVC modules → **Part E Sec 1 & 2 (Water Supply / Drainage and Sanitation)**.
- Building materials (blocks, bricks, aggregates) → **Part B (Building Materials)**.
