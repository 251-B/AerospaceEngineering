---
materia: Aerospace Materials I
tema: "Unit 4: the Fe-Fe3C diagram and steels"
bank_id: P11
title: "Carbon content of an unknown steel worked back from its micrograph"
category: mt2_problem
archetype: fe-c-steels
level: trap
unit: 4
difficulty: 3
points: 3.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of the finals of 2016 (extraordinary, question 4: carbon content from the proeutectoid ferrite) in MATERIALS_FINALEXAM_2016_EXTRA_SOL.pdf and 2017 (extraordinary, question 4: carbon content from the phases at 800 °C) in MATERIALS_FINALEXAM_2017_EXTRA.pdf; not an official exercise. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - fe-c-steels
  - reverse-lever-rule
  - micrograph
---

# Bank P11 — Carbon content of a steel from its micrograph

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Fe-C questions of the finals that ask for the carbon content of a steel from its microstructure. Here the data come from a micrograph, the lever rule is run backwards and it has two solutions. Method: Session 9, Slides 4, 10, 13-14 and 19-20; lever rule of Session 7, Slides 15-21. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

A bar of plain carbon steel of unknown composition (less than 2.14 wt% C) has been cooled slowly from the austenite field. A polished and etched section shows the structure of the figure. Point counting gives **88.0 % of lamellar colonies**; the remaining 12.0 % is a constituent X that forms a **thin, continuous network along the former austenite grain boundaries**, around the colonies. Microhardness indentations show that X is **much harder** than the lamellar colonies. Take the area fractions as mass fractions; they are the fractions formed just below 727 °C, which the slow cooling to room temperature keeps.

![[attachments/MAT-MT2/p11-micrograph.svg]]

(a) Identify the lamellar constituent. Show that a fraction of 88.0 % of it is compatible with two different carbon contents, one on each side of the eutectoid, and calculate both.

(b) Use the description of X to decide which of the two carbon contents is the right one, and justify it. For that steel, estimate the lowest temperature at which it is fully austenitic.

(c) Calculate the mass fractions of the ferrite and cementite phases of the steel just below 727 °C, and how the cementite is shared between X and the colonies.

(d) Give the phases present at 800 °C, their compositions and their mass fractions.

## Setup

#### Data

| Quantity | Symbol | Value | Source |
| :--- | :--- | :--- | :--- |
| Fraction of lamellar colonies | $W_P$ | 88.0 % = 0.880 | statement (point counting) |
| Fraction of constituent X | $W_X$ | 12.0 % = 0.120 | statement |
| Carbon in ferrite at 727 °C | $C_\alpha$ | 0.022 wt% C | Session 9, Slides 5 and 10 |
| Eutectoid composition | $C_E$ | 0.76 wt% C | Session 9, Slide 10 |
| Carbon in cementite | $C_{\text{Fe}_3\text{C}}$ | 6.67 wt% C | Session 9, Slides 4 and 8 |
| Austenite at the eutectic temperature | $C_{\gamma,\max}$ | 2.14 wt% C at 1147 °C | Session 9, Slides 6 and 10 |
| Eutectoid temperature | $T_E$ | 727 °C | Session 9, Slide 10 |

Percentages are turned into fractions by dividing by 100 (88.0 % → 0.880). Compositions stay in wt% because the lever rule only uses their ratios.

#### Model

- Lever rule from the mass balances $W_1 + W_2 = 1$ and $W_1 C_1 + W_2 C_2 = C_0$ (Session 7, Slides 15-21), here solved for $C_0$.
- Hypoeutectoid steels: proeutectoid ferrite + pearlite, short tie line $C_\alpha$ to $C_E$ (Session 9, Slides 14 and 18). Hypereutectoid steels: proeutectoid cementite + pearlite, short tie line $C_E$ to $C_{\text{Fe}_3\text{C}}$ (Session 9, Slides 19-20).
- Acm line approximated by the straight segment through $(0.76, 727)$ and $(2.14, 1147)$, as it is drawn in the bank figures of the Fe-Fe₃C diagram.
- Hypothesis: equilibrium cooling, area fraction = mass fraction (stated).

## (a) Lamellar constituent and the two candidate carbon contents [0.75 pts]

### Hint

Write the pearlite fraction with the lever rule twice: once for a hypoeutectoid steel and once for a hypereutectoid one. Each equation is linear in $C_0$.

### Checkpoint

- Lamellar colonies: pearlite (α + Fe₃C lamellae, 0.76 wt% C overall)
- Hypoeutectoid candidate: $C_0 = 0.671$ wt% C
- Hypereutectoid candidate: $C_0 = 1.469$ wt% C

### Solution

#### The lamellar constituent

Alternating lamellae of ferrite and cementite are **pearlite**, the product of the eutectoid reaction γ (0.76) → α (0.022) + Fe₃C (6.67) at 727 °C (Session 9, Slides 10 and 12). Pearlite always has the eutectoid composition, 0.76 wt% C, but it appears in both hypo- and hypereutectoid steels, so 88.0 % of pearlite alone does not tell on which side of 0.76 the steel lies.

#### Lever rule for the pearlite, derived once

Just above 727 °C the pearlite is still austenite of $C_E = 0.76$ wt% C, in equilibrium with a proeutectoid phase of composition $C_p$ ($C_\alpha$ or $C_{\text{Fe}_3\text{C}}$). Mass balance: $W_P + W_p = 1$. Carbon balance: $W_P C_E + W_p C_p = C_0$. Substitute $W_p = 1 - W_P$:

$$W_P C_E + (1 - W_P) C_p = C_0 \quad\Rightarrow\quad W_P (C_E - C_p) = C_0 - C_p \quad\Rightarrow\quad W_P = \frac{C_0 - C_p}{C_E - C_p}$$

#### Hypoeutectoid candidate ($C_p = C_\alpha$)

$$W_P = \frac{C_0 - C_\alpha}{C_E - C_\alpha}$$

Multiply both sides by $(C_E - C_\alpha)$ and add $C_\alpha$:

$$C_0 = C_\alpha + W_P (C_E - C_\alpha) = 0.022 + 0.880 \times (0.76 - 0.022) = 0.022 + 0.880 \times 0.738 = 0.022 + 0.6494 = 0.671\ \text{wt\% C}$$

#### Hypereutectoid candidate ($C_p = C_{\text{Fe}_3\text{C}}$)

$$W_P = \frac{C_0 - C_{\text{Fe}_3\text{C}}}{C_E - C_{\text{Fe}_3\text{C}}} = \frac{C_{\text{Fe}_3\text{C}} - C_0}{C_{\text{Fe}_3\text{C}} - C_E}$$

Multiply by $(C_{\text{Fe}_3\text{C}} - C_E)$ and isolate $C_0$:

$$C_0 = C_{\text{Fe}_3\text{C}} - W_P (C_{\text{Fe}_3\text{C}} - C_E) = 6.67 - 0.880 \times 5.91 = 6.67 - 5.2008 = 1.469\ \text{wt\% C}$$

**Result:** both 0.671 wt% C (hypoeutectoid, $0.671 < 0.76$) and 1.469 wt% C (hypereutectoid, $0.76 < 1.469 < 2.14$) are steels with 88.0 % pearlite. **Check:** both lie inside their ranges, so both are physically possible.

## (b) Choice of the right carbon content and full austenitisation [0.75 pts]

### Hint

Both proeutectoid phases nucleate on the austenite grain boundaries, so the position of X is not enough; its hardness decides (Session 9, Slides 5 and 8). For the temperature, find where the vertical line of the steel meets the boundary of the γ field.

### Checkpoint

- X is much harder than the pearlite, so it is proeutectoid cementite (not ferrite): the steel is hypereutectoid, $C_0 = 1.469$ wt% C
- Fully austenitic above about 943 °C (Acm line)

### Solution

#### What X is

In a hypoeutectoid steel the proeutectoid constituent is ferrite, which forms **equiaxed grains** of its own between the pearlite colonies (Session 9, Slide 14). In a hypereutectoid steel it is cementite, which forms a **thin network along the boundaries of the former austenite grains** around the pearlite (Session 9, Slide 19). The grain-boundary position alone does not decide, because proeutectoid ferrite also nucleates on the austenite grain boundaries (Session 9, Slide 15; Topic 4, section 14.2), and a large amount of it can outline them too. The hardness does decide: ferrite is a soft phase (Session 9, Slide 5) and would be softer than the pearlite, which contains 11 % of cementite, whereas cementite is hard and brittle (Session 9, Slide 8) and is harder than the pearlite. X is much harder than the colonies, so X is **proeutectoid cementite**, and its thin continuous network is the shape Slide 19 shows for it. The steel is hypereutectoid and

$$C_0 = 1.469\ \text{wt\% C}$$

The other candidate, 0.671 wt% C, would show 12.0 % of ferrite grains, not a grain-boundary network, and is rejected.

#### Lowest temperature of the single-phase austenite field

A hypereutectoid steel is fully austenitic above the Acm line (Session 9, Slides 4 and 11). On the straight Acm segment the temperature grows by $(1147 - 727)/(2.14 - 0.76) = 420/1.38 = 304.3$ °C per wt% C above the eutectoid point:

$$T_{Acm} = 727 + (1.469 - 0.76) \times 304.3 = 727 + 0.709 \times 304.3 = 727 + 215.8 = 942.8\ ^\circ\text{C}$$

**Result:** the bar must have been above about 943 °C to be entirely austenite. (Had the steel been the 0.671 wt% C candidate, it would have been fully austenitic above the A3 line, which at 0.671 wt% C lies only some 5 to 20 °C above 727 °C, depending on how its curve is read: the slides do not give A3 in numbers.)

## (c) Phases below 727 °C and where the cementite is [0.75 pts]

### Hint

Long tie line α - Fe₃C for the phases; the pearlite always has 11.10 % of cementite (Session 9, Slide 13).

### Checkpoint

- $W_{\text{Fe}_3\text{C}} = 0.2177$, $W_\alpha = 0.7823$
- Cementite in X (proeutectoid): 0.120; cementite in the pearlite: 0.0977

### Solution

#### Phases: lever rule on the tie line from 0.022 to 6.67 wt% C

Length $6.67 - 0.022 = 6.648$ (Session 9, Slide 9 for the α + Fe₃C field):

$$W_{\text{Fe}_3\text{C}} = \frac{C_0 - C_\alpha}{C_{\text{Fe}_3\text{C}} - C_\alpha} = \frac{1.469 - 0.022}{6.648} = \frac{1.447}{6.648} = 0.2177, \qquad W_\alpha = 1 - 0.2177 = 0.7823$$

#### Cementite inside the pearlite

The pearlite is the eutectoid steel, whose cementite fraction is (Session 9, Slide 13)

$$W_{\text{Fe}_3\text{C}}^{(P)} = \frac{C_E - C_\alpha}{C_{\text{Fe}_3\text{C}} - C_\alpha} = \frac{0.738}{6.648} = 0.1110$$

so the cementite of the colonies, per unit mass of steel, is $W_P \times 0.1110 = 0.880 \times 0.1110 = 0.0977$. The rest of the cementite is X, the proeutectoid cementite, $W_X = 0.120$.

**Check:** $0.120 + 0.0977 = 0.2177 = W_{\text{Fe}_3\text{C}}$, the value of the long tie line: the two independent routes agree. The ferrite is all inside the pearlite: $0.880 \times (1 - 0.1110) = 0.7823 = W_\alpha$.

## (d) Phases at 800 °C [0.75 pts]

### Hint

800 °C is between 727 °C and the Acm temperature of part (b): the steel is in the γ + Fe₃C field. Read the austenite composition on Acm at 800 °C.

### Checkpoint

- γ with 1.000 wt% C, $W_\gamma = 0.9172$
- Fe₃C with 6.67 wt% C, $W_{\text{Fe}_3\text{C}} = 0.0828$

### Solution

#### Field and ends of the tie line

Since $727 < 800 < 942.8$ °C, the point (1.469 wt% C, 800 °C) lies in the γ + Fe₃C field (Session 9, Slide 9). The tie line ends on Acm and on the cementite line. Inverting the straight Acm, $C = 0.76 + (T - 727)\times 1.38/420$:

$$C_\gamma(800) = 0.76 + (800 - 727) \times \frac{1.38}{420} = 0.76 + 73 \times 0.003286 = 0.76 + 0.2399 = 1.000\ \text{wt\% C}$$

#### Lever rule

Tie line length $6.67 - 1.000 = 5.670$:

$$W_\gamma = \frac{C_{\text{Fe}_3\text{C}} - C_0}{C_{\text{Fe}_3\text{C}} - C_\gamma} = \frac{6.67 - 1.469}{5.670} = \frac{5.201}{5.670} = 0.9172, \qquad W_{\text{Fe}_3\text{C}} = 1 - 0.9172 = 0.0828$$

**Result:** 91.7 % austenite with 1.000 wt% C and 8.3 % proeutectoid cementite with 6.67 wt% C. **Check:** the proeutectoid cementite grows from 8.3 % at 800 °C to 12.0 % at 727 + ΔT, as it must while the austenite slides down Acm towards 0.76 wt% C; carbon balance $0.9172 \times 1.000 + 0.0828 \times 6.67 = 0.917 + 0.552 = 1.469$ wt% C.

## Interpretation

A pearlite fraction measured on a micrograph fixes the distance of the steel from the eutectoid, not the side: the same 88.0 % lies 0.089 wt% C below 0.76 (on the short ferrite side of the diagram) and 0.709 wt% C above it (on the long cementite side). The shape of the proeutectoid constituent, grains of ferrite or a network of cementite, is the second datum that removes the ambiguity, exactly as Slides 14 and 19 of Session 9 show it.

**Limiting cases:** $W_P \to 1$ makes both candidates collapse to $C_E = 0.76$ wt% C (the eutectoid steel); $W_P \to 0$ gives $C_\alpha = 0.022$ on one side and 6.67 wt% C on the other, which is outside the steels: below 2.14 wt% C the pearlite of a hypereutectoid steel never falls below $(6.67 - 2.14)/5.91 = 0.7665$.

**Dimensional check:** $C_0 = C_\alpha + W_P (C_E - C_\alpha)$ is wt% + (dimensionless)(wt%) = wt%; $T_{Acm}$ is °C + (wt%)(°C/wt%) = °C.

**Common exam mistake:** stopping at the first root, 0.671 wt% C, without asking which proeutectoid phase the micrograph shows.

## Verification

- C0 hypoeutectoid candidate (wt% C) | 0.022+0.880*(0.76-0.022) | 0.671
- C0 hypereutectoid candidate (wt% C) | 6.67-0.880*(6.67-0.76) | 1.469
- 0.880 x 5.91 | 0.880*(6.67-0.76) | 5.2008
- T on Acm (°C) | 727+(6.67-0.880*(6.67-0.76)-0.76)*(1147-727)/(2.14-0.76) | 942.8
- W_Fe3C total | (6.67-0.880*(6.67-0.76)-0.022)/(6.67-0.022) | 0.2177
- W_alpha total | 1-(6.67-0.880*(6.67-0.76)-0.022)/(6.67-0.022) | 0.7823
- Fe3C fraction of pearlite | (0.76-0.022)/(6.67-0.022) | 0.1110
- Fe3C inside the pearlite | 0.880*(0.76-0.022)/(6.67-0.022) | 0.0977
- C_gamma at 800 °C (wt% C) | 0.76+(800-727)*(2.14-0.76)/(1147-727) | 1.000
- W_gamma at 800 °C | (6.67-(6.67-0.880*(6.67-0.76)))/(6.67-(0.76+(800-727)*(2.14-0.76)/(1147-727))) | 0.9172
- W_Fe3C at 800 °C | 1-(0.880*(6.67-0.76))/(6.67-(0.76+(800-727)*(2.14-0.76)/(1147-727))) | 0.0828
- minimum pearlite of a hypereutectoid steel | (6.67-2.14)/(6.67-0.76) | 0.7665

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
