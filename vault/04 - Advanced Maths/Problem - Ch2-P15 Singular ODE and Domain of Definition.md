---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.15"
dificultad: media
tags:
  - problema-resuelto
  - singular-odes
  - separable-equations
  - non-uniqueness
  - domain-of-definition
---

# Problem 2.15: Singular ODE and Domain of Definition

Source: ProblemsCh2.pdf, Exercise 15 (page 4). File: sources/cuatrimestre-1/04-advanced-maths/unit-02-first-order-odes/problemas/ProblemsCh2.pdf

Theory reference: Robinson, An Introduction to Ordinary Differential Equations (BookODE's.pdf), Chapter 6, Section 6.2 (Theorem 6.2) and Chapter 8 (separable equations).

## Problem Statement

Consider the differential equation

$$
\frac{dy}{dt} = \frac{2y + 1}{t}.
$$

Compute the general solution and show that there are two solutions such that $y(0) = -1/2$. Does this contradict the uniqueness theorem?

---

## Phase 1: Classification, Hypotheses and Domain

Right-hand side $f(y,t) = (2y+1)/t$. It is continuous, together with $\partial f/\partial y = 2/t$, on each of the half-planes $t > 0$ and $t < 0$, but it is not defined on the line $t = 0$. So the equation is singular at $t = 0$; any solution of the differential equation in the usual sense is defined on $t > 0$ or on $t < 0$ separately. On each half-plane Theorem 6.2 gives a unique solution through every point.

Equilibrium on $t \neq 0$: $2y + 1 = 0$, i.e. $y \equiv -\frac12$.

---

## Phase 2: Choice of Method and Change of Variables

Why this method: the equation is separable ($g(t) = 1/t$, $h(y) = 2y+1$) and also linear. We solve it by separation of variables on each half-line $t \neq 0$, and use the integrating-factor method as an independent check. Then we study what happens at $t = 0$, where the hypotheses of the uniqueness theorem fail.

Change of variables written explicitly: $u = 2y + 1$, $du = 2\,dy$, which reduces the equation to $du/dt = 2u/t$.

---

## Phase 3: Step-by-Step Derivation

### General solution by separation of variables

Equilibrium $y \equiv -\frac12$. For $y \neq -\frac12$ and $t \neq 0$, separate:

$$
\frac{dy}{2y+1} = \frac{dt}{t}.
$$

Integrate, with $u = 2y + 1$, $dy = du/2$ on the left:

$$
\frac12\ln\lvert 2y+1\rvert = \ln\lvert t\rvert + c \quad\Longrightarrow\quad \lvert 2y + 1\rvert = e^{2c}\,t^2.
$$

Let $C = \pm e^{2c} \in \mathbb{R}\setminus\{0\}$. Then $2y + 1 = C\,t^2$. The equilibrium corresponds to $C = 0$, so

$$
y(t) = -\frac12 + \frac{C}{2}\,t^2 = -\frac12 + k\,t^2, \qquad k \in \mathbb{R}.
$$

Independent check with an integrating factor on $t > 0$: $y' - \frac{2}{t}y = \frac1t$, $\mu = e^{-2\ln t} = t^{-2}$, $(t^{-2}y)' = t^{-3}$, so $t^{-2}y = -\frac{1}{2}t^{-2} + k$ and $y = -\frac12 + k\,t^2$, the same family. On $t < 0$ the same formula holds with $\mu = t^{-2}$ again. The constants $k$ on $t > 0$ and on $t < 0$ are independent because the two half-lines are disconnected.

### Solutions through $y(0) = -\frac12$

Every member of the family has the limit $y(t) \to -\frac12 + 0 = -\frac12$ as $t \to 0$. So each of them extends continuously to $t = 0$ with $y(0) = -\frac12$, whatever $k$ is. In particular, for $k = 0$ and $k = 1$:

$$
y_a(t) = -\frac12, \qquad y_b(t) = -\frac12 + t^2, \qquad\text{both satisfy } y(0) = -\frac12.
$$

Both are smooth on all of $\mathbb{R}$ and satisfy the equation in the form $t\,y' = 2y + 1$ at $t = 0$ as well (both sides vanish there: $0 = 0$). Hence there are two (in fact infinitely many, one for each $k$, and even different constants $k_+$, $k_-$ for $t>0$ and $t<0$, which still give a $C^1$ function at $t = 0$) solutions of the IVP.

Conversely, no solution can have $y(0) = y_0 \neq -\frac12$: from $2y + 1 = C t^2$ we get $y \to -\frac12$ as $t \to 0$. So the initial value problem at $t = 0$ is solvable only for $y_0 = -\frac12$, and then it has infinitely many solutions.

---

## Phase 4: Verification, Limits and Interpretation

Substitution check: for $y = -\frac12 + k\,t^2$, $y' = 2kt$, and $\frac{2y+1}{t} = \frac{2kt^2}{t} = 2kt$. Equal for $t \neq 0$.

Does this contradict the uniqueness theorem? No. The theorem requires $f(y,t)$ and $\partial f/\partial y$ to be continuous in a neighborhood of the initial point $(t_0, y_0) = (0, -\frac12)$. Here $f = (2y+1)/t$ is not even defined at $t = 0$, and $\partial f/\partial y = 2/t$ is unbounded as $t \to 0$; no neighborhood of $(0,-\frac12)$ lies inside a region where the hypotheses hold. The multiple solutions all pass through the singular point of the equation. For any initial time $t_0 \neq 0$ the solution is unique, in agreement with the theorem.

Domain of definition: a genuine solution of $y' = (2y+1)/t$ lives on $t > 0$ or $t < 0$. The functions above are solutions of the equation on each half-line and extend to $t = 0$ as solutions of the equivalent form $t\,y' = 2y + 1$, whose coefficient of $y'$ vanishes at $t = 0$; this is why uniqueness is lost there.

#### Result

General solution $y = -\frac12 + k\,t^2$. Through $y(0) = -\frac12$ pass infinitely many solutions (for instance $y = -\frac12$ and $y = -\frac12 + t^2$). No contradiction with the uniqueness theorem, because $f$ is singular at $t = 0$.

---

## Related Notes

- [[04 - Advanced Maths/Concept - Well-Posed Problems and Picard Theorem|Picard theorem and well-posedness]]
- [[04 - Advanced Maths/Concept - Direct Integration and Separable Equations|Direct integration and separable equations]]
- [[04 - Advanced Maths/Problem - Ch2-P14 Non-Lipschitz Branching Pathology in Picard Theorem|Problem 2.14: non-Lipschitz branching]]
