---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
tags:
  - moc-tema
  - advanced-maths
  - segundo-curso
  - edos-primer-orden
  - dinamica-cualitativa
dificultad: media
fuentes:
  - "Notes.pdf (class notes 'Diff Eq', pp. 3-4), sources/cuatrimestre-1/04-advanced-maths/teoria/Notes.pdf"
  - "Robinson (2004), An Introduction to Ordinary Differential Equations, Ch. 6-10"
  - "ProblemsCh2.pdf (Department of Mathematics, UC3M)"
---

# Topic 2: First-Order ODEs: Existence, Stability and Explicit Solutions

> **Key takeaway:** an initial value problem has exactly one local solution when $f$ and $\partial f/\partial y$ are continuous (Picard). For autonomous equations the sign of $f'$ at a stationary point decides its stability. Three classes of equations have explicit solutions: separable equations, linear equations (integrating factor) and exact equations.

This note follows pages 3 and 4 of the class notes (`Notes.pdf`) in their order. Robinson (2004) formalises and extends each step; material that is not in the notes is labelled **Complement (Robinson)**. The web page is `subjects/advanced-maths/teoria/topic-2.html`; sections 1-10 below match its sections.

---

## 1. Initial value problems [Notes, p. 3; Robinson, Sec. 6.1]

An IVP for a first-order ODE is
$$\begin{cases} y'(x) = f\big(x, y(x)\big),\\ y(x_0) = y_0. \end{cases}$$
We look for the **existence** and the **uniqueness** of the solution. (Reading note: the first line of p. 3 writes $y(a_0) = x_0$; the statement of Picard's theorem on the same page writes $y(x_0) = y_0$.)

Robinson writes the same problem as $\dot x = f(x, t)$, $x(t_0) = x_0$ (Eq. 6.2) and defines a solution on an open interval $I \ni t_0$ (Definition 6.1, p. 40).

**Complement (Robinson).** Hadamard's well-posedness (existence, uniqueness, continuous dependence); uniqueness means the model is deterministic (p. 39); an IVP with no solution: $x^2 + t^2\dot x = 0$, $x(0) = c \neq 0$ (p. 38).

## 2. Picard's theorem [Notes, p. 3; Robinson, Thm 6.2, p. 40]

> Let $f$ and $\dfrac{\partial f}{\partial y}$ be continuous functions of $x$ and $y$ near the initial value $(x_0, y_0)$. Then there exists $h > 0$ such that the IVP $y' = f(x, y)$, $y(x_0) = y_0$ has a unique solution for $|x - x_0| < h$.

In Robinson's variables ($t$ independent, $x$ unknown) the derivative to check is $\partial f/\partial x$. The conclusion is local.

**Complement (Robinson).** Lipschitz condition $|f(x,t) - f(y,t)| \le L|x - y|$ (Eq. 6.5) and the Mean Value Theorem proof that a bounded derivative gives it; uniqueness and continuous dependence from $Z = (x - y)^2$, $\dot Z \le 2LZ$, so $|x(t) - y(t)| \le |x_0 - y_0|e^{L(t - t_0)}$ (Exercises 6.3, 9.7); Picard iteration $x_{n+1} = x_0 + \int_0^t f(x_n)$, which for $\dot x = x$ gives the Taylor polynomials of $e^t$ (Exercise 6.4).

## 3. Complement: when the theorem fails [Robinson, Secs. 6.1, 6.3]

- $\dot x = \sqrt x$, $x(0) = 0$: infinitely many solutions $x_c = (t - c)^2/4$ for $t > c$, because $\partial f/\partial x = \tfrac12 x^{-1/2}$ is unbounded at $0$ (same for $x^{1/3}$).
- $\dot x = x^2$: unique, but $x = 1/(x_0^{-1} - t)$ blows up at $t = 1/x_0$: the theorem is only local.
- Navier-Stokes global existence is open (Millennium Prize).

## 4. Autonomous first-order ODEs and stationary points [Notes, p. 3; Robinson, Secs. 7.1-7.3]

**Autonomous:** $x'(t) = f$ with $f$ depending only on $x$. $x' = x^3$ is autonomous ($f(x) = x^3$); $x' = t^2x$ is not ($f(x, t) = t^2x$).

**Stationary points [Notes, p. 3]:** points $x$ with $f(x) = 0$.
- $f(x) = 0$ and $f'(x) > 0$: $x$ is **unstable**.
- $f(x) = 0$ and $f'(x) < 0$: $x$ is a **stable** stationary point.

If $x(0) = x^*$ with $f(x^*) = 0$, then $x'(0) = 0$ and by uniqueness $x(t) \equiv x^*$.

**The sketch of the notes.** $f$ an arch with zeros $\underline x < \overline x$, $f > 0$ between them:
- $\underline x < x_0 < \overline x$: $f(x_0) > 0$, $x' > 0$, the solution goes right;
- $x_0 < \underline x$ or $x_0 > \overline x$: $f(x_0) < 0$, $x' < 0$, it goes left.

So point 1 ($\underline x$, where $f' > 0$) is unstable and point 2 ($\overline x$, where $f' < 0$) is stable. For $f = (x - \underline x)(\overline x - x)$: $f' = (\overline x - x) - (x - \underline x)$, $f'(\underline x) = \overline x - \underline x > 0$, $f'(\overline x) = -(\overline x - \underline x) < 0$.

**Concrete example [Notes, p. 3]:** $x' = kx(1 - x/M) = kx - \frac kMx^2$ (non-linear), $x(0) = x_0 \ge 0$, $k, M > 0$.
1. Critical points: $x = 0$, $x = M$.
2. $f'(x) = k - \frac{2k}{M}x$.
3. $f'(0) = k > 0$: unstable. $f'(M) = k - 2k = -k < 0$: stable.

Each curve of the sketch is a solution; $0$ is unstable because a slight variation goes to $M$; $x_0 = 0$ stays at $0$; $x_0 \neq 0$ ends up at $M$.

**Complement (Robinson).** Monotonicity of solutions and no finite-time arrival at a stationary point (p. 47); $\varepsilon$-$\delta$ definitions of stable and attracting (Eqs. 7.2-7.3); linearisation $\dot\xi \approx f'(x^*)\xi$; the cubic $-x(1-x)(2-x)$; terminal velocity $v^* = \sqrt{mg/k}$; $\dot x = |x|$ vs $\dot x = x^2$ (same phase line, different speed).

## 5. Complement: bifurcations [Robinson, Secs. 7.4, 7.6]

Structural stability; bifurcation near $x^*$ requires $f'(x^*) = 0$; pitchfork $\dot x = x(k - x^2)$, saddle-node $\dot x = x^2 - k$, transcritical $\dot x = kx - x^2$.

## 6. Explicit solutions (1): separable equations [Notes, p. 3; Robinson, Ch. 8]

$$x'(t) = f\big(x(t)\big)\,g(t), \quad x(t_0) = x_0.$$
If $f \neq 0$ (never), divide by $f$ and integrate from $t_0$ to $t$; with $u = x(\tau)$, $du = x'(\tau)\,d\tau$:
$$\int_{t_0}^{t}\frac{x'(\tau)}{f(x(\tau))}\,d\tau = \int_{x_0}^{x(t)}\frac{du}{f(u)} = \int_{t_0}^{t} g(\tau)\,d\tau.$$
"Never" is guaranteed by Picard: a solution that touches a zero of $f$ is constant. Robinson's proof: $H' = 1/f$, $\frac{d}{dt}H(x(t)) = g(t)$ by the chain rule (Sec. 8.4).

**Example [Notes]:** $x' = kx \Rightarrow x = Ce^{kt}$. (The notes point to Sheet 2, Exercises 4-6, for separable equations.)

**The logistic equation [Notes, p. 3]:** $x' = kx(1 - x/M)$, $x(t_0) = x_0$ (the notes write $x(t_0) = t_0$; $x_0$ is meant).
1. Picard: $x \equiv 0$ or $x \equiv M$, or $x$ never reaches $0$ or $M$; $M - x$ keeps the sign of $M - x_0$.
2. $\displaystyle\int_{x_0}^{x}\frac{dx}{x(1 - x/M)} = k(t - t_0)$.
3. $\frac{1}{x(1 - x/M)} = \frac Ax + \frac{B}{1 - x/M}$: $1 = A(1 - x/M) + Bx$; $x = 0 \Rightarrow A = 1$; $x = M \Rightarrow B = 1/M$. So $\frac1x + \frac{1/M}{1 - x/M} = \frac1x + \frac{1}{M - x}$.
4. $\int_{x_0}^{x}\frac{dx}{x} + \int_{x_0}^{x}\frac{dx}{M - x} = \ln\frac{x}{x_0} + \ln\frac{M - x_0}{M - x} = \ln\frac{x(M - x_0)}{x_0(M - x)}$ (substitution $u = M - x$, $du = -dx$ in the second).
5. $\frac{x}{M - x} = \frac{x_0e^{k(t - t_0)}}{M - x_0} =: E$.
6. $x = ME - xE \Rightarrow x(1 + E) = ME \Rightarrow x = \frac{Mx_0e^{k(t - t_0)}}{M - x_0 + x_0e^{k(t - t_0)}}$.
7. $$x(t) = \frac{Mx_0}{x_0 + (M - x_0)e^{-k(t - t_0)}}, \qquad \lim_{t\to\infty}x(t) = \frac{Mx_0}{x_0 + 0} = M.$$

Checks: $x(t_0) = x_0$; $x_0 = M$ gives $M$; small $x$ gives $x_0e^{k(t - t_0)}$; fastest growth at $x = M/2$. Robinson's $\frac{M}{p(M - p)} = \frac1p + \frac{1}{M - p}$ (Eq. 8.13) is step 3 times $M$.

**Complement (Robinson).** Example 8.1 ($\dot x = x^2$); census fit of the logistic model ($M = 83.1$ million, $k = 0.0141\ \text{yr}^{-1}$, Eq. 8.14); pitchfork solved by partial fractions (Sec. 8.6.1).

## 7. Explicit solutions (2): the integrating factor [Notes, p. 3; Robinson, Ch. 9]

$x' + p(t)x = q(t)$ is not separable in general. Multiply by $I(t)$: $Ix' + Ipx = Iq$. Choose $I$ with $(Ix)' = Ix' + Ipx$; the product rule $(Ix)' = I'x + Ix'$ leaves $I' = Ip$, so $I'/I = p$, $\ln I = \int p\,dt = P(t)$ and
$$I(t) = e^{P(t)} \quad\text{(integrating factor; e.g. } p = t \Rightarrow P = t^2/2).$$
Then $(Ix)' = Iq$, $Ix = \int Iq\,dt$, and $x(t) = \frac{1}{I(t)}\int I(t)q(t)\,dt$ (general solution).

**IVP in three steps [Notes, p. 3]** ($x(t_0) = x_0$, $t > t_0$):
1. $P(t) = \int_{t_0}^{t}p(\tau)\,d\tau$, so $P(t_0) = 0$ and $I(t_0) = e^0 = 1$.
2. $\int_{t_0}^{t}(I(\tau)x(\tau))'\,d\tau = \int_{t_0}^{t}I(\tau)q(\tau)\,d\tau$.
3. $I(t)x(t) - I(t_0)x(t_0) = I(t)x(t) - x_0$, so
$$x(t) = \frac{x_0}{I(t)} + \frac{1}{I(t)}\int_{t_0}^{t} I(\tau)q(\tau)\,d\tau, \qquad I(t) = e^{P(t)}.$$

**Worked example (written for the portal):** $x' + tx = t$, $x(0) = x_0$. $P = t^2/2$, $I = e^{t^2/2}$; $\int_0^t \tau e^{\tau^2/2}d\tau = \int_0^{t^2/2}e^u\,du = e^{t^2/2} - 1$ ($u = \tau^2/2$, $du = \tau\,d\tau$); $x(t) = 1 + (x_0 - 1)e^{-t^2/2}$. Check: $x' + tx = t$; $x \to 1$.

**Complement (Robinson).** Constant coefficients (Eqs. 9.3-9.6); Examples 9.1 ($x = e^{-3t} + t/3 - 1/9$) and 9.2 ($y = 3 + c/(x^2 + 1)^2$); Newton's law of cooling (Eq. 9.9), the time-of-death erratum of p. 81 ($t_0 \approx 6{:}18$ a.m., not 1:42 a.m.), periodic surroundings (Eq. 9.17), cabin ventilation as a stirred tank.

## 8. Explicit solutions (3): exact equations [Notes, p. 4; Robinson, Sec. 10.1]

Let $y = y(x)$ and $F(x, y) = C$. By the chain rule $\frac{\partial F}{\partial x} + \frac{\partial F}{\partial y}\frac{dy}{dx} = 0$, a first-order ODE. So if $f(x, y) + g(x, y)\frac{dy}{dx} = 0$ and $F$ satisfies $F_x = f$, $F_y = g$, the solution is $F(x, y) = C$. Observation: $\frac{\partial f}{\partial y} = \frac{\partial^2F}{\partial y\,\partial x} = \frac{\partial^2F}{\partial x\,\partial y} = \frac{\partial g}{\partial x}$ (Schwarz).

> **Theorem [Notes, p. 4].** Let $f, g, \frac{\partial f}{\partial y}, \frac{\partial g}{\partial x}$ be continuous. Then $f + g\frac{dy}{dx} = 0$ is exact if $\frac{\partial f}{\partial y} = \frac{\partial g}{\partial x}$; the solution is $F(x, y) = C$ with $F_x = f$, $F_y = g$. (Complement, Robinson: on a rectangle or simply connected domain the condition is also necessary, so "if and only if".)

Sufficiency (Robinson, Eqs. 10.6-10.7): $F = \int f\,dx + \varphi(y)$ and $\varphi' = g - \partial_y\int f\,dx$ is free of $x$ because $f_y = g_x$.

**Ex 1 [Notes, p. 4; Robinson Example 10.1]:** $x^3 + \frac yx + (y^2 + \ln x)\frac{dy}{dx} = 0$, $x > 0$. Not linear ($y^2y'$). $f_y = \frac1x = g_x$. $F = \frac{x^4}{4} + y\ln x + \varphi(y)$; $F_y = \ln x + \varphi'(y) = y^2 + \ln x \Rightarrow \varphi = \frac{y^3}{3}$. Implicit solution $F = \frac{x^4}{4} + \frac{y^3}{3} + y\ln x = C$ (left implicit, "since $x$ and $y$ are together"; isolating $y$ would need Cardano's formula for the cubic).

**Ex 2 [Notes, p. 4]:** $(1 + e^xy + xe^xy) + (xe^x + 2)\frac{dy}{dx} = 0$. $f_y = e^x + xe^x$; $g_x = e^x + xe^x$ (product rule). By parts ($u = x$, $dv = e^xdx$): $\int xe^x\,dx = xe^x - e^x$, so $F = x + ye^x + y(xe^x - e^x) + \varphi(y) = x + yxe^x + \varphi(y)$; $F_y = xe^x + \varphi' = xe^x + 2 \Rightarrow \varphi = 2y$.
$$F = x + yxe^x + 2y = C \quad\Longrightarrow\quad y = \frac{C - x}{xe^x + 2}.$$
$xe^x + 2 \ge 2 - 1/e > 0$ (minimum of $xe^x$ at $x = -1$), so $y$ is defined for every $x$. Check: $\frac{d}{dx}[y(xe^x + 2)] = -1$ gives back the ODE. The equation is also linear: in normal form $p = (1 + x)e^x/(xe^x + 2)$, so the integrating factor is $I = xe^x + 2$.

**Complement (Robinson).** Integrating factors $I(x)$ and $I(y)$ for non-exact equations (Eqs. 10.9-10.11, Example 10.2).

## 9. Complement: homogeneous and Bernoulli substitutions [Robinson, Sec. 10.2]

$y' = F(y/x)$ with $y = ux$; $y' + py = qy^n$ with $u = y^{1-n}$ (Example 10.4: $y = 3/(Ce^{-3x^2} - 1)$).

## 10. Choosing a method

| Equation | Test | Method | Notes |
| :--- | :--- | :--- | :--- |
| IVP $y' = f(x, y)$ | $f$, $f_y$ continuous | Picard: unique local solution | p. 3 |
| Autonomous $x' = f(x)$ | no explicit $t$ | stationary points, sign of $f'$ | p. 3 |
| Separable $x' = f(x)g(t)$ | right side factorises | $\int du/f = \int g$ | p. 3 |
| Linear $x' + px = q$ | first powers of $x$, $x'$ | $I = e^{P}$, three steps | p. 3 |
| Exact $f + gy' = 0$ | $f_y = g_x$ | $F_x = f$, $F_y = g$, $F = C$ | p. 4 |

---

## Solved problems (ProblemsCh2.pdf, 17 problems)

Every problem from Sheet 2 is developed in 4 exhaustive phases with zero omitted algebraic steps:

| Problem | Title | Key Method / Theoretical Core | Key Result / Formula |
| :--- | :--- | :--- | :--- |
| **[[04 - Advanced Maths/Problem - Ch2-P1 Direct Integration General Solutions|Problem 2.1]]** | Direct Integration General Solutions | 5 antiderivative calculations ($e^{3x}-x$, $1/x$, $x e^{x^2}$, algebraic fractions) | $y(x) = \frac{1}{3}e^{3x}-\frac{x^2}{2}+C$, $y = \ln|x|+C$, $y = \frac{1}{2}e^{x^2}+C$, etc. |
| **[[04 - Advanced Maths/Problem - Ch2-P2 Separable ODEs and Asymptotic Integrals|Problem 2.2]]** | Separable ODEs & Asymptotic Integrals | Separation of variables, Gaussian integral, finite-time blow-up | Gaussian threshold: blow-up if $y(0) > \frac{2}{\sqrt{\pi}}$ |
| **[[04 - Advanced Maths/Problem - Ch2-P3 Integrating Factor Method and Asymptotics|Problem 2.3]]** | Integrating Factor Method & Asymptotics | 8 linear ODEs solved with $\mu(t)$, hyperbolic functions, cotangent | Part (viii): $x(t) \to \frac{b}{a}$ as $t \to \infty$ |
| **[[04 - Advanced Maths/Problem - Ch2-P4 Exact Differential Equations|Problem 2.4]]** | Exact Differential Equations | 4 exact ODEs, potential reconstruction $F(x, y) = C$ | Closed-form algebraic solutions for all 4 equations |
| **[[04 - Advanced Maths/Problem - Ch2-P5 Integrating Factor for Non-Exact Equations|Problem 2.5]]** | Integrating Factor for Non-Exact Equations | Finding $\mu(x) = x$ via $\frac{1}{N}(M_y - N_x) = \frac{1}{x}$ | Exact potential $x^3 y + \frac{1}{2} x^2 y^2 = C$ |
| **[[04 - Advanced Maths/Problem - Ch2-P6 Exactness of Separated Differential Forms|Problem 2.6]]** | Exactness of Separated Differential Forms | Proof that $f(x) + g(y)y' = 0$ is always exact; 2 applications | $V(x) + y^2 = C$; $\ln y - a y + 2\ln x - bx = C$ |
| **[[04 - Advanced Maths/Problem - Ch2-P7 Nonlinear Change of Variables|Problem 2.7]]** | Nonlinear Change of Variables | Substitution $z = y^2$ for $y' = y + x/y$, $y(0)=1$ | $y(x) = \sqrt{\frac{3}{2}e^{2x} - x - \frac{1}{2}}$ |
| **[[04 - Advanced Maths/Problem - Ch2-P8 General Bernoulli Equation Reduction|Problem 2.8]]** | General Bernoulli Equation Reduction | General reduction $z = y^{1-\alpha}$; study of $\alpha = 0, 1$ | $z' + (1-\alpha)a(x)z = (1-\alpha)b(x)$ |
| **[[04 - Advanced Maths/Problem - Ch2-P9 Solution Uniqueness and Lipschitz Analysis|Problem 2.9]]** | Solution Uniqueness & Lipschitz Analysis | Testing Lipschitz continuity at $x=0$ for 5 powers of $x$ | Non-unique: $x^{1/3}, x^{1/2}(1+x)^2$; Unique: $x(1-x^2), x^3, (1+x)^{3/2}$ |
| **[[04 - Advanced Maths/Problem - Ch2-P10 Uniqueness via Integrating Transformation|Problem 2.10]]** | Uniqueness via Integrating Transformation | Energy transform $z(t) = y(t)\exp(\int p)$ without Picard | $z'(t) \equiv 0 \implies y(t) = y_0 \exp(-\int p)$, trivial if $y_0=0$ |
| **[[04 - Advanced Maths/Problem - Ch2-P11 Invariance of Solution Ratios in Linear ODEs|Problem 2.11]]** | Invariance of Solution Ratios in Linear ODEs | Quotient rule on $\frac{d}{dt}\left(\frac{y_1}{y_2}\right) = 0$ | Proves linear solutions are constant scalar multiples |
| **[[04 - Advanced Maths/Problem - Ch2-P12 Trajectory Crossing and Uniqueness Bounds|Problem 2.12]]** | Trajectory Crossing and Uniqueness Bounds | No-crossing theorem bounds: barrier solutions | (i) $y(t) > -2$; (ii) $-t-1 < y(t) < t^2+1$ $\forall t$ |
| **[[04 - Advanced Maths/Problem - Ch2-P13 Multi-Equilibria Autonomous Phase Line Dynamics|Problem 2.13]]** | Autonomous Phase Line Dynamics | Equilibrium barriers for $y' = y(y-2)(y-3)$ | Trajectory confinement across 4 intervals |
| **[[04 - Advanced Maths/Problem - Ch2-P14 Non-Lipschitz Branching Pathology in Picard Theorem|Problem 2.14]]** | Non-Lipschitz Branching Pathology | Dual solutions $y_1=t^3, y_2=0$ for $y' = 3y^{2/3}$ | $\partial f/\partial y \to \infty$ violates Lipschitz at $y=0$ |
| **[[04 - Advanced Maths/Problem - Ch2-P15 Singular ODE and Domain of Definition|Problem 2.15]]** | Singular ODE and Domain of Definition | $y' = \frac{2y+1}{t}$, multiple solutions at $t=0$ | Domain singularity: $f$ undefined at $t=0$, Picard intact |
| **[[04 - Advanced Maths/Problem - Ch2-P16 Pitchfork Phase Line and Stability Regimes|Problem 2.16]]** | Pitchfork Phase Line & Stability Regimes | $\dot{x} = x(\kappa^2 - x^2)$; 3 equilibria $0, \pm\kappa$ | $x=0$ unstable; $x=\pm\kappa$ asymptotically stable attractors |
| **[[04 - Advanced Maths/Problem - Ch2-P17 Direct Difference Method for Uniqueness|Problem 2.17]]** | Direct Difference Method for Uniqueness | Inspection solution + difference $w = y_1 - y_2$ energy | $w(t) \equiv 0 \implies y_1(t) = y_2(t)$, unconditional uniqueness |

---

## Further worked examples, one per method (verified)

Complement (Robinson). Examples B to F come from Robinson's book (Book ODE's; the printed page is cited, the PDF page is printed page plus 16). Example A is an **illustrative example**. Every closed form was checked with sympy (residual 0 in the ODE and the initial datum) and with an RK4 integration in pure Python.

### Example A (illustrative example) — Separable: $y' = x\,e^{-y}$, $y(0)=0$
Here $g(x)=x$, $h(y)=e^{-y}>0$, so there are no equilibria and the division is legitimate. Multiply by $e^{y}$ and use the chain rule $\frac{d}{dx}e^{y(x)} = e^{y(x)}\,y'(x)$:
$$ \frac{d}{dx}\left[e^{y(x)}\right] = x \;\Longrightarrow\; \int_{0}^{y(x)} e^{u}\,du = \int_0^x s\,ds \;\Longrightarrow\; \left[e^{u}\right]_{0}^{y(x)} = \left[\frac{s^2}{2}\right]_0^x $$
$$ e^{y} - 1 = \frac{x^2}{2} \;\Longrightarrow\; \boxed{y(x) = \ln\left(1 + \frac{x^2}{2}\right)}, \quad x \in \mathbb{R}\ \text{(the argument is at least 1).} $$

### Example B — Linear, integrating factor: $x' + 3x = t$, $x(0) = 8/9$ (Book, Example 9.1, p. 78)
With $p(t)=3$: $\mu(t) = \exp\left(\int_0^t 3\,ds\right) = e^{3t}$, $\mu(0)=1$. By the product rule $\frac{d}{dt}\left[x e^{3t}\right] = e^{3t}x' + 3e^{3t}x = t e^{3t}$. Integrate over $[0,t]$ (Barrow), with $\int s e^{3s}ds = \frac{s e^{3s}}{3} - \frac{e^{3s}}{9}$ (by parts, $u=s$, $dv = e^{3s}ds$):
$$ x(t)e^{3t} - x(0) = \left[\frac{s e^{3s}}{3} - \frac{e^{3s}}{9}\right]_{0}^{t} = \frac{t e^{3t}}{3} - \frac{e^{3t}}{9} + \frac{1}{9} $$
Using $x(0)=\frac{8}{9}$: $x e^{3t} = \frac{t e^{3t}}{3} - \frac{e^{3t}}{9} + 1$, so $\boxed{x(t) = e^{-3t} + \frac{t}{3} - \frac{1}{9}}$, global on $\mathbb{R}$ (the coefficients are continuous). The term $e^{-3t}$ is the transient and $\frac{t}{3}-\frac{1}{9}$ the forced response.

### Example C — Exact: $\left(x^3 + \frac{y}{x}\right) + \left(y^2 + \ln x\right)y' = 0$, $x>0$ (Book, Example 10.1, p. 91)
$M = x^3 + \frac{y}{x}$, $N = y^2 + \ln x$. **Exactness check:** $\frac{\partial M}{\partial y} = \frac{1}{x} = \frac{\partial N}{\partial x}$ on the simply connected domain $x>0$. **Potential:** $F = \int M\,dx = \frac{x^4}{4} + y\ln x + C(y)$; then $F_y = \ln x + C'(y) = N = y^2 + \ln x \Rightarrow C'(y)=y^2 \Rightarrow C(y) = \frac{y^3}{3}$. Solution (implicit; it cannot be solved for $y$):
$$ \boxed{F(x,y) = \frac{x^4}{4} + y\ln x + \frac{y^3}{3} = c} $$
Check: $dF = \left(x^3 + \frac{y}{x}\right)dx + \left(\ln x + y^2\right)dy$. With $y(1)=1$: $c = \frac14 + 0 + \frac13 = \frac{7}{12}$.

### Example D — Bernoulli: $y' - 6xy = 2xy^2$, $y(0) = \frac12$ (Book, Example 10.4, p. 96, with an added initial datum)
Here $\alpha = 2$, $a=6x$, $b=2x$. The equilibrium $y\equiv 0$ is lost on dividing by $y^2$ and must be listed apart. Divide by $y^2$ and set $u = y^{1-\alpha} = y^{-1}$, so by the chain rule $u' = -y^{-2}y'$:
$$ y^{-2}y' - 6x\,y^{-1} = 2x \;\Longrightarrow\; -u' - 6xu = 2x \;\Longrightarrow\; u' + 6x\,u = -2x, \quad u(0)=2. $$
Integrating factor $\mu(x) = \exp\left(\int_0^x 6s\,ds\right) = e^{3x^2}$, so $\frac{d}{dx}\left[u e^{3x^2}\right] = -2x e^{3x^2}$. Barrow with $w = 3s^2$, $dw = 6s\,ds$ (so $2s\,ds = \frac{dw}{3}$, limits $0 \to 3x^2$):
$$ u e^{3x^2} - 2 = -\frac13\int_0^{3x^2} e^{w}\,dw = -\frac13\left(e^{3x^2} - 1\right) \;\Longrightarrow\; u = \frac{7}{3}e^{-3x^2} - \frac13 $$
$$ \boxed{y(x) = \frac{3}{7e^{-3x^2} - 1}} $$
The denominator vanishes at $e^{-3x^2} = \frac17$, i.e. $x_* = \pm\sqrt{\frac{\ln 7}{3}} \approx \pm 0.805$, so the maximal interval is $(-x_*, x_*)$.

### Example E — Autonomous phase line: $p' = kp\left(1 - \frac pM\right)$, $k, M > 0$ (Book, Section 7.5.1, p. 51)
Equilibria: $f(p)=0 \iff p = 0$ or $p = M$. Sign of $f$: $f<0$ on $(-\infty,0)$, $f>0$ on $(0,M)$, $f<0$ on $(M,\infty)$. Since $p$ increases where $f>0$ and decreases where $f<0$: the flow leaves $0$ on both sides (unstable) and enters $M$ from both sides (stable). Analytic confirmation: $f'(p) = k - \frac{2kp}{M}$, $f'(0) = k > 0$ (unstable), $f'(M) = -k < 0$ (stable). If $f'(p^*)=0$ the test is inconclusive and the sign of $f$ decides (for $x' = x^2$ the origin is semistable).

### Example F — Finite-time blow-up: $x' = x^2$, $x(0) = x_0 > 0$ (Book, Example 8.1, p. 60; Section 6.3, pp. 41-42)
$f = x^2$ and $f_x = 2x$ are continuous, so a unique local solution exists. Separate and apply Barrow:
$$ \int_{x_0}^{x(t)} \frac{du}{u^2} = \int_0^t ds \;\Longrightarrow\; -\frac{1}{x(t)} + \frac{1}{x_0} = t \;\Longrightarrow\; \boxed{x(t) = \frac{1}{x_0^{-1} - t}} $$
The denominator vanishes at $T = x_0^{-1}$; equivalently $T = \int_{x_0}^{\infty} \frac{du}{u^2} = \frac{1}{x_0}$ (time to reach infinity). For $t\to T^-$, $x\to +\infty$. For $t \to -\infty$, $x \to 0^+$, so the **maximal interval of existence** is $(-\infty, x_0^{-1})$. For $x_0<0$ it is $(x_0^{-1}, +\infty)$ and only $x_0 = 0$ gives a solution on all of $\mathbb{R}$.

**Verification record (one line per example):** sympy residual 0 and RK4 (2000 steps) vs closed form: A $y(2)=1.0986122887$ vs $\ln 3$; B $x(2)$ differs by $1.5\times10^{-14}$; C $F(1.5, y_{RK4})=0.58333333$ vs $c=7/12$; D $y(0.5)=1.30063487$ vs $1.30063487$; E $p(20)=2.0000000$ from $p_0=0.5$ and $p_0=3$ ($k=1$, $M=2$); F $x(0.49)=100.0000$ vs $1/(0.5-0.49)=100$ ($x_0=2$).

---

## Interdisciplinary aerospace connections
* **Aerospace Propulsion & Combustion:** The Gaussian integral and blow-up threshold analyzed in Problem 2.2 model thermal runaway in adiabatic chemical reactors and rocket engine pre-burners.
* **Flight Mechanics & Aerodynamic Stability:** The autonomous phase line dynamics and pitchfork bifurcation studied in Problem 2.16 govern roll-coupling stability and angle-of-attack trim states in transonic flight.

---

## Navigation
* **Upward Navigation:** [[04 - Advanced Maths/Advanced Maths MOC|Advanced Mathematics MOC]]
* **Previous Unit:** [[04 - Advanced Maths/Topic 1 - Introduction, Modeling and Classification of ODEs|Tema 1: Introduction, Modeling and Classification]]
* **Root Index:** [[00 - Indice Central/Master Index|Central Master Index]]
