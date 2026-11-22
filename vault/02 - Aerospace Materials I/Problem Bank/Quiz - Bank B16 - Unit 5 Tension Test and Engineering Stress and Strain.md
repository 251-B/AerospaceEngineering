---
materia: Aerospace Materials I
tema: "Unit 5: mechanical properties, mechanical tests and engineering stress and strain"
bank_id: B16
title: "Mechanical tests, the tension test and engineering stress and strain"
category: mt2_test_block
unit: 5
concepts:
  - u5-mechanical-property-definition
  - u5-tests-purpose
  - u5-tension-test-specimen
  - u5-engineering-stress-calc
  - u5-engineering-strain-calc
difficulty: 1
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 11, Slides 2-4 and 9."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-5
---

# Bank B16 — Mechanical tests, the tension test and engineering stress and strain

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 11, Slides 2-4 and 9.

## Q16.1 What a mechanical property describes

- id: B16-Q1
- concept_id: u5-mechanical-property-definition
- format: complete-sentence
- asks: definition

A mechanical property of a material describes:

a) how its phases change with temperature
b) how fast its atoms diffuse at high temperature
c) how it responds to applied mechanical forces
d) how it responds to an applied electric field

### Answer

c

### Explanation

Session 11, Slide 3 defines a mechanical property as "how a material responds to an outside stimulus induced by mechanical forces": a load produces a strain, and the microstructure controls the relation between them.

- a) This is what a phase diagram shows (Unit 4); it involves no applied force at all.
- b) Diffusion is mass transport (Unit 3), a kinetic property, not the response of the material to a load.
- d) This describes an electrical property (Unit 6), the neighbouring family of properties; a mechanical property is the response to a mechanical force.

### Source

Session 11, Slides 2-3.

## Q16.2 Key mechanical properties

- id: B16-Q2
- concept_id: u5-mechanical-property-definition
- format: identify
- asks: classification

Which property in the following list is NOT a mechanical property?

a) Toughness
b) Electrical conductivity
c) Stiffness
d) Ductility

### Answer

b

### Explanation

Session 11, Slide 2 lists the key mechanical properties as stiffness, strength, hardness, ductility and toughness. Electrical conductivity is the response to an electric field, an electrical property of Unit 6.

- a) Toughness, the energy absorbed up to fracture, is one of the five key mechanical properties of Slide 2.
- c) Stiffness, measured by Young's modulus, is the first of the key mechanical properties of Slide 2.
- d) Ductility, the plastic deformation supported before fracture, is one of the key mechanical properties of Slide 2.

### Source

Session 11, Slide 2.

## Q16.3 Standardised mechanical tests

- id: B16-Q3
- concept_id: u5-tests-purpose
- format: false-statement
- asks: definition

Which one of the following statements about mechanical tests is FALSE?

a) They replicate service conditions as nearly as possible
b) They are run under free, non-standard laboratory conditions
c) They are standardised laboratory experiments
d) They help to establish the causes of failure in service

### Answer

b

### Explanation

Session 11, Slide 3: tests are "carefully designed (standardized) laboratory experiments that replicate as nearly as possible the service conditions"; they obey established standards (for example ASTM E8 for the tension test of metals, Slide 4). A free, non-standard test is the opposite of that.

- a) This is true: the tests are designed to replicate the service conditions as nearly as possible (Slide 3).
- c) This is true: Slide 3 states that tests are standardised and obey established standards.
- d) This is true: establishing the failure causes of a material in service is one of the five purposes listed on Slide 3.

### Source

Session 11, Slides 3-4.

## Q16.4 Purpose of a test after a failure

- id: B16-Q4
- concept_id: u5-tests-purpose
- format: complete-sentence
- asks: application

Testing samples cut from a bracket that broke in service, to find out why it broke, serves the purpose of:

a) selecting the material for a new design
b) quality control in the fabrication process
c) studying a new type of material
d) establishing the causes of failure in service

### Answer

d

### Explanation

Session 11, Slide 3 lists five purposes of the tests; one of them is to "establish the failure causes of the material during service", which is exactly the analysis of a part that broke in use.

- a) Determining properties to choose possible uses is a different purpose; the question is why an existing part failed.
- b) Quality control checks parts while they are being made, before they reach service; here the part has already failed in service.
- c) The bracket is an existing part made of a known material; nothing new is being developed.

### Source

Session 11, Slide 3.

## Q16.5 Nature of the uniaxial tension test

- id: B16-Q5
- concept_id: u5-tension-test-specimen
- format: true-statement
- asks: definition

Which one of the following statements about the uniaxial tension test is TRUE?

a) It uses a specimen whose section changes along the gauge
b) It is a non-destructive test, like the hardness tests
c) It records the load against time to obtain the curve
d) It is a destructive test on a specimen of uniform section

### Answer

d

### Explanation

Session 11, Slide 4: the uniaxial tension test is a normalised, destructive test for the evaluation of mechanical properties under tensile load, made on a specimen with a uniform cross-section (norm ASTM E8 for metals).

- a) The specimen has a uniform cross-section so that the stress is the same along the gauge length.
- b) Hardness tests are the non-destructive ones (Session 12, Slide 15); the tension test takes the specimen to fracture.
- c) The test records the load against the elongation, which become stress and strain; time is not the variable of the curve.

### Source

Session 11, Slides 4 and 9; Session 12, Slide 15.

## Q16.6 Gauge length of the specimen

- id: B16-Q6
- concept_id: u5-tension-test-specimen
- format: complete-sentence
- asks: cause

The calibration (gauge) length of a tensile specimen is the length needed for:

a) the grips to hold the specimen firmly
b) the stress to be transmitted uniformly
c) the specimen to recover its length on unloading
d) necking to start at the shoulders of the specimen

### Answer

b

### Explanation

Session 11, Slide 4 defines the calibration length as the "necessary length so that σ is transmitted uniformly" along the specimen; the slide's ASTM E8 specimen has a 50 mm gauge length.

- a) Gripping is the job of the wider grip ends (18 mm diameter on the slide), not of the gauge length.
- c) Recovering the length on unloading is elastic behaviour of the material; it does not depend on the gauge length.
- d) The gauge length is chosen so that the stress is uniform along it, not to force necking at the shoulders.

### Source

Session 11, Slide 4.

## Q16.7 Engineering stress in a copper rod

- id: B16-Q7
- concept_id: u5-engineering-stress-calc
- format: numeric
- asks: calculation
- calc: 15000/(pi*4.0**2)

A tensile load of 15 kN is applied to a copper rod of 8.0 mm diameter. Determine the engineering stress:

a) 0.298 MPa
b) 74.6 MPa
c) 298 MPa
d) 937 MPa

### Answer

c

### Explanation

Engineering stress (Session 11, Slide 9): $\sigma_n = F/A_0$ with $A_0 = \pi r^2 = \pi\,(4.0)^2 = 50.3$ mm², so $\sigma_n = 15000/50.3 = 298$ MPa (N/mm² = MPa).

- a) The load was kept in kN: $15/(\pi\cdot 4^2) = 0.298$, a factor of 1000 too small.
- b) The diameter was used as the radius: $15000/(\pi\cdot 8^2) = 74.6$ MPa, an area four times too large.
- d) The factor $\pi$ was left out of the area: $15000/4^2 = 937.5$ MPa.

### Source

Session 11, Slide 9.

## Q16.8 Effect of doubling diameter on engineering stress

- id: B16-Q8
- concept_id: u5-engineering-stress-calc
- format: cause-effect
- asks: application

With an increase in the diameter of a cylindrical rod to twice its original value under the same axial tensile load, the engineering stress:

a) decreases by a factor of two
b) stays the same, because the load is unchanged
c) decreases by a factor of four
d) increases by a factor of four

### Answer

c

### Explanation

From $\sigma_n = F/A_0$ (Session 11, Slide 9), the cross-sectional area of a circular rod is $A_0 = \pi d_0^2/4$. Doubling $d_0$ multiplies $A_0$ by $2^2 = 4$, so under constant load $F$ the engineering stress is divided by four.

- a) This forgets that area scales with the square of diameter, $A_0 \propto d_0^2$, not linearly with $d_0$.
- b) Engineering stress depends on both load and original cross-sectional area; increasing the area lowers the stress.
- d) Inverted dependence: a thicker rod spreads the same force over a larger cross-section, lowering the stress.

### Source

Session 11, Slide 9.

## Q16.9 Engineering strain from the gauge length

- id: B16-Q9
- concept_id: u5-engineering-strain-calc
- format: numeric
- asks: calculation
- calc: 0.42/120

Under load, the 120 mm gauge length of a specimen becomes 120.42 mm. Determine the engineering strain:

a) $3.50\times10^{-3}$
b) $3.50\times10^{-1}$
c) $4.20\times10^{-1}$
d) 1.0035

### Answer

a

### Explanation

Engineering strain (Session 11, Slide 9): $\varepsilon_n = (l - l_0)/l_0 = (120.42 - 120)/120 = 0.42/120 = 3.50\times10^{-3}$, a non-dimensional number.

- b) The strain in percent (0.35 %) was written as a fraction, a factor of 100 too large.
- c) The elongation in millimetres, 0.42, was given as the strain without dividing by $l_0$.
- d) This is the ratio $l/l_0$, not $(l - l_0)/l_0$: the original length was not subtracted.

### Source

Session 11, Slide 9.

## Q16.10 Definition of engineering strain

- id: B16-Q10
- concept_id: u5-engineering-strain-calc
- format: complete-sentence
- asks: definition

In the tension test, the nominal (engineering) strain is:

a) the elongation divided by the original length
b) the load divided by the original area
c) the elongation of the gauge, in millimetres
d) the elongation divided by the final length

### Answer

a

### Explanation

Session 11, Slide 9: $\varepsilon_n = (l - l_0)/l_0$, the change of length divided by the initial length; it is non-dimensional.

- b) This is the nominal (engineering) stress $F/A_0$, the other variable of the curve.
- c) The elongation alone has units of length; the strain is normalised by $l_0$ and has no dimension.
- d) Dividing by the current length belongs to the true strain built step by step (Slide 37), not to the nominal strain.

### Source

Session 11, Slides 9 and 37.
