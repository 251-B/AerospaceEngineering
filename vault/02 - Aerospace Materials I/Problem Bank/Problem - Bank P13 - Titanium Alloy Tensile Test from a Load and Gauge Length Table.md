---
materia: Aerospace Materials I
tema: "Unit 5: tensile test"
bank_id: P13
title: "Titanium alloy tensile test from a load and gauge length table"
category: mt2_problem
archetype: tensile-test
level: standard
unit: 5
difficulty: 2
points: 2.0
time_minutes: 15
official: false
origen: "Problem written for the bank in the style of the finals of January 2013 (question 7) and January 2014 (question 2) in MATERIALS_FINALEXAM_COMPILATION_2013-2017.pdf (load and gauge-length table of a magnesium specimen); not an official exercise. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - tensile-test
  - young-modulus
  - yield-strength
---

# Bank P13 — Titanium alloy tensile test from a load and gauge length table

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the load and gauge-length tables of the finals of January 2013 and January 2014 (magnesium). Here the data are a table of raw readings, and the path is: table of engineering stress and strain, slope of the straight rows, 0.2 % offset line solved by linear interpolation between two rows, maximum load. Method: Session 11, Slides 9, 12, 28 and 30. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

A round specimen of a titanium alloy with a diameter of 10.0 mm and an initial gauge length of 50.000 mm is pulled in a uniaxial tension test. The machine records the load and the distance between the gauge marks:

| Row | Load $F$ (N) | Gauge length $l$ (mm) |
| ---: | ---: | ---: |
| 0 | 0 | 50.000 |
| 1 | 15 000 | 50.089 |
| 2 | 30 000 | 50.179 |
| 3 | 45 000 | 50.268 |
| 4 | 60 000 | 50.357 |
| 5 | 63 000 | 50.420 |
| 6 | 66 000 | 50.500 |
| 7 | 69 000 | 50.900 |
| 8 | 72 000 | 51.750 |
| 9 | 74 000 (maximum load) | 53.000 |
| 10 | 71 000 (fracture) | 54.600 |

## Setup

#### Data

| Quantity | Symbol | Value | In SI |
| :--- | :--- | ---: | ---: |
| Initial diameter | $d_0$ | 10.0 mm | $10.0\times10^{-3}$ m |
| Initial gauge length | $l_0$ | 50.000 mm | $5.0000\times10^{-2}$ m |
| Loads of the table | $F$ | 15 000 to 74 000 N | N |
| Offset of the conventional yield strength | $\varepsilon_{\text{off}}$ | 0.002 | (dimensionless) |

Initial cross-section, with the conversion to SI written out:

$$A_0 = \frac{\pi d_0^2}{4} = \frac{\pi\,(10.0\times10^{-3}\ \text{m})^2}{4} = \frac{\pi\times1.000\times10^{-4}\ \text{m}^2}{4} = 7.854\times10^{-5}\ \text{m}^2 = 78.54\ \text{mm}^2$$

Since $1\ \text{N/mm}^2 = 10^6\ \text{N/m}^2 = 1\ \text{MPa}$, a load in N divided by an area in mm² gives the stress directly in MPa.

#### Model

- Engineering stress and strain, defined with the original area and length [Session 11 Slide 9]: $\sigma = F/A_0$ and $\varepsilon = (l - l_0)/l_0$.
- Hooke's law in the elastic zone, $\sigma = E\,\varepsilon$; the Young's modulus $E$ is the slope of the straight part of the curve [Session 11 Slide 12].
- Conventional yield strength: the stress where the curve meets the line parallel to the elastic line drawn from $\varepsilon = 0.002$ [Session 11 Slide 28].
- Tensile strength: the maximum engineering stress the specimen supports [Session 11 Slide 30].
- Hypotheses: uniaxial stress, uniform over the gauge length up to the maximum load; between two rows of the table the curve is taken as a straight segment (linear interpolation).

## (a) Compute the engineering stress and strain of the rows and the modulus of elasticity of the alloy [0.7 pts]

### Hint

Divide each load by $A_0$ and each elongation by $l_0$; then check which rows keep the same ratio $\sigma/\varepsilon$.

### Checkpoint

- $A_0 = 78.54\ \text{mm}^2$
- Row 4: $\sigma = 763.9$ MPa, $\varepsilon = 0.00714$
- $E = 107.0$ GPa (rows 1 to 4 are the straight part)

### Solution

#### Engineering stress and strain of one row, written out

The idea is to remove the size of the specimen from the readings: the load per unit of original area and the elongation per unit of original length [Session 11 Slide 9]. For row 4:

$$\sigma_4 = \frac{F_4}{A_0} = \frac{60\,000\ \text{N}}{78.54\ \text{mm}^2} = 763.9\ \text{MPa}$$

$$\varepsilon_4 = \frac{l_4 - l_0}{l_0} = \frac{50.357\ \text{mm} - 50.000\ \text{mm}}{50.000\ \text{mm}} = \frac{0.357\ \text{mm}}{50.000\ \text{mm}} = 0.00714$$

#### The same operation for every row

The last column is the secant ratio $\sigma/\varepsilon$, which is constant only while Hooke's law holds:

| Row | $F$ (N) | $l - l_0$ (mm) | $\sigma$ (MPa) | $\varepsilon$ | $\sigma/\varepsilon$ (GPa) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 15 000 | 0.089 | 191.0 | 0.00178 | 107.3 |
| 2 | 30 000 | 0.179 | 382.0 | 0.00358 | 106.7 |
| 3 | 45 000 | 0.268 | 573.0 | 0.00536 | 106.9 |
| 4 | 60 000 | 0.357 | 763.9 | 0.00714 | 107.0 |
| 5 | 63 000 | 0.420 | 802.1 | 0.00840 | 95.5 |
| 6 | 66 000 | 0.500 | 840.3 | 0.01000 | 84.0 |
| 7 | 69 000 | 0.900 | 878.5 | 0.01800 | 48.8 |
| 8 | 72 000 | 1.750 | 916.7 | 0.03500 | 26.2 |
| 9 | 74 000 | 3.000 | 942.2 | 0.06000 | 15.7 |
| 10 | 71 000 | 4.600 | 904.0 | 0.09200 | 9.8 |

#### Pick the straight rows and average their slope

Rows 1 to 4 give the same ratio within the reading error of the last digit of $l$ (106.7 to 107.3 GPa); from row 5 on the ratio falls (95.5, 84.0 GPa), so the curve has left the straight line. The modulus is the slope of the straight part through the origin [Session 11 Slide 12], taken as the mean of the four secant ratios:

$$E = \frac{1}{4}\left(\frac{\sigma_1}{\varepsilon_1} + \frac{\sigma_2}{\varepsilon_2} + \frac{\sigma_3}{\varepsilon_3} + \frac{\sigma_4}{\varepsilon_4}\right) = \frac{107.3 + 106.7 + 106.9 + 107.0}{4}\ \text{GPa} = 106\,970\ \text{MPa} \approx 107.0\ \text{GPa}$$

(The sum is formed with the unrounded ratios.) Check: the slide's table gives $E = 107$ GPa for titanium [Session 11 Slide 17], so the readings are consistent with a titanium alloy.

![[attachments/MAT-MT2/p13-ti-curve.svg]]

## (b) Determine the yield strength with the 0.2 % offset method [0.8 pts]

### Hint

Write the offset line as $\sigma = E(\varepsilon - 0.002)$, find the two rows between which the curve passes from above it to below it, and intersect the offset line with the straight segment that joins those two rows.

### Checkpoint

- The crossing lies between rows 5 and 6
- Slope of that segment $m = 23\,873$ MPa
- $\varepsilon^* = 0.009814$, $\sigma_y = 835.9$ MPa

### Solution

#### Equation of the offset line

The conventional yield strength is read where the curve meets the line parallel to the elastic one, shifted to a plastic strain of 0.002 [Session 11 Slide 28]. Parallel means the same slope $E$; passing through $(0.002, 0)$ gives

$$\sigma_{\text{off}}(\varepsilon) = E\,(\varepsilon - 0.002)$$

#### Locate the crossing between two rows

The curve is above the offset line while $g = \sigma - E(\varepsilon - 0.002)$ is positive:

| Row | $\varepsilon$ | $\sigma$ (MPa) | $E(\varepsilon - 0.002)$ (MPa) | $g$ (MPa) |
| ---: | ---: | ---: | ---: | ---: |
| 4 | 0.00714 | 763.9 | 549.8 | 214.1 |
| 5 | 0.00840 | 802.1 | 684.6 | 117.5 |
| 6 | 0.01000 | 840.3 | 855.8 | -15.4 |

$g$ changes sign between rows 5 and 6, so the yield point lies on the segment that joins them.

#### Equation of the segment between rows 5 and 6

Its slope is the rise over the run of the two rows:

$$m = \frac{\sigma_6 - \sigma_5}{\varepsilon_6 - \varepsilon_5} = \frac{840.34 - 802.14}{0.01000 - 0.00840}\ \text{MPa} = \frac{38.20}{0.00160}\ \text{MPa} = 23\,873\ \text{MPa}$$

and the segment is $\sigma(\varepsilon) = \sigma_5 + m\,(\varepsilon - \varepsilon_5)$.

#### Intersect the two lines

At the crossing $\varepsilon = \varepsilon^*$ both lines give the same stress:

$$\sigma_5 + m\,(\varepsilon^* - \varepsilon_5) = E\,(\varepsilon^* - 0.002)$$

Expanding both sides and moving the terms in $\varepsilon^*$ to the right:

$$\sigma_5 - m\,\varepsilon_5 + 0.002\,E = (E - m)\,\varepsilon^*$$

Dividing by $(E - m)$:

$$\varepsilon^* = \frac{\sigma_5 - m\,\varepsilon_5 + 0.002\,E}{E - m} = \frac{802.14 - 200.54 + 213.94}{106\,970 - 23\,873} = \frac{815.55}{83\,097} = 0.009814$$

#### Yield strength

Substituting $\varepsilon^*$ in the offset line:

$$\sigma_y = E\,(\varepsilon^* - 0.002) = 106\,970\ \text{MPa}\times(0.009814 - 0.002) = 106\,970\ \text{MPa}\times0.007814 = 835.9\ \text{MPa}$$

Check on the other line: $\sigma_5 + m(\varepsilon^* - \varepsilon_5) = 802.14 + 23\,873\times0.001414 = 835.9$ MPa, the same value, and it lies between $\sigma_5 = 802.1$ and $\sigma_6 = 840.3$ MPa, as it must.

## (c) Give the tensile strength and compare it with the yield strength [0.5 pts]

### Hint

The original area does not change in the engineering stress, so the largest stress is at the largest load.

### Checkpoint

- $\sigma_{TS} = 942.2$ MPa (row 9)
- $\sigma_{TS}/\sigma_y = 1.127$

### Solution

#### Maximum engineering stress

The tensile strength is the maximum nominal stress the specimen supports [Session 11 Slide 30]. With $A_0$ fixed, the maximum of $F/A_0$ is at the maximum load, row 9:

$$\sigma_{TS} = \frac{F_{\max}}{A_0} = \frac{74\,000\ \text{N}}{78.54\ \text{mm}^2} = 942.2\ \text{MPa}$$

#### Comparison with the yield strength

$$\frac{\sigma_{TS}}{\sigma_y} = \frac{942.2\ \text{MPa}}{835.9\ \text{MPa}} = 1.127$$

The alloy hardens only about 13 % between yielding and the maximum load: a high-strength alloy with little strain hardening. After row 9 the load falls (row 10, 71 000 N) because the specimen necks [Session 11 Slide 30], so row 10 is not the tensile strength even though the specimen is longer.

## Interpretation

- **Order of magnitude.** $E = 107.0$ GPa matches the titanium value of the slide's table (107 GPa) [Session 11 Slide 17]; $\sigma_y$ of about 840 MPa and $\sigma_{TS}$ of about 940 MPa are those of a high-strength titanium alloy, far above an aluminium alloy.
- **Control checks.** The yield point lies after the last straight row (row 4) and before the maximum (row 9): $\varepsilon_4 = 0.00714 < \varepsilon^* = 0.009814 < \varepsilon_9 = 0.060$; and $\sigma_y < \sigma_{TS}$. If the offset were zero, the line would be the elastic line itself and the crossing would move back to the end of the straight part (about row 4): the offset is what makes the reading reproducible.
- **Dimensions.** $\sigma = F/A_0$ is N/m² = Pa; $\varepsilon$ is m/m, dimensionless; $E = \sigma/\varepsilon$ and $m$ are in Pa; in $\varepsilon^* = (\sigma_5 - m\varepsilon_5 + 0.002E)/(E - m)$ the numerator and denominator are both in Pa, so $\varepsilon^*$ is dimensionless, as a strain must be.
- **Common exam mistake.** Taking the yield strength as the stress of the last straight row (763.9 MPa) or as the stress at a total strain of 0.002 (on the elastic line, 214 MPa): the 0.2 % is a plastic strain, measured from the offset line, not from the origin.

## Verification

- A0 (mm2) | pi*10.0**2/4 | 78.54
- sigma row 4 (MPa) | 60000/(pi*10.0**2/4) | 763.9
- eps row 4 | (50.357-50.000)/50.000 | 0.00714
- E (GPa) | (15000/(pi*25)/(0.089/50)+30000/(pi*25)/(0.179/50)+45000/(pi*25)/(0.268/50)+60000/(pi*25)/(0.357/50))/4/1000 | 107.0
- slope rows 5-6 (MPa) | (66000-63000)/(pi*25)/((50.500-50.420)/50) | 23873
- eps star | (lambda E, s5, m: (s5-m*0.0084+0.002*E)/(E-m))((15000/(pi*25)/(0.089/50)+30000/(pi*25)/(0.179/50)+45000/(pi*25)/(0.268/50)+60000/(pi*25)/(0.357/50))/4, 63000/(pi*25), 3000/(pi*25)/0.0016) | 0.009814
- sigma_y (MPa) | (lambda E, s5, m: E*((s5-m*0.0084+0.002*E)/(E-m)-0.002))((15000/(pi*25)/(0.089/50)+30000/(pi*25)/(0.179/50)+45000/(pi*25)/(0.268/50)+60000/(pi*25)/(0.357/50))/4, 63000/(pi*25), 3000/(pi*25)/0.0016) | 835.9
- sigma_TS (MPa) | 74000/(pi*10.0**2/4) | 942.2
- TS/YS | (74000/(pi*25))/((lambda E, s5, m: E*((s5-m*0.0084+0.002*E)/(E-m)-0.002))((15000/(pi*25)/(0.089/50)+30000/(pi*25)/(0.179/50)+45000/(pi*25)/(0.268/50)+60000/(pi*25)/(0.357/50))/4, 63000/(pi*25), 3000/(pi*25)/0.0016)) | 1.127

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
