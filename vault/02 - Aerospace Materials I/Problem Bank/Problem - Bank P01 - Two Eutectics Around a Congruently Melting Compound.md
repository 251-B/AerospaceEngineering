---
materia: Aerospace Materials I
tema: "Unit 4: phase diagrams"
bank_id: P01
title: "Two eutectics around a congruently melting compound in a hypothetical A-B system"
category: mt2_problem
archetype: phase-diagram-invariant
level: standard
unit: 4
difficulty: 2
points: 3.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of Part II of MATERIALS_SECONDPARTIAL_2019.pdf (Ni-Nb, p. 4) and of the final of January 2017, question 4 (Ag-Sn, MATERIALS_FINALEXAM_2017_ORD.pdf, pp. 2-3); hypothetical system, not an official exercise. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - phase-diagram-invariant
  - intermetallic-compound
  - congruent-melting
  - lever-rule
---

# Bank P01 — Two eutectics around a congruently melting compound

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Part II problem of the 2019 Assessment Test II (Ni-Nb) and of the final of January 2017 (Ag-Sn). The A-B system is hypothetical. Method: Session 7, Slides 15-21 and 30-32; Session 8, Slides 6, 14-15 and 17. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

The figure shows the equilibrium phase diagram of a hypothetical binary system A-B (composition in wt% B). Every invariant temperature and the compositions of the phases on each invariant line are printed on the diagram.

![[attachments/MAT-MT2/p01-ab-diagram.svg]]

a) Determine all the invariant reactions: type of reaction, temperature and composition of every phase involved.

b) For an alloy A-50 wt% B at 700 − ΔT °C, give the phases present with their compositions and amounts, and the microconstituents present with their amounts.

c) Sketch the microstructure of an alloy A-20 wt% B at 700 + ΔT °C and at 700 − ΔT °C, labelling every microconstituent and giving its amount.

d) Indicate whether the intermetallic compound γ melts congruently or incongruently, and give the maximum solubility of B in A and of A in B, with the temperature at which each is observed.

## Setup

#### Data read on the diagram

| Item | Value read on the figure |
| :--- | :--- |
| Melting point of A | 900 °C (left axis) |
| Melting point of B | 1050 °C (right axis) |
| Compound γ | vertical line at 60 wt% B, top of the liquidus at 1150 °C |
| Invariant line at 700 °C | α 10 wt% B, L 35 wt% B, γ 60 wt% B |
| Invariant line at 850 °C | γ 60 wt% B, L 78 wt% B, β 92 wt% B |
| Alloys | $C_0$ = 50 wt% B (part b), $C_0$ = 20 wt% B (part c) |

Unit conversion: a composition in wt% is a mass fraction times 100, so 50 wt% B means 0.50 kg of B per kg of alloy. The lever rule uses the ratio of two differences of compositions, so the fractions it gives are dimensionless mass fractions whether the compositions are written in wt% or as fractions. No formula of this problem needs kelvin, so the temperatures stay in °C.

#### Model

- **Invariant reactions** [Session 8 Slide 6]: three phases coexist on a horizontal line at a fixed temperature. On cooling, eutectic $L \rightarrow \alpha + \beta$ (a liquid field ends in a V on the line), peritectic $\alpha + L \rightarrow \beta$ (a solid field ends in an inverted V below the line), eutectoid $\gamma \rightarrow \alpha + \beta$ and peritectoid $\alpha + \beta \rightarrow \gamma$ in the solid state.
- **Tie line and lever rule** [Session 7 Slides 15-16]: in a two-phase field, the horizontal line through the alloy point gives the compositions of the two phases at its ends; each phase takes the arm on the side of the other phase, divided by the length of the tie line.
- **Microconstituents** [Session 7 Slides 30-32]: the primary (proeutectic) constituent is counted on the tie line just above the eutectic temperature, where the remaining liquid has the eutectic composition and becomes the eutectic; the total phases are counted on the tie line just below it.
- **Intermetallic compounds and melting** [Session 8 Slides 14-15, 17]: a stoichiometric compound is a vertical line; it melts congruently when it sits at a maximum of the liquidus (the liquid keeps its composition) and incongruently when it ends at a peritectic line.
- Hypotheses: equilibrium cooling, pressure fixed at 1 atm, values read on the figure as printed.

## (a) Determine all the invariant reactions, with their type, temperature and the composition of every phase [0.75 pts]

### Hint

Look for the horizontal lines: each one joins three phases. Decide the type from the field that lies above the line and the shape of the boundaries that meet it.

### Checkpoint

- 700 °C, eutectic: L (35 wt% B) → α (10 wt% B) + γ (60 wt% B).
- 850 °C, eutectic: L (78 wt% B) → γ (60 wt% B) + β (92 wt% B).
- The maximum of γ at 1150 °C is a congruent melting point, not a three-phase reaction.

### Solution

#### Find the three-phase lines on the diagram

The diagram has two horizontal lines, at 700 °C (from 10 to 60 wt% B) and at 850 °C (from 60 to 92 wt% B). By the Gibbs phase rule at constant pressure, $F = C - P + 1$ [Session 7 Slide 13], three phases in a two-component system leave $F = 2 - 3 + 1 = 0$, so a three-phase equilibrium can only appear as a horizontal line at one temperature with three fixed compositions. Those are the invariant reactions [Session 8 Slide 6].

#### Classify the line at 700 °C

Above the line, between 10 and 60 wt% B, there are two fields, α + L and γ + L, whose liquidus branches fall from 900 °C (pure A) and from 1150 °C (γ) and meet in a V at 35 wt% B on the line. Below the line there is the single two-solid field α + γ. A liquid that ends in a V on the line and gives two solids below it is a **eutectic** [Session 8 Slide 6]. Reading the three points on the figure, on cooling:

$$L\,(35\ \text{wt\% B}) \;\xrightarrow{\;700\ ^\circ\text{C}\;}\; \alpha\,(10\ \text{wt\% B}) + \gamma\,(60\ \text{wt\% B}) \qquad \text{eutectic}$$

#### Classify the line at 850 °C

Between 60 and 92 wt% B the liquidus falls from the maximum of γ (1150 °C) and from the melting point of B (1050 °C) to a V at 78 wt% B on the line; below the line lies γ + β. Again a liquid gives two solids, so this is a second **eutectic**:

$$L\,(78\ \text{wt\% B}) \;\xrightarrow{\;850\ ^\circ\text{C}\;}\; \gamma\,(60\ \text{wt\% B}) + \beta\,(92\ \text{wt\% B}) \qquad \text{eutectic}$$

#### Check that no other point is invariant

The melting points of A (900 °C) and B (1050 °C) and the maximum of γ (1150 °C) are points where one solid melts to a liquid of its own composition; they behave as one-component transformations ($F = 1 - 2 + 1 = 0$ with the composition fixed) and involve two phases, not three, so they are not invariant reactions of the binary system. Each eutectic temperature lies below the melting points of its two neighbouring solids (700 < 900 and 700 < 1150; 850 < 1150 and 850 < 1050), as a eutectic must.

## (b) Phases and microconstituents of A-50 wt% B at 700 − ΔT °C [0.75 pts]

### Hint

Phases: tie line just below 700 °C, from α to γ. Microconstituents: tie line just above 700 °C, from the eutectic liquid to γ, because the primary γ forms before the eutectic.

### Checkpoint

- Phases at 700 − ΔT °C: α (10 wt% B) 0.200 and γ (60 wt% B) 0.800.
- Microconstituents: primary γ 0.600 and eutectic (α + γ) 0.400.
- Inside the eutectic: eutectic α 0.200 and eutectic γ 0.200 of the alloy.

### Solution

#### Locate the alloy and derive the lever rule

The alloy, 50 wt% B, lies between the eutectic composition (35) and γ (60), so on cooling it first crosses the γ liquidus and forms primary γ. Just below 700 °C it lies in the α + γ field. On a tie line with phases α and γ the two mass balances are, for the alloy and for B [Session 7 Slide 16]:

$$W_\alpha + W_\gamma = 1 \qquad W_\alpha C_\alpha + W_\gamma C_\gamma = C_0$$

Substituting $W_\gamma = 1 - W_\alpha$ in the second balance:

$$W_\alpha C_\alpha + (1 - W_\alpha) C_\gamma = C_0$$

$$W_\alpha (C_\alpha - C_\gamma) = C_0 - C_\gamma$$

Dividing by $(C_\alpha - C_\gamma)$ and changing the sign of numerator and denominator:

$$W_\alpha = \frac{C_\gamma - C_0}{C_\gamma - C_\alpha} \qquad W_\gamma = 1 - W_\alpha = \frac{C_0 - C_\alpha}{C_\gamma - C_\alpha}$$

This is the lever rule: each phase takes the arm on the side of the other phase.

#### Apply it to the phases just below 700 °C

Tie line read on the figure: $C_\alpha$ = 10 wt% B, $C_\gamma$ = 60 wt% B, length 60 − 10 = 50 wt% B.

$$W_\alpha = \frac{60 - 50}{60 - 10} = \frac{10}{50} = 0.200 \qquad W_\gamma = \frac{50 - 10}{60 - 10} = \frac{40}{50} = 0.800$$

#### Count the microconstituents on the tie line just above 700 °C

Just above 700 °C the alloy is γ (60 wt% B) + liquid that has reached the eutectic composition, 35 wt% B. All that liquid becomes eutectic at 700 °C, and the γ already present stays as primary γ. The same lever rule on the tie line from L (35) to γ (60), length 25 wt% B:

$$W_{\gamma,\text{primary}} = \frac{C_0 - C_E}{C_\gamma - C_E} = \frac{50 - 35}{60 - 35} = \frac{15}{25} = 0.600 \qquad W_{E} = W_{L}(700 + \Delta T) = \frac{60 - 50}{60 - 35} = \frac{10}{25} = 0.400$$

#### Split the eutectic into its phases

All the α of the alloy is inside the eutectic (there is no primary α), so eutectic α = $W_\alpha$ = 0.200. The γ inside the eutectic is the total γ minus the primary γ:

$$W_{\gamma,\text{eutectic}} = W_\gamma - W_{\gamma,\text{primary}} = 0.800 - 0.600 = 0.200$$

Check: $0.200 + 0.200 = 0.400 = W_E$. The eutectic itself has the composition 35 wt% B, so inside it the fraction of α is $(60 - 35)/(60 - 10) = 25/50 = 0.500$, and $0.500 \times 0.400 = 0.200$, the same eutectic α.

#### Answer and checks

At 700 − ΔT °C: phases α (10 wt% B, 20.0 %) and γ (60 wt% B, 80.0 %); microconstituents primary γ (60.0 %) and eutectic α + γ (40.0 %). B balance: $0.200 \times 10 + 0.800 \times 60 = 2 + 48 = 50$ wt% B $= C_0$.

## (c) Sketch the microstructure of A-20 wt% B at 700 + ΔT and 700 − ΔT °C [0.75 pts]

### Hint

20 wt% B is hypoeutectic (between 10 and 35): primary α forms first. Above the line the second constituent is still liquid; below it, that liquid has become eutectic.

### Checkpoint

- 700 + ΔT °C: primary α (10 wt% B) 0.600 in liquid (35 wt% B) 0.400.
- 700 − ΔT °C: primary α 0.600 in eutectic α + γ 0.400; total phases α 0.800 and γ 0.200.

### Solution

#### Follow the cooling path to the eutectic line

The vertical line of 20 wt% B crosses the α liquidus (at about 830 °C, a reading of the figure): grains of primary α nucleate and grow, while the liquid becomes richer in B along the liquidus. Just above 700 °C the α has 10 wt% B and the liquid 35 wt% B, the eutectic composition [Session 7 Slides 30-31].

#### Amounts at 700 + ΔT °C

Lever rule derived in part (b), on the tie line from α (10) to L (35), length 25 wt% B:

$$W_\alpha = \frac{35 - 20}{35 - 10} = \frac{15}{25} = 0.600 \qquad W_L = \frac{20 - 10}{35 - 10} = \frac{10}{25} = 0.400$$

#### Amounts at 700 − ΔT °C

At 700 °C the liquid (0.400) transforms at constant temperature into the eutectic $L \rightarrow \alpha + \gamma$; the primary α (0.600) does not change. The total phases come from the tie line from α (10) to γ (60), length 50:

$$W_\alpha = \frac{60 - 20}{60 - 10} = \frac{40}{50} = 0.800 \qquad W_\gamma = \frac{20 - 10}{60 - 10} = \frac{10}{50} = 0.200$$

The eutectic holds all the γ (0.200) and $0.800 - 0.600 = 0.200$ of α, and $0.200 + 0.200 = 0.400$, the eutectic fraction.

#### The sketches

Left: rounded grains of primary α (60 %) surrounded by liquid. Right: the same α grains, now surrounded by a lamellar eutectic of alternating α and γ layers (40 %).

![[attachments/MAT-MT2/p01-sketches.svg]]

## (d) Melting of γ and maximum solubilities [0.75 pts]

### Hint

A compound at the top of a liquidus dome melts like a pure metal. The maximum solubility of a terminal solid solution is the end of its field on an invariant line.

### Checkpoint

- γ melts congruently at 1150 °C (maximum of the liquidus).
- Maximum solubility of B in A (α): 10 wt% B at 700 °C.
- Maximum solubility of A in B (β): 100 − 92 = 8 wt% A at 850 °C.

### Solution

#### Classify the melting of γ

The vertical line of γ (60 wt% B) reaches the liquidus at its maximum, 1150 °C: heated to that point, γ gives a liquid of 60 wt% B, its own composition, and no other solid appears. By Session 8 Slide 17 that is **congruent melting**. Had γ ended at a horizontal peritectic line below the liquidus, it would decompose into a liquid plus another solid (incongruent melting); this diagram has no peritectic line.

#### Maximum solubility of B in A

The α field is bounded by the solidus (from 900 °C) and the solvus (down to 200 °C); both meet the eutectic line at 10 wt% B, the widest point of the field. So α dissolves at most **10 wt% B, at 700 °C**; below 700 °C the solvus moves back towards A and the solubility falls.

#### Maximum solubility of A in B

The β field is widest where its boundaries meet the 850 °C line, at 92 wt% B, so β holds at most

$$100 - 92 = 8\ \text{wt\% A}$$

at **850 °C**.

## Interpretation

The compound γ splits the diagram into two simple eutectic sub-systems, A-γ and γ-B, each read exactly like Pb-Sn: a hypoeutectic alloy of the A-γ side (20 wt% B) gives primary α in an α + γ eutectic, a hypereutectic one (50 wt% B) gives primary γ. Control cases of the lever rule: as $C_0 \to 35$ wt% B the primary γ of part (b) tends to $(35-35)/25 = 0$ and the alloy becomes 100 % eutectic; as $C_0 \to 60$ it tends to 1. All fractions lie between 0 and 1 and add up to 1. Dimensions: the lever rule is a ratio of compositions (wt% over wt%), so every fraction is dimensionless, as a mass fraction must be. A common exam mistake is to give the primary γ from the tie line below 700 °C ($W_\gamma$ = 0.800): that number is the total γ, which also contains the γ inside the eutectic.

## Verification

- (b) W_alpha below 700 C | (60-50)/(60-10) | 0.200
- (b) W_gamma below 700 C | (50-10)/(60-10) | 0.800
- (b) primary gamma | (50-35)/(60-35) | 0.600
- (b) eutectic | (60-50)/(60-35) | 0.400
- (b) eutectic gamma | (50-10)/(60-10) - (50-35)/(60-35) | 0.200
- (c) W_alpha at 700+dT | (35-20)/(35-10) | 0.600
- (c) W_L at 700+dT | (20-10)/(35-10) | 0.400
- (c) W_alpha below 700 C | (60-20)/(60-10) | 0.800
- (c) W_gamma below 700 C | (20-10)/(60-10) | 0.200
- (d) solubility of A in B (wt%) | 100-92 | 8

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
