---
materia: Aerospace Materials I
tema: "Unit 10: composite materials"
bank_id: P23
title: "Glass-epoxy composite replacing metallic plate"
category: mt3_problem
archetype: composite-unidirectional
level: trap
unit: 10
difficulty: 2
points: 5.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of Problems T10_CompositeMaterials.pdf (Problems 4 and 7); not an official exercise. Verified with tools/materials_bank/verify_mt3.py"
tags:
  - problem-bank
  - midterm-3
  - unit-10
  - composite-materials
  - aluminium-replacement
  - weight-saving
  - rule-of-mixtures
---

# Bank P23 — Glass-epoxy composite replacing metallic plate

> [!info] Practice item, not an official exercise
> Written for the bank in the style of `Problems T10_CompositeMaterials.pdf` (Problems 4 and 7). Method: Session 21, Slide 18; Session 22, Slides 21–27. Every result is recomputed by tools/materials_bank/verify_mt3.py.

## Statement

An aircraft structural fairing plate measuring $1.20\ \text{m}$ long, $0.25\ \text{m}$ wide, and $8.0\ \text{mm}$ thick is currently machined from aluminium alloy Al 2024-T3. To reduce structural mass, engineers evaluate replacing the metallic plate with a plate of the exact same outer dimensions made from a unidirectional continuous E-glass/epoxy composite containing $55\ \text{vol\%}$ E-glass fibres aligned along the plate length. Constituent and alloy properties are listed below:

| Material | Density ($\text{g/cm}^3$) | Elastic modulus (GPa) | Tensile strength (MPa) |
| :--- | ---: | ---: | ---: |
| E-glass fibre ($f$) | 2.58 | 72.5 | 3450 |
| Epoxy resin ($m$) | 1.20 | 3.20 | 68.0 |
| Al 2024-T3 ($\text{Al}$) | 2.78 | 72.4 | 470 |

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| E-glass volume fraction | $V_f$ | $55\ \%$ | $0.55$ (dimensionless) |
| Epoxy volume fraction | $V_m$ | $1 - V_f = 45\ \%$ | $0.45$ (dimensionless) |
| E-glass density | $\rho_f$ | $2.58\ \text{g/cm}^3$ | $2580\ \text{kg/m}^3$ |
| Epoxy density | $\rho_m$ | $1.20\ \text{g/cm}^3$ | $1200\ \text{kg/m}^3$ |
| Al 2024-T3 density | $\rho_{\text{Al}}$ | $2.78\ \text{g/cm}^3$ | $2780\ \text{kg/m}^3$ |
| E-glass elastic modulus | $E_f$ | $72.5\ \text{GPa}$ | $72.5\times10^{9}\ \text{Pa}$ |
| Epoxy elastic modulus | $E_m$ | $3.20\ \text{GPa}$ | $3.20\times10^{9}\ \text{Pa}$ |
| Al 2024-T3 elastic modulus | $E_{\text{Al}}$ | $72.4\ \text{GPa}$ | $72.4\times10^{9}\ \text{Pa}$ |
| E-glass tensile strength | $\sigma_f$ | $3450\ \text{MPa}$ | $3450\times10^{6}\ \text{Pa}$ |
| Epoxy tensile strength | $\sigma_m$ | $68.0\ \text{MPa}$ | $68.0\times10^{6}\ \text{Pa}$ |
| Plate length | $L$ | $1.20\ \text{m}$ | $1.20\ \text{m}$ |
| Plate width | $b$ | $0.25\ \text{m}$ | $0.25\ \text{m}$ |
| Plate thickness | $t$ | $8.0\ \text{mm}$ | $8.0\times10^{-3}\ \text{m}$ |

#### Model

- Composite density and weight fractions: $\rho_c = V_f\rho_f + V_m\rho_m$ and $w_i = \frac{V_i\rho_i}{\rho_c}$ [Session 22, Slide 27].
- Longitudinal isostrain modulus and load sharing: $E_{1C} = V_f E_f + V_m E_m$ and $\frac{F_f}{F_C} = \frac{V_f E_f}{E_{1C}}$ [Session 22, Slides 21–22].
- Longitudinal composite tensile strength: $\sigma_{1C} = V_f\sigma_f + V_m\sigma_m$ [Session 22, Slide 26].
- Percentage change relative to the replaced metallic baseline: $\Delta X / X_{\text{Al}} = (X_c - X_{\text{Al}})/X_{\text{Al}}$.
- Hypotheses: zero porosity; perfect bonding; unidirectional continuous alignment parallel to the $1.20\ \text{m}$ axis; identical plate volume $\mathcal{V} = L\,b\,t$ for both materials [Session 22, Slide 20].

## (a) From $V_f = 0.55$, determine the composite density $\rho_c$ and the weight fractions $w_f$ and $w_m$. [1.2 pts]

### Hint

Convert the densities to $\text{kg/m}^3$, apply $\rho_c = V_f\rho_f + V_m\rho_m$, and then take each constituent's mass contribution over $\rho_c$.

### Checkpoint

- $\rho_c = 1959\ \text{kg/m}^3 = 1.959\ \text{g/cm}^3$
- $w_f = 0.7243$ ($72.43\ \text{wt\%}$), $w_m = 0.2757$ ($27.57\ \text{wt\%}$)

### Solution

#### Composite density $\rho_c$

With $V_f = 0.55$ and $V_m = 1 - 0.55 = 0.45$, the density of the composite is the volume-weighted sum [Session 22, Slide 27]:

$$\rho_c = V_f\rho_f + V_m\rho_m = 0.55\,(2580\ \text{kg/m}^3) + 0.45\,(1200\ \text{kg/m}^3) = 1419\ \text{kg/m}^3 + 540\ \text{kg/m}^3 = 1959\ \text{kg/m}^3 = 1.959\ \text{g/cm}^3$$

#### Fibre and matrix weight fractions

In $1\ \text{m}^3$ of composite, the glass fibres account for $1419\ \text{kg}$ and the epoxy matrix accounts for $540\ \text{kg}$ out of $1959\ \text{kg}$:

$$w_f = \frac{V_f\rho_f}{\rho_c} = \frac{1419\ \text{kg/m}^3}{1959\ \text{kg/m}^3} = 0.7243 \quad (72.43\ \text{wt\%})$$

$$w_m = \frac{V_m\rho_m}{\rho_c} = \frac{540\ \text{kg/m}^3}{1959\ \text{kg/m}^3} = 0.2757 \quad (27.57\ \text{wt\%})$$

Check: $0.7243 + 0.2757 = 1.0000$. Because E-glass is more than twice as dense as epoxy ($2580$ vs $1200\ \text{kg/m}^3$), the weight fraction of glass fibres ($72.43\ \%$) is much higher than their volume fraction ($55\ \%$).

## (b) Calculate the longitudinal modulus $E_{1C}$ and the percentage stiffness change relative to Al 2024-T3. Explain whether the composite is stiffer or more compliant than the alloy. [1.3 pts]

### Hint

Use the Al 2024-T3 modulus as the denominator in $(E_{1C} - E_{\text{Al}})/E_{\text{Al}}$; pay attention to the sign of the change, because E-glass has nearly the same modulus as aluminium.

### Checkpoint

- $E_{1C} = 41.32\ \text{GPa}$
- Percentage stiffness change: $-42.94\ \%$ (the E-glass/epoxy composite is more compliant than Al 2024-T3)

### Solution

#### Longitudinal elastic modulus $E_{1C}$

Along the fibre direction (isostrain) [Session 22, Slide 22]:

$$E_{1C} = V_f E_f + V_m E_m = 0.55\,(72.5\ \text{GPa}) + 0.45\,(3.20\ \text{GPa}) = 39.875\ \text{GPa} + 1.440\ \text{GPa} = 41.315\ \text{GPa} \approx 41.32\ \text{GPa}$$

#### Percentage change in stiffness relative to Al 2024-T3

Since the composite replaces the aluminium alloy, Al 2024-T3 is the baseline in the denominator:

$$\frac{\Delta E}{E_{\text{Al}}} = \frac{E_{1C} - E_{\text{Al}}}{E_{\text{Al}}} = \frac{41.315\ \text{GPa} - 72.4\ \text{GPa}}{72.4\ \text{GPa}} = \frac{-31.085\ \text{GPa}}{72.4\ \text{GPa}} = -0.4294 \quad (-42.94\ \%)$$

#### Physical explanation

The E-glass/epoxy composite is **$42.94\ \%$ less stiff (more compliant)** than Al 2024-T3. E-glass fibres have almost the same elastic modulus as aluminium ($72.5\ \text{GPa}$ vs $72.4\ \text{GPa}$), so mixing $55\ \text{vol\%}$ E-glass with $45\ \text{vol\%}$ compliant epoxy ($3.20\ \text{GPa}$) necessarily lowers the longitudinal modulus below $72.4\ \text{GPa}$. Unlike carbon/epoxy, glass/epoxy is chosen for high tensile strength and low cost rather than high stiffness [Session 21, Slide 17].

## (c) Estimate the longitudinal tensile strength $\sigma_{1C}$ and the fibre load share $F_f/F_C$. [1.3 pts]

### Hint

Apply the rule of mixtures for longitudinal strength using the tabulated constituent strengths, and obtain the load share from the isostrain stiffness ratio $V_f E_f / E_{1C}$.

### Checkpoint

- $\sigma_{1C} = 1928\ \text{MPa} = 1.928\ \text{GPa}$ (over four times the strength of Al 2024-T3)
- $F_f/F_C = 0.9651$ ($96.51\ \%$ of the axial load carried by the fibres)

### Solution

#### Longitudinal tensile strength $\sigma_{1C}$

Using the rule of mixtures for longitudinal tensile strength [Session 22, Slide 26]:

$$\sigma_{1C} = V_f\sigma_f + V_m\sigma_m = 0.55\,(3450\ \text{MPa}) + 0.45\,(68.0\ \text{MPa}) = 1897.5\ \text{MPa} + 30.6\ \text{MPa} = 1928.1\ \text{MPa} \approx 1928\ \text{MPa}$$

This is $1928.1 / 470 = 4.10$ times the tensile strength of Al 2024-T3 ($470\ \text{MPa}$).

#### Fibre load share $F_f/F_C$

Under longitudinal isostrain loading, $\varepsilon_f = \varepsilon_C = \varepsilon$, with $F_f = \sigma_f A_f = E_f\varepsilon V_f A_C$ and $F_C = E_{1C}\varepsilon A_C$ [Session 22, Slides 21–22]:

$$\frac{F_f}{F_C} = \frac{V_f E_f}{E_{1C}} = \frac{0.55\,(72.5\ \text{GPa})}{41.315\ \text{GPa}} = \frac{39.875}{41.315} = 0.9651 \quad (96.51\ \%)$$

The E-glass fibres carry $96.51\ \%$ of the total axial load, leaving $3.49\ \%$ on the epoxy matrix.

## (d) For the fixed-geometry plate ($1.20\ \text{m} \times 0.25\ \text{m} \times 8.0\ \text{mm}$), determine the masses $m_c$ and $m_{\text{Al}}$, the mass difference $\Delta m$, and the percentage weight change. [1.2 pts]

### Hint

Convert thickness $t = 8.0\ \text{mm}$ to metres to find the plate volume $\mathcal{V}$, multiply by each density in $\text{kg/m}^3$, and compute $(m_c - m_{\text{Al}})/m_{\text{Al}}$.

### Checkpoint

- $\mathcal{V} = 2.400\times10^{-3}\ \text{m}^3$
- $m_c = 4.702\ \text{kg}$, $m_{\text{Al}} = 6.672\ \text{kg}$
- $\Delta m = -1.970\ \text{kg}$ ($1.970\ \text{kg}$ lighter), percentage weight change $= -29.53\ \%$

### Solution

#### Plate volume

Converting $t = 8.0\ \text{mm} = 8.0\times10^{-3}\ \text{m}$:

$$\mathcal{V} = L\,b\,t = (1.20\ \text{m})(0.25\ \text{m})(8.0\times10^{-3}\ \text{m}) = 2.400\times10^{-3}\ \text{m}^3$$

#### Plate masses

Multiplying the volume by the respective densities in SI:

$$m_c = \rho_c\,\mathcal{V} = (1959\ \text{kg/m}^3)(2.400\times10^{-3}\ \text{m}^3) = 4.7016\ \text{kg} \approx 4.702\ \text{kg}$$

$$m_{\text{Al}} = \rho_{\text{Al}}\,\mathcal{V} = (2780\ \text{kg/m}^3)(2.400\times10^{-3}\ \text{m}^3) = 6.672\ \text{kg}$$

#### Mass change and percentage weight change

$$\Delta m = m_c - m_{\text{Al}} = 4.7016\ \text{kg} - 6.672\ \text{kg} = -1.970\ \text{kg}$$

$$\frac{\Delta m}{m_{\text{Al}}} = \frac{-1.9704\ \text{kg}}{6.672\ \text{kg}} = -0.2953 \quad (-29.53\ \%)$$

At fixed geometry, the E-glass/epoxy plate is **$1.970\ \text{kg}$ ($29.53\ \%$) lighter** than the Al 2024-T3 plate (note that under uniform gravity, percentage weight change equals percentage mass change).

## Interpretation

- Replacing Al 2024-T3 at fixed thickness with $55\ \text{vol\%}$ E-glass/epoxy delivers a $29.5\ \%$ mass saving and a fourfold increase in longitudinal strength, at the cost of a $42.9\ \%$ drop in longitudinal modulus (specific modulus drops from $72.4/2.78 = 26.04$ to $41.32/1.959 = 21.09\ \text{MN}\cdot\text{m/kg}$). If stiffness is the limiting design criterion (e.g., deflection or buckling), the composite plate would need a larger thickness or carbon fibres instead of E-glass.
- Control case: even at $V_f = 1.0$ (pure E-glass, $72.5\ \text{GPa}$), the stiffness gain over Al 2024-T3 ($72.4\ \text{GPa}$) would be only $+0.14\ \%$; thus no glass/epoxy volume fraction can match Al 2024-T3 stiffness without exceeding $V_f \approx 99.9\ \%$.
- SI dimensional check: $\mathcal{V} = L b t$ is in $\text{m}^3$; $m = \rho\mathcal{V}$ is in $(\text{kg/m}^3)\cdot\text{m}^3 = \text{kg}$; relative changes $\Delta E/E_{\text{Al}}$ and $\Delta m/m_{\text{Al}}$ are dimensionless ratios.
- Common mistake: placing the new composite value in the denominator when computing percentage change ($(41.32 - 72.4)/41.32 = -75.2\ \%$ instead of $-42.94\ \%$), or assuming every fibre composite is automatically stiffer than aluminium.

## Verification

- rho_c (kg/m^3) | 0.55*2580 + 0.45*1200 | 1959
- rho_c (g/cm^3) | (0.55*2580 + 0.45*1200)/1000 | 1.959
- w_f | (0.55*2580)/(0.55*2580 + 0.45*1200) | 0.7243
- w_m | (0.45*1200)/(0.55*2580 + 0.45*1200) | 0.2757
- E1C (GPa) | 0.55*72.5 + 0.45*3.20 | 41.32
- stiffness change (%) | (0.55*72.5 + 0.45*3.20 - 72.4)/72.4*100 | -42.94
- sigma_1C (MPa) | 0.55*3450 + 0.45*68.0 | 1928
- strength ratio vs Al | (0.55*3450 + 0.45*68.0)/470 | 4.10
- F_f / F_C | (0.55*72.5)/(0.55*72.5 + 0.45*3.20) | 0.9651
- plate volume (m^3) | 1.20*0.25*8.0e-3 | 2.400e-3
- m_c (kg) | (0.55*2580 + 0.45*1200)*(1.20*0.25*8.0e-3) | 4.702
- m_Al (kg) | 2780*(1.20*0.25*8.0e-3) | 6.672
- Delta m (kg) | (0.55*2580 + 0.45*1200 - 2780)*(1.20*0.25*8.0e-3) | -1.970
- mass change (%) | (0.55*2580 + 0.45*1200 - 2780)/2780*100 | -29.53
- specific modulus Al (MN*m/kg) | 72.4/2.78 | 26.04
- specific modulus comp (MN*m/kg) | (0.55*72.5 + 0.45*3.20)/((0.55*2580 + 0.45*1200)/1000) | 21.09
- wrong stiffness denominator (%) | (0.55*72.5 + 0.45*3.20 - 72.4)/(0.55*72.5 + 0.45*3.20)*100 | -75.2

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
