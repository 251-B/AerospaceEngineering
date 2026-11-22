---
materia: Aerospace Materials I
tema: "Unit 10: longitudinal isostrain micromechanics, load sharing, critical fibre volume fraction, fibre stress-strain curves and specific properties"
bank_id: B98
title: "Longitudinal isostrain micromechanics"
category: mt3_test_block
unit: 10
concepts:
  - u10-isostrain-condition
  - u10-isostrain-majority-load
  - u10-isostrain-e1c-modulus
  - u10-isostrain-load-ratio
  - u10-isostrain-vmin-vcrit
  - u10-isostrain-selection-vf40
  - u10-isostrain-specific-chart
  - u10-isostrain-fiber-curves
  - u10-isostrain-ud-vs-woven
  - u10-isostrain-specific-ordering
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_THIRDPARTIAL_2020.pdf, including Q9b of MATERIALS_FINALEXAM_2017_EXTRA.pdf. Content from Session 21 Slides 37, 40-43, Session 22 Slides 19-22, 26, and Problems T10."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-10
---

# Bank B98 — Longitudinal isostrain micromechanics

> [!info] Includes official exam questions
> Ten test questions written for the bank in the style of Part I of Assessment Test III, including an adaptation of Q9b from the June 2017 extraordinary final exam (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 21, Slides 37 and 40-43; Session 22, Slides 19-22 and 26; Problems T10.

## Q98.1 Isostrain assumptions along continuous fibres

- id: B98-Q1
- concept_id: u10-isostrain-condition
- format: topic-true
- asks: definition

Referring to the mechanics-of-materials model for a unidirectional composite loaded parallel to continuous aligned fibres, which one of the following statements is TRUE:

a) The fibres and the matrix carry equal axial stress while their axial strains differ in proportion to their moduli
b) Assuming a perfect interfacial bond, fibre, matrix, and composite undergo equal axial strain so $\sigma_{1C} = V_f\sigma_{1f} + V_m\sigma_{1m}$
c) Because the fibres occupy only part of the cross-section, the composite length is greater than the fibre length
d) For $E_f \gg E_m$, the longitudinal modulus is governed by the harmonic mean $1/E_{1C} = V_f/E_f + V_m/E_m$

### Answer

b

### Explanation

Session 22, Slides 20-22: under longitudinal loading with good fibre-matrix bonding, the composite obeys isostrain ($\varepsilon_C = \varepsilon_f = \varepsilon_m$). Force equilibrium $F_C = F_f + F_m$ with equal lengths $L_C = L_f = L_m$ turns area fractions into volume fractions ($A_f/A_C = V_f$), yielding $\sigma_{1C} = V_f\sigma_{1f} + V_m\sigma_{1m}$ and $E_{1C} = V_f E_f + V_m E_m$.

- a) Confuses longitudinal isostrain with transverse isostress: equal stress ($\sigma_f = \sigma_m$) holds only when loading is perpendicular to the fibres (Slide 23).
- c) Violates the geometric premise of continuous aligned fibres spanning the whole specimen, where $L_C = L_f = L_m$ (Slide 21).
- d) Applies the transverse isostress harmonic-mean formula (Eq. 2, Slide 24) instead of the longitudinal rule of mixtures (Eq. 1, Slide 22).

### Source

Session 22, Slides 20-24.

## Q98.2 Phase carrying the majority of longitudinal load

- id: B98-Q2
- concept_id: u10-isostrain-majority-load
- format: cause-effect
- asks: cause
- origin: official-exam

A continuous and aligned composite containing 30 vol% silicon carbide fibres ($E_f = 400$ GPa) in 70 vol% polycarbonate matrix ($E_m = 2.4$ GPa) is loaded along the fibre axis. Which phase supports the vast majority of the applied load, and why?

a) The polycarbonate matrix, because its 70 % volume fraction provides a larger cross-sectional area than the fibres
b) Both phases support nearly equal loads, because perfect bonding enforces equal stress in fibres and matrix
c) The polycarbonate matrix, because its lower modulus allows larger local strain that absorbs more elastic work
d) The SiC fibre phase, because equal axial strains give $\sigma_f/\sigma_m = E_f/E_m \gg 1$ and $F_f/F_m \approx 71.4$

### Answer

d

### Explanation

June 2017 extraordinary final exam, Q9b (and Session 22, Slides 21-22): under longitudinal isostrain ($\varepsilon_f = \varepsilon_m$), Hooke's law gives $\sigma_f/\sigma_m = E_f/E_m = 400/2.4 = 166.7$. Multiplying by the area ratio $A_f/A_m = V_f/V_m = 0.30/0.70$ gives the fibre-to-matrix load ratio $F_f/F_m = (E_f V_f)/(E_m V_m) = (400 \times 0.30)/(2.4 \times 0.70) = 71.4$, so the fibres carry roughly 98.6 % of the load.

- a) Looks only at volume fraction $V_m = 0.70$ and ignores the 167-fold stiffness advantage of SiC fibres over polycarbonate.
- b) Confuses isostrain ($\varepsilon_f = \varepsilon_m$) with isostress ($\sigma_f = \sigma_m$); even with equal stress, unequal areas would not split the load equally.
- c) Violates strain compatibility: in longitudinal isostrain, the matrix cannot deform more than the bonded fibres ($\varepsilon_m = \varepsilon_f$).

### Source

MATERIALS_FINALEXAM_2017_EXTRA.pdf, pp. 5-6 Q9b; Session 22, Slides 21-22.

## Q98.3 Longitudinal modulus of an E-glass/polyester composite

- id: B98-Q3
- concept_id: u10-isostrain-e1c-modulus
- format: numeric
- asks: calculation
- calc: 0.40 * 72.0 + 0.60 * 3.4

A unidirectional continuous E-glass/polyester composite contains 40 vol% aligned fibres ($E_f = 72.0$ GPa) in a polyester matrix ($E_m = 3.4$ GPa). Under longitudinal isostrain conditions, what is its longitudinal elastic modulus $E_{1C}$?

a) 30.8 GPa
b) 5.5 GPa
c) 44.6 GPa
d) 28.8 GPa

### Answer

a

### Explanation

Session 22, Slide 22 (and Problems T10, Q5a): by the longitudinal rule of mixtures, $E_{1C} = V_f E_f + (1 - V_f)E_m = 0.40(72.0\text{ GPa}) + 0.60(3.4\text{ GPa}) = 28.80 + 2.04 = 30.84\text{ GPa} \approx 30.8\text{ GPa}$.

- b) Applies the transverse isostress equation $E_{2C} = [0.40/72.0 + 0.60/3.4]^{-1} = 5.49\text{ GPa}$ instead of the longitudinal isostrain rule.
- c) Swaps the volume fractions, computing $0.60(72.0) + 0.40(3.4) = 44.56\text{ GPa}$ as if the composite contained 60 vol% fibres.
- d) Neglects the matrix contribution $V_m E_m = 2.04\text{ GPa}$ by using the rough approximation $E_1 \approx V_f E_f = 28.8\text{ GPa}$, which underestimates $E_{1C}$ at $V_f = 40\%$.

### Source

Problems T10_CompositeMaterials.pdf, Q5; Session 22, Slide 22.

## Q98.4 Fibre load ratio and matrix contribution

- id: B98-Q4
- concept_id: u10-isostrain-load-ratio
- format: complete-sentence
- asks: comparison

When a continuous aligned composite with $V_f = 55\%$ and $E_f \gg E_m$ is loaded longitudinally in the elastic regime, the matrix contribution $(1 - V_f)E_m$ to $E_{1C}$ is small, so:

a) increasing $E_m$ tenfold has a much stronger effect on $E_{1C}$ than doubling $V_f$
b) the longitudinal modulus can be approximated by $E_{1C} \approx E_m / V_m$
c) the fibre load fraction $F_f/F_C = V_f E_f / E_{1C}$ stays close to unity and $E_{1C} \approx V_f E_f$
d) the stress in the matrix exceeds the stress in the fibres by the factor $V_f / V_m$

### Answer

c

### Explanation

Session 22, Slide 22: when $E_f \gg E_m$ at typical fibre contents ($V_f = 50\text{–}60\%$), the matrix term $(1 - V_f)E_m$ is negligible relative to $V_f E_f$, giving $E_1 \approx E_f V_f$. Consequently, the fraction of longitudinal force carried by the fibres is $F_f/F_C = V_f E_f / E_{1C} \approx 1$.

- a) Overstates the small matrix term: because $E_f \gg E_m$, raising $V_f$ dominates $E_{1C}$ far more than modest changes in $E_m$.
- b) Prints the transverse approximation $E_2 \approx E_m/V_m$ (Slide 24), which applies perpendicular to the fibres rather than along them.
- d) Inverts the stress ratio: under isostrain, $\sigma_f/\sigma_m = E_f/E_m \gg 1$, so the fibres carry much higher stress than the matrix.

### Source

Session 22, Slides 22 and 24; Problems T10_CompositeMaterials.pdf, Q4, Q6.

## Q98.5 Critical and minimum fibre volume fractions

- id: B98-Q5
- concept_id: u10-isostrain-vmin-vcrit
- format: topic-false
- asks: definition

Regarding the longitudinal tensile strength $\sigma_{cu}$ of a unidirectional composite with brittle fibres ($\sigma_{fu}$) in a ductile matrix ($\sigma_{mu}$) as a function of fibre volume fraction $V_f$, which one of the following statements is FALSE:

a) Below $V_{\min}$, once the few brittle fibres fracture, the remaining matrix carries the composite and its strength follows $\sigma_m(1 - V_f)$
b) Adding any small volume fraction of continuous brittle fibres ($0 < V_f < V_{\min}$) raises the composite tensile strength above $\sigma_{mu}$
c) Above $V_{\text{crit}}$, composite tensile strength exceeds the unreinforced matrix strength $\sigma_{mu}$ and follows $\sigma_{fu}V_f + \sigma'_m(1 - V_f)$
d) Because $\sigma_{fu} \gg \sigma_{mu}$ in typical structural fibre-polymer systems, both $V_{\min}$ and $V_{\text{crit}}$ are only a few percent

### Answer

b

### Explanation

Session 22, Slide 26: when $V_f < V_{\text{crit}}$, the composite tensile strength actually falls below that of the unreinforced matrix $\sigma_{mu}$; in particular, for $0 < V_f < V_{\min}$, fractured fibres leave voids so only the matrix fraction $(1 - V_f)$ carries load, giving $\sigma_{cu} = \sigma_{mu}(1 - V_f) < \sigma_{mu}$. Statement b is false.

- a) True: Slide 26 explicitly prints $\sigma_C = \sigma_m(1 - V_f)$ for the post-fibre-fracture regime governing low $V_f$.
- c) True: above $V_{\text{crit}}$, the rule-of-mixtures branch $\sigma_{fu}V_f + \sigma'_m(1 - V_f)$ surpasses $\sigma_{mu}$ (Slide 26).
- d) True: with $\sigma_{fu}$ orders of magnitude above $\sigma_{mu}$, $V_{\min}$ and $V_{\text{crit}}$ are small compared with typical 50-60 vol% aerospace laminates.

### Source

Session 22, Slide 26.

## Q98.6 Candidate fibre selection at capped volume fraction

- id: B98-Q6
- concept_id: u10-isostrain-selection-vf40
- format: identify
- asks: application

An epoxy matrix ($E_m = 3.1$ GPa, $\sigma_m = 69$ MPa) is reinforced with continuous aligned fibres at $V_f \le 40\%$. Minimum requirements are $E_{1C} \ge 55$ GPa and $\sigma_{1C} \ge 1200$ MPa. Using glass ($E = 72$ GPa, $\sigma = 2000$ MPa), aramid ($E = 124$ GPa, $\sigma = 3500$ MPa), or carbon ($E = 350$ GPa, $\sigma = 3500$ MPa), which reinforcement satisfies both criteria?

a) Only glass fibres, because glass offers the best balance of stiffness and elongation
b) Both aramid and carbon fibres, because both reach $\sigma_{1C} > 1200$ MPa at $V_f = 40\%$
c) Only carbon fibres, because glass and aramid both fall short of $E_{1C} = 55$ GPa at $V_f \le 40\%$
d) All three fibre types, because $V_f = 40\%$ exceeds the critical volume fraction of every candidate

### Answer

c

### Explanation

Problems T10, Q2 (and Jan 2012 ordinary final, Q5): at the upper limit $V_f = 0.40$, $E_{1C} = 0.40 E_f + 0.60(3.1)$. Glass gives $E_{1C} = 30.7$ GPa (and $\sigma_{1C} = 841$ MPa), failing both targets; aramid gives $\sigma_{1C} = 1441$ MPa (passes strength) but $E_{1C} = 51.5\text{ GPa} < 55$ GPa (fails stiffness); only carbon reaches both $E_{1C} = 141.9$ GPa and $\sigma_{1C} = 1441$ MPa.

- a) Glass fails both minimum targets at $V_f = 40\%$, reaching roughly half the required modulus and 70 % of the required strength.
- b) Checks only strength and overlooks that aramid ($E_f = 124$ GPa) reaches at most 51.5 GPa in epoxy at $V_f = 40\%$, below 55 GPa.
- d) Exceeding $V_{\text{crit}}$ ensures the composite outperforms pure epoxy, not that it meets arbitrary stiffness and strength design thresholds.

### Source

Problems T10_CompositeMaterials.pdf, Q2; MATERIALS_FINALEXAM_2012_ORD.pdf, p. 3 Q5.

## Q98.7 Reading the specific strength vs specific modulus chart

- id: B98-Q7
- concept_id: u10-isostrain-specific-chart
- format: diagram-reading
- asks: figure-reading

From the plot of specific tensile strength against specific modulus for epoxy-matrix composites, which pair lists, in order, the unidirectional composite with the highest specific tensile strength and the one with the highest specific modulus?

![[attachments/T10/s21-specific-strength-modulus-MJ-chart.png]]

a) Kevlar 49 and high-modulus graphite
b) S-glass and Kevlar 49
c) E-glass and boron fibre
d) Steel and high-modulus graphite

### Answer

a

### Explanation

Session 21, Slide 43: on the specific-properties map (in MJ/kg = m²/s²), unidirectional Kevlar 49/epoxy sits at the top of the vertical axis (around 1.45 MJ/kg, just ahead of high-strength graphite), while unidirectional high-modulus graphite/epoxy sits farthest right along the horizontal axis (around 178 MJ/kg).

- b) S-glass reaches roughly 1.0 MJ/kg in specific strength (below Kevlar 49 and HS graphite), and Kevlar 49 sits near 58 MJ/kg in specific modulus rather than at the right extreme.
- c) E-glass has the lowest specific strength among the fibres (~0.52 MJ/kg), and boron fibre (~98 MJ/kg) lies well left of high-modulus graphite.
- d) Bulk steel sits near the bottom-left origin (~0.24 MJ/kg specific strength), together with bulk titanium and aluminium alloys.

### Source

Session 21, Slide 43.

## Q98.8 Stress-strain behaviour of reinforcing fibres

- id: B98-Q8
- concept_id: u10-isostrain-fiber-curves
- format: diagram-reading
- asks: comparison

Which statement accurately interprets the tensile stress-strain curves shown for common reinforcing fibres?

![[attachments/T10/s21-mechanical-properties-fibres-chart.png]]

a) HM graphite yarn displays extensive plastic yielding past 3 % strain before failing
b) E-glass roving has a higher tensile elastic modulus than Type HT graphite yarn
c) Nomex exhibits the steepest initial elastic slope and highest ultimate stress among the fibres
d) All fibres behave linearly up to brittle fracture, with stiffer fibres failing at lower strain than S-glass

### Answer

d

### Explanation

Session 21, Slide 40: each reinforcing fibre deforms elastically along a straight line straight to brittle fracture without yielding. High-modulus graphite ($E_T = 414$ GPa) and boron ($379$ GPa) break below 1 % strain, whereas more compliant E-glass ($68.9$ GPa) and S-glass ($82.7$ GPa) sustain 2.5 % to over 3.5 % strain.

- a) Attributes ductile yielding to brittle HM graphite yarn, which fractures below 0.6 % strain in a purely linear trace.
- b) Inverts the slopes: E-glass has $E_T = 68.9$ GPa, nearly four times lower than Type HT graphite ($E_T = 262$ GPa).
- c) Misreads the bottom curve: Nomex lies far below every structural reinforcement on both slope and fracture stress.

### Source

Session 21, Slide 40.

## Q98.9 Unidirectional vs woven and cross-plied epoxy laminates

- id: B98-Q9
- concept_id: u10-isostrain-ud-vs-woven
- format: true-statement
- asks: comparison

Which of the following statements is TRUE regarding unidirectional (UD) and multi-directional carbon/epoxy laminates:

a) A UD carbon/epoxy laminate is completely isotropic in-plane, keeping the same modulus at 0° and 90°
b) Stacking plies at 0°, 90°, and $\pm 45^\circ$ reduces 0° stiffness relative to UD 0° while raising transverse or shear performance
c) A $\pm 45^\circ$ woven carbon/epoxy laminate achieves a higher 0° tensile modulus than a 0/90 woven laminate
d) A UD Kevlar 49/epoxy laminate exhibits higher compressive strength than tensile strength along the 0° fibre axis

### Answer

b

### Explanation

Session 21, Slides 37 and 41: UD carbon/epoxy reaches $E_{0^\circ} = 134$ GPa and $\text{UTS}_{0^\circ} = 2040$ MPa along the fibres, but drops to $E_{90^\circ} = 11$ GPa and $\text{UTS}_{90^\circ} = 90$ MPa transversely. A 0/90 woven laminate shares stiffness equally at $70$ GPa in both 0° and 90°, while a $\pm 45^\circ$ carbon laminate raises the shear modulus $G$ to 27 GPa (versus 5 GPa for UD).

- a) Contradicts UD anisotropy: UD carbon/epoxy drops more than tenfold in modulus and more than twentyfold in strength from 0° to 90° (Slide 41).
- c) Inverts 0/90 and $\pm 45^\circ$ tensile stiffness: in the table on Slide 41, 0/90 woven carbon/epoxy has $E_{0^\circ} = 70$ GPa whereas $\pm 45^\circ$ has $E_{0^\circ} = 18$ GPa.
- d) Inverts Kevlar's tension-compression asymmetry: UD Kevlar 49/epoxy has $\text{UTS}_{0^\circ} = 1379$ MPa against only $\text{UCS}_{0^\circ} = 276$ MPa (Slide 41).

### Source

Session 21, Slides 37 and 41.

## Q98.10 Ranking aerospace structural materials by specific modulus

- id: B98-Q10
- concept_id: u10-isostrain-specific-ordering
- format: ordering
- asks: comparison

Three aerospace structural candidates are sized to match a longitudinal elastic modulus of $E = 110$ GPa: a monolithic Ti alloy ($E/\rho = 24\,406$ kN·m/kg), a unidirectional boron/aluminium composite ($E/\rho = 41\,431$ kN·m/kg), and a unidirectional carbon/polyester composite ($E/\rho = 78\,314$ kN·m/kg). In order of INCREASING specific modulus (and thus DECREASING part mass for fixed stiffness), they rank as:

a) Carbon/polyester, boron/aluminium, Ti alloy
b) Boron/aluminium, Ti alloy, carbon/polyester
c) Ti alloy, boron/aluminium, carbon/polyester
d) Ti alloy, carbon/polyester, boron/aluminium

### Answer

c

### Explanation

Problems T10, Q11 (and Session 21, Slide 43): specific modulus is $E/\rho$. For a fixed part geometry and target longitudinal stiffness $E = 110$ GPa, higher $E/\rho$ directly translates into lower density and lower structural mass (450 kg Ti alloy $\to$ 265 kg B-Al $\to$ 140.3 kg C-PE). Thus increasing specific modulus runs Ti alloy ($24\,406$) < boron/aluminium ($41\,431$) < carbon/polyester ($78\,314$ kN·m/kg).

- a) Reverses the ranking, ordering the three candidates by *decreasing* specific modulus (increasing mass).
- b) Places boron/aluminium below Ti alloy despite its lower density and nearly 70 % higher specific modulus.
- d) Swaps boron/aluminium and carbon/polyester, overlooking the much lower density of a polymer matrix compared with aluminium.

### Source

Problems T10_CompositeMaterials.pdf, Q11; Session 21, Slide 43.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
