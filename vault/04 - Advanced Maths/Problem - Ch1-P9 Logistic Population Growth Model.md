---
materia: "Advanced Mathematics"
tema: "Tema 1: Introduction, Modeling and Classification of ODEs"
origen: "ProblemsCh1.pdf — Exercise 1.9"
dificultad: media
tags:
  - problema-resuelto
  - modelo-logistico
  - verhulst
  - fracciones-parciales
  - capacidad-carga
  - limites-asintoticos
---

# ✏️ Problem 1.9: Logistic Population Growth Model

## 📄 Enunciado (Problem Statement)

A refinement over Malthus' population growth model discussed in Chapter 1 is provided by the logistic equation:
$$ \frac{dp}{dt} = kp \left( 1 - \frac{p}{M} \right) $$
where $p(t)$ is the population size at time $t$, $k$ is its growth rate (difference between birth rate and death rate), and $M$ is the maximum sustainable population (carrying capacity).

Solve the equation for a generic initial condition $p(t_0) = p_0$ and discuss the evolution of the population for $t \to \infty$, comparing with Malthus' ($M \to \infty$) prediction.

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Variables and Parameters:
* **Dependent variable:** Population $p(t) > 0$ $[N]$.
* **Independent variable:** Time $t \ge t_0$ $[T]$.
* **Parameters:**
  * Net intrinsic growth rate: $k = \beta - \delta > 0$ $[T^{-1}]$.
  * Carrying capacity: $M > 0$ $[N]$.
  * Initial state: $p(t_0) = p_0 > 0$ at initial time $t_0$.

### Hypotheses:
* [x] **Density-dependent limitation:** Environmental resistance increases proportionally with population density, reducing the effective growth rate linearly: $k_{\text{eff}}(p) = k\left(1 - \frac{p}{M}\right)$.
* [x] **Continuous differentiability:** $p \in C^1([t_0, \infty))$.
* [x] **Non-trivial initial state:** $p_0 > 0$. If $p_0 = M$, the solution is identically the steady state $p(t) \equiv M$.

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

1. The logistic equation $\frac{dp}{dt} = \frac{k}{M} p(M - p)$ is a **first-order separable nonlinear ODE**.
2. Separate variables by moving all terms in $p$ to the left-hand side and all terms in $t$ to the right-hand side:
   $$ \frac{dp}{p(M - p)} = \frac{k}{M} dt $$
3. Perform a **partial fraction decomposition** on the rational algebraic fraction $\frac{1}{p(M - p)}$.
4. Integrate both sides from initial state $(t_0, p_0)$ to current state $(t, p(t))$, strictly retaining all intermediate signs.
5. Invert the logarithmic equation to isolate $p(t)$ as an explicit function of time.
6. Evaluate the long-term asymptotic limit $\lim_{t \to \infty} p(t)$ and the unbounded capacity limit $\lim_{M \to \infty} p(t)$, comparing with Malthus' law.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Step 1: Constant solutions and separation (method of the class notes [Notes.pdf, p. 3])
The class notes solve this equation as their example of a separable equation. By Picard's theorem a solution that takes the value $0$ or $M$ is constant: $p \equiv 0$ or $p \equiv M$, or $p$ never reaches these values. Take $p_0 > 0$, $p_0 \neq M$; then $p(t) > 0$ and $M - p(t)$ keeps the sign of $M - p_0$. Separating ($f(p) = p(1 - p/M)$, $g = k$):
$$ \int_{p_0}^{p} \frac{du}{u\left(1 - \frac{u}{M}\right)} = \int_{t_0}^{t} k\,d\tau = k(t - t_0) \tag{1} $$

---

### Step 2: Partial fractions (as in the notes)
$$ \frac{1}{u\left(1 - \frac uM\right)} = \frac{A}{u} + \frac{B}{1 - \frac uM} \implies 1 = A\left(1 - \frac uM\right) + Bu $$
* $u = 0$: $1 = A$.
* $u = M$: $1 = 0 + BM \implies B = \frac1M$.

Hence, multiplying top and bottom of the second fraction by $M$:
$$ \frac{1}{u\left(1 - \frac uM\right)} = \frac1u + \frac{1/M}{1 - u/M} = \frac1u + \frac{1}{M - u} \tag{2} $$

---

### Step 3: Exact definite integration
An antiderivative of $\frac1u$ ($u > 0$) is $\ln u$; for $\frac{1}{M - u}$ substitute $w = M - u$, $dw = -du$: $\int\frac{du}{M - u} = -\ln|M - u|$. By Barrow's rule
$$ \int_{p_0}^{p}\frac{du}{u} + \int_{p_0}^{p}\frac{du}{M - u} = \ln\frac{p}{p_0} + \ln\frac{|M - p_0|}{|M - p|} = \ln\frac{p\,(M - p_0)}{p_0\,(M - p)} \tag{3} $$
(the moduli cancel because $M - p$ and $M - p_0$ have the same sign).

---

### Step 4: Exponentiation and isolation of $p(t)$ (the notes' $E$)
Equating (1) and (3) and exponentiating:
$$ \frac{p}{M - p} = \frac{p_0\,e^{k(t - t_0)}}{M - p_0} =: E $$
Then $p = (M - p)E = ME - pE$, so $p(1 + E) = ME$ and
$$ p(t) = \frac{ME}{1 + E} = \frac{M p_0 e^{k(t - t_0)}}{(M - p_0) + p_0 e^{k(t - t_0)}} \tag{4} $$

Divide both the numerator and the denominator by $e^{k(t - t_0)}$:
$$ \mathbf{p(t) = \frac{M p_0}{p_0 + (M - p_0) e^{-k(t - t_0)}}} \tag{5} $$

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Final Analytical Solution:
$$ \mathbf{p(t) = \frac{M p_0}{p_0 + (M - p_0) e^{-k(t - t_0)}}} $$

### Asymptotic Evolution as $t \to \infty$:
Since $k > 0$, as $t \to \infty$, the term $(t - t_0) \to +\infty$, which drives the exponential decay term to zero:
$$ \lim_{t \to \infty} e^{-k(t - t_0)} = 0 $$

Evaluating the limit:
$$ \lim_{t \to \infty} p(t) = \frac{M p_0}{p_0 + (M - p_0) \cdot 0} = \frac{M p_0}{p_0} = \mathbf{M} $$

* **Physical Interpretation:** Regardless of whether the initial population starts below the carrying capacity ($0 < p_0 < M$, sigmoidal growth) or above it ($p_0 > M$, monotonic die-off), the population asymptotically stabilizes at the **carrying capacity $M$**. The equilibrium state $p = M$ is globally asymptotically stable for all $p_0 > 0$.

```mermaid
xychart-beta
    title "Logistic Growth: Saturation at Carrying Capacity M"
    x-axis "Time t" [0, 1, 2, 3, 4, 5, 6, 7, 8]
    y-axis "Population p(t)" 0 --> 100
    line [10, 18, 32, 53, 74, 88, 95, 98, 99]
```

---

### Comparison with Malthus' Prediction ($M \to \infty$):
Divide the numerator and denominator of $(5)$ by $M$:
$$ p(t) = \frac{p_0}{\frac{p_0}{M} + \left(1 - \frac{p_0}{M}\right) e^{-k(t - t_0)}} $$

Taking the mathematical limit as carrying capacity becomes infinite ($M \to \infty$):
$$ \lim_{M \to \infty} \frac{p_0}{M} = 0 $$
$$ \lim_{M \to \infty} p(t) = \frac{p_0}{0 + (1 - 0) e^{-k(t - t_0)}} = \frac{p_0}{e^{-k(t - t_0)}} = \mathbf{p_0 e^{k(t - t_0)}} $$

* **Comparison:** Malthus' model predicts unconstrained exponential growth without bound ($\lim_{t\to\infty} p_{\text{Malthus}} = +\infty$), corresponding physically to an infinite environment ($M \to \infty$). Verhulst's logistic equation contains Malthus' model as a special asymptotic limit, but reflects finite resources by bending the trajectory into a saturation asymptote at $p = M$.

---

## 🔗 Related Notes
* [[04 - Advanced Maths/Concept - Logistic Equation and Carrying Capacity|Logistic Equation and Carrying Capacity]]
* [[04 - Advanced Maths/Concept - First-Order Physical Models|First-Order Physical Models]]
* [[04 - Advanced Maths/Problem - Ch1-P2 Malthusian Population Dynamics|Problem 1.2: Malthusian Population Dynamics]]
