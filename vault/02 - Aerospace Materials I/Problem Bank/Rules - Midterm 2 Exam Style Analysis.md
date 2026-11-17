---
materia: Aerospace Materials I
tema: "Assessment Test II (Units 4 to 7): structure, question style and bank plan"
tipo: rules
estado: active
fuentes:
  - "sources/cuatrimestre-1/02-aerospace-materials-1/examenes/MATERIALS_SECONDPARTIAL_2019.pdf"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/examenes/MATERIALS_SECONDPARTIAL_2018.docx"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/examenes/MATERIALS_FINALEXAM_COMPILATION_2013-2017.pdf"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/examenes/MATERIALS_FINALEXAM_2017_ORD.pdf"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/examenes/MATERIALS_THIRDPARTIAL_2020_V2.pdf"
  - "sources/cuatrimestre-1/02-aerospace-materials-1/examenes/first-partial/1stPartialTipoTestsVariados.pdf"
tags:
  - problem-bank
  - midterm-2
  - exam-analysis
  - rules
---

# Midterm 2 (Assessment Test II): exam style analysis and bank plan

This note is the specification of the Midterm 2 bank: what the real paper looks like, how its test questions are written, which mistakes its wrong options exploit, and how many questions the bank holds per unit and per concept. The bank notes (`Quiz - Bank Bnn - ...`, `Problem - Bank Pnn - ...`) follow it, and `tools/build_materials_bank.py` enforces the countable rules.

## 1. Structure of the paper

| Item | Value | Source |
| :--- | :--- | :--- |
| Name and date | "Assessment Test II", model B, 22 November 2019, course 2019/20, "Grade: Points/10" | MATERIALS_SECONDPARTIAL_2019.pdf, p. 2 |
| Part I | "Part I (5 points)": 10 test questions, four options (a to d), "There is only one correct answer per question" | 2019, p. 2 (questions 1 to 5) and p. 3 (questions 6 to 10) |
| Scoring of Part I | "The correct answers will mark + 0.5 points while the incorrect answers will mark as -0.15 points. Non answered questions will not mark nor positively nor negatively. The resulting mark will not be smaller than 0 in any case." | 2019, p. 2, header |
| Answer sheet | "Mark the right answer with a X in the table below" | 2019, p. 2, header |
| Material allowed | "Neither books nor any other extra material is allowed in the exam but the calculator." | 2019, p. 2, header |
| Part II | One problem, "2. (5 points)", on the Ni-Nb phase diagram, four parts: a) 1.2 p, b) 1.3 p, c) 1.3 p, d) 1.2 p | 2019, p. 4 |
| Part II in 2026-27 | Two problems: a longer one on phase diagrams and a shorter one on Unit 5 (mechanical properties). Points used here: 3.0 + 2.0, from the 2:1 ratio of the finals (section 6) | Course announcement for 2026-27, given by the student; points are an assumption |
| Figures | Pb-Sn diagram printed under question 10 (used by question 7); four dipole pictures as the options of question 9; the Ni-Nb diagram of the problem | 2019, pp. 3 and 4 |
| Duration | Not printed | 2019 and 2018 |
| 2018 paper | The same ten questions (question 2 with 6400 N instead of 6000 N) and the same problem, with no header | MATERIALS_SECONDPARTIAL_2018.docx |

Discrepancies between the sources, and the choice made:

- **Force of question 2.** 2018 gives 6400 N, 2019 gives 6000 N. With the 5 mm wire, $\sigma = F/A_0 = 6400/(\pi\cdot 2.5^2) = 326$ MPa in 2018 (above the tensile strength of 310 MPa) and $6000/(\pi\cdot 2.5^2) = 306$ MPa in 2019 (between the yield strength of 250 MPa and the tensile strength). The two years therefore have different right answers. The most recent paper (2019) is taken as the model.
- **Hand marks of the 2019 scan** (reading of the scan): the circled options are 1 d, 2 c, 3 b, 4 a, 5 b, 8 d, 9 a, 10 c; questions 6 and 7 carry no clear mark. They are a student's answers, not a key. For question 2 the circle is on c (necking), while the computed stress (306 MPa) is below the tensile strength, which gives a (plastic and uniform deformation). The bank follows the computation.
- **Duration.** No paper prints it. `Schedule_MAT AERO I 2026 - 27.pdf` gives the test one session shared with the resolution of problems. The simulator uses 60 minutes as its standard and says that it is an assumption.

The final exams are open-answer papers (2 h 30 min, MATERIALS_FINALEXAM_2017_ORD.pdf, p. 1): they have no multiple-choice part, so they are used here for the problem types and for the True or False statements with a justification, not for the scoring.

## 2. Inventory of the real test questions on Units 4 to 7

Source: MATERIALS_SECONDPARTIAL_2019.pdf (pp. 2 and 3); the same questions are in MATERIALS_SECONDPARTIAL_2018.docx and on sheet A (p. 2) of first-partial/1stPartialTipoTestsVariados.pdf.

| Q | Unit | Concept | Format | Opening words | Figure | Wrong options built from |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 5 | Elastic and plastic deformation at the atomic level | true-statement | "Which one of the following statements is TRUE" | no | elastic and plastic swapped (two options); a true premise with a false consequence (E "stress-dependent") |
| 2 | 5 | Stress against yield and tensile strength | what-happens (hidden calculation) | "A 6000 N force is applied to a 5 mm diameter nickel wire having ... What will happen with the wire:" | no | the three other regions of the curve (elastic recovery, necking, fracture) |
| 3 | 5 | Strain hardening | identify | "Which strengthening mechanism in metallic materials is based on ..." | no | the three other strengthening mechanisms |
| 4 | 6 | Conductivity of metals and temperature | cause-effect | "With an increase in temperature the electrical conductivity of metals:" | no | 2 x 2 grid: right or wrong trend, each with a right or wrong reason |
| 5 | 6 | Extrinsic semiconductor at high temperature | complete-sentence | "Extrinsic semiconductor behaves as an intrinsic one only:" | no | the opposite limit (very low temperature) and an irrelevant feature (p type, n type) |
| 6 | 4 | Microstructure of a hypoeutectoid steel | complete-sentence | "Microstructure of steel with 0.5 wt% C below 727 °C consists of:" | no | 2 x 2 grid: matrix (pearlite or austenite) x proeutectoid phase (ferrite, austenite, cementite) |
| 7 | 4 | Range of compositions that undergo the eutectic reaction | diagram-reading | "From the shown Pb-Sn phase diagram, indicate which alloys will go through ..." | Pb-Sn diagram | half of the right range; only the eutectic composition; the range with no eutectic |
| 8 | 5 | Young's modulus from Poisson's contraction | numeric | "Determine the modulus of elasticity of some hypothetical alloy if it has ..." | no | four values in GPa, three significant figures, evenly spaced (160, 190, 220, 250) |
| 9 | 7 | Paramagnetism without field | choose-figure | "Which picture describes paramagnetic material before application of an external field?" | four dipole pictures | the other orderings (ferromagnetic, antiferromagnetic, ferrimagnetic) |
| 10 | 7 | Thermal expansion and bonding | complete-sentence (four independent statements) | "The linear coefficient of thermal expansion:" | no | inverted trend; a false "is not affected by"; a wrong comparison with a false reason |

Assessment Test III of 16 December 2020 covers Units 8 to 11, but its Wuolah copy (MATERIALS_THIRDPARTIAL_2020_V2.pdf) carries four more test questions on Unit 7:

| Item | Unit | Concept | Format | Opening words | Figure | Wrong options built from |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| "9" (p. 3) | 7 | Paramagnetism without field | choose-figure | the same question 9 of 2019 | four dipole pictures | the other orderings |
| "10" (p. 3) | 7 | Thermal expansion and bonding | complete-sentence | the same question 10 of 2019 | no | as above |
| "11" (p. 5) | 7 | Ferrimagnetism | choose-figure | "Which picture describes ferrimagnetic material before application of an external field?" | four dipole pictures | the other orderings |
| "12" (p. 5) | 7 | Thermal expansion coefficient | true-statement | "Indicate which statement is TRUE regarding the thermal expansion coefficient (α)" | no | an absolute ("Ceramics do not experience thermal expansion"); inverted trend with bonding; inverted trend with melting temperature. Right: "It can change abruptly during phase transformations" |

The marks on that copy are a student's (reading of the scan), not a key.

True or False statements and short questions of the final exams on these units (they give the bank its `true-statement` and `false-statement` material and the wording of its concepts):

| Unit | Concept | Form in the finals | Source |
| :--- | :--- | :--- | :--- |
| 4 | Invariant reactions of a real diagram, phases and microconstituents with the lever rule, congruent melting, maximum solubility | problem with four parts | MATERIALS_FINALEXAM_2017_ORD.pdf, question 4 (Ag-Sn); MATERIALS_FINALEXAM_COMPILATION_2013-2017.pdf: January 2014 question 1 (Al-Ni), January 2015 question 2 (Ni-Mo, statements to judge) |
| 4 | Steel on the Fe-C diagram: proeutectoid ferrite and ferrite inside pearlite at 400 °C for 100 g of alloy; effect of 8 % Ni or Mn on the eutectoid | problem | Compilation: January 2013 and June 2015 question 2 |
| 4 | Building a diagram from a list of features (two eutectics, solubility limits) | construction | Compilation: June 2014 question 3 |
| 4 | "Is the solubility of carbon higher in ferrite or austenite? Why?" | short question | Compilation: June 2015 question 4 d |
| 5 | Tensile test from a load and gauge-length table: curve, yield and tensile strength, E, resilience, ductility, engineering and true stress at fracture, change of diameter | problem (2 marks) | Compilation: January 2013 question 7; January 2014 question 2 (magnesium, 12 mm, $l_0$ = 30.00 mm) |
| 5 | Bar under load: does it yield, final length and diameter | problem (1 point) | 2017_ORD, question 5 (titanium bar) |
| 5 | Rod holding a weight: yield, E, resilience, comparison of two curves | problem (2 marks) | Compilation: June 2015 question 3 |
| 5 | Stress-strain curve from $\sigma_Y$, $\sigma_{UTS}$, $\sigma_f$ and %EL; elastic against plastic; safety factor $n$ = 2 for a tube | short questions | Compilation: January 2015 question 8 |
| 5 | Strengthening mechanisms: three names, common objective, one explained | short question | Compilation: June 2014 question 8 |
| 5 | Order materials by hardness and by elastic modulus | ordering | Compilation: June 2014 question 4 |
| 6 | Type of semiconductor for a dopant (B, In, P in Si); conductivity of doped Si with complete ionisation | short question with a number | Compilation: January 2013 question 4; January 2014 question 8 |
| 6 | Charge carriers of intrinsic, p-type and n-type semiconductors | short question | Compilation: January 2015 question 6 b |
| 6 | Resistivity of a metal against temperature, impurities, alloying, dislocations, grain boundaries; residual resistivity | short question | Compilation: June 2015 question 8 a; 2017_ORD, question 6 |
| 7 | Label the B-H loops of a hard and a soft ferromagnet; one application of each; grain size and the loop | choose the figure and explain | Compilation: June 2014 question 6 B |
| 7 | Superconductors and magnetism, $T_c$, Meissner effect | short question | Compilation: June 2015 question 8 b |

True or False statements with the official mark: "Materials with a strong atomic bonding present a low Young's modulus" (MATERIALS_FINALEXAM_2016_ORD_SOL.pdf, p. 1, question 1, statement 4); "Materials that exhibit high linear coefficient of thermal expansion have a strong atomic bonding and they are useful in applications where the components repeatedly undergo rapid heating and cooling", marked F (MATERIALS_FINALEXAM_2017_EXTRA.pdf, p. 1, question 1, statement 4).

## 3. Language patterns

- **Opening formulas (literal):** "Which one of the following statements is TRUE", "Which one of the following statements is FALSE :" (sheet B of the first-partial tests), "With an increase in temperature the ... of ...:", "... behaves as ... only:", "Microstructure of ... consists of:", "From the shown ... phase diagram, indicate which ...", "Determine the ... of some hypothetical alloy if it has ...", "Which picture describes ... ?", "Which strengthening mechanism ... is based on ...:", "What will happen with the wire:", "The linear coefficient of thermal expansion:".
- **Length:** the statement is one sentence of 8 to 25 words (the numeric one, 35 words). Options are 2 to 12 words; the four options of a question have the same grammatical shape and nearly the same length.
- **Register:** plain lecture-room English, present tense, no hedging, statements often end with a colon and are completed by the options. The papers carry small slips ("uniformely", missing articles, "Decrease" next to "Increases"); they are recorded here and **not** copied: the bank is written in correct English with the same plainness.
- **Data and units:** forces in N, diameters and lengths in mm, stresses in MPa, moduli in GPa, compositions in wt% (the problem in at%), temperatures in °C, small lengths in scientific notation ($2.5\times10^{-4}$ mm). A number and its unit are separated by a space.
- **Numerical options:** four values with the same unit and the same number of significant figures (three), in increasing order and evenly spaced; the right one is not always at an end.
- **Figures:** a diagram is "the shown ... phase diagram" and is read for one feature (a range, a temperature, a composition); pictures can be the options themselves.

## 4. Anatomy of the wrong options

| Format | What each wrong option exploits |
| :--- | :--- |
| true-statement / false-statement | Two neighbouring concepts swapped (elastic and plastic, engineering and true, intrinsic and extrinsic, soft and hard magnet); a right premise with a wrong consequence; a right trend with the wrong cause |
| complete-sentence | 2 x 2 grid of two binary choices (matrix x proeutectoid phase; trend x reason); the opposite limit (low instead of high temperature); a feature that does not matter |
| cause-effect | Inverted sign of the trend; right trend with the mechanism of the other class of material (metal and semiconductor); number of carriers confused with their mobility |
| what-happens | The neighbouring regions of the stress-strain curve; forgetting to compare with the right limit (yield instead of tensile strength); area computed with the diameter instead of the radius |
| numeric | Diameter used as radius (factor 4); mm$^2$ not converted to m$^2$ (factor $10^6$) or MPa and GPa confused; Poisson's ratio inverted or dropped; lever rule with the arms swapped; engineering instead of true value; percentage instead of fraction; $n$ and $p$ or $\mu_e$ and $\mu_h$ swapped; temperature in °C instead of K |
| diagram-reading | Half of the right range; a single composition instead of a range; the neighbouring field; the liquidus read instead of the solidus; wt% of the other component |
| choose-figure | The other members of the same family (dia, para, ferro, antiferro, ferri; soft and hard loop; conductor, semiconductor and insulator bands; ductile and brittle curve) |
| identify | The other members of the list (four strengthening mechanisms, four hardness tests, five invariant reactions, the types of magnetism) |
| ordering | One pair swapped; the fully reversed order; the order of a neighbouring property (hardness order given for conductivity) |

No absurd options: each wrong option is the result of one nameable mistake, and the explanation of the question names it.

## 5. Frequency per unit and quota of the bank

Real paper: Unit 5 four questions (1, 2, 3, 8), Units 4, 6 and 7 two each, and the 5-point problem on Unit 4. The finals add problems on Units 4, 5 and 6 and short questions on Unit 7. The bank keeps Unit 5 as the largest unit for the test, gives Unit 4 more than its two test questions because it also carries Part II, and never goes below 100 per unit. Units 6 and 7 were raised to 150 after the audit of the first 100 (see below).

| Unit | Share of the real test | Questions in the bank | Blocks of ten | Block ids |
| :--- | :--- | :--- | :--- | :--- |
| 4 Phase diagrams | 2 of 10 (+ the problem) | 150 | 15 | B01 to B15 |
| 5 Mechanical properties | 4 of 10 | 170 | 17 | B16 to B32 |
| 6 Electrical properties | 2 of 10 | 150 | 15 | B33 to B42, B53 to B57 |
| 7 Magnetic and thermal properties | 2 of 10 | 150 | 15 | B43 to B52, B58 to B62 |
| Total | 10 | 620 | 62 | |

The simulator offers six practice scopes (`modes` of `exam-blueprint-midterm-2.json`): **Mixed (real paper)** draws 2 + 4 + 2 + 2 and the Part II problem; **Mixed (focus on Units 6 and 7)** draws 1 + 2 + 4 + 3 (Unit 4 is already examined by the Part II problem, Unit 5 keeps two questions, Units 6 and 7 carry the extra weight expected this course) and the problem; **Unit 4 only** to **Unit 7 only** draw the ten test questions of one unit from ten different blocks, graded out of 5 with the same rule, with a 20-minute clock (an assumption). The validator checks that every mode adds up to ten and that the bank holds enough questions and blocks for it.

Target mix of formats over the whole bank (the real paper has 1 true-statement, 3 complete-sentence, 1 cause-effect, 1 what-happens, 1 identify, 1 diagram-reading, 1 numeric, 1 choose-figure): true-statement and false-statement 20 %, complete-sentence 20 %, cause-effect 12 %, numeric 15 %, identify 9 %, what-happens 8 %, diagram-reading 8 % (most of it in Unit 4), choose-figure 4 %, ordering 4 %. Each unit may move these by a few points to fit its content.

### Quota per concept group

At most four questions share one `concept_id`, and those that do differ in format or in what they ask (definition, cause, effect, calculation, figure reading, comparison, classification, application). Each group below is split into as many `concept_id`s as it needs.

**Unit 4 (150)**

| Concept group | Slides | Questions |
| :--- | :--- | :--- |
| Component, phase, microconstituent, solubility limit | Session 7, 2-3 | 8 |
| Unary diagrams (water, iron) and allotropy | Session 7, 5-6 | 6 |
| Isomorphous systems, cooling curves, complete solubility | Session 7, 8-11 | 12 |
| Gibbs phase rule | Session 7, 13 | 10 |
| Tie line and lever rule | Session 7, 15-21 | 14 |
| Non-equilibrium solidification and coring | Session 7, 23-24 | 6 |
| Eutectic systems: reaction, reading the Pb-Sn diagram, which alloys undergo it | Session 7, 26-29 | 16 |
| Hypoeutectic and hypereutectic alloys: microconstituents and their amounts | Session 7, 30-32 | 16 |
| Solvus and solid-state precipitation | Session 8, 2-4 | 6 |
| Invariant reactions: eutectoid, peritectic, peritectoid, monotectic | Session 8, 6-12 | 14 |
| Intermetallic compounds, congruent and incongruent melting | Session 8, 14-17 | 8 |
| Fe-Fe3C diagram: phases and invariant reactions | Session 9, 2-11 | 14 |
| Steels: eutectoid, hypoeutectoid and hypereutectoid microstructures and amounts | Session 9, 12-20 | 14 |
| Pearlite and cooling rate, alloying elements | Session 9, 21-23 | 4 |
| Ceramic and ternary diagrams | Session 10 | 2 |

**Unit 5 (170)**

| Concept group | Slides | Questions |
| :--- | :--- | :--- |
| Stress, strain, the tension test and its curve | Session 11, 2-9 | 12 |
| Elastic and plastic deformation at the atomic level | Session 11, 10, 21 | 10 |
| Hooke's law, Young's modulus, bonding, non-linear elasticity | Session 11, 12-18 | 16 |
| Poisson's ratio and shear modulus | Session 11, 7, 19 | 14 |
| Other tests: compression, impact, bending, shear, torsion | Session 11, 5-7 | 8 |
| Slip, dislocations and slip systems | Session 11, 23-25; Session 12, 2-3 | 10 |
| Yield strength, 0.2 % offset, working stress and safety factor | Session 11, 28-29 | 14 |
| Tensile strength, necking, fracture; what a given load does | Session 11, 30-31 | 16 |
| Ductility: percent elongation and reduction in area | Session 11, 32-33 | 10 |
| Toughness and modulus of resilience | Session 11, 34-35 | 10 |
| True stress and true strain | Session 11, 37-38 | 12 |
| Strengthening principle, strain hardening and cold work | Session 12, 4-7 | 12 |
| Solid solution, grain size and precipitation strengthening | Session 12, 8-13 | 14 |
| Hardness tests and hardness against tensile strength | Session 12, 15-30 | 12 |

**Unit 6 (100)**

| Concept group | Slides | Questions |
| :--- | :--- | :--- |
| Energy bands; conductors, semiconductors and insulators | Session 13, 2-8 | 12 |
| Ohm's law, conductivity, resistivity, drift velocity and mobility | Session 13, 10-13 | 14 |
| Matthiessen's rule: temperature, impurities, deformation | Session 13, 14-19 | 14 |
| Non-metallic conductors | Session 13, 20-23 | 4 |
| Intrinsic semiconductors: carriers, gap, temperature | Session 13, 25-34 | 16 |
| Extrinsic semiconductors: n and p type, donor and acceptor levels, majority carriers | Session 13, 35-42 | 16 |
| Extrinsic semiconductors and temperature | Session 13, 43-44 | 8 |
| Devices: p-n junction, photoconductivity, LED, thermistor | Session 13, 45-49 | 6 |
| Dielectrics, ferroelectrics and piezoelectrics | Session 13, 51-60 | 10 |
| Added in B53-B57: inverse resistivity problems, wire strategies, ionic against metallic conduction, intrinsic ratios and gaps, dopant energy tables, mobility against doping, extrinsic regions, dielectric calculations | Session 13, 14-23, 25-34, 35-49, 51-60 | 50 |

**Unit 7 (100)**

| Concept group | Slides | Questions |
| :--- | :--- | :--- |
| Origin of magnetism; H, B, M, permeability and susceptibility | Session 15, 3-4 | 10 |
| Types of magnetism (with the dipole pictures) | Session 15, 5-13 | 18 |
| Domains, Bloch walls and the magnetisation curve | Session 15, 14-16 | 8 |
| Hysteresis: soft and hard magnets, applications, what controls the loop | Session 15, 17-22 | 14 |
| Curie and Néel temperatures | Session 15, 23-24 | 6 |
| Superconductivity | Session 15, 25-32 | 6 |
| Heat capacity | Session 15, 34-35 | 8 |
| Thermal expansion: coefficient, bonding, allotropy, bimetals | Session 15, 36-39 | 12 |
| Thermal conductivity | Session 15, 40-44 | 10 |
| Thermal stresses and thermal shock | Session 15, 45-48 | 8 |
| Added in B58-B62: moments and fields from the 3d table, tables of soft and hard magnets, loop factors, Curie and Néel conversions, superconductor envelope and Josephson effect, heat capacity, expansion, thermal conduction and thermocouple, stress and shock | Session 15, 3-48 | 50 |

## 6. Problem types of Part II

### 6.1 Structure for 2026-27

Part II is **two problems** this year: a longer problem on phase diagrams and a shorter problem on Unit 5. The 2019 and 2018 papers had one 5-point problem on a binary diagram; the finals, re-read for this section, always pair the two topics with a 2:1 weight:

| Final | Phase-diagram problem | Unit 5 problem | Source |
| :--- | :--- | :--- | :--- |
| January 2017 (ordinary) | Q4, 2 points, Ag-Sn in wt%: invariant reactions with name, temperature and compositions; phases and amounts at 480 - ΔT °C for Ag-30 Sn; microconstituents and fractions at 221 - ΔT °C for Ag-60 Sn; congruent melting and maximum solubility (4 × 0.5 p) | Q5, 1 point: titanium bar, 10 mm, 204 mm, σy 345 MPa, E 110 GPa, ν 0.30: does it yield under 22 kN; length and diameter under the load (2 × 0.5 p) | MATERIALS_FINALEXAM_2017_ORD.pdf, pp. 2-4 |
| 2017 (extraordinary) | Q4, 2 points, Fe-C: 5 kg bar of 0.55 % C, kg of proeutectoid ferrite, eutectoid ferrite and cementite at 727 - ΔT; phases and microconstituents at 600 °C; carbon content from 64.7 % austenite and 35.3 % cementite at 800 °C; effect of alloying on the eutectoid point (4 × 0.5 p) | Q5, 1 point: brass specimen 10 mm × 120 mm: length under 11 750 N; length after unloading from 23 500 N with a strain of 2.2·10⁻² before unloading (elastic recovery) | MATERIALS_FINALEXAM_2017_EXTRA.pdf, pp. 2-4 |
| 2016 (ordinary) | Q4, 2 points, Ni-Ti in at%: invariant reactions at 765, 984 and 1118 °C; microstructure sketch at 765 - ΔT for 8 at% Ni; microconstituents at 1304 - ΔT for 80 at% Ni; congruent melting and maximum solubility (4 × 0.5 p) | Q5, 1 point: material selection for a 120 mm rod of 14 mm carrying 30 kN without yielding, diameter loss under 10 µm and mass under 100 g, from a table of four alloys (E, σy, ν, ρ) | MATERIALS_FINALEXAM_2016_ORD_SOL.pdf, pp. 2-4 |
| 2016 (extraordinary) | Q4, 1 point, Fe-Fe3C: kg of proeutectoid ferrite, eutectoid ferrite and cementite for a 5 kg bar of 0.55 % C; carbon content from 63.3 % proeutectoid ferrite | Q6, 1 point: two square bars of materials A and B (E, ν): back-calculate dimensions and force from lateral and axial changes | MATERIALS_FINALEXAM_2016_EXTRA_SOL.pdf, pp. 2-4 |
| June 2015 | Q2, 2 marks, Fe-C steel, 100 g at 400 °C, effect of 8 % Mn | Q3, 2 marks: rod of 3 m and 20 mm under 65 kN with Δd = 0.014 mm and ν = 0.36: loaded length; yield from a hanging mass of 26 608 kg, safety factor 2; E and resilience; two curves | Compilation 2013-2017, pp. 34-36 |
| January 2015 | Q2, 2 marks, Ni-Mo: judge statements on the reactions and microconstituents | Q8, 1 mark: draw a curve from σy, σUTS, σf and %EL; elastic against plastic; tube with safety factor 2 under 12 000 N | Compilation, pp. 27-31 |
| January 2014 | Q1, 2 marks, Al-Ni in at%: reactions at 639.9, 700, 1133 and 1385 °C; sketch and amounts at 638 °C for 10 at% Ni; congruent melting | Q2, 2 marks: magnesium specimen 12 mm, l0 = 30.00 mm, load-length table: curve, σy, UTS, E, resilience, %EL, %RA, engineering and true fracture stress, true stress and strain at 176.8 MPa, Δd under 10 kN with ν = 0.29 | Compilation, pp. 4-14 |
| 2013 and 2012 | Ag-Sn (2.5 p) and Al-Pt (2 p) diagrams; June 2014 Q3 builds a diagram from a list of features | Magnesium table (2 marks), brass table of rectangular section (1.5 p, key E 40 GPa, σy 150 MPa, R 234 MPa, Ur 0.28 MPa) | MATERIALS_FINALEXAM_2012_ORD.pdf, pp. 1-2; 2012_EXTRA, pp. 1-2; compilation p. 21 |

Since 2016 the phase-diagram problem is worth twice the Unit 5 problem (2 against 1 point). Part II keeps its 5 points, so the bank uses **3.0 points for the phase-diagram problem and 2.0 for the Unit 5 problem**. This split is an assumption until the paper confirms it (`exam-blueprint-midterm-2.json`, `provenance`).

### 6.2 The long problem: phase diagrams (3.0 points)

Four or five parts (e.g. 4 × 0.75). The recurring parts, in the order of the papers: (a) every invariant reaction with its name, temperature and the composition of the three phases; (b) phases, compositions and amounts of one alloy just above or below an invariant temperature (lever rule); (c) microconstituents and their amounts, or a sketch of the microstructure at T ± ΔT; (d) congruent or incongruent melting of the compounds and the maximum solubility with its temperature. Steel variants replace (a) to (d) with kg of proeutectoid and eutectoid phases for a given bar, phases at a second temperature, the carbon content worked backwards from a microstructure, and the effect of an alloying element on the eutectoid point. Compositions in wt% or at%, as printed on the diagram.

| Type (archetype) | Real model | Problems |
| :--- | :--- | :--- |
| `phase-diagram-invariant` Binary diagram with intermetallic compounds | 2019 (Ni-Nb), 2017 (Ag-Sn), 2016 (Ni-Ti), 2014 (Al-Ni), 2015 (Ni-Mo) | P01 to P04 |
| `eutectic-lever-rule` Eutectic system with terminal solid solutions | Question 7 of the test; June 2014 Q3 (building a diagram); sheets of Unit 4 | P05 to P08 |
| `fe-c-steels` Fe-Fe3C diagram and steels | 2017 extraordinary, 2016 extraordinary, January 2013, June 2015 | P09 to P12 |

### 6.3 The short problem: Unit 5 (2.0 points)

Two or three parts (e.g. 1.0 + 1.0), about 15 minutes. The papers ask one of two things:

| Type (archetype) | Real model | Typical parts | Problems |
| :--- | :--- | :--- | :--- |
| `tensile-test` Tensile test from data or a curve | January 2014 and 2013 (magnesium table), 2012 (brass table), January 2015 Q8 a | engineering stress and strain of chosen rows; E; 0.2 % offset yield; tensile strength; %EL and %RA; resilience; true stress and strain | P13 to P16 |
| `loaded-bar` Bar or rod under load | 2017 ordinary (titanium bar), 2017 extraordinary (brass, unloading), 2016 ordinary (material selection), 2016 extraordinary (two bars), June 2015 (rod with a hanging mass), January 2015 Q8 c (tube with a safety factor) | does it yield; elongation and change of diameter with Poisson's ratio; minimum size or material choice with a safety factor and a limit on the deformation; length after unloading from the plastic range | P17 to P20 |

Units 6 and 7 appear in the finals only as short questions, so they have test questions and no Part II type this year.

## 7. Rules for the bank notes

- One block of ten questions is one note, `Quiz - Bank Bnn - Unit N <theme>.md`; one problem is one note, `Problem - Bank Pnn - <title>.md`. Format and checks: [[Tool - build_materials_bank]].
- Every item is labelled "Practice item, not an official exercise". No official question is copied: the data, the angle or the concept changes.
- Physical data come from the slides and the official sheets and are cited in `### Source`. Anything outside the course is left out, or marked **extension** with its definition.
- Known errata of the web pages of these units (`sources/cuatrimestre-1/02-aerospace-materials-1/Auditoría Temas 4 A 7.md`) are not carried into the questions.
- Every number is recomputed by `tools/materials_bank/verify_mt2.py`.

## 8. Answer-form audit (Units 6 and 7)

An audit of the first 200 questions of Units 6 and 7 found tells in the form of the answer and rewrote 24 questions (same id and right letter): a wrong option carrying an absolute ("only", "depends only on X", "does not change, as ... only") that no right option ever carries (33 cases, 10 of them the template "does not change, as it depends only on X"), a right option clearly the longest (5), and absurd options (3). Rules that follow, enforced by review and by the blind solve: no absolute only in wrong options; the right option is not systematically the longest; every wrong option is one nameable mistake; at most two definition questions per block; at least three calculations and two table or graph readings per block.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]] · [[Aerospace Materials I MOC]]
