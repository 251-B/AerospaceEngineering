---
materia: Aerospace Materials I
tema: "Unit 6: dopants of silicon and germanium, ionisation energies, p-type conductivity and the temperature ranges of extrinsic semiconductors"
bank_id: B40
title: "Dopant levels and extrinsic conductivity with temperature"
category: mt2_test_block
unit: 6
concepts:
  - u6-dopant-type
  - u6-p-type-conductivity-calc
  - u6-donor-acceptor-levels
  - u6-dopant-ionisation-energy
  - u6-extrinsic-slopes
  - u6-extrinsic-to-intrinsic
  - u6-extrinsic-temperature-regions
difficulty: 2
origen: "Includes Question 5 of MATERIALS_SECONDPARTIAL_2019.pdf (and 2018) alongside practice items in the style of Part I. Content and data from Session 13 Slides 31 and 35-44."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B40 — Dopant levels and extrinsic conductivity with temperature

> [!info] Includes official exam questions
> Ten test questions in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Question 9 is Question 5 of MATERIALS_SECONDPARTIAL_2019.pdf; the remaining nine are practice items. Content: Session 13, Slides 31 and 35-44.

## Q40.1 Dopants of silicon

- id: B40-Q1
- concept_id: u6-dopant-type
- format: false-statement
- asks: classification

Which one of the following statements about dopants in silicon is FALSE?

a) Antimony acts as an electron donor
b) Boron creates an acceptor level in the gap
c) Arsenic adds one loosely bound electron per atom
d) Gallium makes silicon an n-type semiconductor

### Answer

d

### Explanation

Session 13, Slides 35-37: gallium belongs to group IIIA, with three valence electrons; it is an acceptor and makes silicon p-type. Statement d) is false.

- a) True: antimony is a group VA donor (Slides 35-36).
- b) True: boron, group IIIA, creates an acceptor level $E_a$ just above the valence band (Slide 37).
- c) True: arsenic (group VA) uses four of its five valence electrons in the bonds and has one loosely bound excess electron (Slide 36).

### Source

Session 13, Slides 35-37.

## Q40.2 Conductivity of gallium-doped germanium

- id: B40-Q2
- concept_id: u6-p-type-conductivity-calc
- format: numeric
- asks: calculation
- calc: 5.0e21*q*0.19

Germanium is doped with $5.0\times10^{21}$ gallium atoms/m³, all ionised. With $\mu_n = 0.39$ m²/(V·s) and $\mu_p = 0.19$ m²/(V·s), determine its conductivity:

a) $6.57\times10^{-3}$ (Ω·m)⁻¹
b) 152 (Ω·m)⁻¹
c) 312 (Ω·m)⁻¹
d) 465 (Ω·m)⁻¹

### Answer

b

### Explanation

Session 13, Slide 37: gallium is an acceptor, so the material is p-type with $p = 5.0\times10^{21}$ m⁻³ and $\sigma \cong p|q_e|\mu_H = 5.0\times10^{21}\cdot1.6\times10^{-19}\cdot0.19 = 152$ (Ω·m)⁻¹ (mobilities of Ge from Slide 31).

- a) The reciprocal was taken: $1/152 = 6.57\times10^{-3}$ is the resistivity in Ω·m, not the conductivity.
- c) The electron mobility was used, as if gallium were a donor: $5.0\times10^{21}\cdot1.6\times10^{-19}\cdot0.39 = 312$.
- d) Both mobilities were added, as for an intrinsic semiconductor: 465; electrons are minority carriers here.

### Source

Session 13, Slides 31 and 37.

## Q40.3 Reading the band diagram of phosphorus-doped silicon

- id: B40-Q3
- concept_id: u6-donor-acceptor-levels
- format: diagram-reading
- asks: figure-reading
- calc: 1.100-1.055

From the shown energy-band diagram of phosphorus-doped silicon, indicate the energy needed to ionise a phosphorus atom:

![[attachments/MAT-MT2/u6-si-p-levels.svg]]

a) 0.045 eV
b) 0.550 eV
c) 1.055 eV
d) 1.100 eV

### Answer

a

### Explanation

Session 13, Slides 36 and 40: the excess electron of the donor jumps from the donor level to the conduction band, so the energy is $\Delta E = E_c - E_d = 1.100 - 1.055 = 0.045$ eV, the value of the table for P in Si.

- b) Half the band gap, $E_g/2$, is the exponent of intrinsic excitation (Slide 29), not the donor ionisation energy.
- c) The position of the donor level measured from the valence band, $E_d - E_v$, was read instead of its distance to the conduction band.
- d) The whole band gap $E_c - E_v$ is the energy to excite a valence electron, the intrinsic mechanism.

### Source

Session 13, Slides 29, 36 and 40.

## Q40.4 Impurity levels compared with the band gap

- id: B40-Q4
- concept_id: u6-dopant-ionisation-energy
- format: topic-true
- asks: cause

With respect to donor and acceptor impurity levels in extrinsic silicon, indicate which statement is TRUE:

a) Ionising a phosphorus donor atom requires supplying the full 1.1 eV band gap of silicon
b) Increasing the ionic size of a group IIIA acceptor reduces $E_a - E_v$ and increases conductivity
c) Donor and acceptor levels lie very close to the band edges, requiring far less energy than $E_g$ to ionise
d) Impurity levels sit exactly at mid-gap, so half of $E_g$ is needed to activate any dopant

### Answer

c

### Explanation

Session 13, Slides 36-37 and 40: donor levels sit just below $E_c$ and acceptor levels just above $E_v$ (about $0.04$ to $0.16$ eV in Si against $E_g = 1.1$ eV), so dopants ionise much more easily than intrinsic valence electrons at room temperature.

- a) Confuses extrinsic donor excitation ($E_c - E_d$) with intrinsic band-to-band excitation across $E_g$.
- b) Inverts the ionic-size trend for acceptors (Slide 40): a larger acceptor ion holds the valence electron more weakly and increases $E_a - E_v$, lowering conductivity.
- d) Misplaces the impurity states: mid-gap states would need $\approx E_g/2$, whereas shallow dopants sit near the band edges.

### Source

Session 13, Slides 36-37 and 40.

## Q40.5 Ranking acceptors in silicon

- id: B40-Q5
- concept_id: u6-dopant-ionisation-energy
- format: ordering
- asks: comparison

Order the group IIIA acceptors in silicon from the smallest to the largest acceptor ionisation energy $E_a - E_v$ (ionic radius increases down the group: $\text{B} < \text{Al} < \text{Ga} < \text{In}$):

a) In < Ga < Al < B
b) B < Al < Ga < In
c) B < Ga < Al < In
d) Al < B < Ga < In

### Answer

b

### Explanation

Session 13, Slide 40: in silicon $E_a - E_v$ grows with the size of the acceptor ion (B 0.045, Al 0.057, Ga 0.065, In 0.160 eV), because a smaller acceptor ion exerts a stronger attraction on the valence electron and places the acceptor level closer to the valence band.

- a) Fully reversed order, from the largest to the smallest ionisation energy.
- c) Ga and Al are swapped against the periodic trend down group IIIA.
- d) Al and B are swapped: boron is the smallest group IIIA atom and has the smallest $E_a - E_v$.

### Source

Session 13, Slide 40.

## Q40.6 Increasing donor ionisation energy

- id: B40-Q6
- concept_id: u6-dopant-ionisation-energy
- format: what-happens
- asks: application

What will happen to the low-temperature electron concentration of an n-type semiconductor if a dopant with a larger donor ionisation energy $E_c - E_d$ is used at the same dopant concentration:

a) It will increase, because the donor level lies closer to the conduction band
b) It will stay identical, because all group VA elements always give the same level
c) It will double, because each ionised donor releases both an electron and a hole
d) It will decrease, because fewer donor electrons have enough thermal energy to reach $E_c$

### Answer

d

### Explanation

Session 13, Slides 40 and 43: in the extrinsic range $\sigma = \sigma_0\exp[-(E_c - E_d)/2kT]$, so a larger energy gap $E_c - E_d$ makes donor ionisation harder and reduces the concentration of free conduction electrons at a given low temperature.

- a) Inverts the meaning of $E_c - E_d$: a larger ionisation energy means the donor level lies farther below $E_c$, not closer.
- b) Assumes group membership fixes the exact energy level; the levels vary with dopant and host.
- c) Confuses donor ionisation (one conduction electron per donor, no mobile hole) with intrinsic excitation across $E_g$.

### Source

Session 13, Slides 36, 40 and 43.

## Q40.7 Region with the band-gap slope

- id: B40-Q7
- concept_id: u6-extrinsic-slopes
- format: diagram-reading
- asks: figure-reading

From the shown plot of $\ln\sigma$ against $1/T$ for an n-type semiconductor, indicate the region whose slope is $-E_g/2k$:

![[attachments/MAT-MT2/u6-extrinsic-regions.svg]]

a) Region I
b) Region II
c) Region III
d) Regions I and III

### Answer

a

### Explanation

Session 13, Slide 43: at high temperature (small $1/T$, left of the plot) intrinsic generation across the gap takes over and the line has slope $-E_g/2k$: region I, the intrinsic range.

- b) Region II is the exhaustion range, where all donors are ionised and $\sigma$ is almost constant (slope near zero).
- c) Region III is the extrinsic range at low temperature, with the gentler slope $-(E_c - E_d)/2k$.
- d) Region III has a slope set by the donor energy, not by the band gap; only region I has $-E_g/2k$.

### Source

Session 13, Slide 43.

## Q40.8 Donor energy and the extrinsic slope

- id: B40-Q8
- concept_id: u6-extrinsic-slopes
- format: cause-effect
- asks: effect

With an increase in the donor ionisation energy $E_c - E_d$, the extrinsic-range slope of $\ln\sigma$ against $1/T$:

a) Becomes less steep, as the slope is $-2k/(E_c - E_d)$
b) Becomes steeper, as the slope is $-E_g/2k$
c) Stays the same, as the slope is set by the donor concentration
d) Becomes steeper, as the slope is $-(E_c - E_d)/2k$

### Answer

d

### Explanation

Session 13, Slide 43: in the extrinsic range $\ln\sigma = \ln\sigma_0 - (E_c - E_d)/2kT$, so the slope is $-(E_c - E_d)/2k$ and grows in magnitude with the donor energy.

- a) The ratio was inverted; with it a larger energy would wrongly flatten the line.
- b) Right trend with the slope of the intrinsic range, which depends on $E_g$, not on the donor level.
- c) Takes the donor concentration as the origin of the slope: it only shifts the line (the intercept $\ln\sigma_0$), while the slope contains $E_c - E_d$ (Slide 43).

### Source

Session 13, Slide 43.

## Q40.9 When an extrinsic semiconductor behaves as intrinsic

- id: B40-Q9
- concept_id: u6-extrinsic-to-intrinsic
- format: complete-sentence
- asks: definition
- origin: official-exam

An extrinsic semiconductor behaves as an intrinsic one only:

a) If it is a p-type
b) At very high temperatures
c) If it is an n-type
d) At very low temperatures

### Answer

b

### Explanation

MATERIALS_SECONDPARTIAL_2019.pdf, p. 2 (Question 5) and Session 13, Slides 43-44: at very high temperatures, thermal excitation of valence electrons across the band gap $E_g$ produces far more intrinsic electron-hole pairs than the dopant atoms supply, so the material behaves as an intrinsic semiconductor regardless of whether it is n-type or p-type.

- a) Being p-type sets the majority carriers at moderate temperature; it does not turn the semiconductor intrinsic.
- c) Being n-type sets electron conduction in the extrinsic and exhaustion regimes, not intrinsic behaviour.
- d) Inverts the temperature limit: at very low temperatures intrinsic carrier generation is negligible and even dopants freeze out.

### Source

MATERIALS_SECONDPARTIAL_2019.pdf, p. 2 (Question 5); MATERIALS_SECONDPARTIAL_2018.docx; Session 13, Slides 43-44.

## Q40.10 Extrinsic semiconductor at low temperature

- id: B40-Q10
- concept_id: u6-extrinsic-temperature-regions
- format: true-statement
- asks: definition

Which one of the following statements about an extrinsic semiconductor heated from a low temperature is TRUE?

a) At low temperature, $\sigma$ is set by electrons crossing the band gap
b) At intermediate temperature, $\sigma$ rises steeply with temperature
c) At low temperature, $\sigma$ is set by the number of ionised impurities
d) At very high temperature, it behaves as a metallic conductor

### Answer

c

### Explanation

Session 13, Slides 43-44: at low temperature the number of ionised impurities per unit volume determines $\sigma$; as $T$ increases more atoms are ionised and $\sigma$ increases (extrinsic range).

- a) Excitation across the gap is the very-high-temperature (intrinsic) mechanism.
- b) At intermediate temperature all the impurities are ionised and $\sigma$ is almost constant (exhaustion or saturation range).
- d) At very high temperature the material behaves as an intrinsic semiconductor, not as a metal.

### Source

Session 13, Slides 43-44.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
