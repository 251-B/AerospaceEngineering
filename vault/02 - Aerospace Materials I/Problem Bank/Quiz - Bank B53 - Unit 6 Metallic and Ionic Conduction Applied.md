---
materia: Aerospace Materials I
tema: "Unit 6: resistivity of metals applied to wires, strengthening strategies, ionic conductors, graphene and conductive polymers"
bank_id: B53
title: "Metallic and ionic conduction applied"
category: mt2_test_block
unit: 6
concepts:
  - u6-resistivity-match-temperature
  - u6-matthiessen-table-reading
  - u6-conductivity-from-n-mobility
  - u6-graphene-copper-ratio
  - u6-wire-strategy-weight
  - u6-wire-strategy-effects
  - u6-resistivity-coefficient-table
  - u6-copper-impurity-chart
  - u6-ionic-metal-temperature
  - u6-polymer-doping-scale
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 13 Slides 10-23."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B53 — Metallic and ionic conduction applied

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 13, Slides 10-23 (resistivity of metals, strengthening and conductivity, conductive ceramics, polymers and graphene).

## Q53.1 Gold and copper at the same resistivity

- id: B53-Q1
- concept_id: u6-resistivity-match-temperature
- format: numeric
- asks: calculation
- calc: (1.6*(1+0.0039*300)/2.3-1)/0.0034

At what temperature will a gold wire exhibit the same resistivity as a copper wire at 300 °C? Use $\rho_0 = 1.6$ μΩ·cm and $\alpha_T = 0.0039$ °C⁻¹ for copper, and $\rho_0 = 2.3$ μΩ·cm and $\alpha_T = 0.0034$ °C⁻¹ for gold:

a) 131 °C
b) 345 °C
c) 150 °C
d) 444 °C

### Answer

c

### Explanation

Session 13, Slide 14: $\rho_T = \rho_0(1+\alpha_T T)$. Copper at 300 °C: $\rho = 1.6\,(1+0.0039\cdot300) = 3.472$ μΩ·cm. For gold, $T = \dfrac{\rho/\rho_{0,Au}-1}{\alpha_{T,Au}} = \dfrac{3.472/2.3-1}{0.0034} = 150$ °C.

- a) The coefficient of copper (0.0039) was used for gold: $(3.472/2.3-1)/0.0039 = 131$ °C.
- b) The $\rho_0$ of gold was dropped from the denominator: $(3.472-2.3)/0.0034 = 345$ °C.
- d) The term 1 was forgotten: $3.472/(2.3\cdot0.0034) = 444$ °C, which is not the temperature for $\rho_T = \rho_0(1+\alpha_T T)$.

### Source

Session 13, Slide 14 and Slide 15 (same method, other metals and temperatures).

## Q53.2 Aluminium wire with residual resistivity

- id: B53-Q2
- concept_id: u6-matthiessen-table-reading
- format: numeric
- asks: calculation
- calc: 2.7*(1+0.0039*80)+0.35+0.20+0.10

An aluminium wire ($\rho_0 = 2.7$ μΩ·cm, $\alpha_T = 0.0039$ °C⁻¹) works at 80 °C. Its residual resistivity comes from the three defect sources of the table. Determine its total resistivity:

| Source of residual resistivity | Contribution (μΩ·cm) |
| :--- | :---: |
| Alloying atoms in solid solution | 0.35 |
| Dislocations from cold work | 0.20 |
| Grain boundaries | 0.10 |

a) 4.19 μΩ·cm
b) 3.54 μΩ·cm
c) 3.89 μΩ·cm
d) 4.40 μΩ·cm

### Answer

a

### Explanation

Session 13, Slide 14 (Matthiessen's rule) and Slide 16: $\rho_{total} = \rho_T + \rho_r$ with $\rho_T = 2.7\,(1+0.0039\cdot80) = 3.542$ μΩ·cm and $\rho_r = 0.35+0.20+0.10 = 0.65$ μΩ·cm, so $\rho_{total} = 4.19$ μΩ·cm.

- b) The residual term was left out: only the thermal part, $3.54$ μΩ·cm.
- c) Only the alloying atoms were added: $3.542+0.35 = 3.89$ μΩ·cm; dislocations and grain boundaries also scatter the electrons (Slide 16).
- d) The residual term was multiplied by $(1+\alpha_T T)$ as well: $3.542 + 0.65\cdot1.312 = 4.40$ μΩ·cm; $\rho_r$ does not depend on temperature.

### Source

Session 13, Slides 14 and 16.

## Q53.3 A hypothetical metal against copper

- id: B53-Q3
- concept_id: u6-conductivity-from-n-mobility
- format: numeric
- asks: calculation
- calc: 6.0e28*q*5.0e-3/0.60e8

A hypothetical metal has $n = 6.0\times10^{28}$ free electrons per m³ and an electron mobility $\mu = 5.0\times10^{-3}$ m²/(V·s). With $\sigma_{Cu} = 0.60\times10^{8}$ (Ω·m)⁻¹, determine the ratio $\sigma/\sigma_{Cu}$:

a) 0.50
b) 1.25
c) 1.60
d) 0.80

### Answer

d

### Explanation

Session 13, Slides 13 and 21: $\sigma = n|q_e|\mu = 6.0\times10^{28}\cdot1.602\times10^{-19}\cdot5.0\times10^{-3} = 4.81\times10^{7}$ (Ω·m)⁻¹, and $4.81\times10^{7}/0.60\times10^{8} = 0.80$. Units: m⁻³ · C · m²/(V·s) = (Ω·m)⁻¹.

- a) The conductivity was compared with that of graphene, $0.96\times10^{8}$ (Ω·m)⁻¹: $4.81\times10^{7}/0.96\times10^{8} = 0.50$.
- b) The ratio was inverted: $\sigma_{Cu}/\sigma = 1.25$.
- c) The charge was counted twice, as if each atom gave two electrons that also carried a double charge: $2\cdot0.80 = 1.60$.

### Source

Session 13, Slides 13 and 21.

## Q53.4 Resistivity of copper and graphene

- id: B53-Q4
- concept_id: u6-graphene-copper-ratio
- format: numeric
- asks: comparison
- calc: (0.96/0.60-1)*100

The conductivities of two materials are given in the table. Compared with that of graphene, the resistivity of copper is higher by:

| Material | $\sigma$ ((Ω·m)⁻¹) |
| :--- | :---: |
| Graphene | $0.96\times10^{8}$ |
| Copper | $0.60\times10^{8}$ |
| Silicon | $4.5\times10^{-4}$ |

a) 37.5 %
b) 60 %
c) 62.5 %
d) 160 %

### Answer

b

### Explanation

Session 13, Slide 21: $\rho = 1/\sigma$, so $\rho_{Cu}/\rho_{gr} = \sigma_{gr}/\sigma_{Cu} = 0.96/0.60 = 1.60$: the resistivity of copper is 60 % higher.

- a) The percentage by which the conductivity of copper is lower, $(0.96-0.60)/0.96 = 37.5$ %, was given instead of the rise of the resistivity.
- c) The inverse ratio $\sigma_{Cu}/\sigma_{gr} = 0.625$ was written as a percentage.
- d) The ratio 1.60 was written as 160 % instead of the excess over 100 %.

### Source

Session 13, Slide 21.

## Q53.5 Lighter wire with the same strength and conductivity

- id: B53-Q5
- concept_id: u6-wire-strategy-weight
- format: cause-effect
- asks: application

To reduce the weight of an aluminium alloy wire (a thinner wire) while keeping its tensile strength and its conductivity, the best strategy is:

a) Alloying with a more conductive metal such as copper
b) Cold drawing with a high percentage of cold work
c) Increasing the grain size by heat treatment
d) Lowering the working temperature of the wire

### Answer

d

### Explanation

Problems T6 and T7, Problem 2 (Slides 18-19): lowering the temperature raises the conductivity (lower $\rho_T$) and the strength, so a thinner wire can carry the same current with the same load. The official table for this wire gives: alloying, conductivity decreases and strength increases; lower temperature, conductivity increases and strength increases more; larger grains, conductivity increases and strength decreases; precipitation and cold work, conductivity decreases and strength increases.

- a) Alloying atoms raise the strength but also $\rho_i$, so the conductivity falls (Slide 16).
- b) Cold work raises the strength through dislocations, which scatter electrons and lower the conductivity (Slide 18).
- c) Fewer grain boundaries improve the conductivity, but the strength falls with the larger grain.

### Source

Problems T6 and T7, Problem 2; Session 13, Slides 16, 18 and 19.

## Q53.6 Intermetallic precipitation in a wire

- id: B53-Q6
- concept_id: u6-wire-strategy-effects
- format: what-happens
- asks: effect

What will happen to the conductivity and the tensile strength of an aluminium alloy wire after a treatment that causes intermetallic precipitation?

a) The conductivity decreases and the strength increases
b) The conductivity and the strength both decrease
c) The conductivity increases and the strength decreases
d) The conductivity and the strength both increase

### Answer

a

### Explanation

Problems T6 and T7, Problem 2, part d; Slides 16 and 18: the particles hinder the dislocations (higher strength) and also scatter the electrons, so the residual resistivity grows and the conductivity falls. All hardening methods lower $\sigma$ to a greater or lesser extent.

- c) This is the effect of grain growth: fewer boundaries, higher conductivity, lower strength.
- b) Defects do lower the conductivity, but they obstruct slip, so the strength does not fall.
- d) This pair belongs to a lower working temperature; precipitates add scattering centres and cannot improve the conductivity.

### Source

Problems T6 and T7, Problem 2; Session 13, Slides 16 and 18.

## Q53.7 Coefficients of resistivity from a table

- id: B53-Q7
- concept_id: u6-resistivity-coefficient-table
- format: diagram-reading
- asks: comparison

Using the data of the table, determine which wire has the smallest absolute increase of resistivity, in μΩ·cm, when it is heated from 0 °C to 100 °C:

| Metal | $\rho_0$ at 0 °C (μΩ·cm) | $\alpha_T$ (°C⁻¹) |
| :--- | :---: | :---: |
| Aluminium | 2.7 | 0.0039 |
| Copper | 1.6 | 0.0039 |
| Gold | 2.3 | 0.0034 |
| Silver | 1.47 | 0.0038 |

a) Gold
b) Copper
c) Silver
d) Aluminium

### Answer

c

### Explanation

Session 13, Slide 14: $\Delta\rho = \rho_0\alpha_T\,\Delta T$. For $\Delta T = 100$ °C: Al 1.05, Cu 0.62, Au 0.78 and Ag 0.56 μΩ·cm; silver has the smallest increase because its $\rho_0$ is the lowest of the four and its $\alpha_T$ is almost that of copper.

- a) Gold has the smallest $\alpha_T$ (0.0034), but the increase also depends on $\rho_0$: 0.78 μΩ·cm.
- b) Copper was chosen as the best-known conductor without computing; it gives 0.62 μΩ·cm, above silver.
- d) Aluminium has the largest $\rho_0$, which was taken to mean less sensitivity to temperature; it gives the largest increase, 1.05 μΩ·cm.

### Source

Session 13, Slide 14.

## Q53.8 Impurities in copper

- id: B53-Q8
- concept_id: u6-copper-impurity-chart
- format: diagram-reading
- asks: figure-reading

From the shown chart, indicate which element raises the room-temperature resistivity of copper the most when 0.10 weight percent of it is added:

![[attachments/MAT-MT2/u6-b53-cu-impurity.svg]]

a) Pb
b) Fe
c) Al
d) Ag

### Answer

b

### Explanation

Session 13, Slide 16: the impurity resistivity $\rho_i$ grows with the amount of added element, and the slope depends on the element. At 0.10 wt% the iron line is the highest of the four, roughly twice as far above the starting resistivity as the others.

- a) The lead line was read as the steepest because lead is the heaviest atom; the chart shows a gentle slope.
- c) The aluminium line is the second one in the chart, well below the iron line.
- d) The silver line is the flattest one: silver added to copper hardly changes its resistivity.

### Source

Session 13, Slide 16.

## Q53.9 Ionic ceramic and metal when heated

- id: B53-Q9
- concept_id: u6-ionic-metal-temperature
- format: what-happens
- asks: effect

With an increase in temperature, the electrical conductivity of an ionic ceramic and that of a metal, respectively:

a) Increases and increases
b) Decreases and increases
c) Increases and decreases
d) Decreases and decreases

### Answer

c

### Explanation

Session 13, Slides 14 and 22 (Problem 3): in a metal, a higher temperature increases $\rho_T$ and the conductivity falls. In an ionic ceramic the charge is carried by ions that move through vacancies or interstitial voids at high temperatures (Slide 22), so heating makes this movement easier and $\sigma$ increases. The statement that the ions hop more easily when heated is an **extension** of the slide wording.

- a) Both were treated as thermally activated; the metal has a fixed number of electrons and only more collisions.
- b) The two behaviours were swapped.
- d) The metal trend was applied to both materials, ignoring that ions need thermal energy to move.

### Source

Session 13, Slides 14 and 22; Problems T6 and T7, Problem 3.

## Q53.10 Doping a conductive polymer

- id: B53-Q10
- concept_id: u6-polymer-doping-scale
- format: complete-sentence
- asks: application

An undoped conductive polymer has $\sigma = 10^{-12}$ S/cm and, after doping, $10^{3}$ S/cm. On the conductivity scale of the polymers, it passes from the range of:

a) Semiconductors to that of insulators
b) Insulators to that of semiconductors
c) Metallic conductors to that of insulators
d) Insulators to that of metallic conductors

### Answer

d

### Explanation

Session 13, Slide 20: conducting polymers go from the uncharged (undoped) to the charged (doped) state along the scale; $10^{-12}$ S/cm lies in the insulator range ($10^{-18}$ to about $10^{-6}$ S/cm) and $10^{3}$ S/cm in the range of metallic conductors (to the right of the second dotted line of the scale).

- a) The two ranges were swapped and the sample taken as a semiconductor before doping.
- b) The final value was placed in the semiconductor band, whose upper limit is far below $10^{3}$ S/cm.
- c) The direction was inverted: doping raises the conductivity.

### Source

Session 13, Slide 20.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
