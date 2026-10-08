---
title: "Topic 4: Angular Momentum and Central Forces (Kepler's Problem)"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
ground_truth: "slides/04_-_Angular_momentum.pdf & teoria/Notes.pdf (Chapters 4.8 & 8)"
tier: "Theory Master Guide"
language: "English"
tags:
  - topic-4
  - angular-momentum
  - central-forces
  - kepler-problem
---

# 🌀 Topic 4: Angular Momentum, Central Forces & Kepler's Problem

## 📌 Syllabus & Pedagogical Map
This comprehensive master guide provides the complete theoretical, mathematical, and physical development of **Angular Momentum, Central Force Fields, and Kepler's Problem** in classical aerospace mechanics. It follows **`slides/04_-_Angular_momentum.pdf`** (Slides 1–17) and Section 4.8 (pp. 49–51, Eqs. 4.48–4.58) and Chapter 8 (pp. 71–74, Eqs. 8.1–8.21) of **`teoria/Notes.pdf`**, and adds the intermediate steps that the sources skip (two-body reduction, the $d(1/u)/d\theta$ chain rule, the integration constants of the Binet solution, and the effective-potential first integral used in Problem 42). Equation numbers quoted below are the numbers printed in `Notes.pdf`.

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
   (Notes Sec. 4.8.1, property 5.) If $h \ne 0$, as $r \to 0$, the required angular velocity diverges as $\dot{\theta} \sim 1/r^2$, and the transverse kinetic energy diverges as:
   $$ T_\theta = \frac{1}{2}m (r\dot{\theta})^2 = \frac{m h^2}{2r^2} \to +\infty $$
   Unless the potential energy becomes infinitely attractive at least as fast as $-1/r^2$, a particle with non-zero angular momentum **cannot reach the origin $O$**. For the Newtonian potential $-\mu/r$ (and for any central force weaker than $1/r^3$) the particle can only collide with $O$ if $h = 0$ (rectilinear radial motion). The statement is **not** true for every central force: in Problem 42 the forces $F \propto 1/r^3$ (with $h^2 < \mu$) and $F \propto 1/r^4$ do carry particles with $h \ne 0$ to $r = 0$ (see [[Solutions - Topic 4 Angular Momentum and Central Forces]]).

---

## 🌌 5. Kepler's Problem and the Two-Body Reduction (Slides 8–11, Notes Ch. 8 intro and 8.1)

### 5.1 Empirical Kepler's Laws (Slide 8, Notes Sec. 8.1)
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

### 5.3 Center of Mass & Reduction to a One-Body Problem (Slides 9–11)
**Why.** The two equations of §5.2 are coupled through the same relative vector. Adding them removes the interaction (action and reaction cancel) and shows how the pair moves as a whole; subtracting them isolates the relative motion, which is the only part that carries the orbit.

*Note on the sources.* `Notes.pdf` Chapter 8 skips this step: it takes $m^P \ll m^S$ from the start, places $O$ at the barycentre and writes $\mu = G m^S$ (Eq. 8.1). The reduction below follows Slides 9–11.

**Step 1: motion of the barycentre (sum).** Let $M_{\text{tot}} = m^S + m^P$ and define the barycentre
$$ \mathbf{r}_0^G = \frac{m^P\mathbf{r}_0^P + m^S\mathbf{r}_0^S}{M_{\text{tot}}} $$
Adding the two equations of motion of §5.2, the right-hand sides cancel because the forces are equal and opposite:
$$ m^P \ddot{\mathbf{r}}_0^P + m^S \ddot{\mathbf{r}}_0^S = M_{\text{tot}}\,\ddot{\mathbf{r}}_0^G = \mathbf{0} $$
Integrating twice in time,
$$ \dot{\mathbf{r}}_0^G = \mathbf{v}_0^G = \text{const}, \qquad \mathbf{r}_0^G(t) = \mathbf{r}_0^G(0) + \mathbf{v}_0^G\,t $$
so the barycentre moves **uniformly in a straight line**. A frame $S_G$ with origin at $G$ and axes parallel to $S_0$ is related to $S_0$ by a translation at constant velocity (the change-of-basis matrix is the identity, $\det = 1$), hence $S_G$ is inertial and $d/dt|_G = d/dt|_0$.

**Step 2: relative motion (difference).** Divide the first equation by $m^P$ and the second by $m^S$ and subtract. With $\mathbf{r} \equiv \mathbf{r}_0^P - \mathbf{r}_0^S$ and $r = \|\mathbf{r}\|$:
$$ \ddot{\mathbf{r}} = \ddot{\mathbf{r}}_0^P - \ddot{\mathbf{r}}_0^S = -\frac{G m^S}{r^3}\mathbf{r} - \frac{G m^P}{r^3}\mathbf{r} = -\frac{G(m^S + m^P)}{r^3}\mathbf{r} $$
Defining the **standard gravitational parameter** $\mu \equiv G(m^S + m^P)$ gives the **equivalent one-body Kepler equation** (Slide 11):
$$ \frac{d^2\mathbf{r}}{dt^2} = -\frac{\mu}{r^3}\mathbf{r} = -\frac{\mu}{r^2}\mathbf{e}_r $$

**Reduced mass.** Multiplying by $m_{\text{red}} \equiv \dfrac{m^P m^S}{m^P + m^S}$ and using $m_{\text{red}}\,G(m^S + m^P) = G m^P m^S$:
$$ m_{\text{red}}\,\ddot{\mathbf{r}} = -\frac{G m^P m^S}{r^2}\mathbf{e}_r $$
that is, the relative vector moves like a single particle of mass $m_{\text{red}}$ attracted by a fixed centre with the full gravitational force. Once $\mathbf{r}(t)$ is known, each body is recovered from the barycentre:
$$ \mathbf{r}_0^P = \mathbf{r}_0^G + \frac{m^S}{M_{\text{tot}}}\,\mathbf{r}, \qquad \mathbf{r}_0^S = \mathbf{r}_0^G - \frac{m^P}{M_{\text{tot}}}\,\mathbf{r} $$
so both bodies describe similar conics about $G$, scaled by $m^S/M_{\text{tot}}$ and $m^P/M_{\text{tot}}$.

**Limit used in aerospace.** If $m^S \gg m^P$ (satellite around Earth, planet around Sun), then $m_{\text{red}} \to m^P$, $G \to S$ and $\mu \approx G m^S$, as in Notes Eq. 8.1. For Earth: $\mu_\oplus = G M_\oplus \approx 3.986004418 \times 10^{14}\,\text{m}^3/\text{s}^2$. The mass of $P$ does not appear in the reduced equation, so the motion is independent of $m^P$ and mass-specific variables (specific angular momentum, specific energy) are used from now on.

---

## 📐 6. Kinematics, Dynamics, and Kepler's 2nd Law (Slide 12, Notes 8.2–8.4)

### 6.1 Equations of Motion in Polar Coordinates
**Why a rotating basis.** Because $\mathbf{H}$ is fixed (§4.2), choose $S_0$ with $\mathbf{k}_0 \parallel \mathbf{H}$ so that the motion is in the plane $z = 0$. The direction of $\mathbf{r}$ changes with time, so we attach to $P$ the polar basis $\mathcal{B}_1 = \{\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}_0\}$ (Notes Eq. 8.2):
$$ \mathbf{e}_r = \cos\theta\,\mathbf{i}_0 + \sin\theta\,\mathbf{j}_0, \qquad \mathbf{e}_\theta = -\sin\theta\,\mathbf{i}_0 + \cos\theta\,\mathbf{j}_0, \qquad \mathbf{k}_0 $$
The change-of-basis matrix (columns are the components of $\mathbf{e}_r, \mathbf{e}_\theta, \mathbf{k}_0$ in $\mathcal{B}_0$) is
$$ [{}_0 R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = \cos^2\theta + \sin^2\theta = 1, \qquad [{}_0 R_1]^T[{}_0 R_1] = I $$
(the columns are unit vectors and mutually orthogonal: $\mathbf{e}_r\cdot\mathbf{e}_\theta = -\cos\theta\sin\theta + \sin\theta\cos\theta = 0$). The basis rotates with angular velocity $\boldsymbol{\omega}_{10} = \dot{\theta}\,\mathbf{k}_0$, so Poisson's formula $\dot{\mathbf{e}} = \boldsymbol{\omega}\times\mathbf{e}$ gives
$$ \dot{\mathbf{e}}_r = \dot{\theta}\,\mathbf{k}_0\times\mathbf{e}_r = \dot{\theta}\,\mathbf{e}_\theta, \qquad \dot{\mathbf{e}}_\theta = \dot{\theta}\,\mathbf{k}_0\times\mathbf{e}_\theta = -\dot{\theta}\,\mathbf{e}_r $$
Differentiating $\mathbf{r} = r\mathbf{e}_r$ with the product rule:
$$ \mathbf{v} = \dot{r}\,\mathbf{e}_r + r\dot{\mathbf{e}}_r = \dot{r}\,\mathbf{e}_r + r\dot{\theta}\,\mathbf{e}_\theta $$
$$ \mathbf{a} = \ddot{r}\,\mathbf{e}_r + \dot{r}\dot{\theta}\,\mathbf{e}_\theta + \left(\dot{r}\dot{\theta} + r\ddot{\theta}\right)\mathbf{e}_\theta + r\dot{\theta}\left(-\dot{\theta}\,\mathbf{e}_r\right) $$
In the orbital plane (Notes Eq. 8.3):
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
**Why.** The radial equation $\ddot{r} - r\dot{\theta}^2 = -\mu/r^2$ is nonlinear in $r(t)$. We want the shape $r(\theta)$ of the orbit and not the time law, and the substitution $u = 1/r$ together with $\theta$ as independent variable turns it into a linear equation (Notes Eqs. 8.9–8.12).

Because $h = r^2\dot{\theta}$ is constant and $\dot{\theta} > 0$ (or $< 0$, a mirror image), $\theta$ is a monotonic function of $t$ and can replace it. Define
$$ u(\theta) \equiv \frac{1}{r(\theta)}, \qquad \dot{\theta} = \frac{h}{r^2} = h u^2 $$
The time derivative of any function $f(\theta(t))$ is $\dot{f} = f'\,\dot{\theta} = h u^2 f'$, with $' = d/d\theta$.

**Step 1: derivative of $r = 1/u$ with respect to $\theta$ (chain rule).** Writing $r = u^{-1}$ and using $\dfrac{d}{du}u^{-1} = -u^{-2}$:
$$ \frac{dr}{d\theta} = \frac{d(1/u)}{d\theta} = \frac{d(u^{-1})}{du}\frac{du}{d\theta} = -\frac{1}{u^2}\,u' $$

**Step 2: radial velocity.**
$$ \dot{r} = \frac{dr}{d\theta}\,\dot{\theta} = \left(-\frac{u'}{u^2}\right)\left(h u^2\right) = -h\,u' $$
(Notes Eq. 8.10: $\dot{r} = -h\,d(1/r)/d\theta$; Eq. 8.9 is the same identity in time form, $-r^2\,d(1/r)/dt = \dot{r}$.)

**Step 3: radial acceleration.** Differentiate $\dot{r} = -h u'(\theta)$ with respect to time, again with the chain rule ($h$ is constant):
$$ \ddot{r} = \frac{d}{dt}\left(-h u'\right) = -h\,u''\,\dot{\theta} = -h\,u''\,\left(h u^2\right) = -h^2 u^2\,u'' $$
(Notes Eq. 8.11.)

**Step 4: centrifugal term.**
$$ r\dot{\theta}^2 = \frac{1}{u}\left(h u^2\right)^2 = h^2 u^3 $$

### 7.2 Insertion into the Radial Equation of Motion
Substitute $\ddot{r}$ and $r\dot{\theta}^2$ (Step 3 and Step 4) into the radial dynamic equation $\ddot{r} - r\dot{\theta}^2 = -\mu/r^2 = -\mu u^2$ (Notes Eq. 8.5):
$$ -h^2 u^2 \frac{d^2u}{d\theta^2} - \frac{1}{u}\left(h u^2\right)^2 = -\mu u^2 $$
$$ -h^2 u^2 \frac{d^2u}{d\theta^2} - h^2 u^3 = -\mu u^2 $$

Dividing through by $-h^2 u^2$ (since $u \ne 0$ for finite distances):
$$ \frac{d^2u}{d\theta^2} + u = \frac{\mu}{h^2} $$
This is the **Binet Equation** for an inverse-square central force field (Notes Eq. 8.12).

### 7.3 General Solution & Trajectory Equation
**Why this form.** The Binet equation is linear with constant coefficients, mathematically a harmonic oscillator in the variable $\theta$ driven by the constant $\mu/h^2$. Its general solution is the sum of the homogeneous solution and one particular solution (Notes Eq. 8.13).

1. **Homogeneous equation** $u_h'' + u_h = 0$: the characteristic roots are $\lambda = \pm i$, so
   $$ u_h(\theta) = C_1\cos\theta + C_2\sin\theta $$
2. **Particular solution:** try a constant $u_p = c$; then $0 + c = \mu/h^2$, so $u_p = \mu/h^2$.
3. **General solution:**
   $$ u(\theta) = \frac{\mu}{h^2} + C_1\cos\theta + C_2\sin\theta $$

**Fixing the constants from the initial data.** Let the particle have $u = u_i = 1/r_i$ and $u' = u_i' = -\dot{r}_i/h$ at the polar angle $\theta_i$ (measured from any convenient axis; take $\theta_i = 0$ for the moment). Then
$$ u(0) = \frac{\mu}{h^2} + C_1 = u_i \implies C_1 = u_i - \frac{\mu}{h^2}, \qquad u'(0) = C_2 = u_i' $$
The two constants can be written as an amplitude and a phase, $C_1\cos\theta + C_2\sin\theta = A\cos(\theta - \theta_0)$ with
$$ A = \sqrt{C_1^2 + C_2^2}, \qquad A\cos\theta_0 = C_1, \qquad A\sin\theta_0 = C_2 $$
so that
$$ u(\theta) = \frac{\mu}{h^2}\left[1 + e\cos(\theta - \theta_0)\right], \qquad e \equiv \frac{A h^2}{\mu} = \frac{h^2}{\mu}\sqrt{\left(u_i - \frac{\mu}{h^2}\right)^2 + u_i'^2} \;\ge 0 $$
**Choice of the angular origin.** The orbit is closest to the focus when $u$ is maximum, at $\theta - \theta_0 = 0$ (where $u' = -(\mu e/h^2)\sin(\theta - \theta_0) = 0$ and $u'' < 0$). Redefining the polar axis so that $\theta = 0$ is the periapsis direction, i.e. $\theta_0 = 0$ (the "rotated" polar axis is the first axis of the plane orbital basis $\{\mathbf{e}_p, \mathbf{e}_q, \mathbf{k}_0\}$ with $\mathbf{e}_p$ pointing to the periapsis, $\mathbf{e}_q = \mathbf{k}_0\times\mathbf{e}_p$; its change-of-basis matrix from $\mathcal{B}_0$ is the same rotation $[{}_0 R_1]$ with angle $\theta_0$, $\det = 1$, $R^TR = I$):
$$ \frac{1}{r(\theta)} = \frac{\mu}{h^2}\left(1 + e\cos\theta\right) \quad \text{(Notes Eq. 8.13 with } \psi = 0\text{)} $$
Inverting to obtain $r(\theta)$ (Notes Eq. 8.14):
$$ r(\theta) = \frac{h^2/\mu}{1 + e\cos\theta} = \frac{p}{1 + e\cos\theta}, \qquad p \equiv \frac{h^2}{\mu} $$
where $p$ is the **semi-latus rectum** (conic parameter) and $e$ is fixed by the initial position and velocity through the expression above. This is the polar equation of a **conic section with one focus at the origin $O$**, which proves Kepler's First Law for $e < 1$.

*Example (Problem 44).* With $r_i = R$, $\dot{r}_i = \tfrac{\sqrt{3}}{2}v_0$ and $h = \tfrac{1}{2}Rv_0$, the formula for $e$ gives $e = 31/35$ (worked in [[Solutions - Topic 4 Angular Momentum and Central Forces]]).

### 7.4 First Integral in the Variable $u$ and Effective Potential
**Why.** For a general central force $F(r)$ (Problem 42), the Binet equation becomes $u'' + u = -F(1/u)/(m h^2 u^2)$ and cannot be solved in closed form for every exponent. A first integral gives the limits of the motion without solving the equation.

The mass-specific energy $\xi = \tfrac{1}{2}v^2 + V_0(r)$ is conserved (the force is conservative). With $v^2 = \dot{r}^2 + r^2\dot{\theta}^2$, and from §7.1 $\dot{r} = -h u'$ and $r\dot{\theta} = h u$:
$$ \xi = \frac{1}{2}h^2\left[(u')^2 + u^2\right] + V_0\!\left(\frac{1}{u}\right) \implies (u')^2 + W_{\text{eff}}(u) = \frac{2\xi}{h^2} \equiv E^*, \qquad W_{\text{eff}}(u) = u^2 + \frac{2V_0(1/u)}{h^2} $$
Since $(u')^2 \ge 0$, motion is possible only where $W_{\text{eff}}(u) \le E^*$; turning points ($u' = 0$) are the roots of $W_{\text{eff}}(u) = E^*$. A minimum of $W_{\text{eff}}$ is a stable circular orbit, a maximum an unstable one. For the Newtonian potential $V_0 = -\mu u$:
$$ W_{\text{eff}}(u) = u^2 - \frac{2\mu}{h^2}u = \left(u - \frac{\mu}{h^2}\right)^2 - \left(\frac{\mu}{h^2}\right)^2 $$
a parabola with its minimum at $u = \mu/h^2$ (the circular orbit $r = p$); the bound motions are those with $-(\mu/h^2)^2 \le E^* < 0$. Differentiating the first integral with respect to $\theta$ and dividing by $2u'$ returns the Binet equation (check: $2u'u'' + W_{\text{eff}}'(u)\,u' = 0 \Rightarrow u'' + u - \mu/h^2 = 0$).
For the stability of circular orbits under other power laws, see the case-by-case discussion of $\alpha = 1, 2, 3, 4$ in Problem 42 of [[Solutions - Topic 4 Angular Momentum and Central Forces]]; `Notes.pdf` does not treat stability of circular orbits.

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
**Derivation from the orbit equation (Notes Eqs. 8.14–8.16).** Evaluate $r(\theta) = p/(1 + e\cos\theta)$ at the two apsides, $\theta = 0$ and $\theta = \pi$:
$$ r_p = \frac{p}{1 + e}, \qquad r_a = \frac{p}{1 - e} $$
The major axis is $2a = r_p + r_a$ (Eq. 8.15), hence
$$ 2a = \frac{p(1 - e) + p(1 + e)}{(1 + e)(1 - e)} = \frac{2p}{1 - e^2} \implies p = a(1 - e^2) $$
Combining with $p = h^2/\mu$ (Eq. 8.16):
$$ h^2 = \mu p = \mu a (1 - e^2) \implies h = \sqrt{\mu a(1 - e^2)} $$
and $r_p = \dfrac{a(1 - e^2)}{1 + e} = a(1 - e)$, $r_a = a(1 + e)$. The focus-to-centre distance is $c = a - r_p = ae$. At the end of the minor axis the sum of the distances to the two foci is $2a$ (definition of the ellipse), so each distance is $a$ and $b^2 + c^2 = a^2$, which gives $b = a\sqrt{1 - e^2}$.

**Summary:**

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

### 9.1 Analytical Derivation (Notes Eqs. 8.16–8.18, Slide 15)
The total area enclosed by an ellipse of semi-major axis $a$ and semi-minor axis $b$ is:
$$ A_{\text{ellipse}} = \pi a b $$

Integrating the areal velocity $\frac{dA}{dt} = \frac{h}{2}$ over one complete orbital period $\tau$:
$$ \int_0^\tau \frac{dA}{dt}\,dt = \int_0^{A_{\text{ellipse}}} dA \implies \frac{h}{2}\tau = \pi a b $$
Solving for the orbital period $\tau$:
$$ \tau = \frac{2\pi a b}{h} $$

Substituting $b = a\sqrt{1 - e^2}$ and $h = \sqrt{\mu a(1 - e^2)}$ (derived in §8.2):
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
**Why.** $\xi$ is constant, so its value can be computed at any convenient point of the orbit. At an apsis $\dot{r} = 0$ (because $u' \propto \sin\theta = 0$ there), so the velocity is purely transverse and angular momentum conservation $h = r v$ gives $v$ directly. Notes Sec. 8.5 states that the constant is obtained "at pericenter and apocenter"; the algebra is shown here.

**Periapsis** ($r_p = a(1 - e)$, $v_p = h/r_p$):
$$ v_p = \frac{h}{r_p} = \frac{\sqrt{\mu a(1 - e^2)}}{a(1 - e)} = \sqrt{\frac{\mu(1+e)(1-e)}{a(1-e)^2}} = \sqrt{\frac{\mu}{a}\frac{1+e}{1-e}} $$
$$ \xi = \frac{1}{2}v_p^2 - \frac{\mu}{r_p} = \frac{\mu}{2a}\frac{1+e}{1-e} - \frac{\mu}{a(1-e)} = \frac{\mu}{2a(1-e)}\left[(1+e) - 2\right] = -\frac{\mu(1-e)}{2a(1-e)} = -\frac{\mu}{2a} $$

**Apoapsis** ($r_a = a(1 + e)$, $v_a = h/r_a = \sqrt{\dfrac{\mu}{a}\dfrac{1-e}{1+e}}$):
$$ \xi = \frac{1}{2}v_a^2 - \frac{\mu}{r_a} = \frac{\mu}{2a}\frac{1-e}{1+e} - \frac{\mu}{a(1+e)} = \frac{\mu}{2a(1+e)}\left[(1-e) - 2\right] = -\frac{\mu(1+e)}{2a(1+e)} = -\frac{\mu}{2a} $$
Both apsides give the same value, as they must.

**Check at an arbitrary $\theta$.** With $u = \tfrac{\mu}{h^2}(1 + e\cos\theta)$, $u' = -\tfrac{\mu}{h^2}e\sin\theta$, and the energy of §7.4, $\xi = \tfrac{1}{2}h^2[(u')^2 + u^2] - \mu u$:
$$ \xi = \frac{\mu^2}{2h^2}\left[e^2\sin^2\theta + (1 + e\cos\theta)^2\right] - \frac{\mu^2}{h^2}(1 + e\cos\theta) = \frac{\mu^2}{2h^2}\left(e^2 - 1\right) = -\frac{\mu}{2a} $$
where the last step uses $h^2 = \mu a(1 - e^2)$. The energy is the same at every point of the orbit and independent of $\theta$.

We obtain the fundamental relation between specific orbital energy and semi-major axis (Notes Eq. 8.19):
$$ \xi = -\frac{\mu}{2a} $$

### 10.3 The Vis-Viva Equation (Notes Eq. 8.19)
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

### 11.1 Circular Velocity ($v_c$) (Notes Eq. 8.20)
For a circular orbit of radius $r = a$:
$$ v_c = \sqrt{\mu\left(\frac{2}{r} - \frac{1}{r}\right)} = \sqrt{\frac{\mu}{r}} = \sqrt{\frac{\mu}{a}} $$
*Circular speed decreases monotonically with orbital altitude ($v_c \propto 1/\sqrt{r}$).*

### 11.2 Escape Velocity ($v_e$) (Notes Eq. 8.21)
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
but the true 3D trajectory is a **circle**. Indeed,
$$ x^2 + y^2 + \left(z + \frac{g}{k^2}\right)^2 = \left(\frac{g}{k^2}\right)^2\left[3\cos^2(kt) + 4\sin^2(kt) + \cos^2(kt)\right] = \frac{4g^2}{k^4}, $$
so the path lies on a sphere of radius $2g/k^2$ centred at $(0, 0, -g/k^2)$. The plane $x - \sqrt{3}z = \sqrt{3}g/k^2$ passes through this centre (distance $|0 + \sqrt{3}g/k^2 - \sqrt{3}g/k^2|/2 = 0$), hence the path is a great circle of radius $R = 2g/k^2$, run at angular rate $k$. The plane contains the direction $(\sqrt{3}, 0, 1)$, so it is inclined $30^\circ$ to the horizontal (official key: Problems.pdf, PDF page 73).

#### Step 6: Velocity Vector as a Function of Time
Differentiating $\mathbf{r}(t)$:
$$ \mathbf{v}(t) = \dot{x}(t)\mathbf{i} + \dot{y}(t)\mathbf{j} + \dot{z}(t)\mathbf{k} $$
$$ \mathbf{v}(t) = -\frac{\sqrt{3}g}{k}\sin(kt)\,\mathbf{i} + \frac{2g}{k}\cos(kt)\,\mathbf{j} - \frac{g}{k}\sin(kt)\,\mathbf{k} $$
Velocity magnitude squared:
$$ v^2(t) = \frac{g^2}{k^2}\left(3\sin^2(kt) + 4\cos^2(kt) + \sin^2(kt)\right) = \frac{g^2}{k^2}\left(4\sin^2(kt) + 4\cos^2(kt)\right) = \frac{4g^2}{k^2} $$
Remarkably, the **speed of the particle is constant**:
$$ v(t) = \frac{2g}{k} = \text{constant} $$

---

## 🧩 13. Other Worked Problems of this Topic
* **Problem 39** (string over a plate edge): moving basis $\{\hat{\mathbf{u}}, \mathbf{e}_\theta, \mathbf{e}_\phi\}$, equations of motion, tension power and energy.
* **Problem 42** (force $m\mu/r^\alpha$): Binet equation in general and the effective-potential discussion for $\alpha = 1, 2, 3, 4$.
* **Problem 43** (two particles through a hole): angular momentum plus energy reduction to quadratures.
* **Problem 44** (seed on an asteroid): angular momentum and energy between launch and apocenter.

All are solved in [[Solutions - Topic 4 Angular Momentum and Central Forces]]; the statements are in [[Problems - Topic 4 Angular Momentum and Central Forces]].

---

## 📚 Pedagogical Summary & Study Guidelines
1. **Always check torque:** If $\mathbf{M}_O = \mathbf{0}$, $\mathbf{H}_O$ is conserved $\implies$ the motion is planar.
2. **Polar coordinates are natural:** For any central force, $h = r^2\dot{\theta}$ is the first integral of motion.
3. **Binet variable $u = 1/r$ transforms nonlinear orbital kinematics into a linear oscillator.**
4. **Vis-Viva equation connects speed, position, and orbital semi-major axis without integrating time laws.**
