---
status: active
project: civil-engineering
type: reference
---
# Part D, Section 6 — Information and Communication Enabled Installations

Covers ICT/telecom infrastructure requirements in buildings: telecom spaces (ER/TR/EF/TE), cabling media and pathways, bonding/earthing, installation safety, and in-building mobile coverage (DAS/IBS). PDF pages 2461–2504 (pages 2505–2506 at the tail of this slice already belong to Part E Sec 1's title/contents — not part of this Section).

## 1 Scope (p. 2465)
1.1–1.2: Covers essential requirements for ICT-enabled installations, technology systems, cabling, and passive/active equipment in buildings; basic design/integration requirements for telecom spaces and cabling infrastructure. Applies to residential and other buildings; indicative (not mandatory) for data centres/telecom exchange buildings. New in this revision: street furniture (Annex B) and building/digital-connectivity info template (Annex C).

## 2 Terminology (p. 2465–2468)
Defines: Access Point, Antenna, Attenuation, Backbone/Backbone Cabling, Building Management System (BMS), Bus Bar, Coaxial Cable, Consolidation Point (CP), Cross-Connect, Distributed Antenna System (DAS), DTH, Horizontal Cabling, Cross-Connect types (HC/IC/MC), IoT, LAN/MAN/WAN, In-Building Solution (IBS), Inside/Outside Plant (ISP/OSP), M2M, MUTOA, Optical/Main Distribution Frame (ODF/MDF), Smart City/Building/Home, Telecommunication Spaces (ER/TR/EF/TE), Telecom Service Provider (TSP), VSAT, Workstation/Workspace.

## 3 General Requirements for Telecommunication Spaces and Connecting Hardware (p. 2468–2487)

### 3.1 Telecommunication Spaces (p. 2468–2472)
- **3.1.1 General considerations** (p. 2468–2469): accessibility, acoustic noise separation, administration/documentation, cable separation from EMI/RFI, ceiling height min **2.4 m** (3 m preferred), dust/static control, electrical power redundancy + UPS, flood avoidance, lighting (dedicated switch, emergency circuit), location (centrally located, vertically aligned in multi-floor buildings), environmental control (temperature/humidity per OEM, min 1 air change/hour), fire protection (see Part F cross-ref), bonding/grounding.
- **3.1.2 Equipment Room (ER)** (p. 2470–2471): sizing — usable floor space = total floor area − 20% if unknown; **9.3 m² per work area** for calculating work areas; **minimum ER size 14 m²**; general provisioning **0.07 m² of ER per 10 m² of usable floor space** (special buildings like hospitals/hotels may vary).
- **3.1.3 Telecommunications Room (TR)** (p. 2471–2472): additional TR needed if horizontal cable run exceeds **90 m** (subject to fibre-type exceptions) or usable floor space served exceeds **930 m²**. TR size table:

  | Area Served | Dimension of TR |
  |---|---|
  | ≤465 m² | 3 m × 2.4 m |
  | >465 m² and ≤930 m² | 3 m × 3.4 m |

  Smaller-building guidance:

  | Building Smaller Than | Served As |
  |---|---|
  | 465 m² | Shallow/walk-in rooms (walk-in ≥1.3 m × 1.3 m; shallow ≥0.6 m deep × 2.6 m wide) |
  | 93 m² | Wall cabinets / self-contained / enclosed cabinets |

  **verify against PDF p.2471–2472 — NOT cross-checked** (background table-extraction pass had not reached this page range yet; the plain-text extraction of these two tables reads cleanly and consistently, but confirm against the PDF before using in a real design submission).

- **3.1.4 Entrance Facilities (EF)** (p. 2472): TSP space ≥ **1.2 m × 1.83 m** per service provider; separate 230 V/16A circuits every 2.4 m along EF/ER wall, outlets ~300 mm above finished floor.
- **3.1.5 Telecommunication Enclosures (TE)** (p. 2472): minimum one TE per floor if no TR present; earthed if metallic.

### 3.2 Telecom Media and Connecting Hardware (p. 2472–2477)
- 3.2.4.1 Copper twisted-pair — **Table 1 Balanced Twisted-Pair Cabling Channel Performance** (Clause 3.2.4.1, p. 2473):

  | ISO Category/Class | TIA Category | Frequency (MHz) | Max Data Rate |
  |---|---|---|---|
  | Cat 3/Class C | Cat 3 | 16 | 10 Mbps |
  | Cat 5/Class D | Cat 5e | 100 | 1 Gbps |
  | Cat 6/Class E | Cat 6 | 250 | 1 Gbps |
  | Cat 6A/Class EA | Cat 6A | 500 | 10 Gbps |
  | Cat 7/Class F | NA | 600 | 10 Gbps |
  | Cat 7A/Class FA | NA | 1000 | 10 Gbps |
  | Cat 8/Class G | Cat 8 | 1500–2000 | 25/40 Gbps (max distance 30 m) |

  **verify against PDF p.2473 — NOT cross-checked**.

- 3.2.4.2 Optical fibre (p. 2474–2475): single-mode core 8–11 μm / multi-mode 50 or 62.5 μm, cladding ~125 μm. Fibre colour code (12-fibre repeating: Blue, Orange, Green, Brown, Grey, White, Red, Black, Yellow, Purple, Rose, Aqua) (p. 2474). Backbone length/data-rate chart (p. 2475): OM1 2000 m@155 Mb/s; OM2 550 m (campus)/300 m (building)@1 Gb/s; OM3 300 m@10 Gb/s or 100 m@100 Gb/s; OM4 550 m@10 Gb/s or 150 m@100 Gb/s; OS (single-mode) 10 000 m@100 Gb/s. **verify against PDF p.2475 — NOT cross-checked**.
- 3.2.4.3 Coaxial cable (p. 2475–2476): Series-6, Series-11, RG-59, 75 Ω impedance; DAS/IBS cables/components should cover 400–4000 MHz.
- 3.2.5 Wireless systems (p. 2476): WLAN AP (IEEE 802.11ax/be or higher), DAS/IBS, wireless repeaters.
- 3.2.6 Connecting hardware — details in Annex A.
- 3.3 Backbone cabling/pathways (p. 2477–2483): star vs hierarchical-star topology (Fig 1–3); inter-building pathways (underground/direct-buried/aerial/tunnel) — underground conduit min **100 mm** diameter, max two 90° bends, manhole spare-loop 2–4 m; backbone building pathways — vertical conduit bend radius ≥10× conduit diameter (typ. 1 m), pull box min 600×600×150 mm, min three **100 mm** conduits between adjacent-floor TR/TE, roof access min two 75 mm + one 20 mm conduit.
- 3.3.4 Ethernet in the First Mile (p. 2482–2483): Cat 5e/Cat 6 common; Cat 7/8 support 10/40 Gbps.
- 3.4 Horizontal cabling (p. 2483–2487): UTP/ScTP 4-pair 100 Ω, distance limit **90 m** (incl. 10 m patch/work-area allowance); star topology preferred; MUTOA typically serves **12 work spaces**, copper run (horizontal+work area+cords) ≤ **100 m** total; CP located ≥15 m from HC(FD).
- 3.5 Building info template — see Annex C.

## 4 Specific Requirements for Telecom Infrastructure Cabling (p. 2487–2491)

### 4.1 Bonding and Grounding (p. 2487–2489)
PBB (primary bonding busbar) min **6.35 mm thick × 101.6 mm wide**; SBB (secondary) min **6.35 mm thick × 50 mm wide**. TBB conductor sizing by max PBB–SBB length:

| Max PBB–SBB length (m) | TBB cross-section (mm²) |
|---|---|
| <4 | 16 |
| 4–6 | 25 |
| 6–8 | 35 |
| 8–10 | 35 |
| 10–13 | 50 |
| 13–16 | 60 |
| 16–20 | 70 |
| 20–26 | 95 |
| 26–32 | 120 |
| 32–38 | 150 |
| 38–46 | 150 |
| 46–53 | 185 |
| 53–76 | 150 |
| 76–91 | 300 |

(beyond this, calculate at 3.3 mm² per metre). **Verified against PDF 2026-09-05 — transcription is faithful.** The non-monotonic step (46–53 m → 185 mm², then 53–76 m → **150 mm²**, then 76–91 m → 300 mm²) is a **typo in the NBC 2026 source itself**, not an extraction error. By the trend, the 53–76 m value should be ≥ 185 (likely ~240); use engineering judgement / the 3.3 mm²·m⁻¹ rule and don't take the printed 150 at face value for a 53–76 m run.

4.1.1 Meshed bonded networks (p. 2488–2489): preferred for high-density ICT sites (data centres, hospitals, airports); Fig 7 (earthing/bonding arrangement) and Fig 8 (mesh-BN) at p. 2489.

### 4.2 Installation and Workplace Safety (p. 2490–2491)
Cabling installation guidelines: no exceeding max tensile load, min bend radius, cable slack for 2× re-termination, EMC (cross mains cables at right angles), proper routing/labelling. Workplace safety: PPE, adequate lighting at splice points, eye/respiratory protection for fibre splicing (glass fragment hazard, chemical adhesives).

## 5 Other Applications in Telecom Infrastructure Cabling (p. 2490–2492)
- 5.1 Electronic Access Control (EAC) — locks/card readers/biometrics, 4-pair shielded cable typical.
- 5.2 Video surveillance — visible/IR/thermal/film cameras, fixed vs pan-tilt mounts.

## Annex A — Additional Guidelines (p. 2492–2495)
Connector types: IDC, modular plug/jack (copper); LC/SC/ST/splices (fibre); BNC/F/N-style (coaxial). Cable fire-safety marking classes (p. 2493–2494): Twisted-pair — CMP (plenum), CMR (riser), CMG/CM (general), CMX (limited use), CMUC (under-carpet). Optical fibre — OFNP/OFCP (plenum), OFNR/OFCR (riser), OFNG/OFCG (general, non/conductive), OFN/OFC (general). Balanced cable nomenclature — Table 2 (p. 2495): screen-type combinations (U/U, U/F, F/U, F/F, S/U, S/F, SF/U, SF/F) mapping to North American designations (TP, ScTP, S TP, SS TP etc). **verify against PDF p.2495 — NOT cross-checked**.

## Annex B — Street Furniture for ICT Installations (p. 2500)
New in this revision. Street furniture (streetlights, utility poles, bus stops, traffic signals) as small-cell/air-fibre hosts under PM Gati Shakti National Master Plan (26.5 million units digitally mapped). Telecommunications (Right of Way) Rules 2024 define small cells as having coverage range up to **2 km**. B-1.1 structural/positional aspects (load-bearing, aesthetics, clearances, stability); B-1.2 administrative aspects (RoW, GIS-mapped inventory, municipal permissions).

## Annex C — Building Information & Digital Connectivity Requirements Template (p. 2501–2503)
Clause 3.5. Blank data-collection template: C-1 general building info (incl. occupancy classification list: Group A Residential, B Educational, C Institutional, D Assembly, E Business, F Mercantile, G Industrial, H Storage, I Hazardous, J Mixed-use — note this classification is specific to this Annex only, not the NBCS's general occupancy classification elsewhere); C-2 occupant/user details; C-3 digital connectivity requirements; C-4 infrastructure support (existing buildings).

## List of Standards (p. 2504)
IS 9537 Parts 2/3/5 (rigid steel / rigid plain / pliable conduits for electrical installations), IS 3419:1988 (fittings for rigid non-metallic conduits).

## Cross-references
- Fire-stopping of sleeves/slots and fire detection/suppression in telecom spaces → **Part F, Fire and Life Safety** (p. 2469, p. 2470).
- IEC/ISO/ITU/TEC/TRAI/DOT external standards referenced throughout (ISO/IEC 11801:2002, ISO/IEC 30129:2015) — not other NBCS Parts.
- No explicit cross-reference found to Part C (Structural) despite street-furniture load-bearing content (Annex B) — a practicing engineer combining ICT infrastructure with structural design of poles/masts would need to separately consult Part C Sec 1 (Loads) and the relevant structural section for the pole/mast material.
