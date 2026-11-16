---
materia: Aerospace Materials I
tema: "Unit 7: atomic moments of the 3d elements, susceptibility and induction, classification of materials by chi and by B against B0, examples of each type of magnetism and arrangement of dipoles (applied)"
bank_id: B58
title: "Magnetic moments, fields and types of magnetism applied"
category: mt2_test_block
unit: 7
concepts:
  - u7-moment-per-mole-3d-table
  - u7-iron-manganese-moment-pairing
  - u7-induction-from-susceptibility
  - u7-classify-by-susceptibility-table
  - u7-induction-line-types
  - u7-examples-of-each-magnetism
  - u7-oriented-dipoles-zero-field
  - u7-orbital-spin-moment-sum
  - u7-titanium-gold-induction
  - u7-susceptibility-ratio-ferro-para
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 15 Slides 3-13."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-7
---

# Bank B58 — Magnetic moments, fields and types of magnetism applied

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 15, Slides 3-13.

## Q58.1 Moment of a mole of chromium atoms

- id: B58-Q1
- concept_id: u7-moment-per-mole-3d-table
- format: numeric
- asks: calculation
- calc: 5*9.27e-24*6.022e23

The table gives the net magnetic moment of an atom of some 3d elements:

| Element | Sc | Ti | V | Cr | Mn | Fe | Co | Ni | Cu |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Moment ($\mu_B$) | 1 | 2 | 3 | 5 | 5 | 4 | 3 | 2 | 0 |

Determine the total moment of one mole of chromium atoms with all their moments aligned, with $\mu_B = 9.27\times10^{-24}$ A·m² and $N_A = 6.022\times10^{23}$ atoms/mol:

a) 16.7 A·m²
b) $4.64\times10^{-23}$ A·m²
c) 27.9 A·m²
d) 22.3 A·m²

### Answer

c

### Explanation

Session 15, Slide 3: the moment of the atom is the sum of its electron moments, 5 $\mu_B$ for Cr, so the mole gives $5\cdot9.27\times10^{-24}\cdot6.022\times10^{23} = 27.9$ A·m².

- a) The row of Co (3 $\mu_B$) was read instead of that of Cr: $3\cdot9.27\times10^{-24}\cdot6.022\times10^{23} = 16.7$.
- b) The moment of a single atom, $5\mu_B$, was given: the number of atoms in the mole was not applied.
- d) The row of Fe (4 $\mu_B$) was read instead of that of Cr: $4\cdot9.27\times10^{-24}\cdot6.022\times10^{23} = 22.3$.

### Source

Session 15, Slide 3.

## Q58.2 Why iron has less moment than manganese

- id: B58-Q2
- concept_id: u7-iron-manganese-moment-pairing
- format: complete-sentence
- asks: cause

An Fe atom has one 3d electron more than a Mn atom, but its moment is 4 $\mu_B$ against 5 $\mu_B$ for Mn, because the sixth 3d electron:

a) takes the spin opposite to the other five, which cancels one moment
b) has no spin moment, which reduces the five moments of Mn by one
c) moves into the 4s shell, which removes one of the 3d moments
d) raises the orbital moment, which opposes the spin moments

### Answer

a

### Explanation

Session 15, Slide 3: the moment of an atom is the sum of the moments of its electrons; the five 3d orbitals of Mn hold five parallel spins (5 $\mu_B$), and the sixth electron of Fe must pair with one of them with the opposite spin, so one moment is cancelled and $5 - 1 = 4$ $\mu_B$ remain.

- b) A paired electron was treated as spinless: every electron carries a spin moment $\pm\mu_B$, and this one has the opposite sign.
- c) The sixth electron stays in the 3d shell, as the table of the slide shows; a move to 4s would not cancel an existing moment.
- d) The orbital contribution was invoked: the moments of the table come from the spin of the 3d electrons, and the pairing of spins is what lowers the sum.

### Source

Session 15, Slide 3.

## Q58.3 Induction in a material with a given susceptibility

- id: B58-Q3
- concept_id: u7-induction-from-susceptibility
- format: numeric
- asks: calculation
- calc: 1.257e-6*(1+4.0)*1.2e3*1e3

A material has a magnetic susceptibility $\chi_m = 4.0$ and is placed in a field $H = 1.2\times10^{3}$ A/m. Determine the induction $B$ inside it, with $\mu_0 = 1.257\times10^{-6}$ H/m:

a) 6.03 mT
b) 7.54 mT
c) 1.51 mT
d) $-4.53$ mT

### Answer

b

### Explanation

Session 15, Slide 4: $M = \chi_m H$ and $B = \mu_0 H + \mu_0 M = \mu_0(1+\chi_m)H = \mu_r\mu_0 H$, with $\mu_r = 1+\chi_m = 5.0$: $B = 1.257\times10^{-6}\cdot5.0\cdot1.2\times10^{3} = 7.54\times10^{-3}$ T.

- a) The relative permeability was taken equal to the susceptibility, $\mu_r = \chi_m = 4.0$.
- c) The contribution of the magnetization was left out: $\mu_0 H = 1.51$ mT is the induction in vacuum.
- d) A sign slip, $\mu_r = 1-\chi_m = -3.0$: with $\chi_m > 0$ the material strengthens the field, so $B > \mu_0 H$.

### Source

Session 15, Slide 4.

## Q58.4 Classifying three materials from their susceptibility

- id: B58-Q4
- concept_id: u7-classify-by-susceptibility-table
- format: diagram-reading
- asks: classification

Three materials have the susceptibilities $\chi_m$ shown:

| Material | A | B | C |
| --- | --- | --- | --- |
| $\chi_m$ | $+3.0\times10^{-4}$ | $+5.0\times10^{5}$ | $-1.2\times10^{-5}$ |

Which option classifies A, B and C, in that order?

a) Paramagnetic, ferromagnetic, paramagnetic
b) Diamagnetic, ferromagnetic, paramagnetic
c) Paramagnetic, paramagnetic, diamagnetic
d) Paramagnetic, ferromagnetic, diamagnetic

### Answer

d

### Explanation

Session 15, Slides 5, 6, 8 and 9: a paramagnetic material has $10^{-5} \le \chi_m < 10^{-2}$ (A), a ferromagnetic one has a very large $\chi_m$, up to $10^{6}$ (B), and a diamagnetic one has $\chi_m < 0$ (C).

- a) Only the size of $|\chi_m|$ was used for C ($1.2\times10^{-5}$ is of paramagnetic size): its negative sign makes it diamagnetic.
- b) The meaning of the sign was inverted: a small positive $\chi_m$ is paramagnetic and a negative one diamagnetic.
- c) Every positive susceptibility was called paramagnetic: B, with $\chi_m$ up to $10^{6}$, is ferromagnetic.

### Source

Session 15, Slides 5, 6, 8 and 9.

## Q58.5 Diamagnetic material on a B against mu0 H plot

- id: B58-Q5
- concept_id: u7-induction-line-types
- format: diagram-reading
- asks: figure-reading

In the schematic plot of the induction $B$ against $\mu_0H$, the dashed line is the induction in vacuum. Which line corresponds to a diamagnetic material?

![[attachments/MAT-MT2/u7-b58-b-lines.svg]]

a) Line 1
b) Line 2
c) Line 3
d) The dashed line

### Answer

b

### Explanation

Session 15, Slides 6 and 8: for a diamagnetic material $B < B_0 = \mu_0H$ ($\mu_r < 1$, $\chi_m < 0$), so its line lies below the dashed vacuum line: line 2. Line 1 ($B > B_0$) is a paramagnetic material and line 3, with a much larger slope, a ferromagnetic one.

- a) The trend was inverted: line 1 lies above the vacuum line, which is the paramagnetic behaviour ($B > \mu_0H$).
- c) The strongest response was read as diamagnetic: line 3 has $B \gg \mu_0H$, as a ferromagnetic material.
- d) Diamagnetism was taken as no response: on the vacuum line $B = \mu_0H$ the dipoles would add nothing, whereas the induced dipoles of a diamagnet oppose the field.

### Source

Session 15, Slides 5, 6, 8 and 9.

## Q58.6 Ferro-, antiferro- and ferrimagnetic examples

- id: B58-Q6
- concept_id: u7-examples-of-each-magnetism
- format: identify
- asks: classification

Which one of the following lists gives, in this order, a ferromagnetic, an antiferromagnetic and a ferrimagnetic material?

a) Co, MnO, a garnet M₃Fe₅O₁₂
b) Ni, a ferrite AB₂O₄, MnO
c) Al, Cr, a garnet M₃Fe₅O₁₂
d) Fe, Cu, a ferrite AB₂O₄

### Answer

a

### Explanation

Session 15, Slides 9-11: Fe, Ni and Co are ferromagnetic; Cr, Mn and MnO are antiferromagnetic; the ceramics ferrites (AB₂O₄), garnets (M₃Fe₅O₁₂) and AB₁₂O₁₉ are ferrimagnetic. Co, MnO and a garnet follow the asked order.

- b) The second and third materials were swapped: the ferrite is the ferrimagnetic ceramic and MnO the antiferromagnetic oxide.
- c) Aluminium was taken as ferromagnetic: it is paramagnetic (Slide 8).
- d) Copper was taken as antiferromagnetic: it is diamagnetic (Slide 6).

### Source

Session 15, Slides 6, 8, 9, 10 and 11.

## Q58.7 Types with oriented dipoles without a field

- id: B58-Q7
- concept_id: u7-oriented-dipoles-zero-field
- format: identify
- asks: classification

Which group lists only types of magnetism whose dipoles are oriented in the absence of an applied field?

a) Ferromagnetic, antiferromagnetic and paramagnetic
b) Paramagnetic, ferrimagnetic and diamagnetic
c) Ferromagnetic, antiferromagnetic and ferrimagnetic
d) Antiferromagnetic, ferrimagnetic and diamagnetic

### Answer

c

### Explanation

Session 15, Slide 13 (summary): the dipoles are oriented in the absence of a field in ferromagnetic, antiferromagnetic and ferrimagnetic materials; in paramagnetic materials they are oriented only in the presence of a field, and diamagnetic materials have no permanent dipoles, only induced ones.

- a) The permanent dipoles of a paramagnet were taken as oriented: without a field they point at random (Slide 8).
- b) Paramagnetic and diamagnetic were included: neither has oriented dipoles at zero field; only the ferrimagnetic one belongs to the group.
- d) The induced dipoles of a diamagnet were counted: they exist only while a field acts (Slide 6).

### Source

Session 15, Slides 6, 8 and 13.

## Q58.8 Net moment of two electrons

- id: B58-Q8
- concept_id: u7-orbital-spin-moment-sum
- format: numeric
- asks: calculation
- calc: 2 + (-1) + 1 + 1

Two electrons of an atom have orbital quantum numbers $m_l = +2$ and $m_l = -1$, and both have a spin moment of $+\mu_B$. Determine the net magnetic moment of the two electrons, in Bohr magnetons:

a) 5 $\mu_B$
b) 1 $\mu_B$
c) 2 $\mu_B$
d) 3 $\mu_B$

### Answer

d

### Explanation

Session 15, Slide 3: the orbital moment of each electron is $m_l\mu_B$ and its spin moment $\pm\mu_B$, and the moment of the atom is the sum of those of all its electrons: $(+2) + (-1) + (+1) + (+1) = 3$ $\mu_B$.

- a) The orbital contributions were added as magnitudes, $2 + 1 + 1 + 1 = 5$, without the sign of $m_l = -1$.
- b) Only the orbital moments were summed, $2 - 1 = 1$: the spin moments also count.
- c) Only the spin moments were summed, $1 + 1 = 2$: the orbital moments also count.

### Source

Session 15, Slide 3.

## Q58.9 Titanium and gold in the same field

- id: B58-Q9
- concept_id: u7-titanium-gold-induction
- format: true-statement
- asks: application

A titanium rod and a gold rod are placed, one after the other, in the same field $H$. Which one of the following statements compares their induction $B$ with $\mu_0H$?

a) Both rods have an induction slightly above $\mu_0H$
b) Titanium has an induction slightly below $\mu_0H$ and gold slightly above
c) Titanium has an induction slightly above $\mu_0H$ and gold slightly below
d) Both rods have an induction slightly below $\mu_0H$

### Answer

c

### Explanation

Session 15, Slides 6 and 8: titanium is paramagnetic ($\mu_r > 1$, $B > B_0 = \mu_0H$, a small addition) and gold is diamagnetic ($\mu_r < 1$, $B < B_0$, a small reduction).

- a) Gold was treated as paramagnetic, as if every metal strengthened the field.
- b) The two behaviours were swapped between the metals: titanium is the paramagnetic one.
- d) Titanium was treated as diamagnetic, as if every metal weakened the field.

### Source

Session 15, Slides 6 and 8.

## Q58.10 Magnetization of a ferromagnet against a paramagnet

- id: B58-Q10
- concept_id: u7-susceptibility-ratio-ferro-para
- format: numeric
- asks: calculation
- calc: 2.0e5/3.0e-4

In the same field $H$, a ferromagnetic material with $\chi_m = 2.0\times10^{5}$ and a paramagnetic one with $\chi_m = 3.0\times10^{-4}$ are magnetized. Determine the ratio $M_{ferro}/M_{para}$:

a) $6.67\times10^{8}$
b) $1.50\times10^{-9}$
c) $6.67\times10^{5}$
d) $6.67\times10^{9}$

### Answer

a

### Explanation

Session 15, Slides 4, 8 and 9: $M = \chi_m H$ with the same $H$, so $M_{ferro}/M_{para} = \chi_{ferro}/\chi_{para} = 2.0\times10^{5}/3.0\times10^{-4} = 6.67\times10^{8}$.

- b) The ratio was inverted, $\chi_{para}/\chi_{ferro}$.
- c) The exponent of the paramagnetic susceptibility was read as $10^{-1}$ instead of $10^{-4}$: $2.0\times10^{5}/0.30$.
- d) The exponent of the paramagnetic susceptibility was read as $10^{-5}$ instead of $10^{-4}$: $2.0\times10^{5}/3.0\times10^{-5}$.

### Source

Session 15, Slides 4, 8 and 9.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
