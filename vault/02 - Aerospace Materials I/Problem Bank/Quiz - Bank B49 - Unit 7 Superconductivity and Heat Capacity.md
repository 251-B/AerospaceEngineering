---
materia: Aerospace Materials I
tema: "Unit 7: Meissner effect and critical field of superconductors, heat capacity and specific heat"
bank_id: B49
title: "Superconductivity and heat capacity"
category: mt2_test_block
unit: 7
concepts:
  - u7-superconductor-tc-meissner
  - u7-superconductor-critical-field
  - u7-heat-capacity-definition
  - u7-heat-capacity-debye
  - u7-specific-heat-energy
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 15, Slides 26-27, 34-35 and 38."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-7
---

# Bank B49 — Superconductivity and heat capacity

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 15, Slides 26-27, 34-35 and 38.

## Q49.1 Magnet above a cooled superconductor

- id: B49-Q1
- concept_id: u7-superconductor-tc-meissner
- format: what-happens
- asks: application

A small permanent magnet rests on a ceramic superconductor, which is then cooled below its critical temperature with liquid nitrogen. What will happen to the magnet?

a) It levitates, because the superconductor expels the field
b) It sticks to it, because the superconductor becomes ferromagnetic
c) It tips over and slides off, because one pole is repelled
d) It is pulled down, because the field lines crowd into it

### Answer

a

### Explanation

Slide 27: below $T_c$ the superconductor expels the magnetic field (Meissner effect) and behaves as a perfect diamagnet; the repulsion lifts the magnet, which levitates above the superconductor cooled by liquid nitrogen.

- b) A superconductor in the Meissner state is diamagnetic, not ferromagnetic, so it repels the magnet instead of attracting it.
- c) Treats the superconductor as a second magnet with a fixed pole; a perfect diamagnet repels either pole of the magnet, so it floats instead of tipping over.
- d) Inverted picture: the field lines are pushed around the superconductor, not drawn into it.

### Source

Session 15, Slide 27.

## Q49.2 Critical field and temperature

- id: B49-Q2
- concept_id: u7-superconductor-critical-field
- format: cause-effect
- asks: effect

With an increase in temperature below $T_c$, the critical magnetic field $H_c$ of a superconductor:

a) increases, so higher fields are tolerated
b) stays constant up to $T_c$ and then drops to zero
c) increases, while the critical current density falls
d) decreases, so lower fields destroy superconductivity

### Answer

d

### Explanation

Slide 26: $H_c$ and $J_c$ decrease with increasing temperature; closer to $T_c$ a smaller field (or current density) is enough to return the material to the normal state, which is the shape of the superconducting envelope.

- a) Inverted trend: the critical field is largest at the lowest temperature.
- b) Reads the curve as a switch: $H_c$ is largest at the lowest temperature and falls steadily to zero at $T_c$ (Slide 26).
- c) Right about $J_c$, wrong about $H_c$: the slide says both decrease with temperature.

### Source

Session 15, Slide 26.

## Q49.3 Energy per mole and per degree

- id: B49-Q3
- concept_id: u7-heat-capacity-definition
- format: identify
- asks: definition

Which quantity is the energy required to raise the temperature of one mole of a material by one degree?

a) The heat capacity
b) The specific heat
c) The thermal conductivity
d) The linear coefficient of thermal expansion

### Answer

a

### Explanation

Slide 34 defines the heat capacity $C = dQ/dT$ as the energy required to raise the temperature of one mole of a material by one degree, in J/(mol·K).

- b) The specific heat refers to one gram of material, not one mole (Slide 34).
- c) The thermal conductivity measures the rate at which heat is transferred, in W/(m·K) (Slide 40).
- d) The expansion coefficient is the change of unit length per degree (Slide 36), not an energy.

### Source

Session 15, Slides 34, 36 and 40.

## Q49.4 Phonon

- id: B49-Q4
- concept_id: u7-heat-capacity-definition
- format: complete-sentence
- asks: definition

A phonon is:

a) a quantum of light emitted by a hot solid
b) a free electron carrying heat in a metal
c) a packet of elastic waves of lattice vibration
d) a defect that scatters conduction electrons

### Answer

c

### Explanation

Slide 34: the thermal energy of a solid is the vibrational energy of its atoms, which travels as lattice waves; a phonon is a packet of these elastic waves.

- a) A quantum of light is a photon; the slide's phonon is an elastic (sound) wave of the lattice.
- b) Free electrons are the other heat carrier, $k_e$ (Slide 40), not phonons, $k_{ph}$.
- d) Lattice vibrations do scatter electrons (Unit 6), but a phonon is the vibration itself, not a defect.

### Source

Session 15, Slides 34 and 40.

## Q49.5 Heat capacity plateau above the Debye temperature

- id: B49-Q5
- concept_id: u7-heat-capacity-debye
- format: topic-true
- asks: comparison

Regarding the Debye temperature $\theta_D$ and the molar heat capacity $C$ of crystalline solids, which one of the following statements is TRUE:

a) Above $\theta_D$, the molar heat capacity rises linearly with temperature without reaching a plateau
b) Below $\theta_D$, ceramics typically reach the $3R$ plateau at lower temperatures than metals
c) Above $\theta_D$, the molar heat capacity levels off near $3R$ and becomes nearly temperature-independent
d) Above $\theta_D$, grain size and dislocation density double the molar heat capacity of pure metals

### Answer

c

### Explanation

Session 15, Slide 35: as temperature rises, lattice waves gain average energy so $C$ increases until it reaches the Debye temperature $\theta_D$, above which $C$ levels off at approximately $3R \approx 6\ \text{cal/(mol}\cdot\text{K)}$ ($\approx 24.9$ J/(mol·K)) and becomes independent of temperature.

- a) Inverts the high-temperature plateau: above $\theta_D$, $C$ stops rising and levels off near $3R$.
- b) Swaps metals and ceramics: the Slide 35 chart shows metals reaching the $3R$ plateau at lower temperatures than ceramics.
- d) Contradicts structural insensitivity: Slide 35 states that dislocations, vacancies, and grain size do not significantly affect heat capacity.

### Source

Session 15, Slide 35.

## Q49.6 Heat capacity below the Debye temperature

- id: B49-Q6
- concept_id: u7-heat-capacity-debye
- format: cause-effect
- asks: cause

With an increase in temperature below the Debye temperature, the heat capacity of a solid:

a) decreases, because the atoms vibrate more freely and store less
b) stays at 3R, because every vibration mode is already excited
c) increases, because more free electrons are created to store heat
d) increases, because the lattice waves gain average energy

### Answer

d

### Explanation

Slide 35: the heat capacity increases with temperature because the lattice waves can increase their average energy; only above $\theta_D$ does it level off at about $3R$.

- a) Inverted trend: heating gives the lattice waves more energy to store, not less.
- b) $3R$ is reached only above the Debye temperature; below it the heat capacity is still rising.
- c) Right trend, wrong mechanism: thermally created carriers belong to semiconductors (Unit 6); the slide explains the rise with the lattice waves.

### Source

Session 15, Slide 35.

## Q49.7 What the heat capacity depends on

- id: B49-Q7
- concept_id: u7-heat-capacity-definition
- format: true-statement
- asks: comparison

Which one of the following statements is TRUE about the heat capacity of materials?

a) It depends strongly on grain size and dislocation density
b) Iron shows a high specific heat at its Curie temperature
c) Above the Debye temperature it keeps rising with temperature
d) Ceramics reach the 3R plateau at lower temperatures than metals

### Answer

b

### Explanation

Slide 35: the heat capacity of most materials does not depend significantly on the structure, except for ferromagnetic materials such as iron, which show a high specific heat at the Curie temperature (the ferromagnetic to paramagnetic change).

- a) The slide states the opposite: dislocations, vacancies and grain size do not change the heat capacity significantly.
- c) Above $\theta_D$ the heat capacity becomes independent of temperature, at about $3R$.
- d) Inverted comparison: on the chart of Slide 35 the metals reach the plateau at lower temperatures than the ceramics.

### Source

Session 15, Slide 35.

## Q49.8 Heat to warm a copper block

- id: B49-Q8
- concept_id: u7-specific-heat-energy
- format: numeric
- asks: calculation
- calc: 2.0*386*(120-20)/1000

Determine the heat needed to raise a 2.0 kg copper block ($c_p = 386$ J/(kg·K)) from 20 °C to 120 °C:

a) 38.6 kJ
b) 77.2 kJ
c) 92.6 kJ
d) 303 kJ

### Answer

b

### Explanation

The specific heat is the energy per unit mass and per degree (Slide 34), so $Q = m\,c_p\,\Delta T = 2.0\times386\times(120 - 20) = 77\,200$ J $= 77.2$ kJ.

- a) The mass is left out: $386\times100 = 38\,600$ J, the heat for 1 kg only.
- c) The final temperature is used instead of the change: $2.0\times386\times120 = 92\,600$ J.
- d) The final temperature in kelvin is used as $\Delta T$: $2.0\times386\times393 = 303\,000$ J; a difference of temperature is the same in °C and K.

### Source

Session 15, Slides 34 and 38.

## Q49.9 Ranking by heat needed

- id: B49-Q9
- concept_id: u7-specific-heat-energy
- format: ordering
- asks: comparison

Equal masses of tungsten ($c_p = 138$ J/(kg·K)), iron ($448$ J/(kg·K)), aluminium ($900$ J/(kg·K)) and high-density polyethylene ($1850$ J/(kg·K)) are heated by the same temperature increment. Order them by increasing heat needed:

a) polyethylene, aluminium, iron, tungsten
b) iron, tungsten, aluminium, polyethylene
c) tungsten, iron, aluminium, polyethylene
d) polyethylene, iron, tungsten, aluminium

### Answer

c

### Explanation

With equal mass and $\Delta T$, the heat is proportional to $c_p$: W 138, Fe 448, Al 900 and polyethylene 1850 J/(kg·K) (Slide 38).

- a) The fully reversed order.
- b) Tungsten and iron swapped, as if the denser metal needed more heat per kilogram.
- d) This is the order of the thermal conductivity $k$ (0.46-0.50, 80, 178, 247 W/(m·K)), the neighbouring column of the table.

### Source

Session 15, Slide 38.

## Q49.10 Same heat to aluminium and copper

- id: B49-Q10
- concept_id: u7-specific-heat-energy
- format: what-happens
- asks: application
- check: abs(9000/386 - 23.3) < 0.1 and 9000/900 == 10

Blocks of 1.0 kg of aluminium ($c_p = 900$ J/(kg·K)) and copper ($c_p = 386$ J/(kg·K)) each receive 9.0 kJ of heat. What will happen?

a) Copper warms by about 23 °C, aluminium by 10 °C
b) Aluminium warms by about 23 °C, copper by 10 °C
c) Both warm by the same amount, as they receive the same heat
d) Aluminium warms more, since it is the lighter metal

### Answer

a

### Explanation

$\Delta T = Q/(m\,c_p)$ (Slide 34): copper $9000/(1.0\times386) = 23.3$ °C and aluminium $9000/(1.0\times900) = 10.0$ °C. The metal with the lower specific heat warms more.

- b) The two results are swapped: the larger $c_p$ of aluminium gives the smaller rise.
- c) The same heat gives the same $\Delta T$ only if the specific heats were equal; they differ by a factor of 2.3.
- d) The masses are equal by statement, so the density does not enter; and aluminium is the one that warms less.

### Source

Session 15, Slides 34 and 38.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
