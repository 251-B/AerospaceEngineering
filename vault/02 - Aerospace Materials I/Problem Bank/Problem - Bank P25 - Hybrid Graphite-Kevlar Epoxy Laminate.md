---
materia: Aerospace Materials I
tema: "Unit 10: composite materials"
bank_id: P25
title: "Hybrid graphite-Kevlar epoxy laminate"
category: mt3_problem
archetype: composite-hybrid-specific
level: standard
unit: 10
difficulty: 2
points: 5.0
time_minutes: 25
official: false
origen: "Problem written for the bank in the style of Assessment Test III Model B (2020, Part II, p. 3) in MATERIALS_THIRDPARTIAL_2020.pdf; not an official exercise. Verified with tools/materials_bank/verify_mt3.py"
tags:
  - problem-bank
  - midterm-3
  - unit-10
  - composite-materials
  - hybrid-composite
  - specific-properties
---

# Bank P25 — Hybrid graphite-Kevlar epoxy laminate

> [!info] Practice item, not an official exercise
> Written for the bank in the style of Assessment Test III Model B (2020, Part II). Method: Session 21, Slides 30 and 43; Session 22, Slides 22–27. Every result is recomputed by tools/materials_bank/verify_mt3.py.

## Statement

A unidirectional aerospace composite laminate contains $60\ \text{vol\%}$ continuous aligned high-modulus graphite (graphite-HM) fibres in an epoxy matrix. The constituent properties are listed in the table below:

| Material | Density ($\text{g/cm}^3$) | Elastic modulus (GPa) | Tensile strength (MPa) |
| :--- | ---: | ---: | ---: |
| Epoxy resin ($m$) | 1.22 | 3.40 | 68.0 |
| Graphite-HM fibre ($\text{gr}$) | 1.85 | 385 | 2450 |
| Kevlar-49 fibre ($K$) | 1.44 | 131 | 3700 |

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| Baseline graphite fibre volume fraction | $V_{f,0}$ | $60\ \%$ | $0.60$ (dimensionless) |
| Epoxy matrix volume fraction | $V_m$ | $40\ \%$ | $0.40$ (dimensionless) |
| Graphite replacement fraction (part c) | — | $40\ \%$ of fibre volume | $V_{\text{gr}} = 0.36$, $V_K = 0.24$ |
| Epoxy density | $\rho_m$ | $1.22\ \text{g/cm}^3$ | $1220\ \text{kg/m}^3$ |
| Graphite-HM density | $\rho_{\text{gr}}$ | $1.85\ \text{g/cm}^3$ | $1850\ \text{kg/m}^3$ |
| Kevlar-49 density | $\rho_K$ | $1.44\ \text{g/cm}^3$ | $1440\ \text{kg/m}^3$ |
| Epoxy modulus, strength | $E_m$, $\sigma_m$ | $3.40\ \text{GPa}$, $68.0\ \text{MPa}$ | $3.40\times10^{9}\ \text{Pa}$, $68.0\times10^{6}\ \text{Pa}$ |
| Graphite-HM modulus, strength | $E_{\text{gr}}$, $\sigma_{\text{gr}}$ | $385\ \text{GPa}$, $2450\ \text{MPa}$ | $385\times10^{9}\ \text{Pa}$, $2450\times10^{6}\ \text{Pa}$ |
| Kevlar-49 modulus, strength | $E_K$, $\sigma_K$ | $131\ \text{GPa}$, $3700\ \text{MPa}$ | $131\times10^{9}\ \text{Pa}$, $3700\times10^{6}\ \text{Pa}$ |

#### Model

- General rule of mixtures for three-constituent hybrids: $\rho_{\text{hyb}} = \sum_i V_i\rho_i$, $E_{\text{hyb}} = \sum_i V_i E_i$, and $\sigma_{\text{hyb}} = \sum_i V_i\sigma_i$ with $\sum_i V_i = 1$ [Session 22, Slides 22, 26–27].
- Weight fraction of constituent $i$: $w_i = V_i\rho_i / \rho_c$ [Session 22, Slide 27].
- Specific modulus and specific strength: $E/\rho$ and $\sigma/\rho$, in $\text{Pa}/(\text{kg/m}^3) = \text{N}\cdot\text{m/kg} = \text{m}^2/\text{s}^2$ [Session 21, Slide 43].
- Transverse isostress modulus of the baseline composite: $\frac{1}{E_{2C}} = \frac{V_{f,0}}{E'_{\text{gr}}} + \frac{V_m}{E_m}$ [Session 22, Slide 24].
- Hypotheses: zero porosity; unidirectional alignment along direction 1; perfect bonding; isotropic baseline fibre transverse modulus ($E'_{\text{gr}} = E_{\text{gr}}$) [Session 22, Slide 20]; tabulated matrix tensile strength used in the rule of mixtures for longitudinal composite strength.

## (a) Estimate the density $\rho_c$ and longitudinal elastic modulus $E_{1C}$ of the baseline graphite-HM/epoxy composite. [1.2 pts]

### Hint

Apply the two-constituent rule of mixtures with $V_{f,0} = 0.60$ and $V_m = 0.40$ for both density and longitudinal modulus.

### Checkpoint

- $\rho_c = 1598\ \text{kg/m}^3 = 1.598\ \text{g/cm}^3$
- $E_{1C} = 232.4\ \text{GPa}$

### Solution

#### Baseline composite density $\rho_c$

Converting densities to SI ($\rho_{\text{gr}} = 1850\ \text{kg/m}^3$, $\rho_m = 1220\ \text{kg/m}^3$) and applying $\rho_c = V_{f,0}\rho_{\text{gr}} + V_m\rho_m$ [Session 22, Slide 27]:

$$\rho_c = 0.60\,(1850\ \text{kg/m}^3) + 0.40\,(1220\ \text{kg/m}^3) = 1110\ \text{kg/m}^3 + 488\ \text{kg/m}^3 = 1598\ \text{kg/m}^3 = 1.598\ \text{g/cm}^3$$

#### Baseline longitudinal modulus $E_{1C}$

Under isostrain loading parallel to the graphite fibres [Session 22, Slide 22]:

$$E_{1C} = 0.60\,(385\ \text{GPa}) + 0.40\,(3.40\ \text{GPa}) = 231.0\ \text{GPa} + 1.36\ \text{GPa} = 232.36\ \text{GPa} \approx 232.4\ \text{GPa}$$

## (b) Estimate the fibre weight fraction $w_f$ and matrix weight fraction $w_m$ of the baseline composite. [1.0 pts]

### Hint

Divide each constituent's mass contribution per cubic metre from part (a) by $\rho_c$.

### Checkpoint

- $w_f = 0.6946$ ($69.46\ \text{wt\%}$), $w_m = 0.3054$ ($30.54\ \text{wt\%}$)

### Solution

#### Weight fractions from masses per unit volume

From part (a), $1\ \text{m}^3$ of baseline composite contains $1110\ \text{kg}$ of graphite fibres and $488\ \text{kg}$ of epoxy resin out of a total mass of $1598\ \text{kg}$:

$$w_f = \frac{V_{f,0}\rho_{\text{gr}}}{\rho_c} = \frac{1110\ \text{kg/m}^3}{1598\ \text{kg/m}^3} = 0.6946 \quad (69.46\ \text{wt\%})$$

$$w_m = \frac{V_m\rho_m}{\rho_c} = \frac{488\ \text{kg/m}^3}{1598\ \text{kg/m}^3} = 0.3054 \quad (30.54\ \text{wt\%})$$

Check: $0.6946 + 0.3054 = 1.0000$.

## (c) If $40\ \%$ of the graphite fibres by volume are replaced with Kevlar-49 fibres, calculate the hybrid density $\rho_{\text{hyb}}$, longitudinal modulus $E_{\text{hyb}}$, tensile strength $\sigma_{\text{hyb}}$, specific modulus $E_{\text{hyb}}/\rho_{\text{hyb}}$, and specific strength $\sigma_{\text{hyb}}/\rho_{\text{hyb}}$. [1.8 pts]

### Hint

Keep the matrix fraction fixed at $0.40$ and split the $0.60$ fibre volume as $60\ \%$ remaining graphite and $40\ \%$ Kevlar-49; then apply the three-constituent rule of mixtures and divide by $\rho_{\text{hyb}}$ in $\text{kg/m}^3$.

### Checkpoint

- $V_{\text{gr}} = 0.36$, $V_K = 0.24$, $V_m = 0.40$
- $\rho_{\text{hyb}} = 1500\ \text{kg/m}^3$ ($1.500\ \text{g/cm}^3$), $E_{\text{hyb}} = 171.4\ \text{GPa}$, $\sigma_{\text{hyb}} = 1797\ \text{MPa}$
- $E_{\text{hyb}}/\rho_{\text{hyb}} = 114.3\times10^{6}\ \text{m}^2/\text{s}^2 = 114\,297\ \text{kN}\cdot\text{m/kg}$, $\sigma_{\text{hyb}}/\rho_{\text{hyb}} = 1198\ \text{kN}\cdot\text{m/kg} = 1.198\times10^{6}\ \text{m}^2/\text{s}^2$

### Solution

#### Constituent volume fractions in the hybrid

Replacing $40\ \%$ of the $0.60$ graphite fibre volume by Kevlar-49 leaves $60\ \%$ of it as graphite while keeping total fibre fraction at $0.60$ and epoxy at $0.40$:

$$V_K = 0.40 \times 0.60 = 0.24 \qquad V_{\text{gr}} = 0.60 \times 0.60 = 0.36 \qquad V_m = 0.40$$

Check: $0.36 + 0.24 + 0.40 = 1.00$.

#### Hybrid density $\rho_{\text{hyb}}$, modulus $E_{\text{hyb}}$, and strength $\sigma_{\text{hyb}}$

Applying the three-constituent rule of mixtures [Session 22, Slides 22, 26–27]:

$$\rho_{\text{hyb}} = 0.36\,(1850) + 0.24\,(1440) + 0.40\,(1220) = 666.0 + 345.6 + 488.0 = 1499.6\ \text{kg/m}^3 \approx 1500\ \text{kg/m}^3 \quad (1.500\ \text{g/cm}^3)$$

$$E_{\text{hyb}} = 0.36\,(385\ \text{GPa}) + 0.24\,(131\ \text{GPa}) + 0.40\,(3.40\ \text{GPa}) = 138.60 + 31.44 + 1.36 = 171.40\ \text{GPa}$$

$$\sigma_{\text{hyb}} = 0.36\,(2450\ \text{MPa}) + 0.24\,(3700\ \text{MPa}) + 0.40\,(68.0\ \text{MPa}) = 882.0 + 888.0 + 27.2 = 1797.2\ \text{MPa} \approx 1797\ \text{MPa}$$

#### Longitudinal specific modulus and specific tensile strength

Converting modulus and strength to Pa and dividing by $\rho_{\text{hyb}} = 1499.6\ \text{kg/m}^3$ [Session 21, Slide 43]:

$$\frac{E_{\text{hyb}}}{\rho_{\text{hyb}}} = \frac{171.40\times10^{9}\ \text{N/m}^2}{1499.6\ \text{kg/m}^3} = 114.3\times10^{6}\ \frac{\text{m}^2}{\text{s}^2} = 114\,297\ \text{kN}\cdot\text{m/kg}$$

$$\frac{\sigma_{\text{hyb}}}{\rho_{\text{hyb}}} = \frac{1797.2\times10^{6}\ \text{N/m}^2}{1499.6\ \text{kg/m}^3} = 1.198\times10^{6}\ \frac{\text{m}^2}{\text{s}^2} = 1198\ \text{kN}\cdot\text{m/kg}$$

Equivalently, $\sigma_{\text{hyb}}/\rho_{\text{hyb}} = 1797.2\ \text{MPa}/(1.4996\ \text{g/cm}^3) = 1198\ \text{MPa}\cdot\text{cm}^3/\text{g} = 1198\ \text{kN}\cdot\text{m/kg}$.

## (d) Calculate the transverse elastic modulus $E_{2C}$ of the baseline composite from part (a). [1.0 pts]

### Hint

Apply the isostress rule with $V_{f,0} = 0.60$, $V_m = 0.40$, $E_{\text{gr}} = 385\ \text{GPa}$, and $E_m = 3.40\ \text{GPa}$.

### Checkpoint

- $E_{2C} = 8.389\ \text{GPa}$

### Solution

#### Isostress transverse modulus $E_{2C}$

Perpendicular to the graphite fibres in the baseline composite [Session 22, Slide 24], assuming $E'_{\text{gr}} = E_{\text{gr}} = 385\ \text{GPa}$:

$$\frac{1}{E_{2C}} = \frac{V_{f,0}}{E_{\text{gr}}} + \frac{V_m}{E_m} = \frac{0.60}{385\ \text{GPa}} + \frac{0.40}{3.40\ \text{GPa}} = 1.5584\times10^{-3}\ \text{GPa}^{-1} + 0.11765\ \text{GPa}^{-1} = 0.11921\ \text{GPa}^{-1}$$

Taking the reciprocal gives:

$$E_{2C} = \frac{1}{0.11921\ \text{GPa}^{-1}} = 8.389\ \text{GPa}$$

## Interpretation

- Comparing the baseline ($100\ \%$ graphite-HM fibres) against the hybrid ($60\ \%$ graphite-HM / $40\ \%$ Kevlar-49): the baseline has strength $\sigma_{1C} = 0.60(2450) + 0.40(68.0) = 1497\ \text{MPa}$, specific modulus $232.36\times10^{9}/1598 = 145.4\times10^{6}\ \text{m}^2/\text{s}^2$, and specific strength $1497.2/1.598 = 936.9\ \text{kN}\cdot\text{m/kg}$. Replacing $40\ \%$ of the graphite with Kevlar-49 trades $21.4\ \%$ of specific stiffness ($145.4 \to 114.3\times10^{6}\ \text{m}^2/\text{s}^2$) to gain $20.0\ \%$ in tensile strength ($1497 \to 1797\ \text{MPa}$), cut density by $6.2\ \%$ ($1598 \to 1500\ \text{kg/m}^3$), and boost specific strength by $27.9\ \%$ ($936.9 \to 1198\ \text{kN}\cdot\text{m/kg}$), while also improving impact tolerance [Session 21, Slide 30].
- Control case: if $0\ \%$ of the graphite were replaced, the hybrid formulas reproduce $\rho_c = 1598\ \text{kg/m}^3$ and $E_{1C} = 232.4\ \text{GPa}$; if $100\ \%$ were replaced with Kevlar-49, $\rho = 0.60(1440) + 0.40(1220) = 1352\ \text{kg/m}^3$ and $E = 0.60(131) + 0.40(3.40) = 79.96\ \text{GPa}$.
- SI dimensional check: $E/\rho$ and $\sigma/\rho$ have units $\text{Pa}/(\text{kg/m}^3) = (\text{N/m}^2)/(\text{kg/m}^3) = \text{N}\cdot\text{m/kg} = \text{m}^2/\text{s}^2$. Moreover, $1\ \text{MPa}\cdot\text{cm}^3/\text{g} = (10^{6}\ \text{Pa})/(10^{3}\ \text{kg/m}^3) = 10^{3}\ \text{N}\cdot\text{m/kg} = 1\ \text{kN}\cdot\text{m/kg}$.
- Common mistake: replacing $40\ \%$ of the *total laminate* volume ($V_K = 0.40, V_{\text{gr}} = 0.20$) instead of $40\ \%$ of the *graphite fibre* volume ($V_K = 0.40\times 0.60 = 0.24$), or using the graphite fibre weight fraction $0.6946$ inside the modulus formula.

## Verification

- rho_c baseline (kg/m^3) | 0.60*1850 + 0.40*1220 | 1598
- rho_c baseline (g/cm^3) | (0.60*1850 + 0.40*1220)/1000 | 1.598
- E1C baseline (GPa) | 0.60*385 + 0.40*3.40 | 232.4
- w_f baseline | (0.60*1850)/(0.60*1850 + 0.40*1220) | 0.6946
- w_m baseline | (0.40*1220)/(0.60*1850 + 0.40*1220) | 0.3054
- V_gr hybrid | 0.60*0.60 | 0.36
- V_K hybrid | 0.40*0.60 | 0.24
- rho_hyb (kg/m^3) | 0.36*1850 + 0.24*1440 + 0.40*1220 | 1500
- rho_hyb (g/cm^3) | (0.36*1850 + 0.24*1440 + 0.40*1220)/1000 | 1.500
- E_hyb (GPa) | 0.36*385 + 0.24*131 + 0.40*3.40 | 171.4
- sigma_hyb (MPa) | 0.36*2450 + 0.24*3700 + 0.40*68.0 | 1797
- E_hyb/rho_hyb (1e6 m^2/s^2) | (0.36*385e9 + 0.24*131e9 + 0.40*3.40e9)/(0.36*1850 + 0.24*1440 + 0.40*1220)/1e6 | 114.3
- E_hyb/rho_hyb (kN*m/kg) | (0.36*385e9 + 0.24*131e9 + 0.40*3.40e9)/(0.36*1850 + 0.24*1440 + 0.40*1220)/1e3 | 114297
- sigma_hyb/rho_hyb (kN*m/kg) | (0.36*2450e6 + 0.24*3700e6 + 0.40*68.0e6)/(0.36*1850 + 0.24*1440 + 0.40*1220)/1e3 | 1198
- sigma_hyb/rho_hyb (1e6 m^2/s^2) | (0.36*2450e6 + 0.24*3700e6 + 0.40*68.0e6)/(0.36*1850 + 0.24*1440 + 0.40*1220)/1e6 | 1.198
- E2C baseline (GPa) | 1/(0.60/385 + 0.40/3.40) | 8.389
- sigma_1C baseline (MPa) | 0.60*2450 + 0.40*68.0 | 1497
- specific modulus baseline (1e6 m^2/s^2) | (0.60*385e9 + 0.40*3.40e9)/(0.60*1850 + 0.40*1220)/1e6 | 145.4
- specific strength baseline (kN*m/kg) | (0.60*2450e6 + 0.40*68.0e6)/(0.60*1850 + 0.40*1220)/1e3 | 936.9
- control 100% Kevlar rho (kg/m^3) | 0.60*1440 + 0.40*1220 | 1352
- control 100% Kevlar E (GPa) | 0.60*131 + 0.40*3.40 | 79.96

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
