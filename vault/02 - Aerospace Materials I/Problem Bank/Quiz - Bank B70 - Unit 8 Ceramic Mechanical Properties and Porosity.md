---
materia: Aerospace Materials I
tema: "Unit 8: mechanical properties of ceramics, porosity, tension vs compression, three-point bending MOR and Weibull scatter"
bank_id: B70
title: "Ceramic mechanical properties and porosity"
category: mt3_test_block
unit: 8
concepts:
  - u8-mech-insulators-strength
  - u8-mech-hardness-brittleness
  - u8-mech-stiffness-specific
  - u8-mech-tension-compression
  - u8-mech-porosity-strength
  - u8-mech-porosity-modulus
  - u8-mech-three-point-bending
  - u8-weibull-scatter
difficulty: 2
origen: "Includes official exam items from MATERIALS_THIRDPARTIAL_2020_V2.pdf (Paper B, Q4), MATERIALS_FINALEXAM_2012_EXTRA.pdf (Q7), and MATERIALS_FINALEXAM_2014_EXTRA.pdf (Q4); remaining items written for the bank in the style of Part I of Assessment Test III. Content from Session 16, Slides 2-3 and 16-20."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-8
---

# Bank B70 — Ceramic mechanical properties and porosity

> [!info] Includes official exam questions
> Ten test questions in the style of Part I of Assessment Test III (four options, one right answer; +0.5 right, -0.15 wrong), including official exam items from the 2020 Paper B and the 2012 and 2014 extraordinary finals. Content: Session 16, Slides 2-3 and 16-20.

## Q70.1 General ceramic properties

- id: B70-Q1
- concept_id: u8-mech-insulators-strength
- format: true-statement
- asks: classification
- origin: official-exam

Indicate which of the following statements is TRUE:

a) Ceramics present better properties in tension than in compression
b) Ceramics exhibit high elastic modulus and high thermal shock resistance
c) SiO₂ is a glass modifier which decreases viscosity to lead to better glass workability
d) Ceramics are good electrical and thermal insulators

### Answer

d

### Explanation

Session 16, Slides 2-3 (and `MATERIALS_THIRDPARTIAL_2020_V2.pdf`, Paper B Q4): because valence electrons in ionic and covalent ceramic bonds are localized rather than forming a free-electron gas, ceramics have very low electrical and thermal conductivity and serve as good electrical and thermal insulators.

- a) Inverts the mechanical behaviour of ceramics: compressive strength is much higher than tensile strength because cracks grow stably in compression and unstably in tension (Slide 18).
- b) Ceramics combine high elastic modulus $E$ with low thermal conductivity $k$, which lowers $TSR = \sigma_f k/(E\alpha_l)$ and gives low thermal shock resistance (Slides 3 and 21).
- c) Misclassifies $\text{SiO}_2$: silica is a glass former that builds the three-dimensional network, whereas oxides such as $\text{Na}_2\text{O}$ and $\text{CaO}$ act as glass modifiers (Slide 28).

### Source

MATERIALS_THIRDPARTIAL_2020_V2.pdf, p. 4 (Paper B, Q4); Session 16, Slides 2-3, 18, 21 and 28.

## Q70.2 Structural origin of hardness and brittleness

- id: B70-Q2
- concept_id: u8-mech-hardness-brittleness
- format: cause-effect
- asks: cause
- origin: official-exam

Which structural features explain why ceramic materials exhibit both very high hardness and brittle fracture at room temperature?

a) Free-electron clouds bond ions weakly and allow easy dislocation slip at low stress
b) Strong ionic and covalent bonds resist deformation and prevent dislocation motion, so cracks grow before yielding
c) Weak secondary van der Waals forces between atomic planes permit cleavage without plastic flow
d) High densities of pre-existing metallic dislocations lock together as soon as any tensile load is applied

### Answer

b

### Explanation

`MATERIALS_FINALEXAM_2012_EXTRA.pdf`, Q7 (and Session 16, Slides 3 and 16-17): strong ionic and/or covalent bonds create a deep interatomic potential well and high lattice resistance, giving ceramics high hardness and stiffness; because dislocation motion is suppressed by directional covalent bonds or like-ion electrostatic repulsion, stress concentrations at flaws cannot blunt by plastic yielding, producing catastrophic brittle fracture ($\sigma_y = UTS = \sigma_{\text{fracture}}$).

- a) Describes metallic bonding with easy dislocation glide, which produces ductility and lower hardness rather than ceramic brittleness.
- c) Attributes ceramic behaviour to secondary van der Waals bonding, which governs polymers rather than primary-bonded inorganic ceramics.
- d) Misstates the cause of brittleness: ceramics fracture before plastic flow because dislocations cannot move readily at room temperature, not because of metallic dislocation tangling.

### Source

MATERIALS_FINALEXAM_2012_EXTRA.pdf, p. 2 (Q7); Session 16, Slides 3 and 16-17.

## Q70.3 Hardness and specific modulus of ceramics

- id: B70-Q3
- concept_id: u8-mech-stiffness-specific
- format: topic-true
- asks: comparison

Referring to the hardness and elastic stiffness of ceramic materials, which one of the following statements is TRUE:

a) Covalent ceramics such as SiC are harder than ionic oxides such as Al₂O₃, and ceramic fibres provide a high specific modulus $E/\rho$
b) Ionic oxide ceramics are harder than covalent carbides because electrostatic attraction exceeds covalent bond strength
c) The Young's modulus of crystalline ceramics decreases markedly with loading duration at room temperature
d) Ceramics have lower Young's moduli than common engineering metals because their ionic lattices are more open

### Answer

a

### Explanation

Session 16, Slide 16: hardness is greater in covalent ceramics (diamond, $\text{SiC}$) than in ionic oxides ($\text{Al}_2\text{O}_3$, $\text{ZrO}_2$), ceramic elastic moduli exceed those of metals due to strong bonding, and low density gives high specific modulus $E/\rho$ (e.g. $100\ \text{GPa}/(\text{Mg/m}^3)$ for alumina vs. $27$ for steel), making ceramic fibres ideal composite reinforcements.

- b) Inverts the hardness ranking between covalent carbides/diamond and ionic oxide ceramics (Slide 16).
- c) Wrongly attributes polymer viscoelastic time dependence to ceramics; Slide 16 explicitly states $E \neq f(\text{time the load is applied})$.
- d) Inverts the stiffness relation: $E_{\text{ceramics}} > E_{\text{metals}}$ because ionic and covalent bonds are stronger than metallic bonds.

### Source

Session 16, Slide 16.

## Q70.4 Tension versus compression testing

- id: B70-Q4
- concept_id: u8-mech-tension-compression
- format: topic-false
- asks: comparison

Regarding uniaxial tension and compression testing of ceramic specimens, which one of the following statements is FALSE:

a) Clamping a ceramic specimen in tensile grips easily creates surface cracks that propagate rapidly across the section
b) Under compressive loading, cracks grow stably parallel to the load axis and many must link before total collapse
c) Uniaxial tension yields a higher measured strength and smaller scatter than compression because cracks close under tensile stress
d) Compression testing is simpler to perform on ceramics and produces smaller stress concentrations at defects than tension

### Answer

c

### Explanation

Session 16, Slide 18: under tension, cracks perpendicular to the load open and the largest flaw runs unstably, producing low strength and high scatter; under compression, flaws experience smaller stress concentration and grow stably parallel to the applied axis, giving much higher compressive strength and smaller dispersion. Statement c) is false.

- a) True: Slide 18 notes that gripping specimens by clamps generates cracks that propagate, making tensile tests difficult.
- b) True: the compression crack diagram on Slide 18 shows multiple cracks growing parallel to the compressive load rather than opening catastrophically.
- d) True: Slide 18 states that compression tests are simpler than tension tests, with smaller defect stress concentrations and lower dispersion.

### Source

Session 16, Slide 18.

## Q70.5 Porosity effect on flexural strength

- id: B70-Q5
- concept_id: u8-mech-porosity-strength
- format: diagram-reading
- asks: figure-reading

The curve below shows how the flexural strength of a ceramic varies with volume fraction porosity $P$. Based on the curve, increasing the porosity from $P = 0.05$ to $P = 0.40$ causes the average flexural strength to:

![[attachments/T8/s16-porosity-flexural-strength.png]]

a) drop slightly from roughly 195 MPa to 160 MPa, because isolated pores leave most of the load-bearing section intact
b) stay nearly constant around 180 MPa up to $P = 0.30$ and fall sharply only above $P = 0.40$
c) rise from roughly 50 MPa to 180 MPa, because pores blunt advancing crack tips by redistributing local tension
d) fall sharply from roughly 175 MPa to about 45 MPa, because pores reduce the solid area and act as stress concentrators

### Answer

d

### Explanation

Session 16, Slide 17: reading the plotted trend for alumina, at $P = 0.05$ the mean curve lies near $175\text{ MPa}$ and decays exponentially to roughly $45\text{ MPa}$ at $P = 0.40$. Pores both reduce the load-bearing cross-sectional area and act as stress concentrators in a brittle matrix incapable of plastic crack blunting.

- a) Severely underestimates the strength loss visible on the vertical axis between $P = 0.05$ and $P = 0.40$.
- b) Misreads the exponential decay as a flat plateau; the steepest drop actually occurs at low porosity between $P = 0$ and $P = 0.20$.
- c) Inverts the direction of the curve and wrongly applies ductile crack-blunting behaviour to brittle ceramics.

### Source

Session 16, Slide 17.

## Q70.6 Porosity effect on elastic modulus

- id: B70-Q6
- concept_id: u8-mech-porosity-modulus
- format: what-happens
- asks: effect

When incomplete sintering leaves a rising volume fraction of pores $P$ inside an alumina part, what happens to its Young's modulus $E$ as $P$ increases from 0 toward 1?

a) It remains at the dense alumina value until $P = 0.5$ and then drops abruptly to zero
b) It decreases continuously and monotonically from the fully dense modulus toward zero as $P$ approaches 1
c) It increases slightly at low $P$ because internal pore surfaces stiffen neighbouring bonds
d) It increases linearly with $P$ because trapped gas inside closed pores resists compressive strain

### Answer

b

### Explanation

Session 16, Slide 17: the elastic modulus versus volume fraction porosity curve decreases smoothly and monotonically from the zero-porosity value $E_0$ (about $380\text{ GPa}$) down to zero as $P \to 1$, because void space carries no elastic load and reduces the effective solid cross-section.

- a) Confuses continuous modulus reduction with a sharp percolation threshold.
- c) Inverts the stiffness trend: adding empty volume lowers macroscopic stiffness rather than stiffening atomic bonds.
- d) Treats pore gas stiffness as comparable to an ionic-covalent ceramic lattice, whereas pores act mechanically as zero-stiffness voids.

### Source

Session 16, Slide 17.

## Q70.7 Stress distribution in three-point bending

- id: B70-Q7
- concept_id: u8-mech-three-point-bending
- format: complete-sentence
- asks: effect

In a three-point bending test of a ceramic bar loaded downward at mid-span:

a) the top surface is in compression and the bottom surface is in tension, so fracture initiates at the bottom surface
b) the top surface is in tension and the bottom surface is in compression, so fracture initiates beneath the central indenter
c) both outer surfaces carry pure shear stress while the neutral axis undergoes maximum tension
d) the bar yields plastically on the tensile side before breaking, so flexural strength equals tensile yield strength

### Answer

a

### Explanation

Session 16, Slide 19: under downward central loading, the upper face bends concavely in compression while the lower face is stretched in tension; because ceramics are far weaker in tension than in compression, brittle fracture starts at surface flaws along the bottom tensile face.

- b) Inverts the bending stress state between the upper concave surface and the lower convex surface.
- c) Confuses normal bending stress (maximum at the outer fibres, zero at the neutral axis) with shear stress.
- d) Assumes ductile plastic yielding in a ceramic; room-temperature ceramics fracture elastically without plastic yield (Slide 17).

### Source

Session 16, Slides 17 and 19.

## Q70.8 Modulus of rupture calculation

- id: B70-Q8
- concept_id: u8-mech-three-point-bending
- format: numeric
- asks: calculation
- calc: 3*1000*40/(2*8*5**2)

A ceramic bar of rectangular cross-section ($b = 8.0\ \text{mm}$, $d = 5.0\ \text{mm}$) is tested in three-point bending over a support span $L = 40\ \text{mm}$ and fractures at a central load $F_f = 1000\ \text{N}$. Calculate its flexural strength (modulus of rupture):

![[attachments/T8/s16-three-point-bending.png]]

a) 200 MPa
b) 600 MPa
c) 300 MPa
d) 1500 MPa

### Answer

c

### Explanation

Session 16, Slide 19: for a rectangular bar in three-point bending, the flexural strength (modulus of rupture) is $\sigma_{fs} = \dfrac{3 F_f L}{2 b d^2} = \dfrac{3 \times 1000\ \text{N} \times 40\ \text{mm}}{2 \times 8.0\ \text{mm} \times (5.0\ \text{mm})^2} = \dfrac{120\,000}{400} = 300\ \text{MPa}$.

- a) Omits the $3/2$ prefactor, computing $F_f L / (b d^2) = 200\ \text{MPa}$.
- b) Omits the factor of $2$ in the denominator, computing $3 F_f L / (b d^2) = 600\ \text{MPa}$.
- d) Forgets to square the section depth $d$, computing $3 F_f L / (2 b d) = 1500$, which does not even have units of stress.

### Source

Session 16, Slide 19.

## Q70.9 Stiffness ranking across material classes

- id: B70-Q9
- concept_id: u8-mech-stiffness-specific
- format: ordering
- asks: comparison
- origin: official-exam

Rank the following four materials in order of INCREASING elastic modulus $E$:

a) aluminium oxide, aluminium, epoxy resin, low-density polyethylene
b) low-density polyethylene, aluminium, epoxy resin, aluminium oxide
c) epoxy resin, low-density polyethylene, aluminium, aluminium oxide
d) low-density polyethylene, epoxy resin, aluminium, aluminium oxide

### Answer

d

### Explanation

`MATERIALS_FINALEXAM_2014_EXTRA.pdf`, Q4 (and Session 16, Slide 16): stiffness follows atomic bond strength. Low-density polyethylene has weak secondary van der Waals interchain bonds ($E < 1\ \text{GPa}$); epoxy resin is a densely crosslinked thermoset network ($E \approx 2\text{–}4\ \text{GPa}$); aluminium has metallic bonding ($E \approx 70\ \text{GPa}$); and aluminium oxide ($\text{Al}_2\text{O}_3$) has strong mixed ionic-covalent bonding ($E \approx 390\ \text{GPa}$).

- a) Reverses the ranking into decreasing order of Young's modulus.
- b) Places metallic aluminium below crosslinked epoxy resin, ignoring the much higher stiffness of primary metallic bonds relative to a polymer network.
- c) Places a lightly branched thermoplastic (LDPE) above a rigid crosslinked thermoset (epoxy).

### Source

MATERIALS_FINALEXAM_2014_EXTRA.pdf, p. 6 (Q4); Session 16, Slides 3 and 16.

## Q70.10 Weibull modulus and strength scatter

- id: B70-Q10
- concept_id: u8-weibull-scatter
- format: cause-effect
- asks: definition

Even under identical testing conditions, nominal fracture stress varies widely across ceramic specimens, and this statistical dispersion is described by the Weibull modulus $k$. Compared with a metal, a ceramic having a lower Weibull modulus $k$ exhibits:

a) a higher minimum threshold strength $x_0$ and a narrower strength distribution
b) greater sample-to-sample scatter in fracture strength because failure is controlled by the largest random flaw
c) deterministic yielding at a single well-defined tensile strength independent of specimen volume
d) reduced strength variability because internal pores distribute applied loads evenly

### Answer

b

### Explanation

Session 16, Slide 20: the Weibull distribution models statistical strength scatter in brittle ceramics; a lower Weibull modulus $k$ corresponds to a broader distribution and greater variation in fracture strength from specimen to specimen, because each specimen fails when its worst random flaw reaches critical stress.

- a) Inverts the meaning of $k$: a *higher* Weibull modulus produces a narrower distribution, whereas ceramics have low $k$ and wide scatter.
- c) Describes ductile metallic behaviour with reproducible yield stress, not flaw-sensitive brittle ceramics.
- d) Contradicts Slide 17 and Slide 20: pores act as stress concentrators that increase scatter rather than homogenizing stress.

### Source

Session 16, Slides 17 and 20.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
