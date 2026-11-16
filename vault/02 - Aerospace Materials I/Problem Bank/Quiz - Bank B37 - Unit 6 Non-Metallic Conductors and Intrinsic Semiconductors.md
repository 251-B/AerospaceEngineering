---
materia: Aerospace Materials I
tema: "Unit 6: conductive polymers, graphene and ceramics; semiconductor types; carriers of intrinsic semiconductors"
bank_id: B37
title: "Non-metallic conductors and intrinsic semiconductors"
category: mt2_test_block
unit: 6
concepts:
  - u6-polymers-graphene
  - u6-conductive-ceramics
  - u6-semiconductor-definition-types
  - u6-intrinsic-resistivity-calc
  - u6-intrinsic-carriers
difficulty: 1
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 13 Slides 20-22, 25-28 and 31-33."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B37 — Non-metallic conductors and intrinsic semiconductors

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 13, Slides 20-22, 25-28 and 31-33.

## Q37.1 Charge transport in conductive polymers

- id: B37-Q1
- concept_id: u6-polymers-graphene
- format: complete-sentence
- asks: definition

In conductive polymers, the main mechanism for transmitting the electric charge is:

a) The movement of ions through vacancies
b) The movement of delocalised electrons between redox sites
c) The movement of holes created by boron dopants
d) The free electron cloud of the metallic bond

### Answer

b

### Explanation

Session 13, Slide 20: the main mechanism in conductive polymers is the movement of delocalised electrons, an exchange reaction of electrons between neighbouring redox sites.

- a) Ions moving through vacancies is the ionic mechanism of some ceramics (Slide 22).
- c) Holes from boron are the carriers of p-type silicon (Slide 37), not of polymers.
- d) The electron cloud of the metallic bond is the mechanism of metals (Slide 10); polymers have no metallic bond.

### Source

Session 13, Slides 10, 20, 22 and 37.

## Q37.2 Graphene

- id: B37-Q2
- concept_id: u6-polymers-graphene
- format: true-statement
- asks: comparison

Which one of the following statements about graphene is TRUE?

a) Its conductivity is higher than that of copper
b) It is a stack of many hexagonal carbon layers
c) Its charge carriers are ions moving between layers
d) Its conductivity is close to that of silicon

### Answer

a

### Explanation

Session 13, Slide 21: graphene has $\sigma = 0.96\times10^{8}$ (Ω·m)⁻¹ against $0.60\times10^{8}$ (Ω·m)⁻¹ for Cu, thanks to a huge $\pi$ cloud of delocalised electrons.

- b) A stack of layers is graphite; graphene is a single layer of the hexagonal lattice.
- c) The carriers are delocalised electrons that move over the surface, not ions.
- d) Silicon has $4.5\times10^{-4}$ (Ω·m)⁻¹ in the same table, about eleven orders of magnitude lower.

### Source

Session 13, Slide 21.

## Q37.3 Use of ionic ceramic conductors

- id: B37-Q3
- concept_id: u6-conductive-ceramics
- format: identify
- asks: application

Which application uses the ionic conduction of advanced ceramics?

a) Heating elements
b) Resistors
c) Solid oxide fuel cells
d) Electrodes

### Answer

c

### Explanation

Session 13, Slide 22: ionic conduction (anions or cations moving through vacancies or interstitial voids at high temperature) is used in gas sensors, fuel cells and batteries; the slide shows a solid oxide fuel cell with oxygen ions crossing the electrolyte.

- a) Heating elements are listed under electronic conduction (impurities with a different valence or rare-earth elements).
- b) Resistors are also uses of electronic conduction in ceramics.
- d) Electrodes are the third electronic use of the slide, not an ionic one.

### Source

Session 13, Slide 22.

## Q37.4 Mechanism of ionic conduction

- id: B37-Q4
- concept_id: u6-conductive-ceramics
- format: complete-sentence
- asks: definition

In an ionic conductive ceramic, the charge is carried by the movement of:

a) Anions or cations through vacancies or interstitial voids
b) Free electrons of a metallic bond
c) Delocalised $\pi$ electrons over a single layer
d) Electrons given by dopants of a different valence

### Answer

a

### Explanation

Session 13, Slide 22: ionic mechanism, movement of anions or cations through vacancies or interstitial voids at high temperatures (movement of ions, or equivalently of vacancies, and of small interstitial cations).

- b) A metallic electron cloud belongs to metals (Slide 10).
- c) Delocalised $\pi$ electrons describe graphene (Slide 21).
- d) Electrons from impurities with a different valence are the electronic mechanism of conductive ceramics, the other option of the same slide.

### Source

Session 13, Slides 10, 21 and 22.

## Q37.5 Extrinsic semiconductors

- id: B37-Q5
- concept_id: u6-semiconductor-definition-types
- format: complete-sentence
- asks: definition

The electrical properties of an extrinsic semiconductor are determined by:

a) The inherent properties of the pure material
b) A band gap larger than 2 eV
c) The movement of ions through the lattice
d) Dopants with a different number of valence electrons

### Answer

d

### Explanation

Session 13, Slide 26: in extrinsic semiconductors the electrical properties are given by adding dopants with a number of valence electrons different from the solvent, usually in substitutional solid solution at 100 to 1000 ppm.

- a) This defines the intrinsic semiconductors (pure Si and Ge), the neighbouring concept.
- b) A gap above 2 eV defines an insulator (Slide 8).
- c) Ion movement is ionic conduction (Slides 10 and 22), not the semiconductor mechanism.

### Source

Session 13, Slides 8, 22 and 26.

## Q37.6 General features of semiconductors

- id: B37-Q6
- concept_id: u6-semiconductor-definition-types
- format: true-statement
- asks: definition

Which one of the following statements about semiconductors is TRUE?

a) Their valence band is half filled
b) Their conductivity is mediocre but easily controllable
c) Their band gap is larger than 2 eV
d) Their dopant content is typically 10 to 20 wt%

### Answer

b

### Explanation

Session 13, Slide 25: semiconductors are mediocre conductors whose conductivity is easily controllable, which became useful with the manufacture of materials of extremely high purity.

- a) A half-filled valence band is the band structure of a conductor (Slide 6); a semiconductor has a full valence band.
- c) Semiconductors have $E_g < 2$ eV; above 2 eV the material is an insulator (Slides 8 and 25).
- d) Dopants are added at low concentrations, 100 to 1000 ppm (Slide 26), not tens of percent.

### Source

Session 13, Slides 6, 8, 25 and 26.

## Q37.7 Resistivity of intrinsic silicon

- id: B37-Q7
- concept_id: u6-intrinsic-resistivity-calc
- format: numeric
- asks: calculation
- calc: 1/(1.5e16*q*(0.135+0.048))

Intrinsic silicon has $n_i = 1.5\times10^{16}$ m⁻³, $\mu_e = 0.135$ m²/(V·s) and $\mu_h = 0.048$ m²/(V·s). Determine its electrical resistivity:

a) $4.40\times10^{-4}$ Ω·m
b) $1.14\times10^{3}$ Ω·m
c) $2.27\times10^{3}$ Ω·m
d) $3.08\times10^{3}$ Ω·m

### Answer

c

### Explanation

Session 13, Slide 28: $\sigma = n|q_e|(\mu_e+\mu_h)$ with $n = p = n_i$: $\sigma = 1.5\times10^{16}\cdot1.6\times10^{-19}\cdot0.183 = 4.40\times10^{-4}$ (Ω·m)⁻¹, so $\rho = 1/\sigma = 2.27\times10^{3}$ Ω·m (the table of Slide 31 gives about 2300 Ω·m).

- a) The conductivity was given instead of its reciprocal, the resistivity.
- b) The carrier density was counted twice ($2n_i$ with the sum of mobilities), which halves the resistivity: $1.14\times10^{3}$ Ω·m.
- d) Only the electrons were counted: $1/(n_i|q_e|\mu_e) = 3.08\times10^{3}$ Ω·m; in an intrinsic semiconductor holes conduct too.

### Source

Session 13, Slides 28 and 31.

## Q37.8 Carriers of an intrinsic semiconductor

- id: B37-Q8
- concept_id: u6-intrinsic-carriers
- format: complete-sentence
- asks: definition

In an intrinsic semiconductor, the charge carriers are:

a) Conduction electrons and valence-band holes in equal numbers
b) Only electrons in the conduction band
c) Only holes in the valence band
d) Electrons and holes, with far more electrons than holes

### Answer

a

### Explanation

Session 13, Slides 27-28: each excited electron leaves a hole in the valence band, so there are two types of carriers, with $n_e = n_H = n$.

- b) Forgets the hole left behind by each excited electron.
- c) Forgets the electron that was excited into the conduction band.
- d) $n_e \gg n_H$ describes an n-type extrinsic semiconductor (Slide 36).

### Source

Session 13, Slides 27-28 and 36.

## Q37.9 Excitation of a valence electron

- id: B37-Q9
- concept_id: u6-intrinsic-carriers
- format: what-happens
- asks: effect
- check: 1.3 > 1.1

What will happen to a valence electron of pure silicon ($E_g = 1.1$ eV) that receives 1.3 eV:

a) It will move to a donor level below the conduction band
b) It will stay bound, as only dopants free electrons
c) It will become free and leave no hole behind
d) It will become a free electron and leave a hole

### Answer

d

### Explanation

Session 13, Slides 27-28: once the critical energy (here more than $E_g = 1.1$ eV) is supplied, the valence electron leaves its bonding position, becomes a free conduction electron and leaves a positively charged hole in the lattice.

- a) Pure silicon has no donor levels; they appear only with group VA dopants (Slide 36).
- b) Intrinsic excitation across the gap frees electrons without any dopant (Slide 27).
- c) The vacancy left in the bond is the hole, the second carrier of the intrinsic semiconductor.

### Source

Session 13, Slides 8, 27-28 and 36.

## Q37.10 Electrons and holes in an intrinsic semiconductor

- id: B37-Q10
- concept_id: u6-intrinsic-carriers
- format: false-statement
- asks: comparison

Which one of the following statements about an intrinsic semiconductor is FALSE?

a) The numbers of electrons and holes are equal, $n = p$
b) Holes are more mobile than electrons, $\mu_H > \mu_e$
c) A hole carries a charge of $+1.6\times10^{-19}$ C
d) Both electrons and holes add to the conductivity

### Answer

b

### Explanation

Session 13, Slides 28 and 33: in an intrinsic semiconductor $\mu_e > \mu_H$ (Si: 0.14 against 0.05; Ge: 0.38 against 0.18 m²/(V·s)), so statement b) is false.

- a) True: every excited electron leaves one hole, $n = p$ (Slide 28).
- c) True: the hole has the charge of the electron with the opposite sign (Slide 28).
- d) True: $\sigma = n|q_e|\mu_e + p|q_e|\mu_H$ (Slide 28).

### Source

Session 13, Slides 28 and 33.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
