---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.6"
dificultad: media
tags:
  - problema-resuelto
  - formas-separadas
  - ecuaciones-exactas
  - conservacion-energia
  - dinamica-lotka-volterra
---

# ✏️ Problem 2.6: Exactness of Separated Differential Forms

## 📄 Enunciado (Problem Statement)

Show that any equation that can be written in the form:
$$ f(x) + g(y) \frac{dy}{dx} = 0 $$
is exact, and find its solution in terms of integrals of $f$ and $g$. Hence find the solutions of:

(i) $V'(x) + 2y \frac{dy}{dx} = 0$  
(ii) $\left( \frac{1}{y} - a \right) \frac{dy}{dx} + \frac{2}{x} - b = 0$, for $x, y > 0$.

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Structure:
An equation where the velocity field is separated additively into single-variable components:
$$ f(x) \, dx + g(y) \, dy = 0 $$
with $M(x, y) = f(x)$ and $N(x, y) = g(y)$.

### Particular Cases:
* **(i)** $f(x) = V'(x)$, $g(y) = 2y$.
* **(ii)** $f(x) = \frac{2}{x} - b$, $g(y) = \frac{1}{y} - a$, with domain restricted to the first quadrant $x > 0, y > 0$. Parameters $a, b > 0$.

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

1. Compute the mixed partial derivatives $\frac{\partial M}{\partial y}$ and $\frac{\partial N}{\partial x}$. Because $f(x)$ is independent of $y$ and $g(y)$ is independent of $x$, both partials vanish identically, establishing universal exactness.
2. Integrate the total differential $dF = f(x) dx + g(y) dy = 0$ to construct the potential $F(x, y) = \int f(x) dx + \int g(y) dy = C$.
3. Apply this general formula directly to solve parts (i) and (ii).

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Step 1: General Proof of Exactness
Write the equation in standard differential form:
$$ M(x, y) \, dx + N(x, y) \, dy = 0 $$
where:
$$ M(x, y) = f(x), \quad N(x, y) = g(y) $$

Compute the cross partial derivatives:
$$ \frac{\partial M}{\partial y} = \frac{\partial}{\partial y} [f(x)] = 0 $$
$$ \frac{\partial N}{\partial x} = \frac{\partial}{\partial x} [g(y)] = 0 $$
Since:
$$ \frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} = 0 $$
on any domain where $f$ and $g$ are defined, **every separated differential equation is automatically exact**. $\blacksquare$

---

### Step 2: General Solution in Terms of Integrals
Because the differential form is exact, there exists a potential function $F(x, y)$ such that $dF = f(x) dx + g(y) dy$:
$$ \frac{\partial F}{\partial x} = f(x) \implies F(x, y) = \int f(x) \, dx + h(y) $$
Differentiating with respect to $y$:
$$ \frac{\partial F}{\partial y} = h'(y) = N(x, y) = g(y) \implies h(y) = \int g(y) \, dy $$
Therefore, the general potential function is:
$$ \mathbf{F(x, y) = \int f(x) \, dx + \int g(y) \, dy = C} \tag{1} $$

---

### Part (i): $V'(x) + 2y \frac{dy}{dx} = 0$
Here $f(x) = V'(x)$ and $g(y) = 2y$.
Applying formula $(1)$:
$$ \int V'(x) \, dx + \int 2y \, dy = C $$
By the Fundamental Theorem of Calculus:
$$ \int V'(x) \, dx = V(x) $$
$$ \int 2y \, dy = y^2 $$
$$ \mathbf{V(x) + y^2 = C} \tag{2} $$

*Aerospace / Mechanical Interpretation:* If $x$ is position and $y = \frac{\dot{x}}{\sqrt{2m}}$, this equation expresses the **conservation of total mechanical energy** in a conservative potential:
$$ E = \frac{1}{2} m \dot{x}^2 + V(x) = \text{constant} $$

---

### Part (ii): $\left( \frac{1}{y} - a \right) \frac{dy}{dx} + \frac{2}{x} - b = 0$, for $x, y > 0$
Write in differential form:
$$ \left( \frac{2}{x} - b \right) dx + \left( \frac{1}{y} - a \right) dy = 0 $$
Here:
$$ f(x) = \frac{2}{x} - b, \quad g(y) = \frac{1}{y} - a $$

Applying formula $(1)$:
$$ \int \left( \frac{2}{x} - b \right) dx + \int \left( \frac{1}{y} - a \right) dy = C $$
Since $x > 0$ and $y > 0$:
$$ \int \frac{2}{x} \, dx - \int b \, dx = 2\ln(x) - bx $$
$$ \int \frac{1}{y} \, dy - \int a \, dy = \ln(y) - ay $$

Summing the terms:
$$ 2\ln(x) - bx + \ln(y) - ay = C \tag{3} $$
Combine the logarithmic terms:
$$ \ln(x^2) + \ln(y) - (bx + ay) = C $$
$$ \ln\left( x^2 y \right) - (bx + ay) = C \tag{4} $$

Exponentiating both sides:
$$ \exp\left( \ln(x^2 y) - (bx + ay) \right) = e^C $$
$$ \mathbf{x^2 y \, e^{-(bx + ay)} = C_1} \tag{5} $$
where $C_1 = e^C > 0$.

*Ecological / Flight Dynamics Interpretation:* Equation $(5)$ defines the closed orbital trajectories (first integral) of the classical **Lotka-Volterra predator-prey system**, proving periodic oscillations around the coexistence equilibrium.

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Summary of Results:
* **General Proof:**
  $$ \frac{\partial M}{\partial y} = \frac{\partial}{\partial y}[f(x)] = 0 = \frac{\partial}{\partial x}[g(y)] = \frac{\partial N}{\partial x} \implies \text{Always Exact} $$
  General solution: $\mathbf{\int f(x) dx + \int g(y) dy = C}$.
* **(i) Solution:**
  $$ \mathbf{V(x) + y^2 = C} $$
* **(ii) Solution:**
  $$ \mathbf{2\ln x - bx + \ln y - ay = C \iff x^2 y \, e^{-(bx + ay)} = C_1} $$

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Ecuaciones Exactas y Factores Integrantes Especiales|Exact Equations Theory]]`
* `[[04 - Advanced Maths/Concepto - Metodos de Integracion Directa y Ecuaciones Separables|Separable Equations]]`
* `[[04 - Advanced Maths/Problema - Ch2-P4 Exact Differential Equations|Problem 2.4: Exact Equations]]`
