---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.2"
dificultad: media
tags:
  - problema-resuelto
  - separable-equations
  - initial-value-problem
  - finite-time-blow-up
  - asymptotics
---

# Problem 2.2: Separable Equations and Asymptotic Integrals

Source: ProblemsCh2.pdf, Exercise 2 (page 1). File: sources/cuatrimestre-1/04-advanced-maths/unit-02-first-order-odes/problemas/ProblemsCh2.pdf

Theory reference: Robinson, An Introduction to Ordinary Differential Equations (BookODE's.pdf), Chapter 8 (Sections 8.1 'The solution recipe' and 8.4 'Justifying the method') and Section 6.3 (maximal interval of existence).

## Problem Statement

Solve the following equations:

(i) $\dot{x} = t^3(1-x)$ with $x(0) = 3$;  
(ii) $y' = (1+y^2)\tan x$ with $y(0) = 1$;  
(iii) $\dot{x} = t^2 x$ (general solution);  
(iv) $\dot{x} = -x^2$ (general solution);  
(v) $dy/dt = e^{-t^2}y^2$: give the solution in terms of an integral and describe the behavior as $t \to \infty$ depending on the initial condition $y(0)$. Use that $\int_0^{\infty} e^{-s^2}\,ds = \sqrt{\pi}/2$.  

---

## Phase 1: Classification, Hypotheses and Domain

All five equations have the separable form $\dot{x} = g(t)\,h(x)$ (the letters $x(t)$, $y(x)$ or $y(t)$ are used as in the statement).

- (i) $g(t) = t^3$, $h(x) = 1-x$. $f(t,x) = t^3(1-x)$ and $\partial f/\partial x = -t^3$ are continuous on $\mathbb{R}^2$, so the IVP has a unique local solution (Robinson, Theorem 6.2). The only equilibrium is $x \equiv 1$; since $x(0)=3 \neq 1$ and solutions cannot cross an equilibrium (uniqueness), $x(t) > 1$ for all $t$.
- (ii) $g(x) = \tan x$, $h(y) = 1+y^2$. $f$ and $\partial f/\partial y = 2y\tan x$ are continuous for $x \in (-\pi/2, \pi/2)$, which contains $x=0$. There are no equilibria because $1+y^2 \ge 1$.
- (iii) $g(t) = t^2$, $h(x) = x$: linear and homogeneous; $f$, $\partial f/\partial x = t^2$ continuous on $\mathbb{R}^2$. Equilibrium $x \equiv 0$.
- (iv) $h(x) = -x^2$: $f$, $\partial f/\partial x = -2x$ continuous on $\mathbb{R}^2$. Equilibrium $x \equiv 0$. Because $f$ grows quadratically, finite-time blow-up is possible.
- (v) $g(t) = e^{-t^2}$, $h(y) = y^2$: $f$, $\partial f/\partial y = 2y e^{-t^2}$ continuous on $\mathbb{R}^2$. Equilibrium $y \equiv 0$. Again $h$ is quadratic, so blow-up in finite time must be checked.

---

## Phase 2: Choice of Method and Change of Variables

Why this method: if $\dot{x} = g(t)h(x)$ and $h(x_0) \neq 0$, then near the initial point $\frac{1}{h(x)}\dot{x} = g(t)$, and integrating both sides in $t$ (the left side by the substitution $x = x(t)$, $dx = \dot{x}\,dt$) gives $H(x(t)) - H(x_0) = G(t) - G(t_0)$, with $H' = 1/h$ and $G' = g$. This requires $h \neq 0$ along the solution (equilibria $h(x^*) = 0$ are treated separately and are excluded from the division) and $g$, $1/h$ continuous (Robinson, Section 8.4).

Procedure used throughout, written explicitly each time:

- find the equilibria $h(x^*) = 0$ and the interval containing $x_0$ where $h \neq 0$;
- separate: $\frac{dx}{h(x)} = g(t)\,dt$;
- integrate with Barrow's rule from $(t_0, x_0)$: $\left[H(s)\right]_{x_0}^{x} = \left[G(\tau)\right]_{t_0}^{t}$, so the constant is fixed automatically;
- solve for $x$, track the sign inside absolute values, and determine the maximal interval of existence.

---

## Phase 3: Step-by-Step Derivation

### Part (i): $\dot{x} = t^3(1-x)$, $x(0)=3$

Equilibrium: $1-x=0$, i.e. $x \equiv 1$. The initial value $x(0)=3 > 1$, so $1-x < 0$ along the solution. Separate and integrate from $(0,3)$ with Barrow's rule:

$$
\int_{3}^{x} \frac{ds}{1-s} = \int_{0}^{t} \tau^3\,d\tau.
$$

Left side: $\int \frac{ds}{1-s} = -\ln\lvert 1-s\rvert$ (put $u = 1-s$, $du = -ds$). Right side: $\left[\tau^4/4\right]_0^t = t^4/4$. Substitute the limits:

$$
\Big[-\ln\lvert 1-s\rvert\Big]_{3}^{x} = -\ln\lvert 1-x\rvert + \ln\lvert 1-3\rvert = -\ln\lvert 1-x\rvert + \ln 2 = \frac{t^4}{4}.
$$

Solve: $\ln\lvert 1-x\rvert = \ln 2 - t^4/4$, hence $\lvert 1-x\rvert = 2e^{-t^4/4}$. Because $x - 1 > 0$ for all $t$ (no crossing of the equilibrium), $\lvert 1-x\rvert = x-1$ and

$$
x(t) = 1 + 2e^{-t^4/4}, \qquad t \in \mathbb{R}.
$$

### Part (ii): $y' = (1+y^2)\tan x$, $y(0)=1$

No equilibria. Separate: $\frac{dy}{1+y^2} = \tan x\,dx$. Integrate from $(0,1)$:

$$
\int_{1}^{y} \frac{ds}{1+s^2} = \int_{0}^{x} \tan\sigma\,d\sigma.
$$

Left: $\arctan s$. Right: $\int \tan\sigma\,d\sigma = \int \frac{\sin\sigma}{\cos\sigma}\,d\sigma$; put $u = \cos\sigma$, $du = -\sin\sigma\,d\sigma$, giving $-\int du/u = -\ln\lvert\cos\sigma\rvert$. On $(-\pi/2,\pi/2)$, $\cos\sigma > 0$. Substitute the limits:

$$
\arctan y - \arctan 1 = -\ln(\cos x) + \ln(\cos 0) = -\ln(\cos x).
$$

With $\arctan 1 = \pi/4$ and $\ln\cos 0 = 0$:

$$
\arctan y = \frac{\pi}{4} - \ln(\cos x) \quad\Longrightarrow\quad y(x) = \tan\left(\frac{\pi}{4} - \ln\cos x\right).
$$

Domain: $\arctan y \in (-\pi/2, \pi/2)$ is required. Since $\cos x \le 1$, $-\ln\cos x \ge 0$, so the argument $\pi/4 - \ln\cos x \ge \pi/4 > -\pi/2$ and the constraint is $\frac{\pi}{4} - \ln\cos x < \frac{\pi}{2}$, i.e. $\ln\cos x > -\frac{\pi}{4}$, i.e. $\cos x > e^{-\pi/4}$. This defines the symmetric interval $\lvert x\rvert < x^*$ with

$$
x^* = \arccos\left(e^{-\pi/4}\right) \approx 1.0974 \ (< \pi/2 \approx 1.5708).
$$

As $x \to x^{*-}$, $\arctan y \to \pi/2$, so $y \to +\infty$: the solution blows up at the finite point $x^*$ (and symmetrically at $-x^*$, because $\cos$ is even). The maximal interval of existence is $(-x^*, x^*)$, strictly smaller than the interval $(-\pi/2,\pi/2)$ where $f$ is continuous. This is the situation described in Robinson, Section 6.3.

### Part (iii): $\dot{x} = t^2 x$ (general solution)

Equilibrium $x \equiv 0$. For $x \neq 0$ separate and integrate (indefinite form, then fix the constant):

$$
\int \frac{dx}{x} = \int t^2\,dt \quad\Longrightarrow\quad \ln\lvert x\rvert = \frac{t^3}{3} + c.
$$

Exponentiate: $\lvert x\rvert = e^{c}e^{t^3/3}$, so $x = \pm e^{c}e^{t^3/3}$. Put $A = \pm e^{c} \in \mathbb{R}\setminus\{0\}$. The equilibrium $x \equiv 0$ corresponds to $A = 0$ and indeed satisfies the equation, so

$$
x(t) = A\,e^{t^3/3}, \qquad A \in \mathbb{R},\ t \in \mathbb{R}.
$$

### Part (iv): $\dot{x} = -x^2$ (general solution)

Equilibrium $x \equiv 0$. For $x \neq 0$, separate: $\frac{dx}{x^2} = -dt$. Integrate:

$$
\int x^{-2}\,dx = -\int dt \quad\Longrightarrow\quad -\frac{1}{x} = -t + c \quad\Longrightarrow\quad x(t) = \frac{1}{t + k}, \quad k = -c.
$$

The family $x = 1/(t+k)$, $k \in \mathbb{R}$, together with the equilibrium $x \equiv 0$ (which is not obtained for any finite $k$), is the full set of solutions. With the initial condition $x(0) = x_0 \neq 0$ one gets $k = 1/x_0$, i.e.

$$
x(t) = \frac{x_0}{1 + x_0 t}.
$$

Each member with $x_0 \neq 0$ blows up at $t^* = -1/x_0$. If $x_0 > 0$ the solution exists for $t > -1/x_0$ (it decays to $0$ as $t \to +\infty$). If $x_0 < 0$ it exists for $t < -1/x_0 = 1/\lvert x_0\rvert$ and blows up forward in time at $t^* = 1/\lvert x_0\rvert$.

### Part (v): $dy/dt = e^{-t^2}y^2$

Equilibrium $y \equiv 0$ (initial condition $y(0) = 0$). Suppose $y_0 = y(0) \neq 0$. Separate and integrate from $(0, y_0)$:

$$
\int_{y_0}^{y} \frac{ds}{s^2} = \int_{0}^{t} e^{-\tau^2}\,d\tau =: I(t).
$$

Left side: $\left[-1/s\right]_{y_0}^{y} = -\frac{1}{y} + \frac{1}{y_0}$. So

$$
\frac{1}{y} = \frac{1}{y_0} - I(t) \quad\Longrightarrow\quad y(t) = \frac{y_0}{1 - y_0\,I(t)}, \qquad I(t) = \int_0^t e^{-\tau^2}\,d\tau.
$$

This formula also gives $y \equiv 0$ for $y_0 = 0$. The function $I$ is odd, strictly increasing ($I' = e^{-t^2} > 0$), with $I(0) = 0$ and, by the given integral, $I(t) \to \sqrt{\pi}/2$ as $t \to +\infty$. Hence on $t \ge 0$ we have $0 \le I(t) < \sqrt{\pi}/2$. The denominator $D(t) = 1 - y_0 I(t)$ decides the behavior.

Case $y_0 \le 0$: then $-y_0 I(t) \ge 0$, so $D(t) \ge 1 > 0$ for all $t \ge 0$ and no blow-up occurs. As $t \to \infty$:

$$
y(t) \to \frac{y_0}{1 - y_0\sqrt{\pi}/2} = \frac{2y_0}{2 - \sqrt{\pi}\,y_0} =: y_\infty \le 0.
$$

Case $0 < y_0 < 2/\sqrt{\pi}$: $y_0 I(t) < y_0\sqrt{\pi}/2 < 1$, so $D(t) > 1 - y_0\sqrt{\pi}/2 > 0$ and again $y(t) \to y_\infty = \frac{2y_0}{2 - \sqrt{\pi}\,y_0} > 0$, a finite limit larger than $y_0$.

Case $y_0 = 2/\sqrt{\pi}$: $D(t) = \frac{2}{\sqrt{\pi}}\left(\frac{\sqrt{\pi}}{2} - I(t)\right) = \frac{2}{\sqrt{\pi}}\int_t^{\infty} e^{-s^2}\,ds > 0$ for every finite $t$ but $D(t) \to 0^+$. Thus $y(t) \to +\infty$ as $t \to \infty$, without finite-time blow-up (it grows like $e^{t^2}$ up to a power of $t$, since $\int_t^\infty e^{-s^2}ds \sim e^{-t^2}/(2t)$).

Case $y_0 > 2/\sqrt{\pi}$: $D(0) = 1$ and $D$ decreases continuously to $1 - y_0\sqrt{\pi}/2 < 0$, so there is a unique $T^* > 0$ with $I(T^*) = 1/y_0$, where $D(T^*) = 0$ and $y \to +\infty$. This is finite-time blow-up. In terms of the error function, $I(t) = \frac{\sqrt{\pi}}{2}\operatorname{erf}(t)$, so $T^* = \operatorname{erf}^{-1}\left(\frac{2}{\sqrt{\pi}\,y_0}\right)$. The solution exists only on $0 \le t < T^*$; the limit $t \to \infty$ is not reached. Example: for $y_0 = 2$, solving $I(T^*) = 1/2$ numerically (mpmath quadrature and root finding) gives $T^* \approx 0.5510$, equal to $\operatorname{erf}^{-1}(1/\sqrt{\pi})$.

---

## Phase 4: Verification, Limits and Interpretation

Substitution checks:

- (i) $\dot{x} = 2e^{-t^4/4}\cdot\left(-\frac{4t^3}{4}\right) = -2t^3 e^{-t^4/4}$ and $t^3(1-x) = t^3\left(-2e^{-t^4/4}\right)$. They agree, and $x(0) = 1+2 = 3$. As $t \to \pm\infty$, $x \to 1$ (the equilibrium), approached from above.
- (ii) With $\theta = \pi/4 - \ln\cos x$, $y = \tan\theta$, $y' = (1+\tan^2\theta)\,\theta'$ and $\theta' = \tan x$. Hence $y' = (1+y^2)\tan x$. At $x = 0$: $\theta = \pi/4$, $y = 1$. Numerically $x^* = \arccos(e^{-\pi/4}) \approx 1.0974$; at $x = x^* - 10^{-6}$ the formula gives $y \approx 5.1\times 10^{5}$, confirming the blow-up.
- (iii) $\dot{x} = A\,t^2 e^{t^3/3} = t^2 x$.
- (iv) $\dot{x} = -\frac{1}{(t+k)^2} = -x^2$.
- (v) $y' = \frac{y_0 \cdot y_0 I'(t)}{(1 - y_0 I)^2} = y^2 e^{-t^2}$, since $I'(t) = e^{-t^2}$.

Time scales: in (ii) the natural variable is the spatial coordinate $x$, with blow-up at $x^* \approx 1.0974$ rather than as $x \to \pi/2$; in (iv) the blow-up time is $-1/x_0$; in (v) the blow-up time is $T^* = \operatorname{erf}^{-1}\!\left(2/(\sqrt{\pi}\,y_0)\right)$ when $y_0 > 2/\sqrt{\pi}$, so for those data a statement about $t \to \infty$ is meaningless. For all other $y_0$ the long-time behavior is governed by the finite integral $\int_0^\infty e^{-s^2}ds = \sqrt{\pi}/2$.

#### Summary of (v) for $t \to \infty$

| Initial condition | Behavior |
| :--- | :--- |
| $y_0 < 2/\sqrt{\pi}$ | bounded, $y \to \frac{2y_0}{2 - \sqrt{\pi}\,y_0}$ (equals $0$ for $y_0 = 0$) |
| $y_0 = 2/\sqrt{\pi}$ | $y \to +\infty$ as $t \to \infty$, no finite blow-up |
| $y_0 > 2/\sqrt{\pi}$ | blow-up at finite $T^*$ with $\operatorname{erf}(T^*) = 2/(\sqrt{\pi}\,y_0)$ |

---

## Related Notes

- [[04 - Advanced Maths/Concepto - Metodos de Integracion Directa y Ecuaciones Separables|Direct integration and separable equations]]
- [[04 - Advanced Maths/Concepto - Well-Posed Problems and Picard Theorem|Picard theorem and well-posedness]]
- [[04 - Advanced Maths/Problema - Ch2-P13 Multi-Equilibria Autonomous Phase Line Dynamics|Problem 2.13: finite-time blow-up on the phase line]]
