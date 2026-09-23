---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.15"
dificultad: media
tags:
  - problema-resuelto
  - singularidad-dominio
  - teorema-unicidad
  - infinitas-soluciones
  - edos-separables
---

# ✏️ Problem 2.15: Singular ODE and Domain of Definition

## 📄 Enunciado (Problem Statement)

Consider the differential equation:
$$ \frac{dy}{dt} = \frac{2y + 1}{t} $$
Compute the general solution and show that there are two solutions such that $y(0) = -1/2$. Does this contradict the uniqueness theorem?

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Setting:
* **Differential Equation:** $\frac{dy}{dt} = f(t, y)$ where $f(t, y) = \frac{2y + 1}{t}$.
* **Initial Condition:** $y(0) = -\frac{1}{2}$ at the initial point $(t_0, y_0) = \left(0, -\frac{1}{2}\right)$.
* **Domain of Definition:** The function $f(t, y)$ is undefined on the vertical line $t = 0$ due to division by zero. The natural domain of definition is $D = \{ (t, y) \in \mathbb{R}^2 : t \neq 0 \}$.

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

1. Solve the first-order ODE for $t \neq 0$ using separation of variables or an integrating factor.
2. Note the equilibrium constant solution $2y + 1 = 0 \implies y(t) \equiv -\frac{1}{2}$.
3. Express the full family of general solutions in terms of an arbitrary parameter $C \in \mathbb{R}$.
4. Evaluate the limit of the solution family as $t \to 0$ to demonstrate that *infinitely many* distinct curves pass through $\left(0, -\frac{1}{2}\right)$.
5. Re-examine the hypotheses of the Picard-Lindelöf Existence and Uniqueness Theorem:
   * Picard requires $f(t, y)$ and $\frac{\partial f}{\partial y}$ to be **continuous in an open neighborhood** containing the initial point $(t_0, y_0)$.
   * Because $t_0 = 0$ is a coordinate singularity where $f(t, y)$ is not even defined, the hypotheses are completely violated, and no contradiction exists.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Step 1: Solution via Separation of Variables
Starting from:
$$ \frac{dy}{dt} = \frac{2y + 1}{t} \tag{1} $$

Assuming $2y + 1 \neq 0$ and $t \neq 0$, separate variables:
$$ \frac{1}{2y + 1} \, dy = \frac{1}{t} \, dt \tag{2} $$

Integrate both sides:
$$ \int \frac{1}{2y + 1} \, dy = \int \frac{1}{t} \, dt $$

On the left-hand side, substitute $u = 2y + 1 \implies du = 2 dy \implies dy = \frac{1}{2} du$:
$$ \frac{1}{2} \int \frac{du}{u} = \int \frac{dt}{t} $$
$$ \frac{1}{2} \ln|2y + 1| = \ln|t| + C_0 $$

Multiply the entire equation by $2$:
$$ \ln|2y + 1| = 2\ln|t| + 2C_0 = \ln(t^2) + C_1 $$
where $C_1 = 2C_0$.

Exponentiate both sides:
$$ |2y + 1| = \exp(\ln(t^2) + C_1) = e^{C_1} t^2 $$
$$ 2y + 1 = \pm e^{C_1} t^2 = C t^2 $$
where $C \in \mathbb{R} \setminus \{0\}$.

Including the singular equilibrium solution $2y + 1 = 0 \iff y(t) \equiv -\frac{1}{2}$ corresponds to setting $C = 0$.
Isolate $y(t)$:
$$ 2y(t) = -1 + C t^2 \implies \mathbf{y(t) = -\frac{1}{2} + \frac{C}{2} t^2} $$
Absorbing the factor $1/2$ into the arbitrary constant $k = C/2 \in \mathbb{R}$:
$$ \mathbf{y(t) = -\frac{1}{2} + k t^2, \quad k \in \mathbb{R}} \tag{3} $$

---

### Step 2: Verification of the Initial Condition $y(0) = -1/2$
Evaluate the general solution $(3)$ at $t = 0$:
$$ y(0) = -\frac{1}{2} + k(0)^2 = -\frac{1}{2} + 0 = -\frac{1}{2} $$
Remarkably, this equality holds **for EVERY real choice of $k$**!

#### Selecting Two Explicit Distinct Solutions:
* For $k = 0$:
  $$ y_1(t) \equiv -\frac{1}{2} $$
  *Check ODE:* $y_1' = 0$, and $\frac{2(-1/2) + 1}{t} = \frac{0}{t} = 0 \quad \checkmark$
* For $k = 1$:
  $$ y_2(t) = -\frac{1}{2} + t^2 $$
  *Check ODE:* $y_2' = 2t$, and $\frac{2(-1/2 + t^2) + 1}{t} = \frac{-1 + 2t^2 + 1}{t} = \frac{2t^2}{t} = 2t \quad \checkmark$

Both $y_1(t)$ and $y_2(t)$ are $C^1$ functions on $\mathbb{R}$, satisfy $y_1(0) = y_2(0) = -\frac{1}{2}$, and satisfy the differential equation for all $t \neq 0$ (and in the limit as $t \to 0$).

---

### Step 3: Analysis of the Uniqueness Theorem
* **Does this contradict the Uniqueness Theorem?**
  **NO, it does not.**

#### Formal Mathematical Explanation:
The Picard-Lindelöf Existence and Uniqueness Theorem states:
> If the function $f(t, y)$ and its partial derivative $\frac{\partial f}{\partial y}$ are continuous on an open domain $D \subseteq \mathbb{R}^2$ containing the point $(t_0, y_0)$, then there exists an interval around $t_0$ on which the IVP has a unique solution.

Let us inspect the vector field:
$$ f(t, y) = \frac{2y + 1}{t} $$
The initial condition is specified at $t_0 = 0$.
However, the function $f(t, y)$ **is not defined at $t = 0$**, because division by zero is undefined in $\mathbb{R}$.

Consequently:
1. There exists **no open neighborhood** or rectangle $R$ around $(0, -1/2)$ on which $f(t, y)$ is defined, let alone continuous.
2. The initial point $(0, -1/2)$ lies completely outside the domain of definition of the differential equation ($t_0 \notin \text{Domain}(f)$).
3. The point $t = 0$ is a **singular point** of the differential equation.

Because the very first hypothesis of the Picard-Lindelöf Theorem (continuity on an open neighborhood of the initial point) fails catastrophically, the theorem simply **does not apply**. Therefore, having multiple (indeed, an infinite family of) solutions passing through $(0, -1/2)$ does not contradict any mathematical theorem.

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Master Summary:
* **General Solution:**
  $$ \mathbf{y(t) = -\frac{1}{2} + k t^2, \quad k \in \mathbb{R}} $$
* **Coexistence of Solutions at $t = 0$:**
  $$ y_1(t) = -\frac{1}{2} \quad \text{and} \quad y_2(t) = -\frac{1}{2} + t^2 $$
  both satisfy $y(0) = -1/2$.
* **Uniqueness Theorem Verdict:**
  **No contradiction.** The initial value is prescribed at $t = 0$, which is a **domain singularity** where $f(t, y)$ is undefined. The Picard-Lindelöf theorem requires continuity in an open neighborhood around $(t_0, y_0)$, which fails completely at $t_0 = 0$.

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Well-Posed Problems and Picard Theorem|Picard-Lindelöf Theorem and Singularities]]`
* `[[04 - Advanced Maths/Problema - Ch2-P14 Non-Lipschitz Branching Pathology in Picard Theorem|Problem 2.14: Non-Lipschitz Branching]]`
