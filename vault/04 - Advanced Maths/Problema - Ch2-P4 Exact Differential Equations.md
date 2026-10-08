---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.4"
dificultad: media
tags:
  - problema-resuelto
  - exact-equations
  - potential-function
  - implicit-solutions
---

# Problem 2.4: Exact Differential Equations

Source: ProblemsCh2.pdf, Exercise 4 (page 2). File: sources/cuatrimestre-1/04-advanced-maths/unit-02-first-order-odes/problemas/ProblemsCh2.pdf

Theory reference: Robinson, An Introduction to Ordinary Differential Equations (BookODE's.pdf), Chapter 10, Section 10.1 (exact equations).

## Problem Statement

Check that the following equations are exact and solve them.

(i) $(2xy - \sec^2 x) + (x^2 + 2y)\dfrac{dy}{dx} = 0$,  
(ii) $(1 + e^x y + x e^x y) + (x e^x + 2)\dfrac{dy}{dx} = 0$,  
(iii) $(x\cos y + \cos x)\dfrac{dy}{dx} + \sin y - y\sin x = 0$,  
(iv) $e^x\sin y + y + (e^x\cos y + x + e^y)\dfrac{dy}{dx} = 0$.  

---

## Phase 1: Classification, Hypotheses and Domain

Each equation is written in the form

$$
M(x,y) + N(x,y)\,\frac{dy}{dx} = 0, \qquad\text{equivalently}\qquad M\,dx + N\,dy = 0.
$$

The equation is exact if there is a function $F(x,y)$ of class $C^2$ with $F_x = M$ and $F_y = N$. Along any solution $y(x)$ one then has $\frac{d}{dx}F(x,y(x)) = F_x + F_y y' = M + N y' = 0$, so $F(x,y(x)) = C$.

Hypotheses: $M$, $N$ and their first partial derivatives continuous on a rectangle (or any simply connected open set) $\Omega$. Then (Robinson, Section 10.1, condition (10.5)) the equation is exact on $\Omega$ if and only if

$$
\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}.
$$

| Part | $M$ | $N$ | Domain used |
| :--- | :--- | :--- | :--- |
| (i) | $2xy - \sec^2 x$ | $x^2 + 2y$ | $x \in (-\pi/2, \pi/2)$ (or any strip between zeros of $\cos x$), $y \in \mathbb{R}$ |
| (ii) | $1 + e^x y + x e^x y$ | $x e^x + 2$ | $\mathbb{R}^2$ |
| (iii) | $\sin y - y\sin x$ | $x\cos y + \cos x$ | $\mathbb{R}^2$ |
| (iv) | $e^x\sin y + y$ | $e^x\cos y + x + e^y$ | $\mathbb{R}^2$ |

---

## Phase 2: Choice of Method and Change of Variables

Why this method: if the exactness criterion $M_y = N_x$ holds, a potential $F$ exists and the solution curves are the level sets $F = C$, so no integrating factor or substitution is needed.

Construction of $F$, applied identically in each part:

- (a) Test: compute $M_y$ and $N_x$ and compare.
- (b) Integrate $F_x = M$ in $x$ holding $y$ fixed: $F = \int M\,dx + h(y)$, where the arbitrary function $h(y)$ plays the role of the constant of integration.
- (c) Differentiate in $y$ and impose $F_y = N$: $h'(y) = N - \partial_y\int M\,dx$. The right side depends on $y$ only because $M_y = N_x$.
- (d) Integrate $h'$ and write the implicit solution $F(x,y) = C$.

---

## Phase 3: Step-by-Step Derivation

### Part (i): $M = 2xy - \sec^2 x$, $N = x^2 + 2y$

(a) $M_y = 2x$ and $N_x = 2x$. They coincide, so the equation is exact.

(b) $F = \int (2xy - \sec^2 x)\,dx + h(y) = x^2 y - \tan x + h(y)$ (using $\frac{d}{dx}\tan x = \sec^2 x$).

(c) $F_y = x^2 + h'(y)$ must equal $N = x^2 + 2y$, so $h'(y) = 2y$.

(d) $h(y) = y^2$ (the constant is absorbed in $C$). Therefore

$$
F(x,y) = x^2 y - \tan x + y^2 = C.
$$

Solving the quadratic $y^2 + x^2 y - (\tan x + C) = 0$ for $y$ gives, where the discriminant is nonnegative,

$$
y(x) = \frac{-x^2 \pm \sqrt{x^4 + 4(\tan x + C)}}{2}.
$$

### Part (ii): $M = 1 + e^x y + x e^x y$, $N = x e^x + 2$

(a) $M_y = e^x + x e^x$ and $N_x = e^x + x e^x$ (product rule on $x e^x$). They coincide: exact.

(b) $F = \int\left[1 + y\,(e^x + x e^x)\right]dx + h(y)$. Since $\frac{d}{dx}(x e^x) = e^x + x e^x$, this integral is $x + y\,x e^x$. So $F = x + x e^x y + h(y)$.

(c) $F_y = x e^x + h'(y)$ must equal $x e^x + 2$, so $h'(y) = 2$.

(d) $h(y) = 2y$. Therefore

$$
F(x,y) = x + x e^x y + 2y = C.
$$

This is linear in $y$, so it can be solved explicitly:

$$
y(x) = \frac{C - x}{x e^x + 2}.
$$

The denominator is never zero: $g(x) = x e^x$ has $g'(x) = (1+x)e^x = 0$ only at $x = -1$, where $g(-1) = -1/e \approx -0.368$, its global minimum, so $x e^x + 2 \ge 2 - 1/e > 0$. The solutions are therefore defined on all of $\mathbb{R}$.

### Part (iii): $M = \sin y - y\sin x$, $N = x\cos y + \cos x$

(a) $M_y = \cos y - \sin x$ and $N_x = \cos y - \sin x$. Exact.

(b) $F = \int(\sin y - y\sin x)\,dx + h(y) = x\sin y + y\cos x + h(y)$ (since $\int\sin x\,dx = -\cos x$, so $-y\int\sin x\,dx = y\cos x$).

(c) $F_y = x\cos y + \cos x + h'(y)$ must equal $N = x\cos y + \cos x$, so $h'(y) = 0$ and $h$ is constant.

(d) Absorbing the constant:

$$
F(x,y) = x\sin y + y\cos x = C.
$$

### Part (iv): $M = e^x\sin y + y$, $N = e^x\cos y + x + e^y$

(a) $M_y = e^x\cos y + 1$ and $N_x = e^x\cos y + 1$. Exact.

(b) $F = \int(e^x\sin y + y)\,dx + h(y) = e^x\sin y + x y + h(y)$.

(c) $F_y = e^x\cos y + x + h'(y)$ must equal $e^x\cos y + x + e^y$, so $h'(y) = e^y$.

(d) $h(y) = e^y$. Therefore

$$
F(x,y) = e^x\sin y + x y + e^y = C.
$$

---

## Phase 4: Verification, Limits and Interpretation

Check $F_x = M$ and $F_y = N$ for each potential:

- (i) $F = x^2y - \tan x + y^2$: $F_x = 2xy - \sec^2 x = M$, $F_y = x^2 + 2y = N$.
- (ii) $F = x + x e^x y + 2y$: $F_x = 1 + (e^x + x e^x)y = M$, $F_y = x e^x + 2 = N$. Also, for $y = (C-x)/(xe^x+2)$ with $C = 1$, $x = 0$: $y(0) = 1/2$; direct insertion gives $M(0,\tfrac12) + N(0,\tfrac12)y'(0) = \tfrac32 + 2y'(0)$, and $y'(0) = -\tfrac{3}{4}$ from the quotient rule, so the sum is $0$.
- (iii) $F = x\sin y + y\cos x$: $F_x = \sin y - y\sin x = M$, $F_y = x\cos y + \cos x = N$.
- (iv) $F = e^x\sin y + xy + e^y$: $F_x = e^x\sin y + y = M$, $F_y = e^x\cos y + x + e^y = N$.

Caveat on the level sets: $F(x,y) = C$ defines $y$ as a function of $x$ only where $F_y = N \neq 0$ (implicit function theorem). At points where $N = 0$ the level curve can have a vertical tangent and cannot be written as $y(x)$; for (ii) this never happens on the solution branch because $N = xe^x + 2 > 0$.

#### Results

| Part | Exactness | Solution |
| :--- | :--- | :--- |
| (i) | $M_y = N_x = 2x$ | $x^2y - \tan x + y^2 = C$ |
| (ii) | $M_y = N_x = e^x(1+x)$ | $x + xe^xy + 2y = C$, i.e. $y = \frac{C-x}{xe^x+2}$ |
| (iii) | $M_y = N_x = \cos y - \sin x$ | $x\sin y + y\cos x = C$ |
| (iv) | $M_y = N_x = e^x\cos y + 1$ | $e^x\sin y + xy + e^y = C$ |

---

## Related Notes

- [[04 - Advanced Maths/Concepto - Ecuaciones Exactas y Factores Integrantes Especiales|Exact equations and special integrating factors]]
- [[04 - Advanced Maths/Problema - Ch2-P5 Integrating Factor for Non-Exact Equations|Problem 2.5: integrating factor for a non-exact equation]]
- [[04 - Advanced Maths/Problema - Ch2-P6 Exactness of Separated Differential Forms|Problem 2.6: separated differential forms]]
