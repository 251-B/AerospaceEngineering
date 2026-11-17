---
materia: Aerospace Materials I
tema: "Unit 4: the Fe-Fe3C diagram and steels"
bank_id: P12
title: "Three steels compared: microconstituents, hardness and alloying elements"
category: mt2_problem
archetype: fe-c-steels
level: conceptual
unit: 4
difficulty: 2
points: 3.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of the finals of June 2015 (question 2 d, effect of 8 % Mn) in MATERIALS_FINALEXAM_COMPILATION_2013-2017.pdf and 2017 (extraordinary, question 4, effect of alloying on the eutectoid point) in MATERIALS_FINALEXAM_2017_EXTRA.pdf; not an official exercise. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - fe-c-steels
  - alloying-elements
  - comparison
---

# Bank P12 — Three steels compared

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Fe-C questions of the finals (amounts of each microconstituent, effect of an alloying element on the eutectoid point). The data are a table of three steels, and the question asks for a comparison and a design limit. Method: Session 9, Slides 4, 8, 10, 12-14, 18-20 and 22-23; lever rule of Session 7, Slides 15-21. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

A supplier offers three plain carbon steels, all slowly cooled from the austenite field:

| Steel | Carbon content (wt% C) |
| :--- | :--- |
| S1 | 0.25 |
| S2 | 0.60 |
| S3 | 1.35 |

(a) Classify each steel and calculate the mass fraction of each of its microconstituents just below 727 °C.

(b) Calculate the mass fractions of the ferrite and cementite phases of each steel just below 727 °C. Rank the three steels by hardness and justify the ranking.

(c) A designer wants a plain carbon hypoeutectoid steel with at least 50 % pearlite. What is the lowest carbon content that meets the requirement? Is there any hypereutectoid steel that does not meet it?

(d) Steel S2 is now alloyed in one version with chromium and in another with manganese. State how each element changes the eutectoid temperature and the eutectoid composition, and how the microconstituents of S2 change. What would S2 look like if the eutectoid composition fell below 0.60 wt% C?

## Setup

#### Data

| Quantity | Symbol | Value | Source |
| :--- | :--- | :--- | :--- |
| Carbon contents | $C_0$ | 0.25, 0.60, 1.35 wt% C | statement |
| Carbon in ferrite at 727 °C | $C_\alpha$ | 0.022 wt% C | Session 9, Slides 5 and 10 |
| Eutectoid composition | $C_E$ | 0.76 wt% C | Session 9, Slide 10 |
| Carbon in cementite | $C_{\text{Fe}_3\text{C}}$ | 6.67 wt% C | Session 9, Slides 4 and 8 |
| Upper limit of steels | $C_{\gamma,\max}$ | 2.14 wt% C | Session 9, Slide 4 |
| Eutectoid temperature | $T_E$ | 727 °C | Session 9, Slide 10 |

Compositions enter only as ratios in the lever rule, so the wt% values are used directly (the factor 1/100 cancels). Percentages of the answers are fractions times 100.

#### Model

- Classification by carbon content: hypoeutectoid below 0.76, hypereutectoid from 0.76 to 2.14 wt% C (Session 9, Slide 4).
- Lever rule from the mass balances $W_1 + W_2 = 1$ and $W_1 C_1 + W_2 C_2 = C_0$ (Session 7, Slides 15-21), derived in part (a).
- Cementite is hard and brittle, ferrite is soft (Session 9, Slides 5 and 8).
- Alloying elements (Session 9, Slides 22-23): α-stabilisers move the eutectoid to higher temperature and lower %C; γ-stabilisers move it to lower temperature and lower %C.

## (a) Classification and microconstituents just below 727 °C [0.75 pts]

### Hint

Just above 727 °C each steel is the eutectoid austenite (0.76 wt% C) plus its proeutectoid phase; that austenite becomes pearlite. Use the short tie line on the side of the steel.

### Checkpoint

- S1 (hypoeutectoid): $W_{\alpha_p} = 0.6911$, $W_P = 0.3089$
- S2 (hypoeutectoid): $W_{\alpha_p} = 0.2168$, $W_P = 0.7832$
- S3 (hypereutectoid): $W_{\text{Fe}_3\text{C},p} = 0.0998$, $W_P = 0.9002$

### Solution

#### Classify the three steels

S1 (0.25) and S2 (0.60) are below 0.76 wt% C: **hypoeutectoid**, with proeutectoid ferrite and pearlite (Session 9, Slide 14). S3 (1.35) lies between 0.76 and 2.14 wt% C: **hypereutectoid**, with proeutectoid cementite and pearlite (Session 9, Slide 19).

#### Derive the lever rule once

At 727 + ΔT the steel is a proeutectoid phase of composition $C_p$ plus austenite of $C_E = 0.76$. Mass balance: $W_p + W_\gamma = 1$. Carbon balance: $W_p C_p + W_\gamma C_E = C_0$. Substitute $W_\gamma = 1 - W_p$ and group the terms in $W_p$:

$$W_p (C_p - C_E) = C_0 - C_E \quad\Rightarrow\quad W_p = \frac{C_0 - C_E}{C_p - C_E} = \frac{C_E - C_0}{C_E - C_p}$$

All that austenite becomes pearlite at 727 °C, and the proeutectoid phase does not change, so just below 727 °C $W_P = 1 - W_p$ (Session 9, Slides 18 and 20).

#### S1 and S2: proeutectoid ferrite ($C_p = C_\alpha = 0.022$, tie line length $0.76 - 0.022 = 0.738$)

$$W_{\alpha_p}(S1) = \frac{0.76 - 0.25}{0.738} = \frac{0.51}{0.738} = 0.6911, \qquad W_P(S1) = 1 - 0.6911 = 0.3089$$

$$W_{\alpha_p}(S2) = \frac{0.76 - 0.60}{0.738} = \frac{0.16}{0.738} = 0.2168, \qquad W_P(S2) = 1 - 0.2168 = 0.7832$$

#### S3: proeutectoid cementite ($C_p = 6.67$, tie line length $6.67 - 0.76 = 5.91$)

$$W_{\text{Fe}_3\text{C},p}(S3) = \frac{1.35 - 0.76}{5.91} = \frac{0.59}{5.91} = 0.0998, \qquad W_P(S3) = \frac{6.67 - 1.35}{5.91} = \frac{5.32}{5.91} = 0.9002$$

![[attachments/MAT-MT2/p12-constituents.svg]]

**Checks:** each pair adds up to 1; the pearlite grows from S1 to S2 as $C_0$ approaches 0.76, and in S3 it falls again as $C_0$ moves away on the cementite side.

## (b) Phases and ranking by hardness [0.75 pts]

### Hint

Long tie line α - Fe₃C for each steel. The hard phase is cementite.

### Checkpoint

- $W_{\text{Fe}_3\text{C}}$: S1 0.0343, S2 0.0869, S3 0.1998 (ferrite: 0.9657, 0.9131, 0.8002)
- Hardness: S3 > S2 > S1, in the order of the cementite fraction

### Solution

#### Lever rule on the tie line from 0.022 to 6.67 wt% C

Below 727 °C every steel lies in the α + Fe₃C field (Session 9, Slide 9). Tie line length $6.67 - 0.022 = 6.648$; with the lever rule of part (a) written for α and Fe₃C:

$$W_{\text{Fe}_3\text{C}} = \frac{C_0 - C_\alpha}{C_{\text{Fe}_3\text{C}} - C_\alpha}, \qquad W_\alpha = 1 - W_{\text{Fe}_3\text{C}}$$

$$W_{\text{Fe}_3\text{C}}(S1) = \frac{0.25 - 0.022}{6.648} = \frac{0.228}{6.648} = 0.0343, \qquad W_\alpha(S1) = 0.9657$$

$$W_{\text{Fe}_3\text{C}}(S2) = \frac{0.60 - 0.022}{6.648} = \frac{0.578}{6.648} = 0.0869, \qquad W_\alpha(S2) = 0.9131$$

$$W_{\text{Fe}_3\text{C}}(S3) = \frac{1.35 - 0.022}{6.648} = \frac{1.328}{6.648} = 0.1998, \qquad W_\alpha(S3) = 0.8002$$

#### Ranking by hardness

Ferrite is a soft phase and cementite is hard and brittle (Session 9, Slides 5 and 8), so at the same (slow) cooling the hardness grows with the fraction of cementite: **S3 (20.0 % Fe₃C) > S2 (8.7 %) > S1 (3.4 %)**. The fraction of cementite grows linearly with $C_0$, which is why harder steels are those with more carbon. S3 pays for its hardness with a brittle network of proeutectoid cementite at the grain boundaries (Session 9, Slide 19).

**Check:** the cementite of S3 splits into 0.0998 proeutectoid and $0.9002 \times 0.1110 = 0.0999$ inside the pearlite (0.1110 is the cementite of any pearlite, Session 9, Slide 13); $0.0998 + 0.0999 = 0.1998$.

## (c) Lowest carbon content for at least 50 % pearlite [0.75 pts]

### Hint

Write $W_P \geq 0.50$ with the hypoeutectoid lever rule and solve the inequality for $C_0$. For hypereutectoid steels, look at the end of the steel range.

### Checkpoint

- Hypoeutectoid: $C_0 \geq 0.391$ wt% C (S1 fails, S2 meets it)
- Every hypereutectoid steel meets it: the least pearlite, at 2.14 wt% C, is 0.7665

### Solution

#### Set up the inequality

For a hypoeutectoid steel the pearlite fraction is the lever rule of part (a):

$$W_P = \frac{C_0 - C_\alpha}{C_E - C_\alpha} \geq 0.50$$

Multiply both sides by the positive length $(C_E - C_\alpha) = 0.738$ (the sense of the inequality is kept) and add $C_\alpha$:

$$C_0 \geq C_\alpha + 0.50\,(C_E - C_\alpha) = 0.022 + 0.50 \times 0.738 = 0.022 + 0.369 = 0.391\ \text{wt\% C}$$

**Result:** the hypoeutectoid steel needs at least 0.391 wt% C. S1 (0.25, 30.9 % pearlite) fails; S2 (0.60, 78.3 %) passes.

#### Hypereutectoid steels

For $C_0 > 0.76$, $W_P = (6.67 - C_0)/5.91$ decreases as $C_0$ grows, so its smallest value in the steel range is at $C_0 = 2.14$ wt% C (Session 9, Slide 4):

$$W_P(2.14) = \frac{6.67 - 2.14}{5.91} = \frac{4.53}{5.91} = 0.7665$$

That is above 0.50, so **every hypereutectoid steel** has more than 50 % pearlite.

## (d) Effect of chromium and manganese on S2 [0.75 pts]

### Hint

Session 9, Slide 22 lists the α-stabilising and γ-stabilising elements; both kinds lower the eutectoid carbon content.

### Checkpoint

- Cr (favours α): eutectoid at higher temperature and lower %C
- Mn (favours γ): eutectoid at lower temperature and lower %C
- In both cases S2 is closer to the eutectoid: less proeutectoid ferrite, more pearlite, and the pearlite has less than 0.76 wt% C
- If the eutectoid composition fell below 0.60 wt% C, S2 would behave as hypereutectoid: proeutectoid cementite + pearlite

### Solution

#### Direction of the shift for each element

Session 9, Slide 22: elements that favour α (Si, P, Al, Be, Sn, Sb, As, Ti, Nb, V, Ta, Mo, W, **Cr**) stabilise ferrite and displace the eutectoid to **higher temperature and lower %C**; elements that favour γ (**Mn**, Co, Ni, Cu, Zn, Au) stabilise austenite and displace it to **lower temperature and lower %C**. Slide 23 gives the size of the shifts against the alloy content; the statement gives no content, so only the direction is asked.

| Version of S2 | Eutectoid temperature | Eutectoid composition |
| :--- | :--- | :--- |
| S2 + Cr (α-stabiliser) | above 727 °C | below 0.76 wt% C |
| S2 + Mn (γ-stabiliser) | below 727 °C | below 0.76 wt% C |

#### Consequence for the microconstituents of S2

In both versions the eutectoid composition $C_E'$ is lower than 0.76, so the pearlite (which always has the eutectoid composition) carries less than 0.76 wt% C. The proeutectoid ferrite is $W_{\alpha_p} = (C_E' - C_0)/(C_E' - C_\alpha)$: a smaller $C_E'$ shrinks the numerator, so S2 has **less proeutectoid ferrite and more pearlite** than the plain 0.60 wt% C steel of part (a), and is harder.

#### If the eutectoid composition fell below 0.60 wt% C

Then $C_0 = 0.60 > C_E'$ and S2 would sit on the cementite side of the new eutectoid: on slow cooling it would form **proeutectoid cementite** at the austenite grain boundaries, followed by pearlite, like a hypereutectoid plain steel (Session 9, Slide 19).

## Interpretation

The three steels show the whole story of the Fe-Fe₃C steel corner: the pearlite fraction peaks at the eutectoid and falls on both sides, but the cementite fraction, which sets the hardness, grows steadily with the carbon content. S1 is a soft, mostly ferritic steel; S2 is mostly pearlite; S3 is the hardest and the least tough, because of its 10 % grain-boundary cementite network. Alloying moves the eutectoid point, so "hypo" and "hyper" are relative to the eutectoid of the actual alloy, not always to 0.76 wt% C.

**Limiting cases:** $C_0 \to 0.022$ gives $W_{\alpha_p} \to 1$ and $W_{\text{Fe}_3\text{C}} \to 0$; $C_0 \to 0.76$ gives $W_P \to 1$ from both sides; $C_0 \to 6.67$ would give $W_{\text{Fe}_3\text{C}} \to 1$ (outside the steels).

**Dimensional check:** every lever rule is (wt%)/(wt%), dimensionless; the bound of part (c) is wt% + (dimensionless)(wt%) = wt%.

**Common exam mistake:** saying that a γ-stabiliser such as Mn raises the eutectoid carbon content because it "stabilises austenite". Session 9, Slide 22 states that both kinds of element lower the eutectoid %C; they differ only in the direction of the temperature shift.

## Verification

- S1 W_alpha_p | (0.76-0.25)/(0.76-0.022) | 0.6911
- S1 W_P | (0.25-0.022)/(0.76-0.022) | 0.3089
- S2 W_alpha_p | (0.76-0.60)/(0.76-0.022) | 0.2168
- S2 W_P | (0.60-0.022)/(0.76-0.022) | 0.7832
- S3 W_Fe3C_p | (1.35-0.76)/(6.67-0.76) | 0.0998
- S3 W_P | (6.67-1.35)/(6.67-0.76) | 0.9002
- S1 W_Fe3C | (0.25-0.022)/(6.67-0.022) | 0.0343
- S1 W_alpha | (6.67-0.25)/(6.67-0.022) | 0.9657
- S2 W_Fe3C | (0.60-0.022)/(6.67-0.022) | 0.0869
- S2 W_alpha | (6.67-0.60)/(6.67-0.022) | 0.9131
- S3 W_Fe3C | (1.35-0.022)/(6.67-0.022) | 0.1998
- S3 W_alpha | (6.67-1.35)/(6.67-0.022) | 0.8002
- S3 Fe3C inside pearlite | (6.67-1.35)/(6.67-0.76)*(0.76-0.022)/(6.67-0.022) | 0.0999
- C0 minimum for 50 % pearlite (wt% C) | 0.022+0.50*(0.76-0.022) | 0.391
- W_P at 2.14 wt% C | (6.67-2.14)/(6.67-0.76) | 0.7665

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
