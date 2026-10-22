---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
origen: "probls_ch4-i_2627_v2.pdf - Exercise 5"
dificultad: media
id: "e5"
pill: "Inhomogeneous System • Particular Solution"
tags:
  - problema-resuelto
  - sistemas-inhomogeneos
  - solucion-particular
---

# Problem 4.I.5: General Solution of an Inhomogeneous System

> Official exercise 5 of the sheet `probls_ch4-i_2627_v2.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 4 Part 1]]. Method and notation: [[Concept - Planar Systems with Complex Eigenvalues]].

## Statement

Suppose that we have an inhomogeneous system

$$ \begin{cases} \dfrac{dx}{dt} = a_1(t)x + b_1(t)y + f_1(t), \\[4pt] \dfrac{dy}{dt} = a_2(t)x + b_2(t)y + f_2(t) \end{cases} \tag{4} $$

and one particular solution

$$ \begin{cases} x = x_p(t) \\ y = y_p(t). \end{cases} \tag{5} $$

Show that, if $x_1(t)$ and $x_2(t)$ are linearly independent solutions of the homogeneous system, then the general solution of (4) is

$$ \begin{cases} x = c_1x_1(t) + c_2x_2(t) + x_p(t) \\ y = c_1y_1(t) + c_2y_2(t) + y_p(t) \end{cases} $$

## Phase 1: Setup and hypotheses

Coefficients and forcings $f_1, f_2$ continuous on $[a, b]$. The homogeneous system is (1) of Exercise 2. $\mathbf x_1 = (x_1, y_1)$ and $\mathbf x_2 = (x_2, y_2)$ are linearly independent solutions of (1) (the statement writes "$x_1(t)$ and $x_2(t)$" for the two solution vectors). Their Wronskian is non-zero on $[a, b]$: by Exercise 3 it is either $\equiv 0$ or never zero, and if $W(t_0) = 0$ there would be $(c_1, c_2) \neq (0, 0)$ with $c_1\mathbf x_1(t_0) + c_2\mathbf x_2(t_0) = \mathbf 0$; the combination $c_1\mathbf x_1 + c_2\mathbf x_2$ solves (1) with zero data at $t_0$, so it is $\equiv \mathbf 0$ by uniqueness (Exercise 4, Step 2), contradicting independence. $\mathbf x_p = (x_p, y_p)$ solves (4).

## Phase 2: Formulation

Two claims: (A) every function of the displayed form solves (4); (B) every solution of (4) has that form. The key idea (Robinson Sec. 14.1 for scalar equations, Topic 4 Sec. 3.1) is that the difference of two solutions of (4) solves the **homogeneous** system.

> [!info] Method of the class notes [Notes, p. 9]
> The last theorem of the notes for linear systems: $\mathbf x = \mathbf x_h + \mathbf x_p$. The proof is the one of the scalar case (Topic 3, notes p. 6): the difference of two solutions of the inhomogeneous system solves the homogeneous one.

## Phase 3: Derivation

#### (A) The family solves (4)

Write $\mathbf x = c_1\mathbf x_1 + c_2\mathbf x_2 + \mathbf x_p$ and $\dot{\mathbf x} = A\mathbf x + \mathbf f$ with $A = \begin{pmatrix} a_1 & b_1 \\ a_2 & b_2 \end{pmatrix}$, $\mathbf f = (f_1, f_2)^T$. Using $\dot{\mathbf x}_j = A\mathbf x_j$ and $\dot{\mathbf x}_p = A\mathbf x_p + \mathbf f$:

$$ \dot{\mathbf x} = c_1A\mathbf x_1 + c_2A\mathbf x_2 + A\mathbf x_p + \mathbf f = A(c_1\mathbf x_1 + c_2\mathbf x_2 + \mathbf x_p) + \mathbf f = A\mathbf x + \mathbf f $$

#### (B) Every solution has this form

Let $\mathbf x = (x, y)$ be any solution of (4) and put $\mathbf z = \mathbf x - \mathbf x_p$. Then

$$ \dot{\mathbf z} = \dot{\mathbf x} - \dot{\mathbf x}_p = (A\mathbf x + \mathbf f) - (A\mathbf x_p + \mathbf f) = A(\mathbf x - \mathbf x_p) = A\mathbf z $$

so $\mathbf z$ solves the homogeneous system (1). Since $\mathbf x_1, \mathbf x_2$ are independent solutions of (1) (non-zero Wronskian), Exercise 4 gives constants $c_1, c_2$ with $\mathbf z = c_1\mathbf x_1 + c_2\mathbf x_2$. Hence $\mathbf x = c_1\mathbf x_1 + c_2\mathbf x_2 + \mathbf x_p$. $\blacksquare$

## Phase 4: Interpretation and checks

- The structure "general = complementary + particular" is the same as for scalar linear equations (Topic 3 Sec. 5 lemma). The two constants are fixed by an initial condition $\mathbf x(t_0) = \mathbf x_0$: $\mathbf c = \Phi(t_0)^{-1}\left[\mathbf x_0 - \mathbf x_p(t_0)\right]$.
- Example (Topic 4 Example 26.1): $\dot x = x + y$, $\dot y = 4x - 2y + 4e^{-2t}$ has the particular solution $(-e^{-2t}, 3e^{-2t})$: check $\dot x_p = 2e^{-2t} = x_p + y_p = -e^{-2t} + 3e^{-2t}$ and $\dot y_p = -6e^{-2t} = 4(-e^{-2t}) - 2(3e^{-2t}) + 4e^{-2t} = -6e^{-2t}$.
- A particular solution can be found by elimination (Exercise 7), undetermined coefficients, or variation of parameters $\mathbf x_p = \Phi\int\Phi^{-1}\mathbf f$ (Topic 4 Sec. 3.1).
- Different particular solutions differ by a homogeneous solution, which is absorbed in $c_1, c_2$.
