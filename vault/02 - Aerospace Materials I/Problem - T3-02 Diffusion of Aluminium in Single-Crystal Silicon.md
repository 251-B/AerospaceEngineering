---
materia: "Aerospace Materials I"
tema: "Topic 3: Diffusion in Solids and Mass Transport"
origen: "Problems T3_Diffusion.pdf, Problem 2"
dificultad: medium
tags:
  - official-problem
  - solved
  - arrhenius
  - semiconductors
  - silicon-doping
  - activation-energy
---

# ✏️ Problem: T3-02 — Diffusion of Aluminium in Single-Crystal Silicon

## 📄 Official Statement
> **2.- Al can diffuse in a Si monocrystal. Calculate the temperature at which the diffusion coefficient will have a value of $10^{-14}\text{ m}^2/\text{s}$? Data: $E_D = 73\text{ kcal/mol}$; $D_0 = 1.55 \times 10^{-4}\text{ m}^2/\text{s}$ and $R = 1.987\text{ cal/mol}\cdot\text{K}$.**  
> *(Solution: $T = 1566\text{ K}$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Physical Hypotheses:
1. **Arrhenius behaviour:** The diffusivity of aluminium in silicon follows the Arrhenius law $D = D_0 e^{-E_D/RT}$ in the temperature range of interest [Session 5 Slide 26].
2. **Constancy of Kinetic Parameters:** Both the pre-exponential factor $D_0$ and the activation energy $E_D$ are considered independent of temperature in the thermodynamic interval of interest.
3. **Volume diffusion:** The silicon is a single crystal, so there are no grain boundaries; the diffusion takes place through the volume of the crystal, the slowest of the paths $D_{surface} > D_{grain\ boundary} > D_{volume}$ [Slide 25].

### Input Parameters:
* Desired diffusion coefficient: $D = 10^{-14}\text{ m}^2/\text{s} = 1.0 \times 10^{-14}\text{ m}^2/\text{s}$
* Pre-exponential frequency factor: $D_0 = 1.55 \times 10^{-4}\text{ m}^2/\text{s}$
* Diffusion activation energy: $E_D = 73\text{ kcal/mol} = 73\,000\text{ cal/mol}$
* Universal gas constant: $R = 1.987\text{ cal/mol}\cdot\text{K}$

---

## 🧠 2. Phase 2: Frames and Change of Basis

The temperature dependence of diffusivity in solids is formulated through the Arrhenius equation [Session 5 Slide 26]:

$$D = D_0 \exp\left(-\frac{E_D}{RT}\right)$$

### Solution Strategy:
1. Isolate the exponential term by dividing both sides by $D_0$:
   $$\frac{D}{D_0} = \exp\left(-\frac{E_D}{RT}\right)$$
2. Apply the natural logarithm ($\ln$) to both sides to linearise the relation:
   $$\ln\left(\frac{D}{D_0}\right) = -\frac{E_D}{RT} \iff \ln\left(\frac{D_0}{D}\right) = \frac{E_D}{RT}$$
3. Solve analytically for the absolute temperature $T$ in Kelvin:
   $$T = \frac{E_D}{R \cdot \ln(D_0 / D)} = \frac{-E_D}{R \cdot \ln(D / D_0)}$$
4. Evaluate numerically and convert to degrees Celsius ($^\circ\text{C} = \text{K} - 273.15$) to check experimental feasibility.

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Diffusivity Ratio:
We evaluate the quotient between the pre-exponential factor $D_0$ and the target coefficient $D$:
$$\frac{D_0}{D} = \frac{1.55 \times 10^{-4}\text{ m}^2/\text{s}}{1.0 \times 10^{-14}\text{ m}^2/\text{s}} = 1.55 \times 10^{10}$$

---

### 2. Evaluation of the Natural Logarithm:
Taking the natural logarithm of the quotient:
$$\ln\left(\frac{D_0}{D}\right) = \ln(1.55 \times 10^{10}) = \ln(1.55) + 10 \cdot \ln(10)$$

Calculating with decimal precision:
* $\ln(1.55) \approx 0.438255$
* $\ln(10) \approx 2.302585 \implies 10 \cdot \ln(10) \approx 23.025851$
* Adding:
  $$\ln\left(\frac{D_0}{D}\right) = 0.438255 + 23.025851 = \mathbf{23.464106}$$

*(If evaluated as $\ln(D/D_0)$: $\ln\left(\frac{10^{-14}}{1.55 \times 10^{-4}}\right) = -23.464106$).*

---

### 3. Absolute Temperature ($T$):
Substituting the values in consistent calorie units ($\text{cal}$):
* $E_D = 73\,000\text{ cal/mol}$
* $R = 1.987\text{ cal/mol}\cdot\text{K}$
* Denominator:
  $$R \cdot \ln\left(\frac{D_0}{D}\right) = (1.987\text{ cal/mol}\cdot\text{K}) \times (23.464106) = 46.62318\text{ cal/mol}\cdot\text{K}$$

Carrying out the final quotient:
$$T = \frac{73\,000\text{ cal/mol}}{46.62318\text{ cal/mol}\cdot\text{K}} \approx \mathbf{1565.74\text{ K}} \approx \mathbf{1566\text{ K}}$$

### Conversion to the Celsius Scale:
$$T = 1565.74 - 273.15 = \mathbf{1292.59^\circ\text{C}} \approx \mathbf{1293^\circ\text{C}}$$

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Dimensional Analysis:
$$[T] = \frac{[E_D]}{[R] \cdot [\text{adimensional}]} = \frac{\text{cal/mol}}{(\text{cal/mol}\cdot\text{K})} = \text{K} \quad \checkmark$$

### Physical-Technological Interpretation:
1. **Temperature needed:** A diffusivity of $10^{-14}\text{ m}^2/\text{s}$ needs $1293^\circ\text{C}$ ($1566\text{ K}$). Because $D$ depends exponentially on $T$, small changes in temperature change $D$ a lot [Slide 26]. Diffusion of impurities in Si wafers is the process used to fabricate integrated circuits [Slide 29].
2. **High activation energy:** $E_D = 73\text{ kcal/mol} \approx 305.4\text{ kJ/mol}$ is above every self-diffusion value in the table except Mo, so a high temperature is needed to give the atoms enough energy to jump [Slides 4, 9].

---

## 🔗 Related Links
* [[Topic 3 - Diffusion in Solids and Mass Transport]] (Master MOC for Topic 3)
* [[Concept - The Arrhenius Equation and Factors Influencing Diffusivity]]
* [[Problem - T3-03 Activation Energy and Diffusivity of Carbon in Steel]]
* [[Problem - T3-05 Carburising Temperature of 1010 Steel in 8 Hours]]
