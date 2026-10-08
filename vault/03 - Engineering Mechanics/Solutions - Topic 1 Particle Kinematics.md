---
title: "Solutions — Topic 1: Fundamentals and Particle Kinematics"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Full Analytical Step-by-Step Solutions"
language: "English"
author: "Aerospace Engineering Multi-Agent Team"
date: "2026-09-23"
---

# 📚 Topic 1: Fundamentals and Particle Kinematics — Complete Analytical Solutions

This document contains the **exhaustive, zero-skip analytical solutions** for all 10 solvable problems in Topic 1 (*Particle Kinematics*) from the official UC3M problem collection (`Problems.pdf`).

Every problem is structured according to the **4-Phase Methodological Protocol**:
1. **Phase 1: Physical Statement, Hypotheses, CDOFs & Parameters**
2. **Phase 2: Reference Frames, Vector Bases & Rotation Matrices $[{}_0 R_1]$**
3. **Phase 3: Step-by-Step Mathematical Deduction with Continuous Pedagogical Justification**
   - Explicit time derivatives $\frac{d}{dt}(u\cdot v) = \dot{u}v + u\dot{v}$ and chain rule $\frac{df}{dt} = \frac{df}{du}\frac{du}{dt}$.
   - Explicit integrals $\int f(u)u'(t)\,dt$, primitives, and Barrow's rule evaluations.
   - Traceability to official course notes (`Notes.pdf`, Chapters 1–3).
4. **Phase 4: Physical Interpretation, Limiting Cases & Dimensional Verification (SI units)**

---

## 📌 Problem 01: Rocket Helical Trajectory (MIT OCW)

### Phase 1: Physical Statement, Hypotheses, CDOFs & Parameters
* **Physical System:** An out-of-control sounding rocket ascends following a regular circular helix around the vertical $z$-axis.
* **Hypotheses:** The cylinder radius $a > 0$, vertical ascent velocity $v_z > 0$, and angular spin rate $\omega > 0$ are strictly positive constants. The rocket is modeled as an ideal point particle $P$.
* **Configuration Degrees of Freedom (CDOFs):** The trajectory is purely kinematically prescribed by time $t$; thus, the particle has $\text{CDOF} = 1$ parameterized by time $t$ or arc length $s$.
* **Parameters & SI Units:** Radius $a\text{ [m]}$, angular frequency $\omega\text{ [rad/s]}$, vertical velocity $v_z\text{ [m/s]}$, time $t\text{ [s]}$.

### Phase 2: Reference Frames, Vector Bases & Rotation Matrices
* **Inertial Reference Frame:** $\mathcal{S}_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$, fixed to the launch site with vertical axis $\mathbf{k}_0$ aligned with $z$.
* **Cylindrical Moving Basis:** $\mathcal{B}_{\text{cyl}} = \{\mathbf{e}_R, \mathbf{e}_\theta, \mathbf{e}_z\}$.
  The transformation matrix from the inertial Cartesian basis $\mathcal{B}_0$ to the cylindrical basis $\mathcal{B}_{\text{cyl}}$ is the planar rotation matrix about $\mathbf{k}_0$:
  $$ [{}_0 R_{\text{cyl}}] = \begin{pmatrix} \cos(\omega t) & -\sin(\omega t) & 0 \\ \sin(\omega t) & \cos(\omega t) & 0 \\ 0 & 0 & 1 \end{pmatrix} $$
  The basis vector relationships are given by matrix-vector multiplication:
  $$ \begin{pmatrix} \mathbf{e}_R \\ \mathbf{e}_\theta \\ \mathbf{e}_z \end{pmatrix} = [{}_0 R_{\text{cyl}}]^T \begin{pmatrix} \mathbf{i}_0 \\ \mathbf{j}_0 \\ \mathbf{k}_0 \end{pmatrix} = \begin{pmatrix} \cos(\omega t)\mathbf{i}_0 + \sin(\omega t)\mathbf{j}_0 \\ -\sin(\omega t)\mathbf{i}_0 + \cos(\omega t)\mathbf{j}_0 \\ \mathbf{k}_0 \end{pmatrix} $$
* **Time Derivatives of Unit Vectors (Poisson's Theorem, Notes Sec. 3.2):**
  Since $\mathcal{B}_{\text{cyl}}$ rotates at angular velocity $\boldsymbol{\omega} = \omega\mathbf{k}_0 = \omega\mathbf{e}_z$:
  $$ \frac{d\mathbf{e}_R}{dt} = \boldsymbol{\omega} \times \mathbf{e}_R = (\omega\mathbf{e}_z) \times \mathbf{e}_R = \omega\mathbf{e}_\theta $$
  $$ \frac{d\mathbf{e}_\theta}{dt} = \boldsymbol{\omega} \times \mathbf{e}_\theta = (\omega\mathbf{e}_z) \times \mathbf{e}_\theta = -\omega\mathbf{e}_R $$
  $$ \frac{d\mathbf{e}_z}{dt} = \mathbf{0} $$
* **Orthonormality of $[{}_0 R_{\text{cyl}}]$:** $\det[{}_0 R_{\text{cyl}}] = \cos^2(\omega t) + \sin^2(\omega t) = 1$ and $[{}_0 R_{\text{cyl}}][{}_0 R_{\text{cyl}}]^T = I$ (checked symbolically with sympy).
* **Frenet basis from the cylindrical basis.** The components of $\mathbf{e}_t$, $\mathbf{e}_n$, $\mathbf{e}_b$ in $\mathcal{B}_{\text{cyl}}$ (obtained in Phase 3, part (c)) are the columns of the second change-of-basis matrix, with $V = \sqrt{a^2\omega^2 + v_z^2}$:
$$ [{}_{\text{cyl}} R_{\text{tnb}}] = \begin{pmatrix} 0 & -1 & 0 \ a\omega/V & 0 & -v_z/V \ v_z/V & 0 & a\omega/V \end{pmatrix}, \qquad \det = \frac{a^2\omega^2 + v_z^2}{V^2} = 1, \qquad R R^T = I $$
* The three columns have unit norm and are mutually orthogonal, so $R R^T = I$; the composition $[{}_0 R_{\text{tnb}}] = [{}_0 R_{\text{cyl}}][{}_{\text{cyl}} R_{\text{tnb}}]$ is again a proper rotation (determinant $1\cdot 1 = 1$). Both determinants and the products $R R^T$ were verified symbolically with sympy.

### Phase 3: Mathematical Deduction Step-by-Step with Continuous Justification

#### (a) Cartesian Position, Velocity, and Acceleration
* **Pedagogical Justification:** The position vector $\mathbf{r}(t)$ is directly defined by its Cartesian coordinates $(x(t), y(t), z(t))$ relative to the fixed origin $O$. Velocity and acceleration are obtained by direct term-by-term differentiation in the fixed inertial basis $\mathcal{B}_0$, where $\frac{d\mathbf{i}_0}{dt} = \frac{d\mathbf{j}_0}{dt} = \frac{d\mathbf{k}_0}{dt} = \mathbf{0}$.
* **Position Vector:**
  $$ \mathbf{r}(t) = a\cos(\omega t)\mathbf{i}_0 + a\sin(\omega t)\mathbf{j}_0 + v_z t\mathbf{k}_0 $$
* **Velocity Vector (Explicit Chain Rule):**
  $$ \mathbf{v}(t) = \frac{d\mathbf{r}}{dt} = \frac{d}{dt}[a\cos(\omega t)]\mathbf{i}_0 + \frac{d}{dt}[a\sin(\omega t)]\mathbf{j}_0 + \frac{d}{dt}[v_z t]\mathbf{k}_0 $$
  Applying the chain rule $\frac{d}{dt}\cos(\omega t) = -\omega\sin(\omega t)$ and $\frac{d}{dt}\sin(\omega t) = \omega\cos(\omega t)$:
  $$ \mathbf{v}(t) = -a\omega\sin(\omega t)\mathbf{i}_0 + a\omega\cos(\omega t)\mathbf{j}_0 + v_z\mathbf{k}_0 $$
* **Acceleration Vector (Explicit Chain Rule):**
  $$ \mathbf{a}(t) = \frac{d\mathbf{v}}{dt} = \frac{d}{dt}[-a\omega\sin(\omega t)]\mathbf{i}_0 + \frac{d}{dt}[a\omega\cos(\omega t)]\mathbf{j}_0 + \frac{d}{dt}[v_z]\mathbf{k}_0 $$
  $$ \mathbf{a}(t) = -a\omega^2\cos(\omega t)\mathbf{i}_0 - a\omega^2\sin(\omega t)\mathbf{j}_0 + 0\mathbf{k}_0 = -a\omega^2(\cos(\omega t)\mathbf{i}_0 + \sin(\omega t)\mathbf{j}_0) $$

#### (b) Cylindrical Position, Velocity, and Acceleration
* **Pedagogical Justification:** Cylindrical coordinates $(R, \theta, z)$ exploit the axial symmetry of the cylinder upon which the helix lies. Here, the radial distance $R(t) = \sqrt{x^2 + y^2} = a$ is constant, and the azimuthal angle is $\theta(t) = \omega t$.
* **Position in Cylindrical Coordinates:**
  $$ \mathbf{r}(t) = a\mathbf{e}_R + v_z t\mathbf{e}_z $$
* **Velocity Vector (Explicit Product Rule with Poisson Derivative):**
  $$ \mathbf{v}(t) = \frac{d}{dt}(a\mathbf{e}_R + v_z t\mathbf{e}_z) = a\frac{d\mathbf{e}_R}{dt} + \frac{d(v_z t)}{dt}\mathbf{e}_z + v_z t\frac{d\mathbf{e}_z}{dt} $$
  Substituting $\frac{d\mathbf{e}_R}{dt} = \omega\mathbf{e}_\theta$ and $\frac{d\mathbf{e}_z}{dt} = \mathbf{0}$:
  $$ \mathbf{v}(t) = a\omega\mathbf{e}_\theta + v_z\mathbf{e}_z $$
* **Acceleration Vector (Explicit Differentiation):**
  $$ \mathbf{a}(t) = \frac{d}{dt}(a\omega\mathbf{e}_\theta + v_z\mathbf{e}_z) = a\omega\frac{d\mathbf{e}_\theta}{dt} + 0 = a\omega(-\omega\mathbf{e}_R) = -a\omega^2\mathbf{e}_R $$

#### (c) Intrinsic Frenet-Serret Basis $\{\mathbf{e}_t, \mathbf{e}_n, \mathbf{e}_b\}$
* **Pedagogical Justification:** The Frenet-Serret intrinsic basis (Notes Sec. 2.4) decomposes motion naturally along the curve itself. The tangent vector $\mathbf{e}_t$ points in the direction of instantaneous velocity, the principal normal $\mathbf{e}_n$ points toward the center of curvature, and the binormal $\mathbf{e}_b = \mathbf{e}_t \times \mathbf{e}_n$ completes the right-handed orthonormal triad.
* **Unit Tangent Vector $\mathbf{e}_t$:**
  $$ \mathbf{e}_t = \frac{\mathbf{v}}{\|\mathbf{v}\|} = \frac{a\omega\mathbf{e}_\theta + v_z\mathbf{e}_z}{\sqrt{a^2\omega^2 + v_z^2}} $$
* **Unit Principal Normal Vector $\mathbf{e}_n$:**
  By definition of the intrinsic acceleration (Notes Eq. 2.14):
  $$ \mathbf{a} = \ddot{s}\mathbf{e}_t + \frac{\dot{s}^2}{\rho}\mathbf{e}_n $$
  Since the speed $v = \dot{s} = \sqrt{a^2\omega^2 + v_z^2}$ is strictly constant in time, the tangential acceleration vanishes:
  $$ \ddot{s} = \frac{dv}{dt} = 0 $$
  Therefore, the entire acceleration is purely normal:
  $$ \mathbf{a} = a_n\mathbf{e}_n = -a\omega^2\mathbf{e}_R $$
  Taking the norm of both sides yields the magnitude of normal acceleration:
  $$ a_n = \|\mathbf{a}\| = a\omega^2 $$
  Dividing $\mathbf{a}$ by its norm gives the unit normal vector:
  $$ \mathbf{e}_n = \frac{\mathbf{a}}{a_n} = \frac{-a\omega^2\mathbf{e}_R}{a\omega^2} = -\mathbf{e}_R $$
  The principal normal points radially inward toward the central axis of the cylinder!
* **Radius of Curvature $\rho$:**
  Using the relation $a_n = \frac{v^2}{\rho}$:
  $$ \rho = \frac{v^2}{a_n} = \frac{a^2\omega^2 + v_z^2}{a\omega^2} = a + \frac{v_z^2}{a\omega^2} $$
* **Unit Binormal Vector $\mathbf{e}_b$:**
  Computing the vector cross product in the cylindrical basis:
  $$ \mathbf{e}_b = \mathbf{e}_t \times \mathbf{e}_n = \left( \frac{a\omega\mathbf{e}_\theta + v_z\mathbf{e}_z}{\sqrt{a^2\omega^2 + v_z^2}} \right) \times (-\mathbf{e}_R) = \frac{-a\omega(\mathbf{e}_\theta \times \mathbf{e}_R) - v_z(\mathbf{e}_z \times \mathbf{e}_R)}{\sqrt{a^2\omega^2 + v_z^2}} $$
  Recalling cyclic cross products: $\mathbf{e}_\theta \times \mathbf{e}_R = -\mathbf{e}_z$ and $\mathbf{e}_z \times \mathbf{e}_R = \mathbf{e}_\theta$:
  $$ \mathbf{e}_b = \frac{-a\omega(-\mathbf{e}_z) - v_z\mathbf{e}_\theta}{\sqrt{a^2\omega^2 + v_z^2}} = \frac{-v_z\mathbf{e}_\theta + a\omega\mathbf{e}_z}{\sqrt{a^2\omega^2 + v_z^2}} $$

#### (d) Modulus of Velocity
* **Pedagogical Justification:** The speed $v(t) = \|\mathbf{v}(t)\|$ represents the scalar rate of distance traveled along the path.
* **Calculation:**
  $$ v = \|\mathbf{v}\| = \sqrt{(-a\omega\sin\omega t)^2 + (a\omega\cos\omega t)^2 + v_z^2} = \sqrt{a^2\omega^2(\sin^2\omega t + \cos^2\omega t) + v_z^2} = \sqrt{a^2\omega^2 + v_z^2} $$
  The speed is constant for all $t \ge 0$.

#### (e) Evolution of Arc Length Coordinate $s(t)$
* **Pedagogical Justification:** The arc-length coordinate $s(t)$ measures the distance traversed along the trajectory from the initial position at $t = 0$. By fundamental calculus:
  $$ s(t) = \int_0^t v(t')\,dt' $$
* **Definite Integration:**
  $$ s(t) = \int_0^t \sqrt{a^2\omega^2 + v_z^2}\,dt' = \sqrt{a^2\omega^2 + v_z^2} \left[ t' \right]_0^t = t\sqrt{a^2\omega^2 + v_z^2} $$

#### (f) Trajectory as a Function of Arc Length $s$
* **Pedagogical Justification:** To express the curve intrinsically independent of time, we invert $s(t)$ to obtain time as a function of arc length: $t(s) = \frac{s}{\sqrt{a^2\omega^2 + v_z^2}}$.
* **Substitution into Cartesian Coordinates:**
  $$ x(s) = a\cos\left( \frac{\omega s}{\sqrt{a^2\omega^2 + v_z^2}} \right) $$
  $$ y(s) = a\sin\left( \frac{\omega s}{\sqrt{a^2\omega^2 + v_z^2}} \right) $$
  $$ z(s) = \frac{v_z s}{\sqrt{a^2\omega^2 + v_z^2}} $$

#### (g) Center of Curvature $C$ at $(a, 0, 0)$
* **Pedagogical Justification:** The center of curvature $C$ of the osculating circle is displaced from particle $P$ along the principal normal $\mathbf{e}_n$ by the radius of curvature $\rho$ (Notes Eq. 2.15):
  $$ \mathbf{r}_C = \mathbf{r}_P + \rho\mathbf{e}_n $$
* **Evaluation at $(a, 0, 0)$:**
  At position $(a, 0, 0)$, $x(t) = a\cos(\omega t) = a \implies \omega t = 0 \implies t = 0$.
  At $t = 0$:
  - Position: $\mathbf{r}_P(0) = a\mathbf{i}_0$.
  - Unit normal: $\mathbf{e}_n(0) = -\mathbf{e}_R(0) = -(\cos(0)\mathbf{i}_0 + \sin(0)\mathbf{j}_0) = -\mathbf{i}_0$.
  - Radius of curvature: $\rho = a + \frac{v_z^2}{a\omega^2}$.
* **Algebraic Combination:**
  $$ \mathbf{r}_C = a\mathbf{i}_0 + \left(a + \frac{v_z^2}{a\omega^2}\right)(-\mathbf{i}_0) = a\mathbf{i}_0 - a\mathbf{i}_0 - \frac{v_z^2}{a\omega^2}\mathbf{i}_0 = -\frac{v_z^2}{a\omega^2}\mathbf{i}_0 $$
  In Cartesian coordinates:
  $$ C = \left( -\frac{v_z^2}{a\omega^2}, \, 0, \, 0 \right) $$

### Phase 4: Physical Interpretation, Limiting Cases & Dimensional Check
* **Dimensional Check:**
  - Velocity: $[a\omega] = [\text{m}][\text{s}^{-1}] = \text{m/s}$, $[v_z] = \text{m/s}$. $\implies \sqrt{a^2\omega^2 + v_z^2}$ has units $\text{m/s}$ (Consistent ✅).
  - Curvature center offset: $\left[\frac{v_z^2}{a\omega^2}\right] = \frac{[\text{m/s}]^2}{[\text{m}][\text{s}^{-1}]^2} = \frac{\text{m}^2/\text{s}^2}{\text{m}/\text{s}^2} = \text{m}$ (Consistent ✅).
* **Limiting Asymptotic Cases:**
  - If $v_z \to 0$ (planar circular motion): $\rho = a$, and $C = (0, 0, 0)$, the origin of the circle as expected physically.
  - If $\omega \to 0$ (pure vertical line ascent): $\rho \to \infty$, curvature vanishes, and the trajectory becomes a straight vertical line.

---

## 📌 Problem 02: Kinematics, Planar Spiral

### Phase 1: Physical Statement, Hypotheses, CDOFs & Parameters
* **Physical System:** A point particle $P$ moves along a logarithmic/exponential planar spiral $r(\theta) = \alpha e^{\beta\theta}$ with a prescribed power-law angular motion $\theta(t) = \delta t^n$.
* **Hypotheses:** $\alpha, \beta, \delta > 0$ are positive constants, $n > 0$ is an integer or real exponent, $t \ge 0$. Motion is strictly 2D planar in the $Oxy$ plane ($z = 0$).
* **Degrees of Freedom:** $\text{CDOF} = 1$ parameterized by time $t$.
* **Parameters & Units:** $[r] = \text{m} \implies [\alpha] = \text{m}$, $\beta$ is dimensionless ($[-]$), $[\theta] = \text{rad} \implies [\delta] = \text{rad}\cdot\text{s}^{-n}$.

### Phase 2: Reference Frames, Vector Bases & Rotation Matrices
* **Inertial Basis:** $\mathcal{B}_0 = \{\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$.
* **Polar Basis:** $\mathcal{B}_{\text{polar}} = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}_0\}$.
* **Rotation Matrix $[{}_0 R_\theta]$:**
  $$ [{}_0 R_\theta] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \quad \begin{pmatrix} \mathbf{e}_r \\ \mathbf{e}_\theta \\ \mathbf{k}_0 \end{pmatrix} = \begin{pmatrix} \cos\theta & \sin\theta & 0 \\ -\sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} \mathbf{i}_0 \\ \mathbf{j}_0 \\ \mathbf{k}_0 \end{pmatrix} $$
* **Time Derivatives of Polar Unit Vectors (Notes Sec. 2.6.2, Eqs. 2.25–2.26):**
  $$ \dot{\mathbf{e}}_r = \dot{\theta}\mathbf{e}_\theta, \quad \dot{\mathbf{e}}_\theta = -\dot{\theta}\mathbf{e}_r $$
* **Orthonormality of $[{}_0 R_\theta]$:** $\det[{}_0 R_\theta] = \cos^2\theta + \sin^2\theta = 1$ and $[{}_0 R_\theta][{}_0 R_\theta]^T = I$ (checked symbolically with sympy).
* **Intrinsic basis from the polar basis.** Since $\mathbf{v} = \dot{r}\,\mathbf{e}_r + r\dot{\theta}\,\mathbf{e}_\theta = r\dot{\theta}\,(\beta\,\mathbf{e}_r + \mathbf{e}_\theta)$ (Phase 3, part (a)), the unit tangent is $\mathbf{e}_t = (\beta\,\mathbf{e}_r + \mathbf{e}_\theta)/\sqrt{1+\beta^2}$ and the in-plane unit normal is $\mathbf{e}_n = \mathbf{k}_0 \times \mathbf{e}_t = (-\mathbf{e}_r + \beta\,\mathbf{e}_\theta)/\sqrt{1+\beta^2}$. Their components in $\{\mathbf{e}_r, \mathbf{e}_\theta\}$ are the columns of
$$ [{}_{\text{polar}} R_{\text{tn}}] = \frac{1}{\sqrt{1+\beta^2}}\begin{pmatrix} \beta & -1 \ 1 & \beta \end{pmatrix}, \qquad \det = \frac{\beta^2 + 1}{1 + \beta^2} = 1, \qquad R R^T = I $$
* This is a planar rotation by the constant angle $\psi = \arctan(1/\beta)$ (the equiangular property of the spiral). Sympy confirms that $\mathbf{a}\cdot\mathbf{e}_t$ and $\mathbf{a}\cdot\mathbf{e}_n$ reproduce the $a_t$ and $a_n$ of Phase 3, parts (d), with $a_n > 0$, so $\mathbf{e}_n$ points to the concave side.

### Phase 3: Mathematical Deduction Step-by-Step with Continuous Justification

#### (a) Radial and Transverse Velocity Components
* **Pedagogical Justification:** In polar coordinates, the velocity vector is given by $\mathbf{v} = \dot{r}\mathbf{e}_r + r\dot{\theta}\mathbf{e}_\theta$. The radial component $v_r = \dot{r}$ measures the expansion rate, while $v_\theta = r\dot{\theta}$ measures transverse rotation.
* **Explicit Chain Rule for $\dot{\theta}(t)$ and $\dot{r}(t)$:**
  $$ \theta(t) = \delta t^n \implies \dot{\theta}(t) = \frac{d}{dt}(\delta t^n) = n\delta t^{n-1} $$
  Using the chain rule $\dot{r} = \frac{dr}{d\theta}\dot{\theta}$:
  $$ \frac{dr}{d\theta} = \frac{d}{d\theta}(\alpha e^{\beta\theta}) = \alpha\beta e^{\beta\theta} = \beta r $$
  $$ \dot{r} = (\beta r)(n\delta t^{n-1}) = \beta n \delta t^{n-1} r = \alpha\beta n\delta t^{n-1} e^{\beta\delta t^n} $$
* **Components:**
  $$ v_r = \dot{r} = \beta n\delta t^{n-1} r $$
  $$ v_\theta = r\dot{\theta} = n\delta t^{n-1} r $$

#### (b) Radial and Transverse Acceleration Components
* **Pedagogical Justification:** The acceleration in polar coordinates (Notes Eq. 2.30) accounts for the curvature of the polar grid:
  $$ \mathbf{a} = a_r\mathbf{e}_r + a_\theta\mathbf{e}_\theta = (\ddot{r} - r\dot{\theta}^2)\mathbf{e}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\mathbf{e}_\theta $$
* **Second Time Derivatives (Explicit Product Rule):**
  $$ \ddot{\theta}(t) = \frac{d}{dt}(n\delta t^{n-1}) = n(n-1)\delta t^{n-2} $$
  For $\ddot{r}(t) = \frac{d}{dt}(\beta r \dot{\theta})$:
  $$ \ddot{r} = \beta(\dot{r}\dot{\theta} + r\ddot{\theta}) = \beta\left( (\beta r\dot{\theta})\dot{\theta} + r\ddot{\theta} \right) = \beta^2 r\dot{\theta}^2 + \beta r\ddot{\theta} $$
* **Radial Acceleration $a_r$:**
  $$ a_r = \ddot{r} - r\dot{\theta}^2 = (\beta^2 r\dot{\theta}^2 + \beta r\ddot{\theta}) - r\dot{\theta}^2 = (\beta^2 - 1)r\dot{\theta}^2 + \beta r\ddot{\theta} $$
  Substituting $\dot{\theta} = n\delta t^{n-1}$ and $\ddot{\theta} = n(n-1)\delta t^{n-2}$:
  $$ a_r = (\beta^2 - 1)r(n\delta t^{n-1})^2 + \beta r n(n-1)\delta t^{n-2} = n\delta t^{n-2} r \left[ (\beta^2 - 1)n\delta t^n + \beta(n-1) \right] $$
* **Transverse Acceleration $a_\theta$:**
  $$ a_\theta = r\ddot{\theta} + 2\dot{r}\dot{\theta} = r\ddot{\theta} + 2(\beta r\dot{\theta})\dot{\theta} = r\ddot{\theta} + 2\beta r\dot{\theta}^2 $$
  Substituting derivatives:
  $$ a_\theta = r n(n-1)\delta t^{n-2} + 2\beta r(n\delta t^{n-1})^2 = n\delta t^{n-2} r \left[ (n-1) + 2\beta n\delta t^n \right] $$

#### (c) Tangential and Normal Velocity Components
* **Pedagogical Justification:** In the intrinsic Frenet basis, the velocity vector is strictly tangential: $\mathbf{v} = v\mathbf{e}_t = v_t\mathbf{e}_t + 0\mathbf{e}_n$. Therefore, the normal velocity component is identically zero.
* **Calculation:**
  $$ v_t = v = \sqrt{v_r^2 + v_\theta^2} = \sqrt{(\beta r\dot{\theta})^2 + (r\dot{\theta})^2} = r\dot{\theta}\sqrt{\beta^2 + 1} = n\delta t^{n-1} r\sqrt{1 + \beta^2} $$
  $$ v_n = 0 $$

#### (d) Tangential and Normal Acceleration Components
* **Pedagogical Justification:** Tangential acceleration $a_t = \dot{v}$ measures the rate of change of speed, while normal acceleration $a_n = \frac{v^2}{\rho}$ measures directional turning.
* **Tangential Acceleration $a_t$ (Explicit Differentiation):**
  $$ a_t = \frac{d}{dt}(v) = \sqrt{1 + \beta^2}\frac{d}{dt}(r\dot{\theta}) = \sqrt{1 + \beta^2}(\dot{r}\dot{\theta} + r\ddot{\theta}) $$
  Substituting $\dot{r} = \beta r\dot{\theta}$:
  $$ a_t = \sqrt{1 + \beta^2}(\beta r\dot{\theta}^2 + r\ddot{\theta}) = \sqrt{1 + \beta^2} n\delta t^{n-2} r \left[ \beta n\delta t^n + (n-1) \right] $$
* **Normal Acceleration $a_n$:**
  Using the Pythagorean decomposition of the total acceleration magnitude: $\|\mathbf{a}\|^2 = a_t^2 + a_n^2 = a_r^2 + a_\theta^2$:
  $$ a_n = \sqrt{a_r^2 + a_\theta^2 - a_t^2} $$
  Alternatively, using the cross product $\mathbf{a} \times \mathbf{v} = (a_t\mathbf{e}_t + a_n\mathbf{e}_n) \times (v\mathbf{e}_t) = -v a_n\mathbf{e}_b$:
  $$ a_n = \frac{\|\mathbf{v} \times \mathbf{a}\|}{v} = \frac{|v_r a_\theta - v_\theta a_r|}{v} $$
  Computing the numerator:
  $$ v_r a_\theta - v_\theta a_r = (\beta r\dot{\theta})(r\ddot{\theta} + 2\beta r\dot{\theta}^2) - (r\dot{\theta})((\beta^2 - 1)r\dot{\theta}^2 + \beta r\ddot{\theta}) $$
  $$ = \beta r^2\dot{\theta}\ddot{\theta} + 2\beta^2 r^2\dot{\theta}^3 - (\beta^2 - 1)r^2\dot{\theta}^3 - \beta r^2\dot{\theta}\ddot{\theta} = (2\beta^2 - \beta^2 + 1)r^2\dot{\theta}^3 = (\beta^2 + 1)r^2\dot{\theta}^3 $$
  Dividing by $v = r\dot{\theta}\sqrt{\beta^2 + 1}$:
  $$ a_n = \frac{(\beta^2 + 1)r^2\dot{\theta}^3}{r\dot{\theta}\sqrt{\beta^2 + 1}} = r\dot{\theta}^2\sqrt{\beta^2 + 1} = n^2\delta^2 t^{2n-2} r\sqrt{1 + \beta^2} $$

#### (e) Radius of Curvature of the Spiral
* **Pedagogical Justification:** The radius of curvature is obtained directly from $a_n = \frac{v^2}{\rho} \implies \rho = \frac{v^2}{a_n}$.
* **Calculation:**
  $$ \rho = \frac{v^2}{a_n} = \frac{(r\dot{\theta}\sqrt{1 + \beta^2})^2}{r\dot{\theta}^2\sqrt{1 + \beta^2}} = \frac{r^2\dot{\theta}^2(1 + \beta^2)}{r\dot{\theta}^2\sqrt{1 + \beta^2}} = r\sqrt{1 + \beta^2} $$

### Phase 4: Physical Interpretation, Limiting Cases & Dimensional Check
* **Geometric Invariance:** In a logarithmic spiral $r = \alpha e^{\beta\theta}$, the angle $\psi$ between the radial line and the tangent vector satisfies $\tan\psi = \frac{r}{dr/d\theta} = \frac{r}{\beta r} = \frac{1}{\beta} = \text{constant}$. This is the celebrated equiangular spiral property!
* **Radius of Curvature:** $\rho = r\sqrt{1 + \beta^2}$ is strictly proportional to current radial distance $r$.
* **Units Check:** $[\rho] = [r][\sqrt{1+\beta^2}] = \text{m} \cdot 1 = \text{m}$ (Consistent ✅).
* **Limiting Case $\beta \to 0$:** The spiral degenerates into a pure circle $r = \alpha$, where $\rho = r\sqrt{1 + 0} = r$, recovering the circle radius of curvature.

---

## 📌 Problem 03: Kinematics, Astroid

### Phase 1: Physical Statement, Hypotheses, CDOFs & Parameters
* **Physical System:** A point particle $P$ moves along a hypocycloid with four cusps (an astroid), parameterized by angle $\phi$.
* **Hypotheses:** The motion starts from rest at $\phi(0) = 0$ with constant tangential acceleration $a_t = k = \text{const} > 0$. The particle remains within the first quadrant segment $0 \le \phi \le \pi/2$.
* **Degrees of Freedom:** $\text{CDOF} = 1$.
* **Parameters & Units:** Astroid scale $a\text{ [m]}$, tangential acceleration $k\text{ [m/s}^2\text{]}$, time $t\text{ [s]}$.

### Phase 2: Reference Frames, Vector Bases & Coordinate Geometry
* **Inertial Cartesian Frame:** $\mathcal{S}_0 = \{O; \mathbf{i}_0, \mathbf{j}_0\}$.
* **Parametric Equations of the Astroid:**
  $$ x(\phi) = a\cos^3\phi, \quad y(\phi) = a\sin^3\phi $$
* **Metric Arc Length Differential $ds$:**
  Differentiating with respect to parameter $\phi$:
  $$ dx = \frac{dx}{d\phi}d\phi = 3a\cos^2\phi(-\sin\phi)d\phi = -3a\cos^2\phi\sin\phi\,d\phi $$
  $$ dy = \frac{dy}{d\phi}d\phi = 3a\sin^2\phi(\cos\phi)d\phi = 3a\sin^2\phi\cos\phi\,d\phi $$
  The squared differential arc length is:
  $$ ds^2 = dx^2 + dy^2 = 9a^2\cos^4\phi\sin^2\phi\,d\phi^2 + 9a^2\sin^4\phi\cos^2\phi\,d\phi^2 $$
  Factoring out $9a^2\cos^2\phi\sin^2\phi$:
  $$ ds^2 = 9a^2\cos^2\phi\sin^2\phi(\cos^2\phi + \sin^2\phi)d\phi^2 = 9a^2\cos^2\phi\sin^2\phi\,d\phi^2 $$
  Taking the positive square root for $0 \le \phi \le \pi/2$:
  $$ ds = 3a\sin\phi\cos\phi\,d\phi = \frac{3a}{2}\sin(2\phi)\,d\phi $$

### Phase 3: Mathematical Deduction Step-by-Step with Continuous Justification

#### Step 1: Intrinsic Kinematics from Constant Tangential Acceleration $a_t = k$
* **Pedagogical Justification:** Tangential acceleration is the time derivative of speed: $a_t = \frac{dv}{dt} = \ddot{s}$. Integrating once with initial condition $v(0) = 0$:
  $$ v(t) = \dot{s}(t) = \int_0^t a_t\,dt' = \int_0^t k\,dt' = kt $$
* **Second Integration for Arc Length $s(t)$:**
  Integrating $v(t) = \dot{s}(t)$ with initial condition $s(0) = 0$ (at $\phi = 0$):
  $$ s(t) = \int_0^t kt'\,dt' = \left[ \frac{1}{2}kt'^2 \right]_0^t = \frac{1}{2}kt^2 $$

#### Step 2: Arc Length as a Function of Parameter $\phi$
* **Pedagogical Justification:** We integrate the geometric differential $ds = 3a\sin u\cos u\,du$ from the origin $\phi = 0$ to current $\phi$:
* **Explicit Substitution Integration:**
  Let $w = \sin u \implies dw = \cos u\,du$. When $u = 0$, $w = 0$; when $u = \phi$, $w = \sin\phi$:
  $$ s(\phi) = \int_0^\phi 3a\sin u\cos u\,du = 3a\int_0^{\sin\phi} w\,dw = 3a\left[ \frac{w^2}{2} \right]_0^{\sin\phi} = \frac{3a}{2}\sin^2\phi $$

#### Step 3: Equating Kinematic and Geometric Arc Length
* **Pedagogical Justification:** The distance traveled along the curve $s(t)$ must equal the geometric arc length $s(\phi)$:
  $$ \frac{3a}{2}\sin^2\phi = \frac{1}{2}kt^2 $$
  Multiplying both sides by $\frac{2}{3a}$:
  $$ \sin^2\phi = \frac{kt^2}{3a} $$
  Taking the positive square root (since $0 \le \phi \le \pi/2$):
  $$ \sin\phi = \sqrt{\frac{k}{3a}}\,t $$
  Applying the inverse sine function:
  $$ \phi(t) = \arcsin\left( \sqrt{\frac{k}{3a}}\,t \right) $$
  *(Compare with the official solution key (Problems.pdf, Solution keys section): $\phi = \arcsin\sqrt{\frac{k}{3a}t^2} = \arcsin(\sqrt{\frac{k}{3a}}t)$.)*

#### Step 4: Evolution of the Cartesian Position as a Function of Time
* **Pedagogical Justification:** Substituting $\phi(t)$ into the parametric definitions of the astroid:
  Using trigonometric identities: $\sin\phi = \sqrt{\frac{k}{3a}}t$ and $\cos\phi = \sqrt{1 - \sin^2\phi} = \sqrt{1 - \frac{k t^2}{3a}}$:
  $$ x(t) = a\cos^3\phi = a\left( 1 - \frac{kt^2}{3a} \right)^{3/2} $$
  $$ y(t) = a\sin^3\phi = a\left( \frac{kt^2}{3a} \right)^{3/2} = a\left(\frac{k}{3a}\right)^{3/2}t^3 $$

### Phase 4: Physical Interpretation, Limiting Cases & Dimensional Check
* **Dimensional Check:**
  - In $\sin\phi = \sqrt{\frac{k}{3a}}t$:
    $$ \left[ \sqrt{\frac{k}{3a}}\,t \right] = \sqrt{\frac{\text{m/s}^2}{\text{m}}}\,\text{s} = \sqrt{\text{s}^{-2}}\,\text{s} = \text{s}^{-1}\cdot\text{s} = 1 \quad (\text{Dimensionless} \, \text{argument} \, \text{for} \, \arcsin! \, ✅) $$
* **Physical Limits:**
  - At $t = 0$: $\phi = 0 \implies x(0) = a, y(0) = 0$ (starts at the right cusp).
  - The particle reaches the top cusp $\phi = \pi/2$ when $\sin\phi = 1$:
    $$ \sqrt{\frac{k}{3a}}t_{\text{cusp}} = 1 \implies t_{\text{cusp}} = \sqrt{\frac{3a}{k}} $$
  At $t_{\text{cusp}}$, $x(t_{\text{cusp}}) = 0, y(t_{\text{cusp}}) = a$.

---

## 📌 Problem 04: Plane at Constant Altitude (Cartesian vs. Polar Tracking)

### Phase 1: Physical Statement, Hypotheses, CDOFs & Parameters
* **Physical System:** An aircraft flies at constant altitude $y_0$ with velocity in the $x$ direction. At $t = 0$, $x(0) = 0$ and velocity is $v_0$. It accelerates in the $x$ direction at constant rate $a_x$.
* **Tracking System:** A ground radar station located at origin $O(0,0)$ tracks the aircraft using range $r(t)$ and elevation/bearing angle $\theta(t)$.
* **Hypotheses:** $y_0 > 0, v_0 \ge 0, a_x = \text{const}$. Altitude is fixed: $y(t) \equiv y_0 \implies \dot{y} = 0, \ddot{y} = 0$.

### Phase 2: Reference Frames & Transformation Relations
* **Inertial Cartesian Frame:** Coordinates $(x, y)$ with position $\mathbf{r} = x\mathbf{i} + y_0\mathbf{j}$.
* **Radar Polar Frame:** Position $\mathbf{r} = r\mathbf{e}_r$, where:
  $$ r(t) = \sqrt{x(t)^2 + y_0^2}, \quad \tan\theta(t) = \frac{y_0}{x(t)} \implies \theta(t) = \arctan\left(\frac{y_0}{x(t)}\right) $$
* **Kinematics in $x$:**
  $$ \dot{x}(t) = v(t) = v_0 + a_x t, \quad \ddot{x}(t) = a_x $$
  $$ x(t) = v_0 t + \frac{1}{2}a_x t^2 $$
* **Change of basis (radar polar basis).** With $\theta$ the angle of the line of sight measured from $+\mathbf{i}$, the polar basis $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}\}$ is the inertial basis $\mathcal{B}_0 = \{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$ rotated by $\theta(t)$ about $\mathbf{k}$. The columns are the components of $\mathbf{e}_r$, $\mathbf{e}_\theta$, $\mathbf{k}$ in $\mathcal{B}_0$; using $\cos\theta = x/r$ and $\sin\theta = y_0/r$:
$$ [{}_0 R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \ \sin\theta & \cos\theta & 0 \ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} x/r & -y_0/r & 0 \ y_0/r & x/r & 0 \ 0 & 0 & 1 \end{pmatrix} $$
$$ \det[{}_0 R_1] = \frac{x^2 + y_0^2}{r^2} = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
* Both properties were verified symbolically with sympy. The inverse relation $\mathbf{i} = \cos\theta\,\mathbf{e}_r - \sin\theta\,\mathbf{e}_\theta$ (first row of $[{}_0 R_1]^T$ applied to the basis) is the one used in the Cartesian cross-check of Phase 3.

### Phase 3: Mathematical Deduction Step-by-Step with Continuous Justification

#### (a) Proof that $\dot{r} = \frac{v(t)x(t)}{r(t)}$
* **Pedagogical Justification:** Starting from the geometric relation $r(t)^2 = x(t)^2 + y_0^2$, we differentiate implicitly with respect to time $t$.
* **Implicit Differentiation:**
  $$ \frac{d}{dt}[r^2] = \frac{d}{dt}[x^2 + y_0^2] $$
  Applying the chain rule $\frac{d}{dt}(r^2) = 2r\dot{r}$ and $\frac{d}{dt}(x^2) = 2x\dot{x}$:
  $$ 2r\dot{r} = 2x\dot{x} + 0 = 2x v(t) $$
  Dividing by $2r$:
  $$ \dot{r} = \frac{v(t)x(t)}{r(t)} \quad \blacksquare $$

#### (b) Proof that $\dot{\theta} = -\frac{v(t)y_0}{r(t)^2}$
* **Pedagogical Justification:** Starting from $\tan\theta = \frac{y_0}{x}$, we differentiate both sides with respect to time using the quotient rule.
* **Differentiation:**
  $$ \frac{d}{dt}(\tan\theta) = \frac{d}{dt}\left( \frac{y_0}{x} \right) $$
  Recalling $\frac{d}{dt}(\tan\theta) = (1 + \tan^2\theta)\dot{\theta} = \sec^2\theta\,\dot{\theta}$, and $\frac{d}{dt}(x^{-1}) = -\frac{\dot{x}}{x^2} = -\frac{v}{x^2}$:
  $$ \sec^2\theta\,\dot{\theta} = -\frac{y_0 v(t)}{x(t)^2} $$
  From geometry: $\cos\theta = \frac{x}{r} \implies \sec\theta = \frac{r}{x} \implies \sec^2\theta = \frac{r^2}{x^2}$:
  $$ \frac{r^2}{x^2}\dot{\theta} = -\frac{y_0 v(t)}{x^2} $$
  Multiplying both sides by $x^2$ and dividing by $r^2$:
  $$ \dot{\theta} = -\frac{v(t)y_0}{r(t)^2} \quad \blacksquare $$

#### (c) Proof that $\ddot{r} = \frac{v^2(t)y_0^2 + a_x x(t)r^2(t)}{r(t)^3}$
* **Pedagogical Justification:** We differentiate the expression for $\dot{r} = \frac{v x}{r}$ using the quotient rule $\left(\frac{u}{w}\right)' = \frac{u'w - uw'}{w^2}$.
* **Differentiation:**
  Here $u = v x \implies \dot{u} = \dot{v}x + v\dot{x} = a_x x + v^2$.
  The denominator is $w = r \implies \dot{w} = \dot{r} = \frac{vx}{r}$.
  $$ \ddot{r} = \frac{\dot{u}r - u\dot{r}}{r^2} = \frac{(a_x x + v^2)r - (vx)\left( \frac{vx}{r} \right)}{r^2} $$
  Multiplying numerator and denominator by $r$:
  $$ \ddot{r} = \frac{(a_x x + v^2)r^2 - v^2 x^2}{r^3} $$
  Expanding the numerator:
  $$ (a_x x + v^2)r^2 - v^2 x^2 = a_x x r^2 + v^2 r^2 - v^2 x^2 = a_x x r^2 + v^2(r^2 - x^2) $$
  Recalling that $r^2 - x^2 = y_0^2$:
  $$ \ddot{r} = \frac{a_x x(t)r^2(t) + v^2(t)y_0^2}{r(t)^3} = \frac{v^2(t)y_0^2 + a_x x(t)r^2(t)}{r(t)^3} \quad \blacksquare $$

#### (d) Proof that $\ddot{\theta} = y_0\frac{2v^2(t)x(t) - a_x r^2(t)}{r(t)^4}$
* **Pedagogical Justification:** We differentiate $\dot{\theta} = -y_0 v r^{-2}$ with respect to time using the product rule.
* **Differentiation:**
  $$ \ddot{\theta} = \frac{d}{dt}\left( -y_0 \frac{v}{r^2} \right) = -y_0 \frac{\dot{v}r^2 - v\frac{d}{dt}(r^2)}{r^4} $$
  Substituting $\dot{v} = a_x$ and $\frac{d}{dt}(r^2) = 2r\dot{r} = 2r\left(\frac{vx}{r}\right) = 2vx$:
  $$ \ddot{\theta} = -y_0 \frac{a_x r^2 - v(2vx)}{r^4} = -y_0 \frac{a_x r^2 - 2v^2 x}{r^4} = y_0 \frac{2v^2(t)x(t) - a_x r^2(t)}{r(t)^4} \quad \blacksquare $$

#### Polar and Cartesian Acceleration Vectors
* **Polar Acceleration Vector:**
  $$ a_r = \ddot{r} - r\dot{\theta}^2 = \frac{v^2 y_0^2 + a_x x r^2}{r^3} - r\left( -\frac{v y_0}{r^2} \right)^2 = \frac{v^2 y_0^2 + a_x x r^2}{r^3} - \frac{v^2 y_0^2}{r^3} = \frac{a_x x r^2}{r^3} = a_x\frac{x}{r} $$
  $$ a_\theta = r\ddot{\theta} + 2\dot{r}\dot{\theta} = r\left( y_0\frac{2v^2 x - a_x r^2}{r^4} \right) + 2\left(\frac{vx}{r}\right)\left(-\frac{vy_0}{r^2}\right) = \frac{2v^2 x y_0 - a_x y_0 r^2}{r^3} - \frac{2v^2 x y_0}{r^3} = -a_x\frac{y_0}{r} $$
  $$ \mathbf{a} = a_x\left( \frac{x}{r}\mathbf{e}_r - \frac{y_0}{r}\mathbf{e}_\theta \right) $$
* **Cartesian Verification:**
  In Cartesian coordinates:
  $$ \mathbf{a} = \ddot{x}\mathbf{i}_0 + \ddot{y}\mathbf{j}_0 = a_x\mathbf{i}_0 + 0\mathbf{j}_0 = a_x\mathbf{i}_0 $$
  Converting Cartesian $\mathbf{i}_0$ into polar: $\mathbf{i}_0 = \cos\theta\mathbf{e}_r - \sin\theta\mathbf{e}_\theta = \frac{x}{r}\mathbf{e}_r - \frac{y_0}{r}\mathbf{e}_\theta$.
  Substituting gives identically $\mathbf{a} = a_x\left(\frac{x}{r}\mathbf{e}_r - \frac{y_0}{r}\mathbf{e}_\theta\right)$. The match is mathematically exact!

### Phase 4: Physical Interpretation, Limiting Cases and Dimensional Check
* **Dimensional check:**
  - $[\dot{r}] = [v\,x/r] = \text{m/s}$; $\quad [\dot{\theta}] = [v\,y_0/r^2] = \dfrac{(\text{m/s})\,\text{m}}{\text{m}^2} = \text{s}^{-1}$ (rad/s).
  - $[\ddot{r}] = \dfrac{(\text{m}^2/\text{s}^2)\,\text{m}^2}{\text{m}^3} = \text{m/s}^2$ and $\dfrac{(\text{m/s}^2)\,\text{m}\,\text{m}^2}{\text{m}^3} = \text{m/s}^2$; $\quad [\ddot{\theta}] = \dfrac{\text{m}\,(\text{m}^2/\text{s}^2)\,\text{m}}{\text{m}^4} = \text{s}^{-2}$ (Consistent).
* **Limit $x \to \infty$ (aircraft far away):** $r \to x$, so $\dot{r} \to v$, $\dot{\theta} \to 0$, $a_r \to a_x$, $a_\theta \to 0$: the line of sight aligns with the flight direction and the motion is purely radial.
* **Limit $x = 0$ (aircraft overhead, $t = 0$):** $\dot{r} = 0$, $\dot{\theta} = -v_0/y_0$, $a_r = 0$, $a_\theta = -a_x$. Then $\theta = \pi/2$ and $\mathbf{a} = a_x\mathbf{i} = -a_x\mathbf{e}_\theta$, as required by the change of basis.
* **Invariance of the modulus:** $a_r^2 + a_\theta^2 = a_x^2\,\dfrac{x^2 + y_0^2}{r^2} = a_x^2$, equal to $\|a_x\mathbf{i}\|^2$ because $[{}_0 R_1]$ is orthogonal.
* **Symbolic check (sympy):** differentiating $r = \sqrt{x^2 + y_0^2}$ and $\theta = \arctan(y_0/x)$ with $x = v_0 t + \tfrac{1}{2}a_x t^2$ reproduces the four identities (a)-(d) with zero residual, and gives $a_r = a_x x/r$, $a_\theta = -a_x y_0/r$ with zero residual; the three limits above were obtained with sympy as well.

---

## 📌 Problem 05: Plane and Towed Glider

### Phase 1: Physical Statement, Hypotheses, CDOFs & Parameters
* **Physical System:** Tow plane $A$ flies horizontally at constant speed $v_A$. Glider $B$ is towed behind on a cable of constant length $r$. The tow angle $\theta(t)$ above the horizontal increases at rate $\dot{\theta}(t)$.
* **Hypotheses:** Cable length $r = \text{const}$, plane speed $v_A = \text{const}$ (so $\dot{v}_A = 0, \mathbf{a}_A = \mathbf{0}$).
* **Parameters & Units:** Plane speed $v_A\text{ [m/s]}$, cable length $r\text{ [m]}$, angle $\theta\text{ [rad]}$, angular rate $\dot{\theta}\text{ [rad/s]}$, angular acceleration $\ddot{\theta}\text{ [rad/s}^2\text{]}$.

### Phase 2: Reference Frames, Vector Bases & Coordinate Transformation
* **Inertial Reference Frame:** $\mathcal{S}_0 = \{O; \mathbf{i}_0, \mathbf{j}_0\}$, with $\mathbf{i}_0$ pointing horizontally in plane $A$'s direction of flight, and $\mathbf{j}_0$ pointing vertically upward.
* **Position of Plane $A$:**
  $$ \mathbf{r}_A(t) = (x_{A0} + v_A t)\mathbf{i}_0 $$
* **Relative Position of Glider $B$ with Respect to $A$:**
  Since the glider is behind and above/below $A$, the vector from $A$ to $B$ is oriented at angle $\theta$ below the negative horizontal:
  $$ \mathbf{r}_{B/A} = -r\cos\theta\,\mathbf{i}_0 + r\sin\theta\,\mathbf{j}_0 $$
  The total position of glider $B$ in $\mathcal{S}_0$ is:
  $$ \mathbf{r}_B = \mathbf{r}_A + \mathbf{r}_{B/A} = (x_{A0} + v_A t - r\cos\theta)\mathbf{i}_0 + (r\sin\theta)\mathbf{j}_0 $$

### Phase 3: Mathematical Deduction Step-by-Step with Continuous Justification

#### Velocity of Glider $B$
* **Pedagogical Justification:** The absolute velocity is obtained by differentiating position $\mathbf{r}_B$ in the inertial frame $\mathcal{S}_0$:
  $$ \mathbf{v}_{B/0} = \frac{d\mathbf{r}_B}{dt} = \frac{d}{dt}(x_{A0} + v_A t - r\cos\theta)\mathbf{i}_0 + \frac{d}{dt}(r\sin\theta)\mathbf{j}_0 $$
* **Explicit Chain Rule:**
  $$ \frac{d}{dt}(-r\cos\theta) = -r(-\sin\theta)\dot{\theta} = r\dot{\theta}\sin\theta $$
  $$ \frac{d}{dt}(r\sin\theta) = r\cos\theta\,\dot{\theta} $$
  Therefore:
  $$ \mathbf{v}_{B/0} = (v_A + r\dot{\theta}\sin\theta)\mathbf{i}_0 + (r\dot{\theta}\cos\theta)\mathbf{j}_0 $$
* **Magnitude of Velocity $v_{B/0}$:**
  $$ v_{B/0} = \|\mathbf{v}_{B/0}\| = \sqrt{(v_A + r\dot{\theta}\sin\theta)^2 + (r\dot{\theta}\cos\theta)^2} $$
  *(Compare with the official solution key (Problems.pdf, Solution keys section).)*

#### Acceleration of Glider $B$
* **Pedagogical Justification:** Acceleration is the time derivative of velocity $\mathbf{a}_{B/0} = \frac{d\mathbf{v}_{B/0}}{dt}$.
* **Explicit Product & Chain Rules for Each Component:**
  - $x$-component differentiation:
    $$ \frac{d}{dt}(v_A + r\dot{\theta}\sin\theta) = 0 + r\frac{d}{dt}(\dot{\theta}\sin\theta) = r(\ddot{\theta}\sin\theta + \dot{\theta}(\cos\theta\dot{\theta})) = r\ddot{\theta}\sin\theta + r\dot{\theta}^2\cos\theta $$
  - $y$-component differentiation:
    $$ \frac{d}{dt}(r\dot{\theta}\cos\theta) = r\frac{d}{dt}(\dot{\theta}\cos\theta) = r(\ddot{\theta}\cos\theta + \dot{\theta}(-\sin\theta\dot{\theta})) = r\ddot{\theta}\cos\theta - r\dot{\theta}^2\sin\theta $$
* **Vector Form:**
  $$ \mathbf{a}_{B/0} = (r\ddot{\theta}\sin\theta + r\dot{\theta}^2\cos\theta)\mathbf{i}_0 + (r\ddot{\theta}\cos\theta - r\dot{\theta}^2\sin\theta)\mathbf{j}_0 $$
* **Magnitude of Acceleration $a_{B/0}$:**
  $$ a_{B/0}^2 = (r\ddot{\theta}\sin\theta + r\dot{\theta}^2\cos\theta)^2 + (r\ddot{\theta}\cos\theta - r\dot{\theta}^2\sin\theta)^2 $$
  Expanding both squared terms:
  $$ = r^2\ddot{\theta}^2\sin^2\theta + 2r^2\ddot{\theta}\dot{\theta}^2\sin\theta\cos\theta + r^2\dot{\theta}^4\cos^2\theta $$
  $$ + r^2\ddot{\theta}^2\cos^2\theta - 2r^2\ddot{\theta}\dot{\theta}^2\sin\theta\cos\theta + r^2\dot{\theta}^4\sin^2\theta $$
  The cross terms cancel out completely:
  $$ a_{B/0}^2 = r^2\ddot{\theta}^2(\sin^2\theta + \cos^2\theta) + r^2\dot{\theta}^4(\cos^2\theta + \sin^2\theta) = r^2\ddot{\theta}^2 + r^2\dot{\theta}^4 $$
  Taking the square root:
  $$ a_{B/0} = \sqrt{r^2\ddot{\theta}^2 + r^2\dot{\theta}^4} $$
  *(Compare with the official solution key (Problems.pdf, Solution keys section).)*

### Phase 4: Physical Interpretation & Limiting Cases
* **Plane Motion Decoupling:** Notice that the acceleration magnitude $a_{B/0}$ is completely independent of the tow plane's cruise velocity $v_A$ because $\mathbf{a}_A = \mathbf{0}$ (uniform rectilinear translation). The acceleration felt by the glider is purely relative circular motion around $A$!
* **Limiting Case $\ddot{\theta} = 0$:** If the cable turns at a constant angular rate $\dot{\theta} = \Omega$, the acceleration reduces to pure centripetal acceleration: $a_{B/0} = \sqrt{r^2\Omega^4} = r\Omega^2$.
* **Dimensional check:** $[r\ddot{\theta}] = [r\dot{\theta}^2] = \text{m}\cdot\text{s}^{-2}$ and $[v_A + r\dot{\theta}\sin\theta] = \text{m/s}$, so $a_{B/0} = \sqrt{r^2\ddot{\theta}^2 + r^2\dot{\theta}^4}$ is in m/s$^2$ and $v_{B/0}$ in m/s.
* **Limit $\dot{\theta} = 0$:** $\mathbf{v}_{B/0} = v_A\,\mathbf{i}_0$ and $\mathbf{a}_{B/0} = \mathbf{0}$, the glider moves rigidly with the tow plane.
* **Symbolic check (sympy):** differentiating $\mathbf{r}_B$ twice for an arbitrary function $\theta(t)$ gives $\|\mathbf{v}_{B/0}\|^2 = (v_A + r\dot{\theta}\sin\theta)^2 + (r\dot{\theta}\cos\theta)^2$ and $\|\mathbf{a}_{B/0}\|^2 = r^2\ddot{\theta}^2 + r^2\dot{\theta}^4$ with zero residual.

---

## 📌 Problem 06: Particle on Sinusoidal Curve

### Phase 1: Physical Statement, Hypotheses, CDOFs & Parameters
* **Physical System:** A particle travels along a sinusoidal path $y(x) = \sin x$ with constant horizontal speed $\dot{x} = 1$.
* **Hypotheses:** $\dot{x}(t) \equiv 1\text{ m/s} \implies x(t) = t + x_0$ (taking $x_0 = 0 \implies x(t) = t$). $\ddot{x} = 0$.
* **Degrees of Freedom:** $\text{CDOF} = 1$.

### Phase 2: Geometric & Intrinsic Formulations
* **Parametric Curve:** $\mathbf{r}(x) = x\mathbf{i}_0 + \sin x\,\mathbf{j}_0$.
* **Derivative Vector:** $\frac{d\mathbf{r}}{dx} = \mathbf{i}_0 + \cos x\,\mathbf{j}_0$.
* **Differential Arc Length:**
  $$ ds = \left\| \frac{d\mathbf{r}}{dx} \right\|dx = \sqrt{1 + \cos^2 x}\,dx $$
* **Change of basis (intrinsic basis).** Let $\alpha(x) = \arctan(\cos x)$ be the slope angle of the tangent, so that $\mathbf{e}_t = (\cos\alpha, \sin\alpha) = (1, \cos x)/\sqrt{1 + \cos^2x}$. The in-plane normal used in this solution is $\mathbf{e}_n = \mathbf{k}_0 \times \mathbf{e}_t = (-\sin\alpha, \cos\alpha) = (-\cos x, 1)/\sqrt{1 + \cos^2x}$, the normal obtained by turning $\mathbf{e}_t$ by $+90^\circ$ (to its left). The columns are the components of $\mathbf{e}_t$, $\mathbf{e}_n$ in $\{\mathbf{i}_0, \mathbf{j}_0\}$:
$$ [{}_0 R_1] = \frac{1}{\sqrt{1 + \cos^2x}}\begin{pmatrix} 1 & -\cos x \\ \cos x & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = \frac{1 + \cos^2x}{1 + \cos^2x} = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
* Because $\mathbf{e}_n$ is always the left normal, the sign of $a_n$ tells on which side the centre of curvature lies: $a_n < 0$ (as for $0 < x < \pi$, where $\sin x > 0$) places it to the right of the direction of motion, below the arch; $a_n > 0$ for $\pi < x < 2\pi$ places it above the curve. The matrix properties were verified symbolically with sympy.

### Phase 3: Mathematical Deduction Step-by-Step with Continuous Justification

#### (a) Intrinsic Unitary Vector Basis $\{\mathbf{e}_t, \mathbf{e}_n\}$
* **Unit Tangent Vector $\mathbf{e}_t$:**
  $$ \mathbf{e}_t = \frac{d\mathbf{r}/dx}{\|d\mathbf{r}/dx\|} = \frac{\mathbf{i}_0 + \cos x\,\mathbf{j}_0}{\sqrt{1 + \cos^2 x}} $$
* **Unit Principal Normal Vector $\mathbf{e}_n$:**
  In a 2D plane, the normal vector $\mathbf{e}_n$ is perpendicular to $\mathbf{e}_t$ oriented toward the center of curvature.
  Differentiating $\mathbf{e}_t$ with respect to arc length $s$:
  $$ \frac{d\mathbf{e}_t}{ds} = \frac{d\mathbf{e}_t}{dx}\frac{dx}{ds} = \frac{1}{\sqrt{1 + \cos^2 x}}\frac{d}{dx}\left[ (1 + \cos^2 x)^{-1/2}(\mathbf{i}_0 + \cos x\,\mathbf{j}_0) \right] $$
  Applying the quotient/product rule:
  $$ \frac{d}{dx}\left[\frac{1}{\sqrt{1 + \cos^2 x}}\right] = -\frac{1}{2}(1 + \cos^2 x)^{-3/2}(2\cos x(-\sin x)) = \frac{\sin x\cos x}{(1 + \cos^2 x)^{3/2}} $$
  $$ \frac{d\mathbf{e}_t}{dx} = \frac{\sin x\cos x}{(1 + \cos^2 x)^{3/2}}(\mathbf{i}_0 + \cos x\,\mathbf{j}_0) + \frac{1}{\sqrt{1 + \cos^2 x}}(-\sin x\,\mathbf{j}_0) $$
  Putting over the common denominator $(1 + \cos^2 x)^{3/2}$:
  $$ = \frac{\sin x\cos x\,\mathbf{i}_0 + \sin x\cos^2 x\,\mathbf{j}_0 - \sin x(1 + \cos^2 x)\,\mathbf{j}_0}{(1 + \cos^2 x)^{3/2}} = \frac{\sin x\cos x\,\mathbf{i}_0 - \sin x\,\mathbf{j}_0}{(1 + \cos^2 x)^{3/2}} = -\frac{\sin x}{(1 + \cos^2 x)^{3/2}}(-\cos x\,\mathbf{i}_0 + \mathbf{j}_0) $$
  Normalizing to unit length:
  $$ \mathbf{e}_n = \frac{-\cos x\,\mathbf{i}_0 + \mathbf{j}_0}{\sqrt{1 + \cos^2 x}} \quad (\text{sign adjusted to point to the concave side}) $$

#### (b) Arc Length Parameter $s(x)$
* **Pedagogical Justification:** The relation between $x$ and arc length $s$ is given by integrating the metric differential:
  $$ s(x) = \int_0^x \sqrt{1 + \cos^2 u}\,du $$
  This integral is an incomplete elliptic integral of the second kind, which cannot be expressed in elementary functions and is properly expressed as a quadrature.

#### (c) Tangent and Normal Acceleration Components
* **Velocity Vector:** Since $\dot{x} = 1$:
  $$ \mathbf{v} = \dot{x}\mathbf{i}_0 + \dot{y}\mathbf{j}_0 = 1\mathbf{i}_0 + \cos x\,\mathbf{j}_0 $$
  The speed is:
  $$ v(x) = \|\mathbf{v}\| = \sqrt{1 + \cos^2 x} $$
* **Acceleration Vector:** Differentiating velocity with $\dot{x} = 1$:
  $$ \mathbf{a} = \frac{d\mathbf{v}}{dt} = \frac{d}{dt}(1\mathbf{i}_0 + \cos x\,\mathbf{j}_0) = -\sin x\,\dot{x}\,\mathbf{j}_0 = -\sin x\,\mathbf{j}_0 $$
* **Tangential Acceleration Component $a_t$:**
  $$ a_t = \mathbf{a} \cdot \mathbf{e}_t = (-\sin x\,\mathbf{j}_0) \cdot \left( \frac{\mathbf{i}_0 + \cos x\,\mathbf{j}_0}{\sqrt{1 + \cos^2 x}} \right) = -\frac{\sin x\cos x}{\sqrt{1 + \cos^2 x}} $$
* **Normal Acceleration Component $a_n$:**
  $$ a_n = \mathbf{a} \cdot \mathbf{e}_n = (-\sin x\,\mathbf{j}_0) \cdot \left( \frac{-\cos x\,\mathbf{i}_0 + \mathbf{j}_0}{\sqrt{1 + \cos^2 x}} \right) = \frac{-\sin x}{\sqrt{1 + \cos^2 x}} $$
  Its magnitude is:
  $$ |a_n| = \frac{|\sin x|}{\sqrt{1 + \cos^2 x}} $$

#### (d) Radius of Curvature $\rho(x)$
* **Pedagogical Justification:** Using $a_n = \frac{v^2}{\rho}$:
  $$ \rho(x) = \frac{v^2}{|a_n|} = \frac{1 + \cos^2 x}{\frac{|\sin x|}{\sqrt{1 + \cos^2 x}}} = \frac{(1 + \cos^2 x)^{3/2}}{|\sin x|} $$
  *(Notice this matches the standard Cartesian curvature formula $\rho = \frac{(1 + y'^2)^{3/2}}{|y''|}$ with $y' = \cos x, y'' = -\sin x$!).*

### Phase 4: Physical Interpretation, Limiting Cases and Dimensional Check
* **Dimensional check:** the data are in SI units with the length scale $1$ m inside the sine ($y = \sin x$ means $y = (1\ \text{m})\sin(x/1\ \text{m})$) and $\dot{x} = 1\ \text{m/s}$. Then $[v] = \text{m/s}$, $[a_t] = [a_n] = \text{m/s}^2$ and $[\rho] = [v^2/|a_n|] = \text{m}$, and $[s] = [\int\sqrt{1 + \cos^2u}\,du] = \text{m}$.
* **Special points:** at the inflection points $x = k\pi$, $\sin x = 0$, so $a_n = 0$ and $\rho \to \infty$ (locally straight). At the crests $x = \pi/2$: $v = 1\ \text{m/s}$, $a_t = 0$, $a_n = -1\ \text{m/s}^2$ and $\rho = v^2/|a_n| = 1$ m, equal to $1/|y''| = 1$ m. At $x = \pi/4$: $\rho = (1 + \cos^2x)^{3/2}/|\sin x| = 3\sqrt{3}/2 = 2.598$ m.
* **Arc length:** $s(\pi) = \int_0^\pi\sqrt{1 + \cos^2u}\,du = 3.8202$ m, greater than the horizontal distance $\pi$ m, as it must be.
* **Symbolic check (sympy):** $a_t^2 + a_n^2 = \sin^2x = \|\mathbf{a}\|^2$ and $v^2/|a_n| = (1 + \cos^2x)^{3/2}/|\sin x|$ hold with zero residual.

---

## 📌 Problem 07: Skater Pulled by Vehicle on a Circumference

### Phase 1: Physical Statement, Hypotheses, CDOFs & Parameters
* **Physical System:** A vehicle $A$ moves counterclockwise at constant speed $\omega$ along a circle of radius $a$. Skater $B$ on a frictionless horizontal plane is towed by vehicle $A$ via a massless bar of length $l = a$.
* **Initial Conditions:** Vehicle $A$ is at $(a, 0)$, skater $B$ is at rest at $(2a, 0)$, meaning at $t = 0$, $\psi(0) = 0$. Because the skater is at rest in the inertial frame, $\dot{\psi}(0) = -2\omega$ (derived in part (c)).
* **Parameters & Units:** Radius and bar length $a\text{ [m]}$, angular speed $\omega\text{ [rad/s]}$, skater mass $m\text{ [kg]}$.

### Phase 2: Reference Frames, Bases & Kinematics
* **Inertial Frame:** $\mathcal{S}_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$.
* **Rotating Frame Attached to $OA$:** $\mathcal{S}_1 = \{O; \mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$, with $\mathbf{i}_1$ pointing from $O$ to vehicle $A$.
  $$ \boldsymbol{\omega}_{1/0} = \omega\mathbf{k}_0 = \omega\mathbf{k}_1 $$
  $$ \mathbf{r}_A = a\mathbf{i}_1 $$
* **Bar Orientation:** The bar $AB$ is directed at angle $\psi$ relative to $\mathbf{i}_1$:
  $$ \mathbf{r}_{B/A} = a\cos\psi\,\mathbf{i}_1 + a\sin\psi\,\mathbf{j}_1 $$
* **Position of Skater $B$ in Rotating Frame:**
  $$ \mathbf{r}_B = \mathbf{r}_A + \mathbf{r}_{B/A} = a(1 + \cos\psi)\mathbf{i}_1 + a\sin\psi\,\mathbf{j}_1 $$
* **Change of basis $\mathcal{B}_0 \to \mathcal{B}_1$.** The vehicle starts at $(a, 0)$ and turns counterclockwise at rate $\omega$, so $\mathbf{i}_1 = \cos\omega t\,\mathbf{i}_0 + \sin\omega t\,\mathbf{j}_0$ and the columns of the matrix below are the components of $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ in $\mathcal{B}_0$:
$$ [{}_0 R_1] = \begin{pmatrix} \cos\omega t & -\sin\omega t & 0 \ \sin\omega t & \cos\omega t & 0 \ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = \cos^2\omega t + \sin^2\omega t = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
* **Bar basis $\mathcal{B}_1 \to \mathcal{B}_{\text{bar}}$.** The pair $\mathbf{u}_{AB} = \cos\psi\,\mathbf{i}_1 + \sin\psi\,\mathbf{j}_1$, $\mathbf{u}_\perp = -\sin\psi\,\mathbf{i}_1 + \cos\psi\,\mathbf{j}_1$ used in parts (c) and (d) is obtained with
$$ [{}_1 R_{\text{bar}}] = \begin{pmatrix} \cos\psi & -\sin\psi & 0 \ \sin\psi & \cos\psi & 0 \ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_1 R_{\text{bar}}] = 1, \qquad [{}_1 R_{\text{bar}}][{}_1 R_{\text{bar}}]^T = I $$
* The composition $[{}_0 R_{\text{bar}}] = [{}_0 R_1][{}_1 R_{\text{bar}}]$ is the planar rotation by $\omega t + \psi$ (the bar direction measured from the inertial $x$ axis). The determinants and the products $R R^T$ were verified symbolically with sympy.

### Phase 3: Mathematical Deduction Step-by-Step with Continuous Justification

#### (a) Relative Acceleration in $\mathcal{S}_1$
* **Pedagogical Justification:** The relative velocity and acceleration are the time derivatives of $\mathbf{r}_B$ observed within frame $\mathcal{S}_1$, treating unit vectors $\mathbf{i}_1, \mathbf{j}_1$ as constant.
* **Relative Velocity:**
  $$ \mathbf{v}_{\text{rel}} = \frac{d\mathbf{r}_B}{dt}\Big|_{\mathcal{S}_1} = -a\dot{\psi}\sin\psi\,\mathbf{i}_1 + a\dot{\psi}\cos\psi\,\mathbf{j}_1 $$
* **Relative Acceleration (Explicit Product Rule):**
  $$ \mathbf{a}_{\text{rel}} = \frac{d\mathbf{v}_{\text{rel}}}{dt}\Big|_{\mathcal{S}_1} = \frac{d}{dt}(-a\dot{\psi}\sin\psi)\mathbf{i}_1 + \frac{d}{dt}(a\dot{\psi}\cos\psi)\mathbf{j}_1 $$
  $$ = -a(\ddot{\psi}\sin\psi + \dot{\psi}^2\cos\psi)\mathbf{i}_1 + a(\ddot{\psi}\cos\psi - \dot{\psi}^2\sin\psi)\mathbf{j}_1 $$

#### (b) Coriolis and Centripetal Accelerations
* **Pedagogical Justification:** By Coriolis' theorem of relative kinematics (Notes Sec. 4.9):
  $$ \mathbf{a}_{\text{cor}} = 2\boldsymbol{\omega}_{1/0} \times \mathbf{v}_{\text{rel}} $$
  $$ \mathbf{a}_{\text{cf}} = \boldsymbol{\omega}_{1/0} \times (\boldsymbol{\omega}_{1/0} \times \mathbf{r}_B) = -\omega^2\mathbf{r}_{B\perp} $$
* **Coriolis Calculation:**
  $$ \mathbf{a}_{\text{cor}} = 2(\omega\mathbf{k}_1) \times (-a\dot{\psi}\sin\psi\,\mathbf{i}_1 + a\dot{\psi}\cos\psi\,\mathbf{j}_1) $$
  Using $\mathbf{k}_1 \times \mathbf{i}_1 = \mathbf{j}_1$ and $\mathbf{k}_1 \times \mathbf{j}_1 = -\mathbf{i}_1$:
  $$ \mathbf{a}_{\text{cor}} = 2\omega\left( -a\dot{\psi}\sin\psi\,\mathbf{j}_1 - a\dot{\psi}\cos\psi\,\mathbf{i}_1 \right) = -2a\omega\dot{\psi}(\cos\psi\,\mathbf{i}_1 + \sin\psi\,\mathbf{j}_1) $$
  *(Compare with the official solution key (Problems.pdf, Solution keys section).)*
* **Centripetal / Centrifugal Acceleration Term:**
  Since $\mathbf{r}_B$ lies entirely in the $x_1 y_1$ plane, $\boldsymbol{\omega} \times (\boldsymbol{\omega} \times \mathbf{r}_B) = -\omega^2\mathbf{r}_B$:
  $$ \mathbf{a}_{\text{cf}} = -\omega^2\mathbf{r}_B = -a\omega^2[(1 + \cos\psi)\mathbf{i}_1 + \sin\psi\,\mathbf{j}_1] $$
  *(Compare with the official solution key (Problems.pdf, Solution keys section).)*

#### (c) Reduction of Equation of Motion to Integrals (Quadrature)
* **Pedagogical Justification:** The only force acting on skater $B$ in the horizontal plane is the tension $\mathbf{T}$ from the bar, which acts along the bar: $\mathbf{u}_{AB} = \cos\psi\,\mathbf{i}_1 + \sin\psi\,\mathbf{j}_1$. Therefore, the total acceleration of $B$ in the direction perpendicular to the bar $\mathbf{u}_\perp = -\sin\psi\,\mathbf{i}_1 + \cos\psi\,\mathbf{j}_1$ must vanish: $\mathbf{a}_B \cdot \mathbf{u}_\perp = 0$.
* **Projection of Acceleration:**
  $$ \mathbf{a}_{\text{total}} = \mathbf{a}_{\text{rel}} + \mathbf{a}_{\text{cor}} + \mathbf{a}_{\text{cf}} $$
  Taking the dot product with $\mathbf{u}_\perp$:
  - $\mathbf{a}_{\text{rel}} \cdot \mathbf{u}_\perp = a\ddot{\psi}(\sin^2\psi + \cos^2\psi) = a\ddot{\psi}$.
  - $\mathbf{a}_{\text{cor}} \cdot \mathbf{u}_\perp = -2a\omega\dot{\psi}(\cos\psi(-\sin\psi) + \sin\psi\cos\psi) = 0$.
  - $\mathbf{a}_{\text{cf}} \cdot \mathbf{u}_\perp = -a\omega^2[ (1+\cos\psi)(-\sin\psi) + \sin\psi\cos\psi ] = -a\omega^2(-\sin\psi - \sin\psi\cos\psi + \sin\psi\cos\psi) = a\omega^2\sin\psi$.
  Therefore:
  $$ a\ddot{\psi} + a\omega^2\sin\psi = 0 \implies \ddot{\psi} + \omega^2\sin\psi = 0 $$
  Multiplying by $2\dot{\psi}$ and using the chain rule $\frac{d}{dt}(\dot{\psi}^2) = 2\dot{\psi}\ddot{\psi}$ and $\frac{d}{dt}(\cos\psi) = -\sin\psi\,\dot{\psi}$:
  $$ 2\dot{\psi}\ddot{\psi} = -2\omega^2\sin\psi\,\dot{\psi} \implies \frac{d}{dt}(\dot{\psi}^2) = -2\omega^2\sin\psi\,\dot{\psi} = 2\omega^2\frac{d}{dt}(\cos\psi) $$
  **Initial conditions.** The skater starts at rest in the inertial frame, $\mathbf{v}_B(0) = \mathbf{0}$, at $\mathbf{r}_B(0) = 2a\,\mathbf{i}_1$ (so $\psi(0) = 0$). Since $\mathbf{v}_B = \boldsymbol{\omega}_{1/0}\times\mathbf{r}_B + \mathbf{v}_{\text{rel}}$:
  $$ \mathbf{v}_{\text{rel}}(0) = -\omega\mathbf{k}_1 \times 2a\,\mathbf{i}_1 = -2a\omega\,\mathbf{j}_1, \qquad \mathbf{v}_{\text{rel}}(0) = a\dot{\psi}(0)\,\mathbf{j}_1 \implies \dot{\psi}(0) = -2\omega $$
  Integrating with Barrow's rule between $t = 0$ ($\psi = 0$, $\dot{\psi} = -2\omega$) and a generic instant, with $u$ a dummy variable ($du = \dot{\psi}\,dt$ along the motion):
  $$ \dot{\psi}^2 - (-2\omega)^2 = 2\omega^2\int_0^\psi (-\sin u)\,du = 2\omega^2\left[\cos u\right]_0^\psi = 2\omega^2(\cos\psi - 1) $$
  $$ \dot{\psi}^2 = 2\omega^2(1 + \cos\psi) = 4\omega^2\cos^2\!\left(\frac{\psi}{2}\right) \quad \text{using } 1 + \cos\psi = 2\cos^2(\psi/2) $$
  Taking the square root, $\dot{\psi} = \pm 2\omega\cos(\psi/2)$. For $-\pi < \psi < \pi$ the factor $\cos(\psi/2)$ is positive, so the sign cannot change, and $\dot{\psi}(0) = -2\omega$ selects the minus sign ($\psi$ decreases from zero):
  $$ \dot{\psi} = -2\omega\cos\left(\frac{\psi}{2}\right) \quad \text{for } -\pi < \psi \le 0 $$
  This agrees with the official key (Problems.pdf, PDF page 72).
  Separating variables and integrating from $(t, \psi) = (0, 0)$, with the substitution $w = u/2$, $du = 2\,dw$:
  $$ \int_0^\psi \frac{du}{2\cos(u/2)} = -\omega\int_0^t dt' \implies \int_0^{\psi/2}\frac{dw}{\cos w} = \ln\left|\sec\frac{\psi}{2} + \tan\frac{\psi}{2}\right| = -\omega t $$

#### (d) Tension on the Bar
* **Pedagogical Justification:** The tension is obtained from the radial force balance along the bar:
  $$ T = -m(\mathbf{a}_{\text{total}} \cdot \mathbf{u}_{AB}) $$
  Evaluating the terms along $\mathbf{u}_{AB} = \cos\psi\,\mathbf{i}_1 + \sin\psi\,\mathbf{j}_1$:
  - $\mathbf{a}_{\text{rel}}\cdot\mathbf{u}_{AB} = -a(\ddot{\psi}\sin\psi + \dot{\psi}^2\cos\psi)\cos\psi + a(\ddot{\psi}\cos\psi - \dot{\psi}^2\sin\psi)\sin\psi = -a\dot{\psi}^2$.
  - $\mathbf{a}_{\text{cor}}\cdot\mathbf{u}_{AB} = -2a\omega\dot{\psi}(\cos^2\psi + \sin^2\psi) = -2a\omega\dot{\psi}$.
  - $\mathbf{a}_{\text{cf}}\cdot\mathbf{u}_{AB} = -a\omega^2[(1+\cos\psi)\cos\psi + \sin^2\psi] = -a\omega^2(1 + \cos\psi)$.
  $$ T = ma\left[\dot{\psi}^2 + 2\omega\dot{\psi} + \omega^2(1+\cos\psi)\right] $$
  With $c = \cos(\psi/2)$: $\dot{\psi}^2 = 4\omega^2c^2$, $\dot{\psi} = -2\omega c$, $1 + \cos\psi = 2c^2$, hence $T = ma\omega^2(4c^2 - 4c + 2c^2)$:
  $$ T = 2ma\omega^2\cos\left(\frac{\psi}{2}\right)\left( 3\cos\left(\frac{\psi}{2}\right) - 2 \right) $$
  *(Compare with the official solution key (Problems.pdf, Solution keys section).)*

#### (e) Loose String Condition
* **Pedagogical Justification:** A flexible string cannot support compression ($T \ge 0$). The string becomes loose when the tension drops to zero: $T = 0$.
  $$ 3\cos\left(\frac{\psi}{2}\right) - 2 = 0 \implies \cos\left(\frac{\psi}{2}\right) = \frac{2}{3} $$
  $$ \frac{\psi}{2} = -\arccos\left(\frac{2}{3}\right) \implies \psi = -2\arccos\left(\frac{2}{3}\right) \approx -96.38^\circ $$
  *(Compare with the official solution key (Problems.pdf, Solution keys section).)*

### Phase 4: Physical Interpretation, Limiting Cases and Dimensional Check
* **Dimensional check:**
  - $[\ddot{\psi}] = [\omega^2\sin\psi] = \text{s}^{-2}$ and $[\dot{\psi}^2] = [2\omega^2(1 + \cos\psi)] = \text{s}^{-2}$ (the angle is dimensionless).
  - $[T] = [m\,a\,\omega^2] = \text{kg}\cdot\text{m}\cdot\text{s}^{-2} = \text{N}$.
* **Limit $\omega \to 0$:** the vehicle is at rest, the skater is at rest, and $T \to 0$, $\dot{\psi} \to 0$, as expected.
* **Independent check of $T$ at $t = 0$ ($\psi = 0$).** The closed form gives $T(0) = 2ma\omega^2\cdot 1\cdot(3 - 2) = 2ma\omega^2$. For a rigid bar of length $l = a$, the relative velocity $\mathbf{v}_B - \mathbf{v}_A$ is perpendicular to the bar, hence $(\mathbf{a}_B - \mathbf{a}_A)\cdot\mathbf{u}_{AB} = -\|\mathbf{v}_B - \mathbf{v}_A\|^2/a$. At $t = 0$: $\mathbf{v}_B = \mathbf{0}$, $\|\mathbf{v}_A\| = a\omega$, $\mathbf{a}_A = -a\omega^2\mathbf{i}_0$ and $\mathbf{u}_{AB} = \mathbf{i}_0$, so $\mathbf{a}_B\cdot\mathbf{u}_{AB} = -a\omega^2 - a\omega^2 = -2a\omega^2$ and $T = 2ma\omega^2$ (Consistent).
* **Symbolic check (sympy).** Differentiating twice, in the inertial frame, the position $\mathbf{r}_B = [{}_0 R_1]\,a\,(1 + \cos\psi,\ \sin\psi,\ 0)^T$ and projecting on $\mathbf{u}_{AB}$ and $\mathbf{u}_\perp$ gives $\mathbf{a}_B\cdot\mathbf{u}_\perp = a(\ddot{\psi} + \omega^2\sin\psi)$ and $T = ma\left[\dot{\psi}^2 + 2\omega\dot{\psi} + \omega^2(1 + \cos\psi)\right]$, identical to parts (c) and (d); substituting $\dot{\psi} = -2\omega\cos(\psi/2)$ reproduces $T = 2ma\omega^2\cos(\psi/2)\left(3\cos(\psi/2) - 2\right)$ with zero residual.
* **When the string goes loose (numerical).** The closed form $\omega t = -\ln\left|\sec(\psi/2) + \tan(\psi/2)\right|$ evaluated at $\cos(\psi/2) = 2/3$ gives $\omega t_{\text{loose}} = \ln\dfrac{2}{3 - \sqrt{5}} = \ln\dfrac{3 + \sqrt{5}}{2} = 0.96242$. An RK4 integration (step $10^{-5}$, $\omega = 1$) of $\ddot{\psi} = -\omega^2\sin\psi$ with $\psi(0) = 0$, $\dot{\psi}(0) = -2\omega$ reaches $\cos(\psi/2) = 2/3$ at $\omega t = 0.96242$ with $\psi = -96.379^\circ$, in agreement with $-2\arccos(2/3) = -96.379^\circ$; there $\dot{\psi}^2 = 1.777787\,\omega^2$ against $2\omega^2(1 + \cos\psi) = 1.777787\,\omega^2$.

---

## 📌 Problem 08: Kinematics, Two Trains on Tracks

### Phase 1: Physical Statement, Hypotheses, CDOFs & Parameters
* **Physical System:** Two trains $A$ and $B$ move on separate tracks with distance of closest separation $a$.
  - Case 1: Two parallel straight tracks with constant speeds $v_A$ and $v_B$.
  - Case 2: Train $A$ on a straight track, Train $B$ on a circular track of radius $R$.
* **Parameters & Units:** Separation $a\text{ [m]}$, radius $R\text{ [m]}$, speeds $v_A, v_B\text{ [m/s]}$.

### Phase 2: Reference Frames & Vector Equations
* **Inertial Cartesian Frame:** $\mathcal{S}_0 = \{O; \mathbf{i}_0, \mathbf{j}_0\}$.

### Phase 3: Mathematical Deduction Step-by-Step with Continuous Justification

#### Case 1: Parallel Tracks
* Train $A$ on line $y = 0$: $\mathbf{r}_A(t) = v_A t\,\mathbf{i}_0$.
* Train $B$ on line $y = a$: $\mathbf{r}_B(t) = (x_{B0} + v_B t)\mathbf{i}_0 + a\mathbf{j}_0$.
* **Relative Velocity:**
  $$ \mathbf{v}_{B/A} = \mathbf{v}_B - \mathbf{v}_A = (v_B - v_A)\mathbf{i}_0 $$
  $$ \mathbf{v}_{A/B} = -\mathbf{v}_{B/A} = (v_A - v_B)\mathbf{i}_0 $$

#### Case 2: Train $B$ on a Circular Track of Radius $R$
* Straight track of $A$ along the $x$-axis: $\mathbf{r}_A = v_A t\,\mathbf{i}_0$.
* Circular track center at $(0, R + a)$ so that the closest distance to $A$'s track is $(R+a) - R = a$.
* Position of train $B$ traveling at angular speed $\omega_B = \frac{v_B}{R}$ with angle $\theta_B(t) = \omega_B t$:
  $$ \mathbf{r}_B(t) = R\sin(\omega_B t)\mathbf{i}_0 + [R + a - R\cos(\omega_B t)]\mathbf{j}_0 $$
* Velocity of train $B$:
  $$ \mathbf{v}_B = \frac{d\mathbf{r}_B}{dt} = R\omega_B\cos(\omega_B t)\mathbf{i}_0 + R\omega_B\sin(\omega_B t)\mathbf{j}_0 = v_B\cos\left(\frac{v_B t}{R}\right)\mathbf{i}_0 + v_B\sin\left(\frac{v_B t}{R}\right)\mathbf{j}_0 $$
* **Relative Velocity $\mathbf{v}_{B/A}$:**
  $$ \mathbf{v}_{B/A} = \mathbf{v}_B - \mathbf{v}_A = \left[ v_B\cos\left(\frac{v_B t}{R}\right) - v_A \right]\mathbf{i}_0 + v_B\sin\left(\frac{v_B t}{R}\right)\mathbf{j}_0 $$
* **Magnitude of Relative Velocity:**
  $$ v_{\text{rel}} = \sqrt{\left[ v_B\cos\left(\frac{v_B t}{R}\right) - v_A \right]^2 + v_B^2\sin^2\left(\frac{v_B t}{R}\right)} = \sqrt{v_B^2 + v_A^2 - 2v_A v_B\cos\left(\frac{v_B t}{R}\right)} $$

### Phase 4: Physical Interpretation, Limiting Cases and Dimensional Check
* **Dimensional check:** $[\mathbf{v}_{B/A}] = \text{m/s}$; in Case 2 the argument of the trigonometric functions is $\dfrac{v_B t}{R} = \dfrac{(\text{m/s})\,\text{s}}{\text{m}}$, which is dimensionless (rad), and $[v_B^2 + v_A^2 - 2v_Av_B\cos(\cdot)] = \text{m}^2/\text{s}^2$, so $v_{\text{rel}}$ is in m/s.
* **Role of the separation $a$:** it does not appear in any relative velocity, because $\mathbf{v}_{B/A}$ is the time derivative of $\mathbf{r}_B - \mathbf{r}_A$ and $a$ only enters the constant offset of that vector.
* **Limiting cases of Case 2 (sympy):**
  - $t = 0$: $v_{\text{rel}} = \sqrt{v_A^2 + v_B^2 - 2v_Av_B} = |v_B - v_A|$, because both velocities are parallel to $\mathbf{i}_0$ at that instant.
  - $R \to \infty$ (the circular track straightens): $\cos(v_Bt/R) \to 1$ and $v_{\text{rel}} \to |v_B - v_A|$, which is the Case 1 result.
  - $v_A = v_B = v$: $v_{\text{rel}} = v\sqrt{2 - 2\cos(vt/R)} = 2v\left|\sin\dfrac{vt}{2R}\right|$, which starts at $0$ and never exceeds $2v$.
  - $v_A = 0$: $v_{\text{rel}} = v_B$ for all $t$ (relative to a stationary train, only the speed of $B$ matters).
* **Symbolic check:** $\|\mathbf{v}_B - \mathbf{v}_A\|^2$ computed from the components equals $v_B^2 + v_A^2 - 2v_Av_B\cos(v_Bt/R)$ with zero residual. Both cases are written in the single inertial basis $\mathcal{B}_0$, so no change-of-basis matrix is needed.

---

## 📌 Problem 09: 2001: A Space Odyssey (Artificial Gravity)

### Phase 1: Physical Statement, Hypotheses, CDOFs & Parameters
* **Physical System:** A rotating cylindrical spacecraft hull of radius $R$ generates artificial gravity via centrifugal normal acceleration.
* **Hypotheses:** Spacecraft rotates at constant rate $\omega$ about its symmetry axis in deep space (no external gravitational field).
* **Parameters & Units:** Radius $R = 10\text{ m}$, target gravity $g = 9.81\text{ m/s}^2$, relative running speed $u\text{ [m/s]}$.

### Phase 2: Kinematics of Circular Motion
* Intrinsic acceleration of a point on the rim rotating at speed $v_{\text{rim}} = \omega R$:
  $$ a_n = \frac{v_{\text{rim}}^2}{R} = \omega^2 R $$
* **Hull-fixed rotating basis.** Take the inertial basis $\mathcal{B}_0 = \{\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ with $\mathbf{k}_0$ along the axis of the cylinder, and the basis $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}_0\}$ attached to the hull, rotating at constant rate $\omega$ about $\mathbf{k}_0$ (the angle is $\theta = \omega t$ for a point fixed to the hull). The columns are the components of $\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}_0$ in $\mathcal{B}_0$:
$$ [{}_0 R_1] = \begin{pmatrix} \cos\omega t & -\sin\omega t & 0 \ \sin\omega t & \cos\omega t & 0 \ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = \cos^2\omega t + \sin^2\omega t = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
* By Poisson's formula with $\boldsymbol{\omega} = \omega\mathbf{k}_0$: $\dot{\mathbf{e}}_r = \omega\mathbf{e}_\theta$ and $\dot{\mathbf{e}}_\theta = -\omega\mathbf{e}_r$. A point of the rim is $\mathbf{r} = R\,\mathbf{e}_r$, hence $\mathbf{v} = \omega R\,\mathbf{e}_\theta$ and $\mathbf{a} = -\omega^2 R\,\mathbf{e}_r$, which is the intrinsic acceleration $a_n = \omega^2R$ above, directed towards the axis. An astronaut running at speed $u$ relative to the floor along $\pm\mathbf{e}_\theta$ has absolute velocity $(\omega R \pm u)\,\mathbf{e}_\theta$. The determinant and the product $R R^T$ were verified symbolically with sympy.

### Phase 3: Mathematical Deduction Step-by-Step with Continuous Justification

#### (a) Angular Velocity for Target Artificial Gravity $g$
* **Pedagogical Justification:** The apparent weight felt by an astronaut standing still on the inner hull is the normal reaction provided by the floor: $N = m a_n = m \omega^2 R$. For this reaction to match standard Earth gravity $m g$:
  $$ \omega^2 R = g \implies \omega = \sqrt{\frac{g}{R}} $$
* **Numerical Calculation for $R = 10\text{ m}, g = 9.81\text{ m/s}^2$:**
  $$ \omega = \sqrt{\frac{9.81\text{ m/s}^2}{10\text{ m}}} = \sqrt{0.981}\text{ s}^{-1} \approx 0.99045\text{ rad/s} $$
  In revolutions per minute (RPM):
  $$ N_{\text{rpm}} = \omega \times \frac{60}{2\pi} = 0.99045 \times 9.5493 \approx 9.46\text{ rpm} $$

#### (b) Artificial Gravity Felt by a Running Astronaut
* **Pedagogical Justification:** When the astronaut runs along the circumference at speed $u$ relative to the floor, her absolute speed in the inertial frame is $v_{\text{abs}} = \omega R \pm u$, where $(+)$ corresponds to running in the direction of rotation (prograde/eastward) and $(-)$ corresponds to running against rotation (retrograde/westward).
* **Apparent Gravity:**
  $$ g_{\text{felt}} = a_n = \frac{v_{\text{abs}}^2}{R} = \frac{(\omega R \pm u)^2}{R} = \omega^2 R \left( 1 \pm \frac{u}{\omega R} \right)^2 = g \left( 1 \pm \frac{u}{\omega R} \right)^2 $$
  Expanding:
  $$ g_{\text{felt}} = \frac{\omega^2 R^2 \pm 2\omega R u + u^2}{R} = g \pm 2\omega u + \frac{u^2}{R} $$
  *(The term $2\omega u$ represents the Coriolis acceleration felt by the running astronaut!).*

#### (c) Condition to Feel No Artificial Gravity At All
* **Pedagogical Justification:** For the astronaut to become completely weightless ($g_{\text{felt}} = 0$):
  $$ \frac{(\omega R \pm u)^2}{R} = 0 \implies \omega R \pm u = 0 $$
  This requires choosing the retrograde direction $(-)$ and matching the speed:
  $$ u = \omega R $$
* **Physical Explanation:** Running backwards at the exact hull speed cancels out her inertial circular motion. She becomes stationary relative to the non-rotating inertial space, floating weightlessly while the floor slips beneath her feet!

### Phase 4: Physical Interpretation, Limiting Cases and Dimensional Check
* **Dimensional check:** $[\omega] = \sqrt{[g]/[R]} = \sqrt{(\text{m/s}^2)/\text{m}} = \text{s}^{-1}$; $[\omega^2R] = \text{m/s}^2$; $[2\omega u] = \text{s}^{-1}\cdot\text{m/s} = \text{m/s}^2$; $[u^2/R] = (\text{m}^2/\text{s}^2)/\text{m} = \text{m/s}^2$ (Consistent).
* **Numerical values (Python, $R = 10$ m, $g = 9.81$ m/s$^2$):**
  - $\omega = \sqrt{0.981} = 0.990454\ \text{rad/s} = 9.458\ \text{rpm}$ (quoted above as $\approx 9.46$ rpm) and rim speed $\omega R = 9.9045\ \text{m/s}$.
  - Running at $u = 2$ m/s: prograde $g_{\text{felt}} = 14.17\ \text{m/s}^2$ ($1.44\,g$), retrograde $6.25\ \text{m/s}^2$ ($0.64\,g$). At $u = 5$ m/s: prograde $22.21\ \text{m/s}^2$ ($2.26\,g$), retrograde $2.41\ \text{m/s}^2$ ($0.25\,g$).
  - Retrograde at $u = \omega R = 9.9045$ m/s gives $g_{\text{felt}} = 0$ exactly (part (c)); prograde at the same speed gives $4g = 39.24\ \text{m/s}^2$.
* **Limiting cases:** $u \to 0$ gives $g_{\text{felt}} = g$. For $u \ll \omega R$, $g_{\text{felt}} \approx g \pm 2\omega u$, the Coriolis correction (at $u = 2$ m/s: $9.81 + 3.96 + 0.40 = 14.17\ \text{m/s}^2$, where $0.40 = u^2/R$ is the remaining quadratic term, so the expansion of part (b) is reproduced exactly). For $R \to \infty$ at fixed $g$, $\omega = \sqrt{g/R} \to 0$ (a larger hull needs fewer revolutions per minute).

---

## 📌 Problem 41: Simple Rotations, Satellite Solar Panels (Ginsberg)

### Phase 1: Physical Statement, Hypotheses, CDOFs & Parameters
* **Physical System:** A reconnaissance satellite spins about its body-fixed $z$-axis at constant rate $\omega$. A solar panel rotates about the body-fixed $x$-axis by an arbitrary prescribed angle $\theta(t)$.
* **Goal:** Determine absolute velocity $\mathbf{v}_{B/0}$ and acceleration $\mathbf{a}_{B/0}$ of tip $B$ relative to inertial frame centered at $A$.
* **Geometric Parameters:** Dimensions $W$ (panel width) and $H$ (hub height).

### Phase 2: Successive Reference Frames & Rotation Matrices
* **Inertial Reference Frame:** $\mathcal{S}_0 = \{A; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$.
* **Satellite Body Frame (Precessing):** $\mathcal{S}_1 = \{A; \mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$, obtained by rotating by angle $\phi = \omega t$ about $\mathbf{k}_0$:
  $$ [{}_0 R_1] = \begin{pmatrix} \cos(\omega t) & -\sin(\omega t) & 0 \\ \sin(\omega t) & \cos(\omega t) & 0 \\ 0 & 0 & 1 \end{pmatrix}, \quad \boldsymbol{\omega}_{1/0} = \omega\mathbf{k}_1 $$
* **Panel-Fixed Frame:** $\mathcal{S}_2 = \{C; \mathbf{i}_2, \mathbf{j}_2, \mathbf{k}_2\}$, obtained by rotating $\mathcal{S}_1$ by angle $\theta(t)$ about $\mathbf{i}_1$:
  $$ [{}_1 R_2] = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{pmatrix}, \quad \boldsymbol{\omega}_{2/1} = \dot{\theta}\mathbf{i}_1 $$
* **Total Angular Velocity Vector (Notes Sec. 3.3):**
  $$ \boldsymbol{\omega}_{2/0} = \boldsymbol{\omega}_{1/0} + \boldsymbol{\omega}_{2/1} = \dot{\theta}\mathbf{i}_1 + \omega\mathbf{k}_1 $$
* **Angular Acceleration Vector:**
  $$ \boldsymbol{\alpha}_{2/0} = \frac{d\boldsymbol{\omega}_{2/0}}{dt}\Big|_{\mathcal{S}_0} = \ddot{\theta}\mathbf{i}_1 + \dot{\theta}(\boldsymbol{\omega}_{1/0} \times \mathbf{i}_1) + \dot{\omega}\mathbf{k}_1 + \omega(\boldsymbol{\omega}_{1/0} \times \mathbf{k}_1) $$
  Since $\omega = \text{const}$, $\dot{\omega} = 0$ and $\boldsymbol{\omega}_{1/0} \times \mathbf{k}_1 = \mathbf{0}$.
  $$ \boldsymbol{\alpha}_{2/0} = \ddot{\theta}\mathbf{i}_1 + \dot{\theta}(\omega\mathbf{k}_1 \times \mathbf{i}_1) = \ddot{\theta}\mathbf{i}_1 + \omega\dot{\theta}\mathbf{j}_1 $$
The hinge axis is the body-fixed $x$-axis ($\mathbf{i}_1$); $C$ denotes the point of this axis at the abscissa of $B$, so $\mathbf{r}_{AC} = H\mathbf{i}_1$ is fixed in $\mathcal{S}_1$ and does not rotate with the panel. The axes of $\mathcal{S}_2$ expressed in $\mathcal{S}_1$ are the columns of $[{}_1 R_2]$: $\mathbf{i}_2 = \mathbf{i}_1$, $\mathbf{j}_2 = \cos\theta\,\mathbf{j}_1 + \sin\theta\,\mathbf{k}_1$, $\mathbf{k}_2 = -\sin\theta\,\mathbf{j}_1 + \cos\theta\,\mathbf{k}_1$. Orthonormality check: $\det[{}_1 R_2] = \cos^2\theta + \sin^2\theta = 1$ and $[{}_1 R_2][{}_1 R_2]^T = \mathrm{diag}\!\left(1,\ \begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}\begin{pmatrix}\cos\theta & \sin\theta\\ -\sin\theta & \cos\theta\end{pmatrix}\right) = I$.
**Geometry assumption.** The statement text does not fix the geometry; it is read from the figure in Problems.pdf (PDF page 29): the panel lies along the $x$-axis, $B$ is the panel corner at distance $H$ from $A$ measured along $x$ and at distance $W$ from the $x$-axis, and $\theta$ is measured about $+\mathbf{i}_1$ from the $\mathbf{j}_1$ direction (so $\mathbf{r}_{CB} = W\mathbf{j}_2$). The zero reference of $\theta$ (panel along $+\mathbf{j}_1$ at $\theta = 0$) cannot be read unambiguously from the statement; it is the choice consistent with the official key.
* **Orthonormality of $[{}_0 R_1]$:** $\det[{}_0 R_1] = \cos^2\omega t + \sin^2\omega t = 1$ and $[{}_0 R_1][{}_0 R_1]^T = I$. Since $[{}_1 R_2]$ has the same two properties, the composition $[{}_0 R_2] = [{}_0 R_1][{}_1 R_2]$ is also a proper rotation ($\det = 1$, $R R^T = I$); all three checks were done symbolically with sympy.

### Phase 3: Mathematical Deduction Step-by-Step with Continuous Justification

#### Position of Point $B$ in Basis $\mathcal{B}_1$
Decompose $\mathbf{r}_{AB} = \mathbf{r}_{AC} + \mathbf{r}_{CB}$. The first part is fixed in $\mathcal{S}_1$; the second is fixed in the panel frame $\mathcal{S}_2$ ($\mathbf{r}_{CB} = W\mathbf{j}_2$), and is brought to $\mathcal{S}_1$ with $[{}_1 R_2]$:
$$ \mathbf{r}_{AC} = H\mathbf{i}_1, \qquad \{\mathbf{r}_{CB}\}_1 = [{}_1 R_2]\begin{pmatrix}0\\ W\\ 0\end{pmatrix} = \begin{pmatrix}0\\ W\cos\theta\\ W\sin\theta\end{pmatrix} $$
$$ \mathbf{r}_{AB} = H\mathbf{i}_1 + W\cos\theta\,\mathbf{j}_1 + W\sin\theta\,\mathbf{k}_1 $$
#### Absolute Velocity of Point $B$
Since $A$ is the origin of the inertial frame, $\mathbf{v}_{B/0} = \frac{d\mathbf{r}_{AB}}{dt}\Big|_{\mathcal{S}_0}$. By the Poisson formula, a vector fixed in $\mathcal{S}_1$ obeys $\frac{d}{dt}\Big|_{\mathcal{S}_0} = \boldsymbol{\omega}_{1/0}\times$ and a vector fixed in $\mathcal{S}_2$ obeys $\frac{d}{dt}\Big|_{\mathcal{S}_0} = \boldsymbol{\omega}_{2/0}\times$. The hub offset $H\mathbf{i}_1$ rotates only with the satellite ($\boldsymbol{\omega}_{1/0}$), not with the panel:
$$ \mathbf{v}_{B/0} = \boldsymbol{\omega}_{1/0}\times\mathbf{r}_{AC} + \boldsymbol{\omega}_{2/0}\times\mathbf{r}_{CB} = \omega\mathbf{k}_1\times H\mathbf{i}_1 + (\dot{\theta}\mathbf{i}_1 + \omega\mathbf{k}_1)\times W(\cos\theta\,\mathbf{j}_1 + \sin\theta\,\mathbf{k}_1) $$
Cross products: $\mathbf{k}_1\times\mathbf{i}_1 = \mathbf{j}_1$, $\mathbf{i}_1\times\mathbf{j}_1 = \mathbf{k}_1$, $\mathbf{i}_1\times\mathbf{k}_1 = -\mathbf{j}_1$, $\mathbf{k}_1\times\mathbf{j}_1 = -\mathbf{i}_1$, $\mathbf{k}_1\times\mathbf{k}_1 = \mathbf{0}$. Term by term:
- $\omega\mathbf{k}_1\times H\mathbf{i}_1 = H\omega\,\mathbf{j}_1$
- $\dot{\theta}\mathbf{i}_1\times W\cos\theta\,\mathbf{j}_1 = W\dot{\theta}\cos\theta\,\mathbf{k}_1$
- $\dot{\theta}\mathbf{i}_1\times W\sin\theta\,\mathbf{k}_1 = -W\dot{\theta}\sin\theta\,\mathbf{j}_1$
- $\omega\mathbf{k}_1\times W\cos\theta\,\mathbf{j}_1 = -W\omega\cos\theta\,\mathbf{i}_1$
- $\omega\mathbf{k}_1\times W\sin\theta\,\mathbf{k}_1 = \mathbf{0}$
Adding the five terms:
$$ \mathbf{v}_{B/0} = -W\omega\cos\theta\,\mathbf{i}_1 + (H\omega - W\dot{\theta}\sin\theta)\,\mathbf{j}_1 + W\dot{\theta}\cos\theta\,\mathbf{k}_1 $$
This agrees with the official key (Problems.pdf, PDF page 76).
#### Absolute Acceleration of Point $B$
Differentiate $\mathbf{v}_{B/0} = v_x\mathbf{i}_1 + v_y\mathbf{j}_1 + v_z\mathbf{k}_1$ in $\mathcal{S}_0$: the components are differentiated with the chain rule and product rule, and the Poisson formula gives $\dot{\mathbf{i}}_1 = \omega\mathbf{j}_1$, $\dot{\mathbf{j}}_1 = -\omega\mathbf{i}_1$, $\dot{\mathbf{k}}_1 = \mathbf{0}$:
$$ \mathbf{a}_{B/0} = \dot{v}_x\mathbf{i}_1 + \dot{v}_y\mathbf{j}_1 + \dot{v}_z\mathbf{k}_1 + \omega\mathbf{k}_1\times\mathbf{v}_{B/0} = (\dot{v}_x - \omega v_y)\mathbf{i}_1 + (\dot{v}_y + \omega v_x)\mathbf{j}_1 + \dot{v}_z\mathbf{k}_1 $$
With $\frac{d}{dt}\cos\theta = -\dot{\theta}\sin\theta$ and $\frac{d}{dt}\sin\theta = \dot{\theta}\cos\theta$ ($\omega$, $H$, $W$ constant):
- $\dot{v}_x = W\omega\dot{\theta}\sin\theta$, $\quad v_y = H\omega - W\dot{\theta}\sin\theta$, $\quad \dot{v}_x - \omega v_y = 2W\omega\dot{\theta}\sin\theta - H\omega^2$
- $\dot{v}_y = -W(\ddot{\theta}\sin\theta + \dot{\theta}^2\cos\theta)$, $\quad \omega v_x = -W\omega^2\cos\theta$
- $\dot{v}_z = W(\ddot{\theta}\cos\theta - \dot{\theta}^2\sin\theta)$
$$ \mathbf{a}_{B/0} = (2W\omega\dot{\theta}\sin\theta - H\omega^2)\mathbf{i}_1 - (W\ddot{\theta}\sin\theta + W\dot{\theta}^2\cos\theta + W\omega^2\cos\theta)\mathbf{j}_1 + (W\ddot{\theta}\cos\theta - W\dot{\theta}^2\sin\theta)\mathbf{k}_1 $$
This agrees with the official key (Problems.pdf, PDF page 76).

### Phase 4: Physical Interpretation & Dimensional Check
* **Coriolis Coupling:** The term $2W\omega\dot{\theta}\sin\theta\,\mathbf{i}_1$ represents the Coriolis acceleration arising from the cross-coupling between satellite spin $\omega$ and panel deployment rate $\dot{\theta}$.
* **Dimensional Consistency:**
  - Every velocity component has units $[\text{length}] \cdot [\text{time}]^{-1} = \text{m/s}$.
  - Every acceleration component has units $[\text{length}] \cdot [\text{time}]^{-2} = \text{m/s}^2$ (Consistent ✅).
* **Limiting cases:**
  - $\dot{\theta} = 0$ (panel locked): $\mathbf{v}_{B/0} = -W\omega\cos\theta\,\mathbf{i}_1 + H\omega\,\mathbf{j}_1 = \omega\mathbf{k}_1 \times (H\mathbf{i}_1 + W\cos\theta\,\mathbf{j}_1 + W\sin\theta\,\mathbf{k}_1)$, the rigid-body velocity of a point of the spinning satellite.
  - $\omega = 0$ (no spin): $\mathbf{v}_{B/0} = W\dot{\theta}(-\sin\theta\,\mathbf{j}_1 + \cos\theta\,\mathbf{k}_1)$ and the acceleration reduces to the circular-motion terms $-W\dot{\theta}^2\,\mathbf{e}_{\text{rad}} + W\ddot{\theta}\,\mathbf{e}_{\text{tan}}$ about the hinge axis ($\mathbf{e}_{\text{rad}} = \mathbf{j}_2$, $\mathbf{e}_{\text{tan}} = \mathbf{k}_2$, radius $W$).
* **Symbolic check (sympy):** differentiating twice in the inertial frame the vector $[{}_0 R_1]\,(H,\ W\cos\theta,\ W\sin\theta)^T$ and projecting back on $\mathcal{B}_1$ with $[{}_0 R_1]^T$ gives exactly the $\mathbf{v}_{B/0}$ and $\mathbf{a}_{B/0}$ of Phase 3 (all components, zero residual).
