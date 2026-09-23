---
title: "Concept: Normal and Tangent Subspaces for Surfaces and Curves"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
ground_truth: "slides/03_-_Constraints (1).pdf (Slides 7–12) & teoria/Notes.pdf (Section 6.3)"
tier: "Atomic Concept Note"
language: "English"
---

# 📐 Concept: Normal and Tangent Subspaces for Surfaces and Curves

## 1. Direct Sum Decomposition of 3D Space

At every regular point $P$ of a smooth constraint manifold embedded in Euclidean space $\mathbb{R}^3$, the vector space decomposes into the direct sum of two mutually orthogonal subspaces (Slides 7–8):
$$ \mathbb{R}^3 = V_N \oplus V_T, \quad \text{with} \quad V_N \cap V_T = \{\mathbf{0}\} $$
where:
* $V_N$ is the **Normal Vector Subspace**.
* $V_T$ is the **Tangent Vector Subspace**.
* $\dim(V_N) + \dim(V_T) = 3$.

---

## 2. Geometry on a Surface (2D Manifold)

A surface constraint restricts motion to two spatial dimensions:
$$ \dim(V_N) = 1, \quad \dim(V_T) = 2 $$

### 2.1 Normal Subspace $V_N$
* A normal vector $\mathbf{n} \in V_N$ is obtained directly by taking the gradient of the surface's implicit equation $f(x, y, z) = 0$:
  $$ \mathbf{n} = \nabla f = \frac{\partial f}{\partial x}\mathbf{i}_0 + \frac{\partial f}{\partial y}\mathbf{j}_0 + \frac{\partial f}{\partial z}\mathbf{k}_0 $$
* Unit normal vector:
  $$ \mathbf{e}_n = \frac{\nabla f}{\|\nabla f\|} $$

### 2.2 Tangent Subspace $V_T$
* Two independent tangent vectors $\mathbf{t}_\alpha, \mathbf{t}_\beta \in V_T$ are obtained by differentiating the parametric position vector $\mathbf{r}(\alpha, \beta)$ with respect to generalized coordinates $\alpha$ and $\beta$:
  $$ \mathbf{t}_\alpha = \frac{\partial\mathbf{r}}{\partial\alpha} = \frac{\partial x}{\partial\alpha}\mathbf{i}_0 + \frac{\partial y}{\partial\alpha}\mathbf{j}_0 + \frac{\partial z}{\partial\alpha}\mathbf{k}_0 $$
  $$ \mathbf{t}_\beta = \frac{\partial\mathbf{r}}{\partial\beta} = \frac{\partial x}{\partial\beta}\mathbf{i}_0 + \frac{\partial y}{\partial\beta}\mathbf{j}_0 + \frac{\partial z}{\partial\beta}\mathbf{k}_0 $$
* **Normal from Tangent Vectors:** A normal vector is also given by the cross product:
  $$ \mathbf{n} = \mathbf{t}_\alpha \times \mathbf{t}_\beta $$
* **Local Basis:** $\mathcal{B}_P = \{\mathbf{t}_\alpha, \mathbf{t}_\beta, \mathbf{n}\}$ forms a local basis at point $P$.

---

## 3. Geometry on a Curve (1D Manifold)

A curve constraint restricts motion to a single spatial trajectory:
$$ \dim(V_N) = 2, \quad \dim(V_T) = 1 $$

### 3.1 Tangent Subspace $V_T$
* A tangent vector $\mathbf{t} \in V_T$ is obtained by differentiating the parametric curve $\mathbf{r}(\alpha)$ with respect to parameter $\alpha$:
  $$ \mathbf{t} = \frac{d\mathbf{r}}{d\alpha} = \frac{dx}{d\alpha}\mathbf{i}_0 + \frac{dy}{d\alpha}\mathbf{j}_0 + \frac{dz}{d\alpha}\mathbf{k}_0 $$
* If parameter $\alpha$ is chosen as the arc length $s$, then $\mathbf{t}$ is the unit tangent vector $\mathbf{e}_t$ of the Frenet-Serret frame.

### 3.2 Normal Subspace $V_N$
* Two independent normal vectors $\mathbf{n}_f, \mathbf{n}_g \in V_N$ are obtained from the gradients of the two implicit surfaces defining the curve ($f=0$ and $g=0$):
  $$ \mathbf{n}_f = \nabla f, \quad \mathbf{n}_g = \nabla g $$
* **Tangent from Normal Vectors:** The tangent direction is collinear with the cross product of the gradients:
  $$ \mathbf{t} = \mathbf{n}_f \times \mathbf{n}_g = \nabla f \times \nabla g $$
* **Local Basis:** $\mathcal{B}_P = \{\mathbf{t}, \mathbf{n}_f, \mathbf{n}_g\}$ forms a local basis at point $P$.

---

## 4. Duality Summary Table

| Property | Surface Constraint | Curve Constraint |
| :--- | :--- | :--- |
| **Constraint Equations** | $1$ ($f(x,y,z)=0$) | $2$ ($f(x,y,z)=0, g(x,y,z)=0$) |
| **CDOFs** | $2$ (parameters $\alpha, \beta$) | $1$ (parameter $\alpha$) |
| **$\dim(V_N)$** | $1$ | $2$ |
| **$\dim(V_T)$** | $2$ | $1$ |
| **Normal Vector Source** | $\mathbf{n} = \nabla f$ or $\mathbf{t}_\alpha \times \mathbf{t}_\beta$ | $\mathbf{n}_f = \nabla f, \mathbf{n}_g = \nabla g$ |
| **Tangent Vector Source** | $\mathbf{t}_\alpha = \frac{\partial\mathbf{r}}{\partial\alpha}, \mathbf{t}_\beta = \frac{\partial\mathbf{r}}{\partial\beta}$ | $\mathbf{t} = \frac{d\mathbf{r}}{d\alpha}$ or $\nabla f \times \nabla g$ |
| **Unknown Reactions** | $1$ scalar ($N_1$) | $2$ scalars ($N_1, N_2$) |

---

## 🔗 Related Notes
* [[Topic 3 - Constraints and Reaction Forces|Topic 3 Master Guide]]
* [[Concept - Constraint and Reaction Forces Dynamical Decoupling|Dynamical Decoupling]]
* [[Concept - Work and Power of Constraint Forces and Energy Preservation|Work & Power of Constraints]]
