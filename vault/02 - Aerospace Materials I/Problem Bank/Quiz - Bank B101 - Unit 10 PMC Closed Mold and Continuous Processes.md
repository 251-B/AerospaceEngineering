---
materia: Aerospace Materials I
tema: "Unit 10: filament winding and patterns, pultrusion, resin transfer molding (RTM), resin film infusion (RFI), compression molding with SMC/BMC, and spray lay-up"
bank_id: B101
title: "PMC closed mold and continuous processes"
category: mt3_test_block
unit: 10
concepts:
  - u10-filament-winding-process
  - u10-filament-winding-patterns
  - u10-pultrusion-process
  - u10-pultrusion-geometry-limitation
  - u10-rtm-process-principles
  - u10-rtm-mold-features
  - u10-rfi-resin-film-infusion
  - u10-molding-smc-compression
  - u10-molding-spray-layup
  - u10-molding-process-selection
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_THIRDPARTIAL_2020.pdf; not official exercises. Content from Session 23 Slides 7, 9-18, 23 and 54."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-10
---

# Bank B101 — PMC closed mold and continuous processes

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test III (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 23, Slides 7, 9-18, 23 and 54.

## Q101.1 Filament winding fundamentals and aerospace uses

- id: B101-Q1
- concept_id: u10-filament-winding-process
- format: topic-true
- asks: application

Referring to filament winding of polymer matrix composites, which one of the following statements is TRUE:

a) Filament winding injects chopped short fibres and paste between matched metal dies to stamp flat car panels
b) It is limited to planar open sheets that are later stamped in a compression press
c) It requires feeding dry fabrics into an open mould without impregnating the fibres until after autoclave removal
d) Continuous filaments, rovings, or narrow prepregs are wrapped under tension onto a rotating mandrel to form hollow axisymmetric parts

### Answer

d

### Explanation

Session 23, Slides 17-18 and 54: filament winding—the first automated composite process—passes continuous filaments, rovings, or tapes through a resin bath (or uses narrow prepregs), winds them onto a rotating mandrel via a traversing carriage, and cures the part. It produces hollow closed and open shells or tubes such as pressure vessels, rocket motor casings, radomes, drive shafts, and the Boeing 767 slide-raft inflation vessels.

- a) Describes compression moulding of Sheet/Bulk Moulding Compound (Slides 7 and 11), not filament winding.
- b) Confuses filament winding with flat ATL lamination and hot forming of spars/ribs (Slide 20).
- c) In filament winding, fibres are either resin-impregnated in a bath right before wrapping or supplied as narrow prepregs, and cured on the mandrel.

### Source

Session 23, Slides 17-18 and 54.

## Q101.2 Winding patterns and fibre angle control

- id: B101-Q2
- concept_id: u10-filament-winding-patterns
- format: cause-effect
- asks: cause

In CNC filament winding on a cylindrical mandrel, what controls the winding angle $\theta$ of the fibres, and which winding pattern is required to wrap over the dome ends of a closed pressure vessel?

a) The ratio of carriage traverse speed to mandrel rotational speed sets $\theta$; helical or polar winding wraps over the dome ends while circumferential (hoop) winding resists radial hoop stress
b) The resin bath temperature sets $\theta$; circumferential (hoop) winding covers the closed end domes along the mandrel axis
c) The autoclave gas pressure sets $\theta$; spray lay-up covers the end domes after hoop winding
d) The fibre tow count sets $\theta$; only $90^\circ$ circumferential winding can carry axial pressure loads without fibre slip

### Answer

a

### Explanation

Session 23, Slide 17: the fibre orientation angle depends on the ratio between the linear carriage feed speed and the angular speed of the rotating mandrel. Circumferential (hoop) winding places fibres nearly perpendicular to the cylinder axis to carry hoop stress, whereas helical and polar patterns (following non-slip geodesic paths in advanced winding, extension) traverse end-to-end to cover the domes and carry axial loads.

- b) Bath temperature affects resin viscosity rather than winding geometry, and hoop winding near $90^\circ$ cannot wrap across polar end domes.
- c) Filament winding is typically oven-cured on the mandrel rather than shaped by autoclave pressure, and spray lay-up is a separate manual process.
- d) Tow count sets band thickness and cost (Session 21, Slide 25), not angle, and $90^\circ$ hoop plies alone carry almost no axial load.

### Source

Session 23, Slide 17.

## Q101.3 Reading the continuous pultrusion schematic

- id: B101-Q3
- concept_id: u10-pultrusion-process
- format: diagram-reading
- asks: figure-reading

In the continuous pultrusion process shown, what is the role of the preforming die located immediately upstream of the heated curing die?

![[attachments/T10/s23-pultrusion-schematic.png]]

a) To chop continuous rovings into random short fibres and deposit them onto a resin paste sheet
b) To establish the cross-sectional profile and meter the fibre-to-resin ratio before curing
c) To apply pressurized inert gas that infiltrates molten metal into the fibre bundle
d) To strip backing paper from B-stage prepreg sheets before vacuum bagging

### Answer

b

### Explanation

Session 23, Slide 23: in pultrusion, continuous fibre rovings (glass, carbon, or aramid) are drawn through a resin impregnation tank (polyester, vinyl ester, or epoxy), pulled through a **preforming die** that shapes the cross-section and removes excess resin to fix the fibre/matrix ratio, and then cured inside a heated die before exiting through the pullers.

- a) Describes SMC line fabrication (Slide 7), whereas pultrusion uses continuous aligned rovings throughout.
- c) Describes gas pressure infiltration for metal matrix composites (Slide 35), not polymer pultrusion.
- d) Backing paper removal belongs to prepreg tape laying (ATL, Slide 19), whereas pultrusion impregnates raw rovings in a liquid resin bath.

### Source

Session 23, Slides 7, 19, 23 and 35.

## Q101.4 Shapes and mechanics of pultrusion vs extrusion

- id: B101-Q4
- concept_id: u10-pultrusion-geometry-limitation
- format: identify
- asks: application

Which statement correctly identifies the parts produced by pultrusion and how the process operates?

a) Hollow spherical pressure vessels with variable wall thickness, formed by pushing molten resin through a die
b) Complex doubly curved fuselage skins with cutouts, formed by vacuum-drawing dry fabrics over a male tool
c) Constant cross-section profiles such as rods, tubes, beams, and stringers, formed by pulling continuous fibres and thermoset resin through heated dies
d) Thin isotropic panels of randomly oriented chopped fibres, formed by spraying resin onto an open mould

### Answer

c

### Explanation

Session 23, Slides 23 and 54: pultrusion pulls continuous rovings impregnated with thermoset resin (polyester, vinyl ester, or epoxy) through a preforming die and heated curing die to manufacture constant cross-section profiles—such as rods, tubes, floor beams, stringers, spars, ribs, and longerons. Unlike polymer extrusion (which pushes melt through a die), pultrusion pulls continuous fibres under tension.

- a) Spherical or closed dome vessels require filament winding (Slide 17), and pultrusion pulls rather than pushes.
- b) Curved aerospace skin shells are made by ATL/AFP, hand lay-up, or RFI/RTM, not constant-section pultrusion.
- d) Random chopped-fibre open-mould panels correspond to spray lay-up (Slide 10).

### Source

Session 23, Slides 10, 17, 23 and 54.

## Q101.5 Resin Transfer Molding (RTM) principles

- id: B101-Q5
- concept_id: u10-rtm-process-principles
- format: topic-false
- asks: definition

Regarding Resin Transfer Molding (RTM), also known as Resin Injection Molding (RIM), which one of the following statements is FALSE:

a) RTM places pre-impregnated B-stage prepreg tape onto a single open mould without closing or sealing the tool
b) RTM places a dry fibre preform or fabric inside a closed mould and injects liquid resin under pressure to impregnate the fibres
c) The closed RTM mould cavity is often evacuated under vacuum while resin is injected to aid complete fibre wet-out
d) Epoxy and polyester are the most widely used RTM resins, although low-viscosity thermoplastic precursors can also be processed

### Answer

a

### Explanation

Session 23, Slides 13-14: RTM places **dry** (non-impregnated) fabric or discontinuous preforms inside a **closed** matched mould and forces liquid resin into the cavity under injection pressure (often assisted by vacuum). Using B-stage prepreg on an open mould describes hand lay-up or vacuum-bag prepreg moulding, not RTM. Statement a is false.

- b) True: Slide 13 defines RTM as placing dry preform/fabric in a closed mould and forcing resin in under pressure before cure.
- c) True: Slide 13 explicitly notes that the closed mould is often under vacuum during injection (a principle shared by one-sided vacuum-assisted infusion, VARTM, extension).
- d) True: Slide 14 lists epoxy and polyester as the main RTM resins and notes that thermoplastic matrices can also be used.

### Source

Session 23, Slides 13-14.

## Q101.6 Closed-mould features in the RTM section

- id: B101-Q6
- concept_id: u10-rtm-mold-features
- format: diagram-reading
- asks: figure-reading

In the Resin Transfer Molding (RTM) closed-mould cross-section shown, what is the purpose of the perimeter seal and the central air-sucking vent?

![[attachments/T10/s23-rtm-mold-section.png]]

a) To allow continuous fibre rovings to slide uninterruptedly out of the tool like a pultrusion die
b) To heat the dry fabric above the glass-transition temperature of the carbon fibres prior to spraying
c) To inject pressurized inert gas from the centre so the resin drains back out into the storage tank
d) To seal the matched mould halves so vacuum can evacuate air ahead of the injected resin front and prevent dry voids

### Answer

d

### Explanation

Session 23, Slides 13-14: in the closed RTM mould section, the perimeter seal keeps the cavity airtight while the central air-sucking port ("creep draining" / vent) draws out trapped air under vacuum as liquid resin enters from the side injection ports, ensuring full impregnation of the dry fabric preform without air pockets.

- a) RTM is a batch closed-mould process for discrete preforms, not a continuous open-ended pulling die.
- b) Carbon fibres do not melt or soften at polymer processing temperatures, and RTM does not use spray guns.
- c) Evacuation removes air *ahead* of the resin front to eliminate voids; pressurizing the centre port would push resin away and block wet-out.

### Source

Session 23, Slides 13-14.

## Q101.7 Resin Film Infusion (RFI) vs liquid injection

- id: B101-Q7
- concept_id: u10-rfi-resin-film-infusion
- format: complete-sentence
- asks: comparison

In Resin Film Infusion (RFI), dry fibre reinforcement is stacked with a solid or semi-solid film-shaped resin in the mould, so that when heat and pressure are applied:

a) the dry fibres dissolve into the film and are sprayed onto a mandrel
b) the resin film melts and diffuses through the thickness of the dry preform to impregnate it completely
c) the film remains unmelted as a protective peel ply that is stripped away after curing
d) the resin must be pumped horizontally across the full length of the mould from a heated external tank

### Answer

b

### Explanation

Session 23, Slide 15: RFI places resin in film form together with dry fibre layers inside either a closed mould or an open mould with a vacuum bag. Applying heat and pressure (in an autoclave or with vacuum and heat) causes the resin film to liquefy and flow through the dry fibre thickness, achieving complete wet-out.

- a) RFI impregnates stacked dry fabrics in place; no dissolution of fibres or spraying takes place.
- c) Unlike a disposable peel ply (Slide 12), the resin film becomes the structural polymer matrix of the cured composite.
- d) Pumping liquid resin horizontally from an external tank characterizes RTM (Slides 13-14), whereas RFI melts a pre-placed resin film through the thickness.

### Source

Session 23, Slides 12-15.

## Q101.8 Sheet Molding Compound (SMC) and compression molding

- id: B101-Q8
- concept_id: u10-molding-smc-compression
- format: true-statement
- asks: classification

Which of the following statements is TRUE regarding Sheet Molding Compound (SMC) and compression molding of PMCs:

a) SMC consists of continuous unidirectional carbon tapes pressed between heated rolls for primary aircraft wing spars
b) Compression molding places a dry non-impregnated preform into an open mould and cures it under atmospheric vacuum without a second mould half
c) SMC is prepared by sandwiching randomly oriented chopped short fibres between two resin paste layers and is shaped between two matched moulds in compression molding
d) Compression molding cannot process bulk-forming compounds (BMC) because matched moulds can only operate at cryogenic temperatures

### Answer

c

### Explanation

Session 23, Slides 7 and 11: SMC is manufactured by chopping continuous fibres into short lengths, depositing them randomly over a layer of resin paste, adding a top resin layer, and rolling into a viscous sheet (less widely used in aerospace than prepregs). Compression molding then places SMC or a bulk-forming compound (BMC: viscous mixture of polymer, chopped fibres, and additives) between two matched moulds (at room temperature or heated) and applies pressure.

- a) Continuous unidirectional aerospace tapes are prepregs (Slides 4-6), whereas SMC uses chopped short random fibres (Slide 7).
- b) Placing dry fabric in an open mould under a vacuum bag describes RFI or vacuum-bag moulding, whereas compression moulding uses two matched mould halves on pre-mixed SMC/BMC.
- d) Compression moulding routinely handles BMC between moulds at room or elevated temperature, never cryogenic temperatures (Slide 11).

### Source

Session 23, Slides 4-7 and 11.

## Q101.9 Fibre architecture constraint in spray lay-up

- id: B101-Q9
- concept_id: u10-molding-spray-layup
- format: what-happens
- asks: effect

When a composite part is manufactured by manual spray lay-up (spraying a mixture of fibres, resin, and curing agent onto an open mould), what reinforcement architecture results?

a) Continuous unidirectional aligned fibres with over 65 % fibre volume fraction
b) Three-dimensional braided continuous preforms oriented along principal stress paths
c) Alternating cross-plied layers at $0^\circ$, $+45^\circ$, $-45^\circ$, and $90^\circ$
d) Short, randomly oriented fibres, because continuous fibres cannot be sprayed through the gun

### Answer

d

### Explanation

Session 23, Slide 10: spray lay-up directs chopped glass fibres together with resin and curing agent from a spray gun onto an open mould. Slide 10 explicitly states that spray lay-up *cannot use continuous fibres*—only short, randomly aligned fibres—giving lower mechanical performance than hand-laid continuous prepregs.

- a) High-volume-fraction continuous UD composites require prepregs, filament winding, or pultrusion, not a chopper spray gun.
- b) 3D braided preforms are dry textile structures (Session 21, Slide 33) infused by RTM or RFI.
- c) Multi-angle laminates ($0/\pm 45/90$) require continuous plies or NCFs (Session 21, Slides 32 and 37), impossible to control with random spray deposition.

### Source

Session 23, Slide 10; Session 21, Slides 32-33 and 37.

## Q101.10 Selecting the closed-mold or continuous PMC process

- id: B101-Q10
- concept_id: u10-molding-process-selection
- format: identify
- asks: application

An automotive or aerospace supplier needs a smooth surface finish on both sides of a complex, three-dimensional hollow bracket with ribs, starting from a dry braided carbon preform and liquid epoxy resin without using B-stage prepregs or an autoclave. Which process is best suited?

a) Pultrusion
b) Resin Transfer Molding (RTM)
c) Spray lay-up
d) Hand lay-up of UD prepreg

### Answer

b

### Explanation

Session 23, Slides 9-15 and 23: **RTM** uses a dry fibre preform placed inside a two-sided closed matched mould—producing controlled thickness and smooth tool surfaces on both sides—and injects liquid epoxy under pressure (often with vacuum assistance) before curing without an autoclave.

- a) Pultrusion only produces straight, constant cross-section profiles (rods, beams, stringers), not complex 3D bracket shapes (Slide 23).
- c) Spray lay-up deposits random chopped fibres on a single open mould, yielding low strength and only one smooth tool-side face (Slide 10).
- d) Hand lay-up of prepreg uses pre-impregnated plies rather than a dry braided preform and leaves the bag side rougher than a matched closed mould.

### Source

Session 23, Slides 9-15 and 23.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
