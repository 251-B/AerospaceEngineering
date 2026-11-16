---
materia: Aerospace Materials I
tema: "Unit 7: factors that change the loop, Curie and Néel temperatures, superconductors"
bank_id: B60
title: "Loop factors, Curie and Néel temperatures and superconductors"
category: mt2_test_block
unit: 7
concepts:
  - u7-grain-size-loop-effect
  - u7-inclusions-dislocations-pores
  - u7-heating-below-curie-loop
  - u7-curie-margin-calc
  - u7-curie-recording-comparison-calc
  - u7-curie-table-working-temperature
  - u7-neel-table-working-temperature
  - u7-superconductor-tc-limit-calc
  - u7-type-ii-materials
  - u7-mixed-state-hc1-hc2
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 15, Slides 20-25 and 28-29, and Problems T6 and T7, Problem 12."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-7
---

# Bank B60 — Loop factors, Curie and Néel temperatures and superconductors

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 15, Slides 20-25 and 28-29. Kelvin and Celsius: use 0 °C = 273 K.

## Q60.1 Effect of the grain size on the loop

- id: B60-Q1
- concept_id: u7-grain-size-loop-effect
- format: what-happens
- asks: effect

With an increase in the grain size of a soft ferromagnetic alloy of fixed composition, the following changes take place:

a) the permeability decreases, while the coercivity and the remanence increase
b) the permeability, the coercivity and the remanence all increase
c) the permeability increases, while the coercivity and the remanence decrease
d) the permeability and the remanence decrease, while the coercivity increases

### Answer

c

### Explanation

Slide 21: a larger grain has fewer grain boundaries, so the mobility of the Bloch walls increases; as a consequence the permeability increases and $H_c$ and $B_r$ decrease (Problems T6 and T7, Problem 12, column of grain size).

- a) This is the effect of more inclusions, dislocations or pores, not of larger grains.
- b) All three properties are moved in the same direction, as if an easier wall motion also made the magnet harder to demagnetize.
- d) Mixed trends: easier wall motion lowers the coercivity, so it cannot go together with a lower permeability.

### Source

Session 15, Slide 21; Problems T6 and T7, Problem 12.

## Q60.2 Dislocations introduced by cold working

- id: B60-Q2
- concept_id: u7-inclusions-dislocations-pores
- format: cause-effect
- asks: cause

Cold working introduces dislocations in a soft magnetic alloy of fixed composition; therefore the Bloch walls:

a) move less easily, so the permeability falls and the coercivity rises
b) move more easily, so the permeability rises and the coercivity falls
c) move less easily, so the permeability falls and the coercivity falls
d) move more easily, so the permeability rises and the coercivity rises

### Answer

a

### Explanation

Slides 20-21: inclusions, dislocations and pores hinder the movement of the Bloch walls, so the mobility decreases, the permeability decreases and $H_c$ (and $B_r$) increase. Strains from mechanical deformation are a factor of the loop (Slide 20).

- b) Describes the effect of larger grains, not of extra defects.
- c) Right cause, but the coercivity is given the same trend as the permeability; harder wall motion needs a larger reverse field.
- d) Wrong cause for the right direction of the coercivity: defects do not ease the wall motion.

### Source

Session 15, Slides 20-21; Problems T6 and T7, Problem 12.

## Q60.3 Heating a ferromagnet below its Curie temperature

- id: B60-Q3
- concept_id: u7-heating-below-curie-loop
- format: what-happens
- asks: effect

When a ferromagnet is heated from room temperature to a temperature still below $T_c$, its hysteresis cycle changes as follows:

a) $M_s$ decreases, while $B_r$ and $H_c$ increase
b) $M_s$ remains constant, while $B_r$ and $H_c$ decrease
c) $M_s$ and $B_r$ decrease, while $H_c$ increases
d) $M_s$, $B_r$ and $H_c$ all decrease

### Answer

d

### Explanation

Slide 22: the thermal agitation reduces the maximum alignment of the dipoles reached under the field ($M_s$ falls) and makes it difficult to keep them aligned when the field disappears ($B_r$ and $H_c$ are reduced).

- a) Only the trend of $M_s$ is right; the remanence and the coercivity are given the opposite one.
- b) The constancy of $M_s$ holds for a given composition at fixed conditions (Slide 20), but not when the temperature changes.
- c) The coercivity is given the trend of a hardening process, but heating reduces it.

### Source

Session 15, Slides 20 and 22.

## Q60.4 Margin of cobalt below its Curie temperature

- id: B60-Q4
- concept_id: u7-curie-margin-calc
- format: numeric
- asks: calculation
- calc: 1404-(1000+273)

Cobalt has $T_c = 1404$ K (Slide 23). A cobalt part works at 1000 °C. Determine by how many kelvin the working temperature is below $T_c$:

a) 404 K
b) 131 K
c) 677 K
d) 1131 K

### Answer

b

### Explanation

The working temperature is $1000 + 273 = 1273$ K, so the margin is $1404 - 1273 = 131$ K and the part is still ferromagnetic (Slide 23).

- a) The 1000 is subtracted from 1404 without converting °C to K.
- c) The conversion is made in the wrong direction ($1000 - 273 = 727$ K), giving $1404 - 727 = 677$ K.
- d) $T_c$ is converted to °C ($1404 - 273 = 1131$ °C) and that value is reported as the margin.

### Source

Session 15, Slide 23.

## Q60.5 Nickel against barium ferrite

- id: B60-Q5
- concept_id: u7-curie-recording-comparison-calc
- format: numeric
- asks: calculation
- calc: 631-(350+273)

The Curie temperature of nickel is 631 K (Slide 23) and that of the barium ferrite recording powder is 350 °C (Slide 24). Determine by how many kelvin the $T_c$ of nickel is above that of the barium ferrite:

a) 8 K
b) 281 K
c) 554 K
d) 904 K

### Answer

a

### Explanation

Barium ferrite: $350 + 273 = 623$ K, so the difference is $631 - 623 = 8$ K. Both values must be in the same scale before subtracting.

- b) The 350 °C is subtracted from 631 K directly, mixing scales.
- c) The conversion of the barium ferrite is made in the wrong direction ($350 - 273 = 77$ K), giving $631 - 77 = 554$ K.
- d) The kelvin value of nickel is treated as if it were in °C and converted again ($631 + 273 = 904$ K), which is then the number reported.

### Source

Session 15, Slides 23 and 24.

## Q60.6 Ferromagnetic metals at 400 °C

- id: B60-Q6
- concept_id: u7-curie-table-working-temperature
- format: diagram-reading
- asks: classification

Using the shown Curie temperatures (Slide 23), indicate which metals are ferromagnetic at 400 °C:

| Metal | Fe | Co | Ni | Gd |
| :--- | ---: | ---: | ---: | ---: |
| $T_c$ (K) | 1043 | 1404 | 631 | 289 |

a) Fe, Co and Ni ferromagnetic; Gd paramagnetic
b) Fe and Co ferromagnetic; Ni and Gd paramagnetic
c) Ni and Gd ferromagnetic; Fe and Co paramagnetic
d) Fe, Co, Ni and Gd all ferromagnetic

### Answer

b

### Explanation

400 °C = 673 K. A material is ferromagnetic below $T_c$ and paramagnetic above it (Slide 23): Fe (1043 K) and Co (1404 K) are below $T_c$; Ni (631 K) and Gd (289 K) are above it.

- a) The 400 is compared with the kelvin values without converting; then only Gd (289 K) falls below it.
- c) Inverted comparison: the metals with $T_c$ below the working temperature are called ferromagnetic.
- d) The conversion is made in the wrong direction ($400 - 273 = 127$ K), which is below all four values.

### Source

Session 15, Slide 23.

## Q60.7 Antiferromagnet at 100 °C

- id: B60-Q7
- concept_id: u7-neel-table-working-temperature
- format: diagram-reading
- asks: classification

Using the shown Néel temperatures (Slide 23), indicate which material is still antiferromagnetic at 100 °C:

| Material | α-Mn | MnO | Cr | NiO |
| :--- | ---: | ---: | ---: | ---: |
| $T_N$ (K) | 100 | 116 | 310 | 523 |

a) α-Mn
b) MnO
c) Cr
d) NiO

### Answer

d

### Explanation

100 °C = 373 K. An antiferromagnet becomes paramagnetic above its Néel temperature (Slide 23), so only NiO (523 K) is still ordered; Cr (310 K) and the other two are paramagnetic.

- a) Inverted choice: the lowest Néel temperature is taken as the most robust ordering.
- b) The 116 is compared with 100 as if both were in the same scale (K against °C).
- c) The 310 is compared with 100 in the same way; Cr is paramagnetic above 310 K = 37 °C.

### Source

Session 15, Slide 23.

## Q60.8 Highest critical temperature in °C

- id: B60-Q8
- concept_id: u7-superconductor-tc-limit-calc
- format: numeric
- asks: calculation
- calc: 165-273

Slide 25 states that the critical temperatures of superconductors range between 0.01 and 165 K. Express the upper limit in °C:

a) 438 °C
b) 165 °C
c) -108 °C
d) -208 °C

### Answer

c

### Explanation

$T\,(°\text{C}) = T\,(\text{K}) - 273 = 165 - 273 = -108$ °C: even the best known superconductor needs a very low temperature (Slide 25).

- a) The 273 is added instead of subtracted: $165 + 273 = 438$ °C.
- b) The kelvin value is reported as it is, without any conversion.
- d) The offset 373 (the boiling point of water in kelvin) is used in place of 273: $165 - 373 = -208$ °C.

### Source

Session 15, Slide 25.

## Q60.9 Type II superconductors

- id: B60-Q9
- concept_id: u7-type-ii-materials
- format: identify
- asks: classification

Which pair of materials are both Type II superconductors?

a) Nb-Ti and Nb₃Sn
b) Sn and Pb
c) Nb-Zr and Al
d) Hg and YBaCuO

### Answer

a

### Explanation

Slide 29: Type II are alloys (Nb-Zr, Nb-Ti), intermetallics (Nb₃Sn) and ceramics (YBaCuO). Slide 28: Type I are pure metals (Sn, Al, Pb, Hg).

- b) Both are pure metals, hence Type I.
- c) Nb-Zr is Type II but Al is a pure metal of Type I.
- d) YBaCuO is Type II but Hg is a pure metal of Type I; the student assumes the ceramic and the liquid metal go together.

### Source

Session 15, Slides 28-29.

## Q60.10 State between Hc1 and Hc2

- id: B60-Q10
- concept_id: u7-mixed-state-hc1-hc2
- format: what-happens
- asks: effect

A Type II superconductor below $T_c$ is placed in a field $H$ with $H_{c1} < H < H_{c2}$. The material is in:

a) a fully superconducting state, with the field totally expelled
b) a mixed state, with normal and superconducting regions together
c) a fully normal state, with the field completely penetrating it
d) a state with a sharp jump to the normal state at $H_{c1}$

### Answer

b

### Explanation

Slide 29: flux lines begin to penetrate at $H_{c1}$ and the penetration is complete at $H_{c2}$; between both fields normal and superconducting regions coexist (mixed state).

- a) This is the Meissner state, valid only below $H_{c1}$ (Slide 27).
- c) This is the state above $H_{c2}$, where the field penetration is complete.
- d) A sharp transition belongs to Type I superconductors (Slide 28), not to a gradual Type II one.

### Source

Session 15, Slides 27-29.
