---
materia: Aerospace Materials I
tema: "Unit 6: capacitors and dielectric constant, requirements of insulators, loss factor, dielectric strength, ferroelectrics and piezoelectrics"
bank_id: B42
title: "Dielectrics, ferroelectrics and piezoelectrics"
category: mt2_test_block
unit: 6
concepts:
  - u6-dielectric-capacitance
  - u6-insulator-properties
  - u6-ferroelectric-polarisation
  - u6-piezoelectric
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 13 Slides 51-60."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B42 — Dielectrics, ferroelectrics and piezoelectrics

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 13, Slides 51-60.

## Q42.1 Capacitance with a porcelain dielectric

- id: B42-Q1
- concept_id: u6-dielectric-capacitance
- format: numeric
- asks: calculation
- calc: 6.0*8.85e-12*2.0e-4/0.5e-3*1e12

Two parallel plates of 2.0 cm² are separated by 0.50 mm of porcelain ($\varepsilon_r = 6.0$, $\varepsilon_0 = 8.85\times10^{-12}$ F/m). Determine the capacitance:

a) 0.0212 pF
b) 3.54 pF
c) 21.2 pF
d) 133 pF

### Answer

c

### Explanation

Session 13, Slide 52: $C = \varepsilon_r\varepsilon_0 A/d = 6.0\cdot8.85\times10^{-12}\cdot2.0\times10^{-4}/0.50\times10^{-3} = 2.12\times10^{-11}$ F $= 21.2$ pF ($\varepsilon_r$ of porcelain from Slide 57).

- a) The separation was left in mm ($d = 0.50$ taken as metres): the result is $10^{3}$ times too small, 0.0212 pF.
- b) The dielectric constant was left out: $C_0 = \varepsilon_0 A/d = 3.54$ pF is the capacitance with vacuum between the plates.
- d) Area and separation were swapped: $\varepsilon_r\varepsilon_0 d/A = 1.33\times10^{-10}$ F = 133 pF.

### Source

Session 13, Slides 52 and 57.

## Q42.2 Capacitor filled with barium titanate

- id: B42-Q2
- concept_id: u6-dielectric-capacitance
- format: what-happens
- asks: effect

What will happen to the charge stored at a fixed voltage when the vacuum between the plates of a capacitor is replaced by BaTiO₃:

a) It will rise about 4000 times
b) It will rise about 10 times
c) It will fall about 4000 times
d) It will rise about 400 times

### Answer

a

### Explanation

Session 13, Slides 52 and 57: $C = \varepsilon_r C_0$ and BaTiO₃ has $\varepsilon_r = 4000$; at the same voltage the plates store $Q = CV$, about 4000 times the charge of the same capacitor with vacuum.

- b) Uses the dielectric constant of a common dielectric, Al₂O₃ ($\varepsilon_r = 10$, Slide 57), instead of that of the ferroelectric.
- c) The dielectric constant was applied as a divisor: a polarised dielectric lets the plates store more charge, $Q_0 + Q'$, not less.
- d) Power-of-ten slip: $\varepsilon_r = 4000$ was read as 400, so $Q = CV$ rises 400 times instead of 4000 times.

### Source

Session 13, Slides 52 and 57.

## Q42.3 A good electrical insulator

- id: B42-Q3
- concept_id: u6-insulator-properties
- format: true-statement
- asks: definition

Which one of the following statements about a good electrical insulator is TRUE?

a) It should have a high permittivity
b) It should have a low dielectric strength
c) It should have a low resistivity
d) It should have a small loss factor

### Answer

d

### Explanation

Session 13, Slide 54: an insulator should have a high resistivity, a high dielectric strength, a small loss factor $\tan\delta$ and a low permittivity.

- a) Inverted: a low permittivity is required, to avoid polarisation; a high one is wanted in a capacitor dielectric.
- b) Inverted: a high dielectric strength is required, to avoid breakdowns of the insulation.
- c) Inverted: a high resistivity is required, to avoid current leaks.

### Source

Session 13, Slides 52 and 54.

## Q42.4 Frequency and loss factor

- id: B42-Q4
- concept_id: u6-insulator-properties
- format: cause-effect
- asks: effect

With an increase in the frequency of the current, the loss factor $\tan\delta$ of a capacitor dielectric:

a) Decreases, as the dipoles stop reorienting
b) Increases, due to friction among reorienting dipoles
c) Increases, due to electrons crossing the band gap
d) Decreases, as the resistivity of the dielectric rises

### Answer

b

### Explanation

Session 13, Slide 53: the loss factor is the electrical energy lost as heat by a capacitor in an alternating circuit, due to friction among the dipoles when they try to reorient; it increases with moisture, temperature and the frequency of the current.

- a) Inverted trend, contrary to the slide: faster field changes make the dipoles reorient more often.
- c) Right trend with a wrong cause: the loss comes from dipole friction, not from conduction across the gap of the insulator.
- d) The slide says the same factors lower the resistivity, and the loss factor rises.

### Source

Session 13, Slide 53.

## Q42.5 Dielectric strength of a porcelain sheet

- id: B42-Q5
- concept_id: u6-insulator-properties
- format: numeric
- asks: calculation
- calc: 24/2.0

A porcelain insulator sheet 0.20 cm thick breaks down at a voltage of 24 kV. Determine its dielectric strength:

a) 0.0833 kV/mm
b) 12.0 kV/mm
c) 48.0 kV/mm
d) $1.20\times10^{2}$ kV/mm

### Answer

b

### Explanation

Session 13, Slide 53: $E_{break} = U_{break}/d = 24\ \text{kV}/2.0\ \text{mm} = 12.0$ kV/mm, at the top of the 2-12 kV/mm range of porcelain insulators (Slide 54).

- a) The ratio was inverted: $d/U = 2.0/24 = 0.0833$.
- c) Voltage and thickness were multiplied: $24\cdot2.0 = 48.0$.
- d) The thickness was left in cm: $24/0.20 = 1.20\times10^{2}$, ten times too large in kV/mm.

### Source

Session 13, Slides 53-54.

## Q42.6 Ferroelectric materials

- id: B42-Q6
- concept_id: u6-ferroelectric-polarisation
- format: true-statement
- asks: comparison

Which one of the following statements about ferroelectric materials is TRUE?

a) Their dielectric constant is close to that of air
b) They have no dipoles without an applied field
c) Their dipoles stay aligned with no applied field
d) They polarise only under a mechanical stress

### Answer

c

### Explanation

Session 13, Slide 55: ferroelectric materials have permanent dipoles that can remain aligned in the absence of an electric field, a spontaneous polarisation.

- a) Inverted comparison: $\varepsilon_r$ of ferroelectrics is much larger than that of common dielectrics (BaTiO₃ 4000, air 1.0; Slide 57).
- b) Describes a common dielectric, whose dipoles are randomly oriented and give zero net polarisation without field (Slide 51).
- d) Polarisation by a mechanical stress defines the piezoelectric effect (Slide 58).

### Source

Session 13, Slides 51, 55, 57 and 58.

## Q42.7 Barium titanate above 120 °C

- id: B42-Q7
- concept_id: u6-ferroelectric-polarisation
- format: complete-sentence
- asks: effect

Above its Curie temperature of 120 °C, barium titanate:

a) Becomes cubic and loses its permanent dipoles
b) Becomes tetragonal and gains permanent dipoles
c) Stays ferroelectric up to its melting point
d) Becomes cubic and keeps its dipoles aligned

### Answer

a

### Explanation

Session 13, Slide 56: above the Curie temperature a ferroelectric loses its ferroelectric properties; BaTiO₃ ($T_c = 120$ °C) is tetragonal below 120 °C and cubic above it, and the permanent dipoles disappear.

- b) Swaps the two structures: the tetragonal, polarised form is the one below 120 °C.
- c) Ignores the Curie temperature, above which the material becomes a plain dielectric.
- d) Right structure, wrong consequence: in the symmetric cubic cell the ions are not displaced, so no permanent dipole remains.

### Source

Session 13, Slides 55-56.

## Q42.8 Remanent polarisation on the loop

- id: B42-Q8
- concept_id: u6-ferroelectric-polarisation
- format: diagram-reading
- asks: figure-reading

From the shown hysteresis loop of a ferroelectric, indicate the point that gives the remanent polarisation:

![[attachments/MAT-MT2/u6-pe-loop.svg]]

a) Point K
b) Point L
c) Point M
d) Point N

### Answer

c

### Explanation

Session 13, Slide 56: the remanent polarisation $P_r$ is the polarisation that stays when the field is removed, so it is read where the loop crosses the polarisation axis at $E = 0$: point M.

- a) Point K is the tip of the loop, the saturation polarisation reached under a strong field.
- b) Point L is where the polarisation returns to zero under a reversed field: the coercive field $E_c$.
- d) Point N is the origin, the unpolarised state before the first application of the field.

### Source

Session 13, Slide 56.

## Q42.9 Direct piezoelectric effect

- id: B42-Q9
- concept_id: u6-piezoelectric
- format: identify
- asks: application

Which device is based on the direct piezoelectric effect?

a) An inkjet printer actuator
b) A speaker transducer
c) A BaTiO₃ capacitor of a computer memory
d) A lighter that turns a shock into a spark

### Answer

d

### Explanation

Session 13, Slides 58-60: in the direct effect an external stress deforms the crystal, alters the dipoles and generates an electric field; a lighter converts a mechanical shock into a spark.

- a) The inkjet actuator is pushed by a pulsed voltage: an electric field changes the dimensions, the reverse effect.
- b) A speaker transducer converts an electric signal into motion, also the reverse effect.
- c) Ferroelectric capacitors use the high dielectric constant of BaTiO₃ (Slide 57), not a mechanical stress.

### Source

Session 13, Slides 57-60.

## Q42.10 Piezoelectric materials

- id: B42-Q10
- concept_id: u6-piezoelectric
- format: false-statement
- asks: definition

Which one of the following statements about piezoelectric materials is FALSE?

a) They occur in ceramics with a low degree of symmetry
b) In the direct effect, an electric field changes their dimensions
c) They are ferroelectrics that polarise under a mechanical stress
d) They convert electrical energy into mechanical energy and back

### Answer

b

### Explanation

Session 13, Slide 58: in the direct effect an external stress generates a voltage; a dimensional change produced by an electric field is the reverse effect (electrostriction). Statement b) is false.

- a) True: the effect occurs in ceramics whose crystal structure has a low degree of symmetry (Slide 58).
- c) True: piezoelectrics are ferroelectric materials that can be polarised by an external mechanical stress (Slide 58).
- d) True: they are used to transform electrical energy into mechanical energy and vice versa (Slide 59).

### Source

Session 13, Slides 58-59.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
