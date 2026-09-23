---
materia: "Advanced Mathematics"
tema: "Tema 1: Introduction, Modeling and Classification of ODEs"
origen: "ProblemsCh1.pdf — Exercise 1.4"
dificultad: baja
tags:
  - problema-resuelto
  - ley-enfriamiento-newton
  - modelado-termico
  - clasificacion-variables
---

# ✏️ Problem 1.4: Newton's Law of Cooling Modeling

## 📄 Enunciado (Problem Statement)

A cup of hot chocolate is initially at temperature $T(0)$ and is left in the room with an ambient temperature $T_A(t)$. The rate of cooling of the hot chocolate is proportional to the difference between the current temperature $T(t)$ and the ambient temperature.

(i) Which are the dependent variable, the independent variable, and the parameters?  
(ii) Write a linear differential equation for the temperature of the hot chocolate that takes into account the heat exchange with the room. Such differential equation is known as Newton's law of cooling.

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Physical Setup:
* System: Liquid hot chocolate contained in a mug placed within a room.
* Surrounding medium: Ambient air at time-dependent temperature $T_A(t)$.
* Initial condition: $T(0) = T_0$.

### Hypotheses:
* [x] **Lumped capacitance approximation:** The fluid inside the mug is well-mixed or has high thermal diffusivity such that temperature spatial gradients inside the liquid are negligible ($\text{Bi} = \frac{h L_c}{\kappa} \ll 0.1$). The temperature depends only on time: $T = T(t)$.
* [x] **Newtonian convective cooling:** The heat flux between the mug surface and the ambient air is linear in the temperature difference $(T - T_A(t))$.
* [x] **Constant thermo-physical properties:** Mass $m$, surface area $A_s$, specific heat capacity $c_p$, and heat transfer coefficient $h$ remain constant over the cooling process.

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

1. **Variables and Parameters Classification:**
   * Distinguish between the dynamical state that changes over time (dependent variable), the axis of evolution (independent variable), and the geometric/physical constants (parameters).
2. **First Law of Thermodynamics (Energy Conservation):**
   The time rate of change of internal thermal energy $E_{\text{thermal}}$ of the liquid equals the net rate of heat transfer $\dot{Q}$:
   $$ \frac{dE_{\text{thermal}}}{dt} = \dot{Q}_{\text{in}} - \dot{Q}_{\text{out}} = -\dot{Q}_{\text{loss}} $$
   where $E_{\text{thermal}} = m c_p T(t)$.
3. **Convective Heat Exchange:**
   $$ \dot{Q}_{\text{loss}} = h A_s \left( T(t) - T_A(t) \right) $$
4. Combine the energy balance with the convective relation, divide by the thermal capacitance $m c_p$, and define the lumped thermal relaxation constant $k = \frac{h A_s}{m c_p} > 0$.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Part (i): Identification of Variables and Parameters

1. **Independent Variable:**
   * **$t$ (Time):** The physical dimension across which the thermal relaxation occurs $[s]$ (or $[\text{min}], [\text{h}]$).
2. **Dependent Variable:**
   * **$T$ or $T(t)$ (Temperature of the hot chocolate):** The thermodynamic state function to be solved $[{}^\circ\text{C}]$ or $[\text{K}]$.
3. **Parameters and Prescribed Functions:**
   * **$k$ (Cooling proportionality constant):** Represents the inverse thermal time constant $[t^{-1}]$, combining geometry and heat transfer properties ($k = \frac{h A_s}{m c_p}$).
   * **$T(0)$ or $T_0$ (Initial temperature):** Boundary data at $t = 0$ $[{}^\circ\text{C}]$.
   * **$T_A(t)$ (Ambient room temperature):** An externally specified function representing the thermal reservoir. If the room is thermostatically regulated, $T_A$ acts as a constant parameter.

---

### Part (ii): Derivation of the Differential Equation

#### Step 1: Physical Rate Balance
The rate of cooling is the negative derivative of temperature $-\frac{dT}{dt}$. The problem statement dictates:
$$ \text{Rate of cooling} \propto \left( T(t) - T_A(t) \right) $$

Let $k > 0$ be the positive constant of proportionality:
$$ -\frac{dT}{dt} = k \left( T(t) - T_A(t) \right) $$

Multiplying both sides by $-1$:
$$ \mathbf{\frac{dT}{dt} = -k \left( T(t) - T_A(t) \right)} \tag{1} $$

#### Step 2: Verification of the Physical Sign
* If the chocolate is hotter than the room ($T(t) > T_A(t)$):
  $$ T(t) - T_A(t) > 0 \implies \frac{dT}{dt} = -k(+ \dots) < 0 $$
  The temperature decreases, which corresponds correctly to cooling.
* If the chocolate is colder than the room ($T(t) < T_A(t)$):
  $$ T(t) - T_A(t) < 0 \implies \frac{dT}{dt} = -k(- \dots) > 0 $$
  The temperature increases (warming).

#### Step 3: Canonical Linear Form
Expand and rearrange equation $(1)$:
$$ \frac{dT}{dt} = -k T + k T_A(t) $$
$$ \mathbf{\frac{dT}{dt} + k T(t) = k T_A(t)} \tag{2} $$

Comparing with the official UC3M linear ODE definition:
$$ a_1(t) \frac{dT}{dt} + a_0(t) T = b(t) $$
we identify:
$$ a_1(t) = 1, \quad a_0(t) = k, \quad b(t) = k T_A(t) $$
Since $a_1(t), a_0(t), b(t)$ do not depend on the dependent variable $T$, and $T$ and its derivative appear to the first power, the ODE is strictly **linear of order 1**.

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Final Answers:
* **(i) Variables & Parameters:**
  * **Independent Variable:** $t$ (time)
  * **Dependent Variable:** $T(t)$ (temperature of the hot chocolate)
  * **Parameters:** $k$ (cooling constant), $T(0)$ (initial temperature), and ambient temperature $T_A$ (if constant).
* **(ii) Governing ODE:**
  $$ \mathbf{\frac{dT}{dt} = -k \left( T - T_A(t) \right) \iff \frac{dT}{dt} + k T = k T_A(t)} $$

### Dimensional & Asymptotic Check:
1. **Dimensional Consistency:**
   $$ \left[ \frac{dT}{dt} \right] = \frac{\Theta}{T} $$
   $$ [k (T - T_A)] = [k] \cdot [\Theta] = \frac{1}{T} \cdot \Theta = \frac{\Theta}{T} $$
   Units match identically on both sides.
2. **Thermal Equilibrium ($t \to \infty$):**
   If $T_A(t) = T_A = \text{const}$, solving $(2)$ yields $T(t) = T_A + (T(0) - T_A)e^{-kt}$.
   As $t \to \infty$, $e^{-kt} \to 0$, giving $\lim_{t\to\infty} T(t) = T_A$, satisfying the Second Law of Thermodynamics (thermal equilibrium with the reservoir).

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - First-Order Physical Models|First-Order Physical Models]]`
* `[[04 - Advanced Maths/Concepto - Linearity and Order of Differential Equations|Linearity and Order of Differential Equations]]`
* `[[04 - Advanced Maths/Problema - Ch1-P5 Forensic Time of Death Estimation|Problem 1.5: Forensic Time of Death Estimation]]`
