---
materia: Aerospace Materials I
tema: "Unit 5: Young's modulus and bonding, moduli of material families, non-linear elasticity, compression and bend tests"
bank_id: B19
title: "Young's modulus, bonding, families of materials and non-linear elasticity"
category: mt2_test_block
unit: 5
concepts:
  - u5-modulus-bond-strength
  - u5-modulus-ranking-families
  - u5-nonlinear-modulus-types
  - u5-compression-test
  - u5-bend-test
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 11, Slides 5-6 and 13-17."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-5
---

# Bank B19 — Young's modulus, bonding, families of materials and non-linear elasticity

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 11, Slides 5-6 and 13-17.

## Q19.1 Modulus and the interatomic force curve

- id: B19-Q1
- concept_id: u5-modulus-bond-strength
- format: true-statement
- asks: definition

Which one of the following statements about the Young's modulus at the atomic scale is TRUE?

a) It equals the bonding force at the equilibrium spacing $r_0$
b) It does not depend on the strength of the bonds
c) It is proportional to the slope of the force curve at $r_0$
d) It is the slope of the force curve at its maximum

### Answer

c

### Explanation

Session 11, Slide 13: $E \propto (\partial F/\partial r)_{r_0}$, the slope of the interatomic force curve at the equilibrium spacing; Slide 14 shows that the nearly straight part of that curve is the straight elastic line of the stress-strain curve.

- a) At $r_0$ the net bonding force is zero; the modulus comes from the slope of the curve there, not from its value.
- b) Slide 13 states the opposite: $E = f(\text{bond strength})$, a stronger bond gives a larger $E$.
- d) The atoms work around the equilibrium spacing, where the curve is nearly straight; the maximum of the force curve is far from it.

### Source

Session 11, Slides 13-14.

## Q19.2 Bonding and stiffness

- id: B19-Q2
- concept_id: u5-modulus-bond-strength
- format: false-statement
- asks: comparison

Which one of the following statements about bonding and elastic behaviour is FALSE?

a) Weakly bonded materials have the highest Young's moduli
b) Elastic deformation is reversible
c) Ceramics are stiffer than metals
d) Stronger bonds go with higher melting temperatures

### Answer

a

### Explanation

Session 11, Slide 13: "↑ bond strength ↔ ↑E". Weak bonds give the lowest moduli (polymers), so the statement inverts the trend.

- b) This is true: "elastic means reversible" (Slide 12).
- c) This is true: $E_{\text{ceramics}} > E_{\text{metals}} > E_{\text{polymers}}$ (Slide 13).
- d) This is true: Slide 13 links the bond force with the melting temperature.

### Source

Session 11, Slides 12-13.

## Q19.3 Ranking four materials by modulus

- id: B19-Q3
- concept_id: u5-modulus-ranking-families
- format: ordering
- asks: comparison

Order these materials from the highest to the lowest Young's modulus: steel, alumina, aluminium and high-density polyethylene:

a) Alumina > aluminium > steel > HDPE
b) HDPE > aluminium > steel > alumina
c) Alumina > steel > aluminium > HDPE
d) Steel > alumina > aluminium > HDPE

### Answer

c

### Explanation

Session 11, Slide 17: alumina 393 GPa, steel 207 GPa, aluminium 69 GPa, HDPE 1.08 GPa; the order follows ceramics > metals > polymers (Slide 13).

- a) The middle pair is swapped: aluminium (69 GPa) is about three times less stiff than steel.
- b) This is the complete order reversed, from the lowest to the highest modulus.
- d) The first pair is swapped: alumina (393 GPa) is stiffer than steel (207 GPa).

### Source

Session 11, Slides 13 and 17.

## Q19.4 Families of materials by modulus

- id: B19-Q4
- concept_id: u5-modulus-ranking-families
- format: complete-sentence
- asks: classification

By elastic modulus, the slides rank the families of materials as:

a) metals, then ceramics, then polymers
b) ceramics, then metals, then polymers
c) metals, then polymers, then ceramics
d) polymers, then metals, then ceramics

### Answer

b

### Explanation

Session 11, Slide 13: $E_{\text{ceramics}} > E_{\text{metals}} > E_{\text{polymers}}$; the bubble chart of Slide 18 shows the same order.

- a) Metals and ceramics are swapped; ceramics, with their strong ionic and covalent bonds, have the highest moduli.
- c) Ceramics are put last although they are the stiffest family; polymers have the lowest moduli.
- d) This is the order reversed, from the lowest to the highest modulus.

### Source

Session 11, Slides 13 and 18.

## Q19.5 Stiffest material per unit mass

- id: B19-Q5
- concept_id: u5-modulus-ranking-families
- format: identify
- asks: comparison
- check: 390/3.9 > max(210/7.8, 70/2.7, 69/2.6)

According to the specific modulus $E/\rho$ in the slides, which material is the stiffest per unit mass?

a) Alumina
b) Aluminium alloy
c) Silica
d) Steel

### Answer

a

### Explanation

Session 11, Slide 13: alumina has $E = 390$ GPa and $\rho = 3.9$ Mg/m³, so $E/\rho = 100$ GPa/(Mg/m³), about four times the value of steels (27), Al alloys (26) and silica (27).

- b) Aluminium alloys are light, but their modulus is low: $E/\rho = 70/2.7 = 26$.
- c) Silica has a low density but also a low modulus (69 GPa): $E/\rho = 27$.
- d) Steel has a high modulus (210 GPa) but also a high density (7.8 Mg/m³), so $E/\rho = 27$, like aluminium.

### Source

Session 11, Slide 13.

## Q19.6 Secant and tangent lines on a non-linear curve

- id: B19-Q6
- concept_id: u5-nonlinear-modulus-types
- format: diagram-reading
- asks: figure-reading

From the shown non-linear stress-strain curve, identify the lines that give the secant and the tangent modulus at point Q:

![[attachments/MAT-MT2/u5-nonlinear-moduli.svg]]

a) Secant: line 3; tangent: line 2
b) Secant: line 1; tangent: line 3
c) Secant: line 2; tangent: line 1
d) Secant: line 2; tangent: line 3

### Answer

d

### Explanation

Session 11, Slide 15: the secant modulus is measured "between origin and" the chosen point, so it is line 2 from O to Q; the tangent modulus is the slope of the curve at the strain of interest, line 3 at Q; line 1 is the initial modulus.

- a) The two definitions are swapped: the secant joins the origin to Q, the tangent touches the curve at Q.
- b) Line 1 is tangent to the curve at the origin, which is the initial modulus, not the secant.
- c) Line 1 is the tangent at the origin; the tangent modulus at Q is the slope of the curve at Q itself.

### Source

Session 11, Slide 15.

## Q19.7 Initial modulus of a non-linear material

- id: B19-Q7
- concept_id: u5-nonlinear-modulus-types
- format: complete-sentence
- asks: definition

For a non-linear elastic material, the initial modulus is defined for strains:

a) up to the tensile strength
b) below 0.5 %
c) at any strain of interest
d) equal to 2 %

### Answer

b

### Explanation

Session 11, Slide 15: initial $E$ for $\varepsilon < 0.5\,\%$, secant $E$ for $\varepsilon = 2\,\%$, tangent $E$ at the desired $\varepsilon$; Hooke's law becomes $\sigma = E(\varepsilon)\,\varepsilon$.

- a) The three practical moduli belong to the elastic response; the tensile strength is a plastic, ultimate property.
- c) The modulus at the strain of interest is the tangent modulus.
- d) A strain of 2 % is where the slide defines the secant modulus.

### Source

Session 11, Slide 15.

## Q19.8 Materials with non-linear elasticity

- id: B19-Q8
- concept_id: u5-nonlinear-modulus-types
- format: identify
- asks: classification

Which group of materials shows non-linear elastic behaviour according to the slides?

a) Some polymers, concrete and grey cast irons
b) Steels, aluminium alloys and copper
c) Alumina, silicon carbide and soda-lime glass
d) Tungsten, nickel and titanium

### Answer

a

### Explanation

Session 11, Slide 15: non-linear elasticity "is produced in some materials (some polymers, concrete, gray cast irons)"; then $E$ depends on $\varepsilon$.

- b) These metals follow Hooke's law with a straight elastic line and a single modulus.
- c) These ceramics and glasses are linear and steep up to fracture.
- d) These metals have constant moduli listed on Slide 17; their elastic zone is linear.

### Source

Session 11, Slides 15 and 17.

## Q19.9 Use of the compression test

- id: B19-Q9
- concept_id: u5-compression-test
- format: complete-sentence
- asks: application

The compression test is applied mainly to materials that:

a) are used to make springs
b) neck strongly before they fracture
c) are thin coatings on a component
d) behave in a fragile way, like concrete and ceramics

### Answer

d

### Explanation

Session 11, Slide 5: the compression test is for "materials that exhibit a fragile behavior (i.e. concrete)" and it is "widely applied to ceramics".

- a) Springs call for a high modulus of resilience, a tensile property (Slide 35).
- b) Necking is a feature of ductile metals in tension; it is not why a compression test is chosen.
- c) Thin coatings are measured with surface hardness or microhardness tests (Session 12).

### Source

Session 11, Slide 5; Session 11, Slide 35; Session 12, Slides 17 and 27.

## Q19.10 Where a bend specimen breaks

- id: B19-Q10
- concept_id: u5-bend-test
- format: true-statement
- asks: effect

Which one of the following statements about the three-point bend test is TRUE?

a) The whole specimen is under a uniform tension
b) Fracture starts at the upper surface, under compression
c) The upper surface is in tension and the lower in compression
d) Fracture starts at the lower surface, under tension

### Answer

d

### Explanation

Session 11, Slide 6: at the point where the load is applied the upper surface is under compressive stress and the lower surface under tensile stress, and fracture occurs along the outermost edge, which is under tension.

- a) The specimen is under both tension and compression; that is why the slide says it avoids testing them separately.
- b) The upper surface is under compression, but the fracture starts on the outermost edge under tension.
- c) The two sides are swapped: below the load point the upper surface is compressed and the lower one stretched.

### Source

Session 11, Slide 6.
