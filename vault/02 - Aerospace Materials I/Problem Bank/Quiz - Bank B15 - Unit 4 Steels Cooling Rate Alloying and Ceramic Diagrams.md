---
materia: Aerospace Materials I
tema: "Unit 4: steels, pearlite and cooling rate, alloying elements, ceramic and ternary diagrams"
bank_id: B15
title: "Steels, cooling rate, alloying elements and ceramic diagrams"
category: mt2_test_block
unit: 4
concepts:
  - u4-total-ferrite-steel
  - u4-pearlite-composition
  - u4-steel-carbon-from-microstructure
  - u4-hypereutectoid-microstructure
  - u4-cooling-rate-pearlite
  - u4-alloying-elements
  - u4-ceramic-diagrams
  - u4-ternary-reading
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 9 Slides 4-23 (0.022, 0.76 and 6.67 wt% C at 727 °C) and Session 10 Slides 3 and 5."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-4
---

# Bank B15 — Steels, cooling rate, alloying elements and ceramic diagrams

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 9, Slides 4-23; Session 10, Slides 3 and 5.

## Q15.1 Ferrite in 200 g of a 0.6 C steel

- id: B15-Q1
- concept_id: u4-total-ferrite-steel
- format: numeric
- asks: calculation
- calc: 200*(6.67-0.6)/(6.67-0.022)

Determine the total mass of ferrite in 200 g of a slowly cooled 0.6 wt% C steel at 600 °C:

a) 17.4 g
b) 43.4 g
c) 139 g
d) 183 g

### Answer

d

### Explanation

Below 727 °C the phases are α (0.022) and Fe₃C (6.67 wt% C) (Session 9, Slides 4 and 9): $W_\alpha = \dfrac{6.67 - 0.6}{6.67 - 0.022} = \dfrac{6.07}{6.648} = 0.913$, so $m_\alpha = 0.913 \times 200 = 183$ g.

- a) $200 \times (0.6 - 0.022)/6.648 = 17.4$ g is the cementite: arms swapped.
- b) $200 \times (0.76 - 0.6)/0.738 = 43.4$ g is only the proeutectoid ferrite, a microconstituent.
- c) $183 - 43.4 = 139$ g is only the ferrite inside the pearlite, missing the proeutectoid ferrite.

### Source

Session 9, Slides 4, 9 and 17-18.

## Q15.2 Cementite inside the pearlite of 2 kg

- id: B15-Q2
- concept_id: u4-pearlite-composition
- format: numeric
- asks: calculation
- calc: 2*(0.76-0.022)/(6.67-0.022)

Determine the mass of cementite in 2 kg of a slowly cooled eutectoid steel (0.76 wt% C) below 727 °C:

a) 0.0152 kg
b) 0.222 kg
c) 1.78 kg
d) 2.00 kg

### Answer

b

### Explanation

The steel is all pearlite, whose cementite comes from the lever rule on the tie line 0.022-6.67 wt% C (Session 9, Slides 12-13): $W_{\text{Fe}_3\text{C}} = \dfrac{0.76 - 0.022}{6.648} = 0.111$, and $0.111 \times 2 = 0.222$ kg.

- a) $2 \times 0.76/100 = 0.0152$ kg is the mass of carbon, not the mass of cementite that holds it.
- c) $2 \times 0.889 = 1.78$ kg is the ferrite of the pearlite: the other phase.
- d) 2.00 kg is the whole pearlite, a microconstituent made of two phases.

### Source

Session 9, Slides 12-13.

## Q15.3 Steel with ferrite and pearlite

- id: B15-Q3
- concept_id: u4-steel-carbon-from-microstructure
- format: true-statement
- asks: application

A slowly cooled plain carbon steel shows only pearlite and proeutectoid ferrite. Which one of the following statements is TRUE:

a) Its carbon content is below 0.76 wt%
b) Its carbon content is between 0.76 and 2.14 wt%
c) Its carbon content is above 2.14 wt%
d) Its carbon content is exactly 0.76 wt%

### Answer

a

### Explanation

Proeutectoid ferrite forms only in hypoeutectoid steels, those with less than 0.76 wt% C (Session 9, Slides 4 and 14).

- b) Between 0.76 and 2.14 wt% C the proeutectoid phase is cementite, not ferrite (Slide 19).
- c) Above 2.14 wt% C the alloy is a cast iron, with ledeburite.
- d) At exactly 0.76 wt% C the steel is all pearlite, with no proeutectoid ferrite (Slide 12).

### Source

Session 9, Slides 4, 12, 14 and 19.

## Q15.4 Cementite network of hypereutectoid steels

- id: B15-Q4
- concept_id: u4-hypereutectoid-microstructure
- format: cause-effect
- asks: cause

A slowly cooled hypereutectoid steel tends to be brittle along the boundaries of its former austenite grains because:

a) Soft ferrite collects at those boundaries
b) Liquid remains trapped at those boundaries
c) A network of hard, brittle cementite forms there
d) The pearlite there has the coarsest lamellae

### Answer

c

### Explanation

In a hypereutectoid steel the proeutectoid cementite forms a network along the boundaries of the former austenite grains (Session 9, Slide 19), and cementite is hard and brittle (Slide 8); a continuous brittle network gives an easy path along those boundaries.

- a) Proeutectoid ferrite belongs to hypoeutectoid steels, and ferrite is soft, not brittle.
- b) A steel is fully solid below the solidus; no liquid remains in it at room temperature.
- d) Lamellar spacing affects the hardness of pearlite (Slide 12); it is not what gathers at the grain boundaries.

### Source

Session 9, Slides 8, 12 and 19.

## Q15.5 Pearlite and cooling rate

- id: B15-Q5
- concept_id: u4-cooling-rate-pearlite
- format: cause-effect
- asks: effect

With an increase in cooling rate, the pearlite of a steel:

a) Becomes finer and harder
b) Becomes coarser and harder
c) Becomes finer and softer
d) Does not change, since its make-up is fixed

### Answer

a

### Explanation

Session 9, Slide 21: a higher cooling rate decreases the spacing of the pearlite lamellae (fine pearlite instead of coarse), and decreasing that spacing increases the hardness (Slide 12).

- b) Coarser lamellae are the result of slow cooling, and they are softer.
- c) Right change of spacing, wrong consequence: finer pearlite is harder, not softer.
- d) The ferrite/cementite proportion is fixed, but the lamellar spacing, and with it the hardness, changes with the cooling rate.

### Source

Session 9, Slides 12 and 21.

## Q15.6 Proeutectoid ferrite with faster cooling

- id: B15-Q6
- concept_id: u4-cooling-rate-pearlite
- format: what-happens
- asks: effect

A hypoeutectoid steel is cooled faster than in equilibrium. What will happen to its amount of proeutectoid ferrite:

a) It increases
b) It is replaced by proeutectoid cementite
c) It stays the same as in equilibrium
d) It decreases

### Answer

d

### Explanation

Session 9, Slide 21: with a higher cooling rate the eutectoid point moves to lower temperatures and lower carbon contents, so the percentage of proeutectoid ferrite decreases (and the pearlite increases).

- a) Inverted trend: the shifted eutectoid point brings the steel closer to it, with less proeutectoid ferrite.
- b) Proeutectoid cementite needs a carbon content above the eutectoid; the steel stays hypoeutectoid.
- c) The slide states that the amount changes with the cooling rate.

### Source

Session 9, Slide 21.

## Q15.7 A gamma-stabilising element

- id: B15-Q7
- concept_id: u4-alloying-elements
- format: identify
- asks: classification

Which of the following alloying elements favours γ and lowers the eutectoid temperature of steel:

a) Cr
b) Si
c) Ni
d) Mo

### Answer

c

### Explanation

Session 9, Slides 22-23: the elements favouring γ (Mn, Co, Ni, Cu, Zn, Au) displace the eutectoid to lower temperature and lower carbon content.

- a) Cr favours α: it raises the eutectoid temperature.
- b) Si is in the list of elements favouring α, so it raises the eutectoid temperature, like Cr.
- d) Mo favours α, so it moves the eutectoid to higher temperature.

### Source

Session 9, Slides 22-23.

## Q15.8 Effect of an alpha-stabiliser

- id: B15-Q8
- concept_id: u4-alloying-elements
- format: complete-sentence
- asks: effect

Adding a ferrite-stabilising element such as Cr to a steel moves the eutectoid point to:

a) Higher temperature and lower carbon content
b) Lower temperature and lower carbon content
c) Higher temperature and higher carbon content
d) Lower temperature and higher carbon content

### Answer

a

### Explanation

Session 9, Slides 22-23: elements favouring α (Si, P, Al, ..., Mo, W, Cr) displace the eutectoid to higher temperature and lower %C.

- b) Lower temperature and lower %C is the effect of the γ-stabilisers (Ni, Mn); the two families are swapped.
- c) The temperature is right but the carbon content falls for both families; it never rises.
- d) Both changes are wrong for Cr: temperature falls only with γ-stabilisers, and %C does not rise.

### Source

Session 9, Slides 22-23.

## Q15.9 Mullite in Al2O3-SiO2

- id: B15-Q9
- concept_id: u4-ceramic-diagrams
- format: true-statement
- asks: classification

Which one of the following statements about the Al₂O₃-SiO₂ system of the slides is TRUE:

a) Mullite melts congruently at 1587 °C
b) Mullite melts incongruently at 1828 °C
c) Al₂O₃ and SiO₂ are completely soluble in the solid
d) Its eutectic reaction is at 1828 °C

### Answer

b

### Explanation

Session 10, Slide 3: mullite (ss) has an incongruent melting point at 1828 °C, $3\text{Al}_2\text{O}_3\cdot 2\text{SiO}_2 \rightarrow L\,(77\ \text{wt\%}\ \text{Al}_2\text{O}_3) + \text{Al}_2\text{O}_3$, the peritectic read on heating.

- a) 1587 °C is the eutectic between mullite and SiO₂, and mullite does not keep its composition on melting.
- c) Complete solid solubility is the Al₂O₃-Cr₂O₃ system (Slide 2); here mullite is an intermediate phase between alumina and cristobalite.
- d) 1828 °C is the peritectic; the eutectic is at 1587 °C.

### Source

Session 10, Slides 2-3.

## Q15.10 Third component of a ternary alloy

- id: B15-Q10
- concept_id: u4-ternary-reading
- format: numeric
- asks: calculation
- calc: 100-45-30

A point of a ternary A-B-C diagram has 45 wt% A and 30 wt% B. Determine its content of C:

a) 15.0 wt%
b) 25.0 wt%
c) 37.5 wt%
d) 75.0 wt%

### Answer

b

### Explanation

Session 10, Slide 5: each point inside the composition triangle is one composition whose three percentages add up to 100 %, so C $= 100 - 45 - 30 = 25.0$ wt%.

- a) $45 - 30 = 15$ subtracts one given content from the other instead of both from 100 %.
- c) $(45 + 30)/2 = 37.5$ averages the two given contents, which has no meaning for a composition.
- d) $45 + 30 = 75$ is the sum of A and B, not the remainder.

### Source

Session 10, Slide 5.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
