---
materia: Aerospace Materials I
tema: "Unit 4: hypoeutectic and hypereutectic alloys, microconstituents and their amounts"
bank_id: B08
title: "Hypoeutectic and hypereutectic alloys"
category: mt2_test_block
unit: 4
concepts:
  - u4-hypo-hyper-classification
  - u4-eutectic-reaction
  - u4-primary-fraction
  - u4-eutectic-fraction
  - u4-total-phase-fraction
  - u4-hypo-cooling-sequence
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 7 Slides 26-32 (Pb-Sn: 183 °C, 18.3, 61.9 and 97.8 wt% Sn) and Session 8 Slide 6."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-4
---

# Bank B08 — Hypoeutectic and hypereutectic alloys

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 7, Slides 26-32; Session 8, Slide 6. Pb-Sn values of Slide 32: eutectic 183 °C and 61.9 wt% Sn, α 18.3 and β 97.8 wt% Sn.

## Q08.1 Name of a Sn-rich alloy

- id: B08-Q1
- concept_id: u4-hypo-hyper-classification
- format: complete-sentence
- asks: definition

An alloy whose composition lies between the eutectic composition and the β limit is called:

a) Hypoeutectic
b) Hypereutectic
c) Eutectoid
d) Peritectic

### Answer

b

### Explanation

Session 7, Slide 30: an alloy between the α limit and the eutectic composition is hypoeutectic; one between the eutectic composition and the β limit is hypereutectic.

- a) Hypoeutectic is the neighbouring range, on the α side of the eutectic composition.
- c) Eutectoid names a solid-state invariant reaction ($\gamma \rightarrow \alpha + \beta$), not a range of alloys of a eutectic system.
- d) Peritectic names another invariant reaction ($\alpha + L \rightarrow \beta$), not a composition range.

### Source

Session 7, Slide 30.

## Q08.2 One liquid into two solids

- id: B08-Q2
- concept_id: u4-eutectic-reaction
- format: identify
- asks: classification

Which invariant reaction turns one liquid into two different solids at a fixed temperature:

a) Peritectic
b) Eutectoid
c) Monotectic
d) Eutectic

### Answer

d

### Explanation

Session 8, Slide 6: the eutectic is $L \rightarrow \alpha + \beta$ on cooling, a liquid giving two solids at one temperature (Session 7, Slide 27).

- a) The peritectic consumes a liquid and a solid to give one solid: $\alpha + L \rightarrow \beta$.
- b) The eutectoid starts from a solid, $\gamma \rightarrow \alpha + \beta$, not from a liquid.
- c) The monotectic gives a solid and another liquid, $L_1 \rightarrow L_2 + \alpha$.

### Source

Session 8, Slide 6; Session 7, Slide 27.

## Q08.3 Primary alpha in Pb-50 Sn

- id: B08-Q3
- concept_id: u4-primary-fraction
- format: numeric
- asks: calculation
- calc: (61.9-50)/(61.9-18.3)*100

Determine the mass percentage of primary α in a Pb-50 wt% Sn alloy just below 183 °C:

a) 15.0 %
b) 27.3 %
c) 60.1 %
d) 72.7 %

### Answer

b

### Explanation

Microconstituents use the short tie line from α (18.3) to the eutectic liquid (61.9 wt% Sn) (Session 7, Slide 32): $W_{\alpha'} = \dfrac{Q}{P + Q} = \dfrac{61.9 - 50}{61.9 - 18.3} = \dfrac{11.9}{43.6} = 0.273$.

- a) $11.9/79.5 = 0.150$ divides by the whole α-β tie line, which is used for phases, not for microconstituents.
- c) $(97.8 - 50)/(97.8 - 18.3) = 0.601$ is the total α (primary plus eutectic), a phase fraction.
- d) $(50 - 18.3)/43.6 = 0.727$ is the eutectic fraction: arms swapped.

### Source

Session 7, Slide 32.

## Q08.4 Eutectic microconstituent properties

- id: B08-Q4
- concept_id: u4-eutectic-fraction
- format: topic-true
- asks: comparison

Regarding the eutectic microconstituent in binary alloys just below the eutectic temperature, which statement is TRUE:

a) Its mass fraction equals the mass fraction of liquid present just above the eutectic temperature
b) Its chemical composition shifts continuously with the overall Sn content of the alloy
c) In a hypereutectic alloy it coexists with primary $\alpha$ rather than primary $\beta$
d) Its mass fraction is found directly from the lever rule on the whole $\alpha$–$\beta$ tie line

### Answer

a

### Explanation

Session 7, Slides 28 and 32: all liquid remaining just above the eutectic temperature has the eutectic composition (61.9 wt% Sn in Pb-Sn) and transforms into the eutectic microconstituent at 183 °C, so $W_e = W_L$ just above the isotherm.

- b) The eutectic microconstituent always forms from liquid at the fixed eutectic composition (61.9 wt% Sn), so its composition and internal $\alpha/\beta$ ratio never vary with $C_0$.
- c) A hypereutectic alloy lies on the $\beta$ side of the eutectic, so it forms primary $\beta$ surrounded by eutectic; primary $\alpha$ belongs to hypoeutectic alloys.
- d) The whole $\alpha$–$\beta$ tie line gives the total phase fractions ($W_\alpha, W_\beta$), whereas microconstituent fractions ($W_{\alpha'}, W_e$ or $W_{\beta'}, W_e$) use the short tie line ending at $C_e$.

### Source

Session 7, Slides 28 and 30-32.

## Q08.5 Phases versus microconstituents in Pb-Sn

- id: B08-Q5
- concept_id: u4-total-phase-fraction
- format: topic-false
- asks: application

Referring to phases and microconstituents in a hypoeutectic Pb-Sn alloy just below 183 °C, which statement is FALSE:

a) Total $\alpha$ phase equals the sum of primary $\alpha$ and the $\alpha$ inside the eutectic lamellae
b) All of the $\beta$ phase present in the alloy belongs to the eutectic microconstituent
c) The mass fractions of primary $\alpha$ and eutectic microconstituent sum to unity
d) The phase balance on the $\alpha$–$\beta$ tie line conflicts with the microconstituent balance

### Answer

d

### Explanation

Statement d) is false: the phase balance ($W_\alpha + W_\beta = 1$) and the microconstituent balance ($W_{\alpha'} + W_e = 1$) always agree, because $W_\alpha = W_{\alpha'} + W_{\alpha,e}$ and $W_e = W_{\alpha,e} + W_\beta$ (Session 7, Slide 32; Problems T4_PhaseDiagrams I.pdf, Q3–Q4).

- a) True: $\alpha$ appears in two forms—as primary grains formed before 183 °C and as alternating layers inside the eutectic.
- b) True: in a hypoeutectic alloy no primary $\beta$ forms above 183 °C, so every bit of $\beta$ forms inside the eutectic.
- c) True: primary $\alpha$ and eutectic are the two microconstituents filling the microstructure ($W_{\alpha'} + W_e = 1$).

### Source

Session 7, Slide 32.

## Q08.6 Structures met on cooling Pb-40 Sn

- id: B08-Q6
- concept_id: u4-hypo-cooling-sequence
- format: ordering
- asks: application

Order the states met during slow cooling of a Pb-40 wt% Sn alloy from 300 °C to room temperature:

a) L; eutectic; primary α + eutectic
b) L; β + L; primary β + eutectic
c) α + L; L; eutectic
d) L; α + L; primary α + eutectic

### Answer

d

### Explanation

Pb-40 wt% Sn is hypoeutectic (Session 7, Slide 30): liquid above its liquidus, then crystals of α in liquid, and at 183 °C the remaining liquid (now 61.9 wt% Sn) becomes eutectic, leaving primary α surrounded by eutectic.

- a) The eutectic cannot form before the primary α: the liquid reaches the eutectic composition only after α has grown.
- b) Primary β belongs to hypereutectic alloys, on the other side of 61.9 wt% Sn.
- c) The order is reversed: on cooling the liquid comes first, and the final structure keeps primary α.

### Source

Session 7, Slide 30.

## Q08.7 Remaining liquid at 183 °C

- id: B08-Q7
- concept_id: u4-hypo-cooling-sequence
- format: what-happens
- asks: effect

A Pb-50 wt% Sn alloy cooling through α + L reaches 183 °C. What will happen to the liquid that is left:

a) It solidifies as β over a range below 183 °C
b) It stays liquid down to room temperature
c) It transforms at 183 °C into the α + β eutectic
d) It becomes primary α of 61.9 wt% Sn

### Answer

c

### Explanation

Just above 183 °C the liquid has reached the eutectic composition (61.9 wt% Sn); at 183 °C it transforms at constant temperature, $L \rightarrow \alpha + \beta$, giving the eutectic around the primary α (Session 7, Slide 30).

- a) A liquid of eutectic composition does not solidify over a range: the reaction is invariant, at one temperature.
- b) Below 183 °C there is no liquid in the Pb-Sn diagram; the eutectic temperature is the lowest at which liquid exists.
- d) α can hold at most 18.3 wt% Sn; 61.9 wt% Sn is the composition of the liquid, not of α.

### Source

Session 7, Slides 27 and 30.

## Q08.8 Primary phase of a hypereutectic alloy

- id: B08-Q8
- concept_id: u4-hypo-cooling-sequence
- format: true-statement
- asks: classification

Which one of the following statements about a hypereutectic Pb-Sn alloy below 183 °C is TRUE:

a) Its primary phase is β
b) Its primary phase is α
c) It contains no eutectic
d) All its β lies inside the eutectic

### Answer

a

### Explanation

Session 7, Slide 31: in a hypereutectic alloy primary β forms between the liquidus and the eutectic temperature; the remaining liquid gives the eutectic, so the final structure is primary β plus eutectic.

- b) Primary α is the first solid of hypoeutectic alloys, on the other side of the eutectic composition.
- c) The liquid left at 183 °C always becomes eutectic; its amount changes with the alloy but is never zero between 61.9 and 97.8 wt% Sn.
- d) This holds for β in a hypoeutectic alloy; in a hypereutectic one part of the β is primary.

### Source

Session 7, Slides 30-31.

## Q08.9 Eutectic and Sn content

- id: B08-Q9
- concept_id: u4-eutectic-fraction
- format: cause-effect
- asks: effect

With an increase in Sn content from 20 to 61.9 wt% in Pb-Sn alloys, the fraction of eutectic just below 183 °C:

a) Decreases, because more primary α forms
b) Increases, but never above 54.8 %
c) Stays constant at 45.2 %
d) Increases, reaching 100 % at 61.9 wt% Sn

### Answer

d

### Explanation

$W_e = (C_0 - 18.3)/(61.9 - 18.3)$ (Session 7, Slide 32): it grows with $C_0$ and reaches 1 at the eutectic composition, where the alloy is all eutectic (Slide 28).

- a) Inverted trend: closer to the eutectic composition there is less primary α, not more.
- b) 54.8 % is the β content inside the eutectic, a different quantity, not a limit on the eutectic fraction.
- c) 45.2 % is the α content inside every eutectic; the amount of eutectic changes with the alloy.

### Source

Session 7, Slides 28 and 32.

## Q08.10 Tie line for the total alpha

- id: B08-Q10
- concept_id: u4-total-phase-fraction
- format: complete-sentence
- asks: definition

In a hypoeutectic alloy just below the eutectic temperature, the total fraction of α is computed on the tie line that runs from:

a) The α limit to the eutectic composition
b) The eutectic composition to the β limit
c) The α limit to the β limit
d) The alloy composition to the eutectic composition

### Answer

c

### Explanation

Session 7, Slide 32: the phases (total α, β) use the whole tie line between α and β, $W_\alpha = (Q + R)/(P + Q + R)$; the microconstituents use the short tie line between α and the eutectic liquid.

- a) The short tie line from α to the eutectic gives the microconstituents (primary α and eutectic), not the total α.
- b) From the eutectic to β is the short tie line of a hypereutectic alloy.
- d) This is only one arm of the lever, not a whole tie line.

### Source

Session 7, Slide 32.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
