---
title: "Concept: Classification of Constraints (Holonomic, Rheonomic, Unilateral)"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
ground_truth: "slides/03_-_Constraints (1).pdf (Slide 21) & teoria/Notes.pdf (Section 6.5)"
tier: "Atomic Concept Note"
language: "English"
---

# 🏷️ Concept: Classification of Constraints (Holonomic, Rheonomic, Unilateral)

## 1. Mathematical Taxonomy of Constraints

In classical aerospace mechanics, kinematic constraints on point particles and rigid bodies are systematically classified according to three fundamental mathematical criteria (Slide 21 & Notes Sec. 6.5):

```
                       KINEMATIC CONSTRAINTS
                                |
        +-----------------------+-----------------------+
        |                       |                       |
   Integrability           Time Dependence         Domain Type
   (Holonomic vs           (Scleronomic vs         (Bilateral vs
   Non-Holonomic)            Rheonomic)              Unilateral)
```

---

## 2. Holonomic vs. Non-Holonomic Constraints

### 2.1 Holonomic (Integrable) Constraints
A constraint is **holonomic** if it can be formulated purely as an algebraic relationship between the configuration coordinates and time:
$$ f(x, y, z, t) = 0 $$
* **Physical Consequence:** Each independent holonomic constraint directly reduces the number of Configuration Degrees of Freedom (CDOFs) by 1:
  $$ \text{CDOF} = 3N - k $$
  where $N$ is the number of particles and $k$ is the number of independent holonomic constraint equations.
* **Examples:** Rigid rods of fixed length ($\|\mathbf{r}_1 - \mathbf{r}_2\| = \ell$), fixed guides, bead sliding on a wire ($f(x,y,z)=0, g(x,y,z)=0$).

### 2.2 Non-Holonomic (Non-Integrable) Constraints
A constraint is **non-holonomic** if it is expressed as a non-integrable relation involving velocities or coordinate differentials:
$$ \sum_{i=1}^3 A_i(\mathbf{r}, t)\dot{x}_i + B(\mathbf{r}, t) = 0 \quad \text{or} \quad \sum_{i=1}^3 A_i(\mathbf{r}, t)dx_i + B(\mathbf{r}, t)dt = 0 $$
where the differential 1-form is not exact and cannot be integrated into an equivalent algebraic coordinate function $f(\mathbf{r}, t) = 0$.
* **Physical Consequence:** Non-holonomic constraints **cannot** be used to eliminate spatial coordinates. The system configuration still requires the full set of coordinates, but velocity vectors are confined to a sub-distribution.
* **Examples:** Pure rolling without slip of a wheel, ball, or aircraft tire on a 2D surface.

---

## 3. Scleronomic (Stationary) vs. Rheonomic (Time-Dependent) Constraints

### 3.1 Scleronomic (Stationary)
A constraint is **scleronomic** if time $t$ does not appear explicitly in the constraint equation:
$$ f(x, y, z) = 0 \implies \frac{\partial f}{\partial t} = 0 $$
* **Energy Impact:** Constraint forces perform **identically zero work** ($W_N \equiv 0$) because velocity $\mathbf{v}_0^P$ is strictly tangent to the constraint manifold ($\mathbf{v}_0^P \in V_T$), while reaction force $\mathbf{N}$ is normal ($\mathbf{N} \in V_N \perp V_T$).
* **Examples:** A fixed spherical bowl, a stationary parabolic wire.

### 3.2 Rheonomic (Time-Dependent)
A constraint is **rheonomic** if time $t$ appears explicitly in the constraint equation:
$$ f(x, y, z, t) = 0 \implies \frac{\partial f}{\partial t} \neq 0 $$
* **Energy Impact:** Constraint forces **can perform work and change the mechanical energy** of the particle ($W_N \neq 0$), because velocity $\mathbf{v}_0^P$ has a non-zero component along the normal gradient $\nabla f$:
  $$ \frac{df}{dt} = \nabla f \cdot \mathbf{v}_0^P + \frac{\partial f}{\partial t} = 0 \implies \nabla f \cdot \mathbf{v}_0^P = -\frac{\partial f}{\partial t} \neq 0 $$
* **Examples:** A bead on a rotating wire loop ($\theta = \omega t$), a particle suspended from a string being wound onto a motorized spool at speed $c$ ($z(t) = L_0 - ct$).

---

## 4. Bilateral vs. Unilateral Constraints

### 4.1 Bilateral Constraints
A constraint is **bilateral** if it is defined by a strict mathematical equality:
$$ f(x, y, z, t) = 0 $$
* **Reaction Force:** The particle is permanently trapped on the manifold; the normal reaction force can point in either normal direction ($N \in \mathbb{R}$).

### 4.2 Unilateral Constraints
A constraint is **unilateral** if it is defined by an inequality:
$$ f(x, y, z, t) \ge 0 $$
* **Reaction Force:** The normal reaction can only push, not pull: $N \ge 0$.
* **Bifurcated Mechanics:**
  1. *Contact / Attached State ($f = 0, N > 0$):* The constraint is active.
  2. *Free / Detached State ($f > 0, N = 0$):* The constraint is inactive; particle flies freely.
* **Separation / Liftoff Criterion:** The transition from attached to detached motion occurs at the exact threshold where the normal reaction vanishes:
  $$ N = 0 $$
* **Aerospace Example (Slide 23):** Aircraft takeoff from runway. The ground reaction $N = mg - L = mg - \frac{1}{2}\rho v^2 S C_L$ vanishes at $v_{\text{takeoff}} = \sqrt{\frac{2mg}{\rho S C_L}}$.

---

## 5. Definition of a Simple Constraint
In this course, a **simple constraint** is defined as an:
$$\text{\textbf{Integrable (Holonomic)}} \quad + \quad \text{\textbf{Stationary (Scleronomic)}} \quad + \quad \text{\textbf{Bilateral}}$$
constraint on a single point particle, represented by stationary surfaces (2D) or curves (1D).

---

## 🔗 Related Notes
* [[Topic 3 - Constraints and Reaction Forces|Topic 3 Master Guide]]
* [[Concept - Normal and Tangent Subspaces for Surfaces and Curves|Normal and Tangent Subspaces]]
* [[Concept - Work and Power of Constraint Forces and Energy Preservation|Work & Power of Constraints]]
