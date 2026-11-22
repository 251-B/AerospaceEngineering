---
materia: Aerospace Materials I
tema: "Unit 5: toughness as the area under the curve, modulus of resilience and spring materials"
bank_id: B27
title: "Toughness and the modulus of resilience"
category: mt2_test_block
unit: 5
concepts:
  - u5-toughness-area
  - u5-modulus-resilience-calc
  - u5-resilience-spring-materials
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 11, Slides 5, 12 and 34-35."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-5
---

# Bank B27 — Toughness and the modulus of resilience

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 11, Slides 5, 12 and 34-35.

## Q27.1 Tougher of two alloys

- id: B27-Q1
- concept_id: u5-toughness-area
- format: diagram-reading
- asks: comparison

From the shown stress-strain curves of alloys A and B, indicate which statement about their toughness is TRUE:

![[attachments/MAT-MT2/u5-two-curves-toughness.svg]]

a) B is tougher, because its area under the curve is larger
b) A is tougher, because its tensile strength is higher
c) B is tougher, because its yield strength is lower
d) A is tougher, because its curve is higher everywhere

### Answer

a

### Explanation

Session 11, Slide 34: toughness is the energy absorbed up to fracture by elastic and plastic deformation, the area under the stress-strain curve. A: about $650 \times 0.05 \approx 32$ MJ/m³; B: about $370 \times 0.35 \approx 130$ MJ/m³.

- b) A higher maximum stress does not make up for a strain at fracture seven times smaller; toughness is the whole area.
- c) The answer is right but the reason is wrong: a lower yield strength alone lowers the area; B wins through its much larger strain at fracture.
- d) A's curve ends at a strain of 0.05, so beyond that it encloses no area at all.

### Source

Session 11, Slide 34.

## Q27.2 Measure of toughness on the curve

- id: B27-Q2
- concept_id: u5-toughness-area
- format: identify
- asks: definition

Which quantity of the stress-strain curve measures the toughness of a material?

a) The height of the maximum of the curve
b) The area under the elastic part only
c) The slope of the elastic part of the curve
d) The whole area under the curve up to fracture

### Answer

d

### Explanation

Session 11, Slide 34: "area under the curve: it is a measure of toughness", the elastic plus plastic energy per unit volume (Pa or J/m³).

- a) The maximum is the tensile strength, a stress, not an energy.
- b) The area up to the yield point is the modulus of resilience (Slide 35).
- c) The slope is Young's modulus, the stiffness (Slide 12).

### Source

Session 11, Slides 12 and 34-35.

## Q27.3 Statements on toughness

- id: B27-Q3
- concept_id: u5-toughness-area
- format: false-statement
- asks: application

Which one of the following statements about toughness is FALSE?

a) It counts only the elastic energy of the material
b) It can be measured with an impact test
c) It matters in protection and security systems
d) It is an energy per unit volume, in J/m³

### Answer

a

### Explanation

Session 11, Slide 34: toughness is the ability to absorb energy up to fracture "by elastic and plastic deformation"; only the elastic energy up to yielding is the resilience.

- b) This is true: the impact test determines toughness as the energy absorbed until fracture (Slide 5).
- c) This is true: the slide names protection and security systems among its applications.
- d) This is true: toughness is given in Pa or J/m³ (Slide 34).

### Source

Session 11, Slides 5 and 34-35.

## Q27.4 Modulus of resilience of a spring steel

- id: B27-Q4
- concept_id: u5-modulus-resilience-calc
- format: numeric
- asks: calculation
- calc: 1000**2/(2*207000)

Determine the modulus of resilience of a spring steel with a yield strength of 1000 MPa and $E$ = 207 GPa:

a) 0.00242 MJ/m³
b) 2.42 MJ/m³
c) 4.83 MJ/m³
d) 2420 MJ/m³

### Answer

b

### Explanation

Session 11, Slide 35: $U_r = \sigma_y^2/(2E) = 1000^2/(2 \times 207\,000) = 2.42$ MPa $= 2.42$ MJ/m³ (1 MPa = 1 MJ/m³).

- a) The yield strength was not squared: $\sigma_y/(2E)$, which is a strain, not an energy.
- c) The factor 1/2 of the triangle was left out.
- d) The modulus was entered in GPa, $1000^2/(2 \times 207)$, a factor of 1000 too large.

### Source

Session 11, Slide 35.

## Q27.5 Yield-strength dependence of resilience

- id: B27-Q5
- concept_id: u5-modulus-resilience-calc
- format: topic-false
- asks: application

Referring to the modulus of resilience $U_r = \sigma_y^2/(2E)$ of a linear-elastic material, which statement is FALSE?

a) Its SI unit is J/m³ (equivalently Pa or MJ/m³)
b) It equals the maximum elastic energy per unit volume recoverable on unloading
c) Doubling $\sigma_y$ while keeping $E$ constant doubles the modulus of resilience
d) High-resilience spring alloys combine high yield strength with relatively low $E$

### Answer

c

### Explanation

Because $U_r = \sigma_y^2/(2E)$ scales with the square of the yield strength $\sigma_y$ (Session 11, Slide 35), doubling $\sigma_y$ at constant $E$ multiplies $U_r$ by $2^2 = 4$, not by $2$.

- a) This is true: Slide 35 gives $U_r$ in Pa or J/m³, since stress has units of Pa = J/m³ and strain is dimensionless.
- b) This is true: resilience is the elastic energy absorbed up to the yield point and recovered on unloading.
- d) This is true: maximizing $\sigma_y^2/(2E)$ calls for high $\sigma_y$ and low $E$, the criterion for spring alloys (Slide 35).

### Source

Session 11, Slide 35.

## Q27.6 Resilience and yield strength

- id: B27-Q6
- concept_id: u5-modulus-resilience-calc
- format: cause-effect
- asks: effect

With an increase in the yield strength of an alloy at constant Young's modulus, its modulus of resilience:

a) increases in proportion to the yield strength
b) decreases, because the alloy becomes harder
c) increases with the square of the yield strength
d) stays the same, because the modulus does not change

### Answer

c

### Explanation

Session 11, Slide 35: $U_r = \tfrac12\sigma_y\varepsilon_y$ with $\varepsilon_y = \sigma_y/E$, so $U_r = \sigma_y^2/(2E)$.

- a) The trend is right but the law is not: $U_r$ goes with $\sigma_y^2$, so doubling $\sigma_y$ multiplies it by four.
- b) The trend is inverted: a higher yield strength stores more elastic energy.
- d) $U_r$ depends on both $\sigma_y$ and $E$; changing $\sigma_y$ alone changes it.

### Source

Session 11, Slide 35.

## Q27.7 Definition of the modulus of resilience

- id: B27-Q7
- concept_id: u5-modulus-resilience-calc
- format: complete-sentence
- asks: definition

The modulus of resilience is the energy per unit volume:

a) needed to deform the material up to the yield point
b) absorbed in the plastic zone only
c) needed to start necking in the specimen
d) absorbed by the material up to fracture

### Answer

a

### Explanation

Session 11, Slide 35: "modulus of resilience $U_r$: $E_{\text{deformation}}$ per unit volume (Pa or J/m³) necessary to deform a material up to the yield point", $U_r = \int_0^{\varepsilon_y}\sigma\,d\varepsilon$.

- b) Resilience is elastic energy; the plastic zone starts where it ends.
- c) Necking starts at the tensile strength, well into the plastic zone.
- d) Energy up to fracture, elastic plus plastic, is toughness (Slide 34).

### Source

Session 11, Slides 34-35.

## Q27.8 Resilience as an area

- id: B27-Q8
- concept_id: u5-resilience-spring-materials
- format: choose-figure
- asks: figure-reading

Which picture shows the modulus of resilience as the shaded area under a stress-strain curve?

a) ![[attachments/MAT-MT2/u5-area-4.svg]]
b) ![[attachments/MAT-MT2/u5-area-2.svg]]
c) ![[attachments/MAT-MT2/u5-area-1.svg]]
d) ![[attachments/MAT-MT2/u5-area-3.svg]]

### Answer

d

### Explanation

Session 11, Slide 35: $U_r = \int_0^{\varepsilon_y}\sigma\,d\varepsilon$; for a linear elastic zone it is the triangle under the straight line up to the yield point, $\tfrac12\sigma_y\varepsilon_y$.

- a) The area from the maximum to fracture belongs to the necking part of the test, not to the elastic zone.
- b) The area from the yield point to fracture is the plastic energy; resilience ends where it begins.
- c) The whole area up to fracture is the toughness, not the resilience.

### Source

Session 11, Slides 34-35.

## Q27.9 Best alloy for a spring

- id: B27-Q9
- concept_id: u5-resilience-spring-materials
- format: identify
- asks: application
- check: 900**2/107000 > max(900**2/207000, 600**2/69000, 200**2/45000)

Which alloy stores the most elastic energy per unit volume and is therefore the best choice for a spring?

a) Magnesium alloy: $\sigma_y$ = 200 MPa, $E$ = 45 GPa
b) Titanium alloy: $\sigma_y$ = 900 MPa, $E$ = 107 GPa
c) Steel: $\sigma_y$ = 900 MPa, $E$ = 207 GPa
d) Aluminium alloy: $\sigma_y$ = 600 MPa, $E$ = 69 GPa

### Answer

b

### Explanation

Session 11, Slide 35: $U_r = \sigma_y^2/(2E)$, and springs use alloys with high $U_r$. Titanium: $900^2/(2 \times 107\,000) = 3.79$ MJ/m³, the largest of the four.

- a) Choosing the lowest modulus alone ignores the yield strength: $U_r = 0.44$ MJ/m³.
- c) Same yield strength as the titanium alloy but twice the modulus, so half the resilience: $U_r = 1.96$ against 3.79 MJ/m³.
- d) This has the highest $\sigma_y/E$ (the yield strain), but $U_r$ goes with $\sigma_y^2$: 2.61 MJ/m³.

### Source

Session 11, Slides 17 and 35.

## Q27.10 Materials for springs

- id: B27-Q10
- concept_id: u5-resilience-spring-materials
- format: true-statement
- asks: cause

Which one of the following statements about materials for springs is TRUE?

a) They need a low yield strength and a high modulus
b) They need a high ductility above all
c) They need a high yield strength and a low modulus
d) They need a high yield strength and a high modulus

### Answer

c

### Explanation

Session 11, Slide 35: "materials with ↑ resilience: ↑ $\sigma_y$, ↓ $E$"; "application: alloys to fabricate springs", since $U_r = \sigma_y^2/(2E)$.

- a) Both requirements are inverted: this gives the lowest $\sigma_y^2/(2E)$.
- b) Ductility is plastic deformation; a spring must work in the elastic zone.
- d) Half right: a high modulus lowers the elastic energy stored up to yielding.

### Source

Session 11, Slides 32 and 35.
