---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - fuente-puntual
  - esfericas
  - linea-fluida
  - tubo-corriente
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-02-flow-kinematics/problemas/K3.pdf"
---

# Problem K3: Three-Dimensional Point Source at the Origin

> Official UC3M kinematics problem collection (Introduction to Fluid Mechanics). Part of [[Tema 2 - Flow Kinematics]]. Related concepts: [[Concepto - Coordenadas Curvilineas y Operadores Diferenciales|curvilinear coordinates and differential operators]], [[Concepto - Descripcion Euleriana vs Lagrangiana y Lineas de Flujo|flow lines and fluid lines]], [[Concepto - Flujo Convectivo y Funcion de Corriente|convective flux]].

## Statement

A three-dimensional fluid source placed at the origin induces a radial motion given by $v_r = Q(t)/(4\pi r^2)$, with $v_\theta = v_\phi = 0$. Obtain:

1. Streamlines, trajectories and paths.
2. Equation for the fluid surface initially located at $r = R$.
3. Equation for the fluid line that corresponds at the initial instant with a circle of radius $R$ intersecting the origin.
4. Streamtube that intersects the circle defined by $r = R_1$ and $\theta = \theta_1$.
5. The velocity components in cartesian coordinates, as well as the corresponding streamlines and trajectories.
6. Equations for the streamlines and trajectories for an observer moving with velocity $U$.

Source: K3.pdf (page 1). Notes.pdf, Chapter 2: spherical coordinates and scale factors (Fig. 2.1, Eqs. 2.3-2.7), trajectories Eq. (2.12), fluid lines and surfaces Eqs. (2.16)-(2.20), stream lines and stream tubes Eq. (2.21), observer dependence of steadiness (text before Eq. 2.11), convective flux Eqs. (2.35)-(2.38).

## Phase 1: Hypotheses, Degrees of Freedom and Data

- Spherically symmetric, purely radial flow: $\mathbf{v} = \dfrac{Q(t)}{4\pi r^2}\mathbf{e}_r$ for $r > 0$. The field depends on $r$ and $t$ only. The point $r = 0$ is the source and is excluded from the domain.
- $Q(t)$ is the volume flux emitted by the source (volume per unit time) and is a given function of time, so the flow is unsteady in general.
- The accumulated emitted volume is $q(t) \equiv \int_0^t Q(t')\,dt'$ (volume). We assume $r^3 > 0$ for all particles considered (automatically true for $Q \ge 0$).
- Each particle has three degrees of freedom $(r, \theta, \phi)$; the field acts on $r$ only, so $\theta$ and $\phi$ are conserved by each particle.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $Q(t)$ | source strength (volume flux) | m$^3$/s |
| $q(t)$ | emitted volume | m$^3$ |
| $r_0, R, R_1$ | initial radius, radius of the initial surface/circle, radius of the circle of part 4 | m |
| $\theta, \phi$ | polar angle (from $+z$) and azimuth | rad |
| $U$ | speed of the observer along $x$ | m/s |

## Phase 2: Coordinates, Frames and Changes of Variable

- Spherical coordinates $(r,\theta,\phi)$ with polar axis $z$ and scale factors $(1, r, r\sin\theta)$ (Notes, Section on coordinate systems): $x = r\sin\theta\cos\phi$, $y = r\sin\theta\sin\phi$, $z = r\cos\theta$, $r = (x^2+y^2+z^2)^{1/2}$.
- Basis change used in part 5: $\mathbf{e}_r = (x\,\mathbf{e}_x + y\,\mathbf{e}_y + z\,\mathbf{e}_z)/r$.
- Frames: the laboratory frame $S$ (source at rest at the origin) for parts 1-5; for part 6 an inertial frame $S'$ moving with constant velocity $U\mathbf{e}_x$ relative to $S$, with axes parallel and coincident origins at $t=0$, so $x' = x - Ut$, $y' = y$, $z' = z$ and $\mathbf{v}' = \mathbf{v} - U\mathbf{e}_x$ (Galilean change of observer; no inertial terms because $S'$ is not accelerated, cf. Eq. 2.28).
- Lagrangian labels: initial position $(r_0, \theta_0, \phi_0)$.

## Phase 3: Step-by-Step Derivation

### 3.1 Streamlines, trajectories and paths

Why this tool: streamlines come from the tangency condition (Eq. 2.21, here with scale factors $1$, $r$, $r\sin\theta$); trajectories from the initial-value problem $d\mathbf{x}/dt = \mathbf{v}$ (Eqs. 2.12-2.13).

Streamlines at a frozen instant:
$$ \frac{dr}{v_r} = \frac{r\,d\theta}{v_\theta} = \frac{r\sin\theta\,d\phi}{v_\phi}. $$
With $v_\theta = v_\phi = 0$ the second and third ratios are only compatible with $d\theta = 0$ and $d\phi = 0$, i.e. $\theta = \theta_0$ and $\phi = \phi_0$: the streamlines are straight rays through the origin, at every instant.

Trajectories, from $(r_0,\theta_0,\phi_0)$ at $t = 0$:
$$ r\frac{d\theta}{dt} = 0, \quad r\sin\theta\frac{d\phi}{dt} = 0 \;\Longrightarrow\; \theta(t) = \theta_0,\ \phi(t) = \phi_0, \qquad \frac{dr}{dt} = \frac{Q(t)}{4\pi r^2}. $$
Separate variables and integrate with Barrow's rule between $(r_0, 0)$ and $(r, t)$:
$$ \int_{r_0}^{r}4\pi r'^2\,dr' = \int_0^t Q(t')\,dt' \;\Longrightarrow\; \frac{4\pi}{3}\left[r'^3\right]_{r_0}^{r} = q(t) \;\Longrightarrow\; \boxed{\,\frac{4\pi}{3}\left(r^3 - r_0^3\right) = q(t) = \int_0^t Q\,dt',\,} $$
$$ r(t) = \left[r_0^3 + \frac{3}{4\pi}\,q(t)\right]^{1/3}. $$
Because $\theta$ and $\phi$ never change, the path lines are the same rays as the streamlines, but the particle moves along them with the time law above. The physical content of the boxed equation is volume conservation: the sphere of radius $r$ contains the sphere of radius $r_0$ plus the emitted volume.

### 3.2 Fluid surface initially at $r = R$

Why this tool: a fluid surface is the set of trajectories of the particles of the initial surface (Eqs. 2.18-2.20). The initial surface is $\mathbf{x}_s(\alpha,\beta) = (r_0 = R,\ \theta_0 = \alpha,\ \phi_0 = \beta)$ with $\alpha \in [0,\pi]$, $\beta\in[0,2\pi)$.

Apply 3.1 with $r_0 = R$ and $\theta = \alpha$, $\phi = \beta$:
$$ \frac{4\pi}{3}\left(r^3 - R^3\right) = q(t), \quad \theta = \alpha, \quad \phi = \beta. $$
The parameters $\alpha, \beta$ are the spherical angles themselves, so eliminating them leaves a relation in $r$ and $t$ only:
$$ \boxed{\,r(t) = \left[R^3 + \frac{3}{4\pi}\int_0^t Q\,dt'\right]^{1/3}.\,} $$
The fluid surface remains a sphere centred at the source; the volume it encloses grows exactly by the emitted volume $q(t)$.

### 3.3 Fluid line initially a circle of radius $R$ through the origin

Why this tool: the fluid line is again the image of the initial curve under the trajectories (Eq. 2.17); the label of the curve is eliminated at the end.

Initial curve. Take the circle in the plane $\phi = 0$ (the $x$-$z$ plane), tangent to the $x$-axis at the origin, with centre $(x,z) = (0,R)$. In polar form this circle is $r_0 = 2R\cos\lambda$, where $\lambda \in (-\pi/2, \pi/2)$ is the signed polar angle from the $z$-axis (negative $\lambda$ labels the half-plane $\phi = \pi$). Check: $x_0 = r_0\sin\lambda = R\sin 2\lambda$ and $z_0 = r_0\cos\lambda = R(1 + \cos 2\lambda)$, so $x_0^2 + (z_0 - R)^2 = R^2\left(\sin^2 2\lambda + \cos^2 2\lambda\right) = R^2$. The origin corresponds to $\lambda \to \pm\pi/2$, $r_0 \to 0$.

Evolution: from 3.1, $\theta = \lambda$, $\phi$ unchanged and
$$ \frac{4\pi}{3}\left(r^3 - 8R^3\cos^3\lambda\right) = q(t). $$
Eliminate the label with $\lambda = \theta$ (the polar angle of the particle):
$$ \boxed{\,\frac{4\pi}{3}\left(r^3 - 8R^3\cos^3\theta\right) = \int_0^t Q\,dt' \;\Longleftrightarrow\; r(\theta,t) = \left[8R^3\cos^3\theta + \frac{3}{4\pi}\int_0^t Q\,dt'\right]^{1/3},\,} \qquad \lvert\theta\rvert < \tfrac{\pi}{2}. $$
At $t = 0$ it is $r = 2R\cos\theta$, the initial circle; for $t > 0$ the line is dilated, and the particle that started at the source ($\lambda = \pm\pi/2$) lies on the sphere $r = [3q/4\pi]^{1/3}$ in the plane of the circle.

> [!warning] Erratum in the official solution
> The handwritten K3.pdf (part 3) takes $r_0 = R\cos\lambda$ and writes $\frac{4\pi}{3}(r^3 - R^3\cos^3\theta) = \int_0^t Q\,dt'$. The polar equation $r = R\cos\theta$ is a circle of diameter $R$ (radius $R/2$), not of radius $R$; a circle of radius $R$ through the origin is $r = 2R\cos\theta$, which gives the factor $8R^3$ above. The two results coincide only after the substitution $R \to 2R$.

### 3.4 Streamtube through the circle $r = R_1$, $\theta = \theta_1$

Why this tool: a stream tube is the surface formed by the streamlines that cross a closed curve (Notes, after Eq. 2.21). The curve $r = R_1$, $\theta = \theta_1$ ($0 \le \phi < 2\pi$) is a horizontal circle of radius $R_1\sin\theta_1$ about the polar axis.

Each streamline through a point of that circle is the ray $\theta = \theta_1$, $\phi = \phi_0$ (3.1). The union over $\phi_0 \in [0, 2\pi)$ and all $r > 0$ gives
$$ \boxed{\,\theta = \theta_1,\,} $$
a right circular cone of half-angle $\theta_1$ with its vertex at the source. The value of $R_1$ does not matter: any circle $\theta=\theta_1$ generates the same cone.

Flux inside the tube. The solid angle of the cone is $2\pi(1 - \cos\theta_1)$, and $\mathbf{v}\cdot\mathbf{e}_r\,r^2 = Q/4\pi$ is independent of $r$, so the volume flux through any spherical cap of the cone is
$$ \int\mathbf{v}\cdot\mathbf{n}\,d\sigma = \frac{Q}{4\pi r^2}\cdot r^2\,2\pi(1-\cos\theta_1) = \frac{Q}{2}\left(1 - \cos\theta_1\right), $$
which is constant along the tube, as it must be since no fluid crosses a stream tube. For $\theta_1 = \pi$ it gives $Q$.

### 3.5 Cartesian components, streamlines and trajectories

Why this tool: the same field is written in the Cartesian basis, where the trajectory equations are three coupled equations that can be decoupled using the radial symmetry.

Using $\mathbf{e}_r = (x,y,z)/r$ and $v_r = Q/(4\pi r^2)$,
$$ \boxed{\,v_x = \frac{Q(t)}{4\pi}\frac{x}{(x^2+y^2+z^2)^{3/2}},\quad v_y = \frac{Q(t)}{4\pi}\frac{y}{(x^2+y^2+z^2)^{3/2}},\quad v_z = \frac{Q(t)}{4\pi}\frac{z}{(x^2+y^2+z^2)^{3/2}}.\,} $$
Streamlines (frozen $t$): the common factor $Q/4\pi r^3$ cancels in
$$ \frac{dx}{v_x} = \frac{dy}{v_y} = \frac{dz}{v_z} \;\Longrightarrow\; \frac{dx}{x} = \frac{dy}{y} = \frac{dz}{z} \;\Longrightarrow\; \ln\frac{\lvert x\rvert}{\lvert x_0\rvert} = \ln\frac{\lvert y\rvert}{\lvert y_0\rvert} = \ln\frac{\lvert z\rvert}{\lvert z_0\rvert}, $$
$$ \boxed{\,\frac{x}{x_0} = \frac{y}{y_0} = \frac{z}{z_0},\,} $$
the rays through the origin and the point $(x_0,y_0,z_0)$.

Trajectories: from the streamline relations the position vector stays proportional to its initial value, so $\rho \equiv x/x_0 = y/y_0 = z/z_0 > 0$ is a common factor (assume $x_0 \neq 0$; otherwise use a non-zero component) and $r = \rho\,r_0$. Then
$$ \frac{dx}{dt} = \frac{Q}{4\pi}\frac{x}{r^3} = \frac{Q}{4\pi}\frac{x_0^3}{r_0^3}\frac{1}{x^2} \;\Longrightarrow\; \int_{x_0}^{x}x'^2\,dx' = \frac{x_0^3}{4\pi r_0^3}\int_0^t Q\,dt' \;\Longrightarrow\; \frac{x^3 - x_0^3}{3} = \frac{x_0^3}{4\pi r_0^3}\,q(t), $$
where $x = \rho x_0$ and $r = \rho r_0$ were used in $x/r^3$. Hence $x^3 = x_0^3\left[1 + 3q/(4\pi r_0^3)\right]$, that is $\rho^3 = r^3/r_0^3 = 1 + 3q/(4\pi r_0^3)$, which is the law of 3.1, and $\mathbf{x}(t) = (r(t)/r_0)\,\mathbf{x}_0$.

### 3.6 Observer moving with velocity $U$

Why this tool: steadiness depends on the observer (Notes, text before Eq. 2.11), so the flow lines of the source seen from $S'$ must be recomputed from the transformed field, with the lab position written in terms of the observer coordinates. The source is fixed in $S$ (the statement gives the flow induced by a source placed at the origin of the lab), so in $S'$ it sits at $x' = -Ut$.

With $x = x' + Ut$, $y = y'$, $z = z'$, define $\xi \equiv x' + Ut$ and $\rho_s^2 \equiv \xi^2 + y'^2 + z'^2$. Then
$$ v'_x = \frac{Q(t)}{4\pi}\frac{\xi}{\rho_s^3} - U, \qquad v'_y = \frac{Q(t)}{4\pi}\frac{y'}{\rho_s^3}, \qquad v'_z = \frac{Q(t)}{4\pi}\frac{z'}{\rho_s^3}. $$
The relative field depends explicitly on $t$ through $Ut$ and $Q(t)$ even when $Q$ is constant, so it is unsteady.

Trajectories relative to the observer. A fluid particle has lab trajectory $\mathbf{x}(t) = (r(t)/r_0)\,\mathbf{x}_0$ (3.5). Its position in $S'$ is $\mathbf{x}'(t) = \mathbf{x}(t) - Ut\,\mathbf{e}_x$:
$$ \boxed{\,\mathbf{x}'(t) = r(t)\,\mathbf{e}_r(\theta_0,\phi_0) - Ut\,\mathbf{e}_x,\qquad r(t) = \left[r_0^3 + \tfrac{3}{4\pi}q(t)\right]^{1/3}.\,} $$
These curves are generally curved (a radial motion with decreasing speed plus a uniform drift), and satisfy $d\mathbf{x}'/dt = \mathbf{v}'(\mathbf{x}',t)$ by construction.

Streamlines at a frozen instant $t$. The relative field is axisymmetric about the $x'$-axis through the source. Write $\varpi^2 = y'^2 + z'^2$. Away from the source $\nabla\cdot\mathbf{v}' = 0$, and for such axisymmetric fields the Stokes stream function $\Psi$ with $v'_\xi = \varpi^{-1}\partial_\varpi\Psi$, $v'_\varpi = -\varpi^{-1}\partial_\xi\Psi$ exists; then $d\Psi = -\varpi\left(v'_\varpi\,d\xi - v'_\xi\,d\varpi\right) = 0$ along streamlines. For the source plus the uniform stream $-U\mathbf{e}_x$,
$$ \Psi = -\frac{Q(t)}{4\pi}\frac{\xi}{\rho_s} - \frac{U}{2}\varpi^2, $$
which reproduces $v'_\xi = \tfrac{Q}{4\pi}\xi/\rho_s^3 - U$ and $v'_\varpi = \tfrac{Q}{4\pi}\varpi/\rho_s^3$ (checked symbolically). The instantaneous streamlines are therefore the curves, in each meridian plane $\phi' = $ const,
$$ \boxed{\,\frac{Q(t)}{4\pi}\frac{\xi}{\rho_s} + \frac{U}{2}\left(y'^2 + z'^2\right) = \text{const},\qquad \xi = x' + Ut,\,} $$
equivalently the ODE system $dx'/v'_x = dy'/v'_y = dz'/v'_z$ at frozen $t$. On the axis ($\varpi = 0$, $\xi > 0$) the velocity vanishes at $\xi_s = \sqrt{Q/(4\pi U)}$ (a stagnation point, Eq. 2.11), and the streamline through it, $\tfrac{Q}{4\pi}\left(1 - \xi/\rho_s\right) = \tfrac{U}{2}\varpi^2$, is the instantaneous half-body of revolution, whose far-wake radius $\varpi_\infty = \sqrt{Q/(\pi U)}$ satisfies $Q = U\pi\varpi_\infty^2$.

> [!warning] Unfinished official solution
> K3.pdf stops at part 6 with the note "to be continued" and writes $v'_x = \frac{Q}{4\pi}\frac{x}{(x^2+y^2+z^2)^{3/2}} - U$ with unshifted coordinates. That expression is correct only if the source moves together with the observer (source at $x' = 0$), which is a different, steady problem (a point source in a uniform stream, a half-body of revolution for constant $Q$). For a source fixed in the laboratory, the source sits at $x' = -Ut$ and the field is the shifted, unsteady one derived above.

## Phase 4: Interpretation, Limits and Dimensional Check

- Mass conservation: $\nabla\cdot\mathbf{v} = r^{-2}\,\partial_r\!\left(r^2v_r\right) = r^{-2}\,\partial_r\!\left[Q/4\pi\right] = 0$ for $r > 0$, and the flux through any sphere centred at the source is $4\pi r^2 v_r = Q$, independent of $r$ (the whole emitted flux). The fluid surface of 3.2 and the equation $\tfrac{4\pi}{3}(r^3-R^3) = q$ express the same fact.
- Late-time behaviour: for constant $Q$, $r \simeq (3Qt/4\pi)^{1/3}$, so the radial speed $dr/dt = Q/(4\pi r^2) \propto t^{-2/3}$ decays; for $t \to 0$ and $r_0 > 0$, $r \to r_0$.
- Observer limit: for $U \to 0$ the quantities of 3.6 reduce to those of 3.1-3.5 (streamlines $\tfrac{\xi}{\rho_s} = $ const, i.e. rays).
- Dimensions (SI): $[v_r] = [Q/r^2] = (\text{m}^3/\text{s})/\text{m}^2 = \text{m/s}$; $[q] = \text{m}^3$ and $[\tfrac{4\pi}{3}r^3] = \text{m}^3$; $[\xi_s] = [\sqrt{Q/U}] = \sqrt{\text{m}^3/\text{s}\cdot\text{s}/\text{m}} = \text{m}$; $[\Psi] = [Q/4\pi] = [U\varpi^2] = \text{m}^3/\text{s}$.
- Numerical cross-check (RK4 integration of the particle ODE against the closed form), with $Q(t) = Q_0(1 + 0.5\sin t)$, $Q_0 = 2.0$ m$^3$/s, $U = 0.7$ m/s, initial point $(0.8, 0.5, 0.3)$ m, $t = 3$ s: lab radius $1.4223654$ m (both) with the direction cosines unchanged; relative position $(-0.950555,\ 0.718403,\ 0.431042)$ m from the ODE in $S'$ and from the formula of 3.6 (agreement to $10^{-11}$ m). The circle of 3.3 satisfies $x_0^2 + (z_0 - R)^2 = R^2$ to machine precision for $R = 1.3$ m, $\lambda = 0.7$. The Stokes stream function reproduces the components of $\mathbf{v}'$ exactly (symbolic).
