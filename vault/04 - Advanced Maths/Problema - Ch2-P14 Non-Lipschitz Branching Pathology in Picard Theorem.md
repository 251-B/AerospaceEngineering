---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.14"
dificultad: media
tags:
  - problema-resuelto
  - no-unicidad
  - teorema-picard
  - condicion-lipschitz
  - bifurcacion-soluciones
---

# ✏️ Problem 2.14: Non-Lipschitz Branching Pathology in Picard Theorem

## 📄 Enunciado (Problem Statement)

Given the initial value problem (IVP):
$$ \frac{dy}{dt} = 3 y^{2/3}, \quad y(0) = 0 $$
on the rectangle $R = \{ (y, t) \in \mathbb{R}^2 : |y| \le 1, \, |t| \le 1 \}$.

Show that both $y_1(t) = t^3$ and $y_2(t) = 0$ are solutions. Does this contradict Picard's theorem?

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Setting:
* **Differential Equation:** $\frac{dy}{dt} = f(t, y)$ with $f(t, y) = 3 y^{2/3}$.
* **Initial Condition:** $y(0) = 0$ at $t_0 = 0$.
* **Domain:** Closed compact rectangle $R = [-1, 1] \times [-1, 1] \subset \mathbb{R}^2$.
* **Proposed Candidate Solutions:**
  * Candidate 1: $y_1(t) = t^3$
  * Candidate 2: $y_2(t) \equiv 0$

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

1. Verify by direct substitution that both candidate functions $y_1(t)$ and $y_2(t)$ satisfy the differential equation and the initial condition on $[-1, 1]$.
2. Review the exact hypotheses required by the **Picard-Lindelöf Existence and Uniqueness Theorem**:
   * Hypothesis A: $f(t, y)$ must be continuous on $R$ (guarantees *existence* via Peano's Theorem).
   * Hypothesis B: $f(t, y)$ must be **Lipschitz continuous with respect to $y$** on $R$ (guarantees *uniqueness*).
3. Compute the partial derivative $\frac{\partial f}{\partial y}$ and evaluate its boundedness on $R$, particularly near $y = 0$.
4. Determine whether Picard's theorem applies. If its hypotheses are not satisfied, explain why the presence of multiple solutions does not constitute a contradiction.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Step 1: Verification of Candidate 2 ($y_2(t) \equiv 0$)
* **Initial Condition:**
  $$ y_2(0) = 0 \quad \checkmark $$
* **Derivative:**
  $$ \frac{dy_2}{dt} = \frac{d}{dt}[0] = 0 $$
* **Right-Hand Side:**
  $$ 3 [y_2(t)]^{2/3} = 3 [0]^{2/3} = 0 $$
Since $0 = 0$, $y_2(t) \equiv 0$ is a valid solution on $[-1, 1]$.

---

### Step 2: Verification of Candidate 1 ($y_1(t) = t^3$)
* **Initial Condition:**
  $$ y_1(0) = 0^3 = 0 \quad \checkmark $$
* **Derivative:**
  $$ \frac{dy_1}{dt} = \frac{d}{dt}\left[ t^3 \right] = 3 t^2 $$
* **Right-Hand Side:**
  $$ 3 [y_1(t)]^{2/3} = 3 \left[ t^3 \right]^{2/3} = 3 \left( t^3 \right)^{2/3} = 3 \left( t^{3 \cdot \frac{2}{3}} \right) = 3 t^2 $$
Because $\frac{dy_1}{dt} = 3t^2$ and the right-hand side is $3t^2$, they match identically for all $t \in [-1, 1]$.
Furthermore, for $t \in [-1, 1]$, $|y_1(t)| = |t^3| \le 1$, so the trajectory remains inside the rectangle $R$.
* **Conclusion:** Both $y_1(t)$ and $y_2(t)$ are valid solutions to the IVP on $R$.

---

### Step 3: Investigation of Picard's Theorem Hypotheses
The Picard-Lindelöf theorem states:
> If $f(t, y)$ is continuous on $R$ and satisfies a Lipschitz condition with respect to $y$ on $R$:
> $$ |f(t, y_a) - f(t, y_b)| \le L |y_a - y_b| \quad \forall (t, y_a), (t, y_b) \in R $$
> then there exists a **unique** solution to the IVP.

#### 1. Continuity Test:
$f(t, y) = 3 y^{2/3}$ is the composition of continuous functions, hence $f$ is continuous on the entire rectangle $R$. Peano's Theorem guarantees that **at least one solution exists**.

#### 2. Lipschitz Continuity Test:
Compute the partial derivative with respect to $y$:
$$ \frac{\partial f}{\partial y} = \frac{\partial}{\partial y}\left( 3 y^{2/3} \right) = 3 \cdot \frac{2}{3} y^{\frac{2}{3} - 1} = 2 y^{-1/3} = \frac{2}{y^{1/3}} \tag{1} $$

Evaluate the limit as $y$ approaches the initial value $y = 0$:
$$ \lim_{y \to 0^+} \frac{\partial f}{\partial y} = \lim_{y \to 0^+} \frac{2}{y^{1/3}} = +\infty $$
$$ \lim_{y \to 0^-} \frac{\partial f}{\partial y} = \lim_{y \to 0^-} \frac{2}{y^{1/3}} = -\infty $$

The derivative $\frac{\partial f}{\partial y}$ is **unbounded** in any neighborhood containing the initial point $y = 0$.

#### Direct Verification via the Difference Quotient:
Take $y_a = y$ and $y_b = 0$:
$$ \frac{|f(t, y) - f(t, 0)|}{|y - 0|} = \frac{|3 y^{2/3} - 0|}{|y|} = 3 \frac{|y|^{2/3}}{|y|} = \frac{3}{|y|^{1/3}} $$
As $y \to 0$:
$$ \lim_{y \to 0} \frac{|f(t, y) - f(t, 0)|}{|y - 0|} = \lim_{y \to 0} \frac{3}{|y|^{1/3}} = +\infty $$
There exists **no finite constant $L < \infty$** such that $|f(t, y) - f(t, 0)| \le L |y|$.
Therefore, $f(t, y)$ **violates the Lipschitz condition on $R$**.

---

### Step 4: Resolution of the Apparent Contradiction
* **Does this contradict Picard's Theorem?**
  **NO, it does not.**
* **Epistemological Reason:**
  Picard's theorem is an implication of the form:
  $$ \text{Continuity} + \text{Lipschitz Condition} \implies \text{Existence and Uniqueness} $$
  If the hypothesis (Lipschitz condition) is not satisfied, the theorem makes **no assertion whatsoever** about uniqueness. It does not state that uniqueness must fail; it simply cannot guarantee that uniqueness will hold.
  The coexistence of two solutions ($y_1(t) = t^3$ and $y_2(t) \equiv 0$) is entirely compatible with mathematical logic: when the Lipschitz premise fails, the conclusion of uniqueness is no longer assured.

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Final Answers:
1. **Verification:**
   * $y_1(t) = t^3 \implies y_1'(t) = 3t^2 = 3(t^3)^{2/3} \quad \checkmark$
   * $y_2(t) = 0 \implies y_2'(t) = 0 = 3(0)^{2/3} \quad \checkmark$
2. **Contradiction with Picard's Theorem:**
   **No contradiction exists.** Picard's theorem requires $f$ to be locally Lipschitz in $y$. Here:
   $$ \frac{\partial f}{\partial y} = \frac{2}{y^{1/3}} \to \infty \quad \text{as } y \to 0 $$
   Because the Lipschitz condition is violated at the initial point $(0, 0)$, Picard's theorem does not apply.

### Infinite Family of Branching Solutions:
In fact, the IVP possesses an **infinite continuum of solutions** indexed by an arbitrary branching time $c \in [0, 1]$:
$$ y_c(t) = \begin{cases} 0 & 0 \le t \le c \\ (t - c)^3 & c < t \le 1 \end{cases} $$
Every such function is continuously differentiable ($C^1$) and satisfies the IVP identically, demonstrating total loss of determinism at a non-Lipschitz singularity.

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Well-Posed Problems and Picard Theorem|Picard-Lindelöf Existence and Uniqueness Theory]]`
* `[[04 - Advanced Maths/Problema - Ch2-P9 Solution Uniqueness and Lipschitz Analysis|Problem 2.9: Lipschitz Analysis of Exponents]]`
