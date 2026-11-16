---
materia: Aerospace Materials I
tema: "Unit 7: thermal conductivity and temperature, heat flow, thermal stresses in constrained bodies and thermal shock"
bank_id: B52
title: "Thermal stresses and thermal shock"
category: mt2_test_block
unit: 7
concepts:
  - u7-conductivity-defects-temperature
  - u7-fourier-law-calc
  - u7-thermal-stress-constrained
  - u7-thermal-shock-gradients
  - u7-thermal-shock-resistance
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf and of the thermal shock items of the 2016 and 2017 finals; not official exercises. Content and data from Session 15, Slides 38, 40, 42 and 45-48, and Session 11, Slide 17 (moduli)."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-7
---

# Bank B52 — Thermal stresses and thermal shock

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 15, Slides 38, 40, 42 and 45-48.

## Q52.1 Temperature and the conductivity of metals

- id: B52-Q1
- concept_id: u7-conductivity-defects-temperature
- format: true-statement
- asks: effect

Which one of the following statements is TRUE about the effect of temperature on the thermal conductivity of metals?

a) Higher T raises both the electron mobility and $k_{ph}$
b) Higher T lowers both $k_{ph}$ and the electron mobility
c) Higher T lowers $k_{ph}$ and raises the electron mobility
d) Higher T raises $k_{ph}$ but lowers the electron mobility

### Answer

d

### Explanation

Slide 42 gives two competing effects for metals: a higher temperature increases the contribution of the lattice vibrations $k_{ph}$, and it decreases the electron mobility (more scattering of the electrons).

- a) Right for $k_{ph}$, wrong for the electrons: more thermal vibration scatters them more, so their mobility falls.
- b) Right for the electron mobility, wrong for $k_{ph}$: the slide says that heating increases the lattice contribution, so the two effects compete.
- c) Both effects inverted: the slide says that heating raises $k_{ph}$ and lowers the mobility of the electrons, not the reverse.

### Source

Session 15, Slide 42.

## Q52.2 Heat lost through a window pane

- id: B52-Q2
- concept_id: u7-fourier-law-calc
- format: numeric
- asks: application
- calc: 1.7*1.5*(10-6)/0.004/1000

A soda-lime glass pane ($k = 1.7$ W/(m·K), Slide 38) of 1.5 m² and 4.0 mm thickness has its faces at 10 °C and 6 °C. Determine the heat flow through it:

a) 0.00255 kW
b) 1.70 kW
c) 2.55 kW
d) 6.38 kW

### Answer

c

### Explanation

Fourier's law (Slide 40), $Q = q\,A = k\,A\,\Delta T/\Delta x = 1.7\times1.5\times(10 - 6)/0.0040 = 2550$ W $= 2.55$ kW.

- a) The thickness is entered as 4.0 m instead of 0.0040 m: $1.7\times1.5\times4/4.0 = 2.55$ W $= 0.00255$ kW.
- b) The area is left out: $1.7\times4/0.0040 = 1700$ W is the flux per square metre, $q$, not the heat flow $Q$.
- d) The temperature of the warm face is used instead of the difference: $1.7\times1.5\times10/0.0040 = 6380$ W.

### Source

Session 15, Slides 38 and 40.

## Q52.3 Copper bar between rigid walls

- id: B52-Q3
- concept_id: u7-thermal-stress-constrained
- format: numeric
- asks: calculation
- calc: 110e3*17.0e-6*(70-20)

A copper bar ($E = 110$ GPa, Session 11; $\alpha = 17.0\times10^{-6}$ °C⁻¹, Slide 38) fits between rigid walls at 20 °C and is heated to 70 °C. Determine the magnitude of its thermal stress:

a) 0.0935 MPa
b) 93.5 MPa
c) 131 MPa
d) 641 MPa

### Answer

b

### Explanation

Slide 45: $\sigma = E\alpha(T_0 - T_f)$; in magnitude $110\,000\ \text{MPa}\times17.0\times10^{-6}\times50 = 93.5$ MPa, compressive because the bar is heated.

- a) $E$ is left in GPa while the answer is given in MPa: $110\times17.0\times10^{-6}\times50 = 0.0935$.
- c) The final temperature is used instead of the change: $110\,000\times17.0\times10^{-6}\times70 = 131$ MPa.
- d) The final temperature in kelvin is used as $\Delta T$: $110\,000\times17.0\times10^{-6}\times343 = 641$ MPa.

### Source

Session 15, Slides 38 and 45; Session 11, Slide 17.

## Q52.4 Constrained bar on cooling

- id: B52-Q4
- concept_id: u7-thermal-stress-constrained
- format: complete-sentence
- asks: effect

A bar held between rigid walls and then cooled develops a thermal stress that is:

a) tensile, since the walls prevent its contraction
b) compressive, since the walls prevent its contraction
c) zero, since a uniform change creates no gradient
d) tensile at the surface and compressive inside

### Answer

a

### Explanation

Slide 45: with $T_f < T_0$, $\sigma = E\alpha(T_0 - T_f) > 0$: the walls stop the bar from contracting, so they pull on it and the stress is tensile.

- b) Sign of the heating case: a prevented expansion gives compression, a prevented contraction gives tension.
- c) Mixes up the two sources of thermal stress: gradients (Slide 47) are not needed here, since the walls block the free contraction $\alpha\Delta T$ and the stress $E\alpha\Delta T$ appears at uniform temperature.
- d) Tensile surface and compressive interior is the stress profile of rapid cooling of a free body with a temperature gradient (Slide 47), not of a uniformly cooled constrained bar.

### Source

Session 15, Slides 45 and 47.

## Q52.5 Aluminium rod heated between walls

- id: B52-Q5
- concept_id: u7-thermal-stress-constrained
- format: what-happens
- asks: application
- check: 69e3*23.6e-6*(100-20) > 100

An aluminium rod ($E = 69$ GPa, $\alpha = 23.6\times10^{-6}$ °C⁻¹, yield strength 100 MPa) fits between rigid walls at 20 °C and is heated to 100 °C. What will happen?

a) It stays free of stress, as the walls hold it
b) It deforms plastically in tension
c) It stays elastic, with a small compressive stress
d) It deforms plastically in compression

### Answer

d

### Explanation

$|\sigma| = E\alpha\,\Delta T = 69\,000\times23.6\times10^{-6}\times80 = 130$ MPa (Slide 45), above the 100 MPa yield strength; heating a constrained bar gives a compressive stress, so the rod yields in compression.

- a) The walls are what create the stress: they prevent the free expansion, and the prevented strain becomes stress.
- b) Wrong sign: on heating ($T_f > T_0$) the slide gives $\sigma < 0$, compressive.
- c) $E$ is left in GPa: $69\times23.6\times10^{-6}\times80 = 0.130$ looks far below the yield strength, but the real stress is 130 MPa.

### Source

Session 15, Slides 38 and 45; Session 11, Slide 17.

## Q52.6 Quenching a hot glass plate

- id: B52-Q6
- concept_id: u7-thermal-shock-gradients
- format: what-happens
- asks: effect

A hot glass plate is suddenly quenched in cold water. What will happen to the stresses inside it?

a) Compressive at the surface, tensile in the interior
b) Tensile at the surface, compressive in the interior
c) Tensile stresses at both surface and interior
d) Compressive stresses at both surface and interior

### Answer

b

### Explanation

Slide 47: on rapid cooling the outside cools and contracts before the interior, which holds it back; the surface is under tension and the interior under compression.

- a) This is the stress state of rapid heating, with the signs inverted.
- c) Takes the sign of a constrained bar that is cooled (Slide 45); in a free plate the surface and the interior must balance each other, so they do not share the same sign.
- d) Takes the sign of a constrained bar that is heated; for the same balance reason a free plate cannot be compressed everywhere.

### Source

Session 15, Slide 47.

## Q52.7 Origin of thermal stresses in a free body

- id: B52-Q7
- concept_id: u7-thermal-shock-gradients
- format: complete-sentence
- asks: cause

Thermal stresses appear in an unconstrained body during rapid heating because:

a) the walls around it prevent its expansion
b) the whole body expands by the same amount
c) the inside heats up faster than the outside
d) the outside heats up faster than the inside

### Answer

d

### Explanation

Slide 47: thermal stresses are established by temperature gradients across a body caused by rapid heating or cooling, because the outside temperature changes more rapidly than the interior.

- a) Walls are the constrained case of Slide 45; the body in the question is unconstrained.
- b) A uniform expansion produces no stress at all; stresses need the parts of the body to expand by different amounts.
- c) Inverted gradient: the heat enters through the surface, so the outside heats first.

### Source

Session 15, Slides 45 and 47.

## Q52.8 Thermal shock resistance of alumina

- id: B52-Q8
- concept_id: u7-thermal-shock-resistance
- format: numeric
- asks: calculation
- calc: 300e6*39/(393e9*7.6e-6)

Alumina has a fracture stress of 300 MPa, $k = 39$ W/(m·K), $\alpha = 7.6\times10^{-6}$ °C⁻¹ (Slide 38) and $E = 393$ GPa (Session 11). Determine its thermal shock resistance $TSR = \sigma_f k/(E\alpha_l)$:

a) $2.55\times10^{-4}$ W/m
b) $3.92\times10^{2}$ W/m
c) $3.92\times10^{3}$ W/m
d) $3.92\times10^{6}$ W/m

### Answer

c

### Explanation

Slide 48: $TSR = \sigma_f k/(E\alpha_l) = (300\times10^6\times39)/(393\times10^9\times7.6\times10^{-6}) = 3.92\times10^3$ W/m, with $\sigma_f$ and $E$ in the same unit (Pa).

- a) The formula is inverted: $E\alpha_l/(\sigma_f k) = 2.55\times10^{-4}$.
- b) The coefficient is taken as $7.6\times10^{-5}$ °C⁻¹ (exponent slip), giving a value ten times too small.
- d) $\sigma_f$ in MPa and $E$ in GPa are mixed without conversion: $300\times39/(393\times7.6\times10^{-6}) = 3.92\times10^6$.

### Source

Session 15, Slides 38 and 48; Session 11, Slide 17.

## Q52.9 Thermal conductivity and thermal shock

- id: B52-Q9
- concept_id: u7-thermal-shock-resistance
- format: cause-effect
- asks: cause

With an increase in the thermal conductivity of a ceramic, its thermal shock resistance:

a) increases, because the temperature evens out faster
b) decreases, because more heat reaches the interior
c) increases, because the material expands less
d) does not change, as k does not enter the TSR

### Answer

a

### Explanation

Slide 48: a higher thermal conductivity gives a higher thermal shock resistance ($k$ is in the numerator of $TSR = \sigma_f k/(E\alpha_l)$); heat spreads faster, so the gradient between surface and interior, which causes the stresses (Slide 47), stays small.

- b) Inverted trend: heat reaching the interior quickly is what reduces the gradient and the stresses.
- c) Right trend, wrong cause: the expansion is set by $\alpha_l$, a separate factor that $k$ does not change.
- d) $k$ is one of the four factors of the slide and appears in the numerator of the TSR.

### Source

Session 15, Slides 47-48.

## Q52.10 Fused silica against soda-lime glass

- id: B52-Q10
- concept_id: u7-thermal-shock-resistance
- format: true-statement
- asks: comparison
- check: 17 < (1.4*69*9.0)/(1.7*73*0.4) < 18

Fused silica ($E = 73$ GPa, $\alpha = 0.4\times10^{-6}$ °C⁻¹, $k = 1.4$ W/(m·K)) and soda-lime glass ($E = 69$ GPa, $\alpha = 9.0\times10^{-6}$ °C⁻¹, $k = 1.7$ W/(m·K)) have the same fracture stress. Which statement is TRUE?

a) Soda-lime glass resists thermal shock better, as its k is higher
b) Fused silica resists thermal shock about 17 times better
c) Both resist thermal shock alike, as their E and k are similar
d) Fused silica resists thermal shock about 22 times better

### Answer

b

### Explanation

With equal $\sigma_f$, the ratio of $TSR = \sigma_f k/(E\alpha_l)$ (Slide 48) is $\dfrac{1.4/(73\times0.4)}{1.7/(69\times9.0)} = \dfrac{1.4\times69\times9.0}{1.7\times73\times0.4} = 17.5$: the very low expansion of fused silica dominates.

- a) Looks at $k$ alone; the 22-fold difference in $\alpha$ outweighs the slightly higher conductivity of soda-lime glass.
- c) Ignores $\alpha$, the factor in which the two glasses differ most.
- d) Uses only the ratio of the coefficients, $9.0/0.4 = 22.5$, leaving out the differences in $k$ and $E$.

### Source

Session 15, Slides 38 and 48; Session 11, Slide 17.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
