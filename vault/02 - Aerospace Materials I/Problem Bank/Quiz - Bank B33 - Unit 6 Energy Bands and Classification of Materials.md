---
materia: Aerospace Materials I
tema: "Unit 6: energy bands, band gap and the classification of conductors, semiconductors and insulators"
bank_id: B33
title: "Energy bands and classification of materials"
category: mt2_test_block
unit: 6
concepts:
  - u6-band-formation
  - u6-valence-conduction-bands
  - u6-band-gap-classification
  - u6-conductor-band-structure
  - u6-conductivity-ranges
difficulty: 1
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf and adapted from MATERIALS_FINALEXAM_2012_ORD.pdf (Q6). Content from Session 13 Slides 3-8, 10 and 22."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B33 — Energy bands and classification of materials

> [!info] Includes official exam questions
> Ten test questions in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Question 10 adapts Question 6 of MATERIALS_FINALEXAM_2012_ORD.pdf; the remaining nine are practice items. Content: Session 13, Slides 3-8, 10 and 22.

## Q33.1 Atomic levels in a solid

- id: B33-Q1
- concept_id: u6-band-formation
- format: complete-sentence
- asks: definition

When a very large number of atoms come together to form a solid, each atomic energy level:

a) Splits into a band of closely spaced levels
b) Stays as a single discrete level
c) Becomes a gap with no allowed states
d) Splits into exactly two separate levels

### Answer

a

### Explanation

Session 13, Slide 3: two atoms give two levels, a few atoms a few close levels, and the huge number of atoms of a solid gives so many levels so close in energy that they form a continuous energy band.

- b) This is the picture of an isolated atom; it ignores the interaction of the orbitals when the atoms come into close proximity.
- c) Confuses the band with the band gap: the gap is the energy range left between two bands, not what a level turns into.
- d) Two levels is the case of two interacting atoms only; the very large number of atoms of a solid gives a band, not two levels.

### Source

Session 13, Slide 3.

## Q33.2 Interatomic separation and bands

- id: B33-Q2
- concept_id: u6-band-formation
- format: cause-effect
- asks: effect

With a decrease in interatomic separation from that of isolated atoms, the electron energy levels of the atoms:

a) Stay discrete for outer electrons, while core levels broaden
b) Narrow into single levels for both outer and core electrons
c) Broaden into bands for outer electrons, while core levels hardly change
d) Broaden into bands for core electrons more than for outer ones

### Answer

c

### Explanation

Session 13, Slides 3-4: as the atoms approach, the outer orbitals overlap and their levels broaden into bands; the core-level electrons stay almost unchanged. The solid sits at the equilibrium interatomic distance, where the bands have the width and gap of the figure.

- a) Swaps outer and core electrons: the inner levels are the ones that remain almost unchanged.
- b) Inverted trend: closer atoms interact more, so the levels spread out instead of narrowing.
- d) Right effect (broadening) given to the wrong electrons: the core orbitals overlap least, so they broaden least.

### Source

Session 13, Slides 3-4.

## Q33.3 The conduction band

- id: B33-Q3
- concept_id: u6-valence-conduction-bands
- format: complete-sentence
- asks: definition

In the band structure of a solid, the conduction band is:

a) The outermost band occupied with electrons
b) The band located immediately above the valence band
c) The energy range where no electron states exist
d) The band formed by the core-level electrons

### Answer

b

### Explanation

Session 13, Slide 4: the conduction band is the band located immediately above the valence band.

- a) This is the definition of the valence band, the neighbouring concept.
- c) This is the band gap $E_g$, which separates the two bands.
- d) The core levels stay almost discrete (Slide 3) and lie far below the valence band.

### Source

Session 13, Slides 3-4.

## Q33.4 The band gap

- id: B33-Q4
- concept_id: u6-valence-conduction-bands
- format: true-statement
- asks: definition

Which one of the following statements about the band gap $E_g$ of a solid is TRUE?

a) It is an energy range where no electron states exist
b) It is the band occupied by the valence electrons
c) It is wider in semiconductors than in insulators
d) It is the energy of the Fermi level of a metal

### Answer

a

### Explanation

Session 13, Slides 3-4: between bands a band gap may remain, an energy range where there are no electron states.

- b) That is the valence band, not the gap above it.
- c) Inverted comparison: semiconductors have $E_g < 2$ eV and insulators $E_g > 2$ eV (Slide 8).
- d) The Fermi energy $E_f$ separates filled and empty states inside the half-filled band of a metal (Slide 6); it is a level, not a gap.

### Source

Session 13, Slides 4, 6 and 8.

## Q33.5 Picture of an insulator

- id: B33-Q5
- concept_id: u6-band-gap-classification
- format: choose-figure
- asks: classification

Which picture describes the band structure of an insulator such as diamond?

a) ![[attachments/MAT-MT2/u6-bands-a.svg]]
b) ![[attachments/MAT-MT2/u6-bands-b.svg]]
c) ![[attachments/MAT-MT2/u6-bands-c.svg]]
d) ![[attachments/MAT-MT2/u6-bands-d.svg]]

### Answer

d

### Explanation

Session 13, Slide 8: an insulator has a filled valence band separated from an empty conduction band by a relatively large gap, $E_g > 2$ eV (diamond: 6 to 7 eV). Picture D has $E_g = 6$ eV.

- a) A full valence band with a narrow gap of 1.1 eV (below 2 eV) is a semiconductor, pure silicon (Slide 8).
- b) A half-filled valence band with empty states just above $E_f$ is a conductor such as Cu or Al (Slide 6).
- c) A filled band overlapping an empty band is a conductor such as Mg (Slide 6).

### Source

Session 13, Slides 6 and 8.

## Q33.6 Semiconductor by its band gap

- id: B33-Q6
- concept_id: u6-band-gap-classification
- format: identify
- asks: classification

Which one of the following solids is a semiconductor according to the band model?

a) A solid with a band gap of 5.0 eV
b) A solid with a half-filled valence band
c) A solid with a band gap of 1.4 eV
d) A solid with overlapping valence and conduction bands

### Answer

c

### Explanation

Session 13, Slides 8 and 25: a semiconductor has a full valence band and an empty conduction band separated by a narrow gap, $E_g < 2$ eV; 1.4 eV is below that limit.

- a) $E_g = 5.0$ eV is above 2 eV, so the solid is an insulator.
- b) A half-filled band is the conductor case A1 of Slide 6 (Na, Cu, Al).
- d) Overlapping bands are the conductor case A2 of Slide 6 (Mg).

### Source

Session 13, Slides 6, 8 and 25.

## Q33.7 Why copper conducts

- id: B33-Q7
- concept_id: u6-conductor-band-structure
- format: true-statement
- asks: cause

Which one of the following statements about the band structure of conductors is TRUE?

a) Magnesium conducts because its 3s band is half filled
b) Copper conducts because its valence band is half filled
c) Copper conducts because it has a gap smaller than 2 eV
d) Metals conduct because no empty states lie above $E_f$

### Answer

b

### Explanation

Session 13, Slide 6: Cu (like Na and Al) has only one $s$ electron per atom, so its valence band is half filled, with empty states just above the Fermi energy.

- a) Mg has $3s^2$: its 3s band is full, and it conducts because that band overlaps the empty 3p band (case A2), not because it is half filled.
- c) A gap below 2 eV defines a semiconductor (Slide 8); a conductor has no gap between its filled and empty states.
- d) Inverted: a metal conducts precisely because empty states lie just above $E_f$ (Slides 6-7).

### Source

Session 13, Slides 6-8.

## Q33.8 Small field and metallic conduction

- id: B33-Q8
- concept_id: u6-conductor-band-structure
- format: complete-sentence
- asks: cause

A small electric field makes the electrons of a metal move because these electrons:

a) Find empty states just above the filled ones
b) First jump a gap narrower than 2 eV
c) Are freed from covalent bonds that break easily
d) Lie in a band that is completely filled

### Answer

a

### Explanation

Session 13, Slides 6-7: a material conducts when its electrons can find empty states just above the filled ones, so a small excitation promotes an electron to an empty state just above $E_f$.

- b) A gap to jump is the semiconductor mechanism (Slide 8); a metal has no gap between filled and empty states.
- c) Breaking covalent bonds describes the excitation of an intrinsic semiconductor (Slide 28), not a metal.
- d) In a completely filled band with no overlap there are no empty states nearby, so the field could not move the electrons.

### Source

Session 13, Slides 6-8 and 28.

## Q33.9 Ranking by conductivity

- id: B33-Q9
- concept_id: u6-conductivity-ranges
- format: ordering
- asks: comparison

Order the following materials from the lowest to the highest electrical conductivity at room temperature:

a) Silicon < polyethylene < copper
b) Polyethylene < copper < silicon
c) Copper < silicon < polyethylene
d) Polyethylene < silicon < copper

### Answer

d

### Explanation

Session 13, Slide 5: insulators (polyethylene) have $10^{-20}$ to $10^{-10}$ (Ω·m)⁻¹, semiconductors (Si) $10^{-6}$ to $10^{4}$ (Ω·m)⁻¹ and conductors (copper) about $10^{7}$ (Ω·m)⁻¹.

- a) The insulator and the semiconductor are swapped.
- b) The semiconductor and the conductor are swapped.
- c) Fully reversed order: this ranks the materials by resistivity, $\rho = 1/\sigma$.

### Source

Session 13, Slide 5.

## Q33.10 Metals, ceramics and polymers compared

- id: B33-Q10
- concept_id: u6-conductivity-ranges
- format: topic-true
- asks: cause
- origin: official-exam

Referring to the electrical conductivity of metals, typical ceramics and typical polymers, indicate which statement is TRUE:

a) Metals conduct poorly compared with ceramics because their valence electrons are tightly held in ionic bonds
b) Polymers are strong conductors because covalent chains share free electrons across overlapping bands
c) Metals have the highest conductivity due to free electrons, while ceramics and polymers act as insulators with wide band gaps
d) Ceramics conduct better than metals at room temperature because their ions hop easily between lattice sites

### Answer

c

### Explanation

Session 13, Slides 5-8 and 10 (MATERIALS_FINALEXAM_2012_ORD.pdf, Q6): metals have half-filled or overlapping bands with free delocalised electrons ($\sigma \sim 10^{7}$ (Ω·m)⁻¹), whereas typical ceramics and polymers bind their valence electrons in ionic or covalent bonds, leaving a wide band gap ($E_g > 2$ eV) and very low conductivity ($10^{-20}$ to $10^{-10}$ (Ω·m)⁻¹).

- a) Inverts the bonding and conductivity of metals and ceramics: metals have metallic bonds with free electron clouds, not tightly bound ionic electrons.
- b) Confuses insulating polymers (tight covalent bonds, large gap) with metals; only specially manufactured conductive polymers conduct (Slide 20).
- d) Ionic conduction in advanced ceramics requires high temperatures to mobilise ions through vacancies (Slide 22); at room temperature typical ceramics remain insulators.

### Source

MATERIALS_FINALEXAM_2012_ORD.pdf, p. 3 (Question 6); Session 13, Slides 5-8, 10 and 22.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
