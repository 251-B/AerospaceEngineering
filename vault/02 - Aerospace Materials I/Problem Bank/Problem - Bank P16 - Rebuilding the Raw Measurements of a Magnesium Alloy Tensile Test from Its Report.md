---
materia: Aerospace Materials I
tema: "Unit 5: tensile test"
bank_id: P16
title: "Rebuilding the raw measurements of a magnesium alloy tensile test from its report"
category: mt2_problem
archetype: tensile-test
level: trap
unit: 5
difficulty: 3
points: 2.0
time_minutes: 15
official: false
origen: "Problem written for the bank in the style of the finals of January 2013 (question 7) and January 2014 (question 2) in MATERIALS_FINALEXAM_COMPILATION_2013-2017.pdf, worked backwards from the results to the measurements; not an official exercise. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - tensile-test
  - yield-strength
  - ductility
  - true-stress
---

# Bank P16 — Rebuilding the raw measurements of a magnesium alloy tensile test

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the magnesium tensile tests of the finals of January 2013 and January 2014, but worked backwards: the report gives the results and the student must recover the loads and the lengths and diameters the machine and the calliper would have measured. Each definition of the slides is solved for the measurement instead of the property. Method: Session 11, Slides 9, 12, 28, 30, 32, 33, 37-38. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

The raw data sheet of a tensile test on a round magnesium alloy specimen (initial diameter 9.00 mm, initial gauge length 45.00 mm) has been lost. The report only keeps the results: modulus of elasticity 45 GPa, yield strength (0.2 % offset) 170 MPa, tensile strength 255 MPa reached at an engineering strain of 0.080, elongation after fracture 11.0 % and reduction in area 13.0 %.

## Setup

#### Data

| Quantity | Symbol | Value | In SI |
| :--- | :--- | ---: | ---: |
| Initial diameter | $d_0$ | 9.00 mm | $9.00\times10^{-3}$ m |
| Initial gauge length | $l_0$ | 45.00 mm | $4.500\times10^{-2}$ m |
| Modulus of elasticity | $E$ | 45 GPa | $4.5\times10^{10}$ Pa $= 45\,000$ MPa |
| Yield strength (0.2 % offset) | $\sigma_y$ | 170 MPa | $1.70\times10^{8}$ Pa |
| Tensile strength | $\sigma_{TS}$ | 255 MPa | $2.55\times10^{8}$ Pa |
| Engineering strain at the maximum load | $\varepsilon_u$ | 0.080 | (dimensionless) |
| Elongation after fracture | $EL$ | 11.0 % | 0.110 |
| Reduction in area | $RA$ | 13.0 % | 0.130 |

Initial area, with the conversion written out:

$$A_0 = \frac{\pi d_0^2}{4} = \frac{\pi\,(9.00\ \text{mm})^2}{4} = \frac{\pi\times81.00\ \text{mm}^2}{4} = 63.62\ \text{mm}^2 = 6.362\times10^{-5}\ \text{m}^2$$

A stress in MPa times an area in mm² gives N, because $1\ \text{MPa} = 1\ \text{N/mm}^2$.

#### Model

- $\sigma = F/A_0$ and $\varepsilon = (l - l_0)/l_0$ [Session 11 Slide 9]; Hooke's law $\sigma = E\varepsilon$ [Session 11 Slide 12].
- 0.2 % offset: the yield point lies on the line $\sigma = E(\varepsilon - 0.002)$ [Session 11 Slide 28].
- $EL\,(\%) = \dfrac{l_f - l_0}{l_0}\times100$ [Session 11 Slide 32] and $RA\,(\%) = \dfrac{A_0 - A_f}{A_0}\times100$ [Session 11 Slide 33].
- Constant volume before necking, $A_0 l_0 = A_i l_i$, and $\sigma_T = F/A_i$ [Session 11 Slides 37-38].
- Hypothesis: the deformation is uniform up to the maximum load, where necking starts [Session 11 Slide 30].

## (a) Find the load at the yield strength, the maximum load, and the gauge length the extensometer read at the yield point [1.0 pts]

### Hint

The yield point is not on the elastic line: its strain is the 0.002 offset plus the elastic strain $\sigma_y/E$.

### Checkpoint

- $F_y = 10\,815$ N, $F_{\max} = 16\,222$ N
- $\varepsilon$ at the yield point $= 0.005778$
- $l_y = 45.260$ mm

### Solution

#### Loads from the stresses

The engineering stress is $\sigma = F/A_0$ [Session 11 Slide 9]; multiplying both sides by $A_0$ isolates the load, $F = \sigma A_0$:

$$F_y = \sigma_y\,A_0 = 170\ \text{N/mm}^2\times63.62\ \text{mm}^2 = 10\,815\ \text{N}$$

$$F_{\max} = \sigma_{TS}\,A_0 = 255\ \text{N/mm}^2\times63.62\ \text{mm}^2 = 16\,222\ \text{N}$$

#### Strain at the yield point from the offset line

The conventional yield point is where the curve meets the line parallel to the elastic one from $\varepsilon = 0.002$ [Session 11 Slide 28], so its coordinates satisfy $\sigma_y = E(\varepsilon_Y - 0.002)$. Dividing by $E$ and then adding 0.002 to both sides:

$$\varepsilon_Y - 0.002 = \frac{\sigma_y}{E} \qquad\Rightarrow\qquad \varepsilon_Y = 0.002 + \frac{\sigma_y}{E} = 0.002 + \frac{170\ \text{MPa}}{45\,000\ \text{MPa}} = 0.002 + 0.003778 = 0.005778$$

The total strain at that point is the plastic offset plus the elastic part, as the figure shows; the total strain before fracture is always $\varepsilon_t = \varepsilon_e + \varepsilon_p$ [Session 11 Slide 32].

![[attachments/MAT-MT2/p16-offset-split.svg]]

#### Gauge length at the yield point

From $\varepsilon = (l - l_0)/l_0$, multiplying by $l_0$ and adding $l_0$: $l = l_0\,(1 + \varepsilon)$.

$$l_y = l_0\,(1 + \varepsilon_Y) = 45.00\ \text{mm}\times1.005778 = 45.260\ \text{mm}$$

The extensometer read an elongation of 0.260 mm. A student who places the yield point on the elastic line ($\varepsilon = 0.003778$) would rebuild 45.170 mm, missing the 0.090 mm of plastic offset.

## (b) Rebuild the gauge length and the neck diameter measured after fracture, and the diameter and true stress of the specimen at the maximum load [1.0 pts]

### Hint

Solve the definitions of %EL and %RA for $l_f$ and $A_f$. At the maximum load the deformation is still uniform, so constant volume gives the area from the length.

### Checkpoint

- $l_f = 49.95$ mm, $A_f = 55.35$ mm², $d_f = 8.39$ mm
- At the maximum load: $d = 8.66$ mm, $\sigma_T = 275.4$ MPa

### Solution

#### Gauge length after fracture from %EL

From $EL = (l_f - l_0)/l_0$ (as a fraction, 0.110), multiplying by $l_0$ and adding $l_0$:

$$l_f = l_0\,(1 + EL) = 45.00\ \text{mm}\times(1 + 0.110) = 49.95\ \text{mm}$$

This is the distance between the marks with the two halves fitted together, after the elastic recovery [Session 11 Slide 32].

#### Neck diameter from %RA

From $RA = (A_0 - A_f)/A_0$ (0.130 as a fraction), multiplying by $A_0$ and isolating $A_f$:

$$A_f = A_0\,(1 - RA) = 63.62\ \text{mm}^2\times(1 - 0.130) = 63.62\ \text{mm}^2\times0.870 = 55.35\ \text{mm}^2$$

The area of a circle is $\pi d^2/4$, so $d_f = \sqrt{4A_f/\pi}$; the factor $\pi/4$ cancels against that of $A_0$, which gives directly

$$d_f = d_0\,\sqrt{1 - RA} = 9.00\ \text{mm}\times\sqrt{0.870} = 9.00\ \text{mm}\times0.9327 = 8.39\ \text{mm}$$

#### Diameter at the maximum load from constant volume

Up to the maximum load the deformation is uniform and the volume of the gauge length does not change [Session 11 Slide 38]: $A_0 l_0 = A_u l_u$. Isolating the area and writing $l_u/l_0 = 1 + \varepsilon_u$:

$$A_u = \frac{A_0\,l_0}{l_u} = \frac{A_0}{1 + \varepsilon_u} = \frac{63.62\ \text{mm}^2}{1.080} = 58.90\ \text{mm}^2$$

and, with $A \propto d^2$, $d_u = d_0/\sqrt{1 + \varepsilon_u} = 9.00\ \text{mm}/\sqrt{1.080} = 8.66$ mm.

#### True stress at the maximum load

The true stress is the load over the instantaneous area [Session 11 Slide 37]:

$$\sigma_{T,u} = \frac{F_{\max}}{A_u} = \frac{16\,222\ \text{N}}{58.90\ \text{mm}^2} = 275.4\ \text{MPa}$$

the same as $\sigma_{TS}(1 + \varepsilon_u) = 255\ \text{MPa}\times1.080 = 275.4$ MPa, as it must be, since both come from constant volume.

## Interpretation

- **Consistency of the report.** The neck diameter after fracture (8.39 mm) is smaller than the uniform diameter at the maximum load (8.66 mm): the neck kept thinning after the maximum, as it must [Session 11 Slide 30]. And $l_f = 49.95$ mm is longer than the length at the maximum, $45.00\times1.080 = 48.60$ mm, because the neck added plastic elongation even though the elastic part was recovered.
- **Order of magnitude.** $E = 45$ GPa is the magnesium value of the slide's table [Session 11 Slide 17]; magnesium is hcp, with 6 slip systems against 12 for fcc and bcc [Session 11 Slide 25]. **Extension** (not on the slides): fewer slip systems usually mean less ductility, which fits the small %RA of 13 %.
- **Limiting case.** If $RA \to 0$ (no neck), $d_f \to d_0$; if $\varepsilon_u \to 0$, $d_u \to d_0$ and $\sigma_T \to \sigma$.
- **Dimensions.** $F = \sigma A_0$ is Pa·m² = N; $l_0(1 + \varepsilon)$ is m; $d_0\sqrt{1 - RA}$ is m; $F/A_u$ is Pa.
- **Common exam mistake.** Getting the diameter after fracture as $d_0(1 - RA)$ = 7.83 mm: %RA is a reduction of the area, so the diameter scales with the square root.

## Verification

- A0 (mm2) | pi*9.00**2/4 | 63.62
- F_y (N) | 170*pi*9.00**2/4 | 10815
- F_max (N) | 255*pi*9.00**2/4 | 16222
- eps_e at yield | 170/45000 | 0.003778
- eps at Y | 0.002+170/45000 | 0.005778
- l_y (mm) | 45.00*(1+0.002+170/45000) | 45.260
- l on elastic line (mm) | 45.00*(1+170/45000) | 45.170
- l_f (mm) | 45.00*(1+0.110) | 49.95
- A_f (mm2) | pi*9.00**2/4*(1-0.130) | 55.35
- sqrt(0.870) | sqrt(1-0.130) | 0.9327
- d_f (mm) | 9.00*sqrt(1-0.130) | 8.39
- A_u (mm2) | pi*9.00**2/4/1.080 | 58.90
- d_u (mm) | 9.00/sqrt(1.080) | 8.66
- true stress at max (MPa) | 255*pi*9.00**2/4/(pi*9.00**2/4/1.080) | 275.4
- length at max (mm) | 45.00*1.080 | 48.60
- wrong d_f (mm) | 9.00*(1-0.130) | 7.83

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
