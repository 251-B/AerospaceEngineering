---
materia: Aerospace Materials I
tema: "Unit 4: the Fe-Fe3C diagram, its phases and invariant reactions"
bank_id: B13
title: "The Fe-Fe3C diagram"
category: mt2_test_block
unit: 4
concepts:
  - u4-fec-diagram-reading
  - u4-fec-invariants
  - u4-fec-phases
  - u4-fec-carbon-solubility
  - u4-fec-ranges
difficulty: 2
origen: "Includes official exam statements from Q2(a) of MATERIALS_FINALEXAM_2015_EXTRA.pdf (p. 3); other questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf. Data from Session 9 Slides 4-12 (eutectoid 727 °C: 0.022, 0.76, 6.67 wt% C; eutectic 1147 °C: 2.14, 4.30 wt% C; peritectic 1493 °C)."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-4
---

# Bank B13 — The Fe-Fe3C diagram

> [!info] Includes official exam questions
> Ten test questions in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong); Q13.5 integrates statements from `MATERIALS_FINALEXAM_2015_EXTRA.pdf` (Q2a). Content: Session 9, Slides 4-12.

## Q13.1 Phases at point 3 of Fe-Fe3C

- id: B13-Q1
- concept_id: u4-fec-diagram-reading
- format: diagram-reading
- asks: figure-reading

An Fe-C alloy sits at the point numbered 3 of the iron-carbon diagram below. Which two phases does it contain?

![[attachments/MAT-MT2/u4-fec-points.svg]]

a) γ + Fe₃C
b) α + Fe₃C
c) γ only
d) γ + L

### Answer

a

### Explanation

Point 3 (1.8 wt% C, 850 °C) lies between 727 and 1147 °C and to the right of the $A_{cm}$ line: the field austenite + cementite (Session 9, Slides 4 and 9).

- b) α + Fe₃C lies below 727 °C; point 3 is above the eutectoid line.
- c) Single-phase γ lies to the left of $A_{cm}$; at 850 °C that line is near 1.2 wt% C, so 1.8 wt% C has crossed it.
- d) γ + L lies above 1147 °C; point 3 is below the eutectic line.

### Source

Session 9, Slides 4, 9 and 11.

## Q13.2 Liquid on the Fe-Fe3C diagram

- id: B13-Q2
- concept_id: u4-fec-diagram-reading
- format: diagram-reading
- asks: classification

Liquid is still present in the alloy marked by which number in the Fe-Fe₃C diagram below?

![[attachments/MAT-MT2/u4-fec-points.svg]]

a) 1
b) 2
c) 3
d) 4

### Answer

d

### Explanation

Point 4 (2.8 wt% C, 1220 °C) lies above the eutectic line (1147 °C) and below the liquidus, in the field γ + L (Session 9, Slide 4).

- a) Point 1 (0.4 wt% C, 900 °C) is single-phase austenite, fully solid.
- b) Point 2 (1.0 wt% C, 600 °C) lies below 727 °C, in α + Fe₃C.
- c) Point 3 lies in γ + Fe₃C, below 1147 °C, where no liquid exists.

### Source

Session 9, Slides 4 and 9.

## Q13.3 Reaction at 1147 °C

- id: B13-Q3
- concept_id: u4-fec-invariants
- format: identify
- asks: classification

Which invariant reaction of the Fe-Fe₃C diagram takes place at 1147 °C on cooling:

a) Eutectoid
b) Eutectic
c) Peritectic
d) Monotectic

### Answer

b

### Explanation

Session 9, Slide 10: at 1147 °C, $L\,(4.30) \rightarrow \gamma\,(2.14) + \text{Fe}_3\text{C}\,(6.67)$, a liquid giving two solids: the eutectic, whose product is ledeburite.

- a) The eutectoid of Fe-C is at 727 °C ($\gamma \rightarrow \alpha + \text{Fe}_3\text{C}$).
- c) The peritectic is at 1493 °C ($\delta + L \rightarrow \gamma$).
- d) The Fe-Fe₃C diagram has no monotectic.

### Source

Session 9, Slide 10.

## Q13.4 A wrong claim about the Fe-C reactions

- id: B13-Q4
- concept_id: u4-fec-invariants
- format: false-statement
- asks: definition

Which one of the following statements about the invariant reactions of the Fe-Fe₃C diagram is FALSE:

a) The eutectoid at 727 °C gives pearlite
b) The eutectic at 1147 °C gives ledeburite
c) The peritectic at 1493 °C gives austenite
d) The eutectoid starts from a liquid of 0.76 wt% C

### Answer

d

### Explanation

Statement d) is false: the eutectoid starts from austenite, a solid, of 0.76 wt% C: $\gamma\,(0.76) \rightarrow \alpha\,(0.022) + \text{Fe}_3\text{C}\,(6.67)$ (Session 9, Slide 10).

- a) True: the product of the eutectoid is pearlite.
- b) True: the product of the eutectic is ledeburite.
- c) True: $\delta\,(0.09) + L\,(0.53) \rightarrow \gamma\,(0.16)$ gives austenite.

### Source

Session 9, Slide 10.

## Q13.5 Phases and microconstituents in Fe-Fe3C alloys

- id: B13-Q5
- concept_id: u4-fec-ranges
- format: topic-false
- asks: classification
- origin: official-exam

Referring to the Fe-Fe₃C metastable phase diagram, which statement is FALSE:

a) The maximum solubility of carbon in α-ferrite at 727 °C is 0.022 wt%
b) The microconstituents of an Fe-3 wt% C alloy at 1000 °C are primary austenite and cementite
c) An Fe-3 wt% C alloy is a hypoeutectic cast iron because its carbon content lies between 2.14 and 4.30 wt%
d) At 1147 °C a eutectic liquid of 4.30 wt% C transforms into austenite and cementite (ledeburite)

### Answer

b

### Explanation

Statement b) is false (from `MATERIALS_FINALEXAM_2015_EXTRA.pdf`, Q2a): at 1000 °C an Fe-3 wt% C alloy lies between 727 and 1147 °C in the $\gamma + \text{Fe}_3\text{C}$ phase field, so its **phases** are austenite and cementite, whereas its **microconstituents** are primary austenite ($\gamma_p$) and ledeburite ($\gamma + \text{Fe}_3\text{C}$ eutectic).

- a) True: 0.022 wt% C is the maximum carbon solubility of α-ferrite at the eutectoid temperature, 727 °C (2015 EXTRA Q2a; Session 9, Slide 5).
- c) True: alloys between 2.14 and 4.30 wt% C are hypoeutectic cast irons (Session 9, Slide 4).
- d) True: the eutectic reaction at 1147 °C is $L\,(4.30) \rightarrow \gamma\,(2.14) + \text{Fe}_3\text{C}\,(6.67)$, producing ledeburite (Session 9, Slide 10).

### Source

MATERIALS_FINALEXAM_2015_EXTRA.pdf, p. 3 (Q2a); Session 9, Slides 4-5 and 10-11.

## Q13.6 A eutectoid steel through 727 °C

- id: B13-Q6
- concept_id: u4-fec-invariants
- format: what-happens
- asks: effect

A steel of 0.76 wt% C, all austenite, is cooled slowly through 727 °C. What will happen to it:

a) All the austenite turns into pearlite at 727 °C
b) Proeutectoid ferrite forms before the pearlite
c) Proeutectoid cementite forms before the pearlite
d) The austenite stays unchanged down to room temperature

### Answer

a

### Explanation

0.76 wt% C is the eutectoid composition: the austenite reaches the eutectoid point only at 727 °C and transforms entirely into one microconstituent, pearlite (α + Fe₃C lamellae) (Session 9, Slides 10 and 12).

- b) Proeutectoid ferrite forms only in hypoeutectoid steels (below 0.76 wt% C), which cross the $A_3$ line first.
- c) Proeutectoid cementite forms only in hypereutectoid steels (above 0.76 wt% C), which cross the $A_{cm}$ line first.
- d) Below 727 °C austenite is not stable in the Fe-Fe₃C diagram; it must transform.

### Source

Session 9, Slides 10 and 12-13.

## Q13.7 A wrong claim about the phases of iron-carbon

- id: B13-Q7
- concept_id: u4-fec-phases
- format: false-statement
- asks: classification

Which one of the following statements about the phases of the Fe-Fe₃C diagram is FALSE:

a) α-ferrite is BCC and soft
b) Austenite is FCC and not magnetic
c) Austenite is stable at room temperature in slowly cooled steels
d) δ-ferrite is BCC, like α-ferrite

### Answer

c

### Explanation

Statement c) is false: in the Fe-Fe₃C diagram austenite exists only above 727 °C; below it every alloy is α + Fe₃C (Session 9, Slides 4 and 9).

- a) True: α-ferrite is an interstitial solid solution of C in BCC iron, a soft phase (Slide 5).
- b) True: austenite is FCC and not magnetic (Slide 6).
- d) True: δ-ferrite is BCC, with the same properties as α-ferrite but at higher temperatures (Slide 7).

### Source

Session 9, Slides 4-9.

## Q13.8 Single phase at point 1

- id: B13-Q8
- concept_id: u4-fec-phases
- format: diagram-reading
- asks: figure-reading

From the shown Fe-Fe₃C phase diagram, indicate the phase present at point 1:

![[attachments/MAT-MT2/u4-fec-points.svg]]

a) Austenite (γ)
b) α-ferrite
c) Cementite
d) δ-ferrite

### Answer

a

### Explanation

Point 1 (0.4 wt% C, 900 °C) lies above the $A_3$ line (about 775 °C at 0.4 wt% C) and below the solidus, inside the γ field: single-phase austenite (Session 9, Slides 4 and 6).

- b) α-ferrite is stable at that composition only below the $A_3$ line, near 727 °C and below.
- c) Cementite is the vertical line at 6.67 wt% C; it appears with austenite only to the right of $A_{cm}$.
- d) δ-ferrite exists only above about 1394 °C, at the top left of the diagram.

### Source

Session 9, Slides 4-7.

## Q13.9 Carbon in alpha-ferrite

- id: B13-Q9
- concept_id: u4-fec-carbon-solubility
- format: true-statement
- asks: definition

Which one of the following statements about the carbon solubility of α-ferrite is TRUE:

a) It is largest at room temperature
b) It reaches 2.14 wt% C at 1147 °C
c) Its maximum, 0.022 wt% C, occurs at 727 °C
d) It is 0.76 wt% C at 727 °C

### Answer

c

### Explanation

Session 9, Slide 5: α-ferrite has a low carbon content, with a maximum solubility of 0.022 wt% C at 727 °C.

- a) The solubility of C in ferrite falls on cooling below 727 °C (the boundary moves towards 0 % C), so it is not largest at room temperature.
- b) 2.14 wt% C at 1147 °C is the maximum of austenite, the neighbouring phase.
- d) 0.76 wt% C is the composition of the eutectoid austenite, not of ferrite.

### Source

Session 9, Slides 4-6.

## Q13.10 Classes of Fe-C alloys by carbon content

- id: B13-Q10
- concept_id: u4-fec-ranges
- format: ordering
- asks: comparison

Order the classes of Fe-C alloys by increasing carbon content:

a) Hypoeutectoid, hypoeutectic, hypereutectoid, hypereutectic
b) Hypoeutectoid, hypereutectoid, hypoeutectic, hypereutectic
c) Hypereutectic, hypoeutectic, hypereutectoid, hypoeutectoid
d) Hypereutectoid, hypoeutectoid, hypoeutectic, hypereutectic

### Answer

b

### Explanation

Session 9, Slide 4: hypoeutectoid steels up to 0.76 wt% C, hypereutectoid steels from 0.76 to 2.14, hypoeutectic cast irons from 2.14 to 4.30 and hypereutectic cast irons from 4.30 to 6.67 wt% C.

- a) The middle pair is swapped: hypereutectoid steels (below 2.14 wt% C) come before hypoeutectic cast irons.
- c) This is the fully reversed order, by decreasing carbon content.
- d) The first pair is swapped: hypoeutectoid steels have less carbon than hypereutectoid ones.

### Source

Session 9, Slide 4.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
