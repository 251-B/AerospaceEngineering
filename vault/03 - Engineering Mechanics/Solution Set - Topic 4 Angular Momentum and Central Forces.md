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
* **System:** a particle $P$ of mass $m$ attracted to $O$ by $\mathbf{F} = -\dfrac{m\mu}{r^\alpha}\mathbf{e}_r$.
* **Hypotheses:** $S_0$ inertial; $\mu \gt 0$, $\alpha \gt 0$ constants; no other forces; $h \ne 0$ unless stated.
* **Degrees of freedom:** free particle, $\text{CDOF} = 3$; after part (a) the motion is planar, $\text{CDOF} = 2$ with coordinates $(r, \theta)$.
* **Variables:** $u(\theta) = 1/r(\theta)$, $u' = du/d\theta$, $h = \|\mathbf{r}\times\mathbf{v}\|$ [m$^2$/s].

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mu$ | force strength per unit mass, $F/m = \mu/r^\alpha$ | m$^{\alpha+1}$/s$^2$ |
| $h$ | specific angular momentum | m$^2$/s |
| $u$ | reciprocal radius | m$^{-1}$ |
| $\xi$ | specific mechanical energy | J/kg = m$^2$/s$^2$ |

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* **Change of basis (polar basis in the plane of motion).** Take $\mathbf{k}$ along $\mathbf{H}_O$. The polar basis $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}\}$ is the inertial basis $\mathcal{B}_0 = \{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$ rotated by $\theta(t)$ about $\mathbf{k}$:
$$ [{}_0 R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0R_1] = \cos^2\theta + \sin^2\theta = 1, \qquad [{}_0R_1]^T[{}_0R_1] = I $$

The angular velocity of $\mathcal{B}_1$ is $\boldsymbol{\omega}_{10} = \dot{\theta}\,\mathbf{k}$; Poisson's formula $\dot{\mathbf{e}} = \boldsymbol{\omega}\times\mathbf{e}$ gives $\dot{\mathbf{e}}_r = \dot{\theta}\,\mathbf{e}_\theta$ and $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_r$. The product rule on $\mathbf{r} = r\mathbf{e}_r$ yields

$$ \mathbf{v} = \dot{r}\,\mathbf{e}_r + r\dot{\theta}\,\mathbf{e}_\theta, \qquad \mathbf{a} = \left(\ddot{r} - r\dot{\theta}^2\right)\mathbf{e}_r + \left(r\ddot{\theta} + 2\dot{r}\dot{\theta}\right)\mathbf{e}_\theta $$

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a): conservation laws and planar motion
* **Pedagogical Justification:** The force line of action passes through the fixed point $O$, so its torque about $O$ vanishes, and the angular momentum theorem about a fixed point (Notes Eq. 4.53) gives a constant $\mathbf{H}_O$.
$$ \mathbf{M}_O = \mathbf{r}\times\mathbf{F} = r\mathbf{e}_r\times\left(-\frac{m\mu}{r^\alpha}\mathbf{e}_r\right) = \mathbf{0} \implies \left.\frac{d\mathbf{H}_O}{dt}\right|_0 = \mathbf{0} \implies \mathbf{H}_O = m\,\mathbf{r}\times\mathbf{v} = \text{const} $$

Since $\mathbf{r}\cdot\mathbf{H}_O \equiv 0$ and $\mathbf{v}\cdot\mathbf{H}_O \equiv 0$, $P$ stays in the plane through $O$ perpendicular to $\mathbf{H}_O$.

* **Pedagogical Justification:** The force is purely radial and depends only on $r$, so its elementary work $\mathbf{F}\cdot d\mathbf{r} = F(r)\,dr$ is the exact differential of a function of $r$ (equivalently $\nabla\times\mathbf{F} = \mathbf{0}$). The force is conservative, so the energy is conserved. The potential energy per unit mass follows from Barrow's rule with the reference at infinity (for $\alpha \gt 1$; for $\alpha \le 1$ the reference point is arbitrary):
$$ V_0(r) = -\int_\infty^r\left(-\frac{\mu}{s^\alpha}\right)ds = \mu\left[\frac{s^{1-\alpha}}{1 - \alpha}\right]_\infty^r = -\frac{\mu}{(\alpha - 1)\,r^{\alpha - 1}} \quad (\alpha \gt 1), \qquad V_0(r) = \mu\ln r \quad (\alpha = 1) $$
$$ \xi = \tfrac{1}{2}v^2 + V_0(r) = \text{const} $$

#### Part (b): Binet equation for a power law
* **Pedagogical Justification:** Eliminate time with $h = r^2\dot{\theta} = \text{const}$, i.e. $\dot{\theta} = hu^2$. The chain rule for $r = u^{-1}$ gives $dr/d\theta = -u'/u^2$.
$$ \dot{r} = \frac{dr}{d\theta}\dot{\theta} = \left(-\frac{u'}{u^2}\right)\left(hu^2\right) = -hu', \qquad \ddot{r} = \frac{d}{dt}\left(-hu'\right) = -hu''\,\dot{\theta} = -h^2u^2u'' $$

The radial equation $\ddot{r} - r\dot{\theta}^2 = -\mu/r^\alpha = -\mu u^\alpha$ with $r\dot{\theta}^2 = \frac{1}{u}(hu^2)^2 = h^2u^3$ becomes

$$ -h^2u^2u'' - h^2u^3 = -\mu u^\alpha \quad\overset{\div\,(-h^2u^2)}{\Longrightarrow}\quad \boxed{u'' + u = \frac{\mu}{h^2}\,u^{\alpha - 2}} $$

#### Part (c): first integral
* **Pedagogical Justification:** Write the specific energy with $\dot{r} = -hu'$ and $r\dot{\theta} = hu$. Since $\xi$ is constant, this is a first integral; it can be checked by multiplying the Binet equation by $u'$ and integrating in $\theta$.
$$ \xi = \tfrac{1}{2}h^2\left[(u')^2 + u^2\right] + V_0\!\left(\frac{1}{u}\right) \implies \boxed{(u')^2 + W_{\text{eff}}(u) = E^*}, \quad E^* \equiv \frac{2\xi}{h^2}, \quad W_{\text{eff}}(u) = u^2 + \frac{2V_0(1/u)}{h^2} $$

Check: $\frac{d}{d\theta}\left[(u')^2 + W_{\text{eff}}\right] = 2u'u'' + W_{\text{eff}}'u' = 0$ gives $u'' = -\tfrac{1}{2}W_{\text{eff}}'$, which is the Binet equation. Motion exists only where $W_{\text{eff}}(u) \le E^*$; turning points ($u' = 0$) are the roots of $W_{\text{eff}}(u) = E^*$, and a minimum or a maximum of $W_{\text{eff}}$ is a circular orbit.

#### Case $\alpha = 2$: inverse square (Kepler)
* Binet: $u'' + u = \mu/h^2$. Potential: $V_0 = -\mu u$, so $W_{\text{eff}} = u^2 - \dfrac{2\mu}{h^2}u = \left(u - \dfrac{\mu}{h^2}\right)^2 - \left(\dfrac{\mu}{h^2}\right)^2$, a parabola with minimum $-(\mu/h^2)^2$ at $u = \mu/h^2$.
* **(i) Escape ($u \to 0$):** possible if $E^* \ge W_{\text{eff}}(0) = 0$, i.e. $\xi \ge 0$ (parabola or hyperbola).
* **(ii) Reaching $r = 0$:** impossible for $h \ne 0$, because $W_{\text{eff}} \to +\infty$ as $u \to \infty$.
* **(iii) Oscillation:** for $-(\mu/h^2)^2 \lt E^* \lt 0$, i.e. $-\mu^2/(2h^2) \lt \xi \lt 0$: $u$ oscillates between the two roots (periapsis and apoapsis of an ellipse); $E^* = -(\mu/h^2)^2$ is the circular orbit.

#### Case $\alpha = 1$: $F \propto 1/r$
* Binet: $u'' + u = \dfrac{\mu}{h^2u}$. Potential $V_0(1/u) = -\mu\ln u$, so $W_{\text{eff}} = u^2 - \dfrac{2\mu}{h^2}\ln u$.
* $W_{\text{eff}} \to +\infty$ both as $u \to 0$ (because $-\ln u \to +\infty$) and as $u \to \infty$. Its minimum is at $2u - \dfrac{2\mu}{h^2u} = 0$, i.e. $u_0 = \sqrt{\mu}/h$.
* **(i)** Escape is impossible for any finite energy. **(ii)** Reaching $r = 0$ is impossible. **(iii)** Every orbit with $E^* \gt W_{\text{eff}}(u_0)$ oscillates between two finite turning points; $E^* = W_{\text{eff}}(u_0)$ is the circular orbit $r = h/\sqrt{\mu}$.

#### Case $\alpha = 3$: $F \propto 1/r^3$
* $V_0 = -\dfrac{\mu}{2r^2} = -\dfrac{\mu}{2}u^2$. Binet: $u'' + \lambda u = 0$ with $\lambda \equiv 1 - \mu/h^2$. Then $W_{\text{eff}} = \lambda u^2$ and $(u')^2 + \lambda u^2 = E^*$.
* **$h^2 \gt \mu$ ($\lambda = \kappa^2 \gt 0$, $\kappa = \sqrt{1 - \mu/h^2}$):** $u = A\cos(\kappa\theta + \delta)$ with $A = \sqrt{u_0^2 + (u_0'/\kappa)^2}$. The cosine vanishes at a finite angle, so $u \to 0$ in every case: **(i) the particle always escapes**; a particle moving inward ($u_0' \gt 0$) is first reflected at the periapsis $u = A$. **(ii)** never, since $u \le A$. **(iii)** no oscillation between two positive values.
* **$h^2 \lt \mu$ ($\lambda = -\kappa^2 \lt 0$, $\kappa = \sqrt{\mu/h^2 - 1}$):** $u = C_1e^{\kappa\theta} + C_2e^{-\kappa\theta}$ with $C_1 = \tfrac{1}{2}(u_0 + u_0'/\kappa)$, $C_2 = \tfrac{1}{2}(u_0 - u_0'/\kappa)$. If $C_1 \gt 0$ (i.e. $u_0' \gt -\kappa u_0$), $u \to \infty$: **(ii) the particle reaches the origin**. If $C_1 \lt 0$ ($u_0' \lt -\kappa u_0$), $u$ reaches $0$ at a finite angle: **(i) escape**. If $C_1 = 0$, $u = u_0e^{-\kappa\theta} \to 0$ only asymptotically (spiral $r = r_0e^{\kappa\theta}$), a limiting case of escape. **(iii)** no oscillation.
* **$h^2 = \mu$ ($\lambda = 0$):** $u'' = 0 \Rightarrow u = u_0 + u_0'\theta$ (reciprocal spiral). $u_0' \gt 0$: reaches the origin; $u_0' \lt 0$: escapes at $\theta = u_0/|u_0'|$; $u_0' = 0$: circle $r = 1/u_0$.

#### Case $\alpha = 4$: $F \propto 1/r^4$
* Binet: $u'' + u = \dfrac{\mu}{h^2}u^2$. $V_0 = -\dfrac{\mu}{3}u^3$, so $W_{\text{eff}} = u^2 - \dfrac{2\mu}{3h^2}u^3 = u^2\left(1 - \dfrac{2\mu}{3h^2}u\right)$.
* $W_{\text{eff}}'(u) = 2u - \dfrac{2\mu}{h^2}u^2 = 2u\left(1 - \dfrac{\mu}{h^2}u\right)$: stationary points $u = 0$ (minimum, $W = 0$) and $u_b = h^2/\mu$ (maximum, barrier $W_{\max} = u_b^2 - \dfrac{2\mu}{3h^2}u_b^3 = \dfrac{h^4}{3\mu^2}$). For $u \gt u_b$, $W_{\text{eff}}$ decreases without bound and crosses zero at $u_0 = 3h^2/(2\mu) \gt u_b$.
* **There is no interior minimum**, so the allowed set $\{W_{\text{eff}} \le E^*\}$ either contains $u = 0$ or extends to $u \to \infty$. Because $\dot{\theta} = hu^2 \gt 0$, $u'$ has the sign of $\dot{u}$.
* **$0 \le E^* \lt W_{\max}$:** two roots $u_1 \in [0, u_b)$ and $u_2 \gt u_b$; allowed $u \le u_1$ or $u \ge u_2$. If $u(0) \le u_1$ the particle is reflected at $u_1$ and escapes; if $u(0) \ge u_2$ it is reflected at $u_2$ and falls to the origin.
* **$E^* \lt 0$:** only $u \ge u_2 \gt u_0$ is allowed; the particle reaches $r = 0$. **$E^* \gt W_{\max}$:** no turning points; $u'(0) \lt 0$ (moving outward) escapes and $u'(0) \gt 0$ (moving inward) falls to the origin. **$E^* = W_{\max}$:** the unstable circular orbit $u = u_b$ and asymptotic approaches to it.
* **(i)** escape: $0 \le E^* \lt W_{\max}$ with $u(0) \lt u_b$, or $E^* \gt W_{\max}$ with $u'(0) \lt 0$. **(ii)** reaching $r = 0$: $E^* \lt 0$, or $0 \le E^* \lt W_{\max}$ with $u(0) \gt u_b$, or $E^* \gt W_{\max}$ with $u'(0) \gt 0$. **(iii)** bounded oscillation between two values of $u$: **does not occur**; it would need an interior minimum of $W_{\text{eff}}$, and the only bounded motion is the unstable circle $u = u_b$.

### Phase 4: Physical Interpretation & Dimensional Verification
* **Dimensional check:** $[F/m] = \text{m/s}^2 = [\mu]/\text{m}^\alpha$ gives $[\mu] = \text{m}^{\alpha+1}/\text{s}^2$. With $[h^2] = \text{m}^4/\text{s}^2$ and $[u] = \text{m}^{-1}$, $\dfrac{\mu}{h^2}u^{\alpha - 2}$ has units $\text{m}^{\alpha - 3}\,\text{m}^{-(\alpha - 2)} = \text{m}^{-1}$, the same as $u$ and $u''$ ($\theta$ is dimensionless).
* **Stability of circular orbits (consequence of the first integral):** for general $\alpha$, $W_{\text{eff}}'(u_0) = 0$ gives $u_0^{\alpha - 3} = h^2/\mu$ and $W_{\text{eff}}''(u_0) = 2(3 - \alpha)$, so the circular orbit is a minimum (stable) for $\alpha \lt 3$ and a maximum (unstable) for $\alpha \gt 3$, in agreement with the cases above ($\alpha = 4$: barrier at $u_b = h^2/\mu$).
* **Numerical check** (Python, RK4 with step $10^{-4}$ rad on $u'' = -u + (\mu/h^2)u^{\alpha-2}$, units with $\mu = h = 1$ unless stated):

| Case | Initial data $(u_0, u_0')$ | Predicted | Integration result |
|---|---|---|---|
| $\alpha = 2$ | $(1.5, 0)$ | bounded, $0.5$ to $1.5$ | $u \in [0.5000, 1.5000]$ over $60$ rad |
| $\alpha = 2$ | $(0.5, -0.9)$, $E^* \gt 0$ | escape | $u = 0$ at $\theta = 0.823$ |
| $\alpha = 4$ | $(0.5, 0)$, $E^* = 1/6 \lt 1/3$ | reflected, then escape | $u = 0$ at $\theta = 2.078$ |
| $\alpha = 4$ | $(1.2, 0)$, $E^* = 0.288 \lt 1/3$ | collapse | $u \to \infty$ at $\theta = 3.713$ |
| $\alpha = 4$ | $(0.5, 0.9)$, $E^* \gt 1/3$ | collapse | $u \to \infty$ at $\theta = 3.258$ |
| $\alpha = 4$ | $(0.5, -0.9)$, $E^* \gt 1/3$ | escape | $u = 0$ at $\theta = 0.524$ |
| $\alpha = 4$ | $(1, 0)$, $E^* = W_{\max}$ | unstable circular orbit | $u = 1$ for $20$ rad |
| $\alpha = 3$, $\mu/h^2 = 2$ | $(1, 0.2)$, $C_1 \gt 0$ | collapse | $u = \cosh\theta + 0.2\sinh\theta$ is finite at every finite $\theta$ and $\to \infty$ only as $\theta \to \infty$ (the particle reaches $r = 0$ in finite time after infinitely many turns); $\theta = 4.423$ is the integrator cutoff |
| $\alpha = 3$, $\mu/h^2 = 2$ | $(1, -1.5)$, $C_1 \lt 0$ | escape | $u = 0$ at $\theta = 0.805$ |
| $\alpha = 3$, $\mu/h^2 = 1/2$ | $(1, 0)$ | escape | $u = 0$ at $\theta = 2.222$ |
| $\alpha = 3$, $\mu = h^2$ | $(1, -0.1)$ | escape at $\theta = 10$ | $u = 0$ at $\theta = 10.000$ |
| $\alpha = 1$ | $(0.5, 0.3)$ | bounded | $u \in [0.471, 1.653]$ over $100$ rad |

The official key (Problems.pdf) gives no answer for Problem 42, so these checks are against the derived classification only.

---

## 📌 Problem 43: Two Connected Particles, Plane with Hole

### Phase 1: Physical Statement, Hypotheses & Parameters
* **System:** $P_1$ on a smooth horizontal plane at polar position $(r, \theta)$ and $P_2$ hanging on the vertical through the hole $O$, joined by an inextensible massless cord of length $2a$ passing through $O$.
* **Constraints and degrees of freedom:** the cord length gives $r + \ell_2 = 2a$, where $\ell_2$ is the hanging length, so $z_2 = -\ell_2 = r - 2a$ ($Oz$ up). The generalized coordinates are $(r, \theta)$, $\text{CDOF} = 2$.
* **Hypotheses:** inertial frame $S_0$ with $O$ at the hole; smooth hole and plane for parts (a)-(e); the cord stays taut; no drag.
* **Initial state:** $r(0) = a$, $\dot{r}(0) = 0$, $r(0)\dot{\theta}(0) = v_0$, hence $\dot{\theta}(0) = v_0/a$ and $\dot{z}_2(0) = 0$.

| Symbol | Meaning | SI unit |
|---|---|---|
| $m$ | mass of each particle | kg |
| $a$ | half of the cord length | m |
| $v_0$ | initial speed of $P_1$ | m/s |
| $g$ | gravitational acceleration | m/s$^2$ |
| $\mu$ | friction coefficient (part f) | 1 |

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* **Inertial frame:** $S_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$, horizontal plane $z = 0$, $\mathbf{k}$ up.
* **Change of basis (polar basis of $P_1$).** $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}\}$ is the inertial basis rotated by $\theta(t)$ about $\mathbf{k}$:
$$ [{}_0 R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0R_1] = 1, \qquad [{}_0R_1]^T[{}_0R_1] = I $$

with $\boldsymbol{\omega}_{10} = \dot{\theta}\,\mathbf{k}$, $\dot{\mathbf{e}}_r = \dot{\theta}\,\mathbf{e}_\theta$ and $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_r$ (Poisson).

* **Kinematics:** $\mathbf{r}_1 = r\mathbf{e}_r$, $\mathbf{v}_1 = \dot{r}\mathbf{e}_r + r\dot{\theta}\mathbf{e}_\theta$; $\mathbf{r}_2 = (r - 2a)\mathbf{k}$, $\mathbf{v}_2 = \dot{r}\mathbf{k}$.
$$ T_{\text{kin}} = \tfrac{1}{2}m\left(\dot{r}^2 + r^2\dot{\theta}^2\right) + \tfrac{1}{2}m\dot{r}^2 = m\dot{r}^2 + \tfrac{1}{2}mr^2\dot{\theta}^2, \qquad V = mgz_2 = mg(r - 2a) $$

### Phase 3: Step-by-Step Mathematical Deduction

#### (a) Circular motion, $r \equiv a$
* **Pedagogical Justification:** On the plane the only horizontal force on $P_1$ is the tension $-T\mathbf{e}_r$, which is central. For $r = a$ the radial acceleration is purely centripetal; $P_2$ must stay at rest.
$$ P_1: \; m\left(\ddot{r} - r\dot{\theta}^2\right) = -T \;\xrightarrow{\;r = a,\ \ddot{r} = 0\;}\; T = ma\dot{\theta}^2 = \frac{mv_0^2}{a}, \qquad P_2: \; m\ddot{z}_2 = T - mg = 0 \implies T = mg $$
$$ \frac{mv_0^2}{a} = mg \implies v_0 = \sqrt{ag} $$

#### (b) Tension in the circular case
$$ T = mg $$

#### (c) Quadratures for $v_0 = \sqrt{8ag/3}$
* **Pedagogical Justification:** The tension on $P_1$ is central, so $h = r^2\dot{\theta}$ is constant; the plane and hole are smooth and the cord inextensible, so $E = T_{\text{kin}} + V$ is constant. The two first integrals leave one equation for $r(t)$.
$$ h = r^2\dot{\theta} = a v_0 = a\sqrt{\frac{8ag}{3}} \implies h^2 = \frac{8}{3}a^3g $$
$$ E = m\dot{r}^2 + \frac{mh^2}{2r^2} + mg(r - 2a), \qquad E(0) = \tfrac{1}{2}m\cdot\frac{8ag}{3} - mga = \frac{1}{3}mga $$

Equating, dividing by $m$ and isolating $\dot{r}^2$:

$$ \dot{r}^2 + \frac{4a^3g}{3r^2} + gr - 2ga = \frac{1}{3}ga \implies \dot{r}^2 = \frac{7}{3}ga - gr - \frac{4a^3g}{3r^2} = \frac{g}{3r^2}\left(7ar^2 - 3r^3 - 4a^3\right) $$

Separating variables and applying Barrow's rule from $r(0) = a$:

$$ \frac{dr}{dt} = \pm\sqrt{\frac{g}{3}}\,\frac{\sqrt{-3r^3 + 7ar^2 - 4a^3}}{r} \implies \int_a^r\frac{r'\,dr'}{\sqrt{-3r'^3 + 7ar'^2 - 4a^3}} = \pm\sqrt{\frac{g}{3}}\,t $$

#### (d) Oscillation between $r = a$ and $r = 2a$
* **Pedagogical Justification:** Motion requires $\dot{r}^2 \ge 0$, i.e. $P(r) = -3r^3 + 7ar^2 - 4a^3 \ge 0$. With $x = r/a$ the polynomial is $a^3(-3x^3 + 7x^2 - 4)$, and the hint gives its roots.
$$ -3x^3 + 7x^2 - 4 = -(x - 1)(x - 2)(3x + 2) $$

Check of the roots: $x = 1$: $-3 + 7 - 4 = 0$; $x = 2$: $-24 + 28 - 4 = 0$; $x = -2/3$: $\frac{8}{9} + \frac{28}{9} - 4 = 0$. Since $r \gt 0$, $3x + 2 \gt 0$ and $P \ge 0$ requires $(x - 1)(x - 2) \le 0$:

$$ 1 \le x \le 2 \iff a \le r(t) \le 2a $$

The turning points ($\dot{r} = 0$) are $r_{\min} = a$ and $r_{\max} = 2a$, and the motion oscillates between them.

#### (e) Tension of the cord
* **Pedagogical Justification:** Apply Newton's second law to $P_2$ (weight and tension) with $\ddot{z}_2 = \ddot{r}$, because $z_2 = r - 2a$.
$$ m\ddot{r} = T - mg \implies T = m\left(g + \ddot{r}\right) $$

Differentiate $\dot{r}^2 = \frac{7}{3}ga - gr - \frac{4a^3g}{3r^2}$ with respect to time (chain rule, $\frac{d}{dt}r^{-2} = -2r^{-3}\dot{r}$):

$$ 2\dot{r}\ddot{r} = \left(-g + \frac{8a^3g}{3r^3}\right)\dot{r} \implies \ddot{r} = -\frac{g}{2} + \frac{4a^3g}{3r^3} $$
$$ \boxed{T = mg\left(\frac{1}{2} + \frac{4a^3}{3r^3}\right)} $$

$T \gt 0$ for all $r \in [a, 2a]$, so the cord stays taut.

#### (f) Rough plane
* **Pedagogical Justification:** Coulomb friction acts on $P_1$ opposite to its velocity, with magnitude $\mu N_1$. The normal force is $N_1 = mg$, because the cord is horizontal on the plane and only the weight acts vertically.
$$ \mathbf{F}_f = -\mu mg\,\frac{\mathbf{v}_1}{\|\mathbf{v}_1\|} = -\mu mg\,\frac{\dot{r}\,\mathbf{e}_r + r\dot{\theta}\,\mathbf{e}_\theta}{\sqrt{\dot{r}^2 + r^2\dot{\theta}^2}} $$
$$ \mathbf{e}_r: \; m\left(\ddot{r} - r\dot{\theta}^2\right) = -T - \mu mg\frac{\dot{r}}{\sqrt{\dot{r}^2 + r^2\dot{\theta}^2}} $$
$$ \mathbf{e}_\theta: \; m\left(r\ddot{\theta} + 2\dot{r}\dot{\theta}\right) = -\mu mg\frac{r\dot{\theta}}{\sqrt{\dot{r}^2 + r^2\dot{\theta}^2}}, \qquad P_2: \; m\ddot{r} = T - mg $$

Adding the $\mathbf{e}_r$ equation and the $P_2$ equation eliminates $T$; multiplying the $\mathbf{e}_\theta$ equation by $r$ gives the evolution of $h$:

$$ 2\ddot{r} - r\dot{\theta}^2 = -g - \mu g\frac{\dot{r}}{\sqrt{\dot{r}^2 + r^2\dot{\theta}^2}}, \qquad \frac{d}{dt}\left(r^2\dot{\theta}\right) = -\mu g\,\frac{r^2\dot{\theta}}{\sqrt{\dot{r}^2 + r^2\dot{\theta}^2}} $$

Angular momentum and energy are no longer conserved (friction dissipates energy), so the problem cannot be reduced to the quadratures of (c).

### Phase 4: Physical Interpretation & Dimensional Verification
* **Tension at the turning points:** $T(a) = mg\left(\tfrac{1}{2} + \tfrac{4}{3}\right) = \tfrac{11}{6}mg$ and $T(2a) = mg\left(\tfrac{1}{2} + \tfrac{4}{24}\right) = \tfrac{2}{3}mg$, both positive.
* **Consistency with (a):** for $v_0^2 = ag$, $h^2 = a^3g$ and $\ddot{r}(a) = -\tfrac{g}{2} + \tfrac{h^2}{2a^3} = 0$, so $r = a$ is an equilibrium of the radial equation, as expected for the circular case.
* **Radial period** (consequence of (c) and (d)): with $x = r/a$ and $x = \tfrac{3}{2} - \tfrac{1}{2}\cos s$, $(x - 1)(2 - x) = \tfrac{1}{4}\sin^2 s$ and $dx = \tfrac{1}{2}\sin s\,ds$, so $\tau_r = 2\sqrt{\dfrac{3a}{g}}\displaystyle\int_0^\pi\dfrac{x(s)\,ds}{\sqrt{3x(s) + 2}} \approx 6.342\sqrt{\dfrac{a}{g}}$.
* **Numerical check** (Python, RK4 on $\ddot{r} = -g/2 + 4a^3g/(3r^3)$ with $a = g = 1$, $r(0) = 1$, $\dot{r}(0) = 0$): maximum radius $2.0000$, period $6.3425$ s (the quadrature gives $6.3424$), and the energy-integral residual stays below $4\times 10^{-14}$.
* **Dimensions:** $[T] = [m][g] = \text{N}$ and $[v_0] = \sqrt{[a][g]} = \text{m/s}$.
* **Key:** the official key (Problems.pdf) has no entry for Problem 43.

---

## 📌 Problem 44: The Little Prince Throwing Seeds

### Phase 1: Physical Statement, Hypotheses & Parameters
* **System:** a seed of mass $m \ll M$ launched from the surface ($r_0 = R$) with speed $v_0$ at $60^\circ$ above the local horizontal; it reaches the apocenter $r_a = 3R$.
* **Hypotheses:** spherically symmetric, non-rotating asteroid, so the gravitational force $\mathbf{F} = -\dfrac{GMm}{r^2}\mathbf{e}_r$ is central and conservative with $\mu = GM$; vacuum (no drag); inertial frame $S_0$ centred on the asteroid.
* **Degrees of freedom:** free particle, planar motion by central-force conservation of $\mathbf{H}_O$; coordinates $(r, \theta)$.
* **Initial state:** $r = R$, radial component $v_{r0} = v_0\sin 60^\circ = \tfrac{\sqrt{3}}{2}v_0$ and transverse component $v_{\theta 0} = v_0\cos 60^\circ = \tfrac{1}{2}v_0$.

| Symbol | Meaning | SI unit |
|---|---|---|
| $M$, $R$ | mass and radius of the asteroid | kg, m |
| $G$ | universal gravitational constant, $6.6743\times 10^{-11}$ | m$^3$/(kg s$^2$) |
| $\mu = GM$ | gravitational parameter | m$^3$/s$^2$ |
| $\beta$ | launch angle above the horizontal | $60^\circ$ |
| $r_a$ | apocenter radius | $3R$ |

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* **Change of basis (polar basis in the orbital plane).** $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}\}$ is the inertial basis rotated by the true anomaly $\theta$ about $\mathbf{k}$ (along $\mathbf{H}_O$):
$$ [{}_0 R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0R_1] = 1, \qquad [{}_0R_1]^T[{}_0R_1] = I $$
* **Velocity in $\mathcal{B}_1$:** $\mathbf{v} = \dot{r}\,\mathbf{e}_r + r\dot{\theta}\,\mathbf{e}_\theta$; at launch $\dot{r} = v_0\sin 60^\circ$ and $r\dot{\theta} = v_0\cos 60^\circ$. At the apocenter $\dot{r} = 0$, so the velocity is purely transverse.

### Phase 3: Step-by-Step Mathematical Deduction

#### 1. Conservation of specific angular momentum
* **Pedagogical Justification:** The gravitational force passes through $O$, so $\mathbf{M}_O = \mathbf{0}$ and $h = \|\mathbf{r}\times\mathbf{v}\| = r^2\dot{\theta}$ is constant. Evaluate it at launch and at the apocenter, where $v_a = r_a\dot{\theta}_a$.
$$ h = R\left(v_0\cos 60^\circ\right) = \frac{1}{2}Rv_0, \qquad h = r_av_a = 3Rv_a \implies v_a = \frac{v_0}{6} $$

#### 2. Conservation of specific energy
* **Pedagogical Justification:** Gravity is conservative with $V_0 = -\mu/r$ (derived with Barrow's rule, reference at infinity), so $\xi = \tfrac{1}{2}v^2 - GM/r$ takes the same value at launch and at the apocenter.
$$ \frac{1}{2}v_0^2 - \frac{GM}{R} = \frac{1}{2}\left(\frac{v_0}{6}\right)^2 - \frac{GM}{3R} = \frac{v_0^2}{72} - \frac{GM}{3R} $$

#### 3. Solving for $v_0$
$$ \left(\frac{1}{2} - \frac{1}{72}\right)v_0^2 = \left(1 - \frac{1}{3}\right)\frac{GM}{R} \implies \frac{35}{72}v_0^2 = \frac{2}{3}\frac{GM}{R} \implies v_0^2 = \frac{2}{3}\cdot\frac{72}{35}\frac{GM}{R} = \frac{48}{35}\frac{GM}{R} $$
$$ \boxed{v_0 = \sqrt{\frac{48}{35}\,\frac{GM}{R}}} $$

### Phase 4: Physical Interpretation & Dimensional Verification
* **Bound orbit:** the escape speed at the surface is $v_e = \sqrt{2GM/R}$, i.e. $v_e^2 = \tfrac{70}{35}GM/R$. Since $\tfrac{48}{35} \lt 2$, $v_0 \lt v_e$ and the orbit is an ellipse: the seed falls back.
* **Orbital parameters:** $h^2 = \tfrac{1}{4}R^2v_0^2 = \tfrac{12}{35}GMR$, $p = h^2/\mu = \tfrac{12}{35}R$. From $r_a = p/(1 - e) = 3R$: $1 - e = \tfrac{4}{35}$ and $e = \tfrac{31}{35} \approx 0.8857$. The periapsis of the full conic is $r_p = p/(1 + e) = \tfrac{2}{11}R \lt R$, inside the asteroid; only the arc from the launch point to the apocenter is physical, and the seed lands before reaching the periapsis.
* **Independent check with the Binet solution.** With $u = \tfrac{\mu}{h^2}(1 + e\cos\theta)$ and the launch values $u(\theta_0) = 1/R$, $u'(\theta_0) = -\dot{r}/h$ (here $\dot{r} = \tfrac{\sqrt{3}}{2}v_0$), the eccentricity formula of the theory page gives
$$ e = \frac{h^2}{\mu}\sqrt{\left(\frac{1}{R} - \frac{\mu}{h^2}\right)^2 + \left(\frac{\dot{r}}{h}\right)^2} = \frac{12R}{35}\sqrt{\frac{529}{144R^2} + \frac{3}{R^2}} = \frac{12R}{35}\cdot\frac{31}{12R} = \frac{31}{35} $$

and the launch angle follows from $\tan\beta = \dot{r}/(r\dot{\theta}) = \dfrac{R}{p}\,e\sin\theta_0$ with $\cos\theta_0 = \dfrac{p/R - 1}{e} = -\dfrac{23}{31}$, $\sin\theta_0 = \dfrac{\sqrt{432}}{31}$:

$$ \tan\beta = \frac{35}{12}\cdot\frac{31}{35}\cdot\frac{\sqrt{432}}{31} = \frac{\sqrt{432}}{12} = \sqrt{3} \implies \beta = 60^\circ $$
* **Numerical check** (Python, velocity-Verlet integration of $\ddot{\mathbf{r}} = -\mu\mathbf{r}/r^3$ with $\mu = R = 1$ and $v_0 = \sqrt{48/35}$): the maximum radius reached is $2.99999999981R$, in agreement with $r_a = 3R$.
* **Dimensions:** $[v_0] = \sqrt{[G][M]/[R]} = \sqrt{\dfrac{\text{m}^3}{\text{kg}\,\text{s}^2}\cdot\dfrac{\text{kg}}{\text{m}}} = \text{m/s}$.
* **Key:** the official key (Problems.pdf) has no entry for Problem 44.
