---
materia: Aerospace Materials I
tema: "Unit 5: true values after necking, the strengthening principle, strain hardening and percent cold work"
bank_id: B29
title: "The neck, the strengthening principle and strain hardening"
category: mt2_test_block
unit: 5
concepts:
  - u5-true-after-necking
  - u5-strengthening-principle
  - u5-strain-hardening-mechanism
  - u5-percent-cold-work
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 11, Slide 38 and Session 12, Slides 2-7."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-5
---

# Bank B29 — The neck, the strengthening principle and strain hardening

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 11, Slide 38 and Session 12, Slides 2-7.

## Q29.1 True values after necking

- id: B29-Q1
- concept_id: u5-true-after-necking
- format: false-statement
- asks: definition

Which one of the following statements about the true values after necking is FALSE?

a) $\varepsilon_r = \ln(1 + \varepsilon_{\text{eng}})$ still holds in the neck
b) The true strain can be written as $2\ln(D_0/D)$
c) The true stress is the load over the area of the neck
d) The deformation is no longer uniform along the gauge

### Answer

a

### Explanation

Session 11, Slide 38: $\varepsilon_r = \ln(1 + \varepsilon_{\text{eng}})$ and $\sigma_r = \sigma_{\text{eng}}(1 + \varepsilon_{\text{eng}})$ hold "until the beginning of necking"; after it, the true values must be taken from the area of the neck.

- b) This is true: $\varepsilon_r = \ln(A_0/A) = 2\ln(D_0/D)$ (Slide 38).
- c) This is true: after necking $\sigma = F_i/A_i$ (Slide 38).
- d) This is true: the slide heads this case "after necking (deformation is not uniform)".

### Source

Session 11, Slide 38.

## Q29.2 Why the uniform formulas fail in the neck

- id: B29-Q2
- concept_id: u5-true-after-necking
- format: cause-effect
- asks: cause

After necking begins, $\sigma_r = \sigma_{\text{eng}}(1 + \varepsilon_{\text{eng}})$ can no longer be used because:

a) the specimen starts to lose volume
b) the true strain becomes negative
c) the deformation is no longer uniform along the gauge
d) the applied load drops to zero

### Answer

c

### Explanation

Session 11, Slide 38: the relation comes from $l_0A_0 = l_iA_i$ with the same area along the gauge, valid "before necking (uniform deformation)"; after necking the neck has a smaller area than the rest, so the true stress is $F_i/A_i$ with the neck area.

- a) The formula fails because the strain concentrates in the neck, not because the material loses volume.
- b) In tension the true strain stays positive; $\ln(A_0/A) > 0$ in the neck.
- d) The load falls after the maximum but it is not zero until fracture.

### Source

Session 11, Slide 38.

## Q29.3 Principle of all strengthening mechanisms

- id: B29-Q3
- concept_id: u5-strengthening-principle
- format: complete-sentence
- asks: definition

All the strengthening mechanisms of metals rely on one principle:

a) breaking all the bonds of a plane at once
b) making the dislocations move more easily
c) raising the Young's modulus of the metal
d) impeding the movement of dislocations

### Answer

d

### Explanation

Session 12, Slide 4: "a restriction in the dislocation movement → increase in the stress required to activate the slip system → strengthening"; all four methods rely on this one principle.

- a) Simultaneous breaking of bonds is the slip without dislocations, which is not a strengthening method.
- b) Easier dislocation motion means easier plastic deformation, that is, a weaker metal.
- c) $E$ measures elastic stiffness and is set by the bonds; strengthening raises the yield strength.

### Source

Session 11, Slides 13 and 23; Session 12, Slide 4.

## Q29.4 Not a strengthening mechanism

- id: B29-Q4
- concept_id: u5-strengthening-principle
- format: identify
- asks: classification

Which of the following is NOT one of the four strengthening mechanisms listed in the slides?

a) Solid solution strengthening
b) Precipitation strengthening
c) Strain hardening
d) Growth of the grain size

### Answer

d

### Explanation

Session 12, Slide 4: strain hardening, solid solution strengthening, grain size reduction strengthening and precipitation strengthening. Growth of the grains removes barriers to slip, the opposite of grain size reduction (Slide 10).

- a) It is listed: solute atoms distort the lattice (Slides 4 and 8).
- b) It is listed: particles of a second phase obstruct dislocations (Slides 4 and 12).
- c) It is listed: cold work raises the dislocation density (Slides 4-5).

### Source

Session 12, Slides 4 and 10.

## Q29.5 Dislocation mobility and strength

- id: B29-Q5
- concept_id: u5-strengthening-principle
- format: cause-effect
- asks: effect

With an increase in the mobility of its dislocations, the strength of a metal:

a) decreases, because slip becomes easier
b) increases, because more slip becomes possible
c) decreases, because its bonds become weaker
d) does not change, because $E$ stays constant

### Answer

a

### Explanation

Session 12, Slides 2-3: plastic deformation is the movement of dislocations, and "increased dislocation motion decreases the strength".

- b) The trend is inverted: more slip at a lower stress means a lower strength.
- c) The trend is right but the cause is wrong: the bonds are the same; what changes is how easily dislocations move.
- d) Strength and stiffness are different properties; the yield strength depends on dislocation motion.

### Source

Session 12, Slides 2-4.

## Q29.6 Mechanism of strain hardening

- id: B29-Q6
- concept_id: u5-strain-hardening-mechanism
- format: true-statement
- asks: cause

Which one of the following statements about strain hardening is TRUE?

a) It works by particles of a second phase in the grains
b) Cold deformation multiplies dislocations, which tangle together
c) It works by solute atoms that distort the lattice
d) Cold deformation removes dislocations, so slip becomes easier

### Answer

b

### Explanation

Session 12, Slide 5: cold plastic deformation generates dislocations; the increase in dislocation density makes further deformation difficult because the dislocations "tangle with each other".

- a) This is precipitation strengthening (Slide 12).
- c) This is solid solution strengthening (Slide 8).
- d) Inverted: the density rises, from $10^6$ to $10^{12}$ m/m³ on the slide, and slip becomes harder.

### Source

Session 12, Slides 5, 8 and 12.

## Q29.7 Cold rolling a copper strip

- id: B29-Q7
- concept_id: u5-strain-hardening-mechanism
- format: what-happens
- asks: effect

A copper strip is cold rolled to a smaller thickness. What will happen to its properties:

a) Both its yield strength and its ductility will rise
b) Its yield strength will fall and its ductility will rise
c) Its yield strength will rise and its ductility will fall
d) Both its yield strength and its ductility will fall

### Answer

c

### Explanation

Session 12, Slides 5 and 7: the higher the %CW, the higher $\sigma_y$ and the lower the ductility; the charts for 1040 steel, brass and copper show the yield strength rising and %EL falling.

- a) Half right: the strength rises, but the ductility falls.
- b) Both trends are inverted; this is the opposite of cold work.
- d) Half right: the ductility falls, but the strength rises.

### Source

Session 12, Slides 5-7.

## Q29.8 Ductility against cold work

- id: B29-Q8
- concept_id: u5-strain-hardening-mechanism
- format: choose-figure
- asks: figure-reading

Which picture describes the ductility (%EL) of copper as the percent cold work increases?

a) ![[attachments/MAT-MT2/u5-trend-3.svg]]
b) ![[attachments/MAT-MT2/u5-trend-4.svg]]
c) ![[attachments/MAT-MT2/u5-trend-1.svg]]
d) ![[attachments/MAT-MT2/u5-trend-2.svg]]

### Answer

a

### Explanation

Session 12, Slide 7: the ductility (%EL) of copper, brass and 1040 steel falls as the percent cold work grows, while the yield strength rises and levels off.

- b) A flat line would mean that cold work does not affect ductility, against the slide.
- c) A curve that rises and levels off is the shape of the yield strength against %CW, not of the ductility.
- d) A maximum at medium cold work does not appear on the slide; the ductility falls from the start.

### Source

Session 12, Slides 5 and 7.

## Q29.9 Percent cold work of a drawn rod

- id: B29-Q9
- concept_id: u5-percent-cold-work
- format: numeric
- asks: calculation
- calc: (15.0**2-12.0**2)/15.0**2*100

A rod of 15.0 mm diameter is cold drawn to 12.0 mm. Determine the percent cold work:

a) 20.0 %
b) 36.0 %
c) 56.3 %
d) 64.0 %

### Answer

b

### Explanation

Session 12, Slide 6: $\%CW = \dfrac{A_0 - A_d}{A_0}\times100 = \dfrac{15.0^2 - 12.0^2}{15.0^2}\times100 = \dfrac{81}{225}\times100 = 36.0\,\%$.

- a) The diameters were used instead of the areas: $(15 - 12)/15$.
- c) The change of area was divided by the deformed area, $81/144$, instead of the original one.
- d) This is $A_d/A_0$, the area that remains, not the cold work.

### Source

Session 12, Slide 6.

## Q29.10 What the percent cold work compares

- id: B29-Q10
- concept_id: u5-percent-cold-work
- format: complete-sentence
- asks: definition

The percent cold work of a deformed part compares:

a) its hardness before and after deformation
b) its cross-sections before and after deformation
c) its yield strengths before and after deformation
d) its lengths before and after deformation

### Answer

b

### Explanation

Session 12, Slide 6: $\%CW = (A_0 - A_d)/A_0 \times 100$, with $A_0$ the original cross-section and $A_d$ the cross-section after deformation.

- a) Hardness also rises with cold work, but it is not how %CW is defined.
- c) The yield strength is the effect of cold work, not its measure.
- d) Comparing lengths is the form of the percent elongation; %CW is defined with areas.

### Source

Session 11, Slide 32; Session 12, Slides 5-6.
