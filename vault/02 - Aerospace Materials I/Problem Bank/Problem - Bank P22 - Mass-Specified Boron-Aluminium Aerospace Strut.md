---
materia: Aerospace Materials I
tema: "Unit 10: composite materials"
bank_id: P22
title: "Mass-specified boron-aluminium aerospace strut"
category: mt3_problem
archetype: composite-unidirectional
level: standard
unit: 10
difficulty: 2
points: 5.0
time_minutes: 25
official: false
origen: "Problem written for the bank in the style of Problems T10_CompositeMaterials.pdf (Problem 8) and Session 22 micromechanics; not an official exercise. Verified with tools/materials_bank/verify_mt3.py"
tags:
  - problem-bank
  - midterm-3
  - unit-10
  - composite-materials
  - metal-matrix-composite
  - isostrain
  - isostress
---

# Bank P22 — Mass-specified boron-aluminium aerospace strut

> [!info] Practice item, not an official exercise
> Written for the bank in the style of `Problems T10_CompositeMaterials.pdf` (Problem 8). Method: Session 22, Slides 20–27. Every result is recomputed by tools/materials_bank/verify_mt3.py.

## Statement

A metal-matrix composite (MMC) for an aerospace pylon strut is manufactured by introducing $4.20\ \text{kg}$ of continuous, unidirectionally aligned boron fibres into $7.80\ \text{kg}$ of an aluminium alloy matrix. The properties of the two constituents are:

- Boron fibres ($f$): $\rho_f = 2.35\ \text{g/cm}^3$, $E_f = 390\ \text{GPa}$.
- Aluminium alloy matrix ($m$): $\rho_m = 2.70\ \text{g/cm}^3$, $E_m = 70.0\ \text{GPa}$.

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| Mass of boron fibres | $m_f$ | $4.20\ \text{kg}$ | $4.20\ \text{kg}$ |
| Mass of aluminium matrix | $m_m$ | $7.80\ \text{kg}$ | $7.80\ \text{kg}$ |
| Boron fibre density | $\rho_f$ | $2.35\ \text{g/cm}^3$ | $2350\ \text{kg/m}^3$ |
| Aluminium matrix density | $\rho_m$ | $2.70\ \text{g/cm}^3$ | $2700\ \text{kg/m}^3$ |
| Boron elastic modulus | $E_f$ | $390\ \text{GPa}$ | $390\times10^{9}\ \text{Pa}$ |
| Aluminium elastic modulus | $E_m$ | $70.0\ \text{GPa}$ | $70.0\times10^{9}\ \text{Pa}$ |
| Strut diameter (part d) | $d$ | $24.0\ \text{mm}$ | $2.40\times10^{-2}\ \text{m}$ |
| Strut length (part d) | $L_0$ | $1.80\ \text{m}$ | $1.80\ \text{m}$ |
| Applied axial force (part d) | $F_C$ | $95.0\ \text{kN}$ | $95.0\times10^{3}\ \text{N}$ |

#### Model

- Constituent volumes from mass and density: $\mathcal{V}_i = m_i / \rho_i$, with total volume $\mathcal{V}_c = \mathcal{V}_f + \mathcal{V}_m$ and volume fractions $V_i = \mathcal{V}_i / \mathcal{V}_c$.
- Composite density: $\rho_c = (m_f + m_m)/\mathcal{V}_c = V_f\rho_f + V_m\rho_m$ [Session 22, Slide 27].
- Longitudinal isostrain modulus: $E_{1C} = V_f E_f + V_m E_m$ [Session 22, Slide 22].
- Transverse isostress modulus: $\frac{1}{E_{2C}} = \frac{V_f}{E'_f} + \frac{V_m}{E_m}$ [Session 22, Slide 24].
- Axial load fraction and elongation: $\frac{F_f}{F_C} = \frac{V_f E_f}{E_{1C}}$ and $\Delta L = \varepsilon L_0 = \frac{F_C L_0}{A_C E_{1C}}$ [Session 22, Slides 21–22].
- Hypotheses: zero void porosity; isotropic fibres ($E'_f = E_f$); perfect fibre-matrix bonding; linearly elastic deformation in both phases [Session 22, Slide 20].

## (a) Convert the given constituent masses into volume fractions $V_f$ (boron) and $V_m$ (aluminium). [1.2 pts]

### Hint

Volume fractions cannot be replaced by mass fractions ($4.2/12.0$): first find the volume $\mathcal{V}_i = m_i / \rho_i$ of each constituent using consistent SI units ($\text{kg}$ and $\text{kg/m}^3$), then divide by the total volume $\mathcal{V}_c$.

### Checkpoint

- $\mathcal{V}_f = 1.787\times10^{-3}\ \text{m}^3$, $\mathcal{V}_m = 2.889\times10^{-3}\ \text{m}^3$, $\mathcal{V}_c = 4.676\times10^{-3}\ \text{m}^3$
- $V_f = 0.3822$ ($38.22\ \text{vol\%}$), $V_m = 0.6178$ ($61.78\ \text{vol\%}$)

### Solution

#### Volume of each constituent in SI

Convert the densities to $\text{kg/m}^3$: $\rho_f = 2.35\times10^{3} = 2350\ \text{kg/m}^3$ and $\rho_m = 2.70\times10^{3} = 2700\ \text{kg/m}^3$. Using $\mathcal{V}_i = m_i / \rho_i$:

$$\mathcal{V}_f = \frac{m_f}{\rho_f} = \frac{4.20\ \text{kg}}{2350\ \text{kg/m}^3} = 1.7872\times10^{-3}\ \text{m}^3$$

$$\mathcal{V}_m = \frac{m_m}{\rho_m} = \frac{7.80\ \text{kg}}{2700\ \text{kg/m}^3} = 2.8889\times10^{-3}\ \text{m}^3$$

#### Total volume and volume fractions

Assuming no porosity, the total composite volume is the sum of the constituent volumes:

$$\mathcal{V}_c = \mathcal{V}_f + \mathcal{V}_m = 1.7872\times10^{-3}\ \text{m}^3 + 2.8889\times10^{-3}\ \text{m}^3 = 4.6761\times10^{-3}\ \text{m}^3$$

Dividing each constituent volume by $\mathcal{V}_c$ gives the volume fractions:

$$V_f = \frac{\mathcal{V}_f}{\mathcal{V}_c} = \frac{1.7872\times10^{-3}\ \text{m}^3}{4.6761\times10^{-3}\ \text{m}^3} = 0.3822 \quad (38.22\ \text{vol\%})$$

$$V_m = \frac{\mathcal{V}_m}{\mathcal{V}_c} = \frac{2.8889\times10^{-3}\ \text{m}^3}{4.6761\times10^{-3}\ \text{m}^3} = 0.6178 \quad (61.78\ \text{vol\%})$$

Check: $V_f + V_m = 0.3822 + 0.6178 = 1.0000$. Because boron is less dense than aluminium ($2350 < 2700\ \text{kg/m}^3$), its volume fraction ($38.22\ \%$) is larger than its mass fraction ($w_f = 4.20/12.0 = 35.0\ \%$).

## (b) Compute the density $\rho_c$ of the boron-aluminium composite. [0.8 pts]

### Hint

Divide the total mass $m_f + m_m$ by the total volume $\mathcal{V}_c$ found in part (a), and verify with the rule of mixtures $\rho_c = V_f\rho_f + V_m\rho_m$.

### Checkpoint

- $\rho_c = 2566\ \text{kg/m}^3 = 2.566\ \text{g/cm}^3$

### Solution

#### Total mass over total volume

The total mass of the composite is $m_c = m_f + m_m = 4.20\ \text{kg} + 7.80\ \text{kg} = 12.00\ \text{kg}$. Dividing by the total volume $\mathcal{V}_c = 4.6761\times10^{-3}\ \text{m}^3$:

$$\rho_c = \frac{m_c}{\mathcal{V}_c} = \frac{12.00\ \text{kg}}{4.6761\times10^{-3}\ \text{m}^3} = 2566\ \text{kg/m}^3 = 2.566\ \text{g/cm}^3$$

#### Cross-check by the rule of mixtures

Using the volume fractions from part (a) in $\rho_c = V_f\rho_f + V_m\rho_m$ [Session 22, Slide 27]:

$$\rho_c = 0.3822\,(2350\ \text{kg/m}^3) + 0.6178\,(2700\ \text{kg/m}^3) = 898.2\ \text{kg/m}^3 + 1668.1\ \text{kg/m}^3 = 2566\ \text{kg/m}^3$$

Both calculations agree and lie strictly between the constituent densities ($2350 < 2566 < 2700\ \text{kg/m}^3$).

## (c) Calculate the longitudinal modulus $E_{1C}$ and the transverse modulus $E_{2C}$ of the composite. [1.5 pts]

### Hint

Apply the isostrain rule along the boron fibres and the isostress rule across them, using the exact volume fractions from part (a).

### Checkpoint

- $E_{1C} = 192.3\ \text{GPa} = 1.923\times10^{11}\ \text{Pa}$
- $E_{2C} = 102.0\ \text{GPa} = 1.020\times10^{11}\ \text{Pa}$

### Solution

#### Longitudinal elastic modulus $E_{1C}$

Under isostrain loading parallel to the boron fibres [Session 22, Slide 22]:

$$E_{1C} = V_f E_f + V_m E_m = 0.38220\,(390\times10^{9}\ \text{Pa}) + 0.61780\,(70.0\times10^{9}\ \text{Pa})$$

Evaluating each term explicitly:

$$E_{1C} = 1.4906\times10^{11}\ \text{Pa} + 4.3246\times10^{10}\ \text{Pa} = 1.923\times10^{11}\ \text{Pa} = 192.3\ \text{GPa}$$

#### Transverse elastic modulus $E_{2C}$

Under isostress loading perpendicular to the fibres [Session 22, Slide 24], taking $E'_f = E_f = 390\times10^{9}\ \text{Pa}$:

$$\frac{1}{E_{2C}} = \frac{V_f}{E_f} + \frac{V_m}{E_m} = \frac{0.38220}{390\times10^{9}\ \text{Pa}} + \frac{0.61780}{70.0\times10^{9}\ \text{Pa}}$$

Computing the two compliance terms:

$$\frac{1}{E_{2C}} = 9.800\times10^{-13}\ \text{Pa}^{-1} + 8.826\times10^{-12}\ \text{Pa}^{-1} = 9.806\times10^{-12}\ \text{Pa}^{-1}$$

Inverting to obtain the transverse modulus:

$$E_{2C} = \frac{1}{9.8057\times10^{-12}\ \text{Pa}^{-1}} = 1.020\times10^{11}\ \text{Pa} = 102.0\ \text{GPa}$$

## (d) A cylindrical strut of this composite, $24.0\ \text{mm}$ in diameter and $1.80\ \text{m}$ long, carries an axial tensile load of $95.0\ \text{kN}$ parallel to the fibres. Determine the elongation $\Delta L$ and the load fraction $F_f/F_C$ (and force $F_f$) carried by the boron fibres. [1.5 pts]

### Hint

Compute the composite cross-sectional area $A_C$, the applied stress $\sigma_C = F_C/A_C$, and the common axial strain $\varepsilon = \sigma_C/E_{1C}$. Then evaluate $\Delta L = \varepsilon L_0$ and $F_f/F_C = V_f E_f / E_{1C}$.

### Checkpoint

- $A_C = 4.524\times10^{-4}\ \text{m}^2$, $\sigma_C = 210.0\ \text{MPa}$, $\varepsilon = 1.092\times10^{-3}$
- $\Delta L = 1.966\times10^{-3}\ \text{m} = 1.966\ \text{mm}$
- $F_f/F_C = 0.7751$ ($77.51\ \%$), $F_f = 73.64\ \text{kN}$ ($73\,635\ \text{N}$)

### Solution

#### Area, composite stress and axial strain

With $d = 24.0\ \text{mm} = 2.40\times10^{-2}\ \text{m}$ and $F_C = 95.0\ \text{kN} = 9.50\times10^{4}\ \text{N}$:

$$A_C = \frac{\pi d^2}{4} = \frac{\pi\,(2.40\times10^{-2}\ \text{m})^2}{4} = 4.524\times10^{-4}\ \text{m}^2$$

$$\sigma_C = \frac{F_C}{A_C} = \frac{9.50\times10^{4}\ \text{N}}{4.5239\times10^{-4}\ \text{m}^2} = 2.100\times10^{8}\ \text{Pa} = 210.0\ \text{MPa}$$

From Hooke's law for the composite along direction 1, $\sigma_C = E_{1C}\varepsilon$, dividing by $E_{1C} = 1.9231\times10^{11}\ \text{Pa}$:

$$\varepsilon = \frac{\sigma_C}{E_{1C}} = \frac{2.100\times10^{8}\ \text{Pa}}{1.9231\times10^{11}\ \text{Pa}} = 1.092\times10^{-3}$$

#### Axial elongation $\Delta L$

Multiplying the strain by the initial strut length $L_0 = 1.80\ \text{m}$:

$$\Delta L = \varepsilon\,L_0 = (1.0920\times10^{-3})(1.80\ \text{m}) = 1.966\times10^{-3}\ \text{m} = 1.966\ \text{mm}$$

#### Load fraction and force carried by the boron fibres

Because fibres and matrix undergo the same axial strain $\varepsilon$, the force carried by the fibres is $F_f = \sigma_f A_f = (E_f\varepsilon)(V_f A_C)$ while the total force is $F_C = \sigma_C A_C = (E_{1C}\varepsilon) A_C$ [Session 22, Slides 21–22]. Taking their ratio eliminates $\varepsilon$ and $A_C$:

$$\frac{F_f}{F_C} = \frac{V_f E_f}{E_{1C}} = \frac{0.38220\,(390\times10^{9}\ \text{Pa})}{1.9231\times10^{11}\ \text{Pa}} = \frac{1.4906\times10^{11}}{1.9231\times10^{11}} = 0.7751 \quad (77.51\ \%)$$

Multiplying by the applied load $F_C = 95.0\ \text{kN}$ yields the force in the boron fibres:

$$F_f = 0.7751\,(95.0\ \text{kN}) = 73.64\ \text{kN} \quad (73\,635\ \text{N})$$

The aluminium matrix carries the remaining $F_m = 95.0 - 73.64 = 21.36\ \text{kN}$ ($22.49\ \%$ of the load).

## Interpretation

- Unlike polymer-matrix composites, where the matrix carries under $2\ \%$ of the longitudinal load, here the aluminium matrix ($E_m = 70\ \text{GPa}$) is already stiff, so it carries $22.5\ \%$ of the axial load and keeps the transverse modulus high ($E_{2C} = 102.0\ \text{GPa}$, over half of $E_{1C}$). Even so, adding $38.2\ \text{vol\%}$ boron lowers the density below pure aluminium ($2566 < 2700\ \text{kg/m}^3$) while nearly tripling longitudinal stiffness ($192.3$ vs $70.0\ \text{GPa}$).
- Control case: if the boron mass were added with the same density as aluminium ($\rho_f = \rho_m$), the volume fraction would equal the mass fraction $w_f = 0.350$. With $V_f = 0$, $E_{1C} = E_{2C} = 70.0\ \text{GPa}$ and $F_f/F_C = 0$.
- SI dimensional check: $\mathcal{V}_i = m_i/\rho_i$ has units $\text{kg}/(\text{kg/m}^3) = \text{m}^3$; $1/E_{2C}$ has units $\text{Pa}^{-1}$; $\varepsilon = F_C/(A_C E_{1C})$ has units $\text{N}/(\text{m}^2\cdot\text{N/m}^2) = 1$; $\Delta L = \varepsilon L_0$ has units $\text{m}$.
- Common mistake: substituting mass fractions ($w_f = 4.20/12.0 = 0.350$, $w_m = 0.650$) directly into the rule of mixtures for $E_{1C}$ and $\rho_c$ instead of converting masses to volumes first (which would give $E_{1C} = 182.0\ \text{GPa}$ instead of $192.3\ \text{GPa}$).

## Verification

- V_f volume (m^3) | 4.20/2350 | 1.787e-3
- V_m volume (m^3) | 7.80/2700 | 2.889e-3
- V_c volume (m^3) | 4.20/2350 + 7.80/2700 | 4.676e-3
- Vf fraction | (4.20/2350)/(4.20/2350 + 7.80/2700) | 0.3822
- Vm fraction | (7.80/2700)/(4.20/2350 + 7.80/2700) | 0.6178
- w_f mass fraction | 4.20/(4.20 + 7.80) | 0.350
- rho_c (kg/m^3) | (4.20 + 7.80)/(4.20/2350 + 7.80/2700) | 2566
- rho_c (g/cm^3) | (4.20 + 7.80)/(4.20/2350 + 7.80/2700)/1000 | 2.566
- E1C (GPa) | ((4.20/2350)*390 + (7.80/2700)*70.0)/(4.20/2350 + 7.80/2700) | 192.3
- E2C (GPa) | (4.20/2350 + 7.80/2700)/((4.20/2350)/390 + (7.80/2700)/70.0) | 102.0
- A_C (m^2) | pi*(24.0e-3)**2/4 | 4.524e-4
- sigma_C (MPa) | 95.0e3/(pi*(24.0e-3)**2/4)/1e6 | 210.0
- strain eps | 95.0e3/(pi*(24.0e-3)**2/4)/(((4.20/2350)*390e9 + (7.80/2700)*70.0e9)/(4.20/2350 + 7.80/2700)) | 1.092e-3
- Delta L (mm) | 95.0e3/(pi*(24.0e-3)**2/4)/(((4.20/2350)*390e9 + (7.80/2700)*70.0e9)/(4.20/2350 + 7.80/2700))*1.80*1e3 | 1.966
- F_f / F_C | ((4.20/2350)*390)/((4.20/2350)*390 + (7.80/2700)*70.0) | 0.7751
- F_f (kN) | 95.0*((4.20/2350)*390)/((4.20/2350)*390 + (7.80/2700)*70.0) | 73.64
- F_m (kN) | 95.0*((7.80/2700)*70.0)/((4.20/2350)*390 + (7.80/2700)*70.0) | 21.36
- wrong E1C using wf (GPa) | 0.350*390 + 0.650*70.0 | 182.0

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
