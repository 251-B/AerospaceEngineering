---
materia: Aerospace Materials I
tema: "Unit 7: domains, the initial magnetization curve, permeabilities, remanence and coercivity"
bank_id: B46
title: "Magnetization curve and hysteresis loop"
category: mt2_test_block
unit: 7
concepts:
  - u7-domains-bloch-walls
  - u7-initial-magnetization-curve
  - u7-initial-max-permeability
  - u7-hysteresis-remanence-coercivity
  - u7-soft-hard-magnets
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 15, Slides 14-18 and 24."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-7
---

# Bank B46 — Magnetization curve and hysteresis loop

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 15, Slides 14-18 and 24.

## Q46.1 Domains and grains

- id: B46-Q1
- concept_id: u7-domains-bloch-walls
- format: true-statement
- asks: comparison

Which one of the following statements is TRUE about magnetic domains?

a) A small grain can be a single magnetic domain
b) Domains are usually larger than the grains that hold them
c) A Bloch wall is about 100 μm thick
d) A never-magnetized ferromagnet has a large net magnetization

### Answer

a

### Explanation

Slide 14: domains (about 10 to 100 μm) are usually smaller than the grains, and the slide draws a small grain that is a single domain while a larger grain contains several.

- b) Inverted comparison: the domains are usually smaller than the grains.
- c) Sizes swapped: the domain is 10 to 100 μm, the Bloch wall about 100 nm (some 300 atoms).
- d) Because of the domains, a ferromagnetic material never exposed to a field has a null net magnetization (Slide 14).

### Source

Session 15, Slide 14.

## Q46.2 Stages of the initial magnetization curve

- id: B46-Q2
- concept_id: u7-initial-magnetization-curve
- format: diagram-reading
- asks: figure-reading

In the shown initial magnetization curve of a demagnetized ferromagnet, the rotation of the domains towards the field takes place mainly:

![[attachments/MAT-MT2/u7-init-curve-stages.svg]]

a) between O and point 1
b) between points 1 and 2
c) between points 2 and 3
d) beyond point 3

### Answer

c

### Explanation

Slide 16: the magnetization grows slowly at first (O to 1), then rapidly while the favourable domains grow (1 to 2), and then it slows down because the domains must rotate to reach saturation (2 to 3); beyond 3 the curve is flat, at saturation.

- a) The slow start, at the initial permeability, comes before the fast growth of the domains, not at the end.
- b) The steep part is the growth of the favourable domains at the expense of the others, not their rotation.
- d) Beyond point 3 the curve is flat: saturation has been reached and nothing is left to rotate.

### Source

Session 15, Slide 16.

## Q46.3 Saturation magnetization

- id: B46-Q3
- concept_id: u7-initial-magnetization-curve
- format: complete-sentence
- asks: definition

The saturation magnetization $M_s$ of a ferromagnet is reached when:

a) all the dipoles of the solid are aligned with the field
b) the field is brought back to zero after magnetizing
c) the favourable domains start to grow
d) a reverse field brings the induction to zero

### Answer

a

### Explanation

Slide 16: the saturation magnetization is the magnetization that results when all the magnetic dipoles of the solid are aligned with the external field.

- b) The induction left at zero field is the remanence $B_r$ (Slide 17).
- c) The growth of the favourable domains is an early stage of the curve, well below saturation.
- d) The reverse field that brings $B$ to zero is the coercivity $H_c$ (Slide 17).

### Source

Session 15, Slides 16-17.

## Q46.4 Slope of the tangent from the origin

- id: B46-Q4
- concept_id: u7-initial-max-permeability
- format: identify
- asks: definition

Which quantity is the slope of the line drawn from the origin tangent to the initial magnetization curve?

a) The initial permeability
b) The maximum permeability
c) The coercivity
d) The remanence

### Answer

b

### Explanation

Slide 16: the maximum permeability $\mu_{max}$ is the slope of the line from the origin tangent to the curve, the largest value of $B/H$ along it.

- a) The initial permeability $\mu_i$ is the slope of the curve at its start, at the origin itself.
- c) The coercivity is a field read on the hysteresis loop (Slide 17), not a slope.
- d) The remanence is an induction read at $H = 0$ on the loop, not a slope of the initial curve.

### Source

Session 15, Slides 16-17.

## Q46.5 Initial and maximum permeability along the curve

- id: B46-Q5
- concept_id: u7-initial-max-permeability
- format: topic-true
- asks: comparison

Regarding the initial permeability $\mu_i$ and the maximum permeability $\mu_{\max}$ of a ferromagnetic material, which one of the following statements is TRUE:

a) Both $\mu_i$ and $\mu_{\max}$ remain identical at every field strength $H$, because $B$ rises linearly up to saturation
b) The maximum permeability $\mu_{\max}$ is the slope at the origin, whereas $\mu_i$ is measured once the loop saturates
c) The initial permeability $\mu_i$ is larger than $\mu_{\max}$, because domain walls move fastest at zero field
d) The permeability varies with $H$, with $\mu_i$ as the slope at the origin and $\mu_{\max}$ as the steepest secant slope $B/H$

### Answer

d

### Explanation

Session 15, Slide 16: the permeability $\mu = B/H$ of a ferromagnet changes along the initial magnetization curve; $\mu_i$ is the initial slope at $H = 0$, and $\mu_{\max}$ is the slope of the line from the origin tangent to the curve (the maximum ratio $B/H$).

- a) Treats $B(H)$ as linear: in a ferromagnet the curve is S-shaped (slow start, rapid domain growth, then domain rotation to saturation).
- b) Swaps the definitions and adds a false saturation slope: the slope at saturation approaches $\mu_0$, whereas $\mu_{\max}$ is at the tangent point from the origin.
- c) Inverts the ordering: the initial slope $\mu_i$ is gentler than the tangent slope $\mu_{\max}$ reached during rapid domain growth.

### Source

Session 15, Slide 16.

## Q46.6 First stages of magnetization

- id: B46-Q6
- concept_id: u7-initial-magnetization-curve
- format: cause-effect
- asks: cause

With an increase in the applied field from zero, the magnetization of a demagnetized iron sample:

a) falls, because the Bloch walls are pinned
b) grows, because dipoles are induced opposite to the field
c) stays at zero until saturation is reached
d) grows, because favourable domains grow at the expense of others

### Answer

d

### Explanation

Slide 16: starting from a random distribution of domains, the field makes the domains oriented favourably grow and the unfavourable ones shrink, so the magnetization rises (later the domains rotate and saturate).

- a) Inverted trend: pinned walls make the growth harder (Slide 21), but the magnetization still rises with the field.
- b) Right trend with the diamagnetic mechanism; opposite induced dipoles would lower the magnetization.
- c) Saturation is the end of the curve, reached after the magnetization has grown through every stage.

### Source

Session 15, Slide 16.

## Q46.7 Remanence on a loop

- id: B46-Q7
- concept_id: u7-hysteresis-remanence-coercivity
- format: diagram-reading
- asks: figure-reading

On the shown B-H hysteresis loop, which point gives the remanence of the material?

![[attachments/MAT-MT2/u7-loop-points.svg]]

a) Point P
b) Point Q
c) Point R
d) Point S

### Answer

b

### Explanation

The remanence $B_r$ is the induction that remains when the field is brought back to zero (Slide 17): the point where the descending branch crosses the B axis, point Q.

- a) P is the tip of the loop at the largest field, the saturation induction $B_s$.
- c) R lies on the H axis, where $B = 0$: its abscissa is the coercivity $-H_c$.
- d) S is the tip of the loop at saturation in the reverse direction, $-B_s$.

### Source

Session 15, Slides 17-18.

## Q46.8 Coercivity

- id: B46-Q8
- concept_id: u7-hysteresis-remanence-coercivity
- format: complete-sentence
- asks: definition

The coercivity $H_c$ of a ferromagnetic material is:

a) the induction left when the field returns to zero
b) the field needed to reach saturation
c) the slope of the initial magnetization curve
d) the reverse field needed to bring the induction to zero

### Answer

d

### Explanation

Slide 17: $H_c$ is the reverse field needed to bring the induction to zero, a measure of the opposition of the dipoles to a change of orientation.

- a) This is the remanence $B_r$, the neighbouring quantity read on the same loop.
- b) The field at saturation is not given a name on the slides; it is not the coercivity.
- c) The slope at the start of the curve is the initial permeability $\mu_i$ (Slide 16).

### Source

Session 15, Slide 17.

## Q46.9 Reducing the field from saturation to zero

- id: B46-Q9
- concept_id: u7-hysteresis-remanence-coercivity
- format: what-happens
- asks: effect

A ferromagnetic material is magnetized to saturation and the applied field $H$ is then reduced back to zero. What happens to the magnetic induction $B$?

a) It returns linearly along the initial curve to zero, because the domains instantly become random again
b) It rises above the saturation induction $B_s$, because the removal of $H$ aligns the remaining domains
c) It stays positive at the remanence $B_r$, because the domains do not return to their random arrangement
d) It immediately reverses to $-B_r$, because the demagnetized state opposes the previous field

### Answer

c

### Explanation

Session 15, Slide 17: as $H$ drops from saturation back to zero, the domains do not return to their original random arrangement, so a positive remanent induction $B_r$ remains at $H = 0$ (a reverse field $H_c$ is needed to bring $B$ back to zero).

- a) Describes reversible (non-hysteretic) behaviour; hysteresis arises precisely because the descending branch does not retrace the initial curve.
- b) Inverted direction: reducing the aligning field lets some domain rotation relax, so $B_r \le B_s$, never above $B_s$.
- d) Reversing the induction requires applying an opposite field past $-H_c$; at $H = 0$ the remanence keeps the same sign as saturation.

### Source

Session 15, Slide 17.

## Q46.10 Two loops on the same axes

- id: B46-Q10
- concept_id: u7-soft-hard-magnets
- format: diagram-reading
- asks: classification

From the two shown B-H loops, drawn on the same axes, indicate which statement is TRUE:

![[attachments/MAT-MT2/u7-loop-pair.svg]]

a) Loop 1 is a soft magnet, suited to transformer cores
b) Loop 2 is a soft magnet, with the lower coercivity
c) Loop 2 is a hard magnet, with the higher remanence
d) Loop 1 has the higher initial permeability

### Answer

b

### Explanation

Slide 18: a soft magnetic material has a narrow loop (low $H_c$, high initial permeability) and a hard one a wide loop (high $B_r$ and $H_c$). Loop 2 is the narrow one, so it is the soft magnet with the lower coercivity.

- a) Soft and hard swapped: loop 1 is the wide loop of a hard magnet, used for permanent magnets, not for transformer cores.
- c) Soft and hard swapped again: loop 2 crosses the B axis lower than loop 1, so its remanence is the lower one.
- d) The hard material has a low initial permeability (Slide 18); the high one belongs to the soft loop 2.

### Source

Session 15, Slides 17-19.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
