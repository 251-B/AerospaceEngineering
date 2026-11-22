---
materia: Aerospace Materials I
tema: "Unit 8: general ceramic properties, bonding-property chain, traditional vs engineering ceramics, Pauling ionic character and ionic packing rules"
bank_id: B63
title: "Ceramic bonding and packing rules"
category: mt3_test_block
unit: 8
concepts:
  - u8-ceramic-general-properties
  - u8-ceramic-bonding-property-chain
  - u8-traditional-vs-engineering-ceramics
  - u8-ionic-packing-factors
  - u8-pauling-ionic-character
  - u8-pauling-ionic-trend
  - u8-radius-ratio-limits
  - u8-coordination-contact-stability
  - u8-electroneutrality-rule
difficulty: 2
origen: "Includes Question 2 of MATERIALS_THIRDPARTIAL_2020.pdf (p. 1) alongside practice items in the style of Part I of Assessment Test III. Content and data from Session 16 Slides 2-6 and Session 18 Slides 4-5, 42."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-8
---

# Bank B63 — Ceramic bonding and packing rules

> [!info] Includes official exam questions
> Ten test questions in the style of Part I of Assessment Test III (four options, one right answer; +0.5 right, -0.15 wrong). Question 4 is Question 2 of `MATERIALS_THIRDPARTIAL_2020.pdf`; the remaining nine are practice items. Content: Session 16, Slides 2-6 and Session 18, Slides 4-5 and 42.

## Q63.1 General properties and atomic bonding of ceramics

- id: B63-Q1
- concept_id: u8-ceramic-general-properties
- format: true-statement
- asks: cause

Which of the following statements about crystalline ceramics and their atomic bonding is TRUE:

a) Low melting points and ductile yielding arise from delocalized metallic electron clouds
b) High elastic modulus, hardness, and brittleness arise from strong ionic or covalent bonds
c) High thermal shock resistance results from combining a high Young's modulus with low thermal conductivity
d) High electrical conductivity at room temperature follows from rapid electron transport between ions

### Answer

b

### Explanation

Session 16, Slides 2-3: ceramic materials consist of metals and non-metals joined by strong ionic and/or covalent bonds without an electronic cloud, which produces high Young's modulus, high melting point, hardness, brittleness, high compressive strength, chemical stability, and limited electrical and thermal conductivity.

- a) Attributes metallic bonding (electron sea and ductility) to ceramics, which lack free electrons and fracture without plastic yielding.
- c) Inverts the thermal shock resistance relation: $TSR = \sigma_f k / (E\alpha_l)$ is *low* when $E$ is high and $k$ is low.
- d) Contradicts the absence of free electrons in ceramics, which makes typical ceramics electrical insulators at room temperature.

### Source

Session 16, Slides 2-3.

## Q63.2 Ceramic behaviour under room-temperature tension

- id: B63-Q2
- concept_id: u8-ceramic-bonding-property-chain
- format: what-happens
- asks: effect

Because strong ceramic bonds lock valence electrons tightly rather than forming a free-electron sea, a crystalline ceramic bar loaded in tension at room temperature will typically:

a) yield plastically at low stress through easy dislocation glide
b) absorb large strains by necking before final rupture
c) conduct electric current readily through delocalized valence electrons
d) fracture catastrophically before any measurable plastic deformation occurs

### Answer

d

### Explanation

Session 16, Slides 2-3, 17-18: localized ionic and covalent bonds prevent dislocation motion at room temperature, so ceramics break in a brittle, catastrophic manner with $\sigma_y = UTS = \sigma_{\text{fracture}}$ and lack free electrons for conduction.

- a) Confuses ceramic bonding with metallic bonding, where non-directional electron-sea bonds allow dislocation glide.
- b) Describes ductile metallic necking rather than brittle ceramic rupture without plastic strain.
- c) Ignores that electrons are localized on anions or shared in covalent bonds, leaving ceramics as insulators at room temperature.

### Source

Session 16, Slides 2-3 and 17-18.

## Q63.3 Traditional ceramics against engineering ceramics

- id: B63-Q3
- concept_id: u8-traditional-vs-engineering-ceramics
- format: topic-false
- asks: classification

Regarding traditional ceramics and engineering (advanced) ceramics, indicate which statement is FALSE:

a) Engineering ceramics are clay-based mixtures of natural quartz and feldspar used mainly for low-cost bricks
b) Traditional ceramics include porous wares such as bricks and pottery alongside compact porcelain made from clay, silica, and feldspar
c) Engineering ceramics include refractories such as $\text{Al}_2\text{O}_3$ and $\text{ZrO}_2$, abrasives such as $\text{Si}_3\text{N}_4$ and $\text{SiC}$, and ferroelectrics such as $\text{BaTiO}_3$
d) Superconducting oxides such as $\text{YBa}_2\text{Cu}_3\text{O}_7$ and bioceramics such as hydroxyapatite belong to engineering ceramics

### Answer

a

### Explanation

Session 16, Slide 4 and Session 18, Slides 4-5 and 42: traditional ceramics are low-cost clay-based products made from natural clay ($\text{Al}_2\text{O}_3\cdot\text{SiO}_2\cdot\text{H}_2\text{O}$), silica ($\text{SiO}_2$), and feldspar ($\text{K}_2\text{O}\cdot\text{Al}_2\text{O}_3\cdot 6\text{SiO}_2$), whereas engineering (advanced) ceramics rely on synthesized high-purity powders such as $\text{Al}_2\text{O}_3$, $\text{ZrO}_2$, $\text{SiC}$, $\text{Si}_3\text{N}_4$, and $\text{BaTiO}_3$. Statement a) is false.

- b) True (Session 16, Slide 4; Session 18, Slide 42): bricks, pottery, china, porcelain, and earthenware are traditional clay ceramics.
- c) True (Session 16, Slide 4): lists refractory oxides, nitride/carbide abrasives, and $\text{BaTiO}_3$ ferroelectrics under engineering ceramics.
- d) True (Session 16, Slide 4): classifies $\text{YBa}_2\text{Cu}_3\text{O}_7$ superconductors and hydroxyapatite biomaterials under engineering ceramics.

### Source

Session 16, Slide 4; Session 18, Slides 4-5 and 42.

## Q63.4 Factors governing packing in ionic ceramics

- id: B63-Q4
- concept_id: u8-ionic-packing-factors
- format: identify
- asks: cause
- origin: official-exam

Which of the following factors are important in determining the packing of anions and cations in an ionic solid?

a) Lattice energy
b) Valence and bond length
c) Relative size of anions and cations and electroneutrality
d) All of the above

### Answer

c

### Explanation

MATERIALS_THIRDPARTIAL_2020.pdf, p. 1 (Part I, Q2) and Session 16, Slide 6: the crystal lattice formed by packing anions with cations in interstitial sites is governed by the relative sizes of the ions ($r_C/r_A$, which fixes the coordination index) and electrical neutrality (electroneutrality, which fixes the cation-to-anion ratio).

- a) Lattice energy reflects bond strength and thermal stability once ions are arranged, rather than serving as the geometric packing rule.
- b) Valence alone without charge balance and bond length without the cation-to-anion radius ratio do not determine the coordination polyhedron.
- d) Wrongly includes lattice energy and bond length alongside the true packing criteria.

### Source

MATERIALS_THIRDPARTIAL_2020.pdf, p. 1 (Part I, Q2); Session 16, Slide 6.

## Q63.5 Pauling percent ionic character calculation

- id: B63-Q5
- concept_id: u8-pauling-ionic-character
- format: numeric
- asks: calculation
- calc: 100*(1 - exp(-(1.8**2)/4))

Two elements $A$ and $B$ in a ceramic bond have electronegativities $X_A = 3.5$ and $X_B = 1.7$. Using Pauling's formula, calculate the percentage of ionic character of the $A\text{–}B$ bond:

a) 36.2 %
b) 55.5 %
c) 44.5 %
d) 80.2 %

### Answer

b

### Explanation

Session 16, Slide 5: Pauling's relation gives $\%\ \text{ionic character} = 100\left\{1 - \exp\!\left[-\dfrac{(X_A - X_B)^2}{4}\right]\right\}$. With $X_A - X_B = 3.5 - 1.7 = 1.8$, $\dfrac{1.8^2}{4} = 0.81$, so $\%\ \text{ionic character} = 100(1 - e^{-0.81}) = 100(1 - 0.4449) = 55.5\ \%$.

- a) Forgot to square the electronegativity difference: $100(1 - e^{-1.8/4}) = 36.2\ \%$.
- c) Reported the percentage of covalent character ($100\,e^{-0.81} = 44.5\ \%$) instead of the percentage of ionic character.
- d) Divided by $2$ instead of $4$ in the exponent: $100(1 - e^{-1.8^2/2}) = 80.2\ \%$.

### Source

Session 16, Slide 5.

## Q63.6 Ranking ceramics by covalent bonding character

- id: B63-Q6
- concept_id: u8-pauling-ionic-trend
- format: ordering
- asks: comparison

Given the Pauling electronegativity differences $\Delta X$ ($\text{Mg–O} = 2.3$, $\text{Al–O} = 2.0$, $\text{Si–O} = 1.7$, $\text{Si–C} = 0.7$), rank $\text{MgO}$, $\text{Al}_2\text{O}_3$, $\text{SiO}_2$, and $\text{SiC}$ in order of increasing covalent bonding character:

a) $\text{MgO} < \text{Al}_2\text{O}_3 < \text{SiO}_2 < \text{SiC}$
b) $\text{SiC} < \text{SiO}_2 < \text{Al}_2\text{O}_3 < \text{MgO}$
c) $\text{Al}_2\text{O}_3 < \text{MgO} < \text{SiO}_2 < \text{SiC}$
d) $\text{MgO} < \text{SiO}_2 < \text{Al}_2\text{O}_3 < \text{SiC}$

### Answer

a

### Explanation

Session 16, Slide 5: as $\Delta X = |X_A - X_B|$ decreases, the Pauling percentage of ionic character falls and the covalent character rises: $\text{MgO}$ ($73\%$ ionic, $27\%$ covalent), $\text{Al}_2\text{O}_3$ ($63\%$ ionic, $37\%$ covalent), $\text{SiO}_2$ ($51\%$ ionic, $49\%$ covalent), and $\text{SiC}$ ($11\%$ ionic, $89\%$ covalent).

- b) Reverses the trend, ordering the compounds by increasing ionic character instead of increasing covalent character.
- c) Swaps $\text{Al}_2\text{O}_3$ ($\Delta X = 2.0$) and $\text{MgO}$ ($\Delta X = 2.3$), failing to place the largest $\Delta X$ as most ionic.
- d) Swaps $\text{SiO}_2$ ($\Delta X = 1.7$) and $\text{Al}_2\text{O}_3$ ($\Delta X = 2.0$) in the middle of the ranking.

### Source

Session 16, Slide 5.

## Q63.7 Coordination polyhedron from radius ratio

- id: B63-Q7
- concept_id: u8-radius-ratio-limits
- format: identify
- asks: classification

A binary ionic ceramic has a cation-to-anion radius ratio $r_C / r_A = 0.345$. Which coordination index and geometric arrangement of anions around each central cation are predicted?

a) $\text{C.I.} = 8$, corners of a cube
b) $\text{C.I.} = 6$, corners of an octahedron
c) $\text{C.I.} = 3$, corners of a triangle
d) $\text{C.I.} = 4$, corners of a tetrahedron

### Answer

d

### Explanation

Session 16, Slides 6 and 9: the radius ratio $r_C/r_A = 0.345$ falls inside the range $0.225\text{–}0.414$, which corresponds to $\text{C.I.} = 4$ with anions at the corners of a tetrahedron (the zinc blende range).

- a) Cubic coordination ($\text{C.I.} = 8$) requires $r_C/r_A$ in the range $0.732\text{–}1.0$.
- b) Octahedral coordination ($\text{C.I.} = 6$) requires $r_C/r_A$ in the range $0.414\text{–}0.732$.
- c) Triangular coordination ($\text{C.I.} = 3$) corresponds to the smaller ratio range $0.155\text{–}0.225$.

### Source

Session 16, Slides 6 and 9.

## Q63.8 Cause of unstable ionic coordination

- id: B63-Q8
- concept_id: u8-coordination-contact-stability
- format: cause-effect
- asks: cause

In an ionic crystal, if a cation is smaller than the minimum critical radius ratio for a given coordination polyhedron, that geometry becomes unstable because:

a) adjacent cations overlap across the faces of the surrounding polyhedron
b) the bond converts into a metallic sea and loses electrostatic attraction
c) the surrounding anions touch and repel while the undersized cation rattles inside
d) the cation pulls extra anions in until the coordination index rises to 12

### Answer

c

### Explanation

Session 16, Slide 6: the critical radius ratio corresponds to the minimum geometry where the central cation touches all surrounding anions just as the anions touch each other. For a smaller $r_C/r_A$, the anions make contact and repel electrostatically while the undersized cation fails to touch all of them, making the arrangement unstable.

- a) Misidentifies the colliding species: it is the larger surrounding *anions* that touch and repel when the central cation is too small.
- b) Confuses geometric hard-sphere contact instability with a change in chemical bond type.
- d) Inverts the coordination trend: reducing $r_C/r_A$ *decreases* the maximum stable coordination index rather than raising it.

### Source

Session 16, Slide 6.

## Q63.9 Shift in coordination across radius-ratio intervals

- id: B63-Q9
- concept_id: u8-radius-ratio-limits
- format: complete-sentence
- asks: definition

For ionic solids with $r_C < r_A$, increasing the radius ratio $r_C/r_A$ from the interval $0.155\text{–}0.225$ into $0.414\text{–}0.732$ shifts the stable cation coordination from:

a) triangular ($\text{C.I.} = 3$) to octahedral ($\text{C.I.} = 6$)
b) tetrahedral ($\text{C.I.} = 4$) to cubic ($\text{C.I.} = 8$)
c) linear ($\text{C.I.} = 2$) to tetrahedral ($\text{C.I.} = 4$)
d) triangular ($\text{C.I.} = 3$) to tetrahedral ($\text{C.I.} = 4$)

### Answer

a

### Explanation

Session 16, Slide 6: the interval $0.155\text{–}0.225$ corresponds to $\text{C.I.} = 3$ (corners of a triangle), $0.225\text{–}0.414$ to $\text{C.I.} = 4$ (tetrahedron), $0.414\text{–}0.732$ to $\text{C.I.} = 6$ (octahedron), and $0.732\text{–}1.0$ to $\text{C.I.} = 8$ (cube).

- b) Shifts each interval up by one coordination shell ($0.225\text{–}0.414$ and $0.732\text{–}1.0$).
- c) Assigns the $< 0.155$ ($\text{C.I.} = 2$) and $0.225\text{–}0.414$ ($\text{C.I.} = 4$) limits to the given ratios.
- d) Stops one coordination step early at $\text{C.I.} = 4$ ($0.225\text{–}0.414$) instead of reaching $\text{C.I.} = 6$.

### Source

Session 16, Slide 6.

## Q63.10 Electroneutrality and coordination stability in ionic solids

- id: B63-Q10
- concept_id: u8-electroneutrality-rule
- format: topic-false
- asks: application

With respect to electroneutrality and coordination in ionic crystals, indicate which statement is FALSE:

a) Macroscopic electroneutrality fixes the cation-to-anion stoichiometric ratio of the crystal unit cell
b) When $A^{m+}$ and $X^{n-}$ carry charges of different magnitude, their coordination indices differ in the inverse ratio
c) Pushing the surrounding anions apart while the central cation stays in full contact with every anion remains stable
d) An ionic crystal achieves its lowest energy by adopting the lowest possible coordination index allowed by $r_C/r_A$

### Answer

d

### Explanation

Session 16, Slide 6: ions pack densely to lower total energy, and *increasing* the coordination index *increases* stability, so a crystal adopts the highest coordination index for which the cation can still contact all its neighbouring anions. Statement d) is false.

- a) True (Session 16, Slide 6): electroneutrality requires total positive and negative charges in the cell to balance.
- b) True (Session 16, Slides 10-11): in $\text{CaF}_2$ ($+2/-1$), $\text{C.I.}(\text{Ca}^{2+}) = 8$ and $\text{C.I.}(\text{F}^-) = 4$ so total cation–anion bonds balance.
- c) True (Session 16, Slide 6, right-hand stability sketch): a cation larger than the minimum contact size pushes anions apart and contacts all of them stably.

### Source

Session 16, Slides 6 and 10-11.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
