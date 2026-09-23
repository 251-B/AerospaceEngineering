---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.4"
dificultad: media
tags:
  - problema-resuelto
  - ecuaciones-exactas
  - funcion-potencial
  - derivadas-parciales-cruzadas
  - formas-diferenciales
---

# ✏️ Problem 2.4: Exact Differential Equations

## 📄 Enunciado (Problem Statement)

Check that the following equations are exact and solve them:

(i) $(2xy - \sec^2 x) + (x^2 + 2y) \frac{dy}{dx} = 0$  
(ii) $(1 + e^x y + xe^x y) + (xe^x + 2) \frac{dy}{dx} = 0$  
(iii) $(x \cos y + \cos x) \frac{dy}{dx} + \sin y - y \sin x = 0$  
(iv) $e^x \sin y + y + (e^x \cos y + x + e^y) \frac{dy}{dx} = 0$

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Structure:
Each equation is written in the differential form:
$$ M(x, y) \, dx + N(x, y) \, dy = 0 $$
where exactness requires testing the condition $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$ across a simply connected domain $D \subseteq \mathbb{R}^2$.

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

1. Identify $M(x, y)$ (the term multiplying $dx$) and $N(x, y)$ (the term multiplying $dy$ or $\frac{dy}{dx}$).
2. Compute the partial derivatives $\frac{\partial M}{\partial y}$ and $\frac{\partial N}{\partial x}$.
3. Verify that $\frac{\partial M}{\partial y} \equiv \frac{\partial N}{\partial x}$ (Euler-Cauchy-Schwarz condition).
4. Reconstruct the potential function $F(x, y)$ by partial integration and match the remaining single-variable derivative.
5. State the general solution in implicit level curve form $F(x, y) = C$.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Part (i): $(2xy - \sec^2 x) + (x^2 + 2y) \frac{dy}{dx} = 0$

#### Step 1: Identification & Exactness Check
$$ M(x, y) = 2xy - \sec^2 x, \quad N(x, y) = x^2 + 2y $$
Compute mixed partials:
$$ \frac{\partial M}{\partial y} = \frac{\partial}{\partial y}(2xy - \sec^2 x) = 2x $$
$$ \frac{\partial N}{\partial x} = \frac{\partial}{\partial x}(x^2 + 2y) = 2x $$
Since $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} = 2x$, **the equation is exact**.

#### Step 2: Potential Function Reconstruction
Integrate $M$ with respect to $x$:
$$ F(x, y) = \int (2xy - \sec^2 x) \, dx = x^2 y - \tan x + h(y) $$
Differentiate with respect to $y$ and equate to $N(x, y)$:
$$ \frac{\partial F}{\partial y} = x^2 + h'(y) = x^2 + 2y $$
$$ h'(y) = 2y \implies h(y) = y^2 $$
The potential function is $F(x, y) = x^2 y - \tan x + y^2$.
$$ \mathbf{x^2 y - \tan x + y^2 = C} \tag{1} $$

---

### Part (ii): $(1 + e^x y + xe^x y) + (xe^x + 2) \frac{dy}{dx} = 0$

#### Step 1: Identification & Exactness Check
$$ M(x, y) = 1 + e^x y + x e^x y, \quad N(x, y) = x e^x + 2 $$
Compute mixed partials:
$$ \frac{\partial M}{\partial y} = e^x + x e^x $$
$$ \frac{\partial N}{\partial x} = \frac{\partial}{\partial x}(x e^x + 2) = 1 \cdot e^x + x e^x + 0 = e^x + x e^x $$
Since $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} = (1 + x)e^x$, **the equation is exact**.

#### Step 2: Potential Function Reconstruction
Integrating $N$ with respect to $y$ is simpler:
$$ F(x, y) = \int (x e^x + 2) \, dy = (x e^x + 2) y + g(x) = x e^x y + 2y + g(x) $$
Differentiate with respect to $x$ and equate to $M(x, y)$:
$$ \frac{\partial F}{\partial x} = (e^x + x e^x) y + g'(x) = 1 + e^x y + x e^x y $$
$$ g'(x) = 1 \implies g(x) = x $$
The potential function is $F(x, y) = x e^x y + 2y + x$.
$$ \mathbf{x e^x y + 2y + x = C \implies y(x) = \frac{C - x}{x e^x + 2}} \tag{2} $$

---

### Part (iii): $(x \cos y + \cos x) \frac{dy}{dx} + \sin y - y \sin x = 0$

#### Step 1: Standard Differential Form
Rearranging into $M \, dx + N \, dy = 0$:
$$ (\sin y - y \sin x) \, dx + (x \cos y + \cos x) \, dy = 0 $$
$$ M(x, y) = \sin y - y \sin x, \quad N(x, y) = x \cos y + \cos x $$

#### Step 2: Exactness Check
$$ \frac{\partial M}{\partial y} = \cos y - \sin x $$
$$ \frac{\partial N}{\partial x} = \cos y - \sin x $$
Since $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} = \cos y - \sin x$, **the equation is exact**.

#### Step 3: Potential Function Reconstruction
Integrate $M$ with respect to $x$:
$$ F(x, y) = \int (\sin y - y \sin x) \, dx = x \sin y - y (-\cos x) + h(y) = x \sin y + y \cos x + h(y) $$
Differentiate with respect to $y$ and equate to $N(x, y)$:
$$ \frac{\partial F}{\partial y} = x \cos y + \cos x + h'(y) = x \cos y + \cos x $$
$$ h'(y) = 0 \implies h(y) = 0 $$
$$ \mathbf{x \sin y + y \cos x = C} \tag{3} $$

---

### Part (iv): $e^x \sin y + y + (e^x \cos y + x + e^y) \frac{dy}{dx} = 0$

#### Step 1: Identification & Exactness Check
$$ M(x, y) = e^x \sin y + y, \quad N(x, y) = e^x \cos y + x + e^y $$
Compute mixed partials:
$$ \frac{\partial M}{\partial y} = e^x \cos y + 1 $$
$$ \frac{\partial N}{\partial x} = e^x \cos y + 1 + 0 = e^x \cos y + 1 $$
Since $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$, **the equation is exact**.

#### Step 2: Potential Function Reconstruction
Integrate $M$ with respect to $x$:
$$ F(x, y) = \int (e^x \sin y + y) \, dx = e^x \sin y + x y + h(y) $$
Differentiate with respect to $y$ and equate to $N(x, y)$:
$$ \frac{\partial F}{\partial y} = e^x \cos y + x + h'(y) = e^x \cos y + x + e^y $$
$$ h'(y) = e^y \implies h(y) = e^y $$
The potential function is $F(x, y) = e^x \sin y + x y + e^y$.
$$ \mathbf{e^x \sin y + x y + e^y = C} \tag{4} $$

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Master Solution Table:

| Part | $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$ | Potential Function $F(x, y)$ | General Implicit Solution |
| :---: | :---: | :---: | :--- |
| **(i)** | $2x$ | $x^2 y - \tan x + y^2$ | $\mathbf{x^2 y - \tan x + y^2 = C}$ |
| **(ii)** | $(1+x)e^x$ | $x e^x y + 2y + x$ | $\mathbf{x e^x y + 2y + x = C}$ |
| **(iii)** | $\cos y - \sin x$ | $x \sin y + y \cos x$ | $\mathbf{x \sin y + y \cos x = C}$ |
| **(iv)** | $e^x \cos y + 1$ | $e^x \sin y + xy + e^y$ | $\mathbf{e^x \sin y + xy + e^y = C}$ |

### Verification:
Taking the total derivative $dF = \frac{\partial F}{\partial x} dx + \frac{\partial F}{\partial y} dy = 0$ reproduces each differential equation identically.

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Ecuaciones Exactas y Factores Integrantes Especiales|Exact Equations Theory]]`
* `[[04 - Advanced Maths/Problema - Ch2-P5 Integrating Factor for Non-Exact Equations|Problem 2.5: Special Integrating Factors]]`
* `[[04 - Advanced Maths/Problema - Ch2-P6 Exactness of Separated Differential Forms|Problem 2.6: Separated Forms are Exact]]`
