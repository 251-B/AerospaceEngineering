---
materia: Aerospace Materials I
tema: "Unit 5: tensile test"
bank_id: P14
title: "Ductility and true fracture stress of an aluminium alloy from the broken specimen"
category: mt2_problem
archetype: tensile-test
level: standard
unit: 5
difficulty: 2
points: 2.0
time_minutes: 15
official: false
origen: "Problem written for the bank in the style of the finals of January 2013 (question 7, parts d and e) and January 2014 (question 2, parts c and d) in MATERIALS_FINALEXAM_COMPILATION_2013-2017.pdf; not an official exercise. Verified with tools/materials_bank/verify_mt2.py"
tags:
  - problem-bank
  - midterm-2
  - tensile-test
  - ductility
  - true-stress
---

# Bank P14 — Ductility and true fracture stress of an aluminium alloy

> [!info] Practice item, not an official exercise
> Written for the bank in the style of parts (c) to (e) of the magnesium problems of the finals of January 2013 and January 2014. The data come as a narrative with no table: two loads and the measurements of the broken specimen. The path is: engineering stresses, %EL and %RA, then the true stress and true strain in the neck with the measured area, and why the constant-volume formulas would fail there. Method: Session 11, Slides 9, 30-33, 37-38. Every result is recomputed by tools/materials_bank/verify_mt2.py.

## Statement

A round specimen of an aluminium alloy, 8.00 mm in diameter, with gauge marks 40.00 mm apart, is pulled to fracture. The highest load recorded during the test is 21.5 kN, and the load at the instant of fracture is 17.8 kN. After the test the two halves are fitted together: the gauge marks are then 45.60 mm apart, and the diameter of the neck at the fracture surface is 6.10 mm.

![[attachments/MAT-MT2/p14-al-specimen.svg]]

## Setup

#### Data

| Quantity | Symbol | Value | In SI |
| :--- | :--- | ---: | ---: |
| Initial diameter | $d_0$ | 8.00 mm | $8.00\times10^{-3}$ m |
| Initial gauge length | $l_0$ | 40.00 mm | $4.000\times10^{-2}$ m |
| Maximum load | $F_{\max}$ | 21.5 kN | $2.15\times10^{4}$ N |
| Load at fracture | $F_f$ | 17.8 kN | $1.78\times10^{4}$ N |
| Gauge length after fracture | $l_f$ | 45.60 mm | $4.560\times10^{-2}$ m |
| Neck diameter after fracture | $d_f$ | 6.10 mm | $6.10\times10^{-3}$ m |

Areas, with the conversions written out ($1\ \text{mm}^2 = 10^{-6}\ \text{m}^2$):

$$A_0 = \frac{\pi d_0^2}{4} = \frac{\pi\,(8.00\ \text{mm})^2}{4} = \frac{\pi\times64.00\ \text{mm}^2}{4} = 50.27\ \text{mm}^2 = 5.027\times10^{-5}\ \text{m}^2$$

$$A_f = \frac{\pi d_f^2}{4} = \frac{\pi\,(6.10\ \text{mm})^2}{4} = \frac{\pi\times37.21\ \text{mm}^2}{4} = 29.22\ \text{mm}^2 = 2.922\times10^{-5}\ \text{m}^2$$

A load in N over an area in mm² gives MPa, because $1\ \text{N/mm}^2 = 10^{6}\ \text{N/m}^2$.

#### Model

- Engineering stress $\sigma = F/A_0$ [Session 11 Slide 9]; tensile strength = maximum engineering stress [Session 11 Slide 30]; fracture stress = stress at fracture [Session 11 Slide 31].
- Percent elongation after failure $EL\,(\%) = \dfrac{l_f - l_0}{l_0}\times100$ [Session 11 Slide 32]; percent reduction in area $RA\,(\%) = \dfrac{A_0 - A_f}{A_0}\times100$ [Session 11 Slide 33].
- True stress $\sigma_T = F/A_i$ with the instantaneous area; true strain $\varepsilon_T = \int dl/l$; after necking $\varepsilon_T = \ln(A_0/A) = 2\ln(D_0/D)$ [Session 11 Slides 37-38].
- Hypotheses: uniaxial load; the measurements after fracture are made with the load removed, so the elastic strain has been recovered [Session 11 Slide 32].

## (a) Calculate the tensile strength, the engineering fracture stress, the percent elongation and the percent reduction in area [1.0 pts]

### Hint

All engineering quantities use the original dimensions $A_0$ and $l_0$; only the numerators change.

### Checkpoint

- $\sigma_{TS} = 427.7$ MPa, $\sigma_f = 354.1$ MPa
- $EL = 14.0$ %
- $RA = 41.9$ %

### Solution

#### Tensile strength and engineering fracture stress

The tensile strength is the largest engineering stress [Session 11 Slide 30]; with $A_0$ fixed it corresponds to the largest load:

$$\sigma_{TS} = \frac{F_{\max}}{A_0} = \frac{21\,500\ \text{N}}{50.27\ \text{mm}^2} = 427.7\ \text{MPa}$$

The engineering fracture stress is the load at fracture over the same original area [Session 11 Slide 31]:

$$\sigma_f = \frac{F_f}{A_0} = \frac{17\,800\ \text{N}}{50.27\ \text{mm}^2} = 354.1\ \text{MPa}$$

$\sigma_f < \sigma_{TS}$: after the maximum the load falls because the specimen necks.

#### Percent elongation

The marks are measured on the broken, unloaded specimen, so the elastic strain has been recovered and $l_f - l_0$ is the plastic elongation [Session 11 Slide 32]:

$$EL\,(\%) = \frac{l_f - l_0}{l_0}\times100 = \frac{45.60\ \text{mm} - 40.00\ \text{mm}}{40.00\ \text{mm}}\times100 = \frac{5.60}{40.00}\times100 = 14.0\ \%$$

#### Percent reduction in area

The final area is the area of the fracture surface in the neck [Session 11 Slide 33]:

$$RA\,(\%) = \frac{A_0 - A_f}{A_0}\times100 = \frac{50.265 - 29.225}{50.265}\times100 = \frac{21.040}{50.265}\times100 = 41.9\ \%$$

The circle areas share the factor $\pi/4$, so the same number comes from the diameters alone: $RA = \left(1 - d_f^2/d_0^2\right)\times100 = (1 - 37.21/64.00)\times100 = 41.9$ %. As the slide warns, $EL\,(\%) \neq RA\,(\%)$ [Session 11 Slide 33].

## (b) Calculate the true stress and the true strain at fracture, and explain why $\sigma_T = \sigma(1+\varepsilon)$ cannot be used here [1.0 pts]

### Hint

At fracture the specimen has necked: use the measured neck area for the stress and the area ratio for the strain.

### Checkpoint

- $\sigma_{T,f} = 609.1$ MPa
- $\varepsilon_{T,f} = 0.542$
- $\sigma_f(1 + EL/100) = 403.7$ MPa underestimates it by about a third

### Solution

#### True stress at fracture with the measured area

The true stress is the load over the area that actually carries it at that instant [Session 11 Slide 37]. At fracture that area is the neck, $A_f$:

$$\sigma_{T,f} = \frac{F_f}{A_f} = \frac{17\,800\ \text{N}}{29.22\ \text{mm}^2} = 609.1\ \text{MPa}$$

Equivalently $\sigma_{T,f} = \sigma_f\,A_0/A_f = 354.1\ \text{MPa}\times1.720 = 609.1$ MPa [Session 11 Slide 38].

#### True strain at fracture from the area ratio

After necking the length between the marks no longer describes the strain of the neck, so the slide writes the true strain with the areas [Session 11 Slide 38]. With $A = \pi D^2/4$ the factor $\pi/4$ cancels in the ratio, and the logarithm of a square is twice the logarithm:

$$\varepsilon_{T,f} = \ln\frac{A_0}{A_f} = \ln\frac{d_0^2}{d_f^2} = 2\ln\frac{d_0}{d_f} = 2\ln\frac{8.00}{6.10} = 2\times0.2712 = 0.542$$

#### Why the uniform-deformation formulas fail here

The formulas $\sigma_T = \sigma(1+\varepsilon)$ and $\varepsilon_T = \ln(1+\varepsilon)$ of Slide 38 come from constant volume, $A_0 l_0 = A l$, applied to a gauge length that deforms **uniformly**, so that one strain $\varepsilon$ describes every cross-section. After the maximum load the strain concentrates in the neck: the average strain of the gauge length (0.14) is much smaller than the local strain at the fracture surface. Using them anyway gives

$$\sigma_f\,(1 + 0.140) = 354.1\ \text{MPa}\times1.140 = 403.7\ \text{MPa} \qquad \ln(1 + 0.140) = 0.131$$

against 609.1 MPa and 0.542 from the measured neck: the area ratio of the neck is $A_0/A_f = 1.720$, not $1 + \varepsilon = 1.140$. That is why the slide switches to $F_i/A_i$ and $\ln(A_0/A)$ after necking [Session 11 Slide 38].

## Interpretation

- **Physical meaning.** The engineering curve falls after the maximum (427.7 to 354.1 MPa) only because it divides by the original area; the metal in the neck is still hardening, and at fracture it carries 609.1 MPa. True stress above engineering stress and true strain different from the engineering one are the two signs the slide gives [Session 11 Slide 37].
- **Control checks.** $\sigma_f < \sigma_{TS} < \sigma_{T,f}$; $0 < RA < 100$ %; if the specimen had broken without necking ($d_f \to d_0$), $RA \to 0$ and $\sigma_{T,f} \to \sigma_f$, the behaviour of a brittle material.
- **Dimensions.** $F/A$ is N/m² = Pa; %EL and %RA are ratios of lengths and of areas, and $\ln(A_0/A_f)$ is the logarithm of a pure number, so both strains are dimensionless.
- **Common exam mistake.** Dividing the fracture load by the original area and calling it the true fracture stress, or computing %RA with the diameters instead of their squares ($1 - 6.10/8.00 = 23.8$ %, wrong).

## Verification

- A0 (mm2) | pi*8.00**2/4 | 50.27
- Af (mm2) | pi*6.10**2/4 | 29.22
- sigma_TS (MPa) | 21500/(pi*8.00**2/4) | 427.7
- sigma_f eng (MPa) | 17800/(pi*8.00**2/4) | 354.1
- EL (%) | (45.60-40.00)/40.00*100 | 14.0
- RA (%) | (1-6.10**2/8.00**2)*100 | 41.9
- area ratio | 8.00**2/6.10**2 | 1.720
- true fracture stress (MPa) | 17800/(pi*6.10**2/4) | 609.1
- true fracture strain | 2*ln(8.00/6.10) | 0.542
- ln(d0/df) | ln(8.00/6.10) | 0.2712
- uniform formula stress (MPa) | 17800/(pi*8.00**2/4)*(1+(45.60-40.00)/40.00) | 403.7
- uniform formula strain | ln(1+(45.60-40.00)/40.00) | 0.131
- wrong RA with diameters (%) | (1-6.10/8.00)*100 | 23.8

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
