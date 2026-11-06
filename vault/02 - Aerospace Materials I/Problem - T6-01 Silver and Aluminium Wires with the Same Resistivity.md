---
materia: "Aerospace Materials I"
tema: "Topic 6: Electrical Properties"
origen: "Problems T6andT7_Electric and Magnetic Properties.pdf, Problem 1"
dificultad: easy
badge: "Resistivity · temperature coefficient"
tags:
  - official-problem
  - solved
  - resistivity
  - temperature-coefficient
  - matthiessen
---

# ✏️ Problem: T6-01 — Silver and Aluminium Wires with the Same Resistivity

## 📄 Official Statement
> 1. At what temperature will a silver wire exhibit the same resistivity as an aluminium wire at 45 ºC. The resistivities of silver and aluminium at 0 ºC are $1.47\cdot10^{-6}$ and $2.70\cdot10^{-6}$ Ω·cm respectively and their resistivity coefficients, 0.0038 and 0.0039 ºC⁻¹, respectively.
>
> *(Solution: 305 °C)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Matthiessen's rule.** The resistivity of a metal is the sum of a thermal part and a residual part, [Session 13 Slide 14]. The residual part (impurities and defects) is already contained in the resistivity measured at 0 °C, so each wire is described by one number $\rho_0$ and one coefficient $\alpha_T$.
2. **Linear thermal resistivity.** The thermal part grows linearly with the temperature measured from 0 °C, with the temperature coefficient of resistivity $\alpha_T$ [Session 13 Slide 14]. The sheet gives one constant $\alpha_T$ per metal, so it is used over the whole range up to the result (an extrapolation that the sheet asks for; real silver departs slowly from a straight line).
3. **Same wire geometry is irrelevant.** Resistivity is a property of the material, not of the length or section, so the wires need no dimensions.

### Data
| Quantity | Symbol | Value as printed | In SI |
| :--- | :--- | ---: | ---: |
| Resistivity of Ag at 0 °C | $\rho_{0,\text{Ag}}$ | $1.47\times10^{-6}$ Ω·cm | $1.47\times10^{-8}$ Ω·m |
| Resistivity of Al at 0 °C | $\rho_{0,\text{Al}}$ | $2.70\times10^{-6}$ Ω·cm | $2.70\times10^{-8}$ Ω·m |
| Coefficient of Ag | $\alpha_{\text{Ag}}$ | 0.0038 °C⁻¹ | 0.0038 K⁻¹ |
| Coefficient of Al | $\alpha_{\text{Al}}$ | 0.0039 °C⁻¹ | 0.0039 K⁻¹ |
| Temperature of the Al wire | $T_{\text{Al}}$ | 45 °C | 45 °C (a difference from 0 °C: 45 K) |

**Unknown:** the temperature $T_{\text{Ag}}$ at which silver has the resistivity of the aluminium wire at 45 °C.

The sheet prints the resistivities in Ω·cm and without the Ω and the dot in the first value; they are read from Slide 15, where the same problem is solved ($\rho_0$ in $\mu\Omega\cdot$cm on Slide 14: Al 2.7, Ag 1.47).

---

## 🧠 2. Model and Strategy

Aluminium is more resistive than silver at 0 °C, so silver has to be heated until the growth of its thermal resistivity makes up the difference. The figure shows the two straight lines and the horizontal level that fixes the answer.

![[attachments/T6/t6-p1-resistivity-lines.svg]]

**Strategy.**
1. Convert the resistivities to SI.
2. Evaluate the resistivity of aluminium at 45 °C with the law of Slide 14.
3. Impose the same resistivity on silver and solve the linear equation for its temperature.
4. Check by substituting back, and compare with the solution that Slide 15 prints.

---

## 🔢 3. Step-by-Step Derivation

### 1. Law of the thermal resistivity [Session 13 Slide 14]
The resistivity at temperature $T$ (in °C, from 0 °C) of each wire is:

$$\rho_T=\rho_0\,\bigl(1+\alpha_T\,T\bigr)$$

### 2. Unit conversion to SI
One ohm-centimetre is one ohm times one hundredth of a metre:

$$1\ \Omega\,\text{cm}=1\ \Omega\times10^{-2}\ \text{m}=10^{-2}\ \Omega\,\text{m}$$

Applied to each resistivity at 0 °C:

$$\rho_{0,\text{Al}}=2.70\times10^{-6}\ \Omega\,\text{cm}\times10^{-2}\ \frac{\Omega\,\text{m}}{\Omega\,\text{cm}}=2.70\times10^{-8}\ \Omega\,\text{m}$$

$$\rho_{0,\text{Ag}}=1.47\times10^{-6}\ \Omega\,\text{cm}\times10^{-2}\ \frac{\Omega\,\text{m}}{\Omega\,\text{cm}}=1.47\times10^{-8}\ \Omega\,\text{m}$$

### 3. Resistivity of the aluminium wire at 45 °C
The product $\alpha T$ is dimensionless:

$$\alpha_{\text{Al}}\,T_{\text{Al}}=0.0039\ {}^{\circ}\text{C}^{-1}\times45\ {}^{\circ}\text{C}=0.1755$$

$$1+\alpha_{\text{Al}}T_{\text{Al}}=1+0.1755=1.1755$$

$$\rho_{\text{Al}}(45\ {}^{\circ}\text{C})=2.70\times10^{-8}\ \Omega\,\text{m}\times1.1755=\mathbf{3.17385\times10^{-8}\ \Omega\,m}$$

### 4. Condition of the statement: the same resistivity in silver
$$\rho_{0,\text{Ag}}\bigl(1+\alpha_{\text{Ag}}\,T_{\text{Ag}}\bigr)=\rho_{\text{Al}}(45\ {}^{\circ}\text{C})$$

Dividing both sides by $\rho_{0,\text{Ag}}$, subtracting 1 and dividing by $\alpha_{\text{Ag}}$:

$$\begin{aligned}1+\alpha_{\text{Ag}}T_{\text{Ag}}&=\frac{\rho_{\text{Al}}(45\ {}^{\circ}\text{C})}{\rho_{0,\text{Ag}}}\\ \alpha_{\text{Ag}}T_{\text{Ag}}&=\frac{\rho_{\text{Al}}(45\ {}^{\circ}\text{C})}{\rho_{0,\text{Ag}}}-1=\frac{\rho_{\text{Al}}(45\ {}^{\circ}\text{C})-\rho_{0,\text{Ag}}}{\rho_{0,\text{Ag}}}\\ T_{\text{Ag}}&=\frac{\rho_{\text{Al}}(45\ {}^{\circ}\text{C})-\rho_{0,\text{Ag}}}{\rho_{0,\text{Ag}}\,\alpha_{\text{Ag}}}\end{aligned}$$

### 5. Numerical evaluation, one operation per block
Numerator, in ohm-metres:

$$\rho_{\text{Al}}(45\ {}^{\circ}\text{C})-\rho_{0,\text{Ag}}=3.17385\times10^{-8}\ \Omega\,\text{m}-1.47\times10^{-8}\ \Omega\,\text{m}=1.70385\times10^{-8}\ \Omega\,\text{m}$$

Denominator, in ohm-metres per degree:

$$\rho_{0,\text{Ag}}\,\alpha_{\text{Ag}}=1.47\times10^{-8}\ \Omega\,\text{m}\times0.0038\ {}^{\circ}\text{C}^{-1}=5.586\times10^{-11}\ \frac{\Omega\,\text{m}}{{}^{\circ}\text{C}}$$

Quotient:

$$T_{\text{Ag}}=\frac{1.70385\times10^{-8}\ \Omega\,\text{m}}{5.586\times10^{-11}\ \Omega\,\text{m}\ {}^{\circ}\text{C}^{-1}}=\mathbf{305.0\ {}^{\circ}C}$$

### 6. Substitution back into the law
$$\alpha_{\text{Ag}}T_{\text{Ag}}=0.0038\ {}^{\circ}\text{C}^{-1}\times305.02\ {}^{\circ}\text{C}=1.15908$$

$$\rho_{\text{Ag}}(305.02\ {}^{\circ}\text{C})=1.47\times10^{-8}\ \Omega\,\text{m}\times(1+1.15908)=1.47\times10^{-8}\ \Omega\,\text{m}\times2.15908=3.17385\times10^{-8}\ \Omega\,\text{m}$$

### 7. The solution printed on Slide 15
Slide 15 rounds the aluminium resistivity to $3.173\times10^{-6}$ Ω·cm before dividing:

$$T_{\text{Ag}}=\frac{3.173\times10^{-6}-1.47\times10^{-6}}{1.47\times10^{-6}\times0.0038}\ {}^{\circ}\text{C}=\frac{1.703\times10^{-6}}{5.586\times10^{-9}}\ {}^{\circ}\text{C}=304.87\ {}^{\circ}\text{C}$$

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units of the coefficient term.**

$$[\alpha_T\,T]={}^{\circ}\text{C}^{-1}\cdot{}^{\circ}\text{C}=1$$

- **Units of the result.**

$$[T_{\text{Ag}}]=\frac{\Omega\,\text{m}}{\Omega\,\text{m}\cdot{}^{\circ}\text{C}^{-1}}={}^{\circ}\text{C}$$

- **Substitution.** Silver at 305.02 °C has $3.17385\times10^{-8}$ Ω·m, equal to aluminium at 45 °C (step 6).
- **Rounding.** The 304.87 of Slide 15 differs from our 305.02 only because the slide rounds $\rho_{\text{Al}}$ to four figures; our value keeps the exact product.

### Interpretation
Silver conducts better than aluminium at the same temperature, so the temperature that equalises them is far above 45 °C: silver must be heated until its thermal resistivity has grown from its low value at 0 °C up to the aluminium value (step 5). The result is large because the thermal slope of silver, $\rho_{0,\text{Ag}}\alpha_{T,\text{Ag}}$, is small; as that slope tends to zero the temperature tends to infinity. The linear law is used up to 305 °C because the sheet fixes it; real metals bend away from a straight line at high temperature.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| Temperature of the silver wire | 305 °C | 305.0 °C | agrees; Slide 15 prints 304.86 because it rounds $\rho_{\text{Al}}$ to 3.173 (we get 304.87 with that rounding) |

## 🔗 Related Links
* [[Topic 6 - Electrical Properties]]
* [[Concept - Metallic Bonding and Energy Band Theory]]
