---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
origen: "probls_ch4-i_2627_v2.pdf - Exercise 2"
dificultad: media
id: "e2"
pill: "Superposition • Linear Combination of Solutions"
tags:
  - problema-resuelto
  - sistemas-lineales
  - superposicion
---

# Problem 4.I.2: Superposition for Homogeneous Linear Systems

> Official exercise 2 of the sheet `probls_ch4-i_2627_v2.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 4 Part 1]]. Method and notation: [[Concept - Planar Systems with Complex Eigenvalues]].

## Statement

Show that if a homogeneous linear system

$$ \begin{cases} \dfrac{dx}{dt} = a_1(t)x + b_1(t)y, \\[4pt] \dfrac{dy}{dt} = a_2(t)x + b_2(t)y \end{cases} \tag{1} $$

has two solutions

$$ \begin{cases} x = x_1(t) \\ y = y_1(t) \end{cases} \quad\text{and}\quad \begin{cases} x = x_2(t) \\ y = y_2(t) \end{cases} \tag{2} $$

then any linear combination

$$ \begin{cases} x = c_1x_1(t) + c_2x_2(t) \\ y = c_1y_1(t) + c_2y_2(t) \end{cases} \tag{3} $$

with constants $c_1, c_2 \in \mathbb R$ is a solution as well.

## Phase 1: Setup

Hypotheses: $a_i, b_i$ are functions of $t$ (not necessarily constant) defined on an interval $I$, and $(x_1, y_1)$, $(x_2, y_2)$ are differentiable on $I$ with

$$ \dot x_j = a_1x_j + b_1y_j, \qquad \dot y_j = a_2x_j + b_2y_j \qquad (j = 1, 2) \tag{H} $$

## Phase 2: Formulation

To show: with $x = c_1x_1 + c_2x_2$ and $y = c_1y_1 + c_2y_2$ the two equations of (1) hold. Tool: differentiation is linear, $\frac{d}{dt}(c_1f + c_2g) = c_1\dot f + c_2\dot g$ for constants $c_1, c_2$. In vector notation: $\mathbf x = c_1\mathbf x_1 + c_2\mathbf x_2$ solves $\dot{\mathbf x} = A(t)\mathbf x$ because the right-hand side is linear in $\mathbf x$ (Robinson Eq. 27.3).

## Phase 3: Derivation

First equation. Differentiate $x = c_1x_1 + c_2x_2$ and use (H):

$$ \dot x = c_1\dot x_1 + c_2\dot x_2 = c_1(a_1x_1 + b_1y_1) + c_2(a_1x_2 + b_1y_2) $$

Regroup the terms with $a_1$ and with $b_1$:

$$ \dot x = a_1(c_1x_1 + c_2x_2) + b_1(c_1y_1 + c_2y_2) = a_1\,x + b_1\,y $$

Second equation. In the same way

$$ \dot y = c_1\dot y_1 + c_2\dot y_2 = c_1(a_2x_1 + b_2y_1) + c_2(a_2x_2 + b_2y_2) = a_2(c_1x_1 + c_2x_2) + b_2(c_1y_1 + c_2y_2) = a_2\,x + b_2\,y $$

Both equations of (1) are satisfied by (3). $\blacksquare$

#### Matrix form

$$ \dot{\mathbf x} = c_1\dot{\mathbf x}_1 + c_2\dot{\mathbf x}_2 = c_1A\mathbf x_1 + c_2A\mathbf x_2 = A(c_1\mathbf x_1 + c_2\mathbf x_2) = A\mathbf x, \qquad A(t) = \begin{pmatrix} a_1 & b_1 \\ a_2 & b_2 \end{pmatrix} $$

## Phase 4: Interpretation and checks

- Linearity and homogeneity are both used: homogeneity guarantees that the right-hand side of (1) vanishes when $x = y = 0$ (a forcing term $f(t)$ would be multiplied by $c_1 + c_2$ instead of by $1$, and the combination would not be a solution unless $c_1 + c_2 = 1$ and so on).
- Constant coefficients were not needed: only linearity of the derivative and of $(x, y) \mapsto (a_1x + b_1y, a_2x + b_2y)$.
- The set of solutions is therefore a vector space; Exercises 3 and 4 show that it has dimension $2$.
- Quick example: $\dot x = y$, $\dot y = -x$ has $(\cos t, -\sin t)$ and $(\sin t, \cos t)$ as solutions, and so $(c_1\cos t + c_2\sin t,\ -c_1\sin t + c_2\cos t)$ does.
