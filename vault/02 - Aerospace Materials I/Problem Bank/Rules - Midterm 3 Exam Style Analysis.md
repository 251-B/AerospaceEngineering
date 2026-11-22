---
materia: Aerospace Materials I
tema: "Assessment Test III (Units 8 to 11): structure, question style and bank plan"
tipo: rules
estado: active
fuentes:
  - "sources/cuatrimestre-1/02-aerospace-materials-1/examenes/MATERIALS_THIRDPARTIAL_2020.pdf"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/examenes/MATERIALS_THIRDPARTIAL_2020_V2.pdf"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/schedule/Schedule_MAT AERO I 2026 - 27.pdf"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/examenes/MATERIALS_FINALEXAM_COMPILATION_2013-2017.pdf"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/examenes/MATERIALS_FINALEXAM_2012_ORD.pdf"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/examenes/MATERIALS_FINALEXAM_2012_EXTRA.pdf"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/examenes/MATERIALS_FINALEXAM_2016_ORD_SOL.pdf"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/examenes/MATERIALS_FINALEXAM_2016_EXTRA_SOL.pdf"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/examenes/MATERIALS_FINALEXAM_2017_ORD.pdf"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/examenes/MATERIALS_FINALEXAM_2017_EXTRA.pdf"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/unit-08-ceramic-materials/problemas/Problems T8_CeramicMaterials.pdf"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/unit-09-polymers/problemas/Problems T9_Polymers.pdf"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/unit-10-composite-materials/problemas/Problems T10_CompositeMaterials.pdf"
tags:
  - problem-bank
  - midterm-3
  - exam-analysis
  - rules
---

# Midterm 3 (Assessment Test III): exam style analysis and bank plan

This note is the specification of the Midterm 3 bank: what the real paper looks like, how its test questions are written, which mistakes its wrong options exploit, and how many questions and problems the bank holds per unit and per concept. The bank notes (`Quiz - Bank Bnn - ...`, `Problem - Bank Pnn - ...`) follow it, `tools/build_materials_bank.py` enforces the structural rules, and `tools/materials_bank/verify_mt3.py` recomputes every numerical check and problem verification line.

## 1. Structure of Assessment Test III

| Item | Value | Source |
| :--- | :--- | :--- |
| Name and date | "Assessment Test III", Model B, 16 December 2020, course 2020/21, "Grade: Points/10" | `MATERIALS_THIRDPARTIAL_2020.pdf`, p. 1; `V2`, p. 2 |
| Second 2020 paper (Paper B) | Same sitting ("1. (5 points) Mark with an X the right answer, there is only one correct answer per question"), graded student scan with red ticks and blue X marks | `MATERIALS_THIRDPARTIAL_2020_V2.pdf`, pp. 4–5 |
| Part I | "Part I (5 points)": 10 test questions, four options per question (`a` to `d` in Model B; four rows in Paper B), "There is only one correct answer per question" | `2020`, pp. 1–2; `V2`, pp. 2–5 |
| Scoring of Part I | "+ 0.5 points" per right answer, "-0.15 points" per wrong answer, "0" for blank answers, and "The resulting mark will not be smaller than 0 in any case" (floor 0) | `2020`, p. 1 header; `V2`, pp. 2, 4 headers |
| Answer sheet | "Mark the right answer with a X in the table below" (Model B); mark with an X beside each row (Paper B) | `2020`, p. 1; `V2`, p. 4 |
| Material allowed | "Neither books nor any other extra material is allowed in the exam but the calculator." | `2020`, p. 1 header |
| Part II | One problem, "Part II (5 points)", on Composite Materials, four subquestions: 55 vol% unidirectional graphite-HM/epoxy plus 50 % Kevlar-49 hybrid replacement (a) 1.5 p, (b) 1.5 p, (c) 1.0 p, (d) 1.0 p | `2020`, p. 3; `V2`, p. 6 (plus an extra 4 × 1.25 p carbon/polyester problem on `V2`, p. 8) |
| Figures | None in the 10 core Units 8–10 MCQs of 2020; four magnetic-dipole images in pasted Unit 7 items; property table printed in Part II | `2020`, pp. 1–3; `V2`, pp. 2–6 |
| Duration | Not printed on either 2020 paper; `Schedule_MAT AERO I 2026 - 27.pdf` (p. 2, Session 26, 11 Dec) allocates one session to `TEST 3`. The simulator sets **60 minutes** as an assumption (with 50 / 60 / 75 min options) | `Schedule_MAT AERO I 2026 - 27.pdf`, p. 2; `exam-blueprint-midterm-3.json` |
| 2026–27 scope | Topics 8, 9, 10, and 11 (**Adhesives added**, whereas 2020 Test 3 covered Units 8–10 plus two Unit 7 questions). Default blueprint mix: `U8 = 3, U9 = 3, U10 = 2, U11 = 2` (10 MCQs, 5.0 pts) + 1 Composites Part II problem (5.0 pts) | `Schedule_MAT AERO I 2026 - 27.pdf`, p. 2; `exam-blueprint-midterm-3.json` |

### 1.1 Wuolah student scan discrepancies verified against slides

Handwritten student marks on `MATERIALS_THIRDPARTIAL_2020_V2.pdf` are never treated as an authoritative key without checking the official lecture slides (`Session 16`–`Session 24`):

- **Model B Q10 (`Typical applications for composites in civil aircrafts are:`, `2020` p. 2 / `V2` p. 3):** The student circled `b) Bulkheads and stringers` in blue pen, which is **wrong**. `Session 23` Slides 47–53 explicitly identify **`c) Engine cowlings, elevators and spoilers`** as the typical civil aircraft applications introduced from the early 1980s onward (B757, B767, B737-300, A310, A320, B777, A340-600). Turbine blades (`a`) and landing gear (`d`) are explicitly excluded (`Session 23` Slide 48: *"Engine, Landing gear not included"*), while bulkheads and stringers (`b`) appear only selectively in later platforms (such as A340-600/A380 rear pressure bulkheads and A350 fuselage stringers) whereas overall civil airframes remain mostly metallic (61–75 % Al).
- **Paper B Q2 (`Crystallinity of a polymer is higher...`, `V2` p. 4):** Confirmed as **`due to an increase in its molecular weight`** (Option 3), verified both by the red grading tick on the graded scan and by strict falsification of Options 1, 2, and 4 against `Session 19` Slides 26–27: atactic PP is amorphous whereas isotactic is crystalline (falsifies Option 1); random copolymers are amorphous whereas block copolymers have some crystallinity (falsifies Option 2); complex monomeric structures lower crystallinity (falsifies Option 4). Note the exact slide nuance: `Session 19` Slides 26–27 (*Factors affecting crystallinity*) do not list molecular weight explicitly, whereas `Session 19` Slide 30 plots low MW ($10^2\text{–}10^3$) as a mobile/viscous liquid versus higher MW ($\ge 10^4$) as a partially crystalline plastic, `Session 20` Slide 16 links high MW with linear chains and high crystallinity in fibres, and `Session 19` Slide 43 pairs higher $M$ and higher crystallinity with higher $\sigma$ and $E$.
- **Paper B Q9 (`When stress is applied perpendicular to fibers in a continuous fibers reinforced composite:`, `V2` p. 5):** No red grading tick appears on the scan and the student drew swap arrows before marking Option 2 (`Matrix is subjected to higher deformation`) with a blue `X`. Verified as **`Matrix is subjected to higher deformation`** against `Session 22` Slides 23–24: under transverse isostress loading, $\sigma_{2C} = \sigma_f = \sigma_m$ (which eliminates Options 3 and 4 claiming unequal stress), so $\varepsilon_f = \sigma_2 / E'_f$ and $\varepsilon_m = \sigma_2 / E_m$. Because $E'_f \gg E_m$, the matrix carries the larger strain ($\varepsilon_m > \varepsilon_f$).
- **Other scan notes:** In Paper B Q6 (`V2` pp. 4–5), a stray pencil circle sits on `8` while the blue `X` and red grading tick sit on **`6`**, confirmed by `Session 16` Slides 8 and 14 (`CaO` has the rock salt structure with $\text{C.I.} = 6$ for both ions). Pages 3 and 5 of `V2` also carry four Unit 7 questions (Q9 paramagnetism, Q10 thermal expansion, Q11 ferrimagnetism, Q12 thermal expansion coefficient); in the 2026–27 syllabus Unit 7 belongs to Test 2 (`Schedule_MAT AERO I 2026 - 27.pdf`, p. 1), so those four questions stay in the Midterm 2 bank.

### 1.2 Simulator practice modes (`exam-blueprint-midterm-3.json`)

The exam simulator offers four modes aligned with both the 2026–27 syllabus and the 2020 paper:

1. **`full` (default):** 10 MCQs distributed **`U8 = 3, U9 = 3, U10 = 2, U11 = 2`** (5.0 pts, +0.5/-0.15/0, floor 0) plus **1 Part II Composites problem** (5.0 pts), 60 min (assumption; options 50, 60, 75 min).
2. **`paper-2020`:** Reproduces the December 2020 distribution across Units 8–10 (**`U8 = 4, U9 = 3, U10 = 3`**) plus **1 Part II Composites problem** (5.0 pts), 60 min.
3. **`custom-test`:** Pick 1, 2, 3, or all 4 units (Units 8–11) and 5, 10, 15, 20, or 30 questions spread evenly across the selected units, either timed (default 20 min; options 10, 15, 20, 30, 45 min) or with instant feedback.
4. **`problems`:** Practice 1 or 2 Part II / final calculation problems (default 1 problem, 35 min; options 25, 35, 50 min) chosen by archetype across Unit 10 (`composite-unidirectional`, `composite-hybrid-specific`, `composite-selection-inverse`), Unit 8 (`ceramic-structure`), and Unit 9 (`polymer-mw-crystallinity`).

The final exams are open-answer papers (`2 h 30 min`, `MATERIALS_FINALEXAM_2017_ORD.pdf`, p. 1) with no multiple-choice section; they supply the True/False statements, short-theory styles, and Unit 8 / Unit 9 / Unit 10 full calculation archetypes.

## 2. Complete inventory of official MCQs & final exam questions (Units 8 to 11)

### 2.1 Official 2020 Assessment Test III MCQs (Model B and Paper B)

Sources: `MATERIALS_THIRDPARTIAL_2020.pdf` (pp. 1–2, also in `V2` pp. 2–3) and `MATERIALS_THIRDPARTIAL_2020_V2.pdf` (Paper B, pp. 4–5). Across all **20 official MCQs** (10 in Model B and 10 in Paper B), there are **0/10 numeric calculation questions in Model B and 0/10 in Paper B (0/20 overall)**. Every single Part I test item on Midterm 3 is conceptual, structural, processing-based, or comparative.

**Model B (`MATERIALS_THIRDPARTIAL_2020.pdf`, pp. 1–2):**

| Q | Unit | Concept | Format | Opening words | Figure | Verified answer & wrong options built from |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 8 | Zinc blende ionic structure | identify | "Which ionic structure has cubic packing of the negative ions and positive ions filling half of the tetrahedra interstitials" | no | `a` (`Zn-blende structure`); wrong: other $AX$/$AX_2$ cells (`Fluorite` all tetrahedral, `NaCl` all octahedral, `CsCl` simple cubic) |
| 2 | 8 | Factors governing ionic packing | identify | "Which of the following factors are important in determine the packing of ions and cations (only one correct answer)" | no | `c` (`Relative size of anions and cations and electroneutrality`); wrong: non-geometric/unrelated parameters (`Lattice energy`, `Valance and bond length`, `All of the above`) |
| 3 | 8 | Ceramic processing and sintering | topic-true | "Which of the following statements about ceramics is TRUE:" | no | `b` (`Ceramic injection molding involves mixing a ceramic powder with a binder or wax`); wrong: inverted accuracy of slip casting (`high dimensional accuracy`), above-$T_m$ sintering, and sintered compact misnamed `"green compact"` |
| 4 | 8 | Glasses: definition, constituents, melting, flaws | true-statement | "Which of the following statements is TRUE:" | no | `d` (`Mechanical properties of glasses, like those of ceramics, are influenced strongly by imperceptions and defects`); wrong: glass called purely ionic, $\text{Al}_2\text{O}_3$ called a glass former (actually intermediate), glass given a distinct melting point |
| 5 | 9 | Structural factors favouring crystallinity | identify | "Which of the following polymers is more likely to be crystalline?" | no | `a` (`Polyethylene`); wrong: three amorphous structures (`Atactic Polypropylene`, `Epoxy resin` thermoset, `Styrene-butadiene (SB) copolymer` elastomer/random) |
| 6 | 9 | Polymer structure, orientation and types | true-statement | "Which of the following statements is TRUE:" | no | `c` (`Deforming a polymer can increase their strength`); wrong: thermosets called crystalline, thermoplastics said unable to be reheated, homopolymers given $>1$ monomer type |
| 7 | 9 | Processing method for thermosets | identify | "Which of the following processing method is more appropriate for thermosetting polymers" | no | `b` (`Transfer molding`); wrong: three thermoplastic forming processes (`Thermoforming`, `Extrusion`, `Blow molding`) |
| 8 | 10 | Functions of matrix vs fibres | identify (negative) | "Indicate which of the following is NOT the function of the matrix in a fiber reinforced composite:" | no | `d` (`Support the major part of the applied load`, which is the fibre function); wrong: three real matrix functions (`Transfer external load`, `Prevents chemical and abrasive degradation`, `Keeps fiber orientation`) |
| 9 | 10 | Prepregs and laminar composites | false-statement | "Which of the following statement is FALSE:" | no | `a` (`Prepegs cannot be assembled into laminated structures`); wrong (true): prepreg definition, laminar stacking of oriented layers, limited shelf life of thermoset prepregs |
| 10 | 10 | Aerospace applications in civil aircraft | identify | "Typical applications for composites in civil aircrafts are:" | no | `c` (`Engine cowlings, elevators and spoilers`, overriding student blue circle on `b`); wrong: turbine blades (excluded/superalloys), bulkheads and stringers (selective newer airframes only), landing gear (excluded) |

**Paper B (`MATERIALS_THIRDPARTIAL_2020_V2.pdf`, pp. 4–5):**

| Q | Unit | Concept | Format | Opening words | Figure | Verified answer & wrong options built from |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 9 | Properties and processing of thermoplastics | topic-false | "Indicate which one of the following statements related to thermoplastic properties is FALSE:" | no | Opt 1 (`Processing of the thermoplastic polymers involves cross-linking between chains`); wrong (true): recyclable/reusable, soften on heating and harden on cooling, used for plastic bottles |
| 2 | 9 | Factors raising polymer crystallinity | complete-sentence | "Crystallinity of a polymer is higher..." | no | Opt 3 (`due to an increase in its molecular weight`, red tick + Slides 26–27/30); wrong: atactic vs isotactic PP swapped, random vs block copolymer swapped, more complex monomer |
| 3 | 9 | Polymer sheet forming process | identify | "The most suitable process for manufacturing a thermoplastic sheet of a certain shape with a high quality and good durability is:" | no | Opt 4 (`Thermoforming`); wrong: three other thermoplastic processes (`Injection molding` 3D cavities, `Blow molding` hollow containers, `Extrusion` continuous profiles) |
| 4 | 8 | Ceramic mechanical, thermal, electrical and glass roles | true-statement | "Indicate which of the following statements is TRUE:" | no | Opt 4 (`Ceramics are good electrical and thermal insulators`); wrong: tension better than compression (inverted), high thermal shock resistance (inverted), $\text{SiO}_2$ called a glass modifier (actually former) |
| 5 | 8 | Zinc blende crystal structure | complete-sentence | "A ceramic material with a zinc blende structure presents..." | no | Opt 2 (`cations occupying half of the tetrahedral interstitial sites of the FCC unit cell`); wrong: C.I. = 6 (NaCl), HCP anions (corundum), all octahedral sites (NaCl) |
| 6 | 8 | Coordination index in CaO (rock salt) | identify | "CaO presents a \"rock salt\" structure. Identify the coordination index for O2- ions:" | no | `6` (red tick, overriding stray pencil circle on `8`); wrong: `8` (CsCl / fluorite cation), `3` (triangular), `4` (ZnS / fluorite anion) |
| 7 | 8 | Ceramic tape casting | complete-sentence | "For fabrication of ceramic layers, _______ process involves the casting the slurry onto a flat moving carrier surface." | no | Opt 1 (`Tape casting`); wrong: three other ceramic shaping routes (`Slip casting`, `Ceramic injection moulding`, `Extrusion`) |
| 8 | 10 | Classification of Kevlar 29 | identify | "Which type of fiber is the Kevlar 29?" | no | Opt 2 (`Aramid fibre`); wrong: the three other aerospace fibre families (`Carbon fibre`, `Glass fibre`, `Boron fibre`) |
| 9 | 10 | Transverse (isostress) loading of continuous-fibre composite | what-happens | "When stress is applied perpendicular to fibers in a continuous fibers reinforced composite:" | no | Opt 2 (`Matrix is subjected to higher deformation`, confirmed via Slides 23–24); wrong: fibres deform more (swapped $E$), fibres or matrix carry higher stress (ignores equal isostress $\sigma_f = \sigma_m$) |
| 10 | 10 | Two-phase MMC processing | identify | "Select the method for processing of composites in which reinforcement is introduced into spray of melt droplets:" | no | Opt 3 (`Spray co-deposition`); wrong: the other MMC liquid/two-phase methods (`Rheocasting`, `Melt stirring`, `Squeeze casting`) |

### 2.2 Official True/False statements and short-theory / problem items (Finals 2012–2017 and `Problems T8`–`T10`)

**True/False table (Units 8–11):**

| Exam & Question | Unit | Statement | Official key | Reason |
| :--- | :--- | :--- | :--- | :--- |
| `2017_ORD` Q7.1 | 8 | "The fluorite structure (CaF2) is FCC, where Ca2+ ions are located in the FCC lattice sites and the F- ions occupy half of the tetrahedral sites" | **F** | $\text{F}^-$ ions occupy **all** tetrahedral sites (`Session 16`, Slide 10) |
| `2017_ORD` Q7.2 | 8 | "Hardness of ceramic materials with covalent bonds is higher than those with ionic ones." | **T** | Covalent ceramics (diamond, SiC) are harder than ionic oxides (`Session 16`, Slide 16) |
| `2017_ORD` Q7.3 | 8 | "For fabrication of ceramic layers, slip casting process involves the casting the slurry onto a flat moving carrier surface." | **F** | Casting onto a flat moving carrier is **tape casting**, not slip casting (`Session 18`, Slide 18) |
| `2017_ORD` Q7.4 | 8 | "Sintering a ceramic material involves heating the part to an elevated temperature above the melting point in a controlled environment." | **F** | Sintering takes place **below** the melting point by solid-state/liquid-phase diffusion (`Session 18`, Slide 25) |

**Short-theory, matching, ordering and calculation items in Final Exams (2012–2017):**

| Unit | Concept | Form in the finals | Source |
| :--- | :--- | :--- | :--- |
| 8 | KCl ($\text{CsCl}$ vs $\text{NaCl}$ structure check, packing factor); $\text{GaAs}$ (zinc blende: structure, C.I., $a$, $\rho$, $\rho_{[111]}$, $\rho_{(111)}$, APF); $A_x B_y$ from `(010)`/`(110)` planes; $\text{CeO}_2$ fluorite; $\text{BaTiO}_3$ perovskite | calculation problem (1.5–2.0 pts) | `2012_ORD` Q1; `2014_EXTRA` Q1; `2015_ORD` Q1; `2016_ORD_SOL` Q8; `2017_EXTRA` Q7 |
| 8 | Ceramics vs glasses (structure and processing); structural causes of hardness and brittleness; thermal shock mechanism; packing factors; traditional vs engineering ceramics and sintering; ionic lattice energy parameters and matching $T_m$, $U$, hardness (`NaCl`, `KCl`, `MgO`, `BaO`); dry-pressing steps | short-theory / matching (0.5–1.0 pt) | `2012_ORD` Q8; `2012_EXTRA` Q7; `2013_ORD` Q6; `2014_ORD` Q5; `2015_EXTRA` Q6, Q7; `2016_EXTRA_SOL` Q7 |
| 8 / 9 | Order `Aluminium`, `Aluminium oxide`, `Epoxy Resin`, `Low Density Polyethylene` by hardness and elastic modulus + justify | ordering + justification (1.0 pt) | `2014_EXTRA` Q4 |
| 9 | Monodisperse polymer ($M = 200\,000\text{ g/mol}$) contaminated with 1 wt% impurity ($1000\text{ g/mol}$): calculate $\bar{M}_n$ and $\bar{M}_w$ | calculation problem (1.0 pt) | `2017_EXTRA` Q8 |
| 9 | Effect of strain rate and $T$ on thermoplastic $\sigma$-$\varepsilon$ / $E$; chain branching on crystallinity/strength/elongation; thermoplastics vs thermosets (chain bonding, temperature stability, processing, extrusion); semicrystalline $\sigma$-$\varepsilon$ curve and tie-chain deformation; $T_g$ matching/series (`PE`, `PP`, `PVC`, `epoxy`); tensile strength comparison across tacticity/MW/crosslinking/density; why crosslinking raises $T_g$ and why polymers are never 100 % crystalline | short-theory / sketch / comparison (0.5–1.0 pt) | `2012_ORD` Q9; `2012_EXTRA` Q8; `2013_EXTRA` Q7; `2014_ORD` Q6; `2014_EXTRA` Q5; `2015_ORD` Q3; `2015_EXTRA` Q1; `2016_ORD_SOL` Q9; `2016_EXTRA_SOL` Q8; `2017_ORD` Q8 |
| 10 | Unidirectional composite: longitudinal & transverse moduli, density, weight fraction, fibre/matrix load ratio & stresses, rod extension, $\sigma_C$, specific strength/modulus, reinforcement selection ($V_f \le 40\%$), inverse $V_f$ from fibre stress | calculation problem (1.0–2.0 pts; 5.0 pts in Test 3) | `2012_ORD` Q5; `2012_EXTRA` Q4; `2013_EXTRA` Q3; `2014_EXTRA` Q2; `2016_ORD_SOL` Q10; `2017_ORD` Q9; `2017_EXTRA` Q9; `2020_V2` p. 8 |
| 10 | Common fibre types, PMC processing, parallel vs perpendicular anisotropy; primary roles of matrix vs fibres & prepreg manufacture; GLARE components/applications/advantages; CMCs (matrices, advantages, reinforcement role, unique processing); identifying fibre, composite and matrix $\sigma$-$\varepsilon$ curves + residual fracture stress $\sigma_m(1-V_f)$ | short-theory / diagram ID (0.5–1.0 pt) | `2013_ORD` Q3; `2014_ORD` Q3; `2015_ORD` Q4; `2015_EXTRA` Q5; `2016_EXTRA_SOL` Q9 |
| 11 | Joint design selection from schematics (90° L-bracket peel vs compression; butt vs lap joint) + maximize shear/compression, minimize peel/tension; surface preparation & primers; production steps & design considerations; prepolymerized vs polymerizing adhesives; failure modes with sketches | short-theory / diagram selection (0.5–1.0 pt) | `2013_ORD` Q4B; `2013_EXTRA` Q6A; `2014_EXTRA` Q6A; `2015_ORD` Q6(a); `2016_EXTRA_SOL` Q10; `2017_ORD` Q10 |

**Conceptual and problem items embedded in `Problems T8`–`T10`:**

- **`Problems T8_CeramicMaterials.pdf` (Problems 1–7):** Calculation problems on ZnS, $\text{CaTiO}_3$, $A_x B_y C_z$ orthorhombic perovskite, $AB_2$ fluorite, $AB$ rock salt, $\text{SrSnO}_3$, and MgO (unit cell volume, theoretical density, packing factor, linear and planar ionic densities, rod mass). Conceptual structure identification and close-packing description appear directly in Q3(a),(c), Q4(a), and Q5(a).
- **`Problems T9_Polymers.pdf` (Problems 1–9):** Quantitative problems on degree of polymerization and number of chains (Q1), degree of crystallinity from density (Q6, Q9), and molecular weight averages, PDI, and monomer identification (Q7, Q8). Strong conceptual core across Q2 (crystallization likelihood: linear vs branched PE, PE vs copolymer, isotactic vs atactic PP), Q3 (rolling vs fast-cooled casting strength), Q4 (ranking $T_m$ across four pairs), Q5 & Q6 ($\log E$ vs $T$ plots for MW, crosslinking, crystallinity), Q7(d) (side-group effect on crystallinity), Q8(c) (identifying Nylon 6,6 from $M_0$), and Q9(a) (PP repeat unit and tacticity).
- **`Problems T10_CompositeMaterials.pdf` (Problems 1–12):** Micromechanics calculations on weight fractions, density, $E_1$, $E_2$, fibre/matrix forces, extension, strength, and porous tungsten infiltration (Q1, Q4–Q10, Q12). Selection and comparative trade-off tasks appear in Q1(d) (modulus vs $V_f$), Q2 (choosing carbon vs glass vs aramid for $V_f \le 40\%$), Q3(c)–(d) (hybrid graphite/Kevlar specific properties and critical $V_f$), and Q11(c) (specific modulus comparison of Ti, B–Al, and C–PE for a spacecraft structure).

## 3. Language patterns, formats and negative constraints

- **Opening formulas (literal from Model B and Paper B):** `"Which of the following statements about ... is TRUE:"`, `"Which of the following statements is TRUE:"`, `"Which of the following statement is FALSE:"`, `"Indicate which one of the following statements related to ... is FALSE:"`, `"Which ionic structure has ..."`, `"Which of the following factors are important in ..."`, `"Which of the following polymers is more likely to be ..."`, `"Which of the following processing method is more appropriate for ..."`, `"Indicate which of the following is NOT the function of ..."`, `"Which type of fiber is ..."`, `"When stress is applied perpendicular to fibers in ..."`, `"Select the method for processing of ... in which ..."`, `"Crystallinity of a polymer is higher..."`, `"For fabrication of ceramic layers, _______ process involves ..."`.
- **Additional `topic-true` / `topic-false` openings for the bank:** `"Referring to ..., which one of the following statements is TRUE:"`, `"Regarding ..., indicate which of the following statements is FALSE:"`, `"With respect to ..., which statement is TRUE:"`, always pairing **four independent statements** (as in Model B Q3/Q4/Q6/Q9, Paper B Q1/Q4, and `2017_ORD` Q7) so the student cannot solve by eliminating a 2×2 grid alone.
- **Zero slide/course meta-references:** Question stems and options must test general, fundamental materials science and engineering only. Never write phrases such as *"According to the slides"*, *"In Session 18"*, *"In Table 10.11"*, *"listed in the course notes"*, or *"given in the lecture"* in any stem or option (`tools/build_materials_bank.py` enforces `_SLIDE_META` on every item). Slide numbers belong strictly in `### Source` and `### Explanation`.
- **Numeric MCQ cap (`<= 8%`):** Because official Test 3 Part I papers had **0/20 numeric MCQs**, the bank enforces `MAX_NUMERIC_SHARE = 0.08` across each of Units 8, 9, 10, and 11 — at most **1 quick conceptual calculation per 10-question block** (such as Pauling % ionic character, radius ratio $r_C/r_A$, $X_n = M_n/M_0$, simple rule of mixtures for $\rho_c$ or $E_{1C}$, or reading a peel/shear ratio). Multi-step calculations belong in Part II (`P21`–`P36`).
- **Length, register and units:** Plain, direct engineering English in the present tense, avoiding hedging. Stems are 10–30 words; options are 2–16 words with parallel grammar and balanced length so the right option is never systematically the longest. No absolutes (*"only"*, *"always"*, *"never"*, *"cannot"*) placed exclusively in wrong options. Use SI units throughout (nm, Å only where crystallographic data use Å, MPa, GPa, g/cm³, °C or K as formulas require, N/m) with a space between number and unit.
- **Diagrams and official PNG crops:** `diagram-reading` and `choose-figure` questions embed verified official PNG crops from `vault/attachments/T8/`, `T9/`, `T10/`, and `T11/` (allowed by `_VERIFY_FOLDERS` in `tools/build_materials_bank.py`), never redrawn schematics of printed slide figures. Diagrams are read for structure identification, curve/axis interpretation, thermal-transition shifts, process steps, or joint geometry.

## 4. Anatomy of the wrong options

| Format | What each wrong option exploits |
| :--- | :--- |
| `topic-true` / `topic-false` | Four independent claims mixing inverted property trends, swapped material classes (glass former vs modifier, thermoplastic vs thermoset, covalent vs ionic ceramic), wrong processing temperatures (above vs below $T_m$), or misattributed mechanisms |
| `true-statement` / `false-statement` | Swapped neighbouring terms (`adhesion` vs `cohesion`, `green` vs `brown` compact, `slip` vs `tape` casting, `isostrain` vs `isostress`); true premise with inverted consequence |
| `identify` | The three other members of the official taxonomy (`CsCl`/`NaCl`/`ZnS`/`CaF2`; `glass`/`carbon`/`aramid`/`boron`; `extrusion`/`injection`/`blow`/`thermoforming`/`transfer`/`compression`; `anaerobic`/`cyanoacrylate`/`epoxy`/`polyurethane`) |
| `complete-sentence` | Swapped tacticity (`atactic` vs `isotactic`), swapped copolymer sequence (`random` vs `block`), opposite structural factor, or neighbouring crystal lattice site (`tetrahedral` vs `octahedral`, `half` vs `all`) |
| `cause-effect` | Inverted sign of the effect ($T_g$, $T_m$, crystallinity, $\sigma$, $\varepsilon_f$, peel strength, thermal shock resistance); right trend paired with the wrong microscopic mechanism |
| `what-happens` | Confusing equal stress ($\sigma_f = \sigma_m$ in isostress) with equal strain ($\varepsilon_f = \varepsilon_m$ in isostrain); applying metal plastic blunting to brittle ceramics; confusing adhesive heating degradation with thermoplastic remelting |
| `ordering` | One adjacent pair swapped (e.g., $\text{PP}$ vs $\text{PVC}$ in $T_g$, or aramid vs carbon in modulus vs toughness); fully reversed rank; ranking by $E$ when strength or specific property is asked |
| `diagram-reading` / `choose-figure` | Adjacent curve or region (`amorphous` vs `semicrystalline` vs `crystalline`; `curve A/B/C` swapped; `peel` vs `shear` joint geometry; `poor` vs `good` interface SEM; wrong temperature/viscosity reference point) |
| `numeric` (<= 8 %) | Radius ratio with $r_A/r_C$ inverted; $M_n$ vs $M_w$ formulas swapped; weight fraction confused with volume fraction; $E_{2C}$ computed with isostrain instead of harmonic mean; percent vs decimal |

No absurd distractors: every wrong option corresponds to one nameable mistake, explicitly diagnosed in `### Explanation`.

## 5. Frequency per unit and quota of the bank

Official 2020 Test 3 allocated 4, 3, and 3 questions across Units 8, 9, and 10 (with 2 extra Unit 7 questions on `V2`) plus one 5-point Composite Materials problem. In 2026–27, Test 3 covers Units 8, 9, 10, and 11, so the blueprint default is `3 + 3 + 2 + 2` plus one Composite Materials problem (`U10`). The bank holds **500 MCQs across 50 blocks (`B63` to `B112`)** and **16 Part II / final calculation problems (`P21` to `P36`)**:

| Unit | Share of default 2026–27 test | Share of 2020 paper | MCQs in the bank | Blocks of ten | Block ids | Part II / final problems |
| :--- | :--- | :--- | ---: | ---: | :--- | :--- |
| 8 · Ceramic materials | 3 of 10 | 4 of 10 | 140 | 14 | `B63` to `B76` | 3 (`P31`–`P33`, `ceramic-structure`) |
| 9 · Polymers | 3 of 10 | 3 of 10 | 140 | 14 | `B77` to `B90` | 3 (`P34`–`P36`, `polymer-mw-crystallinity`) |
| 10 · Composite materials | 2 of 10 (+ 5 pt problem) | 3 of 10 (+ 5 pt problem) | 140 | 14 | `B91` to `B104` | 10 (`P21`–`P30`, Composites) |
| 11 · Adhesives | 2 of 10 | — | 80 | 8 | `B105` to `B112` | — |
| **Total** | **10** | **10** | **500** | **50** | **`B63`–`B112`** | **16 (`P21`–`P36`)** |

Target format mix over the 500 MCQs (reflecting the strictly conceptual 2020 Part I papers): `topic-true` and `topic-false` 25 %, `true-statement` and `false-statement` 18 %, `identify` 18 %, `complete-sentence` 14 %, `cause-effect` 9 %, `what-happens` 5 %, `diagram-reading` and `choose-figure` 5 %, `ordering` 4 %, and `numeric` <= 8 % (strictly <= 1 quick conceptual calculation per block, hard-capped at <= 8 % per unit by `tools/build_materials_bank.py`). Right letters `a` to `d` are balanced between 20 % and 30 % across Midterm 3 with no four identical answers in a row, and at most four questions share a single `concept_id` (each differing in `(format, asks)`).

### 5.1 Concept-group breakdown per unit

**Unit 8 · Ceramic materials (140 MCQs, Blocks `B63` to `B76`)**

| Concept group | Official sources | Questions |
| :--- | :--- | ---: |
| General properties, bonding-property chain, traditional vs engineering ceramics | `Session 16`, Slides 2–4; `Session 18`, Slides 4, 42 | 10 |
| Pauling ionic/covalent character and ionic packing rules ($r_C/r_A$, C.I., electroneutrality) | `Session 16`, Slides 5–6 | 12 |
| $AX$ crystal structures: CsCl, rock salt (NaCl), zinc blende (ZnS) | `Session 16`, Slides 7–9, 14; `Problems T8`, Q1, Q5, Q7 | 14 |
| $AX_2$, $ABO_3$, and corundum structures: fluorite, anti-fluorite, perovskite, corundum | `Session 16`, Slides 10–14; `Problems T8`, Q2, Q3, Q4, Q6 | 14 |
| Covalent ceramics (diamond, SiC, $\text{Si}_3\text{N}_4$) and silicates ($\text{SiO}_4^{4-}$, silica allotropy, feldspars) | `Session 16`, Slides 15, 23–26 | 12 |
| Mechanical behaviour of ceramics: hardness, stiffness ($E/\rho$), porosity, tension vs compression, 3-point bending (MOR), Weibull scatter | `Session 16`, Slides 16–20 | 14 |
| Thermal shock and ferroelectric/piezoelectric ceramics ($\text{BaTiO}_3$) | `Session 16`, Slides 21–22 | 8 |
| Glasses: $T_g$ vs $T_m$, formers/modifiers/intermediates, glass types, optical/electrical/thermal properties, glass-ceramics (LAS) | `Session 16`, Slides 27–32 | 14 |
| Ceramic processing chain: raw materials, Acheson SiC synthesis, milling, additives, spray-dry granulation | `Session 18`, Slides 5–8 | 8 |
| Ceramic shaping: uniaxial pressing, CIP (wet/dry bag), colloidal slips, slip casting, tape casting, extrusion, injection moulding, additive manufacturing | `Session 18`, Slides 9–22, 29 | 14 |
| Drying, debinding, and sintering (densifying vs non-densifying mechanisms, liquid-phase, HIP, SPS) | `Session 18`, Slides 23–28 | 10 |
| Glass processing (viscosity points, float/drawing/blowing, tempering, optical fibres) and aerospace uses (Shuttle TPS, TBC YSZ, turbine parts) | `Session 18`, Slides 30–41 | 10 |

**Unit 9 · Polymers (140 MCQs, Blocks `B77` to `B90`)**

| Concept group | Official sources | Questions |
| :--- | :--- | ---: |
| Monomers, macromolecules, plastic vs polymer, classification, addition vs condensation polymerization | `Session 19`, Slides 2–11 | 12 |
| Molecular weight distribution, $M_n$, $M_w$, polydispersity index $I$, degree of polymerization $X_n$ | `Session 19`, Slides 12–15; `Problems T9`, Q1, Q7, Q8 | 12 |
| Conformation, chain coiling, *cis*/*trans* isomerism, tacticity (isotactic, syndiotactic, atactic), homopolymers and copolymers | `Session 19`, Slides 16–20; `Problems T9`, Q2, Q9 | 14 |
| Molecular architecture (linear, branched, crosslinked, network) and interchain bonding | `Session 19`, Slides 21–22 | 8 |
| Semicrystalline vs amorphous polymers, spherulites, lamellae, tie chains, density-crystallinity equation | `Session 19`, Slides 23–25; `Problems T9`, Q6, Q9 | 12 |
| Factors affecting crystallinity (cooling rate, monomer complexity, branching, tacticity, polarity, copolymer sequence) | `Session 19`, Slides 26–27; `Problems T9`, Q2, Q7(d) | 12 |
| Thermal transitions ($T_g$ vs $T_m$), specific volume/density plots, side-group/intermolecular effects on $T_g$ and $T_m$, MW-temperature map | `Session 19`, Slides 28–30; `Problems T9`, Q4 | 14 |
| Stress–strain behaviour (brittle, ductile, cold drawing, elastomers), chain deformation stages, orientation hardening, $T$ and strain-rate effects | `Session 19`, Slides 31–44; `Problems T9`, Q3 | 14 |
| $\log E$ vs $T$ regimes and viscoelasticity: creep compliance $J(t)$, stress relaxation $E_r(t)$, time–temperature equivalence | `Session 19`, Slides 45–50; `Problems T9`, Q5, Q6 | 10 |
| Polymer families by temperature/structure and use: commodity and engineering thermoplastics, thermosets, elastomers (vulcanization, SBR), fibres | `Session 20`, Slides 3–16, 36 | 16 |
| Polymer processing & selection: extrusion, injection, blow, rotational, thermoforming, compression, transfer moulding; cost/volume trade-offs | `Session 20`, Slides 17–35, 38 | 16 |

**Unit 10 · Composite materials (140 MCQs, Blocks `B91` to `B104`)**

| Concept group | Official sources | Questions |
| :--- | :--- | ---: |
| Concept of composites, synergism, constituents/interface, classification by matrix (PMC/MMC/CMC) and reinforcement, geometric factors | `Session 21`, Slides 2–8 | 10 |
| Particle-reinforced composites (large particles, cermets) and dispersion-strengthened composites (SAP, TD-Ni) | `Session 21`, Slides 9–13 | 10 |
| Fibre-reinforced composites: fibre vs matrix functions, glass fibres & sizing, carbon fibres (PAN/pitch, Types I–III, tows), aramid (Kevlar/Nomex), ceramic fibres, fabrics/NCFs/preforms | `Session 21`, Slides 14–34 | 20 |
| Structural composites: symmetric/balanced laminates, quasi-isotropic stacks, sandwich panels (faces & honeycomb core), GLARE FML | `Session 21`, Slides 35–39 | 12 |
| Mechanical & specific properties of fibres and epoxy composites (UD 0° vs 90°, 0/90, $\pm 45$, specific stiffness and strength) | `Session 21`, Slides 40–43; `Problems T10`, Q2, Q3, Q11 | 10 |
| Polymer matrices (thermoset epoxy/BMI/polyimide vs thermoplastic PEEK/PPS/PEI, additives) and interface adherence (coupling agents, SEM) | `Session 22`, Slides 2–18 | 14 |
| Micromechanics: isostrain $E_{1C}$ & load sharing, isostress $E_{2C}$ & strain, strength $\sigma_C$, $V_{\min}$/$V_{\text{crit}}$, particle bounds ($n = \pm 1$), $K_{IC}$ | `Session 22`, Slides 19–29; `Problems T10`, Q1–Q12 | 18 |
| PMC manufacturing: B-stage prepregs, SMC, hand/spray lay-up, vacuum/pressure-bag, compression, RTM, RFI, filament winding, ATL, AFP, pultrusion, autoclave, co-curing/co-bonding | `Session 23`, Slides 2–29 | 20 |
| MMC and CMC processing & toughness: solid-state, liquid-phase (melt stirring, squeeze casting, infiltration), two-phase (rheocasting, spray co-deposition); CMC crack bridging/pull-out, sol-gel, slurry | `Session 23`, Slides 30–45; `Problems T10`, Q12 | 14 |
| Aerospace & structural applications: civil aircraft (B757–787, A320–A380), military fighters, helicopters, satellites, Shuttle RCC, naval/automotive/MMC uses | `Session 23`, Slides 46–65 | 12 |

**Unit 11 · Adhesives (80 MCQs, Blocks `B105` to `B112`)**

| Concept group | Official sources | Questions |
| :--- | :--- | ---: |
| Joining methods compared (fasteners, welding, adhesives), adhesion vs cohesion definitions, advantages and disadvantages | `Session 24`, Slides 2–4 | 8 |
| Adhesion mechanisms (mechanical, electrostatic, diffusive, adsorption/dispersive, chemisorption) and wetting & surface roughness | `Session 24`, Slides 5–9 | 14 |
| Adhesive components (base polymer, primers, plasticizers, tackifiers, coupling agents, fillers) and classification (application, temperature, origin, curing) | `Session 24`, Slides 10–12 | 10 |
| Specific adhesive families & curing: rigid/tough/flexible classes, anaerobics, cyanoacrylates, epoxies, polyurethanes, silicones, modified acrylics, phenolics | `Session 24`, Slides 12–14, 24, 35–38 | 14 |
| Joint production chain, selection (CTE match), and joint design (shear/compression vs peel/cleavage/tension; lap, scarf, stepped, tapered joints) | `Session 24`, Slides 15–20 | 12 |
| Adherent preparation (degreasing, abrasion, anodizing), primers, and curing triggers | `Session 24`, Slides 21–24 | 8 |
| Testing (tack, peel brittle vs tough, normal/shear), failure modes (acceptable vs unacceptable), and environmental degradation (T, moisture hydrolysis/segregation, corrosion, UV/O₂ ageing) | `Session 24`, Slides 25–34 | 14 |

## 6. Problem types of Part II and finals (`P21` to `P36`)

Part II of Midterm 3 is **one 5.0-point Composite Materials problem** (`P21` to `P30`, Unit 10). In addition, final exams from 2012–2017 feature multi-part calculation problems on Unit 8 ceramic crystal structures (`P31` to `P33`) and Unit 9 polymer molecular weight and crystallinity (`P34` to `P36`), which the simulator makes available under the `problems` practice mode. Every problem carries **5.0 points** across 3 or 4 subquestions.

| Type (`archetype`) | Unit | Real exam & sheet models | Typical subquestions | Problems |
| :--- | :--- | :--- | :--- | :--- |
| `composite-unidirectional` | 10 | `2020_V2` p. 8 (carbon/polyester); `2013_EXTRA` Q3; `2014_EXTRA` Q2; `2012_EXTRA` Q4; `2017_ORD` Q9; `Problems T10`-01, 04, 05, 06, 08, 10 | composite density $\rho_c$; weight fraction $w_f$; longitudinal $E_{1C}$ and transverse $E_{2C}$; fibre-matrix load ratio $F_f/F_m$; phase stresses $\sigma_f,\sigma_m$ and forces $F_f,F_m$; elongation $\Delta L$; longitudinal strength $\sigma_C$ | `P21` to `P24` (4) |
| `composite-hybrid-specific` | 10 | `2020` Model B Part II (`V2` p. 6, graphite-HM + Kevlar-49/epoxy); `Problems T10`-03, 07, 11 | hybrid density, modulus and tensile strength; specific modulus $E/\rho$ and specific strength $\sigma/\rho$; mass saving and comparison with Al 2024 / Ti alloys; transverse modulus $E_{2C}$ | `P25` to `P27` (3) |
| `composite-selection-inverse` | 10 | `2012_ORD` Q5 (choice at $V_f \le 40\%$); `2016_ORD_SOL` Q10 (inverse $V_f$); `Problems T10`-02, 09, 12 | candidate fibre selection meeting minimum $E_c$ and $\sigma_c$ below $V_{\max}$; inverse volume fraction $V_f$ from applied load and fibre stress; required fibre mass or infiltrated porous density | `P28` to `P30` (3) |
| `ceramic-structure` | 8 | `2012_ORD` Q1; `2014_EXTRA` Q1; `2015_ORD` Q1; `2016_ORD_SOL` Q8; `2017_EXTRA` Q7; `Problems T8`-01 to 07 | structure ID from $r_C/r_A$ or plane sketches; stoichiometry and coordination numbers; lattice parameter $a$; APF and theoretical density $\rho$; linear and planar ionic densities; part mass | `P31` to `P33` (3) |
| `polymer-mw-crystallinity` | 9 | `2017_EXTRA` Q8 (1 % impurity); `Problems T9`-01, 06, 07, 08, 09 | $M_n$, $M_w$, polydispersity $I = M_w/M_n$, degree of polymerization $X_n$, chain count, repeat-unit identification, forward and inverse density-crystallinity calculations | `P34` to `P36` (3) |

## 7. Rules for the bank notes

- One block of ten questions is one note, `Quiz - Bank Bnn - Unit N <theme>.md`; one problem is one note, `Problem - Bank Pnn - <title>.md`. Builder and checks: [[Tool - build_materials_bank]].
- Every practice item carries the `"Practice item, not an official exercise"` callout (or `"Includes official exam questions"` / `"Includes official exam adaptation"` where official items are adapted).
- Question stems and options never cite slides, sessions, tables, or lecture notes (`_SLIDE_META`); physical constants and material properties come from `Session 16`–`Session 24` and `Problems T8`–`T10` and are cited in `### Source`. Anything beyond the slides is omitted or explicitly marked **extension**.
- Numeric `calc` and `check` fields in MCQs and `## Verification` lines in Part II / final problems are recomputed by `tools/materials_bank/verify_mt3.py`.
- Diagram questions use existing official PNG crops from `vault/attachments/T8/`–`T11/` (or `MAT-MT3/` if new derived schematics are added for Part II problems).

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]] · [[Aerospace Materials I MOC]]
