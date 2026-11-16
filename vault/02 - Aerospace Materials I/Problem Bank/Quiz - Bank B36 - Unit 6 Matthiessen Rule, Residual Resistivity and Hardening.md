---
materia: Aerospace Materials I
tema: "Unit 6: thermal resistivity of metals, Matthiessen's rule, residual resistivity, hardening and defects"
bank_id: B36
title: "Matthiessen's rule, residual resistivity and hardening"
category: mt2_test_block
unit: 6
concepts:
  - u6-thermal-resistivity-linear
  - u6-matthiessen-sum
  - u6-residual-resistivity
  - u6-metal-conductivity-temperature
  - u6-hardening-conductivity
  - u6-defects-resistivity
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 13 Slides 14-18; the chart of question 5 is the official figure of Slide 17."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B36 — Matthiessen's rule, residual resistivity and hardening

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 13, Slides 14-18.

## Q36.1 Resistivity of gold at 150 °C

- id: B36-Q1
- concept_id: u6-thermal-resistivity-linear
- format: numeric
- asks: calculation
- calc: 2.3*(1+0.0034*150)

Gold has $\rho_0 = 2.3$ μΩ·cm at 0 °C and $\alpha_T = 0.0034$ °C⁻¹. Determine its resistivity at 150 °C:

a) 1.17 μΩ·cm
b) 2.81 μΩ·cm
c) 3.47 μΩ·cm
d) 5.61 μΩ·cm

### Answer

c

### Explanation

Session 13, Slide 14: $\rho_T = \rho_0(1+\alpha_T\Delta T)$ with $\Delta T$ in °C from 0 °C: $\rho = 2.3\,(1 + 0.0034\cdot150) = 2.3\cdot1.51 = 3.47$ μΩ·cm.

- a) The "1 +" was dropped: $2.3\cdot0.0034\cdot150 = 1.17$ μΩ·cm is only the increase, not the resistivity.
- b) The coefficient was added instead of multiplied: $2.3 + 0.0034\cdot150 = 2.81$.
- d) The temperature was put in kelvin: $2.3\,(1 + 0.0034\cdot423) = 5.61$ μΩ·cm; $\rho_0$ is the value at 0 °C, so $\Delta T$ is in °C.

### Source

Session 13, Slide 14 (law and table of resistivities).

## Q36.2 Ranking metals by resistivity

- id: B36-Q2
- concept_id: u6-thermal-resistivity-linear
- format: ordering
- asks: comparison

Order the following metals from the lowest to the highest resistivity at 0 °C:

a) Silver < copper < aluminium < iron
b) Copper < silver < aluminium < iron
c) Iron < aluminium < copper < silver
d) Silver < copper < iron < aluminium

### Answer

a

### Explanation

Session 13, Slide 14 (table at 0 °C): Ag 1.47, Cu 1.6, Al 2.7 and Fe 9 μΩ·cm.

- b) Silver and copper are swapped: copper (1.6) is slightly more resistive than silver (1.47).
- c) Fully reversed order: this ranks the metals by conductivity, $\sigma = 1/\rho$.
- d) Iron and aluminium are swapped: iron (9 μΩ·cm) is more than three times as resistive as aluminium (2.7).

### Source

Session 13, Slide 14.

## Q36.3 Total resistivity of a deformed alloy

- id: B36-Q3
- concept_id: u6-matthiessen-sum
- format: numeric
- asks: calculation
- calc: 1.6*(1+0.0039*100)+1.4+0.3

A cold-worked Cu-Ni alloy at 100 °C has $\rho_i = 1.4$ μΩ·cm and $\rho_d = 0.3$ μΩ·cm. With $\rho_0 = 1.6$ μΩ·cm and $\alpha_T = 0.0039$ °C⁻¹ for copper, determine its total resistivity:

a) 3.30 μΩ·cm
b) 3.92 μΩ·cm
c) 4.59 μΩ·cm
d) 5.63 μΩ·cm

### Answer

b

### Explanation

Matthiessen's rule (Session 13, Slides 14 and 16): $\rho = \rho_T + \rho_i + \rho_d$. The thermal part is that of copper (the curves of Slide 17 are parallel): $\rho_T = 1.6\,(1+0.0039\cdot100) = 2.22$ μΩ·cm, so $\rho = 2.22 + 1.4 + 0.3 = 3.92$ μΩ·cm.

- a) The value at 0 °C, $\rho_0 = 1.6$, was used for the thermal part: $1.6 + 1.4 + 0.3 = 3.30$.
- c) The temperature factor was applied to the residual terms too: $(1.6+1.4+0.3)\cdot1.39 = 4.59$; $\rho_i$ and $\rho_d$ do not depend on temperature.
- d) The temperature was put in kelvin: $1.6\,(1+0.0039\cdot373) + 1.7 = 5.63$.

### Source

Session 13, Slides 14, 16 and 17.

## Q36.4 Matthiessen's rule

- id: B36-Q4
- concept_id: u6-matthiessen-sum
- format: true-statement
- asks: definition

Which one of the following statements about Matthiessen's rule for metals is TRUE?

a) The total resistivity is the product of its thermal and residual parts
b) The impurity term grows linearly with the temperature
c) The deformation term disappears at low temperature
d) The total resistivity is the sum of thermal, impurity and deformation terms

### Answer

d

### Explanation

Session 13, Slides 14 and 16: $\rho_{total} = \rho_T + \rho_r = \rho_T + \rho_i + \rho_d$, a sum of independent contributions.

- a) The contributions add, they do not multiply.
- b) The impurity term is part of the residual resistivity, which does not depend on temperature (Slide 16).
- c) Inverted: at low temperature the thermal part vanishes and the residual part, deformation included, is what remains (the floor of the curve, Slide 14).

### Source

Session 13, Slides 14 and 16.

## Q36.5 Reading the copper-nickel chart

- id: B36-Q5
- concept_id: u6-residual-resistivity
- format: diagram-reading
- asks: figure-reading

From the shown chart of copper and copper-nickel alloys, indicate the residual resistivity of the Cu + 1.12 at% Ni alloy:

![[attachments/T6/s13-matthiessen-copper.png]]

a) $0.9\times10^{-8}$ Ω·m
b) $1.4\times10^{-8}$ Ω·m
c) $2.6\times10^{-8}$ Ω·m
d) $3.0\times10^{-8}$ Ω·m

### Answer

b

### Explanation

Session 13, Slides 14 and 17: the residual resistivity is the value that remains when the thermal part vanishes, at the low-temperature end of the curve. The Cu + 1.12 at% Ni curve flattens at about $1.4\times10^{-8}$ Ω·m near −270 °C (reading of the chart).

- a) $0.9\times10^{-8}$ Ω·m is the thermal part $\rho_t$ of pure copper at −100 °C marked on the chart, not a residual value.
- c) $2.6\times10^{-8}$ Ω·m is the floor of the neighbouring curve, Cu + 2.16 at% Ni.
- d) $3.0\times10^{-8}$ Ω·m is the total resistivity of the Cu + 1.12 at% Ni alloy at 0 °C, thermal part included.

### Source

Session 13, Slide 17 (chart of resistivity against temperature for copper and Cu-Ni alloys); Slide 14 (residual component).

## Q36.6 Nickel content and resistivity

- id: B36-Q6
- concept_id: u6-residual-resistivity
- format: cause-effect
- asks: cause

With an increase in the nickel content of a copper alloy, its residual resistivity:

a) Decreases, as nickel adds free electrons
b) Increases, as nickel raises the lattice vibrations
c) Increases, as the foreign atoms distort the lattice
d) Stays constant, as only dislocations add to it

### Answer

c

### Explanation

Session 13, Slides 16-17: $\rho_r$ increases with the degree of distortion of the lattice; each foreign atom breaks the periodicity and scatters the electrons, so more nickel gives a higher, parallel curve.

- a) Inverted trend; the slides give no change in the number of free electrons, only scattering by the impurity.
- b) Right trend with the wrong cause: lattice vibrations are the thermal part, which the chart shows to be the same for all the alloys.
- d) Impurities ($\rho_i$) are one of the two sources of the residual resistivity, together with structural imperfections ($\rho_d$).

### Source

Session 13, Slides 16-17.

## Q36.7 Why a heated metal conducts less

- id: B36-Q7
- concept_id: u6-metal-conductivity-temperature
- format: identify
- asks: cause

Which mechanism lowers the electrical conductivity of a pure metal when it is heated?

a) Scattering of electrons by vibrating atoms
b) Scattering of electrons by impurity atoms
c) A fall in the number of free electrons
d) The opening of a gap above the Fermi level

### Answer

a

### Explanation

Session 13, Slide 17: in a crystal heated to a high temperature the atoms vibrate and displace from their sites, scatter the electrons and reduce their mobility, so the conductivity falls.

- b) Impurity scattering exists, but it does not depend on temperature (residual resistivity, Slide 16), so it cannot explain the change on heating.
- c) The number of free electrons of a metal stays constant; the mobility changes.
- d) The band structure of a metal keeps empty states just above $E_f$ (Slide 6); no gap opens on heating.

### Source

Session 13, Slides 6, 16 and 17.

## Q36.8 Hardening and conductivity

- id: B36-Q8
- concept_id: u6-hardening-conductivity
- format: complete-sentence
- asks: effect

According to the course, all hardening methods of metals, to a greater or lesser extent:

a) Increase the electrical conductivity
b) Leave the electrical conductivity unchanged
c) Decrease the electrical conductivity
d) Increase the conductivity and decrease the strength

### Answer

c

### Explanation

Session 13, Slide 18: "all hardening methods cause, to a greater or lesser extent, a decrease of the conductivity". The obstacles that stop dislocations (solute atoms, dislocations, boundaries, precipitates) also scatter the electrons.

- a) Inverted effect: the obstacles scatter electrons and raise the resistivity.
- b) Ignores the scattering by the defects and solute atoms introduced by hardening (residual resistivity, Slide 16).
- d) Describes a softening treatment, the opposite of hardening, and reverses both properties.

### Source

Session 13, Slides 16 and 18.

## Q36.9 Strengthening copper and keeping its conductivity

- id: B36-Q9
- concept_id: u6-hardening-conductivity
- format: complete-sentence
- asks: application

Copper is strengthened with the smallest loss of electrical conductivity by:

a) Adding zinc in solid solution
b) Raising its working temperature
c) Adding nickel in solid solution
d) Cold working it

### Answer

d

### Explanation

Session 13, Slide 18: with cold work the yield strength rises strongly while the conductivity falls only slightly; with zinc in solution the strength rises moderately but the conductivity falls sharply.

- a) Zinc in solid solution is the case of the slide in which the conductivity falls sharply.
- b) A higher temperature does not strengthen the metal and it raises the thermal resistivity (Slide 14).
- c) Nickel is also a solute: each at% raises the residual resistivity of copper strongly (Slides 16-17), as zinc does.

### Source

Session 13, Slides 14, 16-18.

## Q36.10 Defects and resistivity

- id: B36-Q10
- concept_id: u6-defects-resistivity
- format: false-statement
- asks: cause

Which one of the following statements about the resistivity of a metal is FALSE?

a) Grain boundaries add to the deformation resistivity $\rho_d$
b) Dislocations lower the resistivity by easing electron flow
c) Foreign atoms, larger or smaller than the host, raise the resistivity
d) Pure copper and Cu-Ni alloys have the same thermal part $\rho_T$

### Answer

b

### Explanation

Session 13, Slides 16-17: dislocations break the periodicity of the crystal and scatter the electrons, so they raise the resistivity (deformation term $\rho_d$). Statement b) is false.

- a) True: structural imperfections such as dislocations and grain boundaries give the deformation resistivity (Slide 16).
- c) True: a foreign atom, large or small, distorts the lattice around it and raises $\rho_r$ (Slide 16).
- d) True: the curves of the slide are parallel, separated by constant residual terms, with the same temperature component (Slide 17).

### Source

Session 13, Slides 16-17.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
