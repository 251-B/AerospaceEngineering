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
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 13 Slides 31, 35-44."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B40 — Dopant levels and extrinsic conductivity with temperature

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 13, Slides 31 and 35-44.

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

## Q40.4 Easiest dopant to ionise in silicon

- id: B40-Q4
- concept_id: u6-dopant-ionisation-energy
- format: identify
- asks: comparison

Which dopant of silicon needs the smallest energy to supply a charge carrier?

a) Arsenic
b) Gallium
c) Indium
d) Antimony

### Answer

d

### Explanation

Session 13, Slide 40 (table of donor and acceptor energies in Si): Sb 0.039 eV, As 0.049 eV, Ga 0.065 eV and In 0.160 eV. Antimony has the smallest ionisation energy.

- a) Arsenic needs 0.049 eV, slightly more than antimony.
- b) Gallium is an acceptor with $E_a - E_v = 0.065$ eV.
- c) Indium has the largest ionisation energy of the table, 0.160 eV.

### Source

Session 13, Slide 40.

## Q40.5 Ranking acceptors in silicon

- id: B40-Q5
- concept_id: u6-dopant-ionisation-energy
- format: ordering
- asks: comparison

Order the following acceptors in silicon from the smallest to the largest ionisation energy $E_a - E_v$:

a) In < Ga < Al < B
b) B < Al < Ga < In
c) B < Ga < Al < In
d) Al < B < Ga < In

### Answer

b

### Explanation

Session 13, Slide 40: in silicon $E_a - E_v$ is 0.045 eV for B, 0.057 eV for Al, 0.065 eV for Ga and 0.160 eV for In; the energy grows with the size of the acceptor.

- a) Fully reversed order, from the largest to the smallest energy.
- c) Ga and Al are swapped: aluminium (0.057 eV) is below gallium (0.065 eV).
- d) Al and B are swapped: boron (0.045 eV) has the smallest energy.

### Source

Session 13, Slide 40.

## Q40.6 Changing the acceptor of germanium

- id: B40-Q6
- concept_id: u6-dopant-ionisation-energy
- format: what-happens
- asks: application
- check: 0.0104 < 0.0112

What will happen to the conductivity of germanium at a low temperature if its indium dopant is replaced by the same concentration of boron:

a) It will decrease, as boron has a smaller $E_a - E_v$
b) It will stay the same, as both are group IIIA acceptors
c) It will increase, as boron has a smaller $E_a - E_v$
d) It will increase, as boron acts as a donor

### Answer

c

### Explanation

Session 13, Slides 40 and 43: in Ge, $E_a - E_v$ is 0.0104 eV for B and 0.0112 eV for In. In the extrinsic range $\sigma = \sigma_0\exp[-(E_a-E_v)/2kT]$, so the smaller energy ionises more acceptors and the conductivity increases (the slide's arrow: smaller acceptor, higher conductivity).

- a) Right energy comparison, inverted consequence: a smaller ionisation energy gives more holes, not fewer.
- b) Being in the same group does not give the same level; the energies of the table differ.
- d) Boron has three valence electrons: it is an acceptor in Ge as in Si.

### Source

Session 13, Slides 37, 40 and 43.

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

## Q40.9 n-type semiconductor at very high temperature

- id: B40-Q9
- concept_id: u6-extrinsic-to-intrinsic
- format: complete-sentence
- asks: cause

At very high temperature, the conductivity of an n-type semiconductor is controlled by:

a) The electrons supplied by the donor levels as they ionise
b) The holes created at the acceptor levels
c) The electrons and holes generated across the band gap
d) The mobility of the ionised donor atoms

### Answer

c

### Explanation

Session 13, Slides 43-44: at very high temperature the intrinsic generation across the gap takes over and the material behaves as an intrinsic conductor; the carriers are the electrons and holes created across $E_g$.

- a) Electrons from the donors describe the extrinsic and exhaustion ranges; at very high temperature they are outnumbered by intrinsic carriers.
- b) An n-type material has donor levels, not acceptor levels.
- d) The ionised donors are fixed in the lattice; they are not carriers.

### Source

Session 13, Slides 36 and 43-44.

## Q40.10 Extrinsic semiconductor at low temperature

- id: B40-Q10
- concept_id: u6-extrinsic-temperature-regions
- format: true-statement
- asks: definition

Which one of the following statements about an extrinsic semiconductor heated from a low temperature is TRUE?

a) At low temperature, $\sigma$ is set by electrons crossing the band gap
b) At low temperature, $\sigma$ is set by the number of ionised impurities
c) At intermediate temperature, $\sigma$ rises steeply with temperature
d) At very high temperature, it behaves as a metallic conductor

### Answer

b

### Explanation

Session 13, Slides 43-44: at low temperature the number of ionised impurities per unit volume determines $\sigma$; as $T$ increases more atoms are ionised and $\sigma$ increases (extrinsic range).

- a) Excitation across the gap is the very-high-temperature (intrinsic) mechanism.
- c) At intermediate temperature all the impurities are ionised and $\sigma$ is almost constant (exhaustion or saturation range).
- d) At very high temperature the material behaves as an intrinsic semiconductor, not as a metal.

### Source

Session 13, Slides 43-44.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
