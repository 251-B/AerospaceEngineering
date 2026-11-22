---
materia: Aerospace Materials I
tema: "Unit 6: intrinsic semiconductors applied: conductivity against temperature, carrier concentration, band gap from data, bonding and mobility"
bank_id: B54
title: "Intrinsic semiconductors applied"
category: mt2_test_block
unit: 6
concepts:
  - u6-intrinsic-temperature-concept
  - u6-intrinsic-conductivity-calc
  - u6-gap-and-bonding
  - u6-two-lines-gap-ratio
  - u6-band-gap-trend-bonding
  - u6-band-gap-classification
  - u6-germanium-three-temperatures
  - u6-metal-vs-semiconductor-heating
  - u6-intrinsic-mobility-purity
  - u6-photon-gap-excitation
difficulty: 2
origen: "Questions written for the bank in the style of Part I of MATERIALS_SECONDPARTIAL_2019.pdf; not official exercises. Content and data from Session 13 Slides 25-34 and 46."
tags:
  - problem-bank
  - midterm-2
  - test-block
  - unit-6
---

# Bank B54 — Intrinsic semiconductors applied

> [!info] Practice item, not an official exercise
> Ten test questions written for the bank in the style of Part I of Assessment Test II (four options, one right answer; +0.5 right, -0.15 wrong). Content: Session 13, Slides 25-34 and 46.

## Q54.1 Intrinsic semiconductors under heating

- id: B54-Q1
- concept_id: u6-intrinsic-temperature-concept
- format: topic-true
- asks: cause

Regarding intrinsic semiconductors under changing temperature, indicate which statement is TRUE:

a) Carrier concentration stays constant with temperature, so conductivity falls slightly due to lattice scattering
b) Raising temperature excites electrons across $E_g$, which increases carrier mobility and raises conductivity
c) Exponential carrier generation across $E_g$ outweighs the drop in carrier mobility, so $\sigma$ rises strongly on heating
d) At absolute zero ($0$ K), pure silicon conducts moderately because many covalent bonds remain broken

### Answer

c

### Explanation

Session 13, Slide 29: in an intrinsic semiconductor $n = p = n_i \propto \exp(-E_g/2kT)$ rises exponentially with temperature; although thermal vibrations reduce carrier mobility, this loss is masked by the rapid rise in carrier density, so $\sigma$ increases strongly.

- a) Describes a metal rather than an intrinsic semiconductor: metals have fixed $n$, whereas intrinsic semiconductors create new electron-hole pairs on heating.
- b) Correctly notes $\sigma$ rises, but attributes it to rising mobility instead of rising carrier concentration; lattice scattering actually lowers mobility.
- d) At 0 K there is no thermal energy to excite electrons across $E_g$, so the valence band is full and the conduction band is empty (Slide 31).

### Source

Session 13, Slides 29 and 31.

## Q54.2 Intrinsic conductivity formula

- id: B54-Q2
- concept_id: u6-intrinsic-conductivity-calc
- format: topic-false
- asks: cause

With respect to the intrinsic conductivity relation $\sigma = n|q_e|(\mu_e + \mu_h)$, indicate which statement is FALSE:

a) Electrons and holes contribute equally to the total current because their carrier concentrations are equal ($n = p$)
b) Electrons carry the larger share of the current in pure silicon and germanium because $\mu_e > \mu_h$
c) Raising chemical and structural purity reduces defect scattering and supports higher carrier mobilities
d) Each thermal excitation across the band gap generates one conduction electron and one valence-band hole

### Answer

a

### Explanation

Session 13, Slides 28 and 33: although $n = p = n_i$, the electron contribution $n|q_e|\mu_e$ and hole contribution $p|q_e|\mu_h$ are unequal because $\mu_e > \mu_h$ (e.g., 0.135 against 0.048 m²/(V·s) in Si). Statement a) is false.

- b) True (Slides 28 and 33): since $\mu_e > \mu_h$ while $n = p$, electrons carry the majority of the intrinsic current.
- c) True (Slide 33): high chemical and structural purity reduces scattering centres and favours high carrier mobility.
- d) True (Slides 27-28): promoting one electron leaves one hole behind, keeping $n = p$.

### Source

Session 13, Slides 27-28 and 33.

## Q54.3 Silicon against germanium at room temperature

- id: B54-Q3
- concept_id: u6-gap-and-bonding
- format: topic-true
- asks: application

Referring to pure silicon ($E_g = 1.11$ eV) and pure germanium ($E_g = 0.67$ eV) at room temperature, indicate which statement is TRUE:

a) Silicon has a higher intrinsic carrier concentration $n_i$ than germanium because its atoms are smaller
b) Germanium has a higher intrinsic conductivity than silicon because its smaller band gap permits far more thermal carriers
c) Silicon conducts better than germanium because stronger covalent bonds let electrons move without scattering
d) Germanium behaves as an insulator at 300 K because a $0.67$ eV gap exceeds the thermal threshold

### Answer

b

### Explanation

Session 13, Slides 29, 31 and 33: since $n_i \propto \exp(-E_g/2kT)$, the narrower band gap of germanium ($0.67$ eV vs $1.11$ eV in Si) yields a much larger intrinsic carrier concentration ($2.4\times10^{19}$ vs $1.5\times10^{16}$ m⁻³) and higher intrinsic conductivity ($2.2$ vs $4\times10^{-4}$ (Ω·m)⁻¹).

- a) Inverts the atomic-size and gap trend: smaller Si atoms form stronger bonds with a wider gap, yielding fewer intrinsic carriers.
- c) Stronger covalent bonds widen $E_g$ and decrease intrinsic conductivity rather than raising it.
- d) Insulators have $E_g > 2$ eV (Slide 8); $0.67$ eV is well within the semiconductor regime.

### Source

Session 13, Slides 8, 29, 31 and 33.

## Q54.4 Two intrinsic semiconductors on an Arrhenius plot

- id: B54-Q4
- concept_id: u6-two-lines-gap-ratio
- format: diagram-reading
- asks: figure-reading

The plot shows $\ln\sigma$ against $1/T$ for two intrinsic semiconductors A and B. Which statement about their band gaps is TRUE?

![[attachments/MAT-MT2/u6-b54-two-lines.svg]]

a) Material B has the larger band gap because its line sits higher on the right side (lower temperatures)
b) Both materials have the same band gap because both plot $\ln\sigma$ as straight lines against $1/T$
c) Material A has the smaller band gap because its conductivity decreases more rapidly as $1/T$ increases
d) Material A has the larger band gap because the Arrhenius slope $-E_g/2k$ of line A is steeper

### Answer

d

### Explanation

Session 13, Slide 29: $\ln\sigma = \ln\sigma_0 - (E_g/2k)(1/T)$, so the slope magnitude is directly proportional to $E_g$. Line A drops more steeply as $1/T$ increases, showing a steeper negative slope and therefore a larger band gap than B.

- a) Confuses the vertical value $\ln\sigma$ at one temperature (which also depends on $\sigma_0$) with the slope $-E_g/2k$ that measures the band gap.
- b) A straight line confirms the Arrhenius law $\sigma = \sigma_0\exp(-E_g/2kT)$, not equal band gaps; different slopes mean different $E_g$.
- c) Inverts the relation between slope steepness and band gap: a steeper drop means a larger $E_g$, not a smaller one.

### Source

Session 13, Slide 29.

## Q54.5 Energy band gap and atomic bonding

- id: B54-Q5
- concept_id: u6-band-gap-trend-bonding
- format: topic-true
- asks: cause

Referring to the energy band gap $E_g$ of solids and its relation to atomic bonding, indicate which statement is TRUE:

a) Moving down group IVA from silicon to germanium decreases atomic size and widens the band gap
b) Increasing ionic character in compound semiconductors narrows $E_g$ and raises intrinsic conductivity
c) Increasing ionic character or bond strength widens $E_g$, lowering intrinsic carrier excitation across the gap
d) Pure metals possess a narrow band gap below $0.5$ eV that valence electrons cross without resistance

### Answer

c

### Explanation

Session 13, Slides 8 and 31-32: as covalent character decreases and ionic character increases (from group 14 elements to 13-15 and 12-16 compounds, and toward ionic insulators), electrons are held more tightly, $E_g$ widens and intrinsic conductivity falls.

- a) Down group IVA, atoms become larger (Ge > Si), weakening covalent overlap and shrinking $E_g$ ($0.67$ eV < $1.11$ eV).
- b) Inverts the ionic-character trend of Slide 32: more ionic bonding widens $E_g$ and reduces intrinsic conductivity.
- d) Metals have half-filled or overlapping bands with empty states right above $E_f$ and no band gap (Slide 6).

### Source

Session 13, Slides 6, 8 and 31-32.

## Q54.6 Energy band gap classification

- id: B54-Q6
- concept_id: u6-band-gap-classification
- format: topic-false
- asks: classification

Referring to the energy band gap separating conductors, semiconductors and insulators, indicate which statement is FALSE:

a) Insulators such as polyethylene and diamond have a filled valence band and a wide band gap ($E_g > 2$ eV)
b) Intrinsic semiconductors conduct slightly at 0 K because their narrow gap ($E_g < 2$ eV) stays partly filled with valence states
c) Metallic conductors have a half-filled valence band or overlapping bands, leaving no energy gap above $E_f$
d) Intrinsic semiconductors have a filled valence band and an empty conduction band at 0 K separated by $E_g < 2$ eV

### Answer

b

### Explanation

Session 13, Slides 8, 25 and 31: a band gap is an energy range with zero allowed electron states, and at 0 K an intrinsic semiconductor has a completely full valence band and completely empty conduction band with no carriers. Statement b) is false.

- a) True (Slide 8): insulators are characterised by $E_g > 2$ eV (e.g., diamond 6-7 eV).
- c) True (Slide 6): conductors provide empty states immediately above $E_f$ without crossing any gap.
- d) True (Slides 8 and 31): semiconductors have $E_g < 2$ eV and an empty conduction band at 0 K.

### Source

Session 13, Slides 6, 8, 25 and 31.

## Q54.7 Pure germanium at three temperatures

- id: B54-Q7
- concept_id: u6-germanium-three-temperatures
- format: ordering
- asks: comparison

Order pure germanium at 0 °C, 25 °C and 50 °C from the highest to the lowest electrical conductivity:

a) 0 °C, 25 °C, 50 °C
b) 25 °C, 50 °C, 0 °C
c) 25 °C and 50 °C equal, then 0 °C
d) 50 °C, 25 °C, 0 °C

### Answer

d

### Explanation

Session 13, Slide 29 and Problems T6 and T7, Problem 9a: in an intrinsic semiconductor $n$ and $p$ grow as $\exp(-E_g/2kT)$ and this masks the loss of mobility, so $\sigma$ increases with $T$: $\sigma_{50} > \sigma_{25} > \sigma_{0}$.

- a) The trend of a metal was applied: conductivity falling as the material is heated.
- b) A maximum at room temperature was assumed, as if the lattice disorder won beyond 25 °C; in the intrinsic range the carrier number wins.
- c) The saturation of an extrinsic semiconductor was assumed; pure germanium has no dopant levels to exhaust.

### Source

Session 13, Slide 29; Problems T6 and T7, Problem 9a.

## Q54.8 Copper wire and intrinsic silicon heated

- id: B54-Q8
- concept_id: u6-metal-vs-semiconductor-heating
- format: what-happens
- asks: comparison

Which one of the following statements about a copper wire and a piece of intrinsic silicon, both heated from 20 to 100 °C, is TRUE?

a) Both conduct better, as the heating frees more carriers in each of them
b) Both conduct worse, as the vibrations of the lattice scatter the carriers in each of them
c) The copper conducts worse because of more collisions, the silicon better because of more carriers
d) The copper conducts better because of more carriers, the silicon worse because of more collisions

### Answer

c

### Explanation

Session 13, Slides 14, 29 and 30 (Problem 4): in the metal the number of electrons is fixed and the thermal vibrations increase the collisions, so $\rho_T$ rises; in the intrinsic semiconductor the number of electrons and holes grows exponentially, so $\sigma$ rises and $\rho$ falls.

- a) The disorder effect was applied to both; in the semiconductor it is masked by the larger number of carriers.
- b) The carrier excitation was applied to both; a metal has no gap to cross.
- d) The two behaviours were swapped.

### Source

Session 13, Slides 14, 29 and 30; Problems T6 and T7, Problem 4.

## Q54.9 Dominant carrier in intrinsic silicon

- id: B54-Q9
- concept_id: u6-intrinsic-mobility-purity
- format: cause-effect
- asks: cause

In an intrinsic semiconductor such as pure silicon, the electrons contribute a larger fraction of the total conductivity than the holes because:

a) Conduction-band electrons move with higher mobility than valence-band holes ($\mu_e > \mu_h$)
b) Thermal excitation across the band gap produces roughly three times as many electrons as holes
c) Conduction electrons carry twice the magnitude of electric charge carried by valence-band holes
d) Valence holes stay pinned to impurity sites while electrons travel freely through the lattice

### Answer

a

### Explanation

Session 13, Slides 28 and 33: in an intrinsic semiconductor $n = p$ and $|q_e| = |q_h|$, so the electron and hole fractions of $\sigma = n|q_e|\mu_e + p|q_e|\mu_h$ are $\mu_e/(\mu_e+\mu_h)$ and $\mu_h/(\mu_e+\mu_h)$; because $\mu_e > \mu_h$, electrons carry the larger share.

- b) Equal numbers of electrons and holes ($n = p$) are produced by excitation across the gap.
- c) Both electrons and holes carry the same charge magnitude, $1.602\times10^{-19}$ C.
- d) Pure intrinsic semiconductors contain no dopant sites, and holes are mobile carriers in the valence band.

### Source

Session 13, Slides 28 and 33.

## Q54.10 Photon and band gap

- id: B54-Q10
- concept_id: u6-photon-gap-excitation
- format: identify
- asks: application

Photons of energy 1.25 eV fall on the intrinsic semiconductors of the table. In which of them can a photon excite an electron from the valence band to the conduction band?

| Material | $E_g$ (eV) |
| :--- | :---: |
| Si | 1.11 |
| Ge | 0.67 |
| GaAs | 1.42 |
| Diamond | 6.0 |

a) Si, Ge and GaAs
b) Si and Ge
c) GaAs and Diamond
d) Ge and GaAs

### Answer

b

### Explanation

Session 13, Slides 8, 33 and 46: an electron jumps across the band gap only when the absorbed photon energy is at least $E_g$. With 1.25 eV that holds for Ge ($0.67$ eV) and Si ($1.11$ eV); the photon energy is below the gap of GaAs ($1.42$ eV) and diamond ($6.0$ eV).

- a) GaAs was included because 1.42 eV is close to 1.25 eV; the photon energy must equal or exceed $E_g$.
- c) The condition was inverted: the materials whose band gap exceeds the photon energy were selected.
- d) Silicon ($1.11$ eV) was missed while GaAs ($1.42$ eV) was wrongly included.

### Source

Session 13, Slides 8, 33 and 46.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
