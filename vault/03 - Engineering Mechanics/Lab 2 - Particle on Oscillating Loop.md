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
  - "sources/cuatrimestre-1/03-engineering-mechanics/laboratorios/general-instructions/mechanics_labs.pdf"
  - "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
  - "sources/cuatrimestre-1/03-engineering-mechanics/laboratorios/lab-2/Lab2_Hector/main.m"
---

# Laboratory 2: Particle on Oscillating Loop

> **Primary Course Reference:** *Mechanics Applied to Aerospace Engineering (MAAE) — UC3M*
> **Source Document:** [[Source - 03-engineering-mechanics - laboratorios - general-instructions - mechanics_labs (pdf)|mechanics_labs.pdf]] (pp. 17–19)
> **Same system as an official exercise:** Problem 34 of `Problems.pdf`, solved step by step in [[Solution Set - Topic 5 Relative Motion]] (statement in [[Problem Set - Topic 5 Relative Motion]]). The lab adds the numerical work (items 4 to 9); the equations below agree with that official key.
> **Theoretical Prerequisites:** [[Topic 5 - Relative Motion]], [[Concept - Inertia Forces and Dynamics in Non-Inertial Frames]], [[Concept - The Simple Pendulum Nonlinear Dynamics and Linearization]]
> **Navigation:** [[Lab - Guidelines and Scientific Report Standards|Guidelines]] | [[Engineering Mechanics MOC|Mechanics MOC]]

---

## 1. Physical System Description

A heavy point particle $P$ of mass $m$ slides without friction along a rigid circular wire of center $C$ and radius $R$.

* The wire lies in the plane $Oxy$, which rotates about the vertical axis $Oy$ with the prescribed angular velocity
  $$\mathbf{\Omega}(t) = \Omega(t)\,\mathbf{j} = A\omega\sin(\omega t)\,\mathbf{j}$$
  where $A$ and $\omega$ are known positive constants.
* **Geometry (from the figure):** the axis $Oy$ is tangent to the wire at $O$, and the center is $C = (R, 0)$, so $\overrightarrow{OC} = R\,\mathbf{i}$. The distance from $P$ to the axis is $x = R(1+\cos\phi)$.
* $\phi$ is the angle between $Ox$ and $\overrightarrow{CP}$. Gravity is $\mathbf{g} = -g\,\mathbf{j}$.
* The rotating frame $Oxyz$ is attached to the wire plane: $\mathbf{i}$ in the plane along the horizontal diameter, $\mathbf{j}$ vertical upward, $\mathbf{k} = \mathbf{i}\times\mathbf{j}$ normal to the plane. The inertial frame $Ox_1y_1z_1$ coincides with $Oxyz$ at $t=0$.
* Polar basis of the wire: $\mathbf{e}_r = \cos\phi\,\mathbf{i} + \sin\phi\,\mathbf{j}$, $\mathbf{e}_\phi = -\sin\phi\,\mathbf{i} + \cos\phi\,\mathbf{j}$.

The system has one configuration degree of freedom, $\phi$, and the configuration depends explicitly on time through the rotation of the plane.

---

## 2. Kinematics

### 2.1 Relative motion (frame $Oxyz$)

$$\mathbf{r} = R(1+\cos\phi)\,\mathbf{i} + R\sin\phi\,\mathbf{j}$$
$$\mathbf{v}_{\text{rel}} = -R\dot\phi\sin\phi\,\mathbf{i} + R\dot\phi\cos\phi\,\mathbf{j} = R\dot\phi\,\mathbf{e}_\phi$$
$$\mathbf{a}_{\text{rel}} = -R\left(\ddot\phi\sin\phi + \dot\phi^2\cos\phi\right)\mathbf{i} + R\left(\ddot\phi\cos\phi - \dot\phi^2\sin\phi\right)\mathbf{j} = R\ddot\phi\,\mathbf{e}_\phi - R\dot\phi^2\,\mathbf{e}_r$$

### 2.2 Motion of the frame and absolute kinematics

$$\mathbf{\Omega} = A\omega\sin(\omega t)\,\mathbf{j}, \qquad \dot{\mathbf{\Omega}} = A\omega^2\cos(\omega t)\,\mathbf{j}$$

With $\mathbf{j}\times\mathbf{i} = -\mathbf{k}$ and $\mathbf{j}\times\mathbf{k} = \mathbf{i}$:

| Term | Expression |
|---|---|
| $\mathbf{\Omega}\times\mathbf{r}$ | $-\Omega R(1+\cos\phi)\,\mathbf{k}$ |
| Euler, $\dot{\mathbf{\Omega}}\times\mathbf{r}$ | $-\dot\Omega R(1+\cos\phi)\,\mathbf{k}$ |
| Centripetal, $\mathbf{\Omega}\times(\mathbf{\Omega}\times\mathbf{r})$ | $-\Omega^2R(1+\cos\phi)\,\mathbf{i}$ |
| Coriolis, $2\mathbf{\Omega}\times\mathbf{v}_{\text{rel}}$ | $2\Omega R\dot\phi\sin\phi\,\mathbf{k}$ |

$$\mathbf{v} = \mathbf{v}_{\text{rel}} + \mathbf{\Omega}\times\mathbf{r}, \qquad \mathbf{a} = \mathbf{a}_{\text{rel}} + \dot{\mathbf{\Omega}}\times\mathbf{r} + \mathbf{\Omega}\times(\mathbf{\Omega}\times\mathbf{r}) + 2\mathbf{\Omega}\times\mathbf{v}_{\text{rel}}$$

### 2.3 Angle turned by the plane

With $\theta(0)=0$ and $\dot\theta = \Omega$ (substitution $u=\omega\tau$ and Barrow's rule):
$$\theta(t) = \int_0^t A\omega\sin(\omega\tau)\,d\tau = A\left[-\cos u\right]_0^{\omega t} = A\left(1-\cos\omega t\right)$$
The plane swings between $\theta=0$ and $\theta=2A$ (for $A=\pi$, one full turn at $t=T/2$, then back). Position in the fixed frame, with $\mathbf{i} = \cos\theta\,\mathbf{i}_1 - \sin\theta\,\mathbf{k}_1$:
$$x_1 = R(1+\cos\phi)\cos\theta, \qquad y_1 = R\sin\phi, \qquad z_1 = -R(1+\cos\phi)\sin\theta$$
Check: $d\mathbf{i}/dt = -\dot\theta\,\mathbf{k} = \mathbf{\Omega}\times\mathbf{i}$.

---

## 3. Dynamics in the Rotating Frame

### 3.1 Forces

In $Oxyz$ the balance is $m\mathbf{a}_{\text{rel}} = \mathbf{F}_{\text{real}} + \mathbf{F}_{\text{iner}}$.

* **Real forces:**
  * Weight: $\mathbf{W} = -mg\,\mathbf{j}$.
  * Wire reaction (smooth wire, no tangential component): $\mathbf{N} = N_r\,\mathbf{e}_r + N_z\,\mathbf{k}$.
* **Inertia forces:**
  * Centrifugal: $\mathbf{F}_{\text{cent}} = m\Omega^2R(1+\cos\phi)\,\mathbf{i} = mA^2\omega^2R\sin^2(\omega t)(1+\cos\phi)\,\mathbf{i}$
  * Euler: $\mathbf{F}_{\text{Euler}} = mA\omega^2R\cos(\omega t)(1+\cos\phi)\,\mathbf{k}$
  * Coriolis: $\mathbf{F}_{\text{Cor}} = -2mA\omega R\dot\phi\sin(\omega t)\sin\phi\,\mathbf{k}$

### 3.2 Equation of motion

The tangent $\mathbf{e}_\phi$ is the only direction free of the unknown reaction, and Euler and Coriolis (along $\mathbf{k}$) drop out. Projecting: $mR\ddot\phi = -mg\cos\phi - m\Omega^2R(1+\cos\phi)\sin\phi$, that is
$$\boxed{\ddot\phi + \frac{g}{R}\cos\phi + A^2\omega^2\sin^2(\omega t)\,(1+\cos\phi)\sin\phi = 0}$$

### 3.3 Reaction components

* **Along $\mathbf{e}_r$:** $-mR\dot\phi^2 = N_r - mg\sin\phi + m\Omega^2R(1+\cos\phi)\cos\phi$
  $$\boxed{N_r = mg\sin\phi - mA^2\omega^2R\sin^2(\omega t)(1+\cos\phi)\cos\phi - mR\dot\phi^2}$$
* **Along $\mathbf{k}$:** $0 = N_z + \mathbf{F}_{\text{Euler}}\cdot\mathbf{k} + \mathbf{F}_{\text{Cor}}\cdot\mathbf{k}$
  $$\boxed{N_z = 2mA\omega R\,\dot\phi\sin\phi\sin(\omega t) - mA\omega^2R(1+\cos\phi)\cos(\omega t)}$$

Both agree with the official key of Problem 34. $N_z$ is what the wire supplies to drag $P$ along with the swinging plane.

### 3.4 Energy

* $\mathbf{N}\cdot\mathbf{v}_{\text{rel}} = 0$, and Euler and Coriolis do no work (they are normal to the plane that contains $\mathbf{v}_{\text{rel}}$).
* The centrifugal potential $-\tfrac12 m\Omega(t)^2x^2$ depends explicitly on time, so the relative energy
  $$E_{\text{rel}} = \tfrac12 mR^2\dot\phi^2 + mgR\sin\phi - \tfrac12 m\Omega^2R^2(1+\cos\phi)^2$$
  satisfies $dE_{\text{rel}}/dt = -m\Omega\dot\Omega R^2(1+\cos\phi)^2 \neq 0$. It is conserved only if $\Omega$ is constant (in particular for $A=0$).
* In the fixed frame the reaction $N_z\,\mathbf{k}$ does work, because the wire moves: $\dfrac{d(E_k+E_p)}{dt} = -\Omega R(1+\cos\phi)\,N_z$, with $E_k = \tfrac12 m\left(R^2\dot\phi^2 + \Omega^2x^2\right)$ and $E_p = mgR\sin\phi$.

---

## 4. Numerical Analysis and Study Questions

Implementation: `sources/cuatrimestre-1/03-engineering-mechanics/laboratorios/lab-2/Lab2_Hector/main.m` (same style as the Lab 1 code; only `ode45` is used to integrate).

### 4.1 State-space form for `ode45`

State $\mathbf{X} = [\phi, \dot\phi]^T$ and $\Omega(t) = A\omega\sin(\omega t)$:
$$\begin{cases}
\dot X_1 = X_2 \\
\dot X_2 = -\dfrac{g}{R}\cos X_1 - \Omega(t)^2\,(1+\cos X_1)\sin X_1
\end{cases}$$

**Nominal parameters (item 5):** $A=\pi$, $g=9.81\ \text{m/s}^2$, $m=1\ \text{kg}$, $R=1\ \text{m}$, $\omega=0.1\ \text{rad/s}$, $\phi(0)=0$, $\dot\phi(0)=0$. Period $T = 2\pi/\omega = 62.83\ \text{s}$, integration interval $[0, 3T]$, with $A\omega = 0.314\ \text{rad/s}$.

Results of the run with MATLAB R2026b (not compared with an official numerical key):

* $\phi \in [-\pi, 0.012]$: starting from $\phi=0$ at rest the bead swings about the bottom $\phi=-\pi/2$.
* $N_r \in [-29.43, 0]\ \text{N}$; the minimum is $-3mg$ at the bottom, where $\dot\phi^2 = 2g/R$.
* $N_z \in [-2.76, 2.77]\ \text{N}$.
* $E_k + E_p$ (absolute kinetic energy) varies between $-0.08$ and $0.31\ \text{J}$: it is not conserved, as in section 3.4.

### 4.2 Autonomous case ($A = 0$) and phase portrait (item 7)

With $A=0$ the plane is fixed and the equation is the vertical pendulum
$$\ddot\phi + \frac{g}{R}\cos\phi = 0$$
Stable equilibrium at $\phi=-\pi/2$, unstable at $\phi=+\pi/2$. The energy is conserved:
$$E = \tfrac12 mR^2\dot\phi^2 + mgR\sin\phi$$

**Condition for steady growth of $\phi$.** The bead must cross the top $\phi=\pi/2$, where $E_p = mgR$ is maximum:
$$\tfrac12 mR^2\dot\phi_0^2 + mgR\sin\phi_0 > mgR \implies \boxed{|\dot\phi_0| > \sqrt{\frac{2g}{R}\left(1-\sin\phi_0\right)}}$$
Equality is the separatrix $\dot\phi = \pm\sqrt{(2g/R)(1-\sin\phi)}$ (the top is approached but never reached in finite time); below it, $\phi$ oscillates between two values.

For the nine initial conditions of the lab ($g/R = 9.81\ \text{s}^{-2}$):

| $\phi(0)$ | critical $\dot\phi(0)$ | $\dot\phi(0)=0$ | $\dot\phi(0)=1.5$ | $\dot\phi(0)=3$ |
|---|---|---|---|---|
| $0$ | $4.43$ | oscillates | oscillates | oscillates |
| $\pi/4$ | $2.40$ | oscillates | oscillates | **increases** |
| $\pi/2$ | $0$ | unstable equilibrium | **increases** | **increases** |

At $(\pi/2, 0)$ the bead stays at rest analytically; numerically $\cos(\pi/2)\approx 6\cdot10^{-17}$, so it drifts away very slowly.

### 4.3 Linearization for small oscillations (item 8)

For $A^2\omega^2 \ll g/R$ and $\phi = \delta - \pi/2$ with $|\delta|\ll1$: $\cos\phi \approx \delta$, $\sin\phi \approx -1$, $1+\cos\phi \approx 1+\delta$. Keeping first order and dropping $A^2\omega^2\sin^2(\omega t)\,\delta$ against $(g/R)\,\delta$:
$$\boxed{\ddot\delta + \frac{g}{R}\,\delta = A^2\omega^2\sin^2(\omega t) = \frac{A^2\omega^2}{2}\left[1-\cos(2\omega t)\right]}$$
This is a **forced linear oscillator** (not a parametric one) with natural frequency $\omega_n=\sqrt{g/R}$. For $2\omega\neq\omega_n$:
$$\delta(t) = \frac{A^2R\omega^2}{2g} - \frac{A^2\omega^2\cos(2\omega t)}{2\left(\omega_n^2-4\omega^2\right)} + a\cos\omega_nt + b\sin\omega_nt$$
The bead oscillates about $\delta_0 = A^2R\omega^2/(2g)$. The approximation fails at **resonance**, $2\omega\approx\omega_n$, i.e. $\omega\approx\tfrac12\sqrt{g/R}$, where $\delta_p = -\dfrac{A^2\omega^2}{4\omega_n}\,t\sin(\omega_nt)$ grows linearly.

**Numerical comparison** (script settings: $R=0.01\ \text{m}$, $A=0.1$, $\delta(0)=0.01$, $\dot\delta(0)=0$, $t\in[0,10]\ \text{s}$; the lab statement gives no initial conditions, so these are a choice). Percentage error $100\,|\delta_{\text{lin}}-\delta_{\text{full}}|/\max|\delta_{\text{full}}|$ (normalised by the amplitude because $\delta$ crosses zero):

| $\omega$ | $\max\lvert\delta\rvert$ | error at $t=5\ \text{s}$ | maximum error |
|---|---|---|---|
| $\sqrt{g/R}$ | 0.0100 | 4.96 % | 14.2 % |
| $\tfrac12\sqrt{g/R}$ | **0.194** | 2.73 % | **27.7 %** |
| $\tfrac14\sqrt{g/R}$ | 0.0108 | 1.28 % | 4.85 % |

Two error mechanisms: a **phase drift** from the dropped term $\Omega^2\delta$ (it shifts the natural frequency, and grows with $\omega$), and, in the resonant case, $\delta$ growing until $\delta\ll1$ no longer holds.

### 4.4 Points for the critical discussion (item 9)

* The wire is a bilateral constraint: the bead cannot leave it, so there is no stop event, unlike Lab 1.
* Euler and Coriolis forces do not enter the equation of $\phi$; they only load the wire through $N_z$.
* The energy is not conserved while $\Omega(t)$ varies; it is for $A=0$, which the phase portrait shows.
* The linearization is valid while $\delta$ stays small; it fails by phase drift at large $\omega$ and by resonance at $\omega\approx\tfrac12\sqrt{g/R}$.
