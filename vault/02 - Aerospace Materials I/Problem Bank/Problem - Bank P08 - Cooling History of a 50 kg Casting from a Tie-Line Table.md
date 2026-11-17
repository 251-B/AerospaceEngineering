---
materia: Aerospace Materials I
tema: "Unit 4: phase diagrams"
bank_id: P08
title: "Cooling history of a 50 kg casting from a table of tie-line compositions"
category: mt2_problem
archetype: eutectic-lever-rule
level: standard
unit: 4
difficulty: 2
points: 3.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of Slide 23 of Session 7 (compositions of the liquid and the solid tabulated along the cooling) and of the finals that ask for kg of each constituent (2016 and 2017 extraordinary), with a hypothetical eutectic system given only as a table; not an official exercise. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - eutectic-lever-rule
  - cooling-history
  - solvus
  - mass-of-phases
---

# Bank P08 — Cooling history of a 50 kg casting from a table of tie-line compositions

> [!info] Practice item, not an official exercise
> Written for the bank in the style of Session 7 Slide 23, where the compositions of the liquid and the solid are tabulated along the cooling of one alloy, and of the finals that ask for kilograms of each constituent. Method: tie line and lever rule [Session 7 Slides 15-16], eutectic microconstituents [Session 7 Slides 30, 32], precipitation below the solvus [Session 8 Slides 3-4]. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

In a hypothetical A-B system, A melts at 1000 °C and forms with B a eutectic at 800 °C. Instead of the diagram, the laboratory gives the compositions (wt% B) of the phases that are in equilibrium at several temperatures:

| T (°C) | Liquid in equilibrium with α | α (on the solidus or solvus) | β (on the solvus) |
| :--- | :--- | :--- | :--- |
| 1000 | 0 (pure A melts) | 0 | — |
| 950 | 12 | 4 | — |
| 900 | 24 | 8 | — |
| 850 | 36 | 12 | — |
| 800 (eutectic) | 48 | 16 | 85 |
| 600 | — | 10 | 88 |
| 400 | — | 6 | 91 |
| 20 | — | 3 | 94 |

Between two rows every boundary may be taken as straight (linear interpolation). A casting of 50 kg of an A-30 wt% B alloy is cooled slowly from 1050 °C to 20 °C.

(a) At which temperature does the casting start to solidify, and what is the composition of the first solid? At which temperature does it finish, and what is the composition of the last liquid?

(b) At 850 °C, give the phases, their compositions and their masses in kg.

(c) Just above and just below 800 °C, give the phases and the microconstituents with their masses in kg, and the mass of α inside the eutectic.

(d) At 20 °C, give the masses of α and β. How many kg of β form below 800 °C, from which constituent, and why?

## Setup

#### Data

| Quantity | Symbol | Value |
| :--- | :--- | :--- |
| Alloy | $C_0$ | 30 wt% B |
| Mass of the casting | $m$ | 50 kg |
| Eutectic | $T_E$, $C_E$ | 800 °C, 48 wt% B |
| Ends of the eutectic line | $C_\alpha$, $C_\beta$ | 16 and 85 wt% B |
| Tie lines | rows of the table | liquid and α from 950 to 800 °C; α and β from 800 to 20 °C |

The first column of compositions lies on the liquidus, the second on the α solidus (above 800 °C) or on the α solvus (below), the third on the β solvus. The table is the diagram: plotting its points and joining them gives the figure of part (a). The lever rule uses ratios of compositions in wt% B, where the factor 1/100 cancels; a mass is a fraction times 50 kg.

#### Model

- Tie line at temperature $T$: its ends are the two compositions in the row of $T$ [Session 7 Slide 15]; between rows, linear interpolation, $C(T) = C_1 + (T - T_1)\dfrac{C_2 - C_1}{T_2 - T_1}$.
- Lever rule [Session 7 Slides 15-16], derived in part (b).
- Microconstituents of a hypoeutectic alloy [Session 7 Slides 30, 32]; precipitation below the solvus [Session 8 Slides 3-4]. Hypotheses: equilibrium cooling, closed system.

## (a) First solid and last liquid [0.75 pts]

### Hint

Find between which rows the liquid column passes 30 wt% B, and interpolate both columns at that temperature. Then compare 30 with the eutectic line 16–85.

### Checkpoint

- Solidification starts at 875 °C; the first solid is α of 10 wt% B.
- It ends at 800 °C with the eutectic reaction; the last liquid has 48 wt% B.

### Solution

#### Place the alloy against the liquidus

On cooling, the alloy stays liquid until the liquid column of the table reaches its own composition: that point is on the liquidus. The liquid column goes from 24 wt% B at 900 °C to 36 wt% B at 850 °C, so 30 wt% B is reached between those two rows. Writing the liquidus between them as a straight line and isolating $T$:

$$C_L = 24 + (900 - T)\,\frac{36 - 24}{900 - 850} = 24 + 0.24\,(900 - T)$$

$$30 = 24 + 0.24\,(900 - T) \quad\Rightarrow\quad 900 - T = \frac{30 - 24}{0.24} = 25 \quad\Rightarrow\quad T = 875\ ^\circ\text{C}$$

#### Composition of the first solid

At 875 °C the first crystals are the α at the other end of the tie line, on the α solidus, interpolated between 8 wt% B (900 °C) and 12 wt% B (850 °C):

$$C_\alpha(875) = 8 + (900 - 875)\,\frac{12 - 8}{900 - 850} = 8 + 25 \times 0.08 = 10\ \text{wt\% B}$$

The first solid is much poorer in B than the alloy (10 against 30 wt% B), so the liquid left behind gets richer in B as α grows.

#### End of solidification

The alloy lies on the eutectic line, $16 < 30 < 48$, so it is hypoeutectic: its liquid keeps enriching along the liquidus until it reaches the eutectic point, 48 wt% B at 800 °C, and that last liquid turns into α + β at constant temperature [Session 7 Slides 30, 32]:

$$\text{cooling: } L\ (48\ \text{wt\% B}) \rightarrow \alpha\ (16\ \text{wt\% B}) + \beta\ (85\ \text{wt\% B}) \quad \text{at } 800\ ^\circ\text{C (eutectic)}$$

![[attachments/MAT-MT2/p08-table-diagram.svg]]

## (b) Phases and masses at 850 °C [0.75 pts]

### Hint

850 °C is a row of the table: no interpolation is needed. Write the two mass balances.

### Checkpoint

- L of 36 wt% B and α of 12 wt% B.
- $W_L = 0.75$: 37.5 kg of liquid and 12.5 kg of α.

### Solution

#### Read the tie line

850 °C lies between 875 °C and 800 °C, so the alloy is in α + L. The row of 850 °C gives the ends of the tie line: $C_\alpha = 12$ and $C_L = 36$ wt% B.

#### Derive the lever rule

The two phases make up the whole alloy (total mass balance), and the B of the alloy is the B of α plus the B of the liquid (mass balance of B):

$$W_\alpha + W_L = 1$$

$$W_\alpha C_\alpha + W_L C_L = C_0$$

Replacing $W_\alpha = 1 - W_L$ and expanding:

$$(1 - W_L)\,C_\alpha + W_L C_L = C_0$$

$$C_\alpha + W_L\,(C_L - C_\alpha) = C_0$$

so

$$W_L = \frac{C_0 - C_\alpha}{C_L - C_\alpha} \qquad W_\alpha = 1 - W_L = \frac{C_L - C_0}{C_L - C_\alpha}$$

#### Substitute and convert to kg

$$W_L = \frac{30 - 12}{36 - 12} = \frac{18}{24} = 0.75 \qquad W_\alpha = \frac{36 - 30}{24} = \frac{6}{24} = 0.25$$

$$m_L = 0.75 \times 50\ \text{kg} = 37.5\ \text{kg} \qquad m_\alpha = 0.25 \times 50\ \text{kg} = 12.5\ \text{kg}$$

Check of the B balance: $12.5 \times 0.12 + 37.5 \times 0.36 = 1.5 + 13.5 = 15.0$ kg of B, which is $0.30 \times 50$ kg.

## (c) Just above and just below 800 °C [0.75 pts]

### Hint

Above 800 °C the tie line runs from α (16) to the eutectic liquid (48); below it, from α (16) to β (85). The liquid of 48 wt% B becomes the eutectic.

### Checkpoint

- 800 + ΔT: α 28.125 kg, L 21.875 kg.
- 800 − ΔT: α 39.86 kg (16 wt% B), β 10.14 kg (85 wt% B).
- Primary α 28.125 kg, eutectic 21.875 kg; α inside the eutectic 11.73 kg.

### Solution

#### Just above 800 °C

The row of 800 °C gives $C_\alpha = 16$ and $C_L = C_E = 48$ wt% B (length 32):

$$W_\alpha = \frac{48 - 30}{48 - 16} = \frac{18}{32} = 0.5625 \qquad W_L = \frac{30 - 16}{32} = \frac{14}{32} = 0.4375$$

$$m_\alpha = 0.5625 \times 50 = 28.125\ \text{kg} \qquad m_L = 0.4375 \times 50 = 21.875\ \text{kg}$$

#### Just below 800 °C: phases

The eutectic reaction has used up the liquid. The tie line is the whole eutectic line, $C_\alpha = 16$ to $C_\beta = 85$ wt% B (length 69):

$$W_\alpha = \frac{85 - 30}{85 - 16} = \frac{55}{69} = 0.7971 \qquad W_\beta = \frac{30 - 16}{69} = \frac{14}{69} = 0.2029$$

$$m_\alpha = 0.7971 \times 50 = 39.86\ \text{kg} \qquad m_\beta = 0.2029 \times 50 = 10.14\ \text{kg}$$

#### Just below 800 °C: microconstituents

The α formed above 800 °C stays as **primary α**, and the liquid of eutectic composition becomes the **eutectic** [Session 7 Slide 32]:

$$m_{\alpha'} = 28.125\ \text{kg} \qquad m_E = 21.875\ \text{kg}$$

All the β is in the eutectic (the primary phase is α); the α of the eutectic is the total α minus the primary α:

$$m_{\alpha,E} = 39.86 - 28.125 = 11.73\ \text{kg}$$

Check with the make-up of the eutectic, $(85 - 48)/69 = 0.5362$ α: $0.5362 \times 21.875 = 11.73$ kg, and $11.73 + 10.14 = 21.87$ kg $= m_E$.

## (d) At 20 °C and the precipitated β [0.75 pts]

### Hint

Use the row of 20 °C. Compare the β with that just below 800 °C, and look at how the α solvus moves.

### Checkpoint

- α (3 wt% B) 35.16 kg; β (94 wt% B) 14.84 kg.
- 4.69 kg of β precipitate below 800 °C, from the α (primary and eutectic).

### Solution

#### Phases at 20 °C

Below 800 °C the ends of the tie line follow the two solvus columns; at 20 °C they are $C_\alpha = 3$ and $C_\beta = 94$ wt% B (length 91):

$$W_\alpha = \frac{94 - 30}{94 - 3} = \frac{64}{91} = 0.7033 \qquad W_\beta = \frac{30 - 3}{91} = \frac{27}{91} = 0.2967$$

$$m_\alpha = 0.7033 \times 50 = 35.16\ \text{kg} \qquad m_\beta = 0.2967 \times 50 = 14.84\ \text{kg}$$

#### β formed in the solid state

$$\Delta m_\beta = m_\beta(20\ ^\circ\text{C}) - m_\beta(800 - \Delta T) = 14.835 - 10.145 = 4.69\ \text{kg}$$

(with the unrounded masses $50 \times 27/91 = 14.835$ kg and $50 \times 14/69 = 10.145$ kg). The α column falls from 16 wt% B at 800 °C to 3 wt% B at 20 °C: α can hold less and less B, so the α of the casting (primary α and the α of the eutectic) becomes supersaturated and rejects the excess as small β particles, which grow as the temperature falls [Session 8 Slides 3-4]. The β column also moves (85 → 94 wt% B), so the β already present gets slightly richer in B too. The microconstituents keep their names; the primary α now holds fine β precipitates.

## Interpretation

The table is enough to follow the whole cooling: the casting starts to solidify at 875 °C with α of 10 wt% B, is three-quarters liquid at 850 °C, reaches 800 °C with 28.1 kg of primary α and 21.9 kg of liquid of 48 wt% B, and that liquid becomes eutectic. In the solid, another 4.69 kg of β precipitate down to room temperature.

Control cases: for $C_0 \to 16$ the eutectic vanishes and for $C_0 \to 48$ the casting is all eutectic; at the liquidus temperature (875 °C) the lever rule gives $W_L = (30 - 10)/(30 - 10) = 1$, all liquid, as it must. Every pair of masses adds up to 50 kg. Dimensional check: the lever rule is (wt% B)/(wt% B), dimensionless; the interpolation slopes are 0.24 and 0.08 wt% B per °C, so $(T_1 - T)$ in °C times them gives wt% B; masses are fractions times kg.

Common exam mistake: taking the first solid to have the alloy composition (30 wt% B). The first solid sits at the other end of the tie line, on the solidus, and is much poorer in B (10 wt% B).

## Verification

- liquidus temperature (C) | 900-(30-24)/((36-24)/(900-850)) | 875
- first solid (wt% B) | 8+(900-875)*(12-8)/(900-850) | 10
- W_L at 850 C | (30-12)/(36-12) | 0.75
- liquid at 850 C (kg) | 50*(30-12)/(36-12) | 37.5
- alpha at 850 C (kg) | 50*(36-30)/(36-12) | 12.5
- alpha at 800+dT (kg) | 50*(48-30)/(48-16) | 28.125
- liquid at 800+dT (kg) | 50*(30-16)/(48-16) | 21.875
- W_alpha at 800-dT | (85-30)/(85-16) | 0.7971
- alpha at 800-dT (kg) | 50*(85-30)/(85-16) | 39.86
- beta at 800-dT (kg) | 50*(30-16)/(85-16) | 10.14
- alpha inside the eutectic (kg) | 50*((85-30)/(85-16)-(48-30)/(48-16)) | 11.73
- make-up of the eutectic (alpha) | (85-48)/(85-16) | 0.5362
- W_alpha at 20 C | (94-30)/(94-3) | 0.7033
- alpha at 20 C (kg) | 50*(94-30)/(94-3) | 35.16
- beta at 20 C (kg) | 50*(30-3)/(94-3) | 14.84
- beta precipitated (kg) | 50*((30-3)/(94-3)-(30-16)/(85-16)) | 4.69

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
