---
subject: Mechanics Applied to Aerospace Engineering
topic: 1 - Fundamentals and Particle Kinematics
tags:
  - theory
  - key-concept
  - degrees-of-freedom
  - generalized-coordinates
  - constraints
difficulty: medium
prerequisites:
  - "Linear Algebra"
  - "Multivariable Calculus"
---

# 📖 Concept: Configuration Degrees of Freedom, Generalized Coordinates, and Constraints

> **Key Takeaway in One Sentence:** Configuration degrees of freedom represent the minimum number of independent coordinates needed to uniquely define the configuration of a mechanical system; geometric constraints diminish degrees of freedom and introduce unknown reaction forces.

---

## 🎯 1. Physical Principle and Intuition

A free point particle in 3D Euclidean space can displace along three independent directions ($x, y, z$), possessing **$3$ degrees of freedom**.

In mechanical systems, physical constraints restrict the freedom of motion:
* A bead sliding along a curved wire ($1$ DOF).
* A roller constrained to stay on a track or surface ($2$ DOF).
* Masses linked by inextensible cables or rigid links.

---

## 📐 2. Counting Rule for Degrees of Freedom

For a system of $N$ point particles subject to $k$ independent holonomic (geometric) constraints:
$$ \text{DOF} = 3N - k $$

| Mechanical System | Space Dimension | Constraint Equations | Configuration DOF | Ideal Generalized Coordinates |
| :--- | :--- | :--- | :--- | :--- |
| **Free particle in 3D space** | $\mathbb{R}^3$ ($3$) | None ($0$) | **3** | Cartesian $\{x, y, z\}$ or Spherical $\{r, \theta, \phi\}$ |
| **Particle on a surface** | $\mathbb{R}^3$ ($3$) | $f(x,y,z) = 0$ ($1$) | **2** | Surface parameters $(\alpha, \beta)$ or $\{R, \theta\}$ |
| **Particle on a wire / curve** | $\mathbb{R}^3$ ($3$) | $f=0, \; g=0$ ($2$) | **1** | Arc length coordinate $s$ or angle $\theta$ |
| **Free Rigid Body in 3D space** | $\mathbb{R}^3$ | Rigidity condition | **6** | 3 CM position coords $(x_G, y_G, z_G)$ + 3 Euler angles $(\psi, \theta, \phi)$ |

---

## 🔍 3. Generalized Coordinates and Configuration Space

* **Generalized Coordinates ($q_1, q_2, \dots, q_n$):** Any set of $n$ independent scalar parameters that uniquely describe the configuration of the mechanical system while automatically fulfilling all holonomic constraints.
* **Configuration Space:** The $n$-dimensional manifold formed by all permissible values of the generalized coordinates.

---

## ⚠️ 4. Common Exam Pitfalls
> [!WARNING] Exam Precautions
> 1. Introducing more coordinates than effective degrees of freedom without stating the corresponding constraint equations, resulting in underdetermined systems.
> 2. Using dependent or redundant coordinates (e.g., using both height $z$ and slope length $s$ on an inclined plane without specifying $z = s\sin\alpha$).

---

## 🔗 Related Concepts
* `[[Topic 1 - Fundamentals and Particle Kinematics|Topic 1: Fundamentals and Particle Kinematics]]`
