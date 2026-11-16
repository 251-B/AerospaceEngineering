---
materia: Aerospace Materials I
tema: "Unit 5: percent cold work and its effects, solid solution strengthening and grain size strengthening"
bank_id: B30
title: "Effects of cold work, solid solution and grain size strengthening"
category: mt2_test_block
unit: 5
concepts:
  - u5-percent-cold-work
  - u5-cold-work-effects
  - u5-solid-solution-strengthening
  - u5-grain-size-strengthening
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 12, Slides 5-11."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-5
---

# Bank B30 — Effects of cold work, solid solution and grain size strengthening

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 12, Slides 5-11.

## Q30.1 Diameter after a given cold work

- id: B30-Q1
- concept_id: u5-percent-cold-work
- format: numeric
- asks: application
- calc: 20.0*sqrt(1-0.30)

A bar of 20.0 mm diameter must be cold drawn to a cold work of 30 %. Determine its final diameter:

a) 6.00 mm
b) 10.9 mm
c) 14.0 mm
d) 16.7 mm

### Answer

d

### Explanation

Session 12, Slide 6: $\%CW = (A_0 - A_d)/A_0 \times 100$, so $A_d = 0.70\,A_0$; with $A \propto d^2$, $d_d = 20.0\sqrt{0.70} = 16.7$ mm.

- a) The cold work fraction was applied to the diameter, $20 \times 0.30$, as if it were what remains.
- b) The cold work fraction was used as the remaining area: $20\sqrt{0.30}$.
- c) The remaining area fraction was applied to the diameter without the square root: $20 \times 0.70$.

### Source

Session 12, Slide 6.

## Q30.2 Effects of cold work

- id: B30-Q2
- concept_id: u5-cold-work-effects
- format: false-statement
- asks: effect

Which one of the following statements about cold work of a metal is FALSE?

a) It can lower the material cost of a design
b) It lowers the ductility of the metal
c) It lowers the hardness of the metal
d) It produces a texture along the rolling direction

### Answer

c

### Explanation

Session 12, Slide 5: strain hardening is "the increase in strength and hardness when a material is plastically deformed at low temperatures"; cold work raises the hardness, it does not lower it.

- a) This is true: if the process design takes it into account, the strength rises and the material cost falls (Slide 6).
- b) This is true: the higher the %CW, the lower the ductility (Slide 5).
- d) This is true: cold work gives a regular orientation of the grains (Slide 6).

### Source

Session 12, Slides 5-6.

## Q30.3 Yield strength of a steel against cold work

- id: B30-Q3
- concept_id: u5-cold-work-effects
- format: cause-effect
- asks: comparison

With an increase in the percent cold work, the yield strength of a 1040 steel on the slide's chart:

a) falls steadily over the whole range
b) rises along a straight line without limit
c) rises and then tends to level off
d) first falls and then rises

### Answer

c

### Explanation

Session 12, Slide 7: the yield strength of 1040 steel, brass and copper grows with the percent cold work, steeply at first and then more slowly, while the ductility falls.

- a) The trend is inverted: cold work strengthens the steel.
- b) The rise is not linear: the curves of the slide flatten at high cold work.
- d) The chart starts rising from 0 % cold work; there is no initial drop.

### Source

Session 12, Slides 5 and 7.

## Q30.4 Texture from cold work

- id: B30-Q4
- concept_id: u5-cold-work-effects
- format: identify
- asks: definition

Which description matches the texture that cold work produces in a metal, according to the slides?

a) A layer of precipitates along the grain boundaries
b) A regular orientation of the grains along the rolling direction
c) A random orientation of very fine grains
d) A surface roughness left by the rolls

### Answer

b

### Explanation

Session 12, Slide 6: cold work produces a texture, "a regular orientation of the grains in the direction of rolling".

- a) Precipitates belong to precipitation strengthening (Slide 12), not to cold work.
- c) Cold work aligns the grains; a random orientation is the opposite of a texture.
- d) The texture is an internal orientation of the grains, not a surface finish.

### Source

Session 12, Slides 6 and 12.

## Q30.5 Strain field around a solute atom

- id: B30-Q5
- concept_id: u5-solid-solution-strengthening
- format: true-statement
- asks: cause

Which one of the following statements about substitutional solute atoms in a metal is TRUE?

a) Solute atoms leave the lattice undistorted
b) A larger solute puts the surrounding atoms in tension
c) A smaller solute puts the surrounding atoms in tension
d) A smaller solute puts the surrounding atoms in compression

### Answer

c

### Explanation

Session 12, Slide 8: a smaller solute atom puts the host atoms around it in tension, a larger one puts them in compression; either way the lattice is distorted and dislocations move with more difficulty.

- a) Any solute of a different size distorts the lattice; this is why it hinders dislocations.
- b) The two cases are swapped: tension comes from a smaller solute.
- d) The two cases are swapped: compression comes from a larger solute.

### Source

Session 12, Slide 8.

## Q30.6 Why alloys are stronger than pure metals

- id: B30-Q6
- concept_id: u5-solid-solution-strengthening
- format: cause-effect
- asks: cause

Alloys are stronger than the pure metals they are made from because the impurity atoms:

a) make the grains of the metal coarser
b) strain the lattice and restrict dislocation motion
c) raise the Young's modulus of the metal
d) multiply the number of dislocations

### Answer

b

### Explanation

Session 12, Slide 9: "alloys are stronger than pure metals because impurity atoms impose strains on the surrounding host atoms", and these strains restrict the movement of dislocations.

- a) Coarser grains would lower the strength (Slide 10); this is not the mechanism of alloying.
- c) Stiffness is not strength; solid solutions are stronger because slip is harder.
- d) A higher dislocation density is the mechanism of strain hardening, not of alloying.

### Source

Session 12, Slides 5, 9 and 10.

## Q30.7 Property lowered by alloying

- id: B30-Q7
- concept_id: u5-solid-solution-strengthening
- format: identify
- asks: effect

Which property do alloying elements decrease, according to the slides on solid solution strengthening?

a) Yield strength
b) Hardness
c) Tensile strength
d) Electrical conductivity

### Answer

d

### Explanation

Session 12, Slide 9: alloying elements improve the yield strength, the UTS and the hardness, and decrease the ductility, the corrosion resistance and the electrical conductivity.

- a) Raising the yield strength is the purpose of solid solution strengthening.
- b) Alloying raises the hardness together with the yield strength and the UTS.
- c) Alloying raises the UTS (Slide 9).

### Source

Session 12, Slide 9.

## Q30.8 Strongest grain structure

- id: B30-Q8
- concept_id: u5-grain-size-strengthening
- format: choose-figure
- asks: comparison

Which picture describes the grain structure that gives the highest yield strength to the same alloy?

a) ![[attachments/MAT-MT2/u5-grains-2.svg]]
b) ![[attachments/MAT-MT2/u5-grains-4.svg]]
c) ![[attachments/MAT-MT2/u5-grains-1.svg]]
d) ![[attachments/MAT-MT2/u5-grains-3.svg]]

### Answer

a

### Explanation

Session 12, Slide 10: ↓ grain size → ↑ number of grains → ↑ barriers to dislocation motion → ↑ strengthening. The picture with the smallest grains has the most boundaries.

- b) These grains are finer than the medium ones but still coarser than the finest structure.
- c) These grains are of medium size; there are fewer boundaries to block slip than in the finest structure.
- d) This is the coarsest structure, with the fewest barriers: the lowest yield strength of the four.

### Source

Session 12, Slides 10-11.

## Q30.9 Why grain boundaries hinder slip

- id: B30-Q9
- concept_id: u5-grain-size-strengthening
- format: complete-sentence
- asks: cause

Grain boundaries make the slip of dislocations difficult because:

a) they are made of particles of a secondary phase
b) the neighbouring grains have the same orientation
c) they raise the Young's modulus of the metal
d) the neighbouring grains have different orientations

### Answer

d

### Explanation

Session 12, Slide 10: grain boundaries separate crystals with different orientations; "the grain boundary makes the sliding of dislocations difficult due to the angle" between neighbouring grains.

- a) Particles of a secondary phase are the obstacles of precipitation strengthening.
- b) If the orientation were the same, the slip planes would continue across and the boundary would not block slip.
- c) Grain boundaries affect the yield strength through slip, not the elastic stiffness.

### Source

Session 12, Slides 10 and 12.

## Q30.10 Ranking grain sizes by yield strength

- id: B30-Q10
- concept_id: u5-grain-size-strengthening
- format: ordering
- asks: comparison

Order four samples of the same alloy from the highest to the lowest yield strength by their grain sizes: 10, 50, 100 and 200 μm:

a) 10 > 50 > 100 > 200 μm
b) 200 > 100 > 50 > 10 μm
c) 50 > 10 > 100 > 200 μm
d) 10 > 100 > 50 > 200 μm

### Answer

a

### Explanation

Session 12, Slide 10: the yield strength rises as the grain size falls (the slide's plot of $\sigma_y$ against $d^{-1/2}$ is a straight line), so the finest grains give the highest yield strength.

- b) This is the complete order reversed: larger grains mean fewer barriers and a lower yield strength.
- c) The first pair is swapped: the 10 μm sample has more boundaries than the 50 μm one.
- d) The middle pair is swapped: 50 μm grains give more barriers than 100 μm grains.

### Source

Session 12, Slide 10.
