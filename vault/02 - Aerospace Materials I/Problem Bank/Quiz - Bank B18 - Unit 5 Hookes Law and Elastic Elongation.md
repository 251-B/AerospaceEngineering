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

## Q18.2 Largest stress for an allowed elastic strain

- id: B18-Q2
- concept_id: u5-hooke-law-calc
- format: numeric
- asks: application
- calc: 69000*0.0015

An aluminium part ($E$ = 69 GPa) must work with an elastic strain of no more than 0.0015. Determine the largest allowed stress:

a) 0.104 MPa
b) 104 MPa
c) 311 MPa
d) 1040 MPa

### Answer

b

### Explanation

Hooke's law (Session 11, Slide 12): $\sigma = E\varepsilon = 69\,000\ \text{MPa} \times 0.0015 = 103.5$ MPa $\approx 104$ MPa.

- a) The modulus was kept in GPa and the result read as MPa: $69 \times 0.0015 = 0.1035$, a factor of 1000 too small.
- c) The modulus of steel (207 GPa) was used instead of that of aluminium (69 GPa, Slide 17).
- d) The strain was read as 0.015, one decimal place off, which gives a stress ten times too large.

### Source

Session 11, Slides 12 and 17.

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

## Q18.6 Diameter that limits the elongation

- id: B18-Q6
- concept_id: u5-elastic-elongation-calc
- format: numeric
- asks: application
- calc: 2*sqrt(20000/(207000*5.0/10000)/pi)

A 10 m steel cable ($E$ = 207 GPa) carries 20 kN and may stretch at most 5.0 mm. Determine the minimum cable diameter:

a) 0.496 mm
b) 7.84 mm
c) 13.9 mm
d) 15.7 mm

### Answer

d

### Explanation

$\varepsilon = 5.0/10\,000 = 5.0\times10^{-4}$, $\sigma = E\varepsilon = 207\,000 \times 5.0\times10^{-4} = 103.5$ MPa (Session 11, Slide 12), $A = F/\sigma = 20\,000/103.5 = 193.2$ mm² and $d = 2\sqrt{A/\pi} = 15.7$ mm.

- a) The strain was computed with the length in metres and the elongation in millimetres, $5/10 = 0.5$, a strain 1000 times too large.
- b) This is the radius of the required section; it was not doubled to give the diameter.
- c) The section was taken as a square, $d = \sqrt{A} = \sqrt{193.2}$, instead of a circle of area $\pi d^2/4$.

### Source

Session 11, Slides 9, 12 and 17.

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

## Q18.8 Engineering stress in a rectangular strip

- id: B18-Q8
- concept_id: u5-stress-rectangular-section
- format: numeric
- asks: calculation
- calc: 18000/(4.0*25)

A strip of rectangular section, 4.0 mm by 25 mm, carries a tensile load of 18 kN. Determine the engineering stress:

a) 0.180 MPa
b) 180 MPa
c) 310 MPa
d) 720 MPa

### Answer

b

### Explanation

$\sigma_n = F/A_0$ (Session 11, Slide 9) with $A_0 = 4.0 \times 25 = 100$ mm²: $\sigma_n = 18\,000/100 = 180$ MPa.

- a) The load was kept in kN: $18/100 = 0.18$, a factor of 1000 too small.
- c) The perimeter, $2(4 + 25) = 58$ mm, was used instead of the area of the section.
- d) Only the width was used as the area, $18\,000/25$, ignoring the 4.0 mm thickness.

### Source

Session 11, Slide 9.

## Q18.9 Final length from the engineering strain

- id: B18-Q9
- concept_id: u5-engineering-strain-calc
- format: numeric
- asks: application
- calc: 50*(1+0.0024)

A 50.00 mm gauge length is stretched to an engineering strain of 0.24 %. Determine the length of the gauge under load:

a) 0.120 mm
b) 12.0 mm
c) 50.12 mm
d) 62.0 mm

### Answer

c

### Explanation

From $\varepsilon_n = (l - l_0)/l_0$ (Session 11, Slide 9): $l = l_0(1 + \varepsilon_n) = 50.00 \times (1 + 0.0024) = 50.12$ mm.

- a) This is the elongation $\varepsilon\,l_0$, not the length under load: $l_0$ was not added.
- b) The strain 0.24 % was used as the fraction 0.24, and only the elongation was computed.
- d) The strain 0.24 % was used as the fraction 0.24: $50 \times 1.24 = 62$ mm.

### Source

Session 11, Slide 9.

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
