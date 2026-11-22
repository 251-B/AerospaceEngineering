---
materia: Aerospace Materials I
tema: "Unit 10: composite materials"
bank_id: P26
title: "Hybrid carbon-glass wing spar comparison"
category: mt3_problem
archetype: composite-hybrid-specific
level: trap
unit: 10
difficulty: 3
points: 5.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of Problems T10_CompositeMaterials.pdf (Problem 3) and Assessment Test III Model B (2020, Part II); not an official exercise. Verified with tools/materials_bank/verify_mt3.py"
tags:
  - problem-bank
  - midterm-3
  - unit-10
  - composite-materials
  - hybrid-composite
  - weight-fraction
  - specific-properties
---

# Bank P26 — Hybrid carbon-glass wing spar comparison

> [!info] Practice item, not an official exercise
> Written for the bank in the style of `Problems T10_CompositeMaterials.pdf` (Problem 3) and Assessment Test III Model B (2020, Part II). Method: Session 21, Slides 18, 43; Session 22, Slides 22, 26–27. Every result is recomputed by tools/materials_bank/verify_mt3.py.

## Statement

A wing spar laminate is initially formulated with $68.0\ \text{wt\%}$ continuous unidirectional high-modulus graphite (graphite-HM) fibres in an epoxy matrix. To assess a hybrid carbon-glass architecture, engineers consider replacing half ($50\ \%$) of the graphite fibre **volume** with continuous E-glass fibres while keeping the epoxy volume fraction unchanged. Constituent properties are listed below:

| Material | Density ($\text{g/cm}^3$) | Elastic modulus (GPa) | Tensile strength (MPa) |
| :--- | ---: | ---: | ---: |
| Epoxy resin ($m$) | 1.22 | 3.50 | 70.0 |
| Graphite-HM fibre ($\text{gr}$) | 1.86 | 390 | 2400 |
| E-glass fibre ($g$) | 2.58 | 72.5 | 3450 |

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| Initial graphite weight fraction | $w_{\text{gr},0}$ | $68.0\ \%$ | $0.680$ (dimensionless) |
| Initial epoxy weight fraction | $w_{m,0}$ | $32.0\ \%$ | $0.320$ (dimensionless) |
| Epoxy density, modulus, strength | $\rho_m$, $E_m$, $\sigma_m$ | $1.22\ \text{g/cm}^3$, $3.50\ \text{GPa}$, $70.0\ \text{MPa}$ | $1220\ \text{kg/m}^3$, $3.50\times10^{9}\ \text{Pa}$, $70.0\times10^{6}\ \text{Pa}$ |
| Graphite-HM density, modulus, strength | $\rho_{\text{gr}}$, $E_{\text{gr}}$, $\sigma_{\text{gr}}$ | $1.86\ \text{g/cm}^3$, $390\ \text{GPa}$, $2400\ \text{MPa}$ | $1860\ \text{kg/m}^3$, $390\times10^{9}\ \text{Pa}$, $2400\times10^{6}\ \text{Pa}$ |
| E-glass density, modulus, strength | $\rho_g$, $E_g$, $\sigma_g$ | $2.58\ \text{g/cm}^3$, $72.5\ \text{GPa}$, $3450\ \text{MPa}$ | $2580\ \text{kg/m}^3$, $72.5\times10^{9}\ \text{Pa}$, $3450\times10^{6}\ \text{Pa}$ |

#### Model

- Conversion from weight fractions to volume fractions (for $1\ \text{kg}$ of composite): $\mathcal{V}_i = w_i/\rho_i$, $V_i = \frac{w_i/\rho_i}{\sum_j (w_j/\rho_j)}$, and $\rho_c = \frac{1}{\sum_j (w_j/\rho_j)}$.
- General rule of mixtures: $\rho = \sum_i V_i\rho_i$, $E_{1C} = \sum_i V_i E_i$, and $\sigma_{1C} = \sum_i V_i\sigma_i$ with $\sum_i V_i = 1$ [Session 22, Slides 22, 26–27].
- Specific modulus $E/\rho$ and specific tensile strength $\sigma/\rho$ [Session 21, Slide 43].
- Hypotheses: zero porosity; perfect interfacial bonding; continuous aligned fibres along direction 1; tabulated matrix strength used in the rule of mixtures for longitudinal strength.

## (a) Convert the $68.0\ \text{wt\%}$ composition into volume fractions $V_{\text{gr},0}$ and $V_{m,0}$, and estimate the initial composite density $\rho_{c,0}$ and longitudinal modulus $E_{1C,0}$. [1.3 pts]

### Hint

Notice the composition is given by **mass** ($68.0\ \text{wt\%}$), not by volume: take a $1.000\ \text{kg}$ basis, compute the volume $w_i/\rho_i$ of graphite and epoxy, sum them to find the total volume and $\rho_{c,0}$, and then form $V_i$.

### Checkpoint

- $V_{\text{gr},0} = 0.5823$ ($58.23\ \text{vol\%}$), $V_{m,0} = 0.4177$ ($41.77\ \text{vol\%}$)
- $\rho_{c,0} = 1593\ \text{kg/m}^3$ ($1.593\ \text{g/cm}^3$), $E_{1C,0} = 228.5\ \text{GPa}$

### Solution

#### Volume of each constituent in $1.000\ \text{kg}$ of composite

In $1.000\ \text{kg}$ of initial composite, there are $m_{\text{gr}} = 0.680\ \text{kg}$ of graphite-HM and $m_m = 0.320\ \text{kg}$ of epoxy resin. Using $\rho_{\text{gr}} = 1860\ \text{kg/m}^3$ and $\rho_m = 1220\ \text{kg/m}^3$:

$$\mathcal{V}_{\text{gr}} = \frac{m_{\text{gr}}}{\rho_{\text{gr}}} = \frac{0.680\ \text{kg}}{1860\ \text{kg/m}^3} = 3.6559\times10^{-4}\ \text{m}^3$$

$$\mathcal{V}_m = \frac{m_m}{\rho_m} = \frac{0.320\ \text{kg}}{1220\ \text{kg/m}^3} = 2.6230\times10^{-4}\ \text{m}^3$$

#### Total volume, volume fractions, and initial density

Adding the two volumes gives the specific volume of the composite:

$$\mathcal{V}_{c,0} = 3.6559\times10^{-4}\ \text{m}^3 + 2.6230\times10^{-4}\ \text{m}^3 = 6.2789\times10^{-4}\ \text{m}^3$$

Dividing each constituent volume by $\mathcal{V}_{c,0}$ gives the volume fractions:

$$V_{\text{gr},0} = \frac{3.6559\times10^{-4}}{6.2789\times10^{-4}} = 0.5823 \quad (58.23\ \text{vol\%}) \qquad V_{m,0} = 1 - 0.5823 = 0.4177 \quad (41.77\ \text{vol\%})$$

And the initial composite density is total mass ($1.000\ \text{kg}$) over total volume:

$$\rho_{c,0} = \frac{1.000\ \text{kg}}{6.2789\times10^{-4}\ \text{m}^3} = 1592.6\ \text{kg/m}^3 \approx 1593\ \text{kg/m}^3 \quad (1.593\ \text{g/cm}^3)$$

#### Initial longitudinal modulus $E_{1C,0}$

Applying the isostrain rule of mixtures [Session 22, Slide 22]:

$$E_{1C,0} = V_{\text{gr},0} E_{\text{gr}} + V_{m,0} E_m = 0.58226\,(390\ \text{GPa}) + 0.41774\,(3.50\ \text{GPa}) = 227.08\ \text{GPa} + 1.46\ \text{GPa} = 228.5\ \text{GPa}$$

## (b) Replace $50\ \%$ of the graphite fibre volume with E-glass fibres. Compute the hybrid density $\rho_{\text{hyb}}$, longitudinal modulus $E_{\text{hyb}}$, tensile strength $\sigma_{\text{hyb}}$, specific modulus $E_{\text{hyb}}/\rho_{\text{hyb}}$, and specific strength $\sigma_{\text{hyb}}/\rho_{\text{hyb}}$. [1.7 pts]

### Hint

Split $V_{\text{gr},0}$ equally into $V_{\text{gr}} = V_g = V_{\text{gr},0}/2$ while keeping $V_{m,0}$ unchanged. Evaluate $\rho_{\text{hyb}}$, $E_{\text{hyb}}$, and $\sigma_{\text{hyb}}$ by summing over all three constituents, then divide by $\rho_{\text{hyb}}$ in $\text{kg/m}^3$.

### Checkpoint

- $V_{\text{gr}} = V_g = 0.2911$, $V_m = 0.4177$
- $\rho_{\text{hyb}} = 1802\ \text{kg/m}^3$ ($1.802\ \text{g/cm}^3$), $E_{\text{hyb}} = 136.1\ \text{GPa}$, $\sigma_{\text{hyb}} = 1732\ \text{MPa}$
- $E_{\text{hyb}}/\rho_{\text{hyb}} = 75.52\times10^{6}\ \text{m}^2/\text{s}^2$ ($75\,521\ \text{kN}\cdot\text{m/kg}$), $\sigma_{\text{hyb}}/\rho_{\text{hyb}} = 961.2\ \text{kN}\cdot\text{m/kg}$ ($0.9612\times10^{6}\ \text{m}^2/\text{s}^2$)

### Solution

#### Hybrid volume fractions

Half of the graphite fibre volume is replaced by E-glass, so:

$$V_{\text{gr}} = V_g = \frac{V_{\text{gr},0}}{2} = \frac{0.58226}{2} = 0.29113 \qquad V_m = 0.41774$$

Check: $0.29113 + 0.29113 + 0.41774 = 1.00000$.

#### Hybrid density, longitudinal modulus, and tensile strength

Using the three-constituent rule of mixtures [Session 22, Slides 22, 26–27]:

$$\rho_{\text{hyb}} = 0.29113\,(1860) + 0.29113\,(2580) + 0.41774\,(1220) = 541.5 + 751.1 + 509.6 = 1802.3\ \text{kg/m}^3 \approx 1802\ \text{kg/m}^3 \quad (1.802\ \text{g/cm}^3)$$

$$E_{\text{hyb}} = 0.29113\,(390) + 0.29113\,(72.5) + 0.41774\,(3.50) = 113.54 + 21.11 + 1.46 = 136.11\ \text{GPa} \approx 136.1\ \text{GPa}$$

$$\sigma_{\text{hyb}} = 0.29113\,(2400) + 0.29113\,(3450) + 0.41774\,(70.0) = 698.7 + 1004.4 + 29.24 = 1732.3\ \text{MPa} \approx 1732\ \text{MPa}$$

#### Specific modulus and specific tensile strength

Dividing the SI modulus and strength by $\rho_{\text{hyb}} = 1802.3\ \text{kg/m}^3$ [Session 21, Slide 43]:

$$\frac{E_{\text{hyb}}}{\rho_{\text{hyb}}} = \frac{136.11\times10^{9}\ \text{N/m}^2}{1802.3\ \text{kg/m}^3} = 75.52\times10^{6}\ \frac{\text{m}^2}{\text{s}^2} = 75\,521\ \text{kN}\cdot\text{m/kg}$$

$$\frac{\sigma_{\text{hyb}}}{\rho_{\text{hyb}}} = \frac{1732.3\times10^{6}\ \text{N/m}^2}{1802.3\ \text{kg/m}^3} = 961.2\times10^{3}\ \frac{\text{N}\cdot\text{m}}{\text{kg}} = 961.2\ \text{kN}\cdot\text{m/kg} = 0.9612\times10^{6}\ \text{m}^2/\text{s}^2$$

## (c) Calculate the minimum fibre volume fraction $V_{\text{gr},\min}$ of a two-constituent graphite-HM/epoxy composite needed to match the hybrid's longitudinal tensile strength. [1.0 pts]

### Hint

Set $\sigma_{1C}(V_{\text{gr}}) = V_{\text{gr}}\sigma_{\text{gr}} + (1 - V_{\text{gr}})\sigma_m = \sigma_{\text{hyb}}$ and isolate $V_{\text{gr}}$.

### Checkpoint

- $V_{\text{gr},\min} = 0.7135$ ($71.35\ \text{vol\%}$)

### Solution

#### Solving the strength rule of mixtures for $V_{\text{gr},\min}$

For a two-constituent graphite-HM/epoxy composite with fibre volume fraction $V_{\text{gr}}$ [Session 22, Slide 26]:

$$\sigma_{\text{gr}}\,V_{\text{gr}} + \sigma_m\,(1 - V_{\text{gr}}) = \sigma_{\text{hyb}}$$

Expanding $\sigma_m(1 - V_{\text{gr}})$ and grouping the $V_{\text{gr}}$ terms:

$$(\sigma_{\text{gr}} - \sigma_m)\,V_{\text{gr}} + \sigma_m = \sigma_{\text{hyb}}$$

Subtracting $\sigma_m$ from both sides and dividing by $(\sigma_{\text{gr}} - \sigma_m)$:

$$V_{\text{gr},\min} = \frac{\sigma_{\text{hyb}} - \sigma_m}{\sigma_{\text{gr}} - \sigma_m} = \frac{1732.3\ \text{MPa} - 70.0\ \text{MPa}}{2400\ \text{MPa} - 70.0\ \text{MPa}} = \frac{1662.3\ \text{MPa}}{2330\ \text{MPa}} = 0.7135 \quad (71.35\ \text{vol\%})$$

Notice that the baseline composite of part (a) ($V_{\text{gr},0} = 0.5823$) had $\sigma_{1C,0} = 0.5823(2400) + 0.4177(70) = 1427\ \text{MPa}$, which is weaker than the hybrid ($1732\ \text{MPa}$) because E-glass has higher tensile strength than graphite-HM ($3450 > 2400\ \text{MPa}$).

## (d) Repeat part (c) for a two-constituent E-glass/epoxy composite ($V_{g,\min}$) and comment on the feasibility and stiffness-strength trade-off. [1.0 pts]

### Hint

Solve $V_g\sigma_g + (1 - V_g)\sigma_m = \sigma_{\text{hyb}}$ for $V_{g,\min}$, and compare the modulus of that E-glass/epoxy composite against $E_{\text{hyb}}$ and $E_{1C,0}$.

### Checkpoint

- $V_{g,\min} = 0.4918$ ($49.18\ \text{vol\%}$), easily achievable in practice
- At $V_g = 0.4918$, $E_{1C} = 37.44\ \text{GPa}$ (only $27.5\ \%$ of $E_{\text{hyb}}$)

### Solution

#### Minimum volume fraction of E-glass fibres $V_{g,\min}$

Applying the same algebraic isolation with $\sigma_g = 3450\ \text{MPa}$ and $\sigma_m = 70.0\ \text{MPa}$:

$$V_{g,\min} = \frac{\sigma_{\text{hyb}} - \sigma_m}{\sigma_g - \sigma_m} = \frac{1732.3\ \text{MPa} - 70.0\ \text{MPa}}{3450\ \text{MPa} - 70.0\ \text{MPa}} = \frac{1662.3\ \text{MPa}}{3380\ \text{MPa}} = 0.4918 \quad (49.18\ \text{vol\%})$$

#### Feasibility and trade-off

While pure graphite-HM/epoxy needs $71.35\ \text{vol\%}$ fibres (near the packing limit of unidirectional laminates and well above the typical $50\text{–}60\ \text{vol\%}$ [Session 22, Slide 22]) to reach $1732\ \text{MPa}$, E-glass/epoxy needs only $49.18\ \text{vol\%}$. However, at $V_g = 0.4918$, E-glass/epoxy delivers a modulus of just $0.4918(72.5) + 0.5082(3.50) = 37.44\ \text{GPa}$ and a density of $0.4918(2580) + 0.5082(1220) = 1889\ \text{kg/m}^3$. The hybrid keeps the stiffness far higher ($136.1\ \text{GPa}$) than pure glass while raising strength $21.4\ \%$ above the initial graphite composite.

## Interpretation

- Unlike Kevlar-49 in P25 (which lowers density), replacing graphite-HM with E-glass **increases** density ($1593 \to 1802\ \text{kg/m}^3$) and cuts specific modulus nearly in half (from $228.5/1.593 = 143.5$ to $75.52\times10^{6}\ \text{m}^2/\text{s}^2$), while raising specific strength slightly from $1426.7/1.593 = 895.8$ to $961.2\ \text{kN}\cdot\text{m/kg}$. Engineers add E-glass to graphite mainly to lower cost and raise tensile strength/elongation, not to save weight.
- Control case: if the hybrid composition were $V_{\text{gr}} = 0.5823, V_g = 0$, then $\sigma = 1427\ \text{MPa}$ and $V_{\text{gr},\min} = 0.5823$; if all fibres were E-glass at $V_g = 0.5823$, $\sigma = 0.5823(3450) + 0.4177(70) = 2038\ \text{MPa} > 1732\ \text{MPa}$.
- SI dimensional check: $w_i/\rho_i$ in $\text{m}^3/\text{kg}$ makes $V_i$ dimensionless; $E/\rho$ and $\sigma/\rho$ are in $(\text{N/m}^2)/(\text{kg/m}^3) = \text{m}^2/\text{s}^2 = \text{N}\cdot\text{m/kg}$.
- Common mistake: treating the given $68.0\ \text{wt\%}$ as $V_f = 0.68$ directly (which would give $\rho_{c,0} = 1655\ \text{kg/m}^3$ and $E_{1C,0} = 266.3\ \text{GPa}$ instead of $1593\ \text{kg/m}^3$ and $228.5\ \text{GPa}$), or replacing $50\ \%$ by **weight** instead of $50\ \%$ by **volume** in part (b).

## Verification

- V_gr0 | (0.680/1860)/(0.680/1860 + 0.320/1220) | 0.5823
- V_m0 | (0.320/1220)/(0.680/1860 + 0.320/1220) | 0.4177
- rho_c0 (kg/m^3) | 1/(0.680/1860 + 0.320/1220) | 1593
- rho_c0 (g/cm^3) | 1/(0.680/1860 + 0.320/1220)/1000 | 1.593
- E1C_0 (GPa) | ((0.680/1860)*390 + (0.320/1220)*3.50)/(0.680/1860 + 0.320/1220) | 228.5
- sigma_1C0 (MPa) | ((0.680/1860)*2400 + (0.320/1220)*70.0)/(0.680/1860 + 0.320/1220) | 1427
- V_gr hybrid | 0.5*(0.680/1860)/(0.680/1860 + 0.320/1220) | 0.2911
- rho_hyb (kg/m^3) | (0.5*(0.680/1860)*1860 + 0.5*(0.680/1860)*2580 + (0.320/1220)*1220)/(0.680/1860 + 0.320/1220) | 1802
- rho_hyb (g/cm^3) | (0.5*(0.680/1860)*1860 + 0.5*(0.680/1860)*2580 + (0.320/1220)*1220)/(0.680/1860 + 0.320/1220)/1000 | 1.802
- E_hyb (GPa) | (0.5*(0.680/1860)*(390+72.5) + (0.320/1220)*3.50)/(0.680/1860 + 0.320/1220) | 136.1
- sigma_hyb (MPa) | (0.5*(0.680/1860)*(2400+3450) + (0.320/1220)*70.0)/(0.680/1860 + 0.320/1220) | 1732
- E_hyb/rho_hyb (1e6 m^2/s^2) | ((0.5*(0.680/1860)*(390e9+72.5e9) + (0.320/1220)*3.50e9)/(0.5*(0.680/1860)*(1860+2580) + (0.320/1220)*1220))/1e6 | 75.52
- E_hyb/rho_hyb (kN*m/kg) | ((0.5*(0.680/1860)*(390e9+72.5e9) + (0.320/1220)*3.50e9)/(0.5*(0.680/1860)*(1860+2580) + (0.320/1220)*1220))/1e3 | 75521
- sigma_hyb/rho_hyb (kN*m/kg) | ((0.5*(0.680/1860)*(2400e6+3450e6) + (0.320/1220)*70.0e6)/(0.5*(0.680/1860)*(1860+2580) + (0.320/1220)*1220))/1e3 | 961.2
- V_gr_min | ((0.5*(0.680/1860)*(2400+3450) + (0.320/1220)*70.0)/(0.680/1860 + 0.320/1220) - 70.0)/(2400 - 70.0) | 0.7135
- V_g_min | ((0.5*(0.680/1860)*(2400+3450) + (0.320/1220)*70.0)/(0.680/1860 + 0.320/1220) - 70.0)/(3450 - 70.0) | 0.4918
- E at V_g_min (GPa) | (((0.5*(0.680/1860)*(2400+3450) + (0.320/1220)*70.0)/(0.680/1860 + 0.320/1220) - 70.0)/(3450 - 70.0))*72.5 + (1 - ((0.5*(0.680/1860)*(2400+3450) + (0.320/1220)*70.0)/(0.680/1860 + 0.320/1220) - 70.0)/(3450 - 70.0))*3.50 | 37.44
- rho at V_g_min (kg/m^3) | (((0.5*(0.680/1860)*(2400+3450) + (0.320/1220)*70.0)/(0.680/1860 + 0.320/1220) - 70.0)/(3450 - 70.0))*2580 + (1 - ((0.5*(0.680/1860)*(2400+3450) + (0.320/1220)*70.0)/(0.680/1860 + 0.320/1220) - 70.0)/(3450 - 70.0))*1220 | 1889
- spec E0 (1e6 m^2/s^2) | ((0.680/1860)*390e9 + (0.320/1220)*3.50e9)/1e6 | 143.5
- spec S0 (kN*m/kg) | ((0.680/1860)*2400e6 + (0.320/1220)*70.0e6)/1e3 | 895.8
- wrong rho using Vf=0.68 (kg/m^3) | 0.68*1860 + 0.32*1220 | 1655
- wrong E1C using Vf=0.68 (GPa) | 0.68*390 + 0.32*3.50 | 266.3

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
