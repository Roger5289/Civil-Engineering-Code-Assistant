---
status: active
project: civil-engineering
type: reference
---
# Part E, Section 1 — Water Supply

Covers water demand estimation, storage/tank design, distribution system design, hot water supply, backflow prevention, swimming pools, and water supply for high-altitude/sub-zero regions. Renamed in this edition from "NBC" to "National Building Construction Standards (NBCS)."

## 1 Scope (p. 2511)
Covers water supply for residential, business and other buildings including traffic terminal stations; plumbing connected to public supply; distribution system design; expansion in piping; swimming pools. **Excludes** industrial process water and firefighting/street-cleaning water (those are covered in Part F).

## 3 General principles (p. 2517–2519)
- Minimum residual head at consumer's tap: **0.018 N/mm² (0.18 bar)**, higher for flush valves (up to 0.1 N/mm² / 1.0 bar) (p. 2517).
- Minimum fixtures per dwelling: 1 WC, 1 lavatory, 1 kitchen sink, 1 bathing place (p. 2518).
- Accessibility: doors, fixtures, grab bars etc. for persons with disabilities per cross-reference to good practice [E-1(3)] (p. 2518).

## 4.1 Water demand estimation (p. 2520–2524)
**Population/occupancy basis** (p. 2520–2521): offices 1 person/10 m²; schools = strength + staff; hostels = beds + staff; hotels = beds + staff + restaurant seating; hospitals = beds + staff + attendants (density 5/bed secondary care, 7/bed tertiary, 9/bed quaternary); mercantile 1 person/3 m² (street floor) or /6 m² (upper floors); assembly (per Part F Fire and Life Safety) 1 person/0.65 m² (concentrated, no fixed seating) to 1 person/1.8 m² (dining); warehouse 1/20 m²; industrial/hazardous 1/10 m²; storage 1/30 m².
Dwelling unit population: 1BR=3, 2BR=4, 3BR=5, 4BR+=6; EWS=4; studio=2 (p. 2520).

**Residential per-capita demand** (p. 2521): urban 135 LPCD; urban with water-efficient fixtures 100 LPCD; rural 70 LPCD (incl. 15 LPCD flushing). Breakdown for 135 LPCD: drinking 5, bathing 35, cooking 10, washing utensils 20, floor cleaning 10, washing clothes 25 (total 105 domestic + 30 flushing) — see Table breakdown p. 2521–2522.

**Table 1 — Water requirements for buildings other than residences** (Clause 4.1.2/4.1.3, p. 2522–2523): domestic + flushing litres/day by occupancy, e.g. factories with bathrooms 30+15=45/head; hospital ≤100 beds 230+110=340/bed, >100 beds 300+150=450/bed; hostels 90+45=135/head; hotel ≤3★ 120+60=180/head, 4★+ 260+60=320/head, with bathtub 320+60=380/head; offices 25+20=45/head; schools without boarding 25+20=45/head, with boarding 90+45=135/head; shopping mall staff 25+20=45/head, visitors 5+10=15/head; airports 40+30=70/head; also OPD 10+5=15/bed, hospital secondary care 800/bed, super-speciality 950/bed. **All the above rows verified against the PDF 2026-09-05.** The full table has ~25 building types (transport terminals, sports, restaurants, clubs, etc.) — pull any not listed here straight from PDF p.2523–2525.

**Landscaping**: 6–8 litre/m²/day for lawns (p. 2524).

## 4.2–4.3 Water quality, sources, demand load (p. 2524–2526)
Waste water reclamation for flushing/landscaping/HVAC cooling towers permitted with dual piping to avoid cross-connection (p. 2525). Future demand projection methods: demographic, arithmetic/geometric progression, incremental increase, logistic, graphical (p. 2525–2526).

## 4.4 Storage of water (p. 2526–2529)
- Storage tanks: RCC, brick masonry, ferrocement, steel, plastic, GRP (p. 2526).
- Overhead tank (OHT) clearance above highest fixture: minimum **2 m** (p. 2528).
- **Storage capacity rule (Clause 4.4.10, p. 2527–2528) — verified against PDF 2026-09-05:**
  - Main OHT only (plotted development): half a day's demand.
  - Other buildings (apartments/hotels/hospitals/commercial): UGT = 1.5 days, OHT = 0.5 day (combined 1.5 days when raw/treated stored separately in UGTs).
  - Hydro-pneumatic system from UGT: UGT storage = 2 days' demand.
  - OHT-only fallback: 33–50% of one day's requirement.
  - Combined UGT+OHT gravity system: UGT 150%, OHT 50% of one day's requirement.
  - Fire-fighting storage is **additional** — see Part F.
- Tanks >5000 L: must have vent pipes (p. 2527).

## 4.6–4.7 Materials, distribution design (p. 2529–2534)
Pipe materials: CI, steel, ductile iron, RCC/PSC, GI, copper, brass, wrought iron, stainless steel, PE, HDPE, uPVC, CPVC, PPR, composite (PE-AL-PE), PEX, polybutylene (p. 2530).
Peak factor for intermittent flow design: **2 to 3** (p. 2530).

**Table 2 — Water Supply Fixture Units (WSFU)** (Clause 4.7.3.1, p. 2531): bath tub 4 (private)/– (public); WC flush valve 5(private)/5–8(public), min pipe 25/32mm; WC flush tank 2/3–5, min pipe 15mm; shower 2/3, 15mm; bathroom group flush valve 8/10, 25/32mm; bathroom group flush tank 5/6, 20mm; urinal flush valve 3/5–6, 20mm. **Verify against PDF p. 2531 for exact figures if sizing pipes — full table has 22 fixture types.**

**Table 3 — Probable simultaneous demand** (Clause 4.7.3.2, p. 2532–2533): converts fixture units to L/min demand via Hunter's method, e.g. 100 FU → 166.5 L/min (flush tank) / 257.4 L/min (flush valve); 1000 FU → 787.3/787.3 L/min (curves converge above ~1000 FU). **Verify against PDF p. 2532–2533 before use — long numeric table.**

**Max flow rates/flush volumes** (Clause 4.7.3.3, p. 2533): WC baseline 6 L/flush (efficient: 6.0/4.8/4.0 full, 3.0/2.8/2.0 reduced); urinal 3.8 L baseline; shower head 10 L/min baseline.

Max distribution pressure: **0.42 N/mm²**; above this, pressure-reducing valves required (Clause 4.7.5, p. 2534). Max velocity: 2.4 m/s (general), 1.5 m/s (hot water in copper pipes) (Clause 4.8.6, p. 2537).

## 4.8 Multi-storey distribution systems (p. 2535–2538)
Four methods: direct mains supply, gravity (OHT), pressurized/hydro-pneumatic, combined. Zoning: recommended for every **7–9 floors** (Clause 4.8.6, p. 2537). See Fig. 3 (hydro-pneumatic schematic, p. 2536), Fig. 4 (OHT distribution, p. 2537), Fig. 5 (gravity zoning schematic, p. 2538), Fig. 6 (hydro-pneumatic zoning schematic, p. 2539) — figures reference staircase/lift-well tank placement directly.

## 4.9–4.13 Pipe work, mains, jointing, laying (p. 2540–2545)
Main cover depth: **900 mm under roadways, 750 mm under footpaths** (Clause 4.9.1, p. 2540). Service pipe entry depth: **≥750 mm** below outside ground level (Clause 4.13.5.3, p. 2545). Water/sewer pipes in same trench: water pipe ≥300 mm above sewer crown if unavoidable (Clause 4.13.5.2, p. 2544).

## 4.11 Backflow prevention (p. 2542–2543)
Devices: barometric loop, air gap, atmospheric/pressure vacuum breaker, double check valve, reduced-pressure backflow device. Air gap for less-satisfactory water into cistern: **≥2× nominal bore, minimum 150 mm** (Clause 4.12.3, p. 2543).

## 4.14 Hot water supply (p. 2545–2551)
Design temperatures (Clause 4.14.2.1, p. 2545–2546): scalding 65°C, sink 60°C, hot bath 43°C (run) / 41°C (use), warm bath 37°C, tepid bath 29.5°C. Recommended storage temp: 60°C (up to 65°C with soft water).
Storage capacity: 50–75 L @ 60°C for bathtub dwelling, 25 L for shower/tap (Clause 4.14.3, p. 2546); capacity ≥120% of max short-time demand.
**Table 4 — Rate of hot water flow** (p. 2546): kitchen sink 5 L/min, wash basin 5 L/min, shower (spray) 6.5 L/min.
**Table 5 — Max permissible hot water draw-off pipe lengths** (Clause 4.14.12.2.3, p. 2550): ≤20mm dia → 12 m; 20–25mm → 7.5 m; >25mm → 3.0 m.
GI/galvanized steel suitability by water pH vs. temporary hardness table (Clause 4.14.6.2, p. 2547–2548): e.g. pH 7.3 needs ≥210 mg/L hardness, pH 7.9–8.5 needs ≥70 mg/L. Below pH 7.2, GI must not be used at all.
Cold-feed tank sizing for water heaters: ≥2× heater capacity (1.5× if >10 heaters share a tank) (Clause 4.14.10.2.1, p. 2548).
Max hot water temp at fixture (scald prevention): **40°C recommended** at thermostatic mixers for public use (Clause 4.14.12.2.4, p. 2550).

## 4.15–4.18 Testing, disinfection, maintenance (p. 2551–2555)
Hydrostatic test pressure: **0.5 N/mm² or 2× working pressure**, whichever greater, held ≥5 min (mains, Clause 4.15.2, p. 2551) / ≥30 min (hot water system, Clause 4.15.4.1, p. 2552).
Disinfection dose: 50 ppm chlorine, held ≥3 hours (Clause 4.16.2, p. 2552).
Storage tank/cistern cleaning: at least once per year (Clause 4.16.1, p. 2552).

## 4.17 High-altitude/sub-zero regions (p. 2553–2554)
Frost line in northern India: **0.9–1.2 m below ground**. Pipes must be laid below this depth or insulated. See Fig. 7 (insulation at service connection, p. 2554).

## 4.19 Swimming pools (p. 2554–2560)
Three types: fill-and-draw, flow-through (both discouraged for water conservation), recirculating (recommended) (p. 2555).
**Turnover rates** (p. 2556): private outdoor pool 6h, private indoor 10h, public 6h, competition 6h, wading pool 1h, public spa 0.5h, private spa 1h.
**User load / surface area** (Clause 4.19.1.3, p. 2556): depth ≤1m → 2.2 m²/user; ≤1.5m → 2.7 m²/user; >1.5m → 4.0 m²/user.
**Recommended dimensions** (Clause 4.19.1.4, p. 2556): half-Olympic 25×12-13×1.8m; full Olympic 50×25×2m; diving depth 3.5m (1m board) / 5m (10m platform).
Floor slope limits (Clause 4.19.2.4, p. 2557): shallow area ≤300mm vertical in 3.6m horizontal; deep area (>1.5m) not steeper than 300mm in 1m.
Pool deck width: ≥1.2m surrounding, ≥2.5m between adjacent pools, ≥2m overhead clearance (Clause 4.19.2.8, p. 2557–2558). Accessible transfer wall: 1.5×1.5m clear deck, height 400–480mm, width 300–400mm (p. 2558).
Water treatment (p. 2559–2560): chlorine residual 1.0–4.0 ppm (≥2.0 ppm above 30°C); bromine 2.0–8.0 ppm (≥4.0 ppm above 30°C); filtration rates: low 10 m³/m²/h, medium 11–30, high 31–50, backwash min 30 m³/m²/h.
Outlet/drain spacing: minimum 2 drains at deepest point, centre-to-centre ≤2.0m, ≤3.0m from walls, max grate opening 8mm, outlet velocity ≤0.3 m/s (Clause 4.19.4.4, p. 2559).

## 4.21 Colour codes for pipes (p. 2561–2562)
Table lists ground/band colours for cooling water, boiler feed, condensate, drinking water (sea green/French blue/signal red), fire water (fire red/crimson), etc. **Verify against PDF p. 2561–2562 if specifying — 23-row table.**

## Annexes (p. 2563–2566)
Annex A — water supply application form (Clause 3.2.1). Annex B — plumber's completion certificate (Clause 3.2.3). Annex C — Hazen-Williams nomogram with worked examples for pipe sizing (Clause 4.7.4).

## List of Standards (p. 2567–2568)
24 referenced IS standards, e.g. IS 10500:2012 (drinking water spec), IS 2065:1983 (water supply in buildings code of practice), IS 3328:2026 (swimming pool water quality), IS 16508:2017 (public swimming pool safety).

## Cross-references
- Firefighting water storage, wet risers, fire pump capacity → **Part F, Fire and Life Safety** (Clauses 4.1.4.1–4.1.4.3, p. 2524; also 4.4.10 note, p. 2529).
- Accessibility (disabled/elderly fixtures) → cross-references good practice standards tied to **Part 3 Development Control Rules** per the section's foreword history note (p. 2508) — note: this NBCS edition doesn't itself contain a "Part 3 DCR" (per Part A, DCRs are explicitly out of scope of this document) — this looks like a residual/uncorrected reference to the old NBC 2016 structure, worth flagging if precision matters.
- Water-efficient fixtures → external standard IS 17650 (accepted standard [E-1(5)]).
- Materials for pipes/fittings → **Part B, Building Materials** (Clause 4.6.1, p. 2529; also Clause 4.17.4.1, p. 2553).
- Occupancy/assembly population caps → **Part F, Fire and Life Safety** (p. 2521).
