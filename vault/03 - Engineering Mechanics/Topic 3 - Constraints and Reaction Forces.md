---
title: "Topic 3: Constraints and Reaction Forces"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
ground_truth: "slides/03_-_Constraints (1).pdf & teoria/Notes.pdf (Chapter 6)"
tier: "Theory Master Guide"
language: "English"
---

# 🔗 Topic 3: Constraints and Reaction Forces

## 📌 Syllabus & Pedagogical Map
This comprehensive master guide covers **Constraints and Reaction Forces** in classical aerospace mechanics, matching 100% of **`slides/03_-_Constraints (1).pdf`** (Slides 1–24) and Chapter 6 of **`teoria/Notes.pdf`** (pp. 61–66).

* [[Concept - Classification of Constraints Holonomic Rheonomic and Unilateral|Classification of Constraints]]
* [[Concept - Normal and Tangent Subspaces for Surfaces and Curves|Normal and Tangent Subspaces]]
* [[Concept - Constraint and Reaction Forces Dynamical Decoupling|Constraint and Reaction Forces]]
* [[Concept - Work and Power of Constraint Forces and Energy Preservation|Work and Power of Constraint Forces]]
* [[Concept - Coulomb Friction as Applied Force and Tangent Reaction|Coulomb Friction]]
* [[Concept - Constraints on Multi-Particle Systems and Pulleys|Multi-Particle Constraints]]
* [[Formula Sheet - Topic 3 Constraints and Reaction Forces|Formula Sheet]]

---

## 🧭 1. Introduction to Constraints & Configuration Degrees of Freedom (Slides 3–4, Notes 6.1–6.2)

### 1.1 Physical Definition of a Constraint
In unconstrained kinematics, a particle is free to explore three-dimensional Euclidean space $\mathbb{R}^3$. However, in engineering and flight mechanics, particle motion is restricted by contacts with surfaces, guides, cables, or rigid links (Slide 3 & Notes Sec. 6.1):
* An aircraft rolling along an airport runway or descending along a prescribed glide slope.
* A bead sliding along a fixed structural wire or curved pipe.
* Two satellite modules or payload masses connected by an inextensible tether running over a pulley mechanism.

Such physical restrictions are termed **constraints**. Mathematically, a **simple constraint** on a point particle:
1. Is expressed as an algebraic equation relating the spatial coordinates $(x, y, z)$ of a chosen reference frame.
2. Does not depend explicitly on time $t$ (**stationary / scleronomic**).
3. Completely restricts the particle from leaving the boundary on either side (**bilateral**).

Geometrically, simple constraints restrict the particle to move along **stationary surfaces** (two-dimensional manifolds) or **stationary curves** (one-dimensional manifolds).

### 1.2 Configuration Degrees of Freedom (CDOFs)
The number of **Configuration Degrees of Freedom (CDOFs)** is the minimum number of independent scalar variables required to uniquely specify the spatial position of the mechanical system at any instant:
* **Free Particle in 3D Space:** $\text{CDOF} = 3$ (independent Cartesian coordinates $x, y, z$).
* **Particle on a Surface:** A single constraint equation $f(x, y, z) = 0$ removes 1 spatial degree of freedom:
  $$ \text{CDOF} = 3 - 1 = 2 $$
* **Particle on a Curve:** Two independent constraint equations $f(x, y, z) = 0$ and $g(x, y, z) = 0$ remove 2 spatial degrees of freedom:
  $$ \text{CDOF} = 3 - 2 = 1 $$

### 1.3 Two Mathematical Strategies: DAE vs. Generalized Coordinates (Slide 4)
There are two distinct mathematical routes to formulate constrained mechanics:
1. **Differential-Algebraic Equations (DAE Approach):**
   Retain the full three Cartesian coordinates $(x, y, z)$, formulate Newton's Second Law with unknown constraint forces $\mathbf{N}$, and append the algebraic constraint equations:
   $$ \begin{cases} m_P\,\ddot{\mathbf{r}}_0^P = \mathbf{F}_{\text{applied}} + \mathbf{N} \\ f(x, y, z) = 0 \end{cases} $$
   *Drawback:* This yields a coupled differential-algebraic system whose analytical and numerical solution is notoriously complex and prone to numerical drift.
2. **Generalized Coordinates Approach (Primary Aerospace Course Method):**
   Select a minimal set of $n$ generalized coordinates $(q_1, \dots, q_n)$ equal to the number of CDOFs ($n = \text{CDOF}$) that naturally parametrize the constraint manifold:
   $$ \mathbf{r} = \mathbf{r}(q_1, \dots, q_n) $$
   By construction, the constraint equations are **identically satisfied for all values of $q_i$**, completely eliminating algebraic constraint equations from the dynamic evolution problem!

### 1.4 Pedagogical Coordinate Selection Strategy (Notes Sec. 6.2)
While coordinates can be chosen arbitrarily, selecting coordinates that mirror the constraint geometry simplifies the algebra immensely:
* **Tethered Particle / Fixed Radius Linkage:** If particle $P$ is attached by a rigid rod or taut string of length $\ell$ to fixed point $A$, it is constrained to the surface of a sphere of radius $\ell$ centered at $A$ (2 CDOFs). The natural generalized coordinates are the spherical angles $(\theta, \phi)$.
* **Particle on a Conical Guide:** For motion on a cone of half-angle $\alpha$, the azimuth angle $\theta$ and distance to the vertex $\rho$ (or vertical height $z$) provide the natural 2 CDOFs.
* **Particle on a Fixed Wire:** For a 1D curve, the Frenet arc length coordinate $s$ or one Cartesian coordinate parametrizing the curve provides the 1 CDOF.

---

## 🌐 2. Surfaces and Curves: Implicit and Parametric Representations (Slides 5–6, Notes 6.1)

### 2.1 Surfaces (2-Manifolds)
* **Implicit Form (Slide 5 & Notes Eq. 6.5):** A single scalar equation relating coordinates:
  $$ f(x, y, z) = 0 $$
  *Example (Notes Eq. 6.6):* Sphere of radius $R$ centered at origin: $x^2 + y^2 + z^2 - R^2 = 0$.
* **Parametric Form (Slide 5 & Notes Eq. 6.3):** Defined in terms of two independent parameters $(\alpha, \beta)$ which serve as natural generalized coordinates:
  $$ \begin{cases} x = x(\alpha, \beta) \\ y = y(\alpha, \beta) \\ z = z(\alpha, \beta) \end{cases} $$
  *Example (Notes Eq. 6.4):* Sphere of radius $R$ parametrized by spherical angles $(\theta, \phi)$:
  $$ x = R\cos\phi\sin\theta, \quad y = R\sin\phi\sin\theta, \quad z = R\cos\theta $$

### 2.2 Curves (1-Manifolds)
* **Implicit Form (Slide 5 & Notes Eq. 6.7):** Defined as the spatial intersection of two distinct surfaces:
  $$ \begin{cases} f(x, y, z) = 0 \\ g(x, y, z) = 0 \end{cases} $$
  *Example (Notes Eq. 6.8):* Circumference of radius $a$ in horizontal plane $z = C_z$ centered at $(C_x, C_y, C_z)$:
  $$ \begin{cases} (x - C_x)^2 + (y - C_y)^2 - a^2 = 0 \quad (\text{cylinder}) \\ z - C_z = 0 \quad (\text{plane}) \end{cases} $$
  *(Note: The representation of a curve as surface intersections is not unique; the same circle could be defined by intersecting a sphere and a plane).*
* **Parametric Form (Slide 5 & Notes Eq. 6.1):** Defined in terms of a single scalar parameter $\alpha$:
  $$ \begin{cases} x = x(\alpha) \\ y = y(\alpha) \\ z = z(\alpha) \end{cases} $$
  *Example (Notes Eq. 6.2):* Circumference of radius $a$: $x = C_x + a\cos\theta, y = C_y + a\sin\theta, z = C_z$.

### 2.3 Solved Benchmark Examples (Slide 6)

#### Example 1: Parametric Ellipse to Implicit Form
Given the parametric planar curve:
$$ \begin{cases} x(\alpha) = a\cos\alpha \\ y(\alpha) = b\sin\alpha \\ z(\alpha) = 0 \end{cases} $$
* **Step 1 (Isolate Trigonometric Functions):**
  $$ \cos\alpha = \frac{x}{a}, \quad \sin\alpha = \frac{y}{b} $$
* **Step 2 (Apply Fundamental Pythagorean Identity):**
  Applying $\cos^2\alpha + \sin^2\alpha \equiv 1$:
  $$ \left(\frac{x}{a}\right)^2 + \left(\frac{y}{b}\right)^2 = 1 \implies \frac{x^2}{a^2} + \frac{y^2}{b^2} - 1 = 0 $$
* **Step 3 (Formulate Implicit Curve System):**
  Intersecting the elliptic cylinder with the $z=0$ plane:
  $$ \begin{cases} f(x, y, z) = \frac{x^2}{a^2} + \frac{y^2}{b^2} - 1 = 0 \\ g(x, y, z) = z = 0 \end{cases} $$

#### Example 2: Parametric Sphere to Implicit Form
Given the parametric surface with azimuth $\alpha \in [0, 2\pi)$ and elevation $\beta \in [-\pi/2, \pi/2]$:
$$ \begin{cases} x(\alpha, \beta) = a\cos\alpha\cos\beta \\ y(\alpha, \beta) = a\sin\alpha\cos\beta \\ z(\alpha, \beta) = a\sin\beta \end{cases} $$
* **Step 1 (Horizontal Radius Sum of Squares):**
  $$ x^2 + y^2 = (a\cos\alpha\cos\beta)^2 + (a\sin\alpha\cos\beta)^2 = a^2\cos^2\beta(\cos^2\alpha + \sin^2\alpha) = a^2\cos^2\beta $$
* **Step 2 (Full 3D Euclidean Sum of Squares):**
  $$ x^2 + y^2 + z^2 = a^2\cos^2\beta + a^2\sin^2\beta = a^2(\cos^2\beta + \sin^2\beta) = a^2 $$
* **Step 3 (Implicit Form):**
  $$ f(x, y, z) = x^2 + y^2 + z^2 - a^2 = 0 $$

---

## 📐 3. Tangent and Normal Vector Subspaces (Slides 7–12, Notes 6.3)

At each regular point $P$ lying on a smooth constraint manifold, Euclidean space decomposes into the direct sum of two orthogonal vector subspaces (Slides 7–8):
$$ \mathbb{R}^3 = V_N \oplus V_T, \quad \text{with} \quad V_N \cap V_T = \{\mathbf{0}\} $$
where $V_N$ is the **normal subspace** and $V_T$ is the **tangent subspace**.

### 3.1 Vector Subspaces on a Surface (Slides 7 & 9)
* Dimensions: $\dim(V_N) = 1$ and $\dim(V_T) = 2$.
* **Normal Vector $\mathbf{n} \in V_N$ via Gradient Theorem (Notes Eq. 6.9):**
  By the Gradient Theorem for regular level sets $f(x, y, z) = 0$, the spatial gradient vector is strictly perpendicular to the tangent plane:
  $$ \mathbf{n} = \nabla f = \frac{\partial f}{\partial x}\mathbf{i}_0 + \frac{\partial f}{\partial y}\mathbf{j}_0 + \frac{\partial f}{\partial z}\mathbf{k}_0 $$
* **Unit Normal Vector (Notes Eq. 6.10):**
  $$ \mathbf{e}_n = \frac{\nabla f}{\|\nabla f\|} $$
* **Tangent Vectors $\mathbf{t}_\alpha, \mathbf{t}_\beta \in V_T$ via Parametric Derivatives:**
  $$ \mathbf{t}_\alpha = \frac{\partial\mathbf{r}}{\partial\alpha} = \frac{\partial x}{\partial\alpha}\mathbf{i}_0 + \frac{\partial y}{\partial\alpha}\mathbf{j}_0 + \frac{\partial z}{\partial\alpha}\mathbf{k}_0 $$
  $$ \mathbf{t}_\beta = \frac{\partial\mathbf{r}}{\partial\beta} = \frac{\partial x}{\partial\beta}\mathbf{i}_0 + \frac{\partial y}{\partial\beta}\mathbf{j}_0 + \frac{\partial z}{\partial\beta}\mathbf{k}_0 $$
* **Normal via Cross Product:** A valid normal vector is directly provided by the vector product of the tangent vectors:
  $$ \mathbf{n} = \mathbf{t}_\alpha \times \mathbf{t}_\beta $$
* **Local Surface Basis:** $\mathcal{B}_P = \{\mathbf{t}_\alpha, \mathbf{t}_\beta, \mathbf{n}\}$ forms a local basis of $\mathbb{R}^3$ at $P$.

### 3.2 Vector Subspaces on a Curve (Slides 8 & 10)
* Dimensions: $\dim(V_N) = 2$ and $\dim(V_T) = 1$.
* **Tangent Vector $\mathbf{t} \in V_T$ via Differentiation:**
  $$ \mathbf{t} = \frac{d\mathbf{r}}{d\alpha} = \frac{dx}{d\alpha}\mathbf{i}_0 + \frac{dy}{d\alpha}\mathbf{j}_0 + \frac{dz}{d\alpha}\mathbf{k}_0 $$
  *(Note: If $\alpha$ is chosen as the arc length $s$, then $\mathbf{t}$ is unitary: $\mathbf{t} = \mathbf{e}_t$).*
* **Normal Vectors $\mathbf{n}_f, \mathbf{n}_g \in V_N$ via Implicit Gradients:**
  $$ \mathbf{n}_f = \nabla f, \quad \mathbf{n}_g = \nabla g $$
* **Tangent via Cross Product:** The tangent direction is collinear with the line of intersection of both tangent planes:
  $$ \mathbf{t} = \mathbf{n}_f \times \mathbf{n}_g = \nabla f \times \nabla g $$
* **Local Curve Basis:** $\mathcal{B}_P = \{\mathbf{t}, \mathbf{n}_f, \mathbf{n}_g\}$ forms a local vector basis of $\mathbb{R}^3$ at point $P$.

---

### 3.3 Solved Slide Examples with Detailed Calculus (Slides 11 & 12)

#### Example 1: Tangent and Normal Subspaces of an Ellipse (Slide 11)
Given the curve $\mathbf{r}(\alpha) = a\cos\alpha\,\mathbf{i}_0 + b\sin\alpha\,\mathbf{j}_0 + 0\,\mathbf{k}_0$.
* **Tangent Vector $\mathbf{t} \in V_T$:**
  Applying the derivative rules $\frac{d}{d\alpha}\cos\alpha = -\sin\alpha$ and $\frac{d}{d\alpha}\sin\alpha = \cos\alpha$:
  $$ \mathbf{t} = \frac{d\mathbf{r}}{d\alpha} = -a\sin\alpha\,\mathbf{i}_0 + b\cos\alpha\,\mathbf{j}_0 $$
* **Normal Vectors $\mathbf{n}_f, \mathbf{n}_g \in V_N$:**
  From implicit equations $f = \frac{x^2}{a^2} + \frac{y^2}{b^2} - 1 = 0$ and $g = z = 0$:
  $$ \mathbf{n}_f = \nabla f = \frac{\partial f}{\partial x}\mathbf{i}_0 + \frac{\partial f}{\partial y}\mathbf{j}_0 + \frac{\partial f}{\partial z}\mathbf{k}_0 = \frac{2x}{a^2}\mathbf{i}_0 + \frac{2y}{b^2}\mathbf{j}_0 = \frac{2\cos\alpha}{a}\mathbf{i}_0 + \frac{2\sin\alpha}{b}\mathbf{j}_0 $$
  $$ \mathbf{n}_g = \nabla g = 0\,\mathbf{i}_0 + 0\,\mathbf{j}_0 + 1\,\mathbf{k}_0 = \mathbf{k}_0 $$
* **Orthogonality Verification via Scalar Products:**
  $$ \mathbf{t} \cdot \mathbf{n}_f = (-a\sin\alpha)\left(\frac{2\cos\alpha}{a}\right) + (b\cos\alpha)\left(\frac{2\sin\alpha}{b}\right) + 0 = -2\sin\alpha\cos\alpha + 2\sin\alpha\cos\alpha \equiv 0 $$
  $$ \mathbf{t} \cdot \mathbf{n}_g = (-a\sin\alpha)(0) + (b\cos\alpha)(0) + (0)(1) = 0 $$
* **Cross Product Alignment:**
  $$ \mathbf{n}_f \times \mathbf{n}_g = \begin{vmatrix} \mathbf{i}_0 & \mathbf{j}_0 & \mathbf{k}_0 \\ \frac{2\cos\alpha}{a} & \frac{2\sin\alpha}{b} & 0 \\ 0 & 0 & 1 \end{vmatrix} = \frac{2\sin\alpha}{b}\mathbf{i}_0 - \frac{2\cos\alpha}{a}\mathbf{j}_0 $$
  Notice that $\mathbf{n}_f \times \mathbf{n}_g$ is parallel to $\mathbf{t}$ because:
  $$ \mathbf{n}_f \times \mathbf{n}_g = -\frac{2}{ab}\left( -a\sin\alpha\,\mathbf{i}_0 + b\cos\alpha\,\mathbf{j}_0 \right) = -\frac{2}{ab}\mathbf{t} $$

#### Example 2: Paraboloid Surface Vectors (Slide 12)
Given the surface $x^2 + y^2 = z$ with $z > 0$.
* **Implicit Form & Normal Gradient:**
  $$ f(x, y, z) = x^2 + y^2 - z = 0 $$
  $$ \mathbf{n} = \nabla f = \frac{\partial(x^2+y^2-z)}{\partial x}\mathbf{i}_0 + \frac{\partial(x^2+y^2-z)}{\partial y}\mathbf{j}_0 + \frac{\partial(x^2+y^2-z)}{\partial z}\mathbf{k}_0 = 2x\,\mathbf{i}_0 + 2y\,\mathbf{j}_0 - \mathbf{k}_0 $$
* **Parametric Form & Tangent Vectors:**
  Adopting polar cylindrical coordinates $(r, \theta)$ with $z = r^2$:
  $$ \mathbf{r}(r, \theta) = r\cos\theta\,\mathbf{i}_0 + r\sin\theta\,\mathbf{j}_0 + r^2\,\mathbf{k}_0 $$
  Taking partial derivatives:
  $$ \mathbf{t}_r = \frac{\partial\mathbf{r}}{\partial r} = \cos\theta\,\mathbf{i}_0 + \sin\theta\,\mathbf{j}_0 + 2r\,\mathbf{k}_0 $$
  $$ \mathbf{t}_\theta = \frac{\partial\mathbf{r}}{\partial\theta} = -r\sin\theta\,\mathbf{i}_0 + r\cos\theta\,\mathbf{j}_0 + 0\,\mathbf{k}_0 $$
* **Cross Product Determinant Expansion:**
  $$ \mathbf{t}_r \times \mathbf{t}_\theta = \begin{vmatrix} \mathbf{i}_0 & \mathbf{j}_0 & \mathbf{k}_0 \\ \cos\theta & \sin\theta & 2r \\ -r\sin\theta & r\cos\theta & 0 \end{vmatrix} $$
  $$ = \mathbf{i}_0(0 - 2r^2\cos\theta) - \mathbf{j}_0(0 - (-2r^2\sin\theta)) + \mathbf{k}_0(r\cos^2\theta - (-r\sin^2\theta)) $$
  $$ = -2r^2\cos\theta\,\mathbf{i}_0 - 2r^2\sin\theta\,\mathbf{j}_0 + r(\cos^2\theta + \sin^2\theta)\,\mathbf{k}_0 $$
  $$ = -2r(r\cos\theta)\,\mathbf{i}_0 - 2r(r\sin\theta)\,\mathbf{j}_0 + r\,\mathbf{k}_0 = -r(2x\,\mathbf{i}_0 + 2y\,\mathbf{j}_0 - \mathbf{k}_0) = -r\nabla f = -r\mathbf{n} $$
  This confirms analytically that $\mathbf{t}_r \times \mathbf{t}_\theta$ is strictly normal to the surface.

---

## ⚖️ 4. Constraint Reaction Forces & Dynamical Decoupling (Slides 13–15, Notes 6.4–6.5)

### 4.1 Physical Nature of Constraint Forces
The physical agent enforcing a kinematic constraint is a **constraint (or reaction) force $\mathbf{N}$**:
* By definition of a smooth constraint, **the reaction force resides strictly in the normal vector subspace**:
  $$ \mathbf{N} \in V_N $$
* The scalar components of $\mathbf{N}$ are **not known a priori**; they adjust automatically to enforce the constraint:
  * For a **surface** ($\dim(V_N) = 1$): $\mathbf{N} = \lambda\,\nabla f = N_1\,\mathbf{n}$ (1 unknown scalar component $N_1(t)$).
  * For a **curve** ($\dim(V_N) = 2$): $\mathbf{N} = \lambda_1\,\nabla f + \lambda_2\,\nabla g = N_1\,\mathbf{n}_f + N_2\,\mathbf{n}_g$ (2 unknown scalar components $N_1(t), N_2(t)$).

### 4.2 Closure of the Dynamic Problem (Slide 13)
Newton's Second Law provides 3 scalar ODEs in 3D:
$$ m_P\,\mathbf{a}_0^P = \mathbf{F}_{\text{applied}} + \mathbf{N} $$
* **Curve Case:** $1 \text{ CDOF } (q_1) + 2 \text{ reaction components } (N_1, N_2) = 3 \text{ unknowns} \implies \text{Closed System}$ ($3 = 3$).
* **Surface Case:** $2 \text{ CDOFs } (q_1, q_2) + 1 \text{ reaction component } (N_1) = 3 \text{ unknowns} \implies \text{Closed System}$ ($3 = 3$).

### 4.3 Dynamical Decoupling Strategy (Slide 14)
To solve the coupled system cleanly:
1. **Isolate Generalized Equations of Motion:**
   Project Newton's second law onto the **tangent subspace $V_T$**:
   * For a curve, project along $\mathbf{t}$:
     $$ m_P\,\mathbf{a}_0^P \cdot \mathbf{t} = \mathbf{F}_{\text{applied}} \cdot \mathbf{t} + \underbrace{\mathbf{N} \cdot \mathbf{t}}_{=0} \implies m_P\,\mathbf{a}_0^P \cdot \mathbf{t} = \mathbf{F}_{\text{applied}} \cdot \mathbf{t} $$
   * For a surface, project along $\mathbf{t}_\alpha$ and $\mathbf{t}_\beta$:
     $$ m_P\,\mathbf{a}_0^P \cdot \mathbf{t}_\alpha = \mathbf{F}_{\text{applied}} \cdot \mathbf{t}_\alpha, \quad m_P\,\mathbf{a}_0^P \cdot \mathbf{t}_\beta = \mathbf{F}_{\text{applied}} \cdot \mathbf{t}_\beta $$
   Because $\mathbf{N} \perp V_T$, all unknown reaction terms vanish identically! This produces pure differential equations for the generalized coordinates $q_i(t)$.
2. **Determine Reaction Forces:**
   Once $q_i(t)$ and their time derivatives are known, project Newton's second law onto the **normal subspace $V_N$** to directly extract $N_1(t)$ and $N_2(t)$.

---

### 4.4 Path Variables Formulation along Smooth Curves (Notes Sec. 6.5, Eqs. 6.14–6.19)
When analyzing motion along a 3D smooth curve, formulating dynamics in the **Frenet-Serret intrinsic frame** $\{\mathbf{e}_t, \mathbf{e}_n, \mathbf{e}_b\}$ provides maximum clarity:
* **Acceleration (Notes Eq. 6.14):**
  $$ \mathbf{a}_0^P = \ddot{s}\,\mathbf{e}_t + \frac{\dot{s}^2}{\rho}\,\mathbf{e}_n $$
  where $s(t)$ is the arc length and $\rho(s)$ is the radius of curvature.
* **Force Decomposition (Notes Eqs. 6.15–6.16):**
  $$ \mathbf{F}_{\text{applied}} = F_t\,\mathbf{e}_t + F_n\,\mathbf{e}_n + F_b\,\mathbf{e}_b $$
  $$ \mathbf{N} = N_n\,\mathbf{e}_n + N_b\,\mathbf{e}_b \quad (\text{since } N_t = 0 \text{ for smooth wire}) $$
* **Newton's Equations Projected on Frenet-Serret Frame (Notes Eqs. 6.17–6.19):**
  $$ \begin{cases}
  F_t = m\ddot{s} & (\text{Tangential: Evolves Speed } \dot{s}) \\
  F_n + N_n = m\frac{\dot{s}^2}{\rho} & (\text{Principal Normal: Yields } N_n) \\
  F_b + N_b = 0 & (\text{Binormal: Yields } N_b)
  \end{cases} $$
  The tangential equation is completely decoupled from the reactions $N_n$ and $N_b$!

---

### 4.5 Slide 15 Benchmark Problem: Heavy Particle on a Vertical Circular Wire
A particle $P$ of mass $m$ slides along a vertical circular wire of radius $a$ in $Oxy$ under gravity $\mathbf{g} = -g\mathbf{j}_0$.

#### Step 1: Kinematics and Polar Basis
* Polar coordinates: $\mathbf{r}_0^P = a\,\mathbf{e}_R(\theta) = a(\cos\theta\,\mathbf{i}_0 + \sin\theta\,\mathbf{j}_0)$.
* Chain rule on polar unit vectors:
  $$ \frac{d\mathbf{e}_R}{dt} = \dot{\theta}\,\mathbf{e}_\theta, \quad \frac{d\mathbf{e}_\theta}{dt} = -\dot{\theta}\,\mathbf{e}_R $$
* Velocity vector (product rule with $a = \text{const}$):
  $$ \mathbf{v}_0^P = \frac{d}{dt}(a\,\mathbf{e}_R) = a\dot{\mathbf{e}}_R = a\dot{\theta}\,\mathbf{e}_\theta $$
* Acceleration vector (product and chain rules):
  $$ \mathbf{a}_0^P = \frac{d}{dt}(a\dot{\theta}\,\mathbf{e}_\theta) = a\ddot{\theta}\,\mathbf{e}_\theta + a\dot{\theta}\left(-\dot{\theta}\,\mathbf{e}_R\right) = -a\dot{\theta}^2\,\mathbf{e}_R + a\ddot{\theta}\,\mathbf{e}_\theta $$

#### Step 2: Force Projections
1. **Weight $\mathbf{W} = -mg\mathbf{j}_0$:**
   $$ \mathbf{W} \cdot \mathbf{e}_R = -mg\mathbf{j}_0 \cdot (\cos\theta\,\mathbf{i}_0 + \sin\theta\,\mathbf{j}_0) = -mg\sin\theta $$
   $$ \mathbf{W} \cdot \mathbf{e}_\theta = -mg\mathbf{j}_0 \cdot (-\sin\theta\,\mathbf{i}_0 + \cos\theta\,\mathbf{j}_0) = -mg\cos\theta $$
   $$ \mathbf{W} = -mg\sin\theta\,\mathbf{e}_R - mg\cos\theta\,\mathbf{e}_\theta $$
2. **Wire Reaction Force:** Acts strictly along the normal direction: $\mathbf{N} = N_R\,\mathbf{e}_R$.

#### Step 3: Newton's Second Law Projection
$$ m(-a\dot{\theta}^2\,\mathbf{e}_R + a\ddot{\theta}\,\mathbf{e}_\theta) = (N_R - mg\sin\theta)\,\mathbf{e}_R - mg\cos\theta\,\mathbf{e}_\theta $$
* **Tangential Equation ($\mathbf{e}_\theta \in V_T$):**
  $$ m a\ddot{\theta} = -mg\cos\theta \implies \ddot{\theta} + \frac{g}{a}\cos\theta = 0 $$
* **Radial Equation ($\mathbf{e}_R \in V_N$):**
  $$ -m a\dot{\theta}^2 = N_R - mg\sin\theta \implies N_R(\theta, \dot{\theta}) = mg\sin\theta - ma\dot{\theta}^2 $$

#### Step 4: First Integral of Motion via Work-Energy Theorem
Because the constraint is stationary and smooth, total mechanical energy is conserved:
$$ E_0 = T_0 + V_0 = \frac{1}{2}m(a\dot{\theta})^2 + mga\sin\theta = \text{constant} $$
Assuming release from rest at angle $\theta_0$ ($\dot{\theta}_0 = 0$):
$$ E_0 = mga\sin\theta_0 \implies \frac{1}{2}m a^2\dot{\theta}^2 + mga\sin\theta = mga\sin\theta_0 $$
Solving for the centripetal acceleration term $a\dot{\theta}^2$:
$$ a\dot{\theta}^2 = 2g(\sin\theta_0 - \sin\theta) $$
Substituting directly into the normal reaction force equation:
$$ N_R(\theta) = mg\sin\theta - m\left[ 2g(\sin\theta_0 - \sin\theta) \right] = mg(3\sin\theta - 2\sin\theta_0) $$
This expresses the reaction force purely as an algebraic function of position $\theta$!

---

## ⚡ 5. Power, Work, and Conservation of Mechanical Energy (Slide 16, Notes 6.4)

### 5.1 Power Exerted by a Constraint Force
The instantaneous power developed by constraint reaction $\mathbf{N}$ on particle $P$ is:
$$ P_N = \mathbf{N} \cdot \mathbf{v}_0^P $$

### 5.2 The Fundamental Work Theorem for Scleronomic Constraints
> [!IMPORTANT]
> **Stationary Constraint Work Theorem (Slide 16 & Notes Sec. 6.4):**
> For any **stationary (time-independent / scleronomic)** smooth constraint, the velocity vector $\mathbf{v}_0^P$ is strictly contained within the tangent subspace $V_T$, while the reaction force $\mathbf{N}$ resides strictly in the normal subspace $V_N$:
> $$ \mathbf{v}_0^P \in V_T \quad \text{and} \quad \mathbf{N} \in V_N \implies \mathbf{N} \perp \mathbf{v}_0^P $$
> Consequently, the instantaneous power and work done by the constraint force vanish identically:
> $$ P_N = \mathbf{N} \cdot \mathbf{v}_0^P \equiv 0 \implies W_N = \int_{t_1}^{t_2} P_N\,dt \equiv 0 $$

### 5.3 Proof via Differential Forms (Notes Eq. 6.12)
For a surface $f(x, y, z) = 0$, the reaction force is $\mathbf{N} = \lambda\,\nabla f$. The elementary work in displacement $d\mathbf{r}$ is:
$$ \delta W_N = \mathbf{N} \cdot d\mathbf{r} = (\lambda\,\nabla f) \cdot d\mathbf{r} = \lambda\left( \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy + \frac{\partial f}{\partial z}dz \right) = \lambda\,df $$
Because the particle is constrained to remain on the surface for all time, $f(x, y, z) = 0 \implies df \equiv 0$. Thus, $\delta W_N \equiv 0$.

### 5.4 Mechanical Energy Preservation
Because stationary constraint forces perform zero work, **they neither inject nor dissipate mechanical energy**. If all active applied forces are conservative ($\mathbf{F}_{\text{applied}} = -\nabla V_0$), total mechanical energy is strictly conserved:
$$ \frac{dE_0}{dt} = \frac{d(T_0 + V_0)}{dt} = P_{\text{applied}} + P_N = (-\nabla V_0 \cdot \mathbf{v}_0^P) + 0 + \frac{dV_0}{dt} \equiv 0 \implies E_0 = \text{constant} $$

---

## 🪢 6. Constraints on Systems of Particles: The Atwood Machine (Slide 17)

When several particles $\{P_1, P_2, \dots, P_N\}$ interact via kinematic constraints (such as inextensible cables running over pulleys or rigid linkages):
1. **Holonomic System Constraint:** The total length of an inextensible cable establishes a single scalar relation:
   $$ L = s_1 + 2s_2 + \text{constant} \implies \dot{s}_1 + 2\dot{s}_2 = 0 $$
2. **Minimal Coordinates:** The system CDOF is reduced. A two-particle system with one constraint cable has $2 \times 1 - 1 = 1$ CDOF.
3. **Internal Energy Transfer:** Cable tension exerts non-zero work on each individual particle:
   $$ W_1 = \int \mathbf{T}_1 \cdot d\mathbf{r}_1, \quad W_2 = \int \mathbf{T}_2 \cdot d\mathbf{r}_2 $$
   However, because the cable is massless and inextensible, $\mathbf{T}_1$ and $\mathbf{T}_2$ form an internal action-reaction network:
   $$ W_{\text{internal}} = W_1 + W_2 = \int T\,ds_1 + \int T\,(-ds_1) \equiv 0 $$
   The constraint simply **transfers mechanical energy** between particles, leaving the **total mechanical energy of the complete system perfectly conserved**!

### 6.1 Complete Worked Case Study: Classical Atwood Machine
Two masses $m_1$ and $m_2$ ($m_1 > m_2$) hang vertically from a light inextensible cable of length $L$ passing over a frictionless, massless pulley of radius $R$:
* **Kinematic Constraint:**
  $$ z_1 + z_2 = L - \pi R = \text{constant} $$
  Differentiating with respect to time twice:
  $$ \dot{z}_1 + \dot{z}_2 = 0 \implies \dot{z}_2 = -\dot{z}_1 $$
  $$ \ddot{z}_1 + \ddot{z}_2 = 0 \implies \ddot{z}_2 = -\ddot{z}_1 $$
* **Newton's Second Law for Each Mass:**
  $$ m_1\ddot{z}_1 = m_1 g - T $$
  $$ m_2\ddot{z}_2 = m_2 g - T \implies -m_2\ddot{z}_1 = m_2 g - T $$
* **Solving for Acceleration and Tension:**
  Subtracting the equations eliminates tension $T$:
  $$ (m_1 + m_2)\ddot{z}_1 = (m_1 - m_2)g \implies \ddot{z}_1 = \frac{m_1 - m_2}{m_1 + m_2}g $$
  Multiplying the first by $m_2$ and the second by $m_1$ and adding yields:
  $$ T = \frac{2m_1 m_2}{m_1 + m_2}g $$
* **Energy Verification:**
  $$ W_{\text{internal}} = \int_0^t (T\dot{z}_1 + T\dot{z}_2)\,dt' = \int_0^t T(\dot{z}_1 - \dot{z}_1)\,dt' \equiv 0 $$
  Total energy $E = \frac{1}{2}m_1\dot{z}_1^2 + \frac{1}{2}m_2\dot{z}_2^2 - m_1 g z_1 - m_2 g z_2 = \text{constant}$.

---

## 🛑 7. Coulomb Friction on Curves and Surfaces (Slides 18–20, Notes 6.6)

When surfaces or guides are rough, a **friction force $\mathbf{F}_R$** develops tangent to the contact manifold. We model this via the classical **Coulomb Friction Law** with friction coefficient $\mu$.

### 7.1 Two Distinct Physical Regimes (Slide 18)

| Parameter | Dynamic Friction Regime (Relative Motion) | Static Friction Regime (Relative Rest) |
| :--- | :--- | :--- |
| **Relative Velocity** | $\mathbf{v}_P^* \neq \mathbf{0}$ | $\mathbf{v}_P^* = \mathbf{0}$ |
| **Force Category** | **Applied Force** (Known magnitude & direction) | **Constraint Reaction Force** (Unknown magnitude) |
| **Mathematical Form** | $\mathbf{F}_R = -\mu N\,\frac{\mathbf{v}_P^*}{\|\mathbf{v}_P^*\|}$ | $\mathbf{F}_R \in V_T$ ($\mathbf{F}_R = R_1\mathbf{t}$ or $R_1\mathbf{t}_\alpha + R_2\mathbf{t}_\beta$) |
| **Magnitude** | Saturated: $\|\mathbf{F}_R\| = \mu N$ | Bounded: $\|\mathbf{F}_R\| \le \mu N$ |
| **Power & Work** | Strictly dissipative: $P_R = -\mu N v_P^* < 0$ | Zero: $P_R = \mathbf{F}_R \cdot \mathbf{0} \equiv 0$ |

### 7.2 Switching Criteria Between Regimes (Slide 19)
To solve mechanical problems with friction, we must monitor the contact state dynamically:
1. **Static $\to$ Dynamic (Initiation of Slip):**
   The particle remains at rest relative to the constraint as long as the tangential reaction force required to balance external forces satisfies:
   $$ \|\mathbf{F}_R\| \le \mu N $$
   If the required tangential force exceeds the Coulomb threshold ($\|\mathbf{F}_R\| > \mu N$), the static constraint breaks down and the particle begins to slip. We immediately switch to the dynamic formulation with $\mathbf{F}_R = -\mu N \frac{\mathbf{v}_P^*}{v_P^*}$.
2. **Dynamic $\to$ Static (Sticking / Arrest):**
   The particle moves under dynamic friction until its relative velocity drops to zero ($\mathbf{v}_P^* = \mathbf{0}$). At that instant, we test whether $\|\mathbf{F}_{\text{applied, tangential}}\| \le \mu N$. If true, the particle sticks and transitions back to the static regime.

---

### 7.3 Slide 20 Benchmark Problem: Particle on a Rough Circular Cylinder
A particle $P$ of mass $m$ moves on the surface of a rough fixed circular cylinder of radius $a$ oriented along the $z$-axis ($x^2 + y^2 = a^2$) with friction coefficient $\mu$.

#### Cylinder Geometry in Cylindrical Coordinates $\{R, \theta, z\}$:
* Constraint equation: $R = a = \text{const} \implies \dot{R} = 0, \ddot{R} = 0$.
* Tangent subspace $V_T$: spanned by azimuthal unit vector $\mathbf{e}_\theta$ and axial unit vector $\mathbf{e}_z$.
* Normal subspace $V_N$: spanned by radial unit vector $\mathbf{e}_R$.
* Kinematics:
  $$ \mathbf{v}_0^P = a\dot{\theta}\,\mathbf{e}_\theta + \dot{z}\,\mathbf{e}_z $$
  $$ \mathbf{a}_0^P = -a\dot{\theta}^2\,\mathbf{e}_R + a\ddot{\theta}\,\mathbf{e}_theta + \ddot{z}\,\mathbf{e}_z $$
* Normal reaction force: $\mathbf{N} = N\,\mathbf{e}_R$.

#### Regime A: Relative Motion Case ($\mathbf{v}_P^* = \mathbf{v}_0^P \neq \mathbf{0}$)
* Instantaneous speed: $v = \sqrt{(a\dot{\theta})^2 + \dot{z}^2} > 0$.
* Dynamic friction force (applied force opposing velocity):
  $$ \mathbf{F}_R = -\mu N\,\frac{\mathbf{v}_0^P}{v} = -\mu N\left( \frac{a\dot{\theta}}{v}\mathbf{e}_\theta + \frac{\dot{z}}{v}\mathbf{e}_z \right) $$
* Newton's second law: $m\mathbf{a}_0^P = \mathbf{F}_{\text{ext}} + \mathbf{N} + \mathbf{F}_R$:
  $$ \begin{cases}
  -m a\dot{\theta}^2 = F_{\text{ext}, R} + N \implies N = -F_{\text{ext}, R} - ma\dot{\theta}^2 \\
  m a\ddot{\theta} = F_{\text{ext}, \theta} - \mu N\frac{a\dot{\theta}}{v} \\
  m\ddot{z} = F_{\text{ext}, z} - \mu N\frac{\dot{z}}{v}
  \end{cases} $$
  The normal force $N = -F_{\text{ext}, R} - ma\dot{\theta}^2$ is substituted directly into the two tangential equations of motion.

#### Regime B: Relative Rest Case ($\mathbf{v}_0^P = \mathbf{0}$)
* Velocity vanishes: $\dot{\theta} = 0, \dot{z} = 0$.
* Friction acts as an unknown reaction vector in the tangent plane: $\mathbf{F}_R = R_\theta\,\mathbf{e}_\theta + R_z\,\mathbf{e}_z$.
* Newton's second law for equilibrium:
  $$ \mathbf{a}_0^P = \mathbf{0} \implies \begin{cases}
  0 = F_{\text{ext}, R} + N \implies N = -F_{\text{ext}, R} \\
  0 = F_{\text{ext}, \theta} + R_\theta \implies R_\theta = -F_{\text{ext}, \theta} \\
  0 = F_{\text{ext}, z} + R_z \implies R_z = -F_{\text{ext}, z}
  \end{cases} $$
* Static slip condition: The particle remains at rest if and only if:
  $$ \|\mathbf{F}_R\| = \sqrt{R_\theta^2 + R_z^2} = \sqrt{F_{\text{ext}, \theta}^2 + F_{\text{ext}, z}^2} \le \mu N = \mu(-F_{\text{ext}, R}) $$

---

## 🚀 8. Advanced Classification of Constraints (Slides 21–23, Notes 6.5)

Constraints in aerospace and structural mechanics are classified according to three fundamental mathematical dichotomies:

### 8.1 Holonomic vs. Non-Holonomic
* **Holonomic (Integrable):** The constraint equation can be expressed strictly as an algebraic relation among coordinates and time:
  $$ f(\mathbf{r}, t) = 0 $$
  *Consequence:* Each holonomic constraint directly reduces the number of CDOFs by 1.
* **Non-Holonomic (Non-Integrable):** The constraint is formulated in terms of coordinate differentials or velocities:
  $$ \sum_{i=1}^3 A_i(\mathbf{r}, t)\dot{x}_i + B(\mathbf{r}, t) = 0 $$
  which **cannot be integrated** into an equivalent algebraic coordinate relation (e.g., pure rolling of a sphere or disk without slip on a plane).
  *Consequence:* Non-holonomic constraints **cannot reduce the number of configuration coordinates**; the kinematic velocity relations must be appended to the dynamical equations using Lagrange multipliers.

### 8.2 Scleronomic (Stationary) vs. Rheonomic (Time-Dependent)
* **Scleronomic:** The constraint equations do not contain time explicitly ($\frac{\partial f}{\partial t} = 0$).
  *Consequence:* Reaction forces perform zero work ($W_N \equiv 0$).
* **Rheonomic:** The constraint manifold evolves explicitly with time ($\frac{\partial f}{\partial t} \neq 0$).
  *Consequence:* Velocity has a component along $\nabla f$; constraint forces **can perform work and change the mechanical energy of the particle**! Adding time requires $t$ (or a moving frame parameter) as an explicit dependency.

### 8.3 Bilateral vs. Unilateral
* **Bilateral:** Formulated as strict equalities ($f(\mathbf{r}, t) = 0$). The particle is permanently trapped on the manifold; the normal reaction can take either positive or negative values ($N \in \mathbb{R}$).
* **Unilateral:** Formulated as inequalities ($f(\mathbf{r}, t) \ge 0$). The particle can move freely in the domain $f > 0$ and is supported at the boundary $f = 0$ with $N \ge 0$.
  *Consequence:* The solution must be bifurcated into two regimes:
  1. *Attached regime:* Constraint is active ($f = 0, N > 0$).
  2. *Detached regime:* Particle flies off ($f > 0, N = 0$).
  *Liftoff / Separation Criterion:* Separation occurs precisely when the normal reaction force drops to zero:
  $$ N = 0 $$

---

### 8.4 Solved Classification Examples (Slides 22 & 23)

#### Example 1: Rheonomic Constraint — Spool Reeling String (Slide 22)
A heavy particle $P$ of mass $m$ is suspended along the vertical $z$-axis by a massless string being collected onto a spool at origin $O$ at constant speed $c > 0$. At $t = 0$, the string length is $L_0$.
* **Constraint Equation:**
  $$ z(t) = -(L_0 - ct) = ct - L_0 $$
* **Classification:**
  * Integrable in coordinates $\implies$ **Holonomic**.
  * Contains explicit time $t$ ($\frac{\partial f}{\partial t} = c \neq 0$) $\implies$ **Rheonomic**.
  * The particle cannot leave the string $\implies$ **Bilateral**.
* **Calculus & Work:**
  Differentiating position with respect to time:
  $$ \dot{z}(t) = \frac{d}{dt}(ct - L_0) = c $$
  Newton's second law along the vertical axis ($\mathbf{a}_0^P = \ddot{z}\mathbf{k}_0 = \mathbf{0}$):
  $$ m\ddot{z} = T - mg \implies 0 = T - mg \implies T = mg $$
  Instantaneous power exerted by the string tension:
  $$ P_T = \mathbf{T} \cdot \mathbf{v}_0^P = (T\,\mathbf{k}_0) \cdot (c\,\mathbf{k}_0) = T c = mgc \neq 0 $$
  Work done over interval $[0, t]$:
  $$ W_T = \int_0^t P_T\,dt' = \int_0^t mgc\,dt' = [mgct']_0^t = mgct > 0 $$
  Because the constraint is rheonomic, **it injects positive mechanical work into the particle**, increasing its potential energy!

#### Example 2: Unilateral Constraint — Airplane Takeoff on Runway (Slide 23)
An aircraft of mass $m$ accelerates along a horizontal runway ($z = 0$) in a calm atmosphere. The aerodynamic lift generated by its wings is:
$$ L = \frac{1}{2}\rho v^2 S C_L $$
where $\rho$ is air density, $S$ is wing surface area, and $C_L$ is the lift coefficient.

* **Constraint Formulation:**
  The ground prevents the airplane from penetrating the Earth ($z \ge 0$), but allows it to lift off into the air ($z > 0$):
  $$ z \ge 0, \quad N \ge 0 \implies \text{\textbf{Unilateral Constraint}} $$
* **Vertical Dynamic Equilibrium on Runway ($z = 0, \ddot{z} = 0$):**
  $$ \sum F_z = m\ddot{z} = 0 \implies N + L - mg = 0 \implies N(v) = mg - \frac{1}{2}\rho v^2 S C_L $$
* **Liftoff Condition:**
  The aircraft lifts off the runway the exact instant the ground reaction force vanishes ($N = 0$):
  $$ N(v_{\text{takeoff}}) = 0 \implies mg - \frac{1}{2}\rho v_{\text{takeoff}}^2 S C_L = 0 $$
  $$ \frac{1}{2}\rho v_{\text{takeoff}}^2 S C_L = mg \implies v_{\text{takeoff}}^2 = \frac{2mg}{\rho S C_L} $$
  Taking the positive square root:
  $$ v_{\text{takeoff}} = \sqrt{\frac{2mg}{\rho S C_L}} \quad [\text{m/s}] $$
* **Aerospace Numerical Order of Magnitude:**
  For a typical narrow-body commercial airliner (e.g. Boeing 737 / Airbus A320):
  * Mass $m = 65{,}000\text{ kg}$
  * Wing area $S = 122.6\text{ m}^2$
  * Takeoff lift coefficient $C_L = 1.6$
  * Sea level air density $\rho = 1.225\text{ kg/m}^3$
  * Gravity $g = 9.81\text{ m/s}^2$
  $$ v_{\text{takeoff}} = \sqrt{\frac{2 \times 65000 \times 9.81}{1.225 \times 122.6 \times 1.6}} = \sqrt{\frac{1{,}275{,}300}{240.296}} \approx \sqrt{5307.2} \approx 72.85\text{ m/s} \approx 262.3\text{ km/h} \approx 141.6\text{ knots} $$
  This demonstrates directly why runway takeoff requirements and rotation speeds ($V_r$) are dictated by aircraft mass, wing loading ($m/S$), and flap deflection ($C_L$).
