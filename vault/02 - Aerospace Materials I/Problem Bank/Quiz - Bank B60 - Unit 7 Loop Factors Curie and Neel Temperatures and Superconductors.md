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
  - u7-curie-neel-comparison
  - u7-curie-thermal-agitation
  - u7-curie-table-working-temperature
  - u7-neel-table-working-temperature
  - u7-superconductivity-meissner-relationship
  - u7-type-ii-materials
  - u7-mixed-state-hc1-hc2
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf, including adaptations of Q7 (Jan 2012 final) and Q6B/Q8b (June 2013 & June 2015 finals). Content and data from Session 15, Slides 20-29."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-7
---

# Bank B60 — Loop factors, Curie and Néel temperatures and superconductors

> [!info] Includes official exam questions
> Ten test questions written for the bank in the style of Part I of Assessment Test II, including adaptations from the 2012, 2013 and 2015 final exams (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 15, Slides 20-29. Kelvin and Celsius: use 0 °C = 273 K.

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

## Q60.4 Curie vs. Néel temperatures and operating limits

- id: B60-Q4
- concept_id: u7-curie-neel-comparison
- format: topic-true
- asks: comparison
- origin: official-exam

With respect to Curie and Néel temperatures in magnetic materials, which one of the following statements is TRUE:

a) The Curie temperature applies to antiferromagnets and the Néel temperature to ferromagnets, marking where each gains permanent order
b) The Curie temperature marks where ferromagnets and ferrimagnets become paramagnetic, whereas the Néel temperature marks that transition for antiferromagnets
c) Above the Curie or Néel temperature, dipoles lock into a rigid antiparallel lattice, making these the minimum operating temperatures
d) Knowing $T_c$ or $T_N$ defines the temperature where electrical resistivity drops to zero rather than the upper limit of magnetic ordering

### Answer

b

### Explanation

January 2012 final exam, Q7 (and Session 15, Slide 23): the Curie temperature $T_c$ is the temperature above which ferromagnetic and ferrimagnetic materials become paramagnetic, whereas the Néel temperature $T_N$ is the analogous transition temperature for antiferromagnetic materials. Knowing them fixes the upper service-temperature limit beyond which spontaneous magnetic order is lost.

- a) Swaps Curie and Néel temperatures and reverses what happens above them (order is lost, not gained).
- c) Inverts the thermal effect: above $T_c$ or $T_N$, thermal energy destroys macroscopic ordering rather than locking dipoles in place.
- d) Confuses the magnetic Curie/Néel transition with the critical temperature $T_c$ of a superconductor (Slide 25).

### Source

MATERIALS_FINALEXAM_2012_ORD.pdf, p. 3 Q7; Session 15, Slides 23 and 25.

## Q60.5 Thermal agitation and reversibility at the Curie point

- id: B60-Q5
- concept_id: u7-curie-thermal-agitation
- format: topic-false
- asks: cause

Regarding the Curie temperature $T_c$ and thermal agitation in ferromagnetic materials, which one of the following statements is FALSE:

a) Thermal agitation opposes dipole alignment, so $M_s$ falls and drops abruptly to zero at $T_c$
b) Above $T_c$, dipoles can still align temporarily under an applied field, so the material behaves as paramagnetic
c) Once the field $H$ is removed above $T_c$, thermal energy randomizes the dipoles and no hysteresis loop remains
d) Heating past $T_c$ permanently destroys the atomic magnetic moments so ferromagnetism cannot recover upon cooling

### Answer

d

### Explanation

Session 15, Slides 22-23: heating above $T_c$ overcomes macroscopic dipole alignment through thermal agitation so the material becomes paramagnetic, but individual atomic dipoles remain intact and cooling back below $T_c$ restores spontaneous domain ordering. Statement d is false.

- a) True: Slide 23 states that thermal agitation misaligns dipoles until $M_s$ drops abruptly to zero at $T_c$.
- b) True: Slide 22 notes that above $T_c$ the dipoles still align with $H$, giving paramagnetic behaviour.
- c) True: Slide 22 notes that above $T_c$, when $H$ disappears, the alignments become random with no remanence.

### Source

Session 15, Slides 22-23.

## Q60.6 Ferromagnetic metals at 400 °C

- id: B60-Q6
- concept_id: u7-curie-table-working-temperature
- format: diagram-reading
- asks: classification

Using the Curie temperatures below, indicate which metals are ferromagnetic at 400 °C:

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

Using the Néel temperatures below, indicate which material is still antiferromagnetic at 100 °C:

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

## Q60.8 Superconductivity, critical temperature and magnetism

- id: B60-Q8
- concept_id: u7-superconductivity-meissner-relationship
- format: topic-true
- asks: definition
- origin: official-exam

Referring to superconductivity, the critical temperature $T_c$, and the Meissner effect, which one of the following statements is TRUE:

a) Below $T_c$, electrical resistivity drops to zero while external magnetic flux lines concentrate inside the material like a ferromagnet
b) Above $T_c$, a metal becomes superconducting and the Meissner effect forces all magnetic field lines into its interior
c) Below $T_c$, electrical resistivity drops to zero and the Meissner effect expels magnetic flux lines, yielding perfect diamagnetism
d) At $T_c$, electrical resistivity rises sharply while the material loses its induced diamagnetism and becomes permanently ferromagnetic

### Answer

c

### Explanation

June 2013 extraordinary final exam (Q6B) and June 2015 extraordinary final exam (Q8b), with Session 15, Slides 25 and 27: $T_c$ is the critical temperature below which electrical resistivity vanishes; in the superconducting state, the Meissner-Ochsenfeld effect expels external magnetic flux lines from the bulk, producing perfect diamagnetism.

- a) Confuses perfect diamagnetism with ferromagnetism: flux lines are pushed out around the superconductor, not concentrated inside.
- b) Inverts both the temperature condition (superconductivity occurs below $T_c$, not above) and the flux-expulsion direction.
- d) Inverts the resistivity drop at $T_c$ and wrongly associates the transition with ferromagnetism.

### Source

MATERIALS_FINALEXAM_2013_EXTRA.pdf, p. 3 Q6B; MATERIALS_FINALEXAM_2015_EXTRA.pdf, p. 9 Q8b; Session 15, Slides 25 and 27.

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

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
