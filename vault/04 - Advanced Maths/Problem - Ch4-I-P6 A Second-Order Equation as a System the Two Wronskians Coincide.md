---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
origen: "probls_ch4-i_2627_v2.pdf - Exercise 6"
dificultad: media
id: "e6"
pill: "Second Order to System • Wronskian • Abel"
tags:
  - problema-resuelto
  - wronskiano
  - sistemas
  - identidad-de-abel
---

# Problem 4.I.6: A Second-Order Equation as a System: the Two Wronskians Coincide

> Official exercise 6 of the sheet `probls_ch4-i_2627_v2.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 4 Part 1]]. Method and notation: [[Concept - Planar Systems with Complex Eigenvalues]].

## Statement

Suppose that we have a second order linear ODE $x''(t) + p(t)x'(t) + q(t)x(t) = 0$, and two solutions $x_1(t)$ and $x_2(t)$. Write it as a linear system of two first order ODEs. Check that if

$$ \begin{cases} x = x_1(t) \\ y = y_1(t) \end{cases} \quad\text{and}\quad \begin{cases} x = x_2(t) \\ y = y_2(t) \end{cases} $$

are the corresponding solutions of the system, then the Wronskian as defined in this chapter coincides with the definition that we had before for second order ODEs.

## Phase 1: Setup

$p, q$ continuous on an interval $I$. Two definitions to compare: the scalar Wronskian $W_2[x_1, x_2] = x_1x_2' - x_2x_1'$ (Topic 3 Sec. 2.1) and the Wronskian of vector solutions $W_{sys} = \det[\mathbf x_1\ \mathbf x_2]$ (Topic 4 Sec. 3).

## Phase 2: Formulation: the system

Introduce $y = x'$ (Robinson Sec. 25.1: $x_1 \to x$, $x_2 \to x'$). Then $x' = y$ and, from the ODE, $y' = x'' = -p\,x' - q\,x = -q\,x - p\,y$:

$$ \begin{cases} x' = 0\cdot x + 1\cdot y \\ y' = -q(t)\,x - p(t)\,y \end{cases} \qquad \dot{\mathbf x} = \begin{pmatrix} 0 & 1 \\ -q & -p \end{pmatrix}\mathbf x $$

This has the form (1) with $a_1 = 0$, $b_1 = 1$, $a_2 = -q$, $b_2 = -p$ (continuous). A solution $x_j(t)$ of the ODE gives the solution $(x_j, y_j) = (x_j, x_j')$ of the system, and conversely the first component of a system solution solves the ODE.

> [!info] Method of the class notes [Notes, p. 9]
> This is the important point of the notes with $x_1 = x$ and $x_2 = \dot x$ (here $y$), applied to $x'' + px' + qx = 0$: $A = \begin{pmatrix} 0 & 1 \\ -q & -p \end{pmatrix}$. The Wronskian of the system, $\det\begin{pmatrix} x_1 & x_2 \\ y_1 & y_2 \end{pmatrix} = x_1y_2 - x_2y_1$ with $y_j = x_j'$, is then the Wronskian $x_1x_2' - x_2x_1'$ of the notes for second-order equations (p. 5).

## Phase 3: Derivation

The corresponding solutions of the system are $\mathbf x_1 = (x_1, x_1')^T$ and $\mathbf x_2 = (x_2, x_2')^T$, so $y_j = x_j'$. Their system Wronskian is

$$ W_{sys} = \begin{vmatrix} x_1 & x_2 \\ y_1 & y_2 \end{vmatrix} = x_1y_2 - x_2y_1 = x_1x_2' - x_2x_1' = W_2[x_1, x_2] $$

The two definitions coincide identically. $\blacksquare$

#### Consistency with Exercise 3

Exercise 3 applied to this system ($a_1 + b_2 = 0 + (-p) = -p$) gives $\dot W = -pW$, i.e. $W(t) = W(t_0)\exp\left(-\int_{t_0}^{t}p\right)$, which is Abel's identity of Topic 3 (Robinson Exercise 11.2). Direct check from the scalar definition: $W_2' = x_1'x_2' + x_1x_2'' - x_2'x_1' - x_2x_1'' = x_1x_2'' - x_2x_1'' = x_1(-px_2' - qx_2) - x_2(-px_1' - qx_1) = -p(x_1x_2' - x_2x_1') = -pW_2$, the same equation.

## Phase 4: Interpretation and checks

- Therefore all the theory of systems (non-vanishing Wronskian $\Leftrightarrow$ independence, general solution, dichotomy) contains the scalar results of Topic 3 as the special case $A = \begin{pmatrix} 0 & 1 \\ -q & -p \end{pmatrix}$; the notation $\mathbf x(t_0) = (x(t_0), \dot x(t_0))$ for the initial data is the same pair as in Theorem 11.1.
- Example: $\ddot x + x = 0$, $x_1 = \cos t$, $x_2 = \sin t$: $W_2 = \cos^2t + \sin^2t = 1$ and $W_{sys} = \begin{vmatrix} \cos t & \sin t \\ -\sin t & \cos t \end{vmatrix} = 1$; $p = 0$ so $W$ is constant, as Abel/Liouville predict.
- The matrix $\begin{pmatrix} 0 & 1 \\ -q & -p \end{pmatrix}$ has trace $-p$ and determinant $q$; for constants it gives the characteristic polynomial $\mu^2 + p\mu + q$ of Topic 3.
