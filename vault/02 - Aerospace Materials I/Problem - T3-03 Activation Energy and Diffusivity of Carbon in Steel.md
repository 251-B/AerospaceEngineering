---
materia: "Aerospace Materials I"
tema: "Topic 3: Diffusion in Solids and Mass Transport"
origen: "Problems T3_Diffusion.pdf, Problem 3"
dificultad: medium
tags:
  - official-problem
  - solved
  - arrhenius
  - activation-energy
  - carbon-in-steel
  - two-point-method
---

# ✏️ Problem: T3-03 — Activation Energy and Diffusivity of Carbon in Mild Steel

## 📄 Official Statement
> **3.- The diffusivity of carbon in mild steel was measured at two different temperatures:**  
> **Data: $R = 8.314\text{ J/mol}\cdot\text{K}$**  
> 
> | Temperature ($^\circ\text{C}$) | Diffusivity ($\text{m}^2/\text{s}$) |
> | :---: | :---: |
> | 850 | $4.826 \times 10^{-12}$ |
> | 950 | $1.805 \times 10^{-11}$ |
> 
> **Using these data, calculate:**  
> **a) The activation energy for the C diffusion in mild steel, for the temperature interval of $850^\circ\text{C}$ to $950^\circ\text{C}$ *(Solution: $E_D = 36\text{ kcal/mol}$)*.**  
> **b) The diffusivity at $1000^\circ\text{C}$, assuming that the activation energy does not change at this temperature range. *(Solution: $D = 3.23 \times 10^{-11}\text{ m}^2/\text{s}$)*.**

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Physical Hypotheses:
1. **Monotonic Arrhenius Behaviour:** The dependence of the diffusivity of carbon in the austenitic lattice of mild steel ($\gamma\text{-Fe}$, FCC) strictly follows the Arrhenius law in the thermal interval $850^\circ\text{C}\text{--}1000^\circ\text{C}$ with no allotropic phase changes occurring in that range (assumption: the steel is fully austenitic over the whole interval, i.e. above its $A_3$ temperature; the slides do not give $A_3$, which depends on the carbon content) [Session 5 Slides 23-26].
2. **Invariance of $E_D$ and $D_0$:** The activation energy $E_D$ and the pre-exponential factor $D_0$ remain constant over the thermal range considered.

### Input Parameters:
* State 1: $T_1 = 850^\circ\text{C} = 850 + 273.15 = 1123.15\text{ K}$, with $D_1 = 4.826 \times 10^{-12}\text{ m}^2/\text{s}$
* State 2: $T_2 = 950^\circ\text{C} = 950 + 273.15 = 1223.15\text{ K}$, with $D_2 = 1.805 \times 10^{-11}\text{ m}^2/\text{s}$
* Target state 3: $T_3 = 1000^\circ\text{C} = 1000 + 273.15 = 1273.15\text{ K}$, unknown $D_3$
* Gas constant: $R = 8.314\text{ J/mol}\cdot\text{K}$
* Calorie equivalence: $1\text{ cal} = 4.184\text{ J} \implies R = 1.987\text{ cal/mol}\cdot\text{K}$

---

## 🧠 2. Phase 2: Frames and Change of Basis

The diffusivity at two given temperatures obeys the Arrhenius law in two-point form [Session 5 Slide 26]:

$$D_1 = D_0 \exp\left(-\frac{E_D}{R T_1}\right), \qquad D_2 = D_0 \exp\left(-\frac{E_D}{R T_2}\right)$$

### For Part (a) — Determination of $E_D$:
Dividing term by term to eliminate the pre-exponential factor $D_0$:
$$\frac{D_2}{D_1} = \exp\left[-\frac{E_D}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)\right] = \exp\left[\frac{E_D}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)\right]$$

Taking the natural logarithm:
$$\ln\left(\frac{D_2}{D_1}\right) = \frac{E_D}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right) \implies E_D = \frac{R \cdot \ln(D_2 / D_1)}{\frac{1}{T_1} - \frac{1}{T_2}}$$

### For Part (b) — Determination of $D_3$ at $1000^\circ\text{C}$:
Relating state 3 to state 2 (or state 1):
$$\ln\left(\frac{D_3}{D_2}\right) = -\frac{E_D}{R}\left(\frac{1}{T_3} - \frac{1}{T_2}\right) = \frac{E_D}{R}\left(\frac{1}{T_2} - \frac{1}{T_3}\right)$$
$$D_3 = D_2 \cdot \exp\left[\frac{E_D}{R}\left(\frac{1}{T_2} - \frac{1}{T_3}\right)\right]$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### Part (a): Activation Energy ($E_D$)

1. **Diffusivity ratio:**
   $$\frac{D_2}{D_1} = \frac{1.805 \times 10^{-11}\text{ m}^2/\text{s}}{4.826 \times 10^{-12}\text{ m}^2/\text{s}} = 3.7401575$$
   $$\ln\left(\frac{D_2}{D_1}\right) = \ln(3.7401575) \approx 1.319128$$

2. **Difference of inverse temperatures:**
   $$\frac{1}{T_1} = \frac{1}{1123.15\text{ K}} \approx 8.903530 \times 10^{-4}\text{ K}^{-1}$$
   $$\frac{1}{T_2} = \frac{1}{1223.15\text{ K}} \approx 8.175612 \times 10^{-4}\text{ K}^{-1}$$
   $$\frac{1}{T_1} - \frac{1}{T_2} = (8.903530 - 8.175612) \times 10^{-4} = 7.27918 \times 10^{-5}\text{ K}^{-1}$$

   *(If the integer scale $T_1 = 1123\text{ K}$ and $T_2 = 1223\text{ K}$ is used: $\frac{1}{1123} - \frac{1}{1223} = 7.281 \times 10^{-5}\text{ K}^{-1}$).*

3. **$E_D$ in SI units ($\text{J/mol}$):**
   $$E_D = \frac{8.314\text{ J/mol}\cdot\text{K} \times 1.319128}{7.27918 \times 10^{-5}\text{ K}^{-1}} = \frac{10.96723}{7.27918 \times 10^{-5}} \approx \mathbf{150\,666\text{ J/mol}} = \mathbf{150.67\text{ kJ/mol}}$$

4. **Conversion to $\text{kcal/mol}$:**
   $$E_D = \frac{150\,666\text{ J/mol}}{4184\text{ J/kcal}} \approx \mathbf{36.01\text{ kcal/mol}} \approx \mathbf{36\text{ kcal/mol}}$$
   *(Or using $R = 1.987\text{ cal/mol}\cdot\text{K}$: $E_D = \frac{1.987 \times 1.319128}{7.27918 \times 10^{-5}} = 36009\text{ cal/mol} \approx \mathbf{36\text{ kcal/mol}}$).*

---

### Part (b): Diffusivity at $1000^\circ\text{C}$ ($T_3 = 1273.15\text{ K}$)

1. **Difference of inverses between $T_2$ and $T_3$:**
   $$\frac{1}{T_3} = \frac{1}{1273.15\text{ K}} \approx 7.854534 \times 10^{-4}\text{ K}^{-1}$$
   $$\frac{1}{T_2} - \frac{1}{T_3} = (8.175612 - 7.854534) \times 10^{-4} = 3.21078 \times 10^{-5}\text{ K}^{-1}$$

2. **Evaluation of the thermal exponent:**
   $$\Delta_{\text{exp}} = \frac{E_D}{R}\left(\frac{1}{T_2} - \frac{1}{T_3}\right) = \frac{150\,666\text{ J/mol}}{8.314\text{ J/mol}\cdot\text{K}} \times (3.21078 \times 10^{-5}\text{ K}^{-1})$$
   $$\Delta_{\text{exp}} = 18121.96 \times 3.21078 \times 10^{-5} \approx 0.581857$$

3. **Exponential ratio and final diffusivity:**
   $$\exp(\Delta_{\text{exp}}) = e^{0.581857} \approx 1.78936$$
   $$D_3 = D_2 \times 1.78936 = (1.805 \times 10^{-11}\text{ m}^2/\text{s}) \times 1.78936 \approx \mathbf{3.2298 \times 10^{-11}\text{ m}^2/\text{s}} \approx \mathbf{3.23 \times 10^{-11}\text{ m}^2/\text{s}}$$

*(Session 5 Slide 23 lists $D_{\text{C en Fe-FCC}} \approx 3 \times 10^{-11}\text{ m}^2/\text{s}$ at $1000^\circ\text{C}$: same order of magnitude as the $3.23 \times 10^{-11}$ obtained, the slide value being a one-significant-figure figure).*

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Physical and Dimensional Coherence:
1. **Dimensional Analysis:**
   * $[E_D] = \frac{[\text{J/mol}\cdot\text{K}]}{[\text{K}^{-1}]} = \text{J/mol} \quad \checkmark$
   * $[D_3] = [D_2] \cdot [e^{\text{adimensional}}] = \text{m}^2/\text{s} \quad \checkmark$
2. **Thermal Sensitivity in Steels:** An increase of only $50^\circ\text{C}$ (from $950^\circ\text{C}$ to $1000^\circ\text{C}$) raises the diffusivity by a factor of:
   $$\frac{D_{1000^\circ\text{C}}}{D_{950^\circ\text{C}}} = \frac{3.23 \times 10^{-11}}{1.805 \times 10^{-11}} \approx 1.79 \quad (+79\%)$$
   This explains why industrial carburising treatments seek the maximum admissible austenitising temperature, since it drastically shortens furnace times and reduces energy costs, provided that excessive grain growth is not promoted [Slides 25, 30].
3. **Magnitude of the Activation Energy:** The value $E_D \approx 36\text{ kcal/mol} \approx 150.7\text{ kJ/mol}$ is characteristic of an **interstitial** mechanism (where the carbon atom migrates between octahedral holes of the FCC lattice without needing to create vacancies). For substitutional self-diffusion of iron in the same FCC lattice, the required activation energy is higher (e.g. $\alpha\text{-Fe}$: $E_a = 240\text{ kJ/mol} = 57.5\text{ kcal/mol}$) [Slide 9].

---

## 🔗 Related Links
* [[Topic 3 - Diffusion in Solids and Mass Transport]] (Master MOC for Topic 3)
* [[Concept - The Arrhenius Equation and Factors Influencing Diffusivity]]
* [[Concept - Diffusion Mechanisms, Vacancies and Interstitials]]
* [[Problem - T3-02 Diffusion of Aluminium in Single-Crystal Silicon]]
* [[Problem - T3-05 Carburising Temperature of 1010 Steel in 8 Hours]]
