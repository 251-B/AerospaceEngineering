---
materia: Aerospace Materials I
tema: "Unit 4: non-equilibrium solidification, coring and the eutectic reaction"
bank_id: B06
title: "Coring and the eutectic reaction"
category: mt2_test_block
unit: 4
concepts:
  - u4-coring-cause
  - u4-nonequilibrium-solidus
  - u4-homogenisation
  - u4-eutectic-reaction
  - u4-eutectic-lines
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 7 Slides 23-27 and Session 8 Slide 6."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-4
---

# Bank B06 — Coring and the eutectic reaction

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 7, Slides 23-27; Session 8, Slide 6.

## Q06.1 Why fast cooling gives cored grains

- id: B06-Q1
- concept_id: u4-coring-cause
- format: cause-effect
- asks: cause

With a high cooling rate, the grains of a Cu-Ni casting have a cored structure because:

a) Solid-state diffusion has no time to even out the composition
b) Diffusion in the liquid stops completely
c) A eutectic forms at the grain boundaries
d) The equilibrium solidus moves to higher temperatures

### Answer

a

### Explanation

Session 7, Slide 23: when the alloy goes down through the diagram too quickly, diffusion in the solid has no time to keep the whole solid at the equilibrium composition; only the surface of each crystal has the solidus composition and the inside keeps the composition it had when it formed (microsegregation).

- b) The slide blames the slow diffusion in the solid, not in the liquid; the liquid keeps mixing.
- c) Cu-Ni is isomorphous and has no eutectic; coring is a composition gradient inside one phase.
- d) The equilibrium diagram does not change with the cooling rate; it is the average composition of the solid that follows a different (non-equilibrium) line.

### Source

Session 7, Slides 23-24.

## Q06.2 Meaning of a cored structure

- id: B06-Q2
- concept_id: u4-coring-cause
- format: complete-sentence
- asks: definition

A cored (microsegregated) structure consists of:

a) Grains made of two phases in alternating plates
b) A network of one phase around the former grains
c) Grains whose composition varies from centre to edge
d) Grains of uniform composition equal to the alloy

### Answer

c

### Explanation

Session 7, Slide 23: non-equilibrium solidification gives a microstructure of heterogeneous composition, microsegregation or cored structure; in Cu-35 wt% Ni the grains have 46 wt% Ni at the centre and 31 wt% Ni at the edge.

- a) Alternating plates of two phases describe a eutectic (or eutectoid) product, not coring.
- b) A network around former grains describes a proeutectoid phase such as cementite in steels.
- d) Uniform grains with the alloy composition are the result of equilibrium cooling (or of homogenisation), the opposite case.

### Source

Session 7, Slides 23-24.

## Q06.3 End of solidification with fast cooling

- id: B06-Q3
- concept_id: u4-nonequilibrium-solidus
- format: what-happens
- asks: effect

A Cu-35 wt% Ni alloy is cooled fast through the α + L region. What will happen to the end of its solidification:

a) It ends exactly on the equilibrium solidus
b) It ends above the equilibrium solidus
c) It ends at the liquidus temperature
d) It ends below the equilibrium solidus

### Answer

d

### Explanation

With fast cooling the average composition of the solid follows a non-equilibrium solidus that lies to the right of the equilibrium one, so liquid survives below the equilibrium solidus; in the slide example solidification ends at e′ instead of d′ (Session 7, Slide 23; Slide 24: at $T_7$ instead of $T_5$).

- a) Ending on the equilibrium solidus is the equilibrium (slow cooling) case.
- b) The trend is inverted: coring delays the end of solidification to lower temperatures, it does not advance it.
- c) At the liquidus solidification only starts; this confuses the start with the end.

### Source

Session 7, Slides 23-24.

## Q06.4 Liquid left with a cored solid

- id: B06-Q4
- concept_id: u4-nonequilibrium-solidus
- format: numeric
- asks: calculation
- calc: (42-35)/(42-29)*100

With fast cooling, at point c′ a Cu-35 wt% Ni alloy has liquid of 29 wt% Ni and cored α whose average composition is 42 wt% Ni. Determine the mass percentage of liquid:

a) 45.5 %
b) 46.2 %
c) 53.8 %
d) 83.3 %

### Answer

c

### Explanation

The tie line now ends on the non-equilibrium solidus, at the average composition of the solid (Session 7, Slide 23); the lever rule (Slide 16) gives $W_L = \dfrac{42 - 35}{42 - 29} = \dfrac{7}{13} = 0.538$.

- a) $(40 - 35)/(40 - 29) = 0.455$ uses the equilibrium solidus (40 wt% Ni at c′), which is the equilibrium answer, not the fast-cooling one.
- b) $(35 - 29)/(42 - 29) = 0.462$ is the fraction of α: the arms were swapped.
- d) $35/42 = 0.833$ is a ratio of compositions, not a lever.

### Source

Session 7, Slides 16 and 23 (c′: liquid 29 wt% Ni, average solid 42 wt% Ni).

## Q06.5 Removing the coring

- id: B06-Q5
- concept_id: u4-homogenisation
- format: identify
- asks: application

Which treatment removes the coring of a Cu-Ni casting:

a) Remelting and casting at a higher cooling rate
b) A homogenisation heat treatment below the solidus
c) A short heating above the liquidus
d) Cold working at room temperature

### Answer

b

### Explanation

Session 7, Slide 24: microsegregation is eliminated with a homogenisation heat treatment at a temperature below the solidus (below the lowest temperature at which liquid could exist); solid-state diffusion evens out the composition of the grains.

- a) A higher cooling rate leaves less time for diffusion and makes the coring worse.
- c) Heating above the liquidus melts the casting; on cooling again the same coring would form.
- d) At room temperature diffusion is too slow to change the composition, and cold work only deforms the grains.

### Source

Session 7, Slide 24.

## Q06.6 How homogenisation works

- id: B06-Q6
- concept_id: u4-homogenisation
- format: true-statement
- asks: cause

Which one of the following statements about the homogenisation of a cored alloy is TRUE:

a) It evens out the composition by solid-state diffusion
b) It must be done above the equilibrium solidus
c) It works by forming a eutectic between the grains
d) It needs a higher cooling rate than the casting

### Answer

a

### Explanation

Session 7, Slide 24: the treatment is done at $T_{TT}$ below the lowest temperature at which liquid could exist, and the solid-state diffusion of Topic 3 evens out the composition inside the grains.

- b) Above the solidus (and in a cored casting even somewhat below it) liquid would form; the slide places the treatment below that temperature.
- c) No new phase forms; the alloy stays a single solid solution that only changes its internal composition.
- d) The cooling rate is not the mechanism; time at high temperature for diffusion is.

### Source

Session 7, Slide 24.

## Q06.7 Equation of the eutectic reaction

- id: B06-Q7
- concept_id: u4-eutectic-reaction
- format: complete-sentence
- asks: definition

On cooling, the eutectic reaction of a binary system is:

a) α + L → β
b) γ → α + β
c) L₁ → L₂ + α
d) L → α + β

### Answer

d

### Explanation

Session 7, Slide 27 and Session 8, Slide 6: in the eutectic reaction a liquid transforms at a fixed temperature into two solids, $L \rightarrow \alpha + \beta$.

- a) α + L → β is the peritectic reaction (a solid and a liquid give a new solid).
- b) γ → α + β is the eutectoid reaction, the solid-state analogue with γ instead of L.
- c) L₁ → L₂ + α is the monotectic reaction, with a liquid miscibility gap.

### Source

Session 7, Slide 27; Session 8, Slide 6.

## Q06.8 Behaviour of the eutectic liquid

- id: B06-Q8
- concept_id: u4-eutectic-reaction
- format: true-statement
- asks: effect

Which one of the following statements about a liquid of eutectic composition is TRUE:

a) It first forms primary α and then β
b) It turns at one temperature into two solids
c) It solidifies over a range of temperatures
d) It turns into a single solid solution

### Answer

b

### Explanation

Session 7, Slide 26: a liquid of eutectic composition does not pass through a two-phase L + solid region; at the eutectic temperature it transforms at once into two solids, α and β, in a fine structure of alternating layers.

- a) Primary α followed by eutectic is the path of a hypoeutectic alloy, not of the eutectic one.
- c) A solidification range belongs to non-eutectic alloys; the eutectic reaction is invariant ($F = 0$).
- d) The eutectic product contains two phases, α and β, not one solid solution.

### Source

Session 7, Slides 26-27.

## Q06.9 Line of maximum solid solubility

- id: B06-Q9
- concept_id: u4-eutectic-lines
- format: identify
- asks: definition

In a binary eutectic diagram, which line gives the maximum solubility of B in α at each temperature in the solid state:

a) Liquidus
b) Solidus
c) Eutectic isotherm
d) Solvus

### Answer

d

### Explanation

Session 7, Slide 26: the solvus gives the maximum solubility of B in α (and of A in β) at each temperature in the solid state.

- a) The liquidus bounds the liquid region; above it everything is liquid.
- b) The solidus is the line below which there is no liquid; it limits α against α + L, not against α + β.
- c) The eutectic isotherm is the horizontal line of the eutectic reaction at a single temperature, not a line valid at each temperature.

### Source

Session 7, Slide 26.

## Q06.10 Maximum solubility of B in alpha

- id: B06-Q10
- concept_id: u4-eutectic-lines
- format: diagram-reading
- asks: figure-reading

From the shown A-B phase diagram, indicate the maximum solubility of B in α and the temperature at which it occurs:

![[attachments/MAT-MT2/u4-eut-ab.svg]]

a) 15 wt% B at 450 °C
b) 60 wt% B at 450 °C
c) 15 wt% B at 800 °C
d) 90 wt% B at 450 °C

### Answer

a

### Explanation

The α field is widest at the eutectic temperature: the solidus and the solvus of α meet at 15 wt% B and 450 °C, the left end of the eutectic line (Session 7, Slide 26).

- b) 60 wt% B is the eutectic composition, a point of the liquid, not a limit of α.
- c) 800 °C is the melting point of pure A, where α holds no B at all; the right composition is paired with the wrong temperature.
- d) 90 wt% B is the limit of β at 450 °C, the neighbouring phase.

### Source

Session 7, Slide 26.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
