---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.2"
dificultad: alta
tags:
  - problema-resuelto
  - ecuaciones-separables
  - integral-gaussiana
  - blow-up
  - comportamiento-asintotico
---

# ✏️ Problem 2.2: Separable ODEs and Asymptotic Integrals

## 📄 Enunciado (Problem Statement)

Solve the following equations:

(i) $\dot{x} = t^3 (1 - x)$ with $x(0) = 3$  
(ii) $y' = (1 + y^2) \tan x$ with $y(0) = 1$  
(iii) $\dot{x} = t^2 x$ (general solution)  
(iv) $\dot{x} = -x^2$ (general solution)  
(v) $\frac{dy}{dt} = e^{-t^2} y^2$; give the solution in terms of an integral and describe the behavior as $t \to \infty$ depending on the initial condition $y(0)$. Use that:
$$ \int_0^\infty e^{-s^2} \, ds = \frac{\sqrt{\pi}}{2} $$

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Structure:
All five differential equations are **first-order separable ODEs** of the form:
$$ \frac{dx}{dt} = g(t) h(x) \quad \text{or} \quad \frac{dy}{dx} = g(x) h(y) $$

### Initial Conditions & Specific Parameters:
* (i) $x(0) = 3$, $g(t) = t^3$, $h(x) = 1 - x$. Equilibrium at $x = 1$.
* (ii) $y(0) = 1$, $g(x) = \tan x$, $h(y) = 1 + y^2 > 0$ (no real equilibrium roots).
* (iii) General solution, $g(t) = t^2$, $h(x) = x$. Equilibrium at $x = 0$.
* (iv) General solution, $g(t) = -1$, $h(x) = x^2$. Equilibrium at $x = 0$.
* (v) Initial condition $y(0) = y_0$, $g(t) = e^{-t^2}$, $h(y) = y^2$. Equilibrium at $y = 0$. Known Gaussian integral $\int_0^\infty e^{-s^2} ds = \frac{\sqrt{\pi}}{2}$.

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

1. For items (i)–(iv), identify any equilibrium solutions $h(x^*) = 0$. For non-equilibrium trajectories, divide by $h(x)$ and integrate both sides directly. Apply the initial conditions where prescribed.
2. For item (v):
   * Note the equilibrium solution $y_0 = 0 \implies y(t) \equiv 0$.
   * For $y_0 \neq 0$, separate variables and integrate over $[0, t]$ using definite integrals.
   * Express the solution analytically in terms of $I(t) = \int_0^t e^{-s^2} ds$.
   * Analyze the root of the denominator $1 - y_0 I(t) = 0$ as $t \to \infty$ to identify the critical blow-up threshold $y_0^* = \frac{2}{\sqrt{\pi}}$.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Part (i): $\dot{x} = t^3 (1 - x)$, $x(0) = 3$

#### Step 1: Separation of Variables
Notice $x = 1$ is an equilibrium solution. For $x \neq 1$:
$$ \frac{1}{1 - x} \, dx = t^3 \, dt $$

#### Step 2: Definite Integration
Integrate from $t = 0$ ($x = 3$) to $t$ ($x = x(t)$):
$$ \int_3^{x(t)} \frac{1}{1 - u} \, du = \int_0^t s^3 \, ds $$
$$ \left[ -\ln|1 - u| \right]_3^{x(t)} = \left[ \frac{s^4}{4} \right]_0^t $$
$$ -\ln|1 - x(t)| - (-\ln|1 - 3|) = \frac{t^4}{4} $$
$$ -\ln|1 - x(t)| + \ln(2) = \frac{t^4}{4} $$
$$ \ln|1 - x(t)| = \ln(2) - \frac{t^4}{4} $$

#### Step 3: Inversion and Sign Determination
Exponentiate both sides:
$$ |1 - x(t)| = \exp\left( \ln(2) - \frac{t^4}{4} \right) = 2 e^{-t^4/4} $$
Since $x(0) = 3 > 1$, by continuity $x(t) > 1$ for all $t$. Thus $|1 - x| = -(1 - x) = x - 1$:
$$ x(t) - 1 = 2 e^{-t^4/4} $$
$$ \mathbf{x(t) = 1 + 2 e^{-t^4/4}} \tag{1} $$

---

### Part (ii): $y' = (1 + y^2) \tan x$, $y(0) = 1$

#### Step 1: Separation of Variables
Since $1 + y^2 \ge 1 > 0$, divide by $1 + y^2$:
$$ \frac{1}{1 + y^2} \, dy = \tan x \, dx = \frac{\sin x}{\cos x} \, dx $$

#### Step 2: Definite Integration
Integrate from $x = 0$ ($y = 1$) to $x$ ($y = y(x)$):
$$ \int_1^{y(x)} \frac{1}{1 + u^2} \, du = \int_0^x \frac{\sin s}{\cos s} \, ds $$
$$ [\arctan u]_1^{y(x)} = [-\ln|\cos s|]_0^x $$
$$ \arctan(y(x)) - \arctan(1) = -\ln|\cos x| - (-\ln|\cos 0|) $$
Recall $\arctan(1) = \frac{\pi}{4}$ and $\cos(0) = 1 \implies \ln(1) = 0$:
$$ \arctan(y(x)) - \frac{\pi}{4} = -\ln|\cos x| = \ln|\sec x| $$
$$ \arctan(y(x)) = \frac{\pi}{4} - \ln|\cos x| $$

#### Step 3: Inversion
Take the tangent of both sides:
$$ \mathbf{y(x) = \tan\left( \frac{\pi}{4} - \ln|\cos x| \right)} \tag{2} $$

---

### Part (iii): $\dot{x} = t^2 x$ (General Solution)

#### Step 1: Equilibrium Solution
If $x = 0$, $\dot{x} = 0$, so $\mathbf{x(t) \equiv 0}$ is a solution.

#### Step 2: Separation of Variables for $x \neq 0$
$$ \frac{1}{x} \, dx = t^2 \, dt \implies \int \frac{1}{x} \, dx = \int t^2 \, dt $$
$$ \ln|x| = \frac{t^3}{3} + C_1 $$
Exponentiate both sides:
$$ |x(t)| = e^{C_1} e^{t^3/3} \implies x(t) = \pm e^{C_1} e^{t^3/3} $$
Let $C = \pm e^{C_1} \in \mathbb{R} \setminus \{0\}$. Including the equilibrium solution $x \equiv 0$ corresponds to $C = 0$:
$$ \mathbf{x(t) = C e^{t^3/3}, \quad C \in \mathbb{R}} \tag{3} $$

---

### Part (iv): $\dot{x} = -x^2$ (General Solution)

#### Step 1: Equilibrium Solution
$x = 0 \implies \dot{x} = 0$, so $\mathbf{x(t) \equiv 0}$ is a stationary solution.

#### Step 2: Separation of Variables for $x \neq 0$
$$ -\frac{1}{x^2} \, dx = dt \implies \int -x^{-2} \, dx = \int dt $$
$$ \frac{1}{x(t)} = t + C $$
Invert both sides:
$$ \mathbf{x(t) = \frac{1}{t + C}, \quad C \in \mathbb{R}} \quad \text{together with} \quad \mathbf{x(t) \equiv 0} \tag{4} $$

---

### Part (v): $\frac{dy}{dt} = e^{-t^2} y^2$ (Asymptotic & Blow-Up Analysis)

#### Step 1: Equilibrium Case
If $y(0) = 0$, then $\mathbf{y(t) \equiv 0}$ for all $t \ge 0$.

#### Step 2: General IVP Integration for $y(0) = y_0 \neq 0$
Separate variables and integrate from $s = 0$ to $s = t$:
$$ \int_{y_0}^{y(t)} \frac{du}{u^2} = \int_0^t e^{-s^2} \, ds $$
$$ \left[ -\frac{1}{u} \right]_{y_0}^{y(t)} = \int_0^t e^{-s^2} \, ds $$
$$ -\frac{1}{y(t)} + \frac{1}{y_0} = \int_0^t e^{-s^2} \, ds $$
Isolate $\frac{1}{y(t)}$:
$$ \frac{1}{y(t)} = \frac{1}{y_0} - \int_0^t e^{-s^2} \, ds = \frac{1 - y_0 \int_0^t e^{-s^2} \, ds}{y_0} $$
Inverting yields the exact analytical solution:
$$ \mathbf{y(t) = \frac{y_0}{1 - y_0 \int_0^t e^{-s^2} \, ds}} \tag{5} $$

#### Step 3: Asymptotic Behavior as $t \to \infty$
Define the Gaussian integral function:
$$ I(t) \equiv \int_0^t e^{-s^2} \, ds $$
$I(t)$ is strictly increasing for $t \ge 0$, with:
$$ I(0) = 0, \quad \lim_{t \to \infty} I(t) = \int_0^\infty e^{-s^2} \, ds = \frac{\sqrt{\pi}}{2} \approx 0.8862 $$
Therefore, for all $t \in [0, \infty)$:
$$ 0 \le I(t) < \frac{\sqrt{\pi}}{2} $$

We analyze the denominator $D(t) = 1 - y_0 I(t)$ according to the value of $y_0$:

1. **Subcritical Case 1 ($y_0 \le 0$):**
   * If $y_0 = 0$: $y(t) \equiv 0$.
   * If $y_0 < 0$: $-y_0 > 0$, so $D(t) = 1 + |y_0| I(t) \ge 1 > 0$ for all $t \ge 0$. The denominator never vanishes. The solution exists globally for all $t \ge 0$.
   * Asymptotic limit:
     $$ \lim_{t \to \infty} y(t) = \frac{y_0}{1 - y_0 \frac{\sqrt{\pi}}{2}} < 0 $$
2. **Subcritical Case 2 ($0 < y_0 < \frac{2}{\sqrt{\pi}}$):**
   * Since $y_0 < \frac{2}{\sqrt{\pi}}$, we have $y_0 I(t) < y_0 \frac{\sqrt{\pi}}{2} < 1$ for all $t \ge 0$.
   * Hence $D(t) = 1 - y_0 I(t) > 1 - y_0 \frac{\sqrt{\pi}}{2} > 0$ is strictly positive for all $t \ge 0$. No blow-up occurs!
   * The solution exists globally for all $t \ge 0$, and as $t \to \infty$:
     $$ \lim_{t \to \infty} y(t) = \frac{y_0}{1 - y_0 \frac{\sqrt{\pi}}{2}} \in (0, \infty) $$
3. **Critical Case ($y_0 = \frac{2}{\sqrt{\pi}}$):**
   * The denominator is $D(t) = 1 - \frac{2}{\sqrt{\pi}} I(t) > 0$ for every finite $t < \infty$, but approaches $0$ as $t \to \infty$.
   * The solution exists for all finite $t \in [0, \infty)$, and blows up at infinity:
     $$ \lim_{t \to \infty} y(t) = +\infty $$
4. **Supercritical Blow-Up Case ($y_0 > \frac{2}{\sqrt{\pi}}$):**
   * Since $\frac{1}{y_0} < \frac{\sqrt{\pi}}{2}$, by the Intermediate Value Theorem there exists a unique **finite blow-up time $t^* > 0$** such that:
     $$ \int_0^{t^*} e^{-s^2} \, ds = \frac{1}{y_0} $$
   * As $t \to t^{*-}$, the denominator $D(t) \to 0^+$, resulting in **finite-time blow-up**:
     $$ \lim_{t \to t^{*-}} y(t) = +\infty $$
   * The solution ceases to exist for $t \ge t^*$.

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Summary of Solutions:
* **(i)** $x(t) = 1 + 2 e^{-t^4/4}$ (decays asymptotically to the equilibrium $x = 1$).
* **(ii)** $y(x) = \tan\left( \frac{\pi}{4} - \ln|\cos x| \right)$.
* **(iii)** $x(t) = C e^{t^3/3}, \quad C \in \mathbb{R}$.
* **(iv)** $x(t) = \frac{1}{t + C}$ and $x(t) \equiv 0$.
* **(v)** Exact solution:
  $$ \mathbf{y(t) = \frac{y_0}{1 - y_0 \int_0^t e^{-s^2} \, ds}} $$
  * **If $y_0 < \frac{2}{\sqrt{\pi}}$:** Global existence, saturates at $\mathbf{y_\infty = \frac{y_0}{1 - y_0 \frac{\sqrt{\pi}}{2}}}$.
  * **If $y_0 = \frac{2}{\sqrt{\pi}}$:** Global existence for finite $t$, $\mathbf{\lim_{t\to\infty} y(t) = +\infty}$.
  * **If $y_0 > \frac{2}{\sqrt{\pi}}$:** **Finite-time blow-up** at $t^*$ where $\int_0^{t^*} e^{-s^2} ds = \frac{1}{y_0}$.

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Metodos de Integracion Directa y Ecuaciones Separables|Separable Equations and Blow-up Theory]]`
* `[[04 - Advanced Maths/Concepto - Well-Posed Problems and Picard Theorem|Picard Theorem: Local vs. Global Existence]]`
