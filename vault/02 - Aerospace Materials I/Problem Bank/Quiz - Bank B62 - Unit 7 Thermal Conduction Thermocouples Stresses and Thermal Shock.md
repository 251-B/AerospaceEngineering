---
materia: Aerospace Materials I
tema: "Unit 7: thermal conductivity, Wiedemann-Franz law, thermocouples, thermal stresses and thermal shock resistance"
bank_id: B62
title: "Thermal conduction, thermocouples, thermal stresses and thermal shock"
category: mt2_test_block
unit: 7
concepts:
  - u7-k-classes-comparison
  - u7-fourier-conceptual-microstructure
  - u7-wf-conceptual-intuition
  - u7-k-alloy-electron-scattering
  - u7-k-porosity-ceramic
  - u7-thermocouple-principle
  - u7-thermal-stress-constrained-sign
  - u7-thermal-stress-length-independence
  - u7-thermal-shock-heating-surface
  - u7-tsr-ceramic-ordering
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content from Session 15 Slides 38 and 40-48."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-7
---

# Bank B62 — Thermal conduction, thermocouples, thermal stresses and thermal shock

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 15, Slides 38 and 40-48.

## Q62.1 Thermal conductivity in metals, ceramics and polymers

- id: B62-Q1
- concept_id: u7-k-classes-comparison
- format: topic-true
- asks: comparison

Referring to thermal conductivity in metals, ceramics and polymers, which one of the following statements is TRUE:

a) Ceramics and polymers typically conduct heat better than pure metals because covalent and ionic bonds vibrate faster
b) Pure metals generally show the highest thermal conductivity via free electrons, whereas polymers are poor conductors via phonons
c) Polymers have higher thermal conductivity than metals because their specific heat $c_p$ per kilogram is much higher
d) Metals and polymers both conduct heat primarily by free electrons, whereas ceramics conduct exclusively by ion diffusion

### Answer

b

### Explanation

Session 15, Slides 40-41: thermal energy is transferred by free electrons ($k_e$) and phonons ($k_{ph}$); pure metals have abundant free electrons ($k \approx k_e$, hundreds of W/(m·K)), whereas polymers and traditional ceramics lack free electrons and rely on less effective phonon conduction ($k \approx k_{ph}$, roughly 0.1–0.5 W/(m·K) for polymers).

- a) Inverts the classes: pure metals conduct far better than common ceramics and polymers because free-electron transport is much more effective than phonon transport.
- c) Confuses specific heat $c_p$ (heat stored per kg and degree) with thermal conductivity $k$ (rate of heat transfer).
- d) Wrong carriers: polymers lack free electrons and conduct by phonons, and conduction is not mass diffusion of ions.

### Source

Session 15, Slides 40-41.

## Q62.2 Fourier's law and microstructural sensitivity of k

- id: B62-Q2
- concept_id: u7-fourier-conceptual-microstructure
- format: topic-false
- asks: application

Regarding steady-state heat conduction and Fourier's law ($q = -k\,\Delta T/\Delta x$), which one of the following statements is FALSE:

a) Thermal conductivity $k$ is insensitive to microstructure, so impurities and porosity leave $k$ unchanged
b) The minus sign in Fourier's law indicates that thermal energy flows down the temperature gradient from hot to cold
c) The heat flux $q = Q/A$ is measured in W/m², whereas the thermal conductivity $k$ is measured in W/(m·K)
d) Raising the thermal conductivity $k$ increases the steady-state heat flux $q$ for a given temperature gradient

### Answer

a

### Explanation

Session 15, Slides 40 and 43: thermal conductivity $k$ is explicitly defined as a *microstructure-sensitive* property—impurities, alloying elements, dislocations, and porosity scatter electrons and phonons, reducing $k$ (unlike heat capacity, which is nearly structure-insensitive). Statement a is false.

- b) True: heat flux flows from the hot end towards the cold end (Slide 40).
- c) True: $q = Q/A$ has units of W/m², and $k$ has units of W/(m·K) (Slide 40).
- d) True: $q$ is directly proportional to $k$ at fixed $\Delta T/\Delta x$.

### Source

Session 15, Slides 40 and 43.

## Q62.3 Wiedemann-Franz relation and alloying

- id: B62-Q3
- concept_id: u7-wf-conceptual-intuition
- format: cause-effect
- asks: effect

According to the Wiedemann-Franz law ($L = k/(\sigma T)$), if alloying a pure metal at constant temperature reduces its electrical conductivity $\sigma$ to one third of its original value, its electronic thermal conductivity $k_e$ will:

a) triple, because $k_e$ and $\sigma$ are inversely proportional at constant temperature
b) remain unchanged, because thermal energy in metals is carried mainly by phonons
c) increase slightly, because alloying atoms supply extra free electrons
d) decrease to roughly one third, because free electrons carry both charge and heat

### Answer

d

### Explanation

Session 15, Slides 40-41: with the Lorenz number $L$ constant and temperature $T$ fixed, $k \approx k_e = L\sigma T$, so electronic thermal conductivity scales directly with electrical conductivity $\sigma$. Cutting $\sigma$ to one third by electron scattering cuts $k_e$ in the same proportion.

- a) Inverts the proportionality: $k = L\sigma T$ places $\sigma$ in the numerator, not the denominator.
- b) Wrong heat carrier for metals: in conductive metals, heat is carried predominantly by free electrons ($k \approx k_e$).
- c) Ignores impurity scattering: solute atoms act as defects that scatter conduction electrons and lower both $\sigma$ and $k$ (Slide 43).

### Source

Session 15, Slides 40-41 and 43.

## Q62.4 Nickel in copper

- id: B62-Q4
- concept_id: u7-k-alloy-electron-scattering
- format: cause-effect
- asks: cause

Pure copper has a thermal conductivity of about 400 W/(m·K), whereas a Cu-30% Ni solid-solution alloy drops to about 50 W/(m·K). The main reason for this drop is that the nickel atoms:

a) scatter the free electrons, which lowers their contribution to $k$
b) add free electrons that scatter the phonons of the lattice
c) lower the Lorentz number of the alloy, which lowers $k$
d) form pores that block the path of the heat

### Answer

a

### Explanation

Session 15, Slides 40 and 43: in metals most heat is carried by the free electrons ($k_e$), and alloying atoms act as defects that scatter them, so $k$ decreases.

- b) Extra free electrons would not scatter phonons into a lower $k$; the effect of alloying is on the electron transport itself.
- c) The Lorentz number is a constant (Slide 41); what falls with alloying is $k$ through the electrical conductivity $\sigma$.
- d) Pores are the cause in ceramics (Slide 43), not in a dense solid solution.

### Source

Session 15, Slides 40, 41 and 43.

## Q62.5 Porous alumina

- id: B62-Q5
- concept_id: u7-k-porosity-ceramic
- format: what-happens
- asks: effect

A dense alumina part is replaced by a porous part made of the same alumina. The thermal conductivity of the part will:

a) increase, as the gas in the pores adds heat carriers
b) decrease, as the pores interrupt the path of the heat
c) decrease, as the pores raise the heat capacity
d) stay equal, as the composition has not changed

### Answer

b

### Explanation

Session 15, Slide 43: alloying, defects and porosity reduce the thermal conductivity. In a ceramic, heat travels by phonons and the pores break their path.

- a) The trend is inverted: gas in pores conducts far worse than the solid, so pores lower $k$.
- c) The cause is mixed up: Slide 35 says that the heat capacity is not significantly changed by the structure.
- d) The microstructure matters as well as the composition: $k$ is described as a microstructure-sensitive property (Slide 40).

### Source

Session 15, Slides 35, 40 and 43.

## Q62.6 Voltage of a thermocouple

- id: B62-Q6
- concept_id: u7-thermocouple-principle
- format: complete-sentence
- asks: cause

A thermocouple produces a voltage when:

a) a single homogeneous conductor carries an electric current while heated uniformly
b) two identical metal conductors touch each other at a single heated spot
c) a single metal conductor moves steadily through a magnetic field at room temperature
d) two dissimilar conductors touch and one contact differs from the reference temperature

### Answer

d

### Explanation

Session 15, Slide 44: a thermocouple has two dissimilar conductors that contact each other at one or more spots, and it produces a voltage when the temperature of one of the spots differs from the reference temperature at the other parts of the circuit (the slide shows Ni-Cr and Al-Cr).

- a) A single conductor heated uniformly has no contact between different metals, so there is no temperature difference to generate a voltage.
- b) The two conductors must be dissimilar; identical conductors give no voltage even at a hot contact.
- c) A magnetic field is not involved in the thermocouple of the slide; the effect depends on temperature differences between contacts.

### Source

Session 15, Slide 44.

## Q62.7 Thermal stress sign in constrained heating and cooling

- id: B62-Q7
- concept_id: u7-thermal-stress-constrained-sign
- format: topic-true
- asks: effect

Referring to thermal stresses in a bar constrained between rigid walls ($\sigma = E\alpha(T_0 - T_f)$), which one of the following statements is TRUE:

a) Heating ($T_f > T_0$) produces tensile stress because the bar tries to expand, whereas cooling produces compressive stress
b) Uniform heating or cooling produces zero stress in a constrained bar because a temperature gradient is required
c) Cooling ($T_f < T_0$) produces tensile stress because contraction is prevented, whereas heating produces compressive stress
d) Doubling Young's modulus $E$ halves the thermal stress because a stiffer material resists thermal strain

### Answer

c

### Explanation

Session 15, Slide 45: in a constrained bar held at fixed length, cooling ($T_f < T_0$) prevents natural contraction so the walls pull on the bar, creating tensile stress ($\sigma > 0$), while heating ($T_f > T_0$) prevents expansion and creates compressive stress ($\sigma < 0$).

- a) Inverts the signs of heating and cooling: prevented expansion causes compression, and prevented contraction causes tension.
- b) Confuses constrained thermal stress (which arises at uniform temperature when external walls block $\alpha\Delta T$) with thermal-shock gradient stress (Slide 47).
- d) Inverts the proportionality to $E$: $\sigma = E\alpha(T_0 - T_f)$ scales linearly with $E$, so doubling $E$ doubles the stress.

### Source

Session 15, Slides 45 and 47.

## Q62.8 Length independence of constrained thermal stress

- id: B62-Q8
- concept_id: u7-thermal-stress-length-independence
- format: cause-effect
- asks: comparison

Two bars of the same alloy and cross-sectional area—one 0.5 m long and the other 2.0 m long—are clamped between rigid walls and cooled by the same $\Delta T$. Compared with the shorter bar, the thermal stress magnitude in the longer bar is:

a) four times larger, because the blocked free contraction $\Delta l = \alpha\,l_0\,\Delta T$ is four times larger
b) the same, because prevented thermal strain $\alpha\,\Delta T$ and $\sigma = E\alpha\,\Delta T$ do not depend on initial length
c) one quarter as large, because the same thermal strain is distributed over four times the length
d) zero, because constrained bars develop thermal stress during heating rather than during cooling

### Answer

b

### Explanation

Session 15, Slide 45: although free contraction $\Delta l = \alpha\,l_0\,\Delta T$ scales with $l_0$, thermal strain is $\varepsilon_{th} = \Delta l/l_0 = \alpha\,\Delta T$, so clamping the bar induces $\sigma = E\alpha(T_0 - T_f)$, which is independent of the initial length $l_0$.

- a) Confuses total free elongation $\Delta l$ (which depends on $l_0$) with thermal strain $\alpha\Delta T$ (which does not).
- c) Wrongly treats $\Delta l$ as fixed rather than proportional to $l_0$, leading to an inverse-$l_0$ scaling.
- d) False restriction: cooling a clamped bar produces tensile thermal stress just as heating produces compressive stress.

### Source

Session 15, Slide 45.

## Q62.9 Cold ceramic block put in a hot furnace

- id: B62-Q9
- concept_id: u7-thermal-shock-heating-surface
- format: what-happens
- asks: effect

A cold ceramic block is suddenly placed in a hot furnace. In the first moments, the stress at its surface and the stress in its interior are, respectively:

a) compressive and tensile
b) tensile and compressive
c) compressive and compressive
d) tensile and tensile

### Answer

a

### Explanation

Session 15, Slide 47: in rapid heating the exterior is hotter and tries to expand more than the interior, so the surface stress is compressive and the interior stress tensile.

- b) This is the pattern of rapid cooling, where the surface contracts first and is in tension.
- c) A temperature gradient cannot give a compressive state everywhere: the surface stress must be balanced by an opposite stress in the interior.
- d) A tensile state everywhere would also leave the forces unbalanced; the interior opposes the surface.

### Source

Session 15, Slide 47.

## Q62.10 Thermal shock resistance of four ceramics

- id: B62-Q10
- concept_id: u7-tsr-ceramic-ordering
- format: ordering
- asks: comparison

Assume equal fracture stress and modulus of elasticity. Using the values below, order these four ceramics by increasing thermal shock resistance:

| Ceramic | $\alpha$ ($10^{-6}$ °C⁻¹) | $k$ (W/(m·K)) |
| :--- | :--- | :--- |
| Alumina | 7.6 | 39 |
| Magnesia | 13.5 | 37.7 |
| Spinel | 7.6 | 15.0 |
| Fused silica | 0.4 | 1.4 |

a) fused silica, spinel, magnesia, alumina
b) alumina, fused silica, magnesia, spinel
c) spinel, magnesia, fused silica, alumina
d) fused silica, alumina, spinel, magnesia

### Answer

c

### Explanation

Session 15, Slide 48: $TSR = \sigma_f k/(E\,\alpha_l)$, so with equal $\sigma_f$ and $E$ it is proportional to $k/\alpha$: spinel 15.0/7.6 = 1.97, magnesia 37.7/13.5 = 2.79, fused silica 1.4/0.4 = 3.5, alumina 39/7.6 = 5.13 (relative values, in W/(m·K) per $10^{-6}$ °C⁻¹).

- a) The ceramics were ordered by $k$ alone: the expansion coefficient also enters, and it lowers $TSR$.
- b) This is the decreasing order of the true ranking.
- d) The ceramics were ordered by increasing $\alpha$, as if a larger $\alpha$ raised the resistance; the slide says that a larger $\alpha$ lowers it.

### Source

Session 15, Slides 38 and 48.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
