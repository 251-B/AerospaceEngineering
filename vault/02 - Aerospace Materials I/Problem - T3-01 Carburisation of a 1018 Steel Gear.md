---
materia: "Aerospace Materials I"
tema: "Topic 3: Diffusion in Solids and Mass Transport"
origen: "Problems T3_Diffusion.pdf, Problem 1"
dificultad: medium
tags:
  - official-problem
  - solved
  - ficks-second-law
  - carburization
  - error-function
  - steel-1018
  - semi-infinite-solid
---

# ✏️ Problem: T3-01 — Carburisation of an AISI 1018 Steel Gear

## 📄 Official Statement
> **1. In a steel gear of grade 1018 (0.18 wt% in C) a cementation process is carried out at $927^\circ\text{C}$. Calculate the time required in order to increase the C content up to $0.3\text{ wt}\%$ at $0.6\text{ mm}$ below the surface of the gear. Assume that the C content in the surface is $1\text{ wt}\%$. Data: $D_{\text{C in } \gamma\text{-Fe}} = 1.28 \times 10^{-11}\text{ m}^2/\text{s}$.**  
> *(Solution: $t = 6636\text{ s}$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Physical Hypotheses:
1. **Semi-Infinite Solid:** Since the required carburising depth ($x = 0.6\text{ mm}$) is orders of magnitude smaller than the macroscopic dimensions of the gear tooth (typically $10\text{--}50\text{ mm}$), the diffusion can be modelled exactly as one-dimensional in a semi-infinite solid ($0 \le x < \infty$) [Session 5 Slide 20].
2. **Constant Surface Concentration:** The reactive methane and hydrogen gas atmosphere ($\text{CH}_4 - \text{H}_2$) maintains a constant carbon chemical activity at the surface of the part throughout the treatment: $C(0, t) = C_s = 1.0\text{ wt}\%$ for all $t > 0$ [Slides 20, 30].
3. **Homogeneous Initial Composition:** The original AISI 1018 steel contains a uniform carbon mass fraction throughout its volume: $C(x, 0) = C_0 = 0.18\text{ wt}\%$.
4. **Constant Diffusivity:** The diffusion coefficient of carbon in austenite ($\gamma\text{-Fe}$, FCC structure) is assumed invariant with local concentration in this compositional range ($0.18\text{--}1.0\text{ wt}\%$): $D \neq f(C)$ [Slide 19].

### Input Parameters:
* Uniform initial concentration in the steel: $C_0 = 0.18\text{ wt}\%$
* Imposed surface concentration: $C_s = 1.00\text{ wt}\%$
* Required concentration at the depth of interest: $C_x = 0.30\text{ wt}\%$
* Treatment depth: $x = 0.6\text{ mm} = 0.6 \times 10^{-3}\text{ m} = 6.0 \times 10^{-4}\text{ m}$
* Operating temperature: $T = 927^\circ\text{C} = 927 + 273.15 = 1200.15\text{ K}$
* Diffusion coefficient provided: $D = 1.28 \times 10^{-11}\text{ m}^2/\text{s}$

---

## 🧠 2. Phase 2: Frames and Change of Basis

Non-steady-state carbon diffusion in a semi-infinite medium with constant surface concentration is governed by the analytical solution of **Fick's Second Law**, expressed through the Gauss error function [Session 5 Slide 20]:

$$\frac{C_x - C_0}{C_s - C_0} = 1 - \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right)$$

Rearranging in direct terms of the error function:
$$\frac{C_s - C_x}{C_s - C_0} = \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right) = \text{erf}(z)$$

where we define the dimensionless argument:
$$z \equiv \frac{x}{2\sqrt{Dt}}$$

### Solution Strategy:
1. Evaluate the dimensionless concentration ratio $\frac{C_s - C_x}{C_s - C_0}$.
2. Equate this numerical value to $\text{erf}(z)$ and consult the course **Official Error Function Table** [Session 5 Slide 21].
3. Perform an **exact linear interpolation** between the two adjacent tabulated values to determine the argument $z$ with maximum precision.
4. Solve for the treatment time $t$ from the definition of $z$:
   $$z = \frac{x}{2\sqrt{Dt}} \implies 2\sqrt{Dt} = \frac{x}{z} \implies Dt = \frac{x^2}{4z^2} \implies t = \frac{x^2}{4z^2 D}$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Concentration Ratio:
Substituting the values from the statement:
$$\frac{C_s - C_x}{C_s - C_0} = \frac{1.00 - 0.30}{1.00 - 0.18} = \frac{0.70}{0.82} = \frac{35}{41} \approx 0.8536585$$

Therefore:
$$\text{erf}(z) = 0.8536585$$

---

### 2. Search and Linear Interpolation in the Official Table:
Examining the official $\text{erf}(z)$ table [Session 5 Slide 21; Problems T3]:
* For $z_1 = 1.00 \implies \text{erf}(z_1) = 0.8427$
* For $z_2 = 1.10 \implies \text{erf}(z_2) = 0.8802$

Since $0.8427 < 0.8536585 < 0.8802$, we apply the linear interpolation formula:
$$\frac{z - z_1}{z_2 - z_1} = \frac{\text{erf}(z) - \text{erf}(z_1)}{\text{erf}(z_2) - \text{erf}(z_1)}$$

Substituting the values:
$$\frac{z - 1.00}{1.10 - 1.00} = \frac{0.8536585 - 0.8427}{0.8802 - 0.8427}$$
$$\frac{z - 1.00}{0.10} = \frac{0.0109585}{0.0375} \approx 0.292227$$
$$z = 1.00 + 0.10 \times 0.292227 = 1.00 + 0.029223 = \mathbf{1.02922}$$

Squaring the value of $z$:
$$z^2 = (1.02922)^2 \approx \mathbf{1.05930}$$

---

### 3. Solving for the Carburising Time ($t$):
Starting from:
$$z = \frac{x}{2\sqrt{Dt}}$$

We solve algebraically for the time $t$:
$$\sqrt{t} = \frac{x}{2z\sqrt{D}} \implies t = \frac{x^2}{4 \cdot z^2 \cdot D}$$

Substituting the magnitudes in consistent SI units ($x = 6.0 \times 10^{-4}\text{ m}$, $D = 1.28 \times 10^{-11}\text{ m}^2/\text{s}$):
$$x^2 = (6.0 \times 10^{-4}\text{ m})^2 = 3.60 \times 10^{-7}\text{ m}^2$$
$$4 \cdot z^2 \cdot D = 4 \times 1.05930 \times 1.28 \times 10^{-11}\text{ m}^2/\text{s} = 5.4236 \times 10^{-11}\text{ m}^2/\text{s}$$

Carrying out the quotient:
$$t = \frac{3.60 \times 10^{-7}\text{ m}^2}{5.4236 \times 10^{-11}\text{ m}^2/\text{s}} \approx \mathbf{6638\text{ s}}$$

> [!warning] Discrepancy with the official solution
> The official key gives $t = 6636\text{ s}$. Linear interpolation in the table gives $z = 1.0292$ and $t = 6637.6\text{ s} \approx 6638\text{ s}$ (the exact inverse error function, $z = 1.0271$, would give $6665\text{ s}$ because the table is linear between $1.00$ and $1.10$). The key is $0.02\%$ below the interpolated value; this is a rounding difference, and the interpolated value is reported.

### Conversion to Hours:
$$t = \frac{6638\text{ s}}{3600\text{ s/h}} \approx \mathbf{1.844\text{ h}} \quad (\approx 1\text{ hour, } 50\text{ minutes and } 38\text{ seconds})$$

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Dimensional Analysis:
$$[t] = \frac{[x]^2}{[z]^2 \cdot [D]} = \frac{\text{m}^2}{1 \cdot (\text{m}^2/\text{s})} = \text{s} \quad \checkmark$$

### Physical-Metallurgical Interpretation:
1. **Industrial Viability:** A treatment time of approximately **$1.84\text{ hours}$** at $927^\circ\text{C}$ is extraordinarily reasonable and economically viable for a surface carburising cycle in continuous industrial gear furnaces [Slide 30].
2. **Effect of Temperature:** The chosen temperature ($927^\circ\text{C} = 1200\text{ K}$) places the steel in the pure austenitic phase ($\gamma\text{-Fe}$), where the maximum carbon solubility exceeds $1.0\text{ wt}\%$, making it possible to reach the desired $1\text{ wt}\%$ at the surface without premature precipitation of harmful massive carbides at the surface [Slide 24].
3. **Fatigue Resistance:** Carbon diffusion to $0.6\text{ mm}$ ensures a hardened layer (*case depth*) sufficient to withstand the high Hertzian contact pressures between gear teeth and to generate compressive residual stresses that prevent fatigue cracking [Slide 30].

---

## 🔗 Related Links
* [[Topic 3 - Diffusion in Solids and Mass Transport]] (Master MOC for Topic 3)
* [[Concept - Fick's Second Law, Non-Steady-State Diffusion and the Error Function]]
* [[Concept - Carburizing and Industrial Applications of Diffusion]]
* [[Problem - T3-05 Carburising Temperature of 1010 Steel in 8 Hours]]
