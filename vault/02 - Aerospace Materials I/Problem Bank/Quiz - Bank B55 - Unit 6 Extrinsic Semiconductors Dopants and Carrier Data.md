---
materia: Aerospace Materials I
tema: "Unit 6: extrinsic semiconductors, donor and acceptor energies, solubility limits and mobility data"
bank_id: B55
title: "Extrinsic semiconductors, dopants and carrier data"
category: mt2_test_block
unit: 6
concepts:
  - u6-donor-host-comparison
  - u6-acceptor-pair-comparison
  - u6-ionisation-energy-ratio
  - u6-solubility-limit-table
  - u6-mobility-vs-doping
  - u6-mobility-ratio-calc
  - u6-solubility-ppm-calc
  - u6-carrier-number-control
  - u6-extrinsic-intrinsic-ratio
  - u6-minority-carrier-term
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 13 Slides 35-42."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B55 — Extrinsic semiconductors, dopants and carrier data

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 13, Slides 35-42.

## Q55.1 Phosphorus in two hosts

- id: B55-Q1
- concept_id: u6-donor-host-comparison
- format: cause-effect
- asks: comparison

With a change of the host from silicon to germanium, for the same phosphorus content and at the same low temperature, the electrical conductivity:

a) Decreases, as germanium has the smaller band gap and fewer donors ionise
b) Increases, as the donor level of phosphorus lies closer to the conduction band
c) Stays the same, as phosphorus is a group VA donor in both hosts
d) Increases, as phosphorus acts as an acceptor in the germanium lattice

### Answer

b

### Explanation

Session 13, Slide 40: the donor energy $E_c - E_d$ of phosphorus is 0.0120 eV in germanium and 0.045 eV in silicon. A smaller energy to ionise a donor gives more free electrons at the same low temperature, so $\sigma \approx n_e|q_e|\mu_e$ is larger in germanium (the Ge against Si comparison of Problem 10 d).

- a) A smaller band gap does not remove donors: the donors ionise from $E_d$, and for this a small $E_c - E_d$ is what counts, not $E_g$.
- c) The group of the dopant fixes its type (donor), not the size of its ionisation energy, which depends on the host.
- d) Phosphorus is a donor in both hosts (group VA, five valence electrons); it does not change type.

### Source

Session 13, Slides 36 and 40; Problems T6 and T7, Problem 10 d.

## Q55.2 Boron against indium in silicon

- id: B55-Q2
- concept_id: u6-acceptor-pair-comparison
- format: true-statement
- asks: comparison

Which one of the following statements about two silicon samples at the same low temperature, one with 10 ppm of boron and the other with 10 ppm of indium, is TRUE?

a) The indium sample conducts better, as its larger ionic radius gives a larger acceptor energy
b) Both conduct equally, as boron and indium are both group IIIA acceptors
c) The boron sample conducts better, as $E_a - E_v$ is 0.045 eV against 0.160 eV
d) The boron sample conducts better, as $E_a - E_v$ is 0.160 eV against 0.045 eV

### Answer

c

### Explanation

Session 13, Slide 40: in silicon $E_a = 0.045$ eV for boron and 0.160 eV for indium. The smaller the energy needed to take an electron from the valence band to the acceptor level, the more holes at a given low temperature, so $\sigma$ is larger for boron (Problem 10 e). The arrow "Increasing $\sigma$" of the slide points towards boron.

- a) A larger energy $E_a - E_v$ means that fewer acceptors are ionised, so it lowers $\sigma$ instead of raising it.
- b) The same group gives the same type of semiconductor, not the same ionisation energy.
- d) Right conclusion with the two values swapped: indium is the one with 0.160 eV.

### Source

Session 13, Slide 40; Problems T6 and T7, Problem 10 e.

## Q55.3 Ratio of the donor energies of antimony

- id: B55-Q3
- concept_id: u6-ionisation-energy-ratio
- format: numeric
- asks: calculation
- calc: 0.039/0.0096

The donor energies $E_c - E_d$ of the slide (in eV, silicon and germanium) are 0.045 and 0.0120 for P, 0.049 and 0.0127 for As, 0.039 and 0.0096 for Sb. Determine the ratio between the donor energy of antimony in silicon and in germanium:

a) 0.246
b) 3.75
c) 3.86
d) 4.06

### Answer

d

### Explanation

Session 13, Slide 40: for antimony the ratio is $E_d^{Si}/E_d^{Ge} = 0.039/0.0096 = 4.06$ (both in eV, so the ratio is dimensionless).

- a) The ratio was inverted: $0.0096/0.039 = 0.246$ is germanium over silicon.
- b) The phosphorus row was used: $0.045/0.0120 = 3.75$.
- c) The arsenic row was used: $0.049/0.0127 = 3.86$.

### Source

Session 13, Slide 40.

## Q55.4 Donor able to supply a high concentration

- id: B55-Q4
- concept_id: u6-solubility-limit-table
- format: identify
- asks: application

A silicon crystal has to hold $1.5\times10^{27}$ donor atoms/m³. From the maximum solid solubilities of the slide, indicate which dopant can supply them:

| Dopant in Si | Group | Maximum solubility (atoms/m³) |
| :--- | :--- | :--- |
| B | IIIA | $600\times10^{24}$ |
| Ga | IIIA | $40\times10^{24}$ |
| P | VA | $1000\times10^{24}$ |
| As | VA | $2000\times10^{24}$ |
| Sb | VA | $70\times10^{24}$ |

a) Phosphorus
b) Gallium
c) Antimony
d) Arsenic

### Answer

d

### Explanation

Session 13, Slide 40: the target is $1.5\times10^{27} = 1500\times10^{24}$ atoms/m³ of donors, so the dopant must be a donor (group VA) with a solubility limit above it: only arsenic ($2000\times10^{24}$) qualifies.

- a) Phosphorus is a donor, but its limit of $1000\times10^{24}$ is below the target.
- b) Gallium is a group IIIA acceptor, and its limit is only $40\times10^{24}$.
- c) Antimony is a donor, but its limit of $70\times10^{24}$ is far below the target.

### Source

Session 13, Slide 40.

## Q55.5 Hole mobility at high doping

- id: B55-Q5
- concept_id: u6-mobility-vs-doping
- format: diagram-reading
- asks: figure-reading

Approximate values read from the chart of room-temperature mobility against dopant concentration in silicon are given below. When the dopant concentration rises from $10^{19}$ to $10^{24}$ m⁻³, the hole mobility:

| Dopant concentration (m⁻³) | $\mu_e$ (m²/(V·s)) | $\mu_h$ (m²/(V·s)) |
| :--- | :--- | :--- |
| $10^{19}$ | 0.14 | 0.048 |
| $10^{22}$ | 0.10 | 0.044 |
| $10^{24}$ | 0.05 | 0.010 |

a) Falls to about one fiftieth of its value
b) Falls to about one fifth of its value
c) Rises by a factor of about five
d) Stays within 10 % of its value

### Answer

b

### Explanation

Session 13, Slide 42 (chart): $\mu_h$ goes from about 0.048 to about 0.010 m²/(V·s), a factor $0.048/0.010 \approx 5$ down. The curve is flat up to about $10^{22}$ m⁻³ and falls beyond it; the statement of the slide, that the distortion caused by doping is negligible, holds for moderate doping.

- a) The drop was read as about two decades of the logarithmic axis (a factor 50): the curve falls by less than one decade, $\log(4.8) = 0.68$.
- c) The trend was inverted: the mobility does not rise with the dopant concentration.
- d) Only the flat part of the chart (up to $10^{22}$ m⁻³, where $\mu_h$ changes by 8 %) was considered.

### Source

Session 13, Slide 42.

## Q55.6 Conductivity from the mobility ratio

- id: B55-Q6
- concept_id: u6-mobility-ratio-calc
- format: numeric
- asks: calculation
- calc: 5e21*q*2.81*0.045

Silicon contains $5.0\times10^{21}$ phosphorus atoms/m³, all ionised. With $\mu_h = 0.045$ m²/(V·s) and $\mu_e/\mu_h = 2.81$, determine its electrical conductivity:

a) 12.8 (Ω·m)⁻¹
b) 36.0 (Ω·m)⁻¹
c) 101 (Ω·m)⁻¹
d) 285 (Ω·m)⁻¹

### Answer

c

### Explanation

Session 13, Slides 36 and 42: phosphorus is a donor, so $n_e \approx 5.0\times10^{21}$ m⁻³ and $\sigma \approx n_e|q_e|\mu_e$ with $\mu_e = 2.81\cdot0.045 = 0.126$ m²/(V·s): $\sigma = 5.0\times10^{21}\cdot1.602\times10^{-19}\cdot0.126 = 101$ (Ω·m)⁻¹.

- a) $\mu_e$ was taken as $\mu_h/2.81$: the ratio was inverted.
- b) The hole mobility was used: $n_e|q_e|\mu_h = 36.0$ (Ω·m)⁻¹, but in an n-type semiconductor the electrons conduct.
- d) The ratio was applied twice: $\mu_e = 2.81^2\cdot0.045$.

### Source

Session 13, Slides 36 and 42.

## Q55.7 Solubility limit of antimony in ppm

- id: B55-Q7
- concept_id: u6-solubility-ppm-calc
- format: numeric
- asks: calculation
- calc: 70e24/5.0e28*1e6

Silicon has $5.0\times10^{28}$ atoms/m³. From the table of maximum solid solubilities, the limit of dopant in silicon is $1000\times10^{24}$ atoms/m³ for P, $2000\times10^{24}$ for As and $70\times10^{24}$ for Sb, and in germanium $10\times10^{24}$ for Sb. Determine the maximum content of antimony in silicon in ppm of atoms:

a) 200 ppm
b) 1400 ppm
c) 20000 ppm
d) 40000 ppm

### Answer

b

### Explanation

Session 13, Slide 40: the fraction is $70\times10^{24}/5.0\times10^{28} = 1.4\times10^{-3}$, that is 1400 ppm ($1\ \mathrm{ppm} = 10^{-6}$).

- a) The germanium row was used: $10\times10^{24}/5.0\times10^{28}\cdot10^6 = 200$ ppm.
- c) The phosphorus limit was used: $1000\times10^{24}/5.0\times10^{28}\cdot10^6 = 20\,000$ ppm.
- d) The arsenic limit was used: $2000\times10^{24}/5.0\times10^{28}\cdot10^6 = 40\,000$ ppm.

### Source

Session 13, Slide 40.

## Q55.8 Why the carriers control the conductivity

- id: B55-Q8
- concept_id: u6-carrier-number-control
- format: cause-effect
- asks: cause

According to the slides, the conductivity of an extrinsic semiconductor is controlled by the number of charge carriers because the doping:

a) Raises the mobility in proportion to the number of carriers
b) Distorts the crystal strongly, so the mobility falls as fast as $n$ rises
c) Barely distorts the crystal, so the mobility stays almost constant
d) Makes the electron and hole mobilities equal in the material

### Answer

c

### Explanation

Session 13, Slide 42: $\sigma = n|q_e|\mu$; the distortion of the crystal caused by doping is negligible, so $\mu$ hardly changes and the large change of $n$ with the doping (and with the ionisation) sets $\sigma$.

- a) No such law exists: the chart of the slide shows a mobility that is constant or falling with dopant concentration.
- b) The inverse was assumed: if the mobility cancelled the rise of $n$, $\sigma$ would not depend on the doping.
- d) In extrinsic semiconductors $\mu_e > \mu_h$ (ratio 2.81 for Si, 2.05 for Ge).

### Source

Session 13, Slide 42.

## Q55.9 Doped against pure silicon

- id: B55-Q9
- concept_id: u6-extrinsic-intrinsic-ratio
- format: numeric
- asks: calculation
- calc: 2e22*q*0.10/4e-4

Silicon doped with $2.0\times10^{22}$ donor atoms/m³, all ionised, has $\mu_e = 0.10$ m²/(V·s). Pure silicon at the same temperature has $\sigma = 4\times10^{-4}$ (Ω·m)⁻¹. Determine the ratio of the conductivity of the doped to the pure silicon:

a) $1.25\times10^{-6}$
b) $3.20\times10^{2}$
c) $8.01\times10^{3}$
d) $8.01\times10^{5}$

### Answer

d

### Explanation

Session 13, Slides 36 and 42: $\sigma_{ext} \approx n_e|q_e|\mu_e = 2.0\times10^{22}\cdot1.602\times10^{-19}\cdot0.10 = 320$ (Ω·m)⁻¹, and $320/(4\times10^{-4}) = 8.01\times10^{5}$ (dimensionless). Doping multiplies the conductivity by many orders of magnitude.

- a) The ratio was inverted: $4\times10^{-4}/320$.
- b) The extrinsic conductivity was reported and not divided by the intrinsic one.
- c) A factor 100 was slipped in the conversion of the intrinsic value between (Ω·cm)⁻¹ and (Ω·m)⁻¹, although both data are already in (Ω·m)⁻¹.

### Source

Session 13, Slides 36 and 42.

## Q55.10 Electron term in p-type silicon

- id: B55-Q10
- concept_id: u6-minority-carrier-term
- format: cause-effect
- asks: cause

In p-type silicon the electron term of the conductivity is negligible against the hole term, in spite of $\mu_e > \mu_h$, because:

a) Electrons are the minority carriers and $p \gg n$
b) The electron mobility is lower than the hole mobility
c) Electrons carry less charge than the holes do
d) The acceptor atoms capture every free electron

### Answer

a

### Explanation

Session 13, Slides 37 and 42: $\sigma = n|q_e|\mu_e + p|q_e|\mu_h$ with $p \gg n$. The number of holes exceeds the number of electrons by many orders of magnitude, which outweighs the factor 2.81 between the mobilities, so $\sigma \approx p|q_e|\mu_h$.

- b) The mobilities were swapped: in extrinsic semiconductors $\mu_e > \mu_h$.
- c) Electrons and holes carry charges of the same magnitude, $1.6\times10^{-19}$ C.
- d) Acceptors take electrons from the valence band and leave holes; they do not remove the electrons of the conduction band, whose number is only small (minority).

### Source

Session 13, Slides 37 and 42.
