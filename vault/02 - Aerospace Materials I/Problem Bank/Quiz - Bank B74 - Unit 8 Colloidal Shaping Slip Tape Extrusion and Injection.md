---
materia: Aerospace Materials I
tema: "Unit 8: colloidal stabilization, slip casting, pressure slip casting, tape casting (doctor blade), extrusion, injection moulding and ceramic additive manufacturing"
bank_id: B74
title: "Colloidal shaping, slip, tape, extrusion and injection"
category: mt3_test_block
unit: 8
concepts:
  - u8-shaping-injection-molding
  - u8-shaping-colloid-slip
  - u8-shaping-slip-casting
  - u8-shaping-tape-casting
  - u8-shaping-extrusion
  - u8-shaping-additive
difficulty: 2
origen: "Includes official exam items from MATERIALS_THIRDPARTIAL_2020.pdf (Model B, Q3) and MATERIALS_THIRDPARTIAL_2020_V2.pdf (Paper B, Q7); remaining items written for the bank in the style of Part I of Assessment Test III. Content from Session 18, Slides 9 and 14-22."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-8
---

# Bank B74 — Colloidal shaping, slip, tape, extrusion and injection

> [!info] Includes official exam questions
> Ten test questions in the style of Part I of Assessment Test III (four options, one right answer; +0.5 right, -0.15 wrong), including Q3 from the 2020 Model B exam and Q7 from the 2020 Paper B exam. Content: Session 18, Slides 9, 14-22 and 29.

## Q74.1 Ceramic processing and injection moulding

- id: B74-Q1
- concept_id: u8-shaping-injection-molding
- format: topic-true
- asks: classification
- origin: official-exam

Which of the following statements about ceramics is TRUE:

a) Slip casting can be used to form components with a high dimensional accuracy
b) Ceramic injection molding involves mixing a ceramic powder with a binder or wax
c) Sintering involves heating the ceramic compact above the melting point
d) The ceramic component after sintering is called a "green compact"

### Answer

b

### Explanation

`MATERIALS_THIRDPARTIAL_2020.pdf`, Model B Q3 (and Session 18, Slides 19 and 22): ceramic injection moulding begins by mixing ceramic powder with a polymeric binder or wax (plus additives) to form a flowable plastic feedstock.

- a) Inverts the capability of slip casting: Slide 15 explicitly lists "low dimensional accuracy" under the drawbacks of slip casting.
- c) Inverts the thermal condition of sintering: sintering takes place **below** the melting point via diffusion processes (Slide 25).
- d) Misnames the stages: the "green part" (green compact) is the shaped compact *before* binder/water removal and sintering, not after sintering (Slides 22-23).

### Source

MATERIALS_THIRDPARTIAL_2020.pdf, p. 1 (Model B, Q3); Session 18, Slides 15, 19, 22-23 and 25.

## Q74.2 Requirements for a stable colloidal slip

- id: B74-Q2
- concept_id: u8-shaping-colloid-slip
- format: topic-false
- asks: definition

Regarding colloidal ceramic suspensions (slips) used in wet shaping, which one of the following statements is FALSE:

a) A slip is a suspension of colloidal ceramic particles in an immiscible carrier liquid, typically water
b) Good slips require chemical inertness, low viscosity for smooth flow, and easy detachment from the mould
c) Stable colloidal suspensions prevent particle aggregation and sedimentation during storage and casting
d) High drying shrinkage and heavily flocculated, high-viscosity slurries are preferred to accelerate slip casting

### Answer

d

### Explanation

Session 18, Slide 14: a functional ceramic slip must be a **stable** (non-aggregating, non-sedimenting) suspension exhibiting optimum flowability (low viscosity), low-turbulence Newtonian flow, maximum solids density, mould detachment ability, and **low shrinkage during drying**. Statement d) is false.

- a) True: Slide 14 defines a slip as a suspension of colloidal ceramic particles in an immiscible liquid, generally water.
- b) True: chemical inertness, low viscosity, and detachment ability are explicitly listed among slip characteristics on Slide 14.
- c) True: the colloid stability diagram on Slide 14 contrasts stable dispersed particles against unstable aggregation and sedimentation.

### Source

Session 18, Slide 14.

## Q74.3 Capillary mechanism and drawbacks of slip casting

- id: B74-Q3
- concept_id: u8-shaping-slip-casting
- format: cause-effect
- asks: cause

Conventional slip casting in porous plaster or alabaster moulds excels at producing large, complex hollow shapes with low-cost equipment, yet its wall thickness is normally limited to about $10\ \text{mm}$ and its production rate is low because:

a) molten ceramic solidifies slowly against the hot steel walls of the plaster mould
b) uniaxial punches cannot compact powder evenly through depths exceeding $10\ \text{mm}$
c) carrier water must migrate by capillary suction through the deposited powder cake, slowing deposition as thickness grows
d) polymeric waxes must be thermally pyrolyzed inside the plaster mould before pouring out excess slip

### Answer

c

### Explanation

Session 18, Slides 15-16: in slip casting, the porous plaster mould extracts water by capillary action, depositing particles along the mould wall; as the deposited cake thickens, water flows through it much more slowly, limiting practical wall thickness to $\sim 10\ \text{mm}$ and slowing production (alongside low dimensional accuracy).

- a) Confuses cold aqueous slip casting in porous plaster with high-temperature metal casting.
- b) Confuses wet slip casting with dry uniaxial die pressing.
- d) Confuses aqueous colloidal slip casting with plastic injection moulding debinding (Slide 22).

### Source

Session 18, Slides 15-16.

## Q74.4 Pressure-assisted slip casting kinetics

- id: B74-Q4
- concept_id: u8-shaping-slip-casting
- format: diagram-reading
- asks: figure-reading

The plot below shows cast wall thickness versus casting time for $\text{SiC}$ slip casting under four applied pressures ($1.7$, $3.4$, $6.8$, and $10.2\ \text{MPa}$). Based on the curves, raising the applied pressure from $1.7\ \text{MPa}$ to $10.2\ \text{MPa}$ causes the time needed to reach an $8\ \text{mm}$ cast thickness to:

![[attachments/T8/s18-pressure-casting-thickness.png]]

a) double from roughly $20\ \text{s}$ to $40\ \text{s}$ because higher pressure compresses the plaster pores shut
b) remain constant near $110\ \text{s}$ because capillary suction in plaster is independent of pressure
c) drop only slightly from $150\ \text{s}$ to $130\ \text{s}$ while reducing wall reliability
d) drop dramatically from roughly $110\text{–}120\ \text{s}$ down to about $20\ \text{s}$, greatly speeding up casting

### Answer

d

### Explanation

Session 18, Slide 16: reading the four curves at a cast body thickness of $8\ \text{mm}$, the $1.7\ \text{MPa}$ curve reaches $8\ \text{mm}$ at roughly $110\text{–}120\ \text{s}$, the $3.4\ \text{MPa}$ curve near $65\ \text{s}$, the $6.8\ \text{MPa}$ curve near $32\ \text{s}$, and the $10.2\ \text{MPa}$ curve near $20\ \text{s}$. Applied pressure sharply reduces processing time and improves thickness reliability.

- a) Inverts the effect of pressure and misreads the leftmost ($10.2\ \text{MPa}$) curve for the lowest pressure.
- b) Ignores the wide separation among the four pressure curves on the horizontal time axis.
- c) Underestimates the speed-up by reading the $1.7\ \text{MPa}$ curve at $9.5\ \text{mm}$ and reverses the reliability benefit stated on Slide 16.

### Source

Session 18, Slide 16.

## Q74.5 Tape casting process definition

- id: B74-Q5
- concept_id: u8-shaping-tape-casting
- format: complete-sentence
- asks: definition
- origin: official-exam

For fabrication of ceramic layers, _______ process involves casting the slurry onto a flat moving carrier surface.

a) Tape casting
b) Slip casting
c) Ceramic injection moulding
d) Extrusion

### Answer

a

### Explanation

`MATERIALS_THIRDPARTIAL_2020_V2.pdf`, Paper B Q7 (and Session 18, Slide 18): in **tape casting** (doctor-blade process), a ceramic colloidal slip is cast onto a flat moving carrier film/belt beneath an adjustable blade to form thin continuous sheets or layers ($< 1.5\ \text{mm}$).

- b) Slip casting pours an aqueous slip into a stationary porous plaster mould rather than onto a flat moving carrier belt (Slide 15).
- c) Ceramic injection moulding forces a wax/polymer-bound plastic feedstock into a closed die cavity (Slide 22).
- d) Extrusion forces a stiff plastic feedstock through a shaping die to produce uniform profiles or tubes (Slide 20).

### Source

MATERIALS_THIRDPARTIAL_2020_V2.pdf, p. 5 (Paper B, Q7); Session 18, Slides 15, 18, 20 and 22.

## Q74.6 Applications and thickness range of tape casting

- id: B74-Q6
- concept_id: u8-shaping-tape-casting
- format: identify
- asks: application

Which ceramic component pair and thickness range are characteristic of continuous tape casting (doctor blade)?

a) Large bathroom sanitary ware and plant pots with walls thicker than $15\ \text{mm}$
b) Axisymmetric thermocouple refractory tubes with minimum section above $15\ \text{mm}$
c) Thin ceramic sheets ($< 1.5\ \text{mm}$) for multilayer capacitors and fuel-cell components
d) Spark-plug ceramic insulators formed inside thick rubber bags without binders

### Answer

c

### Explanation

Session 18, Slide 18: tape casting is a continuous wet shaping route with acceptable dimensional accuracy for ceramic layers thinner than $1.5\ \text{mm}$, typically used for multilayer ceramic capacitors (co-sintered with $\text{Ag}$, $\text{Au}$, or $\text{Cu}$ conductors) and fuel-cell components.

- a) Sanitary ware and plant pots belong to conventional slip casting in porous plaster moulds (Slide 15).
- b) Refractory tubes with smallest cross-section $> 15\ \text{mm}$ are produced by plastic extrusion (Slide 21).
- d) Spark-plug insulators formed inside rubber bags without binders belong to dry-bag cold isostatic pressing (Slide 13).

### Source

Session 18, Slides 13, 15, 18 and 21.

## Q74.7 Ceramic extrusion capabilities and limitations

- id: B74-Q7
- concept_id: u8-shaping-extrusion
- format: false-statement
- asks: application

Which one of the following statements about ceramic extrusion is FALSE:

a) Ceramic powder is mixed with a binder, wax, or thermoplastic and additives to obtain a plastic feedstock pushed through a die
b) Extrusion readily forms intricate three-dimensional turbine blades with abruptly varying cross-sections along their length
c) Extrusion achieves high production rates and high reproducibility for hollow or solid axisymmetric profiles of constant cross-section
d) Technical ceramics such as $\text{Al}_2\text{O}_3$, $\text{ZrO}_2$, $\text{Si}_3\text{N}_4$, and $\text{SiC}$ can be extruded into refractory tubes and catalyst supports

### Answer

b

### Explanation

Session 18, Slides 19-21: extrusion forces plastic feedstock continuously through a rigid die, so it is restricted to components with a **constant transverse cross-section** (such as tubes, bricks, and catalyst honeycombs); complex 3D net shapes with varying cross-sections require injection moulding or additive manufacturing. Statement b) is false.

- a) True: Slide 19 and Slide 20 describe compounding ceramic powder with binder/additives into feedstock forced by a ram, screw, or piston.
- c) True: Slide 21 highlights high production rate, high reproducibility for constant sections, and hollow small-diameter capability.
- d) True: Slide 21 lists $\text{Al}_2\text{O}_3$, $\text{ZrO}_2$, $\text{Si}_3\text{N}_4$, and $\text{SiC}$ refractory tubes for thermocouples, furnaces, and catalysts.

### Source

Session 18, Slides 19-21.

## Q74.8 Sequence of ceramic injection moulding

- id: B74-Q8
- concept_id: u8-shaping-injection-molding
- format: ordering
- asks: comparison

Which sequence lists the steps of ceramic injection moulding in the correct chronological order?

a) mix powder with binder/wax $\to$ force feedstock into die $\to$ eject green part $\to$ remove binder (brown part) $\to$ sinter
b) mix powder with binder/wax $\to$ sinter in furnace $\to$ remove binder (brown part) $\to$ force feedstock into die (green part)
c) force dry powder into die $\to$ eject brown part $\to$ spray-dry slurry $\to$ remove binder (green part) $\to$ sinter
d) eject green part $\to$ mix powder with binder/wax $\to$ remove binder $\to$ sinter $\to$ force feedstock into die

### Answer

a

### Explanation

Session 18, Slide 22: ceramic injection moulding proceeds in five steps: (1) mixing ceramic powder with binder/wax to make feedstock, (2) injecting feedstock into the die, (3) obtaining the moulded **green part**, (4) debinding by pyrolysis, thermal evaporation, or solvent washing to obtain the **brown part**, and (5) sintering to full density.

- b) Places sintering before binder removal and moulding, which would fuse an unshaped mixture and trap pyrolysis gases.
- c) Swaps green and brown part terminology and inserts spray-drying granulation after die compaction.
- d) Places green-part ejection before feedstock preparation and places die injection after sintering.

### Source

Session 18, Slide 22.

## Q74.9 Trade-offs and aerospace uses of ceramic injection moulding

- id: B74-Q9
- concept_id: u8-shaping-injection-molding
- format: true-statement
- asks: application

Which one of the following statements about ceramic injection moulding (CIM) is TRUE:

a) It uses binder-free dry powder and yields poor dimensional accuracy compared with slip casting
b) It is limited to constant-section rods thicker than $15\ \text{mm}$ and cannot form complex curvatures
c) It is an expensive route offering high dimensional accuracy for complex high-technology parts such as turbocharger rotors and rocket engine components
d) It produces fully dense, binder-free components immediately upon ejection from the injection mould

### Answer

c

### Explanation

Session 18, Slide 22: ceramic injection moulding is expensive (due to tooling, feedstock compounding, and lengthy debinding), yet provides good dimensional accuracy for complex high-technology parts including turbocharger rotors and rocket engine components.

- a) Confuses CIM (high accuracy, rich binder feedstock) with binder-free pressing or low-accuracy slip casting.
- b) Describes the geometric limits of plastic extrusion (Slide 21), not 3D cavity injection moulding.
- d) Ignores that the ejected component is a porous polymer-filled *green part* requiring debinding and sintering.

### Source

Session 18, Slides 21-22.

## Q74.10 Ceramic additive manufacturing processes

- id: B74-Q10
- concept_id: u8-shaping-additive
- format: identify
- asks: classification

Among ceramic free-form fabrication (additive manufacturing) routes, which process selectively cures a liquid photopolymer resin loaded with ceramic particles layer by layer using light or a laser?

a) Powder bed fusion
b) Binder jetting
c) Laminated object manufacturing
d) Photopolymerization

### Answer

d

### Explanation

Session 18, Slides 9 and 29: the six free-form ceramic fabrication methods are material extrusion, material jetting, binder jetting, photopolymerization, powder bed fusion, and laminated object manufacturing; in **photopolymerization**, a UV laser or projected light cures a ceramic-filled photosensitive resin layer by layer.

- a) Powder bed fusion melts or sinters dry powder particles directly in a powder bed with a high-power laser without a photocurable resin.
- b) Binder jetting selectively deposits droplets of liquid binding agent onto a ceramic powder bed rather than curing a liquid resin vat.
- c) Laminated object manufacturing stacks and laser-cuts pre-formed ceramic tape sheets rather than curing liquid resin.

### Source

Session 18, Slides 9 and 29.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
