---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
origen: "probls_ch4-i_2627_v2.pdf - Exercise 3"
dificultad: media
id: "e3"
pill: "Wronskian • Liouville • Dichotomy"
tags:
  - problema-resuelto
  - wronskiano
  - formula-de-liouville
  - sistemas-lineales
---

# Problem 4.I.3: The Wronskian of a Linear System: Liouville's Formula and the Dichotomy

> Official exercise 3 of the sheet `probls_ch4-i_2627_v2.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 4 Part 1]]. Method and notation: [[Concept - Planar Systems with Complex Eigenvalues]].

## Statement

Show that given a homogeneous linear system (1) with continuous coefficients in $[a, b]$, then the Wronskian $W(t)$ of two solutions (2) satisfies the first order ODE

$$ \frac{dW}{dt} = \left(a_1(t) + b_2(t)\right)W. $$

Deduce that this Wronskian is either identically $0$ or nowhere zero in $[a, b]$.

## Phase 1: Setup

System (1) of Exercise 2 with $a_1, b_1, a_2, b_2$ continuous on $[a, b]$. For two solutions $(x_1, y_1)$ and $(x_2, y_2)$ the Wronskian is the determinant of the matrix whose columns are the solutions (Topic 4 Sec. 3):

$$ W(t) = \begin{vmatrix} x_1 & x_2 \\ y_1 & y_2 \end{vmatrix} = x_1y_2 - x_2y_1 $$

## Phase 2: Formulation

Differentiate $W$ with the product rule, substitute the equations (H) of Exercise 2 for each derivative, and recognise $W$. The resulting scalar linear ODE is solved by an integrating factor.

## Phase 3: Derivation

#### Step 1: the product rule

$$ \dot W = \dot x_1y_2 + x_1\dot y_2 - \dot x_2y_1 - x_2\dot y_1 $$

#### Step 2: substitute the system

$$ \dot W = (a_1x_1 + b_1y_1)y_2 + x_1(a_2x_2 + b_2y_2) - (a_1x_2 + b_1y_2)y_1 - x_2(a_2x_1 + b_2y_1) $$

Expand and collect by coefficient:

$$ \dot W = a_1(x_1y_2 - x_2y_1) + b_2(x_1y_2 - x_2y_1) + b_1(y_1y_2 - y_2y_1) + a_2(x_1x_2 - x_2x_1) $$

The terms in $b_1$ and $a_2$ vanish identically ($y_1y_2 - y_2y_1 = 0$ and $x_1x_2 - x_2x_1 = 0$), and the remaining brackets are $W$:

$$ \boxed{\dot W = \left(a_1 + b_2\right)W} \qquad (= (\operatorname{tr}A)\,W) $$

#### Step 3: solve the scalar equation

Let $\tau(t) = \int_{t_0}^{t}\left[a_1(s) + b_2(s)\right]ds$, which exists and is differentiable because $a_1 + b_2$ is continuous, with $\tau'(t) = a_1(t) + b_2(t)$ (fundamental theorem of calculus). The chain rule gives $\frac{d}{dt}e^{-\tau(t)} = -\tau'(t)e^{-\tau(t)}$, so by the product rule $\frac{d}{dt}\left(e^{-\tau}W\right) = e^{-\tau}\dot W - \tau'e^{-\tau}W = e^{-\tau}(\dot W - \tau'W) = e^{-\tau}\left(\dot W - (a_1 + b_2)W\right) = 0$, so $e^{-\tau}W$ is constant on $[a, b]$. Barrow's rule, $[e^{-\tau(s)}W(s)]_{t_0}^{t} = 0$, gives $e^{-\tau(t)}W(t) = e^{-\tau(t_0)}W(t_0) = W(t_0)$ (as $\tau(t_0) = 0$):

$$ W(t) = W(t_0)\exp\left(\int_{t_0}^{t}\left[a_1(s) + b_2(s)\right]ds\right), \qquad t \in [a, b] $$

#### Step 4: the dichotomy

The exponential is finite and strictly positive, so $W(t) = 0$ exactly when $W(t_0) = 0$. Since $t_0 \in [a, b]$ was arbitrary: either $W(t_0) = 0$ for one (hence every) $t_0$, and then $W \equiv 0$ on $[a, b]$; or $W(t_0) \neq 0$ for one (hence every) $t_0$, and then $W$ does not vanish anywhere on $[a, b]$. There is no third possibility. $\blacksquare$

## Phase 4: Interpretation and checks

- Constant coefficients: $W(t) = W(0)e^{(a_1 + b_2)t} = W(0)e^{(\operatorname{tr}A)t}$ (Topic 4 Sec. 3, Liouville). Check with Example 28.1: eigenvalues $2$ and $-3$ have trace $-1$ and $W \propto e^{2t}e^{-3t} = e^{-t}$.
- For the system of a second-order equation $\ddot x + p\dot x + qx = 0$, $a_1 = 0$ and $b_2 = -p$ and the result is Abel's identity $\dot W = -pW$ (Exercise 6).
- Geometric meaning: $|W|$ is the area of the parallelogram spanned by the two solution vectors; $\operatorname{tr}A$ is the divergence of the flow, which rates the growth of areas. If $\operatorname{tr}A = 0$ areas are conserved ($W$ constant).
- This dichotomy is what makes the Wronskian a test for independence: it is enough to evaluate it at a single instant (Exercise 4).
