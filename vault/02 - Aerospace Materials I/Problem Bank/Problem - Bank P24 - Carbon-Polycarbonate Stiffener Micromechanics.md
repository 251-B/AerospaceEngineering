---
materia: Aerospace Materials I
tema: "Unit 10: composite materials"
bank_id: P24
title: "Carbon-polycarbonate stiffener micromechanics"
category: mt3_problem
archetype: composite-unidirectional
level: conceptual
unit: 10
difficulty: 2
points: 5.0
time_minutes: 25
official: false
origen: "Problem written for the bank in the style of the final of June 2017 (question 9) in MATERIALS_FINALEXAM_2017_EXTRA.pdf, the final of June 2014 (question 2) in MATERIALS_FINALEXAM_COMPILATION_2013-2017.pdf, and the final of June 2016 (question 9) in MATERIALS_FINALEXAM_2016_EXTRA_SOL.pdf; not an official exercise. Verified with tools/materials_bank/verify_mt3.py"
tags:
  - problem-bank
  - midterm-3
  - unit-10
  - composite-materials
  - micromechanics
  - load-sharing
  - critical-volume-fraction
---

# Bank P24 — Carbon-polycarbonate stiffener micromechanics

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the finals of June 2017 (question 9), June 2014 (question 2), and June 2016 (question 9). Method: Session 22, Slides 20–26. Every result is recomputed by tools/materials_bank/verify_mt3.py.

## Statement

A continuous, aligned fibre-reinforced thermoplastic stiffener is produced from $38\ \text{vol\%}$ PAN carbon fibres and $62\ \text{vol\%}$ polycarbonate (PC) matrix, with a cross-sectional area of $280\ \text{mm}^2$. In service it supports a longitudinal tensile load of $52.0\ \text{kN}$ parallel to the fibres. The elastic moduli are $E_f = 240\ \text{GPa}$ for the carbon fibres and $E_m = 2.40\ \text{GPa}$ for the polycarbonate matrix. The tensile strength of the carbon fibres is $\sigma_f^* = 3400\ \text{MPa}$, the matrix stress at the fibre-fracture strain is $\sigma'_m = 34.0\ \text{MPa}$, and the ultimate tensile strength of unreinforced polycarbonate is $\sigma_m^* = 65.0\ \text{MPa}$.

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| Fibre volume fraction | $V_f$ | $38\ \%$ | $0.38$ (dimensionless) |
| Matrix volume fraction | $V_m$ | $62\ \%$ | $0.62$ (dimensionless) |
| Cross-sectional area | $A_C$ | $280\ \text{mm}^2$ | $2.80\times10^{-4}\ \text{m}^2$ |
| Longitudinal axial force | $F_C$ | $52.0\ \text{kN}$ | $52.0\times10^{3}\ \text{N}$ |
| Carbon fibre modulus | $E_f$ | $240\ \text{GPa}$ | $240\times10^{9}\ \text{Pa}$ |
| Polycarbonate matrix modulus | $E_m$ | $2.40\ \text{GPa}$ | $2.40\times10^{9}\ \text{Pa}$ |
| Carbon fibre tensile strength | $\sigma_f^*$ | $3400\ \text{MPa}$ | $3400\times10^{6}\ \text{Pa}$ |
| Matrix stress at fibre-fracture strain | $\sigma'_m$ | $34.0\ \text{MPa}$ | $34.0\times10^{6}\ \text{Pa}$ |
| Polycarbonate ultimate tensile strength | $\sigma_m^*$ | $65.0\ \text{MPa}$ | $65.0\times10^{6}\ \text{Pa}$ |

#### Model

- Longitudinal isostrain loading: $\varepsilon_{1C} = \varepsilon_f = \varepsilon_m$, $E_{1C} = V_f E_f + V_m E_m$, and $F_C = F_f + F_m$ [Session 22, Slides 21–22].
- Transverse isostress loading: $\sigma_{2C} = \sigma_f = \sigma_m$ and $\frac{1}{E_{2C}} = \frac{V_f}{E'_f} + \frac{V_m}{E_m}$ [Session 22, Slides 23–24].
- Longitudinal tensile strength before fibre fracture: $\sigma_{1C} = V_f\sigma_f^* + (1 - V_f)\sigma'_m$ [Session 22, Slide 26].
- Post-fibre-fracture residual composite strength (carried by matrix alone): $\sigma_{C,\text{res}} = \sigma_m^*(1 - V_f)$ [Session 22, Slide 26].
- Minimum and critical fibre volume fractions: intersection of the two failure lines $V_{\min} = \frac{\sigma_m^* - \sigma'_m}{\sigma_f^* + \sigma_m^* - \sigma'_m}$, and strengthening threshold $V_{\text{crit}} = \frac{\sigma_m^* - \sigma'_m}{\sigma_f^* - \sigma'_m}$ [Session 22, Slide 26].
- Hypotheses: continuous aligned fibres with perfect bonding; isotropic linearly elastic fibres ($E'_f = E_f$) up to brittle fracture at $\varepsilon_f^* = \sigma_f^*/E_f$; no void porosity [Session 22, Slide 20].

## (a) Compute the longitudinal elastic modulus $E_{1C}$ and transverse elastic modulus $E_{2C}$ of the stiffener. [1.2 pts]

### Hint

Apply the isostrain rule of mixtures along the fibres and the isostress harmonic rule perpendicular to the fibres.

### Checkpoint

- $E_{1C} = 92.69\ \text{GPa} = 9.269\times10^{10}\ \text{Pa}$
- $E_{2C} = 3.847\ \text{GPa} = 3.847\times10^{9}\ \text{Pa}$

### Solution

#### Longitudinal elastic modulus $E_{1C}$

With $V_f = 0.38$ and $V_m = 0.62$, the isostrain rule of mixtures [Session 22, Slide 22] yields:

$$E_{1C} = V_f E_f + V_m E_m = 0.38\,(240\times10^{9}\ \text{Pa}) + 0.62\,(2.40\times10^{9}\ \text{Pa}) = 9.120\times10^{10}\ \text{Pa} + 1.488\times10^{9}\ \text{Pa} = 9.269\times10^{10}\ \text{Pa} = 92.69\ \text{GPa}$$

#### Transverse elastic modulus $E_{2C}$

Perpendicular to the fibres (isostress) [Session 22, Slide 24], with $E'_f = E_f = 240\times10^{9}\ \text{Pa}$:

$$\frac{1}{E_{2C}} = \frac{V_f}{E_f} + \frac{V_m}{E_m} = \frac{0.38}{240\times10^{9}\ \text{Pa}} + \frac{0.62}{2.40\times10^{9}\ \text{Pa}} = 1.583\times10^{-12}\ \text{Pa}^{-1} + 2.583\times10^{-10}\ \text{Pa}^{-1} = 2.599\times10^{-10}\ \text{Pa}^{-1}$$

Inverting gives the transverse modulus:

$$E_{2C} = \frac{1}{2.5992\times10^{-10}\ \text{Pa}^{-1}} = 3.847\times10^{9}\ \text{Pa} = 3.847\ \text{GPa}$$

## (b) Calculate the fibre-to-matrix load ratio $F_f/F_m$ under longitudinal loading and explain physically why one constituent supports almost the entire load. [1.2 pts]

### Hint

Combine $F_i = \sigma_i A_i$, $\sigma_i = E_i\varepsilon$, and $A_f/A_m = V_f/V_m$ under the isostrain condition $\varepsilon_f = \varepsilon_m$.

### Checkpoint

- $F_f/F_m = 61.29$ (fibres carry $98.39\ \%$ of the axial load)

### Solution

#### Derivation and value of $F_f/F_m$

For continuous aligned fibres of uniform length ($L_f = L_m = L_C$), the ratio of constituent cross-sectional areas equals the ratio of volume fractions, $A_f / A_m = V_f / V_m$ [Session 22, Slide 21]. Because the bond is perfect, both constituents experience the exact same axial strain ($\varepsilon_f = \varepsilon_m = \varepsilon$). By Hooke's law, $\sigma_f = E_f\varepsilon$ and $\sigma_m = E_m\varepsilon$, so:

$$\frac{F_f}{F_m} = \frac{\sigma_f A_f}{\sigma_m A_m} = \frac{(E_f\varepsilon)(V_f A_C)}{(E_m\varepsilon)(V_m A_C)} = \frac{E_f V_f}{E_m V_m}$$

Substituting the given moduli and volume fractions:

$$\frac{F_f}{F_m} = \frac{(240\times10^{9}\ \text{Pa})(0.38)}{(2.40\times10^{9}\ \text{Pa})(0.62)} = \frac{9.120\times10^{10}}{1.488\times10^{9}} = 61.29$$

The corresponding load share carried by the fibres is $F_f/F_C = 61.29/(61.29 + 1) = 0.9839$ ($98.39\ \%$).

#### Physical justification

Under longitudinal isostrain loading, the matrix and the fibres are forced to stretch by the same fraction $\varepsilon$. Because the carbon fibres are $E_f / E_m = 240 / 2.40 = 100$ times stiffer than the polycarbonate matrix, developing the same strain $\varepsilon$ requires $100$ times more stress in the fibres ($\sigma_f = 100\,\sigma_m$) [Session 22, Slide 22]. Even though the fibres occupy only $38\ \%$ of the area, their hundredfold higher modulus causes the matrix to transfer almost all axial force into the fibres ($98.39\ \%$), fulfilling the primary load-bearing function of the reinforcement while the polymer matrix serves to distribute stress, separate fibres, and preserve geometry [Session 21, Slide 16].

## (c) Under the longitudinal load of $52.0\ \text{kN}$ on the $280\ \text{mm}^2$ section, compute the composite strain $\varepsilon$ and the stresses $\sigma_f$ and $\sigma_m$ in the fibre and matrix phases. [1.3 pts]

### Hint

Convert $A_C = 280\ \text{mm}^2$ to $\text{m}^2$, compute the average stress $\sigma_C = F_C/A_C$, divide by $E_{1C}$ to obtain the shared strain $\varepsilon$, and multiply $\varepsilon$ by $E_f$ and $E_m$.

### Checkpoint

- $\sigma_C = 185.7\ \text{MPa}$, $\varepsilon = 2.004\times10^{-3}$
- $\sigma_f = 480.9\ \text{MPa}$, $\sigma_m = 4.809\ \text{MPa}$

### Solution

#### Average composite stress and shared axial strain

Converting the area to SI ($1\ \text{mm}^2 = 10^{-6}\ \text{m}^2$) gives $A_C = 280\times10^{-6}\ \text{m}^2 = 2.80\times10^{-4}\ \text{m}^2$. With $F_C = 52.0\ \text{kN} = 5.20\times10^{4}\ \text{N}$:

$$\sigma_C = \frac{F_C}{A_C} = \frac{5.20\times10^{4}\ \text{N}}{2.80\times10^{-4}\ \text{m}^2} = 1.857\times10^{8}\ \text{Pa} = 185.7\ \text{MPa}$$

Using Hooke's law for the composite along direction 1 with $E_{1C} = 9.2688\times10^{10}\ \text{Pa}$:

$$\varepsilon = \frac{\sigma_C}{E_{1C}} = \frac{1.8571\times10^{8}\ \text{Pa}}{9.2688\times10^{10}\ \text{Pa}} = 2.004\times10^{-3}$$

#### Stresses in the fibre and matrix phases

Since $\varepsilon_f = \varepsilon_m = \varepsilon = 2.0036\times10^{-3}$ (isostrain), Hooke's law gives each constituent stress:

$$\sigma_f = E_f\varepsilon = (240\times10^{9}\ \text{Pa})(2.0036\times10^{-3}) = 4.809\times10^{8}\ \text{Pa} = 480.9\ \text{MPa}$$

$$\sigma_m = E_m\varepsilon = (2.40\times10^{9}\ \text{Pa})(2.0036\times10^{-3}) = 4.809\times10^{6}\ \text{Pa} = 4.809\ \text{MPa}$$

Check: $\sigma_C = V_f\sigma_f + V_m\sigma_m = 0.38(480.88) + 0.62(4.809) = 182.73 + 2.98 = 185.7\ \text{MPa}$, and $\sigma_f/\sigma_m = 100.0 = E_f/E_m$.

## (d) Compute the composite's longitudinal tensile strength $\sigma_{1C}$ and its post-fibre-fracture residual strength $\sigma_m^*(1 - V_f)$. Verify $V_f > V_{\min}$ and explain why unreinforced polycarbonate is stronger than the post-fibre-fracture residual composite strength. [1.3 pts]

### Hint

Compare the composite strength before fibre fracture, $\sigma_{1C} = V_f\sigma_f^* + (1 - V_f)\sigma'_m$, with the post-fracture residual strength carried by the matrix alone, $\sigma_{C,\text{res}} = \sigma_m^*(1 - V_f)$, and equate them to isolate $V_{\min}$.

### Checkpoint

- $\sigma_{1C} = 1313\ \text{MPa}$, $\sigma_{C,\text{res}} = 40.30\ \text{MPa}$
- $V_{\min} = 9.035\times10^{-3}$ ($0.904\ \text{vol\%}$), $V_{\text{crit}} = 9.210\times10^{-3}$ ($0.921\ \text{vol\%}$): $V_f = 0.38 \gg V_{\min}$ and $V_{\text{crit}}$
- Unreinforced PC ($65.0\ \text{MPa}$) exceeds $\sigma_{C,\text{res}} = 40.30\ \text{MPa}$ because broken fibres leave only $(1 - V_f) = 62\ \%$ of the area to carry load

### Solution

#### Longitudinal tensile strength at fibre fracture

Because the brittle carbon fibres fracture before the ductile polycarbonate matrix (at $\varepsilon_f^* = 3400\ \text{MPa} / 240\,000\ \text{MPa} = 1.417\times10^{-2}$), the peak composite strength when the fibres break is [Session 22, Slide 26]:

$$\sigma_{1C} = V_f\sigma_f^* + (1 - V_f)\sigma'_m = 0.38\,(3400\ \text{MPa}) + 0.62\,(34.0\ \text{MPa}) = 1292\ \text{MPa} + 21.08\ \text{MPa} = 1313.1\ \text{MPa} \approx 1313\ \text{MPa}$$

Note that $\sigma'_m = E_m\varepsilon_f^* = 2400\ \text{MPa}\times 0.01417 = 34.0\ \text{MPa}$ is indeed the elastic matrix stress at the fibre fracture strain.

#### Post-fibre-fracture residual composite strength

Once the fibres fracture, they carry no load across the fracture plane and act effectively as void holes; only the remaining matrix cross-sectional fraction $(1 - V_f)$ supports the force [Session 22, Slide 26]:

$$\sigma_{C,\text{res}} = \sigma_m^*(1 - V_f) = (65.0\ \text{MPa})(1 - 0.38) = (65.0\ \text{MPa})(0.62) = 40.30\ \text{MPa}$$

This residual stress ($40.30\ \text{MPa}$) is far below $\sigma_{1C} = 1313\ \text{MPa}$ and also below the unreinforced matrix strength ($\sigma_m^* = 65.0\ \text{MPa}$) because $38\ \%$ of the load-bearing section has been lost to broken fibres.

#### Verification of $V_f > V_{\min}$ and $V_{\text{crit}}$

The minimum volume fraction $V_{\min}$ is the intersection where the fibre-governed line equals the post-fracture residual matrix line [Session 22, Slide 26]:

$$\sigma_f^* V_{\min} + \sigma'_m(1 - V_{\min}) = \sigma_m^*(1 - V_{\min})$$

Expanding the brackets and collecting terms in $V_{\min}$ on the left-hand side:

$$\sigma_f^* V_{\min} + \sigma'_m - \sigma'_m V_{\min} = \sigma_m^* - \sigma_m^* V_{\min}$$

$$\left(\sigma_f^* + \sigma_m^* - \sigma'_m\right) V_{\min} = \sigma_m^* - \sigma'_m$$

Dividing both sides by $(\sigma_f^* + \sigma_m^* - \sigma'_m)$ isolates $V_{\min}$:

$$V_{\min} = \frac{\sigma_m^* - \sigma'_m}{\sigma_f^* + \sigma_m^* - \sigma'_m} = \frac{65.0 - 34.0}{3400 + 65.0 - 34.0} = \frac{31.0\ \text{MPa}}{3431\ \text{MPa}} = 9.035\times10^{-3} \quad (0.904\ \text{vol\%})$$

Similarly, the critical volume fraction $V_{\text{crit}}$ required for the composite to exceed the strength of the unreinforced matrix ($\sigma_{1C} > \sigma_m^*$) satisfies $\sigma_f^* V_{\text{crit}} + \sigma'_m(1 - V_{\text{crit}}) = \sigma_m^*$:

$$V_{\text{crit}} = \frac{\sigma_m^* - \sigma'_m}{\sigma_f^* - \sigma'_m} = \frac{65.0 - 34.0}{3400 - 34.0} = \frac{31.0\ \text{MPa}}{3366\ \text{MPa}} = 9.210\times10^{-3} \quad (0.921\ \text{vol\%})$$

Since $V_f = 0.38 \gg V_{\text{crit}} > V_{\min}$, the carbon fibres truly reinforce the polycarbonate matrix: the stiffener fails catastrophically at $\sigma_{1C} = 1313\ \text{MPa}$ when the fibres break, because the residual matrix alone ($40.30\ \text{MPa}$) cannot carry the $1313\ \text{MPa}$ load.

## Interpretation

- The stress-strain curve of the composite lies between the brittle high-slope fibre curve and the ductile low-slope matrix curve (`Session 22`, Slide 26). At $V_f = 38\ \%$, the composite is $20.2$ times stronger than unreinforced polycarbonate ($1313\ \text{MPa}$ vs $65.0\ \text{MPa}$) and $38.6$ times stiffer longitudinally ($92.69\ \text{GPa}$ vs $2.40\ \text{GPa}$).
- Control case: if only $0.5\ \text{vol\%}$ of carbon fibres ($V_f = 0.005 < V_{\min}$) were added, the fibre-fracture formula would give $0.005(3400) + 0.995(34.0) = 50.83\ \text{MPa}$, whereas the post-fracture matrix branch gives $0.995(65.0) = 64.68\ \text{MPa}$: the broken fibres would simply weaken the polycarbonate from $65.0$ to $64.68\ \text{MPa}$!
- SI dimensional check: $A_C$ is in $\text{m}^2$; $\sigma_C = F_C/A_C$ in $\text{N/m}^2 = \text{Pa}$; $\varepsilon = \sigma_C/E_{1C}$ in $\text{Pa/Pa}$ (dimensionless); $V_{\min}$ and $V_{\text{crit}}$ are ratios of MPa over MPa (dimensionless).
- Common mistake: substituting $V_f = 0.38$ only into $\sigma_m^*(1 - V_f)$ and reporting $40.3\ \text{MPa}$ as the composite strength without checking $V_f > V_{\min}$, or using $\sigma_m^*$ instead of $\sigma'_m$ in the pre-fracture term when $\sigma'_m$ is explicitly provided.

## Verification

- E1C (GPa) | (0.38*240e9 + 0.62*2.40e9)/1e9 | 92.69
- E2C (GPa) | 1/(0.38/240e9 + 0.62/2.40e9)/1e9 | 3.847
- F_f / F_m | (0.38*240e9)/(0.62*2.40e9) | 61.29
- F_f / F_C | (0.38*240e9)/(0.38*240e9 + 0.62*2.40e9) | 0.9839
- E_f / E_m | 240/2.40 | 100.0
- A_C (m^2) | 280e-6 | 2.80e-4
- sigma_C (MPa) | 52.0e3/280e-6/1e6 | 185.7
- strain eps | 52.0e3/280e-6/(0.38*240e9 + 0.62*2.40e9) | 2.004e-3
- sigma_f (MPa) | 240e9*52.0e3/280e-6/(0.38*240e9 + 0.62*2.40e9)/1e6 | 480.9
- sigma_m (MPa) | 2.40e9*52.0e3/280e-6/(0.38*240e9 + 0.62*2.40e9)/1e6 | 4.809
- fibre fracture strain | 3400/240000 | 1.417e-2
- sigma_1C (MPa) | 0.38*3400 + 0.62*34.0 | 1313
- sigma_C_res (MPa) | 65.0*(1 - 0.38) | 40.30
- V_min | (65.0 - 34.0)/(3400 + 65.0 - 34.0) | 9.035e-3
- V_crit | (65.0 - 34.0)/(3400 - 34.0) | 9.210e-3

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
