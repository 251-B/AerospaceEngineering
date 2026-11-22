---
materia: Aerospace Materials I
tema: "Unit 7: atomic moments of the 3d elements, susceptibility and induction, classification of materials by chi and by B against B0, examples of each type of magnetism and arrangement of dipoles (applied)"
bank_id: B58
title: "Magnetic moments, fields and types of magnetism applied"
category: mt2_test_block
unit: 7
concepts:
  - u7-3d-shell-pairing-trend
  - u7-iron-manganese-moment-pairing
  - u7-induction-field-sign
  - u7-classify-by-susceptibility-table
  - u7-induction-line-types
  - u7-examples-of-each-magnetism
  - u7-oriented-dipoles-zero-field
  - u7-ferrimagnetism
  - u7-titanium-gold-induction
  - u7-magnetization-removal-comparison
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf, including Q11 of MATERIALS_THIRDPARTIAL_2020_V2.pdf p. 5. Content and data from Session 15 Slides 3-13."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-7
---

# Bank B58 — Magnetic moments, fields and types of magnetism applied

> [!info] Includes official exam questions
> Ten test questions written for the bank in the style of Part I of Assessment Test II, including an official Unit 7 MCQ from the 2020 paper (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 15, Slides 3-13.

## Q58.1 Net atomic moments across the 3d transition metals

- id: B58-Q1
- concept_id: u7-3d-shell-pairing-trend
- format: topic-true
- asks: cause

Regarding the net magnetic moments of isolated 3d transition-metal atoms (from Sc to Cu), which one of the following statements is TRUE:

a) The atomic moment grows steadily with atomic number up to Cu because each added electron adds one Bohr magneton
b) The atomic moment rises up to half-filling of the 3d shell and then falls to zero in Cu as spins pair up
c) The outer 4s electrons provide the main magnetic moment of transition metals while all 3d spins cancel out
d) Isolated Fe atoms carry a larger net moment than isolated Mn atoms because Fe has one extra 3d electron

### Answer

b

### Explanation

Session 15, Slide 3: the 3d shell holds five orbitals; from Sc (1 $\mu_B$) to Cr and Mn (5 $\mu_B$) unpaired spins accumulate, and beyond half-filling (Fe 4, Co 3, Ni 2, Cu 0 $\mu_B$) added electrons pair with opposite spins and cancel moments until the full 3d shell of Cu has zero net moment.

- a) Ignores Pauli spin pairing after five 3d electrons: Cu has the highest atomic number in the row yet 0 $\mu_B$.
- c) Swaps the active shells: the table of Slide 3 counts unpaired 3d spins, whereas paired 4s electrons cancel out.
- d) Inverts Mn and Fe: the sixth 3d electron in Fe pairs with an opposite spin, dropping the moment from 5 $\mu_B$ (Mn) to 4 $\mu_B$ (Fe).

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

## Q58.3 Induction, magnetization and susceptibility relations

- id: B58-Q3
- concept_id: u7-induction-field-sign
- format: topic-false
- asks: comparison

Regarding magnetic field strength $H$, magnetization $M$, magnetic susceptibility $\chi_m$, and magnetic induction $B$, which one of the following statements is FALSE:

a) Inside a solid, the magnetic induction equals $\mu_0(H + M)$, combining the vacuum field and the material response
b) For linear media, $M = \chi_m H$ and the relative permeability satisfies $\mu_r = 1 + \chi_m$
c) In a ferromagnetic material with $\chi_m \gg 1$, the material term dominates so that $B \cong \mu_0 M$
d) In a paramagnetic material ($\chi_m > 0$), the internal induction $B$ is slightly lower than $\mu_0 H$

### Answer

d

### Explanation

Session 15, Slides 4 and 8: for a paramagnetic material $\chi_m > 0$ and $\mu_r = 1 + \chi_m > 1$, so $M = \chi_m H > 0$ adds to the external field and $B = \mu_0(H + M) > \mu_0 H$. Having $B < \mu_0 H$ corresponds to diamagnetism ($\chi_m < 0$).

- a) True: Slide 4 prints $B = \mu_0 H + \mu_0 M = \mu_0(H + M)$.
- b) True: combining $B = \mu_r\mu_0 H$ with $M = \chi_m H$ gives $\mu_r = 1 + \chi_m$ (Slide 4).
- c) True: for ferromagnets $\chi_m$ reaches $10^6$, so $M \gg H$ and $B \cong \mu_0 M$ (Slides 5 and 9).

### Source

Session 15, Slides 4-5 and 8-9.

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

## Q58.8 Ferrimagnetic dipoles before an external field

- id: B58-Q8
- concept_id: u7-ferrimagnetism
- format: choose-figure
- asks: classification
- origin: official-exam

Which picture shows the permanent dipole arrangement of a ferrimagnetic ceramic (such as a ferrite) before applying an external magnetic field?

a) ![[attachments/MAT-MT2/u7-dip-3.svg]]
b) ![[attachments/MAT-MT2/u7-dip-1.svg]]
c) ![[attachments/MAT-MT2/u7-dip-4.svg]]
d) ![[attachments/MAT-MT2/u7-dip-2.svg]]

### Answer

c

### Explanation

Session 15, Slides 11 and 13 (and `MATERIALS_THIRDPARTIAL_2020_V2.pdf`, p. 5 Q11): ferrimagnetic ceramics have permanent magnetic dipoles of different magnitudes aligned antiparallel without an external field, leaving a net magnetic moment (picture c).

- a) Antiparallel dipoles of equal size cancel completely and correspond to an antiferromagnetic material.
- b) Randomly oriented permanent dipoles correspond to a paramagnetic material with no external field.
- d) Parallel dipoles of equal size correspond to a ferromagnetic material within a single domain.

### Source

MATERIALS_THIRDPARTIAL_2020_V2.pdf, p. 5 Q11; Session 15, Slides 11 and 13.

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

## Q58.10 Magnetization response after removing the field

- id: B58-Q10
- concept_id: u7-magnetization-removal-comparison
- format: topic-true
- asks: effect

When an external magnetic field is applied and then removed at room temperature, which one of the following statements correctly compares diamagnetic, paramagnetic, and ferromagnetic materials?

a) Diamagnetic and paramagnetic materials lose their magnetization when $H$ returns to zero, whereas a ferromagnet can retain a remanence $B_r$
b) Paramagnetic materials retain a large permanent magnetization when $H$ returns to zero, whereas diamagnetic and ferromagnetic materials lose theirs
c) Diamagnetic materials keep induced dipoles permanently aligned opposite to $H$, whereas paramagnetic dipoles vanish once $H$ returns to zero
d) All three classes retain permanent net magnetization after $H$ returns to zero, differing in the sign and size of $B_r$

### Answer

a

### Explanation

Session 15, Slides 6, 8, 9, 13 and 17: diamagnetism is purely induced while $H$ acts, and paramagnetic permanent dipoles randomize again once $H$ is removed; only ferromagnetic (and ferrimagnetic) materials keep domain alignment and exhibit remanence $B_r$ at $H = 0$.

- b) Swaps paramagnetism and ferromagnetism: thermal agitation randomizes paramagnetic dipoles as soon as the field disappears.
- c) Inverts permanence: diamagnetic dipoles are induced and disappear with the field, whereas paramagnetic dipoles are permanent atoms that randomize.
- d) Wrongly attributes hysteresis and permanent remanence to diamagnetic and paramagnetic solids.

### Source

Session 15, Slides 6, 8, 9, 13 and 17.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
