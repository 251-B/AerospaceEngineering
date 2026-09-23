---
subject: Mechanics Applied to Aerospace Engineering
topic: 1 - Fundamentals and Particle Kinematics
tags:
  - theory
  - key-concept
  - cylindrical-coordinates
  - spherical-coordinates
  - particle-kinematics
difficulty: medium
prerequisites:
  - "Multivariable Calculus"
  - "Orthonormal Vector Bases"
---

# 📖 Concept: Cartesian, Cylindrical, and Spherical Coordinate Systems

> **Key Takeaway in One Sentence:** Choosing the appropriate orthogonal curvilinear coordinate system tailors the mathematical description to the physical symmetries of the motion; the time-dependent rotation of moving unit vectors introduces characteristic inertial terms such as centripetal acceleration and Coriolis acceleration.

---

## 🎯 1. Physical Principle and Intuition

* **Cylindrical Coordinates $\{R, \theta, z\}$:** Naturally match problems with axisymmetry (turbomachinery, helicopter rotors, spin-stabilized rockets, vortex cores).
* **Spherical Coordinates $\{r, \theta, \phi\}$:** Naturally match central force problems and celestial mechanics (planetary orbits, ballistic trajectories, satellite ground tracks).

---

## 📐 2. Cylindrical Coordinates $\{R, \theta, z\}$

### 2.1 Coordinate Transformation
$$ \begin{cases} x = R\cos\theta \\ y = R\sin\theta \\ z = z \end{cases} \iff \begin{cases} R = \sqrt{x^2+y^2} \\ \theta = \arctan(y/x) \\ z = z \end{cases} $$

### 2.2 Moving Local Basis and Time Derivatives
$$ \mathbf{e}_R = \cos\theta\,\mathbf{i} + \sin\theta\,\mathbf{j}, \quad \mathbf{e}_\theta = -\sin\theta\,\mathbf{i} + \cos\theta\,\mathbf{j}, \quad \mathbf{e}_z = \mathbf{k} $$
$$ \dot{\mathbf{e}}_R = \dot{\theta}\,\mathbf{e}_\theta, \quad \dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_R, \quad \dot{\mathbf{e}}_z = \mathbf{0} $$

### 2.3 Kinematic Equations
* **Position:**
  $$ \mathbf{r}_0^P = R\,\mathbf{e}_R + z\,\mathbf{e}_z $$
* **Velocity:**
  $$ \mathbf{v}_0^P = \dot{R}\,\mathbf{e}_R + R\dot{\theta}\,\mathbf{e}_\theta + \dot{z}\,\mathbf{e}_z $$
* **Acceleration:**
  $$ \mathbf{a}_0^P = (\ddot{R} - R\dot{\theta}^2)\,\mathbf{e}_R + (R\ddot{\theta} + 2\dot{R}\dot{\theta})\,\mathbf{e}_\theta + \ddot{z}\,\mathbf{e}_z $$

> [!NOTE] Physical Breakdown of Terms
> * $\ddot{R}$: Linear radial acceleration.
> * $-R\dot{\theta}^2$: **Centripetal acceleration**, directed radially inwards toward the $Oz$ axis.
> * $R\ddot{\theta}$: Azimuthal acceleration due to angular acceleration.
> * $2\dot{R}\dot{\theta}$: **Coriolis acceleration term**, arising from the cross-coupling of radial velocity and azimuthal rotation.

---

## 📐 3. Spherical Coordinates $\{r, \theta, \phi\}$

### 3.1 Coordinate Transformation (Latitude Convention $\phi$)
* $r = \|\mathbf{r}_0^P\| \in [0, \infty)$: Spherical distance from the origin.
* $\theta \in [0, 2\pi)$: Azimuthal longitude in the $Oxy$ plane.
* $\phi \in [-\pi/2, \pi/2]$: **Latitude angle** measured upwards from the equatorial plane $Oxy$.

$$ \begin{cases} x = r\cos\phi\cos\theta \\ y = r\cos\phi\sin\theta \\ z = r\sin\phi \end{cases} \iff \begin{cases} r = \sqrt{x^2+y^2+z^2} \\ \theta = \arctan(y/x) \\ \phi = \arctan\left(\frac{z}{\sqrt{x^2+y^2}}\right) \end{cases} $$

### 3.2 Moving Local Basis and Time Derivatives
$$ \begin{cases}
\mathbf{e}_r = \cos\phi\cos\theta\,\mathbf{i} + \cos\phi\sin\theta\,\mathbf{j} + \sin\phi\,\mathbf{k} \\
\mathbf{e}_\theta = -\sin\theta\,\mathbf{i} + \cos\theta\,\mathbf{j} \\
\mathbf{e}_\phi = -\sin\phi\cos\theta\,\mathbf{i} - \sin\phi\sin\theta\,\mathbf{j} + \cos\phi\,\mathbf{k}
\end{cases} $$
$$ \dot{\mathbf{e}}_r = \dot{\theta}\cos\phi\,\mathbf{e}_\theta + \dot{\phi}\,\mathbf{e}_\phi, \quad \dot{\mathbf{e}}_\theta = -\dot{\theta}\cos\phi\,\mathbf{e}_r + \dot{\theta}\sin\phi\,\mathbf{e}_\phi, \quad \dot{\mathbf{e}}_\phi = -\dot{\phi}\,\mathbf{e}_r - \dot{\theta}\sin\phi\,\mathbf{e}_\theta $$

### 3.3 Kinematic Equations
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

## ⚠️ 4. Common Exam Pitfalls
> [!WARNING] Exam Precautions
> 1. Confusing radial cylindrical acceleration $a_R = \ddot{R} - R\dot{\theta}^2$ with intrinsic normal acceleration $a_n = v^2/\rho$. They only coincide for pure planar circles centered at the origin ($\dot{R}=0, R=\text{const}$).
> 2. Forgetting the factor 2 in the Coriolis term ($2\dot{R}\dot{\theta}$).
> 3. Confusing latitude $\phi$ with co-latitude $\psi = \pi/2 - \phi$: always check whether the angle is measured from the equator or the pole.

---

## 🔗 Related Concepts
* `[[Topic 1 - Fundamentals and Particle Kinematics|Topic 1: Fundamentals and Particle Kinematics]]`
* `[[Concept - Intrinsic Frenet-Serret Frame and Intrinsic Acceleration|Concept: Intrinsic Frenet-Serret Frame]]`
