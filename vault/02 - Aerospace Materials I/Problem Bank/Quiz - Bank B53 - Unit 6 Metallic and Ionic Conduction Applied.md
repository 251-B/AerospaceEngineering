---
materia: Aerospace Materials I
tema: "Unit 6: resistivity of metals applied to wires, strengthening strategies, ionic conductors, graphene and conductive polymers"
bank_id: B53
title: "Metallic and ionic conduction applied"
category: mt2_test_block
unit: 6
concepts:
  - u6-thermal-resistivity-linear
  - u6-defects-resistivity
  - u6-conductivity-from-n-mobility
  - u6-polymers-graphene
  - u6-wire-strategy-weight
  - u6-wire-strategy-effects
  - u6-resistivity-coefficient-table
  - u6-copper-impurity-chart
  - u6-ionic-metal-temperature
  - u6-polymer-doping-scale
difficulty: 2
origen: "Includes Question 5 of MATERIALS_FINALEXAM_2012_EXTRA.pdf alongside practice items in the style of Part I. Content and data from Session 13 Slides 10-23."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B53 — Metallic and ionic conduction applied

> [!info] Includes official exam questions
> Ten test questions in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Question 2 adapts Question 5 of MATERIALS_FINALEXAM_2012_EXTRA.pdf; the remaining nine are practice items. Content: Session 13, Slides 10-23 (resistivity of metals, strengthening and conductivity, conductive ceramics, polymers and graphene).

## Q53.1 Thermal resistivity of pure metals

- id: B53-Q1
- concept_id: u6-thermal-resistivity-linear
- format: topic-true
- asks: comparison

Referring to the linear thermal resistivity relation $\rho_T = \rho_0(1+\alpha_T\,\Delta T)$ for pure metals such as copper and aluminium, indicate which statement is TRUE:

a) The reference resistivity $\rho_0$ is measured at 0 K, so $\Delta T$ must be entered in kelvin
b) Two metals with different $\rho_0$ and $\alpha_T$ can reach equal resistivities if held at different temperatures
c) Thermal resistivity $\rho_T$ decreases linearly on heating because lattice vibrations lose amplitude
d) Dissolving alloying elements changes $\alpha_T$ strongly while keeping the residual resistivity $\rho_r$ equal to zero

### Answer

b

### Explanation

Session 13, Slides 14-15: since $\rho_T = \rho_0(1+\alpha_T\Delta T)$ increases linearly with temperature at a rate $\rho_0\alpha_T$, a better conductor at 0 °C (such as silver or copper) can reach the same resistivity as a higher-$\rho_0$ metal when heated to a higher temperature.

- a) In the course relation $\rho_0$ is tabulated at 0 °C and $\Delta T$ is measured in degrees Celsius, not from 0 K.
- c) Inverts the trend: heating raises thermal vibration amplitude, increasing electron scattering and $\rho_T$.
- d) Inverts Matthiessen's rule: alloying elements keep the temperature slope nearly parallel while adding a positive residual term $\rho_i$ (Slides 16-17).

### Source

Session 13, Slides 14-17.

## Q53.2 Defects and electrical conductivity in metals

- id: B53-Q2
- concept_id: u6-defects-resistivity
- format: topic-true
- asks: effect
- origin: official-exam

Referring to point defects, dislocations and grain boundaries in a metallic conductor, indicate which statement is TRUE:

a) Vacancies and solute atoms leave residual resistivity unchanged whenever the solute shares the host valence
b) Dislocations act as conductive channels that guide free electrons and lower metallic resistivity
c) Grain boundaries affect the thermal resistivity $\rho_T$ and vanish from Matthiessen's rule below 0 °C
d) Lattice imperfections break crystal periodicity, scatter conduction electrons, reduce mobility and lower conductivity

### Answer

d

### Explanation

MATERIALS_FINALEXAM_2012_EXTRA.pdf, p. 2 (Question 5) and Session 13, Slides 16-17: in a metal, conduction electrons move without scattering only in a perfect periodic lattice; point defects (vacancies, impurities/solutes) and structural defects (dislocations, grain boundaries) distort periodicity, scatter electrons, shorten the mean free time $\tau$, reduce mobility $\mu$ and therefore lower conductivity (raising $\rho_r = \rho_i + \rho_d$).

- a) Any foreign atom or vacancy disturbs the periodic crystal potential around it and increases scattering regardless of valence.
- b) Dislocations obstruct and scatter conduction electrons rather than guiding them, raising $\rho_d$.
- c) Grain boundaries belong to the temperature-independent residual deformation resistivity $\rho_d$, which persists down to 0 K.

### Source

MATERIALS_FINALEXAM_2012_EXTRA.pdf, p. 2 (Question 5); Session 13, Slides 16-17.

## Q53.3 Conductivity from electron density and mobility

- id: B53-Q3
- concept_id: u6-conductivity-from-n-mobility
- format: numeric
- asks: calculation
- calc: 6.0e28*q*5.0e-3

A metallic conductor has $6.0\times10^{28}$ free electrons per m³ and an electron mobility of $5.0\times10^{-3}$ m²/(V·s). Using $|q_e| = 1.602\times10^{-19}$ C, determine its electrical conductivity:

a) $4.81\times10^{7}$ (Ω·m)⁻¹
b) $3.00\times10^{26}$ (Ω·m)⁻¹
c) $2.08\times10^{-8}$ (Ω·m)⁻¹
d) $9.61\times10^{7}$ (Ω·m)⁻¹

### Answer

a

### Explanation

Session 13, Slides 12-13: $\sigma = n|q_e|\mu = 6.0\times10^{28}\cdot1.602\times10^{-19}\cdot5.0\times10^{-3} = 4.81\times10^{7}$ (Ω·m)⁻¹. Units: $\text{m}^{-3}\cdot\text{C}\cdot\text{m}^2/(\text{V}\cdot\text{s}) = \text{A}/(\text{V}\cdot\text{m}) = (\Omega\cdot\text{m})^{-1}$.

- b) The elementary charge $|q_e|$ was omitted: $n\mu = 6.0\times10^{28}\cdot5.0\times10^{-3} = 3.00\times10^{26}$.
- c) The resistivity $\rho = 1/\sigma = 2.08\times10^{-8}$ Ω·m was computed instead of the conductivity.
- d) The charge was doubled ($2|q_e|$), giving $9.61\times10^{7}$ (Ω·m)⁻¹.

### Source

Session 13, Slides 12-13.

## Q53.4 Non-metallic conductors compared with copper

- id: B53-Q4
- concept_id: u6-polymers-graphene
- format: topic-false
- asks: comparison

Regarding non-metallic conductors such as graphene and conductive polymers compared with copper, indicate which statement is FALSE:

a) Graphene is a single hexagonal carbon sheet whose delocalised $\pi$ electrons give higher conductivity than copper
b) Conductive polymers transport charge by delocalised electron exchange between neighbouring redox sites and offer flexibility
c) Graphite conducts better across its stacked layers than graphene because interlayer spacing multiplies electron speed
d) Undoped polymers behave as electrical insulators until chemical doping creates mobile charge carriers

### Answer

c

### Explanation

Session 13, Slides 20-21: graphene is a single hexagonal carbon sheet with a huge delocalised $\pi$-electron cloud moving at very high speed, giving higher conductivity than copper ($0.96\times10^{8}$ vs $0.60\times10^{8}$ (Ω·m)⁻¹); graphite is a multi-layer stack and does not outperform single-layer graphene across layers. Statement c) is false.

- a) True (Slide 21): graphene exceeds copper in conductivity via its delocalised $\pi$ cloud.
- b) True (Slide 20): conductive polymers combine flexibility and easy formability with electron exchange between redox sites.
- d) True (Slide 20): undoped polymers lie in the insulator band and jump into the conductive range upon doping.

### Source

Session 13, Slides 20-21.

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
