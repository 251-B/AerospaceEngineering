---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.17"
dificultad: media
tags:
  - problema-resuelto
  - uniqueness
  - existence
  - difference-method
  - energy-method
  - linear-odes
---

# Problem 2.17: Direct Difference Method for Uniqueness

Source: ProblemsCh2.pdf, Exercise 17 (page 4). File: sources/cuatrimestre-1/04-advanced-maths/unit-02-first-order-odes/problemas/ProblemsCh2.pdf

Theory reference: Robinson, An Introduction to Ordinary Differential Equations (BookODE's.pdf), Section 5.2 (general solutions and initial conditions) and Section 9.1 (constant coefficients).

## Problem Statement

Show existence and uniqueness for the initial value problem (IVP)

$$
\frac{dy}{dt} + a\,y = 0, \qquad y(t_0) = y_0.
$$

For existence, just find a solution by inspection. Then suppose that there are two different solutions and argue that they have to be the same by taking their difference.

---

## Phase 1: Classification, Hypotheses and Domain

Data: a constant $a \in \mathbb{R}$ (of either sign), an initial time $t_0$ and an initial value $y_0 \in \mathbb{R}$. A solution is a differentiable function $y: \mathbb{R} \to \mathbb{R}$ with $y' + a y = 0$ and $y(t_0) = y_0$. This is a special case of $y' + p(t)y = 0$ with $p \equiv a$ continuous, so the result also follows from Problem 2.10 or from Picard's theorem; here we are asked for a direct proof.

We prove two statements: (E) a solution exists, (U) two solutions of the same IVP coincide. Tools allowed: differentiation, linearity of the derivative, and the fact that a function with zero derivative on an interval is constant (Mean Value Theorem).

---

## Phase 2: Choice of Method and Change of Variables

Existence by inspection: the exponential function reproduces itself under differentiation up to a constant factor, which is exactly the behavior required by $y' = -a\,y$. We propose $y(t) = y_0 e^{-a(t - t_0)}$ and verify it.

Uniqueness by the difference: since the equation is linear and homogeneous, the difference of two solutions solves the same equation with zero initial data. So it is enough to prove that the only solution of $w' + a w = 0$, $w(t_0) = 0$, is $w \equiv 0$. Two routes are given.

- Approach A (squared difference): $E = w^2 \geq 0$ satisfies $E' = -2a\,E$, and $\left(E\,e^{2a(t-t_0)}\right)' = 0$.
- Approach B (integrating factor): $\left(w\,e^{a(t-t_0)}\right)' = 0$ directly.

In both approaches we must not write down the solution formula of the equation for $w$ or $E$, because that formula presupposes the uniqueness we are proving. We only differentiate a product and apply the Mean Value Theorem.

---

## Phase 3: Step-by-Step Derivation

### Existence

Candidate: $y(t) = y_0\,e^{-a(t - t_0)}$. Initial condition: $y(t_0) = y_0 e^{0} = y_0$. Differentiate with the chain rule, $\frac{d}{dt}\left[-a(t - t_0)\right] = -a$:

$$
y'(t) = y_0\,e^{-a(t-t_0)}\cdot(-a) = -a\,y(t) \quad\Longrightarrow\quad y'(t) + a\,y(t) = 0 \quad \forall t \in \mathbb{R}.
$$

So $y$ is a solution and existence is proved.

### Uniqueness: the difference

Let $y_1, y_2$ be two solutions of the same IVP and define $w = y_1 - y_2$. Then $w(t_0) = y_0 - y_0 = 0$, and by linearity of the derivative

$$
w' + a\,w = (y_1' + a y_1) - (y_2' + a y_2) = 0 - 0 = 0.
$$

### Approach A: squared difference

Let $E(t) = w(t)^2 \geq 0$. By the chain rule, $E' = 2\,w\,w'$, and using $w' = -a\,w$:

$$
E' = 2w\,(-a\,w) = -2a\,w^2 = -2a\,E, \qquad\text{i.e.}\quad E' + 2a\,E = 0.
$$

Multiply by $e^{2a(t - t_0)}$ and use the product rule:

$$
\frac{d}{dt}\left[E(t)\,e^{2a(t-t_0)}\right] = \left(E' + 2a\,E\right)e^{2a(t-t_0)} = 0.
$$

By the Mean Value Theorem, $E(t)\,e^{2a(t-t_0)}$ is constant, equal to its value at $t_0$, which is $E(t_0)\,e^{0} = w(t_0)^2 = 0$. Since $e^{2a(t-t_0)} > 0$, we can divide:

$$
E(t) = 0 \quad \forall t \in \mathbb{R}, \qquad\text{so}\quad w(t)^2 = 0 \ \Longrightarrow\ w(t) = 0.
$$

This holds for either sign of $a$. The shorter argument 'E decreases and is non-negative, hence zero' would only work for $a \geq 0$ and forward in time, which is why the product $E\,e^{2a(t-t_0)}$ is used.

### Approach B: integrating factor on $w$

Multiply $w' + a w = 0$ by $e^{a(t-t_0)}$:

$$
\frac{d}{dt}\left[w(t)\,e^{a(t-t_0)}\right] = \left(w' + a\,w\right)e^{a(t-t_0)} = 0.
$$

By the Mean Value Theorem $w(t)\,e^{a(t-t_0)} = w(t_0)\,e^{0} = 0$, and since the exponential never vanishes, $w(t) = 0$ for all $t$.

In both approaches $w \equiv 0$, i.e. $y_1 \equiv y_2$. Uniqueness is proved.

---

## Phase 4: Verification, Limits and Interpretation

Numerical sanity check: $a = 2$, $t_0 = 1$, $y_0 = 3$: $y(t) = 3e^{-2(t-1)}$, $y(1) = 3$, $y'(t) = -6e^{-2(t-1)} = -2y$. For $a = -1.5$ the same formula gives exponential growth, and the uniqueness argument is unchanged.

Why the restriction to the difference is legitimate: linearity. For a non-linear equation, the difference of two solutions would not solve the same equation and more work (a Lipschitz estimate or Gronwall's inequality) would be needed, which is the content of Picard's theorem.

Relation to other exercises: Approach B is exactly the proof of Problem 2.10 with $p \equiv a$ and $y_0 = 0$; Approach A uses the quantity $w^2$, the one-dimensional analogue of an energy functional.

#### Result

Existence: $y(t) = y_0\,e^{-a(t-t_0)}$. Uniqueness: the difference $w$ of two solutions satisfies $w' + a w = 0$, $w(t_0) = 0$, and both $\left(w^2 e^{2a(t-t_0)}\right)' = 0$ and $\left(w\,e^{a(t-t_0)}\right)' = 0$ force $w \equiv 0$.

---

## Related Notes

- [[04 - Advanced Maths/Concept - Well-Posed Problems and Picard Theorem|Picard theorem and well-posedness]]
- [[04 - Advanced Maths/Problem - Ch2-P10 Uniqueness via Integrating Transformation|Problem 2.10: uniqueness via an integrating transformation]]
