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
  - u7-meissner-levitation-physics
  - u7-heat-capacity-structure-units
  - u7-iron-curie-heat-peak
  - u7-specific-heat-classes
  - u7-bimetal-cooling-invar
  - u7-expansion-melting-allotropy
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf, including Q6 (June 2012 final) and Q12 of MATERIALS_THIRDPARTIAL_2020_V2.pdf p. 5. Content from Session 15 Slides 25-27, 31-32, 34-39."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-7
---

# Bank B61 — Superconductor applications, heat capacity and thermal expansion

> [!info] Includes official exam questions
> Ten test questions written for the bank in the style of Part I of Assessment Test II, including official Unit 7 items from the June 2012 final and 2020 exam papers (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 15, Slides 25-27, 31-32 and 34-39.

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

Which one of the following is NOT a practical application of superconductors?

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

## Q61.5 Meissner effect and magnetic levitation

- id: B61-Q5
- concept_id: u7-meissner-levitation-physics
- format: topic-false
- asks: effect
- origin: official-exam

With respect to the Meissner effect and magnetic levitation above a cooled superconductor, which one of the following statements is FALSE:

a) Below $T_c$, a Type I superconductor carries zero resistance while allowing magnetic flux lines to pass freely through its bulk
b) Below $T_c$, the Meissner effect expels magnetic flux from the interior so the superconductor behaves as a perfect diamagnet
c) A permanent magnet can levitate above a cooled ceramic superconductor because Meissner repulsion balances gravity
d) Exceeding either the critical temperature $T_c$ or the critical field $H_c$ returns the superconductor to the normal state

### Answer

a

### Explanation

June 2012 extraordinary final exam, Q6 (and Session 15, Slides 26-28): below $T_c$ and $H_c$, the Meissner-Ochsenfeld effect pushes external magnetic field lines out around the superconductor rather than letting them pass through its interior, producing perfect diamagnetism. Statement a is false.

- b) True: flux expulsion turns the superconductor into a perfect diamagnet (Slide 27).
- c) True: Slide 27 illustrates a permanent magnet levitating above a liquid-nitrogen-cooled superconductor via Meissner repulsion.
- d) True: Slides 26 and 28 show that surpassing $T_c$, $H_c$, or $J_c$ destroys superconductivity.

### Source

MATERIALS_FINALEXAM_2012_EXTRA.pdf, p. 2 Q6; Session 15, Slides 26-28.

## Q61.6 Phonons, heat capacity and structural sensitivity

- id: B61-Q6
- concept_id: u7-heat-capacity-structure-units
- format: false-statement
- asks: classification

Which one of the following statements is FALSE regarding thermal energy, heat capacity $C$, and specific heat $c_p$ in solids?

a) Thermal energy in solids is stored as atomic vibrations that travel as lattice wave packets called phonons
b) Molar heat capacity $C$ refers to one mole of material, whereas specific heat $c_p$ refers to unit mass
c) Ferromagnetic solids such as iron display a pronounced peak in specific heat around the Curie temperature
d) Increasing dislocation density or refining grain size causes a large permanent rise in specific heat across all solids

### Answer

d

### Explanation

Session 15, Slides 34-35: the heat capacity and specific heat of most materials do not depend significantly on microstructural features such as dislocations, vacancies, or grain size (with ferromagnetic solids near $T_c$ being the main exception). Statement d is false.

- a) True: Slide 34 defines phonons as packets of elastic lattice-vibration waves carrying thermal energy.
- b) True: Slide 34 defines $C$ per mole and $c_p$ as heat capacity divided by atomic weight (per unit mass).
- c) True: Slide 35 explicitly notes the high specific heat of iron at its Curie temperature.

### Source

Session 15, Slides 34-35.

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

## Q61.8 Specific heat of polymers against heavy metals

- id: B61-Q8
- concept_id: u7-specific-heat-classes
- format: complete-sentence
- asks: cause

Polymers typically exhibit a significantly higher specific heat $c_p$ (per unit mass) than heavy metals such as tungsten or iron because:

a) specific heat divides molar heat capacity by molar mass, and polymers consist of much lighter elements such as C and H
b) polymers conduct thermal energy by free electrons, which absorb more heat per unit mass than lattice vibrations
c) heavy metals reach a lower molar plateau of $R$ above $\theta_D$, whereas polymers reach a higher plateau of $6R$
d) polymers undergo ferromagnetic transitions near room temperature that continuously raise their specific heat

### Answer

a

### Explanation

Session 15, Slides 34-35 and 38: above $\theta_D$, molar heat capacity approaches $C \approx 3R$ across solids, and specific heat is $c_p = C/M$. Because polymers are built from light atoms (C, H, N, O) rather than heavy transition-metal atoms (Fe, W), each kilogram contains far more moles of atoms and thus requires more heat per kg and kelvin.

- b) Polymers are thermal insulators with essentially no free electrons; heat travels by lattice phonons (Slide 40).
- c) The Dulong-Petit high-temperature plateau is $\approx 3R$ per mole of atoms, not $R$ for metals or $6R$ for polymers (Slide 35).
- d) Common polymers are non-ferromagnetic; the Curie-point specific-heat anomaly occurs in ferromagnets such as iron (Slide 35).

### Source

Session 15, Slides 34-35, 38 and 40.

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

## Q61.10 Thermal expansion coefficient and phase transformations

- id: B61-Q10
- concept_id: u7-expansion-melting-allotropy
- format: true-statement
- asks: effect
- origin: official-exam

Indicate which statement is TRUE regarding the thermal expansion coefficient ($\alpha$):

a) Ceramics do not experience thermal expansion
b) A stronger atomic bond conveys a higher thermal expansion
c) It can change abruptly during phase transformations
d) Metals with high melting temperatures have higher thermal expansion coefficients

### Answer

c

### Explanation

Session 15, Slide 37 (and `MATERIALS_THIRDPARTIAL_2020_V2.pdf`, p. 5 Q12): allotropic materials such as iron undergo abrupt dimensional changes when phase transformations occur (e.g., $\alpha \to \gamma \to \delta$), causing $\alpha$ to jump sharply at the transformation temperatures.

- a) False: ceramics expand when heated (for example $\text{Al}_2\text{O}_3$ has $\alpha = 7.6\times10^{-6}$ °C⁻¹ on Slide 38).
- b) False: stronger atomic bonding deepens the potential well and produces a *lower* thermal expansion coefficient (Slide 36).
- d) False: Slide 37 shows that metals with higher melting temperatures have *lower* thermal expansion coefficients because their bonding is stronger.

### Source

MATERIALS_THIRDPARTIAL_2020_V2.pdf, p. 5 Q12; Session 15, Slides 36-38.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
