---
materia: Aerospace Materials I
tema: "Unit 10: composite materials"
bank_id: P29
title: "Inverse fiber volume fraction from allowable fiber stress"
category: mt3_problem
archetype: composite-selection-inverse
level: trap
unit: 10
difficulty: 3
points: 5.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of the final of January 2016 (question 10) in MATERIALS_FINALEXAM_2016_ORD_SOL.pdf and Problems T10_CompositeMaterials.pdf (Problems 9 and 10); not an official exercise. Verified with tools/materials_bank/verify_mt3.py"
tags:
  - problem-bank
  - midterm-3
  - unit-10
  - composite-materials
  - inverse-design
  - isostrain
  - weight-fraction
---

# Bank P29 — Inverse fiber volume fraction from allowable fiber stress

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the final of January 2016 (question 10) and `Problems T10_CompositeMaterials.pdf` (Problems 9 and 10). Method: Session 22, Slides 21–22 and 27. Every result is recomputed by tools/materials_bank/verify_mt3.py.

## Statement

An epoxy resin matrix is reinforced with continuous, longitudinally aligned S-glass fibres to fabricate a cylindrical rod $22.0\ \text{mm}$ in diameter and $1.60\ \text{m}$ in length that must withstand an axial tensile load of $32.0\ \text{kN}$ parallel to the fibres without the stress in any fibre exceeding an allowable limit of $\sigma_{f,\text{allow}} = 210\ \text{MPa}$. The constituent properties are:

- S-glass fibres ($f$): $E_f = 85.5\ \text{GPa}$, $\rho_f = 2.48\ \text{g/cm}^3$.
- Epoxy resin matrix ($m$): $E_m = 3.20\ \text{GPa}$, $\rho_m = 1.22\ \text{g/cm}^3$.

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| Rod diameter | $d$ | $22.0\ \text{mm}$ | $2.20\times10^{-2}\ \text{m}$ |
| Rod initial length | $L_0$ | $1.60\ \text{m}$ | $1.60\ \text{m}$ |
| Longitudinal axial load | $F_C$ | $32.0\ \text{kN}$ | $32.0\times10^{3}\ \text{N}$ |
| Allowable fibre stress | $\sigma_{f,\text{allow}}$ | $210\ \text{MPa}$ | $210\times10^{6}\ \text{Pa}$ |
| S-glass modulus, density | $E_f$, $\rho_f$ | $85.5\ \text{GPa}$, $2.48\ \text{g/cm}^3$ | $85.5\times10^{9}\ \text{Pa}$, $2480\ \text{kg/m}^3$ |
| Epoxy modulus, density | $E_m$, $\rho_m$ | $3.20\ \text{GPa}$, $1.22\ \text{g/cm}^3$ | $3.20\times10^{9}\ \text{Pa}$, $1220\ \text{kg/m}^3$ |
| Target batch mass (part c) | $m_{\text{batch}}$ | $4.00\ \text{kg}$ | $4.00\ \text{kg}$ |

#### Model

- Isostrain compatibility: $\varepsilon_c = \varepsilon_f = \varepsilon_m = \frac{F_C}{A_C E_{1C}}$ with $E_{1C} = E_f V_f + E_m(1 - V_f)$ [Session 22, Slides 21–22].
- Fibre stress under Hooke's law: $\sigma_f = E_f\varepsilon_c = \frac{E_f F_C}{A_C[E_f V_f + E_m(1 - V_f)]}$.
- Matrix stress under Hooke's law: $\sigma_m = E_m\varepsilon_c$.
- Composite density and fibre weight fraction: $\rho_c = V_f\rho_f + (1 - V_f)\rho_m$ and $w_f = \frac{V_f\rho_f}{\rho_c}$ [Session 22, Slide 27].
- Axial elongation: $\Delta L = \varepsilon_c L_0$.
- Hypotheses: zero porosity; perfect interfacial bonding; continuous aligned fibres; linear elastic behaviour in both constituents.

## (a) Derive from isostrain equilibrium the equation relating $\sigma_f$, $F_C$, $A_C$, and $V_f$, and solve for the minimum fibre volume fraction $V_{f,\min}$ so that $\sigma_f \le 210\ \text{MPa}$. [1.6 pts]

### Hint

Do not divide $F_C$ by $V_f A_C$ alone! Express $\varepsilon_c = \sigma_C / E_{1C} = F_C / (A_C [E_f V_f + E_m(1 - V_f)])$, multiply by $E_f$, clear the denominator to form the linear equation in $V_f$, and isolate $V_f$.

### Checkpoint

- $A_C = 3.801\times10^{-4}\ \text{m}^2$, $\sigma_C = 84.18\ \text{MPa}$
- Required $E_{1C} \ge 34.27\ \text{GPa}$
- $V_{f,\min} = 0.3776$ ($37.76\ \text{vol\%}$)

### Solution

#### Cross-sectional area and average composite stress

Converting $d = 22.0\ \text{mm} = 2.20\times10^{-2}\ \text{m}$:

$$A_C = \frac{\pi d^2}{4} = \frac{\pi\,(2.20\times10^{-2}\ \text{m})^2}{4} = 3.801\times10^{-4}\ \text{m}^2$$

With $F_C = 32.0\times10^{3}\ \text{N}$, the average longitudinal stress on the composite rod is:

$$\sigma_C = \frac{F_C}{A_C} = \frac{32.0\times10^{3}\ \text{N}}{3.8013\times10^{-4}\ \text{m}^2} = 8.418\times10^{7}\ \text{Pa} = 84.18\ \text{MPa}$$

#### Derivation of the governing equation for $V_f$

Under longitudinal isostrain loading [Session 22, Slides 21–22], the composite strain equals the fibre and matrix strains:

$$\varepsilon_c = \frac{\sigma_C}{E_{1C}} = \frac{F_C}{A_C\,[E_f V_f + E_m(1 - V_f)]}$$

Applying Hooke's law to the S-glass fibres, $\sigma_f = E_f\varepsilon_c$, yields:

$$\sigma_f = \frac{E_f F_C}{A_C\,[E_f V_f + E_m(1 - V_f)]}$$

Imposing the allowable stress limit $\sigma_f \le \sigma_{f,\text{allow}}$ and multiplying both sides by the positive denominator $A_C[E_f V_f + E_m(1 - V_f)]$, then dividing by $\sigma_{f,\text{allow}} A_C$:

$$E_f V_f + E_m(1 - V_f) \ge \frac{E_f F_C}{A_C\,\sigma_{f,\text{allow}}} = \frac{E_f\sigma_C}{\sigma_{f,\text{allow}}}$$

Expanding the left-hand side into a linear expression in $V_f$:

$$E_m + (E_f - E_m)\,V_f \ge \frac{E_f\sigma_C}{\sigma_{f,\text{allow}}}$$

Subtracting $E_m$ from both sides and dividing by $(E_f - E_m) > 0$ isolates $V_f$:

$$V_f \ge \frac{\dfrac{E_f\sigma_C}{\sigma_{f,\text{allow}}} - E_m}{E_f - E_m}$$

#### Numerical evaluation of $V_{f,\min}$

First compute the minimum composite modulus required:

$$E_{1C,\min} = \frac{E_f\sigma_C}{\sigma_{f,\text{allow}}} = \frac{(85.5\ \text{GPa})(84.181\ \text{MPa})}{210\ \text{MPa}} = 34.274\ \text{GPa}$$

Substituting into the isolated expression for $V_{f,\min}$:

$$V_{f,\min} = \frac{34.274\ \text{GPa} - 3.20\ \text{GPa}}{85.5\ \text{GPa} - 3.20\ \text{GPa}} = \frac{31.074\ \text{GPa}}{82.30\ \text{GPa}} = 0.3776 \quad (37.76\ \text{vol\%})$$

## (b) At $V_{f,\min}$, determine the resulting composite longitudinal modulus $E_{1C}$ and the matrix stress $\sigma_m$. [1.2 pts]

### Hint

Verify $E_{1C}$ by substituting $V_{f,\min}$ into the rule of mixtures, find $\varepsilon_c = \sigma_{f,\text{allow}}/E_f$, and compute $\sigma_m = E_m\varepsilon_c$.

### Checkpoint

- $E_{1C} = 34.27\ \text{GPa}$
- $\varepsilon_c = 2.456\times10^{-3}$, $\sigma_m = 7.860\ \text{MPa}$

### Solution

#### Resulting longitudinal composite modulus $E_{1C}$

With $V_{f,\min} = 0.37757$ and $V_m = 1 - 0.37757 = 0.62243$, the rule of mixtures [Session 22, Slide 22] confirms:

$$E_{1C} = 0.37757\,(85.5\ \text{GPa}) + 0.62243\,(3.20\ \text{GPa}) = 32.282\ \text{GPa} + 1.992\ \text{GPa} = 34.274\ \text{GPa} \approx 34.27\ \text{GPa}$$

#### Axial strain and stress carried by the epoxy matrix

When the fibres work exactly at $\sigma_f = 210\ \text{MPa}$, the common axial strain is:

$$\varepsilon_c = \frac{\sigma_f}{E_f} = \frac{210\times10^{6}\ \text{Pa}}{85.5\times10^{9}\ \text{Pa}} = 2.456\times10^{-3}$$

Applying Hooke's law to the epoxy matrix at the same isostrain $\varepsilon_m = \varepsilon_c$:

$$\sigma_m = E_m\varepsilon_c = (3.20\times10^{9}\ \text{Pa})(2.4561\times10^{-3}) = 7.860\times10^{6}\ \text{Pa} = 7.860\ \text{MPa}$$

Cross-check on total stress: $\sigma_C = V_f\sigma_f + V_m\sigma_m = 0.37757(210) + 0.62243(7.860) = 79.29 + 4.89 = 84.18\ \text{MPa}$, matching $F_C/A_C$ exactly. The matrix carries $4.89 / 84.18 = 5.81\ \%$ of the total axial force.

## (c) Calculate the composite density $\rho_c$, the fibre weight fraction $w_f$, and the mass of S-glass fibres $m_f$ required for a $4.00\ \text{kg}$ batch at $V_{f,\min}$. [1.2 pts]

### Hint

Compute $\rho_c$ from $V_{f,\min}$ and $V_m$, obtain $w_f = V_f\rho_f/\rho_c$, and multiply by $4.00\ \text{kg}$.

### Checkpoint

- $\rho_c = 1696\ \text{kg/m}^3$ ($1.696\ \text{g/cm}^3$)
- $w_f = 0.5522$ ($55.22\ \text{wt\%}$)
- $m_f = 2.209\ \text{kg}$ of S-glass fibres (and $1.791\ \text{kg}$ of epoxy resin)

### Solution

#### Composite density and fibre weight fraction

Converting densities to SI ($\rho_f = 2480\ \text{kg/m}^3$, $\rho_m = 1220\ \text{kg/m}^3$) [Session 22, Slide 27]:

$$\rho_c = 0.37757\,(2480\ \text{kg/m}^3) + 0.62243\,(1220\ \text{kg/m}^3) = 936.37 + 759.37 = 1695.7\ \text{kg/m}^3 \approx 1696\ \text{kg/m}^3 \quad (1.696\ \text{g/cm}^3)$$

The corresponding fibre mass fraction is:

$$w_f = \frac{V_{f,\min}\rho_f}{\rho_c} = \frac{936.37\ \text{kg/m}^3}{1695.7\ \text{kg/m}^3} = 0.5522 \quad (55.22\ \text{wt\%})$$

#### Required mass of fibres for a $4.00\ \text{kg}$ batch

Multiplying the weight fraction by the batch mass $m_{\text{batch}} = 4.00\ \text{kg}$:

$$m_f = w_f\,m_{\text{batch}} = 0.5522\,(4.00\ \text{kg}) = 2.209\ \text{kg}$$

The remaining matrix mass is $m_m = 4.00 - 2.209 = 1.791\ \text{kg}$ of epoxy resin.

## (d) Determine the axial elongation $\Delta L$ of the $1.60\ \text{m}$ rod under the $32.0\ \text{kN}$ load. [1.0 pts]

### Hint

Multiply the common axial strain $\varepsilon_c$ found in part (b) by the rod length $L_0 = 1.60\ \text{m}$.

### Checkpoint

- $\Delta L = 3.930\times10^{-3}\ \text{m} = 3.930\ \text{mm}$

### Solution

#### Axial elongation $\Delta L$

Using $\varepsilon_c = \Delta L / L_0$ with $\varepsilon_c = 2.4561\times10^{-3}$ and $L_0 = 1.60\ \text{m}$:

$$\Delta L = \varepsilon_c\,L_0 = (2.4561\times10^{-3})(1.60\ \text{m}) = 3.930\times10^{-3}\ \text{m} = 3.930\ \text{mm}$$

As a check directly from the composite modulus, $\Delta L = \frac{F_C L_0}{A_C E_{1C}} = \frac{(32\,000\ \text{N})(1.60\ \text{m})}{(3.8013\times10^{-4}\ \text{m}^2)(34.274\times10^{9}\ \text{Pa})} = 3.930\times10^{-3}\ \text{m}$.

## Interpretation

- Because the epoxy matrix carries $5.81\ \%$ of the axial load ($1.86\ \text{kN}$ out of $32.0\ \text{kN}$), the S-glass fibres only have to support the remaining $30.14\ \text{kN}$, allowing $V_{f,\min} = 37.76\ \text{vol\%}$ instead of $40.09\ \text{vol\%}$. Notice that increasing $V_f$ above $0.3776$ raises $E_{1C}$, reduces $\varepsilon_c$, and lowers $\sigma_f$ further below $210\ \text{MPa}$.
- Control case: if the matrix had zero stiffness ($E_m \to 0$), the formula would collapse to $V_{f,\min} = \sigma_C / \sigma_{f,\text{allow}} = 84.181 / 210 = 0.4009$ ($40.09\ \text{vol\%}$), where fibres carry $100\ \%$ of the load.
- SI dimensional check: $A_C$ is in $\text{m}^2$; $E_f\sigma_C/\sigma_{f,\text{allow}}$ has units $\text{Pa}\cdot\text{Pa}/\text{Pa} = \text{Pa}$; $V_{f,\min}$ and $w_f$ are dimensionless; $m_f$ is in $\text{kg}$; $\Delta L$ is in $\text{m}$.
- Common mistake: neglecting the matrix load contribution by setting $\sigma_f = F_C / (V_f A_C)$ (which gives the wrong value $40.09\ \%$ instead of $37.76\ \%$), or forgetting to convert $w_f$ from $V_f$ before multiplying by $4.00\ \text{kg}$ (which would wrongly give $0.3776 \times 4.00 = 1.51\ \text{kg}$).

## Verification

- A_C (m^2) | pi*(22.0e-3)**2/4 | 3.801e-4
- sigma_C (MPa) | 32.0e3/(pi*(22.0e-3)**2/4)/1e6 | 84.18
- E1C req (GPa) | 85.5*(32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 | 34.27
- Vf_min | (85.5*(32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 - 3.20)/(85.5 - 3.20) | 0.3776
- E1C at Vf_min (GPa) | ((85.5*(32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 - 3.20)/(85.5 - 3.20))*85.5 + (1 - (85.5*(32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 - 3.20)/(85.5 - 3.20))*3.20 | 34.27
- strain eps_c | 210e6/85.5e9 | 2.456e-3
- sigma_m (MPa) | 3.20e9*(210e6/85.5e9)/1e6 | 7.860
- matrix load share (%) | (1 - (85.5*(32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 - 3.20)/(85.5 - 3.20))*(3.20e9*(210e6/85.5e9)/1e6)/(32.0e3/(pi*(22.0e-3)**2/4)/1e6)*100 | 5.81
- rho_c (kg/m^3) | ((85.5*(32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 - 3.20)/(85.5 - 3.20))*2480 + (1 - (85.5*(32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 - 3.20)/(85.5 - 3.20))*1220 | 1696
- rho_c (g/cm^3) | (((85.5*(32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 - 3.20)/(85.5 - 3.20))*2480 + (1 - (85.5*(32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 - 3.20)/(85.5 - 3.20))*1220)/1000 | 1.696
- w_f | (((85.5*(32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 - 3.20)/(85.5 - 3.20))*2480)/(((85.5*(32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 - 3.20)/(85.5 - 3.20))*2480 + (1 - (85.5*(32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 - 3.20)/(85.5 - 3.20))*1220) | 0.5522
- m_f (kg) | 4.00*(((85.5*(32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 - 3.20)/(85.5 - 3.20))*2480)/(((85.5*(32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 - 3.20)/(85.5 - 3.20))*2480 + (1 - (85.5*(32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 - 3.20)/(85.5 - 3.20))*1220) | 2.209
- m_m (kg) | 4.00 - 4.00*(((85.5*(32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 - 3.20)/(85.5 - 3.20))*2480)/(((85.5*(32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 - 3.20)/(85.5 - 3.20))*2480 + (1 - (85.5*(32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 - 3.20)/(85.5 - 3.20))*1220) | 1.791
- Delta L (mm) | (210e6/85.5e9)*1.60*1e3 | 3.930
- control Em=0 Vf_min | (32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 | 0.4009
- wrong mf using Vf (kg) | 4.00*((85.5*(32.0e3/(pi*(22.0e-3)**2/4)/1e6)/210 - 3.20)/(85.5 - 3.20)) | 1.51

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
