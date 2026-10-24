---
subject: "Engineering Mechanics"
topic: "Formula sheet and solving compendium, Topics 1 to 5"
tags:
  - formula-sheet
  - cheat-sheet
  - quick-reference
  - engineering-mechanics
sources:
  - "sources/cuatrimestre-1/03-engineering-mechanics/teoria/Notes.pdf"
web: "subjects/engineering-mechanics/formula-sheet/index.html"
---

# Formula Sheet - Engineering Mechanics

Every key formula of the course with its short derivation, the reason for each step, its hypotheses and the recipe to use it in an exam. It gathers the five topic sheets ([[Formula Sheet - Topic 1 Particle Kinematics]], [[Formula Sheet - Topic 2 Point Particle Dynamics]], [[Formula Sheet - Topic 3 Constraints and Reaction Forces]], [[Formula Sheet - Topic 4 Angular Momentum]], [[Formula Sheet - Topic 5 Relative Motion]]) and the theory notes [[Topic 1 - Fundamentals and Particle Kinematics]] to [[Topic 5 - Relative Motion]], and keeps their notation and citations (Notes = `Notes.pdf`, Slide = the topic's lecture slides).

The page `subjects/engineering-mechanics/formula-sheet/index.html` is generated from this note by `python tools/build_formula_sheet.py`; edit this note, never the page. Card headings are `### <Kind>: <title>`; a derivation card opens with an `In short:` line; tables headed `| Step | Why |` become the step grid.

## How to solve a mechanics problem
Pages: Problems=problemas/index.html; Extra problems=extra-problems/midterm-1-problems.html

### Algorithm: The lecturer's order
1. **Frames, bases and coordinates.** Fixed frame $S_0 = \{O;\ \mathcal B_0\}$, moving frames $S_1 = \{A;\ \mathcal B_1\}, \dots$, intrinsic basis $\{\mathbf e_t, \mathbf e_n, \mathbf e_b\}$ if useful. Count degrees of freedom, write the constraints, list the parameters with SI units.
2. **Change of basis and position vector.** Deduce every $[{}_0R_1]$ from a drawing of each rotation (axis out of the paper ⊙ or into it ⊗); build $\mathbf r_0^P$ as a chain of vectors, e.g. $\overrightarrow{OC} + \overrightarrow{CP}$.
3. **Kinematics.** Velocity and acceleration: chain rule, product rule, $\boldsymbol\omega \times$ for rotating unit vectors, composition of motions and Coriolis.
4. **Forces and equations of motion.** Free-body diagram: applied forces, constraint reactions (normal to the constraint), inertia forces if the frame is not inertial; project $m\mathbf a = \sum\mathbf F$ on the chosen basis. Tangent projections give the motion, normal projections the reactions.
5. **Answers and checks.** Answer every part; limiting cases ($\theta = 0$, $\Omega = 0$), dimensions, $\det R = 1$, orthogonality, energy if it is conserved.

### Pattern: Notation of the course
- $\mathbf r_0^P$, $\mathbf v_0^P$, $\mathbf a_0^P$: position, velocity, acceleration of the point $P$ (superscript) seen from $S_0$ (subscript).
- $\left.\dfrac{d\mathbf b}{dt}\right|_0$: derivative of a vector seen from $S_0$; it differs from $\left.\dfrac{d\mathbf b}{dt}\right|_1$ when $S_1$ rotates.
- $[{}_0R_1]$: change-of-basis matrix; its **columns** are $\mathbf i_1, \mathbf j_1, \mathbf k_1$ written in $\mathcal B_0$, and $[\mathbf b]_0 = [{}_0R_1][\mathbf b]_1$ [Notes Eqs. 1.12–1.13].
- $\boldsymbol\omega_{10}$, $\boldsymbol\alpha_{10}$: angular velocity and acceleration of $S_1$ relative to $S_0$.
- $T_0$ kinetic energy, $V_0$ potential, $E_0 = T_0 + V_0$, all measured in $S_0$.

### Trap: Mistakes that cost the most marks
- Differentiating a unit vector of a moving basis as if it were constant: $\dot{\mathbf e}_R = \dot\theta\,\mathbf e_\theta \neq \mathbf 0$.
- A sign in $[{}_0R_1]$ guessed instead of deduced: draw the view along the rotation axis and apply the right-hand rule.
- Writing a reaction with a tangent component on a smooth constraint (it has none), or forgetting that friction is applied force when sliding.
- Adding inertia forces when working in the inertial frame $S_0$ (they exist only in the equation written in $S_1$).
- Missing the factor 2 of Coriolis, or the minus sign of the centripetal term $-R\dot\theta^2\mathbf e_R$.

## Topic 1 — Fundamentals and particle kinematics
Pages: Theory=teoria/topic-1.html; Problems=problemas/topic-1.html

### Theorem: Rotation matrices
- **Orthogonal, proper:** $[{}_1R_0] = [{}_0R_1]^{-1} = [{}_0R_1]^T$, $\det[{}_0R_1] = +1$ [Notes Eqs. 1.14–1.15].
- **Composition:** $[{}_0R_2] = [{}_0R_1][{}_1R_2]$, not commutative [Notes Eq. 1.16].
- **Axis and angle:** eigenvalues $1, e^{\pm i\beta}$; the axis is the eigenvector of $\lambda = 1$ and $\operatorname{tr}R = 1 + 2\cos\beta$ [Slide 6].

$$[{}_0R_1(z,\theta)] = \begin{pmatrix}\cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1\end{pmatrix}$$

About $x$: rows $(1,0,0)$, $(0,\cos,-\sin)$, $(0,\sin,\cos)$. About $y$: rows $(\cos,0,\sin)$, $(0,1,0)$, $(-\sin,0,\cos)$: the minus moves to the lower row because $\mathbf k \times \mathbf i = \mathbf j$ [Notes Eqs. 1.18–1.20].

### Derivation: Building $[{}_0R_1]$ from a drawing
In short: write each new unit vector in the old basis using the right triangle of the rotation angle; those components are the columns.

| Step | Why |
| --- | --- |
| rotation $\theta$ about $\mathbf k_0$ (⊙, out of the paper) | the view along the axis shows $\mathbf i_0$, $\mathbf j_0$ in the plane; positive $\theta$ is counterclockwise |
| $\mathbf i_1 = \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0$ | unit hypotenuse: adjacent side $\cos\theta$ on $\mathbf i_0$, opposite side $\sin\theta$ on $\mathbf j_0$ |
| $\mathbf j_1 = -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0$ | $\mathbf j_1$ is $\mathbf i_1$ turned $90°$ more: its $\mathbf i_0$ component points backwards |
| $\mathbf k_1 = \mathbf k_0$ | the axis of rotation does not move |
| check $\det = \cos^2\theta + \sin^2\theta = 1$ | a right-handed orthonormal basis |

If the axis points into the paper (⊗) in the view drawn, the positive angle is clockwise there and the signs of the $\sin$ terms swap.

### Derivation: Cylindrical coordinates
In short: the polar unit vectors rotate with $\theta$, $\dot{\mathbf e}_R = \dot\theta\,\mathbf e_\theta$ and $\dot{\mathbf e}_\theta = -\dot\theta\,\mathbf e_R$, and the product rule does the rest.

| Step | Why |
| --- | --- |
| $\mathbf e_R = \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0,\ \mathbf e_\theta = -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0$ | $\mathbf e_R$ along $OP$ projected on $Oxy$; $\mathbf e_\theta$ at $+90°$ |
| $\dot{\mathbf e}_R = \dot\theta(-\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0) = \dot\theta\,\mathbf e_\theta$ | chain rule: $\frac{d}{dt}\cos\theta = -\sin\theta\,\dot\theta$ |
| $\dot{\mathbf e}_\theta = -\dot\theta\,\mathbf e_R$ | same calculation |
| $\mathbf r = R\,\mathbf e_R + z\,\mathbf k_0 \Rightarrow \mathbf v = \dot R\,\mathbf e_R + R\dot\theta\,\mathbf e_\theta + \dot z\,\mathbf k_0$ | product rule on $R\,\mathbf e_R$ |
| $\mathbf a = (\ddot R - R\dot\theta^2)\,\mathbf e_R + (R\ddot\theta + 2\dot R\dot\theta)\,\mathbf e_\theta + \ddot z\,\mathbf k_0$ | differentiate again; $\dot R\dot\theta$ appears twice |

$-R\dot\theta^2$ is the centripetal term; $2\dot R\dot\theta$ vanishes if the radius or the angle is constant. Also $R\ddot\theta + 2\dot R\dot\theta = \frac1R\frac{d}{dt}(R^2\dot\theta)$.

### Table: Spherical coordinates (latitude $\phi$)
$x = r\cos\phi\cos\theta$, $y = r\cos\phi\sin\theta$, $z = r\sin\phi$, with $\theta$ the azimuth in $Oxy$ and $\phi \in [-\pi/2, \pi/2]$ measured up from the equator.

| Quantity | Expression |
| --- | --- |
| basis rates | $\dot{\mathbf e}_r = \dot\theta\cos\phi\,\mathbf e_\theta + \dot\phi\,\mathbf e_\phi$; $\dot{\mathbf e}_\theta = -\dot\theta\cos\phi\,\mathbf e_r + \dot\theta\sin\phi\,\mathbf e_\phi$; $\dot{\mathbf e}_\phi = -\dot\phi\,\mathbf e_r - \dot\theta\sin\phi\,\mathbf e_\theta$ |
| velocity | $\dot r\,\mathbf e_r + r\dot\theta\cos\phi\,\mathbf e_\theta + r\dot\phi\,\mathbf e_\phi$ |
| $a_r$ | $\ddot r - r\dot\phi^2 - r\dot\theta^2\cos^2\phi$ |
| $a_\theta$ | $2\dot r\dot\theta\cos\phi + r\ddot\theta\cos\phi - 2r\dot\theta\dot\phi\sin\phi$ |
| $a_\phi$ | $2\dot r\dot\phi + r\ddot\phi + r\dot\theta^2\sin\phi\cos\phi$ |

**Trap:** with the colatitude convention ($\phi$ measured from $+z$) every $\cos\phi$ becomes $\sin\phi$; check which angle the statement uses.

### Derivation: Intrinsic (Frenet) acceleration
In short: $\mathbf v = \dot s\,\mathbf e_t$; differentiating, the turning of $\mathbf e_t$ gives the normal term $\dot s^2/\rho$.

| Step | Why |
| --- | --- |
| $\mathbf v = \dfrac{d\mathbf r}{ds}\dfrac{ds}{dt} = \dot s\,\mathbf e_t$ | chain rule; $d\mathbf r/ds$ is the unit tangent |
| $\mathbf a = \ddot s\,\mathbf e_t + \dot s\,\dfrac{d\mathbf e_t}{ds}\dfrac{ds}{dt}$ | product rule, then chain rule on $\mathbf e_t(s(t))$ |
| $\dfrac{d\mathbf e_t}{ds} = \dfrac{1}{\rho}\,\mathbf e_n$ | first Frenet formula: definition of curvature $\kappa = 1/\rho$ |
| $\mathbf a = \ddot s\,\mathbf e_t + \dfrac{\dot s^2}{\rho}\,\mathbf e_n$ | $a_b = 0$: $\mathbf v$ and $\mathbf a$ lie in the osculating plane |
| $\mathbf v \times \mathbf a = \dfrac{\dot s^3}{\rho}\,\mathbf e_b \Rightarrow \kappa = \dfrac{\lVert\mathbf v \times \mathbf a\rVert}{v^3}$ | $\mathbf e_t \times \mathbf e_t = \mathbf 0$, $\mathbf e_t \times \mathbf e_n = \mathbf e_b$ |

Then $\mathbf e_t = \mathbf v/v$, $\mathbf e_b = \mathbf v \times \mathbf a/\lVert\mathbf v \times \mathbf a\rVert$, $\mathbf e_n = \mathbf e_b \times \mathbf e_t$, $a_t = \dot v = \mathbf a\cdot\mathbf e_t$, $a_n = \sqrt{a^2 - a_t^2}$. Centre of curvature: $\mathbf r_C = \mathbf r + \rho\,\mathbf e_n$.

### Table: Frenet-Serret formulas
| Formula | Meaning |
| --- | --- |
| $\dfrac{d\mathbf e_t}{ds} = \kappa\,\mathbf e_n$ | the tangent turns towards the centre of curvature |
| $\dfrac{d\mathbf e_n}{ds} = -\kappa\,\mathbf e_t + \tau\,\mathbf e_b$ | the normal turns in the osculating plane and leaves it with the torsion |
| $\dfrac{d\mathbf e_b}{ds} = -\tau\,\mathbf e_n$ | a plane curve has $\tau = 0$ and a fixed binormal |
| $\tau = \dfrac{(\mathbf v \times \mathbf a)\cdot\dot{\mathbf a}}{\lVert\mathbf v \times \mathbf a\rVert^2}$ | torsion from time derivatives |

### Trap: Intrinsic kinematics
- $v_n = v_b = 0$ always; $a_b = 0$ always.
- $a_t = 0$ means constant speed, not zero acceleration (uniform circular motion has $a_n = v^2/\rho$).
- Arc length: $s(t) = \int_{t_0}^{t}\lVert\mathbf v(\tau)\rVert\,d\tau$; for a helix $v$ is constant and $s = vt$.

## Topic 2 — Point particle dynamics
Pages: Theory=teoria/topic-2.html; Problems=problemas/topic-2.html

### Theorem: Newton's laws and momentum
- **Second law** in an inertial frame: $\mathbf F = \left.\dfrac{d\mathbf p_0}{dt}\right|_0 = m\,\mathbf a_0^P$, $\mathbf p_0 = m\,\mathbf v_0^P$ [Slides 4–6].
- **Projected** on any basis: Cartesian $m\ddot x = F_x$; cylindrical $m(\ddot R - R\dot\theta^2) = F_R$, $m(R\ddot\theta + 2\dot R\dot\theta) = F_\theta$, $m\ddot z = F_z$ [Slide 9].
- **State form:** with $\mathbf v = \dot{\mathbf r}$, six first-order equations and six initial conditions $\mathbf r(0)$, $\mathbf v(0)$ [Slide 10].
- **Isolated system:** $\sum\mathbf F^{ext} = \mathbf 0 \Rightarrow \sum m_i\mathbf v_i = $ const [Slides 7–8].

### Derivation: Kinetic energy theorem
In short: dot Newton's law with $\mathbf v$: $m\,\mathbf a\cdot\mathbf v = \frac{d}{dt}(\tfrac12mv^2)$, so power equals the rate of change of kinetic energy.

| Step | Why |
| --- | --- |
| $m\,\mathbf a\cdot\mathbf v = \mathbf F\cdot\mathbf v$ | dot product of $m\mathbf a = \mathbf F$ with $\mathbf v$ |
| $\dfrac{d}{dt}\big(\tfrac12m\,\mathbf v\cdot\mathbf v\big) = m\,\dot{\mathbf v}\cdot\mathbf v$ | product rule; the dot product is symmetric |
| $\dfrac{dT_0}{dt} = P = \mathbf F\cdot\mathbf v_0^P$ | power of the force [Slide 13] |
| $T_0(t_2) - T_0(t_1) = \int_{t_1}^{t_2}P\,dt = \int_{\mathbf r_1}^{\mathbf r_2}\mathbf F\cdot d\mathbf r = W_{12}$ | integrate with Barrow's rule; $\mathbf v\,dt = d\mathbf r$ |

A force normal to the velocity (a smooth fixed constraint, the Coriolis force) does no work.

### Derivation: Potential energy and energy conservation
In short: if $\mathbf F = -\nabla V_0$, then $\mathbf F\cdot\mathbf v = -\frac{dV_0}{dt}$, so $T_0 + V_0$ is constant when only conservative forces work.

| Step | Why |
| --- | --- |
| $\dfrac{d}{dt}V_0(\mathbf r(t)) = \nabla V_0\cdot\dot{\mathbf r}$ | chain rule in three variables |
| $P = \mathbf F\cdot\mathbf v = -\nabla V_0\cdot\mathbf v = -\dfrac{dV_0}{dt}$ | definition of potential |
| $\dfrac{d}{dt}(T_0 + V_0) = P_{NC}$ | add the kinetic energy theorem; only non-conservative forces remain |
| $E_0 = T_0 + V_0 = $ const if $P_{NC} = 0$ | non-conservative forces absent or normal to $\mathbf v$ [Slides 19–20] |

### Table: Potentials of the course
| Force | Potential $V_0$ |
| --- | --- |
| uniform gravity $-mg\,\mathbf k_0$ | $mgz$ |
| linear spring, stiffness $k$, natural length $\ell_0$ | $\tfrac12k(\ell - \ell_0)^2$ |
| inverse square $-\dfrac{GMm}{r^2}\mathbf e_r$ | $-\dfrac{GMm}{r}$ |
| central $F(r)\,\mathbf e_r$ | $V_0(r) = -\int F(r)\,dr$ |
| $aR\,\mathbf e_R$ (Slide 17) | $-\tfrac12aR^2$ |

### Pattern: Is the force conservative?
- Cartesian test: $\nabla \times \mathbf F = \mathbf 0$ on a simply connected domain, equivalently $\oint\mathbf F\cdot d\mathbf r = 0$ [Slides 14–16].
- Plane polar test for $\mathbf F = F_R\,\mathbf e_R + F_\theta\,\mathbf e_\theta$: $\dfrac{\partial(RF_\theta)}{\partial R} - \dfrac{\partial F_R}{\partial\theta} = 0$.
- Slide 18: $\mathbf F = bR^2\,\mathbf e_\theta$ gives $\partial_R(bR^3) = 3bR^2 \neq 0$: not conservative (a full turn does work $2\pi bR^3$).
- Friction, drag and any force that depends on the velocity are not conservative.

### Derivation: One-dimensional motion from the energy
In short: $\tfrac12m\dot x^2 + V_0(x) = E_0$ gives the speed at each $x$, the allowed regions and, by separation, the time.

| Step | Why |
| --- | --- |
| $\ddot x = \dfrac{d\dot x}{dt} = \dfrac{d\dot x}{dx}\dfrac{dx}{dt} = \dot x\dfrac{d\dot x}{dx} = \dfrac{d}{dx}\big(\tfrac12\dot x^2\big)$ | chain rule: the standard trick to integrate $m\ddot x = F(x)$ once |
| $\tfrac12m\dot x^2 = \int F\,dx = -V_0(x) + E_0$ | integrate in $x$; the constant is the energy |
| $v(x) = \sqrt{2(E_0 - V_0(x))/m}$ | real only where $E_0 \ge V_0(x)$ (allowed region) |
| $t = \int_{x_0}^{x}\dfrac{dx'}{\sqrt{2(E_0 - V_0(x'))/m}}$ | separable: $dt = dx/v$ |

Turning points: $V_0(x) = E_0$. Between two turning points the motion is periodic.

### Theorem: Equilibrium and stability
- Equilibrium: $F(x^*) = -V_0'(x^*) = 0$ [Slides 21–22].
- Stable if $V_0''(x^*) > 0$ (minimum), unstable if $V_0''(x^*) < 0$ (maximum); if $V_0'' = 0$ look at higher derivatives.
- Small oscillations about a minimum: $m\ddot\xi + V_0''(x^*)\,\xi = 0$, $\omega = \sqrt{V_0''(x^*)/m}$ (Taylor: $V_0'(x^* + \xi) \approx V_0''(x^*)\xi$).

### Derivation: Simple pendulum
In short: in the polar basis of the rod, the transverse equation gives $\ddot\theta + (g/\ell)\sin\theta = 0$ and the radial one the tension $T = m(g\cos\theta + \ell\dot\theta^2)$.

| Step | Why |
| --- | --- |
| $\mathbf r = \ell\,\mathbf e_r$, $\theta$ from the downward vertical | one degree of freedom; $\ell$ fixed by the rod |
| $\mathbf a = -\ell\dot\theta^2\,\mathbf e_r + \ell\ddot\theta\,\mathbf e_\theta$ | cylindrical formulas with $\dot R = \ddot R = 0$ |
| $m\mathbf g = mg\cos\theta\,\mathbf e_r - mg\sin\theta\,\mathbf e_\theta$ | gravity is adjacent to $\theta$ along the rod, opposite across it, and pulls back towards $\theta = 0$ |
| $\mathbf e_\theta$: $m\ell\ddot\theta = -mg\sin\theta$ | the tension $-T\,\mathbf e_r$ has no transverse component |
| $\mathbf e_r$: $-m\ell\dot\theta^2 = mg\cos\theta - T$ | gives the tension (a reaction) |
| $E_0 = \tfrac12m\ell^2\dot\theta^2 + mg\ell(1 - \cos\theta)$ | first integral: multiply the $\mathbf e_\theta$ equation by $\dot\theta$ and integrate |

Small angles: $\sin\theta \approx \theta$, $\omega_0 = \sqrt{g/\ell}$, period $2\pi\sqrt{\ell/g}$. Equilibria $\theta = 0$ (stable) and $\theta = \pi$ (unstable).

## Topic 3 — Constraints and reaction forces
Pages: Theory=teoria/topic-3.html; Problems=problemas/topic-3.html

### Table: Degrees of freedom and reactions
| Constraint | Equations | DOF | Normal space | Unknown reactions |
| --- | --- | --- | --- | --- |
| free particle | none | 3 | — | 0 |
| surface | $f(\mathbf r) = 0$ | 2 | $\nabla f$ | 1 |
| curve | $f = 0,\ g = 0$ | 1 | $\nabla f$, $\nabla g$ | 2 |

Normal of a surface: $\nabla f$, or $\mathbf t_\alpha \times \mathbf t_\beta$ with $\mathbf t_\alpha = \partial\mathbf r/\partial\alpha$ from a parametrisation. Tangent of a curve: $d\mathbf r/d\alpha$, or $\nabla f \times \nabla g$ [Slides 7–12, Notes 6.3].

### Derivation: Why a smooth fixed constraint does no work
In short: differentiating $f(\mathbf r(t)) = 0$ shows $\mathbf v \perp \nabla f$; the reaction is along $\nabla f$, so $\mathbf N\cdot\mathbf v = 0$.

| Step | Why |
| --- | --- |
| $\dfrac{d}{dt}f(\mathbf r(t), t) = \nabla f\cdot\mathbf v + \dfrac{\partial f}{\partial t} = 0$ | chain rule along the motion; the constraint holds at all times |
| scleronomic, $\partial f/\partial t = 0$: $\nabla f\cdot\mathbf v = 0$ | the velocity is tangent to the constraint |
| $\mathbf N = N_1\nabla f \Rightarrow P_N = \mathbf N\cdot\mathbf v = 0$ | smooth constraint: the reaction lies in the normal space [Notes Eq. 6.12] |
| rheonomic: $P_N = -N_1\,\partial f/\partial t \neq 0$ | a moving constraint can do work (spool, Slide 22) |

### Algorithm: Dynamical decoupling
1. Write $m\,\mathbf a_0^P = \mathbf F_{applied} + \mathbf N$ with $\mathbf N = N_1\mathbf n$ (surface) or $N_1\mathbf n_f + N_2\mathbf n_g$ (curve) [Slide 13].
2. Project on the **tangent** vectors: $\mathbf N$ disappears and the equations of motion of the free coordinates remain [Slide 14].
3. Project on the **normal** vectors: each projection gives one reaction once the motion is known.
4. Along a curve use the intrinsic frame: $F_t = m\ddot s$, $F_n + N_n = m\dot s^2/\rho$, $F_b + N_b = 0$ [Notes Eqs. 6.17–6.19].
5. Conservative applied forces and fixed smooth constraints: use $E_0 = $ const as a first integral to get $\dot s^2$ (or $\dot\theta^2$) in the normal equation.

### Table: Coulomb friction
| Regime | Friction force | Power |
| --- | --- | --- |
| sliding, $\mathbf v^* \neq \mathbf 0$ | applied force $\mathbf F_R = -\mu N\,\dfrac{\mathbf v^*}{\lVert\mathbf v^*\rVert}$ | $-\mu Nv^* < 0$ |
| sticking, $\mathbf v^* = \mathbf 0$ | constraint force in the tangent space, $\lVert\mathbf F_R\rVert \le \mu N$ | $0$ |

$\mathbf v^*$ is the velocity relative to the surface and $N$ the magnitude of the normal reaction. Switch to sliding when the tangential force needed to stay at rest exceeds $\mu N$; switch back to rest when $\mathbf v^* = \mathbf 0$ and the applied tangential force is at most $\mu N$ [Slides 18–19, Notes 6.6].

### Derivation: Atwood machine
In short: the inextensible string gives $\ddot x_2 = -\ddot x_1$; subtracting the two equations of motion eliminates the tension.

| Step | Why |
| --- | --- |
| $x_1 + x_2 = $ const $\Rightarrow \ddot x_2 = -\ddot x_1$ | string length fixed, $x_i$ measured downwards, ideal pulley |
| $m_1\ddot x_1 = m_1g - T,\ m_2\ddot x_2 = m_2g - T$ | same tension on both sides of a massless frictionless pulley |
| $(m_1 + m_2)\ddot x_1 = (m_1 - m_2)g$ | subtract the second equation from the first |
| $T = \dfrac{2m_1m_2}{m_1 + m_2}\,g$ | back into the first equation |

Checks: $m_1 = m_2$ gives rest or uniform motion and $T = m_1g$; $m_2 = 0$ gives free fall.

### Table: Classification of constraints
| Type | Form | Consequence |
| --- | --- | --- |
| holonomic | $f(\mathbf r, t) = 0$ | removes one coordinate |
| non-holonomic | $\sum A_i\dot x_i + B = 0$, not integrable | removes a velocity, not a coordinate |
| scleronomic | $\partial f/\partial t = 0$ | no work if smooth |
| rheonomic | $\partial f/\partial t \neq 0$ | the reaction can do work |
| unilateral | $f \ge 0$, $N \ge 0$ | the particle leaves the constraint when $N = 0$ |

**Trap:** for a unilateral contact (a bead on the outside of a sphere, an aircraft on the runway) compute $N$ as a function of the position and find where it reaches zero; beyond that point the equations with $N$ are no longer valid.

## Topic 4 — Angular momentum and central forces
Pages: Theory=teoria/topic-4.html; Problems=problemas/topic-4.html

### Derivation: Angular momentum about a moving point
In short: differentiating $\mathbf H_{A0}^P = \overrightarrow{AP} \times m\mathbf v_0^P$ gives $\dot{\mathbf H}_{A0} = \mathbf M_A - \mathbf v_0^A \times m\mathbf v_0^P$.

| Step | Why |
| --- | --- |
| $\mathbf H_{A0}^P = (\mathbf r_0^P - \mathbf r_0^A) \times m\,\mathbf v_0^P$ | definition [Slide 3, Notes 4.8] |
| $\dot{\mathbf H}_{A0}^P = (\mathbf v_0^P - \mathbf v_0^A) \times m\mathbf v_0^P + \overrightarrow{AP} \times m\,\mathbf a_0^P$ | product rule for the cross product (order kept) |
| $\mathbf v_0^P \times m\mathbf v_0^P = \mathbf 0$ | parallel vectors |
| $\overrightarrow{AP} \times m\mathbf a_0^P = \overrightarrow{AP} \times \mathbf F = \mathbf M_A$ | Newton's second law |
| $\dot{\mathbf H}_{A0}^P = \mathbf M_A - \mathbf v_0^A \times m\,\mathbf v_0^P$ | the extra term vanishes if $A$ is fixed or $\mathbf v_0^A \parallel \mathbf v_0^P$ [Slide 4] |

Conservation: $\mathbf M_A = \mathbf 0$ about a fixed point $\Rightarrow \mathbf H_{A0} = $ const (three scalar first integrals).

### Derivation: Central forces: planar motion and Kepler's second law
In short: $\mathbf M_O = \mathbf r \times F(r)\mathbf e_r = \mathbf 0$, so $\mathbf H_O$ is constant, the motion is planar and $h = r^2\dot\theta$ is constant.

| Step | Why |
| --- | --- |
| $\mathbf r \times F(r)\,\mathbf e_r = \mathbf 0$ | $\mathbf r$ and $\mathbf e_r$ are parallel |
| $\mathbf H_O = $ const, $\mathbf r \perp \mathbf H_O$ | $\mathbf H_O = \mathbf r \times m\mathbf v$ is normal to $\mathbf r$: $\mathbf r$ stays in a fixed plane |
| $m(r\ddot\theta + 2\dot r\dot\theta) = 0$ | transverse equation: a central force has no $\mathbf e_\theta$ component |
| $r\ddot\theta + 2\dot r\dot\theta = \dfrac1r\dfrac{d}{dt}(r^2\dot\theta) = 0$ | product rule backwards |
| $h = r^2\dot\theta = $ const, $\dfrac{dA}{dt} = \tfrac12r^2\dot\theta = \dfrac h2$ | the area swept in $dt$ is the triangle $\tfrac12r\cdot r\,d\theta$ [Slide 12] |

### Derivation: Binet's equation
In short: with $u = 1/r$ and $d/dt = hu^2\,d/d\theta$, the radial equation becomes $u'' + u = -F/(mh^2u^2)$; for gravity $u'' + u = \mu/h^2$.

| Step | Why |
| --- | --- |
| $\dot\theta = hu^2$ | $h = r^2\dot\theta$ with $r = 1/u$ |
| $\dot r = -\dfrac{\dot u}{u^2} = -\dfrac{u'\dot\theta}{u^2} = -h\,u'$ | chain rule twice; $' = d/d\theta$ |
| $\ddot r = -h\,u''\,\dot\theta = -h^2u^2u''$ | $h$ is constant |
| $m(\ddot r - r\dot\theta^2) = F$ with $r\dot\theta^2 = h^2u^3$ | radial equation [Slide 13, Notes 8.4] |
| $u'' + u = -\dfrac{F(1/u)}{mh^2u^2}$ | divide by $-mh^2u^2$ |
| $F = -\dfrac{\mu m}{r^2}$: $u = \dfrac{\mu}{h^2} + C\cos(\theta - \theta_0)$ | constant forcing: particular solution plus harmonic part |
| $r = \dfrac{p}{1 + e\cos(\theta - \theta_0)},\ p = \dfrac{h^2}{\mu},\ e = \dfrac{Ch^2}{\mu}$ | a conic with focus at $O$ (Kepler's first law); periapsis at $\theta = \theta_0$ |

### Table: Conics and energy
| Orbit | $e$ | $a$ | $\xi = \tfrac12v^2 - \mu/r$ |
| --- | --- | --- | --- |
| circle | $0$ | $p$ | $-\mu/(2a) < 0$ |
| ellipse | $0 < e < 1$ | $p/(1 - e^2) > 0$ | $-\mu/(2a) < 0$ |
| parabola | $1$ | $\infty$ | $0$ |
| hyperbola | $e > 1$ | $< 0$ | $-\mu/(2a) > 0$ |

Ellipse: $r_p = a(1 - e)$, $r_a = a(1 + e)$, $b = a\sqrt{1 - e^2}$, $p = a(1 - e^2) = b^2/a$, $h = \sqrt{\mu p}$, $v_p/v_a = r_a/r_p$.

### Derivation: Vis-viva and Kepler's third law
In short: evaluate $\xi$ at periapsis with $h = r_pv_p$ to get $\xi = -\mu/(2a)$; the area rate $h/2$ gives the period $\tau = 2\pi\sqrt{a^3/\mu}$.

| Step | Why |
| --- | --- |
| $v_p = h/r_p,\ r_p = \dfrac{p}{1 + e},\ h^2 = \mu p$ | at periapsis $\dot r = 0$, so $v = r\dot\theta = h/r$ |
| $\xi = \dfrac{\mu(1 + e)^2}{2p} - \dfrac{\mu(1 + e)}{p} = -\dfrac{\mu(1 - e^2)}{2p}$ | substitute and factor $\mu(1 + e)/(2p)$ |
| $\xi = -\dfrac{\mu}{2a} \Rightarrow v^2 = \mu\Big(\dfrac2r - \dfrac1a\Big)$ | $p = a(1 - e^2)$; vis-viva [Notes Eq. 8.19] |
| $\tau = \dfrac{\pi ab}{h/2} = \dfrac{2\pi ab}{\sqrt{\mu a(1 - e^2)}} = 2\pi\sqrt{\dfrac{a^3}{\mu}}$ | ellipse area over areal velocity; $b = a\sqrt{1 - e^2}$ [Notes Eqs. 8.16–8.18] |

Circular speed $v_c = \sqrt{\mu/r}$, escape speed $v_e = \sqrt{2\mu/r} = \sqrt2\,v_c$ [Notes Eqs. 8.20–8.21].

### Table: Two-body reduction
| Quantity | Formula |
| --- | --- |
| barycentre | $\mathbf r_G = \dfrac{m_P\mathbf r_P + m_S\mathbf r_S}{m_P + m_S}$, $\ddot{\mathbf r}_G = \mathbf 0$ |
| relative vector | $\mathbf r = \mathbf r_P - \mathbf r_S$, $\ddot{\mathbf r} = -\dfrac{\mu}{r^3}\mathbf r$, $\mu = G(m_P + m_S)$ |
| bodies about $G$ | $\mathbf r_P - \mathbf r_G = \dfrac{m_S}{m_P + m_S}\mathbf r$, $\mathbf r_S - \mathbf r_G = -\dfrac{m_P}{m_P + m_S}\mathbf r$ |

### Pattern: Effective potential in $u$
For any central force, $(u')^2 + W_{eff}(u) = 2\xi/h^2$ with $W_{eff}(u) = u^2 + 2V_0(1/u)/h^2$ ($V_0$ per unit mass). Motion only where $W_{eff} \le 2\xi/h^2$; the roots give $r_{min}$ and $r_{max}$. For gravity, $W_{eff} = u^2 - 2\mu u/h^2$.

## Topic 5 — Relative motion
Pages: Theory=teoria/topic-5.html; Problems=problemas/topic-5.html

### Derivation: The Coriolis theorem
In short: write $\mathbf b$ in the moving basis; the derivative of each moving unit vector seen from $S_0$ is $\boldsymbol\omega_{10} \times$ that vector.

| Step | Why |
| --- | --- |
| $\mathbf b = b_x\mathbf i_1 + b_y\mathbf j_1 + b_z\mathbf k_1$ | components in $\mathcal B_1$ |
| $\left.\dfrac{d\mathbf b}{dt}\right\rvert_0 = (\dot b_x\mathbf i_1 + \dot b_y\mathbf j_1 + \dot b_z\mathbf k_1) + b_x\dot{\mathbf i}_1 + b_y\dot{\mathbf j}_1 + b_z\dot{\mathbf k}_1$ | product rule; seen from $S_0$ the unit vectors move |
| $\left.\dfrac{d\mathbf i_1}{dt}\right\rvert_0 = \boldsymbol\omega_{10} \times \mathbf i_1$ (same for $\mathbf j_1$, $\mathbf k_1$) | Poisson: a unit vector only rotates [Notes Eqs. 3.3–3.5, Slide 14] |
| $\left.\dfrac{d\mathbf b}{dt}\right\rvert_0 = \left.\dfrac{d\mathbf b}{dt}\right\rvert_1 + \boldsymbol\omega_{10} \times \mathbf b$ | the bracket is the derivative seen from $S_1$ [Notes Eq. 3.8] |

Consequence: $\boldsymbol\alpha_{10} = \dot{\boldsymbol\omega}_{10}\rvert_0 = \dot{\boldsymbol\omega}_{10}\rvert_1$ because $\boldsymbol\omega_{10} \times \boldsymbol\omega_{10} = \mathbf 0$ [Notes Eq. 3.9].

### Table: Composition of angular motions
| Result | Formula |
| --- | --- |
| velocities add | $\boldsymbol\omega_{20} = \boldsymbol\omega_{21} + \boldsymbol\omega_{10}$ [Notes Eq. 3.14] |
| accelerations do not | $\boldsymbol\alpha_{20} = \boldsymbol\alpha_{21} + \boldsymbol\omega_{10} \times \boldsymbol\omega_{21} + \boldsymbol\alpha_{10}$ [Notes Eq. 3.15] |
| inverse | $\boldsymbol\omega_{01} = -\boldsymbol\omega_{10}$, $\boldsymbol\alpha_{01} = -\boldsymbol\alpha_{10}$ |
| simple rotation | $\psi(t)$ about $\mathbf k_0$: $\boldsymbol\omega_{10} = \dot\psi\,\mathbf k_0$ [Slide 16] |
| Euler 3-1-3 | $\boldsymbol\omega_{30} = \dot\psi\,\mathbf k_0 + \dot\theta\,\mathbf i_1 + \dot\varphi\,\mathbf k_2$ [Slides 20–21] |

The $\boldsymbol\omega_{10} \times \boldsymbol\omega_{21}$ term comes from differentiating $\boldsymbol\omega_{21}$ (known in $S_1$) from $S_0$ with the Coriolis theorem.

### Derivation: Relative velocity and acceleration
In short: differentiate $\mathbf r_0^P = \mathbf r_0^A + \mathbf r_1^P$ twice in $S_0$, applying the Coriolis theorem to every vector known in $S_1$.

| Step | Why |
| --- | --- |
| $\mathbf r_0^P = \mathbf r_0^A + \mathbf r_1^P$ | vector chain $\overrightarrow{OA} + \overrightarrow{AP}$ [Notes Eq. 3.16] |
| $\mathbf v_0^P = \mathbf v_0^A + \mathbf v_1^P + \boldsymbol\omega_{10} \times \mathbf r_1^P$ | Coriolis theorem on $\mathbf r_1^P$ [Notes Eq. 3.26] |
| $\left.\dfrac{d\mathbf v_1^P}{dt}\right\rvert_0 = \mathbf a_1^P + \boldsymbol\omega_{10} \times \mathbf v_1^P$ | Coriolis theorem on $\mathbf v_1^P$ |
| $\left.\dfrac{d}{dt}(\boldsymbol\omega_{10} \times \mathbf r_1^P)\right\rvert_0 = \boldsymbol\alpha_{10} \times \mathbf r_1^P + \boldsymbol\omega_{10} \times (\mathbf v_1^P + \boldsymbol\omega_{10} \times \mathbf r_1^P)$ | product rule, then Coriolis on $\mathbf r_1^P$ |
| $\mathbf a_0^P = \mathbf a_0^A + \mathbf a_1^P + \boldsymbol\alpha_{10} \times \mathbf r_1^P + \boldsymbol\omega_{10} \times (\boldsymbol\omega_{10} \times \mathbf r_1^P) + 2\boldsymbol\omega_{10} \times \mathbf v_1^P$ | the two $\boldsymbol\omega_{10} \times \mathbf v_1^P$ make the Coriolis term [Notes Eq. 3.27] |

Names: $\mathbf a_0^A$ origin, $\mathbf a_1^P$ relative, $\boldsymbol\alpha \times \mathbf r$ Euler, $\boldsymbol\omega \times (\boldsymbol\omega \times \mathbf r) = -\omega^2\mathbf r_\perp$ centripetal, $2\boldsymbol\omega \times \mathbf v_1^P$ Coriolis. Pure translation: $\mathbf a_0^P = \mathbf a_0^A + \mathbf a_1^P$.

### Table: Inertia forces in a non-inertial frame
$m\,\mathbf a_1^P = \mathbf F + \mathbf F_i$ [Notes Eq. 4.63], with $\mathbf F_i = -m(\mathbf a_0^P - \mathbf a_1^P)$:

| Term | Force | Potential, work |
| --- | --- | --- |
| origin | $-m\,\mathbf a_0^A$ | $V_1 = m\,\mathbf a_0^A\cdot\mathbf r_1^P$ if $\mathbf a_0^A$ is constant |
| Euler | $-m\,\boldsymbol\alpha_{10} \times \mathbf r_1^P$ | no potential |
| centrifugal | $-m\,\boldsymbol\omega_{10} \times (\boldsymbol\omega_{10} \times \mathbf r_1^P) = m\omega^2\mathbf r_\perp$ | $V_1 = -\tfrac12m\omega^2r_\perp^2$ if $\boldsymbol\omega_{10}$ is constant |
| Coriolis | $-2m\,\boldsymbol\omega_{10} \times \mathbf v_1^P$ | never works: $\perp \mathbf v_1^P$ |

$\mathbf r_\perp$ is the component of $\mathbf r_1^P$ perpendicular to the rotation axis through $A$. Energy in $S_1$: $E_1 = \tfrac12m(v_1^P)^2 + V - \tfrac12m\omega^2r_\perp^2$ is conserved if $\mathbf a_0^A = \mathbf 0$, $\boldsymbol\omega_{10}$ constant, actual forces conservative and constraints fixed in $S_1$ [Slide 29].

### Algorithm: Relative-motion problem
1. Choose $S_1$ attached to the moving body (tube, disc, platform) so that the particle's motion in $S_1$ is simple.
2. Write $\boldsymbol\omega_{10}$, $\boldsymbol\alpha_{10}$, $\mathbf a_0^A$ in $\mathcal B_1$; deduce $[{}_0R_1]$ from the drawing.
3. Relative kinematics: $\mathbf r_1^P$, $\mathbf v_1^P$, $\mathbf a_1^P$ in $\mathcal B_1$.
4. Either absolute route ($m\mathbf a_0^P = \mathbf F$ with the composition formula) or relative route ($m\mathbf a_1^P = \mathbf F + \mathbf F_i$): both give the same equations.
5. Project: the directions free for the particle give its equation of motion; the constrained directions give the reactions.
6. Checks: $\Omega = 0$ recovers the fixed-frame problem; units of every term m/s²; $E_1$ conserved if the conditions above hold.

### Trap: Relative-motion traps
- $\mathbf v_1^P$ is the velocity seen from $S_1$, not the component of $\mathbf v_0^P$ in $\mathcal B_1$.
- $\boldsymbol\alpha_{10} \neq \mathbf 0$ whenever the direction of $\boldsymbol\omega_{10}$ changes, even with constant magnitude.
- The centrifugal force points away from the axis, not away from $A$.
- Both routes at once: inertia forces belong only to the equation written in $S_1$.

## Pocket prerequisites
Pages: Theory index=teoria/index.html

### Prerequisite: Vector algebra
| Identity | Use |
| --- | --- |
| $\mathbf a \times (\mathbf b \times \mathbf c) = \mathbf b\,(\mathbf a\cdot\mathbf c) - \mathbf c\,(\mathbf a\cdot\mathbf b)$ | centripetal term $\boldsymbol\omega \times (\boldsymbol\omega \times \mathbf r) = \boldsymbol\omega(\boldsymbol\omega\cdot\mathbf r) - \omega^2\mathbf r$ |
| $\mathbf a \times \mathbf b = -\mathbf b \times \mathbf a$, $\mathbf a \times \mathbf a = \mathbf 0$ | order in torques and Coriolis |
| $\mathbf i \times \mathbf j = \mathbf k,\ \mathbf j \times \mathbf k = \mathbf i,\ \mathbf k \times \mathbf i = \mathbf j$ | cyclic order of a right-handed basis |
| $\mathbf a\cdot(\mathbf b \times \mathbf c) = \det[\mathbf a, \mathbf b, \mathbf c]$ | torsion, volumes, coplanarity |
| $\dfrac{d}{dt}(\mathbf a \times \mathbf b) = \dot{\mathbf a} \times \mathbf b + \mathbf a \times \dot{\mathbf b}$ | angular momentum, relative kinematics |

### Prerequisite: Calculus tools
- Chain rule: $\dfrac{d}{dt}f(\theta(t)) = f'(\theta)\,\dot\theta$, so $\dfrac{d}{dt}\cos\theta = -\dot\theta\sin\theta$ and $\dfrac{d}{dt}(\dot\theta^2) = 2\dot\theta\ddot\theta$.
- Integrating $\ddot\theta = g(\theta)$ once: $\ddot\theta = \dfrac{d}{d\theta}\big(\tfrac12\dot\theta^2\big)$, so $\tfrac12\dot\theta^2 - \tfrac12\dot\theta_0^2 = \int_{\theta_0}^{\theta}g(s)\,ds$.
- Barrow's rule: $\int_a^b f(x)\,dx = F(b) - F(a)$; write the antiderivative before substituting the limits.
- Small angles: $\sin\theta \approx \theta$, $\cos\theta \approx 1 - \theta^2/2$, $\tan\theta \approx \theta$.

### Prerequisite: Trigonometry
- $\cos(\theta - \pi/2) = \sin\theta$, $\sin(\theta - \pi/2) = -\cos\theta$: relating an angle from the vertical to the polar angle.
- $\sin(a \pm b) = \sin a\cos b \pm \cos a\sin b$, $\cos(a \pm b) = \cos a\cos b \mp \sin a\sin b$.
- $\cos^2\theta = \tfrac12(1 + \cos 2\theta)$, $\sin\theta\cos\theta = \tfrac12\sin 2\theta$.
- In every right triangle: adjacent $=$ hypotenuse $\times\cos$, opposite $=$ hypotenuse $\times\sin$.

### Prerequisite: Units and dimensions
| Quantity | SI unit |
| --- | --- |
| force, $m\mathbf a$, $m\omega^2r$, $m\omega v$ | $\mathrm{N = kg\,m\,s^{-2}}$ |
| energy, work, $V_0$, $\tfrac12mv^2$ | $\mathrm{J = N\,m}$ |
| power $\mathbf F\cdot\mathbf v$ | $\mathrm{W = J\,s^{-1}}$ |
| angular momentum $\mathbf r \times m\mathbf v$; torque | $\mathrm{kg\,m^2\,s^{-1}}$; $\mathrm{N\,m}$ |
| $h = r^2\dot\theta$; $\mu = GM$ | $\mathrm{m^2\,s^{-1}}$; $\mathrm{m^3\,s^{-2}}$ |
| $\omega$, $\alpha$, curvature $\kappa$ | $\mathrm{s^{-1}}$, $\mathrm{s^{-2}}$, $\mathrm{m^{-1}}$ |
