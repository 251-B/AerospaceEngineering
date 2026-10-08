---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.8"
dificultad: media
tags:
  - problema-resuelto
  - bernoulli-equation
  - change-of-variables
  - integrating-factor
  - linear-reduction
---

# Problem 2.8: General Bernoulli Equation Reduction

Source: ProblemsCh2.pdf, Exercise 8 (page 2). File: sources/cuatrimestre-1/04-advanced-maths/unit-02-first-order-odes/problemas/ProblemsCh2.pdf

Theory reference: Robinson, An Introduction to Ordinary Differential Equations (BookODE's.pdf), Chapter 10, Section 10.2 (substitution methods) and Section 9.2 (integrating factors).

## Problem Statement

Show that the Bernoulli equation

$$
y'(x) = a(x)\,y(x) + b(x)\,y(x)^{\alpha},
$$

where $\alpha \neq 0, 1$, can be transformed into a linear ODE with the change of variable $z(x) = y(x)^{1-\alpha}$ and find the solution. What happens if $\alpha = 0$ or $\alpha = 1$?

---

## Phase 1: Classification, Hypotheses and Domain

Assume $a$ and $b$ are continuous on an interval $I$ and $\alpha \in \mathbb{R}$, $\alpha \neq 0, 1$. The power $y^{\alpha}$ and $y^{1-\alpha}$ must make sense, so we work with $y > 0$ (for rational $\alpha$ with odd denominators other branches can be treated analogously). On $y > 0$, $f(x,y) = a y + b y^{\alpha}$ and $\partial f/\partial y = a + \alpha b\,y^{\alpha-1}$ are continuous, so IVPs with $y(x_0) = y_0 > 0$ have unique local solutions.

The equation is non-linear because $y^{\alpha}$ with $\alpha \neq 0, 1$ is not affine in $y$. When $\alpha > 0$, $y \equiv 0$ is also a solution; it is excluded by the assumption $y > 0$ and has to be added by hand (for $0 < \alpha < 1$ uniqueness at $y = 0$ may fail, as in Problem 2.14).

---

## Phase 2: Choice of Method and Change of Variables

Why this substitution: dividing by $y^{\alpha}$ gives $y^{-\alpha}y' = a\,y^{1-\alpha} + b$, where the left side is, up to a constant factor, the derivative of $y^{1-\alpha}$ and the right side contains $y^{1-\alpha}$ linearly. So the natural unknown is $z = y^{1-\alpha}$.

Change of variables written explicitly: $z = y^{1-\alpha}$, $\ z' = (1-\alpha)\,y^{-\alpha}\,y'$ (chain rule), $\ y = z^{1/(1-\alpha)}$.

---

## Phase 3: Step-by-Step Derivation

### Step 1: derive the linear equation

Differentiate $z = y^{1-\alpha}$ with the chain rule and substitute the equation for $y'$:

$$
z' = (1-\alpha)\,y^{-\alpha}\,y' = (1-\alpha)\,y^{-\alpha}\left(a\,y + b\,y^{\alpha}\right) = (1-\alpha)\left(a\,y^{1-\alpha} + b\right).
$$

Since $y^{1-\alpha} = z$:

$$
z' - (1-\alpha)\,a(x)\,z = (1-\alpha)\,b(x).
$$

This is linear first order in $z$, with $p(x) = -(1-\alpha)a(x)$ and $q(x) = (1-\alpha)b(x)$, both continuous.

### Step 2: solve it with an integrating factor

Fix $x_0 \in I$ and define $A(x) = \int_{x_0}^{x} a(s)\,ds$. Then $\int p\,dx = -(1-\alpha)A(x)$ and

$$
\mu(x) = e^{-(1-\alpha)A(x)}, \qquad \mu(x_0) = 1, \qquad (\mu z)' = (1-\alpha)\,b(x)\,\mu(x).
$$

Integrate from $x_0$ to $x$ (Barrow's rule), with $z_0 = z(x_0) = y_0^{1-\alpha}$:

$$
\mu(x)z(x) - z_0 = (1-\alpha)\int_{x_0}^{x} b(s)\,e^{-(1-\alpha)A(s)}\,ds.
$$

Multiply by $1/\mu(x) = e^{(1-\alpha)A(x)}$:

$$
z(x) = e^{(1-\alpha)A(x)}\left[z_0 + (1-\alpha)\int_{x_0}^{x} b(s)\,e^{-(1-\alpha)A(s)}\,ds\right].
$$

### Step 3: return to $y$

Since $y = z^{1/(1-\alpha)}$, wherever the bracket is positive (so that $y > 0$):

$$
y(x) = \left\{ e^{(1-\alpha)A(x)}\left[y_0^{1-\alpha} + (1-\alpha)\int_{x_0}^{x} b(s)\,e^{-(1-\alpha)A(s)}\,ds\right]\right\}^{\frac{1}{1-\alpha}}.
$$

The solution exists as long as the expression in braces stays positive; if it reaches $0$ at a finite point the solution ceases to exist there (the substitution is valid only for $y > 0$).

### Step 4: the excluded cases $\alpha = 0$ and $\alpha = 1$

- $\alpha = 1$: the equation is $y' = (a + b)\,y$, already linear and homogeneous. The substitution would give $z = y^{0} = 1$, a constant that carries no information (the formula above has the factor $1-\alpha = 0$, so it degenerates to $z' = 0$). The solution is obtained directly: $y(x) = y_0\exp\left(\int_{x_0}^{x}(a + b)\,ds\right)$.
- $\alpha = 0$: the equation is $y' = a\,y + b$, already linear (inhomogeneous). The substitution gives $z = y^{1} = y$, the identity, and the formula above with $1-\alpha = 1$ reproduces the variation-of-constants solution $y = e^{A}\left[y_0 + \int_{x_0}^{x} b\,e^{-A}\,ds\right]$. No transformation is needed.

---

## Phase 4: Verification, Limits and Interpretation

Check the general solution by differentiation. Put $B(x) = z_0 + (1-\alpha)\int_{x_0}^{x} b\,e^{-(1-\alpha)A}\,ds$, so $z = e^{(1-\alpha)A}B$ and

$$
z' = (1-\alpha)a\,e^{(1-\alpha)A}B + e^{(1-\alpha)A}(1-\alpha)\,b\,e^{-(1-\alpha)A} = (1-\alpha)a\,z + (1-\alpha)b.
$$

This is the linear equation of Step 1, and $z(x_0) = e^0 z_0 = z_0$. Undoing the change of variables is reversible for $y > 0$, so $y = z^{1/(1-\alpha)}$ solves the Bernoulli equation.

Consistency with Problem 2.7: for $a = 1$, $b = x$, $\alpha = -1$ the formula gives $1-\alpha = 2$, $A = x$, $z' - 2z = 2x$, which is the equation obtained there for $z = y^2$.

Check with a constant-coefficient case ($a$, $b$ constants, $\alpha = 2$, so $1-\alpha = -1$): $z' + a z = -b$, giving $z = -\frac{b}{a} + \left(z_0 + \frac{b}{a}\right)e^{-a(x-x_0)}$ and $y = 1/z$, which is the logistic-type solution of $y' = ay + by^2$. A sympy substitution of this closed form into $y' = a y + b y^2$ (with $a, b > 0$ symbols and $y_0 = 1$) gives residual $0$.

#### Result

$z = y^{1-\alpha}$ turns the Bernoulli equation into $z' - (1-\alpha)a z = (1-\alpha)b$, with solution $z = e^{(1-\alpha)A}\left[z_0 + (1-\alpha)\int b\,e^{-(1-\alpha)A}\right]$ and $y = z^{1/(1-\alpha)}$. For $\alpha = 1$ and $\alpha = 0$ the equation is already linear and the substitution is trivial or degenerate.

---

## Related Notes

- [[04 - Advanced Maths/Concepto - Sustituciones No Lineales y Ecuacion de Bernoulli|Nonlinear substitutions and the Bernoulli equation]]
- [[04 - Advanced Maths/Concepto - Factor Integrante y Ecuaciones Lineales de Primer Orden|Integrating factor theory]]
- [[04 - Advanced Maths/Problema - Ch2-P7 Nonlinear Change of Variables|Problem 2.7: the case alpha = -1]]
