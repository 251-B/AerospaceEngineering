---
materia: Fluid Mechanics
tema: "Topic 2: Flow Kinematics"
tags:
  - theory
  - key-concept
  - vector-calculus
  - kinematics
dificultad: medium
prerrequisitos: []
---

# 📐 Concept: Orthogonal Curvilinear Coordinates and Differential Operators

> **Key idea in one sentence:** Metric scale factors $(h_1, h_2, h_3)$ make it possible to unify and formulate invariantly the differential operators of vector calculus (gradient, divergence, curl, Laplacian and tensor derivatives) in Cartesian, cylindrical and spherical systems.

---

## 🎯 1. Physical and Geometric Foundation

In fluid mechanics, the geometry of the flow or of the confining bodies (pipes, rocket nozzles, airfoils, oscillating droplets) determines the convenience of adopting orthogonal coordinate systems adapted to the symmetry of the problem:
* **Cartesian $(x, y, z)$:** Planar two-dimensional flows, straight channels, flat boundary layers.
* **Cylindrical $(r, \theta, z)$:** Circular pipes, vortices, axisymmetric jets, turbomachinery rotors.
* **Spherical $(r, \theta, \phi)$:** Flow around droplets, bubbles or spherical bodies in slow (Stokes) regime, spherical acoustic waves.

---

## 📐 2. Rigorous Mathematical Formulation and Scale Factors

We consider a local orthonormal basis $(\vec{e}_1, \vec{e}_2, \vec{e}_3)$ at each point of space. The differential position displacement vector is expressed as:

$$ d\vec{x} = h_1 dx_1 \vec{e}_1 + h_2 dx_2 \vec{e}_2 + h_3 dx_3 \vec{e}_3 $$

where the metric coefficients $(h_1, h_2, h_3)$ are the **scale factors**:

| Coordinate System | Coordinates $(x_1, x_2, x_3)$ | Scale Factors $(h_1, h_2, h_3)$ | Differential Line Element $d\vec{x}$ |
| :--- | :--- | :--- | :--- |
| **Cartesian** | $(x, y, z)$ | $(1, 1, 1)$ | $(dx, dy, dz)$ |
| **Cylindrical** | $(r, \theta, z)$ | $(1, r, 1)$ | $(dr, r d\theta, dz)$ |
| **Spherical** | $(r, \theta, \phi)$ | $(1, r, r\sin\theta)$ | $(dr, r d\theta, r\sin\theta d\phi)$ |

Defining the metric determinant $h = h_1 h_2 h_3$, the volume differential is $dV = h_1 h_2 h_3 dx_1 dx_2 dx_3 = h dx_1 dx_2 dx_3$.

---

## 🔍 3. Differential Operators in General Coordinates (Notes.pdf, Eqs. 2.3–2.8)

### 1. Gradient of a Scalar Field $\Phi$ (Vector)
$$ \nabla\Phi = \left( \frac{1}{h_1}\frac{\partial \Phi}{\partial x_1}, \, \frac{1}{h_2}\frac{\partial \Phi}{\partial x_2}, \, \frac{1}{h_3}\frac{\partial \Phi}{\partial x_3} \right) \qquad \text{[Eq. 2.3]} $$

### 2. Laplacian of a Scalar Field $\Phi$ (Scalar)
$$ \nabla^2\Phi = \frac{1}{h_1 h_2 h_3} \left[ \frac{\partial}{\partial x_1}\left(\frac{h_2 h_3}{h_1}\frac{\partial \Phi}{\partial x_1}\right) + \frac{\partial}{\partial x_2}\left(\frac{h_1 h_3}{h_2}\frac{\partial \Phi}{\partial x_2}\right) + \frac{\partial}{\partial x_3}\left(\frac{h_1 h_2}{h_3}\frac{\partial \Phi}{\partial x_3}\right) \right] \qquad \text{[Eq. 2.4]} $$

### 3. Divergence of a Vector Field $\vec{a} = \sum_i a_i \vec{e}_i$ (Scalar)
$$ \nabla \cdot \vec{a} = \frac{1}{h_1 h_2 h_3} \left[ \frac{\partial}{\partial x_1}(h_2 h_3 a_1) + \frac{\partial}{\partial x_2}(h_1 h_3 a_2) + \frac{\partial}{\partial x_3}(h_1 h_2 a_3) \right] \qquad \text{[Eq. 2.5]} $$

### 4. Curl of a Vector Field $\vec{a}$ (Vector)
$$ \nabla \wedge \vec{a} = \frac{1}{h_1 h_2 h_3} \begin{vmatrix} h_1 \vec{e}_1 & h_2 \vec{e}_2 & h_3 \vec{e}_3 \\ \frac{\partial}{\partial x_1} & \frac{\partial}{\partial x_2} & \frac{\partial}{\partial x_3} \\ h_1 a_1 & h_2 a_2 & h_3 a_3 \end{vmatrix} \qquad \text{[Eq. 2.6]} $$

Expanded into components:
$$ (\nabla \wedge \vec{a})_1 = \frac{1}{h_2 h_3}\left[ \frac{\partial(h_3 a_3)}{\partial x_2} - \frac{\partial(h_2 a_2)}{\partial x_3} \right] $$
$$ (\nabla \wedge \vec{a})_2 = \frac{1}{h_1 h_3}\left[ \frac{\partial(h_1 a_1)}{\partial x_3} - \frac{\partial(h_3 a_3)}{\partial x_1} \right] $$
$$ (\nabla \wedge \vec{a})_3 = \frac{1}{h_1 h_2}\left[ \frac{\partial(h_2 a_2)}{\partial x_1} - \frac{\partial(h_1 a_1)}{\partial x_2} \right] $$

### 5. Gradient of a Vector Field (Second-Order Tensor)
$$ (\nabla\vec{a})_{ii} = \frac{1}{h_i}\frac{\partial a_i}{\partial x_i} + \sum_{k \neq i} \frac{a_k}{h_i h_k}\frac{\partial h_i}{\partial x_k} \qquad \text{[Eq. 2.7a]} $$
$$ (\nabla\vec{a})_{ij} = \frac{1}{h_i}\frac{\partial a_j}{\partial x_i} - \frac{a_i}{h_i h_j}\frac{\partial h_i}{\partial x_j} \quad (i \neq j) \qquad \text{[Eq. 2.7b]} $$

### 6. Divergence of a Second-Order Tensor $\bar{\bar{A}}$ (Vector)
$$ (\nabla \cdot \bar{\bar{A}})_i = \frac{h_i}{h}\sum_j \frac{\partial}{\partial x_j}\left( \frac{h A_{ij}}{h_i h_j} \right) + \sum_j \frac{A_{ij} + A_{ji}}{h_i h_j}\frac{\partial h_i}{\partial x_j} - \sum_j \frac{A_{jj}}{h_i h_j}\frac{\partial h_j}{\partial x_i} \qquad \text{[Eq. 2.8]} $$

---

## ⚠️ 4. Typical Exam Mistakes

> [!WARNING] Beware of the Derivatives of Unit Vectors
> In curvilinear coordinates (cylindrical and spherical), the basis vectors $\vec{e}_r, \vec{e}_\theta, \vec{e}_\phi$ **change direction with position**. A vector cannot be differentiated component by component as in Cartesian coordinates. For example, in cylindrical coordinates:
> $$ \frac{\partial \vec{e}_r}{\partial \theta} = \vec{e}_\theta, \qquad \frac{\partial \vec{e}_\theta}{\partial \theta} = -\vec{e}_r $$
> Omitting these terms when computing accelerations or tensor divergences is the most frequent mistake in exams.

---

## 🔗 Related Concepts
* [[01 - Fluid Mechanics/Topic 2 - Flow Kinematics|Topic 2: Flow Kinematics]]
* [[01 - Fluid Mechanics/Concept - Material Derivative and Fluid Acceleration|Concept: Material Derivative and Acceleration]]
