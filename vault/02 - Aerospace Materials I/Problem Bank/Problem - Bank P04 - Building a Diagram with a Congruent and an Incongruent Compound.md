---
materia: Aerospace Materials I
tema: "Unit 4: phase diagrams"
bank_id: P04
title: "Building a G-H diagram with a congruent and an incongruent compound from a table of equilibria"
category: mt2_problem
archetype: phase-diagram-invariant
level: standard
unit: 4
difficulty: 3
points: 3.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of the final of June 2014, question 3 (building a diagram from a list of features, MATERIALS_FINALEXAM_COMPILATION_2013-2017.pdf, p. 21), of Problems T4_PhaseDiagrams I.pdf, Problem 11, and of the Part II problem of MATERIALS_SECONDPARTIAL_2019.pdf (Ni-Nb); hypothetical system, not an official exercise. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - phase-diagram-invariant
  - building-a-diagram
  - congruent-melting
  - incongruent-melting
  - lever-rule
---

# Bank P04 — Building a diagram with a congruent and an incongruent compound

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the June 2014 final (draw a diagram from its features) and of the Part II problem of the 2019 Assessment Test II. The G-H system is hypothetical. Method: Session 7, Slides 15-16 and 26-32; Session 8, Slides 6, 8-9, 14-15 and 17. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

A laboratory has measured the following features of a hypothetical binary system G-H (compositions in wt% H). No diagram is given.

| Feature | Measured data |
| :--- | :--- |
| Pure G | melts at 1500 °C; forms the terminal solid solution α |
| Pure H | melts at 1350 °C; forms the terminal solid solution β |
| Compound θ (stoichiometric, 30 wt% H) | melts at 1400 °C to a liquid of 30 wt% H |
| Compound η (stoichiometric, 60 wt% H) | stable only below 1150 °C |
| Three-phase equilibrium at 1250 °C | α (6 wt% H), L (15 wt% H), θ (30 wt% H) |
| Three-phase equilibrium at 1150 °C | L (50 wt% H), η (60 wt% H), β (88 wt% H) |
| Three-phase equilibrium at 1000 °C | θ (30 wt% H), L (40 wt% H), η (60 wt% H) |
| Solvus lines | α holds 3 wt% H and β 92 wt% H at 700 °C |

a) Draw the phase diagram between 700 and 1600 °C to scale and label every phase field.

b) Name each invariant reaction, writing it on cooling with the compositions of the three phases, say which compound melts congruently and which incongruently, and give the maximum solubility of H in G and of G in H with their temperatures.

c) A casting of 2.00 kg of G-55 wt% H is cooled slowly. Give the mass and composition of each phase at 1150 + ΔT °C and at 1150 − ΔT °C, and the mass of β used up by the reaction at 1150 °C.

d) For the same casting at 1000 − ΔT °C, give the mass of each microconstituent and of each phase, and the masses of θ and η inside the eutectic.

## Setup

#### Data

| Symbol | Meaning | Value |
| :--- | :--- | :--- |
| $T_G$, $T_H$ | melting points of G and H | 1500 °C, 1350 °C |
| $C_\theta$, $C_\eta$ | compositions of the compounds | 30, 60 wt% H |
| 1250 °C | α, L, θ | 6, 15, 30 wt% H |
| 1150 °C | L, η, β | 50, 60, 88 wt% H |
| 1000 °C | θ, L, η | 30, 40, 60 wt% H |
| $m_0$, $C_0$ | mass and composition of the casting | 2.00 kg, 55 wt% H |

Unit conversions: 55 wt% H is a mass fraction of 0.55, so the casting contains $0.55 \times 2.00\ \text{kg} = 1.10$ kg of H and 0.90 kg of G. The lever rule gives mass fractions $W$ (dimensionless); the mass of a phase is $m_i = W_i\,m_0$ in kg.

#### Model

- **Phase fields** [Session 7 Slides 26-27]: liquidus, solidus and solvus bound the fields; single-phase and two-phase fields alternate across every boundary, and three phases meet only on a horizontal invariant line ($F = 2 - 3 + 1 = 0$, Session 7 Slide 13).
- **Invariant reactions** [Session 8 Slide 6]: eutectic $L \rightarrow \alpha + \beta$ (the liquid lies between the two solids on the line), peritectic $\alpha + L \rightarrow \beta$ (the new solid lies between the solid and the liquid) [Session 8 Slides 8-9].
- **Compounds** [Session 8 Slides 14-15, 17]: a stoichiometric compound is a vertical line; congruent melting at a maximum of the liquidus, incongruent melting at a peritectic line.
- **Lever rule** [Session 7 Slides 15-16]; primary constituent counted just above the eutectic line [Session 7 Slides 30-32].
- Hypotheses: equilibrium cooling (complete peritectic reaction), 1 atm, the boundaries between the given points drawn as smooth curves (their exact shape is not measured, only their end points).

## (a) Draw the phase diagram and label every field [0.75 pts]

### Hint

Start with the fixed points: the two melting points, the top of θ, the three horizontal lines and the two vertical compound lines. Then join each liquid point to the next with the liquidus, and each solid end to its melting point or to the bottom of the diagram.

### Checkpoint

- Liquidus: 1500 °C (0) → 1250 °C (15) → 1400 °C (30) → 1000 °C (40) → 1150 °C (50) → 1350 °C (100).
- Vertical lines: θ at 30 wt% H up to 1400 °C, η at 60 wt% H up to 1150 °C.
- Fields: L; α; α + L; α + θ; θ + L on both sides of θ; θ + η; η + L; η + β; β + L; β.

### Solution

#### Place the fixed points

On axes of 0 to 100 wt% H and 700 to 1600 °C: the melting points (0, 1500) and (100, 1350); the top of θ (30, 1400), because θ gives a liquid of its own composition there; the three horizontal lines at 1250 °C (6 to 30), 1150 °C (50 to 88) and 1000 °C (30 to 60), each with its three points marked; the vertical line of θ at 30 wt% H from 700 to 1400 °C, and that of η at 60 wt% H from 700 °C up to 1150 °C only, because η exists only below that temperature.

#### Draw the liquidus

The liquidus must pass through every liquid point of the table, in order of composition: from G (1500 °C) down to the liquid of the 1250 °C line (15), up to the maximum of θ (1400 °C at 30), down to the liquid of the 1000 °C line (40), up to the liquid of the 1150 °C line (50), and up to H (1350 °C). Above it everything is liquid.

#### Draw the solid boundaries

α: solidus from (0, 1500) to (6, 1250) and solvus from (6, 1250) to (3, 700). β: solidus from (100, 1350) to (88, 1150) and solvus from (88, 1150) to (92, 700).

#### Label the fields

Two-phase fields fill the gaps between neighbouring single-phase regions: α + L (between the α solidus and the liquidus), θ + L on each side of θ above 1250 and 1000 °C, α + θ (below 1250 °C between α and θ), θ + η (below 1000 °C), η + L (between 1000 and 1150 °C, left of η), η + β (below 1150 °C), and β + L (above 1150 °C, between the liquidus and the β solidus). Each boundary crossed horizontally changes the number of phases by one (one, two, one, two), as required.

![[attachments/MAT-MT2/p04-gh-diagram.svg]]

## (b) Invariant reactions, melting of the compounds and maximum solubilities [0.75 pts]

### Hint

For each line, ask which phase lies between the other two: if it is the liquid, the line is a eutectic; if it is a solid that exists only below the line, it is a peritectic.

### Checkpoint

- 1250 °C, eutectic: L (15) → α (6) + θ (30).
- 1150 °C, peritectic: L (50) + β (88) → η (60).
- 1000 °C, eutectic: L (40) → θ (30) + η (60).
- θ melts congruently (1400 °C); η melts incongruently (1150 °C).
- Maximum solubility: 6 wt% H in G at 1250 °C; 100 − 88 = 12 wt% G in H at 1150 °C.

### Solution

#### The line at 1250 °C

The liquid (15) lies between α (6) and θ (30), with α + L and θ + L above and α + θ below: the liquid gives two solids, a **eutectic** [Session 8 Slide 6]:

$$L\,(15) \;\xrightarrow{\;1250\ ^\circ\text{C}\;}\; \alpha\,(6) + \theta\,(30) \qquad \text{eutectic, wt\% H}$$

#### The line at 1150 °C

Here the solid η (60) lies between the liquid (50) and β (88), and η exists only below the line. Above the line there is β + L; below it η + L and η + β. A liquid and a solid combine into a new solid: a **peritectic** [Session 8 Slides 8-9]:

$$L\,(50) + \beta\,(88) \;\xrightarrow{\;1150\ ^\circ\text{C}\;}\; \eta\,(60) \qquad \text{peritectic}$$

#### The line at 1000 °C

The liquid (40) lies between θ (30) and η (60), with θ + L and η + L above and θ + η below: a second **eutectic**:

$$L\,(40) \;\xrightarrow{\;1000\ ^\circ\text{C}\;}\; \theta\,(30) + \eta\,(60) \qquad \text{eutectic}$$

#### Melting of the compounds

θ melts at 1400 °C to a liquid of 30 wt% H, its own composition, at the top of the liquidus: **congruent melting** [Session 8 Slide 17]. η ends at the peritectic line: heated above 1150 °C it decomposes into L (50) + β (88), a liquid of another composition plus another solid, so it melts **incongruently**.

#### Maximum solubilities

α is widest on the 1250 °C line: **6 wt% H in G at 1250 °C**. β is widest on the 1150 °C line, at 88 wt% H, so it holds

$$100 - 88 = 12\ \text{wt\% G}$$

at **1150 °C**. Both solubilities fall on cooling, along the solvus lines (to 3 wt% H and 8 wt% G at 700 °C).

## (c) Masses of the phases of 2.00 kg of G-55 wt% H at 1150 ± ΔT °C [0.75 pts]

### Hint

55 lies on the 1150 °C line between L (50) and β (88), and below it between L (50) and η (60). Find the fractions with the lever rule, then multiply by 2.00 kg.

### Checkpoint

- 1150 + ΔT: L (50 wt% H) 1.737 kg, β (88 wt% H) 0.263 kg.
- 1150 − ΔT: η (60 wt% H) 1.000 kg, L (50 wt% H) 1.000 kg.
- All the β, 0.263 kg, is used up by the peritectic.

### Solution

#### Derive the lever rule

On a tie line with phases L and β the mass of the alloy and the mass of H are conserved:

$$W_L + W_\beta = 1 \qquad W_L C_L + W_\beta C_\beta = C_0$$

Substituting $W_\beta = 1 - W_L$:

$$W_L C_L + (1 - W_L) C_\beta = C_0 \qquad\Rightarrow\qquad W_L (C_L - C_\beta) = C_0 - C_\beta$$

$$W_L = \frac{C_\beta - C_0}{C_\beta - C_L} \qquad W_\beta = \frac{C_0 - C_L}{C_\beta - C_L}$$

#### Just above 1150 °C

The alloy lies in β + L on the tie line from L (50) to β (88), length 38 wt% H:

$$W_L = \frac{88 - 55}{88 - 50} = \frac{33}{38} = 0.8684 \qquad W_\beta = \frac{55 - 50}{88 - 50} = \frac{5}{38} = 0.1316$$

Masses, with $m_i = W_i\,m_0$:

$$m_L = 0.8684 \times 2.00\ \text{kg} = 1.737\ \text{kg} \qquad m_\beta = 0.1316 \times 2.00\ \text{kg} = 0.263\ \text{kg}$$

#### Just below 1150 °C

At 1150 °C, L (50) and β (88) react to form η (60). The alloy (55) lies left of η, between L and η, so the β runs out first and liquid remains. Tie line from L (50) to η (60), length 10:

$$W_\eta = \frac{55 - 50}{60 - 50} = \frac{5}{10} = 0.500 \qquad W_L = \frac{60 - 55}{60 - 50} = \frac{5}{10} = 0.500$$

$$m_\eta = 0.500 \times 2.00\ \text{kg} = 1.000\ \text{kg} \qquad m_L = 0.500 \times 2.00\ \text{kg} = 1.000\ \text{kg}$$

#### Mass balance of the reaction

All 0.263 kg of β disappear. The η formed (1.000 kg) comes from that β and from $1.000 - 0.263 = 0.737$ kg of liquid, which is exactly the drop of the liquid from 1.737 to 1.000 kg. H check: $0.263 \times 0.88 + 0.737 \times 0.50 = 0.2316 + 0.3684 = 0.600$ kg of H in 1.000 kg of η, that is 60 wt% H, the composition of η.

## (d) Microconstituents and phases of the casting at 1000 − ΔT °C [0.75 pts]

### Hint

Between 1150 and 1000 °C η grows from the liquid, which moves along the liquidus to 40 wt% H. The η present just above 1000 °C is primary η; the liquid left becomes the eutectic θ + η.

### Checkpoint

- Primary η 1.500 kg; eutectic (θ + η) 0.500 kg.
- Phases: θ (30 wt% H) 0.333 kg, η (60 wt% H) 1.667 kg.
- Inside the eutectic: θ 0.333 kg and η 0.167 kg.

### Solution

#### Primary η just above 1000 °C

The tie line runs from the eutectic liquid (40) to η (60), length 20 wt% H. The η is primary and the liquid will become eutectic:

$$W_{\eta,\text{primary}} = \frac{55 - 40}{60 - 40} = \frac{15}{20} = 0.750 \qquad W_E = \frac{60 - 55}{60 - 40} = \frac{5}{20} = 0.250$$

$$m_{\eta,\text{primary}} = 0.750 \times 2.00 = 1.500\ \text{kg} \qquad m_E = 0.250 \times 2.00 = 0.500\ \text{kg}$$

#### Phases just below 1000 °C

Tie line from θ (30) to η (60), length 30:

$$W_\theta = \frac{60 - 55}{60 - 30} = \frac{5}{30} = 0.1667 \qquad W_\eta = \frac{55 - 30}{60 - 30} = \frac{25}{30} = 0.8333$$

$$m_\theta = 0.1667 \times 2.00 = 0.333\ \text{kg} \qquad m_\eta = 0.8333 \times 2.00 = 1.667\ \text{kg}$$

#### Split the eutectic

All the θ is in the eutectic (there is no primary θ), so eutectic θ = 0.333 kg. The eutectic η is the total η minus the primary η:

$$m_{\eta,E} = 1.667 - 1.500 = 0.167\ \text{kg}$$

Check: $0.333 + 0.167 = 0.500$ kg, the mass of eutectic. The eutectic has 40 wt% H, so inside it the θ fraction is $(60 - 40)/(60 - 30) = 20/30 = 0.667$, and $0.667 \times 0.500 = 0.333$ kg, as found.

## Interpretation

The two compounds split the diagram into three simpler parts: G-θ (a simple eutectic), θ-η (a simple eutectic) and η-H (a peritectic). θ behaves like a pure metal because it melts at a maximum of the liquidus; η cannot be melted as a single liquid. The casting of 55 wt% H shows the peritectic in action: the 0.263 kg of β formed first is completely consumed at 1150 °C, so the final microstructure has no trace of β, only primary η in a θ + η eutectic. Checks: every pair of fractions adds up to 1 and the masses add up to 2.00 kg; H balance at 1000 − ΔT: $0.333 \times 0.30 + 1.667 \times 0.60 = 0.100 + 1.000 = 1.100$ kg of H $= 0.55 \times 2.00$ kg. Limiting case: a casting of exactly 60 wt% H would leave no liquid after the peritectic and be 100 % η. Dimensions: $W$ is wt% over wt%, dimensionless, and $m = W\,m_0$ has units of kg. Common mistake: drawing η up to the liquidus as if it melted congruently; the table says η exists only below 1150 °C, which is the signature of a peritectic.

## Verification

- (b) solubility of G in H (wt%) | 100-88 | 12
- (c) W_L at 1150+dT | (88-55)/(88-50) | 0.8684
- (c) W_beta at 1150+dT | (55-50)/(88-50) | 0.1316
- (c) m_L at 1150+dT (kg) | (88-55)/(88-50)*2.00 | 1.737
- (c) m_beta at 1150+dT (kg) | (55-50)/(88-50)*2.00 | 0.263
- (c) m_eta at 1150-dT (kg) | (55-50)/(60-50)*2.00 | 1.000
- (c) liquid used by the peritectic (kg) | (55-50)/(60-50)*2.00 - (55-50)/(88-50)*2.00 | 0.737
- (c) H in the eta formed (kg) | (55-50)/(88-50)*2.00*0.88 + ((55-50)/(60-50)*2.00 - (55-50)/(88-50)*2.00)*0.50 | 0.600
- (d) primary eta (kg) | (55-40)/(60-40)*2.00 | 1.500
- (d) eutectic (kg) | (60-55)/(60-40)*2.00 | 0.500
- (d) m_theta (kg) | (60-55)/(60-30)*2.00 | 0.333
- (d) m_eta (kg) | (55-30)/(60-30)*2.00 | 1.667
- (d) eutectic eta (kg) | (55-30)/(60-30)*2.00 - (55-40)/(60-40)*2.00 | 0.167

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
