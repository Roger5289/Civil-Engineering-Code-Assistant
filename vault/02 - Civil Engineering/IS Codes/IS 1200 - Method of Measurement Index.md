---
status: active
project: civil-engineering
type: index
---
# IS 1200 — Method of Measurement of Building and Civil Engineering Works

The measurement/billing counterpart to the design codes in [[IS Codes]] — built 2026-09-11 to feed Code Design Assistant's roadmap and, directly, BOQ/billing work. A 28-part series, one part per trade, first published 1958 and split into parts from the 1960s–70s onward; editions here range from 1971 to 1994. Source PDFs: `...\CED44-Methods of measurement of works of civil engineering\1200_1.pdf` through `1200_28.pdf`. Extracted texts: `<local extracted text>\IS 1200\IS-1200-Part{N}-fulltext.txt`.

**Built all 28 parts in full depth** (locked decision 2026-09-11, after confirming with the maintainer — the alternative was a core-trades-only subset or one consolidated note, but he chose full coverage matching the vault's "full notes, not a lean index" precedent). Total source volume ≈260 pages — comparable to one more single code, not 28x anything, since each part is short (5–15 pages).

**Audited 2026-09-11.** Scope was proportional rather than exhaustive: this series is overwhelmingly prose measurement-rules, not dense numeric tables — a structurally different risk profile from NBC/IS 875, where the damage was concentrated entirely in multi-column numeric grids. Consistent with that session-wide pattern (prose content has audited clean every time — IS 13920, SP 16's formulas), the audit targeted the series' two genuinely tabular, multi-column-extraction-risk tables and verified both against page-image renders of the actual source: **[[IS 1200 Part 15 - Painting Polishing Varnishing Etc]]'s Table 1** (19 rows, 6 notes — confirmed 100% correct, no errors) and **[[IS 1200 Part 22 - Materials]]'s Table 1** (~60 rows — found and fixed two real errors: "Paint (Dry)" should read "Paint (Stiff)," and the "mild steel expanded metal" unit, previously flagged as OCR-ambiguous, is confirmed m²). The remaining 26 parts were not re-verified page-by-page; if a specific number from one of them is going to drive a real billing decision, re-check it against the source PDF first rather than trusting the note alone — the same standing rule that applies to every note in this vault.

## What's genuinely shared across the whole series (read once)
Every part opens with near-identical general rules — full text captured once in [[IS 1200 Part 1 - Earthwork]] rather than repeated in every note: clubbing of items, booking-of-dimensions order (length→breadth→height), net-decimal measurement to 0.01 m/m²/m³ unless a part states a finer tolerance, bills-of-quantities requirements, and a "work measured separately" list (water/mud/foul/tides, usually +snow) with the same historical foreword boilerplate about measurement-practice unification (safely skipped — administrative preamble, not technical content).

**Where parts genuinely diverge from that shared baseline — worth knowing before assuming one number applies series-wide:**
- **Opening-deduction thresholds vary by trade**, not one universal number: 0.1 m² (concrete, brick, stone — cross-sections/dissimilar-material ends), 0.3 m² ([[IS 1200 Part 28 - Sound Insulation Work]]), 0.4 m² ([[IS 1200 Part 9 - Roof Covering]], [[IS 1200 Part 10 - Ceiling and Linings]]), 0.5 m² ([[IS 1200 Part 12 - Plastering and Pointing]], [[IS 1200 Part 13 - Whitewashing Colour Washing Distempering and Painting]], [[IS 1200 Part 15 - Painting Polishing Varnishing Etc]]).
- **Dimension precision also varies:** 0.01 m default; 0.005 m for slab thickness ([[IS 1200 Part 2 - Concrete Works]]) and road-layer thickness ([[IS 1200 Part 17 - Road Work Including Airfield Pavements]]); 0.001 m for steelwork ([[IS 1200 Part 8 - Steelwork and Ironwork]]); 2 mm for timber ([[IS 1200 Part 21 - Woodwork and Joinery]]); the >25 m dimension relaxes to 0.1 m in the two mechanized/niche parts (27, 28).
- **"Height >10 m, 5 m stages (or per-storey if a floor exists ≤5 m up)"** recurs identically in Parts 12 and 28 — a genuine shared convention, not coincidence.

## Notes in this series
- [[IS 1200 Part 1 - Earthwork]] — soil/rock classification, excavation methods, lead+lift, planking/strutting, tree removal. **Anchors the series' shared general rules.**
- [[IS 1200 Part 2 - Concrete Works]] — plain/reinforced/prestressed/precast concrete classification and measurement, defers to Parts 5 (formwork) and 8 (reinforcement).
- [[IS 1200 Part 3 - Brickwork]] — general brickwork, circular work, cavity walls, fair cutting, chases/openings.
- [[IS 1200 Part 4 - Stone Masonry]] — closely parallel to Part 3 with stone-specific substitutions (flagged where they differ).
- [[IS 1200 Part 5 - Formwork]] — classification by surface type, the 30°-slope split, secondary-beam/column intersection rules.
- [[IS 1200 Part 6 - Refractory Work]] — furnace/kiln linings; tighter 0.01 m² void-deduction threshold than the rest of the series.
- [[IS 1200 Part 7 - Hardware]] — builders' ironmongery; Table 1 defines what "size" means per article type (33 items).
- [[IS 1200 Part 8 - Steelwork and Ironwork]] — the hub Part every other trade defers reinforcement/structural steel to; rivet-head 2.5% allowance, the 0.02/0.05/0.1 m² deduction bands.
- [[IS 1200 Part 9 - Roof Covering]] — metal/AC/tile/thatch/terrace roofing, rainwater goods.
- [[IS 1200 Part 10 - Ceiling and Linings]] — short, largely standard; supports deferred elsewhere.
- [[IS 1200 Part 11 - Paving Floor Finishes Dado and Skirting]] — in-situ/tile/sheet finishes, bedding+backing; shares Part 12's deduction-band structure.
- [[IS 1200 Part 12 - Plastering and Pointing]] — carries the 0.5 m²/3 m² deduction-band logic reused almost verbatim by Part 13.
- [[IS 1200 Part 13 - Whitewashing Colour Washing Distempering and Painting]] — building-surface finishes specifically; corrugation/JALLI area multipliers.
- [[IS 1200 Part 14 - Glazing]] — pane measurement; **2002 amendment changed curved-cutting from billable-extra to deemed-included** — edition-sensitive, flagged.
- [[IS 1200 Part 15 - Painting Polishing Varnishing Etc]] — general paint/polish/varnish (distinct from Part 13); **Table 1's equivalent-plain-area multipliers** is the core reference content (19 joinery/steelwork/gate types).
- [[IS 1200 Part 16 - Laying of Water and Sewer Lines]] — trunk mains/sewers; manhole depth-band classification convention (shared with Part 19).
- [[IS 1200 Part 17 - Road Work Including Airfield Pavements]] — IRC-aligned; the 5 m/2.5 m level-grid method for finished-thickness computation.
- [[IS 1200 Part 18 - Demolition and Dismantling]] — defines "demolition" vs "dismantling"; 100 m/500 m lead bands, category-by-category measurement.
- [[IS 1200 Part 19 - Water Supply Plumbing and Drains]] — in-building counterpart to Part 16; long enumerated-fixture list.
- [[IS 1200 Part 20 - Laying of Gas and Oil Pipe Lines]] — near-identical to Part 16 except for heat-treatment/testing/pigging/insulation clauses specific to gas/oil.
- [[IS 1200 Part 21 - Woodwork and Joinery]] — the most detailed Part in the series; full staircase sub-clause structure (Cl 4.7).
- [[IS 1200 Part 22 - Materials]] — supply-measurement lookup table for ~60 material types; one OCR-ambiguous cell flagged (mild steel expanded metal, m² vs m³).
- [[IS 1200 Part 23 - Piling]] — precast/timber/steel-sheet/cast-in-situ/bored/RCC-sheet piles, each with its own measurement formula.
- [[IS 1200 Part 24 - Well Foundations]] — caisson/well-sinking; kentledge, steining, pneumatic sinking.
- [[IS 1200 Part 25 - Tunneling]] — the "B line"/pay-line excavation convention; supports and lining measured against it.
- [[IS 1200 Part 26 - Acid Resistant Lining]] — niche, all finished-surface measurement, "simplest possible" by design.
- [[IS 1200 Part 27 - Earthwork Done by Mechanical Appliances]] — the machine counterpart to Part 1; several explicit divergences (lift not measured at all, 50%-void rock/soil split, different lead banding).
- [[IS 1200 Part 28 - Sound Insulation Work]] — niche, same "simplest possible" philosophy as Part 26; 0.3 m² deduction threshold (series outlier).

## The Part 8 / Part 2 / Part 5 hub pattern
Reinforcement and structural steel (Part 8), plain/reinforced concrete (Part 2), and formwork (Part 5) are the three Parts almost every other trade Part defers to rather than re-specifying. When a BOQ item crosses trades (e.g. a reinforced concrete beam with formwork), expect to pull line items from up to three Parts for one physical element — this is how the series is designed to compose, not a redundancy.

## Cross-references
- [[IS Codes]] — the design-code series this measurement series complements.
- Code Design Assistant — parent plan and roadmap.
