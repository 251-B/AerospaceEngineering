---
materia: "Aerospace Materials I"
tema: "Topic 6: Electrical Properties"
origen: "Problems T6andT7_Electric and Magnetic Properties.pdf, Problem 4"
dificultad: medium
badge: "Metal vs intrinsic semiconductor · temperature"
tags:
  - official-problem
  - solved
  - intrinsic-semiconductor
  - temperature-dependence
  - mobility
---

# ✏️ Problem: T6-04 — Effect of Temperature on a Metal and on an Intrinsic Semiconductor

## 📄 Official Statement
> 4. Justify the different effects that an increase on the exposure temperature have on a metal and on an intrinsic semiconductor

The sheet prints no solution for this problem.

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Conductivity is carriers times mobility.** For any conductor $\sigma=n|q|\mu$; for an intrinsic semiconductor both electrons and holes count, $\sigma=n|q|(\mu_e+\mu_h)$ [Session 13 Slides 12, 27-28].
2. **Metal.** The conduction electrons are the non-bonded electrons of the atoms, so their number does not depend on temperature in the range considered; only the mobility changes, through the thermal resistivity $\rho_T=\rho_0(1+\alpha_TT)$ [Session 13 Slides 13-14].
3. **Intrinsic semiconductor.** The carriers are created by thermal excitation across the gap, so $n=p=n_i$ grows with the temperature as $n_i\propto\exp(-E_g/2kT)$ and the exponential factor is the one that dominates the conductivity [Session 13 Slide 29]. The temperature also disorders the lattice, but that effect "is masked by the increase of the number of charge carriers" (Slide 29).
4. **Numerical illustration.** Copper with $\alpha_T=0.0039$ °C⁻¹ [Session 13 Slide 14] and germanium with $E_g=0.67$ eV [Session 13 Slide 8], both from 25 °C to 75 °C, the interval of [[Problem - T6-07 Conductivity of Intrinsic Germanium at 75 C|Problem T6-07]]. $k_B=8.62\times10^{-5}$ eV/K.

### Data
| Quantity | Symbol | Value |
| :--- | :--- | ---: |
| Temperature coefficient of Cu | $\alpha_T$ | 0.0039 °C⁻¹ |
| Band gap of Ge | $E_g$ | 0.67 eV |
| Boltzmann constant | $k_B$ | $8.62\times10^{-5}$ eV/K |
| Temperatures | $T_1,\ T_2$ | 25 °C, 75 °C (298.15 K, 348.15 K) |

**Unknown:** the sign and the size of the change of $\sigma$ in each material.

---

## 🧠 2. Model and Strategy

Take the logarithmic derivative of $\sigma=n\mu$ with respect to the temperature: it splits the change of the conductivity into the change of the carrier number and the change of the mobility. In the metal only the second term exists; in the intrinsic semiconductor the first term is far larger than the second.

![[attachments/T6/t6-p4-sigma-temperature.svg]]

**Strategy.**
1. Write the logarithmic derivative of the conductivity.
2. Evaluate it for the metal, using Slide 14, and for the semiconductor, using Slide 29.
3. Compare the numerical changes between 25 and 75 °C.

---

## 🔢 3. Step-by-Step Derivation

### 1. The two ways in which temperature can act
Conductivity as number of carriers times mobility, and its logarithmic derivative (product rule of the logarithm and chain rule):

$$\sigma=n\,|q|\,\mu\ \Rightarrow\ \ln\sigma=\ln n+\ln|q|+\ln\mu$$

$$\frac{1}{\sigma}\frac{d\sigma}{dT}=\frac{1}{n}\frac{dn}{dT}+\frac{1}{\mu}\frac{d\mu}{dT}$$

### 2. Metal [Session 13 Slides 13-14]
The number of free electrons is constant, so the first term vanishes, and the conductivity is the inverse of the thermal resistivity:

$$\frac{dn}{dT}=0\qquad\sigma=\frac{1}{\rho_0(1+\alpha_TT)}$$

Derivative of the inverse (chain rule with $u=1+\alpha_TT$, $du/dT=\alpha_T$):

$$\frac{1}{\sigma}\frac{d\sigma}{dT}=-\frac{1}{u}\frac{du}{dT}=-\frac{\alpha_T}{1+\alpha_TT}$$

Evaluated for copper at 25 °C:

$$1+\alpha_TT=1+0.0039\ {}^{\circ}\text{C}^{-1}\times25\ {}^{\circ}\text{C}=1.0975$$

$$\frac{1}{\sigma}\frac{d\sigma}{dT}=-\frac{0.0039\ {}^{\circ}\text{C}^{-1}}{1.0975}=\mathbf{-3.554\times10^{-3}\ K^{-1}}$$

so the relative change of the conductivity per kelvin, written as a percentage, is:

$$-3.554\times10^{-3}\ \text{K}^{-1}\times100\ \%=-0.3554\ \%\ \text{K}^{-1}$$

Over the 50 K of the interval:

$$\frac{\rho(75\ {}^{\circ}\text{C})}{\rho(25\ {}^{\circ}\text{C})}=\frac{1+0.0039\times75}{1+0.0039\times25}=\frac{1.2925}{1.0975}=1.1777$$

$$\frac{\sigma(75\ {}^{\circ}\text{C})}{\sigma(25\ {}^{\circ}\text{C})}=\frac{1}{1.1777}=\mathbf{0.8491}$$

### 3. Intrinsic semiconductor [Session 13 Slide 29]
The conductivity follows the carrier number:

$$\sigma=\sigma_0\exp\!\left(-\frac{E_g}{2k_BT}\right)\ \Rightarrow\ \ln\sigma=\ln\sigma_0-\frac{E_g}{2k_B}\,T^{-1}$$

Derivative with respect to $T$ (power rule on $T^{-1}$):

$$\frac{1}{\sigma}\frac{d\sigma}{dT}=-\frac{E_g}{2k_B}\left(-T^{-2}\right)=\frac{E_g}{2k_B\,T^2}$$

Evaluated for germanium at 298.15 K, first the constant $E_g/2k_B$ and the square of the temperature:

$$\frac{E_g}{2k_B}=\frac{0.67\ \text{eV}}{2\times8.62\times10^{-5}\ \text{eV/K}}=3886.3\ \text{K}$$

$$T^2=(298.15\ \text{K})^2=8.8893\times10^{4}\ \text{K}^2$$

$$\frac{1}{\sigma}\frac{d\sigma}{dT}=\frac{3886.3\ \text{K}}{8.8893\times10^{4}\ \text{K}^2}=\mathbf{+4.372\times10^{-2}\ K^{-1}}$$

so the relative change of the conductivity per kelvin, written as a percentage, is:

$$4.372\times10^{-2}\ \text{K}^{-1}\times100\ \%=+4.372\ \%\ \text{K}^{-1}$$

Over the 50 K of the interval (the ratio of Problem T6-07):

$$\frac{\sigma(75\ {}^{\circ}\text{C})}{\sigma(25\ {}^{\circ}\text{C})}=\exp\!\left[3886.3\ \text{K}\left(\frac{1}{298.15\ \text{K}}-\frac{1}{348.15\ \text{K}}\right)\right]=\exp(1.8720)=\mathbf{6.501}$$

### 4. Comparison of the two
Ratio of the relative rates at 25 °C, in absolute value:

$$\frac{4.372\times10^{-2}\ \text{K}^{-1}}{3.554\times10^{-3}\ \text{K}^{-1}}=12.30$$

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units of both logarithmic rates.**

$$\left[\frac{\alpha_T}{1+\alpha_TT}\right]=\frac{ {}^{\circ}\text{C}^{-1}}{1}=\text{K}^{-1}\qquad\left[\frac{E_g}{2k_BT^2}\right]=\frac{\text{eV}}{\text{eV}\,\text{K}^{-1}\,\text{K}^2}=\text{K}^{-1}$$

- **Interval.** A temperature difference of 1 °C equals 1 K, so the coefficient in °C⁻¹ can be read in K⁻¹.
- **Signs.** Metal: negative rate; semiconductor: positive rate.

### Interpretation
In the metal the carriers are already all there; heat only agitates the ions, the electrons collide more often, the mobility falls and so does $\sigma$. In the intrinsic semiconductor the heat itself creates carriers by lifting electrons across the gap, and the exponential growth of their number (4.4 % per kelvin) overpowers the loss of mobility, which is the same kind of effect as in the metal (a loss of 0.36 % per kelvin for copper). Over 50 K the metal loses 15 % of its conductivity and the semiconductor multiplies it by 6.5. For $E_g\to0$ the semiconductor rate tends to zero, as in a metal where the carrier number is temperature independent; for a large gap the rate becomes very large, and the material is an insulator at ordinary temperatures.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| Effect on the metal | not printed on the sheet | $\sigma$ decreases (0.8491 for Cu, 25 to 75 °C) | consistent with Session 13 Slides 13-14 |
| Effect on the intrinsic semiconductor | not printed on the sheet | $\sigma$ increases (6.501 for Ge, 25 to 75 °C) | consistent with Session 13 Slide 29; the 6.501 is the ratio of Problem T6-07 |

## 🔗 Related Links
* [[Topic 6 - Electrical Properties]]
* [[Concept - Metallic Bonding and Energy Band Theory]]
* [[Problem - T6-07 Conductivity of Intrinsic Germanium at 75 C|Problem T6-07]]
