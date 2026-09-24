---
materia: "Advanced Maths"
tema: "Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients"
origen: "ProblemsCh3.pdf — Exercise 3"
dificultad: media-alta
tags:
  - problema-resuelto
  - wronskiano
  - contraejemplo-peano
  - independencia-lineal
  - analisis-real
---

# ✏️ Problem 3.3: Peano's Counterexample on Wronskian Vanishing

## 📄 Enunciado (Problem Statement)

We have seen that, if $x_1(t)$ and $x_2(t)$ are two solutions of a linear homogeneous second order differential equation, then they are linearly independent if and only if their Wronskian is non-zero. This is not true for general functions that are not the solutions of some differential equation.

**(i)** Check that, if $f(t) = t^2 |t|$, then $\frac{df}{dt} = 3t |t|$ (straightforward for $t \neq 0$; you will have to use the formal definition of the derivative at $t = 0$).  
**(ii)** Considering $f_1(t) = t^2 |t|$ and $f_2(t) = t^3$, show that, although these two functions are linearly independent on $\mathbb{R}$, their Wronskian is identically zero.

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Setting:
1. Consider the function $f(t) = t^2 |t|$ defined on all $t \in \mathbb{R}$.
2. Absolute value definition:
   $$ |t| = \begin{cases} t, & t \ge 0 \\ -t, & t < 0 \end{cases} \implies f(t) = \begin{cases} t^3, & t \ge 0 \\ -t^3, & t < 0 \end{cases} $$
3. Let $f_1(t) = t^2 |t|$ and $f_2(t) = t^3$. Both functions belong to $C^2(\mathbb{R})$.
4. This is the celebrated **Peano Counterexample** (Giuseppe Peano, 1889), which clarifies the boundary between pure linear algebra in function spaces and ordinary differential equations.

---

## 🧠 2. Estrategia y Planteamiento Matemático (Phase 2)

### Part (i) Plan:
- For $t > 0$: $f(t) = t^3$, standard polynomial differentiation gives $3t^2 = 3t|t|$.
- For $t < 0$: $f(t) = -t^3$, differentiation gives $-3t^2 = 3t(-t) = 3t|t|$.
- At $t = 0$: evaluate the limit of the Newton difference quotient:
  $$ f'(0) = \lim_{h \to 0} \frac{f(0 + h) - f(0)}{h} $$

### Part (ii) Plan:
- **Linear Independence on $\mathbb{R}$:** Use the definition: $c_1 f_1(t) + c_2 f_2(t) = 0$ for all $t \in \mathbb{R}$. Pick two test points (e.g. $t = 1$ and $t = -1$) to construct a linear system and prove $c_1 = c_2 = 0$.
- **Wronskian Calculation:** Compute $W[f_1, f_2](t) = f_1(t) f_2'(t) - f_2(t) f_1'(t)$ across all $t \in \mathbb{R}$. Show it evaluates identically to $0$.
- **Pedagogical Explanation:** Explain why this does not contradict the Wronskian theorem for ODEs.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Part (i): Derivative of $f(t) = t^2 |t|$

#### Case 1: $t > 0$
When $t > 0$, $|t| = t$, so $f(t) = t^2 \cdot t = t^3$.
$$ \frac{df}{dt} = \frac{d}{dt}(t^3) = 3t^2 $$
Since $t > 0$, $|t| = t \implies 3t^2 = 3t(t) = 3t|t|$.

#### Case 2: $t < 0$
When $t < 0$, $|t| = -t$, so $f(t) = t^2(-t) = -t^3$.
$$ \frac{df}{dt} = \frac{d}{dt}(-t^3) = -3t^2 $$
Since $t < 0$, $|t| = -t \implies -3t^2 = 3t(-t) = 3t|t|$.

#### Case 3: $t = 0$ (Formal limit of difference quotient)
At $t = 0$, $f(0) = 0^2 \cdot |0| = 0$. By definition of the derivative:
$$ f'(0) = \lim_{h \to 0} \frac{f(h) - f(0)}{h} = \lim_{h \to 0} \frac{h^2 |h| - 0}{h} = \lim_{h \to 0} h |h| $$
Evaluating the two-sided limit:
$$ \lim_{h \to 0^+} h |h| = \lim_{h \to 0^+} h^2 = 0 $$
$$ \lim_{h \to 0^-} h |h| = \lim_{h \to 0^-} (-h^2) = 0 $$
Since both one-sided limits exist and are equal to $0$:
$$ f'(0) = 0 $$
Evaluating the proposed formula $3t|t|$ at $t = 0$:
$$ 3(0)|0| = 0 $$
Therefore, for all $t \in \mathbb{R}$:
$$ \mathbf{\frac{df}{dt} = 3t|t|} \tag{1} $$
*(Note: repeating this procedure shows $f''(t) = 6|t|$, which is continuous at $t=0$, so $f \in C^2(\mathbb{R})$).*

---

### Part (ii): Linear Independence vs Wronskian on $\mathbb{R}$

#### Sub-step 1: Proof of Linear Independence on $\mathbb{R}$
Let $c_1, c_2 \in \mathbb{R}$ such that:
$$ c_1 f_1(t) + c_2 f_2(t) = 0, \quad \forall t \in \mathbb{R} \tag{2} $$
Substituting explicit definitions:
$$ c_1 t^2 |t| + c_2 t^3 = 0, \quad \forall t \in \mathbb{R} $$
This equality must hold for every real value of $t$:
* Evaluate at $t = 1$:
  $$ c_1 (1)^2 |1| + c_2 (1)^3 = 0 \implies c_1 + c_2 = 0 \tag{3a} $$
* Evaluate at $t = -1$:
  $$ c_1 (-1)^2 |-1| + c_2 (-1)^3 = 0 \implies c_1(1) + c_2(-1) = 0 \implies c_1 - c_2 = 0 \tag{3b} $$

Solving the system (3a)–(3b):
Adding both equations:
$$ (c_1 + c_2) + (c_1 - c_2) = 0 \implies 2c_1 = 0 \implies c_1 = 0 $$
Subtracting (3b) from (3a):
$$ 2c_2 = 0 \implies c_2 = 0 $$
Since the only linear combination that vanishes for all $t \in \mathbb{R}$ is the trivial one $c_1 = c_2 = 0$:
$$ \mathbf{f_1(t) \text{ and } f_2(t) \text{ are linearly independent on } \mathbb{R}.} $$

---

#### Sub-step 2: Calculation of the Wronskian Determinant
The derivatives are:
* $f_1'(t) = 3t|t|$
* $f_2'(t) = \frac{d}{dt}(t^3) = 3t^2$

The Wronskian determinant is:
$$ W[f_1, f_2](t) = f_1(t) f_2'(t) - f_2(t) f_1'(t) $$
Substitute the functions and derivatives:
$$ W[f_1, f_2](t) = \left( t^2 |t| \right) \cdot \left( 3t^2 \right) - \left( t^3 \right) \cdot \left( 3t |t| \right) $$
Simplify each term:
$$ W[f_1, f_2](t) = 3 t^4 |t| - 3 t^4 |t| \equiv 0 $$
$$ \mathbf{W[f_1, f_2](t) = 0 \quad \forall t \in \mathbb{R}.} \tag{4} $$

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Master Resolution Summary:
1. $\mathbf{f'(t) = 3t|t|}$ for all $t \in \mathbb{R}$, rigorously verified at $t = 0$ via the Newton quotient.
2. $\mathbf{f_1(t) \text{ and } f_2(t)}$ are **linearly independent on $\mathbb{R}$**, yet their Wronskian **vanishes identically: $W(t) \equiv 0$**.

### Critical Epistemological Insight (Why is there no contradiction?):
> [!WARNING] The Critical Difference: General Functions vs ODE Solutions
> The theorem stating that *"identically vanishing Wronskian implies linear dependence"* requires the crucial hypothesis that $x_1(t), x_2(t)$ are solutions of a **regular second-order linear ODE**:
> $$ x'' + p_1(t)x' + p_2(t)x = 0 $$
> where $p_1(t)$ and $p_2(t)$ are **continuous** across the entire interval.
> 
> If we construct the differential equation satisfied by $f_1$ and $f_2$:
> On $t > 0$, $f_1 = f_2 = t^3$, both satisfy $t^2 x'' - 6x = 0 \iff x'' - \frac{6}{t^2} x = 0$.
> Notice that the coefficient $p_2(t) = -\frac{6}{t^2}$ is **singular at $t = 0$**! There exists no regular ODE with continuous coefficients at $t = 0$ that has both $f_1$ and $f_2$ as solutions.
> Therefore, Abel's identity does not apply across $t = 0$, which is why linearly independent functions can exhibit an identically vanishing Wronskian.

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Independencia Lineal de Funciones y Determinante Wronskiano|Determinante Wronskiano]]`
* `[[04 - Advanced Maths/Concepto - Identidad de Abel y Propiedades del Wronskiano|Identidad de Abel y Dicotomía]]`
* `[[04 - Advanced Maths/Problema - Ch3-P1 Linear Independence via Wronskian|Problem 3.1: Wronskian Linear Independence]]`
* `[[04 - Advanced Maths/Problema - Ch3-P2 Abels Identity and Wronskian Dichotomy|Problem 3.2: Abel's Identity]]`
* `[[04 - Advanced Maths/Matematicas Avanzadas MOC|⬅️ Central Advanced Maths MOC]]`
