---
materia: Aerospace Materials I
tema: "Unit 11: tack, peel, lap-shear and wedge durability tests, brittle versus tough peel curves and joint failure modes"
bank_id: B111
title: "Adhesive Testing and Failure Modes"
category: mt3_test_block
unit: 11
concepts:
  - u11-testing-geometric-factors
  - u11-testing-tack-methods
  - u11-testing-peel-variants-factors
  - u11-testing-climbing-drum-wedge
  - u11-testing-brittle-vs-tough-peel
  - u11-testing-normal-shear-uniform
  - u11-failure-2016-extra-modes
  - u11-failure-adhesion-cohesion-locus
  - u11-failure-unacceptable-peel-creep
  - u11-testing-lap-shear-numeric
difficulty: 2
origen: "Questions written for the bank in the style of Part I of Assessment Test III, including Q10 of the June 2016 final exam. Content from Session 24, Slides 4, 25-28 and 30-31."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-11
---

# Bank B111 — Adhesive Testing and Failure Modes

> [!info] Includes official exam questions
> Ten test questions written for the bank in the style of Part I of Assessment Test III, including an official final exam question from June 2016 (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 24, Slides 4, 25-28 and 30-31.

## Q111.1 Geometric parameters of an adhesive test joint

- id: B111-Q1
- concept_id: u11-testing-geometric-factors
- format: identify
- asks: classification

Which set of four geometric parameters characterizes a lap-bonded adhesive joint specimen during mechanical testing?

a) Grain diameter, porosity fraction, specimen mass, and notch angle
b) Melt flow index, chain molecular weight, tacticity, and crystallinity
c) Contact angle, curing oven power, droplet diameter, and roughness depth
d) Bond width, overlapping length, adhesive thickness, and substrate thickness

### Answer

d

### Explanation

Session 24, Slide 25 explicitly defines the geometric factors characterizing an adhesive joint: the width of the bond, the overlapping length, the adhesive thickness, and the substrate thickness.

- a) Describes microstructural parameters of polycrystalline ceramics or metals rather than adhesive lap geometry.
- b) Describes bulk polymer molecular and morphological characteristics (Unit 9), not bonded joint dimensions.
- c) Mixes wetting and process variables with surface roughness rather than the four standard specimen dimensions.

### Source

Session 24, Slide 25.

## Q111.2 Tack (instantaneous adhesion) testing

- id: B111-Q2
- concept_id: u11-testing-tack-methods
- format: topic-true
- asks: definition

Referring to tack testing of adhesives, which one of the following statements is TRUE:

a) Tack measures long-term thermal ageing resistance after 1000 hours at 180 °C
b) Tack evaluates destructive shear strength of fully cured two-part epoxy aircraft spars
c) Tack measures instantaneous adhesion and wettability, evaluated by probe touch-and-lift or rolling distance down an inclined track
d) Tack is assessed exclusively by driving a steel wedge into a cured titanium-epoxy lap joint

### Answer

c

### Explanation

Session 24, Slide 25 defines tack as instantaneous adhesion (ability to stick and wettability), illustrated by touching and lifting a vertical probe from an adhesive layer and by the distance a sphere/drop rolls along an adhesive-coated inclined plane.

- a) Thermal ageing durability is a physical-chemical long-term criterion (Slide 34), not instantaneous tack.
- b) Destructive shear strength of cured structural joints is measured by single-lap shear testing (Slides 28 and 30).
- d) Driving a wedge into a cured specimen tests environmental crack-growth durability, not instantaneous tack.

### Source

Session 24, Slide 25.

## Q111.3 Peel test geometries and bondline thickness effect

- id: B111-Q3
- concept_id: u11-testing-peel-variants-factors
- format: diagram-reading
- asks: figure-reading

![[attachments/T11/s24-peel-tests.png]]

According to the peel-test schematic and the accompanying `Shear strength` versus `thickness` curve shown, which statement is correct?

a) Increasing adhesive thickness raises shear strength linearly across all thickness values
b) Apparent shear strength drops as adhesive thickness increases, and peel tests (90°, 180°, T-peel) represent a loading mode avoided in service
c) The T-peel geometry requires two infinitely rigid steel blocks loaded in pure compression
d) Peel force depends strictly on overlap length and is unaffected by peel angle, rate, or temperature

### Answer

b

### Explanation

Session 24, Slide 26: the plot shows shear strength decreasing as adhesive thickness increases (thicker bondlines contain more defects and higher bending eccentricity). The 90°, 180°, and T-peel tests assess tape/bond compatibility and depend on substrate properties, peel angle, rate, adhesion mechanism, and temperature, though joints must not be loaded in peel in service.

- a) Inverts the plotted curve: shear strength falls rather than rises as adhesive thickness increases.
- c) T-peel tests peel two flexible adherends pulled in opposite directions into a T shape, not rigid compression blocks.
- d) Contradicts Slide 26, which explicitly lists substrate nature/roughness, peeling angle, rate, adhesion mechanism, and temperature as governing peel factors.

### Source

Session 24, Slide 26.

## Q111.4 Specialized peel and wedge durability tests

- id: B111-Q4
- concept_id: u11-testing-climbing-drum-wedge
- format: identify
- asks: application

While T-peel tests two flexible adherends and climbing drum peel measures thin skin-to-honeycomb sandwich peel resistance, which test drives a wedge into a bonded double-cantilever interface under hot-wet exposure to screen surface-preparation durability?

a) Wedge durability test
b) Rolling-ball tack test
c) Unconfined compression block test
d) Vicat softening point test

### Answer

a

### Explanation

Session 24, Slides 25-28 (with standard aerospace testing extension): in the wedge durability test, a metal wedge is driven into the bondline of two thick adherends to open a crack tip under sustained cleavage stress; exposing the wedged specimen to hot-wet environments tracks crack growth to detect weak or poorly prepared interfaces.

- b) Rolling-ball tack tests measure instantaneous surface stickiness of uncured/pressure-sensitive adhesives, not cured interfacial durability.
- c) Compression block tests apply uniform normal compressive loads rather than driving an opening crack tip.
- d) Vicat softening measures thermoplastic needle penetration temperature rather than adhesive interfacial durability.

### Source

Session 24, Slides 25-28; Topic 11 aerospace test extension.

## Q111.5 Brittle versus tough adhesives under peel loading

- id: B111-Q5
- concept_id: u11-testing-brittle-vs-tough-peel
- format: diagram-reading
- asks: figure-reading

![[attachments/T11/s24-brittle-tough-peel.png]]

Compare the left and right peel-front schematics shown. Which pairing correctly identifies the two adhesive classes and explains their difference in peel resistance?

a) Left: flexible polyurethane deforming a large volume; right: rigid epoxy concentrating stress on a line
b) Left: rigid epoxy failing cohesively at high energy; right: rigid cyanoacrylate failing by creep
c) Both schematics represent identical peel energy because the upward arrow acts at the same angle
d) Left: rigid/brittle adhesive concentrating stress on a narrow adhesion line; right: tough/flexible adhesive distributing stress across a large deforming volume

### Answer

d

### Explanation

Session 24, Slide 27: in a rigid/brittle adhesive such as epoxy (left), only the narrow line at the peel front carries the stress, creating high local concentration and low peel energy (< 525 N/m). In a tough/flexible adhesive such as polyurethane (right), a large volume of deforming/fibrillating adhesive shares the stress over a wider surface, yielding much higher peel strength (up to 14 000 N/m).

- a) Swaps the left (line-concentrated brittle) and right (volume-deforming tough) schematics.
- b) Mislabels both panels: rigid epoxy does not absorb high peel energy, and the right schematic illustrates tough/flexible fibrillation rather than creep.
- c) Equal peel angle does not equalize peel energy when one adhesive restricts deformation to a front line and the other spreads strain over a large volume.

### Source

Session 24, Slides 27 and 38.

## Q111.6 Normal and shear qualification tests

- id: B111-Q6
- concept_id: u11-testing-normal-shear-uniform
- format: complete-sentence
- asks: comparison

Unlike peel tests, single-lap shear (UNE-EN 1465), tension, and compression tests characterize structural adhesives fairly because:

a) the load is restricted to a single atom-wide crack tip so adhesive toughness does not matter
b) the substrate yields before any load reaches the adhesive bondline
c) stresses are distributed over the entire bonded area so the whole joint surface carries load
d) results are completely independent of overlap width, length, and surface preparation

### Answer

c

### Explanation

Session 24, Slides 28 and 30: in compression, tension, and shear specimens, the adhesive joint operates over its entire surface area with nearly uniform stress distribution, directly testing the high strength required of structural adhesives.

- a) Line concentration describes peel tests rather than normal/shear qualification tests.
- b) Structural testing aims to measure adhesive shear/normal strength rather than prematurely yielding the adherend.
- d) Bonded area ($w \times L$) and surface cleanliness strongly affect measured failure load in lap-shear testing.

### Source

Session 24, Slides 25, 28, and 30.

## Q111.7 Failure modes of an adhesive joint

- id: B111-Q7
- concept_id: u11-failure-2016-extra-modes
- format: topic-false
- asks: classification
- origin: official-exam

Regarding the failure modes of an adhesive joint (cohesive in adhesive, cohesive in substrate, interfacial/adhesive, and mixed), which one of the following statements is FALSE:

a) Cohesive failure within the adhesive leaves polymer residue on both substrates and is an acceptable mode
b) Clean interfacial (adhesive) failure leaving one bare adherend is the preferred acceptable failure mode
c) Adherend failure or surface-ply delamination in composites indicates the bond exceeded the substrate's local strength and is acceptable
d) Mixed failure (such as 50 % cohesive) shows partial cohesive tearing alongside partial interfacial separation

### Answer

b

### Explanation

June 2016 extraordinary final exam, Q10 (and Session 24, Slides 30-31): cohesive failure of the adhesive, surface-ply delamination of composite adherends, and adherend failure are *acceptable* failure modes because the adhesive-adherend interface held. Interfacial (adhesive) failure between two phases is *unacceptable* because it reveals surface contamination, defective preparation, or environmental interfacial attack. Statement b is false.

- a) True: Slide 31 explicitly classifies cohesive failure of the adhesive as an acceptable failure mode.
- c) True: Slides 30-31 classify substrate (adherend) failure and composite surface-ply delamination as acceptable modes (indicating an over-dimensioned adhesive or sound bond).
- d) True: Slide 30 illustrates 50 % cohesive failure alongside 100 % cohesive, adhesive, and substrate failures under UNE-EN 1465.

### Source

MATERIALS_FINALEXAM_2016_EXTRA_SOL.pdf, p. 5 Q10; Session 24, Slides 30-31.

## Q111.8 Diagnosing failure locus from the adhesion-cohesion schematic

- id: B111-Q8
- concept_id: u11-failure-adhesion-cohesion-locus
- format: diagram-reading
- asks: figure-reading

![[attachments/T11/s24-adhesion-cohesion-schematic.png]]

If a tensile-shear specimen fractures exclusively across the vertical interfacial links (`Adhesión`) along `Sustrato 1` while leaving all internal bulk links (`Cohesión`) intact on `Sustrato 2`, what failure mode has occurred and what does it diagnose?

a) Adhesive (interfacial) failure, diagnosing poor surface preparation, contamination, or interfacial attack
b) Cohesive failure of the adhesive, diagnosing optimal surface cleaning and full adhesive strength
c) Cohesive failure of the substrate, diagnosing excessive overlap length on a weak aluminium skin
d) Adhesive creep flow, diagnosing exposure above the polymer melting point during mixing

### Answer

a

### Explanation

Session 24, Slides 4 and 30-31: breaking across the interfacial `Adhesión` bonds at `Sustrato 1` leaves `Sustrato 1` bare with all adhesive remaining on `Sustrato 2`. That defines interfacial (adhesive) failure—an unacceptable mode pointing to contamination, poor surface preparation, or interfacial moisture degradation.

- b) Cohesive failure breaks the internal `Cohesión` links inside the adhesive molecules, leaving adhesive on both substrates.
- c) Substrate failure breaks `Sustrato 1` or `Sustrato 2` outside the bondline rather than parting the interfacial links.
- d) Creep flow appears as progressive time-dependent shear slip inside the adhesive layer, not brittle interfacial parting.

### Source

Session 24, Slides 4 and 30-31.

## Q111.9 Unacceptable failure modes in service

- id: B111-Q9
- concept_id: u11-failure-unacceptable-peel-creep
- format: what-happens
- asks: cause

Two failed aerospace bonded panels are examined: Panel X failed by excessive out-of-plane deflection peeling the skin from the bondline edge, whereas Panel Y experienced slow time-dependent shear slip while held under static load in a warm cabin. How are these failures classified?

a) Both are acceptable failure modes because neither panel fractured inside the metal skin
b) Panel X is acceptable composite ply delamination, while Panel Y is acceptable cohesive failure
c) Both are unacceptable failure modes: Panel X shows adhesive peel from poor load-path design, and Panel Y shows adhesive creep
d) Only Panel X is unacceptable; Panel Y is desirable viscous stress relaxation

### Answer

c

### Explanation

Session 24, Slide 31 explicitly groups three *unacceptable* failure modes: (1) adhesion failure at the interface, (2) adhesive peel due to excessive out-of-plane loads, and (3) adhesive creep (flow) under sustained load/temperature. Both Panel X and Panel Y represent unacceptable design or material-selection failures.

- a) Failure outside the metal skin does not make peel or creep acceptable; only cohesive adhesive failure and surface-ply delamination are acceptable non-adherend modes.
- b) Out-of-plane peeling at the interface is unacceptable adhesive peel, and slow shear flow is unacceptable creep, not cohesive fracture.
- d) Uncontrolled viscous creep causes permanent joint slip and eventual rupture, so it is classified as unacceptable on Slide 31.

### Source

Session 24, Slide 31.

## Q111.10 Apparent lap-shear strength calculation

- id: B111-Q10
- concept_id: u11-testing-lap-shear-numeric
- format: numeric
- asks: calculation
- calc: 5000 / (25 * 12.5)

In a standard single-lap shear test (UNE-EN 1465), a bonded specimen has bond width $w = 25\text{ mm}$ and overlap length $L = 12.5\text{ mm}$. It fails cohesively at a maximum tensile load $F_{\max} = 5.0\text{ kN}$. What is the apparent lap-shear strength?

a) 8.0 MPa
b) 16.0 MPa
c) 20.0 MPa
d) 32.0 MPa

### Answer

b

### Explanation

Session 24, Slides 25, 28, and 30: the bonded shear area is $A = w L = 25\text{ mm} \times 12.5\text{ mm} = 312.5\text{ mm}^2$. Dividing the failure load $F_{\max} = 5000\text{ N}$ by $A$ gives $\tau_{\max} = 5000 / 312.5 = 16.0\text{ N/mm}^2 = 16.0\text{ MPa}$.

- a) Divides the result by 2 ($8.0\text{ MPa}$), as if two separate shear planes shared the load in a double-lap specimen.
- c) Uses an incorrect overlap length of $10\text{ mm}$ ($5000 / 250 = 20.0\text{ MPa}$) instead of $12.5\text{ mm}$.
- d) Doubles the correct stress ($32.0\text{ MPa}$), corresponding to halving the bonded area.

### Source

Session 24, Slides 25, 28, and 30.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
