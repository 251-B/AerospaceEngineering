---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.7"
dificultad: media
tags:
  - problema-resuelto
  - change-of-variables
  - bernoulli-equation
  - integrating-factor
  - initial-value-problem
---

# Problem 2.7: Nonlinear Change of Variables

Source: ProblemsCh2.pdf, Exercise 7 (page 2). File: sources/cuatrimestre-1/04-advanced-maths/unit-02-first-order-odes/problemas/ProblemsCh2.pdf

Theory reference: Robinson, An Introduction to Ordinary Differential Equations (BookODE's.pdf), Chapter 10, Section 10.2 (substitution methods), Section 9.2 (integrating factors) and Theorem 6.2.

## Problem Statement

We consider the following initial value problem:

$$
y'(x) = y(x) + \frac{x}{y(x)}, \qquad y(0) = 1.
$$

Make the change of variable $z(x) = y(x)^2$ and find the solution.

---

## Phase 1: Classification, Hypotheses and Domain

Right-hand side: $f(x,y) = y + x/y$. It is continuous for $y \neq 0$, and $\partial f/\partial y = 1 - x/y^2$ is continuous for $y \neq 0$. The initial point $(0,1)$ lies in the region $y > 0$, so Theorem 6.2 gives a unique local solution. The line $y = 0$ is excluded from the domain, so the solution cannot cross it: while it exists it keeps the sign of $y(0) = 1$, that is $y(x) > 0$.

The equation is non-linear in $y$ because of the term $x\,y^{-1}$. It has Bernoulli form $y' - y = x\,y^{-1}$ with exponent $\alpha = -1$ (see Problem 2.8).

---

## Phase 2: Choice of Method and Change of Variables

Why this substitution: multiplying the equation by $y$ gives $y\,y' = y^2 + x$, and the left side is $\frac{1}{2}\frac{d}{dx}(y^2)$. In terms of $z = y^2$ the right side $y^2 + x = z + x$ is linear, so the problem becomes a linear first-order equation, solvable with an integrating factor.

Change of variables written explicitly: $z = y^2$, $\ z' = 2y\,y'$ (chain rule), $\ z(0) = y(0)^2 = 1$. Back-substitution: since $y > 0$, $y = +\sqrt{z}$.

---

## Phase 3: Step-by-Step Derivation

### Step 1: transform the equation

Multiply $y' = y + x/y$ by $2y$ (allowed since $y \neq 0$):

$$
2y\,y' = 2y^2 + 2x.
$$

With $z = y^2$ and $z' = 2yy'$:

$$
z' = 2z + 2x, \qquad z(0) = 1, \qquad\text{i.e.}\quad z' - 2z = 2x.
$$

### Step 2: integrating factor

$p(x) = -2$, so $\int p\,dx = -2x$ and $\mu(x) = e^{-2x}$, $\mu(0) = 1$. Then $(z\,e^{-2x})' = 2x\,e^{-2x}$. Integrate from $0$ to $x$ (Barrow):

$$
z(x)e^{-2x} - z(0)\cdot 1 = \int_0^x 2s\,e^{-2s}\,ds.
$$

Integration by parts with $u = 2s$, $dv = e^{-2s}ds$, $du = 2\,ds$, $v = -\tfrac12 e^{-2s}$:

$$
\int 2s\,e^{-2s}\,ds = -s\,e^{-2s} + \int e^{-2s}\,ds = -s\,e^{-2s} - \frac{1}{2}e^{-2s}.
$$

Evaluate between the limits $0$ and $x$:

$$
\left[-s\,e^{-2s} - \tfrac12 e^{-2s}\right]_0^x = -x\,e^{-2x} - \tfrac12 e^{-2x} + \tfrac12.
$$

Hence $z\,e^{-2x} = 1 - x\,e^{-2x} - \tfrac12 e^{-2x} + \tfrac12 = \tfrac32 - x\,e^{-2x} - \tfrac12 e^{-2x}$. Multiply by $e^{2x}$:

$$
z(x) = \frac{3}{2}e^{2x} - x - \frac{1}{2}.
$$

### Step 3: return to $y$ and find the domain

Since $y > 0$ and $y^2 = z$, we need $z > 0$ and take the positive root:

$$
y(x) = \sqrt{\frac{3}{2}e^{2x} - x - \frac{1}{2}}.
$$

Domain: is $z(x) > 0$ for all $x$? Minimize $z$: $z'(x) = 3e^{2x} - 1 = 0$ at $e^{2x} = 1/3$, i.e. $x_m = -\tfrac12\ln 3 \approx -0.549$. Since $z'' = 6e^{2x} > 0$ this is the global minimum, and

$$
z(x_m) = \frac32\cdot\frac13 + \frac12\ln 3 - \frac12 = \frac12\ln 3 \approx 0.549 > 0.
$$

So $z(x) \geq \frac12\ln 3 > 0$ for every real $x$: the solution never reaches $y = 0$ and is defined on all of $\mathbb{R}$ (the maximal interval of existence is $\mathbb{R}$).

---

## Phase 4: Verification, Limits and Interpretation

Substitute back into the original equation. Differentiate $y = \sqrt{z}$: $y' = \dfrac{z'}{2y} = \dfrac{3e^{2x} - 1}{2y}$. The right-hand side is

$$
y + \frac{x}{y} = \frac{y^2 + x}{y} = \frac{z + x}{y} = \frac{\frac32 e^{2x} - \frac12}{y} = \frac{3e^{2x} - 1}{2y}.
$$

They agree. Initial condition: $z(0) = \frac32 - 0 - \frac12 = 1$, so $y(0) = 1$.

- As $x \to +\infty$: $y \sim \sqrt{3/2}\,e^{x}$, exponential growth, consistent with $y' \approx y$ for large $y$.
- As $x \to -\infty$: $z \sim -x$, so $y \sim \sqrt{\lvert x\rvert} \to \infty$: the term $x/y$ is negative for $x<0$, while $z \approx -x$ grows.

Numeric check (fourth-order Runge-Kutta against the formula): the maximum absolute difference at $x = -2, -1, 1, 2$ is about $4.5\times 10^{-13}$ (fourth-order Runge-Kutta, 40000 steps per interval).

#### Result

$$
y(x) = \sqrt{\tfrac32 e^{2x} - x - \tfrac12}, \qquad x \in \mathbb{R}.
$$

---

## Related Notes

- [[04 - Advanced Maths/Concepto - Sustituciones No Lineales y Ecuacion de Bernoulli|Nonlinear substitutions and the Bernoulli equation]]
- [[04 - Advanced Maths/Concepto - Factor Integrante y Ecuaciones Lineales de Primer Orden|Integrating factor theory]]
- [[04 - Advanced Maths/Problema - Ch2-P8 General Bernoulli Equation Reduction|Problem 2.8: general Bernoulli reduction]]
