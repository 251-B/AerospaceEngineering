---
materia: Aerospace Materials I
tema: "Unit 7: thermal expansion of constrained gaps, bonding and expansion, Fourier's law, heat carriers and the Lorenz relation"
bank_id: B51
title: "Thermal conductivity and expansion"
category: mt2_test_block
unit: 7
concepts:
  - u7-expansion-bonding-strength
  - u7-expansion-bonding-well
  - u7-conductivity-mechanisms
  - u7-fourier-law-calc
  - u7-conductivity-defects-temperature
  - u7-wiedemann-franz
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf, including an adaptation of Q1a from the June 2016 final exam. Content and data from Session 15, Slides 36, 38 and 40-43."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-7
---

# Bank B51 — Thermal conductivity and expansion

> [!info] Includes official exam questions
> Ten test questions written for the bank in the style of Part I of Assessment Test II, including an adaptation from the June 2016 final exam (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 15, Slides 36, 38 and 40-43.

## Q51.1 Atomic bonding strength and thermal expansion

- id: B51-Q1
- concept_id: u7-expansion-bonding-strength
- format: cause-effect
- asks: cause
- origin: official-exam

With an increase in atomic bonding strength across different solid materials, the linear coefficient of thermal expansion ($\alpha$) generally:

a) decreases, because stronger bonds produce a deeper potential energy well with smaller spacing shifts
b) increases, because stronger bonds store more energy and widen the interatomic spacing faster
c) stays unchanged, because thermal expansion is governed by density rather than bond strength
d) increases, because stiffer covalent and ionic bonds expand more rapidly upon heating

### Answer

a

### Explanation

Session 15, Slides 36-37 (and June 2016 final, Q1a): stronger atomic bonding corresponds to a deeper, narrower potential energy well; raising temperature produces a smaller increase in mean interatomic spacing, so $\alpha$ is lower (as shown by metals with higher melting temperatures having lower $\alpha$).

- b) Inverts the relationship between bond energy and thermal expansion: deeper wells shift less in mean spacing for a given rise in thermal energy.
- c) Ignores the atomic origin of expansion: $\alpha$ depends directly on the depth and asymmetry of the interatomic bonding curve, not on mass density.
- d) Inverts both trend and class behaviour: strong covalent/ionic ceramics typically have lower $\alpha$ than weakly bonded polymers.

### Source

MATERIALS_FINALEXAM_2016_EXTRA_SOL.pdf, p. 1 Q1a; Session 15, Slides 36-37.

## Q51.2 Strong bonding and expansion

- id: B51-Q2
- concept_id: u7-expansion-bonding-well
- format: true-statement
- asks: comparison

Which one of the following statements is TRUE about materials with strong atomic bonding?

a) They have a low α and usually a high melting temperature
b) They have a high α, as their atoms vibrate more strongly
c) Their α depends on their density, not on the bonding
d) Their atomic spacing does not change on heating

### Answer

a

### Explanation

Slide 36: materials with a high bonding energy have low coefficients of thermal expansion, and Slide 37 shows that the metals with the higher melting temperature (stronger bonding) have the lower coefficients.

- b) Inverted trend: strong bonding gives a low coefficient (the final of June 2017 marks the opposite statement as false).
- c) The slides relate $\alpha$ to the bonding energy and to the melting temperature, not to the density.
- d) An absolute statement: the spacing of every solid grows on heating; strong bonding only makes the growth smaller.

### Source

Session 15, Slides 36-37.

## Q51.3 Heat carriers in metals

- id: B51-Q3
- concept_id: u7-conductivity-mechanisms
- format: complete-sentence
- asks: classification

In metals, heat is carried mainly by:

a) lattice vibrations, or phonons
b) free electrons
c) photons emitted by the hot lattice
d) ions diffusing through the lattice

### Answer

b

### Explanation

Slide 40: the thermal energy is transferred by free electrons ($k_e$) and by phonons ($k_{ph}$); in conductive materials the transfer is by free electrons, $k \approx k_e$.

- a) Phonons are the main carrier in insulating materials, $k \approx k_{ph}$, not in metals.
- c) The slides name only electrons and phonons as the two mechanisms of thermal conduction.
- d) Diffusing ions transport mass (Unit 3), not the thermal energy of conduction.

### Source

Session 15, Slide 40.

## Q51.4 Heat flux through an iron plate

- id: B51-Q4
- concept_id: u7-fourier-law-calc
- format: numeric
- asks: calculation
- calc: 80*(120-80)/0.010

An iron plate 10 mm thick ($k = 80$ W/(m·K)) has one face at 120 °C and the other at 80 °C. Determine the heat flux through it in steady state:

a) $3.20\times10^{1}$ W/m²
b) $3.20\times10^{2}$ W/m²
c) $3.20\times10^{5}$ W/m²
d) $9.60\times10^{5}$ W/m²

### Answer

c

### Explanation

Fourier's law (Slide 40), in magnitude: $q = k\,\Delta T/\Delta x = 80\times(120 - 80)/0.010 = 3.20\times10^5$ W/m², flowing from the hot face to the cold one.

- a) The thickness is multiplied instead of divided: $80\times40\times0.010 = 32.0$ W/m².
- b) The thickness is left in millimetres: $80\times40/10 = 320$ W/m².
- d) The temperature of the hot face is used instead of the difference: $80\times120/0.010 = 9.60\times10^5$ W/m².

### Source

Session 15, Slides 38 and 40.

## Q51.5 Ceramics and polymers as insulators

- id: B51-Q5
- concept_id: u7-conductivity-mechanisms
- format: complete-sentence
- asks: cause

Ceramics and polymers are poor thermal conductors because:

a) many free electrons scatter their phonons in the lattice
b) their heat capacity is higher than that of metals, so heat is stored
c) they have few free electrons, so heat travels by phonons
d) their atoms vibrate too weakly to pass heat along

### Answer

c

### Explanation

Slide 40: in insulating materials the transfer of thermal energy is by phonons, $k \approx k_{ph}$, because there are hardly any free electrons; phonon conduction is much less effective, which is why $k$ of polymers is about 0.1-0.5 W/(m·K) against hundreds for metals (Slide 41).

- a) Insulators do not have many free electrons; that is the feature of metals.
- b) The specific heat is a different property (heat stored, not heat transferred); it does not explain a low conductivity.
- d) Phonon conduction is the mechanism of these materials, only less effective than electrons; phonons do carry heat, and some ceramics such as SiC and AlN reach up to 270 W/(m·K) through them (Slide 41).

### Source

Session 15, Slides 40-41.

## Q51.6 Zinc in copper and thermal conductivity

- id: B51-Q6
- concept_id: u7-conductivity-defects-temperature
- format: cause-effect
- asks: effect

With an increase in the zinc content of a Cu-Zn alloy, its thermal conductivity:

a) decreases, because solute atoms scatter electrons and phonons
b) increases, because zinc adds free electrons
c) decreases, because zinc lowers the heat capacity
d) increases, because the alloy becomes harder and stiffer

### Answer

a

### Explanation

Slide 43: alloying, defects and porosity reduce the thermal conductivity, and the Cu-Zn chart shows $k$ falling as zinc is added; the solute atoms are defects that scatter the heat carriers.

- b) Inverted trend: the chart of Slide 43 shows the conductivity of copper falling with zinc.
- c) Right trend, wrong cause: the heat capacity does not depend significantly on the structure (Slide 35), and the drop comes from scattering.
- d) Mixes up strength and conductivity: solute atoms harden the alloy, but the same defects reduce $k$ (Slide 43).

### Source

Session 15, Slides 35 and 43.

## Q51.7 Thermal conductivity of copper from the Lorenz number

- id: B51-Q7
- concept_id: u7-wiedemann-franz
- format: numeric
- asks: calculation
- calc: 2.44e-8*6.0e7*300

Copper has an electrical conductivity $\sigma = 6.0\times10^7$ (Ω·m)⁻¹ at 300 K (27 °C). Estimate its thermal conductivity with $L = 2.44\times10^{-8}$ W·Ω/K²:

a) 0.00488 W/(m·K)
b) 39.5 W/(m·K)
c) 99.0 W/(m·K)
d) 439 W/(m·K)

### Answer

d

### Explanation

Slide 41: $L = k/(\sigma T)$, so $k = L\sigma T = 2.44\times10^{-8}\times6.0\times10^7\times300 = 439$ W/(m·K), close to the 398-400 W/(m·K) of the tables.

- a) $T$ divided instead of multiplied: $2.44\times10^{-8}\times6.0\times10^7/300 = 0.00488$ W/(m·K).
- b) The temperature is entered in °C: $2.44\times10^{-8}\times6.0\times10^7\times27 = 39.5$ W/(m·K); the law needs the absolute temperature.
- c) The value of $L$ in calories, $5.5\times10^{-9}$, is used with SI data: $5.5\times10^{-9}\times6.0\times10^7\times300 = 99.0$.

### Source

Session 15, Slides 38 and 41.

## Q51.8 Fourier's law

- id: B51-Q8
- concept_id: u7-fourier-law-calc
- format: true-statement
- asks: definition

Which one of the following statements is TRUE about Fourier's law, $q = -k\,\Delta T/\Delta x$?

a) Heat flows up the temperature gradient, from cold to hot
b) The minus sign means that heat flows from hot to cold
c) The symbol $q$ is the total heat flow, in W
d) The conductivity $k$ is measured in W/(m²·K)

### Answer

b

### Explanation

Slide 40: the heat flux flows towards the cold end at a rate set by the temperature gradient; the minus sign makes $q$ positive in the direction in which the temperature falls.

- a) Inverted direction: heat flows down the gradient, from the hot to the cold side.
- c) $q = Q/A$ is the heat flux per unit area, in W/m²; $Q$, in W, is the heat flow.
- d) The unit of $k$ is W/(m·K): $q$ in W/m² divided by a gradient in K/m.

### Source

Session 15, Slide 40.

## Q51.9 Ranking of thermal conductivities

- id: B51-Q9
- concept_id: u7-conductivity-mechanisms
- format: ordering
- asks: comparison

Order polystyrene, soda-lime glass, iron and copper by increasing thermal conductivity:

a) copper, iron, soda-lime glass, polystyrene
b) soda-lime glass, polystyrene, iron, copper
c) soda-lime glass, iron, copper, polystyrene
d) polystyrene, soda-lime glass, iron, copper

### Answer

d

### Explanation

Slide 41: polystyrene 0.13, soda-lime glass 0.96-1.7, Fe 79 and Cu 400 W/(m·K); polymers and glasses conduct by phonons, metals by free electrons.

- a) The fully reversed order.
- b) Glass and polystyrene swapped: the polymer is the poorer conductor of the two.
- c) This is the order of the expansion coefficient (9.0, 11.8, 17.0 and $90$-$150\times10^{-6}$ °C⁻¹, Slide 38), not of $k$.

### Source

Session 15, Slides 38 and 41.

## Q51.10 Meaning of the Lorenz relation

- id: B51-Q10
- concept_id: u7-wiedemann-franz
- format: complete-sentence
- asks: application

The relation $L = k/(\sigma T)$, with $L$ constant, shows that among metals at the same temperature:

a) good electrical conductors are also good thermal conductors
b) good electrical conductors are poor thermal conductors
c) the thermal conductivity does not depend on $\sigma$
d) heat is carried mainly by phonons

### Answer

a

### Explanation

Slide 41: with $L$ constant, $k = L\sigma T$, so at a given temperature $k$ grows in proportion to $\sigma$; the same free electrons carry charge and heat in metals.

- b) Inverted proportion: $k$ and $\sigma$ rise together, they are not inversely related.
- c) The relation itself ties $k$ to $\sigma$; only their ratio over $T$ is constant.
- d) The link with $\sigma$ exists because metals conduct heat by free electrons, $k \approx k_e$ (Slide 40), not by phonons.

### Source

Session 15, Slides 40-41.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
