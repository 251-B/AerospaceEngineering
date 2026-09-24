---
materia: "Advanced Maths"
tema: "Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients"
origen: "ProblemsCh3.pdf — Exercise 2"
dificultad: media
tags:
  - problema-resuelto
  - identidad-de-abel
  - dicotomia-wronskiano
  - edos-segundo-orden
  - teoria-fundamental
---

# ✏️ Problem 3.2: Abel's Identity and Wronskian Dichotomy

## 📄 Enunciado (Problem Statement)

Show that the Wronskian for two solutions $x_1(t)$ and $x_2(t)$ of the second order differential equation
$$ \frac{d^2x}{dt^2} + p_1(t)\frac{dx}{dt} + p_2(t)x = 0 $$
satisfies
$$ \frac{dW(t)}{dt} = -p_1(t)W(t). $$
Deduce either that $W(t) = 0$ for all $t$, or that $W(t) \neq 0$ for all $t$.

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Hypotheses:
1. Let $I \subseteq \mathbb{R}$ be an open interval.
2. The coefficient functions $p_1(t), p_2(t) \in C^0(I)$ are continuous on $I$.
3. The functions $x_1(t)$ and $x_2(t)$ are two classical solutions of the homogeneous equation:
   $$ L[x] \equiv \ddot{x} + p_1(t)\dot{x} + p_2(t)x = 0, \qquad x_1, x_2 \in C^2(I) $$
4. The Wronskian of the ordered pair $(x_1, x_2)$ is defined as:
   $$ W(t) \equiv W[x_1, x_2](t) = x_1(t)\dot{x}_2(t) - x_2(t)\dot{x}_1(t) $$

---

## 🧠 2. Estrategia y Planteamiento Físico-Matemático (Phase 2)

### Plan:
1. **Differentiate the Wronskian:** Apply the Leibniz product rule to compute $\frac{dW}{dt}$. Notice the natural cancellation of symmetric terms $\dot{x}_1 \dot{x}_2$.
2. **Substitute the ODEs:** Express $\ddot{x}_1$ and $\ddot{x}_2$ in terms of first and zeroth derivatives using the fact that both satisfy $L[x] = 0$.
3. **Derive Abel's Differential Equation:** Factor out $-p_1(t)$ and note that the remaining term proportional to $p_2(t)$ identically vanishes.
4. **Integrate to Abel's Formula:** Solve the first-order separable linear ODE for $W(t)$ using an integrating factor or separation of variables.
5. **Deduce the Wronskian Dichotomy:** Use the strict positivity of the exponential function $\exp(-\int p_1 ds) > 0$ to prove the binary behavior.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Step 1: Derivative of the Wronskian Determinant
Starting from the definition:
$$ W(t) = x_1(t)\dot{x}_2(t) - x_2(t)\dot{x}_1(t) $$
Differentiating with respect to $t$:
$$ \frac{dW(t)}{dt} = \frac{d}{dt}\left[ x_1(t)\dot{x}_2(t) \right] - \frac{d}{dt}\left[ x_2(t)\dot{x}_1(t) \right] $$
By the product rule:
$$ \frac{dW}{dt} = \left( \dot{x}_1\dot{x}_2 + x_1\ddot{x}_2 \right) - \left( \dot{x}_2\dot{x}_1 + x_2\ddot{x}_1 \right) $$
The mixed terms $\dot{x}_1\dot{x}_2$ and $\dot{x}_2\dot{x}_1$ cancel identically:
$$ \frac{dW(t)}{dt} = x_1(t)\ddot{x}_2(t) - x_2(t)\ddot{x}_1(t) \tag{1} $$

---

### Step 2: Incorporating the Differential Equation
Since $x_1(t)$ and $x_2(t)$ solve $\ddot{x} + p_1(t)\dot{x} + p_2(t)x = 0$, we isolate their second derivatives:
$$ \ddot{x}_1(t) = -p_1(t)\dot{x}_1(t) - p_2(t)x_1(t) \tag{2a} $$
$$ \ddot{x}_2(t) = -p_1(t)\dot{x}_2(t) - p_2(t)x_2(t) \tag{2b} $$
Substitute (2a) and (2b) into equation (1):
$$ \frac{dW}{dt} = x_1\left( -p_1\dot{x}_2 - p_2 x_2 \right) - x_2\left( -p_1\dot{x}_1 - p_2 x_1 \right) $$

---

### Step 3: Regrouping and Algebraic Simplification
Expand and group terms by coefficients $p_1(t)$ and $p_2(t)$:
$$ \frac{dW}{dt} = -p_1(t)\left[ x_1(t)\dot{x}_2(t) - x_2(t)\dot{x}_1(t) \right] - p_2(t)\left[ x_1(t)x_2(t) - x_2(t)x_1(t) \right] $$
Notice that:
* The bracket multiplying $-p_1(t)$ is precisely the definition of $W(t)$:
  $$ x_1\dot{x}_2 - x_2\dot{x}_1 = W(t) $$
* The bracket multiplying $-p_2(t)$ is identically zero by commutativity:
  $$ x_1 x_2 - x_2 x_1 = 0 $$
Therefore:
$$ \mathbf{\frac{dW(t)}{dt} = -p_1(t) W(t)} \tag{3} $$
This completes the first part of the proof.

---

### Step 4: Analytical Integration — Abel's Identity
Equation (3) is a linear, homogeneous, first-order ordinary differential equation for the unknown function $W(t)$.
Separating variables on any subinterval where $W(t) \neq 0$:
$$ \frac{1}{W(t)} \frac{dW}{dt} = -p_1(t) \implies \frac{d}{dt}\left( \ln|W(t)| \right) = -p_1(t) $$
Integrating both sides from an arbitrary reference point $t_0 \in I$ to $t$:
$$ \int_{t_0}^t \frac{d}{ds}\left( \ln|W(s)| \right) ds = -\int_{t_0}^t p_1(s)\,ds $$
$$ \ln|W(t)| - \ln|W(t_0)| = -\int_{t_0}^t p_1(s)\,ds $$
Exponentiating both sides:
$$ \left| \frac{W(t)}{W(t_0)} \right| = \exp\left( -\int_{t_0}^t p_1(s)\,ds \right) $$
Resolving the absolute value and noting continuity:
$$ \mathbf{W(t) = W(t_0) \exp\left( -\int_{t_0}^t p_1(s)\,ds \right)} \tag{4} $$

---

### Step 5: Deduction of the Wronskian Dichotomy
Let $E(t) = \exp\left(-\int_{t_0}^t p_1(s)\,ds\right)$.
Because $p_1(s)$ is continuous on $I$, the integral $\int_{t_0}^t p_1(s)\,ds$ is a well-defined finite real number for every $t \in I$.
The exponential function takes strictly positive values everywhere:
$$ E(t) > 0 \quad \forall t \in I $$
Now, examine the factor $W(t_0)$ in equation (4):
1. **Case A: $W(t_0) = 0$ at some point $t_0 \in I$.**
   $$ W(t) = 0 \cdot E(t) = 0 \quad \forall t \in I $$
   Thus, if the Wronskian vanishes at a single point, it must vanish identically on the entire interval $I$.
2. **Case B: $W(t_0) \neq 0$ at some point $t_0 \in I$.**
   Since $W(t_0) \neq 0$ and $E(t) \neq 0$, their product can never be zero:
   $$ W(t) = W(t_0) \cdot E(t) \neq 0 \quad \forall t \in I $$
   Thus, if the Wronskian is non-zero at a single point, it is non-zero at every point of the interval $I$.

> [!IMPORTANT] The Wronskian Dichotomy Theorem
> For any two solutions of a linear homogeneous second-order ODE with continuous coefficients on an interval $I$, exactly one of the following two mutually exclusive alternatives holds:
> 1. $W(t) = 0$ for all $t \in I$ (solutions are linearly dependent on $I$).
> 2. $W(t) \neq 0$ for all $t \in I$ (solutions form a fundamental set on $I$).
> The Wronskian can **never** cross zero or change signs without being identically zero.

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Master Formulas:
$$ \boxed{\frac{dW(t)}{dt} = -p_1(t)W(t)} $$
$$ \boxed{W(t) = W(t_0) \exp\left( -\int_{t_0}^t p_1(s)\,ds \right)} $$

### Aerospace & Systems Insight:
- In aeroelastic flutter analysis, the coefficient $p_1(t)$ represents aeroelastic damping $2\zeta\omega_n$. Abel's identity proves that state-space phase volume contraction is governed strictly by the damping trace:
  $$ \frac{dV}{dt} = -p_1(t) V(t) $$
  When damping is positive ($p_1 > 0$), phase volume decays exponentially, guaranteeing asymptotic stability (Liouville's theorem for dissipative linear systems).

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Identidad de Abel y Propiedades del Wronskiano|Identidad de Abel y Propiedades del Wronskiano]]`
* `[[04 - Advanced Maths/Concepto - Independencia Lineal de Funciones y Determinante Wronskiano|Determinante Wronskiano]]`
* `[[04 - Advanced Maths/Problema - Ch3-P3 Peano Counterexample on Wronskian Vanishing|Problem 3.3: Peano Counterexample]]`
* `[[04 - Advanced Maths/Matematicas Avanzadas MOC|⬅️ Central Advanced Maths MOC]]`
