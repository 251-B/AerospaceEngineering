---
materia: Aerospace Materials I
tema: "Unit 4: phase diagrams"
bank_id: P02
title: "Alloy composition from the eutectic fraction in an M-N system with an incongruent compound (at%)"
category: mt2_problem
archetype: phase-diagram-invariant
level: standard
unit: 4
difficulty: 3
points: 3.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of the final of January 2014, question 1 (Al-Ni in at%, MATERIALS_FINALEXAM_COMPILATION_2013-2017.pdf, pp. 4 and 12-13) and of the 2017 extraordinary final (composition worked backwards from a microstructure); hypothetical system, not an official exercise. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - phase-diagram-invariant
  - peritectic
  - incongruent-melting
  - atomic-percent
  - lever-rule
---

# Bank P02 — Alloy composition from the eutectic fraction in a peritectic system

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Al-Ni problem of January 2014 (diagram in atomic percent) and of the finals that ask for a composition worked backwards from a microstructure. The M-N system is hypothetical. Method: Session 7, Slides 13-16 and 30-32; Session 8, Slides 6, 8-9, 14-15 and 17. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

The figure shows the equilibrium phase diagram of a hypothetical binary system M-N, with the composition in **atomic percent** of N. The intermediate phase δ is the stoichiometric compound MN₂.

![[attachments/MAT-MT2/p02-mn-diagram.svg]]

a) Write all the invariant reactions: type, temperature and composition (at% N) of every phase involved.

b) Does δ melt congruently or incongruently? Give the phases and their amounts when δ is heated to 1000 + ΔT °C, and the maximum solubility of N in M and of M in N, with their temperatures.

c) A slowly cooled M-N alloy, examined just below 600 °C, shows grains of primary δ surrounded by 30.0 % of eutectic microconstituent (atom fraction 0.300). Find the composition of the alloy.

d) For the alloy of part (c), give the phases present, their compositions and their amounts at 1000 + ΔT °C, at 1000 − ΔT °C and at 600 − ΔT °C.

## Setup

#### Data read on the diagram

| Item | Value read on the figure |
| :--- | :--- |
| Melting points | M 1400 °C, N 700 °C |
| Compound δ = MN₂ | vertical line at 66.7 at% N, from the 1000 °C line down |
| Invariant line at 1000 °C | α 25 at% N, δ 66.7 at% N, L 78 at% N |
| Invariant line at 600 °C | δ 66.7 at% N, L 92 at% N, β 98 at% N |
| Microstructure of part (c) | primary δ + eutectic, $x_E$ = 0.300 just below 600 °C |

Units: the axis is in at% N, so a composition of 66.7 at% N means 0.667 mol of N atoms per mol of atoms. The lever rule is a ratio of composition differences, so on an atomic axis it gives **atom (mole) fractions** $x$ of each phase or constituent; this reading of the lever rule on an at% axis is an **extension** of Session 7 Slide 16, where the axis is in wt% and the fractions are mass fractions $W$ (the same construction, with the balance written for atoms instead of mass). The value 66.7 is $2/3 \times 100$, the N content of MN₂ (two N atoms out of three).

#### Model

- **Invariant reactions** [Session 8 Slide 6]: eutectic $L \rightarrow \alpha + \beta$; peritectic $\alpha + L \rightarrow \beta$, where a solid field ends in an inverted V below the line [Session 8 Slides 8-9].
- **Gibbs phase rule** at constant pressure, $F = C - P + 1$ [Session 7 Slide 13]: three phases of two components give $F = 0$, a horizontal line.
- **Lever rule** on a tie line [Session 7 Slides 15-16]; **microconstituents** counted on the tie line just above the eutectic line [Session 7 Slides 30-32].
- **Congruent and incongruent melting** [Session 8 Slide 17]: a compound at a maximum of the liquidus melts congruently; one ending at a peritectic line melts incongruently (liquid plus another solid).
- Hypotheses: equilibrium cooling (complete peritectic reaction, no coring), 1 atm, compositions read on the figure as printed.

## (a) Write all the invariant reactions [0.75 pts]

### Hint

Two horizontal lines. For each, look at what lies above it: a liquid that ends in a V (eutectic) or a solid plus liquid that meet a new solid in an inverted V (peritectic).

### Checkpoint

- 1000 °C, peritectic: α (25 at% N) + L (78 at% N) → δ (66.7 at% N).
- 600 °C, eutectic: L (92 at% N) → δ (66.7 at% N) + β (98 at% N).

### Solution

#### Why horizontal lines are the invariant reactions

With $C = 2$ and $P = 3$ the phase rule gives $F = 2 - 3 + 1 = 0$ [Session 7 Slide 13]: temperature and the three compositions are fixed, so every three-phase equilibrium is one horizontal line. The diagram has two of them.

#### Classify the line at 1000 °C

The line runs from α (25) to L (78). Above it lies the two-phase field α + L. Below it, the vertical line of δ (66.7) starts at the line and splits it into α + δ (left) and δ + L (right): a new solid appears below the line between the two phases above it, the inverted V of a **peritectic** [Session 8 Slides 8-9]. On cooling:

$$\alpha\,(25\ \text{at\% N}) + L\,(78\ \text{at\% N}) \;\xrightarrow{\;1000\ ^\circ\text{C}\;}\; \delta\,(66.7\ \text{at\% N}) \qquad \text{peritectic}$$

#### Classify the line at 600 °C

The liquidus of δ falls from 78 at% N at 1000 °C and the liquidus of β falls from 700 °C (pure N); they meet in a V at 92 at% N on the line, and below it lies δ + β. A liquid that gives two solids is a **eutectic**:

$$L\,(92\ \text{at\% N}) \;\xrightarrow{\;600\ ^\circ\text{C}\;}\; \delta\,(66.7\ \text{at\% N}) + \beta\,(98\ \text{at\% N}) \qquad \text{eutectic}$$

#### Check

Each reaction has the composition of the product (or the liquid of the eutectic) between the other two: $25 < 66.7 < 78$ and $66.7 < 92 < 98$. The eutectic temperature, 600 °C, is below the melting point of N (700 °C) and below the temperature at which δ stops existing (1000 °C).

## (b) Melting of δ, decomposition at 1000 + ΔT °C and maximum solubilities [0.75 pts]

### Hint

δ does not reach the liquidus: follow its vertical line up to the 1000 °C line and read the tie line just above it. The lever rule is derived here from the two atom balances.

### Checkpoint

- δ melts incongruently (it ends at the peritectic line, 1000 °C).
- At 1000 + ΔT °C, δ has become α (25 at% N) 0.213 + L (78 at% N) 0.787.
- Maximum solubility of N in M: 25 at% N at 1000 °C; of M in N: 2 at% M at 600 °C.

### Solution

#### Classify the melting of δ

The δ line stops at 1000 °C, on the peritectic line, well below the liquidus. Heating δ through 1000 °C runs the peritectic backwards, $\delta \rightarrow \alpha + L$: the compound gives a liquid of a different composition (78 at% N) plus another solid (α). By Session 8 Slide 17 this is **incongruent melting**.

#### Derive the lever rule for atom fractions

Just above 1000 °C the δ composition, $C_0$ = 66.7 at% N, lies in α + L on the tie line from α (25) to L (78). The atoms of the alloy are shared by the two phases, and so are the N atoms:

$$x_\alpha + x_L = 1 \qquad x_\alpha C_\alpha + x_L C_L = C_0$$

Substituting $x_L = 1 - x_\alpha$:

$$x_\alpha C_\alpha + (1 - x_\alpha) C_L = C_0$$

$$x_\alpha (C_\alpha - C_L) = C_0 - C_L$$

$$x_\alpha = \frac{C_L - C_0}{C_L - C_\alpha} \qquad x_L = 1 - x_\alpha = \frac{C_0 - C_\alpha}{C_L - C_\alpha}$$

#### Amounts at 1000 + ΔT °C

Tie line length $78 - 25 = 53$ at% N:

$$x_\alpha = \frac{78 - 66.7}{78 - 25} = \frac{11.3}{53} = 0.213 \qquad x_L = \frac{66.7 - 25}{78 - 25} = \frac{41.7}{53} = 0.787$$

Most of the compound turns into liquid, and about a fifth of its atoms stay as solid α.

#### Maximum solubilities

The α field is widest where it touches the peritectic line, at 25 at% N: N dissolves in M up to **25 at% N at 1000 °C**. The β field touches the eutectic line at 98 at% N, so M dissolves in N up to

$$100 - 98 = 2\ \text{at\% M}$$

at **600 °C**.

## (c) Composition of the alloy with primary δ and 30.0 % eutectic [0.75 pts]

### Hint

Write the eutectic fraction with the lever rule on the tie line just above 600 °C (from δ to the eutectic liquid) and solve it for $C_0$. Check which side of the eutectic point the alloy must be on.

### Checkpoint

- The alloy is between δ (66.7) and the eutectic point (92), because its primary constituent is δ.
- $C_0$ = 74.29 at% N (about 74.3 at% N).

### Solution

#### Choose the side of the eutectic

The eutectic microconstituent at 600 °C forms from alloys between 66.7 and 98 at% N. Those between 66.7 and 92 at% N reach 600 °C with primary δ, those between 92 and 98 at% N with primary β. The alloy shows primary δ, so $66.7 < C_0 < 92$.

#### Write the eutectic fraction with the lever rule

Just above 600 °C the alloy is δ (66.7) + liquid of eutectic composition (92). All that liquid becomes eutectic, so the eutectic fraction is the liquid fraction on this tie line (lever rule of part b):

$$x_E = x_L(600 + \Delta T) = \frac{C_0 - C_\delta}{C_E - C_\delta}$$

#### Isolate the composition

Multiply both sides by $(C_E - C_\delta)$:

$$x_E\,(C_E - C_\delta) = C_0 - C_\delta$$

Add $C_\delta$ to both sides:

$$C_0 = C_\delta + x_E\,(C_E - C_\delta)$$

Substitute $x_E$ = 0.300, $C_\delta$ = 66.7 and $C_E$ = 92 at% N:

$$C_0 = 66.7 + 0.300 \times (92 - 66.7) = 66.7 + 0.300 \times 25.3 = 66.7 + 7.59 = 74.29\ \text{at\% N}$$

#### Check

$66.7 < 74.29 < 92$, as required. Back-substitution: $(74.29 - 66.7)/(92 - 66.7) = 7.59/25.3 = 0.300$. The primary δ is $1 - 0.300 = 0.700$. The other root, from the hypereutectic side, $x_E = (98 - C_0)/(98 - 92)$, would give $C_0 = 98 - 0.300 \times 6 = 96.2$ at% N, but that alloy has primary β, not δ, so it is rejected.

## (d) Phases of the alloy M-74.29 at% N at 1000 ± ΔT and 600 − ΔT °C [0.75 pts]

### Hint

At 1000 + ΔT the alloy (74.29) lies between α (25) and L (78). After the peritectic it lies between δ (66.7) and L (78), because it has more N than δ. Below 600 °C the tie line runs from δ to β.

### Checkpoint

- 1000 + ΔT °C: α (25 at% N) 0.0700 and L (78 at% N) 0.930.
- 1000 − ΔT °C: δ (66.7 at% N) 0.328 and L (78 at% N) 0.672.
- 600 − ΔT °C: δ (66.7 at% N) 0.758 and β (98 at% N) 0.242.

### Solution

#### Just above the peritectic line

The alloy, 74.29 at% N, lies on the tie line from α (25) to L (78), length 53:

$$x_\alpha = \frac{78 - 74.29}{78 - 25} = \frac{3.71}{53} = 0.0700 \qquad x_L = \frac{74.29 - 25}{78 - 25} = \frac{49.29}{53} = 0.930$$

#### Just below the peritectic line

At 1000 °C all the α reacts with part of the liquid to form δ. Since $C_0 = 74.29 > 66.7$, the α runs out first and liquid is left over (as for alloy 2 of Session 8 Slide 9). Tie line from δ (66.7) to L (78), length 11.3:

$$x_\delta = \frac{78 - 74.29}{78 - 66.7} = \frac{3.71}{11.3} = 0.328 \qquad x_L = \frac{74.29 - 66.7}{78 - 66.7} = \frac{7.59}{11.3} = 0.672$$

#### Just below the eutectic line

Between 1000 and 600 °C more δ grows from the liquid, which follows the liquidus to 92 at% N; at 600 °C the remaining liquid (0.300, part c) becomes eutectic δ + β. Tie line from δ (66.7) to β (98), length 31.3:

$$x_\delta = \frac{98 - 74.29}{98 - 66.7} = \frac{23.71}{31.3} = 0.758 \qquad x_\beta = \frac{74.29 - 66.7}{98 - 66.7} = \frac{7.59}{31.3} = 0.242$$

#### Check with the microconstituents

The δ total (0.758) is primary δ (0.700) plus eutectic δ, so the eutectic δ is 0.0575 and the eutectic β 0.242; together $0.0575 + 0.242 = 0.300 = x_E$. N balance at 600 − ΔT: $0.758 \times 66.7 + 0.242 \times 98 = 50.56 + 23.72 = 74.28$ at% N, equal to $C_0$ = 74.29 within the rounding of the fractions.

## Interpretation

δ cannot be melted as a single liquid of its own composition: it decomposes at 1000 °C into a liquid and the M-rich α, which is why it ends in a peritectic and not at a maximum of the liquidus. The fraction of eutectic is a fingerprint of the composition: on the δ side it grows linearly from 0 at 66.7 at% N to 1 at 92 at% N, so a measured eutectic fraction fixes $C_0$ uniquely once the primary constituent is known. Limiting cases: $x_E \to 0$ gives $C_0 \to 66.7$ (pure δ) and $x_E \to 1$ gives $C_0 \to 92$ (fully eutectic). Dimensions: every fraction is at% over at%, dimensionless, and every composition stays between the ends of its tie line. Common mistake: using mass fractions or quoting the result in wt%; on an at% diagram the lever rule gives atom fractions, and converting to wt% would need the atomic masses of M and N, which the problem does not give.

## Verification

- (b) x_alpha at 1000+dT | (78-66.7)/(78-25) | 0.213
- (b) x_L at 1000+dT | (66.7-25)/(78-25) | 0.787
- (b) solubility of M in N (at%) | 100-98 | 2
- (c) C0 (at% N) | 66.7+0.300*(92-66.7) | 74.29
- (c) hypereutectic root rejected | 98-0.300*(98-92) | 96.2
- (d) x_alpha at 1000+dT | (78-(66.7+0.3*(92-66.7)))/(78-25) | 0.0700
- (d) x_L at 1000+dT | ((66.7+0.3*(92-66.7))-25)/(78-25) | 0.930
- (d) x_delta at 1000-dT | (78-(66.7+0.3*(92-66.7)))/(78-66.7) | 0.328
- (d) x_L at 1000-dT | ((66.7+0.3*(92-66.7))-66.7)/(78-66.7) | 0.672
- (d) x_delta at 600-dT | (98-(66.7+0.3*(92-66.7)))/(98-66.7) | 0.758
- (d) x_beta at 600-dT | ((66.7+0.3*(92-66.7))-66.7)/(98-66.7) | 0.242
- (d) eutectic delta | (98-(66.7+0.3*(92-66.7)))/(98-66.7) - 0.7 | 0.0575

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
