---
title: "Formula Sheet: Topic 3 Constraints and Reaction Forces"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
ground_truth: "slides/03_-_Constraints (1).pdf & teoria/Notes.pdf (Chapter 6)"
tier: "Formula Sheet"
language: "English"
---

# 📑 Formula Sheet: Topic 3 Constraints and Reaction Forces

## 1. Degrees of Freedom & Manifold Dimensions

| Constraint Type | Defining Equations | CDOF | $\dim(V_N)$ | $\dim(V_T)$ | Unknown Reactions |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Free 3D Particle** | None | $3$ | $0$ | $3$ | $0$ |
| **Surface (2-Manifold)** | $f(x, y, z) = 0$ | $2$ | $1$ | $2$ | $1$ ($N_1$) |
| **Curve (1-Manifold)** | $f(x, y, z) = 0, \; g(x, y, z) = 0$ | $1$ | $2$ | $1$ | $2$ ($N_1, N_2$) |

---

## 2. Tangent and Normal Subspace Vectors

### 2.1 Surface Vectors
* **Normal from Implicit:** $\mathbf{n} = \nabla f = \frac{\partial f}{\partial x}\mathbf{i}_0 + \frac{\partial f}{\partial y}\mathbf{j}_0 + \frac{\partial f}{\partial z}\mathbf{k}_0$
* **Unit Normal:** $\mathbf{e}_n = \frac{\nabla f}{\|\nabla f\|}$
* **Tangents from Parametric:** $\mathbf{t}_\alpha = \frac{\partial\mathbf{r}}{\partial\alpha}, \quad \mathbf{t}_\beta = \frac{\partial\mathbf{r}}{\partial\beta}$
* **Normal from Tangents:** $\mathbf{n} = \mathbf{t}_\alpha \times \mathbf{t}_\beta$

### 2.2 Curve Vectors
* **Tangent from Parametric:** $\mathbf{t} = \frac{d\mathbf{r}}{d\alpha} = \frac{dx}{d\alpha}\mathbf{i}_0 + \frac{dy}{d\alpha}\mathbf{j}_0 + \frac{dz}{d\alpha}\mathbf{k}_0$
* **Normals from Implicit:** $\mathbf{n}_f = \nabla f, \quad \mathbf{n}_g = \nabla g$
* **Tangent from Normals:** $\mathbf{t} = \mathbf{n}_f \times \mathbf{n}_g = \nabla f \times \nabla g$

---

## 3. Dynamic Equations and Decoupling

* **Newton's Second Law:**
  $$ m_P\,\mathbf{a}_0^P = \mathbf{F}_{\text{applied}} + \mathbf{N} $$
* **Reaction Force Representation:**
  * Surface: $\mathbf{N} = N_1\,\mathbf{n}$
  * Curve: $\mathbf{N} = N_1\,\mathbf{n}_f + N_2\,\mathbf{n}_g$
* **Tangential Projection (Isolates Generalized Coordinates):**
  $$ m_P\,\mathbf{a}_0^P \cdot \mathbf{t} = \mathbf{F}_{\text{applied}} \cdot \mathbf{t} \quad (\text{since } \mathbf{N} \cdot \mathbf{t} \equiv 0) $$
* **Normal Projection (Determines Reactions):**
  $$ m_P\,\mathbf{a}_0^P \cdot \mathbf{n} = (\mathbf{F}_{\text{applied}} + \mathbf{N}) \cdot \mathbf{n} $$

---

## 4. Power, Work, and Energy Conservation

* **Instantaneous Power:** $P_N = \mathbf{N} \cdot \mathbf{v}_0^P$
* **Scleronomic Theorem:** For stationary constraints ($\frac{\partial f}{\partial t} = 0$):
  $$ \mathbf{v}_0^P \in V_T \perp \mathbf{N} \in V_N \implies P_N \equiv 0, \quad W_N \equiv 0 $$
* **Mechanical Energy Conservation:** If applied forces are conservative:
  $$ E_0 = T_0 + V_0 = \text{constant} $$

---

## 5. Coulomb Friction Model

* **Dynamic Friction ($\mathbf{v}_P^* \neq \mathbf{0}$):** Applied Force
  $$ \mathbf{F}_R = -\mu N\,\frac{\mathbf{v}_P^*}{\|\mathbf{v}_P^*\|}, \quad P_R = -\mu N v_P^* < 0 $$
* **Static Friction ($\mathbf{v}_P^* = \mathbf{0}$):** Constraint Force in $V_T$
  $$ \mathbf{F}_R \in V_T, \quad \|\mathbf{F}_R\| \le \mu N, \quad P_R \equiv 0 $$
* **Slip Threshold:** $\|\mathbf{F}_R\| = \mu N$

---

## 6. Classification of Constraints

* **Holonomic:** $f(\mathbf{r}, t) = 0$ (Reduces CDOFs by 1)
* **Non-Holonomic:** $\sum A_i \dot{x}_i + B = 0$ (Cannot eliminate coordinates)
* **Scleronomic:** $\frac{\partial f}{\partial t} = 0 \implies W_N \equiv 0$
* **Rheonomic:** $\frac{\partial f}{\partial t} \neq 0 \implies W_N \neq 0$
* **Unilateral:** $f \ge 0, N \ge 0 \implies \text{Liftoff at } N = 0$
* **Simple Constraint:** Holonomic + Scleronomic + Bilateral
