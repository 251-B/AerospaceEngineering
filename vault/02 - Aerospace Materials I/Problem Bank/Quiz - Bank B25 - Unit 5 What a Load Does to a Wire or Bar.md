---
materia: Aerospace Materials I
tema: "Unit 5: stress against yield and tensile strength, sizing against yielding and necking, reading the curve"
bank_id: B25
title: "What a given load does to a wire, a bar or a rod"
category: mt2_test_block
unit: 5
concepts:
  - u5-load-outcome-wire
  - u5-load-outcome-design
  - u5-curve-points-reading
difficulty: 2
origen: "Includes official exam question (MATERIALS_SECONDPARTIAL_2019.pdf, Q2) and practice items in the style of Part I of Assessment Test II. Data from Session 11, Slides 9-10, 12, 16 and 28-31."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-5
---

# Bank B25 — What a given load does to a wire, a bar or a rod

> [!info] Includes official exam questions
> Ten test questions in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong), combining an official exam question and bank practice items. Content: Session 11, Slides 9-10, 12, 16 and 28-31.

## Q25.1 Nickel wire under a 6000 N load

- id: B25-Q1
- concept_id: u5-load-outcome-wire
- format: what-happens
- asks: effect
- origin: official-exam
- check: 250 < 6000/(pi*2.5**2) < 310

A 6000 N force is applied to a 5 mm diameter nickel wire having a yield strength of 250 MPa and a tensile strength of 310 MPa. What will happen with the wire:

a) The wire will deform plastically and uniformly
b) The wire will fracture
c) The wire will experience necking
d) The wire will recover its original length when unloaded

### Answer

a

### Explanation

With $r = 2.5$ mm, $A_0 = \pi(2.5)^2 = 19.63$ mm², so the engineering stress is $\sigma = F/A_0 = 6000/19.63 = 305.6$ MPa (Session 11, Slide 9). Because $\sigma_y = 250\ \text{MPa} < 305.6\ \text{MPa} < \text{TS} = 310$ MPa, the wire is past yielding but below the tensile strength, so it undergoes uniform plastic deformation (Slides 10 and 30).

- b) Fracture occurs only after exceeding the tensile strength (310 MPa), which requires more than $310 \times 19.63 = 6087$ N.
- c) Necking begins only once the stress reaches the tensile strength of 310 MPa; at 305.6 MPa deformation is still uniform.
- d) Full elastic recovery occurs only below the yield strength (250 MPa); using diameter instead of radius would falsely give 76.4 MPa.

### Source

MATERIALS_SECONDPARTIAL_2019.pdf, p. 2, Question 2; Session 11, Slides 9-10 and 28-30.

## Q25.2 Length of a brass bar after unloading

- id: B25-Q2
- concept_id: u5-load-outcome-wire
- format: what-happens
- asks: application
- check: 345 < 30000/(pi*5**2) < 420

A brass bar of 10 mm diameter ($\sigma_y$ = 345 MPa, tensile strength 420 MPa) is loaded to 30 kN and then unloaded. What will its length be:

a) Longer than the original length
b) It cannot be measured, since the bar breaks
c) Equal to the original length
d) Shorter than the original length

### Answer

a

### Explanation

$\sigma = 30\,000/(\pi\cdot 5^2) = 382$ MPa (Session 11, Slide 9), between $\sigma_y = 345$ MPa and 420 MPa: the bar deforms plastically, and on unloading only the elastic part is recovered, so a permanent elongation remains (Slides 21 and 32).

- b) Fracture needs a stress above the tensile strength, 420 MPa; 382 MPa is below it.
- c) Full recovery needs a stress below the yield strength; the bar reached 382 MPa, above 345 MPa.
- d) Unloading recovers only the elastic strain; it cannot shorten the bar below its original length.

### Source

Session 11, Slides 9, 21, 28 and 32.

## Q25.3 Steel rod above its maximum load

- id: B25-Q3
- concept_id: u5-load-outcome-wire
- format: what-happens
- asks: calculation
- check: 22000/(pi*3**2) > 750

A 22 kN force is applied to a steel rod of 6.0 mm diameter with a yield strength of 600 MPa and a tensile strength of 750 MPa. What will happen to the rod:

a) The rod will stretch permanently but evenly
b) The rod will stay in the elastic zone
c) The rod will neck and keep holding the load
d) The rod will break

### Answer

d

### Explanation

$\sigma = 22\,000/(\pi\cdot 3.0^2) = 778$ MPa (Session 11, Slide 9), above the tensile strength of 750 MPa, the maximum nominal stress the rod can support (Slide 30): it fractures.

- a) This would need $600 < \sigma < 750$ MPa; the stress is 778 MPa.
- b) This is what the diameter used as the radius gives, 195 MPa; the real stress is four times larger.
- c) A neck can carry at most the maximum load, $750 \times \pi\cdot 3^2 = 21.2$ kN; 22 kN is more than that.

### Source

Session 11, Slides 9 and 28-31.

## Q25.4 One load on two copper wires

- id: B25-Q4
- concept_id: u5-load-outcome-wire
- format: what-happens
- asks: comparison
- check: 4000/(pi*2.5**2) > 200 > 4000/(pi*3**2)

The same 4.0 kN load hangs from a 5.0 mm and a 6.0 mm copper wire, both with $\sigma_y$ = 200 MPa. What will happen after unloading:

a) Only the 6.0 mm wire keeps a permanent elongation
b) Neither wire keeps a permanent elongation
c) Both wires keep a permanent elongation
d) Only the 5.0 mm wire keeps a permanent elongation

### Answer

d

### Explanation

$\sigma_{5} = 4000/(\pi\cdot 2.5^2) = 204$ MPa $> 200$ MPa (plastic) and $\sigma_{6} = 4000/(\pi\cdot 3^2) = 141$ MPa $< 200$ MPa (elastic) (Session 11, Slides 9-10); only the wire stressed beyond its yield strength keeps a plastic strain after unloading.

- a) Inverted: the thicker wire has the larger area and the lower stress, 141 MPa.
- b) The 5.0 mm wire is at 204 MPa, just above the yield strength of 200 MPa.
- c) The 6.0 mm wire is at 141 MPa, below the yield strength, so it recovers fully.

### Source

Session 11, Slides 9-10 and 21.

## Q25.5 Smallest diameter that avoids yielding

- id: B25-Q5
- concept_id: u5-load-outcome-design
- format: numeric
- asks: calculation
- calc: 2*sqrt(50000/450/pi)

A steel tie with a yield strength of 450 MPa must carry 50 kN without yielding. Determine its smallest diameter:

a) 5.95 mm
b) 10.5 mm
c) 11.9 mm
d) 111 mm

### Answer

c

### Explanation

To stay elastic, $\sigma = F/A_0 \le \sigma_y$ (Session 11, Slides 9-10): $A_0 = 50\,000/450 = 111.1$ mm² and $d = 2\sqrt{A_0/\pi} = 11.9$ mm.

- a) This is the radius of the required section, not its diameter.
- b) The section was taken as a square: $\sqrt{111}$ mm.
- d) This is the required area, 111 mm², given as a diameter.

### Source

Session 11, Slides 9-10 and 28.

## Q25.6 Effect of yield strength on minimum rod diameter

- id: B25-Q6
- concept_id: u5-load-outcome-design
- format: cause-effect
- asks: application

Referring to sizing a cylindrical tie rod to carry a fixed axial load $F$ without yielding, replacing the alloy with one that has four times the yield strength $\sigma_y$ allows the minimum required diameter $d_{\min}$ to:

a) decrease to one quarter of its original value
b) decrease to one half of its original value
c) decrease to one sixteenth of its original value
d) stay unchanged because minimum diameter depends only on Young's modulus

### Answer

b

### Explanation

To avoid yielding, $\sigma = F/A_0 \le \sigma_y$, giving $A_{\min} = \pi d_{\min}^2/4 = F/\sigma_y$ (Session 11, Slides 9-10 and 28). Thus $d_{\min} = \sqrt{4F/(\pi\sigma_y)} \propto 1/\sqrt{\sigma_y}$; quadrupling $\sigma_y$ reduces $d_{\min}$ by $\sqrt{4} = 2$ (to one half).

- a) This assumes diameter scales linearly as $1/\sigma_y$; it is the cross-sectional area $A_{\min}$ that drops by a factor of four.
- c) This squares the area factor instead of taking its square root.
- d) Young's modulus governs elastic stiffness (deflection), whereas the onset of yielding is governed by $\sigma_y$.

### Source

Session 11, Slides 9-10, 12 and 28.

## Q25.7 Sizing a bar on the tensile strength

- id: B25-Q7
- concept_id: u5-load-outcome-design
- format: true-statement
- asks: effect

A bar is sized so that its service stress equals its tensile strength. Which statement about the bar is TRUE?

a) It will deform permanently and start to neck in service
b) It will stay elastic up to the tensile strength
c) It will be safer than a bar sized on the yield strength
d) It will neck as soon as it reaches the yield strength

### Answer

a

### Explanation

The tensile strength is the maximum nominal stress and necking follows it (Session 11, Slide 30); it is above the yield strength, where permanent deformation begins (Slide 28). This is why design uses $\sigma_w = \sigma_y/N$ (Slide 29).

- b) The elastic zone ends at the yield strength, below the tensile strength.
- c) The design rule of the slides divides the yield strength by $N$, giving a lower stress, not a higher one.
- d) Necking begins at the tensile strength; at the yield strength the plastic deformation is still uniform.

### Source

Session 11, Slides 28-30.

## Q25.8 Point of tensile strength on the curve

- id: B25-Q8
- concept_id: u5-curve-points-reading
- format: diagram-reading
- asks: figure-reading

From the shown engineering stress-strain curve, indicate which marked point gives the tensile strength:

![[attachments/MAT-MT2/u5-curve-points.svg]]

a) Point D
b) Point C
c) Point B
d) Point A

### Answer

c

### Explanation

Session 11, Slide 30: the tensile strength is the maximum nominal stress the specimen supports, the highest point of the engineering curve: point B.

- a) D lies on the elastic line, where the stress is still proportional to the strain.
- b) C is the end of the curve, the fracture stress, which is below the maximum.
- d) A is where the straight elastic line ends, close to yielding.

### Source

Session 11, Slides 9 and 30-31.

## Q25.9 Curve of a ceramic

- id: B25-Q9
- concept_id: u5-curve-points-reading
- format: choose-figure
- asks: classification

Which picture describes the tensile stress-strain curve of a ceramic or a glass?

a) ![[attachments/MAT-MT2/u5-family-3.svg]]
b) ![[attachments/MAT-MT2/u5-family-1.svg]]
c) ![[attachments/MAT-MT2/u5-family-4.svg]]
d) ![[attachments/MAT-MT2/u5-family-2.svg]]

### Answer

d

### Explanation

Session 11, Slide 16: ceramics, glasses and concrete have a steep curve that breaks at a low strain with almost no plastic zone; the right picture is a straight line ending in fracture.

- a) This strongly curved response up to a very large strain is that of an elastomer.
- b) This curve rises to a maximum and falls with necking before fracture: a ductile metal.
- c) A peak, a long plateau and a final rise is the curve of a thermoplastic above its glass transition.

### Source

Session 11, Slide 16.

## Q25.10 Modulus read from the elastic line

- id: B25-Q10
- concept_id: u5-curve-points-reading
- format: diagram-reading
- asks: calculation
- check: abs(140/0.002/1000 - 70) < 1e-9

From the shown elastic part of a stress-strain curve, determine the Young's modulus of the material:

![[attachments/MAT-MT2/u5-elastic-slope.svg]]

a) 0.7 GPa
b) 70 GPa
c) 140 GPa
d) 70000 GPa

### Answer

b

### Explanation

Hooke's law (Session 11, Slide 12): $E = \sigma/\varepsilon = 140\ \text{MPa}/0.002 = 70\,000$ MPa $= 70$ GPa, the order of the modulus of aluminium (Slide 17).

- a) The strain was read in percent (0.2) and used as a fraction: $140/0.2 = 700$ MPa.
- c) The marked point was read at a strain of 0.001 instead of 0.002.
- d) The result in MPa, $140/0.002 = 70\,000$, was given as GPa.

### Source

Session 11, Slides 12 and 17.
