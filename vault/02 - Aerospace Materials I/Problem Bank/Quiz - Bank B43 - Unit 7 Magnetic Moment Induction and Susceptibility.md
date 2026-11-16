---
materia: Aerospace Materials I
tema: "Unit 7: origin of magnetism, field, induction, magnetization, permeability and susceptibility"
bank_id: B43
title: "Magnetic moment, induction, permeability and susceptibility"
category: mt2_test_block
unit: 7
concepts:
  - u7-atomic-magnetic-moment
  - u7-induction-field-magnetization
  - u7-permeability-susceptibility
difficulty: 1
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 15, Slides 3-5."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-7
---

# Bank B43 — Magnetic moment, induction, permeability and susceptibility

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 15, Slides 3-5.

## Q43.1 Origin of the atomic magnetic moment

- id: B43-Q1
- concept_id: u7-atomic-magnetic-moment
- format: complete-sentence
- asks: definition

The net magnetic moment of an isolated atom comes from:

a) the orbital motion of its electrons only
b) the orbital and spin moments of its electrons
c) the spin moments of its electrons only
d) the static electric charge of its nucleus

### Answer

b

### Explanation

Session 15, Slide 3: each electron has an orbital magnetic moment, $m_l\mu_B$, from its motion around the nucleus, and a spin magnetic moment, $\pm\mu_B$; the moment of the atom is the sum of both contributions over all its electrons.

- a) Leaves out the spin moment, which the slide lists as the second contribution of every electron (and the main one in ferromagnets, Slide 9).
- c) Leaves out the orbital moment; spin dominates in ferromagnets, but the moment of the atom is the sum of both terms.
- d) Magnetism comes from moving charges (Slide 3); a static charge produces an electric field, not a magnetic moment.

### Source

Session 15, Slide 3.

## Q43.2 Moment of a cobalt atom in Bohr magnetons

- id: B43-Q2
- concept_id: u7-atomic-magnetic-moment
- format: numeric
- asks: calculation
- calc: 3*9.27e-24

The table of Session 15 gives a moment of 3 Bohr magnetons for an isolated Co atom. Determine this moment in SI units, with $\mu_B = 9.27\times10^{-24}$ A·m²:

a) $9.27\times10^{-24}$ A·m²
b) $1.39\times10^{-23}$ A·m²
c) $2.78\times10^{-23}$ A·m²
d) $6.49\times10^{-23}$ A·m²

### Answer

c

### Explanation

The moment of the atom is the number of Bohr magnetons times $\mu_B$ (Slide 3): $3 \times 9.27\times10^{-24} = 2.78\times10^{-23}$ A·m².

- a) This is a single Bohr magneton, as if only one unpaired electron counted.
- b) Each unpaired spin is taken as $\mu_B/2$, confusing the spin quantum number $\pm 1/2$ with the spin moment $\pm\mu_B$: $1.5\times9.27\times10^{-24} = 1.39\times10^{-23}$ A·m².
- d) All seven 3d electrons of Co are counted as $7\mu_B$; paired spins cancel, so only the three unpaired ones contribute.

### Source

Session 15, Slide 3 (value of $\mu_B$ and table of the 3d elements).

## Q43.3 Moments of the 3d transition elements

- id: B43-Q3
- concept_id: u7-atomic-magnetic-moment
- format: true-statement
- asks: comparison

Which one of the following statements is TRUE about the atomic moments tabulated for the 3d elements?

a) A Cu atom has no net moment, since its 3d shell has no unpaired spins
b) An Fe atom has a larger moment than a Mn atom
c) The atomic moment grows steadily with atomic number from Sc to Cu
d) An atom with a null net moment behaves as a magnetic dipole

### Answer

a

### Explanation

The table of Slide 3 counts the unpaired spins of the 3d shell: Cu has a full 3d shell and a moment of 0 $\mu_B$.

- b) Inverted comparison: Mn has 5 $\mu_B$ and Fe 4 $\mu_B$ in the table; a higher atomic number does not mean a larger moment.
- c) The moments rise from Sc (1) to Cr and Mn (5) and then fall to Cu (0), because the spins begin to pair once the 3d shell is half full.
- d) The slide states the opposite condition: an atom behaves as a magnetic dipole only if its net moment is not null.

### Source

Session 15, Slide 3.

## Q43.4 Magnetization from B and H

- id: B43-Q4
- concept_id: u7-induction-field-magnetization
- format: numeric
- asks: calculation
- calc: 1.30/1.257e-6 - 2.0e5

A specimen in a field $H = 2.0\times10^5$ A/m has an induction $B = 1.30$ T. Determine its magnetization, with $\mu_0 = 1.257\times10^{-6}$ H/m:

a) $8.34\times10^{5}$ A/m
b) $1.03\times10^{6}$ A/m
c) $1.23\times10^{6}$ A/m
d) $1.01\times10^{7}$ A/m

### Answer

a

### Explanation

From $B = \mu_0 H + \mu_0 M$ (Slide 4), $M = B/\mu_0 - H = 1.30/1.257\times10^{-6} - 2.0\times10^5 = 1.034\times10^6 - 2.0\times10^5 = 8.34\times10^5$ A/m.

- b) $B/\mu_0 = 1.03\times10^6$ A/m: the applied field $H$ is not subtracted, as if all of $B$ came from the material.
- c) $B/\mu_0 + H = 1.23\times10^6$ A/m: sign error, $H$ added instead of subtracted.
- d) $\mu_0$ taken as $1.257\times10^{-7}$ H/m (exponent slip): $1.30/1.257\times10^{-7} - 2.0\times10^5 = 1.01\times10^7$ A/m.

### Source

Session 15, Slide 4.

## Q43.5 Definition of the magnetization

- id: B43-Q5
- concept_id: u7-induction-field-magnetization
- format: complete-sentence
- asks: definition

The magnetization M of a material is:

a) the magnetic moment carried by each atom
b) the flux density measured inside the material
c) the field strength produced by the external coil
d) the magnetic moment per unit volume

### Answer

d

### Explanation

Slide 4 defines the magnetization $M$ as the magnetic moment per unit volume, in A/m.

- a) The moment per atom is given in Bohr magnetons (Slides 3 and 9); the magnetization refers to a volume of material, not to one atom.
- b) The flux density inside the material is the induction $B$, which includes the term $\mu_0 H$ as well as $\mu_0 M$.
- c) The field produced by the coil is the field strength $H$; $M$ is the response of the material to it.

### Source

Session 15, Slide 4.

## Q43.6 Units of B and H

- id: B43-Q6
- concept_id: u7-induction-field-magnetization
- format: identify
- asks: definition

Which pair gives the SI units of the magnetic induction B and of the field strength H, in that order?

a) A/m and T
b) H/m and A/m
c) T and A/m
d) T and H/m

### Answer

c

### Explanation

Slide 4: $B$ is measured in Wb/m², that is tesla, and $H$ in A/m.

- a) The two units are swapped: A/m belongs to $H$ (and to $M$), and the tesla to $B$.
- b) H/m is the unit of the permeability $\mu$, not of the induction.
- d) H/m is again the unit of the permeability; the field strength $H$ is in A/m.

### Source

Session 15, Slide 4.

## Q43.7 Induction inside a magnetized material

- id: B43-Q7
- concept_id: u7-induction-field-magnetization
- format: true-statement
- asks: effect

Which one of the following statements is TRUE about the induction B inside a material placed in a field H?

a) It equals $\mu_0 H$ only when the material is ferromagnetic
b) It exceeds $\mu_0 H$ when the magnetization M is positive
c) It does not depend on the applied field H
d) It is lower than $\mu_0 H$ in paramagnetic materials

### Answer

b

### Explanation

$B = \mu_0 H + \mu_0 M$ (Slide 4): the material adds $\mu_0 M$ to the vacuum value $\mu_0 H$, so a positive $M$ gives $B > \mu_0 H$.

- a) $B = \mu_0 H$ is the vacuum line; a ferromagnet lies far above it, with $B \cong \mu_0 M$ (Slide 5).
- c) $B$ contains the term $\mu_0 H$, and $M$ itself grows with $H$ ($M = \chi_m H$), so $B$ depends on $H$.
- d) Paramagnetic and diamagnetic swapped: $B_{para} > B_0$, and only the diamagnetic materials, with $M < 0$, give $B < \mu_0 H$ (Slides 6 and 8).

### Source

Session 15, Slides 4-5.

## Q43.8 Permeability of a core and induction

- id: B43-Q8
- concept_id: u7-permeability-susceptibility
- format: cause-effect
- asks: effect

With an increase in the relative permeability of a coil core, at the same field H, the induction B:

a) increases, because $B = \mu_r\mu_0 H$
b) decreases, because the core opposes the field
c) does not change, because B depends only on H
d) increases, because $\mu_0$ grows with the core

### Answer

a

### Explanation

Slide 4: $B = \mu H$ with $\mu = \mu_r\mu_0$, so at constant $H$ the induction grows in proportion to $\mu_r$.

- b) Inverted trend: a core that opposes the field is diamagnetic, with $\mu_r < 1$; a larger $\mu_r$ strengthens the induction.
- c) Ignores the material: $B = \mu_0 H$ holds only in vacuum, and a core changes $B$ through $\mu_r$.
- d) Right trend, wrong cause: $\mu_0$ is the constant permeability of vacuum, $1.257\times10^{-6}$ H/m; only $\mu_r$ depends on the material.

### Source

Session 15, Slide 4.

## Q43.9 Relative permeability and susceptibility

- id: B43-Q9
- concept_id: u7-permeability-susceptibility
- format: complete-sentence
- asks: definition

The relative permeability $\mu_r$ and the magnetic susceptibility $\chi_m$ of a material are related by:

a) $\mu_r = \chi_m - 1$
b) $\mu_r = \mu_0\chi_m$
c) $\chi_m = 1/\mu_r$
d) $\mu_r = 1 + \chi_m$

### Answer

d

### Explanation

With $M = \chi_m H$ in $B = \mu_0 H + \mu_0 M$ (Slide 4), $B = \mu_0(1 + \chi_m)H$; comparing with $B = \mu_r\mu_0 H$ gives $\mu_r = 1 + \chi_m$.

- a) Sign error in the rearrangement: it is $\chi_m = \mu_r - 1$, not $\mu_r = \chi_m - 1$.
- b) Confuses the relative permeability with the absolute one, $\mu = \mu_r\mu_0$; $\mu_r$ and $\chi_m$ are both dimensionless.
- c) An inverse relation would give a positive $\chi_m$ for every positive $\mu_r$, so no diamagnet ($\mu_r$ just below 1 and $\chi_m < 0$, Slide 6) could exist.

### Source

Session 15, Slide 4.

## Q43.10 Relative permeability just below one

- id: B43-Q10
- concept_id: u7-permeability-susceptibility
- format: complete-sentence
- asks: classification

A material whose relative permeability is slightly below 1:

a) has a positive susceptibility and strengthens the field
b) has a positive susceptibility and weakens the field
c) has a negative susceptibility and weakens the field
d) has a negative susceptibility and strengthens the field

### Answer

c

### Explanation

$\mu_r < 1$ gives $\chi_m = \mu_r - 1 < 0$: the material is diamagnetic, its magnetization opposes $H$ and $B < B_0$ (Slide 6).

- a) Describes $\mu_r$ slightly above 1, a paramagnetic material ($\chi_m > 0$, $B > B_0$, Slide 8).
- b) Wrong sign of $\chi_m$: with $\mu_r < 1$ the susceptibility cannot be positive.
- d) Right sign of $\chi_m$ but wrong effect: a negative $M$ subtracts $\mu_0|M|$ from $\mu_0 H$, so the field inside is weakened.

### Source

Session 15, Slides 4-6.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
