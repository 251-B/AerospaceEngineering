---
materia: Aerospace Materials I
tema: "Unit 9: polymer molecular weight and crystallinity"
bank_id: P34
title: "Polymer molecular weight distribution and monomer identification"
category: mt3_problem
archetype: polymer-mw-crystallinity
level: standard
unit: 9
difficulty: 2
points: 5.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of Problems T9 (problem 8) and Session 19 (Slides 12-15); not an official exercise. Verified with tools/materials_bank/verify_mt3.py"
tags:
  - problem-bank
  - midterm-3
  - polymer-mw-crystallinity
  - molecular-weight
  - polydispersity
  - degree-of-polymerization
---

# Bank P34 — Polymer molecular weight distribution and monomer identification

> [!info] Practice item, not an official exercise
> Written for the bank in the style of Problems T9 (problem 8). Method: Session 19, Slides 12–15 and 50; Session 20, Slides 8–9 ($X_w = \bar{M}_w/M_0$ marked as extension). Every result is recomputed by tools/materials_bank/verify_mt3.py.

## Statement

A linear thermoplastic polymer sample is fractionated by gel-permeation chromatography into six molecular-weight intervals with the number fractions $x_i$ and weight fractions $w_i$ given below:

| Molecular-weight range (g/mol) | Number fraction, $x_i$ | Weight fraction, $w_i$ |
| :--- | ---: | ---: |
| 5 000 – 15 000 | 0.04 | 0.01 |
| 15 000 – 25 000 | 0.10 | 0.05 |
| 25 000 – 35 000 | 0.20 | 0.15 |
| 35 000 – 45 000 | 0.28 | 0.28 |
| 45 000 – 55 000 | 0.24 | 0.30 |
| 55 000 – 65 000 | 0.14 | 0.21 |

The number-average degree of polymerization is $X_n = 640$. Take atomic masses $\text{C} = 12.0$, $\text{H} = 1.0$, $\text{N} = 14.0$, $\text{O} = 16.0$, $\text{F} = 19.0$, and $\text{Cl} = 35.5\ \text{g/mol}$, and Avogadro's constant $N_A = 6.022\times10^{23}\ \text{mol}^{-1}$.

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| Number-average DP | $X_n$ | 640 | dimensionless |
| Sum of number fractions | $\sum x_i$ | $0.04+0.10+0.20+0.28+0.24+0.14 = 1.00$ | dimensionless |
| Sum of weight fractions | $\sum w_i$ | $0.01+0.05+0.15+0.28+0.30+0.21 = 1.00$ | dimensionless |
| Avogadro's constant | $N_A$ | $6.022\times10^{23}\ \text{mol}^{-1}$ | $6.022\times10^{23}\ \text{mol}^{-1}$ |

Unit conversion for molar mass: $1\ \text{g/mol} = 10^{-3}\ \text{kg/mol}$.

#### Model

- **Range representative mass:** each interval $[M_{\min,i}, M_{\max,i}]$ is represented by its midpoint $\bar{M}_i = \frac{1}{2}(M_{\min,i} + M_{\max,i})$ [Session 19, Slides 14–15].
- **Molecular weight averages:** $\bar{M}_n = \sum x_i \bar{M}_i$ and $\bar{M}_w = \sum w_i \bar{M}_i$ [Session 19, Slide 13].
- **Polydispersity index:** $\text{PDI} = I = \bar{M}_w / \bar{M}_n$ [Session 19, Slide 13].
- **Number-average degree of polymerization:** $X_n = \bar{M}_n / M_0$, where $M_0$ is the molar mass of the repeat unit [Session 19, Slide 12].
- **Weight-average degree of polymerization (extension):** by analogy with $X_n$, $X_w = \bar{M}_w / M_0$.
- **Number of chains in mass $m$:** $N_{\text{chains}} = (m / \bar{M}_n)\,N_A$.

## (a) Calculate the number-average molecular weight $\bar{M}_n$ and the weight-average molecular weight $\bar{M}_w$. [1.5 pts]

### Hint

Replace each interval by its midpoint $\bar{M}_i$, then build a table of $x_i \bar{M}_i$ and $w_i \bar{M}_i$ and sum each column.

### Checkpoint

- Midpoints: $10\,000,\ 20\,000,\ 30\,000,\ 40\,000,\ 50\,000,\ 60\,000\ \text{g/mol}$
- $\bar{M}_n = 40\,000\ \text{g/mol} = 40.00\ \text{kg/mol}$
- $\bar{M}_w = 44\,400\ \text{g/mol} = 44.40\ \text{kg/mol}$

### Solution

#### Midpoints and weighted contributions

Computing the midpoint $\bar{M}_i = (M_{\min,i} + M_{\max,i})/2$ for each range and multiplying by $x_i$ and $w_i$ [Session 19, Slides 13–15]:

| Range (g/mol) | Midpoint $\bar{M}_i$ (g/mol) | $x_i$ | $w_i$ | $x_i \bar{M}_i$ (g/mol) | $w_i \bar{M}_i$ (g/mol) |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 5 000 – 15 000 | 10 000 | 0.04 | 0.01 | 400 | 100 |
| 15 000 – 25 000 | 20 000 | 0.10 | 0.05 | 2 000 | 1 000 |
| 25 000 – 35 000 | 30 000 | 0.20 | 0.15 | 6 000 | 4 500 |
| 35 000 – 45 000 | 40 000 | 0.28 | 0.28 | 11 200 | 11 200 |
| 45 000 – 55 000 | 50 000 | 0.24 | 0.30 | 12 000 | 15 000 |
| 55 000 – 65 000 | 60 000 | 0.14 | 0.21 | 8 400 | 12 600 |
| **Total** | | **1.00** | **1.00** | **40 000** | **44 400** |

#### Number-average and weight-average molecular weights

$$\bar{M}_n = \sum x_i \bar{M}_i = 400 + 2000 + 6000 + 11\,200 + 12\,000 + 8400 = 40\,000\ \text{g/mol} = 40.00\ \text{kg/mol}$$

$$\bar{M}_w = \sum w_i \bar{M}_i = 100 + 1000 + 4500 + 11\,200 + 15\,000 + 12\,600 = 44\,400\ \text{g/mol} = 44.40\ \text{kg/mol}$$

## (b) Calculate the polydispersity index (PDI) and comment on the breadth of the molecular-weight distribution. [0.8 pts]

### Hint

Divide the weight-average molecular weight by the number-average molecular weight.

### Checkpoint

- $\text{PDI} = 1.110$ (narrow molecular-weight distribution, close to $1$)

### Solution

#### Polydispersity index

Using the definition from Session 19, Slide 13:

$$\text{PDI} = I = \frac{\bar{M}_w}{\bar{M}_n} = \frac{44\,400\ \text{g/mol}}{40\,000\ \text{g/mol}} = 1.110$$

Because $\text{PDI} = 1.110$ is close to unity (the monodisperse limit $\text{PDI} = 1$), the sample has a **narrow** molecular-weight distribution: most chains cluster near $35\,000\text{–}55\,000\ \text{g/mol}$.

## (c) Determine the molar mass of the repeat unit $M_0$ and identify the polymer from the candidate list: PE, PP, PVC, PTFE, PMMA, PS, Nylon 6,6, PC. [1.5 pts]

### Hint

Isolate $M_0$ from $X_n = \bar{M}_n / M_0$, then compute the repeat-unit molar mass of every candidate polymer from its chemical formula.

### Checkpoint

- $M_0 = 62.50\ \text{g/mol}$
- Polymer identified: **poly(vinyl chloride) (PVC)**, repeat unit $\mathrm{-[CH_2{-}CHCl]-}$ ($\mathrm{C_2H_3Cl}$, $M_0 = 62.5\ \text{g/mol}$)

### Solution

#### Repeat-unit molar mass from $X_n$

From $X_n = \bar{M}_n / M_0$ [Session 19, Slide 12], multiplying both sides by $M_0$ and dividing by $X_n$:

$$M_0 = \frac{\bar{M}_n}{X_n} = \frac{40\,000\ \text{g/mol}}{640} = 62.50\ \text{g/mol} = 0.06250\ \text{kg/mol}$$

#### Candidate comparison

Computing $M_0$ for each candidate polymer (repeat units from Session 19, Slide 50 and Session 20, Slides 8–9):

| Polymer | Repeat unit | Formula | Molar mass $M_0$ (g/mol) |
| :--- | :--- | :--- | ---: |
| PE | $\mathrm{-[CH_2{-}CH_2]-}$ | $\mathrm{C_2H_4}$ | $2(12.0)+4(1.0) = 28.0$ |
| PP | $\mathrm{-[CH_2{-}CH(CH_3)]-}$ | $\mathrm{C_3H_6}$ | $3(12.0)+6(1.0) = 42.0$ |
| **PVC** | $\mathrm{-[CH_2{-}CHCl]-}$ | $\mathrm{C_2H_3Cl}$ | $2(12.0)+3(1.0)+35.5 = 62.5$ |
| PTFE | $\mathrm{-[CF_2{-}CF_2]-}$ | $\mathrm{C_2F_4}$ | $2(12.0)+4(19.0) = 100.0$ |
| PMMA | $\mathrm{-[CH_2{-}C(CH_3)(COOCH_3)]-}$ | $\mathrm{C_5H_8O_2}$ | $5(12.0)+8(1.0)+2(16.0) = 100.0$ |
| PS | $\mathrm{-[CH_2{-}CH(C_6H_5)]-}$ | $\mathrm{C_8H_8}$ | $8(12.0)+8(1.0) = 104.0$ |
| Nylon 6,6 | $\mathrm{-[NH{-}(CH_2)_6{-}NH{-}CO{-}(CH_2)_4{-}CO]-}$ | $\mathrm{C_{12}H_{22}N_2O_2}$ | $12(12.0)+22(1.0)+2(14.0)+2(16.0) = 226.0$ |
| PC | $\mathrm{-[O{-}CO{-}O{-}C_6H_4{-}C(CH_3)_2{-}C_6H_4]-}$ | $\mathrm{C_{16}H_{14}O_3}$ | $16(12.0)+14(1.0)+3(16.0) = 254.0$ |

Only **poly(vinyl chloride) (PVC)** matches $M_0 = 62.50\ \text{g/mol}$.

## (d) Calculate the weight-average degree of polymerization $X_w$ and the total number of polymer chains in a $5.0\ \text{g}$ sample. [1.2 pts]

### Hint

$X_w = \bar{M}_w / M_0$, and the number of moles of chains in $m = 5.0\ \text{g}$ depends on the **number-average** molar mass $\bar{M}_n$, not $\bar{M}_w$.

### Checkpoint

- $X_w = 710.4$ (note $X_w / X_n = 1.110 = \text{PDI}$)
- $n = 1.250\times10^{-4}\ \text{mol}$, $N_{\text{chains}} = 7.528\times10^{19}\ \text{chains}$

### Solution

#### Weight-average degree of polymerization

Using $X_w = \bar{M}_w / M_0$ (**extension**):

$$X_w = \frac{\bar{M}_w}{M_0} = \frac{44\,400\ \text{g/mol}}{62.50\ \text{g/mol}} = 710.4$$

Notice that $X_w / X_n = 710.4 / 640 = 1.110 = \text{PDI}$, because dividing both $\bar{M}_w$ and $\bar{M}_n$ by the constant $M_0$ leaves the ratio unchanged.

#### Total number of chains in $5.0\ \text{g}$

The number-average molar mass $\bar{M}_n$ is the total mass divided by the total number of moles of polymer chains ($\bar{M}_n = \sum N_i M_i / \sum N_i$). Thus, in $m = 5.0\ \text{g} = 5.0\times10^{-3}\ \text{kg}$:

$$n = \frac{m}{\bar{M}_n} = \frac{5.0\ \text{g}}{40\,000\ \text{g/mol}} = 1.250\times10^{-4}\ \text{mol}$$

Multiplying by Avogadro's constant $N_A$:

$$N_{\text{chains}} = n\,N_A = 1.250\times10^{-4}\ \text{mol}\times 6.022\times10^{23}\ \text{mol}^{-1} = 7.5275\times10^{19} \approx 7.528\times10^{19}\ \text{chains}$$

## Interpretation

- **Internal consistency between $x_i$ and $w_i$ (**extension**):** the weight fraction of interval $i$ must satisfy $w_i = x_i \bar{M}_i / \bar{M}_n$. Checking every row: $0.04(10\,000)/40\,000 = 0.01$, $0.10(20\,000)/40\,000 = 0.05$, $0.20(30\,000)/40\,000 = 0.15$, $0.28(40\,000)/40\,000 = 0.28$, $0.24(50\,000)/40\,000 = 0.30$, and $0.14(60\,000)/40\,000 = 0.21$ — the two columns represent the exact same sample without rounding discrepancy.
- **Weight-average dominance:** as required by the Cauchy–Schwarz inequality ($\bar{M}_w \ge \bar{M}_n$), $\bar{M}_w = 44\,400 > \bar{M}_n = 40\,000\ \text{g/mol}$ because heavier chains carry a larger share of the total mass (notice that intervals above $45\,000\ \text{g/mol}$ hold $38\%$ of the chains by number, $0.24 + 0.14$, yet $51\%$ of the mass, $0.30 + 0.21$).
- **SI dimensional check:** $[\bar{M}_n] = [\bar{M}_w] = \text{kg/mol}$; $[\text{PDI}] = [X_n] = [X_w] = 1$ (dimensionless); $[M_0] = \text{kg/mol}$; $[n] = \text{kg}/(\text{kg/mol}) = \text{mol}$; $[N_{\text{chains}}] = \text{mol}\cdot\text{mol}^{-1} = 1$.
- **Common mistake:** dividing $m = 5.0\ \text{g}$ by $\bar{M}_w$ instead of $\bar{M}_n$ to count chains (which would undercount by $\text{PDI}$, giving $6.782\times10^{19}$), or swapping $x_i$ and $w_i$ so that $\bar{M}_n > \bar{M}_w$ and $\text{PDI} < 1$, which is mathematically impossible.

## Verification

- M_n (g/mol) | 0.04*10000+0.10*20000+0.20*30000+0.28*40000+0.24*50000+0.14*60000 | 40000
- M_w (g/mol) | 0.01*10000+0.05*20000+0.15*30000+0.28*40000+0.30*50000+0.21*60000 | 44400
- PDI | (0.01*10000+0.05*20000+0.15*30000+0.28*40000+0.30*50000+0.21*60000)/40000 | 1.110
- M_0 (g/mol) | 40000/640 | 62.50
- M_0 PVC (g/mol) | 2*12.0+3*1.0+35.5 | 62.5
- X_w | 44400/62.5 | 710.4
- n (mol) | 5.0/40000 | 1.250e-4
- N_chains | 5.0/40000*N_A | 7.528e19
- wrong N_chains with M_w | 5.0/44400*N_A | 6.782e19

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
