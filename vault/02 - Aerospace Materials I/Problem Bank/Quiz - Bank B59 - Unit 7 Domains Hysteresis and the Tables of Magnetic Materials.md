---
materia: Aerospace Materials I
tema: "Unit 7: reading the tables of soft, hard and recording magnetic materials; domains and hysteresis loops"
bank_id: B59
title: "Domains, hysteresis and the tables of magnetic materials"
category: mt2_test_block
unit: 7
concepts:
  - u7-soft-table-max-permeability
  - u7-hard-magnet-energy-product
  - u7-coercivity-tesla-to-ampere
  - u7-soft-hard-limit-classification
  - u7-induction-from-table-permeability
  - u7-remanence-ratio-table
  - u7-recording-powders-curie-table
  - u7-magnetization-curve-sequence
  - u7-loop-area-energy-loss
  - u7-rectangular-loop-materials
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 15, Slides 16-19 and 24."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-7
---

# Bank B59 — Domains, hysteresis and the tables of magnetic materials

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 15, Slides 16-19 and 24 (Tables 20-4, 20-5 and 20-6).

## Q59.1 Highest maximum permeability in the soft-magnet table

- id: B59-Q1
- concept_id: u7-soft-table-max-permeability
- format: diagram-reading
- asks: figure-reading

From the shown rows of Table 20-4 (Slide 24), indicate which soft magnetic material reaches the highest maximum relative permeability:

| Name | Initial $\mu_r$ | Maximum $\mu_r$ |
| :--- | ---: | ---: |
| 4750 alloy | 11 000 | 80 000 |
| 4-79 permalloy | 40 000 | 200 000 |
| Superalloy | 80 000 | 450 000 |
| Metglas 2650S-2 | not given | 600 000 |

a) 4750 alloy
b) 4-79 permalloy
c) Superalloy
d) Metglas 2650S-2

### Answer

d

### Explanation

The maximum permeability is read in the last column: 600 000 for Metglas 2650S-2, above 450 000 (Superalloy), 200 000 (4-79 permalloy) and 80 000 (4750 alloy). The empty cell of the initial permeability does not remove the row (Slide 24).

- a) The 80 000 of the 4750 alloy is the maximum permeability of that row; it equals the initial permeability of the Superalloy, so the student reads the initial column of another row.
- b) The student picks the well-known Fe-Ni permalloy without comparing the numbers of the last column.
- c) The Superalloy has the highest initial permeability of the shown rows (80 000), but the question asks for the maximum permeability.

### Source

Session 15, Slide 24.

## Q59.2 Energy stored by a rare-earth magnet

- id: B59-Q2
- concept_id: u7-hard-magnet-energy-product
- format: numeric
- asks: calculation
- calc: round(144/44, 1)

Table 20-6 (Slide 24) gives $(BH)_{max} = 144$ kJ/m³ for SmCo₅ and $(BH)_{max} = 44$ kJ/m³ for Alnico-5. Determine how many times more energy per unit volume the SmCo₅ magnet can store:

a) 0.31 times
b) 3.3 times
c) 4.2 times
d) 24 times

### Answer

b

### Explanation

The maximum energy product measures the energy a permanent magnet stores per unit volume, so the ratio is $144/44 = 3.3$ (Slide 24).

- a) Inverted ratio, $44/144 = 0.31$: the Alnico-5 value is placed in the numerator.
- c) Wrong row: $144/34 = 4.2$ uses the 34 kJ/m³ of the barium ferrite instead of the 44 kJ/m³ of Alnico-5.
- d) Wrong row: $144/6 = 24$ uses the 6 kJ/m³ of the Co-steel.

### Source

Session 15, Slide 24.

## Q59.3 Coercivity of SmCo₅ from the table

- id: B59-Q3
- concept_id: u7-coercivity-tesla-to-ampere
- format: numeric
- asks: calculation
- calc: 0.80/1.257e-6/1e3

Table 20-6 (Slide 24) lists $\mu_0 H_c = 0.80$ T for SmCo₅. Determine its coercivity $H_c$ ($\mu_0 = 1.257\times10^{-6}$ H/m):

a) 636 kA/m
b) 2550 kA/m
c) 1270 kA/m
d) 8000 kA/m

### Answer

a

### Explanation

$H_c = 0.80/\mu_0 = 0.80/1.257\times10^{-6} = 6.36\times10^{5}$ A/m $= 636$ kA/m, far above the 10 000 A/m limit of Slide 18 (hard magnet). Check of units: T divided by H/m gives A/m.

- b) $\mu_0$ is taken as $\pi\times10^{-7}$ H/m (the factor 4 of $4\pi$ is lost), which gives $0.80/\pi\times10^{-7}$ = 2550 kA/m.
- c) $\mu_0$ replaced by $6.28\times10^{-7}$ H/m ($2\pi\times10^{-7}$, a factor 2 lost), which doubles the result.
- d) $\mu_0$ rounded to $10^{-7}$ H/m, which gives $0.80/10^{-7} = 8\times10^{6}$ A/m.

### Source

Session 15, Slides 18 and 24.

## Q59.4 Classification of Co-steel

- id: B59-Q4
- concept_id: u7-soft-hard-limit-classification
- format: identify
- asks: classification
- check: 0.02/1.257e-6 > 10000 and 0.02/1.257e-5 < 10000

Table 20-6 (Slide 24) gives $\mu_0 H_c = 0.02$ T for the Fe-Co alloy Co-steel. With $\mu_0 = 1.257\times10^{-6}$ H/m and the limit $H_c = 10\,000$ A/m of Slide 18, this material is classified as:

a) soft, because its $H_c$ of 0.02 A/m is below the limit
b) soft, because its $H_c$ of 1.6 kA/m is below the limit
c) hard, because its $H_c$ of 15.9 kA/m is above the limit
d) soft, because its $H_c$ of 15.9 kA/m is above the limit

### Answer

c

### Explanation

$H_c = 0.02/1.257\times10^{-6} = 1.59\times10^{4}$ A/m, which is above 10 000 A/m, so the Bloch walls are difficult to move and the material is hard (Slide 18).

- a) The tesla value is compared with the limit without dividing by $\mu_0$.
- b) Exponent slip in $\mu_0$ ($1.257\times10^{-5}$ instead of $1.257\times10^{-6}$) gives 1.6 kA/m.
- d) Right number but soft and hard swapped: a coercivity above the limit defines a hard magnet.

### Source

Session 15, Slides 18 and 24.

## Q59.5 Induction of a permalloy in the initial stage

- id: B59-Q5
- concept_id: u7-induction-from-table-permeability
- format: numeric
- asks: calculation
- calc: 40000*1.257e-6*0.5*1e3

A demagnetized specimen of 4-79 permalloy (initial $\mu_r = 40\,000$, Table 20-4, Slide 24) is placed in a field $H = 0.5$ A/m, in the initial stage of its magnetization curve. Determine the induction $B$ ($\mu_0 = 1.257\times10^{-6}$ H/m):

a) 50.3 mT
b) 126 mT
c) 101 mT
d) 25.1 mT

### Answer

d

### Explanation

In the initial stage the slope is the initial permeability, so $B = \mu_r\mu_0 H = 40\,000\times1.257\times10^{-6}\times0.5 = 2.51\times10^{-2}$ T $= 25.1$ mT (Slide 16).

- a) The factor $H = 0.5$ A/m is left out ($H$ taken as 1 A/m), which doubles the result.
- b) The maximum permeability (200 000) is used instead of the initial one, which is wrong in the first stage of the curve.
- c) The field is divided instead of multiplied ($40\,000\times1.257\times10^{-6}/0.5 = 101$ mT).

### Source

Session 15, Slides 16 and 24.

## Q59.6 Remanence-to-saturation ratio of grain-oriented silicon iron

- id: B59-Q6
- concept_id: u7-remanence-ratio-table
- format: numeric
- asks: calculation
- calc: round(1.20/2.01, 2)

For grain-oriented silicon iron, Table 20-4 (Slide 24) gives $B_r = 1.20$ T and $B_{max} = 2.01$ T. Determine the ratio $B_r/B_{max}$ of the loop:

a) 1.7
b) 0.60
c) 0.36
d) 0.81

### Answer

b

### Explanation

$B_r/B_{max} = 1.20/2.01 = 0.60$: about 60 % of the maximum induction is kept when the field is removed (remanence, Slide 17).

- a) Inverted ratio, $2.01/1.20 = 1.7$: a remanence cannot exceed the maximum induction of the same loop.
- c) Wrong row: $0.77/2.14 = 0.36$ uses the values of ingot iron.
- d) Difference in place of ratio: $2.01 - 1.20 = 0.81$ (a value in tesla, not a ratio).

### Source

Session 15, Slides 17 and 24.

## Q59.7 Recording powder past its Curie temperature

- id: B59-Q7
- concept_id: u7-recording-powders-curie-table
- format: diagram-reading
- asks: figure-reading

From the shown values of Table 20-5 (Slide 24), indicate which recording powder has already lost its ferromagnetic order when it works at 400 °C:

| Powder | Curie temperature $T_c$ (°C) |
| :--- | ---: |
| γ-Fe₂O₃ | 600 |
| Co-γ-Fe₂O₃ | 700 |
| Fe | 770 |
| Barium ferrite | 350 |

a) Barium ferrite
b) γ-Fe₂O₃
c) Fe
d) Co-γ-Fe₂O₃

### Answer

a

### Explanation

A material is paramagnetic above its Curie temperature (Slide 23). Only the barium ferrite has $T_c = 350\,°\text{C} < 400\,°\text{C}$; the other three have $T_c$ above 400 °C and stay ordered.

- b) The 600 is read as kelvin (600 K = 327 °C, below 400 °C), but the column is already in °C.
- c) Inverted comparison: the highest $T_c$ is chosen as the one that has been exceeded.
- d) The student assumes that the cobalt addition lowers the Curie temperature; the table shows 700 °C, higher than that of γ-Fe₂O₃.

### Source

Session 15, Slides 23 and 24.

## Q59.8 Order of the stages of magnetization

- id: B59-Q8
- concept_id: u7-magnetization-curve-sequence
- format: ordering
- asks: application

When a field is applied to a demagnetized ferromagnet and increased up to saturation, the stages follow, in order:

a) random domains, rotation of domains, growth of favourable domains, saturation
b) growth of favourable domains, random domains, rotation of domains, saturation
c) random domains, growth of favourable domains, rotation of domains, saturation
d) random domains, growth of favourable domains, saturation, rotation of domains

### Answer

c

### Explanation

Slide 16: the domains start randomly distributed; the favourable domains grow at the expense of the unfavourable ones (fast rise); later the magnetization slows because the domains must rotate; finally all dipoles are aligned, which is saturation.

- a) Growth and rotation are swapped: rotation is the last, slow stage, since domain walls move before dipoles turn.
- b) The sequence starts with growth: the demagnetized state, with random domains, comes first.
- d) Saturation placed before rotation: saturation is reached only when the rotation has aligned all the dipoles.

### Source

Session 15, Slide 16.

## Q59.9 Energy lost per cycle in a soft core

- id: B59-Q9
- concept_id: u7-loop-area-energy-loss
- format: cause-effect
- asks: cause

A soft magnetic core in an alternating field dissipates little energy per cycle because:

a) its Bloch walls are difficult to move, so it keeps a high remanence
b) its Bloch walls move easily, so its loop encloses a small area
c) its domains are larger than its grains, so its loop encloses a small area
d) its initial permeability is low, so its loop is narrow

### Answer

b

### Explanation

Slides 18-19: in soft materials the Bloch walls are easy to move, so the coercivity is low and the loop is narrow; they are used under alternating fields to minimize energy losses. The energy lost per cycle is proportional to the area of the loop (extension: not written on the slides).

- a) Describes a hard material (walls difficult to move, high remanence), which has a wide loop and large losses.
- c) Wrong cause: domains are usually smaller than the grains (Slide 14), and their size does not set the area of the loop.
- d) Inverted trend: soft materials have a high initial permeability (Slide 18), and a low one belongs to hard materials.

### Source

Session 15, Slides 18-19.

## Q59.10 Material of a rectangular hysteresis loop

- id: B59-Q10
- concept_id: u7-rectangular-loop-materials
- format: identify
- asks: application

According to Slide 19, a material with a rectangular hysteresis cycle is:

a) a soft magnet heat-treated in a magnetic field, used in magnetic memories
b) a hard magnet quenched from high temperature, used in permanent magnets
c) a soft magnet annealed without field, used in cores of transformers
d) a hard magnet of high remanence, used in cores of electric motors

### Answer

a

### Explanation

Slide 19: rectangular-cycle materials are soft magnetic materials modified by a thermal treatment in the presence of a magnetic field, with low remanence, low saturation magnetization and low coercive field; they serve for magnetic memories, magnetic amplifiers and pulse transformers (data storage).

- b) Hard magnets with wide loops make permanent magnets, not rectangular-cycle memories.
- c) Transformer cores use ordinary soft materials; the rectangular cycle needs the treatment in the field.
- d) Motor cores need soft materials under alternating fields; a high remanence belongs to permanent magnets.

### Source

Session 15, Slide 19.
