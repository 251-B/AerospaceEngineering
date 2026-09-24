---
materia: "Advanced Maths"
tema: "Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients"
origen: "ProblemsCh3.pdf — Exercise 1"
dificultad: media
tags:
  - problema-resuelto
  - wronskiano
  - independencia-lineal
  - edos-segundo-orden
  - aerospace-maths
---

# ✏️ Problem 3.1: Linear Independence via Wronskian Determinant

## 📄 Enunciado (Problem Statement)

By finding the Wronskian of the following pairs of functions, show that they are linearly independent:

**(i)** $x_1(t) = e^{k_1 t}$ and $x_2(t) = e^{k_2 t}$ with $k_1 \neq k_2$.  
**(ii)** $x_1(t) = e^{k t}$ and $x_2(t) = t e^{k t}$.  
**(iii)** $x_1(t) = e^{\rho t} \sin(\omega t)$ and $x_2(t) = e^{\rho t} \cos(\omega t)$ with $\omega \neq 0$.

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Setting:
We are given three pairs of smooth real functions $\{x_1(t), x_2(t)\} \subset C^\infty(\mathbb{R})$.
Each pair forms the canonical basis for the null space $\ker(L)$ of a second-order linear differential operator with constant coefficients:
$$ L[x] = a \ddot{x} + b \dot{x} + c x = 0 $$
corresponding respectively to:
1. Two distinct real roots: $k_1 \neq k_2 \in \mathbb{R}$.
2. A repeated real root: $k \in \mathbb{R}$ with algebraic multiplicity 2.
3. A pair of complex conjugate roots: $k = \rho \pm i\omega$ with $\omega \neq 0$.

### Goal:
Compute the Wronskian determinant $W[x_1, x_2](t)$ for each pair and prove that $W(t) \neq 0$ for all $t \in \mathbb{R}$, thereby establishing their linear independence.

---

## 🧠 2. Estrategia y Planteamiento Matemático (Phase 2)

### Wronskian Definition:
For two differentiable functions $x_1, x_2 \in C^1(I)$, the Wronskian determinant is defined as:
$$ W[x_1, x_2](t) = \det \begin{pmatrix} x_1(t) & x_2(t) \\ \dot{x}_1(t) & \dot{x}_2(t) \end{pmatrix} = x_1(t) \dot{x}_2(t) - x_2(t) \dot{x}_1(t) $$

### Linear Independence Criterion:
> [!NOTE] Fundamental Theorem of Linear Independence via Wronskian
> If the Wronskian $W[x_1, x_2](t)$ is non-zero at even a single point $t_0 \in I$, the functions $x_1(t)$ and $x_2(t)$ are linearly independent on the interval $I$.
> For solutions of a linear homogeneous second-order ODE with continuous coefficients, Abel's identity further guarantees that $W(t)$ is either non-zero everywhere or identically zero on $I$.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Part (i): Distinct Exponential Modes $x_1(t) = e^{k_1 t}$, $x_2(t) = e^{k_2 t}$ ($k_1 \neq k_2$)

1. Compute first-order time derivatives:
   $$ \dot{x}_1(t) = k_1 e^{k_1 t}, \qquad \dot{x}_2(t) = k_2 e^{k_2 t} $$

2. Construct and expand the Wronskian determinant:
   $$ W[x_1, x_2](t) = \det \begin{pmatrix} e^{k_1 t} & e^{k_2 t} \\ k_1 e^{k_1 t} & k_2 e^{k_2 t} \end{pmatrix} = e^{k_1 t}(k_2 e^{k_2 t}) - e^{k_2 t}(k_1 e^{k_1 t}) $$

3. Factor the exponential base:
   $$ W[x_1, x_2](t) = (k_2 - k_1) e^{(k_1 + k_2)t} \tag{1} $$

4. Evaluation and non-vanishing condition:
   Since the exponential function satisfies $e^{(k_1 + k_2)t} > 0$ for all $t \in \mathbb{R}$, and the problem statement establishes $k_1 \neq k_2 \iff k_2 - k_1 \neq 0$:
   $$ W[x_1, x_2](t) \neq 0 \quad \forall t \in \mathbb{R} $$
   Hence, $\{e^{k_1 t}, e^{k_2 t}\}$ are linearly independent on $\mathbb{R}$.

---

### Part (ii): Repeated Root Mode $x_1(t) = e^{kt}$, $x_2(t) = t e^{kt}$

1. Compute first-order time derivatives (applying product rule to $x_2$):
   $$ \dot{x}_1(t) = k e^{kt} $$
   $$ \dot{x}_2(t) = \frac{d}{dt}(t e^{kt}) = 1 \cdot e^{kt} + t \cdot (k e^{kt}) = (1 + kt) e^{kt} $$

2. Formulate the Wronskian determinant:
   $$ W[x_1, x_2](t) = \det \begin{pmatrix} e^{kt} & t e^{kt} \\ k e^{kt} & (1 + kt) e^{kt} \end{pmatrix} = e^{kt} \cdot (1 + kt) e^{kt} - t e^{kt} \cdot k e^{kt} $$

3. Expand algebraic terms:
   $$ W[x_1, x_2](t) = e^{2kt} \left[ (1 + kt) - k t \right] = e^{2kt} \cdot 1 = e^{2kt} \tag{2} $$

4. Non-vanishing condition:
   $$ W[x_1, x_2](t) = e^{2kt} > 0 \quad \forall t \in \mathbb{R} $$
   Since $W(t)$ is strictly positive everywhere, $\{e^{kt}, t e^{kt}\}$ are linearly independent on $\mathbb{R}$.

---

### Part (iii): Conjugate Complex Modes $x_1(t) = e^{\rho t} \sin(\omega t)$, $x_2(t) = e^{\rho t} \cos(\omega t)$ ($\omega \neq 0$)

1. Compute first-order time derivatives via product rule:
   $$ \dot{x}_1(t) = \rho e^{\rho t} \sin(\omega t) + \omega e^{\rho t} \cos(\omega t) = e^{\rho t} \left( \rho \sin(\omega t) + \omega \cos(\omega t) \right) $$
   $$ \dot{x}_2(t) = \rho e^{\rho t} \cos(\omega t) - \omega e^{\rho t} \sin(\omega t) = e^{\rho t} \left( \rho \cos(\omega t) - \omega \sin(\omega t) \right) $$

2. Formulate the Wronskian determinant:
   $$ W[x_1, x_2](t) = x_1 \dot{x}_2 - x_2 \dot{x}_1 $$
   $$ W[x_1, x_2](t) = \left( e^{\rho t} \sin(\omega t) \right) \cdot \left[ e^{\rho t} (\rho \cos(\omega t) - \omega \sin(\omega t)) \right] - \left( e^{\rho t} \cos(\omega t) \right) \cdot \left[ e^{\rho t} (\rho \sin(\omega t) + \omega \cos(\omega t)) \right] $$

3. Factor $e^{2\rho t}$:
   $$ W[x_1, x_2](t) = e^{2\rho t} \left[ \rho \sin(\omega t)\cos(\omega t) - \omega \sin^2(\omega t) - \rho \cos(\omega t)\sin(\omega t) - \omega \cos^2(\omega t) \right] $$

4. Cancel the cross-product terms $\rho \sin(\omega t)\cos(\omega t)$:
   $$ W[x_1, x_2](t) = e^{2\rho t} \left[ -\omega \left( \sin^2(\omega t) + \cos^2(\omega t) \right) \right] $$

5. Apply Pythagorean trigonometric identity $\sin^2\theta + \cos^2\theta = 1$:
   $$ W[x_1, x_2](t) = -\omega e^{2\rho t} \tag{3} $$

6. Non-vanishing condition:
   Since $\omega \neq 0$ and $e^{2\rho t} > 0$ for all $t \in \mathbb{R}$:
   $$ W[x_1, x_2](t) = -\omega e^{2\rho t} \neq 0 \quad \forall t \in \mathbb{R} $$
   Hence, the oscillatory modes $\{e^{\rho t}\sin(\omega t), e^{\rho t}\cos(\omega t)\}$ are linearly independent on $\mathbb{R}$.

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Master Summary of Wronskian Determinants:

| Pair of Functions | Parameter Condition | Wronskian $W[x_1, x_2](t)$ | Linear Independence Status |
| :--- | :--- | :--- | :---: |
| **(i)** $e^{k_1 t}, \; e^{k_2 t}$ | $k_1 \neq k_2$ | $\mathbf{(k_2 - k_1) e^{(k_1 + k_2)t}}$ | **Linearly Independent** on $\mathbb{R}$ |
| **(ii)** $e^{kt}, \; t e^{kt}$ | $k \in \mathbb{R}$ | $\mathbf{e^{2kt}}$ | **Linearly Independent** on $\mathbb{R}$ |
| **(iii)** $e^{\rho t}\sin\omega t, \; e^{\rho t}\cos\omega t$ | $\omega \neq 0$ | $\mathbf{-\omega e^{2\rho t}}$ | **Linearly Independent** on $\mathbb{R}$ |

### Aerospace & Dynamical Engineering Interpretation:
These three fundamental pairs constitute the complete modal alphabet of linear time-invariant (LTI) mechanical and aeronautical structures:
- Case (i) governs overdamped flight modes (e.g. roll subsidence, spiral mode).
- Case (ii) models critical damping, providing the most rapid monotonic return without overshoot in control actuator design.
- Case (iii) governs underdamped aeroelastic flutter and pitch-heave oscillations, where $\rho$ dictates damping rate and $\omega$ sets flutter frequency.

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Independencia Lineal de Funciones y Determinante Wronskiano|Independencia Lineal de Funciones y Determinante Wronskiano]]`
* `[[04 - Advanced Maths/Concepto - Identidad de Abel y Propiedades del Wronskiano|Identidad de Abel y Propiedades del Wronskiano]]`
* `[[04 - Advanced Maths/Concepto - Ecuaciones Homogeneas con Coeficientes Constantes y Ecuacion Caracteristica|Ecuaciones Homogéneas con Coeficientes Constantes]]`
* `[[04 - Advanced Maths/Problema - Ch3-P2 Abels Identity and Wronskian Dichotomy|Problem 3.2: Abel's Identity and Wronskian Dichotomy]]`
* `[[04 - Advanced Maths/Matematicas Avanzadas MOC|⬅️ Central Advanced Maths MOC]]`
