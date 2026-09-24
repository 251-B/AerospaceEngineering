---
materia: "Advanced Maths"
tema: "Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients"
origen: "ProblemsCh3.pdf — Exercise 11"
dificultad: media-alta
tags:
  - problema-resuelto
  - ecuacion-euler-cauchy
  - cambio-de-variable
  - regla-de-la-cadena
  - resonancia
---

# ✏️ Problem 3.11: Euler-Cauchy Equation via Exponential Transformation

## 📄 Enunciado (Problem Statement)

We consider the following second order ODE (Euler equation):
$$ x^2 y''(x) + p x y'(x) + q y(x) = g(x) $$
where $p, q$ are real constants and $x > 0$.

**(i)** By making the change of variable $x = e^z$ and using the chain rule, show that the ODE is transformed into one with constant coefficients in the variable $z$:
$$ \frac{d^2y}{dz^2} + (p - 1)\frac{dy}{dz} + q y = g(e^z) $$
**(ii)** Take $p = 3$, $q = -3$, and $g(x) = 4x$, make the previous transformation and compute the general solution.

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Structure:
- The given equation is a non-homogeneous **Euler-Cauchy differential equation** of order 2.
- The monomial pre-factors $x^2$ and $x$ have powers matching the derivative order ($y''$ and $y'$).
- Domain: $x \in (0, \infty)$, ensuring $z = \ln x$ is a smooth bijective diffeomorphism between $(0, \infty)$ and $(-\infty, \infty)$.
- In part (ii): $p = 3$, $q = -3$, $g(x) = 4x$.

---

## 🧠 2. Estrategia y Planteamiento Matemático (Phase 2)

### Plan for Part (i):
1. Express $z = \ln x \implies \frac{dz}{dx} = \frac{1}{x}$.
2. Apply the chain rule to the first derivative $\frac{dy}{dx} = \frac{dy}{dz}\frac{dz}{dx}$.
3. Differentiate once more with respect to $x$ using the product and chain rules to express $\frac{d^2 y}{dx^2}$ in terms of $\frac{dy}{dz}$ and $\frac{d^2 y}{dz^2}$.
4. Substitute $x y'(x)$ and $x^2 y''(x)$ into the Euler-Cauchy ODE and verify that all variable coefficients in $x$ cancel identically.

### Plan for Part (ii):
1. Substitute $p = 3, q = -3$ and $g(e^z) = 4e^z$ into the transformed ODE:
   $$ \frac{d^2 y}{dz^2} + 2 \frac{dy}{dz} - 3 y = 4 e^z $$
2. Solve the homogeneous auxiliary equation $r^2 + 2r - 3 = 0$.
3. Determine a particular solution $y_p(z)$ via undetermined coefficients (accounting for root resonance since $r = 1$ is already a homogeneous mode).
4. Combine into the general solution $y(z) = y_h(z) + y_p(z)$.
5. Invert the coordinate transformation using $z = \ln x$ to express $y(x)$.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Part (i): Chain Rule Derivation of the Transformation

Let $x = e^z$, so that $z = \ln x$ for $x > 0$.
The first derivative with respect to $x$ is:
$$ \frac{dz}{dx} = \frac{1}{x} $$

#### 1. Transformation of the First Derivative:
By the chain rule:
$$ \frac{dy}{dx} = \frac{dy}{dz} \frac{dz}{dx} = \frac{dy}{dz} \left( \frac{1}{x} \right) = \frac{1}{x} \frac{dy}{dz} $$
Multiplying both sides by $x$:
$$ \mathbf{x \frac{dy}{dx} = \frac{dy}{dz}} \tag{1} $$

#### 2. Transformation of the Second Derivative:
Differentiating $\frac{dy}{dx}$ with respect to $x$ using the product rule:
$$ \frac{d^2 y}{dx^2} = \frac{d}{dx}\left[ \frac{1}{x} \frac{dy}{dz} \right] = \left( \frac{d}{dx}\left(\frac{1}{x}\right) \right) \frac{dy}{dz} + \frac{1}{x} \left( \frac{d}{dx}\left(\frac{dy}{dz}\right) \right) $$
Compute each component:
* $\frac{d}{dx}\left(\frac{1}{x}\right) = -\frac{1}{x^2}$
* By the chain rule applied to $\frac{dy}{dz}$:
  $$ \frac{d}{dx}\left( \frac{dy}{dz} \right) = \frac{d}{dz}\left( \frac{dy}{dz} \right) \frac{dz}{dx} = \frac{d^2 y}{dz^2} \left( \frac{1}{x} \right) = \frac{1}{x} \frac{d^2 y}{dz^2} $$
Substituting these into the second derivative expression:
$$ \frac{d^2 y}{dx^2} = -\frac{1}{x^2} \frac{dy}{dz} + \frac{1}{x} \left( \frac{1}{x} \frac{d^2 y}{dz^2} \right) = \frac{1}{x^2} \left( \frac{d^2 y}{dz^2} - \frac{dy}{dz} \right) $$
Multiplying both sides by $x^2$:
$$ \mathbf{x^2 \frac{d^2 y}{dx^2} = \frac{d^2 y}{dz^2} - \frac{dy}{dz}} \tag{2} $$

#### 3. Substitution into the Euler-Cauchy ODE:
The original ODE is:
$$ x^2 y''(x) + p x y'(x) + q y(x) = g(x) $$
Substitute equations (1) and (2) into the differential equation, and note that $g(x) = g(e^z)$:
$$ \left( \frac{d^2 y}{dz^2} - \frac{dy}{dz} \right) + p \left( \frac{dy}{dz} \right) + q y = g(e^z) $$
Group terms by derivative orders of $y$ with respect to $z$:
$$ \mathbf{\frac{d^2 y}{dz^2} + (p - 1)\frac{dy}{dz} + q y = g(e^z)} \tag{3} $$
This is a linear second-order differential equation with constant coefficients in the independent variable $z$.

---

### Part (ii): Resolution for $p = 3, \; q = -3, \; g(x) = 4x$

#### Step 1: Formulate the Transformed ODE
Substitute the given values into equation (3):
- $p - 1 = 3 - 1 = 2$
- $q = -3$
- $g(e^z) = 4 e^z$
The ODE becomes:
$$ \mathbf{\frac{d^2 y}{dz^2} + 2 \frac{dy}{dz} - 3y = 4e^z} \tag{4} $$

#### Step 2: Homogeneous General Solution $y_h(z)$
Consider the homogeneous equation:
$$ \frac{d^2 y}{dz^2} + 2 \frac{dy}{dz} - 3y = 0 $$
The characteristic auxiliary polynomial is:
$$ r^2 + 2r - 3 = 0 $$
Factoring the quadratic polynomial:
$$ (r + 3)(r - 1) = 0 \implies r_1 = 1, \quad r_2 = -3 $$
The complementary homogeneous solution is:
$$ \mathbf{y_h(z) = c_1 e^z + c_2 e^{-3z}} \tag{5} $$

#### Step 3: Particular Solution $y_p(z)$ via Resonant Undetermined Coefficients
The forcing term is $F(z) = 4e^z$.  
Notice that the exponent $\alpha = 1$ in $e^{1\cdot z}$ is already a simple root of the auxiliary polynomial ($r_1 = 1$).  
Therefore, the standard trial $A e^z$ would be absorbed into the kernel $\ker(L)$.  
We must multiply by $z$ to account for **resonance**:
$$ y_p(z) = A z e^z \tag{6} $$

Compute first and second derivatives of $y_p(z)$:
$$ \frac{dy_p}{dz} = A \left( 1 \cdot e^z + z e^z \right) = A (1 + z) e^z $$
$$ \frac{d^2 y_p}{dz^2} = A \left( 1 \cdot e^z + (1 + z) e^z \right) = A (2 + z) e^z $$

Substitute $y_p, y_p', y_p''$ into the differential equation (4):
$$ A (2 + z) e^z + 2 A (1 + z) e^z - 3 A z e^z = 4 e^z $$
Factor out $A e^z$:
$$ A e^z \left[ (2 + z) + 2(1 + z) - 3z \right] = 4 e^z $$
Simplify the polynomial inside the bracket:
$$ 2 + z + 2 + 2z - 3z = 4 + (1 + 2 - 3)z = 4 + 0 \cdot z = 4 $$
The secular terms in $z$ cancel out cleanly:
$$ 4 A e^z = 4 e^z \implies 4A = 4 \implies \mathbf{A = 1} $$
Thus, the particular solution is:
$$ \mathbf{y_p(z) = z e^z} \tag{7} $$

#### Step 4: General Solution in Variable $z$
Combining complementary and particular solutions:
$$ y(z) = y_h(z) + y_p(z) = c_1 e^z + c_2 e^{-3z} + z e^z \tag{8} $$

#### Step 5: Back-Transformation to Original Physical Variable $x$
Recall that $x = e^z$ and $z = \ln x$:
* $e^z = x$
* $e^{-3z} = (e^z)^{-3} = x^{-3} = \frac{1}{x^3}$
* $z e^z = (\ln x) x = x \ln x$

Substituting into equation (8):
$$ \mathbf{y(x) = c_1 x + \frac{c_2}{x^3} + x \ln x} \tag{9} $$
where $c_1, c_2 \in \mathbb{R}$ are arbitrary constants, valid for all $x \in (0, \infty)$.

---

### Step 6: Rigorous Analytical Verification
Differentiate the final solution (9) and substitute back into the original Euler-Cauchy ODE:
$$ y(x) = c_1 x + c_2 x^{-3} + x \ln x $$
$$ y'(x) = c_1 - 3 c_2 x^{-4} + \ln x + 1 $$
$$ y''(x) = 12 c_2 x^{-5} + \frac{1}{x} $$

Form the left-hand side $L[y] = x^2 y'' + 3x y' - 3y$:
$$ x^2 y'' = x^2 \left( 12 c_2 x^{-5} + \frac{1}{x} \right) = 12 c_2 x^{-3} + x $$
$$ 3x y' = 3x \left( c_1 - 3 c_2 x^{-4} + \ln x + 1 \right) = 3 c_1 x - 9 c_2 x^{-3} + 3x \ln x + 3x $$
$$ -3y = -3 \left( c_1 x + c_2 x^{-3} + x \ln x \right) = -3 c_1 x - 3 c_2 x^{-3} - 3x \ln x $$

Summing all terms:
- Coefficient of $c_2 x^{-3}$: $12 - 9 - 3 = 0$.
- Coefficient of $c_1 x$: $3 - 3 = 0$.
- Coefficient of $x \ln x$: $3 - 3 = 0$.
- Remaining terms in $x$: $x + 3x = 4x$.

$$ L[y] = 4x \equiv g(x) $$
The solution is verified beyond any doubt.

---

## 🎯 4. Resultado Final y Síntesis (Phase 4)

### Master Formulas:
$$ \boxed{\frac{d^2 y}{dz^2} + (p - 1)\frac{dy}{dz} + q y = g(e^z)} $$
$$ \boxed{y(x) = c_1 x + \frac{c_2}{x^3} + x \ln x, \quad x > 0} $$

### Aerospace Engineering Applications:
- Euler-Cauchy differential equations frequently arise in axisymmetric elasticity (thick-walled aircraft pressurized cylinders, Lamé problems), radial heat diffusion in rocket nozzles, and potential flow around circular airfoils where coordinate transformations from polar radii $r$ map naturally to logarithmic space $\ln r$.

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Ecuaciones Homogeneas con Coeficientes Constantes y Ecuacion Caracteristica|Ecuaciones Homogéneas]]`
* `[[04 - Advanced Maths/Concepto - Operador Lineal y Principio de Superposicion|Operador Lineal y Superposición]]`
* `[[04 - Advanced Maths/Problema - Ch3-P4 Second Order Homogeneous Linear ODEs with IVPs|Problem 3.4: Homogeneous Linear ODEs]]`
* `[[04 - Advanced Maths/Matematicas Avanzadas MOC|⬅️ Central Advanced Maths MOC]]`
