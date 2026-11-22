---
materia: Aerospace Materials I
tema: "Unit 9: temperature and strain rate effects, viscoelastic creep and stress relaxation, log Er vs T regimes, and shifts with MW, crosslinking and crystallinity"
bank_id: B87
title: "Temperature, strain rate and viscoelasticity"
category: mt3_test_block
unit: 9
concepts:
  - u9-temp-strain-rate-effect
  - u9-temp-pmma-curve
  - u9-strain-rate-pvc-curve
  - u9-visco-time-temp-equiv
  - u9-visco-creep-vs-relaxation
  - u9-visco-creep-recovery-plot
  - u9-log-er-regimes
  - u9-log-er-shifts-ps
  - u9-log-er-mw-crosslink-cryst
  - u9-visco-relaxation-calc
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_THIRDPARTIAL_2020.pdf, including 2012 ORD Q9 / 2012 EXTRA Q8 and Problems T9 Q5-Q6. Content from Session 19 Slides 42 and 45-49."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-9
---

# Bank B87 — Temperature, strain rate and viscoelasticity

> [!info] Includes official exam questions
> Ten test questions written for the bank in the style of Part I of Assessment Test III, including official exam questions from the January 2012 ordinary and 2012 extraordinary final exams plus Problems T9 Q5–Q6 (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 19, Slides 42 and 45–49.

## Q87.1 Effect of temperature and strain rate on thermoplastics

- id: B87-Q1
- concept_id: u9-temp-strain-rate-effect
- format: what-happens
- asks: effect
- origin: official-exam

For a thermoplastic polymer tested in uniaxial tension, how do decreasing the temperature or increasing the strain rate alter its mechanical response?

a) Elastic modulus and tensile strength increase, ductility drops, and behaviour becomes more brittle
b) Elastic modulus and tensile strength increase, and strain at fracture also increases
c) Elastic modulus decreases while tensile strength and elongation at fracture increase
d) Elastic modulus and tensile strength remain unchanged because covalent backbone bonds are unaffected

### Answer

a

### Explanation

January 2012 ordinary final exam, Q9; 2012 extraordinary final exam, Q8; and Session 19, Slide 42: lowering temperature or raising strain rate restricts molecular mobility and prevents chains from unravelling during deformation. Consequently, Young's modulus $E$ and strength rise while percent elongation at fracture drops, shifting the response from ductile toward brittle.

- b) Incorrect ductility trend: stiffening the polymer by cooling or faster loading makes chain disentanglement harder and *reduces* strain at fracture.
- c) Describes the effect of *increasing* temperature or *decreasing* strain rate, not cooling or faster stretching.
- d) Unlike room-temperature metals, polymer mechanical properties depend strongly on temperature and deformation rate (Slide 32: $\text{properties} = f(T, v_{\text{def}}, \text{environment})$).

### Source

MATERIALS_FINALEXAM_2012_ORD.pdf, p. 3 Q9; MATERIALS_FINALEXAM_2012_EXTRA.pdf, p. 2 Q8; Session 19, Slides 32 and 42.

## Q87.2 Temperature dependence of PMMA tensile curves

- id: B87-Q2
- concept_id: u9-temp-pmma-curve
- format: diagram-reading
- asks: figure-reading

![[attachments/T9/s19-temperature-pmma.png]]

In the tensile stress–strain curves of PMMA ($T_g$ in the $86\text{–}104\,^\circ\text{C}$ range), what transition occurs as the test temperature rises above $104\,^\circ\text{C}$?

a) PMMA transforms from a flexible elastomer into a rigid glass with higher elastic modulus
b) PMMA loses all viscoelastic time dependence and fractures instantaneously at zero strain
c) PMMA changes from a stiff brittle glass into a ductile polymer with lower modulus
d) PMMA melts directly into a dense crystalline solid with higher yield stress and modulus

### Answer

c

### Explanation

Session 19, Slide 42: below $T_g$ ($-40\,^\circ\text{C}$ to $86\,^\circ\text{C}$), PMMA has frozen amorphous segments, so it displays a steep initial slope, high strength, and brittle fracture at low strain. Above $T_g$ ($104\,^\circ\text{C}$ to $140\,^\circ\text{C}$), chain segments move freely, lowering $E$ and yield stress while allowing extensive plastic deformation and necking.

- a) Inverts the direction of the transition: heating *above* $T_g$ softens a glass rather than turning an elastomer into a glass.
- b) Above $T_g$ PMMA becomes *more* ductile (huge elongation at $140\,^\circ\text{C}$), not instantaneously brittle at zero strain.
- d) Heating above $T_g$ never creates a rigid crystal with higher strength; strength and modulus both decrease as $T$ rises.

### Source

Session 19, Slide 42.

## Q87.3 Strain-rate dependence of PVC tensile curves

- id: B87-Q3
- concept_id: u9-strain-rate-pvc-curve
- format: diagram-reading
- asks: figure-reading

![[attachments/T9/s19-strain-rate-pvc.png]]

Why does PVC tested at $1\text{ mm/s}$ fail shortly after the stress peak, whereas at $0.05\text{ mm/s}$ it draws out to a large fracture strain?

a) At $1\text{ mm/s}$ chains lack time to unravel, giving stiffer brittle failure
b) At $0.05\text{ mm/s}$ slow deformation triggers covalent crosslinking along the PVC chains
c) At $1\text{ mm/s}$ viscous heating melts the gauge section before the yield peak
d) At $0.05\text{ mm/s}$ chlorine atoms detach from the backbone, weakening interchain attraction

### Answer

a

### Explanation

Session 19, Slide 42: at the higher strain rate ($1\text{ mm/s}$), chain disentanglement is restricted because the chains do not have enough time to uncoil and slide past one another, raising initial stiffness/peak stress and causing brittle failure soon after the peak.

- b) Stretching a thermoplastic slowly does not induce covalent crosslinking reactions.
- c) Rapid testing causes brittle fracture near the yield peak rather than melting before the elastic limit.
- d) Mechanical testing at $0.05\text{ mm/s}$ does not break covalent C–Cl chemical bonds.

### Source

Session 19, Slide 42.

## Q87.4 Time-temperature equivalence in viscoelasticity

- id: B87-Q4
- concept_id: u9-visco-time-temp-equiv
- format: complete-sentence
- asks: comparison

In viscoelastic polymers, increasing the rate at which stress or strain is applied produces the same qualitative change in modulus and ductility as:

a) increasing the ambient service temperature well above $T_m$
b) lowering temperature, since both curb molecular motion during loading
c) reducing the degree of crystallinity down toward zero percent
d) adding low-molecular-weight plasticizers to weaken interchain forces

### Answer

b

### Explanation

Session 19, Slides 42 and 48 verbatim: `An increase of this rate exerts the same effect of a decrease of temperature`. Faster loading gives chain segments less time to rearrange and relax, mimicking the reduced thermal mobility of a lower temperature.

- a) Raising temperature above $T_m$ increases mobility and causes melting, the exact opposite of faster loading.
- c) Reducing crystallinity increases amorphous mobility and lowers modulus above $T_g$, opposite to raising strain rate.
- d) Adding plasticizer lowers $T_g$ and softens the polymer (analogous to heating), opposite to raising strain rate.

### Source

Session 19, Slides 42 and 48.

## Q87.5 Creep compliance versus relaxation modulus

- id: B87-Q5
- concept_id: u9-visco-creep-vs-relaxation
- format: topic-true
- asks: definition

Referring to viscoelastic creep and stress relaxation in polymers, which one of the following statements is TRUE:

a) Creep occurs under constant strain $\varepsilon_0$, where stress grows linearly as $J(t) = \sigma(t)/\varepsilon_0$
b) Stress relaxation holds constant stress $\sigma_0$ while strain decays exponentially over time
c) Both $J(t)$ and $E_r(t)$ are dimensionless constants independent of temperature and elapsed time
d) Creep defines $J(t) = \varepsilon(t)/\sigma_0$ at constant stress; relaxation defines $E_r(t) = \sigma(t)/\varepsilon_0$ at constant strain

### Answer

d

### Explanation

Session 19, Slides 47–48: under a constant step stress $\sigma(t) = \sigma_0 H(t)$, a viscoelastic polymer exhibits time-dependent strain growth characterized by creep compliance $J(t) = \varepsilon(t)/\sigma_0$ (in $\text{Pa}^{-1}$). Under a constant step strain $\varepsilon(t) = \varepsilon_0 H(t)$, stress decays gradually as characterized by the relaxation modulus $E_r(t) = \sigma(t)/\varepsilon_0$ (in $\text{Pa}$).

- a) Confuses creep with stress relaxation and puts stress in the numerator of $J(t)$.
- b) Confuses stress relaxation with creep: stress relaxation holds *strain* constant while *stress* decreases.
- c) Neither quantity is dimensionless ($[J] = \text{Pa}^{-1}$, $[E_r] = \text{Pa}$) and both depend strongly on time and temperature.

### Source

Session 19, Slides 47–48.

## Q87.6 Creep and recovery response of viscoelastic polymers

- id: B87-Q6
- concept_id: u9-visco-creep-recovery-plot
- format: diagram-reading
- asks: figure-reading

![[attachments/T9/s19-creep-recovery.png]]

When the constant applied stress $\sigma_0$ is suddenly removed during a creep-recovery test, how does the viscoelastic strain curve behave compared with purely elastic and purely viscous solids?

a) It drops instantaneously by an elastic step, recovers gradually, and keeps permanent viscous strain
b) It rebounds instantaneously back to zero strain with zero permanent deformation, matching the purely elastic curve
c) It stays completely flat after unloading at its peak strain without any instantaneous or delayed recovery
d) It continues rising linearly at the same viscous slope even after the applied stress drops to zero

### Answer

a

### Explanation

Session 19, Slide 47: a viscoelastic polymer combines elastic-solid and viscous-liquid behaviour. Upon unloading, the purely elastic fraction recovers instantaneously, a time-dependent viscoelastic fraction relaxes gradually, and the permanent viscous flow fraction remains unrecovered as residual strain.

- b) Describes the purely elastic dotted reference line, ignoring the viscous and delayed viscoelastic terms.
- c) Describes the purely viscous dotted curve, ignoring the instantaneous and delayed elastic recovery clearly drawn on the figure.
- d) Strain cannot keep growing under zero applied stress during recovery.

### Source

Session 19, Slide 47.

## Q87.7 Regimes of relaxation modulus Er(10) versus temperature

- id: B87-Q7
- concept_id: u9-log-er-regimes
- format: diagram-reading
- asks: figure-reading

![[attachments/T9/s19-relaxation-modulus-vs-temperature.png]]

For atactic polystyrene shown in the plot of $E_r(10)$ versus temperature ($T_g = 100\,^\circ\text{C}$), which regime spans the sharp three-decade modulus drop around $T_g$ (from $\sim 10^3\text{ MPa}$ down toward $\sim 1\text{ MPa}$), and which regime forms the flat region around $120\text{–}150\,^\circ\text{C}$?

a) Glassy drop; Viscous flow plateau
b) Viscous flow drop; Glassy plateau
c) Leathery drop; Rubbery plateau
d) Rubbery drop; Leathery plateau

### Answer

c

### Explanation

Session 19, Slide 49: as temperature rises across $T_g = 100\,^\circ\text{C}$, the amorphous polymer leaves the `Glassy` plateau ($> 10^3\text{ MPa}$), plunges roughly three orders of magnitude through the `Leathery` transition region, settles onto a temporary `Rubbery` plateau near $0.3\text{–}0.7\text{ MPa}$ ($120\text{–}150\,^\circ\text{C}$), and then enters `Rubbery flow` and `Viscous flow (liquid)` as chains slip completely.

- a) Mislabels the transition around $T_g$ as glassy (glassy lies *below* the drop) and the plateau as viscous flow (viscous flow drops sharply at the right).
- b) Completely inverts the temperature order of viscous flow and glassy states.
- d) Swaps the `Leathery` transition region with the `Rubbery` plateau.

### Source

Session 19, Slide 49.

## Q87.8 Identifying curves A, B and C on log Er(10) vs T

- id: B87-Q8
- concept_id: u9-log-er-shifts-ps
- format: diagram-reading
- asks: classification

![[attachments/T9/s19-ps-relaxation-atactic.png]]

For polystyrene in the plot of $E_r(10)$ against temperature, which microstructures correspond to curves A (green), B (blue), and C (red)?

a) A: amorphous atactic; B: crystalline isotactic; C: lightly crosslinked atactic
b) A: crystalline isotactic; B: lightly crosslinked atactic; C: amorphous atactic
c) A: lightly crosslinked atactic; B: crystalline isotactic; C: amorphous atactic
d) A: amorphous atactic; B: lightly crosslinked atactic; C: crystalline isotactic

### Answer

b

### Explanation

Session 19, Slides 45–46 and 49 (and Problems T9 Q5–Q6): curve A stays stiff ($10^2\text{–}10^3\text{ MPa}$) above $T_g$ because crystalline isotactic regions hold the structure rigid until they melt at $T_m \approx 240\,^\circ\text{C}$. Curve B drops at $T_g$ like an amorphous polymer, but covalent crosslinks keep it on a flat rubbery plateau with no viscous flow (lightly crosslinked atactic). Curve C plunges at $T_g$ and proceeds to viscous flow (linear amorphous polystyrene).

- a) Swaps crystalline isotactic (which resists softening up to $T_m$) with amorphous atactic (which drops three decades at $T_g$ and flows).
- c) Swaps the high-modulus semicrystalline curve A with the soft rubbery-plateau curve B.
- d) Completely reverses curves A and C.

### Source

Session 19, Slides 45–46 and 49; Problems T9_Polymers.pdf, Problems 5 and 6.

## Q87.9 How MW, crosslinking and crystallinity shift log E vs T

- id: B87-Q9
- concept_id: u9-log-er-mw-crosslink-cryst
- format: topic-false
- asks: effect

![[attachments/T9/s19-modulus-vs-temperature-crystallinity.png]]

![[attachments/T9/s19-crosslinking-modulus.png]]

Referring to how molecular weight, crosslinking, and crystallinity shift the $\log E$ versus temperature curve of an amorphous polymer, which one of the following statements is FALSE:

a) Increasing crystallinity reduces the size of the modulus drop at $T_g$ and sustains a stiff plateau up to $T_m$
b) Increasing crosslinking lifts the plateau modulus above $T_g$ and eliminates the viscous flow regime because chains are covalently tied
c) Heavy crosslinking yields a high modulus that scarcely falls with temperature until chemical degradation
d) Increasing molecular weight raises the glassy modulus below $T_g$ by three orders of magnitude and eliminates viscous flow

### Answer

d

### Explanation

Problems T9 Q5 and Session 19, Slides 45–46: raising molecular weight increases chain entanglements, which *extends* the rubbery plateau to higher temperatures and delays the onset of viscous flow; however, below $T_g$ the glassy modulus hardly changes, and without covalent crosslinks the polymer still enters viscous flow at sufficiently high temperatures. Statement d is false.

- a) True: Slide 45 and `Problems T9 Q5(c)`/`Q6` show that crystalline lamellae reduce the drop at $T_g$ and prop up modulus until $T_m$.
- b) True: Slide 46 and `Problems T9 Q5(b)` show crosslinks block chain slippage, eliminating viscous flow and raising the rubbery plateau.
- c) True: the top curve in Slide 46 (`Heavy cross-linking`) stays nearly flat at the glassy level across temperature until thermal degradation.

### Source

Problems T9_Polymers.pdf, Problems 5 and 6; Session 19, Slides 45–46.

## Q87.10 Calculating relaxed stress from Er(10)

- id: B87-Q10
- concept_id: u9-visco-relaxation-calc
- format: numeric
- asks: calculation
- calc: 400 * 0.015

A viscoelastic polystyrene rod is held at a constant tensile strain $\varepsilon_0 = 0.015$ at a temperature in the transition zone where its $10\text{ s}$ relaxation modulus is $E_r(10) = 400\text{ MPa}$. What is the tensile stress $\sigma(10)$ sustained by the rod at $t = 10\text{ s}$?

a) $0.60\text{ MPa}$
b) $6.0\text{ MPa}$
c) $60.0\text{ MPa}$
d) $26.7\text{ MPa}$

### Answer

b

### Explanation

Session 19, Slide 48 defines the relaxation modulus as $E_r(t) = \sigma(t)/\varepsilon_0$. Solving for the stress at $t = 10\text{ s}$ gives $\sigma(10) = E_r(10)\,\varepsilon_0 = 400\text{ MPa} \times 0.015 = 6.0\text{ MPa}$.

- a) Misplaced decimal factor of 10 ($\sigma = 400 \times 0.0015$ instead of $0.015$).
- c) Treated strain $\varepsilon_0 = 0.015$ as $15\%$ ($0.15$) instead of $1.5\%$ ($0.015$).
- d) Divided $400\text{ MPa}$ by $15$ instead of multiplying by $\varepsilon_0 = 0.015$.

### Source

Session 19, Slide 48.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]] · [[Aerospace Materials I MOC]]
