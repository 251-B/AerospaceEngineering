---
materia: Aerospace Materials I
tema: "Unit 10: composite materials"
bank_id: P30
title: "Porous metal matrix infiltration and target modulus"
category: mt3_problem
archetype: composite-selection-inverse
level: conceptual
unit: 10
difficulty: 2
points: 5.0
time_minutes: 25
official: false
origen: "Problem written for the bank in the style of Problems T10_CompositeMaterials.pdf (Problems 9 and 12); not an official exercise. Verified with tools/materials_bank/verify_mt3.py"
tags:
  - problem-bank
  - midterm-3
  - unit-10
  - composite-materials
  - liquid-infiltration
  - metal-matrix-composite
  - isostrain
  - isostress
---

# Bank P30 — Porous metal matrix infiltration and target modulus

> [!info] Practice item, not an official exercise
> Written for the bank in the style of `Problems T10_CompositeMaterials.pdf` (Problems 9 and 12). Method: Session 22, Slides 22–27; Session 23, Slides 33–35. Every result is recomputed by tools/materials_bank/verify_mt3.py.

## Statement

An aerospace propulsion group evaluates two separate composite formulations for different thermal zones of a rocket thruster assembly:

1. **Infiltrated tungsten-copper MMC (parts a–b):** A sintered porous tungsten ($W$) preform with $22\ \text{vol\%}$ interconnected porosity is completely infiltrated with liquid copper ($\text{Cu}$). The densities of pure solid tungsten and pure copper are $\rho_W = 19.25\ \text{g/cm}^3$ and $\rho_{\text{Cu}} = 8.96\ \text{g/cm}^3$.
2. **Unidirectional carbon/polyimide PMC (parts c–d):** A $6.00\ \text{kg}$ batch of continuous unidirectional high-strength (HS) carbon fibres in a polyimide ($\text{PI}$) matrix must reach a longitudinal elastic modulus of at least $165\ \text{GPa}$ parallel to the fibres. Constituent properties are $E_f = 260\ \text{GPa}$, $\rho_f = 1.76\ \text{g/cm}^3$ for the carbon fibres, and $E_m = 3.05\ \text{GPa}$, $\rho_m = 1.40\ \text{g/cm}^3$ for the polyimide matrix.

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| Interconnected pore fraction (preform) | $V_p$ | $22\ \%$ | $0.22$ (dimensionless) |
| Solid tungsten volume fraction | $V_W$ | $1 - V_p = 78\ \%$ | $0.78$ (dimensionless) |
| Pure tungsten density | $\rho_W$ | $19.25\ \text{g/cm}^3$ | $19\,250\ \text{kg/m}^3$ |
| Pure copper density | $\rho_{\text{Cu}}$ | $8.96\ \text{g/cm}^3$ | $8960\ \text{kg/m}^3$ |
| Carbon/PI batch mass (part c) | $m_{\text{batch}}$ | $6.00\ \text{kg}$ | $6.00\ \text{kg}$ |
| Target longitudinal modulus (part c) | $E_{1C,\text{target}}$ | $165\ \text{GPa}$ | $165\times10^{9}\ \text{Pa}$ |
| HS carbon modulus, density | $E_f$, $\rho_f$ | $260\ \text{GPa}$, $1.76\ \text{g/cm}^3$ | $260\times10^{9}\ \text{Pa}$, $1760\ \text{kg/m}^3$ |
| Polyimide modulus, density | $E_m$, $\rho_m$ | $3.05\ \text{GPa}$, $1.40\ \text{g/cm}^3$ | $3.05\times10^{9}\ \text{Pa}$, $1400\ \text{kg/m}^3$ |

#### Model

- Rule of mixtures for density: $\rho = \sum_i V_i\rho_i$ [Session 22, Slide 27]; empty pores contribute volume without mass ($\rho_{\text{pore}} \approx 0$).
- Weight fraction of constituent $i$: $w_i = V_i\rho_i/\rho_c$ [Session 22, Slide 27].
- Liquid infiltration of a porous preform [Session 23, Slides 33–35]: molten metal is forced under pressure into open, interconnected pores until solidification is complete.
- Longitudinal isostrain modulus and target design: $E_{1C} = V_f E_f + (1 - V_f)E_m \implies V_f = \frac{E_{1C} - E_m}{E_f - E_m}$ [Session 22, Slide 22].
- Transverse isostress modulus: $\frac{1}{E_{2C}} = \frac{V_f}{E'_f} + \frac{V_m}{E_m}$ and matrix-dominated approximation $E_2 \approx E_m / V_m$ [Session 22, Slide 24].
- Hypotheses: complete infiltration of all $22\ \%$ pores with zero residual voids in the W–Cu composite; zero porosity, perfect bonding, continuous alignment, and isotropic fibre modulus ($E'_f = E_f$) in the carbon/PI composite.

## (a) Calculate the bulk density of the porous tungsten preform before infiltration, and explain why interconnected porosity is essential. [1.0 pts]

### Hint

In $1\ \text{m}^3$ of porous preform, $0.78\ \text{m}^3$ is solid tungsten and $0.22\ \text{m}^3$ is empty pore space with negligible mass.

### Checkpoint

- $\rho_{\text{before}} = 15\,015\ \text{kg/m}^3 = 15.02\ \text{g/cm}^3$
- Closed (isolated) pores prevent liquid copper from reaching internal voids, leaving trapped porosity

### Solution

#### Bulk density before infiltration

Before infiltration, the $22\ \text{vol\%}$ interconnected pores contain air/vacuum of negligible mass, so only the $V_W = 1 - 0.22 = 0.78$ solid tungsten fraction contributes mass [Session 22, Slide 27]:

$$\rho_{\text{before}} = V_W\rho_W + V_p\,(0) = 0.78\,(19\,250\ \text{kg/m}^3) = 15\,015\ \text{kg/m}^3 = 15.015\ \text{g/cm}^3 \approx 15.02\ \text{g/cm}^3$$

#### Role of interconnected porosity

In liquid-phase infiltration (such as squeeze casting or gas-pressure infiltration [Session 23, Slides 33–35]), molten copper must flow through a continuous network of open channels from the preform surface into the interior under applied pressure. If the pores were closed (isolated inside solid tungsten walls), the molten metal could not penetrate them, leaving empty voids that lower density, strength, and thermal conductivity.

## (b) After complete copper infiltration, calculate the composite density $\rho_{\text{after}}$ and the weight fractions $w_W$ and $w_{\text{Cu}}$. [1.3 pts]

### Hint

Liquid copper replaces the $22\ \text{vol\%}$ pore space completely ($V_{\text{Cu}} = 0.22$), so add $V_{\text{Cu}}\rho_{\text{Cu}}$ to $\rho_{\text{before}}$, then take each mass over $\rho_{\text{after}}$.

### Checkpoint

- $\rho_{\text{after}} = 16\,986\ \text{kg/m}^3 = 16.99\ \text{g/cm}^3$
- $w_W = 0.8840$ ($88.40\ \text{wt\%}$), $w_{\text{Cu}} = 0.1160$ ($11.60\ \text{wt\%}$)

### Solution

#### Composite density after complete infiltration

Because all interconnected pores ($V_{\text{Cu}} = V_p = 0.22$) are filled with liquid copper at $\rho_{\text{Cu}} = 8960\ \text{kg/m}^3$:

$$\rho_{\text{after}} = V_W\rho_W + V_{\text{Cu}}\rho_{\text{Cu}} = 0.78\,(19\,250\ \text{kg/m}^3) + 0.22\,(8960\ \text{kg/m}^3)$$

$$\rho_{\text{after}} = 15\,015\ \text{kg/m}^3 + 1971.2\ \text{kg/m}^3 = 16\,986.2\ \text{kg/m}^3 \approx 16\,986\ \text{kg/m}^3 \quad (16.99\ \text{g/cm}^3)$$

#### Weight fractions $w_W$ and $w_{\text{Cu}}$

In $1\ \text{m}^3$ of infiltrated W–Cu composite, tungsten supplies $15\,015\ \text{kg}$ and copper supplies $1971.2\ \text{kg}$ out of $16\,986.2\ \text{kg}$:

$$w_W = \frac{15\,015\ \text{kg/m}^3}{16\,986.2\ \text{kg/m}^3} = 0.8840 \quad (88.40\ \text{wt\%})$$

$$w_{\text{Cu}} = \frac{1971.2\ \text{kg/m}^3}{16\,986.2\ \text{kg/m}^3} = 0.1160 \quad (11.60\ \text{wt\%})$$

Check: $w_W + w_{\text{Cu}} = 0.8840 + 0.1160 = 1.0000$.

## (c) For the $6.00\ \text{kg}$ unidirectional carbon/polyimide batch targeting $E_{1C} \ge 165\ \text{GPa}$, determine the required fibre volume fraction $V_f$, composite density $\rho_c$, weight fraction $w_f$, and mass of carbon fibres $m_f$. [1.5 pts]

### Hint

Invert the isostrain modulus rule $E_{1C} = V_f E_f + (1 - V_f)E_m$ for the minimum $V_f$, compute $\rho_c$, convert $V_f$ to mass fraction $w_f$, and multiply by $6.00\ \text{kg}$.

### Checkpoint

- $V_f = 0.6303$ ($63.03\ \text{vol\%}$), $V_m = 0.3697$ ($36.97\ \text{vol\%}$)
- $\rho_c = 1627\ \text{kg/m}^3$ ($1.627\ \text{g/cm}^3$)
- $w_f = 0.6818$ ($68.18\ \text{wt\%}$), $m_f = 4.091\ \text{kg}$ of carbon fibres (and $1.909\ \text{kg}$ of polyimide)

### Solution

#### Minimum fibre volume fraction $V_f$

Since $E_{1C}$ increases monotonically with $V_f$, the minimum fibre content meets $E_{1C} = 165\ \text{GPa}$ [Session 22, Slide 22]:

$$E_{1C} = V_f E_f + (1 - V_f)E_m = E_m + V_f(E_f - E_m) \implies V_f = \frac{E_{1C} - E_m}{E_f - E_m}$$

Substituting $E_{1C} = 165\ \text{GPa}$, $E_f = 260\ \text{GPa}$, and $E_m = 3.05\ \text{GPa}$:

$$V_f = \frac{165 - 3.05}{260 - 3.05} = \frac{161.95\ \text{GPa}}{256.95\ \text{GPa}} = 0.6303 \quad (63.03\ \text{vol\%})$$

Thus the matrix volume fraction is $V_m = 1 - 0.63028 = 0.3697$ ($36.97\ \text{vol\%}$).

#### Composite density, weight fraction, and fibre batch mass

Converting densities to SI ($\rho_f = 1760\ \text{kg/m}^3$, $\rho_m = 1400\ \text{kg/m}^3$) [Session 22, Slide 27]:

$$\rho_c = 0.63028\,(1760\ \text{kg/m}^3) + 0.36972\,(1400\ \text{kg/m}^3) = 1109.3 + 517.6 = 1626.9\ \text{kg/m}^3 \approx 1627\ \text{kg/m}^3 \quad (1.627\ \text{g/cm}^3)$$

Computing the fibre weight fraction:

$$w_f = \frac{V_f\rho_f}{\rho_c} = \frac{1109.3\ \text{kg/m}^3}{1626.9\ \text{kg/m}^3} = 0.6818 \quad (68.18\ \text{wt\%})$$

Multiplying by the $6.00\ \text{kg}$ batch mass:

$$m_f = w_f\,m_{\text{batch}} = 0.6818\,(6.00\ \text{kg}) = 4.091\ \text{kg}$$

And the required polyimide mass is $m_m = 6.00 - 4.091 = 1.909\ \text{kg}$.

## (d) Compute the resulting transverse elastic modulus $E_{2C}$ of the carbon/polyimide composite and compare it with the matrix-dominated approximation $E_m/V_m$. [1.2 pts]

### Hint

Apply the isostress equation $1/E_{2C} = V_f/E_f + V_m/E_m$ using $V_f = 0.6303$ and $V_m = 0.3697$, and evaluate $E_m/V_m$.

### Checkpoint

- $E_{2C} = 8.088\ \text{GPa}$
- Matrix-dominated approximation: $E_m/V_m = 8.249\ \text{GPa}$ (overestimates $E_{2C}$ by $2.0\ \%$)

### Solution

#### Exact isostress transverse modulus $E_{2C}$

Perpendicular to the continuous carbon fibres [Session 22, Slide 24] with $E'_f = E_f = 260\ \text{GPa}$:

$$\frac{1}{E_{2C}} = \frac{V_f}{E_f} + \frac{V_m}{E_m} = \frac{0.63028}{260\ \text{GPa}} + \frac{0.36972}{3.05\ \text{GPa}}$$

$$\frac{1}{E_{2C}} = 2.424\times10^{-3}\ \text{GPa}^{-1} + 0.12122\ \text{GPa}^{-1} = 0.12364\ \text{GPa}^{-1}$$

Taking the reciprocal gives:

$$E_{2C} = \frac{1}{0.12364\ \text{GPa}^{-1}} = 8.088\ \text{GPa}$$

#### Comparison with the matrix-dominated approximation

Because $E_f / E_m = 260 / 3.05 = 85.2$, the fibre compliance term ($2.424\times10^{-3}\ \text{GPa}^{-1}$) is tiny compared with the matrix compliance term ($0.12122\ \text{GPa}^{-1}$). Dropping the fibre term yields the slide approximation [Session 22, Slide 24]:

$$E_{2,\text{approx}} \approx \frac{E_m}{V_m} = \frac{3.05\ \text{GPa}}{0.36972} = 8.249\ \text{GPa}$$

The approximation overestimates $E_{2C}$ by $(8.249 - 8.088)/8.088 = +2.0\ \%$ because neglecting the finite fibre compliance makes the fibres appear infinitely rigid ($E_f \to \infty$).

## Interpretation

- Both systems illustrate complementary composite design principles: in W–Cu, infiltrating $22\ \text{vol\%}$ copper closes every pore, raises bulk density by $13.1\ \%$ ($15.02 \to 16.99\ \text{g/cm}^3$), and creates a continuous metallic thermal path while preserving tungsten's high-temperature skeleton; in carbon/polyimide, reaching $165\ \text{GPa}$ requires $63.03\ \text{vol\%}$ ($68.18\ \text{wt\%}$) fibres, pushing longitudinal stiffness to $54$ times neat polyimide while transverse stiffness remains matrix-limited at $8.088\ \text{GPa}$ (anisotropy ratio $165/8.088 = 20.4$).
- Control cases: in part (a), if porosity were $0\ \%$, $\rho_{\text{before}} = \rho_{\text{after}} = 19\,250\ \text{kg/m}^3$; if porosity were $100\ \%$ and infiltrated, $\rho_{\text{after}} = \rho_{\text{Cu}} = 8960\ \text{kg/m}^3$. In part (c), dropping the matrix modulus ($E_m \to 0$) gives $V_f \approx 165/260 = 0.6346$ (within $0.7\ \%$ of $0.6303$).
- SI dimensional check: densities $\rho = \sum V_i\rho_i$ are in $\text{kg/m}^3$; $w_i$ and $V_f$ are dimensionless; $m_f = w_f m_{\text{batch}}$ is in $\text{kg}$; $1/E_{2C}$ is in $\text{GPa}^{-1}$ so $E_{2C}$ is in $\text{GPa}$.
- Common mistake: adding $0.22\times 8.96$ to $19.25$ instead of $0.78\times 19.25$ (which would exceed pure tungsten density!), or multiplying $6.00\ \text{kg}$ by $V_f = 0.6303$ instead of $w_f = 0.6818$ (giving $3.78\ \text{kg}$ instead of $4.091\ \text{kg}$).

## Verification

- rho_before (kg/m^3) | 0.78*19250 | 15015
- rho_before (g/cm^3) | 0.78*19.25 | 15.02
- rho_after (kg/m^3) | 0.78*19250 + 0.22*8960 | 16986
- rho_after (g/cm^3) | 0.78*19.25 + 0.22*8.96 | 16.99
- density gain (%) | ((0.78*19.25 + 0.22*8.96)/(0.78*19.25) - 1)*100 | 13.1
- w_W | (0.78*19250)/(0.78*19250 + 0.22*8960) | 0.8840
- w_Cu | (0.22*8960)/(0.78*19250 + 0.22*8960) | 0.1160
- Vf carbon/PI | (165 - 3.05)/(260 - 3.05) | 0.6303
- Vm carbon/PI | 1 - (165 - 3.05)/(260 - 3.05) | 0.3697
- rho_c carbon/PI (kg/m^3) | ((165 - 3.05)/(260 - 3.05))*1760 + (1 - (165 - 3.05)/(260 - 3.05))*1400 | 1627
- rho_c carbon/PI (g/cm^3) | (((165 - 3.05)/(260 - 3.05))*1760 + (1 - (165 - 3.05)/(260 - 3.05))*1400)/1000 | 1.627
- w_f carbon/PI | (((165 - 3.05)/(260 - 3.05))*1760)/(((165 - 3.05)/(260 - 3.05))*1760 + (1 - (165 - 3.05)/(260 - 3.05))*1400) | 0.6818
- m_f (kg) | 6.00*(((165 - 3.05)/(260 - 3.05))*1760)/(((165 - 3.05)/(260 - 3.05))*1760 + (1 - (165 - 3.05)/(260 - 3.05))*1400) | 4.091
- m_m (kg) | 6.00 - 6.00*(((165 - 3.05)/(260 - 3.05))*1760)/(((165 - 3.05)/(260 - 3.05))*1760 + (1 - (165 - 3.05)/(260 - 3.05))*1400) | 1.909
- E2C (GPa) | 1/(((165 - 3.05)/(260 - 3.05))/260 + (1 - (165 - 3.05)/(260 - 3.05))/3.05) | 8.088
- E2 approx (GPa) | 3.05/(1 - (165 - 3.05)/(260 - 3.05)) | 8.249
- E2 approx error (%) | ((3.05/(1 - (165 - 3.05)/(260 - 3.05)))/(1/(((165 - 3.05)/(260 - 3.05))/260 + (1 - (165 - 3.05)/(260 - 3.05))/3.05)) - 1)*100 | 2.0
- E1C/E2C anisotropy | 165/(1/(((165 - 3.05)/(260 - 3.05))/260 + (1 - (165 - 3.05)/(260 - 3.05))/3.05)) | 20.4
- control Em=0 Vf | 165/260 | 0.6346
- wrong mf using Vf (kg) | 6.00*((165 - 3.05)/(260 - 3.05)) | 3.78

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
