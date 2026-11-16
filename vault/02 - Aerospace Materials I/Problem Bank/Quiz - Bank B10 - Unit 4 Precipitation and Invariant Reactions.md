---
materia: Aerospace Materials I
tema: "Unit 4: solvus and solid-state precipitation; eutectoid and peritectic reactions"
bank_id: B10
title: "Precipitation and invariant reactions"
category: mt2_test_block
unit: 4
concepts:
  - u4-solvus-precipitation
  - u4-precipitation-alloys
  - u4-precipitation-location
  - u4-eutectoid-reaction
  - u4-peritectic-reaction
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 8 Slides 2-10 (Pb-Sn precipitation, Fe-Ni peritectic at 1517 °C) and a hypothetical eutectoid diagram."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-4
---

# Bank B10 — Precipitation and invariant reactions

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 8, Slides 2-10.

## Q10.1 Beta precipitated at 121 °C

- id: B10-Q1
- concept_id: u4-solvus-precipitation
- format: numeric
- asks: calculation
- calc: (12-6)/(99-6)*100

A Pb-12 wt% Sn alloy is held at 121 °C, where the solvus of α is at 6 wt% Sn and β contains 99 wt% Sn. Determine the mass percentage of precipitated β:

a) 6.06 %
b) 6.45 %
c) 12.1 %
d) 93.5 %

### Answer

b

### Explanation

Below the solvus the alloy is α + β, and the lever rule on the tie line from 6 to 99 wt% Sn (Session 7, Slide 16; Session 8, Slide 4) gives $W_\beta = \dfrac{12 - 6}{99 - 6} = \dfrac{6}{93} = 0.0645$.

- a) $6/99 = 0.0606$ divides by the β composition instead of by the whole tie line.
- c) $12/99 = 0.121$ is a ratio of compositions, not a mass balance.
- d) $(99 - 12)/93 = 0.935$ is the fraction of α: arms swapped.

### Source

Session 8, Slide 4 (readings at 121 °C: solvus near 6 wt% Sn, β near 99 wt% Sn); Session 7, Slide 16.

## Q10.2 What the solvus separates

- id: B10-Q2
- concept_id: u4-solvus-precipitation
- format: true-statement
- asks: definition

Which one of the following statements about the solvus line is TRUE:

a) Above it the alloy is liquid
b) Crossing it on cooling dissolves the β particles
c) It is a horizontal line at the eutectic temperature
d) It separates α from α + β in the solid state

### Answer

d

### Explanation

Session 7, Slide 26 and Session 8, Slide 3: the solvus gives the maximum solubility of B in α at each temperature in the solid state; it separates the single-phase α field from α + β, and crossing it on cooling makes β precipitate.

- a) The line above which the alloy is liquid is the liquidus.
- b) Inverted: crossing the solvus on cooling exceeds the solubility and β forms; β dissolves on heating.
- c) The horizontal line is the eutectic isotherm; the solvus is a curve whose composition changes with temperature.

### Source

Session 7, Slide 26; Session 8, Slide 3.

## Q10.3 Slow cooling of Pb-1 Sn

- id: B10-Q3
- concept_id: u4-precipitation-alloys
- format: what-happens
- asks: application

A Pb-1 wt% Sn alloy is cooled slowly from 350 °C to room temperature. What will happen to it:

a) Liquid, then α + L, then only α down to room temperature
b) Liquid, then α, then α + β below the solvus
c) Liquid, then α + L, then eutectic at 183 °C
d) It stays liquid down to 183 °C

### Answer

a

### Explanation

Session 8, Slide 2: Pb-1 wt% Sn is liquid at 350 °C, α starts to form at about 330 °C (α + L), it is only α at 270 °C, and it stays α on further cooling: its composition stays below the solubility limit at every temperature.

- b) Precipitation of β needs an alloy that crosses the solvus, such as Pb-16 wt% Sn; 1 wt% Sn never does.
- c) The eutectic reaction concerns alloys above 18.3 wt% Sn; this alloy is fully solid long before 183 °C.
- d) The liquidus of this alloy is near 330 °C, close to the melting point of Pb, far above 183 °C.

### Source

Session 8, Slide 2.

## Q10.4 Where the precipitates form

- id: B10-Q4
- concept_id: u4-precipitation-location
- format: complete-sentence
- asks: classification

When an alloy cools below the solvus, the small β particles form mostly:

a) Inside the remaining liquid
b) As eutectic layers between the grains
c) At the grain boundaries of α
d) Only at the free surface of the part

### Answer

c

### Explanation

Session 8, Slide 3: below the solvus small β particles appear in a matrix of α, mostly at the grain boundaries (as in the micrograph of the slide), and they become more numerous and grow at lower temperatures.

- a) Below the solvus the alloy is fully solid: there is no liquid left.
- b) Eutectic layers come from a liquid at the eutectic temperature, not from solid-state precipitation.
- d) Precipitation happens throughout the α grains and at their boundaries, not only at the surface.

### Source

Session 8, Slide 3.

## Q10.5 Definition of the eutectoid reaction

- id: B10-Q5
- concept_id: u4-eutectoid-reaction
- format: complete-sentence
- asks: definition

The eutectoid reaction is an invariant reaction in which:

a) A liquid transforms into two solids
b) A solid and a liquid form a new solid
c) Two solids form a new solid
d) A solid transforms into two other solids

### Answer

d

### Explanation

Session 8, Slide 7: a eutectoid reaction is an invariant reaction where a solid phase transforms into two solid phases, $\gamma \rightarrow \alpha + \beta$ (Cu-Zn at 560 °C: δ → γ + ε).

- a) A liquid into two solids is the eutectic, the reaction with the same shape but with L instead of a solid.
- b) A solid plus a liquid giving a new solid is the peritectic.
- c) Two solids giving a new solid is the peritectoid.

### Source

Session 8, Slides 6-7.

## Q10.6 Beta below the A-B eutectoid

- id: B10-Q6
- concept_id: u4-eutectoid-reaction
- format: numeric
- asks: calculation
- calc: (25-10)/(80-10)*100

From the shown diagram, determine the mass percentage of the β phase in the 25 wt% B alloy just below 600 °C:

![[attachments/MAT-MT2/u4-eutectoid-ab.svg]]

a) 18.8 %
b) 21.4 %
c) 50.0 %
d) 78.6 %

### Answer

b

### Explanation

Just below 600 °C the alloy is α (10 wt% B) + β (80 wt% B); the lever rule on the whole tie line (Session 7, Slide 16) gives $W_\beta = \dfrac{25 - 10}{80 - 10} = \dfrac{15}{70} = 0.214$.

- a) $15/80 = 0.188$ divides by the β composition instead of by the tie line.
- c) $(25 - 10)/(40 - 10) = 0.500$ uses the short tie line to the eutectoid point: that is the fraction of eutectoid microconstituent, not of β.
- d) $(80 - 25)/70 = 0.786$ is the fraction of α: arms swapped.

### Source

Session 8, Slide 7; Session 7, Slides 16 and 32.

## Q10.7 Reaction at 600 °C

- id: B10-Q7
- concept_id: u4-eutectoid-reaction
- format: diagram-reading
- asks: figure-reading

From the shown phase diagram, indicate the reaction that takes place at 600 °C on cooling:

![[attachments/MAT-MT2/u4-eutectoid-ab.svg]]

a) γ → α + β
b) L → α + β
c) α + β → γ
d) β + L → γ

### Answer

a

### Explanation

At 600 °C the single-phase solid γ ends in a V on the horizontal line, with α + β below it: a solid gives two solids, the eutectoid reaction (Session 8, Slides 6-7).

- b) There is no liquid in the diagram; L → α + β would be a eutectic.
- c) This is the eutectoid written on heating (or a peritectoid read from the shape); on cooling γ disappears, it does not form.
- d) β + L → γ is a peritectic, which needs a liquid and a solid field narrowing to a point below the line; here γ ends in a V above it.

### Source

Session 8, Slides 6-7.

## Q10.8 The Fe-Ni reaction at 1517 °C

- id: B10-Q8
- concept_id: u4-peritectic-reaction
- format: identify
- asks: classification

In the Fe-Ni system, δ (4.0 % Ni) + L (5.4 % Ni) → γ (4.3 % Ni) at 1517 °C on cooling. Which reaction is it:

a) Eutectic
b) Eutectoid
c) Peritectic
d) Monotectic

### Answer

c

### Explanation

Session 8, Slide 8: a solid and a liquid transform into a different solid, $\alpha + L \rightarrow \beta$: the peritectic reaction. Fe-Ni at 1517 °C is the example of the slide.

- a) A eutectic consumes only a liquid and gives two solids.
- b) A eutectoid involves only solids, one giving two.
- d) A monotectic gives a solid and a second liquid from a liquid.

### Source

Session 8, Slides 6 and 8.

## Q10.9 Liquid just above the peritectic

- id: B10-Q9
- concept_id: u4-peritectic-reaction
- format: numeric
- asks: calculation
- calc: (4.6-4.0)/(5.4-4.0)*100

A Fe-4.6 wt% Ni alloy is just above 1517 °C, with δ of 4.0 wt% Ni and liquid of 5.4 wt% Ni. Determine the mass percentage of liquid:

a) 27.3 %
b) 42.9 %
c) 57.1 %
d) 85.2 %

### Answer

b

### Explanation

Lever rule on the tie line δ-L just above the peritectic line (Session 8, Slide 8; Session 7, Slide 16): $W_L = \dfrac{4.6 - 4.0}{5.4 - 4.0} = \dfrac{0.6}{1.4} = 0.429$.

- a) $(4.6 - 4.3)/(5.4 - 4.3) = 0.273$ is the liquid left just below 1517 °C, after the reaction, on the γ-L tie line.
- c) $(5.4 - 4.6)/1.4 = 0.571$ is the fraction of δ: arms swapped.
- d) $4.6/5.4 = 0.852$ is a ratio of compositions.

### Source

Session 8, Slide 8; Session 7, Slide 16.

## Q10.10 Peritectic with fast cooling

- id: B10-Q10
- concept_id: u4-peritectic-reaction
- format: cause-effect
- asks: cause

With rapid cooling through a peritectic reaction α + L → β, the reaction often does not finish because:

a) The liquid first solidifies as a eutectic
b) α dissolves completely in the liquid
c) β melts congruently and returns to liquid
d) β surrounds α and acts as a diffusion barrier

### Answer

d

### Explanation

Session 8, Slide 10: during the peritectic reaction the β formed surrounds the primary α (encasement); β then acts as a diffusion barrier for the atoms that must cross it, which results in coring and a structure that is not the equilibrium one.

- a) No eutectic is involved; the reaction product is the single solid β.
- b) If α dissolved completely the reaction would have no α left to consume; the problem is that α is shielded, not that it disappears.
- c) Congruent melting is a property of some compounds on heating; it does not explain an incomplete reaction on cooling.

### Source

Session 8, Slide 10.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
