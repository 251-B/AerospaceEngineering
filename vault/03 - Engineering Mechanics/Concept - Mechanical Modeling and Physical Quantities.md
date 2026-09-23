---
subject: Mechanics Applied to Aerospace Engineering
topic: 1 - Fundamentals and Particle Kinematics
tags:
  - theory
  - key-concept
  - mechanical-modeling
  - physical-quantities
difficulty: low
prerequisites:
  - "Linear Algebra"
  - "Physics I"
---

# 📖 Concept: Mechanical Modeling and Physical Quantities

> **Key Takeaway in One Sentence:** Classical mechanics does not attempt to solve physical reality directly, but operates on an idealized mathematical model (point particle or rigid body) described by physical quantities (scalars, free/sliding/bound vectors, and tensors) whose intrinsic meaning is strictly invariant under coordinate and observer changes.

---

## 🎯 1. Physical Principle and Intuition

In Aerospace Engineering, all analytical modeling starts with an abstraction:
1. **Point Particle:** An idealization where an object's spatial dimensions are negligible relative to the scale of its motion. Orientation and internal deformation are ignored; only translational motion is tracked ($3$ degrees of freedom in $\mathbb{R}^3$).
   * *Aerospace Example:* A satellite in Low Earth Orbit (LEO) or a commercial aircraft along an airway route.
2. **Rigid Body:** A body with finite geometry where distances between all pairs of internal points remain invariant over time ($\|\mathbf{r}^{P_i} - \mathbf{r}^{P_j}\| = \text{const}$). Tracking requires both position and **spatial attitude** ($6$ degrees of freedom in free 3D space).
   * *Aerospace Example:* An aircraft during pitch, yaw, and roll attitude control, or a spacecraft during docking alignment.
3. **Deformable Bodies:** Bodies where internal strains and elastic deflections (e.g. wing flutter) cannot be neglected.

---

## 📐 2. Classification of Physical Quantities

### 2.1 Tensorial Order
* **Scalars (Order 0):** A single real number accompanied by its physical unit ($m$ $[\text{kg}]$, $t$ $[\text{s}]$, $E$ $[\text{J}]$).
* **Vectors (Order 1):** Elements of $\mathbb{R}^3$ with magnitude, direction, sense, and units. Denoted in boldface: $\mathbf{v}, \mathbf{a}, \mathbf{F}$. Speed or norm is denoted in standard typeface: $v = \|\mathbf{v}\|$.
* **Second-Order Tensors (Order 2):** Linear operators mapping vectors to vectors, represented as $3 \times 3$ matrices in a basis $\mathcal{B} \otimes \mathcal{B}$. The primary mechanical example is the **inertia tensor** $\bar{\bar{I}}_0$, which maps angular velocity to angular momentum: $\mathbf{H}_0 = \bar{\bar{I}}_0 \cdot \boldsymbol{\omega}$.

### 2.2 Physical Classification of Vectors by Application Point
| Vector Class | Parallel Translation Property | Aerospace Examples |
| :--- | :--- | :--- |
| **Free Vector** | Can be translated anywhere in space without altering its physical effect. | Angular velocity $\boldsymbol{\omega}$, pure torque couple $\mathbf{M}$. |
| **Sliding Vector** | Can be translated along its **line of action** without altering its effect on a rigid body. | External force $\mathbf{F}$ applied to a rigid body (Principle of Transmissibility). |
| **Bound Vector** | Bound to a specific application point; shifting its origin changes the physical problem. | Position vector $\mathbf{r}_0^P = \vec{OP}$, or concentrated load on a deformable elastic wing skin. |

---

## 🔍 3. The Observer Invariance Principle

> [!IMPORTANT] Invariance of Physical Laws
> Physical quantities exist in nature independently of any coordinate system or basis. While component arrays change when rotating bases ($\mathcal{B}_0 \to \mathcal{B}_1$), the geometric vector entity remains invariant:
> $$ \mathbf{A} = A_{x0}\mathbf{i}_0 + A_{y0}\mathbf{j}_0 + A_{z0}\mathbf{k}_0 = A_{x1}\mathbf{i}_1 + A_{y1}\mathbf{j}_1 + A_{z1}\mathbf{k}_1 $$

---

## ⚠️ 4. Common Exam Pitfalls
> [!WARNING] Exam Precautions
> 1. Confusing a vector with its scalar magnitude: Writing $v = \dot{x}\mathbf{i} + \dot{y}\mathbf{j}$ instead of $\mathbf{v}$ (or mixing up vector velocity $\mathbf{v}$ and scalar speed $v = \|\mathbf{v}\|$) is considered a severe error at UC3M.
> 2. Treating a concentrated load on an elastic or deformable structure as a sliding vector: in elasticity, moving the point of load application fundamentally alters internal stresses.

---

## 🔗 Related Concepts
* `[[Topic 1 - Fundamentals and Particle Kinematics|Topic 1: Fundamentals and Particle Kinematics]]`
* `[[Concept - Vector Bases Rotation Matrices and Poisson Theorem|Concept: Vector Bases, Rotation Matrices, and Poisson's Theorem]]`
