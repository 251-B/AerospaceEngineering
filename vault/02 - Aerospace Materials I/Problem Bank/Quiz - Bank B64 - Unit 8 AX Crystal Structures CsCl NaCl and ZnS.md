---
materia: Aerospace Materials I
tema: "Unit 8: AX ceramic crystal structures (CsCl, rock salt NaCl/MgO/CaO, zinc blende ZnS), coordination indices, lattice occupancy and linear/planar intuition"
bank_id: B64
title: "AX crystal structures CsCl NaCl and ZnS"
category: mt3_test_block
unit: 8
concepts:
  - u8-zincblende-structure
  - u8-cscl-not-bcc
  - u8-rocksalt-occupancy
  - u8-rocksalt-cao-ci
  - u8-ax-contact-directions
  - u8-ax-examples-bonding
  - u8-ax-linear-planar-intuition
difficulty: 2
origen: "Includes Question 1 of MATERIALS_THIRDPARTIAL_2020.pdf (p. 1) and Questions 5 and 6 of MATERIALS_THIRDPARTIAL_2020_V2.pdf (pp. 4-5), alongside practice items. Content from Session 16 Slides 7-9 and 14, and Problems T8_CeramicMaterials.pdf Problems 1, 5, and 7."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-8
---

# Bank B64 — AX crystal structures CsCl NaCl and ZnS

> [!info] Includes official exam questions
> Ten test questions in the style of Part I of Assessment Test III (four options, one right answer; +0.5 right, -0.15 wrong). Question 1 is Question 1 of `MATERIALS_THIRDPARTIAL_2020.pdf`, and Questions 4 and 5 are Questions 6 and 5 of `MATERIALS_THIRDPARTIAL_2020_V2.pdf` (Paper B); the remaining seven are practice items. Content: Session 16, Slides 7-9 and 14; Problems T8, Problems 1, 5, and 7.

## Q64.1 Identifying the zinc blende structure from packing

- id: B64-Q1
- concept_id: u8-zincblende-structure
- format: identify
- asks: classification
- origin: official-exam

Which ionic structure has cubic packing of the negative ions with positive ions filling half of the tetrahedral interstitial sites?

a) Zn-blende structure
b) Fluorite structure
c) NaCl structure
d) CsCl structure

### Answer

a

### Explanation

MATERIALS_THIRDPARTIAL_2020.pdf, p. 1 (Part I, Q1) and Session 16, Slides 9 and 14: in the zinc blende ($\text{ZnS}$) structure, the $\text{S}^{2-}$ anions occupy the FCC lattice sites (cubic close packing) and the $\text{Zn}^{2+}$ cations occupy half ($4$ of $8$) of the tetrahedral interstitial sites, giving $4\ \text{Zn}^{2+}$ and $4\ \text{S}^{2-}$ per unit cell with $\text{C.I.} = 4$.

- b) Fluorite ($\text{CaF}_2$) places $\text{Ca}^{2+}$ cations on FCC sites and $\text{F}^-$ anions in *all* $8$ tetrahedral sites.
- c) Rock salt ($\text{NaCl}$) places anions on FCC sites with cations occupying *all* $4$ octahedral interstitial sites.
- d) Cesium chloride ($\text{CsCl}$) has a simple cubic anion array with the cation at the cube centre ($\text{C.I.} = 8$).

### Source

MATERIALS_THIRDPARTIAL_2020.pdf, p. 1 (Part I, Q1); Session 16, Slides 9 and 14.

## Q64.2 Bravais lattice and occupancy of CsCl

- id: B64-Q2
- concept_id: u8-cscl-not-bcc
- format: true-statement
- asks: classification

Which one of the following statements about the cesium chloride ($\text{CsCl}$) crystal structure is TRUE:

a) Its Bravais lattice is body-centered cubic (BCC) because $\text{Cs}^+$ sits at the cube centre
b) Its unit cell contains two $\text{Cs}^+$ ions and two $\text{Cl}^-$ ions, making four ions per cube
c) Its radius ratio $r_{\text{Cs}^+}/r_{\text{Cl}^-} = 0.94$ gives octahedral $\text{C.I.} = 6$ for both ions
d) Its Bravais lattice is simple cubic with a two-ion basis ($\text{Cl}^-$ corners, $\text{Cs}^+$ centre) and $\text{C.I.} = 8$

### Answer

d

### Explanation

Session 16, Slide 7: in $\text{CsCl}$, $\text{Cl}^-$ sits at the eight cube corners ($8\times\frac{1}{8} = 1$) and $\text{Cs}^+$ at the cube centre ($1$), giving $r_{\text{Cs}^+}/r_{\text{Cl}^-} = 0.94 > 0.732$ and $\text{C.I.} = 8$. Because the corner and centre ions are chemically different, the Bravais lattice is simple cubic with a two-ion basis, not BCC.

- a) Confuses visual appearance with lattice equivalence: in BCC, corner and centre sites must hold identical atoms, whereas $\text{CsCl}$ places $\text{Cl}^-$ and $\text{Cs}^+$ on those sites.
- b) Miscounts $8\times\frac{1}{8} + 1 = 2$ total ions (which is $1\ \text{Cs}^+ + 1\ \text{Cl}^-$) as two formula units.
- c) Uses the wrong radius-ratio interval: $0.94 > 0.732$ gives cubic coordination ($\text{C.I.} = 8$), not octahedral ($\text{C.I.} = 6$).

### Source

Session 16, Slide 7.

## Q64.3 Interstitial site occupancy in rock salt

- id: B64-Q3
- concept_id: u8-rocksalt-occupancy
- format: complete-sentence
- asks: definition

In the rock salt ($\text{NaCl}$) structure, the larger anions occupy the FCC lattice points while the cations fill:

a) half of the tetrahedral interstitial sites, giving 2 formula units per unit cell
b) all of the octahedral interstitial sites, giving 4 cations and 4 anions per unit cell
c) all of the tetrahedral interstitial sites, giving 8 cations and 4 anions per unit cell
d) the body-centre octahedral site alone, giving 1 cation and 4 anions per unit cell

### Answer

b

### Explanation

Session 16, Slide 8: in rock salt ($\text{NaCl}$), $\text{Cl}^-$ ions sit on the FCC corners and face centres ($8\times\frac{1}{8} + 6\times\frac{1}{2} = 4$), and $\text{Na}^+$ ions occupy all octahedral interstitial sites ($12$ edge centres $\times\frac{1}{4} + 1$ body centre $= 4$), yielding $\text{C.I.} = 6$.

- a) Confuses rock salt ($1:1$ octahedral occupancy) with zinc blende ($4$ cations in half of the $8$ tetrahedral sites).
- c) Describes the $8$-cation count of anti-fluorite ($\text{Li}_2\text{O}$), which violates the $1:1$ stoichiometry of $AX$ rock salt.
- d) Misses the $12$ edge-centre octahedral sites that carry $12\times\frac{1}{4} = 3$ more cations per FCC cell.

### Source

Session 16, Slide 8.

## Q64.4 Coordination index of oxygen in CaO

- id: B64-Q4
- concept_id: u8-rocksalt-cao-ci
- format: identify
- asks: classification
- origin: official-exam

$\text{CaO}$ presents a "rock salt" structure. Identify the coordination index for $\text{O}^{2-}$ ions:

a) 3
b) 4
c) 6
d) 8

### Answer

c

### Explanation

MATERIALS_THIRDPARTIAL_2020_V2.pdf, pp. 4-5 (Paper B, Q6) and Session 16, Slides 8 and 14: $\text{CaO}$ adopts the rock salt ($\text{NaCl}$) crystal structure, in which both the cation ($\text{Ca}^{2+}$) and the anion ($\text{O}^{2-}$) have octahedral coordination with $\text{C.I.} = 6$.

- a) Triangular coordination ($\text{C.I.} = 3$) belongs to $r_C/r_A$ in $0.155\text{–}0.225$, not rock salt.
- b) Tetrahedral coordination ($\text{C.I.} = 4$) corresponds to zinc blende or the anion in fluorite, not rock salt.
- d) Cubic coordination ($\text{C.I.} = 8$) corresponds to $\text{CsCl}$ or the cation in fluorite, not rock salt.

### Source

MATERIALS_THIRDPARTIAL_2020_V2.pdf, pp. 4-5 (Paper B, Q6); Session 16, Slides 8 and 14.

## Q64.5 Structural description of zinc blende

- id: B64-Q5
- concept_id: u8-zincblende-structure
- format: complete-sentence
- asks: definition
- origin: official-exam

A ceramic material with a zinc blende structure presents:

a) a coordination index of 6
b) cations occupying half of the tetrahedral interstitial sites of the FCC unit cell
c) anions located at the lattice sites of a hexagonal close-packed unit cell
d) cations occupying all the octahedral interstitial sites of the FCC unit cell

### Answer

b

### Explanation

MATERIALS_THIRDPARTIAL_2020_V2.pdf, p. 4 (Paper B, Q5) and Session 16, Slides 9 and 14: in zinc blende ($\text{ZnS}$), $\text{S}^{2-}$ anions sit on the FCC lattice points and $\text{Zn}^{2+}$ cations occupy half of the tetrahedral interstitial sites ($4$ of $8$), giving $4\ \text{Zn}^{2+}$ and $4\ \text{S}^{2-}$ per unit cell with $\text{C.I.} = 4$.

- a) $\text{C.I.} = 6$ belongs to octahedral coordination (rock salt or corundum), whereas zinc blende has $\text{C.I.} = 4$.
- c) HCP anion packing belongs to corundum ($\text{Al}_2\text{O}_3$), not to cubic zinc blende.
- d) Occupying all octahedral sites of an FCC lattice defines rock salt ($\text{NaCl}$), not zinc blende.

### Source

MATERIALS_THIRDPARTIAL_2020_V2.pdf, p. 4 (Paper B, Q5); Session 16, Slides 9 and 14.

## Q64.6 Hard-sphere contact directions in AX cells

- id: B64-Q6
- concept_id: u8-ax-contact-directions
- format: topic-false
- asks: comparison

With respect to hard-sphere cation–anion contact and lattice parameter $a$ in cubic $AX$ structures, indicate which statement is FALSE:

a) In rock salt ($\text{NaCl}$), cations and anions touch along the face diagonal so that $a\sqrt{2} = 2(r_C + r_A)$
b) In $\text{CsCl}$, the central cation touches the corner anions along the body diagonal so that $a\sqrt{3} = 2(r_C + r_A)$
c) In zinc blende ($\text{ZnS}$), the tetrahedral cation touches the corner anion along the body diagonal so that $a\sqrt{3}/4 = r_C + r_A$
d) In $\text{MgO}$ (rock salt), $\text{Mg}^{2+}$ and $\text{O}^{2-}$ touch along the cube edge so that $a = 2(r_C + r_A)$

### Answer

a

### Explanation

Session 16, Slides 7-9 and Problems T8, Problems 1, 5, and 7: in the rock salt ($\text{NaCl}$) structure, cations sit at edge midpoints and anions at corners, so cation–anion contact occurs along the **cube edge** ($a = 2(r_C + r_A)$), whereas the face diagonal connects like ions ($a\sqrt{2}/2 \ge 2r_A$). Statement a) is false.

- b) True (Session 16, Slide 7 geometry): corner-to-centre contact in $\text{CsCl}$ runs half the body diagonal, $a\sqrt{3}/2 = r_C + r_A$.
- c) True (Problems T8, Problem 1): a tetrahedral site lies at $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$, a quarter of the body diagonal from the corner.
- d) True (Problems T8, Problem 7): $\text{MgO}$ has the rock salt structure with edge contact $a = 2(r_{\text{Mg}^{2+}} + r_{\text{O}^{2-}})$.

### Source

Session 16, Slides 7-9; Problems T8_CeramicMaterials.pdf, Problems 1, 5, and 7.

## Q64.7 Ceramic examples adopting rock salt

- id: B64-Q7
- concept_id: u8-ax-examples-bonding
- format: identify
- asks: application

Which list contains three ceramic compounds that all adopt the rock salt ($\text{NaCl}$) crystal structure?

a) $\text{CsCl}$, $\text{CsBr}$, $\text{TlCl}$
b) $\text{ZnS}$, $\text{CdS}$, $\text{GaAs}$
c) $\text{UO}_2$, $\text{ThO}_2$, $\text{CeO}_2$
d) $\text{MgO}$, $\text{CaO}$, $\text{FeO}$

### Answer

d

### Explanation

Session 16, Slides 8 and 14: oxides such as $\text{MgO}$, $\text{CaO}$, $\text{FeO}$, and $\text{NiO}$ adopt the rock salt ($\text{NaCl}$) crystal structure with $\text{C.I.} = 6$ for both ions.

- a) $\text{CsCl}$, $\text{CsBr}$, and $\text{TlCl}$ are halides with the simple-cubic $\text{CsCl}$ structure ($\text{C.I.} = 8$, Slide 7).
- b) $\text{ZnS}$, $\text{CdS}$, and $\text{GaAs}$ are semiconducting compounds adopting the zinc blende structure ($\text{C.I.} = 4$, Slide 9).
- c) $\text{UO}_2$, $\text{ThO}_2$, and $\text{CeO}_2$ are $AX_2$ dioxides adopting the fluorite ($\text{CaF}_2$) structure (Slide 10).

### Source

Session 16, Slides 7-10 and 14.

## Q64.8 Ions on (111) planes and [111] directions in MgO and ZnS

- id: B64-Q8
- concept_id: u8-ax-linear-planar-intuition
- format: topic-true
- asks: comparison

Referring to the $(111)$ plane triangle and $[111]$ body diagonal of cubic rock salt ($\text{MgO}$) and zinc blende ($\text{ZnS}$) unit cells, indicate which statement is TRUE:

a) In rock salt $\text{MgO}$, the $(111)$ triangle through $(1,0,0)$, $(0,1,0)$, and $(0,0,1)$ holds equal numbers of $\text{Mg}^{2+}$ and $\text{O}^{2-}$ ions
b) In zinc blende $\text{ZnS}$, the $[111]$ body diagonal passes through two occupied $\text{Zn}^{2+}$ tetrahedral sites at $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$ and $(\frac{3}{4},\frac{3}{4},\frac{3}{4})$
c) In both rock salt and zinc blende, the $(111)$ triangle cuts only the FCC anion sublattice (2 anions), whereas $[111]$ intersects both cations and anions
d) In $\text{CsCl}$, the $(100)$ cube face contains both $\text{Cs}^+$ and $\text{Cl}^-$ ions in a $1:1$ ratio

### Answer

c

### Explanation

Problems T8_CeramicMaterials.pdf, Problems 1 and 7: in both $\text{MgO}$ (rock salt) and $\text{ZnS}$ (zinc blende), the $(111)$ plane $x + y + z = 1$ contains only the FCC anions ($3\times\frac{1}{6}$ corners $+ 3\times\frac{1}{2}$ face centres $= 2$ anions), while the $[111]$ body diagonal intersects corner anions ($2\times\frac{1}{2} = 1$) plus the interior cation ($\text{Mg}^{2+}$ at $(\frac{1}{2},\frac{1}{2},\frac{1}{2})$ in $\text{MgO}$, or $\text{Zn}^{2+}$ at $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$ in $\text{ZnS}$).

- a) In $\text{MgO}$, $\text{Mg}^{2+}$ ions sit at edge midpoints ($x+y+z=\frac{1}{2}$) and body centre ($\frac{3}{2}$), lying in parallel planes outside $(111)$.
- b) In $\text{ZnS}$, only half of the tetrahedral sites are occupied, so $(\frac{3}{4},\frac{3}{4},\frac{3}{4})$ is empty when $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$ is filled.
- d) In $\text{CsCl}$, $\text{Cs}^+$ sits at the interior body centre $(\frac{1}{2},\frac{1}{2},\frac{1}{2})$ and does not lie on the $(100)$ cube face.

### Source

Problems T8_CeramicMaterials.pdf, Problems 1 and 7; Session 16, Slides 7-9.

## Q64.9 Why covalent SiC and ZnS favor zinc blende

- id: B64-Q9
- concept_id: u8-zincblende-structure
- format: cause-effect
- asks: cause

Although $\text{ZnS}$ and $\text{SiC}$ have strongly covalent bonding ($\sim 87\text{–}89\%$ covalent character), they adopt the zinc blende structure because:

a) directional $sp^3$ covalent orbitals require an octahedral coordination of six neighbours
b) tetrahedral sites provide four neighbours at $109.5^\circ$, matching directional $sp^3$ covalent bonding
c) filling half the tetrahedral sites creates a net positive charge that stabilizes covalent sharing
d) an FCC anion cell provides four tetrahedral interstitial sites instead of eight

### Answer

b

### Explanation

Session 16, Slides 5, 9, and 15: Pauling's relation gives high covalent character for $\text{ZnS}$ ($\sim 87\%$) and $\text{SiC}$ ($89\%$), and each tetrahedral interstitial site provides $\text{C.I.} = 4$ arranged symmetrically at $109.5^\circ$, matching the geometry of directional $sp^3$ covalent bonds.

- a) Confuses $\text{C.I.} = 6$ (octahedral) with $sp^3$ hybridization, which forms four bonds in a tetrahedron.
- c) Violates electroneutrality: filling $4$ tetrahedral sites with divalent cations balances the $4$ FCC anions ($4\ \text{ZnS}$ formula units, zero net charge).
- d) Misstates the FCC void count: an FCC cell contains $8$ tetrahedral sites, of which zinc blende fills half ($4$).

### Source

Session 16, Slides 5, 6, 9, and 15.

## Q64.10 Ion sequence along the [100] cube edge

- id: B64-Q10
- concept_id: u8-ax-linear-planar-intuition
- format: what-happens
- asks: effect

Comparing the $[100]$ cube edge from $(0,0,0)$ to $(1,0,0)$ in rock salt ($\text{NaCl}$) and in cesium chloride ($\text{CsCl}$), the ion centres encountered along the edge are, respectively:

a) anion–cation–anion in $\text{NaCl}$, and anion–anion only in $\text{CsCl}$
b) anion–anion only in $\text{NaCl}$, and anion–cation–anion in $\text{CsCl}$
c) anion–cation–anion in both structures, because both share the $AX$ formula
d) cation–cation–anion in $\text{NaCl}$, and anion–cation–anion in $\text{CsCl}$

### Answer

a

### Explanation

Session 16, Slides 7-8: in $\text{NaCl}$, $\text{Cl}^-$ anions sit at corners $(0,0,0)$ and $(1,0,0)$ while a $\text{Na}^+$ cation sits at the edge midpoint $(\frac{1}{2},0,0)$, giving anion–cation–anion along $[100]$. In $\text{CsCl}$, $\text{Cl}^-$ anions sit at corners while $\text{Cs}^+$ sits at the cube centre $(\frac{1}{2},\frac{1}{2},\frac{1}{2})$, so no cation lies on the $[100]$ cube edge.

- b) Swaps the edge occupancies of $\text{NaCl}$ and $\text{CsCl}$.
- c) Assumes equal $AX$ stoichiometry implies identical edge occupancy, overlooking where the cation sits in $\text{CsCl}$.
- d) Places different ions on equivalent cube corners of $\text{NaCl}$, violating lattice periodicity.

### Source

Session 16, Slides 7-8.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
