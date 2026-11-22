---
materia: Aerospace Materials I
tema: "Unit 7: soft and hard magnetic materials, their applications and the factors that control the hysteresis loop"
bank_id: B47
title: "Soft and hard magnetic materials"
category: mt2_test_block
unit: 7
concepts:
  - u7-soft-hard-magnets
  - u7-hysteresis-remanence-coercivity
  - u7-magnet-applications
  - u7-loop-microstructure-temperature
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf, including an adaptation of Q6B from the June 2014 final exam. Content from Session 15, Slides 17-22."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-7
---

# Bank B47 — Soft and hard magnetic materials

> [!info] Includes official exam questions
> Ten test questions written for the bank in the style of Part I of Assessment Test II, including an adaptation of Q6B from the June 2014 final exam (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 15, Slides 17-22.

## Q47.1 Soft magnetic materials

- id: B47-Q1
- concept_id: u7-soft-hard-magnets
- format: true-statement
- asks: definition

Which one of the following statements is TRUE about soft magnetic materials?

a) Their Bloch walls are difficult to move, giving a wide loop
b) They have a high initial permeability and a low coercivity
c) Their coercivity is above 10 000 A/m, giving a wide loop
d) They are chosen for permanent magnets, as they keep their field

### Answer

b

### Explanation

Slide 18: in soft magnetic materials the Bloch walls are easy to move, which gives a high initial permeability and a low coercivity (a narrow loop).

- a) Hard and soft swapped: walls that are difficult to move, and the wide loop that follows, are the feature of hard magnetic materials.
- c) The limit is the other way round: $H_c$ above 10 000 A/m classifies a material as hard (Slide 18).
- d) Soft materials lose their magnetization easily, which is their purpose in transformer cores; permanent magnets need a high resistance to demagnetization, so they are made of hard materials (Slide 19).

### Source

Session 15, Slides 18-19.

## Q47.2 Reading a loop with a scale

- id: B47-Q2
- concept_id: u7-hysteresis-remanence-coercivity
- format: diagram-reading
- asks: classification
- check: 50e3 > 10000

From the shown B-H loop, indicate the coercivity of the material and its class:

![[attachments/MAT-MT2/u7-loop-hard-scale.svg]]

a) 50 kA/m, hard magnetic material
b) 50 kA/m, soft magnetic material
c) 0.9 T, hard magnetic material
d) 100 kA/m, hard magnetic material

### Answer

a

### Explanation

The loop crosses the H axis at $\pm 50$ kA/m, so $H_c = 50$ kA/m $= 50\,000$ A/m (Slide 17). This is above the limit $H_c = 10\,000$ A/m of Slide 18, so the material is hard.

- b) Right reading but wrong class: 50 kA/m is five times the 10 kA/m limit, so the material is hard, not soft.
- c) 0.9 T is where the loop crosses the B axis: the remanence $B_r$, an induction, not the coercivity.
- d) The full width of the loop between $-H_c$ and $+H_c$ is read as the coercivity; $H_c$ is half of it.

### Source

Session 15, Slides 17-18.

## Q47.3 Hard magnetic materials

- id: B47-Q3
- concept_id: u7-soft-hard-magnets
- format: false-statement
- asks: comparison

Which one of the following statements is FALSE about hard magnetic materials?

a) They have a high initial permeability
b) Their Bloch walls are difficult to move
c) They have a high resistance to demagnetization
d) Their coercivity is above 10 000 A/m

### Answer

a

### Explanation

Slide 18 lists a low initial permeability $\mu_i$ for the hard materials; the high initial permeability belongs to the soft ones, so statement a is false.

- b) True: the Bloch walls of hard materials are difficult to move (Slide 18).
- c) True: this is why they are used for permanent magnets (Slides 18-19).
- d) True: Slide 18 sets the limit between soft and hard materials at $H_c = 10\,000$ A/m.

### Source

Session 15, Slides 18-19.

## Q47.4 Loop for a transformer core

- id: B47-Q4
- concept_id: u7-magnet-applications
- format: choose-figure
- asks: application

Which picture shows the B-H curve best suited to the core of a transformer working under an alternating field?

a) ![[attachments/MAT-MT2/u7-loopopt-1.svg]]
b) ![[attachments/MAT-MT2/u7-loopopt-3.svg]]
c) ![[attachments/MAT-MT2/u7-loopopt-2.svg]]
d) ![[attachments/MAT-MT2/u7-loopopt-4.svg]]

### Answer

c

### Explanation

Slide 19: materials under alternating fields (cores of transformers, motors and generators) must minimize the energy losses, so they are soft magnetic materials with a small coercive field and a high permeability: the narrow loop of picture c.

- a) The wide loop belongs to a hard material, used for permanent magnets because it resists demagnetization.
- b) The rectangular loop is the one of magnetic memories (Slide 19), not of transformer cores.
- d) A straight line through the origin, with no loop and a small slope, is the response of a paramagnetic or diamagnetic material ($\mu_r$ close to 1), useless to increase the flux.

### Source

Session 15, Slides 5 and 18-19.

## Q47.5 Application of a hard magnet

- id: B47-Q5
- concept_id: u7-magnet-applications
- format: identify
- asks: application

Which of the following applications requires a hard magnetic material?

a) Transformer cores
b) Electric motor cores
c) Magnetic memories with a square loop
d) Permanent magnets

### Answer

d

### Explanation

Slide 19: permanent magnets use hard magnetic materials, because of their high resistance to demagnetization (high remanence and high coercive field).

- a) Transformer cores work under alternating fields and use soft materials, to minimize losses.
- b) Motor cores are also under alternating fields: soft materials, for the same reason.
- c) Magnetic memories use materials with a rectangular loop, which Slide 19 describes as soft materials modified by a thermal treatment in a field.

### Source

Session 15, Slide 19.

## Q47.6 Rectangular hysteresis loop

- id: B47-Q6
- concept_id: u7-magnet-applications
- format: complete-sentence
- asks: application

Materials with a rectangular hysteresis loop are used in:

a) permanent magnets
b) transformer cores under alternating fields
c) superconducting magnets for MRI
d) magnetic memories of computers

### Answer

d

### Explanation

Slide 19 matches the rectangular loop with magnetic memories in computers, magnetic amplifiers and pulse transformers (data storage).

- a) Permanent magnets need the wide loop of a hard material.
- b) Transformer cores need the narrow loop of a soft material.
- c) The MRI magnets of Slide 32 are superconducting electromagnets, an application of superconductivity, not of a hysteresis loop.

### Source

Session 15, Slides 19 and 32.

## Q47.7 Grain size and coercivity

- id: B47-Q7
- concept_id: u7-loop-microstructure-temperature
- format: cause-effect
- asks: effect

With an increase in the grain size of a ferromagnetic material, its coercivity:

a) increases, because the Bloch walls move more easily
b) decreases, because the Bloch walls move more easily
c) increases, because more boundaries pin the walls
d) decreases, because the saturation magnetization falls

### Answer

b

### Explanation

Slide 21: the Bloch walls move more easily in larger grains, so the permeability rises and $H_c$ and $B_r$ fall.

- a) Right cause with the inverted effect: easier wall motion makes the loop narrower, not wider.
- c) A larger grain size means fewer grain boundaries, not more, so fewer obstacles to the walls.
- d) Right trend, wrong cause: the saturation magnetization is fixed by the composition and does not change with the grain size; the fall in $H_c$ comes from the easier wall motion (Slide 20).

### Source

Session 15, Slides 20-21.

## Q47.8 Loop of iron below its Curie temperature

- id: B47-Q8
- concept_id: u7-loop-microstructure-temperature
- format: what-happens
- asks: effect

What will happen to the hysteresis loop of iron if its temperature rises but stays below the Curie temperature?

a) It shrinks, with lower $M_s$, $B_r$ and $H_c$
b) It widens, with higher $B_r$ and $H_c$
c) It does not change, since $M_s$ is fixed by composition
d) It becomes a straight line, as in a paramagnet

### Answer

a

### Explanation

Slide 22: a higher temperature raises the mobility of the dipoles; the maximum alignment is lower ($M_s$ falls) and the alignment is harder to keep when the field disappears ($B_r$ and $H_c$ fall), so the loop shrinks.

- b) Inverted trend: the thermal agitation makes the loop smaller, not larger.
- c) $M_s$ is constant for a given composition only at a given temperature; Slide 22 shows the loop shrinking as the temperature rises.
- d) The loss of the loop is what happens above $T_c$, where the material becomes paramagnetic; the statement keeps the temperature below $T_c$.

### Source

Session 15, Slides 20 and 22.

## Q47.9 Factors that control the loop

- id: B47-Q9
- concept_id: u7-loop-microstructure-temperature
- format: false-statement
- asks: cause

Which one of the following statements is FALSE about the factors that control the hysteresis loop?

a) The coercivity depends strongly on the microstructure
b) Pores and inclusions pin the Bloch walls
c) The saturation magnetization changes strongly with grain size
d) Strains from mechanical deformation affect the loop

### Answer

c

### Explanation

Slide 20: the saturation magnetization is constant for a material of a given composition; it does not depend on the grain size, so statement c is false.

- a) True: Slide 20 calls the coercivity a strongly microstructure-dependent property.
- b) True: inclusions, dislocations and pores reduce the mobility of the walls (Slide 21).
- d) True: the presence of strains due to mechanical deformation is one of the processing factors of Slide 20.

### Source

Session 15, Slides 20-21.

## Q47.10 Soft vs. hard B-H loops, applications and grain size

- id: B47-Q10
- concept_id: u7-soft-hard-magnets
- format: topic-true
- asks: application
- origin: official-exam

Regarding soft and hard ferromagnetic materials, their typical applications, and the effect of grain size on the hysteresis loop, which one of the following statements is TRUE:

a) A soft magnet shows a wide loop for permanent magnets, a hard magnet shows a narrow loop for transformers, and larger grains raise coercivity
b) A hard magnet shows a narrow loop for motor cores, a soft magnet shows a wide loop for permanent magnets, and larger grains raise permeability
c) A soft magnet shows a narrow loop for transformer cores, a hard magnet shows a wide loop for permanent magnets, and larger grains lower coercivity
d) A soft magnet shows a narrow loop for permanent magnets, a hard magnet shows a wide loop for transformers, and larger grains raise saturation magnetization

### Answer

c

### Explanation

Session 15, Slides 18-21 (and June 2014 final, Q6B): soft ferromagnets have narrow $B$-$H$ loops (low $H_c$, low hysteresis loss) suited to alternating-field applications such as transformer cores, whereas hard ferromagnets have wide loops (high $H_c$, high resistance to demagnetization) suited to permanent magnets. Increasing grain size decreases grain-boundary area so Bloch walls move more easily, increasing permeability and lowering coercivity and remanence.

- a) Swaps soft and hard loops/applications and inverts the grain-size effect on coercivity.
- b) Swaps soft and hard loops/applications, even though the grain-size trend for permeability is right.
- d) Swaps the applications of soft and hard magnets and wrongly claims grain size changes saturation magnetization (which depends on composition, Slide 20).

### Source

MATERIALS_FINALEXAM_2014_EXTRA.pdf, Q6B; Session 15, Slides 18-21.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
