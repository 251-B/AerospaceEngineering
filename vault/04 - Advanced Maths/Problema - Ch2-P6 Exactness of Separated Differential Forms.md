---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.6"
dificultad: baja
tags:
  - problema-resuelto
  - exact-equations
  - separable-equations
  - potential-function
  - conserved-quantity
---

# Problem 2.6: Exactness of Separated Differential Forms

Source: ProblemsCh2.pdf, Exercise 6 (page 2). File: sources/cuatrimestre-1/04-advanced-maths/unit-02-first-order-odes/problemas/ProblemsCh2.pdf

Theory reference: Robinson, An Introduction to Ordinary Differential Equations (BookODE's.pdf), Chapter 10, Section 10.1 (exact equations); this is also Exercise 10.3 of the book.

## Problem Statement

Show that any equation that can be written in the form

$$
f(x) + g(y)\frac{dy}{dx} = 0
$$

is exact, and find its solution in terms of integrals of $f$ and $g$. Hence find the solutions of

(i) $V'(x) + 2y\dfrac{dy}{dx} = 0$,  
(ii) $\left[\dfrac{1}{y} - a\right]\dfrac{dy}{dx} + \dfrac{2}{x} - b = 0$, for $x, y > 0$.  

---

## Phase 1: Classification, Hypotheses and Domain

General form: $M(x,y) + N(x,y)\,y' = 0$ with $M = f(x)$ depending on $x$ only and $N = g(y)$ depending on $y$ only. Assume $f$ continuous on an interval $I_x$ and $g$ continuous on an interval $I_y$, so that $M$ and $N$ are continuous on the rectangle $\Omega = I_x \times I_y$ (a simply connected set).

- (i) $f(x) = V'(x)$, with $V \in C^1$ so that $V'$ is continuous; $g(y) = 2y$. Rectangle: $I_x$ any interval, $I_y = \mathbb{R}$.
- (ii) $f(x) = \frac{2}{x} - b$, $g(y) = \frac{1}{y} - a$. Continuous on $x > 0$ and $y > 0$ (the stated domain), so $\Omega = (0,\infty)\times(0,\infty)$.

---

## Phase 2: Choice of Method and Change of Variables

Why this method: the exactness criterion $M_y = N_x$ (Robinson, Section 10.1) is the hypothesis for a potential function $F$ with $F_x = M$, $F_y = N$ to exist on $\Omega$. Here both partial derivatives are trivial, so the criterion can be checked at once, and the potential can be constructed by integrating each variable separately.

Construction: integrate $F_x = f(x)$ in $x$, then fix the $y$-dependent integration function $h(y)$ from $F_y = g(y)$. Level sets of $F$ are the solutions.

---

## Phase 3: Step-by-Step Derivation

### General case

$M = f(x)$ does not depend on $y$, and $N = g(y)$ does not depend on $x$:

$$
\frac{\partial M}{\partial y} = 0 = \frac{\partial N}{\partial x}.
$$

The exactness condition holds, so the equation is exact. Construct $F$: from $F_x = f(x)$,

$$
F(x,y) = \int_{x_0}^{x} f(s)\,ds + h(y).
$$

Differentiate in $y$: $F_y = h'(y)$, and this must equal $N = g(y)$. So $h'(y) = g(y)$ and

$$
h(y) = \int_{y_0}^{y} g(r)\,dr.
$$

Hence the solutions are the level curves

$$
\boxed{\ \int_{x_0}^{x} f(s)\,ds + \int_{y_0}^{y} g(r)\,dr = C\ }, \qquad C \in \mathbb{R}.
$$

If a solution passes through $(x_0,y_0)$, then $C = 0$ with these lower limits (Barrow's rule fixes the constant). The same result follows from separation of variables: $g(y)\,dy = -f(x)\,dx$, then integrate both sides.

### Part (i): $V'(x) + 2y\,y' = 0$

Here $f = V'$ and $g = 2y$. The integrals are $\int V'(x)\,dx = V(x)$ and $\int 2y\,dy = y^2$. Therefore

$$
V(x) + y^2 = C.
$$

Equivalent explicit form: $y = \pm\sqrt{C - V(x)}$, defined where $V(x) \leq C$. The equation says $\frac{d}{dx}\left[V(x) + y^2\right] = V' + 2yy' = 0$, i.e. $V + y^2$ is conserved along the solution.

### Part (ii): $\left[\frac1y - a\right]y' + \frac2x - b = 0$, $x,y>0$

Here $f(x) = \frac{2}{x} - b$ and $g(y) = \frac{1}{y} - a$. Integrate each, using $x > 0$ and $y > 0$ so no absolute values are needed:

$$
\int\left(\frac2x - b\right)dx = 2\ln x - bx, \qquad \int\left(\frac1y - a\right)dy = \ln y - ay.
$$

The solutions are therefore

$$
2\ln x - bx + \ln y - ay = C.
$$

Combine the logarithms and exponentiate: $\ln(x^2 y) = C + bx + ay$, so with $K = e^{C} > 0$,

$$
x^2\,y\,e^{-bx - ay} = K.
$$

---

## Phase 4: Verification, Limits and Interpretation

Check by implicit differentiation:

- General case: $\frac{d}{dx}\left[\int_{x_0}^{x}f\,ds + \int_{y_0}^{y(x)}g\,dr\right] = f(x) + g(y)\,y'$, using the Fundamental Theorem of Calculus and the chain rule; this vanishes by the ODE.
- (i) $\frac{d}{dx}\left[V(x) + y^2\right] = V'(x) + 2y\,y' = 0$.
- (ii) $\frac{d}{dx}\left[2\ln x - bx + \ln y - ay\right] = \frac{2}{x} - b + \left(\frac{1}{y} - a\right)y' = 0$, the original equation.

Dimensional remark for (ii): $\ln x$ and $\ln y$ require dimensionless arguments, so $x$ and $y$ are understood as measured in fixed reference units; then $bx$ and $ay$ are dimensionless, which means $[b] = [x]^{-1}$ and $[a] = [y]^{-1}$, consistent with the terms $\frac{2}{x} - b$ and $\frac{1}{y} - a$ being summed.

Domain: in (ii) the level set $x^2 y e^{-bx-ay} = K$ in the open quadrant is a union of curves; $y$ is a function of $x$ locally wherever $F_y = \frac1y - a \neq 0$, i.e. away from $y = 1/a$ when $a > 0$.

#### Results

General form: $\int f\,dx + \int g\,dy = C$. (i) $V(x) + y^2 = C$. (ii) $2\ln x - bx + \ln y - ay = C$, i.e. $x^2 y\,e^{-bx-ay} = K > 0$.

---

## Related Notes

- [[04 - Advanced Maths/Concepto - Ecuaciones Exactas y Factores Integrantes Especiales|Exact equations and special integrating factors]]
- [[04 - Advanced Maths/Concepto - Metodos de Integracion Directa y Ecuaciones Separables|Direct integration and separable equations]]
- [[04 - Advanced Maths/Problema - Ch2-P4 Exact Differential Equations|Problem 2.4: exact equations]]
