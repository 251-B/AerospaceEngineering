---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.11"
dificultad: baja
tags:
  - problema-resuelto
  - linear-odes
  - solution-ratio
  - uniqueness
  - quotient-rule
---

# Problem 2.11: Invariance of Solution Ratios in Linear ODEs

Source: ProblemsCh2.pdf, Exercise 11 (page 3). File: sources/cuatrimestre-1/04-advanced-maths/unit-02-first-order-odes/problemas/ProblemsCh2.pdf

Theory reference: Robinson, An Introduction to Ordinary Differential Equations (BookODE's.pdf), Section 9.2 (integrating factors); this is also Exercise 9.6 of the book.

## Problem Statement

Without solving the ODE, show that if $y_1(t)$ and $y_2(t)$ are any two solutions of

$$
\frac{dy}{dt} + p(t)\,y = 0,
$$

then the ratio $y_1(t)/y_2(t)$ is constant.

---

## Phase 1: Classification, Hypotheses and Domain

Assume $p$ is continuous on an interval $I$, and $y_1, y_2$ are differentiable solutions on $I$: $y_i' = -p\,y_i$ for $i = 1, 2$. The ratio $r(t) = y_1(t)/y_2(t)$ is defined only where $y_2(t) \neq 0$. So we first have to settle where $y_2$ can vanish.

Fact needed: a solution of this equation either vanishes identically or has no zeros. This follows from uniqueness (Problem 2.10): if $y_2(t_1) = 0$ at some $t_1$, then $y_2$ and the zero function solve the same IVP at $t_1$, so $y_2 \equiv 0$. We assume $y_2 \not\equiv 0$ (otherwise the ratio is meaningless), hence $y_2(t) \neq 0$ on all of $I$.

---

## Phase 2: Choice of Method and Change of Variables

Why this method: to show that a function is constant on an interval it is enough to show that its derivative is zero (Mean Value Theorem). The derivative of a quotient can be computed with the quotient rule, and the ODE lets us replace $y_1'$ and $y_2'$ by $-p\,y_1$ and $-p\,y_2$ without solving anything.

---

## Phase 3: Step-by-Step Derivation

Apply the quotient rule to $r = y_1/y_2$, on $I$ where $y_2 \neq 0$:

$$
r'(t) = \frac{y_1'(t)\,y_2(t) - y_1(t)\,y_2'(t)}{y_2(t)^2}.
$$

Substitute $y_1' = -p\,y_1$ and $y_2' = -p\,y_2$:

$$
r'(t) = \frac{\left(-p\,y_1\right)y_2 - y_1\left(-p\,y_2\right)}{y_2^2} = \frac{-p\,y_1y_2 + p\,y_1y_2}{y_2^2} = 0.
$$

So $r' \equiv 0$ on the interval $I$, and by the Mean Value Theorem $r$ is constant: $y_1(t) = c\,y_2(t)$ with

$$
c = \frac{y_1(t_0)}{y_2(t_0)} \quad\text{for any } t_0 \in I.
$$

---

## Phase 4: Verification, Limits and Interpretation

Consistency with the explicit solution (Problem 2.10): $y_i = y_i(t_0)\,e^{-P(t)}$ with $P(t) = \int_{t_0}^{t}p\,ds$, so $y_1/y_2 = y_1(t_0)/y_2(t_0)$, independent of $t$. Example: $p = 2t$, $y_1 = 3e^{-t^2}$, $y_2 = e^{-t^2}$, ratio $3$.

Interpretation: the solution set of $y' + p y = 0$ is a one-dimensional linear space, spanned by $e^{-P}$. Any two non-trivial solutions are proportional.

Limits: the result requires $y_2 \neq 0$ on the interval, which is guaranteed by the Fact in Phase 1. Without linearity (for example $y' = y^2$) the argument breaks down: the term $-p\,y_i$ is replaced by a non-proportional expression and $r'$ does not vanish.

#### Result

$\dfrac{d}{dt}\left(\dfrac{y_1}{y_2}\right) = 0$, hence $y_1/y_2 \equiv c$ is constant.

---

## Related Notes

- [[04 - Advanced Maths/Concept - Integrating Factor and First-Order Linear Equations|Integrating factor theory]]
- [[04 - Advanced Maths/Problem - Ch2-P10 Uniqueness via Integrating Transformation|Problem 2.10: uniqueness via an integrating transformation]]
