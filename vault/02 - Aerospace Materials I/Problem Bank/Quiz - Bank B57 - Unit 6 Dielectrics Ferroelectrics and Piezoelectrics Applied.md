---
materia: Aerospace Materials I
tema: "Unit 6: dipole moment, capacitor geometry and permittivity table, insulators against dielectrics, dielectric strength, loss factor, ferroelectric loops, Curie temperature and piezoelectric devices (applied)"
bank_id: B57
title: "Dielectrics, ferroelectrics and piezoelectrics applied"
category: mt2_test_block
unit: 6
concepts:
  - u6-dielectric-polarisation
  - u6-dielectric-capacitance
  - u6-insulator-against-dielectric
  - u6-permittivity-plate-area-order
  - u6-dielectric-strength-voltage
  - u6-loss-factor-factors
  - u6-ferroelectric-loop-area-energy
  - u6-curie-temperature-barium-titanate
  - u6-piezoelectric-reverse-devices
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 13 Slides 51-60."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B57 — Dielectrics, ferroelectrics and piezoelectrics applied

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 13, Slides 51-60.

## Q57.1 Dipoles and polarisation in a dielectric

- id: B57-Q1
- concept_id: u6-dielectric-polarisation
- format: topic-true
- asks: definition

Regarding electrical dipoles and polarisation in a dielectric material, indicate which statement is TRUE:

a) Free conduction electrons drift across the insulator and gather at the positive plate to create a dipole moment
b) Without an electric field dipoles orient randomly; applying a field aligns them and induces opposite surface charges
c) Any common dielectric preserves full saturation polarisation permanently once the external electric field is turned off
d) Polarising a dielectric inside a capacitor lowers the charge stored on the plates at a fixed applied voltage

### Answer

b

### Explanation

Session 13, Slides 51-52: in a common dielectric without an applied field the dipoles point in random directions (zero net polarisation); an external field aligns the dipoles ($p = q\,d$) and generates surface charges ($-Q'$ and $+Q'$) that let the capacitor store more charge ($Q_0 + Q'$).

- a) Insulators/dielectrics lack free conduction electrons ($E_g > 2$ eV); polarisation shifts bound dipole charges locally.
- c) Permanent spontaneous polarisation after removing the field is a property of ferroelectrics (Slide 55), not of common dielectrics.
- d) Inverts the dielectric effect: polarisation increases capacitance $C = \varepsilon_r C_0$ and increases stored charge $Q = CV$.

### Source

Session 13, Slides 51-52 and 55.

## Q57.2 Capacitance change with separation and dielectric

- id: B57-Q2
- concept_id: u6-dielectric-capacitance
- format: what-happens
- asks: application
- check: 10*2 == 20

What will happen to the capacitance $C$ of a parallel-plate capacitor if the plate separation $d$ is halved and the vacuum between the plates is replaced by alumina ($\varepsilon_r = 10$):

a) It will increase 5 times, because $C = \varepsilon_r\varepsilon_0 d/A$ places $d$ in the numerator
b) It will decrease 20 times, because the dielectric opposes charge storage on the plates
c) It will increase 10 times, because plate separation $d$ cancels out when $\varepsilon_r$ is inserted
d) It will increase 20 times, because $C = \varepsilon_r\varepsilon_0 A/d$ scales with $\varepsilon_r$ and $1/d$

### Answer

d

### Explanation

Session 13, Slides 52 and 57: $C = \varepsilon_r\varepsilon_0 A/d = \varepsilon_r C_0$. Replacing vacuum with alumina multiplies $C$ by $\varepsilon_r = 10$, and halving the separation $d$ multiplies $C$ by $2$, giving $10\times 2 = 20$ times the initial capacitance.

- a) Inverts $d$ in the formula: $C$ is inversely proportional to plate separation $d$, so halving $d$ doubles $C$ rather than halving it.
- b) Inverts both factors: a dielectric increases stored charge and capacitance rather than reducing them.
- c) Ignores the geometric factor $1/d$, counting only the permittivity gain $\varepsilon_r = 10$.

### Source

Session 13, Slides 52 and 57.

## Q57.3 Dielectric, ferroelectric and piezoelectric materials

- id: B57-Q3
- concept_id: u6-insulator-against-dielectric
- format: topic-false
- asks: application

Regarding dielectric, ferroelectric and piezoelectric materials, indicate which statement is FALSE:

a) Electrical insulators separating high-voltage conductors require a very high permittivity $\varepsilon_r$ to store charge
b) Capacitor dielectrics benefit from a high permittivity $\varepsilon_r$ to maximise charge stored per unit area and voltage
c) Ferroelectric ceramics such as BaTiO$_3$ reach $\varepsilon_r$ orders of magnitude higher than polyethylene or alumina
d) Polymers such as polyethylene and ceramics such as alumina act as electrical insulators with wide band gaps

### Answer

a

### Explanation

Session 13, Slides 52, 54 and 57: an electrical insulator must have a **low** permittivity $\varepsilon_r$ to avoid polarisation, alongside high resistivity, high dielectric strength and a small loss factor; a high $\varepsilon_r$ is desired in capacitor dielectrics, not in insulators. Statement a) is false.

- b) True (Slide 52): $C = \varepsilon_r\varepsilon_0 A/d$, so high $\varepsilon_r$ raises capacitance.
- c) True (Slide 57): BaTiO$_3$ has $\varepsilon_r = 4000$ against $2.3$ for polyethylene and $10$ for Al$_2$O$_3$.
- d) True (Slides 5, 8 and 57): polyethylene and alumina are classic wide-gap insulating materials.

### Source

Session 13, Slides 5, 8, 52, 54 and 57.

## Q57.4 Plate area needed for the same capacitance

- id: B57-Q4
- concept_id: u6-permittivity-plate-area-order
- format: ordering
- asks: comparison

Three capacitors must have the same capacitance and the same plate separation, using polyethylene ($\varepsilon_r = 2.3$), alumina ($\varepsilon_r = 10$) or barium titanate ($\varepsilon_r = 4000$) as dielectric. Ranked from the smallest to the largest plate area required, they are:

a) Polyethylene, alumina, barium titanate
b) Alumina, barium titanate, polyethylene
c) Barium titanate, alumina, polyethylene
d) Barium titanate, polyethylene, alumina

### Answer

c

### Explanation

Session 13, Slides 52 and 57: from $C = \varepsilon_r\varepsilon_0 A/d$, a fixed $C$ and $d$ give $A = Cd/(\varepsilon_r\varepsilon_0)$, so the area is inversely proportional to $\varepsilon_r$: the largest $\varepsilon_r$ (BaTiO$_3$, 4000) needs the smallest plate area and the smallest (polyethylene, 2.3) the largest.

- a) The order was inverted: it ranks by increasing $\varepsilon_r$, which is the order of increasing capacitance at fixed area, not of increasing area required.
- b) The first two were swapped: alumina ($\varepsilon_r = 10$) cannot need less area than barium titanate ($4000$).
- d) The last two were swapped: polyethylene ($\varepsilon_r = 2.3$) needs more area than alumina ($10$).

### Source

Session 13, Slides 52 and 57.

## Q57.5 Insulator against capacitor dielectric

- id: B57-Q5
- concept_id: u6-insulator-against-dielectric
- format: true-statement
- asks: comparison

Which one of the following statements correctly contrasts an electrical insulator with a dielectric for capacitors?

a) The insulator needs a low permittivity, the dielectric needs intense dipoles that line up easily
b) The insulator needs a high permittivity, the dielectric needs intense dipoles that line up easily
c) The insulator needs a low permittivity, the dielectric needs a low permittivity too
d) The insulator needs intense dipoles that line up easily, the dielectric needs a high resistivity

### Answer

a

### Explanation

Session 13, Slides 52 and 54: an insulator separates conductors and should have a low permittivity, to avoid polarisation; a dielectric between the plates of a capacitor increases its capacitance and needs intense dipoles that line up easily with the electric field.

- b) The requirement of the capacitor was attributed to the insulator: a high permittivity means a strong polarisation, which an insulator must avoid.
- c) The dielectric was treated as an insulator: a low permittivity would give a capacitor with hardly any extra capacitance.
- d) The roles were swapped: easily aligned dipoles characterise the dielectric, and a high resistivity (to avoid current leaks) is a requirement of the insulator.

### Source

Session 13, Slides 52 and 54.

## Q57.6 Maximum voltage across an insulating sheet

- id: B57-Q6
- concept_id: u6-dielectric-strength-voltage
- format: numeric
- asks: calculation
- calc: 14*2.4

An insulating sheet 2.4 mm thick has a dielectric strength of 14 kV/mm. Determine the maximum voltage it can hold across its thickness without electrical breakdown:

a) 33.6 kV
b) 16.4 kV
c) 0.171 kV
d) 5.83 kV

### Answer

a

### Explanation

Session 13, Slide 53: $E_{break} = U_{break}/d$, so $U_{break} = E_{break}\,d = 14\ \text{kV/mm}\cdot2.4\ \text{mm} = 33.6$ kV.

- b) The strength and the thickness were added, $14 + 2.4 = 16.4$, instead of multiplied.
- c) The ratio was inverted, $d/E_{break} = 2.4/14$: the units of the result would not be kV.
- d) The strength was divided by the thickness, $E_{break}/d = 14/2.4$, instead of multiplied by it.

### Source

Session 13, Slide 53.

## Q57.7 Changes that do not raise the dielectric loss

- id: B57-Q7
- concept_id: u6-loss-factor-factors
- format: false-statement
- asks: cause

A capacitor works in an alternating current circuit. Which one of the following changes will NOT increase the electrical energy lost as heat in its dielectric?

a) Operating the capacitor at a higher temperature
b) Letting the dielectric absorb moisture
c) Raising the frequency of the current
d) Lowering the frequency of the current

### Answer

d

### Explanation

Session 13, Slide 53: the loss factor $\tan\delta$, the electrical energy lost as heat by friction among dipoles that try to reorient, increases with moisture, temperature and the frequency of the current; lowering the frequency therefore does not raise it.

- a) Temperature is one of the three factors listed on the slide: the loss factor rises with it.
- b) Moisture is also listed: a wet dielectric loses more energy, not less.
- c) A higher frequency makes the dipoles try to reorient more often, so the friction losses increase.

### Source

Session 13, Slide 53.

## Q57.8 Two ferroelectric loops

- id: B57-Q8
- concept_id: u6-ferroelectric-loop-area-energy
- format: diagram-reading
- asks: figure-reading

The shown polarisation against electric field loops belong to two ferroelectrics with the same remanent polarisation. Which one of the following statements is TRUE?

![[attachments/MAT-MT2/u6-b57-pe-pair.svg]]

a) Material 2 needs more energy to reorient its dipoles, as its loop is narrower
b) Material 1 needs more energy to reorient its dipoles, as its loop encloses more area
c) Material 1 has the larger remanent polarisation, as its loop is wider
d) Both need the same energy to reorient their dipoles, as they share the same remanent polarisation

### Answer

b

### Explanation

Session 13, Slide 56: the area under the hysteresis curve is related to the energy required to change the orientation of the dipoles; loop 1 is much wider and encloses a larger area than loop 2, so material 1 needs more energy per cycle.

- a) The reading of the width was inverted: a narrow loop encloses a small area and a small energy.
- c) Both loops cross the polarisation axis at the same height, so the remanent polarisation is equal; the width of the loop measures the coercive field, not $P_r$.
- d) The energy depends on the whole area of the loop, which differs, not on the remanent polarisation alone.

### Source

Session 13, Slide 56.

## Q57.9 Barium titanate on both sides of the Curie temperature

- id: B57-Q9
- concept_id: u6-curie-temperature-barium-titanate
- format: true-statement
- asks: application

Two BaTiO₃ samples, one at 80 °C and the other at 150 °C, are examined. Which one of the following statements is TRUE?

a) The 80 °C sample is cubic and unpolarised, and the 150 °C sample is tetragonal and polarised
b) The 80 °C sample is tetragonal and polarised, and the 150 °C sample is cubic and unpolarised
c) The 80 °C sample is tetragonal and polarised, and the 150 °C sample is tetragonal and unpolarised
d) Both are ferroelectric, as the Curie temperatures of ferroelectrics lie between $-200$ and 640 °C

### Answer

b

### Explanation

Session 13, Slide 56: BaTiO₃ has $T_c = 120$ °C; under 120 °C its structure is tetragonal and it keeps permanent dipoles, and above 120 °C it is cubic, the permanent dipoles disappear and the material becomes a common dielectric.

- a) The two structures were swapped between the temperatures: the tetragonal, polarised form belongs to the lower one.
- c) The loss of the dipoles was kept but not the change of structure: above 120 °C the crystal becomes cubic.
- d) The typical range of Curie temperatures of ferroelectrics ($-200$ to 640 °C) was read as a condition for being ferroelectric: each material has its own $T_c$, 120 °C for BaTiO₃, and above it the sample is no longer ferroelectric.

### Source

Session 13, Slide 56.

## Q57.10 Devices that use the reverse piezoelectric effect

- id: B57-Q10
- concept_id: u6-piezoelectric-reverse-devices
- format: identify
- asks: classification

In which pair are both devices based on the reverse piezoelectric effect, an electric field that changes the dimensions of the material?

a) A lighter and a microphone
b) A microphone and a hydrophone
c) A speaker transducer and an inkjet printer
d) A speaker transducer and a hydrophone

### Answer

c

### Explanation

Session 13, Slides 58-60: in the reverse effect an external electric field alters the dipoles and deforms the crystal structure, giving a dimensional change; the transducer of a speaker (voltage to motion) and the actuator of an inkjet printer (voltage pulse to a change of volume) work this way.

- a) Both devices turn a mechanical action into an electric signal (a shock gives a spark, sound pressure gives a voltage): the direct effect.
- b) Microphones and hydrophones sense pressure waves and generate a voltage from the stress: the direct effect, although both appear in the same list of Slide 60.
- d) The speaker is right but the hydrophone was taken as an emitter: it detects the pressure of sound in water, a direct effect.

### Source

Session 13, Slides 58-60.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
