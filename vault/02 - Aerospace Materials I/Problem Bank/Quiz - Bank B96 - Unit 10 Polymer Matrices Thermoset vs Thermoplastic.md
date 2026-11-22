---
materia: Aerospace Materials I
tema: "Unit 10: why polymer matrices dominate aerospace composites, certification pyramid, thermosets (epoxy, BMI, polyimide, polyester, phenolic) vs thermoplastics (PEEK, PPS, PSF, PES, PI, PEI) and resin additives"
bank_id: B96
title: "Polymer matrices: thermosets vs thermoplastics"
category: mt3_test_block
unit: 10
concepts:
  - u10-thermoset-matrix-pmc-pros-cons
  - u10-thermoset-matrix-certification
  - u10-thermoset-matrix-vs-tp-chem
  - u10-thermoset-matrix-epoxy
  - u10-thermoset-matrix-bmi-pi
  - u10-thermoset-matrix-tg-ordering
  - u10-thermoset-matrix-toughening
  - u10-thermoset-matrix-additives
  - u10-thermoset-matrix-tp-shelf-strain
  - u10-thermoset-matrix-tp-crystallinity
difficulty: 2
origen: "Practice items written for the bank in the style of Part I of MATERIALS_THIRDPARTIAL_2020.pdf; not official exercises. Content and data from Session 22 Slides 1-15."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-10
---

# Bank B96 — Polymer matrices: thermosets vs thermoplastics

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test III (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 22, Slides 1–15 (advantages and disadvantages of PMCs, certification pyramid, thermosetting and thermoplastic matrices, resin additives and toughening).

## Q96.1 Advantages and disadvantages of polymer-matrix composites

- id: B96-Q1
- concept_id: u10-thermoset-matrix-pmc-pros-cons
- format: topic-false
- asks: classification

Regarding the advantages and disadvantages of advanced polymer-matrix composites (PMCs) in aerospace structures, which one of the following statements is FALSE:

a) Advantages include high specific mechanical performance, good fatigue performance, low weight, corrosion immunity and part-count reduction
b) Disadvantages include high material and equipment costs, water entry in sandwich panels, low impact resistance and low recyclability
c) Because carbon/epoxy PMCs exhibit higher thermal and electrical conductivity than aluminium, they eliminate the need for lightning-strike protection
d) Advanced PMCs require costly qualification programmes and additional surface protection against rain or particle erosion

### Answer

c

### Explanation

Session 22, Slides 2–3: polymer-matrix composites have **low** thermal conductivity and low electrical conductivity relative to aluminium skins, so aircraft composite structures explicitly require additional protection against lightning strikes as well as against erosion.

- a) True (Slide 2): lists core PMC advantages including specific performance, fatigue resistance, no corrosion and part integration.
- b) True (Slide 3): lists key PMC limitations including high capital/material cost, sandwich water ingress, low impact tolerance and poor recyclability.
- d) True (Slide 3): costly evaluation/certification programmes and added erosion protection are explicit PMC disadvantages.

### Source

Session 22, Slides 2–3.

## Q96.2 Building-block certification pyramid

- id: B96-Q2
- concept_id: u10-thermoset-matrix-certification
- format: diagram-reading
- asks: application

The qualification and certification pyramid for aerospace composite structures is shown below. How does this building-block hierarchy explain the high evaluation cost of PMCs?

![[attachments/T10/s22-certification-pyramid.png]]

a) Only full-scale aircraft components at the apex require testing, avoiding coupon-level mechanical tests
b) Extensive material qualification tests on coupons and details at the base must progress sequentially through elements, sub-components and full-scale components for aircraft certification
c) Coupon tests are performed after final aircraft flight certification solely to verify recyclability
d) Coupons evaluate aerodynamic drag whereas components measure polymer glass transition temperature

### Answer

b

### Explanation

Session 22, Slide 3: the certification pyramid starts at the broad base with material qualification (coupons and details) and narrows upward through aircraft certification (elements, sub-components and full-scale structural components), requiring large numbers of tests at multiple scales and driving high qualification cost.

- a) Contradicts the diagram base: thousands of coupons and structural details must be qualified before building up to elements and components.
- c) Reverses the temporal sequence: material qualification precedes aircraft certification.
- d) Misstates what coupons test: the coupon sketches show tensile, shear, bolted-joint and bending mechanical tests, not aerodynamics.

### Source

Session 22, Slide 3.

## Q96.3 Thermosetting vs thermoplastic polymer matrices

- id: B96-Q3
- concept_id: u10-thermoset-matrix-vs-tp-chem
- format: topic-true
- asks: comparison

Referring to the fundamental contrast between thermosetting and thermoplastic composite matrices, which one of the following statements is TRUE:

a) Thermosets undergo an irreversible chemical crosslinking reaction during curing and offer low pre-cure viscosity for good fibre wetting, whereas thermoplastics consolidate reversibly without curing from high-viscosity melts
b) Thermoplastics form dense covalent crosslinks during cooling, making them insoluble and impossible to post-form
c) Thermosets have unlimited storage shelf life at room temperature because no chemical reaction occurs until $400\ ^\circ\text{C}$
d) Thermoplastic melts have much lower viscosity than liquid uncured epoxies, eliminating shearing forces on fibres during moulding

### Answer

a

### Explanation

Session 22, Slides 4–5: thermosets are cross-linked polymers whose processing is irreversible and cured via chemical reaction (1–2 h), giving low pre-cure viscosity and good fibre wetting; thermoplastics are uncrosslinked, non-reacting and reversibly consolidated by heat and pressure ($300\text{–}400\ ^\circ\text{C}$), with very high melt viscosities.

- b) Attributes thermoset crosslinking and irreversibility to thermoplastics.
- c) Inverts shelf life (Slide 4–5): thermosets have low/restricted storage life (requiring refrigeration for prepregs), while thermoplastics have unlimited shelf life at room temperature.
- d) Inverts viscosity (Slide 4): thermoplastics have *very high* melt viscosities requiring high pressure and shear forces that risk reinforcement damage.

### Source

Session 22, Slides 4–5.

## Q96.4 Epoxy as the dominant structural thermoset matrix

- id: B96-Q4
- concept_id: u10-thermoset-matrix-epoxy
- format: identify
- asks: application

Which thermosetting resin family dominates structural aerospace composites because it combines low curing shrinkage, a wide viscosity window for fibre wetting, good mechanical properties up to $60\text{–}150\ ^\circ\text{C}$ and excellent adhesion to most fibres?

a) Unsaturated polyester
b) Phenolic resin
c) Condensation polyimide (PMR-15)
d) Epoxy resin

### Answer

d

### Explanation

Session 22, Slides 8, 10 and 11: epoxy resins (such as Hexcel 920 or Hercules 3501, cured at $120\ ^\circ\text{C}$ or $180\ ^\circ\text{C}$) are the most widely used matrices in structural aerospace composites thanks to low shrinkage, good fibre adhesion, easy wetting and balanced mechanical properties.

- a) Polyesters show lower modulus ($1.3\text{–}4.5\text{ GPa}$), higher thermal expansion ($100\text{–}200 \times 10^{-6}\text{ K}^{-1}$) and lower aerospace structural share than epoxies (Slide 11).
- b) Phenolics are primarily selected for FST/interior fire-retardant uses rather than primary structural matrices.
- c) Condensation polyimides (PMR-15) are far more expensive and difficult to process, reserved for extended high-temperature service up to $\sim 230\text{–}320\ ^\circ\text{C}$ (Slides 8 and 10).

### Source

Session 22, Slides 8, 10 and 11.

## Q96.5 Bismaleimides (BMI) and polyimides (PI)

- id: B96-Q5
- concept_id: u10-thermoset-matrix-bmi-pi
- format: false-statement
- asks: comparison

Which of the following statements about high-temperature thermosetting matrices—bismaleimides (BMIs) and polyimides (PIs)—is FALSE:

a) Untoughened BMIs exhibit $T_g$ around $275\text{–}300\ ^\circ\text{C}$ and higher service temperature capability ($\sim 230\text{–}250\ ^\circ\text{C}$) than standard epoxies, typically requiring post-cure
b) BMIs exhibit higher fracture toughness than standard epoxies and remain immune to microcracking during thermal cycling or prolonged high-temperature exposure
c) Thermosetting polyimides such as PMR-15 extend service capability above epoxy and BMI temperatures, but have low toughness and are difficult to process
d) Polyimides generally absorb more moisture ($4\text{–}4.5\%$) and cost more than standard structural epoxy resins

### Answer

b

### Explanation

Session 22, Slides 9–10: BMIs are explicitly **even less tough than epoxies**, undergo curing shrinkage, and are **prone to microcracking** during prolonged exposure to high temperatures or thermal cycling (while toughened BMI Cytec 5250-4 improves damage resistance at the expense of lowering max wet capability from $230$ to $180\ ^\circ\text{C}$).

- a) True (Slides 9–10): BMIs have $T_g = 275\text{–}300\ ^\circ\text{C}$, operate around $230\text{–}250\ ^\circ\text{C}$ and need post-cure for optimum properties.
- c) True (Slides 8 and 10): PMR-15 condensation polyimide reaches $320\ ^\circ\text{C}$ max capability with oxidation resistance, low toughness and difficult processing.
- d) True (Slides 8 and 11): PIs are more expensive and exhibit higher water absorption ($4\text{–}4.5\%$) and lower stiffness than many epoxies.

### Source

Session 22, Slides 8–11.

## Q96.6 Glass transition temperature ranking of thermosets

- id: B96-Q6
- concept_id: u10-thermoset-matrix-tg-ordering
- format: ordering
- asks: comparison

Order the three aerospace thermosetting matrix families by increasing glass transition temperature ($T_g$):

a) Polyimides $<$ Bismaleimides $<$ Epoxies
b) Bismaleimides $<$ Epoxies $<$ Polyimides
c) Epoxies ($120\text{–}190\ ^\circ\text{C}$) $<$ Bismaleimides ($275\text{–}300\ ^\circ\text{C}$) $<$ Polyimides ($300\text{–}350\ ^\circ\text{C}$)
d) Epoxies $<$ Polyimides $<$ Bismaleimides

### Answer

c

### Explanation

Session 22, Slide 11: the property table reports $T_g = 120\text{–}190\ ^\circ\text{C}$ for epoxies, $275\text{–}300\ ^\circ\text{C}$ for bismaleimides and $300\text{–}350\ ^\circ\text{C}$ for polyimides, matching their progressive use at higher service temperatures.

- a) Reverses the ranking from highest to lowest $T_g$.
- b) Swaps epoxies above bismaleimides, ignoring BMI's higher aromatic/imide crosslink density.
- d) Swaps polyimides below bismaleimides ($300\text{–}350\ ^\circ\text{C}$ vs $275\text{–}300\ ^\circ\text{C}$).

### Source

Session 22, Slide 11.

## Q96.7 Toughening agents in thermosetting resins

- id: B96-Q7
- concept_id: u10-thermoset-matrix-toughening
- format: identify
- asks: classification

Which type of resin additive precipitates during curing as fine particles—via either a dispersed thermoplastic polymer such as polyethersulphone (PES) or an in-situ CTBN rubber dispersion—to modify crack propagation in brittle thermosets?

a) Toughening agents
b) Volatile solvents
c) Inert hollow glass spheres
d) Plasticizers

### Answer

a

### Explanation

Session 22, Slide 12: toughening agents precipitate from the reacting resin during curing as fine dispersed particles that alter crack propagation and improve toughness, achieved via either pre-formulated thermoplastic dispersions (such as polyethersulphone, PES) or in-situ rubber dispersions (carboxyl- or amine-terminated CTBN rubbers).

- b) Solvents are added strictly to reduce pre-cure resin viscosity for handling and fibre wet-out, then evaporated before full cure.
- c) Inert fillers (including hollow spheres) modify density, resin flow, cost and effective modulus without acting via CTBN/PES precipitation toughening.
- d) Plasticizers lower elastic modulus and raise elongation to failure by spacing chains rather than precipitating discrete CTBN or PES particles.

### Source

Session 22, Slide 12.

## Q96.8 Roles of solvents, plasticizers and inert fillers

- id: B96-Q8
- concept_id: u10-thermoset-matrix-additives
- format: cause-effect
- asks: effect

In thermosetting matrix formulation, adding inert fillers (such as hollow glass spheres) instead of volatile solvents or plasticizers primarily alters:

a) pre-cure viscosity solely to aid hand wet-out before evaporating during drying
b) covalent crosslink density by doubling the stoichiometric hardener ratio
c) longitudinal tensile strength of carbon fibres by etching graphitic planes
d) composite density, resin flow, cost and effective modulus

### Answer

d

### Explanation

Session 22, Slide 12: inert fillers (including hollow spheres) are added to alter composite density, resin flow, manufacturing cost and effective modulus, whereas solvents reduce viscosity before curing and plasticizers reduce elastic modulus while increasing elongation to failure.

- a) Describes volatile solvents used to lower viscosity prior to curing, not permanent inert fillers.
- b) Inert fillers do not participate chemically in stoichiometric crosslinking.
- c) Matrix fillers reside in the polymer resin and do not chemically etch reinforcing carbon filaments.

### Source

Session 22, Slide 12.

## Q96.9 Advantages and limitations of thermoplastic matrices

- id: B96-Q9
- concept_id: u10-thermoset-matrix-tp-shelf-strain
- format: topic-false
- asks: comparison

Regarding thermoplastic matrices (such as PEEK, PPS and PEI) used to substitute thermosets in aerospace composites, which one of the following statements is FALSE:

a) They offer unlimited shelf life at room temperature, high fracture strain ($30\text{–}100\%$), good fire/smoke/toxicity (FST) behaviour and recyclability
b) They require freezer storage at $-18\ ^\circ\text{C}$ to halt curing reactions and exhibit lower fracture strain than untoughened epoxies
c) They suffer from high raw-material cost and require high processing temperatures ($300\text{–}400\ ^\circ\text{C}$) and high pressures
d) They show lower resistance to some organic solvents than thermosets and can be prone to creep under sustained load

### Answer

b

### Explanation

Session 22, Slides 4–5 and 13: thermoplastic matrices undergo **no** curing reaction, so they have **unlimited shelf life at room temperature** (no $-18\ ^\circ\text{C}$ storage needed) and much **higher** toughness and strain at fracture ($30\text{–}100\%$) than brittle thermosets.

- a) True (Slide 13): lists room-temperature storage, unlimited shelf life, $30\text{–}100\%$ fracture strain, good FST behaviour and reprocessability.
- c) True (Slides 5, 13 and 15): process temperatures of $340\text{–}400\ ^\circ\text{C}$ and high pressure drive up manufacturing cost.
- d) True (Slide 5): thermoplastic disadvantages explicitly include lower resistance to organic solvents in some cases and creep proneness.

### Source

Session 22, Slides 4–5, 13 and 15.

## Q96.10 Amorphous vs semicrystalline thermoplastic matrices

- id: B96-Q10
- concept_id: u10-thermoset-matrix-tp-crystallinity
- format: true-statement
- asks: classification

Which of the following statements contrasting amorphous and semicrystalline thermoplastic matrices is TRUE:

a) Amorphous thermoplastics such as PEI have higher resistance to aggressive aerospace fluids than semicrystalline PEEK
b) PEEK ($T_g = 145\ ^\circ\text{C}$) and PPS ($T_g = 90\ ^\circ\text{C}$) are amorphous matrices processed near room temperature with wide cooling-rate tolerance
c) Semicrystalline thermoplastics such as PEEK and PPS resist aggressive fluids well, but require tight control of cooling rate because it sets their crystallinity
d) Polysulphone (PSF) and polyethersulphone (PES) are heavily crosslinked thermosets that cannot soften upon heating

### Answer

c

### Explanation

Session 22, Slides 14–15: semicrystalline thermoplastics (PEEK, PPS) possess high molecular order and very good resistance to aggressive fluids, but have a critical processing window—especially cooling rate, which determines crystallinity and mechanical behaviour; amorphous thermoplastics (such as PEI) rely on entanglements, have a wide processing window and show low resistance to aggressive fluids.

- a) Inverts fluid resistance: semicrystalline PEEK and PPS resist aggressive fluids much better than amorphous PEI (Slide 14).
- b) Misclassifies PEEK and PPS as amorphous (they are semicrystalline) and ignores their $340\text{–}400\ ^\circ\text{C}$ processing temperatures (Slide 15).
- d) Misclassifies PSF and PES (listed under thermoplastic matrix materials on Slides 14–15) as thermosets.

### Source

Session 22, Slides 14–15.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
