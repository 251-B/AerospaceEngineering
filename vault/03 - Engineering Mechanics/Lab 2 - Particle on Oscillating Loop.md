---
subject: Mechanics Applied to Aerospace Engineering
topic: Laboratory 2 - Particle on Oscillating Loop
course_code: "251-14165"
tags:
  - laboratory
  - non-inertial-frame
  - rotating-reference-frame
  - coriolis-force
  - centrifugal-force
  - phase-portrait
  - linearization
difficulty: hard
sources:
  - "[[mechanics_labs.pdf]]"
---

# 🔄 Laboratory 2: Particle on Oscillating Loop

> **Primary Course Reference:** *Mechanics Applied to Aerospace Engineering (MAAE) — UC3M*  
> **Source Document:** [[mechanics_labs.pdf]] (pp. 17–19)  
> **Theoretical Prerequisites:** [[Topic 1 - Fundamentals and Particle Kinematics]], [[Topic 2 - Point Particle Dynamics]], [[Topic 3 - Constraints and Reaction Forces]]  
> **Navigation:** [[Lab - Guidelines and Scientific Report Standards|Guidelines]] | [[Mecanica de Estructuras MOC|⬅️ Mechanics MOC]]

---

## 📌 1. Physical System Description

A heavy point particle $P$ of mass $m$ slides without friction along a rigid circular wire (loop) of center $C$ and radius $R$.

* The wire loop is contained in a plane $Oxy$ that rotates about the vertical axis $Oy$ with a prescribed time-dependent angular velocity:
  $$\mathbf{\Omega}(t) = \Omega(t)\,\mathbf{j} = A\omega\sin(\omega t)\,\mathbf{j}$$
  where $A$ and $\omega$ are known positive constants.
* The position of the particle on the circular wire is parametrized by the angle $\phi(t)$ measured from the horizontal $Ox$ axis to the radius vector $\mathbf{CP}$.
* Gravity acts vertically downward: $\mathbf{g} = -g\,\mathbf{j}$.
* We define a rotating reference frame $Oxyz$ rigidly attached to the wire loop plane, with $\mathbf{j}$ pointing vertically upward, $\mathbf{i}$ lying in the loop plane along the horizontal diameter, and $\mathbf{k} = \mathbf{i} \times \mathbf{j}$ perpendicular to the loop plane.
* A stationary (inertial) reference frame is denoted by $Ox_1y_1z_1$, coinciding with $Oxyz$ at $t = 0$.

```
                        y ^  \Omega(t) = A\omega\sin(\omega t) j
                          |  |
                          | /_)
                       .-'''-.
                     .'   |   `.
                    /     |     \ P (m)
                   |      C------*------> x
                    \     |    / |
                     '.   |  R/  | \phi
                       '-.|-''---'
                          |
                          v g
```

---

## 🧭 2. Kinematics in Non-Inertial & Inertial Frames

### 2.1 Position and Relative Motion
The position vector of particle $P$ relative to the rotating frame origin $O$ (assuming center $C$ is at $(R, 0, 0)$ or $(0,0,0)$—in standard UC3M geometry, center $C$ is along the $x$-axis or at origin; here $\mathbf{CP} = R\cos\phi\,\mathbf{i} + R\sin\phi\,\mathbf{j}$):
$$\mathbf{r}_O^P = \mathbf{r}_O^C + \mathbf{CP} = R\cos\phi\,\mathbf{i} + R\sin\phi\,\mathbf{j}$$

The relative velocity observed in the rotating frame $\mathcal{F}_{\text{rot}} = \{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$ is:
$$\mathbf{v}_{\text{rel}} = \left(\frac{d\mathbf{r}_O^P}{dt}\right)_{\mathcal{F}_{\text{rot}}} = -R\dot{\phi}\sin\phi\,\mathbf{i} + R\dot{\phi}\cos\phi\,\mathbf{j} = R\dot{\phi}\,\mathbf{e}_\phi$$
where $\mathbf{e}_r = \cos\phi\,\mathbf{i} + \sin\phi\,\mathbf{j}$ and $\mathbf{e}_\phi = -\sin\phi\,\mathbf{i} + \cos\phi\,\mathbf{j}$.

The relative acceleration in $\mathcal{F}_{\text{rot}}$ is:
$$\mathbf{a}_{\text{rel}} = -R\left(\ddot{\phi}\sin\phi + \dot{\phi}^2\cos\phi\right)\mathbf{i} + R\left(\ddot{\phi}\cos\phi - \dot{\phi}^2\sin\phi\right)\mathbf{j} = -R\dot{\phi}^2\,\mathbf{e}_r + R\ddot{\phi}\,\mathbf{e}_\phi$$

### 2.2 Transport & Coriolis Accelerations
The angular velocity and angular acceleration of the rotating frame relative to the inertial frame are:
$$\mathbf{\Omega}(t) = A\omega\sin(\omega t)\,\mathbf{j}$$
$$\dot{\mathbf{\Omega}}(t) = A\omega^2\cos(\omega t)\,\mathbf{j}$$

1. **Transport Acceleration $\mathbf{a}_{\text{trans}}$:**
   $$\mathbf{a}_{\text{trans}} = \dot{\mathbf{\Omega}} \times \mathbf{r}_O^P + \mathbf{\Omega} \times (\mathbf{\Omega} \times \mathbf{r}_O^P)$$
   $$\dot{\mathbf{\Omega}} \times \mathbf{r}_O^P = \left(A\omega^2\cos(\omega t)\,\mathbf{j}\right) \times (R\cos\phi\,\mathbf{i} + R\sin\phi\,\mathbf{j}) = -R A\omega^2\cos(\omega t)\cos\phi\,\mathbf{k}$$
   $$\mathbf{\Omega} \times (\mathbf{\Omega} \times \mathbf{r}_O^P) = -\Omega^2(t)\,(R\cos\phi)\,\mathbf{i} = -R A^2\omega^2\sin^2(\omega t)\cos\phi\,\mathbf{i}$$

2. **Coriolis Acceleration $\mathbf{a}_{\text{Cor}}$:**
   $$\mathbf{a}_{\text{Cor}} = 2\,\mathbf{\Omega} \times \mathbf{v}_{\text{rel}} = 2\left(A\omega\sin(\omega t)\,\mathbf{j}\right) \times \left(-R\dot{\phi}\sin\phi\,\mathbf{i} + R\dot{\phi}\cos\phi\,\mathbf{j}\right) = 2 R A\omega\dot{\phi}\sin(\omega t)\sin\phi\,\mathbf{k}$$

Total absolute acceleration in the inertial frame:
$$\mathbf{a}_{\text{abs}} = \mathbf{a}_{\text{rel}} + \mathbf{a}_{\text{trans}} + \mathbf{a}_{\text{Cor}}$$

---

## ⚖️ 3. Dynamics in the Rotating Frame

### 3.1 Forces and Fictitious Forces
In the non-inertial rotating frame, the equation of motion is:
$$m \mathbf{a}_{\text{rel}} = \mathbf{F}_{\text{real}} + \mathbf{F}_{\text{iner}}$$
where:
* **Real Forces:**
  * Gravity: $\mathbf{P}_{\text{grav}} = -m g\,\mathbf{j}$
  * Wire Reaction: Since the wire is smooth (frictionless), the reaction force $\mathbf{N}$ has no component along the tangent direction $\mathbf{e}_\phi$:
    $$\mathbf{N} = N_r\,\mathbf{e}_r + N_z\,\mathbf{k} = N_r(\cos\phi\,\mathbf{i} + \sin\phi\,\mathbf{j}) + N_z\,\mathbf{k}$$
* **Inertia (Fictitious) Forces:**
  * Centrifugal Force: $\mathbf{F}_{\text{cent}} = -m\,\mathbf{\Omega} \times (\mathbf{\Omega} \times \mathbf{r}_O^P) = m R A^2\omega^2\sin^2(\omega t)\cos\phi\,\mathbf{i}$
  * Euler Force: $\mathbf{F}_{\text{Euler}} = -m\dot{\mathbf{\Omega}} \times \mathbf{r}_O^P = m R A\omega^2\cos(\omega t)\cos\phi\,\mathbf{k}$
  * Coriolis Force: $\mathbf{F}_{\text{Cor}} = -m\mathbf{a}_{\text{Cor}} = -2m R A\omega\dot{\phi}\sin(\omega t)\sin\phi\,\mathbf{k}$

### 3.2 Equation of Motion for $\phi(t)$
Projecting the dynamic balance onto the tangent direction $\mathbf{e}_\phi = -\sin\phi\,\mathbf{i} + \cos\phi\,\mathbf{j}$ eliminates the reaction force components ($N_r, N_z$):
$$m\,\mathbf{a}_{\text{rel}} \cdot \mathbf{e}_\phi = (\mathbf{P}_{\text{grav}} + \mathbf{F}_{\text{cent}}) \cdot \mathbf{e}_\phi$$
$$m R \ddot{\phi} = -m g\cos\phi - m R A^2\omega^2\sin^2(\omega t)\cos\phi\sin\phi$$
Dividing by $m R$:
$$\ddot{\phi} = -\frac{g}{R}\cos\phi - \frac{1}{2}A^2\omega^2\sin^2(\omega t)\sin(2\phi)$$

### 3.3 Reaction Force Components
Projecting onto $\mathbf{e}_r$ and $\mathbf{k}$:
* **Radial Reaction $N_r$:**
  $$-m R \dot{\phi}^2 = N_r - m g\sin\phi + m R A^2\omega^2\sin^2(\omega t)\cos^2\phi$$
  $$N_r(t) = -m R \dot{\phi}^2 + m g\sin\phi - m R A^2\omega^2\sin^2(\omega t)\cos^2\phi$$
* **Transverse (Out-of-Plane) Reaction $N_z$:**
  $$0 = N_z + (\mathbf{F}_{\text{Euler}} + \mathbf{F}_{\text{Cor}}) \cdot \mathbf{k}$$
  $$N_z(t) = -m R A\omega\left[\omega\cos(\omega t)\cos\phi - 2\dot{\phi}\sin(\omega t)\sin\phi\right]$$

---

## 📈 4. Numerical Analysis & Study Questions

### 4.1 State-Space Implementation for `ode45`
State vector $\mathbf{X} = [\phi, \dot{\phi}]^T$:
$$\begin{cases}
\dot{X}_1 = X_2 \\
\dot{X}_2 = -\dfrac{g}{R}\cos X_1 - \dfrac{1}{2}A^2\omega^2\sin^2(\omega t)\sin(2 X_1)
\end{cases}$$

**Nominal Simulation Parameters:**
* $A = \pi$
* $g = 9.81\text{ m/s}^2$
* $m = 1.0\text{ kg}$
* $R = 1.0\text{ m}$
* $\omega = 0.1\text{ rad/s}$
* Period $T = \frac{2\pi}{\omega} = 20\pi \approx 62.83\text{ s}$
* Integration interval: $t \in [0, 3T] \approx [0, 188.5\text{ s}]$
* Initial conditions: $\phi(0) = 0$, $\dot{\phi}(0) = 0$.

### 4.2 Autonomous Case ($A = 0$) & Phase Portrait Analysis
When $A = 0$, the frame is stationary ($\Omega = 0$). The equation reduces to the classical vertical pendulum:
$$\ddot{\phi} + \frac{g}{R}\cos\phi = 0$$
Stable equilibrium is at the bottom of the loop: $\phi_{\text{eq}} = -\pi/2$ (or $3\pi/2$).  
The total mechanical energy is conserved:
$$E = \frac{1}{2}m R^2\dot{\phi}^2 + m g R\sin\phi = \text{constant}$$

* **Condition for Continuous Circulation (steady increase of $\phi$):**
  The particle can cross the highest point $\phi = \pi/2$ if and only if the mechanical energy exceeds the potential energy at the crest:
  $$E > E_p(\pi/2) = +m g R$$
  $$\frac{1}{2}m R^2\dot{\phi}(0)^2 + m g R\sin\phi(0) > m g R \implies \dot{\phi}(0) > \sqrt{\frac{2g}{R}\left(1 - \sin\phi(0)\right)}$$

### 4.3 Linearization for Small Oscillations
For $A^2 \ll g / (R\omega^2)$ and $\phi(t) = \delta(t) - \pi/2$ with $|\delta| \ll 1$:
$$\cos(\delta - \pi/2) = \sin\delta \approx \delta$$
$$\sin(2(\delta - \pi/2)) = -\sin(2\delta) \approx -2\delta$$
The linearized equation becomes a Mathieu-type parametric oscillator:
$$\ddot{\delta} + \left[\frac{g}{R} - A^2\omega^2\sin^2(\omega t)\right]\delta = 0$$
Integrating this linearized equation against the full nonlinear ODE demonstrates the limits of perturbation validity as a function of the drive frequency $\omega$.
