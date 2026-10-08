---
title: "Solutions - Topic 4: Angular Momentum and Central Forces"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Full Analytical Solutions (4-Phase Methodology)"
language: "English"
---

# 📚 Topic 4: Angular Momentum and Central Forces - Full Analytical Solutions

Exhaustive, step-by-step analytical solutions for official problems from Topic 4 (**Angular Momentum, Central Forces, and Kepler's Problem**) of *Mechanics Applied to Aerospace Engineering* (UC3M). Every problem strictly complies with the mandatory 4-phase pedagogical methodology, with explicit justification prior to every equation, zero algebraic omissions, explicit derivative developments (product, quotient, and chain rules), explicit integral evaluations (substitutions, primitives, and Barrow's rule), polar rotation matrices $[{}_0 R_1]$, and dimensional verifications.

---

## 📌 Problem 17: Linear Central Force under Gravity (Slide 6 Benchmark)

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A point particle $M$ of mass $m$ is subject to an attractive central force directed towards origin $O$ whose magnitude is proportional to $m$ and the distance $r = \|\mathbf{r}\|$, with proportionality constant $k^2$:
  $$ \mathbf{F}_{\text{attract}} = -m k^2 \mathbf{r} $$
* **Forces Acting on $M$:**
  1. Linear isotropic attractive central force: $\mathbf{F}_{\text{attract}} = -m k^2 (x\mathbf{i} + y\mathbf{j} + z\mathbf{k})$.
  2. Uniform gravitational force directed along $-Oz$: $\mathbf{F}_g = -mg\mathbf{k}$.
* **Hypotheses:**
  1. Inertial reference frame $S_0 : \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$ with origin at the center of attraction $O$.
  2. Free particle in 3D Euclidean space: $\text{CDOF} = 3$ (Cartesian coordinates $x, y, z$).
  3. No aerodynamic drag or friction.
* **Initial Conditions ($t = 0$):**
  $$ \mathbf{r}(0) = x_0\mathbf{i} + y_0\mathbf{j} + z_0\mathbf{k} = \frac{\sqrt{3}g}{k^2}\mathbf{i} + 0\mathbf{j} + 0\mathbf{k} $$
  $$ \mathbf{v}(0) = \dot{x}_0\mathbf{i} + \dot{y}_0\mathbf{j} + \dot{z}_0\mathbf{k} = 0\mathbf{i} + \frac{2g}{k}\mathbf{j} + 0\mathbf{k} $$
* **Parameters:** $m > 0$ [kg], $g > 0$ [m/s$^2$], $k > 0$ [s$^{-1}$].

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* **Inertial Reference Frame:** $S_0 : \{O; \mathcal{B}_0\}$ with canonical orthonormal basis $\mathcal{B}_0 = \{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$.
* **Position, Velocity, Acceleration Vectors:**
  $$ \mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k} $$
  $$ \mathbf{v}(t) = \dot{x}(t)\mathbf{i} + \dot{y}(t)\mathbf{j} + \dot{z}(t)\mathbf{k} $$
  $$ \mathbf{a}(t) = \ddot{x}(t)\mathbf{i} + \ddot{y}(t)\mathbf{j} + \ddot{z}(t)\mathbf{k} $$

### Phase 3: Step-by-Step Mathematical Deduction

#### 1. Equations of Motion in Cartesian Coordinates
* **Pedagogical Justification:** By Newton's Second Law in an inertial frame, $m\mathbf{a} = \sum \mathbf{F}$. Because the restoring force is linear in the position vector $\mathbf{r}$, the Cartesian components decouple cleanly:

$$ m\left(\ddot{x}\mathbf{i} + \ddot{y}\mathbf{j} + \ddot{z}\mathbf{k}\right) = -m k^2 (x\mathbf{i} + y\mathbf{j} + z\mathbf{k}) - mg\mathbf{k} $$
Dividing by mass $m > 0$:
$$ \begin{cases} \ddot{x} + k^2 x = 0 \\ \ddot{y} + k^2 y = 0 \\ \ddot{z} + k^2 z = -g \end{cases} $$

#### 2. Analytical Integration of $x(t)$
* **Pedagogical Justification:** The equation $\ddot{x} + k^2 x = 0$ is a homogeneous linear second-order ODE with constant coefficients and characteristic roots $\lambda = \pm i k$.

General solution:
$$ x(t) = A_1\cos(kt) + B_1\sin(kt) $$
Differentiating with respect to time:
$$ \dot{x}(t) = -k A_1\sin(kt) + k B_1\cos(kt) $$
Imposing initial conditions $x(0) = \frac{\sqrt{3}g}{k^2}$ and $\dot{x}(0) = 0$:
$$ x(0) = A_1 = \frac{\sqrt{3}g}{k^2}, \qquad \dot{x}(0) = k B_1 = 0 \implies B_1 = 0 $$
$$ x(t) = \frac{\sqrt{3}g}{k^2}\cos(kt) $$

#### 3. Analytical Integration of $y(t)$
* **Pedagogical Justification:** The equation $\ddot{y} + k^2 y = 0$ shares the same natural frequency $k$.

General solution:
$$ y(t) = A_2\cos(kt) + B_2\sin(kt) $$
$$ \dot{y}(t) = -k A_2\sin(kt) + k B_2\cos(kt) $$
Imposing initial conditions $y(0) = 0$ and $\dot{y}(0) = \frac{2g}{k}$:
$$ y(0) = A_2 = 0, \qquad \dot{y}(0) = k B_2 = \frac{2g}{k} \implies B_2 = \frac{2g}{k^2} $$
$$ y(t) = \frac{2g}{k^2}\sin(kt) $$

#### 4. Analytical Integration of $z(t)$
* **Pedagogical Justification:** The vertical ODE $\ddot{z} + k^2 z = -g$ has a constant particular solution representing the static equilibrium position:
$$ z_{\text{eq}} = -\frac{g}{k^2} $$
Defining the perturbation variable $z^*(t) \equiv z(t) - z_{\text{eq}} = z(t) + \frac{g}{k^2}$, the equation becomes homogeneous: $\ddot{z}^* + k^2 z^* = 0$.

General solution:
$$ z(t) = -\frac{g}{k^2} + A_3\cos(kt) + B_3\sin(kt) $$
$$ \dot{z}(t) = -k A_3\sin(kt) + k B_3\cos(kt) $$
Imposing initial conditions $z(0) = 0$ and $\dot{z}(0) = 0$:
$$ z(0) = -\frac{g}{k^2} + A_3 = 0 \implies A_3 = \frac{g}{k^2} $$
$$ \dot{z}(0) = k B_3 = 0 \implies B_3 = 0 $$
$$ z(t) = \frac{g}{k^2}\left(\cos(kt) - 1\right) $$

#### 5. Geometric Characterization of the Trajectory
* **Planar Confinement:**
  Comparing $x(t)$ and $z(t)$, both depend on the identical phase function $\cos(kt)$:
  $$ \cos(kt) = \frac{k^2 x(t)}{\sqrt{3}g} $$
  Substituting into $z(t)$:
  $$ z(t) = \frac{g}{k^2}\left( \frac{k^2 x(t)}{\sqrt{3}g} - 1 \right) = \frac{x(t)}{\sqrt{3}} - \frac{g}{k^2} $$
  Rearranging into standard plane form $Ax + By + Cz + D = 0$:
  $$ x - \sqrt{3}z - \frac{\sqrt{3}g}{k^2} = 0 $$
  *The entire motion is strictly planar, contained in a plane inclined at $30^\circ$ to the vertical!*

* **Conic Trajectory Shape:**
  Eliminating time $t$ between $x(t)$ and $y(t)$ using the Pythagorean trigonometric identity $\cos^2(kt) + \sin^2(kt) \equiv 1$:
  $$ \left(\frac{x(t)}{\sqrt{3}g/k^2}\right)^2 + \left(\frac{y(t)}{2g/k^2}\right)^2 = 1 $$
  The projection onto the $Oxy$ plane is an **ellipse** with semi-axes:
  $$ a_x = \frac{\sqrt{3}g}{k^2}, \qquad b_y = \frac{2g}{k^2} $$
  Because the intersection of an elliptic cylinder with an oblique non-parallel plane is an ellipse, the **true 3D trajectory is an ellipse centered at $(0, 0, -g/k^2)$**.

#### 6. Velocity Vector and Magnitude
Differentiating the position components:
$$ \mathbf{v}(t) = \dot{x}(t)\mathbf{i} + \dot{y}(t)\mathbf{j} + \dot{z}(t)\mathbf{k} = -\frac{\sqrt{3}g}{k}\sin(kt)\,\mathbf{i} + \frac{2g}{k}\cos(kt)\,\mathbf{j} - \frac{g}{k}\sin(kt)\,\mathbf{k} $$
Computing the speed squared:
$$ v^2(t) = \left(-\frac{\sqrt{3}g}{k}\sin(kt)\right)^2 + \left(\frac{2g}{k}\cos(kt)\right)^2 + \left(-\frac{g}{k}\sin(kt)\right)^2 $$
$$ v^2(t) = \frac{g^2}{k^2}\left[ 3\sin^2(kt) + 4\cos^2(kt) + \sin^2(kt) \right] = \frac{g^2}{k^2}\left[ 4\sin^2(kt) + 4\cos^2(kt) \right] = \frac{4g^2}{k^2} $$
Taking the square root:
$$ v(t) = \frac{2g}{k} = \text{constant} $$

### Phase 4: Physical Interpretation & Dimensional Verification
* **Constant Speed Property:** Although the path is an ellipse, the speed is constant because the conservative potential is $V(x,y,z) = \frac{1}{2}m k^2(x^2 + y^2 + z^2) + mgz = \frac{1}{2}m k^2[x^2 + y^2 + (z + g/k^2)^2] - \frac{mg^2}{2k^2}$, which possesses circular symmetry around the displaced equilibrium center.
* **Dimensional Checks:**
  - Coordinates: $[x] = [g/k^2] = \frac{\text{m/s}^2}{\text{s}^{-2}} = \text{m}$ (Correct).
  - Velocity: $[v] = [g/k] = \frac{\text{m/s}^2}{\text{s}^{-1}} = \text{m/s}$ (Correct).

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
  The force field is central and purely radial $\mathbf{F} = F(r)\mathbf{e}_r$. Its curl in spherical coordinates is $\nabla \times \mathbf{F} \equiv \mathbf{0}$, so $\mathbf{F}$ is conservative.
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
  - **iii. Bounded oscillation:** Every orbit with $E^* > W_{\min}$ oscillates between two finite turning points $u_{\min}$ and $u_{\max}$.

##### 3. Case $\alpha = 3$ (Inverse-Cube Force: $F \propto 1/r^3$)
* Binet Equation: $u'' + u = \frac{\mu}{h^2}u \implies u'' + \left(1 - \frac{\mu}{h^2}\right)u = 0$
* Effective Potential: $W_{\text{eff}}(u) = \left(1 - \frac{\mu}{h^2}\right)u^2$
* Analysis:
  - **Subcase $h^2 > \mu$:** $W_{\text{eff}}(u) = k^2 u^2 > 0$. $u(\theta) = A\cos(\sqrt{1 - \mu/h^2}\theta + \delta)$.
    * Escape to infinity ($u \to 0$) occurs at $\theta$ where cosine vanishes.
    * Collision ($u \to \infty$) is impossible.
  - **Subcase $h^2 < \mu$:** $W_{\text{eff}}(u) = -C^2 u^2 < 0$.
    * The coefficient is negative: $u(\theta) = C_1 e^{\kappa\theta} + C_2 e^{-\kappa\theta}$.
    * As $\theta$ increases, $u \to \infty \implies$ **the particle falls into the origin $r \to 0$ (orbital collapse)**!
  - **Subcase $h^2 = \mu$:** $u'' = 0 \implies u(\theta) = A\theta + B$. Straight-line spiral.

##### 4. Case $\alpha = 4$ (Inverse-Quartic Force: $F \propto 1/r^4$)
* Binet Equation: $u'' + u = \frac{\mu}{h^2}u^2$
* Effective Potential: $W_{\text{eff}}(u) = u^2 - \frac{2\mu}{3h^2}u^3$
* Analysis:
  - Derivative: $W'(u) = 2u - \frac{2\mu}{h^2}u^2 = 2u(1 - \frac{\mu}{h^2}u)$.
  - Extrema: Minimum at $u = 0$ ($W = 0$), local maximum (potential barrier) at $u_{\text{barrier}} = \frac{h^2}{\mu}$ with $W_{\max} = \frac{h^4}{3\mu^2}$.
  - For $u > u_{\text{barrier}}$, the $-u^3$ term dominates and $W_{\text{eff}}(u) \to -\infty$.
  - **i. Escape to infinity ($u \to 0$):** Occurs if $E^* \ge 0$ and $u(0) < u_{\text{barrier}}$.
  - **ii. Collision with origin ($u \to \infty$):** Occurs whenever $E^* > W_{\max}$, or if $u(0) > u_{\text{barrier}}$ with $u'(0) > 0$. The particle overcomes the centrifugal barrier and plunges into $r = 0$!
  - **iii. Bounded oscillation:** Occurs in the potential well $0 < E^* < W_{\max}$ with $u < u_{\text{barrier}}$.

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
* **Check Bound Condition ($v_0 < v_{\text{esc}}$):**
  - Escape speed from surface: $v_e = \sqrt{\frac{2GM}{R}} = \sqrt{\frac{70}{35}\frac{GM}{R}}$.
  - Since $\frac{48}{35} \approx 1.3714 < 2$, we have $v_0 < v_e$, confirming the orbit is an ellipse and the seed returns to the asteroid as stated!
* **Check Orbital Parameters:**
  - $h^2 = \frac{1}{4}R^2 v_0^2 = \frac{1}{4}R^2 \left(\frac{48}{35}\frac{GM}{R}\right) = \frac{12}{35}GM R$.
  - Semi-latus rectum: $p = h^2/\mu = \frac{12}{35}R$.
  - At apocenter: $r_a = \frac{p}{1 - e} = 3R \implies 1 - e = \frac{p}{3R} = \frac{12/35}{3} = \frac{4}{35} \implies e = 1 - \frac{4}{35} = \frac{31}{35} \approx 0.8857$.
  - Periapsis: $r_p = \frac{p}{1 + e} = \frac{12/35}{66/35}R = \frac{12}{66}R = \frac{2}{11}R < R$. (The pericenter is inside the asteroid, confirming it is an intersecting ballistic trajectory!).
* **Dimensional Check:** $[v_0] = \sqrt{[G][M]/[R]} = \sqrt{\frac{\text{m}^3}{\text{kg}\cdot\text{s}^2}\frac{\text{kg}}{\text{m}}} = \text{m/s}$ (Correct).

---

## 📌 Problem 39: Particle on a String with a Plate

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A heavy point particle $P$ of mass $m$ is connected to origin $O$ on a horizontal thin square plate by a massless inextensible cord of length $\ell$. The distance from $O$ to the plate edge is $d$. The string hangs over the straight edge at a contact point $Q$.
* **Configuration Degrees of Freedom:**
  - $P$ is constrained by the inextensible string length: $\|\mathbf{OQ}\| + \|\mathbf{QP}\| = \ell$.
  - String stays in contact with the edge and remains taut at all times.
  - The edge of the plate is a straight line $y = d$ in the plate plane.
  - The position of $Q$ along the edge is parametrized by polar angle $\theta$ from $Ox_0$.
  - The hanging segment $QP$ is free to swing in space, described by angle $\phi$.
  - Total CDOF $= 2$ (angles $\theta$ and $\phi$).
* **Initial State ($t = 0$):**
  - $\theta(0) = \phi(0) = \pi/3\text{ rad}$.
  - $v_0^P(0) = \sqrt{\ell g}$.
* **Parameters:** $m > 0$ [kg], $\ell > 0$ [m], $d > 0$ [m], $g > 0$ [m/s$^2$].

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* **Inertial Reference Frame:** $S_0 : \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ with $Ox_0 y_0$ in the plate plane, $Oz_0$ upwards, and plate edge along $y_0 = d$.
* **Contact Point $Q$:**
  $$ \mathbf{r}_0^Q = \frac{d}{\sin\theta}\left(\cos\theta\,\mathbf{i}_0 + \sin\theta\,\mathbf{j}_0\right) = d\cot\theta\,\mathbf{i}_0 + d\,\mathbf{j}_0 $$
  Length of segment $OQ$: $L_{OQ} = \frac{d}{\sin\theta}$.
* **Hanging Segment $QP$:**
  Remaining length: $L_{QP} = \ell - L_{OQ} = \ell - \frac{d}{\sin\theta}$.
  Unit vector along $QP$:
  $$ \mathbf{u}_{QP} = \sin\phi\cos\theta\,\mathbf{i}_0 + \sin\phi\sin\theta\,\mathbf{j}_0 - \cos\phi\,\mathbf{k}_0 $$
* **Position of Particle $P$:**
  $$ \mathbf{r}_0^P = \mathbf{r}_0^Q + \left(\ell - \frac{d}{\sin\theta}\right)\mathbf{u}_{QP} $$

### Phase 3: Step-by-Step Mathematical Deduction
* **Velocity of $Q$:**
  $$ \mathbf{v}_0^Q = \frac{d\mathbf{r}_0^Q}{dt} = -d\frac{\dot{\theta}}{\sin^2\theta}\,\mathbf{i}_0 $$
* **Velocity of $P$:**
  Applying the product rule and chain rule to $\mathbf{r}_0^P$:
  $$ \mathbf{v}_0^P = \mathbf{v}_0^Q + \left(-\frac{d(-\cos\theta)\dot{\theta}}{\sin^2\theta}\right)\mathbf{u}_{QP} + \left(\ell - \frac{d}{\sin\theta}\right)\frac{d\mathbf{u}_{QP}}{dt} $$
  $$ \mathbf{v}_0^P = -\frac{d\dot{\theta}}{\sin^2\theta}\mathbf{i}_0 + \frac{d\dot{\theta}\cos\theta}{\sin^2\theta}\mathbf{u}_{QP} + \left(\ell - \frac{d}{\sin\theta}\right)\left(\dot{\phi}\frac{\partial\mathbf{u}_{QP}}{\partial\phi} + \dot{\theta}\frac{\partial\mathbf{u}_{QP}}{\partial\theta}\right) $$
* **Equations of Motion & Energy:**
  Because the string is frictionless over the plate edge, the constraint does no work. Gravity is conservative. The mechanical energy $E = T + V = \frac{1}{2}m(v_0^P)^2 - mg z_P$ is strictly conserved.

### Phase 4: Physical Interpretation & Verification
* When $\theta = \pi/2$, $Q$ is at the closest approach distance $d$, and the hanging length is maximized ($\ell - d$).
* Dimensional consistency: all lengths scale with $\ell, d$, velocities with $\sqrt{\ell g}$.
