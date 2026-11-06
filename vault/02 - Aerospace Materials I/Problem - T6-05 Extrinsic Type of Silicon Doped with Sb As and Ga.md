---
materia: "Aerospace Materials I"
tema: "Topic 6: Electrical Properties"
origen: "Problems T6andT7_Electric and Magnetic Properties.pdf, Problem 5"
dificultad: easy
badge: "Extrinsic type · donors and acceptors"
tags:
  - official-problem
  - solved
  - extrinsic-semiconductor
  - donor
  - acceptor
---

# ✏️ Problem: T6-05 — Extrinsic Type of Silicon Doped with Sb, As and Ga

## 📄 Official Statement
> 5. Indicate which of the following semiconductors are extrinsic n-type and extrinsic p-type and whether the introduced impurities act as donors or acceptors
>
> - a) Silicon doped with antimony in substitutional solid solution
> - b) Silicon doped with arsenic in substitutional solid solution
> - c) Silicon doped with gallium in substitutional solid solution
>
> *(Solution: a) n-type extrinsic; b) n-type extrinsic; c) p-type extrinsic)*

Slide 39 poses the same question with germanium doped with arsenic in item b; the classification is the same (step 5).

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Substitutional doping.** The dopant atom takes the place of a silicon atom in the diamond lattice, where each atom shares its 4 valence electrons in covalent bonds [Session 13 Slides 26, 31].
2. **Donor and acceptor rule.** An impurity with more valence electrons than the host (group 15) donates the extra electron to the conduction band and is a donor, giving n-type material; an impurity with fewer valence electrons (group 13) leaves a hole and is an acceptor, giving p-type material [Session 13 Slides 35-37].
3. **Group numbers.** Sb and As are in group 15 (VA), Ga is in group 13 (IIIA), Si and Ge are in group 14 (IVA) [Session 13 Slides 35-37]. (Slide 37 prints "group VA" next to B, Al, Ga, but the table on the same slide places them in group 3A.)
4. **Room temperature,** taken as 300 K here (the problems whose statement gives 25 °C use 298.15 K), with $k_B=8.62\times10^{-5}$ eV/K, and the ionisation energies of Slide 40.

### Data
| Dopant | Group | Valence electrons | Host | Level of Slide 40 |
| :--- | :---: | :---: | :---: | :--- |
| Sb | 15 | 5 | Si | $E_d=0.039$ eV |
| As | 15 | 5 | Si | $E_d=0.049$ eV |
| Ga | 13 | 3 | Si | $E_a=0.065$ eV |
| As | 15 | 5 | Ge | $E_d=0.0127$ eV |

**Unknown:** type of each semiconductor (n or p) and role of each impurity (donor or acceptor).

---

## 🧠 2. Model and Strategy

Compare the number of valence electrons of the dopant with the 4 of the host: the difference is the electron surplus (donor) or the hole surplus (acceptor). The figure marks the three dopants of the sheet in the periodic table.

![[attachments/T6/t6-p5-doping-groups.svg]]

**Strategy.**
1. Count the valence electrons of each dopant and subtract the 4 of the host.
2. Assign donor or acceptor from the sign of the difference, and n or p from the carrier that is in excess.
3. Check with the ionisation energies of Slide 40 that the level lies close enough to its band to be ionised at room temperature.

---

## 🔢 3. Step-by-Step Derivation

### 1. Valence-electron surplus of each substitution [Session 13 Slides 36-37]
Surplus of electrons with respect to the 4 valence electrons that the silicon atom replaced:

$$\Delta Z_{\text{Sb}}=Z_{\text{Sb}}-Z_{\text{Si}}=5-4=+1$$

$$\Delta Z_{\text{As}}=Z_{\text{As}}-Z_{\text{Si}}=5-4=+1$$

$$\Delta Z_{\text{Ga}}=Z_{\text{Ga}}-Z_{\text{Si}}=3-4=-1$$

### 2. Roles and types
Four of the five valence electrons of Sb or As fill the four covalent bonds; the fifth one is loosely bound and jumps to the conduction band from the donor level $E_d$ [Session 13 Slide 36]:

$$\Delta Z=+1\ \Rightarrow\ \text{donor}\ \Rightarrow\ n_e\gg n_H\ \Rightarrow\ \sigma\approx n_e\,|q_e|\,\mu_e\quad(\text{n-type})$$

Ga has three valence electrons for four bonds; one bond is incomplete and a neighbouring valence electron can fill it from just above the valence band, leaving a hole [Session 13 Slide 37]:

$$\Delta Z=-1\ \Rightarrow\ \text{acceptor}\ \Rightarrow\ p\gg n\ \Rightarrow\ \sigma\approx p\,|q_e|\,\mu_h\quad(\text{p-type})$$

### 3. Ionisation energies against the thermal energy at 300 K
Thermal energy:

$$k_BT=8.62\times10^{-5}\ \frac{\text{eV}}{\text{K}}\times300\ \text{K}=0.02586\ \text{eV}$$

Ratio of each level of Slide 40 to it, with the conversion of the energy to joules ($1\ \text{eV}=1.602\times10^{-19}$ J):

$$E_d(\text{Sb in Si})=0.039\ \text{eV}\times1.602\times10^{-19}\ \frac{\text{J}}{\text{eV}}=6.248\times10^{-21}\ \text{J}\qquad\frac{0.039}{0.02586}=1.51$$

$$E_d(\text{As in Si})=0.049\ \text{eV}\times1.602\times10^{-19}\ \frac{\text{J}}{\text{eV}}=7.850\times10^{-21}\ \text{J}\qquad\frac{0.049}{0.02586}=1.89$$

$$E_a(\text{Ga in Si})=0.065\ \text{eV}\times1.602\times10^{-19}\ \frac{\text{J}}{\text{eV}}=1.041\times10^{-20}\ \text{J}\qquad\frac{0.065}{0.02586}=2.51$$

### 4. Result of the sheet
$$\text{a) Si + Sb}:\ \mathbf{n\text{-}type,\ Sb\ donor}\qquad\text{b) Si + As}:\ \mathbf{n\text{-}type,\ As\ donor}\qquad\text{c) Si + Ga}:\ \mathbf{p\text{-}type,\ Ga\ acceptor}$$

### 5. The version of Slide 39 (germanium doped with arsenic)
Arsenic keeps its 5 valence electrons and the host keeps 4:

$$\Delta Z_{\text{As in Ge}}=5-4=+1\ \Rightarrow\ \text{donor, n-type}\qquad\frac{E_d}{k_BT}=\frac{0.0127\ \text{eV}}{0.02586\ \text{eV}}=0.49$$

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Dimensions.** All energy ratios are eV over eV, dimensionless; all three levels are of the order of $k_BT$ or a few times it, so a large fraction of the impurities is ionised at room temperature.
- **Charge neutrality.** The ionised donor is a fixed positive ion (it lost an electron) and the ionised acceptor a fixed negative ion; the crystal stays neutral.
- **Limit.** For $\Delta Z=0$ (an isoelectronic atom such as Ge in Si) no carriers are added and the material stays intrinsic.

### Interpretation
Sb and As add electrons: in silicon they are donors and the majority carriers are electrons. Ga removes one: it is an acceptor and the majority carriers are holes. In all three cases the dopant is a substitutional atom and contributes one carrier per atom, which is why a small concentration (hundreds of ppm) changes the conductivity by orders of magnitude [Session 13 Slide 26].

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a) Si + Sb | n-type extrinsic | n-type, Sb is a donor | agrees |
| b) Si + As | n-type extrinsic | n-type, As is a donor | agrees |
| c) Si + Ga | p-type extrinsic | p-type, Ga is an acceptor | agrees |

## 🔗 Related Links
* [[Topic 6 - Electrical Properties]]
* [[Concept - Covalent Bonding and Polar Character]]
* [[Concept - Substitutional and Interstitial Solid Solutions, Hume-Rothery Rules]]
