---
title: "Solution Set - Topic 3: Constraints and Reaction Forces"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Full Analytical Solutions (4-Phase Methodology)"
language: "English"
tags:
  - solutions
  - constraints
---

# 📚 Topic 3: Constraints and Reaction Forces - Full Analytical Solutions

Exhaustive, step-by-step analytical solutions for all 12 solvable problems from Topic 3 (**Constraints and Reaction Forces**) of *Mechanics Applied to Aerospace Engineering* (UC3M). Every problem adheres to the mandatory 4-phase pedagogical methodology, with explicit justification prior to every equation, zero algebraic omissions, explicit derivative developments (product, quotient, and chain rules), explicit integral evaluations (substitutions, primitives, and Barrow's rule), rotation matrices $[{}_0 R_1]$, normal and tangent subspaces ($V_N, V_T$), and dimensional verifications.

---

## 📌 Problem 18: Heavy Particle on a Cone

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a heavy particle of mass $m$ moves without friction on the interior of the cone $z^2 = x^2 + y^2$, $z \gt 0$. The frame $Oxyz$ is inertial and $Oz$ is the ascending vertical.
* **Constraint:** the particle stays on the surface, $\Phi(x, y, z) = x^2 + y^2 - z^2 = 0$ (holonomic, scleronomic). It is unilateral in principle (the particle can leave the cone if the reaction would have to pull it), so we verify $N \ge 0$ at the end. The surface is smooth, so the reaction is normal to it.
* **Degrees of freedom:** $\text{CDOF} = 3 - 1 = 2$. We choose the cylindrical coordinates $(r, \theta)$ and, on the cone, $z = r$.
* **Initial state:** position $(a, 0, a)$, i.e. $r(0) = a$, $\theta(0) = 0$, $z(0) = a$; velocity $\sqrt{ag}\,\mathbf{j}$, i.e. $\dot{r}(0) = 0$, $r(0)\dot{\theta}(0) = \sqrt{ag}$, $\dot{z}(0) = 0$.
* **Parameters:** $m$ [kg], $g$ [m/s$^2$], $a$ [m].

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $\mathcal{F}_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$ with $\mathbf{k}$ vertical upward.
* **Cylindrical basis:** $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}\}$, the inertial basis rotated by $\theta(t)$ about $\mathbf{k}$:
$$ [{}_0 R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = \cos^2\theta + \sin^2\theta = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
Multiplying out, $RR^T$ has diagonal entries $\cos^2 + \sin^2 = 1$ of the rotation angle (and $1$) and off-diagonal entries $\pm(\cos\sin - \sin\cos) = 0$, so it is the identity.
* The angular velocity of $\mathcal{B}_1$ is $\boldsymbol{\omega}_{10} = \dot{\theta}\,\mathbf{k}$, so Poisson's formula gives $\dot{\mathbf{e}}_r = \dot{\theta}\,\mathbf{e}_\theta$ and $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_r$.
* **Surface-adapted basis.** On the cone $z = r$ (slope $45^\circ$) the unit generator is $\mathbf{e}_g = (\mathbf{e}_r + \mathbf{k})/\sqrt{2}$ and the unit normal pointing into the cone, where the particle lies, is $\mathbf{n}_{in} = (\mathbf{k} - \mathbf{e}_r)/\sqrt{2}$. The triple $\{\mathbf{e}_g, \mathbf{e}_\theta, \mathbf{n}_{in}\}$ is right-handed ($\mathbf{e}_g\times\mathbf{e}_\theta = \mathbf{n}_{in}$) and its components in $\mathcal{B}_1$ are the columns of
$$ [{}_1 R_2] = \begin{pmatrix} 1/\sqrt{2} & 0 & -1/\sqrt{2} \\ 0 & 1 & 0 \\ 1/\sqrt{2} & 0 & 1/\sqrt{2} \end{pmatrix}, \qquad \det[{}_1 R_2] = \tfrac{1}{2} + \tfrac{1}{2} = 1, \qquad [{}_1 R_2][{}_1 R_2]^T = I $$

### Phase 3: Derivation

#### 3.1 Kinematics
* **Pedagogical Justification:** the position is written with the cylindrical coordinates and the constraint $z = r$ is applied before differentiating, so that only the free coordinates $(r, \theta)$ remain. The derivatives of $\mathbf{e}_r$ use Poisson's formula.
$$ \mathbf{r} = r\,\mathbf{e}_r + r\,\mathbf{k}, \qquad \mathbf{v} = \dot{r}\,\mathbf{e}_r + r\dot{\theta}\,\mathbf{e}_\theta + \dot{r}\,\mathbf{k}, \qquad v^2 = 2\dot{r}^2 + r^2\dot{\theta}^2 $$
$$ \mathbf{a} = \left(\ddot{r} - r\dot{\theta}^2\right)\mathbf{e}_r + \left(r\ddot{\theta} + 2\dot{r}\dot{\theta}\right)\mathbf{e}_\theta + \ddot{r}\,\mathbf{k} $$

#### 3.2 Forces
* **Applied force:** the weight $-mg\,\mathbf{k}$ (conservative, $V = mgz = mgr$).
* **Constraint force:** the reaction of the smooth cone, normal to the surface, i.e. along $\nabla\Phi \propto \mathbf{e}_r - \mathbf{k}$. With an unknown magnitude $\nu$ (positive when pressing the particle against the surface from inside), $\mathbf{N} = \nu\,\mathbf{n}_{in} = \dfrac{\nu}{\sqrt{2}}\left(\mathbf{k} - \mathbf{e}_r\right)$. It has no $\mathbf{e}_\theta$ component.
* **Inertia forces:** none ($S_0$ is inertial).

#### 3.3 Equations of Motion
* **Pedagogical Justification:** Newton's second law in $S_0$ projected on the cylindrical basis gives three scalar equations for the three unknowns $r$, $\theta$ and $\nu$ (the constraint $z = r$ is already used):
$$ \mathbf{e}_r: \; m\left(\ddot{r} - r\dot{\theta}^2\right) = -\frac{\nu}{\sqrt{2}}, \qquad \mathbf{e}_\theta: \; m\left(r\ddot{\theta} + 2\dot{r}\dot{\theta}\right) = 0, \qquad \mathbf{k}: \; m\ddot{r} = \frac{\nu}{\sqrt{2}} - mg $$
* **Dynamical decoupling.** Adding the $\mathbf{e}_r$ and $\mathbf{k}$ equations eliminates the reaction, which is then obtained from the last equation once $r(t)$ is known: $2\ddot{r} - r\dot{\theta}^2 = -g$.
* **First integral from $\mathbf{e}_\theta$.** The azimuthal acceleration is $r\ddot{\theta} + 2\dot{r}\dot{\theta} = \frac{1}{r}\frac{d}{dt}\left(r^2\dot{\theta}\right)$ (product rule), so $r^2\dot{\theta}$ is constant:
$$ \frac{d}{dt}\left(r^2\dot{\theta}\right) = 0 \implies r^2\dot{\theta} = r(0)^2\dot{\theta}(0) = a\sqrt{ag} \implies \dot{\theta} = \frac{a\sqrt{ga}}{r^2} $$
* **Energy.** The reaction does no work ($\mathbf{N}\cdot\mathbf{v} = 0$ because $\mathbf{N}$ is normal to the surface and $\mathbf{v}$ is tangent to it) and gravity is conservative, so $E = \tfrac{1}{2}mv^2 + mgz$ is constant. This is a first integral of the equations above and replaces the radial equation:
$$ E = \tfrac{1}{2}m\left(2\dot{r}^2 + r^2\dot{\theta}^2\right) + mgr = \tfrac{1}{2}m(ag) + mga = \tfrac{3}{2}mga $$

#### 3.4 Integration and Answers
##### Reduction to quadratures
* **Pedagogical Justification:** substitute $\dot{\theta} = a\sqrt{ga}/r^2$ in the energy, so that only $r$ and $\dot{r}$ remain, and isolate $\dot{r}^2$:
$$ m\dot{r}^2 + \frac{mga^3}{2r^2} + mgr = \frac{3}{2}mga \implies \dot{r}^2 = \frac{3}{2}ga - gr - \frac{ga^3}{2r^2} = \frac{g}{2r^2}\left(3ar^2 - 2r^3 - a^3\right) $$
* **General quadrature.** For arbitrary initial data, with energy $E$ and $h = r^2\dot{\theta}$, the same steps give $m\dot{r}^2 + \dfrac{mh^2}{2r^2} + mgr = E$, and separating variables with Barrow's rule from $r(0) = r_0$:
$$ \int_{r_0}^{r}\frac{dr'}{\sqrt{\dfrac{E - mgr'}{m} - \dfrac{h^2}{2r'^2}}} = \pm\int_0^tdt' = \pm t, \qquad \theta(t) = \theta_0 + \int_0^t\frac{h}{r(t')^2}\,dt' $$
* **These initial data** ($E = \tfrac32 mga$, $h = a\sqrt{ga}$, $r_0 = a$) give the radicand $\dfrac{g}{2r^2}\left(-2r^3 + 3ar^2 - a^3\right)$, which is shown below to be $\le 0$ and to vanish only at $r = a$; the separation of variables is then not possible ($\dot{r} \equiv 0$) and the motion is found directly:

##### Maximum and minimum of $z = r$
* **Pedagogical Justification:** the turning points of $r$ are the roots of $\dot{r}^2 = 0$, i.e. of $P(r) = -2r^3 + 3ar^2 - a^3$. Since the particle starts at $r = a$ with $\dot{r}(0) = 0$, $r = a$ is a root: $2a^3 - 3a^3 + a^3 = 0$. Dividing $2r^3 - 3ar^2 + a^3$ by $(r - a)$ (check: $(r - a)(2r^2 - ar - a^2) = 2r^3 - ar^2 - a^2r - 2ar^2 + a^2r + a^3 = 2r^3 - 3ar^2 + a^3$):
$$ 2r^3 - 3ar^2 + a^3 = (r - a)\left(2r^2 - ar - a^2\right) = (r - a)(r - a)(2r + a) = (r - a)^2(2r + a) $$
* Therefore
$$ \dot{r}^2 = -\frac{g\,(2r + a)}{2r^2}\,(r - a)^2 $$
For $r \gt 0$ the factor $(2r + a)$ is positive, so the right-hand side is $\le 0$, and it vanishes only at $r = a$. Since $\dot{r}^2 \ge 0$, the only possible motion is
$$ \boxed{r(t) \equiv a, \qquad z_{\max} = z_{\min} = a} $$
The data of the problem are exactly those of a circular orbit at constant height.

### Phase 4: Interpretation & Checks
* **Steady circular orbit:** the initial speed $\sqrt{ag}$ is the circular-orbit speed on the cone, $v^2 = gr\tan\gamma$ with $\tan\gamma = dz/dr = 1$. The particle sits at the minimum of the effective potential $V_{\text{eff}}(r) = mgr + \dfrac{ma^3g}{2r^2}$ and describes a horizontal circle with $\dot{\theta} = \sqrt{g/a}$.
* **Reaction on the orbit.** With $r = a$ and $\dot{\theta}^2 = g/a$ the acceleration is $\mathbf{a} = -g\,\mathbf{e}_r$. From $\mathbf{N} - mg\,\mathbf{k} = m\mathbf{a}$: $\mathbf{N} = mg\left(\mathbf{k} - \mathbf{e}_r\right) = \sqrt{2}\,mg\,\mathbf{n}_{in}$, so $\nu = \sqrt{2}\,mg \gt 0$: the cone pushes the particle, and the unilateral constraint stays active.
* **Stability.** The effective inertia of the $r$-motion is $2m$ (the kinetic energy has $2\dot{r}^2$) and $V_{\text{eff}}''(a) = 3mg/a$, hence $\omega_r^2 = 3g/(2a)$: small radial oscillations have period $2\pi/\sqrt{3g/(2a)}$.
* **Dimensional check:** $[r^2\dot{\theta}] = \text{m}^2\text{s}^{-1}$ and $[ga^3/r^2] = \text{m}^2\text{s}^{-2}$, like $[\dot{r}^2]$, so every term of the energy equation has the same units.
* **Check against the official key:** `Problems.pdf` has no entry for Problem 18 in its solution keys, so the result is verified by independent derivation. Sympy confirms $\dot{r}^2 = -g(a - r)^2(a + 2r)/(2r^2)$ and $\mathbf{N} = mg(\mathbf{k} - \mathbf{e}_r)$ with $\|\mathbf{N}\| = \sqrt{2}\,mg$. Numerical integration ($g = a = 1$) keeps $r = 1$ to $10^{-12}$, and for a perturbed start $r(0) = 1.001$ the radial period is $5.13020$, against $2\pi/\sqrt{3/2} = 5.13020$.

---

## 📌 Problem 19: Heavy Particle on a Paraboloid

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a heavy particle of mass $m$ moves without friction on the paraboloid of revolution $az = r^2$, with $a \gt 0$ and $r = \sqrt{x^2 + y^2}$.
* **Constraint:** $f(x, y, z) = x^2 + y^2 - az = 0$ (holonomic, scleronomic, smooth). The particle is inside the bowl; the reaction must press it against the surface ($\nu \gt 0$), which is verified in 3.3.
* **Degrees of freedom:** $\text{CDOF} = 3 - 1 = 2$, with the cylindrical coordinates $(r, \theta)$ and $z = r^2/a$.
* **Initial state:** $r(0) = a$ (so $z(0) = a$) and velocity $v_0$ tangent to the local parallel: $\mathbf{v}_0 = v_0\,\mathbf{e}_\theta$, i.e. $\dot{r}(0) = 0$, $\dot{\theta}(0) = v_0/a$, $\dot{z}(0) = 0$.
* **Parameters:** $m$ [kg], $a$ [m], $g$ [m/s$^2$], $v_0$ [m/s].

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $\mathcal{F}_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$ with $\mathbf{k}$ vertical upward.
* **Cylindrical basis:** $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}\}$, obtained from $\mathcal{B}_0$ by a rotation $\theta(t)$ about $\mathbf{k}$:
$$ [{}_0 R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
Multiplying out, $RR^T$ has diagonal entries $\cos^2 + \sin^2 = 1$ of the rotation angle (and $1$) and off-diagonal entries $\pm(\cos\sin - \sin\cos) = 0$, so it is the identity.
* **Surface-adapted basis.** With $s = \sqrt{1 + 4r^2/a^2}$, the unit tangent along the meridian is $\mathbf{e}_g = \left(\mathbf{e}_r + \tfrac{2r}{a}\mathbf{k}\right)/s$ and the unit normal pointing into the bowl is $\mathbf{n}_{in} = \left(\mathbf{k} - \tfrac{2r}{a}\mathbf{e}_r\right)/s$, proportional to $-\nabla f = -2r\,\mathbf{e}_r + a\,\mathbf{k}$. Since $\mathbf{e}_g\times\mathbf{e}_\theta = \mathbf{n}_{in}$ the triple is right-handed, and
$$ [{}_1 R_2] = \begin{pmatrix} 1/s & 0 & -2r/(as) \\ 0 & 1 & 0 \\ 2r/(as) & 0 & 1/s \end{pmatrix}, \qquad \det[{}_1 R_2] = \frac{1}{s^2} + \frac{4r^2}{a^2s^2} = 1, \qquad [{}_1 R_2][{}_1 R_2]^T = I $$

### Phase 3: Derivation

#### 3.1 Kinematics
* **Pedagogical Justification:** the constraint is used to write $z = r^2/a$ and its derivatives with the chain rule, so that only $(r, \theta)$ remain.
$$ z = \frac{r^2}{a}, \qquad \dot{z} = \frac{2r\dot{r}}{a}, \qquad \ddot{z} = \frac{2}{a}\left(\dot{r}^2 + r\ddot{r}\right) $$
$$ \mathbf{v} = \dot{r}\,\mathbf{e}_r + r\dot{\theta}\,\mathbf{e}_\theta + \frac{2r\dot{r}}{a}\,\mathbf{k}, \qquad v^2 = \dot{r}^2\left(1 + \frac{4r^2}{a^2}\right) + r^2\dot{\theta}^2 $$
$$ \mathbf{a} = \left(\ddot{r} - r\dot{\theta}^2\right)\mathbf{e}_r + \left(r\ddot{\theta} + 2\dot{r}\dot{\theta}\right)\mathbf{e}_\theta + \ddot{z}\,\mathbf{k} $$

#### 3.2 Forces
* **Applied force:** the weight $-mg\,\mathbf{k}$, with $V = mgz = mgr^2/a$.
* **Constraint force:** the reaction of the smooth surface along $\mathbf{n}_{in}$ (no $\mathbf{e}_\theta$ component, because $\nabla f = 2r\,\mathbf{e}_r - a\,\mathbf{k}$ has none): $\mathbf{N} = \nu\,\mathbf{n}_{in} = \dfrac{\nu}{s}\left(\mathbf{k} - \dfrac{2r}{a}\mathbf{e}_r\right)$. **Inertia forces:** none.

#### 3.3 Equations of Motion
* **Pedagogical Justification:** Newton's second law in $S_0$ gives three scalar equations for the unknowns $r$, $\theta$ and $\nu$:
$$ \mathbf{e}_r: \; m\left(\ddot{r} - r\dot{\theta}^2\right) = -\frac{2r}{as}\,\nu, \qquad \mathbf{e}_\theta: \; m\left(r\ddot{\theta} + 2\dot{r}\dot{\theta}\right) = 0, \qquad \mathbf{k}: \; m\ddot{z} = \frac{\nu}{s} - mg $$
* **Decoupling.** Eliminating $\nu/s$ between the $\mathbf{e}_r$ and $\mathbf{k}$ equations gives one second-order equation for $r$ (the reaction is computed afterwards from the $\mathbf{k}$ equation, see below).
* **Reaction.** From the $\mathbf{k}$ equation $\nu/s = m(\ddot{z} + g)$. The $\mathbf{e}_r$ equation gives $\ddot{r} - r\dot{\theta}^2 = -\frac{2r}{a}(\ddot{z} + g)$; with $\ddot{z} = \frac{2}{a}(\dot{r}^2 + r\ddot{r})$ this is $r\ddot{r}\,s^2 = r^2\dot{\theta}^2 - \frac{4r^2\dot{r}^2}{a^2} - \frac{2gr^2}{a}$, hence $\dot{r}^2 + r\ddot{r} = \left(\dot{r}^2 + r^2\dot{\theta}^2 - \frac{2gr^2}{a}\right)/s^2$ and, using $g s^2 - 4gr^2/a^2 = g$,
$$ \ddot{z} + g = \frac{g + \frac{2}{a}\left(\dot{r}^2 + r^2\dot{\theta}^2\right)}{s^2} \implies \nu = \frac{m}{s}\left[g + \frac{2}{a}\left(\dot{r}^2 + r^2\dot{\theta}^2\right)\right] \gt 0 $$
so the surface always pushes the particle and the motion is admissible for any $v_0$.
* **First integral from $\mathbf{e}_\theta$.** As in Problem 18, $\frac{1}{r}\frac{d}{dt}\left(r^2\dot{\theta}\right) = 0$, so
$$ r^2\dot{\theta} = r(0)^2\dot{\theta}(0) = a^2\cdot\frac{v_0}{a} = av_0 \implies \dot{\theta} = \frac{av_0}{r^2} $$
* **Energy.** The reaction does no work ($\mathbf{N}\cdot\mathbf{v} = 0$) and gravity is conservative, so $E = \tfrac{1}{2}mv^2 + mg\dfrac{r^2}{a}$ is constant. At $t = 0$: $E = \tfrac{1}{2}mv_0^2 + mga$.

#### 3.4 Integration and Answers
##### Reduction to quadratures
* **Pedagogical Justification:** substitute $\dot{\theta} = av_0/r^2$ in the energy and multiply by $2/m$:
$$ \dot{r}^2\left(1 + \frac{4r^2}{a^2}\right) + \frac{a^2v_0^2}{r^2} + \frac{2gr^2}{a} = v_0^2 + 2ga \quad\Longleftrightarrow\quad \dot{r}^2\left(1 + \frac{4r^2}{a^2}\right) + r^2\left(\dot{\theta}^2 + \frac{2g}{a}\right) = v_0^2 + 2ga $$
* Isolating $\dot{r}$, taking the square root and separating variables (Barrow's rule from $r(0) = a$, $t = 0$):
$$ \dot{r}^2 = \frac{v_0^2 + 2ga - a^2v_0^2/r^2 - 2gr^2/a}{1 + 4r^2/a^2} \implies \int_a^r\sqrt{\frac{1 + 4r'^2/a^2}{v_0^2 + 2ga - a^2v_0^2/r'^2 - 2gr'^2/a}}\,dr' = \pm\int_0^tdt' = \pm t $$
with $\theta(t) = \displaystyle\int_0^t\frac{av_0}{r(t')^2}\,dt'$.

##### Maximum and minimum of $r$
* **Pedagogical Justification:** the turning points satisfy $\dot{r} = 0$. Multiplying the numerator by $-ar^2$ and writing $u = r^2$:
$$ 2gu^2 - a\left(v_0^2 + 2ga\right)u + a^3v_0^2 = 0 $$
* Since the particle starts at $r = a$ with $\dot{r} = 0$, $u = a^2$ is a root: $2ga^4 - a^3v_0^2 - 2ga^4 + a^3v_0^2 = 0$. Factorising:
$$ 2gu^2 - a\left(v_0^2 + 2ga\right)u + a^3v_0^2 = \left(u - a^2\right)\left(2gu - av_0^2\right) = 0 \implies r_1 = a, \qquad r_2 = v_0\sqrt{\frac{a}{2g}} $$
* **Case $v_0 \lt \sqrt{2ga}$:** $r_2 \lt a$, so $r_{\max} = a$ and $r_{\min} = v_0\sqrt{a/(2g)}$. The particle falls toward the vertex, reaches $r_{\min}$ and climbs back to $a$.
* **Case $v_0 = \sqrt{2ga}$:** $r_2 = a$, a double root: $r_{\min} = r_{\max} = a$, a horizontal circular orbit.
* **Case $v_0 \gt \sqrt{2ga}$:** $r_2 \gt a$, so $r_{\min} = a$ and $r_{\max} = v_0\sqrt{a/(2g)}$. The particle climbs to $r_{\max}$ and falls back to $a$.

### Phase 4: Interpretation & Checks
* **Circular orbit (case $v_0^2 = 2ga$):** the quadratic becomes $2gu^2 - 4ga^2u + 2ga^4 = 2g\left(u - a^2\right)^2$, a double root, so $\dot{r} \equiv 0$. This agrees with the circular-orbit condition $v^2 = gr\tan\gamma$ with $\tan\gamma = dz/dr = 2r/a = 2$ at $r = a$.
* **Limit $v_0 \to 0$:** $r_{\min} \to 0$, the particle drops to the vertex, as expected for a body released at rest.
* **Dimensional check:** $[v_0^2 + 2ga] = [a^2v_0^2/r^2] = [2gr^2/a] = \text{m}^2/\text{s}^2$, and $\left[v_0\sqrt{a/(2g)}\right] = \text{m}$.
* **Check against the official key:** the key of `Problems.pdf` gives the quadrature $\dot{r}^2\left(1 + 4r^2/a^2\right) + r^2\left(\dot{\theta}^2 + 2g/a\right) = v_0^2 + 2ga$ with $r^2\dot{\theta} = av_0$, and the extremes: if $v_0 \lt \sqrt{2ga}$, $r_{\max} = a$ and $r_{\min} = v_0\sqrt{a/(2g)}$; if $v_0 = \sqrt{2ga}$, $r = a$ is constant; if $v_0 \gt \sqrt{2ga}$, $r_{\min} = a$ and $r_{\max} = v_0\sqrt{a/(2g)}$. All coincide with the results above. Numerical integration of the radial equation ($g = a = 1$) gives the turning points $0.707107$ for $v_0 = 1$, $1.000000$ for $v_0 = \sqrt{2}$ and $1.414214$ for $v_0 = 2$, equal to $v_0\sqrt{a/(2g)}$.

---

## 📌 Problem 23: Simple Pendulum

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a particle of mass $m$ hangs from a string of length $L$ fixed at the pivot $O$, or equivalently moves along the smooth interior of a vertical circle of radius $L$. In part (b) the circle rotates about the vertical diameter with the constant angular velocity $\omega$.
* **Constraints:** the particle stays on the circle, $|\mathbf{r}| = L$ in the vertical plane. Free in space it has 3 coordinates; the plane and the circle are two holonomic constraints, so $\text{CDOF} = 3 - 2 = 1$, with the angle $\theta$ measured from the downward vertical. The constraint is **unilateral**: the particle can leave the circle if the reaction would have to become negative ($N = 0$, or slack string). In part (b) the plane turns at the prescribed rate, so the constraint depends explicitly on time (rheonomic); it is solved in the inertial frame.
* **Initial motion:** pushed from the lowest point ($\theta = 0$) with speed $v_0$.
* **Parameters:** $m$ [kg], $L$ [m], $g$ [m/s$^2$], $v_0$ [m/s], $\omega \ge 0$ [rad/s].

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $\mathcal{F}_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$ with $\mathbf{k}$ vertical upward and the circle in the plane $Oxz$ for part (a).
* **Polar basis in the plane**, with $\theta$ from the downward vertical:
$$ \mathbf{e}_r = \sin\theta\,\mathbf{i} - \cos\theta\,\mathbf{k} \ \ (\text{outward}), \qquad \mathbf{e}_\theta = \cos\theta\,\mathbf{i} + \sin\theta\,\mathbf{k} \ \ (\text{along increasing } \theta) $$
* **Change of basis.** The triple $\{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{j}\}$ has $\mathbf{e}_r\times\mathbf{e}_\theta = -\mathbf{j}$, so it is left-handed. The right-handed polar triple is $\{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{e}_3\}$ with $\mathbf{e}_3 = -\mathbf{j}$ (the third vector plays no role in the planar kinematics). Its columns in $\mathcal{B}_0 = \{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$ give
$$ [{}_0 R_1] = \begin{pmatrix} \sin\theta & \cos\theta & 0 \\ 0 & 0 & -1 \\ -\cos\theta & \sin\theta & 0 \end{pmatrix}, \qquad \det[{}_0 R_1] = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
Multiplying out, $RR^T$ has diagonal entries $\cos^2 + \sin^2 = 1$ of the rotation angle (and $1$) and off-diagonal entries $\pm(\cos\sin - \sin\cos) = 0$, so it is the identity.
* The angular velocity of the basis is $\boldsymbol{\omega}_{10} = \dot{\theta}\,\mathbf{e}_3 = -\dot{\theta}\,\mathbf{j}$, and Poisson's formula gives $\dot{\mathbf{e}}_r = \dot{\theta}\,\mathbf{e}_\theta$ and $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_r$.
* **For part (b)**, the cylindrical basis $\{\mathbf{e}_\rho, \mathbf{e}_\varphi, \mathbf{k}\}$ is obtained from $\mathcal{B}_0$ by the simple rotation $\mathrm{R}_z(\omega t)$ about $\mathbf{k}$ (matrix $\begin{pmatrix}\cos \omega t & -\sin \omega t & 0\\ \sin \omega t & \cos \omega t & 0\\ 0 & 0 & 1\end{pmatrix}$, $\det = \cos^2\omega t + \sin^2\omega t = 1$; $RR^T$ has diagonal entries $\cos^2\omega t + \sin^2\omega t = 1$ (and $1$) and off-diagonal entries $\cos \omega t\sin \omega t - \sin \omega t\cos \omega t = 0$, so $RR^T = I$); the meridian plane of the circle is $\varphi = \omega t$ and the pair $\{\mathbf{e}_r, \mathbf{e}_\theta\}$ is written with $\mathbf{e}_\rho$ in place of $\mathbf{i}$.

### Phase 3: Derivation

#### 3.1 Kinematics
##### Part (a): planar motion
* **Pedagogical Justification:** the particle moves on a circle of constant radius, so $\mathbf{r} = L\,\mathbf{e}_r$ and, with Poisson's formula,
$$ \mathbf{v} = L\dot{\theta}\,\mathbf{e}_\theta, \qquad \mathbf{a} = -L\dot{\theta}^2\,\mathbf{e}_r + L\ddot{\theta}\,\mathbf{e}_\theta $$

##### Part (b): rotating circle
* **Pedagogical Justification:** in the inertial frame the particle has cylindrical coordinates $\rho = L\sin\theta$, $z = -L\cos\theta$ and $\varphi = \omega t$, with $\dot{\varphi} = \omega$ constant, so $\ddot{\varphi} = 0$. No moving-frame theorem is needed: the acceleration comes from the cylindrical formulas (Notes Sec. 2.6.2).
$$ \mathbf{r} = \rho\,\mathbf{e}_\rho + z\,\mathbf{k}, \qquad \mathbf{a} = \left(\ddot{\rho} - \rho\omega^2\right)\mathbf{e}_\rho + 2\dot{\rho}\omega\,\mathbf{e}_\varphi + \ddot{z}\,\mathbf{k} $$
* Differentiating with the chain rule $\frac{d}{dt}f(\theta) = f'(\theta)\dot{\theta}$:
$$ \dot{\rho} = L\cos\theta\,\dot{\theta}, \qquad \ddot{\rho} = L\cos\theta\,\ddot{\theta} - L\sin\theta\,\dot{\theta}^2, \qquad \dot{z} = L\sin\theta\,\dot{\theta}, \qquad \ddot{z} = L\sin\theta\,\ddot{\theta} + L\cos\theta\,\dot{\theta}^2 $$

#### 3.2 Forces
* **Applied force:** the weight $-mg\,\mathbf{k}$, conservative.
* **Constraint force:** the reaction of the smooth track (or the string tension), normal to the circle. In part (a), $\mathbf{N} = -N\,\mathbf{e}_r$ with $N \gt 0$ pushing inward. In part (b) the reaction also has a component perpendicular to the plane of the circle: $\mathbf{N} = N_r\,\mathbf{e}_r + N_\varphi\,\mathbf{e}_\varphi$, with $\mathbf{N}\cdot\mathbf{e}_\theta = 0$.
* **Inertia forces:** none ($\mathcal{F}_0$ is inertial).
* In the basis $\{\mathbf{e}_r, \mathbf{e}_\theta\}$ the weight is $-mg\,\mathbf{k} = mg\cos\theta\,\mathbf{e}_r - mg\sin\theta\,\mathbf{e}_\theta$.

#### 3.3 Equations of Motion
##### Part (a)
* **Pedagogical Justification:** one unknown coordinate $\theta$ and one unknown reaction $N$, and two scalar equations in the plane. The tangential projection has no reaction and is the equation of motion; the normal projection gives $N$.
$$ \mathbf{e}_\theta: \; mL\ddot{\theta} = -mg\sin\theta, \qquad -\mathbf{e}_r: \; N - mg\cos\theta = mL\dot{\theta}^2 = m\frac{v^2}{L} $$
* **Energy.** $\mathbf{N}\cdot\mathbf{v} = 0$ (the reaction is normal to the velocity), so the reaction does no work and the energy is a first integral. Multiplying the tangential equation by $L\dot{\theta}$ gives the same result. With the lowest point as the reference, $V(\theta) = mgL(1 - \cos\theta)$:
$$ E = \tfrac{1}{2}mv^2 + mgL(1 - \cos\theta) = \tfrac{1}{2}mv_0^2 \implies v^2(\theta) = v_0^2 - 2gL(1 - \cos\theta) $$

##### Part (b)
* **Pedagogical Justification:** projecting Newton's second law on the tangent $\mathbf{e}_\theta = \cos\theta\,\mathbf{e}_\rho + \sin\theta\,\mathbf{k}$ of the circle removes the reaction ($\mathbf{N}\cdot\mathbf{e}_\theta = 0$): $m\,\mathbf{a}\cdot\mathbf{e}_\theta = -mg\sin\theta$. Computing $\mathbf{a}\cdot\mathbf{e}_\theta = \left(\ddot{\rho} - \rho\omega^2\right)\cos\theta + \ddot{z}\sin\theta$:
$$ \ddot{\rho}\cos\theta + \ddot{z}\sin\theta = L\ddot{\theta}\left(\cos^2\theta + \sin^2\theta\right) + L\dot{\theta}^2\left(-\sin\theta\cos\theta + \sin\theta\cos\theta\right) = L\ddot{\theta}, \qquad -\rho\omega^2\cos\theta = -L\omega^2\sin\theta\cos\theta $$
$$ mL\ddot{\theta} - mL\omega^2\sin\theta\cos\theta = -mg\sin\theta \implies \boxed{\ddot{\theta} + \left(\frac{g}{L} - \omega^2\cos\theta\right)\sin\theta = 0} $$
* **Reaction components.** Perpendicular to the plane ($\mathbf{e}_\varphi$): $N_\varphi = m\cdot 2\dot{\rho}\omega = 2mL\omega\dot{\theta}\cos\theta$. In the plane, projecting on $\mathbf{e}_r = \sin\theta\,\mathbf{e}_\rho - \cos\theta\,\mathbf{k}$, with $\mathbf{a}\cdot\mathbf{e}_r = -L\left(\dot{\theta}^2 + \omega^2\sin^2\theta\right)$:
$$ N_r + mg\cos\theta = -mL\left(\dot{\theta}^2 + \omega^2\sin^2\theta\right) \implies -N_r = mL\left(\dot{\theta}^2 + \omega^2\sin^2\theta\right) + mg\cos\theta $$
For $\omega = 0$ this is the inward reaction of part (a).

#### 3.4 Integration and Answers
##### Part (a): normal reaction and detachment
* **Pedagogical Justification:** the reaction follows from the normal equation with the energy relation, and the particle leaves the circle when $N$ vanishes:
$$ N(\theta) = mg\cos\theta + \frac{m}{L}\left[v_0^2 - 2gL(1 - \cos\theta)\right] = \frac{mv_0^2}{L} - mg(2 - 3\cos\theta) $$
$$ N(\theta_d) = 0 \implies \boxed{\cos\theta_d = \frac{2gL - v_0^2}{3gL}} $$
* **Regime 1, $v_0 \le \sqrt{2gL}$.** The speed vanishes when $v_0^2 = 2gL(1 - \cos\theta_{\max})$, i.e. $\cos\theta_{\max} = 1 - \dfrac{v_0^2}{2gL} \ge 0$, so $\theta_{\max} \le \pi/2$. There $N(\theta_{\max}) = mg\cos\theta_{\max} \ge 0$: the particle stops and returns before $N$ can vanish. **The detachment point is never reached**; the particle oscillates in the lower semicircle (at $v_0^2 = 2gL$ it reaches the horizontal at rest with $N = 0$ and turns back).
* **Regime 2, $\sqrt{2gL} \lt v_0 \lt \sqrt{5gL}$.** Since $v_0^2 \gt 2gL$ the particle crosses $\theta = \pi/2$ with positive speed, and $2gL \lt v_0^2 \lt 5gL$ gives $-1 \lt \cos\theta_d \lt 0$, i.e. $\theta_d \in (\pi/2, \pi)$. The speed there is $v^2(\theta_d) = v_0^2 - 2gL\left(1 - \cos\theta_d\right) = \dfrac{v_0^2 - 2gL}{3} \gt 0$. **The detachment point is reached**: the particle leaves the circle at $\theta_d = \arccos\dfrac{2gL - v_0^2}{3gL}$ and continues in free (parabolic) flight under gravity.
* **Regime 3, $v_0 \ge \sqrt{5gL}$.** At the top, $N(\pi) = \dfrac{mv_0^2}{L} - 5mg \ge 0$, and $N(\theta)$ decreases monotonically from $0$ to $\pi$, so the reaction stays non-negative along the whole loop. **The particle never leaves** the circle and makes complete turns.

##### Part (b): equilibrium positions
* **Pedagogical Justification:** an equilibrium relative to the turning circle is a static solution of the equation of motion, $\ddot{\theta} = \dot{\theta} = 0$ (in the inertial frame the particle then describes a horizontal circle):
$$ \left(\frac{g}{L} - \omega^2\cos\theta\right)\sin\theta = 0 $$
* **Vertical alignments** ($\sin\theta = 0$): $\theta_1 = 0$ (bottom) and $\theta_2 = \pi$ (top). The constraint of the statement is unilateral (the particle moves on the inside of the circumference). At rest, $-N_r = mL\left(\dot{\theta}^2 + \omega^2\sin^2\theta\right) + mg\cos\theta$ gives $-N_r = mg \gt 0$ at the bottom (admissible) but $-N_r = -mg \lt 0$ at the top, an outward push that the inside of the hoop cannot exert. So $\theta_2 = \pi$ is an equilibrium only for a bilateral constraint (a bead on a wire) and is **excluded** here.
* **Off-axis equilibria** ($\cos\theta = g/(\omega^2L)$): they exist if and only if $\left|g/(\omega^2L)\right| \le 1$, i.e. $\omega^2 \ge g/L$, and they are admissible because $-N_r = mL\omega^2\sin^2\theta_0 + mg\cos\theta_0 \gt 0$ ($\cos\theta_0 \gt 0$). For $\omega \gt \sqrt{g/L}$ there are two symmetric positions $\theta_{3,4} = \pm\arccos\dfrac{g}{\omega^2L}$.
* **Stability** (linearisation of $\ddot{\theta} = F(\theta)$ with $F = -\left(g/L - \omega^2\cos\theta\right)\sin\theta$): $F'(0) = -(g/L - \omega^2)$, so the bottom is stable for $\omega^2 \lt g/L$ and unstable for $\omega^2 \gt g/L$; near $\theta = \pi$, $\ddot{\theta} \approx (g/L + \omega^2)(\theta - \pi)$, always unstable; at $\theta_{3,4}$, $F'(\theta_0) = -\omega^2\sin^2\theta_0 \lt 0$, stable.

### Phase 4: Interpretation & Checks
* **Supercritical pitchfork:** for $\omega \lt \omega_c = \sqrt{g/L}$ the bottom is the only stable equilibrium. At $\omega_c$ it becomes unstable and two stable off-axis equilibria appear, at the angle where the horizontal circle of radius $L\sin\theta$ has the centripetal acceleration required by the balance with gravity. As $\omega \to \infty$, $\cos\theta_0 \to 0$ and $\theta_0 \to \pi/2$.
* **Limits of the regimes:** at $v_0^2 = 2gL$, $\cos\theta_d = 0$ ($\theta_d = \pi/2$), the boundary between oscillation and detachment; at $v_0^2 = 5gL$, $\cos\theta_d = -1$ ($\theta_d = \pi$) and $N(\pi) = 0$, the boundary between detachment and full loops. For $\omega \to 0$ the equation of (b) reduces to the simple pendulum $\ddot{\theta} + (g/L)\sin\theta = 0$.
* **Dimensional check:** $[N] = [mv_0^2/L] = \text{N}$; $\cos\theta_d$ is dimensionless; $\omega_c = \sqrt{g/L}$ is in s$^{-1}$.
* **Check against the official key:** `Problems.pdf` has no entry for Problem 23 in its solution keys, so the results are verified by independent derivation. Numerical integration ($g = L = 1$, detachment found where $N = 0$) gives $\theta_d = 120.000^\circ$ for $v_0^2 = 3.5$ (with $v^2 = 0.5 = (v_0^2 - 2gL)/3$), $99.594^\circ$ for $v_0^2 = 2.5$ and $165.165^\circ$ for $v_0^2 = 4.9$, all equal to $\arccos\left[(2 - v_0^2)/3\right]$. Sympy confirms the equation of motion of part (b) and $N_\varphi = 2mL\omega\dot{\theta}\cos\theta$ from the inertial acceleration of the point on the turning circle.

---

## 📌 Problem 24: Particle on a Circumference with a Spring

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a heavy particle $P$ of mass $m$ slides on a vertical circular wire of radius $a$ centred at $O$. A linear spring of stiffness $k$ and zero natural length joins $P$ to the anchor $A = (0, \beta a)$ on the $y$-axis. Gravity acts along $-\mathbf{j}$.
* **Constraints:** $P$ stays on the circle $x^2 + y^2 = a^2$ in the plane $Oxy$ (holonomic, scleronomic, smooth, bilateral). The wire gives a reaction normal to it, with an in-plane component and, if needed, a component perpendicular to the plane (zero here). $\text{CDOF} = 2 - 1 = 1$, with the angle $\theta$ measured counterclockwise from the positive $x$-axis.
* **Initial state:** $P$ starts at $(a, 0)$, i.e. $\theta(0) = 0$, with $\mathbf{v}_0 = v_0\,\mathbf{j}$, i.e. $\dot{\theta}(0) = v_0/a$.
* **Parameters:** $m$, $a$, $k$, $g$, $\beta$, $v_0 \gt 0$. Parts (e) and (f) use $\beta = mg/(ka)$ (the case of part (d)), and the additional force has the constant $2m\mu$.

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $\mathcal{F}_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$ with $\mathbf{j}$ vertical upward.
* **Polar basis:** $\mathbf{e}_r = \cos\theta\,\mathbf{i} + \sin\theta\,\mathbf{j}$ and $\mathbf{e}_\theta = -\sin\theta\,\mathbf{i} + \cos\theta\,\mathbf{j}$, a rotation of $\mathcal{B}_0$ by $\theta$ about $\mathbf{k}$ (matrix $\begin{pmatrix}\cos \theta & -\sin \theta & 0\\ \sin \theta & \cos \theta & 0\\ 0 & 0 & 1\end{pmatrix}$, $\det = \cos^2\theta + \sin^2\theta = 1$; $RR^T$ has diagonal entries $\cos^2\theta + \sin^2\theta = 1$ (and $1$) and off-diagonal entries $\cos \theta\sin \theta - \sin \theta\cos \theta = 0$, so $RR^T = I$), with $\dot{\mathbf{e}}_r = \dot{\theta}\,\mathbf{e}_\theta$ and $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_r$ (Poisson).

### Phase 3: Derivation

#### 3.1 Kinematics
* **Pedagogical Justification:** the position of $P$ and the anchor give the spring vector, and the polar formulas give the velocity and acceleration:
$$ \mathbf{r}_P = a\,\mathbf{e}_r = a\cos\theta\,\mathbf{i} + a\sin\theta\,\mathbf{j}, \qquad \mathbf{v} = a\dot{\theta}\,\mathbf{e}_\theta, \qquad \mathbf{a} = -a\dot{\theta}^2\,\mathbf{e}_r + a\ddot{\theta}\,\mathbf{e}_\theta $$
$$ \overrightarrow{AP} = \mathbf{r}_P - \beta a\,\mathbf{j} = a\cos\theta\,\mathbf{i} + a(\sin\theta - \beta)\,\mathbf{j}, \qquad \left|\overrightarrow{AP}\right|^2 = a^2\left(1 + \beta^2 - 2\beta\sin\theta\right) $$

#### 3.2 Forces
* **Gravity:** $-mg\,\mathbf{j}$, with $\mathbf{F}_g\cdot\mathbf{e}_r = -mg\sin\theta$ and $\mathbf{F}_g\cdot\mathbf{e}_\theta = -mg\cos\theta$.
* **Spring:** $\mathbf{F}_s = -k\,\overrightarrow{AP}$, with $\mathbf{F}_s\cdot\mathbf{e}_r = -ka\left(1 - \beta\sin\theta\right)$ and $\mathbf{F}_s\cdot\mathbf{e}_\theta = ka\beta\cos\theta$.
* **Reaction:** $\mathbf{N} = N\,\mathbf{e}_r$ (normal to the wire; $N \gt 0$ is outward). **Additional force** (parts e, f): $\mathbf{F}_d = 2m\mu\,\mathbf{v}$, along the velocity, as the statement says. **Inertia forces:** none.
* **Potential.** Gravity and the linear spring are conservative, so the total potential energy is the sum of $V_g = mgy = mga\sin\theta$ and $V_s = \tfrac{1}{2}k\left|\overrightarrow{AP}\right|^2$ (the work of the wire reaction is zero):
$$ V(\theta) = mga\sin\theta + \tfrac{1}{2}ka^2\left(1 + \beta^2 - 2\beta\sin\theta\right) = \tfrac{1}{2}ka^2\left(1 + \beta^2\right) + \left(mg - k\beta a\right)a\sin\theta $$

#### 3.3 Equations of Motion
* **Tangential equation** (no reaction): $ma\ddot{\theta} = \mathbf{F}_g\cdot\mathbf{e}_\theta + \mathbf{F}_s\cdot\mathbf{e}_\theta + \mathbf{F}_d\cdot\mathbf{e}_\theta = -\left(mg - k\beta a\right)\cos\theta + 2m\mu a\dot{\theta}$. For $\mu = 0$ this is $ma\ddot{\theta} = -\frac{1}{a}\frac{dV}{d\theta}$, i.e. the equation of motion of the conservative problem.
* **Radial equation** (gives the reaction): $-ma\dot{\theta}^2 = N - mg\sin\theta - ka\left(1 - \beta\sin\theta\right)$.
* Two equations for the two unknowns $\theta(t)$ and $N(t)$. The reaction is decoupled and is computed after $\theta(t)$.
* **Energy (conservative case $\mu = 0$):** the reaction does no work, so $E = \tfrac{1}{2}ma^2\dot{\theta}^2 + V(\theta)$ is a first integral.

#### 3.4 Integration and Answers
##### (a) Potential of the forces
$$ \boxed{V(\theta) = \tfrac{1}{2}ka^2\left(1 + \beta^2\right) + \left(mg - k\beta a\right)a\sin\theta} $$

##### (b) Equilibrium positions
* **Pedagogical Justification:** equilibrium requires $\dfrac{dV}{d\theta} = 0$:
$$ \frac{dV}{d\theta} = \left(mg - k\beta a\right)a\cos\theta = 0 $$
* If $mg - k\beta a \ne 0$: $\cos\theta = 0$, i.e. $\theta_1 = \pi/2$ (top) and $\theta_2 = -\pi/2$ (bottom). Since $V'' = -(mg - k\beta a)a\sin\theta$, the top is a minimum (stable) if $mg \lt k\beta a$ and the bottom is a minimum if $mg \gt k\beta a$.
* If $\beta = \dfrac{mg}{ka}$: $dV/d\theta \equiv 0$, so **every** position is an equilibrium (neutral equilibrium).

##### (c) Reduction to quadratures
* **Pedagogical Justification:** the energy is constant for $\mu = 0$. At $t = 0$, $V(0) = \tfrac{1}{2}ka^2(1 + \beta^2)$ and $\dot{\theta}(0) = v_0/a$, so
$$ \tfrac{1}{2}ma^2\dot{\theta}^2 + V(\theta) = \tfrac{1}{2}mv_0^2 + V(0) \implies \dot{\theta} = \pm\sqrt{\frac{v_0^2}{a^2} - \frac{2\left(mg - k\beta a\right)}{ma}\sin\theta} $$
$$ \int_0^{\theta(t)}\frac{d\theta'}{\sqrt{\dfrac{v_0^2}{a^2} - \dfrac{2\left(mg - k\beta a\right)}{ma}\sin\theta'}} = \pm\int_0^tdt' = \pm t $$

##### (d) Case $\beta = mg/(ka)$
* **Pedagogical Justification:** the coefficient $mg - k\beta a$ vanishes, so $V$ is constant and the tangential force is zero: $ma\ddot{\theta} = 0$. Integrating with Barrow's rule:
$$ \dot{\theta}(t) = \dot{\theta}(0) = \frac{v_0}{a}, \qquad \theta(t) = \int_0^t\frac{v_0}{a}\,dt' = \left[\frac{v_0t'}{a}\right]_0^t = \boxed{\frac{v_0}{a}\,t} $$
The particle circles the wire at constant angular speed.

##### (e) Position with the additional force along the velocity
* **Pedagogical Justification:** with $\beta = mg/(ka)$ the gravity and spring contributions to the tangential equation cancel, so only the additional force remains: $ma\ddot{\theta} = 2m\mu\,(a\dot{\theta})$, i.e.
$$ \ddot{\theta} - 2\mu\dot{\theta} = 0 $$
* Let $\Omega(t) = \dot{\theta}$; then $\dfrac{d\Omega}{\Omega} = 2\mu\,dt$, and integrating from $\Omega(0) = v_0/a$ (Barrow):
$$ \int_{v_0/a}^{\Omega}\frac{d\Omega'}{\Omega'} = \int_0^t2\mu\,dt' \implies \left[\ln\Omega'\right]_{v_0/a}^{\Omega} = \ln\frac{a\Omega}{v_0} = 2\mu t \implies \frac{a\Omega}{v_0} = e^{2\mu t} \implies \Omega(t) = \frac{v_0}{a}e^{2\mu t} $$
* With $w = 2\mu t'$, $dw = 2\mu\,dt'$, the antiderivative is $\int e^{2\mu t'}dt' = \frac{1}{2\mu}\int e^w\,dw = \frac{e^{2\mu t'}}{2\mu}$, and with $\theta(0) = 0$:
$$ \theta(t) = \frac{v_0}{a}\int_0^te^{2\mu t'}dt' = \frac{v_0}{a}\left[\frac{e^{2\mu t'}}{2\mu}\right]_0^t = \frac{v_0}{a}\cdot\frac{e^{2\mu t} - 1}{2\mu} = \boxed{\frac{v_0}{2\mu a}\left(e^{2\mu t} - 1\right)} $$
The force acts along the velocity, so it feeds energy to the particle and the angular speed grows exponentially.

> [!note] Reading of the statement
> The statement says that the additional force is proportional to, and in the **same direction as**, the instantaneous velocity (checked on the PDF page), so it is $+2m\mu\,\mathbf{v}$ and the solution above follows it literally. If the force were meant to oppose the velocity (viscous damping), the sign changes: $\ddot{\theta} + 2\mu\dot{\theta} = 0$, $\theta(t) = \dfrac{v_0}{2\mu a}\left(1 - e^{-2\mu t}\right)$, which tends to $\theta_\infty = v_0/(2\mu a)$ at rest, and the reaction below becomes $N = ka - \dfrac{mv_0^2}{a}e^{-4\mu t}$.

##### (f) Reaction of the circumference
* **Pedagogical Justification:** the radial equation of 3.3, with $\mathbf{F}_g\cdot\mathbf{e}_r$ and $\mathbf{F}_s\cdot\mathbf{e}_r$ of 3.2 (the additional force is tangential, so it has no radial component):
$$ N(t) = -ma\dot{\theta}^2 + mg\sin\theta + ka\left(1 - \beta\sin\theta\right) $$
* With $\beta = mg/(ka)$ the terms in $\sin\theta$ cancel ($mg\sin\theta - ka\beta\sin\theta = 0$), and $\dot{\theta} = (v_0/a)e^{2\mu t}$:
$$ \boxed{N(t) = ka - \frac{mv_0^2}{a}\,e^{4\mu t}} $$
$N$ is the outward component. It starts at $ka - mv_0^2/a$ and becomes more and more negative: the wire must push the particle inward with a force that grows as $e^{4\mu t}$.

### Phase 4: Interpretation & Checks
* **Dimensional check:** $[ka] = \text{N}$ and $[mv_0^2/a] = \text{N}$; $\mu$ has units s$^{-1}$, so $2\mu t$ is dimensionless and $[v_0/(2\mu a)] = 1$ (rad).
* **Limits:** for $\mu \to 0$, $\theta \to (v_0/a)t$, the result of (d), and $N \to ka - mv_0^2/a$, the preload of the spring minus the centripetal force, constant.
* **Check against the official key:** `Problems.pdf` has no entry for Problem 24 in its solution keys, so the results are verified by independent derivation. Sympy confirms the radial equation $N = -ma\dot{\theta}^2 + mg\sin\theta + ka(1 - \beta\sin\theta)$ for either sign of the additional force and the reduction to $N = ka - (mv_0^2/a)e^{\pm 4\mu t}$ when $\beta = mg/(ka)$. Numerical integration of $\ddot{\theta} = 2\mu\dot{\theta}$ ($a = 1$, $v_0 = 1.7$, $\mu = 0.3$) gives $\theta(2) = 6.57366$, equal to the closed form; the damping reading gives $1.97995$, also equal to its closed form.

---

## 📌 Problem 29: Heavy Particle on a Tilted Cylinder

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a heavy particle of mass $m$ moves without friction on the surface of an infinitely long circular cylinder of radius $R$ whose axis $Oz$ forms the angle $\alpha$ with the vertical $Oz_1$.
* **Constraint:** the particle stays on the surface, $x^2 + y^2 = R^2$ in the frame of the cylinder (holonomic, scleronomic, smooth). The statement says the particle is constrained to move along the surface, so we treat it as bilateral; the sign of the reaction tells on which side the surface presses it (checked in (c)).
* **Degrees of freedom:** $\text{CDOF} = 3 - 1 = 2$, with the coordinates of the statement: the axial coordinate $z(t)$ and the angle $\theta(t)$ around the axis.
* **Initial state:** $z(0) = 0$, $\theta(0) = \pi/2$, $\dot{z}(0) = v_0$, $\dot{\theta}(0) = \omega_0$.
* **Parameters:** $m$, $R$, $\alpha$, $g$, $v_0$, $\omega_0$.

### Phase 2: Reference Frames & Vector Bases
* **Vertical frame:** $S_1 = \{O; \mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$ with $\mathbf{k}_1$ vertical upward.
* **Cylinder frame:** $S_2 = \{O; \hat{\mathbf{x}}, \hat{\mathbf{y}}, \hat{\mathbf{z}}\}$ with $\hat{\mathbf{z}}$ along the axis. From the figure, $\hat{\mathbf{z}} = \sin\alpha\,\mathbf{i}_1 + \cos\alpha\,\mathbf{k}_1$, $\hat{\mathbf{x}} = \cos\alpha\,\mathbf{i}_1 - \sin\alpha\,\mathbf{k}_1$ and $\hat{\mathbf{y}} = \mathbf{j}_1$, a rotation of $S_1$ by $\alpha$ about $\mathbf{j}_1$:
$$ [{}_1 R_2] = \begin{pmatrix} \cos\alpha & 0 & \sin\alpha \\ 0 & 1 & 0 \\ -\sin\alpha & 0 & \cos\alpha \end{pmatrix}, \qquad \det[{}_1 R_2] = \cos^2\alpha + \sin^2\alpha = 1, \qquad [{}_1 R_2][{}_1 R_2]^T = I $$
* **Cylindrical basis:** $\mathbf{e}_r = \cos\theta\,\hat{\mathbf{x}} + \sin\theta\,\hat{\mathbf{y}}$, $\mathbf{e}_\theta = -\sin\theta\,\hat{\mathbf{x}} + \cos\theta\,\hat{\mathbf{y}}$, $\hat{\mathbf{z}}$, a rotation of $S_2$ by $\theta$ about $\hat{\mathbf{z}}$ (matrix $\begin{pmatrix}\cos \theta & -\sin \theta & 0\\ \sin \theta & \cos \theta & 0\\ 0 & 0 & 1\end{pmatrix}$, $\det = \cos^2\theta + \sin^2\theta = 1$; $RR^T$ has diagonal entries $\cos^2\theta + \sin^2\theta = 1$ (and $1$) and off-diagonal entries $\cos \theta\sin \theta - \sin \theta\cos \theta = 0$, so $RR^T = I$), with $\dot{\mathbf{e}}_r = \dot{\theta}\,\mathbf{e}_\theta$ and $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_r$.
* **Gravity in this basis.** From $\mathbf{k}_1 = \cos\alpha\,\hat{\mathbf{z}} - \sin\alpha\,\hat{\mathbf{x}}$:
$$ -g\,\mathbf{k}_1 = g\sin\alpha\,\hat{\mathbf{x}} - g\cos\alpha\,\hat{\mathbf{z}} = g\sin\alpha\cos\theta\,\mathbf{e}_r - g\sin\alpha\sin\theta\,\mathbf{e}_\theta - g\cos\alpha\,\hat{\mathbf{z}} $$
so $\theta = 0$ is the lowest generator of the cylinder ($\mathbf{e}_r$ points downward there).

### Phase 3: Derivation

#### 3.1 Kinematics
* **Pedagogical Justification:** on the cylinder $r = R$ is constant, so the position uses the two free coordinates, and Poisson's formula gives the derivatives of $\mathbf{e}_r$:
$$ \mathbf{r} = R\,\mathbf{e}_r + z\,\hat{\mathbf{z}}, \qquad \mathbf{v} = R\dot{\theta}\,\mathbf{e}_\theta + \dot{z}\,\hat{\mathbf{z}}, \qquad \mathbf{a} = -R\dot{\theta}^2\,\mathbf{e}_r + R\ddot{\theta}\,\mathbf{e}_\theta + \ddot{z}\,\hat{\mathbf{z}} $$

#### 3.2 Forces
* **Applied force:** the weight $m\mathbf{g}$, decomposed in 2.
* **Constraint force:** the reaction of the smooth cylinder is normal to the surface, so it is radial: $\mathbf{N} = -N\,\mathbf{e}_r$ (with $N \gt 0$ when it pushes toward the axis). It has no component along $\hat{\mathbf{z}}$ or $\mathbf{e}_\theta$.
* **Inertia forces:** none ($S_1$ is inertial).

#### 3.3 Equations of Motion
* **Pedagogical Justification:** Newton's second law in $S_1$ projected on the three directions of the cylindrical basis gives three scalar equations for the three unknowns $z$, $\theta$ and $N$. The axial and azimuthal projections contain no reaction and are the equations of motion; the radial one gives $N$:
$$ \hat{\mathbf{z}}: \; m\ddot{z} = -mg\cos\alpha, \qquad \mathbf{e}_\theta: \; mR\ddot{\theta} = -mg\sin\alpha\sin\theta, \qquad \mathbf{e}_r: \; -mR\dot{\theta}^2 = -N + mg\sin\alpha\cos\theta $$
* **Decoupling.** The axial equation involves only $z$ and the azimuthal one only $\theta$ (a pendulum equation); the reaction is computed afterwards from the radial equation.
* **First integral.** Multiplying the azimuthal equation by $\dot{\theta}$ (chain rule, $\frac{d}{dt}\left(\tfrac{1}{2}\dot{\theta}^2\right) = \dot{\theta}\ddot{\theta}$ and $\frac{d}{dt}\cos\theta = -\sin\theta\,\dot{\theta}$):
$$ \frac{d}{dt}\left[\tfrac{1}{2}\dot{\theta}^2 - \frac{g\sin\alpha}{R}\cos\theta\right] = \dot{\theta}\left(\ddot{\theta} + \frac{g\sin\alpha}{R}\sin\theta\right) = 0 $$

#### 3.4 Integration and Answers
##### (a) Axial motion $z(t)$
* **Pedagogical Justification:** the axial equation is $\ddot{z} = -g\cos\alpha$. Integrating twice with Barrow's rule from the initial conditions:
$$ \dot{z}(t) = v_0 + \int_0^t\left(-g\cos\alpha\right)dt' = v_0 - g\cos\alpha\,t, \qquad \boxed{z(t) = \int_0^t\left(v_0 - g\cos\alpha\,t'\right)dt' = \left[v_0t' - \tfrac{1}{2}g\cos\alpha\,t'^2\right]_0^t = v_0t - \tfrac{1}{2}g\cos\alpha\,t^2} $$

##### (b) Reduction of $\theta(t)$ to quadratures
* From the first integral, with $\theta = \pi/2$ ($\cos\theta = 0$) and $\dot{\theta} = \omega_0$ at $t = 0$, the constant is $\tfrac{1}{2}\omega_0^2$:
$$ \dot{\theta}^2 = \omega_0^2 + \frac{2g\sin\alpha}{R}\cos\theta $$
* Separating variables (Barrow's rule from $\theta(0) = \pi/2$):
$$ \boxed{\int_{\pi/2}^{\theta(t)}\frac{d\theta'}{\sqrt{\omega_0^2 + \dfrac{2g\sin\alpha}{R}\cos\theta'}} = \pm\,t} $$
with the sign of $\dot{\theta}$.

##### (c) Reaction of the cylinder
* **Pedagogical Justification:** the radial equation gives $N = mR\dot{\theta}^2 + mg\sin\alpha\cos\theta$; substituting $\dot{\theta}^2$ from (b):
$$ N(\theta) = mR\left(\omega_0^2 + \frac{2g\sin\alpha}{R}\cos\theta\right) + mg\sin\alpha\cos\theta = \boxed{mR\omega_0^2 + 3mg\sin\alpha\cos\theta} $$
$N$ is the component toward the axis. If it becomes negative, the surface would have to pull the particle: possible for a bilateral constraint, but a particle resting on the inside of the cylinder would leave the surface.

##### (d) Case $\omega_0^2 = g\sin\alpha/R$
* **Pedagogical Justification:** the turning points of the angular motion are where $\dot{\theta} = 0$:
$$ \dot{\theta}^2 = \frac{g\sin\alpha}{R}\left(1 + 2\cos\theta\right) = 0 \implies \cos\theta = -\frac{1}{2} \implies \theta = \pm\frac{2\pi}{3} $$
* **Motion:** since $\theta = 0$ is the stable bottom generator, the particle oscillates in $\theta$ between $-2\pi/3$ and $+2\pi/3$ about the bottom (for $\omega_0 \gt 0$ it first moves to $+2\pi/3$, then swings through $\theta = 0$ to $-2\pi/3$ and back), while it moves along the axis with the uniform deceleration $-g\cos\alpha$: $z(t) = v_0t - \tfrac{1}{2}g\cos\alpha\,t^2$. The trajectory is a wavy curve on the cylinder.
* **Reaction:** $N = mg\sin\alpha\left(1 + 3\cos\theta\right)$, which is negative for $\cos\theta \lt -1/3$ ($\theta \gt 109.5^\circ$), so the motion up to $\pm 2\pi/3$ (where $N = -\tfrac{1}{2}mg\sin\alpha$) needs a bilateral constraint.

##### (e) Case $\omega_0^2 = 4g\sin\alpha/R$
* **Pedagogical Justification:** now $\dot{\theta}^2 = \dfrac{g\sin\alpha}{R}\left(4 + 2\cos\theta\right) \ge \dfrac{2g\sin\alpha}{R} \gt 0$ for every $\theta$ (the minimum is at $\theta = \pi$, the top).
* **Motion:** the angular velocity never vanishes and keeps its sign, so the particle makes complete turns around the cylinder, in a helical-like trajectory whose pitch follows the axial velocity $\dot{z} = v_0 - g\cos\alpha\,t$, which decreases, vanishes at $t = v_0/(g\cos\alpha)$ and then reverses sign, so the pitch shrinks to zero and then changes sense. The reaction $N = mg\sin\alpha\left(4 + 3\cos\theta\right) \ge mg\sin\alpha \gt 0$ is always positive, so this motion is also admissible if the particle is inside a hollow cylinder.

### Phase 4: Interpretation & Checks
* **Decoupling:** the axial motion is a uniformly decelerated one-dimensional motion and the azimuthal motion is that of a nonlinear pendulum of length $R$ in the effective gravity $g\sin\alpha$ (the component of gravity in the cross-section).
* **Dimensional check:** $[g\sin\alpha/R] = \text{s}^{-2} = [\omega_0^2]$ and $[N] = [mR\omega_0^2] = \text{N}$.
* **Limits:** for $\alpha \to 0$ (vertical axis) there is no azimuthal force and $\dot{\theta} = \omega_0$; for $\alpha \to \pi/2$ (horizontal axis) $\ddot{z} \to 0$.
* **Check against the official key:** `Problems.pdf` has no entry for Problem 29 in its solution keys, so the results are verified by independent derivation. Sympy reproduces the components of the acceleration in the cylindrical basis and those of gravity ($\mathbf{g}\cdot\hat{\mathbf{z}} = -g\cos\alpha$, $\mathbf{g}\cdot\mathbf{e}_r = g\sin\alpha\cos\theta$, $\mathbf{g}\cdot\mathbf{e}_\theta = -g\sin\alpha\sin\theta$). Numerical integration of $\ddot{\theta} = -(g\sin\alpha/R)\sin\theta$ from $\theta(0) = \pi/2$ gives the turning points $\pm 0.66667\pi = \pm 2\pi/3$ for (d), no turning point for (e), and a minimum of $N$ of $-0.5\,mg\sin\alpha$ for (d) and $+1.0\,mg\sin\alpha$ for (e).

---

## 📌 Problem 31: Two Particles on Cone with String

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** two heavy particles $P_1$ and $P_2$ of mass $m$ are joined by an inextensible massless string of length $\ell$ that passes without friction through the aperture at the vertex $O$ of a cone of semi-angle $\alpha$. $P_1$ moves without friction on the cone surface; $P_2$ hangs along the cone axis ($Oz$ vertical upward, the cone opens downward). The string stays taut and the particles do not reach $O$.
* **Constraints:** with $6$ coordinates for two free particles:
  - $P_1$ on the cone: $1$ constraint (bilateral: the statement says the particle cannot leave the surface).
  - Constant string length: $\xi + (\text{depth of } P_2) = \ell$, i.e. $1$ constraint (unilateral: $T \ge 0$).
  - $P_2$ on the axis: $x_2 = y_2 = 0$, $2$ constraints.
* **Degrees of freedom:** $\text{CDOF} = 6 - 4 = 2$, with $\xi$ (the length of the string between $O$ and $P_1$) and $\theta$ (the azimuthal angle of $P_1$).
* **Parameters:** $m$, $\ell$, $\alpha$, $g$.

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $S_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$ with $\mathbf{k}$ vertical upward.
* **Cylindrical basis:** $\mathbf{e}_R = \cos\theta\,\mathbf{i} + \sin\theta\,\mathbf{j}$, $\mathbf{e}_\theta = -\sin\theta\,\mathbf{i} + \cos\theta\,\mathbf{j}$, $\mathbf{k}$ (rotation about $\mathbf{k}$ by $\theta$, matrix $\begin{pmatrix}\cos \theta & -\sin \theta & 0\\ \sin \theta & \cos \theta & 0\\ 0 & 0 & 1\end{pmatrix}$, $\det = \cos^2\theta + \sin^2\theta = 1$; $RR^T$ has diagonal entries $\cos^2\theta + \sin^2\theta = 1$ (and $1$) and off-diagonal entries $\cos \theta\sin \theta - \sin \theta\cos \theta = 0$, so $RR^T = I$; $\dot{\mathbf{e}}_R = \dot{\theta}\,\mathbf{e}_\theta$, $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_R$).
* **Cone basis:** the unit vector along the generator from $O$ to $P_1$, $\mathbf{e}_\xi = \sin\alpha\,\mathbf{e}_R - \cos\alpha\,\mathbf{k}$; the unit outward normal to the cone, $\mathbf{n} = \cos\alpha\,\mathbf{e}_R + \sin\alpha\,\mathbf{k}$; and $\mathbf{e}_\theta$. The triple $\{\mathbf{e}_\xi, \mathbf{e}_\theta, \mathbf{n}\}$ is right-handed ($\mathbf{e}_\xi\times\mathbf{e}_\theta = \mathbf{n}$). In the cylindrical basis $\{\mathbf{e}_R, \mathbf{e}_\theta, \mathbf{k}\}$
$$ [{}_1R_2] = \begin{pmatrix} \sin\alpha & 0 & \cos\alpha \\ 0 & 1 & 0 \\ -\cos\alpha & 0 & \sin\alpha \end{pmatrix}, \qquad \det[{}_1R_2] = \sin\alpha\cdot\sin\alpha + \cos\alpha\cdot\cos\alpha = \sin^2\alpha + \cos^2\alpha = 1 $$
and its columns have unit norm ($\sin^2\alpha + \cos^2\alpha = 1$) and are orthogonal ($\sin\alpha\cos\alpha - \cos\alpha\sin\alpha = 0$), so $[{}_1R_2][{}_1R_2]^T = I$.

### Phase 3: Derivation

#### 3.1 Kinematics
##### (a) Position, velocity and acceleration
* **Pedagogical Justification:** $P_1$ is at the distance $\xi$ from $O$ along the generator, so $\mathbf{r}_1 = \xi\,\mathbf{e}_\xi = \xi\sin\alpha\,\mathbf{e}_R - \xi\cos\alpha\,\mathbf{k}$. Since $\mathbf{e}_R$ rotates with $\theta$, the derivatives use the product rule and Poisson's formula. $P_2$ is on the axis at the depth $\ell - \xi$ below $O$ (the string has length $\xi$ on the cone side and $\ell - \xi$ on the hanging side).
$$ \mathbf{v}_1 = \dot{\xi}\,\mathbf{e}_\xi + \xi\sin\alpha\,\dot{\theta}\,\mathbf{e}_\theta $$
$$ \mathbf{a}_1 = \left(\ddot{\xi} - \xi\dot{\theta}^2\sin^2\alpha\right)\mathbf{e}_\xi + \sin\alpha\left(\xi\ddot{\theta} + 2\dot{\xi}\dot{\theta}\right)\mathbf{e}_\theta - \xi\dot{\theta}^2\sin\alpha\cos\alpha\,\mathbf{n} $$
$$ \mathbf{r}_2 = -(\ell - \xi)\,\mathbf{k}, \qquad \mathbf{v}_2 = \dot{\xi}\,\mathbf{k}, \qquad \mathbf{a}_2 = \ddot{\xi}\,\mathbf{k} $$

#### 3.2 Forces
##### (b) Forces on $P_1$ and $P_2$
* **On $P_1$:** the weight $-mg\,\mathbf{k} = mg\cos\alpha\,\mathbf{e}_\xi - mg\sin\alpha\,\mathbf{n}$; the tension of the string, directed toward $O$, $\mathbf{T}_1 = -T\,\mathbf{e}_\xi$ ($T \gt 0$); and the reaction of the cone $\mathbf{N} = N\,\mathbf{n}$ (outward).
* **On $P_2$:** the weight $-mg\,\mathbf{k}$; the tension $+T\,\mathbf{k}$ (same string, massless, smooth aperture); and the reaction $\mathbf{R}_2$ of the guide, perpendicular to $\mathbf{k}$ (horizontal).
* **Inertia forces:** none ($S_0$ is inertial).

#### 3.3 Equations of Motion
##### (c) Differential equations
* **Pedagogical Justification:** Newton's second law for each particle, six scalar equations for the six unknowns $\xi$, $\theta$, $T$, $N$ and the two horizontal components of $\mathbf{R}_2$:
$$ P_2,\ \mathbf{k}: \; m\ddot{\xi} = T - mg \implies T = m\left(g + \ddot{\xi}\right), \qquad P_2,\ \text{horizontal}: \; \mathbf{R}_2 = \mathbf{0} \ (\text{since } \mathbf{a}_2 \parallel \mathbf{k}) $$
$$ P_1,\ \mathbf{e}_\xi: \; m\left(\ddot{\xi} - \xi\dot{\theta}^2\sin^2\alpha\right) = mg\cos\alpha - T $$
$$ P_1,\ \mathbf{e}_\theta: \; m\sin\alpha\left(\xi\ddot{\theta} + 2\dot{\xi}\dot{\theta}\right) = 0, \qquad P_1,\ \mathbf{n}: \; -m\xi\dot{\theta}^2\sin\alpha\cos\alpha = N - mg\sin\alpha $$
* **Decoupling.** Substituting $T = m(g + \ddot{\xi})$ in the $\mathbf{e}_\xi$ equation eliminates the tension and leaves the equations of the two free coordinates:
$$ \boxed{2\ddot{\xi} - \xi\dot{\theta}^2\sin^2\alpha + g\left(1 - \cos\alpha\right) = 0}, \qquad \boxed{\xi\ddot{\theta} + 2\dot{\xi}\dot{\theta} = 0} $$
and, once $\xi(t)$ and $\theta(t)$ are known,
$$ T = m\left(g + \ddot{\xi}\right), \qquad N = mg\sin\alpha - m\xi\dot{\theta}^2\sin\alpha\cos\alpha $$
* **First integrals** (independent of $T$ and $N$): see 3.4(f).

#### 3.4 Integration and Answers
##### (d) Condition for the string to remain taut
* **Pedagogical Justification:** the string can only pull, so $T \gt 0$ at all times:
$$ T = m\left(g + \ddot{\xi}\right) \gt 0 \iff \boxed{\ddot{\xi} \gt -g} $$
Substituting $\ddot{\xi} = \tfrac{1}{2}\left[\xi\dot{\theta}^2\sin^2\alpha - g(1 - \cos\alpha)\right]$ from the decoupled equation of (c) gives $T = \tfrac{m}{2}\left[g\left(1 + \cos\alpha\right) + \xi\dot{\theta}^2\sin^2\alpha\right] \gt 0$ for $0 \lt \alpha \lt \pi$, so the string stays taut throughout the motion.

> [!warning] Discrepancy with the official solution
> The key of `Problems.pdf` states the condition as $\ddot{\xi} \gt g$. That cannot be right: for the horizontal circular trajectory of part (e) the key itself gives $T = mg \gt 0$ with $\ddot{\xi} = 0$, which violates $\ddot{\xi} \gt g$, while $\ddot{\xi} = 0 \gt -g$ is satisfied. The equation of $P_2$ gives $T = m(g + \ddot{\xi})$, hence $\ddot{\xi} \gt -g$ (the minus sign is missing in the key).

##### (e) Circular trajectory on a parallel
* **Pedagogical Justification:** a horizontal circle on the cone has $\xi$ constant, so $\dot{\xi} = \ddot{\xi} = 0$ and the radial equation reduces to
$$ -\xi\dot{\theta}^2\sin^2\alpha + g\left(1 - \cos\alpha\right) = 0 \implies \boxed{\dot{\theta} = \frac{1}{\sin\alpha}\sqrt{\frac{g\left(1 - \cos\alpha\right)}{\xi}}} $$
* **Tension:** $T = m\left(g + 0\right) = mg$, directed on $P_1$ as $\mathbf{T}_1 = -mg\,\mathbf{e}_\xi = mg\left(-\sin\alpha\,\mathbf{e}_R + \cos\alpha\,\mathbf{k}\right)$.
* **Cone reaction:** with $\xi\dot{\theta}^2\sin^2\alpha = g\left(1 - \cos\alpha\right)$:
$$ N = mg\sin\alpha - m\cos\alpha\,\frac{g\left(1 - \cos\alpha\right)}{\sin\alpha} = \frac{mg}{\sin\alpha}\left(\sin^2\alpha - \cos\alpha + \cos^2\alpha\right) = \boxed{\frac{mg\left(1 - \cos\alpha\right)}{\sin\alpha}}, \qquad \mathbf{N} = N\left(\cos\alpha\,\mathbf{e}_R + \sin\alpha\,\mathbf{k}\right) $$
$N \gt 0$ for $0 \lt \alpha \lt \pi$: the cone presses on the particle (which would also be admissible for a one-sided contact).

##### (f) Two first integrals independent of the tension and the reactions
* **Azimuthal integral (first integral of the $\mathbf{e}_\theta$ equation).** With the product rule, the azimuthal acceleration is $\sin\alpha\left(\xi\ddot{\theta} + 2\dot{\xi}\dot{\theta}\right) = \dfrac{\sin\alpha}{\xi}\dfrac{d}{dt}\left(\xi^2\dot{\theta}\right)$. Gravity, the tension (toward $O$) and the cone reaction all lie in the meridian plane of $P_1$, so they have no $\mathbf{e}_\theta$ component:
$$ \frac{d}{dt}\left(\xi^2\dot{\theta}\right) = 0 \implies \boxed{\xi^2\dot{\theta} = C_1} $$
* **Energy.** The reactions do no work: $\mathbf{N}\cdot\mathbf{v}_1 = 0$ ($\mathbf{N}$ is normal to the surface) and the tension does the work $-T\dot{\xi}$ on $P_1$ and $+T\dot{\xi}$ on $P_2$, which cancel (inextensible string, smooth aperture). Gravity is conservative. The kinetic and potential energies are
$$ K = \tfrac{1}{2}m\left(\dot{\xi}^2 + \xi^2\dot{\theta}^2\sin^2\alpha\right) + \tfrac{1}{2}m\dot{\xi}^2 = m\dot{\xi}^2 + \tfrac{1}{2}m\xi^2\dot{\theta}^2\sin^2\alpha, \qquad V = -mg\xi\cos\alpha - mg(\ell - \xi) = mg\xi\left(1 - \cos\alpha\right) - mg\ell $$
$$ \boxed{2\dot{\xi}^2 + \xi^2\dot{\theta}^2\sin^2\alpha + 2g\xi\left(1 - \cos\alpha\right) = C_2} $$
where the constant $C_2$ absorbs $-2g\ell$ and the factor $2/m$.

### Phase 4: Interpretation & Checks
* **Effective potential.** With $\xi^2\dot{\theta} = C_1$ the energy becomes $2\dot{\xi}^2 + W(\xi) = C_2$ with $W(\xi) = \dfrac{C_1^2\sin^2\alpha}{\xi^2} + 2g\xi\left(1 - \cos\alpha\right)$. Its minimum is at $W'(\xi_c) = -\dfrac{2C_1^2\sin^2\alpha}{\xi_c^3} + 2g\left(1 - \cos\alpha\right) = 0$, i.e. $\xi_c\dot{\theta}^2\sin^2\alpha = g\left(1 - \cos\alpha\right)$, the circular parallel of (e); and $W'' = \dfrac{6C_1^2\sin^2\alpha}{\xi^4} \gt 0$, so it is a stable minimum.
* **Dimensional check:** $[\xi^2\dot{\theta}] = \text{m}^2\text{s}^{-1}$ and $[g\xi] = \text{m}^2\text{s}^{-2} = [\dot{\xi}^2]$; $[T] = [N] = \text{N}$.
* **Check against the official key:** the key of `Problems.pdf` gives two degrees of freedom, the quadratures $\xi^2\dot{\theta} = C_1$ and $2\dot{\xi}^2 + \xi^2\dot{\theta}^2\sin^2\alpha + 2g\xi(1 - \cos\alpha) = C_2$, the circular condition $\xi\dot{\theta}^2\sin^2\alpha = g(1 - \cos\alpha)$, $\mathbf{T} = mg\left(-\sin\alpha\,\mathbf{e}_R + \cos\alpha\,\mathbf{k}\right)$ and $\mathbf{N} = \dfrac{mg(1 - \cos\alpha)}{\sin\alpha}(\cdots)$. Everything agrees with the results above, with two remarks: the tension condition of the key ($\ddot{\xi} \gt g$) is an erratum (see (d)), and the key writes the direction of $\mathbf{N}$ with $\mathbf{e}_\theta$, which is tangent to the parallel and cannot be normal to the cone; the normal direction is $\cos\alpha\,\mathbf{e}_R + \sin\alpha\,\mathbf{k}$. Sympy confirms the three components of $\mathbf{a}_1$ and numerical integration of the equations of (c) ($\alpha = 40^\circ$) conserves $\xi^2\dot{\theta}$ and the energy to $3\times 10^{-14}$, with $T$ and $N$ positive throughout and $N/(mg) = 0.363970$ on the circular orbit, equal to $(1 - \cos\alpha)/\sin\alpha$.

---

## 📌 Problem 32: Particle with String on Spool

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a heavy particle $P$ of mass $m$ hangs from a string of length $l = 4\pi a$ that unwinds from a spool of radius $a$ and centre $O$, which rotates counterclockwise at the constant rate $\omega$. The string is massless, inextensible, thin and stays taut. One end is fixed to the spool at the point $A$ of its perimeter; $B$ is the point where the straight segment $BP$ leaves the spool, and $\phi$ is the angle between $Ox$ and $OB$. Initially $\overrightarrow{OA} = -a\,\mathbf{i}$ and $B$ never reaches $A$.
* **Constraints:** $P$ is a particle in the plane (2 coordinates). The string of fixed length that winds on the spool ties its position to the geometry: the free length $BP$ is $s = l - (\text{wrapped arc})$, and the attachment $A$ turns with the spool, so the constraint depends explicitly on time (rheonomic, holonomic) when $\omega \ne 0$. It is unilateral ($T \ge 0$, taut string).
* **Degrees of freedom (part a):** $\text{CDOF} = 2 - 1 = 1$, the angle $\phi$.
* **Parameters:** $m$, $a$, $l = 4\pi a$, $\omega$, $g$.

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $S_0 = \{O; \mathbf{i}, \mathbf{j}\}$ with $\mathbf{j}$ vertical upward.
* **Basis at $B$:** $\mathbf{u}_r = \cos\phi\,\mathbf{i} + \sin\phi\,\mathbf{j}$ (radial) and $\mathbf{u}_t = -\sin\phi\,\mathbf{i} + \cos\phi\,\mathbf{j}$ (counterclockwise tangent), a rotation of $\{\mathbf{i}, \mathbf{j}\}$ by $\phi$ (matrix $\begin{pmatrix}\cos \phi & -\sin \phi & 0\\ \sin \phi & \cos \phi & 0\\ 0 & 0 & 1\end{pmatrix}$, $\det = \cos^2\phi + \sin^2\phi = 1$; $RR^T$ has diagonal entries $\cos^2\phi + \sin^2\phi = 1$ (and $1$) and off-diagonal entries $\cos \phi\sin \phi - \sin \phi\cos \phi = 0$, so $RR^T = I$), with $\dot{\mathbf{u}}_r = \dot{\phi}\,\mathbf{u}_t$ and $\dot{\mathbf{u}}_t = -\dot{\phi}\,\mathbf{u}_r$. The straight segment leaves $B$ clockwise, toward the lower right in the figure, i.e. along $-\mathbf{u}_t$.

### Phase 3: Derivation

#### 3.1 Kinematics
##### (a) Degrees of freedom
* The particle moves in the plane (2 coordinates) but the string constraint leaves exactly **one** degree of freedom, $\phi$.

##### (b) Position, velocity and acceleration of $P$
* **Pedagogical Justification:** the point $B$ is at $a\,\mathbf{u}_r$ and $P$ is at the distance $s$ from $B$ along $-\mathbf{u}_t$. The length $s$ is the total length minus the wrapped arc. The attachment $A$ is at the angle $\pi + \omega t$ (it turns with the spool), and the string is wound from $B$ (angle $\phi$) to $A$, so the wrapped arc is $a(\pi + \omega t - \phi)$:
$$ s(t) = l - a\left(\pi + \omega t - \phi\right) = a\left(3\pi - \omega t + \phi\right), \qquad \dot{s} = a\left(\dot{\phi} - \omega\right) $$
$$ \mathbf{r}_P = a\,\mathbf{u}_r - s\,\mathbf{u}_t $$
* **Velocity** (product rule and Poisson's formula):
$$ \mathbf{v}_P = a\dot{\phi}\,\mathbf{u}_t - \dot{s}\,\mathbf{u}_t - s\left(-\dot{\phi}\,\mathbf{u}_r\right) = a\dot{\phi}\,\mathbf{u}_t - a\left(\dot{\phi} - \omega\right)\mathbf{u}_t + s\dot{\phi}\,\mathbf{u}_r = a\omega\,\mathbf{u}_t + s\dot{\phi}\,\mathbf{u}_r $$
* **Acceleration:**
$$ \mathbf{a}_P = a\omega\left(-\dot{\phi}\,\mathbf{u}_r\right) + \dot{s}\dot{\phi}\,\mathbf{u}_r + s\ddot{\phi}\,\mathbf{u}_r + s\dot{\phi}\left(\dot{\phi}\,\mathbf{u}_t\right) = \left[s\ddot{\phi} + a\dot{\phi}^2 - 2a\omega\dot{\phi}\right]\mathbf{u}_r + s\dot{\phi}^2\,\mathbf{u}_t $$
(using $\dot{s}\dot{\phi} = a\left(\dot{\phi} - \omega\right)\dot{\phi}$).

#### 3.2 Forces
##### (c) Forces on $P$
* **Weight:** $-mg\,\mathbf{j} = -mg\left(\sin\phi\,\mathbf{u}_r + \cos\phi\,\mathbf{u}_t\right)$.
* **Tension:** along the straight segment, toward $B$: $\mathbf{T} = +T\,\mathbf{u}_t$ with $T \gt 0$ (since $\mathbf{r}_B - \mathbf{r}_P = s\,\mathbf{u}_t$).
* **Inertia forces:** none. There is no other force: the string is the only constraint.

#### 3.3 Equations of Motion
##### (e) Closed set of equations
* **Pedagogical Justification:** Newton's second law in $S_0$ gives two scalar equations for the two unknowns $\phi(t)$ and $T(t)$. The radial projection contains no tension:
$$ \mathbf{u}_r: \; m\left[s\ddot{\phi} + a\dot{\phi}^2 - 2a\omega\dot{\phi}\right] = -mg\sin\phi, \qquad \mathbf{u}_t: \; ms\dot{\phi}^2 = T - mg\cos\phi $$
$$ \boxed{a\left[\left(3\pi - \omega t + \phi\right)\ddot{\phi} - 2\omega\dot{\phi} + \dot{\phi}^2\right] = -g\sin\phi}, \qquad \boxed{T = ma\left(3\pi - \omega t + \phi\right)\dot{\phi}^2 + mg\cos\phi} $$
The first is the equation of motion for $\phi(t)$; the tension follows from the second once $\phi(t)$ is known.

##### (d) Energy
* **Pedagogical Justification:** the power of the tension on $P$ is $\mathbf{T}\cdot\mathbf{v}_P = T\,\mathbf{u}_t\cdot\left(a\omega\,\mathbf{u}_t + s\dot{\phi}\,\mathbf{u}_r\right) = Ta\omega$. For $\omega \ne 0$ it is not zero (the contact point $B$ moves with the spool), so the tension does work on $P$ and the mechanical energy of $P$ is **not conserved**. For $\omega = 0$ the power is zero, the constraint is scleronomic and the energy is conserved.

#### 3.4 Integration and Answers
##### (f) Case $\omega = 0$
* **Pedagogical Justification:** with $\omega = 0$ the tension does no work and gravity is conservative, so the mechanical energy is a first integral that involves only $\phi$ and $\dot{\phi}$ (it contains no $\ddot{\phi}$). From $\mathbf{r}_P = a\,\mathbf{u}_r - s\,\mathbf{u}_t$ with $s = a(3\pi + \phi)$, the height is $y = a\sin\phi - a(3\pi + \phi)\cos\phi$, and $v^2 = s^2\dot{\phi}^2$ (from 3.1 with $\omega = 0$):
$$ \boxed{E = \tfrac{1}{2}m\left[a(3\pi + \phi)\right]^2\dot{\phi}^2 + mga\left[\sin\phi - (3\pi + \phi)\cos\phi\right] = \text{const}} $$

### Phase 4: Interpretation & Checks
* **Involute pendulum:** the system behaves like a pendulum whose effective length $s = a(3\pi - \omega t + \phi)$ changes as the string unwinds.
* **Dimensional check:** $[a\ddot{\phi}\,s/a] = \text{m s}^{-2}$, like $[g\sin\phi]$; $[T] = \left[ma\left(3\pi + \phi\right)\dot{\phi}^2\right] = \text{N}$.
* **Check against the official key:** the key of `Problems.pdf` gives the two equations $a\left[\left(3\pi - \omega t + \phi\right)\ddot{\phi} - 2\omega\dot{\phi} + \dot{\phi}^2\right] = -g\sin\phi$ and $ma\left(3\pi - \omega t + \phi\right)\dot{\phi}^2 = -mg\cos\phi + T$, the conservation of the mechanical energy for $\omega = 0$ and its quadrature $\tfrac{1}{2}m\left[a(3\pi + \phi)\right]^2\dot{\phi}^2 + mga\left[\sin\phi - (3\pi + \phi)\cos\phi\right] = E$. All coincide with the results above. Sympy reproduces $\mathbf{v}_P$ and $\mathbf{a}_P$ by differentiating $\mathbf{r}_P$, and numerical integration of the equation with $\omega = 0$ conserves the energy to $6\times 10^{-12}$ with $T \gt 0$.

---

## 📌 Problem 35: String with Two Particles on a Cylinder

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** two heavy particles $P$ and $Q$ of mass $m$ are joined by an inextensible massless string of length $L$ that rests on a fixed smooth cylinder of radius $R$ and centre $O$, and by a spring of zero natural length and stiffness $k$. The motion is planar, in $Oxy$ with $Oy$ upward. $A$ (right) and $B$ (left) are the tangency points of the string with the cylinder. The string stays taut and the spring does not touch the cylinder.
* **Constraints:** two free particles in the plane have $4$ coordinates. The inextensible string, taut and in contact with the cylinder, gives one holonomic constraint (unilateral: $T \ge 0$), so $\text{CDOF} = 4 - 1 = 3$. The smooth cylinder acts on the string, not on the particles.
* **Coordinates:** $A$ is at the polar angle $\alpha$ from $Ox$ and $B$ at the polar angle $\beta$. The straight segments $AP$ and $BQ$ have lengths $\xi_P$ and $\xi_Q$, and the string wraps the arc $AB$ of length $R(\beta - \alpha)$ on the cylinder:
$$ \xi_P + \xi_Q + R(\beta - \alpha) = L $$
The generalised coordinates are $(\alpha, \beta, \xi_P)$, with $\xi_Q = L - \xi_P - R(\beta - \alpha)$ (the four quantities $\alpha, \beta, \xi_P, \xi_Q$ are used below together with this one relation).
* **Parameters:** $m$ [kg], $L$ [m], $R$ [m], $k$ [N/m], $g$ [m/s$^2$]; $\ell_0 = (L - \pi R)/2$ [m] is defined in (e).

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $S_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$ fixed to the cylinder.
* **Bases following the contact points:** $\mathbf{n}$ is the outward normal of the cylinder and $\mathbf{t}$ the unit vector along the straight string, from the tangency point to the particle (clockwise at $A$, counterclockwise at $B$):
$$ \mathbf{n}_A = \cos\alpha\,\mathbf{i} + \sin\alpha\,\mathbf{j}, \quad \mathbf{t}_A = \sin\alpha\,\mathbf{i} - \cos\alpha\,\mathbf{j}, \qquad \mathbf{n}_B = \cos\beta\,\mathbf{i} + \sin\beta\,\mathbf{j}, \quad \mathbf{t}_B = -\sin\beta\,\mathbf{i} + \cos\beta\,\mathbf{j} $$
* **Changes of basis** (columns are the components of $\mathbf{t}_A, \mathbf{n}_A, \mathbf{k}$ and of $\mathbf{n}_B, \mathbf{t}_B, \mathbf{k}$):
$$ [{}_0 R_A] = \begin{pmatrix} \sin\alpha & \cos\alpha & 0 \\ -\cos\alpha & \sin\alpha & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad [{}_0 R_B] = \begin{pmatrix} \cos\beta & -\sin\beta & 0 \\ \sin\beta & \cos\beta & 0 \\ 0 & 0 & 1 \end{pmatrix} $$
$$ \det[{}_0 R_A] = \sin^2\alpha + \cos^2\alpha = 1, \quad \det[{}_0 R_B] = \cos^2\beta + \sin^2\beta = 1, \quad [{}_0 R_A][{}_0 R_A]^T = [{}_0 R_B][{}_0 R_B]^T = I $$
Multiplying out, $RR^T$ has diagonal entries $\cos^2 + \sin^2 = 1$ of the rotation angle (and $1$) and off-diagonal entries $\pm(\cos\sin - \sin\cos) = 0$, so it is the identity.
* **Time derivatives** (each basis turns about $\mathbf{k}$ at the rate of its angle):
$$ \dot{\mathbf{t}}_A = \dot{\alpha}\,\mathbf{n}_A, \quad \dot{\mathbf{n}}_A = -\dot{\alpha}\,\mathbf{t}_A, \qquad \dot{\mathbf{n}}_B = \dot{\beta}\,\mathbf{t}_B, \quad \dot{\mathbf{t}}_B = -\dot{\beta}\,\mathbf{n}_B $$

### Phase 3: Derivation

#### 3.1 Kinematics
##### (b) Position, velocity and acceleration
* **Pedagogical Justification:** each particle is at the tangency point plus the straight segment, $\mathbf{r}_P = R\,\mathbf{n}_A + \xi_P\,\mathbf{t}_A$ and $\mathbf{r}_Q = R\,\mathbf{n}_B + \xi_Q\,\mathbf{t}_B$. The derivatives use the product rule and the formulas of Phase 2:
$$ \mathbf{v}_P = -R\dot{\alpha}\,\mathbf{t}_A + \dot{\xi}_P\,\mathbf{t}_A + \xi_P\dot{\alpha}\,\mathbf{n}_A = \left(\dot{\xi}_P - R\dot{\alpha}\right)\mathbf{t}_A + \xi_P\dot{\alpha}\,\mathbf{n}_A $$
$$ \mathbf{a}_P = \left(\ddot{\xi}_P - R\ddot{\alpha}\right)\mathbf{t}_A + \left(\dot{\xi}_P - R\dot{\alpha}\right)\dot{\alpha}\,\mathbf{n}_A + \left(\dot{\xi}_P\dot{\alpha} + \xi_P\ddot{\alpha}\right)\mathbf{n}_A - \xi_P\dot{\alpha}^2\,\mathbf{t}_A = \left(\ddot{\xi}_P - R\ddot{\alpha} - \xi_P\dot{\alpha}^2\right)\mathbf{t}_A + \left(\xi_P\ddot{\alpha} + 2\dot{\xi}_P\dot{\alpha} - R\dot{\alpha}^2\right)\mathbf{n}_A $$
$$ \mathbf{v}_Q = \left(\dot{\xi}_Q + R\dot{\beta}\right)\mathbf{t}_B - \xi_Q\dot{\beta}\,\mathbf{n}_B, \qquad \mathbf{a}_Q = \left(\ddot{\xi}_Q + R\ddot{\beta} - \xi_Q\dot{\beta}^2\right)\mathbf{t}_B - \left(\xi_Q\ddot{\beta} + 2\dot{\xi}_Q\dot{\beta} + R\dot{\beta}^2\right)\mathbf{n}_B $$
$\mathbf{a}_Q$ follows from $\mathbf{v}_Q$ exactly as $\mathbf{a}_P$ from $\mathbf{v}_P$, with $\dot{\mathbf{t}}_B$ and $\dot{\mathbf{n}}_B$ of Phase 2 and $\beta$ in place of $\alpha$. In terms of the chosen coordinates $(\alpha, \beta, \xi_P)$: $\xi_Q = L - \xi_P - R(\beta - \alpha)$, $\dot{\xi}_Q = -\dot{\xi}_P - R(\dot{\beta} - \dot{\alpha})$ (so $\dot{\xi}_Q + R\dot{\beta} = R\dot{\alpha} - \dot{\xi}_P$) and $\ddot{\xi}_Q + R\ddot{\beta} = R\ddot{\alpha} - \ddot{\xi}_P$.

#### 3.2 Forces
##### (c) Forces on $P$ and $Q$
* **Weights:** $-mg\,\mathbf{j}$ on each particle.
* **String tension** $T \ge 0$ (the same on both sides: the cylinder is smooth and the string massless): $-T\,\mathbf{t}_A$ on $P$ and $-T\,\mathbf{t}_B$ on $Q$, directed toward the tangency points.
* **Spring** (zero natural length): $\mathbf{F}_{s,P} = k\,\mathbf{d}$ and $\mathbf{F}_{s,Q} = -k\,\mathbf{d}$, with $\mathbf{d} = \mathbf{r}_Q - \mathbf{r}_P$.
* **Inertia forces:** none. The projections of the weight on the bases are $\mathbf{j}\cdot\mathbf{t}_A = -\cos\alpha$, $\mathbf{j}\cdot\mathbf{n}_A = \sin\alpha$, $\mathbf{j}\cdot\mathbf{t}_B = \cos\beta$, $\mathbf{j}\cdot\mathbf{n}_B = \sin\beta$.

#### 3.3 Equations of Motion
* **Pedagogical Justification:** Newton's second law for $P$ and $Q$, projected on the bases of the contact points, gives four scalar equations; together with the length constraint there are 5 equations for the 5 unknowns $\alpha, \beta, \xi_P, \xi_Q, T$:
$$ m\left(\ddot{\xi}_P - R\ddot{\alpha} - \xi_P\dot{\alpha}^2\right) = -T + mg\cos\alpha + k\,\mathbf{d}\cdot\mathbf{t}_A $$
$$ m\left(\xi_P\ddot{\alpha} + 2\dot{\xi}_P\dot{\alpha} - R\dot{\alpha}^2\right) = -mg\sin\alpha + k\,\mathbf{d}\cdot\mathbf{n}_A $$
$$ m\left(\ddot{\xi}_Q + R\ddot{\beta} - \xi_Q\dot{\beta}^2\right) = -T - mg\cos\beta - k\,\mathbf{d}\cdot\mathbf{t}_B $$
$$ -m\left(\xi_Q\ddot{\beta} + 2\dot{\xi}_Q\dot{\beta} + R\dot{\beta}^2\right) = -mg\sin\beta - k\,\mathbf{d}\cdot\mathbf{n}_B $$
* **Decoupling.** Subtracting the first and third equations removes the tension $T$; the remaining equations, with the length constraint, determine the three coordinates, and $T$ is computed afterwards.

#### 3.4 Integration and Answers
##### (a) Degrees of freedom
* $\text{CDOF} = 3$ (see Phase 1): for example $(\alpha, \beta, \xi_P)$.

##### (d) Mechanical energy
* **Pedagogical Justification:** the energy of $P$ alone is not conserved: the tension and the spring both do work on it, and that work is exchanged with $Q$. For the system $P + Q$, the only forces that could dissipate energy are the tensions, so their total power is computed first, with $\mathbf{t}_A\cdot\mathbf{v}_P = \dot{\xi}_P - R\dot{\alpha}$ and $\mathbf{t}_B\cdot\mathbf{v}_Q = \dot{\xi}_Q + R\dot{\beta}$:
$$ \dot{W}_T = -T\,\mathbf{t}_A\cdot\mathbf{v}_P - T\,\mathbf{t}_B\cdot\mathbf{v}_Q = -T\,\frac{d}{dt}\left[\xi_P + \xi_Q + R(\beta - \alpha)\right] = -T\dot{L} = 0 $$
* The tensions do zero net work. Gravity and the spring are conservative, so the total mechanical energy of the system is conserved, with the potential energy
$$ V = mg\left(y_P + y_Q\right) + \tfrac{1}{2}k\left|\mathbf{r}_Q - \mathbf{r}_P\right|^2, \qquad E = \tfrac{1}{2}m\left(v_P^2 + v_Q^2\right) + V = \text{const} $$

##### (e) Symmetric configurations about $Oy$
* **Pedagogical Justification:** if the motion keeps the mirror symmetry about $Oy$, then $\beta = \pi - \alpha$ and $\xi_P = \xi_Q = \xi$. The length constraint becomes $2\xi + R(\pi - 2\alpha) = L$, i.e.
$$ \xi(\alpha) = \ell_0 + R\alpha, \qquad \ell_0 = \frac{L - \pi R}{2} $$
* The system has $\text{CDOF} = 1$, the angle $\alpha$. The relations between the previous coordinates are $\beta = \pi - \alpha$, $\xi_P = \xi_Q = \ell_0 + R\alpha$ and $\dot{\xi} = R\dot{\alpha}$.

##### (f) Equilibrium and small oscillations
* **Pedagogical Justification:** with the symmetry, one coordinate $\alpha$ describes the system. The coordinates of $P$ are $x_P = R\cos\alpha + \xi\sin\alpha$ and $y_P = R\sin\alpha - \xi\cos\alpha$. Differentiating with respect to $\alpha$ (with $\xi' = R$):
$$ x_P' = -R\sin\alpha + R\sin\alpha + \xi\cos\alpha = \xi\cos\alpha, \qquad y_P' = R\cos\alpha - R\cos\alpha + \xi\sin\alpha = \xi\sin\alpha $$
so $v_P = \xi\dot{\alpha}$. By symmetry $x_Q = -x_P$, $y_Q = y_P$ and $|\mathbf{r}_Q - \mathbf{r}_P| = 2x_P$:
$$ K = 2\cdot\tfrac{1}{2}m\xi^2\dot{\alpha}^2 = m\xi^2\dot{\alpha}^2, \qquad V(\alpha) = 2mgy_P + \tfrac{1}{2}k(2x_P)^2 = 2mgy_P + 2kx_P^2 $$
$$ V'(\alpha) = 2mg\xi\sin\alpha + 4kx_P\xi\cos\alpha = 2\xi f(\alpha), \qquad f(\alpha) = mg\sin\alpha + 2k\cos\alpha\left(R\cos\alpha + \xi\sin\alpha\right) $$
* **Equilibrium.** $V'(\alpha_0) = 0$, i.e. $f(\alpha_0) = 0$ (since $\xi \gt 0$). Physically, the horizontal pull $2kx_P$ of the spring must be balanced by the horizontal component of the tension, which needs $\alpha_0 \lt 0$: the segments $AP$ and $BQ$ are slightly inclined inward. For a small deviation from the vertical, $|\alpha_0| \ll 1$, keep first-order terms ($\sin\alpha \approx \alpha$, $\cos\alpha \approx 1$, $\xi \approx \ell_0$):
$$ mg\alpha_0 + 2k\left(R + \ell_0\alpha_0\right) = 0 \implies \alpha_0 \approx -\frac{2kR}{mg + 2k\ell_0} $$
and the other coordinates at equilibrium follow from the symmetry relations: $\beta_0 = \pi - \alpha_0 \approx \pi + \dfrac{2kR}{mg + 2k\ell_0}$ and $\xi_0 = \ell_0 + R\alpha_0 \approx \ell_0 - \dfrac{2kR^2}{mg + 2k\ell_0}$.
* **Equation of motion.** From $\frac{d}{dt}(K + V) = 0$ with the chain rule and $\dot{\xi} = R\dot{\alpha}$:
$$ 2m\xi^2\dot{\alpha}\ddot{\alpha} + 2m\xi R\dot{\alpha}^3 + 2\xi f\dot{\alpha} = 0 \implies m\xi\ddot{\alpha} + mR\dot{\alpha}^2 + f(\alpha) = 0 $$
This is the $\mathbf{n}_A$ equation of 3.3 with $\dot{\xi}_P = R\dot{\alpha}$ and $\mathbf{d}\cdot\mathbf{n}_A = -2x_P\cos\alpha$.
* **Linearisation.** Put $\alpha = \alpha_0 + \delta$ with $\delta$ small: $\dot{\alpha}^2$ is second order and $f(\alpha) \approx f'(\alpha_0)\delta$, with $f'(\alpha) = mg\cos\alpha + 2k\left[\xi\cos^2\alpha - x_P\sin\alpha\right] \approx mg + 2k\ell_0$:
$$ \ddot{\delta} + \frac{mg + 2k\ell_0}{m\ell_0}\,\delta = 0 \implies \omega^2 = \frac{g}{\ell_0} + \frac{2k}{m}, \qquad \boxed{\omega = \sqrt{\frac{g}{\ell_0} + \frac{2k}{m}}} $$

### Phase 4: Interpretation & Checks
* **Limit $k \to 0$:** $\omega = \sqrt{g/\ell_0}$, the pendulum of length $\ell_0$ (the free length of each hanging segment).
* **Limit $g \to 0$:** $\omega = \sqrt{2k/m}$, the frequency of two particles of mass $m$ joined by a spring $k$ (reduced mass $m/2$ and stiffness $k$). In this limit $\alpha_0 \to -R/\ell_0$, which is small only if $R \ll \ell_0$; otherwise the limit lies outside the small-angle hypothesis.
* **Dimensional check:** $[g/\ell_0] = \text{s}^{-2}$, $[2k/m] = \text{N m}^{-1}\text{kg}^{-1} = \text{s}^{-2}$; $[\alpha_0] = [kR/(mg + 2k\ell_0)] = 1$.
* **Check against the official key:** `Problems.pdf` gives only the spring force, $\mathbf{F}_{S,P} = -\mathbf{F}_{S,Q} = k\overrightarrow{PQ} = k(\mathbf{r}_Q - \mathbf{r}_P)$ written in its own coordinates, which is the same vector as $k\,\mathbf{d}$ above. The remaining results are verified by independent derivation and numerically ($R = 1$ m, $\ell_0 = 2$ m, $m = 1$ kg, $k = 0.3$ N/m, $g = 9.81$ m/s$^2$): the exact root of $f(\alpha_0) = 0$ is $\alpha_0 = -0.054532$ rad against $-0.054496$ rad from the linear formula, and integrating $m\xi\ddot{\alpha} + mR\dot{\alpha}^2 + f = 0$ gives $\omega^2 = 5.6482$ s$^{-2}$, equal to $f'(\alpha_0)/(m\xi(\alpha_0))$; the difference with $g/\ell_0 + 2k/m = 5.505$ s$^{-2}$ is the first-order correction $\xi(\alpha_0) = \ell_0 + R\alpha_0$ in place of $\ell_0$.

---

## 📌 Problem 38: Particle on Torus

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a heavy particle $P$ ($m_P = 1$) moves without friction on the vertical torus $x_0 = (2 + \cos\phi)\sin\theta$, $y_0 = \sin\phi$, $z_0 = 4 + (2 + \cos\phi)\cos\theta$, and cannot separate from its surface. A second particle $Q$ ($m_Q = 2$) is constrained to the plane $Ox_0y_0$ without friction. $P$ and $Q$ attract each other with a force proportional to their distance, with constant $k = 2$.
* **Initial state:** $\mathbf{r}_P(t_0) = 2\mathbf{i}_0 + \mathbf{j}_0 + 4\mathbf{k}_0$, $\mathbf{v}_P(t_0) = -\mathbf{k}_0$; $\mathbf{r}_Q(t_0) = 3\mathbf{i}_0 + \mathbf{j}_0$, $\mathbf{v}_Q(t_0) = -\mathbf{i}_0 + \mathbf{j}_0$.
* **Constraints and degrees of freedom (a):** two free particles have $6$ coordinates. $P$ is on the torus surface ($1$ constraint) and $Q$ is on the plane $z_0 = 0$ ($1$ constraint), so $\text{CDOF} = 6 - 2 = 4$. A minimal set: $(\theta, \phi)$ for $P$, where $\theta$ is the toroidal angle (rotation about $\mathbf{j}_0$ of the axis of the torus, which passes through $z_0 = 4$) and $\phi$ the poloidal angle (angle around the tube, whose centre circle has radius $2$ and the tube radius is $1$); and $(\xi, \eta)$ for $Q$, its Cartesian coordinates in the plane.
* **Initial values of the coordinates:** from $x_0 = 2$, $y_0 = 1$, $z_0 = 4$: $\sin\phi = 1$ and $(2 + \cos\phi)\sin\theta = 2$, so $\phi = \theta = \pi/2$. The initial velocity $-\mathbf{k}_0$ gives $\dot{\theta}(0) = 1/2$ and $\dot{\phi}(0) = 0$ (shown in 3.1), and $\xi = 3$, $\eta = 1$, $\dot{\xi} = -1$, $\dot{\eta} = 1$.
* **Parameters:** $m_P = 1$, $m_Q = 2$, $k = 2$, $g = 9.81$ m/s$^2$.

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $S_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ with $\mathbf{k}_0$ vertical upward.
* **Toroidal basis.** With $\theta$ (rotation about $\mathbf{j}_0$): $\mathcal{B}_1 = \{\mathbf{e}_\rho, \mathbf{e}_\theta, \mathbf{j}_0\}$ with $\mathbf{e}_\rho = \sin\theta\,\mathbf{i}_0 + \cos\theta\,\mathbf{k}_0$ and $\mathbf{e}_\theta = \cos\theta\,\mathbf{i}_0 - \sin\theta\,\mathbf{k}_0$ (so $\mathbf{e}_\rho\times\mathbf{e}_\theta = \mathbf{j}_0$):
$$ [{}_0 R_1] = \begin{pmatrix} \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \\ \cos\theta & -\sin\theta & 0 \end{pmatrix}, \qquad \det[{}_0 R_1] = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
Multiplying out, $RR^T$ has diagonal entries $\cos^2 + \sin^2 = 1$ of the rotation angle (and $1$) and off-diagonal entries $\pm(\cos\sin - \sin\cos) = 0$, so it is the identity.
with $\dot{\mathbf{e}}_\rho = \dot{\theta}\,\mathbf{e}_\theta$ and $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_\rho$.
* **Poloidal basis.** With $\phi$ (rotation about $\mathbf{e}_\theta$): $\mathcal{B}_2 = \{\mathbf{n}, \mathbf{e}_\theta, \mathbf{t}_\phi\}$ with $\mathbf{n} = \cos\phi\,\mathbf{e}_\rho + \sin\phi\,\mathbf{j}_0$ (outward normal) and $\mathbf{t}_\phi = -\sin\phi\,\mathbf{e}_\rho + \cos\phi\,\mathbf{j}_0$:
$$ [{}_1 R_2] = \begin{pmatrix} \cos\phi & 0 & -\sin\phi \\ 0 & 1 & 0 \\ \sin\phi & 0 & \cos\phi \end{pmatrix}, \qquad \det[{}_1 R_2] = 1, \qquad [{}_1 R_2][{}_1 R_2]^T = I $$
Multiplying out, $RR^T$ has diagonal entries $\cos^2 + \sin^2 = 1$ of the rotation angle (and $1$) and off-diagonal entries $\pm(\cos\sin - \sin\cos) = 0$, so it is the identity.

### Phase 3: Derivation

#### 3.1 Kinematics
##### (b) Position, velocity and acceleration
* **Pedagogical Justification:** with $\varrho \equiv 2 + \cos\phi$, the position of $P$ is $\mathbf{r}_P = 4\mathbf{k}_0 + \varrho\,\mathbf{e}_\rho + \sin\phi\,\mathbf{j}_0$ and that of $Q$ is $\mathbf{r}_Q = \xi\,\mathbf{i}_0 + \eta\,\mathbf{j}_0$. With $\dot{\varrho} = -\sin\phi\,\dot{\phi}$ and Poisson's formula,
$$ \mathbf{v}_P = -\sin\phi\,\dot{\phi}\,\mathbf{e}_\rho + \varrho\dot{\theta}\,\mathbf{e}_\theta + \cos\phi\,\dot{\phi}\,\mathbf{j}_0, \qquad v_P^2 = \dot{\phi}^2 + \varrho^2\dot{\theta}^2 $$
$$ \mathbf{a}_P = \left(\ddot{\varrho} - \varrho\dot{\theta}^2\right)\mathbf{e}_\rho + \left(\varrho\ddot{\theta} + 2\dot{\varrho}\dot{\theta}\right)\mathbf{e}_\theta + \left(\cos\phi\,\ddot{\phi} - \sin\phi\,\dot{\phi}^2\right)\mathbf{j}_0, \qquad \ddot{\varrho} = -\cos\phi\,\dot{\phi}^2 - \sin\phi\,\ddot{\phi} $$
$$ \mathbf{v}_Q = \dot{\xi}\,\mathbf{i}_0 + \dot{\eta}\,\mathbf{j}_0, \qquad \mathbf{a}_Q = \ddot{\xi}\,\mathbf{i}_0 + \ddot{\eta}\,\mathbf{j}_0 $$
* **Initial rates.** At $\theta = \phi = \pi/2$: $\mathbf{e}_\theta = -\mathbf{k}_0$, $\varrho = 2$, so $\mathbf{v}_P = -\dot{\phi}\,\mathbf{e}_\rho - 2\dot{\theta}\,\mathbf{k}_0 = -\mathbf{k}_0$ gives $\dot{\theta}(0) = 1/2$ and $\dot{\phi}(0) = 0$.

##### (c) Two tangent vectors and one normal vector to the torus
* The two independent tangent vectors are the partial derivatives of $\mathbf{r}_P$, and the normal is their cross product:
$$ \frac{\partial\mathbf{r}_P}{\partial\theta} = \varrho\,\mathbf{e}_\theta, \qquad \frac{\partial\mathbf{r}_P}{\partial\phi} = \mathbf{t}_\phi, \qquad \frac{\partial\mathbf{r}_P}{\partial\theta}\times\frac{\partial\mathbf{r}_P}{\partial\phi} = \varrho\,\mathbf{n} $$

#### 3.2 Forces
##### (d) Forces on $P$ and $Q$
* **On $P$:** its weight $-m_Pg\,\mathbf{k}_0$; the attraction of $Q$, $\mathbf{F} = k\left(\mathbf{r}_Q - \mathbf{r}_P\right)$; and the reaction of the smooth torus $N\,\mathbf{n}$ (normal, with unknown magnitude; it does not enter the tangent projections). Explicitly,
$$ \mathbf{F} = 2\left[\xi - (2 + \cos\phi)\sin\theta\right]\mathbf{i}_0 + 2\left[\eta - \sin\phi\right]\mathbf{j}_0 - 2\left[4 + (2 + \cos\phi)\cos\theta\right]\mathbf{k}_0 $$
* **On $Q$:** the attraction $-\mathbf{F}$ and its weight $-m_Qg\,\mathbf{k}_0$, balanced by the vertical reaction of the smooth plane (so the motion of $Q$ is horizontal). **Inertia forces:** none.

#### 3.3 Equations of Motion
##### (e) Second-order equations for the four coordinates
* **Pedagogical Justification:** the unknown reaction $N\,\mathbf{n}$ is orthogonal to the two tangent vectors, so projecting Newton's second law for $P$ on $\mathbf{e}_\theta$ and on $\mathbf{t}_\phi$ gives two equations free of $N$. With $\mathbf{k}_0 = \cos\theta\,\mathbf{e}_\rho - \sin\theta\,\mathbf{e}_\theta$, $\mathbf{i}_0 = \sin\theta\,\mathbf{e}_\rho + \cos\theta\,\mathbf{e}_\theta$, and the accelerations of 3.1:
$$ \mathbf{a}_P\cdot\mathbf{e}_\theta = \varrho\ddot{\theta} - 2\sin\phi\,\dot{\phi}\dot{\theta}, \qquad \mathbf{a}_P\cdot\mathbf{t}_\phi = \ddot{\phi} + \varrho\sin\phi\,\dot{\theta}^2 $$
$$ \left(\mathbf{F} - m_Pg\,\mathbf{k}_0\right)\cdot\mathbf{e}_\theta = m_Pg\sin\theta + k\left(\xi\cos\theta + 4\sin\theta\right) $$
$$ \left(\mathbf{F} - m_Pg\,\mathbf{k}_0\right)\cdot\mathbf{t}_\phi = m_Pg\sin\phi\cos\theta + k\left(-\xi\sin\phi\sin\theta + \eta\cos\phi + 4\sin\phi\cos\theta + 2\sin\phi\right) $$
* **Equations of motion** (with $m_P = 1$, $m_Q = 2$, $k = 2$; for $Q$, $m_Q\ddot{\xi} = -k(\xi - x_P)$ and $m_Q\ddot{\eta} = -k(\eta - y_P)$):
$$ (2 + \cos\phi)\,\ddot{\theta} = 2\sin\phi\,\dot{\phi}\dot{\theta} + g\sin\theta + 2\left(\xi\cos\theta + 4\sin\theta\right) $$
$$ \ddot{\phi} = -(2 + \cos\phi)\sin\phi\,\dot{\theta}^2 + g\sin\phi\cos\theta + 2\left(-\xi\sin\phi\sin\theta + \eta\cos\phi + 4\sin\phi\cos\theta + 2\sin\phi\right) $$
$$ \ddot{\xi} = -\left[\xi - (2 + \cos\phi)\sin\theta\right], \qquad \ddot{\eta} = -\left[\eta - \sin\phi\right] $$
* **Check of closure:** four unknown coordinates and four equations; the reaction of the torus follows afterwards from the $\mathbf{n}$ projection (the statement says that $P$ cannot separate from the surface, so the constraint is bilateral and $N$ may have either sign).

#### 3.4 Integration and Answers
##### (f) A scalar conservation law
* **Pedagogical Justification:** the reactions of the torus and of the plane are normal to the velocities of $P$ and $Q$ and do no work; gravity and the spring are conservative; there are no other forces. The total mechanical energy of the system is conserved:
$$ E = \tfrac{1}{2}m_Pv_P^2 + \tfrac{1}{2}m_Qv_Q^2 + m_Pgz_P + \tfrac{1}{2}k\left|\mathbf{r}_P - \mathbf{r}_Q\right|^2 = \text{const} $$
* **Initial value:**
$$ T_P = \tfrac{1}{2}(1)(1)^2 = \tfrac{1}{2}, \qquad T_Q = \tfrac{1}{2}(2)\left((-1)^2 + 1^2\right) = 2, \qquad V_g = m_Pgz_P(t_0) = 4g $$
$$ \left|\mathbf{r}_P - \mathbf{r}_Q\right|^2 = (2 - 3)^2 + (1 - 1)^2 + (4 - 0)^2 = 17 \implies V_{\text{spring}} = \tfrac{1}{2}(2)(17) = 17, \qquad E_0 = \tfrac{1}{2} + 2 + 4g + 17 = 19.5 + 4g $$

##### (g) Can $P$ reach the highest point of the torus?
* **Pedagogical Justification:** use the conservation law alone. The highest point of the torus is at $\phi = 0$, $\theta = 0$, with $z_{\max} = 4 + (2 + 1) = 7$. There the gravitational energy of $P$ is $7g$, and the other terms of $E$ (the kinetic energies and the spring energy) are non-negative, so reaching the summit requires $E_0 \ge 7g$:
$$ E_0 = 19.5 + 4g \ge 7g \iff 19.5 \ge 3g = 29.43 \quad\text{(false)} $$
* **Answer:** no. With $g = 9.81$ m/s$^2$, $E_0 = 58.74$ J and the summit needs at least $7g = 68.67$ J, a deficit of $9.93$ J.

### Phase 4: Interpretation & Checks
* **Robustness:** for a general stiffness $E_0 = 2.5 + 4g + 8.5k$. At the summit $z_P = 7$ and $z_Q = 0$, so $|\mathbf{r}_P - \mathbf{r}_Q| \ge 7$ and $V_{\text{spring}} \ge \tfrac12 k\cdot 49 = 24.5k$. Reaching it requires $2.5 + 4g + 8.5k \ge 7g + 24.5k$, i.e. $2.5 \ge 3g + 16k$, false for every $k \ge 0$: the conclusion does not depend on $k$. (With $k = 2$: $58.74$ J against at least $68.67 + 49 = 117.67$ J.)
* **Dimensional check:** $[k|\mathbf{r}_P - \mathbf{r}_Q|^2] = \text{N m}^{-1}\text{m}^2 = \text{J}$, $[mgz] = \text{J}$ and $[mv^2] = \text{J}$.
* **Check against the official key:** `Problems.pdf` gives the force on $P$ due to $Q$, $\mathbf{F}_P = 2\left[\xi - (2 + \cos\phi)\sin\theta\right]\mathbf{i}_0 + 2\left[\eta - \sin\phi\right]\mathbf{j}_0 - 2\left[4 + (2 + \cos\phi)\cos\theta\right]\mathbf{k}_0$ (the key writes the same vector with its own letters), identical to part (d). The rest is verified by independent derivation. Sympy confirms the two tangent vectors and the normal, the projections of $\mathbf{a}_P$ and of the forces used in (e), and numerical integration of the four equations (DOP853) conserves $E$ to $2\times 10^{-11}$ with $E_0 = 58.74$ and keeps $z_P \le 4$ over $6$ s (the summit $z = 7$ is not approached).

---

## 📌 Problem 39: Particle on a String with a Plate

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a heavy particle $P$ of mass $m$ hangs from a massless inextensible string of length $\ell$ anchored at the point $O$ of the upper surface of a thin horizontal plate. The string passes without friction over the straight edge of the plate, at perpendicular distance $d$ from $O$, at the contact point $Q$; it remains taut and in contact with the plate.
* **Geometry (read from the figure, `Problems.pdf` PDF page 27).** The edge is the straight line $x_0 = d$, parallel to $\mathbf{j}_0$ ($Ox_0$ is perpendicular to the edge); $\theta$ is the angle between $Ox_0$ and $OQ$, so $\mathbf{r}_Q = d\,\mathbf{i}_0 + d\tan\theta\,\mathbf{j}_0$; and $\phi$ is the angle between the vertical and the line through $P$ perpendicular to the edge, which lies in a plane normal to the edge. The statement text does not fix the direction of the edge, so this reading relies on the figure.
* **Constraints and degrees of freedom (a):** $P$ has $3$ coordinates. The string has constant length: $|OQ| + |QP| = \ell$ with $Q$ on the edge, and $Q$ slides on the edge (the position of $Q$ on the edge is not fixed). The frictionless sliding over the edge makes the two string segments meet the edge at equal angles (the hint of the statement). These conditions leave the two independent coordinates $\theta$ and $\phi$: $\text{CDOF} = 2$.
* **Initial state:** $\theta(0) = \phi(0) = \pi/3$ and $|\mathbf{v}_P(0)| = \sqrt{\ell g}$.
* **Parameters:** $m$, $\ell$, $d$, $g$.

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $S_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ with $\mathbf{k}_0$ vertical upward; the plate in the plane $z_0 = 0$.
* **Lengths:** $|OQ| = d/\cos\theta$, so the hanging segment has length $\rho = \ell - \dfrac{d}{\cos\theta}$.
* **Swing basis.** The hanging segment $QP$ swings in the plane normal to the edge, i.e. about the direction $\mathbf{j}_0$. The basis $\mathcal{B}_1 = \{\mathbf{i}_1, \mathbf{j}_0, \mathbf{k}_1\}$ is the inertial basis rotated by $-\phi$ about $\mathbf{j}_0$ (by $\phi$ about $-\mathbf{j}_0$), with $\mathbf{i}_1 = \cos\phi\,\mathbf{i}_0 + \sin\phi\,\mathbf{k}_0$ and $\mathbf{k}_1 = -\sin\phi\,\mathbf{i}_0 + \cos\phi\,\mathbf{k}_0$ (columns in $\mathcal{B}_0$):
$$ [{}_0 R_1] = \begin{pmatrix} \cos\phi & 0 & -\sin\phi \\ 0 & 1 & 0 \\ \sin\phi & 0 & \cos\phi \end{pmatrix}, \qquad \det[{}_0 R_1] = \cos^2\phi + \sin^2\phi = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
Multiplying out, $RR^T$ has diagonal entries $\cos^2 + \sin^2 = 1$ of the rotation angle (and $1$) and off-diagonal entries $\pm(\cos\sin - \sin\cos) = 0$, so it is the identity.

### Phase 3: Derivation

#### 3.1 Kinematics
##### (b) Unit vector from $Q$ to $P$
* **Pedagogical Justification:** the edge is frictionless, so the two string segments make equal angles with it (the hint). The unit vector from $Q$ to $O$ is $-\left(\cos\theta\,\mathbf{i}_0 + \sin\theta\,\mathbf{j}_0\right)$, hence $\mathbf{e}_{QP}\cdot\mathbf{j}_0 = \sin\theta$. The remaining part of $\mathbf{e}_{QP}$ lies in the plane normal to the edge, along $\sin\phi\,\mathbf{i}_0 - \cos\phi\,\mathbf{k}_0 = -\mathbf{k}_1$, with magnitude $\sqrt{1 - \sin^2\theta} = \cos\theta$:
$$ \mathbf{e}_{QP} = \cos\theta\sin\phi\,\mathbf{i}_0 + \sin\theta\,\mathbf{j}_0 - \cos\theta\cos\phi\,\mathbf{k}_0 = \sin\theta\,\mathbf{j}_0 - \cos\theta\,\mathbf{k}_1, \qquad |\mathbf{e}_{QP}|^2 = \cos^2\theta\left(\sin^2\phi + \cos^2\phi\right) + \sin^2\theta = 1 $$

##### (c) Position, velocity and acceleration
* **Pedagogical Justification:** $Q$ is on the edge and $P$ hangs at the distance $\rho$ along $\mathbf{e}_{QP}$:
$$ \mathbf{r}_Q = d\,\mathbf{i}_0 + d\tan\theta\,\mathbf{j}_0, \qquad \mathbf{v}_Q = \frac{d\dot{\theta}}{\cos^2\theta}\,\mathbf{j}_0, \qquad \mathbf{r}_P = \mathbf{r}_Q + \rho\,\mathbf{e}_{QP} $$
$$ \mathbf{r}_P = \left[d + (\ell\cos\theta - d)\sin\phi\right]\mathbf{i}_0 + \left[d\tan\theta + \left(\ell - \frac{d}{\cos\theta}\right)\sin\theta\right]\mathbf{j}_0 - (\ell\cos\theta - d)\cos\phi\,\mathbf{k}_0 $$
(using $\rho\cos\theta = \ell\cos\theta - d$). Write $u \equiv \ell\cos\theta - d = \rho\cos\theta \ge 0$. The $\mathbf{j}_0$ component simplifies, $d\tan\theta + \ell\sin\theta - d\tan\theta = \ell\sin\theta$, so
$$ \mathbf{r}_P = \left(d + u\sin\phi\right)\mathbf{i}_0 + \ell\sin\theta\,\mathbf{j}_0 - u\cos\phi\,\mathbf{k}_0, \qquad z_P = -u\cos\phi, \qquad \frac{du}{d\theta} = -\ell\sin\theta $$
* **Velocity of $P$.** The chain rule gives $\mathbf{v}_P = \mathbf{t}_\theta\dot{\theta} + \mathbf{t}_\phi\dot{\phi}$ with the tangent vectors
$$ \mathbf{t}_\theta = \frac{\partial\mathbf{r}_P}{\partial\theta} = \ell\begin{pmatrix} -\sin\theta\sin\phi \\ \cos\theta \\ \sin\theta\cos\phi \end{pmatrix}, \qquad \mathbf{t}_\phi = \frac{\partial\mathbf{r}_P}{\partial\phi} = u\begin{pmatrix} \cos\phi \\ 0 \\ \sin\phi \end{pmatrix} $$
They are orthogonal ($\mathbf{t}_\theta\cdot\mathbf{t}_\phi = \ell u\sin\theta\sin\phi\cos\phi\,(-1 + 1) = 0$) with $|\mathbf{t}_\theta|^2 = \ell^2\left(\sin^2\theta + \cos^2\theta\right) = \ell^2$ and $|\mathbf{t}_\phi|^2 = u^2$, so
$$ v_P^2 = \ell^2\dot{\theta}^2 + u^2\dot{\phi}^2 $$
* **Acceleration of $P$.** Differentiating once more (product rule, with $\mathbf{t}_{\theta\theta} = \partial^2\mathbf{r}_P/\partial\theta^2$ and so on):
$$ \mathbf{a}_P = \mathbf{t}_\theta\ddot{\theta} + \mathbf{t}_\phi\ddot{\phi} + \mathbf{t}_{\theta\theta}\dot{\theta}^2 + 2\mathbf{t}_{\theta\phi}\dot{\theta}\dot{\phi} + \mathbf{t}_{\phi\phi}\dot{\phi}^2 $$
$$ \mathbf{t}_{\theta\theta} = \ell\begin{pmatrix} -\cos\theta\sin\phi \\ -\sin\theta \\ \cos\theta\cos\phi \end{pmatrix}, \quad \mathbf{t}_{\theta\phi} = -\ell\sin\theta\begin{pmatrix} \cos\phi \\ 0 \\ \sin\phi \end{pmatrix}, \quad \mathbf{t}_{\phi\phi} = u\begin{pmatrix} -\sin\phi \\ 0 \\ \cos\phi \end{pmatrix} $$
* **Velocity and acceleration of $Q$.** From $\mathbf{v}_Q = d\dot{\theta}\cos^{-2}\theta\,\mathbf{j}_0$ and $\frac{d}{dt}\cos^{-2}\theta = 2\sin\theta\cos^{-3}\theta\,\dot{\theta}$:
$$ \mathbf{a}_Q = \frac{d\left(\ddot{\theta}\cos\theta + 2\dot{\theta}^2\sin\theta\right)}{\cos^3\theta}\,\mathbf{j}_0 $$

#### 3.2 Forces
##### (d) Forces on $P$
* **Weight:** $-mg\,\mathbf{k}_0$. **String tension:** along the segment $QP$, toward $Q$: $\mathbf{T} = -T\,\mathbf{e}_{QP}$ with $T \ge 0$. The edge acts on the string, not on $P$. **Inertia forces:** none.

#### 3.3 Equations of Motion
##### (f) Work of the tension (needed to eliminate $T$ from the equations)
* **Pedagogical Justification:** the tension acts along $-\mathbf{e}_{QP}$ on $P$, so its power is $-T\,\mathbf{e}_{QP}\cdot\mathbf{v}_P$. Differentiating $\mathbf{r}_P = \mathbf{r}_Q + \rho\,\mathbf{e}_{QP}$ (product rule) gives $\mathbf{v}_P = \mathbf{v}_Q + \dot{\rho}\,\mathbf{e}_{QP} + \rho\,\dot{\mathbf{e}}_{QP}$. Since $|\mathbf{e}_{QP}| = 1$, $\mathbf{e}_{QP}\cdot\dot{\mathbf{e}}_{QP} = \tfrac{1}{2}\frac{d}{dt}|\mathbf{e}_{QP}|^2 = 0$, so
$$ \mathbf{e}_{QP}\cdot\mathbf{v}_P = \mathbf{e}_{QP}\cdot\mathbf{v}_Q + \dot{\rho} $$
* $\mathbf{v}_Q$ has only a $\mathbf{j}_0$ component, so $\mathbf{e}_{QP}\cdot\mathbf{v}_Q = \sin\theta\,\dfrac{d\dot{\theta}}{\cos^2\theta}$. With the chain rule $\frac{d}{dt}\left(\frac{1}{\cos\theta}\right) = \frac{\sin\theta}{\cos^2\theta}\dot{\theta}$, the hanging length changes at the rate $\dot{\rho} = -\dfrac{d\dot{\theta}\sin\theta}{\cos^2\theta}$. Therefore
$$ \mathbf{e}_{QP}\cdot\mathbf{v}_P = \frac{d\dot{\theta}\sin\theta}{\cos^2\theta} - \frac{d\dot{\theta}\sin\theta}{\cos^2\theta} = 0 \implies \mathbf{T}\cdot\mathbf{v}_P = 0 $$
The tension does **no work** on $P$ ($W_T = 0$).
* **Consequence.** The identity holds for arbitrary $\dot{\theta}$ and $\dot{\phi}$, so $\mathbf{e}_{QP}$ is orthogonal to both tangent vectors $\partial\mathbf{r}_P/\partial\theta$ and $\partial\mathbf{r}_P/\partial\phi$. Projecting Newton's second law on these two vectors therefore removes the tension.

##### (e) Second-order equations for $\theta$ and $\phi$
* **Pedagogical Justification:** Newton's second law $m\mathbf{a}_P = -mg\,\mathbf{k}_0 + \mathbf{T}$ is projected on $\mathbf{t}_\theta$ and $\mathbf{t}_\phi$, which are orthogonal to $\mathbf{T}$ (part f), so the tension drops out: $m\,\mathbf{a}_P\cdot\mathbf{t}_q = -mg\,\mathbf{k}_0\cdot\mathbf{t}_q$ for $q = \theta, \phi$. The scalar products of the vectors of 3.1(c) are
$$ \mathbf{t}_{\theta\theta}\cdot\mathbf{t}_\theta = \ell^2\left(\cos\theta\sin\theta\sin^2\phi - \sin\theta\cos\theta + \sin\theta\cos\theta\cos^2\phi\right) = 0, \qquad \mathbf{t}_{\theta\phi}\cdot\mathbf{t}_\theta = \ell^2\sin^2\theta\left(\sin\phi\cos\phi - \sin\phi\cos\phi\right) = 0, \qquad \mathbf{t}_{\phi\phi}\cdot\mathbf{t}_\theta = \ell u\sin\theta $$
$$ \mathbf{t}_{\theta\theta}\cdot\mathbf{t}_\phi = 0, \qquad \mathbf{t}_{\theta\phi}\cdot\mathbf{t}_\phi = -\ell u\sin\theta, \qquad \mathbf{t}_{\phi\phi}\cdot\mathbf{t}_\phi = 0 $$
and the orthogonality of $\mathbf{t}_\theta$ and $\mathbf{t}_\phi$ gives
$$ \mathbf{a}_P\cdot\mathbf{t}_\theta = \ell^2\ddot{\theta} + \ell u\sin\theta\,\dot{\phi}^2, \qquad \mathbf{a}_P\cdot\mathbf{t}_\phi = u^2\ddot{\phi} - 2\ell u\sin\theta\,\dot{\theta}\dot{\phi} $$
while $-g\,\mathbf{k}_0\cdot\mathbf{t}_\theta = -g\ell\sin\theta\cos\phi$ and $-g\,\mathbf{k}_0\cdot\mathbf{t}_\phi = -gu\sin\phi$. Dividing the first projection by $\ell$ and the second by $u \gt 0$:
$$ \boxed{\ell\ddot{\theta} + \left(\ell\cos\theta - d\right)\sin\theta\,\dot{\phi}^2 + g\sin\theta\cos\phi = 0} $$
$$ \boxed{\left(\ell\cos\theta - d\right)\ddot{\phi} - 2\ell\sin\theta\,\dot{\theta}\dot{\phi} + g\sin\phi = 0} $$
* **Tension (afterwards).** Along $\mathbf{e}_{QP}$: $T = mg\cos\theta\cos\phi + m\,\mathbf{v}_P\cdot\dot{\mathbf{e}}_{QP}$, since $\mathbf{a}_P\cdot\mathbf{e}_{QP} = -\mathbf{v}_P\cdot\dot{\mathbf{e}}_{QP}$ (from $\mathbf{v}_P\cdot\mathbf{e}_{QP} = 0$).

#### 3.4 Integration and Answers
##### (g) Mechanical energy
* **Pedagogical Justification:** the plate is at rest (scleronomic constraint), the tension does no work (part f) and gravity is conservative, so the mechanical energy of $P$ is conserved:
$$ E = \tfrac{1}{2}mv_P^2 + mgz_P = \tfrac{1}{2}m\left[\ell^2\dot{\theta}^2 + \left(\ell\cos\theta - d\right)^2\dot{\phi}^2\right] - mg\left(\ell\cos\theta - d\right)\cos\phi = \text{const} $$
* **Initial value.** At $t = 0$, $|\mathbf{v}_P|^2 = \ell g$ and $\cos\theta = \cos\phi = \tfrac{1}{2}$, so $z_P(0) = -\left(\tfrac{\ell}{2} - d\right)\tfrac{1}{2}$:
$$ \boxed{E_0 = \tfrac{1}{2}m\ell g - mg\left(\frac{\ell}{2} - d\right)\frac{1}{2} = \frac{mg\ell}{4} + \frac{mgd}{2}} $$
It is a conserved quantity of the motion.

### Phase 4: Interpretation & Checks
* **Variable-length spherical pendulum:** the system acts as a spherical pendulum whose length changes as $Q$ slides along the edge.
* **Limit $d \to 0$:** the edge passes through $O$, so $Q = O$, $\rho = \ell$ and $\mathbf{e}_{QP}$ is the unit vector of a spherical pendulum of length $\ell$ with $\cos\gamma = \cos\theta\cos\phi$ the cosine of its angle with the downward vertical; the energy reduces to $E_0 = mg\ell/4$, equal to $\tfrac{1}{2}m\ell g - mg\ell\cos\theta\cos\phi$ at $\theta = \phi = \pi/3$.
* **Dimensional check:** $[\rho] = \text{m}$; $[mg\ell] = [mgd] = \text{J}$; $[u] = \text{m}$ and every term of the two equations of motion has units m/s$^2$.
* **Check against the official key:** the key of `Problems.pdf` answers (f): "No, the tension does not exert work; it is easy to prove it with $\mathbf{e}_r\cdot\mathbf{v}_P^0 = 0$", which is the result of 3.3. The rest is verified by independent derivation. Sympy confirms $\mathbf{e}_{QP}\cdot\mathbf{v}_P = 0$, $v_P^2 = \ell^2\dot{\theta}^2 + (\ell\cos\theta - d)^2\dot{\phi}^2$, $z_P = (d - \ell\cos\theta)\cos\phi$, the equivalence of the two projections with the equations above, and numerically $E_0 = mg\ell/4 + mgd/2 = 7.3575$ J for $m = 1$ kg, $\ell = 2$ m, $d = 0.5$ m, equal to $\tfrac{1}{2}m\ell g + mgz_P(0) = 9.81 - 2.4525$ J.

---

## 📌 Problem 48: Two Connected Particles, One on Paraboloid

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** two heavy particles $P$ and $Q$ of mass $m$ are joined by an inextensible massless cord of length $\ell$ that passes through a small hole at the origin $O$. $P$ moves without friction on the paraboloid $z = cR^2$ ($c \gt 0$, cylindrical coordinates $\{R, \theta, z\}$); $Q$ is restricted to hang along the vertical axis $Oz$. The frame $S_0$ is inertial, there is no friction, the cord is always taut and $Q$ never reaches $O$.
* **Constraints (a):** two free particles have $6$ coordinates, and there are $4$ independent constraints:
  - $P$ on the paraboloid: $z_P = cR^2$ (1; bilateral, since the statement says $P$ is constrained to stay on the paraboloid).
  - $Q$ on the axis: $x_Q = y_Q = 0$ (2).
  - Constant cord length: $|\overrightarrow{OP}| + |z_Q| = \ell$ (1; unilateral, $T \ge 0$).
* **Degrees of freedom:** $\text{CDOF} = 6 - 4 = 2$, with $(R, \theta)$.
* **Initial state (h):** $R(0) = 1/c$, $\theta(0) = 0$, $\dot{R}(0) = 0$, $\dot{\theta}(0) = d \ne 0$.
* **Parameters:** $m$, $c$ [m$^{-1}$], $\ell$, $g$, $d$ [s$^{-1}$].

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $S_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$.
* **Cylindrical basis:** $\mathcal{B}_1 = \{\mathbf{e}_R, \mathbf{e}_\theta, \mathbf{k}\}$ with $\mathbf{k} = \mathbf{k}_0$, the inertial basis rotated by $\theta(t)$ about $\mathbf{k}$:
$$ [{}_0 R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
Multiplying out, $RR^T$ has diagonal entries $\cos^2 + \sin^2 = 1$ of the rotation angle (and $1$) and off-diagonal entries $\pm(\cos\sin - \sin\cos) = 0$, so it is the identity.
with $\dot{\mathbf{e}}_R = \dot{\theta}\,\mathbf{e}_\theta$ and $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_R$.
* **Surface-adapted basis.** With $s = \sqrt{1 + 4c^2R^2}$, the unit meridian tangent is $\mathbf{e}_g = (\mathbf{e}_R + 2cR\,\mathbf{k})/s$, the unit normal pointing into the bowl is $\hat{\mathbf{n}} = (-2cR\,\mathbf{e}_R + \mathbf{k})/s$, and $\mathbf{e}_g\times\mathbf{e}_\theta = \hat{\mathbf{n}}$, so
$$ [{}_1 R_2] = \begin{pmatrix} 1/s & 0 & -2cR/s \\ 0 & 1 & 0 \\ 2cR/s & 0 & 1/s \end{pmatrix}, \qquad \det[{}_1 R_2] = \frac{1 + 4c^2R^2}{s^2} = 1, \qquad [{}_1 R_2][{}_1 R_2]^T = I $$

### Phase 3: Derivation

#### 3.1 Kinematics
##### (b) Position, velocity and acceleration
* **Pedagogical Justification:** the cord runs straight from $O$ to $P$, so the length of its part on the side of $P$ is $\rho(R) = |\mathbf{r}_P| = R\sqrt{1 + c^2R^2}$, and $Q$ hangs at the depth $\ell - \rho$:
$$ \mathbf{r}_P = R\,\mathbf{e}_R + cR^2\,\mathbf{k}, \qquad \mathbf{r}_Q = -\left(\ell - \rho(R)\right)\mathbf{k} $$
* **Derivatives of $\rho$** (chain rule, with $w = \sqrt{1 + c^2R^2}$): $\rho' = \dfrac{d\rho}{dR} = w + \dfrac{c^2R^2}{w} = \dfrac{1 + 2c^2R^2}{w}$ and $\rho'' = \dfrac{c^2R\left(3 + 2c^2R^2\right)}{w^3}$.
* **Particle $P$** (product rule and Poisson):
$$ \mathbf{v}_P = \dot{R}\,\mathbf{e}_R + R\dot{\theta}\,\mathbf{e}_\theta + 2cR\dot{R}\,\mathbf{k}, \qquad v_P^2 = \dot{R}^2\left(1 + 4c^2R^2\right) + R^2\dot{\theta}^2 $$
$$ \mathbf{a}_P = \left(\ddot{R} - R\dot{\theta}^2\right)\mathbf{e}_R + \left(R\ddot{\theta} + 2\dot{R}\dot{\theta}\right)\mathbf{e}_\theta + 2c\left(\dot{R}^2 + R\ddot{R}\right)\mathbf{k} $$
* **Particle $Q$:** $\mathbf{v}_Q = \rho'\dot{R}\,\mathbf{k}$ and $\mathbf{a}_Q = \left(\rho'\ddot{R} + \rho''\dot{R}^2\right)\mathbf{k}$.

##### (c) Tangent and normal vectors to the paraboloid
$$ \mathbf{t}_R = \frac{\partial\mathbf{r}_P}{\partial R} = \mathbf{e}_R + 2cR\,\mathbf{k}, \qquad \mathbf{t}_\theta = \frac{\partial\mathbf{r}_P}{\partial\theta} = R\,\mathbf{e}_\theta, \qquad \mathbf{n} = \mathbf{t}_R\times\mathbf{t}_\theta = R\left(-2cR\,\mathbf{e}_R + \mathbf{k}\right) $$

#### 3.2 Forces
##### (d) Forces on $P$ and $Q$
* **On $P$:** its weight $-mg\,\mathbf{k}$; the reaction of the smooth paraboloid $\mathbf{N} = N\,\hat{\mathbf{n}}$ (unknown magnitude $N$, normal to the surface); and the tension of the cord, directed toward the hole, $\mathbf{T}_P = -T\,\dfrac{\mathbf{r}_P}{|\mathbf{r}_P|}$.
* **On $Q$:** its weight $-mg\,\mathbf{k}$, the tension $\mathbf{T}_Q = +T\,\mathbf{k}$ (same cord, smooth hole), and the horizontal reaction $\mathbf{R}_Q$ of the vertical guide.
* **Inertia forces:** none ($S_0$ is inertial).

#### 3.3 Equations of Motion
##### (f) Two second-order equations for $R$ and $\theta$
* **Pedagogical Justification:** the unknowns are $R$, $\theta$, $T$, $N$ and the two components of $\mathbf{R}_Q$, i.e. $6$ unknowns, and Newton's second law for $P$ and $Q$ gives $6$ scalar equations. Projecting the equation of $P$ on the tangent vectors removes the normal reaction $N$, and the equation of $Q$ gives $T$ and $\mathbf{R}_Q = \mathbf{0}$ (since $\mathbf{a}_Q \parallel \mathbf{k}$):
$$ Q,\ \mathbf{k}: \; m\left(\rho'\ddot{R} + \rho''\dot{R}^2\right) = T - mg \implies T = m\left(g + \rho'\ddot{R} + \rho''\dot{R}^2\right) $$
* **Equation for $\theta$.** Projecting on $\mathbf{e}_\theta$ (no component of the reaction, of gravity or of the tension, which lies in the meridian plane): $m\left(R\ddot{\theta} + 2\dot{R}\dot{\theta}\right) = 0$, i.e. $\dfrac{m}{R}\dfrac{d}{dt}\left(R^2\dot{\theta}\right) = 0$.
* **Equation for $R$.** Projecting on $\mathbf{t}_R$: the tension component is $-T\,\dfrac{\mathbf{r}_P}{|\mathbf{r}_P|}\cdot\mathbf{t}_R = -T\rho'$ (because $\dfrac{\mathbf{r}_P}{|\mathbf{r}_P|}\cdot\mathbf{t}_R = \dfrac{R + 2c^2R^3}{R w} = \rho'$) and the weight gives $-mg\,\mathbf{k}\cdot\mathbf{t}_R = -2cmgR$:
$$ m\left[\ddot{R} - R\dot{\theta}^2 + 2cR\cdot 2c\left(\dot{R}^2 + R\ddot{R}\right)\right] = -2cmgR - T\rho' $$
Substituting $T$ from the equation of $Q$:
$$ \boxed{\left(1 + 4c^2R^2 + \rho'^2\right)\ddot{R} + \left(4c^2R + \rho'\rho''\right)\dot{R}^2 - R\dot{\theta}^2 + 2cgR + g\rho' = 0}, \qquad \boxed{R\ddot{\theta} + 2\dot{R}\dot{\theta} = 0} $$
with $\rho'^2 = \dfrac{(1 + 2c^2R^2)^2}{1 + c^2R^2}$.

#### 3.4 Integration and Answers
##### (e) Condition for the cord to remain in tension
* **Pedagogical Justification:** the cord can only pull, so $T \gt 0$ at all times. From the equation of $Q$:
$$ T = m\left(g + \ddot{z}_Q\right) \gt 0 \iff \ddot{z}_Q = \rho'\ddot{R} + \rho''\dot{R}^2 \gt -g, \qquad \text{i.e.} \quad \frac{1 + 2c^2R^2}{\sqrt{1 + c^2R^2}}\ddot{R} + \frac{c^2R\left(3 + 2c^2R^2\right)}{\left(1 + c^2R^2\right)^{3/2}}\dot{R}^2 \gt -g $$

##### (g) Two scalar conservation laws (first integrals)
* **Azimuthal integral (first integral of the $\theta$ equation).** From the equation for $\theta$ and $a_\theta = \frac{1}{R}\frac{d}{dt}\left(R^2\dot{\theta}\right)$ (product rule):
$$ \boxed{R^2\dot{\theta} = \text{const} = R(0)^2\,d = \frac{d}{c^2}} \implies \dot{\theta} = \frac{d}{c^2R^2} $$
* **Mechanical energy.** The reaction of the paraboloid does no work ($\mathbf{N}\cdot\mathbf{v}_P = 0$), the tension does the work $-T\rho'\dot{R}$ on $P$ and $+T\rho'\dot{R}$ on $Q$, which cancel (inextensible cord, smooth hole), the guide reaction is perpendicular to $\mathbf{v}_Q$, and gravity is conservative. With $V = mg\left(cR^2 + z_Q\right) = mg\left[cR^2 + \rho - \ell\right]$:
$$ E = \tfrac{1}{2}m\left[\left(1 + 4c^2R^2 + \rho'^2\right)\dot{R}^2 + R^2\dot{\theta}^2\right] + mg\left(cR^2 + \rho\right) - mg\ell = \text{const} $$

##### (h) Equation $f(R) = 0$ for the extreme values of $R$
* **Pedagogical Justification:** at the extremes $\dot{R} = 0$, so only $\tfrac{1}{2}mR^2\dot{\theta}^2$ remains of the kinetic energy, with $R^2\dot{\theta}^2 = d^2/(c^4R^2)$ from the azimuthal integral. The constant $-mg\ell$ cancels in $E - E_0$. At $R(0) = 1/c$: $\rho = \sqrt{2}/c$ and $R^2\dot{\theta}^2 = d^2/c^2$. Per unit mass:
$$ \boxed{f(R) = \frac{d^2}{2c^4R^2} + g\left(cR^2 + R\sqrt{1 + c^2R^2}\right) - \frac{d^2}{2c^2} - \frac{(1 + \sqrt{2})\,g}{c} = 0} $$
* The allowed radii are those with $f(R) \le 0$ (so that $\dot{R}^2 \ge 0$), and $R = 1/c$ is a root.

### Phase 4: Interpretation & Checks
* **Limit $c \to 0$ (flat plane):** $\rho = R$, $\rho' = 1$, $\rho'' = 0$, and the equation for $R$ becomes $2\ddot{R} - R\dot{\theta}^2 + g = 0$, that of two equal particles joined through a hole in a horizontal plane.
* **Bounded precessing motion:** the particle moves between two parallel circles $R_{\min}$ and $R_{\max}$, with the azimuthal angle monotonic ($\dot{\theta} = d/(c^2R^2)$ has the sign of $d$).
* **Dimensional check:** $[c] = \text{m}^{-1}$, $[d] = \text{s}^{-1}$; $[cR^2] = [\rho] = \text{m}$ and $cR$ is dimensionless; every term of $f$ has units m$^2$/s$^2$.
* **Check against the official key:** `Problems.pdf` has no entry for Problem 48 in its solution keys, so the results are verified by independent derivation. Sympy confirms $\rho'$, $\rho''$, the projections of $\mathbf{a}_P$ on $\mathbf{t}_R$ and $\mathbf{e}_\theta$, and numerical integration of the two equations of (f) ($c = d = g = 1$) conserves $E$ to $2\times 10^{-12}$, keeps $T/m \ge 0.303$ and bounds $R$ between $0.482807$ and $1$, the roots of $f$ ($f(0.482807) = 0$ and $f(1) = 0$; $f \lt 0$ between them).

---

## 📌 Problem 50: Double Pendulum

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a double pendulum of two heavy particles $P$ and $Q$ of mass $m$ joined to $O$ and to each other by two rigid massless bars of length $\ell$. The motion is planar (the figure and the angles $\theta$ and $\phi$ describe a plane). The angle $\theta$ is that of the bar $OP$ with the downward vertical and $\phi$ that of the bar $PQ$ with the downward vertical.
* **Constraints:** two particles in the plane have $4$ coordinates; the rigid bars give $|OP| = \ell$ and $|PQ| = \ell$ (holonomic, scleronomic, bilateral). $\text{CDOF} = 4 - 2 = 2$, with $(\theta, \phi)$.
* **Parameters:** $m$, $\ell$, $g$.

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $S_0 = \{O; \mathbf{i}, \mathbf{j}\}$, with $\mathbf{i}$ horizontal to the right and $\mathbf{j}$ vertical upward (the horizontal axis is $Ox$).
* **Bar bases** (rotations about the axis perpendicular to the plane; check below):
$$ \mathbf{e}_P = \sin\theta\,\mathbf{i} - \cos\theta\,\mathbf{j}, \quad \mathbf{e}_\theta = \cos\theta\,\mathbf{i} + \sin\theta\,\mathbf{j}, \qquad \mathbf{e}_Q = \sin\phi\,\mathbf{i} - \cos\phi\,\mathbf{j}, \quad \mathbf{e}_\phi = \cos\phi\,\mathbf{i} + \sin\phi\,\mathbf{j} $$
In $\{\mathbf{i}, \mathbf{j}\}$ the matrix with columns $\mathbf{e}_P, \mathbf{e}_\theta$ is $\begin{pmatrix}\sin\theta & \cos\theta\\ -\cos\theta & \sin\theta\end{pmatrix}$, with $\det = \sin^2\theta + \cos^2\theta = 1$ and orthonormal columns ($\sin^2\theta + \cos^2\theta = 1$, $\sin\theta\cos\theta - \cos\theta\sin\theta = 0$), so $RR^T = I$; the same holds with $\phi$ for $\mathbf{e}_Q, \mathbf{e}_\phi$.
where $\mathbf{e}_P$ points from $O$ to $P$ and $\mathbf{e}_Q$ from $P$ to $Q$. Their derivatives are $\dot{\mathbf{e}}_P = \dot{\theta}\,\mathbf{e}_\theta$, $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_P$, and the same with $\phi$.
* **Scalar products needed:** $\mathbf{j}\cdot\mathbf{e}_P = -\cos\theta$, $\mathbf{j}\cdot\mathbf{e}_\theta = \sin\theta$, $\mathbf{j}\cdot\mathbf{e}_Q = -\cos\phi$, $\mathbf{j}\cdot\mathbf{e}_\phi = \sin\phi$, and
$$ \mathbf{e}_P\cdot\mathbf{e}_Q = \cos(\theta - \phi), \quad \mathbf{e}_\theta\cdot\mathbf{e}_Q = \sin(\phi - \theta), \quad \mathbf{e}_\theta\cdot\mathbf{e}_\phi = \cos(\theta - \phi), \quad \mathbf{e}_P\cdot\mathbf{e}_\phi = \sin(\theta - \phi) $$

### Phase 3: Derivation

#### 3.1 Kinematics
##### (a) Position, velocity and acceleration
* **Pedagogical Justification:** the positions are sums of the two bar vectors, $\mathbf{r}_P = \ell\,\mathbf{e}_P$ and $\mathbf{r}_Q = \ell\,\mathbf{e}_P + \ell\,\mathbf{e}_Q$; the derivatives use Poisson's formula:
$$ \mathbf{r}_P = \ell\sin\theta\,\mathbf{i} - \ell\cos\theta\,\mathbf{j}, \qquad \mathbf{r}_Q = \ell\left(\sin\theta + \sin\phi\right)\mathbf{i} - \ell\left(\cos\theta + \cos\phi\right)\mathbf{j} $$
$$ \mathbf{v}_P = \ell\dot{\theta}\,\mathbf{e}_\theta, \qquad \mathbf{v}_Q = \ell\dot{\theta}\,\mathbf{e}_\theta + \ell\dot{\phi}\,\mathbf{e}_\phi, \qquad v_P^2 = \ell^2\dot{\theta}^2, \quad v_Q^2 = \ell^2\left[\dot{\theta}^2 + \dot{\phi}^2 + 2\dot{\theta}\dot{\phi}\cos(\theta - \phi)\right] $$
$$ \mathbf{a}_P = \ell\left(\ddot{\theta}\,\mathbf{e}_\theta - \dot{\theta}^2\,\mathbf{e}_P\right), \qquad \mathbf{a}_Q = \mathbf{a}_P + \ell\left(\ddot{\phi}\,\mathbf{e}_\phi - \dot{\phi}^2\,\mathbf{e}_Q\right) $$

#### 3.2 Forces
##### (b) Forces on $P$ and $Q$
* The bars are massless and rigid, so each transmits a force along its axis: $T_1$ in $OP$ and $T_2$ in $PQ$ (negative values mean compression).
* **On $P$:** its weight $-mg\,\mathbf{j}$, the pull $-T_1\,\mathbf{e}_P$ of the bar $OP$ and the pull $+T_2\,\mathbf{e}_Q$ of the bar $PQ$. **On $Q$:** its weight $-mg\,\mathbf{j}$ and the pull $-T_2\,\mathbf{e}_Q$ of the bar $PQ$ (action and reaction). **Inertia forces:** none.

#### 3.3 Equations of Motion
##### (c) Equations of motion for $\theta$ and $\phi$
* **Pedagogical Justification:** Newton's second law, $m\mathbf{a}_P = -mg\,\mathbf{j} - T_1\mathbf{e}_P + T_2\mathbf{e}_Q$ and $m\mathbf{a}_Q = -mg\,\mathbf{j} - T_2\mathbf{e}_Q$, gives four scalar equations for the four unknowns $\theta, \phi, T_1, T_2$. The two tensions are removed by choosing the projection directions.
* **Equation for $\phi$.** Project the equation of $Q$ on $\mathbf{e}_\phi$, which is orthogonal to $\mathbf{e}_Q$ and removes $T_2$. With $\mathbf{a}_P\cdot\mathbf{e}_\phi = \ell\left[\ddot{\theta}\cos(\theta - \phi) - \dot{\theta}^2\sin(\theta - \phi)\right]$ and $\ell\left(\ddot{\phi}\,\mathbf{e}_\phi - \dot{\phi}^2\mathbf{e}_Q\right)\cdot\mathbf{e}_\phi = \ell\ddot{\phi}$:
$$ \boxed{\ddot{\phi} + \ddot{\theta}\cos(\theta - \phi) - \dot{\theta}^2\sin(\theta - \phi) + \frac{g}{\ell}\sin\phi = 0} $$
* **Equation for $\theta$.** Add the two equations of motion so that $T_2\,\mathbf{e}_Q$ cancels, and project on $\mathbf{e}_\theta$, which is orthogonal to $\mathbf{e}_P$ and removes $T_1$. The right-hand side is $-2mg\,\mathbf{j}\cdot\mathbf{e}_\theta = -2mg\sin\theta$, and the left-hand side is $m\left(\mathbf{a}_P + \mathbf{a}_Q\right)\cdot\mathbf{e}_\theta$ with $\mathbf{a}_P\cdot\mathbf{e}_\theta = \ell\ddot{\theta}$ and $\mathbf{a}_Q\cdot\mathbf{e}_\theta = \ell\ddot{\theta} + \ell\ddot{\phi}\cos(\theta - \phi) + \ell\dot{\phi}^2\sin(\theta - \phi)$:
$$ \boxed{2\ddot{\theta} + \ddot{\phi}\cos(\theta - \phi) + \dot{\phi}^2\sin(\theta - \phi) + \frac{2g}{\ell}\sin\theta = 0} $$
* **Tensions (afterwards).** Projecting on the bar directions,
$$ T_2 = mg\cos\phi - m\ell\left[\ddot{\theta}\sin(\phi - \theta) - \dot{\theta}^2\cos(\theta - \phi) - \dot{\phi}^2\right], \qquad T_1 = mg\cos\theta + m\ell\dot{\theta}^2 + T_2\cos(\theta - \phi) $$
At rest at $\theta = \phi = 0$: $T_2 = mg$ and $T_1 = 2mg$, the static tensions of the hanging chain.

#### 3.4 Integration and Answers
##### (d) Conservation law
* **Pedagogical Justification:** the bar forces do no net work. Bar $OP$ acts on $P$ with $-T_1\mathbf{e}_P$, whose power is $-T_1\mathbf{e}_P\cdot\ell\dot{\theta}\,\mathbf{e}_\theta = 0$. Bar $PQ$ acts with $+T_2\mathbf{e}_Q$ on $P$ and $-T_2\mathbf{e}_Q$ on $Q$, total power $-T_2\mathbf{e}_Q\cdot(\mathbf{v}_Q - \mathbf{v}_P) = -T_2\mathbf{e}_Q\cdot\ell\dot{\phi}\,\mathbf{e}_\phi = 0$. Gravity is conservative, so the mechanical energy is constant:
$$ E = \tfrac{1}{2}m\ell^2\left[2\dot{\theta}^2 + \dot{\phi}^2 + 2\dot{\theta}\dot{\phi}\cos(\theta - \phi)\right] - mg\ell\left(2\cos\theta + \cos\phi\right) = \text{const} $$

##### (e) Will $Q$ ever cross the $Ox$ axis?
* **Pedagogical Justification:** with $\theta(0) = \phi(0) = \pi/4$ and $\dot{\theta}(0) = \dot{\phi}(0) = 0$, the initial energy is purely potential:
$$ E_0 = -mg\ell\left(2\cos\frac{\pi}{4} + \cos\frac{\pi}{4}\right) = -\frac{3\sqrt{2}}{2}mg\ell \approx -2.121\,mg\ell $$
* $Q$ is on the axis when $y_Q = -\ell\left(\cos\theta + \cos\phi\right) = 0$, i.e. $\cos\phi = -\cos\theta$. There the potential energy is $V = -mg\ell\left(2\cos\theta + \cos\phi\right) = -mg\ell\cos\theta \ge -mg\ell$. Since the kinetic energy is non-negative, $E \ge V$ at any point of the motion, so reaching the axis would require $E_0 \ge -mg\ell$. But $E_0 = -2.121\,mg\ell \lt -mg\ell$.
* **Answer:** $Q$ can **never** cross the $Ox$ axis (it would need a negative kinetic energy).

##### (f) Additional constraint $\phi = 2\theta$: small-angle natural frequency
* **Pedagogical Justification:** with the constraint $\phi = 2\theta$ the system has one degree of freedom. The additional ideal constraint (scleronomic, no friction) does no work, so the energy is still conserved. For small angles, $\dot{\phi} = 2\dot{\theta}$, $\cos(\theta - \phi) = \cos\theta \approx 1$ and $\cos u \approx 1 - u^2/2$:
$$ K = \tfrac{1}{2}m\ell^2\left[2 + 4 + 4\right]\dot{\theta}^2 = 5m\ell^2\dot{\theta}^2, \qquad V = -mg\ell\left[2\left(1 - \tfrac{\theta^2}{2}\right) + \left(1 - 2\theta^2\right)\right] = -3mg\ell + 3mg\ell\theta^2 $$
$$ E = 5m\ell^2\dot{\theta}^2 + 3mg\ell\theta^2 + \text{const} \implies E' = 10m\ell^2\dot{\theta}\ddot{\theta} + 6mg\ell\theta\dot{\theta} = 0 \implies \ddot{\theta} + \frac{3g}{5\ell}\theta = 0 $$
* **Comparison with the hint.** The energy of an ideal oscillator is $\tfrac{1}{2}m_{\text{eq}}\left(\dot{x}^2 + \omega_0^2x^2\right)$; here $\tfrac{1}{2}(10m\ell^2)\left(\dot{\theta}^2 + \dfrac{3g}{5\ell}\theta^2\right)$, so
$$ \boxed{\omega_0 = \sqrt{\frac{3g}{5\ell}}} $$

### Phase 4: Interpretation & Checks
* **Dimensional check:** $[g/\ell] = \text{s}^{-2}$, so $[\omega_0] = \text{s}^{-1}$; $[T_1] = [T_2] = [mg] = \text{N}$.
* **Comparison (not a limit of this system):** for a single pendulum the frequency would be $\sqrt{g/\ell}$; the constrained double pendulum oscillates more slowly ($\omega_0^2 = 0.6\,g/\ell$) because the second mass adds inertia faster than restoring torque.
* **Check against the official key:** `Problems.pdf` has no entry for Problem 50 in its solution keys, so the results are verified by independent derivation. Sympy confirms that the Euler-Lagrange equations of $K - V$ are $m\ell^2$ times the two equations of (c), and gives $K \approx 5m\ell^2\dot{\theta}^2$ and $V''(0) = 6mg\ell$ for the constrained case.
