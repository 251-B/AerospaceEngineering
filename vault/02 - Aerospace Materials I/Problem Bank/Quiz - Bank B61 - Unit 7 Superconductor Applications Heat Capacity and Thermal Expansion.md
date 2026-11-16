---
materia: Aerospace Materials I
tema: "Unit 7: superconductor envelope, Josephson effect and applications, heat capacity and specific heat, bimetals and Invar"
bank_id: B61
title: "Superconductor applications, heat capacity and thermal expansion"
category: mt2_test_block
unit: 7
concepts:
  - u7-sc-envelope-nb3sn
  - u7-josephson-junction-structure
  - u7-josephson-dc-voltage
  - u7-sc-applications-list
  - u7-sc-tc-kelvin-celsius
  - u7-molar-heat-capacity-iron
  - u7-iron-curie-heat-peak
  - u7-heat-cp-table-polymer
  - u7-bimetal-cooling-invar
  - u7-invar-expansion-difference
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content from Session 15 Slides 25-26, 31-32, 34-36, 38-39."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-7
---

# Bank B61 — Superconductor applications, heat capacity and thermal expansion

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 15, Slides 25-26, 31-32, 34-36, 38-39.

## Q61.1 Heating a Nb3Sn winding at its limit

- id: B61-Q1
- concept_id: u7-sc-envelope-nb3sn
- format: what-happens
- asks: effect

A Nb3Sn winding works at a point of its superconducting envelope (temperature, field, current density) close to the surface. If its temperature rises while the field and the current stay unchanged, the winding will most likely:

a) stay superconducting, as only the field limits the superconducting state
b) turn normal, as $H_c$ and $J_c$ both fall when the temperature rises
c) turn normal, as $H_c$ falls while $J_c$ rises with the temperature
d) stay superconducting, as $H_c$ and $J_c$ both rise with the temperature

### Answer

b

### Explanation

Session 15, Slide 26: the critical field $H_c$ and the critical current density $J_c$ both decrease with increasing temperature, so the envelope shrinks; the material is superconducting inside the envelope and normal outside. A point close to the surface is left outside when the temperature rises.

- a) The envelope is set by the three variables together (temperature, field and current density); the field is not the only limit.
- c) Only the trend of $J_c$ is inverted: the slide shows that $J_c$ falls with temperature just like $H_c$.
- d) Both trends are inverted: a higher temperature shrinks the envelope instead of enlarging it.

### Source

Session 15, Slide 26.

## Q61.2 Structure of a tunnel junction

- id: B61-Q2
- concept_id: u7-josephson-junction-structure
- format: complete-sentence
- asks: definition

In a Josephson tunnel junction, the two superconductors are separated by:

a) an insulating oxide layer about 3 nm thick
b) an insulating oxide layer about 3 µm thick
c) a normal-metal layer about 3 nm thick
d) a semiconductor layer about 3 nm thick

### Answer

a

### Explanation

Session 15, Slide 31: the Josephson (tunnel) effect occurs when current flows between two superconductors separated by a very thin insulating layer; the tunnel junction is a very thin oxide layer of about 3 nm.

- b) The thickness is off by a factor of 1000 (nm read as µm); a layer that thick would not let the pairs tunnel.
- c) The layer is an insulator, not a normal metal: tunnelling through an insulating barrier is what defines the effect.
- d) A semiconductor is confused with the insulating oxide barrier of the slide.

### Source

Session 15, Slide 31.

## Q61.3 Direct voltage across a junction

- id: B61-Q3
- concept_id: u7-josephson-dc-voltage
- format: what-happens
- asks: effect

A DC voltage is applied across a Josephson tunnel junction. What will be observed through the junction?

a) No current, because the oxide layer is an insulator
b) A steady DC current, because the junction obeys Ohm's law
c) An RF voltage, because a DC current is produced
d) An RF current oscillation, because the junction responds to the voltage

### Answer

d

### Explanation

Session 15, Slide 31: a DC voltage applied through the junction causes an RF current oscillation. The Josephson current also flows with no potential difference.

- a) The insulating layer is only about 3 nm thick, so current tunnels through it; Slide 31 gives a current even with zero voltage.
- b) The junction is not an ohmic resistor: the response to a DC voltage is oscillating, not steady.
- c) The two directions are swapped: it is an RF voltage applied through the junction that causes a DC current, not the reverse.

### Source

Session 15, Slide 31.

## Q61.4 Applications of superconductors

- id: B61-Q4
- concept_id: u7-sc-applications-list
- format: false-statement
- asks: classification

Which one of the following is NOT an application of superconductors given in the course?

a) Levitated transport
b) Electromagnets of magnetic resonance imaging
c) Resistive heating elements of electric furnaces
d) Filters for mobile phone base stations

### Answer

c

### Explanation

Session 15, Slide 32 lists levitated transport, powerful electromagnets for MRI, RF and microwave filters (for example for mobile phone base stations) and the particle accelerator. A superconductor has zero resistivity, so it cannot heat by the Joule effect.

- a) Levitated transport is the first application on the slide.
- b) MRI uses powerful superconducting electromagnets, as stated on the slide.
- d) RF and microwave filters for mobile phone base stations are listed on the slide.

### Source

Session 15, Slide 32.

## Q61.5 Highest critical temperature in degrees Celsius

- id: B61-Q5
- concept_id: u7-sc-tc-kelvin-celsius
- format: numeric
- asks: calculation
- calc: 165-273.15

Superconductors have critical temperatures between 0.01 K and 165 K. Express the upper limit in degrees Celsius:

a) -108 °C
b) 438 °C
c) -165 °C
d) 73.9 °C

### Answer

a

### Explanation

Session 15, Slide 25: $T_c$ ranges between 0.01 and 165 K. With $T(^\circ\mathrm{C}) = T(\mathrm{K}) - 273.15$: $165 - 273.15 = -108$ °C. Even the highest $T_c$ is far below room temperature.

- b) The 273 was added instead of subtracted.
- c) The kelvin value was copied as if it were already in °C.
- d) The conversion for degrees Fahrenheit, $(165 - 32)/1.8$, was applied to a temperature in kelvin.

### Source

Session 15, Slide 25.

## Q61.6 Molar heat capacity of iron

- id: B61-Q6
- concept_id: u7-molar-heat-capacity-iron
- format: numeric
- asks: calculation
- calc: 448*55.85/1000

The table of Slide 38 gives a specific heat $c_p = 448$ J/(kg·K) for iron, whose atomic weight is 55.85 g/mol. Determine its heat capacity per mole, to compare it with $3R \approx 24.9$ J/(mol·K):

a) 8.02 J/(mol·K)
b) 25.0 J/(mol·K)
c) $2.50\times10^{4}$ J/(mol·K)
d) $8.02\times10^{-3}$ J/(mol·K)

### Answer

b

### Explanation

Session 15, Slides 34, 35 and 38: specific heat is the heat capacity divided by the atomic weight, so $C = c_p\,M = 448\ \text{J/(kg·K)}\times 0.05585\ \text{kg/mol} = 25.0$ J/(mol·K), very close to the plateau $3R$ reached above the Debye temperature.

- a) The specific heat was divided by the atomic weight ($448/55.85$) instead of multiplied.
- c) The atomic weight was used in g/mol without converting to kg/mol: the result is 1000 times too large.
- d) Both slips together: division by the atomic weight and the g to kg conversion.

### Source

Session 15, Slides 34, 35 and 38.

## Q61.7 Peak of the heat capacity of iron

- id: B61-Q7
- concept_id: u7-iron-curie-heat-peak
- format: cause-effect
- asks: cause

The specific heat of iron shows a high value at one temperature. This is caused by:

a) the change from bcc to fcc structure, an allotropic transformation
b) the temperature reaching the Debye temperature of the lattice
c) the change from ferromagnetic to paramagnetic at the Curie temperature
d) the annealing of dislocations and vacancies of the metal

### Answer

c

### Explanation

Session 15, Slide 35: the heat capacity of most materials does not depend on structure, with one exception, ferromagnetic materials such as iron, which show a high specific heat at the Curie temperature, where they change from ferromagnetic to paramagnetic.

- a) The allotropic transformation of iron is visible in its expansion coefficient (Slide 37), not as the peak of the specific heat.
- b) Reaching the Debye temperature makes $C$ constant ($\approx 3R$), it does not produce a peak.
- d) Slide 35 says that dislocations and vacancies do not change the heat capacity significantly.

### Source

Session 15, Slide 35.

## Q61.8 Heating a nylon part

- id: B61-Q8
- concept_id: u7-heat-cp-table-polymer
- format: numeric
- asks: application
- calc: 20000/(0.50*1670)

Using $q = m\,c_p\,\Delta T$ and the specific heats of Slide 38 shown, determine the temperature rise of a 0.50 kg nylon 6,6 part that absorbs 20 kJ:

| Material | $c_p$ (J/(kg·K)) |
| :--- | :--- |
| Aluminum | 900 |
| Iron | 448 |
| 6,6-Nylon | 1670 |

a) 12.0 °C
b) 24.0 °C
c) 6.00 °C
d) 0.0240 °C

### Answer

b

### Explanation

Session 15, Slides 34 and 38: $\Delta T = q/(m\,c_p) = 20\,000/(0.50\times1670) = 24.0$ °C. Nylon has nearly twice the specific heat of aluminium (1670 against 900 J/(kg·K)), so a polymer needs more heat per kilogram and degree than a metal.

- a) The mass was left out: $20\,000/1670 = 12.0$ °C.
- c) The mass multiplied instead of dividing: $20\,000\times0.50/1670$.
- d) The heat was entered as 20 J instead of 20 kJ.

### Source

Session 15, Slides 34 and 38.

## Q61.9 Cooling an Invar-brass strip

- id: B61-Q9
- concept_id: u7-bimetal-cooling-invar
- format: what-happens
- asks: application

A straight bimetallic strip of Invar ($\alpha = 1.6\times10^{-6}$ °C⁻¹) bonded to brass ($\alpha = 20.0\times10^{-6}$ °C⁻¹) is cooled. What will happen?

a) It bends towards the Invar, as the brass contracts more
b) It bends towards the brass, as the brass contracts more
c) It bends towards the Invar, as the Invar contracts more
d) It stays straight, as both metals contract

### Answer

b

### Explanation

Session 15, Slides 36, 38 and 39: the bimetallic strip turns a temperature change into a displacement because its two metals have different α. On cooling, the brass (larger α) shortens more, so its face becomes the shorter, inner side and the strip bends towards the brass.

- a) The cause is right but the direction is wrong: the strip curves towards the metal that contracts more.
- c) The trend is inverted: Invar has the lower α, so it contracts less than brass.
- d) Both metals contract, but by different amounts, and the bonding forces the strip to bend.

### Source

Session 15, Slides 36, 38 and 39.

## Q61.10 Invar against steel

- id: B61-Q10
- concept_id: u7-invar-expansion-difference
- format: numeric
- asks: comparison
- calc: (12.0-1.6)*1e-6*800*60

A 0.800 m rod of Invar and a 0.800 m rod of 1025 steel are heated freely by 60 °C. Using the α of the table of Slide 38 shown, determine the difference between their elongations:

| Material | $\alpha$ ($10^{-6}$ °C⁻¹) |
| :--- | :--- |
| Invar (64Fe-36Ni) | 1.6 |
| 1025 Steel | 12.0 |
| Super Invar | 0.72 |

a) 0.499 mm
b) 0.0768 mm
c) 0.576 mm
d) 0.653 mm

### Answer

a

### Explanation

Session 15, Slides 36 and 38: $\Delta l = \alpha\,l_0\,\Delta T$ for each rod, so $\Delta l_{steel} - \Delta l_{Invar} = (12.0-1.6)\times10^{-6}\times800\ \text{mm}\times60 = 0.499$ mm.

- b) Only the elongation of the Invar rod was computed ($1.6\times10^{-6}\times800\times60$).
- c) Only the elongation of the steel rod was computed ($12.0\times10^{-6}\times800\times60$).
- d) The two coefficients were added (13.6) instead of subtracted.

### Source

Session 15, Slides 36 and 38.
