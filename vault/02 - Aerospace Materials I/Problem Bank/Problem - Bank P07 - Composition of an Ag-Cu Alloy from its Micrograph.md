---
materia: Aerospace Materials I
tema: "Unit 4: phase diagrams"
bank_id: P07
title: "Composition of an Ag-Cu alloy worked backwards from its micrograph"
category: mt2_problem
archetype: eutectic-lever-rule
level: trap
unit: 4
difficulty: 3
points: 3.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of Problem 2 of Problems T4_PhaseDiagrams I.pdf and of the 2016 and 2017 extraordinary finals (composition worked backwards from a microstructure), with the Ag-Cu values of the problem sheet (p. 2); not an official exercise. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - eutectic-lever-rule
  - ag-cu
  - microconstituents
  - working-backwards
---

# Bank P07 — Composition of an Ag-Cu alloy worked backwards from its micrograph

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the problems that deduce a composition from a microstructure (Problem 2 of the Unit 4 sheet; the 2016 and 2017 extraordinary finals), with the Ag-Cu values printed on the diagram of Problems T4_PhaseDiagrams I.pdf, p. 2. Method: lever rule [Session 7 Slides 15-16] and microconstituents of hypo- and hypereutectic alloys [Session 7 Slides 30-32]. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

A casting of 3.0 kg of an Ag-Cu alloy of unknown composition was cooled slowly. Its micrograph (sketch below) shows rounded, dendritic grains of a primary constituent in a fine lamellar matrix. Image analysis gives 55 % of the section as lamellar matrix and 45 % as primary grains; take these area fractions as mass fractions. Microanalysis shows that the primary grains are the Cu-rich solid solution (Cu).

The Ag-Cu diagram of the problem sheet has a single eutectic at 779.1 °C, where the liquid contains 28.1 wt% Cu; at that temperature the Ag-rich solid solution (Ag) holds 8.8 wt% Cu and the Cu-rich solid solution (Cu) holds 92 wt% Cu.

![[attachments/MAT-MT2/p07-agcu-micrograph.svg]]

(a) Show that the eutectic fraction alone allows two compositions of the alloy, compute both, and use the micrograph to choose the right one.

(b) Just below 779.1 °C, give the phases with their compositions and mass fractions, and the mass fraction of each phase inside the eutectic.

(c) For the 3.0 kg casting, give the mass in kg of every microconstituent and of every phase just below 779.1 °C, and the mass and composition of the liquid just above 779.1 °C. How many kg of Cu does that liquid hold?

(d) The supplier's certificate states Ag-50 wt% Cu. What eutectic fraction would that alloy show? Is the certificate consistent with the micrograph?

## Setup

#### Data

| Quantity | Symbol | Value |
| :--- | :--- | :--- |
| Eutectic temperature | $T_E$ | 779.1 °C |
| Eutectic liquid | $C_E$ | 28.1 wt% Cu |
| (Ag) at $T_E$ | $C_\alpha$ | 8.8 wt% Cu |
| (Cu) at $T_E$ | $C_\beta$ | 92 wt% Cu |
| Eutectic fraction (lamellar matrix) | $W_E$ | 0.55 |
| Primary fraction (grains) | $W_{\beta'}$ | 0.45, identified as (Cu) |
| Mass of the casting | $m$ | 3.0 kg |
| Certificate | $C_{cert}$ | 50 wt% Cu |

In what follows α is (Ag) and β is (Cu). Compositions are mass percentages of Cu; in a ratio of composition differences the factor 1/100 that turns them into mass fractions cancels, but in a mass of Cu it does not: 28.1 wt% is a mass fraction of 0.281.

#### Model

- Lever rule on a horizontal tie line [Session 7 Slides 15-16], derived in part (a) from the two mass balances.
- Microconstituents [Session 7 Slides 30-32]: just below $T_E$ the primary phase is the solid present just above $T_E$, and the eutectic is the liquid of composition $C_E$ present just above $T_E$. A hypoeutectic alloy ($C_\alpha < C_0 < C_E$) has primary α; a hypereutectic one ($C_E < C_0 < C_\beta$) has primary β.
- Hypotheses: equilibrium cooling; area fraction equal to mass fraction (as the statement imposes); closed system.

## (a) Two candidate compositions and the choice [0.75 pts]

### Hint

Write the eutectic fraction with the lever rule twice: once on the tie line α–E (hypoeutectic) and once on E–β (hypereutectic). Then solve each for $C_0$.

### Checkpoint

- Hypoeutectic candidate: $C_0 = 19.4$ wt% Cu (primary would be (Ag)).
- Hypereutectic candidate: $C_0 = 56.86$ wt% Cu (primary would be (Cu)).
- The primary grains are (Cu): the alloy is Ag-56.86 wt% Cu.

### Solution

#### Derive the lever rule for the eutectic fraction

Just above $T_E$ the alloy holds a primary solid and liquid of composition $C_E$; that liquid becomes the eutectic, so $W_E = W_L(T_E + \Delta T)$. For a tie line from a solid of composition $C_s$ to the liquid $C_E$, the total mass balance and the Cu balance are

$$W_s + W_L = 1$$

$$W_s C_s + W_L C_E = C_0$$

Putting $W_s = 1 - W_L$ in the second equation and expanding:

$$(1 - W_L)\,C_s + W_L C_E = C_0$$

$$C_s + W_L\,(C_E - C_s) = C_0$$

hence

$$W_E = W_L = \frac{C_0 - C_s}{C_E - C_s}$$

#### Hypoeutectic candidate (solid α, $C_s = 8.8$)

$$0.55 = \frac{C_0 - 8.8}{28.1 - 8.8} = \frac{C_0 - 8.8}{19.3}$$

$$C_0 - 8.8 = 0.55 \times 19.3 = 10.615 \quad\Rightarrow\quad C_0 = 8.8 + 10.615 = 19.4\ \text{wt\% Cu}$$

#### Hypereutectic candidate (solid β, $C_s = 92$)

With $C_s = 92$ the same formula reads $W_E = (C_0 - 92)/(28.1 - 92) = (92 - C_0)/(92 - 28.1)$:

$$0.55 = \frac{92 - C_0}{92 - 28.1} = \frac{92 - C_0}{63.9}$$

$$92 - C_0 = 0.55 \times 63.9 = 35.145 \quad\Rightarrow\quad C_0 = 92 - 35.145 = 56.86\ \text{wt\% Cu}$$

#### Choose with the primary constituent

The eutectic fraction is the same function of $C_0$ on both sides of E, rising from 0 at an end of the eutectic line to 1 at E, so one value of $W_E$ always corresponds to two alloys. The primary constituent tells them apart: a hypoeutectic Ag-Cu alloy would show primary (Ag), a hypereutectic one primary (Cu) [Session 7 Slides 30-31]. The microanalysis finds (Cu) grains, so

$$C_0 = 56.86\ \text{wt\% Cu} \qquad (28.1 < 56.86 < 92\text{, hypereutectic})$$

## (b) Phases just below 779.1 °C and the make-up of the eutectic [0.75 pts]

### Hint

The tie line now spans the whole eutectic line, from 8.8 to 92 wt% Cu. The primary constituent is β, so all the α is in the eutectic.

### Checkpoint

- α (8.8 wt% Cu) $W_\alpha = 0.422$; β (92 wt% Cu) $W_\beta = 0.578$.
- Inside the eutectic: α 0.422 and β 0.128 of the alloy; the eutectic itself is 76.8 % α.

### Solution

#### Total phases with the lever rule

Below $T_E$ the liquid has gone and the alloy is α + β. With the lever rule of part (a) on the tie line from $C_\alpha = 8.8$ to $C_\beta = 92$ (length 83.2), carrying $C_0 = 56.855$:

$$W_\alpha = \frac{C_\beta - C_0}{C_\beta - C_\alpha} = \frac{92 - 56.855}{92 - 8.8} = \frac{35.145}{83.2} = 0.422$$

$$W_\beta = \frac{C_0 - C_\alpha}{C_\beta - C_\alpha} = \frac{56.855 - 8.8}{83.2} = \frac{48.055}{83.2} = 0.578$$

#### Split the β between primary and eutectic

The primary β is 0.45 of the alloy (data). The rest of the β, and all of the α, are inside the eutectic:

$$W_{\beta,E} = W_\beta - W_{\beta'} = 0.5776 - 0.45 = 0.128$$

$$W_{\alpha,E} = W_\alpha = 0.422$$

Check: $W_{\alpha,E} + W_{\beta,E} = 0.422 + 0.128 = 0.550 = W_E$.

#### Make-up of the eutectic

The eutectic is the liquid of 28.1 wt% Cu split on the tie line 8.8–92; its α fraction is

$$\frac{C_\beta - C_E}{C_\beta - C_\alpha} = \frac{92 - 28.1}{83.2} = \frac{63.9}{83.2} = 0.768$$

so the eutectic is 76.8 % α and 23.2 % β whatever the alloy, and $0.55 \times 0.768 = 0.422$ reproduces $W_{\alpha,E}$. The lamellar matrix is mostly the Ag-rich phase.

## (c) Masses in the 3.0 kg casting [0.75 pts]

### Hint

Multiply each fraction by 3.0 kg. For the Cu in the liquid, turn 28.1 wt% into a mass fraction first.

### Checkpoint

- Primary β 1.35 kg, eutectic 1.65 kg; α 1.267 kg, β 1.733 kg (of which 0.383 kg in the eutectic).
- Just above 779.1 °C: 1.65 kg of liquid of 28.1 wt% Cu, holding 0.464 kg of Cu.

### Solution

#### Microconstituents and phases just below 779.1 °C

The mass of each constituent is its mass fraction times the mass of the casting, $m_i = W_i\,m$:

$$m_{\beta'} = 0.45 \times 3.0\ \text{kg} = 1.35\ \text{kg} \qquad m_E = 0.55 \times 3.0\ \text{kg} = 1.65\ \text{kg}$$

$$m_\alpha = 0.4224 \times 3.0\ \text{kg} = 1.267\ \text{kg} \qquad m_\beta = 0.5776 \times 3.0\ \text{kg} = 1.733\ \text{kg}$$

$$m_{\beta,E} = 0.1276 \times 3.0\ \text{kg} = 0.383\ \text{kg}$$

Check: $1.35 + 1.65 = 3.00$ kg and $1.267 + 1.733 = 3.000$ kg.

#### The liquid just above 779.1 °C

Just above $T_E$ the alloy is β + L; the liquid has the eutectic composition, 28.1 wt% Cu, and its mass is the future eutectic, 1.65 kg. Converting the composition to a mass fraction, $28.1\ \text{wt\%} \rightarrow 0.281$:

$$m_{Cu,L} = 0.281 \times 1.65\ \text{kg} = 0.464\ \text{kg}$$

#### Cu balance of the casting

The Cu of the primary β is $0.92 \times 1.35\ \text{kg} = 1.242$ kg, so the casting holds $1.242 + 0.464 = 1.706$ kg of Cu, which is $1.706/3.0 = 0.5686$ of its mass: 56.86 wt% Cu, the composition found in part (a).

## (d) Checking the certificate [0.75 pts]

### Hint

Apply the eutectic-fraction formula of part (a) on the hypereutectic side to $C_0 = 50$ and compare with 0.55.

### Checkpoint

- Ag-50 wt% Cu would show $W_E = 0.657$ eutectic and 0.343 primary (Cu).
- Measured 0.55: the certificate overstates the Ag content of the alloy (or understates its Cu); the micrograph points to 56.86 wt% Cu.

### Solution

#### Eutectic fraction of the certified alloy

Ag-50 wt% Cu is also hypereutectic ($28.1 < 50 < 92$), so its eutectic is

$$W_E(50) = \frac{92 - 50}{92 - 28.1} = \frac{42}{63.9} = 0.657$$

and its primary (Cu) is $1 - 0.657 = 0.343$.

#### Compare with the measurement

The micrograph shows 0.55 eutectic, not 0.657: about 11 points less eutectic and therefore more primary (Cu) than the certified alloy would have. Because $W_E$ falls as $C_0$ moves from E towards β, less eutectic means more Cu: the measurement corresponds to 56.86 wt% Cu, not 50. Within the hypotheses of the problem (equilibrium cooling, area fraction equal to mass fraction), the certificate is not consistent with the micrograph. The two alloys would also differ in their total phase fractions: α would be $42/83.2 = 0.505$ for the certified alloy, against 0.422 for the alloy of the micrograph.

## Interpretation

A eutectic fraction alone never fixes the composition: it gives one hypoeutectic and one hypereutectic alloy, here 19.4 and 56.86 wt% Cu, and the nature of the primary grains decides between them. The alloy is hypereutectic: 45 % primary (Cu) dendrites in a matrix that, although it is 55 % of the alloy, is three-quarters Ag-rich α.

Control cases: with $W_E \to 1$ both candidates tend to $C_E = 28.1$ (fully eutectic), and with $W_E \to 0$ they tend to the ends of the eutectic line, 8.8 and 92 wt% Cu. All fractions lie between 0 and 1 and the masses add up to 3.0 kg. Dimensional check: the lever rule is a ratio of composition differences, (wt% Cu)/(wt% Cu), so it is dimensionless; a mass is a dimensionless fraction times kg, so it is in kg; and a mass of Cu needs the composition as a fraction (0.281), not as 28.1.

Common exam mistake (the trap of this problem): solving only on the side of the eutectic point one is used to (the hypoeutectic one) and answering 19.4 wt% Cu, an alloy that would show primary (Ag), not the (Cu) grains of the micrograph.

## Verification

- hypoeutectic candidate (wt% Cu) | 8.8+0.55*(28.1-8.8) | 19.4
- hypereutectic candidate (wt% Cu) | 92-0.55*(92-28.1) | 56.86
- W_alpha below T_E | (92-(92-0.55*63.9))/(92-8.8) | 0.422
- W_beta below T_E | ((92-0.55*63.9)-8.8)/(92-8.8) | 0.578
- beta inside the eutectic | ((92-0.55*63.9)-8.8)/(92-8.8)-0.45 | 0.128
- make-up of the eutectic (alpha) | (92-28.1)/(92-8.8) | 0.768
- primary beta (kg) | 0.45*3.0 | 1.35
- eutectic (kg) | 0.55*3.0 | 1.65
- alpha (kg) | 3.0*(92-(92-0.55*63.9))/(92-8.8) | 1.267
- beta (kg) | 3.0*((92-0.55*63.9)-8.8)/(92-8.8) | 1.733
- eutectic beta (kg) | 3.0*(((92-0.55*63.9)-8.8)/(92-8.8)-0.45) | 0.383
- Cu in the liquid (kg) | 0.281*0.55*3.0 | 0.464
- Cu in the primary beta (kg) | 0.92*0.45*3.0 | 1.242
- Cu in the casting (kg) | 0.92*0.45*3.0+0.281*0.55*3.0 | 1.706
- eutectic of Ag-50 Cu | (92-50)/(92-28.1) | 0.657
- primary beta of Ag-50 Cu | 1-(92-50)/(92-28.1) | 0.343
- W_alpha of Ag-50 Cu | (92-50)/(92-8.8) | 0.505

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
