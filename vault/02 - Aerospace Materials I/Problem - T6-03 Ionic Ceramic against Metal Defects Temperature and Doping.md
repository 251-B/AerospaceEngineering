---
materia: "Aerospace Materials I"
tema: "Topic 6: Electrical Properties"
origen: "Problems T6andT7_Electric and Magnetic Properties.pdf, Problem 3"
dificultad: medium
badge: "Ionic and metallic conduction · defects"
tags:
  - official-problem
  - solved
  - ionic-conduction
  - point-defects
  - metallic-conduction
---

# ✏️ Problem: T6-03 — Ionic Ceramic against Metal: Defects, Temperature and Doping

## 📄 Official Statement
> 3. Compare the effect of following factors on the conductivity of an ionic conductor and a metallic conductor
>
> | Factor | Ionic ceramic | Metal |
> | :--- | :--- | :--- |
> | Vacant positions in the net | | |
> | Cations in interstitial positions | | |
> | Anions in interstitial positions | | |
> | Increase of temperature | | |
> | Disorder of the net | | |
> | Doping with substances with other valences | | |

The sheet prints no solution for this problem.

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Metal.** The conduction electrons are free and their number is fixed by the atoms; the conductivity is $\sigma=n|q_e|\mu$, and anything that scatters electrons lowers the mobility $\mu$ [Session 13 Slides 12-13]. Resistivity is the sum of the thermal, impurity and deformation terms [Session 13 Slides 14, 16].
2. **Ionic ceramic.** The charge is carried by ions: cations or anions that move through vacancies or interstitial voids, at high temperature [Session 13 Slide 22]. The number of mobile ions and their ease of movement decide the conductivity, so the same structure formula $\sigma=\sum n_k|q_k|\mu_k$ holds with ions in place of electrons (an extension of the form of Slide 12, which the slide writes for electrons only).
3. **Cations are the small ions.** The slide draws the interstitial movement for cations of radius smaller than the atom ($r_i<r_{atom}$) [Session 13 Slide 22]; the anions of an ionic crystal are the larger ions and fit interstitial voids poorly (Topic 2).
4. **The ionic column is argued** from Slide 22 and from the defect chemistry of Topic 2; the metal column from Slides 13, 14 and 16. The sheet prints no key, so no verdict below is copied from a solution.

### Data
Six factors, two kinds of conductor; the unknown is the sign of the effect on the conductivity ($\uparrow$ increases, $\downarrow$ decreases, $\approx$ almost no effect).

---

## 🧠 2. Model and Strategy

The two columns follow opposite logic: in the metal a defect is an obstacle for the electron, in the ionic ceramic a defect is a place where an ion can jump. The figure shows both pictures.

![[attachments/T6/t6-p3-ionic-metal.svg]]

**Strategy.**
1. Write the conductivity of each conductor type as number of carriers times charge times mobility.
2. For each factor decide whether it changes the number of mobile carriers or their mobility.
3. Collect the verdicts in a table.

---

## 🔢 3. Step-by-Step Derivation

### 1. Metallic conductor [Session 13 Slides 12-14, 16]
Conductivity from the number of free electrons and their mobility, and the mobility from the relaxation time between collisions:

$$\sigma=n\,|q_e|\,\mu\qquad\mu=\frac{\tau\,|q_e|}{m_e}$$

Every factor that increases the number of collisions shortens $\tau$, lowers $\mu$ and so lowers $\sigma$; Matthiessen's rule collects the sources:

$$\rho_{\text{total}}=\rho_T+\rho_i+\rho_d\qquad\sigma=\frac{1}{\rho_{\text{total}}}$$

The thermal term grows with temperature:

$$\rho_T=\rho_0\,(1+\alpha_T\,T)$$

### 2. Ionic conductor [Session 13 Slide 22]
Conductivity as the sum over the mobile ionic species, with the number of mobile ions $n_k$ and their mobility $\mu_k$ (extension of the form of Slide 12):

$$\sigma_{\text{ionic}}=\sum_k n_k\,|q_k|\,\mu_k$$

The ions move by jumps between lattice sites, so their mobility follows the diffusivity of the ion, which is thermally activated (Topic 3, Arrhenius):

$$D=D_0\exp\!\left(-\frac{Q}{R\,T}\right)$$

and the Nernst-Einstein relation links mobility and diffusivity (extension, not in Session 13):

$$\mu_k=\frac{|q_k|\,D_k}{k_B\,T}$$

Jumps need empty sites. The equilibrium fraction of vacancies grows with temperature (Topic 2, thermal vacancies):

$$\frac{n_v}{N}=\exp\!\left(-\frac{Q_v}{k_B\,T}\right)$$

### 3. Vacant positions and interstitial atoms
In the metal a vacancy or an interstitial atom distorts the lattice and belongs to the deformation or impurity term:

$$n_v\uparrow\ \Rightarrow\ \rho_d\uparrow\ \Rightarrow\ \sigma\downarrow$$

In the ionic crystal a vacancy offers the neighbouring cations an empty site to jump into, and an interstitial cation can move through the interstitial voids [Session 13 Slide 22]:

$$n_v\uparrow\ \Rightarrow\ \text{jumps}\uparrow\ \Rightarrow\ \mu_k\uparrow\ \Rightarrow\ \sigma_{\text{ionic}}\uparrow$$

An interstitial anion is the exception: the anion is the larger ion and fits an interstitial void only with a large distortion, so few anions are interstitial and they hardly move; the slide draws the interstitial jump for the small cation. The verdict is "almost no effect" (this is a size argument of Topic 2, not a statement of the slide):

$$r_{\text{anion}}>r_{\text{cation}}\ \Rightarrow\ \text{few mobile interstitial anions}\ \Rightarrow\ \Delta\sigma_{\text{ionic}}\approx0$$

### 4. Temperature
Metal: the thermal resistivity grows linearly and the conductivity falls:

$$T\uparrow\ \Rightarrow\ \rho_T=\rho_0(1+\alpha_T T)\uparrow\ \Rightarrow\ \sigma\downarrow$$

Ionic ceramic: both the number of vacancies and the diffusivity grow exponentially with $T$, so the conductivity rises strongly (conduction occurs "at high temperatures" [Session 13 Slide 22]):

$$T\uparrow\ \Rightarrow\ \exp\!\left(-\frac{Q_v}{k_BT}\right)\uparrow\ \text{and}\ \exp\!\left(-\frac{Q}{RT}\right)\uparrow\ \Rightarrow\ \sigma_{\text{ionic}}\uparrow\uparrow$$

### 5. Disorder of the net
Metal: disorder is the distortion of the metal net; the residual resistivity increases with "the degree of distortion" [Session 13 Slide 16]:

$$\text{disorder}\uparrow\ \Rightarrow\ \rho_r\uparrow\ \Rightarrow\ \sigma\downarrow$$

Ionic ceramic: disorder (point defects, open structure) means more empty sites and more paths for the jumps:

$$\text{disorder}\uparrow\ \Rightarrow\ \text{empty sites and paths}\uparrow\ \Rightarrow\ \sigma_{\text{ionic}}\uparrow$$

### 6. Doping with substances of another valence
Metal: a solute is an impurity, whatever its valence [Session 13 Slide 16]:

$$\text{solute}\ \Rightarrow\ \rho_i\uparrow\ \Rightarrow\ \sigma\downarrow$$

Ionic ceramic: an ion of another valence must be compensated to keep the crystal neutral. Two $\text{Al}^{3+}$ replacing two $\text{Mg}^{2+}$ in MgO bring an excess charge that a cation vacancy removes (the case of [[Problem - T2-DEF03 Cationic Vacancies in MgO from Dissolving Al2O3 and TiO2|Problem T2-DEF03]]):

$$2\times(+3)-2\times(+2)=+2\ \Rightarrow\ \text{one cation vacancy of charge}\ -2$$

so doping creates vacancies and the conductivity rises:

$$\text{aliovalent doping}\ \Rightarrow\ n_v\uparrow\ \Rightarrow\ \sigma_{\text{ionic}}\uparrow$$

### 7. Result table
| Factor | Ionic ceramic | Metal |
| :--- | :---: | :---: |
| Vacant positions in the net | $\uparrow$ | $\downarrow$ |
| Cations in interstitial positions | $\uparrow$ | $\downarrow$ |
| Anions in interstitial positions | $\approx$ | $\downarrow$ |
| Increase of temperature | $\uparrow\uparrow$ | $\downarrow$ |
| Disorder of the net | $\uparrow$ | $\downarrow$ |
| Doping with substances with other valences | $\uparrow$ | $\downarrow$ |

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units of the ionic expression.**

$$[\sigma_{\text{ionic}}]=\text{m}^{-3}\cdot\text{C}\cdot\frac{\text{m}^2}{\text{V}\,\text{s}}=\frac{\text{A}}{\text{V}\,\text{m}}=\Omega^{-1}\text{m}^{-1}$$

- **Opposite logic.** Every entry of the metal column is a decrease; five of six entries of the ionic column are an increase. In the metal the carriers (electrons) are not created by the defects, so a defect can only hinder them; in the ionic crystal the defects are both the carriers' route and their number.
- **Limits.** At a very low temperature the vacancies freeze out and an ionic ceramic is an insulator, while a metal has its lowest resistivity (only $\rho_r$ left); at a very high temperature the ceramic is a good ionic conductor and the metal is at its most resistive.

### Interpretation
The same defect has opposite meaning in the two conductors: it is an obstacle for an electron wave in the metal and a stepping stone for an ion in the ceramic. This is why metals are cooled to improve conduction and ceramic electrolytes (fuel cells, gas sensors, Slide 22) are heated to work.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| All six factors | not printed on the sheet | table of step 7 | argued from Session 13 Slides 13, 14, 16, 22 and Topics 2-3; the interstitial anion entry and the Nernst-Einstein relation are the note's own reasoning, not slide content |

## 🔗 Related Links
* [[Topic 6 - Electrical Properties]]
* [[Concept - Metallic Bonding and Energy Band Theory]]
* [[Problem - T2-DEF03 Cationic Vacancies in MgO from Dissolving Al2O3 and TiO2|Problem T2-DEF03]]
* [[Concept - Point Defects, Thermal Vacancies, Schottky and Frenkel]]
* [[Concept - The Arrhenius Equation and Factors Influencing Diffusivity]]
