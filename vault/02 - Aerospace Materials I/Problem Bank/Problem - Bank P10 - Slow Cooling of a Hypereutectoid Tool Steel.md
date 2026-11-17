---
materia: Aerospace Materials I
tema: "Unit 4: the Fe-Fe3C diagram and steels"
bank_id: P10
title: "Slow cooling of a hypereutectoid tool steel read on the Fe-Fe3C diagram"
category: mt2_problem
archetype: fe-c-steels
level: standard
unit: 4
difficulty: 2
points: 3.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of the finals of June 2015 (question 2 c, cementite in each microconstituent) in MATERIALS_FINALEXAM_COMPILATION_2013-2017.pdf and 2017 (extraordinary, question 4) in MATERIALS_FINALEXAM_2017_EXTRA.pdf; not an official exercise. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - fe-c-steels
  - hypereutectoid
  - proeutectoid-cementite
---

# Bank P10 — Slow cooling of a hypereutectoid tool steel

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Fe-C questions of the finals (cementite in each microconstituent, phases at a second temperature). The data are given as a narrative and read from the figure. Method: Session 9, Slides 4, 10, 13 and 19-20; lever rule of Session 7, Slides 15-21. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

A 2.5 kg forging of a tool steel with 1.10 wt% C is held at 950 °C (point a of the figure) until it is completely austenitic. It is then cooled slowly to room temperature, so the steel follows the equilibrium diagram. At point b the first new constituent appears at the grain boundaries; the steel goes on cooling through 780 °C, reaches the eutectoid line and ends at room temperature. The figure is the steel corner of the metastable Fe-Fe₃C diagram drawn with the values of the course; the Acm line is drawn as a straight segment between its two printed ends.

![[attachments/MAT-MT2/p10-diagram.svg]]

(a) Read the temperature of point b on the diagram. Which constituent starts to form there, and where? Give the phases, their compositions and their mass fractions at 780 °C.

(b) Write the reaction that takes place at 727 °C and calculate the mass, in kg, of proeutectoid cementite and of pearlite in the forging at 727 − ΔT °C.

(c) Calculate the mass of the ferrite and cementite phases in the forging at 727 − ΔT °C.

(d) How much of the cementite is inside the pearlite? Check it in two independent ways, and explain where the proeutectoid cementite sits and what that means for the toughness of the steel.

## Setup

#### Data

| Quantity | Symbol | Value | Source |
| :--- | :--- | :--- | :--- |
| Mass of the forging | $m$ | 2.5 kg | statement |
| Carbon content | $C_0$ | 1.10 wt% C | statement |
| Eutectoid point | $(C_E, T_E)$ | (0.76 wt% C, 727 °C) | figure; Session 9, Slide 10 |
| Upper end of Acm (maximum solubility of C in γ) | $(C_{\gamma,\max}, T_{eu})$ | (2.14 wt% C, 1147 °C) | figure; Session 9, Slides 6 and 10 |
| Carbon in ferrite at 727 °C | $C_\alpha$ | 0.022 wt% C | figure; Session 9, Slides 5 and 10 |
| Carbon in cementite | $C_{\text{Fe}_3\text{C}}$ | 6.67 wt% C | Session 9, Slides 4 and 8 |

Compositions enter only as ratios in the lever rule, so they are used in wt% (the factor 1/100 that turns wt% into a fraction cancels). Masses stay in kg.

#### Model

- Since $0.76 < C_0 = 1.10 < 2.14$ wt% C, the steel is **hypereutectoid** (Session 9, Slide 4): its microconstituents below 727 °C are proeutectoid cementite and pearlite (Session 9, Slide 19).
- Lever rule, from the mass balances $W_1 + W_2 = 1$ and $W_1 C_1 + W_2 C_2 = C_0$ (Session 7, Slides 15-21); derived in part (a).
- The straight Acm segment of the figure, through $(0.76, 727)$ and $(2.14, 1147)$, gives the boundary γ / γ + Fe₃C: $T_{Acm}(C) = 727 + (C - 0.76)\,\dfrac{1147 - 727}{2.14 - 0.76}$ °C.
- Hypothesis: equilibrium (slow) cooling.

## (a) Start of the transformation and phases at 780 °C [0.75 pts]

### Hint

Point b is where the vertical line of the steel meets Acm. At 780 °C the tie line goes from the Acm line to the cementite line at 6.67 wt% C.

### Checkpoint

- Point b: about 830 °C (830.5 °C on the straight Acm); proeutectoid cementite starts to form at the austenite grain boundaries
- At 780 °C: γ with 0.934 wt% C, $W_\gamma = 0.9711$; Fe₃C with 6.67 wt% C, $W_{\text{Fe}_3\text{C}} = 0.0289$

### Solution

#### Read point b on the Acm line

From a (950 °C) down to b the steel is single-phase austenite with 1.10 wt% C ($W_\gamma = 1$). Point b lies on the straight Acm segment. Between its printed ends, the temperature grows linearly with the composition: the slope is $(1147 - 727)/(2.14 - 0.76) = 420/1.38 = 304.3$ °C per wt% C. At $C_0 = 1.10$:

$$T_b = 727 + (1.10 - 0.76) \times \frac{420}{1.38} = 727 + 0.34 \times 304.3 = 727 + 103.5 = 830.5\ ^\circ\text{C}$$

On the dashed 50 °C grid of the figure, b lies three fifths of the way from the 800 °C line to the 850 °C line: about 830 °C, in agreement.

#### Constituent that forms at b

Below Acm the solubility of carbon in austenite is lower than 1.10 wt% C, so the excess carbon leaves the austenite as **proeutectoid cementite**, Fe₃C, which forms along the boundaries of the austenite grains (Session 9, Slide 19). The austenite that remains becomes poorer in carbon, following the Acm line down towards 0.76 wt% C.

#### Composition of the austenite at 780 °C

At 780 °C the tie line starts on Acm. Invert the straight line $T = 727 + (C - 0.76)\times 420/1.38$ for $C$: subtract 727, multiply by $1.38/420$, add 0.76:

$$C_\gamma(780) = 0.76 + (780 - 727) \times \frac{1.38}{420} = 0.76 + 53 \times 0.003286 = 0.76 + 0.1741 = 0.934\ \text{wt\% C}$$

The other end of the tie line is cementite, $C_{\text{Fe}_3\text{C}} = 6.67$ wt% C (a vertical line on the diagram, Session 9, Slide 4).

#### Lever rule, derived from the mass balances

Mass of the alloy: $W_\gamma + W_{\text{Fe}_3\text{C}} = 1$. Carbon: $W_\gamma C_\gamma + W_{\text{Fe}_3\text{C}} C_{\text{Fe}_3\text{C}} = C_0$. Put $W_\gamma = 1 - W_{\text{Fe}_3\text{C}}$ into the carbon balance:

$$C_\gamma + W_{\text{Fe}_3\text{C}}(C_{\text{Fe}_3\text{C}} - C_\gamma) = C_0$$

Subtract $C_\gamma$ and divide by $(C_{\text{Fe}_3\text{C}} - C_\gamma)$:

$$W_{\text{Fe}_3\text{C}} = \frac{C_0 - C_\gamma}{C_{\text{Fe}_3\text{C}} - C_\gamma}, \qquad W_\gamma = \frac{C_{\text{Fe}_3\text{C}} - C_0}{C_{\text{Fe}_3\text{C}} - C_\gamma}$$

#### Substitute at 780 °C

Tie line length: $6.67 - 0.934 = 5.736$ wt% C.

$$W_\gamma = \frac{6.67 - 1.10}{6.67 - 0.934} = \frac{5.57}{5.736} = 0.9711, \qquad W_{\text{Fe}_3\text{C}} = \frac{1.10 - 0.934}{5.736} = \frac{0.166}{5.736} = 0.0289$$

**Result:** at 780 °C, 97.1 % austenite with 0.934 wt% C and 2.9 % cementite with 6.67 wt% C. **Check:** $0.9711 \times 0.934 + 0.0289 \times 6.67 = 0.907 + 0.193 = 1.10$ wt% C.

## (b) Eutectoid reaction, proeutectoid cementite and pearlite in the forging [0.75 pts]

### Hint

Just above 727 °C the austenite has reached 0.76 wt% C. All of it becomes pearlite; the cementite formed above 727 °C stays as proeutectoid cementite.

### Checkpoint

- Reaction on cooling at 727 °C: γ (0.76) → α (0.022) + Fe₃C (6.67), eutectoid, product pearlite
- $W_{\text{Fe}_3\text{C},p} = 0.0575$ → 0.1438 kg; $W_P = 0.9425$ → 2.356 kg

### Solution

#### The eutectoid reaction

Cooling: γ (0.76 wt% C) → α (0.022 wt% C) + Fe₃C (6.67 wt% C) at 727 °C, **eutectoid** reaction; the lamellar product is pearlite (Session 9, Slides 10 and 12).

#### Tie line just above 727 °C

At 727 + ΔT the tie line runs from the eutectoid austenite, $C_E = 0.76$, to cementite, 6.67 wt% C; length $6.67 - 0.76 = 5.91$. With the lever rule of part (a):

$$W_{\text{Fe}_3\text{C},p} = \frac{C_0 - C_E}{C_{\text{Fe}_3\text{C}} - C_E} = \frac{1.10 - 0.76}{5.91} = \frac{0.34}{5.91} = 0.0575$$

$$W_\gamma(727 + \Delta T) = \frac{6.67 - 1.10}{5.91} = \frac{5.57}{5.91} = 0.9425$$

#### Microconstituents at 727 − ΔT and their masses

The proeutectoid cementite does not take part in the reaction, and all the austenite of 0.76 wt% C becomes pearlite, so $W_P = 0.9425$ (Session 9, Slide 20). With $m_i = W_i\,m$ and $m = 2.5$ kg:

$$m_{\text{Fe}_3\text{C},p} = 0.05753 \times 2.5\ \text{kg} = 0.1438\ \text{kg}, \qquad m_P = 0.9425 \times 2.5\ \text{kg} = 2.356\ \text{kg}$$

**Checks:** $0.1438 + 2.356 = 2.500$ kg. Between 780 °C (2.9 % cementite) and 727 °C (5.75 %) the proeutectoid cementite has kept growing, as expected while the austenite moves down Acm.

## (c) Ferrite and cementite phases in the forging at 727 − ΔT [0.75 pts]

### Hint

Use the long tie line from ferrite (0.022) to cementite (6.67 wt% C).

### Checkpoint

- $W_{\text{Fe}_3\text{C}} = 0.1622$ → 0.4054 kg of cementite
- $W_\alpha = 0.8378$ → 2.095 kg of ferrite

### Solution

#### Lever rule on the tie line α - Fe₃C

Below 727 °C the steel lies in the α + Fe₃C field (Session 9, Slide 9); the tie line runs from $C_\alpha = 0.022$ to 6.67 wt% C, length $6.67 - 0.022 = 6.648$:

$$W_{\text{Fe}_3\text{C}} = \frac{C_0 - C_\alpha}{C_{\text{Fe}_3\text{C}} - C_\alpha} = \frac{1.10 - 0.022}{6.648} = \frac{1.078}{6.648} = 0.1622, \qquad W_\alpha = \frac{6.67 - 1.10}{6.648} = \frac{5.57}{6.648} = 0.8378$$

#### Masses

$$m_{\text{Fe}_3\text{C}} = 0.16215 \times 2.5\ \text{kg} = 0.4054\ \text{kg}, \qquad m_\alpha = 0.83785 \times 2.5\ \text{kg} = 2.095\ \text{kg}$$

**Check:** $0.4054 + 2.095 = 2.500$ kg. Even this hard tool steel is about 84 % ferrite by mass.

## (d) Cementite inside the pearlite, and where the proeutectoid cementite sits [0.75 pts]

### Hint

Total cementite = proeutectoid cementite + eutectoid cementite. The second way uses the make-up of any pearlite (Session 9, Slide 13).

### Checkpoint

- Eutectoid cementite: $W = 0.1046$ → 0.2616 kg (both ways)
- Proeutectoid cementite: a continuous network along the former austenite grain boundaries; hard and brittle, it lowers the toughness

### Solution

#### First way: subtract the proeutectoid cementite from the total

$$W_{\text{Fe}_3\text{C},E} = W_{\text{Fe}_3\text{C}} - W_{\text{Fe}_3\text{C},p} = \frac{1.078}{6.648} - \frac{0.34}{5.91} = 0.16215 - 0.05753 = 0.1046$$

$$m_{\text{Fe}_3\text{C},E} = 0.10462 \times 2.5\ \text{kg} = 0.2616\ \text{kg}$$

#### Second way: the make-up of pearlite

Every pearlite has the composition of the eutectoid, 0.76 wt% C, so its cementite fraction is the lever rule of the eutectoid steel (Session 9, Slide 13):

$$W_{\text{Fe}_3\text{C}}^{(P)} = \frac{0.76 - 0.022}{6.67 - 0.022} = \frac{0.738}{6.648} = 0.1110$$

The pearlite of the forging is 2.356 kg (part b), so its cementite is $0.1110 \times 2.356 = 0.2616$ kg, the same value.

#### Where the proeutectoid cementite sits

The proeutectoid cementite forms between b and 727 °C at the boundaries of the austenite grains, so after cooling it is a thin, continuous network around the pearlite colonies (Session 9, Slide 19). Cementite is hard and brittle (Session 9, Slide 8), and a continuous brittle film along the grain boundaries gives a crack an easy path: the 0.1438 kg network makes the forging hard but lowers its toughness.

## Interpretation

Of the 0.4054 kg of cementite in the forging, about one third (0.1438 kg) formed above 727 °C as a grain-boundary network and two thirds (0.2616 kg) formed at 727 °C inside the pearlite lamellae. The transformation starts about 103 °C above the eutectoid line because 1.10 wt% C exceeds what austenite can hold below 830 °C.

**Limiting cases:** $C_0 \to 0.76$ makes point b fall to 727 °C and $W_{\text{Fe}_3\text{C},p} \to 0$ (all pearlite); $C_0 \to 2.14$ moves b to 1147 °C and gives the largest proeutectoid cementite of a steel, $(2.14 - 0.76)/5.91 = 0.234$.

**Dimensional check:** a temperature on Acm is °C + (wt%)·(°C/wt%) = °C; every lever rule is (wt%)/(wt%), dimensionless; a mass is a fraction times kg.

**Common exam mistake:** using the long tie line (0.022 to 6.67) for the proeutectoid cementite. That gives the total cementite, 0.1622; the proeutectoid part needs the short tie line from 0.76 wt% C.

## Verification

- T at point b (°C) | 727+(1.10-0.76)*(1147-727)/(2.14-0.76) | 830.5
- Acm slope (°C per wt% C) | (1147-727)/(2.14-0.76) | 304.3
- C_gamma at 780 °C (wt% C) | 0.76+(780-727)*(2.14-0.76)/(1147-727) | 0.934
- W_gamma at 780 °C | (6.67-1.10)/(6.67-(0.76+(780-727)*(2.14-0.76)/(1147-727))) | 0.9711
- W_Fe3C at 780 °C | 1-(6.67-1.10)/(6.67-(0.76+(780-727)*(2.14-0.76)/(1147-727))) | 0.0289
- W_Fe3C proeutectoid | (1.10-0.76)/(6.67-0.76) | 0.0575
- W_pearlite | (6.67-1.10)/(6.67-0.76) | 0.9425
- m proeutectoid cementite (kg) | 2.5*(1.10-0.76)/(6.67-0.76) | 0.1438
- m pearlite (kg) | 2.5*(6.67-1.10)/(6.67-0.76) | 2.356
- W_Fe3C total | (1.10-0.022)/(6.67-0.022) | 0.1622
- W_alpha total | (6.67-1.10)/(6.67-0.022) | 0.8378
- m cementite (kg) | 2.5*(1.10-0.022)/(6.67-0.022) | 0.4054
- m ferrite (kg) | 2.5*(6.67-1.10)/(6.67-0.022) | 2.095
- W_Fe3C eutectoid | (1.10-0.022)/(6.67-0.022)-(1.10-0.76)/(6.67-0.76) | 0.1046
- m eutectoid cementite (kg) | 2.5*((1.10-0.022)/(6.67-0.022)-(1.10-0.76)/(6.67-0.76)) | 0.2616
- Fe3C fraction of pearlite | (0.76-0.022)/(6.67-0.022) | 0.1110
- max proeutectoid cementite of a steel | (2.14-0.76)/(6.67-0.76) | 0.234

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
