---
materia: Aerospace Materials I
tema: "Unit 5: working stress and safety factor, tensile strength, necking and fracture stress"
bank_id: B24
title: "Working stress, tensile strength and necking"
category: mt2_test_block
unit: 5
concepts:
  - u5-working-stress-safety-factor
  - u5-tensile-strength-definition
  - u5-necking-fracture-stress
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 11, Slides 9 and 29-31."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-5
---

# Bank B24 — Working stress, tensile strength and necking

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 11, Slides 9 and 29-31.

## Q24.1 Largest working load of a brass rod

- id: B24-Q1
- concept_id: u5-working-stress-safety-factor
- format: numeric
- asks: calculation
- calc: 345/2*pi*5**2/1000

A brass rod of 10 mm diameter has a yield strength of 345 MPa. With a safety factor of 2, determine the largest working load:

a) 6.77 kN
b) 13.5 kN
c) 27.1 kN
d) 54.2 kN

### Answer

b

### Explanation

Session 11, Slide 29: $\sigma_w = \sigma_y/N = 345/2 = 172.5$ MPa; $F = \sigma_w A_0 = 172.5 \times \pi\,(5)^2 = 13\,550$ N $= 13.5$ kN.

- a) The safety factor was applied twice, $345/2^2$, which halves the allowed load once more.
- c) The safety factor was left out: this is the load that starts yielding, with no margin.
- d) The diameter was used as the radius, so the area is four times too large.

### Source

Session 11, Slides 9 and 29.

## Q24.2 Definition of the working stress

- id: B24-Q2
- concept_id: u5-working-stress-safety-factor
- format: complete-sentence
- asks: definition

In design, the working stress is:

a) the yield strength multiplied by the safety factor
b) the fracture stress divided by the safety factor
c) the tensile strength multiplied by the safety factor
d) the yield strength divided by the safety factor

### Answer

d

### Explanation

Session 11, Slide 29: "design security: working stress $\sigma_w = \sigma_y/N$", with $\sigma_y$ the yield strength and $N$ the safety factor.

- a) With $N > 1$ this would allow stresses above the yield strength, that is, permanent deformation in service.
- b) The slide divides the yield strength, so that the part stays in the elastic zone.
- c) Multiplying would give a stress above the tensile strength, and the slide's design is based on the yield strength.

### Source

Session 11, Slide 29.

## Q24.3 Effect of increasing the safety factor

- id: B24-Q3
- concept_id: u5-working-stress-safety-factor
- format: what-happens
- asks: application

A structural tie rod carrying a fixed axial load is redesigned with a larger safety factor $N > 1$ against yielding using the same alloy. What must change in the rod?

a) Its cross-sectional area must decrease so the working stress rises
b) Its length must decrease so the elastic strain falls
c) Its cross-sectional area must increase so the stress stays within $\sigma_w = \sigma_y/N$
d) Its diameter stays unchanged because $N$ does not affect sizing

### Answer

c

### Explanation

Since $\sigma_w = \sigma_y/N$ (Session 11, Slide 29), increasing $N$ lowers the allowable working stress $\sigma_w$. To carry the same force $F$ without exceeding $\sigma_w = F/A_0$, the minimum cross-sectional area $A_0 = F/\sigma_w = N F/\sigma_y$ must increase.

- a) Reducing the area raises the stress in service, which lowers rather than raises the safety margin.
- b) Axial stress $\sigma = F/A_0$ is independent of the rod's length.
- d) The safety factor directly sets the allowable working stress and therefore the required cross-section.

### Source

Session 11, Slides 9 and 29.

## Q24.4 Why a working stress is used

- id: B24-Q4
- concept_id: u5-working-stress-safety-factor
- format: cause-effect
- asks: cause

Parts are designed for a working stress below the yield strength because:

a) mechanical properties vary from one piece to another
b) the yield strength always rises during service
c) Young's modulus changes with the applied load
d) the tensile strength is lower than the yield strength

### Answer

a

### Explanation

Session 11, Slide 29: the working stress is used "due to the variability in mechanical properties", as a design safety margin: $\sigma_w = \sigma_y/N$.

- b) This is not a reason given on the slide, and a rising strength would not call for a margin.
- c) In the linear elastic zone $E$ is a constant of the material.
- d) False premise: the tensile strength is the maximum of the curve, above the yield strength.

### Source

Session 11, Slides 12, 29 and 30.

## Q24.5 Tensile strength

- id: B24-Q5
- concept_id: u5-tensile-strength-definition
- format: true-statement
- asks: definition

Which one of the following statements about the tensile strength is TRUE?

a) It is the maximum nominal stress of the curve
b) It is the nominal stress at which fracture occurs
c) It is the true stress at the moment of fracture
d) It is always lower than the yield strength

### Answer

a

### Explanation

Session 11, Slide 30: "tensile strength (or ultimate TS): maximum nominal stress that a specimen supports under tension"; necking follows it.

- b) That is the fracture stress (Slide 31), which in a ductile metal is below the maximum.
- c) The tensile strength is a nominal (engineering) value, $F_{\max}/A_0$.
- d) The tensile strength is reached after yielding and is the maximum of the engineering curve.

### Source

Session 11, Slides 30-31.

## Q24.6 Ultimate tensile strength versus nominal fracture stress

- id: B24-Q6
- concept_id: u5-tensile-strength-definition
- format: topic-false
- asks: comparison

With respect to ultimate tensile strength (UTS) and nominal fracture stress in a ductile metal tensile test, which statement is FALSE?

a) UTS equals the maximum load divided by the original cross-sectional area $A_0$
b) Plastic deformation remains uniform along the gauge length up to UTS
c) Beyond UTS, localized necking reduces the load required for further stretching
d) The nominal fracture stress is always higher than UTS because the necked area shrinks

### Answer

d

### Explanation

In an engineering (nominal) curve, both UTS and nominal fracture stress divide the load by the original area $A_0$ (Session 11, Slides 9 and 30-31). Because necking after UTS reduces the load the specimen can sustain, the nominal fracture stress of a ductile metal is lower than UTS (whereas true fracture stress $F_f/A_f$ is higher).

- a) This is true: UTS is the maximum engineering stress $F_{\max}/A_0$ (Slide 30).
- b) This is true: uniform plastic deformation extends from yielding up to UTS (Slides 9 and 30).
- c) This is true: once necking starts at UTS, the cross-section decreases locally and the nominal load falls until fracture.

### Source

Session 11, Slides 9, 30-31 and 37.

## Q24.7 Pulling past the maximum of the curve

- id: B24-Q7
- concept_id: u5-tensile-strength-definition
- format: what-happens
- asks: effect

A ductile metal specimen is pulled past the maximum of its engineering stress-strain curve. What will happen to it:

a) It will return elastically to its original length
b) It will break at once with no further strain
c) It will deform uniformly with a rising load
d) It will neck, and the load will fall until fracture

### Answer

d

### Explanation

Session 11, Slides 9 and 30-31: necking follows the tensile strength; the deformation concentrates in the neck and the nominal stress falls until the fracture stress is reached.

- a) Only the elastic part of the strain could be recovered, and only on unloading.
- b) Sudden fracture at the maximum is the behaviour of brittle materials; a ductile metal still deforms in the neck.
- c) Uniform deformation with a rising load happens before the maximum, between yielding and the tensile strength.

### Source

Session 11, Slides 9 and 30-31.

## Q24.8 Ductility and necking

- id: B24-Q8
- concept_id: u5-necking-fracture-stress
- format: cause-effect
- asks: comparison

With an increase in the ductility of a metal, the necking before fracture:

a) stays the same, because it depends only on the load
b) increases, because of porosity and inclusions
c) increases, because more plastic flow is possible
d) decreases, because the metal is softer

### Answer

c

### Explanation

Session 11, Slide 31: "the more ductile the material, the higher the amount of necking or constriction".

- a) The amount of necking depends on the material, as the slide's comparison shows.
- b) The trend is right but the cause is wrong: defects lower the fracture stress, they do not make the metal ductile.
- d) The trend is inverted: the slide states that more ductile materials neck more.

### Source

Session 11, Slide 31.

## Q24.9 A very low fracture stress

- id: B24-Q9
- concept_id: u5-necking-fracture-stress
- format: identify
- asks: cause

In a tensile test, which material feature is indicated by an abnormally low fracture stress?

a) A very fine grain size
b) Defects such as porosity or inclusions
c) A very high Young's modulus
d) A very high ductility

### Answer

b

### Explanation

Session 11, Slide 31: "the fracture gives an idea of the presence of defects (porosity, inclusions) in the material if the value is very low".

- a) A fine grain size strengthens the metal (Session 12, Slide 10); it does not lower the fracture stress.
- c) $E$ describes elastic stiffness; it is not read from the fracture stress.
- d) High ductility shows as a large necking and elongation, not as an abnormally low fracture stress.

### Source

Session 11, Slides 12 and 31; Session 12, Slide 10.

## Q24.10 Where necking takes place on the curve

- id: B24-Q10
- concept_id: u5-necking-fracture-stress
- format: diagram-reading
- asks: figure-reading

From the shown engineering stress-strain curve, indicate between which marked points the specimen deforms with a neck:

![[attachments/MAT-MT2/u5-curve-points.svg]]

a) Between B and C
b) Between D and A
c) Between A and C
d) Between A and B

### Answer

a

### Explanation

Session 11, Slides 9 and 30: point B is the maximum of the curve, the tensile strength, and necking follows it; C is the fracture. Between A (end of the elastic line) and B the deformation is uniform plastic deformation.

- b) D and A are on the elastic line, where the deformation is elastic and uniform.
- c) This covers the whole plastic zone, including the uniform part from A to B.
- d) From A to B the deformation is plastic but uniform; the neck forms only after the maximum at B.

### Source

Session 11, Slides 9 and 30-31.
