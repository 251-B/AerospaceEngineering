---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.16"
dificultad: alta
tags:
  - problema-resuelto
  - autonomous-odes
  - phase-line
  - pitchfork-bifurcation
  - stability
  - bernoulli-equation
---

# Problem 2.16: Pitchfork Phase Line and Stability Regimes

Source: ProblemsCh2.pdf, Exercise 16 (page 4). File: sources/cuatrimestre-1/04-advanced-maths/unit-02-first-order-odes/problemas/ProblemsCh2.pdf

Theory reference: Robinson, An Introduction to Ordinary Differential Equations (BookODE's.pdf), Chapter 7 (Sections 7.1 to 7.3 and 7.6, the pitchfork bifurcation) and Section 10.2 (substitution methods).

## Problem Statement

Consider the autonomous equation

$$
\frac{dx}{dt} = x\,(\kappa^2 - x^2)
$$

with a general initial condition $x(0) = x_0$.

(i) Calculate the stationary solutions, which satisfy $dx/dt = 0$;  
(ii) Calculate and sketch the solutions for $t > 0$, discussing the different behaviors which can be obtained in terms of the relative values of $\kappa > 0$ and $x_0$, with the help of the uniqueness theorem.  

---

## Phase 1: Classification, Hypotheses and Domain

Autonomous equation $\dot{x} = f(x)$ with $f(x) = x(\kappa^2 - x^2) = \kappa^2 x - x^3$ and parameter $\kappa > 0$. We have

$$
f'(x) = \kappa^2 - 3x^2.
$$

Both $f$ and $f'$ are polynomials, hence continuous on $\mathbb{R}$: the IVP has a unique solution for every $x_0 \in \mathbb{R}$, on a maximal interval of existence. The right-hand side is odd, $f(-x) = -f(x)$, so if $x(t)$ is a solution then $-x(t)$ is also a solution (symmetry $x \to -x$).

---

## Phase 2: Choice of Method and Change of Variables

Why these methods: (a) the phase line (sign of $f$ between equilibria) and the no-crossing consequence of uniqueness give the qualitative picture for every $x_0$ without solving; (b) the equation is a Bernoulli equation ($\alpha = 3$, see Problem 2.8), so the substitution $w = x^{-2}$ turns it into a linear equation and gives the exact solution to confirm the qualitative picture and to find timescales.

Change of variables written explicitly: $w = x^{1-\alpha} = x^{-2}$ (valid for $x \neq 0$), $\ w' = -2x^{-3}x'$, $\ w(0) = 1/x_0^2$.

---

## Phase 3: Step-by-Step Derivation

### Part (i): stationary solutions

Solve $f(x^*) = x^*(\kappa - x^*)(\kappa + x^*) = 0$ using $\kappa^2 - x^2 = (\kappa - x)(\kappa + x)$:

$$
x^* = 0, \qquad x^* = \kappa, \qquad x^* = -\kappa.
$$

Stability from $f'(x^*)$: $f'(0) = \kappa^2 > 0$ (unstable); $f'(\pm\kappa) = \kappa^2 - 3\kappa^2 = -2\kappa^2 < 0$ (asymptotically stable). Therefore the constant solutions are $x \equiv 0$ (unstable) and $x \equiv \pm\kappa$ (stable).

### Part (ii), step 1: phase line from uniqueness

By uniqueness solutions cannot cross the equilibria, so the equilibria $-\kappa, 0, \kappa$ split $\mathbb{R}$ into four invariant intervals. Sign of $f = x(\kappa - x)(\kappa + x)$:

| Region | Signs of $x$, $\kappa - x$, $\kappa + x$ | Sign of $f$ | Motion |
| :--- | :--- | :--- | :--- |
| $x > \kappa$ | $+,\ -,\ +$ | $-$ | decreases to $\kappa$ |
| $0 < x < \kappa$ | $+,\ +,\ +$ | $+$ | increases to $\kappa$ |
| $-\kappa < x < 0$ | $-,\ +,\ +$ | $-$ | decreases to $-\kappa$ |
| $x < -\kappa$ | $-,\ +,\ -$ | $+$ | increases to $-\kappa$ |

In each region the solution is monotone and bounded by the neighboring equilibria, hence global in time, with a limit that is an equilibrium: all solutions with $x_0 > 0$ tend to $\kappa$, all with $x_0 < 0$ tend to $-\kappa$, and $x_0 = 0$ stays at $0$.

### Part (ii), step 2: exact solution

Let $x_0 \neq 0$ (then $x(t) \neq 0$ for all $t$, by uniqueness). Compute $w = x^{-2}$ using the chain rule:

$$
w' = -2x^{-3}x' = -2x^{-3}\left(\kappa^2 x - x^3\right) = -2\kappa^2 x^{-2} + 2 = -2\kappa^2 w + 2.
$$

Linear equation $w' + 2\kappa^2 w = 2$. Integrating factor: $\int 2\kappa^2\,dt = 2\kappa^2 t$, $\mu = e^{2\kappa^2 t}$, $\mu(0) = 1$, and $(\mu w)' = 2e^{2\kappa^2 t}$. Barrow from $0$ to $t$:

$$
w(t)\,e^{2\kappa^2 t} - w(0) = \int_0^t 2e^{2\kappa^2 s}\,ds = \frac{1}{\kappa^2}\left[e^{2\kappa^2 s}\right]_0^t = \frac{1}{\kappa^2}\left(e^{2\kappa^2 t} - 1\right).
$$

Hence, with $w(0) = 1/x_0^2$,

$$
w(t) = \frac{1}{\kappa^2} + \left(\frac{1}{x_0^2} - \frac{1}{\kappa^2}\right)e^{-2\kappa^2 t} = \frac{x_0^2 + (\kappa^2 - x_0^2)\,e^{-2\kappa^2 t}}{\kappa^2 x_0^2}.
$$

Since $x = \pm w^{-1/2}$ with the sign fixed by $x_0$ (a solution cannot change sign), and $x(0) = x_0$:

$$
x(t) = \frac{\kappa\,x_0}{\sqrt{x_0^2 + (\kappa^2 - x_0^2)\,e^{-2\kappa^2 t}}}, \qquad x_0 \neq 0.
$$

(For $x_0 = 0$ the solution is $x \equiv 0$, which the formula does not cover.) Check: at $t = 0$, the square root is $\sqrt{\kappa^2} = \kappa$, so $x(0) = x_0$.

### Part (ii), step 3: behavior for $t > 0$

Write $E(t) = e^{-2\kappa^2 t} \in (0, 1]$ for $t \geq 0$. The radicand is $x_0^2(1 - E) + \kappa^2 E$, a convex combination of $x_0^2 > 0$ and $\kappa^2 > 0$, hence positive for all $t \geq 0$: the solution exists for all $t > 0$. As $t \to \infty$, $E \to 0$, the radicand $\to x_0^2$ and

$$
x(t) \to \frac{\kappa\,x_0}{\lvert x_0\rvert} = \kappa\,\operatorname{sgn}(x_0).
$$

| Initial condition | Behavior for $t > 0$ | Limit as $t \to \infty$ |
| :--- | :--- | :--- |
| $x_0 > \kappa$ | decreasing, stays above $\kappa$ | $\kappa$ |
| $x_0 = \kappa$ | constant $x \equiv \kappa$ | $\kappa$ |
| $0 < x_0 < \kappa$ | increasing, stays below $\kappa$ | $\kappa$ |
| $x_0 = 0$ | constant $x \equiv 0$ | $0$ (unstable) |
| $-\kappa < x_0 < 0$ | decreasing, stays above $-\kappa$ | $-\kappa$ |
| $x_0 = -\kappa$ | constant $x \equiv -\kappa$ | $-\kappa$ |
| $x_0 < -\kappa$ | increasing, stays below $-\kappa$ | $-\kappa$ |

Shape of the sketch: for $0 < x_0 < \kappa$ the curve is sigmoidal if $x_0 < \kappa/\sqrt{3}$ (inflection point where $x'' = f'(x)\,x' = 0$, i.e. $f'(x) = \kappa^2 - 3x^2 = 0$, at $x = \kappa/\sqrt{3}$, where the slope is maximal), and concave without inflection if $x_0 \geq \kappa/\sqrt{3}$. The curves for $x_0 < 0$ are mirror images ($x \to -x$).

Behavior backward in time (for completeness): the radicand vanishes when $E = x_0^2/(x_0^2 - \kappa^2)$, which requires $\lvert x_0\rvert > \kappa$ and happens at $t = -\frac{1}{2\kappa^2}\ln\frac{x_0^2}{x_0^2 - \kappa^2} < 0$. So solutions with $\lvert x_0\rvert > \kappa$ blow up in finite negative time, while those with $0 < \lvert x_0\rvert < \kappa$ exist for all $t < 0$ and tend to $0$ as $t \to -\infty$.

---

## Phase 4: Verification, Limits and Interpretation

Check the ODE by differentiating the explicit solution. With $D(t) = x_0^2 + (\kappa^2 - x_0^2)e^{-2\kappa^2 t}$: $x = \kappa x_0 D^{-1/2}$, $x' = -\frac12\kappa x_0 D^{-3/2}D'$, and $D' = -2\kappa^2(\kappa^2 - x_0^2)e^{-2\kappa^2 t}$. Also $\kappa^2 - x^2 = \kappa^2 - \frac{\kappa^2 x_0^2}{D} = \frac{\kappa^2(D - x_0^2)}{D} = \frac{\kappa^2(\kappa^2 - x_0^2)e^{-2\kappa^2 t}}{D}$, so $x(\kappa^2 - x^2) = \kappa x_0 D^{-1/2}\cdot\frac{\kappa^2(\kappa^2 - x_0^2)e^{-2\kappa^2 t}}{D}$. This equals $x'$: $-\frac12\kappa x_0 D^{-3/2}\cdot\left(-2\kappa^2(\kappa^2 - x_0^2)e^{-2\kappa^2 t}\right) = \kappa x_0 D^{-3/2}\kappa^2(\kappa^2 - x_0^2)e^{-2\kappa^2 t}$. They agree.

Numerical check (computed): for $\kappa = 1$, a fourth-order Runge-Kutta integration over $t \in [0, 5]$ (20000 steps) matches the closed form to better than $10^{-14}$ for $x_0 = 0.3,\ 2,\ -0.5,\ -3$. At $t = 5$ the distance to $\kappa = 1$ is $2.3\times 10^{-4}$ for $x_0 = 0.3$ and $1.7\times 10^{-5}$ for $x_0 = 2$, consistent with the time constant $1/(2\kappa^2) = 0.5$.

Time scale and dimensions: the linearization at $x = \pm\kappa$ has rate $f'(\pm\kappa) = -2\kappa^2$, so the approach to $\pm\kappa$ is exponential with time constant $1/(2\kappa^2)$ (visible in the factor $e^{-2\kappa^2 t}$), and at $x = 0$ the repulsion rate is $\kappa^2$. The equation is written in non-dimensional form: $\kappa^2$ is a rate with units $[t]^{-1}$, and $x$ is measured in units for which the cubic coefficient equals $1$.

Bifurcation context (Robinson, Section 7.6): for the parameter $\mu = \kappa^2$ the equation $\dot{x} = \mu x - x^3$ has one equilibrium $x = 0$ (stable) for $\mu < 0$, and for $\mu > 0$ the origin becomes unstable and two stable branches $\pm\sqrt{\mu}$ appear: a supercritical pitchfork. Here $\kappa > 0$ is the case $\mu > 0$.

#### Result

Equilibria $0$ (unstable) and $\pm\kappa$ (stable). For $x_0 \neq 0$: $x(t) = \kappa x_0\big/\sqrt{x_0^2 + (\kappa^2 - x_0^2)e^{-2\kappa^2 t}} \to \kappa\,\operatorname{sgn}(x_0)$ as $t \to \infty$.

---

## Related Notes

- [[04 - Advanced Maths/Concepto - Analisis Cualitativo de EDOs Autonomas y Estabilidad|Qualitative analysis of autonomous ODEs and stability]]
- [[04 - Advanced Maths/Problema - Ch2-P8 General Bernoulli Equation Reduction|Problem 2.8: Bernoulli reduction]]
- [[04 - Advanced Maths/Problema - Ch2-P13 Multi-Equilibria Autonomous Phase Line Dynamics|Problem 2.13: phase line with three equilibria]]
