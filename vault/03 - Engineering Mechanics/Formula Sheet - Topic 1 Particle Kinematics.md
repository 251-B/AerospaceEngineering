---
subject: Mechanics Applied to Aerospace Engineering
topic: 1 - Fundamentals and Particle Kinematics
tags:
  - formula-sheet
  - cheat-sheet
  - kinematics
  - quick-reference
---

# 📋 Formula Sheet: Particle Kinematics and Coordinate Systems

## ⚡ Fundamental Equations by Coordinate System

| System | Position Vector $\mathbf{r}_0^P$ | Velocity Vector $\mathbf{v}_0^P$ | Acceleration Vector $\mathbf{a}_0^P$ |
| :--- | :--- | :--- | :--- |
| **Cartesian** $\{x, y, z\}$ | $x\mathbf{i} + y\mathbf{j} + z\mathbf{k}$ | $\dot{x}\mathbf{i} + \dot{y}\mathbf{j} + \dot{z}\mathbf{k}$ | $\ddot{x}\mathbf{i} + \ddot{y}\mathbf{j} + \ddot{z}\mathbf{k}$ |
| **Cylindrical** $\{R, \theta, z\}$ | $R\mathbf{e}_R + z\mathbf{e}_z$ | $\dot{R}\mathbf{e}_R + R\dot{\theta}\mathbf{e}_\theta + \dot{z}\mathbf{e}_z$ | $(\ddot{R}-R\dot{\theta}^2)\mathbf{e}_R + (R\ddot{\theta}+2\dot{R}\dot{\theta})\mathbf{e}_\theta + \ddot{z}\mathbf{e}_z$ |
| **Spherical** $\{r, \theta, \phi\}$ | $r\mathbf{e}_r$ | $\dot{r}\mathbf{e}_r + r\dot{\theta}\cos\phi\,\mathbf{e}_\theta + r\dot{\phi}\,\mathbf{e}_\phi$ | See detailed breakdown below |
| **Intrinsic** $\{s\}$ (Frenet) | $\mathbf{r}(s)$ | $\dot{s}\,\mathbf{e}_t = v\,\mathbf{e}_t$ | $\ddot{s}\,\mathbf{e}_t + \frac{v^2}{\rho}\,\mathbf{e}_n = \dot{v}\,\mathbf{e}_t + \frac{v^2}{\rho}\,\mathbf{e}_n$ |

---

## 🧭 Acceleration Breakdown in Spherical Coordinates (Latitude $\phi$)
$$ a_r = \ddot{r} - r\dot{\theta}^2\cos^2\phi - r\dot{\phi}^2 $$
$$ a_\theta = 2\dot{r}\dot{\theta}\cos\phi + r\ddot{\theta}\cos\phi - 2r\dot{\theta}\dot{\phi}\sin\phi $$
$$ a_\phi = 2\dot{r}\dot{\phi} + r\ddot{\phi} + r\dot{\theta}^2\cos\phi\sin\phi $$

---

## 🎢 Frenet-Serret Formulas
$$ \frac{d\mathbf{e}_t}{ds} = \kappa\,\mathbf{e}_n = \frac{1}{\rho}\,\mathbf{e}_n $$
$$ \frac{d\mathbf{e}_n}{ds} = -\kappa\,\mathbf{e}_t + \tau\,\mathbf{e}_b = -\frac{1}{\rho}\,\mathbf{e}_t + \tau\,\mathbf{e}_b $$
$$ \frac{d\mathbf{e}_b}{ds} = -\tau\,\mathbf{e}_n $$
* **Curvature & Radius:** $\kappa = \frac{1}{\rho} = \left\|\frac{d\mathbf{e}_t}{ds}\right\| = \frac{\|\mathbf{v} \times \mathbf{a}\|}{v^3}$
* **Unit Tangent:** $\mathbf{e}_t = \frac{\mathbf{v}}{v}$
* **Principal Normal:** $\mathbf{e}_n = \rho \frac{d\mathbf{e}_t}{ds}$
* **Binormal:** $\mathbf{e}_b = \mathbf{e}_t \times \mathbf{e}_n = \frac{\mathbf{v} \times \mathbf{a}}{\|\mathbf{v} \times \mathbf{a}\|}$
* **Torsion:** $\tau = \frac{(\mathbf{v} \times \mathbf{a}) \cdot \dot{\mathbf{a}}}{\|\mathbf{v} \times \mathbf{a}\|^2}$

---

## 🔄 Elementary Rotation Matrices
* **$x$-axis:** $[R_x(\theta)] = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{bmatrix}$
* **$y$-axis:** $[R_y(\theta)] = \begin{bmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{bmatrix}$
* **$z$-axis:** $[R_z(\theta)] = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix}$

---

## 💡 Key Takeaways and Exam Rules
1. **Intrinsic Velocity:** $v_n \equiv 0$ and $v_b \equiv 0$. Velocity NEVER has a normal or binormal component!
2. **Intrinsic Acceleration:** $a_b \equiv 0$. Acceleration NEVER has a binormal component! Both $\mathbf{v}$ and $\mathbf{a}$ reside entirely in the **osculating plane**.
3. **Coriolis term in Cylindricals:** $2\dot{R}\dot{\theta}\mathbf{e}_\theta$. Vanishes if either $\dot{\theta}=0$ (no rotation) or $\dot{R}=0$ (constant radius).
4. **Centripetal term:** Always negative in the radial direction: $-R\dot{\theta}^2\mathbf{e}_R$.
