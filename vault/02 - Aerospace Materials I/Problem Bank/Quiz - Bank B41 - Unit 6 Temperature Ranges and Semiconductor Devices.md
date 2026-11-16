---
materia: Aerospace Materials I
tema: "Unit 6: exhaustion, saturation and intrinsic ranges; p-n junction, LED, photoconductivity and thermistors"
bank_id: B41
title: "Temperature ranges and semiconductor devices"
category: mt2_test_block
unit: 6
concepts:
  - u6-extrinsic-temperature-regions
  - u6-extrinsic-to-intrinsic
  - u6-extrinsic-slopes
  - u6-pn-junction-led
  - u6-photoconductivity-thermistor
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 13 Slides 33 and 43-48; the chart of question 9 is the official figure of Slide 48."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B41 — Temperature ranges and semiconductor devices

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 13, Slides 33 and 43-48.

## Q41.1 The flat region of the plot

- id: B41-Q1
- concept_id: u6-extrinsic-temperature-regions
- format: diagram-reading
- asks: cause

In region II of the shown plot, the conductivity of the n-type semiconductor stays almost constant because:

![[attachments/MAT-MT2/u6-extrinsic-regions.svg]]

a) All the donor atoms are already ionised
b) Electrons are excited across the band gap
c) The donor atoms are not yet ionised
d) The mobility of the carriers rises with temperature

### Answer

a

### Explanation

Session 13, Slides 43-44: at intermediate temperature all the impurities have been ionised, so the number of carriers stays constant and $\sigma$ is almost constant: the exhaustion range of an n-type semiconductor (region II).

- b) Excitation across the gap is the mechanism of region I, the intrinsic range at high temperature, where $\sigma$ rises steeply.
- c) Donors still being ionised is the situation of region III (extrinsic range), where $\sigma$ rises with temperature.
- d) Inverted: the disordering effect of temperature lowers the mobility, which is why $\sigma$ even decreases slightly in this range (Slide 44).

### Source

Session 13, Slides 43-44.

## Q41.2 Name of the range in a p-type semiconductor

- id: B41-Q2
- concept_id: u6-extrinsic-temperature-regions
- format: complete-sentence
- asks: definition

For a p-type semiconductor, the temperature range in which every acceptor is ionised and $\sigma$ is almost constant is called the:

a) Exhaustion range
b) Intrinsic range
c) Extrinsic range
d) Saturation range

### Answer

d

### Explanation

Session 13, Slide 43: at intermediate temperature all the impurities are ionised; for the n-type this is the exhaustion range (all donor electrons lost) and for the p-type the saturation range (all acceptor atoms ionised).

- a) Exhaustion is the name of the same range for an n-type semiconductor.
- b) The intrinsic range is the high-temperature range, where carriers are generated across the gap.
- c) The extrinsic range is the low-temperature range, where the number of ionised impurities is still growing.

### Source

Session 13, Slide 43.

## Q41.3 Phosphorus-doped germanium at very high temperature

- id: B41-Q3
- concept_id: u6-extrinsic-to-intrinsic
- format: what-happens
- asks: effect

What will happen to germanium doped with phosphorus when it is heated to a very high temperature:

a) It will become a p-type semiconductor
b) It will behave as an intrinsic semiconductor
c) Its conductivity will fall to that of an insulator
d) Its conductivity will stay at the exhaustion value

### Answer

b

### Explanation

Session 13, Slides 43-44: at very high temperature the electrons and holes generated across the gap outnumber the carriers of the dopant, so the material behaves as an intrinsic conductor.

- a) The type of dopant does not change on heating; intrinsic generation gives electrons and holes in equal numbers, not a p-type material.
- c) Inverted: heating increases the number of carriers, and $\sigma$ rises with slope $-E_g/2k$.
- d) The exhaustion value holds only at intermediate temperature, before intrinsic generation takes over.

### Source

Session 13, Slides 43-44.

## Q41.4 Slope of the intrinsic range against the extrinsic range

- id: B41-Q4
- concept_id: u6-extrinsic-slopes
- format: cause-effect
- asks: comparison
- check: 1.1 > 0.045

With an increase in temperature from the extrinsic to the intrinsic range of phosphorus-doped silicon, the slope of $\ln\sigma$ against $1/T$:

a) Becomes steeper, as $E_g$ is much larger than $E_c - E_d$
b) Becomes less steep, as $E_g$ is much larger than $E_c - E_d$
c) Becomes steeper, as the carrier mobility rises
d) Stays the same, as both ranges depend on $E_c - E_d$

### Answer

a

### Explanation

Session 13, Slide 43: the extrinsic slope is $-(E_c - E_d)/2k$ and the intrinsic slope $-E_g/2k$. For P in Si, $E_c - E_d = 0.045$ eV (Slide 40) against $E_g = 1.1$ eV, so the intrinsic line is much steeper.

- b) Right comparison of the energies, inverted consequence: a larger energy gives a steeper slope.
- c) Right trend with the wrong cause: the mobility falls with temperature; the slope comes from the energy of the excitation.
- d) The intrinsic range is set by the band gap, not by the donor level.

### Source

Session 13, Slides 40 and 43.

## Q41.5 The p-n junction

- id: B41-Q5
- concept_id: u6-pn-junction-led
- format: complete-sentence
- asks: definition

A p-n junction is:

a) The contact between a metal and a semiconductor
b) The boundary between two grains of pure silicon
c) The gap between the valence and the conduction band
d) The interface between p-type and n-type regions of one crystal

### Answer

d

### Explanation

Session 13, Slide 45: a p-n junction is a boundary or interface between two types of semiconductor material, p-type and n-type, inside a single crystal.

- a) A metal is not one of the two sides; both sides are doped semiconductor.
- b) A grain boundary of an intrinsic material has no p and n sides; it is a planar defect.
- c) The band gap is an energy range of one material, not an interface between two regions.

### Source

Session 13, Slide 45.

## Q41.6 Colour of an LED

- id: B41-Q6
- concept_id: u6-pn-junction-led
- format: complete-sentence
- asks: cause

The colour of the light emitted by an LED depends on:

a) The intensity of the forward current
b) The temperature of the p-n junction
c) The distance between the valence and conduction bands
d) The thickness of the depletion layer

### Answer

c

### Explanation

Session 13, Slide 47: in an LED electrons and holes recombine at the junction and release the energy $E_g$ as a photon; the colour depends on the distance between the valence and the conduction band.

- a) The current sets how many recombinations occur, not the energy of each photon.
- b) The slide relates the colour to the material, through its gap, not to the temperature.
- d) The depletion layer is part of the junction (Slide 45), but the photon energy is the band gap.

### Source

Session 13, Slides 45 and 47.

## Q41.7 Ranking LED materials by band gap

- id: B41-Q7
- concept_id: u6-pn-junction-led
- format: ordering
- asks: comparison

Order the following LED materials from the smallest to the largest band gap:

a) AlGaAs < GaP < ZnSe < diamond
b) Diamond < ZnSe < GaP < AlGaAs
c) GaP < AlGaAs < ZnSe < diamond
d) AlGaAs < ZnSe < GaP < diamond

### Answer

a

### Explanation

Session 13, Slide 47: the band gap increases down the table, from AlGaAs (red and infra-red) to GaP (green), ZnSe (blue) and diamond (ultra-violet); the gaps of Slides 33 and 46 agree (AlGaAs 1.7 eV, GaP 2.25 eV, diamond 6 to 7 eV).

- b) Fully reversed order, from the largest to the smallest gap (it ranks the wavelengths).
- c) AlGaAs and GaP are swapped: red light has less energy than green light.
- d) GaP and ZnSe are swapped: blue light needs a larger gap than green light.

### Source

Session 13, Slides 8, 33, 46 and 47.

## Q41.8 Photons of 1.3 eV on two solar cells

- id: B41-Q8
- concept_id: u6-photoconductivity-thermistor
- format: what-happens
- asks: application
- check: 1.1 < 1.3 < 1.43

What will happen to photons of 1.3 eV that reach a silicon cell and a gallium arsenide cell:

a) Both materials will absorb them
b) Neither material will absorb them
c) Gallium arsenide will absorb them and silicon will let them through
d) Silicon will absorb them and gallium arsenide will let them through

### Answer

d

### Explanation

Session 13, Slide 46: a photon can lift an electron across the gap only if its energy is at least $E_g$; silicon absorbs photons above 1.1 eV and gallium arsenide above 1.43 eV, so 1.3 eV is absorbed by Si and goes through GaAs.

- a) Ignores that 1.3 eV is below the 1.43 eV gap of GaAs.
- b) Ignores that 1.3 eV is above the 1.1 eV gap of Si.
- c) The two materials are swapped: GaAs has the larger gap.

### Source

Session 13, Slide 46.

## Q41.9 Reading the thermistor chart

- id: B41-Q9
- concept_id: u6-photoconductivity-thermistor
- format: diagram-reading
- asks: application

From the shown chart of conductivity against temperature, indicate which material suits a thermistor and why:

![[attachments/T6/s13-thermistor.png]]

a) Aluminium, as its conductivity is the highest
b) Germanium, as its conductivity changes by orders of magnitude
c) Aluminium, as its conductivity falls with temperature
d) Germanium, as its conductivity is almost constant

### Answer

b

### Explanation

Session 13, Slide 48: thermistors are devices based on the change of the electrical conductivity of semiconductors with temperature. In the chart the conductivity of germanium grows from about 0.02 to about 30 (Ω·cm)⁻¹ between 25 and 400 °C (reading of the chart), while aluminium changes by less than a factor of three.

- a) A high conductivity is what a conductor needs; a thermistor needs a large change of conductivity with temperature.
- c) Aluminium does change, but only slightly (reducing mobility); the slide bases thermistors on semiconductors.
- d) Misreads the chart: the germanium curve rises steeply on the logarithmic axis, it is not flat.

### Source

Session 13, Slide 48.

## Q41.10 Photoconductivity

- id: B41-Q10
- concept_id: u6-photoconductivity-thermistor
- format: true-statement
- asks: definition

Which one of the following statements about photoconductivity is TRUE?

a) It needs photons with energy below the band gap
b) It lowers the conductivity of the material
c) It needs photons with energy of at least the band gap
d) It is caused only by the heating of the lattice

### Answer

c

### Explanation

Session 13, Slide 46: photoconductivity is the phenomenon in which a material becomes more conductive due to the absorption of electromagnetic radiation; the photon must lift an electron across the gap, so its energy must be at least $E_g$.

- a) Inverted: photons below the gap go through the material without being absorbed.
- b) Inverted effect: the absorbed light creates carriers, so the material becomes more conductive.
- d) Thermal excitation is a different cause listed on the same slide; photoconductivity is excitation by radiation.

### Source

Session 13, Slide 46.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
