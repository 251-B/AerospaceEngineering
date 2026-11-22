---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 3"
dificultad: media
id: "e3"
pill: "Cooperation • Bounded vs Unbounded Growth"
tags:
  - problema-resuelto
  - sistemas-no-lineales
  - retrato-de-fase
---

# Problem 5.3: Two Cooperative Species Models

> Official exercise 3 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Theory and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

The situation in which two species cooperate, so that the presence of one enhances the environment for the other, can be modelled by a coupled pair of equations of the form

$$
\dot x = x(A - ax + by), \qquad \dot y = y(B + cx - dy),
$$

where all the parameters are positive. Sketch the phase portraits for the following cooperative equations:

(i) $\dot x = x(1 - x + y)$, $\dot y = y(1 + x - 2y)$,

(ii) $\dot x = x(2 - x + y)$, $\dot y = y(4 + 2x - y)$.

## Setting up the system

We begin by identifying the positive parameters $(A, a, b, B, c, d)$ in each model and noting the invariant coordinate axes. In both models, $x = 0 \implies \dot x = 0$ and $y = 0 \implies \dot y = 0$, so the first quadrant $x \ge 0, y \ge 0$ is positively invariant. Both species grow logistically in isolation (with carrying capacities $A/a$ and $B/d$), while the positive cross-terms $+bxy$ and $+cxy$ represent mutual benefit (cooperation). The qualitative outcome depends on the balance between self-limitation ($ad$) and mutual enhancement ($bc$).

### (i) Weak cooperation ($ad > bc$)

Here $\dot x = x(1 - x + y)$ and $\dot y = y(1 + x - 2y)$, so $A = 1$, $a = 1$, $b = 1$, $B = 1$, $c = 1$, $d = 2$. Self-limitation dominates cooperation because $ad = 1 \cdot 2 = 2 > bc = 1 \cdot 1 = 1$.

### (ii) Strong cooperation ($ad < bc$)

Here $\dot x = x(2 - x + y)$ and $\dot y = y(4 + 2x - y)$, so $A = 2$, $a = 1$, $b = 1$, $B = 4$, $c = 2$, $d = 1$. Mutual enhancement overwhelms self-limitation because $ad = 1 \cdot 1 = 1 < bc = 1 \cdot 2 = 2$.

## Step 1: Critical points

We find all stationary points $(x^*, y^*)$ in the biologically meaningful region $x \ge 0, y \ge 0$ by setting $\dot x = 0$ and $\dot y = 0$ simultaneously.

### (i) Critical points of $\dot x = x(1 - x + y)$, $\dot y = y(1 + x - 2y)$

Solving $x(1 - x + y) = 0$ and $y(1 + x - 2y) = 0$:

1. $x = 0$, $y = 0 \implies A(0, 0)$.
2. $y = 0$, $1 - x = 0 \implies x = 1 \implies B(1, 0)$.
3. $x = 0$, $1 - 2y = 0 \implies y = \frac{1}{2} \implies C\bigl(0, \tfrac{1}{2}\bigr)$.
4. Interior equilibrium: solve $1 - x + y = 0$ (i.e. $x - y = 1$) and $1 + x - 2y = 0$ (i.e. $-x + 2y = 1$). Adding the two equations eliminates $x$:
   $$
   (x - y) + (-x + 2y) = 1 + 1 \;\Longrightarrow\; y^* = 2, \qquad x^* = 1 + y^* = 3.
   $$
   Thus $D(3, 2)$ lies in the first quadrant.

### (ii) Critical points of $\dot x = x(2 - x + y)$, $\dot y = y(4 + 2x - y)$

Solving $x(2 - x + y) = 0$ and $y(4 + 2x - y) = 0$:

1. $x = 0$, $y = 0 \implies A(0, 0)$.
2. $y = 0$, $2 - x = 0 \implies x = 2 \implies B(2, 0)$.
3. $x = 0$, $4 - y = 0 \implies y = 4 \implies C(0, 4)$.
4. Fourth system: solve $2 - x + y = 0 \implies y = x - 2$ and $4 + 2x - y = 0 \implies y = 2x + 4$. Equating the two expressions for $y$:
   $$
   x - 2 = 2x + 4 \;\Longrightarrow\; x = -6, \qquad y = -6 - 2 = -8.
   $$
   Because $(-6, -8)$ lies in the third quadrant, there is **no fourth (interior) stationary point in $x, y \ge 0$**.

## Step 2: Linearization

We compute the Jacobian matrix $J(x,y)$ from the partial derivatives of $f(x,y)$ and $g(x,y)$ and evaluate it at every stationary point in $x, y \ge 0$.

### (i) Jacobian matrices

Expanding $f(x,y) = x - x^2 + xy$ and $g(x,y) = y + xy - 2y^2$:

$$
\frac{\partial f}{\partial x} = 1 - 2x + y, \quad \frac{\partial f}{\partial y} = x, \quad \frac{\partial g}{\partial x} = y, \quad \frac{\partial g}{\partial y} = 1 + x - 4y.
$$

Evaluating at $A(0,0)$, $B(1,0)$, $C\bigl(0, \tfrac{1}{2}\bigr)$, and $D(3,2)$:

$$
J(0,0) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad J(1,0) = \begin{pmatrix} -1 & 1 \\ 0 & 2 \end{pmatrix}, \qquad J\!\left(0, \frac{1}{2}\right) = \begin{pmatrix} \frac{3}{2} & 0 \\ \frac{1}{2} & -1 \end{pmatrix},
$$

$$
J(3,2) = \begin{pmatrix} 1 - 6 + 2 & 3 \\ 2 & 1 + 3 - 8 \end{pmatrix} = \begin{pmatrix} -3 & 3 \\ 2 & -4 \end{pmatrix}.
$$

### (ii) Jacobian matrices

Expanding $f(x,y) = 2x - x^2 + xy$ and $g(x,y) = 4y + 2xy - y^2$:

$$
\frac{\partial f}{\partial x} = 2 - 2x + y, \quad \frac{\partial f}{\partial y} = x, \quad \frac{\partial g}{\partial x} = 2y, \quad \frac{\partial g}{\partial y} = 4 + 2x - 2y.
$$

Evaluating at $A(0,0)$, $B(2,0)$, and $C(0,4)$:

$$
J(0,0) = \begin{pmatrix} 2 & 0 \\ 0 & 4 \end{pmatrix}, \qquad J(2,0) = \begin{pmatrix} -2 & 2 \\ 0 & 8 \end{pmatrix}, \qquad J(0,4) = \begin{pmatrix} 6 & 0 \\ 8 & -4 \end{pmatrix}.
$$

## Step 3: Local study

We solve the characteristic equation $\det(J - \lambda I) = 0$ and find the eigenvectors row by row at each critical point to classify the local phase portrait.

### (i) Local classification

- **$A(0,0)$:** $J(0,0) = I$, so $(1 - \lambda)^2 = 0 \implies \lambda_1 = \lambda_2 = 1 > 0$ with two independent eigenvectors $(1,0)^T, (0,1)^T$. **Unstable star.**
- **$B(1,0)$:** Upper triangular, so $(-1 - \lambda)(2 - \lambda) = 0 \implies \lambda_1 = -1 < 0$, $\lambda_2 = 2 > 0$. **Saddle point.**
  - For $\lambda_1 = -1$: $\begin{pmatrix} 0 & 1 \\ 0 & 3 \end{pmatrix}\vec v_1 = \vec 0 \implies v_2 = 0 \implies \vec v_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$.
  - For $\lambda_2 = 2$: $\begin{pmatrix} -3 & 1 \\ 0 & 0 \end{pmatrix}\vec v_2 = \vec 0 \implies -3v_1 + v_2 = 0 \implies \vec v_2 = \begin{pmatrix} 1 \\ 3 \end{pmatrix}$.
- **$C\bigl(0, \tfrac{1}{2}\bigr)$:** Lower triangular, so $\bigl(\frac{3}{2} - \lambda\bigr)(-1 - \lambda) = 0 \implies \lambda_1 = \frac{3}{2} > 0$, $\lambda_2 = -1 < 0$. **Saddle point.**
  - For $\lambda_1 = \frac{3}{2}$: $\begin{pmatrix} 0 & 0 \\ 1/2 & -5/2 \end{pmatrix}\vec v_1 = \vec 0 \implies \frac{1}{2}v_1 - \frac{5}{2}v_2 = 0 \implies \vec v_1 = \begin{pmatrix} 5 \\ 1 \end{pmatrix}$.
  - For $\lambda_2 = -1$: $\begin{pmatrix} 5/2 & 0 \\ 1/2 & 0 \end{pmatrix}\vec v_2 = \vec 0 \implies v_1 = 0 \implies \vec v_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.
- **$D(3,2)$:** Expanding $\det(J(3,2) - \lambda I) = 0$:
  $$
  (-3 - \lambda)(-4 - \lambda) - (3)(2) = \lambda^2 + 7\lambda + 12 - 6 = \lambda^2 + 7\lambda + 6 = (\lambda + 1)(\lambda + 6) = 0.
  $$
  Hence $\lambda_1 = -1 < 0$ and $\lambda_2 = -6 < 0$: **stable node**.
  - For $\lambda_1 = -1$: $\begin{pmatrix} -2 & 3 \\ 2 & -3 \end{pmatrix}\vec v_1 = \vec 0 \implies -2v_1 + 3v_2 = 0 \implies \vec v_1 = \begin{pmatrix} 3 \\ 2 \end{pmatrix}$ (slow direction).
  - For $\lambda_2 = -6$: $\begin{pmatrix} 3 & 3 \\ 2 & 2 \end{pmatrix}\vec v_2 = \vec 0 \implies v_1 + v_2 = 0 \implies \vec v_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$ (fast direction).

### (ii) Local classification

- **$A(0,0)$:** Diagonal, so $(2 - \lambda)(4 - \lambda) = 0 \implies \lambda_1 = 2 > 0$ with $\vec v_1 = (1,0)^T$, $\lambda_2 = 4 > 0$ with $\vec v_2 = (0,1)^T$. **Unstable node** (trajectories leave tangent to the $x$-axis).
- **$B(2,0)$:** Upper triangular, so $(-2 - \lambda)(8 - \lambda) = 0 \implies \lambda_1 = -2 < 0$, $\lambda_2 = 8 > 0$. **Saddle point.**
  - For $\lambda_1 = -2$: $\begin{pmatrix} 0 & 2 \\ 0 & 10 \end{pmatrix}\vec v_1 = \vec 0 \implies v_2 = 0 \implies \vec v_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$.
  - For $\lambda_2 = 8$: $\begin{pmatrix} -10 & 2 \\ 0 & 0 \end{pmatrix}\vec v_2 = \vec 0 \implies -10v_1 + 2v_2 = 0 \implies \vec v_2 = \begin{pmatrix} 1 \\ 5 \end{pmatrix}$.
- **$C(0,4)$:** Lower triangular, so $(6 - \lambda)(-4 - \lambda) = 0 \implies \lambda_1 = 6 > 0$, $\lambda_2 = -4 < 0$. **Saddle point.**
  - For $\lambda_1 = 6$: $\begin{pmatrix} 0 & 0 \\ 8 & -10 \end{pmatrix}\vec v_1 = \vec 0 \implies 8v_1 - 10v_2 = 0 \implies \vec v_1 = \begin{pmatrix} 5 \\ 4 \end{pmatrix}$.
  - For $\lambda_2 = -4$: $\begin{pmatrix} 10 & 0 \\ 8 & 0 \end{pmatrix}\vec v_2 = \vec 0 \implies v_1 = 0 \implies \vec v_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.

## Step 4: Global picture

We sketch the non-trivial nullclines and vector-field signs in $x, y \ge 0$ to contrast the two cooperation regimes.

### (i) Bounded mutualistic coexistence ($ad > bc$)

The non-trivial nullclines are $y = x - 1$ ($\dot x = 0$, slope $1$) and $y = \frac{1}{2}x + \frac{1}{2}$ ($\dot y = 0$, slope $\frac{1}{2}$). Because the $\dot x = 0$ nullcline is steeper than the $\dot y = 0$ nullcline ($a/b = 1 > c/d = 1/2 \iff ad > bc$), they intersect in the first quadrant at $D(3, 2)$. In all four regions around $D$, the vector field points toward $D$, and the unstable manifolds of both boundary saddles $B(1,0)$ and $C(0, 1/2)$ flow directly into $D$. Consequently, every initial state with $x(0) > 0$ and $y(0) > 0$ converges to $D(3, 2)$: **both species coexist stably at populations strictly larger than their isolated carrying capacities** ($x^* = 3 > 1$, $y^* = 2 > 1/2$).

![[attachments/AM-PS/ch5-e3-i.svg]]
*Phase portrait of cooperative model (i) in $x, y \ge 0$: the nullclines $y = x - 1$ and $y = (1+x)/2$ cross at the globally attracting coexistence node $D(3,2)$.*

### (ii) Unbounded mutualistic growth ($ad < bc$)

The non-trivial nullclines are $y = x - 2$ ($\dot x = 0$, slope $1$) and $y = 2x + 4$ ($\dot y = 0$, slope $2$). Because $a/b = 1 < c/d = 2$ ($ad < bc$), the two lines diverge in the first quadrant rather than intersecting. Inside the open wedge $x - 2 < y < 2x + 4$ between them, both $\dot x > 0$ and $\dot y > 0$; trajectories starting above $y = 2x + 4$ move right and down ($\dot x > 0, \dot y < 0$) into the wedge, while trajectories starting below $y = x - 2$ move left and up ($\dot x < 0, \dot y > 0$) into the wedge. Once inside the wedge, trajectories can never leave and both populations grow without bound: **$x(t) \to +\infty$ and $y(t) \to +\infty$** (a classic modelling pathology of unconstrained linear mutualism, showing that realistic strong cooperation requires saturation terms).

![[attachments/AM-PS/ch5-e3-ii.svg]]
*Phase portrait of cooperative model (ii) in $x, y \ge 0$: the nullclines $y = x - 2$ and $y = 2x + 4$ diverge in the first quadrant, and all interior trajectories escape to $(+\infty, +\infty)$.*

## Answers and checks

- **General condition $ad \gtrless bc$:** Solving $A - ax + by = 0$ and $B + cx - dy = 0$ by Cramer's rule gives
  $$
  x^* = \frac{Ad + Bb}{ad - bc}, \qquad y^* = \frac{Ac + Ba}{ad - bc}.
  $$
  Since $A, B, a, b, c, d > 0$, both numerators are strictly positive, so a first-quadrant coexistence equilibrium exists if and only if $ad - bc > 0$. Model (i) has $ad - bc = 2 - 1 = 1 > 0$ (giving $x^* = 3, y^* = 2$), whereas model (ii) has $ad - bc = 1 - 2 = -1 < 0$ (giving $x^* = -6, y^* = -8 \notin \mathbb{R}_+^2$).
- **Check against Robinson (Ex. 33.2):** All critical points, eigenvalues, and the bounded-vs-unbounded dichotomy match Robinson, *An Introduction to Ordinary Differential Equations*, Exercise 33.2.
- **Dimensional consistency:** With dimensionless scaled densities $x, y$, every coefficient $A, B, a, b, c, d$ has dimension $[T^{-1}]$, so $ad - bc$ has homogeneous dimension $[T^{-2}]$ and $x^*, y^*$ are dimensionless.

> [!result] Key results
> - **Model (i) ($ad = 2 > bc = 1$):** $(0,0)$ unstable star; $(1,0)$ and $(0, 1/2)$ saddles; $(3,2)$ stable node ($\lambda_1 = -1, \lambda_2 = -6$). All positive initial states converge to bounded mutualistic coexistence at $(3,2)$.
> - **Model (ii) ($ad = 1 < bc = 2$):** $(0,0)$ unstable node ($\lambda = 2, 4$); $(2,0)$ and $(0,4)$ saddles; no interior equilibrium in $x, y \ge 0$. All positive initial states experience unbounded growth ($x, y \to +\infty$).
