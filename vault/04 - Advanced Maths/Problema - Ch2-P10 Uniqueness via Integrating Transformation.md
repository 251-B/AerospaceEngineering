---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.10"
dificultad: media
tags:
  - problema-resuelto
  - uniqueness
  - linear-odes
  - integrating-factor
  - mean-value-theorem
---

# Problem 2.10: Uniqueness via an Integrating Transformation

Source: ProblemsCh2.pdf, Exercise 10 (page 3). File: sources/cuatrimestre-1/04-advanced-maths/unit-02-first-order-odes/problemas/ProblemsCh2.pdf

Theory reference: Robinson, An Introduction to Ordinary Differential Equations (BookODE's.pdf), Section 9.2 (integrating factors); compare Theorem 6.2.

## Problem Statement

Without using Picard's theorem, show that the IVP

$$
\frac{dy}{dt} + p(t)\,y = 0, \qquad y(t_0) = y_0
$$

with $p(t)$ a continuous function has a unique solution, and calculate it. What solution do we obtain if $y_0 = 0$? Hint: consider the function $z(t) = y(t)\,e^{\int_{t_0}^{t}p(s)\,ds}$, where $y(t)$ solves the IVP, show that $z(t)$ is constant and deduce $y(t)$.

---

## Phase 1: Classification, Hypotheses and Domain

Data: $p$ continuous on an open interval $I \ni t_0$; $y_0 \in \mathbb{R}$ arbitrary. A solution is a differentiable function $y: J \to \mathbb{R}$ on an interval $J \subseteq I$ containing $t_0$ with $y' = -p(t)\,y$ and $y(t_0) = y_0$. Linearity of the equation means that no non-linear terms can cause finite-time blow-up, so we may expect solutions on all of $I$.

We must prove two statements: (a) any solution is given by one explicit formula (this gives uniqueness), (b) that formula really is a solution (existence). Picard's theorem is not to be used; only the Fundamental Theorem of Calculus and the fact that a function with zero derivative on an interval is constant (Mean Value Theorem) are allowed.

---

## Phase 2: Choice of Method and Change of Variables

Why this method (the hint): the function $P(t) = \int_{t_0}^{t}p(s)\,ds$ is differentiable with $P' = p$ because $p$ is continuous (Fundamental Theorem of Calculus). The function $e^{P(t)}$ is exactly an integrating factor $\mu$ for $y' + p y = 0$. For any solution $y$, the product $z = y\,e^{P}$ should have zero derivative, which forces $z$ to be constant.

Change of unknown, written explicitly: $z(t) = y(t)\,e^{P(t)}$, $P(t) = \int_{t_0}^{t}p(s)\,ds$, $P(t_0) = 0$, hence $z(t_0) = y_0$.

---

## Phase 3: Step-by-Step Derivation

### Uniqueness

Let $y$ be any solution. Differentiate $z = y\,e^{P}$ with the product rule and the chain rule ($\frac{d}{dt}e^{P} = P'\,e^{P} = p\,e^{P}$):

$$
z'(t) = y'(t)\,e^{P(t)} + y(t)\,p(t)\,e^{P(t)} = e^{P(t)}\left[y'(t) + p(t)\,y(t)\right] = e^{P(t)}\cdot 0 = 0.
$$

A function whose derivative vanishes on an interval is constant (Mean Value Theorem), so $z(t) = z(t_0)$ for all $t \in J$. Evaluate at $t_0$: $z(t_0) = y(t_0)\,e^{0} = y_0$. Hence $y(t)\,e^{P(t)} = y_0$, and since $e^{P(t)} > 0$,

$$
y(t) = y_0\,e^{-P(t)} = y_0\exp\left(-\int_{t_0}^{t}p(s)\,ds\right).
$$

Every solution coincides with this expression, so there is at most one solution.

### Existence

Define $y(t) = y_0\,e^{-P(t)}$ on $I$. It is differentiable, with $y' = y_0\,e^{-P}\cdot(-P') = -p(t)\,y(t)$, i.e. $y' + p y = 0$, and $y(t_0) = y_0 e^{0} = y_0$. So the IVP has this solution on all of $I$.

### The case $y_0 = 0$

The formula gives $y(t) = 0\cdot e^{-P(t)} \equiv 0$, the trivial solution. By the uniqueness just proved it is the only solution with $y(t_0) = 0$. Equivalently: if a solution vanishes at one time $t_1$, apply the result with initial time $t_1$ to get $y \equiv 0$; so a non-trivial solution of this equation never vanishes (since $e^{-P} > 0$, it keeps the sign of $y_0$).

---

## Phase 4: Verification, Limits and Interpretation

Check with $p(t) = 2t$, $t_0 = 0$, $y_0 = 3$: $P = t^2$, $y = 3e^{-t^2}$, $y' = -6t\,e^{-t^2} = -2t\,y$. Correct.

The same formula follows from the integrating-factor method (Problem 2.3): $\mu = e^{P}$, $(\mu y)' = 0$. The point of this exercise is that the argument above proves uniqueness directly, i.e. it does not presuppose the formula.

Interval of existence: the solution exists on the whole interval $I$ where $p$ is continuous, in agreement with the explicit formula, which is finite wherever $p$ is continuous. This contrasts with non-linear equations such as Problem 2.13, where solutions can blow up in finite time.

#### Result

$$
y(t) = y_0\exp\left(-\int_{t_0}^{t}p(s)\,ds\right), \qquad y_0 = 0 \ \Longrightarrow\ y \equiv 0.
$$

---

## Related Notes

- [[04 - Advanced Maths/Concepto - Well-Posed Problems and Picard Theorem|Picard theorem and well-posedness]]
- [[04 - Advanced Maths/Concepto - Factor Integrante y Ecuaciones Lineales de Primer Orden|Integrating factor theory]]
- [[04 - Advanced Maths/Problema - Ch2-P11 Invariance of Solution Ratios in Linear ODEs|Problem 2.11: ratio of solutions]]
- [[04 - Advanced Maths/Problema - Ch2-P17 Direct Difference Method for Uniqueness|Problem 2.17: uniqueness by the difference method]]
