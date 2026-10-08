---
materia: "Aerospace Materials I"
tema: "Topic 3: Diffusion in Solids and Mass Transport"
origen: "Problems T3_Diffusion.pdf, Problem 5"
dificultad: high
tags:
  - official-problem
  - solved
  - ficks-second-law
  - carburization
  - arrhenius
  - error-function
  - steel-1010
  - inverse-temperature-design
---

# ✏️ Problem: T3-05 — Carburising Temperature of AISI 1010 Steel in 8 Hours

## 📄 Official Statement
> **5.- A 1010 steel, that contains $0.10\text{ wt}\%\text{ C}$ is subjected to cementation process, in order to obtain effective $\text{C}$ composition of $0.30\text{ wt}\%$ at a depth of $1.16\text{ mm}$ below the surface. Assume that the maximum $\text{C}$ solubility in the steel surface is reached at moment that the carburizing process is initiated, generating a $\text{C}$ concentration at the surface of $1.31\text{ wt}\%$. Determine the required cementation temperature for the process to be successfully carried out within an 8 hour time span.**  
> **Data: $D_0 (\text{C in Fe}) = 16.2\text{ mm}^2/\text{s}$; $E_D = 137\,800\text{ J/mol}$; $R = 8.314\text{ J/mol}\cdot\text{K}$.**  
> *(Solution: $T = 1175\text{ K} = 902^\circ\text{C}$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Physical Hypotheses:
1. **Non-Steady Semi-Infinite Model:** The required depth of the carburised layer ($x = 1.16\text{ mm}$) is small compared with the thickness of the part, allowing rigorous application of the semi-infinite solid solution of Fick's Second Law [Session 5 Slide 20].
2. **Instantaneous Surface Saturation:** The carbon concentration at the surface is assumed to reach instantaneously the solubility limit in equilibrium with the carburising atmosphere and to remain fixed throughout the cycle: $C_s = 1.31\text{ wt}\%$ for all $t > 0$ [Slides 20, 30].
3. **Interstitial Diffusion Governed by Arrhenius:** The diffusion coefficient $D$ of carbon in austenite ($\gamma\text{-Fe}$) obeys the Arrhenius law with the supplied kinetic parameters ($D_0$ and $E_D$) [Slide 26].

### Input Parameters:
* Uniform initial carbon concentration in 1010 steel: $C_0 = 0.10\text{ wt}\%$
* Imposed surface concentration: $C_s = 1.31\text{ wt}\%$
* Required concentration at the design depth: $C_x = 0.30\text{ wt}\%$
* Design depth: $x = 1.16\text{ mm} = 1.16 \times 10^{-3}\text{ m}$
* Available process time: $t = 8\text{ h} = 8 \times 3600\text{ s} = 28\,800\text{ s}$
* Pre-exponential frequency factor: $D_0 = 16.2\text{ mm}^2/\text{s} = 16.2 \times 10^{-6}\text{ m}^2/\text{s}$
* Diffusion activation energy: $E_D = 137\,800\text{ J/mol} = 137.8\text{ kJ/mol}$
* Universal gas constant: $R = 8.314\text{ J/mol}\cdot\text{K}$

---

## 🧠 2. Phase 2: Frames and Change of Basis

This problem elegantly combines the **solution of Fick's Second Law** with the **Arrhenius thermal equation** [Session 5 Slides 20, 26]:

### Stage A: Determination of the Required Diffusivity ($D$)
1. Apply the error-function solution for a semi-infinite solid:
   $$\frac{C_s - C_x}{C_s - C_0} = \text{erf}(z)$$
2. Compute the value of $\text{erf}(z)$ from the given concentrations.
3. Determine the argument $z$ by linear interpolation in the official $\text{erf}(z)$ table [Slide 21].
4. Solve for the required diffusivity $D$ from the definition of $z$:
   $$z = \frac{x}{2\sqrt{Dt}} \implies 2\sqrt{Dt} = \frac{x}{z} \implies D = \frac{x^2}{4 \cdot z^2 \cdot t}$$

### Stage B: Determination of the Process Temperature ($T$)
5. With the numerical value of $D$, equate it to the Arrhenius equation:
   $$D = D_0 \exp\left(-\frac{E_D}{RT}\right) \implies \frac{D}{D_0} = \exp\left(-\frac{E_D}{RT}\right)$$
6. Take the natural logarithm and solve for the absolute temperature $T$:
   $$\ln\left(\frac{D}{D_0}\right) = -\frac{E_D}{RT} \implies T = \frac{-E_D}{R \cdot \ln(D / D_0)} = \frac{E_D}{R \cdot \ln(D_0 / D)}$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Concentration Ratio:
$$\frac{C_s - C_x}{C_s - C_0} = \frac{1.31 - 0.30}{1.31 - 0.10} = \frac{1.01}{1.21} \approx \mathbf{0.83471074}$$

Therefore, we require:
$$\text{erf}(z) = 0.83471074$$

---

### 2. Linear Interpolation in the Official Error Function Table:
Consulting the course $\text{erf}(z)$ table [Session 5 Slide 21]:
* For $z_1 = 0.95 \implies \text{erf}(z_1) = 0.8209$
* For $z_2 = 1.00 \implies \text{erf}(z_2) = 0.8427$

Since $0.8209 < 0.83471074 < 0.8427$, we interpolate linearly:
$$\frac{z - z_1}{z_2 - z_1} = \frac{\text{erf}(z) - \text{erf}(z_1)}{\text{erf}(z_2) - \text{erf}(z_1)}$$

Substituting the values:
$$\frac{z - 0.95}{1.00 - 0.95} = \frac{0.83471074 - 0.8209}{0.8427 - 0.8209}$$
$$\frac{z - 0.95}{0.05} = \frac{0.01381074}{0.0218} \approx 0.633520$$
$$z = 0.95 + 0.05 \times 0.633520 = 0.95 + 0.031676 = \mathbf{0.981676}$$

Squaring:
$$z^2 = (0.981676)^2 \approx \mathbf{0.963688}$$

---

### 3. Required Diffusivity ($D$):
Substituting $x = 1.16 \times 10^{-3}\text{ m}$, $t = 28\,800\text{ s}$ and $z^2 = 0.963688$:
* $x^2 = (1.16 \times 10^{-3}\text{ m})^2 = 1.3456 \times 10^{-6}\text{ m}^2$
* Denominator:
  $$4 \cdot z^2 \cdot t = 4 \times 0.963688 \times 28\,800\text{ s} = 111\,016.86\text{ s}$$
* Diffusion coefficient in SI units:
  $$D = \frac{1.3456 \times 10^{-6}\text{ m}^2}{111\,016.86\text{ s}} \approx \mathbf{1.21207 \times 10^{-11}\text{ m}^2/\text{s}}$$

*(In $\text{mm}^2/\text{s}$: $D = 1.21207 \times 10^{-5}\text{ mm}^2/\text{s}$).*

---

### 4. Temperature from Arrhenius:
We compute the ratio between $D$ and the pre-exponential factor $D_0 = 16.2 \times 10^{-6}\text{ m}^2/\text{s}$:
$$\frac{D}{D_0} = \frac{1.21207 \times 10^{-11}\text{ m}^2/\text{s}}{16.2 \times 10^{-6}\text{ m}^2/\text{s}} \approx 7.48191 \times 10^{-7}$$

Taking the natural logarithm:
$$\ln\left(\frac{D}{D_0}\right) = \ln(7.48191 \times 10^{-7}) = 2.01249 - 16.11810 = -\mathbf{14.10561}$$

Solving for the absolute temperature $T$:
$$T = \frac{-E_D}{R \cdot \ln(D / D_0)} = \frac{-137\,800\text{ J/mol}}{(8.314\text{ J/mol}\cdot\text{K}) \times (-14.10561)}$$
$$T = \frac{137\,800}{117.275} \approx \mathbf{1175.02\text{ K}} \approx \mathbf{1175\text{ K}}$$

### Conversion to the Celsius Scale:
$$T = 1175.02 - 273.15 = \mathbf{901.87^\circ\text{C}} \approx \mathbf{902^\circ\text{C}}$$

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Dimensional Analysis:
* $[D] = \frac{[x]^2}{[t]} = \frac{\text{m}^2}{\text{s}} \quad \checkmark$
* $[T] = \frac{[E_D]}{[R] \cdot [\ln(D/D_0)]} = \frac{\text{J/mol}}{(\text{J/mol}\cdot\text{K}) \cdot 1} = \text{K} \quad \checkmark$

### Interpretation and Engineering Relevance:
1. **Work-Shift Cycle Time Control:** In the automotive and aerospace industries, a carburising cycle of exactly **8 hours** is synchronised with a full work shift. Knowing the precise temperature ($902^\circ\text{C}$) allows the engineer to program the furnace with certainty of reaching the required case depth ($1.16\text{ mm}$ at $0.30\text{ wt}\%$) without overheating the part [Slide 30].
2. **Stable Austenitic Structure:** At $902^\circ\text{C}$ ($1175\text{ K}$), AISI 1010 steel lies comfortably in the homogeneous austenitic field ($\gamma\text{-Fe}$), where the carbon solubility reaches up to the $1.31\text{ wt}\%$ fixed at the surface [Slides 23, 30].
3. **Energy Optimisation:** If it were operated at a lower temperature, e.g. $850^\circ\text{C}$ ($1123.15\text{ K}$), $D$ falls by a factor $\exp\!\left[\frac{E_D}{R}\left(\frac{1}{1123.15} - \frac{1}{1175.02}\right)\right] = e^{0.6516} = 1.92$, so the required time would be multiplied by $\approx 1.9$ (almost double, not triple); conversely, at higher temperatures $D$ grows exponentially and the time decreases [Session 5 Slide 26].

---

## 🔗 Related Links
* [[Topic 3 - Diffusion in Solids and Mass Transport]] (Master MOC for Topic 3)
* [[Concept - Fick's Second Law, Non-Steady-State Diffusion and the Error Function]]
* [[Concept - The Arrhenius Equation and Factors Influencing Diffusivity]]
* [[Concept - Carburizing and Industrial Applications of Diffusion]]
* [[Problem - T3-01 Carburisation of a 1018 Steel Gear]]
