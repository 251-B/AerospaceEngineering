---
materia: Aerospace Materials I
tema: "Unit 5: yield strength, the 0.2 % offset criterion and discontinuous yield points"
bank_id: B23
title: "Yield strength, the 0.2 % offset and discontinuous yielding"
category: mt2_test_block
unit: 5
concepts:
  - u5-yield-strength-definition
  - u5-offset-method
  - u5-discontinuous-yield
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 11, Slides 10, 21 and 28."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-5
---

# Bank B23 — Yield strength, the 0.2 % offset and discontinuous yielding

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 11, Slides 10, 21 and 28.

## Q23.1 Meaning of the yield strength

- id: B23-Q1
- concept_id: u5-yield-strength-definition
- format: true-statement
- asks: definition

Which one of the following statements about the yield strength $\sigma_y$ is TRUE?

a) It is the stress above which deformation becomes permanent
b) It is the stress at which the specimen breaks
c) It is the maximum stress that the specimen supports
d) It is the stress at which necking begins

### Answer

a

### Explanation

Session 11, Slide 28: "yield strength (stress) $\sigma_y$: stress above which permanent deformation occurs"; Slide 10 separates the elastic zone $\sigma < \sigma_y$ from the plastic zone $\sigma > \sigma_y$.

- b) The stress at fracture is the fracture stress (Slide 31), the last point of the curve.
- c) The maximum nominal stress is the tensile strength (Slide 30), reached after yielding.
- d) Necking begins at the tensile strength, at the maximum of the curve, not at yielding.

### Source

Session 11, Slides 10, 28, 30 and 31.

## Q23.2 Strain above the yield strength

- id: B23-Q2
- concept_id: u5-yield-strength-definition
- format: cause-effect
- asks: effect

With an increase in the applied stress above the yield strength, the strain of a metal:

a) stops growing until the specimen starts to neck
b) stays proportional to the stress, as in the elastic zone
c) is still fully recovered when the load is removed
d) is no longer proportional to the stress and is partly permanent

### Answer

d

### Explanation

Session 11, Slides 10 and 21: in the plastic zone ($\sigma > \sigma_y$) "$\varepsilon$ is no longer proportional to $\sigma$" and the deformation is permanent; on unloading only the elastic part is recovered.

- a) The strain keeps growing in the uniform plastic deformation between yielding and the tensile strength.
- b) Proportionality is lost at yielding: in the plastic zone $\varepsilon$ is not proportional to $\sigma$.
- c) Full recovery belongs to the elastic zone; above $\sigma_y$ a permanent part remains.

### Source

Session 11, Slides 10 and 21.

## Q23.3 Criteria for the yield stress

- id: B23-Q3
- concept_id: u5-yield-strength-definition
- format: false-statement
- asks: classification

Which one of the following statements about the criteria for the yield stress is FALSE?

a) Above the yield stress the deformation is permanent
b) Low-carbon steels may show upper and lower yield points
c) The 0.2 % offset criterion is rarely used for metals
d) The criterion is chosen according to the material

### Answer

c

### Explanation

Session 11, Slide 28: the conventional yield stress at 0.2 % plastic strain is "the most frequently used in metals"; low-carbon steels and some polymers with a discontinuous yield point use $\sigma_y = (\sigma_{\max} + \sigma_{\min})/2$.

- a) This is true: it is the definition of the yield stress (Slide 28).
- b) This is true: they are the slide's example of discontinuous yielding.
- d) This is true: "depending on the deformation of material we adopt criteria" (Slide 28).

### Source

Session 11, Slide 28.

## Q23.4 Reading the 0.2 % offset yield strength

- id: B23-Q4
- concept_id: u5-offset-method
- format: diagram-reading
- asks: figure-reading
- check: abs(300 + 160*(1 - exp(-(0.0039 - 0.0015)/(0.0024/log(2)))) - 380) < 1 and abs(200000*(0.0039 - 0.002) - 380) < 1e-6

From the shown stress-strain curve of an alloy with $E$ = 200 GPa, indicate the yield strength given by the 0.2 % offset method:

![[attachments/MAT-MT2/u5-offset-yield.svg]]

a) 300 MPa
b) 380 MPa
c) 400 MPa
d) 450 MPa

### Answer

b

### Explanation

Session 11, Slide 28: the conventional yield stress is read where the curve meets the line drawn parallel to the elastic slope from $\varepsilon = 0.002$. On the figure that line, $\sigma = 200\,000(\varepsilon - 0.002)$, crosses the curve at Y: $\varepsilon = 0.0039$, $\sigma = 380$ MPa.

- a) This is point P, where the curve leaves the straight line; the conventional yield stress is taken at 0.2 % plastic strain, not at the end of linearity.
- c) This is the stress of the elastic line at $\varepsilon = 0.002$, $200\,000 \times 0.002$; the offset line starts at 0.002, it does not end there.
- d) This is close to the highest stress drawn, which belongs to the tensile strength region, not to yielding.

### Source

Session 11, Slides 28 and 30.

## Q23.5 Construction of the offset line

- id: B23-Q5
- concept_id: u5-offset-method
- format: complete-sentence
- asks: definition

In the 0.2 % offset method, the yield strength is read where the curve meets a line:

a) horizontal, at 0.2 % of the tensile strength
b) parallel to the elastic part, starting at the origin
c) perpendicular to the elastic part, at $\varepsilon = 0.002$
d) parallel to the elastic part, starting at $\varepsilon = 0.002$

### Answer

d

### Explanation

Session 11, Slide 28: $\sigma_y = \sigma(0.2\,\%\ \text{of}\ \varepsilon)$: a line with the elastic slope $E$ is drawn from $\varepsilon = 0.002$, and its intersection with the curve is the conventional yield stress.

- a) The 0.2 % is a plastic strain, not a fraction of a stress.
- b) A line from the origin with the elastic slope is the elastic line itself; it meets the curve only where yielding begins to be visible.
- c) The construction uses a parallel line, so that it measures a plastic strain of exactly 0.2 %.

### Source

Session 11, Slides 28 and 32.

## Q23.6 Stress on the offset line

- id: B23-Q6
- concept_id: u5-offset-method
- format: numeric
- asks: application
- calc: 110000*(0.0050 - 0.002)

For a copper alloy with $E$ = 110 GPa, determine the stress of the 0.2 % offset line at a total strain of 0.0050:

a) 220 MPa
b) 330 MPa
c) 550 MPa
d) 770 MPa

### Answer

b

### Explanation

The offset line has the elastic slope and starts at $\varepsilon = 0.002$ (Session 11, Slide 28): $\sigma = E(\varepsilon - 0.002) = 110\,000 \times 0.0030 = 330$ MPa.

- a) Only the offset strain was used: $110\,000 \times 0.002$.
- c) The offset was ignored: $110\,000 \times 0.0050$ is the elastic line from the origin.
- d) The offset was added instead of subtracted: $110\,000 \times (0.0050 + 0.002)$.

### Source

Session 11, Slides 12 and 28.

## Q23.7 Criterion for an aluminium alloy

- id: B23-Q7
- concept_id: u5-offset-method
- format: identify
- asks: application

Which criterion gives the yield strength of an aluminium alloy whose curve has no upper and lower yield points?

a) The 0.2 % offset yield stress
b) The mean of the upper and lower yield points
c) The maximum nominal stress of the curve
d) The stress at which the specimen fractures

### Answer

a

### Explanation

Session 11, Slide 28: the conventional yield stress at 0.2 % plastic strain is the most used criterion in metals; the mean of the maximum and minimum is kept for materials with a discontinuous yield point.

- b) This criterion is for discontinuous yielding, which this curve does not show.
- c) The maximum nominal stress is the tensile strength, not the onset of plastic deformation.
- d) The fracture stress is the end of the test, far beyond yielding.

### Source

Session 11, Slides 28 and 30-31.

## Q23.8 Yield stress of a low-carbon steel

- id: B23-Q8
- concept_id: u5-discontinuous-yield
- format: diagram-reading
- asks: figure-reading
- check: (330 + 290)/2 == 310

From the shown curve of a low-carbon steel, indicate its yield stress according to the criterion of the slides:

![[attachments/MAT-MT2/u5-discontinuous-yield.svg]]

a) 20 MPa
b) 290 MPa
c) 310 MPa
d) 330 MPa

### Answer

c

### Explanation

Session 11, Slide 28: for discontinuous yielding (low-carbon steels, some polymers), $\sigma_y = (\sigma_{\max} + \sigma_{\min})/2 = (330 + 290)/2 = 310$ MPa.

- a) The difference was halved, $(330 - 290)/2$, instead of the sum.
- b) Only the lower yield point was taken; the slide uses the mean of both points.
- d) Only the upper yield point was taken; the slide uses the mean of both points.

### Source

Session 11, Slide 28.

## Q23.9 Materials with discontinuous yielding

- id: B23-Q9
- concept_id: u5-discontinuous-yield
- format: identify
- asks: classification

Which materials show upper and lower yield points according to the slides?

a) Low-carbon steels and some polymers
b) Elastomers such as natural rubber
c) Aluminium and copper alloys
d) Ceramics and glasses

### Answer

a

### Explanation

Session 11, Slide 28: "discontinuity phenomena in the yield point: low carbon steels, some polymers, etc.", with $\sigma_y = (\sigma_{\max} + \sigma_{\min})/2$.

- b) Elastomers have a curved, largely elastic response (Slide 16) without a yield drop.
- c) These yield gradually and are given the 0.2 % offset yield stress.
- d) These fail in the elastic zone with almost no plastic deformation (Slide 16), so they show no yield points.

### Source

Session 11, Slides 16 and 28.

## Q23.10 Lower yield point from the yield stress

- id: B23-Q10
- concept_id: u5-discontinuous-yield
- format: numeric
- asks: application
- calc: 2*240 - 262

A steel with discontinuous yielding has an upper yield point of 262 MPa and a yield stress of 240 MPa by the slides' criterion. Determine its lower yield point:

a) 22.0 MPa
b) 218 MPa
c) 251 MPa
d) 284 MPa

### Answer

b

### Explanation

Session 11, Slide 28: $\sigma_y = (\sigma_{\max} + \sigma_{\min})/2$, so $\sigma_{\min} = 2\sigma_y - \sigma_{\max} = 480 - 262 = 218$ MPa.

- a) This is the difference $262 - 240$, not the lower yield point.
- c) The yield stress and the upper point were averaged, $(240 + 262)/2$, which reverses the criterion.
- d) The difference was added to the yield stress instead of subtracted: $240 + 22$.

### Source

Session 11, Slide 28.
