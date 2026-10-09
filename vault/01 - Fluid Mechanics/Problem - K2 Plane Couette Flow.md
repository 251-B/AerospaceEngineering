---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - couette
  - deformacion
  - vorticidad
  - circulacion
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-02-flow-kinematics/problemas/K2.pdf"
---

# Problem K2: Plane Couette Flow, Rotation and Strain

> Official UC3M kinematics problem collection (Introduction to Fluid Mechanics). Part of [[Topic 2 - Flow Kinematics]]. Related concepts: [[Concept - Eulerian vs Lagrangian Description and Flow Lines|flow lines]], [[Concept - Vorticity, Circulation and Velocity Potential|vorticity and circulation]], [[Concept - Deformation, Rotation and the Rate-of-Strain Tensor|deformation, rotation and rate-of-strain tensor]].

## Statement

Consider the steady flow of a liquid confined between two parallel planar walls separated a distance $H$. If the top wall moves with constant velocity $U$, the resulting fluid motion exhibits a single velocity component $v_x = Uy/H$, where $y$ denotes the distance to the bottom wall, assumed to be at rest.

1. Determine the streamlines and the trajectories.
2. Obtain the vorticity field.
3. Compute the circulation $\Gamma$ around a rectangular line of side $L$ oriented parallel to the walls and height $h$.
4. Calculate the gradient of velocity, the rate-of-strain tensor and the expansion rate.
5. Obtain the principal directions of strain as well as the associated principal strain rates.
6. Investigate the evolution of a square fluid element of side $dl$ oriented parallel to the walls.

Source: K2.pdf (page 1). Notes.pdf, Chapter 2: trajectories Eq. (2.12), stream lines Eq. (2.21), circulation and Stokes theorem Eqs. (2.29)-(2.33), velocity gradient and its decomposition Eqs. (2.46)-(2.52), principal directions Eqs. (2.54)-(2.55), square element Eqs. (2.56)-(2.61), expansion rate Eqs. (2.62)-(2.63).

## Phase 1: Hypotheses, Degrees of Freedom and Data

- Planar, steady, unidirectional flow: $\mathbf{v} = (Uy/H)\,\mathbf{e}_x$, with $v_y = v_z = 0$. The velocity depends on one coordinate only ($y$), so there is a single spatial degree of freedom; the time derivative of the field vanishes.
- The domain is $0 \le y \le H$ (liquid between the walls); the bottom wall ($y=0$) is at rest and the top wall ($y=H$) moves with velocity $U$, so the no-slip condition is satisfied at both walls.
- The liquid is treated as a continuum of constant density, as stated ("a liquid").

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $U$ | velocity of the top wall | m/s |
| $H$ | gap between the walls | m |
| $L$, $h$ | length (along $x$) and height (along $y$) of the rectangular circuit | m |
| $dl$ | side of the fluid element | m |
| $U/H$ | shear rate | s$^{-1}$ |

## Phase 2: Coordinates, Frames and Changes of Variable

- Inertial laboratory frame, Cartesian basis $(\mathbf{e}_x, \mathbf{e}_y, \mathbf{e}_z)$, $\mathbf{e}_z = \mathbf{e}_x \wedge \mathbf{e}_y$ (out of the plane of the motion). The bottom wall defines the frame at rest.
- Convention for the velocity gradient (Notes, after Eq. 2.26): $(\nabla\mathbf{v})_{ij} = \partial v_j/\partial x_i$, so that the change of the velocity across a small material segment $d\mathbf{x}$ is the row vector times the matrix, $d\mathbf{v} = d\mathbf{x}\cdot\nabla\mathbf{v}$ (Eq. 2.46).
- The principal axes of strain are obtained from a change of basis: the eigenvectors of the symmetric tensor $\bar{\bar{T}}_d$ give a rotated basis $(\mathbf{n}_1, \mathbf{n}_2)$ at $\pm 45^\circ$ to $(\mathbf{e}_x,\mathbf{e}_y)$ (part 5). The change-of-basis matrix has the vectors $\mathbf{n}_1$ and $\mathbf{n}_2$ as columns.

## Phase 3: Step-by-Step Derivation

### 3.1 Streamlines and trajectories

Why this tool: streamlines are tangent to $\mathbf{v}$ at one instant (Eq. 2.21); trajectories solve $d\mathbf{x}/dt = \mathbf{v}$ (Eq. 2.12). For a steady field both are determined by the same vector field and, as shown below, they coincide geometrically.

Streamlines: $dx/v_x = dy/v_y$ with $v_y = 0$. Written as $v_y\,dx - v_x\,dy = 0$ this reads $-v_x\,dy = 0$, and $dy = 0$ wherever $v_x \neq 0$. Hence $y = y_0 = $ const: straight lines parallel to the walls.

Trajectories with $\mathbf{x}(0) = (x_0, y_0)$:
$$ \frac{dy}{dt} = 0 \;\Longrightarrow\; y(t) = y_0, \qquad \frac{dx}{dt} = \frac{Uy_0}{H} \;\Longrightarrow\; \int_{x_0}^{x}dx' = \int_0^t\frac{Uy_0}{H}\,dt' \;\Longrightarrow\; x(t) = x_0 + \frac{Uy_0}{H}\,t. $$
Eliminating $t$ gives the path line $y = y_0$. The particles on the bottom wall are at rest ($y_0 = 0$) and the particles at $y_0 = H$ move at $U$. Streamlines, path lines and (because the field is steady) streak lines are the same family of lines $y = $ const.

### 3.2 Vorticity

Why this tool: $\boldsymbol{\omega} = \nabla\wedge\mathbf{v}$ is twice the angular velocity of the material element (Eq. 2.52).
$$ \omega_z = \frac{\partial v_y}{\partial x} - \frac{\partial v_x}{\partial y} = 0 - \frac{\partial}{\partial y}\left(\frac{Uy}{H}\right) = -\frac{U}{H}, \qquad \boxed{\,\boldsymbol{\omega} = -\frac{U}{H}\,\mathbf{e}_z.\,} $$
The vorticity is uniform and non-zero: the flow is rotational, with clockwise rotation (the top moves in $+x$, the bottom is at rest).

### 3.3 Circulation around a rectangle

Why this tool: by definition $\Gamma = \oint\mathbf{v}\cdot d\mathbf{l}$ (Eq. 2.29); since the rectangle lies inside the fluid, Stokes theorem (Eq. 2.32) gives the same value from the vorticity flux. The circuit occupies $x \le x' \le x + L$ and $y \le y' \le y + h$ with $0 \le y$ and $y + h \le H$, and is traversed counter-clockwise (normal $+\mathbf{e}_z$).

Line integral, bottom + right - top - left:
$$ \Gamma = \int_x^{x+L}v_x(y)\,dx' + \int_y^{y+h}v_y\,dy' - \int_x^{x+L}v_x(y+h)\,dx' - \int_y^{y+h}v_y\,dy'. $$
Both vertical integrals vanish because $v_y \equiv 0$, and the horizontal ones are integrals of constants over the length $L$:
$$ \Gamma = \frac{Uy}{H}L - \frac{U(y+h)}{H}L = \boxed{\,-\frac{UhL}{H}.\,} $$
Stokes theorem: $\Gamma = \iint_S\boldsymbol{\omega}\cdot\mathbf{e}_z\,d\sigma = \left(-\dfrac{U}{H}\right)(hL)$, which is the same.

### 3.4 Velocity gradient, rate-of-strain tensor and expansion rate

Why this tool: splitting $\nabla\mathbf{v}$ into symmetric and anti-symmetric parts (Eq. 2.47) separates the pure strain of the element, $\bar{\bar{T}}_d$, from its rigid rotation, $\bar{\bar{T}}_r$.
$$ \nabla\mathbf{v} = \begin{pmatrix}\partial_x v_x & \partial_x v_y\\ \partial_y v_x & \partial_y v_y\end{pmatrix} = \begin{pmatrix}0 & 0\\ U/H & 0\end{pmatrix}, $$
$$ \bar{\bar{T}}_d = \tfrac{1}{2}\left[\nabla\mathbf{v} + (\nabla\mathbf{v})^T\right] = \begin{pmatrix}0 & \dfrac{U}{2H}\\[4pt] \dfrac{U}{2H} & 0\end{pmatrix}, \qquad \bar{\bar{T}}_r = \tfrac{1}{2}\left[\nabla\mathbf{v} - (\nabla\mathbf{v})^T\right] = \begin{pmatrix}0 & -\dfrac{U}{2H}\\[4pt] \dfrac{U}{2H} & 0\end{pmatrix}. $$
Expansion rate (the trace, Eqs. 2.62-2.63): $\nabla\cdot\mathbf{v} = \operatorname{tr}\bar{\bar{T}}_d = 0 + 0 = 0$. The liquid element keeps its volume.

Consistency with the vorticity: in this convention $(\bar{\bar{T}}_r)_{12} = \tfrac12\left(\partial_x v_y - \partial_y v_x\right) = \omega_z/2 = -U/2H$ is the angular velocity of the element, and $d\mathbf{v}_r = d\mathbf{x}\cdot\bar{\bar{T}}_r = \tfrac12\boldsymbol{\omega}\wedge d\mathbf{x}$ (Eq. 2.52). Check with $d\mathbf{x} = (0, dl)$: $d\mathbf{x}\cdot\bar{\bar{T}}_r = (dl\,U/2H,\,0)$ and $\tfrac12(-U/H)\,\mathbf{e}_z\wedge dl\,\mathbf{e}_y = +\tfrac{U}{2H}dl\,\mathbf{e}_x$; both agree.

### 3.5 Principal directions and strain rates

Why this tool: along the principal directions the strain reduces to a pure extension without shear (Eq. 2.54), so the eigenproblem of the symmetric tensor $\bar{\bar{T}}_d$ is solved through its characteristic equation (Eq. 2.55).
$$ \det\left(\bar{\bar{T}}_d - \lambda\bar{\bar{I}}\right) = \begin{vmatrix}-\lambda & U/2H\\ U/2H & -\lambda\end{vmatrix} = \lambda^2 - \left(\frac{U}{2H}\right)^2 = 0 \;\Longrightarrow\; \lambda_{1,2} = \pm\frac{U}{2H}. $$
For $\lambda_1 = +U/2H$: $\begin{pmatrix}-U/2H & U/2H\\ U/2H & -U/2H\end{pmatrix}\begin{pmatrix}n_x\\ n_y\end{pmatrix} = 0 \Rightarrow n_x = n_y$, and normalising, $\mathbf{n}_1 = \tfrac{1}{\sqrt2}(1, 1)$ (angle $+45^\circ$).

For $\lambda_2 = -U/2H$: $\begin{pmatrix}U/2H & U/2H\\ U/2H & U/2H\end{pmatrix}\begin{pmatrix}n_x\\ n_y\end{pmatrix} = 0 \Rightarrow n_x = -n_y$, so $\mathbf{n}_2 = \tfrac{1}{\sqrt2}(1, -1)$ (angle $-45^\circ$).

Change of basis: with $\mathbf{P} = [\mathbf{n}_1\ \mathbf{n}_2] = \tfrac{1}{\sqrt2}\begin{pmatrix}1 & 1\\ 1 & -1\end{pmatrix}$ we have $\mathbf{P}\mathbf{P}^T = \mathbf{I}$ and $\det\mathbf{P} = -1$. The pair $(\mathbf{n}_1,\mathbf{n}_2)$ is orthonormal but left-handed; using $-\mathbf{n}_2$ instead gives a proper rotation with $\det = +1$. In either case $\mathbf{P}^T\bar{\bar{T}}_d\mathbf{P} = \operatorname{diag}(U/2H, -U/2H)$.

The material is stretched along $+45^\circ$ and compressed along $-45^\circ$, at the rate $U/2H$ per unit length in each direction; the sum of the principal rates is zero, as required by $\nabla\cdot\mathbf{v} = 0$.

### 3.6 Evolution of a square fluid element

Why this tool: a material segment $d\mathbf{l}$ evolves as $d\mathbf{l}(t+dt) = d\mathbf{l} + (d\mathbf{l}\cdot\nabla\mathbf{v})\,dt$ (Eqs. 2.46 and 2.56-2.57), valid to first order in $dt$.

Horizontal side, $d\mathbf{l}_1 = dl\,(1, 0)$: $d\mathbf{l}_1\cdot\nabla\mathbf{v} = dl\,(1,0)\begin{pmatrix}0&0\\U/H&0\end{pmatrix} = dl\,(0,0)$, so $d\mathbf{l}_1 \to dl\,(1, 0)$: it neither stretches nor turns.

Vertical side, $d\mathbf{l}_2 = dl\,(0, 1)$: $d\mathbf{l}_2\cdot\nabla\mathbf{v} = dl\,(0,1)\begin{pmatrix}0&0\\U/H&0\end{pmatrix} = dl\,(U/H,\,0)$, so
$$ d\mathbf{l}_2 \to dl\left(\frac{U}{H}\,dt,\; 1\right). $$
The square becomes a parallelogram: the vertical side tilts towards $+x$ by the small angle $(U/H)\,dt$, and the angle between the two sides decreases from $\pi/2$ to $\pi/2 - (U/H)\,dt$. The area, base $dl$ times height $dl$, is unchanged to first order (zero expansion rate).

Decomposition of the same motion (Eq. 2.51 and 2.60-2.61), side by side:

- Horizontal side: $d\mathbf{l}_1\cdot\bar{\bar{T}}_r = dl\,(0, -U/2H)$ (rotation, clockwise) and $d\mathbf{l}_1\cdot\bar{\bar{T}}_d = dl\,(0, +U/2H)$ (strain, counter-clockwise); the two cancel, as found directly.
- Vertical side: $d\mathbf{l}_2\cdot\bar{\bar{T}}_r = dl\,(U/2H, 0)$ and $d\mathbf{l}_2\cdot\bar{\bar{T}}_d = dl\,(U/2H, 0)$; both move the tip towards $+x$ and add up to $dl\,(U/H, 0)$.

So the distortion is the combined result of a rigid rotation with angular velocity $\Omega_z = -U/2H$ (angle $-(U/2H)\,dt$) and a shear strain with strain rate $\dot\gamma = \partial_x v_y + \partial_y v_x = U/H$, which is the rate at which the angle between the sides decreases (Notes, after Eq. 2.61).

## Phase 4: Interpretation, Limits and Dimensional Check

- Physical picture: layers slide over each other with uniform shear rate $U/H$; rotation and strain contribute equally, $\omega_z = -\dot\gamma$, so that $\lvert\Omega_z\rvert = \dot\gamma/2$. The principal strain axes are at $\pm 45^\circ$, as in any simple shear.
- Limits: $U \to 0$ gives rest ($\boldsymbol{\omega}$, $\bar{\bar{T}}_d$ and $\Gamma$ vanish); $H \to \infty$ at fixed $U$ gives vanishing shear rate. For $h \to 0$, $\Gamma \to 0$ linearly and $\Gamma/(hL) = -U/H = \omega_z$, which is Eq. (2.33): the circulation per unit area equals the normal component of the vorticity.
- Incompressibility: $\nabla\cdot\mathbf{v} = 0$, $\operatorname{tr}\bar{\bar{T}}_d = 0$ and $\lambda_1 + \lambda_2 = 0$ are mutually consistent.
- Dimensions (SI): $[U/H] = \text{s}^{-1}$ for $\omega_z$, $\nabla\mathbf{v}$, $\bar{\bar{T}}_d$ and the principal strain rates; $[\Gamma] = [UhL/H] = (\text{m/s})(\text{m})(\text{m})/\text{m} = \text{m}^2/\text{s}$; $[x(t)] = [Uy_0t/H] = \text{m}$.
- Symbolic cross-check: for the gradient above, the eigen-decomposition of $\bar{\bar{T}}_d$ returns eigenvalue $+U/2H$ with eigenvector $(1,1)$ and $-U/2H$ with eigenvector $(-1,1)$, which is $\mathbf{n}_2$ up to sign.

> [!note] Reading of the official handwritten solution
> K2.pdf states the final decomposition as a rotation with angular velocity $-U/2H$ plus a shear strain rate $U/H$, which agrees with the result above, and writes $\nabla\mathbf{v}$ with the same convention $(\nabla\mathbf{v})_{ij} = \partial_i v_j$ used here. No discrepancy was found in this problem.
