---
materia: Aerospace Materials I
tema: "Unit 4: isomorphous systems, cooling curves and the Gibbs phase rule"
bank_id: B03
title: "Isomorphous systems and the Gibbs phase rule"
category: mt2_test_block
unit: 4
concepts:
  - u4-iso-microstructure
  - u4-liquidus-solidus
  - u4-complete-solubility
  - u4-gibbs-rule-unary
  - u4-gibbs-rule-binary
  - u4-gibbs-invariant
  - u4-cooling-curves
difficulty: 1
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 7 Slides 8-13, 23 and 27 and Session 10 Slide 2."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-4
---

# Bank B03 — Isomorphous systems and the Gibbs phase rule

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 7, Slides 8-13, 23 and 27; Session 10, Slide 2.

## Q03.1 Between liquidus and solidus

- id: B03-Q1
- concept_id: u4-iso-microstructure
- format: complete-sentence
- asks: classification

At a temperature between the liquidus and the solidus, a Cu-Ni alloy consists of:

a) Liquid only
b) Crystals of solid solution in a liquid matrix
c) Two different solid solutions
d) A polycrystalline single solid solution

### Answer

b

### Explanation

Session 7, Slide 10: at a temperature $T_1$ between the liquidus and the solidus the microstructure is crystallites of the solid solution SS₁ in a matrix of liquid L₁, whose compositions are read on the solidus and the liquidus.

- a) Liquid only is the state above the liquidus; between the two lines solid has already formed.
- c) Two solid solutions need limited solubility (a eutectic system); Cu-Ni has complete solid solubility and a single solid phase.
- d) A single-phase polycrystal is the state below the solidus, when the last liquid has disappeared.

### Source

Session 7, Slides 10-11.

## Q03.2 Composition of the solid during slow cooling

- id: B03-Q2
- concept_id: u4-iso-microstructure
- format: what-happens
- asks: effect

A Cu-35 wt% Ni alloy is cooled very slowly (equilibrium) from the liquid to below its solidus. What will happen to the composition of the solid that forms:

a) It follows the solidus and ends at 35 wt% Ni
b) It keeps the composition of the first solid formed
c) It follows the liquidus and ends richer in Ni
d) It equals 35 wt% Ni from the very beginning

### Answer

a

### Explanation

In equilibrium the solid follows the solidus and the liquid follows the liquidus as the temperature falls (Session 7, Slide 23): the first solid has 46 wt% Ni (b′), it becomes poorer in Ni (40 wt% at c′), and at the solidus (d′) it reaches the alloy composition, 35 wt% Ni, when the last liquid disappears.

- b) Keeping the composition of the first solid is what happens inside the grains with fast cooling (coring), not in equilibrium.
- c) The liquidus gives the composition of the liquid, not of the solid; and both phases become poorer in Ni on cooling.
- d) The first solid is richer in Ni (46 wt%) than the alloy; it reaches 35 wt% only at the solidus.

### Source

Session 7, Slides 10 and 23.

## Q03.3 Solidification range from the diagram

- id: B03-Q3
- concept_id: u4-liquidus-solidus
- format: numeric
- asks: calculation
- calc: 1250-1140

Determine the width of the solidification interval of the alloy marked $C_0$ on the isomorphous diagram below:

![[attachments/MAT-MT2/u4-iso-ab.svg]]

a) 50 °C
b) 60 °C
c) 110 °C
d) 250 °C

### Answer

c

### Explanation

The alloy starts to solidify on the liquidus (1250 °C) and ends on the solidus (1140 °C) (Session 7, Slides 9-11), so the range is $1250 - 1140 = 110$ °C.

- a) $1250 - 1200 = 50$ °C uses the temperature of the drawn tie line as the end of solidification instead of the solidus.
- b) $1200 - 1140 = 60$ °C again takes the tie line, this time as the start of solidification instead of the liquidus.
- d) $1250 - 1000 = 250$ °C takes the melting point of pure A as the end of solidification instead of reading the solidus on the alloy line.

### Source

Session 7, Slides 9-11.

## Q03.4 Same lattice as the pure metal

- id: B03-Q4
- concept_id: u4-complete-solubility
- format: cause-effect
- asks: cause

A Cu-Ni solid solution has the same crystal structure as pure copper because:

a) Ni atoms sit in the interstitial sites of the Cu lattice
b) Ni precipitates as separate particles with its own lattice
c) Cu and Ni have very different crystal structures
d) Ni atoms replace Cu atoms in the same lattice

### Answer

d

### Explanation

Session 7, Slide 11: with complete solid solubility the material is a polycrystalline single-phase material whose structure is not different from that of the pure metal, because the atoms of B simply replace atoms of A in the same lattice.

- a) Interstitial solid solutions, such as C in Fe, hold only small amounts of solute; complete solubility needs substitution of one atom for the other.
- b) Separate particles would be another phase, and the alloy would no longer be a single solid solution.
- c) Very different structures would prevent complete solubility; the slide describes the solute entering the same lattice.

### Source

Session 7, Slide 11.

## Q03.5 A wrong statement about Al2O3-Cr2O3

- id: B03-Q5
- concept_id: u4-complete-solubility
- format: false-statement
- asks: classification

Which one of the following statements about the Al₂O₃-Cr₂O₃ system is FALSE:

a) It forms a complete solid solution below the solidus
b) Its diagram has the lens shape of an isomorphous system
c) Every composition solidifies at a single temperature
d) Below 950 °C two solid solutions exist (immiscibility)

### Answer

c

### Explanation

Statement c) is false: Al₂O₃-Cr₂O₃ is isomorphous (Session 10, Slide 2), so its alloys solidify over a range between the liquidus and the solidus; only the two pure oxides solidify at one temperature (Session 7, Slide 11).

- a) True: the slide describes a complete interval of solid solution, Al₂₋ₓCrₓO₃, below the solidus.
- b) True: the diagram has the lens shape of a binary isomorphous system.
- d) True: below 950 °C the slide shows immiscibility, with two crystalline phases.

### Source

Session 10, Slide 2; Session 7, Slide 11.

## Q03.6 Degrees of freedom on a melting line

- id: B03-Q6
- concept_id: u4-gibbs-rule-unary
- format: numeric
- asks: calculation
- calc: 1-2+2

Determine the degrees of freedom of a pure substance at a point of its melting line, with pressure and temperature both free:

a) 0
b) 1
c) 2
d) 3

### Answer

b

### Explanation

Gibbs phase rule with $N = 2$ (Session 7, Slide 13): one component and two phases (solid and liquid) on the line, so $F = C - P + 2 = 1 - 2 + 2 = 1$. If the temperature is chosen, the line fixes the pressure.

- a) $F = 0$ is the triple point, where three phases coexist ($1 - 3 + 2$).
- c) $F = 2$ is a point inside a single-phase region ($1 - 1 + 2$).
- d) $F = 3$ comes from adding the number of phases instead of subtracting it ($1 + 2 + 2 - 2$): a wrong sign in the rule.

### Source

Session 7, Slide 13.

## Q03.7 Meaning of N in the phase rule

- id: B03-Q7
- concept_id: u4-gibbs-rule-binary
- format: complete-sentence
- asks: definition

In the Gibbs phase rule $F = C - P + N$, the term $N$ is the number of:

a) Phases in equilibrium
b) Components of the system
c) Degrees of freedom left to the system
d) Non-compositional variables, such as P and T

### Answer

d

### Explanation

Session 7, Slide 13: $N$ is the number of non-compositional variables (pressure and temperature, $N = 2$); with the pressure fixed at 1 atm, $N = 1$ and $F = C - P + 1$.

- a) The number of phases is $P$, the term that is subtracted.
- b) The number of components is $C$.
- c) The degrees of freedom are $F$, the result of the rule, not one of its terms.

### Source

Session 7, Slide 13.

## Q03.8 Why the eutectic temperature is fixed

- id: B03-Q8
- concept_id: u4-gibbs-invariant
- format: cause-effect
- asks: cause

At 1 atm, the eutectic reaction of a binary alloy takes place at one fixed temperature because:

a) Three phases coexist, so $F = 0$
b) Two phases coexist, so $F = 1$
c) The eutectic alloy is a pure component
d) No heat is released by the reaction

### Answer

a

### Explanation

At the eutectic point L, α and β coexist in a two-component system at constant pressure: $F = 2 - 3 + 1 = 0$ (Session 7, Slides 13 and 27). Temperature and the compositions of the three phases are all fixed, so the reaction is invariant and the cooling curve shows a plateau.

- b) With two phases $F = 1$ and the alloy would transform over a range of temperatures, as in L + α.
- c) The eutectic alloy has two components; it behaves like a pure metal only because three phases coexist.
- d) Heat is released by the reaction; it is that latent heat that keeps the temperature constant on the plateau.

### Source

Session 7, Slides 13 and 27.

## Q03.9 Degrees of freedom read on a diagram

- id: B03-Q9
- concept_id: u4-gibbs-rule-binary
- format: diagram-reading
- asks: figure-reading

From the shown A-B phase diagram at constant pressure, indicate the degrees of freedom of the 30 wt% B alloy at 550 °C:

![[attachments/MAT-MT2/u4-eut-ab.svg]]

a) F = 0
b) F = 1
c) F = 2
d) F = 3

### Answer

b

### Explanation

At 30 wt% B and 550 °C the point lies below the liquidus (650 °C at 30 wt% B) and inside α + L. With two components and two phases at constant pressure, $F = C - P + 1 = 2 - 2 + 1 = 1$ (Session 7, Slide 13).

- a) $F = 0$ holds only on the eutectic line at 450 °C, where L, α and β coexist.
- c) $F = 2$ is the value inside a single-phase field (L, α or β), not in α + L.
- d) $F = 3$ uses $N = 2$ and one phase, ignoring both the fixed pressure and the liquid present.

### Source

Session 7, Slides 13 and 26.

## Q03.10 Experiment that gives the liquidus

- id: B03-Q10
- concept_id: u4-cooling-curves
- format: identify
- asks: application

Which procedure is used to find the liquidus and solidus temperatures of the alloys of a binary system:

a) Applying the Gibbs phase rule to each alloy
b) Applying the lever rule at each temperature
c) Recording cooling curves of several compositions
d) Measuring tie lines on micrographs

### Answer

c

### Explanation

Session 7, Slides 8-9: the temperature of each cooling alloy is recorded against time; the changes of slope give the start and the end of solidification, and joining them over several compositions gives the liquidus and the solidus.

- a) The phase rule counts degrees of freedom; it gives no temperatures.
- b) The lever rule needs the diagram already drawn: it gives amounts of phases, not the boundaries.
- d) Tie lines are constructions on an existing diagram, not measurements on micrographs.

### Source

Session 7, Slides 8-9.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
