---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
origen: "probls_ch4-i_2627_v2.pdf - Exercise 1"
dificultad: media
id: "e1"
pill: "Reduction to a System • Existence and Uniqueness"
tags:
  - problema-resuelto
  - sistemas
  - reduccion-de-orden
  - unicidad
---

# Problem 4.I.1: An n-th Order Equation as a First-Order System and Its Uniqueness

> Official exercise 1 of the sheet `probls_ch4-i_2627_v2.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 4 Part 1]]. Method and notation: [[Concept - Planar Systems with Complex Eigenvalues]].

## Statement

By choosing an appropriate collection of new variables $x_1, \dots, x_n$, rewrite the $n$th order differential equation

$$ \frac{d^nx}{dt^n} = f\left(\frac{d^{n-1}x}{dt^{n-1}}, \dots, \frac{dx}{dt}, x, t\right) $$

as a set of $n$ coupled linear first order equations. Find the conditions on the function $f(x_n, \dots, x_1, t)$ for the original differential equation to have a unique solution.

## Phase 1: Setup and hypotheses

Unknown: $x(t)$, $n$ times differentiable on an interval $I$. Data: $f(x_n, \dots, x_1, t)$ defined on a region $\Omega \subset \mathbb R^{n+1}$. The initial value problem prescribes the $n$ numbers $x(t_0), \dot x(t_0), \dots, x^{(n-1)}(t_0)$. The tool for uniqueness is the existence and uniqueness theorem for first-order systems $\dot{\mathbf x} = \mathbf F(\mathbf x, t)$ (Robinson Thm 25.2, Topic 4 Sec. 1).

## Phase 2: Formulation: the new variables

Introduce one variable for the function and for each derivative below the highest order (Robinson Sec. 25.1):

$$ x_1 = x,\quad x_2 = \frac{dx}{dt},\quad x_3 = \frac{d^2x}{dt^2},\quad \dots,\quad x_n = \frac{d^{n-1}x}{dt^{n-1}}, \qquad\text{i.e. } x_k = x^{(k-1)}\ (k = 1, \dots, n) $$

> [!info] Method of the class notes [Notes, p. 9]
> The important point of the notes: an ODE of order $n \ge 2$ is a system of $n$ first-order ODEs; for $\ddot x = f(\dot x, x, t)$ they set $x_1 = x$, $x_2 = \dot x$, so that $\dot x_1 = x_2$ and $\dot x_2 = f(x_2, x_1, t)$. The variables above are the same choice for order $n$. Uniqueness then follows from the condition the notes state for systems: $\mathbf f$ and its Jacobian $D\mathbf f$ continuous near $(\mathbf x_0, t_0)$. Only the last component $f$ is not trivial, so the condition falls on $f$ and its partial derivatives $\partial f/\partial x_k$.

## Phase 3: Derivation

#### The system

By construction $\dot x_k = x^{(k)} = x_{k+1}$ for $k = 1, \dots, n - 1$, and $\dot x_n = x^{(n)} = f(x_n, \dots, x_1, t)$ by the original equation:

$$ \begin{aligned} \dot x_1 &= x_2 \\ \dot x_2 &= x_3 \\ &\ \,\vdots \\ \dot x_{n-1} &= x_n \\ \dot x_n &= f(x_n, x_{n-1}, \dots, x_1, t) \end{aligned} \qquad\Longleftrightarrow\qquad \dot{\mathbf x} = \mathbf F(\mathbf x, t) = \begin{pmatrix} x_2 \\ x_3 \\ \vdots \\ x_n \\ f(x_n, \dots, x_1, t) \end{pmatrix} $$

The first $n - 1$ equations are linear in the unknowns (they say $\dot x_k = x_{k+1}$); the last one is linear exactly when $f$ is a linear function of $x_1, \dots, x_n$ (as for a linear ODE, where the whole system is linear, $\dot{\mathbf x} = A(t)\mathbf x + \mathbf b(t)$). The first-order system form is valid for any $f$.

#### Equivalence

(a) If $x$ solves the $n$th-order equation, then $\mathbf x = (x, \dot x, \dots, x^{(n-1)})^T$ solves the system. (b) Conversely, if $(x_1, \dots, x_n)$ solves the system, then $\dot x_1 = x_2$, $\ddot x_1 = \dot x_2 = x_3$, ..., $x_1^{(k)} = x_{k+1}$ for $k \leq n - 1$, and $x_1^{(n)} = \dot x_n = f(x_n, \dots, x_1, t) = f(x_1^{(n-1)}, \dots, \dot x_1, x_1, t)$: the function $x = x_1$ solves the original equation. The initial condition $\mathbf x(t_0) = (x_1^0, \dots, x_n^0)$ is exactly $x(t_0) = x_1^0$, $\dot x(t_0) = x_2^0$, ..., $x^{(n-1)}(t_0) = x_n^0$.

#### Conditions for a unique solution

Theorem 25.2 (Robinson p. 250) requires $\mathbf F$ and the matrix of partial derivatives $D\mathbf F$ to be continuous on an open set containing the initial point. Compute it row by row: for $F_k = x_{k+1}$ ($k < n$) the partial derivatives are $0$ or $1$, and for $F_n = f$ they are $\partial f/\partial x_j$:

$$ D\mathbf F = \begin{pmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 1 & \cdots & 0 \\ \vdots & & & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & 1 \\ \dfrac{\partial f}{\partial x_1} & \dfrac{\partial f}{\partial x_2} & \dfrac{\partial f}{\partial x_3} & \cdots & \dfrac{\partial f}{\partial x_n} \end{pmatrix} $$

The first $n - 1$ rows are constant, hence continuous. Therefore all the conditions reduce to the last row:

> [!result] Condition for uniqueness
> **$f(x_n, \dots, x_1, t)$ and its partial derivatives $\partial f/\partial x_j$, $j = 1, \dots, n$, must be continuous in an open region containing the initial point $(x(t_0), \dots, x^{(n-1)}(t_0), t_0)$.** Then the IVP has exactly one solution on some interval around $t_0$ (local existence and uniqueness), and two solutions with the same $x(t_0), \dots, x^{(n-1)}(t_0)$ coincide wherever both exist.

## Phase 4: Interpretation and checks

- For $n = 2$ the system is $\dot x_1 = x_2$, $\dot x_2 = f(x_2, x_1, t)$ and the condition is Theorem 11.1 of Topic 3 (continuity of $f$, $\partial f/\partial x_1$, $\partial f/\partial x_2$); for $n = 1$ it is Picard's theorem.
- No condition on $\partial f/\partial t$ is needed: the theorem asks continuity in $t$ but no differentiability in $t$.
- Dependence on the $n$ derivatives: continuity of the partial derivatives $\partial f/\partial x_j$ gives a local Lipschitz bound in $(x_1, \dots, x_n)$, which is what excludes branching solutions (compare Exercise 2.14 of Chapter 2, where the Lipschitz condition fails).
- For a linear equation $x^{(n)} + a_{n-1}(t)x^{(n-1)} + \dots + a_0(t)x = g(t)$, $f = g - \sum a_{k}x_{k+1}$ and $\partial f/\partial x_{k+1} = -a_k(t)$: the conditions reduce to continuity of the $a_k$ and $g$. For linear equations the solution in fact exists on the whole interval of continuity of the coefficients (a standard result for linear systems, not in Robinson Thm 25.2, which is local; see the continuation argument in Exercise 4).
- Check with the mass-spring-damper (Topic 4 Sec. 1.1): $n = 2$, $f = -\lambda x_2 - \omega^2x_1$ has constant partial derivatives $-\omega^2$ and $-\lambda$: unique solutions for all data.
