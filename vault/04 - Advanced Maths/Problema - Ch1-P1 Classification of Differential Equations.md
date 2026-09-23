---
materia: "Advanced Mathematics"
tema: "Tema 1: Introduction, Modeling and Classification of ODEs"
origen: "ProblemsCh1.pdf — Exercise 1.1"
dificultad: media
tags:
  - problema-resuelto
  - clasificacion
  - edo
  - edp
  - linealidad
  - orden
---

# ✏️ Problem 1.1: Classification of Differential Equations

## 📄 Enunciado (Problem Statement)

Classify the following equations as ordinary or partial; give their order; and state whether they are linear or nonlinear. In each case identify the dependent and independent variables:

(i) **Bessel's equation** ($\nu$ is a parameter):
$$ x^2 y'' + x y' + (x^2 - \nu^2)y = 0 $$

(ii) **Burgers' equation** ($\nu$ is a parameter):
$$ \frac{\partial u}{\partial t} - \nu \frac{\partial^2 u}{\partial x^2} + u \frac{\partial u}{\partial x} = 0 $$

(iii) **Duffing's equation** ($m, k, a, b$ are parameters):
$$ m \ddot{x} + k x = a x - b x^3 $$

(iv)
$$ \frac{dy}{dt} = t - y^2 $$

(v) **The wave equation** ($c$ is a parameter):
$$ \frac{\partial^2 y}{\partial t^2} = c^2 \frac{\partial^2 y}{\partial x^2} $$

(vi) **Newton's law of cooling** ($k$ is a parameter and $T_A(t)$ is a specified function):
$$ \frac{dT}{dt} = -k(T - T_A(t)) $$

(vii) **The logistic population model** ($k$ is a parameter):
$$ \frac{dp}{dt} = k p (1 - p) $$

(viii) **Newton's second law** for a particle of mass $m$ moving in a potential $V(x)$:
$$ m \ddot{x} = -V'(x) $$

(ix) **The coupled equations**:
$$ \dot{x} = x(4 - 2x - y), \quad \dot{y} = y(9 - 3x - 3y) $$

(x)
$$ \frac{d\mathbf{x}}{dt} = A\mathbf{x} $$
where $\mathbf{x}$ is an $n$-component vector and $A$ is an $n \times n$ matrix.

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Criteria for Classification:
1. **Type:**
   * **ODE (Ordinary Differential Equation):** A single independent variable. All derivatives are ordinary ($\frac{d}{dx}, \frac{d}{dt}, '$, or $\dot{ }$).
   * **PDE (Partial Differential Equation):** Two or more independent variables. Derivatives are partial ($\frac{\partial}{\partial t}, \frac{\partial}{\partial x}, \dots$).
2. **Order:** The highest derivative order appearing anywhere in the equation.
3. **Dependent vs. Independent Variables:**
   * **Independent variable(s):** The variable(s) with respect to which differentiation is performed.
   * **Dependent variable(s):** The unknown function(s) being differentiated.
4. **Linearity Criterion (Official UC3M Cátedra Formulation):**
   An equation is **linear** if it can be written as:
   $$ \sum_{j=0}^n a_j(x) y^{(j)}(x) = b(x) $$
   where the dependent variable $y$ and all its derivatives appear to the first power, are not multiplied together, and are not arguments of nonlinear functions. The coefficients $a_j(x)$ and forcing term $b(x)$ may depend arbitrarily on the independent variable $x$.

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

For each of the 10 equations:
1. Identify all variables and differentiate parameters (constants) from true variables.
2. Count the independent variables to establish ODE vs. PDE.
3. Locate the highest derivative to determine the order.
4. Test the linearity of the operator by examining whether the dependent variable or its derivatives appear with powers $\neq 1$, in products with each other, or inside transcendental functions.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### (i) Bessel's Equation: $x^2 y'' + x y' + (x^2 - \nu^2)y = 0$
* **Independent variable:** $x$ (single variable $\implies$ **ODE**).
* **Dependent variable:** $y = y(x)$.
* **Order:** Highest derivative is $y'' = \frac{d^2 y}{dx^2} \implies$ **Order 2**.
* **Linearity Test:** Compare with canonical form $a_2(x)y'' + a_1(x)y' + a_0(x)y = b(x)$:
  $$ a_2(x) = x^2, \quad a_1(x) = x, \quad a_0(x) = x^2 - \nu^2, \quad b(x) = 0 $$
  The dependent variable $y$ and its derivatives $y', y''$ appear linearly.
* **Conclusion:** **Linear ODE of 2nd order**.

---

### (ii) Burgers' Equation: $\frac{\partial u}{\partial t} - \nu \frac{\partial^2 u}{\partial x^2} + u \frac{\partial u}{\partial x} = 0$
* **Independent variables:** $t$ and $x$ (two independent variables $\implies$ **PDE**).
* **Dependent variable:** $u = u(x, t)$.
* **Order:** Derivatives present are $\frac{\partial u}{\partial t}$ (order 1), $\frac{\partial u}{\partial x}$ (order 1), and $\frac{\partial^2 u}{\partial x^2}$ (order 2). Highest derivative is $\frac{\partial^2 u}{\partial x^2} \implies$ **Order 2**.
* **Linearity Test:** The convective term $u \frac{\partial u}{\partial x}$ is a product of the dependent variable $u$ and its partial derivative $\frac{\partial u}{\partial x}$. This product violates linearity:
  $$ \mathcal{L}[c u] = c u \cdot c \frac{\partial u}{\partial x} = c^2 \left( u \frac{\partial u}{\partial x} \right) \neq c \, \mathcal{L}[u] $$
* **Conclusion:** **Nonlinear PDE of 2nd order**.

---

### (iii) Duffing's Equation: $m \ddot{x} + k x = a x - b x^3$
* **Notation:** Overdots denote differentiation with respect to time $t$: $\ddot{x} = \frac{d^2 x}{dt^2}$.
* **Independent variable:** $t$ (single variable $\implies$ **ODE**).
* **Dependent variable:** $x = x(t)$. (Parameters: $m, k, a, b \in \mathbb{R}$).
* **Order:** Highest derivative is $\ddot{x} \implies$ **Order 2**.
* **Linearity Test:** Rearranging to standard form:
  $$ m \ddot{x} + (k - a) x + b x^3 = 0 $$
  If $b \neq 0$, the cubic term $x^3$ is a nonlinear function of the dependent variable $x$.
* **Conclusion:** **Nonlinear ODE of 2nd order** (if $b \neq 0$; reduces to linear if $b = 0$).

---

### (iv) First-Order Riccati Type: $\frac{dy}{dt} = t - y^2$
* **Independent variable:** $t$ (single variable $\implies$ **ODE**).
* **Dependent variable:** $y = y(t)$.
* **Order:** Highest derivative is $\frac{dy}{dt} \implies$ **Order 1**.
* **Linearity Test:** Rearranging:
  $$ \frac{dy}{dt} + y^2 = t $$
  The term $y^2$ involves the dependent variable raised to the power 2.
* **Conclusion:** **Nonlinear ODE of 1st order**.

---

### (v) The Wave Equation: $\frac{\partial^2 y}{\partial t^2} = c^2 \frac{\partial^2 y}{\partial x^2}$
* **Independent variables:** $t$ and $x$ (two independent variables $\implies$ **PDE**).
* **Dependent variable:** $y = y(x, t)$ (representing transverse displacement).
* **Order:** Derivatives are $\frac{\partial^2 y}{\partial t^2}$ and $\frac{\partial^2 y}{\partial x^2} \implies$ **Order 2**.
* **Linearity Test:**
  $$ \frac{\partial^2 y}{\partial t^2} - c^2 \frac{\partial^2 y}{\partial x^2} = 0 $$
  The differential operator $L[y] = \frac{\partial^2 y}{\partial t^2} - c^2 \frac{\partial^2 y}{\partial x^2}$ is purely linear: $L[c_1 y_1 + c_2 y_2] = c_1 L[y_1] + c_2 L[y_2]$.
* **Conclusion:** **Linear PDE of 2nd order**.

---

### (vi) Newton's Law of Cooling: $\frac{dT}{dt} = -k(T - T_A(t))$
* **Independent variable:** $t$ (single variable $\implies$ **ODE**).
* **Dependent variable:** $T = T(t)$ (temperature).
* **Parameters / Functions:** $k$ is a constant parameter; $T_A(t)$ is an externally prescribed ambient temperature function of time.
* **Order:** Highest derivative is $\frac{dT}{dt} \implies$ **Order 1**.
* **Linearity Test:** Rearranging:
  $$ \frac{dT}{dt} + k T = k T_A(t) $$
  Matching $a_1(t) \frac{dT}{dt} + a_0(t) T = b(t)$ with $a_1(t) = 1$, $a_0(t) = k$, and $b(t) = k T_A(t)$.
* **Conclusion:** **Linear ODE of 1st order**.

---

### (vii) The Logistic Population Model: $\frac{dp}{dt} = k p (1 - p)$
* **Independent variable:** $t$ (single variable $\implies$ **ODE**).
* **Dependent variable:** $p = p(t)$ (normalized population).
* **Order:** Highest derivative is $\frac{dp}{dt} \implies$ **Order 1**.
* **Linearity Test:** Expanding the right-hand side:
  $$ \frac{dp}{dt} - k p + k p^2 = 0 $$
  The quadratic term $k p^2$ is nonlinear in $p$.
* **Conclusion:** **Nonlinear ODE of 1st order**.

---

### (viii) Newton's Second Law in a Potential: $m \ddot{x} = -V'(x)$
* **Independent variable:** $t$ (single variable $\implies$ **ODE**).
* **Dependent variable:** $x = x(t)$ (position).
* **Order:** Highest derivative is $\ddot{x} = \frac{d^2 x}{dt^2} \implies$ **Order 2**.
* **Linearity Test:** In general, the potential energy $V(x)$ is an arbitrary smooth function, making the force $F(x) = -V'(x)$ a nonlinear function of position $x$ (e.g., gravitational potential $V(x) = -G M m / x \implies V'(x) \propto 1/x^2$, or pendulum $V(\theta) = -mg l \cos\theta \implies V' \propto \sin\theta$). The equation is linear **only** in the special case of a harmonic potential $V(x) = \frac{1}{2}\kappa x^2 \implies -V'(x) = -\kappa x$.
* **Conclusion:** **Nonlinear ODE of 2nd order** (in the general case).

---

### (ix) Coupled Competing Species / Predator-Prey System:
$$ \dot{x} = x(4 - 2x - y), \quad \dot{y} = y(9 - 3x - 3y) $$
* **Independent variable:** $t$ (single variable $\implies$ **System of ODEs**).
* **Dependent variables:** $x = x(t)$ and $y = y(t)$ (two coupled dependent state variables).
* **Order:** Highest derivative in each equation is 1st-order ($\dot{x}, \dot{y} \implies$ **Order 1**).
* **Linearity Test:** Expanding:
  $$ \dot{x} = 4x - 2x^2 - xy $$
  $$ \dot{y} = 9y - 3xy - 3y^2 $$
  The system contains quadratic self-interaction terms ($x^2, y^2$) and bilinear cross-coupling terms ($xy$).
* **Conclusion:** **Nonlinear system of ODEs of 1st order**.

---

### (x) Linear Vector System: $\frac{d\mathbf{x}}{dt} = A\mathbf{x}$
* **Independent variable:** $t$ (single variable $\implies$ **System of ODEs**).
* **Dependent variables:** $\mathbf{x}(t) = [x_1(t), x_2(t), \dots, x_n(t)]^T \in \mathbb{R}^n$ ($n$ coupled dependent variables).
* **Order:** Highest derivative is $\frac{d\mathbf{x}}{dt} \implies$ **Order 1**.
* **Linearity Test:** Matrix multiplication is a linear operator: $A(c_1 \mathbf{x}_1 + c_2 \mathbf{x}_2) = c_1 A\mathbf{x}_1 + c_2 A\mathbf{x}_2$. In component form:
  $$ \frac{dx_i}{dt} = \sum_{j=1}^n A_{ij} x_j \iff \frac{dx_i}{dt} - \sum_{j=1}^n A_{ij} x_j = 0 $$
  Every component $x_j$ appears strictly to the first power with constant coefficients $A_{ij}$.
* **Conclusion:** **Linear system of ODEs of 1st order**.

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Master Classification Summary Table

| Item | Equation | Type | Order | Linearity | Dependent Var(s) | Independent Var(s) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **(i)** | $x^2 y'' + xy' + (x^2-\nu^2)y = 0$ | **ODE** | **2** | **Linear** | $y$ | $x$ |
| **(ii)** | $u_t - \nu u_{xx} + u u_x = 0$ | **PDE** | **2** | **Nonlinear** | $u$ | $t, x$ |
| **(iii)** | $m \ddot{x} + kx = ax - bx^3$ | **ODE** | **2** | **Nonlinear** | $x$ | $t$ |
| **(iv)** | $y' = t - y^2$ | **ODE** | **1** | **Nonlinear** | $y$ | $t$ |
| **(v)** | $y_{tt} = c^2 y_{xx}$ | **PDE** | **2** | **Linear** | $y$ | $t, x$ |
| **(vi)** | $T' = -k(T - T_A(t))$ | **ODE** | **1** | **Linear** | $T$ | $t$ |
| **(vii)** | $p' = kp(1-p)$ | **ODE** | **1** | **Nonlinear** | $p$ | $t$ |
| **(viii)** | $m \ddot{x} = -V'(x)$ | **ODE** | **2** | **Nonlinear** | $x$ | $t$ |
| **(ix)** | $\dot{x}=x(4-2x-y), \; \dot{y}=y(9-3x-3y)$ | **ODE (System)** | **1** | **Nonlinear** | $x, y$ | $t$ |
| **(x)** | $\dot{\mathbf{x}} = A\mathbf{x}$ | **ODE (System)** | **1** | **Linear** | $\mathbf{x} \in \mathbb{R}^n$ | $t$ |

### Physical Insights:
* **Wave Equation (v) vs. Burgers' Equation (ii):** The wave equation allows linear superposition (sound waves pass through one another without distortion). In contrast, the nonlinear convective term $u \frac{\partial u}{\partial x}$ in Burgers' equation steepens wave fronts, creating **shock waves**—a cornerstone of supersonic aerodynamics.
* **Bessel's Equation (i):** The non-constant coefficients $x^2$ and $x$ originate from applying the Laplacian operator in cylindrical coordinates $\nabla^2 = \frac{1}{r}\frac{\partial}{\partial r}(r \frac{\partial}{\partial r})$, fundamental to aircraft fuselage vibrations and nozzle acoustics.

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Linearity and Order of Differential Equations|Linearity and Order of Differential Equations]]`
* `[[04 - Advanced Maths/Tema 1 - Introduction, Modeling and Classification of ODEs|Tema 1 Guide]]`
