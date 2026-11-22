---
materia: Aerospace Materials I
tema: "Unit 8: stoichiometry from unit cell ion sharing, unit cell reading and crystallographic plane-pair identification"
bank_id: B66
title: "Crystal structure identification and stoichiometry"
category: mt3_test_block
unit: 8
concepts:
  - u8-unit-cell-ion-sharing
  - u8-nacl-cell-diagram
  - u8-cscl-cell-diagram
  - u8-zns-cell-diagram
  - u8-fluorite-cell-diagram
  - u8-perovskite-cell-diagram
  - u8-planes-perovskite-id
  - u8-planes-rocksalt-id
  - u8-stoichiometry-from-occupancy
difficulty: 2
origen: "Practice items written for the bank in the style of Part I of Assessment Test III. Content and figures from Session 16 Slides 7-12 and Problems T8_CeramicMaterials.pdf Problems 3 and 5."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-8
---

# Bank B66 — Crystal structure identification and stoichiometry

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test III (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 16, Slides 7-12 and Problems T8, Problems 3 and 5.

## Q66.1 Ion sharing fractions in a cubic unit cell

- id: B66-Q1
- concept_id: u8-unit-cell-ion-sharing
- format: false-statement
- asks: classification

Which one of the following statements about counting ions shared across cubic unit cells is FALSE:

a) An ion located at a cube corner is shared by eight unit cells and contributes $1/8$ to each cell
b) An ion located at an edge midpoint is shared by two unit cells and contributes $1/2$ to each cell
c) An ion located at a face centre is shared by two unit cells and contributes $1/2$ to each cell
d) An ion located in a tetrahedral site or at the body centre lies wholly inside one cell and contributes $1$

### Answer

b

### Explanation

Session 16, Slides 7-12 and Topic 2 (Unit 2 cell counting): an edge of a cube is shared by **four** adjacent unit cells, so each edge-midpoint ion contributes $1/4$ per cell (giving $12\times\frac{1}{4} = 3$ edge ions per cell, plus $1$ body centre $= 4$ octahedral sites in FCC). Statement b) is false.

- a) True: eight cubes meet at every corner vertex, so each corner contributes $1/8$.
- c) True: two cubes meet across each face, so each face-centre ion contributes $1/2$.
- d) True: interior sites (body centre and octant tetrahedral sites) are unshared and contribute $1$.

### Source

Session 16, Slides 7-12; Problems T8_CeramicMaterials.pdf, Problems 3-5.

## Q66.2 Reading ion counts and interstitials in rock salt

- id: B66-Q2
- concept_id: u8-nacl-cell-diagram
- format: diagram-reading
- asks: figure-reading

From the ion positions in the unit cell shown below ($\text{Cl}^-$ green, $\text{Na}^+$ purple), determine how many ions of each species belong to one unit cell and which interstitial sites the $\text{Na}^+$ ions occupy:

![[attachments/T8/s16-nacl-structure.png]]

a) $1\ \text{Na}^+$ and $1\ \text{Cl}^-$ per cell; cubic sites
b) $4\ \text{Na}^+$ and $4\ \text{Cl}^-$ per cell; half of the tetrahedral sites
c) $4\ \text{Na}^+$ and $8\ \text{Cl}^-$ per cell; all of the tetrahedral sites
d) $4\ \text{Na}^+$ and $4\ \text{Cl}^-$ per cell; all of the octahedral sites

### Answer

d

### Explanation

Session 16, Slide 8: $\text{Cl}^-$ anions sit at the $8$ corners and $6$ face centres ($8\times\frac{1}{8} + 6\times\frac{1}{2} = 4$), while $\text{Na}^+$ cations occupy all $12$ edge midpoints and the body centre ($12\times\frac{1}{4} + 1 = 4$), which are all the octahedral interstitial sites of the FCC lattice.

- a) Confuses the $4$-formula-unit FCC cell with the $1$-formula-unit simple-cubic $\text{CsCl}$ cell.
- b) Misidentifies the edge-centre and body-centre octahedral sites as tetrahedral sites (which sit inside octants, as in $\text{ZnS}$).
- c) Assigns an $8:4$ count ($AX_2$ fluorite) instead of the equal $4:4$ occupancy visible in the cell.

### Source

Session 16, Slide 8.

## Q66.3 Reading ion counts and coordination in CsCl

- id: B66-Q3
- concept_id: u8-cscl-cell-diagram
- format: diagram-reading
- asks: figure-reading

Based on the ion positions shown in the unit cell below, what are the net numbers of $\text{Cl}^-$ and $\text{Cs}^+$ ions belonging to one unit cell and the coordination index of $\text{Cs}^+$?

![[attachments/T8/s16-cscl-unit-cell.png]]

a) $1\ \text{Cl}^-$, $1\ \text{Cs}^+$, and $\text{C.I.} = 8$
b) $2\ \text{Cl}^-$, $1\ \text{Cs}^+$, and $\text{C.I.} = 8$
c) $1\ \text{Cl}^-$, $1\ \text{Cs}^+$, and $\text{C.I.} = 6$
d) $8\ \text{Cl}^-$, $1\ \text{Cs}^+$, and $\text{C.I.} = 12$

### Answer

a

### Explanation

Session 16, Slide 7: $\text{Cl}^-$ ions occupy the $8$ cube corners, contributing $8\times\frac{1}{8} = 1\ \text{Cl}^-$ per cell, and the single interior $\text{Cs}^+$ ion contributes $1\ \text{Cs}^+$ per cell; the central $\text{Cs}^+$ touches all $8$ corner $\text{Cl}^-$ ions, so $\text{C.I.} = 8$.

- b) Miscounts the $8$ shared corner anions as $2$ ions instead of $8\times\frac{1}{8} = 1$.
- c) Assigns the octahedral coordination index ($\text{C.I.} = 6$) instead of cubic $8$-fold coordination.
- d) Counts every corner ion as $1$ whole ion rather than $1/8$ and uses the FCC metallic coordination ($12$).

### Source

Session 16, Slide 7.

## Q66.4 Reading interstitial fraction and formula units in zinc blende

- id: B66-Q4
- concept_id: u8-zns-cell-diagram
- format: diagram-reading
- asks: figure-reading

In the unit cell shown below, $\text{S}^{2-}$ ions occupy the FCC lattice points while $\text{Zn}^{2+}$ ions sit inside alternating sub-cubes. Which interstitial fraction and formula-unit count per cell does this arrangement give?

![[attachments/T8/s16-zincblende-structure.png]]

a) All octahedral sites filled; $4\ \text{ZnS}$ formula units per cell
b) All tetrahedral sites filled; $8\ \text{ZnS}$ formula units per cell
c) Half of the tetrahedral sites filled; $4\ \text{ZnS}$ formula units per cell
d) One-quarter of the octahedral sites filled; $1\ \text{ZnS}$ formula unit per cell

### Answer

c

### Explanation

Session 16, Slide 9: an FCC cell contains $8$ tetrahedral octants; $\text{Zn}^{2+}$ ions occupy $4$ of those $8$ tetrahedral sites ($1/2$ occupied), pairing with $8\times\frac{1}{8} + 6\times\frac{1}{2} = 4\ \text{S}^{2-}$ anions to yield $4\ \text{ZnS}$ formula units per unit cell.

- a) Confuses the alternating interior tetrahedral sites with the edge-and-body octahedral sites of rock salt.
- b) Counts all $8$ octants as occupied, which would give $8\ \text{Zn}^{2+}$ and $4\ \text{S}^{2-}$ ($\text{Zn}_2\text{S}$).
- d) Confuses the $1/4$ octahedral occupancy of perovskite ($ABO_3$) with the $1/2$ tetrahedral occupancy of zinc blende.

### Source

Session 16, Slide 9.

## Q66.5 Reading ion counts and coordination in fluorite

- id: B66-Q5
- concept_id: u8-fluorite-cell-diagram
- format: diagram-reading
- asks: figure-reading

Inspect the unit cell below, where $\text{Ca}^{2+}$ occupies the corners and face centres and $\text{F}^-$ occupies all eight interior octants. Which ion counts per cell and coordination indices match this geometry?

![[attachments/T8/s16-fluorite-structure.png]]

a) $4\ \text{Ca}^{2+}$ and $4\ \text{F}^-$; $\text{C.I.}(\text{Ca}^{2+}) = 6$, $\text{C.I.}(\text{F}^-) = 6$
b) $4\ \text{Ca}^{2+}$ and $8\ \text{F}^-$; $\text{C.I.}(\text{Ca}^{2+}) = 8$, $\text{C.I.}(\text{F}^-) = 4$
c) $8\ \text{Ca}^{2+}$ and $4\ \text{F}^-$; $\text{C.I.}(\text{Ca}^{2+}) = 4$, $\text{C.I.}(\text{F}^-) = 8$
d) $4\ \text{Ca}^{2+}$ and $8\ \text{F}^-$; $\text{C.I.}(\text{Ca}^{2+}) = 4$, $\text{C.I.}(\text{F}^-) = 8$

### Answer

b

### Explanation

Session 16, Slide 10: $\text{Ca}^{2+}$ on FCC corners and faces contributes $8\times\frac{1}{8} + 6\times\frac{1}{2} = 4$ cations, and $8$ wholly interior $\text{F}^-$ ions contribute $8$ anions ($4\ \text{CaF}_2$ units). Each $\text{Ca}^{2+}$ is surrounded by $8\ \text{F}^-$ anions ($\text{C.I.} = 8$), and each $\text{F}^-$ inside its octant tetrahedron has $4\ \text{Ca}^{2+}$ neighbours ($\text{C.I.} = 4$).

- a) Miscounts $8$ interior $\text{F}^-$ ions as $4$ and assigns rock-salt octahedral coordination.
- c) Reverses the ion counts to $8$ cations and $4$ anions (the anti-fluorite stoichiometry).
- d) Keeps the right cell counts ($4$ and $8$) but swaps the coordination indices of $\text{Ca}^{2+}$ and $\text{F}^-$.

### Source

Session 16, Slide 10.

## Q66.6 Reading ion counts and coordination in perovskite

- id: B66-Q6
- concept_id: u8-perovskite-cell-diagram
- format: diagram-reading
- asks: figure-reading

From the unit cell shown below ($\text{Ca}^{2+}$ at corners, $\text{O}^{2-}$ at face centres, $\text{Ti}^{4+}$ at body centre), how many ions of each kind belong to one cell and what is the coordination index of $\text{Ca}^{2+}$?

![[attachments/T8/s16-perovskite-cell.png]]

a) $1\ \text{Ca}^{2+}$, $1\ \text{Ti}^{4+}$, $6\ \text{O}^{2-}$; $\text{C.I.}(\text{Ca}^{2+}) = 8$
b) $4\ \text{Ca}^{2+}$, $1\ \text{Ti}^{4+}$, $3\ \text{O}^{2-}$; $\text{C.I.}(\text{Ca}^{2+}) = 6$
c) $1\ \text{Ca}^{2+}$, $4\ \text{Ti}^{4+}$, $3\ \text{O}^{2-}$; $\text{C.I.}(\text{Ca}^{2+}) = 12$
d) $1\ \text{Ca}^{2+}$, $1\ \text{Ti}^{4+}$, $3\ \text{O}^{2-}$; $\text{C.I.}(\text{Ca}^{2+}) = 12$

### Answer

d

### Explanation

Session 16, Slide 12: corners give $8\times\frac{1}{8} = 1\ \text{Ca}^{2+}$, face centres give $6\times\frac{1}{2} = 3\ \text{O}^{2-}$, and the body centre gives $1\ \text{Ti}^{4+}$, forming $\text{CaTiO}_3$. Since $\text{Ca}^{2+}$ and $\text{O}^{2-}$ together form an FCC packing, each corner $\text{Ca}^{2+}$ has $12$ nearest face-centre $\text{O}^{2-}$ neighbours ($\text{C.I.} = 12$), while $\text{Ti}^{4+}$ has $\text{C.I.} = 6$.

- a) Forgets the $1/2$ sharing factor on the $6$ face-centre $\text{O}^{2-}$ ions and gives $\text{Ca}^{2+}$ a $\text{CsCl}$-like $\text{C.I.} = 8$.
- b) Miscounts corner $\text{Ca}^{2+}$ as $4$ instead of $8\times\frac{1}{8} = 1$ and attributes $\text{Ti}^{4+}$'s $\text{C.I.} = 6$ to $\text{Ca}^{2+}$.
- c) Counts the four possible octahedral sites of FCC instead of the $1$ occupied body-centre $\text{Ti}^{4+}$.

### Source

Session 16, Slide 12.

## Q66.7 Identifying perovskite from (110) and (100) planes

- id: B66-Q7
- concept_id: u8-planes-perovskite-id
- format: diagram-reading
- asks: classification

The figure shows the $(110)$ and $(100)$ crystallographic planes of an $A_x B_y C_z$ unit cell with orthogonal axes. Identify its crystal system, stoichiometry, and structure type:

![[attachments/T8/t8-p1-planes-110-100.png]]

a) Cubic system, $A_2BC_3$, fluorite-type
b) Tetragonal system, $ABC_2$, rock-salt-type
c) Orthorhombic system, $ABC_3$, perovskite-type
d) Orthorhombic system, $AB_2C_3$, corundum-type

### Answer

c

### Explanation

Problems T8_CeramicMaterials.pdf, Problem 3 and Session 16, Slide 12: from $(100)$, $b = 0.387\text{ nm}$ and $c = 0.383\text{ nm}$; from $(110)$, $a = \sqrt{0.546^2 - 0.387^2} = 0.385\text{ nm} \neq b \neq c$, so the orthogonal cell is **orthorhombic**. $A$ sits at all $8$ corners ($1$), $C$ at the $(100)$ face centre and top/bottom face centres in $(110)$ ($6\times\frac{1}{2} = 3$), and $B$ at the body centre ($1$), giving $ABC_3$ perovskite.

- a) Overlooks that $a = 0.385$, $b = 0.387$, and $c = 0.383\text{ nm}$ are three unequal edges (not cubic) and miscounts the $A$ corners.
- b) Assumes $a = b$ (tetragonal) without solving the base diagonal and miscounts the $C$ face-centre anions.
- d) Correctly reads the orthorhombic distortion but miscounts $B$ at the body centre ($1$, not $2$) and misidentifies the cubic-derived perovskite as HCP corundum.

### Source

Problems T8_CeramicMaterials.pdf, Problem 3; Session 16, Slide 12.

## Q66.8 Lattice parameter a from orthogonal (110) and (100) planes

- id: B66-Q8
- concept_id: u8-planes-perovskite-id
- format: numeric
- asks: calculation
- calc: sqrt(0.546**2 - 0.387**2)

From the $(110)$ and $(100)$ planes of the orthogonal unit cell shown below ($b = 0.387\text{ nm}$, $c = 0.383\text{ nm}$, base face diagonal $= 0.546\text{ nm}$), calculate the lattice parameter $a$:

![[attachments/T8/t8-p1-planes-110-100.png]]

a) $0.385\text{ nm}$
b) $0.546\text{ nm}$
c) $0.772\text{ nm}$
d) $0.159\text{ nm}$

### Answer

a

### Explanation

Problems T8_CeramicMaterials.pdf, Problem 3: the $(110)$ plane is a vertical diagonal rectangle of height $c = 0.383\text{ nm}$ and base equal to the face diagonal $\sqrt{a^2 + b^2} = 0.546\text{ nm}$. By Pythagoras, $a = \sqrt{0.546^2 - 0.387^2} = \sqrt{0.29812 - 0.14977} = \sqrt{0.14835} = 0.385\text{ nm}$.

- b) Reads the horizontal edge of the diagonal $(110)$ plane ($0.546\text{ nm}$) directly as $a$.
- c) Multiplies $0.546$ by $\sqrt{2}$ ($0.772\text{ nm}$) instead of solving $a^2 + b^2 = 0.546^2$.
- d) Subtracts linearly ($0.546 - 0.387 = 0.159\text{ nm}$) instead of subtracting squares under the square root.

### Source

Problems T8_CeramicMaterials.pdf, Problem 3.

## Q66.9 Identifying rock salt from (020) and (100) planes

- id: B66-Q9
- concept_id: u8-planes-rocksalt-id
- format: diagram-reading
- asks: classification

The figure shows the $(020)$ mid-plane (at $y = a/2$) and $(100)$ face of a cubic unit cell with ions $A$ (small black) and $B$ (large open). Which stoichiometry and structure type do these planes represent?

![[attachments/T8/t8-p2-planes-020-100.png]]

a) $AB_2$, fluorite structure
b) $AB$, rock salt ($\text{NaCl}$) structure
c) $AB$, cesium chloride ($\text{CsCl}$) structure
d) $AB$, zinc blende ($\text{ZnS}$) structure

### Answer

b

### Explanation

Problems T8_CeramicMaterials.pdf, Problem 5 and Session 16, Slide 8: in $(100)$, $B$ occupies corners and the face centre (FCC lattice, $4$ ions), while $A$ occupies edge midpoints; in $(020)$, $A$ also sits at the centre $(\frac{1}{2},\frac{1}{2},\frac{1}{2})$, showing that $A$ fills all octahedral sites ($12\times\frac{1}{4} + 1 = 4$ ions). Thus the formula is $AB$ with the rock salt ($\text{NaCl}$) structure.

- a) Fluorite ($AB_2$) places anions inside the octant tetrahedral sites visible on $(110)$, not at edge midpoints and body centre.
- c) $\text{CsCl}$ places only $B$ at corners and $A$ at the body centre, with empty face centres and empty edge midpoints.
- d) Zinc blende places $A$ ions inside four of the eight octants, leaving edge midpoints and the body centre empty.

### Source

Problems T8_CeramicMaterials.pdf, Problem 5; Session 16, Slide 8.

## Q66.10 Stoichiometry and valence from octahedral occupancy

- id: B66-Q10
- concept_id: u8-stoichiometry-from-occupancy
- format: topic-true
- asks: application

In a cubic oxide whose $\text{O}^{2-}$ anions occupy the FCC lattice sites, cations $M^{z+}$ fill all octahedral interstitial sites and leave all tetrahedral sites empty. Referring to the unit-cell stoichiometry and cation valence $z$, indicate which statement is TRUE:

a) The unit cell contains $4\ M$ and $8\ \text{O}$, giving formula $MO_2$ and $z = +4$
b) The unit cell contains $8\ M$ and $4\ \text{O}$, giving formula $M_2O$ and $z = +1$
c) The unit cell contains $4\ M$ and $4\ \text{O}$, giving formula $MO$ and $z = +2$
d) The unit cell contains $2\ M$ and $4\ \text{O}$, giving formula $MO_2$ and $z = +4$

### Answer

c

### Explanation

Session 16, Slides 6 and 8: an FCC cell contains $4$ lattice $\text{O}^{2-}$ anions ($8\times\frac{1}{8} + 6\times\frac{1}{2} = 4$) and $4$ octahedral sites ($12\times\frac{1}{4} + 1 = 4$). Filling all octahedral sites gives $4\ M$ and $4\ \text{O}$, so the formula is $MO$ and electroneutrality with $\text{O}^{2-}$ fixes $z = +2$.

- a) Doubles the anion count ($8\ \text{O}$) instead of counting $4$ FCC lattice anions.
- b) Uses $8$ (the number of tetrahedral sites in FCC) instead of $4$ (the number of octahedral sites).
- d) Assumes only half of the octahedral sites are filled ($2\ M$), leaving a net negative deficiency if all sites are filled.

### Source

Session 16, Slides 6 and 8.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
