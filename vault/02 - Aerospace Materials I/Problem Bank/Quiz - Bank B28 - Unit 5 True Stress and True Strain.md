---
materia: Aerospace Materials I
tema: "Unit 5: true against engineering values, true stress, true strain and the neck"
bank_id: B28
title: "True stress and true strain"
category: mt2_test_block
unit: 5
concepts:
  - u5-true-vs-engineering
  - u5-true-stress-calc
  - u5-true-strain-calc
  - u5-true-after-necking
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 11, Slides 9 and 37-38."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-5
---

# Bank B28 — True stress and true strain

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 11, Slides 9 and 37-38.

## Q28.1 True against engineering values

- id: B28-Q1
- concept_id: u5-true-vs-engineering
- format: true-statement
- asks: comparison

Which one of the following statements comparing true and engineering values in a tensile test is TRUE?

a) Both the true stress and the true strain are larger
b) The true stress is smaller and the true strain larger
c) Both the true stress and the true strain are smaller
d) The true stress is larger and the true strain smaller

### Answer

d

### Explanation

Session 11, Slide 37: the original dimensions change during the test, so $\sigma_{\text{real}} > \sigma_{\text{eng}}$ and $\varepsilon_{\text{real}} < \varepsilon_{\text{eng}}$.

- a) Half right: the true stress is larger, but the true strain is smaller.
- b) Both comparisons are inverted with respect to Slide 37.
- c) Half right: the true strain is smaller, but the true stress is larger.

### Source

Session 11, Slide 37.

## Q28.2 Which curve is the true curve

- id: B28-Q2
- concept_id: u5-true-vs-engineering
- format: diagram-reading
- asks: figure-reading

The shown curves 1 and 2 come from the same tensile test. Indicate which one is the true stress-strain curve and why:

![[attachments/MAT-MT2/u5-true-eng-curves.svg]]

a) Curve 2, because it uses the instantaneous area
b) Curve 1, because it uses the instantaneous area
c) Curve 1, because it uses the original area
d) Curve 2, because it uses the original area

### Answer

a

### Explanation

Session 11, Slide 37: $\sigma_r = F/A_i$ with the instantaneous area; as $A_i$ shrinks, especially in the neck, the true stress keeps rising up to fracture, while the engineering stress $F/A_0$ falls after the maximum. Curve 2 also ends at a smaller strain, since $\varepsilon_r < \varepsilon_{\text{eng}}$.

- b) Curve 1 falls after its maximum, which is the sign of the original area: the engineering curve.
- c) The reason describes the engineering curve correctly, but the true curve is the one asked for.
- d) The curve is right but the reason is wrong: dividing by the original area gives the engineering curve.

### Source

Session 11, Slides 37-38.

## Q28.3 Why the true stress is larger

- id: B28-Q3
- concept_id: u5-true-vs-engineering
- format: cause-effect
- asks: cause

During a tensile test the true stress exceeds the engineering stress because:

a) the gauge length shortens during the test
b) Young's modulus grows with the strain
c) the cross-section shrinks as the specimen stretches
d) the load keeps rising after the maximum

### Answer

c

### Explanation

Session 11, Slide 37: $\sigma_r = F/A_i = \sigma_{\text{eng}}\,A_0/A_i$, and $A_i < A_0$ while the specimen stretches, so $\sigma_r > \sigma_{\text{eng}}$.

- a) The gauge length grows in tension; it is the section that shrinks.
- b) $E$ is the slope of the elastic zone; it does not enter the true stress.
- d) False premise: the load falls after the maximum; the true stress grows because the area falls faster.

### Source

Session 11, Slide 37.

## Q28.4 True stress before necking

- id: B28-Q4
- concept_id: u5-true-stress-calc
- format: numeric
- asks: calculation
- calc: 400*(1+0.20)

Before necking, a specimen has an engineering stress of 400 MPa at an engineering strain of 0.20. Determine the true stress:

a) 72.9 MPa
b) 333 MPa
c) 480 MPa
d) 576 MPa

### Answer

c

### Explanation

Session 11, Slide 38: before necking the volume is constant, $A_0/A_i = l_i/l_0 = 1 + \varepsilon$, so $\sigma_r = \sigma_{\text{eng}}(1 + \varepsilon_{\text{eng}}) = 400 \times 1.20 = 480$ MPa.

- a) The engineering stress was multiplied by the true strain $\ln(1.20)$ instead of by $(1 + \varepsilon)$.
- b) The engineering stress was divided by $(1 + \varepsilon)$: this gives a true stress smaller than the engineering one.
- d) The factor $(1 + \varepsilon)$ was applied twice.

### Source

Session 11, Slide 38.

## Q28.5 True stress from the instantaneous diameter

- id: B28-Q5
- concept_id: u5-true-stress-calc
- format: numeric
- asks: application
- calc: 40000/(pi*5.0**2)

A bar of 12.0 mm original diameter carries 40 kN at the moment its diameter has shrunk to 10.0 mm. Determine the true stress:

a) 127 MPa
b) 246 MPa
c) 354 MPa
d) 509 MPa

### Answer

d

### Explanation

Session 11, Slide 37: $\sigma_r = F/A_i = 40\,000/(\pi\cdot 5.0^2) = 509$ MPa, larger than the engineering stress $40\,000/(\pi\cdot 6.0^2) = 354$ MPa.

- a) The instantaneous diameter was used as the radius: an area four times too large.
- b) The area ratio was inverted: the engineering stress was multiplied by $A_i/A_0$ instead of $A_0/A_i$.
- c) This is the engineering stress, with the original area of 12.0 mm diameter.

### Source

Session 11, Slide 37.

## Q28.6 True stress in terms of engineering values

- id: B28-Q6
- concept_id: u5-true-stress-calc
- format: complete-sentence
- asks: definition

Before necking, the true stress is obtained from the engineering stress and strain as:

a) $\sigma_{\text{eng}}\,(1 + \varepsilon_{\text{eng}})$
b) $\sigma_{\text{eng}}\,(1 + \varepsilon_{\text{eng}})^{-1}$
c) $\sigma_{\text{eng}}\,\varepsilon_{\text{eng}}$
d) $\sigma_{\text{eng}}\,\ln(1 + \varepsilon_{\text{eng}})$

### Answer

a

### Explanation

Session 11, Slide 38: with constant volume, $l_0A_0 = l_iA_i$, so $A_0/A_i = l_i/l_0 = 1 + \varepsilon_{\text{eng}}$ and $\sigma_r = \sigma_{\text{eng}}(1 + \varepsilon_{\text{eng}})$, valid until necking begins.

- b) Dividing makes the true stress smaller than the engineering one, the opposite of Slide 37.
- c) The 1 was dropped from $(1 + \varepsilon)$: the product of stress and strain is an energy per unit volume, not a stress.
- d) $\ln(1 + \varepsilon_{\text{eng}})$ is the true strain; it is not a factor of the stress.

### Source

Session 11, Slide 38.

## Q28.7 True strain from the engineering strain

- id: B28-Q7
- concept_id: u5-true-strain-calc
- format: numeric
- asks: calculation
- calc: log(1+0.35)

Determine the true strain that corresponds to a uniform engineering strain of 0.35:

a) 0.130
b) 0.300
c) 0.350
d) 0.473

### Answer

b

### Explanation

Session 11, Slide 38: before necking $\varepsilon_r = \ln(1 + \varepsilon_{\text{eng}}) = \ln 1.35 = 0.300$, smaller than 0.35 as Slide 37 states.

- a) The decimal logarithm was used: $\log_{10}(1.35)$; the true strain uses the natural logarithm.
- c) This is the engineering strain; the true strain is smaller.
- d) The strain was multiplied by $(1 + \varepsilon)$, as is done for the stress.

### Source

Session 11, Slides 37-38.

## Q28.8 Growing gap between true and engineering strain

- id: B28-Q8
- concept_id: u5-true-strain-calc
- format: cause-effect
- asks: comparison
- check: (0.5 - log(1.5)) > (0.01 - log(1.01)) > 0

With an increase in the engineering strain, the difference between the engineering strain and the true strain:

a) shrinks, and both tend to the same value
b) grows, with the true strain further below
c) stays constant during the whole test
d) grows, with the true strain further above

### Answer

b

### Explanation

Session 11, Slides 37-38: $\varepsilon_r = \ln(1 + \varepsilon_{\text{eng}}) < \varepsilon_{\text{eng}}$; at $\varepsilon = 0.01$, $\ln 1.01 = 0.00995$, while at $\varepsilon = 0.5$, $\ln 1.5 = 0.405$.

- a) Inverted: the two are nearly equal only at small strains.
- c) $\varepsilon - \ln(1 + \varepsilon)$ is not constant: it is about $5\times10^{-5}$ at 0.01 and 0.095 at 0.5.
- d) The difference does grow, but the true strain is the smaller one.

### Source

Session 11, Slides 37-38.

## Q28.9 Expression of the true strain

- id: B28-Q9
- concept_id: u5-true-strain-calc
- format: identify
- asks: definition

Which expression gives the true strain for large strains, when the gauge length changes during the test?

a) $\ln(L_0/L)$
b) $(L - L_0)/L_0$
c) $(L - L_0)/L$
d) $\ln(L/L_0)$

### Answer

d

### Explanation

Session 11, Slide 37: the true strain adds the increments of length over the current length, $\varepsilon_r = \int_{L_0}^{L} dL/L = \ln(L/L_0)$.

- a) The ratio is inverted, which gives a negative strain in tension.
- b) This is the engineering strain, referred only to the initial length.
- c) Dividing by the final length only once does not sum the increments $dL/L$ along the test.

### Source

Session 11, Slide 37.

## Q28.10 True strain in the neck

- id: B28-Q10
- concept_id: u5-true-after-necking
- format: numeric
- asks: calculation
- calc: 2*log(10.0/7.0)

A 10.0 mm diameter specimen has necked down to 7.0 mm. Determine the true strain in the neck:

a) 0.357
b) 0.510
c) 0.713
d) 1.04

### Answer

c

### Explanation

Session 11, Slide 38: after necking $\varepsilon_r = \ln(A_0/A) = 2\ln(D_0/D) = 2\ln(10.0/7.0) = 2 \times 0.357 = 0.713$.

- a) The factor 2 was left out: $\ln(D_0/D)$ is half of $\ln(A_0/A)$.
- b) This is the reduction in area as a fraction, $(A_0 - A)/A_0$, not a true strain.
- d) The ratio $A_0/A - 1$ was taken, an engineering-type strain on areas.

### Source

Session 11, Slide 38.
