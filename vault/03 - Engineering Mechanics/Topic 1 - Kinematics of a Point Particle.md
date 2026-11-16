---
subject: Mechanics Applied to Aerospace Engineering
topic: 1 - Fundamentals and Particle Kinematics
course_code: "251-14165"
tags:
  - theory
  - kinematics
  - point-particle
  - coordinate-systems
  - frenet-serret
difficulty: medium
prerequisites:
  - "Calculus I & II"
  - "Linear Algebra"
  - "Physics I"
---

# 🚀 Topic 1: Fundamentals and Particle Kinematics

> **Core Foundational Result:**
> $$ \mathbf{v}_0^P = \dot{s}\,\mathbf{e}_t = v\,\mathbf{e}_t, \quad \mathbf{a}_0^P = \ddot{s}\,\mathbf{e}_t + \frac{v^2}{\rho}\,\mathbf{e}_n = a_t\,\mathbf{e}_t + a_n\,\mathbf{e}_n $$
> *Kinematics describes the geometry of motion without regard to the forces causing it. Any curved path decomposes particle acceleration into a tangential component (rate of speed change) and a centripetal normal component (rate of velocity direction change), both strictly confined to the local osculating plane.*

---

## 🧭 1. Introduction and Mechanical Modeling Philosophy

In Aerospace Engineering, every analysis and design task (whether for aircraft, launch vehicles, satellites, or planetary probes) requires developing a **mathematical model of reality**.

### 1.1 The Model is Not the Reality
A model is an idealized mathematical abstraction of an actual physical system:
* It retains only the essential features of interest (e.g. trajectory, stability, velocity, load distribution).
* It deliberately neglects secondary microscopic or irrelevant details that would cause mathematical intractability.
* Attempting to "solve reality" directly without modeling leads inevitably to *analysis paralysis*. In Newtonian mechanics, sound engineering requires stating explicitly:
  1. **The system under study:** its precise physical boundaries.
  2. **The environment:** all permissible interactions crossing those boundaries.
  3. **The simplifying assumptions:** every hypothesis adopted during formulation.

### 1.2 Fundamental Mechanical Models in the Course
In *Mechanics Applied to Aerospace Engineering*, two primary idealizations are employed:
1. **Point Particle:** An object of negligible dimensions compared to the characteristic length scales of its motion. Its spatial orientation (attitude) and internal deformations are disregarded; only translational motion is tracked (**3 degrees of freedom** in 3D Euclidean space $\mathbb{R}^3$).
   * *Aerospace Example:* A commercial transport aircraft modeled along a continental route of hundreds of kilometers, or a satellite in a Keplerian orbit around the Earth.
2. **Rigid Body:** An object of finite physical size and non-deformable geometry, where the Euclidean distance between any pair of its constituent points remains strictly constant over time:
   $$ \|\mathbf{r}^{P_i}(t) - \mathbf{r}^{P_j}(t)\| = \text{constant} \quad \forall t $$
   Describing a rigid body requires specifying both the position of an arbitrary reference point and the **attitude / spatial orientation** of the body (**6 degrees of freedom** in unconstrained 3D space).
   * *Aerospace Example:* An aircraft during pitch, yaw, and roll attitude maneuvers, or a spacecraft executing docking reorientation.
3. **Deformable Bodies:** Systems where structural elasticity under load (e.g., wing aeroelastic bending and flutter) directly couples with aerodynamics and dynamics. Treated in Structural Mechanics and Aeroelasticity.

---

## 📊 2. Physical Quantities: Scalars, Vectors, and Tensors

Any measurable or describable property of a mechanical system constitutes a physical quantity.

### 2.1 Classification by Tensorial Order
* **Scalars (Order 0):** Represented completely by a single real number accompanied by its SI dimensional unit. They possess no spatial direction.
  * *Examples:* Mass $m$ $[\text{kg}]$, time $t$ $[\text{s}]$, kinetic energy $T$ $[\text{J}]$, work $W$ $[\text{J}]$.
* **Vectors (Order 1):** Elements of $\mathbb{R}^N$ ($N=2,3$) possessing magnitude (norm), direction, sense, and physical units.
  * *Department Notation:* Boldface letters ($\mathbf{v}, \mathbf{F}, \mathbf{a}$); vector magnitude is denoted in standard typeface: $v = \|\mathbf{v}\|$.
* **Second-Order Tensors (Order 2):** Linear operators mapping vectors to vectors. Represented as square $N \times N$ matrices in a tensor product basis $\mathcal{B} \otimes \mathcal{B}$.
  * *Department Notation:* Double bar over the letter, such as the inertia tensor $\bar{\bar{I}}_0$. If $\mathbf{A}$ is a vector and $\bar{\bar{I}}$ a tensor, $\mathbf{B} = \bar{\bar{I}} \cdot \mathbf{A}$ is a vector and $p = \mathbf{A} \cdot \bar{\bar{I}} \cdot \mathbf{A}$ is a scalar.

### 2.2 Physical Classification of Vectors by Point of Application
1. **Free Vectors:** Physical effect and meaning do not depend on the point in space where they are drawn. They can be translated in parallel without altering their properties.
   * *Examples:* Angular velocity $\boldsymbol{\omega}$, angular acceleration $\boldsymbol{\alpha}$, pure torque couple $\mathbf{M}$.
2. **Sliding Vectors:** Physical effect on a rigid body is unaltered as long as the vector is shifted along its **line of action** (Principle of Transmissibility).
   * *Fundamental Example:* External force $\mathbf{F}$ applied to an indeformable rigid body.
3. **Bound / Fixed Vectors:** Physical effect depends strictly on the exact point of application in space.
   * *Examples:* Position vector $\mathbf{r}_0^P = \vec{OP}$ (bound to origin $O$), or forces on deformable elastic bodies where contact location governs internal stress concentrations.

> [!IMPORTANT]
> **Observer Invariance Principle:**
> Genuine physical entities (vectors and tensors such as wind velocity, gravity, or inertia) **do not depend on the observer or the mathematical vector basis chosen to project their numbers**. Changing bases alters component arrays, but the physical geometric vector remains unchanged:
> $$ \mathbf{A} = A_{x0}\mathbf{i}_0 + A_{y0}\mathbf{j}_0 + A_{z0}\mathbf{k}_0 = A_{x1}\mathbf{i}_1 + A_{y1}\mathbf{j}_1 + A_{z1}\mathbf{k}_1 $$

---

## 📐 3. Vector Spaces, Bases, and Rotation Matrices

### 3.1 Orthonormal Right-Handed Vector Basis
To operate analytically in $\mathbb{R}^3$, we select an ordered triad of 3 linearly independent unit vectors $\mathcal{B}_0 = \{\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ satisfying:
1. **Unit magnitude:** $\|\mathbf{i}_0\| = \|\mathbf{j}_0\| = \|\mathbf{k}_0\| = 1$.
2. **Mutual orthogonality:** $\mathbf{i}_0 \cdot \mathbf{j}_0 = \mathbf{j}_0 \cdot \mathbf{k}_0 = \mathbf{k}_0 \cdot \mathbf{i}_0 = 0$.
3. **Right-hand rule (dextral orientation):** $\mathbf{i}_0 \times \mathbf{j}_0 = \mathbf{k}_0$, $\mathbf{j}_0 \times \mathbf{k}_0 = \mathbf{i}_0$, $\mathbf{k}_0 \times \mathbf{i}_0 = \mathbf{j}_0$.

Any vector $\mathbf{A} \in \mathbb{R}^3$ is uniquely decomposed as:
$$ \mathbf{A} = A_{x0}\mathbf{i}_0 + A_{y0}\mathbf{j}_0 + A_{z0}\mathbf{k}_0 = \begin{bmatrix} A_{x0} \\ A_{y0} \\ A_{z0} \end{bmatrix}_0 $$

### 3.2 Change-of-Basis Matrix $[{}_0 R_1]$
Given two orthonormal bases $\mathcal{B}_0 = \{\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ and $\mathcal{B}_1 = \{\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$, the same vector $\mathbf{A}$ satisfies:
$$ \begin{bmatrix} A_{x0} \\ A_{y0} \\ A_{z0} \end{bmatrix}_0 = [{}_0 R_1] \begin{bmatrix} A_{x1} \\ A_{y1} \\ A_{z1} \end{bmatrix}_1, \quad [{}_0 R_1] = \begin{bmatrix} \ell_{x1,x0} & \ell_{y1,x0} & \ell_{z1,x0} \\ \ell_{x1,y0} & \ell_{y1,y0} & \ell_{z1,y0} \\ \ell_{x1,z0} & \ell_{y1,z0} & \ell_{z1,z0} \end{bmatrix} $$
where the columns of $[{}_0 R_1]$ are the components of $\{\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$ expressed in $\mathcal{B}_0$, and its rows are the components of $\{\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ in $\mathcal{B}_1$.

**Cardinal Properties of $[{}_0 R_1]$:**
1. **Orthogonal Matrix:** $[{}_1 R_0] = [{}_0 R_1]^{-1} = [{}_0 R_1]^T \implies [{}_0 R_1]^T [{}_0 R_1] = [U]$.
2. **Determinant Unity:** $\det([{}_0 R_1]) = +1$ (proper rotation preserving chirality).
3. **Euler's Rotation Theorem:** Any change of orthonormal right-handed bases is equivalent to a single pure rotation through an angle $\theta$ about an invariant unit axis $\mathbf{e}$. Consequently, $[{}_0 R_1]$ always has an eigenvalue $\lambda = 1$.

### 3.3 Simple Rotations About Coordinate Axes
* **Rotation about the $x$-axis by angle $\theta_x$:**
  $$ [{}_0 R_1(x, \theta_x)] = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\theta_x & -\sin\theta_x \\ 0 & \sin\theta_x & \cos\theta_x \end{bmatrix} $$
* **Rotation about the $y$-axis by angle $\theta_y$:**
  $$ [{}_0 R_1(y, \theta_y)] = \begin{bmatrix} \cos\theta_y & 0 & \sin\theta_y \\ 0 & 1 & 0 \\ -\sin\theta_y & 0 & \cos\theta_y \end{bmatrix} $$
* **Rotation about the $z$-axis by angle $\theta_z$:**
  $$ [{}_0 R_1(z, \theta_z)] = \begin{bmatrix} \cos\theta_z & -\sin\theta_z & 0 \\ \sin\theta_z & \cos\theta_z & 0 \\ 0 & 0 & 1 \end{bmatrix} $$

> [!WARNING] Sign Convention in $R_y$
> In $R_y(\theta_y)$, the minus sign appears at entry $(3,1)$, unlike $R_x$ and $R_z$ where it appears at entry $(1,2)$ or $(2,3)$. This stems from the right-hand rule in the plane perpendicular to the $y$-axis ($\mathbf{k}_0 \times \mathbf{i}_0 = \mathbf{j}_0$).

### 3.4 Composition and Infinitesimal Rotations
* **Finite Rotations (Non-Commutative):** Sequential rotations multiply from right to left: $[R] = [R_n]\cdots[R_1]$ and $[R_i][R_j] \neq [R_j][R_i]$.
* **Infinitesimal Rotations (Commutative):** For differential angles $d\theta_x, d\theta_y, d\theta_z \ll 1$:
  $$ [R] \approx [U] + [\Omega]\,dt, \quad [\Omega] = \begin{bmatrix} 0 & -\dot{\theta}_z & \dot{\theta}_y \\ \dot{\theta}_z & 0 & -\dot{\theta}_x \\ -\dot{\theta}_y & \dot{\theta}_x & 0 \end{bmatrix}, \quad [\Omega]\mathbf{A} \equiv \boldsymbol{\omega} \times \mathbf{A} $$
  where $\boldsymbol{\omega} = \dot{\theta}_x\mathbf{i} + \dot{\theta}_y\mathbf{j} + \dot{\theta}_z\mathbf{k}$ is the genuine **angular velocity vector**.

---

## ⏱️ 4. Reference Frames and Vector Time Differentiation

### 4.1 Definition of Reference Frame
A reference frame $S_0$ embodies an observer's perspective:
$$ S_0 = \{O; \mathcal{B}_0\} $$
comprising a spatial origin point $O$ and an orthonormal vector basis $\mathcal{B}_0 = \{\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$.

### 4.2 Time Derivative of a Vector: Magnitude vs. Direction
For any time-dependent vector $\mathbf{A}(t) = A(t)\,\mathbf{e}_A(t)$:
$$ \frac{d\mathbf{A}}{dt} = \frac{dA}{dt}\mathbf{e}_A + A\,\frac{d\mathbf{e}_A}{dt} = \frac{dA}{dt}\mathbf{e}_A + \boldsymbol{\omega} \times \mathbf{A} $$
* $\frac{dA}{dt}\mathbf{e}_A$ is parallel to $\mathbf{A}$ and accounts for magnitude changes.
* $\boldsymbol{\omega} \times \mathbf{A}$ is perpendicular to $\mathbf{A}$ and accounts for direction changes.

### 4.3 Poisson's Theorem (Kinematic Transport Formula)
Vector time derivatives depend on the observer's reference frame:
$$ \left.\frac{d\mathbf{b}}{dt}\right|_0 \neq \left.\frac{d\mathbf{b}}{dt}\right|_1 $$
If frame $S_1$ rotates with angular velocity $\boldsymbol{\omega}_{10}$ relative to $S_0$:
$$ \left.\frac{d\mathbf{A}}{dt}\right|_0 = \left.\frac{d\mathbf{A}}{dt}\right|_1 + \boldsymbol{\omega}_{10} \times \mathbf{A} $$

---

## 🎯 5. Point Particle Kinematics: Position, Velocity, and Acceleration

In an inertial reference frame $S_0 = \{O; \mathcal{B}_0\}$:

### 5.1 Position Vector $\mathbf{r}_0^P$
$$ \mathbf{r}_0^P(t) = \vec{OP} = x(t)\mathbf{i}_0 + y(t)\mathbf{j}_0 + z(t)\mathbf{k}_0 $$

### 5.2 Absolute Velocity Vector $\mathbf{v}_0^P$
$$ \mathbf{v}_0^P = \left.\frac{d\mathbf{r}_0^P}{dt}\right|_0 = \lim_{\Delta t \to 0} \frac{\Delta \mathbf{r}_0^P}{\Delta t} $$
* **Fundamental geometric property:** $\mathbf{v}_0^P$ is **always tangent to the particle's spatial trajectory**.
* **Speed / Celerity ($v$):** The scalar magnitude $v = \|\mathbf{v}_0^P\|$. Never confuse velocity (vector) with speed (scalar).

### 5.3 Absolute Acceleration Vector $\mathbf{a}_0^P$
$$ \mathbf{a}_0^P = \left.\frac{d\mathbf{v}_0^P}{dt}\right|_0 = \left.\frac{d^2\mathbf{r}_0^P}{dt^2}\right|_0 = \ddot{x}\mathbf{i}_0 + \ddot{y}\mathbf{j}_0 + \ddot{z}\mathbf{k}_0 $$
* While position $\mathbf{r}_0^P$ depends on the chosen origin $O$, **velocity and acceleration are independent of the origin $O$** (as long as $O$ is stationary in $S_0$).

---

## 🌐 6. Orthogonal Curvilinear Coordinate Systems

A point's position can be described by three coordinates $\{q_1, q_2, q_3\}$. The local vector basis is defined by:
$$ \mathbf{u}_{q_i} = \frac{\partial \mathbf{r}_0^P}{\partial q_i}, \quad \mathbf{e}_{q_i} = \frac{\mathbf{u}_{q_i}}{\|\mathbf{u}_{q_i}\|} $$

### 6.1 Cartesian Coordinates $\{x, y, z\}$
* Fixed basis: $\{\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$.
* $\mathbf{r}_0^P = x\mathbf{i}_0 + y\mathbf{j}_0 + z\mathbf{k}_0$
* $\mathbf{v}_0^P = \dot{x}\mathbf{i}_0 + \dot{y}\mathbf{j}_0 + \dot{z}\mathbf{k}_0$
* $\mathbf{a}_0^P = \ddot{x}\mathbf{i}_0 + \ddot{y}\mathbf{j}_0 + \ddot{z}\mathbf{k}_0$

---

### 6.2 Cylindrical Coordinates $\{R, \theta, z\}$
Ideal for systems with axial symmetry (rotors, propellers, pipes, atmospheric vortices).

#### Coordinate Transformation
$$ \begin{cases} x = R\cos\theta \\ y = R\sin\theta \\ z = z \end{cases} \iff \begin{cases} R = \sqrt{x^2+y^2} \\ \theta = \arctan(y/x) \\ z = z \end{cases} $$

#### Local Basis and Time Derivatives
$$ \begin{cases}
\mathbf{e}_R = \cos\theta\,\mathbf{i}_0 + \sin\theta\,\mathbf{j}_0 \\
\mathbf{e}_\theta = -\sin\theta\,\mathbf{i}_0 + \cos\theta\,\mathbf{j}_0 \\
\mathbf{e}_z = \mathbf{k}_0
\end{cases} $$
$$ \dot{\mathbf{e}}_R = \dot{\theta}\,\mathbf{e}_\theta, \quad \dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_R, \quad \dot{\mathbf{e}}_z = \mathbf{0} $$

#### Kinematic Equations
* **Position:**
  $$ \mathbf{r}_0^P = R\,\mathbf{e}_R + z\,\mathbf{e}_z $$
* **Velocity:**
  $$ \mathbf{v}_0^P = \dot{R}\,\mathbf{e}_R + R\dot{\theta}\,\mathbf{e}_\theta + \dot{z}\,\mathbf{e}_z $$
* **Acceleration:**
  $$ \mathbf{a}_0^P = (\ddot{R} - R\dot{\theta}^2)\,\mathbf{e}_R + (R\ddot{\theta} + 2\dot{R}\dot{\theta})\,\mathbf{e}_\theta + \ddot{z}\,\mathbf{e}_z $$

> [!NOTE] Physical Meaning of Acceleration Terms
> * $-R\dot{\theta}^2$: **Centripetal acceleration**, directed radially inwards toward the rotation axis.
> * $2\dot{R}\dot{\theta}$: **Coriolis acceleration term**, arising from simultaneous radial motion and azimuthal rotation.
> * Note: $(\ddot{R}-R\dot{\theta}^2)$ and $(R\ddot{\theta}+2\dot{R}\dot{\theta})$ do **not** generally equal normal and tangential acceleration.

---

### 6.3 Spherical Coordinates $\{r, \theta, \phi\}$
Standard in orbital mechanics, central gravitational fields, and inertial navigation.

#### Coordinate Transformation (Latitude Convention $\phi$)
* $r = \|\mathbf{r}_0^P\| \in [0, \infty)$: Spherical radius.
* $\theta \in [0, 2\pi)$: Azimuthal angle in the $Oxy$ plane.
* $\phi \in [-\pi/2, \pi/2]$: **Latitude angle** measured upwards from the equatorial plane $Oxy$.

$$ \begin{cases} x = r\cos\phi\cos\theta \\ y = r\cos\phi\sin\theta \\ z = r\sin\phi \end{cases} \iff \begin{cases} r = \sqrt{x^2+y^2+z^2} \\ \theta = \arctan(y/x) \\ \phi = \arctan\left(\frac{z}{\sqrt{x^2+y^2}}\right) \end{cases} $$

#### Local Basis and Time Derivatives
$$ \begin{cases}
\mathbf{e}_r = \cos\phi\cos\theta\,\mathbf{i}_0 + \cos\phi\sin\theta\,\mathbf{j}_0 + \sin\phi\,\mathbf{k}_0 \\
\mathbf{e}_\theta = -\sin\theta\,\mathbf{i}_0 + \cos\theta\,\mathbf{j}_0 \\
\mathbf{e}_\phi = -\sin\phi\cos\theta\,\mathbf{i}_0 - \sin\phi\sin\theta\,\mathbf{j}_0 + \cos\phi\,\mathbf{k}_0
\end{cases} $$
$$ \dot{\mathbf{e}}_r = \dot{\theta}\cos\phi\,\mathbf{e}_\theta + \dot{\phi}\,\mathbf{e}_\phi, \quad \dot{\mathbf{e}}_\theta = -\dot{\theta}\cos\phi\,\mathbf{e}_r + \dot{\theta}\sin\phi\,\mathbf{e}_\phi, \quad \dot{\mathbf{e}}_\phi = -\dot{\phi}\,\mathbf{e}_r - \dot{\theta}\sin\phi\,\mathbf{e}_\theta $$

#### Kinematic Equations
* **Position:**
  $$ \mathbf{r}_0^P = r\,\mathbf{e}_r $$
* **Velocity:**
  $$ \mathbf{v}_0^P = \dot{r}\,\mathbf{e}_r + r\dot{\theta}\cos\phi\,\mathbf{e}_\theta + r\dot{\phi}\,\mathbf{e}_\phi $$
* **Acceleration:**
  $$ \mathbf{a}_0^P = a_r\,\mathbf{e}_r + a_\theta\,\mathbf{e}_\theta + a_\phi\,\mathbf{e}_\phi $$
  $$ \begin{cases}
  a_r = \ddot{r} - r\dot{\theta}^2\cos^2\phi - r\dot{\phi}^2 \\
  a_\theta = 2\dot{r}\dot{\theta}\cos\phi + r\ddot{\theta}\cos\phi - 2r\dot{\theta}\dot{\phi}\sin\phi \\
  a_\phi = 2\dot{r}\dot{\phi} + r\ddot{\phi} + r\dot{\theta}^2\cos\phi\sin\phi
  \end{cases} $$

---

## 🎛️ 7. Degrees of Freedom, Generalized Coordinates, and Constraints

* **Configuration Degrees of Freedom (DOF):** The minimum number of independent coordinates required to completely and unambiguously fix the position of all elements of the system:
  * Free particle in 3D space: $\text{DOF} = 3$.
  * Particle constrained to a smooth regular surface $f(x,y,z) = 0$: $\text{DOF} = 3 - 1 = 2$.
  * Particle constrained to a spatial curve $f=0, g=0$: $\text{DOF} = 3 - 2 = 1$.
* **Generalized Coordinates ($q_i$):** Any set of independent parameters (distances, angles, arc lengths) chosen to parametrize the configuration space while intrinsically respecting kinematic constraints.

---

## 🎢 8. Trajectory and the Intrinsic Frenet-Serret Basis

### 8.1 Arc Length Parameter $s(t)$
For any spatial trajectory $\mathbf{r}_0^P = \mathbf{r}_0^P(s)$, the arc length differential is:
$$ ds = \|d\mathbf{r}_0^P\| = \sqrt{dx^2 + dy^2 + dz^2} $$

### 8.2 The Frenet-Serret Triad $\{\mathbf{e}_t, \mathbf{e}_n, \mathbf{e}_b\}$

1. **Unit Tangent Vector ($\mathbf{e}_t$):**
   $$ \mathbf{e}_t = \frac{d\mathbf{r}_0^P}{ds} = \lim_{\Delta s \to 0}\frac{\Delta \mathbf{r}_0^P}{\Delta s}, \quad \|\mathbf{e}_t\| = 1 $$
2. **Principal Normal Unit Vector ($\mathbf{e}_n$) and Curvature ($\kappa$):**
   Since $\|\mathbf{e}_t\|^2 = 1 \implies \mathbf{e}_t \cdot \frac{d\mathbf{e}_t}{ds} = 0$, the derivative of $\mathbf{e}_t$ with respect to $s$ is strictly normal to the curve. The **curvature $\kappa$** and **radius of curvature $\rho$** are defined as:
   $$ \kappa = \left\|\frac{d\mathbf{e}_t}{ds}\right\| = \frac{d\theta}{ds} = \frac{1}{\rho} \implies \frac{d\mathbf{e}_t}{ds} = \kappa\,\mathbf{e}_n = \frac{1}{\rho}\,\mathbf{e}_n $$
   * $\mathbf{e}_n$ points always towards the **local center of curvature $C$** of the **osculating circle**.
   * Along straight segments, $\rho \to \infty$, $\kappa \to 0$, and $\mathbf{e}_n$ is undefined.
3. **Binormal Unit Vector ($\mathbf{e}_b$) and Torsion ($\tau$):**
   Completes the right-handed orthonormal triad:
   $$ \mathbf{e}_b = \mathbf{e}_t \times \mathbf{e}_n $$
   * $\mathbf{e}_b$ is perpendicular to the **osculating plane** defined by $\{\mathbf{e}_t, \mathbf{e}_n\}$.
   * Torsion $\tau$ measures the rate of rotation (twisting) of the osculating plane along $s$:
     $$ \frac{d\mathbf{e}_b}{ds} = -\tau\,\mathbf{e}_n $$

### 8.3 The 3D Frenet-Serret Formulas
$$ \begin{bmatrix} d\mathbf{e}_t/ds \\ d\mathbf{e}_n/ds \\ d\mathbf{e}_b/ds \end{bmatrix} = \begin{bmatrix} 0 & \kappa & 0 \\ -\kappa & 0 & \tau \\ 0 & -\tau & 0 \end{bmatrix} \begin{bmatrix} \mathbf{e}_t \\ \mathbf{e}_n \\ \mathbf{e}_b \end{bmatrix} $$

---

## ⚡ 9. Tangential and Normal Acceleration

Using the chain rule $\frac{d}{dt} = \frac{ds}{dt}\frac{d}{ds} = v\frac{d}{ds}$:

### 9.1 Intrinsic Velocity
$$ \mathbf{v}_0^P = \frac{d\mathbf{r}_0^P}{dt} = \frac{d\mathbf{r}_0^P}{ds}\frac{ds}{dt} = \dot{s}\,\mathbf{e}_t = v\,\mathbf{e}_t $$
* **Crucial Property:** The velocity vector has **only a tangential component**. Normal and binormal components are identically zero: $v_n \equiv 0, v_b \equiv 0$.

### 9.2 Intrinsic Acceleration
$$ \mathbf{a}_0^P = \frac{d\mathbf{v}_0^P}{dt} = \frac{d}{dt}(v\,\mathbf{e}_t) = \dot{v}\,\mathbf{e}_t + v\left(\frac{d\mathbf{e}_t}{ds}\frac{ds}{dt}\right) = \dot{v}\,\mathbf{e}_t + \frac{v^2}{\rho}\,\mathbf{e}_n $$
$$ a_t = \ddot{s} = \dot{v}, \quad a_n = \frac{v^2}{\rho} = \kappa v^2, \quad a_b \equiv 0 $$

### 9.3 Four Cardinal Physical Theorems
1. **$a_t = \dot{v}$** is solely responsible for changes in speed (velocity magnitude). If speed is constant, $a_t = 0$.
2. **$a_n = \frac{v^2}{\rho}$** is solely responsible for changes in the direction of the velocity vector. It points always towards the concave side (center of curvature $C$).
3. **Binormal acceleration is strictly zero ($a_b \equiv 0$).**
4. **Confinement to the Osculating Plane:** Both velocity $\mathbf{v}$ and acceleration $\mathbf{a}$ **always lie within the osculating plane** spanned by $\{\mathbf{e}_t, \mathbf{e}_n\}$.

---

## 🧮 10. Analytical Case Study: The Helicoidal Rocket Trajectory (Slide 29)

> **Pedagogical Audit (`problem_step_mentor`):**  
> This lecture exercise synthesizes all Topic 1 fundamentals: transforming between Cartesian, Cylindrical, and Intrinsic coordinates via **orthogonal rotation matrices $[{}_0 R_C]$**, arc length calculation $s(t)$, and evaluating the Frenet-Serret frame and osculating radius $\rho$. Every single step is explained with complete algebra and official references to `Notes.pdf`.

### Problem Statement (Slide 29)
An out-of-control experimental rocket traces an upward helical trajectory in 3D space, described in Cartesian coordinates for $t > 0$ by:
$$ x(t) = a\cos(\omega t), \quad y(t) = a\sin(\omega t), \quad z(t) = v_z t $$
where $a > 0$, $\omega > 0$, and $v_z > 0$ are known constants.

---

### Step 0: Physical Analysis, Degrees of Freedom, and Surface Constraint
* **Physical Aerospace Context:** Models an unguided spin-stabilized rocket with an induced roll rate $\omega$ and a steady vertical climb velocity $v_z$.
* **Geometric Surface Constraint:**  
  Squaring and adding $x(t)$ and $y(t)$:
  $$ x(t)^2 + y(t)^2 = [a\cos(\omega t)]^2 + [a\sin(\omega t)]^2 = a^2(\cos^2\omega t + \sin^2\omega t) = a^2 $$
  The particle is geometrically constrained to move on a **right circular cylinder of radius $a$** with central axis along $Oz$:
  $$ f(x, y, z) = x^2 + y^2 - a^2 = 0 $$
  Per Section 2.7 of `Notes.pdf`, this holonomic surface constraint reduces the configuration degrees of freedom from 3 to $3 - 1 = 2$ DOF. Cylindrical coordinates $\{R, \theta, z\}$ are naturally tailored to this problem since $R = a = \text{const}$.

---

### Vector Bases and Derivation of the Change-of-Basis Matrix $[{}_0 R_C]$

We identify the relevant bases:
* Fixed Cartesian basis: $\mathcal{B}_0 = \{\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ ($\dot{\mathbf{i}}_0 = \dot{\mathbf{j}}_0 = \dot{\mathbf{k}}_0 = \mathbf{0}$).
* Moving Cylindrical basis: $\mathcal{B}_C = \{\mathbf{e}_R, \mathbf{e}_\theta, \mathbf{e}_z\}$, rotating at $\theta(t) = \omega t$.

Projecting the unit vectors of $\mathcal{B}_C$ onto $\mathcal{B}_0$:
$$ \mathbf{e}_R = \cos\theta\,\mathbf{i}_0 + \sin\theta\,\mathbf{j}_0 + 0\,\mathbf{k}_0 $$
$$ \mathbf{e}_\theta = -\sin\theta\,\mathbf{i}_0 + \cos\theta\,\mathbf{j}_0 + 0\,\mathbf{k}_0 $$
$$ \mathbf{e}_z = 0\,\mathbf{i}_0 + 0\,\mathbf{j}_0 + 1\,\mathbf{k}_0 $$

According to **Eq. (1.13) of `Notes.pdf`**, the columns of the change-of-basis matrix $[{}_0 R_C]$ are the components of $\{\mathbf{e}_R, \mathbf{e}_\theta, \mathbf{e}_z\}$ in $\mathcal{B}_0$:
$$ [{}_0 R_C(\theta)] = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix} $$
This matches the elementary rotation matrix $R_z(\theta)$ (Eq. 1.20 of `Notes.pdf`).

By matrix orthogonality (Eq. 1.14 of `Notes.pdf`), the inverse transformation matrix from $\mathcal{B}_0$ to $\mathcal{B}_C$ is simply the transpose:
$$ [{}_C R_0(\theta)] = [{}_0 R_C(\theta)]^{-1} = [{}_0 R_C(\theta)]^T = \begin{bmatrix} \cos\theta & \sin\theta & 0 \\ -\sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix} $$

---

### Detailed Step-by-Step Analytical Derivation

#### (a) Kinematics in the Cartesian System $\{\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$
* **Pedagogical Rationale:** In the inertial frame $S_0$, Cartesian unit vectors are strictly constant in time. Per Eq. (2.6) of `Notes.pdf`, time differentiation acts directly on each scalar component without requiring Coriolis transport terms.
1. **Position Vector:**
   $$ \mathbf{r}_0^P(t) = a\cos(\omega t)\,\mathbf{i}_0 + a\sin(\omega t)\,\mathbf{j}_0 + v_z t\,\mathbf{k}_0 = \begin{bmatrix} a\cos(\omega t) \\ a\sin(\omega t) \\ v_z t \end{bmatrix}_0 $$
2. **Velocity Vector:** Differentiating with respect to $t$ using the chain rule:
   $$ \dot{x}(t) = -a\omega\sin(\omega t), \quad \dot{y}(t) = a\omega\cos(\omega t), \quad \dot{z}(t) = v_z $$
   $$ \mathbf{v}_0^P(t) = -a\omega\sin(\omega t)\,\mathbf{i}_0 + a\omega\cos(\omega t)\,\mathbf{j}_0 + v_z\,\mathbf{k}_0 = \begin{bmatrix} -a\omega\sin(\omega t) \\ a\omega\cos(\omega t) \\ v_z \end{bmatrix}_0 $$
3. **Acceleration Vector:** Differentiating velocity with respect to $t$ (Eq. 2.7 of `Notes.pdf`):
   $$ \ddot{x}(t) = -a\omega^2\cos(\omega t), \quad \ddot{y}(t) = -a\omega^2\sin(\omega t), \quad \ddot{z}(t) = 0 $$
   $$ \mathbf{a}_0^P(t) = -a\omega^2\cos(\omega t)\,\mathbf{i}_0 - a\omega^2\sin(\omega t)\,\mathbf{j}_0 + 0\,\mathbf{k}_0 = \begin{bmatrix} -a\omega^2\cos(\omega t) \\ -a\omega^2\sin(\omega t) \\ 0 \end{bmatrix}_0 $$

---

#### (b) Kinematics in the Cylindrical System $\{\mathbf{e}_R, \mathbf{e}_\theta, \mathbf{e}_z\}$ via Change-of-Basis Matrix
* **Pedagogical Rationale:** Rather than relying on memorized formulas, we apply the change-of-basis matrix $[\mathbf{A}]_C = [{}_C R_0][\mathbf{A}]_0$ (Eq. 1.12 of `Notes.pdf`).

1. **Position Vector Transformation:**
   $$ \begin{bmatrix} r_R \\ r_\theta \\ r_z \end{bmatrix}_C = \begin{bmatrix} \cos(\omega t) & \sin(\omega t) & 0 \\ -\sin(\omega t) & \cos(\omega t) & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} a\cos(\omega t) \\ a\sin(\omega t) \\ v_z t \end{bmatrix}_0 = \begin{bmatrix} a(\cos^2\omega t + \sin^2\omega t) \\ -a\sin\omega t\cos\omega t + a\sin\omega t\cos\omega t \\ v_z t \end{bmatrix} = \begin{bmatrix} a \\ 0 \\ v_z t \end{bmatrix}_C $$
   $$ \mathbf{r}_0^P = a\,\mathbf{e}_R + v_z t\,\mathbf{e}_z $$
   *(In cylindrical coordinates, position has zero azimuthal component $r_\theta \equiv 0$ by definition).*

2. **Velocity Vector Transformation:**
   $$ \begin{bmatrix} v_R \\ v_\theta \\ v_z \end{bmatrix}_C = \begin{bmatrix} \cos(\omega t) & \sin(\omega t) & 0 \\ -\sin(\omega t) & \cos(\omega t) & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} -a\omega\sin(\omega t) \\ a\omega\cos(\omega t) \\ v_z \end{bmatrix}_0 = \begin{bmatrix} 0 \\ a\omega \\ v_z \end{bmatrix}_C $$
   $$ \mathbf{v}_0^P = a\omega\,\mathbf{e}_\theta + v_z\,\mathbf{e}_z $$
   *(Because $R = a = \text{const} \implies \dot{R} = 0$, radial velocity vanishes identically).*

3. **Acceleration Vector Transformation:**
   $$ \begin{bmatrix} a_R \\ a_\theta \\ a_z \end{bmatrix}_C = \begin{bmatrix} \cos(\omega t) & \sin(\omega t) & 0 \\ -\sin(\omega t) & \cos(\omega t) & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} -a\omega^2\cos(\omega t) \\ -a\omega^2\sin(\omega t) \\ 0 \end{bmatrix}_0 = \begin{bmatrix} -a\omega^2 \\ 0 \\ 0 \end{bmatrix}_C $$
   $$ \mathbf{a}_0^P = -a\omega^2\,\mathbf{e}_R $$
   *Verification with Eq. (2.30) of `Notes.pdf`:*
   $$ a_R = \ddot{R} - R\dot{\theta}^2 = 0 - a\omega^2 = -a\omega^2 $$
   $$ a_\theta = R\ddot{\theta} + 2\dot{R}\dot{\theta} = a(0) + 2(0)(\omega) = 0 $$
   $$ a_z = \ddot{z} = 0 $$
   The acceleration is purely centripetal, pointing directly towards the cylinder's central axis $Oz$.

---

#### (c) Speed / Celerity ($v$)
* **Pedagogical Rationale:** Speed is an invariant scalar quantity ($v = \|\mathbf{v}_0^P\|$) required to determine the arc length relation $ds = v\,dt$.
$$ v = \sqrt{v_R^2 + v_\theta^2 + v_z^2} = \sqrt{0^2 + (a\omega)^2 + v_z^2} = \sqrt{a^2\omega^2 + v_z^2} = \text{constant} $$
The rocket travels along the helical curve with **uniform speed**.

---

#### (d) Arc Length Coordinate $s(t)$
* **Pedagogical Rationale:** By Eq. (2.16) of `Notes.pdf`, $v = \dot{s} = \frac{ds}{dt}$. Integrating with initial condition $s(0) = 0$:
$$ s(t) = \int_0^t v\,dt' = \int_0^t \sqrt{a^2\omega^2 + v_z^2}\,dt' = t\sqrt{a^2\omega^2 + v_z^2} $$

---

#### (e) Intrinsic Frenet-Serret Basis and Intrinsic Acceleration
* **Pedagogical Rationale:** The Frenet-Serret frame decouples speed rate-of-change ($a_t$) from directional turning ($a_n$).
1. **Unit Tangent Vector $\mathbf{e}_t$ (Eq. 2.9 of `Notes.pdf`):**
   $$ \mathbf{e}_t = \frac{\mathbf{v}_0^P}{v} = \frac{-a\omega\sin(\omega t)\,\mathbf{i}_0 + a\omega\cos(\omega t)\,\mathbf{j}_0 + v_z\,\mathbf{k}_0}{\sqrt{a^2\omega^2 + v_z^2}} = \frac{a\omega\,\mathbf{e}_\theta + v_z\,\mathbf{e}_z}{\sqrt{a^2\omega^2 + v_z^2}} $$
2. **Tangential Acceleration $a_t$ (Eq. 2.18 of `Notes.pdf`):**
   $$ a_t = \dot{v} = \frac{d}{dt}\left(\sqrt{a^2\omega^2 + v_z^2}\right) = 0 $$
3. **Curvature $\kappa$ and Radius of Curvatura $\rho$ (Eq. 2.12 of `Notes.pdf`):**
   Applying $\frac{d}{ds} = \frac{1}{v}\frac{d}{dt}$:
   $$ \frac{d\mathbf{e}_t}{ds} = \frac{1}{v}\frac{d\mathbf{e}_t}{dt} = \frac{-a\omega^2(\cos\omega t\,\mathbf{i}_0 + \sin\omega t\,\mathbf{j}_0)}{a^2\omega^2 + v_z^2} = -\frac{a\omega^2}{a^2\omega^2 + v_z^2}\,\mathbf{e}_R $$
   The curvature is the norm of this derivative:
   $$ \kappa = \left\|\frac{d\mathbf{e}_t}{ds}\right\| = \frac{a\omega^2}{a^2\omega^2 + v_z^2} \implies \rho = \frac{1}{\kappa} = a\left(1 + \frac{v_z^2}{a^2\omega^2}\right) $$
   *Physical interpretation:* For $v_z = 0$, $\rho = a$ (circular path). Vertical climb $v_z > 0$ stretches the helix, flattening the curve and increasing its osculating radius $\rho > a$.
4. **Principal Normal Vector $\mathbf{e}_n$ (Eq. 2.11 of `Notes.pdf`):**
   $$ \mathbf{e}_n = \frac{1}{\kappa}\frac{d\mathbf{e}_t}{ds} = -\mathbf{e}_R = -(\cos\omega t\,\mathbf{i}_0 + \sin\omega t\,\mathbf{j}_0) $$
   $\mathbf{e}_n$ points directly inwards toward the axis of rotation $Oz$.
5. **Normal Acceleration $a_n$ (Eq. 2.18 of `Notes.pdf`):**
   $$ a_n = \frac{v^2}{\rho} = \kappa v^2 = a\omega^2 $$
   $$ \mathbf{a}_0^P = a_t\,\mathbf{e}_t + a_n\,\mathbf{e}_n = 0\,\mathbf{e}_t + a\omega^2(-\mathbf{e}_R) = -a\omega^2\,\mathbf{e}_R $$
6. **Binormal Unit Vector $\mathbf{e}_b = \mathbf{e}_t \times \mathbf{e}_n$:**
   $$ \mathbf{e}_b = \left( \frac{a\omega\,\mathbf{e}_\theta + v_z\,\mathbf{e}_z}{\sqrt{a^2\omega^2 + v_z^2}} \right) \times (-\mathbf{e}_R) = \frac{-v_z\,\mathbf{e}_\theta + a\omega\,\mathbf{e}_z}{\sqrt{a^2\omega^2 + v_z^2}} $$

---

#### (f) Center of Curvature $C$ at Position $(a, 0, 0)$
* **Pedagogical Rationale:** The center of curvature $C$ of the osculating circle is located at distance $\rho$ along $\mathbf{e}_n$ (Section 2.4 and Figure 2.2 of `Notes.pdf`):
$$ \mathbf{r}_C(t) = \mathbf{r}(t) + \rho\,\mathbf{e}_n(t) $$
At $(a, 0, 0)$, time is $t = 0$. Here $\mathbf{r}(0) = a\,\mathbf{i}_0$ and $\mathbf{e}_n(0) = -\mathbf{i}_0$:
$$ \mathbf{r}_C(0) = a\,\mathbf{i}_0 + \left(a + \frac{v_z^2}{a\omega^2}\right)(-\mathbf{i}_0) = -\frac{v_z^2}{a\omega^2}\,\mathbf{i}_0 $$
$$ C = \left( -\frac{v_z^2}{a\omega^2}, \, 0, \, 0 \right) $$
*Physical Insight:* The center of the osculating circle does not lie on the cylinder's axis $(0,0,0)$, but is shifted along the negative $x$-axis by $\frac{v_z^2}{a\omega^2}$ due to the upward pitch angle of the helix.
