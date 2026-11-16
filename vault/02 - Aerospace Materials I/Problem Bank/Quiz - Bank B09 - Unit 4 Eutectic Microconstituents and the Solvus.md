---
materia: Aerospace Materials I
tema: "Unit 4: amounts of microconstituents in eutectic systems and solid-state precipitation"
bank_id: B09
title: "Eutectic microconstituents and the solvus"
category: mt2_test_block
unit: 4
concepts:
  - u4-primary-fraction
  - u4-eutectic-fraction
  - u4-total-phase-fraction
  - u4-eutectic-alpha-split
  - u4-hypo-cooling-sequence
  - u4-eutectic-inverse
  - u4-solvus-precipitation
  - u4-precipitation-alloys
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 7 Slides 26-32 (Pb-Sn: 183 °C, 18.3, 61.9 and 97.8 wt% Sn) and Session 8 Slides 2-4."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-4
---

# Bank B09 — Eutectic microconstituents and the solvus

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 7, Slides 26-32; Session 8, Slides 2-4.

## Q09.1 Primary beta read on the A-B diagram

- id: B09-Q1
- concept_id: u4-primary-fraction
- format: diagram-reading
- asks: calculation
- check: abs((80-60)/(90-60) - 0.667) < 0.001

From the shown A-B phase diagram, indicate the mass percentage of primary β in the 80 wt% B alloy just below 450 °C:

![[attachments/MAT-MT2/u4-eut-ab.svg]]

a) 66.7 %
b) 33.3 %
c) 86.7 %
d) 26.7 %

### Answer

a

### Explanation

The alloy is hypereutectic (between 60 and 90 wt% B). The short tie line runs from the eutectic (60) to β (90 wt% B) (Session 7, Slides 31-32): $W_{\beta'} = (80 - 60)/(90 - 60) = 20/30 = 0.667$.

- b) $(90 - 80)/30 = 0.333$ is the eutectic fraction: arms swapped.
- c) $(80 - 15)/(90 - 15) = 0.867$ is the total β (primary plus eutectic), a phase fraction on the whole tie line.
- d) $20/75 = 0.267$ divides the right arm by the whole α-β tie line instead of the short one.

### Source

Session 7, Slides 31-32.

## Q09.2 A wrong claim about primary alpha

- id: B09-Q2
- concept_id: u4-primary-fraction
- format: false-statement
- asks: comparison
- check: (61.9-50)/(61.9-18.3) < 0.5 and (61.9-40)/(61.9-18.3) > (61.9-50)/(61.9-18.3)

Which one of the following statements about Pb-Sn alloys just below 183 °C is FALSE:

a) Pb-40 wt% Sn has more primary α than Pb-50 wt% Sn
b) Pb-61.9 wt% Sn has no primary phase
c) Pb-70 wt% Sn has primary β
d) Pb-50 wt% Sn has more primary α than eutectic

### Answer

d

### Explanation

Statement d) is false: for Pb-50 wt% Sn, $W_{\alpha'} = (61.9 - 50)/(61.9 - 18.3) = 0.273$ and $W_e = 0.727$ (Session 7, Slide 32), so it has more eutectic than primary α.

- a) True: $(61.9 - 40)/43.6 = 0.502$ against 0.273; the farther from the eutectic composition, the more primary α.
- b) True: the eutectic alloy is 100 % eutectic (Session 7, Slide 28).
- c) True: 70 wt% Sn lies between 61.9 and 97.8 wt% Sn, the hypereutectic range, whose primary phase is β (Slide 31).

### Source

Session 7, Slides 28 and 30-32.

## Q09.3 What the eutectic fraction equals

- id: B09-Q3
- concept_id: u4-eutectic-fraction
- format: identify
- asks: definition

Which quantity equals the fraction of eutectic microconstituent just below the eutectic temperature:

a) The total fraction of β
b) The fraction of liquid just above the eutectic temperature
c) The fraction of primary α
d) The fraction of α inside the eutectic

### Answer

b

### Explanation

Session 7, Slide 32: $W_e = W_L$; all the liquid present just above the eutectic temperature has the eutectic composition and becomes eutectic.

- a) In a hypoeutectic alloy the β is only part of the eutectic (about 55 % of it in Pb-Sn), so it is smaller than $W_e$.
- c) The primary α is the other microconstituent: $W_{\alpha'} = 1 - W_e$.
- d) The α inside the eutectic is only one of its two phases, $W_\alpha - W_{\alpha'}$.

### Source

Session 7, Slide 32.

## Q09.4 Total and primary alpha

- id: B09-Q4
- concept_id: u4-total-phase-fraction
- format: true-statement
- asks: comparison

Which one of the following statements about a Pb-40 wt% Sn alloy just below 183 °C is TRUE:

a) Its total α equals its primary α
b) Part of its β is primary
c) Its total α is larger than its primary α
d) Its total β equals its eutectic fraction

### Answer

c

### Explanation

Total α counts the primary α and the α inside the eutectic (Session 7, Slide 32): $W_\alpha = (97.8 - 40)/79.5 = 0.727$, larger than $W_{\alpha'} = (61.9 - 40)/43.6 = 0.502$.

- a) This forgets the α layers of the eutectic, which are part of the total α.
- b) A hypoeutectic alloy has no primary β; all its β is inside the eutectic.
- d) The eutectic also contains α; the β is only part of it ($0.273$ against $0.498$).

### Source

Session 7, Slide 32.

## Q09.5 Alpha inside the eutectic of Pb-40 Sn

- id: B09-Q5
- concept_id: u4-eutectic-alpha-split
- format: numeric
- asks: calculation
- calc: ((97.8-40)/(97.8-18.3) - (61.9-40)/(61.9-18.3))*100

Just below 183 °C, part of the α of a Pb-40 wt% Sn alloy sits inside the eutectic layers. Determine that part as a percentage of the whole alloy mass:

a) 22.5 %
b) 27.3 %
c) 49.8 %
d) 72.7 %

### Answer

a

### Explanation

Total α minus primary α (Session 7, Slide 32): $W_\alpha = \dfrac{97.8 - 40}{79.5} = 0.727$, $W_{\alpha'} = \dfrac{61.9 - 40}{43.6} = 0.502$, so $W_{\alpha,e} = 0.727 - 0.502 = 0.225$. Check: $W_e \times 0.452 = 0.498 \times 0.452 = 0.225$.

- b) $(40 - 18.3)/79.5 = 0.273$ is the total β, the other phase of the eutectic.
- c) $(40 - 18.3)/43.6 = 0.498$ is the whole eutectic, both of its phases together.
- d) 0.727 is the total α, primary α included.

### Source

Session 7, Slide 32.

## Q09.6 Definition of eutectic alpha

- id: B09-Q6
- concept_id: u4-eutectic-alpha-split
- format: complete-sentence
- asks: definition

In a hypoeutectic alloy, the fraction of α that belongs to the eutectic equals:

a) The primary α minus the total α
b) The total α minus the β
c) The fraction of eutectic itself
d) The total α minus the primary α

### Answer

d

### Explanation

Session 7, Slide 32 separates the total α, $W_\alpha$ (whole tie line), from the primary α, $W_{\alpha'}$ (short tie line); the difference is the α in the eutectic, $W_{\alpha,e} = W_\alpha - W_{\alpha'}$.

- a) The subtraction is reversed and gives a negative number.
- b) Subtracting β mixes two different phases and has no meaning as a mass balance.
- c) The eutectic contains α and β; its α is only a part of it.

### Source

Session 7, Slide 32.

## Q09.7 First solid from point 4

- id: B09-Q7
- concept_id: u4-hypo-cooling-sequence
- format: diagram-reading
- asks: figure-reading

From the shown Pb-Sn phase diagram, indicate the first solid that forms when the alloy at point 4 is cooled slowly:

![[attachments/MAT-MT2/u4-pbsn-points.svg]]

a) α
b) β
c) The α + β eutectic
d) Pure Pb

### Answer

a

### Explanation

Point 4 (50 wt% Sn, 280 °C) is liquid; the alloy line meets the Pb-rich liquidus, between 18.3 and 61.9 wt% Sn, so the alloy is hypoeutectic and its first solid is primary α (Session 7, Slide 30).

- b) β forms first only in hypereutectic alloys, to the right of 61.9 wt% Sn.
- c) The eutectic forms only at 183 °C, after primary α has grown; only a 61.9 wt% Sn alloy starts with it.
- d) The first solid is the solid solution α, whose composition is read on the solidus, not pure Pb.

### Source

Session 7, Slides 26 and 30.

## Q09.8 Composition from the eutectic fraction

- id: B09-Q8
- concept_id: u4-eutectic-inverse
- format: numeric
- asks: calculation
- calc: 18.3+0.40*(61.9-18.3)

A hypoeutectic Pb-Sn alloy is 40 % eutectic microconstituent just below 183 °C. Determine its Sn content:

a) 24.8 wt% Sn
b) 35.7 wt% Sn
c) 44.5 wt% Sn
d) 50.1 wt% Sn

### Answer

b

### Explanation

$W_e = (C_0 - 18.3)/(61.9 - 18.3)$ (Session 7, Slide 32), solved for $C_0$: $C_0 = 18.3 + 0.40 \times 43.6 = 35.7$ wt% Sn.

- a) $0.40 \times 61.9 = 24.8$ forgets the α end of the tie line and scales the eutectic composition alone.
- c) $61.9 - 0.40 \times 43.6 = 44.5$ treats 40 % as the primary α: arms swapped.
- d) $18.3 + 0.40 \times 79.5 = 50.1$ uses the whole α-β tie line, which gives phases, not the eutectic microconstituent.

### Source

Session 7, Slide 32.

## Q09.9 Cooling below the solvus

- id: B09-Q9
- concept_id: u4-solvus-precipitation
- format: cause-effect
- asks: effect

With a decrease in temperature below the solvus (about 172 °C), a single-phase Pb-16 wt% Sn alloy:

a) Dissolves again its β particles
b) Melts partially at the grain boundaries
c) Precipitates β particles that grow on further cooling
d) Forms the α + β eutectic

### Answer

c

### Explanation

Session 8, Slides 3-4: when an alloy crosses the solvus on cooling, the solid solubility of α is exceeded and small particles of β form; they grow as the temperature decreases (Pb-16 wt% Sn: only α at 192 °C, α + β at 121 °C).

- a) Inverted: β dissolves on heating above the solvus, not on cooling below it.
- b) No liquid exists in Pb-Sn below 183 °C; the alloy is fully solid.
- d) The eutectic forms from liquid at 183 °C; this alloy never meets the eutectic line, it changes by solid-state precipitation.

### Source

Session 8, Slides 3-4.

## Q09.10 Alloy that precipitates in the solid state

- id: B09-Q10
- concept_id: u4-precipitation-alloys
- format: identify
- asks: classification

Which Pb-Sn alloy forms β only by solid-state precipitation on slow cooling from the liquid to room temperature:

a) Pb-1 wt% Sn
b) Pb-16 wt% Sn
c) Pb-40 wt% Sn
d) Pb-61.9 wt% Sn

### Answer

b

### Explanation

Pb-16 wt% Sn solidifies as single-phase α (below 18.3 wt% Sn it never reaches the eutectic) and then crosses the solvus near 172 °C, where β precipitates in the solid (Session 8, Slide 4).

- a) Pb-1 wt% Sn stays inside the α field down to room temperature and never crosses the solvus (Session 8, Slide 2).
- c) Pb-40 wt% Sn forms its β in the eutectic at 183 °C, from liquid, not only by precipitation.
- d) The eutectic alloy forms all its β from the liquid at 183 °C.

### Source

Session 8, Slides 2-4.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
