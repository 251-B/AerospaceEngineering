---
materia: Aerospace Materials I
tema: "Unit 9: polymer molecular weight and crystallinity"
bank_id: P36
title: "Polymer crystallinity from two density measurements"
category: mt3_problem
archetype: polymer-mw-crystallinity
level: standard
unit: 9
difficulty: 2
points: 5.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of Problems T9 (problems 6 and 9); not an official exercise. Verified with tools/materials_bank/verify_mt3.py"
tags:
  - problem-bank
  - midterm-3
  - polymer-mw-crystallinity
  - crystallinity
  - density
  - modulus-temperature
---

# Bank P36 — Polymer crystallinity from two density measurements

> [!info] Practice item, not an official exercise
> Written for the bank in the style of Problems T9 (problems 6 and 9). Method: Session 19, Slides 24–25, 27, 29, and 45; Session 20, Slide 8 (linearization in specific volumes marked as extension). Every result is recomputed by tools/materials_bank/verify_mt3.py.

## Statement

Two linear polyethylene (PE) specimens prepared with different cooling rates have the following measured bulk densities and mass degrees of crystallinity:

| Specimen | Measured density, $\rho_s$ ($\text{g/cm}^3$) | Degree of crystallinity ($\%$) |
| :--- | ---: | ---: |
| Sample 1 (quenched) | 0.9233 | 45.0 |
| Sample 2 (slowly cooled) | 0.9695 | 80.0 |

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| Sample 1 density | $\rho_1$ | 0.9233 g/cm³ | 923.3 kg/m³ |
| Sample 1 crystallinity fraction | $f_{c,1}$ | 0.450 (45.0%) | dimensionless |
| Sample 2 density | $\rho_2$ | 0.9695 g/cm³ | 969.5 kg/m³ |
| Sample 2 crystallinity fraction | $f_{c,2}$ | 0.800 (80.0%) | dimensionless |
| Target crystallinity (part b) | $f_{c,3}$ | 0.750 (75.0%) | dimensionless |
| Sample 4 density (part c) | $\rho_4$ | 0.9450 g/cm³ | 945.0 kg/m³ |

#### Model

- **Semicrystalline density–crystallinity relation:** crystalline lamellae are denser than amorphous regions ($\rho_c > \rho_a$), and the mass percentage of crystallinity is [Session 19, Slides 24–25]:

$$\%\ \text{crystallinity} = \frac{\rho_c(\rho_s - \rho_a)}{\rho_s(\rho_c - \rho_a)}\times 100 \qquad \text{or} \qquad f_c = \frac{\%\ \text{cryst}}{100} = \frac{\rho_c(\rho_s - \rho_a)}{\rho_s(\rho_c - \rho_a)}$$

- **Specific-volume linearization (extension):** because specific volumes of the crystalline and amorphous fractions add on a mass basis, the relation is linear in $u = 1/\rho_s$, $u_c = 1/\rho_c$, and $u_a = 1/\rho_a$.
- **Thermal transitions of polyethylene:** $T_g \approx -110^\circ\text{C}$ [Session 19, Slide 29] and $T_m \approx 110\text{–}137^\circ\text{C}$ [Session 20, Slide 8]; higher crystallinity raises $T_m$ [Session 19, Slide 27] and keeps a higher rubbery/semicrystalline plateau on the $\log E$ versus $T$ plot [Session 19, Slide 45].

## (a) Rewrite the crystallinity formula as a linear equation in specific volumes $1/\rho_s$, $1/\rho_a$, and $1/\rho_c$, and solve for $\rho_a$ and $\rho_c$. [1.8 pts]

### Hint

Divide the numerator and denominator of the right-hand side by $\rho_s \rho_c \rho_a$ (or expand $f_c \rho_s(\rho_c - \rho_a) = \rho_c(\rho_s - \rho_a)$ and divide by $\rho_s \rho_c \rho_a$) to obtain $1/\rho_s = (1 - f_c)/\rho_a + f_c/\rho_c$.

### Checkpoint

- Linear form: $\frac{1}{\rho_s} = \frac{1 - f_c}{\rho_a} + \frac{f_c}{\rho_c}$
- $u_a = 1.1494\ \text{cm}^3/\text{g}$, $u_c = 1.0020\ \text{cm}^3/\text{g}$
- $\rho_a = 0.8700\ \text{g/cm}^3 = 870.0\ \text{kg/m}^3$, $\rho_c = 0.9980\ \text{g/cm}^3 = 998.0\ \text{kg/m}^3$

### Solution

#### Linearize the crystallinity equation in $1/\rho_s$ (**extension**)

Starting from the formula of Session 19, Slide 25 with $f_c = \%\ \text{crystallinity}/100$:

$$f_c = \frac{\rho_c(\rho_s - \rho_a)}{\rho_s(\rho_c - \rho_a)}$$

Divide both numerator and denominator of the right-hand side by $\rho_s \rho_c \rho_a$ (or equivalently cross-multiply by $\rho_s(\rho_c - \rho_a)$ and divide by $\rho_s \rho_c \rho_a$):

$$f_c\left(\frac{1}{\rho_a} - \frac{1}{\rho_c}\right) = \frac{1}{\rho_a} - \frac{1}{\rho_s}$$

Isolating $1/\rho_s$ on the left (add $1/\rho_s$ to both sides and subtract $f_c(1/\rho_a - 1/\rho_c)$):

$$\frac{1}{\rho_s} = \frac{1}{\rho_a} - f_c\left(\frac{1}{\rho_a} - \frac{1}{\rho_c}\right) = \frac{1 - f_c}{\rho_a} + \frac{f_c}{\rho_c}$$

Setting $u_a = 1/\rho_a$ and $u_c = 1/\rho_c$ gives the linear system $u_s = (1 - f_c)\,u_a + f_c\,u_c$.

#### Set up and solve the linear system

Evaluating the specific volumes $1/\rho_1$ and $1/\rho_2$ of the two samples:

$$\frac{1}{\rho_1} = \frac{1}{0.9233\ \text{g/cm}^3} = 1.083072\ \text{cm}^3/\text{g} \qquad \frac{1}{\rho_2} = \frac{1}{0.9695\ \text{g/cm}^3} = 1.031460\ \text{cm}^3/\text{g}$$

Substituting the two pairs $(f_{c,1}, 1/\rho_1) = (0.450, 1.083072)$ and $(f_{c,2}, 1/\rho_2) = (0.800, 1.031460)$:

$$0.550\,u_a + 0.450\,u_c = 1.083072\ \text{cm}^3/\text{g}$$

$$0.200\,u_a + 0.800\,u_c = 1.031460\ \text{cm}^3/\text{g}$$

Subtracting the second equation from the first eliminates the constant coefficients of $u_a + u_c$:

$$(0.550 - 0.200)\,u_a + (0.450 - 0.800)\,u_c = 1.083072 - 1.031460$$

$$0.350\,(u_a - u_c) = 0.051612\ \text{cm}^3/\text{g} \quad\Longrightarrow\quad u_a - u_c = \frac{0.051612}{0.350} = 0.147463\ \text{cm}^3/\text{g}$$

Hence $u_a = u_c + 0.147463\ \text{cm}^3/\text{g}$. Substituting this into the second equation:

$$0.200\,(u_c + 0.147463) + 0.800\,u_c = 1.031460$$

$$u_c + 0.029493 = 1.031460 \quad\Longrightarrow\quad u_c = 1.031460 - 0.029493 = 1.001967\ \text{cm}^3/\text{g} \approx 1.0020\ \text{cm}^3/\text{g}$$

$$u_a = 1.001967 + 0.147463 = 1.149430\ \text{cm}^3/\text{g} \approx 1.1494\ \text{cm}^3/\text{g}$$

#### Amorphous and crystalline densities

Inverting $u_a$ and $u_c$:

$$\rho_a = \frac{1}{u_a} = \frac{1}{1.149430\ \text{cm}^3/\text{g}} = 0.8700\ \text{g/cm}^3 = 870.0\ \text{kg/m}^3$$

$$\rho_c = \frac{1}{u_c} = \frac{1}{1.001967\ \text{cm}^3/\text{g}} = 0.9980\ \text{g/cm}^3 = 998.0\ \text{kg/m}^3$$

## (b) Calculate the density of a polyethylene sample processed to $75.0\%$ crystallinity. [1.0 pts]

### Hint

Use the linear specific-volume relation with $f_{c,3} = 0.750$ and invert $1/\rho_3$.

### Checkpoint

- $1/\rho_3 = 1.0388\ \text{cm}^3/\text{g}$
- $\rho_3 = 0.9626\ \text{g/cm}^3 = 962.6\ \text{kg/m}^3$

### Solution

#### Specific volume and bulk density at $75.0\%$ crystallinity

Using $\frac{1}{\rho_3} = \frac{1 - f_{c,3}}{\rho_a} + \frac{f_{c,3}}{\rho_c}$ with $f_{c,3} = 0.750$:

$$\frac{1}{\rho_3} = 0.250\,u_a + 0.750\,u_c = 0.250\times 1.149430\ \text{cm}^3/\text{g} + 0.750\times 1.001967\ \text{cm}^3/\text{g} = 0.287358 + 0.751475 = 1.038833\ \text{cm}^3/\text{g}$$

Inverting to obtain the density:

$$\rho_3 = \frac{1}{1.038833\ \text{cm}^3/\text{g}} = 0.9626\ \text{g/cm}^3 = 962.6\ \text{kg/m}^3$$

## (c) Calculate the degree of crystallinity (in $\%$) of a polyethylene specimen whose measured density is $\rho_4 = 0.9450\ \text{g/cm}^3$. [1.0 pts]

### Hint

Substitute $\rho_s = 0.9450\ \text{g/cm}^3$ directly into the crystallinity equation of Session 19, Slide 25 using $\rho_a$ and $\rho_c$ from part (a).

### Checkpoint

- $\%\ \text{crystallinity} = 61.87\%$

### Solution

#### Evaluate numerator and denominator

Checking the physical order $\rho_a = 0.8700 < \rho_4 = 0.9450 < \rho_c = 0.9980\ \text{g/cm}^3$, the crystallinity must lie between $45.0\%$ ($\rho_1 = 0.9233$) and $75.0\%$ ($\rho_3 = 0.9626$). Using Session 19, Slide 25:

$$\rho_c(\rho_4 - \rho_a) = 0.998037\,(0.9450 - 0.87000) = 0.998037\times 0.07500 = 0.074853\ (\text{g/cm}^3)^2$$

$$\rho_4(\rho_c - \rho_a) = 0.9450\,(0.998037 - 0.87000) = 0.9450\times 0.128037 = 0.120995\ (\text{g/cm}^3)^2$$

#### Degree of crystallinity

$$\%\ \text{crystallinity} = \frac{0.074853}{0.120995}\times 100 = 61.865\% \approx 61.87\%$$

## (d) Describe and sketch qualitatively how $E(T)$ and the transitions $T_g$ and $T_m$ evolve across amorphous, $45\%$-crystalline, $80\%$-crystalline, and completely crystalline polyethylene. [1.2 pts]

### Hint

Refer to the $\log E$ versus $T$ schematic of Session 19, Slide 45, recalling that polyethylene has $T_g \approx -110^\circ\text{C}$ and $T_m \approx 110\text{–}137^\circ\text{C}$, and that higher crystallinity increases $T_m$ and raises the stiffness plateau between $T_g$ and $T_m$.

### Checkpoint

- **Completely amorphous:** single drop of several orders of magnitude at $T_g \approx -110^\circ\text{C}$ into a rubbery/viscous-flow tail; **no $T_m$**
- **Semicrystalline ($45\%$ vs $80\%$):** glass drop at $T_g$ shrinks as crystallinity increases; intermediate plateau rises with crystallinity; **melting temperature $T_m$ shifts upward** (from LDPE-like $\sim 110^\circ\text{C}$ toward HDPE-like $\sim 137^\circ\text{C}$)
- **Completely crystalline ($100\%$):** **no drop at $T_g$**; remains stiff until it melts abruptly at $T_m$

### Solution

#### Qualitative $\log E$ versus $T$ diagram [Session 19, Slide 45]

![[attachments/T9/s19-modulus-vs-temperature-crystallinity.png]]

Comparing the four states of linear polyethylene (whose transitions from the slides are $T_g \approx -110^\circ\text{C}$ [Session 19, Slide 29] and $T_m \approx 110\text{–}137^\circ\text{C}$ [Session 20, Slide 8]):

1. **Completely amorphous ($0\%$ crystalline):** below $T_g \approx -110^\circ\text{C}$, the polymer is a rigid glass ($E$ high). At $T_g$, the modulus drops steeply by several orders of magnitude because all chains belong to disordered amorphous regions that gain segmental mobility; above $T_g$ it passes through a short rubbery region and flows continuously into a viscous liquid with **no melting point $T_m$** [Session 19, Slides 23, 28, and 45].
2. **Sample 1 ($45\%$ crystalline, lower-density PE-like):** shows **both** $T_g$ and $T_m$. At $T_g$, the modulus drops significantly (driven by the $55\%$ amorphous fraction), but less than in the $0\%$ curve because the crystalline lamellae reinforce the polymer into a semicrystalline plateau between $T_g$ and $T_m$. At $T_m$, the lamellae melt and the polymer flows.
3. **Sample 2 ($80\%$ crystalline, HDPE-like):** because only $20\%$ of the mass is amorphous, the modulus drop at $T_g$ is noticeably **smaller**, and the semicrystalline plateau between $T_g$ and $T_m$ sits **higher** (closer to the $100\%$ crystalline curve), giving a stiffer solid at room temperature ($20^\circ\text{C} > T_g$). Moreover, higher crystallinity raises the melting point $T_m$ [Session 19, Slide 27], shifting the final drop upward toward the upper end of PE's melting range ($\sim 137^\circ\text{C}$).
4. **Completely crystalline ($100\%$ crystalline, theoretical limit):** has no amorphous phase, so **there is no $T_g$ drop**; the high modulus persists nearly flat all the way to $T_m$, where the crystal lattice melts abruptly [Session 19, Slide 45].

## Interpretation

- **Monotonic density ordering:** $\rho_a = 0.8700 < \rho_1 = 0.9233 < \rho_4 = 0.9450 < \rho_3 = 0.9626 < \rho_2 = 0.9695 < \rho_c = 0.9980\ \text{g/cm}^3$ — density always increases monotonically with crystallinity because folded lamellae pack more tightly than random coils [Session 19, Slide 24].
- **Mass fraction versus volume fraction (**extension**):** for Sample 4 ($61.87\%$ by mass), the crystalline volume fraction is $(\rho_4 - \rho_a)/(\rho_c - \rho_a) = 0.0750/0.1280 = 58.58\%$, smaller than the mass fraction by $\rho_4/\rho_c = 0.9469$ because the crystalline phase is denser.
- **SI dimensional check:** $[u] = \text{m}^3/\text{kg}$; $[\rho] = \text{kg/m}^3$; $[f_c]$ dimensionless; $\rho_c(\rho_s - \rho_a)/[\rho_s(\rho_c - \rho_a)]$ has units $(\text{kg/m}^3)^2 / (\text{kg/m}^3)^2 = 1$.
- **Common mistake:** writing $\rho_s = f_c \rho_c + (1 - f_c)\rho_a$ instead of averaging **specific volumes** $1/\rho_s = f_c/\rho_c + (1 - f_c)/\rho_a$: a mass-weighted density average treats $f_c$ as a *volume* fraction and gives $\rho_a = 0.8639$ and $\rho_c = 0.9959\ \text{g/cm}^3$, violating the definition of crystallinity on Session 19, Slide 25.

## Verification

- u_1 (cm^3/g) | 1/0.9233 | 1.083072
- u_2 (cm^3/g) | 1/0.9695 | 1.031460
- u_a - u_c (cm^3/g) | (1/0.9233-1/0.9695)/0.350 | 0.147463
- u_c (cm^3/g) | 1/0.9695-0.200*((1/0.9233-1/0.9695)/0.350) | 1.0020
- u_a (cm^3/g) | 1/0.9695+0.800*((1/0.9233-1/0.9695)/0.350) | 1.1494
- rho_a (g/cm^3) | 1/(1/0.9695+0.800*((1/0.9233-1/0.9695)/0.350)) | 0.8700
- rho_a (kg/m^3) | 1000/(1/0.9695+0.800*((1/0.9233-1/0.9695)/0.350)) | 870.0
- rho_c (g/cm^3) | 1/(1/0.9695-0.200*((1/0.9233-1/0.9695)/0.350)) | 0.9980
- rho_c (kg/m^3) | 1000/(1/0.9695-0.200*((1/0.9233-1/0.9695)/0.350)) | 998.0
- u_3 at 75% (cm^3/g) | 0.250*(1/0.9695+0.800*((1/0.9233-1/0.9695)/0.350))+0.750*(1/0.9695-0.200*((1/0.9233-1/0.9695)/0.350)) | 1.0388
- rho_3 (g/cm^3) | 1/(0.250*(1/0.9695+0.800*((1/0.9233-1/0.9695)/0.350))+0.750*(1/0.9695-0.200*((1/0.9233-1/0.9695)/0.350))) | 0.9626
- rho_3 (kg/m^3) | 1000/(0.250*(1/0.9695+0.800*((1/0.9233-1/0.9695)/0.350))+0.750*(1/0.9695-0.200*((1/0.9233-1/0.9695)/0.350))) | 962.6
- pct_cryst_4 (%) | (1/(1/0.9695-0.200*((1/0.9233-1/0.9695)/0.350)))*(0.9450-(1/(1/0.9695+0.800*((1/0.9233-1/0.9695)/0.350))))/(0.9450*((1/(1/0.9695-0.200*((1/0.9233-1/0.9695)/0.350)))-(1/(1/0.9695+0.800*((1/0.9233-1/0.9695)/0.350)))))*100 | 61.87
- vol_frac_4 (%) | (0.9450-(1/(1/0.9695+0.800*((1/0.9233-1/0.9695)/0.350))))/((1/(1/0.9695-0.200*((1/0.9233-1/0.9695)/0.350)))-(1/(1/0.9695+0.800*((1/0.9233-1/0.9695)/0.350))))*100 | 58.58

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
