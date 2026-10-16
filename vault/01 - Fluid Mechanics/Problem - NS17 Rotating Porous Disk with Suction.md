---
materia: Fluid Mechanics
tema: "Topic 4: The Navier-Stokes Equations"
tags:
  - problema-examen
  - navier-stokes
  - disco-rotatorio
  - solucion-de-semejanza
  - succion
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-04-navier-stokes/problemas/NS17.pdf"
id: "ns17"
pill: "NS17: Rotating disk"
tags_html:
  - "Similarity solution"
  - "Rotating disk with suction"
  - "Boundary conditions"
  - "Pressure distribution"
---

# Problem NS17: Rotating Porous Disk with Suction

> Official UC3M Navier-Stokes problem collection (Introduction to Fluid Mechanics). Part of [[Topic 4 - The Navier-Stokes Equations]]. Related: [[Concept - Navier-Poisson Constitutive Equation|Navier-Poisson law]], [[Concept - Fourier's Law and Heat Conduction|Fourier's law]], [[Formula Sheet - Topic 3 Conservation Laws|Topic 3 formula sheet]].
> Method: the statement is transcribed word for word; the solution follows the four phases (setup, frames and field form, step-by-step derivation, interpretation), with continuity and each component of the Navier-Stokes equations simplified term by term and every integration constant fixed with its boundary condition.

## Statement

We will consider an infinitely large porous disk rotating with angular velocity $\Omega$ that sucks the fluid with a known velocity $v_z = -2(\nu\Omega)^{1/2}\lambda_1$. The velocity induced in the fluid of density $\rho$ and kinematic viscosity $\nu = \mu/\rho$ is three-dimensional, with components $(v_r, v_\theta, v_z)$ in the cylindrical coordinates system shown in the sketch.

We want to show that the solution of the problem has the form $v_z = -2(\nu\Omega)^{1/2}f(\eta)$, $v_\theta = r\Omega g(\eta)$, where $\eta = (\Omega/\nu)^{1/2}z$ is a similarity variable and $f(\eta)$ and $g(\eta)$ are two functions that must be obtained in the course of the solution, such that the solution far from the disk, as $\eta \to \infty$, is given by $v_r \to 0$, $v_\theta \to 0$.

Taking into account the azimuthal symmetry of the problem,

1. Use the continuity equation to obtain the radial component $v_r$ in terms of the function $f(\eta)$.

2. Use the azimuthal momentum equation to find the ordinary differential equation to be satisfied by the function $g(\eta)$.

3. Use the physical boundary conditions for $\bar{v}$ to find the boundary conditions that $f(\eta)$ and $g(\eta)$ must satisfy.

4. Use the vertical momentum equation to obtain the pressure distribution in terms of an integration function $C(r)$ that will appear in the course of the integration.

5. Use the radial momentum equation to determine $C(r)$ and the ordinary differential equation to be satisfied by $f(\eta)$, with its corresponding boundary conditions. Use the variable separation method to show that $C(r) = A$, where $A$ is a constant. Obtain $A$ in terms of the pressure far from the plate $p_\infty$ and the pressure distribution $p(\eta)$.

The sheet is headed "ESCUELA POLITECNICA SUPERIOR, INTRODUCTION TO FLUID MECHANICS, 14-11-2016, PROBLEM 2 (10 POINTS), Time: 60 minutes".

![[attachments/FM-T4/ns17-statement.png]]
*Statement figure (crop of NS17.pdf, p. 1): porous disk rotating with angular velocity $\Omega$, side view (axes $z$, $r$) and top view (polar angle $\theta$)*

Source: NS17.pdf (page 1 of 2: statement; page 2: handwritten solution). Notes.pdf, Chapter 4: continuity Eq. 4.40 and momentum Eq. 4.41 in cylindrical coordinates.

## Phase 1: Hypotheses, Data and Unknowns

- Steady, axisymmetric ($\partial/\partial\theta = 0$, $\partial/\partial t = 0$) flow of an incompressible liquid with constant $\rho$ and $\nu$ above an infinitely large rotating porous disk, without mass forces. Equations (4.40) and (4.41) in cylindrical coordinates.
- The disk (plane $z = 0$, the liquid occupies $z > 0$) rotates with the angular velocity $\Omega$ and sucks the liquid with the known axial velocity $v_z(0) = -2(\nu\Omega)^{1/2}\lambda_1$, with $\lambda_1$ a given constant.
- Self-similar ansatz of the statement: $v_z = -2(\nu\Omega)^{1/2}f(\eta)$, $v_\theta = r\Omega\,g(\eta)$, with $\eta = (\Omega/\nu)^{1/2}z$; $v_r$ is to be obtained.
- Far from the disk ($\eta \to \infty$): $v_r \to 0$, $v_\theta \to 0$ and the pressure tends to $p_\infty$.
- Data: $[\rho,\ \nu,\ \Omega,\ \lambda_1,\ p_\infty]$. Unknowns: $v_r$, the ODEs for $f$ and $g$ with their boundary conditions, $p(r,z)$ and the constant $A$.
- Derivatives used: $d\eta/dz = (\Omega/\nu)^{1/2}$, so that $\partial/\partial z = (\Omega/\nu)^{1/2}\,d/d\eta$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $\Omega$ | angular velocity of the disk | rad/s |
| $\nu = \mu/\rho$ | kinematic viscosity | m$^2$/s |
| $\eta = (\Omega/\nu)^{1/2}z$ | similarity variable | 1 |
| $f(\eta)$, $g(\eta)$ | dimensionless axial and azimuthal functions | 1 |
| $\lambda_1$ | dimensionless suction parameter | 1 |
| $p_\infty$ | pressure far from the disk | Pa |

## Phase 2: Frames, Field Form and Boundary Conditions

- Cylindrical frame $(r,\theta,z)$ with $z$ along the axis of rotation, normal to the disk and pointing into the liquid; the basis $\{\bar{e}_r,\bar{e}_\theta,\bar{e}_z\}$ is orthonormal and right-handed (see the sketch of the statement).
- Field form: $v_r = v_r(r,z)$, $v_\theta = r\Omega\,g(\eta)$, $v_z = -2(\nu\Omega)^{1/2}f(\eta)$, $p = p(r,z)$.

| Location | Condition | Origin |
| :--- | :--- | :--- |
| $z = 0$ | $v_r = 0$, $v_\theta = r\Omega$ | no-slip on the rotating disk |
| $z = 0$ | $v_z = -2(\nu\Omega)^{1/2}\lambda_1$ | known suction velocity |
| $z \to \infty$ | $v_r \to 0$, $v_\theta \to 0$ | liquid at rest far from the disk |
| $z \to \infty$ | $p \to p_\infty$ | pressure far from the disk |

## Phase 3: Step-by-Step Derivation

### 3.1 Radial velocity from continuity (item 1)

$$ \frac{1}{r}\frac{\partial(rv_r)}{\partial r} + \underbrace{\cancel{\frac{1}{r}\frac{\partial v_\theta}{\partial\theta}}}_{\partial_\theta = 0} + \frac{\partial v_z}{\partial z} = 0 \tag{1} $$

The axial derivative is, by the chain rule, $\dfrac{\partial v_z}{\partial z} = \dfrac{dv_z}{d\eta}\dfrac{d\eta}{dz} = -2(\nu\Omega)^{1/2}f'\,\left(\frac{\Omega}{\nu}\right)^{1/2} = -2\Omega f'(\eta)$. Hence $\dfrac{1}{r}\dfrac{\partial(rv_r)}{\partial r} = 2\Omega f'$. Multiplying by $r$ and integrating in $r$ at fixed $z$ (so $f'$ is constant): $r\,v_r = \Omega f'\,r^2 + F(z)$; the radial velocity must be finite on the axis $r = 0$, which requires $F(z) = 0$:

$$ \boxed{\,v_r = r\,\Omega\,f'(\eta)\,} \tag{2} $$

### 3.2 Azimuthal momentum (item 2)

The $\theta$ component of (4.41), steady, with $\partial/\partial\theta = 0$ and no mass force:

$$ \rho\left(v_r\frac{\partial v_\theta}{\partial r} + \frac{v_rv_\theta}{r} + v_z\frac{\partial v_\theta}{\partial z}\right) = \mu\left[\frac{\partial}{\partial r}\left(\frac{1}{r}\frac{\partial(rv_\theta)}{\partial r}\right) + \frac{\partial^2v_\theta}{\partial z^2}\right] \tag{3} $$

Each term for $v_\theta = r\Omega g$, $v_r = r\Omega f'$, $v_z = -2(\nu\Omega)^{1/2}f$ (the $\eta$ derivatives bring $(\Omega/\nu)^{1/2}$):

- $v_r\,\partial v_\theta/\partial r = (r\Omega f')(\Omega g) = r\Omega^2f'g$ and $v_rv_\theta/r = (r\Omega f')(\Omega g) = r\Omega^2f'g$;
- $v_z\,\partial v_\theta/\partial z = -2(\nu\Omega)^{1/2}f\cdot r\Omega g'\,(\Omega/\nu)^{1/2} = -2r\Omega^2fg'$;
- the first viscous term is zero: $r^{-1}\partial(rv_\theta)/\partial r = r^{-1}\partial(r^2\Omega g)/\partial r = 2\Omega g$ does not depend on $r$;
- $\partial^2v_\theta/\partial z^2 = r\Omega g''\,\Omega/\nu$.

Substituting and using $\mu/\nu = \rho$:

$$ \rho\,r\Omega^2\left(2f'g - 2fg'\right) = \rho\,r\Omega^2g'' \;\Longrightarrow\; \boxed{\,g'' + 2\left(f\,g' - f'g\right) = 0\,} \tag{4} $$

### 3.3 Boundary conditions (item 3)

At the disk, $z = 0$ ($\eta = 0$): $v_r = r\Omega f'(0) = 0$ gives $f'(0) = 0$; $v_\theta = r\Omega g(0) = r\Omega$ gives $g(0) = 1$; $v_z = -2(\nu\Omega)^{1/2}f(0) = -2(\nu\Omega)^{1/2}\lambda_1$ gives $f(0) = \lambda_1$. Far from the disk ($\eta \to \infty$): $v_r \to 0$ gives $f'(\infty) = 0$ and $v_\theta \to 0$ gives $g(\infty) = 0$:

$$ \boxed{\,f(0) = \lambda_1,\quad f'(0) = 0,\quad f'(\infty) = 0,\qquad g(0) = 1,\quad g(\infty) = 0\,} \tag{5} $$

### 3.4 Vertical momentum and the pressure (item 4)

The $z$ component of (4.41): $v_r\,\partial v_z/\partial r = 0$ because $v_z$ depends only on $z$, and the viscous term is $\mu\,\partial^2v_z/\partial z^2$ (the radial part $r^{-1}\partial(r\partial v_z/\partial r)/\partial r$ vanishes):

$$ \rho\,v_z\frac{\partial v_z}{\partial z} = -\frac{\partial p}{\partial z} + \mu\frac{\partial^2v_z}{\partial z^2} \;\Longrightarrow\; \frac{\partial}{\partial z}\left[p + \frac{\rho v_z^2}{2} - \mu\frac{\partial v_z}{\partial z}\right] = 0 \tag{6} $$

Integrating in $z$ at fixed $r$, the bracket is a function $C(r)$:

$$ p + \frac{\rho v_z^2}{2} - \mu\frac{\partial v_z}{\partial z} = C(r) \tag{7} $$

With $\rho v_z^2/2 = 2\rho\nu\Omega f^2 = 2\mu\Omega f^2$ and $-\mu\,\partial v_z/\partial z = 2\mu\Omega f'$:

$$ \boxed{\,p(r,\eta) = C(r) - 2\mu\Omega\left[f^2(\eta) + f'(\eta)\right]\,} \tag{8} $$

### 3.5 Radial momentum, the ODE for $f$ and the constant $A$ (item 5)

The $r$ component of (4.41) with the viscous terms $\mu\left[\partial\left(r^{-1}\partial(rv_r)/\partial r\right)/\partial r + \partial^2v_r/\partial z^2\right]$:

$$ \rho\left(v_r\frac{\partial v_r}{\partial r} - \frac{v_\theta^2}{r} + v_z\frac{\partial v_r}{\partial z}\right) = -\frac{\partial p}{\partial r} + \mu\left[\frac{\partial}{\partial r}\left(\frac{1}{r}\frac{\partial(rv_r)}{\partial r}\right) + \frac{\partial^2v_r}{\partial z^2}\right] \tag{9} $$

Each term: $v_r\,\partial v_r/\partial r = (r\Omega f')(\Omega f') = r\Omega^2f'^2$; $v_\theta^2/r = r\Omega^2g^2$; $v_z\,\partial v_r/\partial z = -2(\nu\Omega)^{1/2}f\cdot r\Omega f''(\Omega/\nu)^{1/2} = -2r\Omega^2ff''$; the first viscous term is zero because $r^{-1}\partial(r^2\Omega f')/\partial r = 2\Omega f'$ does not depend on $r$; $\partial^2v_r/\partial z^2 = r\Omega f'''\,\Omega/\nu$. From (8), $\partial p/\partial r = C'(r)$, since the $\eta$ term does not depend on $r$. Substituting and using $\mu/\nu = \rho$:

$$ \rho\,r\Omega^2\left(f'^2 - g^2 - 2ff''\right) = -C'(r) + \rho\,r\Omega^2f''' \;\Longrightarrow\; -f''' + f'^2 - g^2 - 2ff'' = -\frac{C'(r)}{\rho\,r\Omega^2} \tag{10} $$

The left side depends only on $\eta$ and the right side only on $r$: both equal a constant, $-\lambda$. As $\eta \to \infty$, $f'\to 0$ (and so $f'' \to 0$, $f''' \to 0$) and $g \to 0$: the left side tends to $0$, so $\lambda = 0$. Therefore $C'(r) = 0$, that is

$$ \boxed{\,C(r) = A\ (\text{a constant}), \qquad f''' + 2ff'' - f'^2 + g^2 = 0\,} \tag{11} $$

with the boundary conditions (5) for $f$ ($f(0) = \lambda_1$, $f'(0) = f'(\infty) = 0$); the system (4)-(11) for $f$ and $g$, with the five conditions (5), is a nonlinear boundary-value problem.

The constant $A$ follows from (8) as $\eta \to \infty$ ($p \to p_\infty$, $f' \to 0$, $f \to f(\infty)$):

$$ p_\infty = A - 2\mu\Omega f(\infty)^2 \;\Longrightarrow\; \boxed{\,A = p_\infty + 2\mu\Omega\,f(\infty)^2\,} \tag{12} $$

and the pressure distribution is

$$ \boxed{\,p(\eta) = p_\infty - 2\mu\Omega\left[f^2(\eta) - f^2(\infty) + f'(\eta)\right]\,} \tag{13} $$

## Phase 4: Interpretation, Limits and Dimensional Check

- **Physical meaning.** The disk drags the liquid into rotation and the centrifugal force throws it outwards (the term $-g^2$ of (11)); continuity then draws liquid towards the disk (the term $-2f'$ of the radial velocity and the axial velocity $v_z \propto -f$). With suction the axial flow is imposed at the disk ($f(0) = \lambda_1$). The velocity profile has the same form at every radius because $v_r$ and $v_\theta$ scale with $r$: that is the self-similarity.
- **Limits.** For $\lambda_1 = 0$ (impermeable disk) the equations (4) and (11) with the conditions (5) are those of the rotating disk of the classical similarity solution; for $\Omega \to 0$ the whole flow vanishes. The pressure (13) is independent of $r$: the pressure of the problem varies only across the layer.
- **Dimensional check.** $\eta = (\Omega/\nu)^{1/2}z$ is dimensionless ($\sqrt{\mathrm{s^{-1}}\,\mathrm{s/m^2}}\,\mathrm{m} = 1$). $(\nu\Omega)^{1/2}$ has units $\mathrm{m/s}$, so $v_z$ is a velocity; $r\Omega$ is a velocity. $\mu\Omega$ has units $\mathrm{Pa\,s\cdot s^{-1}} = \mathrm{Pa}$, so (8) and (13) are pressures.
- **Consistency of (11).** Differentiating (8) with respect to $r$ at fixed $\eta$ shows that $\partial p/\partial r = C'(r)$ and (11) makes the radial momentum balance independent of $r$, as the similarity ansatz requires.
