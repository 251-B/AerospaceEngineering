---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.8"
dificultad: media
tags:
  - problema-resuelto
  - ecuacion-bernoulli
  - reduccion-lineal
  - cambio-variable
---

# ✏️ Problem 2.8: General Bernoulli Equation Reduction

## 📄 Enunciado (Problem Statement)

Show that the Bernoulli equation:
$$ y'(x) = a(x) y(x) + b(x) y(x)^\alpha $$
where $\alpha \neq 0, 1$, can be transformed into a linear ODE with the change of variable $z(x) = y(x)^{1 - \alpha}$ and find the solution. What happens if $\alpha = 0$ or $\alpha = 1$?

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Structure:
* **Bernoulli ODE:** $\frac{dy}{dx} - a(x) y = b(x) y^\alpha$.
* **Coefficient functions:** $a(x), b(x) \in C^0(I)$.
* **Parameter:** Exponent $\alpha \in \mathbb{R}$.
* **Prescribed Transformation:** $z(x) \equiv [y(x)]^{1 - \alpha}$.

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

1. For $\alpha \neq 0, 1$, the equation is nonlinear due to $y^\alpha$.
2. Divide the ODE by $y^\alpha$ to create the leading term $y^{-\alpha} y'$.
3. Differentiate the proposed transformation $z(x) = y^{1-\alpha}$ using the chain rule:
   $$ z'(x) = (1 - \alpha) y^{-\alpha} y'(x) \implies y^{-\alpha} y' = \frac{z'}{1 - \alpha} $$
4. Substitute $z$ and $z'$ into the equation to yield a standard first-order **linear ODE** in $z(x)$.
5. Formulate the general solution for $z(x)$ using an integrating factor and invert to obtain $y(x) = [z(x)]^{\frac{1}{1-\alpha}}$.
6. Analyze the degenerate cases $\alpha = 0$ and $\alpha = 1$, demonstrating why they are already linear without transformation.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Step 1: Algebraic Division by $y^\alpha$
Starting from:
$$ \frac{dy}{dx} - a(x) y = b(x) y^\alpha \tag{1} $$

Assuming $y(x) \neq 0$, divide both sides of $(1)$ by $y^\alpha$:
$$ y^{-\alpha} \frac{dy}{dx} - a(x) \frac{y}{y^\alpha} = b(x) $$
Using laws of exponents $\frac{y}{y^\alpha} = y^{1 - \alpha}$:
$$ y^{-\alpha} \frac{dy}{dx} - a(x) y^{1 - \alpha} = b(x) \tag{2} $$

---

### Step 2: Differentiation of the Substitution $z(x)$
Define the new dependent variable:
$$ z(x) \equiv [y(x)]^{1 - \alpha} \tag{3} $$

Differentiating with respect to $x$ via the chain rule:
$$ \frac{dz}{dx} = \frac{d}{dx}\left[ y(x)^{1 - \alpha} \right] = (1 - \alpha) y(x)^{(1 - \alpha) - 1} \frac{dy}{dx} $$
$$ \frac{dz}{dx} = (1 - \alpha) y(x)^{-\alpha} \frac{dy}{dx} \tag{4} $$

Since $\alpha \neq 1$, the factor $(1 - \alpha) \neq 0$. Dividing equation $(4)$ by $(1 - \alpha)$:
$$ y^{-\alpha} \frac{dy}{dx} = \frac{1}{1 - \alpha} \frac{dz}{dx} \tag{5} $$

---

### Step 3: Linearized Differential Equation in $z(x)$
Substitute $(3)$ and $(5)$ directly into $(2)$:
$$ \frac{1}{1 - \alpha} \frac{dz}{dx} - a(x) z(x) = b(x) $$

Multiply the entire equation by the non-zero scalar $(1 - \alpha)$:
$$ \mathbf{\frac{dz}{dx} - (1 - \alpha) a(x) z(x) = (1 - \alpha) b(x)} \tag{6} $$

Equation $(6)$ is in canonical linear standard form $z' + P(x) z = Q(x)$ with:
$$ P(x) = -(1 - \alpha) a(x), \quad Q(x) = (1 - \alpha) b(x) $$
This completes the proof of linear transformation. $\blacksquare$

---

### Step 4: Analytical General Solution
1. **Integrating Factor for $z(x)$:**
   $$ \mu(x) = \exp\left( \int -(1 - \alpha) a(x) \, dx \right) = \exp\left( (\alpha - 1) \int a(x) \, dx \right) \tag{7} $$
2. **Total Derivative:**
   $$ \frac{d}{dx} \left[ z(x) \mu(x) \right] = (1 - \alpha) b(x) \mu(x) $$
3. **Quadrature:**
   $$ z(x) = \frac{1}{\mu(x)} \left[ (1 - \alpha) \int b(x) \mu(x) \, dx + C \right] \tag{8} $$
4. **Recovery of Original Variable $y(x)$:**
   Since $z = y^{1 - \alpha}$:
   $$ \mathbf{y(x) = \left\{ \frac{1}{\mu(x)} \left[ (1 - \alpha) \int b(x) \mu(x) \, dx + C \right] \right\}^{\frac{1}{1 - \alpha}}} \tag{9} $$
   *(In addition, if $\alpha > 0$, the trivial function $y(x) \equiv 0$ is also a solution).*

---

### Step 5: Analysis of Cases $\alpha = 0$ and $\alpha = 1$

#### Case $\alpha = 0$:
Substitute $\alpha = 0$ into equation $(1)$:
$$ y'(x) = a(x) y(x) + b(x) y^0 $$
Since $y^0 = 1$:
$$ \mathbf{y'(x) - a(x) y(x) = b(x)} \tag{10} $$
* **Conclusion:** The equation is **already a linear non-homogeneous first-order ODE**. No nonlinear transformation is needed. The integrating factor is $\mu(x) = \exp\left(-\int a(x) dx\right)$.

#### Case $\alpha = 1$:
Substitute $\alpha = 1$ into equation $(1)$:
$$ y'(x) = a(x) y(x) + b(x) y^1 = [a(x) + b(x)] y(x) $$
Rearranging:
$$ \mathbf{y'(x) - [a(x) + b(x)] y(x) = 0} \tag{11} $$
* **Conclusion:** The equation is **already a linear homogeneous first-order ODE**. It is separable and solved directly by:
  $$ \frac{dy}{y} = [a(x) + b(x)] dx \implies y(x) = C \exp\left( \int [a(x) + b(x)] \, dx \right) $$

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Master Summary:
* **Transformation:** $z = y^{1-\alpha}$ reduces Bernoulli's equation to:
  $$ \mathbf{z' - (1 - \alpha) a(x) z = (1 - \alpha) b(x)} $$
* **General Solution:**
  $$ \mathbf{y(x) = [z(x)]^{\frac{1}{1 - \alpha}}} $$
* **Special Cases:**
  * **$\alpha = 0$:** Linear inhomogeneous ODE: $y' - ay = b$.
  * **$\alpha = 1$:** Linear homogeneous ODE: $y' - (a + b)y = 0$.

### Aerospace Engineering Applications:
* **Aerodynamic Drag:** When an aircraft or projectile travels at high speed, aerodynamic drag is quadratic in velocity ($F_D \propto v^2$). Newton's law gives $m \dot{v} = T - c_D v^2$, which is a Bernoulli equation with $\alpha = 2$. Setting $z = v^{1-2} = v^{-1}$ transforms the quadratic drag equation into a linear ODE for momentum inverse.

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Sustituciones No Lineales y Ecuacion de Bernoulli|Bernoulli Equation Theory]]`
* `[[04 - Advanced Maths/Problema - Ch2-P7 Nonlinear Change of Variables|Problem 2.7: Nonlinear Substitution]]`
