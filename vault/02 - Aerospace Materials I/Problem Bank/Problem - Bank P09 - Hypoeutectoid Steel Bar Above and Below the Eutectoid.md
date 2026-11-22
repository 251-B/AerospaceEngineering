---
materia: Aerospace Materials I
tema: "Unit 4: the Fe-Fe3C diagram and steels"
bank_id: P09
title: "Hypoeutectoid steel bar above and below the eutectoid temperature"
category: mt2_problem
archetype: fe-c-steels
level: standard
unit: 4
difficulty: 2
points: 3.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of the finals of 2017 (extraordinary, question 4) and 2016 (extraordinary, question 4), MATERIALS_FINALEXAM_2017_EXTRA.pdf and MATERIALS_FINALEXAM_2016_EXTRA_SOL.pdf, and of January 2013 (question 5) in MATERIALS_FINALEXAM_COMPILATION_2013-2017.pdf; not an official exercise. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - fe-c-steels
  - hypoeutectoid
  - lever-rule
---

# Bank P09 — Hypoeutectoid steel bar above and below the eutectoid temperature

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Fe-C questions of the finals (a bar of steel in kg, phases just above and just below 727 °C, proeutectoid and eutectoid ferrite). Method: Session 9, Slides 4, 10 and 14-18; lever rule of Session 7, Slides 15-21. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

A bar of plain carbon steel with a mass of 8.0 kg and a carbon content of 0.45 wt% C is fully austenitised and then cooled slowly enough to stay at equilibrium. Use the metastable Fe-Fe₃C diagram of the course.

(a) Just above the eutectoid temperature (727 + ΔT °C), name the phases present and give their chemical composition and mass fraction.

(b) Just below the eutectoid temperature (727 − ΔT °C), name the phases and the microconstituents present and give the mass fraction of each.

(c) Calculate the mass, in kg, of proeutectoid ferrite, of eutectoid ferrite (the ferrite inside the pearlite) and of cementite in the bar at 727 − ΔT °C.

(d) Draw a schematic sketch of the microstructure at 727 − ΔT °C, and explain how the amount of proeutectoid ferrite and the pearlite would change if the bar were cooled faster.

## Setup

#### Data

| Quantity | Symbol | Value | As a fraction or in SI |
| :--- | :--- | :--- | :--- |
| Mass of the bar | $m$ | 8.0 kg | 8.0 kg |
| Carbon content of the steel | $C_0$ | 0.45 wt% C | 0.0045 |
| Carbon in ferrite at 727 °C (maximum solubility) | $C_\alpha$ | 0.022 wt% C | Session 9, Slides 5 and 10 |
| Eutectoid composition (austenite at 727 °C) | $C_E$ | 0.76 wt% C | Session 9, Slide 10 |
| Carbon in cementite, Fe₃C | $C_{\text{Fe}_3\text{C}}$ | 6.67 wt% C | Session 9, Slides 4 and 8 |
| Eutectoid temperature | $T_E$ | 727 °C | Session 9, Slide 10 |

The lever rule uses ratios of compositions, so the wt% values can be used directly: the factor 1/100 that turns wt% into a mass fraction cancels between numerator and denominator.

#### Model

- Metastable Fe-Fe₃C diagram, Session 9, Slide 4. Eutectoid reaction on cooling, Session 9, Slide 10: γ (0.76 wt% C) → α (0.022 wt% C) + Fe₃C (6.67 wt% C) at 727 °C; its product is pearlite.
- Since $C_0 = 0.45 < C_E = 0.76$, the steel is **hypoeutectoid** (Session 9, Slide 4): its microconstituents below 727 °C are proeutectoid ferrite and pearlite (Session 9, Slide 14).
- Lever rule on a tie line (Session 7, Slides 15-21), derived in part (a).
- Hypothesis: slow (equilibrium) cooling, so the compositions of the phases are those read on the diagram.

## (a) Phases, compositions and amounts just above the eutectoid temperature [0.75 pts]

### Hint

At 727 + ΔT °C the point (0.45 wt% C, 727 °C) lies in the α + γ field; the ends of the tie line are the ferrite and austenite boundaries at that temperature.

### Checkpoint

- Phases: ferrite α with 0.022 wt% C and austenite γ with 0.76 wt% C
- $W_\alpha = 0.4201$ (42.0 %), $W_\gamma = 0.5799$ (58.0 %)

### Solution

#### Locate the alloy on the diagram and read the ends of the tie line

On cooling, the 0.45 wt% C austenite crosses the A3 line and ferrite starts to form at the austenite grain boundaries (Session 9, Slide 15). Just above 727 °C the point lies in the two-phase field α + γ. The horizontal tie line at 727 + ΔT °C ends on the ferrite boundary at $C_\alpha = 0.022$ wt% C and on the A3 line at the eutectoid point, $C_\gamma = C_E = 0.76$ wt% C (Session 9, Slides 4 and 17).

#### Derive the lever rule from the two mass balances

The phases are the only two places where the mass of the alloy can be, so the mass fractions add up to one (mass balance of the alloy):

$$W_\alpha + W_\gamma = 1$$

The carbon of the alloy is shared between the two phases (mass balance of carbon):

$$W_\alpha C_\alpha + W_\gamma C_\gamma = C_0$$

Substitute $W_\gamma = 1 - W_\alpha$ from the first balance into the second:

$$W_\alpha C_\alpha + (1 - W_\alpha) C_\gamma = C_0$$

Expand and group the terms in $W_\alpha$:

$$W_\alpha (C_\alpha - C_\gamma) = C_0 - C_\gamma$$

Divide by $(C_\alpha - C_\gamma)$ and change the sign of numerator and denominator:

$$W_\alpha = \frac{C_\gamma - C_0}{C_\gamma - C_\alpha}, \qquad W_\gamma = 1 - W_\alpha = \frac{C_0 - C_\alpha}{C_\gamma - C_\alpha}$$

This is the lever rule of Session 7, Slides 15-21: each phase is weighted by the segment of the tie line on the **opposite** side of $C_0$.

#### Substitute the compositions

Tie line length: $C_\gamma - C_\alpha = 0.76 - 0.022 = 0.738$ wt% C.

$$W_\alpha = \frac{0.76 - 0.45}{0.76 - 0.022} = \frac{0.31}{0.738} = 0.4201$$

$$W_\gamma = \frac{0.45 - 0.022}{0.76 - 0.022} = \frac{0.428}{0.738} = 0.5799$$

**Result:** 42.0 % ferrite with 0.022 wt% C and 58.0 % austenite with 0.76 wt% C.

**Checks:** $0.4201 + 0.5799 = 1$. Carbon balance: $0.4201 \times 0.022 + 0.5799 \times 0.76 = 0.0092 + 0.4407 = 0.450$ wt% C $= C_0$.

## (b) Phases and microconstituents just below the eutectoid temperature [0.75 pts]

### Hint

The phases come from the long tie line α - Fe₃C at 727 − ΔT; the microconstituents come from the austenite that existed at 727 + ΔT, because all of it becomes pearlite.

### Checkpoint

- Phases: α (0.022 wt% C) $W_\alpha = 0.9356$; Fe₃C (6.67 wt% C) $W_{\text{Fe}_3\text{C}} = 0.0644$
- Microconstituents: proeutectoid ferrite $W_{\alpha_p} = 0.4201$; pearlite $W_P = 0.5799$ (0.76 wt% C)

### Solution

#### Phases: lever rule on the tie line from ferrite to cementite

Below 727 °C the point lies in the α + Fe₃C field (Session 9, Slide 9). The tie line at 727 − ΔT runs from $C_\alpha = 0.022$ to $C_{\text{Fe}_3\text{C}} = 6.67$ wt% C, length $6.67 - 0.022 = 6.648$. With the lever rule of part (a), written for the pair α, Fe₃C (Session 9, Slide 18):

$$W_\alpha = \frac{C_{\text{Fe}_3\text{C}} - C_0}{C_{\text{Fe}_3\text{C}} - C_\alpha} = \frac{6.67 - 0.45}{6.67 - 0.022} = \frac{6.22}{6.648} = 0.9356$$

$$W_{\text{Fe}_3\text{C}} = \frac{C_0 - C_\alpha}{C_{\text{Fe}_3\text{C}} - C_\alpha} = \frac{0.45 - 0.022}{6.648} = \frac{0.428}{6.648} = 0.0644$$

#### Microconstituents: the austenite of 727 + ΔT becomes pearlite

The proeutectoid (primary) ferrite formed above 727 °C does not change when the steel crosses the eutectoid line. The austenite present at 727 + ΔT has exactly the eutectoid composition, 0.76 wt% C, so all of it undergoes the eutectoid reaction γ (0.76) → α (0.022) + Fe₃C (6.67) and becomes pearlite (Session 9, Slides 10 and 18). The fractions are therefore those of part (a), which is the lever rule on the short tie line from $C_\alpha$ to $C_E$:

$$W_{\alpha_p} = \frac{C_E - C_0}{C_E - C_\alpha} = \frac{0.76 - 0.45}{0.738} = 0.4201, \qquad W_P = \frac{C_0 - C_\alpha}{C_E - C_\alpha} = \frac{0.428}{0.738} = 0.5799$$

**Result:** two phases, ferrite (93.6 %, 0.022 wt% C) and cementite (6.4 %, 6.67 wt% C); two microconstituents, proeutectoid ferrite (42.0 %) and pearlite (58.0 %, overall 0.76 wt% C).

**Checks:** each pair adds up to 1. The ferrite phase (93.6 %) is larger than the proeutectoid ferrite (42.0 %) because the pearlite also contains ferrite; part (c) separates the two.

## (c) Mass of proeutectoid ferrite, eutectoid ferrite and cementite in the 8.0 kg bar [0.75 pts]

### Hint

Eutectoid ferrite = total ferrite − proeutectoid ferrite. Multiply each mass fraction by the mass of the bar.

### Checkpoint

- Proeutectoid ferrite: 3.360 kg
- Eutectoid ferrite (inside the pearlite): 4.125 kg
- Cementite: 0.515 kg (all of it inside the pearlite)

### Solution

#### Split the ferrite phase into proeutectoid and eutectoid ferrite

The ferrite phase of part (b) is the sum of the proeutectoid ferrite and the ferrite of the pearlite lamellae (Session 9, Slide 18):

$$W_{\alpha} = W_{\alpha_p} + W_{\alpha_E}$$

Isolate the eutectoid ferrite:

$$W_{\alpha_E} = W_\alpha - W_{\alpha_p} = \frac{6.22}{6.648} - \frac{0.31}{0.738} = 0.9356 - 0.4201 = 0.5156$$

#### Convert mass fractions into masses

A mass fraction is the mass of the constituent divided by the mass of the bar, $W_i = m_i / m$, so $m_i = W_i\, m$ with $m = 8.0$ kg:

$$m_{\alpha_p} = 0.4201 \times 8.0\ \text{kg} = 3.360\ \text{kg}$$

$$m_{\alpha_E} = 0.5156 \times 8.0\ \text{kg} = 4.125\ \text{kg}$$

$$m_{\text{Fe}_3\text{C}} = 0.0644 \times 8.0\ \text{kg} = 0.515\ \text{kg}$$

(The products are computed with the unrounded fractions, 0.420054, 0.515566 and 0.064380.)

#### Check with the make-up of pearlite

Every pearlite has the make-up of the eutectoid steel, $W_\alpha = (6.67 - 0.76)/(6.67 - 0.022) = 5.91/6.648 = 0.8890$ ferrite and 0.1110 cementite (Session 9, Slide 13). The pearlite of the bar weighs $0.5799 \times 8.0 = 4.640$ kg, so it holds $0.8890 \times 4.640 = 4.125$ kg of ferrite and $0.1110 \times 4.640 = 0.515$ kg of cementite, the values above. Mass check: $3.360 + 4.125 + 0.515 = 8.000$ kg.

## (d) Sketch of the microstructure and effect of a faster cooling [0.75 pts]

### Hint

Draw two kinds of grains in the proportion of part (b). For the cooling rate, recall where the eutectoid point moves on Session 9, Slide 21.

### Checkpoint

- Sketch: light grains of proeutectoid ferrite (about 42 % of the area) and lamellar pearlite colonies (about 58 %)
- Faster cooling: the eutectoid point moves to lower temperature and lower %C, so less proeutectoid ferrite, more pearlite and finer (harder) pearlite

### Solution

#### Draw the two microconstituents in their proportions

The proeutectoid ferrite nucleated at the austenite grain boundaries between the A3 line and 727 °C and grew into equiaxed, light grains; the remaining austenite became pearlite, alternating lamellae of ferrite and cementite (Session 9, Slides 12 and 14). As an approximation (not stated on the slides), the densities of ferrite and pearlite are taken as close, so the mass fractions are drawn as area fractions on the section: about 42 % of light ferrite grains and 58 % of lamellar colonies.

![[attachments/MAT-MT2/p09-microstructure.svg]]

#### Faster cooling: displacement of the eutectoid point

Session 9, Slide 21: if the cooling rate increases, the eutectoid point moves towards lower temperatures and lower carbon contents. The tie line used for the microconstituents then ends at a value $C_E' < 0.76$ wt% C, and the proeutectoid ferrite fraction $(C_E' - C_0)/(C_E' - C_\alpha)$ falls because its numerator shrinks faster than its denominator. So the bar would show **less proeutectoid ferrite and more pearlite**, and the pearlite lamellae would be **closer together (fine pearlite)**, which raises its hardness (Session 9, Slides 12 and 21). The number 0.4201 is valid only for equilibrium cooling.

## Interpretation

The steel spends its last moments above 727 °C as a 42/58 mixture of ferrite and eutectoid austenite; the eutectoid reaction turns all of that austenite into pearlite without touching the ferrite, which is why the microconstituent fractions below 727 °C equal the phase fractions above it. Most of the bar is ferrite (93.6 % by mass), and the 6.4 % of hard cementite is entirely inside the pearlite.

**Limiting cases:** with $C_0 \to C_\alpha = 0.022$ the lever rule gives $W_{\alpha_p} \to 1$ (all ferrite); with $C_0 \to C_E = 0.76$ it gives $W_{\alpha_p} \to 0$ (all pearlite, the eutectoid steel of Session 9, Slide 13).

**Dimensional check:** the lever rule is a ratio of two compositions, (wt%)/(wt%), so it is dimensionless; a mass is a dimensionless fraction times kg, so it is in kg.

**Common exam mistake:** giving the 0.9356 of the long tie line as the "proeutectoid ferrite". That is the whole ferrite phase; the proeutectoid ferrite comes from the short tie line ending at 0.76 wt% C.

## Verification

- W_alpha above 727 | (0.76-0.45)/(0.76-0.022) | 0.4201
- W_gamma above 727 | (0.45-0.022)/(0.76-0.022) | 0.5799
- W_alpha total below 727 | (6.67-0.45)/(6.67-0.022) | 0.9356
- W_Fe3C below 727 | (0.45-0.022)/(6.67-0.022) | 0.0644
- W_alpha_E | (6.67-0.45)/(6.67-0.022)-(0.76-0.45)/(0.76-0.022) | 0.5156
- m proeutectoid ferrite (kg) | 8.0*(0.76-0.45)/(0.76-0.022) | 3.360
- m eutectoid ferrite (kg) | 8.0*((6.67-0.45)/(6.67-0.022)-(0.76-0.45)/(0.76-0.022)) | 4.125
- m cementite (kg) | 8.0*(0.45-0.022)/(6.67-0.022) | 0.515
- m pearlite (kg) | 8.0*(0.45-0.022)/(0.76-0.022) | 4.640
- W_alpha in pearlite | (6.67-0.76)/(6.67-0.022) | 0.8890

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
