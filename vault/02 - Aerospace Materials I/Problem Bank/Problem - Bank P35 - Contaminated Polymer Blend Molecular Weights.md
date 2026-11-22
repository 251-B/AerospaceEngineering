---
materia: Aerospace Materials I
tema: "Unit 9: polymer molecular weight and crystallinity"
bank_id: P35
title: "Contaminated polymer blend molecular weights"
category: mt3_problem
archetype: polymer-mw-crystallinity
level: trap
unit: 9
difficulty: 3
points: 5.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of the final of June 2017 (question 8) in MATERIALS_FINALEXAM_2017_EXTRA.pdf; not an official exercise. Verified with tools/materials_bank/verify_mt3.py"
tags:
  - problem-bank
  - midterm-3
  - polymer-mw-crystallinity
  - molecular-weight
  - polydispersity
  - contamination
---

# Bank P35 — Contaminated polymer blend molecular weights

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the final of June 2017 (question 8). Method: Session 19, Slide 13 (mass-to-number conversion and percentage changes marked as explicit algebraic derivation). Every result is recomputed by tools/materials_bank/verify_mt3.py.

## Statement

A monodisperse engineering polymer with molar mass $M_1 = 240\,000\ \text{g/mol}$ is accidentally contaminated during synthesis with $2.0\ \text{wt\%}$ of a low-molecular-weight residual oligomer of molar mass $M_2 = 1200\ \text{g/mol}$. Take Avogadro's constant as $N_A = 6.022\times10^{23}\ \text{mol}^{-1}$.

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| Pure polymer molar mass | $M_1$ | 240 000 g/mol | 240.0 kg/mol |
| Impurity molar mass | $M_2$ | 1 200 g/mol | 1.200 kg/mol |
| Weight fraction of polymer | $w_1$ | 0.980 (98.0 wt%) | dimensionless |
| Weight fraction of impurity | $w_2$ | 0.020 (2.0 wt%) | dimensionless |
| Avogadro's constant | $N_A$ | $6.022\times10^{23}\ \text{mol}^{-1}$ | $6.022\times10^{23}\ \text{mol}^{-1}$ |

#### Model

- **Mole (number) fractions from mass fractions:** taking a reference mass $m_{\text{ref}}$, the moles of component $i$ are $n_i = W_i / M_i = w_i m_{\text{ref}} / M_i$, and the number (mole) fraction is $x_i = N_i / \sum N_j = n_i / \sum n_j$ [Session 19, Slide 13].
- **Number-average molecular weight:** $\bar{M}_n = \sum x_i M_i = \frac{\sum W_i}{\sum (W_i / M_i)}$ [Session 19, Slide 13]. (Note: Session 19, Slide 13 has a print error writing $\sum W_i M_i$ in the numerator of the weight form; dimensional consistency requires $\sum W_i$.)
- **Weight-average molecular weight:** $\bar{M}_w = \sum w_i M_i$ [Session 19, Slide 13].
- **Polydispersity index:** $\text{PDI} = I = \bar{M}_w / \bar{M}_n$ [Session 19, Slide 13].
- **Molecule count in mass $m$:** $N_i = (w_i m / M_i)\,N_A$.

## (a) Convert the mass fractions $(w_1, w_2)$ into mole (number) fractions $(x_1, x_2)$. [1.2 pts]

### Hint

Choose a $100\ \text{g}$ (or $1\ \text{g}$) reference sample, compute the moles $n_1 = W_1/M_1$ and $n_2 = W_2/M_2$, and divide each by $n_1 + n_2$. Do not confuse $w_i$ with $x_i$!

### Checkpoint

- In $100\ \text{g}$: $n_1 = 4.083\times10^{-4}\ \text{mol}$, $n_2 = 1.667\times10^{-3}\ \text{mol}$, $n_{\text{tot}} = 2.075\times10^{-3}\ \text{mol}$
- $x_1 = 0.1968$ ($19.68\%$), $x_2 = 0.8032$ ($80.32\%$)

### Solution

#### Moles of each species in a $100\ \text{g}$ reference sample

Taking $m_{\text{ref}} = 100\ \text{g}$ gives $W_1 = 98.0\ \text{g}$ of polymer and $W_2 = 2.0\ \text{g}$ of impurity. Dividing each mass by its molar mass:

$$n_1 = \frac{W_1}{M_1} = \frac{98.0\ \text{g}}{240\,000\ \text{g/mol}} = 4.0833\times10^{-4}\ \text{mol} \approx 4.083\times10^{-4}\ \text{mol}$$

$$n_2 = \frac{W_2}{M_2} = \frac{2.0\ \text{g}}{1200\ \text{g/mol}} = 1.6667\times10^{-3}\ \text{mol} \approx 1.667\times10^{-3}\ \text{mol}$$

Summing to find the total number of moles:

$$n_{\text{tot}} = n_1 + n_2 = 4.0833\times10^{-4}\ \text{mol} + 16.6667\times10^{-4}\ \text{mol} = 2.0750\times10^{-3}\ \text{mol}$$

#### Mole (number) fractions

Because $N_i = n_i N_A$, the ratio of molecule counts $N_i/N_{\text{tot}}$ equals the mole fraction $n_i/n_{\text{tot}}$:

$$x_1 = \frac{n_1}{n_{\text{tot}}} = \frac{4.0833\times10^{-4}\ \text{mol}}{2.0750\times10^{-3}\ \text{mol}} = 0.19679 \approx 0.1968$$

$$x_2 = \frac{n_2}{n_{\text{tot}}} = \frac{1.6667\times10^{-3}\ \text{mol}}{2.0750\times10^{-3}\ \text{mol}} = 0.80321 \approx 0.8032$$

Check: $x_1 + x_2 = 0.1968 + 0.8032 = 1.0000$. Even though the impurity is only $2.0\ \text{wt\%}$ by mass, it constitutes **$80.32\%$** of the molecules by number!

## (b) Calculate $\bar{M}_n$ and $\bar{M}_w$ of the contaminated polymer, and determine the percentage drop of each average relative to the pure polymer. [1.4 pts]

### Hint

Use $x_1, x_2$ in $\bar{M}_n = \sum x_i M_i$ (and cross-check with $m_{\text{ref}}/n_{\text{tot}}$), and use $w_1, w_2$ in $\bar{M}_w = \sum w_i M_i$.

### Checkpoint

- $\bar{M}_n = 48\,193\ \text{g/mol}$ ($79.92\%$ drop from $240\,000\ \text{g/mol}$)
- $\bar{M}_w = 235\,224\ \text{g/mol}$ ($1.99\%$ drop from $240\,000\ \text{g/mol}$)

### Solution

#### Number-average molecular weight $\bar{M}_n$

Applying $\bar{M}_n = \sum x_i M_i$ [Session 19, Slide 13]:

$$\bar{M}_n = x_1 M_1 + x_2 M_2 = 0.19679\times 240\,000\ \text{g/mol} + 0.80321\times 1200\ \text{g/mol} = 47\,229 + 964 = 48\,193\ \text{g/mol} = 48.19\ \text{kg/mol}$$

Cross-checking directly with the total mass over total moles, $\bar{M}_n = m_{\text{ref}}/n_{\text{tot}}$:

$$\bar{M}_n = \frac{100\ \text{g}}{2.0750\times10^{-3}\ \text{mol}} = 48\,193\ \text{g/mol}$$

Percentage drop relative to the uncontaminated polymer ($M_1 = 240\,000\ \text{g/mol}$):

$$\Delta\bar{M}_n(\%) = \frac{240\,000 - 48\,193}{240\,000}\times 100 = \frac{191\,807}{240\,000}\times 100 = 79.92\%$$

#### Weight-average molecular weight $\bar{M}_w$

Applying $\bar{M}_w = \sum w_i M_i$ [Session 19, Slide 13]:

$$\bar{M}_w = w_1 M_1 + w_2 M_2 = 0.980\times 240\,000\ \text{g/mol} + 0.020\times 1200\ \text{g/mol} = 235\,200 + 24 = 235\,224\ \text{g/mol} = 235.2\ \text{kg/mol}$$

Percentage drop relative to the uncontaminated polymer:

$$\Delta\bar{M}_w(\%) = \frac{240\,000 - 235\,224}{240\,000}\times 100 = \frac{4776}{240\,000}\times 100 = 1.99\%$$

## (c) Calculate the polydispersity index (PDI) and explain why $\bar{M}_n$ is much more sensitive than $\bar{M}_w$ to low-MW tails or impurities. [1.2 pts]

### Hint

Compute $\bar{M}_w / \bar{M}_n$ and inspect how each average weights a molecule of mass $M_i$ (by count $N_i$ versus by mass $W_i = N_i M_i$).

### Checkpoint

- $\text{PDI} = 4.881$ (up from $1.000$ for the monodisperse polymer)
- $\bar{M}_n$ weights every molecule equally by number ($80.32\%$ of molecules are $1200\ \text{g/mol}$), whereas $\bar{M}_w$ weights by mass ($98.0\%$ of mass is $240\,000\ \text{g/mol}$)

### Solution

#### Polydispersity index

$$\text{PDI} = I = \frac{\bar{M}_w}{\bar{M}_n} = \frac{235\,224\ \text{g/mol}}{48\,193\ \text{g/mol}} = 4.881$$

Before contamination the monodisperse polymer had $\text{PDI} = 1.000$; adding just $2.0\ \text{wt\%}$ of low-MW oligomer raises $\text{PDI}$ nearly fivefold to $4.881$.

#### Physical origin of the sensitivity contrast

- **Why $\bar{M}_n$ plunges:** $\bar{M}_n = \sum N_i M_i / \sum N_i$ counts every molecule equally regardless of size. Because the oligomer is $200$ times lighter than the polymer chain ($240\,000/1200 = 200$), each $1\ \text{g}$ of oligomer supplies $200$ times as many molecules as $1\ \text{g}$ of polymer. Thus $2.0\ \text{wt\%}$ impurity floods the denominator $\sum N_i$ ($x_2 = 0.8032$), pulling $\bar{M}_n$ down by $79.92\%$.
- **Why $\bar{M}_w$ barely moves:** $\bar{M}_w = \sum W_i M_i / \sum W_i$ weights each species by its mass fraction $w_i$. Because $98.0\%$ of the sample mass still belongs to the $240\,000\ \text{g/mol}$ polymer, the $2.0\ \text{wt\%}$ oligomer contributes only $0.020\times 1200 = 24\ \text{g/mol}$ to $\bar{M}_w$, reducing it by only $1.99\%$.

## (d) Calculate the number of high-MW polymer chains $N_1$, impurity molecules $N_2$, and total molecules $N_{\text{tot}}$ in a $10.0\ \text{g}$ sample. [1.2 pts]

### Hint

Split the $10.0\ \text{g}$ mass using $w_1$ and $w_2$, divide each component mass by its own molar mass $M_1$ or $M_2$, and multiply by $N_A$. Verify that $N_1/N_{\text{tot}} = x_1$ and $m/\bar{M}_n \cdot N_A = N_{\text{tot}}$.

### Checkpoint

- $N_1 = 2.459\times10^{19}\ \text{chains}$, $N_2 = 1.004\times10^{20}\ \text{molecules}$
- $N_{\text{tot}} = 1.250\times10^{20}\ \text{molecules}$ (over four impurity molecules per polymer chain)

### Solution

#### Mass of each component in $10.0\ \text{g}$

$$m_1 = w_1\,m = 0.980\times 10.0\ \text{g} = 9.80\ \text{g} \qquad m_2 = w_2\,m = 0.020\times 10.0\ \text{g} = 0.20\ \text{g}$$

#### Molecule counts

Converting each mass to moles and multiplying by $N_A = 6.022\times10^{23}\ \text{mol}^{-1}$:

$$N_1 = \frac{m_1}{M_1}\,N_A = \frac{9.80\ \text{g}}{240\,000\ \text{g/mol}}\times 6.022\times10^{23}\ \text{mol}^{-1} = 4.0833\times10^{-5}\ \text{mol}\times 6.022\times10^{23}\ \text{mol}^{-1} = 2.459\times10^{19}\ \text{chains}$$

$$N_2 = \frac{m_2}{M_2}\,N_A = \frac{0.20\ \text{g}}{1200\ \text{g/mol}}\times 6.022\times10^{23}\ \text{mol}^{-1} = 1.6667\times10^{-4}\ \text{mol}\times 6.022\times10^{23}\ \text{mol}^{-1} = 1.0037\times10^{20} \approx 1.004\times10^{20}\ \text{molecules}$$

Summing for the total molecule count:

$$N_{\text{tot}} = N_1 + N_2 = 2.459\times10^{19} + 10.037\times10^{19} = 1.2496\times10^{20} \approx 1.250\times10^{20}\ \text{molecules}$$

Cross-check using $\bar{M}_n$: $(10.0\ \text{g}/48\,193\ \text{g/mol})\times 6.022\times10^{23}\ \text{mol}^{-1} = 1.250\times10^{20}\ \text{molecules}$, and $N_2/N_1 = 4.082$ (over four impurity molecules for every polymer chain).

## Interpretation

- **Colligative versus mechanical impact:** properties driven by molecule count (such as osmotic pressure and end-group concentration) track $\bar{M}_n$ and plummet by $80\%$, whereas melt viscosity and tensile stiffness depend primarily on the entangled long chains tracked by $\bar{M}_w$, although residual oligomer can act as an unintended plasticizer and lower $T_g$.
- **Limiting cases:** setting $w_2 \to 0$ gives $x_1 \to 1$, $\bar{M}_n \to M_1$, $\bar{M}_w \to M_1$, and $\text{PDI} \to 1$; setting $w_2 \to 1$ gives $\bar{M}_n \to M_2$, $\bar{M}_w \to M_2$, and $\text{PDI} \to 1$.
- **SI dimensional check:** $[n_i] = \text{kg}/(\text{kg/mol}) = \text{mol}$; $[x_i] = [w_i] = [\text{PDI}] = 1$ (dimensionless); $[\bar{M}_n] = [\bar{M}_w] = \text{kg/mol}$; $[N_i] = 1$.
- **Common mistakes (the traps):** (1) plugging mass fractions directly into $\bar{M}_n = 0.98(240\,000) + 0.02(1200) = 235\,224\ \text{g/mol}$, which actually computes $\bar{M}_w$ and yields $\text{PDI} = 1$; (2) using the printed slide typo $\sum W_i M_i / \sum(W_i/M_i)$ for $\bar{M}_n$, which has units of $(\text{g}^2/\text{mol})/\text{mol} = \text{g}^2/\text{mol}^2$ instead of $\text{g/mol}$.

## Verification

- n1 in 100 g (mol) | 98.0/240000 | 4.083e-4
- n2 in 100 g (mol) | 2.0/1200 | 1.667e-3
- n_tot in 100 g (mol) | 98.0/240000+2.0/1200 | 2.075e-3
- x_1 | (98.0/240000)/(98.0/240000+2.0/1200) | 0.1968
- x_2 | (2.0/1200)/(98.0/240000+2.0/1200) | 0.8032
- M_n (g/mol) | 100/(98.0/240000+2.0/1200) | 48193
- M_n drop (%) | (240000-100/(98.0/240000+2.0/1200))/240000*100 | 79.92
- M_w (g/mol) | 0.98*240000+0.02*1200 | 235224
- M_w drop (%) | (240000-(0.98*240000+0.02*1200))/240000*100 | 1.99
- PDI | (0.98*240000+0.02*1200)/(100/(98.0/240000+2.0/1200)) | 4.881
- N_1 in 10 g | 9.8/240000*N_A | 2.459e19
- N_2 in 10 g | 0.2/1200*N_A | 1.004e20
- N_tot in 10 g | (9.8/240000+0.2/1200)*N_A | 1.250e20
- ratio N2/N1 | (0.2/1200)/(9.8/240000) | 4.082

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
