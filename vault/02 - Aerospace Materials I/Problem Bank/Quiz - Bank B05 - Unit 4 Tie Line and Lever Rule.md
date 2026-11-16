---
materia: Aerospace Materials I
tema: "Unit 4: tie line and lever rule in isomorphous systems"
bank_id: B05
title: "Tie line and lever rule"
category: mt2_test_block
unit: 4
concepts:
  - u4-tie-line-compositions
  - u4-lever-rule-cooling-path
  - u4-lever-rule-masses
  - u4-lever-rule-inverse
  - u4-lever-rule-limits
  - u4-lever-rule-mass-balance
  - u4-lever-rule-basis
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 7 Slides 13-23."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-4
---

# Bank B05 — Tie line and lever rule

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 7, Slides 13-23.

## Q05.1 Two alloys on the same tie line

- id: B05-Q1
- concept_id: u4-tie-line-compositions
- format: what-happens
- asks: comparison

Two Cu-Ni alloys, of 32 and 40 wt% Ni, are held at the same temperature inside α + L. What will happen to their phases:

a) Same phase compositions, different phase amounts
b) Same phase amounts, different phase compositions
c) Same phase compositions and same phase amounts
d) Different phase compositions and different phase amounts

### Answer

a

### Explanation

At a given temperature in α + L, $F = 1$ has been used by the temperature, so the compositions of α and L are the ends of the same tie line for every alloy (Session 7, Slides 13 and 15). Changing the overall composition only moves the alloy point along the tie line and changes the amounts given by the lever rule (Slide 16).

- b) Swapped: the compositions are the ones fixed by the tie line, the amounts are the ones that change.
- c) Equal amounts would need equal overall compositions; the alloy points sit at different places on the lever.
- d) The phase compositions do not depend on the alloy at fixed temperature, since $F = 1$ in a two-phase field.

### Source

Session 7, Slides 13 and 15-16.

## Q05.2 Liquid fraction at point c-prime

- id: B05-Q2
- concept_id: u4-lever-rule-cooling-path
- format: numeric
- asks: calculation
- calc: (40-33)/(40-29)*100

At the temperature of point c′ of the Cu-Ni diagram the tie line runs from $C_L = 29$ to $C_\alpha = 40$ wt% Ni. Determine the mass percentage of liquid in a Cu-33 wt% Ni alloy at that temperature:

a) 36.4 %
b) 63.6 %
c) 82.5 %
d) 87.9 %

### Answer

b

### Explanation

Lever rule (Session 7, Slide 16): $W_L = \dfrac{C_\alpha - C_0}{C_\alpha - C_L} = \dfrac{40 - 33}{40 - 29} = \dfrac{7}{11} = 0.636$.

- a) $(33 - 29)/(40 - 29) = 0.364$ is the fraction of α: the arm on the side of the liquid itself was used (arms swapped).
- c) $33/40 = 0.825$ divides the alloy composition by that of α, a ratio of compositions and not a mass balance.
- d) $29/33 = 0.879$ divides the liquid composition by the alloy composition, again a ratio of compositions.

### Source

Session 7, Slides 16 and 23 (tie line at c′: 29 and 40 wt% Ni).

## Q05.3 Mass of alpha in a 5 kg casting

- id: B05-Q3
- concept_id: u4-lever-rule-masses
- format: numeric
- asks: calculation
- calc: 5*(38-32)/(43-32)

A 5 kg Cu-38 wt% Ni casting is held where the tie line gives $C_L = 32$ and $C_\alpha = 43$ wt% Ni. Determine the mass of α:

a) 1.90 kg
b) 2.27 kg
c) 2.73 kg
d) 4.42 kg

### Answer

c

### Explanation

Lever rule (Session 7, Slide 16): $W_\alpha = \dfrac{C_0 - C_L}{C_\alpha - C_L} = \dfrac{38 - 32}{43 - 32} = 0.545$, so $m_\alpha = 0.545 \times 5 = 2.73$ kg.

- a) $0.38 \times 5 = 1.90$ kg takes the alloy composition as the fraction of α.
- b) $5 \times (43 - 38)/(43 - 32) = 2.27$ kg is the mass of liquid: the arms were swapped.
- d) $5 \times 38/43 = 4.42$ kg uses a ratio of compositions instead of the lever.

### Source

Session 7, Slides 16-17.

## Q05.4 Alloy composition from the phase amounts

- id: B05-Q4
- concept_id: u4-lever-rule-inverse
- format: numeric
- asks: calculation
- calc: 20+0.75*(50-20)

At some temperature an A-B alloy is 75 % α of 50 wt% B and 25 % liquid of 20 wt% B. Determine the composition of the alloy:

a) 27.5 wt% B
b) 35.0 wt% B
c) 37.5 wt% B
d) 42.5 wt% B

### Answer

d

### Explanation

The lever rule solved for $C_0$ (Session 7, Slides 16 and 21): $W_\alpha = (C_0 - C_L)/(C_\alpha - C_L)$ gives $C_0 = C_L + W_\alpha (C_\alpha - C_L) = 20 + 0.75 \times 30 = 42.5$ wt% B; the same as the mass balance $0.75 \times 50 + 0.25 \times 20$.

- a) $20 + 0.25 \times 30 = 27.5$ uses the fraction of liquid in place of that of α: arms swapped.
- b) $(20 + 50)/2 = 35.0$ is the plain average of the two phase compositions, ignoring their amounts.
- c) $0.75 \times 50 = 37.5$ counts only the B inside α and forgets the B in the liquid.

### Source

Session 7, Slides 16 and 21.

## Q05.5 Moving the alloy towards the liquidus

- id: B05-Q5
- concept_id: u4-lever-rule-limits
- format: cause-effect
- asks: effect

On a fixed tie line, as the alloy composition approaches the liquidus end, the fraction of liquid:

a) Increases, and reaches 1 at the liquidus end
b) Decreases, and reaches 0 at the liquidus end
c) Increases, but never exceeds 0.5
d) Stays constant, because the phase compositions are fixed

### Answer

a

### Explanation

$W_L = (C_\alpha - C_0)/(C_\alpha - C_L)$ (Session 7, Slide 16): the arm opposite the liquid grows as $C_0$ approaches $C_L$, and at $C_0 = C_L$ it equals the whole tie line, $W_L = 1$ (as at point b′ of Slide 23).

- b) Inverted trend: the phase whose boundary the alloy approaches becomes more abundant, not less.
- c) There is no limit at 0.5; the fraction runs from 0 at one end of the tie line to 1 at the other.
- d) The compositions are fixed, but the amounts change with the position of the alloy on the lever.

### Source

Session 7, Slides 16 and 23.

## Q05.6 Lever rule along the cooling of Cu-35 Ni

- id: B05-Q6
- concept_id: u4-lever-rule-limits
- format: true-statement
- asks: application

Which one of the following statements about a Cu-35 wt% Ni alloy cooled in equilibrium is TRUE:

a) At the solidus temperature the liquid fraction is 1
b) The amount of solid decreases as the temperature falls
c) Halfway between liquidus and solidus the liquid fraction is always 0.5
d) At the liquidus temperature the liquid fraction is 1

### Answer

d

### Explanation

Session 7, Slide 23: at b′ (liquidus) the tie line runs from 35 to 46 wt% Ni and $W_L = (46 - 35)/(46 - 35) = 1$; at c′ $W_L = 0.455$; at d′ (solidus) $W_L = (35 - 35)/(35 - 24) = 0$.

- a) Swapped limits: at the solidus the last liquid disappears, $W_L = 0$.
- b) Inverted trend: the solid grows from 0 to 1 as the temperature falls.
- c) The fraction depends on the tie-line compositions, not on the temperature midpoint; at c′ it is 0.455, not 0.5.

### Source

Session 7, Slide 23.

## Q05.7 Checking a lever-rule result

- id: B05-Q7
- concept_id: u4-lever-rule-mass-balance
- format: complete-sentence
- asks: application

A lever-rule result is checked because the sum of each phase fraction times its composition must equal:

a) 100 wt% of the solute
b) The length of the tie line
c) The overall composition of the alloy
d) The eutectic composition of the system

### Answer

c

### Explanation

The lever rule is a mass balance of the solute: $W_L C_L + W_\alpha C_\alpha = C_0$ (with $W_L + W_\alpha = 1$). For the slide example, $0.727 \times 32 + 0.273 \times 43 = 35.0$ wt% Ni $= C_0$ (Session 7, Slides 16-21).

- a) 100 % is the sum of the fractions themselves, $W_L + W_\alpha = 1$, not of the fractions times the compositions.
- b) The tie-line length is the denominator of the rule, not the result of the balance.
- d) The eutectic composition has nothing to do with an isomorphous tie line; the balance returns the alloy composition.

### Source

Session 7, Slides 16-21.

## Q05.8 What kind of fraction the lever rule gives

- id: B05-Q8
- concept_id: u4-lever-rule-basis
- format: identify
- asks: definition

Applied on a diagram whose composition axis is in wt%, the lever rule gives:

a) Volume fractions of the phases
b) Atom fractions of the phases
c) Area fractions seen in the micrograph
d) Mass fractions of the phases

### Answer

d

### Explanation

Session 7, Slide 16 writes $W_L$ and $W_\alpha$, mass fractions, because the composition axis is in weight percent: the balance is a balance of masses. On an atomic % axis the same construction would give atom fractions.

- a) Volume fractions would also need the densities of the phases, which the diagram does not give.
- b) Atom fractions come out only when the axis is in atomic %, not in wt%.
- c) Area fractions on a micrograph estimate volume, not mass; the lever rule does not give them.

### Source

Session 7, Slides 16-21.

## Q05.9 Mass of liquid read on the diagram

- id: B05-Q9
- concept_id: u4-lever-rule-masses
- format: diagram-reading
- asks: calculation
- check: abs(2*(55-40)/(55-30) - 1.20) < 0.005

From the shown A-B phase diagram, indicate the mass of liquid in 2 kg of the alloy marked $C_0$ at 1200 °C:

![[attachments/MAT-MT2/u4-iso-ab.svg]]

a) 1.20 kg
b) 0.80 kg
c) 1.45 kg
d) 2.00 kg

### Answer

a

### Explanation

The tie line at 1200 °C runs from 30 (liquidus) to 55 wt% B (solidus) through $C_0 = 40$ (Session 7, Slides 15-16): $W_L = (55 - 40)/(55 - 30) = 0.600$, and $0.600 \times 2 = 1.20$ kg.

- b) $2 \times (40 - 30)/(55 - 30) = 0.80$ kg is the mass of α: the arms were swapped.
- c) $2 \times 40/55 = 1.45$ kg is a ratio of compositions, not a lever.
- d) 2.00 kg assumes the alloy is all liquid, reading 1200 °C as above the liquidus of the alloy (1250 °C).

### Source

Session 7, Slides 15-16.

## Q05.10 Equal amounts of the two phases

- id: B05-Q10
- concept_id: u4-lever-rule-inverse
- format: complete-sentence
- asks: application
- check: 30 + 0.5*(55-30) == 42.5

On a tie line from 30 wt% B (liquid) to 55 wt% B (α), the alloy that contains equal masses of liquid and α has:

a) 12.5 wt% B
b) 42.5 wt% B
c) 50.0 wt% B
d) 55.0 wt% B

### Answer

b

### Explanation

With $W_L = W_\alpha = 0.5$ the alloy sits at the middle of the tie line (Session 7, Slide 16): $C_0 = 30 + 0.5 \times (55 - 30) = 42.5$ wt% B.

- a) 12.5 is half the length of the tie line, $25/2$, without adding it to the liquid end at 30 wt% B.
- c) 50.0 wt% takes "50 % of each phase" as the composition of the alloy, confusing an amount with a composition.
- d) 55.0 wt% B is the α end of the tie line, where the alloy would be all α.

### Source

Session 7, Slide 16.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
