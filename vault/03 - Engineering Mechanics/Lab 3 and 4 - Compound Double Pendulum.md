---
subject: Mechanics Applied to Aerospace Engineering
topic: Laboratory 3 & 4 - Compound Double Pendulum
course_code: "251-14165"
tags:
  - laboratory
  - rigid-body-dynamics
  - compound-double-pendulum
  - deterministic-chaos
  - numerical-methods
  - ode23s
  - newton-euler
  - video-tracking
difficulty: expert
sources:
  - "[[mechanics_labs.pdf]]"
---

# ⛓️ Laboratory 3 & 4: Compound Double Pendulum (Experimental & Numerical)

> **Primary Course Reference:** *Mechanics Applied to Aerospace Engineering (MAAE) — UC3M*  
> **Source Document:** [[mechanics_labs.pdf]] (pp. 19–26)  
> **Theoretical Prerequisites:** [[Topic 7 - Kinematics of Rigid Bodies and Euler Angles]], [[Topic 8 - Geometry of Masses and Inertia Tensor]], [[Topic 10 - Rigid Body Dynamics and Euler's Equations]]  
> **Navigation:** [[Lab - Guidelines and Scientific Report Standards|Guidelines]] | [[Mecanica de Estructuras MOC|⬅️ Mechanics MOC]]

---

## 📌 1. Physical System Description

The **compound double pendulum** consists of two planar rigid limbs of distributed mass and finite rotational inertia connected in series by low-friction revolute joints (pivots):

1. **Upper Limb (Pendulum 1):** Length $l_1$, mass $m_1$, center of mass $G_1$, and moment of inertia $I_1$ about the out-of-plane axis through $G_1$. It pivots about the fixed point $P_1(0,0)$ and carries the moving pivot $P_2$ at distance $L_1 = \|\mathbf{P_1P_2}\|$. The distance to its center of mass is $R_1 = \|\mathbf{P_1G_1}\|$.
2. **Lower Limb (Pendulum 2):** Length $l_2$, mass $m_2$, center of mass $G_2$, and moment of inertia $I_2$ about the out-of-plane axis through $G_2$. It is suspended from the moving pivot $P_2$. The distance to its center of mass is $R_2 = \|\mathbf{P_2G_2}\|$.
3. **Pivots and Markers:**
   * $P_1(0,0)$: Fixed origin pivot.
   * $P_2$: Intermediate joint connecting limb 1 and limb 2.
   * $P_3$: Tip marker on limb 2 (used for optical video tracking).
   * Markers are color-coded (Blue, Red, Green) for digital video motion tracking.

```
          P1(0,0) [Fixed]
             \
              \  \theta_1
               \
                G1(x1, y1)  [Center of mass 1]
                 \
                  \
                   P2(xP2, yP2) [Moving Joint]
                    \
                     \  \theta_2
                      \
                       G2(x2, y2) [Center of mass 2]
                        \
                         \
                          P3 (Tip Marker)
```

### Table 1: Standard Limb Geometries and Masses (UC3M Apparatus)
| Total Length ($l$) | Pivot Distance ($L$) | Mass ($m$) | Width ($w$) | Thickness ($t$) |
| :--- | :--- | :--- | :--- | :--- |
| **$350\text{ mm}$** | $297\text{ mm}$ | $560 \pm 1\text{ g}$ | $50\text{ mm}$ | $12.5\text{ mm}$ |
| **$300\text{ mm}$** | $247\text{ mm}$ | $480 \pm 1\text{ g}$ | $50\text{ mm}$ | $12.5\text{ mm}$ |
| **$250\text{ mm}$** | $197\text{ mm}$ | $400 \pm 1\text{ g}$ | $50\text{ mm}$ | $12.5\text{ mm}$ |

---

## 🧮 2. Moment of Inertia with Rounded Tips

Each limb is a rectangular bar with semicircular rounded ends of radius $r = w/2 = 25\text{ mm}$. To compute the exact moment of inertia about the center of gravity ($I_{G}$):
* Decompose the limb into a central rectangular prism of length $l_{\text{rect}} = l - 2r = l - w$ and two half-cylinders of radius $r$ and thickness $t$.
* Apply Steiner's Parallel Axis Theorem to translate the inertial contributions to the composite center of mass $G$.
* For a simplified homogeneous rectangular bar approximation:
  $$I_{G} \approx \frac{1}{12}m\left(l^2 + w^2\right)$$
  *(In the laboratory report, the exact composite geometry accounting for the rounded tips and pivot holes must be evaluated).*

---

## 📐 3. Mathematical Model: Symmetric Setup ($\varphi = 0$)

The angles $\theta_1$ and $\theta_2$ are measured clockwise from the downward vertical ($-\mathbf{j}$).

### 3.1 Kinematics
Position vectors:
$$\mathbf{r}_0^{G_1} = R_1\sin\theta_1\,\mathbf{i} - R_1\cos\theta_1\,\mathbf{j}$$
$$\mathbf{r}_0^{P_2} = L_1\sin\theta_1\,\mathbf{i} - L_1\cos\theta_1\,\mathbf{j}$$
$$\mathbf{r}_0^{G_2} = \mathbf{r}_0^{P_2} + R_2\sin\theta_2\,\mathbf{i} - R_2\cos\theta_2\,\mathbf{j} = \left(L_1\sin\theta_1 + R_2\sin\theta_2\right)\mathbf{i} - \left(L_1\cos\theta_1 + R_2\cos\theta_2\right)\mathbf{j}$$

Velocities of centers of mass:
$$\mathbf{v}_0^{G_1} = \dot{\theta}_1 R_1\cos\theta_1\,\mathbf{i} + \dot{\theta}_1 R_1\sin\theta_1\,\mathbf{j}$$
$$\mathbf{v}_0^{G_2} = \left(\dot{\theta}_1 L_1\cos\theta_1 + \dot{\theta}_2 R_2\cos\theta_2\right)\mathbf{i} + \left(\dot{\theta}_1 L_1\sin\theta_1 + \dot{\theta}_2 R_2\sin\theta_2\right)\mathbf{j}$$

Accelerations of centers of mass:
$$\mathbf{a}_0^{G_1} = \left(-\dot{\theta}_1^2 R_1\sin\theta_1 + \ddot{\theta}_1 R_1\cos\theta_1\right)\mathbf{i} + \left(\dot{\theta}_1^2 R_1\cos\theta_1 + \ddot{\theta}_1 R_1\sin\theta_1\right)\mathbf{j}$$
$$\mathbf{a}_0^{G_2} = \left(-\dot{\theta}_1^2 L_1\sin\theta_1 + \ddot{\theta}_1 L_1\cos\theta_1 - \dot{\theta}_2^2 R_2\sin\theta_2 + \ddot{\theta}_2 R_2\cos\theta_2\right)\mathbf{i} + \left(\dot{\theta}_1^2 L_1\cos\theta_1 + \ddot{\theta}_1 L_1\sin\theta_1 + \dot{\theta}_2^2 R_2\cos\theta_2 + \ddot{\theta}_2 R_2\sin\theta_2\right)\mathbf{j}$$

### 3.2 Newton-Euler Dynamic Equations
Let $\mathbf{T}_1 = T_{1x}\mathbf{i} + T_{1y}\mathbf{j}$ be the reaction at pivot $P_1$, and $\mathbf{T}_2 = T_{2x}\mathbf{i} + T_{2y}\mathbf{j}$ the reaction on limb 1 at pivot $P_2$ (by Newton's third law, $-\mathbf{T}_2$ acts on limb 2).

For Pendulum 1:
$$m_1 \ddot{x}_1 = T_{1x} + T_{2x}$$
$$m_1 \ddot{y}_1 = T_{1y} + T_{2y} - m_1 g$$
$$I_1 \ddot{\theta}_1 = (-\mathbf{r}_0^{G_1}) \times \mathbf{T}_1 + (\mathbf{r}_0^{P_2} - \mathbf{r}_0^{G_1}) \times \mathbf{T}_2$$

For Pendulum 2:
$$m_2 \ddot{x}_2 = -T_{2x}$$
$$m_2 \ddot{y}_2 = -T_{2y} - m_2 g$$
$$I_2 \ddot{\theta}_2 = -(\mathbf{r}_0^{G_2} - \mathbf{r}_0^{P_2}) \times (-\mathbf{T}_2) = R_2\sin\theta_2 T_{2y} + R_2\cos\theta_2 T_{2x}$$

### 3.3 Closed-Form Analytical Equations of Motion
Eliminating the four internal reaction force components ($T_{1x}, T_{1y}, T_{2x}, T_{2y}$) yields the coupled system for $[\ddot{\theta}_1, \ddot{\theta}_2]^T$:

$$\ddot{\theta}_1 = \frac{1}{D}\left[-\left(2 g m_1 R_1 (I_2 + m_2 R_2^2)\sin\theta_1 + L_1 m_2 g (2 I_2 + m_2 R_2^2)\sin\theta_1 + R_2\left(g m_2 R_2\sin(\theta_1 - 2\theta_2) + 2\left(\dot{\theta}_2^2 (I_2 + m_2 R_2^2) + \dot{\theta}_1^2 L_1 m_2 R_2\cos(\theta_1 - \theta_2)\right)\sin(\theta_1 - \theta_2)\right)\right)\right]$$

$$\ddot{\theta}_2 = \frac{1}{D}\left[m_2 R_2\left(-\left(g (2 I_1 + L_1^2 m_2 + 2 m_1 R_1^2)\sin\theta_2\right) + L_1\left(g m_1 R_1\sin\theta_2 + 2\dot{\theta}_1^2 (I_1 + L_1^2 m_2 + m_1 R_1^2)\sin(\theta_1 - \theta_2) + \dot{\theta}_2^2 L_1 m_2 R_2\sin(2(\theta_1 - \theta_2)) + g m_1 R_1\sin(2\theta_1 - \theta_2) + g L_1 m_2\sin(2\theta_1 - \theta_2)\right)\right)\right]$$

where the denominator determinant $D(\theta_1, \theta_2)$ is:
$$D = 2 I_2 L_1^2 m_2 + 2 I_2 m_1 R_1^2 + L_1^2 m_2^2 R_2^2 + 2 m_1 m_2 R_1^2 R_2^2 + 2 I_1 (I_2 + m_2 R_2^2) - L_1^2 m_2^2 R_2^2\cos(2(\theta_1 - \theta_2))$$

---

## 🔄 4. Annex: Generalization for Asymmetric Center of Mass ($\varphi \neq 0$)

When mass distribution is uneven across the longitudinal symmetry axis, the vector $\mathbf{P_1G_1}$ forms an offset angle $\varphi \neq 0$ with the line $\mathbf{P_1P_2}$:
$$\mathbf{P_1P_2} = L_1\sin(\theta_1 + \varphi)\,\mathbf{i} - L_1\cos(\theta_1 + \varphi)\,\mathbf{j}$$

The resulting equations of motion incorporate the constant phase shift $\varphi$:
$$\ddot{\theta}_1 = \frac{1}{D}\left[-\left(2 g m_1 R_1 (I_2 + m_2 R_2^2)\sin\theta_1 + L_1 m_2 g (2 I_2 + m_2 R_2^2)\sin(\theta_1 + \varphi) + R_2\left(g m_2 R_2\sin(\theta_1 - 2\theta_2 + \varphi) + 2\left(\dot{\theta}_2^2 (I_2 + m_2 R_2^2) + \dot{\theta}_1^2 L_1 m_2 R_2\cos(\theta_1 - \theta_2 + \varphi)\right)\sin(\theta_1 - \theta_2 + \varphi)\right)\right)\right]$$

$$\ddot{\theta}_2 = \frac{1}{D}\left[m_2 R_2\left(-\left(g (2 I_1 + L_1^2 m_2 + 2 m_1 R_1^2)\sin\theta_2\right) + L_1\left(g m_1 R_1\sin(\theta_2 - \varphi) + 2\dot{\theta}_1^2 (I_1 + L_1^2 m_2 + m_1 R_1^2)\sin(\theta_1 - \theta_2 + \varphi) + \dot{\theta}_2^2 L_1 m_2 R_2\sin(2(\theta_1 - \theta_2 + \varphi)) + g m_1 R_1\sin(2\theta_1 - \theta_2 + \varphi) + g L_1 m_2\sin(2\theta_1 - \theta_2 + 2\varphi)\right)\right)\right]$$

$$D = 2 I_2 L_1^2 m_2 + 2 I_2 m_1 R_1^2 + L_1^2 m_2^2 R_2^2 + 2 m_1 m_2 R_1^2 R_2^2 + 2 I_1 (I_2 + m_2 R_2^2) - L_1^2 m_2^2 R_2^2\cos(2(\theta_1 - \theta_2 + \varphi))$$

---

## ⚡ 5. Energy Analysis & Conservation

The total mechanical energy of the compound double pendulum is:
$$E = E_k + E_p$$

### Kinetic Energy (König's Theorem)
$$E_k = \frac{1}{2}m_1\|\mathbf{v}_0^{G_1}\|^2 + \frac{1}{2}I_1\dot{\theta}_1^2 + \frac{1}{2}m_2\|\mathbf{v}_0^{G_2}\|^2 + \frac{1}{2}I_2\dot{\theta}_2^2$$
Expanding using the velocity relations:
$$E_k = \frac{1}{2}\left(I_1 + m_1 R_1^2 + m_2 L_1^2\right)\dot{\theta}_1^2 + \frac{1}{2}\left(I_2 + m_2 R_2^2\right)\dot{\theta}_2^2 + m_2 L_1 R_2\dot{\theta}_1\dot{\theta}_2\cos(\theta_1 - \theta_2)$$

### Potential Energy
Taking $y = 0$ at pivot $P_1$:
$$E_p = m_1 g y_1 + m_2 g y_2 = -m_1 g R_1\cos\theta_1 - m_2 g\left(L_1\cos\theta_1 + R_2\cos\theta_2\right)$$

In frictionless simulation, $E(t) = \text{constant}$. Deviations quantify numerical drift of the ODE solver. In the experimental video data, $E(t)$ decays monotonically due to aerodynamic drag and pivot bearing friction.

---

## 🌀 6. Numerical Integration (`ode23s`) & Deterministic Chaos

The compound double pendulum is inherently **stiff** and **chaotic** at high energy levels.

### Why `ode23s`?
Standard non-stiff Runge-Kutta solvers (`ode45`) suffer severe time-step degradation or instability due to high frequency gyroscopic coupling and stiffness. MATLAB's modified Rosenbrock solver **`ode23s`** provides superior numerical stability and energy conservation.

### Sensitivity to Initial Conditions (Lyapunov Exponent Demonstration)
Consider release from rest:
* **Low-Energy Regime ($\theta_0 = 45^\circ$):**
  Compare $\theta_0 = 45^\circ$ vs $\theta_0 = 45^\circ + 10^{-10}\text{ rad}$. The trajectories remain nearly identical over tens of seconds (regular, quasi-periodic motion).
* **High-Energy Regime ($\theta_0 = 135^\circ$):**
  Compare $\theta_0 = 135^\circ$ vs $\theta_0 = 135^\circ + 10^{-10}\text{ rad}$. Within a few oscillation cycles ($t \sim 3\text{–}5\text{ s}$), the infinitesimal perturbation $\varepsilon = 10^{-10}\text{ rad}$ grows exponentially, leading to completely divergent trajectories—the hallmark of **deterministic chaos**.

---

## 📦 7. Deliverables & Required Scripts

* **`main_exp.m`**: Loads video data / marker coordinates, reconstructs $\theta_1(t), \theta_2(t)$, filters measurement noise, estimates velocities, and computes experimental energy decay.
* **`main_num.m`**: Integrates the theoretical ODEs with `ode23s`, generates phase portraits, compares with experimental trajectories, and evaluates the chaotic perturbation test ($\theta_0 = 45^\circ$ vs $135^\circ$).
