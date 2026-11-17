---
materia: Aerospace Materials I
tema: "Unit 4: phase diagrams"
bank_id: P06
title: "Building a eutectic diagram from a description and using it"
category: mt2_problem
archetype: eutectic-lever-rule
level: standard
unit: 4
difficulty: 2
points: 3.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of the final of June 2014 (question 3) in MATERIALS_FINALEXAM_COMPILATION_2013-2017.pdf and of Problem 8 of Problems T4_PhaseDiagrams I.pdf, with a new system (900, 700 and 550 °C; 20, 70 and 92 wt% B), a hypereutectic alloy and a solvus question; not an official exercise. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - eutectic-lever-rule
  - phase-diagram-construction
  - hypereutectic
  - solvus
---

# Bank P06 — Building a eutectic diagram from a description and using it

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the final of June 2014 (question 3), where the diagram is built from a list of features, and of Problem 8 of the Unit 4 sheet. Method: binary eutectic systems [Session 7 Slides 26-27], tie line and lever rule [Session 7 Slides 15-16], microconstituents [Session 7 Slides 31-32], solvus and precipitation [Session 8 Slides 2-4]. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

Two metals A and B are completely soluble in the liquid state and partially soluble in the solid state, where they form a solid solution α rich in A and a solid solution β rich in B. Metal A melts at 900 °C and metal B at 700 °C. The system has a single invariant point, a eutectic at 550 °C, where the liquid contains 70 wt% B. At that temperature α can dissolve at most 20 wt% B and β at most 8 wt% A. At room temperature (20 °C) the solubilities fall to 5 wt% B in α and 3 wt% A in β. Assume that every boundary of the diagram is a straight line between the points given, and that cooling is slow (equilibrium).

(a) Draw the phase diagram (temperature against wt% B), label every region and write the invariant reaction.

(b) For an alloy of 85 wt% B: at which temperature does it start to solidify and what is the composition of the first solid? Give the phases, their compositions and their mass fractions at 600 °C.

(c) For the same alloy, give the microconstituents and their mass fractions just below 550 °C, and the mass fraction of each phase inside the eutectic.

(d) Which alloys of the system contain eutectic at room temperature? An alloy of 12 wt% B contains none: at which temperature does β appear in it, and how much β is there at 20 °C?

## Setup

#### Data

| Feature of the statement | Point of the diagram (wt% B, °C) | Meaning |
| :--- | :--- | :--- |
| A melts at 900 °C | (0, 900) | top of the liquidus and of the α solidus |
| B melts at 700 °C | (100, 700) | top of the liquidus and of the β solidus |
| Eutectic, liquid of 70 wt% B at 550 °C | E = (70, 550) | lowest point of the liquidus |
| α holds at most 20 wt% B at 550 °C | (20, 550) | α end of the eutectic line |
| β holds at most 8 wt% A at 550 °C | (100 − 8, 550) = (92, 550) | β end of the eutectic line |
| α holds 5 wt% B at 20 °C | (5, 20) | lower end of the α solvus |
| β holds 3 wt% A at 20 °C | (100 − 3, 20) = (97, 20) | lower end of the β solvus |
| Alloys | $C_0$ = 85 and 12 wt% B | parts (b) to (d) |

The composition axis is wt% B, so a content of A is turned into a content of B with $C_B = 100 - C_A$: 8 wt% A is 92 wt% B, and 3 wt% A is 97 wt% B. The lever rule uses ratios of composition differences, so the wt% can be used directly (the factor 1/100 that turns them into mass fractions cancels).

#### Model

- Binary eutectic system with partial solid solubility [Session 7 Slides 26-27]: liquidus from each melting point down to E; solidus from each melting point to the end of the eutectic line; solvus from each end of the eutectic line down to room temperature.
- Straight boundary through $(C_1, T_1)$ and $(C_2, T_2)$, as the statement imposes: $C = C_1 + (T - T_1)\dfrac{C_2 - C_1}{T_2 - T_1}$ (linear interpolation).
- Lever rule on a horizontal tie line [Session 7 Slides 15-16]; microconstituents of a hypereutectic alloy: primary β and eutectic [Session 7 Slides 31-32]; precipitation of β when an alloy crosses the solvus [Session 8 Slides 3-4].

## (a) Diagram and invariant reaction [0.75 pts]

### Hint

Place the seven points first. Each melting point is the common top of a liquidus and a solidus; each end of the eutectic line is the common top of a solidus end and a solvus.

### Checkpoint

- Liquidus (0, 900)–(70, 550)–(100, 700); solidus (0, 900)–(20, 550) and (100, 700)–(92, 550); eutectic line (20, 550)–(92, 550); solvus (20, 550)–(5, 20) and (92, 550)–(97, 20).
- Regions: L; α + L; β + L; α; β; α + β.
- Cooling: L (70 wt% B) → α (20 wt% B) + β (92 wt% B) at 550 °C, eutectic.

### Solution

#### Draw the boundaries from the points

The liquidus is the line above which only liquid exists; in a eutectic system it falls from the melting point of each metal to the eutectic point, so it is made of the two segments (0, 900)–(70, 550) and (70, 550)–(100, 700). The solidus is the line below which there is no liquid; it falls from each melting point to the corresponding end of the eutectic line: (0, 900)–(20, 550) for α and (100, 700)–(92, 550) for β. The horizontal eutectic line joins (20, 550) and (92, 550). Below it, the solvus lines give the limit of solubility in each solid solution: (20, 550)–(5, 20) for α and (92, 550)–(97, 20) for β [Session 7 Slides 26-27].

#### Label the regions

Above the liquidus: L. Between the A-side liquidus and the α solidus: α + L. Between the B-side liquidus and the β solidus: β + L. Left of the α solidus and α solvus: α. Right of the β solidus and β solvus: β. Below the eutectic line, between the two solvus lines: α + β. Every two-phase field lies between two one-phase fields of the phases it contains, as it must in a binary diagram.

![[attachments/MAT-MT2/p06-ab-diagram.svg]]

#### Write the invariant reaction

At 550 °C a liquid of fixed composition gives two solids of fixed compositions; this is a eutectic reaction, and with three phases it has $F = 3 - P = 0$ degrees of freedom [Session 7 Slide 13]:

$$\text{cooling: } L\ (70\ \text{wt\% B}) \rightarrow \alpha\ (20\ \text{wt\% B}) + \beta\ (92\ \text{wt\% B}) \quad \text{at } 550\ ^\circ\text{C (eutectic)}$$

The diagram is thermodynamically sensible: both liquidus branches fall towards E, each solid solution is richest in solute at the eutectic temperature, and the eutectic composition lies between those of α and β.

## (b) Start of solidification and the tie line at 600 °C [0.75 pts]

### Hint

85 wt% B lies right of E, so the alloy meets the B-side liquidus. Interpolate on that line and on the β solidus.

### Checkpoint

- Liquidus temperature 625 °C; first solid β of 96 wt% B.
- At 600 °C: L of 80 wt% B and β of 94.7 wt% B; $W_L = 0.659$, $W_\beta = 0.341$.

### Solution

#### Liquidus temperature of the alloy

On the straight B-side liquidus from (70, 550) to (100, 700), the temperature rises by $(700 - 550)/(100 - 70) = 150/30 = 5$ °C per wt% B. Writing the line and putting $C = 85$:

$$T = 550 + 5\,(C - 70) = 550 + 5\,(85 - 70) = 550 + 75 = 625\ ^\circ\text{C}$$

#### Composition of the first solid

At 625 °C the first crystal is the solid in equilibrium with the liquid, at the other end of the tie line, on the β solidus from (92, 550) to (100, 700). On that line the composition grows by $(100 - 92)/(700 - 550) = 8/150$ wt% B per °C:

$$C_\beta = 92 + (T - 550)\,\frac{8}{150} = 92 + (625 - 550)\,\frac{8}{150} = 92 + 4.0 = 96.0\ \text{wt\% B}$$

The first solid (β of 96 wt% B) is richer in B than the alloy, as the tie line requires.

#### Ends of the tie line at 600 °C

At 600 °C the alloy (85, 600) lies between the liquidus and the β solidus: β + L. The liquid end is found by isolating $C$ in the liquidus equation:

$$600 = 550 + 5\,(C_L - 70) \quad\Rightarrow\quad C_L - 70 = \frac{600 - 550}{5} = 10 \quad\Rightarrow\quad C_L = 80\ \text{wt\% B}$$

$$C_\beta = 92 + (600 - 550)\,\frac{8}{150} = 92 + 2.667 = 94.67\ \text{wt\% B}$$

#### Derive the lever rule and apply it

With W the mass fractions of the two phases, the total mass balance and the mass balance of B are

$$W_L + W_\beta = 1$$

$$W_L C_L + W_\beta C_\beta = C_0$$

Putting $W_L = 1 - W_\beta$ into the second equation and expanding:

$$(1 - W_\beta)\,C_L + W_\beta C_\beta = C_0$$

$$C_L + W_\beta\,(C_\beta - C_L) = C_0$$

so

$$W_\beta = \frac{C_0 - C_L}{C_\beta - C_L} \qquad W_L = 1 - W_\beta = \frac{C_\beta - C_0}{C_\beta - C_L}$$

With a tie line of length $94.67 - 80 = 14.67$ wt% B [Session 7 Slide 16]:

$$W_\beta = \frac{85 - 80}{94.67 - 80} = \frac{5}{14.67} = 0.341$$

$$W_L = \frac{94.67 - 85}{94.67 - 80} = \frac{9.667}{14.67} = 0.659$$

Check of the B balance: $0.659 \times 80 + 0.341 \times 94.67 = 52.73 + 32.27 = 85.0$ wt% B.

## (c) Microconstituents just below 550 °C [0.75 pts]

### Hint

The β present just above 550 °C is the primary β; the remaining liquid has the eutectic composition. Below 550 °C the tie line spans the whole eutectic line.

### Checkpoint

- Primary β $W_{\beta'} = 0.682$; eutectic $W_E = 0.318$.
- Total phases: $W_\alpha = 0.0972$, $W_\beta = 0.903$.
- Inside the eutectic: α 0.0972 and β 0.221 of the alloy.

### Solution

#### Phases just above 550 °C

The tie line now runs from the eutectic liquid ($C_E = 70$) to the β end of the eutectic line ($C_\beta = 92$), length 22 wt% B:

$$W_{\beta}(550 + \Delta T) = \frac{C_0 - C_E}{C_\beta - C_E} = \frac{85 - 70}{92 - 70} = \frac{15}{22} = 0.682$$

$$W_{L}(550 + \Delta T) = \frac{92 - 85}{22} = \frac{7}{22} = 0.318$$

#### Microconstituents just below 550 °C

The alloy is hypereutectic ($70 < 85 < 92$), so its primary phase is β [Session 7 Slide 31]. The β formed above 550 °C remains as **primary β**, and the liquid of 70 wt% B turns entirely into the **eutectic** microconstituent [Session 7 Slide 32]:

$$W_{\beta'} = 0.682 \qquad W_E = 0.318$$

#### Total phases just below 550 °C

Now α + β, on the tie line from 20 to 92 wt% B (length 72):

$$W_\alpha = \frac{C_\beta - C_0}{C_\beta - C_\alpha} = \frac{92 - 85}{92 - 20} = \frac{7}{72} = 0.0972$$

$$W_\beta = \frac{C_0 - C_\alpha}{C_\beta - C_\alpha} = \frac{85 - 20}{72} = \frac{65}{72} = 0.903$$

#### Phases inside the eutectic

The primary constituent is β, so every bit of α is in the eutectic: $W_{\alpha,E} = W_\alpha = 0.0972$. The β of the eutectic is the total β minus the primary β, with four figures:

$$W_{\beta,E} = W_\beta - W_{\beta'} = 0.9028 - 0.6818 = 0.221$$

Check with the make-up of the eutectic, which is $(92 - 70)/72 = 0.3056$ α: $0.3182 \times 0.3056 = 0.0972$ α, and $0.0972 + 0.221 = 0.318 = W_E$.

## (d) Alloys with eutectic, and the 12 wt% B alloy [0.75 pts]

### Hint

Eutectic can only form from liquid that reaches E. For 12 wt% B, find where the alloy line meets the α solvus, then use the tie line at 20 °C.

### Checkpoint

- Eutectic at room temperature for $20 < C_0 < 92$ wt% B.
- The 12 wt% B alloy crosses the α solvus at 267.3 °C; at 20 °C it holds $W_\beta = 0.0761$ of precipitated β.

### Solution

#### Range of alloys with eutectic

An alloy contains eutectic only if some of its liquid reaches the eutectic point at 550 °C, that is, if its vertical line crosses the eutectic line. The line runs from 20 to 92 wt% B, so the alloys with eutectic are those with $20 < C_0 < 92$ wt% B. An alloy of 12 wt% B solidifies completely as α before reaching 550 °C (it crosses the α solidus), so it has no eutectic.

#### Temperature at which β appears

Below its solidus the 12 wt% B alloy is single-phase α, until its vertical line meets the α solvus, the straight line from (20, 550) to (5, 20). Writing that line as temperature against composition and putting $C = 12$:

$$T = 20 + (C - 5)\,\frac{550 - 20}{20 - 5} = 20 + (12 - 5)\,\frac{530}{15} = 20 + 7 \times 35.33 = 267.3\ ^\circ\text{C}$$

Below 267.3 °C α cannot hold all its B, and β precipitates as fine particles inside the α grains and on their boundaries [Session 8 Slides 3-4].

#### Amount of β at 20 °C

At 20 °C the tie line runs from the α solvus (5 wt% B) to the β solvus (97 wt% B), length 92:

$$W_\beta = \frac{C_0 - C_\alpha}{C_\beta - C_\alpha} = \frac{12 - 5}{97 - 5} = \frac{7}{92} = 0.0761$$

$$W_\alpha = \frac{97 - 12}{92} = \frac{85}{92} = 0.924$$

All this β (7.61 % of the alloy) is precipitated β; none of it is eutectic.

## Interpretation

The description fixes the diagram completely once straight lines are assumed: seven points, six boundaries and six regions. The 85 wt% B alloy starts to solidify at 625 °C with β of 96 wt% B, is two-thirds primary β at 550 °C, and the last 31.8 % of liquid becomes a eutectic that holds all the α of the alloy (9.72 %). The 12 wt% B alloy shows that a two-phase structure does not need a eutectic: it appears by precipitation when the solvus is crossed at 267.3 °C.

Control cases: for $C_0 \to 70$ the primary β $W_{\beta'} = (C_0 - 70)/22 \to 0$ and the alloy is all eutectic; for $C_0 \to 92$, $W_{\beta'} \to 1$. For $C_0 \to 5$ the solvus temperature tends to 20 °C, and for $C_0 \to 20$ to 550 °C. Dimensional check: interpolation slopes are in °C per wt% B (5 °C/wt%, 530/15 = 35.33 °C/wt%) or wt% B per °C (8/150), so every interpolated temperature is in °C and every composition in wt% B; the fractions are ratios of compositions and are dimensionless.

Common exam mistake: writing the β end of the eutectic line at 8 wt% B instead of 92 wt% B; the statement gives the solubility of A in β, and the axis is wt% B.

## Verification

- liquidus temperature of 85 B (C) | 550+(700-550)/(100-70)*(85-70) | 625
- first solid (wt% B) | 92+(625-550)*(100-92)/(700-550) | 96.0
- C_L at 600 C (wt% B) | 70+(600-550)/((700-550)/(100-70)) | 80
- C_beta at 600 C (wt% B) | 92+(600-550)*(100-92)/(700-550) | 94.67
- W_beta at 600 C | (85-80)/(92+50*8/150-80) | 0.341
- W_L at 600 C | (92+50*8/150-85)/(92+50*8/150-80) | 0.659
- primary beta | (85-70)/(92-70) | 0.682
- eutectic | (92-85)/(92-70) | 0.318
- W_alpha at 550-dT | (92-85)/(92-20) | 0.0972
- W_beta at 550-dT | (85-20)/(92-20) | 0.903
- beta inside the eutectic | (85-20)/(92-20)-(85-70)/(92-70) | 0.221
- make-up of the eutectic (alpha) | (92-70)/(92-20) | 0.3056
- solvus temperature of 12 B (C) | 20+(12-5)*(550-20)/(20-5) | 267.3
- W_beta at 20 C, 12 B | (12-5)/(97-5) | 0.0761
- W_alpha at 20 C, 12 B | (97-12)/(97-5) | 0.924

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
