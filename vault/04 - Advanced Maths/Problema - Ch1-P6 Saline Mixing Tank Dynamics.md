---
materia: "Advanced Mathematics"
tema: "Tema 1: Introduction, Modeling and Classification of ODEs"
origen: "ProblemsCh1.pdf — Exercise 1.6"
dificultad: media
tags:
  - problema-resuelto
  - cstr
  - balance-materia
  - tanque-mezcla
  - factor-integrante
---

# ✏️ Problem 1.6: Saline Mixing Tank Dynamics

## 📄 Enunciado (Problem Statement)

A tank contains 100 liters of water with 1 kg of salt dissolved in it (uniformly). At time $t_0 = 0$, water without salt flows into the tank at a rate of 1 liter per minute, while the mixture flows out at the same rate.

(i) Write a differential equation for $x(t)$, which is the number of kg of salt dissolved in the tank at time $t \ge 0$.  
(ii) How much salt is dissolved in the tank as $t \to \infty$?  
(iii) What happens if water with $s$ kg of salt per liter flows into the tank at a given rate while the mixture (that is kept uniform) flows out at the same rate?

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Known Parameters (Parts i and ii):
* Tank fluid volume: $V_0 = 100\text{ L}$.
* Initial mass of dissolved salt: $x(0) = x_0 = 1\text{ kg}$.
* Volumetric flow rate in: $Q_{\text{in}} = 1\text{ L/min}$.
* Volumetric flow rate out: $Q_{\text{out}} = 1\text{ L/min}$.
* Salt concentration in the inlet stream: $C_{\text{in}} = 0\text{ kg/L}$ (pure water).

### Unknowns:
1. Differential equation governing salt mass $x(t)$ $[\text{kg}]$.
2. Analytical expression for $x(t)$ and asymptotic limit as $t \to \infty$.
3. Generalization for an arbitrary inlet concentration $C_{\text{in}} = s$ $[\text{kg/L}]$ and arbitrary matched flow rate $Q$ $[\text{L/min}]$.

### Modeling Hypotheses:
* [x] **Constant tank volume:** Since $Q_{\text{in}} = Q_{\text{out}} = Q$, the total liquid volume in the tank is constant:
  $$ \frac{dV}{dt} = Q_{\text{in}} - Q_{\text{out}} = 0 \implies V(t) \equiv V_0 = 100\text{ L} $$
* [x] **Perfect instantaneous mixing (CSTR assumption):** The salt is distributed uniformly throughout the tank volume at every instant $t$, so the outflow concentration equals the bulk concentration:
  $$ C_{\text{out}}(t) = C_{\text{tank}}(t) = \frac{x(t)}{V(t)} = \frac{x(t)}{100} $$
* [x] **Incompressible fluid:** Dissolved salt does not alter the volumetric flow rate.

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

1. Apply the fundamental conservation law of species mass for the dissolved solute:
   $$ \frac{dx}{dt} = \dot{m}_{\text{in}} - \dot{m}_{\text{out}} $$
   where $\dot{m}_{\text{in}} = Q_{\text{in}} C_{\text{in}}$ and $\dot{m}_{\text{out}} = Q_{\text{out}} C_{\text{out}}(t)$.
2. Substitute the specific values for the pure water flushing case ($C_{\text{in}} = 0$), integrate the resulting separable ODE, and evaluate the asymptotic limit as $t \to \infty$.
3. For the general case with inlet concentration $s$, formulate the inhomogeneous linear first-order ODE, solve using an integrating factor $\mu(t)$, and determine the new steady-state equilibrium.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Part (i): Differential Equation for Pure Water Flushing
The rate of mass entering the tank is:
$$ \dot{m}_{\text{in}} = Q_{\text{in}} \cdot C_{\text{in}} = (1\text{ L/min}) \cdot (0\text{ kg/L}) = 0\text{ kg/min} $$

The rate of mass leaving the tank is:
$$ \dot{m}_{\text{out}} = Q_{\text{out}} \cdot C_{\text{out}}(t) = (1\text{ L/min}) \cdot \left( \frac{x(t)}{100}\text{ kg/L} \right) = \frac{x(t)}{100}\text{ kg/min} $$

Applying the mass balance $\frac{dx}{dt} = \dot{m}_{\text{in}} - \dot{m}_{\text{out}}$:
$$ \mathbf{\frac{dx}{dt} = -\frac{x(t)}{100}} \tag{1} $$
with the initial condition $x(0) = 1\text{ kg}$.

---

### Part (ii): Solution and Asymptotic Limit as $t \to \infty$
Equation $(1)$ is a separable first-order linear ODE:
$$ \frac{1}{x} \, dx = -\frac{1}{100} \, dt $$

Integrate both sides from $t = 0$ ($x = 1$) to $t$ ($x = x(t)$):
$$ \int_1^{x(t)} \frac{1}{\xi} \, d\xi = \int_0^t -\frac{1}{100} \, ds $$
$$ \left[ \ln\xi \right]_1^{x(t)} = -\frac{1}{100} [s]_0^t $$
$$ \ln(x(t)) - \ln(1) = -\frac{t}{100} $$
Since $\ln(1) = 0$:
$$ \ln(x(t)) = -\frac{t}{100} $$

Exponentiating both sides:
$$ \mathbf{x(t) = e^{-t/100}\text{ kg}} \tag{2} $$

#### Asymptotic Evaluation:
Take the limit as $t \to \infty$:
$$ \lim_{t \to \infty} x(t) = \lim_{t \to \infty} e^{-t/100} = \mathbf{0\text{ kg}} $$

*Physical Meaning:* The continuous influx of fresh water completely flushes out (washes out) the solute asymptotically.

---

### Part (iii): General Case with Inlet Saline Concentration $s$
Let the inlet concentration be $C_{\text{in}} = s$ $[\text{kg/L}]$, and let the matched volumetric flow rate be $Q$ $[\text{L/min}]$ across tank volume $V$ $[\text{L}]$:
$$ \dot{m}_{\text{in}} = Q \cdot s $$
$$ \dot{m}_{\text{out}} = Q \cdot \frac{x(t)}{V} $$

The general differential mass balance is:
$$ \frac{dx}{dt} = Q s - \frac{Q}{V} x(t) $$
Rearranging into standard linear form:
$$ \mathbf{\frac{dx}{dt} + \frac{Q}{V} x(t) = Q s} \tag{3} $$

#### Solving via Integrating Factor:
Define the characteristic residence timescale $\tau = \frac{V}{Q}$:
$$ \frac{dx}{dt} + \frac{1}{\tau} x = Q s $$
The integrating factor is:
$$ \mu(t) = \exp\left( \int \frac{1}{\tau} \, dt \right) = e^{t/\tau} $$

Multiply both sides of $(3)$ by $e^{t/\tau}$:
$$ e^{t/\tau} \frac{dx}{dt} + \frac{1}{\tau} e^{t/\tau} x = Q s e^{t/\tau} $$
Recognizing the product rule on the left-hand side:
$$ \frac{d}{dt}\left[ x(t) e^{t/\tau} \right] = Q s e^{t/\tau} $$

Integrate both sides with respect to $t$:
$$ x(t) e^{t/\tau} = \int Q s e^{t/\tau} \, dt = Q s \left( \tau e^{t/\tau} \right) + C $$
Since $Q \tau = Q \cdot \frac{V}{Q} = V$:
$$ x(t) e^{t/\tau} = s V e^{t/\tau} + C $$

Multiply both sides by $e^{-t/\tau}$:
$$ x(t) = s V + C e^{-t/\tau} \tag{4} $$

#### Applying the Initial Condition $x(0) = x_0$:
$$ x_0 = s V + C e^0 \implies C = x_0 - s V $$

Substituting $C$ back into $(4)$:
$$ \mathbf{x(t) = s V + (x_0 - s V) e^{-\frac{Q}{V} t}} \tag{5} $$

#### Asymptotic Behavior as $t \to \infty$:
Since $\frac{Q}{V} > 0$, $\lim_{t\to\infty} e^{-\frac{Q}{V} t} = 0$:
$$ \lim_{t \to \infty} x(t) = s V + (x_0 - s V) \cdot 0 = \mathbf{s V} $$

The corresponding steady-state concentration in the tank is:
$$ C_\infty = \lim_{t \to \infty} \frac{x(t)}{V} = \frac{s V}{V} = \mathbf{s} $$

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Summary of Solutions:
* **(i) Washout Differential Equation:**
  $$ \frac{dx}{dt} = -\frac{x}{100} \quad [\text{kg/min}] $$
* **(ii) Solute Remaining as $t \to \infty$:**
  $$ x(t) = e^{-t/100}\text{ kg} \implies \lim_{t \to \infty} x(t) = \mathbf{0\text{ kg}} $$
* **(iii) General Inflow Solution & Limit:**
  $$ x(t) = s V + (x_0 - s V)e^{-\frac{Q}{V}t} \implies \lim_{t \to \infty} x(t) = \mathbf{s V} $$
  For the given numbers ($V = 100\text{ L}$, $Q = 1\text{ L/min}$, $x_0 = 1\text{ kg}$):
  $$ x(t) = 100s + (1 - 100s) e^{-t/100} $$

### Physical & Dimensional Checks:
1. **Dimensions:**
   * $[dx/dt] = \text{M}/\text{T} = \text{kg/min}$.
   * $[Q s] = (\text{L/min}) \cdot (\text{kg/L}) = \text{kg/min}$.
   * $[(Q/V) x] = (\text{min}^{-1}) \cdot \text{kg} = \text{kg/min}$. Homogeneous!
2. **Initial Condition Recovery:**
   At $t = 0$: $x(0) = s V + (x_0 - s V)(1) = x_0$. Satisfied identically.
3. **Physical Equilibrium:**
   As $t \to \infty$, the tank concentration completely forgets its initial state $x_0$ and aligns with the incoming fluid concentration $s$. If the incoming fluid has $s = 0.05\text{ kg/L}$, the tank ends up with exactly $100 \times 0.05 = 5\text{ kg}$ of salt.

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - First-Order Physical Models|First-Order Physical Models]]`
* `[[04 - Advanced Maths/Problema - Ch1-P4 Newton Law of Cooling Modeling|Problem 1.4: Thermal Relaxation Analogy]]`
