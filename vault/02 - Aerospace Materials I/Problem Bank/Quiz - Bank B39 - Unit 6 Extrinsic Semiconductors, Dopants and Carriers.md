---
materia: Aerospace Materials I
tema: "Unit 6: n-type and p-type semiconductors, donor and acceptor levels, majority and minority carriers, conductivity with complete ionisation"
bank_id: B39
title: "Extrinsic semiconductors, dopants and carriers"
category: mt2_test_block
unit: 6
concepts:
  - u6-dopant-type
  - u6-donor-acceptor-levels
  - u6-majority-carriers
  - u6-n-type-conductivity-calc
  - u6-dopant-concentration-calc
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 13 Slides 31 and 35-38."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B39 — Extrinsic semiconductors, dopants and carriers

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 13, Slides 31 and 35-38.

## Q39.1 Silicon doped with indium

- id: B39-Q1
- concept_id: u6-dopant-type
- format: complete-sentence
- asks: classification

Silicon doped with indium in substitutional solid solution is:

a) A p-type semiconductor, with indium acting as an acceptor
b) An n-type semiconductor, with indium acting as a donor
c) A p-type semiconductor, with indium acting as a donor
d) An n-type semiconductor, with indium acting as an acceptor

### Answer

a

### Explanation

Session 13, Slides 35 and 37: indium belongs to group IIIA, with fewer valence electrons (3) than silicon (4); it leaves a bond with a missing electron, behaves as an acceptor and makes the semiconductor p-type.

- b) Swaps both choices: donors (more valence electrons, group VA) give n-type material.
- c) Right type, wrong role: in a p-type semiconductor the dopant accepts electrons, it does not donate them.
- d) Right role, wrong type: acceptors create holes, the majority carriers of a p-type material.

### Source

Session 13, Slides 35-37.

## Q39.2 Dopant for n-type silicon

- id: B39-Q2
- concept_id: u6-dopant-type
- format: identify
- asks: classification

Which dopant makes silicon an n-type extrinsic semiconductor?

a) Boron
b) Gallium
c) Aluminium
d) Phosphorus

### Answer

d

### Explanation

Session 13, Slides 35-36: phosphorus (group VA, five valence electrons) uses four of them in the covalent bonds of silicon and has one loosely bound excess electron: it is a donor and the material is n-type.

- a) Boron (group IIIA, three valence electrons) is an acceptor and gives p-type silicon (Slide 37).
- b) Gallium is also a group IIIA acceptor (Slide 37).
- c) Aluminium is the third group IIIA acceptor of the slide; it gives p-type silicon.

### Source

Session 13, Slides 35-37.

## Q39.3 Arsenic in germanium

- id: B39-Q3
- concept_id: u6-dopant-type
- format: true-statement
- asks: cause

Which one of the following statements about germanium doped with arsenic is TRUE?

a) Arsenic is a donor because its atoms are larger than germanium atoms
b) Arsenic is an acceptor because it has one fewer valence electron
c) Arsenic is a donor because it has one more valence electron
d) Arsenic is an acceptor because it creates a level near the valence band

### Answer

c

### Explanation

Session 13, Slides 35-36: arsenic belongs to group VA (five valence electrons) and germanium to group IVA (four); the excess electron is loosely bound and easily given to the conduction band, so arsenic is a donor.

- a) Right role with the wrong cause: what makes a donor is the number of valence electrons, not the atom size.
- b) The count is inverted: one fewer valence electron is the condition for an acceptor (group IIIA).
- d) A level near the valence band is an acceptor level (Slide 37); arsenic creates a donor level just below the conduction band.

### Source

Session 13, Slides 35-37.

## Q39.4 Picture of an n-type semiconductor

- id: B39-Q4
- concept_id: u6-donor-acceptor-levels
- format: choose-figure
- asks: figure-reading

Which picture describes the band structure of an n-type extrinsic semiconductor?

a) ![[attachments/MAT-MT2/u6-impurity-scheme-1.svg]]
b) ![[attachments/MAT-MT2/u6-impurity-scheme-2.svg]]
c) ![[attachments/MAT-MT2/u6-impurity-scheme-3.svg]]
d) ![[attachments/MAT-MT2/u6-impurity-scheme-4.svg]]

### Answer

a

### Explanation

Session 13, Slide 36: the donor atoms create a donor level $E_d$ inside the gap, very close to the conduction band and occupied by the loosely bound electrons (filled dots in picture A).

- b) A level just above the valence band with empty states is the acceptor level of a p-type semiconductor (Slide 37).
- c) Electrons in the conduction band and an equal number of holes in the valence band, with no impurity level, is an intrinsic semiconductor (Slide 27).
- d) A wide gap of 6 eV with no level is an insulator (Slide 8).

### Source

Session 13, Slides 8, 27, 36 and 37.

## Q39.5 Position of the acceptor level

- id: B39-Q5
- concept_id: u6-donor-acceptor-levels
- format: complete-sentence
- asks: definition

In a p-type semiconductor, the acceptor level $E_a$ lies:

a) Just below the bottom of the conduction band
b) In the middle of the band gap
c) Just above the top of the valence band
d) Inside the conduction band

### Answer

c

### Explanation

Session 13, Slide 37: the acceptor creates a level $E_a$ in the gap just above the top of the valence band, so a small energy $E_a - E_v$ lifts a valence electron into it and leaves a hole.

- a) That is the position of the donor level $E_d$ of an n-type semiconductor (Slide 36).
- b) A mid-gap level would need about $E_g/2$ to be reached; the slides give small energies (0.045 to 0.160 eV in Si, Slide 40).
- d) A level inside the conduction band would not be a level in the gap; the conduction band already holds the free electrons.

### Source

Session 13, Slides 36, 37 and 40.

## Q39.6 Names of the carrier concentrations

- id: B39-Q6
- concept_id: u6-majority-carriers
- format: false-statement
- asks: definition

Which one of the following statements about the carrier concentrations of extrinsic semiconductors is FALSE?

a) In n-type material, $n_n$ is the majority-carrier concentration
b) In p-type material, $p_p$ is the majority-carrier concentration
c) In n-type material, $p_n$ is the minority-carrier concentration
d) In p-type material, $n_p$ is the majority-carrier concentration

### Answer

d

### Explanation

Session 13, Slide 38: in p-type material the majority carriers are holes, $p_p$, and the electrons, $n_p$, are the minority carriers. Statement d) is false.

- a) True: electrons in n-type material, $n_n$, are the majority carriers.
- b) True: holes in p-type material, $p_p$, are the majority carriers.
- c) True: holes in n-type material, $p_n$, are the minority carriers.

### Source

Session 13, Slide 38.

## Q39.7 Majority carriers and conductivity

- id: B39-Q7
- concept_id: u6-majority-carriers
- format: true-statement
- asks: comparison

Which one of the following statements about extrinsic semiconductors is TRUE?

a) In n-type silicon $n_e \gg n_H$, so $\sigma \approx n_e|q_e|\mu_e$
b) In p-type silicon electrons are the majority carriers
c) In n-type silicon electrons and holes are equal in number
d) In p-type silicon $\sigma \cong n_e|q_e|\mu_e$

### Answer

a

### Explanation

Session 13, Slides 36-37: in n-type material the electrons in the conduction band are the majority carriers, $n_e \gg n_H$, so $\sigma \approx n_e|q_e|\mu_e$; in p-type material $p \gg n$ and $\sigma \cong p|q_e|\mu_H$.

- b) n and p swapped: holes are the majority carriers of p-type silicon.
- c) Equal numbers of electrons and holes describe an intrinsic semiconductor.
- d) Uses the n-type formula for a p-type material: the holes and their mobility $\mu_H$ dominate there.

### Source

Session 13, Slides 28 and 36-37.

## Q39.8 Boron content and holes

- id: B39-Q8
- concept_id: u6-majority-carriers
- format: cause-effect
- asks: effect

With an increase in the boron content of pure silicon, the hole concentration:

a) Decreases, as boron atoms fill the holes
b) Increases, as each boron atom accepts a valence electron
c) Increases, as boron atoms give free electrons
d) Stays equal to the electron concentration

### Answer

b

### Explanation

Session 13, Slides 37-38: boron (three valence electrons) leaves a bond with a missing electron; a small energy lifts a valence electron into the acceptor level, leaving a hole in the valence band. More boron gives more holes, which become the majority carriers.

- a) Inverted: boron creates holes, it does not remove them.
- c) Right trend with the donor mechanism: giving free electrons is what group VA atoms do.
- d) Equal concentrations hold only in an intrinsic semiconductor; doping makes $p \gg n$.

### Source

Session 13, Slides 37-38.

## Q39.9 Conductivity of arsenic-doped silicon

- id: B39-Q9
- concept_id: u6-n-type-conductivity-calc
- format: numeric
- asks: calculation
- calc: 2.0e22*q*0.135

Silicon is doped with $2.0\times10^{22}$ arsenic atoms/m³, all ionised. With $\mu_e = 0.135$ m²/(V·s) and $\mu_h = 0.048$ m²/(V·s), determine its conductivity:

a) 154 (Ω·m)⁻¹
b) 433 (Ω·m)⁻¹
c) 586 (Ω·m)⁻¹
d) 865 (Ω·m)⁻¹

### Answer

b

### Explanation

Session 13, Slide 36: arsenic is a donor, so with complete ionisation $n_e = 2.0\times10^{22}$ m⁻³ and $\sigma \approx n_e|q_e|\mu_e = 2.0\times10^{22}\cdot1.6\times10^{-19}\cdot0.135 = 433$ (Ω·m)⁻¹ (the intrinsic carriers, $1.5\times10^{16}$ m⁻³, are negligible).

- a) The hole mobility was used, as if the material were p-type: $2.0\times10^{22}\cdot1.6\times10^{-19}\cdot0.048 = 154$.
- c) Both mobilities were added, $0.183$, as for an intrinsic semiconductor: 586; in n-type material holes are minority carriers.
- d) Each arsenic atom was taken to give two electrons: 865; it has only one excess electron.

### Source

Session 13, Slides 31 and 36.

## Q39.10 Donor concentration for a target resistivity

- id: B39-Q10
- concept_id: u6-dopant-concentration-calc
- format: numeric
- asks: calculation
- calc: (1/0.010)/(q*0.135)

Phosphorus-doped silicon must have a resistivity of 0.010 Ω·m at room temperature. With $\mu_e = 0.135$ m²/(V·s), $\mu_h = 0.048$ m²/(V·s) and complete ionisation, determine the phosphorus concentration:

a) $4.62\times10^{17}$ m⁻³
b) $3.41\times10^{21}$ m⁻³
c) $4.62\times10^{21}$ m⁻³
d) $1.30\times10^{22}$ m⁻³

### Answer

c

### Explanation

Session 13, Slides 13 and 36: $\sigma = 1/\rho = 100$ (Ω·m)⁻¹ and $\sigma \approx n_e|q_e|\mu_e$, so $n_e = 100/(1.6\times10^{-19}\cdot0.135) = 4.62\times10^{21}$ m⁻³, one electron per phosphorus atom.

- a) The resistivity was used as if it were the conductivity: $0.010/(1.6\times10^{-19}\cdot0.135) = 4.62\times10^{17}$.
- b) Both mobilities were added, $0.183$, as for an intrinsic semiconductor: $3.41\times10^{21}$.
- d) The hole mobility was used, as if phosphorus gave holes: $1.30\times10^{22}$.

### Source

Session 13, Slides 13, 31 and 36.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
