---
materia: Aerospace Materials I
tema: "Unit 10: composite materials"
bank_id: P27
title: "Spacecraft strut mass reduction and specific properties"
category: mt3_problem
archetype: composite-hybrid-specific
level: standard
unit: 10
difficulty: 2
points: 5.0
time_minutes: 25
official: false
origen: "Problem written for the bank in the style of Problems T10_CompositeMaterials.pdf (Problem 11); not an official exercise. Verified with tools/materials_bank/verify_mt3.py"
tags:
  - problem-bank
  - midterm-3
  - unit-10
  - composite-materials
  - specific-modulus
  - specific-strength
  - weight-saving
---

# Bank P27 — Spacecraft strut mass reduction and specific properties

> [!info] Practice item, not an official exercise
> Written for the bank in the style of `Problems T10_CompositeMaterials.pdf` (Problem 11). Method: Session 21, Slides 16 and 43; Session 22, Slides 22, 26–27. Every result is recomputed by tools/materials_bank/verify_mt3.py.

## Statement

A baseline structural strut on a spacecraft payload adapter is machined from titanium alloy Ti-6Al-4V and has a mass of $320\ \text{kg}$. To save launch mass while preserving the exact same part geometry (same volume) and the same longitudinal elastic modulus $E_{1C} = E_{\text{Ti}} = 114\ \text{GPa}$, two continuous unidirectional composite alternatives are proposed:

1. **B/Al MMC:** aluminium alloy matrix reinforced with continuous aligned boron fibres.
2. **HM-C/epoxy PMC:** epoxy matrix reinforced with continuous aligned high-modulus carbon fibres.

Constituent and baseline alloy properties are given in the table below:

| Material | Density ($\text{g/cm}^3$) | Elastic modulus (GPa) | Tensile strength (MPa) |
| :--- | ---: | ---: | ---: |
| Ti-6Al-4V ($\text{Ti}$) | 4.43 | 114 | 950 |
| Aluminium matrix ($\text{Al}$) | 2.70 | 70.0 | 280 |
| Boron fibre ($B$) | 2.36 | 385 | 3400 |
| Epoxy matrix ($\text{ep}$) | 1.24 | 3.50 | 70.0 |
| HM-carbon fibre ($C$) | 1.85 | 450 | 2500 |

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| Baseline Ti-6Al-4V strut mass | $m_{\text{Ti}}$ | $320\ \text{kg}$ | $320\ \text{kg}$ |
| Target longitudinal modulus | $E_{1C} = E_{\text{Ti}}$ | $114\ \text{GPa}$ | $114\times10^{9}\ \text{Pa}$ |
| Ti-6Al-4V density, strength | $\rho_{\text{Ti}}$, $\sigma_{\text{Ti}}$ | $4.43\ \text{g/cm}^3$, $950\ \text{MPa}$ | $4430\ \text{kg/m}^3$, $950\times10^{6}\ \text{Pa}$ |
| Aluminium density, modulus, strength | $\rho_{\text{Al}}$, $E_{\text{Al}}$, $\sigma_{\text{Al}}$ | $2.70\ \text{g/cm}^3$, $70.0\ \text{GPa}$, $280\ \text{MPa}$ | $2700\ \text{kg/m}^3$, $70.0\times10^{9}\ \text{Pa}$, $280\times10^{6}\ \text{Pa}$ |
| Boron fibre density, modulus, strength | $\rho_B$, $E_B$, $\sigma_B$ | $2.36\ \text{g/cm}^3$, $385\ \text{GPa}$, $3400\ \text{MPa}$ | $2360\ \text{kg/m}^3$, $385\times10^{9}\ \text{Pa}$, $3400\times10^{6}\ \text{Pa}$ |
| Epoxy density, modulus, strength | $\rho_{\text{ep}}$, $E_{\text{ep}}$, $\sigma_{\text{ep}}$ | $1.24\ \text{g/cm}^3$, $3.50\ \text{GPa}$, $70.0\ \text{MPa}$ | $1240\ \text{kg/m}^3$, $3.50\times10^{9}\ \text{Pa}$, $70.0\times10^{6}\ \text{Pa}$ |
| HM-carbon fibre density, modulus, strength | $\rho_C$, $E_C$, $\sigma_C$ | $1.85\ \text{g/cm}^3$, $450\ \text{GPa}$, $2500\ \text{MPa}$ | $1850\ \text{kg/m}^3$, $450\times10^{9}\ \text{Pa}$, $2500\times10^{6}\ \text{Pa}$ |

#### Model

- Constant-volume replacement: $\mathcal{V} = m_{\text{Ti}}/\rho_{\text{Ti}}$, and composite part mass $m_c = \rho_c\mathcal{V}$.
- Isostrain longitudinal modulus: $E_{1C} = V_f E_f + (1 - V_f)E_m \implies V_f = \frac{E_{1C} - E_m}{E_f - E_m}$ [Session 22, Slide 22].
- Composite density and tensile strength: $\rho_c = V_f\rho_f + (1 - V_f)\rho_m$ and $\sigma_{1C} = V_f\sigma_f + (1 - V_f)\sigma_m$ [Session 22, Slides 26–27].
- Specific modulus $E/\rho$ and specific strength $\sigma/\rho$ [Session 21, Slide 43].
- Hypotheses: zero porosity; perfect bonding; continuous aligned fibres along the strut axis; identical outer part volume $\mathcal{V}$ for all three materials.

## (a) Find the strut volume $\mathcal{V}$, the required boron volume fraction $V_{f,B}$ in the B/Al composite to match $E_{\text{Ti}}$, and the resulting B/Al strut mass $m_{B\text{-Al}}$. [1.3 pts]

### Hint

Compute $\mathcal{V} = m_{\text{Ti}}/\rho_{\text{Ti}}$ in $\text{m}^3$, isolate $V_{f,B}$ from $E_{1C} = E_{\text{Ti}}$, compute $\rho_{B\text{-Al}}$, and multiply by $\mathcal{V}$.

### Checkpoint

- $\mathcal{V} = 7.223\times10^{-2}\ \text{m}^3$, $V_{f,B} = 0.1397$ ($13.97\ \text{vol\%}$)
- $\rho_{B\text{-Al}} = 2653\ \text{kg/m}^3$, $m_{B\text{-Al}} = 191.6\ \text{kg}$ ($40.1\ \%$ mass saved)

### Solution

#### Volume of the titanium strut

With $m_{\text{Ti}} = 320\ \text{kg}$ and $\rho_{\text{Ti}} = 4430\ \text{kg/m}^3$:

$$\mathcal{V} = \frac{m_{\text{Ti}}}{\rho_{\text{Ti}}} = \frac{320\ \text{kg}}{4430\ \text{kg/m}^3} = 7.2235\times10^{-2}\ \text{m}^3$$

#### Required boron fibre volume fraction $V_{f,B}$

Setting $E_{1C} = V_{f,B} E_B + (1 - V_{f,B}) E_{\text{Al}} = E_{\text{Ti}}$ [Session 22, Slide 22], expanding $(1 - V_{f,B})E_{\text{Al}}$, and isolating $V_{f,B}$:

$$E_{\text{Al}} + V_{f,B}(E_B - E_{\text{Al}}) = E_{\text{Ti}} \implies V_{f,B} = \frac{E_{\text{Ti}} - E_{\text{Al}}}{E_B - E_{\text{Al}}}$$

Substituting $E_{\text{Ti}} = 114\ \text{GPa}$, $E_{\text{Al}} = 70.0\ \text{GPa}$, and $E_B = 385\ \text{GPa}$:

$$V_{f,B} = \frac{114 - 70.0}{385 - 70.0} = \frac{44.0\ \text{GPa}}{315\ \text{GPa}} = 0.1397 \quad (13.97\ \text{vol\%})$$

#### B/Al composite density and strut mass

With $V_{m,\text{Al}} = 1 - 0.13968 = 0.86032$:

$$\rho_{B\text{-Al}} = 0.13968\,(2360\ \text{kg/m}^3) + 0.86032\,(2700\ \text{kg/m}^3) = 329.7 + 2322.9 = 2652.5\ \text{kg/m}^3 \approx 2653\ \text{kg/m}^3$$

Multiplying by the strut volume $\mathcal{V} = 7.2235\times10^{-2}\ \text{m}^3$:

$$m_{B\text{-Al}} = \rho_{B\text{-Al}}\,\mathcal{V} = (2652.5\ \text{kg/m}^3)(7.2235\times10^{-2}\ \text{m}^3) = 191.6\ \text{kg}$$

This saves $320 - 191.6 = 128.4\ \text{kg}$ ($40.1\ \%$ of the titanium strut mass).

## (b) Find the required HM-carbon volume fraction $V_{f,C}$ in the HM-carbon/epoxy composite to match $E_{\text{Ti}}$, and the resulting strut mass $m_{C\text{-ep}}$. [1.3 pts]

### Hint

Apply the exact same stiffness-matching formula for $V_{f,C}$ with epoxy and HM-carbon properties, then find $\rho_{C\text{-ep}}$ and $m_{C\text{-ep}} = \rho_{C\text{-ep}}\mathcal{V}$.

### Checkpoint

- $V_{f,C} = 0.2475$ ($24.75\ \text{vol\%}$)
- $\rho_{C\text{-ep}} = 1391\ \text{kg/m}^3$, $m_{C\text{-ep}} = 100.5\ \text{kg}$ ($68.6\ \%$ mass saved)

### Solution

#### Required HM-carbon volume fraction $V_{f,C}$

Using $V_{f,C} = \frac{E_{\text{Ti}} - E_{\text{ep}}}{E_C - E_{\text{ep}}}$ with $E_{\text{Ti}} = 114\ \text{GPa}$, $E_{\text{ep}} = 3.50\ \text{GPa}$, and $E_C = 450\ \text{GPa}$:

$$V_{f,C} = \frac{114 - 3.50}{450 - 3.50} = \frac{110.5\ \text{GPa}}{446.5\ \text{GPa}} = 0.2475 \quad (24.75\ \text{vol\%})$$

#### HM-carbon/epoxy composite density and strut mass

With $V_{m,\text{ep}} = 1 - 0.24748 = 0.75252$:

$$\rho_{C\text{-ep}} = 0.24748\,(1850\ \text{kg/m}^3) + 0.75252\,(1240\ \text{kg/m}^3) = 457.8 + 933.1 = 1391.0\ \text{kg/m}^3 \approx 1391\ \text{kg/m}^3$$

Multiplying by $\mathcal{V} = 7.2235\times10^{-2}\ \text{m}^3$:

$$m_{C\text{-ep}} = \rho_{C\text{-ep}}\,\mathcal{V} = (1391.0\ \text{kg/m}^3)(7.2235\times10^{-2}\ \text{m}^3) = 100.5\ \text{kg}$$

This saves $320 - 100.5 = 219.5\ \text{kg}$ ($68.6\ \%$ of the original titanium mass).

## (c) Calculate and compare the longitudinal specific modulus $E/\rho$ of all three materials. [1.2 pts]

### Hint

All three materials share $E = 114\ \text{GPa} = 114\times10^{9}\ \text{N/m}^2$; divide by each material's density in $\text{kg/m}^3$.

### Checkpoint

- $(E/\rho)_{\text{Ti}} = 25\,734\ \text{kN}\cdot\text{m/kg}$ ($25.73\times10^{6}\ \text{m}^2/\text{s}^2$)
- $(E/\rho)_{B\text{-Al}} = 42\,978\ \text{kN}\cdot\text{m/kg}$ ($42.98\times10^{6}\ \text{m}^2/\text{s}^2$, $1.67\times$ Ti)
- $(E/\rho)_{C\text{-ep}} = 81\,958\ \text{kN}\cdot\text{m/kg}$ ($81.96\times10^{6}\ \text{m}^2/\text{s}^2$, $3.18\times$ Ti)

### Solution

#### Specific modulus values in exact SI units

Converting $E = 114\ \text{GPa} = 1.14\times10^{11}\ \text{N/m}^2$ and dividing by each density [Session 21, Slide 43]:

$$\left(\frac{E}{\rho}\right)_{\text{Ti}} = \frac{1.14\times10^{11}\ \text{N/m}^2}{4430\ \text{kg/m}^3} = 25.73\times10^{6}\ \frac{\text{m}^2}{\text{s}^2} = 25\,734\ \text{kN}\cdot\text{m/kg}$$

$$\left(\frac{E}{\rho}\right)_{B\text{-Al}} = \frac{1.14\times10^{11}\ \text{N/m}^2}{2652.5\ \text{kg/m}^3} = 42.98\times10^{6}\ \frac{\text{m}^2}{\text{s}^2} = 42\,978\ \text{kN}\cdot\text{m/kg}$$

$$\left(\frac{E}{\rho}\right)_{C\text{-ep}} = \frac{1.14\times10^{11}\ \text{N/m}^2}{1391.0\ \text{kg/m}^3} = 81.96\times10^{6}\ \frac{\text{m}^2}{\text{s}^2} = 81\,958\ \text{kN}\cdot\text{m/kg}$$

#### Comparison

At equal stiffness and volume, part mass scales inversely with specific modulus, $m / m_{\text{Ti}} = \rho / \rho_{\text{Ti}} = (E/\rho)_{\text{Ti}} / (E/\rho)$. Thus B/Al achieves $1.67$ times the specific stiffness of Ti-6Al-4V ($42\,978/25\,734 = 1.67$), and HM-C/epoxy achieves $3.18$ times the specific stiffness of Ti-6Al-4V ($81\,958/25\,734 = 3.18$).

## (d) Estimate the longitudinal tensile strength $\sigma_{1C}$ of each stiffness-matched composite and compare the specific tensile strength $\sigma/\rho$ across all three materials. [1.2 pts]

### Hint

Compute $\sigma_{1C} = V_f\sigma_f + (1 - V_f)\sigma_m$ for both composites at the volume fractions from parts (a) and (b), and divide by each material's density.

### Checkpoint

- $\sigma_{B\text{-Al}} = 715.8\ \text{MPa}$, $\sigma_{C\text{-ep}} = 671.4\ \text{MPa}$ (both lower in absolute strength than Ti at $950\ \text{MPa}$)
- Specific strengths: Ti $= 214.4\ \text{kN}\cdot\text{m/kg}$, B/Al $= 269.9\ \text{kN}\cdot\text{m/kg}$, HM-C/epoxy $= 482.7\ \text{kN}\cdot\text{m/kg}$

### Solution

#### Longitudinal tensile strengths of the stiffness-matched composites

Applying the strength rule of mixtures [Session 22, Slide 26]:

$$\sigma_{B\text{-Al}} = 0.13968\,(3400\ \text{MPa}) + 0.86032\,(280\ \text{MPa}) = 474.9 + 240.9 = 715.8\ \text{MPa}$$

$$\sigma_{C\text{-ep}} = 0.24748\,(2500\ \text{MPa}) + 0.75252\,(70.0\ \text{MPa}) = 618.7 + 52.7 = 671.4\ \text{MPa}$$

#### Specific tensile strengths in SI

Dividing by each density in $\text{kg/m}^3$ [Session 21, Slide 43]:

$$\left(\frac{\sigma}{\rho}\right)_{\text{Ti}} = \frac{950\times10^{6}\ \text{N/m}^2}{4430\ \text{kg/m}^3} = 214.4\times10^{3}\ \frac{\text{N}\cdot\text{m}}{\text{kg}} = 214.4\ \text{kN}\cdot\text{m/kg}$$

$$\left(\frac{\sigma}{\rho}\right)_{B\text{-Al}} = \frac{715.8\times10^{6}\ \text{N/m}^2}{2652.5\ \text{kg/m}^3} = 269.9\times10^{3}\ \frac{\text{N}\cdot\text{m}}{\text{kg}} = 269.9\ \text{kN}\cdot\text{m/kg}$$

$$\left(\frac{\sigma}{\rho}\right)_{C\text{-ep}} = \frac{671.4\times10^{6}\ \text{N/m}^2}{1391.0\ \text{kg/m}^3} = 482.7\times10^{3}\ \frac{\text{N}\cdot\text{m}}{\text{kg}} = 482.7\ \text{kN}\cdot\text{m/kg}$$

| Material | $\rho$ ($\text{kg/m}^3$) | Mass (kg) | $E/\rho$ ($\text{kN}\cdot\text{m/kg}$) | $\sigma$ (MPa) | $\sigma/\rho$ ($\text{kN}\cdot\text{m/kg}$) |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Ti-6Al-4V | 4430 | 320.0 | 25 734 | 950.0 | 214.4 |
| B/Al MMC ($13.97\ \%$ B) | 2653 | 191.6 | 42 978 | 715.8 | 269.9 |
| HM-C/epoxy ($24.75\ \%$ C) | 1391 | 100.5 | 81 958 | 671.4 | 482.7 |

Even though both stiffness-matched composites have lower absolute tensile strength than Ti-6Al-4V ($715.8$ and $671.4\ \text{MPa}$ vs $950\ \text{MPa}$), their specific strengths exceed titanium by $25.9\ \%$ (B/Al) and $125.1\ \%$ (HM-C/epoxy).

## Interpretation

- For a stiffness-limited spacecraft strut, replacing Ti-6Al-4V with HM-carbon/epoxy cuts structural mass by more than two-thirds ($219.5\ \text{kg}$ saved) using only $24.75\ \text{vol\%}$ fibre; if the design also carries high service temperatures (above $150\ ^\circ\text{C}$, where epoxy softens [Session 22, Slide 8]), B/Al MMC remains viable while still saving $40.1\ \%$ mass [Session 23, Slide 30]. Notice also that if the same part were sized for equal *load* rather than equal volume, HM-C/epoxy at $60\ \text{vol\%}$ fibre would achieve even higher mass savings.
- Control case: if the fibre modulus fell to $E_{\text{Ti}} = 114\ \text{GPa}$, then $V_f \to 1.00$ would be needed; if $V_f = 0$ in B/Al, $E_{1C} = 70.0\ \text{GPa} < 114\ \text{GPa}$ (impossible for unreinforced aluminium to match Ti stiffness).
- SI dimensional check: $\mathcal{V} = m/\rho$ is $\text{kg}/(\text{kg/m}^3) = \text{m}^3$; $m_c = \rho_c\mathcal{V}$ is in $\text{kg}$; $E/\rho$ and $\sigma/\rho$ are in $(\text{N/m}^2)/(\text{kg/m}^3) = \text{N}\cdot\text{m/kg} = \text{m}^2/\text{s}^2$.
- Common mistake: forgetting the matrix contribution $(1 - V_f)E_m$ when solving for $V_f$ (which gives $V_{f,B} = 114/385 = 0.296$ instead of $0.1397$, a huge error because $E_{\text{Al}} = 70\ \text{GPa}$ is large!), or comparing absolute tensile strengths without dividing by density.

## Verification

- V_part (m^3) | 320.0/4430 | 7.223e-2
- Vf_BAl | (114 - 70.0)/(385 - 70.0) | 0.1397
- rho_BAl (kg/m^3) | ((114 - 70.0)/(385 - 70.0))*2360 + (1 - (114 - 70.0)/(385 - 70.0))*2700 | 2653
- m_BAl (kg) | (((114 - 70.0)/(385 - 70.0))*2360 + (1 - (114 - 70.0)/(385 - 70.0))*2700)*(320.0/4430) | 191.6
- mass saved BAl (kg) | 320.0 - (((114 - 70.0)/(385 - 70.0))*2360 + (1 - (114 - 70.0)/(385 - 70.0))*2700)*(320.0/4430) | 128.4
- mass saved BAl (%) | (1 - (((114 - 70.0)/(385 - 70.0))*2360 + (1 - (114 - 70.0)/(385 - 70.0))*2700)/4430)*100 | 40.1
- Vf_Cep | (114 - 3.50)/(450 - 3.50) | 0.2475
- rho_Cep (kg/m^3) | ((114 - 3.50)/(450 - 3.50))*1850 + (1 - (114 - 3.50)/(450 - 3.50))*1240 | 1391
- m_Cep (kg) | (((114 - 3.50)/(450 - 3.50))*1850 + (1 - (114 - 3.50)/(450 - 3.50))*1240)*(320.0/4430) | 100.5
- mass saved Cep (kg) | 320.0 - (((114 - 3.50)/(450 - 3.50))*1850 + (1 - (114 - 3.50)/(450 - 3.50))*1240)*(320.0/4430) | 219.5
- mass saved Cep (%) | (1 - (((114 - 3.50)/(450 - 3.50))*1850 + (1 - (114 - 3.50)/(450 - 3.50))*1240)/4430)*100 | 68.6
- spec E Ti (kN*m/kg) | 114e9/4430/1e3 | 25734
- spec E BAl (kN*m/kg) | 114e9/(((114 - 70.0)/(385 - 70.0))*2360 + (1 - (114 - 70.0)/(385 - 70.0))*2700)/1e3 | 42978
- spec E Cep (kN*m/kg) | 114e9/(((114 - 3.50)/(450 - 3.50))*1850 + (1 - (114 - 3.50)/(450 - 3.50))*1240)/1e3 | 81958
- spec E ratio BAl/Ti | 4430/(((114 - 70.0)/(385 - 70.0))*2360 + (1 - (114 - 70.0)/(385 - 70.0))*2700) | 1.67
- spec E ratio Cep/Ti | 4430/(((114 - 3.50)/(450 - 3.50))*1850 + (1 - (114 - 3.50)/(450 - 3.50))*1240) | 3.18
- sigma BAl (MPa) | ((114 - 70.0)/(385 - 70.0))*3400 + (1 - (114 - 70.0)/(385 - 70.0))*280 | 715.8
- sigma Cep (MPa) | ((114 - 3.50)/(450 - 3.50))*2500 + (1 - (114 - 3.50)/(450 - 3.50))*70.0 | 671.4
- spec S Ti (kN*m/kg) | 950e6/4430/1e3 | 214.4
- spec S BAl (kN*m/kg) | (((114 - 70.0)/(385 - 70.0))*3400e6 + (1 - (114 - 70.0)/(385 - 70.0))*280e6)/(((114 - 70.0)/(385 - 70.0))*2360 + (1 - (114 - 70.0)/(385 - 70.0))*2700)/1e3 | 269.9
- spec S Cep (kN*m/kg) | (((114 - 3.50)/(450 - 3.50))*2500e6 + (1 - (114 - 3.50)/(450 - 3.50))*70.0e6)/(((114 - 3.50)/(450 - 3.50))*1850 + (1 - (114 - 3.50)/(450 - 3.50))*1240)/1e3 | 482.7
- spec S gain BAl (%) | (((((114 - 70.0)/(385 - 70.0))*3400 + (1 - (114 - 70.0)/(385 - 70.0))*280)/(((114 - 70.0)/(385 - 70.0))*2360 + (1 - (114 - 70.0)/(385 - 70.0))*2700))/(950/4430) - 1)*100 | 25.9
- spec S gain Cep (%) | (((((114 - 3.50)/(450 - 3.50))*2500 + (1 - (114 - 3.50)/(450 - 3.50))*70.0)/(((114 - 3.50)/(450 - 3.50))*1850 + (1 - (114 - 3.50)/(450 - 3.50))*1240))/(950/4430) - 1)*100 | 125.1

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
