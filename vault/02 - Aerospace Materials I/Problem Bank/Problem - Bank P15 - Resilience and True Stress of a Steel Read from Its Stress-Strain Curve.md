---
materia: Aerospace Materials I
tema: "Unit 5: tensile test"
bank_id: P15
title: "Resilience and true stress of a steel read from its stress-strain curve"
category: mt2_problem
archetype: tensile-test
level: standard
unit: 5
difficulty: 2
points: 2.0
time_minutes: 15
official: false
origen: "Problem written for the bank in the style of the final of January 2014 (question 2, parts b and d: modulus of resilience, true stress and true strain at a given engineering stress) and of the curves of June 2015 (question 3 d) in MATERIALS_FINALEXAM_COMPILATION_2013-2017.pdf; not an official exercise. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - tensile-test
  - resilience
  - true-stress
---

# Bank P15 — Resilience and true stress of a steel read from its curve

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the January 2014 final (resilience; true stress and strain at a point of the curve). Here every datum is read from a drawn curve, and the two formulas the final applies directly are derived: the modulus of resilience as an integral with Barrow's rule, the true strain as an integral and the true stress from constant volume. Method: Session 11, Slides 9, 12, 28, 30, 35, 37-38. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

The figure shows the engineering stress-strain curve of a steel, drawn to fracture (left), and the start of the same test enlarged (right). The marked points are: A on the straight part, Y where the dashed line parallel to the straight part from $\varepsilon = 0.002$ meets the curve, B on the rising part, U at the maximum and F at fracture.

![[attachments/MAT-MT2/p15-steel-curve.svg]]

## Setup

#### Data

Values read from the figure: A, B and Y have dashed projections that end on a printed axis value; U lies on the 0.15 and 600 gridlines; F is at (0.25, 500) and is not needed.

| Point | What it is | Strain $\varepsilon$ | Stress $\sigma$ (MPa) | In SI |
| :--- | :--- | ---: | ---: | ---: |
| A | point of the straight part (right panel) | 0.0015 | 310 | $3.10\times10^{8}$ Pa |
| Y | crossing with the 0.2 % offset line (right panel) | read below | 450 | $4.50\times10^{8}$ Pa |
| B | rising part, before the maximum (left panel) | 0.08 | 560 | $5.60\times10^{8}$ Pa |
| U | maximum of the curve (left panel) | 0.15 | 600 | $6.00\times10^{8}$ Pa |

#### Model

- Hooke's law $\sigma = E\varepsilon$ on the straight part; $E$ is its slope [Session 11 Slide 12].
- Conventional yield strength at the crossing with the line parallel to the elastic one from $\varepsilon = 0.002$ [Session 11 Slide 28].
- Modulus of resilience: energy per unit volume up to yielding, $U_r = \int_0^{\varepsilon_y}\sigma\,d\varepsilon$ [Session 11 Slide 35].
- True stress $\sigma_T = F/A_i$ and true strain $\varepsilon_T = \int_{l_0}^{l} dl/l$ [Session 11 Slide 37]; before necking the volume is constant, $A_0 l_0 = A_i l_i$ [Session 11 Slide 38].
- Hypothesis for $U_r$: as on Slide 35, the elastic region is taken as linear up to $\sigma_y$ (the small rounding of the curve between about 380 and 450 MPa is neglected).

## (a) Read the modulus of elasticity and the yield strength, and derive and calculate the modulus of resilience [1.0 pts]

### Hint

The slope of the straight part comes from one point of it and the origin. The resilience is the area under the elastic line from zero to the yield strain: write it as an integral of $E\varepsilon$.

### Checkpoint

- $E = 206.7$ GPa
- $\sigma_y = 450$ MPa, $\varepsilon_y = \sigma_y/E = 0.002177$
- $U_r = 0.490$ MPa $= 0.490$ MJ/m³

### Solution

#### Modulus of elasticity from point A

The straight part passes through the origin and through A, and Hooke's law says its slope is $E$ [Session 11 Slide 12]:

$$E = \frac{\sigma_A - 0}{\varepsilon_A - 0} = \frac{310\ \text{MPa}}{0.0015} = 206\,667\ \text{MPa} = 206.7\ \text{GPa}$$

This agrees with the steel value of the slide's table, 207 GPa [Session 11 Slide 17].

#### Yield strength from point Y

The yield strength is the stress at the crossing of the curve with the offset line [Session 11 Slide 28]; the horizontal projection of Y ends at 450 on the stress axis:

$$\sigma_y = 450\ \text{MPa}$$

Check of the reading: on the offset line $\sigma = E(\varepsilon - 0.002)$, so the strain of Y must be $\varepsilon_Y = 0.002 + \sigma_y/E = 0.002 + 450/206\,667 = 0.004177$, which is where Y sits in the right panel (just to the right of the 0.004 gridline).

#### Elastic strain at the yield strength

Treating the elastic region as linear up to $\sigma_y$ (Slide 35) and isolating the strain from Hooke's law $\sigma_y = E\,\varepsilon_y$:

$$\varepsilon_y = \frac{\sigma_y}{E} = \frac{450\ \text{MPa}}{206\,667\ \text{MPa}} = 0.002177$$

#### Modulus of resilience as the area under the elastic line

The resilience is the energy absorbed per unit volume while the material deforms elastically, the area under the curve up to the yield point [Session 11 Slide 35]. In the elastic region $\sigma = E\varepsilon$, so

$$U_r = \int_0^{\varepsilon_y}\sigma\,d\varepsilon = \int_0^{\varepsilon_y}E\,\varepsilon\,d\varepsilon$$

$E$ is a constant and leaves the integral; an antiderivative of $\varepsilon$ is $\varepsilon^2/2$ (its derivative is $2\varepsilon/2 = \varepsilon$). Barrow's rule with the limits substituted:

$$U_r = E\left[\frac{\varepsilon^2}{2}\right]_0^{\varepsilon_y} = E\left(\frac{\varepsilon_y^2}{2} - \frac{0^2}{2}\right) = \frac{E\,\varepsilon_y^2}{2}$$

Replacing $\varepsilon_y = \sigma_y/E$: $U_r = \dfrac{E}{2}\,\dfrac{\sigma_y^2}{E^2} = \dfrac{\sigma_y^2}{2E}$, the formula of the slide, which is also the area of the triangle $\tfrac12\sigma_y\varepsilon_y$.

#### Numerical value

$$U_r = \frac{\sigma_y^2}{2E} = \frac{(450\ \text{MPa})^2}{2\times206\,667\ \text{MPa}} = \frac{202\,500}{413\,333}\ \text{MPa} = 0.490\ \text{MPa}$$

Since $1\ \text{MPa} = 10^6\ \text{N/m}^2 = 10^6\ \text{N·m/m}^3 = 1\ \text{MJ/m}^3$, each cubic metre of this steel stores 0.490 MJ of recoverable elastic energy before it yields. Check with the triangle: $\tfrac12\times450\ \text{MPa}\times0.002177 = 0.490$ MPa.

## (b) Calculate the true stress and the true strain at point B, deriving the formulas you use, and say why they cannot be used after point U [1.0 pts]

### Hint

Write the true strain as the integral of $dl/l$, and use constant volume, $A_0 l_0 = A l$, to replace the instantaneous area by the length.

### Checkpoint

- $\varepsilon_{T,B} = \ln(1.08) = 0.0770$
- $\sigma_{T,B} = 560 \times 1.08 = 604.8$ MPa
- Valid only up to U ($\varepsilon = 0.15$), where necking starts

### Solution

#### True strain as a sum of small increments

The true strain adds each small elongation $dl$ divided by the length $l$ the specimen has at that moment [Session 11 Slide 37]:

$$\varepsilon_T = \int_{l_0}^{l}\frac{dl}{l}$$

An antiderivative of $1/l$ is $\ln l$. Barrow's rule with the limits substituted:

$$\varepsilon_T = \left[\ln l\right]_{l_0}^{l} = \ln l - \ln l_0 = \ln\frac{l}{l_0}$$

Since $\varepsilon = (l - l_0)/l_0$, the ratio is $l/l_0 = (l_0 + l - l_0)/l_0 = 1 + \varepsilon$, and

$$\varepsilon_T = \ln(1 + \varepsilon)$$

#### True stress from constant volume

Plastic deformation does not change the volume, and before necking the specimen deforms uniformly, so the volume of the gauge length is the same at every instant [Session 11 Slide 38]:

$$A_0\,l_0 = A_i\,l_i$$

Isolating the instantaneous area: $A_i = A_0\,l_0/l_i$. The true stress is the load over that area [Session 11 Slide 37]:

$$\sigma_T = \frac{F}{A_i} = \frac{F}{A_0\,l_0/l_i} = \frac{F}{A_0}\cdot\frac{l_i}{l_0} = \sigma\,(1 + \varepsilon)$$

using again $l_i/l_0 = 1 + \varepsilon$.

#### Values at point B

Point B is read at $\varepsilon_B = 0.08$, $\sigma_B = 560$ MPa:

$$\varepsilon_{T,B} = \ln(1 + 0.08) = \ln 1.08 = 0.0770$$

$$\sigma_{T,B} = \sigma_B\,(1 + \varepsilon_B) = 560\ \text{MPa}\times1.08 = 604.8\ \text{MPa}$$

As Slide 37 predicts, $\sigma_T > \sigma$ (604.8 > 560 MPa) and $\varepsilon_T < \varepsilon$ (0.0770 < 0.08). The cross-section at B has shrunk by the factor $A_i/A_0 = 1/1.08 = 0.926$.

#### Why not after point U

Point U is the maximum of the curve, the tensile strength (600 MPa), and necking follows it [Session 11 Slide 30]. From U on the deformation concentrates in the neck: the gauge length no longer has one area, $A_0 l_0 = A_i l_i$ with a single $A_i$ fails, and $\sigma(1+\varepsilon)$ and $\ln(1+\varepsilon)$ no longer describe the neck. After necking the slide uses the measured area, $\sigma_T = F_i/A_i$ and $\varepsilon_T = \ln(A_0/A) = 2\ln(D_0/D)$ [Session 11 Slide 38], so the diameter of the neck would have to be measured (for example at F).

## Interpretation

- **Physical meaning.** $U_r = 0.490$ MJ/m³ is small next to the area under the whole curve (the toughness: a mean stress of about 530 MPa over a strain of 0.25 gives roughly $530\ \text{MPa}\times0.25 \approx 130$ MJ/m³): a structural steel absorbs almost all its energy plastically. A spring material needs high $\sigma_y$ and low $E$ [Session 11 Slide 35].
- **Limiting case.** For small strains $\ln(1+\varepsilon) \approx \varepsilon$ and $1+\varepsilon \approx 1$: at A ($\varepsilon = 0.0015$) the true stress exceeds the engineering one by 0.15 % and the true strain is smaller by about 0.075 %; at B the stresses differ by 8 % and the strains by about 3.8 % (0.0770 against 0.08). The distinction matters only in the plastic range.
- **Dimensions.** $\int\sigma\,d\varepsilon$ is Pa × (dimensionless) = Pa = J/m³; $\sigma_y^2/E$ is Pa²/Pa = Pa; $\ln(l/l_0)$ is the logarithm of a pure number; $\sigma(1+\varepsilon)$ is Pa.
- **Common exam mistake.** Taking $\varepsilon_y = 0.002$ or $\varepsilon_Y = 0.004177$ (the strain of the crossing, which includes the plastic offset) in the resilience: $U_r$ uses only the elastic strain $\sigma_y/E$.

## Verification

- E (GPa) | 310/0.0015/1000 | 206.7
- eps_y | 450/(310/0.0015) | 0.002177
- eps at Y | 0.002+450/(310/0.0015) | 0.004177
- U_r (MPa) | 450**2/(2*310/0.0015) | 0.490
- U_r triangle (MPa) | 0.5*450*450/(310/0.0015) | 0.490
- true strain B | ln(1+0.08) | 0.0770
- true stress B (MPa) | 560*(1+0.08) | 604.8
- area ratio at B | 1/(1+0.08) | 0.926

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
