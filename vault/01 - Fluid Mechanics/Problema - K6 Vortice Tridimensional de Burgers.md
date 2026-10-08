---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - vortice-burgers
  - cilindricas
  - incompresibilidad
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-02-flow-kinematics/problemas/K6.pdf"
---

# Problem K6: Three-Dimensional Burgers Vortex

> Official UC3M kinematics problem collection (Introduction to Fluid Mechanics). Part of [[Tema 2 - Flow Kinematics]]. Related concepts: [[Concepto - Coordenadas Curvilineas y Operadores Diferenciales|cylindrical coordinates]], [[Concepto - Vorticidad, Circulacion y Potencial de Velocidades|vorticity and circulation]], [[Concepto - Descripcion Euleriana vs Lagrangiana y Lineas de Flujo|flow lines]].

## Statement

The axisymmetric velocity field corresponding to a three-dimensional steady vortex of circulation $\Gamma$ is given in cylindrical coordinates by

$$ v_r = -\frac{r}{\tau_r}, \qquad v_\theta = \frac{\Gamma}{2\pi r}\left\{1 - \exp\left[-\left(\frac{r}{R_o}\right)^2\right]\right\}, \qquad v_z = \frac{z}{\tau_z}, $$

where the constants $R_o$, $\tau_r$ and $\tau_z$ measure the radius of the inner core where viscous effects are important, and the characteristic times associated with radial convection and axial stretch, respectively.

1. Determine the condition required for the motion to be that of an incompressible fluid.
2. Compute streamlines and trajectories.

Source: K6.pdf (page 1). Notes.pdf, Chapter 2: divergence in orthogonal coordinates Eq. (2.5) with the cylindrical scale factors $(1, r, 1)$; incompressibility Eq. (2.38) and (2.63); trajectories Eqs. (2.12)-(2.13); stream lines Eq. (2.21).

## Phase 1: Hypotheses, Degrees of Freedom and Data

- Steady, axisymmetric, three-dimensional flow with three velocity components $(v_r, v_\theta, v_z)$ that depend on $r$ and $z$ only. A particle has three degrees of freedom $(r, \theta, z)$.
- $R_o$, $\tau_r$ and $\tau_z$ are positive constants: $v_r < 0$ is an inflow (radial convection towards the axis) and $v_z$ has the sign of $z$ (axial stretching away from the plane $z=0$).
- The vortex has circulation $\Gamma$ far from the core, $r v_\theta \to \Gamma/2\pi$; the Gaussian factor regularises the axis.
- The velocity is smooth at $r = 0$: expanding the exponential, $v_\theta \simeq \Gamma r/(2\pi R_o^2)$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $\Gamma$ | circulation of the vortex | m$^2$/s |
| $R_o$ | core radius | m |
| $\tau_r$ | time of radial convection | s |
| $\tau_z$ | time of axial stretching | s |
| $r, z$ | radial and axial coordinates | m |

## Phase 2: Coordinates, Frames and Changes of Variable

- Inertial frame with the vortex axis along $z$; cylindrical coordinates $(r,\theta,z)$ with scale factors $(1, r, 1)$ and basis $(\mathbf{e}_r,\mathbf{e}_\theta,\mathbf{e}_z)$.
- Divergence (Eq. 2.5 with $h_1 = 1$, $h_2 = r$, $h_3 = 1$): $\nabla\cdot\mathbf{v} = \dfrac{1}{r}\left[\dfrac{\partial(rv_r)}{\partial r} + \dfrac{\partial v_\theta}{\partial\theta} + \dfrac{\partial(rv_z)}{\partial z}\right]$.
- Lagrangian labels: $(r_0,\theta_0,z_0)$ at $t = 0$. The change of variable $t \to r$ along a trajectory, $dt = -\tau_r\,dr/r$ (from the radial equation), will be used to integrate the azimuthal motion; the substitution $u = r^2$ is then used for the primitive.
- The trajectory system is not coupled in the cylindrical basis for $r$ and $z$ (each depends only on its own coordinate), and $\theta$ follows from $r(t)$.

## Phase 3: Step-by-Step Derivation

### 3.1 Condition for incompressibility

Why this tool: for a liquid (constant density) the volume of a fluid element cannot change, which requires $\nabla\cdot\mathbf{v} = 0$ at every point (Eqs. 2.38 and 2.63).
$$ \nabla\cdot\mathbf{v} = \frac{1}{r}\left[\frac{\partial}{\partial r}\left(-\frac{r^2}{\tau_r}\right) + \frac{\partial v_\theta}{\partial\theta} + r\frac{\partial}{\partial z}\left(\frac{z}{\tau_z}\right)\right] = \frac{1}{r}\left[-\frac{2r}{\tau_r} + 0 + \frac{r}{\tau_z}\right] = -\frac{2}{\tau_r} + \frac{1}{\tau_z}, $$
where $\partial_\theta v_\theta = 0$ because $v_\theta$ does not depend on $\theta$ (axisymmetry). The expansion rate is the same constant everywhere, and it vanishes if and only if
$$ \boxed{\,\tau_r = 2\tau_z.\,} $$
The radial inflow convergence ($2/\tau_r$) must be exactly balanced by the axial stretching ($1/\tau_z$).

### 3.2 Trajectories

Why this tool: trajectories solve $d\mathbf{x}/dt = \mathbf{v}$ (Eq. 2.12) with $(r,\theta,z)(0) = (r_0,\theta_0,z_0)$. In cylindrical coordinates the components are $dr/dt = v_r$, $r\,d\theta/dt = v_\theta$, $dz/dt = v_z$.

Radial motion:
$$ \frac{dr}{dt} = -\frac{r}{\tau_r} \;\Longrightarrow\; \int_{r_0}^{r}\frac{dr'}{r'} = -\frac{1}{\tau_r}\int_0^t dt' \;\Longrightarrow\; \ln\frac{r}{r_0} = -\frac{t}{\tau_r} \;\Longrightarrow\; \boxed{\,r = r_0\,e^{-t/\tau_r}.\,} $$
Axial motion:
$$ \frac{dz}{dt} = \frac{z}{\tau_z} \;\Longrightarrow\; \ln\frac{z}{z_0} = \frac{t}{\tau_z} \;\Longrightarrow\; \boxed{\,z = z_0\,e^{t/\tau_z}.\,} $$
Azimuthal motion:
$$ \frac{d\theta}{dt} = \frac{\Gamma}{2\pi r^2}\left[1 - e^{-(r/R_o)^2}\right]. $$
Change of variable from $t$ to $r$ using $dt = -\tau_r\,dr/r$:
$$ d\theta = -\frac{\Gamma\tau_r}{2\pi}\,\frac{1 - e^{-(r/R_o)^2}}{r^3}\,dr \;\Longrightarrow\; \theta - \theta_0 = -\frac{\Gamma\tau_r}{2\pi}\int_{r_0}^{r}\frac{1 - e^{-(s/R_o)^2}}{s^3}\,ds. $$
Substitute $u = s^2$, $du = 2s\,ds$, so $ds/s^3 = du/(2u^2)$, and write $a = 1/R_o^2$:
$$ \theta - \theta_0 = -\frac{\Gamma\tau_r}{4\pi}\int_{r_0^2}^{r^2}\frac{1 - e^{-au}}{u^2}\,du. $$
A primitive is $G(u) = -\dfrac{1 - e^{-au}}{u} - a\,E_1(au)$, where $E_1(x) = \int_x^\infty e^{-s}\,ds/s$ is the exponential integral, $E_1'(x) = -e^{-x}/x$. Check by differentiation:
$$ G'(u) = \frac{1 - e^{-au}}{u^2} - \frac{a\,e^{-au}}{u} + a\cdot\frac{e^{-au}}{u} = \frac{1 - e^{-au}}{u^2}. $$
Barrow's rule between $u = r_0^2$ and $u = r^2$ gives
$$ \boxed{\,\theta - \theta_0 = -\frac{\Gamma\tau_r}{4\pi}\left[G(r^2) - G(r_0^2)\right],\qquad r = r_0e^{-t/\tau_r},\,} $$
which gives $\theta(t)$ explicitly once $r(t)$ is inserted. Two limits of the integral: for a particle inside the core ($r_0, r \ll R_o$), $1 - e^{-s^2/R_o^2} \simeq s^2/R_o^2$ and $\theta - \theta_0 \simeq -\frac{\Gamma\tau_r}{2\pi R_o^2}\ln\frac{r}{r_0} = \frac{\Gamma}{2\pi R_o^2}\,t$ (solid-body rotation with angular velocity $\Gamma/2\pi R_o^2$); for $r_0, r \gg R_o$, the bracket tends to $1$ and $\theta - \theta_0 \simeq \frac{\Gamma\tau_r}{4\pi}\left(\frac{1}{r^2} - \frac{1}{r_0^2}\right)$, i.e. the angle advances ever faster as the particle is convected inwards (conservation of $rv_\theta$).

Path lines: eliminate $t$. The relation $\theta(r)$ above is already time-free. For the axial coordinate, $t = -\tau_r\ln(r/r_0)$ and $z = z_0e^{t/\tau_z} = z_0(r/r_0)^{-\tau_r/\tau_z}$; with the incompressibility condition $\tau_r/\tau_z = 2$:
$$ \boxed{\,z\,r^2 = z_0\,r_0^2.\,} $$

### 3.3 Streamlines

Why this tool: the flow is steady, so streamlines and path lines coincide as curves; they are still obtained from the tangency condition (Eq. 2.21 with scale factors $1, r, 1$):
$$ \frac{dr}{v_r} = \frac{r\,d\theta}{v_\theta} = \frac{dz}{v_z}. $$
First equality with the third: $\dfrac{dr}{-r/\tau_r} = \dfrac{dz}{z/\tau_z} \Rightarrow \dfrac{dz}{z} = -\dfrac{\tau_r}{\tau_z}\dfrac{dr}{r} \Rightarrow \ln\dfrac{z}{z_0} = -\dfrac{\tau_r}{\tau_z}\ln\dfrac{r}{r_0}$, i.e. $\left(z/z_0\right)^{\tau_z} = \left(r/r_0\right)^{-\tau_r}$, which with $\tau_r = 2\tau_z$ is $z\,r^2 = z_0\,r_0^2$. First equality alone: $d\theta = \dfrac{v_\theta}{r\,v_r}\,dr = -\dfrac{\Gamma\tau_r}{2\pi}\dfrac{1 - e^{-(r/R_o)^2}}{r^3}\,dr$, the same relation as in 3.2. Hence
$$ \boxed{\,\theta - \theta_0 = -\frac{\Gamma\tau_r}{4\pi}\left[G(r^2) - G(r_0^2)\right],\qquad z\,r^2 = z_0\,r_0^2\,}$$
are the streamlines: spirals winding around the axis on the surfaces $zr^2 = $ const, tightening as they approach the axis. They are traversed with the time law $r = r_0e^{-t/\tau_r}$.

## Phase 4: Interpretation, Limits and Dimensional Check

- Physical picture: a vortex of circulation $\Gamma$ whose core is sustained against viscous diffusion by the radial inflow and the axial strain; vortex lines are stretched along $z$ while the core shrinks. For $r \gg R_o$ the flow is the irrotational vortex $v_\theta \to \Gamma/2\pi r$, and for $r \ll R_o$ it is a rigid rotation with vorticity $\omega_z = \Gamma/(\pi R_o^2)$. In general $\omega_z = r^{-1}\partial_r(rv_\theta) = \dfrac{\Gamma}{\pi R_o^2}e^{-r^2/R_o^2}$, a Gaussian vorticity distribution whose integral over the plane is $\Gamma$.
- Volume check: a ring of fluid with radius $r$ and height $z$ conserves $r^2z$ (3.2), as required by $\nabla\cdot\mathbf{v} = 0$. For general $\tau_r$ and $\tau_z$ the product evolves as $r^2z = r_0^2z_0\exp\left[(1/\tau_z - 2/\tau_r)\,t\right] = r_0^2z_0\exp\left[(\nabla\cdot\mathbf{v})\,t\right]$, which is constant exactly when $\tau_r = 2\tau_z$.
- Axis and plane: $r = 0$ and $z = 0$ are invariant (a particle on the axis only moves along it; a particle in the plane $z = 0$ stays in it).
- Dimensions (SI): $[r/\tau_r] = \text{m/s}$; $[\Gamma/2\pi r] = (\text{m}^2/\text{s})/\text{m} = \text{m/s}$; $[z/\tau_z] = \text{m/s}$; $[\nabla\cdot\mathbf{v}] = [1/\tau] = \text{s}^{-1}$; in the integral for $\theta$, $[\Gamma\tau_r/(4\pi)]\cdot[1/u] = (\text{m}^2/\text{s})(\text{s})(1/\text{m}^2)$ is dimensionless, as an angle must be; $a = 1/R_o^2$ has units m$^{-2}$ so $au$ is dimensionless.
- Numerical cross-check with $\Gamma = 1.4$ m$^2$/s, $R_o = 0.8$ m, $\tau_r = 1.3$ s, $\tau_z = 0.65$ s, initial point $(r_0,\theta_0,z_0) = (1.1\ \text{m}, 0.3\ \text{rad}, 0.7\ \text{m})$, $t = 0.9$ s: RK4 integration of the particle ODE gives $r = 0.550462$ m (formula $r_0e^{-t/\tau_r}$: same), $zr^2 = 0.847000$ m$^3$ (same as $z_0r_0^2$), and $\theta - \theta_0 = 0.2000243$ rad, which is also what the $E_1$ expression and a direct quadrature of the integral in 3.2 return.

> [!note] Reading of the official handwritten solution
> K6.pdf obtains $\tau_r = 2\tau_z$, the radial and axial exponentials, the integral form for $\theta - \theta_0$ (left unevaluated) and the streamline relation $zr^2 = z_0r_0^2$; all agree with the above. Evaluating the integral in terms of the exponential integral $E_1$, and the core and far-field limits of $\theta(t)$, are added here.
