---
subject: Mechanics Applied to Aerospace Engineering
topic: 2 - Point Particle Dynamics
concept: Newton's Laws and Equations of Motion
tags:
  - concept
  - newton-laws
  - inertial-frames
  - equations-of-motion
---

# Concept: Newton's Laws of Motion and Equations of Motion

## 1. Context and Physical Significance
Newton's three laws of motion (1687) form the foundational axiomatic framework of classical Newtonian mechanics:
* They are valid exclusively in **inertial reference frames** (frames in which a free particle undergoes zero acceleration).
* They relate the forces acting on a body to the resulting acceleration and momentum time evolution.

---

## 2. Mathematical Formulation

### 2.1 First Law (Law of Inertia)
$$ \sum \mathbf{F} = \mathbf{0} \implies \mathbf{p}_0 = \text{constant} \implies \mathbf{v}_0^P = \text{constant} $$
A particle maintains its state of rest or constant rectilinear velocity unless acted upon by a non-zero net external force.

### 2.2 Second Law (Fundamental Law of Dynamics)
$$ \mathbf{F} = \left.\frac{d\mathbf{p}_0}{dt}\right|_0 = m_P\,\mathbf{a}_0^P $$
For a particle of constant mass $m_P$, the net force vector equals the product of mass and absolute acceleration.

### 2.3 Third Law (Action and Reaction)
$$ \mathbf{F}_{PQ} = -\mathbf{F}_{QP} $$
Forces between two particles $P$ and $Q$ are mutual, equal in magnitude, opposite in direction, and collinear with the line joining $P$ and $Q$.

---

## 3. Projection and Initial Value Problem
Projecting the vector equation $\mathbf{F} = m_P\mathbf{a}_0^P$ into Cartesian coordinates:
$$ \begin{cases}
m_P\,\ddot{x} = F_x(t, x, y, z, \dot{x}, \dot{y}, \dot{z}) \\
m_P\,\ddot{y} = F_y(t, x, y, z, \dot{x}, \dot{y}, \dot{z}) \\
m_P\,\ddot{z} = F_z(t, x, y, z, \dot{x}, \dot{y}, \dot{z})
\end{cases} $$
Equivalent state-space system of 6 first-order ODEs:
$$ \dot{\mathbf{x}} = \mathbf{v}, \quad \dot{\mathbf{v}} = \frac{1}{m_P}\mathbf{F} $$
The unique solution requires specifying 6 initial conditions: position $\mathbf{r}_0^P(0)$ and velocity $\mathbf{v}_0^P(0)$.
