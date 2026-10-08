---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.5"
dificultad: media
tags:
  - problema-resuelto
  - exact-equations
  - integrating-factor
  - non-exact-equations
---

# Problem 2.5: Integrating Factor for a Non-Exact Equation

Source: ProblemsCh2.pdf, Exercise 5 (page 2). File: sources/cuatrimestre-1/04-advanced-maths/unit-02-first-order-odes/problemas/ProblemsCh2.pdf

Theory reference: Robinson, An Introduction to Ordinary Differential Equations (BookODE's.pdf), Chapter 10, Section 10.1 (exact equations).

## Problem Statement

Find an integrating factor depending only on $x$ that makes the equation

$$
3xy + y^2 + (x^2 + xy)\frac{dy}{dx} = 0
$$

exact, and find its solution.

---

## Phase 1: Classification, Hypotheses and Domain

Write the equation as $M + N\,y' = 0$ with

$$
M(x,y) = 3xy + y^2, \qquad N(x,y) = x^2 + xy = x(x+y).
$$

$M$, $N$ and their partial derivatives are polynomials, hence continuous on $\mathbb{R}^2$. Exactness test:

$$
M_y = 3x + 2y, \qquad N_x = 2x + y.
$$

$M_y - N_x = x + y$, which is not identically zero, so the equation is not exact. We look for $\mu = \mu(x)$ (nowhere zero on the domain considered) such that $\mu M + \mu N\,y' = 0$ is exact. We work on a region where $x \neq 0$ (the line $x = 0$ is excluded because $N(0,y) = 0$ there).

---

## Phase 2: Choice of Method and Change of Variables

Why this method: multiplying the equation by a nonzero function does not change its solution set (on the region where the factor is nonzero) but can restore exactness. The requirement is $(\mu M)_y = (\mu N)_x$. If $\mu$ depends only on $x$, then $(\mu M)_y = \mu M_y$ and $(\mu N)_x = \mu' N + \mu N_x$, so the condition becomes

$$
\mu M_y = \mu' N + \mu N_x \quad\Longleftrightarrow\quad \frac{\mu'}{\mu} = \frac{M_y - N_x}{N}.
$$

This ordinary differential equation for $\mu(x)$ is solvable only if the right-hand side depends on $x$ alone (otherwise no integrating factor of the form $\mu(x)$ exists). Then we integrate it, and continue with the standard exact-equation construction $F_x = \mu M$, $F_y = \mu N$.

---

## Phase 3: Step-by-Step Derivation

### Step 1: find $\mu(x)$

Compute the quotient, factoring $N = x(x+y)$:

$$
\frac{M_y - N_x}{N} = \frac{x + y}{x(x+y)} = \frac{1}{x} \qquad (x + y \neq 0).
$$

This depends only on $x$, so $\mu$ exists. Solve $\mu'/\mu = 1/x$:

$$
\int\frac{d\mu}{\mu} = \int\frac{dx}{x} \ \Longrightarrow\ \ln\lvert\mu\rvert = \ln\lvert x\rvert + c \ \Longrightarrow\ \mu(x) = x \quad (\text{taking the constant multiple equal to }1).
$$

### Step 2: check exactness of the new equation

Multiply by $\mu = x$:

$$
\tilde{M} = x M = 3x^2y + xy^2, \qquad \tilde{N} = xN = x^3 + x^2y.
$$

$$
\tilde{M}_y = 3x^2 + 2xy, \qquad \tilde{N}_x = 3x^2 + 2xy.
$$

They coincide, so the new equation is exact.

### Step 3: potential function

Integrate $F_x = \tilde{M}$ in $x$ at fixed $y$:

$$
F = \int(3x^2y + xy^2)\,dx + h(y) = x^3 y + \frac{x^2y^2}{2} + h(y).
$$

Impose $F_y = \tilde{N}$:

$$
F_y = x^3 + x^2 y + h'(y) = x^3 + x^2y \ \Longrightarrow\ h'(y) = 0.
$$

So $h$ is constant and the solution in implicit form is

$$
x^3y + \frac{1}{2}x^2y^2 = C \qquad\Longleftrightarrow\qquad x^2y^2 + 2x^3y = K, \quad K = 2C.
$$

### Step 4: explicit form

Complete the square in $y$: $x^2y^2 + 2x^3y = x^2\left[(y + x)^2 - x^2\right]$. Then $x^2(y+x)^2 = K + x^4$, so

$$
y(x) = -x \pm \frac{\sqrt{x^4 + K}}{\lvert x\rvert}, \qquad x \neq 0,\ x^4 + K \geq 0.
$$

Remark: on the line $y = -x$ the coefficient $N = x(x+y)$ vanishes. Direct substitution of $y = -x$ gives $M = -3x^2 + x^2 = -2x^2$ and $N = 0$, so $M + N y' = -2x^2 \neq 0$ and $y = -x$ is not a solution.

---

## Phase 4: Verification, Limits and Interpretation

Check the potential: $F = x^3y + \tfrac12 x^2y^2$ has $F_x = 3x^2y + xy^2 = x(3xy + y^2) = xM$ and $F_y = x^3 + x^2y = x(x^2 + xy) = xN$, as required.

Check along a solution curve: implicit differentiation of $x^3y + \tfrac12x^2y^2 = C$ gives $(3x^2y + xy^2) + (x^3 + x^2y)y' = 0$. Dividing by $x \neq 0$ gives back $(3xy + y^2) + (x^2 + xy)y' = 0$, the original equation. The division by $x$ is why the line $x = 0$ must be excluded from the region of validity.

Numeric spot check of the explicit branch: with $K = 3$ and $x = 1$, $y = -1 + \sqrt{1 + 3} = 1$; then $F = 1 + \tfrac12 = \tfrac32 = K/2$, consistent. The slope from the ODE is $y' = -\frac{3xy + y^2}{x^2 + xy} = -\frac{4}{2} = -2$, and the derivative of $y = -x + \sqrt{x^4+3}/x$ is $-1 + \frac{x^4 - 3}{x^2\sqrt{x^4+3}}$, which equals $-1 + \frac{-2}{1\cdot 2} = -2$ at $x = 1$.

#### Result

Integrating factor $\mu(x) = x$ (up to a constant factor). Solution: $x^3y + \tfrac12x^2y^2 = C$ on regions with $x \neq 0$.

---

## Related Notes

- [[04 - Advanced Maths/Concept - Exact Equations and Special Integrating Factors|Exact equations and special integrating factors]]
- [[04 - Advanced Maths/Problem - Ch2-P4 Exact Differential Equations|Problem 2.4: exact equations]]
