---
materia: Aerospace Materials I
tema: "Unit 6: resistance of a wire, conductivity from carriers and mobility, ionic and electronic conduction, resistivity of metals and temperature"
bank_id: B35
title: "Conductivity, carriers and resistivity of metals"
category: mt2_test_block
unit: 6
concepts:
  - u6-resistance-geometry
  - u6-conductivity-carriers-mobility
  - u6-ionic-vs-electronic-conduction
  - u6-metal-conductivity-temperature
  - u6-residual-resistivity
  - u6-thermal-resistivity-linear
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 13 Slides 10-17 and 22."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B35 — Conductivity, carriers and resistivity of metals

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 13, Slides 10-17 and 22.

## Q35.1 Resistance of a copper wire

- id: B35-Q1
- concept_id: u6-resistance-geometry
- format: numeric
- asks: calculation
- calc: 1.6e-8*50/(pi*(1.0e-3)**2)

Copper has a resistivity of 1.6 μΩ·cm at 0 °C. Determine the resistance at 0 °C of a copper wire 50 m long and 2.0 mm in diameter:

a) $2.55\times10^{-7}$ Ω
b) 0.0637 Ω
c) 0.255 Ω
d) 25.5 Ω

### Answer

c

### Explanation

$R = \rho\,l/A$ (Topic 6 note, Section 4) with $\rho = 1.6\ \mu\Omega\cdot\text{cm} = 1.6\times10^{-8}$ Ω·m (Session 13, Slide 14) and $A = \pi(1.0\times10^{-3})^2 = 3.14\times10^{-6}$ m²: $R = 1.6\times10^{-8}\cdot 50/3.14\times10^{-6} = 0.255$ Ω.

- a) The area was left in mm² ($3.14$ mm²) while $\rho$ was in Ω·m: $1.6\times10^{-8}\cdot 50/3.14 = 2.55\times10^{-7}$ Ω.
- b) The diameter was used as the radius, so the area is four times too large: $0.0637$ Ω.
- d) The centimetre of μΩ·cm was not converted: $1.6\times10^{-6}$ Ω·cm was taken as Ω·m, giving a value 100 times too large, $25.5$ Ω.

### Source

Session 13, Slide 14 (resistivity of copper at 0 °C); Topic 6 note, Section 4 ($R = \rho l/A$).

## Q35.2 Electron mobility of a hypothetical metal

- id: B35-Q2
- concept_id: u6-conductivity-carriers-mobility
- format: numeric
- asks: calculation
- calc: 1/(1.7e-8*8.5e28*q)

Determine the electron mobility of some hypothetical metal if it has $8.5\times10^{28}$ free electrons per m³ and a resistivity of $1.7\times10^{-8}$ Ω·m:

a) $6.92\times10^{-22}$ m²/(V·s)
b) $1.25\times10^{-18}$ m²/(V·s)
c) $4.32\times10^{-3}$ m²/(V·s)
d) $2.31\times10^{2}$ m²/(V·s)

### Answer

c

### Explanation

Session 13, Slides 12-13: $\sigma = n|q_e|\mu$ and $\sigma = 1/\rho$, so $\mu = 1/(\rho\,n\,|q_e|) = 1/(1.7\times10^{-8}\cdot 8.5\times10^{28}\cdot 1.6\times10^{-19}) = 4.32\times10^{-3}$ m²/(V·s).

- a) The electron charge was left out: $1/(\rho n) = 6.92\times10^{-22}$.
- b) The resistivity was used as if it were the conductivity: $\rho/(n|q_e|) = 1.25\times10^{-18}$.
- d) The formula was inverted: $\rho\,n\,|q_e| = 2.31\times10^{2}$ is the reciprocal of the mobility.

### Source

Session 13, Slides 12-13.

## Q35.3 What the conductivity of a metal depends on

- id: B35-Q3
- concept_id: u6-conductivity-carriers-mobility
- format: complete-sentence
- asks: definition

According to $\sigma = n|q_e|\mu$, the electrical conductivity of a metal depends on:

a) The number of free electrons per volume and their mobility
b) The number of electrons excited across the band gap
c) The number of holes created by acceptor dopants
d) The applied electric field, since $\sigma$ grows with $E$

### Answer

a

### Explanation

Session 13, Slide 13: in metals the carriers are the non-bonded electrons, and the conductivity depends on the number of electrons per volume unit and on their mobility.

- b) Excitation across a gap is the carrier mechanism of an intrinsic semiconductor (Slide 27), not of a metal.
- c) Holes from acceptors are the majority carriers of a p-type semiconductor (Slide 37).
- d) Confuses $\sigma$ with the current density: $J = \sigma E$ grows with the field, while $\sigma$ is a property of the material.

### Source

Session 13, Slides 12-13, 27 and 37.

## Q35.4 Lower mobility in a metal

- id: B35-Q4
- concept_id: u6-conductivity-carriers-mobility
- format: what-happens
- asks: effect
- check: 1/(0.5) == 2

What will happen to the resistivity of a metal if the mobility of its electrons is halved and their number stays the same:

a) It will be halved
b) It will stay the same
c) It will become four times larger
d) It will double

### Answer

d

### Explanation

Session 13, Slide 13: $\rho = 1/\sigma = 1/(n|q_e|\mu)$; with $n$ fixed, halving $\mu$ halves $\sigma$ and doubles $\rho$.

- a) The conductivity is halved, not the resistivity: $\sigma$ and $\rho$ were confused.
- b) Assumes that only the number of electrons matters; the mobility is the other factor of $\sigma$.
- c) The factor was squared, as if $\rho$ depended on $\mu^2$.

### Source

Session 13, Slides 12-13.

## Q35.5 Ionic conductors

- id: B35-Q5
- concept_id: u6-ionic-vs-electronic-conduction
- format: identify
- asks: classification

Which materials carry electric charge mainly by the movement of ions?

a) Aqueous electrolytes and some ceramics
b) Metals such as copper and aluminium
c) Intrinsic semiconductors such as silicon
d) Conductive polymers with delocalised electrons

### Answer

a

### Explanation

Session 13, Slide 10: the charge is carried either by ionic conductivity (aqueous electrolytes, some ceramics) or by electronic conductivity (metals).

- b) Metals conduct with the cloud of non-bonded electrons: electronic, not ionic conduction.
- c) Silicon conducts with electrons and holes (Slide 28), not with ions.
- d) The slide on conductive polymers names delocalised electrons as the mechanism (Slide 20), which is electronic conduction.

### Source

Session 13, Slides 10, 20 and 28.

## Q35.6 Ionic and electronic conduction

- id: B35-Q6
- concept_id: u6-ionic-vs-electronic-conduction
- format: false-statement
- asks: definition

Which one of the following statements about electrical conduction is FALSE?

a) In metals the charge is carried by non-bonded electrons
b) In ionic ceramics, ions move through vacancies or interstitial voids
c) For a metallic conductor, the current follows Ohm's law, $I = V/R$
d) In metals the charge is carried by ions moving through vacancies

### Answer

d

### Explanation

Session 13, Slides 10 and 13: metals conduct electronically, through the cloud of non-bonded electrons around the positive ions. Ions moving through vacancies is the ionic mechanism of some ceramics (Slide 22), so statement d) is false.

- a) True (Slide 13): in metals the carriers are the non-bonded electrons; marking it false confuses the two mechanisms.
- b) True (Slide 22): in conductive ceramics anions or cations move through vacancies or interstitial voids at high temperature.
- c) True (Slide 10): Ohm's law is the macroscopic law of the conduction in a metal.

### Source

Session 13, Slides 10, 13 and 22.

## Q35.7 Resistivity of a pure metal and temperature

- id: B35-Q7
- concept_id: u6-metal-conductivity-temperature
- format: cause-effect
- asks: effect

With an increase in temperature, the electrical resistivity of a pure metal:

a) Decreases, due to a larger number of free electrons
b) Increases, due to stronger vibrations of the atoms
c) Increases, due to a smaller number of free electrons
d) Stays constant, as only impurities scatter electrons

### Answer

b

### Explanation

Session 13, Slides 14 and 17: the thermal resistivity $\rho_T = \rho_0(1+\alpha_T\Delta T)$ grows linearly with temperature because the atoms vibrate and scatter the electrons, which lowers their mobility.

- a) Inverted trend with the semiconductor mechanism: more carriers with temperature is what happens in an intrinsic semiconductor (Slide 29).
- c) Right trend with the wrong reason: the number of free electrons of a metal does not change; the mobility does.
- d) Only the residual part is independent of temperature (Slide 16); the thermal part grows with it.

### Source

Session 13, Slides 14, 16, 17 and 29.

## Q35.8 A metal heated from 20 to 200 °C

- id: B35-Q8
- concept_id: u6-metal-conductivity-temperature
- format: true-statement
- asks: comparison

Which one of the following statements about a pure metal heated from 20 °C to 200 °C is TRUE?

a) Its mobility falls while its number of free electrons stays constant
b) Its number of free electrons rises and its mobility falls
c) Its mobility rises because the atoms vibrate more strongly
d) Its residual resistivity rises in proportion to the temperature

### Answer

a

### Explanation

Session 13, Slides 13-17 and 48: in a metal $n$ is fixed; heating makes the atoms vibrate, scatters the electrons and reduces their mobility, so $\sigma$ falls (the aluminium curve of Slide 48 is labelled "reducing mobility").

- b) Adds the semiconductor effect (more carriers with temperature) to the metal.
- c) Inverted: vibrations scatter the electrons and lower the mobility.
- d) The residual resistivity does not depend on temperature (Slide 16); only the thermal part grows.

### Source

Session 13, Slides 13-17 and 48.

## Q35.9 Residual resistivity

- id: B35-Q9
- concept_id: u6-residual-resistivity
- format: complete-sentence
- asks: definition

The residual resistivity $\rho_r$ of a metal is the part of its resistivity that:

a) Grows linearly with the temperature in °C
b) Comes from the vibrations of the lattice
c) Vanishes when the metal contains impurities
d) Comes from impurities and defects, independent of temperature

### Answer

d

### Explanation

Session 13, Slides 14 and 16: $\rho_{total} = \rho_T + \rho_r$; the residual resistivity does not depend on temperature and is produced by impurities or alloying elements ($\rho_i$) and structural imperfections ($\rho_d$).

- a) This describes the thermal resistivity $\rho_T = \rho_0(1+\alpha_T\Delta T)$.
- b) Lattice vibrations produce the thermal part, not the residual one.
- c) Inverted: impurities are one of the two sources of $\rho_r$, so they raise it.

### Source

Session 13, Slides 14 and 16.

## Q35.10 Meaning of rho zero

- id: B35-Q10
- concept_id: u6-thermal-resistivity-linear
- format: complete-sentence
- asks: definition

In the law $\rho_T = \rho_0(1+\alpha_T\,\Delta T)$ given in the course for metals, $\rho_0$ is:

a) The residual resistivity measured at 0 K
b) The resistivity of the metal at 0 °C
c) The resistivity of the metal at room temperature, 20 °C
d) The temperature coefficient of resistivity

### Answer

b

### Explanation

Session 13, Slide 14: $\rho_0$ is the resistivity at 0 °C (the table gives it in μΩ·cm for Al, Cu, Au, Fe and Ag) and $\alpha_T$ the temperature coefficient in °C⁻¹, so $\Delta T$ is the temperature in °C.

- a) The residual resistivity is the floor of the curve at low temperature, a different term of Matthiessen's rule.
- c) The reference of the table is 0 °C, not room temperature.
- d) That is $\alpha_T$, in °C⁻¹; $\rho_0$ is a resistivity in Ω·m.

### Source

Session 13, Slide 14.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
