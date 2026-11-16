---
materia: Aerospace Materials I
tema: "Unit 6: intrinsic semiconductors applied: conductivity against temperature, carrier concentration, band gap from data, bonding and mobility"
bank_id: B54
title: "Intrinsic semiconductors applied"
category: mt2_test_block
unit: 6
concepts:
  - u6-intrinsic-ratio-kelvin
  - u6-carrier-concentration-from-sigma
  - u6-gap-from-two-points
  - u6-two-lines-gap-ratio
  - u6-iii-v-ordering
  - u6-cdte-insb-covalent
  - u6-germanium-three-temperatures
  - u6-metal-vs-semiconductor-heating
  - u6-electron-hole-fraction
  - u6-photon-gap-excitation
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 13 Slides 25-34 and 46."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B54 — Intrinsic semiconductors applied

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 13, Slides 25-34 and 46.

## Q54.1 Conductivity ratio between two temperatures

- id: B54-Q1
- concept_id: u6-intrinsic-ratio-kelvin
- format: numeric
- asks: calculation
- calc: exp(0.90/(2*k_B)*(1/300-1/360))

An intrinsic semiconductor has a band gap $E_g = 0.90$ eV. By what factor is its conductivity multiplied when its temperature rises from 300 K to 360 K ($k_B = 8.62\times10^{-5}$ eV/K)?

a) 0.0550 times
b) 18.2 times
c) 330 times
d) 1.20 times

### Answer

b

### Explanation

Session 13, Slide 29: $\sigma = \sigma_0\exp(-E_g/2kT)$, so $\dfrac{\sigma_2}{\sigma_1} = \exp\!\left[\dfrac{E_g}{2k}\left(\dfrac{1}{T_1}-\dfrac{1}{T_2}\right)\right] = \exp\!\left[\dfrac{0.90}{2\cdot8.62\times10^{-5}}\left(\dfrac{1}{300}-\dfrac{1}{360}\right)\right] = e^{2.90} = 18.2$.

- a) The ratio was inverted ($\sigma_1/\sigma_2$): an intrinsic semiconductor conducts more when heated.
- c) The factor 2 of $2kT$ was dropped: $\exp(2\cdot2.90) = 330$.
- d) The ratio of the temperatures, $360/300 = 1.20$, was used, as if $\sigma$ were proportional to $T$.

### Source

Session 13, Slide 29.

## Q54.2 Carrier concentration from a measured conductivity

- id: B54-Q2
- concept_id: u6-carrier-concentration-from-sigma
- format: numeric
- asks: calculation
- calc: 5.0e-2/(q*(0.30+0.10))/1e17

The conductivity of an intrinsic semiconductor at room temperature is $5.0\times10^{-2}$ (Ω·m)⁻¹, with $\mu_e = 0.30$ m²/(V·s) and $\mu_h = 0.10$ m²/(V·s). Determine the concentration of electrons (equal to that of holes), in units of $10^{17}$ m⁻³:

a) 3.90
b) 31.2
c) 7.80
d) 10.4

### Answer

c

### Explanation

Session 13, Slide 28: with $n = p$ and $|q_e| = |q_h|$, $\sigma = n|q_e|(\mu_e+\mu_h)$, so $n = \dfrac{5.0\times10^{-2}}{1.602\times10^{-19}\,(0.30+0.10)} = 7.80\times10^{17}$ m⁻³.

- a) The result was divided by 2 again because $n = p$: the factor 2 is already in the sum of the two mobilities, which counts both carriers.
- b) Only the hole mobility was used: $\sigma/(|q|\mu_h) = 31.2\times10^{17}$ m⁻³.
- d) Only the electron mobility was used: $\sigma/(|q|\mu_e) = 10.4\times10^{17}$ m⁻³; the holes also conduct.

### Source

Session 13, Slide 28.

## Q54.3 Band gap from two measurements

- id: B54-Q3
- concept_id: u6-gap-from-two-points
- format: numeric
- asks: calculation
- calc: 2*k_B*ln(6.0e-2/2.0e-3)/(1/300.15-1/350.15)

The conductivity of an intrinsic semiconductor was measured at two temperatures. Determine its band gap ($k_B = 8.62\times10^{-5}$ eV/K):

| $T$ (°C) | $\sigma$ ((Ω·m)⁻¹) |
| :---: | :---: |
| 27 | $2.0\times10^{-3}$ |
| 77 | $6.0\times10^{-2}$ |

a) 0.0244 eV
b) 0.616 eV
c) 2.47 eV
d) 1.23 eV

### Answer

d

### Explanation

Session 13, Slide 29: $\ln\sigma = \ln\sigma_0 - E_g/2kT$, so $E_g = 2k\,\dfrac{\ln(\sigma_2/\sigma_1)}{1/T_1-1/T_2}$ with $T_1 = 300.15$ K and $T_2 = 350.15$ K, $1/T_1-1/T_2 = 4.757\times10^{-4}$ K⁻¹: $E_g = 2\cdot8.62\times10^{-5}\cdot\dfrac{\ln 30}{4.757\times10^{-4}} = 1.23$ eV.

- a) The temperatures in °C were used in $1/T$: $1/27-1/77$ is not the difference of reciprocal absolute temperatures.
- b) The factor 2 of $2kT$ was dropped: $E_g = 8.62\times10^{-5}\cdot\ln30/(4.757\times10^{-4}) = 0.616$ eV.
- c) The factor 2 was applied twice, $E_g = 4k\ln30/(4.757\times10^{-4}) = 2.47$ eV.

### Source

Session 13, Slide 29.

## Q54.4 Two intrinsic semiconductors on an Arrhenius plot

- id: B54-Q4
- concept_id: u6-two-lines-gap-ratio
- format: numeric
- asks: figure-reading
- calc: (8.0-2.0)/(6.0-3.0)

The plot shows $\ln\sigma$ against $1/T$ for two intrinsic semiconductors A and B. Determine the ratio $E_{g,A}/E_{g,B}$ of their band gaps:

![[attachments/MAT-MT2/u6-b54-two-lines.svg]]

a) 0.50
b) 2.0
c) 0.67
d) 1.33

### Answer

b

### Explanation

Session 13, Slide 29: the slope of $\ln\sigma$ against $1/T$ is $-E_g/2k$, so $E_g$ is proportional to the steepness of the line. Slope of A: $(2.0-8.0)/(1.0\times10^{-3}) = -6000$ K per unit; slope of B: $(3.0-6.0)/(1.0\times10^{-3}) = -3000$ K. Then $E_{g,A}/E_{g,B} = 6.0/3.0 = 2.0$.

- a) The ratio was inverted: the steeper line corresponds to the larger gap.
- c) The values of $\ln\sigma$ at $1/T = 2.0\times10^{-3}$ K⁻¹ were compared, $2.0/3.0$: the gap is given by the slope, not by the height at one point.
- d) The values of $\ln\sigma$ at $1/T = 1.0\times10^{-3}$ K⁻¹ were compared, $8.0/6.0$, which ignores the second point of each line.

### Source

Session 13, Slide 29.

## Q54.5 Ordering of three III-V compounds

- id: B54-Q5
- concept_id: u6-iii-v-ordering
- format: ordering
- asks: comparison

Order AlP, GaAs and InSb from the highest to the lowest electrical conductivity at the same temperature:

a) AlP > GaAs > InSb
b) InSb > AlP > GaAs
c) InSb > GaAs > AlP
d) AlP > InSb > GaAs

### Answer

c

### Explanation

Session 13, Slides 31-33 and Problem 10: the three are group 13-15 compounds, and for intrinsic semiconductors $E_g$ decreases as the atoms get larger and $\sigma$ increases (Slide 31). The gaps in the table of Slide 33 are 0.17 eV for InSb and 1.42 eV for GaAs; AlP, with the smallest atoms, has the largest gap (its value is not in the slides: **extension**, taken from the trend). Hence $\sigma_{InSb} > \sigma_{GaAs} > \sigma_{AlP}$.

- a) The order is inverted: the smallest atoms were assumed to give the best conduction.
- b) InSb was put first, but AlP was ranked above GaAs, as if the smaller atoms made the bonding more covalent and the gap smaller.
- d) AlP was placed first because it was assumed that the strongest bonds conduct best; the pair InSb and GaAs then follows the right order.

### Source

Session 13, Slides 31, 33 and 34; Problems T6 and T7, Problem 10.

## Q54.6 CdTe against InSb

- id: B54-Q6
- concept_id: u6-cdte-insb-covalent
- format: true-statement
- asks: cause

CdTe (groups 12 and 16) and InSb (groups 13 and 15) are intrinsic semiconductors at the same temperature. Which one of the following statements is TRUE?

c) CdTe has the higher conductivity, as its bonding is more covalent
b) CdTe has the higher conductivity, as its bonding is more ionic
a) InSb has the higher conductivity, as its bonding is more covalent
d) InSb has the higher conductivity, as its bonding is more ionic

### Answer

a

### Explanation

Session 13, Slide 32 (Problem 10b): from the 13-15 to the 12-16 compounds the covalent character decreases, so $E_g$ increases and $\sigma$ decreases. InSb is the more covalent of the two, has the smaller gap (0.17 eV, Slide 33) and the higher conductivity.

- c) The two compounds were swapped: it is the 13-15 compound that is more covalent.
- b) Ionic bonding was taken as favourable for conduction; in an intrinsic semiconductor it raises the gap.
- d) Right material, wrong cause: more ionic character means a larger gap and a lower conductivity.

### Source

Session 13, Slides 32 and 33; Problems T6 and T7, Problem 10.

## Q54.7 Pure germanium at three temperatures

- id: B54-Q7
- concept_id: u6-germanium-three-temperatures
- format: ordering
- asks: comparison

Order pure germanium at 0 °C, 25 °C and 50 °C from the highest to the lowest electrical conductivity:

a) 0 °C, 25 °C, 50 °C
b) 25 °C, 50 °C, 0 °C
c) 25 °C and 50 °C equal, then 0 °C
d) 50 °C, 25 °C, 0 °C

### Answer

d

### Explanation

Session 13, Slide 29 and Problems T6 and T7, Problem 9a: in an intrinsic semiconductor $n$ and $p$ grow as $\exp(-E_g/2kT)$ and this masks the loss of mobility, so $\sigma$ increases with $T$: $\sigma_{50} > \sigma_{25} > \sigma_{0}$.

- a) The trend of a metal was applied: conductivity falling as the material is heated.
- b) A maximum at room temperature was assumed, as if the lattice disorder won beyond 25 °C; in the intrinsic range the carrier number wins.
- c) The saturation of an extrinsic semiconductor was assumed; pure germanium has no dopant levels to exhaust.

### Source

Session 13, Slide 29; Problems T6 and T7, Problem 9a.

## Q54.8 Copper wire and intrinsic silicon heated

- id: B54-Q8
- concept_id: u6-metal-vs-semiconductor-heating
- format: what-happens
- asks: comparison

Which one of the following statements about a copper wire and a piece of intrinsic silicon, both heated from 20 to 100 °C, is TRUE?

a) Both conduct better, as the heating frees more carriers in each of them
b) Both conduct worse, as the vibrations of the lattice scatter the carriers in each of them
c) The copper conducts worse because of more collisions, the silicon better because of more carriers
d) The copper conducts better because of more carriers, the silicon worse because of more collisions

### Answer

c

### Explanation

Session 13, Slides 14, 29 and 30 (Problem 4): in the metal the number of electrons is fixed and the thermal vibrations increase the collisions, so $\rho_T$ rises; in the intrinsic semiconductor the number of electrons and holes grows exponentially, so $\sigma$ rises and $\rho$ falls.

- a) The disorder effect was applied to both; in the semiconductor it is masked by the larger number of carriers.
- b) The carrier excitation was applied to both; a metal has no gap to cross.
- d) The two behaviours were swapped.

### Source

Session 13, Slides 14, 29 and 30; Problems T6 and T7, Problem 4.

## Q54.9 Share of the electrons in the conductivity

- id: B54-Q9
- concept_id: u6-electron-hole-fraction
- format: numeric
- asks: calculation
- calc: 7.7/(7.7+0.07)*100

A high-purity intrinsic InSb crystal has $\mu_e = 7.7$ m²/(V·s) and $\mu_h = 0.07$ m²/(V·s). What percentage of its conductivity is carried by the electrons?

a) 99.1 %
b) 0.90 %
c) 50.0 %
d) 91.7 %

### Answer

a

### Explanation

Session 13, Slides 28 and 33: with $n = p$, $\sigma_e/\sigma = \mu_e/(\mu_e+\mu_h) = 7.7/7.77 = 0.991$. A pure, ordered crystal has high mobilities (Slide 33) and $\mu_e \gg \mu_h$ here.

- b) The share of the holes, $0.07/7.77 = 0.90$ %, was given.
- c) Equal numbers $n = p$ were taken to mean equal contributions; each term also carries its own mobility.
- d) The hole mobility was misread as 0.7 m²/(V·s): $7.7/8.4 = 91.7$ %.

### Source

Session 13, Slides 28 and 33.

## Q54.10 Photon and band gap

- id: B54-Q10
- concept_id: u6-photon-gap-excitation
- format: identify
- asks: application

Photons of energy 1.0 eV fall on the intrinsic semiconductors of the table. In which of them can a photon excite an electron from the valence band to the conduction band?

| Material | $E_g$ (eV) |
| :--- | :---: |
| Si | 1.11 |
| Ge | 0.67 |
| GaAs | 1.42 |
| InSb | 0.17 |

a) Si, Ge and InSb
b) Ge and InSb
c) Si and GaAs
d) GaAs and InSb

### Answer

b

### Explanation

Session 13, Slides 33 and 46: an electron jumps to the conduction band when it absorbs radiation of energy at least $E_g$. With 1.0 eV that holds for Ge (0.67 eV) and InSb (0.17 eV); the photon energy is too small for Si (1.11 eV) and GaAs (1.42 eV).

- a) Si was included because 1.11 eV is close to 1.0 eV; the photon energy must be at least the gap.
- c) The condition was inverted: the materials with a gap larger than the photon energy were chosen.
- d) GaAs was included with InSb for a gap not far above the photon energy; 1.42 eV exceeds 1.0 eV.

### Source

Session 13, Slides 33 and 46.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
