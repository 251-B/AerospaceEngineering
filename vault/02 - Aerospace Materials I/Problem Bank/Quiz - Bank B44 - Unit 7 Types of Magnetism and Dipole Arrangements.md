---
materia: Aerospace Materials I
tema: "Unit 7: types of magnetism and the arrangement of the magnetic dipoles"
bank_id: B44
title: "Types of magnetism and dipole arrangements"
category: mt2_test_block
unit: 7
concepts:
  - u7-ferromagnetism
  - u7-diamagnetism
  - u7-paramagnetism
  - u7-antiferromagnetism
  - u7-ferrimagnetism
  - u7-magnetism-classification
difficulty: 1
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content from Session 15, Slides 5-13."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-7
---

# Bank B44 — Types of magnetism and dipole arrangements

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 15, Slides 5-13.

## Q44.1 Dipoles of a ferromagnet without a field

- id: B44-Q1
- concept_id: u7-ferromagnetism
- format: choose-figure
- asks: figure-reading

Which picture describes the dipoles of a ferromagnetic material inside one domain, with no external field applied?

a) ![[attachments/MAT-MT2/u7-dip-1.svg]]
b) ![[attachments/MAT-MT2/u7-dip-2.svg]]
c) ![[attachments/MAT-MT2/u7-dip-3.svg]]
d) ![[attachments/MAT-MT2/u7-dip-4.svg]]

### Answer

b

### Explanation

A ferromagnetic material has permanent dipoles oriented parallel to each other in the absence of a field (Slides 9 and 13); within one domain they all point the same way, as in picture b.

- a) Randomly oriented permanent dipoles are the paramagnetic arrangement without a field (Slide 8).
- c) Antiparallel dipoles of equal size are the antiferromagnetic arrangement, with no net moment (Slide 10).
- d) Antiparallel dipoles of unequal size are the ferrimagnetic arrangement of the ferrites (Slides 11 and 13).

### Source

Session 15, Slides 9 and 13.

## Q44.2 Dipoles of a diamagnetic material

- id: B44-Q2
- concept_id: u7-diamagnetism
- format: complete-sentence
- asks: definition

In a diamagnetic material, the magnetic dipoles:

a) exist only while a field acts and oppose it
b) are permanent and turn to align with the field
c) are permanent, antiparallel and of equal size
d) exist only while a field acts and align with it

### Answer

a

### Explanation

Slide 6: a diamagnetic material has no dipoles without a field; the field induces dipoles aligned opposite to it, and the effect is not permanent ($\chi_m < 0$).

- b) Permanent dipoles that align with the field describe a paramagnetic material (Slide 8).
- c) Permanent antiparallel dipoles of equal size describe an antiferromagnetic material (Slide 10).
- d) Right about the induced, non-permanent dipoles, but wrong direction: aligned dipoles would give $\chi_m > 0$, while the diamagnetic ones oppose the field.

### Source

Session 15, Slides 6 and 13.

## Q44.3 Magnetization of a paramagnet and the field

- id: B44-Q3
- concept_id: u7-paramagnetism
- format: cause-effect
- asks: effect

With an increase in the applied field, the magnetization of a paramagnetic material:

a) increases, because its random permanent dipoles turn towards the field
b) increases, because more dipoles are induced opposite to the field
c) decreases, because its dipoles turn against the field
d) does not change, because its dipoles keep random orientations

### Answer

a

### Explanation

Slide 8: a paramagnetic material has permanent dipoles randomly oriented; an applied field turns them towards its direction, and their small induced field adds to the applied one, so $M = \chi_m H$ grows with $H$.

- b) Right trend with the diamagnetic mechanism: induced dipoles opposite to the field give a negative magnetization (Slide 6).
- c) Inverted response: dipoles turning against the field would give $\chi_m < 0$, the diamagnetic sign, not the paramagnetic one.
- d) The random orientation is the state without a field; the field aligns the dipoles, which is why $\chi_m > 0$.

### Source

Session 15, Slide 8.

## Q44.4 Dipoles of an antiferromagnet

- id: B44-Q4
- concept_id: u7-antiferromagnetism
- format: choose-figure
- asks: figure-reading

Which picture describes an antiferromagnetic material such as MnO, with no external field applied?

a) ![[attachments/MAT-MT2/u7-dip-1.svg]]
b) ![[attachments/MAT-MT2/u7-dip-4.svg]]
c) ![[attachments/MAT-MT2/u7-dip-2.svg]]
d) ![[attachments/MAT-MT2/u7-dip-3.svg]]

### Answer

d

### Explanation

Slide 10: the permanent dipoles of an antiferromagnetic material are antiparallel and of the same size, so the solid has no net moment; picture d shows neighbouring arrows of equal length pointing in opposite directions.

- a) Random permanent dipoles are the paramagnetic state without a field (Slide 8).
- b) Antiparallel arrows of unequal length leave a net moment: that is the ferrimagnetic arrangement (Slide 11).
- c) Parallel dipoles are the ferromagnetic arrangement within a domain (Slide 9).

### Source

Session 15, Slides 10 and 13.

## Q44.5 Ferrimagnetic materials

- id: B44-Q5
- concept_id: u7-ferrimagnetism
- format: true-statement
- asks: classification

Which one of the following statements is TRUE about ferrimagnetic materials?

a) They are mostly pure metals such as Fe, Co and Ni
b) Their antiparallel dipoles are equal, so the net moment is zero
c) They are ceramics whose antiparallel moments differ in size
d) Their dipoles exist only while a field is applied

### Answer

c

### Explanation

Slide 11: ferrimagnetism is present in ceramic materials (ferrites, garnets and AB₁₂O₁₉ compounds) with permanent dipoles of different intensity aligned antiparallel, so a net moment remains.

- a) Fe, Co and Ni are the ferromagnetic metals of Slide 9; the ferrimagnetic materials are ceramics.
- b) Equal antiparallel dipoles with zero net moment define the antiferromagnetic materials (Slide 10), the neighbouring type.
- d) Dipoles that exist only under a field are the induced dipoles of diamagnetism (Slide 6); ferrimagnetic dipoles are permanent.

### Source

Session 15, Slides 11 and 13.

## Q44.6 Magnetization of a diamagnetic metal

- id: B44-Q6
- concept_id: u7-diamagnetism
- format: numeric
- asks: calculation
- calc: -1.2e-5*8.0e5

A diamagnetic metal with susceptibility $\chi_m = -1.2\times10^{-5}$ is placed in a field $H = 8.0\times10^5$ A/m. Determine its magnetization:

a) $-6.67\times10^{10}$ A/m
b) $-9.60$ A/m
c) $-1.21\times10^{-5}$ A/m
d) $-1.50\times10^{-11}$ A/m

### Answer

b

### Explanation

$M = \chi_m H$ (Slide 4): $M = -1.2\times10^{-5}\times8.0\times10^5 = -9.60$ A/m. The minus sign says that the induced magnetization opposes the field (Slide 6).

- a) $H$ divided by $\chi_m$ instead of multiplied: $8.0\times10^5/(-1.2\times10^{-5}) = -6.67\times10^{10}$ A/m, a magnetization far above that of any ferromagnet.
- c) The product is multiplied again by $\mu_0$, mixing $M$ with the induction term $\mu_0 M$: $-9.60\times1.257\times10^{-6} = -1.21\times10^{-5}$.
- d) $\chi_m$ divided by $H$: $-1.2\times10^{-5}/8.0\times10^5 = -1.50\times10^{-11}$.

### Source

Session 15, Slides 4-6.

## Q44.7 Paramagnet in an applied field

- id: B44-Q7
- concept_id: u7-paramagnetism
- format: choose-figure
- asks: figure-reading

Which picture describes a paramagnetic material while an external field H is applied in the direction shown?

a) ![[attachments/MAT-MT2/u7-dipf-3.svg]]
b) ![[attachments/MAT-MT2/u7-dipf-2.svg]]
c) ![[attachments/MAT-MT2/u7-dipf-1.svg]]
d) ![[attachments/MAT-MT2/u7-dipf-4.svg]]

### Answer

c

### Explanation

Slide 8 draws the paramagnetic material twice: random permanent dipoles at $H = 0$, and the same dipoles aligned with the direction of $H$ once the field is applied, as in picture c.

- a) Random dipoles are the paramagnetic state before the field is applied; the question asks for the state under the field.
- b) Small dipoles opposite to $H$ are the induced dipoles of a diamagnetic material (Slide 6).
- d) Atoms with no dipoles describe a diamagnetic material at $H = 0$; a paramagnet has permanent dipoles.

### Source

Session 15, Slides 6 and 8.

## Q44.8 A diamagnetic material of the slides

- id: B44-Q8
- concept_id: u7-magnetism-classification
- format: identify
- asks: classification

Which of the following materials is listed on the slides as diamagnetic?

a) Al
b) Ni
c) MnO
d) Cu

### Answer

d

### Explanation

Slides 5 and 6 list Cu, Au, Ag, Si, Zn and Al₂O₃ as diamagnetic materials ($\chi_m \sim -10^{-5}$).

- a) Al is one of the paramagnetic examples (Slides 5 and 8); it is easy to confuse with Al₂O₃, which is diamagnetic.
- b) Ni is ferromagnetic (Slides 5 and 9).
- c) MnO is the antiferromagnetic example of Slide 10.

### Source

Session 15, Slides 5-6.

## Q44.9 Origin of the moment in ferromagnetic metals

- id: B44-Q9
- concept_id: u7-ferromagnetism
- format: complete-sentence
- asks: cause

The permanent magnetic moment of ferromagnetic metals comes mainly from:

a) the orbital moments of their electrons
b) the spin moments of their electrons
c) dipoles induced by the applied field
d) pairs of opposite spins in each atom

### Answer

b

### Explanation

Slide 9: the permanent magnetic moment of ferromagnetic materials is due fundamentally to the spin magnetic moments, with only a small contribution from the orbital moments.

- a) The orbital moments are the small contribution, not the main one.
- c) Induced dipoles are not permanent; they describe diamagnetism (Slide 6).
- d) Paired opposite spins cancel each other (Slide 3); the moment comes from the unpaired spins.

### Source

Session 15, Slides 3 and 9.

## Q44.10 Why an antiferromagnet has no net moment

- id: B44-Q10
- concept_id: u7-antiferromagnetism
- format: complete-sentence
- asks: cause

An antiferromagnetic solid such as MnO has no net magnetic moment because its dipoles:

a) are induced by the applied field and vanish with it
b) are permanent but point at random
c) are antiparallel and of unequal size
d) are antiparallel and of equal size

### Answer

d

### Explanation

Slide 10: the permanent dipoles (the spins of the Mn²⁺ ions in MnO) are oriented antiparallel with the same magnitude, so they cancel and the solid has no net moment.

- a) Induced dipoles belong to the diamagnetic materials; the dipoles of MnO are permanent.
- b) Random permanent dipoles describe a paramagnetic material; MnO below its Néel temperature has an ordered, antiparallel arrangement.
- c) Unequal antiparallel moments do not cancel: that is ferrimagnetism, which leaves a net moment (Slide 11).

### Source

Session 15, Slides 10-11.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
