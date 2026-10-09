---
materia: Fluid Mechanics
tema: "Topic 2: Flow Kinematics"
tags:
  - theory
  - key-concept
  - euler-lagrange
  - streamlines
dificultad: medium
prerrequisitos: []
---

# 🌀 Concept: Eulerian and Lagrangian Descriptions and Flow Lines

> **Key idea in one sentence:** Fluid kinematics distinguishes between following discrete particles on their journey through time (Lagrangian approach) and observing the continuous velocity field at fixed points of space (Eulerian approach), giving rise to three geometric families of lines: pathlines, streamlines and streaklines.

---

## 🎯 1. Fundamentals: Eulerian vs Lagrangian Description

### A. Lagrangian Description
It treats the fluid as a collection of individual particles identified by their initial position $\vec{x}_0$ at time $t_0$. The motion is described by the trajectory function:

$$ \vec{x} = \vec{x}_T(\vec{x}_0, t) \qquad \text{[Eq. 2.10]} $$

Velocity and acceleration are obtained by direct time differentiation keeping $\vec{x}_0$ constant:
$$ \vec{v} = \frac{\partial \vec{x}_T}{\partial t}, \qquad \vec{a} = \frac{\partial^2 \vec{x}_T}{\partial t^2} $$
*Usefulness:* Analysis of dispersed phases (fuel droplets in injectors, volcanic dust/ash particles in turbines).  
*Drawback:* It leads to complex integro-differential formulations of the conservation laws of the continuum.

### B. Eulerian Description (Official Approach of Fluid Mechanics)
It describes the state of the flow at fixed points of space $\vec{x}$ at each instant $t$, treating the velocity as a continuous vector field:

$$ \vec{v} = \vec{v}(\vec{x}, t) $$

---

## 📍 2. Fundamental Classification of Flows

* **Uniform flow:** Invariant in space at a given instant: $\nabla\vec{v} = 0 \implies \vec{v} = \vec{v}(t)$.
* **Steady flow:** Invariant in time at each spatial point: $\frac{\partial\vec{v}}{\partial t} = 0 \implies \vec{v} = \vec{v}(\vec{x})$.
* **Observer relativity:** Steadiness depends on the reference frame. For an aircraft flying at constant velocity $\vec{V}_\infty$, the flow is unsteady for an observer fixed to the ground ($\vec{v}(\vec{x}, t)$), but steady for the pilot or in a wind tunnel ($\vec{v}(\vec{x})$).
* **Stagnation point:** Point of space where the velocity vanishes simultaneously in all three components:
  $$ \vec{v}(\vec{x}, t) = 0 \qquad \text{[Eq. 2.11]} $$

---

## 📐 3. Geometric Families of Flow Lines and Surfaces

### 1. Trajectories and Pathlines
This is the locus described by a specific fluid particle over time. Given the Eulerian field $\vec{v}(\vec{x}, t)$, the trajectory is found by solving the Cauchy (initial value) problem:

$$ \frac{d\vec{x}}{dt} = \vec{v}(\vec{x}, t), \quad \text{with } \vec{x}(t_0) = \vec{x}_0 \qquad \text{[Eq. 2.12]} $$

In general curvilinear coordinates $(h_1, h_2, h_3)$:
$$ dt = \frac{h_1 dx_1}{v_1} = \frac{h_2 dx_2}{v_2} = \frac{h_3 dx_3}{v_3} \qquad \text{[Eq. 2.13]} $$
The trajectory $\vec{x} = \vec{x}_T(\vec{x}_0, t)$ contains positional and temporal information (the rate at which the particle travels). Eliminating the time parameter $t$ yields the **pathlines** as the intersection of two implicit surfaces:
$$ f(\vec{x}_0, \vec{x}) = 0 \quad \text{and} \quad g(\vec{x}_0, \vec{x}) = 0 \qquad \text{[Eq. 2.15]} $$

### 2. Fluid Lines, Surfaces and Volumes
* **Fluid line:** Set of fluid particles that form a curve $\vec{x}_l(\lambda)$ at $t_0$. At any later instant they will continue to form a fluid line $\vec{x} = \vec{x}_T(\vec{x}_l(\lambda), t)$ (Eq. 2.17).
* **Fluid surface:** Surface $f(\vec{x}, t) = 0$ always composed of the same fluid particles. Since particles never leave it, the surface satisfies the **kinematic condition of a fluid surface**:
  $$ \frac{Df}{Dt} = \frac{\partial f}{\partial t} + \vec{v} \cdot \nabla f = 0 $$
* **Fluid volume:** Finite volume bounded by a closed fluid surface. **No mass can cross a fluid surface**; therefore, the mass of a fluid volume is strictly constant in time:
  $$ \frac{d}{dt}\int_{V_f(t)} \rho \, dV = 0 \quad \text{(First conservation principle)} $$

### 3. Streamlines, Stream Surfaces and Stream Tubes
These are the curves tangent at each point to the instantaneous velocity vector at a fixed ("frozen") time $t$:

$$ d\vec{x} \wedge \vec{v} = 0 \iff \frac{h_1 dx_1}{v_1(\vec{x}, t)} = \frac{h_2 dx_2}{v_2(\vec{x}, t)} = \frac{h_3 dx_3}{v_3(\vec{x}, t)} \qquad \text{[Eq. 2.21]} $$

* In Cartesian coordinates: $\frac{dx}{v_x} = \frac{dy}{v_y} = \frac{dz}{v_z}$.
* In cylindrical coordinates: $\frac{dr}{v_r} = \frac{r d\theta}{v_\theta} = \frac{dz}{v_z}$.
* In spherical coordinates: $\frac{dr}{v_r} = \frac{r d\theta}{v_\theta} = \frac{r\sin\theta d\phi}{v_\phi}$.

* **Stream surface:** Ruled surface formed by all the streamlines resting on a directrix. Since $\vec{v}$ is tangent to it at every point, the convective mass flux through a stream surface is identically zero:
  $$ \vec{v} \cdot \vec{n} = 0 $$
* **Stream tube:** Closed stream surface generated from a closed directrix curve.

---

## 🔍 4. Crucial Comparison: When Do Pathlines and Streamlines Coincide?

| Feature | Pathline | Streamline |
| :--- | :--- | :--- |
| **Mathematical concept** | Cauchy problem of time evolution ($t$ is the integration variable). | Family of instantaneous spatial curves ($t$ acts as a frozen parameter). |
| **Experimental visualisation** | Long-exposure photograph of an illuminated tracer particle. | Instantaneous field of tangent vectors obtained with PIV anemometry. |

### Coincidence Theorem (Notes.pdf, p. 13)
Pathlines and streamlines **coincide** in two fundamental cases:
1. **Strictly steady flow:** $\vec{v} = \vec{v}(\vec{x})$.
2. **Flow of time-invariant direction:** $\vec{v}(\vec{x}, t) = f(t) \vec{V}(\vec{x})$, where the velocity magnitude varies with time but its spatial orientation remains frozen.

> [!NOTE] Intersection of Streamlines
> Two streamlines corresponding to the same instant $t$ **can only cross at a stagnation point** ($\vec{v} = 0$), since otherwise the velocity vector would have two different directions at a single spatial point, violating the continuity and single-valuedness of the velocity field.

---

## 🔗 Related Concepts
* [[01 - Fluid Mechanics/Topic 2 - Flow Kinematics|Topic 2: Flow Kinematics]]
* [[01 - Fluid Mechanics/Concept - Material Derivative and Fluid Acceleration|Concept: Material Derivative and Acceleration]]
* [[01 - Fluid Mechanics/Concept - Convective Flux and Stream Function|Concept: Stream Function]]
