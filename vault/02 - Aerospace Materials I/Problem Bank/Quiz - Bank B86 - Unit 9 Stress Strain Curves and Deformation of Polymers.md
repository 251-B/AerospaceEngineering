---
materia: Aerospace Materials I
tema: "Unit 9: polymer stress-strain curves, semicrystalline deformation mechanisms, cold drawing, orientation hardening, rolling vs casting, and elastomer elasticity"
bank_id: B86
title: "Stress-strain curves and deformation of polymers"
category: mt3_test_block
unit: 9
concepts:
  - u9-ss-deformation-strengthening
  - u9-deform-semicrystalline-origin
  - u9-ss-polymer-classes
  - u9-ss-polymers-vs-metals
  - u9-deform-semicrystalline-stages
  - u9-cold-drawing-mechanism
  - u9-cold-drawing-orientation
  - u9-rolling-vs-casting
  - u9-elastomer-uncoiling-curve
  - u9-ss-elastic-modulus-calc
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_THIRDPARTIAL_2020.pdf, including 2020 Model B Q6, 2014 ORD Q6, and Problems T9 Q3. Content from Session 19 Slides 32-44."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-9
---

# Bank B86 — Stress-strain curves and deformation of polymers

> [!info] Includes official exam questions
> Ten test questions written for the bank in the style of Part I of Assessment Test III, including official questions from Assessment Test III 2020 Model B (Q6), the January 2014 final exam (Q6), and Problems T9 Q3 (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 19, Slides 32–44.

## Q86.1 Polymer deformation, structure and monomer types

- id: B86-Q1
- concept_id: u9-ss-deformation-strengthening
- format: true-statement
- asks: classification
- origin: official-exam

Which of the following statements is TRUE:

a) Thermosetting polymers are usually crystalline
b) Thermoplastic polymers cannot be reheated
c) Deforming a polymer can increase their strength
d) Homopolymers contain more than one type of monomer

### Answer

c

### Explanation

2020 Assessment Test III, Model B Q6 (and Session 19, Slides 39 and 43): deforming a thermoplastic polymer orients its macromolecular chains parallel to the stretching axis, leading to more effective secondary interactions between them and increasing both strength and stiffness.

- a) False: thermosets are densely crosslinked 3D covalent networks and are amorphous (Session 20, Slides 6 and 36).
- b) False: thermoplastics have linear or branched chains held by weak van der Waals bonds, so they soften and flow when reheated (Session 20, Slides 5 and 7).
- d) False: a homopolymer contains only one type of monomer, whereas a copolymer combines two or more monomer types (Session 19, Slide 20).

### Source

MATERIALS_THIRDPARTIAL_2020.pdf, p. 2 Q6; Session 19, Slides 20, 39 and 43; Session 20, Slides 5–7 and 36.

## Q86.2 Where plastic deformation starts and effect of crystallinity

- id: B86-Q2
- concept_id: u9-deform-semicrystalline-origin
- format: topic-true
- asks: cause
- origin: official-exam

Referring to the plastic deformation and properties of a semicrystalline polymer, which one of the following statements is TRUE:

a) Plastic deformation initiates inside dense crystalline lamellae before amorphous tie chains elongate
b) Plastic deformation starts in amorphous tie chains, and crystallinity raises strength and $T_m$
c) Increasing crystallinity reduces tensile strength because stiff lamellae nucleate brittle microvoids
d) Increasing crystallinity eliminates the melting temperature $T_m$, leaving a single glass transition

### Answer

b

### Explanation

January 2014 ordinary final exam, Q6 (official UC3M key) and Session 19, Slides 27, 41 and 43: plastic deformation of a semicrystalline polymer starts in the softer amorphous regions with elongation of amorphous tie chains, followed by lamellar tilting, crystalline block separation, and alignment. Higher crystallinity increases chain packing and intermolecular bonding, raising both mechanical strength and melting temperature $T_m$.

- a) Inverts the sequence: tie chains in the disordered amorphous layers deform before the stiff crystalline lamellae tilt and break into blocks.
- c) Inverts the trend: higher crystallinity increases packing density and intermolecular bonding, thereby *increasing* strength and $E$ (Slide 43).
- d) Confuses semicrystalline and amorphous polymers: crystalline regions are what produce $T_m$ (Slides 23 and 28).

### Source

MATERIALS_FINALEXAM_COMPILATION_2013-2017.pdf, p. 16 (2014 ORD Q6 official key); Session 19, Slides 27, 41 and 43.

## Q86.3 Classifying polymer stress-strain curves

- id: B86-Q3
- concept_id: u9-ss-polymer-classes
- format: diagram-reading
- asks: figure-reading

![[attachments/T9/s19-stress-strain-classes.png]]

Which polymer categories correspond respectively to the green curve (`Brittle Plastic`), the red curve (`Hard & Tough Plastic` ending with `Strain Hardening`), and the blue curve (`Elastomer`)?

a) Green: lightly crosslinked rubber; Red: heavily crosslinked epoxy; Blue: polystyrene below $T_g$
b) Green: ductile nylon; Red: brittle ceramic oxide; Blue: heavily crosslinked phenolic thermoset
c) Green: ductile low-density polyethylene; Red: uncrosslinked rubber; Blue: rigid phenolic resin
d) Green: glassy polymer or thermoset; Red: drawn semicrystalline thermoplastic; Blue: lightly crosslinked elastomer

### Answer

d

### Explanation

Session 19, Slides 32, 34–40, and 44: the steep linear green curve fractures at small strain without yielding (typical of a brittle thermoset or a glassy thermoplastic well below $T_g$). The red curve yields, drops into neck propagation (cold drawing plateau), and strain-hardens as chains align (typical of a ductile semicrystalline thermoplastic like 6,6-nylon). The blue curve reaches very large, mostly reversible strains at low stress (an elastomer).

- a) Completely scrambles the three classes, putting soft rubber on the steepest brittle curve and glassy PS on the high-strain elastomer curve.
- b) Assigns ductile nylon to the brittle curve and rigid vulcanized thermoset to the soft elastomer curve.
- c) Assigns rigid phenolic resin (a brittle thermoset) to the elastomer curve and ductile LDPE to the brittle curve.

### Source

Session 19, Slides 32, 34–40 and 44.

## Q86.4 Mechanical behaviour of polymers compared with metals

- id: B86-Q4
- concept_id: u9-ss-polymers-vs-metals
- format: topic-false
- asks: comparison

Regarding the tensile properties of polymers compared with metals, which one of the following statements is FALSE:

a) Polymer elastic moduli typically fall in the range $0.007\text{–}4\text{ GPa}$, far lower than the $48\text{–}410\text{ GPa}$ range of metals
b) Ductile polymers typically yield around $5\text{–}10\%$ strain, whereas structural metals yield below $0.1\%$ strain
c) In polymers, the tensile strength is defined strictly as the stress at the upper yield maximum rather than at fracture
d) Maximum tensile elongations in polymers can exceed $1000\%$, whereas metals remain below $100\%$

### Answer

c

### Explanation

Session 19, Slides 32–33 and 36: for polymers, `Tensile strength: stress at which fracture occurs` (Slide 33), which may lie either above or below the yield peak $\sigma_y$ depending on whether strain hardening occurs before failure. Statement c is false.

- a) True: Slide 32 lists $E = 0.007\text{–}4\text{ GPa}$ for polymers against $48\text{–}410\text{ GPa}$ for metals.
- b) True: Slide 36 explicitly contrasts polymer yielding at $5\text{–}10\%$ strain with metallic yielding below $0.1\%$ strain.
- d) True: Slide 32 lists $\%\varepsilon_m > 1000\%$ possible for polymers against $< 100\%$ for metals.

### Source

Session 19, Slides 32, 33 and 36.

## Q86.5 Microscopic sequence of plastic deformation in semicrystalline polymers

- id: B86-Q5
- concept_id: u9-deform-semicrystalline-stages
- format: ordering
- asks: effect

Arrange the four irreversible stages that follow elastic deformation when a semicrystalline polymer is stretched to high strain in tension:

1. Separation of crystalline block segments and initial alignment with the tensile axis
2. Orientation of both crystalline block segments and tie chains parallel to the tensile axis
3. Elongation of amorphous tie chains between lamellae
4. Tilting of lamellar chain folds toward the loading direction

a) $3 \rightarrow 1 \rightarrow 4 \rightarrow 2$
b) $4 \rightarrow 3 \rightarrow 1 \rightarrow 2$
c) $3 \rightarrow 4 \rightarrow 1 \rightarrow 2$
d) $1 \rightarrow 4 \rightarrow 3 \rightarrow 2$

### Answer

c

### Explanation

Session 19, Slide 41 and 2014 ORD Q6 official key: following initial elastic stretching, plastic deformation begins with (3) elongation of the amorphous tie chains, then (4) tilting of the lamellar chain folds, followed by (1) separation of crystalline block segments and alignment with the tensile axis, and finally (2) full orientation of both block segments and tie chains along the tensile axis.

- a) Places block-segment separation before lamellar chain-fold tilting.
- b) Places lamellar tilting before tie-chain elongation in the amorphous layers.
- d) Incorrectly starts plastic deformation by breaking crystalline blocks apart before deforming the amorphous tie chains.

### Source

Session 19, Slide 41; MATERIALS_FINALEXAM_COMPILATION_2013-2017.pdf, p. 16 (2014 ORD Q6).

## Q86.6 Why necking propagates along a polymer specimen

- id: B86-Q6
- concept_id: u9-cold-drawing-mechanism
- format: what-happens
- asks: effect

After a ductile thermoplastic passes its yield peak and forms a local neck, why does the neck propagate along the specimen length at nearly constant stress instead of narrowing locally until prompt fracture?

a) Dislocation pile-ups at crystal grain boundaries pin the local neck permanently
b) Local frictional melting inside the neck reduces its cross-sectional area immediately
c) Rapid covalent crosslinking across the unnecked shoulders prevents further yielding
d) Chain alignment strengthens the neck so deformation shifts into unoriented zones

### Answer

d

### Explanation

Session 19, Slides 34, 37 and 38: as the neck forms, polymer chains unravel and align parallel to the tensile axis. Because oriented chains interact far more strongly, the necked zone becomes stronger and harder to stretch than the unnecked shoulders, so the neck propagates steadily across the gauge length (cold drawing) rather than sharpening to premature failure.

- a) Polymers do not deform by metallic crystal dislocation slip at grain boundaries.
- b) Cold drawing proceeds below $T_m$ by solid-state chain unravelling, not local melting.
- c) Unoriented thermoplastic shoulders contain no crosslinks; they deform progressively because they are *weaker* than the aligned neck.

### Source

Session 19, Slides 34, 37 and 38.

## Q86.7 Strain hardening after cold drawing

- id: B86-Q7
- concept_id: u9-cold-drawing-orientation
- format: complete-sentence
- asks: cause

Once cold drawing has propagated a neck along the entire gauge length of a thermoplastic specimen, the stress rises sharply until fracture because:

a) new monomer units condense spontaneously to double the molecular weight
b) chains align parallel to the tensile axis, raising stiffness and strength
c) amorphous regions crystallize into isotropic spherulites that soften the specimen
d) the glass transition temperature $T_g$ drops below the test temperature, causing flow

### Answer

b

### Explanation

Session 19, Slides 39–40: once the whole gauge section is necked, further extension stretches a fully oriented structure whose chains lie parallel to the applied load. An oriented polymer is substantially stronger and stiffer than an isotropic one, producing strain hardening until no further alignment is possible and failure occurs.

- a) Mechanical stretching at room temperature does not drive polymerization or increase molecular weight.
- c) Drawing destroys spherical spherulites and replaces them with an anisotropic fibrillar alignment, increasing—not softening—strength.
- d) Viscous flow above $T_g$ lowers stress rather than producing a steep upward strain-hardening tail.

### Source

Session 19, Slides 39–40.

## Q86.8 Rolling versus fast-cooled casting for polymer strength

- id: B86-Q8
- concept_id: u9-rolling-vs-casting
- format: cause-effect
- asks: comparison

When the same thermoplastic polymer is shaped either by rolling (mechanical deformation) or by casting with fast cooling, which method produces higher strength in the working direction and why?

a) Rolling, because deformation aligns chains for stronger interchain bonding
b) Fast-cooled casting, because rapid cooling maximizes spherulite size and packing density
c) Fast-cooled casting, because rapid cooling introduces covalent crosslinks between chains
d) Neither method differs, because tensile strength depends solely on the monomer repeat unit

### Answer

a

### Explanation

Problems T9 Q3 and Session 19, Slides 26, 38–39 and 43: rolling deforms the solid polymer and orients the macromolecular chains parallel to the rolling direction, creating stronger secondary interactions and higher strength (like cold drawing). Fast-cooled casting freezes the random coils from the melt into smaller crystals and larger amorphous regions with weaker isotropic properties.

- b) Inverts Slide 26: faster cooling gives *smaller* crystals and less time for ordering, not maximum crystal growth.
- c) Cooling a thermoplastic does not create covalent crosslinks between chains.
- d) Ignores microstructure and chain orientation: oriented and crystalline thermoplastics are dramatically stronger than quenched isotropic ones.

### Source

Problems T9_Polymers.pdf, Problem 3; Session 19, Slides 26, 38–39 and 43.

## Q86.9 Nonlinear elastic deformation of elastomers

- id: B86-Q9
- concept_id: u9-elastomer-uncoiling-curve
- format: cause-effect
- asks: cause

In a tensile test of an elastomer, virtually all deformation is elastic, yet the modulus of elasticity (slope) increases markedly at large strains because:

a) spherulites nucleate rapidly under tension and crystallize the rubber permanently
b) metallic-like dislocation tangling raises the yield stress after $100\%$ elongation
c) viscous flow increases the cross-sectional area while the tensile load stays constant
d) chains uncoil easily at low strain, then stretch covalent backbone bonds at high strain

### Answer

d

### Explanation

Session 19, Slide 44: an elastomer's stress–strain curve is nonlinear despite being almost completely elastic. At low strain, kinked chains between sparse crosslinks uncoil easily with little force (low slope); once straightened at several hundred percent strain, further extension must stretch primary covalent bonds along the chain, causing the modulus to rise steeply.

- a) Elastomers are amorphous networks, not spherulitic semicrystalline plastics.
- b) Dislocation glide and tangling govern crystalline metals, not rubber networks.
- c) Tensile elongation *reduces* cross-sectional area and sparse crosslinks prevent permanent viscous flow.

### Source

Session 19, Slide 44.

## Q86.10 Initial elastic modulus from linear polymer stress-strain data

- id: B86-Q10
- concept_id: u9-ss-elastic-modulus-calc
- format: numeric
- asks: calculation
- calc: 24e6 / 0.012 / 1e9
- check: 0.007 <= (24e6 / 0.012 / 1e9) <= 4.0

In the initial linear elastic region of a tensile test, a rigid thermoplastic specimen sustains a tensile stress of $24\text{ MPa}$ at a reversible strain of $\varepsilon = 0.012$. What is its modulus of elasticity $E$?

a) $2.0\text{ GPa}$
b) $0.29\text{ GPa}$
c) $20.0\text{ GPa}$
d) $0.050\text{ GPa}$

### Answer

a

### Explanation

Session 19, Slides 32 and 35: in the linear elastic region where Hooke's law holds, $E = \sigma / \varepsilon = 24\text{ MPa} / 0.012 = 2000\text{ MPa} = 2.0\text{ GPa}$, which falls squarely inside the $0.007\text{–}4\text{ GPa}$ range typical of polymers.

- b) Multiplied stress by strain ($24\text{ MPa} \times 0.012 = 0.288\text{ MPa}$, misread as $\text{GPa}$) instead of dividing $\sigma / \varepsilon$.
- c) Misplaced a factor of 10 in converting $2000\text{ MPa}$ to $\text{GPa}$ ($2000\text{ MPa} = 2.0\text{ GPa}$, not $20.0\text{ GPa}$).
- d) Inverted Hooke's law as $\varepsilon / \sigma$ ($0.012 / 24 = 5.0\times 10^{-4}\text{ MPa}^{-1}$, scaled by 100).

### Source

Session 19, Slides 32 and 35.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]] · [[Aerospace Materials I MOC]]
