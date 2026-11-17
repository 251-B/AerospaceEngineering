---
materia: Aerospace Materials I
tema: "Unit 5: loaded bar"
bank_id: P19
title: "Aluminium alloy specimen loaded beyond yield and unloaded"
category: mt2_problem
archetype: loaded-bar
level: standard
unit: 5
difficulty: 2
points: 2.0
time_minutes: 15
official: false
origen: "Problem written for the bank in the style of the final of June 2017 (question 5) in MATERIALS_FINALEXAM_2017_EXTRA.pdf; not an official exercise. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - loaded-bar
  - elastic-recovery
---

# Bank P19 — Aluminium alloy specimen loaded beyond yield and unloaded

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the final of June 2017 (question 5). Method: Session 11, Slides 9, 10, 12, 21 and 32. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

A cylindrical specimen of an aluminium alloy, 12.0 mm in diameter and with a gauge length of 50.0 mm, is pulled in a tensile machine up to a load of 40 kN. At that load the engineering strain measured on the gauge length is 0.035. The load is then removed completely, and later the same specimen is loaded again to 30 kN. Data of the alloy: $E = 69$ GPa, $\sigma_y = 275$ MPa (0.2 % offset).

## Setup

#### Data

| Quantity | Symbol | Value given | In SI |
| :--- | :--- | ---: | ---: |
| Initial diameter | $d_0$ | 12.0 mm | $12.0\times10^{-3}$ m |
| Gauge length | $l_0$ | 50.0 mm | $50.0\times10^{-3}$ m |
| Maximum load | $F_B$ | 40 kN | $40\times10^{3}$ N |
| Total strain at $F_B$ | $\varepsilon_B$ | 0.035 | dimensionless |
| Reloading force | $F_R$ | 30 kN | $30\times10^{3}$ N |
| Young's modulus | $E$ | 69 GPa | $69\times10^{9}$ Pa |
| Yield strength | $\sigma_y$ | 275 MPa | $275\times10^{6}$ Pa |

#### Model

- Engineering stress $\sigma = F/A_0$ and strain $\varepsilon = (l - l_0)/l_0$ [Session 11, Slide 9]; elastic zone for $\sigma < \sigma_y$, plastic for $\sigma > \sigma_y$ [Session 11, Slide 10].
- Hooke's law $\sigma = E\,\varepsilon$ for the elastic part [Session 11, Slide 12].
- Beyond yield the total strain is the sum of an elastic and a plastic part, $\varepsilon_t = \varepsilon_e + \varepsilon_p$; on unloading the elastic part is recovered along a line parallel to the elastic line and the plastic part remains [Session 11, Slide 32].
- **Extension** (idealisation, not stated on the slides): on reloading, the unloaded specimen follows the unloading line elastically up to the previous maximum stress before it yields again. The slides only state that cold work raises the yield strength [Session 12, Slide 5].
- Yielding is drawn, as an idealisation, at the end of the straight elastic line; the real 0.2 % offset value of 275 MPa lies on the curve at a strain of about 0.0060.
- Hypotheses: uniform uniaxial stress; the engineering stress uses the initial area $A_0$; the unloading is elastic with the same modulus $E$; the elastic reloading of part (c) rests on the idealisation marked **extension** above.

## (a) Show that the specimen deforms plastically at 40 kN and give its length under that load. [0.6 pts]

### Hint

Compare the stress with the yield strength. The strain at 40 kN is measured, so Hooke's law is not needed for the length.

### Checkpoint

- $A_0 = 1.131\times10^{-4}$ m², $\sigma_B = 353.7$ MPa $> 275$ MPa: plastic
- $l_B = 51.750$ mm

### Solution

#### Stress at the maximum load

With $d_0 = 12.0\times10^{-3}$ m:

$$A_0 = \frac{\pi d_0^2}{4} = \frac{\pi\,(12.0\times10^{-3}\ \text{m})^2}{4} = 1.131\times10^{-4}\ \text{m}^2$$

and with $F_B = 40\ \text{kN} = 40\times10^{3}$ N [Session 11, Slide 9]:

$$\sigma_B = \frac{F_B}{A_0} = \frac{40\times10^{3}\ \text{N}}{1.131\times10^{-4}\ \text{m}^2} = 3.537\times10^{8}\ \text{Pa} = 353.7\ \text{MPa}$$

#### Elastic or plastic

$\sigma_B = 353.7\ \text{MPa} > \sigma_y = 275\ \text{MPa}$, so the specimen is in the plastic zone [Session 11, Slide 10]. Hooke's law does not hold up to this point: the measured strain 0.035 is much larger than the elastic strain at yield, $\sigma_y/E = 275\times10^{6}/69\times10^{9} = 3.986\times10^{-3}$.

#### Length under the load

The strain under load is given, so the length comes straight from the definition $\varepsilon_B = (l_B - l_0)/l_0$. Multiplying by $l_0$ and adding $l_0$ to both sides:

$$l_B = l_0\,(1 + \varepsilon_B) = 50.0\ \text{mm}\times(1 + 0.035) = 51.750\ \text{mm}$$

## (b) Length of the specimen after the 40 kN load is removed. Draw the loading and unloading path. [0.8 pts]

### Hint

On unloading only the elastic part of the strain is recovered, along a line of slope $E$ that starts at the stress reached, not at the yield strength.

### Checkpoint

- Recovered elastic strain $\varepsilon_e = 5.126\times10^{-3}$
- Permanent strain $\varepsilon_p = 0.02987$
- Final length $l_P = 51.494$ mm (the specimen shortens by 0.256 mm on unloading)

### Solution

#### Split the total strain into its elastic and plastic parts

At point B of the curve the total strain is $\varepsilon_B = \varepsilon_e + \varepsilon_p$ [Session 11, Slide 32]. Unloading removes the stress from $\sigma_B$ to 0 along a straight line parallel to the elastic line, of slope $E$ [Session 11, Slide 32]. The strain recovered is therefore Hooke's law applied to the stress drop $\sigma_B - 0$:

$$\varepsilon_e = \frac{\sigma_B}{E} = \frac{353.7\times10^{6}\ \text{Pa}}{69\times10^{9}\ \text{Pa}} = 5.126\times10^{-3}$$

#### Permanent strain

Isolating the plastic part from $\varepsilon_B = \varepsilon_e + \varepsilon_p$ (subtract $\varepsilon_e$ from both sides):

$$\varepsilon_p = \varepsilon_B - \varepsilon_e = 0.035 - 5.126\times10^{-3} = 0.02987$$

#### Final length after unloading

The permanent strain is measured on the initial gauge length, so

$$l_P = l_0\,(1 + \varepsilon_p) = 50.0\ \text{mm}\times(1 + 0.02987) = 51.494\ \text{mm}$$

The specimen shortens on unloading by $l_B - l_P = 51.750 - 51.494 = 0.256$ mm, which is $\varepsilon_e\,l_0 = 5.126\times10^{-3}\times 50.0$ mm.

#### Loading and unloading path

![[attachments/MAT-MT2/p19-load-unload-path.svg]]

O to Y is the elastic line, with yielding idealised at its end (the 0.2 % offset value lies a little further along the curve); Y to B is the plastic loading up to 353.7 MPa at $\varepsilon = 0.035$; B to P is the unloading, parallel to OY, ending at the permanent strain 0.0299.

## (c) Length of the specimen when it is loaded again to 30 kN. [0.6 pts]

### Hint

Compare the new stress with the highest stress the specimen has already carried. Measure the strain from the original gauge length.

### Checkpoint

- $\sigma_R = 265.3$ MPa $< \sigma_B = 353.7$ MPa: the reloading runs back up the line PB, elastically
- $\varepsilon_R = 0.03372$, $l_R = 51.686$ mm

### Solution

#### Is the reloading elastic?

> [!note] Extension: reloading to the previous maximum
> The idealisation used here is not stated on the slides: a specimen unloaded from B climbs back along the unloading line PB elastically and yields again only when the stress reaches the previous maximum, 353.7 MPa. The slides only say that cold work raises the yield strength [Session 12, Slide 5].

With that idealisation, the reloading is elastic if the new stress stays below 353.7 MPa. The new stress is

$$\sigma_R = \frac{F_R}{A_0} = \frac{30\times10^{3}\ \text{N}}{1.131\times10^{-4}\ \text{m}^2} = 265.3\ \text{MPa} < 353.7\ \text{MPa}$$

so the specimen is elastic on the line PB (point R of the figure), even though 265.3 MPa is close to the original $\sigma_y = 275$ MPa.

#### Strain and length at R

The strain at R is the permanent strain plus the elastic strain of Hooke's law for $\sigma_R$:

$$\varepsilon_R = \varepsilon_p + \frac{\sigma_R}{E} = 0.02987 + \frac{265.3\times10^{6}\ \text{Pa}}{69\times10^{9}\ \text{Pa}} = 0.02987 + 3.844\times10^{-3} = 0.03372$$

$$l_R = l_0\,(1 + \varepsilon_R) = 50.0\ \text{mm}\times 1.03372 = 51.686\ \text{mm}$$

## Interpretation

- The elastic recovery, 0.256 mm, is only about 1/7 of the total elongation of 1.750 mm: in a ductile metal loaded well past yield most of the strain is permanent.
- Control cases: had the load stayed below $\sigma_y$, $\varepsilon_p = 0$ and the specimen would return to 50.0 mm; at R, setting $F_R = 0$ gives back $l_P$, and $F_R = 40$ kN gives back $l_B$, because $\varepsilon_p + \sigma_B/E = 0.035$.
- SI check: $\sigma/E$ is Pa/Pa, dimensionless, and it adds to $\varepsilon_p$, also dimensionless; $l = l_0(1+\varepsilon)$ is in metres.
- Common mistake: recovering $\sigma_y/E$ instead of $\sigma_B/E$ on unloading (that gives 51.551 mm), or computing the length under load with Hooke's law in the plastic zone.

## Verification

- A0 (m^2) | pi*(12.0e-3)**2/4 | 1.131e-4
- sigma_B (MPa) | 40e3/(pi*(12.0e-3)**2/4)/1e6 | 353.7
- eps at yield | 275e6/69e9 | 3.986e-3
- l_B (mm) | 50.0*(1+0.035) | 51.750
- eps_e | 40e3/(pi*(12.0e-3)**2/4)/69e9 | 5.126e-3
- eps_p | 0.035-40e3/(pi*(12.0e-3)**2/4)/69e9 | 0.02987
- l_P (mm) | 50.0*(1+0.035-40e3/(pi*(12.0e-3)**2/4)/69e9) | 51.494
- shortening (mm) | 50.0*40e3/(pi*(12.0e-3)**2/4)/69e9 | 0.256
- sigma_R (MPa) | 30e3/(pi*(12.0e-3)**2/4)/1e6 | 265.3
- eps_e at R | 30e3/(pi*(12.0e-3)**2/4)/69e9 | 3.844e-3
- eps_R | 0.035-40e3/(pi*(12.0e-3)**2/4)/69e9+30e3/(pi*(12.0e-3)**2/4)/69e9 | 0.03372
- l_R (mm) | 50.0*(1+0.035-10e3/(pi*(12.0e-3)**2/4)/69e9) | 51.686
- wrong l with sigma_y (mm) | 50.0*(1+0.035-275e6/69e9) | 51.551

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
