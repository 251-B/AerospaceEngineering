---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
origen: "probls_ch4-i_2627_v2.pdf - Exercise 4"
dificultad: media
id: "e4"
pill: "Fundamental Set • General Solution • Uniqueness"
tags:
  - problema-resuelto
  - wronskiano
  - solucion-general
  - sistemas-lineales
---

# Problem 4.I.4: A Non-Vanishing Wronskian Gives the General Solution

> Official exercise 4 of the sheet `probls_ch4-i_2627_v2.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 4 Part 1]]. Method and notation: [[Concept - Planar Systems with Complex Eigenvalues]].

## Statement

Show that if two solutions (2) of (1) have a Wronskian that does not vanish in $[a, b]$, then (3) gives the general solution of the system.

## Phase 1: Setup and hypotheses

System (1) with coefficients continuous on $[a, b]$ (as in Exercise 3). $(x_1, y_1)$ and $(x_2, y_2)$ are solutions with $W(t) = x_1y_2 - x_2y_1 \neq 0$ for all $t \in [a, b]$. To show: for every solution $(x, y)$ of (1) there are constants $c_1, c_2$ with $x = c_1x_1 + c_2x_2$ and $y = c_1y_1 + c_2y_2$ on $[a, b]$. (By Exercise 2 every combination is a solution, so this shows that (3) describes all of them.)

## Phase 2: Formulation

Tools: (a) uniqueness for linear systems with continuous coefficients: two solutions with the same value at one instant $t_0 \in [a, b]$ coincide on all of $[a, b]$. Robinson Thm 25.2 gives this locally (near $t_0$); the extension to $[a, b]$ is a continuation argument: the set $S$ of instants where the two solutions agree contains $t_0$, is closed (the solutions are continuous) and is open in $[a, b]$ (at each point of $S$ the local uniqueness applies, since the coefficients are continuous), and an interval is connected, so $S = [a, b]$; (b) Cramer's rule: a $2\times 2$ linear system with non-zero determinant has exactly one solution. Plan: match the given solution at one instant with a combination, then invoke uniqueness.

> [!info] Method of the class notes [Notes, p. 9]
> The notes: for $n = 2$ a fundamental set is a pair of solutions with $W(\mathbf x_1, \mathbf x_2) \neq 0$, and every solution is a combination of it. This exercise proves that statement. Matching the data at $t_0$ is the $2 \times 2$ system with determinant $W(t_0)$, as in the second-order example of the notes (p. 5), and uniqueness does the rest.

## Phase 3: Derivation

#### Step 1: choose the constants at one instant

Let $(x, y)$ be any solution and fix $t_0 \in [a, b]$. We look for $c_1, c_2$ such that the combination equals $(x, y)$ at $t_0$:

$$ \begin{pmatrix} x_1(t_0) & x_2(t_0) \\ y_1(t_0) & y_2(t_0) \end{pmatrix}\begin{pmatrix} c_1 \\ c_2 \end{pmatrix} = \begin{pmatrix} x(t_0) \\ y(t_0) \end{pmatrix} $$

The determinant of the coefficient matrix is $W(t_0) \neq 0$ by hypothesis, so there is exactly one solution (Cramer):

$$ c_1 = \frac{x(t_0)y_2(t_0) - x_2(t_0)y(t_0)}{W(t_0)}, \qquad c_2 = \frac{x_1(t_0)y(t_0) - x(t_0)y_1(t_0)}{W(t_0)} $$

#### Step 2: uniqueness

Define $\tilde x = c_1x_1 + c_2x_2$, $\tilde y = c_1y_1 + c_2y_2$. By Exercise 2 $(\tilde x, \tilde y)$ solves (1), and by Step 1 $(\tilde x(t_0), \tilde y(t_0)) = (x(t_0), y(t_0))$. Both $(x, y)$ and $(\tilde x, \tilde y)$ solve the same IVP at $t_0$, so by uniqueness $(x, y) = (\tilde x, \tilde y)$ on $[a, b]$. $\blacksquare$

#### Where Exercise 3 enters

If the Wronskian were known not to vanish at only some $t_0$, the argument would work at that $t_0$; Exercise 3 shows that a non-zero value at one point already implies $W \neq 0$ everywhere, so one test is enough. Also, two solutions with $W \equiv 0$ cannot form a general solution: then the matrix above is singular at each instant, and not every initial vector can be matched.

## Phase 4: Interpretation and checks

- The solution space is a 2-dimensional vector space with basis $\{(x_1, y_1), (x_2, y_2)\}$ (a **fundamental set**; $\Phi = [\mathbf x_1\ \mathbf x_2]$ is a fundamental matrix and $\mathbf c = \Phi(t_0)^{-1}\mathbf x(t_0)$, Topic 4 Sec. 3).
- Example: for $\dot x = x + y$, $\dot y = 4x - 2y$ the solutions $e^{2t}(1, 1)$ and $e^{-3t}(1, -4)$ have $W = e^{2t}e^{-3t}(-4 - 1) = -5e^{-t} \neq 0$, hence form a fundamental set (Topic 4 Example 28.1).
- Check: if $x_2 = kx_1$ and $y_2 = ky_1$ (parallel solutions) then $W = kx_1y_1 - kx_1y_1 = 0$ and the argument rightly fails.
- The same proof works for $n \times n$ systems with $\det\Phi(t_0) \neq 0$.
