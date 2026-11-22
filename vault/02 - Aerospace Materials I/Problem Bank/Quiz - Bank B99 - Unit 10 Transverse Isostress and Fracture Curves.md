---
materia: Aerospace Materials I
tema: "Unit 10: transverse isostress loading, transverse modulus E2C, particle modulus bounds and longitudinal fracture stress-strain curves"
bank_id: B99
title: "Transverse isostress and fracture curves"
category: mt3_test_block
unit: 10
concepts:
  - u10-isostress-transverse-strain
  - u10-isostress-assumptions
  - u10-isostress-e2c-numeric
  - u10-isostress-matrix-control
  - u10-isostress-vs-isostrain-plot
  - u10-bounds-particle-exponent
  - u10-bounds-cu-w-plot
  - u10-curves-abc-identify
  - u10-curves-residual-fracture
  - u10-isostress-direction-anisotropy
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_THIRDPARTIAL_2020_V2.pdf, including Q9 of Paper B (2020) and Q9 of MATERIALS_FINALEXAM_2016_EXTRA_SOL.pdf. Content from Session 22 Slides 22-28 and Final Exam 2013 ORD Q3b."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-10
---

# Bank B99 — Transverse isostress and fracture curves

> [!info] Includes official exam questions
> Ten test questions written for the bank in the style of Part I of Assessment Test III, including Q9 of Paper B (2020) and Q9 of the June 2016 extraordinary final exam (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 22, Slides 22-28.

## Q99.1 Transverse loading of continuous-fibre composites

- id: B99-Q1
- concept_id: u10-isostress-transverse-strain
- format: what-happens
- asks: effect
- origin: official-exam

When stress is applied perpendicular to fibers in a continuous fibers reinforced composite:

a) Fibers are subjected to higher deformation
b) Matrix is subjected to higher deformation
c) Fibers are subjected to higher stresses
d) Matrix is subjected to higher stresses

### Answer

b

### Explanation

Assessment Test III, Paper B Q9 (`MATERIALS_THIRDPARTIAL_2020_V2.pdf`, p. 5) and Session 22, Slides 23-24: loading perpendicular to continuous fibres places the matrix and fibres in series (isostress), so $\sigma_{2C} = \sigma_f = \sigma_m$. Because $\varepsilon_f = \sigma_2/E'_f$ and $\varepsilon_m = \sigma_2/E_m$ with $E'_f \gg E_m$, the compliant matrix undergoes much higher strain ($\varepsilon_m > \varepsilon_f$).

- a) Reverses the stiffness effect: the much stiffer fibres stretch far less than the matrix under equal transverse stress.
- c) Violates series equilibrium in isostress loading, where both phases carry the same transverse stress $\sigma_2$.
- d) Likewise contradicts isostress equilibrium by claiming the matrix carries higher stress than the fibres.

### Source

MATERIALS_THIRDPARTIAL_2020_V2.pdf, p. 5 Q9; Session 22, Slides 23-24.

## Q99.2 Transverse isostress model assumptions and relations

- id: B99-Q2
- concept_id: u10-isostress-assumptions
- format: false-statement
- asks: definition

Which of the following statements regarding transverse (isostress) loading of a unidirectional continuous-fibre composite is FALSE:

a) The total transverse elongation equals the sum of the matrix and fibre elongations ($\Delta L_C = \Delta L_m + \Delta L_f$)
b) The overall transverse strain is the volume-weighted average $\varepsilon_{2C} = V_f\varepsilon_{2f} + (1 - V_f)\varepsilon_{2m}$
c) The derivation assumes the cross-sectional area perpendicular to the load remains unchanged as stress is applied
d) The fibres carry much larger transverse stress than the matrix while both experience identical transverse strain

### Answer

d

### Explanation

Session 22, Slides 23-24: transverse loading corresponds to isostress ($\sigma_{2C} = \sigma_f = \sigma_m$), not isostrain. Because the phases act in series, their stresses are equal while their strains differ inversely with modulus ($\varepsilon_m \gg \varepsilon_f$). Statement d describes longitudinal isostrain behaviour and is false for transverse loading.

- a) True: along the transverse loading path, displacements add in series ($\Delta L_C = \Delta L_m + \Delta L_f$, Slide 23).
- b) True: dividing $\Delta L_C$ by $L_C$ with $L_f = V_f L_C$ and $L_m = V_m L_C$ yields $\varepsilon_{2C} = V_f\varepsilon_{2f} + V_m\varepsilon_{2m}$ (Slide 23).
- c) True: Slide 23 explicitly states the assumption of unchanged cross-sectional area after the transverse stress is applied.

### Source

Session 22, Slides 23-24.

## Q99.3 Calculating the transverse modulus E2C

- id: B99-Q3
- concept_id: u10-isostress-e2c-numeric
- format: numeric
- asks: calculation
- calc: 1 / (0.25 / 390.0 + 0.75 / 3.0)

A unidirectional composite contains 25 vol% continuous carbon fibres ($E_f = 390$ GPa) in an epoxy matrix ($E_m = 3.0$ GPa). Assuming isotropic fibre properties ($E'_f = E_f$), what is its transverse elastic modulus $E_{2C}$?

a) 99.8 GPa
b) 11.8 GPa
c) 3.99 GPa
d) 2.25 GPa

### Answer

c

### Explanation

Session 22, Slide 24 (and June 2014 extraordinary final, Q2a): under transverse isostress, $1/E_{2C} = V_f/E'_f + V_m/E_m = 0.25/390.0 + 0.75/3.0 = 0.000641 + 0.250000 = 0.250641\text{ GPa}^{-1}$, so $E_{2C} = 3.99\text{ GPa}$.

- a) Applies the longitudinal isostrain rule of mixtures $E_{1C} = 0.25(390) + 0.75(3.0) = 99.75\text{ GPa}$ instead of the transverse harmonic mean.
- b) Swaps the volume fractions in the harmonic formula, computing $[0.75/390.0 + 0.25/3.0]^{-1} = 11.7\text{ GPa}$.
- d) Multiplies $E_m V_m = 3.0 \times 0.75 = 2.25\text{ GPa}$ instead of dividing by $V_m$ in the matrix-controlled approximation $E_2 \approx E_m/V_m = 4.00\text{ GPa}$.

### Source

Session 22, Slide 24; MATERIALS_FINALEXAM_2014_EXTRA.pdf, p. 3 Q2a.

## Q99.4 Matrix dominance in transverse stiffness

- id: B99-Q4
- concept_id: u10-isostress-matrix-control
- format: cause-effect
- asks: cause

For typical structural fibre-polymer composites with $V_f = 50\text{–}60\%$ and $E_f \gg E_m$, the transverse modulus $E_{2C}$ stays close to $E_m/V_m$ (only about twice $E_m$) because:

a) the $V_f/E'_f$ compliance term is negligible in $1/E_{2C} = V_f/E'_f + V_m/E_m$, leaving the compliant matrix to control deformation
b) longitudinal fibres carry half the transverse stress in shear, forcing $E_{2C}$ to equal $2E_m$
c) the matrix yields plastically at zero stress perpendicular to the fibres, eliminating fibre stiffening
d) transverse loading triggers interfacial debonding before any elastic strain occurs in the matrix

### Answer

a

### Explanation

Session 22, Slide 24: when $E'_f \gg E_m$, $V_f/E'_f \ll V_m/E_m$ in $1/E_{2C} = V_f/E'_f + V_m/E_m$, so $1/E_{2C} \approx V_m/E_m$ and $E_2 \approx E_m/V_m$. Consequently, at $V_f = 50\text{–}60\%$ ($V_m = 0.40\text{–}0.50$), the transverse modulus is only roughly 2 to 2.5 times $E_m$ because the soft matrix dominates series compliance.

- b) Invents a shear-halving argument; the factor of $\sim 2$ comes purely from $1/V_m = 1/0.50 = 2$ in the series compliance sum.
- c) Wrongly assumes instant zero-stress plasticity; the micromechanical formula is derived in the linear elastic regime.
- d) Confuses elastic micromechanics (assuming a perfect interface) with post-yield failure processes.

### Source

Session 22, Slide 24; Session 21, Slide 37.

## Q99.5 Reading the isostrain vs isostress modulus curves

- id: B99-Q5
- concept_id: u10-isostress-vs-isostrain-plot
- format: diagram-reading
- asks: figure-reading

The plot compares longitudinal (isostrain) and transverse (isostress) elastic moduli for an E-glass/epoxy composite ($E_f = 72.4\times 10^3$ MPa, $E_m = 6.9\times 10^3$ MPa) versus fibre volume fraction $v_f$. At $v_f = 0.5$, how does the isostrain modulus compare with the isostress modulus?

![[attachments/T10/s22-fibreglass-epoxy-modulus.png]]

a) Both curves converge to the same value near $40\times 10^3$ MPa at $v_f = 0.5$
b) The isostress curve sits above the isostrain line until $v_f$ approaches $0.8$
c) The isostrain modulus is roughly $12.6\times 10^3$ MPa and the isostress modulus is roughly $39.7\times 10^3$ MPa
d) The isostrain modulus is roughly $39.7\times 10^3$ MPa, more than three times the isostress value of about $12.6\times 10^3$ MPa

### Answer

d

### Explanation

Session 22, Slide 25: the straight upper line (isostrain) gives $E_1(0.5) = 0.5(72.4) + 0.5(6.9) = 39.65\times 10^3$ MPa, whereas the concave lower curve (isostress) rises very gently near $E_m$ at low-to-moderate $v_f$, giving $E_2(0.5) = [0.5/72.4 + 0.5/6.9]^{-1} = 12.60\times 10^3$ MPa (less than a third of $E_1$).

- a) The two curves agree only at the pure-phase endpoints $v_f = 0$ and $v_f = 1$, diverging widest near mid-fractions.
- b) Reverses the upper and lower curves: the straight isostrain line is strictly above the isostress curve for all $0 < v_f < 1$.
- c) Swaps the numerical values of the isostrain and isostress curves at $v_f = 0.5$.

### Source

Session 22, Slide 25.

## Q99.6 Upper and lower bounds for particulate composites

- id: B99-Q6
- concept_id: u10-bounds-particle-exponent
- format: topic-true
- asks: comparison

Referring to the power-law approximation $E_C^{\,n} = v_l E_l^{\,n} + v_h E_h^{\,n}$ for composites with uniformly dispersed particles ($l$: lower-modulus phase, $h$: higher-modulus phase), which one of the following statements is TRUE:

a) Setting $n = 1$ gives the lower bound (isostress), while setting $n = -1$ gives the upper bound (isostrain)
b) Measured moduli of isotropic particle composites always coincide exactly with the upper bound $n = 1$
c) Setting $n = 1$ gives the upper bound $E_l v_l + E_h v_h$, and setting $n = -1$ gives the lower bound $E_h E_l / (v_h E_l + v_l E_h)$
d) The rule of mixtures gives exact upper and lower bounds only for density, while elastic moduli always exceed $n = 1$

### Answer

c

### Explanation

Session 22, Slides 27-28: in $E_C^{\,n} = v_l E_l^{\,n} + v_h E_h^{\,n}$, $n = 1$ recovers the linear arithmetic average (isostrain upper bound $E_l v_l + E_h v_h$), and $n = -1$ recovers the harmonic average (isostress lower bound $E_h E_l / (v_h E_l + v_l E_h)$). Semi-empirical models such as Halpin-Tsai (extension) and experimental particulate moduli fall between these bounds.

- a) Inverts the signs of $n$: $n = +1$ is the stiffest (isostrain) upper bound, whereas $n = -1$ is the softest (isostress) lower bound.
- b) Spherical/equiaxed particles do not carry continuous load in parallel like fibres, so measured moduli lie between the bounds rather than on $n = 1$.
- d) Density follows the exact linear volume average $\rho_c = \sum f_i\rho_i$, while elastic moduli cannot exceed the Voigt upper bound $n = 1$.

### Source

Session 22, Slides 27-28.

## Q99.7 Tungsten-reinforced copper modulus bounds

- id: B99-Q7
- concept_id: u10-bounds-cu-w-plot
- format: diagram-reading
- asks: figure-reading

The plot shows the experimental elastic modulus of a copper matrix reinforced with tungsten particles alongside the upper and lower theoretical curves. At 60 vol% tungsten, where do the measured data lie?

![[attachments/T10/s22-tungsten-copper-modulus.png]]

a) Between the lower bound (~200 GPa) and the upper bound (~253 GPa), clustering around 225-255 GPa
b) Below the lower bound, near 150 GPa, because tungsten particles create pores in copper
c) Strictly above the upper bound, near 320 GPa, due to particle dispersion hardening of copper
d) Independent of tungsten concentration, staying near 115 GPa across the entire composition range

### Answer

a

### Explanation

Session 22, Slide 28: reading the plot at 60 vol% W ($E_{Cu} \approx 115$ GPa, $E_W \approx 345$ GPa), the blue lower bound lies near 200 GPa (192-203 GPa) and the red upper bound lies near 253 GPa. The green experimental data points sit within this bracket, mostly between about 225 and 255 GPa.

- b) Misreads the vertical axis: no data point at 60 vol% W falls below the blue lower-bound curve near 150 GPa.
- c) Misreads the upper bound: 320 GPa is only reached above 85 vol% W, whereas at 60 vol% W the points stay at or below ~255 GPa.
- d) Ignores the clear upward slope of both bounds and experimental points from pure Cu (~115 GPa) to pure W (~345 GPa).

### Source

Session 22, Slide 28.

## Q99.8 Identifying fibre, composite, and matrix curves

- id: B99-Q8
- concept_id: u10-curves-abc-identify
- format: identify
- asks: classification
- origin: official-exam

Three tensile stress-strain curves A, B, and C are recorded for a unidirectional continuous-fibre polymer composite and its two separate constituents:
- Curve A rises steeply and linearly to brittle fracture at low strain.
- Curve B rises with an intermediate slope, drops abruptly at the fracture strain of A, and continues along a low plateau before fracturing at the failure strain of C.
- Curve C has the lowest initial slope, yields at low stress, and reaches a higher final fracture stress than the tail of B.

Which option identifies curves A, B, and C, in that order?

a) Composite material, reinforcement fibres, polymer matrix
b) Reinforcement fibres, composite material, polymer matrix
c) Polymer matrix, composite material, reinforcement fibres
d) Reinforcement fibres, polymer matrix, composite material

### Answer

b

### Explanation

June 2016 extraordinary final exam, Q9a (and Session 22, Slide 26): brittle reinforcing fibres have the highest modulus and strength with linear-elastic behaviour to failure (curve A); the unreinforced ductile matrix has the lowest modulus, yields early, and stretches to high strain (curve C); the composite displays an intermediate slope $E_{1C}$, drops sharply when the fibres break, and finishes on a matrix-carried residual tail (curve B).

- a) Swaps the steep brittle fibre line (A) with the composite curve showing the two-stage drop (B).
- c) Completely reverses the stiffness and ductility order of fibres (A) and matrix (C).
- d) Swaps the two-stage composite curve (B) with the smooth yielding curve of the unreinforced polymer matrix (C).

### Source

MATERIALS_FINALEXAM_2016_EXTRA_SOL.pdf, pp. 4-5 Q9a; Session 22, Slide 26.

## Q99.9 Residual composite fracture stress vs matrix strength

- id: B99-Q9
- concept_id: u10-curves-residual-fracture
- format: diagram-reading
- asks: cause
- origin: official-exam

In the longitudinal tensile stress-strain diagram shown for a unidirectional fibre composite and its constituents, why is the final fracture stress of the unreinforced matrix curve higher than the final fracture stress of the composite tail after all fibres have broken?

![[attachments/T10/s22-fibre-fracture-stress-strain.png]]

a) Broken fibres impose a compressive thermal residual stress that cancels part of the matrix yield strength
b) After fibre fracture, the matrix carries the applied load over an enlarged effective area $(1 + V_f)A_C$
c) Matrix yielding raises its elastic modulus above the composite rule-of-mixtures modulus prior to final rupture
d) Once the brittle fibres break, only the matrix fraction $(1 - V_f)$ supports load, leaving a residual strength $\sigma_m(1 - V_f) < \sigma_m$

### Answer

d

### Explanation

June 2016 extraordinary final exam, Q9b (and Session 22, Slide 26): once the brittle fibres fracture at their failure strain, they cease carrying tensile load across the fracture plane and behave like empty holes. Only the matrix cross-sectional fraction $V_m = (1 - V_f)$ remains active, so the composite fails at $\sigma_C = \sigma_m(1 - V_f)$, which is lower than the unreinforced matrix strength $\sigma_m$.

- a) Attributes the drop to compressive thermal stress rather than loss of load-bearing fibre cross-section.
- b) Inverts the effective area change: broken fibres reduce the active load-bearing area to $(1 - V_f)A_C$, not $(1 + V_f)A_C$.
- c) Wrongly claims matrix yielding raises stiffness, which cannot explain why the composite fails at a lower stress than pure matrix.

### Source

MATERIALS_FINALEXAM_2016_EXTRA_SOL.pdf, pp. 4-5 Q9b; Session 22, Slide 26.

## Q99.10 Effect of rotating load from 0° to 90°

- id: B99-Q10
- concept_id: u10-isostress-direction-anisotropy
- format: complete-sentence
- asks: comparison

Rotating the applied tensile load on a continuous aligned carbon/epoxy ply from parallel (0°) to perpendicular (90°) to the fibres causes both stiffness and strength to drop sharply because:

a) the load shifts from fibre-dominated parallel sharing (isostrain) to matrix-dominated series compliance (isostress) and transverse interface weakness
b) the fibre volume fraction decreases automatically by a factor of $(1 - V_f)$ whenever the load axis rotates
c) carbon fibres deform plastically under transverse compression before carrying any tensile stress
d) the epoxy matrix switches from crosslinked thermoset behaviour to uncrosslinked thermoplastic flow

### Answer

a

### Explanation

January 2013 ordinary final exam, Q3b (and Session 21, Slide 41; Session 22, Slides 22-24): at 0° the stiff fibres work in parallel (isostrain) and carry over 95 % of the load, whereas at 90° fibres and matrix act in series (isostress), so the low-modulus matrix governs stiffness ($E_{2C} \approx E_m/V_m$) and transverse tensile failure occurs easily along the matrix or fibre-matrix interface.

- b) Treats volume fraction $V_f$ as direction-dependent; $V_f$ is a fixed material composition independent of loading angle.
- c) Carbon fibres are brittle and do not yield plastically; transverse drop stems from matrix compliance and weak transverse load paths.
- d) Matrix chemical crosslinks do not break or convert into thermoplastic chains merely by changing loading direction.

### Source

MATERIALS_FINALEXAM_2013_ORD.pdf, p. 1 Q3b; Session 21, Slide 41; Session 22, Slides 22-24.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
