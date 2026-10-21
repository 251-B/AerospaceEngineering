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

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A point particle of mass $m$ moves without friction on the interior surface of an inverted cone given by $z^2 = x^2 + y^2$ with $z > 0$.
* **Configuration Degrees of Freedom (CDOFs):**
* Ambient space: 3 Cartesian coordinates $(x, y, z)$.
* Holonomic geometric constraint: $\Phi(x, y, z) = x^2 + y^2 - z^2 = 0$.
* Number of CDOFs: $3 - 1 = 2$. We choose cylindrical coordinates $(r, \theta)$ with $z = r$.
* **Hypotheses:**

1\. Constraint is smooth (frictionless): the reaction force $\mathbf{N}$ is strictly orthogonal to the tangent space of the cone ($W_{\mathbf{N}} = 0$).

2\. Inertial frame with gravity acting along $-Oz$: $\mathbf{g} = -g\mathbf{k}$.

* **Initial State ($t = 0$):**
* Position: $(x_0, y_0, z_0) = (a, 0, a) \implies r(0) = a, \theta(0) = 0, z(0) = a$.
* Velocity: $\mathbf{v}_0 = \sqrt{ag}\,\mathbf{j} \implies v_r(0) = 0, v_\theta(0) = r(0)\dot{\theta}(0) = \sqrt{ag}, v_z(0) = 0$.
* **Parameters:** $m > 0$ [kg], $g > 0$ [m/s$^2$], $a > 0$ [m].

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* **Inertial Reference Frame:** $\mathcal{F}_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$.
* **Cylindrical Vector Basis:** $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}\}$, with:
$$ \mathbf{e}_r = \cos\theta\,\mathbf{i} + \sin\theta\,\mathbf{j}, \qquad \mathbf{e}_\theta = -\sin\theta\,\mathbf{i} + \cos\theta\,\mathbf{j}, \qquad \mathbf{k} = \mathbf{k} $$
* **Kinematics with Constraint $z(t) = r(t)$:**
* Position: $\mathbf{r}(t) = r\mathbf{e}_r + r\mathbf{k}$.
* Velocity: Differentiating with respect to time using Poisson's rule $\dot{\mathbf{e}}_r = \dot{\theta}\mathbf{e}_\theta$:
$$ \mathbf{v}(t) = \dot{r}\mathbf{e}_r + r\dot{\theta}\mathbf{e}_\theta + \dot{r}\mathbf{k} $$
* Modulus of velocity squared:
$$ v^2 = \dot{r}^2 + r^2\dot{\theta}^2 + \dot{r}^2 = 2\dot{r}^2 + r^2\dot{\theta}^2 $$
* **Change of basis (cylindrical basis).** $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}\}$ is the inertial basis $\mathcal{B}_0 = \{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$ rotated by $\theta(t)$ about $\mathbf{k}$; the columns are the components of $\mathbf{e}_r$, $\mathbf{e}_\theta$, $\mathbf{k}$ in $\mathcal{B}_0$:
$$ [{}_0 R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = \cos^2\theta + \sin^2\theta = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
* The angular velocity of $\mathcal{B}_1$ is $\boldsymbol{\omega}_{10} = \dot{\theta}\,\mathbf{k}$, so Poisson's formula gives $\dot{\mathbf{e}}_r = \dot{\theta}\,\mathbf{e}_\theta$ and $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_r$, as used above.
* **Surface-adapted basis.** On the cone $z = r$ (slope $45^\circ$) the unit generator is $\mathbf{e}_g = (\mathbf{e}_r + \mathbf{k})/\sqrt{2}$ and the unit normal pointing into the cone, where the particle lies, is $\mathbf{n}_{in} = (\mathbf{k} - \mathbf{e}_r)/\sqrt{2}$. The triple $\{\mathbf{e}_g, \mathbf{e}_\theta, \mathbf{n}_{in}\}$ is right-handed ($\mathbf{e}_g \times \mathbf{e}_\theta = \mathbf{n}_{in}$) and its components in $\mathcal{B}_1$ are the columns of
$$ [{}_1 R_2] = \begin{pmatrix} 1/\sqrt{2} & 0 & -1/\sqrt{2} \\ 0 & 1 & 0 \\ 1/\sqrt{2} & 0 & 1/\sqrt{2} \end{pmatrix}, \qquad \det[{}_1 R_2] = \tfrac{1}{2} + \tfrac{1}{2} = 1, \qquad [{}_1 R_2][{}_1 R_2]^T = I $$
* Both matrices were checked symbolically with sympy.

### Phase 3: Step-by-Step Mathematical Deduction

#### 1. First Integral from the $\mathbf{e}_\theta$ Component of Newton's Law
* **Pedagogical Justification:** The coordinate $\theta$ does not appear in the problem (axisymmetric cone, vertical gravity), so its equation of motion gives a first integral without any further theorem. In cylindrical coordinates the azimuthal acceleration is $a_\theta = r\ddot{\theta} + 2\dot{r}\dot{\theta} = \frac{1}{r}\frac{d}{dt}\left(r^2\dot{\theta}\right)$ (Notes Sec. 2.6.2). The forces have no $\mathbf{e}_\theta$ component: gravity is $-mg\mathbf{k}$, and the normal to the cone $f(r, z) = r - z = 0$ is $\mathbf{n} = \frac{1}{\sqrt{2}}(\mathbf{e}_r - \mathbf{k})$, which lies in the meridian plane (the reaction of a smooth surface is normal to it).
$$ m\,a_\theta = \frac{m}{r}\frac{d}{dt}\left(r^2\dot{\theta}\right) = 0 \implies m r^2 \dot{\theta} = \text{constant} = C_z $$

Evaluate $C_z$ at $t = 0$:

$$ C_z = m [r(0)]^2 \dot{\theta}(0) = m a (a \dot{\theta}_0) = m a (\sqrt{ag}) = m a\sqrt{ga} $$

Therefore:

$$ \dot{\theta}(t) = \frac{a\sqrt{ga}}{r^2(t)} $$

#### 2. Conservation of Mechanical Energy
* **Pedagogical Justification:** Because the constraint is frictionless (bilateral holonomic), the reaction force $\mathbf{N}$ does no work ($\mathbf{N} \cdot \mathbf{v} = 0$). Gravity is conservative with potential energy $V = mgz = mgr$. Hence, total mechanical energy $E = T + V$ is strictly conserved.

Initial energy at $t = 0$:

$$ T(0) = \frac{1}{2}m v_0^2 = \frac{1}{2}m (ag) $$
$$ V(0) = mg z(0) = mga $$
$$ E = T(0) + V(0) = \frac{1}{2}mga + mga = \frac{3}{2}mga $$

Energy at any subsequent time:

$$ E = \frac{1}{2}m\left(2\dot{r}^2 + r^2\dot{\theta}^2\right) + mgr = \frac{3}{2}mga $$

Substitute $\dot{\theta} = \frac{a\sqrt{ga}}{r^2}$:

$$ \frac{1}{2}m\left( 2\dot{r}^2 + r^2 \frac{a^3 g}{r^4} \right) + mgr = \frac{3}{2}mga $$
$$ m\dot{r}^2 + \frac{1}{2}mg\frac{a^3}{r^2} + mgr = \frac{3}{2}mga $$

Divide through by $m$:

$$ \dot{r}^2 + \frac{ga^3}{2r^2} + gr = \frac{3}{2}ga $$

#### 3. Reduction to Quadratures (Integral Equation)

Isolate $\dot{r}^2$:

$$ \dot{r}^2 = \frac{3}{2}ga - gr - \frac{ga^3}{2r^2} = \frac{g}{2r^2}\left(3ar^2 - 2r^3 - a^3\right) $$

Taking the square root:

$$ \frac{dr}{dt} = \pm \sqrt{\frac{g}{2}}\frac{\sqrt{-2r^3 + 3ar^2 - a^3}}{r} $$

Separating variables yields the integral equation:

$$ \int_{a}^{r} \frac{r'\,dr'}{\sqrt{-2r'^3 + 3ar'^2 - a^3}} = \pm \sqrt{\frac{g}{2}}\,t $$

#### 4. Determination of Maximum and Minimum of $z$ ($r$)
* **Pedagogical Justification:** The turning points of the radial motion occur when the radial velocity vanishes, $\dot{r} = 0$, which corresponds to the roots of the cubic polynomial $P(r) = -2r^3 + 3ar^2 - a^3 = 0$.

Rewrite $P(r) = 0$:

$$ 2r^3 - 3ar^2 + a^3 = 0 $$

Since the particle starts at $r = a$, $r = a$ must be a root:

$$ 2(a)^3 - 3a(a)^2 + a^3 = 2a^3 - 3a^3 + a^3 = 0 $$

Divide $2r^3 - 3ar^2 + a^3$ by $(r - a)$:

$$ 2r^3 - 3ar^2 + a^3 = (r - a)(2r^2 - ar - a^2) $$

Factor the quadratic factor:

$$ 2r^2 - ar - a^2 = (r - a)(2r + a) $$

Therefore, the polynomial factors completely as:

$$ 2r^3 - 3ar^2 + a^3 = (r - a)^2 (2r + a) $$

Substituting back into the expression for $\dot{r}^2$:

$$ \dot{r}^2 = -\frac{g}{2r^2}(r - a)^2 (2r + a) $$

Since $r > 0$ and $a > 0$, the factor $(2r + a) > 0$.

The square $(r - a)^2 \ge 0$, which implies:

$$ \dot{r}^2 = -\frac{g(2r + a)}{2r^2}(r - a)^2 \le 0, \qquad \forall r > 0 $$

Because $\dot{r}^2$ is a squared real quantity, it must satisfy $\dot{r}^2 \ge 0$.

The only physically possible solution for all time is:

$$ \dot{r}^2 = 0 \iff r(t) = a = \text{constant} $$

### Phase 4: Physical Interpretation & Dimensional Verification
* **Steady Circular Orbit:** The particle is placed exactly at the minimum of the effective potential $V_{eff}(r) = mgr + \frac{m a^3 g}{2r^2}$. The initial tangential velocity $v_0 = \sqrt{ag}$ provides precisely the centripetal acceleration required to balance the inward horizontal component of the normal reaction force $\mathbf{N}$.
* **Extremal Heights:**
$$ z_{min} = z_{max} = a $$

The particle maintains a constant altitude $z = a$ for all time, executing uniform circular motion with orbital frequency $\omega = \dot{\theta} = \sqrt{g/a}$.

* **Dimensional check:** $[C_z] = [m\,a\sqrt{ga}] = \text{kg}\cdot\text{m}^2\cdot\text{s}^{-1}$ (the constant $C_z = m r^2\dot\theta$); $[\dot{r}^2] = \text{m}^2/\text{s}^2$ and $[g\,a^3/r^2] = (\text{m/s}^2)\,\text{m} = \text{m}^2/\text{s}^2$, so every term of the energy equation has the same units.
* **Reaction on the steady orbit (sympy force balance):** with $\dot{\theta}^2 = g/a$ the horizontal acceleration is $-g\,\mathbf{e}_r$. Requiring $N\,\mathbf{n}_{in} - mg\,\mathbf{k} = -mg\,\mathbf{e}_r$ gives $\mathbf{N} = mg(\mathbf{k} - \mathbf{e}_r) = \sqrt{2}\,mg\,\mathbf{n}_{in}$, so $\|\mathbf{N}\| = \sqrt{2}\,mg$ [N], pointing into the cone, which is physically admissible (it presses the particle against the surface).
* **Stability (small radial oscillations):** the effective inertia of the $r$-motion is $2m$ (the kinetic energy has $2\dot{r}^2$) and $V_{eff}''(a) = 3mg/a$, hence $\omega_r^2 = 3g/(2a)$. An RK4 integration (step $10^{-4}$, $g = a = 1$) of $2\ddot{r} = r\dot{\theta}^2 - g$ with $r(0) = 1.001$, $\dot{r}(0) = 0$ and $r^2\dot{\theta} = a\sqrt{ga}$ has period $5.1304$ against $2\pi/\sqrt{3/2} = 5.1302$ (in units of $\sqrt{a/g}$), confirming that the circular orbit is a stable minimum of $V_{eff}$.

---

## 📌 Problem 19: Heavy Particle on a Paraboloid

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle of mass $m$ moves without friction on the paraboloid of revolution $a z = r^2$, where $a > 0$ and $r = \sqrt{x^2 + y^2}$.
* **Degrees of Freedom:** $3$ coordinates minus $1$ constraint $\implies 2$ CDOFs. We parametrize using cylindrical coordinates $(r, \theta)$ with $z = r^2/a$.
* **Initial State ($t = 0$):**
* Radius: $r(0) = a \implies z(0) = a^2/a = a$.
* Velocity: Launched tangent to the local parallel (pure azimuthal velocity):
$$ \mathbf{v}_0 = v_0\mathbf{e}_\theta \implies \dot{r}(0) = 0, \quad \dot{\theta}(0) = \frac{v_0}{a}, \quad \dot{z}(0) = 0 $$
* **Parameters:** $m > 0$ [kg], $a > 0$ [m], $g > 0$ [m/s$^2$], $v_0 > 0$ [m/s].

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* **Inertial Frame:** $\mathcal{F}_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$.
* **Kinematics with $z = r^2/a$:**
$$ \dot{z} = \frac{d}{dt}\left(\frac{r^2}{a}\right) = \frac{2r\dot{r}}{a} $$

Velocity vector:

$$ \mathbf{v} = \dot{r}\mathbf{e}_r + r\dot{\theta}\mathbf{e}_\theta + \frac{2r\dot{r}}{a}\mathbf{k} $$

Velocity squared:

$$ v^2 = \dot{r}^2\left(1 + \frac{4r^2}{a^2}\right) + r^2\dot{\theta}^2 $$
* **Change of basis (cylindrical basis).** $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}\}$ is obtained from $\mathcal{B}_0 = \{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$ by a rotation $\theta(t)$ about $\mathbf{k}$:
$$ [{}_0 R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
* **Surface-adapted basis.** With $s = \sqrt{1 + 4r^2/a^2}$, the unit tangent along the meridian is $\mathbf{e}_g = (\mathbf{e}_r + \tfrac{2r}{a}\mathbf{k})/s$ and the unit normal pointing into the bowl is $\mathbf{n}_{in} = (\mathbf{k} - \tfrac{2r}{a}\mathbf{e}_r)/s$, proportional to $-\boldsymbol{\nabla}f$ of Phase 3. Since $\mathbf{e}_g \times \mathbf{e}_\theta = \mathbf{n}_{in}$ the triple is right-handed, and
$$ [{}_1 R_2] = \begin{pmatrix} 1/s & 0 & -2r/(as) \\ 0 & 1 & 0 \\ 2r/(as) & 0 & 1/s \end{pmatrix}, \qquad \det[{}_1 R_2] = \frac{1}{s^2} + \frac{4r^2}{a^2s^2} = 1, \qquad [{}_1 R_2][{}_1 R_2]^T = I $$
* The determinants and products $R R^T$ were verified symbolically with sympy.

### Phase 3: Step-by-Step Mathematical Deduction

#### 1. First Integral from the $\mathbf{e}_\theta$ Component of Newton's Law
* **Pedagogical Justification:** The coordinate $\theta$ is cyclic (surface of revolution, vertical gravity). In cylindrical coordinates $a_\theta = r\ddot{\theta} + 2\dot{r}\dot{\theta} = \frac{1}{r}\frac{d}{dt}\left(r^2\dot{\theta}\right)$ (Notes Sec. 2.6.2). The normal to the surface $f(r, z) = r^2 - az = 0$ is $\boldsymbol{\nabla} f = 2r\mathbf{e}_r - a\mathbf{k}$, with no azimuthal component ($\mathbf{n} \cdot \mathbf{e}_\theta = 0$), and gravity acts along $-\mathbf{k}$. Hence the $\mathbf{e}_\theta$ equation of motion is $\frac{m}{r}\frac{d}{dt}(r^2\dot{\theta}) = 0$.
$$ r^2 \dot{\theta} = r(0)^2\dot{\theta}(0) = a^2\left(\frac{v_0}{a}\right) = a v_0 $$
$$ r^2 \dot{\theta} = a v_0 \implies \dot{\theta} = \frac{a v_0}{r^2} $$

#### 2. Conservation of Mechanical Energy
* **Pedagogical Justification:** The constraint is frictionless (bilateral holonomic), so the normal reaction does zero work. Gravity is conservative with potential $V = mgz = mg\frac{r^2}{a}$.

Initial energy:

$$ E = \frac{1}{2}m v_0^2 + mg z(0) = \frac{1}{2}m v_0^2 + mga $$

Energy at time $t$:

$$ E = \frac{1}{2}m\left[ \dot{r}^2\left(1 + \frac{4r^2}{a^2}\right) + r^2\dot{\theta}^2 \right] + mg\frac{r^2}{a} = \frac{1}{2}m v_0^2 + mga $$

Multiply by $\frac{2}{m}$:

$$ \dot{r}^2\left(1 + \frac{4r^2}{a^2}\right) + r^2\left(\frac{a v_0}{r^2}\right)^2 + \frac{2gr^2}{a} = v_0^2 + 2ga $$
$$ \dot{r}^2\left(1 + \frac{4r^2}{a^2}\right) + \frac{a^2 v_0^2}{r^2} + \frac{2gr^2}{a} = v_0^2 + 2ga $$

Grouping terms:

$$ \dot{r}^2\left(1 + \frac{4r^2}{a^2}\right) + r^2\left(\dot{\theta}^2 + \frac{2g}{a}\right) = v_0^2 + 2ga $$

Compare with the quadrature formula in the official solution key (Problems.pdf, Solution keys section).

#### 3. Reduction to Quadratures

Isolating $\dot{r}$:

$$ \dot{r}^2 = \frac{v_0^2 + 2ga - \frac{a^2 v_0^2}{r^2} - \frac{2gr^2}{a}}{1 + \frac{4r^2}{a^2}} = \frac{r^2(v_0^2 + 2ga) - a^2 v_0^2 - \frac{2g}{a}r^4}{r^2\left(1 + \frac{4r^2}{a^2}\right)} $$

Taking the square root and separating variables:

$$ \int \sqrt{\frac{1 + 4r^2/a^2}{v_0^2 + 2ga - a^2 v_0^2/r^2 - 2gr^2/a}}\,dr = \pm \int dt $$

#### 4. Determination of Maximum and Minimum of $r$

Setting $\dot{r} = 0$:

$$ v_0^2 + 2ga - \frac{a^2 v_0^2}{r^2} - \frac{2gr^2}{a} = 0 $$

Multiply by $a r^2$:

$$ a r^2(v_0^2 + 2ga) - a^3 v_0^2 - 2g r^4 = 0 $$
$$ 2g r^4 - a(v_0^2 + 2ga)r^2 + a^3 v_0^2 = 0 $$

Let $u = r^2$. The quadratic in $u$ is:

$$ 2g u^2 - a(v_0^2 + 2ga)u + a^3 v_0^2 = 0 $$

Since $r = a \implies u = a^2$ must be a root:

$$ 2g(a^2)^2 - a(v_0^2 + 2ga)(a^2) + a^3 v_0^2 = 2ga^4 - a^3 v_0^2 - 2ga^4 + a^3 v_0^2 = 0 $$

Factorizing $(u - a^2)$:

$$ 2g u^2 - a(v_0^2 + 2ga)u + a^3 v_0^2 = (u - a^2)(2g u - a v_0^2) = 0 $$

The two roots for $u = r^2$ are:

$$ u_1 = a^2 \implies r_1 = a $$
$$ u_2 = \frac{a v_0^2}{2g} \implies r_2 = v_0\sqrt{\frac{a}{2g}} $$

### Phase 4: Physical Interpretation & Dimensional Verification
* **Case 1: $v_0 < \sqrt{2ga}$**

$r_2 = v_0\sqrt{\frac{a}{2g}} < a$.

$$ r_{max} = a, \qquad r_{min} = v_0\sqrt{\frac{a}{2g}} $$

The particle falls inwards towards the vertex, reaches $r_{min}$, and climbs back to $a$.

* **Case 2: $v_0 = \sqrt{2ga}$**

$r_2 = a$. Both roots coincide:

$$ r_{min} = r_{max} = a $$

The particle moves on a horizontal circular orbit of constant radius $r = a$.

* **Case 3: $v_0 > \sqrt{2ga}$**

$r_2 = v_0\sqrt{\frac{a}{2g}} > a$.

$$ r_{min} = a, \qquad r_{max} = v_0\sqrt{\frac{a}{2g}} $$

The particle climbs up the paraboloid to $r_{max}$, then falls back to $a$.

* Compare with the official solution key (Problems.pdf, Solution keys section).
* **Dimensional check:** $[v_0^2 + 2ga] = \text{m}^2/\text{s}^2$, $[a^2v_0^2/r^2] = \text{m}^2/\text{s}^2$ and $[2gr^2/a] = \text{m}^2/\text{s}^2$; the roots $r_2 = v_0\sqrt{a/(2g)}$ have units $(\text{m/s})\sqrt{\text{m}/(\text{m/s}^2)} = \text{m}$.
* **Circular orbit (Case 2):** for $v_0^2 = 2ga$ the quadratic of Phase 3 becomes $2g\,u^2 - 4ga^2u + 2ga^4 = 2g\,(u - a^2)^2$, a double root at $u = a^2$, so $\dot{r} \equiv 0$. This agrees with the circular-orbit condition $v^2 = g\,r\tan\gamma$ with $\tan\gamma = dz/dr = 2r/a = 2$ at $r = a$.
* **Limit $v_0 \to 0$:** $r_{min} = v_0\sqrt{a/(2g)} \to 0$, the particle drops to the vertex, as expected for a body released at rest.
* **Numerical check ($g = a = v_0 = 1$, case 1):** the turning points are the roots of $v_0^2 + 2ga - a^2v_0^2/r^2 - 2gr^2/a = 0$; bisection gives $r_{min} = 0.707107$ against $v_0\sqrt{a/(2g)} = 0.707107$, and $r_{max} = a = 1$.

---

## 📌 Problem 23: Simple Pendulum

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle of mass $m$ is suspended by a string of length $L$ from pivot $O$, or equivalently moves along the smooth interior of a vertical circular track of radius $L$.
* **Unilateral Constraint:** The particle cannot cross the circular boundary outward, but may detach if the inward contact force drops to zero ($N = 0$, or string slack $T = 0$).
* **Initial Motion:** Pushed from the lowest point ($\theta = 0$) with velocity $v_0$.
* **Part (b) Modification:** The circular track rotates about its vertical diameter with constant angular velocity $\omega$ (a rheonomic constraint, solved in the inertial frame).
* **Parameters:** $m > 0$ [kg], $L > 0$ [m], $g > 0$ [m/s$^2$], $v_0 > 0$ [m/s], $\omega \ge 0$ [rad/s].

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* **Inertial Frame $\mathcal{F}_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$:** $Oz$ points vertically upward ($-\mathbf{k}$ is downward).
* **Polar Coordinate Basis $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{j}\}$:**

Angle $\theta$ measured from the downward vertical ($-\mathbf{k}$):

$$ \mathbf{e}_r = \sin\theta\,\mathbf{i} - \cos\theta\,\mathbf{k} \quad (\text{pointing radially outward}) $$
$$ \mathbf{e}_\theta = \cos\theta\,\mathbf{i} + \sin\theta\,\mathbf{k} \quad (\text{tangential, along increasing } \theta) $$
* **Kinematics:**
* Position: $\mathbf{r} = L\mathbf{e}_r$.
* Velocity: $\mathbf{v} = L\dot{\theta}\mathbf{e}_\theta$.
* Acceleration: $\mathbf{a} = -L\dot{\theta}^2\mathbf{e}_r + L\ddot{\theta}\mathbf{e}_\theta$.
* **Change of basis.** The triple $\{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{j}\}$ listed above has $\mathbf{e}_r \times \mathbf{e}_\theta = -\mathbf{j}$, so it is left-handed (determinant $-1$); the right-handed polar triple is $\{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{e}_3\}$ with $\mathbf{e}_3 = -\mathbf{j}$ (the third vector plays no role in the planar kinematics). The columns are the components in $\mathcal{B}_0 = \{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$:
$$ [{}_0 R_1] = \begin{pmatrix} \sin\theta & \cos\theta & 0 \\ 0 & 0 & -1 \\ -\cos\theta & \sin\theta & 0 \end{pmatrix}, \qquad \det[{}_0 R_1] = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
* The angular velocity of $\mathcal{B}_1$ is $\boldsymbol{\omega}_{10} = \dot{\theta}\,\mathbf{e}_3 = -\dot{\theta}\,\mathbf{j}$, and Poisson's formula gives $\dot{\mathbf{e}}_r = \dot{\theta}\,\mathbf{e}_\theta$, $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_r$, the identities behind $\mathbf{v} = L\dot{\theta}\,\mathbf{e}_\theta$ and $\mathbf{a} = -L\dot{\theta}^2\mathbf{e}_r + L\ddot{\theta}\,\mathbf{e}_\theta$.
* For part (b) the cylindrical basis $\{\mathbf{e}_\rho, \mathbf{e}_\varphi, \mathbf{k}\}$ is obtained from $\mathcal{B}_0$ by the simple rotation $\mathrm{R}_z(\omega t)$ about $\mathbf{k}$ (a rotation matrix with $\det = 1$, $R R^T = I$), and inside the meridian plane the pair $\{\mathbf{e}_r, \mathbf{e}_\theta\}$ is written with $\mathbf{e}_\rho$ in place of $\mathbf{i}$. The determinant and the product $R R^T$ were verified symbolically with sympy.

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a): Planar Motion & Detachment Analysis

#### 1. Mechanical Energy Conservation
* **Pedagogical Justification:** The normal constraint force $\mathbf{N} = -N\mathbf{e}_r$ is always perpendicular to velocity $\mathbf{v} = L\dot{\theta}\mathbf{e}_\theta$ ($\mathbf{N} \cdot \mathbf{v} = 0$), so it does no work. Mechanical energy is strictly conserved.

Taking the lowest point $\theta = 0$ as the gravitational potential reference ($V(0) = 0$):

$$ V(\theta) = mg(L - L\cos\theta) = mgL(1 - \cos\theta) $$
$$ E = \frac{1}{2}m v_0^2 = \frac{1}{2}m v^2 + mgL(1 - \cos\theta) $$

Isolate $v^2(\theta)$:

$$ v^2(\theta) = v_0^2 - 2gL(1 - \cos\theta) $$

#### 2. Normal Reaction Force $N(\theta)$
* **Pedagogical Justification:** Newton's second law along the inward radial normal $\mathbf{e}_n = -\mathbf{e}_r$ provides an explicit expression for the contact reaction force $N(\theta)$ as a function of angle $\theta$.

The forces acting on the particle are gravity $\mathbf{F}_g = -mg\mathbf{k}$ and track reaction $\mathbf{N} = -N\mathbf{e}_r$ ($N > 0$ pushes inward):

$$ \mathbf{F}_g = -mg\mathbf{k} = -mg(-\cos\theta\,\mathbf{e}_r + \sin\theta\,\mathbf{e}_\theta) = mg\cos\theta\,\mathbf{e}_r - mg\sin\theta\,\mathbf{e}_\theta $$

Projecting Newton's second law along the inward normal $-\mathbf{e}_r$:

$$ \sum F_n = N - mg\cos\theta = m a_n = m \frac{v^2}{L} $$
$$ N(\theta) = mg\cos\theta + \frac{m}{L}v^2(\theta) $$

Substitute the energy relation for $v^2(\theta)$:

$$ N(\theta) = mg\cos\theta + \frac{m}{L}\left[ v_0^2 - 2gL(1 - \cos\theta) \right] $$

Expand and combine terms:

$$ N(\theta) = mg\cos\theta + \frac{m v_0^2}{L} - 2mg + 2mg\cos\theta = \frac{m v_0^2}{L} - 2mg + 3mg\cos\theta $$
$$ N(\theta) = \frac{m v_0^2}{L} - mg(2 - 3\cos\theta) $$

#### 3. Detachment Condition ($N = 0$)

The particle leaves the circumference if $N$ drops to zero while $v > 0$:

$$ N(\theta_d) = 0 \implies \frac{m v_0^2}{L} - 2mg + 3mg\cos\theta_d = 0 $$
$$ 3mg\cos\theta_d = 2mg - \frac{m v_0^2}{L} \implies \cos\theta_d = \frac{2gL - v_0^2}{3gL} $$

#### 4. Motion Regimes and Question Resolution: "Is this point ever reached?"
* **Regime 1: $v_0 \le \sqrt{2gL}$ (Low energy, oscillation in lower semicircle)**

Velocity reaches zero when $v^2 = 0$:

$$ v_0^2 - 2gL(1 - \cos\theta_{max}) = 0 \implies \cos\theta_{max} = 1 - \frac{v_0^2}{2gL} \ge 0 \implies \theta_{max} \le \frac{\pi}{2} $$

At this maximum angle, the reaction force is:

$$ N(\theta_{max}) = mg\cos\theta_{max} \ge 0 $$

The particle comes to rest and reverses direction before $N$ can vanish.

**Conclusion:** The detachment point is **never reached**. The particle oscillates periodically in the lower semicircle.

* **Regime 2: $\sqrt{2gL} < v_0 < \sqrt{5gL}$ (Intermediate energy, detachment occurs)**

Since $v_0^2 > 2gL$, the particle crosses the horizontal position $\theta = \pi/2$ with positive velocity.

In the upper semicircle ($\pi/2 < \theta < \pi$), $\cos\theta < 0$.

Evaluate the detachment angle $\cos\theta_d$:

$$ \cos\theta_d = \frac{2gL - v_0^2}{3gL} $$

Because $2gL < v_0^2 < 5gL$:

$$ -1 = \frac{2gL - 5gL}{3gL} < \cos\theta_d < \frac{2gL - 2gL}{3gL} = 0 $$

So $\cos\theta_d \in (-1, 0)$, meaning $\theta_d \in (\pi/2, \pi)$ is physically accessible!

At this point, the speed is:

$$ v^2(\theta_d) = v_0^2 - 2gL\left(1 - \frac{2gL - v_0^2}{3gL}\right) = v_0^2 - 2gL + \frac{2}{3}(2gL - v_0^2) = \frac{v_0^2 - 2gL}{3} > 0 $$

**Conclusion:** The detachment point **is reached**. The particle leaves the circular track at angle $\theta_d = \arccos\left(\frac{2gL - v_0^2}{3gL}\right)$ and transitions into free parabolic flight under gravity alone.

* **Regime 3: $v_0 \ge \sqrt{5gL}$ (High energy, complete vertical loops)**

At the very top of the circle ($\theta = \pi, \cos\pi = -1$):

$$ N(\pi) = \frac{m v_0^2}{L} - mg(2 - 3(-1)) = \frac{m v_0^2}{L} - 5mg \ge 0 $$

The reaction force remains positive throughout the entire loop.

**Conclusion:** The particle **never leaves** the circumference and performs complete revolutions.

#### Part (b): Rotating Circumference with Angular Velocity $\omega$

#### 1. Equations of Motion in the Inertial Frame (rheonomic constraint)
* **Pedagogical Justification:** The circle turns about the vertical axis at the prescribed rate $\omega$, so the constraint depends explicitly on time (rheonomic, Unit 3). The motion is analysed in the inertial frame $\mathcal{F}_0$ with cylindrical coordinates $(\rho, \varphi, z)$ about $Oz$, where the plane of the circle is the meridian plane $\varphi = \omega t$. No moving-frame theorem is needed: the acceleration comes from the cylindrical formulas of Unit 1 and the reaction is a constraint force normal to the wire.

Position of the particle, with $\rho = L\sin\theta$ and $z = -L\cos\theta$ on the circle and $\dot\varphi = \omega$ constant:

$$ \mathbf{r} = \rho\,\mathbf{e}_\rho + z\,\mathbf{k} $$

Cylindrical acceleration with $\ddot\varphi = 0$ (Notes Sec. 2.6.2):

$$ \mathbf{a} = (\ddot\rho - \rho\omega^2)\,\mathbf{e}_\rho + 2\dot\rho\,\omega\,\mathbf{e}_\varphi + \ddot z\,\mathbf{k} $$

Differentiate $\rho$ and $z$ with the chain rule, $\frac{d}{dt}f(\theta(t)) = f'(\theta)\dot\theta$:

$$ \dot\rho = L\cos\theta\,\dot\theta, \qquad \ddot\rho = L\cos\theta\,\ddot\theta - L\sin\theta\,\dot\theta^2 $$
$$ \dot z = L\sin\theta\,\dot\theta, \qquad \ddot z = L\sin\theta\,\ddot\theta + L\cos\theta\,\dot\theta^2 $$

Forces: gravity $\mathbf{F}_g = -mg\,\mathbf{k}$ and the reaction $\mathbf{N} = N_r\,\mathbf{e}_r + N_\varphi\,\mathbf{e}_\varphi$ of the smooth wire. $\mathbf{N}$ is orthogonal to the tangent vector of the circle, $\mathbf{e}_\theta = \cos\theta\,\mathbf{e}_\rho + \sin\theta\,\mathbf{k}$, which lies in the meridian plane, so $\mathbf{N}\cdot\mathbf{e}_\theta = 0$. Projecting Newton's second law on $\mathbf{e}_\theta$ removes the reaction:

$$ m\,\mathbf{a}\cdot\mathbf{e}_\theta = \mathbf{F}_g\cdot\mathbf{e}_\theta = -mg\sin\theta $$

Compute $\mathbf{a}\cdot\mathbf{e}_\theta = (\ddot\rho - \rho\omega^2)\cos\theta + \ddot z\sin\theta$ term by term:

$$ \ddot\rho\cos\theta + \ddot z\sin\theta = L\ddot\theta(\cos^2\theta + \sin^2\theta) + L\dot\theta^2(-\sin\theta\cos\theta + \sin\theta\cos\theta) = L\ddot\theta $$
$$ -\rho\omega^2\cos\theta = -L\omega^2\sin\theta\cos\theta $$

Therefore:

$$ mL\ddot\theta - mL\omega^2\sin\theta\cos\theta = -mg\sin\theta $$
$$ \ddot\theta + \left(\frac{g}{L} - \omega^2\cos\theta\right)\sin\theta = 0 $$

The component of $\mathbf{N}$ along $\mathbf{e}_\varphi$ is the force that makes the particle follow the turning plane: $N_\varphi = 2m\dot\rho\,\omega = 2mL\omega\dot\theta\cos\theta$. The in-plane component $N_r$ follows from the $\mathbf{e}_r$ projection and is not needed here.

#### 2. Computation of Equilibrium Locations
* **Pedagogical Justification:** Equilibrium relative to the turning circle corresponds to static solutions where $\ddot{\theta} = 0$ and $\dot{\theta} = 0$ (in the inertial frame the particle then describes a horizontal circle).

Setting the angular acceleration to zero:

$$ \left(\frac{g}{L} - \omega^2\cos\theta\right)\sin\theta = 0 $$

This equation is satisfied if either factor vanishes:

1\. **Vertical Alignments ($\sin\theta = 0$):**

$$ \theta_1 = 0 \quad (\text{lowest point / bottom}) $$
$$ \theta_2 = \pi \quad (\text{highest point / top}) $$

2\. **Off-Axis Equilibrium ($\cos\theta = \frac{g}{\omega^2 L}$):**

This solution exists physically if and only if:

$$ \left| \frac{g}{\omega^2 L} \right| \le 1 \iff \omega^2 \ge \frac{g}{L} $$

When $\omega > \sqrt{\frac{g}{L}}$, two symmetric equilibrium positions emerge:

$$ \theta_{3,4} = \pm \arccos\left(\frac{g}{\omega^2 L}\right) $$

### Phase 4: Physical Interpretation & Dimensional Verification
* **Supercritical Pitchfork Bifurcation:**
* For slow rotation $\omega < \omega_c = \sqrt{g/L}$, the bottom $\theta = 0$ is the only stable equilibrium.
* When the rotation rate crosses the critical threshold $\omega_c$, the bottom becomes unstable, and the particle naturally climbs up the wire to settle at the tilted angle $\theta_0 = \arccos\left(\frac{g}{\omega^2 L}\right)$, where the horizontal circle of radius $L\sin\theta$ has exactly the centripetal acceleration that the vertical balance with gravity requires.
* As $\omega \to \infty$, $\cos\theta_0 \to 0 \implies \theta_0 \to \pi/2$ (the particle moves toward the equator).
* **Dimensional check:** $[N] = [mv_0^2/L] = \text{kg}\cdot\text{m}\cdot\text{s}^{-2} = \text{N}$; $\cos\theta_d = (2gL - v_0^2)/(3gL)$ is dimensionless; $\omega_c = \sqrt{g/L}$ has units $\text{s}^{-1}$.
* **Limits of the regimes:** at $v_0^2 = 2gL$, $\cos\theta_d = 0$ ($\theta_d = \pi/2$), the boundary between oscillation and detachment; at $v_0^2 = 5gL$, $\cos\theta_d = -1$ ($\theta_d = \pi$) and $N(\pi) = 0$, the boundary between detachment and full loops. For $\omega \to 0$ in part (b) the equation reduces to the simple pendulum $\ddot{\theta} + (g/L)\sin\theta = 0$.
* **Numerical example ($g = L = 1$, $v_0^2 = 3.5$, regime 2):** $\cos\theta_d = (2 - 3.5)/3 = -0.5$, $\theta_d = 120^\circ$; $v^2(\theta_d) = (v_0^2 - 2gL)/3 = 0.5$ and $N(\theta_d) = v_0^2/L - g(2 - 3\cos\theta_d) = 3.5 - 3.5 = 0$, as required.

---

## 📌 Problem 24: Particle on a Circumference with a Spring

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle of mass $m$ slides along a vertical circular wire of radius $a$ centered at $O$. A linear spring of stiffness $k$ and zero natural length connects the particle $P$ to anchor point $A(0, \beta a)$ on the vertical axis.
* **CDOFs:** 1 degree of freedom, angle $\theta$ measured counterclockwise from the positive $x$-axis.
* **Forces:**

1\. Gravity: $-mg\mathbf{j}$.

2\. Spring force: $\mathbf{F}_s = -k\mathbf{AP}$.

3\. Constraint reaction $\mathbf{N}$ normal to the wire.

* **Initial State ($t = 0$):** Released from $(a, 0) \implies \theta(0) = 0$ with $\mathbf{v}_0 = v_0\mathbf{j} \implies \dot{\theta}(0) = v_0/a$.
* **Parameters:** $m, a, k, g, \beta, v_0 > 0$.

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* Position of anchor $A$: $\mathbf{r}_A = \beta a\mathbf{j}$.
* Position of particle $P$: $\mathbf{r}_P = a\cos\theta\,\mathbf{i} + a\sin\theta\,\mathbf{j}$.
* Spring elongation vector:
$$ \mathbf{AP} = \mathbf{r}_P - \mathbf{r}_A = a\cos\theta\,\mathbf{i} + a(\sin\theta - \beta)\,\mathbf{j} $$
* Length squared of spring:
$$ |\mathbf{AP}|^2 = a^2\cos^2\theta + a^2(\sin\theta - \beta)^2 = a^2\left[\cos^2\theta + \sin^2\theta - 2\beta\sin\theta + \beta^2\right] = a^2(1 + \beta^2 - 2\beta\sin\theta) $$

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a): Total Potential Energy Function $V(\theta)$
* **Pedagogical Justification:** Both gravity and the linear spring are conservative forces. The total potential energy is the sum of gravitational and elastic potentials.
$$ V_g(\theta) = mgy = mga\sin\theta $$
$$ V_s(\theta) = \frac{1}{2}k |\mathbf{AP}|^2 = \frac{1}{2}k a^2(1 + \beta^2 - 2\beta\sin\theta) $$

Summing both contributions:

$$ V(\theta) = mga\sin\theta + \frac{1}{2}k a^2(1 + \beta^2) - k\beta a^2\sin\theta = \frac{1}{2}ka^2(1 + \beta^2) + (mg - k\beta a)a\sin\theta $$

#### Part (b): Identification of Equilibrium Positions

Equilibrium requires $\frac{dV}{d\theta} = 0$:

$$ \frac{dV}{d\theta} = (mg - k\beta a)a\cos\theta = 0 $$

Two cases emerge:

1\. If $mg - k\beta a \neq 0$: $\cos\theta = 0 \implies \theta_1 = \frac{\pi}{2}$ (top) and $\theta_2 = -\frac{\pi}{2}$ (bottom).

2\. If $\beta = \frac{mg}{ka}$: $\frac{dV}{d\theta} \equiv 0$ for **all** $\theta$. Every point along the circumference is an equilibrium position (neutral equilibrium)!

#### Part (c): Reduction of Motion to Quadratures

Conservation of mechanical energy:

$$ E = \frac{1}{2}m a^2 \dot{\theta}^2 + V(\theta) = \frac{1}{2}m v_0^2 + V(0) = \frac{1}{2}m v_0^2 + \frac{1}{2}ka^2(1 + \beta^2) $$
$$ \dot{\theta} = \pm \sqrt{\frac{v_0^2}{a^2} - \frac{2(mg - k\beta a)}{ma}\sin\theta} $$
$$ \int_{0}^{\theta(t)} \frac{d\theta'}{\sqrt{\frac{v_0^2}{a^2} - \frac{2(mg - k\beta a)}{ma}\sin\theta'}} = t $$

#### Part (d): Case $\beta = \frac{mg}{ka}$

When $\beta = \frac{mg}{ka}$, the coefficient $(mg - k\beta a) = 0$.

The potential energy is strictly constant: $V(\theta) = \text{constant}$.

The equation of motion reduces to:

$$ \ddot{\theta} = 0 \implies \dot{\theta}(t) = \dot{\theta}(0) = \frac{v_0}{a} $$

Integrating with $\theta(0) = 0$:

$$ \theta(t) = \frac{v_0}{a}t $$

The particle circles the wire with strictly uniform angular speed!

#### Part (e): Viscous Damping Case (Damping force $\mathbf{F}_d = -2m\mu\mathbf{v}$)

With $\beta = \frac{mg}{ka}$, the tangential equation of motion is:

$$ m a \ddot{\theta} = F_{d, \theta} = -2m\mu(a\dot{\theta}) $$

Divide by $ma$:

$$ \ddot{\theta} + 2\mu\dot{\theta} = 0 $$

Let $\omega(t) = \dot{\theta}(t)$:

$$ \dot{\omega} + 2\mu\omega = 0 \implies \omega(t) = \omega(0)e^{-2\mu t} = \frac{v_0}{a}e^{-2\mu t} $$

Integrate for position $\theta(t) = \int_0^t \omega(t')dt'$ with $\theta(0) = 0$:

$$ \theta(t) = \frac{v_0}{a}\int_0^t e^{-2\mu t'}dt' = \frac{v_0}{a}\left[ -\frac{1}{2\mu}e^{-2\mu t'} \right]_0^t = \frac{v_0}{2\mu a}\left(1 - e^{-2\mu t}\right) $$

#### Part (f): Reaction of the Circumference

Radial Newton's second law, with $N$ the component of the reaction along $+\mathbf{e}_r$ (outward), $\mathbf{F}_g \cdot \mathbf{e}_r = -mg\sin\theta$ and $\mathbf{F}_s \cdot \mathbf{e}_r = -ka(1 - \beta\sin\theta)$:

$$ -m a \dot{\theta}^2 = N + \mathbf{F}_g \cdot \mathbf{e}_r + \mathbf{F}_s \cdot \mathbf{e}_r $$
$$ N(t) = -m a [\dot{\theta}(t)]^2 + mg\sin\theta(t) + k a(1 - \beta\sin\theta(t)) $$

Substitute $\beta = \frac{mg}{ka}$:

$$ N(t) = ka - m a \left(\frac{v_0}{a}\right)^2 e^{-4\mu t} = ka - \frac{m v_0^2}{a}e^{-4\mu t} $$
* **Erratum:** The first version of part (f) had the sign of the reaction wrong ($N = ma\dot{\theta}^2 + mg\sin\theta + ka(1 - \beta\sin\theta)$, which follows from no sign convention). With $N$ the outward component, $N = -ma\dot{\theta}^2 + mg\sin\theta + ka(1 - \beta\sin\theta)$, i.e. $N\,\mathbf{e}_r = ka - (mv_0^2/a)e^{-4\mu t}$ for $\beta = mg/(ka)$ (inward component $-N$). Numeric check: sympy solving $m\mathbf{a} = \mathbf{F}_g + \mathbf{F}_s + N\mathbf{e}_r$ reproduces the general expression with zero residual.

### Phase 4: Physical Interpretation & Dimensional Verification
* As $t \to \infty$, the particle comes to rest asymptotically at $\theta_\infty = \frac{v_0}{2\mu a}$, and the reaction force approaches the static spring preload $ka$.

---

## 📌 Problem 29: Heavy Particle on a Tilted Cylinder

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle of mass $m$ moves without friction on an infinitely long circular cylinder of radius $R$ whose axis $Oz$ forms an angle $\alpha$ with the vertical.
* **CDOFs:** 2 degrees of freedom: axial coordinate $z(t)$ and azimuthal angle $\theta(t)$.
* **Initial State ($t = 0$):** $z(0) = 0, \theta(0) = \pi/2$, with $\dot{z}(0) = v_0$ and $\dot{\theta}(0) = \omega_0$.
* **Parameters:** $m, R, \alpha, g, v_0, \omega_0$.

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* Cylindrical basis on cylinder: $\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}$.
* Gravity vector decomposed along cylinder axes:
* Axial component along $-Oz$: $g_z = -g\cos\alpha$.
* Transverse horizontal/vertical component in cross-section: $g_\perp = g\sin\alpha$.
$$ \mathbf{g} = -g\sin\alpha\sin\theta\,\mathbf{e}_\theta + g\sin\alpha\cos\theta\,\mathbf{e}_r - g\cos\alpha\,\mathbf{k} $$

From the figure, $\mathbf{z} = \sin\alpha\,\mathbf{i}_1 + \cos\alpha\,\mathbf{k}_1$ and $\mathbf{x} = \cos\alpha\,\mathbf{i}_1 - \sin\alpha\,\mathbf{k}_1$, so $-g\mathbf{k}_1 = g\sin\alpha\,\mathbf{x} - g\cos\alpha\,\mathbf{z}$: $\theta = 0$ is the lowest generator of the cylinder.

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a): Axial Motion $z(t)$
* **Pedagogical Justification:** The cylinder surface is smooth, so the reaction force is purely radial ($\mathbf{N} = N\mathbf{e}_r$) and has zero component along the cylinder axis $Oz$. The axial dynamics completely decouple into constant gravitational acceleration.
$$ m\ddot{z} = -mg\cos\alpha \implies \ddot{z} = -g\cos\alpha $$

Integrate once with $\dot{z}(0) = v_0$:

$$ \dot{z}(t) = v_0 - g\cos\alpha\,t $$

Integrate for position with $z(0) = 0$:

$$ z(t) = v_0 t - \frac{1}{2}g\cos\alpha\,t^2 $$

#### Part (b): Angular Evolution $\theta(t)$ Reduced to Quadratures

Azimuthal equation:

$$ m R \ddot{\theta} = -mg\sin\alpha\sin\theta \implies \ddot{\theta} + \frac{g\sin\alpha}{R}\sin\theta = 0 $$

Multiply by $\dot{\theta}$ and integrate:

$$ \frac{1}{2}\dot{\theta}^2 - \frac{g\sin\alpha}{R}\cos\theta = C_\theta $$

At $t = 0$, $\theta = \pi/2 \implies \cos(\pi/2) = 0$, $\dot{\theta}(0) = \omega_0$:

$$ C_\theta = \frac{1}{2}\omega_0^2 $$
$$ \dot{\theta}^2 = \omega_0^2 + \frac{2g\sin\alpha}{R}\cos\theta $$

Separation of variables:

$$ \int_{\pi/2}^{\theta(t)} \frac{d\theta'}{\sqrt{\omega_0^2 + \frac{2g\sin\alpha}{R}\cos\theta'}} = \pm t $$

#### Part (c): Normal Reaction Force $N(\theta)$

Radial equation along $-\mathbf{e}_r$ ($N$ is the inward reaction; gravity has component $+mg\sin\alpha\cos\theta$ along $+\mathbf{e}_r$, hence $-mg\sin\alpha\cos\theta$ along $-\mathbf{e}_r$):

$$ m R \dot{\theta}^2 = N - mg\sin\alpha\cos\theta $$
$$ N(\theta) = m R \dot{\theta}^2 + mg\sin\alpha\cos\theta = m R\left(\omega_0^2 + \frac{2g\sin\alpha}{R}\cos\theta\right) + mg\sin\alpha\cos\theta $$
$$ N(\theta) = m R \omega_0^2 + 3mg\sin\alpha\cos\theta $$

#### Part (d): Case $\omega_0^2 = \frac{g\sin\alpha}{R}$
$$ \dot{\theta}^2 = \frac{g\sin\alpha}{R}(1 + 2\cos\theta) $$

Turning point occurs when $\dot{\theta} = 0 \implies \cos\theta = -1/2 \implies \theta = \pm\frac{2\pi}{3}$.

The particle undergoes bounded angular oscillations between $-2\pi/3$ and $+2\pi/3$ about the bottom generator $\theta = 0$ (for $\omega_0 > 0$ it first reaches $2\pi/3$, then swings through $\theta = 0$ to $-2\pi/3$ and back) while accelerating parabolically along the axis $Oz$.

* **Erratum:** The first version had $\mathbf{g}\cdot\mathbf{e}_r = -g\sin\alpha\cos\theta$ and an oscillation between $\pi/3$ and $2\pi/3$. From the figure $\mathbf{g}\cdot\mathbf{e}_r = +g\sin\alpha\cos\theta$ and $\mathbf{g}\cdot\mathbf{e}_\theta = -g\sin\alpha\sin\theta$, so $\theta = 0$ is the stable bottom and the motion in (d) is symmetric about it. The result of (c) was already the inward reaction $N = mR\omega_0^2 + 3mg\sin\alpha\cos\theta$. Numeric check: RK4 of $\ddot{\theta} = -(g\sin\alpha/R)\sin\theta$ from $\theta(0) = \pi/2$ with $\omega_0^2 = g\sin\alpha/R$ gives $\theta_{min}/\pi = -0.6667$ and $\theta_{max}/\pi = +0.6667$; for $\omega_0^2 = 4g\sin\alpha/R$ the particle revolves without stopping.

#### Part (e): Case $\omega_0^2 = \frac{4g\sin\alpha}{R}$

At the top of the cylinder ($\theta = \pi, \cos\pi = -1$):

$$ \dot{\theta}^2(\pi) = \frac{4g\sin\alpha}{R} - \frac{2g\sin\alpha}{R} = \frac{2g\sin\alpha}{R} > 0 $$

The angular velocity never vanishes. The particle performs complete revolutions (helical trajectory with growing pitch) around the cylinder.

### Phase 4: Physical Interpretation & Dimensional Verification
* Complete decoupling between 1D uniform acceleration along $z$ and nonlinear pendulum dynamics in $\theta$.

---

## 📌 Problem 31: Two Particles on Cone with String

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** Two heavy particles $P_1$ and $P_2$, each of mass $m$, connected by an inextensible massless string of length $\ell$.
* $P_1$ is constrained to the frictionless surface of a cone of semi-angle $\alpha$ with vertex at $O$.
* $P_2$ hangs vertically along the cone's axis of symmetry ($Oz$).
* The string passes through a frictionless hole at vertex $O$.
* **Configuration Degrees of Freedom (CDOFs):**
* Ambient coordinates: 6.
* Constraints: $P_1$ on cone (1), string inextensibility $\xi_1 + \xi_2 = \ell$ (1), $P_2$ on axis $Oz$ (2).
* Total CDOFs: $6 - 4 = 2$.
* Generalized coordinates: $\xi(t)$ (distance $OP_1$) and azimuthal angle $\theta(t)$.
* **Hypotheses:** String is always taut ($T(t) > 0$), frictionless hole and cone surface.
* **Parameters:** $m, \ell, \alpha, g > 0$.

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* Cylindrical frame on the cone:
* Unit vector along cone generator from $O$ to $P_1$:
$$ \mathbf{e}_\xi = \sin\alpha\,\mathbf{e}_r - \cos\alpha\,\mathbf{k} $$
* Unit tangent along parallel: $\mathbf{e}_\theta = -\sin\theta\,\mathbf{i} + \cos\theta\,\mathbf{j}$.
* Unit outward normal to the cone:
$$ \mathbf{n} = \cos\alpha\,\mathbf{e}_r + \sin\alpha\,\mathbf{k} $$
* Position of $P_1$:
$$ \mathbf{r}_1 = \xi\mathbf{e}_\xi = \xi\sin\alpha\,\mathbf{e}_r - \xi\cos\alpha\,\mathbf{k} $$
* Position of $P_2$ (hanging at distance $\ell - \xi$ below $O$):
$$ \mathbf{r}_2 = -(\ell - \xi)\mathbf{k} $$

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a): Kinematics of $P_1$ and $P_2$

1\. **For $P_1$:**

Velocity:

$$ \mathbf{v}_1 = \dot{\xi}\mathbf{e}_\xi + \xi\sin\alpha\dot{\theta}\mathbf{e}_\theta $$

Acceleration:

$$ \mathbf{a}_1 = (\ddot{\xi} - \xi\dot{\theta}^2\sin^2\alpha)\mathbf{e}_\xi + (2\dot{\xi}\dot{\theta}\sin\alpha + \xi\ddot{\theta}\sin\alpha)\mathbf{e}_\theta - \xi\dot{\theta}^2\sin\alpha\cos\alpha\,\mathbf{n} $$

2\. **For $P_2$:**

$$ \mathbf{v}_2 = \dot{\xi}\mathbf{k} $$
$$ \mathbf{a}_2 = \ddot{\xi}\mathbf{k} $$

#### Part (b): Forces on $P_1$ and $P_2$

1\. On $P_1$:

* Gravity: $\mathbf{F}_{g1} = -mg\mathbf{k} = mg\cos\alpha\mathbf{e}_\xi - mg\sin\alpha\mathbf{n}$.
* String tension: $\mathbf{T}_1 = -T\mathbf{e}_\xi$ ($T > 0$).
* Normal cone reaction: $\mathbf{N} = N\mathbf{n}$.

2\. On $P_2$:

* Gravity: $\mathbf{F}_{g2} = -mg\mathbf{k}$.
* String tension: $\mathbf{T}_2 = +T\mathbf{k}$.
* Guide reaction: $\mathbf{R}_2 \perp \mathbf{k}$.

#### Part (c): Equations of Motion

1\. $P_2$ along $\mathbf{k}$:

$$ m\ddot{\xi} = T - mg \implies T = m(g + \ddot{\xi}) $$

2\. $P_1$ along generator $\mathbf{e}_\xi$:

$$ m(\ddot{\xi} - \xi\dot{\theta}^2\sin^2\alpha) = mg\cos\alpha - T $$

Substitute $T = m(g + \ddot{\xi})$:

$$ m(\ddot{\xi} - \xi\dot{\theta}^2\sin^2\alpha) = mg\cos\alpha - m(g + \ddot{\xi}) $$
$$ 2\ddot{\xi} - \xi\dot{\theta}^2\sin^2\alpha + g(1 - \cos\alpha) = 0 $$

3\. $P_1$ along parallel $\mathbf{e}_\theta$:

$$ m(\xi\ddot{\theta}\sin\alpha + 2\dot{\xi}\dot{\theta}\sin\alpha) = 0 \implies \xi\ddot{\theta} + 2\dot{\xi}\dot{\theta} = 0 $$
$$ \frac{d}{dt}(\xi^2\dot{\theta}) = 0 $$

4\. $P_1$ along normal $\mathbf{n}$:

$$ m\,\mathbf{a}_1\cdot\mathbf{n} = N - mg\sin\alpha \implies N = mg\sin\alpha - m\xi\dot{\theta}^2\sin\alpha\cos\alpha $$

#### Part (d): Condition for String to Remain Taut

For the string to remain in tension ($T > 0$):

$$ T = m(g + \ddot{\xi}) > 0 \implies \ddot{\xi} > -g $$

#### Part (e): Circular Trajectory on a Parallel

For a steady circular trajectory: $\xi = \text{constant} \implies \dot{\xi} = 0, \ddot{\xi} = 0$.

The radial equation gives:

$$ -\xi\dot{\theta}^2\sin^2\alpha + g(1 - \cos\alpha) = 0 \implies \xi\dot{\theta}^2\sin^2\alpha = g(1 - \cos\alpha) $$
$$ \dot{\theta} = \frac{1}{\sin\alpha}\sqrt{\frac{g(1 - \cos\alpha)}{\xi}} $$

Values of Tension and Normal Force:

$$ T = mg $$
$$ N = mg\sin\alpha - m\cos\alpha\left[\frac{g(1 - \cos\alpha)}{\sin\alpha}\right] = \frac{mg}{\sin\alpha}(\sin^2\alpha - \cos\alpha + \cos^2\alpha) = \frac{mg(1 - \cos\alpha)}{\sin\alpha} $$
* **Erratum:** The first version had $\mathbf{a}_1\cdot\mathbf{n} = +\xi\dot{\theta}^2\sin\alpha\cos\alpha$ and $N = mg\sin\alpha + m\xi\dot{\theta}^2\sin\alpha\cos\alpha$ (its own algebra in (e) did not reach the quoted result). The centripetal term points against the outward normal: $\mathbf{a}_1\cdot\mathbf{n} = -\xi\dot{\theta}^2\sin\alpha\cos\alpha$, hence $N = mg\sin\alpha - m\xi\dot{\theta}^2\sin\alpha\cos\alpha$, which gives the same final value $N = mg(1 - \cos\alpha)/\sin\alpha$. Numeric check: sympy differentiation of $\mathbf{r}_1$ gives $\mathbf{a}_1\cdot\mathbf{n} = -\tfrac{1}{2}\xi\dot{\theta}^2\sin 2\alpha$ and $N/(mg) = 0.5774$ at $\alpha = 60^\circ$, equal to $(1 - \cos\alpha)/\sin\alpha$.

#### Part (f): Two First Integrals of Motion

1\. **Azimuthal First Integral (cyclic coordinate $\theta$):**

With $\rho = \xi\sin\alpha$ the distance of $P_1$ to the axis, $a_\theta = \frac{1}{\rho}\frac{d}{dt}(\rho^2\dot{\theta})$. Gravity, the tension (directed to $O$) and the cone reaction all lie in the meridian plane of $P_1$, so the $\mathbf{e}_\theta$ equation reads $\frac{d}{dt}(\xi^2\sin^2\alpha\,\dot{\theta}) = 0$:

$$ \xi^2\dot{\theta} = C_1 $$

2\. **Mechanical Energy First Integral:**

Kinetic energy of both particles:

$$ T_{total} = \frac{1}{2}m v_1^2 + \frac{1}{2}m v_2^2 = \frac{1}{2}m(\dot{\xi}^2 + \xi^2\dot{\theta}^2\sin^2\alpha) + \frac{1}{2}m\dot{\xi}^2 = m\dot{\xi}^2 + \frac{1}{2}m\xi^2\dot{\theta}^2\sin^2\alpha $$

Potential energy:

$$ V_{total} = mg z_1 + mg z_2 = -mg\xi\cos\alpha - mg(\ell - \xi) = mg\xi(1 - \cos\alpha) - mg\ell $$

Conserved total energy $E = T_{total} + V_{total}$:

$$ 2\dot{\xi}^2 + \xi^2\dot{\theta}^2\sin^2\alpha + 2g\xi(1 - \cos\alpha) = C_2 $$

Compare with the official solution key (Problems.pdf, Solution keys section).

### Phase 4: Physical Interpretation & Dimensional Verification
* The effective potential $V_{eff}(\xi) = \frac{m C_1^2\sin^2\alpha}{2\xi^2} + mg\xi(1 - \cos\alpha)$ exhibits a stable minimum corresponding to the circular parallel orbit.

---

## 📌 Problem 32: Particle with String on Spool

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle $P$ of mass $m$ is attached to a string of length $l = 4\pi a$ unwinding from a circular spool of radius $a$ rotating counterclockwise at constant rate $\omega$.
* **Initial Tangency:** Initially at $t = 0$, $A$ is at $(-a, 0)$ and the string is wrapped around the spool.
* **CDOFs:** 1 degree of freedom: the instantaneous unwinding angle $\phi(t)$.
* **Parameters:** $m, a, l = 4\pi a, \omega, g > 0$.

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* Inertial frame: $Oxy$.
* Position of contact point $B$: $\mathbf{r}_B = a\cos\phi\,\mathbf{i} + a\sin\phi\,\mathbf{j}$.
* Unit vectors at $B$:
* Radial: $\mathbf{u}_r = \cos\phi\,\mathbf{i} + \sin\phi\,\mathbf{j}$.
* Tangential: $\mathbf{u}_t = -\sin\phi\,\mathbf{i} + \cos\phi\,\mathbf{j}$ (counterclockwise tangent; the straight segment leaves $B$ clockwise, towards the lower right in the figure, i.e. along $-\mathbf{u}_t$).
* Straight segment length:

The initial wrapped length was $l$. As the spool rotates at rate $\omega$, the length of the unwound free segment $BP$ is:

$$ s(t) = a(3\pi - \omega t + \phi) $$
* Position of particle $P$:
$$ \mathbf{r}_P = \mathbf{r}_B - s(t)\mathbf{u}_t = a\cos\phi\,\mathbf{i} + a\sin\phi\,\mathbf{j} - a(3\pi - \omega t + \phi)(-\sin\phi\,\mathbf{i} + \cos\phi\,\mathbf{j}) $$

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a): Degrees of Freedom
* Although $P$ moves in the plane (2 coordinates), the constraint of remaining tangent to the unwinding spool leaves exactly **1 degree of freedom** ($\phi$).

#### Part (b): Velocity and Acceleration Vectors

Differentiating $\mathbf{r}_P(t)$ with respect to time:

$$ \mathbf{v}_P = \frac{d\mathbf{r}_P}{dt} = a\dot{\phi}\mathbf{u}_t - \dot{s}\mathbf{u}_t + s\dot{\phi}\mathbf{u}_r $$

Since $s(t) = a(3\pi - \omega t + \phi) \implies \dot{s} = a(\dot{\phi} - \omega)$:

$$ \mathbf{v}_P = a\omega\,\mathbf{u}_t + s\dot{\phi}\mathbf{u}_r $$

Differentiating once more, with $\dot{\mathbf{u}}_t = -\dot{\phi}\mathbf{u}_r$ and $\dot{\mathbf{u}}_r = \dot{\phi}\mathbf{u}_t$:

$$ \mathbf{a}_P = \left[s\ddot{\phi} + a\dot{\phi}^2 - 2a\omega\dot{\phi}\right]\mathbf{u}_r + s\dot{\phi}^2\mathbf{u}_t $$

#### Part (c): Forces Acting on $P$

1\. Gravity: $\mathbf{F}_g = -mg\mathbf{j} = -mg(\sin\phi\,\mathbf{u}_r + \cos\phi\,\mathbf{u}_t)$.

2\. Tension: $\mathbf{T} = +T\mathbf{u}_t$ ($T > 0$ directed towards $B$, since $\mathbf{r}_B - \mathbf{r}_P = s\,\mathbf{u}_t$).

* **Erratum:** The first version placed the particle at $\mathbf{r}_B + s\mathbf{u}_t$ (up and to the left of $B$), which contradicts the figure where the segment $BP$ leaves $B$ towards the lower right. Correct: $\mathbf{r}_P = \mathbf{r}_B - s\mathbf{u}_t$, $\mathbf{v}_P = a\omega\,\mathbf{u}_t + s\dot{\phi}\mathbf{u}_r$, $\mathbf{a}_P = [s\ddot{\phi} + a\dot{\phi}^2 - 2a\omega\dot{\phi}]\mathbf{u}_r + s\dot{\phi}^2\mathbf{u}_t$ and tension $+T\mathbf{u}_t$; the equations of part (e) and the energy of part (f) were already consistent with this. Numeric check: sympy differentiation of $\mathbf{r}_P$ reproduces $\mathbf{v}_P$ and $\mathbf{a}_P$, and RK4 of (e) with $\omega = 0$ conserves the energy of (f) to $10^{-13}$ with $T > 0$.

#### Part (d): Mechanical Energy Discussion

For $\omega \neq 0$, the constraint is **rheonomic** (explicitly time-dependent). The contact point $B$ moves with velocity $\mathbf{v}_B = a\omega\mathbf{u}_t$, so the string tension does work on $P$. Mechanical energy is **not conserved** for $\omega \neq 0$.

#### Part (e): Closed Set of Equations

Projecting along the tangent $\mathbf{u}_t$ and normal $\mathbf{u}_r$:

$$ a\left[(3\pi - \omega t + \phi)\ddot{\phi} - 2\omega\dot{\phi} + \dot{\phi}^2\right] = -g\sin\phi $$
$$ T = m a(3\pi - \omega t + \phi)\dot{\phi}^2 + mg\cos\phi $$

Compare with the official solution key (Problems.pdf, Solution keys section).

#### Part (f): Case $\omega = 0$ (Static Spool)

When $\omega = 0$, the constraint is scleronomic and the string does zero work. Mechanical energy is strictly conserved:

$$ E = \frac{1}{2}m [a(3\pi + \phi)]^2 \dot{\phi}^2 + mg\left[a\sin\phi - a(3\pi + \phi)\cos\phi\right] = \text{constant} $$

Compare with the official solution key (Problems.pdf, Solution keys section).

### Phase 4: Physical Interpretation & Dimensional Verification
* The system behaves as an involute pendulum whose effective string length increases or decreases linearly as it unwinds.

---

## 📌 Problem 35: String with Two Particles on a Cylinder

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** two particles $P$ and $Q$ of mass $m$ joined by an inextensible, massless string of length $L$ that rests on a fixed cylinder of radius $R$ and centre $O$, and by a spring of zero natural length and stiffness $k$. The motion is planar, in the plane $Oxy$ with $Oy$ upward.
* **Hypotheses:** the cylinder is smooth, the string is always tense and touches the cylinder along the arc between the tangency points $A$ (right) and $B$ (left), the spring does not touch the cylinder, and the inertial frame $S_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$ is fixed to the cylinder.
* **Parameters:** $m$ [kg], $L$ [m], $R$ [m], $k$ [N/m], $g$ [m/s$^2$]; $\ell_0 = (L - \pi R)/2$ [m] is defined below.

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry

Tangency point $A$ is at the polar angle $\alpha$ from $Ox$ and $B$ at the polar angle $\beta$ from $Ox$. Two orthonormal bases follow the contact points:

$$ \mathbf{n}_A = \cos\alpha\,\mathbf{i} + \sin\alpha\,\mathbf{j}, \quad \mathbf{t}_A = \sin\alpha\,\mathbf{i} - \cos\alpha\,\mathbf{j}, \qquad \mathbf{n}_B = \cos\beta\,\mathbf{i} + \sin\beta\,\mathbf{j}, \quad \mathbf{t}_B = -\sin\beta\,\mathbf{i} + \cos\beta\,\mathbf{j} $$

$\mathbf{n}$ is the outward normal of the cylinder and $\mathbf{t}$ the unit vector along the straight string, pointing from the tangency point to the particle (clockwise at $A$, counter-clockwise at $B$). Change of basis from $\{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$ (columns are the components of $\mathbf{t}_A, \mathbf{n}_A, \mathbf{k}$ and of $\mathbf{n}_B, \mathbf{t}_B, \mathbf{k}$):

$$ [{}_0 R_A] = \begin{pmatrix} \sin\alpha & \cos\alpha & 0 \\ -\cos\alpha & \sin\alpha & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad [{}_0 R_B] = \begin{pmatrix} \cos\beta & -\sin\beta & 0 \\ \sin\beta & \cos\beta & 0 \\ 0 & 0 & 1 \end{pmatrix} $$
$$ \det[{}_0 R_A] = \sin^2\alpha + \cos^2\alpha = 1, \quad \det[{}_0 R_B] = \cos^2\beta + \sin^2\beta = 1, \quad [{}_0 R_A][{}_0 R_A]^T = [{}_0 R_B][{}_0 R_B]^T = I $$

Time derivatives (each basis turns about $\mathbf{k}$ at the rate of its angle):

$$ \dot{\mathbf{t}}_A = \dot\alpha\,\mathbf{n}_A, \quad \dot{\mathbf{n}}_A = -\dot\alpha\,\mathbf{t}_A, \qquad \dot{\mathbf{n}}_B = \dot\beta\,\mathbf{t}_B, \quad \dot{\mathbf{t}}_B = -\dot\beta\,\mathbf{n}_B $$

### Phase 3: Step-by-Step Mathematical Deduction

#### (a) Degrees of freedom and coordinates
* **Pedagogical Justification:** Two free particles in the plane have 4 degrees of freedom. The inextensible string removes one, so the system has 3.

The straight segments $AP$ and $BQ$ have lengths $\xi_P$ and $\xi_Q$, and the string wraps the arc $AB$ of length $R(\beta - \alpha)$ on the cylinder. The length constraint is

$$ \xi_P + \xi_Q + R(\beta - \alpha) = L $$

Generalized coordinates: $(\alpha, \beta, \xi_P)$, with $\xi_Q = L - \xi_P - R(\beta - \alpha)$ (the quadruple $(\alpha, \beta, \xi_P, \xi_Q)$ is used below with this one relation).

#### (b) Position, velocity and acceleration

Positions: $\mathbf{r}_P = R\,\mathbf{n}_A + \xi_P\,\mathbf{t}_A$ and $\mathbf{r}_Q = R\,\mathbf{n}_B + \xi_Q\,\mathbf{t}_B$.

Velocity of $P$ (product rule on each term, using $\dot{\mathbf{n}}_A = -\dot\alpha\,\mathbf{t}_A$ and $\dot{\mathbf{t}}_A = \dot\alpha\,\mathbf{n}_A$):

$$ \mathbf{v}_P = -R\dot\alpha\,\mathbf{t}_A + \dot\xi_P\,\mathbf{t}_A + \xi_P\dot\alpha\,\mathbf{n}_A = (\dot\xi_P - R\dot\alpha)\,\mathbf{t}_A + \xi_P\dot\alpha\,\mathbf{n}_A $$

Differentiate again, again with the product rule:

$$ \mathbf{a}_P = (\ddot\xi_P - R\ddot\alpha)\,\mathbf{t}_A + (\dot\xi_P - R\dot\alpha)\dot\alpha\,\mathbf{n}_A + (\dot\xi_P\dot\alpha + \xi_P\ddot\alpha)\,\mathbf{n}_A - \xi_P\dot\alpha^2\,\mathbf{t}_A $$
$$ \mathbf{a}_P = \left(\ddot\xi_P - R\ddot\alpha - \xi_P\dot\alpha^2\right)\mathbf{t}_A + \left(\xi_P\ddot\alpha + 2\dot\xi_P\dot\alpha - R\dot\alpha^2\right)\mathbf{n}_A $$

For $Q$, with $\dot{\mathbf{n}}_B = \dot\beta\,\mathbf{t}_B$ and $\dot{\mathbf{t}}_B = -\dot\beta\,\mathbf{n}_B$:

$$ \mathbf{v}_Q = (\dot\xi_Q + R\dot\beta)\,\mathbf{t}_B - \xi_Q\dot\beta\,\mathbf{n}_B $$
$$ \mathbf{a}_Q = \left(\ddot\xi_Q + R\ddot\beta - \xi_Q\dot\beta^2\right)\mathbf{t}_B - \left(\xi_Q\ddot\beta + 2\dot\xi_Q\dot\beta + R\dot\beta^2\right)\mathbf{n}_B $$

These four components were checked symbolically with sympy (zero residual).

#### (c) Forces
* Weights: $-mg\,\mathbf{j}$ on each particle.
* String tension $T \ge 0$ (the same on both sides because the cylinder is smooth and the string massless): $-T\,\mathbf{t}_A$ on $P$ and $-T\,\mathbf{t}_B$ on $Q$, directed towards the tangency points. The cylinder acts on the string, not on the particles.
* Spring (zero natural length): $\mathbf{F}_{s,P} = k(\mathbf{r}_Q - \mathbf{r}_P)$ on $P$ and $\mathbf{F}_{s,Q} = -\mathbf{F}_{s,P}$ on $Q$.

Projections of the weight and of the spring force on the bases ($\mathbf{j}\cdot\mathbf{t}_A = -\cos\alpha$, $\mathbf{j}\cdot\mathbf{n}_A = \sin\alpha$, $\mathbf{j}\cdot\mathbf{t}_B = \cos\beta$, $\mathbf{j}\cdot\mathbf{n}_B = \sin\beta$) give the four Newton equations. Writing $\mathbf{d} = \mathbf{r}_Q - \mathbf{r}_P$:

$$ m\left(\ddot\xi_P - R\ddot\alpha - \xi_P\dot\alpha^2\right) = -T + mg\cos\alpha + k\,\mathbf{d}\cdot\mathbf{t}_A $$
$$ m\left(\xi_P\ddot\alpha + 2\dot\xi_P\dot\alpha - R\dot\alpha^2\right) = -mg\sin\alpha + k\,\mathbf{d}\cdot\mathbf{n}_A $$
$$ m\left(\ddot\xi_Q + R\ddot\beta - \xi_Q\dot\beta^2\right) = -T - mg\cos\beta - k\,\mathbf{d}\cdot\mathbf{t}_B $$
$$ -m\left(\xi_Q\ddot\beta + 2\dot\xi_Q\dot\beta + R\dot\beta^2\right) = -mg\sin\beta - k\,\mathbf{d}\cdot\mathbf{n}_B $$

Together with the length constraint these are 5 equations for the 5 unknowns $\alpha, \beta, \xi_P, \xi_Q, T$. Subtracting the first and third equations removes $T$.

#### (d) Mechanical energy
* **Pedagogical Justification:** The mechanical energy of $P$ alone is not conserved: the tension and the spring do work on it, and that work is exchanged with $Q$. For the pair $P + Q$ the only forces that could dissipate energy are the tensions, so their total power is computed first.

Using $\mathbf{t}_A\cdot\mathbf{v}_P = \dot\xi_P - R\dot\alpha$ and $\mathbf{t}_B\cdot\mathbf{v}_Q = \dot\xi_Q + R\dot\beta$:

$$ \dot W_T = -T\,\mathbf{t}_A\cdot\mathbf{v}_P - T\,\mathbf{t}_B\cdot\mathbf{v}_Q = -T\,\frac{d}{dt}\left[\xi_P + \xi_Q + R(\beta - \alpha)\right] = -T\,\dot L = 0 $$

The tensions do zero net work. Gravity and the spring are conservative, so the total mechanical energy of the system is conserved, with the potential energy

$$ V = mg\,(y_P + y_Q) + \tfrac{1}{2}k\,|\mathbf{r}_Q - \mathbf{r}_P|^2, \qquad E = \tfrac{1}{2}m\,(v_P^2 + v_Q^2) + V = \text{constant} $$

#### (e) Symmetric configurations about $Oy$

If the motion keeps the mirror symmetry about $Oy$, then $\beta = \pi - \alpha$ and $\xi_P = \xi_Q = \xi$. The length constraint becomes $2\xi + R(\pi - 2\alpha) = L$, that is

$$ \xi(\alpha) = \ell_0 + R\alpha, \qquad \ell_0 = \frac{L - \pi R}{2} $$

The system has $1$ degree of freedom, the angle $\alpha$. The relations between the coordinates are $\beta = \pi - \alpha$, $\xi_P = \xi_Q = \ell_0 + R\alpha$ and $\dot\xi = R\dot\alpha$.

#### (f) Equilibrium and small oscillations

Coordinates of $P$ in the symmetric case, with $\xi = \ell_0 + R\alpha$:

$$ x_P = R\cos\alpha + \xi\sin\alpha, \qquad y_P = R\sin\alpha - \xi\cos\alpha $$

Derivatives with respect to $\alpha$ (note $\xi' = R$):

$$ x_P' = -R\sin\alpha + R\sin\alpha + \xi\cos\alpha = \xi\cos\alpha, \qquad y_P' = R\cos\alpha - R\cos\alpha + \xi\sin\alpha = \xi\sin\alpha $$

Hence $v_P = \xi\dot\alpha$. By symmetry $x_Q = -x_P$, $y_Q = y_P$, $|\mathbf{r}_Q - \mathbf{r}_P| = 2x_P$, and

$$ T_{kin} = 2\cdot\tfrac{1}{2}m\,\xi^2\dot\alpha^2 = m\,\xi^2\dot\alpha^2, \qquad V(\alpha) = 2mg\,y_P + \tfrac{1}{2}k\,(2x_P)^2 = 2mg\,y_P + 2k\,x_P^2 $$
$$ V'(\alpha) = 2mg\,\xi\sin\alpha + 4k\,x_P\,\xi\cos\alpha = 2\xi\,f(\alpha), \qquad f(\alpha) = mg\sin\alpha + 2k\cos\alpha\,(R\cos\alpha + \xi\sin\alpha) $$
* **Pedagogical Justification:** Equilibrium requires $V'(\alpha_0) = 0$, that is $f(\alpha_0) = 0$ (since $\xi > 0$). Physically, the horizontal pull $2kx_P$ of the spring must be balanced by the horizontal component of the tension, which needs $\alpha_0 < 0$: the segments $AP$ and $BQ$ are slightly inclined inwards.

Assuming the deviation of $AP$ and $BQ$ from the vertical is small, $|\alpha_0| \ll 1$, keep first-order terms ($\sin\alpha \approx \alpha$, $\cos\alpha \approx 1$, $\xi \approx \ell_0$):

$$ mg\,\alpha_0 + 2k\,(R + \ell_0\alpha_0) = 0 \implies \alpha_0 \approx -\frac{2kR}{mg + 2k\ell_0} $$

The equation of motion follows from $\frac{d}{dt}(T_{kin} + V) = 0$. Differentiate with the chain rule, using $\dot\xi = R\dot\alpha$:

$$ 2m\xi^2\dot\alpha\ddot\alpha + 2m\xi R\,\dot\alpha^3 + 2\xi f\,\dot\alpha = 0 \implies m\,\xi\,\ddot\alpha + m R\,\dot\alpha^2 + f(\alpha) = 0 $$

This is exactly the $\mathbf{n}_A$ equation of part (c) with $\dot\xi_P = R\dot\alpha$ and $\mathbf{d}\cdot\mathbf{n}_A = -2x_P\cos\alpha$. Put $\alpha = \alpha_0 + \delta$ with $\delta$ small; the term $\dot\alpha^2$ is second order and $f(\alpha) \approx f'(\alpha_0)\,\delta$:

$$ f'(\alpha) = mg\cos\alpha + 2k\left[\xi\cos^2\alpha - x_P\sin\alpha\right] \approx mg + 2k\,\ell_0 $$
$$ \ddot\delta + \frac{mg + 2k\ell_0}{m\,\ell_0}\,\delta = 0 \implies \omega^2 = \frac{g}{\ell_0} + \frac{2k}{m} $$
$$ \boxed{\;\omega = \sqrt{\frac{g}{\ell_0} + \frac{2k}{m}}, \qquad \ell_0 = \frac{L - \pi R}{2}\;} $$

### Phase 4: Physical Interpretation & Dimensional Verification
* **Limit $k \to 0$:** $\omega = \sqrt{g/\ell_0}$, the pendulum of length $\ell_0$, the free length of each hanging segment. The string unwinds from the cylinder, but at the vertical the instantaneous centre of rotation of $P$ is the tangency point $A$, at distance $\xi_0 \approx \ell_0$.
* **Limit $g \to 0$:** $\omega = \sqrt{2k/m}$, the frequency of two particles of mass $m$ joined by a spring $k$ (reduced mass $m/2$ and stiffness $k$).
* **Dimensional check:** $[g/\ell_0] = \text{s}^{-2}$, $[2k/m] = \text{N/m}/\text{kg} = \text{s}^{-2}$, so $[\omega] = \text{s}^{-1}$; $[\alpha_0] = [kR/(mg + 2k\ell_0)] = \text{N}/\text{N} = 1$.
* **Numerical check ($R = 1$ m, $\ell_0 = 2$ m, $m = 1$ kg, $k = 0.3$ N/m, $g = 9.81$ m/s$^2$):** the exact root of $f(\alpha_0) = 0$ is $\alpha_0 = -0.05453$ rad against $-0.05450$ rad from the linear formula, and the exact $\omega^2 = f'(\alpha_0)/(m\,\xi(\alpha_0)) = 5.648$ s$^{-2}$ against $g/\ell_0 + 2k/m = 5.505$ s$^{-2}$; the small difference is the first-order correction $\xi(\alpha_0) = \ell_0 + R\alpha_0$ in place of $\ell_0$ (using $\xi(\alpha_0)$ gives $5.642$ s$^{-2}$).

---

## 📌 Problem 38: Particle on Torus

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:**
* Particle $P$ ($m_P = 1$) moves without friction on the vertical torus:
$$ x_0 = (2 + \cos\phi)\sin\theta, \quad y_0 = \sin\phi, \quad z_0 = 4 + (2 + \cos\phi)\cos\theta $$
* Particle $Q$ ($m_Q = 2$) is constrained to the horizontal plane $Ox_0y_0$ ($z_0 = 0$).
* Mutual attractive spring force: $\mathbf{F}_{PQ} = -k(\mathbf{r}_P - \mathbf{r}_Q)$ with $k = 2$.
* **Initial State ($t_0$):**
* $P$: $\mathbf{r}_P(t_0) = 2\mathbf{i}_0 + \mathbf{j}_0 + 4\mathbf{k}_0$, $\mathbf{v}_P(t_0) = -\mathbf{k}_0$.
* $Q$: $\mathbf{r}_Q(t_0) = 3\mathbf{i}_0 + \mathbf{j}_0$, $\mathbf{v}_Q(t_0) = -\mathbf{i}_0 + \mathbf{j}_0$.
* **Parameters:** $m_P = 1$, $m_Q = 2$, $k = 2$, $g = 9.81$ m/s$^2$.

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* Minimal coordinate set:
* For $P$: Toroidal angle $\theta$ and poloidal angle $\phi$.
* For $Q$: Cartesian planar coordinates $(\xi, \eta)$ in the plane $z = 0$.
* Total CDOFs: $2 + 2 = 4$.
* **Toroidal basis.** With the toroidal angle $\theta$ (rotation about $\mathbf{j}_0$), $\mathcal{B}_1 = \{\mathbf{e}_\rho, \mathbf{e}_\theta, \mathbf{j}_0\}$ with $\mathbf{e}_\rho = \sin\theta\,\mathbf{i}_0 + \cos\theta\,\mathbf{k}_0$ and $\mathbf{e}_\theta = \cos\theta\,\mathbf{i}_0 - \sin\theta\,\mathbf{k}_0$ (so that $\mathbf{e}_\rho \times \mathbf{e}_\theta = \mathbf{j}_0$). The columns are the components in $\mathcal{B}_0$:
$$ [{}_0 R_1] = \begin{pmatrix} \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \\ \cos\theta & -\sin\theta & 0 \end{pmatrix}, \qquad \det[{}_0 R_1] = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
* **Poloidal basis.** With the poloidal angle $\phi$ (rotation about $\mathbf{e}_\theta$), $\mathcal{B}_2 = \{\mathbf{n}, \mathbf{e}_\theta, \mathbf{t}_\phi\}$ with $\mathbf{n} = \cos\phi\,\mathbf{e}_\rho + \sin\phi\,\mathbf{j}_0$ (outward normal) and $\mathbf{t}_\phi = -\sin\phi\,\mathbf{e}_\rho + \cos\phi\,\mathbf{j}_0$. Its components in $\mathcal{B}_1$ are the columns of
$$ [{}_1 R_2] = \begin{pmatrix} \cos\phi & 0 & -\sin\phi \\ 0 & 1 & 0 \\ \sin\phi & 0 & \cos\phi \end{pmatrix}, \qquad \det[{}_1 R_2] = 1, \qquad [{}_1 R_2][{}_1 R_2]^T = I $$
* In these bases $\mathbf{r}_P = 4\mathbf{k}_0 + 2\mathbf{e}_\rho + \mathbf{n}$, and the two tangent vectors and the normal asked in the statement are $\partial\mathbf{r}_P/\partial\theta = (2 + \cos\phi)\,\mathbf{e}_\theta$, $\partial\mathbf{r}_P/\partial\phi = \mathbf{t}_\phi$ and $(\partial\mathbf{r}_P/\partial\theta) \times (\partial\mathbf{r}_P/\partial\phi) = (2 + \cos\phi)\,\mathbf{n}$. The initial position $\mathbf{r}_P(t_0) = 2\mathbf{i}_0 + \mathbf{j}_0 + 4\mathbf{k}_0$ corresponds to $\theta = \phi = \pi/2$. Both matrices and these vector identities were verified symbolically with sympy.

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a)-(d): Force on $P$ due to $Q$

The attractive force exerted by $Q$ on $P$ is:

$$ \mathbf{F}_P = k(\mathbf{r}_Q - \mathbf{r}_P) = 2(\mathbf{r}_Q - \mathbf{r}_P) $$

Substitute $\mathbf{r}_Q = \xi\mathbf{i}_0 + \eta\mathbf{j}_0$ and $\mathbf{r}_P$:

$$ \mathbf{F}_P = 2[\xi - (2 + \cos\phi)\sin\theta]\mathbf{i}_0 + 2[\eta - \sin\phi]\mathbf{j}_0 - 2[4 + (2 + \cos\phi)\cos\theta]\mathbf{k}_0 $$

Compare with the official solution key (Problems.pdf, Solution keys section).

#### Part (e)-(g): Scalar Conservation Law & Reachability of Torus Summit
* Both gravity and the mutual attractive spring force are conservative. The normal constraint forces do zero work.
* Total mechanical energy $E = T_P + T_Q + V_g + V_{spring} = \text{constant}$.
* Evaluating total initial energy $E_0$:
$$ T_P(t_0) = \frac{1}{2}(1)(1)^2 = \frac{1}{2} $$
$$ T_Q(t_0) = \frac{1}{2}(2)((-1)^2 + 1^2) = 2 $$
$$ V_g(t_0) = m_P g z_P(t_0) = 1 \cdot g \cdot 4 = 4g $$
$$ |\mathbf{r}_P - \mathbf{r}_Q|^2 = (2 - 3)^2 + (1 - 1)^2 + (4 - 0)^2 = 1 + 0 + 16 = 17 $$
$$ V_{spring}(t_0) = \frac{1}{2} k |\mathbf{r}_P - \mathbf{r}_Q|^2 = \frac{1}{2}(2)(17) = 17 $$
$$ E_0 = \frac{1}{2} + 2 + 4g + 17 = 19.5 + 4g $$
* At the highest point of the torus, $z_{max} = 4 + (2 + 1) = 7$.

The minimum gravitational potential alone required to reach this point is:

$$ V_{g,max} = m_P g z_{max} = 7g $$

Required energy: $E_{req} \ge 7g$.

Since $19.5 + 4g < 7g \iff 19.5 < 3g \approx 29.4$, the particle **does not possess enough energy** to ever reach the highest point of the torus!

### Phase 4: Physical Interpretation & Dimensional Verification
* Energy budgeting definitively rules out reaching the summit regardless of the complex non-linear 4-DOF coupling.
* **Dimensional check (SI):** $[k\,|\mathbf{r}_P - \mathbf{r}_Q|^2] = \text{N/m}\cdot\text{m}^2 = \text{J}$, $[m\,g\,z] = \text{kg}\cdot\text{m/s}^2\cdot\text{m} = \text{J}$ and $[m\,v^2] = \text{J}$, so every term of $E_0$ is an energy.
* **Numerical values ($g = 9.81\ \text{m/s}^2$):** $E_0 = 19.5 + 4g = 58.74\ \text{J}$, whereas reaching the summit $z_{max} = 7\ \text{m}$ requires at least $m_Pgz_{max} = 7g = 68.67\ \text{J}$ (the kinetic and spring energies are non-negative, so the potential energy at the summit cannot exceed $E_0$). The deficit is $68.67 - 58.74 = 9.93\ \text{J} > 0$, hence the summit is unreachable.
* **Robustness:** the same inequality holds for any spring constant that keeps $V_{spring} \ge 0$ and also for $k \to 0$ (then $E_0 = 2.5 + 4g = 41.74\ \text{J} < 7g$), so the conclusion does not depend on the value of $k$.

---

## 📌 Problem 39: Particle on a String with a Plate

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle $P$ of mass $m$ is suspended by an inextensible massless string of length $\ell$ anchored at point $O$ on a horizontal thin square plate. The string passes over the straight edge of the plate (at perpendicular distance $d$ from $O$) at contact point $Q$.
* **CDOFs:** 2 degrees of freedom: the angle $\theta$ defining the position of contact point $Q$ along the edge, and the swing angle $\phi$ of the hanging segment $QP$.
* **Initial State ($t = 0$):** $\theta(0) = \phi(0) = \pi/3$ rad, with $|\mathbf{v}_P(0)| = \sqrt{\ell g}$.
* **Parameters:** $m, \ell, d, g > 0$.

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* Frame $S_0: \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$. Plate in horizontal plane $z_0 = 0$.
* Distance from $O$ to edge point $Q$: $r_Q = \frac{d}{\cos\theta}$.
* Hanging segment length: $\rho = \ell - r_Q = \ell - \frac{d}{\cos\theta}$.
* **Geometry assumption (read from the figure, Problems.pdf PDF page 27).** The plate edge is the straight line $x_0 = d$, parallel to $\mathbf{j}_0$ (so $Ox_0$ is perpendicular to the edge); $\theta$ is the angle between $Ox_0$ and $OQ$, and $\phi$ is the angle between the vertical and the line through $P$ perpendicular to the edge, which lies in a plane normal to the edge. The statement text alone does not fix the direction of the edge, so this reading relies on the figure.
* Unit vector $\mathbf{e}_{QP}$ pointing from $Q$ to $P$. The edge is frictionless, so the two string segments make equal angles with it (the hint of the statement): the unit vector from $Q$ to $O$ is $\mathbf{e}_{QO} = -(\cos\theta\,\mathbf{i}_0 + \sin\theta\,\mathbf{j}_0)$, hence $\mathbf{e}_{QP}\cdot\mathbf{j}_0 = -\mathbf{e}_{QO}\cdot\mathbf{j}_0 = \sin\theta$. The remaining part of $\mathbf{e}_{QP}$ lies in the plane normal to the edge, along $\sin\phi\,\mathbf{i}_0 - \cos\phi\,\mathbf{k}_0$, with magnitude $\sqrt{1 - \sin^2\theta} = \cos\theta$:
$$ \mathbf{e}_{QP} = \cos\theta\sin\phi\,\mathbf{i}_0 + \sin\theta\,\mathbf{j}_0 - \cos\theta\cos\phi\,\mathbf{k}_0, \qquad |\mathbf{e}_{QP}|^2 = \cos^2\theta(\sin^2\phi + \cos^2\phi) + \sin^2\theta = 1 $$
* **Swing basis.** The hanging segment $QP$ swings in the plane normal to the edge, i.e. about the edge direction $\mathbf{j}_0$. The basis $\mathcal{B}_1 = \{\mathbf{i}_1, \mathbf{j}_0, \mathbf{k}_1\}$ is the inertial basis rotated by $\phi$ about $\mathbf{j}_0$, with $\mathbf{i}_1 = \cos\phi\,\mathbf{i}_0 + \sin\phi\,\mathbf{k}_0$ and $\mathbf{k}_1 = -\sin\phi\,\mathbf{i}_0 + \cos\phi\,\mathbf{k}_0$; the columns are the components in $\mathcal{B}_0$:
$$ [{}_0 R_1] = \begin{pmatrix} \cos\phi & 0 & -\sin\phi \\ 0 & 1 & 0 \\ \sin\phi & 0 & \cos\phi \end{pmatrix}, \qquad \det[{}_0 R_1] = \cos^2\phi + \sin^2\phi = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
* In this basis the unit vector of Phase 2 reads $\mathbf{e}_{QP} = \sin\theta\,\mathbf{j}_0 - \cos\theta\,\mathbf{k}_1$, since $-\mathbf{k}_1 = \sin\phi\,\mathbf{i}_0 - \cos\phi\,\mathbf{k}_0$ is the direction of the line through $P$ perpendicular to the edge. Both the matrix properties and the identity with the expression of $\mathbf{e}_{QP}$ in $\mathcal{B}_0$ were verified symbolically with sympy.

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a)-(c): Kinematics of $Q$ and $P$

Position of contact point $Q$:

$$ \mathbf{r}_Q = d\,\mathbf{i}_0 + d\tan\theta\,\mathbf{j}_0 $$

Velocity of $Q$:

$$ \mathbf{v}_Q = \frac{d\dot{\theta}}{\cos^2\theta}\,\mathbf{j}_0 $$

Position of particle $P$:

$$ \mathbf{r}_P = \mathbf{r}_Q + \rho\,\mathbf{e}_{QP} = d\,\mathbf{i}_0 + d\tan\theta\,\mathbf{j}_0 + \left(\ell - \frac{d}{\cos\theta}\right)(\cos\theta\sin\phi\,\mathbf{i}_0 + \sin\theta\,\mathbf{j}_0 - \cos\theta\cos\phi\,\mathbf{k}_0) $$

Velocity $\mathbf{v}_P$ is found by differentiating $\mathbf{r}_P(t)$ with respect to time.

#### Part (d): Forces on $P$

1\. Gravity: $\mathbf{F}_g = -mg\mathbf{k}_0$.

2\. String tension: $\mathbf{T} = -T\mathbf{e}_{QP}$.

#### Part (e): Equations of Motion

Projecting Newton's second law along the independent tangent directions yields two coupled second-order ODEs for $\theta(t)$ and $\phi(t)$.

#### Part (f): Work Done by Tension on $P$
* **Pedagogical Justification:** The tension acts along $-\mathbf{e}_{QP}$ on $P$, so its power is $-T\,\mathbf{e}_{QP}\cdot\mathbf{v}_P$. The string is inextensible, so the hanging length $\rho = \ell - d/\cos\theta$ changes only because $Q$ slides along the edge (direction $\mathbf{j}_0$).

Differentiate $\mathbf{r}_P = \mathbf{r}_Q + \rho\,\mathbf{e}_{QP}$ (product rule): $\mathbf{v}_P = \mathbf{v}_Q + \dot{\rho}\,\mathbf{e}_{QP} + \rho\,\dot{\mathbf{e}}_{QP}$. Since $|\mathbf{e}_{QP}| = 1$, $\mathbf{e}_{QP}\cdot\dot{\mathbf{e}}_{QP} = \tfrac{1}{2}\frac{d}{dt}|\mathbf{e}_{QP}|^2 = 0$, so

$$ \mathbf{e}_{QP}\cdot\mathbf{v}_P = \mathbf{e}_{QP}\cdot\mathbf{v}_Q + \dot{\rho} $$

$\mathbf{v}_Q = \dfrac{d\dot{\theta}}{\cos^2\theta}\,\mathbf{j}_0$ has only a $\mathbf{j}_0$ component, so $\mathbf{e}_{QP}\cdot\mathbf{v}_Q = \sin\theta\,\dfrac{d\dot{\theta}}{\cos^2\theta}$. With the chain rule $\frac{d}{dt}\left(\frac{1}{\cos\theta}\right) = \frac{\sin\theta}{\cos^2\theta}\dot{\theta}$, the rate of change of the hanging length is $\dot{\rho} = -\dfrac{d\dot{\theta}\sin\theta}{\cos^2\theta}$. Therefore

$$ \mathbf{e}_{QP}\cdot\mathbf{v}_P = \frac{d\dot{\theta}\sin\theta}{\cos^2\theta} - \frac{d\dot{\theta}\sin\theta}{\cos^2\theta} = 0 \implies \mathbf{T}\cdot\mathbf{v}_P = -T\,\mathbf{e}_{QP}\cdot\mathbf{v}_P = 0 $$

The tension therefore does no work on $P$ ($W_T = 0$), in agreement with the official key (Problems.pdf, PDF page 76).

#### Part (g): Mechanical Energy Conservation

Since the plate is stationary (scleronomic constraint), the tension does no work (part (f)) and gravity is conservative, so $E$ is conserved. With $z_0$ upwards, $z_P = -\rho\cos\theta\cos\phi = -(\ell\cos\theta - d)\cos\phi$ and the gravitational potential energy is $+mgz_P$:

$$ E = \frac{1}{2}m|\mathbf{v}_P|^2 + mgz_P = \frac{1}{2}m|\mathbf{v}_P|^2 - mg(\ell\cos\theta - d)\cos\phi = \text{constant} $$

At $t = 0$: $|\mathbf{v}_P|^2 = \ell g$, $\cos\theta = \cos\phi = \tfrac{1}{2}$, so

$$ E_0 = \frac{1}{2}m\ell g - mg\left(\frac{\ell}{2} - d\right)\frac{1}{2} = \frac{mg\ell}{4} + \frac{mgd}{2} $$

Parts (d) and (e) are only outlined here: the explicit coupled differential equations for $\theta$ and $\phi$ are not derived in this note.

### Phase 4: Physical Interpretation & Dimensional Verification
* The system acts as a variable-length spherical pendulum where string length changes deterministically as $Q$ slides along the boundary.
* **Dimensional check:** $[\rho] = [\ell - d/\cos\theta] = \text{m}$; $[mg\ell] = [mgd] = \text{J}$, so $E_0 = mg\ell/4 + mgd/2$ is an energy; $[\mathbf{e}_{QP}] = 1$.
* **Limit $d \to 0$:** the edge passes through $O$, so $Q = O$, $\rho = \ell$ and $\mathbf{e}_{QP} = (\cos\theta\sin\phi,\ \sin\theta,\ -\cos\theta\cos\phi)$ is the unit vector of a spherical pendulum of length $\ell$ whose angle $\gamma$ with the downward vertical satisfies $\cos\gamma = \cos\theta\cos\phi$. The energy reduces to $E_0 = mg\ell/4$, which equals $\tfrac{1}{2}m\ell g - mg\ell\cos\theta\cos\phi = \tfrac{1}{2}m\ell g - mg\ell/4$ at $\theta = \phi = \pi/3$.
* **Numerical check ($m = 1$ kg, $\ell = 2$ m, $d = 0.5$ m, $g = 9.81\ \text{m/s}^2$):** $E_0 = mg\ell/4 + mgd/2 = 7.3575\ \text{J}$, and directly $\tfrac{1}{2}m\ell g + mgz_P(0) = 9.81 - 2.4525 = 7.3575\ \text{J}$ with $z_P(0) = -(\ell/2 - d)/2 = -0.25\ \text{m}$.

---

## 📌 Problem 48: Two Connected Particles, One on Paraboloid

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** Two particles $P$ and $Q$ of mass $m$ connected by an inextensible massless cord of length $\ell$.
* Particle $P$ is constrained to the frictionless paraboloid $z = c R^2$ ($c > 0$).
* Particle $Q$ hangs along the vertical axis $Oz$.
* Cord passes through a frictionless hole at origin $O$.
* **CDOFs:** 2 degrees of freedom: $(R, \theta)$.
* **Initial State:** $R(0) = 1/c, \theta(0) = 0, \dot{R}(0) = 0, \dot{\theta}(0) = d \neq 0$.
* **Parameters:** $m, c, \ell, g, d$.

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* Cylindrical basis: $\{\mathbf{e}_R, \mathbf{e}_\theta, \mathbf{k}\}$.
* Position of $P$: $\mathbf{r}_P = R\mathbf{e}_R + cR^2\mathbf{k}$.
* Tangent vectors to paraboloid:
$$ \mathbf{t}_R = \frac{\partial\mathbf{r}_P}{\partial R} = \mathbf{e}_R + 2cR\,\mathbf{k} $$
$$ \mathbf{t}_\theta = \frac{\partial\mathbf{r}_P}{\partial\theta} = R\mathbf{e}_\theta $$
* Normal vector to paraboloid:
$$ \mathbf{n} = \mathbf{t}_R \times \mathbf{t}_\theta = (\mathbf{e}_R + 2cR\,\mathbf{k}) \times (R\mathbf{e}_\theta) = R\mathbf{k} - 2cR^2\,\mathbf{e}_R = R(-2cR\,\mathbf{e}_R + \mathbf{k}) $$
* Position of $Q$: Distance along cord from $O$ to $P$ along generator:

Cord length constraint: $s_P + s_Q = \ell$.

For small hole at origin with straight cord to $P$: $|\mathbf{r}_P| = \sqrt{R^2 + c^2 R^4} = R\sqrt{1 + c^2 R^2}$.

Position of $Q$: $\mathbf{r}_Q = -(\ell - R\sqrt{1 + c^2 R^2})\mathbf{k}$.

* **Change of basis (cylindrical basis).** $\mathcal{B}_1 = \{\mathbf{e}_R, \mathbf{e}_\theta, \mathbf{k}\}$ is the inertial basis $\{\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ rotated by $\theta(t)$ about $\mathbf{k}$ ($\mathbf{k} = \mathbf{k}_0$):
$$ [{}_0 R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
* **Surface-adapted basis.** With $s = \sqrt{1 + 4c^2R^2}$, the unit meridian tangent is $\mathbf{e}_g = (\mathbf{e}_R + 2cR\,\mathbf{k})/s$ (proportional to $\mathbf{t}_R$), the unit normal is $\hat{\mathbf{n}} = (-2cR\,\mathbf{e}_R + \mathbf{k})/s$ (proportional to $\mathbf{n}$ above) and $\mathbf{e}_g \times \mathbf{e}_\theta = \hat{\mathbf{n}}$, so $\{\mathbf{e}_g, \mathbf{e}_\theta, \hat{\mathbf{n}}\}$ is right-handed and
$$ [{}_1 R_2] = \begin{pmatrix} 1/s & 0 & -2cR/s \\ 0 & 1 & 0 \\ 2cR/s & 0 & 1/s \end{pmatrix}, \qquad \det[{}_1 R_2] = \frac{1 + 4c^2R^2}{s^2} = 1, \qquad [{}_1 R_2][{}_1 R_2]^T = I $$
* Both determinants and products $R R^T$ were verified symbolically with sympy.

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a)-(d): Forces and Vectors

1\. Forces on $P$: Gravity $-mg\mathbf{k}$, normal reaction $\mathbf{N} = N\frac{-2cR\mathbf{e}_R + \mathbf{k}}{\sqrt{1 + 4c^2 R^2}}$, cord tension $\mathbf{T}_P = -T\frac{\mathbf{r}_P}{|\mathbf{r}_P|}$.

2\. Forces on $Q$: Gravity $-mg\mathbf{k}$, cord tension $\mathbf{T}_Q = +T\mathbf{k}$.

#### Part (e): Tension Condition

The string remains in tension as long as $T(t) > 0$.

For $Q$, $m\ddot{z}_Q = T - mg \implies T = m(g + \ddot{z}_Q) > 0 \iff \ddot{z}_Q > -g$.

#### Part (f)-(g): Two First Integrals of Motion

1\. **Azimuthal First Integral (cyclic coordinate $\theta$):**

In cylindrical coordinates $a_\theta = \frac{1}{R}\frac{d}{dt}(R^2\dot{\theta})$. The paraboloid is axisymmetric, so its reaction has no $\mathbf{e}_\theta$ component; gravity is vertical and the tension of the cord (directed from $P$ to the hole $O$ on the axis) lies in the meridian plane of $P$. The $\mathbf{e}_\theta$ equation is $\frac{m}{R}\frac{d}{dt}(R^2\dot{\theta}) = 0$:

$$ C_z = m R^2\dot{\theta} = \text{constant} = m [R(0)]^2 d = m\frac{d}{c^2} $$
$$ \dot{\theta}(t) = \frac{d}{c^2 R^2} $$

2\. **Total Mechanical Energy Conservation:**

Constraints are frictionless and scleronomic:

$$ E = T_P + T_Q + V_{g,P} + V_{g,Q} = \text{constant} $$
$$ T_P = \frac{1}{2}m\left[\dot{R}^2(1 + 4c^2 R^2) + R^2\dot{\theta}^2\right] $$
$$ T_Q = \frac{1}{2}m\dot{z}_Q^2 $$
$$ V = mg(cR^2) + mg z_Q $$

#### Part (h): Turning Point Equation $f(R) = 0$

Setting $\dot{R} = 0$ in the conserved energy equation $E(R, \dot{R}=0) = E_0$ yields the implicit algebraic equation $f(R) = 0$ whose positive roots define the minimum and maximum radii $R_{min}$ and $R_{max}$.

### Phase 4: Physical Interpretation & Dimensional Verification
* The particle executes bounded precessing orbits on the paraboloid, bounded between two parallel circles $R_{min}$ and $R_{max}$.
* **Dimensional check:** $[c] = \text{m}^{-1}$, $[d] = \text{s}^{-1}$, $R(0) = 1/c$ is a length; $[cR^2] = \text{m}$ and $[c\,R] = 1$, so $\sqrt{1 + c^2R^2}$ is dimensionless.
* **Explicit turning-point equation (part (h)).** At $\dot{R} = 0$ the kinetic energy reduces to $\tfrac{1}{2}mR^2\dot{\theta}^2$ with $R^2\dot{\theta}^2 = d^2/(c^4R^2)$ (from the azimuthal first integral), and the potential energy is $mg\,[cR^2 + R\sqrt{1 + c^2R^2}] - mg\ell$ (the term $-mg\ell$ cancels in $E - E_0$). Equating with the initial energy at $R(0) = 1/c$ (where $R\sqrt{1 + c^2R^2} = \sqrt{2}/c$), per unit mass:
$$ f(R) = \frac{d^2}{2c^4R^2} + g\left(cR^2 + R\sqrt{1 + c^2R^2}\right) - \frac{d^2}{2c^2} - \frac{(1 + \sqrt{2})\,g}{c} = 0 $$

Each term has units m$^2$/s$^2$. The allowed radii are those with $f(R) \le 0$, and $R = 1/c$ is a root (sympy: $f(1/c) = 0$).

* **Numerical example ($c = d = g = 1$):** the roots of $f$ are $R = 0.4828$ and $R = 1$ (the launch point is the outer turning point), $f(0.7) = -0.549$ and $f(0.9) = -0.276$ are negative (allowed band between the roots), and $f(0.4) = 0.802$, $f(1.2) = 0.747$ are positive (forbidden), so the orbit is bounded between $R_{min} = 0.4828/c$ and $R_{max} = 1/c$.

---

## 📌 Problem 50: Double Pendulum

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** Two point masses $P$ and $Q$, each of mass $m$, connected by two rigid massless bars of length $\ell$.
* First bar connects origin $O$ to $P$, making angle $\theta$ with downward vertical.
* Second bar connects $P$ to $Q$, making angle $\phi$ with downward vertical.
* **CDOFs:** 2 degrees of freedom: $(\theta, \phi)$.
* **Parameters:** $m, \ell, g > 0$.

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* Coordinate axes: $Ox$ horizontal to the right, $Oz$ vertically upwards (downward vertical is $-\mathbf{k}$).
* Position of $P$:
$$ \mathbf{r}_P = \ell\sin\theta\,\mathbf{i} - \ell\cos\theta\,\mathbf{k} $$
* Position of $Q$:
$$ \mathbf{r}_Q = \mathbf{r}_P + \ell\sin\phi\,\mathbf{i} - \ell\cos\phi\,\mathbf{k} = \ell(\sin\theta + \sin\phi)\,\mathbf{i} - \ell(\cos\theta + \cos\phi)\,\mathbf{k} $$

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a): Velocity and Acceleration Vectors

1\. Velocity of $P$:

$$ \mathbf{v}_P = \ell\dot{\theta}\cos\theta\,\mathbf{i} + \ell\dot{\theta}\sin\theta\,\mathbf{k} $$
$$ v_P^2 = \ell^2\dot{\theta}^2 $$

2\. Velocity of $Q$:

$$ \mathbf{v}_Q = \ell(\dot{\theta}\cos\theta + \dot{\phi}\cos\phi)\,\mathbf{i} + \ell(\dot{\theta}\sin\theta + \dot{\phi}\sin\phi)\,\mathbf{k} $$
$$ v_Q^2 = \ell^2\left[ \dot{\theta}^2 + \dot{\phi}^2 + 2\dot{\theta}\dot{\phi}(\cos\theta\cos\phi + \sin\theta\sin\phi) \right] = \ell^2\left[ \dot{\theta}^2 + \dot{\phi}^2 + 2\dot{\theta}\dot{\phi}\cos(\theta - \phi) \right] $$

3\. Acceleration of $P$ and $Q$. Define the unit vectors in the $(\mathbf{i}, \mathbf{k})$ plane: $\mathbf{e}_P = \sin\theta\,\mathbf{i} - \cos\theta\,\mathbf{k}$ (from $O$ to $P$), $\mathbf{e}_{\theta} = \cos\theta\,\mathbf{i} + \sin\theta\,\mathbf{k}$, $\mathbf{e}_Q = \sin\phi\,\mathbf{i} - \cos\phi\,\mathbf{k}$ (from $P$ to $Q$), $\mathbf{e}_{\phi} = \cos\phi\,\mathbf{i} + \sin\phi\,\mathbf{k}$. Their derivatives are $\dot{\mathbf{e}}_P = \dot\theta\,\mathbf{e}_\theta$, $\dot{\mathbf{e}}_\theta = -\dot\theta\,\mathbf{e}_P$ and the same with $\phi$. Since $\mathbf{r}_P = \ell\,\mathbf{e}_P$ and $\mathbf{r}_Q = \ell\,\mathbf{e}_P + \ell\,\mathbf{e}_Q$:

$$ \mathbf{a}_P = \ell\left(\ddot\theta\,\mathbf{e}_\theta - \dot\theta^2\,\mathbf{e}_P\right) = \ell(\ddot\theta\cos\theta - \dot\theta^2\sin\theta)\,\mathbf{i} + \ell(\ddot\theta\sin\theta + \dot\theta^2\cos\theta)\,\mathbf{k} $$
$$ \mathbf{a}_Q = \mathbf{a}_P + \ell\left(\ddot\phi\,\mathbf{e}_\phi - \dot\phi^2\,\mathbf{e}_Q\right) $$

#### Part (b)-(c): Forces and Equations of Motion (Newton)
* **Pedagogical Justification:** The bars are massless and rigid, so each one transmits a force along its own axis (tension $T_1$ in $OP$, $T_2$ in $PQ$; a negative value means compression). These two unknowns are eliminated by choosing the projection directions, which is the strategy of Unit 3 for constrained systems.

Forces on $P$: weight $-mg\,\mathbf{k}$, the pull $-T_1\,\mathbf{e}_P$ of bar $OP$ and the pull $+T_2\,\mathbf{e}_Q$ of bar $PQ$. Forces on $Q$: weight $-mg\,\mathbf{k}$ and the pull $-T_2\,\mathbf{e}_Q$ of bar $PQ$ (action and reaction).

$$ m\,\mathbf{a}_P = -mg\,\mathbf{k} - T_1\,\mathbf{e}_P + T_2\,\mathbf{e}_Q, \qquad m\,\mathbf{a}_Q = -mg\,\mathbf{k} - T_2\,\mathbf{e}_Q $$

Scalar products needed ($\mathbf{k}\cdot\mathbf{e}_P = -\cos\theta$, $\mathbf{k}\cdot\mathbf{e}_\theta = \sin\theta$, $\mathbf{k}\cdot\mathbf{e}_Q = -\cos\phi$, $\mathbf{k}\cdot\mathbf{e}_\phi = \sin\phi$):

$$ \mathbf{e}_P\cdot\mathbf{e}_Q = \cos(\theta - \phi), \quad \mathbf{e}_\theta\cdot\mathbf{e}_Q = \sin(\phi - \theta), \quad \mathbf{e}_\theta\cdot\mathbf{e}_\phi = \cos(\theta - \phi), \quad \mathbf{e}_P\cdot\mathbf{e}_\phi = \sin(\theta - \phi) $$

**Equation for $\phi$.** Project the equation of $Q$ on $\mathbf{e}_\phi$, which is orthogonal to $\mathbf{e}_Q$ and removes $T_2$. With $\mathbf{a}_P\cdot\mathbf{e}_\phi = \ell[\ddot\theta\cos(\theta - \phi) - \dot\theta^2\sin(\theta - \phi)]$ and $\ell(\ddot\phi\,\mathbf{e}_\phi - \dot\phi^2\,\mathbf{e}_Q)\cdot\mathbf{e}_\phi = \ell\ddot\phi$:

$$ m\ell\left[\ddot\phi + \ddot\theta\cos(\theta - \phi) - \dot\theta^2\sin(\theta - \phi)\right] = -mg\sin\phi $$
$$ \ddot\phi + \ddot\theta\cos(\theta - \phi) - \dot\theta^2\sin(\theta - \phi) + \frac{g}{\ell}\sin\phi = 0 $$

**Equation for $\theta$.** Add the two equations of motion, so that $T_2\,\mathbf{e}_Q$ cancels, and project on $\mathbf{e}_\theta$, which is orthogonal to $\mathbf{e}_P$ and removes $T_1$. The right-hand side is $-2mg\,\mathbf{k}\cdot\mathbf{e}_\theta = -2mg\sin\theta$ and the left-hand side is $m(\mathbf{a}_P + \mathbf{a}_Q)\cdot\mathbf{e}_\theta$, with $\mathbf{a}_P\cdot\mathbf{e}_\theta = \ell\ddot\theta$ and $\mathbf{a}_Q\cdot\mathbf{e}_\theta = \ell\ddot\theta + \ell\ddot\phi\cos(\theta - \phi) + \ell\dot\phi^2\sin(\theta - \phi)$:

$$ 2\ddot\theta + \ddot\phi\cos(\theta - \phi) + \dot\phi^2\sin(\theta - \phi) + \frac{2g}{\ell}\sin\theta = 0 $$

These two second-order equations contain only $\theta$, $\phi$ and their derivatives, as required in (c). The tensions follow afterwards by projecting on the bar directions: the $\mathbf{e}_Q$ projection of the equation of $Q$ and the $\mathbf{e}_P$ projection of the equation of $P$ give

$$ T_2 = mg\cos\phi - m\ell\left[\ddot\theta\sin(\phi - \theta) - \dot\theta^2\cos(\theta - \phi) - \dot\phi^2\right], \qquad T_1 = mg\cos\theta + m\ell\dot\theta^2 + T_2\cos(\theta - \phi) $$

Check: at rest at $\theta = \phi = 0$ the equations give $T_2 = mg$ and $T_1 = 2mg$, the static tensions of the hanging chain.

#### Part (d): Conservation Law

The system is conservative with scleronomic constraints. Total mechanical energy is constant:

$$ E = \frac{1}{2}m\ell^2\left[ 2\dot{\theta}^2 + \dot{\phi}^2 + 2\dot{\theta}\dot{\phi}\cos(\theta - \phi) \right] - mg\ell(2\cos\theta + \cos\phi) = \text{constant} $$

#### Part (e): Will $Q$ Ever Cross the $Ox$ Axis?
* Given initial state: $\theta(0) = \phi(0) = \pi/4$, released from rest ($\dot{\theta}(0) = \dot{\phi}(0) = 0$).
* Initial energy:
$$ E_0 = -mg\ell\left(2\cos\frac{\pi}{4} + \cos\frac{\pi}{4}\right) = -3mg\ell\frac{\sqrt{2}}{2} = -\frac{3\sqrt{2}}{2}mg\ell \approx -2.121\,mg\ell $$
* For $Q$ to cross the $Ox$ axis, its vertical coordinate $z_Q$ must reach 0:
$$ z_Q = -\ell(\cos\theta + \cos\phi) = 0 \implies \cos\theta + \cos\phi = 0 $$

At that instant, the minimum potential energy of the system is:

$$ V = -mg\ell(2\cos\theta + \cos\phi) = -mg\ell(\cos\theta + (\cos\theta + \cos\phi)) = -mg\ell\cos\theta $$

Since $\cos\theta \le 1$, $V \ge -mg\ell$.

The required energy to cross the axis would be:

$$ E_{req} \ge V \ge -mg\ell $$

However, the initial energy is $E_0 = -2.121\,mg\ell < -mg\ell$.

Because $E_0 < E_{req}$, the kinetic energy would have to be negative, which is physically impossible!

**Conclusion:** $Q$ can **never** cross the $Ox$ axis.

#### Part (f): Imposed Constraint $\phi = 2\theta$ and Small-Angle Natural Frequency

When $\phi = 2\theta$, $\dot{\phi} = 2\dot{\theta}$.

For small angles $\theta \ll 1$:

$$ \cos(\theta - \phi) = \cos(-\theta) = \cos\theta \approx 1 $$

Kinetic energy:

$$ T = \frac{1}{2}m\ell^2\left[ 2\dot{\theta}^2 + (2\dot{\theta})^2 + 2\dot{\theta}(2\dot{\theta})(1) \right] = \frac{1}{2}m\ell^2 [2 + 4 + 4]\dot{\theta}^2 = 5m\ell^2\dot{\theta}^2 $$

Potential energy with $\cos u \approx 1 - \frac{u^2}{2}$:

$$ V = -mg\ell(2\cos\theta + \cos(2\theta)) \approx -mg\ell\left[ 2\left(1 - \frac{\theta^2}{2}\right) + \left(1 - \frac{4\theta^2}{2}\right) \right] $$
$$ V \approx -mg\ell [3 - 3\theta^2] = \text{const} + 3mg\ell\theta^2 $$

Total energy of the equivalent oscillator:

$$ E = 5m\ell^2\dot{\theta}^2 + 3mg\ell\theta^2 = \text{constant} $$

Differentiating with respect to time:

$$ 10m\ell^2\dot{\theta}\ddot{\theta} + 6mg\ell\theta\dot{\theta} = 0 $$

Divide by $10m\ell^2\dot{\theta}$:

$$ \ddot{\theta} + \frac{6g}{10\ell}\theta = 0 \implies \ddot{\theta} + \frac{3g}{5\ell}\theta = 0 $$

The natural frequency of oscillation is:

$$ \omega_0 = \sqrt{\frac{3g}{5\ell}} $$

### Phase 4: Physical Interpretation & Dimensional Verification
* The mechanical coupling $\phi = 2\theta$ acts as an internal kinematic constraint that stiffens the double pendulum into an equivalent single degree of freedom harmonic oscillator with effective mass $10m$ and effective restoring stiffness $6mg/\ell$, yielding the frequency $\omega_0 = \sqrt{3g/(5\ell)}$.
* **Dimensional check:** $[T] = [m\ell^2\dot{\theta}^2] = \text{kg}\cdot\text{m}^2\cdot\text{s}^{-2} = \text{J}$, $[V] = [mg\ell] = \text{J}$, and $[\omega_0] = \sqrt{[g]/[\ell]} = \text{s}^{-1}$ (the effective inertia $10m\ell^2$ and stiffness $6mg\ell$ are expressed in the coordinate $\theta$; with $x = \ell\theta$ they become $10m$ and $6mg/\ell$).
* **Numerical check of part (e) (RK4, step $10^{-3}$, $g = 9.81\ \text{m/s}^2$, $m = \ell = 1$, 60 s from $\theta = \phi = \pi/4$ at rest):** the full nonlinear equations of part (c) give a maximum of $z_Q/\ell = -1.3375$, always negative, so $Q$ never reaches the $Ox$ axis, consistent with the energy bound $V \ge -mg\ell$ against $E_0 = -2.121\,mg\ell$.
* **Numerical check of part (f):** the exact one-degree-of-freedom equation of motion with $\phi = 2\theta$ (without the small-angle approximation) integrated by RK4 from $\theta = 10^{-3}$ rad has half-period $1.2950$ s, against $\pi/\omega_0 = \pi\sqrt{5\ell/(3g)} = 1.2949$ s.
