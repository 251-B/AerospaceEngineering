---
materia: Aerospace Materials I
tema: "Unit 8: ceramic point defects (Schottky and Frenkel), aliovalent impurity charge compensation (Ca2+ in NaCl, Al2O3 in MgO, Y2O3/CaO in ZrO2) and ionic lattice energy trends"
bank_id: B69
title: "Ceramic point defects and ionic lattice energy"
category: mt3_test_block
unit: 8
concepts:
  - u8-schottky-frenkel-defects
  - u8-frenkel-cation-preference
  - u8-aliovalent-doping-nacl
  - u8-aliovalent-doping-zro2
  - u8-aliovalent-mgo-vacancy-calc
  - u8-ionic-lattice-energy-factors
  - u8-ionic-hardness-radius-trend
  - u8-ionic-lattice-energy-matching
  - u8-schottky-mgo-vs-nacl
difficulty: 2
origen: "Includes Question 7 of MATERIALS_FINALEXAM_2015_EXTRA.pdf (p. 8) alongside practice items in the style of Part I of Assessment Test III. Content from Session 2 Slides 9-13, Session 4 Slides 17-18 and 22, Session 13 Slide 22, Session 16 Slide 10, Session 18 Slide 41, and Problems T2 defects Problem 3."
tags:
  - problem-bank
  - midterm-3
  - test-block
  - unit-8
---

# Bank B69 — Ceramic point defects and ionic lattice energy

> [!info] Includes official exam questions
> Ten test questions in the style of Part I of Assessment Test III (four options, one right answer; +0.5 right, -0.15 wrong). Questions 7 and 9 adapt Question 7 of `MATERIALS_FINALEXAM_2015_EXTRA.pdf`; the remaining eight are practice items. Content: Session 2, Slides 9-13; Session 4, Slides 17-18 and 22; Session 13, Slide 22; Session 16, Slide 10; Session 18, Slide 41; Problems T2 defects, Problem 3.

## Q69.1 Schottky and Frenkel defects in ionic ceramics

- id: B69-Q1
- concept_id: u8-schottky-frenkel-defects
- format: topic-true
- asks: comparison

Referring to intrinsic point defects (Schottky and Frenkel) in stoichiometric ionic ceramics, indicate which statement is TRUE:

a) An isolated single cation vacancy preserves crystal electroneutrality just as well as a paired Schottky defect
b) A Frenkel defect removes one cation and one anion from the crystal interior to the external surface
c) A Schottky defect is a pair of oppositely charged vacancies, whereas a Frenkel defect is a vacancy–interstitial pair
d) In any ionic crystal, Schottky and Frenkel defects always exist in identical equilibrium concentrations

### Answer

c

### Explanation

Session 4, Slides 17-18: to preserve electrical neutrality in an ionic crystal, intrinsic point defects appear as charge-balanced combinations—either a **Schottky defect** (one cationic vacancy plus one anionic vacancy) or a **Frenkel defect** (an ion displaced from its regular lattice site into an interstitial site, creating a vacancy–interstitial pair).

- a) Removing a single ion leaves an uncompensated net electric charge, violating macroscopic electroneutrality.
- b) Swaps the two defect mechanisms: removing an ion pair to the surface defines a Schottky defect, not a Frenkel defect.
- d) In a given crystal, $\Delta H_S \neq \Delta H_F$, and the defect with the lower formation energy dominates exponentially.

### Source

Session 4, Slides 17-18.

## Q69.2 Effect of Schottky versus Frenkel defects on density

- id: B69-Q2
- concept_id: u8-schottky-frenkel-defects
- format: what-happens
- asks: effect

When an ionic ceramic develops a high concentration of Schottky defects rather than Frenkel defects upon heating (assuming a constant unit-cell volume), what happens to its macroscopic mass density?

a) It decreases, because ions leave interior lattice sites to form paired cation and anion vacancies
b) It increases, because extra interstitial ions crowd into the empty voids of each unit cell
c) It remains strictly unchanged, because ions merely shift from lattice sites into nearby interstitial holes
d) It drops abruptly to zero near $1000\text{ K}$ as $\Delta H_S$ becomes negative

### Answer

a

### Explanation

Session 4, Slides 17-18: in a Schottky defect, equal charge equivalents of cations and anions are missing from interior lattice sites (effectively moved to the surface), reducing the mass per unit cell at nearly fixed lattice parameter and thus lowering density, whereas a Frenkel defect keeps every ion inside the crystal and conserves mass.

- b) Incorrectly introduces extra interstitial mass that neither Schottky nor Frenkel defects add to a stoichiometric crystal.
- c) Describes mass conservation in a *Frenkel* defect (where an ion stays inside the crystal in an interstitial hole), not a Schottky defect.
- d) Misstates defect thermodynamics: $\Delta H_S > 0$, and equilibrium vacancy fractions remain small ($n_S/N \ll 1$).

### Source

Session 4, Slides 17-18.

## Q69.3 Why cations dominate Frenkel defects

- id: B69-Q3
- concept_id: u8-frenkel-cation-preference
- format: cause-effect
- asks: cause

When Frenkel defects form in an ionic ceramic, they predominantly involve displaced cations rather than displaced anions because:

a) anions carry negative charge and are repelled by positive interstitial holes
b) an ionic unit cell contains twice as many cation interstitial sites as anion sites
c) anion vacancies violate crystal electroneutrality whereas cation vacancies do not
d) cations are typically much smaller than anions ($r_C < r_A$), fitting into interstitial holes with far less lattice strain

### Answer

d

### Explanation

Session 4, Slides 17-18 and Session 13, Slide 22 (Problems T6 and T7, Problem 3): in ionic crystals $r_{\text{cation}} < r_{\text{anion}}$, so displacing a small cation into an interstitial void requires much lower formation energy $\Delta H_F$ than forcing a bulky anion into a tight interstitial site.

- a) Confuses geometric size mismatch with electrostatic sign; interstitial voids lie between anions and cations alike.
- b) Interstitial voids belong to the crystal lattice as a whole rather than separating into distinct cation vs anion void counts.
- c) Both cation and anion Frenkel pairs keep the displaced ion inside the crystal, so neither violates electroneutrality.

### Source

Session 4, Slides 17-18; Session 13, Slide 22; Problems T6 and T7, Problem 3.

## Q69.4 Charge compensation of Ca2+ impurities in NaCl

- id: B69-Q4
- concept_id: u8-aliovalent-doping-nacl
- format: complete-sentence
- asks: application

When a small amount of $\text{CaCl}_2$ dissolves substitutionally in $\text{NaCl}$ so that $\text{Ca}^{2+}$ ions replace $\text{Na}^+$ ions on the cation sublattice, electrical neutrality is maintained by creating:

a) one $\text{Cl}^-$ anion vacancy for every $\text{Ca}^{2+}$ ion incorporated
b) one $\text{Na}^+$ cation vacancy for every $\text{Ca}^{2+}$ ion incorporated
c) one $\text{Na}^+$ interstitial ion for every $\text{Ca}^{2+}$ ion incorporated
d) two $\text{Cl}^-$ anion vacancies for every $\text{Ca}^{2+}$ ion incorporated

### Answer

b

### Explanation

Session 4, Slide 22 (electroneutrality in ionic solid solutions): each $\text{Ca}^{2+}$ replacing a $\text{Na}^+$ introduces an excess positive charge of $+1$. Neutrality is restored by leaving one $\text{Na}^+$ site vacant per $\text{Ca}^{2+}$ ion ($2\,\text{Na}^+ \leftrightarrow \text{Ca}^{2+} + 1\,V_{\text{Na}}$), keeping total cation charge $+2$ on both sides.

- a) Anion vacancies remove negative charge and add another $+1$ charge deficit instead of cancelling the $+1$ excess from $\text{Ca}^{2+}$.
- c) Adding an extra $\text{Na}^+$ interstitial doubles the excess positive charge instead of compensating it.
- d) Two $\text{Cl}^-$ vacancies would create an even larger positive charge imbalance ($+3$ excess).

### Source

Session 4, Slide 22.

## Q69.5 Oxygen vacancies from lower-valence dopants in ZrO2

- id: B69-Q5
- concept_id: u8-aliovalent-doping-zro2
- format: topic-true
- asks: application

Referring to zirconia ($\text{ZrO}_2$) doped with lower-valence oxides such as $\text{CaO}$ ($\text{Ca}^{2+}$) or $\text{Y}_2\text{O}_3$ ($\text{Y}^{3+}$) substituting for $\text{Zr}^{4+}$, indicate which statement is TRUE:

a) Adding $\text{Ca}^{2+}$ or $\text{Y}^{3+}$ creates $\text{Zr}^{4+}$ cation vacancies to cancel excess positive charge
b) Adding $\text{Y}_2\text{O}_3$ introduces $\text{O}^{2-}$ interstitial ions because $\text{Y}^{3+}$ has higher valence than $\text{Zr}^{4+}$
c) Doping with $\text{Y}_2\text{O}_3$ suppresses ionic conductivity at high temperature by eliminating lattice vacancies
d) Substituting $\text{Ca}^{2+}$ or $\text{Y}^{3+}$ creates $\text{O}^{2-}$ anion vacancies that preserve neutrality, stabilize fluorite $\text{YSZ}$, and allow $\text{O}^{2-}$ conduction

### Answer

d

### Explanation

Session 4, Slide 22, Session 13, Slide 22, Session 16, Slide 10, and Session 18, Slide 41: replacing $\text{Zr}^{4+}$ with lower-valence $\text{Ca}^{2+}$ (charge $-2$ relative to host) or two $\text{Y}^{3+}$ ($2\times(-1) = -2$) requires positive charge compensation, which forms one oxygen ($\text{O}^{2-}$) vacancy per $\text{Ca}^{2+}$ or per two $\text{Y}^{3+}$; these extrinsic oxygen vacancies stabilize cubic fluorite $\text{YSZ}$ and enable oxygen-ion conduction in solid oxide fuel cells and gas sensors.

- a) Confuses lower-valence doping in $\text{ZrO}_2$ with higher-valence doping ($\text{Al}^{3+}$ in $\text{MgO}$); cation vacancies would worsen the positive-charge deficit.
- b) Inverts the valences of $\text{Y}^{3+}$ ($+3$) and $\text{Zr}^{4+}$ ($+4$) and proposes interstitial anions despite their large size.
- c) Inverts the effect of doping on ionic ceramics: extrinsic vacancies created by aliovalent doping dramatically *increase* high-temperature ionic conductivity.

### Source

Session 4, Slide 22; Session 13, Slide 22; Session 16, Slide 10; Session 18, Slide 41.

## Q69.6 Cationic vacancy concentration in MgO doped with Al2O3

- id: B69-Q6
- concept_id: u8-aliovalent-mgo-vacancy-calc
- format: numeric
- asks: calculation
- calc: 1/99

When $1.0\text{ mol}$ of $\text{Al}_2\text{O}_3$ is dissolved in $99\text{ mol}$ of $\text{MgO}$ ($3\,\text{Mg}^{2+} \leftrightarrow 2\,\text{Al}^{3+} + 1\,V_{\text{Mg}}$), determine the ratio of $\text{Mg}^{2+}$ vacancies generated per mole of $\text{MgO}$:

a) 0.0202 mol vacancies/mol MgO
b) 0.0303 mol vacancies/mol MgO
c) 0.0101 mol vacancies/mol MgO
d) 0.0051 mol vacancies/mol MgO

### Answer

c

### Explanation

Session 4, Slide 22 and Problems T2 defects, Problem 3a: each mole of $\text{Al}_2\text{O}_3$ supplies $2\text{ mol}$ of $\text{Al}^{3+}$ (charge $+6$), replacing $3\text{ mol}$ of $\text{Mg}^{2+}$ and leaving $1.0\text{ mol}$ of cationic vacancies $V_{\text{Mg}}$. Dividing by $99\text{ mol}$ of $\text{MgO}$ gives $1.0/99 = 0.0101\ \text{mol vacancies/mol MgO}$.

- a) Generated one vacancy per $\text{Al}^{3+}$ ion ($2/99 = 0.0202$) instead of one vacancy per two $\text{Al}^{3+}$ ions.
- b) Reported all replaced $\text{Mg}^{2+}$ sites ($3/99 = 0.0303$) rather than the empty vacant sites ($1/99$).
- d) Halved the vacancy count again ($0.5/99 = 0.0051$), underestimating the charge deficit.

### Source

Session 4, Slide 22; Problems T2 defects, Problem 3a.

## Q69.7 Parameters governing ionic lattice energy

- id: B69-Q7
- concept_id: u8-ionic-lattice-energy-factors
- format: topic-false
- asks: cause
- origin: official-exam

Regarding the magnitude of the lattice energy $|U| = \dfrac{Z_1 Z_2 e^2 N_A A}{4\pi\varepsilon_0 a_0}\left(1 - \dfrac{1}{n}\right)$ of binary ionic solids, indicate which statement is FALSE:

a) Increasing ionic valences $Z_1$ and $Z_2$ raises $|U|$ sharply, so divalent oxides melt much higher than monovalent halides
b) Increasing cation or anion radius shortens the equilibrium separation $a_0$ and increases lattice energy and melting point
c) At equal ionic charges, a smaller equilibrium spacing $a_0 = r_C + r_A$ produces a higher lattice energy and higher hardness
d) A larger lattice energy corresponds to a deeper potential energy well, raising $T_m$ and $E$ while lowering thermal expansion

### Answer

b

### Explanation

MATERIALS_FINALEXAM_2015_EXTRA.pdf, p. 8 (Q7a) and Session 2, Slides 9-13: lattice energy depends directly on ionic charges ($Z_1 Z_2$) and inversely on equilibrium interionic distance ($a_0 = r_C + r_A$). Increasing ionic radius *increases* $a_0$ and therefore *decreases* $|U|$, lowering $T_m$ and hardness. Statement b) is false.

- a) True (Session 2, Slide 10): $+2/-2$ oxides such as $\text{MgO}$ ($940\text{ kcal/mol}$, $T_m = 2800\ ^\circ\text{C}$) far exceed $+1/-1$ halides such as $\text{NaCl}$ ($183\text{ kcal/mol}$, $801\ ^\circ\text{C}$).
- c) True (Session 2, Slides 10-11): $\text{NaCl}$ ($r_{\text{Na}^+} < r_{\text{K}^+}$) has higher $|U|$ and higher hardness than $\text{KCl}$, and $\text{MgO}$ exceeds $\text{BaO}$.
- d) True (Session 2, Slides 10-13): higher binding energy produces a deeper, steeper well with higher $T_m$, higher $E$, and lower $\alpha$.

### Source

MATERIALS_FINALEXAM_2015_EXTRA.pdf, p. 8 (Q7a); Session 2, Slides 9-13.

## Q69.8 Hardness trend across alkaline-earth oxides

- id: B69-Q8
- concept_id: u8-ionic-hardness-radius-trend
- format: ordering
- asks: comparison

Given that the cation radius increases down group IIA ($r_{\text{Be}^{2+}} < r_{\text{Mg}^{2+}} < r_{\text{Ca}^{2+}} < r_{\text{Ba}^{2+}}$), rank $\text{BeO}$, $\text{MgO}$, $\text{CaO}$, and $\text{BaO}$ in order of increasing Mohs hardness:

a) $\text{BaO} < \text{CaO} < \text{MgO} < \text{BeO}$
b) $\text{BeO} < \text{MgO} < \text{CaO} < \text{BaO}$
c) $\text{CaO} < \text{BaO} < \text{MgO} < \text{BeO}$
d) $\text{BaO} < \text{MgO} < \text{CaO} < \text{BeO}$

### Answer

a

### Explanation

Session 2, Slide 11: for divalent oxides with constant charge ($+2/-2$), smaller cation radius $r_{C^+}$ shortens $d = r_C + r_A$, increasing lattice energy $|U|$ and Mohs hardness ($\text{BaO}: d=2.77\text{ Å}, 3.3$; $\text{CaO}: d=2.40\text{ Å}, 4.5$; $\text{MgO}: d=2.10\text{ Å}, 6.5$; $\text{BeO}: d=1.65\text{ Å}, 9.0$).

- b) Reverses the trend into decreasing hardness (increasing ionic radius) instead of increasing hardness.
- c) Swaps $\text{CaO}$ ($4.5$) and $\text{BaO}$ ($3.3$), mistaking the larger $\text{Ba}^{2+}$ ion for the harder oxide.
- d) Swaps $\text{MgO}$ ($6.5$) and $\text{CaO}$ ($4.5$) in the middle of the series.

### Source

Session 2, Slide 11.

## Q69.9 Matching NaCl, KCl, MgO and BaO to U, Tm and hardness

- id: B69-Q9
- concept_id: u8-ionic-lattice-energy-matching
- format: diagram-reading
- asks: application
- origin: official-exam

Using the influence of ion valence and ionic radius ($r_{\text{Na}^+} < r_{\text{K}^+}$, $r_{\text{Mg}^{2+}} < r_{\text{Ba}^{2+}}$) on lattice energy, match $\text{MgO}$, $\text{BaO}$, $\text{NaCl}$, and $\text{KCl}$ to Rows 1 to 4 of the table below:

| Row | $|U|$ (kcal/mol) | $T_m$ (°C) | Mohs hardness |
| :--- | ---: | ---: | ---: |
| 1 | 940 | 2800 | 6.5 |
| 2 | 747 | 1923 | 3.3 |
| 3 | 183 | 801 | 2.5 |
| 4 | 164 | 776 | 2.25 |

a) 1: $\text{BaO}$, 2: $\text{MgO}$, 3: $\text{KCl}$, 4: $\text{NaCl}$
b) 1: $\text{MgO}$, 2: $\text{NaCl}$, 3: $\text{BaO}$, 4: $\text{KCl}$
c) 1: $\text{KCl}$, 2: $\text{NaCl}$, 3: $\text{BaO}$, 4: $\text{MgO}$
d) 1: $\text{MgO}$, 2: $\text{BaO}$, 3: $\text{NaCl}$, 4: $\text{KCl}$

### Answer

d

### Explanation

MATERIALS_FINALEXAM_2015_EXTRA.pdf, p. 8 (Q7b) and Session 2, Slides 10-11: divalent oxides ($Z_1 Z_2 = 4$) have far higher $|U|$, $T_m$, and hardness than monovalent halides ($Z_1 Z_2 = 1$). Within each valence pair, the smaller cation gives higher $|U|$, $T_m$, and hardness: $\text{MgO} > \text{BaO}$ ($940 > 747\text{ kcal/mol}$) and $\text{NaCl} > \text{KCl}$ ($183 > 164\text{ kcal/mol}$).

- a) Inverts the ionic radius trend within both pairs, placing larger $\text{Ba}^{2+}$ above $\text{Mg}^{2+}$ and larger $\text{K}^+$ above $\text{Na}^+$.
- b) Places monovalent $\text{NaCl}$ above divalent $\text{BaO}$, ignoring the dominant $Z_1 Z_2$ charge factor.
- c) Reverses the entire order from lowest lattice energy (Row 1) to highest (Row 4).

### Source

MATERIALS_FINALEXAM_2015_EXTRA.pdf, p. 8 (Q7b); Session 2, Slides 10-11.

## Q69.10 Schottky concentration in MgO versus NaCl

- id: B69-Q10
- concept_id: u8-schottky-mgo-vs-nacl
- format: cause-effect
- asks: comparison

At $1000\text{ K}$, the equilibrium Schottky defect concentration in $\text{MgO}$ ($\Delta H_S = 10.57\times 10^{-19}\text{ J/defect}$) is roughly eleven orders of magnitude lower than in $\text{NaCl}$ ($\Delta H_S = 3.69\times 10^{-19}\text{ J/defect}$) because:

a) $\text{MgO}$ adopts the fluorite crystal structure, which lacks octahedral cation sites
b) equilibrium vacancy concentration varies linearly with $1/\Delta H_S$ rather than exponentially
c) doubly charged $\text{Mg}^{2+}$ and $\text{O}^{2-}$ ions have a much higher $\Delta H_S$, suppressing $\exp(-\Delta H_S/2k_B T)$
d) $\text{NaCl}$ cannot form Schottky pairs and accommodates vacancies only via Frenkel interstitials

### Answer

c

### Explanation

Session 4, Slide 18: equilibrium Schottky concentration follows $n_S = N\exp(-\Delta H_S / 2k_B T)$. Because $\text{Mg}^{2+}$ and $\text{O}^{2-}$ carry double charges and bind much more strongly than $\text{Na}^+$ and $\text{Cl}^-$, $\Delta H_S(\text{MgO})$ is nearly three times $\Delta H_S(\text{NaCl})$, making Schottky vacancies far harder to form in $\text{MgO}$ ($1.39\times 10^{7}$ vs $9.38\times 10^{17}$ per mol at $1000\text{ K}$).

- a) Misstates $\text{MgO}$'s crystal structure: $\text{MgO}$ has the rock salt ($\text{NaCl}$) structure, the same structure as $\text{NaCl}$.
- b) Ignores the exponential Arrhenius dependence on $-\Delta H_S / (2k_B T)$, which turns a factor of $2.9$ in $\Delta H_S$ into ten orders of magnitude in $n_S$.
- d) Contradicts the official data table showing $\text{NaCl}$ forming abundant Schottky vacancy pairs at $1000\text{ K}$.

### Source

Session 4, Slide 18.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
