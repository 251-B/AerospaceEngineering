---
materia: Aerospace Materials I
tema: "Unit 5: loaded bar"
bank_id: P20
title: "Minimum diameter of a titanium hanger rod"
category: mt2_problem
archetype: loaded-bar
level: standard
unit: 5
difficulty: 2
points: 2.0
time_minutes: 15
official: false
origen: "Problem written for the bank in the style of the finals of June 2015 (question 3) and January 2015 (question 8) in MATERIALS_FINALEXAM_COMPILATION_2013-2017.pdf; not an official exercise. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - loaded-bar
  - safety-factor
  - resilience
---

# Bank P20 — Minimum diameter of a titanium hanger rod

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the finals of June 2015 (question 3) and January 2015 (question 8). Method: Session 11, Slides 9, 12, 29 and 35. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

In an engine test cell, a mass of 2400 kg hangs from a solid cylindrical rod of a titanium alloy, 1.20 m long. The alloy has $E = 107$ GPa and $\sigma_y = 880$ MPa, and the design uses a safety factor $N = 2.5$. Take $g = 9.81$ m/s².

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| Hanging mass | $m$ | 2400 kg | 2400 kg |
| Rod length | $l_0$ | 1.20 m | 1.20 m $= 1200$ mm |
| Young's modulus | $E$ | 107 GPa | $107\times10^{9}$ Pa |
| Yield strength | $\sigma_y$ | 880 MPa | $880\times10^{6}$ Pa |
| Safety factor | $N$ | 2.5 | dimensionless |
| Gravity | $g$ | 9.81 m/s² | 9.81 m/s² |

#### Model

- Weight of the mass $F = m\,g$ (it is the axial force on the rod at rest).
- Engineering stress $\sigma = F/A_0$ and strain $\varepsilon = \Delta l/l_0$ [Session 11, Slide 9].
- Working stress $\sigma_w = \sigma_y/N$ [Session 11, Slide 29].
- Hooke's law $\sigma = E\,\varepsilon$ [Session 11, Slide 12].
- Modulus of resilience $U_r = \int_0^{\varepsilon_y}\sigma\,d\varepsilon$ [Session 11, Slide 35].
- Hypotheses: uniform uniaxial stress; the weight of the rod is neglected against 2400 kg; linear elastic behaviour up to $\sigma_y$.

## (a) Minimum diameter of the rod. [0.8 pts]

### Hint

Turn the safety factor into the largest stress allowed, and isolate the area and then the diameter.

### Checkpoint

- $F = 23\,544$ N, $\sigma_w = 352$ MPa
- $A_{\min} = 6.689\times10^{-5}$ m², $d_{\min} = 9.23$ mm

### Solution

#### Load on the rod

The rod holds the mass at rest, so the axial force is its weight:

$$F = m\,g = 2400\ \text{kg}\times 9.81\ \text{m/s}^2 = 23\,544\ \text{N}$$

#### Largest stress allowed

The design keeps the stress at or below the working stress [Session 11, Slide 29]:

$$\sigma_w = \frac{\sigma_y}{N} = \frac{880\ \text{MPa}}{2.5} = 352\ \text{MPa} = 352\times10^{6}\ \text{Pa}$$

#### Minimum area and diameter

The condition is $\sigma = F/A_0 \le \sigma_w$. Multiplying both sides by $A_0$ and dividing by $\sigma_w$ isolates the area:

$$A_0 \ge \frac{F}{\sigma_w} = \frac{23\,544\ \text{N}}{352\times10^{6}\ \text{Pa}} = 6.689\times10^{-5}\ \text{m}^2$$

From $A_0 = \pi d_0^2/4$: multiply by 4, divide by $\pi$ and take the square root:

$$d_{\min} = \sqrt{\frac{4A_{\min}}{\pi}} = \sqrt{\frac{4\times 6.689\times10^{-5}\ \text{m}^2}{\pi}} = \sqrt{8.516\times10^{-5}\ \text{m}^2} = 9.228\times10^{-3}\ \text{m} = 9.23\ \text{mm}$$

## (b) The rod is made with the next whole millimetre, 10 mm. Find the real safety factor and the elongation of the rod under the load. [0.6 pts]

### Hint

The stress drops with the larger area; the safety factor is the ratio of the yield strength to the actual stress.

### Checkpoint

- $A_0 = 7.854\times10^{-5}$ m², $\sigma = 299.8$ MPa
- $N_{\text{real}} = 2.94$
- $\varepsilon = 2.802\times10^{-3}$, $\Delta l = 3.36$ mm

### Solution

#### Stress with the 10 mm rod

$$A_0 = \frac{\pi\,(10\times10^{-3}\ \text{m})^2}{4} = 7.854\times10^{-5}\ \text{m}^2 \qquad \sigma = \frac{F}{A_0} = \frac{23\,544\ \text{N}}{7.854\times10^{-5}\ \text{m}^2} = 299.8\ \text{MPa}$$

#### Real safety factor

From $\sigma_w = \sigma_y/N$ with the working stress equal to the actual stress, isolating $N$:

$$N_{\text{real}} = \frac{\sigma_y}{\sigma} = \frac{880\ \text{MPa}}{299.8\ \text{MPa}} = 2.94 \ge 2.5$$

#### Elongation

The rod is elastic ($\sigma < \sigma_y$), so Hooke's law gives the strain [Session 11, Slide 12], and $\Delta l = \varepsilon\,l_0$ the elongation:

$$\varepsilon = \frac{\sigma}{E} = \frac{299.8\times10^{6}\ \text{Pa}}{107\times10^{9}\ \text{Pa}} = 2.802\times10^{-3} \qquad \Delta l = 2.802\times10^{-3}\times 1200\ \text{mm} = 3.36\ \text{mm}$$

## (c) Derive the modulus of resilience of the alloy from its definition as an integral and evaluate it. [0.6 pts]

### Hint

Under the integral, replace $\sigma$ by Hooke's law; the antiderivative of $\varepsilon$ is $\varepsilon^2/2$.

### Checkpoint

- $\varepsilon_y = 8.224\times10^{-3}$
- $U_r = 3.619\times10^{6}$ J/m³ $= 3.619$ MPa

### Solution

#### Definition and upper limit

The modulus of resilience is the elastic energy per unit volume stored up to the yield point, the area under the curve from 0 to $\varepsilon_y$ [Session 11, Slide 35]. The upper limit follows from Hooke's law at the yield point, $\sigma_y = E\,\varepsilon_y$, divided by $E$:

$$\varepsilon_y = \frac{\sigma_y}{E} = \frac{880\times10^{6}\ \text{Pa}}{107\times10^{9}\ \text{Pa}} = 8.224\times10^{-3}$$

#### Integrate with Barrow's rule

In the elastic range $\sigma = E\,\varepsilon$ with $E$ constant, so $E$ leaves the integral. The antiderivative of $\varepsilon$ is $\varepsilon^2/2$, and Barrow's rule substitutes the limits:

$$U_r = \int_0^{\varepsilon_y}\sigma\,d\varepsilon = \int_0^{\varepsilon_y}E\,\varepsilon\,d\varepsilon = E\left[\frac{\varepsilon^2}{2}\right]_0^{\varepsilon_y} = E\left(\frac{\varepsilon_y^2}{2} - \frac{0^2}{2}\right) = \frac{E\,\varepsilon_y^2}{2}$$

Replacing $\varepsilon_y = \sigma_y/E$:

$$U_r = \frac{E}{2}\,\frac{\sigma_y^2}{E^2} = \frac{\sigma_y^2}{2E}$$

![[attachments/MAT-MT2/p20-resilience-area.svg]]

#### Value

$$U_r = \frac{(880\times10^{6}\ \text{Pa})^2}{2\times 107\times10^{9}\ \text{Pa}} = \frac{7.744\times10^{17}\ \text{Pa}^2}{2.14\times10^{11}\ \text{Pa}} = 3.619\times10^{6}\ \text{J/m}^3 = 3.619\ \text{MPa}$$

## Interpretation

- Rounding the diameter up from 9.23 mm to 10 mm raises the safety factor from 2.5 to 2.94: the area grows with the square of the diameter, $(10/9.228)^2 = 1.174$.
- Control case: with $N = 1$ the minimum diameter would be $9.228\sqrt{1/2.5} = 5.84$ mm, the rod that just reaches yield; the diameter scales as $\sqrt{N}$.
- The resilience 3.62 MJ/m³ is high because $\sigma_y$ is high and $E$ moderate, the property Slide 35 asks of spring alloys. At the working load each cubic metre of the 10 mm rod stores only $\tfrac{1}{2}\sigma\varepsilon = 0.420$ MJ/m³, about 1/8.6 of $U_r$, since the energy goes with $\sigma^2$.
- SI check: $F/\sigma_w$ in N/Pa = m²; $\sigma_y^2/E$ in Pa²/Pa = Pa = N/m² = J/m³, an energy per volume.
- Common mistake: using the mass in kg as the force (forgetting $g$), or the yield strength in place of the working stress, which gives 5.84 mm and no margin.

## Verification

- F (N) | 2400*9.81 | 23544
- sigma_w (MPa) | 880/2.5 | 352
- A_min (m^2) | 2400*9.81/(880e6/2.5) | 6.689e-5
- 4A/pi (m^2) | 4*2400*9.81/(880e6/2.5)/pi | 8.516e-5
- d_min (mm) | sqrt(4*2400*9.81/(880e6/2.5)/pi)*1e3 | 9.23
- A0 10 mm (m^2) | pi*(10e-3)**2/4 | 7.854e-5
- sigma (MPa) | 2400*9.81/(pi*(10e-3)**2/4)/1e6 | 299.8
- N real | 880/(2400*9.81/(pi*(10e-3)**2/4)/1e6) | 2.94
- eps | 2400*9.81/(pi*(10e-3)**2/4)/107e9 | 2.802e-3
- Delta l (mm) | 2400*9.81/(pi*(10e-3)**2/4)/107e9*1200 | 3.36
- eps_y | 880e6/107e9 | 8.224e-3
- U_r (MPa) | 880e6**2/(2*107e9)/1e6 | 3.619
- area ratio | (10/(sqrt(4*2400*9.81/(880e6/2.5)/pi)*1e3))**2 | 1.174
- d with N=1 (mm) | sqrt(4*2400*9.81/880e6/pi)*1e3 | 5.84
- energy at working load (MJ/m^3) | 0.5*(2400*9.81/(pi*(10e-3)**2/4))**2/107e9/1e6 | 0.420
- U_r over working energy | (880e6**2/(2*107e9))/(0.5*(2400*9.81/(pi*(10e-3)**2/4))**2/107e9) | 8.6

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
