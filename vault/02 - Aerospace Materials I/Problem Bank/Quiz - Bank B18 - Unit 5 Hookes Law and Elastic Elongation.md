---
materia: Aerospace Materials I
tema: "Unit 5: Hooke's law, Young's modulus, elastic elongation and engineering stress and strain"
bank_id: B18
title: "Hooke's law, Young's modulus and elastic elongation"
category: mt2_test_block
unit: 5
concepts:
  - u5-hooke-law-calc
  - u5-elastic-elongation-calc
  - u5-stress-rectangular-section
  - u5-engineering-strain-calc
  - u5-modulus-bond-strength
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Data from Session 11, Slides 9, 12-13 and 17."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-5
---

# Bank B18 — Hooke's law, Young's modulus and elastic elongation

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 11, Slides 9, 12-13 and 17.

## Q18.1 Young's modulus from load and strain

- id: B18-Q1
- concept_id: u5-hooke-law-calc
- format: numeric
- asks: calculation
- calc: 10000/(pi*5.0**2)/0.00125/1000

A 10.0 kN load on a rod of 10.0 mm diameter produces an elastic strain of 0.125 %. Determine the Young's modulus of the rod:

a) 25.5 GPa
b) 50.9 GPa
c) 102 GPa
d) 320 GPa

### Answer

c

### Explanation

$\sigma = F/A_0 = 10\,000/(\pi\cdot 5^2) = 127.3$ MPa (Session 11, Slide 9) and, with Hooke's law $\sigma = E\varepsilon$ (Slide 12), $E = 127.3/0.00125 = 101\,900$ MPa $= 102$ GPa.

- a) The diameter was used as the radius, so the area is four times too large and the stress four times too small.
- b) The area was written as $\pi d^2/2$ instead of $\pi d^2/4$, which halves the stress: $63.7/0.00125 = 50\,900$ MPa.
- d) The factor $\pi$ was left out of the area: $\sigma = 10\,000/5^2 = 400$ MPa and $400/0.00125 = 320$ GPa.

### Source

Session 11, Slides 9 and 12.

## Q18.2 Linear elastic design and Hooke's law

- id: B18-Q2
- concept_id: u5-hooke-law-calc
- format: topic-false
- asks: application

Referring to Hooke's law ($\sigma = E\varepsilon$) in the linear elastic design of a structural alloy, which statement is FALSE?

a) Increasing the applied stress within the elastic limit increases the strain in the same proportion
b) Below the proportional limit, the slope of the stress-strain curve equals Young's modulus $E$
c) Doubling the cross-sectional area of a bar doubles the Young's modulus of the alloy
d) Upon unloading from below the yield strength, the elastic strain returns to zero

### Answer

c

### Explanation

Young's modulus $E$ is an intrinsic stiffness property of the material set by its atomic bond strength (Session 11, Slides 12-13); changing a bar's cross-sectional area alters the stress $\sigma = F/A_0$ and elongation, not $E$ itself.

- a) This is true: $\sigma = E\varepsilon$ means stress and strain are directly proportional in the linear elastic zone.
- b) This is true: $E = \sigma/\varepsilon$ is the slope of the linear elastic segment of the stress-strain curve.
- d) This is true: elastic deformation is reversible when the load is removed (Slide 12).

### Source

Session 11, Slides 10 and 12-13.

## Q18.3 Strain of steel and aluminium under the same stress

- id: B18-Q3
- concept_id: u5-hooke-law-calc
- format: cause-effect
- asks: comparison
- check: abs(207/69 - 3) < 0.01

Under the same elastic stress, compared with a steel bar, an aluminium bar shows a strain that is:

a) about three times larger, because its modulus is lower
b) about three times smaller, because its modulus is lower
c) the same, because the stress is the same
d) about three times larger, because its yield strength is lower

### Answer

a

### Explanation

Hooke's law $\varepsilon = \sigma/E$ (Session 11, Slide 12) with $E_{\text{steel}} = 207$ GPa and $E_{\text{Al}} = 69$ GPa (Slide 17): $\varepsilon_{\text{Al}}/\varepsilon_{\text{steel}} = 207/69 = 3.0$.

- b) The cause is right but the effect is inverted: with $\varepsilon = \sigma/E$, a lower modulus gives a larger strain.
- c) The strain depends on the material through $E$; equal stress gives equal strain only for equal moduli.
- d) The trend is right but the cause is wrong: in the elastic zone the strain is set by $E$, not by the yield strength.

### Source

Session 11, Slides 12 and 17.

## Q18.4 Range of Hooke's law

- id: B18-Q4
- concept_id: u5-hooke-law-calc
- format: true-statement
- asks: definition

Which one of the following statements about Hooke's law is TRUE?

a) Hooke's law also describes the plastic zone of metals
b) Stress is proportional to strain only in the linear elastic zone
c) The Young's modulus is the strain divided by the stress
d) Stress is proportional to strain up to the tensile strength

### Answer

b

### Explanation

Session 11, Slides 10 and 12: for a linear elastic material $\sigma = E\varepsilon$ (Hooke's law), valid for $\sigma < \sigma_y$; in the plastic zone the proportionality is lost.

- a) In the plastic zone "$\varepsilon$ is no longer proportional to $\sigma$" (Slide 21).
- c) The ratio is inverted: $E = \sigma/\varepsilon$, so its units are those of stress.
- d) Beyond the yield strength the strain is no longer proportional to the stress (Slide 10), well before the tensile strength.

### Source

Session 11, Slides 10, 12 and 21.

## Q18.5 Elongation of a brass rod

- id: B18-Q5
- concept_id: u5-elastic-elongation-calc
- format: numeric
- asks: calculation
- calc: 12000/(pi*5**2)/97000*2000

A brass rod ($E$ = 97 GPa), 2.0 m long and 10 mm in diameter, carries an elastic load of 12 kN. Determine its elongation:

a) $3.15\times10^{-3}$ mm
b) 0.788 mm
c) 3.15 mm
d) 9.90 mm

### Answer

c

### Explanation

$\sigma = 12\,000/(\pi\cdot 5^2) = 152.8$ MPa; $\varepsilon = \sigma/E = 152.8/97\,000 = 1.575\times10^{-3}$ (Session 11, Slide 12); $\Delta l = \varepsilon\,l_0 = 1.575\times10^{-3}\times 2000 = 3.15$ mm.

- a) The length was entered as 2.0 (metres) while the answer is given in millimetres, a factor of 1000 too small.
- b) The diameter was used as the radius: an area four times too large gives an elongation four times too small.
- d) The factor $\pi$ was left out of the area, $12\,000/5^2 = 480$ MPa, which overestimates the stress.

### Source

Session 11, Slides 9, 12 and 17.

## Q18.6 Effect of diameter on elastic elongation

- id: B18-Q6
- concept_id: u5-elastic-elongation-calc
- format: cause-effect
- asks: application

Referring to elastic elongation $\Delta l = F l_0/(E A_0)$ under a fixed tensile load, replacing a cylindrical rod with one of the same alloy and length but twice the diameter causes the elastic elongation to:

a) remain unchanged, because the load and length are the same
b) decrease to one half of its original value
c) increase by a factor of four
d) decrease to one quarter of its original value

### Answer

d

### Explanation

Combining $\sigma = F/A_0$ and $\Delta l = (\sigma/E)\,l_0$ (Session 11, Slides 9 and 12) gives $\Delta l = F l_0/(E\,\pi d_0^2/4)$. Doubling the diameter increases the cross-sectional area by a factor of $2^2 = 4$, reducing the stress and elastic elongation to one quarter.

- a) Both the area and the stress change when the diameter changes, so the elongation changes even at constant load and length.
- b) This treats cross-sectional area as proportional to $d_0$ instead of $d_0^2$.
- c) Inverted trend: a thicker rod is stiffer in axial tension and stretches less, not more, under the same force.

### Source

Session 11, Slides 9 and 12.

## Q18.7 Effect of the length on the elastic elongation

- id: B18-Q7
- concept_id: u5-elastic-elongation-calc
- format: complete-sentence
- asks: effect

Doubling the length of a bar that carries the same elastic load:

a) doubles its elongation and keeps its strain
b) keeps its elongation and halves its strain
c) doubles both its elongation and its strain
d) halves its elongation and keeps its strain

### Answer

a

### Explanation

The stress $F/A_0$ and the material are unchanged, so $\varepsilon = \sigma/E$ is unchanged (Session 11, Slides 9 and 12); since $\Delta l = \varepsilon\,l_0$, twice the length gives twice the elongation.

- b) This assumes a fixed elongation; in fact the strain is fixed by $\sigma/E$ and the elongation scales with $l_0$.
- c) The strain $\sigma/E$ depends only on the stress and the material; the length does not change it.
- d) The elongation is $\varepsilon\,l_0$, which grows, not shrinks, with the length.

### Source

Session 11, Slides 9 and 12.

## Q18.8 Square versus circular cross-section under load

- id: B18-Q8
- concept_id: u5-stress-rectangular-section
- format: topic-true
- asks: comparison

With respect to engineering stress $\sigma_n = F/A_0$, consider a square bar of side $a$ and a circular bar of diameter $d = a$ carrying the same axial tensile load $F$. Which statement is TRUE?

a) Both bars experience the same engineering stress because $d = a$
b) The circular bar experiences a higher stress because its area $\pi a^2/4$ is smaller
c) The square bar experiences a higher stress because its area is smaller
d) The circular bar experiences four times the stress of the square bar

### Answer

b

### Explanation

The square section has area $A_{\text{sq}} = a^2$, while the circular section has area $A_{\text{circ}} = \pi a^2/4 \approx 0.785\,a^2 < a^2$. Since $\sigma_n = F/A_0$ (Session 11, Slide 9), the circular bar carries the same load over a smaller area and therefore experiences a higher engineering stress.

- a) Equal width or diameter does not give equal cross-sectional area: a circle inscribed in a square has smaller area by a factor of $\pi/4$.
- c) Inverted comparison: $a^2$ is larger than $\pi a^2/4$, so the square bar has the lower stress.
- d) The factor $\pi$ was omitted from the circular area: comparing $a^2$ with $a^2/4$ omits $\pi$ in the denominator.

### Source

Session 11, Slide 9.

## Q18.9 Properties of engineering strain

- id: B18-Q9
- concept_id: u5-engineering-strain-calc
- format: topic-false
- asks: comparison

Regarding nominal (engineering) strain $\varepsilon_n = (l - l_0)/l_0$ in a uniform bar under uniaxial elastic tension, which statement is FALSE?

a) It is a dimensionless ratio often reported as a fraction or percentage
b) Within the linear elastic region it equals $\sigma_n/E$
c) Doubling the initial gauge length $l_0$ under the same stress doubles the engineering strain
d) Multiplying the strain by $l_0$ gives the elongation $\Delta l$

### Answer

c

### Explanation

Under a given axial stress $\sigma_n$, Hooke's law gives $\varepsilon_n = \sigma_n/E$ (Session 11, Slide 12), which depends only on the stress and the material, not on $l_0$. Doubling $l_0$ doubles the total elongation $\Delta l = \varepsilon_n l_0$, while $\varepsilon_n$ itself stays the same.

- a) This is true: $(l - l_0)/l_0$ divides length by length, so it has no physical dimensions (Slide 9).
- b) This is true: $\sigma = E\varepsilon$ in the linear elastic zone (Slide 12).
- d) This is true: rearranging $\varepsilon_n = \Delta l/l_0$ yields $\Delta l = \varepsilon_n l_0$.

### Source

Session 11, Slides 9 and 12.

## Q18.10 Bond strength, modulus and melting

- id: B18-Q10
- concept_id: u5-modulus-bond-strength
- format: complete-sentence
- asks: cause

Compared with a weakly bonded solid, a solid with stronger interatomic bonds has:

a) a higher Young's modulus and a lower melting temperature
b) a lower Young's modulus and a higher melting temperature
c) a lower Young's modulus and a lower melting temperature
d) a higher Young's modulus and a higher melting temperature

### Answer

d

### Explanation

Session 11, Slide 13: $E = f(\text{bond strength})$, "↑ bond strength ↔ ↑E", and "bond force ↔ T melting"; $E$ is the slope of the force curve at $r_0$, which is steeper for a stronger bond.

- a) Half right: the modulus rises, but the slide links a higher bond force to a higher, not lower, melting temperature.
- b) Half right: the melting temperature rises, but the modulus rises with the bond strength too, it does not fall.
- c) Both trends are inverted: a stronger bond raises both properties.

### Source

Session 11, Slide 13.
