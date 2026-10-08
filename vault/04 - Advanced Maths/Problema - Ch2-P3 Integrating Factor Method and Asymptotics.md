---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.3"
dificultad: media
tags:
  - problema-resuelto
  - integrating-factor
  - linear-odes
  - integration-by-parts
  - asymptotic-behavior
---

# Problem 2.3: Integrating Factor Method and Asymptotics

Source: ProblemsCh2.pdf, Exercise 3 (page 1). File: sources/cuatrimestre-1/04-advanced-maths/unit-02-first-order-odes/problemas/ProblemsCh2.pdf

Theory reference: Robinson, An Introduction to Ordinary Differential Equations (BookODE's.pdf), Chapter 9, Section 9.2 (integrating factors) and Section 9.3 (examples).

## Problem Statement

Use an integrating factor to solve the following differential equations:

(i) $\dfrac{dy}{dx} + \dfrac{y}{x} = x^2$ (find the general solution and the only solution that is finite when $x = 0$),  
(ii) $\dfrac{dx}{dt} + tx = 4t$ (find the solution with $x(0) = 2$),  
(iii) $\dfrac{dz}{dy} = z\tan y + \sin y$ (find the general solution),  
(iv) $y' + e^{-x}y = 1$ (find the solution when $y(0) = e$, leaving your answer as an integral),  
(v) $\dot{x} + x\tanh t = 3$ (find the general solution, and compare it to that for $\dot{x} + x = 3$),  
(vi) $y' + 2y\cot x = 5$ (find the solution with $y(\pi/2) = 1$),  
(vii) $\dfrac{dx}{dt} + 5x = t$ (find the general solution),  
(viii) with $a > 0$, find the solution of the equation $\dfrac{dx}{dt} + \left[a + \dfrac{1}{t}\right]x = b$ for a general initial condition $x(1) = x_0$, and show that $x(t) \to b/a$ as $t \to \infty$.  

---

## Phase 1: Classification, Hypotheses and Domain

All eight equations are linear first order, so they have the standard form

$$
\frac{dx}{dt} + p(t)\,x = q(t),
$$

with the coefficient of the derivative equal to $1$. If $p$ and $q$ are continuous on an interval $I$, the right-hand side $f(t,x) = q(t) - p(t)x$ and $\partial f/\partial x = -p(t)$ are continuous, so there is exactly one solution through each $(t_0, x_0)$, and linearity makes it exist on all of $I$.

| Part | $p$ | $q$ | Interval of continuity used |
| :--- | :--- | :--- | :--- |
| (i) | $1/x$ | $x^2$ | $x>0$ and $x<0$ separately |
| (ii) | $t$ | $4t$ | $\mathbb{R}$ |
| (iii) | $-\tan y$ | $\sin y$ | $y \in (-\pi/2 + k\pi,\ \pi/2 + k\pi)$ |
| (iv) | $e^{-x}$ | $1$ | $\mathbb{R}$ |
| (v) | $\tanh t$ | $3$ | $\mathbb{R}$ |
| (vi) | $2\cot x$ | $5$ | $(0, \pi)$, which contains $\pi/2$ |
| (vii) | $5$ | $t$ | $\mathbb{R}$ |
| (viii) | $a + 1/t$ | $b$ | $t > 0$, which contains $t=1$ |

---

## Phase 2: Choice of Method and Change of Variables

Why this method: for a linear equation $\dot{x} + p x = q$ with $p$ continuous, choose $\mu(t) = \exp\left(\int p(t)\,dt\right)$. Since $\mu' = p\mu$, the product rule gives $(\mu x)' = \mu\dot{x} + p\mu x = \mu(\dot{x} + p x) = \mu q$, so the left side is an exact derivative and the equation can be integrated directly. Only continuity of $p$ and $q$ is needed (Robinson, Section 9.2).

Procedure: (1) read off $p$ and $q$; (2) compute $P(t) = \int p\,dt$ explicitly, any antiderivative will do, and set $\mu = e^{P}$; (3) write $(\mu x)' = \mu q$; (4) integrate, using Barrow's rule $\left[\mu x\right]_{t_0}^{t} = \int_{t_0}^{t}\mu q\,ds$ when an initial condition is given; (5) divide by $\mu$.

Formula: $\displaystyle x(t) = \frac{1}{\mu(t)}\left[\mu(t_0)x_0 + \int_{t_0}^{t}\mu(s)q(s)\,ds\right]$.

---

## Phase 3: Step-by-Step Derivation

### Part (i): $y' + y/x = x^2$

Here $p = 1/x$, $q = x^2$. An antiderivative of $1/x$ is $\ln\lvert x\rvert$, so $\mu = e^{\ln\lvert x\rvert} = \lvert x\rvert$. Any nonzero constant multiple of $\mu$ also works, and on each half-line $\mu = x$ or $\mu = -x$ are both valid; we use $\mu = x$ on both half-lines (check: $(xy)' = xy' + y = x(y' + y/x)$ for any $x \neq 0$). Multiply the equation by $x$:

$$
\frac{d}{dx}\left(x\,y\right) = x\cdot x^2 = x^3.
$$

Integrate: $x\,y = \int x^3\,dx = \dfrac{x^4}{4} + C$. Divide by $x$:

$$
y(x) = \frac{x^3}{4} + \frac{C}{x}, \qquad x \neq 0.
$$

Finiteness at $x = 0$: $x^3/4 \to 0$, whereas $C/x \to \pm\infty$ as $x \to 0$ unless $C = 0$. So the only solution that stays finite at $x = 0$ is

$$
y(x) = \frac{x^3}{4},
$$

which is smooth on all of $\mathbb{R}$ and satisfies $x y' + y = x\cdot\frac{3x^2}{4} + \frac{x^3}{4} = x^3$ also at $x = 0$.

### Part (ii): $\dot{x} + t x = 4t$, $x(0) = 2$

$p = t$, $q = 4t$. $P(t) = \int t\,dt = t^2/2$, so $\mu = e^{t^2/2}$ and $\mu(0) = 1$. Then $(\mu x)' = 4t\,e^{t^2/2}$. Integrate from $0$ to $t$ (Barrow):

$$
x(t)e^{t^2/2} - x(0)\cdot 1 = \int_0^t 4s\,e^{s^2/2}\,ds.
$$

Substitute $u = s^2/2$, $du = s\,ds$; the limits $s = 0, t$ become $u = 0, t^2/2$:

$$
\int_0^t 4s\,e^{s^2/2}\,ds = 4\int_0^{t^2/2} e^{u}\,du = 4\left[e^{u}\right]_0^{t^2/2} = 4\left(e^{t^2/2} - 1\right).
$$

So $x(t)e^{t^2/2} = 2 + 4e^{t^2/2} - 4$, and dividing by $e^{t^2/2}$:

$$
x(t) = 4 - 2e^{-t^2/2}.
$$

### Part (iii): $dz/dy = z\tan y + \sin y$

Rewrite in standard form with independent variable $y$: $z' - (\tan y)\,z = \sin y$, so $p = -\tan y$, $q = \sin y$. Compute $P$ with $u = \cos y$, $du = -\sin y\,dy$:

$$
P(y) = -\int \tan y\,dy = -\int \frac{\sin y}{\cos y}\,dy = \int \frac{du}{u} = \ln\lvert\cos y\rvert.
$$

So $\mu = \lvert\cos y\rvert$; on an interval where $\cos y$ has constant sign we may use $\mu = \cos y$ (check: $(z\cos y)' = z'\cos y - z\sin y = \cos y\,(z' - z\tan y)$). Then

$$
\frac{d}{dy}\left(z\cos y\right) = \cos y\,\sin y.
$$

Integrate with $v = \sin y$, $dv = \cos y\,dy$: $\int \sin y\cos y\,dy = \int v\,dv = \frac{1}{2}\sin^2 y$. Hence $z\cos y = \frac12\sin^2 y + C$ and

$$
z(y) = \frac{\sin^2 y}{2\cos y} + \frac{C}{\cos y} = \frac{1}{2}\sin y\tan y + C\sec y, \qquad \cos y \neq 0.
$$

### Part (iv): $y' + e^{-x}y = 1$, $y(0) = e$

$p = e^{-x}$, $q = 1$. Choose the antiderivative that vanishes at the initial point:

$$
P(x) = \int_0^x e^{-s}\,ds = \left[-e^{-s}\right]_0^x = 1 - e^{-x}, \qquad \mu(x) = e^{1 - e^{-x}}, \quad \mu(0) = e^{0} = 1.
$$

Then $(\mu y)' = \mu$. Barrow from $0$ to $x$:

$$
y(x)\,\mu(x) - y(0)\,\mu(0) = \int_0^x e^{1 - e^{-s}}\,ds = e\int_0^x e^{-e^{-s}}\,ds.
$$

With $y(0) = e$ and $\mu(0) = 1$ the term $y(0)\mu(0) = e$ moves to the right-hand side. Divide by $\mu(x) = e\cdot e^{-e^{-x}}$, i.e. multiply by $1/\mu(x) = e^{-1}e^{e^{-x}}$:

$$
y(x) = e^{-1}e^{e^{-x}}\left[e + e\int_0^x e^{-e^{-s}}\,ds\right] = e^{e^{-x}}\left[1 + \int_0^x e^{-e^{-s}}\,ds\right].
$$

The remaining integral has no elementary antiderivative (the substitution $w = e^{-s}$ turns it into $-\int e^{-w}\,dw/w$, an exponential-integral function), so the answer is left as an integral, as requested.

### Part (v): $\dot{x} + x\tanh t = 3$

$p = \tanh t = \sinh t/\cosh t$, $q = 3$. With $u = \cosh t$, $du = \sinh t\,dt$:

$$
P(t) = \int \frac{\sinh t}{\cosh t}\,dt = \int\frac{du}{u} = \ln\cosh t \quad (\cosh t > 0), \qquad \mu = \cosh t.
$$

$$
\frac{d}{dt}\left(x\cosh t\right) = 3\cosh t \ \Longrightarrow\ x\cosh t = 3\sinh t + C \ \Longrightarrow\ x(t) = 3\tanh t + C\,\operatorname{sech} t.
$$

Comparison equation $\dot{x} + x = 3$: $p = 1$, $\mu = e^{t}$, $(xe^{t})' = 3e^{t}$, so $xe^{t} = 3e^{t} + C_2$ and $x_{\mathrm{c}}(t) = 3 + C_2 e^{-t}$.

- As $t \to +\infty$: $\tanh t \to 1$ and $\operatorname{sech} t \to 0$, so $x \to 3$, exactly as $x_{\mathrm c} \to 3$. Both approach $3$ at rate $e^{-t}$ (since $\operatorname{sech} t \sim 2e^{-t}$ and $3 - 3\tanh t \sim 6e^{-2t}$).
- As $t \to -\infty$: $\tanh t \to -1$, $\operatorname{sech} t \to 0$, so $x \to -3$ for every $C$, whereas $x_{\mathrm c} = 3 + C_2e^{-t}$ diverges to $\operatorname{sgn}(C_2)\cdot\infty$ unless $C_2 = 0$.

The difference comes from the coefficient: $\tanh t \to \pm 1$ changes sign with $t$, so the equation behaves like $\dot{x} + x = 3$ for $t \gg 1$ and like $\dot{x} - x = 3$ for $t \ll -1$, whose equilibrium is $x = -3$.

### Part (vi): $y' + 2y\cot x = 5$, $y(\pi/2) = 1$

$p = 2\cot x$, $q = 5$, on $(0,\pi)$ where $\sin x > 0$. With $u = \sin x$, $du = \cos x\,dx$:

$$
P(x) = 2\int \frac{\cos x}{\sin x}\,dx = 2\ln(\sin x), \qquad \mu = e^{2\ln\sin x} = \sin^2 x, \quad \mu(\pi/2) = 1.
$$

Then $(y\sin^2 x)' = 5\sin^2 x = \frac{5}{2}(1 - \cos 2x)$ (half-angle identity). Primitive: $\int \frac52(1 - \cos 2x)\,dx = \frac52 x - \frac54\sin 2x$ (for the cosine term put $v = 2x$, $dv = 2\,dx$). Barrow from $\pi/2$ to $x$:

$$
y\sin^2 x - 1\cdot 1 = \left[\frac52 s - \frac54\sin 2s\right]_{\pi/2}^{x} = \frac52 x - \frac54\sin 2x - \frac{5\pi}{4} + \frac54\sin\pi.
$$

Since $\sin\pi = 0$:

$$
y(x) = \frac{1 + \frac52 x - \frac54\sin 2x - \frac{5\pi}{4}}{\sin^2 x}, \qquad 0 < x < \pi.
$$

Behavior at the ends of the interval: the numerator tends to $1 - \frac{5\pi}{4} \approx -2.927 \neq 0$ as $x \to 0^+$ and to $1 + \frac{5\pi}{4} \approx 4.927 \neq 0$ as $x \to \pi^-$, while $\sin^2 x \to 0$. So $y \to -\infty$ at $0^+$ and $y \to +\infty$ at $\pi^-$: the maximal interval of existence is exactly $(0,\pi)$, where $p$ is continuous.

### Part (vii): $\dot{x} + 5x = t$

$p = 5$, $q = t$, $\mu = e^{5t}$, so $(xe^{5t})' = t\,e^{5t}$. Integrate by parts with $u = t$, $dv = e^{5t}dt$, $du = dt$, $v = e^{5t}/5$:

$$
\int t\,e^{5t}\,dt = \frac{t\,e^{5t}}{5} - \int \frac{e^{5t}}{5}\,dt = \frac{t\,e^{5t}}{5} - \frac{e^{5t}}{25} + C.
$$

Divide by $e^{5t}$:

$$
x(t) = \frac{t}{5} - \frac{1}{25} + C\,e^{-5t}.
$$

### Part (viii): $\dot{x} + (a + 1/t)x = b$, $a > 0$, $x(1) = x_0$

On $t > 0$: $P(t) = \int\left(a + \frac1t\right)dt = at + \ln t$, so $\mu = e^{at + \ln t} = t\,e^{at}$ and $\mu(1) = e^{a}$. Then $(t\,e^{at}x)' = b\,t\,e^{at}$. Barrow from $1$ to $t$:

$$
t\,e^{at}x(t) - e^{a}x_0 = b\int_1^t s\,e^{as}\,ds.
$$

Integration by parts ($u = s$, $dv = e^{as}ds$, $v = e^{as}/a$):

$$
\int_1^t s\,e^{as}\,ds = \left[\frac{s\,e^{as}}{a} - \frac{e^{as}}{a^2}\right]_1^t = \frac{t\,e^{at}}{a} - \frac{e^{at}}{a^2} - \frac{e^{a}}{a} + \frac{e^{a}}{a^2}.
$$

Hence

$$
t\,e^{at}x(t) = e^{a}x_0 + b\left[\frac{t\,e^{at}}{a} - \frac{e^{at}}{a^2} - \frac{e^{a}}{a} + \frac{e^{a}}{a^2}\right].
$$

Divide by $t\,e^{at}$:

$$
x(t) = \frac{b}{a} - \frac{b}{a^2\,t} + \frac{e^{-a(t-1)}}{t}\left(x_0 - \frac{b}{a} + \frac{b}{a^2}\right).
$$

Limit $t \to \infty$ with $a > 0$: $\frac{b}{a^2 t} \to 0$, and the last term is $\frac{K\,e^{-a(t-1)}}{t}$ with $K = x_0 - b/a + b/a^2$ constant; since $e^{-a(t-1)} \to 0$ and $1/t \to 0$ the product tends to $0$. Therefore

$$
\lim_{t\to\infty} x(t) = \frac{b}{a}.
$$

---

## Phase 4: Verification, Limits and Interpretation

Substitution checks (each solution inserted into its equation):

- (i) $y = x^3/4 + C/x$: $y' = \frac{3x^2}{4} - \frac{C}{x^2}$, $\frac{y}{x} = \frac{x^2}{4} + \frac{C}{x^2}$; the sum is $x^2$.
- (ii) $x = 4 - 2e^{-t^2/2}$: $\dot{x} = 2t\,e^{-t^2/2}$, $t x = 4t - 2t e^{-t^2/2}$; the sum is $4t$ and $x(0) = 2$. As $t \to \pm\infty$, $x \to 4$, the constant solution of $\dot{x} + tx = 4t$.
- (iii) $z = \frac12\sin y\tan y + C\sec y$: sympy substitution of this expression gives $z' - z\tan y - \sin y = 0$.
- (iv) $y(0) = e^{1}[1 + 0] = e$; differentiating, $y' = -e^{-x}y + e^{e^{-x}}e^{-e^{-x}} = -e^{-x}y + 1$.
- (v) $x = 3\tanh t + C\operatorname{sech}t$: $\dot{x} = 3\operatorname{sech}^2 t - C\operatorname{sech}t\tanh t$ and $x\tanh t = 3\tanh^2 t + C\operatorname{sech}t\tanh t$; the sum is $3(\operatorname{sech}^2 t + \tanh^2 t) = 3$.
- (vi) at $x = \pi/2$: numerator $= 1 + \frac{5\pi}{4} - 0 - \frac{5\pi}{4} = 1$, denominator $1$, so $y(\pi/2) = 1$; the ODE is satisfied (sympy residual $0$).
- (vii) the particular solution $x_p = t/5 - 1/25$ satisfies $\dot{x}_p + 5x_p = \frac15 + t - \frac15 = t$, and $Ce^{-5t}$ solves the homogeneous equation.
- (viii) $x(1) = \frac{b}{a} - \frac{b}{a^2} + x_0 - \frac{b}{a} + \frac{b}{a^2} = x_0$.

Dimensional remark for (viii), as a generic relaxation model with $a$ a rate: $[a] = [t]^{-1}$ makes $a t$ dimensionless, and $b/a$ has the dimensions of $x$, as required for the equilibrium of $\dot{x} = b - a x$. The term $1/t$ in the coefficient has the same dimensions as $a$.

#### Results

| Part | Integrating factor $\mu$ | Solution |
| :--- | :--- | :--- |
| (i) | $x$ | $y = \frac{x^3}{4} + \frac{C}{x}$; finite at $0$: $y = \frac{x^3}{4}$ |
| (ii) | $e^{t^2/2}$ | $x = 4 - 2e^{-t^2/2}$ |
| (iii) | $\cos y$ | $z = \frac12\sin y\tan y + C\sec y$ |
| (iv) | $e^{1-e^{-x}}$ | $y = e^{e^{-x}}\left(1 + \int_0^x e^{-e^{-s}}ds\right)$ |
| (v) | $\cosh t$ | $x = 3\tanh t + C\operatorname{sech}t$ |
| (vi) | $\sin^2 x$ | $y = \frac{1 + \frac52 x - \frac54\sin 2x - \frac{5\pi}{4}}{\sin^2 x}$ |
| (vii) | $e^{5t}$ | $x = \frac{t}{5} - \frac{1}{25} + Ce^{-5t}$ |
| (viii) | $t\,e^{at}$ | $x = \frac{b}{a} - \frac{b}{a^2 t} + \frac{e^{-a(t-1)}}{t}\left(x_0 - \frac{b}{a} + \frac{b}{a^2}\right)$, limit $b/a$ |

---

## Related Notes

- [[04 - Advanced Maths/Concepto - Factor Integrante y Ecuaciones Lineales de Primer Orden|Integrating factor theory]]
- [[04 - Advanced Maths/Problema - Ch2-P10 Uniqueness via Integrating Transformation|Problem 2.10: uniqueness via an integrating transformation]]
