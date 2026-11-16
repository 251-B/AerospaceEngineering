---
materia: Aerospace Materials I
tema: "Unit 5: Poisson's ratio, lateral contraction, modulus from the contraction and shear modulus"
bank_id: B20
title: "Poisson's ratio, lateral contraction and the shear modulus"
category: mt2_test_block
unit: 5
concepts:
  - u5-poisson-definition
  - u5-poisson-lateral-contraction
  - u5-modulus-from-poisson-contraction
  - u5-shear-modulus-relation
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 11, Slides 7, 12 and 19."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-5
---

# Bank B20 — Poisson's ratio, lateral contraction and the shear modulus

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 11, Slides 7, 12 and 19.

## Q20.1 Definition of Poisson's ratio

- id: B20-Q1
- concept_id: u5-poisson-definition
- format: complete-sentence
- asks: definition

Poisson's ratio of an isotropic material under uniaxial stress is:

a) minus the transverse strain over the axial stress
b) minus the axial strain over the transverse strain
c) minus the transverse strain over the axial strain
d) the shear stress over the shear strain

### Answer

c

### Explanation

Session 11, Slide 19: $\nu = -\varepsilon_{\text{transverse}}/\varepsilon_{\text{longitudinal}} = -\varepsilon_x/\varepsilon_z = -\varepsilon_y/\varepsilon_z$ for a uniaxial stress on an isotropic material.

- a) A strain divided by a stress has units of 1/MPa; Poisson's ratio relates two strains and has no units.
- b) The ratio is inverted; with it, metals would have values between 2.5 and 4 instead of 0.25 to 0.4.
- d) This ratio is the shear modulus $G$ of the shear test (Slide 7), not Poisson's ratio.

### Source

Session 11, Slides 7 and 19.

## Q20.2 Poisson's ratio of an incompressible material

- id: B20-Q2
- concept_id: u5-poisson-definition
- format: identify
- asks: classification

Which value of Poisson's ratio corresponds to a perfectly incompressible material, with no change in volume?

a) $\nu = 0.25$
b) $\nu = 0$
c) $\nu = 0.5$
d) $\nu = -1$

### Answer

c

### Explanation

Session 11, Slide 19: "ideal materials: $\nu = 0.5$ (perfect incompressible materials, no change in volume)"; real materials have $\nu = 0.2$ to 0.4.

- a) 0.25 is the lower end of the range of metals, which do change volume slightly under load.
- b) With $\nu = 0$ the section would not shrink at all, so the volume would grow with the elongation.
- d) The slide gives $\nu = -1$ as the case with no change in the aspect ratio, not in the volume.

### Source

Session 11, Slide 19.

## Q20.3 Poisson's ratio of real materials

- id: B20-Q3
- concept_id: u5-poisson-definition
- format: true-statement
- asks: comparison

Which one of the following statements about Poisson's ratio of real materials is TRUE?

a) Metals have values close to 0.5
b) Polymers have lower values than metals
c) Real materials have negative values
d) Natural rubber has a value close to 0.5

### Answer

d

### Explanation

Session 11, Slide 19: natural rubber 0.499-0.49, polymers 0.3-0.45, metals 0.25-0.4.

- a) Metals are at 0.25-0.4 on the slide; the value close to 0.5 is that of natural rubber.
- b) The order is inverted: polymers 0.3-0.45, metals 0.25-0.4.
- c) The slide gives positive values (0.2 to 0.4) for real materials; under tension their section shrinks.

### Source

Session 11, Slide 19.

## Q20.4 Reduction in diameter of a steel rod

- id: B20-Q4
- concept_id: u5-poisson-lateral-contraction
- format: numeric
- asks: calculation
- calc: 30000/(pi*6**2)/207000*0.30*12

A steel rod of 12 mm diameter ($E$ = 207 GPa, $\nu$ = 0.30) carries an elastic load of 30 kN. Determine the reduction in its diameter:

a) $1.15\times10^{-3}$ mm
b) $4.61\times10^{-3}$ mm
c) $1.54\times10^{-2}$ mm
d) $5.13\times10^{-2}$ mm

### Answer

b

### Explanation

$\sigma = 30\,000/(\pi\cdot 6^2) = 265.3$ MPa, $\varepsilon_z = \sigma/E = 1.28\times10^{-3}$ (Session 11, Slide 12), $\varepsilon_x = -\nu\,\varepsilon_z = -3.84\times10^{-4}$ (Slide 19), $\Delta d = \varepsilon_x d_0 = -3.84\times10^{-4}\times 12 = -4.61\times10^{-3}$ mm.

- a) The diameter was used as the radius, so the area is four times too large and the strain four times too small.
- c) Poisson's ratio was left out: the axial strain was applied to the diameter.
- d) The axial strain was divided by $\nu$ instead of being multiplied by it.

### Source

Session 11, Slides 9, 12 and 19.

## Q20.5 Diameter of a stretched wire

- id: B20-Q5
- concept_id: u5-poisson-lateral-contraction
- format: what-happens
- asks: effect

A copper wire is stretched elastically along its axis. What will happen to its diameter:

a) It will increase by $\nu$ times the axial strain
b) It will stay constant, since only the length changes
c) It will decrease by the full axial strain
d) It will decrease by $\nu$ times the axial strain

### Answer

d

### Explanation

Session 11, Slide 19: "all elastic longitudinal deformation" produces a "dimensional transverse" change, $\varepsilon_x = -\nu\,\varepsilon_z$; with $\varepsilon_z > 0$ the diameter decreases.

- a) The sign is wrong: the minus sign in $\nu = -\varepsilon_x/\varepsilon_z$ means the section shrinks when the wire is stretched.
- b) Every elastic longitudinal deformation comes with a transverse one (Slide 19).
- c) Poisson's ratio was dropped; the transverse strain is only $\nu \approx 0.25$-0.4 times the axial one in metals.

### Source

Session 11, Slide 19.

## Q20.6 Poisson's ratio from a measurement

- id: B20-Q6
- concept_id: u5-poisson-lateral-contraction
- format: numeric
- asks: application
- calc: (4.8e-3/10.00)/1.5e-3

A bar of 10.00 mm diameter, at an axial strain of $1.5\times10^{-3}$, shows a diameter reduction of $4.8\times10^{-3}$ mm. Determine its Poisson's ratio:

a) $4.80\times10^{-4}$
b) 0.160
c) 0.320
d) 3.13

### Answer

c

### Explanation

$\varepsilon_x = \Delta d/d_0 = -4.8\times10^{-3}/10.00 = -4.8\times10^{-4}$ and $\nu = -\varepsilon_x/\varepsilon_z = 4.8\times10^{-4}/1.5\times10^{-3} = 0.320$ (Session 11, Slide 19), inside the range of metals.

- a) This is the transverse strain $\Delta d/d_0$; it was not divided by the axial strain.
- b) The change of diameter was halved as if it were a change of radius, but it was still divided by the full diameter.
- d) The ratio is inverted: axial strain over transverse strain, $1.5\times10^{-3}/4.8\times10^{-4}$.

### Source

Session 11, Slide 19.

## Q20.7 Modulus of a hypothetical alloy from its contraction

- id: B20-Q7
- concept_id: u5-modulus-from-poisson-contraction
- format: numeric
- asks: calculation
- calc: 15000/(pi*5**2)/((3.0e-3/10.0)/0.30)/1000

Determine the modulus of elasticity of a hypothetical alloy if a 15.0 kN tensile force reduces the 10.0 mm diameter of a bar elastically by $3.0\times10^{-3}$ mm, with Poisson's ratio 0.30:

a) 47.7 GPa
b) 191 GPa
c) 637 GPa
d) 2120 GPa

### Answer

b

### Explanation

$\varepsilon_x = 3.0\times10^{-3}/10.0 = 3.0\times10^{-4}$, $\varepsilon_z = \varepsilon_x/\nu = 1.0\times10^{-3}$ (Session 11, Slide 19); $\sigma = 15\,000/(\pi\cdot 5^2) = 191$ MPa; $E = \sigma/\varepsilon_z = 191\,000$ MPa $= 191$ GPa (Slide 12).

- a) The diameter was used as the radius in the area, which makes the stress four times too small.
- c) Poisson's ratio was left out: the transverse strain $3.0\times10^{-4}$ was used as the axial strain.
- d) The transverse strain was multiplied by $\nu$ instead of divided by it, giving $\varepsilon_z = 9\times10^{-5}$.

### Source

Session 11, Slides 9, 12 and 19.

## Q20.8 Same contraction, different Poisson's ratio

- id: B20-Q8
- concept_id: u5-modulus-from-poisson-contraction
- format: complete-sentence
- asks: comparison

Two bars under the same tensile stress show the same transverse strain; the bar with the larger Poisson's ratio has:

a) the higher Young's modulus
b) the same Young's modulus
c) the lower Young's modulus
d) the larger axial strain

### Answer

a

### Explanation

From $\nu = -\varepsilon_x/\varepsilon_z$ (Session 11, Slide 19), $\varepsilon_z = -\varepsilon_x/\nu$; with Hooke's law $E = \sigma/\varepsilon_z = \sigma\,\nu/|\varepsilon_x|$ (Slide 12). For the same $\sigma$ and $\varepsilon_x$, $E$ grows with $\nu$.

- b) Equal transverse strains do not mean equal axial strains: $\varepsilon_z = -\varepsilon_x/\nu$ depends on $\nu$.
- c) Inverted: with the same transverse strain, a larger $\nu$ means a smaller axial strain, so $E = \sigma/\varepsilon_z$ is larger.
- d) Inverted: $\varepsilon_z = -\varepsilon_x/\nu$ is smaller when $\nu$ is larger.

### Source

Session 11, Slides 12 and 19.

## Q20.9 Shear modulus of an aluminium alloy

- id: B20-Q9
- concept_id: u5-shear-modulus-relation
- format: numeric
- asks: calculation
- calc: 69/(2*(1+0.33))

Determine the shear modulus of an aluminium alloy with $E$ = 69 GPa and Poisson's ratio 0.33:

a) 25.9 GPa
b) 51.9 GPa
c) 105 GPa
d) 184 GPa

### Answer

a

### Explanation

Session 11, Slide 7: $E = 2G(1 + \nu)$, so $G = E/[2(1 + \nu)] = 69/(2 \times 1.33) = 25.9$ GPa.

- b) The factor 2 was left out: $69/1.33$.
- c) $1 + \nu$ was replaced by $\nu$: $69/(2 \times 0.33)$.
- d) The relation was inverted: $G = 2E(1 + \nu)$ instead of $E = 2G(1 + \nu)$.

### Source

Session 11, Slide 7.

## Q20.10 Hooke's law in shear

- id: B20-Q10
- concept_id: u5-shear-modulus-relation
- format: complete-sentence
- asks: definition

In the elastic regime of a shear test:

a) the shear stress is $G$ times the axial strain
b) the shear stress is $E$ times the shear strain
c) the shear strain is $G$ times the shear stress
d) the shear stress is $G$ times the shear strain

### Answer

d

### Explanation

Session 11, Slide 7: $\tau = F/A_0$, $\gamma = a/h = \tan\theta$ and, in the elastic regime, $\tau = G\gamma$, with $G$ the shear modulus.

- a) The shear strain is $\gamma = a/h = \tan\theta$, the sliding over the height, not an axial strain.
- b) $E$ relates normal stress and strain; in shear the constant is $G$, with $E = 2G(1+\nu)$.
- c) The relation is inverted: $G$ has units of stress, so it multiplies the strain, not the stress.

### Source

Session 11, Slide 7.
