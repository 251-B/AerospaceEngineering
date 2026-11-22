---
materia: Aerospace Materials I
tema: "Unit 6: conductivity of intrinsic semiconductors, temperature dependence, band gap and bonding"
bank_id: B38
title: "Intrinsic semiconductors, band gap and temperature"
category: mt2_test_block
unit: 6
concepts:
  - u6-intrinsic-conductivity-calc
  - u6-semiconductor-definition-types
  - u6-intrinsic-temperature
  - u6-gap-and-bonding
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 13 Slides 26-33."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B38 — Intrinsic semiconductors, band gap and temperature

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 13, Slides 26-33.

## Q38.1 Conductivity of intrinsic germanium

- id: B38-Q1
- concept_id: u6-intrinsic-conductivity-calc
- format: numeric
- asks: calculation
- calc: 2.4e19*q*(0.39+0.19)

Intrinsic germanium has $n_i = 2.4\times10^{19}$ m⁻³, $\mu_n = 0.39$ m²/(V·s) and $\mu_p = 0.19$ m²/(V·s). Determine its electrical conductivity:

a) 0.448 (Ω·m)⁻¹
b) 0.730 (Ω·m)⁻¹
c) 1.50 (Ω·m)⁻¹
d) 2.23 (Ω·m)⁻¹

### Answer

d

### Explanation

Session 13, Slide 28: $\sigma = n|q_e|(\mu_e+\mu_h)$ with $n = p = n_i$: $\sigma = 2.4\times10^{19}\cdot1.6\times10^{-19}\cdot(0.39+0.19) = 2.23$ (Ω·m)⁻¹, in agreement with the 2.2 (Ω·m)⁻¹ of the table of Slide 33.

- a) The reciprocal was taken: $1/2.23 = 0.448$ is the resistivity in Ω·m (Slide 31 gives 0.46 Ω·m).
- b) Only the holes were counted: $n_i|q_e|\mu_p = 0.730$.
- c) Only the electrons were counted: $n_i|q_e|\mu_n = 1.50$; in an intrinsic semiconductor both carriers conduct.

### Source

Session 13, Slides 28, 31 and 33.

## Q38.2 Electron and hole terms of the conductivity

- id: B38-Q2
- concept_id: u6-intrinsic-conductivity-calc
- format: true-statement
- asks: comparison

Which one of the following statements about the electron and hole terms of $\sigma$ in intrinsic silicon is TRUE?

a) The electron term is larger, as electrons are more mobile
b) The electron term is larger, as electrons are more numerous
c) The hole term is larger, as holes carry more charge
d) Both terms are equal, as $n = p$

### Answer

a

### Explanation

Session 13, Slides 28 and 33: $\sigma = n|q_e|\mu_e + p|q_e|\mu_H$ with $n = p$ and equal charges, so the two terms differ only through the mobilities, and $\mu_e > \mu_H$ (Si: 0.14 against 0.05 m²/(V·s)).

- b) Right comparison with the wrong reason: in an intrinsic semiconductor $n = p$, so the numbers of carriers are equal.
- c) Electrons and holes carry charges of the same magnitude, $1.6\times10^{-19}$ C.
- d) Equal numbers do not give equal terms: each term is also multiplied by its own mobility.

### Source

Session 13, Slides 28 and 33.

## Q38.3 An intrinsic semiconductor

- id: B38-Q3
- concept_id: u6-semiconductor-definition-types
- format: identify
- asks: classification

Which one of the following materials is an intrinsic semiconductor?

a) Silicon doped with boron
b) Pure gallium arsenide
c) Germanium doped with arsenic
d) Silicon doped with antimony

### Answer

b

### Explanation

Session 13, Slides 26 and 32: an intrinsic semiconductor owes its conductivity to the inherent properties of the pure material; besides Si and Ge, compounds of groups IIIA and VA such as GaAs are intrinsic semiconductors.

- a) Boron is an acceptor dopant: the material is an extrinsic p-type semiconductor (Slide 37).
- c) Arsenic is a donor: extrinsic n-type (Slide 36).
- d) Antimony is a donor: extrinsic n-type (Slide 36).

### Source

Session 13, Slides 26, 32, 36 and 37.

## Q38.4 Intrinsic semiconductor and temperature

- id: B38-Q4
- concept_id: u6-intrinsic-temperature
- format: cause-effect
- asks: effect

With an increase in temperature, the electrical conductivity of an intrinsic semiconductor:

a) Decreases, as lattice vibrations lower the mobility
b) Increases, as the mobility of the carriers rises
c) Decreases, as electrons and holes become fewer
d) Increases, as more electrons cross the band gap

### Answer

d

### Explanation

Session 13, Slide 29: both $n$ and $p$ increase with temperature, $n_i \propto \exp(-E_g/2kT)$, so $\sigma$ increases; temperature also lowers the mobility, but this effect is masked by the increase in the number of carriers.

- a) This is the behaviour and the cause of a metal, whose number of carriers is fixed.
- b) Right trend with the wrong cause: the mobility falls with temperature; the gain comes from the number of carriers.
- c) Inverted: heating excites more electrons across the gap, so the numbers of both carriers grow.

### Source

Session 13, Slides 29 and 48.

## Q38.5 Intrinsic conductivity and temperature

- id: B38-Q5
- concept_id: u6-intrinsic-temperature
- format: topic-false
- asks: cause

Regarding the temperature dependence of conductivity in an intrinsic semiconductor ($\sigma = \sigma_0\exp(-E_g/2kT)$), indicate which statement is FALSE:

a) Raising temperature increases the number of excited electrons and holes exponentially across the gap
b) Conductivity increases on heating because thermal lattice vibrations raise carrier mobilities $\mu_e$ and $\mu_h$
c) Plotting $\ln\sigma$ against $1/T$ produces a straight line whose slope equals $-E_g/2k$
d) The temperature $T$ in the Arrhenius exponent must be expressed in kelvin rather than degrees Celsius

### Answer

b

### Explanation

Session 13, Slide 29: thermal disorder from lattice vibrations actually reduces carrier mobility as temperature rises, just as in metals, but in an intrinsic semiconductor this reduction is masked by the far larger exponential growth in carrier concentration $n_i \propto \exp(-E_g/2kT)$. Statement b) is false.

- a) True (Slide 29): both $n$ and $p$ grow exponentially with temperature via $\exp(-E_g/2kT)$.
- c) True (Slide 29): taking the natural logarithm gives $\ln\sigma = \ln\sigma_0 - (E_g/2k)(1/T)$, a straight line of slope $-E_g/2k$.
- d) True (Slide 29): absolute temperature in kelvin is required in the Boltzmann factor $kT$.

### Source

Session 13, Slide 29.

## Q38.6 Picture of an intrinsic semiconductor

- id: B38-Q6
- concept_id: u6-intrinsic-temperature
- format: choose-figure
- asks: figure-reading

Which picture describes $\ln\sigma$ against $1/T$ for an intrinsic semiconductor?

a) ![[attachments/MAT-MT2/u6-lnsig-1.svg]]
b) ![[attachments/MAT-MT2/u6-lnsig-2.svg]]
c) ![[attachments/MAT-MT2/u6-lnsig-3.svg]]
d) ![[attachments/MAT-MT2/u6-lnsig-4.svg]]

### Answer

a

### Explanation

Session 13, Slide 29: $\ln\sigma = \ln\sigma_0 - E_g/2kT$ is a straight line of negative slope $-E_g/2k$ against $1/T$: $\ln\sigma$ falls as $1/T$ grows (lower temperature). Plot A is that line.

- b) A rising line has the sign of the slope inverted, as if $\sigma$ fell on heating (the behaviour of a metal).
- c) Three segments (steep, flat, gentle) are the extrinsic, exhaustion and intrinsic ranges of a doped semiconductor (Slide 43).
- d) A horizontal line means a number of carriers independent of temperature, which ignores the excitation across the gap.

### Source

Session 13, Slides 29 and 43.

## Q38.7 Band gap from the slope

- id: B38-Q7
- concept_id: u6-intrinsic-temperature
- format: diagram-reading
- asks: calculation
- calc: 2*k_B*(7.0-0.6)/(2.0e-3-1.0e-3)

From the shown plot of $\ln\sigma$ against $1/T$ for an intrinsic semiconductor, determine its band gap ($k_B = 8.62\times10^{-5}$ eV/K):

![[attachments/MAT-MT2/u6-intrinsic-line.svg]]

a) 0.276 eV
b) 0.552 eV
c) 1.10 eV
d) 2.54 eV

### Answer

c

### Explanation

Session 13, Slide 29: the slope of $\ln\sigma$ against $1/T$ is $-E_g/2k$. From the two marked points, slope $= (0.6 - 7.0)/(2.0\times10^{-3} - 1.0\times10^{-3}) = -6400$ K, so $E_g = 2k\cdot6400 = 2\cdot8.62\times10^{-5}\cdot6400 = 1.10$ eV (silicon).

- a) The slope was taken as $-2E_g/k$, that is $E_g = k\cdot6400/2 = 0.276$ eV.
- b) The factor 2 was dropped: $E_g = k\cdot6400 = 0.552$ eV.
- d) The axis was read as $\log_{10}\sigma$ and converted to natural logarithms: $1.10\cdot\ln 10 = 2.54$ eV; the plot is already in $\ln\sigma$.

### Source

Session 13, Slide 29.

## Q38.8 Highest intrinsic conductivity

- id: B38-Q8
- concept_id: u6-gap-and-bonding
- format: identify
- asks: comparison

Which intrinsic semiconductor has the highest electrical conductivity at the same temperature?

a) Silicon
b) Germanium
c) Gallium arsenide
d) Cadmium sulphide

### Answer

b

### Explanation

Session 13, Slides 29 and 33: $\sigma \propto \exp(-E_g/2kT)$, so the smallest gap gives the largest conductivity. Of the four, Ge has the smallest gap, 0.67 eV ($\sigma = 2.2$ (Ω·m)⁻¹ in the table).

- a) Si has $E_g = 1.11$ eV, larger than Ge, and $\sigma = 4\times10^{-4}$ (Ω·m)⁻¹.
- c) GaAs has $E_g = 1.42$ eV and $\sigma = 10^{-6}$ (Ω·m)⁻¹; its very high electron mobility does not make up for the larger gap.
- d) CdS has the largest gap of the four, 2.40 eV, so the fewest carriers.

### Source

Session 13, Slides 29 and 33.

## Q38.9 Ionic character and band gap

- id: B38-Q9
- concept_id: u6-gap-and-bonding
- format: cause-effect
- asks: effect

With an increase in the ionic character of the bonding of an intrinsic semiconductor (from Si to GaAs to ZnTe), its band gap:

a) Decreases and its conductivity increases
b) Increases and its conductivity increases
c) Decreases and its conductivity decreases
d) Increases and its conductivity decreases

### Answer

d

### Explanation

Session 13, Slide 32: going from the group-14 elements to the 13-15 and 12-16 compounds, the covalent character decreases and the ionic character increases, $E_g$ increases (Si 1.11, GaAs 1.42, ZnTe 2.26 eV) and $\sigma$ of the intrinsic semiconductor decreases.

- a) Inverted trend of both quantities, as if the bonding became more covalent.
- b) Right trend for the gap, but a larger gap gives fewer carriers, so $\sigma$ falls.
- c) Wrong trend for the gap, and a smaller gap would raise, not lower, the conductivity.

### Source

Session 13, Slides 32-33.

## Q38.10 Germanium against silicon

- id: B38-Q10
- concept_id: u6-gap-and-bonding
- format: identify
- asks: cause

Which feature explains why germanium has a smaller band gap than silicon?

a) Its atoms are smaller
b) Its bonding is more ionic
c) Its atoms are larger
d) It contains donor impurities

### Answer

c

### Explanation

Session 13, Slide 31: in the group IVA elemental semiconductors (covalent bonds), as the atom size increases, $E_g$ decreases and the conductivity increases; Ge (0.67 eV) has larger atoms than Si (1.1 eV).

- a) Inverted: smaller atoms would give a larger gap.
- b) Si and Ge are both elemental and purely covalent; a more ionic bonding would raise the gap (Slide 32).
- d) The gap of the pure material does not come from dopants; donors add a level inside the gap without changing $E_g$ (Slide 36).

### Source

Session 13, Slides 31, 32 and 36.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
