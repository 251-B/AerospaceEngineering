---
materia: Aerospace Materials I
tema: "Unit 5: loaded bar"
bank_id: P17
title: "Nickel alloy tie rod under a tensile load"
category: mt2_problem
archetype: loaded-bar
level: standard
unit: 5
difficulty: 1
points: 2.0
time_minutes: 15
official: false
origen: "Problem written for the bank in the style of the final of January 2017 (question 5) in MATERIALS_FINALEXAM_2017_ORD.pdf; not an official exercise. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - loaded-bar
---

# Bank P17 — Nickel alloy tie rod under a tensile load

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the final of January 2017 (question 5). Method: Session 11, Slides 9, 10, 12 and 19. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

A tie rod of the engine mount of a light aircraft is a solid cylinder of a nickel alloy, 8.0 mm in diameter and 350 mm long. In service it is pulled along its axis by a force of 9.5 kN. The alloy has a Young's modulus of 207 GPa (the value of nickel in the table of the slides), a yield strength of 280 MPa and a Poisson's ratio of 0.31.

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| Initial diameter | $d_0$ | 8.0 mm | $8.0\times10^{-3}$ m |
| Initial length | $l_0$ | 350 mm | 0.350 m |
| Axial force | $F$ | 9.5 kN | $9.5\times10^{3}$ N |
| Young's modulus | $E$ | 207 GPa | $207\times10^{9}$ Pa |
| Yield strength | $\sigma_y$ | 280 MPa | $280\times10^{6}$ Pa |
| Poisson's ratio | $\nu$ | 0.31 | dimensionless |

#### Model

- Engineering stress and strain: $\sigma = F/A_0$ and $\varepsilon = (l - l_0)/l_0 = \Delta l/l_0$ [Session 11, Slide 9].
- Elastic zone $\sigma < \sigma_y$, plastic zone $\sigma > \sigma_y$ [Session 11, Slide 10].
- Hooke's law in the elastic zone, $\sigma = E\,\varepsilon$ [Session 11, Slide 12].
- Poisson's ratio, $\nu = -\varepsilon_{\text{transverse}}/\varepsilon_{\text{longitudinal}}$ [Session 11, Slide 19].
- Hypotheses: uniform uniaxial stress over the cross-section, isotropic material, no change of $A_0$ used in the stress (engineering stress).

## (a) Does the rod deform plastically under the 9.5 kN load? Justify the answer. [0.8 pts]

### Hint

Compute the engineering stress on the initial cross-section and compare it with the yield strength.

### Checkpoint

- $A_0 = 5.027\times10^{-5}$ m²
- $\sigma = 189.0$ MPa $< \sigma_y = 280$ MPa: elastic, no plastic deformation
- Ratio $\sigma_y/\sigma = 1.48$

### Solution

#### Area of the cross-section, with the diameter in metres

The stress needs the initial area of the circular section. The diameter is first converted to metres, $d_0 = 8.0\ \text{mm} = 8.0\times10^{-3}\ \text{m}$, and then:

$$A_0 = \frac{\pi d_0^2}{4} = \frac{\pi\,(8.0\times10^{-3}\ \text{m})^2}{4} = \frac{\pi\times 6.4\times10^{-5}\ \text{m}^2}{4} = 5.027\times10^{-5}\ \text{m}^2$$

#### Engineering stress produced by the force

The force is converted to newtons, $F = 9.5\ \text{kN} = 9.5\times10^{3}\ \text{N}$. The engineering stress is the force over the initial area [Session 11, Slide 9]:

$$\sigma = \frac{F}{A_0} = \frac{9.5\times10^{3}\ \text{N}}{5.027\times10^{-5}\ \text{m}^2} = 1.890\times10^{8}\ \text{Pa} = 189.0\ \text{MPa}$$

#### Compare the stress with the yield strength

The rod deforms plastically only if the stress exceeds the yield strength [Session 11, Slide 10]. Here

$$\sigma = 189.0\ \text{MPa} < \sigma_y = 280\ \text{MPa}$$

so the rod stays in the elastic zone: **it does not deform plastically**, and all its deformation is recovered when the load is removed. The yield strength is $280/189.0 = 1.48$ times the applied stress.

## (b) Length and diameter of the rod while the load is applied. [1.2 pts]

### Hint

The rod is elastic, so Hooke's law gives the axial strain; Poisson's ratio gives the transverse strain, which has the opposite sign.

### Checkpoint

- $\varepsilon_z = 9.130\times10^{-4}$, $\Delta l = 0.3196$ mm, $l = 350.320$ mm
- $\varepsilon_x = -2.830\times10^{-4}$, $\Delta d = -2.264\times10^{-3}$ mm, $d = 7.9977$ mm

### Solution

#### Axial strain from Hooke's law

Part (a) showed that the rod is elastic, so Hooke's law applies [Session 11, Slide 12]. Isolating the strain from $\sigma = E\,\varepsilon_z$ (divide both sides by $E$):

$$\varepsilon_z = \frac{\sigma}{E} = \frac{189.0\times10^{6}\ \text{Pa}}{207\times10^{9}\ \text{Pa}} = 9.130\times10^{-4}$$

#### Length under the load

From the definition $\varepsilon_z = \Delta l/l_0$ [Session 11, Slide 9], multiplying both sides by $l_0$ gives the elongation:

$$\Delta l = \varepsilon_z\,l_0 = 9.130\times10^{-4}\times 350\ \text{mm} = 0.3196\ \text{mm}$$

$$l = l_0 + \Delta l = 350\ \text{mm} + 0.3196\ \text{mm} = 350.320\ \text{mm}$$

#### Transverse strain from Poisson's ratio

A longitudinal elastic stretch comes with a transverse contraction [Session 11, Slide 19]. From $\nu = -\varepsilon_x/\varepsilon_z$, multiplying both sides by $-\varepsilon_z$:

$$\varepsilon_x = -\nu\,\varepsilon_z = -0.31\times 9.130\times10^{-4} = -2.830\times10^{-4}$$

#### Diameter under the load

The transverse strain is the relative change of the diameter, $\varepsilon_x = \Delta d/d_0$, so

$$\Delta d = \varepsilon_x\,d_0 = -2.830\times10^{-4}\times 8.0\ \text{mm} = -2.264\times10^{-3}\ \text{mm}$$

$$d = d_0 + \Delta d = 8.0\ \text{mm} - 0.002264\ \text{mm} = 7.9977\ \text{mm}$$

The diameter shrinks by about 2.3 µm while the length grows by about 0.32 mm.

## Interpretation

- The rod works at 189 MPa, two thirds of its yield strength, so the whole deformation is elastic and is recovered on unloading. If the same force acted on a rod of 6.0 mm, the stress would rise by $(8/6)^2$ to 336 MPa and the rod would yield: the check of part (a) must always come before Hooke's law.
- Control case: with $\nu = 0$ the diameter would not change; with $\nu = 0.5$ (incompressible, Slide 19) the contraction would be $-4.57\times10^{-4}$, larger than the one found. The value 0.31 lies in the range 0.25 to 0.4 of metals in the slide.
- SI check: $\sigma = F/A_0$ in N/m² = Pa; $\varepsilon = \sigma/E$ in Pa/Pa, dimensionless; $\Delta l = \varepsilon\,l_0$ and $\Delta d = \varepsilon_x d_0$ in metres.
- Common mistake: using the radius in place of the diameter in $\pi d_0^2/4$, or forgetting the minus sign of the transverse strain and giving a diameter that grows under tension.

## Verification

- A0 (m^2) | pi*(8.0e-3)**2/4 | 5.027e-5
- sigma (MPa) | 9.5e3/(pi*(8.0e-3)**2/4)/1e6 | 189.0
- ratio sigma_y/sigma | 280/(9.5e3/(pi*(8.0e-3)**2/4)/1e6) | 1.48
- eps_z | 9.5e3/(pi*(8.0e-3)**2/4)/207e9 | 9.130e-4
- Delta l (mm) | 9.5e3/(pi*(8.0e-3)**2/4)/207e9*350 | 0.3196
- l (mm) | 350+9.5e3/(pi*(8.0e-3)**2/4)/207e9*350 | 350.320
- eps_x | -0.31*9.5e3/(pi*(8.0e-3)**2/4)/207e9 | -2.830e-4
- Delta d (mm) | -0.31*9.5e3/(pi*(8.0e-3)**2/4)/207e9*8.0 | -2.264e-3
- d (mm) | 8.0-0.31*9.5e3/(pi*(8.0e-3)**2/4)/207e9*8.0 | 7.9977
- 6 mm rod stress (MPa) | 9.5e3/(pi*(6.0e-3)**2/4)/1e6 | 336
- eps_x with nu=0.5 | -0.5*9.5e3/(pi*(8.0e-3)**2/4)/207e9 | -4.57e-4

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
