---
materia: Aerospace Materials I
tema: "Unit 4: phase diagrams"
bank_id: P03
title: "Cooling an X-40 wt% Y alloy through a peritectic, a eutectic and a eutectoid"
category: mt2_problem
archetype: phase-diagram-invariant
level: standard
unit: 4
difficulty: 3
points: 3.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of Problems T4_PhaseDiagrams I.pdf, Problem 13 (cooling sequence with microstructures at three temperatures) and of the final of January 2016, question 4 (Ni-Ti: reactions, sketch at T - ΔT, microconstituents); hypothetical system, not an official exercise. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - phase-diagram-invariant
  - peritectic
  - eutectoid
  - gibbs-phase-rule
  - microstructure-sketch
---

# Bank P03 — Cooling through a peritectic, a eutectic and a eutectoid

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the cooling-sequence problems of the Unit 4 sheet and of the final of January 2016. The X-Y system is hypothetical. Method: Session 7, Slides 13-16 and 30-32; Session 8, Slides 6-11 and 17. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

The figure shows the equilibrium phase diagram of a hypothetical binary system X-Y (composition in wt% Y). γ is an intermetallic compound of 55 wt% Y; β is an intermediate solid solution that exists only between 1100 and 600 °C.

![[attachments/MAT-MT2/p03-xy-diagram.svg]]

a) Write all the invariant reactions with their type, temperature and the composition of the three phases, and say how γ melts.

b) Apply the Gibbs phase rule (pressure constant) at the point of 25 wt% Y and 600 °C, inside the β + L field and inside the β field, and explain what each result means.

c) An alloy X-40 wt% Y is cooled slowly from the liquid. Describe its solidification down to 900 °C, giving the phases, their compositions and their amounts at 1100 + ΔT, 1100 − ΔT, 900 + ΔT and 900 − ΔT °C.

d) Continue the cooling to 600 − ΔT °C: give the phases and the microconstituents with their amounts, and sketch the microstructure at 1100 + ΔT, 900 − ΔT and 600 − ΔT °C.

## Setup

#### Data read on the diagram

| Item | Value read on the figure |
| :--- | :--- |
| Melting points | X 1300 °C, Y 800 °C, γ 1000 °C (top of its liquidus) |
| Line at 1100 °C | α 15, β 30, L 45 wt% Y |
| Line at 900 °C | β 38, L 50, γ 55 wt% Y |
| Line at 650 °C | γ 55, L 80, δ 95 wt% Y |
| Line at 600 °C | α 10, β 25, γ 55 wt% Y |
| Alloy | $C_0$ = 40 wt% Y |

Units: 40 wt% Y is a mass fraction of 0.40 kg of Y per kg of alloy; the lever rule divides two composition differences, so the fractions it gives are dimensionless mass fractions. Temperatures stay in °C because no formula here needs kelvin.

#### Model

- **Invariant reactions** [Session 8 Slide 6]: eutectic $L \rightarrow \alpha + \beta$, peritectic $\alpha + L \rightarrow \beta$ [Session 8 Slides 8-9], eutectoid $\gamma \rightarrow \alpha + \beta$ in the solid state [Session 8 Slide 7], peritectoid $\alpha + \beta \rightarrow \gamma$ [Session 8 Slide 11].
- **Gibbs phase rule** $F = C - P + N$, with $N = 1$ at constant pressure [Session 7 Slide 13].
- **Lever rule** on the tie line [Session 7 Slides 15-16]; primary constituents counted just above an invariant line, total phases just below it [Session 7 Slides 30-32].
- **Congruent melting** at a maximum of the liquidus [Session 8 Slide 17].
- Hypotheses: equilibrium cooling (the peritectic reaction and the solid-state diffusion are complete), 1 atm, values as printed.

## (a) Invariant reactions and the melting of γ [0.75 pts]

### Hint

There are four horizontal lines. Two of them have a liquid on the line, one has a solid field closing in a V from above (no liquid), and one has a new solid appearing below the line between the two phases above it.

### Checkpoint

- 1100 °C, peritectic: α (15) + L (45) → β (30).
- 900 °C, eutectic: L (50) → β (38) + γ (55).
- 650 °C, eutectic: L (80) → γ (55) + δ (95).
- 600 °C, eutectoid: β (25) → α (10) + γ (55). All in wt% Y.
- γ melts congruently at 1000 °C.

### Solution

#### Why each horizontal line is an invariant reaction

Three phases of a two-component system at constant pressure leave $F = 2 - 3 + 1 = 0$ [Session 7 Slide 13], so each three-phase equilibrium is one horizontal line with three fixed compositions. The diagram has four.

#### The line at 1100 °C

Above it lies α + L, from α (15) to L (45). Below it the field of β starts at 30 wt% Y, between the two: a new solid forms from a solid and a liquid, the inverted V of a **peritectic** [Session 8 Slides 8-9]:

$$\alpha\,(15) + L\,(45) \;\xrightarrow{\;1100\ ^\circ\text{C}\;}\; \beta\,(30) \qquad \text{peritectic, wt\% Y}$$

#### The lines at 900 and 650 °C

At 900 °C the liquidus of β (falling from 45 at 1100 °C) and the left branch of the liquidus of γ (falling from 1000 °C) meet in a V at 50 wt% Y; below lies β + γ. At 650 °C the right branch of the γ liquidus and the liquidus of δ (from 800 °C, pure Y) meet in a V at 80 wt% Y; below lies γ + δ. Both are **eutectics**:

$$L\,(50) \;\xrightarrow{\;900\ ^\circ\text{C}\;}\; \beta\,(38) + \gamma\,(55) \qquad L\,(80) \;\xrightarrow{\;650\ ^\circ\text{C}\;}\; \gamma\,(55) + \delta\,(95)$$

#### The line at 600 °C

No liquid reaches this line. The single-phase field β narrows downwards between its two solvus lines and closes in a V at 25 wt% Y on the line; below it lies α + γ. A solid that transforms into two other solids is a **eutectoid** [Session 8 Slide 7]:

$$\beta\,(25) \;\xrightarrow{\;600\ ^\circ\text{C}\;}\; \alpha\,(10) + \gamma\,(55) \qquad \text{eutectoid}$$

#### Melting of γ

The vertical line of γ reaches the liquidus at its maximum, 1000 °C, where γ gives a liquid of its own composition (55 wt% Y): **congruent melting** [Session 8 Slide 17].

## (b) Gibbs phase rule at the eutectoid point, in β + L and in β [0.5 pts]

### Hint

Count the components and the phases; at constant pressure only temperature remains as a non-compositional variable.

### Checkpoint

- Eutectoid point (25 wt% Y, 600 °C): $F = 0$.
- β + L field: $F = 1$.
- β field: $F = 2$.

### Solution

#### State the rule and why N = 1

The phase rule is $F = C - P + N$ [Session 7 Slide 13]. Pressure is fixed at 1 atm in a phase diagram of this kind, so only temperature is a non-compositional variable, $N = 1$, and $F = C - P + 1$. The system has two components, X and Y, so $C = 2$.

#### At the eutectoid point

Three phases coexist, β, α and γ, so $P = 3$:

$$F = 2 - 3 + 1 = 0$$

Nothing can be changed: the transformation happens only at 600 °C, with β of 25, α of 10 and γ of 55 wt% Y. On a cooling curve it gives a plateau, like the eutectic.

#### Inside β + L

Two phases, $P = 2$:

$$F = 2 - 2 + 1 = 1$$

Choosing the temperature uses the only degree of freedom: the compositions of β and L are then fixed by the ends of the tie line, and the alloy composition only changes their amounts.

#### Inside β

One phase, $P = 1$:

$$F = 2 - 1 + 1 = 2$$

Temperature and composition can both change (within the field) without a new phase appearing.

## (c) Solidification of X-40 wt% Y down to 900 °C [1.0 pts]

### Hint

The 40 wt% Y vertical first meets the α liquidus. At 1100 °C, 40 lies between β (30) and L (45), so the peritectic uses up all the α and leaves liquid. Then β grows from the liquid down to the eutectic at 900 °C.

### Checkpoint

- 1100 + ΔT: α (15) 0.167, L (45) 0.833.
- 1100 − ΔT: β (30) 0.333, L (45) 0.667.
- 900 + ΔT: β (38) 0.833, L (50) 0.167.
- 900 − ΔT: β (38) 0.882, γ (55) 0.118; microconstituents primary β 0.833 and eutectic β + γ 0.167.

### Solution

#### First solid: primary α

The 40 wt% Y vertical crosses the liquidus of α just above 1100 °C (the liquidus reaches 45 wt% Y at 1100 °C, so for 40 wt% Y it is a few tens of degrees higher; a reading of the figure). Crystals of α start to grow, and the liquid becomes richer in Y along the liquidus.

#### Derive the lever rule and apply it at 1100 + ΔT

On a tie line with phases α and L the alloy and the element Y must both be conserved:

$$W_\alpha + W_L = 1 \qquad W_\alpha C_\alpha + W_L C_L = C_0$$

Substituting $W_L = 1 - W_\alpha$ and grouping the terms in $W_\alpha$:

$$W_\alpha (C_\alpha - C_L) = C_0 - C_L \qquad\Rightarrow\qquad W_\alpha = \frac{C_L - C_0}{C_L - C_\alpha} \qquad W_L = \frac{C_0 - C_\alpha}{C_L - C_\alpha}$$

Just above 1100 °C, α has 15 and L has 45 wt% Y (length 30):

$$W_\alpha = \frac{45 - 40}{45 - 15} = \frac{5}{30} = 0.167 \qquad W_L = \frac{40 - 15}{45 - 15} = \frac{25}{30} = 0.833$$

#### The peritectic reaction at 1100 °C

At 1100 °C, α (15) reacts with L (45) to give β (30). The alloy (40) lies to the right of β, between β and L, so the α runs out before the liquid. Just below 1100 °C the tie line runs from β (30) to L (45), length 15:

$$W_\beta = \frac{45 - 40}{45 - 30} = \frac{5}{15} = 0.333 \qquad W_L = \frac{40 - 30}{45 - 30} = \frac{10}{15} = 0.667$$

#### From 1100 to 900 °C: β grows from the liquid

In β + L the liquid follows the β liquidus from 45 to 50 wt% Y and β follows its solidus from 30 to 38 wt% Y; the amount of β grows. Just above 900 °C (β 38, L 50, length 12):

$$W_\beta = \frac{50 - 40}{50 - 38} = \frac{10}{12} = 0.833 \qquad W_L = \frac{40 - 38}{50 - 38} = \frac{2}{12} = 0.167$$

This β, formed partly by the peritectic and partly from the liquid, is the **primary β** (0.833), and the liquid, now of eutectic composition, is the future eutectic (0.167).

#### The eutectic at 900 °C

The remaining liquid transforms at 900 °C into β (38) + γ (55). Just below the line, the total phases on the tie line from β (38) to γ (55), length 17:

$$W_\beta = \frac{55 - 40}{55 - 38} = \frac{15}{17} = 0.882 \qquad W_\gamma = \frac{40 - 38}{55 - 38} = \frac{2}{17} = 0.118$$

Microconstituents: primary β 0.833 and eutectic (β + γ) 0.167. All the γ is in the eutectic, and the eutectic β is $0.882 - 0.833 = 0.049$; $0.049 + 0.118 = 0.167$.

## (d) Cooling to 600 − ΔT °C and the three sketches [0.75 pts]

### Hint

Between 900 and 600 °C the β follows its solvus from 38 to 25 wt% Y and rejects γ. At 600 °C every grain of β, primary or eutectic, transforms into the eutectoid α + γ.

### Checkpoint

- 600 + ΔT: β (25) 0.500, γ (55) 0.500.
- 600 − ΔT: α (10) 0.333, γ (55) 0.667.
- Microconstituents at 600 − ΔT: eutectoid (α + γ) 0.500 and γ outside the eutectoid 0.500 (eutectic γ 0.118 plus γ precipitated in the solid 0.382).

### Solution

#### From 900 to 600 °C: precipitation of γ

In β + γ the boundary of β moves from 38 to 25 wt% Y as the temperature falls, so the β loses Y and γ precipitates from it in the solid state (Session 8 Slides 2-4 call this solid-state precipitation). Just above 600 °C (β 25, γ 55, length 30):

$$W_\beta = \frac{55 - 40}{55 - 25} = \frac{15}{30} = 0.500 \qquad W_\gamma = \frac{40 - 25}{55 - 25} = \frac{15}{30} = 0.500$$

The γ grew from 0.118 to 0.500, so $0.500 - 0.118 = 0.382$ of γ precipitated between 900 and 600 °C.

#### The eutectoid at 600 °C

All the β (0.500), which now has the eutectoid composition 25 wt% Y, transforms into the fine eutectoid α + γ. Below the line the total phases on the tie line from α (10) to γ (55), length 45:

$$W_\alpha = \frac{55 - 40}{55 - 10} = \frac{15}{45} = 0.333 \qquad W_\gamma = \frac{40 - 10}{55 - 10} = \frac{30}{45} = 0.667$$

The microconstituents are counted just above the line, like a primary constituent above a eutectic: eutectoid = $W_\beta(600 + \Delta T)$ = 0.500, and γ outside it = 0.500. Check: inside the eutectoid (25 wt% Y) the fraction of α is $(55 - 25)/(55 - 10) = 30/45 = 0.667$, and $0.667 \times 0.500 = 0.333$, all the α of the alloy.

#### The three sketches

At 1100 + ΔT: a few rounded grains of primary α in a large amount of liquid. At 900 − ΔT: large grains of primary β (the α has disappeared in the peritectic) in a lamellar eutectic β + γ. At 600 − ΔT: every former β region, primary and inside the eutectic, is now a fine eutectoid α + γ, with films of γ precipitated on the boundaries of the former β grains.

![[attachments/MAT-MT2/p03-sketches.svg]]

## Interpretation

The alloy passes through three invariant reactions, but none of the original microconstituents survives unchanged: the primary α is consumed by the peritectic, and the primary β disappears in the eutectoid, leaving only a trace of its shape. This is the solid-state counterpart of the eutectic: like a eutectic liquid, the β of 25 wt% Y transforms at one temperature into two phases ($F = 0$). Checks: every fraction lies between 0 and 1, each pair adds up to 1, and the Y balance at 600 − ΔT is $0.333 \times 10 + 0.667 \times 55 = 3.33 + 36.67 = 40.0$ wt% Y. Limiting case: an alloy of exactly 30 wt% Y would leave neither α nor liquid after the peritectic and be 100 % β just below 1100 °C. Dimensions: all fractions are wt% over wt%, dimensionless. Common mistake: taking the eutectoid fraction from the tie line below 600 °C ($W_\alpha$ = 0.333, a phase) instead of from the β just above it (0.500, a microconstituent).

## Verification

- (c) W_alpha at 1100+dT | (45-40)/(45-15) | 0.167
- (c) W_L at 1100+dT | (40-15)/(45-15) | 0.833
- (c) W_beta at 1100-dT | (45-40)/(45-30) | 0.333
- (c) W_L at 1100-dT | (40-30)/(45-30) | 0.667
- (c) primary beta at 900+dT | (50-40)/(50-38) | 0.833
- (c) eutectic at 900 C | (40-38)/(50-38) | 0.167
- (c) W_beta at 900-dT | (55-40)/(55-38) | 0.882
- (c) W_gamma at 900-dT | (40-38)/(55-38) | 0.118
- (c) eutectic beta | (55-40)/(55-38) - (50-40)/(50-38) | 0.049
- (d) W_beta at 600+dT | (55-40)/(55-25) | 0.500
- (d) precipitated gamma | (40-25)/(55-25) - (40-38)/(55-38) | 0.382
- (d) W_alpha at 600-dT | (55-40)/(55-10) | 0.333
- (d) W_gamma at 600-dT | (40-10)/(55-10) | 0.667

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
