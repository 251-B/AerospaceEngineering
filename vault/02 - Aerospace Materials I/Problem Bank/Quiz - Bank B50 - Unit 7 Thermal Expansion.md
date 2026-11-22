---
materia: Aerospace Materials I
tema: "Unit 7: linear coefficient of thermal expansion, bonding, melting temperature, allotropy and bimetals"
bank_id: B50
title: "Thermal expansion"
category: mt2_test_block
unit: 7
concepts:
  - u7-expansion-values-materials
  - u7-linear-expansion-calc
  - u7-expansion-bonding-well
  - u7-expansion-melting-allotropy
  - u7-bimetal-strip
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf, including Q10 of that paper (linear coefficient of thermal expansion). Content and data from Session 15, Slides 36-39."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-7
---

# Bank B50 — Thermal expansion

> [!info] Includes official exam questions
> Ten test questions written for the bank in the style of Part I of Assessment Test II, including an official Assessment Test II item (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 15, Slides 36-39.

## Q50.1 Expansion of the material families

- id: B50-Q1
- concept_id: u7-expansion-values-materials
- format: complete-sentence
- asks: comparison

Comparing the linear coefficient of thermal expansion across the main classes of materials:

a) is higher for materials with a deeper bonding energy well
b) is larger for polymers than for ceramics
c) is the same over the whole temperature range of a solid
d) of tungsten is higher than that of aluminium, as tungsten melts higher

### Answer

b

### Explanation

Slide 38: polymers have coefficients of about $90$ to $220\times10^{-6}$ °C⁻¹, while the ceramics of the table range from $0.4$ to $13.5\times10^{-6}$ °C⁻¹.

- a) Inverted trend: a deep well means strong bonding, and strong bonding gives a low coefficient (Slide 36).
- c) The coefficient of iron changes abruptly at its allotropic transformations (Slide 37), so it is not the same at every temperature.
- d) Wrong comparison with a reason that points the other way: tungsten has $4.5\times10^{-6}$ against $23.6\times10^{-6}$ °C⁻¹ for aluminium, and its higher melting temperature is why its coefficient is lower.

### Source

Session 15, Slides 36-38.

## Q50.2 Elongation of an aluminium rod

- id: B50-Q2
- concept_id: u7-linear-expansion-calc
- format: numeric
- asks: calculation
- calc: 23.6e-6*2000*(170-20)

A 2.00 m aluminium rod ($\alpha = 23.6\times10^{-6}$ °C⁻¹) is heated freely from 20 °C to 170 °C. Determine its elongation:

a) $7.08\times10^{-3}$ mm
b) 3.54 mm
c) 7.08 mm
d) 8.02 mm

### Answer

c

### Explanation

$\Delta l = \alpha\,l_0\,\Delta T$ (Slide 36): $23.6\times10^{-6}\times2000\ \text{mm}\times(170 - 20) = 7.08$ mm.

- a) The result in metres, $7.08\times10^{-3}$ m, is written as millimetres.
- b) The original length is left out: the strain $\alpha\Delta T = 3.54\times10^{-3}$ is read as millimetres per metre and not multiplied by the 2 m of the rod.
- d) The final temperature is used instead of the change: $23.6\times10^{-6}\times2000\times170 = 8.02$ mm.

### Source

Session 15, Slides 36 and 38.

## Q50.3 Two potential energy curves

- id: B50-Q3
- concept_id: u7-expansion-bonding-well
- format: diagram-reading
- asks: figure-reading

The figure shows the potential energy against interatomic distance for two materials, 1 and 2. Indicate which statement is TRUE:

![[attachments/MAT-MT2/u7-energy-wells.svg]]

a) Material 2 has the lower α, as its well is wider
b) Both have the same α, as their minima lie at the same r
c) Material 1 has the higher α, as its bond is stronger
d) Material 1 has the lower α, as its well is deep and narrow

### Answer

d

### Explanation

Slide 36: materials with a high bonding energy (a deep, narrow well) have low coefficients of thermal expansion; when heated, their equilibrium spacing grows less than that of a shallow, wide well such as curve 2.

- a) Inverted reading: the wide, shallow well is the weak bond, which expands more on heating.
- b) The position of the minimum fixes the spacing at rest, not how much it grows when the vibration energy rises; that depends on the depth and shape of the well.
- c) Right premise (curve 1 is the stronger bond) with the inverted consequence: strong bonding gives a low $\alpha$.

### Source

Session 15, Slide 36.

## Q50.4 Why a bar lengthens on heating

- id: B50-Q4
- concept_id: u7-expansion-bonding-well
- format: cause-effect
- asks: cause

With an increase in temperature, the length of a solid bar increases because:

a) the atoms themselves grow in size
b) the vibration energy rises and the mean atomic spacing grows
c) the bonding energy of the material rises
d) the atoms vibrate faster about unchanged positions

### Answer

b

### Explanation

Slide 36: heating raises the vibration energy of the atoms, and on the energy-distance curve this moves the equilibrium (mean) spacing between the atoms to larger values, so the bar lengthens.

- a) The size of the atoms does not change; what grows is the mean distance between them.
- c) Heating does not strengthen the bonds; a higher bonding energy would in fact mean a lower expansion.
- d) If the atoms vibrated about unchanged mean positions, the length would not change; expansion needs the mean spacing to grow.

### Source

Session 15, Slide 36.

## Q50.5 Allotropy and expansion

- id: B50-Q5
- concept_id: u7-expansion-melting-allotropy
- format: false-statement
- asks: effect

Which one of the following statements is FALSE about thermal expansion?

a) Allotropic changes cause abrupt changes of dimensions
b) Phase transformations can crack refractories
c) Invar expands much less than pure iron
d) The coefficient of iron is the same in its α and γ phases

### Answer

d

### Explanation

Slide 37: the linear coefficient of thermal expansion of iron changes abruptly at the temperatures where an allotropic transformation occurs, so it is not the same in the $\alpha$ and $\gamma$ phases.

- a) True: allotropic materials have abrupt changes in their dimensions when phase transformations occur (Slide 37).
- b) True: the slide names cracking in refractories as the consequence.
- c) True: Invar has $1.6\times10^{-6}$ against $11.8\times10^{-6}$ °C⁻¹ for iron (Slide 38).

### Source

Session 15, Slides 37-38.

## Q50.6 Thermal expansion and bonding energy well

- id: B50-Q6
- concept_id: u7-expansion-bonding-well
- format: complete-sentence
- asks: effect
- origin: official-exam

The linear coefficient of thermal expansion:

a) is high when atomic bonding is strong
b) is not affected by allotropic changes
c) is low when the material shows a deep bonding energy well
d) of iron is higher than that of lead, due to its higher melting temperature

### Answer

c

### Explanation

Session 15, Slides 36-37: materials with high bonding energy display a deep, narrow potential energy well, so raising vibrational energy increases the mean interatomic spacing only slightly and yields a low linear coefficient of thermal expansion.

- a) Inverted trend: strong atomic bonding lowers the thermal expansion coefficient rather than raising it.
- b) False statement: allotropic transformations (such as $\alpha \to \gamma$ in iron) cause abrupt changes in dimensions and $\alpha$ (Slide 37).
- d) Inverted comparison with a contradicting cause: iron has a higher melting temperature than lead, which reflects stronger bonding and therefore a lower $\alpha$ than lead.

### Source

MATERIALS_SECONDPARTIAL_2019.pdf, p. 3 Q10 (also MATERIALS_SECONDPARTIAL_2018.docx, Q10; MATERIALS_THIRDPARTIAL_2020_V2.pdf, p. 3 Q10); Session 15, Slides 36-37.

## Q50.7 Ranking of expansion coefficients

- id: B50-Q7
- concept_id: u7-expansion-values-materials
- format: ordering
- asks: comparison

Order fused silica, alumina, copper and high-density polyethylene by increasing linear coefficient of thermal expansion.

a) fused silica, alumina, copper, polyethylene
b) polyethylene, copper, alumina, fused silica
c) fused silica, copper, alumina, polyethylene
d) polyethylene, fused silica, alumina, copper

### Answer

a

### Explanation

Slide 38: fused silica $0.4$, alumina $7.6$, copper $17.0$ and polyethylene $106$-$198\times10^{-6}$ °C⁻¹.

- b) The fully reversed order.
- c) Copper and alumina swapped, as if a metal expanded less than an ionic ceramic.
- d) This is the order of the thermal conductivity $k$ (0.46-0.50, 1.4, 39 and 398 W/(m·K)), the neighbouring column of the same table.

### Source

Session 15, Slide 38.

## Q50.8 Heating a copper-iron bimetal

- id: B50-Q8
- concept_id: u7-bimetal-strip
- format: what-happens
- asks: application
- check: 17.0 > 11.8

A straight bimetallic strip of copper ($\alpha = 17.0\times10^{-6}$ °C⁻¹) bonded to iron ($\alpha = 11.8\times10^{-6}$ °C⁻¹) is heated. What will happen?

a) It bends towards the copper, as copper expands more
b) It stays straight, as both metals expand
c) It bends towards the iron, as copper expands more
d) It bends towards the copper, as iron expands more

### Answer

c

### Explanation

Slide 39: the two metals are bonded and have different coefficients; on heating the copper, with the larger $\alpha$, lengthens more, so the copper side becomes the outside of the curve and the strip bends towards the iron.

- a) Right reason, wrong side: the metal that lengthens more is on the convex (outer) side, so the strip curves away from it.
- b) Both metals expand, but by different amounts; since they are bonded, the difference can only be taken up by bending.
- d) The data are misread: iron has the smaller coefficient, 11.8 against 17.0 ×10⁻⁶ °C⁻¹.

### Source

Session 15, Slides 38-39.

## Q50.9 Material for constant length

- id: B50-Q9
- concept_id: u7-expansion-values-materials
- format: identify
- asks: application

Which metallic alloy is specifically designed to keep its length nearly constant when the temperature changes?

a) Brass
b) Tungsten
c) Plain carbon steel
d) Invar (Fe-36% Ni)

### Answer

d

### Explanation

Session 15, Slide 38 highlights Invar (64Fe-36Ni, $\alpha = 1.6\times10^{-6}$ °C⁻¹) as a dedicated low-expansion alloy, far below plain carbon steel ($\sim 12\times10^{-6}$ °C⁻¹) or brass ($\sim 20\times10^{-6}$ °C⁻¹).

- a) Brass has a large expansion coefficient (about $20\times10^{-6}$ °C⁻¹), so it is used as the high-expansion half of bimetallic strips rather than for constant length.
- b) Pure tungsten has a relatively low coefficient ($4.5\times10^{-6}$ °C⁻¹) for a pure metal, but still nearly three times larger than Invar.
- c) Plain carbon steel expands by roughly $12\times10^{-6}$ °C⁻¹, nearly an order of magnitude more than Invar.

### Source

Session 15, Slide 38.

## Q50.10 Melting temperature and expansion

- id: B50-Q10
- concept_id: u7-expansion-melting-allotropy
- format: cause-effect
- asks: effect

With an increase in the melting temperature of a metal, its linear coefficient of thermal expansion at 25 °C:

a) increases, because its atoms vibrate more strongly
b) decreases, because its bonding is stronger
c) decreases, because the metal is denser
d) increases, because a stiffer bond pushes the atoms further apart

### Answer

b

### Explanation

Slide 37 plots the coefficient of the metals at 25 °C against their melting temperature: the higher the melting temperature, the lower the coefficient, because a high melting temperature reflects strong bonding, which gives low expansion (Slide 36).

- a) Inverted trend: metals with a high melting temperature expand less, not more.
- c) Right trend, wrong cause: the slides relate the coefficient to the bonding energy, not to the density.
- d) Inverted trend with a plausible cause: a strong bond is stiff, but the slides link strong bonding to low expansion, so the chart of Slide 37 falls with the melting temperature.

### Source

Session 15, Slides 36-37.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
