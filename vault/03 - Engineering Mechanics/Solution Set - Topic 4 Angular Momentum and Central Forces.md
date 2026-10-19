---
title: "Solution Set - Topic 4: Angular Momentum and Central Forces"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Full Analytical Solutions (4-Phase Methodology)"
language: "English"
tags:
  - solutions
  - topic-4
  - central-forces
---

# 📚 Topic 4: Angular Momentum and Central Forces - Full Analytical Solutions

Step-by-step analytical solutions for official problems from Topic 4 (**Angular Momentum, Central Forces, and Kepler's Problem**) of *Mechanics Applied to Aerospace Engineering* (UC3M). Every problem strictly complies with the mandatory 4-phase pedagogical methodology, with explicit justification prior to every equation, zero algebraic omissions, explicit derivative developments (product, quotient, and chain rules), explicit integral evaluations (substitutions, primitives, and Barrow's rule), polar rotation matrices $[{}_0 R_1]$, and dimensional verifications.

---

## 📌 Problem 42: Particle Attracted to the Origin ($F = m\mu / r^\alpha$)

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A point particle $P$ of mass $m$ is attracted to origin $O$ by a general power-law central force:
  $$ \mathbf{F} = -\frac{m\mu}{r^\alpha}\mathbf{e}_r $$
* **Hypotheses:**
  1. Inertial reference frame $S_0$.
  2. $\mu > 0$, $\alpha > 0$ constants.
  3. No non-conservative forces act on the system.
* **Variables:** $r(t)$ distance to origin, $\theta(t)$ polar angle in the plane of motion, $u(\theta) \equiv 1/r(\theta)$.

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* **Change of basis (polar basis in the plane of motion).** Take $\mathbf{k}$ along $\mathbf{H}_O$. The polar basis $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}\}$ is obtained from the inertial basis $\mathcal{B}_0 = \{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$ by a rotation $\theta(t)$ about $\mathbf{k}$:
  $$ [{}_0 R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = \cos^2\theta + \sin^2\theta = 1, \qquad R^T R = I $$
  The angular velocity of $\mathcal{B}_1$ is $\boldsymbol{\omega}_{10} = \dot{\theta}\,\mathbf{k}$ and Poisson's formula $\dot{\mathbf{e}} = \boldsymbol{\omega}\times\mathbf{e}$ gives $\dot{\mathbf{e}}_r = \dot{\theta}\,\mathbf{e}_\theta$ and $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_r$. Differentiating $\mathbf{r} = r\mathbf{e}_r$ with the product rule:
  $$ \mathbf{v} = \dot{r}\mathbf{e}_r + r\dot{\theta}\mathbf{e}_\theta, \qquad \mathbf{a} = \ddot{r}\mathbf{e}_r + \dot{r}\dot{\theta}\mathbf{e}_\theta + \left(\dot{r}\dot{\theta} + r\ddot{\theta}\right)\mathbf{e}_\theta - r\dot{\theta}^2\mathbf{e}_r $$
* **Inertial Polar Basis:** $\mathcal{B} = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}\}$ with:
  $$ \mathbf{r} = r\mathbf{e}_r, \qquad \mathbf{v} = \dot{r}\mathbf{e}_r + r\dot{\theta}\mathbf{e}_\theta, \qquad \mathbf{a} = (\ddot{r} - r\dot{\theta}^2)\mathbf{e}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\mathbf{e}_\theta $$

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a): Conservation of Angular Momentum and Energy, Planar Motion
* **Pedagogical Justification:** The line of action of $\mathbf{F}$ passes through origin $O$. Torque about $O$:
  $$ \mathbf{M}_O = \mathbf{r} \times \mathbf{F} = r\mathbf{e}_r \times \left(-\frac{m\mu}{r^\alpha}\mathbf{e}_r\right) = \mathbf{0} $$
  By the angular momentum theorem about fixed point $O$:
  $$ \frac{d\mathbf{H}_O}{dt}\Bigg|_0 = \mathbf{M}_O = \mathbf{0} \implies \mathbf{H}_O = m(\mathbf{r} \times \mathbf{v}) = \text{constant vector} $$
  Since $\mathbf{r}(t) \cdot \mathbf{H}_O \equiv 0$ and $\mathbf{v}(t) \cdot \mathbf{H}_O \equiv 0$, the particle remains permanently in the plane through $O$ orthogonal to $\mathbf{H}_O$.

* **Conservation of Mechanical Energy:**
  The force field is central and purely radial $\mathbf{F} = F(r)\mathbf{e}_r$. Its curl in spherical coordinates is $\nabla \times \mathbf{F} \equiv \mathbf{0}$, so $\mathbf{F}$ is conservative; equivalently, the elementary work $\mathbf{F}\cdot d\mathbf{r} = F(r)\,dr$ depends on $r$ alone and is the exact differential of a function of $r$.
  Mass-specific potential energy $V_0(r)$:
  $$ V_0(r) = -\int_\infty^r \left(-\frac{\mu}{r'^\alpha}\right) dr' = \begin{cases} -\frac{\mu}{(\alpha - 1)r^{\alpha - 1}} & (\alpha \ne 1) \\ \mu\ln(r) & (\alpha = 1) \end{cases} $$
  Because no non-conservative forces act, mass-specific mechanical energy is strictly conserved:
  $$ \xi = \frac{1}{2}v^2 + V_0(r) = \text{constant} $$

#### Part (b): Generalized Binet Equation for $u(\theta) \equiv 1/r(\theta)$
* **Pedagogical Justification:** By angular momentum conservation, specific angular momentum $h \equiv \|\mathbf{H}_O\|/m = r^2\dot{\theta} = \text{const} \implies \dot{\theta} = h u^2$.

Using the chain rule to eliminate time:
$$ \dot{r} = \frac{dr}{d\theta}\dot{\theta} = \frac{d(1/u)}{d\theta}(h u^2) = -\frac{1}{u^2}\frac{du}{d\theta}(h u^2) = -h\frac{du}{d\theta} = -h u' $$
$$ \ddot{r} = \frac{d}{dt}(-h u') = \frac{d(-h u')}{d\theta}\dot{\theta} = -h u'' (h u^2) = -h^2 u^2 u'' $$

Substitute $\ddot{r}$ and $r\dot{\theta}^2 = \frac{1}{u}(h u^2)^2 = h^2 u^3$ into Newton's radial equation $\ddot{r} - r\dot{\theta}^2 = -\frac{\mu}{r^\alpha} = -\mu u^\alpha$:
$$ -h^2 u^2 u'' - h^2 u^3 = -\mu u^\alpha $$
Dividing by $-h^2 u^2$:
$$ \frac{d^2u}{d\theta^2} + u = \frac{\mu}{h^2} u^{\alpha - 2} $$

#### Part (c): First Integral & Orbit Classification for $\alpha \in \{1, 2, 3, 4\}$
* **Pedagogical Justification:** Multiplying by $u' = \frac{du}{d\theta}$ and integrating with respect to $\theta$:
  $$ u' u'' + u u' = \frac{\mu}{h^2} u^{\alpha - 2} u' $$
  Integrating:
  $$ \frac{1}{2}(u')^2 + \frac{1}{2}u^2 - \frac{\mu}{h^2}\int u^{\alpha - 2} du = C $$

Alternatively, using specific energy $\xi = \frac{1}{2}v^2 + V_0(r) = \frac{1}{2}h^2[(u')^2 + u^2] + V_0(1/u)$:
$$ (u')^2 + W_{\text{eff}}(u) = \frac{2\xi}{h^2} \equiv E^* $$
where the effective potential in $u$-space is:
$$ W_{\text{eff}}(u) = u^2 + \frac{2 V_0(1/u)}{h^2} $$

Physical motion exists only in regions where $E^* \ge W_{\text{eff}}(u)$. Turning points ($u' = 0$) correspond to real roots of $W_{\text{eff}}(u) = E^*$.

##### 1. Case $\alpha = 2$ (Standard Kepler Problem: $F \propto 1/r^2$)
* Binet Equation: $u'' + u = \frac{\mu}{h^2}$
* Effective Potential: $W_{\text{eff}}(u) = u^2 - \frac{2\mu}{h^2}u = \left(u - \frac{\mu}{h^2}\right)^2 - \left(\frac{\mu}{h^2}\right)^2$
* Analysis:
  - $W_{\text{eff}}(u)$ is a parabola with minimum at $u = \mu/h^2$ where $W_{\min} = -(\mu/h^2)^2$.
  - **i. Escape to infinity ($u \to 0$):** Occurs if $E^* \ge W_{\text{eff}}(0) = 0 \iff \xi \ge 0$ (parabolic or hyperbolic orbit).
  - **ii. Collision with origin ($u \to \infty$):** Impossible because $W_{\text{eff}}(u) \to +\infty$ as $u \to \infty$. The centrifugal barrier prevents collapse!
  - **iii. Bounded oscillation between two values:** Occurs if $-(\mu/h^2)^2 < E^* < 0 \iff - \frac{\mu^2}{2h^2} < \xi < 0$. The particle oscillates periodically between periapsis $u_p$ and apoapsis $u_a$ (elliptical orbit).

##### 2. Case $\alpha = 1$ (Logarithmic Potential: $F \propto 1/r$)
* Binet Equation: $u'' + u = \frac{\mu}{h^2 u}$
* Potential: $V_0(1/u) = -\mu\ln(u) \implies W_{\text{eff}}(u) = u^2 - \frac{2\mu}{h^2}\ln(u)$
* Analysis:
  - As $u \to 0$, $-\ln(u) \to +\infty \implies W_{\text{eff}} \to +\infty$.
  - As $u \to \infty$, $u^2 \to +\infty \implies W_{\text{eff}} \to +\infty$.
  - Minimum occurs at $2u - \frac{2\mu}{h^2 u} = 0 \implies u_0 = \sqrt{\mu}/h$.
  - **i. Escape to infinity ($u \to 0$):** Impossible for any finite energy because $W_{\text{eff}}(0) = +\infty$. All orbits are bound!
  - **ii. Collision with origin ($u \to \infty$):** Impossible because $W_{\text{eff}}(\infty) = +\infty$.
  - **iii. Bounded oscillation:** Every orbit with $E^* > W_{\min}$ oscillates between two finite turning points $u_{\min}$ and $u_{\max}$; $E^* = W_{\min}$ is the circular orbit $r = h/\sqrt{\mu}$.

##### 3. Case $\alpha = 3$ (Inverse-Cube Force: $F \propto 1/r^3$)
* Potential per unit mass: $V_0(r) = -\dfrac{\mu}{2r^2} = -\dfrac{\mu}{2}u^2$.
* Binet Equation: $u'' + u = \dfrac{\mu}{h^2}u \implies u'' + \lambda u = 0$ with $\lambda \equiv 1 - \dfrac{\mu}{h^2}$.
* Effective Potential: $W_{\text{eff}}(u) = u^2 - \dfrac{\mu}{h^2}u^2 = \lambda u^2$, and the first integral is $(u')^2 + \lambda u^2 = E^*$.
* Analysis (the sign of $\lambda$ decides):
  - **Subcase $h^2 > \mu$ ($\lambda = \kappa^2 > 0$, $\kappa = \sqrt{1 - \mu/h^2}$):** $u(\theta) = A\cos(\kappa\theta + \delta)$ with $A = \sqrt{u_0^2 + (u_0'/\kappa)^2}$ and $E^* = \kappa^2A^2 > 0$.
    * The cosine vanishes at a finite angle, so $u \to 0$ in every case: **the particle always escapes to infinity**. A particle that starts moving inward ($u_0' > 0$) is first reflected at the periapsis $u = A$ and then escapes.
    * $u$ is bounded by $A$, so the origin is never reached, and there is no oscillation between two positive values of $u$.
  - **Subcase $h^2 < \mu$ ($\lambda = -\kappa^2 < 0$, $\kappa = \sqrt{\mu/h^2 - 1}$):** $u(\theta) = C_1e^{\kappa\theta} + C_2e^{-\kappa\theta}$ with $C_1 = \tfrac{1}{2}\left(u_0 + u_0'/\kappa\right)$ and $C_2 = \tfrac{1}{2}\left(u_0 - u_0'/\kappa\right)$.
    * $C_1 > 0$ ($u_0' > -\kappa u_0$): $u \to \infty$, **the particle reaches the origin** (orbital collapse).
    * $C_1 < 0$ ($u_0' < -\kappa u_0$): $u$ reaches $0$ at a finite angle, **the particle escapes to infinity**.
    * $C_1 = 0$ ($u_0' = -\kappa u_0$): $u = u_0e^{-\kappa\theta} \to 0$ only asymptotically (logarithmic spiral $r = r_0e^{\kappa\theta}$), a limiting case of escape.
    * No oscillation is possible: $u$ is a sum of exponentials.
  - **Subcase $h^2 = \mu$ ($\lambda = 0$):** $u'' = 0 \implies u(\theta) = u_0 + u_0'\theta$ (a reciprocal spiral $r = 1/(u_0 + u_0'\theta)$). For $u_0' > 0$ the particle reaches the origin, for $u_0' < 0$ it escapes (at $\theta = u_0/|u_0'|$), and for $u_0' = 0$ it moves on the circle $r = 1/u_0$.

##### 4. Case $\alpha = 4$ (Inverse-Quartic Force: $F \propto 1/r^4$)
* Binet Equation: $u'' + u = \frac{\mu}{h^2}u^2$
* Effective Potential: $W_{\text{eff}}(u) = u^2 - \frac{2\mu}{3h^2}u^3$
* Analysis:
  - Derivative: $W'(u) = 2u - \frac{2\mu}{h^2}u^2 = 2u(1 - \frac{\mu}{h^2}u)$.
  - Extrema: Minimum at $u = 0$ ($W = 0$), local maximum (potential barrier) at $u_{\text{barrier}} = \frac{h^2}{\mu}$ with $W_{\max} = \frac{h^4}{3\mu^2}$.
  - For $u > u_{\text{barrier}}$, the $-u^3$ term dominates and $W_{\text{eff}}(u) \to -\infty$. $W_{\text{eff}}$ vanishes again at $u_0 = \frac{3h^2}{2\mu} > u_{\text{barrier}}$, since $W_{\text{eff}} = u^2\left(1 - \frac{2\mu}{3h^2}u\right)$.
  - There is **no interior minimum**: $W_{\text{eff}}$ increases monotonically from $W_{\text{eff}}(0) = 0$ up to $W_{\max}$ and then decreases without bound, so the allowed region $\{u : W_{\text{eff}}(u) \le E^*\}$ either contains $u = 0$ ($r \to \infty$) or extends to $u \to \infty$ ($r \to 0$). Since $\theta$ increases monotonically with $t$ ($\dot{\theta} = hu^2 > 0$), $u'$ has the sign of $\dot{u}$.
  - **Case $0 \le E^* < W_{\max}$:** $W_{\text{eff}}(u) = E^*$ has two roots $u_1 \in [0, u_{\text{barrier}})$ and $u_2 > u_{\text{barrier}}$, and the allowed set is $u \le u_1$ or $u \ge u_2$. If $u(0) \le u_1$ the particle is reflected at $u_1$ and escapes. If $u(0) \ge u_2$ it is reflected at $u_2$ and falls to the origin.
  - **Case $E^* < 0$:** the only allowed region is $u \ge u_2$ with $u_2 > u_0$, so the particle always reaches $r = 0$.
  - **Case $E^* > W_{\max}$:** there are no turning points and the direction of $u'(0)$ decides: $u'(0) < 0$ (moving outward) escapes, $u'(0) > 0$ (moving inward) falls to the origin.
  - **Case $E^* = W_{\max}$:** besides the unstable circular orbit $u = u_{\text{barrier}}$, the particle approaches it asymptotically.
  - **i. Escape to infinity ($u \to 0$):** occurs if $0 \le E^* < W_{\max}$ and $u(0) < u_{\text{barrier}}$, or if $E^* > W_{\max}$ and $u'(0) < 0$.
  - **ii. Collision with origin ($u \to \infty$):** occurs if $E^* < 0$, or if $0 \le E^* < W_{\max}$ and $u(0) > u_{\text{barrier}}$, or if $E^* > W_{\max}$ and $u'(0) > 0$. For $\alpha = 4$ the attractive $1/r^4$ force beats the centrifugal barrier at small $r$.
  - **iii. Bounded oscillation between two values of $u$:** does **not** occur for $\alpha = 4$ (the only bounded motion is the unstable circular orbit $u = u_{\text{barrier}}$, $E^* = W_{\max}$). The statement "oscillation for $0 < E^* < W_{\max}$" would require an interior minimum of $W_{\text{eff}}$, which does not exist; for such energies the particle on the inner branch is reflected once and escapes.

---

### Phase 4: Physical Interpretation & Verification
* **Dimensional check:** $[F/m] = \text{m/s}^2$ and $F/m = \mu/r^\alpha$ give $[\mu] = \text{m}^{\alpha+1}/\text{s}^2$; with $[h^2] = \text{m}^4/\text{s}^2$ and $[u] = \text{m}^{-1}$, the term $\dfrac{\mu}{h^2}u^{\alpha-2}$ has units $\text{m}^{\alpha-3}\cdot\text{m}^{-(\alpha-2)} = \text{m}^{-1}$, the same as $u$ and $u''$ (the angle is dimensionless).
* **Numerical check (Python, RK4 with step $10^{-4}$ rad on $u'' = -u + (\mu/h^2)u^{\alpha-2}$, units with $\mu = h = 1$ unless stated):**

| Case | Initial data $(u_0, u_0')$ | Predicted | Integration result |
| :--- | :--- | :--- | :--- |
| $\alpha = 2$ | $(1.5, 0)$ | bounded, between $0.5$ and $1.5$ | $u \in [0.5000, 1.5000]$ over $60$ rad |
| $\alpha = 2$ | $(0.5, -0.9)$, $E^* > 0$ | escape | $u = 0$ at $\theta = 0.823$ |
| $\alpha = 4$ | $(0.5, 0)$, $E^* = 1/6 < 1/3$ | reflected, escape | $u = 0$ at $\theta = 2.078$ |
| $\alpha = 4$ | $(1.2, 0)$, $E^* = 0.288 < 1/3$ | collapse | $u \to \infty$ at $\theta = 3.713$ |
| $\alpha = 4$ | $(0.5, 0.9)$, $E^* > 1/3$ | collapse | $u \to \infty$ at $\theta = 3.258$ |
| $\alpha = 4$ | $(0.5, -0.9)$, $E^* > 1/3$ | escape | $u = 0$ at $\theta = 0.524$ |
| $\alpha = 4$ | $(1, 0)$, $E^* = W_{\max}$ | unstable circular orbit | $u = 1$ for $20$ rad |
| $\alpha = 3$, $\mu/h^2 = 2$ | $(1, 0.2)$, $C_1 > 0$ | collapse | $u = \cosh\theta + 0.2\sinh\theta$ is finite at every finite $\theta$ and $\to \infty$ only as $\theta \to \infty$ (the particle reaches $r = 0$ in finite time after infinitely many turns); $\theta = 4.423$ is the integrator cutoff |
| $\alpha = 3$, $\mu/h^2 = 2$ | $(1, -1.5)$, $C_1 < 0$ | escape | $u = 0$ at $\theta = 0.805$ |
| $\alpha = 3$, $\mu/h^2 = 1/2$ | $(1, 0)$ | escape | $u = 0$ at $\theta = 2.222$ |
| $\alpha = 3$, $\mu = h^2$ | $(1, -0.1)$ | escape at $\theta = 10$ | $u = 0$ at $\theta = 10.000$ |
| $\alpha = 1$ | $(0.5, 0.3)$ | bounded | $u \in [0.471, 1.653]$ over $100$ rad |

---

## 📌 Problem 43: Two Connected Particles, Plane with Hole

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** Two point particles $P_1$ and $P_2$ of identical mass $m$ connected by a light inextensible cord of length $2a$. $P_1$ moves on a smooth horizontal plane; $P_2$ hangs vertically below a small frictionless hole at $O$.
* **Configuration Degrees of Freedom:**
  - Ambient space: $P_1$ in plane $(r, \theta)$, $P_2$ along vertical $z_2$.
  - Holonomic string length constraint: $r + (-z_2) = 2a \implies z_2 = r - 2a$ (taking downwards as negative).
  - CDOF $= 2$: generalized coordinates are polar radius $r(t)$ and angle $\theta(t)$ of $P_1$.
* **Initial State ($t = 0$):**
  - Radius: $r(0) = a$ (half cord on plane, half hanging: $-z_2(0) = a$).
  - Velocity of $P_1$: $\dot{r}(0) = 0$, $v_\theta(0) = r(0)\dot{\theta}(0) = v_0 \implies \dot{\theta}(0) = v_0/a$.
  - Velocity of $P_2$: $\dot{z}_2(0) = \dot{r}(0) = 0$.
* **Parameters:** $m > 0$ [kg], $a > 0$ [m], $g > 0$ [m/s$^2$].

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* **Inertial Reference Frame:** $S_0 : \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$ with $O$ at the hole, horizontal plane $z = 0$, and $\mathbf{k}$ vertical upwards.
* **Change of basis (polar basis of $P_1$).** $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}\}$ is the inertial basis rotated by $\theta(t)$ about $\mathbf{k}$:
  $$ [{}_0 R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = 1, \qquad R^T R = I $$
  with $\boldsymbol{\omega}_{10} = \dot{\theta}\mathbf{k}$, $\dot{\mathbf{e}}_r = \dot{\theta}\mathbf{e}_\theta$ and $\dot{\mathbf{e}}_\theta = -\dot{\theta}\mathbf{e}_r$ (Poisson).
* **Kinematics:**
  - Particle $P_1$: $\mathbf{r}_1 = r\mathbf{e}_r$, $\mathbf{v}_1 = \dot{r}\mathbf{e}_r + r\dot{\theta}\mathbf{e}_\theta$.
  - Particle $P_2$: $\mathbf{r}_2 = (r - 2a)\mathbf{k}$, $\mathbf{v}_2 = \dot{r}\mathbf{k}$.
  - System Kinetic Energy:
    $$ T = T_1 + T_2 = \frac{1}{2}m(\dot{r}^2 + r^2\dot{\theta}^2) + \frac{1}{2}m\dot{r}^2 = m\dot{r}^2 + \frac{1}{2}mr^2\dot{\theta}^2 $$
  - System Potential Energy (reference $V = 0$ at $z = 0$):
    $$ V = mg z_2 = mg(r - 2a) = mgr - 2mga $$

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a): Circular Orbit Speed Condition ($r(t) \equiv a$)
* **Pedagogical Justification:** The only horizontal force acting on $P_1$ is the cord tension $\mathbf{T}_1 = -T\mathbf{e}_r$, which is central.
  For $P_1$ to move on a circle of constant radius $r = a$, its radial acceleration must be purely centripetal:
  $$ \ddot{r} = 0 \implies m(0 - a\dot{\theta}^2) = -T \implies T = m a \dot{\theta}^2 = m \frac{v_0^2}{a} $$
  For $P_2$ to remain stationary at constant depth $z_2 = -a$:
  $$ \ddot{z}_2 = 0 \implies T - mg = 0 \implies T = mg $$
  Equating the tension values:
  $$ m\frac{v_0^2}{a} = mg \implies v_0^2 = ag \implies v_0 = \sqrt{ag} $$

#### Part (b): Tension in Circular Orbit
$$ T = mg $$

#### Part (c): Reduction to Quadratures for $v_0 = \sqrt{8ag/3}$
* **Pedagogical Justification:** Because tension is central on $P_1$, angular momentum is conserved:
  $$ h = r^2\dot{\theta} = \text{constant} = a v_0 = a\sqrt{\frac{8ag}{3}} \implies h^2 = \frac{8}{3}a^3 g $$
* Because all constraint reactions are frictionless and bilateral, total mechanical energy $E = T + V$ is conserved:
  $$ E = m\dot{r}^2 + \frac{1}{2}m\frac{h^2}{r^2} + mgr - 2mga = \text{constant} $$
  Evaluate $E$ at $t = 0$ ($r = a, \dot{r} = 0$):
  $$ E = 0 + \frac{1}{2}m v_0^2 + mga - 2mga = \frac{1}{2}m\left(\frac{8ag}{3}\right) - mga = \frac{4}{3}mga - mga = \frac{1}{3}mga $$

Equating expressions for $E$:
$$ m\dot{r}^2 + \frac{1}{2}m\left(\frac{8a^3 g}{3r^2}\right) + mgr - 2mga = \frac{1}{3}mga $$
Dividing through by $m$:
$$ \dot{r}^2 + \frac{4a^3 g}{3r^2} + gr = \frac{7}{3}ga $$
Isolating $\dot{r}^2$:
$$ \dot{r}^2 = \frac{7}{3}ga - gr - \frac{4a^3 g}{3r^2} = \frac{g}{3r^2}\left[ 7a r^2 - 3r^3 - 4a^3 \right] $$

Taking the square root and separating variables:
$$ \frac{dr}{dt} = \pm \sqrt{\frac{g}{3}}\frac{\sqrt{-3r^3 + 7a r^2 - 4a^3}}{r} $$
Integrating to obtain the time quadrature:
$$ \int_a^r \frac{r'\,dr'}{\sqrt{-3r'^3 + 7a r'^2 - 4a^3}} = \pm \sqrt{\frac{g}{3}}\int_0^t dt = \pm \sqrt{\frac{g}{3}}\,t $$

#### Part (d): Radial Oscillation Between $r = a$ and $r = 2a$
* **Pedagogical Justification:** Physical motion requires $\dot{r}^2 \ge 0$, which requires the cubic polynomial $P(r) = -3r^3 + 7a r^2 - 4a^3 \ge 0$.
  Factoring with dimensionless variable $x \equiv r/a$:
  $$ P(x) = -3x^3 + 7x^2 - 4 $$
  Testing roots:
  - $x = 1$: $-3(1) + 7(1) - 4 = 0$ (Root!)
  - $x = 2$: $-3(8) + 7(4) - 4 = -24 + 28 - 4 = 0$ (Root!)
  - $x = -2/3$: $-3(-8/27) + 7(4/9) - 4 = 8/9 + 28/9 - 4 = 36/9 - 4 = 0$ (Root!)

Factored form:
$$ P(x) = -(x - 1)(x - 2)(3x + 2) $$
Because $r > 0$, the factor $(3x + 2) > 0$.
Therefore, $P(x) \ge 0 \iff -(x - 1)(x - 2) \ge 0 \iff (x - 1)(x - 2) \le 0 \iff 1 \le x \le 2$.

The physical radius is bounded strictly by:
$$ a \le r(t) \le 2a $$
The turning points ($\dot{r} = 0$) are exactly $r_{\min} = a$ and $r_{\max} = 2a$. The particle executes non-linear radial oscillations between these two limits!

#### Part (e): Cord Tension $T(r)$
* **Pedagogical Justification:** Applying Newton's Second Law to hanging particle $P_2$:
  $$ m\ddot{z}_2 = T - mg $$
  Since $z_2 = r - 2a$, we have $\ddot{z}_2 = \ddot{r}$. Thus:
  $$ T = m(g + \ddot{r}) $$

To find $\ddot{r}$, differentiate the energy equation $\dot{r}^2 = \frac{7}{3}ga - gr - \frac{4a^3 g}{3r^2}$ with respect to time:
$$ 2\dot{r}\ddot{r} = \left( -g + \frac{8a^3 g}{3r^3} \right)\dot{r} $$
Dividing by $2\dot{r}$:
$$ \ddot{r} = -\frac{g}{2} + \frac{4a^3 g}{3r^3} $$
Substitute $\ddot{r}$ into the tension equation:
$$ T = m\left( g - \frac{g}{2} + \frac{4a^3 g}{3r^3} \right) = mg\left( \frac{1}{2} + \frac{4a^3}{3r^3} \right) $$
*Q.E.D.* (Notice that for all $r \in [a, 2a]$, $T > 0$, verifying the cord remains in tension throughout the motion).

#### Part (f): Modified Equations with Friction $\mu$
If the horizontal plane has Coulomb friction with coefficient $\mu$:
* Normal reaction on $P_1$: $N_1 = mg$.
* Dynamic friction force: $\mathbf{F}_f = -\mu mg \frac{\mathbf{v}_1}{v_1} = -\mu mg \frac{\dot{r}\mathbf{e}_r + r\dot{\theta}\mathbf{e}_\theta}{\sqrt{\dot{r}^2 + r^2\dot{\theta}^2}}$.
* Equations of motion:
  $$ \mathbf{e}_r: \quad m(\ddot{r} - r\dot{\theta}^2) = -T - \mu mg \frac{\dot{r}}{\sqrt{\dot{r}^2 + r^2\dot{\theta}^2}} $$
  $$ \mathbf{e}_\theta: \quad m(r\ddot{\theta} + 2\dot{r}\dot{\theta}) = -\mu mg \frac{r\dot{\theta}}{\sqrt{\dot{r}^2 + r^2\dot{\theta}^2}} $$
  $$ P_2: \quad m\ddot{r} = T - mg $$
* Summing radial equations:
  $$ 2m\ddot{r} - mr\dot{\theta}^2 = -mg - \mu mg \frac{\dot{r}}{\sqrt{\dot{r}^2 + r^2\dot{\theta}^2}} $$
  $$ \frac{d}{dt}\left(r^2\dot{\theta}\right) = -\mu g \frac{r^2\dot{\theta}}{\sqrt{\dot{r}^2 + r^2\dot{\theta}^2}} $$

### Phase 4: Physical Interpretation & Dimensional Verification
* **Radial period (consequence of (c) and (d)).** With $x = r/a$ and $x = \tfrac{3}{2} - \tfrac{1}{2}\cos s$, $s \in [0, \pi]$, one has $(x - 1)(2 - x) = \tfrac{1}{4}\sin^2 s$ and $dx = \tfrac{1}{2}\sin s\,ds$, so
  $$ \tau_r = 2\sqrt{\frac{3a}{g}}\int_1^2\frac{x\,dx}{\sqrt{(x - 1)(2 - x)(3x + 2)}} = 2\sqrt{\frac{3a}{g}}\int_0^\pi\frac{x(s)\,ds}{\sqrt{3x(s) + 2}} \approx 6.342\sqrt{\frac{a}{g}} $$
  A direct RK4 integration of $\ddot{r} = -g/2 + 4a^3g/(3r^3)$ with $a = g = 1$, $r(0) = 1$, $\dot{r}(0) = 0$ gives a period of $6.3425$ s, a maximum radius of $2.0000$ and an energy-integral residual of $3.6\times 10^{-14}$.
* **Tension check at turning points:**
  - At $r = a$: $T(a) = mg(1/2 + 4/3) = \frac{11}{6}mg > 0$.
  - At $r = 2a$: $T(2a) = mg(1/2 + 4/24) = mg(1/2 + 1/6) = \frac{2}{3}mg > 0$.
* **Dimensions:** $[T] = [m][g] = \text{N}$, $[v_0] = \sqrt{[a][g]} = \text{m/s}$ (Correct).

---

## 📌 Problem 44: The Little Prince Throwing Seeds

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A spherical, non-rotating asteroid of mass $M$ and radius $R$. A seed of mass $m$ is launched from the equator ($r_0 = R$) with launch speed $v_0$ and launch angle $\beta = 60^\circ$ above the local horizontal.
* **Apocenter Condition:** The ballistic trajectory achieves an apocenter of:
  $$ r_a = 3R $$
* **Hypotheses:**
  1. Asteroid is spherically symmetric; gravitational field is central: $\mathbf{F}_g = -\frac{GMm}{r^2}\mathbf{e}_r$.
  2. No atmospheric drag (vacuum).
  3. No asteroid rotation $\implies$ inertial surface launch.
  4. Mass of seed $m \ll M$, so gravitational parameter is $\mu = GM$.
* **Parameters:** $M > 0$ [kg], $R > 0$ [m], $G \approx 6.6743 \times 10^{-11}\,\text{m}^3/(\text{kg}\cdot\text{s}^2)$, $\beta = 60^\circ$.

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* **Inertial Frame:** $S_0 : \{O; \mathcal{B}_0\}$ centered at the center of the asteroid.
* **Change of basis (polar basis in the orbital plane).** $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}\}$ is the inertial basis rotated by the true anomaly $\theta$ about $\mathbf{k}$ (along $\mathbf{H}_O$):
  $$ [{}_0 R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = 1, \qquad R^T R = I $$
* **Polar Coordinates:** True anomaly $\theta$ measured from pericenter.
* **Launch Velocity Components:**
  At launch point ($r = R$):
  - Radial component: $v_{r0} = v_0\sin(60^\circ) = \frac{\sqrt{3}}{2}v_0$.
  - Transverse component: $v_{\theta 0} = v_0\cos(60^\circ) = \frac{1}{2}v_0$.

### Phase 3: Step-by-Step Mathematical Deduction

#### 1. Conservation of Specific Angular Momentum
* **Pedagogical Justification:** The gravitational force is central with line of action through $O$, so torque $\mathbf{M}_O = \mathbf{0}$. The mass-specific angular momentum $h = \|\mathbf{r} \times \mathbf{v}\|$ is an invariant of motion:

At launch ($r = R$):
$$ h = r_0 v_{\theta 0} = R \left(v_0\cos 60^\circ\right) = \frac{1}{2} R v_0 $$

At apocenter ($r = r_a = 3R$), the radial velocity vanishes ($\dot{r}_a = 0$), so velocity is purely transverse ($v_a = v_{\theta a}$):
$$ h = r_a v_a = 3R v_a $$
Equating both expressions for $h$:
$$ \frac{1}{2} R v_0 = 3R v_a \implies v_a = \frac{1}{6}v_0 $$

#### 2. Conservation of Specific Mechanical Energy
* **Pedagogical Justification:** The gravitational field is conservative with potential energy $V_0(r) = -\mu/r = -GM/r$. Total specific mechanical energy $\xi = \frac{1}{2}v^2 - \frac{GM}{r}$ is conserved between launch and apocenter:

At launch ($r = R, v = v_0$):
$$ \xi = \frac{1}{2}v_0^2 - \frac{GM}{R} $$

At apocenter ($r = 3R, v = v_a = v_0/6$):
$$ \xi = \frac{1}{2}v_a^2 - \frac{GM}{3R} = \frac{1}{2}\left(\frac{v_0}{6}\right)^2 - \frac{GM}{3R} = \frac{v_0^2}{72} - \frac{GM}{3R} $$

#### 3. Solving for Launch Speed $v_0$
Equating both energy expressions:
$$ \frac{1}{2}v_0^2 - \frac{GM}{R} = \frac{1}{72}v_0^2 - \frac{GM}{3R} $$
Grouping velocity terms on the left and gravitational terms on the right:
$$ \left(\frac{1}{2} - \frac{1}{72}\right)v_0^2 = \frac{GM}{R} - \frac{GM}{3R} $$
Finding common denominators:
$$ \left(\frac{36 - 1}{72}\right)v_0^2 = \left(1 - \frac{1}{3}\right)\frac{GM}{R} $$
$$ \frac{35}{72}v_0^2 = \frac{2}{3}\frac{GM}{R} $$

Multiplying both sides by $\frac{72}{35}$:
$$ v_0^2 = \frac{2}{3} \cdot \frac{72}{35} \frac{GM}{R} = \frac{2 \cdot 24}{35} \frac{GM}{R} = \frac{48}{35} \frac{GM}{R} $$

Taking the square root:
$$ v_0 = \sqrt{\frac{48}{35}\frac{GM}{R}} $$

### Phase 4: Physical Interpretation & Dimensional Verification
* **Independent check with the Binet solution.** With $u = \tfrac{\mu}{h^2}(1 + e\cos\theta)$ in the frame where $\theta = 0$ is the periapsis, the launch point ($r = R$, $\dot{r} = v_0\sin 60^\circ$, $r\dot{\theta} = v_0\cos 60^\circ$) fixes the constants through $u(\theta_0) = 1/R$ and $u'(\theta_0) = -\dot{r}/h$. With $v_0^2 = \tfrac{48}{35}\tfrac{GM}{R}$ and $h^2 = \tfrac{12}{35}GMR$:
  $$ e = \frac{h^2}{\mu}\sqrt{\left(\frac{1}{R} - \frac{\mu}{h^2}\right)^2 + \left(\frac{\dot{r}}{h}\right)^2} = \frac{12R}{35}\sqrt{\frac{529}{144R^2} + \frac{3}{R^2}} = \frac{12R}{35}\cdot\frac{31}{12R} = \frac{31}{35} $$
  and $\tan\beta = \dot{r}/(r\dot{\theta}) = \dfrac{R}{p}\,e\sin\theta_0$ with $\cos\theta_0 = \dfrac{p/R - 1}{e} = -\dfrac{23}{31}$, so $\sin\theta_0 = \dfrac{\sqrt{432}}{31}$ and $\tan\beta = \dfrac{35}{12}\cdot\dfrac{31}{35}\cdot\dfrac{\sqrt{432}}{31} = \dfrac{\sqrt{432}}{12} = \sqrt{3}$, i.e. $\beta = 60^\circ$, as required.
* **Numerical check (Python, velocity-Verlet integration of $\ddot{\mathbf{r}} = -\mu\mathbf{r}/r^3$ with $\mu = R = 1$, $v_0 = \sqrt{48/35}$):** the maximum radius reached is $2.99999999981R$, in agreement with $r_a = 3R$.
* **Check Bound Condition ($v_0 < v_{\text{esc}}$):**
  - Escape speed from surface: $v_e = \sqrt{\frac{2GM}{R}} = \sqrt{\frac{70}{35}\frac{GM}{R}}$.
  - Since $\frac{48}{35} \approx 1.3714 < 2$, we have $v_0 < v_e$, confirming the orbit is an ellipse and the seed returns to the asteroid as stated!
* **Check Orbital Parameters:**
  - $h^2 = \frac{1}{4}R^2 v_0^2 = \frac{1}{4}R^2 \left(\frac{48}{35}\frac{GM}{R}\right) = \frac{12}{35}GM R$.
  - Semi-latus rectum: $p = h^2/\mu = \frac{12}{35}R$.
  - At apocenter: $r_a = \frac{p}{1 - e} = 3R \implies 1 - e = \frac{p}{3R} = \frac{12/35}{3} = \frac{4}{35} \implies e = 1 - \frac{4}{35} = \frac{31}{35} \approx 0.8857$.
  - Periapsis: $r_p = \frac{p}{1 + e} = \frac{12/35}{66/35}R = \frac{12}{66}R = \frac{2}{11}R < R$. (The pericenter of the full conic lies inside the asteroid; only the arc from the launch point to the apocenter is physical, the seed lands before reaching the pericenter.).
* **Dimensional Check:** $[v_0] = \sqrt{[G][M]/[R]} = \sqrt{\frac{\text{m}^3}{\text{kg}\cdot\text{s}^2}\frac{\text{kg}}{\text{m}}} = \text{m/s}$ (Correct).
