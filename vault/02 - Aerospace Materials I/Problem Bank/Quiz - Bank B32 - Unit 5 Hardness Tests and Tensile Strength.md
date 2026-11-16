---
materia: Aerospace Materials I
tema: "Unit 5: hardness tests (Brinell, Vickers, Rockwell) and the relation between hardness and tensile strength"
bank_id: B32
title: "Hardness tests and hardness against tensile strength"
category: mt2_test_block
unit: 5
concepts:
  - u5-hardness-definition-methods
  - u5-brinell-calc
  - u5-vickers-rockwell
  - u5-hardness-tensile-relation
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 12, Slides 15-30."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-5
---

# Bank B32 — Hardness tests and hardness against tensile strength

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 12, Slides 15-30.

## Q32.1 Hardness tests in general

- id: B32-Q1
- concept_id: u5-hardness-definition-methods
- format: true-statement
- asks: comparison

Which one of the following statements about hardness tests is TRUE?

a) Rockwell hardness comes from the area of the indentation
b) The Mohs scale uses a diamond pyramid indenter
c) They are slow, costly and destructive tests
d) There is no universal conversion between their results

### Answer

d

### Explanation

Session 12, Slide 15: "the way you measure it is the way you define it", with "no universal conversion between results of these methods"; the tests are used in industry because they are fast, simple, inexpensive and non-destructive.

- a) Rockwell uses the depth of penetration; the area is used by Brinell and Vickers.
- b) Mohs is a scratch (abrasion) scale; the diamond pyramid belongs to Vickers.
- c) The slide says the opposite: they are fast, simple, inexpensive and non-destructive.

### Source

Session 12, Slides 15-16, 22 and 26.

## Q32.2 Brinell hardness of an aluminium alloy

- id: B32-Q2
- concept_id: u5-brinell-calc
- format: numeric
- asks: calculation
- calc: 2*500/(pi*10*(10-sqrt(10**2-2.8**2)))

A 10 mm Brinell ball under a load of 500 kg leaves an indentation of 2.8 mm diameter in an aluminium alloy. Determine the Brinell hardness:

a) 39.8 HB
b) 79.6 HB
c) 323 HB
d) 781 HB

### Answer

b

### Explanation

Session 12, Slide 19: $HB = \dfrac{2P}{\pi D\left(D - \sqrt{D^2 - D_i^2}\right)} = \dfrac{1000}{\pi \times 10 \times (10 - 9.60)} = \dfrac{1000}{12.57} = 79.6$ HB.

- a) The factor 2 of the formula was left out: the cap area was taken as $\pi D(D - \sqrt{D^2 - D_i^2})$.
- c) The radius of the indentation, 1.4 mm, was used instead of its diameter.
- d) The load was converted to newtons; the slide's formula takes $P$ in kg.

### Source

Session 12, Slide 19.

## Q32.3 Brinell load for a brass

- id: B32-Q3
- concept_id: u5-brinell-calc
- format: numeric
- asks: application
- calc: 10*5**2

Using the load factor that the slides assign to bronzes and brasses, determine the Brinell load for a brass tested with a 5 mm ball:

a) 50.0 kg
b) 125 kg
c) 250 kg
d) 750 kg

### Answer

c

### Explanation

Session 12, Slide 20: $Q = P/D^2$ is constant for each material, with $Q = 10$ for bronzes and brasses; $P = Q\,D^2 = 10 \times 5^2 = 250$ kg, as in the slide's table.

- a) The ball diameter was not squared: $Q\,D = 10 \times 5$.
- b) The load factor of aluminium alloys ($Q = 5$) was used instead of that of brasses.
- d) The load factor of steels ($Q = 30$) was used instead of that of brasses.

### Source

Session 12, Slide 20.

## Q32.4 Brinell test on a thin part

- id: B32-Q4
- concept_id: u5-brinell-calc
- format: complete-sentence
- asks: application

For a thin specimen, the slides' Brinell practice is to use:

a) a smaller ball diameter
b) a load in newtons instead of kilograms
c) a larger ball diameter
d) a higher load factor $Q$

### Answer

a

### Explanation

Session 12, Slide 20: "for small thicknesses, the ball diameter is reduced" (5, 2.5, 1.25 and 0.625 mm), keeping $P = Q\,D^2$; Slide 28 asks for a thickness greater than $2\cdot\varnothing$.

- b) The unit of the load does not change the depth of the indentation.
- c) A larger ball needs a larger load and a thicker specimen (thickness greater than 2 diameters of the indentation).
- d) $Q$ depends on the material, not on the thickness of the specimen.

### Source

Session 12, Slides 20 and 28.

## Q32.5 Vickers hardness from the diagonal

- id: B32-Q5
- concept_id: u5-vickers-rockwell
- format: numeric
- asks: calculation
- calc: 1.854*10/0.250**2

A Vickers test with a load of 10 kgf leaves an indentation with a mean diagonal of 0.250 mm. Determine the Vickers hardness:

a) 74.2 HV
b) 160 HV
c) 297 HV
d) 1190 HV

### Answer

c

### Explanation

Session 12, Slide 26: $\text{HV} = 1.854\,F/d^2 = 1.854 \times 10/0.250^2 = 18.54/0.0625 = 297$ HV, with $d$ the mean of the two diagonals in mm.

- a) The diagonal was not squared: $1.854 \times 10/0.250$.
- b) The constant 1.854 was left out: $10/0.250^2$.
- d) Half the diagonal, 0.125 mm, was used instead of the whole mean diagonal.

### Source

Session 12, Slide 26.

## Q32.6 Indenter of the Rockwell C scale

- id: B32-Q6
- concept_id: u5-vickers-rockwell
- format: identify
- asks: classification

Which indenter and major load does the Rockwell C scale use?

a) Tungsten carbide ball of 10 mm, 3000 kg
b) Diamond cone, 150 kg
c) Diamond pyramid of 136°, 30 kgf
d) 1/16 in steel ball, 100 kg

### Answer

b

### Explanation

Session 12, Slide 22 (Table 6.6a): scale C uses a diamond cone with a major load of 150 kg; scale B a 1/16 in ball with 100 kg.

- a) This is the standard Brinell test for steels ($Q = 30$).
- c) The 136° diamond pyramid is the Vickers indenter.
- d) This is the Rockwell B scale.

### Source

Session 12, Slides 20, 22 and 26.

## Q32.7 What Rockwell hardness depends on

- id: B32-Q7
- concept_id: u5-vickers-rockwell
- format: complete-sentence
- asks: definition

The Rockwell hardness is a function of:

a) the depth of penetration of the indenter
b) the scratch left on the surface
c) the length of the long diagonal
d) the area of the indentation

### Answer

a

### Explanation

Session 12, Slides 22-23: "the Rockwell hardness is a function of the depth of penetration"; $HR = N - h/S$, with $h$ the depth that remains after the additional load is removed.

- b) Scratching is the Mohs abrasion scale.
- c) The long diagonal $l$ gives the Knoop number, $14.2\,P/l^2$.
- d) The area under the load is the basis of Brinell and Vickers.

### Source

Session 12, Slides 16, 19, 22-23 and 29.

## Q32.8 Hardness and tensile strength

- id: B32-Q8
- concept_id: u5-hardness-tensile-relation
- format: true-statement
- asks: definition

Which one of the following statements about hardness and tensile strength in the slides is TRUE?

a) The two properties are not related at all
b) Hardness measures elastic stiffness, unlike tensile strength
c) One conversion factor holds for every material
d) Both indicate plastic deformation, by a material-specific relation

### Answer

d

### Explanation

Session 12, Slide 30: "the tensile strength and hardness are indicators of plastic deformation", and the relation between them depends on the material: the chart plots the Brinell hardness against the tensile strength with one line per family.

- a) The chart relates them for each family of materials.
- b) Hardness is resistance to permanent deformation, not to elastic deformation.
- c) The slide's chart has a separate line for steels, brass and nodular cast iron.

### Source

Session 12, Slides 15 and 30.

## Q32.9 Same hardness, different alloys

- id: B32-Q9
- concept_id: u5-hardness-tensile-relation
- format: complete-sentence
- asks: comparison

A steel and a brass with the same Brinell hardness have tensile strengths that:

a) must differ by the ratio of their moduli
b) must be equal, since their hardness is equal
c) may differ, since each family has its own line
d) cannot be estimated from hardness at all

### Answer

c

### Explanation

Session 12, Slide 30: the relation between hardness and tensile strength depends on the material; the chart gives separate lines for steels, brass and nodular cast iron.

- a) The relation is between two plastic properties; Young's modulus does not enter it.
- b) This assumes one universal relation; the slide's chart has a different line for each family.
- d) The chart of the slide is made precisely to estimate one from the other within a family.

### Source

Session 12, Slide 30.

## Q32.10 Harder steel, stronger steel

- id: B32-Q10
- concept_id: u5-hardness-tensile-relation
- format: cause-effect
- asks: effect

With an increase in the Brinell hardness of a steel, its tensile strength on the slide's chart:

a) increases, along the line for brass
b) increases, along the line for steels
c) does not change, since the two are unrelated
d) decreases, along the line for steels

### Answer

b

### Explanation

Session 12, Slide 30: hardness and tensile strength are both indicators of plastic deformation; on the chart the tensile strength of steels rises with the Brinell hardness along the steel line.

- a) The trend is right but the line is not: each family has its own line.
- c) The chart shows a clear rising relation for each family.
- d) The trend is inverted: both properties grow with the resistance to plastic deformation.

### Source

Session 12, Slide 30.
