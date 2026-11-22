---
materia: Aerospace Materials I
tema: "Unit 6: ln sigma against 1/T of extrinsic semiconductors, onset of the intrinsic range and semiconductor devices"
bank_id: B56
title: "Extrinsic conductivity against temperature and devices"
category: mt2_test_block
unit: 6
concepts:
  - u6-extrinsic-temperature-regions
  - u6-extrinsic-slopes
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

## Q56.1 Three temperature regimes of an extrinsic semiconductor

- id: B56-Q1
- concept_id: u6-extrinsic-temperature-regions
- format: topic-true
- asks: comparison

With respect to the three temperature regimes of an extrinsic semiconductor on a $\ln\sigma$ against $1/T$ plot, indicate which statement is TRUE:

a) In the low-temperature extrinsic range, all dopant atoms are already ionised and conductivity remains flat
b) In the exhaustion range, conductivity climbs steeply with slope $-E_g/2k$ as valence electrons cross the gap
c) In the extrinsic range $\sigma$ rises as dopants ionise, plateaus during exhaustion, and becomes intrinsic at very high $T$
d) In the high-temperature intrinsic range, conductivity drops sharply because thermal vibrations destroy dopant ions

### Answer

c

### Explanation

Session 13, Slides 43-44: on heating from low temperature, $\sigma$ first grows in the extrinsic range as dopants ionise; once all impurities are ionised it reaches the flat exhaustion/saturation range; at very high temperature excitation across $E_g$ dominates in the intrinsic range.

- a) Describes the intermediate-temperature exhaustion (or saturation) plateau, not the low-temperature extrinsic range.
- b) Assigns the high-temperature intrinsic slope $-E_g/2k$ to the flat exhaustion range.
- d) Inverts the high-temperature intrinsic trend: intrinsic carrier generation across $E_g$ drives $\sigma$ steeply upward.

### Source

Session 13, Slides 43-44.

## Q56.2 Arrhenius slopes of a doped semiconductor

- id: B56-Q2
- concept_id: u6-extrinsic-slopes
- format: topic-false
- asks: cause

Regarding the Arrhenius plot of $\ln\sigma$ against $1/T$ for an extrinsic semiconductor, indicate which statement is FALSE:

a) The high-temperature intrinsic slope equals $-E_g/2k$, matching that of the pure semiconductor host
b) Increasing the dopant concentration makes the slope of the low-temperature extrinsic line steeper
c) The extrinsic slope $-(E_c - E_d)/2k$ is far gentler than the intrinsic slope because $E_c - E_d \ll E_g$
d) Across the exhaustion plateau, conductivity can dip slightly as temperature rises due to reduced carrier mobility

### Answer

b

### Explanation

Session 13, Slide 43: in the extrinsic range $\ln\sigma = \ln\sigma_0 - (E_c - E_d)/(2kT)$ (or with $E_a - E_v$), so the slope depends on the dopant ionisation energy while changing dopant concentration shifts the curve vertically ($\sigma_0$) rather than steepening the slope. Statement b) is false.

- a) True (Slide 43): intrinsic generation across $E_g$ gives slope $-E_g/2k$ regardless of doping.
- c) True (Slides 40 and 43): shallow donor/acceptor energies are $\sim 0.04$ eV against $E_g \sim 1.1$ eV in Si.
- d) True (Slide 44): with all dopants ionised ($n$ fixed), lattice scattering lowers $\mu$ and causes a slight drop in $\sigma$.

### Source

Session 13, Slides 40 and 43-44.

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
| Diamond | 6.0 |

a) Germanium
b) Silicon
c) Gallium arsenide
d) Diamond

### Answer

a

### Explanation

Session 13, Slides 8, 33 and 43: the intrinsic range starts when the electrons excited across the gap, $\propto\exp(-E_g/2kT)$, outnumber those of the donors; the smaller the gap, the lower the temperature at which this happens. Germanium has the smallest gap of the four ($0.67$ eV).

- b) Silicon has a larger band gap ($1.11$ eV) than germanium, so intrinsic generation overtakes doping at a higher temperature.
- c) Gallium arsenide ($1.42$ eV) needs a higher temperature than both Ge and Si to reach the intrinsic regime.
- d) Diamond has the widest gap ($6.0$ eV), giving the highest onset temperature rather than the lowest.

### Source

Session 13, Slides 8, 33 and 43-44.

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

## Q56.8 Light-emitting diode band gap and photon emission

- id: B56-Q8
- concept_id: u6-led-gap-comparison
- format: topic-true
- asks: cause

Referring to a light-emitting diode (LED) formed by a forward-biased p-n junction, indicate which statement is TRUE:

a) Raising the forward bias current widens the band gap and shifts the emitted colour from red toward blue
b) Monochromatic light is emitted when valence electrons absorb heat and jump into the conduction band
c) Electrons and holes recombine at the junction, emitting photons whose energy and colour depend on $E_g$
d) Choosing a semiconductor with a larger band gap emits longer-wavelength light toward the infrared

### Answer

c

### Explanation

Session 13, Slide 47: in a forward-biased LED, electrons from the n side and holes from the p side recombine across the junction and release an energy equal to $E_g$ as a monochromatic photon, so the emitted colour is set by the band gap $E_g$.

- a) Forward current controls light intensity (number of recombinations), whereas $E_g$ fixes photon energy and colour.
- b) Describes thermal excitation (absorption of energy), the opposite of radiative electron-hole recombination.
- d) Inverts the photon energy-wavelength relation ($E_g = hc/\lambda$): a larger band gap emits shorter-wavelength light (toward blue/UV, Slide 47).

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
