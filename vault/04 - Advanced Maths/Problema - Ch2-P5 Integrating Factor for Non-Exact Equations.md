---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.5"
dificultad: media
tags:
  - problema-resuelto
  - factor-integrante-especial
  - ecuaciones-no-exactas
  - funcion-potencial
---

# ✏️ Problem 2.5: Integrating Factor for Non-Exact Equations

## 📄 Enunciado (Problem Statement)

Find an integrating factor depending only on $x$ that makes the equation:
$$ (3xy + y^2) + (x^2 + xy) \frac{dy}{dx} = 0 $$
exact, and find its solution.

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Structure:
The differential equation is written in differential form:
$$ M(x, y) \, dx + N(x, y) \, dy = 0 $$
with:
$$ M(x, y) = 3xy + y^2, \quad N(x, y) = x^2 + xy $$

### Objective:
1. Show that the equation is not exact in its current form.
2. Determine an integrating factor $\mu = \mu(x)$ depending solely on $x$.
3. Multiply the equation by $\mu(x)$, verify exactness of the new system, and compute the potential function $F(x, y) = C$.

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

1. Compute $\frac{\partial M}{\partial y}$ and $\frac{\partial N}{\partial x}$ to demonstrate non-exactness.
2. Form the difference $\frac{\partial M}{\partial y} - \frac{\partial N}{\partial x}$.
3. Check if $\frac{M_y - N_x}{N}$ depends exclusively on $x$.
4. Calculate the integrating factor via $\mu(x) = \exp\left( \int \frac{M_y - N_x}{N} dx \right)$.
5. Multiply the equation by $\mu(x)$ and reconstruct the potential function $F(x, y)$ such that $\nabla F = (\mu M, \mu N)$.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Step 1: Verification of Non-Exactness
Compute the partial derivatives:
$$ \frac{\partial M}{\partial y} = \frac{\partial}{\partial y}(3xy + y^2) = 3x + 2y $$
$$ \frac{\partial N}{\partial x} = \frac{\partial}{\partial x}(x^2 + xy) = 2x + y $$

Comparing the two expressions:
$$ \frac{\partial M}{\partial y} - \frac{\partial N}{\partial x} = (3x + 2y) - (2x + y) = x + y \neq 0 $$
Because $\frac{\partial M}{\partial y} \neq \frac{\partial N}{\partial x}$, the equation is **not exact**.

---

### Step 2: Derivation of the Integrating Factor $\mu(x)$
An integrating factor depending only on $x$ exists if and only if the ratio $\frac{M_y - N_x}{N}$ is a function solely of $x$:
$$ \frac{\frac{\partial M}{\partial y} - \frac{\partial N}{\partial x}}{N} = \frac{x + y}{x^2 + xy} $$

Factor the denominator $N(x, y) = x(x + y)$:
$$ \frac{x + y}{x(x + y)} = \frac{1}{x} \quad (\text{for } x + y \neq 0) $$
This ratio depends strictly and solely on $x$:
$$ \phi(x) = \frac{1}{x} $$

Compute the integrating factor:
$$ \mu(x) = \exp\left( \int \phi(x) \, dx \right) = \exp\left( \int \frac{1}{x} \, dx \right) = \exp(\ln|x|) = |x| $$
Selecting the positive branch for $x > 0$:
$$ \mathbf{\mu(x) = x} \tag{1} $$

---

### Step 3: Formulation of the Exact System
Multiply the entire original differential equation by $\mu(x) = x$:
$$ x (3xy + y^2) \, dx + x (x^2 + xy) \, dy = 0 $$
$$ \tilde{M}(x, y) \, dx + \tilde{N}(x, y) \, dy = 0 $$
where:
$$ \tilde{M}(x, y) = 3x^2 y + x y^2 $$
$$ \tilde{N}(x, y) = x^3 + x^2 y $$

#### Verification of Exactness:
$$ \frac{\partial \tilde{M}}{\partial y} = \frac{\partial}{\partial y}(3x^2 y + x y^2) = 3x^2 + 2xy $$
$$ \frac{\partial \tilde{N}}{\partial x} = \frac{\partial}{\partial x}(x^3 + x^2 y) = 3x^2 + 2xy $$
Since $\frac{\partial \tilde{M}}{\partial y} = \frac{\partial \tilde{N}}{\partial x} = 3x^2 + 2xy$, **the transformed equation is exact**.

---

### Step 4: Reconstruction of the Potential Function $F(x, y)$
Integrate $\tilde{M}(x, y)$ with respect to $x$:
$$ F(x, y) = \int \tilde{M}(x, y) \, dx = \int (3x^2 y + x y^2) \, dx $$
$$ F(x, y) = 3y \left( \frac{x^3}{3} \right) + y^2 \left( \frac{x^2}{2} \right) + h(y) = x^3 y + \frac{1}{2} x^2 y^2 + h(y) \tag{2} $$

Differentiate $F(x, y)$ with respect to $y$ and equate to $\tilde{N}(x, y)$:
$$ \frac{\partial F}{\partial y} = x^3 + x^2 y + h'(y) = \tilde{N}(x, y) = x^3 + x^2 y $$

Subtract $x^3 + x^2 y$ from both sides:
$$ h'(y) = 0 \implies h(y) = 0 $$

Thus, the potential function is:
$$ F(x, y) = x^3 y + \frac{1}{2} x^2 y^2 $$

The general solution is given by $F(x, y) = C$:
$$ \mathbf{x^3 y + \frac{1}{2} x^2 y^2 = C} \tag{3} $$
Multiplying by $2$ to clear fractions:
$$ \mathbf{2 x^3 y + x^2 y^2 = C_1} \tag{4} $$

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Final Answers:
* **Integrating Factor:**
  $$ \mathbf{\mu(x) = x} $$
* **General Implicit Solution:**
  $$ \mathbf{x^3 y + \frac{1}{2} x^2 y^2 = C \iff x^2 y \left( x + \frac{1}{2} y \right) = C} $$

### Verification by Implicit Differentiation:
Differentiate $2 x^3 y + x^2 y^2 = C_1$ with respect to $x$:
$$ \frac{d}{dx}\left[ 2 x^3 y + x^2 y^2 \right] = 0 $$
$$ \left( 6 x^2 y + 2 x y^2 \right) + \left( 2 x^3 + 2 x^2 y \right) \frac{dy}{dx} = 0 $$
Divide the entire equation by $2x$:
$$ (3xy + y^2) + (x^2 + xy) \frac{dy}{dx} = 0 $$
which recovers the original non-exact ODE identically.

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Ecuaciones Exactas y Factores Integrantes Especiales|Special Integrating Factors]]`
* `[[04 - Advanced Maths/Problema - Ch2-P4 Exact Differential Equations|Problem 2.4: Exact Equations]]`
