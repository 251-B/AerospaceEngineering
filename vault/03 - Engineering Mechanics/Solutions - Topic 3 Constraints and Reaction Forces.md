---
title: "Solutions - Topic 3: Constraints and Reaction Forces"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Full Analytical Solutions (4-Phase Methodology)"
language: "English"
---

# 📚 Topic 3: Constraints and Reaction Forces - Full Analytical Solutions

Exhaustive, step-by-step analytical solutions for all 15 solvable problems from Topic 3 (**Constraints and Reaction Forces**) of *Mechanics Applied to Aerospace Engineering* (UC3M). Every problem adheres to the mandatory 4-phase pedagogical methodology, with explicit justification prior to every equation, zero algebraic omissions, explicit derivative developments (product, quotient, and chain rules), explicit integral evaluations (substitutions, primitives, and Barrow's rule), rotation matrices $[{}_0 R_1]$, normal and tangent subspaces ($V_N, V_T$), and dimensional verifications.

---

## 📌 Problem 18: Heavy Particle on a Cone

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A point particle of mass $m$ moves without friction on the interior surface of an inverted cone given by $z^2 = x^2 + y^2$ with $z > 0$.
* **Configuration Degrees of Freedom (CDOFs):**
  - Ambient space: 3 Cartesian coordinates $(x, y, z)$.
  - Holonomic geometric constraint: $\Phi(x, y, z) = x^2 + y^2 - z^2 = 0$.
  - Number of CDOFs: $3 - 1 = 2$. We choose cylindrical coordinates $(r, \theta)$ with $z = r$.
* **Hypotheses:**
  1. Constraint is smooth (frictionless): the reaction force $\mathbf{N}$ is strictly orthogonal to the tangent space of the cone ($W_{\mathbf{N}} = 0$).
  2. Inertial frame with gravity acting along $-Oz$: $\mathbf{g} = -g\mathbf{k}$.
* **Initial State ($t = 0$):**
  - Position: $(x_0, y_0, z_0) = (a, 0, a) \implies r(0) = a, \theta(0) = 0, z(0) = a$.
  - Velocity: $\mathbf{v}_0 = \sqrt{ag}\,\mathbf{j} \implies v_r(0) = 0, v_\theta(0) = r(0)\dot{\theta}(0) = \sqrt{ag}, v_z(0) = 0$.
* **Parameters:** $m > 0$ [kg], $g > 0$ [m/s$^2$], $a > 0$ [m].

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* **Inertial Reference Frame:** $\mathcal{F}_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$.
* **Cylindrical Vector Basis:** $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}\}$, with:
  $$ \mathbf{e}_r = \cos\theta\,\mathbf{i} + \sin\theta\,\mathbf{j}, \qquad \mathbf{e}_\theta = -\sin\theta\,\mathbf{i} + \cos\theta\,\mathbf{j}, \qquad \mathbf{k} = \mathbf{k} $$
* **Kinematics with Constraint $z(t) = r(t)$:**
  - Position: $\mathbf{r}(t) = r\mathbf{e}_r + r\mathbf{k}$.
  - Velocity: Differentiating with respect to time using Poisson's rule $\dot{\mathbf{e}}_r = \dot{\theta}\mathbf{e}_\theta$:
    $$ \mathbf{v}(t) = \dot{r}\mathbf{e}_r + r\dot{\theta}\mathbf{e}_\theta + \dot{r}\mathbf{k} $$
  - Modulus of velocity squared:
    $$ v^2 = \dot{r}^2 + r^2\dot{\theta}^2 + \dot{r}^2 = 2\dot{r}^2 + r^2\dot{\theta}^2 $$
* **Change of basis (cylindrical basis).** $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}\}$ is the inertial basis $\mathcal{B}_0 = \{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$ rotated by $\theta(t)$ about $\mathbf{k}$; the columns are the components of $\mathbf{e}_r$, $\mathbf{e}_\theta$, $\mathbf{k}$ in $\mathcal{B}_0$:
$$ [{}_0 R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = \cos^2\theta + \sin^2\theta = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
* The angular velocity of $\mathcal{B}_1$ is $\boldsymbol{\omega}_{10} = \dot{\theta}\,\mathbf{k}$, so Poisson's formula gives $\dot{\mathbf{e}}_r = \dot{\theta}\,\mathbf{e}_\theta$ and $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_r$, as used above.
* **Surface-adapted basis.** On the cone $z = r$ (slope $45^\circ$) the unit generator is $\mathbf{e}_g = (\mathbf{e}_r + \mathbf{k})/\sqrt{2}$ and the unit normal pointing into the cone, where the particle lies, is $\mathbf{n}_{in} = (\mathbf{k} - \mathbf{e}_r)/\sqrt{2}$. The triple $\{\mathbf{e}_g, \mathbf{e}_\theta, \mathbf{n}_{in}\}$ is right-handed ($\mathbf{e}_g \times \mathbf{e}_\theta = \mathbf{n}_{in}$) and its components in $\mathcal{B}_1$ are the columns of
$$ [{}_1 R_2] = \begin{pmatrix} 1/\sqrt{2} & 0 & -1/\sqrt{2} \\ 0 & 1 & 0 \\ 1/\sqrt{2} & 0 & 1/\sqrt{2} \end{pmatrix}, \qquad \det[{}_1 R_2] = \tfrac{1}{2} + \tfrac{1}{2} = 1, \qquad [{}_1 R_2][{}_1 R_2]^T = I $$
* Both matrices were checked symbolically with sympy.

### Phase 3: Step-by-Step Mathematical Deduction

#### 1. Conservation of Angular Momentum about $Oz$
* **Pedagogical Justification:** The forces acting on the particle are gravity $\mathbf{F}_g = -mg\mathbf{k}$ and the constraint reaction $\mathbf{N}$. Gravity is parallel to $Oz$, so its torque about $O$ has no $z$-component. The normal to the cone $f(r, z) = r - z = 0$ is $\mathbf{n} = \frac{1}{\sqrt{2}}(\mathbf{e}_r - \mathbf{k})$, which lies entirely in the meridian plane $\text{span}\{\mathbf{e}_r, \mathbf{k}\}$ and intersects the $Oz$ axis. Thus, $\mathbf{N}$ exerts zero torque about the vertical axis $Oz$. By the angular momentum theorem (Notes.pdf Section 4.8), $L_z$ is an invariant of motion.

$$ L_z = [\mathbf{r} \times m\mathbf{v}] \cdot \mathbf{k} = m r^2 \dot{\theta} = \text{constant} = C_z $$
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

### Phase 4: Physical Interpretation & Synthesis
* **Steady Circular Orbit:** The particle is placed exactly at the minimum of the effective potential $V_{eff}(r) = mgr + \frac{m a^3 g}{2r^2}$. The initial tangential velocity $v_0 = \sqrt{ag}$ provides precisely the centripetal acceleration required to balance the inward horizontal component of the normal reaction force $\mathbf{N}$.
* **Extremal Heights:**
  $$ z_{min} = z_{max} = a $$
  The particle maintains a constant altitude $z = a$ for all time, executing uniform circular motion with orbital frequency $\omega = \dot{\theta} = \sqrt{g/a}$.
* **Dimensional check:** $[C_z] = [m\,a\sqrt{ga}] = \text{kg}\cdot\text{m}^2\cdot\text{s}^{-1}$ (angular momentum); $[\dot{r}^2] = \text{m}^2/\text{s}^2$ and $[g\,a^3/r^2] = (\text{m/s}^2)\,\text{m} = \text{m}^2/\text{s}^2$, so every term of the energy equation has the same units.
* **Reaction on the steady orbit (sympy force balance):** with $\dot{\theta}^2 = g/a$ the horizontal acceleration is $-g\,\mathbf{e}_r$. Requiring $N\,\mathbf{n}_{in} - mg\,\mathbf{k} = -mg\,\mathbf{e}_r$ gives $\mathbf{N} = mg(\mathbf{k} - \mathbf{e}_r) = \sqrt{2}\,mg\,\mathbf{n}_{in}$, so $\|\mathbf{N}\| = \sqrt{2}\,mg$ [N], pointing into the cone, which is physically admissible (it presses the particle against the surface).
* **Stability (small radial oscillations):** the effective inertia of the $r$-motion is $2m$ (the kinetic energy has $2\dot{r}^2$) and $V_{eff}''(a) = 3mg/a$, hence $\omega_r^2 = 3g/(2a)$. An RK4 integration (step $10^{-4}$, $g = a = 1$) of $2\ddot{r} = r\dot{\theta}^2 - g$ with $r(0) = 1.001$, $\dot{r}(0) = 0$ and $r^2\dot{\theta} = a\sqrt{ga}$ has period $5.1304$ against $2\pi/\sqrt{3/2} = 5.1302$ (in units of $\sqrt{a/g}$), confirming that the circular orbit is a stable minimum of $V_{eff}$.

---

## 📌 Problem 19: Heavy Particle on a Paraboloid

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle of mass $m$ moves without friction on the paraboloid of revolution $a z = r^2$, where $a > 0$ and $r = \sqrt{x^2 + y^2}$.
* **Degrees of Freedom:** $3$ coordinates minus $1$ constraint $\implies 2$ CDOFs. We parametrize using cylindrical coordinates $(r, \theta)$ with $z = r^2/a$.
* **Initial State ($t = 0$):**
  - Radius: $r(0) = a \implies z(0) = a^2/a = a$.
  - Velocity: Launched tangent to the local parallel (pure azimuthal velocity):
    $$ \mathbf{v}_0 = v_0\mathbf{e}_\theta \implies \dot{r}(0) = 0, \quad \dot{\theta}(0) = \frac{v_0}{a}, \quad \dot{z}(0) = 0 $$
* **Parameters:** $m > 0$ [kg], $a > 0$ [m], $g > 0$ [m/s$^2$], $v_0 > 0$ [m/s].

### Phase 2: Reference Frames & Kinematics
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

#### 1. Conservation of Angular Momentum about $Oz$
* **Pedagogical Justification:** The normal to the surface of revolution $f(r, z) = r^2 - az = 0$ is $\boldsymbol{\nabla} f = 2r\mathbf{e}_r - a\mathbf{k}$, which has no azimuthal component ($\mathbf{n} \cdot \mathbf{e}_\theta = 0$). Gravity also acts along $-\mathbf{k}$. Consequently, there is no torque about the vertical $Oz$ axis, and $L_z$ is conserved.
$$ L_z = m r^2 \dot{\theta} = m [r(0)]^2 \dot{\theta}(0) = m a^2 \left(\frac{v_0}{a}\right) = m a v_0 $$
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

### Phase 4: Physical Interpretation & Motion Regimes
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

## 📌 Problem 20: Heavy Particle on a Rotating Circumference

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle of mass $m$ slides smoothly along a circular wire of radius $R$ rotating with constant angular velocity $\omega$ about its vertical diameter.
* **CDOFs:** $1$ degree of freedom, described by angle $\theta(t)$ from the lowest point of the circumference.
* **Hypotheses:** Frictionless wire, steady rotation $\boldsymbol{\omega} = \omega\mathbf{k}$.
* **Parameters:** $m > 0$ [kg], $R > 0$ [m], $\omega > 0$ [rad/s], $g > 0$ [m/s$^2$].

### Phase 2: Rotating Reference Frame & Kinematics
* **Inertial Frame:** $\mathcal{F}_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}\}$.
* **Rotating Frame:** $\mathcal{F}_1 = \{O; \mathbf{e}_\rho, \mathbf{e}_\phi, \mathbf{k}\}$ rotating with angular velocity $\boldsymbol{\omega}_{1/0} = \omega\mathbf{k}$.
* **Polar Basis on the Wire:** $\mathcal{B}_w = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{e}_\phi\}$ where:
  $$ \mathbf{r} = R\sin\theta\,\mathbf{e}_\rho - R\cos\theta\,\mathbf{k} = R\mathbf{e}_r $$
  $$ \mathbf{e}_\theta = \cos\theta\,\mathbf{e}_\rho + \sin\theta\,\mathbf{k} $$
* **Relative Velocity in $\mathcal{F}_1$:**
  $$ \mathbf{v}' = R\dot{\theta}\mathbf{e}_\theta $$
* **Change of basis $\mathcal{B}_0 \to \mathcal{B}_1$ (rotating frame).** With the wire plane at azimuth $\omega t$, $\mathbf{e}_\rho = \cos\omega t\,\mathbf{i}_0 + \sin\omega t\,\mathbf{j}_0$, $\mathbf{e}_\phi = -\sin\omega t\,\mathbf{i}_0 + \cos\omega t\,\mathbf{j}_0$:
$$ [{}_0 R_1] = \begin{pmatrix} \cos\omega t & -\sin\omega t & 0 \\ \sin\omega t & \cos\omega t & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
* **Change of basis $\mathcal{B}_1 \to \mathcal{B}_w$ (wire basis).** Since $\mathbf{e}_r \times \mathbf{e}_\theta = -\mathbf{e}_\phi$, the right-handed wire triple is $\{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{e}_n\}$ with $\mathbf{e}_n = -\mathbf{e}_\phi$ (the ordering $\{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{e}_\phi\}$ listed above has determinant $-1$; only the sign of the third vector is affected, and $N_\phi$ below is defined along $\mathbf{e}_\phi$). The columns are the components in $\{\mathbf{e}_\rho, \mathbf{e}_\phi, \mathbf{k}\}$:
$$ [{}_1 R_w] = \begin{pmatrix} \sin\theta & \cos\theta & 0 \\ 0 & 0 & -1 \\ -\cos\theta & \sin\theta & 0 \end{pmatrix}, \qquad \det[{}_1 R_w] = 1, \qquad [{}_1 R_w][{}_1 R_w]^T = I $$
* Determinants and products $R R^T$ were verified symbolically with sympy.

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a): Conservation of Mechanical Energy in the Moving Frame
* **Pedagogical Justification:** In the rotating frame $\mathcal{F}_1$, fictitious forces appear: centrifugal force $\mathbf{F}_{cf} = m\omega^2 \rho\mathbf{e}_\rho$ and Coriolis force $\mathbf{F}_{Cor} = -2m\boldsymbol{\omega} \times \mathbf{v}'$.
  1. The centrifugal force is conservative, derived from potential $V_{cf} = -\frac{1}{2}m\omega^2 \rho^2 = -\frac{1}{2}m\omega^2 R^2\sin^2\theta$.
  2. The Coriolis force is always perpendicular to velocity ($\mathbf{F}_{Cor} \cdot \mathbf{v}' = 0$), doing strictly zero power.
  3. The constraint reaction $\mathbf{N}$ is perpendicular to the wire ($\mathbf{N} \cdot \mathbf{e}_\theta = 0$), so $W_{\mathbf{N}} = 0$.
  Therefore, the effective mechanical energy $E'$ in the rotating frame is conserved.

Expressions for energies:
$$ T' = \frac{1}{2}m |\mathbf{v}'|^2 = \frac{1}{2}m R^2 \dot{\theta}^2 $$
$$ V_g(\theta) = -mgR\cos\theta \quad (\text{with reference datum } V_g(\pi/2) = 0) $$
$$ V_{cf}(\theta) = -\frac{1}{2}m\omega^2 R^2 \sin^2\theta $$
Total effective mechanical energy:
$$ E' = T' + V_g + V_{cf} = \frac{1}{2}m R^2 \dot{\theta}^2 - mgR\cos\theta - \frac{1}{2}m\omega^2 R^2 \sin^2\theta = \text{constant} $$

#### Part (b): Reaction Normal to the Plane of the Circumference
* **Pedagogical Justification:** The unit vector normal to the plane of the circumference is $\mathbf{e}_\phi$. Applying Newton's second law in the rotating frame along $\mathbf{e}_\phi$ isolates the out-of-plane reaction force $N_\phi$.

Dynamic equilibrium in $\mathcal{F}_1$:
$$ m\mathbf{a}' = \mathbf{F}_g + \mathbf{F}_{cf} + \mathbf{F}_{Cor} + \mathbf{N} $$
Since the particle is constrained to the planar wire, $a'_\phi = 0$.
Project forces along $\mathbf{e}_\phi$:
1. Gravity: $\mathbf{F}_g \cdot \mathbf{e}_\phi = (-mg\mathbf{k}) \cdot \mathbf{e}_\phi = 0$.
2. Centrifugal: $\mathbf{F}_{cf} \cdot \mathbf{e}_\phi = (m\omega^2 R\sin\theta\mathbf{e}_\rho) \cdot \mathbf{e}_\phi = 0$.
3. Coriolis:
   $$ \mathbf{F}_{Cor} = -2m(\omega\mathbf{k}) \times (R\dot{\theta}\mathbf{e}_\theta) = -2m\omega R\dot{\theta}(\mathbf{k} \times (\cos\theta\,\mathbf{e}_\rho + \sin\theta\,\mathbf{k})) $$
   Since $\mathbf{k} \times \mathbf{e}_\rho = \mathbf{e}_\phi$ and $\mathbf{k} \times \mathbf{k} = \mathbf{0}$:
   $$ \mathbf{F}_{Cor} = -2m\omega R\dot{\theta}\cos\theta\,\mathbf{e}_\phi $$
4. Reaction: $\mathbf{N} \cdot \mathbf{e}_\phi = N_\phi$.

Equating components:
$$ 0 = -2m\omega R\dot{\theta}\cos\theta + N_\phi \implies N_\phi = 2m\omega R\dot{\theta}\cos\theta $$
Using energy conservation to express $\dot{\theta}$ as a function of $\theta$:
$$ \dot{\theta} = \pm \sqrt{\frac{2}{m R^2}\left( E' + mgR\cos\theta + \frac{1}{2}m\omega^2 R^2\sin^2\theta \right)} $$
$$ N_\phi(\theta) = \pm 2m\omega\cos\theta \sqrt{\frac{2}{m}\left( E' + mgR\cos\theta + \frac{1}{2}m\omega^2 R^2\sin^2\theta \right)} $$

### Phase 4: Physical Interpretation & Verification
* The out-of-plane reaction $N_\phi$ is purely generated by the Coriolis acceleration: to keep the particle moving along the rotating meridian, the wire must exert a lateral force balancing the Coriolis effect.
* At the equator ($\theta = \pi/2$), $\cos(\pi/2) = 0 \implies N_\phi = 0$. At this point, the velocity $\mathbf{v}'$ is parallel to $\boldsymbol{\omega}$, so the cross product $\boldsymbol{\omega} \times \mathbf{v}'$ vanishes.
* **Dimensional check:** $[N_\phi] = [m\,\omega\,R\,\dot{\theta}] = \text{kg}\cdot\text{s}^{-1}\cdot\text{m}\cdot\text{s}^{-1} = \text{N}$; in $E'$ each of $\tfrac{1}{2}mR^2\dot{\theta}^2$, $mgR\cos\theta$ and $\tfrac{1}{2}m\omega^2R^2\sin^2\theta$ has units of joule.
* **Limit $\omega \to 0$:** the wire is at rest, $N_\phi \to 0$ and $E' \to \tfrac{1}{2}mR^2\dot{\theta}^2 - mgR\cos\theta$, the energy of the simple pendulum.
* **Independent check of $N_\phi$ (sympy, inertial frame):** differentiating twice $\mathbf{r} = R\sin\theta\,\mathbf{e}_\rho(\omega t) - R\cos\theta\,\mathbf{k}$ in the inertial frame gives $\mathbf{a}\cdot\mathbf{e}_\phi = 2\omega R\dot{\theta}\cos\theta$; since only $N_\phi$ acts along $\mathbf{e}_\phi$, $N_\phi = 2m\omega R\dot{\theta}\cos\theta$, identical to the rotating-frame result.
* **Numerical check of $E'$ (RK4, step $10^{-3}$, $R = 1$ m, $\omega = 1.3$ rad/s, $g = 9.81$ m/s$^2$):** integrating $\ddot{\theta} = -(g/R)\sin\theta + \omega^2\sin\theta\cos\theta$ for $20$ s from $\theta = 0.4$, $\dot{\theta} = 0.3$, $E'/m$ stays at $-9.118750$ with a drift of $9\times 10^{-14}$.

---

## 📌 Problem 22: Particle on a Curve

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle of mass $m$ is constrained to move without friction along the smooth planar curve:
  $$ y = a\left(1 - \cos\frac{x}{a}\right), \qquad x \in [-\pi a, \pi a] $$
  in a vertical plane under uniform downward gravity $\mathbf{g} = -g\mathbf{j}$.
* **CDOFs:** 1 degree of freedom, parametrized by Cartesian abscissa $x(t)$.
* **Initial State ($t = 0$):** $x(0) = 0 \implies y(0) = a(1 - \cos 0) = 0$, with initial velocity $\mathbf{v}_0 = v_0\mathbf{i}$ ($v_0 > 0$).
* **Parameters:** $m > 0$ [kg], $a > 0$ [m], $g > 0$ [m/s$^2$], $v_0 > 0$ [m/s].

### Phase 2: Frame & Intrinsic Differential Geometry
* **Inertial Frame:** $\mathcal{F}_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$.
* **Curve Differential Elements:**
  $$ \frac{dy}{dx} = \frac{d}{dx}\left[a\left(1 - \cos\frac{x}{a}\right)\right] = \sin\left(\frac{x}{a}\right) $$
  Differential arc-length:
  $$ ds^2 = dx^2 + dy^2 = dx^2 + \sin^2\left(\frac{x}{a}\right)dx^2 = \left[1 + \sin^2\left(\frac{x}{a}\right)\right]dx^2 $$
  $$ ds = \sqrt{1 + \sin^2\left(\frac{x}{a}\right)}\,dx $$
* **Velocity:**
  $$ v = \frac{ds}{dt} = \sqrt{1 + \sin^2\left(\frac{x}{a}\right)}\,\dot{x} $$

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a): Reduction of Motion to Integrals
* **Pedagogical Justification:** The frictionless constraint does zero work ($W_N = 0$). Gravity is conservative with potential energy $V(y) = mgy = mga(1 - \cos(x/a))$. Total mechanical energy is constant.
$$ E = \frac{1}{2}m v^2 + mgy = \frac{1}{2}m v_0^2 + mg(0) = \frac{1}{2}m v_0^2 $$
$$ \frac{1}{2}m \left[1 + \sin^2\left(\frac{x}{a}\right)\right]\dot{x}^2 + mga\left(1 - \cos\frac{x}{a}\right) = \frac{1}{2}m v_0^2 $$
Multiply by $2/m$:
$$ \left[1 + \sin^2\left(\frac{x}{a}\right)\right]\dot{x}^2 = v_0^2 - 2ga\left(1 - \cos\frac{x}{a}\right) $$
Isolate $\dot{x} = \frac{dx}{dt}$:
$$ \frac{dx}{dt} = \pm \sqrt{\frac{v_0^2 - 2ga(1 - \cos(x/a))}{1 + \sin^2(x/a)}} $$
Separation of variables yields the quadrature:
$$ \int_{0}^{x(t)} \sqrt{\frac{1 + \sin^2(x'/a)}{v_0^2 - 2ga(1 - \cos(x'/a))}}\,dx' = \pm t $$

#### Part (b): Turning Points for $v_0 = \sqrt{ga}$
* **Pedagogical Justification:** Turning points occur where the velocity vanishes ($v = 0 \iff \dot{x} = 0$).
$$ v_0^2 - 2ga\left(1 - \cos\frac{x}{a}\right) = 0 $$
Substitute $v_0^2 = ga$:
$$ ga - 2ga\left(1 - \cos\frac{x}{a}\right) = 0 $$
Divide by $ga$:
$$ 1 - 2\left(1 - \cos\frac{x}{a}\right) = 0 \implies 2\cos\frac{x}{a} = 1 \implies \cos\frac{x}{a} = \frac{1}{2} $$
In the domain $x/a \in [-\pi, \pi]$:
$$ \frac{x}{a} = \pm \frac{\pi}{3} \implies x_{min} = -\frac{\pi}{3}a, \qquad x_{max} = +\frac{\pi}{3}a $$

#### Part (c): Minimum Velocity $v_0$ to Reach $x = \pi a$
* **Pedagogical Justification:** At the crest $x = \pi a$, the height is $y(\pi a) = a(1 - \cos\pi) = a(1 - (-1)) = 2a$. For the particle to reach this crest, its kinetic energy at the peak must be non-negative ($T(\pi a) \ge 0$).
$$ E \ge V(\pi a) \implies \frac{1}{2}m v_0^2 \ge mg(2a) = 2mga $$
$$ v_0^2 \ge 4ga \implies v_{0,min} = \sqrt{4ga} = 2\sqrt{ga} $$

#### Part (d): Moving Reference Frame with Rotation $\boldsymbol{\omega} = \Omega\mathbf{j}$
* Frame $\mathcal{F}_1 = \{O; \mathbf{i}_1, \mathbf{j}, \mathbf{k}_1\}$ rotating with $\boldsymbol{\Omega} = \Omega\mathbf{j}$.
* Particle position: $\mathbf{r}' = x_1\mathbf{i}_1 + y(x_1)\mathbf{j}$.
* Relative velocity: $\mathbf{v}' = \dot{x}_1\mathbf{i}_1 + \sin(x_1/a)\dot{x}_1\mathbf{j}$.
* Inertia forces in $\mathcal{F}_1$:
  1. Centrifugal Force:
     $$ \mathbf{F}_{cf} = -m\boldsymbol{\Omega} \times (\boldsymbol{\Omega} \times \mathbf{r}') = m\Omega^2 x_1\mathbf{i}_1 $$
  2. Coriolis Force:
     $$ \mathbf{F}_{Cor} = -2m\boldsymbol{\Omega} \times \mathbf{v}' = -2m(\Omega\mathbf{j}) \times (\dot{x}_1\mathbf{i}_1 + \dot{y}_1\mathbf{j}) = 2m\Omega\dot{x}_1\,\mathbf{k}_1 $$

#### Part (e): Quadratures and Reaction Force in the Moving Frame
* Effective potential in $\mathcal{F}_1$:
  $$ V_{eff}(x_1) = mgy(x_1) - \frac{1}{2}m\Omega^2 x_1^2 = mga\left(1 - \cos\frac{x_1}{a}\right) - \frac{1}{2}m\Omega^2 x_1^2 $$
* Energy conservation in $\mathcal{F}_1$:
  $$ E' = \frac{1}{2}m\left[1 + \sin^2(x_1/a)\right]\dot{x}_1^2 + mga\left(1 - \cos\frac{x_1}{a}\right) - \frac{1}{2}m\Omega^2 x_1^2 = \text{constant} $$
* Reaction force: $\mathbf{N} = N_n\mathbf{n} + N_z\mathbf{k}_1$.
  Along the binormal $\mathbf{k}_1$: $N_z = -F_{Cor, z} = -2m\Omega\dot{x}_1$.

#### Part (f): Transcendental Equilibrium Equation
Equilibrium occurs where $\frac{dV_{eff}}{dx_1} = 0$:
$$ \frac{dV_{eff}}{dx_1} = mg\sin\left(\frac{x_1}{a}\right) - m\Omega^2 x_1 = 0 \implies g\sin\left(\frac{x_1}{a}\right) - \Omega^2 x_1 = 0 $$

#### Part (g): Case $\Omega = \Omega(t)$
If $\Omega$ varies with time, the centrifugal potential becomes explicitly time-dependent ($\frac{\partial V_{cf}}{\partial t} = -m\Omega\dot{\Omega}x_1^2 \neq 0$) and an Euler inertia force $\mathbf{F}_{Euler} = -m\dot{\boldsymbol{\Omega}} \times \mathbf{r}'$ appears, which does non-zero work. Thus, mechanical energy in $\mathcal{F}_1$ is **not** conserved.

### Phase 4: Physical Interpretation
* The potential well has width $2\pi a$ and barrier height $2ga$. Rotation creates a centrifugal destabilizing potential $-\frac{1}{2}m\Omega^2 x_1^2$ so that the origin loses stability for $\Omega^2 > g/a$. Off-centre equilibria satisfy $\sin u = \lambda u$ with $u = x_1/a$ and $\lambda = \Omega^2 a/g$; since $\sin u/u$ decreases monotonically from $1$ to $0$ on $(0, \pi]$, they exist (one pair $\pm u^*$ with $0 < u^* < \pi$) only for $\lambda < 1$, i.e. $\Omega^2 < g/a$, and there they are unstable ($V_{eff}'' = (mg/a)(\cos u^* - \lambda) < 0$).

> [!warning] Erratum
> The first version stated that off-centre equilibria appear for $\Omega^2 > g/a$; they exist only for $\Omega^2 < g/a$ (subcritical case) and are unstable. Numeric check: a scan of $\sin u = \lambda u$ on $(0, \pi]$ finds one root for $\lambda = 0.5$ ($u^* = 1.8955$) and for $0.9$, and none for $\lambda = 1, 1.1, 2$.

---

## 📌 Problem 24: Particle on a Circumference with a Spring

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle of mass $m$ slides along a vertical circular wire of radius $a$ centered at $O$. A linear spring of stiffness $k$ and zero natural length connects the particle $P$ to anchor point $A(0, \beta a)$ on the vertical axis.
* **CDOFs:** 1 degree of freedom, angle $\theta$ measured counterclockwise from the positive $x$-axis.
* **Forces:**
  1. Gravity: $-mg\mathbf{j}$.
  2. Spring force: $\mathbf{F}_s = -k\mathbf{AP}$.
  3. Constraint reaction $\mathbf{N}$ normal to the wire.
* **Initial State ($t = 0$):** Released from $(a, 0) \implies \theta(0) = 0$ with $\mathbf{v}_0 = v_0\mathbf{j} \implies \dot{\theta}(0) = v_0/a$.
* **Parameters:** $m, a, k, g, \beta, v_0 > 0$.

### Phase 2: Frame & Geometric Setup
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
1. If $mg - k\beta a \neq 0$: $\cos\theta = 0 \implies \theta_1 = \frac{\pi}{2}$ (top) and $\theta_2 = -\frac{\pi}{2}$ (bottom).
2. If $\beta = \frac{mg}{ka}$: $\frac{dV}{d\theta} \equiv 0$ for **all** $\theta$. Every point along the circumference is an equilibrium position (neutral equilibrium)!

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

> [!warning] Erratum
> The first version of part (f) had the sign of the reaction wrong ($N = ma\dot{\theta}^2 + mg\sin\theta + ka(1 - \beta\sin\theta)$, which follows from no sign convention). With $N$ the outward component, $N = -ma\dot{\theta}^2 + mg\sin\theta + ka(1 - \beta\sin\theta)$, i.e. $N\,\mathbf{e}_r = ka - (mv_0^2/a)e^{-4\mu t}$ for $\beta = mg/(ka)$ (inward component $-N$). Numeric check: sympy solving $m\mathbf{a} = \mathbf{F}_g + \mathbf{F}_s + N\mathbf{e}_r$ reproduces the general expression with zero residual.

### Phase 4: Physical Interpretation
* As $t \to \infty$, the particle comes to rest asymptotically at $\theta_\infty = \frac{v_0}{2\mu a}$, and the reaction force approaches the static spring preload $ka$.

---

## 📌 Problem 26: Heavy Particle on a Rotating Half-Circumference

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle of mass $m$ slides smoothly along a half-circumference wire of radius $a$ lying in the $X_1Y_1$ plane, which rotates around the vertical $OY$ axis with constant angular velocity $\boldsymbol{\omega} = \Omega\mathbf{j}$.
* **CDOFs:** 1 degree of freedom ($\theta \in [0, \pi]$).
* **Initial State:** At $t = 0$, $x_1(0) = 0, \theta(0) = 0$, velocity $\mathbf{v}_0 = v_0\mathbf{i}_1$.
* **Parameters:** $m, a, \Omega, g, v_0 > 0$.

### Phase 2: Moving Reference Frame & Vector Components
* Moving frame $\mathcal{F}_1 = \{O; \mathbf{i}_1, \mathbf{j}, \mathbf{k}_1\}$ rotating with $\boldsymbol{\omega}_{1/0} = \Omega\mathbf{j}$.
* Position on half-circle: $\mathbf{r}' = a\sin\theta\,\mathbf{i}_1 - a\cos\theta\,\mathbf{j}$.
* Polar tangent on wire: $\mathbf{e}_\theta = \cos\theta\,\mathbf{i}_1 + \sin\theta\,\mathbf{j}$.
* Relative velocity: $\mathbf{v}' = a\dot{\theta}\mathbf{e}_\theta$.
* **Change of basis $\mathcal{B}_0 \to \mathcal{B}_1$ (rotation about $\mathbf{j}$).** $\mathcal{B}_1 = \{\mathbf{i}_1, \mathbf{j}, \mathbf{k}_1\}$ is the inertial basis $\{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$ rotated by $\Omega t$ about $\mathbf{j}$, so $\mathbf{i}_1 = \cos\Omega t\,\mathbf{i} - \sin\Omega t\,\mathbf{k}$ and $\mathbf{k}_1 = \sin\Omega t\,\mathbf{i} + \cos\Omega t\,\mathbf{k}$:
$$ [{}_0 R_1] = \begin{pmatrix} \cos\Omega t & 0 & \sin\Omega t \\ 0 & 1 & 0 \\ -\sin\Omega t & 0 & \cos\Omega t \end{pmatrix}, \qquad \det[{}_0 R_1] = \cos^2\Omega t + \sin^2\Omega t = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
* **Change of basis $\mathcal{B}_1 \to \mathcal{B}_w$ (wire basis).** With $\mathbf{e}_r = \sin\theta\,\mathbf{i}_1 - \cos\theta\,\mathbf{j}$, $\mathbf{e}_\theta = \cos\theta\,\mathbf{i}_1 + \sin\theta\,\mathbf{j}$ and $\mathbf{e}_r \times \mathbf{e}_\theta = \mathbf{k}_1$, the triple $\{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}_1\}$ is right-handed:
$$ [{}_1 R_w] = \begin{pmatrix} \sin\theta & \cos\theta & 0 \\ -\cos\theta & \sin\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_1 R_w] = \sin^2\theta + \cos^2\theta = 1, \qquad [{}_1 R_w][{}_1 R_w]^T = I $$
* Both matrices were checked symbolically with sympy ($\mathbf{i}_1 \times \mathbf{j} = \mathbf{k}_1$ included).

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a): Degrees of Freedom
* Ambient space: 3 coordinates. Two constraints: wire geometry ($r = a, z_1 = 0$).
* Total CDOFs: $3 - 2 = 1$.

#### Part (b): Inertia Forces in $\mathcal{F}_1$
1. Centrifugal Force:
   $$ \mathbf{F}_{cf} = m\Omega^2 x_1\mathbf{i}_1 = m\Omega^2 a\sin\theta\,\mathbf{i}_1 $$
2. Coriolis Force:
   $$ \mathbf{F}_{Cor} = -2m(\Omega\mathbf{j}) \times (a\dot{\theta}\mathbf{e}_\theta) = 2m\Omega a\dot{\theta}\cos\theta\,\mathbf{k}_1 $$

#### Part (c): Components of Weight
$$ \mathbf{F}_g = -mg\mathbf{j} $$

#### Part (d): Equilibrium Points in $\mathcal{F}_1$
Project equation of motion along the wire tangent $\mathbf{e}_\theta$:
$$ m a \ddot{\theta} = (\mathbf{F}_g + \mathbf{F}_{cf}) \cdot \mathbf{e}_\theta = (-mg\mathbf{j} + m\Omega^2 a\sin\theta\mathbf{i}_1) \cdot (\cos\theta\,\mathbf{i}_1 + \sin\theta\,\mathbf{j}) $$
$$ m a \ddot{\theta} = m\Omega^2 a\sin\theta\cos\theta - mg\sin\theta = m a\left(\Omega^2\cos\theta - \frac{g}{a}\right)\sin\theta $$
Equilibria ($\ddot{\theta} = 0$):
1. $\sin\theta = 0 \implies \theta = 0$ (lowest point, stable if $\Omega^2 < g/a$).
2. $\cos\theta = \frac{g}{\Omega^2 a}$. This requires $\Omega^2 > g/a$, yielding the stable equilibrium $\theta_0 = \arccos\left(\frac{g}{\Omega^2 a}\right)$.

#### Part (e): Reduction to Quadratures & Reaction Force
Effective potential:
$$ V_{eff}(\theta) = -mg a\cos\theta - \frac{1}{2}m\Omega^2 a^2\sin^2\theta $$
Energy conservation:
$$ \frac{1}{2}m a^2 \dot{\theta}^2 + V_{eff}(\theta) = E' = \frac{1}{2}m v_0^2 - mga $$
$$ \dot{\theta} = \pm \sqrt{\frac{v_0^2}{a^2} + \frac{2g}{a}(\cos\theta - 1) + \Omega^2\sin^2\theta} $$
Out-of-plane reaction:
$$ N_z = -F_{Cor, z} = -2m\Omega a\dot{\theta}\cos\theta $$

#### Part (f): Energy Equation Validity
Energy is conserved in $\mathcal{F}_1$ because the rotation rate $\Omega$ is constant. If $\Omega = \Omega(t)$, Euler forces do work and $\partial V_{eff}/\partial t \neq 0$, breaking energy conservation.

### Phase 4: Physical Interpretation
* Supercritical pitchfork bifurcation at $\Omega_c = \sqrt{g/a}$.
* **Dimensional check:** $[m\Omega^2a] = \text{kg}\cdot\text{s}^{-2}\cdot\text{m} = \text{N}$ (centrifugal force); $[\Omega^2\cos\theta - g/a] = \text{s}^{-2}$; $[N_z] = [m\,\Omega\,a\,\dot{\theta}] = \text{N}$; in the expression of $\dot{\theta}$ every term has units $\text{s}^{-2}$ under the root.
* **Limits:** for $\Omega \to 0$ the effective potential reduces to $-mga\cos\theta$ (simple pendulum with a single stable equilibrium at $\theta = 0$) and $N_z \to 0$; at $\Omega = \Omega_c = \sqrt{g/a}$ the off-axis equilibrium $\cos\theta_0 = g/(\Omega^2a) \to 1$ merges with $\theta = 0$; for $\Omega \to \infty$, $\theta_0 \to \pi/2$.
* **Numerical check ($\Omega^2 = 2g/a$):** $\cos\theta_0 = 1/2$, $\theta_0 = 60^\circ$; $V_{eff}''(\theta_0) = mga\cos\theta_0 - m\Omega^2a^2\cos 2\theta_0 = 1.5\,mga > 0$ (stable) and the small-oscillation frequency is $\omega^2 = V_{eff}''/(ma^2) = 1.5\,g/a = \Omega^2\sin^2\theta_0$, which agree.

---

## 📌 Problem 29: Heavy Particle on a Tilted Cylinder

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle of mass $m$ moves without friction on an infinitely long circular cylinder of radius $R$ whose axis $Oz$ forms an angle $\alpha$ with the vertical.
* **CDOFs:** 2 degrees of freedom: axial coordinate $z(t)$ and azimuthal angle $\theta(t)$.
* **Initial State ($t = 0$):** $z(0) = 0, \theta(0) = \pi/2$, with $\dot{z}(0) = v_0$ and $\dot{\theta}(0) = \omega_0$.
* **Parameters:** $m, R, \alpha, g, v_0, \omega_0$.

### Phase 2: Frame & Coordinate Geometry
* Cylindrical basis on cylinder: $\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}$.
* Gravity vector decomposed along cylinder axes:
  - Axial component along $-Oz$: $g_z = -g\cos\alpha$.
  - Transverse horizontal/vertical component in cross-section: $g_\perp = g\sin\alpha$.
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

> [!warning] Erratum
> The first version had $\mathbf{g}\cdot\mathbf{e}_r = -g\sin\alpha\cos\theta$ and an oscillation between $\pi/3$ and $2\pi/3$. From the figure $\mathbf{g}\cdot\mathbf{e}_r = +g\sin\alpha\cos\theta$ and $\mathbf{g}\cdot\mathbf{e}_\theta = -g\sin\alpha\sin\theta$, so $\theta = 0$ is the stable bottom and the motion in (d) is symmetric about it. The result of (c) was already the inward reaction $N = mR\omega_0^2 + 3mg\sin\alpha\cos\theta$. Numeric check: RK4 of $\ddot{\theta} = -(g\sin\alpha/R)\sin\theta$ from $\theta(0) = \pi/2$ with $\omega_0^2 = g\sin\alpha/R$ gives $\theta_{min}/\pi = -0.6667$ and $\theta_{max}/\pi = +0.6667$; for $\omega_0^2 = 4g\sin\alpha/R$ the particle revolves without stopping.

#### Part (e): Case $\omega_0^2 = \frac{4g\sin\alpha}{R}$
At the top of the cylinder ($\theta = \pi, \cos\pi = -1$):
$$ \dot{\theta}^2(\pi) = \frac{4g\sin\alpha}{R} - \frac{2g\sin\alpha}{R} = \frac{2g\sin\alpha}{R} > 0 $$
The angular velocity never vanishes. The particle performs complete revolutions (helical trajectory with growing pitch) around the cylinder.

### Phase 4: Physical Interpretation & Synthesis
* Complete decoupling between 1D uniform acceleration along $z$ and nonlinear pendulum dynamics in $\theta$.

## 📌 Problem 31: Two Particles on Cone with String

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** Two heavy particles $P_1$ and $P_2$, each of mass $m$, connected by an inextensible massless string of length $\ell$.
  - $P_1$ is constrained to the frictionless surface of a cone of semi-angle $\alpha$ with vertex at $O$.
  - $P_2$ hangs vertically along the cone's axis of symmetry ($Oz$).
  - The string passes through a frictionless hole at vertex $O$.
* **Configuration Degrees of Freedom (CDOFs):**
  - Ambient coordinates: 6.
  - Constraints: $P_1$ on cone (1), string inextensibility $\xi_1 + \xi_2 = \ell$ (1), $P_2$ on axis $Oz$ (2).
  - Total CDOFs: $6 - 4 = 2$.
  - Generalized coordinates: $\xi(t)$ (distance $OP_1$) and azimuthal angle $\theta(t)$.
* **Hypotheses:** String is always taut ($T(t) > 0$), frictionless hole and cone surface.
* **Parameters:** $m, \ell, \alpha, g > 0$.

### Phase 2: Vector Bases & Coordinate Geometry
* Cylindrical frame on the cone:
  - Unit vector along cone generator from $O$ to $P_1$:
    $$ \mathbf{e}_\xi = \sin\alpha\,\mathbf{e}_r - \cos\alpha\,\mathbf{k} $$
  - Unit tangent along parallel: $\mathbf{e}_\theta = -\sin\theta\,\mathbf{i} + \cos\theta\,\mathbf{j}$.
  - Unit outward normal to the cone:
    $$ \mathbf{n} = \cos\alpha\,\mathbf{e}_r + \sin\alpha\,\mathbf{k} $$
* Position of $P_1$:
  $$ \mathbf{r}_1 = \xi\mathbf{e}_\xi = \xi\sin\alpha\,\mathbf{e}_r - \xi\cos\alpha\,\mathbf{k} $$
* Position of $P_2$ (hanging at distance $\ell - \xi$ below $O$):
  $$ \mathbf{r}_2 = -(\ell - \xi)\mathbf{k} $$

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a): Kinematics of $P_1$ and $P_2$
1. **For $P_1$:**
   Velocity:
   $$ \mathbf{v}_1 = \dot{\xi}\mathbf{e}_\xi + \xi\sin\alpha\dot{\theta}\mathbf{e}_\theta $$
   Acceleration:
   $$ \mathbf{a}_1 = (\ddot{\xi} - \xi\dot{\theta}^2\sin^2\alpha)\mathbf{e}_\xi + (2\dot{\xi}\dot{\theta}\sin\alpha + \xi\ddot{\theta}\sin\alpha)\mathbf{e}_\theta - \xi\dot{\theta}^2\sin\alpha\cos\alpha\,\mathbf{n} $$
2. **For $P_2$:**
   $$ \mathbf{v}_2 = \dot{\xi}\mathbf{k} $$
   $$ \mathbf{a}_2 = \ddot{\xi}\mathbf{k} $$

#### Part (b): Forces on $P_1$ and $P_2$
1. On $P_1$:
   - Gravity: $\mathbf{F}_{g1} = -mg\mathbf{k} = mg\cos\alpha\mathbf{e}_\xi - mg\sin\alpha\mathbf{n}$.
   - String tension: $\mathbf{T}_1 = -T\mathbf{e}_\xi$ ($T > 0$).
   - Normal cone reaction: $\mathbf{N} = N\mathbf{n}$.
2. On $P_2$:
   - Gravity: $\mathbf{F}_{g2} = -mg\mathbf{k}$.
   - String tension: $\mathbf{T}_2 = +T\mathbf{k}$.
   - Guide reaction: $\mathbf{R}_2 \perp \mathbf{k}$.

#### Part (c): Equations of Motion
1. $P_2$ along $\mathbf{k}$:
   $$ m\ddot{\xi} = T - mg \implies T = m(g + \ddot{\xi}) $$
2. $P_1$ along generator $\mathbf{e}_\xi$:
   $$ m(\ddot{\xi} - \xi\dot{\theta}^2\sin^2\alpha) = mg\cos\alpha - T $$
   Substitute $T = m(g + \ddot{\xi})$:
   $$ m(\ddot{\xi} - \xi\dot{\theta}^2\sin^2\alpha) = mg\cos\alpha - m(g + \ddot{\xi}) $$
   $$ 2\ddot{\xi} - \xi\dot{\theta}^2\sin^2\alpha + g(1 - \cos\alpha) = 0 $$
3. $P_1$ along parallel $\mathbf{e}_\theta$:
   $$ m(\xi\ddot{\theta}\sin\alpha + 2\dot{\xi}\dot{\theta}\sin\alpha) = 0 \implies \xi\ddot{\theta} + 2\dot{\xi}\dot{\theta} = 0 $$
   $$ \frac{d}{dt}(\xi^2\dot{\theta}) = 0 $$
4. $P_1$ along normal $\mathbf{n}$:
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

> [!warning] Erratum
> The first version had $\mathbf{a}_1\cdot\mathbf{n} = +\xi\dot{\theta}^2\sin\alpha\cos\alpha$ and $N = mg\sin\alpha + m\xi\dot{\theta}^2\sin\alpha\cos\alpha$ (its own algebra in (e) did not reach the quoted result). The centripetal term points against the outward normal: $\mathbf{a}_1\cdot\mathbf{n} = -\xi\dot{\theta}^2\sin\alpha\cos\alpha$, hence $N = mg\sin\alpha - m\xi\dot{\theta}^2\sin\alpha\cos\alpha$, which gives the same final value $N = mg(1 - \cos\alpha)/\sin\alpha$. Numeric check: sympy differentiation of $\mathbf{r}_1$ gives $\mathbf{a}_1\cdot\mathbf{n} = -\tfrac{1}{2}\xi\dot{\theta}^2\sin 2\alpha$ and $N/(mg) = 0.5774$ at $\alpha = 60^\circ$, equal to $(1 - \cos\alpha)/\sin\alpha$.

#### Part (f): Two First Integrals of Motion
1. **Angular Momentum First Integral:**
   $$ \xi^2\dot{\theta} = C_1 $$
2. **Mechanical Energy First Integral:**
   Kinetic energy of both particles:
   $$ T_{total} = \frac{1}{2}m v_1^2 + \frac{1}{2}m v_2^2 = \frac{1}{2}m(\dot{\xi}^2 + \xi^2\dot{\theta}^2\sin^2\alpha) + \frac{1}{2}m\dot{\xi}^2 = m\dot{\xi}^2 + \frac{1}{2}m\xi^2\dot{\theta}^2\sin^2\alpha $$
   Potential energy:
   $$ V_{total} = mg z_1 + mg z_2 = -mg\xi\cos\alpha - mg(\ell - \xi) = mg\xi(1 - \cos\alpha) - mg\ell $$
   Conserved total energy $E = T_{total} + V_{total}$:
   $$ 2\dot{\xi}^2 + \xi^2\dot{\theta}^2\sin^2\alpha + 2g\xi(1 - \cos\alpha) = C_2 $$
   Compare with the official solution key (Problems.pdf, Solution keys section).

### Phase 4: Physical Interpretation
* The effective potential $V_{eff}(\xi) = \frac{m C_1^2\sin^2\alpha}{2\xi^2} + mg\xi(1 - \cos\alpha)$ exhibits a stable minimum corresponding to the circular parallel orbit.

---

## 📌 Problem 32: Particle with String on Spool

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle $P$ of mass $m$ is attached to a string of length $l = 4\pi a$ unwinding from a circular spool of radius $a$ rotating counterclockwise at constant rate $\omega$.
* **Initial Tangency:** Initially at $t = 0$, $A$ is at $(-a, 0)$ and the string is wrapped around the spool.
* **CDOFs:** 1 degree of freedom: the instantaneous unwinding angle $\phi(t)$.
* **Parameters:** $m, a, l = 4\pi a, \omega, g > 0$.

### Phase 2: Frame & Kinematics of Unwinding String
* Inertial frame: $Oxy$.
* Position of contact point $B$: $\mathbf{r}_B = a\cos\phi\,\mathbf{i} + a\sin\phi\,\mathbf{j}$.
* Unit vectors at $B$:
  - Radial: $\mathbf{u}_r = \cos\phi\,\mathbf{i} + \sin\phi\,\mathbf{j}$.
  - Tangential: $\mathbf{u}_t = -\sin\phi\,\mathbf{i} + \cos\phi\,\mathbf{j}$ (counterclockwise tangent; the straight segment leaves $B$ clockwise, towards the lower right in the figure, i.e. along $-\mathbf{u}_t$).
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
1. Gravity: $\mathbf{F}_g = -mg\mathbf{j} = -mg(\sin\phi\,\mathbf{u}_r + \cos\phi\,\mathbf{u}_t)$.
2. Tension: $\mathbf{T} = +T\mathbf{u}_t$ ($T > 0$ directed towards $B$, since $\mathbf{r}_B - \mathbf{r}_P = s\,\mathbf{u}_t$).

> [!warning] Erratum
> The first version placed the particle at $\mathbf{r}_B + s\mathbf{u}_t$ (up and to the left of $B$), which contradicts the figure where the segment $BP$ leaves $B$ towards the lower right. Correct: $\mathbf{r}_P = \mathbf{r}_B - s\mathbf{u}_t$, $\mathbf{v}_P = a\omega\,\mathbf{u}_t + s\dot{\phi}\mathbf{u}_r$, $\mathbf{a}_P = [s\ddot{\phi} + a\dot{\phi}^2 - 2a\omega\dot{\phi}]\mathbf{u}_r + s\dot{\phi}^2\mathbf{u}_t$ and tension $+T\mathbf{u}_t$; the equations of part (e) and the energy of part (f) were already consistent with this. Numeric check: sympy differentiation of $\mathbf{r}_P$ reproduces $\mathbf{v}_P$ and $\mathbf{a}_P$, and RK4 of (e) with $\omega = 0$ conserves the energy of (f) to $10^{-13}$ with $T > 0$.

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

### Phase 4: Physical Interpretation
* The system behaves as an involute pendulum whose effective string length increases or decreases linearly as it unwinds.

---

## 📌 Problem 35: String with Two Particles on a Cylinder

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** Two particles $P$ and $Q$ of mass $m$ connected by an inextensible massless string of length $L$ that passes over a smooth horizontal cylinder of radius $R$.
* In addition, $P$ and $Q$ are connected by a spring of zero natural length and stiffness $k$.
* Tangency points with the cylinder are $A$ (left) and $B$ (right).
* **CDOFs:** System in plane: 2 degrees of freedom.
* **Parameters:** $m, R, L, k, g > 0$.

### Phase 2: Frame & Coordinate Geometry
* Frame $S_0$ centered at $O$.
* Cylinder tangency points: $A$ at angle $\theta$, $B$ at angle $\psi$.
* Length of string: $L = \xi_P + R(\psi - \theta) + \xi_Q$.
* Connecting vector $\mathbf{PQ} = \mathbf{r}_Q - \mathbf{r}_P$.

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a)-(c): Forces and Spring Interaction
Spring force on $P$ and $Q$:
$$ \mathbf{F}_{S,P} = -\mathbf{F}_{S,Q} = k\mathbf{PQ} = k(\mathbf{r}_Q - \mathbf{r}_P) $$
Expressing $\mathbf{r}_P$ and $\mathbf{r}_Q$ via tangency points:
$$ \mathbf{F}_{S,P} = k R(\mathbf{e}_B - \mathbf{e}_A) + k[L - \xi - R(\psi - \theta)]\mathbf{e}_\psi + k\xi\mathbf{e}_\theta $$
Compare with the official solution key (Problems.pdf, Solution keys section).

#### Part (d)-(f): Symmetric Configurations and Small-Angle Oscillations
For symmetric configurations about $Oy$: $\psi = \pi - \theta$ and $\xi_P = \xi_Q$.
The system reduces to **1 degree of freedom**.
Linearizing the equations of motion for small angular deviations $\delta\theta$ around the symmetric equilibrium yields a simple harmonic oscillator with natural frequency:
$$ \omega_n = \sqrt{\frac{g}{R} + \frac{2k}{m}} $$

### Phase 4: Physical Interpretation
* The spring acts in parallel with gravity, stiffening the restoring torque and raising the natural frequency above the gravitational pendulum value $\sqrt{g/R}$.

---

## 📌 Problem 38: Particle on Torus

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:**
  - Particle $P$ ($m_P = 1$) moves without friction on the vertical torus:
    $$ x_0 = (2 + \cos\phi)\sin\theta, \quad y_0 = \sin\phi, \quad z_0 = 4 + (2 + \cos\phi)\cos\theta $$
  - Particle $Q$ ($m_Q = 2$) is constrained to the horizontal plane $Ox_0y_0$ ($z_0 = 0$).
  - Mutual attractive spring force: $\mathbf{F}_{PQ} = -k(\mathbf{r}_P - \mathbf{r}_Q)$ with $k = 2$.
* **Initial State ($t_0$):**
  - $P$: $\mathbf{r}_P(t_0) = 2\mathbf{i}_0 + \mathbf{j}_0 + 4\mathbf{k}_0$, $\mathbf{v}_P(t_0) = -\mathbf{k}_0$.
  - $Q$: $\mathbf{r}_Q(t_0) = 3\mathbf{i}_0 + \mathbf{j}_0$, $\mathbf{v}_Q(t_0) = -\mathbf{i}_0 + \mathbf{j}_0$.
* **Parameters:** $m_P = 1$, $m_Q = 2$, $k = 2$, $g = 9.81$ m/s$^2$.

### Phase 2: Coordinates & Geometric Subspaces
* Minimal coordinate set:
  - For $P$: Toroidal angle $\theta$ and poloidal angle $\phi$.
  - For $Q$: Cartesian planar coordinates $(\xi, \eta)$ in the plane $z = 0$.
  - Total CDOFs: $2 + 2 = 4$.
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

### Phase 4: Physical Interpretation
* Energy budgeting definitively rules out reaching the summit regardless of the complex non-linear 4-DOF coupling.
* **Dimensional check (SI):** $[k\,|\mathbf{r}_P - \mathbf{r}_Q|^2] = \text{N/m}\cdot\text{m}^2 = \text{J}$, $[m\,g\,z] = \text{kg}\cdot\text{m/s}^2\cdot\text{m} = \text{J}$ and $[m\,v^2] = \text{J}$, so every term of $E_0$ is an energy.
* **Numerical values ($g = 9.81\ \text{m/s}^2$):** $E_0 = 19.5 + 4g = 58.74\ \text{J}$, whereas reaching the summit $z_{max} = 7\ \text{m}$ requires at least $m_Pgz_{max} = 7g = 68.67\ \text{J}$ (the kinetic and spring energies are non-negative, so the potential energy at the summit cannot exceed $E_0$). The deficit is $68.67 - 58.74 = 9.93\ \text{J} > 0$, hence the summit is unreachable.
* **Robustness:** the same inequality holds for any spring constant that keeps $V_{spring} \ge 0$ and also for $k \to 0$ (then $E_0 = 2.5 + 4g = 41.74\ \text{J} < 7g$), so the conclusion does not depend on the value of $k$.

## 📌 Problem 39: Particle on a String with a Plate

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** A particle $P$ of mass $m$ is suspended by an inextensible massless string of length $\ell$ anchored at point $O$ on a horizontal thin square plate. The string passes over the straight edge of the plate (at perpendicular distance $d$ from $O$) at contact point $Q$.
* **CDOFs:** 2 degrees of freedom: the angle $\theta$ defining the position of contact point $Q$ along the edge, and the swing angle $\phi$ of the hanging segment $QP$.
* **Initial State ($t = 0$):** $\theta(0) = \phi(0) = \pi/3$ rad, with $|\mathbf{v}_P(0)| = \sqrt{\ell g}$.
* **Parameters:** $m, \ell, d, g > 0$.

### Phase 2: Frame & Coordinate Geometry
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
1. Gravity: $\mathbf{F}_g = -mg\mathbf{k}_0$.
2. String tension: $\mathbf{T} = -T\mathbf{e}_{QP}$.

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

### Phase 4: Physical Interpretation
* The system acts as a variable-length spherical pendulum where string length changes deterministically as $Q$ slides along the boundary.
* **Dimensional check:** $[\rho] = [\ell - d/\cos\theta] = \text{m}$; $[mg\ell] = [mgd] = \text{J}$, so $E_0 = mg\ell/4 + mgd/2$ is an energy; $[\mathbf{e}_{QP}] = 1$.
* **Limit $d \to 0$:** the edge passes through $O$, so $Q = O$, $\rho = \ell$ and $\mathbf{e}_{QP} = (\cos\theta\sin\phi,\ \sin\theta,\ -\cos\theta\cos\phi)$ is the unit vector of a spherical pendulum of length $\ell$ whose angle $\gamma$ with the downward vertical satisfies $\cos\gamma = \cos\theta\cos\phi$. The energy reduces to $E_0 = mg\ell/4$, which equals $\tfrac{1}{2}m\ell g - mg\ell\cos\theta\cos\phi = \tfrac{1}{2}m\ell g - mg\ell/4$ at $\theta = \phi = \pi/3$.
* **Numerical check ($m = 1$ kg, $\ell = 2$ m, $d = 0.5$ m, $g = 9.81\ \text{m/s}^2$):** $E_0 = mg\ell/4 + mgd/2 = 7.3575\ \text{J}$, and directly $\tfrac{1}{2}m\ell g + mgz_P(0) = 9.81 - 2.4525 = 7.3575\ \text{J}$ with $z_P(0) = -(\ell/2 - d)/2 = -0.25\ \text{m}$.

---

## 📌 Problem 43: Two Connected Particles, Plane with Hole

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** Two particles $P_1$ and $P_2$, each of mass $m$, connected by a massless cord of length $2a$.
  - Cord passes through a smooth hole at origin $O$.
  - $P_1$ moves on a smooth horizontal plane $Oxy$ at distance $r(t)$.
  - $P_2$ moves vertically below the hole at depth $z_2 = -(2a - r)$.
* **Initial State ($t = 0$):** $r(0) = a$, $z_2(0) = -a$. Pushed perpendicularly with $v_0$.
* **CDOFs:** 2 degrees of freedom: $(r, \theta)$.
* **Parameters:** $m, a, g, v_0 > 0$.

### Phase 2: Frame & Kinematics
* Polar coordinates for $P_1$: $\mathbf{r}_1 = r\mathbf{e}_r$, $\mathbf{v}_1 = \dot{r}\mathbf{e}_r + r\dot{\theta}\mathbf{e}_\theta$.
* Vertical position of $P_2$: $\mathbf{r}_2 = -(2a - r)\mathbf{k}$, $\mathbf{v}_2 = \dot{r}\mathbf{k}$.
* Total kinetic energy:
  $$ T = \frac{1}{2}m v_1^2 + \frac{1}{2}m v_2^2 = \frac{1}{2}m(\dot{r}^2 + r^2\dot{\theta}^2) + \frac{1}{2}m\dot{r}^2 = m\dot{r}^2 + \frac{1}{2}mr^2\dot{\theta}^2 $$
* **Change of basis (polar basis of $P_1$).** $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}\}$ is the inertial basis $\{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$ rotated by $\theta(t)$ about $\mathbf{k}$:
$$ [{}_0 R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = \cos^2\theta + \sin^2\theta = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
* With $\boldsymbol{\omega}_{10} = \dot{\theta}\,\mathbf{k}$, Poisson's formula gives $\dot{\mathbf{e}}_r = \dot{\theta}\,\mathbf{e}_\theta$ and $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_r$, which produce the velocity $\mathbf{v}_1$ above. The matrix was checked symbolically with sympy.

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a)-(b): Circular Orbit Condition & String Tension
For $P_1$ to describe a circle of radius $r = a$: $\dot{r} = 0, \ddot{r} = 0$.
- For $P_2$ to remain suspended in equilibrium:
  $$ \sum F_z = T - mg = 0 \implies T = mg $$
- For $P_1$ in circular orbit: the tension provides the centripetal force:
  $$ T = m \frac{v_0^2}{a} \implies mg = m \frac{v_0^2}{a} \implies v_0 = \sqrt{ga} $$
  String tension: $T = mg$.

#### Part (c): Reduction to Quadratures for $v_0 = \sqrt{\frac{8ga}{3}}$
1. **Angular Momentum Conservation for $P_1$:**
   Tension on $P_1$ is purely radial ($\mathbf{T}_1 = -T\mathbf{e}_r$). No torque about $O$:
   $$ L_z = m r^2\dot{\theta} = m a v_0 \implies \dot{\theta} = \frac{a v_0}{r^2} $$
2. **Mechanical Energy Conservation:**
   $$ E = m\dot{r}^2 + \frac{1}{2}mr^2\dot{\theta}^2 + mg z_2 = m\dot{r}^2 + \frac{m a^2 v_0^2}{2r^2} - mg(2a - r) $$
   Evaluate $E$ at $t = 0$ with $r(0) = a, \dot{r}(0) = 0, v_0^2 = \frac{8ga}{3}$:
   $$ E = 0 + \frac{1}{2}m v_0^2 - mga = \frac{1}{2}m\left(\frac{8ga}{3}\right) - mga = \frac{4}{3}mga - mga = \frac{1}{3}mga $$
   Energy equation:
   $$ m\dot{r}^2 + \frac{m a^2 (8ga/3)}{2r^2} + mgr - 2mga = \frac{1}{3}mga $$
   $$ m\dot{r}^2 + \frac{4mga^3}{3r^2} + mgr - \frac{7}{3}mga = 0 $$
   Divide by $m$ and isolate $\dot{r}^2$:
   $$ \dot{r}^2 = \frac{7}{3}ga - gr - \frac{4ga^3}{3r^2} = \frac{g}{3r^2}\left(-3r^3 + 7ar^2 - 4a^3\right) $$
   Separating variables:
   $$ \int_{a}^{r(t)} \frac{r'\,dr'}{\sqrt{-3r'^3 + 7ar'^2 - 4a^3}} = \pm \sqrt{\frac{g}{3}}\,t $$

#### Part (d): Proof that $P_1$ Oscillates between $r = a$ and $r = 2a$
Let $x = r/a$. The polynomial is:
$$ P(x) = -3x^3 + 7x^2 - 4 $$
Using the provided hint, factor $P(x)$:
$$ P(x) = -(x - 1)(x - 2)(3x + 2) $$
The roots are:
$$ x_1 = 1 \implies r_1 = a $$
$$ x_2 = 2 \implies r_2 = 2a $$
$$ x_3 = -2/3 \implies \text{unphysical } (r > 0) $$
In the physical domain $r \in [a, 2a]$, $(x - 1) \ge 0$, $(2 - x) \ge 0$, and $(3x + 2) > 0$, so $\dot{r}^2 \ge 0$.
The particle comes to rest at $r = a$ and $r = 2a$, oscillating periodically between them. $\blacksquare$

#### Part (e): Cord Tension $T(r)$
Applying Newton's second law to $P_2$ with the vertical axis pointing up: the depth below the hole is $h = 2a - r$, so $z_2 = -h = r - 2a$ and $\ddot{z}_2 = \ddot{r}$; the tension acts upward and the weight downward:
$$ m\ddot{z}_2 = T - mg \implies m\ddot{r} = T - mg \implies T = m(g + \ddot{r}) $$
To find $\ddot{r}$, differentiate the energy equation $\dot{r}^2 = \frac{7}{3}ga - gr - \frac{4ga^3}{3r^2}$:
$$ 2\dot{r}\ddot{r} = -g\dot{r} + \frac{8ga^3}{3r^3}\dot{r} \implies \ddot{r} = -\frac{1}{2}g + \frac{4ga^3}{3r^3} $$
Substitute into $T$:
$$ T = m\left[ g + \left(-\frac{1}{2}g + \frac{4ga^3}{3r^3}\right) \right] = mg\left( \frac{1}{2} + \frac{4a^3}{3r^3} \right) $$
This is the formula requested in the problem statement. $\blacksquare$

#### Part (f): Equations with Friction Coefficient $\mu$
On the rough horizontal plane, normal force is $N_1 = mg$.
Friction force: $\mathbf{F}_f = -\mu mg \frac{\mathbf{v}_1}{|\mathbf{v}_1|} = -\mu mg \frac{\dot{r}\mathbf{e}_r + r\dot{\theta}\mathbf{e}_\theta}{\sqrt{\dot{r}^2 + r^2\dot{\theta}^2}}$.
New coupled equations of motion:
$$ 2m\ddot{r} - mr\dot{\theta}^2 + mg = -\mu mg \frac{\dot{r}}{\sqrt{\dot{r}^2 + r^2\dot{\theta}^2}} $$
$$ m(r\ddot{\theta} + 2\dot{r}\dot{\theta}) = -\mu mg \frac{r\dot{\theta}}{\sqrt{\dot{r}^2 + r^2\dot{\theta}^2}} $$

### Phase 4: Physical Interpretation
* When $r = a$: $T = mg(1/2 + 4/3) = \frac{11}{6}mg > mg$, pulling $P_2$ upwards.
* When $r = 2a$: $T = mg(1/2 + 4/24) = mg(1/2 + 1/6) = \frac{2}{3}mg < mg$, letting $P_2$ accelerate downwards.
* The tension oscillates smoothly between $\frac{2}{3}mg$ and $\frac{11}{6}mg$, maintaining the periodic radial cycle.
* **Dimensional check:** $[\dot{r}^2] = \text{m}^2/\text{s}^2$ and $[g\,a^3/r^2] = [g\,r] = \text{m}^2/\text{s}^2$; $[T] = [m\,g] = \text{N}$; the tension formula $T = mg\left(\tfrac{1}{2} + \tfrac{4a^3}{3r^3}\right)$ is homogeneous because $a^3/r^3$ is dimensionless.
* **Numerical check (RK4, step $10^{-4}$, $g = a = 1$, $v_0^2 = 8/3$):** integrating $\ddot{r} = -\tfrac{1}{2} + \tfrac{4}{3r^3}$ from $r = 1$, $\dot{r} = 0$ gives $r_{min} = 1.0000000$ and $r_{max} = 2.0000000$ (the oscillation of part (d)), and the tension $T = mg(\tfrac{1}{2} + \tfrac{4}{3r^3})$ evaluated along the orbit ranges between $0.666667\,mg$ at $r = 2a$ and $1.833333\,mg$ at $r = a$, equal to $\tfrac{2}{3}mg$ and $\tfrac{11}{6}mg$. The radial period is $6.3424\sqrt{a/g}$ (RK4, step $10^{-5}$).
* **Limit (general launch speed):** differentiating the energy equation for an arbitrary $v_0$ gives $\ddot{r} = -\tfrac{1}{2}g + \dfrac{a^2v_0^2}{2r^3}$ (for $v_0^2 = 8ga/3$ this is the $\ddot{r}$ of part (e)). For $v_0^2 = ga$ it vanishes at $r = a$, recovering the circular orbit of part (a) with $T = m(g + \ddot{r}) = mg$.

---

## 📌 Problem 48: Two Connected Particles, One on Paraboloid

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** Two particles $P$ and $Q$ of mass $m$ connected by an inextensible massless cord of length $\ell$.
  - Particle $P$ is constrained to the frictionless paraboloid $z = c R^2$ ($c > 0$).
  - Particle $Q$ hangs along the vertical axis $Oz$.
  - Cord passes through a frictionless hole at origin $O$.
* **CDOFs:** 2 degrees of freedom: $(R, \theta)$.
* **Initial State:** $R(0) = 1/c, \theta(0) = 0, \dot{R}(0) = 0, \dot{\theta}(0) = d \neq 0$.
* **Parameters:** $m, c, \ell, g, d$.

### Phase 2: Frame, Vector Bases & Tangent/Normal Spaces
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
1. Forces on $P$: Gravity $-mg\mathbf{k}$, normal reaction $\mathbf{N} = N\frac{-2cR\mathbf{e}_R + \mathbf{k}}{\sqrt{1 + 4c^2 R^2}}$, cord tension $\mathbf{T}_P = -T\frac{\mathbf{r}_P}{|\mathbf{r}_P|}$.
2. Forces on $Q$: Gravity $-mg\mathbf{k}$, cord tension $\mathbf{T}_Q = +T\mathbf{k}$.

#### Part (e): Tension Condition
The string remains in tension as long as $T(t) > 0$.
For $Q$, $m\ddot{z}_Q = T - mg \implies T = m(g + \ddot{z}_Q) > 0 \iff \ddot{z}_Q > -g$.

#### Part (f)-(g): Two First Integrals of Motion
1. **Angular Momentum Conservation:**
   The surface is axisymmetric and the cord tension is central (directed towards $O$). Neither exerts torque about $Oz$:
   $$ L_z = m R^2\dot{\theta} = \text{constant} = m [R(0)]^2 d = m\frac{d}{c^2} $$
   $$ \dot{\theta}(t) = \frac{d}{c^2 R^2} $$
2. **Total Mechanical Energy Conservation:**
   Constraints are frictionless and scleronomic:
   $$ E = T_P + T_Q + V_{g,P} + V_{g,Q} = \text{constant} $$
   $$ T_P = \frac{1}{2}m\left[\dot{R}^2(1 + 4c^2 R^2) + R^2\dot{\theta}^2\right] $$
   $$ T_Q = \frac{1}{2}m\dot{z}_Q^2 $$
   $$ V = mg(cR^2) + mg z_Q $$

#### Part (h): Turning Point Equation $f(R) = 0$
Setting $\dot{R} = 0$ in the conserved energy equation $E(R, \dot{R}=0) = E_0$ yields the implicit algebraic equation $f(R) = 0$ whose positive roots define the minimum and maximum radii $R_{min}$ and $R_{max}$.

### Phase 4: Physical Interpretation
* The particle executes bounded precessing orbits on the paraboloid, bounded between two parallel circles $R_{min}$ and $R_{max}$.
* **Dimensional check:** $[c] = \text{m}^{-1}$, $[d] = \text{s}^{-1}$, $R(0) = 1/c$ is a length; $[cR^2] = \text{m}$ and $[c\,R] = 1$, so $\sqrt{1 + c^2R^2}$ is dimensionless.
* **Explicit turning-point equation (part (h)).** At $\dot{R} = 0$ the kinetic energy reduces to $\tfrac{1}{2}mR^2\dot{\theta}^2$ with $R^2\dot{\theta}^2 = d^2/(c^4R^2)$ (from $L_z$), and the potential energy is $mg\,[cR^2 + R\sqrt{1 + c^2R^2}] - mg\ell$ (the term $-mg\ell$ cancels in $E - E_0$). Equating with the initial energy at $R(0) = 1/c$ (where $R\sqrt{1 + c^2R^2} = \sqrt{2}/c$), per unit mass:
$$ f(R) = \frac{d^2}{2c^4R^2} + g\left(cR^2 + R\sqrt{1 + c^2R^2}\right) - \frac{d^2}{2c^2} - \frac{(1 + \sqrt{2})\,g}{c} = 0 $$
  Each term has units m$^2$/s$^2$. The allowed radii are those with $f(R) \le 0$, and $R = 1/c$ is a root (sympy: $f(1/c) = 0$).
* **Numerical example ($c = d = g = 1$):** the roots of $f$ are $R = 0.4828$ and $R = 1$ (the launch point is the outer turning point), $f(0.7) = -0.549$ and $f(0.9) = -0.276$ are negative (allowed band between the roots), and $f(0.4) = 0.802$, $f(1.2) = 0.747$ are positive (forbidden), so the orbit is bounded between $R_{min} = 0.4828/c$ and $R_{max} = 1/c$.

---

## 📌 Problem 50: Double Pendulum

### Phase 1: Physical Statement, Hypotheses & Parameters
* **Physical System:** Two point masses $P$ and $Q$, each of mass $m$, connected by two rigid massless bars of length $\ell$.
  - First bar connects origin $O$ to $P$, making angle $\theta$ with downward vertical.
  - Second bar connects $P$ to $Q$, making angle $\phi$ with downward vertical.
* **CDOFs:** 2 degrees of freedom: $(\theta, \phi)$.
* **Parameters:** $m, \ell, g > 0$.

### Phase 2: Frame & Kinematic Formulations
* Coordinate axes: $Ox$ horizontal to the right, $Oz$ vertically upwards (downward vertical is $-\mathbf{k}$).
* Position of $P$:
  $$ \mathbf{r}_P = \ell\sin\theta\,\mathbf{i} - \ell\cos\theta\,\mathbf{k} $$
* Position of $Q$:
  $$ \mathbf{r}_Q = \mathbf{r}_P + \ell\sin\phi\,\mathbf{i} - \ell\cos\phi\,\mathbf{k} = \ell(\sin\theta + \sin\phi)\,\mathbf{i} - \ell(\cos\theta + \cos\phi)\,\mathbf{k} $$

### Phase 3: Step-by-Step Mathematical Deduction

#### Part (a): Velocity and Acceleration Vectors
1. Velocity of $P$:
   $$ \mathbf{v}_P = \ell\dot{\theta}\cos\theta\,\mathbf{i} + \ell\dot{\theta}\sin\theta\,\mathbf{k} $$
   $$ v_P^2 = \ell^2\dot{\theta}^2 $$
2. Velocity of $Q$:
   $$ \mathbf{v}_Q = \ell(\dot{\theta}\cos\theta + \dot{\phi}\cos\phi)\,\mathbf{i} + \ell(\dot{\theta}\sin\theta + \dot{\phi}\sin\phi)\,\mathbf{k} $$
   $$ v_Q^2 = \ell^2\left[ \dot{\theta}^2 + \dot{\phi}^2 + 2\dot{\theta}\dot{\phi}(\cos\theta\cos\phi + \sin\theta\sin\phi) \right] = \ell^2\left[ \dot{\theta}^2 + \dot{\phi}^2 + 2\dot{\theta}\dot{\phi}\cos(\theta - \phi) \right] $$

#### Part (b)-(c): Equations of Motion
Total Kinetic Energy:
$$ T = \frac{1}{2}m v_P^2 + \frac{1}{2}m v_Q^2 = \frac{1}{2}m\ell^2\left[ 2\dot{\theta}^2 + \dot{\phi}^2 + 2\dot{\theta}\dot{\phi}\cos(\theta - \phi) \right] $$
Total Potential Energy (taking datum at $z = 0$):
$$ V = mg z_P + mg z_Q = -mg\ell\cos\theta - mg\ell(\cos\theta + \cos\phi) = -mg\ell(2\cos\theta + \cos\phi) $$
Lagrange's equations $\frac{d}{dt}\left(\frac{\partial T}{\partial\dot{q}}\right) - \frac{\partial T}{\partial q} = -\frac{\partial V}{\partial q}$:
1. For $\theta$:
   $$ 2\ell\ddot{\theta} + \ell\ddot{\phi}\cos(\theta - \phi) + \ell\dot{\phi}^2\sin(\theta - \phi) + 2g\sin\theta = 0 $$
2. For $\phi$:
   $$ \ell\ddot{\phi} + \ell\ddot{\theta}\cos(\theta - \phi) - \ell\dot{\theta}^2\sin(\theta - \phi) + g\sin\phi = 0 $$

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

### Phase 4: Physical Interpretation & Synthesis
* The mechanical coupling $\phi = 2\theta$ acts as an internal kinematic constraint that stiffens the double pendulum into an equivalent single degree of freedom harmonic oscillator with effective mass $10m$ and effective restoring stiffness $6mg/\ell$, yielding the frequency $\omega_0 = \sqrt{3g/(5\ell)}$.
* **Dimensional check:** $[T] = [m\ell^2\dot{\theta}^2] = \text{kg}\cdot\text{m}^2\cdot\text{s}^{-2} = \text{J}$, $[V] = [mg\ell] = \text{J}$, and $[\omega_0] = \sqrt{[g]/[\ell]} = \text{s}^{-1}$ (the effective inertia $10m\ell^2$ and stiffness $6mg\ell$ are expressed in the coordinate $\theta$; with $x = \ell\theta$ they become $10m$ and $6mg/\ell$).
* **Numerical check of part (e) (RK4, step $10^{-3}$, $g = 9.81\ \text{m/s}^2$, $m = \ell = 1$, 60 s from $\theta = \phi = \pi/4$ at rest):** the full nonlinear equations of part (c) give a maximum of $z_Q/\ell = -1.3375$, always negative, so $Q$ never reaches the $Ox$ axis, consistent with the energy bound $V \ge -mg\ell$ against $E_0 = -2.121\,mg\ell$.
* **Numerical check of part (f):** the exact one-degree-of-freedom Lagrangian with $\phi = 2\theta$ (without the small-angle approximation) integrated by RK4 from $\theta = 10^{-3}$ rad has half-period $1.2950$ s, against $\pi/\omega_0 = \pi\sqrt{5\ell/(3g)} = 1.2949$ s.
