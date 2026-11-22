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
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf, including Q1.4 from the June 2017 final exam. Content and data from Session 15, Slides 36, 38, 40, 42 and 45-48."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-7
---

# Bank B52 — Thermal stresses and thermal shock

> [!info] Includes official exam questions
> Ten test questions written for the bank in the style of Part I of Assessment Test II, including a statement from the June 2017 final exam (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 15, Slides 36, 38, 40, 42 and 45-48.

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

## Q52.2 Thickness effect in steady-state heat conduction

- id: B52-Q2
- concept_id: u7-fourier-law-calc
- format: cause-effect
- asks: effect

In steady-state one-dimensional heat conduction through a flat plate at fixed face temperatures, doubling the plate thickness causes the heat flux $q$ to:

a) double, because a thicker plate transfers twice as much heat across the section
b) halve, because the temperature gradient $\Delta T/\Delta x$ is cut in half
c) stay constant, because thermal conductivity $k$ is an intensive property
d) drop to one quarter, because thermal resistance scales with thickness squared

### Answer

b

### Explanation

Session 15, Slide 40: by Fourier's law, $q = -k\,\Delta T/\Delta x$; with $k$ and $\Delta T$ unchanged, doubling $\Delta x$ halves the temperature gradient and therefore halves the steady-state heat flux $q$.

- a) Inverts the denominator dependence on $\Delta x$: heat flux is inversely proportional to thickness, not proportional.
- c) Ignores the spatial gradient: $k$ is an intensive material property, but $q$ also depends on $\Delta T/\Delta x$.
- d) Applies an inverse-square scaling instead of the linear inverse thickness in Fourier's law.

### Source

Session 15, Slide 40.

## Q52.3 Copper bar between rigid walls

- id: B52-Q3
- concept_id: u7-thermal-stress-constrained
- format: numeric
- asks: calculation
- calc: 110e3*17.0e-6*(70-20)

A copper bar ($E = 110$ GPa, $\alpha = 17.0\times10^{-6}$ °C⁻¹) fits between rigid walls at 20 °C and is heated to 70 °C. Determine the magnitude of its thermal stress:

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

## Q52.8 Thermal expansion, bonding and rapid thermal cycling

- id: B52-Q8
- concept_id: u7-thermal-shock-resistance
- format: topic-false
- asks: application
- origin: official-exam

Regarding thermal expansion, atomic bonding, and thermal shock resistance, which one of the following statements is FALSE:

a) Materials with strong atomic bonding and a deep potential well display low coefficients of thermal expansion
b) Increasing thermal conductivity $k$ and fracture stress $\sigma_f$ improves a brittle material's thermal shock resistance
c) Materials with a high $\alpha$ have strong atomic bonding and perform well under rapid heating and cooling
d) Rapid cooling puts the surface of a brittle ceramic under tensile stress, which can initiate cracking

### Answer

c

### Explanation

June 2017 extraordinary final exam, Q1.4 (and Session 15, Slides 36, 47-48): a high linear coefficient of thermal expansion $\alpha$ reflects weak atomic bonding (a shallow energy well), and from $TSR = \sigma_f k/(E\alpha_l)$ a high $\alpha$ produces large thermal strains and stresses during rapid heating and cooling, lowering thermal shock resistance. Statement c is therefore false.

- a) True: strong bonding corresponds to a deep, narrow energy well and small expansion on heating (Slide 36).
- b) True: both $\sigma_f$ and $k$ stand in the numerator of $TSR = \sigma_f k/(E\alpha_l)$ (Slide 48).
- d) True: rapid cooling shrinks the outer layer faster than the interior, putting the surface in tension where ceramics fracture easily (Slide 47).

### Source

MATERIALS_FINALEXAM_2017_EXTRA.pdf, p. 1 Q1.4; Session 15, Slides 36 and 47-48.

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
