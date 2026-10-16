---
materia: Fluid Mechanics
tema: "Topic 4: The Navier-Stokes Equations"
tags:
  - problema-examen
  - navier-stokes
  - cavidad-esferica
  - adimensionalizacion
  - ecuacion-diferencial
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-04-navier-stokes/problemas/NS10.pdf"
id: "ns10"
pill: "NS10: Cavity"
tags_html:
  - "Spherical symmetry"
  - "Null stress condition"
  - "Non-dimensionalization"
  - "Limits Re large and small"
---

# Problem NS10: Underwater Explosion Cavity

> Official UC3M Navier-Stokes problem collection (Introduction to Fluid Mechanics). Part of [[Topic 4 - The Navier-Stokes Equations]]. Related: [[Concept - Navier-Poisson Constitutive Equation|Navier-Poisson law]], [[Concept - Fourier's Law and Heat Conduction|Fourier's law]], [[Formula Sheet - Topic 3 Conservation Laws|Topic 3 formula sheet]].
> Method: the statement is transcribed word for word; the solution follows the four phases (setup, frames and field form, step-by-step derivation, interpretation), with continuity and each component of the Navier-Stokes equations simplified term by term and every integration constant fixed with its boundary condition.

## Statement

As a consequence of an underwater explosion, a spherical cavity of initial radius $R_0$ and initial radial velocity $V_0$ is created inside the ocean. The growth of the cavity induces a flow in the surrounding liquid, whose density $\rho$ and viscosity $\mu$ can be considered constant. It is also assumed that the effect of gravity is negligible, and that the motion is sphericosymmetric, $\bar{v} = v_r(r, t)\,\bar{e}_r$, where $R_c(t) \leq r < \infty$, being $R_c(t)$ the radius of the cavity at time $t$. The liquid is at rest far from the cavity, $r \to \infty$, where the pressure is $p_\infty$, while the pressure inside the cavity can be neglected compared to $p_\infty$.

1. (1.5 points). Find the radial velocity of the liquid, $v_r(r, t)$, as a function of the radius of the cavity, $R_c(t)$, and of its associated expansion velocity, $\dot{R}_c(t) = dR_c/dt$. Show that the resulting flow is irrotational.

2. (1.5 points). Obtain the pressure field, $p(r, t)$, as a function of $R_c(t)$, $\dot{R}_c(t)$, $\ddot{R}_c(t)$, $\rho$ and $p_\infty$.

3. (1 point). Evaluate the resulting pressure distribution at $r = R_c(t)$, to find the ordinary differential equation (ODE) with initial conditions satisfied by $R_c(t)$, in terms of the unknown liquid pressure at the cavity boundary, $p_R(t)$.

4. (1.5 points). Find $p_R(t)$ by imposing the condition of null stress of the liquid at the cavity wall, $\bar{\bar{\tau}}\cdot\bar{n}\big|_{r = R_c(t)} = 0$, where $\bar{\bar{\tau}} = -p\bar{\bar{I}} + \bar{\bar{\tau}}'$ is the stress tensor.

5. (1.5 points). Using the answer to question #4, write the ODE obtained in question #3 in closed form. Nondimensionalize the corresponding initial value problem, using the following dimensionless variables: $R = R_c/R_0$, $\tau = tV_0/R_0$. Show that the problem is governed by two dimensionless parameters, namely the Reynolds number, $\mathrm{Re} = \rho V_0R_0/\mu$, and $\Lambda = p_\infty/(\rho V_0^2)$.

6. (1.5 points). Simplify the ODE in the limit $\mathrm{Re} \to \infty$. By using $z = \ln(R)$ as the independent variable and $F = (dR/d\tau)^2$ as the dependent one, show that $F(z)$ satisfies the linear ODE
$$ \frac{dF}{dz} + 3F = -2\Lambda, $$
with initial condition $F(0) = 1$. Obtain $F(z)$, and use it to find $dR/d\tau$ as a function of $R$.

7. (1.5 points). Obtain the maximum radius of the cavity, $R_{\max}$, as a function of $\Lambda$, and show that the time $\tau_{\max}$, defined such that $R(\tau_{\max}) = R_{\max}$ is given by the integral
$$ \tau_{\max}(\Lambda) = \int_1^{(1 + \frac{3}{2\Lambda})^{1/3}}\frac{dx}{\sqrt{x^{-3} + \frac{2\Lambda}{3}\left(x^{-3} - 1\right)}}. $$
Provide an explicit approximation for $\tau_{\max}$ in the limit $\Lambda \ll 1$.

8. (1 additional point). Simplify the ODE found in question #5 in the limit $\mathrm{Re} \to 0$. Is it possible to satisfy the initial conditions? Find an approximate solution, and discuss its validity.

The sheet is headed "INTRODUCTION TO FLUID MECHANICS, Dec 18, 2012, PROBLEM 2 (1 hour)" and carries no figure; the spelling "sphericosymmetric" is the sheet's.

Source: NS10.pdf (page 1 of 3: statement; pages 2 and 3: handwritten solution). Notes.pdf, Chapter 4: continuity Eq. 4.40, momentum Eq. 4.41 in spherical coordinates, stress components in spherical coordinates.

## Phase 1: Hypotheses, Data and Unknowns

- Incompressible liquid with constant $\rho$ and $\mu$, spherically symmetric flow $\bar{v} = v_r(r,t)\,\bar{e}_r$ in $r > R_c(t)$, gravity neglected. Equations (4.40) and (4.41) in spherical coordinates.
- The cavity gas pressure is neglected compared with $p_\infty$: the liquid has no traction applied at the cavity wall (null stress). The liquid is at rest and at $p_\infty$ far away.
- Initial conditions: $R_c(0) = R_0$, $\dot{R}_c(0) = V_0$.
- Data: $[\rho,\ \mu,\ p_\infty,\ R_0,\ V_0]$. Unknowns: $v_r$, $p$, $p_R(t)$, the ODE for $R_c(t)$ and its non-dimensional limits.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $R_c(t)$, $\dot{R}_c$, $\ddot{R}_c$ | cavity radius, velocity and acceleration | m, m/s, m/s$^2$ |
| $R_0$, $V_0$ | initial radius and initial expansion velocity | m, m/s |
| $p_R(t)$ | liquid pressure at the cavity wall | Pa |
| $\mathrm{Re} = \rho V_0R_0/\mu$, $\Lambda = p_\infty/(\rho V_0^2)$ | dimensionless parameters | 1 |
| $R = R_c/R_0$, $\tau = tV_0/R_0$ | dimensionless radius and time | 1 |

## Phase 2: Frames, Field Form and Boundary Conditions

- Spherical frame $(r,\theta,\phi)$ centred on the cavity centre, fixed; the liquid occupies $r > R_c(t)$. The basis is orthonormal and right-handed.
- Field form: $\bar{v} = v_r(r,t)\,\bar{e}_r$, $p = p(r,t)$.

![[attachments/FM-T4/ns10-setup.svg]]
*Setup of NS10 (drawn for the solution): cavity of radius $R_c(t)$ ($R_c(0) = R_0$, $\dot{R}_c(0) = V_0$) expanding in the ocean, radial velocity field $v_r(r,t)$, pressure $p_R(t)$ at the cavity wall and $p_\infty$ far away*

| Location | Condition | Origin |
| :--- | :--- | :--- |
| $r = R_c(t)$ | $v_r = \dot{R}_c$ | the liquid at the cavity wall moves with it |
| $r \to \infty$ | $v_r \to 0$, $p \to p_\infty$ | liquid at rest far away |
| $r = R_c(t)$ | $\bar{\bar{\tau}}\cdot\bar{n} = 0$, $\bar{n} = \bar{e}_r$ | cavity pressure neglected, no traction |
| $t = 0$ | $R_c = R_0$, $\dot{R}_c = V_0$ | statement |

## Phase 3: Step-by-Step Derivation

### 3.1 Velocity and irrotationality (item 1)

$$ \frac{1}{r^2}\frac{\partial(r^2v_r)}{\partial r} = 0 \;\Longrightarrow\; r^2v_r = A(t), \qquad v_r(R_c,t) = \dot{R}_c \;\Longrightarrow\; A(t) = R_c^2\dot{R}_c \tag{1} $$

$$ \boxed{\,v_r(r,t) = \frac{R_c^2\dot{R}_c}{r^2}\,} \tag{2} $$

The vorticity of $\bar{v} = v_r(r,t)\bar{e}_r$, from the curl in spherical coordinates, has the components $\omega_r = \dfrac{1}{r\sin\theta}\left[\dfrac{\partial(v_\phi\sin\theta)}{\partial\theta} - \dfrac{\partial v_\theta}{\partial\phi}\right] = 0$, $\omega_\theta = \dfrac{1}{r}\left[\dfrac{1}{\sin\theta}\dfrac{\partial v_r}{\partial\phi} - \dfrac{\partial(rv_\phi)}{\partial r}\right] = 0$ and $\omega_\phi = \dfrac{1}{r}\left[\dfrac{\partial(rv_\theta)}{\partial r} - \dfrac{\partial v_r}{\partial\theta}\right] = 0$, because $v_\theta = v_\phi = 0$ and $v_r$ does not depend on $\theta$ or $\phi$. Hence $\nabla\wedge\bar{v} = 0$: **the flow is irrotational**, and therefore $\nabla\wedge(\nabla\wedge\bar{v}) = 0$.

### 3.2 Pressure field (item 2)

The viscous force of the incompressible flow is $-\mu\nabla\wedge(\nabla\wedge\bar{v}) = 0$, so the $r$ component of (4.41) is the Euler equation:

$$ \rho\left(\frac{\partial v_r}{\partial t} + v_r\frac{\partial v_r}{\partial r}\right) = -\frac{\partial p}{\partial r} \tag{3} $$

With $\partial v_r/\partial t = (R_c^2\ddot{R}_c + 2R_c\dot{R}_c^2)/r^2$ (product rule on $R_c^2\dot{R}_c$) and $v_r\,\partial v_r/\partial r = -2R_c^4\dot{R}_c^2/r^5$:

$$ \frac{\partial p}{\partial r} = -\rho\left[\frac{R_c^2\ddot{R}_c + 2R_c\dot{R}_c^2}{r^2} - \frac{2R_c^4\dot{R}_c^2}{r^5}\right] \tag{4} $$

Integrating from $r$ to $\infty$ with $p(\infty) = p_\infty$ (the antiderivatives are $-1/r$ and $-1/(4r^4)$, and Barrow's rule gives $1/r$ and $1/(4r^4)$):

$$ \boxed{\,\frac{p(r,t) - p_\infty}{\rho} = \frac{R_c^2\ddot{R}_c + 2R_c\dot{R}_c^2}{r} - \frac{R_c^4\dot{R}_c^2}{2r^4}\,} \tag{5} $$

### 3.3 Equation at the cavity wall (item 3)

At $r = R_c(t)$, (5) gives $\dfrac{p_R - p_\infty}{\rho} = R_c\ddot{R}_c + 2\dot{R}_c^2 - \dfrac{\dot{R}_c^2}{2}$:

$$ \boxed{\,R_c\ddot{R}_c + \frac{3}{2}\dot{R}_c^2 = \frac{p_R(t) - p_\infty}{\rho}, \qquad R_c(0) = R_0,\ \ \dot{R}_c(0) = V_0\,} \tag{6} $$

### 3.4 Pressure at the wall: null stress (item 4)

The unit normal to the cavity wall, pointing into the liquid, is $\bar{n} = \bar{e}_r$. The stress vector is $\bar{\bar{\tau}}\cdot\bar{e}_r = (-p + \tau'_{rr})\bar{e}_r + \tau'_{r\theta}\bar{e}_\theta + \tau'_{r\phi}\bar{e}_\phi$. For this flow $\tau'_{r\theta} = \tau'_{r\phi} = 0$ and (Notes.pdf, stress components in spherical coordinates)

$$ \tau'_{rr} = 2\mu\frac{\partial v_r}{\partial r} = -\frac{4\mu R_c^2\dot{R}_c}{r^3}, \qquad \tau'_{rr}\Big|_{R_c} = -\frac{4\mu\dot{R}_c}{R_c} \tag{7} $$

The null-stress condition at $r = R_c$ gives $-p_R + \tau'_{rr}(R_c) = 0$:

$$ \boxed{\,p_R(t) = -\frac{4\mu\dot{R}_c}{R_c}\,} \tag{8} $$

### 3.5 Closed ODE and non-dimensionalization (item 5)

Substituting (8) in (6) with $\nu = \mu/\rho$:

$$ R_c\ddot{R}_c + \frac{3}{2}\dot{R}_c^2 + \frac{4\nu\dot{R}_c}{R_c} = -\frac{p_\infty}{\rho} \tag{9} $$

With $R_c = R_0R$ and $t = R_0\tau/V_0$: $\dot{R}_c = V_0\,R'$ and $\ddot{R}_c = (V_0^2/R_0)R''$ (chain rule, $d/dt = (V_0/R_0)\,d/d\tau$, with $R' = dR/d\tau$). Substituting and dividing by $V_0^2$:

$$ \boxed{\,R\,R'' + \frac{3}{2}R'^2 + \frac{4}{\mathrm{Re}}\frac{R'}{R} = -\Lambda, \qquad R(0) = 1,\ \ R'(0) = 1\,} \tag{10} $$

with $\mathrm{Re} = \rho V_0R_0/\mu$ (because $\nu/(V_0R_0) = 1/\mathrm{Re}$) and $\Lambda = p_\infty/(\rho V_0^2)$. The problem depends only on these two parameters.

### 3.6 Limit $\mathrm{Re} \to \infty$ (item 6)

The viscous term drops out: $R\,R'' + \tfrac{3}{2}R'^2 = -\Lambda$. With $z = \ln R$ and $F = (dR/d\tau)^2$, the chain rule gives $dF/d\tau = 2R'R''$ and $dz/d\tau = R'/R$, so

$$ \frac{dF}{dz} = \frac{dF/d\tau}{dz/d\tau} = 2R\,R'' \tag{11} $$

and the equation becomes $\tfrac{1}{2}\dfrac{dF}{dz} + \tfrac{3}{2}F = -\Lambda$, that is $\dfrac{dF}{dz} + 3F = -2\Lambda$ with $F(0) = R'(0)^2 = 1$ (at $\tau = 0$, $R = 1$ and $z = 0$). Multiplying by the integrating factor $e^{3z}$: $(F\,e^{3z})' = -2\Lambda e^{3z}$, so $F\,e^{3z} = -\tfrac{2\Lambda}{3}e^{3z} + C$ and $F(0) = 1$ gives $C = 1 + 2\Lambda/3$:

$$ F(z) = e^{-3z} + \frac{2\Lambda}{3}\left(e^{-3z} - 1\right) \tag{12} $$

With $e^{-3z} = R^{-3}$:

$$ \boxed{\,\frac{dR}{d\tau} = \left[R^{-3} + \frac{2\Lambda}{3}\left(R^{-3} - 1\right)\right]^{1/2}\,} \tag{13} $$

(positive root while the cavity expands).

### 3.7 Maximum radius and time to reach it (item 7)

The cavity stops growing when $dR/d\tau = 0$: $R_{\max}^{-3}(1 + 2\Lambda/3) = 2\Lambda/3$, that is

$$ \boxed{\,R_{\max} = \left(1 + \frac{3}{2\Lambda}\right)^{1/3}\,} \tag{14} $$

Separating variables in (13), $d\tau = dR/\sqrt{R^{-3} + \tfrac{2\Lambda}{3}(R^{-3} - 1)}$, and integrating from $R = 1$ at $\tau = 0$ to $R_{\max}$ at $\tau_{\max}$ (with the dummy variable $x$):

$$ \boxed{\,\tau_{\max}(\Lambda) = \int_1^{(1 + 3/(2\Lambda))^{1/3}}\frac{dx}{\sqrt{x^{-3} + \frac{2\Lambda}{3}\left(x^{-3} - 1\right)}}\,} \tag{15} $$

*Approximation for $\Lambda \ll 1$.* Then $R_{\max} \simeq (3/(2\Lambda))^{1/3} \gg 1$. Factor $x^{-3}$ out of the square root: the integrand is $x^{3/2}\big/\sqrt{(1 + 2\Lambda/3) - (2\Lambda/3)x^3}$ and, with $2\Lambda/3 \simeq R_{\max}^{-3}$ for small $\Lambda$,

$$ \tau_{\max} \simeq \int_1^{R_{\max}}\frac{x^{3/2}\,dx}{\sqrt{1 - (x/R_{\max})^3}} \simeq R_{\max}^{5/2}\int_0^1\frac{s^{3/2}\,ds}{\sqrt{1 - s^3}} \tag{16} $$

(with $x = R_{\max}s$, and the lower limit $s = 1/R_{\max} \to 0$). The substitution $u = s^3$ gives $s^{3/2}ds = \tfrac{1}{3}u^{-1/6}du$, so the integral is $\tfrac{1}{3}B(\tfrac{5}{6},\tfrac{1}{2}) = \dfrac{\sqrt{\pi}\,\Gamma(5/6)}{3\,\Gamma(4/3)} \simeq 0.747$:

$$ \boxed{\,\tau_{\max} \simeq 0.747\left(\frac{3}{2\Lambda}\right)^{5/6} = 0.747\left(\frac{3}{2}\right)^{5/6}\Lambda^{-5/6}\,} \qquad (\Lambda \ll 1) \tag{17} $$

> [!warning] Discrepancy with the official solution
> The handwritten solution approximates the integrand by $x^{3/2}$ over the whole range and obtains $\tau_{\max} \simeq \tfrac{2}{5}(3/2)^{5/6}\Lambda^{-5/6}$, which neglects the factor $(1 - x^3/R_{\max}^3)^{-1/2}$ of (16). Integrating (15) numerically gives $\tau_{\max} = 48.3,\ 330.8,\ 2255.4$ for $\Lambda = 10^{-2},\ 10^{-3},\ 10^{-4}$, while (17) gives $48.6,\ 331.1,\ 2255.8$ and the sheet's expression $26.0,\ 177.3,\ 1208.2$. The scaling $\Lambda^{-5/6}$ is the same; the computed coefficient $0.747$ is kept.

### 3.8 Limit $\mathrm{Re} \to 0$ (item 8)

For $\mathrm{Re} \to 0$ the viscous term dominates the inertial terms and (10) reduces to the first-order ODE

$$ \frac{4}{\mathrm{Re}}\frac{R'}{R} \simeq -\Lambda \;\Longrightarrow\; \frac{dR}{d\tau} = -\frac{\Lambda\,\mathrm{Re}}{4}\,R \tag{18} $$

whose solution with $R(0) = 1$ is

$$ R(\tau) \simeq \exp\left(-\frac{\Lambda\,\mathrm{Re}}{4}\,\tau\right) \tag{19} $$

It is not possible to satisfy both initial conditions: a first-order ODE admits only one, and (19) has $R'(0) = -\Lambda\mathrm{Re}/4 \neq 1$. The approximation is valid only after an initial transient, of duration of the order of $\mathrm{Re}$ in $\tau$, during which the inertial terms $R\,R'' + \tfrac{3}{2}R'^2$ cannot be neglected and the initial velocity is dissipated by viscosity. In this limit the ambient pressure $p_\infty$ crushes the cavity, which then collapses exponentially instead of expanding.

## Phase 4: Interpretation, Limits and Dimensional Check

- **Physical meaning.** (6) is the Rayleigh equation for the cavity with the viscous correction (8): the cavity decelerates because of the ambient pressure $p_\infty$ (term $\Lambda$) and the viscous normal stress (term $4/(\mathrm{Re}\,R)$). For $\mathrm{Re} \to \infty$ the cavity stops at $R_{\max}$ and then collapses; for $\mathrm{Re} \to 0$ viscosity dominates.
- **Limits.** For $\Lambda \to 0$ the right-hand side of (13) is $R^{-3/2}$ with no stopping point: the cavity expands for ever in the inviscid, pressureless case. For $\Lambda \to \infty$, $R_{\max} \to 1$: the cavity cannot expand.
- **Dimensional check.** $R_c\ddot{R}_c$ and $\dot{R}_c^2$ have units $\mathrm{m^2/s^2}$, as does $p_\infty/\rho$ (Pa/(kg/m$^3$)). $4\nu\dot{R}_c/R_c$ has units $(\mathrm{m^2/s})(\mathrm{m/s})/\mathrm{m} = \mathrm{m^2/s^2}$. $\mathrm{Re}$ and $\Lambda$ are dimensionless. $p_R = -4\mu\dot{R}_c/R_c$ has units Pa.
- **Consistency.** At $R = 1$ the bracket of (13) equals $1$ for every $\Lambda$, so $R'(0) = 1$: the solution keeps the initial velocity $V_0$.
