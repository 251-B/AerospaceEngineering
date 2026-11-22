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
  - u6-hardening-conductivity
  - u6-defects-resistivity
difficulty: 2
origen: "Includes Questions from MATERIALS_FINALEXAM_2017_ORD.pdf (Q6) and MATERIALS_FINALEXAM_2015_EXTRA.pdf (Q8a) alongside practice items. Content and data from Session 13 Slides 14-18; the chart of question 5 is the official figure of Slide 17."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B36 — Matthiessen's rule, residual resistivity and hardening

> [!info] Includes official exam questions
> Ten test questions in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Questions 3 and 7 adapt Questions from MATERIALS_FINALEXAM_2017_ORD.pdf (Q6) and MATERIALS_FINALEXAM_2015_EXTRA.pdf (Q8a); the rest are practice items. Content: Session 13, Slides 14-18.

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

## Q36.3 Residual resistivity in Matthiessen's rule

- id: B36-Q3
- concept_id: u6-residual-resistivity
- format: topic-true
- asks: cause
- origin: official-exam

Regarding the residual resistivity $\rho_r$ in Matthiessen's rule for a metallic conductor, indicate which statement is TRUE:

a) It originates from thermal lattice vibrations and rises linearly above 0 °C
b) It disappears completely once solute atoms are dissolved into solid solution
c) It decreases whenever cold plastic deformation increases dislocation density
d) It is temperature-independent and arises from lattice distortion by impurities and structural defects

### Answer

d

### Explanation

Session 13, Slides 14 and 16 (MATERIALS_FINALEXAM_2017_ORD.pdf, Q6): in Matthiessen's rule $\rho_{\text{total}} = \rho_T + \rho_r$, the residual resistivity $\rho_r = \rho_i + \rho_d$ does not depend on temperature and depends on the concentration and type of impurities/alloying elements and structural imperfections (dislocations, grain boundaries) that distort the crystal lattice.

- a) Describes the thermal part $\rho_T = \rho_0(1+\alpha_T\Delta T)$, not the residual part $\rho_r$.
- b) Inverts the impurity effect: dissolved solute atoms distort the lattice and raise $\rho_i$, adding to $\rho_r$.
- c) Inverts the deformation effect: dislocations scatter electrons and raise $\rho_d$, increasing $\rho_r$.

### Source

MATERIALS_FINALEXAM_2017_ORD.pdf, p. 4 (Question 6); Session 13, Slides 14 and 16.

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

a) Decreases, as nickel adds more free electrons to the metal
b) Increases, as nickel raises the lattice vibrations
c) Increases, as the foreign atoms distort the lattice
d) Stays constant, as it is set by the dislocation density

### Answer

c

### Explanation

Session 13, Slides 16-17: $\rho_r$ increases with the degree of distortion of the lattice; each foreign atom breaks the periodicity and scatters the electrons, so more nickel gives a higher, parallel curve.

- a) Inverted trend; the slides give no change in the number of free electrons, only scattering by the impurity.
- b) Right trend with the wrong cause: lattice vibrations are the thermal part, which the chart shows to be the same for all the alloys.
- d) Takes the dislocations as the only source: impurities ($\rho_i$) are one of the two sources of the residual resistivity, together with structural imperfections ($\rho_d$).

### Source

Session 13, Slides 16-17.

## Q36.7 Temperature and defect effects on metallic resistivity

- id: B36-Q7
- concept_id: u6-matthiessen-sum
- format: topic-true
- asks: effect
- origin: official-exam

Referring to Matthiessen's rule and how metallic electrical resistivity responds to temperature, impurities and structural defects, indicate which statement is TRUE:

a) Higher temperature raises $\rho_T$ via lattice vibrations, while alloying, dislocations and grain boundaries add to $\rho_r$
b) Impurities and grain boundaries raise the thermal term $\rho_T$, while temperature sets the residual term $\rho_r$
c) Cold working lowers resistivity by aligning grains, whereas alloying additions raise resistivity above 0 °C
d) Higher temperature lowers metallic resistivity by freeing more electrons, whereas defects leave resistivity unchanged

### Answer

a

### Explanation

MATERIALS_FINALEXAM_2015_EXTRA.pdf, p. 9 (Question 8a) and Session 13, Slides 14 and 16-17: total metallic resistivity is $\rho_{\text{total}} = \rho_T + \rho_i + \rho_d$. Raising temperature increases $\rho_T$ because thermal atomic vibrations scatter electrons, while impurities, alloying elements, dislocations and grain boundaries increase the temperature-independent residual contributions $\rho_i$ and $\rho_d$.

- b) Swaps the thermal and residual mechanisms: temperature enters $\rho_T$, whereas alloying and defects enter $\rho_r$.
- c) Cold work raises resistivity through dislocation scattering ($\rho_d$), and alloying raises $\rho_i$ at all temperatures.
- d) Applies intrinsic-semiconductor behaviour to metals while falsely claiming defects have no scattering effect.

### Source

MATERIALS_FINALEXAM_2015_EXTRA.pdf, p. 9 (Question 8a); Session 13, Slides 14 and 16-17.

## Q36.8 Hardening and conductivity

- id: B36-Q8
- concept_id: u6-hardening-conductivity
- format: complete-sentence
- asks: effect

All hardening methods applied to metallic alloys, to a greater or lesser extent:

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
