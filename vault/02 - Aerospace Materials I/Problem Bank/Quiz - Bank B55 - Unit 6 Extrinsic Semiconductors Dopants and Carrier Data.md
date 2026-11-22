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
  - u6-donor-acceptor-levels
  - u6-extrinsic-band-diagram
  - u6-mobility-vs-doping
  - u6-dopant-concentration-effect
  - u6-dopant-identification
  - u6-carrier-number-control
  - u6-extrinsic-intrinsic-comparison
  - u6-minority-carrier-term
difficulty: 2
origen: "Includes Questions adapted from MATERIALS_FINALEXAM_2014_ORD.pdf (Q8a), MATERIALS_FINALEXAM_2013_ORD.pdf (Q4A) and MATERIALS_FINALEXAM_2017_EXTRA.pdf (Q6a) alongside practice items. Content and data from Session 13 Slides 35-42."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B55 — Extrinsic semiconductors, dopants and carrier data

> [!info] Includes official exam questions
> Ten test questions in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Question 2 adapts Question 8a of MATERIALS_FINALEXAM_2014_ORD.pdf and Question 4 adapts Question 4A of MATERIALS_FINALEXAM_2013_ORD.pdf (and Q6a of 2017_EXTRA); the rest are practice items. Content: Session 13, Slides 35-42.

## Q55.1 Phosphorus in two hosts

- id: B55-Q1
- concept_id: u6-donor-host-comparison
- format: cause-effect
- asks: comparison

With a change of the host from silicon to germanium for the same phosphorus content at the same low temperature (given $E_c - E_d = 0.045$ eV in Si and $0.012$ eV in Ge), the electrical conductivity:

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
- format: topic-true
- asks: comparison
- origin: official-exam

Referring to silicon doped with 1 ppm of boron versus silicon doped with 1 ppm of indium (both group IIIA acceptors, with B ion size smaller than In ion size) at the same temperature, indicate which statement is TRUE:

a) Both are n-type semiconductors with donor levels, and indium conducts better due to its larger ionic size
b) Both conduct identically at low temperature because equal ppm amounts always ionise equal numbers of holes
c) Both are p-type semiconductors, and boron conducts better because its smaller ion reduces $E_a$ via stronger attraction
d) Boron gives a p-type semiconductor while indium gives an n-type semiconductor because indium sits lower in the periodic table

### Answer

c

### Explanation

MATERIALS_FINALEXAM_2014_ORD.pdf, p. 7 (Question 8a) and Official Key (COMPILATION, p. 16); Session 13, Slides 37 and 40: both B and In belong to group IIIA (three valence electrons), making silicon p-type with an acceptor level; the smaller B ion attracts the valence electron more strongly, lowering the acceptor ionisation energy $E_a$ and increasing the hole concentration and conductivity ($\sigma_{\text{B-doped}} > \sigma_{\text{In-doped}}$).

- a) Misidentifies group IIIA acceptors as n-type donors and inverts the ion-size effect on acceptors.
- b) Ignores the difference in acceptor level energy $E_a - E_v$ ($0.045$ eV for B vs $0.160$ eV for In), which controls partial ionisation.
- d) Places B and In into opposite dopant types even though both lie in group IIIA with three valence electrons.

### Source

MATERIALS_FINALEXAM_2014_ORD.pdf, p. 7 (Question 8a) and Official Key (COMPILATION, p. 16); Session 13, Slides 37 and 40.

## Q55.3 Extrinsic impurity energy levels

- id: B55-Q3
- concept_id: u6-donor-acceptor-levels
- format: topic-false
- asks: cause

With respect to extrinsic semiconductors and their impurity energy levels, indicate which statement is FALSE:

a) Group IIIA acceptors such as boron donate their extra valence electron directly into the conduction band
b) Group VA elements such as phosphorus and arsenic create occupied donor levels $E_d$ just below the conduction band
c) Doping silicon with ppm levels of impurities increases majority carrier density by orders of magnitude over pure silicon
d) Extrinsic conductivity is dominated by the majority carrier term ($n_e|q_e|\mu_e$ or $p|q_e|\mu_h$) at room temperature

### Answer

a

### Explanation

Session 13, Slides 36-37: group IIIA acceptors such as boron have only three valence electrons (one fewer than Si), so they accept an electron from the valence band into an acceptor level $E_a$ just above $E_v$, leaving a hole. Donating an extra electron into the conduction band is what group VA donors do. Statement a) is false.

- b) True (Slide 36): group VA atoms form four covalent bonds and contribute one loosely bound electron in a donor level just below $E_c$.
- c) True (Slides 26 and 31): ppm doping yields $\sim 10^{22}$–$10^{23}$ carriers/m³ against $n_i = 1.5\times10^{16}$ m⁻³ in pure Si.
- d) True (Slides 36-37): since $n \gg p$ (n-type) or $p \gg n$ (p-type), the minority carrier contribution is negligible.

### Source

Session 13, Slides 26, 31 and 36-37.

## Q55.4 Band diagrams of P-doped and B-doped silicon

- id: B55-Q4
- concept_id: u6-extrinsic-band-diagram
- format: topic-true
- asks: classification
- origin: official-exam

With respect to the energy-band diagrams of silicon doped with phosphorus (group VA) and silicon doped with boron (group IIIA), indicate which statement is TRUE:

a) Phosphorus creates an occupied donor level just below the conduction band (n-type), whereas boron creates an acceptor level just above the valence band (p-type)
b) Boron creates a donor level near the conduction band (n-type), whereas phosphorus creates an acceptor level near the valence band (p-type)
c) Both phosphorus and boron create levels at the exact centre of the band gap, differing in carrier mobility
d) Neither dopant adds states inside the band gap; doping changes conductivity solely by narrowing the gap $E_g$

### Answer

a

### Explanation

MATERIALS_FINALEXAM_2013_ORD.pdf, p. 1 (Question 4A), MATERIALS_FINALEXAM_2017_EXTRA.pdf, p. 4 (Question 6a), and Session 13, Slides 35-37: phosphorus (5 valence electrons) behaves as an electron donor creating an n-type semiconductor with level $E_d$ just below $E_c$, while boron (3 valence electrons) behaves as an acceptor creating a p-type semiconductor with level $E_a$ just above $E_v$.

- b) Swaps the donor and acceptor roles and the n-type and p-type classifications of P and B.
- c) Places impurity states at mid-gap rather than close to the band edges ($E_c$ for donors, $E_v$ for acceptors).
- d) Ignores the discrete donor/acceptor states in the gap that enable low-energy extrinsic ionisation while leaving $E_g$ of the host unchanged.

### Source

MATERIALS_FINALEXAM_2013_ORD.pdf, p. 1 (Question 4A); MATERIALS_FINALEXAM_2017_EXTRA.pdf, p. 4 (Question 6a); Session 13, Slides 35-37.

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

## Q55.6 Increasing phosphorus doping in silicon

- id: B55-Q6
- concept_id: u6-dopant-concentration-effect
- format: what-happens
- asks: application

A silicon crystal at room temperature has its phosphorus donor concentration raised from 100 ppm to 1000 ppm (both in the moderate doping regime). What will happen to its electrical conductivity:

a) It will stay nearly constant, because silicon covalent bonds saturate above 100 ppm
b) It will decrease roughly tenfold, because phosphorus atoms scatter electrons ten times more strongly
c) It will decrease slightly, because excess phosphorus converts the crystal from n-type to p-type
d) It will increase roughly tenfold, because carrier density scales with doping while mobility stays nearly constant

### Answer

d

### Explanation

Session 13, Slides 26, 36 and 42: in the moderate doping range ($\sim 100$ to $1000$ ppm), crystal distortion by the dopant is small so $\mu_e$ changes little, while all donors are ionised at room temperature, so increasing dopant concentration tenfold multiplies $n_e$ and $\sigma \approx n_e|q_e|\mu_e$ by roughly ten.

- a) Saturation of ionisation with temperature occurs in the exhaustion range for fixed doping; adding ten times more dopant atoms supplies ten times more carriers.
- b) Inverted effect: at moderate concentrations impurity scattering is modest and does not offset the tenfold rise in carrier concentration.
- c) Phosphorus remains a group VA donor at 1000 ppm and keeps the silicon n-type.

### Source

Session 13, Slides 26, 36 and 42; Problems T6 and T7, Problem 9 c.

## Q55.7 Dopants that produce p-type silicon

- id: B55-Q7
- concept_id: u6-dopant-identification
- format: identify
- asks: classification

Which pair of substitutional dopants will both make pure silicon a p-type extrinsic semiconductor?

a) Phosphorus and arsenic
b) Antimony and boron
c) Boron and indium
d) Arsenic and antimony

### Answer

c

### Explanation

Session 13, Slides 35 and 37: silicon has four valence electrons (group IVA), so p-type doping requires group IIIA elements with three valence electrons (acceptors), such as boron (B) and indium (In).

- a) Both phosphorus and arsenic belong to group VA (five valence electrons) and act as donors (n-type).
- b) Boron is a group IIIA acceptor, but antimony is a group VA donor.
- d) Both arsenic and antimony belong to group VA and produce n-type silicon.

### Source

Session 13, Slides 35-37.

## Q55.8 Why the carriers control the conductivity

- id: B55-Q8
- concept_id: u6-carrier-number-control
- format: cause-effect
- asks: cause

In an extrinsic semiconductor at moderate dopant concentrations, the electrical conductivity is controlled by the number of charge carriers because the doping:

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

## Q55.9 Extrinsic versus intrinsic silicon at room temperature

- id: B55-Q9
- concept_id: u6-extrinsic-intrinsic-comparison
- format: topic-true
- asks: comparison

Referring to the conductivity of doped extrinsic silicon versus pure intrinsic silicon at room temperature, indicate which statement is TRUE:

a) Pure silicon conducts much better than doped silicon because dopant atoms break lattice periodicity and cut mobility
b) Both have almost identical conductivity at 300 K because thermal excitation across the 1.1 eV gap dominates both samples
c) Extrinsic doping raises conductivity solely by increasing electron mobility $\mu_e$, while carrier density stays near $10^{16}$ m⁻³
d) Even trace ppm doping adds orders of magnitude more carriers than $n_i$, raising conductivity dramatically over pure silicon

### Answer

d

### Explanation

Session 13, Slides 26, 31, 36 and 42 (Problem 9 b): pure silicon has $n_i = 1.5\times10^{16}$ m⁻³ ($\sigma \approx 4\times10^{-4}$ (Ω·m)⁻¹), whereas even 1 ppm of phosphorus or boron supplies $\sim 5\times10^{22}$ carriers/m³, multiplying the room-temperature conductivity by many orders of magnitude.

- a) While dopants add minor scattering at high levels, the huge gain in carrier number overwhelms any mobility drop.
- b) Intrinsic excitation across $1.1$ eV at 300 K produces negligible carriers compared with shallow-level dopant ionisation.
- c) Doping increases carrier concentration $n$ or $p$ by orders of magnitude while slightly lowering or leaving $\mu$ nearly constant (Slide 42).

### Source

Session 13, Slides 26, 31, 36 and 42; Problems T6 and T7, Problem 9 b.

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
