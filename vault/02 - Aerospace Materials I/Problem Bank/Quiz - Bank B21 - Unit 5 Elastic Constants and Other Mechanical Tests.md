---
materia: Aerospace Materials I
tema: "Unit 5: elastic constants from the lateral contraction and the other mechanical tests"
bank_id: B21
title: "Elastic constants from contraction, and the compression, impact, bend, shear and torsion tests"
category: mt2_test_block
unit: 5
concepts:
  - u5-poisson-lateral-contraction
  - u5-modulus-from-poisson-contraction
  - u5-shear-modulus-relation
  - u5-compression-test
  - u5-impact-test
  - u5-bend-test
  - u5-shear-torsion-test
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 11, Slides 5-7 and 19."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-5
---

# Bank B21 — Elastic constants from contraction, and the compression, impact, bend, shear and torsion tests

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 11, Slides 5-7 and 19.

## Q21.1 Diameter of a bar under compression

- id: B21-Q1
- concept_id: u5-poisson-lateral-contraction
- format: cause-effect
- asks: cause

When a metal bar is compressed elastically along its axis, its diameter:

a) increases, because the axial strain is negative
b) stays constant, because only the length changes
c) increases, because its volume must stay constant
d) decreases, because the axial strain is negative

### Answer

a

### Explanation

Session 11, Slide 19: $\varepsilon_x = -\nu\,\varepsilon_z$. In compression $\varepsilon_z < 0$, so $\varepsilon_x > 0$ and the diameter grows; the same relation that shrinks a stretched bar makes a compressed one wider.

- b) Every elastic longitudinal deformation produces a transverse one (Slide 19).
- c) The trend is right but the cause is not: only an ideal material with $\nu = 0.5$ keeps its volume; metals have $\nu = 0.25$-0.4.
- d) The sign is wrong: with $\varepsilon_z < 0$, $\varepsilon_x = -\nu\,\varepsilon_z$ is positive, so the section grows.

### Source

Session 11, Slide 19.

## Q21.2 Largest load for an allowed contraction

- id: B21-Q2
- concept_id: u5-modulus-from-poisson-contraction
- format: numeric
- asks: application
- calc: 110000*(2.0e-3/10/0.34)*pi*5**2/1000

A copper bar of 10 mm diameter ($E$ = 110 GPa, $\nu$ = 0.34) may lose at most $2.0\times10^{-3}$ mm of diameter elastically. Determine the largest tensile load:

a) 0.587 kN
b) 1.73 kN
c) 5.08 kN
d) 20.3 kN

### Answer

c

### Explanation

$\varepsilon_x = 2.0\times10^{-3}/10 = 2.0\times10^{-4}$; $\varepsilon_z = \varepsilon_x/\nu = 5.88\times10^{-4}$ (Session 11, Slide 19); $\sigma = E\varepsilon_z = 64.7$ MPa (Slide 12); $F = \sigma\,\pi\,(5)^2 = 5082$ N $= 5.08$ kN.

- a) The transverse strain was multiplied by $\nu$ instead of divided by it, which gives an axial strain far too small.
- b) Poisson's ratio was left out: the transverse strain $2.0\times10^{-4}$ was used as the axial strain.
- d) The diameter was used as the radius, so the area, and with it the load, is four times too large.

### Source

Session 11, Slides 9, 12 and 17-19.

## Q21.3 Wrong Poisson's ratio in the modulus

- id: B21-Q3
- concept_id: u5-modulus-from-poisson-contraction
- format: cause-effect
- asks: effect

If $E$ is computed from a measured contraction using $\nu$ = 0.25 instead of the real 0.33, the modulus obtained is:

a) overestimated, because $E$ grows with $\nu$
b) underestimated, because $E$ grows with $\nu$
c) underestimated, because $E$ falls with $\nu$
d) unchanged, because $\nu$ does not enter the modulus

### Answer

b

### Explanation

$\varepsilon_z = |\varepsilon_x|/\nu$ (Session 11, Slide 19) and $E = \sigma/\varepsilon_z = \sigma\,\nu/|\varepsilon_x|$ (Slide 12). With 0.25 instead of 0.33 the axial strain is overestimated and $E$ comes out $0.25/0.33 = 0.76$ times the real value.

- a) The dependence is right but the effect is inverted: a smaller $\nu$ in $E = \sigma\nu/|\varepsilon_x|$ gives a smaller $E$.
- c) The effect is right but the reason is inverted: for a fixed contraction, $E$ is proportional to $\nu$.
- d) $\nu$ is needed to turn the measured transverse strain into the axial strain.

### Source

Session 11, Slides 12 and 19.

## Q21.4 Poisson's ratio from E and G

- id: B21-Q4
- concept_id: u5-shear-modulus-relation
- format: numeric
- asks: application
- calc: 207/(2*80) - 1

A steel has $E$ = 207 GPa and a shear modulus $G$ = 80 GPa. Determine its Poisson's ratio:

a) 0.294
b) 0.773
c) 1.29
d) 1.59

### Answer

a

### Explanation

Session 11, Slide 7: $E = 2G(1 + \nu)$, so $\nu = E/(2G) - 1 = 207/160 - 1 = 0.294$, inside the range 0.25-0.4 of metals (Slide 19).

- b) The ratio $2G/E$ was taken as $\nu$; it is $1/(1 + \nu)$.
- c) The 1 was not subtracted: $E/(2G) = 1.29$ is $1 + \nu$.
- d) The factor 2 was left out: $E/G - 1$.

### Source

Session 11, Slides 7 and 19.

## Q21.5 Test for a ceramic brick

- id: B21-Q5
- concept_id: u5-compression-test
- format: identify
- asks: application

Which test of the course best characterises a ceramic brick that carries the weight of a wall?

a) Rockwell hardness test
b) Compression test
c) Impact test
d) Torsion test

### Answer

b

### Explanation

Session 11, Slide 5: the compression test is applied to materials with a fragile behaviour, such as concrete, and is widely applied to ceramics; tests are chosen to replicate the service conditions (Slide 3).

- a) Hardness measures the surface resistance to indentation, not the strength of the whole piece under load.
- c) The impact test measures the energy absorbed until fracture under a blow, not the response to a steady compressive load.
- d) Torsion applies a twisting moment, a shear state; the brick carries a compressive load.

### Source

Session 11, Slides 3, 5 and 7; Session 12, Slide 15.

## Q21.6 What the impact test measures

- id: B21-Q6
- concept_id: u5-impact-test
- format: complete-sentence
- asks: definition

The impact test determines:

a) stiffness, as the slope of the elastic zone
b) hardness, as the resistance to indentation
c) the yield strength under a sudden load
d) toughness, as the energy absorbed until fracture

### Answer

d

### Explanation

Session 11, Slide 5: the impact test "determines toughness as the energy absorbed by a material until fracture"; a pendulum hammer strikes a notched specimen.

- a) Stiffness is Young's modulus, read from the tension test (Slide 12).
- b) Hardness is measured with indenters (Brinell, Vickers, Rockwell), not with a pendulum.
- c) The pendulum test gives an energy, not a stress at which plastic deformation begins.

### Source

Session 11, Slides 5 and 12; Session 12, Slide 15.

## Q21.7 Izod against Charpy

- id: B21-Q7
- concept_id: u5-impact-test
- format: identify
- asks: comparison

Which feature distinguishes the Izod impact test from the Charpy impact test?

a) The presence of a notch in the specimen
b) The use of a pendulum hammer
c) The property that the test measures
d) How the notched specimen is held

### Answer

d

### Explanation

Session 11, Slide 5: in the Izod test the notched specimen is clamped vertically, in the Charpy test it is supported horizontally; both are struck by a pendulum and measure the energy absorbed.

- a) Both specimens are notched.
- b) Both tests break the specimen with a pendulum hammer.
- c) Both measure toughness, the energy absorbed until fracture.

### Source

Session 11, Slide 5.

## Q21.8 Modulus of rupture of a ceramic bar

- id: B21-Q8
- concept_id: u5-bend-test
- format: numeric
- asks: calculation
- calc: 3*750*40/(2*10*5**2)

A ceramic bar 10 mm wide and 5.0 mm thick breaks under 750 N in a three-point bend test with a 40 mm span. Determine its modulus of rupture:

a) 90 MPa
b) 120 MPa
c) 180 MPa
d) 900 MPa

### Answer

c

### Explanation

Session 11, Slide 6: $\text{MOR} = \dfrac{3FL}{2bh^2} = \dfrac{3 \times 750 \times 40}{2 \times 10 \times 5.0^2} = \dfrac{90\,000}{500} = 180$ MPa.

- a) Width and thickness were swapped: $3FL/(2hb^2)$ with $b = 10$ squared.
- b) The factor $3/2$ was left out: $FL/(bh^2)$.
- d) The thickness was not squared: $3FL/(2bh)$.

### Source

Session 11, Slide 6.

## Q21.9 Shear stress in a shear test

- id: B21-Q9
- concept_id: u5-shear-torsion-test
- format: numeric
- asks: calculation
- calc: 26000*0.05/20

In an elastic shear test on an aluminium alloy ($G$ = 26 GPa, $E$ = 69 GPa), a 20 mm high block slides 0.05 mm. Determine the shear stress:

a) 0.0650 MPa
b) 65.0 MPa
c) 173 MPa
d) 6500 MPa

### Answer

b

### Explanation

Session 11, Slide 7: $\gamma = a/h = 0.05/20 = 0.0025$ and, in the elastic regime, $\tau = G\gamma = 26\,000 \times 0.0025 = 65.0$ MPa.

- a) The shear modulus was kept in GPa while the stress is given in MPa, a factor of 1000 too small.
- c) Young's modulus was used instead of the shear modulus: $69\,000 \times 0.0025$.
- d) The shear strain was written in percent (0.25) and used as a fraction.

### Source

Session 11, Slide 7.

## Q21.10 Variables of the torsion test

- id: B21-Q10
- concept_id: u5-shear-torsion-test
- format: complete-sentence
- asks: definition

In the torsion test, the shear stress and the shear strain are functions of:

a) the torque and the angle of twist
b) the axial load and the elongation
c) the indentation load and its depth
d) the absorbed energy and the notch

### Answer

a

### Explanation

Session 11, Slide 7: torsion is a variant of the shear test in which a twisting force rotates the bar; $\tau = f(F_{\text{torsion}})$ and $\gamma = f(\phi)$.

- b) These are the variables of the tension test.
- c) These are the variables of the Rockwell hardness test.
- d) These belong to the impact test, which measures toughness.

### Source

Session 11, Slides 5, 7 and 9; Session 12, Slide 22.
