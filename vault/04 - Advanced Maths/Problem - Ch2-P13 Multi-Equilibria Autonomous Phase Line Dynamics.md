---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.13"
dificultad: media
tags:
  - problema-resuelto
  - autonomous-odes
  - phase-line
  - equilibria
  - stability
  - finite-time-blow-up
---

# Problem 2.13: Multi-Equilibria Autonomous Phase Line Dynamics

Source: ProblemsCh2.pdf, Exercise 13 (page 3). File: sources/cuatrimestre-1/04-advanced-maths/unit-02-first-order-odes/problemas/ProblemsCh2.pdf

Theory reference: Robinson, An Introduction to Ordinary Differential Equations (BookODE's.pdf), Chapter 7 (Sections 7.1 to 7.3, qualitative approach and stability), Section 6.3 (maximal interval of existence) and Section 8.1 (separable recipe).

## Problem Statement

Consider the autonomous differential equation

$$
\frac{dy}{dt} = y(y-2)(y-3).
$$

In each of the following cases, what can you conclude based on the uniqueness theorem about the different solutions if

(i) $y(0) = -1$,  
(ii) $y(0) = 1$,  
(iii) $y(0) = 2$,  
(iv) $y(0) = 4$?  

---

## Phase 1: Classification, Hypotheses and Domain

Autonomous equation $\dot{y} = f(y)$ with the cubic polynomial

$$
f(y) = y(y-2)(y-3) = y^3 - 5y^2 + 6y, \qquad f'(y) = 3y^2 - 10y + 6.
$$

Both $f$ and $f'$ are continuous on all of $\mathbb{R}$, so the existence and uniqueness theorem holds at every initial point: through each $(0, y_0)$ passes exactly one solution, defined on a maximal open interval of existence.

Equilibria ($f(y^*) = 0$): $y^* = 0,\ 2,\ 3$. They give the constant solutions $y \equiv 0$, $y \equiv 2$, $y \equiv 3$.

---

## Phase 2: Choice of Method and Change of Variables

Why this method: by uniqueness, two different solutions of the same autonomous equation never touch. A non-constant solution therefore cannot reach an equilibrium value in finite time, so it stays in one of the four intervals

$$
I_1 = (-\infty, 0),\quad I_2 = (0, 2),\quad I_3 = (2, 3),\quad I_4 = (3, \infty)
$$

determined by the equilibria. Inside an interval $f$ has a constant sign, so $y(t)$ is strictly monotone. A monotone function that stays in a bounded interval has a limit, and this limit must be an equilibrium. If the interval is unbounded, the solution may escape to infinity; whether this happens in finite time is decided by separating variables.

Sign of $f$ and stability from $f'$:

| Interval or point | Sign of $f$ (test point) | Motion |
| :--- | :--- | :--- |
| $y < 0$ | $f(-1) = (-1)(-3)(-4) = -12 < 0$ | decreasing |
| $0 < y < 2$ | $f(1) = (1)(-1)(-2) = 2 > 0$ | increasing |
| $2 < y < 3$ | $f(2.5) = (2.5)(0.5)(-0.5) = -0.625 < 0$ | decreasing |
| $y > 3$ | $f(4) = (4)(2)(1) = 8 > 0$ | increasing |

Stability: $f'(0) = 6 > 0$ (unstable), $f'(2) = 12 - 20 + 6 = -2 < 0$ (asymptotically stable), $f'(3) = 27 - 30 + 6 = 3 > 0$ (unstable). This agrees with the arrows: flow leaves $0$ and $3$ on both sides and enters $2$ from both sides.

Time scale for blow-up: for $\lvert y\rvert$ large, $f(y) \sim y^3$, and the time needed to reach infinity is $\int^{\infty}dy/f(y) \sim \int^{\infty}dy/y^3 < \infty$. This finite integral signals that infinity is reached in finite time. We compute the time exactly by separation of variables.

---

## Phase 3: Step-by-Step Derivation

### Separation of variables with partial fractions

For $y \neq 0, 2, 3$ write $\dfrac{dy}{y(y-2)(y-3)} = dt$ and decompose:

$$
\frac{1}{y(y-2)(y-3)} = \frac{A}{y} + \frac{B}{y-2} + \frac{C}{y-3}.
$$

Cover-up rule: $A = \frac{1}{(0-2)(0-3)} = \frac16$, $B = \frac{1}{2\,(2-3)} = -\frac12$, $C = \frac{1}{3\,(3-2)} = \frac13$. Check: $A + B + C = \frac16 - \frac12 + \frac13 = 0$, as required since the left side decays like $y^{-3}$. Integrating,

$$
G(y) := \int\frac{dy}{y(y-2)(y-3)} = \frac16\ln\lvert y\rvert - \frac12\ln\lvert y-2\rvert + \frac13\ln\lvert y-3\rvert.
$$

Barrow's rule from $(0, y_0)$: $G(y(t)) - G(y_0) = t$. Equivalently, multiplying by $6$ and exponentiating,

$$
\frac{\lvert y\rvert\,\lvert y-3\rvert^{2}}{\lvert y-2\rvert^{3}} = K\,e^{6t}, \qquad K = \frac{\lvert y_0\rvert\,\lvert y_0-3\rvert^{2}}{\lvert y_0-2\rvert^{3}}.
$$

Limit of $G$ at infinity: the coefficients sum to zero, so $G(y) = \frac16\ln\dfrac{\lvert y\rvert\,\lvert y-3\rvert^2}{\lvert y-2\rvert^3}$, and the argument of the logarithm tends to $1$ as $y \to \pm\infty$. Hence $G(\pm\infty) = \frac16\ln 1 = 0$.

### Case (i): $y(0) = -1$

$y(0) \in I_1$. By uniqueness the solution cannot reach the equilibrium $y = 0$, so $y(t) < 0$ for all $t$ in its domain. Since $f < 0$ there, $y$ is strictly decreasing.

- Backward in time: $y$ increases and is bounded above by $0$, so it tends to an equilibrium: $y \to 0^-$ as $t \to -\infty$.
- Forward in time: $y$ decreases without a lower barrier and $f \sim y^3$, so it blows up to $-\infty$ at a finite time $T^*$.

Blow-up time from Barrow's rule, $T^* = G(-\infty) - G(-1) = -G(-1)$:

$$
G(-1) = \frac16\ln 1 - \frac12\ln 3 + \frac13\ln 4, \qquad T^* = \frac12\ln 3 - \frac13\ln 4 = \frac12\ln 3 - \frac23\ln 2 \approx 0.0872.
$$

Cross-check with the closed form: $K = \frac{1\cdot 16}{27}$, and blow-up occurs when the left side tends to $1$ (as $\lvert y\rvert \to \infty$): $1 = \frac{16}{27}e^{6T^*}$, so $T^* = \frac16\ln\frac{27}{16} = \frac16(3\ln 3 - 4\ln 2)$, the same value.

### Case (ii): $y(0) = 1$

$y(0) \in I_2 = (0,2)$. The equilibria $0$ and $2$ are barriers, so $0 < y(t) < 2$ for all $t$. A bounded solution cannot blow up, so it is defined for all $t \in \mathbb{R}$. Since $f > 0$, $y$ is strictly increasing, hence it has limits at both ends and they are equilibria:

$$
\lim_{t\to-\infty}y(t) = 0, \qquad \lim_{t\to+\infty}y(t) = 2.
$$

The solution goes from the unstable equilibrium $0$ to the stable equilibrium $2$ (a monotone, sigmoidal profile). Neither limit is reached in finite time.

### Case (iii): $y(0) = 2$

$f(2) = 0$, so $y(t) \equiv 2$ is a solution of the IVP. By the uniqueness theorem it is the only one:

$$
y(t) \equiv 2 \quad \forall t \in \mathbb{R}.
$$

In particular no non-constant solution can pass through the point $(t, 2)$ at any time; solutions that start in $I_2$ or $I_3$ approach $2$ only asymptotically.

### Case (iv): $y(0) = 4$

$y(0) \in I_4 = (3,\infty)$. The barrier $y = 3$ gives $y(t) > 3$ for all $t$; $f > 0$ there, so $y$ is strictly increasing.

- Backward in time: bounded below by $3$ and decreasing as $t$ decreases, so $y \to 3^+$ as $t \to -\infty$.
- Forward in time: no upper barrier and $f \sim y^3$, so $y \to +\infty$ at a finite time $T^*$.

$$
T^* = G(+\infty) - G(4) = -G(4) = -\left[\frac16\ln 4 - \frac12\ln 2 + \frac13\ln 1\right] = -\left[\frac13\ln 2 - \frac12\ln 2\right] = \frac16\ln 2 \approx 0.1155.
$$

Cross-check with the closed form: $K = \frac{4\cdot 1}{8} = \frac12$, and $1 = \frac12 e^{6T^*}$ gives $T^* = \frac16\ln 2$.

---

## Phase 4: Verification, Limits and Interpretation

Numerical checks (computed): the partial-fraction decomposition from sympy is $\frac{1}{6y} - \frac{1}{2(y-2)} + \frac{1}{3(y-3)}$, matching $A, B, C$. An independent fourth-order Runge-Kutta integration of $\dot{y} = y(y-2)(y-3)$ with step $1.5\times 10^{-6}$ reaches $\lvert y\rvert > 10^{7}$ at $t \approx 0.115526$ for $y_0 = 4$ (formula: $0.115525$) and at $t \approx 0.087210$ for $y_0 = -1$ (formula: $0.087208$).

Time scale: the correct statement for $y_0 = -1$ and $y_0 = 4$ is not $y \to \pm\infty$ as $t \to \infty$; the solutions cease to exist at $T^* \approx 0.087$ and $T^* \approx 0.116$ respectively, so a limit $t \to \infty$ is meaningless for them. By contrast, for $y_0 = 1$ the solution is global and the limit $t \to \infty$ is $2$.

Dimensional remark: if $y$ is a non-dimensional state and $t$ is measured in units of a characteristic time $\tau$, then $T^*$ is a number of such units; the equation $\dot{y} = f(y)$ requires $[f] = [y]/[t]$, and the coefficients $2, 3$ carry the dimensions of $y$.

#### Classification of trajectories

| Initial condition | Region | Behavior forward | Behavior backward |
| :--- | :--- | :--- | :--- |
| (i) $y(0) = -1$ | $y < 0$, decreasing | blow-up to $-\infty$ at $T^* = \frac12\ln 3 - \frac23\ln 2 \approx 0.087$ | $y \to 0^-$ as $t \to -\infty$ |
| (ii) $y(0) = 1$ | $0 < y < 2$, increasing | $y \to 2$ as $t \to \infty$ | $y \to 0^+$ as $t \to -\infty$ |
| (iii) $y(0) = 2$ | equilibrium | $y \equiv 2$ | $y \equiv 2$ |
| (iv) $y(0) = 4$ | $y > 3$, increasing | blow-up to $+\infty$ at $T^* = \frac16\ln 2 \approx 0.116$ | $y \to 3^+$ as $t \to -\infty$ |

---

## Related Notes

- [[04 - Advanced Maths/Concept - Qualitative Analysis of Autonomous ODEs and Stability|Qualitative analysis of autonomous ODEs and stability]]
- [[04 - Advanced Maths/Concept - Well-Posed Problems and Picard Theorem|Picard theorem and well-posedness]]
- [[04 - Advanced Maths/Problem - Ch2-P16 Pitchfork Phase Line and Stability Regimes|Problem 2.16: pitchfork phase line]]
