---
materia: Aerospace Materials I
tema: "Unit 7: thermal conductivity, Wiedemann-Franz law, thermocouples, thermal stresses and thermal shock resistance"
bank_id: B62
title: "Thermal conduction, thermocouples, thermal stresses and thermal shock"
category: mt2_test_block
unit: 7
concepts:
  - u7-k-ordering-alloys-table
  - u7-fourier-heat-flow-stainless
  - u7-wf-celsius-slip
  - u7-k-alloy-electron-scattering
  - u7-k-porosity-ceramic
  - u7-thermocouple-principle
  - u7-thermal-stress-cooling-steel
  - u7-wire-constant-length-diameter
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

## Q62.1 Ranking of alloys by thermal conductivity

- id: B62-Q1
- concept_id: u7-k-ordering-alloys-table
- format: ordering
- asks: comparison

From the table of Slide 41, with the values shown, order the following alloys by increasing thermal conductivity:

| Material | $k$ (W/(m·K)) |
| :--- | :--- |
| 1020 steel | 100 |
| 3003 aluminum alloy | 280 |
| 304 stainless steel | 30 |
| Cementite | 50 |

a) cementite, 304 stainless steel, 1020 steel, 3003 aluminum alloy
b) 3003 aluminum alloy, 1020 steel, cementite, 304 stainless steel
c) 304 stainless steel, cementite, 1020 steel, 3003 aluminum alloy
d) 304 stainless steel, 1020 steel, cementite, 3003 aluminum alloy

### Answer

c

### Explanation

Session 15, Slide 41: $k$ = 30 (304 stainless steel) < 50 (cementite) < 100 (1020 steel) < 280 W/(m·K) (3003 aluminum alloy).

- a) The two lowest values are swapped: 304 stainless steel (30) is below cementite (50).
- b) The order is read from the highest value: it is the decreasing order.
- d) Cementite (50) and 1020 steel (100) are swapped.

### Source

Session 15, Slide 41.

## Q62.2 Heat flow through a stainless steel wall

- id: B62-Q2
- concept_id: u7-fourier-heat-flow-stainless
- format: numeric
- asks: application
- calc: 15.9*0.20*(100-20)/0.005

A 316 stainless steel wall ($k = 15.9$ W/(m·K), Slide 38) is 5.0 mm thick and has an area of 0.20 m². Its faces are at 100 °C and 20 °C. Determine the heat flow through it in steady state:

a) $5.09\times10^{4}$ W
b) $2.54\times10^{5}$ W
c) 50.9 W
d) 1.27 W

### Answer

a

### Explanation

Session 15, Slide 40: with $q = Q/A = k\,\Delta T/\Delta x$, the heat flow is $Q = k\,A\,\Delta T/\Delta x = 15.9\times0.20\times80/0.005 = 5.09\times10^{4}$ W.

- b) The area was left out, which gives the heat flux $q$ in W/m² (2.54×10⁵) instead of the heat flow $Q$.
- c) The thickness was entered in mm (5.0) instead of in m: the result is 1000 times too small.
- d) The thickness multiplied instead of dividing: $15.9\times0.20\times80\times0.005$.

### Source

Session 15, Slides 38 and 40.

## Q62.3 Electrical conductivity from a measured thermal conductivity

- id: B62-Q3
- concept_id: u7-wf-celsius-slip
- format: numeric
- asks: calculation
- calc: 150/(2.44e-8*(127+273.15))

A metal whose heat is carried by its free electrons has $k = 150$ W/(m·K) at 127 °C. Using the Lorentz number $L = 2.44\times10^{-8}$ W·Ω/K², determine its electrical conductivity at that temperature:

a) $4.84\times10^{7}$ (Ω·m)⁻¹
b) $6.82\times10^{7}$ (Ω·m)⁻¹
c) $2.15\times10^{8}$ (Ω·m)⁻¹
d) $1.54\times10^{7}$ (Ω·m)⁻¹

### Answer

d

### Explanation

Session 15, Slide 41: $L = k/(\sigma T)$, so $\sigma = k/(L\,T)$ with $T$ in kelvin: $T = 127 + 273.15 = 400.15$ K and $\sigma = 150/(2.44\times10^{-8}\times400.15) = 1.54\times10^{7}$ (Ω·m)⁻¹.

- a) The temperature was entered as 127 K, the value in °C.
- b) The Lorentz number of the slide in cal·Ω/(s·K²) ($5.5\times10^{-9}$) was used with $k$ in W/(m·K).
- c) Both slips together: the cal-based Lorentz number and 127 in place of 400 K.

### Source

Session 15, Slide 41.

## Q62.4 Nickel in copper

- id: B62-Q4
- concept_id: u7-k-alloy-electron-scattering
- format: cause-effect
- asks: cause

In the table of Slide 41, copper has $k = 400$ W/(m·K) while the alloy Cu-30% Ni has 50 W/(m·K). The main reason for this drop is that the nickel atoms:

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

a) a single conductor carries a current while it is heated uniformly
b) two identical conductors touch each other at a hot spot
c) a conductor is moved through a magnetic field at room temperature
d) two dissimilar conductors touch and one contact is not at the reference temperature

### Answer

d

### Explanation

Session 15, Slide 44: a thermocouple has two dissimilar conductors that contact each other at one or more spots, and it produces a voltage when the temperature of one of the spots differs from the reference temperature at the other parts of the circuit (the slide shows Ni-Cr and Al-Cr).

- a) A single conductor heated uniformly has no contact between different metals, so there is no temperature difference to generate a voltage.
- b) The two conductors must be dissimilar; identical conductors give no voltage even at a hot contact.
- c) A magnetic field is not involved in the thermocouple of the slide; the effect depends on temperature differences between contacts.

### Source

Session 15, Slide 44.

## Q62.7 Steel bar cooled between rigid walls

- id: B62-Q7
- concept_id: u7-thermal-stress-cooling-steel
- format: numeric
- asks: calculation
- calc: 207e3*12.5e-6*45

A steel bar ($E = 207$ GPa, $\alpha = 12.5\times10^{-6}$ °C⁻¹, Slide 46) is held between rigid walls so that it cannot contract, and it is cooled by 45 °C. Determine the magnitude of the thermal stress that develops:

a) 2.59 MPa
b) 116 MPa
c) $1.16\times10^{5}$ MPa
d) 0.116 MPa

### Answer

b

### Explanation

Session 15, Slide 45: $\sigma = E\,\alpha\,\Delta T = 207\times10^{3}\ \text{MPa}\times12.5\times10^{-6}\ ^\circ\text{C}^{-1}\times45\ ^\circ\text{C} = 116$ MPa. On cooling ($T_f < T_0$) the bar would contract, the walls prevent it and the stress is tensile ($\sigma > 0$); on heating it would be compressive.

- a) The temperature change was left out: $E\,\alpha = 2.59$ MPa per °C.
- c) The modulus was converted from GPa to MPa with a factor $10^{6}$ instead of $10^{3}$.
- d) The modulus was entered as 207 MPa instead of 207 GPa: the result is 1000 times too small.

### Source

Session 15, Slides 45 and 46.

## Q62.8 Wire diameter for a compensating thermal stress

- id: B62-Q8
- concept_id: u7-wire-constant-length-diameter
- format: numeric
- asks: application
- calc: (4*2000/(207e3*12.5e-6*30)/pi)**0.5

A steel wire ($E = 207$ GPa, $\alpha = 12.5\times10^{-6}$ °C⁻¹) is stretched by a force of 2000 N at 15 °C, then held at constant length and heated to 45 °C. Determine the diameter of the wire so that the thermal stress equals the applied stress:

a) 2.86 mm
b) 4.68 mm
c) 5.73 mm
d) 8.20 mm

### Answer

c

### Explanation

Session 15, Slides 45 and 46: $\sigma_{th} = E\,\alpha\,\Delta T = 207\times10^{3}\times12.5\times10^{-6}\times30 = 77.6$ MPa. Then $A_0 = F/\sigma = 2000/77.6 = 25.8$ mm² and $d = \sqrt{4A_0/\pi} = 5.73$ mm.

- a) The radius ($\sqrt{A_0/\pi} = 2.86$ mm) was given instead of the diameter.
- b) The final temperature (45 °C) was used instead of the change $\Delta T = 30$ °C, which gives a higher $\sigma$ and a thinner wire.
- d) The area was taken as $\pi d$ instead of $\pi d^2/4$: $d = A_0/\pi$.

### Source

Session 15, Slides 45 and 46.

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

Assume equal fracture stress and modulus of elasticity. With the data of Slide 38 shown, order the ceramics by increasing thermal shock resistance:

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
