---
materia: "Advanced Maths"
tema: "Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients"
origen: "probls_ch3-ii_2627.pdf - Exercise 7"
dificultad: media
id: "e7"
pill: "Initial Value Problem • Superposition • Uniqueness"
tags:
  - problema-resuelto
  - pvi-segundo-orden
  - superposicion
  - unicidad
---

# Problem 3.II.7: Splitting the Solution of an IVP into Homogeneous and Inhomogeneous Parts

> Official exercise 7 of the sheet `probls_ch3-ii_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 3 Part 2]]. Method and notation: [[Topic 3 - Second-Order Linear ODEs General Theory and Constant Coefficients]].

## Statement

Show that the solution of the initial value problem

$$ L[y] = y'' + p(t)y' + q(t)y = g(t), \qquad y(t_0) = y_0, \quad y'(t_0) = y_0' $$

can be written as $y(t) = u(t) + v(t)$, where $u$ and $v$ are solutions of two different initial value problems:

$$ \begin{aligned} L[u] &= 0, & u(t_0) &= y_0, & u'(t_0) &= y_0', \\ L[v] &= g(t), & v(t_0) &= 0, & v'(t_0) &= 0. \end{aligned} $$

## Phase 1: Setup and hypotheses

Hypotheses: $p, q, g$ are continuous on an open interval $I \ni t_0$. Under these hypotheses the existence and uniqueness theorem (Robinson Thm 11.1, Topic 3 Sec. 1; for linear equations the solution exists on the whole of $I$) states that every IVP $L[w] = h$, $w(t_0) = w_0$, $w'(t_0) = w_1$ has exactly one solution on $I$. Define $L[y] = y'' + p\,y' + q\,y$; $L$ is a **linear operator**: $L[\alpha y_1 + \beta y_2] = \alpha L[y_1] + \beta L[y_2]$ (Robinson Eq. 11.11).

## Phase 2: Formulation

Let $y$ be the unique solution of the original IVP, $u$ the unique solution of the homogeneous IVP with the data of $y$, and $v$ the unique solution of the inhomogeneous IVP with zero data (both exist on $I$ by the theorem). The claim is $y = u + v$ on $I$. Proof strategy: show that $u + v$ solves the **original** IVP; uniqueness then forces $u + v = y$.

## Phase 3: Derivation

#### Step 1: $u + v$ solves the differential equation

$$ L[u + v] = L[u] + L[v] = 0 + g(t) = g(t) \quad \text{on } I, $$

by linearity of $L$ (differentiation is linear: $(u + v)' = u' + v'$ and $(u + v)'' = u'' + v''$, so $L[u + v] = u'' + v'' + p(u' + v') + q(u + v) = (u'' + pu' + qu) + (v'' + pv' + qv)$).

#### Step 2: $u + v$ satisfies the initial conditions

$$ (u + v)(t_0) = u(t_0) + v(t_0) = y_0 + 0 = y_0, \qquad (u + v)'(t_0) = u'(t_0) + v'(t_0) = y_0' + 0 = y_0' $$

#### Step 3: uniqueness

Both $y$ and $u + v$ solve the IVP $L[w] = g$, $w(t_0) = y_0$, $w'(t_0) = y_0'$ on $I$. By uniqueness (Robinson Thm 11.1), $y = u + v$ on $I$. An equivalent argument that avoids quoting the theorem twice: $w = y - (u + v)$ satisfies $L[w] = g - g = 0$ with $w(t_0) = 0$ and $w'(t_0) = 0$; the zero function solves the same homogeneous IVP, so $w \equiv 0$ by uniqueness. $\blacksquare$

#### Where the hypotheses were used

- Linearity of $L$: Steps 1 and the alternative argument.
- Uniqueness: Step 3. Existence of $u$ and $v$ on all of $I$: needed so that $u + v$ is defined where $y$ is; it holds because $L$ is linear with continuous coefficients.

## Phase 4: Interpretation and checks

- Meaning: $u$ is the **free response** (the system left to itself with the given initial state) and $v$ the **forced response** from rest (zero state). This is the decomposition used in control and vibration analysis, e.g. $u$ = transient from initial displacement and velocity, $v$ = response to the external force from a state of rest.
- It reduces any IVP with general data to two simpler ones: the homogeneous one with the data, and the inhomogeneous one with zero data. Variation of constants gives $v$ directly: with $x_1, x_2$ independent homogeneous solutions and $W$ their Wronskian, $v(t) = \int_{t_0}^{t}\dfrac{x_1(s)x_2(t) - x_1(t)x_2(s)}{W(s)}\,g(s)\,ds$ (check: $v(t_0) = 0$ and $v'(t_0) = 0$ because the integrand vanishes at $s = t$ and the extra boundary term is $0$).
- Example (Exercise 1(ii) of this sheet, $\ddot x - 4\dot x = t^2$, $x(0) = 2$, $\dot x(0) = 0$): $u = 2$ (constant; it solves $\ddot u - 4\dot u = 0$ with $u(0) = 2$, $\dot u(0) = 0$) and $v = x_p + c_1 + c_2e^{4t}$ with $v(0) = \dot v(0) = 0$; their sum is the solution found there.
