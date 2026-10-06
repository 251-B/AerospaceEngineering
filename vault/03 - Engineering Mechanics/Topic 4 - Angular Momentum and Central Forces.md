---
title: "Topic 4: Angular Momentum and Central Forces (Kepler's Problem)"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
ground_truth: "slides/04_-_Angular_momentum.pdf & teoria/Notes.pdf (Chapters 4.8 & 8)"
tier: "Theory Master Guide"
language: "English"
---

# 🌀 Topic 4: Angular Momentum, Central Forces & Kepler's Problem

## 📌 Syllabus & Pedagogical Map
This comprehensive master guide provides the complete theoretical, mathematical, and physical development of **Angular Momentum, Central Force Fields, and Kepler's Problem** in classical aerospace mechanics. The content matches 100% of **`slides/04_-_Angular_momentum.pdf`** (Slides 1–17) and Chapters 4.8 (pp. 49–52) & 8 (pp. 71–75) of **`teoria/Notes.pdf`**.

* [[Concept - Angular Momentum Vector and Torque of Forces|Angular Momentum Vector & Torque of Forces]]
* [[Concept - Differential Equation of Angular Momentum with Moving Origins|Differential Equation with Moving Origins]]
* [[Concept - Conservation Laws and Planar Character of Central Force Fields|Conservation Laws & Planar Central Motion]]
* [[Concept - Kepler Laws and Barycentric Two-Body Reduction|Kepler's Laws & Barycentric Two-Body Reduction]]
* [[Concept - Binet Equation and Conic Section Trajectories|Binet Equation & Conic Section Trajectories]]
* [[Concept - Vis-Viva Energy Integral and Orbital Velocities|Vis-Viva Equation & Orbital Speeds]]
* [[Formula Sheet - Topic 4 Angular Momentum|Formula Sheet: Topic 4 Angular Momentum]]
* [[Problems - Topic 4 Angular Momentum and Central Forces|Official Problem Statements]]
* [[Solutions - Topic 4 Angular Momentum and Central Forces|Full Analytical Solutions]]

---

## 🧭 1. Angular Momentum and Torque (Slide 3, Notes 4.8)

### 1.1 Physical Definition of Angular Momentum
In linear particle dynamics, the primary vector quantity is linear momentum $\mathbf{p}_0 = m\mathbf{v}_0^P$. In rotational mechanics about a reference point $A$, the fundamental quantity is the **moment of momentum**, termed the **angular momentum vector** (Slide 3 & Notes Eq. 4.48).

Given a point particle $P$ of mass $m^P$ moving in an inertial reference frame $S_0: \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ with velocity $\mathbf{v}_0^P$, the angular momentum of $P$ about an arbitrary reference point $A$ (which may be stationary or moving) as observed from $S_0$ is defined as:
$$ \mathbf{H}_{A0}^P = \mathbf{AP} \times \mathbf{p}_0^P = \left(\mathbf{r}_0^P - \mathbf{r}_0^A\right) \times m^P \mathbf{v}_0^P $$

#### Key Properties:
1. **Vector Nature:** $\mathbf{H}_{A0}^P$ is an axial (pseudo-)vector perpendicular to both the relative position vector $\mathbf{r}_A^P = \mathbf{AP}$ and the velocity vector $\mathbf{v}_0^P$:
   $$ \mathbf{H}_{A0}^P \cdot \mathbf{AP} = 0, \qquad \mathbf{H}_{A0}^P \cdot \mathbf{v}_0^P = 0 $$
2. **Point Dependence:** The value of $\mathbf{H}_{A0}^P$ depends explicitly on the chosen base point $A$. If we translate the moment center to another point $B$:
   $$ \mathbf{H}_{B0}^P = \mathbf{BP} \times m\mathbf{v}_0^P = (\mathbf{BA} + \mathbf{AP}) \times m\mathbf{v}_0^P = \mathbf{H}_{A0}^P + \mathbf{BA} \times m\mathbf{v}_0^P $$
3. **Reference Frame Dependence:** The velocity $\mathbf{v}_0^P$ is evaluated relative to the observer's frame $S_0$.
4. **Dimensions and SI Units:**
   $$ [\mathbf{H}_{A0}^P] = [M][L]^2[T]^{-1} \implies \text{kg}\cdot\text{m}^2/\text{s} = \text{J}\cdot\text{s} $$

### 1.2 Torque (Moment of a Force)
The moment of an impressed resultant force $\mathbf{F}$ acting on particle $P$ about the reference point $A$ is termed **torque** $\mathbf{M}_A$ (Slide 3 & Notes Eq. 4.51):
$$ \mathbf{M}_A = \mathbf{AP} \times \mathbf{F} = \left(\mathbf{r}_0^P - \mathbf{r}_0^A\right) \times \mathbf{F} $$

* **Dimensions and SI Units:**
  $$ [\mathbf{M}_A] = [M][L]^2[T]^{-2} \implies \text{N}\cdot\text{m} $$
* **Line of Action Invariance:** Because sliding vectors can be translated along their line of action without altering their physical moment:
  $$ \mathbf{AP} \times \mathbf{F} = (\mathbf{AP}_\parallel + \mathbf{AP}_\perp) \times \mathbf{F} = \mathbf{AP}_\perp \times \mathbf{F} $$
  where $|\mathbf{AP}_\perp| = d$ is the lever arm (perpendicular distance from $A$ to the line of action of $\mathbf{F}$).

### 1.3 Action-Reaction Principle for Torques
Consider two interacting particles $P$ and $Q$. By Newton's Third Law, the internal force exerted by $Q$ on $P$, $\mathbf{F}^{P}$, and that by $P$ on $Q$, $\mathbf{F}^{Q}$, satisfy:
$$ \mathbf{F}^Q = -\mathbf{F}^P $$
Furthermore, in classical central interactions, internal forces are collinear along the line connecting $P$ and $Q$ ($\mathbf{F}^P \parallel \mathbf{PQ}$), so that $\mathbf{PQ} \times \mathbf{F}^P = \mathbf{0}$.

Taking torques about an arbitrary base point $A$:
$$ \mathbf{M}_A^P + \mathbf{M}_A^Q = \mathbf{AP} \times \mathbf{F}^P + \mathbf{AQ} \times \mathbf{F}^Q = \mathbf{AP} \times \mathbf{F}^P - \mathbf{AQ} \times \mathbf{F}^P = (\mathbf{AP} - \mathbf{AQ}) \times \mathbf{F}^P = \mathbf{QP} \times \mathbf{F}^P = \mathbf{0} $$
Thus, internal torques between interacting particles always cancel pairwise:
$$ \mathbf{M}_A^{\text{internal}} \equiv \mathbf{0} $$

---

## ⚙️ 2. Differential Evolution Equation for Angular Momentum (Slide 4, Notes 4.8)

### 2.1 General Derivation with an Arbitrary Moving Origin $A$
We take the time derivative of $\mathbf{H}_{A0}^P$ with respect to the inertial frame $S_0$:
$$ \frac{d\mathbf{H}_{A0}^P}{dt}\Bigg|_0 = \frac{d}{dt}\left[ (\mathbf{r}_0^P - \mathbf{r}_0^A) \times m^P \mathbf{v}_0^P \right]_0 $$

Applying the product rule for vector differentiation:
$$ \frac{d\mathbf{H}_{A0}^P}{dt}\Bigg|_0 = \left(\frac{d\mathbf{r}_0^P}{dt}\Bigg|_0 - \frac{d\mathbf{r}_0^A}{dt}\Bigg|_0\right) \times m^P \mathbf{v}_0^P + (\mathbf{r}_0^P - \mathbf{r}_0^A) \times m^P \frac{d\mathbf{v}_0^P}{dt}\Bigg|_0 $$

Recognizing kinematic terms:
1. $\frac{d\mathbf{r}_0^P}{dt}\big|_0 = \mathbf{v}_0^P$
2. $\frac{d\mathbf{r}_0^A}{dt}\big|_0 = \mathbf{v}_0^A$
3. $\frac{d\mathbf{v}_0^P}{dt}\big|_0 = \mathbf{a}_0^P$
4. By Newton's Second Law: $m^P \mathbf{a}_0^P = \mathbf{F}$
5. By definition of torque: $(\mathbf{r}_0^P - \mathbf{r}_0^A) \times \mathbf{F} = \mathbf{AP} \times \mathbf{F} = \mathbf{M}_A$

Substituting these relations:
$$ \frac{d\mathbf{H}_{A0}^P}{dt}\Bigg|_0 = (\mathbf{v}_0^P - \mathbf{v}_0^A) \times m^P \mathbf{v}_0^P + \mathbf{M}_A $$

Expanding the first vector cross product:
$$ (\mathbf{v}_0^P - \mathbf{v}_0^A) \times m^P \mathbf{v}_0^P = \underbrace{m^P(\mathbf{v}_0^P \times \mathbf{v}_0^P)}_{\mathbf{0}} - \mathbf{v}_0^A \times m^P \mathbf{v}_0^P = -\mathbf{v}_0^A \times m^P \mathbf{v}_0^P $$

We obtain the **fundamental differential equation of angular momentum for an arbitrary point $A$** (Slide 4 & Notes Eq. 4.52):
$$ \frac{d\mathbf{H}_{A0}^P}{dt}\Bigg|_0 = \mathbf{M}_A - \mathbf{v}_0^A \times m^P \mathbf{v}_0^P $$

### 2.2 Important Simplifications
The transport term $-\mathbf{v}_0^A \times m^P \mathbf{v}_0^P$ vanishes under two critical conditions:
1. **$A$ is a Fixed Point in $S_0$ ($\mathbf{v}_0^A = \mathbf{0}$):**
   $$ \frac{d\mathbf{H}_{A0}^P}{dt}\Bigg|_0 = \mathbf{M}_A $$
   *Interpretation:* The rate of change of angular momentum about a fixed point equals the net external torque about that point. This is the rotational analogue of Newton's Second Law ($\dot{\mathbf{p}}_0 = \mathbf{F}$).
2. **$A$ Moves Parallel to Particle $P$ ($\mathbf{v}_0^A \parallel \mathbf{v}_0^P$):**
   $$ \mathbf{v}_0^A \times \mathbf{v}_0^P = \mathbf{0} \implies \frac{d\mathbf{H}_{A0}^P}{dt}\Bigg|_0 = \mathbf{M}_A $$

> [!NOTE] Pedagogical Traceability Note (Slide 4)
> This differential equation is derived strictly from Newton's Second Law. It does not introduce independent physical laws beyond Newtonian mechanics, but provides first integrals of motion that simplify integration.

### 2.3 Non-Rotating Translating Reference Frame $S_A$ (Notes Eq. 4.54–4.55)
If we define an auxiliary translating frame $S_A: \{A; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ centered at moving point $A$ without rotation ($\boldsymbol{\omega}_{A0} = \mathbf{0}$):
* Relative velocity: $\mathbf{v}_0^P = \mathbf{v}_0^A + \mathbf{v}_A^P$
* Relative acceleration: $\mathbf{a}_0^P = \mathbf{a}_0^A + \mathbf{a}_A^P$

If point $A$ translates at **constant velocity** ($\mathbf{a}_0^A = \mathbf{0}$), $S_A$ is an inertial reference frame, and the relative angular momentum $\mathbf{H}_{AA} = \mathbf{AP} \times m\mathbf{v}_A^P$ obeys:
$$ \frac{d\mathbf{H}_{AA}}{dt}\Bigg|_A = \mathbf{M}_A $$

---

## ⚖️ 3. Conservation Laws of Angular Momentum (Slide 5, Notes 4.8)

### 3.1 Conservation for a Single Particle
If the net torque about a fixed point $A$ vanishes at all times:
$$ \mathbf{M}_A = \mathbf{0} \implies \frac{d\mathbf{H}_{A0}^P}{dt}\Bigg|_0 = \mathbf{0} \implies \mathbf{H}_{A0}^P = \text{constant vector} $$

Because this is a vector equation in 3D Euclidean space, it provides **three independent scalar conservation laws**:
$$ \begin{cases} H_{Ax} = m(y\dot{z} - z\dot{y}) = C_1 \\ H_{Ay} = m(z\dot{x} - x\dot{z}) = C_2 \\ H_{Az} = m(x\dot{y} - y\dot{x}) = C_3 \end{cases} $$

### 3.2 Conservation of Angular Momentum for Multi-Particle Systems
For an $N$-particle material system:
$$ \mathbf{H}_{A0} = \sum_{i=1}^N \mathbf{AP}_i \times m_i \mathbf{v}_0^{P_i} $$
Differentiating with respect to time about a fixed point $A$:
$$ \frac{d\mathbf{H}_{A0}}{dt}\Bigg|_0 = \sum_{i=1}^N \mathbf{AP}_i \times \mathbf{F}_i^{\text{ext}} + \sum_{i=1}^N \sum_{j \ne i} \mathbf{AP}_i \times \mathbf{f}_{ij}^{\text{int}} = \mathbf{M}_A^{\text{ext}} $$
Because internal torques sum to zero ($\sum \mathbf{AP}_i \times \mathbf{f}_{ij} = \mathbf{0}$):
$$ \mathbf{M}_A^{\text{ext}} = \mathbf{0} \implies \mathbf{H}_{A0} = \text{constant} $$
*Application:* An isolated system (e.g., satellite with deploying solar arrays, spinning celestial bodies) maintains its total angular momentum constant.

---

## 🎯 4. Central Force Problems (Slide 7, Notes 4.8.1)

### 4.1 Definition
A force field $\mathbf{F}$ is called a **central force** with respect to a fixed origin $O$ if the line of action of the force always passes through $O$ at every instant:
$$ \mathbf{F} = F(r, \dots)\,\mathbf{e}_r = F(r)\,\frac{\mathbf{r}}{r} $$
where $\mathbf{r} = \mathbf{r}_0^P$ is the position vector from $O$ to $P$, $r = \|\mathbf{r}\|$, and $\mathbf{e}_r = \mathbf{r}/r$ is the radial unit vector.

### 4.2 The Five Key Physical Properties (Slide 7 & Notes Sec. 4.8.1)

1. **Conservation of Angular Momentum Vector:**
   The moment of the force about the center of attraction $O$ is identically zero:
   $$ \mathbf{M}_O = \mathbf{r} \times \mathbf{F} = \mathbf{r} \times \left(F\,\frac{\mathbf{r}}{r}\right) = \frac{F}{r}\,(\mathbf{r} \times \mathbf{r}) \equiv \mathbf{0} $$
   Therefore, the angular momentum about $O$ is an exact invariant of motion:
   $$ \mathbf{H}_{O0}^P = \mathbf{r} \times m\mathbf{v}_0^P = \mathbf{H} = \text{constant vector} $$

2. **Planar Nature of Motion:**
   By definition of the vector cross product:
   $$ \mathbf{r}(t) \cdot \mathbf{H} = \mathbf{r} \cdot (\mathbf{r} \times m\mathbf{v}) \equiv 0, \qquad \mathbf{v}(t) \cdot \mathbf{H} = \mathbf{v} \cdot (\mathbf{r} \times m\mathbf{v}) \equiv 0 $$
   Because $\mathbf{H}$ is fixed in space, both the position vector $\mathbf{r}(t)$ and the velocity vector $\mathbf{v}(t)$ are permanently constrained to the plane passing through $O$ perpendicular to $\mathbf{H}$. The motion of a particle in any central force field is **strictly two-dimensional (planar)**.

3. **Natural Polar Coordinate Formulation:**
   Choosing Cartesian axes such that $\mathbf{H} = H\,\mathbf{k}$, the motion takes place entirely in the plane $z = 0$. The natural coordinate system is **polar coordinates $(r, \theta)$**:
   $$ \mathbf{r} = r\,\mathbf{e}_r, \qquad \mathbf{v} = \dot{r}\,\mathbf{e}_r + r\dot{\theta}\,\mathbf{e}_\theta $$
   The angular momentum magnitude is:
   $$ H = \|\mathbf{r} \times m\mathbf{v}\| = \|r\mathbf{e}_r \times m(\dot{r}\mathbf{e}_r + r\dot{\theta}\mathbf{e}_\theta)\| = m r^2 \dot{\theta} = \text{constant} $$

4. **Inverse Velocity-Radius Relationship:**
   Defining the **mass-specific angular momentum** $h \equiv H/m$:
   $$ h = r^2\dot{\theta} = \text{constant} \implies \dot{\theta}(t) = \frac{h}{r^2(t)} $$
   As the particle approaches the center of attraction ($r$ decreases), its angular rotation rate $\dot{\theta}$ must increase, and vice versa.

5. **Non-Reachability of the Center ($r \to 0$ Barrier):**
   If $h \ne 0$, as $r \to 0$, the required angular velocity diverges as $\dot{\theta} \sim 1/r^2$, and the transverse kinetic energy diverges as:
   $$ T_\theta = \frac{1}{2}m (r\dot{\theta})^2 = \frac{m h^2}{2r^2} \to +\infty $$
   Unless the potential energy becomes infinitely attractive faster than $-1/r^2$, a particle with non-zero angular momentum **can never reach the origin $O$**. The particle can only collide with $O$ if $h = 0$ (rectilinear radial motion).

---

## 🌌 5. Kepler's Problem and the Two-Body Reduction (Slides 8–10, Notes 8.1–8.3)

### 5.1 Empirical Kepler's Laws (Slide 8)
Formulated by Johannes Kepler between 1609 and 1619 from Tycho Brahe's planetary observations:
1. **1st Law:** The orbit of each planet is an ellipse with the Sun at one of the two foci.
2. **2nd Law:** The line segment joining a planet to the Sun sweeps out equal areas in equal intervals of time ($dA/dt = \text{const}$).
3. **3rd Law:** The square of the orbital period $\tau$ is directly proportional to the cube of the semi-major axis $a$ of its elliptical orbit:
   $$ \tau^2 \propto a^3 $$

### 5.2 Newtonian Gravitational Formulation (Slide 9)
Newton provided the physical foundation through his **Universal Law of Gravitation**:
$$ \mathbf{F}_g = -\frac{G m^P m^S}{\|\mathbf{r}_0^P - \mathbf{r}_0^S\|^2} \frac{\mathbf{r}_0^P - \mathbf{r}_0^S}{\|\mathbf{r}_0^P - \mathbf{r}_0^S\|} $$

In an inertial frame $S_0$, the equations of motion for the planet/satellite $P$ and the Sun/Earth $S$ are:
$$ m^P \frac{d^2\mathbf{r}_0^P}{dt^2}\Bigg|_0 = -\frac{G m^P m^S}{\|\mathbf{r}_0^P - \mathbf{r}_0^S\|^3}(\mathbf{r}_0^P - \mathbf{r}_0^S) $$
$$ m^S \frac{d^2\mathbf{r}_0^S}{dt^2}\Bigg|_0 = +\frac{G m^P m^S}{\|\mathbf{r}_0^P - \mathbf{r}_0^S\|^3}(\mathbf{r}_0^P - \mathbf{r}_0^S) $$

### 5.3 Center of Mass & Barycentric Reduction (Slides 9–10)
Summing both equations yields:
$$ m^P \frac{d^2\mathbf{r}_0^P}{dt^2}\Bigg|_0 + m^S \frac{d^2\mathbf{r}_0^S}{dt^2}\Bigg|_0 = (m^S + m^P)\frac{d^2\mathbf{r}_0^G}{dt^2}\Bigg|_0 = \mathbf{0} $$
The center of mass (barycenter $G$) moves with constant velocity in $S_0$. A non-rotating reference frame $S_G$ centered at $G$ is therefore also an **inertial reference frame**.

Defining the relative position vector $\mathbf{r} \equiv \mathbf{r}_0^P - \mathbf{r}_0^S$:
$$ \frac{d^2\mathbf{r}}{dt^2} = \frac{d^2\mathbf{r}_0^P}{dt^2} - \frac{d^2\mathbf{r}_0^S}{dt^2} = -\frac{G m^S}{r^3}\mathbf{r} - \frac{G m^P}{r^3}\mathbf{r} = -\frac{G(m^S + m^P)}{r^3}\mathbf{r} $$

Defining the **standard gravitational parameter** $\mu$:
$$ \mu \equiv G(m^S + m^P) $$
The relative motion reduces to the **equivalent one-body Kepler equation** (Slide 11):
$$ \frac{d^2\mathbf{r}}{dt^2} = -\frac{\mu}{r^3}\mathbf{r} = -\frac{\mu}{r^2}\mathbf{e}_r $$

In aerospace orbital mechanics (satellites orbiting Earth, planets orbiting the Sun), $m^S \gg m^P$:
$$ \mu \approx G m^S = \text{constant} $$
For Earth: $\mu_\oplus = G M_\oplus \approx 3.986004418 \times 10^{14}\,\text{m}^3/\text{s}^2$.

---

## 📐 6. Kinematics, Dynamics, and Kepler's 2nd Law (Slide 12, Notes 8.2–8.4)

### 6.1 Equations of Motion in Polar Coordinates
In the orbital plane:
* Position: $\mathbf{r} = r\,\mathbf{e}_r$
* Velocity: $\mathbf{v} = \dot{r}\,\mathbf{e}_r + r\dot{\theta}\,\mathbf{e}_\theta$
* Acceleration: $\mathbf{a} = (\ddot{r} - r\dot{\theta}^2)\,\mathbf{e}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\,\mathbf{e}_\theta$

Projecting $\mathbf{a} = -\frac{\mu}{r^2}\mathbf{e}_r$:
$$ \mathbf{e}_r: \quad \ddot{r} - r\dot{\theta}^2 = -\frac{\mu}{r^2} $$
$$ \mathbf{e}_\theta: \quad r\ddot{\theta} + 2\dot{r}\dot{\theta} = 0 $$

### 6.2 Specific Angular Momentum Integration
Multiplying the $\mathbf{e}_\theta$ equation by $r$:
$$ r(r\ddot{\theta} + 2\dot{r}\dot{\theta}) = r^2\ddot{\theta} + 2r\dot{r}\dot{\theta} = \frac{d}{dt}\left(r^2\dot{\theta}\right) = 0 $$
Integrating directly:
$$ h = r^2\dot{\theta} = \text{constant} $$
where $h = \|\mathbf{r} \times \mathbf{v}\|$ is the **magnitude of mass-specific angular momentum**.

### 6.3 Proof of Kepler's 2nd Law (Areal Velocity)
In an infinitesimal time interval $dt$, the radius vector sweeps out an area element $dA$ that can be approximated by a triangle of base $r\,d\theta$ and height $r$:
$$ dA = \frac{1}{2} r (r\,d\theta) = \frac{1}{2} r^2 d\theta $$
Dividing by $dt$:
$$ \frac{dA}{dt} = \frac{1}{2} r^2 \frac{d\theta}{dt} = \frac{1}{2} r^2 \dot{\theta} = \frac{h}{2} = \text{constant} $$

Because $h$ is strictly constant, the **areal velocity $\dot{A}$ is constant in time**:
$$ \frac{dA}{dt} = \frac{h}{2} = \text{constant} $$
*Physical Meaning:* The line segment joining the orbiting body to the gravitational center sweeps out equal geometric areas in equal intervals of time (Kepler's Second Law).

---

## 🔄 7. The Binet Equation & Proof of Kepler's 1st Law (Slide 13, Notes 8.4)

### 7.1 Derivation of the Binet Differential Operator
We eliminate time $t$ in favor of the true anomaly $\theta$ using $h = r^2\dot{\theta} \implies \dot{\theta} = h/r^2$.
Consider the variable substitution:
$$ u(\theta) \equiv \frac{1}{r(\theta)} $$

Applying the chain rule to the radial velocity $\dot{r}$:
$$ \frac{dr}{dt} = \frac{dr}{d\theta}\frac{d\theta}{dt} = \dot{\theta}\frac{dr}{d\theta} = \frac{h}{r^2}\frac{dr}{d\theta} = -h\frac{d}{d\theta}\left(\frac{1}{r}\right) = -h\frac{du}{d\theta} $$

Differentiating again with respect to time $t$ to find $\ddot{r}$:
$$ \frac{d^2r}{dt^2} = \frac{d}{dt}\left(-h\frac{du}{d\theta}\right) = \frac{d}{d\theta}\left(-h\frac{du}{d\theta}\right)\frac{d\theta}{dt} = -h\frac{d^2u}{d\theta^2}\dot{\theta} = -h\frac{d^2u}{d\theta^2}\left(\frac{h}{r^2}\right) = -\frac{h^2}{r^2}\frac{d^2u}{d\theta^2} = -h^2 u^2 \frac{d^2u}{d\theta^2} $$

### 7.2 Insertion into the Radial Equation of Motion
Substitute $\ddot{r}$ and $r\dot{\theta}^2$ into the radial dynamic equation $\ddot{r} - r\dot{\theta}^2 = -\mu/r^2$:
$$ -h^2 u^2 \frac{d^2u}{d\theta^2} - \frac{1}{u}\left(h u^2\right)^2 = -\mu u^2 $$
$$ -h^2 u^2 \frac{d^2u}{d\theta^2} - h^2 u^3 = -\mu u^2 $$

Dividing through by $-h^2 u^2$ (since $u \ne 0$ for finite distances):
$$ \frac{d^2u}{d\theta^2} + u = \frac{\mu}{h^2} $$
This is the celebrated **Binet Equation** for an inverse-square central force field!

### 7.3 General Solution & Trajectory Equation
The Binet equation is an ordinary second-order linear differential equation with constant coefficients, mathematically identical to an **undamped harmonic oscillator with a constant driving force**:
1. **Homogeneous Solution:**
   $$ u_h(\theta) = C_1\cos\theta + C_2\sin\theta = A\cos(\theta - \omega) $$
2. **Particular Solution:**
   $$ u_p(\theta) = \frac{\mu}{h^2} $$
3. **General Solution:**
   $$ u(\theta) = \frac{\mu}{h^2} + A\cos(\theta - \omega) = \frac{\mu}{h^2}\left[ 1 + \left(\frac{A h^2}{\mu}\right)\cos(\theta - \omega) \right] $$

Defining the dimensionless **eccentricity** $e \equiv \frac{A h^2}{\mu}$ and orienting the polar coordinate system so that $\theta = 0$ corresponds to minimum distance (pericenter), we set $\omega = 0$:
$$ u(\theta) = \frac{1}{r(\theta)} = \frac{\mu}{h^2}(1 + e\cos\theta) $$
Inverting to obtain $r(\theta)$:
$$ r(\theta) = \frac{h^2/\mu}{1 + e\cos\theta} = \frac{p}{1 + e\cos\theta} $$
where $p \equiv h^2/\mu$ is the **semi-latus rectum** (or conic parameter).

This is the standard polar equation of a **conic section with one focus at the origin $O$**, proving Kepler's First Law!

---

## 📉 8. Conic Section Trajectories & Classification (Slide 14, Notes 8.4)

### 8.1 Geometric Classification by Eccentricity
The nature of the orbit is governed exclusively by the eccentricity parameter $e \ge 0$:

| Eccentricity $e$ | Semi-major axis $a$ | Geometric Shape | Physical Orbit Type | Bound / Unbound |
| :---: | :---: | :---: | :---: | :---: |
| $e = 0$ | $a = p > 0$ | Circle | Circular satellite orbit | Bound |
| $0 < e < 1$ | $a > 0$ | Ellipse | Planetary & satellite orbits | Bound |
| $e = 1$ | $a \to \infty$ | Parabola | Parabolic escape trajectory | Unbound (critical) |
| $e > 1$ | $a < 0$ | Hyperbola | Interplanetary flybys / probes | Unbound |

### 8.2 Geometric Relations for Elliptical Orbits ($0 \le e < 1$)
* **Periapsis Distance ($r_p$, closest approach at $\theta = 0$):**
  $$ r_p = \frac{p}{1 + e} = a(1 - e) $$
* **Apoapsis Distance ($r_a$, farthest distance at $\theta = \pi$):**
  $$ r_a = \frac{p}{1 - e} = a(1 + e) $$
* **Semi-Major Axis ($a$):**
  $$ 2a = r_p + r_a \implies a = \frac{r_p + r_a}{2} = \frac{p}{1 - e^2} $$
* **Semi-Latus Rectum ($p$):**
  $$ p = a(1 - e^2) = \frac{h^2}{\mu} \implies h = \sqrt{\mu p} = \sqrt{\mu a(1 - e^2)} $$
* **Semi-Minor Axis ($b$):**
  $$ b = a\sqrt{1 - e^2} = \sqrt{a p} $$
* **Linear Eccentricity ($c$, focus-to-center distance):**
  $$ c = a e = \sqrt{a^2 - b^2} $$

---

## ⏱️ 9. Orbital Period & Kepler's 3rd Law (Slide 15, Notes 8.4)

### 9.1 Analytical Derivation
The total area enclosed by an ellipse of semi-major axis $a$ and semi-minor axis $b$ is:
$$ A_{\text{ellipse}} = \pi a b $$

Integrating the areal velocity $\frac{dA}{dt} = \frac{h}{2}$ over one complete orbital period $\tau$:
$$ \int_0^\tau \frac{dA}{dt}\,dt = \int_0^{A_{\text{ellipse}}} dA \implies \frac{h}{2}\tau = \pi a b $$
Solving for the orbital period $\tau$:
$$ \tau = \frac{2\pi a b}{h} $$

Substituting $b = a\sqrt{1 - e^2}$ and $h = \sqrt{\mu a(1 - e^2)}$:
$$ \tau = \frac{2\pi a \left(a\sqrt{1 - e^2}\right)}{\sqrt{\mu a(1 - e^2)}} = \frac{2\pi a^2 \sqrt{1 - e^2}}{\sqrt{\mu a}\sqrt{1 - e^2}} = \frac{2\pi a^{3/2}}{\sqrt{\mu}} = 2\pi\sqrt{\frac{a^3}{\mu}} $$

### 9.2 Kepler's Third Law Formulation
Squaring both sides of the orbital period equation:
$$ \tau^2 = \frac{4\pi^2}{\mu} a^3 $$
*Crucial Conclusion:* The square of the orbital period is strictly proportional to the cube of the semi-major axis, depending only on the gravitational parameter $\mu = G(M + m) \approx GM$. The orbital period is **completely independent of the eccentricity $e$**!

---

## ⚡ 10. The Vis-Viva Equation & Energy Conservation (Slides 11, 16, Notes 8.5)

### 10.1 Mass-Specific Mechanical Energy
Because Newtonian gravity is a conservative central force field, the potential energy per unit mass is:
$$ V_0(r) = -\int_\infty^r \left(-\frac{\mu}{r'^2}\right) dr' = -\frac{\mu}{r} $$
The total mass-specific mechanical energy $\xi \equiv E/m$ is conserved:
$$ \xi = \frac{1}{2}v^2 - \frac{\mu}{r} = \text{constant} $$

### 10.2 Determination of the Energy Constant
At periapsis ($r = r_p = a(1-e)$), the velocity is purely transverse ($v = v_p = r_p \dot{\theta}_p$):
$$ v_p = \frac{h}{r_p} = \frac{\sqrt{\mu a(1 - e^2)}}{a(1 - e)} = \sqrt{\frac{\mu(1+e)(1-e)}{a(1-e)^2}} = \sqrt{\frac{\mu}{a}\frac{1+e}{1-e}} $$
Evaluating $\xi$ at periapsis:
$$ \xi = \frac{1}{2}v_p^2 - \frac{\mu}{r_p} = \frac{1}{2}\left[\frac{\mu}{a}\frac{1+e}{1-e}\right] - \frac{\mu}{a(1-e)} = \frac{\mu}{2a(1-e)}\left[ (1+e) - 2 \right] = \frac{\mu(e - 1)}{2a(1-e)} = -\frac{\mu}{2a} $$

We obtain the fundamental relation between specific orbital energy and semi-major axis:
$$ \xi = -\frac{\mu}{2a} $$

### 10.3 The Vis-Viva Equation
Equating the energy expressions:
$$ \frac{1}{2}v^2 - \frac{\mu}{r} = -\frac{\mu}{2a} $$
Multiplying by 2:
$$ v^2 = \mu\left(\frac{2}{r} - \frac{1}{a}\right) $$

#### Physical Implications of the Energy Sign:
* **Elliptic Orbits ($a > 0$):** $\xi < 0$ (gravitationally bound system).
* **Parabolic Orbits ($a \to \infty$):** $\xi = 0$ (marginally bound/escape threshold).
* **Hyperbolic Orbits ($a < 0$):** $\xi > 0$ (unbound, positive excess energy at infinity $v_\infty^2 = -\mu/a$).

---

## 🚀 11. Fundamental Orbital Velocities (Slide 16, Notes 8.5)

### 11.1 Circular Velocity ($v_c$)
For a circular orbit of radius $r = a$:
$$ v_c = \sqrt{\mu\left(\frac{2}{r} - \frac{1}{r}\right)} = \sqrt{\frac{\mu}{r}} = \sqrt{\frac{\mu}{a}} $$
*Circular speed decreases monotonically with orbital altitude ($v_c \propto 1/\sqrt{r}$).*

### 11.2 Escape Velocity ($v_e$)
The minimum speed required at distance $r$ to escape the gravitational field and reach $r \to \infty$ with zero residual speed ($v_\infty = 0 \implies \xi = 0, a \to \infty$):
$$ v_e = \sqrt{\mu\left(\frac{2}{r} - 0\right)} = \sqrt{\frac{2\mu}{r}} = \sqrt{2}\,v_c $$
*The escape velocity is always exactly $\sqrt{2} \approx 1.4142$ times the local circular orbital velocity.*

### 11.3 Periapsis and Apoapsis Velocities ($v_p, v_a$)
From the Vis-Viva equation evaluated at $r_p = a(1-e)$ and $r_a = a(1+e)$:
$$ v_p = \sqrt{\frac{\mu}{a}\frac{1+e}{1-e}} $$
$$ v_a = \sqrt{\frac{\mu}{a}\frac{1-e}{1+e}} $$
*Velocity ratio across apsides:*
$$ \frac{v_p}{v_a} = \frac{1+e}{1-e} = \frac{r_a}{r_p} \quad (\text{consistent with } r_p v_p = r_a v_a = h) $$

---

## 🧪 12. Solved Benchmark Example: Linear Central Force under Gravity (Slide 6, Problem 17)

### 12.1 Problem Statement
A force attracts a heavy particle $M$ of mass $m$ towards the origin $O$. The attractive force is proportional to the mass and the distance $OM$, with proportionality constant $k^2$:
$$ \mathbf{F}_{\text{attract}} = -m k^2 \mathbf{r} $$
Gravity acts vertically downwards along the $-Oz$ axis: $\mathbf{g} = -g\mathbf{k}$.
Initial state at $t = 0$:
$$ (x_0, y_0, z_0) = \left(\frac{\sqrt{3}g}{k^2}, 0, 0\right), \qquad (\dot{x}_0, \dot{y}_0, \dot{z}_0) = \left(0, \frac{2g}{k}, 0\right) $$
*(a) Describe the motion of $M$, specifying clearly the shape of the path.*  
*(b) What is the velocity of the particle as a function of $t$?*

### 12.2 Step-by-Step Analytical Solution

#### Step 1: Equations of Motion in Cartesian Coordinates
Applying Newton's Second Law $m\ddot{\mathbf{r}} = \mathbf{F}_{\text{attract}} + m\mathbf{g}$:
$$ m\left(\ddot{x}\mathbf{i} + \ddot{y}\mathbf{j} + \ddot{z}\mathbf{k}\right) = -m k^2 (x\mathbf{i} + y\mathbf{j} + z\mathbf{k}) - mg\mathbf{k} $$
Dividing by $m$:
$$ \begin{cases} \ddot{x} + k^2 x = 0 \\ \ddot{y} + k^2 y = 0 \\ \ddot{z} + k^2 z = -g \end{cases} $$
The three Cartesian degrees of freedom are **completely decoupled**!

#### Step 2: Integration of $x(t)$
General solution: $x(t) = C_1\cos(kt) + C_2\sin(kt)$.
Initial conditions: $x(0) = \frac{\sqrt{3}g}{k^2}$, $\dot{x}(0) = 0 \implies C_1 = \frac{\sqrt{3}g}{k^2}, C_2 = 0$.
$$ x(t) = \frac{\sqrt{3}g}{k^2}\cos(kt) $$

#### Step 3: Integration of $y(t)$
General solution: $y(t) = C_3\cos(kt) + C_4\sin(kt)$.
Initial conditions: $y(0) = 0$, $\dot{y}(0) = \frac{2g}{k} \implies C_3 = 0, C_4 = \frac{2g}{k^2}$.
$$ y(t) = \frac{2g}{k^2}\sin(kt) $$

#### Step 4: Integration of $z(t)$
Shift coordinates to equilibrium: $z^* = z + \frac{g}{k^2} \implies \ddot{z}^* + k^2 z^* = 0$.
General solution: $z(t) = -\frac{g}{k^2} + C_5\cos(kt) + C_6\sin(kt)$.
Initial conditions: $z(0) = 0 \implies C_5 = \frac{g}{k^2}$; $\dot{z}(0) = 0 \implies C_6 = 0$.
$$ z(t) = -\frac{g}{k^2}\left(1 - \cos(kt)\right) = \frac{g}{k^2}\cos(kt) - \frac{g}{k^2} $$

#### Step 5: Geometric Trajectory Characterization
Notice the trigonometric link between $x(t)$ and $z(t)$:
$$ \cos(kt) = \frac{k^2 x}{\sqrt{3}g} \implies z(t) = \frac{g}{k^2}\left(\frac{k^2 x}{\sqrt{3}g}\right) - \frac{g}{k^2} = \frac{x}{\sqrt{3}} - \frac{g}{k^2} $$
The particle is permanently confined to the **plane**:
$$ x - \sqrt{3}z - \frac{\sqrt{3}g}{k^2} = 0 $$

Furthermore, eliminating the parameter $t$ between $x(t)$ and $y(t)$:
$$ \left(\frac{x}{\sqrt{3}g/k^2}\right)^2 + \left(\frac{y}{2g/k^2}\right)^2 = \cos^2(kt) + \sin^2(kt) = 1 $$
The projection of the trajectory onto the $Oxy$ plane is an **ellipse** of semi-axes:
$$ a_x = \frac{\sqrt{3}g}{k^2}, \qquad b_y = \frac{2g}{k^2} $$
Because the intersection of an elliptic cylinder with an oblique plane is an ellipse, the **3D trajectory of particle $M$ is a planar ellipse** contained in the inclined plane $x - \sqrt{3}z = \frac{\sqrt{3}g}{k^2}$, centered at $(0, 0, -g/k^2)$.

#### Step 6: Velocity Vector as a Function of Time
Differentiating $\mathbf{r}(t)$:
$$ \mathbf{v}(t) = \dot{x}(t)\mathbf{i} + \dot{y}(t)\mathbf{j} + \dot{z}(t)\mathbf{k} $$
$$ \mathbf{v}(t) = -\frac{\sqrt{3}g}{k}\sin(kt)\,\mathbf{i} + \frac{2g}{k}\cos(kt)\,\mathbf{j} - \frac{g}{k}\sin(kt)\,\mathbf{k} $$
Velocity magnitude squared:
$$ v^2(t) = \frac{g^2}{k^2}\left(3\sin^2(kt) + 4\cos^2(kt) + \sin^2(kt)\right) = \frac{g^2}{k^2}\left(4\sin^2(kt) + 4\cos^2(kt)\right) = \frac{4g^2}{k^2} $$
Remarkably, the **speed of the particle is constant**:
$$ v(t) = \frac{2g}{k} = \text{constant} $$

---

## 📚 Pedagogical Summary & Study Guidelines
1. **Always check torque:** If $\mathbf{M}_O = \mathbf{0}$, $\mathbf{H}_O$ is conserved $\implies$ the motion is planar.
2. **Polar coordinates are natural:** For any central force, $h = r^2\dot{\theta}$ is the first integral of motion.
3. **Binet variable $u = 1/r$ transforms nonlinear orbital kinematics into a linear oscillator.**
4. **Vis-Viva equation connects speed, position, and orbital semi-major axis without integrating time laws.**
