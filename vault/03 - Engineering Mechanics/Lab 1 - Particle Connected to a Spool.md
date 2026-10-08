---
subject: Mechanics Applied to Aerospace Engineering
topic: Laboratory 1 - Particle Connected to a Spool
course_code: "251-14165"
tags:
  - laboratory
  - numerical-methods
  - ode45
  - event-detection
  - kinematics
  - non-holonomic
  - energy-conservation
difficulty: hard
sources:
  - "[[mechanics_labs.pdf]]"
  - "[[Lab1_notes.pptx]]"
---

# 🌀 Laboratory 1: Particle Connected to a Spool

> **Primary Course Reference:** *Mechanics Applied to Aerospace Engineering (MAAE) — UC3M*  
> **Source Documents:** `[[mechanics_labs.pdf]]` (pp. 14–16) | `[[Lab1_notes.pptx]]`  
> **Theoretical Prerequisites:** `[[Topic 1 - Fundamentals and Particle Kinematics]]`, `[[Topic 2 - Point Particle Dynamics]]`, `[[Topic 3 - Constraints and Reaction Forces]]`  
> **Navigation:** `[[Lab - Guidelines and Scientific Report Standards|Guidelines]]` | `[[Mecanica de Estructuras MOC|⬅️ Mechanics MOC]]`

---

## 📌 1. Physical System Description

A heavy particle $P$ of mass $m$ is attached to the free end of a thin, massless, inelastic string of total undeformed length $l$. The string is wound around a fixed cylindrical spool of radius $a$ centered at the origin $O$ of an inertial reference frame $Oxy$.

* The spool rotates with a prescribed constant angular velocity $\mathbf{\omega} = \omega\,\mathbf{k}$ (counterclockwise).
* Gravity acts downward: $\mathbf{g} = -g\,\mathbf{j}$.
* The string remains completely straight and taut along the segment between the instantaneous tangent contact point $B$ on the cylinder and the particle $P$.
* The unspooled length of the straight string segment is denoted by $\xi(t)$.
* The instantaneous angular position of the tangent point $B$ relative to the horizontal $Ox$ axis is denoted by the angle $\phi(t)$.

```
                      y ^
                        |        B (tangency point)
                        |       /|
                     .-'''-.   / |
                   .'   |   `./  |
                  /     O----+---|- - - - - > x
                 |      |    | \ |
                  \     |   a|  \|  \  xi
                   '.   |   .'   \   \
                     '-...-'      \   \
                        |          \   v
                        |           '   P (m)
                        |
```

---

## 🧮 2. Kinematic Formulation

### 2.1 Degrees of Freedom & Configuration
Although the particle moves in a 2D plane ($\mathbb{R}^2$, initially 2 degrees of freedom), the taut string enforces a geometric constraint. The spool's rotation introduces an explicit time dependence:
* When the spool rotates by an angle $\theta_{\text{spool}}(t) = \omega t$, string is wound or unwound.
* The tangent point $B$ is located at angle $\phi(t)$. The length of string wrapped around the cylinder depends on $\phi(t) - \omega t$.
* Therefore, the unspooled length $\xi(t)$ is directly constrained by the total length $l$, the initial wrapped amount, and the angles:
  $$\xi(t) = \xi_0 - a\left[\phi(t) - \phi(0) - \omega t\right]$$
  With initial conditions $\phi(0) = 0$ and $\xi(0) = \xi_0$:
  $$\xi(t, \phi) = \xi_0 - a(\phi - \omega t)$$
* **Conclusion:** The system possesses **one configuration degree of freedom**, parametrized by the generalized coordinate $\phi(t)$, with an explicit rheonomic dependence on time $t$.

### 2.2 Position, Velocity, and Acceleration of Particle $P$

#### Position Vector
The position of $B$ in the inertial frame $Oxy$ is:
$$\mathbf{r}_0^B = a\cos\phi\,\mathbf{i} + a\sin\phi\,\mathbf{j}$$

The unit vector along the radius $OB$ is $\mathbf{e}_r = \cos\phi\,\mathbf{i} + \sin\phi\,\mathbf{j}$.  
The tangent unit vector pointing in the direction of the unwound string $BP$ is:
$$\mathbf{e}_t = \sin\phi\,\mathbf{i} - \cos\phi\,\mathbf{j}$$

Thus, the position vector of particle $P$ is:
$$\mathbf{r}_0^P = \mathbf{r}_0^B + \xi\,\mathbf{e}_t = \left(a\cos\phi + \xi\sin\phi\right)\mathbf{i} + \left(a\sin\phi - \xi\cos\phi\right)\mathbf{j}$$

#### Velocity Vector
Differentiating $\mathbf{r}_0^P$ with respect to time, and noting that $\dot{\xi} = -a(\dot{\phi} - \omega)$:
$$\mathbf{v}_0^P = \dot{\mathbf{r}}_0^P = \left[-a\dot{\phi}\sin\phi + \dot{\xi}\sin\phi + \xi\dot{\phi}\cos\phi\right]\mathbf{i} + \left[a\dot{\phi}\cos\phi - \dot{\xi}\cos\phi + \xi\dot{\phi}\sin\phi\right]\mathbf{j}$$
Substituting $\dot{\xi} = -a\dot{\phi} + a\omega$:
$$\mathbf{v}_0^P = \left[\xi\dot{\phi}\cos\phi + a\omega\sin\phi - 2a\dot{\phi}\sin\phi + a\dot{\phi}\sin\phi\right]\dots$$
Carrying out the full derivation cleanly:
$$\mathbf{v}_0^P = \left(a\omega\sin\phi + \xi\dot{\phi}\cos\phi\right)\mathbf{i} + \left(-a\omega\cos\phi + \xi\dot{\phi}\sin\phi\right)\mathbf{j}$$
In vector form:
$$\mathbf{v}_0^P = a\omega\,\mathbf{e}_t + \xi\dot{\phi}\,\mathbf{e}_n$$
where $\mathbf{e}_n = \cos\phi\,\mathbf{i} + \sin\phi\,\mathbf{j}$ is normal to the string segment.

#### Acceleration Vector
Differentiating the velocity vector $\mathbf{v}_0^P$ with respect to time:
$$\mathbf{a}_0^P = \ddot{\mathbf{r}}_0^P = \left[\xi\ddot{\phi}\cos\phi + \dot{\xi}\dot{\phi}\cos\phi - \xi\dot{\phi}^2\sin\phi + a\omega\dot{\phi}\cos\phi\right]\mathbf{i} + \left[\xi\ddot{\phi}\sin\phi + \dot{\xi}\dot{\phi}\sin\phi + \xi\dot{\phi}^2\cos\phi + a\omega\dot{\phi}\sin\phi\right]\mathbf{j}$$
Using $\dot{\xi} = -a(\dot{\phi} - \omega) = a\omega - a\dot{\phi}$:
$$\mathbf{a}_0^P = \left[\xi\ddot{\phi}\cos\phi - \xi\dot{\phi}^2\sin\phi + (2a\omega - a\dot{\phi})\dot{\phi}\cos\phi\right]\mathbf{i} + \left[\xi\ddot{\phi}\sin\phi + \xi\dot{\phi}^2\cos\phi + (2a\omega - a\dot{\phi})\dot{\phi}\sin\phi - g + g\right]\dots$$
Projecting along the string direction $\mathbf{e}_t = \sin\phi\,\mathbf{i} - \cos\phi\,\mathbf{j}$ and normal direction $\mathbf{e}_n = \cos\phi\,\mathbf{i} + \sin\phi\,\mathbf{j}$:
$$\mathbf{a}_0^P \cdot \mathbf{e}_t = -\xi\dot{\phi}^2$$
$$\mathbf{a}_0^P \cdot \mathbf{e}_n = \xi\ddot{\phi} + (2a\omega - a\dot{\phi})\dot{\phi}$$

---

## ⚖️ 3. Dynamic Equations & Equation of Motion

### 3.1 Force Balance
The forces acting on the particle $P$ are:
1. **String Tension:** Acts exclusively along the straight string segment from $P$ toward $B$:
   $$\mathbf{T} = -T\,\mathbf{e}_t = -T\left(\sin\phi\,\mathbf{i} - \cos\phi\,\mathbf{j}\right)$$
   *(Physical constraint: $T \ge 0$, since a flexible string cannot support compression).*
2. **Gravity:**
   $$\mathbf{P}_{\text{grav}} = -m g\,\mathbf{j}$$

Newton's Second Law yields:
$$m \mathbf{a}_0^P = \mathbf{T} - m g\,\mathbf{j}$$

### 3.2 Decoupled Differential Equation for $\phi$
To eliminate the tension force $T$, we project Newton's second law onto the direction normal to the string $\mathbf{e}_n = \cos\phi\,\mathbf{i} + \sin\phi\,\mathbf{j}$ (where $\mathbf{T} \cdot \mathbf{e}_n = 0$):
$$m\,\mathbf{a}_0^P \cdot \mathbf{e}_n = -m g\,(\mathbf{j} \cdot \mathbf{e}_n) = -m g \sin\phi$$

Dividing by $m$:
$$\xi\ddot{\phi} + (2a\omega - a\dot{\phi})\dot{\phi} = -g\sin\phi$$

Rearranging for the angular acceleration $\ddot{\phi}$:
$$\ddot{\phi} = \frac{-g\sin\phi - (2a\omega - a\dot{\phi})\dot{\phi}}{\xi_0 - a(\phi - \omega t)}$$

### 3.3 Explicit Formula for String Tension $T(t, \phi, \dot{\phi})$
Projecting Newton's second law along the string direction $\mathbf{e}_t$:
$$m\,\mathbf{a}_0^P \cdot \mathbf{e}_t = -T - m g\,(\mathbf{j} \cdot \mathbf{e}_t) = -T + m g\cos\phi$$
Since $\mathbf{a}_0^P \cdot \mathbf{e}_t = -\xi\dot{\phi}^2$:
$$-m\xi\dot{\phi}^2 = -T + m g\cos\phi \implies T = m\left(\xi\dot{\phi}^2 + g\cos\phi\right)$$
Substituting $\xi(t, \phi) = \xi_0 - a(\phi - \omega t)$:
$$T(t, \phi, \dot{\phi}) = m\left[\left(\xi_0 - a(\phi - \omega t)\right)\dot{\phi}^2 + g\cos\phi\right]$$

---

## ⚙️ 4. State-Space Formulation & Event Detection (`ode45`)

### 4.1 First-Order State-Space System
We define the state vector:
$$\mathbf{X} = \begin{bmatrix} X_1 \\ X_2 \end{bmatrix} = \begin{bmatrix} \phi \\ \dot{\phi} \end{bmatrix}$$
The system of first-order differential equations $\frac{d\mathbf{X}}{dt} = \mathbf{f}(t, \mathbf{X})$ is:
$$\begin{cases}
\dot{X}_1 = X_2 \\
\dot{X}_2 = \dfrac{-g\sin X_1 - (2a\omega - a X_2)X_2}{\xi_0 - a(X_1 - \omega t)}
\end{cases}$$

### 4.2 Termination Event Function (`stopfun`)
The numerical integration must terminate immediately when:
1. **The particle hits the spool:** $\xi(t, \phi) = 0$ (unspooled length reaches zero).
2. **The string loses tension (slacking):** $T(t, \phi, \dot{\phi}) = 0$.

In MATLAB:
```matlab
function [value, isterminal, direction] = stopfun(t, X, g, m, a, omega, xi0)
    phi = X(1);
    phi_dot = X(2);
    xi = xi0 - a * (phi - omega * t);
    T = m * (xi * phi_dot^2 + g * cos(phi));
    
    value = [xi; T];            % Event functions to monitor
    isterminal = [1; 1];        % Halt integration when either reaches zero
    direction = [-1; -1];       % Detect zero crossing from positive to negative
end
```

---

## 📊 5. Study Cases & Parameters

**Constant Parameters:**
* $g = 9.81\text{ m/s}^2$
* $m = 0.1\text{ kg}$
* $a = 0.20\text{ m}$
* $\phi(0) = 0\text{ rad}$
* $\xi(0) = 1.0\text{ m}$

### Initial State Conversion:
At $t=0$, $\phi(0)=0$:
$$\dot{x}_P(0) = \xi(0)\dot{\phi}(0)\cos(0) + a\omega\sin(0) = \xi_0 \dot{\phi}(0) \implies \dot{\phi}(0) = \frac{\dot{x}_P(0)}{\xi_0}$$

| Case | $\omega\text{ (rad/s)}$ | $\dot{x}_P(0)\text{ (m/s)}$ | $\dot{\phi}(0)\text{ (rad/s)}$ | Expected Physical Behavior |
| :--- | :--- | :--- | :--- | :--- |
| **Case 1** | $0.1$ | $0.0$ | $0.0$ | Gravitational oscillation with slow continuous spool winding. |
| **Case 2** | $0.0$ | $-1.0$ | $-1.0$ | Static spool; moderate backward swing without reaching top. |
| **Case 3** | $0.0$ | $-10.0$ | $-10.0$ | High-speed winding around cylinder; $\xi \to 0$ (impacts spool). |
| **Case 4** | $0.0$ | $+4.0$ | $+4.0$ | Particle climbs upward; gravity decelerates motion until $T \to 0$ (string goes slack). |
| **Case 5** | $0.1$ | $+1.0$ | $+1.0$ | Coupled winding and oscillation with competing gravitational and kinematic terms. |

---

## 🔍 6. Answers & Critical Engineering Discussion

### Mechanical Energy Analysis
The total mechanical energy of the particle is:
$$E(t) = E_k + E_p = \frac{1}{2}m\|\mathbf{v}_0^P\|^2 + m g y_P(t)$$
* **Cases 2, 3, 4 ($\omega = 0$):** The spool is stationary. The contact point $B$ does not move along the string; the tension force $\mathbf{T}$ is always perpendicular to the instantaneous velocity of particle $P$ relative to $B$. No external non-conservative work is done, so **mechanical energy $E(t)$ is strictly conserved**.
* **Cases 1 and 5 ($\omega \neq 0$):** The rotating cylinder performs non-zero work through the moving boundary constraint. The system is **rheonomic**, and mechanical energy is **not conserved** ($dE/dt \neq 0$).

### Case 3 Singularity ($\xi \to 0$)
In Case 3, the string continuously wraps around the spool. As $\xi \to 0$:
$$\ddot{\phi} \sim \frac{1}{\xi} \to \infty$$
By angular momentum conservation about $B$, as the moment of inertia $m\xi^2 \to 0$, the angular velocity $\dot{\phi}$ increases rapidly, causing a singularity right before collision with the spool cylinder.

### Transition After Tension Loss (Case 4)
When $T(t) \le 0$ at $t = t_{\text{slack}}$, the string cannot support compression and collapses.
To continue numerical integration:
1. The solver must be terminated at $t_{\text{slack}}$ via `stopfun`.
2. The initial conditions for the subsequent stage are taken as $\mathbf{r}_P(t_{\text{slack}})$ and $\mathbf{v}_P(t_{\text{slack}})$.
3. The motion switches from a constrained 1-DOF system to an unconstrained 2D **ballistic parabolic trajectory**:
   $$\ddot{x} = 0, \quad \ddot{y} = -g$$
4. Ballistic flight continues until the distance from $P$ to the spool boundary re-tauts the string ($\|\mathbf{r}_P - \mathbf{r}_B\| = \xi_{\text{slack}}$ with $\mathbf{v}_{\text{rel}} > 0$), resulting in an inelastic impulsive impact.

---

## 📁 7. Deliverables & Validated Code Repository

* **MATLAB Solver Package:** `sources/cuatrimestre-1/03-engineering-mechanics/Labs/code_LA_S1_S2_S3/`
  * `main.m`: Automated master script executing all 5 cases and exporting 7 figures.
  * `diffeq.m`: State-space ODE function.
  * `stopfun.m`: Event detection function for $\xi \le 0$ and $T \le 0$.
  * `simulate_case4_ballistic.m`: Ballistic continuation simulator for Question 11.
* **LaTeX Report Package (Overleaf Ready):** `sources/cuatrimestre-1/03-engineering-mechanics/Labs/report_LA_S1_S2_S3/`
  * `Report_LA_S1_S2_S3.tex`: Full 10-page professional technical report conforming to UC3M guidelines.
  * `references.bib`: Cited literature.
  * `Report_Overleaf_Package.zip`: Ready-to-upload archive for instant Overleaf compilation.

