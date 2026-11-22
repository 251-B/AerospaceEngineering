---
materia: Aerospace Materials I
tema: "Unit 5: loaded bar"
bank_id: P18
title: "Choosing the alloy of a light control rod"
category: mt2_problem
archetype: loaded-bar
level: standard
unit: 5
difficulty: 2
points: 2.0
time_minutes: 15
official: false
origen: "Problem written for the bank in the style of the final of January 2016 (question 5) in MATERIALS_FINALEXAM_2016_ORD_SOL.pdf; not an official exercise. The four alloys are hypothetical, with moduli taken from Session 11, Slide 17. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - loaded-bar
  - material-selection
---

# Bank P18 — Choosing the alloy of a light control rod

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the final of January 2016 (question 5); the alloys are hypothetical. Method: Session 11, Slides 9, 12, 19 and 29. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

A cylindrical control rod of an aircraft must be 250 mm long and 12 mm in diameter, and it carries an axial tensile load of 18 kN. The designer sets three requirements: (1) no yielding with a safety factor $N = 2$; (2) the diameter may not shrink by more than 10 µm under the load; (3) the rod may not weigh more than 150 g. Four alloys are available:

| Alloy | $E$ (GPa) | $\sigma_y$ (MPa) | $\nu$ | $\rho$ (g/cm³) |
| :--- | ---: | ---: | ---: | ---: |
| A, aluminium alloy | 69 | 300 | 0.33 | 2.7 |
| B, titanium alloy | 107 | 850 | 0.34 | 4.5 |
| C, steel | 207 | 480 | 0.30 | 7.8 |
| D, magnesium alloy | 45 | 220 | 0.29 | 1.8 |

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| Length | $l_0$ | 250 mm | 0.250 m |
| Diameter | $d_0$ | 12 mm | $12\times10^{-3}$ m |
| Axial force | $F$ | 18 kN | $18\times10^{3}$ N |
| Safety factor | $N$ | 2 | dimensionless |
| Largest diameter loss | $\lvert\Delta d\rvert_{\max}$ | 10 µm | $10\times10^{-6}$ m $= 10\times10^{-3}$ mm |
| Largest mass | $m_{\max}$ | 150 g | 0.150 kg |

Moduli in pascals: $1\ \text{GPa} = 10^{9}\ \text{Pa}$, $1\ \text{MPa} = 10^{6}\ \text{Pa}$. Densities: $1\ \text{g/cm}^3 = 10^{3}\ \text{kg/m}^3$, so for example $\rho_A = 2.7\ \text{g/cm}^3 = 2700\ \text{kg/m}^3$.

#### Model

- Engineering stress $\sigma = F/A_0$ [Session 11, Slide 9].
- Working stress $\sigma_w = \sigma_y/N$: the design keeps $\sigma \le \sigma_w$ [Session 11, Slide 29].
- Hooke's law $\sigma = E\,\varepsilon_z$ in the elastic zone [Session 11, Slide 12] and Poisson's ratio $\nu = -\varepsilon_x/\varepsilon_z$ [Session 11, Slide 19].
- Mass $m = \rho\,V$ with $V = A_0\,l_0$ for a cylinder (geometry).
- Hypotheses: uniform uniaxial stress; the dimensions are set, so the stress is the same for the four alloys; the deformation is elastic in every alloy that passes requirement (1).

## (a) Which alloys meet the requirement of no yielding with the safety factor? [0.8 pts]

### Hint

The stress does not depend on the material. Turn the safety factor into a minimum yield strength.

### Checkpoint

- $A_0 = 1.131\times10^{-4}$ m², $\sigma = 159.2$ MPa
- Required $\sigma_y \ge 318.3$ MPa: A (300) and D (220) are rejected; B and C pass

### Solution

#### Stress in the rod, the same for every alloy

The diameter in metres is $d_0 = 12\times10^{-3}$ m, so the initial area is

$$A_0 = \frac{\pi d_0^2}{4} = \frac{\pi\,(12\times10^{-3}\ \text{m})^2}{4} = 1.131\times10^{-4}\ \text{m}^2$$

and with $F = 18\ \text{kN} = 18\times10^{3}$ N the engineering stress is [Session 11, Slide 9]

$$\sigma = \frac{F}{A_0} = \frac{18\times10^{3}\ \text{N}}{1.131\times10^{-4}\ \text{m}^2} = 1.592\times10^{8}\ \text{Pa} = 159.2\ \text{MPa}$$

#### Turn the safety factor into a minimum yield strength

The rod is safe when the stress does not exceed the working stress, $\sigma \le \sigma_w = \sigma_y/N$ [Session 11, Slide 29]. Multiplying both sides by $N$ isolates the yield strength the alloy needs:

$$\sigma_y \ge N\,\sigma = 2\times 159.2\ \text{MPa} = 318.3\ \text{MPa}$$

#### Screen the four alloys

| Alloy | $\sigma_y$ (MPa) | $\sigma_y \ge 318.3$ MPa? |
| :--- | ---: | :--- |
| A | 300 | no, rejected (it would work with $N = 300/159.2 = 1.88$) |
| B | 850 | yes |
| C | 480 | yes |
| D | 220 | no, rejected ($N = 220/159.2 = 1.38$) |

Only **B and C** meet the requirement of no yielding with $N = 2$. Alloy A would not yield (300 > 159.2 MPa), but its margin is below the one demanded.

## (b) Check the diameter change and the mass of the remaining alloys and choose the material. [1.2 pts]

### Hint

The stress is below the yield strength of B and C, so Hooke's law and Poisson's ratio give the diameter change. The volume is the same for every alloy.

### Checkpoint

- $\Delta d_B = -6.07$ µm, $\Delta d_C = -2.77$ µm: both within 10 µm
- $V = 28.27$ cm³; $m_B = 127.2$ g, $m_C = 220.5$ g: C is rejected by mass
- Chosen: alloy B (titanium), elongation $\Delta l_B = 0.372$ mm

### Solution

#### Diameter change from Hooke's law and Poisson's ratio

B and C are elastic at 159.2 MPa (part a). Hooke's law gives $\varepsilon_z = \sigma/E$ [Session 11, Slide 12]; Poisson's ratio gives $\varepsilon_x = -\nu\,\varepsilon_z$ [Session 11, Slide 19]; and $\Delta d = \varepsilon_x\,d_0$. Putting the three together, line by line:

$$\Delta d = \varepsilon_x\,d_0 = -\nu\,\varepsilon_z\,d_0 = -\nu\,\frac{\sigma}{E}\,d_0$$

For B, with $E = 107\times10^{9}$ Pa and $d_0 = 12$ mm:

$$\Delta d_B = -0.34\times\frac{159.2\times10^{6}\ \text{Pa}}{107\times10^{9}\ \text{Pa}}\times 12\ \text{mm} = -0.34\times 1.487\times10^{-3}\times 12\ \text{mm} = -6.07\times10^{-3}\ \text{mm} = -6.07\ \mu\text{m}$$

For C, with $E = 207\times10^{9}$ Pa:

$$\Delta d_C = -0.30\times\frac{159.2\times10^{6}\ \text{Pa}}{207\times10^{9}\ \text{Pa}}\times 12\ \text{mm} = -0.30\times 7.689\times10^{-4}\times 12\ \text{mm} = -2.77\ \mu\text{m}$$

Both losses are smaller than 10 µm, so B and C meet requirement (2).

#### Mass of the rod

The volume of the cylinder is the same for every alloy:

$$V = A_0\,l_0 = 1.131\times10^{-4}\ \text{m}^2\times 0.250\ \text{m} = 2.827\times10^{-5}\ \text{m}^3 = 28.27\ \text{cm}^3$$

using $1\ \text{m}^3 = 10^{6}\ \text{cm}^3$. With $m = \rho V$:

$$m_B = 4.5\ \text{g/cm}^3\times 28.27\ \text{cm}^3 = 127.2\ \text{g} \le 150\ \text{g}$$

$$m_C = 7.8\ \text{g/cm}^3\times 28.27\ \text{cm}^3 = 220.5\ \text{g} > 150\ \text{g}$$

Steel C is rejected by the mass limit.

#### Choice and summary of the rejections

| Alloy | Requirement (1), $\sigma_y \ge 318.3$ MPa | Requirement (2), $\lvert\Delta d\rvert \le 10$ µm | Requirement (3), $m \le 150$ g | Result |
| :--- | :--- | :--- | :--- | :--- |
| A | fails (300 MPa) | 9.13 µm | 76.3 g | rejected by (1) |
| B | 850 MPa | 6.07 µm | 127.2 g | **chosen** |
| C | 480 MPa | 2.77 µm | fails (220.5 g) | rejected by (3) |
| D | fails (220 MPa) | fails (12.31 µm) | 50.9 g | rejected by (1) and (2) |

The values of A and D in columns (2) and (3) are given only for completeness (computed with the same formulas). The rod is made of the **titanium alloy B**. Its elongation under the load is

$$\Delta l_B = \frac{\sigma}{E_B}\,l_0 = \frac{159.2\times10^{6}\ \text{Pa}}{107\times10^{9}\ \text{Pa}}\times 250\ \text{mm} = 0.372\ \text{mm}$$

## Interpretation

- The three requirements pull in different directions: steel is stiff and strong but heavy, the light alloys are too weak for $N = 2$, and the titanium alloy wins on strength per unit density. **Extension** (not on the slides): the specific strength $\sigma_y/\rho$ is the yield strength divided by the density; with the table it is about 111 (A), 189 (B), 61.5 (C) and 122 (D) MPa per g/cm³, so B is clearly ahead. On the specific modulus $E/\rho$ B is actually the lowest of the four (23.8 against 25.0 to 26.5 GPa per g/cm³): here stiffness is not the deciding property.
- D fails twice: a low yield strength and a low modulus (a large elastic strain, hence a large diameter loss). A low $E$ makes $\lvert\Delta d\rvert$ grow as $\nu/E$.
- Limiting check: the diameter loss of B, 6.07 µm, is $5\times10^{-4}$ of the diameter, a typical elastic strain of a metal, far below 1 %.
- SI check: $\nu\,\sigma\,d_0/E$ has units Pa·m/Pa = m; $\rho\,V$ in (kg/m³)·m³ = kg.
- Common mistake: rejecting A because "it yields". It does not yield at 159.2 MPa; it is rejected because its safety factor would be 1.88 < 2.

## Verification

- A0 (m^2) | pi*(12e-3)**2/4 | 1.131e-4
- sigma (MPa) | 18e3/(pi*(12e-3)**2/4)/1e6 | 159.2
- required sigma_y (MPa) | 2*18e3/(pi*(12e-3)**2/4)/1e6 | 318.3
- N of A | 300/(18e3/(pi*(12e-3)**2/4)/1e6) | 1.88
- N of D | 220/(18e3/(pi*(12e-3)**2/4)/1e6) | 1.38
- eps_z of B | 18e3/(pi*(12e-3)**2/4)/107e9 | 1.487e-3
- eps_z of C | 18e3/(pi*(12e-3)**2/4)/207e9 | 7.689e-4
- Delta d B (um) | -0.34*18e3/(pi*(12e-3)**2/4)/107e9*12e-3*1e6 | -6.07
- Delta d C (um) | -0.30*18e3/(pi*(12e-3)**2/4)/207e9*12e-3*1e6 | -2.77
- Delta d A (um) | 0.33*18e3/(pi*(12e-3)**2/4)/69e9*12e-3*1e6 | 9.13
- Delta d D (um) | 0.29*18e3/(pi*(12e-3)**2/4)/45e9*12e-3*1e6 | 12.31
- V (cm^3) | pi*(1.2)**2/4*25 | 28.27
- m B (g) | 4.5*pi*(1.2)**2/4*25 | 127.2
- m C (g) | 7.8*pi*(1.2)**2/4*25 | 220.5
- m A (g) | 2.7*pi*(1.2)**2/4*25 | 76.3
- m D (g) | 1.8*pi*(1.2)**2/4*25 | 50.9
- Delta l B (mm) | 18e3/(pi*(12e-3)**2/4)/107e9*250 | 0.372

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
