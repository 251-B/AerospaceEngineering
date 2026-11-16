---
materia: Aerospace Materials I
tema: "Unit 5: ductility, percent elongation after failure and percent reduction in area"
bank_id: B26
title: "Ductility: percent elongation and percent reduction in area"
category: mt2_test_block
unit: 5
concepts:
  - u5-percent-elongation
  - u5-reduction-in-area
  - u5-ductility-meaning
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 11, Slides 16 and 32-33."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-5
---

# Bank B26 — Ductility: percent elongation and percent reduction in area

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 11, Slides 16 and 32-33.

## Q26.1 Percent elongation from the gauge marks

- id: B26-Q1
- concept_id: u5-percent-elongation
- format: numeric
- asks: calculation
- calc: (63.5-50.0)/50.0*100

Gauge marks 50.0 mm apart are found 63.5 mm apart after the specimen has fractured. Determine the percent elongation:

a) 0.270 %
b) 21.3 %
c) 27.0 %
d) 127 %

### Answer

c

### Explanation

Session 11, Slide 32: $EL(\%) = \dfrac{l_f - l_0}{l_0}\times100 = \dfrac{63.5 - 50.0}{50.0}\times100 = 27.0\,\%$.

- a) The fraction 0.270 was written with a percent sign without multiplying by 100.
- b) The elongation was divided by the final length, 63.5 mm, instead of the initial one.
- d) The ratio $l_f/l_0$ was multiplied by 100 without subtracting the original length.

### Source

Session 11, Slide 32.

## Q26.2 Percent elongation read from a curve

- id: B26-Q2
- concept_id: u5-percent-elongation
- format: diagram-reading
- asks: figure-reading
- check: abs((0.30 - 280/70000)*100 - 29.6) < 1e-6

The shown curve belongs to an alloy with $E$ = 70 GPa. Determine its percent elongation after failure:

![[attachments/MAT-MT2/u5-fracture-el.svg]]

a) 0.4 %
b) 29.6 %
c) 30.0 %
d) 30.4 %

### Answer

b

### Explanation

Session 11, Slide 32: %EL is the percentage of plastic strain at fracture, "removing elastic recovery". At fracture $\varepsilon_t = 0.30$ and $\varepsilon_e = \sigma_f/E = 280/70\,000 = 0.004$, so $\varepsilon_p = 0.296$ and $EL = 29.6\,\%$.

- a) This is only the elastic strain recovered at fracture, $280/70\,000$, not the plastic strain that remains.
- c) The strain at fracture was read with its elastic part; after fracture that part is recovered.
- d) The elastic recovery was added to the strain at fracture instead of subtracted.

### Source

Session 11, Slides 12 and 32.

## Q26.3 When the percent elongation is measured

- id: B26-Q3
- concept_id: u5-percent-elongation
- format: true-statement
- asks: definition

Which one of the following statements about the percent elongation after failure is TRUE?

a) It is measured at the maximum load of the test
b) It always equals the percent reduction in area
c) It includes the elastic strain present at fracture
d) It is measured after fracture, without the elastic strain

### Answer

d

### Explanation

Session 11, Slide 32: $EL(\%) = (l_f - l_0)/l_0 \times 100$, measured once the specimen has fractured, so the material has recovered its elastic deformation; after fracture $\varepsilon_t = \varepsilon_p$.

- a) The maximum load gives the tensile strength; the elongation is measured between the marks after fracture.
- b) The slide states that normally $\varepsilon(\%) \neq RA(\%)$.
- c) After fracture the load is zero and the elastic strain has been recovered: $\varepsilon_t = \varepsilon_p$.

### Source

Session 11, Slides 32-33.

## Q26.4 Ranking alloys by percent elongation

- id: B26-Q4
- concept_id: u5-percent-elongation
- format: ordering
- asks: calculation
- check: (62-50)/50 > (30-25)/25 > (56-50)/50 > (54.5-50)/50

Order four alloys from the most to the least ductile, given their gauge lengths before and after fracture: A 50 to 56 mm, B 50 to 62 mm, C 50 to 54.5 mm, D 25 to 30 mm:

a) B > D > C > A
b) B > D > A > C
c) B > A > D > C
d) C > A > D > B

### Answer

b

### Explanation

Session 11, Slide 32: $EL = (l_f - l_0)/l_0 \times 100$: A 12 %, B 24 %, C 9 %, D 20 %. Ductility is compared through this percentage, so B > D > A > C.

- a) A and C were swapped: A reaches 12 % and C only 9 %.
- c) The elongations in millimetres (12, 6, 5, 4.5) were compared without dividing by each initial length.
- d) This is the right order reversed.

### Source

Session 11, Slide 32.

## Q26.5 Percent reduction in area

- id: B26-Q5
- concept_id: u5-reduction-in-area
- format: numeric
- asks: calculation
- calc: (10.0**2-6.0**2)/10.0**2*100

A specimen of 10.0 mm diameter breaks with a neck diameter of 6.0 mm. Determine the percent reduction in area:

a) 36.0 %
b) 40.0 %
c) 64.0 %
d) 178 %

### Answer

c

### Explanation

Session 11, Slide 33: $RA(\%) = \dfrac{A_0 - A_f}{A_0}\times100 = \dfrac{10.0^2 - 6.0^2}{10.0^2}\times100 = 64.0\,\%$ (the factor $\pi/4$ cancels).

- a) This is $A_f/A_0 \times 100$, the area that remains, not the reduction.
- b) The diameters were used instead of the areas: $(10 - 6)/10$.
- d) The reduction was divided by the final area instead of the initial one: $64/36$.

### Source

Session 11, Slide 33.

## Q26.6 Statements on the reduction in area

- id: B26-Q6
- concept_id: u5-reduction-in-area
- format: false-statement
- asks: comparison

Which one of the following statements about the percent reduction in area is FALSE?

a) It is measured after the specimen has fractured
b) It is another measure of ductility
c) It compares the initial and the final cross-sections
d) It is always equal to the percent elongation

### Answer

d

### Explanation

Session 11, Slide 33: "normally $\varepsilon(\%) \neq AR(\%)$"; the two percentages measure ductility in different ways, so they do not coincide.

- a) This is true: $A_f$ is measured after fracture (Slide 33).
- b) This is true: ductility can be given as %EL or as %RA (Slide 33).
- c) This is true: $RA = (A_0 - A_f)/A_0 \times 100$.

### Source

Session 11, Slide 33.

## Q26.7 Neck diameter from the reduction in area

- id: B26-Q7
- concept_id: u5-reduction-in-area
- format: numeric
- asks: application
- calc: 12*sqrt(1-0.51)

A 12 mm diameter bar shows a reduction in area of 51 % after fracture. Determine the diameter of the fracture section:

a) 5.88 mm
b) 6.12 mm
c) 8.40 mm
d) 17.1 mm

### Answer

c

### Explanation

Session 11, Slide 33: $A_f = A_0(1 - RA) = 0.49\,A_0$; since $A \propto d^2$, $d_f = d_0\sqrt{0.49} = 12 \times 0.70 = 8.40$ mm.

- a) The area fraction 0.49 was applied to the diameter without taking the square root.
- b) The reduction, 0.51, was applied to the diameter as if it were the fraction that remains.
- d) The ratio was inverted: $12/0.70$ gives a diameter larger than the original.

### Source

Session 11, Slide 33.

## Q26.8 Definition of ductility

- id: B26-Q8
- concept_id: u5-ductility-meaning
- format: complete-sentence
- asks: definition

Ductility is a measure of:

a) the plastic deformation supported before fracture
b) the resistance of the material to elastic deformation
c) the surface resistance to permanent indentation
d) the elastic energy stored up to the yield point

### Answer

a

### Explanation

Session 11, Slide 32: "ductility: measure of the degree of plastic deformation that can be supported by a material before fracture"; it is given as %EL or %RA.

- b) This is stiffness, given by Young's modulus (Slide 12).
- c) This is hardness (Session 12, Slide 15).
- d) This is the modulus of resilience (Slide 35).

### Source

Session 11, Slides 12, 32 and 35; Session 12, Slide 15.

## Q26.9 Practical meaning of ductility

- id: B26-Q9
- concept_id: u5-ductility-meaning
- format: identify
- asks: application

Which practical information does the ductility of a metal give, according to the slides?

a) How deep an indenter goes into the surface
b) How many forming operations can be done in sequence
c) How much elastic energy a spring can store
d) How stiff a beam will be under service loads

### Answer

b

### Explanation

Session 11, Slide 33: ductility "indicates the maximum deformation the material can withstand before fracture, how many forming operations can be sequentially performed (i.e. lamination)".

- a) That is the Rockwell hardness test (Session 12, Slide 22).
- c) That is read from the modulus of resilience, $\sigma_y^2/2E$ (Slide 35).
- d) Stiffness depends on Young's modulus, not on the plastic strain at fracture.

### Source

Session 11, Slides 12, 33 and 35; Session 12, Slide 22.

## Q26.10 Ductile and brittle materials

- id: B26-Q10
- concept_id: u5-ductility-meaning
- format: true-statement
- asks: comparison

Which one of the following statements about the tensile behaviour of materials is TRUE?

a) Ceramics break with almost no plastic deformation
b) Elastomers break at very low strains
c) Ceramics neck strongly before they break
d) Ductile metals break at very low strains

### Answer

a

### Explanation

Session 11, Slide 16: ceramics, glasses and concrete have steep curves with almost no plastic zone, metals neck before fracture, and elastomers reach high strains.

- b) Elastomers reach the largest strains of all the curves on Slide 16.
- c) Necking belongs to ductile metals; ceramic curves are steep and end at a low strain.
- d) Ductile metals deform plastically and neck before fracture; a low strain at fracture is the brittle case.

### Source

Session 11, Slides 16 and 31.
