---
materia: Aerospace Materials I
tema: "Unit 10: ceramic matrix composites (SiC, Al2O3, Si3N4, C-C, ZrB2/HfB2), toughening via debonding, crack deflection, crack bridging and fibre pull-out raising K_IC, and CMC processing (sol-gel, PIP, slurry, liquid-state limits)"
bank_id: B103
title: "Ceramic matrix composites and toughening"
category: mt3_test_block
unit: 10
concepts:
  - u10-cmc-matrices-advantages
  - u10-cmc-toughening-role
  - u10-cmc-kic-bar-chart
  - u10-cmc-interface-debonding
  - u10-cmc-pullout-micrograph
  - u10-cmc-unique-processing
  - u10-cmc-melt-infiltration-limit
  - u10-cmc-solgel-pip-cycles
  - u10-cmc-slurry-steps
  - u10-cmc-temperature-ranking
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_THIRDPARTIAL_2020.pdf, including Q5 of MATERIALS_FINALEXAM_2015_EXTRA.pdf. Content from Session 22 Slide 29 and Session 23 Slides 38-45."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-10
---

# Bank B103 — Ceramic matrix composites and toughening

> [!info] Includes official exam questions
> Ten test questions written for the bank in the style of Part I of Assessment Test III, including adaptations of Q5 from the June 2015 extraordinary final exam (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 22, Slide 29; Session 23, Slides 38-45.

## Q103.1 Typical matrices and advantages of CMCs

- id: B103-Q1
- concept_id: u10-cmc-matrices-advantages
- format: topic-true
- asks: classification
- origin: official-exam

Referring to ceramic matrix composites (CMCs), which one of the following statements is TRUE:

a) Typical CMC matrices are epoxy and bismaleimide resins, chosen to permit room-temperature vacuum bagging
b) Typical CMC matrices include silica glass, SiC, $\text{Si}_3\text{N}_4$, $\text{Al}_2\text{O}_3$, and carbon, delivering high fracture toughness, low density, and oxidation stability at extreme temperatures
c) CMCs exhibit higher density than nickel-based superalloys and lower maximum operating temperatures than aluminium alloys
d) CMCs are produced by inexpensive, rapid injection moulding so their main advantage over PMCs is low manufacturing cost

### Answer

b

### Explanation

June 2015 extraordinary final exam, Q5a-b (and Session 23, Slides 38-41): common CMC matrices are silica-based glass, silicon carbide (SiC), silicon nitride ($\text{Si}_3\text{N}_4$), alumina ($\text{Al}_2\text{O}_3$), carbon, and ultra-high-temperature borides ($\text{ZrB}_2$, $\text{HfB}_2$). Their key advantages are high fracture toughness (crack resistance), low density, high specific strength and stiffness, oxidation stability at high temperature, wear resistance, and survival under extreme thermal conditions (above Ni superalloys).

- a) Epoxy and BMI are thermosetting *polymer* matrices (Session 22, Slide 7), not ceramic matrices.
- c) Inverts both properties: CMCs are much lighter than Ni superalloys and operate around $1200\text{–}2000\,^\circ\text{C}+$, far above Al alloys and superalloys (Slide 41).
- d) Contradicts Slide 38: costly, complex, and limited fabrication techniques are the primary disadvantage of CMCs.

### Source

MATERIALS_FINALEXAM_2015_EXTRA.pdf, p. 7 Q5a-b; Session 23, Slides 38-41.

## Q103.2 Purpose of fibres in CMCs vs PMCs

- id: B103-Q2
- concept_id: u10-cmc-toughening-role
- format: cause-effect
- asks: cause
- origin: official-exam

Unlike polymer matrix composites—where fibres mainly stiffen and strengthen a soft, ductile matrix—why are continuous ceramic or carbon fibres introduced into a ceramic matrix?

a) To lower the elastic modulus and make the ceramic matrix deform plastically like an elastomer
b) To dissolve into the ceramic lattice and convert covalent bonds into metallic bonds
c) To lower the melting temperature of the ceramic matrix below $200\,^\circ\text{C}$ for easy casting
d) To increase fracture toughness by absorbing fracture energy through interfacial debonding, crack deflection, crack bridging, and fibre pull-out

### Answer

d

### Explanation

June 2015 extraordinary final exam, Q5c (and Session 23, Slide 38; Session 22, Slide 29): monolithic ceramics already possess high stiffness and compressive strength, but fail catastrophically from low fracture toughness $K_{IC}$. Reinforcements in CMCs raise $K_{IC}$ by absorbing energy as an advancing crack debonds and deflects along the fibre-matrix interface, leaves intact fibres bridging the crack wake (**crack bridging**), and pulls broken fibres out against friction (**fibre pull-out**).

- a) Ceramic fibres do not impart elastomeric compliance or metal-like dislocation plasticity to a ceramic matrix.
- b) Composite phases stay chemically distinct across an interface (Session 21, Slide 2) and never turn ceramic bonds metallic.
- c) Refractory capability is an essential virtue of CMCs; fibres do not depress matrix melting temperatures to $200\,^\circ\text{C}$.

### Source

MATERIALS_FINALEXAM_2015_EXTRA.pdf, p. 7 Q5c; Session 23, Slide 38; Session 22, Slide 29.

## Q103.3 Fracture toughness gain shown on the K_IC bar chart

- id: B103-Q3
- concept_id: u10-cmc-kic-bar-chart
- format: diagram-reading
- asks: figure-reading

From the bar chart comparing plane-strain fracture toughness $K_{IC}$ of unreinforced ceramics and ceramic matrix composites, approximately how much higher is $K_{IC}$ in SiC/SiC than in monolithic SiC?

![[attachments/T10/s22-kic-ceramic-composites.png]]

a) Roughly five to six times higher (rising from about $4\text{–}5\text{ MPa}\sqrt{\text{m}}$ to about $25\text{ MPa}\sqrt{\text{m}}$)
b) Roughly half as large (dropping from about $25\text{ MPa}\sqrt{\text{m}}$ to about $12\text{ MPa}\sqrt{\text{m}}$)
c) Practically unchanged (staying near $5\text{ MPa}\sqrt{\text{m}}$ for both monolithic SiC and SiC/SiC)
d) Lower than unreinforced $\text{Si}_3\text{N}_4$, which shows the tallest bar at $25\text{ MPa}\sqrt{\text{m}}$

### Answer

a

### Explanation

Session 22, Slide 29: reading the bar chart, unreinforced $\text{Al}_2\text{O}_3$, SiC, and $\text{Si}_3\text{N}_4$ sit between roughly $3$ and $5\text{ MPa}\sqrt{\text{m}}$, whereas $\text{SiC}/\text{Al}_2\text{O}_3$ reaches $\sim 8\text{ MPa}\sqrt{\text{m}}$, $\text{SiC}/\text{Si}_3\text{N}_4$ reaches $\sim 20\text{ MPa}\sqrt{\text{m}}$, and $\text{SiC}/\text{SiC}$ reaches $\sim 25\text{ MPa}\sqrt{\text{m}}$—a five- to six-fold increase over unreinforced SiC.

- b) Inverts the comparison between monolithic ceramics and toughened CMCs.
- c) Ignores the large jump from the left unreinforced bars ($\le 5\text{ MPa}\sqrt{\text{m}}$) to the right CMC bars ($8\text{–}25\text{ MPa}\sqrt{\text{m}}$).
- d) Misreads the bars: unreinforced $\text{Si}_3\text{N}_4$ is the shortest bar ($\sim 3\text{ MPa}\sqrt{\text{m}}$), whereas $\text{SiC}/\text{SiC}$ is the tallest ($\sim 25\text{ MPa}\sqrt{\text{m}}$).

### Source

Session 22, Slide 29.

## Q103.4 Role of controlled interfacial bonding in CMCs

- id: B103-Q4
- concept_id: u10-cmc-interface-debonding
- format: what-happens
- asks: effect

In a continuous-fibre CMC, what happens if the chemical bond at the fibre-matrix interface is made excessively strong without a compliant debonding coating?

a) Crack bridging and fibre pull-out become even longer because stronger bonds slide farther under tension
b) The composite becomes superplastic at room temperature as cracks turn into dislocation glide planes
c) An advancing matrix crack cuts straight through the fibres without deflecting or debonding, causing brittle catastrophic fracture
d) The matrix transforms into an amorphous glass that self-heals cracks at ambient temperature

### Answer

c

### Explanation

Session 21, Slide 3, Session 22, Slide 18, and Session 23, Slide 38: toughness in CMCs relies on controlled bond strength so that an approaching matrix crack tip can debond and deflect along the interface rather than snapping the intact fibre in the same plane. When the interface is overly strong, the crack propagates straight across the fibres, eliminating crack bridging and fibre pull-out and restoring monolithic brittleness.

- a) Stronger interfacial bonding *prevents* sliding and pull-out, forcing fibres to break flush on the matrix crack plane.
- b) Ceramic phases lack room-temperature dislocation glide regardless of interface strength.
- d) Interface chemistry does not convert crystalline SiC or $\text{Al}_2\text{O}_3$ into a self-healing room-temperature glass.

### Source

Session 21, Slide 3; Session 22, Slide 18; Session 23, Slide 38.

## Q103.5 Microstructural evidence of fibre pull-out on CMC fracture surfaces

- id: B103-Q5
- concept_id: u10-cmc-pullout-micrograph
- format: true-statement
- asks: comparison

Which of the following statements is TRUE regarding the fracture surface of a tough $\text{SiC}_f/\text{SiC}$ ceramic matrix composite compared with a monolithic SiC ceramic:

a) Both fracture surfaces appear flat and mirror-smooth because SiC fibres and SiC matrix share identical chemistry
b) The CMC fracture surface shows long protruding fibres and fibre bundles pulled out of matrix sockets, evidencing frictional energy dissipation
c) The CMC fracture surface exhibits dimpled cup-and-cone necking typical of ductile FCC metals
d) Protruding fibres on the fracture surface indicate zero interfacial load transfer and prove the composite is weaker than monolithic SiC

### Answer

b

### Explanation

Session 23, Slide 38: the SEM fractograph of a SiC fibre / SiC matrix composite shows long bundles of intact fibres extending out of the stepped matrix fracture surface. This direct visual signature of **fibre pull-out** (alongside crack bridging) shows that fibres broke away from the crack plane and slid out against interfacial friction, absorbing substantial fracture energy.

- a) A flat, planar fracture belongs to untoughened monolithic ceramics or over-bonded CMCs lacking pull-out, not tough $\text{SiC}/\text{SiC}$.
- c) Microvoid coalescence and cup-and-cone necking characterize ductile metals, not brittle ceramic fibres sliding out of a ceramic matrix.
- d) Pull-out requires sufficient shear friction along the debonded interface to dissipate fracture work and raise $K_{IC}$ severalfold (Session 22, Slide 29).

### Source

Session 23, Slide 38; Session 22, Slide 29.

## Q103.6 Manufacturing methods tailored specifically to CMCs

- id: B103-Q6
- concept_id: u10-cmc-unique-processing
- format: identify
- asks: classification
- origin: official-exam

Which manufacturing route is specifically tailored to ceramic matrix composites to form a refractory matrix inside a fibre preform without melting high-$T_m$ ceramics?

a) Autoclave curing of B-stage epoxy prepreg tapes at $180\,^\circ\text{C}$ and $700\text{ kPa}$
b) Rheocasting by stirring ceramic particles into a semi-solid aluminium mushy zone
c) Compression moulding of chopped glass-fibre polyester Sheet Moulding Compound (SMC)
d) Infiltrating a ceramic fibre preform with a sol-gel or preceramic polymer followed by drying and pyrolysis at $800\text{–}1300\,^\circ\text{C}$ (repeated over several cycles)

### Answer

d

### Explanation

June 2015 extraordinary final exam, Q5d (and Session 23, Slides 42-45): CMCs cannot be cured like epoxies or easily pressure-infiltrated as molten ceramics. Dedicated CMC routes include **preform infiltration** via sol-gel or **preceramic polymer infiltration and pyrolysis (PIP)** (800-1300 °C, repeated 4-10 times to fill shrinkage voids), **slurry processing** with binder burnout and hot pressing, as well as vapour-phase chemical vapour infiltration (CVI) and reactive liquid silicon infiltration (extension).

- a) Produces thermoset polymer matrix composites (PMCs), not ceramic matrix composites (Slides 25-26).
- b) Produces metal matrix composites (MMCs) such as particulate aluminium alloys (Slide 36).
- c) Produces chopped-fibre PMC components, not continuous-fibre CMCs (Slides 7 and 11).

### Source

MATERIALS_FINALEXAM_2015_EXTRA.pdf, p. 7 Q5d; Session 23, Slides 42-45.

## Q103.7 Why liquid-state melt infiltration and powder pressing struggle in CMCs

- id: B103-Q7
- concept_id: u10-cmc-melt-infiltration-limit
- format: false-statement
- asks: cause

Which of the following statements about limitations in CMC processing is FALSE:

a) Liquid-state infiltration of molten ceramic into a fibre preform is the easiest CMC route because molten ceramics have ultra-low viscosity and never react with fibres
b) In conventional powder mixing and pressing of CMCs, achieving uniform reinforcement distribution is difficult and pressing damages whiskers
c) Conventional mixing and sintering of ceramic powders with whiskers typically yields only a low reinforcement volume fraction
d) Liquid-state pressure infiltration has limited success in CMCs because high ceramic melting temperatures promote fibre-matrix reaction and high melt viscosity slows infiltration

### Answer

a

### Explanation

Session 23, Slide 43: liquid-state pressure infiltration (widely used for lower-melting MMCs) has *limited success* in CMCs specifically because ceramics have extremely high melting temperatures—causing severe chemical reactions that damage the fibres—and high melt viscosities that produce very slow infiltration rates. Statement a is false.

- b) True: Slide 43 notes non-uniform mixing and whisker damage during mixing and pressing in the conventional powder route.
- c) True: conventional mixing/pressing/firing limits achievable reinforcement volume fraction (Slide 43).
- d) True: Slide 43 explicitly lists both high $T_m$ (reaction between matrix and reinforcement) and high viscosity (low infiltration rate).

### Source

Session 23, Slide 43.

## Q103.8 Repeating sol-gel and preceramic polymer infiltration cycles

- id: B103-Q8
- concept_id: u10-cmc-solgel-pip-cycles
- format: diagram-reading
- asks: figure-reading

In the preform infiltration routes shown (sol-gel and preceramic polymer infiltration followed by pyrolysis at $800\text{–}1300\,^\circ\text{C}$), why must infiltration, drying/curing, and pyrolysis be repeated 4 to 10 times?

![[attachments/T10/s23-sol-gel-infiltration-cycle.png]]

a) Each pyrolysis cycle converts the ceramic matrix back into a liquid polymer that leaks out of the die
b) Each cycle strips away one layer of reinforcing fibres to keep the final part thin
c) Drying and pyrolysis cause large volume shrinkage and gas release, leaving pores that must be refilled in successive cycles to achieve high density
d) Repeating the cycle lowers the matrix melting temperature so the composite can later be thermoformed

### Answer

c

### Explanation

Session 23, Slide 44: whether starting from a colloidal sol or a liquid preceramic polymer (PIP), converting the precursor into a ceramic during drying/gelation and pyrolysis ($800\text{–}1300\,^\circ\text{C}$) releases volatile gases and causes large shrinkage, leaving a porous matrix. Repeating infiltration, drying, and pyrolysis 4 to 10 times progressively fills those pores until target density is reached (a densification logic shared with gas-phase CVI, extension).

- a) Pyrolysis irreversibly converts the preceramic polymer or gel *into* a solid ceramic matrix rather than reversing it to liquid polymer.
- b) Fibres remain intact throughout the cycles; only additional matrix precursor is added into open porosity.
- d) Ceramic matrices are refractory and non-thermoformable; cycles aim to eliminate porosity, not lower melting points.

### Source

Session 23, Slide 44.

## Q103.9 Slurry processing steps for fibre-reinforced CMCs

- id: B103-Q9
- concept_id: u10-cmc-slurry-steps
- format: ordering
- asks: application

Which option gives the correct sequence of steps in the slurry processing route for fibre-reinforced CMCs?

a) Hot pressing in a graphite die ($800\text{–}925\,^\circ\text{C}$) $\to$ passing fibres through matrix slurry tank $\to$ stacking tapes $\to$ binder burnout at $500\,^\circ\text{C}$
b) Passing fibres through a matrix slurry tank $\to$ winding and stacking impregnated tapes $\to$ binder burnout at $500\,^\circ\text{C}$ $\to$ hot pressing in a graphite die ($800\text{–}925\,^\circ\text{C}$)
c) Binder burnout at $500\,^\circ\text{C}$ $\to$ passing fibres through a matrix slurry tank $\to$ hot pressing in a graphite die $\to$ winding impregnated tapes
d) Winding dry fibres on a mandrel $\to$ autoclave curing at $180\,^\circ\text{C}$ $\to$ binder burnout at $500\,^\circ\text{C}$ $\to$ passing through a slurry tank

### Answer

b

### Explanation

Session 23, Slide 45: in slurry processing, continuous fibres are drawn through a tank containing ceramic matrix powder suspended in a liquid slurry with binder, wound to form impregnated tapes, cut and stacked, heated to burn out the organic binder around $500\,^\circ\text{C}$, and finally consolidated by hot pressing inside a graphite die at $800\text{–}925\,^\circ\text{C}$.

- a) Places final hot pressing at the start before the slurry has even impregnated the fibres or the binder has been removed.
- c) Attempts binder burnout before the slurry and binder have been applied to the fibres, and places stacking after hot pressing.
- d) Inserts a polymer autoclave cure step and places slurry impregnation at the very end instead of the start.

### Source

Session 23, Slide 45.

## Q103.10 Ranking high-temperature aerospace materials and CMC families

- id: B103-Q10
- concept_id: u10-cmc-temperature-ranking
- format: ordering
- asks: comparison

Consider the maximum temperature capabilities of advanced high-temperature aerospace materials: carbon-carbon (C/C) composites and ultra-high-temperature ceramics ($\text{ZrB}_2$/$\text{HfB}_2$), nickel-based superalloys, $\text{SiC}/\text{SiC}$ CMCs, and $\text{C}/\text{SiC}$ CMCs. Ranked in INCREASING order of temperature capability, they follow:

a) Ni-based superalloys, $\text{SiC}/\text{SiC}$ CMCs, $\text{C}/\text{SiC}$ CMCs, C/C composites and UHTC borides
b) $\text{SiC}/\text{SiC}$ CMCs, Ni-based superalloys, $\text{C}/\text{SiC}$ CMCs, C/C composites and UHTC borides
c) C/C composites and UHTC borides, $\text{C}/\text{SiC}$ CMCs, $\text{SiC}/\text{SiC}$ CMCs, Ni-based superalloys
d) Ni-based superalloys, C/C composites and UHTC borides, $\text{SiC}/\text{SiC}$ CMCs, $\text{C}/\text{SiC}$ CMCs

### Answer

a

### Explanation

Session 23, Slides 39-41: on the temperature capability versus thermal conductivity map (Slide 41), Ni-based superalloys sit near $1000\,^\circ\text{C}$, $\text{SiC}/\text{SiC}$ CMCs operate near $1400\text{–}1500\,^\circ\text{C}$ (e.g., turbine vanes and seals), $\text{C}/\text{SiC}$ CMCs reach $\sim 1600\text{–}1700\,^\circ\text{C}$ (e.g., Vulcain rocket nozzle extensions), and C/C composites along with $\text{ZrB}_2/\text{HfB}_2$ UHTCs exceed $2000\,^\circ\text{C}$ (e.g., re-entry nose caps and brake discs).

- b) Places $\text{SiC}/\text{SiC}$ CMCs below Ni-based superalloys, overlooking why CMCs replace superalloys in hotter engine sections.
- c) Reverses the entire list, placing the highest-temperature materials first (decreasing order).
- d) Places C/C and UHTC borides below SiC-matrix CMCs despite their $> 2000\,^\circ\text{C}$ capability for re-entry nose cones.

### Source

Session 23, Slides 39-41.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
