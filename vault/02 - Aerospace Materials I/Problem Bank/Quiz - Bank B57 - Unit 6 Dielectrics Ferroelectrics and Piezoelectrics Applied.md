---
materia: Aerospace Materials I
tema: "Unit 6: dipole moment, capacitor geometry and permittivity table, insulators against dielectrics, dielectric strength, loss factor, ferroelectric loops, Curie temperature and piezoelectric devices (applied)"
bank_id: B57
title: "Dielectrics, ferroelectrics and piezoelectrics applied"
category: mt2_test_block
unit: 6
concepts:
  - u6-dipole-moment-charge-distance
  - u6-capacitor-circular-plates
  - u6-permittivity-table-ratio
  - u6-permittivity-plate-area-order
  - u6-insulator-against-dielectric
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

## Q57.1 Dipole moment of a pair of charges

- id: B57-Q1
- concept_id: u6-dipole-moment-charge-distance
- format: numeric
- asks: calculation
- calc: 3.2e-19*0.12e-9

A dipole is formed by two charges, $+q$ and $-q$ with $q = 3.2\times10^{-19}$ C, separated by a distance of 0.12 nm. Determine its dipole moment:

a) $1.92\times10^{-29}$ C·m
b) $3.84\times10^{-29}$ C·m
c) $7.68\times10^{-29}$ C·m
d) $3.84\times10^{-30}$ C·m

### Answer

b

### Explanation

Session 13, Slide 51: the dipole moment is $p = q\cdot d$, with $q$ the dipole charge and $d$ the separation between its positive and negative ends: $p = 3.2\times10^{-19}\cdot0.12\times10^{-9} = 3.84\times10^{-29}$ C·m.

- a) The charge of a single electron, $1.6\times10^{-19}$ C, was used instead of the stated $q$: $1.6\times10^{-19}\cdot0.12\times10^{-9} = 1.92\times10^{-29}$.
- c) The two charges were added, $2q\cdot d$: in $p = q\,d$ the charge $q$ is the magnitude of one end of the dipole.
- d) The nanometre was converted as $10^{-10}$ m (an ångström): the separation is ten times too small.

### Source

Session 13, Slide 51.

## Q57.2 Capacitor of circular plates with a PET film

- id: B57-Q2
- concept_id: u6-capacitor-circular-plates
- format: numeric
- asks: calculation
- calc: 3.2*8.85e-12*3.141592653589793*0.015**2/0.2e-3*1e12

A capacitor has two circular plates of 3.0 cm diameter separated by a PET film 0.20 mm thick ($\varepsilon_r = 3.2$, $\varepsilon_0 = 8.85\times10^{-12}$ F/m). Determine its capacitance:

a) 31.3 pF
b) 0.100 pF
c) 400 pF
d) 100 pF

### Answer

d

### Explanation

Session 13, Slides 52 and 57: $C = \varepsilon_r\varepsilon_0 A/d$ with $A = \pi(D/2)^2 = \pi(0.015)^2 = 7.07\times10^{-4}$ m² and $d = 0.20\times10^{-3}$ m: $C = 3.2\cdot8.85\times10^{-12}\cdot7.07\times10^{-4}/0.20\times10^{-3} = 1.00\times10^{-10}$ F $= 100$ pF.

- a) The dielectric constant was left out: $C_0 = \varepsilon_0 A/d = 31.3$ pF is the value with vacuum between the plates.
- b) The separation was left in mm ($d = 0.20$ taken as metres): the result is $10^{3}$ times too small.
- c) The diameter was used as the radius, $A = \pi D^2$: the area is four times too large.

### Source

Session 13, Slides 52 and 57.

## Q57.3 Capacitance ratio from the permittivity table

- id: B57-Q3
- concept_id: u6-permittivity-table-ratio
- format: numeric
- asks: calculation
- calc: 700/6.0

The table gives the relative permittivity of several materials:

| Material | $\varepsilon_r$ |
| --- | --- |
| BaTiO₃ | 4000 |
| KNbO₃ | 700 |
| Rochelle salt | 170 |
| Al₂O₃ | 10 |
| Porcelain | 6.0 |
| PET | 3.2 |

Two capacitors have identical plates and separation, one filled with KNbO₃ and the other with porcelain. Determine the ratio $C_{KNbO_3}/C_{porcelain}$:

a) 117
b) 28.3
c) 667
d) 1.67

### Answer

a

### Explanation

Session 13, Slides 52 and 57: with the same $A$ and $d$, $C = \varepsilon_r\varepsilon_0 A/d$ is proportional to $\varepsilon_r$, so $C_{KNbO_3}/C_{porcelain} = 700/6.0 = 117$.

- b) The value of Rochelle salt was used in place of KNbO₃: $170/6.0 = 28.3$.
- c) The value of BaTiO₃, the first row of the table, was used: $4000/6.0 = 667$.
- d) The value of Al₂O₃ was used for the porcelain-to-KNbO₃ pair: $10/6.0 = 1.67$.

### Source

Session 13, Slides 52 and 57.

## Q57.4 Plate area needed for the same capacitance

- id: B57-Q4
- concept_id: u6-permittivity-plate-area-order
- format: ordering
- asks: comparison

Three capacitors must have the same capacitance and the same plate separation, using PET, Rochelle salt or Al₂O₃ as dielectric ($\varepsilon_r$ = 3.2, 170 and 10, respectively). Ranked from the smallest to the largest plate area required, they are:

a) PET, Al₂O₃, Rochelle salt
b) Al₂O₃, Rochelle salt, PET
c) Rochelle salt, Al₂O₃, PET
d) Rochelle salt, PET, Al₂O₃

### Answer

c

### Explanation

Session 13, Slides 52 and 57: from $C = \varepsilon_r\varepsilon_0 A/d$, a fixed $C$ and $d$ give $A = Cd/(\varepsilon_r\varepsilon_0)$, so the area is inversely proportional to $\varepsilon_r$: the largest $\varepsilon_r$ (Rochelle salt, 170) needs the smallest area and the smallest (PET, 3.2) the largest.

- a) The order was inverted: it ranks by increasing $\varepsilon_r$, which is the order of increasing capacitance, not of increasing area required.
- b) The first two were swapped: Al₂O₃ ($\varepsilon_r = 10$) cannot need less area than Rochelle salt (170).
- d) The last two were swapped: PET ($\varepsilon_r = 3.2$) needs more area than Al₂O₃ (10).

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

a) 0.171 kV
b) 16.4 kV
c) 33.6 kV
d) 5.83 kV

### Answer

c

### Explanation

Session 13, Slide 53: $E_{break} = U_{break}/d$, so $U_{break} = E_{break}\,d = 14\ \text{kV/mm}\cdot2.4\ \text{mm} = 33.6$ kV.

- a) The ratio was inverted, $d/E_{break} = 2.4/14$: the units of the result would not be kV.
- b) The strength and the thickness were added, $14 + 2.4 = 16.4$, instead of multiplied.
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
