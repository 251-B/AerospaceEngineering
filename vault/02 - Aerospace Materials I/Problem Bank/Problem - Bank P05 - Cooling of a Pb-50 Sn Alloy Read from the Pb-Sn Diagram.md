---
materia: Aerospace Materials I
tema: "Unit 4: phase diagrams"
bank_id: P05
title: "Cooling of a Pb-50 wt% Sn alloy read from the Pb-Sn diagram"
category: mt2_problem
archetype: eutectic-lever-rule
level: standard
unit: 4
difficulty: 2
points: 3.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of Problems T4_PhaseDiagrams I.pdf (Problems 3 and 4) and of question 7 of the test, with the Pb-Sn values of Session 7 Slide 32 and a new alloy (50 wt% Sn) and new temperatures (200 and 100 °C); not an official exercise. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - eutectic-lever-rule
  - pb-sn
  - hypoeutectic
  - solvus
---

# Bank P05 — Cooling of a Pb-50 wt% Sn alloy read from the Pb-Sn diagram

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Pb-Sn problems of Problems T4_PhaseDiagrams I.pdf, with the values of Session 7 Slide 32. Method: tie line and lever rule [Session 7 Slides 15-16], eutectic microconstituents [Session 7 Slides 30, 32], precipitation below the solvus [Session 8 Slides 3-4]. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

The figure shows the Pb-Sn phase diagram with the values of Session 7 Slide 32. A Pb-50 wt% Sn alloy is cooled slowly (equilibrium) from 300 °C to 100 °C. The readings needed are printed on the figure: the alloy meets the liquidus at 215 °C; at 200 °C the tie line through the alloy ends at 16.7 and 55.7 wt% Sn; at 100 °C it ends at 4.8 and 99.8 wt% Sn.

![[attachments/MAT-MT2/p05-pbsn-alloy50.svg]]

(a) Write the invariant reaction of the diagram (name, temperature, compositions of the three phases). Classify the alloy and say at which temperatures its solidification starts and ends, and which phase forms first.

(b) At 200 °C, give the phases present, their compositions and their mass fractions.

(c) Just above (183 + ΔT) and just below (183 − ΔT) the eutectic temperature, give the phases with their compositions and mass fractions, and the microconstituents with their mass fractions. What fraction of all the α of the alloy is inside the eutectic?

(d) At 100 °C, give the phases, their compositions and mass fractions. Explain where the extra β comes from.

## Setup

#### Data

| Quantity | Symbol | Value | Where it is read |
| :--- | :--- | :--- | :--- |
| Alloy composition | $C_0$ | 50 wt% Sn (mass fraction 0.50 of Sn) | statement |
| Melting points | $T_{Pb}$, $T_{Sn}$ | 327 °C, 232 °C | ends of the liquidus |
| Eutectic point | $T_E$, $C_E$ | 183 °C, 61.9 wt% Sn | point E |
| Ends of the eutectic line | $C_\alpha$, $C_\beta$ | 18.3 and 97.8 wt% Sn | ends of the horizontal line at 183 °C |
| Liquidus of the alloy | $T_L$ | 215 °C | the dashed alloy line meets the liquidus |
| Tie line at 200 °C | $C_\alpha$, $C_L$ | 16.7 and 55.7 wt% Sn | solidus and liquidus at 200 °C |
| Tie line at 100 °C | $C_\alpha$, $C_\beta$ | 4.8 and 99.8 wt% Sn | the two solvus lines at 100 °C |

The compositions are mass percentages; the lever rule only uses differences and ratios of them, so they can stay in wt% (the conversion to mass fractions, dividing by 100, cancels in every ratio).

#### Model

- Gibbs phase rule at constant pressure for two components, $F = C - P + 1 = 3 - P$ [Session 7 Slide 13]: in a two-phase field $F = 1$, so once the temperature is fixed the compositions of both phases are fixed; they are the ends of the horizontal tie line [Session 7 Slide 15].
- Lever rule [Session 7 Slides 15-16]: on a tie line from $C_1$ to $C_2$, $W_1 = \dfrac{C_2 - C_0}{C_2 - C_1}$ and $W_2 = \dfrac{C_0 - C_1}{C_2 - C_1}$ (derived in part (b)).
- Microconstituents of a hypoeutectic alloy [Session 7 Slides 30, 32]: the α present just above 183 °C is the primary α; the liquid present then (of 61.9 wt% Sn) becomes the eutectic. Hypotheses: equilibrium cooling, closed system (no loss of mass).

## (a) Invariant reaction, type of alloy and start and end of solidification [0.75 pts]

### Hint

Look for the point where the liquidus has its minimum and the horizontal line that passes through it. Compare $C_0$ with the three compositions of that line.

### Checkpoint

- Eutectic at 183 °C: L (61.9 wt% Sn) → α (18.3 wt% Sn) + β (97.8 wt% Sn) on cooling.
- $18.3 < 50 < 61.9$: hypoeutectic alloy; the primary phase is α.
- Solidification starts at 215 °C (first solid α) and ends at 183 °C.

### Solution

#### Identify the invariant reaction at point E

The only horizontal line of the diagram is at 183 °C. It touches three phase fields from above and below: the liquid meets it at a single point E (the minimum of the liquidus), α ends at its left end and β at its right end. A liquid that turns into two solids at a fixed temperature and composition is a eutectic reaction [Session 7 Slides 26-27]. Reading the three compositions on the line:

$$\text{cooling: } L\ (61.9\ \text{wt\% Sn}) \rightarrow \alpha\ (18.3\ \text{wt\% Sn}) + \beta\ (97.8\ \text{wt\% Sn}) \quad \text{at } 183\ ^\circ\text{C (eutectic)}$$

It is invariant: with three phases, $F = 3 - P = 3 - 3 = 0$, so neither the temperature nor any composition can change while the reaction proceeds [Session 7 Slide 13].

#### Classify the alloy

The eutectic line runs from 18.3 to 97.8 wt% Sn, and the eutectic point is at 61.9 wt% Sn. An alloy between the α end and E is hypoeutectic, and its primary (proeutectic) phase is α [Session 7 Slide 30]:

$$C_\alpha = 18.3 < C_0 = 50 < C_E = 61.9 \quad\Rightarrow\quad \text{hypoeutectic alloy, primary phase } \alpha$$

#### Read the start and the end of solidification

Following the dashed vertical line $C_0 = 50$ from above: it stays in L down to the liquidus, which it meets at **215 °C** (printed on the figure). Below that the alloy is in the α + L field, so the first solid is α, the phase on the left boundary of that field. The liquid keeps changing its composition along the liquidus until it reaches E; the last liquid, of 61.9 wt% Sn, solidifies as eutectic at **183 °C**, where solidification ends. Solidification therefore takes place over the interval $215 - 183 = 32$ °C.

## (b) Phases, compositions and amounts at 200 °C [0.75 pts]

### Hint

200 °C lies between 215 and 183 °C on the alloy line. Draw the tie line, read its ends, and write two mass balances.

### Checkpoint

- Phases: α (16.7 wt% Sn) and L (55.7 wt% Sn).
- $W_L = 0.854$, $W_\alpha = 0.146$.

### Solution

#### Place the point and read the tie line

At 200 °C the alloy point (50, 200) is in the α + L field. The horizontal tie line through it meets the α solidus at $C_\alpha = 16.7$ wt% Sn and the liquidus at $C_L = 55.7$ wt% Sn (printed on the figure). These are the compositions of the two phases [Session 7 Slide 15].

#### Derive the lever rule from two mass balances

Take a mass of alloy as the unit. The alloy is made only of α and L, so their mass fractions add up to one (total mass balance); the tin in the alloy is the tin in α plus the tin in L (mass balance of Sn):

$$W_\alpha + W_L = 1$$

$$W_\alpha C_\alpha + W_L C_L = C_0$$

From the first equation, $W_\alpha = 1 - W_L$. Substituting into the second:

$$(1 - W_L)\,C_\alpha + W_L C_L = C_0$$

$$C_\alpha + W_L\,(C_L - C_\alpha) = C_0$$

$$W_L = \frac{C_0 - C_\alpha}{C_L - C_\alpha}$$

and then $W_\alpha = 1 - W_L = \dfrac{C_L - C_\alpha - C_0 + C_\alpha}{C_L - C_\alpha} = \dfrac{C_L - C_0}{C_L - C_\alpha}$. Each phase is given by the arm of the lever on the side of the **other** phase, divided by the length of the tie line [Session 7 Slide 16].

#### Substitute the readings at 200 °C

The tie line has length $C_L - C_\alpha = 55.7 - 16.7 = 39.0$ wt% Sn:

$$W_L = \frac{50 - 16.7}{55.7 - 16.7} = \frac{33.3}{39.0} = 0.854$$

$$W_\alpha = \frac{55.7 - 50}{55.7 - 16.7} = \frac{5.7}{39.0} = 0.146$$

Check: $0.854 + 0.146 = 1.000$, and the Sn balance $0.1462 \times 16.7 + 0.8538 \times 55.7 = 2.44 + 47.56 = 50.0$ wt% Sn returns $C_0$. The alloy is still mostly liquid, because 200 °C is only 15 °C below its liquidus.

## (c) Phases and microconstituents at 183 ± ΔT °C [0.75 pts]

### Hint

Above 183 °C use the tie line from α to the eutectic liquid; below it, the full eutectic line from α to β. The liquid of 61.9 wt% Sn present just above becomes the eutectic just below.

### Checkpoint

- 183 + ΔT: α (18.3) and L (61.9 wt% Sn); $W_\alpha = 0.273$, $W_L = 0.727$.
- 183 − ΔT: α (18.3) and β (97.8 wt% Sn); $W_\alpha = 0.601$, $W_\beta = 0.399$.
- Microconstituents: primary α $W_{\alpha'} = 0.273$, eutectic $W_E = 0.727$; α inside the eutectic 0.328 of the alloy; 54.6 % of all the α is eutectic α.

### Solution

#### Lever rule just above 183 °C

At 183 + ΔT the alloy is still in α + L; the tie line ends at the two ends of the left part of the eutectic line, $C_\alpha = 18.3$ and $C_L = C_E = 61.9$ wt% Sn (length $61.9 - 18.3 = 43.6$). With the lever rule of part (b):

$$W_L = \frac{C_0 - C_\alpha}{C_E - C_\alpha} = \frac{50 - 18.3}{61.9 - 18.3} = \frac{31.7}{43.6} = 0.727$$

$$W_\alpha = \frac{C_E - C_0}{C_E - C_\alpha} = \frac{61.9 - 50}{43.6} = \frac{11.9}{43.6} = 0.273$$

#### Lever rule just below 183 °C (total phases)

At 183 − ΔT the eutectic reaction has consumed all the liquid and the alloy is in α + β. The tie line is the whole eutectic line, from $C_\alpha = 18.3$ to $C_\beta = 97.8$ wt% Sn (length $97.8 - 18.3 = 79.5$) [Session 7 Slide 32]:

$$W_\alpha = \frac{C_\beta - C_0}{C_\beta - C_\alpha} = \frac{97.8 - 50}{79.5} = \frac{47.8}{79.5} = 0.601$$

$$W_\beta = \frac{C_0 - C_\alpha}{C_\beta - C_\alpha} = \frac{50 - 18.3}{79.5} = \frac{31.7}{79.5} = 0.399$$

#### Microconstituents just below 183 °C

The α that existed at 183 + ΔT does not take part in the reaction: it stays as **primary α**. The liquid, which has exactly the eutectic composition, becomes the **eutectic** microconstituent (alternating α and β) [Session 7 Slides 30, 32]. Therefore the microconstituent fractions are the phase fractions just above the eutectic temperature:

$$W_{\alpha'} = W_\alpha(183 + \Delta T) = 0.273 \qquad W_E = W_L(183 + \Delta T) = 0.727$$

#### Split the α between primary and eutectic

All the β is inside the eutectic (the primary phase is α). The α inside the eutectic is the total α minus the primary α; with four significant figures, $W_\alpha = 47.8/79.5 = 0.6013$ and $W_{\alpha'} = 11.9/43.6 = 0.2729$:

$$W_{\alpha,E} = W_\alpha - W_{\alpha'} = 0.6013 - 0.2729 = 0.328$$

$$\frac{W_{\alpha,E}}{W_\alpha} = \frac{0.3283}{0.6013} = 0.546$$

So **54.6 %** of all the α of the alloy is eutectic α. Check: the eutectic is $W_{\alpha,E} + W_{\beta,E} = 0.328 + 0.399 = 0.727 = W_E$, and its own make-up is $(97.8 - 61.9)/79.5 = 0.452$ α, so $0.727 \times 0.452 = 0.328$ (checked).

## (d) Phases at 100 °C and precipitation of β [0.75 pts]

### Hint

Below 183 °C the ends of the tie line move along the two solvus lines. Compare the β fraction at 100 °C with the one just below 183 °C.

### Checkpoint

- α (4.8 wt% Sn) and β (99.8 wt% Sn); $W_\alpha = 0.524$, $W_\beta = 0.476$.
- β grows by 0.077 of the alloy between 183 − ΔT and 100 °C: it precipitates from the α, whose Sn solubility falls from 18.3 to 4.8 wt%.

### Solution

#### Lever rule at 100 °C

The alloy is still in α + β; the tie line now ends on the α solvus at 4.8 and on the β solvus at 99.8 wt% Sn (length $99.8 - 4.8 = 95.0$):

$$W_\alpha = \frac{99.8 - 50}{99.8 - 4.8} = \frac{49.8}{95.0} = 0.524$$

$$W_\beta = \frac{50 - 4.8}{99.8 - 4.8} = \frac{45.2}{95.0} = 0.476$$

#### Explain the change with the solvus

The α solvus slopes to the left: the solubility of Sn in α falls from 18.3 wt% at 183 °C to 4.8 wt% at 100 °C. The α of the alloy (primary and eutectic) is therefore supersaturated as it cools and rejects the excess Sn as small particles of β inside its grains: this is precipitation in the solid state, which grows as the temperature decreases [Session 8 Slides 3-4]. The amount of β gained is

$$\Delta W_\beta = W_\beta(100\ ^\circ\text{C}) - W_\beta(183 - \Delta T) = 0.4758 - 0.3987 = 0.077$$

that is, 7.7 % of the mass of the alloy. The β side changes little (97.8 → 99.8 wt% Sn), so almost all the change comes from the α side. The microconstituents keep their names: primary α (now with fine β precipitates) and eutectic.

## Interpretation

On cooling, the Pb-50 Sn alloy starts to solidify at 215 °C with α, holds 14.6 % α at 200 °C and 27.3 % just above 183 °C; the remaining 72.7 % of liquid, now of eutectic composition, solidifies at 183 °C as eutectic. Because 50 wt% Sn is close to E (61.9), the eutectic dominates the microstructure, and more than half of the α (54.6 %) is eutectic α.

Control cases: as $C_0 \to 18.3$ the eutectic fraction $W_E = (C_0 - 18.3)/43.6 \to 0$ (all primary α), and as $C_0 \to 61.9$, $W_E \to 1$ (fully eutectic). All fractions lie between 0 and 1, and each pair adds up to 1. Dimensional check: the lever rule is a ratio of two composition differences, (wt% Sn)/(wt% Sn), so the fractions are dimensionless, as they must be.

Common exam mistake: taking the primary α from the long tie line below 183 °C (0.601). That number is the total α (primary plus eutectic); the primary α must be read on the short tie line just above 183 °C, which ends at the eutectic liquid.

## Verification

- W_L at 200 C | (50-16.7)/(55.7-16.7) | 0.854
- W_alpha at 200 C | (55.7-50)/(55.7-16.7) | 0.146
- W_L at 183+dT | (50-18.3)/(61.9-18.3) | 0.727
- W_alpha at 183+dT | (61.9-50)/(61.9-18.3) | 0.273
- W_alpha at 183-dT | (97.8-50)/(97.8-18.3) | 0.601
- W_beta at 183-dT | (50-18.3)/(97.8-18.3) | 0.399
- alpha inside the eutectic | (97.8-50)/(97.8-18.3)-(61.9-50)/(61.9-18.3) | 0.328
- share of the alpha that is eutectic | ((97.8-50)/(97.8-18.3)-(61.9-50)/(61.9-18.3))/((97.8-50)/(97.8-18.3)) | 0.546
- make-up of the eutectic (alpha) | (97.8-61.9)/(97.8-18.3) | 0.452
- W_alpha at 100 C | (99.8-50)/(99.8-4.8) | 0.524
- W_beta at 100 C | (50-4.8)/(99.8-4.8) | 0.476
- beta precipitated | (50-4.8)/(99.8-4.8)-(50-18.3)/(97.8-18.3) | 0.077
- freezing range (C) | 215-183 | 32

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
