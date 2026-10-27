---
status: active
project: civil-engineering
type: reference
---
# IS 875 (Part 1):1987 — Dead Loads (Unit Weights of Building Materials and Stored Materials)

Second of the five IS 875 parts, part of Code Design Assistant's IS-code roadmap (after [[IS 456 - Plain and Reinforced Concrete]]). Source: `<your codes folder>\IS CODES\CED37-Structural safety\875_1.pdf` (39 pages). Extracted text: `<local extracted text>\IS 875\IS-875-Part1-Dead-Loads-fulltext.txt`.

**Nature of this document, and how this note treats it:** unlike IS 456, this is overwhelmingly a **reference lookup table**, not a set of design rules — Table 1 alone lists unit weights for ~55 alphabetically-ordered material categories (each with several sub-types), and Appendix A adds another ~8 categories of stored/miscellaneous materials. There's very little "logic" to extract — the value *is* the number, looked up by material name. Transcribing the entire alphabetical list would add bulk without adding clarity (you can already jump to "M" for masonry in the source alphabetically). This note instead captures the materials the maintainer would actually reach for constantly (concrete, brick, soil, water, common finishes), and treats the rest as **look up by material name, page-referenced below.**

## Scope (Cl 1)
Covers unit weights for dead-load calculation: **Table 1** (individual building materials, alphabetical, p.4–28), **Table 2** (assembled building parts/components — ceilings, floors, roofs, walls, p.29–31), **Appendix A** (stored/miscellaneous materials for warehouse-type loading, p.32–37).

## Table 1 — commonly-used values [p.4–28]

| Material | Unit weight | Notes |
|---|---|---|
| Cement concrete, plain (sand/gravel/crushed stone aggregate) | **22.00–23.50 kN/m³** (2 240–2 400 kg/m³) | |
| Cement concrete, prestressed | **23.50 kN/m³** (2 400 kg/m³) | |
| Cement concrete, reinforced (1% steel) | **22.75–24.20 kN/m³** (2 310–2 470 kg/m³) | |
| Cement concrete, reinforced (2% steel) | **23.25–24.80 kN/m³** (2 370–2 530 kg/m³) | |
| Cement concrete, reinforced (5% steel) | **24.80–26.50 kN/m³** (2 530–2 700 kg/m³) | **This is the more precise, steel%-dependent version of what IS 456 Cl 19.2.1 simplifies to a flat 25 kN/m³** — IS 456 explicitly allows the simplified figure "unless more accurate calculations are warranted." Use this table's range when precision matters (e.g. heavily reinforced transfer beams/pile caps with steel % on the high side). |
| Common burnt clay brick | **15.70–18.85 kN/m³** (1 600–1 920 kg/m³) | Engineering brick 21.20; heavy-duty 24.50; sand-lime 20.40. |
| Earth, dry | **15.70 kN/m³** (1 600 kg/m³) | Moist: 18.85 kN/m³ (1 920 kg/m³). |
| Sand, dry clean | **15.10–15.70 kN/m³** (1 540–1 600 kg/m³) | River sand 18.05; wet sand 17.25–19.60. |
| Water, fresh | **9.81 kN/m³** (1 000 kg/m³) | Salt water: 10.05 kN/m³ (1 025 kg/m³). |
| Steel sections (hot-rolled: MB, ISMB beams etc.) | — | **Full standard-section weight-per-metre table, p.17–25 — a large, precisely-defined reference table (mass per running metre for every rolled section designation), reference by page rather than transcribe; risk of a transcription slip on a specific section size is exactly the kind of number worth pulling straight from the source table for a real design.** |
| Timber (various structural species) | — | p.26–28, species-specific — same treatment, pull by page for the actual species in use. |

**Everything else in Table 1** (acoustical materials, aggregates, asbestos products, bitumen, blocks, boards, cast iron, gypsum, lime, linoleum, masonry stone, mastic asphalt, metal sheeting, mortar, pipes, plaster, slagwool, soils/gravels beyond the sample above, terra cotta, terrazzo, tiles, wood-wool slabs) — **look up alphabetically in the source, p.4–28.**

## Table 2 — assembled building parts/components [p.29–31]

More directly useful day-to-day than Table 1 alone, since these are finished-assembly weights rather than raw material densities.

| Component | Weight | Notes |
|---|---|---|
| Ceiling — plaster on tile/concrete, 1.3 cm | **0.25 kN/m²** | Plaster on wood lath, 2.5cm: 0.39; suspended metal lath + cement plaster, 2.5cm: 0.74; + gypsum plaster: 0.49. |
| Floor finish — clay tiles, 12.5–25.4mm ('as laid', excl. screeding) | **0.10–0.2 kN/m²** | Terrazzo paving 'as laid': 0.23 kN/m². |
| Floor, hollow clay blocks (100–200mm, excl. concrete topping) | **1.47–2.55 kN/m²** | Add extra for any concrete topping. Hollow concrete units (100–230mm): 1.67–3.14 kN/m². |
| Wood flooring | **0.11–0.20 kN/m²** | Hardwood 22–28mm: 0.16–0.20; softwood: 0.11–0.13. |
| Roofing — Mangalore tiles with battens | **0.64 kN/m²** | Bedded in mortar over flat tiles: 1.08. Country tiles (single/double): 0.69/1.18. Allahabad tiles (single/double): 0.83/1.67. Thatch with battens: 0.34–0.49. |
| Roof finish — mortar screeding, 10mm | **0.21 kN/m²** | Bitumen macadam: 0.22; lead sheet: 0.07; glass silk quilted: 0.008. |
| Walling — autoclaved reinforced cellular concrete blocks | **4.40–9.80 kN/m³**, by class A (heaviest) to E (lightest) | Brick/concrete-block/stone masonry walls: cross-refer to Table 1's material entries. |

**Roof-load projection note (important, easy to miss):** weights above act **vertically on horizontal projection** — multiply by **cos(roof angle)** to get the load normal to a sloped roof surface.

## Appendix A — stored/miscellaneous materials [p.32–37]

For warehouse/godown/storage-building floor loading. Eight categories: agricultural & food products (grain, rice, wheat, flour, etc.), chemicals & allied materials, fuels, manures, metals & alloys, miscellaneous materials, ores, textiles/paper. **Reference by page** for the specific stored commodity — same "alphabetical lookup" nature as Table 1, not converted to rows here.

## Cross-references

- Feeds directly into IS 456 Cl 19.2.1 (dead load basis) and every structural design calc — this is the starting input, not a design check itself.
- [[IS 456 - Plain and Reinforced Concrete]] — uses the simplified 24/25 kN/m³ concrete figures by default; this table is the fallback for precision.
- IS 875 Parts 2–5 (imposed/wind/snow/special loads) — not yet built, next in the roadmap.
- Parent plan: Code Design Assistant.
