---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - theory
  - key-concept
  - stress-tensor
  - cauchy-principle
  - body-forces
dificultad: high
prerrequisitos:
  - "[[01 - Fluid Mechanics/Topic 2 - Flow Kinematics|Topic 2: Flow Kinematics]]"
---

# 🔬 Concept: Cauchy Stress Tensor and Body Forces

> **Key idea in one sentence:** The mechanical interaction in a fluid is divided into long-range body forces acting on the volume ($\vec{f}_m$) and short-range contact forces acting on the surface; according to Cauchy's Principle, the surface traction vector $\vec{f}_n$ on any orientation $\vec{n}$ is uniquely determined by the projection of a symmetric second-order tensor $\bar{\bar{\tau}}$ ($\vec{f}_n = \bar{\bar{\tau}}\cdot\vec{n}$), whose spatial divergence $\nabla\cdot\bar{\bar{\tau}}$ represents the resultant surface force per unit volume.

---

## 🌌 1. Physical Classification of Forces: Long Range vs Short Range

In macroscopic fluid mechanics, the forces acting on a fluid particle or element are classified according to their intermolecular range of action:

### A. Body or Volumetric Forces ($\vec{f}_m$) — Long Range
Their macroscopic range is infinitely greater than the mean intermolecular distance $d$. They act directly on each mass element $dm = \rho dV$:

$$ d\vec{F}_m = \rho \vec{f}_m(\vec{x}, t) \, dV \qquad \text{[Eq. 3.12]} $$

where $\vec{f}_m$ is the force per unit mass. In the most general case of a **non-inertial reference frame** with translational acceleration $\vec{a}_0(t)$ and instantaneous angular velocity $\vec{\Omega}(t)$, the net body force incorporates the acceleration of gravity and the four fictitious inertial forces:

$$ \mathbf{\vec{f}_m(\vec{x}, t) = \vec{g} - \vec{a}_0 - \frac{d\vec{\Omega}}{dt}\wedge\vec{x} - \vec{\Omega}\wedge(\vec{\Omega}\wedge\vec{x}) - 2\vec{\Omega}\wedge\vec{v}} \qquad \text{[Eq. 3.13]} $$

* $\vec{g}$: terrestrial gravity.
* $-\vec{a}_0$: translational inertia of the reference frame.
* $-\frac{d\vec{\Omega}}{dt}\wedge\vec{x}$: azimuthal or Euler inertial force.
* $-\vec{\Omega}\wedge(\vec{\Omega}\wedge\vec{x})$: apparent centrifugal force.
* $-2\vec{\Omega}\wedge\vec{v}$: Coriolis force (orthogonal to the relative velocity).

#### Potential of Conservative Body Forces
When the entrainment acceleration $\vec{a}_0$ and the rotation $\vec{\Omega}$ are constant, the gravity, linear translation and centrifugal forces are strictly conservative and derive from a single scalar potential $U(\vec{x})$:

$$ \vec{g} - \vec{a}_0 - \vec{\Omega}\wedge(\vec{\Omega}\wedge\vec{x}) = -\nabla U \qquad \text{[Eq. 3.14]} $$
$$ U(\vec{x}) = -\vec{g}\cdot\vec{x} + \vec{a}_0\cdot\vec{x} - \frac{1}{2}| \vec{\Omega}\wedge\vec{x} |^2 $$

### B. Surface Forces — Short Range
Their radius of influence is of molecular order ($d \sim 10^{-9}\text{ m}$). They are exerted exclusively through the contact area between adjacent fluid particles or between the fluid and a solid wall.
Given a differential surface element $d\sigma$ with outward-pointing unit normal vector $\vec{n}$, the surface force exerted on the fluid is given by:

$$ d\vec{F}_s = \vec{f}_n(\vec{n}, \vec{x}, t) \, d\sigma \qquad \text{[Eq. 3.15]} $$

where $\vec{f}_n$ is the **traction vector** or surface stress (force per unit area, units of $\text{N/m}^2$ or $\text{Pa}$). By the principle of action and reaction, $\vec{f}_{-n} = -\vec{f}_n$.

---

## 🔺 2. The Cauchy Tetrahedron and Derivation of the Stress Tensor (Notes.pdf, Eqs. 3.16–3.19)

The traction vector $\vec{f}_n$ depends a priori on the position $\vec{x}$, the time $t$ and the angular orientation of the unit vector $\vec{n} = (n_1, n_2, n_3)$. Cauchy showed that this directional dependence is strictly linear.

Consider an infinitesimal fluid element in the shape of a tetrahedron with three orthogonal faces parallel to the Cartesian coordinate planes, of areas $dA_1, dA_2, dA_3$ with outward normals $-\vec{e}_1, -\vec{e}_2, -\vec{e}_3$, and a fourth inclined or oblique face of area $dA$ with arbitrary outward unit normal $\vec{n} = n_1\vec{e}_1 + n_2\vec{e}_2 + n_3\vec{e}_3$.

By elementary geometric projection of the tetrahedron:
$$ dA_1 = n_1 dA, \quad dA_2 = n_2 dA, \quad dA_3 = n_3 dA $$
The volume of the tetrahedron is of order $dV \sim \frac{1}{6} h dA$, where $h$ is the height perpendicular to the oblique face.

Applying Newton's 2nd Law to the fluid tetrahedron:
$$ \rho dV \frac{D\vec{v}}{Dt} = \vec{f}_n dA + \vec{f}_{-e_1} dA_1 + \vec{f}_{-e_2} dA_2 + \vec{f}_{-e_3} dA_3 + \rho \vec{f}_m dV $$
Using $\vec{f}_{-e_i} = -\vec{f}_{e_i} \equiv -\vec{f}_i$:
$$ \vec{f}_n dA - \vec{f}_1 dA_1 - \vec{f}_2 dA_2 - \vec{f}_3 dA_3 = \rho dV \left(\frac{D\vec{v}}{Dt} - \vec{f}_m\right) \qquad \text{[Eq. 3.16]} $$

Taking the limit as the size of the tetrahedron tends to zero ($h \to 0$):
* Surface forces scale with the area of the faces: $\sim \mathcal{O}(dA) \sim \mathcal{O}(h^2)$.
* Inertial and volumetric forces scale with the volume: $\sim \mathcal{O}(dV) \sim \mathcal{O}(h^3)$.

Therefore, upon dividing by $dA$ and taking the limit $h \to 0$, the right-hand side vanishes rigorously:
$$ \vec{f}_n = n_1 \vec{f}_1 + n_2 \vec{f}_2 + n_3 \vec{f}_3 \qquad \text{[Eq. 3.17]} $$

Defining the Cartesian components of the traction vector on the face perpendicular to $\vec{e}_i$ as:
$$ \vec{f}_i = \tau_{i1}\vec{e}_1 + \tau_{i2}\vec{e}_2 + \tau_{i3}\vec{e}_3 = \sum_{j=1}^3 \tau_{ij}\vec{e}_j $$
where $\tau_{ij}$ represents the force per unit area in the direction $\vec{e}_j$ acting on a face whose outward normal points in the direction $\vec{e}_i$.
Grouping in matrix and tensor notation:

$$ \mathbf{\vec{f}_n = \vec{n} \cdot \bar{\bar{\tau}} = \bar{\bar{\tau}} \cdot \vec{n}} \qquad \text{[Eq. 3.17, 3.19]} $$

where the matrix of the **Cauchy Stress Tensor** $\bar{\bar{\tau}}$ is given by:

$$ \bar{\bar{\tau}} = \begin{bmatrix} \tau_{11} & \tau_{12} & \tau_{13} \\ \tau_{21} & \tau_{22} & \tau_{23} \\ \tau_{31} & \tau_{32} & \tau_{33} \end{bmatrix} \qquad \text{[Eq. 3.18]} $$

* **Normal stresses ($\tau_{11}, \tau_{22}, \tau_{33}$):** Stresses perpendicular to the surface (tension or compression).
* **Tangential or shear stresses ($\tau_{ij}$ with $i \neq j$):** Grazing stresses or viscous friction parallel to the face.

---

## ⚖️ 3. Symmetry of the Stress Tensor ($\tau_{ij} = \tau_{ji}$) (Notes.pdf, Eq. 3.19)

Consider a differential cubic fluid element with edges $dx_1, dx_2, dx_3$ centred at $\vec{x}$. Let us evaluate the angular momentum balance about the axis through the center of the cube parallel to $\vec{e}_3$:

$$ I_3 \frac{d\omega_3}{dt} = \sum M_{3, \text{ext}} $$
* The moment of inertia of the cube is $I_3 = \frac{1}{12} \rho (dx_1 dx_2 dx_3)(dx_1^2 + dx_2^2) \sim \mathcal{O}(dx^5)$.
* The moments of the body forces scale with the volume and the arm: $\sim \mathcal{O}(dx^4)$.
* The tangential forces on the lateral faces generate moments with arms $\frac{dx_1}{2}$ and $\frac{dx_2}{2}$:
  * Forces $\tau_{12}(dx_2 dx_3)$ on the $\pm x_1$ faces generate a counterclockwise couple: $\tau_{12}(dx_2 dx_3) dx_1$.
  * Forces $\tau_{21}(dx_1 dx_3)$ on the $\pm x_2$ faces generate a clockwise couple: $-\tau_{21}(dx_1 dx_3) dx_2$.

The moment balance gives:
$$ (\tau_{12} - \tau_{21}) dx_1 dx_2 dx_3 = \mathcal{O}(dx^4) + \mathcal{O}(dx^5) $$
Dividing by the differential volume $dV = dx_1 dx_2 dx_3$ and letting the size tend to zero ($dx \to 0$):

$$ \mathbf{\tau_{12} = \tau_{21}, \quad \tau_{13} = \tau_{31}, \quad \tau_{23} = \tau_{32} \implies \bar{\bar{\tau}} = \bar{\bar{\tau}}^T} \qquad \text{[Eq. 3.19]} $$

The Cauchy stress tensor is **strictly symmetric** in the absence of distributed internal volumetric couples (Boltzmann hypothesis / non-micropolar continuum).

---

## 🧭 4. Principal Stress Directions (Notes.pdf, Eqs. 3.20–3.21)

At any point of the fluid there exist particular orientations $\vec{n}$ for which the resulting surface traction is strictly normal to the face, with the tangential friction stresses vanishing completely ($\vec{f}_n \parallel \vec{n}$):

$$ \bar{\bar{\tau}} \cdot \vec{n} = \lambda \vec{n} \qquad \text{[Eq. 3.20]} $$

The eigenvalue condition requires the characteristic determinant to vanish:

$$ \mathbf{|\bar{\bar{\tau}} - \lambda \bar{\bar{I}}| = 0} \qquad \text{[Eq. 3.21]} $$

Since $\bar{\bar{\tau}}$ is a real symmetric ($3 \times 3$) matrix, the spectral theorem guarantees:
1. There exist three real roots $\lambda_1, \lambda_2, \lambda_3$ called **principal stresses**.
2. The corresponding associated unit directions $(\vec{n}_1, \vec{n}_2, \vec{n}_3)$ are **mutually orthogonal**.
3. In the coordinate system of the principal axes, the tensor is diagonalised: $\bar{\bar{\tau}} = \text{diag}(\lambda_1, \lambda_2, \lambda_3)$.

---

## 📦 5. Surface Resultant and Divergence of the Tensor (Notes.pdf, Eqs. 3.22–3.25)

The total surface force exerted on the boundary $\Sigma$ of a fluid volume is given by:

$$ \vec{F}_s = \int_\Sigma \vec{f}_n \, d\sigma = \int_\Sigma \bar{\bar{\tau}} \cdot \vec{n} \, d\sigma \qquad \text{[Eq. 3.22]} $$

Applying the general divergence theorem (Gauss's theorem) for second-order tensors:

$$ \mathbf{\int_\Sigma \bar{\bar{\tau}} \cdot \vec{n} \, d\sigma = \int_V (\nabla \cdot \bar{\bar{\tau}}) \, dV} \qquad \text{[Eq. 3.23]} $$

where in Cartesian components, the divergence of the tensor is the vector:
$$ (\nabla \cdot \bar{\bar{\tau}})_i = \sum_{j=1}^3 \frac{\partial \tau_{ji}}{\partial x_j} = \frac{\partial \tau_{1i}}{\partial x_1} + \frac{\partial \tau_{2i}}{\partial x_2} + \frac{\partial \tau_{3i}}{\partial x_3} $$

Evaluating the momentum balance on a differential element $dV$:
$$ \rho dV \frac{D\vec{v}}{Dt} = (\nabla \cdot \bar{\bar{\tau}}) dV + \rho \vec{f}_m dV \qquad \text{[Eq. 3.24]} $$
Dividing by the volume $dV$, the **Cauchy momentum differential equation** is obtained:

$$ \mathbf{\rho \frac{D\vec{v}}{Dt} = \nabla \cdot \bar{\bar{\tau}} + \rho \vec{f}_m} \qquad \text{[Eq. 3.25]} $$

This differential equation governs the dynamic motion of any deformable continuum. To close it mathematically in fluids, it is essential to express $\bar{\bar{\tau}}$ in terms of the kinematic and thermodynamic variables ($\vec{v}, p, T$), which leads to the **Navier-Poisson constitutive equation**.

## Stress Tensor: Complete Derivation Chain (Notes.pdf, Eqs. 3.15-3.25)

### Step 1: Geometry of the Cauchy tetrahedron (Fig. 3.2)

The tetrahedron has a vertex at the origin, three faces on the coordinate planes and one oblique face. Its edges along the axes are $dx_1,dx_2,dx_3$, so the coordinate face normal to $\vec{e}_i$ has area $dA_i$ and the volume is $dV=\tfrac16dx_1dx_2dx_3$ (Notes, p. 28). Let $\vec{n}$ be the outward unit normal of the oblique face, of area $dA$. The outward normals of the coordinate faces are $-\vec{e}_i$. For any closed surface $\oint\vec{n}\,d\sigma=\vec{0}$ (Gauss' theorem applied to a constant field). For the tetrahedron:

$$ dA\,\vec{n}-dA_1\vec{e}_1-dA_2\vec{e}_2-dA_3\vec{e}_3=\vec{0} $$

Taking the scalar product with $\vec{e}_i$ gives the geometrical identity used in the Notes:

$$ dA_i=n_i\,dA $$

The volume of a pyramid is one third of base times height, so $dV=\tfrac13h\,dA$, with $h$ the distance from the origin to the oblique face. If all edges are scaled by $\varepsilon$, the face areas scale as $\varepsilon^2$ and the volume as $\varepsilon^3$.

### Step 2: Stress vector on opposite faces

**Extension, not in the Notes.** The Notes state the sign convention directly (the force through the face normal to $\vec{e}_i$ is $-dA_i\vec{f}_i$). It follows from Newton's law applied to a thin disc of area $d\sigma$ and thickness $\varepsilon$: the mass and the volume forces scale as $\varepsilon\,d\sigma$ and vanish faster than the two face forces, which gives $\vec{f}_n\,d\sigma+\vec{f}_{-n}\,d\sigma\to\vec{0}$, that is $\vec{f}_{-\vec{n}}=-\vec{f}_{\vec{n}}$. The stress vector on the face with outward normal $-\vec{e}_i$ is therefore $-\vec{f}_i$, with $\vec{f}_i=(\tau_{i1},\tau_{i2},\tau_{i3})$.

### Step 3: Newton's second law on the tetrahedron and the limit (Eqs. 3.16 and 3.17)

Mass times acceleration equals the surface forces plus the volume force:

$$ \rho\,dV\,\frac{D\vec{v}}{Dt}=\vec{f}_n\,dA-\vec{f}_1\,dA_1-\vec{f}_2\,dA_2-\vec{f}_3\,dA_3+\rho\vec{f}_m\,dV $$

Substitute $dA_i=n_i\,dA$, divide by $dA$ and use $dV/dA=h/3$:

$$ \vec{f}_n-n_1\vec{f}_1-n_2\vec{f}_2-n_3\vec{f}_3=\frac{h}{3}\,\rho\left(\frac{D\vec{v}}{Dt}-\vec{f}_m\right) $$

Let the tetrahedron shrink to a point, $h\to0$, with the acceleration and the force per unit mass bounded. The right-hand side tends to zero because inertia and volume forces are of order $\varepsilon^3$, whereas the surface forces are of order $\varepsilon^2$. This is Eq. 3.16 divided by $dA$, and it yields

$$ \vec{f}_n=n_1\vec{f}_1+n_2\vec{f}_2+n_3\vec{f}_3 $$

*Eq. 3.17*

In components, $(\vec{f}_n)_j=\sum_in_i\tau_{ij}$, so $\vec{f}_n=\vec{n}\cdot\bar{\bar{\tau}}$ with $\bar{\bar{\tau}}=[\tau_{ij}]$ (Eq. 3.18). The dependence on $\vec{n}$ is linear. The symmetry shown in the next step turns it into $\bar{\bar{\tau}}\cdot\vec{n}$ (Eq. 3.19).

### Step 4: Symmetry of the stress tensor (Eq. 3.19)

Apply the angular momentum balance about the centre of a cube of edge $dx$. The inertia term (moment of inertia of order $dx^5$) and the moment of the volume force (order $dx^4$) are negligible against the moment of the surface forces (order $dx^3$). Consider the $z$ component. The face $x_1=+dx/2$ has outward normal $+\vec{e}_1$ and area $dx^2$; its force has the component $\tau_{12}\,dx^2\,\vec{e}_2$ at the position $(dx/2)\vec{e}_1$. The opposite face has force $-\tau_{12}\,dx^2\,\vec{e}_2$ at $-(dx/2)\vec{e}_1$. Both give the same moment, using $\vec{e}_1\wedge\vec{e}_2=\vec{e}_3$:

$$ 2\times\frac{dx}{2}\,\vec{e}_1\wedge\big(\tau_{12}\,dx^{2}\,\vec{e}_2\big)=\tau_{12}\,dx^{3}\,\vec{e}_3 $$

The faces normal to $\vec{e}_2$ give, with $\vec{e}_2\wedge\vec{e}_1=-\vec{e}_3$, the moment $-\tau_{21}\,dx^{3}\,\vec{e}_3$. The remaining stress components produce forces parallel to the position vector, or moments perpendicular to $\vec{e}_3$. The balance of moments along $\vec{e}_3$ is therefore

$$ \big(\tau_{12}-\tau_{21}\big)\,dx^{3}=O(dx^{4})\;\Longrightarrow\;\tau_{12}=\tau_{21} $$

after dividing by $dx^3$ and letting $dx\to0$. The same argument along $\vec{e}_1$ and $\vec{e}_2$ gives $\tau_{23}=\tau_{32}$ and $\tau_{13}=\tau_{31}$. The tensor has only six independent components and $\vec{n}\cdot\bar{\bar{\tau}}=\bar{\bar{\tau}}\cdot\vec{n}$, which is Eq. 3.19.

### Step 5: Principal stresses (Eqs. 3.20 and 3.21)

The shear stress on a surface of normal $\vec{n}$ vanishes if and only if $\bar{\bar{\tau}}\cdot\vec{n}$ is parallel to $\vec{n}$, that is, if

$$ \bar{\bar{\tau}}\cdot\vec{n}=\lambda\vec{n}\;\Longleftrightarrow\;\big(\bar{\bar{\tau}}-\lambda\bar{\bar{I}}\big)\cdot\vec{n}=\vec{0} $$

*Eq. 3.20*

A non-trivial solution exists only if the determinant of the matrix vanishes (Eq. 3.21), a cubic equation in $\lambda$. **Extension, not in the Notes.** The roots are real because $\bar{\bar{\tau}}$ is symmetric: for an eigenpair, $\lambda\,\bar{\vec{n}}\cdot\vec{n}=\bar{\vec{n}}\cdot\bar{\bar{\tau}}\cdot\vec{n}$ is real (its complex conjugate equals itself by symmetry), and $\bar{\vec{n}}\cdot\vec{n}\gt0$. For two eigenpairs with different eigenvalues,

$$ \lambda_1\,\vec{n}_1\cdot\vec{n}_2=(\bar{\bar{\tau}}\cdot\vec{n}_1)\cdot\vec{n}_2=\vec{n}_1\cdot(\bar{\bar{\tau}}\cdot\vec{n}_2)=\lambda_2\,\vec{n}_1\cdot\vec{n}_2\;\Longrightarrow\;(\lambda_1-\lambda_2)\,\vec{n}_1\cdot\vec{n}_2=0 $$

so the principal directions are mutually orthogonal.

### Step 6: Resultant surface force, Gauss' theorem and the local momentum equation (Eqs. 3.22 to 3.25)

The surface force on a fluid volume $V$ of boundary $\Sigma$ is the integral of the stress vector (Eq. 3.22). Apply Gauss' theorem (Eq. 2.9) to the vector field with components $\tau_{ij}$ ($j=1,2,3$) for each fixed $i$:

$$ \int_\Sigma(\bar{\bar{\tau}}\cdot\vec{n})_i\,d\sigma=\int_\Sigma\tau_{ij}n_j\,d\sigma=\int_V\frac{\partial\tau_{ij}}{\partial x_j}\,dV=\int_V(\nabla\cdot\bar{\bar{\tau}})_i\,dV $$

*Eq. 3.23*

For a volume that shrinks around a point, $\nabla\cdot\bar{\bar{\tau}}=\lim_{V\to0}\frac1V\int_\Sigma\bar{\bar{\tau}}\cdot\vec{n}\,d\sigma$, so $\nabla\cdot\bar{\bar{\tau}}$ is the surface force per unit volume. Newton's second law for a particle of mass $\rho\,dV$ then gives Eq. 3.24, and dividing by $dV$ gives Eq. 3.25:

$$ \rho\,dV\,\frac{D\vec{v}}{Dt}=(\nabla\cdot\bar{\bar{\tau}})\,dV+\rho\vec{f}_m\,dV\;\Longrightarrow\;\rho\frac{D\vec{v}}{Dt}=\nabla\cdot\bar{\bar{\tau}}+\rho\vec{f}_m $$

*Eqs. 3.24 and 3.25*


## Wall Shear Stress from the Stress Tensor (Notes.pdf, Eqs. 3.17, 3.28, 3.30 and 3.32)

**Extension, not in the Notes** (worked application of Eqs. 3.30 and 3.32). Consider a flat wall at $y=0$ with the fluid at $y\gt0$. The unit normal pointing into the fluid is $\vec{n}=\vec{e}_y$. By Eq. 3.32 the force per unit area exerted by the fluid on the wall is the stress vector

$$ \vec{f}=\bar{\bar{\tau}}\cdot\vec{e}_y=-p\,\vec{e}_y+\bar{\bar{\tau}}'\cdot\vec{e}_y $$

In components, Eq. 3.30 reads $\tau'_{ij}=\mu\left(\frac{\partial v_i}{\partial x_j}+\frac{\partial v_j}{\partial x_i}\right)+\lambda(\nabla\cdot\vec{v})\,\delta_{ij}$, since $(T_d)_{ij}=\tfrac12(\partial v_i/\partial x_j+\partial v_j/\partial x_i)$. The tangential component of the force is

$$ f_x=\tau'_{xy}=\mu\left(\frac{\partial v_x}{\partial y}+\frac{\partial v_y}{\partial x}\right)+\lambda(\nabla\cdot\vec{v})\,\delta_{xy} $$

The Kronecker delta is zero for $x\neq y$, so the bulk-viscosity term does not contribute to shear. The no-slip condition gives $v_y(x,0)=0$ for every $x$, hence its derivative along the wall vanishes, $\partial v_y/\partial x|_{y=0}=0$. Therefore

$$ \tau_w=f_x=\mu\left.\frac{\partial v_x}{\partial y}\right|_{y=0} $$

The normal component is $f_y=-p+\tau'_{yy}$ with $\tau'_{yy}=2\mu\,\partial v_y/\partial y+\lambda\nabla\cdot\vec{v}$. At the wall $v_x(x,0)=0$ for every $x$, so $\partial v_x/\partial x=0$ and $\nabla\cdot\vec{v}=\partial v_y/\partial y$. For an incompressible fluid $\nabla\cdot\vec{v}=0$, hence $\partial v_y/\partial y=0$, $\tau'_{yy}=0$ and $f_y=-p$: only pressure loads the wall in the normal direction, and the viscous contribution is purely tangential. The friction drag is the integral of $\tau_w$ over the wetted surface (second term of Eq. 3.32 projected on the flow direction).
