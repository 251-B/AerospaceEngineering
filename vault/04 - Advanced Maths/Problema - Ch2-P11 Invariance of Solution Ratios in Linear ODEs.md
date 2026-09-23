---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.11"
dificultad: baja
tags:
  - problema-resuelto
  - regla-cociente
  - dependencia-lineal
  - wronskiano
  - espacio-soluciones
---

# ✏️ Problem 2.11: Invariance of Solution Ratios in Linear ODEs

## 📄 Enunciado (Problem Statement)

Without solving the ODE, show that if $y_1(t)$ and $y_2(t)$ are any two solutions of:
$$ \frac{dy}{dt} + p(t) y = 0 $$
then the ratio $\frac{y_1(t)}{y_2(t)}$ is constant.

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Setting:
* **Differential Equation:** $y'(t) + p(t) y(t) = 0$.
* **Solutions:** $y_1(t)$ and $y_2(t)$ are two arbitrary continuously differentiable solutions on an open interval $I \subseteq \mathbb{R}$.
* **Hypothesis on $y_2$:** $y_2(t) \neq 0$ for all $t \in I$ (by Problem 2.10, if $y_2(t_0) \neq 0$, it never vanishes anywhere on $I$).
* **Constraint:** The proof must be established **strictly without solving the ODE** (no integration or formula evaluation permitted).

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

1. Define the ratio function:
   $$ R(t) \equiv \frac{y_1(t)}{y_2(t)} $$
2. Differentiate $R(t)$ with respect to time $t$ using the **quotient rule of calculus**:
   $$ R'(t) = \frac{y_1'(t) y_2(t) - y_1(t) y_2'(t)}{[y_2(t)]^2} $$
3. Since $y_1$ and $y_2$ solve the ODE, their derivatives satisfy:
   $$ y_1'(t) = -p(t) y_1(t) \quad \text{and} \quad y_2'(t) = -p(t) y_2(t) $$
4. Substitute these expressions into the numerator of the quotient rule.
5. Demonstrate that the numerator vanishes identically for all $t \in I$.
6. Conclude by the Mean Value Theorem that $R(t)$ is constant, proving that any two solutions of a first-order linear homogeneous ODE are linearly dependent.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Step 1: Definition of the Ratio Function
Consider the ratio of the two solutions on the interval $I$:
$$ R(t) = \frac{y_1(t)}{y_2(t)} \tag{1} $$

---

### Step 2: Differentiation via the Quotient Rule
Differentiating equation $(1)$ with respect to $t$:
$$ \frac{dR}{dt} = \frac{d}{dt}\left[ \frac{y_1(t)}{y_2(t)} \right] = \frac{y_1'(t) y_2(t) - y_1(t) y_2'(t)}{[y_2(t)]^2} \tag{2} $$

---

### Step 3: Substitution of the Differential Relations
Since $y_1(t)$ and $y_2(t)$ are both solutions to $\frac{dy}{dt} + p(t) y = 0$, they satisfy:
$$ y_1'(t) = -p(t) y_1(t) \tag{3} $$
$$ y_2'(t) = -p(t) y_2(t) \tag{4} $$

Substitute equations $(3)$ and $(4)$ directly into the numerator of $(2)$:
$$ \text{Numerator} = y_1'(t) y_2(t) - y_1(t) y_2'(t) $$
$$ = \left[ -p(t) y_1(t) \right] y_2(t) - y_1(t) \left[ -p(t) y_2(t) \right] \tag{5} $$

---

### Step 4: Algebraic Cancellation
Expand the terms in $(5)$:
$$ \text{Numerator} = -p(t) y_1(t) y_2(t) + p(t) y_1(t) y_2(t) \equiv 0 \tag{6} $$

Substituting $(6)$ back into the derivative $(2)$:
$$ \frac{dR}{dt} = \frac{0}{[y_2(t)]^2} = 0 \quad \forall t \in I \tag{7} $$

---

### Step 5: Deduction of Constancy
Since $\frac{dR}{dt} \equiv 0$ on the connected interval $I$, the function $R(t)$ is constant:
$$ R(t) = \frac{y_1(t)}{y_2(t)} \equiv C \tag{8} $$
where $C \in \mathbb{R}$ is a constant.

Multiplying by $y_2(t)$:
$$ \mathbf{y_1(t) = C \, y_2(t)} \tag{9} $$
This completes the proof. $\blacksquare$

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Formal Conclusion:
$$ \mathbf{\frac{d}{dt}\left[ \frac{y_1(t)}{y_2(t)} \right] = \frac{-p y_1 y_2 - y_1(-p y_2)}{y_2^2} = 0 \implies \frac{y_1(t)}{y_2(t)} = C} $$

### Linear Algebra & Wronskian Insights:
1. **Dimension of the Solution Space:**
   This result proves directly that the solution space of the first-order linear homogeneous ODE $y' + p(t)y = 0$ is a **one-dimensional vector space** over $\mathbb{R}$. Once any single non-trivial solution $y_2(t)$ is found, *every* other solution is simply a constant scalar multiple $y_1(t) = C y_2(t)$.
2. **Connection to the Wronskian:**
   The numerator in the quotient rule is the negative of the **Wronskian determinant** $W(y_1, y_2)(t)$:
   $$ W(y_1, y_2)(t) = \det \begin{pmatrix} y_1 & y_2 \\ y_1' & y_2' \end{pmatrix} = y_1 y_2' - y_2 y_1' = 0 $$
   An identically zero Wronskian is the hallmark of linear dependence in ODE theory.

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Factor Integrante y Ecuaciones Lineales de Primer Orden|Linear First-Order Theory]]`
* `[[04 - Advanced Maths/Problema - Ch2-P10 Uniqueness via Integrating Transformation|Problem 2.10: Uniqueness via Transformation]]`
