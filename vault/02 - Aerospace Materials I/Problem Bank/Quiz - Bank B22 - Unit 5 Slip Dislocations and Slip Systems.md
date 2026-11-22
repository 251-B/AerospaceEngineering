---
materia: Aerospace Materials I
tema: "Unit 5: slip of dislocations, the direction of slip and the slip systems"
bank_id: B22
title: "Slip, dislocations and slip systems"
category: mt2_test_block
unit: 5
concepts:
  - u5-dislocation-slip-energy
  - u5-slip-direction-packing
  - u5-slip-systems-structures
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 11, Slides 23-25 and Session 12, Slides 2-3."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-5
---

# Bank B22 — Slip, dislocations and slip systems

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 11, Slides 23-25 and Session 12, Slides 2-3.

## Q22.1 Energy to move a dislocation

- id: B22-Q1
- concept_id: u5-dislocation-slip-energy
- format: complete-sentence
- asks: definition

The energy needed to move a dislocation is proportional to:

a) the distance between neighbouring slip planes
b) the square of the Burgers vector magnitude
c) the Burgers vector magnitude, not squared
d) the number of slip systems of the crystal

### Answer

b

### Explanation

Session 11, Slide 24: "E used to move a dislocation $\propto |\vec b|^2$", so FCC [110] with $b = 2R$ gives $E_b \propto 4R^2$ and FCC [100] with $b = 2\sqrt2\,R$ gives $E_b \propto 8R^2$.

- a) A larger distance between planes makes slip easier, not harder; the slide links it to a lower force between planes.
- c) The slide writes $E \propto |\vec b|^2$; dropping the square halves the contrast between compact and non-compact directions.
- d) The number of slip systems tells how many ways a crystal can slip, not the energy of one dislocation.

### Source

Session 11, Slide 24.

## Q22.2 Energy comparison of two slip directions in FCC

- id: B22-Q2
- concept_id: u5-dislocation-slip-energy
- format: topic-true
- asks: comparison

Referring to dislocation slip energy ($E_{\text{slip}} \propto |\vec b|^2$), compare moving a dislocation along the close-packed $[110]$ direction ($b = 2R$) versus the $[100]$ direction ($b = 2\sqrt{2}\,R$) in an FCC crystal. Which statement is TRUE?

a) Slip along $[100]$ requires half as much energy as along $[110]$
b) Both directions require the same energy because the atomic radius $R$ is identical
c) Slip along $[100]$ requires twice as much energy as along $[110]$
d) Slip along $[100]$ requires four times as much energy as along $[110]$

### Answer

c

### Explanation

Session 11, Slide 24: the energy needed to move a dislocation scales as $|\vec b|^2$, with $b_{[110]} = 2R$ ($E \propto 4R^2$) and $b_{[100]} = 2\sqrt{2}\,R$ ($E \propto 8R^2$). The ratio is $8R^2/(4R^2) = 2$, so $[100]$ requires twice as much energy.

- a) Inverted ratio: the shorter Burgers vector $[110]$ has the lower energy, not $[100]$.
- b) Even with the same atomic radius $R$, the step length $|\vec b|$ differs along different crystallographic directions.
- d) This squares the Burgers vector ratio twice: $(2\sqrt{2}/2)^4 = 4$.

### Source

Session 11, Slide 24.

## Q22.3 Slip with and without dislocations

- id: B22-Q3
- concept_id: u5-dislocation-slip-energy
- format: false-statement
- asks: definition

Which one of the following statements about slip in crystals is FALSE?

a) Plastic deformation is the movement of many dislocations
b) Slip with dislocations needs more energy than without them
c) A slip system is a slip plane plus a slip direction
d) A moving dislocation breaks and re-forms bonds sequentially

### Answer

b

### Explanation

Session 11, Slide 23: without dislocations, several bonds must break at the same time; with dislocations the process is sequential, so the energy consumed is lower and the atoms glide under relatively low forces.

- a) This is true: Session 12, Slide 2.
- c) This is true: it is the definition of Slide 23.
- d) This is true: Slide 23 states that with dislocations "the breakage and formation of bonds is sequential".

### Source

Session 11, Slide 23; Session 12, Slide 2.

## Q22.4 Why slip follows the densest direction

- id: B22-Q4
- concept_id: u5-slip-direction-packing
- format: complete-sentence
- asks: cause

Dislocations move parallel to the direction of maximum packing because there:

a) the planes are further apart and attract each other less
b) the Burgers vector has its largest possible length
c) the planes are closer together and attract each other more
d) the bonds between atoms break all at the same time

### Answer

a

### Explanation

Session 11, Slide 24: "dislocation movement is parallel to the direction of maximum packing → higher distance between planes → lower $F_{\text{atr}}$ between them → easier slipping".

- b) The compact direction gives the shortest Burgers vector ($2R$ in FCC), which is why its energy is the lowest.
- c) Both features are inverted: closer, more strongly attracted planes would make slip harder.
- d) Simultaneous breaking is the high-energy case without dislocations; dislocations break bonds one after another.

### Source

Session 11, Slides 23-24.

## Q22.5 Compact slip direction of FCC

- id: B22-Q5
- concept_id: u5-slip-direction-packing
- format: identify
- asks: classification

Which crystallographic direction family is the primary slip direction of FCC metals?

a) $\langle 110\rangle$
b) $\langle 100\rangle$
c) $\{111\}$
d) $\langle 111\rangle$

### Answer

a

### Explanation

Session 11, Slide 25: FCC slips on $\{111\}$ planes along $\langle\bar110\rangle$ directions, $4 \times 3 = 12$ systems; Slide 24 shows $[110]$ as the compact direction with $b = 2R$.

- b) $\langle 100\rangle$ is the non-compact direction of Slide 24, with a Burgers vector $2\sqrt2 R$ and twice the energy.
- c) $\{111\}$ is the FCC slip plane family, not its slip direction.
- d) $\langle 111\rangle$ is the slip direction family of BCC metals, not of FCC.

### Source

Session 11, Slides 24-25.

## Q22.6 Slip direction and interplanar packing

- id: B22-Q6
- concept_id: u5-slip-direction-packing
- format: topic-false
- asks: comparison

Regarding dislocation glide and slip directions in crystalline metals, which statement is FALSE?

a) Slip occurs preferentially along directions of maximum linear atomic packing
b) Dislocations favour slip directions with the longest Burgers vector and smallest interplanar spacing
c) Along the close-packed FCC $[110]$ direction, the Burgers vector magnitude is $2R$
d) Greater spacing between slip planes lowers the attractive force between them and eases slip

### Answer

b

### Explanation

Session 11, Slide 24: dislocations move along the direction of maximum packing, which has the shortest Burgers vector (minimizing $E \propto |\vec b|^2$) and the largest spacing between planes (minimizing attractive forces across the plane).

- a) This is true: dislocation motion is parallel to the direction of maximum packing (Slide 24).
- c) This is true: along the face diagonal $[110]$ of FCC, touching atoms are $2R$ apart (Slide 24).
- d) This is true: larger interplanar spacing lowers the attractive force between neighbouring planes and makes slip easier.

### Source

Session 11, Slide 24.

## Q22.7 What a slip system is

- id: B22-Q7
- concept_id: u5-slip-systems-structures
- format: complete-sentence
- asks: definition

In crystal plasticity, a slip system consists of:

a) a family of grain boundaries
b) a set of parallel dislocations in a grain
c) a slip plane alone, the densest one
d) a slip plane together with a slip direction

### Answer

d

### Explanation

Session 11, Slide 23: "slip system: slip plane + slip direction"; Slide 25 lists the planes and directions of BCC, FCC and HCP.

- a) Grain boundaries are obstacles to slip (Session 12, Slide 10), not where it takes place.
- b) Dislocations move on slip systems, but they are defects, not the system itself.
- c) A plane alone is not enough: slip happens along a given direction inside the plane.

### Source

Session 11, Slides 23 and 25; Session 12, Slide 10.

## Q22.8 Number of slip systems

- id: B22-Q8
- concept_id: u5-slip-systems-structures
- format: complete-sentence
- asks: classification

Considering the primary $\{110\}$, $\{111\}$ and basal $(0001)$ slip planes, the numbers of slip systems in BCC, FCC and HCP metals are, in that order:

a) 6, 12 and 12
b) 12, 6 and 6
c) 12, 12 and 6
d) 12, 12 and 12

### Answer

c

### Explanation

Session 11, Slide 25: BCC $\{110\}$ $6 \times 2 = 12$; FCC $\{111\}$ $4 \times 3 = 12$; HCP $(0001)$ $2 \times 3 = 6$.

- a) BCC and HCP were swapped: BCC has $6 \times 2 = 12$ systems.
- b) FCC was given the value of HCP: FCC has $4 \times 3 = 12$ systems.
- d) HCP has only $2 \times 3 = 6$ primary systems on its basal plane, half of the cubic structures.

### Source

Session 11, Slide 25.

## Q22.9 Metal with six slip systems

- id: B22-Q9
- concept_id: u5-slip-systems-structures
- format: identify
- asks: application

Which of the following metals has an HCP crystal structure with only six primary slip systems?

a) Nickel
b) Alpha iron
c) Aluminium
d) Magnesium

### Answer

d

### Explanation

Session 11, Slide 25: the HCP examples are Cd, Mg, $\alpha$-Ti and Zn, with $2 \times 3 = 6$ slip systems; Al, Cu, $\gamma$-Fe and Ni are FCC and $\alpha$-Fe, Mo and W are BCC.

- a) Nickel is FCC, with 12 slip systems.
- b) $\alpha$-Fe is BCC, with 12 slip systems.
- c) Aluminium is FCC, with 12 slip systems.

### Source

Session 11, Slide 25.

## Q22.10 Slip planes of cubic metals

- id: B22-Q10
- concept_id: u5-slip-systems-structures
- format: true-statement
- asks: comparison

Which one of the following statements about slip systems in crystalline metals is TRUE?

a) BCC metals slip on $\{111\}$ planes
b) Slip occurs on any plane, whatever the structure
c) HCP metals have twelve slip systems
d) FCC metals slip on $\{111\}$ planes

### Answer

d

### Explanation

Session 11, Slide 25: FCC $\{111\}\langle\bar110\rangle$, 12 systems; BCC $\{110\}\langle\bar111\rangle$, 12 systems; HCP (0001), 6 systems.

- a) BCC metals slip on $\{110\}$ planes; $\{111\}$ are the FCC slip planes.
- b) Slip "occurs along specific crystallographic planes that depend on the structure" (Slide 25).
- c) HCP has 6 slip systems, half of BCC and FCC.

### Source

Session 11, Slide 25.
