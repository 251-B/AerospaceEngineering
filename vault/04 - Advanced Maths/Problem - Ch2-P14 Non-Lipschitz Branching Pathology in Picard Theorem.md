---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.14"
dificultad: media
tags:
  - problema-resuelto
  - picard-theorem
  - non-uniqueness
  - lipschitz-continuity
  - branching-solutions
---

# Problem 2.14: Non-Lipschitz Branching and Picard's Theorem

Source: ProblemsCh2.pdf, Exercise 14 (page 4). File: sources/cuatrimestre-1/04-advanced-maths/unit-02-first-order-odes/problemas/ProblemsCh2.pdf

Theory reference: Robinson, An Introduction to Ordinary Differential Equations (BookODE's.pdf), Chapter 6, Section 6.2 (Theorem 6.2 and the example with $x^{1/2}$).

## Problem Statement

Given the IVP

$$
\frac{dy}{dt} = 3y^{2/3}, \qquad y(0) = 0,
$$

on the rectangle $R = \{(y,t) \in \mathbb{R}^2 : \lvert y\rvert \leq 1,\ \lvert t\rvert \leq 1\}$. Show that both $y_1(t) = t^3$ and $y_2(t) = 0$ are solutions. Does this contradict Picard's theorem?

---

## Phase 1: Classification, Hypotheses and Domain

Right-hand side $f(y,t) = 3y^{2/3}$, where $y^{2/3} = (y^{1/3})^2 = \lvert y\rvert^{2/3} \geq 0$ is defined for all real $y$ (real cube root). It is continuous on $R$. Its partial derivative is

$$
\frac{\partial f}{\partial y} = 2\,y^{-1/3} \quad (y \neq 0),
$$

which is unbounded as $y \to 0$ and not defined at $y = 0$, which is precisely the initial value $y(0) = 0$. So the hypotheses of Picard's theorem (continuity of $f$ and $\partial f/\partial y$ near the initial point, or a Lipschitz condition in $y$) are not satisfied at $(0,0)$.

---

## Phase 2: Choice of Method and Change of Variables

Why this method: to show that a candidate is a solution of an IVP we verify the ODE and the initial condition by direct substitution. To decide whether the non-uniqueness contradicts Picard's theorem, we test the Lipschitz condition $\lvert f(y,t) - f(\tilde{y},t)\rvert \leq L\lvert y - \tilde{y}\rvert$ near $y = 0$; if it fails, the theorem does not apply and no contradiction arises.

---

## Phase 3: Step-by-Step Derivation

### Verification of $y_1(t) = t^3$

Initial condition: $y_1(0) = 0$. Derivative: $y_1'(t) = 3t^2$. Right-hand side with the real cube root: $y_1^{1/3} = (t^3)^{1/3} = t$, so $y_1^{2/3} = t^2$ and $3y_1^{2/3} = 3t^2$. Both sides agree for all $t$. The graph stays in $R$ for $\lvert t\rvert \leq 1$, since $\lvert y_1\rvert = \lvert t\rvert^3 \leq 1$.

### Verification of $y_2(t) = 0$

$y_2' = 0$ and $3\cdot 0^{2/3} = 0$, and $y_2(0) = 0$. It is a solution, and its graph is inside $R$.

Two distinct solutions, $y_1(t) = t^3$ and $y_2(t) = 0$, of the same IVP exist on $[-1,1]$.

### Failure of the Lipschitz condition

Take $\tilde{y} = 0$ and $y > 0$:

$$
\frac{\lvert f(y,t) - f(0,t)\rvert}{\lvert y - 0\rvert} = \frac{3y^{2/3}}{y} = 3\,y^{-1/3} \longrightarrow +\infty \quad (y \to 0^+).
$$

No constant $L$ bounds this quotient, so $f$ is not Lipschitz in $y$ on any neighborhood of $y = 0$ in $R$. Consistently, $\partial f/\partial y = 2y^{-1/3}$ is unbounded.

### Where the branching comes from

For $y > 0$ the equation is separable: $\dfrac{dy}{3y^{2/3}} = dt$. Integrating, $y^{1/3} = t + c$, so $y = (t + c)^3$ for $t + c > 0$. For every $c \in [0,1]$ define

$$
y_c(t) = \begin{cases} 0, & -1 \leq t \leq c,\\ (t - c)^3, & c < t \leq 1. \end{cases}
$$

At $t = c$ the one-sided derivatives are both $0$ ($\frac{d}{dt}(t-c)^3 = 3(t-c)^2 \to 0$), so $y_c$ is $C^1$, it satisfies the ODE on each piece and $y_c(0) = 0$. Hence the IVP has infinitely many solutions, and $y_2 = 0$ (the limit $c \geq 1$) is a member of the family. Note that $y_c$ with $c = 0$ is $0$ for $t \leq 0$ and $t^3$ for $t > 0$; the function $y_1 = t^3$ on all of $[-1,1]$ is a different solution, obtained by using the negative-side branch $y = (t-c)^3$, $t < c$, with $c = 0$ (valid since $\frac{d}{dt}t^3 = 3t^2 = 3(t^3)^{2/3}$).

---

## Phase 4: Verification, Limits and Interpretation

Answer to the question: no contradiction. Picard's theorem (Robinson, Theorem 6.2) guarantees uniqueness only if $f$ and $\partial f/\partial y$ are continuous (or $f$ is Lipschitz in $y$) near the initial point. Here $f$ is continuous but $\partial f/\partial y = 2y^{-1/3}$ is not defined at $y = 0$ and the Lipschitz quotient is unbounded, so the hypotheses fail exactly at the initial point $(0,0)$. The theorem is silent in that case, and non-uniqueness is possible.

Contrast: for any initial value $y_0 \neq 0$ with $t_0 \in (-1,1)$, $f$ and $\partial f/\partial y$ are continuous in a neighborhood and the solution is unique; the branching occurs only from the equilibrium $y = 0$ (compare Problem 2.9 (iii) and (iv)).

Why the solution can leave $y=0$: the time to travel from $0$ to $y$ is $\int_0^{y} ds/(3s^{2/3}) = y^{1/3}$, which is finite and tends to $0$ as $y \to 0$. For Lipschitz right-hand sides this integral diverges (compare $f = y$, where $\int_0 ds/s = \infty$), so an equilibrium cannot be left in finite time.

#### Result

$y_1 = t^3$ and $y_2 = 0$ both solve $\dot{y} = 3y^{2/3}$, $y(0) = 0$. No contradiction with Picard's theorem: its hypotheses fail at $(0,0)$ because $\partial f/\partial y = 2y^{-1/3}$ is unbounded.

---

## Related Notes

- [[04 - Advanced Maths/Concept - Well-Posed Problems and Picard Theorem|Picard theorem and well-posedness]]
- [[04 - Advanced Maths/Problem - Ch2-P9 Solution Uniqueness and Lipschitz Analysis|Problem 2.9: Lipschitz analysis]]
- [[04 - Advanced Maths/Problem - Ch2-P15 Singular ODE and Domain of Definition|Problem 2.15: a singular equation]]
