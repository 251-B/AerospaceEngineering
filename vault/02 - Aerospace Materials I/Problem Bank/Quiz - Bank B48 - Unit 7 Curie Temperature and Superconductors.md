---
materia: Aerospace Materials I
tema: "Unit 7: Curie and Néel temperatures, critical temperature, Meissner effect and types of superconductors"
bank_id: B48
title: "Curie and Néel temperatures and superconductors"
category: mt2_test_block
unit: 7
concepts:
  - u7-curie-temperature
  - u7-neel-temperature
  - u7-superconductor-tc-meissner
  - u7-superconductor-types
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf and of the short questions of the 2012 and June 2015 finals; not official exercises. Data from Session 15, Slides 23-29 and 44."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-7
---

# Bank B48 — Curie and Néel temperatures and superconductors

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 15, Slides 23-29.

## Q48.1 Curie temperature

- id: B48-Q1
- concept_id: u7-curie-temperature
- format: complete-sentence
- asks: definition

The Curie temperature of a ferromagnetic material is the temperature at which:

a) its saturation magnetization falls abruptly to zero
b) its electrical resistivity drops to zero
c) an antiferromagnetic material becomes paramagnetic
d) its coercivity reaches its maximum value

### Answer

a

### Explanation

Slide 23: the Curie temperature $T_c$ is the temperature at which the saturation magnetization abruptly falls to 0; above it, ferromagnetic and ferrimagnetic materials become paramagnetic.

- b) Confuses the Curie temperature with the critical temperature $T_c$ of a superconductor (Slide 25), which shares the same symbol.
- c) This is the Néel temperature, the neighbouring definition for antiferromagnetic materials (Slide 23).
- d) Inverted trend: heating makes the loop shrink, with $H_c$ falling (Slide 22), and above $T_c$ there is no loop at all.

### Source

Session 15, Slides 22-23 and 25.

## Q48.2 Nickel part at 400 °C

- id: B48-Q2
- concept_id: u7-curie-temperature
- format: what-happens
- asks: application
- check: 400 + 273.15 > 631

The Curie temperature of nickel is 631 K. What will happen to the magnetic behaviour of a nickel part held at 400 °C?

a) It stays ferromagnetic, since 400 is below 631
b) It becomes antiferromagnetic above its Néel temperature
c) It becomes diamagnetic, like a superconductor
d) It becomes paramagnetic, being above its Curie temperature

### Answer

d

### Explanation

$400$ °C $= 673$ K, which is above $T_c = 631$ K (Slide 23); above the Curie temperature a ferromagnetic material becomes paramagnetic.

- a) The temperature in °C is compared with a value in K; converted, 400 °C is 673 K, above 631 K.
- b) The Néel temperature belongs to antiferromagnetic materials, and above it they become paramagnetic, not the other way round.
- c) Perfect diamagnetism is the Meissner state of a superconductor below its critical temperature (Slide 27), unrelated to heating a ferromagnet.

### Source

Session 15, Slides 23 and 27.

## Q48.3 Identifying a metal from its Curie point

- id: B48-Q3
- concept_id: u7-curie-temperature
- format: diagram-reading
- asks: figure-reading

The shown curve gives the saturation magnetization of a ferromagnetic metal against temperature. Given Curie temperatures of 1404 K (Co), 1043 K (Fe), 631 K (Ni) and 289 K (Gd), which metal is shown?

![[attachments/MAT-MT2/u7-ms-temperature.svg]]

a) Co
b) Fe
c) Ni
d) Gd

### Answer

b

### Explanation

The magnetization falls to zero just above 1000 K, at about 1040 K; among the four values given, $T_c = 1043$ K corresponds to Fe (Session 15, Slide 23 puts it at about 770 °C).

- a) Co has $T_c = 1404$ K, beyond the drop of the curve.
- c) Ni has $T_c = 631$ K: the curve would reach zero between the 600 and 800 K marks.
- d) Gd has $T_c = 289$ K, so its magnetization would vanish close to room temperature.

### Source

Session 15, Slide 23.

## Q48.4 Behaviour above and below the Curie temperature

- id: B48-Q4
- concept_id: u7-curie-temperature
- format: false-statement
- asks: effect

Which one of the following statements is FALSE about the Curie temperature $T_c$ of magnetic materials?

a) Both ferromagnetic metals and ferrimagnetic ceramics have a Curie temperature
b) Above $T_c$, thermal agitation destroys long-range ordering and the material becomes paramagnetic
c) Near $T_c$, ferromagnetic materials such as iron show a peak in specific heat
d) Once heated above $T_c$, a ferromagnetic metal remains permanently paramagnetic upon cooling

### Answer

d

### Explanation

Session 15, Slides 22-23 and 35: heating above $T_c$ causes thermal agitation to overcome magnetic ordering so $M_s$ drops to zero and the material becomes paramagnetic, but the transition is reversible—cooling back below $T_c$ restores spontaneous ferromagnetic ordering.

- a) True: Slide 23 explicitly states that above $T_c$, ferromagnetic and ferrimagnetic materials become paramagnetic (and plots both Fe and $\text{Fe}_3\text{O}_4$).
- b) True: thermal agitation misaligns dipoles so spontaneous magnetization drops abruptly to zero at $T_c$ (Slide 23).
- c) True: ferromagnetic metals such as iron display a high specific heat at their Curie temperature (Slide 35).

### Source

Session 15, Slides 22-23 and 35.

## Q48.5 Néel temperature

- id: B48-Q5
- concept_id: u7-neel-temperature
- format: true-statement
- asks: definition

Which one of the following statements is TRUE about the Néel temperature?

a) Above it a ferromagnetic material becomes paramagnetic
b) Below it a material turns into a superconductor
c) Above it an antiferromagnetic material becomes paramagnetic
d) Above it an antiferromagnetic material becomes ferromagnetic

### Answer

c

### Explanation

Slide 23: the Néel temperature is the temperature at which an antiferromagnetic material becomes paramagnetic, because the thermal energy destroys its macroscopic magnetic ordering.

- a) This is the Curie temperature, the analogous limit for ferromagnetic and ferrimagnetic materials.
- b) This is the critical temperature of a superconductor (Slide 25).
- d) Heating destroys the order instead of creating a parallel one: the material becomes paramagnetic, not ferromagnetic.

### Source

Session 15, Slides 23 and 25.

## Q48.6 Chromium at 100 °C

- id: B48-Q6
- concept_id: u7-neel-temperature
- format: complete-sentence
- asks: application
- check: 100 + 273.15 > 310

Chromium has a Néel temperature of 310 K. At 100 °C, chromium is:

a) antiferromagnetic
b) paramagnetic
c) ferromagnetic
d) diamagnetic

### Answer

b

### Explanation

$100$ °C $= 373$ K, above the Néel temperature of 310 K (Slide 23), so the antiparallel order is destroyed and chromium is paramagnetic, as Slide 5 lists it.

- a) The 100 °C is compared with 310 without converting to kelvin; 373 K is above the Néel temperature.
- c) The Néel temperature is confused with a Curie temperature, and the ordered state with the parallel one; chromium is never ferromagnetic on the slides.
- d) The diamagnetic examples of Slide 5 (Cu, Ag, Au, Si, Zn) have no permanent dipoles; chromium has them.

### Source

Session 15, Slides 5, 10 and 23.

## Q48.7 Expulsion of the field

- id: B48-Q7
- concept_id: u7-superconductor-tc-meissner
- format: identify
- asks: definition

Which effect is the expulsion of the magnetic field from a material in the superconducting state?

a) The Meissner effect
b) The Josephson effect
c) The Curie transition
d) The thermocouple effect

### Answer

a

### Explanation

Slide 27: the Meissner-Ochsenfeld effect is the expulsion of the magnetic field from a material in the superconducting state; below $T_c$ the field lines are pushed around it and it behaves as a perfect diamagnet.

- b) The Josephson effect is the tunnel current between two superconductors separated by a thin insulating layer (Slide 31).
- c) The Curie transition is the loss of ferromagnetism of a magnetic material on heating (Slide 23).
- d) The thermocouple effect is the voltage produced by two dissimilar conductors at different temperatures (Slide 44).

### Source

Session 15, Slides 23, 27, 31 and 44.

## Q48.8 Identifying a superconductor from its resistivity

- id: B48-Q8
- concept_id: u7-superconductor-tc-meissner
- format: diagram-reading
- asks: figure-reading

A pure metal is cooled towards 0 K and its measured resistivity follows the shown curve. Given critical temperatures of 4.15 K (Hg), 7.19 K (Pb), 9.26 K (Nb) and 1.20 K (Al), the metal is:

![[attachments/MAT-MT2/u7-rho-temperature.svg]]

a) mercury
b) lead
c) niobium
d) aluminium

### Answer

c

### Explanation

The resistivity drops to zero at about 9.3 K, between the 8 and 10 K marks; the table of Slide 25 gives $T_c = 9.26$ K for Nb.

- a) Hg has $T_c = 4.15$ K: the drop would be close to the 4 K mark.
- b) Pb has $T_c = 7.19$ K, below the 8 K mark.
- d) Al has $T_c = 1.20$ K, near the origin of the axis.

### Source

Session 15, Slide 25.

## Q48.9 Type II superconductors

- id: B48-Q9
- concept_id: u7-superconductor-types
- format: true-statement
- asks: comparison

Which one of the following statements is TRUE about Type II superconductors?

a) They lose superconductivity abruptly at one low critical field
b) Between $H_{c1}$ and $H_{c2}$ they are in a mixed state
c) They are pure metals such as Pb and Hg
d) Their critical field rises with temperature

### Answer

b

### Explanation

Slide 29: in Type II superconductors the flux lines begin to penetrate at $H_{c1}$ and the penetration is complete at $H_{c2}$; between the two the material is in a mixed state of normal and superconducting regions.

- a) A sharp transition at a very low $H_c$ is the behaviour of Type I superconductors (Slide 28).
- c) Pure metals such as Sn, Al, Pb and Hg are the Type I examples; Type II are alloys, intermetallics and ceramics.
- d) Inverted trend: $H_c$ and $J_c$ decrease with increasing temperature (Slide 26).

### Source

Session 15, Slides 26, 28 and 29.

## Q48.10 A Type I superconductor

- id: B48-Q10
- concept_id: u7-superconductor-types
- format: identify
- asks: classification

Which of the following materials is a Type I superconductor?

a) Nb₃Sn
b) Nb-Ti
c) YBaCuO
d) Pb

### Answer

d

### Explanation

Slide 28: the Type I (soft) superconductors are pure metals such as Sn, Al, Pb and Hg.

- a) Nb₃Sn is an intermetallic compound, listed as a Type II superconductor (Slide 29).
- b) Nb-Ti is an alloy, listed as Type II (Slide 29).
- c) YBaCuO is a ceramic, listed as Type II (Slide 29).

### Source

Session 15, Slides 28-29.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
