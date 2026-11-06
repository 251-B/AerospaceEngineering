---
materia: "Aerospace Materials I"
tema: "Topic 6: Electrical Properties"
origen: "Problems T6andT7_Electric and Magnetic Properties.pdf, Problem 7"
dificultad: medium
badge: "Intrinsic semiconductor · Arrhenius"
tags:
  - official-problem
  - solved
  - intrinsic-semiconductor
  - band-gap
  - arrhenius
---

# ✏️ Problem: T6-07 — Conductivity of Intrinsic Germanium at 75 °C

## 📄 Official Statement
> 7. The electrical conductivity of intrinsic germanium at 25 ºC is 2.22 Ω⁻¹m⁻¹. What will its conductivity be at 75 ºC? The band gap of germanium is 0.67 eV and $k_B$ = $8.62\cdot10^{-5}$ eV/K
>
> *(Solution: 14.4 Ω⁻¹m⁻¹)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Intrinsic law.** In an intrinsic semiconductor the carrier number, and with it the conductivity, follows $\sigma=\sigma_0\exp(-E_g/2k_BT)$ with the absolute temperature [Session 13 Slide 29]. The constant $\sigma_0$ is the same at both temperatures.
2. **Slide approximation.** The slide writes the proportionality $n_i\propto\exp(-E_g/2kT)$ and neglects the slower dependence of the prefactor and of the mobilities on the temperature; the exponential, which varies by orders of magnitude, dominates the ratio.
3. **Constant gap.** $E_g=0.67$ eV is the same at 25 °C and 75 °C.
4. **Kelvin.** $T[\text{K}]=T[{}^{\circ}\text{C}]+273.15$.

### Data
| Quantity | Symbol | Value as printed | In SI |
| :--- | :--- | ---: | ---: |
| Conductivity at 25 °C | $\sigma_1$ | 2.22 Ω⁻¹m⁻¹ | 2.22 Ω⁻¹m⁻¹ |
| Temperatures | $T_1,\ T_2$ | 25 °C, 75 °C | 298.15 K, 348.15 K |
| Band gap | $E_g$ | 0.67 eV | $0.67\times1.602\times10^{-19}$ J |
| Boltzmann constant | $k_B$ | $8.62\times10^{-5}$ eV/K | $8.62\times10^{-5}\times1.602\times10^{-19}$ J/K |

**Unknown:** the conductivity $\sigma_2$ at 75 °C.

---

## 🧠 2. Model and Strategy

The unknown constant $\sigma_0$ is eliminated by taking the ratio of the law at the two temperatures; what remains is the exponential of $E_g/2k_B$ times the difference of the reciprocal temperatures. The straight line of $\ln\sigma$ against $1/T$ has the slope $-E_g/2k_B$, so the ratio is also the vertical distance between the two points of the figure.

![[attachments/T6/t6-p7-arrhenius-ge.svg]]

**Strategy.**
1. Write the law at $T_1$ and $T_2$ and divide.
2. Evaluate $E_g/2k_B$ in kelvin, the two reciprocals, their difference and the exponent.
3. Take the exponential and multiply by $\sigma_1$.

---

## 🔢 3. Step-by-Step Derivation

### 1. The law at both temperatures [Session 13 Slide 29]
$$\sigma_1=\sigma_0\exp\!\left(-\frac{E_g}{2k_BT_1}\right)\qquad\sigma_2=\sigma_0\exp\!\left(-\frac{E_g}{2k_BT_2}\right)$$

### 2. Elimination of $\sigma_0$
Division of the second by the first and the rule $e^{a}/e^{b}=e^{a-b}$:

$$\frac{\sigma_2}{\sigma_1}=\frac{\exp\!\left(-\frac{E_g}{2k_BT_2}\right)}{\exp\!\left(-\frac{E_g}{2k_BT_1}\right)}=\exp\!\left[-\frac{E_g}{2k_BT_2}+\frac{E_g}{2k_BT_1}\right]$$

Common factor $E_g/2k_B$:

$$\sigma_2=\sigma_1\exp\!\left[\frac{E_g}{2k_B}\left(\frac{1}{T_1}-\frac{1}{T_2}\right)\right]$$

### 3. Temperatures in kelvin
$$T_1=25+273.15=298.15\ \text{K}\qquad T_2=75+273.15=348.15\ \text{K}$$

### 4. The constant $E_g/2k_B$
Direct, with both quantities in eV (the eV cancels):

$$\frac{E_g}{2k_B}=\frac{0.67\ \text{eV}}{2\times8.62\times10^{-5}\ \text{eV/K}}=\frac{0.67}{1.724\times10^{-4}}\ \text{K}=3886.3\ \text{K}$$

The same result in joules, as a check of the unit conversion ($1\ \text{eV}=1.602\times10^{-19}$ J):

$$E_g=0.67\ \text{eV}\times1.602\times10^{-19}\ \frac{\text{J}}{\text{eV}}=1.0733\times10^{-19}\ \text{J}\qquad k_B=8.62\times10^{-5}\ \frac{\text{eV}}{\text{K}}\times1.602\times10^{-19}\ \frac{\text{J}}{\text{eV}}=1.3809\times10^{-23}\ \frac{\text{J}}{\text{K}}$$

$$\frac{E_g}{2k_B}=\frac{1.0733\times10^{-19}\ \text{J}}{2\times1.3809\times10^{-23}\ \text{J/K}}=3886.3\ \text{K}$$

### 5. Reciprocal temperatures and their difference
$$\frac{1}{T_1}=\frac{1}{298.15\ \text{K}}=3.35402\times10^{-3}\ \text{K}^{-1}\qquad\frac{1}{T_2}=\frac{1}{348.15\ \text{K}}=2.87233\times10^{-3}\ \text{K}^{-1}$$

$$\frac{1}{T_1}-\frac{1}{T_2}=3.35402\times10^{-3}\ \text{K}^{-1}-2.87233\times10^{-3}\ \text{K}^{-1}=4.8169\times10^{-4}\ \text{K}^{-1}$$

### 6. Exponent, exponential and result
$$\frac{E_g}{2k_B}\left(\frac{1}{T_1}-\frac{1}{T_2}\right)=3886.3\ \text{K}\times4.8169\times10^{-4}\ \text{K}^{-1}=1.8720$$

$$\frac{\sigma_2}{\sigma_1}=e^{1.8720}=6.501$$

$$\sigma_2=2.22\ \Omega^{-1}\text{m}^{-1}\times6.501=\mathbf{14.43\ \Omega^{-1}m^{-1}}$$

### 7. Using 273 instead of 273.15
$$\frac{1}{298}-\frac{1}{348}=4.8214\times10^{-4}\ \text{K}^{-1}\qquad\sigma_2=2.22\times\exp(3886.3\times4.8214\times10^{-4})=2.22\times e^{1.8737}=14.46\ \Omega^{-1}\text{m}^{-1}$$

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Dimensionless exponent.**

$$\left[\frac{E_g}{2k_B}\left(\frac{1}{T_1}-\frac{1}{T_2}\right)\right]=\text{K}\cdot\text{K}^{-1}=1$$

- **Slope.** On the plot of $\ln\sigma$ against $1/T$ the line has the slope $-3886.3$ K, and the vertical distance between the two points is $\ln(\sigma_2/\sigma_1)=1.8720$.

$$\ln\frac{\sigma_2}{\sigma_1}=\ln\frac{14.43}{2.22}=\ln6.501=1.8720$$

- **Consistency with the slide data.** Slide 31 gives $n_i=2.4\times10^{19}$ m⁻³, $\mu_e=0.39$ and $\mu_h=0.19$ m²/(V·s) for germanium at room temperature:

$$\sigma_1=n_i\,|q_e|\,(\mu_e+\mu_h)=2.4\times10^{19}\times1.602\times10^{-19}\times0.58\ \Omega^{-1}\text{m}^{-1}=2.23\ \Omega^{-1}\text{m}^{-1}$$

which agrees with the 2.22 of the statement.

### Interpretation
A rise of 50 K multiplies the conductivity of germanium by 6.5: in a semiconductor heat creates carriers. At the limit $T_2\to T_1$ the ratio tends to 1; at the limit $T_2\to\infty$ the ratio saturates at the value of the next block (within the model of constant prefactor):

$$\frac{E_g}{2k_BT_1}=\frac{3886.3\ \text{K}}{298.15\ \text{K}}=13.035\qquad e^{13.035}=4.58\times10^{5}$$

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| Conductivity at 75 °C | 14.4 Ω⁻¹m⁻¹ | 14.43 Ω⁻¹m⁻¹ | agrees with 273.15 K; with 273 K the result is 14.46, which rounds to 14.5, so the key uses 273.15 |

## 🔗 Related Links
* [[Topic 6 - Electrical Properties]]
* [[Concept - Interatomic Potential Energy Curves and Macroscopic Properties]]
* [[Problem - T6-04 Effect of Temperature on a Metal and on an Intrinsic Semiconductor]]
