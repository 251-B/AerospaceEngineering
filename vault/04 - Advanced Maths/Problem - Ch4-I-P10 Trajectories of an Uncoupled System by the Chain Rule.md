---
materia: "Advanced Maths"
tema: "Tema 4: Systems of First-Order ODEs and the Phase Plane"
origen: "probls_ch4-i_2627_v2.pdf - Exercise 10"
dificultad: media
id: "e10"
pill: "Chain Rule • Separable Equation • Orbit Equation"
tags:
  - problema-resuelto
  - trayectorias
  - variables-separables
  - regla-de-la-cadena
---

# Problem 4.I.10: Trajectories of an Uncoupled System by the Chain Rule

> Official exercise 10 of the sheet `probls_ch4-i_2627_v2.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 4 Part 1]]. Method and notation: [[Concept - Planar Systems with Complex Eigenvalues]].

## Statement

Using the chain rule for $y = y(x(t))$,

$$ \frac{dy}{dt} = \frac{dy}{dx}\frac{dx}{dt} \;\Longrightarrow\; \frac{dy}{dx} = \frac{\dfrac{dy}{dt}}{\dfrac{dx}{dt}}. $$

Therefore, if

$$ \frac{dx}{dt} = \lambda_1x, \qquad \frac{dy}{dt} = \lambda_2y $$

we have

$$ \frac{dy}{dx} = \frac{\lambda_2y}{\lambda_1x}. $$

Solve the latter equation to determine the curves traced out by trajectories of the system of equations for $x(t)$ and $y(t)$.

## Phase 1: Setup and hypotheses

Real constants $\lambda_1, \lambda_2$. The chain rule is valid where $x(t)$ is a differentiable function with $\dot x \neq 0$, so that $t \mapsto x$ is locally invertible and $y$ can be regarded as a function of $x$. Here $\dot x = \lambda_1x \neq 0$ requires $\lambda_1 \neq 0$ and $x \neq 0$. The cases $x = 0$ (the $y$-axis), $y = 0$ (the $x$-axis) and $\lambda_1 = 0$ are treated separately at the end.

## Phase 2: Formulation

The orbit equation $\frac{dy}{dx} = \frac{\lambda_2}{\lambda_1}\frac{y}{x}$ has no explicit $t$ and is **separable**: all the $y$ on the left and all the $x$ on the right.

## Phase 3: Derivation

#### Integration

Separate variables (for $y \neq 0$, $x \neq 0$) and integrate both sides with their antiderivatives, $\int\frac{dy}{y} = \ln|y|$:

$$ \frac{dy}{y} = \frac{\lambda_2}{\lambda_1}\frac{dx}{x} \;\Longrightarrow\; \ln|y| = \frac{\lambda_2}{\lambda_1}\ln|x| + C $$

Exponentiate and absorb $e^{C}$ in a constant $K = \pm e^{C}$:

$$ |y| = e^{C}|x|^{\lambda_2/\lambda_1} \;\Longrightarrow\; \boxed{y = K\,|x|^{\lambda_2/\lambda_1}}, \qquad K \neq 0 $$

#### Checking with the explicit solution

The equations are solved directly by $x = x_0e^{\lambda_1t}$, $y = y_0e^{\lambda_2t}$ (separation of variables, $\frac{d}{dt}(e^{-\lambda t}u) = 0$). For $x_0 \neq 0$, $|x|/|x_0| = e^{\lambda_1t}$ so $e^{t} = (|x|/|x_0|)^{1/\lambda_1}$ and

$$ y = y_0\left(e^{\lambda_1t}\right)^{\lambda_2/\lambda_1} = y_0\left(\frac{|x|}{|x_0|}\right)^{\lambda_2/\lambda_1} = \underbrace{y_0|x_0|^{-\lambda_2/\lambda_1}}_{K}|x|^{\lambda_2/\lambda_1} $$

which is the same family, with $K = y_0|x_0|^{-\lambda_2/\lambda_1}$ (the sign of $y$ is the sign of $y_0$, preserved since $y = y_0e^{\lambda_2t}$).

#### The axes

If $x_0 = 0$ then $x(t) \equiv 0$ and the orbit is on the $y$-axis (with $y = y_0e^{\lambda_2t}$); if $y_0 = 0$ then $y \equiv 0$ (that is $K = 0$) and the orbit lies on the $x$-axis. The origin is the equilibrium. If $\lambda_1 = 0$, $x$ is constant and the orbits are vertical lines.

#### Shapes of the curves

| Exponent $\lambda_2/\lambda_1$ | Curves $y = K\vert x\vert ^{r}$ | Origin |
| :--- | :--- | :--- |
| $r > 1$ (same sign, $\vert \lambda_2\vert  > \vert \lambda_1\vert $) | parabola-like, tangent to the $x$-axis at $0$ | node (stable if $\lambda_i < 0$, unstable if $> 0$) |
| $r = 1$ ($\lambda_1 = \lambda_2$) | straight lines $y = Kx$ (rays) | star |
| $0 < r < 1$ | tangent to the $y$-axis at $0$ | node |
| $r < 0$ (opposite signs) | hyperbola-like, $y\vert x\vert ^{-r} = K$, asymptotic to the axes | saddle |
| $r = -1$ | rectangular hyperbolas $xy = \pm K$ | saddle |

## Phase 4: Interpretation and checks

- This is the derivation behind the canonical portraits of Topic 4 Sec. 6.1: replace $(x, y)$ by $(z_1, z_2)$ and $\lambda_1, \lambda_2$ by the two eigenvalues to get $z_2 = K|z_1|^{\lambda_2/\lambda_1}$ (Robinson Eq. 28.12).
- Examples: $\lambda_1 = 1$, $\lambda_2 = 2$: $y = Kx^2$ (parabolas); $\lambda_1 = 1$, $\lambda_2 = -1$: $y = K/x$ (hyperbolas).
- Direction along the orbits is **not** given by the orbit equation: it is read from $\dot x = \lambda_1x$, $\dot y = \lambda_2y$ (away from $0$ along an axis if $\lambda > 0$, towards it if $\lambda < 0$).
- Differentiating the answer: $\frac{dy}{dx} = K\frac{\lambda_2}{\lambda_1}|x|^{\lambda_2/\lambda_1 - 1}\operatorname{sign}(x) = \frac{\lambda_2}{\lambda_1}\frac{y}{x}$, which recovers the ODE (using $|x|^{r}/x = |x|^{r-1}\operatorname{sign}x$).
