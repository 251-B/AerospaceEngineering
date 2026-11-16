---
materia: Aerospace Materials I
tema: "Unit 4: degrees of freedom, invariant points, tie line and lever rule"
bank_id: B04
title: "Gibbs phase rule and tie lines"
category: mt2_test_block
unit: 4
concepts:
  - u4-gibbs-rule-unary
  - u4-gibbs-rule-binary
  - u4-gibbs-invariant
  - u4-tie-line-compositions
  - u4-lever-rule-isomorphous
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 7 Slides 13-17, 27 and 32."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-4
---

# Bank B04 — Gibbs phase rule and tie lines

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 7, Slides 13-17, 27 and 32.

## Q04.1 One degree of freedom on a P-T diagram

- id: B04-Q1
- concept_id: u4-gibbs-rule-unary
- format: diagram-reading
- asks: figure-reading

On the P-T diagram below, at which numbered point can only one of the two variables, T or P, be chosen freely?

![[attachments/MAT-MT2/u4-unary-pt.svg]]

a) At 1
b) At 2
c) At 3
d) At 4

### Answer

b

### Explanation

With one component and $N = 2$, $F = 1 - P + 2$ (Session 7, Slide 13). Point 2 lies on the melting line, where solid and liquid coexist: $F = 1 - 2 + 2 = 1$.

- a) Point 1 lies inside the liquid region: one phase, $F = 1 - 1 + 2 = 2$.
- c) Point 3 is the triple point: three phases, $F = 1 - 3 + 2 = 0$.
- d) Point 4 lies inside the solid region: one phase, $F = 2$, like point 1.

### Source

Session 7, Slides 5 and 13.

## Q04.2 Degrees of freedom of a unary system

- id: B04-Q2
- concept_id: u4-gibbs-rule-unary
- format: true-statement
- asks: comparison

Which one of the following statements about a one-component system with P and T free is TRUE:

a) At its triple point it has zero degrees of freedom
b) Inside a single-phase region it has one degree of freedom
c) On a two-phase line it has two degrees of freedom
d) At its triple point it has one degree of freedom

### Answer

a

### Explanation

Session 7, Slide 13 (water): $F = 1 - P + 2$ gives $F = 2$ in a single-phase region, $F = 1$ on a two-phase line and $F = 0$ at the triple point, where three phases coexist at one temperature and one pressure.

- b) In a single-phase region $F = 1 - 1 + 2 = 2$: temperature and pressure can both change.
- c) On a two-phase line $F = 1 - 2 + 2 = 1$; the values of b) and c) have been swapped.
- d) One degree of freedom belongs to a two-phase line; the triple point has $F = 1 - 3 + 2 = 0$.

### Source

Session 7, Slide 13.

## Q04.3 Fixing the temperature in alpha plus liquid

- id: B04-Q3
- concept_id: u4-gibbs-rule-binary
- format: what-happens
- asks: application

A binary alloy at 1 atm lies inside the α + L region of its diagram. What will happen to the phases if the temperature is fixed:

a) Their compositions can still be chosen freely
b) The alloy must become a single phase
c) A third phase appears in equilibrium
d) Their compositions become fixed by the diagram

### Answer

d

### Explanation

In α + L at constant pressure $F = 2 - 2 + 1 = 1$ (Session 7, Slide 13). Choosing the temperature uses that single degree of freedom, so the compositions of α and L are fixed: they are the ends of the tie line at that temperature (Session 7, Slides 15-16). Changing the alloy composition only changes the amounts.

- a) Free compositions would need $F = 2$, which holds only in a single-phase field.
- b) Fixing the temperature does not remove a phase; the alloy stays in the two-phase field.
- c) A third phase would need $F = 0$, which only happens at an invariant temperature, not at any chosen one.

### Source

Session 7, Slides 13 and 15-16.

## Q04.4 A wrong count of degrees of freedom

- id: B04-Q4
- concept_id: u4-gibbs-rule-binary
- format: false-statement
- asks: calculation

Which one of the following statements about a binary system at 1 atm is FALSE:

a) In a two-phase field F = 2
b) In a single-phase field F = 2
c) At the melting point of a pure component F = 0
d) At a eutectic point F = 0

### Answer

a

### Explanation

Statement a) is false: in a two-phase field $F = C - P + 1 = 2 - 2 + 1 = 1$ (Session 7, Slide 13).

- b) True: one phase gives $F = 2 - 1 + 1 = 2$; temperature and composition can both change.
- c) True: at the end of the axis there is one component with two phases, $F = 1 - 2 + 1 = 0$, which is why a pure metal melts at a fixed temperature.
- d) True: three phases (L, α, β) in a two-component system give $F = 2 - 3 + 1 = 0$.

### Source

Session 7, Slides 13 and 27.

## Q04.5 Zero degrees of freedom

- id: B04-Q5
- concept_id: u4-gibbs-invariant
- format: identify
- asks: classification

In a binary system at constant pressure, which situation has zero degrees of freedom:

a) Liquid and one solid solution in equilibrium
b) A single solid solution
c) Three phases at an invariant reaction
d) Two solid phases below the eutectic line

### Answer

c

### Explanation

With $C = 2$ and $N = 1$, $F = 3 - P$ (Session 7, Slide 13); $F = 0$ needs three phases, as at the invariant reactions (Session 8, Slide 6), where temperature and compositions are all fixed.

- a) Two phases give $F = 1$: the field L + solid exists over a range of temperatures.
- b) A single phase gives $F = 2 - 1 + 1 = 2$: temperature and composition are both free.
- d) α + β below the eutectic line is a two-phase field with $F = 1$, not an invariant point.

### Source

Session 7, Slide 13; Session 8, Slide 6.

## Q04.6 The eutectic on the cooling curve

- id: B04-Q6
- concept_id: u4-gibbs-invariant
- format: complete-sentence
- asks: effect

On the cooling curve of a Pb-61.9 wt% Sn alloy, the reaction at 183 °C appears as:

a) A change of slope only
b) A sudden drop of temperature
c) Two plateaus at different temperatures
d) A plateau at constant temperature

### Answer

d

### Explanation

61.9 wt% Sn is the eutectic composition: the liquid transforms into α + β at 183 °C, an invariant reaction ($F = 0$), so its cooling curve is "similar to that of a pure solid", with a single plateau (Session 7, Slide 27).

- a) A change of slope marks a reaction that runs over a range of temperatures, such as the start of solidification of a non-eutectic alloy.
- b) The latent heat of the reaction stops the temperature from falling; it does not make it drop.
- c) Two plateaus would need two invariant reactions; the eutectic alloy has only one, at 183 °C.

### Source

Session 7, Slides 27-28.

## Q04.7 Composition of the liquid on a tie line

- id: B04-Q7
- concept_id: u4-tie-line-compositions
- format: diagram-reading
- asks: figure-reading

From the shown A-B phase diagram, indicate the composition of the liquid in the 40 wt% B alloy at 1200 °C:

![[attachments/MAT-MT2/u4-iso-ab.svg]]

a) 30 wt% B
b) 40 wt% B
c) 55 wt% B
d) 70 wt% B

### Answer

a

### Explanation

The tie line at 1200 °C crosses α + L; its end on the liquidus gives the composition of the liquid, 30 wt% B (Session 7, Slide 15).

- b) 40 wt% B is the overall composition of the alloy, not that of either phase.
- c) 55 wt% B is the end on the solidus: the composition of α.
- d) 70 wt% is the A content of the liquid ($100 - 30$), read as wt% of the other component.

### Source

Session 7, Slide 15.

## Q04.8 What a tie line is

- id: B04-Q8
- concept_id: u4-tie-line-compositions
- format: true-statement
- asks: definition

Which one of the following statements about the tie line is TRUE:

a) Its two ends give the amounts of the two phases
b) It is drawn at constant composition through the alloy
c) It is used in single-phase regions to find two compositions
d) It is drawn at constant temperature across a two-phase region

### Answer

d

### Explanation

Session 7, Slide 15: the tie line is a horizontal (constant temperature) line drawn through the alloy point across a two-phase region; its intersections with the boundaries give the compositions of the two phases.

- a) The ends give compositions; the amounts come from the lever rule, the other tool of the same slide.
- b) The line at constant composition is the vertical line of the alloy, not the tie line.
- c) In a single-phase region the phase has the composition of the alloy; no tie line is needed.

### Source

Session 7, Slide 15.

## Q04.9 Fraction of alpha on a tie line

- id: B04-Q9
- concept_id: u4-lever-rule-isomorphous
- format: numeric
- asks: calculation
- calc: (40-30)/(55-30)*100

A 40 wt% B alloy at 1200 °C contains liquid of 30 wt% B and α of 55 wt% B. Determine the mass percentage of α:

a) 18.2 %
b) 40.0 %
c) 60.0 %
d) 72.7 %

### Answer

b

### Explanation

Lever rule (Session 7, Slide 16): $W_\alpha = \dfrac{C_0 - C_L}{C_\alpha - C_L} = \dfrac{40 - 30}{55 - 30} = 0.400$.

- a) $(40 - 30)/55 = 0.182$ divides the right arm by the composition of α instead of by the whole tie line.
- c) $(55 - 40)/(55 - 30) = 0.600$ uses the arm on the side of α itself: arms swapped, this is the fraction of liquid.
- d) $40/55 = 0.727$ is a ratio of compositions, not a mass balance.

### Source

Session 7, Slides 15-17.

## Q04.10 Statement of the lever rule

- id: B04-Q10
- concept_id: u4-lever-rule-isomorphous
- format: complete-sentence
- asks: definition

In the lever rule, the mass fraction of a phase equals:

a) The arm on its own side divided by the whole tie line
b) The ratio of the two arms of the tie line
c) The arm on the side of the other phase divided by the whole tie line
d) The composition of the phase divided by the alloy composition

### Answer

c

### Explanation

Session 7, Slide 16: the fraction of each phase is the length of the tie line from the alloy composition to the boundary of the other phase, divided by the total length of the tie line, $W_L = S/(R + S)$.

- a) Taking the arm on the phase's own side swaps the arms and gives the fraction of the other phase.
- b) The ratio of the arms, $R/S$, is the ratio of the amounts of the two phases, not a fraction of the whole.
- d) A ratio of compositions is not a mass balance and does not give the amount of a phase.

### Source

Session 7, Slide 16.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
