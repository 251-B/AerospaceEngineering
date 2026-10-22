---
materia: "Advanced Mathematics"
tema: "Tema 1: Introduction, Modeling and Classification of ODEs"
origen: "ProblemsCh1.pdf — Exercise 1.2"
dificultad: baja
tags:
  - problema-resuelto
  - malthus
  - edos-separables
  - dinamica-poblaciones
  - tiempo-duplicacion
---

# ✏️ Problem 1.2: Malthusian Population Dynamics

## 📄 Enunciado (Problem Statement)

Let $x(t)$ be the population of a certain species as a function of time, and suppose that the rate of change of this population is proportional to the existing population at each time, with constant of proportionality $k \in \mathbb{R}$.

(i) Write a differential equation for $x(t)$.  
(ii) Solve it, determine the behavior of $x(t)$ as $t \to \infty$ and interpret it depending on the sign of $k$.  
(iii) If the initial population is $x(0) = x_0$ and $k > 0$, determine the time needed for the population to double.

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Variables and Parameters:
* **Independent variable:** Time $t$ $[T]$ (e.g., seconds, hours, or years).
* **Dependent variable:** Population $x(t)$ $[N]$ (number of individuals or biomass).
* **Parameter:** Growth rate constant $k \in \mathbb{R}$ $[T^{-1}]$.
* **Initial condition:** $x(0) = x_0 > 0$ $[N]$.

### Modeling Hypotheses:
* [x] **Continuum approximation:** The discrete number of individuals is modeled as a continuous, differentiable function $x(t) \in C^1([0, \infty))$.
* [x] **Unconstrained environment:** Food, territory, and resources are abundant; mortality and natality rates remain constant over time.
* [x] **Homogeneous mixing:** Age distribution and spatial variations are neglected.

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

1. **Part (i):** Translate the verbal statement *"rate of change is proportional to the existing population"* directly into differential calculus:
   $$ \frac{dx}{dt} \propto x(t) \implies \frac{dx}{dt} = k x(t) $$
2. **Part (ii):** The equation is a first-order, separable, linear homogeneous ODE. Separate variables, integrate with respect to initial condition $x(0) = x_0$, and take the limit as $t \to \infty$ for the three cases: $k > 0$, $k = 0$, and $k < 0$.
3. **Part (iii):** Define the doubling time $t_d$ by the condition $x(t_d) = 2x_0$, equate to the analytical solution, and solve for $t_d$ using natural logarithms.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Part (i): Formulation of the Differential Equation
The verbal hypothesis states that the instantaneous rate of change $\frac{dx}{dt}$ is proportional to $x(t)$ with proportionality factor $k$:

$$ \mathbf{\frac{dx}{dt} = k x(t)} \tag{1} $$

This is an autonomous, 1st-order linear ODE.

---

### Part (ii): Analytical Solution and Asymptotic Behavior
Method of the class notes [Notes.pdf, p. 2]. The population is positive, $x(t) > 0$, so divide by it, $\frac{x'(\tau)}{x(\tau)} = k$, and integrate both sides from $0$ to $t$:
$$ \int_0^t \frac{x'(\tau)}{x(\tau)}\,d\tau = \int_0^t k\,d\tau \tag{2} $$

*Left side.* Substitute $u = x(\tau)$, $du = x'(\tau)\,d\tau$; the limits $\tau = 0$, $\tau = t$ become $u = x_0$, $u = x(t)$. An antiderivative of $1/u$ ($u > 0$) is $\ln u$, so by Barrow's rule
$$ \int_{x_0}^{x(t)}\frac{du}{u} = \big[\ln u\big]_{x_0}^{x(t)} = \ln x(t) - \ln x_0 = \ln\left(\frac{x(t)}{x_0}\right). $$
(Second route of the notes: by the chain rule $\frac{d}{d\tau}\ln x(\tau) = \frac{x'(\tau)}{x(\tau)}$, so the integrand is $(\ln x(\tau))'$.) *Right side.* $\int_0^t k\,d\tau = [k\tau]_0^t = kt$. Hence
$$ \ln\left( \frac{x}{x_0} \right) = k t $$

Apply the exponential function $\exp(\cdot)$ to both sides:
$$ \exp\left( \ln\left( \frac{x}{x_0} \right) \right) = \exp(k t) $$
$$ \frac{x(t)}{x_0} = e^{kt} $$
Multiplying by $x_0$:
$$ \mathbf{x(t) = x_0 e^{kt}} \tag{3} $$

#### Asymptotic Analysis as $t \to \infty$:
We evaluate $\lim_{t \to \infty} x(t) = \lim_{t \to \infty} x_0 e^{kt}$ according to the sign of $k$ (the notes: "if $k > 0$ population increases, if $k < 0$ it decreases"; the case $k = 0$ is added here):

1. **Case $k > 0$ (Supercritical / Net Positive Growth):**
   $$ \lim_{t \to \infty} x_0 e^{kt} = x_0 \lim_{t \to \infty} e^{kt} = +\infty $$
   *Interpretation:* **Exponential explosion**. The birth rate exceeds the death rate ($\beta > \delta$). In an unconstrained environment, the population grows without bound.
2. **Case $k = 0$ (Critical / Perfect Equilibrium):**
   $$ x(t) = x_0 e^{0} = x_0 \quad \forall t \ge 0 $$
   *Interpretation:* **Stationary population**. Natality and mortality are precisely balanced ($\beta = \delta$), leaving the population constant.
3. **Case $k < 0$ (Subcritical / Net Decay):**
   Writing $k = -|k|$:
   $$ \lim_{t \to \infty} x_0 e^{-|k|t} = 0 $$
   *Interpretation:* **Exponential extinction**. Death rate exceeds birth rate ($\delta > \beta$), asymptotically driving the species to extinction.

---

### Part (iii): Doubling Time Calculation
Let $t_d$ be the doubling time, defined such that:
$$ x(t_d) = 2 x_0 $$

Substitute $t = t_d$ into the analytical solution $(3)$:
$$ x_0 e^{k t_d} = 2 x_0 $$

Since $x_0 > 0$, divide both sides by $x_0$:
$$ e^{k t_d} = 2 $$

Take the natural logarithm of both sides:
$$ \ln(e^{k t_d}) = \ln(2) $$
$$ k t_d = \ln(2) $$

Since $k > 0$, divide by $k$:
$$ \mathbf{t_d = \frac{\ln(2)}{k}} \tag{4} $$

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Final Answers:
* **(i) Differential Equation:**
  $$ \frac{dx}{dt} = k x $$
* **(ii) General Solution & Asymptotics:**
  $$ x(t) = x_0 e^{kt} $$
  $$ \lim_{t \to \infty} x(t) = \begin{cases} +\infty & \text{if } k > 0 \\ x_0 & \text{if } k = 0 \\ 0 & \text{if } k < 0 \end{cases} $$
* **(iii) Doubling Time:**
  $$ \mathbf{t_d = \frac{\ln 2}{k} \approx \frac{0.69315}{k}} $$

### Verification & Physical Critique:
1. **Dimensional Consistency:**
   * $[x] = N$, $[t] = T \implies [dx/dt] = N/T$.
   * $[kx] = [k][x] = (1/T) \cdot N = N/T$. Consistent!
   * $[t_d] = [\ln 2] / [k] = 1 / (1/T) = T$. Consistent!
2. **Independence of Initial Population:**
   The doubling time $t_d$ depends strictly on the growth rate $k$ and is entirely **independent of the initial population size $x_0$**. Whether the colony starts with 10 or $10^6$ organisms, doubling requires the exact same duration.
3. **Physical Limitation:**
   As $t \to \infty$, $x(t) \to \infty$ violates physical reality because finite physical space and nutrient resources impose a carrying capacity. This necessitates the **logistic model** developed in [[04 - Advanced Maths/Problem - Ch1-P9 Logistic Population Growth Model|Problem 1.9]].

---

## 🔗 Related Notes
* [[04 - Advanced Maths/Concept - First-Order Physical Models|First-Order Physical Models]]
* [[04 - Advanced Maths/Concept - Logistic Equation and Carrying Capacity|Logistic Equation and Carrying Capacity]]
* [[04 - Advanced Maths/Problem - Ch1-P3 Plutonium 239 Radioactive Decay|Problem 1.3: Radioactive Decay Constant]]
* [[04 - Advanced Maths/Problem - Ch1-P9 Logistic Population Growth Model|Problem 1.9: Logistic Growth Model]]
