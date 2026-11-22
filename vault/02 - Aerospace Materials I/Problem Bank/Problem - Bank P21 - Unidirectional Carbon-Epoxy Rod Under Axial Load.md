---
materia: Aerospace Materials I
tema: "Unit 10: composite materials"
bank_id: P21
title: "Unidirectional carbon-epoxy rod under axial load"
category: mt3_problem
archetype: composite-unidirectional
level: standard
unit: 10
difficulty: 1
points: 5.0
time_minutes: 25
official: false
origen: "Problem written for the bank in the style of Assessment Test III Paper B (2020, p. 8) in MATERIALS_THIRDPARTIAL_2020_V2.pdf and the final of June 2017 (question 9) in MATERIALS_FINALEXAM_2017_EXTRA.pdf; not an official exercise. Verified with tools/materials_bank/verify_mt3.py"
tags:
  - problem-bank
  - midterm-3
  - unit-10
  - composite-materials
  - rule-of-mixtures
  - isostrain
  - isostress
---

# Bank P21 — Unidirectional carbon-epoxy rod under axial load

> [!info] Practice item, not an official exercise
> Written for the bank in the style of Assessment Test III Paper B (2020, p. 8) and the final of June 2017 (question 9). Method: Session 21, Slide 43; Session 22, Slides 20–27. Every result is recomputed by tools/materials_bank/verify_mt3.py.

## Statement

A structural tie rod for an aircraft control linkage is made from a unidirectional continuous-fibre composite consisting of $60\ \text{vol\%}$ aligned PAN carbon fibres in an epoxy resin matrix. The constituent properties are given in the table below:

| Constituent | Density ($\text{g/cm}^3$) | Elastic modulus (GPa) | Tensile strength (MPa) |
| :--- | ---: | ---: | ---: |
| PAN carbon fibre ($f$) | 1.78 | 280 | 3600 |
| Epoxy resin ($m$) | 1.22 | 3.20 | 72.0 |

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| Fibre volume fraction | $V_f$ | $60\ \%$ | $0.60$ (dimensionless) |
| Matrix volume fraction | $V_m$ | $1 - V_f = 40\ \%$ | $0.40$ (dimensionless) |
| Fibre density | $\rho_f$ | $1.78\ \text{g/cm}^3$ | $1780\ \text{kg/m}^3$ |
| Matrix density | $\rho_m$ | $1.22\ \text{g/cm}^3$ | $1220\ \text{kg/m}^3$ |
| Fibre elastic modulus | $E_f$ | $280\ \text{GPa}$ | $280\times10^{9}\ \text{Pa}$ |
| Matrix elastic modulus | $E_m$ | $3.20\ \text{GPa}$ | $3.20\times10^{9}\ \text{Pa}$ |
| Fibre tensile strength | $\sigma_f^*$ | $3600\ \text{MPa}$ | $3600\times10^{6}\ \text{Pa}$ |
| Matrix tensile strength | $\sigma_m^*$ | $72.0\ \text{MPa}$ | $72.0\times10^{6}\ \text{Pa}$ |
| Rod diameter (part c) | $d$ | $16.0\ \text{mm}$ | $1.60\times10^{-2}\ \text{m}$ |
| Applied longitudinal stress (part c) | $\sigma_C$ | $85.0\ \text{MPa}$ | $85.0\times10^{6}\ \text{Pa}$ |
| Initial rod length (part d) | $L_0$ | $1.40\ \text{m}$ | $1.40\ \text{m}$ |

#### Model

- Longitudinal isostrain loading (direction 1, parallel to the fibres): $\varepsilon_{1C} = \varepsilon_f = \varepsilon_m$, $\sigma_{1C} = V_f\sigma_f + V_m\sigma_m$, and $E_{1C} = V_f E_f + V_m E_m$ [Session 22, Slides 21–22].
- Transverse isostress loading (direction 2, perpendicular to the fibres): $\sigma_{2C} = \sigma_f = \sigma_m$, $\varepsilon_{2C} = V_f\varepsilon_f + V_m\varepsilon_m$, and $\frac{1}{E_{2C}} = \frac{V_f}{E'_f} + \frac{V_m}{E_m}$ [Session 22, Slides 23–24].
- Composite density and weight fractions: $\rho_c = V_f\rho_f + V_m\rho_m$ and $w_i = \frac{V_i\rho_i}{\rho_c}$ [Session 22, Slide 27].
- Longitudinal composite tensile strength (rule of mixtures): $\sigma_{1C}^* = V_f\sigma_f^* + V_m\sigma_m^*$ [Session 22, Slide 26].
- Specific tensile strength: $\sigma_{1C}^*/\rho_c$ [Session 21, Slide 43].
- Hypotheses: zero porosity ($V_f + V_m = 1$); continuous, perfectly aligned, uniformly spaced, linearly elastic and isotropic fibres ($E'_f = E_f$); linearly elastic, homogeneous, isotropic matrix; perfect interfacial bonding with no debonding or slip [Session 22, Slide 20].

## (a) Determine the longitudinal elastic modulus $E_{1C}$ and the transverse elastic modulus $E_{2C}$ of the composite. [1.2 pts]

### Hint

Apply the isostrain rule of mixtures along the fibres (direction 1) and the isostress inverse rule of mixtures perpendicular to the fibres (direction 2).

### Checkpoint

- $E_{1C} = 169.3\ \text{GPa} = 1.693\times10^{11}\ \text{Pa}$
- $E_{2C} = 7.865\ \text{GPa} = 7.865\times10^{9}\ \text{Pa}$

### Solution

#### Longitudinal modulus $E_{1C}$ under isostrain conditions

Along direction 1 (parallel to the fibres), the strain is identical in fibres and matrix, giving the rule of mixtures [Session 22, Slide 22]:

$$E_{1C} = V_f E_f + V_m E_m = V_f E_f + (1 - V_f) E_m$$

Substituting $V_f = 0.60$, $V_m = 0.40$, $E_f = 280\times10^{9}\ \text{Pa}$, and $E_m = 3.20\times10^{9}\ \text{Pa}$:

$$E_{1C} = 0.60\,(280\times10^{9}\ \text{Pa}) + 0.40\,(3.20\times10^{9}\ \text{Pa}) = 1.680\times10^{11}\ \text{Pa} + 1.280\times10^{9}\ \text{Pa} = 1.693\times10^{11}\ \text{Pa} = 169.3\ \text{GPa}$$

Notice that the fibres contribute $168.0/169.28 = 99.2\ \%$ of the longitudinal stiffness, while the matrix contributes less than $1\ \%$.

#### Transverse modulus $E_{2C}$ under isostress conditions

Perpendicular to the fibres (direction 2), fibres and matrix carry the same stress in series, so their strains add in proportion to volume fraction [Session 22, Slides 23–24]. Treating the fibres as isotropic ($E'_f = E_f = 280\times10^{9}\ \text{Pa}$):

$$\frac{1}{E_{2C}} = \frac{V_f}{E_f} + \frac{V_m}{E_m} = \frac{0.60}{280\times10^{9}\ \text{Pa}} + \frac{0.40}{3.20\times10^{9}\ \text{Pa}}$$

Evaluating each compliance term explicitly:

$$\frac{1}{E_{2C}} = 2.143\times10^{-12}\ \text{Pa}^{-1} + 1.250\times10^{-10}\ \text{Pa}^{-1} = 1.271\times10^{-10}\ \text{Pa}^{-1}$$

Taking the reciprocal gives the transverse elastic modulus:

$$E_{2C} = \frac{1}{1.2714\times10^{-10}\ \text{Pa}^{-1}} = 7.865\times10^{9}\ \text{Pa} = 7.865\ \text{GPa}$$

Equivalently, putting the fractions over a common denominator gives $E_{2C} = \frac{E_f E_m}{V_f E_m + V_m E_f} = \frac{280\times 3.20}{0.60\times 3.20 + 0.40\times 280} = \frac{896.0}{113.92} = 7.865\ \text{GPa}$.

## (b) Calculate the composite density $\rho_c$ and the weight fractions $w_f$ and $w_m$ of the fibres and epoxy matrix. [1.0 pts]

### Hint

Compute the mass of each constituent in $1\ \text{m}^3$ (or $1\ \text{cm}^3$) of composite, sum them to get $\rho_c$, and divide each constituent mass by $\rho_c$.

### Checkpoint

- $\rho_c = 1556\ \text{kg/m}^3 = 1.556\ \text{g/cm}^3$
- $w_f = 0.6864$ ($68.64\ \text{wt\%}$), $w_m = 0.3136$ ($31.36\ \text{wt\%}$)

### Solution

#### Composite density $\rho_c$

With zero porosity, $1\ \text{m}^3$ of composite contains $0.60\ \text{m}^3$ of carbon fibres and $0.40\ \text{m}^3$ of epoxy. Applying the rule of mixtures for density [Session 22, Slide 27] with $\rho_f = 1780\ \text{kg/m}^3$ and $\rho_m = 1220\ \text{kg/m}^3$:

$$\rho_c = V_f\rho_f + V_m\rho_m = 0.60\,(1780\ \text{kg/m}^3) + 0.40\,(1220\ \text{kg/m}^3) = 1068\ \text{kg/m}^3 + 488\ \text{kg/m}^3 = 1556\ \text{kg/m}^3$$

Converting back to $\text{g/cm}^3$ ($1000\ \text{kg/m}^3 = 1\ \text{g/cm}^3$), $\rho_c = 1.556\ \text{g/cm}^3$.

#### Weight fractions $w_f$ and $w_m$

In $1\ \text{m}^3$ of composite, the fibre mass is $m_f = V_f\rho_f = 1068\ \text{kg}$ and the matrix mass is $m_m = V_m\rho_m = 488\ \text{kg}$, out of a total mass $\rho_c = 1556\ \text{kg}$:

$$w_f = \frac{V_f\rho_f}{\rho_c} = \frac{1068\ \text{kg/m}^3}{1556\ \text{kg/m}^3} = 0.6864 \quad (68.64\ \text{wt\%})$$

$$w_m = \frac{V_m\rho_m}{\rho_c} = \frac{488\ \text{kg/m}^3}{1556\ \text{kg/m}^3} = 0.3136 \quad (31.36\ \text{wt\%})$$

Check: $w_f + w_m = 0.6864 + 0.3136 = 1.0000$. Because carbon fibres are denser than epoxy ($1780 > 1220\ \text{kg/m}^3$), their mass fraction ($68.64\ \%$) exceeds their volume fraction ($60.0\ \%$).

## (c) A cylindrical rod $16.0\ \text{mm}$ in diameter is stressed longitudinally to $85.0\ \text{MPa}$. Find the total axial force $F_C$, the load ratio $F_f/F_m$, the forces $F_f$ and $F_m$, and the phase stresses $\sigma_f$ and $\sigma_m$. [1.6 pts]

### Hint

Find the cross-sectional area $A_C$ first to obtain $F_C = \sigma_C A_C$. Under isostrain ($\varepsilon_f = \varepsilon_m$), express $F_f/F_m$ in terms of $E_f V_f$ and $E_m V_m$, and compute the common strain $\varepsilon = \sigma_C/E_{1C}$ to evaluate $\sigma_f$ and $\sigma_m$.

### Checkpoint

- $A_C = 2.011\times10^{-4}\ \text{m}^2$, $F_C = 17\,090\ \text{N}$ ($17.09\ \text{kN}$)
- $F_f/F_m = 131.3$, $F_f = 16\,961\ \text{N}$, $F_m = 129.2\ \text{N}$
- $\varepsilon = 5.021\times10^{-4}$, $\sigma_f = 140.6\ \text{MPa}$, $\sigma_m = 1.607\ \text{MPa}$

### Solution

#### Cross-sectional area and total axial force

With diameter $d = 16.0\ \text{mm} = 1.60\times10^{-2}\ \text{m}$, the circular cross-sectional area is:

$$A_C = \frac{\pi d^2}{4} = \frac{\pi\,(1.60\times10^{-2}\ \text{m})^2}{4} = \frac{\pi\,(2.56\times10^{-4}\ \text{m}^2)}{4} = 2.011\times10^{-4}\ \text{m}^2$$

Multiplying by the applied longitudinal stress $\sigma_C = 85.0\times10^{6}\ \text{Pa}$ gives the total axial force:

$$F_C = \sigma_C A_C = (85.0\times10^{6}\ \text{N/m}^2)(2.0106\times10^{-4}\ \text{m}^2) = 17\,090\ \text{N} = 17.09\ \text{kN}$$

#### Fibre-to-matrix load ratio $F_f/F_m$

Under isostrain loading, $\varepsilon_f = \varepsilon_m = \varepsilon$ and both constituents share the same length, so the area ratio equals the volume-fraction ratio, $A_f/A_m = V_f/V_m$ [Session 22, Slides 21–22]. Using Hooke's law $\sigma_i = E_i\varepsilon$ in each constituent:

$$\frac{F_f}{F_m} = \frac{\sigma_f A_f}{\sigma_m A_m} = \frac{(E_f\varepsilon)(V_f A_C)}{(E_m\varepsilon)(V_m A_C)} = \frac{E_f V_f}{E_m V_m}$$

Substituting the numbers:

$$\frac{F_f}{F_m} = \frac{(280\times10^{9}\ \text{Pa})(0.60)}{(3.20\times10^{9}\ \text{Pa})(0.40)} = \frac{1.680\times10^{11}}{1.280\times10^{9}} = 131.25 \approx 131.3$$

#### Forces $F_f$ and $F_m$ carried by fibres and matrix

From $F_C = F_f + F_m$ and $F_f = 131.25\,F_m$, substituting into the total force gives $F_C = 132.25\,F_m$, or equivalently using the load-share fractions $F_f/F_C = V_f E_f / E_{1C}$:

$$F_f = F_C\,\frac{V_f E_f}{E_{1C}} = 17\,090\ \text{N}\times\frac{168.0\ \text{GPa}}{169.28\ \text{GPa}} = 17\,090\ \text{N}\times 0.99244 = 16\,961\ \text{N}$$

$$F_m = F_C - F_f = 17\,090\ \text{N} - 16\,961\ \text{N} = 129.2\ \text{N}$$

Check: $F_f/F_m = 16\,961 / 129.2 = 131.3$, and the fibres carry $99.24\ \%$ of the axial load.

#### Longitudinal strain and constituent stresses $\sigma_f$ and $\sigma_m$

First check that the composite is in the linear elastic regime by computing the common axial strain $\varepsilon = \sigma_C / E_{1C}$:

$$\varepsilon = \frac{\sigma_C}{E_{1C}} = \frac{85.0\times10^{6}\ \text{Pa}}{1.6928\times10^{11}\ \text{Pa}} = 5.021\times10^{-4}$$

Applying Hooke's law $\sigma_i = E_i\varepsilon$ to each constituent:

$$\sigma_f = E_f\varepsilon = (280\times10^{9}\ \text{Pa})(5.0213\times10^{-4}) = 1.406\times10^{8}\ \text{Pa} = 140.6\ \text{MPa}$$

$$\sigma_m = E_m\varepsilon = (3.20\times10^{9}\ \text{Pa})(5.0213\times10^{-4}) = 1.607\times10^{6}\ \text{Pa} = 1.607\ \text{MPa}$$

As an independent cross-check, $\sigma_f = F_f / (V_f A_C) = 16\,961 / (0.60\times 2.0106\times10^{-4}) = 140.6\ \text{MPa}$ and $\sigma_m = F_m / (V_m A_C) = 129.2 / (0.40\times 2.0106\times10^{-4}) = 1.607\ \text{MPa}$. Both stresses are far below the failure strengths ($140.6\ \text{MPa} \ll 3600\ \text{MPa}$ and $1.607\ \text{MPa} \ll 72.0\ \text{MPa}$), confirming elastic behaviour.

## (d) Calculate the axial elongation $\Delta L$ of a $1.40\ \text{m}$ rod under this stress, and estimate the composite's longitudinal specific tensile strength $\sigma_{1C}^*/\rho_c$. [1.2 pts]

### Hint

Use $\Delta L = \varepsilon L_0$ from the axial strain found in part (c), compute $\sigma_{1C}^*$ by the rule of mixtures, and divide by $\rho_c$ in $\text{kg/m}^3$.

### Checkpoint

- $\Delta L = 7.030\times10^{-4}\ \text{m} = 0.703\ \text{mm}$
- $\sigma_{1C}^* = 2189\ \text{MPa}$, $\sigma_{1C}^*/\rho_c = 1407\ \text{kN}\cdot\text{m/kg} = 1.407\times10^{6}\ \text{m}^2/\text{s}^2$

### Solution

#### Axial elongation $\Delta L$

From the definition of engineering strain $\varepsilon = \Delta L / L_0$, multiplying both sides by $L_0 = 1.40\ \text{m}$ gives:

$$\Delta L = \varepsilon\,L_0 = (5.0213\times10^{-4})(1.40\ \text{m}) = 7.030\times10^{-4}\ \text{m} = 0.703\ \text{mm}$$

#### Longitudinal tensile strength $\sigma_{1C}^*$ and specific strength $\sigma_{1C}^*/\rho_c$

Using the rule of mixtures for longitudinal tensile strength [Session 22, Slide 26] with the tabulated fibre and matrix strengths:

$$\sigma_{1C}^* = V_f\sigma_f^* + V_m\sigma_m^* = 0.60\,(3600\ \text{MPa}) + 0.40\,(72.0\ \text{MPa}) = 2160\ \text{MPa} + 28.8\ \text{MPa} = 2188.8\ \text{MPa} \approx 2189\ \text{MPa}$$

Dividing by the composite density in SI ($\rho_c = 1556\ \text{kg/m}^3$) [Session 21, Slide 43]:

$$\frac{\sigma_{1C}^*}{\rho_c} = \frac{2188.8\times10^{6}\ \text{N/m}^2}{1556\ \text{kg/m}^3} = 1.407\times10^{6}\ \frac{\text{N}\cdot\text{m}}{\text{kg}} = 1407\ \text{kN}\cdot\text{m/kg} = 1.407\ \text{MJ/kg}$$

Notice the exact equivalence $(\text{MPa}\cdot\text{cm}^3/\text{g}) = \text{kN}\cdot\text{m/kg}$: $2188.8 / 1.556 = 1407\ \text{kN}\cdot\text{m/kg}$.

## Interpretation

- The unidirectional carbon-epoxy rod shows extreme anisotropy: $E_{1C}/E_{2C} = 169.3 / 7.865 = 21.5$. Along the fibres, the carbon reinforcement carries $99.24\ \%$ of the load ($F_f/F_m = 131.3$) at a stress of $140.6\ \text{MPa}$ compared with $1.607\ \text{MPa}$ in the epoxy, because $\sigma_f/\sigma_m = E_f/E_m = 87.5$. Across the fibres, the compliant epoxy dominates and the matrix-only approximation $E_m/V_m = 3.20/0.40 = 8.00\ \text{GPa}$ [Session 22, Slide 24] lies within $1.7\ \%$ of the exact $7.865\ \text{GPa}$.
- Control case: if the matrix stiffness vanished ($E_m \to 0$), then $E_{1C} \to V_f E_f = 168.0\ \text{GPa}$, $F_f/F_C \to 1$, and $E_{2C} \to 0$ (zero transverse load path). Conversely, if $V_f \to 0$, all properties revert to neat epoxy ($\rho = 1220\ \text{kg/m}^3$, $E = 3.20\ \text{GPa}$, $\sigma = 72.0\ \text{MPa}$).
- SI dimensional check: $F_C = \sigma_C A_C$ has units $(\text{N/m}^2)\cdot\text{m}^2 = \text{N}$; $E_i\varepsilon$ is $\text{Pa}\times 1 = \text{Pa}$; $\Delta L = \varepsilon L_0$ is in $\text{m}$; and specific strength $\sigma_{1C}^*/\rho_c$ has units $(\text{N/m}^2)/(\text{kg/m}^3) = \text{N}\cdot\text{m/kg} = \text{m}^2/\text{s}^2 = \text{J/kg}$.
- Common mistake: splitting the axial force by volume fraction ($F_f = 0.60\,F_C = 10\,254\ \text{N}$) instead of stiffness-weighted area ($V_f E_f / E_{1C} = 0.9924$), or forgetting to convert $\text{g/cm}^3$ to $\text{kg/m}^3$ when computing specific strength in SI ($\text{N}\cdot\text{m/kg}$).

## Verification

- E1C (GPa) | (0.60*280e9 + 0.40*3.20e9)/1e9 | 169.3
- E2C (GPa) | 1/(0.60/280e9 + 0.40/3.20e9)/1e9 | 7.865
- E2 approx (GPa) | (3.20e9/0.40)/1e9 | 8.00
- E1C over E2C | (0.60*280e9 + 0.40*3.20e9)/(1/(0.60/280e9 + 0.40/3.20e9)) | 21.5
- rho_c (kg/m^3) | 0.60*1780 + 0.40*1220 | 1556
- rho_c (g/cm^3) | (0.60*1780 + 0.40*1220)/1000 | 1.556
- w_f | (0.60*1780)/(0.60*1780 + 0.40*1220) | 0.6864
- w_m | (0.40*1220)/(0.60*1780 + 0.40*1220) | 0.3136
- A_C (m^2) | pi*(16.0e-3)**2/4 | 2.011e-4
- F_C (N) | 85.0e6 * (pi*(16.0e-3)**2/4) | 17090
- F_f / F_m | (0.60*280e9)/(0.40*3.20e9) | 131.3
- F_f (N) | 85.0e6*(pi*(16.0e-3)**2/4)*(0.60*280e9)/(0.60*280e9 + 0.40*3.20e9) | 16961
- F_m (N) | 85.0e6*(pi*(16.0e-3)**2/4)*(0.40*3.20e9)/(0.60*280e9 + 0.40*3.20e9) | 129.2
- strain eps | 85.0e6/(0.60*280e9 + 0.40*3.20e9) | 5.021e-4
- sigma_f (MPa) | 280e9*85.0e6/(0.60*280e9 + 0.40*3.20e9)/1e6 | 140.6
- sigma_m (MPa) | 3.20e9*85.0e6/(0.60*280e9 + 0.40*3.20e9)/1e6 | 1.607
- Delta L (mm) | 85.0e6/(0.60*280e9 + 0.40*3.20e9)*1.40*1e3 | 0.703
- sigma_1C* (MPa) | (0.60*3600e6 + 0.40*72.0e6)/1e6 | 2189
- specific strength (kN*m/kg) | (0.60*3600e6 + 0.40*72.0e6)/(0.60*1780 + 0.40*1220)/1e3 | 1407

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
