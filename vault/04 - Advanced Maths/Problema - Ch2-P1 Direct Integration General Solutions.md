---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.1"
dificultad: baja
tags:
  - problema-resuelto
  - integracion-directa
  - primitivas
  - calculo-integral
---

# ✏️ Problem 2.1: Direct Integration General Solutions

## 📄 Enunciado (Problem Statement)

Find the general solution to the following equations:

(i) $y'(x) = e^{3x} - x$  
(ii) $x y'(x) = 1$  
(iii) $y'(x) = x e^{x^2}$  
(iv) $(1 + x) y'(x) = x$  
(v) $(1 + x^2) y'(x) = x$

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Structure:
In each item, the differential equation can be isolated algebraically in the direct derivative form:
$$ \frac{dy}{dx} = f(x) $$
where the right-hand side depends solely on the independent variable $x$, with no appearance of the dependent variable $y$.

### Domains of Definition:
* (i) $f(x) = e^{3x} - x$, continuous on $\mathbb{R}$.
* (ii) $f(x) = \frac{1}{x}$, singular at $x = 0$; domain is $x \in (-\infty, 0) \cup (0, \infty)$.
* (iii) $f(x) = x e^{x^2}$, continuous on $\mathbb{R}$.
* (iv) $f(x) = \frac{x}{1+x}$, singular at $x = -1$; domain is $x \in (-\infty, -1) \cup (-1, \infty)$.
* (v) $f(x) = \frac{x}{1+x^2}$, continuous on $\mathbb{R}$ because $1+x^2 \ge 1 > 0$.

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

By the Fundamental Theorem of Calculus, the general solution is obtained by direct indefinite integration:
$$ y(x) = \int f(x) \, dx + C $$
where $C \in \mathbb{R}$ is an arbitrary integration constant.
* For (i): Integrate elementary exponential and polynomial terms.
* For (ii): Standard logarithmic primitive with absolute value.
* For (iii): Integration by substitution ($u = x^2$).
* For (iv): Polynomial long division / algebraic fraction splitting $\frac{x}{1+x} = 1 - \frac{1}{1+x}$.
* For (v): Logarithmic derivative pattern $\int \frac{u'(x)}{u(x)} dx = \frac{1}{2}\ln(u(x))$.

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Part (i): $y'(x) = e^{3x} - x$
Direct integration with respect to $x$:
$$ y(x) = \int \left( e^{3x} - x \right) dx $$
Splitting the integral by linearity:
$$ y(x) = \int e^{3x} \, dx - \int x \, dx $$
Evaluating each term:
* $\int e^{3x} dx = \frac{1}{3} e^{3x}$
* $\int x dx = \frac{1}{2} x^2$
$$ \mathbf{y(x) = \frac{1}{3} e^{3x} - \frac{1}{2} x^2 + C} \tag{1} $$

---

### Part (ii): $x y'(x) = 1$
Divide both sides by $x$ (for $x \neq 0$):
$$ y'(x) = \frac{1}{x} $$
Integrate with respect to $x$:
$$ y(x) = \int \frac{1}{x} \, dx $$
$$ \mathbf{y(x) = \ln|x| + C, \quad x \neq 0} \tag{2} $$

---

### Part (iii): $y'(x) = x e^{x^2}$
Integrate with respect to $x$:
$$ y(x) = \int x e^{x^2} \, dx $$
Use the substitution $u = x^2$. Then $\frac{du}{dx} = 2x \implies x \, dx = \frac{1}{2} du$:
$$ y(x) = \int e^u \left( \frac{1}{2} \, du \right) = \frac{1}{2} \int e^u \, du = \frac{1}{2} e^u + C $$
Reverting the substitution $u = x^2$:
$$ \mathbf{y(x) = \frac{1}{2} e^{x^2} + C} \tag{3} $$

---

### Part (iv): $(1 + x) y'(x) = x$
Divide by $(1 + x)$ for $x \neq -1$:
$$ y'(x) = \frac{x}{1 + x} $$
Perform algebraic fraction manipulation by adding and subtracting $1$ in the numerator:
$$ \frac{x}{1 + x} = \frac{(x + 1) - 1}{x + 1} = \frac{x + 1}{x + 1} - \frac{1}{x + 1} = 1 - \frac{1}{x + 1} $$
Integrate with respect to $x$:
$$ y(x) = \int \left( 1 - \frac{1}{x + 1} \right) dx = \int 1 \, dx - \int \frac{1}{x + 1} \, dx $$
$$ \mathbf{y(x) = x - \ln|x + 1| + C, \quad x \neq -1} \tag{4} $$

---

### Part (v): $(1 + x^2) y'(x) = x$
Divide by $(1 + x^2)$:
$$ y'(x) = \frac{x}{1 + x^2} $$
Multiply and divide by $2$ to construct the derivative of the denominator in the numerator:
$$ y(x) = \int \frac{x}{1 + x^2} \, dx = \frac{1}{2} \int \frac{2x}{1 + x^2} \, dx $$
Let $u = 1 + x^2$, so $du = 2x \, dx$:
$$ y(x) = \frac{1}{2} \int \frac{du}{u} = \frac{1}{2} \ln|u| + C $$
Since $1 + x^2 \ge 1 > 0$ for all $x \in \mathbb{R}$, $|1 + x^2| = 1 + x^2$:
$$ \mathbf{y(x) = \frac{1}{2} \ln(1 + x^2) + C = \ln\sqrt{1 + x^2} + C} \tag{5} $$

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Master Solution Summary:

| Item | Differential Equation | General Solution | Maximal Interval of Existence |
| :---: | :--- | :--- | :---: |
| **(i)** | $y' = e^{3x} - x$ | $\mathbf{y(x) = \frac{1}{3} e^{3x} - \frac{1}{2} x^2 + C}$ | $(-\infty, \infty)$ |
| **(ii)** | $x y' = 1$ | $\mathbf{y(x) = \ln\|x\| + C}$ | $(-\infty, 0)$ or $(0, \infty)$ |
| **(iii)** | $y' = x e^{x^2}$ | $\mathbf{y(x) = \frac{1}{2} e^{x^2} + C}$ | $(-\infty, \infty)$ |
| **(iv)** | $(1+x)y' = x$ | $\mathbf{y(x) = x - \ln\|x+1\| + C}$ | $(-\infty, -1)$ or $(-1, \infty)$ |
| **(v)** | $(1+x^2)y' = x$ | $\mathbf{y(x) = \frac{1}{2} \ln(1+x^2) + C}$ | $(-\infty, \infty)$ |

### Verification:
Differentiating each result recovers the original ODE identically:
* (i) $\frac{d}{dx}\left[ \frac{1}{3}e^{3x} - \frac{1}{2}x^2 + C \right] = e^{3x} - x$. Confirmed.
* (ii) $\frac{d}{dx}[\ln|x| + C] = \frac{1}{x} \implies x y' = x(1/x) = 1$. Confirmed.
* (iii) $\frac{d}{dx}\left[ \frac{1}{2}e^{x^2} + C \right] = \frac{1}{2}(2x) e^{x^2} = x e^{x^2}$. Confirmed.
* (iv) $\frac{d}{dx}[x - \ln|x+1| + C] = 1 - \frac{1}{x+1} = \frac{x}{x+1}$. Confirmed.
* (v) $\frac{d}{dx}\left[ \frac{1}{2}\ln(1+x^2) + C \right] = \frac{1}{2} \frac{2x}{1+x^2} = \frac{x}{1+x^2}$. Confirmed.

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Metodos de Integracion Directa y Ecuaciones Separables|Direct Integration & Separable Equations]]`
* `[[04 - Advanced Maths/Problema - Ch2-P2 Separable ODEs and Asymptotic Integrals|Problem 2.2: Separable Equations]]`
