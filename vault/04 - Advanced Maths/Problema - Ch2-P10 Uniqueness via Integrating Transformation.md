---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.10"
dificultad: media
tags:
  - problema-resuelto
  - demostracion-unicidad
  - transformacion-integrante
  - sin-picard
  - pvi-lineal
---

# ✏️ Problem 2.10: Uniqueness via Integrating Transformation

## 📄 Enunciado (Problem Statement)

Without using Picard's theorem, show that the initial value problem (IVP):
$$ \frac{dy}{dt} + p(t) y = 0, \quad y(t_0) = y_0 $$
with $p(t)$ a continuous function, has a unique solution, and calculate it. What solution do we obtain if $y_0 = 0$?

*Hint:* Consider the function:
$$ z(t) = y(t) \exp\left( \int_{t_0}^t p(s) \, ds \right) $$
where $y(t)$ solves the IVP; show that $z(t)$ is constant and deduce $y(t)$.

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Setting:
* **Differential Equation:** $\frac{dy}{dt} + p(t) y(t) = 0$ (first-order linear homogeneous ODE).
* **Initial Condition:** $y(t_0) = y_0 \in \mathbb{R}$.
* **Hypothesis on Coefficient:** $p: I \to \mathbb{R}$ is continuous on an open interval $I$ containing $t_0$.
* **Constraint:** Picard's theorem must **not** be invoked. Uniqueness must be established strictly from first principles of single-variable differential calculus.

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

1. Let $y(t)$ be an *arbitrary* continuously differentiable function satisfying the IVP.
2. Define the auxiliary transformed function:
   $$ z(t) \equiv y(t) \exp\left( \int_{t_0}^t p(s) \, ds \right) $$
3. Differentiate $z(t)$ with respect to time $t$ using the product rule and the Fundamental Theorem of Calculus.
4. Exploit the differential equation $y' + p(t)y = 0$ to prove that $z'(t) \equiv 0$ on all of $I$.
5. A basic theorem of calculus states that any function with an identically zero derivative on an interval is constant: $z(t) \equiv C$.
6. Evaluate $C$ at $t = t_0$ to determine $y(t)$ uniquely.
7. Conclude that any solution must be identically equal to this formula, proving existence and uniqueness simultaneously.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Step 1: Definition of the Transformed Function
Let $y(t) \in C^1(I)$ be any solution to the initial value problem:
$$ \begin{cases} y'(t) + p(t) y(t) = 0 \\ y(t_0) = y_0 \end{cases} \tag{1} $$

Define the auxiliary function:
$$ z(t) = y(t) \Phi(t) \tag{2} $$
where:
$$ \Phi(t) \equiv \exp\left( \int_{t_0}^t p(s) \, ds \right) \tag{3} $$
Note that because the exponential function is strictly positive, $\Phi(t) > 0$ for all $t \in I$.

---

### Step 2: Differentiation of the Integrating Factor $\Phi(t)$
By the Fundamental Theorem of Calculus, since $p(s)$ is continuous:
$$ \frac{d}{dt} \left[ \int_{t_0}^t p(s) \, ds \right] = p(t) $$

Applying the chain rule to $\Phi(t) = e^{u(t)}$ with $u(t) = \int_{t_0}^t p(s) ds$:
$$ \frac{d\Phi}{dt} = \frac{d}{dt}\left[ e^{u(t)} \right] = u'(t) e^{u(t)} = p(t) \exp\left( \int_{t_0}^t p(s) \, ds \right) = p(t) \Phi(t) \tag{4} $$

---

### Step 3: Differentiation of $z(t)$
Differentiating $z(t) = y(t) \Phi(t)$ with respect to $t$ via the product rule:
$$ \frac{dz}{dt} = \frac{dy}{dt} \Phi(t) + y(t) \frac{d\Phi}{dt} $$

Substitute the derivative of $\Phi(t)$ from equation $(4)$:
$$ \frac{dz}{dt} = y'(t) \Phi(t) + y(t) \left[ p(t) \Phi(t) \right] $$

Factor out $\Phi(t)$:
$$ \frac{dz}{dt} = \left[ y'(t) + p(t) y(t) \right] \Phi(t) \tag{5} $$

---

### Step 4: Vanishing of the Derivative
From the differential equation $(1)$, $y(t)$ satisfies $y'(t) + p(t) y(t) = 0$ for all $t \in I$. Substituting this into $(5)$:
$$ \frac{dz}{dt} = [0] \cdot \Phi(t) = 0 \quad \forall t \in I \tag{6} $$

---

### Step 5: Deduction of Constancy
By the **Mean Value Theorem**, if a differentiable function on an interval $I$ has zero derivative everywhere on $I$, it is identically constant:
$$ z(t) \equiv C \quad \forall t \in I \tag{7} $$
where $C \in \mathbb{R}$ is a constant.

To evaluate $C$, evaluate equation $(2)$ at the initial time $t = t_0$:
$$ z(t_0) = y(t_0) \exp\left( \int_{t_0}^{t_0} p(s) \, ds \right) $$
Since $\int_{t_0}^{t_0} p(s) ds = 0$ and $e^0 = 1$:
$$ z(t_0) = y_0 \cdot 1 = y_0 $$

Therefore, the constant is uniquely determined:
$$ C = y_0 \implies z(t) = y_0 \quad \forall t \in I \tag{8} $$

---

### Step 6: Isolation of $y(t)$ and Uniqueness Proof
Substitute $z(t) = y_0$ back into equation $(2)$:
$$ y_0 = y(t) \exp\left( \int_{t_0}^t p(s) \, ds \right) $$

Since the exponential term is non-zero, divide both sides by $\exp\left(\int_{t_0}^t p(s) ds\right)$:
$$ \mathbf{y(t) = y_0 \exp\left( -\int_{t_0}^t p(s) \, ds \right)} \tag{9} $$

#### Rigorous Uniqueness Conclusion:
We did not assume what $y(t)$ looked like; we only assumed that $y(t)$ was *some* solution to $(1)$. The derivation proves that **any** solution $y(t)$ must necessarily and inescapably satisfy formula $(9)$.
Because the right-hand side of $(9)$ is uniquely defined for any given $y_0$, there is **at most one solution**. Since direct substitution verifies that $(9)$ indeed solves $(1)$, this establishes **existence and uniqueness** simultaneously without Picard's theorem. $\blacksquare$

---

### Step 7: Case $y_0 = 0$
If the initial condition is $y(t_0) = 0$:
$$ y(t) = 0 \cdot \exp\left( -\int_{t_0}^t p(s) \, ds \right) \equiv 0 \quad \forall t \in I $$
* **Conclusion:** If $y_0 = 0$, the only solution is the **trivial zero solution**:
  $$ \mathbf{y(t) \equiv 0} $$
  A linear homogeneous system released from rest remains identically at rest.

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Master Solution Summary:
* **Explicit Unique Solution:**
  $$ \mathbf{y(t) = y_0 \exp\left( -\int_{t_0}^t p(s) \, ds \right)} $$
* **Case $y_0 = 0$:**
  $$ \mathbf{y(t) \equiv 0} $$
* **Methodological Significance:** This proof demonstrates that for linear first-order differential equations, the **Fundamental Theorem of Calculus and the Mean Value Theorem** alone are sufficient to establish global existence and uniqueness, circumventing the need for the Picard-Lindelöf contraction mapping machinery.

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Factor Integrante y Ecuaciones Lineales de Primer Orden|Integrating Factor Theory]]`
* `[[04 - Advanced Maths/Problema - Ch2-P11 Invariance of Solution Ratios in Linear ODEs|Problem 2.11: Solution Ratios Invariance]]`
* `[[04 - Advanced Maths/Problema - Ch2-P17 Direct Difference Method for Uniqueness|Problem 2.17: Direct Difference Method]]`
