---
materia: Aerospace Materials I
tema: "Unit 6: ln sigma against 1/T of extrinsic semiconductors, onset of the intrinsic range and semiconductor devices"
bank_id: B56
title: "Extrinsic conductivity against temperature and devices"
category: mt2_test_block
unit: 6
concepts:
  - u6-extrinsic-slope-calc
  - u6-intrinsic-ratio-calc
  - u6-photon-gap-calc
  - u6-gap-from-curves
  - u6-exhaustion-mobility
  - u6-intrinsic-onset-gap
  - u6-pn-junction-pairs
  - u6-led-gap-comparison
  - u6-thermistor-resistance
  - u6-transistor-function
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 13 Slides 29 and 43-49."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B56 — Extrinsic conductivity against temperature and devices

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 13, Slides 29 and 43-49.

## Q56.1 Donor energy from the extrinsic range

- id: B56-Q1
- concept_id: u6-extrinsic-slope-calc
- format: numeric
- asks: calculation
- calc: 2*8.62e-5*log(0.130/0.100)/(1/200-1/250)

Two points of the extrinsic range of an n-type semiconductor are given in the table. With $k_B = 8.62\times10^{-5}$ eV/K, determine the donor energy $E_c - E_d$:

| $T$ (K) | $\sigma$ ((Ω·m)⁻¹) |
| :--- | :--- |
| 200 | 0.100 |
| 250 | 0.130 |

a) 0.0196 eV
b) 0.0226 eV
c) 0.0452 eV
d) 0.0905 eV

### Answer

c

### Explanation

Session 13, Slide 43: in the extrinsic range $\ln\sigma = \ln\sigma_0 - (E_c - E_d)/2kT$, so $\ln(\sigma_2/\sigma_1) = \frac{E_c - E_d}{2k}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$ and $E_c - E_d = 2k\,\ln(0.130/0.100)/(1/200 - 1/250) = 2\cdot8.62\times10^{-5}\cdot0.2624/0.00100 = 0.0452$ eV, close to the 0.045 eV of phosphorus in silicon (Slide 40).

- a) The common logarithm was used instead of the natural one: $0.0452\cdot0.434 = 0.0196$ eV.
- b) The factor 2 of the slope $-(E_c - E_d)/2k$ was dropped: $k\ln(\sigma_2/\sigma_1)/(1/T_1 - 1/T_2) = 0.0226$ eV.
- d) The slope was taken as $-2(E_c - E_d)/k$ in place of $-(E_c - E_d)/2k$.

### Source

Session 13, Slides 40 and 43.

## Q56.2 Intrinsic range between two temperatures

- id: B56-Q2
- concept_id: u6-intrinsic-ratio-calc
- format: numeric
- asks: calculation
- calc: exp(1.11/(2*8.62e-5)*(1/400-1/500))

Intrinsic silicon has $E_g = 1.11$ eV. With $k_B = 8.62\times10^{-5}$ eV/K, determine the ratio $\sigma(500\ \mathrm{K})/\sigma(400\ \mathrm{K})$:

a) 0.0400
b) 3.22
c) 25.0
d) 625

### Answer

c

### Explanation

Session 13, Slide 29: $\sigma = \sigma_0\exp(-E_g/2kT)$, so $\sigma_2/\sigma_1 = \exp\left[\frac{E_g}{2k}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)\right] = \exp\left[\frac{1.11}{2\cdot8.62\times10^{-5}}\cdot0.00050\right] = \exp(3.22) = 25.0$.

- a) The ratio was inverted: $\sigma(400)/\sigma(500) = 0.0400$.
- b) The exponent was reported and the exponential was not evaluated: $\ln(\sigma_2/\sigma_1) = 3.22$.
- d) The factor 2 of $2kT$ was dropped: $\sigma\propto\exp(-E_g/kT)$ gives $\exp(6.44) = 625$.

### Source

Session 13, Slides 29 and 33.

## Q56.3 Wavelength that crosses the gap

- id: B56-Q3
- concept_id: u6-photon-gap-calc
- format: numeric
- asks: calculation
- calc: 1240/1.5

A material for photovoltaic cells has $E_g = 1.5$ eV. Taking $hc = 1240$ eV·nm, determine the longest wavelength of light that can excite an electron across its band gap:

a) 413 nm
b) 827 nm
c) 1650 nm
d) 1860 nm

### Answer

b

### Explanation

Session 13, Slide 46: a photon excites an electron from the valence to the conduction band only if $hc/\lambda \ge E_g$, so $\lambda_{max} = hc/E_g = 1240/1.5 = 827$ nm (near infrared). The value $hc = 1240$ eV·nm is a constant given in the statement (**extension**: it is not in the slides); the gap of 1.5 eV is the one of the slide for solar light.

- a) The photon energy was set to twice the gap: $1240/(2\cdot1.5) = 413$ nm.
- c) Half of the gap was used, as in the factor $E_g/2$ of $\exp(-E_g/2kT)$: $1240/0.75 = 1653$ nm, rounded to 1650 nm.
- d) The two numbers were multiplied instead of divided: $1240\cdot1.5 = 1860$ nm.

### Source

Session 13, Slide 46.

## Q56.4 Two semiconductors with the same donors

- id: B56-Q4
- concept_id: u6-gap-from-curves
- format: diagram-reading
- asks: figure-reading

![[attachments/MAT-MT2/u6-b56-two-curves.svg]]

From the shown plot of $\ln\sigma$ against $1/T$ for two n-type semiconductors A and B with the same donor concentration, indicate which one has the larger band gap and why:

a) A, as its intrinsic range starts at a higher temperature with a steeper slope
b) B, as its intrinsic range starts at a lower temperature with a smaller slope
c) Both equal, as their flat ranges are at the same height
d) B, as its intrinsic slope is less steep, being $-2k/E_g$

### Answer

a

### Explanation

Session 13, Slide 43: the slope of the intrinsic range is $-E_g/2k$, so the steeper line (A) has the larger gap, and a larger gap makes the electrons cross it only at a higher temperature (smaller $1/T$), which is where A leaves the flat exhaustion range.

- b) The two features of the figure were read right but the conclusion was inverted: a smaller slope and a lower onset temperature belong to the smaller gap.
- c) The height of the flat range is set by the donor concentration, which is the same; the band gap is read from the intrinsic range.
- d) The slope was taken as $-2k/E_g$: it is $-E_g/2k$, proportional to the gap.

### Source

Session 13, Slides 29 and 43.

## Q56.5 Conductivity in the exhaustion range

- id: B56-Q5
- concept_id: u6-exhaustion-mobility
- format: cause-effect
- asks: cause

In the exhaustion range of an n-type semiconductor, the conductivity decreases slightly with temperature because:

a) Electrons return to the donor level as the temperature rises
b) The carrier number is constant while the thermal disorder lowers the mobility
c) Holes generated across the gap cancel part of the electron current
d) Donor atoms leave the lattice and so the carrier number falls

### Answer

b

### Explanation

Session 13, Slide 44: at moderate to high temperature all the donors are already ionised, so the number of carriers stays constant while the disordering effect of temperature lowers the mobility; with $\sigma = n|q_e|\mu_e$, $\sigma$ decreases slightly.

- a) The freeze-out behaviour of low temperatures was applied: the electrons leave the donors as $T$ rises, they do not return to them.
- c) Holes created across the gap add to $\sigma$ (intrinsic range); they do not cancel the electron current.
- d) The impurity atoms stay in the lattice, so the number of ionised donors cannot fall.

### Source

Session 13, Slides 43 and 44.

## Q56.6 First semiconductor to become intrinsic

- id: B56-Q6
- concept_id: u6-intrinsic-onset-gap
- format: identify
- asks: comparison

Four n-type samples have the same donor concentration. From the band gaps of the table, indicate which one starts to behave as an intrinsic semiconductor at the lowest temperature:

| Material | $E_g$ (eV) |
| :--- | :--- |
| Si | 1.11 |
| Ge | 0.67 |
| GaAs | 1.42 |
| InSb | 0.17 |

a) Germanium
b) Silicon
c) Gallium arsenide
d) Indium antimonide

### Answer

d

### Explanation

Session 13, Slides 33 and 43: the intrinsic range starts when the electrons excited across the gap, $\propto\exp(-E_g/2kT)$, outnumber those of the donors; the smaller the gap, the lower the temperature at which this happens. InSb has the smallest gap (0.17 eV).

- a) Germanium has the second smallest gap (0.67 eV), not the smallest.
- b) Silicon, the best-known elemental semiconductor, has a larger gap (1.11 eV) than Ge and InSb.
- c) The largest gap was chosen, which gives the highest onset temperature, not the lowest.

### Source

Session 13, Slides 33, 43 and 44.

## Q56.7 Joining two doped crystals

- id: B56-Q7
- concept_id: u6-pn-junction-pairs
- format: identify
- asks: application

Which one of the following pairs of doped crystals, when joined, forms a p-n junction?

a) Silicon with boron and silicon with phosphorus
b) Germanium with antimony and germanium with arsenic
c) Silicon with aluminium and silicon with indium
d) Silicon with phosphorus and pure silicon

### Answer

a

### Explanation

Session 13, Slides 36, 37 and 45: a p-n junction is the interface between p-type and n-type material. Boron (group IIIA) gives p-type silicon and phosphorus (group VA) gives n-type silicon.

- b) Antimony and arsenic are both group VA donors, so both crystals are n-type.
- c) Aluminium and indium are both group IIIA acceptors, so both crystals are p-type.
- d) Pure silicon is intrinsic, not p-type, so the interface is between an n-type and an intrinsic crystal.

### Source

Session 13, Slides 36, 37 and 45.

## Q56.8 LED materials with a larger gap than GaP

- id: B56-Q8
- concept_id: u6-led-gap-comparison
- format: complete-sentence
- asks: classification

Among the LED materials of the slide, the two whose band gap is larger than that of the green GaP are:

a) AlGaAs and ZnSe
b) AlGaAs and diamond
c) SiC and diamond
d) AlGaAs and SiC

### Answer

c

### Explanation

Session 13, Slide 47: the band gap increases down the list, and the emitted wavelength falls with it: AlGaAs (red and infrared) lies above GaP (green), while SiC (blue) and diamond (ultraviolet) lie below, so both have a larger gap.

- a) AlGaAs has the smaller gap (red and infrared) and ZnSe the larger one; one of the two is wrong.
- b) AlGaAs emits red and infrared light, which needs a gap smaller than that of GaP.
- d) SiC is right, but AlGaAs again has the smaller gap.

### Source

Session 13, Slide 47.

## Q56.9 Resistance of a germanium thermistor

- id: B56-Q9
- concept_id: u6-thermistor-resistance
- format: cause-effect
- asks: effect

With an increase in temperature, the electrical resistance of a thermistor made of intrinsic germanium:

a) Rises, as the mobility of the carriers falls
b) Rises, as the number of carriers falls
c) Falls, as the mobility of the carriers rises
d) Falls, as more electron-hole pairs are generated

### Answer

d

### Explanation

Session 13, Slides 29 and 48: in an intrinsic semiconductor $n = p = n_i \propto \exp(-E_g/2kT)$ grows with $T$ and this effect masks the loss of mobility, so $\sigma$ rises by orders of magnitude (chart of Slide 48) and the resistance falls. This large change is what a thermistor uses.

- a) The behaviour of a metal was applied: there the mobility falls and the conductivity decreases slightly (aluminium in the chart).
- b) The trend of the carrier number was inverted: it increases with temperature.
- c) Right trend with a wrong cause: the thermal disorder lowers the mobility, it does not raise it.

### Source

Session 13, Slides 29 and 48.

## Q56.10 Device that amplifies signals

- id: B56-Q10
- concept_id: u6-transistor-function
- format: complete-sentence
- asks: definition

Which one of the following semiconductor devices can be used to amplify electrical signals?

a) The light emitting diode
b) The thermistor
c) The photovoltaic cell
d) The transistor

### Answer

d

### Explanation

Session 13, Slide 49: a transistor is a semiconductor device that can be used to amplify electrical signals.

- a) The LED emits monochromatic light when it is directly polarised (Slide 47).
- b) The thermistor uses the change of conductivity with temperature (Slide 48).
- c) The photovoltaic cell uses the excitation of electrons by light of energy near $E_g$ (Slide 46).

### Source

Session 13, Slides 46-49.
