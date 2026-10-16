---
materia: Fluid Mechanics
tema: "Topic 4: The Navier-Stokes Equations"
tags:
  - problema-examen
  - navier-stokes
  - simetria-esferica
  - succion
  - conduccion
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-04-navier-stokes/problemas/NS6.pdf"
id: "ns6"
pill: "NS6: Porous sphere"
tags_html:
  - "Spherical symmetry"
  - "Suction"
  - "Trajectory and time"
  - "Convection-conduction"
---

# Problem NS6: Sphere with Radial Suction

> Official UC3M Navier-Stokes problem collection (Introduction to Fluid Mechanics). Part of [[Topic 4 - The Navier-Stokes Equations]]. Related: [[Concept - Navier-Poisson Constitutive Equation|Navier-Poisson law]], [[Concept - Fourier's Law and Heat Conduction|Fourier's law]], [[Formula Sheet - Topic 3 Conservation Laws|Topic 3 formula sheet]].
> Method: the statement is transcribed word for word; the solution follows the four phases (setup, frames and field form, step-by-step derivation, interpretation), with continuity and each component of the Navier-Stokes equations simplified term by term and every integration constant fixed with its boundary condition.

## Statement

A sphere of radius $a$ is immersed in a liquid of density $\rho$, viscosity $\mu$, thermal conductivity $k$, and specific heat $c$. The liquid is sucked with radial velocity $v_r = -V_o$ through the porous surface of the sphere. For the buoyancy-free, steady sphericosymmetrical motion induced in the surrounding liquid,

1. Obtain the velocity $v_r(r)$

2. Compute the trajectory of a fluid particle initially located at $r = r_i > a$, as well as the time $t_i$ at which the fluid particle is sucked by the sphere.

3. Determine the pressure distribution $p - p_\infty$, where $p_\infty$ is the pressure value far from the sphere.

4. Calculate the temperature distribution in the liquid $T(r)$ assuming that the temperature of the sphere is $T_s$, smaller then the value $T_\infty$ found in the surrounding ambient atmosphere.

5. Obtain the amount of heat transfered to the sphere per unit time.

Transcribed as printed: "sphericosymmetrical", "then" (for "than") and "transfered" are spelling errors of the sheet. The sheet carries no printed figure.

Source: NS6.pdf (page 1). Notes.pdf, Chapter 4: continuity Eq. 4.40, momentum Eq. 4.41 and energy Eq. 4.42 in spherical coordinates, viscous dissipation $\phi_v$ in spherical coordinates.

## Phase 1: Hypotheses, Data and Unknowns

- Steady, spherically symmetric flow of a perfect liquid (constant $\rho$, $\mu$, $k$, $c$): $\bar{v} = v_r(r)\,\bar{e}_r$, $v_\theta = v_\phi = 0$, $\partial/\partial\theta = \partial/\partial\phi = \partial/\partial t = 0$.
- Buoyancy-free: the mass force is neglected. No chemical reaction and no radiation. The temperature depends only on $r$.
- Suction: the porous sphere takes liquid in at the rate $4\pi a^2V_o$, with $V_o > 0$. Far from the sphere the liquid is at rest at $p_\infty$ and $T_\infty$.
- Data: $[\rho,\ \mu,\ k,\ c,\ a,\ V_o,\ T_s,\ T_\infty,\ p_\infty,\ r_i]$ with $T_s < T_\infty$. Unknowns: $v_r(r)$, $r(t)$, $t_i$, $p(r)$, $T(r)$ and the heat rate to the sphere.
- Dimensionless numbers used: the suction Péclet number $\mathrm{Pe} = \rho c a V_o/k$ and the length $\beta = \rho c a^2V_o/k = a\,\mathrm{Pe}$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $a$ | sphere radius | m |
| $V_o$ | suction velocity at the sphere surface | m/s |
| $r_i$, $t_i$ | initial position of the particle, time to reach the sphere | m, s |
| $T_s$, $T_\infty$ | sphere and ambient temperatures | K |
| $\mathrm{Pe}$, $\beta$ | suction Péclet number, length $\beta = a\,\mathrm{Pe}$ | 1, m |
| $\Delta T_d = 12\mu V_o/(\rho c a)$ | temperature scale of the viscous heating | K |

## Phase 2: Frames, Field Form and Boundary Conditions

- Spherical frame $(r,\theta,\phi)$ centred on the sphere; $\bar{e}_r$ points away from the centre; the liquid occupies $r > a$.
- Field form: $\bar{v} = v_r(r)\,\bar{e}_r$, $p = p(r)$, $T = T(r)$.

| Location | Condition | Origin |
| :--- | :--- | :--- |
| $r = a$ | $v_r = -V_o$ | suction through the porous surface |
| $r \to \infty$ | $p \to p_\infty$ | statement |
| $r = a$ | $T = T_s$ | temperature of the sphere |
| $r \to \infty$ | $T \to T_\infty$ | ambient temperature |

## Phase 3: Step-by-Step Derivation

### 3.1 Continuity and the radial velocity

$$ \frac{1}{r^2}\frac{d(r^2v_r)}{dr} = 0 \;\Longrightarrow\; r^2v_r = \text{const} = -a^2V_o \tag{1} $$

where the constant is fixed with $v_r(a) = -V_o$:

$$ \boxed{\,v_r(r) = -\frac{a^2V_o}{r^2}\,} \tag{2} $$

### 3.2 Trajectory and suction time

A fluid particle moves with the local velocity: $dr/dt = v_r = -a^2V_o/r^2$. Separating variables, $r^2\,dr = -a^2V_o\,dt$. Integrating from $r_i$ at $t = 0$:

$$ \frac{r^3 - r_i^3}{3} = -a^2V_o\,t \;\Longrightarrow\; \boxed{\,r(t) = \left(r_i^3 - 3a^2V_o\,t\right)^{1/3}\,} \tag{3} $$

The particle is sucked when $r = a$: $a^3 = r_i^3 - 3a^2V_o\,t_i$, so

$$ \boxed{\,t_i = \frac{r_i^3 - a^3}{3\,a^2V_o}\,} \tag{4} $$

### 3.3 Pressure distribution

In the $r$ component of (4.41) the viscous term $\mu\,\partial\left[r^{-2}\partial(r^2v_r)/\partial r\right]/\partial r$ vanishes because $r^2v_r$ is constant (1): the flow is irrotational. The rest is the steady Euler equation:

$$ \rho\,v_r\frac{dv_r}{dr} = -\frac{dp}{dr} \;\Longrightarrow\; p + \frac{\rho v_r^2}{2} = \text{const} = p_\infty \tag{5} $$

(the constant is evaluated at infinity, where $v_r \to 0$). Substituting (2):

$$ \boxed{\,p - p_\infty = -\frac{\rho\,a^4V_o^2}{2\,r^4}\,} \tag{6} $$

The pressure is below the ambient value, the minimum being at the sphere surface, where the liquid has the highest speed.

### 3.4 Temperature distribution

With $v_\theta = v_\phi = 0$ the energy equation (4.42) in spherical coordinates is

$$ \rho c\,v_r\frac{dT}{dr} = \phi_v + \frac{k}{r^2}\frac{d}{dr}\left(r^2\frac{dT}{dr}\right) \tag{7} $$

The viscous dissipation is $\phi_v = 2\mu\left[(dv_r/dr)^2 + 2(v_r/r)^2\right]$ with $dv_r/dr = 2a^2V_o/r^3$ and $v_r/r = -a^2V_o/r^3$:

$$ \phi_v = 2\mu\left[\frac{4a^4V_o^2}{r^6} + \frac{2a^4V_o^2}{r^6}\right] = \frac{12\mu\,a^4V_o^2}{r^6} \tag{8} $$

Substituting $v_r$ and $\phi_v$ in (7), dividing by $k$ and multiplying by $r^2$:

$$ \frac{d}{dr}\left(r^2\frac{dT}{dr}\right) + \beta\frac{dT}{dr} = -\frac{\Gamma}{r^4}, \qquad \beta = \frac{\rho c a^2V_o}{k}, \quad \Gamma = \frac{12\mu a^4V_o^2}{k} \tag{9} $$

*Homogeneous solution.* With $y = T'$: $r^2y' + (2r + \beta)y = 0$; the integrating factor is $\exp\int(2/r + \beta/r^2)\,dr = r^2e^{-\beta/r}$, so $y = D\,e^{\beta/r}/r^2$, and since $\int e^{\beta/r}r^{-2}dr = -e^{\beta/r}/\beta$:

$$ T_h = B_2 + B_1\,e^{\beta/r} \tag{10} $$

*Particular solution.* Work with $y = T_p'$ in the first-order form $r^2y' + (2r + \beta)y = -\Gamma/r^4$. The right-hand side is a power of $1/r$, so try a sum of powers, $y = -\Gamma\left(\dfrac{c_4}{r^4} + \dfrac{c_3}{r^3} + \dfrac{c_2}{r^2}\right)$, and match powers one at a time. The three terms of the equation are $r^2y' = \Gamma\left(\dfrac{4c_4}{r^3} + \dfrac{3c_3}{r^2} + \dfrac{2c_2}{r}\right)$, $2ry = -\Gamma\left(\dfrac{2c_4}{r^3} + \dfrac{2c_3}{r^2} + \dfrac{2c_2}{r}\right)$ and $\beta y = -\Gamma\left(\dfrac{\beta c_4}{r^4} + \dfrac{\beta c_3}{r^3} + \dfrac{\beta c_2}{r^2}\right)$. Their sum is $\Gamma\left[-\dfrac{\beta c_4}{r^4} + \dfrac{2c_4 - \beta c_3}{r^3} + \dfrac{c_3 - \beta c_2}{r^2}\right]$, which must equal $-\Gamma/r^4$: $c_4 = 1/\beta$, $c_3 = 2c_4/\beta = 2/\beta^2$ and $c_2 = c_3/\beta = 2/\beta^3$. Hence

$$ y = T_p' = -\Gamma\left(\frac{1}{\beta r^4} + \frac{2}{\beta^2r^3} + \frac{2}{\beta^3r^2}\right) $$

and integrating $y$ with respect to $r$ (the antiderivative of $r^{-n}$ is $-r^{1-n}/(n-1)$):

$$ T_p(r) = \Gamma\left(\frac{1}{3\beta r^3} + \frac{1}{\beta^2r^2} + \frac{2}{\beta^3r}\right) = \Delta T_d\left[\frac{1}{3}\left(\frac{a}{r}\right)^3 + \frac{1}{\mathrm{Pe}}\left(\frac{a}{r}\right)^2 + \frac{2}{\mathrm{Pe}^2}\frac{a}{r}\right] \tag{11} $$

with $\Delta T_d = 12\mu V_o/(\rho c a)$ (use $\Gamma/\beta = 12\mu a^2V_o/(\rho c)$ and $\beta = a\,\mathrm{Pe}$). The general solution is $T = B_2 + B_1e^{\beta/r} + T_p(r)$.

*Boundary conditions.* $T(\infty) = T_\infty$: $e^{\beta/r} \to 1$ and $T_p \to 0$, so $B_2 + B_1 = T_\infty$. $T(a) = T_s$: $B_2 + B_1e^{\mathrm{Pe}} + T_p(a) = T_s$, because $\beta/a = \mathrm{Pe}$. Subtracting,

$$ B_1 = -\frac{T_\infty - T_s + T_p(a)}{e^{\mathrm{Pe}} - 1}, \qquad T_p(a) = \Delta T_d\left(\frac{1}{3} + \frac{1}{\mathrm{Pe}} + \frac{2}{\mathrm{Pe}^2}\right) $$

$$ \boxed{\,T(r) = T_\infty + T_p(r) - \left[T_\infty - T_s + T_p(a)\right]\frac{e^{\mathrm{Pe}\,a/r} - 1}{e^{\mathrm{Pe}} - 1}\,} \tag{12} $$

> [!warning] Discrepancy with the official solution
> The handwritten solution gets the particular solution $12\mu V_o/(\rho c\,r)$, as read from the handwriting. Its ODE has the dissipation term as $12\mu V_o^2a^2/(k\,r^2)$, but multiplying $\phi_v/k$ of (8) by $r^2$ gives $12\mu a^4V_o^2/(k\,r^4)$, as in (9). The term $A/r$ cannot satisfy (9), whose right-hand side decays as $r^{-4}$: the check above shows that (11) does. The computed result (12) is kept; with $\Delta T_d \to 0$ (negligible dissipation) it reduces to the sheet's result $T = T_\infty + (T_s - T_\infty)\dfrac{e^{\mathrm{Pe}\,a/r} - 1}{e^{\mathrm{Pe}} - 1}$.

### 3.5 Heat transferred to the sphere

The heat that flows from the liquid into the sphere per unit time is $4\pi a^2\,\bar{q}\cdot\bar{n}$ with $\bar{n} = -\bar{e}_r$ (outward from the liquid) and $\bar{q} = -k\nabla T$, that is $\dot{Q}_s = 4\pi a^2k\,dT/dr\big|_a$. From (12),

$$ \frac{dT}{dr}\Big|_a = T_p'(a) + \frac{\mathrm{Pe}}{a}\left[T_\infty - T_s + T_p(a)\right]\frac{e^{\mathrm{Pe}}}{e^{\mathrm{Pe}} - 1}, \qquad T_p'(a) = -\frac{\Delta T_d}{a}\left(1 + \frac{2}{\mathrm{Pe}} + \frac{2}{\mathrm{Pe}^2}\right) \tag{13} $$

Using $4\pi a\,k\,\mathrm{Pe} = 4\pi\rho c\,a^2V_o$ and $e^{\mathrm{Pe}}/(e^{\mathrm{Pe}} - 1) = 1/(1 - e^{-\mathrm{Pe}})$:

$$ \boxed{\,\dot{Q}_s = \frac{4\pi\rho c\,a^2V_o\left[T_\infty - T_s + T_p(a)\right]}{1 - e^{-\mathrm{Pe}}} - 4\pi a\,k\,\Delta T_d\left(1 + \frac{2}{\mathrm{Pe}} + \frac{2}{\mathrm{Pe}^2}\right)\,} \tag{14} $$

## Phase 4: Interpretation, Limits and Dimensional Check

- **Physical meaning.** The suction brings ambient liquid at $T_\infty$ towards the cold sphere, which compresses the thermal layer against the surface: $\beta = a\,\mathrm{Pe}$ is the length over which convection and conduction compete. Unlike the cylinder of NS9, the sphere has a regular solution for blowing too: for $V_o < 0$ the exponent $\mathrm{Pe}\,a/r$ changes sign but $e^{\mathrm{Pe}\,a/r} \to 1$ at infinity, so (12) still holds.
- **Limits.** For negligible dissipation ($\Delta T_d \to 0$): $\dot{Q}_s = 4\pi\rho ca^2V_o\,(T_\infty - T_s)/(1 - e^{-\mathrm{Pe}})$. For $\mathrm{Pe} \gg 1$ this is $\dot{m}\,c\,(T_\infty - T_s)$ with $\dot{m} = 4\pi\rho a^2V_o$ the sucked mass flow: the sphere only has to cool the liquid it takes in. For $\mathrm{Pe} \to 0$ it tends to $4\pi a k\,(T_\infty - T_s)$, pure conduction to a sphere in an unbounded medium.
- **Dimensional check.** $a^2V_o/r^2$ is a velocity. $\rho v_r^2$ in (6) is a pressure. $\beta = \rho ca^2V_o/k$ has units $(\mathrm{J/(m^3K)})\,\mathrm{m^3/s}/(\mathrm{W/(m\,K)}) = \mathrm{m}$. $\Delta T_d = 12\mu V_o/(\rho ca)$ has units $\mathrm{Pa\,s\cdot m/s}/[(\mathrm{Pa/K})\,\mathrm{m}] = \mathrm{K}$. $\dot{Q}_s$ in (14): $\rho ca^2V_o\,\Delta T$ has units $(\mathrm{Pa/K})\,\mathrm{m^3/s}\cdot\mathrm{K} = \mathrm{W}$.
- **Check of (11).** Differentiating the three terms of (11) and substituting in (9) reproduces $-\Gamma/r^4$ term by term, as written in 3.4.
