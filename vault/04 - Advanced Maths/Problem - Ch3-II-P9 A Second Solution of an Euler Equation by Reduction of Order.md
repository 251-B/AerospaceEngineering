---
materia: "Advanced Maths"
tema: "Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients"
origen: "probls_ch3-ii_2627.pdf - Exercise 9"
dificultad: media
id: "e9"
pill: "Reduction of Order • Euler Equation • Wronskian"
tags:
  - problema-resuelto
  - reduccion-de-orden
  - ecuacion-de-euler
  - wronskiano
---

# Problem 3.II.9: A Second Solution of an Euler Equation by Reduction of Order

> Official exercise 9 of the sheet `probls_ch3-ii_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 3 Part 2]]. Method and notation: [[Topic 3 - Second-Order Linear ODEs General Theory and Constant Coefficients]].

## Statement

For $t > 0$ the function $y_1(t) = 1/t$ is a solution of $t^2\ddot y - 2t\dot y - 4y = 0$. Using the previous exercise, find a second, linearly independent solution.

## Phase 1: Setup and hypotheses

Domain $t > 0$ (so $y_1 = 1/t \neq 0$). The equation $t^2\ddot y - 2t\dot y - 4y = 0$ is homogeneous with variable coefficients; dividing by $t^2$ gives the standard form $\ddot y + p\dot y + qy = 0$ with $p(t) = -\dfrac{2}{t}$, $q(t) = -\dfrac{4}{t^2}$, continuous for $t > 0$. First check that $y_1$ is a solution:

$$ y_1 = t^{-1},\ \ \dot y_1 = -t^{-2},\ \ \ddot y_1 = 2t^{-3} \;\Rightarrow\; t^2(2t^{-3}) - 2t(-t^{-2}) - 4t^{-1} = 2t^{-1} + 2t^{-1} - 4t^{-1} = 0\ \checkmark $$

## Phase 2: Formulation

Apply Exercise 8 with $g = 0$: write $y = v\,y_1 = v/t$, so that $v$ must satisfy $y_1\ddot v + [2\dot y_1 + py_1]\dot v = 0$. A second independent solution is $y_2 = v\,y_1$ with $v$ non-constant.

> [!info] Method of the class notes [Notes, p. 7]
> Reduction of order as in the notes: with the known solution $u = y_1 = 1/t$, write $y = v\,u$; the bracket $u'' + pu' + qu$ vanishes and $z = v'$ satisfies $uz' + (2u' + pu)z = 0$, a first-order equation. The notes stop there; it is separable, and integrating it gives the second solution below.

## Phase 3: Derivation

#### The equation for $v$

Compute the coefficient: $2\dot y_1 + py_1 = 2(-t^{-2}) + \left(-\dfrac{2}{t}\right)\left(\dfrac1t\right) = -2t^{-2} - 2t^{-2} = -4t^{-2}$. The equation of Exercise 8 is

$$ \frac1t\,\ddot v - \frac{4}{t^2}\,\dot v = 0 \quad\Longleftrightarrow\quad \ddot v = \frac4t\,\dot v \quad (\text{multiplying by } t) $$

#### Solve for $w = \dot v$

$\dot w = \dfrac{4}{t}w$ is separable (or use the integrating factor $e^{-4\ln t} = t^{-4}$): $\dfrac{d}{dt}(t^{-4}w) = t^{-4}\dot w - 4t^{-5}w = t^{-4}\left(\dot w - \dfrac4tw\right) = 0$, so $t^{-4}w = c$ and

$$ w = \dot v = c\,t^4 $$

#### Integrate and multiply by $y_1$

$$ v = \int ct^4\,dt = \frac{c}{5}t^5 + b \quad\Longrightarrow\quad y = \frac{v}{t} = \frac{c}{5}t^4 + \frac{b}{t} $$

The term in $b$ is the known solution $y_1 = 1/t$; the new, independent solution is (taking $c = 5$, $b = 0$)

$$ \boxed{y_2(t) = t^4} $$

#### Verification

Substitute: $y_2 = t^4$, $\dot y_2 = 4t^3$, $\ddot y_2 = 12t^2$, so $t^2(12t^2) - 2t(4t^3) - 4t^4 = (12 - 8 - 4)t^4 = 0$ $\checkmark$. Wronskian:

$$ W[y_1, y_2] = y_1\dot y_2 - y_2\dot y_1 = \frac1t(4t^3) - t^4\left(-\frac{1}{t^2}\right) = 4t^2 + t^2 = 5t^2 \neq 0 \quad (t > 0) $$

so $y_1$ and $y_2$ are linearly independent on $t > 0$. Abel's identity gives the same dependence on $t$: $W = W_0\exp\left(-\int p\,dt\right) = W_0\exp\left(\int\frac{2}{t}dt\right) = W_0t^2$, consistent with $5t^2$ ($W_0 = 5$).

## Phase 4: Interpretation and checks

> [!result] Result
> A second independent solution is $y_2 = t^4$, and the general solution on $t > 0$ is $y = c_1t^{-1} + c_2t^{4}$.

- Euler cross-check: for $t^2\ddot y - 2t\dot y - 4y = 0$ the trial $y = t^k$ gives $k(k - 1) - 2k - 4 = k^2 - 3k - 4 = (k - 4)(k + 1) = 0$, so $k = 4, -1$: the same two solutions, found by a different method.
- Dimensional/scaling check: under $t \to \lambda t$ the Euler equation is invariant and the solutions are homogeneous power functions of degree $-1$ and $4$.
- The general solution is not defined at $t = 0$ (where $y_1$ blows up and the equation is singular), consistent with the restriction $t > 0$.
