---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - potencial
  - tridimensional
  - superficie-fluida
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-02-flow-kinematics/problemas/K8.pdf"
---

# Problem K8: Pulsating Three-Dimensional Potential Flow

> Official UC3M kinematics problem collection (Introduction to Fluid Mechanics). Part of [[Tema 2 - Flow Kinematics]]. Related concepts: [[Concepto - Vorticidad, Circulacion y Potencial de Velocidades|vorticity and potential]], [[Concepto - Descripcion Euleriana vs Lagrangiana y Lineas de Flujo|fluid surfaces, path lines and stream lines]].

## Statement

The velocity potential of a three-dimensional flow field is given by

$$ \varphi = A\cos(\Omega t)\left(2x^2 - y^2 - z^2\right), $$

where $A$ and $\Omega$ are known constants.

1. Determine the velocity field, verifying that $\nabla\wedge\vec{v} = 0$ and $\nabla\cdot\vec{v} = 0$.
2. Compute the streamlines, trajectories and particle paths.
3. Obtain the fluid surface that at the initial instant is a sphere of radius $R$ centered at $(x,y,z) = (-R/2, 0, 0)$.

Source: K8.pdf (page 1). Notes.pdf, Chapter 2: potential Eq. (2.34); expansion rate Eqs. (2.37)-(2.38); trajectories and path lines Eqs. (2.12)-(2.15); fluid surfaces Eqs. (2.18)-(2.20); stream lines Eq. (2.21).

## Phase 1: Hypotheses, Degrees of Freedom and Data

- Three-dimensional, unsteady, potential flow, $\mathbf{v} = \nabla\varphi$, in all of space. The only time dependence is the common factor $\cos\Omega t$.
- Degrees of freedom: three coordinates $(x,y,z)$; the field is linear in them.
- Units: $\varphi$ is in m$^2$/s and multiplies a length squared, so $A$ has units s$^{-1}$.
- At the instants when $\cos\Omega t = 0$ the velocity vanishes everywhere; streamlines are defined only at the other instants.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $A$ | amplitude of the strain rate | s$^{-1}$ |
| $\Omega$ | angular frequency | s$^{-1}$ |
| $R$ | radius of the initial sphere | m |
| $(x_i,y_i,z_i)$ | initial position of a particle | m |
| $s(t) = (A/\Omega)\sin\Omega t$ | dimensionless time function, used below | 1 |

## Phase 2: Coordinates, Frames and Changes of Variable

- Inertial frame, Cartesian basis $(\mathbf{e}_x,\mathbf{e}_y,\mathbf{e}_z)$, origin at the centre of the field.
- Material (Lagrangian) variables: the initial position $(x_i,y_i,z_i)$ of a particle. The trajectories give the map $(x_i,y_i,z_i) \mapsto (x,y,z)$ at time $t$, and its inverse is used in part 3.
- Parametrisation of the initial sphere (Notes, footnote to Eq. 2.19): $x_i = -R/2 + R\sin\alpha\cos\beta$, $y_i = R\sin\alpha\sin\beta$, $z_i = R\cos\alpha$, with $0 \le \alpha \le \pi$ and $0 \le \beta < 2\pi$. This is a change of variable from the two surface labels $(\alpha,\beta)$ to the three coordinates, eliminated at the end.

## Phase 3: Step-by-Step Derivation

### 3.1 Velocity field, curl and divergence

Why this tool: $\mathbf{v} = \nabla\varphi$ (Eq. 2.34). Let $c \equiv \cos\Omega t$.
$$ v_x = \frac{\partial\varphi}{\partial x} = 4Acx, \qquad v_y = \frac{\partial\varphi}{\partial y} = -2Acy, \qquad v_z = \frac{\partial\varphi}{\partial z} = -2Acz, $$
$$ \boxed{\,\mathbf{v} = Ac\,(4x,\,-2y,\,-2z).\,} $$
Curl, component by component:
$$ \left(\nabla\wedge\mathbf{v}\right)_x = \partial_yv_z - \partial_zv_y = 0 - 0,\quad \left(\nabla\wedge\mathbf{v}\right)_y = \partial_zv_x - \partial_xv_z = 0 - 0,\quad \left(\nabla\wedge\mathbf{v}\right)_z = \partial_xv_y - \partial_yv_x = 0 - 0, $$
so $\nabla\wedge\mathbf{v} = 0$ (as for any gradient). Divergence:
$$ \nabla\cdot\mathbf{v} = \partial_x(4Acx) + \partial_y(-2Acy) + \partial_z(-2Acz) = Ac\,(4 - 2 - 2) = 0. $$
The potential satisfies $\nabla^2\varphi = A c\,(4 - 2 - 2) = 0$: it is harmonic, the flow is irrotational and incompressible for all $t$. The extension along $x$ is balanced by the compression along $y$ and $z$.

### 3.2 Streamlines, trajectories and path lines

Why this tool: streamlines come from the tangency condition at a frozen instant (Eq. 2.21), trajectories from the initial-value problem $d\mathbf{x}/dt = \mathbf{v}$ (Eq. 2.12), and path lines from eliminating $t$ (Eq. 2.15).

Streamlines (at an instant with $c \neq 0$ the common factor $Ac$ cancels):
$$ \frac{dx}{4x} = \frac{dy}{-2y} = \frac{dz}{-2z}. $$
From the last equality, $dy/y = dz/z \Rightarrow \ln\lvert y/y_0\rvert = \ln\lvert z/z_0\rvert \Rightarrow y/z = y_0/z_0$. From the first equality, $dx/x = -2\,dy/y \Rightarrow \ln\lvert x/x_0\rvert = -2\ln\lvert y/y_0\rvert \Rightarrow$
$$ \boxed{\,x\,y^2 = x_0\,y_0^2,\qquad \frac{y}{z} = \frac{y_0}{z_0},\,} $$
the intersection of two surfaces (Eq. 2.15 type), independent of $t$.

Trajectories, with $\mathbf{x}(0) = (x_i, y_i, z_i)$. Each component decouples. Using Barrow's rule and $\int_0^t\cos\Omega t'\,dt' = \sin(\Omega t)/\Omega$:
$$ \frac{dx}{dt} = 4A\cos(\Omega t)\,x \;\Rightarrow\; \int_{x_i}^{x}\frac{dx'}{x'} = 4A\int_0^t\cos\Omega t'\,dt' \;\Rightarrow\; \ln\frac{x}{x_i} = \frac{4A}{\Omega}\sin\Omega t, $$
$$ \frac{dy}{dt} = -2A\cos(\Omega t)\,y \;\Rightarrow\; \ln\frac{y}{y_i} = -\frac{2A}{\Omega}\sin\Omega t, \qquad \frac{dz}{dt} = -2A\cos(\Omega t)\,z \;\Rightarrow\; \ln\frac{z}{z_i} = -\frac{2A}{\Omega}\sin\Omega t. $$
With $s(t) = (A/\Omega)\sin\Omega t$:
$$ \boxed{\,x = x_i\,e^{4s(t)},\qquad y = y_i\,e^{-2s(t)},\qquad z = z_i\,e^{-2s(t)}.\,} $$
Path lines: eliminate $s$ (that is, $t$). From the last two, $y/z = y_i/z_i$. Raise $y/y_i = e^{-2s}$ to the power $-2$: $(y/y_i)^{-2} = e^{4s} = x/x_i$, hence $xy^2 = x_iy_i^2$:
$$ \boxed{\,x\,y^2 = x_i\,y_i^2,\qquad \frac{y}{z} = \frac{y_i}{z_i}.\,} $$
The path lines coincide with the streamlines of the flow (the direction field is steady; only the magnitude oscillates). The particles move back and forth along these curves: $s(t)$ oscillates between $\pm A/\Omega$, so $x/x_i$ oscillates between $e^{-4A/\Omega}$ and $e^{4A/\Omega}$, and each particle returns to its initial position whenever $\sin\Omega t = 0$.

### 3.3 Fluid surface that is initially a sphere of radius $R$ centred at $(-R/2, 0, 0)$

Why this tool: a fluid surface is the image under the trajectories of the initial surface (Eqs. 2.18-2.20); the surface labels $(\alpha,\beta)$ are then eliminated to obtain $f(x,y,z,t) = 0$.

Initial surface: $(x_i + R/2)^2 + y_i^2 + z_i^2 = R^2$, parametrised as in Phase 2. Trajectories map it to $x = x_i e^{4s}$, $y = y_ie^{-2s}$, $z = z_ie^{-2s}$, i.e. in terms of the labels,
$$ \frac{x}{-R/2 + R\sin\alpha\cos\beta} = e^{4s}, \qquad \frac{y}{R\sin\alpha\sin\beta} = e^{-2s}, \qquad \frac{z}{R\cos\alpha} = e^{-2s}. $$
Eliminate $(\alpha,\beta)$ by inverting the map, $x_i = x\,e^{-4s}$, $y_i = y\,e^{2s}$, $z_i = z\,e^{2s}$, and substituting in the equation of the initial sphere:
$$ \boxed{\,\left(x\,e^{-4s(t)} + \frac{R}{2}\right)^2 + \left(y\,e^{2s(t)}\right)^2 + \left(z\,e^{2s(t)}\right)^2 = R^2,\qquad s(t) = \frac{A}{\Omega}\sin\Omega t.\,} $$
This is an ellipsoid of revolution about the $x$-axis: its centre is at $x_c = -(R/2)\,e^{4s}$, its semi-axis along $x$ is $R\,e^{4s}$ and its semi-axes along $y$ and $z$ are $R\,e^{-2s}$. The enclosed volume is $\tfrac{4\pi}{3}\,Re^{4s}\,R^2e^{-4s} = \tfrac{4\pi}{3}R^3$, constant, as required for an incompressible flow ($\nabla\cdot\mathbf{v} = 0$). At every instant with $\sin\Omega t = 0$ the surface is again the initial sphere.

> [!warning] Reading of the official handwritten solution
> The statement fixes the centre at $(-R/2, 0, 0)$. In K8.pdf (part 3), as legible in the scan, the parametrisation is written $x_i - R/2 = R\sin\alpha\cos\beta$ and the final boxed equation contains $\left(xe^{-4A\sin(\Omega t)/\Omega} - R/2\right)^2$, which corresponds to a sphere centred at $x = +R/2$. For the sphere of the statement the sign in front of $R/2$ must be $+$, as derived above. Numerical test: for $R = 1$ m, $A = 0.6$ s$^{-1}$, $\Omega = 1.9$ s$^{-1}$, $t = 1.1$ s, a particle starting on the sphere of the statement ($\alpha = 0.8$, $\beta = 1.1$) satisfies the equation with $+R/2$ to $10^{-16}$, whereas the $-R/2$ form leaves a residual of $0.349$. The remaining handwritten results (components, streamlines, trajectories, paths) agree with the above.

## Phase 4: Interpretation, Limits and Dimensional Check

- Physical picture: a pulsating pure-strain (stagnation-type) flow: the material is stretched along $x$ and compressed in the $(y,z)$ plane during the half cycles where $\cos\Omega t > 0$, and the opposite sense when $\cos\Omega t < 0$. The net displacement over a full period is zero.
- Limits: $A \to 0$ gives $s \to 0$ and the surface stays the initial sphere; $\Omega \to 0$ with $c \to 1$ gives the steady flow $\mathbf{v} = A(4x,-2y,-2z)$, for which $s \to At$ and the sphere is deformed without bound; at $\sin\Omega t = 0$ every trajectory returns to its starting point.
- Consistency: path lines equal streamlines for this flow, since the unit vector $\mathbf{v}/\lvert\mathbf{v}\rvert$ is time-independent; the volume of the fluid surface is conserved ($\nabla\cdot\mathbf{v} = 0$).
- Dimensions (SI): $[v] = [Ax] = \text{s}^{-1}\text{m} = \text{m/s}$; $[s] = [A/\Omega] = 1$, so $e^{\pm ks}$ are dimensionless; the factors $e^{4s}$, $e^{-2s}$ multiply lengths; in the ellipsoid equation each term has units m$^2$ ($x\,e^{-4s} + R/2$ is a length).
- Numerical cross-check: RK4 integration of the particle ODE with $A = 0.6$ s$^{-1}$, $\Omega = 1.9$ s$^{-1}$ from $(0.5, 0.7, -0.4)$ m up to $t = 1.1$ s gives $(1.497122, 0.404533, -0.231162)$ m, the same as $x_ie^{4s}$, $y_ie^{-2s}$, $z_ie^{-2s}$ (agreement better than $10^{-11}$ m). Symbolic differentiation gives $\nabla\wedge\mathbf{v} = 0$ and $\nabla\cdot\mathbf{v} = 0$.
