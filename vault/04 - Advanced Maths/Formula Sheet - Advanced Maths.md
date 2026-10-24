---
materia: "Advanced Maths"
tema: "Formula sheet and solving compendium, Units 1 to 6"
tags:
  - formulario
  - prontuario
  - repaso-rapido
  - matematicas-avanzadas
fuentes:
  - "sources/cuatrimestre-1/04-advanced-maths/teoria/Notes.pdf"
  - "Robinson, An Introduction to Ordinary Differential Equations (2004)"
web: "subjects/advanced-maths/formula-sheet/index.html"
---

# Formula Sheet - Advanced Maths

Every key formula of the course with its short derivation, the reason for each step, its hypotheses and the recipe to use it in an exam. Units 1 to 4 follow the class notes (`Notes.pdf`) and the theory pages built from them: [[Topic 1 - Introduction, Modeling and Classification of ODEs]], [[Topic 2 - First-Order ODEs and Qualitative Dynamics]], [[Topic 3 - Second-Order Linear ODEs General Theory and Constant Coefficients]] and [[Topic 4 - Systems of Linear ODEs and Phase Portraits]]. The last block (Units 5 and 6) has no class notes in the repository yet: its formulas are the standard results used in the solved [[Problem Set - Advanced Maths Problem Bank|Extra problems]] P08 to P22 and are marked as extension.

The page `subjects/advanced-maths/formula-sheet/index.html` is generated from this note by `python tools/build_formula_sheet.py`; edit this note, never the page. Card headings are `### <Kind>: <title>`; a derivation card opens with an `In short:` line, which is all the compact view shows; tables headed `| Step | Why |` become the step grid with the reason beside each line.

## Unit 1 — Modelling and classification
Pages: Theory=teoria/topic-1.html; Problems=problemas/topic-1-problems.html

### Pattern: Order, linearity and autonomy in five seconds
- **Order** = highest derivative that appears. **ODE**: one independent variable $t$; **PDE**: partial derivatives in two or more.
- **Linear** of order $n$: $a_n(t)x^{(n)} + \dots + a_1(t)\dot x + a_0(t)x = f(t)$. The unknown and its derivatives appear only to the first power, never multiplied together, never inside $\sin$, $e^{(\cdot)}$, $\sqrt{\ }$. The coefficients may depend on $t$ in any way.
- **Homogeneous** if $f \equiv 0$. **Autonomous** if $t$ does not appear explicitly: $\dot x = f(x)$.
- Nonlinear red flags: $x\dot x$, $(\dot x)^2$, $x^2$, $\sin x$, $e^{x}$, $1/x$.

### Theorem: The superposition test
In short: an equation is linear and homogeneous exactly when any combination of two solutions is again a solution.
Write the equation as $L[x] = 0$. It is linear when $L[\alpha x_1 + \beta x_2] = \alpha L[x_1] + \beta L[x_2]$ for all constants $\alpha, \beta$.

| Step | Why |
| --- | --- |
| $L[x] = \ddot x + p(t)\dot x + q(t)x$ | the general homogeneous linear operator of order 2 |
| $L[\alpha x_1 + \beta x_2] = \alpha(\ddot x_1 + p\dot x_1 + qx_1) + \beta(\ddot x_2 + p\dot x_2 + qx_2)$ | the derivative of a sum is the sum of derivatives, constants come out |
| $= \alpha\cdot 0 + \beta\cdot 0 = 0$ | each bracket vanishes because $x_1$, $x_2$ are solutions |

To prove an equation is **not** linear, one counterexample is enough: for $\ddot u = (\dot u)^2 + 1$, the square of $\dot u_1 + \dot u_2$ produces the cross term $2\dot u_1\dot u_2$, which does not cancel.

### Table: The models of the course
| Model | Equation | Solution |
| --- | --- | --- |
| Growth / decay | $\dot N = kN$ | $N = N_0e^{kt}$; half-life $t_{1/2} = \ln 2/\lvert k\rvert$ |
| Logistic | $\dot N = rN(1 - N/K)$ | $N = \dfrac{KN_0}{N_0 + (K - N_0)e^{-rt}}$ |
| Newton cooling | $\dot T = -k(T - T_a)$ | $T = T_a + (T_0 - T_a)e^{-kt}$ |
| Mixing tank | $\dot Q = r_{in}c_{in} - r_{out}\,Q/V(t)$ | linear, integrating factor |
| Free fall | $m\ddot x = -mg$ | $x = x_0 + v_0t - \tfrac12gt^2$ |
| Pendulum | $\ddot\theta + (g/l)\sin\theta = 0$ | small angles, from rest: $\theta = \theta_0\cos\sqrt{g/l}\,t$ |

### Derivation: Newton's law of cooling
In short: shift the unknown by the room temperature, $u = T - T_a$, and the equation becomes pure decay $\dot u = -ku$.

| Step | Why |
| --- | --- |
| $u = T - T_a \Rightarrow \dot u = \dot T$ | $T_a$ is constant, its derivative is zero |
| $\dot u = -ku \Rightarrow u = u_0e^{-kt}$ | the decay law, solved by separation |
| $T(t) = T_a + (T_0 - T_a)e^{-kt}$ | undo the shift, $u_0 = T_0 - T_a$ |
| $k = \dfrac1{t_1}\ln\dfrac{T_0 - T_a}{T_1 - T_a}$ | one extra reading $T(t_1) = T_1$ fixes $k$ (time-of-death problems) |

Units: $[k] = \mathrm{s^{-1}}$, so $kt$ is dimensionless, as the exponent must be.

### Algorithm: Building a model
1. Name the unknown, its unit and the independent variable.
2. Write the balance: rate of change = rate in − rate out (mass, salt, population) or $m\ddot x = \sum F$ (mechanics).
3. For a tank write the volume first: $V(t) = V_0 + (r_{in} - r_{out})t$; concentration $= Q/V$.
4. Classify the equation (order, linear, autonomous) and pick the method from Unit 2 or 3.
5. Check units term by term and the limits $t \to 0$, $t \to \infty$.

### Trap: Typical modelling slips
- Using $V_0$ instead of $V(t)$ when inflow and outflow rates differ.
- Forgetting that $\dot N = kN$ grows for $k > 0$ and decays for $k < 0$: read the sign from the physics.
- Linearising $\sin\theta \approx \theta$ outside small angles.

## Unit 2 — First-order ODEs
Pages: Theory=teoria/topic-2.html; Problems=problemas/topic-2-problems.html

### Theorem: Picard: existence and uniqueness
In short: if $f$ and $\partial f/\partial x$ are continuous around $(t_0, x_0)$, the IVP $\dot x = f(t,x)$, $x(t_0) = x_0$ has exactly one solution near $t_0$.
- **Hypotheses:** $f$ continuous and $\partial f/\partial x$ continuous on a rectangle containing $(t_0, x_0)$; enough is Lipschitz in $x$: $\lvert f(t,x) - f(t,y)\rvert \le L\lvert x - y\rvert$.
- **Conclusion:** a unique solution on some interval $(t_0 - h, t_0 + h)$; it depends continuously on $x_0$.
- **Consequence:** two solution curves never cross, and a non-equilibrium solution never reaches an equilibrium in finite time.

### Trap: When Picard fails or stops short
| Equation | What goes wrong |
| --- | --- |
| $\dot x = \sqrt{x}$, $x(0) = 0$ | $\partial f/\partial x = 1/(2\sqrt x)$ blows up at $0$: both $x \equiv 0$ and $x = t^2/4$ solve it (no uniqueness) |
| $\dot x = x^2$, $x(0) = x_0 > 0$ | $x = \dfrac{1}{1/x_0 - t}$ blows up at $t = 1/x_0$: the theorem is only local |
| $\dot x = f(t,x)$ with $f$ discontinuous | existence itself may fail |

Uniqueness check in an exam: compute $\partial f/\partial x$ and find where it is not continuous; outside those points the solution is unique.

### Pattern: Autonomous equations and the phase line
$\dot x = f(x)$. Equilibria: $f(x^*) = 0$. Draw the $x$-axis, mark the zeros of $f$, and put an arrow to the right where $f > 0$ and to the left where $f < 0$.
- **Stable** (sink): arrows point in on both sides; $f'(x^*) < 0$.
- **Unstable** (source): arrows point out; $f'(x^*) > 0$.
- **Semi-stable**: same sign of $f$ on both sides; $f'(x^*) = 0$ and $f$ does not change sign.
- If $f'(x^*) = 0$, the derivative test is silent: read the sign of $f$ on each side.

### Derivation: Stability from the linearisation
In short: near $x^*$, $\dot\xi \approx f'(x^*)\xi$ for $\xi = x - x^*$, so small perturbations behave like $e^{f'(x^*)t}$.

| Step | Why |
| --- | --- |
| $x = x^* + \xi \Rightarrow \dot x = \dot\xi$ | $x^*$ is constant |
| $f(x^* + \xi) = f(x^*) + f'(x^*)\xi + O(\xi^2)$ | Taylor expansion of $f$ around $x^*$ |
| $\dot\xi \approx f'(x^*)\xi$ | $f(x^*) = 0$ at an equilibrium; drop $O(\xi^2)$ for small $\xi$ |
| $\xi(t) \approx \xi_0e^{f'(x^*)t}$ | decays if $f'(x^*) < 0$, grows if $f'(x^*) > 0$ |

### Table: Bifurcations of the notes
| Normal form | What happens at $r = 0$ |
| --- | --- |
| $\dot x = r + x^2$ (saddle-node) | two equilibria $\pm\sqrt{-r}$ for $r < 0$ merge and vanish |
| $\dot x = rx - x^2$ (transcritical) | $0$ and $r$ exchange stability |
| $\dot x = rx - x^3$ (pitchfork) | $0$ stable for $r < 0$; for $r > 0$, $0$ unstable and $\pm\sqrt r$ stable |

### Derivation: Separable equations
In short: divide by $h(x)$, recognise the chain rule on the left and integrate both sides: $\int dx/h(x) = \int g(t)\,dt$.
Form: $\dot x = g(t)\,h(x)$ (the right-hand side factors into a function of $t$ times a function of $x$).

| Step | Why |
| --- | --- |
| $\dfrac{1}{h(x)}\dfrac{dx}{dt} = g(t)$ | divide where $h(x) \neq 0$; the zeros of $h$ are kept apart |
| $H(x) = \int\dfrac{dx}{h(x)} \Rightarrow \dfrac{d}{dt}H(x(t)) = H'(x)\,\dot x = \dfrac{\dot x}{h(x)}$ | chain rule: this is what makes "separating $dx$ and $dt$" legitimate |
| $\dfrac{d}{dt}H(x(t)) = g(t) \Rightarrow H(x(t)) = \int g(t)\,dt + C$ | integrate both sides in $t$ |
| $H(x) - H(x_0) = \int_{t_0}^{t}g(s)\,ds$ | with the initial condition, by Barrow's rule $[F]_{a}^{b} = F(b) - F(a)$ |

### Derivation: The logistic equation solved
In short: separate, split $1/(N(K - N))$ by partial fractions, integrate to logarithms and solve for $N$.

| Step | Why |
| --- | --- |
| $\dfrac{K\,dN}{N(K - N)} = r\,dt$ | separation of $\dot N = rN(K - N)/K$ |
| $\dfrac{K}{N(K - N)} = \dfrac1N + \dfrac{1}{K - N}$ | partial fractions: $K = (K - N) + N$ |
| $\ln\lvert N\rvert - \ln\lvert K - N\rvert = rt + c$ | $\int\frac{dN}{K - N} = -\ln\lvert K - N\rvert$ (inner derivative $-1$) |
| $\dfrac{N}{K - N} = Ae^{rt},\ A = \dfrac{N_0}{K - N_0}$ | exponentiate; $\pm e^c$ and the initial value fix $A$ |
| $N(t) = \dfrac{KN_0}{N_0 + (K - N_0)e^{-rt}}$ | solve for $N$, multiply top and bottom by $e^{-rt}$ |

Limits: $N \to K$ as $t \to \infty$ for any $N_0 > 0$; $N \equiv 0$ and $N \equiv K$ are the equilibria lost when dividing.

### Derivation: The integrating factor
In short: multiply $\dot x + p(t)x = q(t)$ by $\mu = e^{\int p\,dt}$, so the left side becomes $(\mu x)'$; integrate.

| Step | Why |
| --- | --- |
| $\mu\dot x + \mu p\,x = \mu q$ | multiply by an unknown positive function $\mu(t)$ |
| want $\mu\dot x + \mu p\,x = (\mu x)' = \mu\dot x + \dot\mu x$ | product rule backwards: the left side should be one derivative |
| $\dot\mu = p\mu \Rightarrow \mu(t) = e^{\int p(t)\,dt}$ | compare the two left sides; a separable equation for $\mu$ (no constant needed) |
| $(\mu x)' = \mu q \Rightarrow \mu x = \int\mu q\,dt + C$ | integrate both sides |
| $x(t) = e^{-P(t)}\Big[x_0 + \int_{t_0}^{t}e^{P(s)}q(s)\,ds\Big]$ | with $P(t) = \int_{t_0}^{t}p(s)\,ds$, so $P(t_0) = 0$ and Barrow gives $x(t_0) = x_0$ |

### Algorithm: Linear first-order IVP in three steps
1. Put it in standard form $\dot x + p(t)x = q(t)$: divide by the coefficient of $\dot x$ (note where it vanishes: the solution lives on an interval without those points).
2. $\mu = e^{\int p\,dt}$; check $\dot\mu = p\mu$.
3. $x = \frac1\mu\big(\int\mu q\,dt + C\big)$; impose $x(t_0) = x_0$ last.

### Derivation: Exact equations
In short: if $M\,dx + N\,dy = 0$ has $M_y = N_x$, there is $F(x,y)$ with $F_x = M$, $F_y = N$, and the solutions are the level curves $F(x,y) = C$.

| Step | Why |
| --- | --- |
| $\dfrac{d}{dx}F(x, y(x)) = F_x + F_y\,y'$ | chain rule along a solution curve $y(x)$ |
| $= M + N\,y' = 0$ | this is the equation itself, so $F$ is constant on solutions |
| $F_{xy} = F_{yx} \Rightarrow M_y = N_x$ | equality of mixed partials (Schwarz): the exactness test |
| $F = \int M\,dx + g(y)$ | integrate $F_x = M$ in $x$; the "constant" may depend on $y$ |
| $F_y = N \Rightarrow g'(y) = N - \partial_y\!\int M\,dx$ | the right side must depend on $y$ only (a check of the work) |

### Derivation: Integrating factor for a non-exact equation
In short: look for $\mu(x)$ with $(\mu M)_y = (\mu N)_x$; it exists when $(M_y - N_x)/N$ depends on $x$ only.

| Step | Why |
| --- | --- |
| $(\mu M)_y = (\mu N)_x$ | the new equation $\mu M\,dx + \mu N\,dy = 0$ must be exact |
| $\mu M_y = \mu' N + \mu N_x$ | $\mu = \mu(x)$: no $y$-derivative of $\mu$; product rule in $x$ |
| $\dfrac{\mu'}{\mu} = \dfrac{M_y - N_x}{N}$ | rearrange; must be a function of $x$ alone |
| $\mu(x) = \exp\!\int\dfrac{M_y - N_x}{N}\,dx$ | integrate $(\ln\mu)' $ |
| $\mu(y) = \exp\!\int\dfrac{N_x - M_y}{M}\,dy$ | the same argument with $\mu = \mu(y)$ |

### Derivation: Substitutions: homogeneous and Bernoulli
In short: $y = vx$ turns $y' = F(y/x)$ into a separable equation; $v = y^{1-n}$ turns Bernoulli into a linear one.

| Step | Why |
| --- | --- |
| $y = vx \Rightarrow y' = v + xv'$ | product rule |
| $v + xv' = F(v) \Rightarrow \dfrac{dv}{F(v) - v} = \dfrac{dx}{x}$ | separable in $v$ and $x$ |
| $y' + p(x)y = q(x)y^n,\ n \ne 0, 1$ | Bernoulli form |
| $v = y^{1-n} \Rightarrow v' = (1 - n)y^{-n}y'$ | chain rule |
| $v' + (1 - n)p\,v = (1 - n)q$ | multiply Bernoulli by $(1 - n)y^{-n}$: linear in $v$ |

### Algorithm: Choosing the method
1. Autonomous? Phase line first (equilibria, stability), then solve if asked.
2. Can the right side be written $g(t)h(x)$? Separable.
3. Linear in $x$: $\dot x + p(t)x = q(t)$? Integrating factor.
4. Written as $M\,dx + N\,dy = 0$: test $M_y = N_x$; if not, try $\mu(x)$ or $\mu(y)$.
5. $y' = F(y/x)$: $y = vx$. A power $y^n$ on the right of a linear equation: Bernoulli.
6. Always add back the constant solutions removed by a division.

### Trap: Lost and singular solutions
- Dividing by $h(x)$ removes the equilibria $h(x^*) = 0$: check whether they are solutions and whether the general formula recovers them for some constant.
- Writing $\ln\lvert x\rvert = \dots$ then $x = Ce^{\dots}$: $C = \pm e^{c}$ can take any sign, and $C = 0$ recovers $x \equiv 0$.
- Domain: a solution through $(t_0, x_0)$ lives on the largest interval containing $t_0$ where the formula is defined (look for zero denominators and logs of zero).

## Unit 3 — Second-order linear ODEs and vibrations
Pages: Theory=teoria/topic-3.html; Problems I=problemas/topic-3-problems.html; Problems II=problemas/topic-3-part-2.html

### Theorem: Existence, uniqueness and the general solution
$\ddot x + p(t)\dot x + q(t)x = f(t)$ with $p, q, f$ continuous on an interval $I$, $t_0 \in I$: for any $x(t_0) = x_0$, $\dot x(t_0) = v_0$ there is exactly one solution, and it exists on all of $I$ (linear equations do not blow up inside $I$).
- Two conditions are needed because the equation fixes $\ddot x$ once $x$ and $\dot x$ are known.
- If $x_1, x_2$ solve the homogeneous equation and $W(x_1, x_2) \neq 0$, every solution is $x = C_1x_1 + C_2x_2$; the constants come from

$$\begin{pmatrix} x_1(t_0) & x_2(t_0) \\ \dot x_1(t_0) & \dot x_2(t_0)\end{pmatrix}\begin{pmatrix} C_1 \\ C_2\end{pmatrix} = \begin{pmatrix} x_0 \\ v_0\end{pmatrix},$$

solvable for every datum exactly when the determinant $W(t_0) \neq 0$.

### Derivation: The Wronskian and Abel's identity
In short: differentiate $W = x_1\dot x_2 - x_2\dot x_1$, use the equation to remove $\ddot x_1$, $\ddot x_2$, and get $\dot W = -pW$.

| Step | Why |
| --- | --- |
| $\dot W = (\dot x_1\dot x_2 + x_1\ddot x_2) - (\dot x_2\dot x_1 + x_2\ddot x_1)$ | product rule on each term |
| $= x_1\ddot x_2 - x_2\ddot x_1$ | the $\dot x_1\dot x_2$ terms cancel |
| $= x_1(-p\dot x_2 - qx_2) - x_2(-p\dot x_1 - qx_1)$ | each $x_i$ solves $\ddot x = -p\dot x - qx$ |
| $= -p\,(x_1\dot x_2 - x_2\dot x_1) = -p\,W$ | the $q$ terms cancel |
| $W(t) = W(t_0)\exp\!\Big(-\int_{t_0}^{t}p(s)\,ds\Big)$ | linear first-order equation for $W$ (separable) |

**Dichotomy:** the exponential never vanishes, so for two solutions $W \equiv 0$ on $I$ or $W \neq 0$ everywhere on $I$.

### Trap: The Wronskian of functions that are not solutions
$W \equiv 0$ implies dependence only for solutions of one linear equation. Counterexample (Peano): $x_1 = t^2$, $x_2 = t\lvert t\rvert$ have $W \equiv 0$ but are independent on $(-1, 1)$; they cannot both solve a second-order linear equation with continuous coefficients there. Conversely, $W(t_0) \neq 0$ at one point always proves independence.

### Derivation: Constant coefficients: the characteristic equation
In short: try $x = e^{kt}$; every derivative brings out a factor $k$, so $e^{kt}$ solves $\ddot x + p\dot x + qx = 0$ exactly when $k^2 + pk + q = 0$.

| Step | Why |
| --- | --- |
| $(e^{kt})' = ke^{kt},\ (e^{kt})'' = k^2e^{kt}$ | chain rule on $e^{kt}$ |
| $(k^2 + pk + q)\,e^{kt} = 0$ | substitute; $e^{kt}$ is a common factor |
| $k^2 + pk + q = 0,\ k = \dfrac{-p \pm \sqrt{p^2 - 4q}}{2}$ | $e^{kt} \neq 0$ never, so the bracket must vanish |

### Table: The three cases
| Roots | Condition | Fundamental pair |
| --- | --- | --- |
| real $k_1 \neq k_2$ | $p^2 > 4q$ | $e^{k_1t},\ e^{k_2t}$ |
| double $k = -p/2$ | $p^2 = 4q$ | $e^{kt},\ t\,e^{kt}$ |
| $\rho \pm \omega i$ | $p^2 < 4q$ | $e^{\rho t}\cos\omega t,\ e^{\rho t}\sin\omega t$ |

With $\rho = -p/2$ and $\omega = \sqrt{4q - p^2}/2$. Higher order: a root of multiplicity $m$ gives $e^{kt}, te^{kt}, \dots, t^{m-1}e^{kt}$.

### Derivation: Why $te^{kt}$ for a double root
In short: substituting $te^{kt}$ leaves $[(k^2 + pk + q)t + (2k + p)]e^{kt}$, and both brackets vanish at a double root.

| Step | Why |
| --- | --- |
| $(te^{kt})' = (1 + kt)e^{kt}$ | product rule |
| $(te^{kt})'' = (2k + k^2t)e^{kt}$ | product rule again |
| $L[te^{kt}] = \big[(k^2 + pk + q)t + (2k + p)\big]e^{kt}$ | collect powers of $t$ |
| $k^2 + pk + q = 0$ and $2k + p = 0$ | a double root of $P(k)$ is also a root of $P'(k) = 2k + p$ |

### Derivation: Real solutions from complex roots
In short: Euler's formula splits $e^{(\rho + \omega i)t}$ into $e^{\rho t}(\cos\omega t + i\sin\omega t)$; real and imaginary parts are real solutions.

| Step | Why |
| --- | --- |
| $e^{(\rho \pm \omega i)t} = e^{\rho t}(\cos\omega t \pm i\sin\omega t)$ | Euler: $e^{i\theta} = \cos\theta + i\sin\theta$; $\cos$ is even, $\sin$ odd |
| $\tfrac12(x_+ + x_-) = e^{\rho t}\cos\omega t$ | superposition with $C_1 = C_2 = \tfrac12$ |
| $\tfrac{1}{2i}(x_+ - x_-) = e^{\rho t}\sin\omega t$ | superposition with $C_{1,2} = \pm\tfrac1{2i}$ |
| $x = e^{\rho t}(A\cos\omega t + B\sin\omega t)$ | general real solution, $A, B$ real |

### Derivation: Amplitude and phase
In short: $A\cos\omega t + B\sin\omega t = M\cos(\omega t - \phi)$ with $M = \sqrt{A^2 + B^2}$, $\cos\phi = A/M$, $\sin\phi = B/M$.

| Step | Why |
| --- | --- |
| $M\cos(\omega t - \phi) = M\cos\phi\cos\omega t + M\sin\phi\sin\omega t$ | $\cos(a - b) = \cos a\cos b + \sin a\sin b$ |
| $A = M\cos\phi,\ B = M\sin\phi$ | match the coefficients of $\cos\omega t$ and $\sin\omega t$ |
| $M^2 = A^2 + B^2$ | square and add, $\cos^2 + \sin^2 = 1$ |

**Trap:** $\tan\phi = B/A$ alone loses the quadrant; read it from the signs of $\cos\phi = A/M$ and $\sin\phi = B/M$.

### Table: Mass-spring-damper $\ddot x + \lambda\dot x + \omega^2x = 0$
$\lambda = \mu/m$ (damping per unit mass), $\omega^2 = k/m$ (natural frequency squared). Roots $-\lambda/2 \pm \sqrt{\lambda^2/4 - \omega^2}$.

| Regime | Condition | Motion |
| --- | --- | --- |
| undamped | $\lambda = 0$ | $M\cos(\omega t - \phi)$, period $2\pi/\omega$ |
| underdamped | $\lambda < 2\omega$ | $Me^{-\lambda t/2}\cos(\sigma t - \phi)$, $\sigma = \sqrt{\omega^2 - \lambda^2/4}$ |
| critical | $\lambda = 2\omega$ | $(A + Bt)e^{-\lambda t/2}$: fastest return without oscillation |
| overdamped | $\lambda > 2\omega$ | $Ae^{k_1t} + Be^{k_2t}$, $k_{1,2} < 0$ |

$\sigma < \omega$: damping slows the oscillation; the envelope $\pm Me^{-\lambda t/2}$ bounds it. Over- and critical damping cross zero at most once.

### Derivation: Structure of the inhomogeneous solution
In short: the difference of two solutions of $L[x] = f$ solves $L[x] = 0$, so $x = x_H + x_N$.

| Step | Why |
| --- | --- |
| $L[x - x_N] = L[x] - L[x_N] = f - f = 0$ | linearity of $L$ |
| $x - x_N = C_1x_1 + C_2x_2$ | general solution of the homogeneous equation |
| $x = C_1x_1 + C_2x_2 + x_N$ | impose the initial conditions on this sum, never on $x_H$ alone |

### Table: The educated guess (undetermined coefficients)
| Forcing $f(t)$ | Try $x_N$ |
| --- | --- |
| polynomial of degree $n$ | general polynomial of degree $n$ |
| $ae^{\alpha t}$ | $Ce^{\alpha t}$ |
| $a\cos\alpha t$ or $a\sin\alpha t$ | $C\cos\alpha t + D\sin\alpha t$ |
| $P_n(t)e^{\alpha t}\cos\beta t$ | $e^{\alpha t}\big(Q_n(t)\cos\beta t + R_n(t)\sin\beta t\big)$ |
| sum $f_1 + f_2$ | sum of the two guesses (superposition) |

**Resonance rule:** if the exponent of the forcing ($\alpha$, $i\alpha$ or $\alpha + i\beta$) is a root of the characteristic equation of multiplicity $s$, multiply the guess by $t^s$. Example of the notes: $\ddot x + \dot x - 6x = 5e^{-3t}$ with $k = -3$ a simple root gives $x_N = Cte^{-3t}$, $C = -1$.

### Derivation: Undamped resonance
In short: for $\ddot x + \omega^2x = a\cos\omega t$ the guess $t(C\cos\omega t + D\sin\omega t)$ gives $x_N = \dfrac{a}{2\omega}t\sin\omega t$, an amplitude growing linearly.

| Step | Why |
| --- | --- |
| $x_N = t\,g(t),\ g = C\cos\omega t + D\sin\omega t$ | $i\omega$ is a simple root of $k^2 + \omega^2$: multiply by $t$ |
| $\ddot x_N = 2\dot g + t\ddot g = 2\dot g - \omega^2tg$ | product rule twice; $\ddot g = -\omega^2g$ |
| $\ddot x_N + \omega^2x_N = 2\dot g = 2\omega(D\cos\omega t - C\sin\omega t)$ | the $t$ terms cancel |
| $C = 0,\ D = \dfrac{a}{2\omega}$ | match with $a\cos\omega t$ |

Off resonance ($\alpha \neq \omega$): $x_N = \dfrac{a\cos\alpha t}{\omega^2 - \alpha^2}$. Starting from rest, $x = \dfrac{2a}{\omega^2 - \alpha^2}\sin\dfrac{(\omega - \alpha)t}{2}\sin\dfrac{(\omega + \alpha)t}{2}$: **beats**, a fast oscillation inside a slow envelope.

### Derivation: Damped forced response
In short: $\ddot x + \lambda\dot x + \omega^2x = a\cos\alpha t$ has the steady state $R\cos(\alpha t - \delta)$ with $R = a/\sqrt{(\omega^2 - \alpha^2)^2 + \lambda^2\alpha^2}$.

| Step | Why |
| --- | --- |
| $x_N = C\sin\alpha t + D\cos\alpha t$ | $i\alpha$ is not a root when $\lambda > 0$ |
| $C(\omega^2 - \alpha^2) = D\lambda\alpha,\ D(\omega^2 - \alpha^2) + C\lambda\alpha = a$ | substitute and match $\sin\alpha t$, $\cos\alpha t$ |
| $C = \dfrac{a\lambda\alpha}{\Delta},\ D = \dfrac{a(\omega^2 - \alpha^2)}{\Delta}$ | Cramer, $\Delta = (\omega^2 - \alpha^2)^2 + \lambda^2\alpha^2$ |
| $R = \sqrt{C^2 + D^2} = a/\sqrt{\Delta}$ | amplitude; $\tan\delta = \lambda\alpha/(\omega^2 - \alpha^2)$ |
| $\alpha_r = \sqrt{\omega^2 - \lambda^2/2}$ | minimise $\Delta$ in $s = \alpha^2$: $-2(\omega^2 - s) + \lambda^2 = 0$; exists if $\lambda^2 < 2\omega^2$ |

The homogeneous part decays like $e^{-\lambda t/2}$ (transient); only $R\cos(\alpha t - \delta)$ remains (steady state).

### Derivation: Reduction of order
In short: if $u$ is one solution, $x = uy$ makes the equation first order in $z = \dot y$, giving $x_2 = u\int\dfrac{e^{-\int p\,dt}}{u^2}\,dt$.

| Step | Why |
| --- | --- |
| $\dot x = \dot uy + u\dot y,\ \ddot x = \ddot uy + 2\dot u\dot y + u\ddot y$ | product rule |
| $[\ddot u + p\dot u + qu]\,y + [2\dot u + pu]\,\dot y + u\ddot y = 0$ | substitute and group by $y$, $\dot y$, $\ddot y$ |
| $u\dot z + (2\dot u + pu)z = 0,\ z = \dot y$ | the first bracket is zero because $u$ is a solution; no $y$ left |
| $\dfrac{\dot z}{z} = -\dfrac{2\dot u}{u} - p \Rightarrow z = \dfrac{A\,e^{-\int p\,dt}}{u^2}$ | separable; $\int 2\dot u/u = 2\ln\lvert u\rvert$ |
| $x_2 = u\int z\,dt$ | $y = \int z$; take $A = 1$ and no constant (it only adds $u$ again) |

For the inhomogeneous equation the same substitution gives the linear equation $u\dot z + (2\dot u + pu)z = f$.

### Derivation: Variation of constants
In short: look for $x_N = u_1x_1 + u_2x_2$ with $\dot u_1x_1 + \dot u_2x_2 = 0$; then $\dot u_1 = -x_2f/W$, $\dot u_2 = x_1f/W$.

| Step | Why |
| --- | --- |
| $\dot x_N = u_1\dot x_1 + u_2\dot x_2 + (\dot u_1x_1 + \dot u_2x_2)$ | product rule |
| $\dot u_1x_1 + \dot u_2x_2 = 0$ | free choice (two unknowns, one equation so far): keeps $\ddot x_N$ free of $\ddot u_i$ |
| $L[x_N] = u_1L[x_1] + u_2L[x_2] + \dot u_1\dot x_1 + \dot u_2\dot x_2 = f$ | differentiate again and substitute; $L[x_i] = 0$ |
| $\begin{pmatrix} x_1 & x_2 \\ \dot x_1 & \dot x_2\end{pmatrix}\begin{pmatrix}\dot u_1 \\ \dot u_2\end{pmatrix} = \begin{pmatrix} 0 \\ f\end{pmatrix}$ | the two conditions together; the determinant is $W$ |
| $x_N = -x_1\int\dfrac{x_2f}{W}\,dt + x_2\int\dfrac{x_1f}{W}\,dt$ | Cramer's rule, then integrate |

$f$ is the forcing of the **normalised** equation (coefficient of $\ddot x$ equal to $1$).

### Derivation: Euler-Cauchy equations
In short: $t^2\ddot x + at\dot x + bx = 0$ becomes constant-coefficient with $t = e^s$ ($t > 0$), or directly with $x = t^m$: $m(m - 1) + am + b = 0$.

| Step | Why |
| --- | --- |
| $\dfrac{dx}{dt} = \dfrac{dx}{ds}\dfrac{ds}{dt} = \dfrac1t\,x_s$ | chain rule, $s = \ln t$ |
| $\dfrac{d^2x}{dt^2} = -\dfrac{1}{t^2}x_s + \dfrac{1}{t^2}x_{ss}$ | product rule on $\frac1t x_s$, chain rule again |
| $x_{ss} + (a - 1)x_s + bx = 0$ | multiply by $t^2$ and substitute |
| $x = t^m$: $m(m - 1) + am + b = 0$ | same as $e^{ms}$ in the $s$-equation |

Double root $m$: $t^m$, $t^m\ln t$. Complex $m = \alpha \pm i\beta$: $t^\alpha\cos(\beta\ln t)$, $t^\alpha\sin(\beta\ln t)$.

### Algorithm: Second-order IVP from start to finish
1. Normalise: divide by the coefficient of $\ddot x$; note where $p$, $q$, $f$ are continuous (the interval of the solution).
2. Homogeneous part: constant coefficients, characteristic equation; Euler-Cauchy, $t^m$; one solution known, reduction of order.
3. Particular part: guess (with the resonance rule) for exponential, polynomial or trigonometric forcing; otherwise variation of constants.
4. $x = C_1x_1 + C_2x_2 + x_N$; differentiate the whole sum.
5. Impose $x(t_0)$ and $\dot x(t_0)$; solve the $2\times 2$ system.
6. Check: substitute back, check the initial values, units and the limit $t \to \infty$.

### Trap: Second-order exam traps
- Initial conditions imposed on $x_H$ before adding $x_N$.
- Forgetting the factor $t^s$ when the forcing resonates with a root.
- Using variation of constants with $f$ of the non-normalised equation.
- $e^{kt}$ and $te^{kt}$ written for complex roots, or $\cos$ and $\sin$ without the factor $e^{\rho t}$.

## Unit 4 — Linear systems and the phase plane
Pages: Theory=teoria/topic-4.html; Problems I=problemas/topic-4-part-1.html; Problems II=problemas/topic-4-part-2.html

### Pattern: From an $n$-th order equation to a system
Set $x_1 = x$, $x_2 = \dot x$, ..., $x_n = x^{(n-1)}$. Then $\dot x_1 = x_2$, ..., $\dot x_n = $ the equation solved for $x^{(n)}$. The damped oscillator becomes

$$\frac{d}{dt}\begin{pmatrix} x_1 \\ x_2\end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -\omega^2 & -\lambda\end{pmatrix}\begin{pmatrix} x_1 \\ x_2\end{pmatrix}.$$

Its trace is $-\lambda$ and its determinant $\omega^2$: the characteristic equations of the scalar equation and of the system coincide.

### Theorem: Linear systems: structure and Liouville
$\dot{\mathbf x} = A(t)\mathbf x + \mathbf f(t)$ with continuous entries has a unique solution on the whole interval for each $\mathbf x(t_0)$.
- $n$ independent solutions form the **fundamental matrix** $\Phi = [\mathbf x_1 \mid \cdots \mid \mathbf x_n]$; general solution $\mathbf x = \Phi\mathbf c + \mathbf x_p$.
- **Liouville:** $W = \det\Phi$ satisfies $\dot W = (\operatorname{tr}A)W$, so $W(t) = W(t_0)\exp\int_{t_0}^{t}\operatorname{tr}A(s)\,ds$: zero everywhere or nowhere.
- **Variation of constants:** $\mathbf x_p = \Phi\int\Phi^{-1}\mathbf f\,dt$, from $\mathbf x = \Phi\mathbf c(t)$: $\dot\Phi\mathbf c + \Phi\dot{\mathbf c} = A\Phi\mathbf c + \mathbf f$ and $\dot\Phi = A\Phi$ leave $\Phi\dot{\mathbf c} = \mathbf f$.

### Derivation: Elimination
In short: from $\dot x = ax + by$, $\dot y = cx + dy$ with $b \neq 0$, eliminating $y$ gives $\ddot x - (\operatorname{tr}A)\dot x + (\det A)x = 0$.

| Step | Why |
| --- | --- |
| $y = (\dot x - ax)/b$ | first equation solved for $y$ |
| $\ddot x = a\dot x + b\dot y = a\dot x + b(cx + dy)$ | differentiate the first equation, insert the second |
| $\ddot x = a\dot x + bcx + d(\dot x - ax)$ | replace $by = \dot x - ax$ |
| $\ddot x - (a + d)\dot x + (ad - bc)x = 0$ | collect: a Unit 3 equation |
| $y = (\dot x - ax)/b$ | recover $y$ by differentiating $x$; never integrate a second time |

### Derivation: The eigenvalue method
In short: try $\mathbf x = e^{\lambda t}\mathbf v$; it solves $\dot{\mathbf x} = A\mathbf x$ exactly when $A\mathbf v = \lambda\mathbf v$, so $\lambda^2 - \tau\lambda + \Delta = 0$.

| Step | Why |
| --- | --- |
| $\dot{\mathbf x} = \lambda e^{\lambda t}\mathbf v,\ A\mathbf x = e^{\lambda t}A\mathbf v$ | $\mathbf v$ is constant |
| $(A - \lambda I)\mathbf v = \mathbf 0,\ \mathbf v \neq \mathbf 0$ | equate and divide by $e^{\lambda t} \neq 0$ |
| $\det(A - \lambda I) = 0$ | a homogeneous system has non-zero solutions only if singular |
| $\lambda^2 - \tau\lambda + \Delta = 0,\ \tau = \operatorname{tr}A,\ \Delta = \det A$ | expand the $2\times 2$ determinant |
| $\lambda = \dfrac{\tau}{2} \pm \sqrt{\dfrac{\tau^2}{4} - \Delta}$ | quadratic formula; $\lambda_1 + \lambda_2 = \tau$, $\lambda_1\lambda_2 = \Delta$ |

### Derivation: Distinct real eigenvalues
In short: $\mathbf x = C_1e^{\lambda_1t}\mathbf v_1 + C_2e^{\lambda_2t}\mathbf v_2$; in $\mathbf z = P^{-1}\mathbf x$ with $P = [\mathbf v_1 \mid \mathbf v_2]$ the system decouples and orbits are $z_2 = Kz_1^{\lambda_2/\lambda_1}$.

| Step | Why |
| --- | --- |
| $AP = [\lambda_1\mathbf v_1 \mid \lambda_2\mathbf v_2] = PD$ | column by column, $A\mathbf v_i = \lambda_i\mathbf v_i$ |
| $\dot{\mathbf z} = P^{-1}AP\mathbf z = D\mathbf z$ | $\mathbf x = P\mathbf z$, $P$ constant |
| $z_1 = C_1e^{\lambda_1t},\ z_2 = C_2e^{\lambda_2t}$ | two uncoupled decay or growth laws |
| $z_2 = C_2\big(e^{\lambda_1t}\big)^{\lambda_2/\lambda_1} = Kz_1^{\lambda_2/\lambda_1}$ | eliminate $t$: the orbits |
| $\mathbf x = P\mathbf z = C_1e^{\lambda_1t}\mathbf v_1 + C_2e^{\lambda_2t}\mathbf v_2$ | back to the original variables |

**Node** ($\lambda_1, \lambda_2$ same sign): orbits leave or enter tangent to the eigenvector of smaller $\lvert\lambda\rvert$ (the slow direction) and become parallel to the fast one far away. **Saddle** (opposite signs): the line of $\mathbf v$ with $\lambda < 0$ is the stable manifold, the one with $\lambda > 0$ the unstable manifold. **Zero eigenvalue:** $\mathbf x = C_1\mathbf v_1 + C_2e^{\lambda_2t}\mathbf v_2$, a line of equilibria along $\mathbf v_1$ and straight orbits parallel to $\mathbf v_2$.

### Derivation: Complex eigenvalues: canonical form
In short: with $\lambda = \rho + i\omega$, $\mathbf v = \mathbf u + i\mathbf w$ and $Q = [\mathbf u \mid \mathbf w]$, $Q^{-1}AQ = J = \begin{pmatrix}\rho & \omega \\ -\omega & \rho\end{pmatrix}$.

| Step | Why |
| --- | --- |
| $A(\mathbf u + i\mathbf w) = (\rho + i\omega)(\mathbf u + i\mathbf w)$ | eigenvector for $\rho + i\omega$ (not $\rho - i\omega$) |
| $A\mathbf u = \rho\mathbf u - \omega\mathbf w,\ A\mathbf w = \omega\mathbf u + \rho\mathbf w$ | expand, $i^2 = -1$; real and imaginary parts separately |
| $AQ = [\mathbf u \mid \mathbf w]\begin{pmatrix}\rho & \omega \\ -\omega & \rho\end{pmatrix} = QJ$ | the two lines above, written column by column |
| $\dot z_1 = \rho z_1 + \omega z_2,\ \dot z_2 = -\omega z_1 + \rho z_2$ | $\mathbf z = Q^{-1}\mathbf x$ |
| $r = r_0e^{\rho t},\ \theta = \theta_0 - \omega t$ | polar coordinates: $\dot r = \rho r$, $\dot\theta = -\omega$ (clockwise in the $\mathbf z$-plane) |

Real general solution:

$$\mathbf x = e^{\rho t}\big[(C_1\cos\omega t + C_2\sin\omega t)\mathbf u + (C_2\cos\omega t - C_1\sin\omega t)\mathbf w\big],$$

that is $C_1\operatorname{Re}(\mathbf ve^{\lambda t}) + C_2\operatorname{Im}(\mathbf ve^{\lambda t})$.

### Interpretation: Spirals and centres
- $\rho < 0$: stable spiral (sink); $\rho > 0$: unstable spiral (source); $\rho = 0$: centre, closed ellipses of period $2\pi/\omega$.
- Every turn multiplies the distance by $e^{2\pi\rho/\omega}$.
- **Sense of rotation in the $\mathbf x$-plane:** compute $\dot{\mathbf x} = A\mathbf x$ at $\mathbf x = (1, 0)^T$: it is $(a, c)^T$. If $c > 0$ the orbit turns counterclockwise, if $c < 0$ clockwise (the sense is the sign of the entry $c$ of $A$).

### Derivation: Repeated eigenvalue: stars and improper nodes
In short: if $A \neq \lambda I$, take $\mathbf v_1$ with $(A - \lambda I)\mathbf v_1 = 0$ and $\mathbf v_2$ with $(A - \lambda I)\mathbf v_2 = \mathbf v_1$; then $\mathbf x = e^{\lambda t}[c_1\mathbf v_1 + c_2(t\mathbf v_1 + \mathbf v_2)]$.

| Step | Why |
| --- | --- |
| $\lambda = \tau/2$, $\tau^2 = 4\Delta$ | double root of $\lambda^2 - \tau\lambda + \Delta$ |
| $A = \lambda I$: every vector is an eigenvector | geometric multiplicity 2: **star**, $\mathbf x = e^{\lambda t}\mathbf x_0$, straight rays |
| $A\mathbf v_2 = \lambda\mathbf v_2 + \mathbf v_1 \Rightarrow Q^{-1}AQ = \begin{pmatrix}\lambda & 1 \\ 0 & \lambda\end{pmatrix}$ | $Q = [\mathbf v_1 \mid \mathbf v_2]$, column by column |
| $\dot z_2 = \lambda z_2 \Rightarrow z_2 = c_2e^{\lambda t}$ | the second row is uncoupled |
| $\dot z_1 = \lambda z_1 + c_2e^{\lambda t} \Rightarrow (e^{-\lambda t}z_1)' = c_2$ | integrating factor $e^{-\lambda t}$ |
| $z_1 = (c_1 + c_2t)e^{\lambda t}$ | integrate, multiply back by $e^{\lambda t}$ |

**Improper node:** all orbits are tangent to $\mathbf v_1$ at the origin (for $\lambda < 0$, as $t \to +\infty$). $\mathbf v_2$ is not unique: $\mathbf v_2 + \alpha\mathbf v_1$ works too.

### Table: Classification by trace and determinant
| Condition | Type of the origin |
| --- | --- |
| $\Delta < 0$ | saddle (always unstable) |
| $\Delta > 0$, $\tau^2 > 4\Delta$ | node: stable if $\tau < 0$, unstable if $\tau > 0$ |
| $\Delta > 0$, $\tau^2 = 4\Delta$ | star ($A = \lambda I$) or improper node |
| $\Delta > 0$, $\tau^2 < 4\Delta$, $\tau \neq 0$ | spiral: stable if $\tau < 0$ |
| $\Delta > 0$, $\tau = 0$ | centre |
| $\Delta = 0$ | a line of equilibria (zero eigenvalue) |

### Prerequisite: Matrix exponential (complement)
The fundamental matrix with $\Phi(0) = I$ is $e^{At}$, and $\mathbf x(t) = e^{At}\mathbf x_0$. From the canonical forms:
- $A = PDP^{-1}$: $e^{At} = P\operatorname{diag}(e^{\lambda_1t}, e^{\lambda_2t})P^{-1}$.
- $J = \begin{pmatrix}\lambda & 1 \\ 0 & \lambda\end{pmatrix}$: $e^{Jt} = e^{\lambda t}\begin{pmatrix} 1 & t \\ 0 & 1\end{pmatrix}$.
- $J = \begin{pmatrix}\rho & \omega \\ -\omega & \rho\end{pmatrix}$: $e^{Jt} = e^{\rho t}\begin{pmatrix}\cos\omega t & \sin\omega t \\ -\sin\omega t & \cos\omega t\end{pmatrix}$.
- Then $e^{At} = Qe^{Jt}Q^{-1}$. This packaging is an extension; the notes reach the same solutions through $\mathbf z = Q^{-1}\mathbf x$.

### Algorithm: Planar system from start to finish
1. $\tau = \operatorname{tr}A$, $\Delta = \det A$; classify the origin with the table before computing anything.
2. Eigenvalues from $\lambda^2 - \tau\lambda + \Delta = 0$.
3. Eigenvectors: for the row $(a - \lambda,\ b)$ with $b \neq 0$ take $\mathbf v = (b,\ \lambda - a)^T$.
4. Build $P$ or $Q$ and **check** $Q^{-1}AQ$ equals the expected $D$ or $J$.
5. Write the general solution; impose $\mathbf x(0) = \mathbf x_0$ by solving $Q\mathbf c = \mathbf x_0$.
6. Phase portrait: eigenvector lines, slow and fast directions, sense of rotation from $\dot{\mathbf x}$ at one point.
7. Constant forcing $\dot{\mathbf x} = A\mathbf x + \mathbf b$: equilibrium $\mathbf x^* = -A^{-1}\mathbf b$, then $\mathbf y = \mathbf x - \mathbf x^*$ solves $\dot{\mathbf y} = A\mathbf y$.

### Trap: Phase-plane traps
- Taking the eigenvector of $\rho - i\omega$: $J$ comes out with $\omega$ and $-\omega$ swapped and the rotation reversed.
- Forgetting that eigenvectors can be scaled: different-looking answers may be the same.
- Calling a repeated eigenvalue with $A \neq \lambda I$ a star: it is an improper node with only one eigenvector line.
- Reading a node's tangent direction from the fast eigenvector instead of the slow one.

## Units 5 and 6 — Nonlinear systems, Fourier series and PDEs (extension)
Pages: Extra problems 2nd midterm=extra-problems/midterm-2-problems.html; Extra problems final=extra-problems/final-problems.html

No class notes for these units are in the repository yet. The cards below collect the standard results used in the solved Extra problems P08 to P22; check them against the official notes when they arrive.

### Algorithm: Nonlinear planar systems
1. Equilibria: solve $f(x, y) = 0$, $g(x, y) = 0$ together (factor first; check every branch).
2. Jacobian $D\mathbf F = \begin{pmatrix} f_x & f_y \\ g_x & g_y\end{pmatrix}$ at each equilibrium.
3. Classify each Jacobian with the trace-determinant table of Unit 4.
4. **Linearisation theorem:** if no eigenvalue has zero real part (hyperbolic point), the nonlinear system has the same type nearby. A linear centre is inconclusive.
5. Nullclines $f = 0$ (vertical flow) and $g = 0$ (horizontal flow) to join the local pictures.

### Derivation: Conservative systems and energy
In short: for $\ddot x = -V'(x)$, $E = \tfrac12\dot x^2 + V(x)$ is constant, so orbits are level curves of $E$: minima of $V$ are centres, maxima saddles.

| Step | Why |
| --- | --- |
| $\dot x = y,\ \dot y = -V'(x)$ | first-order system |
| $\dfrac{dE}{dt} = E_x\dot x + E_y\dot y = V'(x)y + y(-V'(x)) = 0$ | chain rule along an orbit |
| $y = \pm\sqrt{2(E - V(x))}$ | each level curve, real where $V(x) \le E$ |

This settles the centres that the linearisation leaves undecided.

### Table: Fourier series on $(-L, L)$
| Item | Formula |
| --- | --- |
| Series | $f \sim \dfrac{a_0}{2} + \sum_{n\ge 1}\Big(a_n\cos\dfrac{n\pi x}{L} + b_n\sin\dfrac{n\pi x}{L}\Big)$ |
| Cosine coefficients | $a_n = \dfrac1L\int_{-L}^{L}f(x)\cos\dfrac{n\pi x}{L}\,dx$ |
| Sine coefficients | $b_n = \dfrac1L\int_{-L}^{L}f(x)\sin\dfrac{n\pi x}{L}\,dx$ |
| $f$ even | $b_n = 0$, $a_n = \frac2L\int_0^L f\cos\frac{n\pi x}{L}\,dx$ |
| $f$ odd | $a_n = 0$, $b_n = \frac2L\int_0^L f\sin\frac{n\pi x}{L}\,dx$ |
| Half range on $(0, L)$ | sine series = odd extension, cosine series = even extension |
| Convergence (Dirichlet) | piecewise smooth $f$: the series gives $\tfrac12\big(f(x^+) + f(x^-)\big)$, also at $\pm L$ via the periodic extension |

With $L = \pi$ the arguments are $nx$. Evaluating the series at a point where $f$ is known gives sums such as $\sum 1/n^2 = \pi^2/6$ and $\sum (-1)^{n+1}/n^2 = \pi^2/12$.

### Derivation: Why the coefficient formulas work
In short: multiply the series by $\cos(m\pi x/L)$ and integrate; orthogonality kills every term except $n = m$.

| Step | Why |
| --- | --- |
| $\cos a\cos b = \tfrac12[\cos(a - b) + \cos(a + b)]$ | product-to-sum |
| $\int_{-L}^{L}\cos\dfrac{n\pi x}{L}\cos\dfrac{m\pi x}{L}\,dx = L\,\delta_{nm}$ | each cosine of a non-zero multiple integrates to $0$ over a full period ($n, m \ge 1$) |
| $\int_{-L}^{L}\sin\dfrac{n\pi x}{L}\cos\dfrac{m\pi x}{L}\,dx = 0$ | odd integrand on a symmetric interval |
| $\int_{-L}^{L}f\cos\dfrac{m\pi x}{L}\,dx = a_mL$ | only the $n = m$ term survives |

### Table: Eigenvalue problems $X'' + \lambda X = 0$ on $(0, L)$
| Boundary conditions | Eigenvalues | Eigenfunctions |
| --- | --- | --- |
| $X(0) = X(L) = 0$ | $(n\pi/L)^2,\ n \ge 1$ | $\sin(n\pi x/L)$ |
| $X'(0) = X'(L) = 0$ | $(n\pi/L)^2,\ n \ge 0$ | $\cos(n\pi x/L)$, with the constant for $n = 0$ |
| $X(0) = 0,\ X'(L) = 0$ | $\big((2n - 1)\pi/(2L)\big)^2$ | $\sin\big((2n - 1)\pi x/(2L)\big)$ |
| Robin, e.g. $X'(L) + hX(L) = 0$ | roots of a transcendental equation, e.g. $\tan\sqrt\lambda L = -\sqrt\lambda/h$ | $\sin\sqrt\lambda x$ |

Always test $\lambda < 0$, $\lambda = 0$ and $\lambda > 0$ separately: a zero mode appears only with Neumann conditions at both ends.

### Algorithm: Separation of variables
1. Homogeneous boundary conditions first: subtract a steady state $u_s(x)$ that carries the non-zero boundary values or the source.
2. $u = X(x)T(t)$; divide by $XT$; both sides equal a constant $-\lambda$.
3. Solve the eigenvalue problem for $X$ (table above).
4. Time (or $y$) factor: heat $T' + k\lambda T = 0 \Rightarrow e^{-k\lambda t}$; wave $T'' + c^2\lambda T = 0 \Rightarrow \cos\omega_nt$, $\sin\omega_nt$ with $\omega_n = c\sqrt{\lambda_n}$; Laplace $Y'' - \lambda Y = 0 \Rightarrow \cosh$, $\sinh$ (and $A_0 + B_0y$ for $\lambda = 0$).
5. Superpose all modes and fit the remaining data with the Fourier coefficient formulas.
6. Checks: boundary values, initial values, $t \to \infty$ (heat tends to $u_s$), units of $k$ and $c$.

### Table: The three classical equations on $(0, L)$ with $u = 0$ at both ends
| Equation | Solution |
| --- | --- |
| Heat $u_t = ku_{xx}$ | $\sum c_n\sin\dfrac{n\pi x}{L}\,e^{-kn^2\pi^2t/L^2}$, $c_n = \frac2L\int_0^L u(x,0)\sin\frac{n\pi x}{L}\,dx$ |
| Wave $u_{tt} = c^2u_{xx}$ | $\sum\big(A_n\cos\omega_nt + B_n\sin\omega_nt\big)\sin\dfrac{n\pi x}{L}$, $\omega_n = \frac{n\pi c}{L}$; $A_n$ from $u(x,0)$, $\omega_nB_n$ from $u_t(x,0)$ |
| Laplace in a rectangle | $\sum\sin\dfrac{n\pi x}{L}\Big(A_n\cosh\dfrac{n\pi y}{L} + B_n\sinh\dfrac{n\pi y}{L}\Big)$ |
| Laplace in a disc or wedge | $r^n$ and $r^{-n}$ times $\cos n\theta$, $\sin n\theta$; keep only $r^n$ if bounded at $r = 0$ |

The slowest heat mode decays with the time constant $\tau_1 = L^2/(k\pi^2)$. The wave equation also has d'Alembert's form $u = \tfrac12[F(x - ct) + F(x + ct)] + \frac{1}{2c}\int_{x - ct}^{x + ct}g(s)\,ds$.

## Pocket prerequisites
Pages: Theory index=teoria/index.html

### Prerequisite: Integrals that keep coming back
| Integral | Result |
| --- | --- |
| $\int\dfrac{f'(x)}{f(x)}\,dx$ | $\ln\lvert f(x)\rvert + C$ |
| $\int\dfrac{dx}{a^2 + x^2}$ | $\dfrac1a\arctan\dfrac xa + C$ |
| $\int\dfrac{dx}{x^2 - a^2}$ | $\dfrac{1}{2a}\ln\left\lvert\dfrac{x - a}{x + a}\right\rvert + C$ |
| $\int te^{at}\,dt$ | $e^{at}\Big(\dfrac ta - \dfrac{1}{a^2}\Big) + C$ |
| $\int e^{at}\cos bt\,dt$ | $\dfrac{e^{at}(a\cos bt + b\sin bt)}{a^2 + b^2} + C$ |
| $\int e^{at}\sin bt\,dt$ | $\dfrac{e^{at}(a\sin bt - b\cos bt)}{a^2 + b^2} + C$ |
| $\int x\cos nx\,dx$ | $\dfrac{x\sin nx}{n} + \dfrac{\cos nx}{n^2} + C$ |
| $\int x\sin nx\,dx$ | $-\dfrac{x\cos nx}{n} + \dfrac{\sin nx}{n^2} + C$ |
| $\int x^2\cos nx\,dx$ | $\dfrac{x^2\sin nx}{n} + \dfrac{2x\cos nx}{n^2} - \dfrac{2\sin nx}{n^3} + C$ |
| $\int\tan x\,dx$ | $-\ln\lvert\cos x\rvert + C$ |

Integration by parts: $\int u\,dv = uv - \int v\,du$; with limits $\int_a^b u\,dv = [uv]_a^b - \int_a^b v\,du$.

### Prerequisite: Values at multiples of $\pi$
- $\sin n\pi = 0$, $\cos n\pi = (-1)^n$, $1 - (-1)^n = 0$ for even $n$ and $2$ for odd $n$.
- $\sin\dfrac{n\pi}{2} = 0, 1, 0, -1, \dots$ for $n = 0, 1, 2, 3$; $\cos\dfrac{(2k + 1)\pi}{2} = 0$.

### Prerequisite: Partial fractions
- Distinct linear factors: $\dfrac{1}{(x - a)(x - b)} = \dfrac{1}{a - b}\Big(\dfrac{1}{x - a} - \dfrac{1}{x - b}\Big)$.
- Logistic: $\dfrac{K}{x(K - x)} = \dfrac1x + \dfrac{1}{K - x}$.
- Repeated factor: $\dfrac{A}{x - a} + \dfrac{B}{(x - a)^2}$. Irreducible quadratic: $\dfrac{Ax + B}{x^2 + px + q}$.
- Cover-up rule: the coefficient of $\frac{1}{x - a}$ is the rest of the fraction evaluated at $x = a$.

### Prerequisite: Trigonometric and hyperbolic identities
| Identity | Use |
| --- | --- |
| $e^{i\theta} = \cos\theta + i\sin\theta$ | complex roots and eigenvalues |
| $\cos^2x = \tfrac12(1 + \cos 2x),\ \sin^2x = \tfrac12(1 - \cos 2x)$ | integrals of squares, energies |
| $\sin a\cos b = \tfrac12[\sin(a + b) + \sin(a - b)]$ | Fourier coefficients |
| $\cos a - \cos b = -2\sin\tfrac{a + b}{2}\sin\tfrac{a - b}{2}$ | beats |
| $\cosh x = \tfrac12(e^x + e^{-x}),\ \sinh x = \tfrac12(e^x - e^{-x})$ | real roots $\pm k$, Laplace modes |
| $\cosh^2x - \sinh^2x = 1,\ (\cosh x)' = \sinh x,\ (\sinh x)' = \cosh x$ | checks of hyperbolic solutions |

### Prerequisite: $2\times 2$ linear algebra
- $A = \begin{pmatrix} a & b \\ c & d\end{pmatrix}$: $\tau = a + d$, $\Delta = ad - bc$, $A^{-1} = \dfrac1\Delta\begin{pmatrix} d & -b \\ -c & a\end{pmatrix}$.
- Eigenvalues: $\lambda = \tfrac\tau2 \pm \sqrt{\tfrac{\tau^2}{4} - \Delta}$; $\lambda_1 + \lambda_2 = \tau$, $\lambda_1\lambda_2 = \Delta$.
- Eigenvector shortcut: $\mathbf v = (b,\ \lambda - a)^T$ if $b \neq 0$, or $(\lambda - d,\ c)^T$ if $c \neq 0$; check with the first row: $(a - \lambda)b + b(\lambda - a) = 0$.
- Always verify $Q^{-1}AQ$ by multiplying out: it catches swapped columns and sign slips.

### Prerequisite: Complex numbers and logarithms
- $z = a + ib = re^{i\theta}$, $r = \sqrt{a^2 + b^2}$, $\theta$ from $\cos\theta = a/r$, $\sin\theta = b/r$ (mind the quadrant).
- $\operatorname{Re}(e^{(\rho + i\omega)t}) = e^{\rho t}\cos\omega t$, $\operatorname{Im}(e^{(\rho + i\omega)t}) = e^{\rho t}\sin\omega t$.
- $e^{\ln x} = x$ for $x > 0$; $\ln\lvert x\rvert = g + c \Rightarrow x = Ce^{g}$ with $C = \pm e^{c}$, and $C = 0$ when $x \equiv 0$ is a solution.
