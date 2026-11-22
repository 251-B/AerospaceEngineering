---
materia: Aerospace Materials I
tema: "Unit 4: hypoeutectoid and hypereutectoid steels, proeutectoid phases and pearlite"
bank_id: B14
title: "Steel microstructures and amounts"
category: mt2_test_block
unit: 4
concepts:
  - u4-hypereutectoid-microstructure
  - u4-hypoeutectoid-microstructure
  - u4-proeutectoid-ferrite-amount
  - u4-proeutectoid-cementite-amount
  - u4-steel-carbon-from-microstructure
  - u4-pearlite-composition
difficulty: 2
origen: "Includes official exam question Q6 of MATERIALS_SECONDPARTIAL_2019.pdf (p. 3); other questions written for the bank in the style of Part I of Assessment Test II. Data from Session 9 Slides 4 and 10-20 (0.022, 0.76 and 6.67 wt% C at 727 °C)."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-4
---

# Bank B14 — Steel microstructures and amounts

> [!info] Includes official exam questions
> Ten test questions in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong); Q14.1 is Question 6 from `MATERIALS_SECONDPARTIAL_2019.pdf`. Content: Session 9, Slides 4 and 10-20; values of the diagram: α 0.022, eutectoid 0.76 and Fe₃C 6.67 wt% C at 727 °C.

## Q14.1 Microstructure of a 0.5 C steel

- id: B14-Q1
- concept_id: u4-hypoeutectoid-microstructure
- format: complete-sentence
- asks: classification
- origin: official-exam

Microstructure of steel with 0.5 wt% C below 727 °C consists of:

a) Pearlite matrix with proeutectoid austenite
b) Pearlite matrix with proeutectoid ferrite
c) Austenite matrix with proeutectoid ferrite
d) Austenite matrix with proeutectoid cementite

### Answer

b

### Explanation

0.5 wt% C is below the eutectoid composition (0.76 wt% C): a hypoeutectoid steel (Session 9, Slides 4 and 14). On cooling across $A_3$, proeutectoid ferrite precipitates first; at 727 °C the remaining austenite (0.76 wt% C) transforms into pearlite, giving a pearlite matrix with proeutectoid ferrite.

- a) Austenite does not survive below 727 °C in the Fe-Fe₃C diagram and cannot be a proeutectoid constituent here.
- c) Austenite transforms into pearlite at 727 °C, so the matrix below 727 °C is pearlite rather than austenite.
- d) Both parts are wrong: austenite is unstable below 727 °C, and proeutectoid cementite occurs only in hypereutectoid steels (above 0.76 wt% C).

### Source

MATERIALS_SECONDPARTIAL_2019.pdf, p. 3 (Part I, Q6); Session 9, Slides 4 and 14-18.

## Q14.2 Picture of a slowly cooled 1.4 C steel

- id: B14-Q2
- concept_id: u4-hypereutectoid-microstructure
- format: choose-figure
- asks: figure-reading

A steel with 1.4 wt% C has been cooled slowly to room temperature and polished. Which of the sketches of its microstructure is the right one?

a) ![[attachments/MAT-MT2/u4-steel-a.svg]]
b) ![[attachments/MAT-MT2/u4-steel-b.svg]]
c) ![[attachments/MAT-MT2/u4-steel-c.svg]]
d) ![[attachments/MAT-MT2/u4-steel-d.svg]]

### Answer

c

### Explanation

A hypereutectoid steel is pearlite surrounded by proeutectoid cementite, which forms a network along the boundaries of the former austenite grains (Session 9, Slides 19-20). Structure C shows pearlite colonies outlined by thick boundaries.

- a) Structure A is pearlite only, with thin boundaries: the eutectoid steel (0.76 wt% C).
- b) Structure B mixes plain grains and pearlite: proeutectoid ferrite with pearlite, a hypoeutectoid steel.
- d) Structure D shows only plain grains: ferrite, a steel with almost no carbon.

### Source

Session 9, Slides 12, 14 and 19-20.

## Q14.3 Austenite of a 0.4 C steel at 727 °C

- id: B14-Q3
- concept_id: u4-hypoeutectoid-microstructure
- format: what-happens
- asks: effect

A 0.4 wt% C steel held in α + γ at 760 °C is cooled to just below 727 °C. What will happen to the austenite that is left:

a) It turns into proeutectoid ferrite
b) It stays as austenite at room temperature
c) It forms a network of proeutectoid cementite
d) It transforms into pearlite

### Answer

d

### Explanation

While the steel cools from $A_3$ to 727 °C, ferrite grows and the austenite becomes richer in carbon along $A_3$; at 727 °C the remaining austenite has 0.76 wt% C and becomes pearlite through the eutectoid reaction (Session 9, Slides 14-18).

- a) Proeutectoid ferrite forms above 727 °C; at 727 °C the austenite left is eutectoid and gives pearlite, not more primary ferrite.
- b) Austenite is not stable below 727 °C in the Fe-Fe₃C diagram.
- c) Proeutectoid cementite belongs to hypereutectoid steels, which cross $A_{cm}$.

### Source

Session 9, Slides 14-18.

## Q14.4 Proeutectoid ferrite in a 0.4 C steel

- id: B14-Q4
- concept_id: u4-proeutectoid-ferrite-amount
- format: numeric
- asks: calculation
- calc: (0.76-0.4)/(0.76-0.022)*100

Determine the mass percentage of proeutectoid ferrite in a 0.4 wt% C steel just below 727 °C:

a) 5.69 %
b) 48.8 %
c) 51.2 %
d) 94.3 %

### Answer

b

### Explanation

Microconstituents use the short tie line from α (0.022) to the eutectoid (0.76 wt% C) (Session 9, Slides 17-18): $W_{\alpha_p} = \dfrac{0.76 - 0.4}{0.76 - 0.022} = \dfrac{0.36}{0.738} = 0.488$.

- a) $(0.4 - 0.022)/(6.67 - 0.022) = 0.0569$ is the total cementite, a phase on the long tie line.
- c) $(0.4 - 0.022)/0.738 = 0.512$ is the pearlite: arms swapped.
- d) $(6.67 - 0.4)/6.648 = 0.943$ is the total ferrite, proeutectoid plus eutectoid.

### Source

Session 9, Slides 4 and 17-18.

## Q14.5 Pearlite fraction limits in steels

- id: B14-Q5
- concept_id: u4-pearlite-composition
- format: topic-true
- asks: application

Regarding the microconstituents of slowly cooled plain-carbon steels below 727 °C, which statement is TRUE:

a) A 1.0 wt% C hypereutectoid steel contains more proeutectoid cementite than pearlite
b) Proeutectoid ferrite appears in slowly cooled steels from 0.022 up to 2.14 wt% C
c) A eutectoid steel contains 89 % pearlite and 11 % proeutectoid cementite
d) The pearlite mass fraction reaches 100 % at 0.76 wt% C and is zero at or below 0.022 wt% C

### Answer

d

### Explanation

Session 9, Slides 12-20 and Problems T4_PhaseDiagrams II.pdf (Q10b): at 0.76 wt% C the steel is 100 % pearlite (maximum pearlite content), while at or below the ferrite solubility limit (0.022 wt% C at 727 °C) the steel never reaches the eutectoid line and contains 100 % ferrite with 0 % pearlite (minimum pearlite content).

- a) At 1.0 wt% C, $W_{\text{Fe}_3\text{C},p} = (1.0 - 0.76)/(6.67 - 0.76) \approx 4.1$ %, whereas pearlite makes up 95.9 % of the mass.
- b) Proeutectoid ferrite forms only in hypoeutectoid steels (below 0.76 wt% C); between 0.76 and 2.14 wt% C the proeutectoid phase is cementite.
- c) 89 % and 11 % are the mass percentages of the ferrite and cementite **phases** inside pearlite, not separate microconstituents; a eutectoid steel is 100 % pearlite.

### Source

Session 9, Slides 12-20; Problems T4_PhaseDiagrams II.pdf, Q10b.

## Q14.6 Carbon content from the pearlite

- id: B14-Q6
- concept_id: u4-steel-carbon-from-microstructure
- format: numeric
- asks: calculation
- calc: 0.022+0.25*(0.76-0.022)

A slowly cooled hypoeutectoid steel contains 25 % pearlite and 75 % proeutectoid ferrite. Determine its carbon content:

a) 0.190 wt% C
b) 0.207 wt% C
c) 0.576 wt% C
d) 1.68 wt% C

### Answer

b

### Explanation

$W_{\text{pearlite}} = (C_0 - 0.022)/(0.76 - 0.022)$ (Session 9, Slides 17-18) solved for $C_0$: $C_0 = 0.022 + 0.25 \times 0.738 = 0.207$ wt% C.

- a) $0.25 \times 0.76 = 0.190$ forgets the 0.022 wt% C of the ferrite end of the tie line.
- c) $0.76 - 0.25 \times 0.738 = 0.576$ treats 25 % as the proeutectoid ferrite: arms swapped.
- d) $0.022 + 0.25 \times 6.648 = 1.68$ uses the α-Fe₃C tie line, which gives cementite, not pearlite.

### Source

Session 9, Slides 17-18.

## Q14.7 Make-up of pearlite

- id: B14-Q7
- concept_id: u4-pearlite-composition
- format: true-statement
- asks: definition

Which one of the following statements about pearlite is TRUE:

a) Its ferrite and cementite proportions depend on the carbon of the steel
b) It is a single phase of 0.76 wt% C
c) It is 50 % ferrite and 50 % cementite
d) It is about 89 % ferrite and 11 % cementite in any steel

### Answer

d

### Explanation

Pearlite forms from austenite of 0.76 wt% C on the tie line from 0.022 to 6.67 wt% C (Session 9, Slides 10 and 12-13): $W_\alpha = (6.67 - 0.76)/(6.67 - 0.022) = 0.889$ and $W_{\text{Fe}_3\text{C}} = 0.111$, the same in every steel.

- a) The carbon of the steel changes how much pearlite there is, not what pearlite is made of.
- b) Pearlite is a microconstituent of two phases, ferrite and cementite, in lamellae.
- c) Equal amounts ignore the lever rule; the eutectoid point is much closer to ferrite than to cementite.

### Source

Session 9, Slides 10 and 12-13.

## Q14.8 Where proeutectoid ferrite starts

- id: B14-Q8
- concept_id: u4-hypoeutectoid-microstructure
- format: identify
- asks: definition

When a hypoeutectoid steel crosses the $A_3$ line on cooling, the proeutectoid ferrite nucleates at:

a) The grain boundaries of the austenite
b) The centre of the cementite plates
c) The interfaces of the pearlite lamellae
d) The surface of the liquid

### Answer

a

### Explanation

Session 9, Slides 14-15: between $A_3$ and 727 °C, ferrite nucleates at the grain boundaries of the austenite and grows, while the austenite becomes richer in carbon.

- b) No cementite exists in a hypoeutectoid steel above 727 °C; it appears only inside pearlite.
- c) Pearlite forms later, at 727 °C, from the remaining austenite; the proeutectoid ferrite forms before it.
- d) The steel is fully solid (austenite) at $A_3$; no liquid is involved.

### Source

Session 9, Slides 14-15.

## Q14.9 A wrong claim about a 1.0 C steel

- id: B14-Q9
- concept_id: u4-proeutectoid-cementite-amount
- format: false-statement
- asks: classification

Which one of the following statements about a slowly cooled 1.0 wt% C steel below 727 °C is FALSE:

a) Its microconstituents are pearlite and proeutectoid cementite
b) Its proeutectoid cementite outlines the former austenite grains
c) Its phases are ferrite and cementite
d) It contains proeutectoid ferrite

### Answer

d

### Explanation

Statement d) is false: a 1.0 wt% C steel is hypereutectoid; it crosses $A_{cm}$, not $A_3$, so its proeutectoid phase is cementite and it has no proeutectoid ferrite (Session 9, Slides 19-20).

- a) True: proeutectoid cementite plus pearlite (Slide 19).
- b) True: the proeutectoid cementite forms a network along the boundaries of the former austenite grains.
- c) True: below 727 °C every Fe-C alloy is α + Fe₃C (Slide 9).

### Source

Session 9, Slides 9 and 19-20.

## Q14.10 Proeutectoid ferrite and carbon content

- id: B14-Q10
- concept_id: u4-proeutectoid-ferrite-amount
- format: cause-effect
- asks: effect

With an increase in carbon content from 0.1 to 0.76 wt%, the fraction of proeutectoid ferrite in slowly cooled steels:

a) Increases, reaching 100 % at 0.76 wt% C
b) Stays constant at about 89 %
c) Decreases, reaching zero at 0.76 wt% C
d) Decreases, reaching 11 % at 0.76 wt% C

### Answer

c

### Explanation

$W_{\alpha_p} = (0.76 - C_0)/(0.76 - 0.022)$ (Session 9, Slides 17-18): it falls as $C_0$ grows and is zero at the eutectoid composition, where the steel is all pearlite (Slide 12).

- a) Inverted trend: more carbon means more pearlite and less proeutectoid ferrite.
- b) 89 % is the ferrite inside pearlite, a fixed make-up, not the proeutectoid fraction.
- d) Right trend, wrong limit: 11 % is the cementite inside pearlite; the proeutectoid ferrite reaches zero.

### Source

Session 9, Slides 12-18.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
