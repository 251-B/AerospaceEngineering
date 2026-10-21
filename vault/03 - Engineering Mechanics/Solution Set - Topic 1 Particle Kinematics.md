---
title: "Solution Set - Topic 1: Fundamentals and Particle Kinematics"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Full Analytical Solutions (course order, Notes chapter 7)"
language: "English"
tags:
  - solutions
  - particle-kinematics
---

# Topic 1: Fundamentals and Particle Kinematics - Complete Analytical Solutions

This document contains the step-by-step solutions of the 6 problems of Topic 1 (*Particle Kinematics*) from the official UC3M problem collection (`Problems.pdf`). Every solution follows the systematic approach of `Notes.pdf`, chapter 7, inside four phases: constraints, degrees of freedom and coordinates (7.1, 7.2); reference frames (7.3); the derivation in the order kinematics (7.4), forces (7.5), equations of motion (7.6) and integration with the answers (7.7); and the interpretation and checks. Topic 1 problems are purely kinematic: the trajectory or the motion is given, so no force acts as an unknown and sections 3.2 and 3.3 state that they do not apply. Each formula is preceded by the reason for using it, with explicit derivatives (product and chain rules) and explicit integrals.

---

## 📌 Problem 01: Rocket Helical Trajectory (MIT OCW)

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** an out-of-control rocket, modelled as a point particle $P$, ascends along a circular helix around the vertical $z$-axis.
* **Hypotheses:** $a \gt 0$, $v_z \gt 0$ and $\omega \gt 0$ are constants and $t \gt 0$.
* **Constraints and degrees of freedom:** the statement gives the three Cartesian coordinates as functions of time, so the particle is on the helix, which satisfies the two holonomic relations $x = a\cos(\omega z/v_z)$ and $y = a\sin(\omega z/v_z)$ (substituting $z = v_zt$ recovers the statement). Two independent relations leave $\text{CDOF} = 3 - 2 = 1$: a single coordinate ($t$, or the arc length $s$) fixes the position on the helix.
* **Coordinates:** the Cartesian coordinates $(x, y, z)$ of the statement; for the questions we also use the cylindrical coordinates $(R, \theta, z)$ and the arc length $s$.
* **Parameters:** radius $a$ [m], angular frequency $\omega$ [rad/s], vertical velocity $v_z$ [m/s], time $t$ [s].

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $\mathcal{S}_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$, fixed to the launch site with $\mathbf{k}_0$ along the vertical $z$-axis.
* **Cylindrical basis:** $\mathcal{B}_{\text{cyl}} = \{\mathbf{e}_R, \mathbf{e}_\theta, \mathbf{e}_z\}$, a rotation of $\mathcal{B}_0$ by the angle $\theta = \omega t$ about $\mathbf{k}_0$:
$$ [{}_0 R_{\text{cyl}}] = \begin{pmatrix} \cos(\omega t) & -\sin(\omega t) & 0 \\ \sin(\omega t) & \cos(\omega t) & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_{\text{cyl}}] = \cos^2(\omega t) + \sin^2(\omega t) = 1, \qquad [{}_0 R_{\text{cyl}}][{}_0 R_{\text{cyl}}]^T = I $$
The product $RR^T$ has diagonal entries $\cos^2(\omega t) + \sin^2(\omega t) = 1$ (and $1$) and off-diagonal entries $\cos(\omega t)\sin(\omega t) - \sin(\omega t)\cos(\omega t) = 0$.
* The basis vectors, from the columns of the matrix:
$$ \mathbf{e}_R = \cos(\omega t)\mathbf{i}_0 + \sin(\omega t)\mathbf{j}_0, \qquad \mathbf{e}_\theta = -\sin(\omega t)\mathbf{i}_0 + \cos(\omega t)\mathbf{j}_0, \qquad \mathbf{e}_z = \mathbf{k}_0 $$
* **Time derivatives of the unit vectors** (direct differentiation of their explicit components, with the chain rule $\frac{d}{dt}\cos(\omega t) = -\omega\sin(\omega t)$ and $\frac{d}{dt}\sin(\omega t) = \omega\cos(\omega t)$; Notes Sec. 2.6.2):
$$ \frac{d\mathbf{e}_R}{dt} = -\omega\sin(\omega t)\,\mathbf{i}_0 + \omega\cos(\omega t)\,\mathbf{j}_0 = \omega\,\mathbf{e}_\theta, \qquad \frac{d\mathbf{e}_\theta}{dt} = -\omega\cos(\omega t)\,\mathbf{i}_0 - \omega\sin(\omega t)\,\mathbf{j}_0 = -\omega\,\mathbf{e}_R, \qquad \frac{d\mathbf{e}_z}{dt} = \mathbf{0} $$
* **Intrinsic basis:** $\mathcal{B}_F = \{\mathbf{e}_t, \mathbf{e}_n, \mathbf{e}_b\}$ (tangent, principal normal toward the centre of curvature, binormal $\mathbf{e}_b = \mathbf{e}_t\times\mathbf{e}_n$), obtained in 3.1 and related to $\mathcal{B}_{\text{cyl}}$ by a second change-of-basis matrix.

### Phase 3: Derivation

#### 3.1 Kinematics
##### (a) Cartesian position, velocity and acceleration
* **Pedagogical Justification:** the position is given by its Cartesian components in the fixed basis, whose unit vectors are constant ($\dot{\mathbf{i}}_0 = \dot{\mathbf{j}}_0 = \dot{\mathbf{k}}_0 = \mathbf{0}$). Velocity and acceleration follow by differentiating term by term.
$$ \mathbf{r}(t) = a\cos(\omega t)\,\mathbf{i}_0 + a\sin(\omega t)\,\mathbf{j}_0 + v_z t\,\mathbf{k}_0 $$
$$ \mathbf{v}(t) = \frac{d\mathbf{r}}{dt} = -a\omega\sin(\omega t)\,\mathbf{i}_0 + a\omega\cos(\omega t)\,\mathbf{j}_0 + v_z\,\mathbf{k}_0 $$
$$ \mathbf{a}(t) = \frac{d\mathbf{v}}{dt} = -a\omega^2\cos(\omega t)\,\mathbf{i}_0 - a\omega^2\sin(\omega t)\,\mathbf{j}_0 + 0\,\mathbf{k}_0 = -a\omega^2\left(\cos(\omega t)\,\mathbf{i}_0 + \sin(\omega t)\,\mathbf{j}_0\right) $$

##### (b) Cylindrical position, velocity and acceleration
* **Pedagogical Justification:** the helix lies on a cylinder, so $R = \sqrt{x^2 + y^2} = a$ is constant and $\theta = \omega t$. The vectors $\mathbf{e}_R$ and $\mathbf{e}_\theta$ are not constant, so we use the product rule with the derivatives of Phase 2.
$$ \mathbf{r} = a\,\mathbf{e}_R + v_z t\,\mathbf{e}_z $$
$$ \mathbf{v} = \dot{a}\,\mathbf{e}_R + a\frac{d\mathbf{e}_R}{dt} + \frac{d(v_z t)}{dt}\mathbf{e}_z + v_z t\frac{d\mathbf{e}_z}{dt} = 0 + a\omega\,\mathbf{e}_\theta + v_z\,\mathbf{e}_z + 0 = a\omega\,\mathbf{e}_\theta + v_z\,\mathbf{e}_z $$
$$ \mathbf{a} = \frac{d(a\omega)}{dt}\mathbf{e}_\theta + a\omega\frac{d\mathbf{e}_\theta}{dt} + \frac{dv_z}{dt}\mathbf{e}_z + v_z\frac{d\mathbf{e}_z}{dt} = 0 + a\omega\left(-\omega\,\mathbf{e}_R\right) + 0 + 0 = -a\omega^2\,\mathbf{e}_R $$

##### (d) Modulus of the velocity
* **Pedagogical Justification:** the speed is the norm of the velocity vector, the rate at which the distance along the path is travelled. It is computed before part (c) because the intrinsic basis and the radius of curvature need it.
$$ v = \|\mathbf{v}\| = \sqrt{a^2\omega^2\left(\sin^2\omega t + \cos^2\omega t\right) + v_z^2} = \sqrt{a^2\omega^2 + v_z^2} \equiv V $$
The speed is constant for all $t$.

##### (c) Intrinsic basis, and velocity and acceleration in terms of $s$ and $\rho$
* **Pedagogical Justification:** the Frenet-Serret basis follows the curve itself (Notes Sec. 2.4): $\mathbf{e}_t$ is the direction of the velocity, $\mathbf{e}_n$ points toward the centre of the osculating circle and $\mathbf{e}_b = \mathbf{e}_t\times\mathbf{e}_n$ completes a right-handed triad. The intrinsic acceleration is (Notes Eq. 2.17)
$$ \mathbf{a} = \ddot{s}\,\mathbf{e}_t + \frac{\dot{s}^2}{\rho}\,\mathbf{e}_n, \qquad \mathbf{v} = \dot{s}\,\mathbf{e}_t $$
* **Tangent.** $\mathbf{e}_t = \dfrac{\mathbf{v}}{\|\mathbf{v}\|} = \dfrac{a\omega\,\mathbf{e}_\theta + v_z\,\mathbf{e}_z}{V}$.
* **Principal normal.** Since $\dot{s} = V$ is constant, $\ddot{s} = dV/dt = 0$ and the whole acceleration is normal: $\mathbf{a} = a_n\mathbf{e}_n = -a\omega^2\mathbf{e}_R$. Taking the norm gives $a_n = a\omega^2$, and dividing the vector by it gives
$$ \mathbf{e}_n = \frac{\mathbf{a}}{a_n} = \frac{-a\omega^2\mathbf{e}_R}{a\omega^2} = -\mathbf{e}_R $$
The principal normal points radially inward, toward the axis of the cylinder.
* **Radius of curvature.** From $a_n = \dot{s}^2/\rho$:
$$ \rho = \frac{V^2}{a_n} = \frac{a^2\omega^2 + v_z^2}{a\omega^2} = a + \frac{v_z^2}{a\omega^2} $$
* **Binormal.** Using $\mathbf{e}_R\times\mathbf{e}_\theta = \mathbf{e}_z$ and its cyclic permutations ($\mathbf{e}_z\times\mathbf{e}_R = \mathbf{e}_\theta$), together with the anticommutativity $\mathbf{e}_\theta\times\mathbf{e}_R = -\mathbf{e}_z$:
$$ \mathbf{e}_b = \mathbf{e}_t\times\mathbf{e}_n = \frac{a\omega\,\mathbf{e}_\theta + v_z\,\mathbf{e}_z}{V}\times(-\mathbf{e}_R) = \frac{-a\omega\left(\mathbf{e}_\theta\times\mathbf{e}_R\right) - v_z\left(\mathbf{e}_z\times\mathbf{e}_R\right)}{V} = \frac{-v_z\,\mathbf{e}_\theta + a\omega\,\mathbf{e}_z}{V} $$
* **Velocity and acceleration with $s$ and $\rho$:**
$$ \mathbf{v} = \dot{s}\,\mathbf{e}_t = V\,\mathbf{e}_t, \qquad \mathbf{a} = \ddot{s}\,\mathbf{e}_t + \frac{\dot{s}^2}{\rho}\,\mathbf{e}_n = \frac{V^2}{\rho}\,\mathbf{e}_n = a\omega^2\,\mathbf{e}_n $$
* **Second change-of-basis matrix.** Its columns are the components of $\mathbf{e}_t$, $\mathbf{e}_n$, $\mathbf{e}_b$ in $\mathcal{B}_{\text{cyl}}$:
$$ [{}_{\text{cyl}} R_{\text{tnb}}] = \begin{pmatrix} 0 & -1 & 0 \\ a\omega/V & 0 & -v_z/V \\ v_z/V & 0 & a\omega/V \end{pmatrix}, \qquad R R^T = I $$
With $V^2 = a^2\omega^2 + v_z^2$, the rows have unit norm ($1$, $(a^2\omega^2 + v_z^2)/V^2 = 1$ and $(v_z^2 + a^2\omega^2)/V^2 = 1$) and are mutually orthogonal (row 1 against rows 2 and 3 gives $0$, rows 2 and 3 give $a\omega v_z/V^2 - v_za\omega/V^2 = 0$), so $RR^T = I$; expanding along the first row, $\det = -(-1)\left(\frac{a^2\omega^2}{V^2} + \frac{v_z^2}{V^2}\right) = 1$.
Expanding the determinant along the first row (its only non-zero entry is $-1$ in position $(1,2)$, with cofactor sign $-1$):
$$ \det = -(-1)\left[\frac{a\omega}{V}\cdot\frac{a\omega}{V} - \left(-\frac{v_z}{V}\right)\frac{v_z}{V}\right] = \frac{a^2\omega^2 + v_z^2}{V^2} = 1 $$
The columns have unit norm and are mutually orthogonal, so $R R^T = I$; the composition $[{}_0 R_{\text{tnb}}] = [{}_0 R_{\text{cyl}}][{}_{\text{cyl}} R_{\text{tnb}}]$ is again a proper rotation (determinant $1\cdot 1 = 1$).

#### 3.2 Forces
Not applicable: kinematics-only problem. The trajectory is given, so no force enters the question.

#### 3.3 Equations of Motion
Not applicable: kinematics-only problem. The motion is prescribed by the statement, so there is no equation of motion to solve.

#### 3.4 Integration and Answers
##### (e) Arc length as a function of time
* **Pedagogical Justification:** $s(t)$ measures the distance travelled along the trajectory from $t = 0$, i.e. the integral of the speed.
$$ s(t) = \int_0^t v\,dt' = \int_0^t V\,dt' = V\left[t'\right]_0^t = V(t - 0) = t\sqrt{a^2\omega^2 + v_z^2} $$

##### (f) Trajectory as a function of the arc length
* **Pedagogical Justification:** inverting $s(t)$ gives $t(s) = s/V$, which is substituted into the parametric equations to remove the time:
$$ x(s) = a\cos\left(\frac{\omega s}{\sqrt{a^2\omega^2 + v_z^2}}\right), \qquad y(s) = a\sin\left(\frac{\omega s}{\sqrt{a^2\omega^2 + v_z^2}}\right), \qquad z(s) = \frac{v_z s}{\sqrt{a^2\omega^2 + v_z^2}} $$

##### (g) Centre of curvature at $(a, 0, 0)$
* **Pedagogical Justification:** the centre $C$ of the osculating circle lies on the principal normal at distance $\rho$: $\mathbf{r}_C = \mathbf{r}_P + \rho\,\mathbf{e}_n$ (Notes Sec. 2.4).
* The helix passes through $(a, 0, 0)$ where $z = v_zt = 0$, i.e. at $t = 0$. The statement says $t \gt 0$, so we take the motion law to hold for $t \ge 0$ (the point is the limit $t \to 0^+$; all formulas are continuous there). At that point $\mathbf{r}_P(0) = a\,\mathbf{i}_0$ and $\mathbf{e}_n(0) = -\mathbf{e}_R(0) = -\mathbf{i}_0$:
$$ \mathbf{r}_C = a\,\mathbf{i}_0 + \left(a + \frac{v_z^2}{a\omega^2}\right)\left(-\mathbf{i}_0\right) = -\frac{v_z^2}{a\omega^2}\,\mathbf{i}_0, \qquad \boxed{C = \left(-\frac{v_z^2}{a\omega^2},\ 0,\ 0\right)} $$

### Phase 4: Interpretation & Checks
* **Dimensional check:** $[a\omega] = \text{m}\cdot\text{s}^{-1}$ and $[v_z] = \text{m/s}$, so $V$ is in m/s. The offset $\left[\dfrac{v_z^2}{a\omega^2}\right] = \dfrac{(\text{m/s})^2}{\text{m}\cdot\text{s}^{-2}} = \text{m}$.
* **Limiting cases:** if $v_z \to 0$ (planar circle) $\rho = a$ and $C = (0, 0, 0)$, the centre of the circle. If $\omega \to 0$ (vertical ascent) $\rho \to \infty$: the curvature vanishes and the trajectory is a straight line.
* **Check against the official key:** `Problems.pdf` has no entry for Problem 1 in its solution keys. The results are verified by independent derivation: sympy reproduces $\|\mathbf{v}\| = V$, $a_n = a\omega^2$, $\rho = a + v_z^2/(a\omega^2)$ (also from $\rho = \|\mathbf{v}\|^3/\|\mathbf{v}\times\mathbf{a}\|$), the binormal, the centre of curvature and $\det[{}_{\text{cyl}}R_{\text{tnb}}] = 1$ with $R R^T = I$.

---

## 📌 Problem 02: Kinematics, Spiral

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a particle $P$ moves along the planar spiral $r = \alpha e^{\beta\theta}$ with the prescribed angular motion $\theta(t) = \delta t^n$.
* **Hypotheses:** $\alpha, \beta, \delta, n \gt 0$ are constants and $t \gt 0$. At $t = 0$, $\dot{\theta} \propto t^{n-1}$ diverges for $0 \lt n \lt 1$ and $\ddot{\theta} \propto t^{n-2}$ diverges for $1 \lt n \lt 2$; for $n = 1$ and for $n \ge 2$ every quantity is finite at $t = 0$ (for $n \ge 2$ the speed vanishes there, which is not a singularity, because $\mathbf{e}_t$ and $\rho$ do not depend on the speed). $t \gt 0$ is kept for all $n$ for uniformity. The motion is planar ($z = 0$).
* **Constraints and degrees of freedom:** the spiral $r = \alpha e^{\beta\theta}$ is a holonomic, scleronomic constraint in the plane. The particle then has $\text{CDOF} = 2 - 1 = 1$, and the motion law $\theta = \delta t^n$ fixes it completely.
* **Coordinates:** polar coordinates $(r, \theta)$ about the origin $O$ of the spiral; the angle $\theta$ is the free coordinate.
* **Parameters and units:** $[r] = \text{m}$, so $[\alpha] = \text{m}$; $\beta$ is dimensionless; $[\theta] = \text{rad}$, so $[\delta] = \text{rad}\cdot\text{s}^{-n}$.

### Phase 2: Reference Frames & Vector Bases
* **Inertial basis:** $\mathcal{B}_0 = \{\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$.
* **Polar basis:** $\mathcal{B}_{\text{polar}} = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}_0\}$, a rotation of $\mathcal{B}_0$ by $\theta$ about $\mathbf{k}_0$:
$$ [{}_0 R_\theta] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_\theta] = \cos^2\theta + \sin^2\theta = 1, \qquad [{}_0 R_\theta][{}_0 R_\theta]^T = I $$
The product $RR^T$ has diagonal entries $\cos^2\theta + \sin^2\theta = 1$ (and $1$) and off-diagonal entries $\cos\theta\sin\theta - \sin\theta\cos\theta = 0$.
* **Angular velocity of the basis:** $\boldsymbol{\omega} = \dot{\theta}\,\mathbf{k}_0$. By Poisson's formula (Notes Sec. 2.6.2, Eqs. 2.25-2.26): $\dot{\mathbf{e}}_r = \dot{\theta}\,\mathbf{e}_\theta$ and $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_r$.
* **Intrinsic basis from the polar basis** (derived in 3.1(c), where the sign of the normal is justified): $\mathbf{e}_t = (\beta\,\mathbf{e}_r + \mathbf{e}_\theta)/\sqrt{1 + \beta^2}$, $\mathbf{e}_n = (-\mathbf{e}_r + \beta\,\mathbf{e}_\theta)/\sqrt{1 + \beta^2}$ and $\mathbf{e}_b = \mathbf{e}_t\times\mathbf{e}_n = \mathbf{k}_0$. The components of $\mathbf{e}_t$ and $\mathbf{e}_n$ in $\{\mathbf{e}_r, \mathbf{e}_\theta\}$ are the columns of
$$ [{}_{\text{polar}} R_{\text{tn}}] = \frac{1}{\sqrt{1 + \beta^2}}\begin{pmatrix} \beta & -1 \\ 1 & \beta \end{pmatrix}, \qquad \det = \frac{\beta^2 + 1}{1 + \beta^2} = 1, \qquad R R^T = I $$
(rows of norm $(\beta^2 + 1)/(1 + \beta^2) = 1$ and orthogonal, $(\beta - \beta)/(1 + \beta^2) = 0$). It is completed with $\mathbf{e}_b = \mathbf{k}_0$ as third row and column, $(0, 0, 1)$, so the full $3\times 3$ matrix is a rotation about $\mathbf{k}_0$.
This is a planar rotation by the constant angle $\arctan(1/\beta)$: the tangent makes a constant angle with the radial direction (equiangular spiral).

### Phase 3: Derivation

#### 3.1 Kinematics
##### (a) Radial and transverse components of the velocity
* **Pedagogical Justification:** in polar coordinates $\mathbf{v} = \dot{r}\,\mathbf{e}_r + r\dot{\theta}\,\mathbf{e}_\theta$ (product rule and Poisson). The coordinates depend on time through $\theta(t)$, so the chain rule is needed.
$$ \dot{\theta} = \frac{d}{dt}\left(\delta t^n\right) = n\delta t^{n-1}, \qquad \frac{dr}{d\theta} = \frac{d}{d\theta}\left(\alpha e^{\beta\theta}\right) = \alpha\beta e^{\beta\theta} = \beta r $$
$$ \dot{r} = \frac{dr}{d\theta}\,\dot{\theta} = \beta r\,n\delta t^{n-1} = \alpha\beta n\delta t^{n-1}e^{\beta\delta t^n} $$
$$ \boxed{v_r = \dot{r} = \beta n\delta t^{n-1}\,r}, \qquad \boxed{v_\theta = r\dot{\theta} = n\delta t^{n-1}\,r} $$

##### (b) Radial and transverse components of the acceleration
* **Pedagogical Justification:** the polar acceleration is (Notes Eq. 2.30; product rule applied to $\mathbf{v}$ with Poisson's formula)
$$ \mathbf{a} = \left(\ddot{r} - r\dot{\theta}^2\right)\mathbf{e}_r + \left(r\ddot{\theta} + 2\dot{r}\dot{\theta}\right)\mathbf{e}_\theta $$
* **Second derivatives** (product rule, with $\dot{r} = \beta r\dot{\theta}$):
$$ \ddot{\theta} = \frac{d}{dt}\left(n\delta t^{n-1}\right) = n(n - 1)\delta t^{n-2}, \qquad \ddot{r} = \beta\left(\dot{r}\dot{\theta} + r\ddot{\theta}\right) = \beta\left(\beta r\dot{\theta}^2 + r\ddot{\theta}\right) = \beta^2r\dot{\theta}^2 + \beta r\ddot{\theta} $$
* **Radial component:**
$$ a_r = \ddot{r} - r\dot{\theta}^2 = \left(\beta^2 - 1\right)r\dot{\theta}^2 + \beta r\ddot{\theta} = r\left[\left(\beta^2 - 1\right)n^2\delta^2t^{2n-2} + \beta n(n - 1)\delta t^{n-2}\right] = n\delta t^{n-2}\,r\left[\left(\beta^2 - 1\right)n\delta t^n + \beta(n - 1)\right] $$
(substituting $\dot{\theta}^2 = n^2\delta^2t^{2n-2}$ and $\ddot{\theta} = n(n - 1)\delta t^{n-2}$, then factoring out $n\delta t^{n-2}$, since $t^{2n-2} = t^{n-2}t^n$).
* **Transverse component:**
$$ a_\theta = r\ddot{\theta} + 2\dot{r}\dot{\theta} = r\ddot{\theta} + 2\beta r\dot{\theta}^2 = r\left[n(n - 1)\delta t^{n-2} + 2\beta n^2\delta^2t^{2n-2}\right] = n\delta t^{n-2}\,r\left[(n - 1) + 2\beta n\delta t^n\right] $$

##### (c) Tangential and normal components of the velocity
* **Pedagogical Justification:** the velocity is always tangent to the path, so in the intrinsic basis $\mathbf{v} = v\,\mathbf{e}_t + 0\,\mathbf{e}_n$ and the normal component is identically zero.
$$ v_t = v = \sqrt{v_r^2 + v_\theta^2} = r\dot{\theta}\sqrt{\beta^2 + 1} = n\delta t^{n-1}\,r\sqrt{1 + \beta^2}, \qquad v_n = 0 $$
* The unit tangent follows from $\mathbf{v} = r\dot{\theta}\left(\beta\,\mathbf{e}_r + \mathbf{e}_\theta\right)$: $\mathbf{e}_t = \left(\beta\,\mathbf{e}_r + \mathbf{e}_\theta\right)/\sqrt{1 + \beta^2}$. The normal toward the centre of curvature must satisfy $\mathbf{a}\cdot\mathbf{e}_n \gt 0$. The left normal $\mathbf{k}_0\times\mathbf{e}_t = \left(-\mathbf{e}_r + \beta\,\mathbf{e}_\theta\right)/\sqrt{1 + \beta^2}$ does: its projection of the acceleration (with $a_r$ and $a_\theta$ of part (b)) is $\left(\beta a_\theta - a_r\right)/\sqrt{1 + \beta^2}$, and
$$ \beta a_\theta - a_r = \beta\left(r\ddot{\theta} + 2\beta r\dot{\theta}^2\right) - \left(\left(\beta^2 - 1\right)r\dot{\theta}^2 + \beta r\ddot{\theta}\right) = \left(1 + \beta^2\right)r\dot{\theta}^2 \gt 0 $$
so $\mathbf{e}_n = \mathbf{k}_0\times\mathbf{e}_t$ and $\mathbf{e}_b = \mathbf{k}_0$.

##### (d) Tangential and normal components of the acceleration
* **Pedagogical Justification:** $a_t = \dot{v}$ is the rate of change of the speed and $a_n = v^2/\rho$ measures the turning of the velocity.
$$ a_t = \frac{d}{dt}\left(\sqrt{1 + \beta^2}\,r\dot{\theta}\right) = \sqrt{1 + \beta^2}\left(\dot{r}\dot{\theta} + r\ddot{\theta}\right) = \sqrt{1 + \beta^2}\left(\beta r\dot{\theta}^2 + r\ddot{\theta}\right) = \sqrt{1 + \beta^2}\,r\left[\beta n^2\delta^2t^{2n-2} + n(n - 1)\delta t^{n-2}\right] = \sqrt{1 + \beta^2}\,n\delta t^{n-2}\,r\left[\beta n\delta t^n + (n - 1)\right] $$
* **Normal component.** The cross product $\mathbf{a}\times\mathbf{v} = \left(a_t\mathbf{e}_t + a_n\mathbf{e}_n\right)\times v\,\mathbf{e}_t = -va_n\,\mathbf{e}_b$ gives $a_n = \dfrac{\|\mathbf{v}\times\mathbf{a}\|}{v} = \dfrac{|v_ra_\theta - v_\theta a_r|}{v}$. The numerator is
$$ v_ra_\theta - v_\theta a_r = \left(\beta r\dot{\theta}\right)\left(r\ddot{\theta} + 2\beta r\dot{\theta}^2\right) - \left(r\dot{\theta}\right)\left(\left(\beta^2 - 1\right)r\dot{\theta}^2 + \beta r\ddot{\theta}\right) $$
$$ = \beta r^2\dot{\theta}\ddot{\theta} + 2\beta^2r^2\dot{\theta}^3 - \left(\beta^2 - 1\right)r^2\dot{\theta}^3 - \beta r^2\dot{\theta}\ddot{\theta} = \left(\beta^2 + 1\right)r^2\dot{\theta}^3 $$
Dividing by $v = r\dot{\theta}\sqrt{\beta^2 + 1}$:
$$ a_n = \frac{\left(\beta^2 + 1\right)r^2\dot{\theta}^3}{r\dot{\theta}\sqrt{\beta^2 + 1}} = r\dot{\theta}^2\sqrt{\beta^2 + 1} = n^2\delta^2t^{2n-2}\,r\sqrt{1 + \beta^2} $$
Here $\|\mathbf{v}\times\mathbf{a}\| = |v_ra_\theta - v_\theta a_r|$, because $(v_r\mathbf{e}_r + v_\theta\mathbf{e}_\theta)\times(a_r\mathbf{e}_r + a_\theta\mathbf{e}_\theta) = (v_ra_\theta - v_\theta a_r)\,\mathbf{k}_0$ ($\mathbf{e}_r\times\mathbf{e}_r = \mathbf{e}_\theta\times\mathbf{e}_\theta = \mathbf{0}$, $\mathbf{e}_r\times\mathbf{e}_\theta = \mathbf{k}_0$).

#### 3.2 Forces
Not applicable: kinematics-only problem. The path and the motion law are given.

#### 3.3 Equations of Motion
Not applicable: kinematics-only problem. The motion is prescribed by $\theta(t) = \delta t^n$.

#### 3.4 Integration and Answers
##### (e) Radius of curvature
* **Pedagogical Justification:** the radius of curvature follows from the normal acceleration, $a_n = v^2/\rho$:
$$ \rho = \frac{v^2}{a_n} = \frac{r^2\dot{\theta}^2\left(1 + \beta^2\right)}{r\dot{\theta}^2\sqrt{1 + \beta^2}} = \boxed{r\sqrt{1 + \beta^2}} $$

### Phase 4: Interpretation & Checks
* **Geometric invariance:** on the spiral the angle $\psi$ between the radial line and the tangent satisfies $\tan\psi = r/(dr/d\theta) = 1/\beta$, a constant. The spiral is self-similar: $\lambda\,r(\theta) = r(\theta + \ln\lambda/\beta)$, so scaling it by a factor $\lambda$ gives the same curve rotated by an angle of magnitude $\ln\lambda/\beta$. Hence every length of the curve, $\rho$ included, scales with $r$.
* **Dimensional check:** $[\rho] = [r]\left[\sqrt{1 + \beta^2}\right] = \text{m}$; $[v_r] = [v_\theta] = [r\dot{\theta}] = \text{m/s}$, and $[a_n] = [r\dot{\theta}^2] = \text{m/s}^2$.
* **Limiting case $\beta \to 0$:** the spiral degenerates into the circle $r = \alpha$, with $\rho = r$ and $a_r = -r\dot{\theta}^2$, the centripetal acceleration.
* **Check against the official key:** `Problems.pdf` has no entry for Problem 2 in its solution keys. The results are verified by independent derivation: sympy reproduces $v_r/(r\dot{\theta}) = \beta$, $v_\theta/(r\dot{\theta}) = 1$, the factorised forms of $a_r$, $a_\theta$ and $a_t$, the identity $a_n^2 = r^2\dot{\theta}^4\left(1 + \beta^2\right)$ and $\rho = r\sqrt{1 + \beta^2}$, with zero residual.

---

## 📌 Problem 03: Kinematics, Astroid

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a particle $P$ moves on the astroid $x = a\cos^3\phi$, $y = a\sin^3\phi$ with constant tangential acceleration $a_t = k$ (the statement calls it $k$) and starts from rest at $\phi = 0$.
* **Hypotheses:** $a \gt 0$, $k \gt 0$. The motion stays within one smooth segment of the curve, here the first-quadrant arc $0 \le \phi \le \pi/2$ (the astroid has cusps at $\phi = 0, \pi/2, \pi, 3\pi/2$). Starting at the cusp $\phi = 0$ the particle could enter either neighbouring arc; we choose the one with $\phi$ increasing, so that $s$ increases with $\phi$ and $d\phi \ge 0$.
* **Constraints and degrees of freedom:** the curve is a holonomic, scleronomic constraint in the plane, so $\text{CDOF} = 2 - 1 = 1$. The coordinate is $\phi$, or the arc length $s$ measured from $\phi = 0$.
* **Parameters and units:** scale $a$ [m], tangential acceleration $k$ [m/s$^2$], time $t$ [s].

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $\mathcal{S}_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ with the curve in the $Oxy$ plane.
* **Parametric curve:** $x(\phi) = a\cos^3\phi$, $y(\phi) = a\sin^3\phi$. Differentiating with respect to the parameter (chain rule):
$$ \frac{dx}{d\phi} = 3a\cos^2\phi\,(-\sin\phi) = -3a\cos^2\phi\sin\phi, \qquad \frac{dy}{d\phi} = 3a\sin^2\phi\cos\phi $$

### Phase 3: Derivation

#### 3.1 Kinematics
* **Pedagogical Justification:** we use the arc length as the coordinate along the path. The differential arc length follows from the hint, $ds = \sqrt{dx^2 + dy^2}$:
$$ ds^2 = \left(-3a\cos^2\phi\sin\phi\right)^2d\phi^2 + \left(3a\sin^2\phi\cos\phi\right)^2d\phi^2 = 9a^2\cos^4\phi\sin^2\phi\,d\phi^2 + 9a^2\sin^4\phi\cos^2\phi\,d\phi^2 $$
$$ ds^2 = 9a^2\cos^2\phi\sin^2\phi\left(\cos^2\phi + \sin^2\phi\right)d\phi^2 = 9a^2\cos^2\phi\sin^2\phi\,d\phi^2 $$
For $0 \le \phi \le \pi/2$ both $\sin\phi$ and $\cos\phi$ are non-negative (and $d\phi \ge 0$), so the positive root is
$$ ds = 3a\sin\phi\cos\phi\,d\phi $$
* **Tangential acceleration.** The tangential component of the acceleration is the second derivative of the arc length: $a_t = \ddot{s} = k$.

#### 3.2 Forces
Not applicable: kinematics-only problem. The tangential acceleration is given.

#### 3.3 Equations of Motion
Not applicable: kinematics-only problem. The law $\ddot{s} = k$ is the statement itself.

#### 3.4 Integration and Answers
##### Step 1: arc length as a function of time
* **Pedagogical Justification:** integrate $\ddot{s} = k$ twice, with the initial conditions $\dot{s}(0) = 0$ (at rest) and $s(0) = 0$ (at $\phi = 0$):
$$ \dot{s}(t) = \int_0^t k\,dt' = \left[kt'\right]_0^t = kt - 0 = kt, \qquad s(t) = \int_0^t kt'\,dt' = \left[\frac{1}{2}kt'^2\right]_0^t = \frac{1}{2}kt^2 - 0 = \frac{1}{2}kt^2 $$

##### Step 2: arc length as a function of $\phi$
* **Pedagogical Justification:** integrate $ds$ from $\phi = 0$. With the substitution $w = \sin u$, $dw = \cos u\,du$, the limits become $w = 0$ at $u = 0$ and $w = \sin\phi$ at $u = \phi$:
$$ s(\phi) = \int_0^\phi 3a\sin u\cos u\,du = 3a\int_0^{\sin\phi}w\,dw = 3a\left[\frac{w^2}{2}\right]_0^{\sin\phi} = 3a\left(\frac{\sin^2\phi}{2} - 0\right) = \frac{3a}{2}\sin^2\phi $$

##### Step 3: equating both expressions
* **Pedagogical Justification:** the distance travelled along the curve is the same quantity in both descriptions, $s(t) = s(\phi)$:
$$ \frac{3a}{2}\sin^2\phi = \frac{1}{2}kt^2 \implies \sin^2\phi = \frac{kt^2}{3a} \implies \sin\phi = \sqrt{\frac{k}{3a}}\,t $$
where the positive root is taken because $0 \le \phi \le \pi/2$. Therefore
$$ \boxed{\phi(t) = \arcsin\left(\sqrt{\frac{k}{3a}}\,t\right)} $$

##### Step 4: position as a function of time
* **Pedagogical Justification:** with $\sin\phi = \sqrt{k/(3a)}\,t$ and $\cos\phi = \sqrt{1 - \sin^2\phi} = \sqrt{1 - kt^2/(3a)}$ (non-negative in the first quadrant):
$$ \boxed{x(t) = a\cos^3\phi = a\left(1 - \frac{kt^2}{3a}\right)^{3/2}}, \qquad \boxed{y(t) = a\sin^3\phi = a\left(\frac{k}{3a}\right)^{3/2}t^3} $$
These hold for $0 \le t \le t_{\text{cusp}}$, where $t_{\text{cusp}}$ is defined in Phase 4.

### Phase 4: Interpretation & Checks
* **Dimensional check:** $\left[\sqrt{\dfrac{k}{3a}}\,t\right] = \sqrt{\dfrac{\text{m}\,\text{s}^{-2}}{\text{m}}}\ \text{s} = \text{s}^{-1}\cdot\text{s} = 1$, so the argument of $\arcsin$ is dimensionless, as it must be.
* **Physical limits:** at $t = 0$, $\phi = 0$ and the particle is at the cusp $(a, 0)$. It reaches the next cusp, $\phi = \pi/2$ at $(0, a)$, when $\sin\phi = 1$:
$$ \sqrt{\frac{k}{3a}}\,t_{\text{cusp}} = 1 \implies t_{\text{cusp}} = \sqrt{\frac{3a}{k}} $$
The total length of the arc is $s(\pi/2) = 3a/2$, consistent with $\frac{1}{2}kt_{\text{cusp}}^2 = \frac{1}{2}k\cdot\frac{3a}{k} = \frac{3a}{2}$. The solution stops at the cusp for a physical reason. The tangent is $\mathbf{e}_t = \left(-\cos\phi, \sin\phi\right)$ and $d\mathbf{e}_t/d\phi = \left(\sin\phi, \cos\phi\right)$ has unit norm, so $\rho = \dfrac{ds/d\phi}{\left\|d\mathbf{e}_t/d\phi\right\|} = 3a\sin\phi\cos\phi$, which tends to $0$ at both cusps, with the centre of curvature on the normal $\mathbf{e}_n = \left(\sin\phi, \cos\phi\right)$ (the arc is convex toward the origin). At arrival the speed is $\dot{s}(t_{\text{cusp}}) = kt_{\text{cusp}} = \sqrt{3ak} \ne 0$, so $a_n = \dot{s}^2/\rho \to \infty$: the motion cannot continue with constant $a_t$ through the cusp. At the start, $a_n \approx \dfrac{(kt)^2}{3a\phi} \to 0$ because $\phi \approx \sqrt{k/(3a)}\,t$, so the departure cusp is regular. Explicitly, $a_n \approx \dfrac{k^2t^2}{3a\sqrt{k/(3a)}\,t} = k\sqrt{\dfrac{k}{3a}}\,t \to 0$.
* **Check against the official key:** the key of `Problems.pdf` is $\phi = \arcsin\left(\sqrt{k/(3a)}\,t\right)$ and $s = kt^2/2$ (read on the rendered page), which equals the result above. Sympy also confirms that $s(\phi(t)) - kt^2/2 = 0$ identically.

---

## 📌 Problem 04: Plane at Constant Altitude

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** an aircraft moves at constant altitude $y_0$ with velocity $v_0$ along $x$. At $t = 0$ it is at $x = 0$ and begins to accelerate along $x$ at a constant rate $a_x$. A fixed observer at the origin $O$ describes its position with polar coordinates.
* **Hypotheses:** $y_0 \gt 0$, $v_0 \ge 0$ and $a_x$ are constants.
* **Constraints and degrees of freedom:** the altitude is fixed, $y = y_0$ (holonomic, scleronomic, so $\dot{y} = \ddot{y} = 0$). The aircraft has $\text{CDOF} = 2 - 1 = 1$, with the coordinate $x(t)$ given by the statement.
* **Coordinates:** Cartesian $x(t)$ for the motion, and polar $(r, \theta)$ about $O$ for the description requested, with $\theta$ measured from $+\mathbf{i}$.

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $\mathcal{S}_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$ and $\mathbf{r} = x\,\mathbf{i} + y_0\,\mathbf{j}$.
* **Polar relations:** $r = \sqrt{x^2 + y_0^2}$ and $\tan\theta = y_0/x$; equivalently $\cos\theta = x/r$ and $\sin\theta = y_0/r$.
* **Polar basis.** $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}\}$ is the inertial basis rotated by $\theta(t)$ about $\mathbf{k}$:
$$ [{}_0 R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} x/r & -y_0/r & 0 \\ y_0/r & x/r & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = \frac{x^2 + y_0^2}{r^2} = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
The product has diagonal entries $(x^2 + y_0^2)/r^2 = 1$ (and $1$) and off-diagonal entries $(xy_0 - y_0x)/r^2 = 0$.
* The inverse relation $\mathbf{i} = \cos\theta\,\mathbf{e}_r - \sin\theta\,\mathbf{e}_\theta$ is the one used in 3.4.

### Phase 3: Derivation

#### 3.1 Kinematics
* **Pedagogical Justification:** the motion along $x$ is uniformly accelerated, so $x(t)$ and $v(t)$ follow by integrating $\ddot{x} = a_x$ with the initial conditions $\dot{x}(0) = v_0$ and $x(0) = 0$ (Barrow's rule):
$$ \dot{x}(t) = v_0 + \int_0^ta_x\,dt' = v_0 + \left[a_xt'\right]_0^t = v_0 + a_xt - a_x\cdot 0 \equiv v(t), \qquad x(t) = 0 + \int_0^t\left(v_0 + a_xt'\right)dt' = \left[v_0t' + \frac{1}{2}a_xt'^2\right]_0^t = \left(v_0t + \frac{1}{2}a_xt^2\right) - 0 $$
* The polar position follows from the geometric relations of Phase 2: $\mathbf{r} = r\,\mathbf{e}_r$ with $r(t) = \sqrt{\left(v_0t + \tfrac{1}{2}a_xt^2\right)^2 + y_0^2}$ and $\theta(t) = \operatorname{arccot}\left(\dfrac{v_0t + \tfrac{1}{2}a_xt^2}{y_0}\right)$, with the branch $\operatorname{arccot} \in (0, \pi)$ (so $\theta(0) = \pi/2$, and $\theta$ stays in $(0, \pi)$ even if $a_x \lt 0$ makes $x$ negative). The velocity and acceleration come from differentiating these relations.
##### (a) Proof that $\dot{r} = \dfrac{v(t)\,x(t)}{r(t)}$
* **Pedagogical Justification:** differentiate implicitly the relation $r^2 = x^2 + y_0^2$ with respect to time.
$$ 2r\dot{r} = 2x\dot{x} + 0 = 2x\,v(t) \implies \dot{r} = \frac{v(t)\,x(t)}{r(t)} \quad \blacksquare $$

##### (b) Proof that $\dot{\theta} = -\dfrac{v(t)\,y_0}{r(t)^2}$
* **Pedagogical Justification:** use $\cot\theta = x/y_0$, which is valid for every $t$ (including $x = 0$, where $\tan\theta$ is infinite), and differentiate with the chain rule: $\frac{d}{dt}\cot\theta = -\csc^2\theta\,\dot{\theta}$ and $\csc^2\theta = 1/\sin^2\theta = r^2/y_0^2$.
$$ -\csc^2\theta\,\dot{\theta} = \frac{\dot{x}}{y_0} = \frac{v(t)}{y_0} \implies -\frac{r^2}{y_0^2}\dot{\theta} = \frac{v}{y_0} \implies \dot{\theta} = -\frac{v(t)\,y_0}{r(t)^2} \quad \blacksquare $$

##### (c) Proof that $\ddot{r} = \dfrac{v^2(t)\,y_0^2 + a_x\,x(t)\,r^2(t)}{r(t)^3}$
* **Pedagogical Justification:** differentiate $\dot{r} = vx/r$ with the quotient rule $\left(\frac{u}{w}\right)' = \frac{\dot{u}w - u\dot{w}}{w^2}$, with $u = vx$ and $w = r$.
$$ \dot{u} = \dot{v}x + v\dot{x} = a_xx + v^2, \qquad \dot{w} = \dot{r} = \frac{vx}{r}, \qquad \ddot{r} = \frac{\left(a_xx + v^2\right)r - vx\,\dfrac{vx}{r}}{r^2} = \frac{\left(a_xx + v^2\right)r^2 - v^2x^2}{r^3} $$
$$ \left(a_xx + v^2\right)r^2 - v^2x^2 = a_xxr^2 + v^2\left(r^2 - x^2\right) = a_xxr^2 + v^2y_0^2 \implies \ddot{r} = \frac{v^2y_0^2 + a_x\,x\,r^2}{r^3} \quad \blacksquare $$

##### (d) Proof that $\ddot{\theta} = y_0\dfrac{2v^2(t)\,x(t) - a_x\,r^2(t)}{r(t)^4}$
* **Pedagogical Justification:** differentiate $\dot{\theta} = -y_0\,v\,r^{-2}$ with the quotient rule, using $\dot{v} = a_x$ and $\frac{d}{dt}\left(r^2\right) = 2r\dot{r} = 2vx$:
$$ \ddot{\theta} = -y_0\,\frac{\dot{v}r^2 - v\,\frac{d}{dt}(r^2)}{r^4} = -y_0\,\frac{a_xr^2 - 2v^2x}{r^4} = y_0\,\frac{2v^2x - a_xr^2}{r^4} \quad \blacksquare $$

##### Position, velocity and acceleration in polar coordinates
* **Position and velocity:** $\mathbf{r} = r\,\mathbf{e}_r$ and, with (a) and (b),
$$ \mathbf{v} = \dot{r}\,\mathbf{e}_r + r\dot{\theta}\,\mathbf{e}_\theta = v\left(\frac{x}{r}\,\mathbf{e}_r - \frac{y_0}{r}\,\mathbf{e}_\theta\right) $$
* **Acceleration** $\mathbf{a} = a_r\mathbf{e}_r + a_\theta\mathbf{e}_\theta$ from the polar formula:
$$ a_r = \ddot{r} - r\dot{\theta}^2 = \frac{v^2y_0^2 + a_xxr^2}{r^3} - r\left(\frac{vy_0}{r^2}\right)^2 = \frac{v^2y_0^2 + a_xxr^2}{r^3} - \frac{v^2y_0^2}{r^3} = \frac{a_xxr^2}{r^3} = a_x\frac{x}{r} $$
$$ a_\theta = r\ddot{\theta} + 2\dot{r}\dot{\theta} = \frac{y_0\left(2v^2x - a_xr^2\right)}{r^3} + 2\,\frac{vx}{r}\left(-\frac{vy_0}{r^2}\right) = \frac{y_0\left(2v^2x - a_xr^2\right)}{r^3} - \frac{2v^2xy_0}{r^3} = -a_x\frac{y_0}{r} \implies \mathbf{a} = a_x\left(\frac{x}{r}\,\mathbf{e}_r - \frac{y_0}{r}\,\mathbf{e}_\theta\right) $$

#### 3.2 Forces
Not applicable: kinematics-only problem. The motion law along $x$ is given.

#### 3.3 Equations of Motion
Not applicable: kinematics-only problem. The acceleration $a_x$ is prescribed.

#### 3.4 Integration and Answers
##### Repeating the problem in Cartesian coordinates
* **Pedagogical Justification:** in the fixed Cartesian basis the unit vectors are constant, so the description is immediate; the polar result must agree with it through the change of basis.
$$ \mathbf{r} = x(t)\,\mathbf{i} + y_0\,\mathbf{j}, \qquad \mathbf{v} = v(t)\,\mathbf{i}, \qquad \mathbf{a} = a_x\,\mathbf{i} $$
* Converting with $\mathbf{i} = \cos\theta\,\mathbf{e}_r - \sin\theta\,\mathbf{e}_\theta = \frac{x}{r}\,\mathbf{e}_r - \frac{y_0}{r}\,\mathbf{e}_\theta$:
$$ \mathbf{v} = v\left(\frac{x}{r}\,\mathbf{e}_r - \frac{y_0}{r}\,\mathbf{e}_\theta\right), \qquad \mathbf{a} = a_x\left(\frac{x}{r}\,\mathbf{e}_r - \frac{y_0}{r}\,\mathbf{e}_\theta\right) $$
These equal the polar results of 3.1 identically.

### Phase 4: Interpretation & Checks
* **Dimensional check:** $[\dot{r}] = [vx/r] = \text{m/s}$ and $[\dot{\theta}] = [vy_0/r^2] = \text{s}^{-1}$; $[\ddot{r}] = \dfrac{(\text{m/s})^2\text{m}^2}{\text{m}^3} = \text{m/s}^2$ and $[\ddot{\theta}] = \dfrac{\text{m}\cdot(\text{m/s})^2\cdot\text{m}}{\text{m}^4} = \text{s}^{-2}$.
* **Limit $x \to \infty$ (aircraft far away):** $r \to x$, so $\dot{r} \to v$, $\dot{\theta} \to 0$, $a_r \to a_x$ and $a_\theta \to 0$: the line of sight aligns with the flight direction and the motion is purely radial.
* **Aircraft overhead ($x = 0$, $t = 0$):** $\dot{r} = 0$, $\dot{\theta} = -v_0/y_0$, $a_r = 0$ and $a_\theta = -a_x$; with $\theta = \pi/2$, $\mathbf{a} = a_x\mathbf{i} = -a_x\mathbf{e}_\theta$.
* **Invariance of the modulus:** $a_r^2 + a_\theta^2 = a_x^2\,\dfrac{x^2 + y_0^2}{r^2} = a_x^2$, equal to $\|a_x\mathbf{i}\|^2$ because $[{}_0R_1]$ is orthogonal.
* **Check against the official key:** `Problems.pdf` has no entry for Problem 4 in its solution keys, but the statement gives the four formulas (a) to (d) as targets, and they are proved above. Sympy confirms the four identities and $a_r = a_xx/r$, $a_\theta = -a_xy_0/r$ with zero residual.

---

## 📌 Problem 05: Plane and Towed Glider

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a tow plane $A$ flies horizontally at constant speed $v_A$ and tows a glider $B$ that gains altitude. The tow cable has length $r$ and forms an angle $\theta$ with the horizontal.
* **Hypotheses:** $v_A$ and the cable length $r$ are constant; $\mathbf{a}_A = \mathbf{0}$. The statement says that $\dot{\theta}$ is constant; the answer is requested as a function of $\theta$ and its derivatives, so we keep $\theta(t)$ general and particularise at the end ($\ddot{\theta} = 0$).
* **Constraints and degrees of freedom:** we place the origin at the altitude of $A$, so $y_A = 0$. The taut cable of constant length keeps $B$ at the distance $r$ from $A$: $\left(x_B - x_{A0} - v_At\right)^2 + y_B^2 = r^2$. This is a holonomic constraint that depends explicitly on time (rheonomic) because the position of $A$ is prescribed, and it is bilateral while the cable is taut. $B$ then has $\text{CDOF} = 2 - 1 = 1$: the angle $\theta$.
* **Coordinates:** $\theta(t)$ for the glider relative to $A$; the position of $A$ along the flight direction is $x_A(t) = x_{A0} + v_At$.
* **Parameters and units:** $v_A$ [m/s], $r$ [m], $\theta$ [rad], $\dot{\theta}$ [rad/s], $\ddot{\theta}$ [rad/s$^2$].

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $\mathcal{S}_0 = \{O; \mathbf{i}_0, \mathbf{j}_0\}$ with $\mathbf{i}_0$ horizontal in the direction of flight of $A$ and $\mathbf{j}_0$ vertical, upward.
* **Relative position of $B$ with respect to $A$:** the glider is behind and above the plane, so the vector from $A$ to $B$ points at the angle $\theta$ above the negative horizontal. Its components in $\mathcal{B}_0$ follow from the geometry of the cable:
$$ \mathbf{r}_{B/A} = -r\cos\theta\,\mathbf{i}_0 + r\sin\theta\,\mathbf{j}_0 $$
This is the only reading compatible with the glider gaining altitude as $\theta$ increases ($r\sin\theta$ grows with $\theta$ for $0 \lt \theta \lt \pi/2$).

### Phase 3: Derivation

#### 3.1 Kinematics
##### Position of the glider
* **Pedagogical Justification:** the position of $B$ is the position of $A$ plus the relative position, all written in the fixed basis, so that no derivative of a unit vector is needed.
$$ \mathbf{r}_A = \left(x_{A0} + v_At\right)\mathbf{i}_0, \qquad \mathbf{r}_B = \mathbf{r}_A + \mathbf{r}_{B/A} = \left(x_{A0} + v_At - r\cos\theta\right)\mathbf{i}_0 + r\sin\theta\,\mathbf{j}_0 $$

##### Velocity of the glider
* **Pedagogical Justification:** differentiate $\mathbf{r}_B$ in $\mathcal{S}_0$ with the chain rule, since $\theta$ depends on time and $r$ is constant:
$$ \frac{d}{dt}\left(-r\cos\theta\right) = r\sin\theta\,\dot{\theta}, \qquad \frac{d}{dt}\left(r\sin\theta\right) = r\cos\theta\,\dot{\theta} $$
$$ \mathbf{v}_B^0 = \left(v_A + r\dot{\theta}\sin\theta\right)\mathbf{i}_0 + r\dot{\theta}\cos\theta\,\mathbf{j}_0, \qquad v_B^0 = \sqrt{\left(v_A + r\dot{\theta}\sin\theta\right)^2 + \left(r\dot{\theta}\cos\theta\right)^2} $$

##### Acceleration of the glider
* **Pedagogical Justification:** differentiate each component of $\mathbf{v}_B^0$ with the product and chain rules:
$$ \frac{d}{dt}\left(v_A + r\dot{\theta}\sin\theta\right) = r\ddot{\theta}\sin\theta + r\dot{\theta}^2\cos\theta, \qquad \frac{d}{dt}\left(r\dot{\theta}\cos\theta\right) = r\ddot{\theta}\cos\theta - r\dot{\theta}^2\sin\theta $$
$$ \mathbf{a}_B^0 = \left(r\ddot{\theta}\sin\theta + r\dot{\theta}^2\cos\theta\right)\mathbf{i}_0 + \left(r\ddot{\theta}\cos\theta - r\dot{\theta}^2\sin\theta\right)\mathbf{j}_0 $$
* **Magnitude.** Expanding both squares,
$$ \left(r\ddot{\theta}\sin\theta + r\dot{\theta}^2\cos\theta\right)^2 = r^2\ddot{\theta}^2\sin^2\theta + 2r^2\ddot{\theta}\dot{\theta}^2\sin\theta\cos\theta + r^2\dot{\theta}^4\cos^2\theta $$
$$ \left(r\ddot{\theta}\cos\theta - r\dot{\theta}^2\sin\theta\right)^2 = r^2\ddot{\theta}^2\cos^2\theta - 2r^2\ddot{\theta}\dot{\theta}^2\sin\theta\cos\theta + r^2\dot{\theta}^4\sin^2\theta $$
and adding them, the cross terms $\pm 2r^2\ddot{\theta}\dot{\theta}^2\sin\theta\cos\theta$ cancel:
$$ \left(a_B^0\right)^2 = r^2\ddot{\theta}^2\left(\sin^2\theta + \cos^2\theta\right) + r^2\dot{\theta}^4\left(\cos^2\theta + \sin^2\theta\right) = r^2\ddot{\theta}^2 + r^2\dot{\theta}^4 $$

#### 3.2 Forces
Not applicable: kinematics-only problem. The motion of $A$ and the cable geometry are given.

#### 3.3 Equations of Motion
Not applicable: kinematics-only problem. No dynamic unknown appears.

#### 3.4 Integration and Answers
* **Pedagogical Justification:** the answers requested are the magnitudes of the velocity and of the acceleration of $B$ in $S_0$ as functions of $\theta$ and its derivatives:
$$ \boxed{v_B^0 = \sqrt{\left(v_A + r\dot{\theta}\sin\theta\right)^2 + \left(r\dot{\theta}\cos\theta\right)^2}}, \qquad \boxed{a_B^0 = \sqrt{r^2\ddot{\theta}^2 + r^2\dot{\theta}^4}} $$
* **Expanded speed.** Expanding the square in $v_B^0$ (valid for any $\theta(t)$, using $\sin^2\theta + \cos^2\theta = 1$): $v_B^0 = \sqrt{v_A^2 + 2v_Ar\dot{\theta}\sin\theta + r^2\dot{\theta}^2}$.
* **Constant rate of the statement.** With $\dot{\theta}$ constant, $\ddot{\theta} = 0$ and $a_B^0 = r\dot{\theta}^2$.

### Phase 4: Interpretation & Checks
* **Decoupling from the cruise speed:** the acceleration does not depend on $v_A$, because $\mathbf{a}_A = \mathbf{0}$ (uniform rectilinear translation). The glider accelerates only through its circular motion relative to $A$.
* **Limiting case $\ddot{\theta} = 0$:** the acceleration is purely centripetal, $a_B^0 = r\dot{\theta}^2$, directed along the cable toward $A$ (circular motion of $B$ around $A$).
* **Limit $\dot{\theta} \equiv 0$ (identically, so $\ddot{\theta} = 0$ too):** $\mathbf{v}_B^0 = v_A\,\mathbf{i}_0$ and $\mathbf{a}_B^0 = \mathbf{0}$: the glider moves rigidly with the plane. (If $\dot{\theta}$ only vanishes at one instant, $a_B^0 = r|\ddot{\theta}|$ there, not zero.)
* **Dimensional check:** $[r\ddot{\theta}] = [r\dot{\theta}^2] = \text{m}\cdot\text{s}^{-2}$ and $[v_A + r\dot{\theta}\sin\theta] = \text{m/s}$, so $a_B^0$ is in m/s$^2$ and $v_B^0$ in m/s.
* **Check against the official key:** the key of `Problems.pdf` is $v_B^0 = \sqrt{(v_A + r\dot{\theta}\sin\theta)^2 + (r\dot{\theta}\cos\theta)^2}$ and $a_B^0 = \sqrt{r^2\ddot{\theta}^2 + r^2\dot{\theta}^4}$ (read on the rendered page), identical to the result above. Sympy confirms both squares for an arbitrary function $\theta(t)$ with zero residual.

---

## 📌 Problem 06: Particle on Sinusoidal Curve

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a particle $P$ travels along the curve $y = \sin x$ with horizontal velocity $\dot{x} = 1$.
* **Hypotheses:** the data are in SI units, so $y = \sin x$ means $y = (1\ \text{m})\sin(x/1\ \text{m})$ and $\dot{x} = 1\ \text{m/s}$. We take $x(0) = 0$, so $x(t) = t$ (in these units).
* **Constraints and degrees of freedom:** the curve $y = \sin x$ is a holonomic, scleronomic constraint in the plane, so $\text{CDOF} = 2 - 1 = 1$. The coordinate is $x$, whose motion law is given.
* **Coordinates:** $x$ (and the arc length $s$ along the curve).

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $\mathcal{S}_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ with the curve in the $Oxy$ plane.
* **Parametric curve:** $\mathbf{r}(x) = x\,\mathbf{i}_0 + \sin x\,\mathbf{j}_0$, with $\dfrac{d\mathbf{r}}{dx} = \mathbf{i}_0 + \cos x\,\mathbf{j}_0$. The differential arc length is
$$ ds = \left\|\frac{d\mathbf{r}}{dx}\right\|dx = \sqrt{1 + \cos^2x}\,dx \equiv L(x)\,dx $$
* **Intrinsic basis.** $\mathbf{e}_t$ is the unit tangent and $\mathbf{e}_n$ points toward the centre of curvature (Notes Sec. 2.4). Both are obtained in 3.1. In the plane the normal can be written as the left normal $\mathbf{k}_0\times\mathbf{e}_t$ up to a sign, because the curve has inflection points where the centre of curvature switches sides:
$$ \mathbf{k}_0\times\mathbf{e}_t = \frac{-\cos x\,\mathbf{i}_0 + \mathbf{j}_0}{L(x)}, \qquad \mathbf{e}_n = \operatorname{sgn}(\sin x)\,\frac{\cos x\,\mathbf{i}_0 - \mathbf{j}_0}{L(x)} \quad (\sin x \ne 0) $$
* **Change of basis.** The matrix with the components of $\mathbf{e}_t$, $\mathbf{e}_n$ and $\mathbf{e}_b$ in $\mathcal{B}_0$ is, for $\sin x \ne 0$,
$$ [{}_0 R_{\text{tnb}}] = \frac{1}{L}\begin{pmatrix} 1 & \operatorname{sgn}(\sin x)\cos x & 0 \\ \cos x & -\operatorname{sgn}(\sin x) & 0 \\ 0 & 0 & -L\operatorname{sgn}(\sin x) \end{pmatrix}, \qquad \det = \frac{1}{L^3}\left(-L\operatorname{sgn}(\sin x)\right)\left(-\operatorname{sgn}(\sin x) - \operatorname{sgn}(\sin x)\cos^2x\right) = 1, \qquad R R^T = I $$
With $L^2 = 1 + \cos^2x$ and $\operatorname{sgn}^2 = 1$, the rows have unit norm ($(1 + \cos^2x)/L^2 = 1$, $(\cos^2x + 1)/L^2 = 1$, $L^2/L^2 = 1$) and are orthogonal (rows 1 and 2: $(\cos x - \operatorname{sgn}^2\cos x)/L^2 = 0$; row 3 has no common nonzero entry with the others), so $RR^T = I$.
For $\sin x \gt 0$, $\mathbf{e}_n$ is the right normal $-\mathbf{k}_0\times\mathbf{e}_t$ and $\mathbf{e}_b = -\mathbf{k}_0$; for $\sin x \lt 0$ it is the left normal and $\mathbf{e}_b = \mathbf{k}_0$. In both cases the triad is right-handed.

### Phase 3: Derivation

#### 3.1 Kinematics
##### Velocity and acceleration
* **Pedagogical Justification:** the position is expressed in the fixed basis, so the derivatives of the unit vectors vanish. With $\dot{x} = 1$ and $\ddot{x} = 0$ (chain rule $\dot{y} = \cos x\,\dot{x}$):
$$ \mathbf{v} = \dot{x}\,\mathbf{i}_0 + \cos x\,\dot{x}\,\mathbf{j}_0 = \mathbf{i}_0 + \cos x\,\mathbf{j}_0, \qquad v(x) = \sqrt{1 + \cos^2x} = L(x) $$
$$ \mathbf{a} = \frac{d\mathbf{v}}{dt} = \ddot{x}\,\mathbf{i}_0 + \left(-\sin x\,\dot{x}^2 + \cos x\,\ddot{x}\right)\mathbf{j}_0 = 0\,\mathbf{i}_0 - \sin x\,\mathbf{j}_0 = -\sin x\,\mathbf{j}_0 $$

##### (a) Intrinsic unit basis
* **Tangent:** $\mathbf{e}_t = \dfrac{d\mathbf{r}/dx}{\|d\mathbf{r}/dx\|} = \dfrac{\mathbf{i}_0 + \cos x\,\mathbf{j}_0}{L}$.
* **Pedagogical Justification (normal):** by the definition of the course, $d\mathbf{e}_t/ds = \mathbf{e}_n/\rho$, so $\mathbf{e}_n$ is the direction of $d\mathbf{e}_t/ds$. We differentiate with respect to $x$ (product rule, with $\frac{d}{dx}L^{-1} = -\frac{1}{2}L^{-3}\left(-2\cos x\sin x\right) = \sin x\cos x\,L^{-3}$) and use $ds = L\,dx$:
$$ \frac{d\mathbf{e}_t}{dx} = \frac{\sin x\cos x}{L^3}\left(\mathbf{i}_0 + \cos x\,\mathbf{j}_0\right) + \frac{1}{L}\left(-\sin x\,\mathbf{j}_0\right) = \frac{\sin x\cos x\,\mathbf{i}_0 + \left[\sin x\cos^2x - \sin x\left(1 + \cos^2x\right)\right]\mathbf{j}_0}{L^3} = -\frac{\sin x}{L^3}\left(-\cos x\,\mathbf{i}_0 + \mathbf{j}_0\right) $$
$$ \frac{d\mathbf{e}_t}{ds} = \frac{1}{L}\frac{d\mathbf{e}_t}{dx} = -\frac{\sin x}{L^4}\left(-\cos x\,\mathbf{i}_0 + \mathbf{j}_0\right) $$
* The norm of this vector is the curvature, and its direction is $\mathbf{e}_n$. The vector $-\cos x\,\mathbf{i}_0 + \mathbf{j}_0$ has norm $L$, so
$$ \left\|\frac{d\mathbf{e}_t}{ds}\right\| = \frac{|\sin x|}{L^3} = \frac{1}{\rho}, \qquad \mathbf{e}_n = -\operatorname{sgn}(\sin x)\,\frac{-\cos x\,\mathbf{i}_0 + \mathbf{j}_0}{L} = \operatorname{sgn}(\sin x)\,\frac{\cos x\,\mathbf{i}_0 - \mathbf{j}_0}{L} $$
* For $0 \lt x \lt \pi$ ($\sin x \gt 0$) the arch is concave down and $\mathbf{e}_n$ points downward; for $\pi \lt x \lt 2\pi$ it points upward. At the inflection points $x = k\pi$ the curvature vanishes and $\mathbf{e}_n$ is not defined ($\rho \to \infty$).
* **Binormal:** $\mathbf{e}_b = \mathbf{e}_t\times\mathbf{e}_n = -\operatorname{sgn}(\sin x)\,\mathbf{k}_0$, constant in each arch.

##### (c) Tangent and normal acceleration components
* **Pedagogical Justification:** project the acceleration on the intrinsic vectors:
$$ a_t = \mathbf{a}\cdot\mathbf{e}_t = \left(-\sin x\,\mathbf{j}_0\right)\cdot\frac{\mathbf{i}_0 + \cos x\,\mathbf{j}_0}{L} = -\frac{\sin x\cos x}{\sqrt{1 + \cos^2x}} $$
$$ a_n = \mathbf{a}\cdot\mathbf{e}_n = \left(-\sin x\,\mathbf{j}_0\right)\cdot\operatorname{sgn}(\sin x)\,\frac{\cos x\,\mathbf{i}_0 - \mathbf{j}_0}{L} = \operatorname{sgn}(\sin x)\,\frac{\sin x}{L} = \frac{|\sin x|}{\sqrt{1 + \cos^2x}} \ge 0 $$
* **Check:** $a_t^2 + a_n^2 = \dfrac{\sin^2x\left(\cos^2x + 1\right)}{1 + \cos^2x} = \sin^2x = \|\mathbf{a}\|^2$.

#### 3.2 Forces
Not applicable: kinematics-only problem. The curve and the motion law $\dot{x} = 1$ are given.

#### 3.3 Equations of Motion
Not applicable: kinematics-only problem. The motion is prescribed by the statement.

#### 3.4 Integration and Answers
##### (b) Arc-length parameter $s(x)$
* **Pedagogical Justification:** integrate the metric differential from $x = 0$ (taking $s(0) = 0$):
$$ s(x) = \int_0^x\sqrt{1 + \cos^2u}\,du $$
The integral cannot be written with elementary functions (extension: it is an incomplete elliptic integral of the second kind); the statement allows leaving it as an integral. Since the integrand satisfies $\sqrt{1 + \cos^2u} \ge 1 \gt 0$, $s(x)$ is strictly increasing, so it can be inverted to give $x(s)$.

##### (d) Radius of curvature
* **Pedagogical Justification:** from $a_n = v^2/\rho$, with $v^2 = 1 + \cos^2x$:
$$ \rho(x) = \frac{v^2}{a_n} = \frac{1 + \cos^2x}{|\sin x|/\sqrt{1 + \cos^2x}} = \boxed{\frac{\left(1 + \cos^2x\right)^{3/2}}{|\sin x|}} $$
As a check (extension), this is the standard curvature formula of a plane graph, $\rho = \dfrac{\left(1 + y'^2\right)^{3/2}}{|y''|}$, for $y' = \cos x$ and $y'' = -\sin x$.

### Phase 4: Interpretation & Checks
* **Dimensional check:** $[v] = \text{m/s}$, $[a_t] = [a_n] = \text{m/s}^2$, $[\rho] = [v^2/a_n] = \text{m}$ and $[s] = \left[\int\sqrt{1 + \cos^2u}\,du\right] = \text{m}$ (using the length scale $1$ m inside the sine).
* **Special points:** at the inflection points $x = k\pi$, $a_n = 0$ and $\rho \to \infty$ (locally straight). At the crest $x = \pi/2$: $v = 1\ \text{m/s}$, $a_t = 0$, $a_n = 1\ \text{m/s}^2$ and $\rho = 1$ m, equal to $1/|y''| = 1$ m; there $\mathbf{e}_n = -\mathbf{j}_0$, toward the centre of curvature below the crest. At $x = \pi/4$: $\rho = (3/2)^{3/2}/(\sqrt{2}/2) = 3\sqrt{3}/2 = 2.598$ m.
* **Arc length:** $s(\pi) = \int_0^\pi\sqrt{1 + \cos^2u}\,du = 3.8202$ m, greater than the horizontal distance $\pi$ m, as it must be.
* **Check against the official key:** `Problems.pdf` has no entry for Problem 6 in its solution keys, so the results are verified by independent derivation: sympy reproduces $a_t$, $a_n$, $a_t^2 + a_n^2 = \sin^2x$, the curvature $\|d\mathbf{e}_t/ds\| = |\sin x|/L^3$ and $\rho(\pi/2) = 1$, $\rho(\pi/4) = 3\sqrt{3}/2$; numerical quadrature gives $s(\pi) = 3.82020$ m.
