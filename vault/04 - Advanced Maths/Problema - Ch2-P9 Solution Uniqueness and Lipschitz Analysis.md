---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.9"
dificultad: media
tags:
  - problema-resuelto
  - teorema-picard
  - condicion-lipschitz
  - unicidad
  - no-unicidad
---

# ✏️ Problem 2.9: Solution Uniqueness and Lipschitz Analysis

## 📄 Enunciado (Problem Statement)

Which of the following differential equations have unique solutions (at least on some small time interval) for any non-negative initial condition $x(0) \ge 0$?

(i) $\dot{x} = x(1 - x^2)$  
(ii) $\dot{x} = x^3$  
(iii) $\dot{x} = x^{1/3}$  
(iv) $\dot{x} = x^{1/2}(1 + x)^2$  
(v) $\dot{x} = (1 + x)^{3/2}$

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Setting:
We consider autonomous Initial Value Problems (IVPs):
$$ \begin{cases} \dot{x} = f(x) \\ x(0) = x_0 \ge 0 \end{cases} $$
where the initial condition $x_0$ can be any non-negative real number in $[0, \infty)$.

### The Picard-Lindelöf Criterion for Uniqueness:
By the **Picard-Lindelöf Theorem**, the IVP has a unique local solution on an interval $(-\delta, \delta)$ if the function $f(x)$ is continuous and satisfies a **local Lipschitz condition** with respect to $x$ in a neighborhood of $x_0$:
$$ |f(x_1) - f(x_2)| \le L |x_1 - x_2| $$
A sufficient and practically necessary condition for $C^1$ functions on open sets is that the derivative $f'(x)$ is **bounded**:
$$ |f'(x)| \le L < \infty $$

### Crucial Observation on the Test Domain:
For strictly positive initial states $x_0 > 0$, all five candidate functions are smooth ($C^1$ or $C^\infty$) on $(0, \infty)$. Therefore, local uniqueness can only fail at the boundary point **$x_0 = 0$**.

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

For each equation $\dot{x} = f(x)$:
1. Verify continuity of $f(x)$ on $[0, \infty)$ (guarantees *existence* by Peano's Theorem).
2. Compute the derivative $f'(x) = \frac{df}{dx}$.
3. Evaluate the behavior of $f'(x)$ as $x \to 0^+$.
   * If $\lim_{x \to 0^+} |f'(x)| < \infty$, the derivative is bounded in a neighborhood of $x_0 = 0$, guaranteeing **local uniqueness**.
   * If $\lim_{x \to 0^+} |f'(x)| = +\infty$, the Lipschitz condition fails at the origin, allowing **branching non-uniqueness** where both the trivial solution $x(t) \equiv 0$ and non-trivial solutions coexist.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Part (i): $\dot{x} = x(1 - x^2)$
* **Vector Field:** $f(x) = x - x^3$.
* **Continuity:** Polynomial, continuous everywhere on $\mathbb{R}$.
* **Derivative:**
  $$ f'(x) = \frac{d}{dx}(x - x^3) = 1 - 3x^2 $$
* **Evaluation at $x_0 = 0$:**
  $$ \lim_{x \to 0^+} f'(x) = f'(0) = 1 - 0 = 1 < \infty $$
  On any compact interval $[0, b]$, $|f'(x)| \le 1 + 3b^2 = L < \infty$.
* **Conclusion:** $f(x)$ is locally Lipschitz on $[0, \infty)$. The solution is **strictly unique** for any $x(0) \ge 0$.

---

### Part (ii): $\dot{x} = x^3$
* **Vector Field:** $f(x) = x^3$.
* **Continuity:** Smooth monomial on $\mathbb{R}$.
* **Derivative:**
  $$ f'(x) = 3x^2 $$
* **Evaluation at $x_0 = 0$:**
  $$ \lim_{x \to 0^+} f'(x) = f'(0) = 0 < \infty $$
  On any neighborhood $[0, b]$, $|f'(x)| \le 3b^2 = L < \infty$.
* **Conclusion:** $f(x)$ is locally Lipschitz everywhere on $[0, \infty)$. By Picard-Lindelöf, the solution is **strictly unique** locally for any $x(0) \ge 0$.  
  *(Note: While solutions with $x_0 > 0$ blow up at finite time $t^* = \frac{1}{2x_0^2}$, uniqueness holds up to the blow-up boundary).*

---

### Part (iii): $\dot{x} = x^{1/3}$
* **Vector Field:** $f(x) = x^{1/3}$.
* **Continuity:** Continuous for all $x \ge 0$.
* **Derivative:**
  $$ f'(x) = \frac{d}{dx}\left( x^{1/3} \right) = \frac{1}{3} x^{-2/3} = \frac{1}{3 x^{2/3}} $$
* **Evaluation at $x_0 = 0$:**
  $$ \lim_{x \to 0^+} f'(x) = \lim_{x \to 0^+} \frac{1}{3 x^{2/3}} = +\infty $$
  The derivative is unbounded in every neighborhood of $x = 0$. The Lipschitz condition is **violated at the origin**.
* **Proof of Non-Uniqueness for $x(0) = 0$:**
  1. $x_1(t) \equiv 0$ is a valid solution ($\dot{x}_1 = 0 = 0^{1/3}$).
  2. By separation of variables, $\int x^{-1/3} dx = \int dt \implies \frac{3}{2} x^{2/3} = t \implies x_2(t) = \left(\frac{2}{3} t\right)^{3/2}$ is also a valid solution for $t \ge 0$ satisfying $x_2(0) = 0$.
* **Conclusion:** **Uniqueness fails** for $x(0) = 0$.

---

### Part (iv): $\dot{x} = x^{1/2}(1 + x)^2$
* **Vector Field:** $f(x) = \sqrt{x}(1 + x)^2$.
* **Continuity:** Continuous for all $x \ge 0$.
* **Derivative:** Using the product rule:
  $$ f'(x) = \frac{1}{2\sqrt{x}} (1 + x)^2 + \sqrt{x} \cdot 2(1 + x) = \frac{(1 + x)^2}{2\sqrt{x}} + 2\sqrt{x}(1 + x) $$
* **Evaluation at $x_0 = 0$:**
  $$ \lim_{x \to 0^+} f'(x) = \lim_{x \to 0^+} \left[ \frac{(1 + 0)^2}{2\sqrt{x}} + 0 \right] = \lim_{x \to 0^+} \frac{1}{2\sqrt{x}} = +\infty $$
  Due to the $\frac{1}{\sqrt{x}}$ singularity, $f'(x)$ is unbounded near $0$.
* **Proof of Non-Uniqueness for $x(0) = 0$:**
  1. $x_1(t) \equiv 0$ is a solution.
  2. Near $x = 0$, $(1 + x)^2 \approx 1$, so the equation behaves like $\dot{x} \approx x^{1/2}$, yielding non-trivial branching solutions $x_2(t) \approx \frac{1}{4} t^2$.
* **Conclusion:** **Uniqueness fails** for $x(0) = 0$.

---

### Part (v): $\dot{x} = (1 + x)^{3/2}$
* **Vector Field:** $f(x) = (1 + x)^{3/2}$.
* **Continuity:** Continuous for all $x \ge -1$, hence on $[0, \infty)$.
* **Derivative:**
  $$ f'(x) = \frac{3}{2}(1 + x)^{1/2} = \frac{3}{2}\sqrt{1 + x} $$
* **Evaluation at $x_0 = 0$:**
  $$ \lim_{x \to 0^+} f'(x) = \frac{3}{2}\sqrt{1 + 0} = \frac{3}{2} < \infty $$
  For any $x \in [0, b]$, $|f'(x)| \le \frac{3}{2}\sqrt{1 + b} = L < \infty$. The derivative is uniformly bounded on bounded intervals.
* **Conclusion:** $f(x)$ is locally Lipschitz on $[0, \infty)$. The solution is **strictly unique** for any $x(0) \ge 0$.

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Master Classification Summary:

| Item | Equation | $f'(x)$ near $x \to 0^+$ | Lipschitz at $x_0 = 0$? | Local Uniqueness for all $x(0) \ge 0$? |
| :---: | :--- | :---: | :---: | :---: |
| **(i)** | $\dot{x} = x(1 - x^2)$ | $1$ | **Yes** | **UNIQUE** |
| **(ii)** | $\dot{x} = x^3$ | $0$ | **Yes** | **UNIQUE** |
| **(iii)** | $\dot{x} = x^{1/3}$ | $+\infty$ | **No** | **NOT UNIQUE** (Multiple solutions at $x_0=0$) |
| **(iv)** | $\dot{x} = x^{1/2}(1+x)^2$ | $+\infty$ | **No** | **NOT UNIQUE** (Multiple solutions at $x_0=0$) |
| **(v)** | $\dot{x} = (1+x)^{3/2}$ | $3/2$ | **Yes** | **UNIQUE** |

### Final Answer:
The differential equations that have unique solutions for every non-negative initial condition $x(0) \ge 0$ are:
$$ \mathbf{\text{(i), (ii), and (v)}} $$

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Well-Posed Problems and Picard Theorem|Well-Posed Problems and Picard-Lindelöf Theorem]]`
* `[[04 - Advanced Maths/Problema - Ch2-P14 Non-Lipschitz Branching Pathology in Picard Theorem|Problem 2.14: Picard Branching Pathology]]`
