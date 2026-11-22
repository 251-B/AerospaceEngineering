---
materia: Aerospace Materials I
tema: "Unit 10: composite materials"
bank_id: P28
title: "Candidate fiber selection under stiffness and strength limits"
category: mt3_problem
archetype: composite-selection-inverse
level: standard
unit: 10
difficulty: 2
points: 5.0
time_minutes: 25
official: false
origen: "Problem written for the bank in the style of the final of May 2012 (question 5) in MATERIALS_FINALEXAM_2012_ORD.pdf and Problems T10_CompositeMaterials.pdf (Problem 2); not an official exercise. Verified with tools/materials_bank/verify_mt3.py"
tags:
  - problem-bank
  - midterm-3
  - unit-10
  - composite-materials
  - fibre-selection
  - rule-of-mixtures
  - isostrain
  - isostress
---

# Bank P28 — Candidate fiber selection under stiffness and strength limits

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the final of May 2012 (question 5) and `Problems T10_CompositeMaterials.pdf` (Problem 2). Method: Session 21, Slides 17–30, 42–43; Session 22, Slides 22–27. Every result is recomputed by tools/materials_bank/verify_mt3.py.

## Statement

A unidirectional continuous-fibre composite is to be fabricated with an epoxy resin matrix. The design limits the fibre volume fraction to a maximum of $45\ \text{vol\%}$ ($V_f \le 0.45$) and requires a minimum longitudinal elastic modulus of $65.0\ \text{GPa}$ ($65.0\times10^{3}\ \text{MPa}$) and a minimum longitudinal tensile strength of $1400\ \text{MPa}$. Three candidate reinforcements (S-glass, aramid Kevlar-49, and intermediate-modulus carbon fibres) are available:

| Material | Density ($\text{g/cm}^3$) | Elastic modulus (GPa) | Tensile strength (MPa) |
| :--- | ---: | ---: | ---: |
| Epoxy resin ($m$) | 1.22 | 3.20 | 68.0 |
| S-glass fibre ($g$) | 2.48 | 85.5 | 4500 |
| Aramid (Kevlar-49) fibre ($a$) | 1.44 | 131 | 3700 |
| Carbon (IM) fibre ($c$) | 1.78 | 300 | 4200 |

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| Maximum fibre volume fraction | $V_{\max}$ | $45\ \%$ | $0.45$ (dimensionless) |
| Corresponding matrix fraction at $V_{\max}$ | $V_{m,\min}$ | $55\ \%$ | $0.55$ (dimensionless) |
| Minimum longitudinal modulus | $E_{1C,\min}$ | $65.0\ \text{GPa}$ | $65.0\times10^{9}\ \text{Pa}$ |
| Minimum longitudinal tensile strength | $\sigma_{1C,\min}$ | $1400\ \text{MPa}$ | $1400\times10^{6}\ \text{Pa}$ |
| Epoxy properties | $\rho_m$, $E_m$, $\sigma_m$ | $1.22\ \text{g/cm}^3$, $3.20\ \text{GPa}$, $68.0\ \text{MPa}$ | $1220\ \text{kg/m}^3$, $3.20\times10^{9}\ \text{Pa}$, $68.0\times10^{6}\ \text{Pa}$ |
| S-glass properties | $\rho_g$, $E_g$, $\sigma_g$ | $2.48\ \text{g/cm}^3$, $85.5\ \text{GPa}$, $4500\ \text{MPa}$ | $2480\ \text{kg/m}^3$, $85.5\times10^{9}\ \text{Pa}$, $4500\times10^{6}\ \text{Pa}$ |
| Aramid properties | $\rho_a$, $E_a$, $\sigma_a$ | $1.44\ \text{g/cm}^3$, $131\ \text{GPa}$, $3700\ \text{MPa}$ | $1440\ \text{kg/m}^3$, $131\times10^{9}\ \text{Pa}$, $3700\times10^{6}\ \text{Pa}$ |
| Carbon (IM) properties | $\rho_c$, $E_c$, $\sigma_c$ | $1.78\ \text{g/cm}^3$, $300\ \text{GPa}$, $4200\ \text{MPa}$ | $1780\ \text{kg/m}^3$, $300\times10^{9}\ \text{Pa}$, $4200\times10^{6}\ \text{Pa}$ |

#### Model

- Longitudinal modulus and tensile strength: $E_{1C} = V_f E_f + (1 - V_f)E_m$ and $\sigma_{1C} = V_f\sigma_f + (1 - V_f)\sigma_m$ [Session 22, Slides 22, 26].
- Transverse modulus: $\frac{1}{E_{2C}} = \frac{V_f}{E'_f} + \frac{V_m}{E_m}$ [Session 22, Slide 24].
- Composite density and specific modulus: $\rho_c = V_f\rho_f + (1 - V_f)\rho_m$ and $E_{1C}/\rho_c$ [Session 21, Slide 43; Session 22, Slide 27].
- Hypotheses: zero porosity; monotonic increase of $E_{1C}$ and $\sigma_{1C}$ with $V_f$ (since $E_f > E_m$ and $\sigma_f > \sigma_m$), so checking $V_f = V_{\max} = 0.45$ tests the best possible performance within the volume-fraction limit; isotropic fibre behaviour ($E'_f = E_f$) for $E_{2C}$.

## (a) Evaluate the longitudinal elastic modulus $E_{1C}$ for all three candidates at $V_{\max} = 0.45$. [1.2 pts]

### Hint

Compute the matrix contribution $(1 - 0.45)E_m$ once and add $0.45\,E_f$ for S-glass, aramid, and carbon.

### Checkpoint

- Matrix contribution: $0.55 \times 3.20 = 1.76\ \text{GPa}$
- $E_{1C}$ at $V_{\max}$: S-glass $= 40.24\ \text{GPa}$ (fails), Aramid $= 60.71\ \text{GPa}$ (fails), Carbon $= 136.8\ \text{GPa}$ (passes)

### Solution

#### Matrix modulus term at $V_f = 0.45$

At the upper bound $V_f = 0.45$, the epoxy matrix fraction is $V_m = 1 - 0.45 = 0.55$, contributing:

$$V_m E_m = 0.55\,(3.20\ \text{GPa}) = 1.760\ \text{GPa}$$

#### Longitudinal modulus $E_{1C}$ for each candidate

Applying $E_{1C} = V_f E_f + V_m E_m$ [Session 22, Slide 22]:

- **S-glass / epoxy:** $E_{1C,g} = 0.45\,(85.5\ \text{GPa}) + 1.760\ \text{GPa} = 38.475 + 1.760 = 40.235\ \text{GPa} \approx 40.24\ \text{GPa} < 65.0\ \text{GPa}$ (fails).
- **Aramid / epoxy:** $E_{1C,a} = 0.45\,(131\ \text{GPa}) + 1.760\ \text{GPa} = 58.950 + 1.760 = 60.71\ \text{GPa} < 65.0\ \text{GPa}$ (fails).
- **Carbon (IM) / epoxy:** $E_{1C,c} = 0.45\,(300\ \text{GPa}) + 1.760\ \text{GPa} = 135.00 + 1.760 = 136.76\ \text{GPa} \approx 136.8\ \text{GPa} \ge 65.0\ \text{GPa}$ (passes).

## (b) Evaluate the longitudinal tensile strength $\sigma_{1C}$ for all three candidates at $V_{\max} = 0.45$. [1.2 pts]

### Hint

Compute the matrix strength term $0.55\,\sigma_m$ and add $0.45\,\sigma_f$ for each candidate, then compare against $\sigma_{1C,\min} = 1400\ \text{MPa}$.

### Checkpoint

- Matrix contribution: $0.55 \times 68.0 = 37.40\ \text{MPa}$
- $\sigma_{1C}$ at $V_{\max}$: S-glass $= 2062\ \text{MPa}$ (passes), Aramid $= 1702\ \text{MPa}$ (passes), Carbon $= 1927\ \text{MPa}$ (passes)

### Solution

#### Matrix strength term at $V_f = 0.45$

With $V_m = 0.55$ and $\sigma_m = 68.0\ \text{MPa}$:

$$V_m \sigma_m = 0.55\,(68.0\ \text{MPa}) = 37.40\ \text{MPa}$$

#### Longitudinal tensile strength $\sigma_{1C}$ for each candidate

Applying $\sigma_{1C} = V_f \sigma_f + V_m \sigma_m$ [Session 22, Slide 26]:

- **S-glass / epoxy:** $\sigma_{1C,g} = 0.45\,(4500\ \text{MPa}) + 37.40\ \text{MPa} = 2025.0 + 37.40 = 2062.4\ \text{MPa} \approx 2062\ \text{MPa} \ge 1400\ \text{MPa}$ (passes).
- **Aramid / epoxy:** $\sigma_{1C,a} = 0.45\,(3700\ \text{MPa}) + 37.40\ \text{MPa} = 1665.0 + 37.40 = 1702.4\ \text{MPa} \approx 1702\ \text{MPa} \ge 1400\ \text{MPa}$ (passes).
- **Carbon (IM) / epoxy:** $\sigma_{1C,c} = 0.45\,(4200\ \text{MPa}) + 37.40\ \text{MPa} = 1890.0 + 37.40 = 1927.4\ \text{MPa} \approx 1927\ \text{MPa} \ge 1400\ \text{MPa}$ (passes).

## (c) Identify which candidate(s) satisfy both requirements, calculate $V_{f,E}$ and $V_{f,\sigma}$ for each candidate, and state the governing minimum $V_f$ for the feasible choice. [1.4 pts]

### Hint

Invert $V_f E_f + (1 - V_f)E_m = 65.0\ \text{GPa}$ and $V_f \sigma_f + (1 - V_f)\sigma_m = 1400\ \text{MPa}$ to find $V_{f,E}$ and $V_{f,\sigma}$ for every fibre; the required volume fraction is $\max(V_{f,E}, V_{f,\sigma})$.

### Checkpoint

- **Carbon (IM) fibre** is the **only** feasible candidate
- S-glass: $V_{f,E} = 0.7509$, $V_{f,\sigma} = 0.3005$ (needs $75.09\ \% > 45\ \%$)
- Aramid: $V_{f,E} = 0.4836$, $V_{f,\sigma} = 0.3667$ (needs $48.36\ \% > 45\ \%$)
- Carbon: $V_{f,E} = 0.2082$, $V_{f,\sigma} = 0.3224 \implies V_{f,\min} = 0.3224$ ($32.24\ \text{vol\%}$, governed by strength)

### Solution

#### Inverting the modulus and strength rules for minimum volume fractions

Solving $V_f E_f + (1 - V_f)E_m = E_{1C,\min}$ and $V_f\sigma_f + (1 - V_f)\sigma_m = \sigma_{1C,\min}$ for $V_f$:

$$V_{f,E} = \frac{E_{1C,\min} - E_m}{E_f - E_m} \qquad V_{f,\sigma} = \frac{\sigma_{1C,\min} - \sigma_m}{\sigma_f - \sigma_m}$$

Evaluating both expressions for each candidate:

- **S-glass:**
  $V_{f,E} = \frac{65.0 - 3.20}{85.5 - 3.20} = \frac{61.8}{82.3} = 0.7509$ ($75.09\ \%$); $\quad V_{f,\sigma} = \frac{1400 - 68.0}{4500 - 68.0} = \frac{1332}{4432} = 0.3005$ ($30.05\ \%$).
- **Aramid (Kevlar-49):**
  $V_{f,E} = \frac{65.0 - 3.20}{131 - 3.20} = \frac{61.8}{127.8} = 0.4836$ ($48.36\ \%$); $\quad V_{f,\sigma} = \frac{1400 - 68.0}{3700 - 68.0} = \frac{1332}{3632} = 0.3667$ ($36.67\ \%$).
- **Carbon (IM):**
  $V_{f,E} = \frac{65.0 - 3.20}{300 - 3.20} = \frac{61.8}{296.8} = 0.2082$ ($20.82\ \%$); $\quad V_{f,\sigma} = \frac{1400 - 68.0}{4200 - 68.0} = \frac{1332}{4132} = 0.3224$ ($32.24\ \%$).

| Candidate fibre | $E_{1C}$ at $0.45$ (GPa) | $\sigma_{1C}$ at $0.45$ (MPa) | $V_{f,E}$ | $V_{f,\sigma}$ | Required $V_{f,\min}$ | Feasible ($\le 0.45$)? |
| :--- | ---: | ---: | ---: | ---: | ---: | :--- |
| S-glass | 40.24 | 2062 | 0.7509 | 0.3005 | 0.7509 | No (fails stiffness) |
| Aramid (Kevlar-49) | 60.71 | 1702 | 0.4836 | 0.3667 | 0.4836 | No (fails stiffness) |
| Carbon (IM) | 136.8 | 1927 | 0.2082 | 0.3224 | 0.3224 | **Yes** |

#### Selection and governing limit

Only **carbon (IM) fibre** meets both specifications with $V_f \le 0.45$. Both S-glass and aramid easily clear the $1400\ \text{MPa}$ strength limit, but they fall short on longitudinal modulus ($40.24$ and $60.71\ \text{GPa} < 65.0\ \text{GPa}$). For carbon/epoxy, any fibre fraction in the window $0.3224 \le V_f \le 0.45$ satisfies both requirements, with the lower bound $V_{f,\min} = 0.3224$ ($32.24\ \text{vol\%}$) governed by strength.

## (d) For the selected carbon/epoxy composite at $V_f = 0.45$, calculate the transverse modulus $E_{2C}$, the composite density $\rho_c$, and the longitudinal specific modulus $E_{1C}/\rho_c$. [1.2 pts]

### Hint

Apply the isostress rule for $E_{2C}$, the density rule of mixtures for $\rho_c$, and divide $E_{1C} = 136.76\ \text{GPa}$ from part (a) by $\rho_c$ in $\text{kg/m}^3$.

### Checkpoint

- $E_{2C} = 5.768\ \text{GPa}$
- $\rho_c = 1472\ \text{kg/m}^3$ ($1.472\ \text{g/cm}^3$)
- $E_{1C}/\rho_c = 92.91\times10^{6}\ \text{m}^2/\text{s}^2 = 92\,908\ \text{kN}\cdot\text{m/kg}$

### Solution

#### Transverse elastic modulus $E_{2C}$

Under isostress transverse loading [Session 22, Slide 24] with $V_f = 0.45$, $V_m = 0.55$, $E'_f = E_c = 300\ \text{GPa}$, and $E_m = 3.20\ \text{GPa}$:

$$\frac{1}{E_{2C}} = \frac{0.45}{300\ \text{GPa}} + \frac{0.55}{3.20\ \text{GPa}} = 1.500\times10^{-3}\ \text{GPa}^{-1} + 0.17188\ \text{GPa}^{-1} = 0.17338\ \text{GPa}^{-1}$$

$$E_{2C} = \frac{1}{0.17338\ \text{GPa}^{-1}} = 5.768\ \text{GPa}$$

#### Composite density $\rho_c$ and specific modulus $E_{1C}/\rho_c$

With $\rho_c = 1780\ \text{kg/m}^3$ for carbon fibres and $\rho_m = 1220\ \text{kg/m}^3$ for epoxy [Session 22, Slide 27]:

$$\rho_{\text{comp}} = 0.45\,(1780\ \text{kg/m}^3) + 0.55\,(1220\ \text{kg/m}^3) = 801\ \text{kg/m}^3 + 671\ \text{kg/m}^3 = 1472\ \text{kg/m}^3 = 1.472\ \text{g/cm}^3$$

Dividing $E_{1C} = 136.76\times10^{9}\ \text{N/m}^2$ by $\rho_{\text{comp}} = 1472\ \text{kg/m}^3$ [Session 21, Slide 43]:

$$\frac{E_{1C}}{\rho_{\text{comp}}} = \frac{136.76\times10^{9}\ \text{N/m}^2}{1472\ \text{kg/m}^3} = 92.91\times10^{6}\ \frac{\text{m}^2}{\text{s}^2} = 92\,908\ \text{kN}\cdot\text{m/kg}$$

## Interpretation

- All three candidates meet the strength target easily, so modulus is the discriminating property: S-glass is even stronger than carbon ($4500$ vs $4200\ \text{MPa}$), yet its modulus ($85.5\ \text{GPa}$) is too low, and aramid misses the $65.0\ \text{GPa}$ target by just $4.29\ \text{GPa}$ (requiring $48.36\ \text{vol\%}$ instead of $45\ \text{vol\%}$). Only carbon combines high stiffness and high strength at low density ($92.91\times10^{6}\ \text{m}^2/\text{s}^2$, more than $3.5$ times that of aluminium or titanium).
- Control case: if the design used carbon at its minimum feasible fraction $V_{f,\min} = 0.3224$, it would achieve $\sigma_{1C} = 1400\ \text{MPa}$, $E_{1C} = 0.3224(300) + 0.6776(3.20) = 98.89\ \text{GPa} > 65.0\ \text{GPa}$, and an even lower density $\rho_{\text{comp}} = 1401\ \text{kg/m}^3$.
- SI dimensional check: $V_{f,E}$ and $V_{f,\sigma}$ are dimensionless ratios of GPa/GPa and MPa/MPa; $E_{2C}$ is in GPa; $E_{1C}/\rho_{\text{comp}}$ is in $(\text{N/m}^2)/(\text{kg/m}^3) = \text{m}^2/\text{s}^2 = \text{N}\cdot\text{m/kg}$.
- Common mistake: picking S-glass because it gives the highest strength at $V_f = 0.45$ ($2062\ \text{MPa}$), without checking the modulus requirement, or forgetting that $V_{f,\min}$ for the feasible candidate must satisfy $\max(V_{f,E}, V_{f,\sigma})$ rather than $\min(V_{f,E}, V_{f,\sigma})$.

## Verification

- matrix E term (GPa) | 0.55*3.20 | 1.760
- E1C S-glass (GPa) | 0.45*85.5 + 0.55*3.20 | 40.24
- E1C Aramid (GPa) | 0.45*131 + 0.55*3.20 | 60.71
- E1C Carbon (GPa) | 0.45*300 + 0.55*3.20 | 136.8
- matrix sigma term (MPa) | 0.55*68.0 | 37.40
- sigma1C S-glass (MPa) | 0.45*4500 + 0.55*68.0 | 2062
- sigma1C Aramid (MPa) | 0.45*3700 + 0.55*68.0 | 1702
- sigma1C Carbon (MPa) | 0.45*4200 + 0.55*68.0 | 1927
- Vf_E S-glass | (65.0 - 3.20)/(85.5 - 3.20) | 0.7509
- Vf_S S-glass | (1400 - 68.0)/(4500 - 68.0) | 0.3005
- Vf_E Aramid | (65.0 - 3.20)/(131 - 3.20) | 0.4836
- Vf_S Aramid | (1400 - 68.0)/(3700 - 68.0) | 0.3667
- Vf_E Carbon | (65.0 - 3.20)/(300 - 3.20) | 0.2082
- Vf_S Carbon | (1400 - 68.0)/(4200 - 68.0) | 0.3224
- E2C Carbon at 0.45 (GPa) | 1/(0.45/300 + 0.55/3.20) | 5.768
- rho Carbon at 0.45 (kg/m^3) | 0.45*1780 + 0.55*1220 | 1472
- rho Carbon at 0.45 (g/cm^3) | (0.45*1780 + 0.55*1220)/1000 | 1.472
- spec E Carbon (1e6 m^2/s^2) | (0.45*300e9 + 0.55*3.20e9)/(0.45*1780 + 0.55*1220)/1e6 | 92.91
- spec E Carbon (kN*m/kg) | (0.45*300e9 + 0.55*3.20e9)/(0.45*1780 + 0.55*1220)/1e3 | 92908
- control E1C at Vf_min (GPa) | ((1400 - 68.0)/(4200 - 68.0))*300 + (1 - (1400 - 68.0)/(4200 - 68.0))*3.20 | 98.89
- control rho at Vf_min (kg/m^3) | ((1400 - 68.0)/(4200 - 68.0))*1780 + (1 - (1400 - 68.0)/(4200 - 68.0))*1220 | 1401

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
