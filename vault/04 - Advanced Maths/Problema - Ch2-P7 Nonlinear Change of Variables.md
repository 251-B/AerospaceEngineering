---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.7"
dificultad: media
tags:
  - problema-resuelto
  - sustituciones-no-lineales
  - linealizacion
  - pvi
---

# ✏️ Problem 2.7: Nonlinear Change of Variables

## 📄 Enunciado (Problem Statement)

We consider the following initial value problem:
$$ y'(x) = y(x) + \frac{x}{y(x)}, \quad y(0) = 1 $$
Make the change of variable $z(x) = y(x)^2$ and find the solution.

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Structure:
* **Given ODE:** $y'(x) = y(x) + \frac{x}{y(x)}$. This is a **nonlinear** first-order ODE due to the denominator $\frac{1}{y(x)}$ (or equivalently, $y y' - y^2 = x$, a Bernoulli-type equation with power $\alpha = -1$).
* **Initial Condition:** $y(0) = 1 > 0$.
* **Prescribed Transformation:** $z(x) \equiv [y(x)]^2$.

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

1. Compute the derivative of the transformation $z(x) = y(x)^2$ with respect to $x$ using the chain rule: $z'(x) = 2 y(x) y'(x)$.
2. Multiply the original ODE by $2 y(x)$ to isolate $2 y y'$ on the left-hand side.
3. Substitute $z$ and $z'$ to obtain a standard first-order **linear inhomogeneous ODE** for $z(x)$.
4. Transform the initial condition: $z(0) = [y(0)]^2 = 1$.
5. Solve the linear equation for $z(x)$ using an integrating factor $\mu(x) = e^{-2x}$.
6. Revert the substitution $y(x) = \pm\sqrt{z(x)}$, selecting the positive branch to satisfy $y(0) = 1$.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Step 1: Derivative of the Substitution
Given:
$$ z(x) = [y(x)]^2 \tag{1} $$
Differentiating both sides with respect to $x$ via the chain rule:
$$ \frac{dz}{dx} = 2 y(x) \frac{dy}{dx} \tag{2} $$

---

### Step 2: Algebraic Reduction to a Linear Equation
The original differential equation is:
$$ \frac{dy}{dx} = y + \frac{x}{y} $$

Multiply both sides by $2y(x)$ (valid for $y(x) \neq 0$):
$$ 2y \frac{dy}{dx} = 2y \left( y + \frac{x}{y} \right) = 2y^2 + 2x \tag{3} $$

Substitute $(1)$ ($y^2 = z$) and $(2)$ ($2y y' = z'$) into $(3)$:
$$ \frac{dz}{dx} = 2z + 2x $$
Rearranging into standard linear form:
$$ \mathbf{\frac{dz}{dx} - 2z = 2x} \tag{4} $$

---

### Step 3: Transformation of the Initial Condition
Using $y(0) = 1$:
$$ z(0) = [y(0)]^2 = 1^2 = 1 \tag{5} $$

We now have the linear IVP:
$$ \begin{cases} z'(x) - 2z(x) = 2x \\ z(0) = 1 \end{cases} $$

---

### Step 4: Solving the Linear ODE via Integrating Factor
For equation $(4)$, $p(x) = -2$ and $q(x) = 2x$.
The integrating factor is:
$$ \mu(x) = \exp\left( \int -2 \, dx \right) = e^{-2x} $$

Multiply $(4)$ by $e^{-2x}$:
$$ e^{-2x} \frac{dz}{dx} - 2e^{-2x} z = 2x e^{-2x} $$
Recognize the exact derivative of the product:
$$ \frac{d}{dx} \left[ z(x) e^{-2x} \right] = 2x e^{-2x} \tag{6} $$

Integrate both sides with respect to $x$:
$$ z(x) e^{-2x} = \int 2x e^{-2x} \, dx + C \tag{7} $$

#### Integration by Parts:
Let $u = 2x \implies du = 2 dx$, and $dv = e^{-2x} dx \implies v = -\frac{1}{2} e^{-2x}$:
$$ \int 2x e^{-2x} \, dx = (2x)\left( -\frac{1}{2} e^{-2x} \right) - \int \left( -\frac{1}{2} e^{-2x} \right) (2 \, dx) $$
$$ = -x e^{-2x} + \int e^{-2x} \, dx = -x e^{-2x} - \frac{1}{2} e^{-2x} $$

Substitute back into $(7)$:
$$ z(x) e^{-2x} = -x e^{-2x} - \frac{1}{2} e^{-2x} + C $$

Multiply through by $e^{2x}$:
$$ z(x) = -x - \frac{1}{2} + C e^{2x} \tag{8} $$

---

### Step 5: Enforcing the Initial Condition $z(0) = 1$
Substitute $x = 0$ and $z = 1$ into $(8)$:
$$ 1 = -0 - \frac{1}{2} + C e^0 $$
$$ 1 = -\frac{1}{2} + C \implies C = 1 + \frac{1}{2} = \frac{3}{2} $$

Therefore:
$$ \mathbf{z(x) = \frac{3}{2} e^{2x} - x - \frac{1}{2}} \tag{9} $$

---

### Step 6: Recovery of the Original Variable $y(x)$
From equation $(1)$, $y(x) = \pm\sqrt{z(x)}$.
Since the initial condition is $y(0) = +1 > 0$, continuity requires selecting the positive branch:
$$ \mathbf{y(x) = \sqrt{\frac{3}{2} e^{2x} - x - \frac{1}{2}}} \tag{10} $$

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Final Explicit Solution:
$$ \mathbf{y(x) = \sqrt{\frac{3}{2} e^{2x} - x - \frac{1}{2}}} $$

### Verification:
1. **Initial Condition Check:**
   $$ y(0) = \sqrt{\frac{3}{2} e^0 - 0 - \frac{1}{2}} = \sqrt{\frac{3}{2} - \frac{1}{2}} = \sqrt{1} = 1 \quad \checkmark $$
2. **Differential Equation Check:**
   Let $g(x) = \frac{3}{2} e^{2x} - x - \frac{1}{2}$. Then $y = g^{1/2}$ and $y' = \frac{g'}{2\sqrt{g}} = \frac{3e^{2x} - 1}{2 y}$.
   Evaluate the RHS:
   $$ y + \frac{x}{y} = \frac{y^2 + x}{y} = \frac{\left( \frac{3}{2}e^{2x} - x - \frac{1}{2} \right) + x}{y} = \frac{\frac{3}{2}e^{2x} - \frac{1}{2}}{y} = \frac{3e^{2x} - 1}{2y} $$
   LHS and RHS match identically!

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Sustituciones No Lineales y Ecuacion de Bernoulli|Nonlinear Substitutions Theory]]`
* `[[04 - Advanced Maths/Problema - Ch2-P8 General Bernoulli Equation Reduction|Problem 2.8: General Bernoulli Reduction]]`
