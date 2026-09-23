---
subject: Mechanics Applied to Aerospace Engineering
topic: 2 - Point Particle Dynamics
course_code: "251-14165"
tags:
  - theory
  - dynamics
  - point-particle
  - newton-laws
  - energy-conservation
  - stability
  - simple-pendulum
difficulty: medium-high
prerequisites:
  - "Topic 1 - Fundamentals and Particle Kinematics"
  - "Calculus I & II"
  - "Linear Algebra"
  - "Physics I"
---

# 🚀 Topic 2: Point Particle Dynamics

> **Core Foundational Result:**
> $$ \mathbf{F} = \left.\frac{d\mathbf{p}_0}{dt}\right|_0 = m_P\mathbf{a}_0^P, \quad \frac{dT_0}{dt} = P = \mathbf{F}\cdot\mathbf{v}_0^P, \quad \frac{dE_0}{dt} = \mathbf{F}_N\cdot\mathbf{v}_0^P $$
> *While kinematics investigates the geometric description of motion without considering its causes, dynamics analyzes the physical forces producing that motion. Newton's second law governs the trajectory in an inertial reference frame, the work-energy theorem establishes that only forces with a tangential component alter particle speed, and mechanical energy conservation provides a powerful first integral of motion to map allowed regions, turning points, and stability.*

---

## 🧭 1. Introduction: Mechanical Quantities in Dynamics

In Newtonian particle dynamics, a point particle $P$ is characterized by an intrinsic, invariant scalar physical property: its **inertial mass $m_P$** $[kg]$. 

### 1.1 Fundamental Dynamic Quantities (Slide 3)
Observed from an inertial reference frame $S_0 = \{O; \mathcal{B}_0\}$:

1. **Linear Momentum (Quantity of Motion) $\mathbf{p}_0$:**
   $$ \mathbf{p}_0 = m_P\,\mathbf{v}_0^P \quad [\text{kg}\cdot\text{m/s}] $$
   A vector quantity possessing the identical direction and sense as the instantaneous velocity $\mathbf{v}_0^P$.
2. **Kinetic Energy $T_0$:**
   $$ T_0 = \frac{1}{2}m_P\,\|\mathbf{v}_0^P\|^2 = \frac{1}{2}m_P\,v_0^2 \ge 0 \quad [\text{J} = \text{kg}\cdot\text{m}^2/\text{s}^2] $$
   A non-negative scalar quantity proportional to the square of the speed $v_0$.
   
*Note on Reference Frame Dependence:* Both $\mathbf{p}_0$ and $T_0$ depend strictly on the observer's frame $S_0$. Changing reference frames alters $\mathbf{v}_0^P$, and thus alters linear momentum and kinetic energy.

---

## ⚖️ 2. Newton's Three Laws of Motion (Slides 4–6)

Newtonian mechanics is founded upon three empirical axioms formulated by Sir Isaac Newton (1687):

### 2.1 First Law (Principle of Inertia)
> *"A particle shall continue in its state of rest or of uniform rectilinear motion unless acted upon by a non-zero resultant external force."*

* **Mathematical Expression:** If $\sum \mathbf{F} = \mathbf{0}$, then:
  $$ \mathbf{p}_0 = \text{constant} \iff \mathbf{v}_0^P = \text{constant} \iff \mathbf{a}_0^P = \mathbf{0} $$
* **Inertial Reference Frame Definition:** The first law serves fundamentally as the definition of an **inertial reference frame**: a frame of reference in which a particle free from all physical interactions moves with zero acceleration.

### 2.2 Second Law (Fundamental Law of Dynamics)
> *"The time rate of change of linear momentum of a particle measured in an inertial frame is directly proportional to, and in the direction of, the resultant force acting upon it."*

$$ \mathbf{F} = \left.\frac{d\mathbf{p}_0}{dt}\right|_0 $$
Assuming the particle mass $m_P$ is constant over time ($\dot{m}_P = 0$):
$$ \mathbf{F} = \left.\frac{d}{dt}(m_P\,\mathbf{v}_0^P)\right|_0 = m_P\left.\frac{d\mathbf{v}_0^P}{dt}\right|_0 = m_P\,\mathbf{a}_0^P $$
where $\mathbf{F} = \sum_{i} \mathbf{F}_i$ denotes the net vector resultant of all forces acting upon $P$.

### 2.3 Third Law (Action-Reaction Principle)
> *"To every action there is always an equal and opposite reaction: the mutual interactions between two particles are always equal in magnitude, opposite in direction, and collinear along their line of centers."*

If particle $P$ exerts a force $\mathbf{F}_{QP}$ on particle $Q$, then particle $Q$ exerts a force $\mathbf{F}_{PQ}$ on particle $P$ such that:
$$ \mathbf{F}_{PQ} = -\mathbf{F}_{QP}, \quad \text{collinear with } (\mathbf{r}^Q - \mathbf{r}^P) $$

---

## 🌐 3. Systems of Particles and Momentum Conservation (Slides 7–8)

Consider an ensemble of $N$ interacting point particles $\{P_1, P_2, \dots, P_N\}$. The total force acting on particle $i$ decomposes into:
$$ \mathbf{F}_i = \mathbf{F}_i^{\text{ext}} + \sum_{j \neq i} \mathbf{F}_{ij}^{\text{int}} $$
where $\mathbf{F}_i^{\text{ext}}$ is the resultant external force applied by the environment, and $\mathbf{F}_{ij}^{\text{int}}$ is the internal interaction force exerted by particle $j$ on particle $i$.

### 3.1 Total Linear Momentum
The total linear momentum of the system is the vector sum:
$$ \mathbf{p}_{\text{tot}} = \sum_{i=1}^N \mathbf{p}_i = \sum_{i=1}^N m_i\,\mathbf{v}_0^{P_i} $$
Differentiating with respect to time:
$$ \left.\frac{d\mathbf{p}_{\text{tot}}}{dt}\right|_0 = \sum_{i=1}^N \mathbf{F}_i = \sum_{i=1}^N \mathbf{F}_i^{\text{ext}} + \sum_{i=1}^N \sum_{j \neq i} \mathbf{F}_{ij}^{\text{int}} $$
By Newton's third law, the internal forces cancel pairwise: $\mathbf{F}_{ij}^{\text{int}} + \mathbf{F}_{ji}^{\text{int}} = \mathbf{0}$. Therefore:
$$ \left.\frac{d\mathbf{p}_{\text{tot}}}{dt}\right|_0 = \mathbf{F}^{\text{ext}} = \sum_{i=1}^N \mathbf{F}_i^{\text{ext}} $$

### 3.2 Principle of Conservation of Total Linear Momentum
> **Conservation Theorem:** If the resultant external force acting on a system vanishes ($\mathbf{F}^{\text{ext}} = \mathbf{0}$), the total linear momentum is strictly conserved:
> $$ \mathbf{p}_{\text{tot}} = \text{constant vector} $$
In an isolated two-particle system ($P$ and $Q$):
$$ \mathbf{p}_0^P(t) + \mathbf{p}_0^Q(t) = \mathbf{p}_0^P(0) + \mathbf{p}_0^Q(0) = \text{constant} $$

---

## 📐 4. Equations of Motion and Trajectory Integration (Slides 9–12)

The second law $\mathbf{F} = m_P\,\mathbf{a}_0^P$ is a single vector differential equation in 3D Euclidean space.

### 4.1 Projection onto Vector Bases (Slide 9)
Projecting onto three linearly independent unit basis vectors yields three scalar second-order ordinary differential equations (ODEs). In Cartesian coordinates:
$$ \begin{cases}
m_P\,\ddot{x}(t) = F_x(t, x, y, z, \dot{x}, \dot{y}, \dot{z}) \\
m_P\,\ddot{y}(t) = F_y(t, x, y, z, \dot{x}, \dot{y}, \dot{z}) \\
m_P\,\ddot{z}(t) = F_z(t, x, y, z, \dot{x}, \dot{y}, \dot{z})
\end{cases} $$

### 4.2 State-Space Form and Initial Value Problem (Slide 10)
Equivalently, the 3 second-order ODEs can be formulated as a system of **6 first-order ODEs**:
$$ \begin{cases}
\dot{x} = v_x, & \dot{v}_x = \frac{1}{m_P}F_x \\
\dot{y} = v_y, & \dot{v}_y = \frac{1}{m_P}F_y \\
\dot{z} = v_z, & \dot{v}_z = \frac{1}{m_P}F_z
\end{cases} $$
Integrating this system yields the trajectory $\mathbf{r}_0^P(t)$ governed by **6 arbitrary integration constants**. These constants are uniquely fixed by the initial state at $t = 0$:
$$ \text{Initial Conditions:} \quad \mathbf{r}_0^P(0) = [x_0, y_0, z_0]^T, \quad \mathbf{v}_0^P(0) = [\dot{x}_0, \dot{y}_0, \dot{z}_0]^T $$

### 4.3 Slide Benchmark Examples (Explicit Calculus & Chain Rule)

* **Direct Integration (Slide 11):** Free motion of $m_P = 1\text{ kg}$ under gravity $\mathbf{F} = -m_P g\,\mathbf{j}_0$ ($g=10\text{ m/s}^2$) with initial conditions $\mathbf{r}_0^P(0) = \mathbf{0}$, $\dot{x}(0) = 2\text{ m/s}$, $\dot{y}(0) = 5\text{ m/s}$.
  
  *Horizontal Motion ($x$-axis):*
  $$ m_P\,\ddot{x}(t) = 0 \implies \ddot{x}(t) = \frac{d\dot{x}}{dt} = 0 $$
  Integrating over time from $0$ to $t$ using the Fundamental Theorem of Calculus:
  $$ \int_0^t \frac{d\dot{x}}{dt'}\,dt' = \int_0^t 0\,dt' \implies [\dot{x}(t')]_0^t = 0 \implies \dot{x}(t) - \dot{x}(0) = 0 \implies \dot{x}(t) = \dot{x}(0) = 2\text{ m/s} $$
  Integrating velocity $\dot{x}(t) = \frac{dx}{dt} = 2$ over time from $0$ to $t$:
  $$ \int_0^t \frac{dx}{dt'}\,dt' = \int_0^t 2\,dt' \implies [x(t')]_0^t = [2t']_0^t \implies x(t) - x(0) = 2t - 0 \implies x(t) = 2t $$

  *Vertical Motion ($y$-axis):*
  $$ m_P\,\ddot{y}(t) = -m_P g \implies \ddot{y}(t) = \frac{d\dot{y}}{dt} = -10\text{ m/s}^2 $$
  Integrating acceleration over time from $0$ to $t$:
  $$ \int_0^t \frac{d\dot{y}}{dt'}\,dt' = \int_0^t (-10)\,dt' \implies [\dot{y}(t')]_0^t = [-10t']_0^t \implies \dot{y}(t) - \dot{y}(0) = -10t \implies \dot{y}(t) = 5 - 10t $$
  Integrating vertical velocity $\dot{y}(t) = \frac{dy}{dt} = 5 - 10t$:
  $$ \int_0^t \frac{dy}{dt'}\,dt' = \int_0^t (5 - 10t')\,dt' \implies [y(t')]_0^t = \left[ 5t' - 10\frac{(t')^2}{2} \right]_0^t \implies y(t) - y(0) = 5t - 5t^2 \implies y(t) = 5t - 5t^2 $$

  *Trajectory Equation (Eliminating parameter $t$):*
  From $x(t) = 2t \implies t(x) = \frac{x}{2}$. Substituting into $y(t)$:
  $$ y(x) = 5\left(\frac{x}{2}\right) - 5\left(\frac{x}{2}\right)^2 = \frac{5}{2}x - \frac{5}{4}x^2 $$

* **Inverse Dynamics (Slide 12):** What force $\mathbf{F}(t)$ is required for $m_P = 2\text{ kg}$ to follow $\mathbf{v}_0^P(t) = 2at^2\,\mathbf{i}_0 + e^{bt}\,\mathbf{j}_0$?
  
  Applying Newton's second law $\mathbf{F} = m_P\,\mathbf{a}_0^P = m_P\,\frac{d\mathbf{v}_0^P}{dt}$, we differentiate each vector component:
  1. For the $x$-component, applying the power rule of differentiation:
     $$ \frac{d}{dt}\left(2at^2\,\mathbf{i}_0\right) = 2a\left(\frac{d(t^2)}{dt}\right)\mathbf{i}_0 = 2a(2t)\,\mathbf{i}_0 = 4at\,\mathbf{i}_0 $$
  2. For the $y$-component, applying the **chain rule** with substitution $u(t) = bt \implies \frac{du}{dt} = b$:
     $$ \frac{d}{dt}\left(e^{bt}\,\mathbf{j}_0\right) = \left(\frac{d(e^u)}{du}\frac{du}{dt}\right)\mathbf{j}_0 = \left(e^u \cdot b\right)\mathbf{j}_0 = b\,e^{bt}\,\mathbf{j}_0 $$
  Multiplying by particle mass $m_P = 2\text{ kg}$:
  $$ \mathbf{F}(t) = 2\left(4at\,\mathbf{i}_0 + b\,e^{bt}\,\mathbf{j}_0\right) = 8at\,\mathbf{i}_0 + 2b\,e^{bt}\,\mathbf{j}_0 $$

---

## ⚡ 5. Power, Work, and the Kinetic Energy Theorem (Slide 13)

### 5.1 Instantaneous Power
The power $P$ exerted by a force $\mathbf{F}$ acting on particle $P$ at velocity $\mathbf{v}_0^P$ is:
$$ P = \mathbf{F} \cdot \mathbf{v}_0^P \quad [\text{W} = \text{J/s}] $$

### 5.2 Kinetic Energy Theorem (Work-Energy Principle)
Differentiating kinetic energy $T_0 = \frac{1}{2}m_P\,(\mathbf{v}_0^P \cdot \mathbf{v}_0^P)$ with respect to time:
$$ \frac{dT_0}{dt} = \frac{1}{2}m_P\left( \frac{d\mathbf{v}_0^P}{dt}\cdot\mathbf{v}_0^P + \mathbf{v}_0^P\cdot\frac{d\mathbf{v}_0^P}{dt} \right) = m_P\,\mathbf{a}_0^P \cdot \mathbf{v}_0^P $$
Substituting Newton's second law $m_P\mathbf{a}_0^P = \mathbf{F}$:
$$ \frac{dT_0}{dt} = \mathbf{F} \cdot \mathbf{v}_0^P = P $$

### 5.3 Work Done by a Force
Integrating the power over the time interval $[t_1, t_2]$:
$$ W_{12} = \int_{t_1}^{t_2} P\,dt = \int_{t_1}^{t_2} (\mathbf{F}\cdot\mathbf{v}_0^P)\,dt = \int_{\mathbf{r}_1}^{\mathbf{r}_2} \mathbf{F} \cdot d\mathbf{r} = \Delta T_0 = T_{0,2} - T_{0,1} $$

> [!IMPORTANT]
> **Cardinal Geometric Property:**
> Because $P = \mathbf{F}\cdot\mathbf{v}_0^P = F_t\,v_0$, **a force exerts power and performs work if and only if it possesses a non-zero tangential component ($F_t \neq 0$)**. Forces acting purely normal to the trajectory (such as tension in inextensible strings, normal support reactions on smooth frictionless surfaces, or the magnetic Lorentz force $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$) perform **identically zero work** ($W \equiv 0$).

---

## 🏔️ 6. Conservative Forces and Potential Energy (Slides 14–16)

In general, the line integral $W_{12} = \int_{\Gamma} \mathbf{F}\cdot d\mathbf{r}$ depends on the specific path $\Gamma$ connecting $\mathbf{r}_1$ and $\mathbf{r}_2$.

### 6.1 Definition of a Conservative Force
A force $\mathbf{F}$ is **conservative** if the work it performs between any two points is **strictly path-independent**:
$$ \int_{\Gamma_A} \mathbf{F}\cdot d\mathbf{r} = \int_{\Gamma_B} \mathbf{F}\cdot d\mathbf{r} \iff \oint_{\mathcal{C}} \mathbf{F}\cdot d\mathbf{r} = 0 \quad \text{for any closed loop } \mathcal{C} $$

### 6.2 Potential Energy Function $V_0(\mathbf{r})$
When path-independence holds, fixing a reference point $\mathbf{r}_*$, we define the **potential energy function** $V_0(\mathbf{r})$:
$$ V_0(\mathbf{r}) = -\int_{\mathbf{r}_*}^{\mathbf{r}} \mathbf{F} \cdot d\mathbf{r}' $$
The work done by a conservative force is the negative variation of potential energy:
$$ W_{12} = \int_{\mathbf{r}_1}^{\mathbf{r}_2} \mathbf{F}\cdot d\mathbf{r} = -(V_0(\mathbf{r}_2) - V_0(\mathbf{r}_1)) = -\Delta V_0 $$
Taking the differential: $dW = \mathbf{F}\cdot d\mathbf{r} = -dV_0 = -\nabla V_0 \cdot d\mathbf{r}$, which establishes:
$$ \mathbf{F} = -\nabla V_0 = -\begin{bmatrix} \frac{\partial V_0}{\partial x} \\ \frac{\partial V_0}{\partial y} \\ \frac{\partial V_0}{\partial z} \end{bmatrix} $$

### 6.3 Mathematical Condition for Conservatism (Curl Test)
A continuously differentiable force field $\mathbf{F}(\mathbf{r})$ defined on a simply-connected domain is conservative **if and only if its curl vanishes identically**:
$$ \nabla \times \mathbf{F} = \mathbf{0} \iff \text{curl}(\mathbf{F}) = \mathbf{0} $$

### 6.4 Classical Aerospace Potential Functions:
1. **Uniform Gravitational Force $\mathbf{W} = -m_P g\,\mathbf{k}_0$:**
   $$ \nabla \times \mathbf{W} = \mathbf{0} \implies V_0(z) = m_P g z + C $$
2. **Linear Elastic Spring $\mathbf{F} = -k\,\mathbf{r}_0^P$:**
   $$ V_0(\mathbf{r}) = \frac{1}{2}k\,\|\mathbf{r}_0^P\|^2 = \frac{1}{2}k\,r^2 $$
3. **Inverse-Square Central Interactions (Gravity / Electrostatics):**
   $$ \mathbf{F} = -\frac{G M m_P}{r^2}\mathbf{e}_r \implies V_0(r) = -\frac{G M m_P}{r} $$

---

## 🔍 7. Analytical Polar/Cylindrical Force Tests (Slides 17–18)

In cylindrical coordinates $\{R, \theta, z\}$, the curl of a vector field is:
$$ \nabla \times \mathbf{F} = \left( \frac{1}{R}\frac{\partial F_z}{\partial \theta} - \frac{\partial F_\theta}{\partial z} \right)\mathbf{e}_R + \left( \frac{\partial F_R}{\partial z} - \frac{\partial F_z}{\partial R} \right)\mathbf{e}_\theta + \frac{1}{R}\left( \frac{\partial(R F_\theta)}{\partial R} - \frac{\partial F_R}{\partial \theta} \right)\mathbf{e}_z $$

### Example 1 (Slide 17): Radial Central Force $\mathbf{F} = aR\,\mathbf{e}_R$
* Components: $F_R = aR$, $F_\theta = 0$, $F_z = 0$.
* Evaluating curl:
  $$ (\nabla \times \mathbf{F})_z = \frac{1}{R}\left( \frac{\partial(0)}{\partial R} - \frac{\partial(aR)}{\partial \theta} \right) = 0 $$
  All curl components vanish: $\nabla \times \mathbf{F} = \mathbf{0}$. The force is **conservative**.
* Potential Energy:
  $$ \mathbf{F} = -\nabla V_0 = -\frac{\partial V_0}{\partial R}\mathbf{e}_R \implies \frac{\partial V_0}{\partial R} = -aR \implies V_0(R) = -\frac{1}{2}aR^2 + C $$

### Example 2 (Slide 18): Azimuthal Shear Force $\mathbf{F} = bR^2\,\mathbf{e}_\theta$
* Components: $F_R = 0$, $F_\theta = bR^2$, $F_z = 0$.
* Evaluating curl:
  $$ (\nabla \times \mathbf{F})_z = \frac{1}{R}\left( \frac{\partial(R \cdot bR^2)}{\partial R} - 0 \right) = \frac{1}{R}\frac{\partial(bR^3)}{\partial R} = \frac{1}{R}(3bR^2) = 3bR \neq 0 $$
  The curl does not vanish! Therefore, $\mathbf{F} = bR^2\,\mathbf{e}_\theta$ is **non-conservative** and no potential energy function exists.

---

## 🔋 8. Conservation of Mechanical Energy and 1D Energy Landscapes (Slides 19–20)

Let particle $P$ be subject to conservative forces $\mathbf{F}_C = -\nabla V_0$ and non-conservative forces $\mathbf{F}_N$:
$$ m_P\,\mathbf{a}_0^P = \mathbf{F}_C + \mathbf{F}_N = -\nabla V_0 + \mathbf{F}_N $$
Taking the scalar product with $\mathbf{v}_0^P$:
$$ m_P\mathbf{a}_0^P \cdot \mathbf{v}_0^P = \frac{dT_0}{dt} = (-\nabla V_0)\cdot\mathbf{v}_0^P + \mathbf{F}_N\cdot\mathbf{v}_0^P = -\frac{dV_0}{dt} + \mathbf{F}_N\cdot\mathbf{v}_0^P $$
Defining the **Total Mechanical Energy $E_0$**:
$$ E_0 = T_0 + V_0 $$
$$ \frac{dE_0}{dt} = \mathbf{F}_N \cdot \mathbf{v}_0^P $$

> **Energy Conservation Law:** If non-conservative forces are absent ($\mathbf{F}_N = \mathbf{0}$) or always perpendicular to the velocity ($\mathbf{F}_N \cdot \mathbf{v}_0^P = 0$), then:
> $$ E_0 = T_0 + V_0 = \text{constant} $$
> The conservation of mechanical energy constitutes a **first integral of motion**.

### 8.1 Qualitative Analysis in 1D Energy Diagrams (Slide 20)
In a 1D conservative system with potential $V_0(x)$:
$$ E_0 = \frac{1}{2}m_P\,v^2 + V_0(x) \implies T_0(x) = \frac{1}{2}m_P\,v^2 = E_0 - V_0(x) $$
Because kinetic energy is strictly non-negative ($T_0 \ge 0$):
1. **Allowed Regions:** Defined by $E_0 \ge V_0(x)$. The particle can only exist where the total energy exceeds or equals the potential energy.
2. **Forbidden Regions:** Defined by $E_0 < V_0(x)$. Real physical motion cannot penetrate these domains since that would imply imaginary velocities ($v^2 < 0$).
3. **Turning Points ($x_{\text{turn}}$):** Where $E_0 = V_0(x_{\text{turn}})$. At these boundary locations, $T_0 = 0 \implies v = 0$. The particle stops and reverses its direction of motion.
4. **Local Speed:** The instantaneous speed is directly proportional to the vertical gap:
   $$ v(x) = \sqrt{\frac{2(E_0 - V_0(x))}{m_P}} $$

### 8.2 Slide 15 Potential Example (Explicit Chain Rule)
Consider the potential function $V_0(x) = \cos(x) + \cos\left(\frac{x}{2} - \frac{\pi}{4}\right)$.
To find the 1D force $F(x) = -\frac{dV_0}{dx}$, we compute the derivative term by term:
1. First term: $\frac{d}{dx}[\cos(x)] = -\sin(x)$.
2. Second term: Applying the **chain rule of differentiation** with $u(x) = \frac{x}{2} - \frac{\pi}{4}$:
   $$ \frac{du}{dx} = \frac{d}{dx}\left(\frac{x}{2} - \frac{\pi}{4}\right) = \frac{1}{2} - 0 = \frac{1}{2} $$
   $$ \frac{d}{dx}\left[\cos\left(\frac{x}{2} - \frac{\pi}{4}\right)\right] = \frac{d(\cos u)}{du}\frac{du}{dx} = (-\sin u)\cdot\left(\frac{1}{2}\right) = -\frac{1}{2}\sin\left(\frac{x}{2} - \frac{\pi}{4}\right) $$
3. Combining and applying the leading negative sign:
   $$ F(x) = -\frac{dV_0}{dx} = -\left[ -\sin(x) - \frac{1}{2}\sin\left(\frac{x}{2} - \frac{\pi}{4}\right) \right] = \sin(x) + \frac{1}{2}\sin\left(\frac{x}{2} - \frac{\pi}{4}\right) $$
* The force always drives the particle "downhill" toward potential valleys.
* The steepness of the slope corresponds directly to the force magnitude.

---

## 🎯 9. Equilibrium Configurations and Stability Criteria (Slides 21–22)

### 9.1 Equilibrium Configuration
A position $\mathbf{r}_*$ is an **equilibrium configuration** if a particle placed at $\mathbf{r}_*$ with zero initial velocity remains permanently at rest:
$$ \mathbf{a}_0^P = \mathbf{0} \iff \sum \mathbf{F}(\mathbf{r}_*) = \mathbf{0} \iff \nabla V_0(\mathbf{r}_*) = \mathbf{0} $$
In 1D, equilibrium positions correspond to the **critical points** of the potential energy function:
$$ \left.\frac{dV_0}{dx}\right|_{x_*} = 0 $$

### 9.2 Formal Stability (Lyapunov Criterion)
An equilibrium configuration $x_*$ is **stable** if for every small neighborhood $\varepsilon_r, \varepsilon_v > 0$, there exist bounds $\delta_r, \delta_v > 0$ such that initial perturbations within $\delta$ remain bounded within $\varepsilon$ for all future time $t > 0$.

### 9.3 Second-Derivative Curvature Criterion in 1D
Expanding $V_0(x)$ in a Taylor series about equilibrium $x_*$:
$$ V_0(x) = V_0(x_*) + \underbrace{\left.\frac{dV_0}{dx}\right|_{x_*}}_{=0}(x - x_*) + \frac{1}{2}\left.\frac{d^2V_0}{dx^2}\right|_{x_*}(x - x_*)^2 + \mathcal{O}((x - x_*)^3) $$
$$ F(x) = -\frac{dV_0}{dx} \approx -\left.\frac{d^2V_0}{dx^2}\right|_{x_*}(x - x_*) $$
1. **Stable Equilibrium ($\frac{d^2V_0}{dx^2}\big|_{x_*} > 0$):**
   * Corresponds to a **local minimum** of $V_0(x)$ (potential well).
   * Restoring force acts back towards $x_*$: $F \approx -k(x - x_*)$.
2. **Unstable Equilibrium ($\frac{d^2V_0}{dx^2}\big|_{x_*} < 0$):**
   * Corresponds to a **local maximum** of $V_0(x)$ (potential hill).
   * Repulsive force pushes particle away from $x_*$: $F \approx +k(x - x_*)$.
3. **Neutral / Indeterminate Equilibrium ($\frac{d^2V_0}{dx^2}\big|_{x_*} = 0$):**
   * Higher-order derivatives must be evaluated.

---

## 🧮 10. Benchmark Case Study: The Simple Pendulum (Slide 23 & Notes Sec. 4.7)

> **Pedagogical Audit (`problem_step_mentor`):**  
> We solve the classical Simple Pendulum following the 4-phase methodology, citing `Notes.pdf` Section 4.7 and avoiding all algebraic omissions.

### Problem Statement
A point particle of mass $m$ is suspended from a fixed pivot $O$ by a massless, rigid, inextensible rod of length $\ell$, subject to uniform downward gravity $\mathbf{g} = -g\mathbf{j}_0$. Analyze its kinematics, dynamic force balance, energy conservation, equilibrium stability, and small-amplitude oscillation.

---

### Step 1: Coordinates, Basis, and Kinematic Constraints (Explicit Calculus)
* The motion is planar in $Oxy$. We adopt polar coordinates $\{R, \theta\}$ with local orthonormal basis $\{\mathbf{e}_R, \mathbf{e}_\theta\}$:
  $$ \mathbf{e}_R(\theta) = \cos\theta\,\mathbf{i}_0 + \sin\theta\,\mathbf{j}_0 $$
  $$ \mathbf{e}_\theta(\theta) = -\sin\theta\,\mathbf{i}_0 + \cos\theta\,\mathbf{j}_0 $$
* Differentiating the basis vectors with respect to time using the **chain rule** ($\frac{d}{dt} = \frac{d\theta}{dt}\frac{\partial}{\partial\theta} = \dot{\theta}\frac{\partial}{\partial\theta}$):
  $$ \frac{d\mathbf{e}_R}{dt} = \frac{\partial\mathbf{e}_R}{\partial\theta}\frac{d\theta}{dt} = \left(\frac{d(\cos\theta)}{d\theta}\mathbf{i}_0 + \frac{d(\sin\theta)}{d\theta}\mathbf{j}_0\right)\dot{\theta} = (-\sin\theta\,\mathbf{i}_0 + \cos\theta\,\mathbf{j}_0)\dot{\theta} = \dot{\theta}\,\mathbf{e}_\theta $$
  $$ \frac{d\mathbf{e}_\theta}{dt} = \frac{\partial\mathbf{e}_\theta}{\partial\theta}\frac{d\theta}{dt} = \left(-\frac{d(\sin\theta)}{d\theta}\mathbf{i}_0 + \frac{d(\cos\theta)}{d\theta}\mathbf{j}_0\right)\dot{\theta} = (-\cos\theta\,\mathbf{i}_0 - \sin\theta\,\mathbf{j}_0)\dot{\theta} = -\dot{\theta}\,\mathbf{e}_R $$
* The inextensibility of the rod establishes a holonomic constraint:
  $$ R(t) = \ell = \text{constant} \implies \dot{R} = 0, \quad \ddot{R} = 0 $$
* **Position Vector:**
  $$ \mathbf{r}_0^P = \ell\,\mathbf{e}_R $$
* **Velocity Vector (applying product rule):**
  $$ \mathbf{v}_0^P = \frac{d}{dt}(\ell\,\mathbf{e}_R) = \underbrace{\frac{d\ell}{dt}}_{=0}\mathbf{e}_R + \ell\frac{d\mathbf{e}_R}{dt} = \ell(\dot{\theta}\,\mathbf{e}_\theta) = \ell\dot{\theta}\,\mathbf{e}_\theta $$
* **Acceleration Vector (applying product rule and chain rule):**
  $$ \mathbf{a}_0^P = \frac{d}{dt}(\ell\dot{\theta}\,\mathbf{e}_\theta) = \ell\left( \frac{d\dot{\theta}}{dt}\mathbf{e}_\theta + \dot{\theta}\frac{d\mathbf{e}_\theta}{dt} \right) = \ell\left( \ddot{\theta}\,\mathbf{e}_\theta + \dot{\theta}(-\dot{\theta}\,\mathbf{e}_R) \right) = -\ell\dot{\theta}^2\,\mathbf{e}_R + \ell\ddot{\theta}\,\mathbf{e}_\theta $$

---

### Step 2: Dynamic Force Balance and Newton's Second Law
Forces acting on $P$:
1. **Weight $\mathbf{W}$:** Expressed in the fixed Cartesian basis as $\mathbf{W} = -mg\mathbf{j}_0$.
   Projecting onto the polar basis $\{\mathbf{e}_R, \mathbf{e}_\theta\}$:
   $$ \mathbf{W} = (\mathbf{W}\cdot\mathbf{e}_R)\mathbf{e}_R + (\mathbf{W}\cdot\mathbf{e}_\theta)\mathbf{e}_\theta = (-mg\mathbf{j}_0\cdot(\cos\theta\mathbf{i}_0+\sin\theta\mathbf{j}_0))\mathbf{e}_R + (-mg\mathbf{j}_0\cdot(-\sin\theta\mathbf{i}_0+\cos\theta\mathbf{j}_0))\mathbf{e}_\theta $$
   $$ \mathbf{W} = mg\cos\theta\,\mathbf{e}_R - mg\sin\theta\,\mathbf{e}_\theta $$
2. **Rod Tension $\mathbf{T}$:** Acts purely along the rod towards the pivot:
   $$ \mathbf{T} = -T\,\mathbf{e}_R $$

Applying Newton's second law: $m\mathbf{a}_0^P = \mathbf{W} + \mathbf{T}$:
$$ m(-\ell\dot{\theta}^2\,\mathbf{e}_R + \ell\ddot{\theta}\,\mathbf{e}_\theta) = (mg\cos\theta - T)\,\mathbf{e}_R - mg\sin\theta\,\mathbf{e}_\theta $$

Equating components along each orthogonal direction:
* **Radial Direction ($\mathbf{e}_R$):**
  $$ -m\ell\dot{\theta}^2 = mg\cos\theta - T \implies T(\theta, \dot{\theta}) = m(g\cos\theta + \ell\dot{\theta}^2) $$
* **Azimuthal Direction ($\mathbf{e}_\theta$):**
  $$ m\ell\ddot{\theta} = -mg\sin\theta \implies \ddot{\theta} + \frac{g}{\ell}\sin\theta = 0 $$

---

### Step 3: Mechanical Energy, Explicit Time Derivative, and First Integral
* **Kinetic Energy:**
  $$ T_0 = \frac{1}{2}m\,\|\mathbf{v}_0^P\|^2 = \frac{1}{2}m(\ell\dot{\theta})^2 = \frac{1}{2}m\ell^2\dot{\theta}^2 $$
* **Potential Energy:** Taking $V_0 = 0$ at the lowest position ($\theta = 0$):
  $$ V_0(\theta) = -mg\ell\cos\theta - (-mg\ell) = mg\ell(1 - \cos\theta) $$
* **Total Mechanical Energy:**
  $$ E_0 = T_0 + V_0 = \frac{1}{2}m\ell^2\dot{\theta}^2 + mg\ell(1 - \cos\theta) = \text{constant} $$
* **Proof of Conservation via Chain Rule:**
  Differentiating $E_0$ with respect to $t$:
  $$ \frac{dT_0}{dt} = \frac{d}{dt}\left(\frac{1}{2}m\ell^2\dot{\theta}^2\right) = \frac{1}{2}m\ell^2\left(\frac{d(\dot{\theta}^2)}{d\dot{\theta}}\frac{d\dot{\theta}}{dt}\right) = \frac{1}{2}m\ell^2(2\dot{\theta}\ddot{\theta}) = m\ell^2\dot{\theta}\ddot{\theta} $$
  $$ \frac{dV_0}{dt} = \frac{d}{dt}[mg\ell(1 - \cos\theta)] = mg\ell\left( \frac{d(1 - \cos\theta)}{d\theta}\frac{d\theta}{dt} \right) = mg\ell(\sin\theta)\dot{\theta} $$
  Summing both rates of change:
  $$ \frac{dE_0}{dt} = m\ell^2\dot{\theta}\ddot{\theta} + mg\ell\sin\theta\dot{\theta} = m\ell\dot{\theta}\left( \ell\ddot{\theta} + g\sin\theta \right) $$
  Because $\ell\ddot{\theta} + g\sin\theta = 0$ by Newton's second law, $\frac{dE_0}{dt} \equiv 0$ strictly!
* **First Integral of Motion:**
  Solving $E_0 = \frac{1}{2}m\ell^2\dot{\theta}^2 + mg\ell(1 - \cos\theta)$ for angular velocity $\dot{\theta}$:
  $$ \frac{1}{2}m\ell^2\dot{\theta}^2 = E_0 - mg\ell(1 - \cos\theta) \implies \dot{\theta} = \pm\sqrt{\frac{2}{m\ell^2}\left[ E_0 - mg\ell(1 - \cos\theta) \right]} $$
* **Turning Points:** Occur when $\dot{\theta} = 0 \implies \cos\theta_{\max} = 1 - \frac{E_0}{mg\ell}$.

---

### Step 4: Equilibrium Configurations and Taylor Linearization
* **Equilibrium Condition:**
  $$ \frac{dV_0}{d\theta} = mg\ell\sin\theta = 0 \implies \theta_* = 0, \pm\pi $$
* **Stability Evaluation (Second Derivative):**
  $$ \frac{d^2V_0}{d\theta^2} = \frac{d}{d\theta}(mg\ell\sin\theta) = mg\ell\cos\theta $$
  * At $\theta_* = 0$: $\frac{d^2V_0}{d\theta^2}\big|_0 = mg\ell\cos(0) = +mg\ell > 0 \implies$ **Stable equilibrium (hanging down).**
  * At $\theta_* = \pm\pi$: $\frac{d^2V_0}{d\theta^2}\big|_{\pm\pi} = -mg\ell < 0 \implies$ **Unstable equilibrium (inverted vertical).**
* **Small Angle Linearization ($\theta \ll 1$):**
  The Taylor series expansion of $\sin\theta$ about $\theta = 0$ is:
  $$ \sin\theta = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!}\theta^{2n+1} = \theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \dots = \theta - \frac{\theta^3}{6} + \mathcal{O}(\theta^5) $$
  For small angular displacements $|\theta| \ll 1\text{ rad}$ (e.g. $|\theta| < 10^\circ \approx 0.175\text{ rad}$), the cubic term satisfies $\frac{\theta^3}{6} \approx 0.00089 \ll \theta$, allowing us to retain only the linear leading term $\sin\theta \approx \theta$:
  $$ \ddot{\theta} + \frac{g}{\ell}\theta = 0 \iff \ddot{\theta} + \omega_0^2\theta = 0 $$
  This is the classical harmonic oscillator ODE. Its characteristic equation is $r^2 + \omega_0^2 = 0 \implies r = \pm i\omega_0$, yielding the general harmonic oscillation:
  $$ \theta(t) = \theta_{\max}\cos(\omega_0 t + \phi_0) $$
  with natural frequency and oscillation period:
  $$ \omega_0 = \sqrt{\frac{g}{\ell}} \quad [\text{rad/s}], \quad T_0 = \frac{2\pi}{\omega_0} = 2\pi\sqrt{\frac{\ell}{g}} \quad [\text{s}] $$
