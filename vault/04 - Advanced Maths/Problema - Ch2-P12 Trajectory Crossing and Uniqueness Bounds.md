---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.12"
dificultad: media
tags:
  - problema-resuelto
  - uniqueness
  - no-crossing
  - comparison
  - intermediate-value-theorem
---

# Problem 2.12: Trajectory Crossing and Uniqueness Bounds

Source: ProblemsCh2.pdf, Exercise 12 (page 3). File: sources/cuatrimestre-1/04-advanced-maths/unit-02-first-order-odes/problemas/ProblemsCh2.pdf

Theory reference: Robinson, An Introduction to Ordinary Differential Equations (BookODE's.pdf), Chapter 6, Section 6.2 (Theorem 6.2).

## Problem Statement

Consider $\dfrac{dy}{dt} = f(y,t)$, where $f$ satisfies the hypothesis of the existence and uniqueness theorem. Suppose that

(i) $y_1(t) = -2$ for all $t$ is a solution and we are studying a different solution for which $y(0) = 0$.  
(ii) $y_1(t) = -t - 1$ and $y_2(t) = t^2 + 1$ are solutions and $y(0) = 0$.  

Based on the uniqueness theorem, what can you conclude about the solutions in each case?

---

## Phase 1: Classification, Hypotheses and Domain

Hypothesis of the theorem: $f$ and $\partial f/\partial y$ are continuous on an open set $\Omega \subseteq \mathbb{R}^2$ containing the graphs of all the solutions considered. Then through every point $(t_*, y_*) \in \Omega$ passes exactly one solution (on its maximal interval of existence).

Consequence used below (no-crossing principle): if two solutions $u, v$ of this ODE satisfy $u(t_*) = v(t_*)$ at some time $t_*$ in the common interval, then they solve the same IVP at $t_*$, so $u \equiv v$ on the common interval. Contrapositive: two different solutions never meet. Hence $u - v$ has no zeros on the common interval.

The function $f$ is not given explicitly, and we only use that the theorem applies. All conclusions are therefore restricted to the common interval of existence $J \ni 0$ of the solutions involved (a connected interval containing $t = 0$).

---

## Phase 2: Choice of Method and Change of Variables

Why this method: the Intermediate Value Theorem states that a continuous function with no zeros on an interval has constant sign there. Apply it to $u - v$ for two solutions that never meet. The sign at $t = 0$, known from the initial data, then fixes the sign on all of $J$. This gives bounds without knowing $f$.

---

## Phase 3: Step-by-Step Derivation

### Part (i): $y_1 \equiv -2$ and a different solution $y$ with $y(0) = 0$

$y_1$ is a solution and $y \not\equiv y_1$ (indeed $y(0) = 0 \neq -2 = y_1(0)$). Define $d(t) = y(t) - y_1(t) = y(t) + 2$. By the no-crossing principle, $d(t) \neq 0$ for all $t \in J$. $d$ is continuous and $d(0) = 0 + 2 = 2 > 0$. By the Intermediate Value Theorem, a continuous function that changes sign must vanish somewhere between; since $d$ never vanishes, it keeps the sign it has at $t=0$:

$$
y(t) + 2 > 0 \quad\Longleftrightarrow\quad y(t) > -2 \qquad \text{for all } t \in J.
$$

Conclusion: the solution starting at $y(0) = 0$ stays strictly above the constant solution $y = -2$ for all time; it is bounded below by $-2$ and can never reach it.

### Part (ii): $y_1 = -t-1$, $y_2 = t^2 + 1$ and a solution $y$ with $y(0) = 0$

First, check how the two given solutions are placed with respect to each other: $y_2(t) - y_1(t) = t^2 + t + 2$. Its discriminant is $1 - 8 = -7 < 0$, so $t^2 + t + 2 > 0$ for all $t$ (its minimum is $7/4$ at $t = -\frac12$). So $y_1 < y_2$ for all $t$, consistent with the no-crossing principle (they never meet).

Initial position of $y$: $y_1(0) = -1$, $y_2(0) = 1$, so $y_1(0) < y(0) = 0 < y_2(0)$. Apply the argument to each pair. $d_1 = y - y_1$ is continuous, $d_1(0) = 0 - (-1) = 1 > 0$ and never vanishes, hence $d_1 > 0$ on $J$. $d_2 = y_2 - y$ is continuous, $d_2(0) = 1 - 0 = 1 > 0$ and never vanishes, hence $d_2 > 0$ on $J$. Therefore

$$
-t - 1 < y(t) < t^2 + 1 \qquad \text{for all } t \in J.
$$

The solution is trapped between the two given solutions for as long as it exists.

---

## Phase 4: Verification, Limits and Interpretation

Sanity check of the geometry: in (i), the line $y = -2$ and the curve $y(t)$ with $y(0) = 0$ are separated by a vertical gap $2$ at $t = 0$; the gap is positive for all $t$. In (ii), the vertical gap between $y_1$ and $y_2$ at $t=0$ is $2$ and $y(0) = 0$ lies strictly inside; at $t = 1$ the bounds are $-2 < y(1) < 2$, and at $t = -1$ they are $0 < y(-1) < 2$.

Limits of the conclusion: it holds only on the common interval of existence $J$; the bounds say nothing about whether $y$ exists globally. If $f$ were not Lipschitz (for example $y' = 3y^{2/3}$, Problem 2.14), different solutions could touch or merge, and the bounds would be lost.

The data in (ii) are a consistency condition for $f$ as well: two solutions that do not meet can coexist, whereas two that cross (say $y_1 = t$, $y_2 = -t$ intersecting at $t = 0$) would contradict the uniqueness hypothesis.

#### Conclusions

(i) $y(t) > -2$ for all $t$ in the interval of existence. (ii) $-t - 1 < y(t) < t^2 + 1$ for all $t$ in the interval of existence.

---

## Related Notes

- [[04 - Advanced Maths/Concepto - Well-Posed Problems and Picard Theorem|Picard theorem and well-posedness]]
- [[04 - Advanced Maths/Problema - Ch2-P13 Multi-Equilibria Autonomous Phase Line Dynamics|Problem 2.13: barriers on the phase line]]
