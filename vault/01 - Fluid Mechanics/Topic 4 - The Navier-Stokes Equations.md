---
materia: Fluid Mechanics
tema: "Topic 4: The Navier-Stokes Equations"
fuentes:
  - "Notes.pdf (Sánchez & Rodríguez-Rodríguez, UC3M), Chapter 4, pp. 37-50 (PDF pages 46-59)"
tags:
  - moc-topic
  - fluid-mechanics
  - navier-stokes
  - second-year
dificultad: high
---

# Topic 4: The Navier-Stokes Equations

> **Central idea.** The integral laws of Chapter 3 give the overall balances of a finite fluid volume. To compute local fields (velocity, density, pressure, temperature at every point) the same laws are rewritten with the Gauss formula as partial differential equations, which are then closed with the equations of state and the Navier-Poisson and Fourier constitutive laws, and integrated with initial and boundary conditions.

---

## 1. From the Integral to the Differential Form

### Why the integral form is not enough

The conservation equations of mass, momentum and energy in integral form, (3.10), (3.35) and (3.46) of Chapter 3, are applied to a conveniently chosen control volume. That approach needs simplifying assumptions (for example, a uniform velocity at the open boundaries) and the neglect of terms expected to be small, so it gives the overall properties of a fluid system. It is not suitable to compute **local** properties of the flow, such as the distributions of velocity $\vec{v}(\vec{x},t)$, density $\rho(\vec{x},t)$ and pressure $p(\vec{x},t)$.

### The laws for a material fluid volume

For that purpose the conservation laws are written for a fluid volume $V_f(t)$ with boundary $\Sigma_f(t)$ and outward normal $\vec{n}$ (Notes.pdf, Eqs. 4.1-4.3).

Mass:

$$ \frac{d}{dt}\int_{V_f(t)} \rho \, dV = 0 \tag{4.1} $$

Linear momentum (pressure force, viscous force and mass force):

$$ \frac{d}{dt}\int_{V_f(t)} \rho \vec{v} \, dV = -\int_{\Sigma_f(t)} p \vec{n} \, d\sigma + \int_{\Sigma_f(t)} \bar{\bar{\tau}}' \cdot \vec{n} \, d\sigma + \int_{V_f(t)} \rho \vec{f}_m \, dV \tag{4.2} $$

Total energy (work of pressure, viscous and mass forces, plus heat conduction, radiation and chemical reaction):

$$ \frac{d}{dt}\int_{V_f(t)} \rho\left(e + \frac{\lvert\vec{v}\rvert^2}{2}\right) dV = -\int_{\Sigma_f(t)} p \vec{v}\cdot\vec{n} \, d\sigma + \int_{\Sigma_f(t)} \vec{v}\cdot\bar{\bar{\tau}}'\cdot\vec{n} \, d\sigma + \int_{V_f(t)} \rho \vec{f}_m\cdot\vec{v} \, dV - \int_{\Sigma_f(t)} \vec{q}\cdot\vec{n} \, d\sigma + \int_{V_f(t)} (Q_c + Q_r) \, dV \tag{4.3} $$

where $e$ is the internal energy per unit mass, $\bar{\bar{\tau}}'$ the viscous stress tensor, $\vec{f}_m$ the mass force per unit mass, $\vec{q}$ the heat flux vector, and $Q_c$, $Q_r$ the heat released per unit volume and time by chemical reaction and by radiation.

### The method used in the whole chapter

Every equation below is obtained with the same two steps:

1. The **Gauss formula** (Notes.pdf, Eq. 2.9), $\int_{\Sigma_f}\vec{A}\cdot\vec{n}\,d\sigma = \int_{V_f}\nabla\cdot\vec{A}\,dV$ (and its tensor version for $\int \bar{\bar{A}}\cdot\vec{n}\,d\sigma$), turns every surface integral into a volume integral over the same $V_f(t)$. The time derivative of the volume integral is expanded with the Reynolds transport theorem of Chapter 3.
2. Because the volume $V_f$ is **arbitrary**, an equation of the form $\int_{V_f} (\ldots) \, dV = 0$ can hold for every choice of $V_f$ if and only if the integrand $(\ldots)$ is zero at each point. This gives a local rate balance.

---

## 2. The Continuity Equation

With the Gauss formula, the Reynolds transport theorem turns (4.1) into

$$ \int_{V_f}\left[\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\vec{v})\right] dV = 0 \tag{4.4} $$

Since $V_f$ is arbitrary, the bracket vanishes at each point of space (Notes.pdf, Eq. 4.5):

$$ \frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\vec{v}) = 0 \tag{4.5} $$

This is the **continuity (mass conservation) equation**: the local rate of density variation plus the rate of mass loss by convective outflow is zero.

An equivalent form follows by expanding the divergence with the product rule, $\nabla\cdot(\rho\vec{v}) = \vec{v}\cdot\nabla\rho + \rho\nabla\cdot\vec{v}$, and recognising the material derivative $D\rho/Dt = \partial\rho/\partial t + \vec{v}\cdot\nabla\rho$:

$$ \frac{1}{\rho}\frac{D\rho}{Dt} = -\nabla\cdot\vec{v} \tag{4.6} $$

The density of a fluid particle changes only because its volume changes (rate of volume variation $\nabla\cdot\vec{v}$).

Special cases:

- **Incompressible fluid** (constant density): $D\rho/Dt = 0$ in (4.6), hence

$$ \nabla\cdot\vec{v} = 0 \tag{4.7} $$

- **Steady gas flow**: $\partial\rho/\partial t = 0$ in (4.5), hence

$$ \nabla\cdot(\rho\vec{v}) = 0 \tag{4.8} $$

that is, the convective rate of mass loss per unit volume is zero.

---

## 3. The Momentum Equation

### 3.1 Derivation

The same procedure (Gauss formula for the three surface integrals, then the arbitrary-volume argument) applied to (4.2) gives (Notes.pdf, Eq. 4.9)

$$ \frac{\partial}{\partial t}(\rho\vec{v}) + \nabla\cdot(\rho\vec{v}\vec{v}) = -\nabla p + \nabla\cdot\bar{\bar{\tau}}' + \rho\vec{f}_m \tag{4.9} $$

To reach the more useful form, expand the left-hand side with the product rule:

$$ \frac{\partial(\rho\vec{v})}{\partial t} + \nabla\cdot(\rho\vec{v}\vec{v}) = \rho\frac{\partial\vec{v}}{\partial t} + \vec{v}\frac{\partial\rho}{\partial t} + \vec{v}\,\nabla\cdot(\rho\vec{v}) + \rho\,\vec{v}\cdot\nabla\vec{v} = \rho\left(\frac{\partial\vec{v}}{\partial t} + \vec{v}\cdot\nabla\vec{v}\right) + \vec{v}\left[\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\vec{v})\right] $$

The last bracket is zero by continuity (4.5). Using the identity (Notes.pdf, Eq. 2.26) $\vec{v}\cdot\nabla\vec{v} = \nabla(\lvert\vec{v}\rvert^2/2) - \vec{v}\wedge(\nabla\wedge\vec{v})$ one obtains (Notes.pdf, Eq. 4.10)

$$ \rho\frac{D\vec{v}}{Dt} = \rho\left[\frac{\partial\vec{v}}{\partial t} + \nabla\left(\frac{\lvert\vec{v}\rvert^2}{2}\right) - \vec{v}\wedge(\nabla\wedge\vec{v})\right] = -\nabla p + \nabla\cdot\bar{\bar{\tau}}' + \rho\vec{f}_m \tag{4.10} $$

This is simply **Newton's second law per unit volume of fluid**: mass per unit volume times acceleration equals pressure force, viscous force and mass force per unit volume (result anticipated in Notes.pdf, Eq. 3.25).

### 3.2 Incompressible fluid with constant viscosity

For an incompressible fluid with constant viscosity the viscous force per unit volume is $\nabla\cdot\bar{\bar{\tau}}' = -\mu\nabla\wedge(\nabla\wedge\vec{v})$. Therefore (4.10) reduces to (Notes.pdf, Eq. 4.11)

$$ \frac{D\vec{v}}{Dt} = -\nabla\left(\frac{p}{\rho}\right) - \nu\nabla\wedge(\nabla\wedge\vec{v}) + \vec{f}_m \tag{4.11} $$

where $\nu = \mu/\rho$ is the kinematic viscosity. The viscous force can alternatively be written as $-\mu\nabla\wedge(\nabla\wedge\vec{v}) = \mu\nabla^2\vec{v}$, so that (Notes.pdf, Eq. 4.12)

$$ \frac{D\vec{v}}{Dt} = -\nabla\left(\frac{p}{\rho}\right) + \nu\nabla^2\vec{v} + \vec{f}_m \tag{4.12} $$

> [!note] Cartesian versus curvilinear coordinates
> In Cartesian coordinates each component of the vector $\nabla^2\vec{v}$ is simply the Laplacian of the corresponding velocity component. In cylindrical and spherical coordinates additional terms appear, which complicates the computation (see Section 8).

Equations (4.7) and (4.11) are enough to determine the velocity and pressure fields of an incompressible flow with constant viscosity. For such flows, which include those of water, these two equations are therefore **decoupled from the energy equation**, which can be used a posteriori to determine the temperature field.

### 3.3 Conservative mass force and reduced pressure

When the mass force is conservative, $\vec{f}_m = -\nabla U$, equation (4.11) can be written as (Notes.pdf, Eq. 4.13)

$$ \frac{D\vec{v}}{Dt} = -\nabla\left(\frac{p + \rho U}{\rho}\right) - \nu\nabla\wedge(\nabla\wedge\vec{v}) \tag{4.13} $$

For the motion of perfect liquids this suggests the **reduced pressure** $P = p + \rho U$ (for example, $P = p + \rho g z$ when $\vec{f}_m = \vec{g}$ points along $-\vec{e}_z$). Using it can simplify the description significantly. When the pressure does not enter the boundary conditions, the solution described with $P$ becomes entirely independent of the mass forces.

### 3.4 Bernoulli's theorem

For a steady incompressible flow with a conservative mass force in which the effect of viscosity is negligible, (4.13) with $\nu = 0$ together with the steady form of (2.26),

$$ \frac{D\vec{v}}{Dt} = \nabla\left(\frac{\lvert\vec{v}\rvert^2}{2}\right) - \vec{v}\wedge(\nabla\wedge\vec{v}) \tag{4.15} $$

gives (Notes.pdf, Eq. 4.14)

$$ \nabla\left(\frac{p}{\rho} + U + \frac{\lvert\vec{v}\rvert^2}{2}\right) - \vec{v}\wedge(\nabla\wedge\vec{v}) = 0 \tag{4.14} $$

This vector equation can be projected along streamlines by multiplying, at each point, by the unit vector $\vec{v}/\lvert\vec{v}\rvert$. The last term is identically zero because $\vec{v}\wedge(\nabla\wedge\vec{v})$ is perpendicular to $\vec{v}$. The projection reduces to

$$ \frac{\partial}{\partial l}\left(\frac{p}{\rho} + U + \frac{\lvert\vec{v}\rvert^2}{2}\right) = 0 \tag{4.16} $$

where $\partial/\partial l = \lvert\vec{v}\rvert^{-1}(\vec{v}\cdot\nabla)$ is the derivative along a streamline. Hence, for frictionless steady flow of an incompressible fluid, the quantity

$$ p + \rho U + \frac{\rho\lvert\vec{v}\rvert^2}{2} = C_l \tag{4.17} $$

remains constant along any given streamline, with a value $C_l$ that is in general different for different streamlines. Equation (4.17) is **Bernoulli's theorem**: it relates the variations of kinetic energy, potential energy and pressure along streamlines. If the flow is also irrotational, $C_l$ is the same for all streamlines, because (4.14) then reduces to $\nabla(p/\rho + U + \lvert\vec{v}\rvert^2/2) = 0$.

---

## 4. The Energy Equation

### 4.1 Total energy

The transformation used for (4.5) and (4.10) gives from (4.3)

$$ \frac{\partial}{\partial t}\left[\rho\left(e + \frac{\lvert\vec{v}\rvert^2}{2}\right)\right] + \nabla\cdot\left[\rho\left(e + \frac{\lvert\vec{v}\rvert^2}{2}\right)\vec{v}\right] = -\nabla\cdot(p\vec{v}) + \nabla\cdot(\vec{v}\cdot\bar{\bar{\tau}}') + \rho\vec{f}_m\cdot\vec{v} - \nabla\cdot\vec{q} + Q_c + Q_r \tag{4.18} $$

Using continuity (4.5), exactly as for the momentum equation, the left-hand side collapses to a material derivative (Notes.pdf, Eq. 4.19):

$$ \rho\frac{D}{Dt}\left(e + \frac{\lvert\vec{v}\rvert^2}{2}\right) = -\nabla\cdot(p\vec{v}) + \nabla\cdot(\vec{v}\cdot\bar{\bar{\tau}}') + \rho\vec{f}_m\cdot\vec{v} - \nabla\cdot\vec{q} + Q_c + Q_r \tag{4.19} $$

If the mass force derives from a steady potential, $\vec{f}_m = -\nabla U$ with $\partial U/\partial t = 0$, then $\rho\vec{f}_m\cdot\vec{v} = -\rho\,DU/Dt$ and the equation admits the alternative writing

$$ \rho\frac{D}{Dt}\left(e + \frac{\lvert\vec{v}\rvert^2}{2} + U\right) = -\nabla\cdot(p\vec{v}) + \nabla\cdot(\vec{v}\cdot\bar{\bar{\tau}}') - \nabla\cdot\vec{q} + Q_c + Q_r \tag{4.20} $$

### 4.2 Mechanical energy and internal energy

A separate equation for the mechanical (kinetic) energy $\lvert\vec{v}\rvert^2/2$ follows by multiplying (4.10) by $\vec{v}$. Since $\vec{v}\cdot[\vec{v}\wedge(\nabla\wedge\vec{v})] = 0$, the product gives the scalar equation (Notes.pdf, Eq. 4.21)

$$ \rho\frac{D}{Dt}\left(\frac{\lvert\vec{v}\rvert^2}{2}\right) = -\vec{v}\cdot\nabla p + \vec{v}\cdot(\nabla\cdot\bar{\bar{\tau}}') + \rho\vec{v}\cdot\vec{f}_m \tag{4.21} $$

a purely mechanical energy law: the rate of variation of the kinetic energy following the fluid particle equals the work rate of the mass force, $\rho\vec{v}\cdot\vec{f}_m$, plus the work rate of the surface forces associated with the translational motion of the particle, $-\vec{v}\cdot\nabla p + \vec{v}\cdot(\nabla\cdot\bar{\bar{\tau}}')$.

Subtract (4.21) from (4.19). Two identities are needed: $\nabla\cdot(p\vec{v}) = \vec{v}\cdot\nabla p + p\nabla\cdot\vec{v}$ and $\nabla\cdot(\vec{v}\cdot\bar{\bar{\tau}}') = \vec{v}\cdot(\nabla\cdot\bar{\bar{\tau}}') + \bar{\bar{\tau}}':\nabla\vec{v}$. The terms with $\vec{v}\cdot\nabla p$, $\vec{v}\cdot(\nabla\cdot\bar{\bar{\tau}}')$ and $\rho\vec{f}_m\cdot\vec{v}$ cancel, leaving the **internal energy equation** (Notes.pdf, Eq. 4.22)

$$ \rho\frac{De}{Dt} = -p\nabla\cdot\vec{v} + \bar{\bar{\tau}}':\nabla\vec{v} - \nabla\cdot\vec{q} + Q_c + Q_r \tag{4.22} $$

The internal energy of a fluid particle varies because of heat addition and because of the deformation work of the surface forces:

- $-p\nabla\cdot\vec{v}$ is the **compression work**. It is a reversible contribution: when the volume of the fluid is reduced ($\nabla\cdot\vec{v} < 0$) the compression work increases the internal energy, and the internal energy decreases for positive expansion rates $\nabla\cdot\vec{v} > 0$.
- $\phi_v = \bar{\bar{\tau}}':\nabla\vec{v}$ is the deformation work due to viscous forces. It is non-negative, $\phi_v \geq 0$, and is the rate of **mechanical energy dissipation** per unit volume and unit time. It is irreversible.

Both $-p\nabla\cdot\vec{v}$ and $\bar{\bar{\tau}}':\nabla\vec{v}$ are independent of the orientation, position and motion of the reference frame.

> [!note] Why the viscous dissipation is never negative
> With the Navier-Poisson law, using the definition of the contraction of two tensors, $\bar{\bar{A}}:\bar{\bar{B}} = \sum_i\sum_j A_{ij}B_{ij}$, one finds $\phi_v = 2\mu\bar{\bar{T}}_d:\bar{\bar{T}}_d + (\mu_B - \tfrac{2}{3}\mu)(\nabla\cdot\vec{v})^2$. In terms of the components $\gamma_{ij}$ of the rate-of-strain tensor this is
>
> $$ \phi_v = \frac{2\mu}{3}\left[(\gamma_{11}-\gamma_{22})^2 + (\gamma_{11}-\gamma_{33})^2 + (\gamma_{22}-\gamma_{33})^2 + 6(\gamma_{12}^2 + \gamma_{13}^2 + \gamma_{23}^2)\right] + \mu_B(\nabla\cdot\vec{v})^2 $$
>
> which is a sum of squares with non-negative coefficients, so $\phi_v \geq 0$ provided $\mu > 0$ and $\mu_B > 0$ (Notes.pdf, footnote 2, p. 40).

### 4.3 Integral balance equations for mechanical and internal energy

The integral energy equation (4.3) is written for the combined quantity $e + \lvert\vec{v}\rvert^2/2$. It is interesting to write separate integral equations for the mechanical and the internal energy. Integrating (4.21) over $V_f(t)$, and using (Notes.pdf, Eq. 4.23)

$$ \rho\frac{D}{Dt}\left(\frac{\lvert\vec{v}\rvert^2}{2}\right) = \frac{\partial}{\partial t}\left(\frac{\rho\lvert\vec{v}\rvert^2}{2}\right) + \nabla\cdot\left(\rho\vec{v}\frac{\lvert\vec{v}\rvert^2}{2}\right) \tag{4.23} $$

together with the Reynolds transport theorem (Notes.pdf, Eq. 3.6), gives for the mechanical energy (Notes.pdf, Eq. 4.24)

$$ \frac{d}{dt}\int_{V_f(t)}\frac{\rho\lvert\vec{v}\rvert^2}{2}\,dV = \underbrace{-\int_{\Sigma_f(t)} p\vec{v}\cdot\vec{n}\,d\sigma + \int_{\Sigma_f(t)} \vec{v}\cdot\bar{\bar{\tau}}'\cdot\vec{n}\,d\sigma + \int_{V_f(t)}\rho\vec{f}_m\cdot\vec{v}\,dV}_{\text{work of surface and mass forces}} + \int_{V_f(t)} p\nabla\cdot\vec{v}\,dV - \int_{V_f(t)}\phi_v\,dV \tag{4.24} $$

Similarly (4.22) gives for the internal energy (Notes.pdf, Eq. 4.25)

$$ \frac{d}{dt}\int_{V_f(t)}\rho e\,dV = \underbrace{-\int_{\Sigma_f(t)}\vec{q}\cdot\vec{n}\,d\sigma + \int_{V_f(t)}(Q_c + Q_r)\,dV}_{\text{heat added}} - \int_{V_f(t)} p\nabla\cdot\vec{v}\,dV + \int_{V_f(t)}\phi_v\,dV \tag{4.25} $$

The way (4.24) and (4.25) are written gives a clear picture of the balances of work and energy in the flow field:

- The work done by the mass forces in the interior of the fluid volume and by the surface forces on its bounding surface (first group of terms of (4.24)) increases the net amount of **mechanical energy** contained in the fluid volume.
- The heat added by conduction, radiation and chemical reaction (first group of terms of (4.25)) is used directly to increase the **internal energy**.
- Viscous dissipation and compression work, written in separate terms, are the mechanisms that transform mechanical energy into internal energy. Only the compression work is reversible.

### 4.4 Enthalpy equation

Equations (4.5) and (4.10) together with (4.19) are the so-called **Navier-Stokes equations** governing fluid motion. The energy equation admits alternative forms. For gas flows it is often convenient to use the enthalpy $h = e + p/\rho$ instead of the internal energy $e$. First, use continuity (4.5) in the form (4.6) to write (Notes.pdf, Eq. 4.26)

$$ \nabla\cdot(p\vec{v}) = \rho\frac{D}{Dt}\left(\frac{p}{\rho}\right) - \frac{\partial p}{\partial t} \tag{4.26} $$

(indeed $\rho\,D(p/\rho)/Dt = Dp/Dt - (p/\rho)D\rho/Dt = \partial p/\partial t + \vec{v}\cdot\nabla p + p\nabla\cdot\vec{v} = \partial p/\partial t + \nabla\cdot(p\vec{v})$). Combining it with (4.19) gives (Notes.pdf, Eq. 4.27)

$$ \rho\frac{D}{Dt}\left(h + \frac{\lvert\vec{v}\rvert^2}{2}\right) = \frac{\partial p}{\partial t} + \nabla\cdot(\vec{v}\cdot\bar{\bar{\tau}}') + \rho\vec{f}_m\cdot\vec{v} - \nabla\cdot\vec{q} + Q_c + Q_r \tag{4.27} $$

which, with the help of (4.21), can also be written as a separate equation for the enthalpy (Notes.pdf, Eq. 4.28):

$$ \rho\frac{Dh}{Dt} = \frac{Dp}{Dt} + \phi_v - \nabla\cdot\vec{q} + Q_c + Q_r \tag{4.28} $$

When the mass forces are conservative and steady, (4.27) reduces to (Notes.pdf, Eq. 4.29)

$$ \rho\frac{D}{Dt}\left(h + \frac{\lvert\vec{v}\rvert^2}{2} + U\right) = \frac{\partial p}{\partial t} + \nabla\cdot(\vec{v}\cdot\bar{\bar{\tau}}') - \nabla\cdot\vec{q} + Q_c + Q_r \tag{4.29} $$

indicating that, when heat addition, temporal pressure variations and viscous dissipation are all simultaneously negligible, the combination $h + \lvert\vec{v}\rvert^2/2 + U$ remains constant in the evolution of each fluid particle.

### 4.5 Entropy equation

It is also of interest to express the energy equation in terms of the entropy $s$. Since $T\,ds = dh - dp/\rho$, equation (4.28) gives (Notes.pdf, Eq. 4.30)

$$ \rho T\frac{Ds}{Dt} = \phi_v - \nabla\cdot\vec{q} + Q_c + Q_r \tag{4.30} $$

The entropy of a fluid particle increases because of viscous dissipation and heat addition, while the rate of compression work $-p\nabla\cdot\vec{v}$ is reversible and does not change the entropy of the particle. Equation (4.30) is an application of the second principle of thermodynamics, and allows entropy changes to be quantified for fluids out of equilibrium.

Divide (4.30) by $T$ and use $\nabla\cdot\vec{q}/T = \nabla\cdot(\vec{q}/T) + (\vec{q}\cdot\nabla T)/T^2$. Integrating in $V_f(t)$ gives, for the total entropy contained in a fluid volume (Notes.pdf, Eq. 4.31),

$$ \frac{d}{dt}\int_{V_f(t)}\rho s\,dV = \int_{V_f(t)}\frac{\phi_v}{T}\,dV - \int_{V_f(t)}\frac{\vec{q}\cdot\nabla T}{T^2}\,dV - \int_{\Sigma_f(t)}\frac{\vec{q}}{T}\cdot\vec{n}\,d\sigma + \int_{V_f(t)}\frac{Q_c + Q_r}{T}\,dV \tag{4.31} $$

- $(Q_c + Q_r)/T$ is a volumetric source of entropy associated with chemical reaction and radiation.
- $\vec{q}\cdot\vec{n}/T$ is the entropy flux across the surface due to heat conduction, so $-\int_{\Sigma_f}(\vec{q}/T)\cdot\vec{n}\,d\sigma$ is the corresponding rate of entropy gain.
- Viscous dissipation gives a non-negative contribution $\int_{V_f}(\phi_v/T)\,dV$.
- $-\int_{V_f}[(\vec{q}\cdot\nabla T)/T^2]\,dV$ is an additional source of entropy due to conduction, which can be shown to be irreversible with the help of (Notes.pdf, Eq. 3.44).

---

## 5. Mathematical Description of Fluid Flows

### What has been built so far

The derivation began by introducing the **continuum hypothesis**, which defines the density $\rho$, the velocity $\vec{v}$ and the internal energy $e$ as continuous functions of position $\vec{x}$ and time $t$. Next, the hypothesis of **local thermodynamic equilibrium** defines the local values of all remaining thermodynamic variables (temperature, pressure, enthalpy, and so on) in terms of $\rho$ and $e$, even for the non-equilibrium states found in fluid mechanics problems. This allows $\rho$ and $e$ to be replaced by $p$ and $T$ as the fundamental thermodynamic variables of the flow-field description. Finally, the viscous stress tensor $\bar{\bar{\tau}}'$ and the heat flux vector $\vec{q}$ are assumed to be **linear isotropic functions** of the rate of strain and of the temperature gradient, respectively. The resulting constitutive equations (Navier-Poisson and Fourier laws) contain three transport coefficients, $\mu$, $\mu_B$ and $k$, assumed to be functions of the local thermodynamic state of the fluid.

Some of these hypotheses can be expected to fail under extreme conditions (rarefied flows, nanofluidics applications, and so on), but the formulation covers most applications of engineering interest.

### Summary of conservation equations, equations of state and constitutive equations

To solve a given flow problem, the conservation equations of continuity, momentum and energy

$$ \frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\vec{v}) = 0 \tag{4.32} $$

$$ \rho\frac{D\vec{v}}{Dt} = -\nabla p + \nabla\cdot\bar{\bar{\tau}}' + \rho\vec{f}_m \tag{4.33} $$

$$ \rho\frac{De}{Dt} = -p\nabla\cdot\vec{v} + \bar{\bar{\tau}}':\nabla\vec{v} - \nabla\cdot\vec{q} + Q_c + Q_r \tag{4.34} $$

must be supplemented with the equations of state

$$ \rho = \rho(p,T) \quad\text{and}\quad e = e(p,T) \tag{4.35} $$

together with the constitutive equations (Navier-Poisson and Fourier)

$$ \bar{\bar{\tau}}' = \mu(\nabla\vec{v} + \nabla\vec{v}^{\,T}) + \left(\mu_B - \frac{2}{3}\mu\right)(\nabla\cdot\vec{v})\bar{\bar{I}} \quad\text{and}\quad \vec{q} = -k\nabla T \tag{4.36} $$

and the associated state functions

$$ \mu = \mu(T), \quad \mu_B = \mu_B(T) \quad\text{and}\quad k = k(T) \tag{4.37} $$

In particular, the state equations (4.35) reduce, for a **perfect liquid**, to

$$ \rho = \rho_o \quad\text{and}\quad e = e_o + cT \tag{4.38} $$

and, for a **perfect gas**, to

$$ \rho = \frac{p}{R_g T} \quad\text{and}\quad e = e_o + c_v T \tag{4.39} $$

The vector expressions of Chapter 2 allow (4.32), (4.33) and (4.34) to be written in any system of orthogonal curvilinear coordinates.

### Perfect liquid with constant viscosity

For a perfect liquid with constant viscosity and thermal conductivity, equations (4.32)-(4.34) take the simplified form (Notes.pdf, Eqs. 4.40-4.42)

$$ \nabla\cdot\vec{v} = 0 \tag{4.40} $$

$$ \rho\frac{D\vec{v}}{Dt} = -\nabla p - \mu\nabla\wedge(\nabla\wedge\vec{v}) + \rho\vec{f}_m \tag{4.41} $$

$$ \rho c\frac{DT}{Dt} = 2\mu\bar{\bar{T}}_d:\bar{\bar{T}}_d + k\nabla^2 T + Q_c + Q_r \tag{4.42} $$

Here (4.42) comes from (4.34) with $e = e_o + cT$, $\nabla\cdot\vec{v} = 0$ (so the compression work vanishes and $\phi_v = 2\mu\bar{\bar{T}}_d:\bar{\bar{T}}_d$) and $\vec{q} = -k\nabla T$ with constant $k$. These equations are written out in Section 8 for Cartesian, cylindrical and spherical coordinates.

---

## 6. Initial and Boundary Conditions

Equations (4.32)-(4.34) describe all fluid motions, within the range of validity of the hypotheses introduced in their derivation. The difference between two flow problems lies in their **initial and boundary conditions**, which must be specified so that the Navier-Stokes equations can be integrated.

### Initial conditions

For unsteady motion, at the initial instant the velocity field $\vec{v} = \vec{v}_o(\vec{x})$ must be given together with the thermodynamic state, for instance $p = p_o(\vec{x})$ and $T = T_o(\vec{x})$ (or any other pair of independent thermodynamic variables).

- For an **incompressible** fluid the initial velocity field must necessarily satisfy $\nabla\cdot\vec{v}_o = 0$.
- For a **gas** there is no such restriction, because of the term $\partial\rho/\partial t$ in (4.32).
- No initial conditions are required for **steady or periodic** flows.

### Solid wall: no-slip condition

The Navier-Stokes equations determine the flow evolution inside the flow field and must be complemented with boundary conditions on its boundaries. In typical configurations the fluid is confined by solid walls, as in ducted flows. The fluid velocity in contact with the wall is assumed equal to the wall velocity: at $\vec{x} = \vec{x}_p$

$$ \vec{v} = \vec{v}_p \tag{no-slip} $$

which reduces to $\vec{v} = 0$ when the wall is at rest relative to the reference frame. This **no-slip condition** comes from assuming that the interaction of the molecules near the wall with the wall is equivalent to that occurring between neighbouring fluid particles. For the velocity field to be continuous, no velocity discontinuity is allowed between the wall and the adjacent fluid. There is ample experimental evidence confirming the condition, at least for flows in which the mean free path $\lambda$ is much shorter than the macroscopic length $L$ of the flow field. When this is not the case, the no-slip condition must be relaxed, along with the condition of local thermodynamic equilibrium, which complicates the analysis.

### Solid wall: temperature

Local thermodynamic equilibrium is also assumed at the wall, so the fluid temperature in contact with the wall equals the wall temperature:

$$ T = T_p \quad\text{at}\quad \vec{x} = \vec{x}_p $$

There must also be an equilibrium of heat fluxes at the wall surface, which gives an additional equation. It reduces to

$$ \vec{q}\cdot\vec{n} = 0, \quad\text{that is,}\quad \frac{\partial T}{\partial n} = 0 \quad\text{at}\quad \vec{x} = \vec{x}_p $$

when the wall is thermally insulated (**adiabatic wall**). In principle, either the temperature distribution $T_p$ or the heat flux $\partial T/\partial n$ could be used as boundary condition for the temperature. In many problems, however, neither quantity is known a priori and both must be determined as part of the solution. That involves integrating the Navier-Stokes equations for the fluid together with the heat conduction equation in the solid, coupled through the conditions of thermodynamic equilibrium and heat flux balance at the wall surface.

### Fluid extending to infinity

For external problems (distances much larger than the characteristic macroscopic size $L$ of the flow field, as in external aerodynamics) the boundary conditions specify the velocity field and its accompanying thermodynamic state far away:

$$ \vec{v} = \vec{v}_\infty(\vec{x},t), \quad p = p_\infty(\vec{x},t), \quad T = T_\infty(\vec{x},t) \quad\text{for}\quad \lvert\vec{x}\rvert \to \infty $$

For instance, to study a uniform stream of velocity $U_\infty$ over a solid body of characteristic size $L$, impose $\vec{v} = U_\infty\vec{e}_x$, $p = p_\infty$ and $T = T_\infty$ at $\lvert\vec{x}\rvert/L \gg 1$.

### Example: a sphere in a liquid stream

![[attachments/FM-T4/sphere-in-stream.svg]]

Consider a liquid stream that moves with velocity $U_\infty(t)\vec{e}_x$ over a spherical body of radius $R$. If the density and transport properties of the fluid are constant and the effects of radiation and chemical reaction are negligible, the problem reduces to integrating (Notes.pdf, Eqs. 4.43-4.45)

$$ \nabla\cdot\vec{v} = 0 \tag{4.43} $$

$$ \rho\frac{\partial\vec{v}}{\partial t} + \rho\vec{v}\cdot\nabla\vec{v} = -\nabla p + \mu\nabla^2\vec{v} + \rho g\vec{e}_z \tag{4.44} $$

$$ \rho c\frac{\partial T}{\partial t} + \rho c\vec{v}\cdot\nabla T = 2\mu\bar{\bar{T}}_d:\bar{\bar{T}}_d + k\nabla^2 T \tag{4.45} $$

Boundary conditions must be imposed on the surface of the body (Notes.pdf, Eq. 4.46, as printed)

$$ \lvert\vec{x}\rvert = R: \quad \vec{v} = 0, \quad T - T_w = 0 \tag{4.46} $$

where $T_w$ is the temperature on the surface of the body, different from the value $T_\infty$ of the free stream. Far from the body the velocity should approach that of the free stream, whereas the pressure balances the gravity and inertial forces according to

$$ \lvert\vec{x}\rvert \gg R: \quad \vec{v} = U_\infty\vec{e}_x, \quad T = T_\infty, \quad p + \rho g z + \rho\frac{dU_\infty}{dt}x = \text{constant} \tag{4.47} $$

If the fluid is initially at rest ($U_\infty = 0$ for $t \leq 0$), appropriate initial conditions are

$$ t = 0: \quad \vec{v} = 0, \quad T = T_\infty + \frac{T_w - T_\infty}{\lvert\vec{x}\rvert/R} \tag{4.48} $$

The temperature field in (4.48) is the one obtained for a fluid at rest by solving the reduced energy equation $\nabla^2 T = 0$ with spherical symmetry. Indeed, in that case $\nabla^2 T = r^{-2}\,d(r^2\,dT/dr)/dr = 0$ gives $T = A + B/r$, and imposing $T(R) = T_w$ and $T(\infty) = T_\infty$ gives $T = T_\infty + (T_w - T_\infty)R/r$.

> [!warning] Sign of the gravity term in Eq. 4.44 as printed in the notes
> Equation (4.44) in Notes.pdf is printed with $+\rho g\vec{e}_z$, but the figure shows gravity pointing down ($\vec{g} = -g\vec{e}_z$) and the far-field condition (4.47) contains $p + \rho g z$, which corresponds to a mass force $\vec{f}_m = -g\vec{e}_z$ (hydrostatic balance $\nabla p = -\rho g\vec{e}_z$). With the figure's axes the gravity term of the momentum equation is therefore $-\rho g\vec{e}_z$. The equation is transcribed here as printed; use the sign consistent with (4.47) when solving problems.

---

## 7. Stress-Tensor Components for a Newtonian Fluid

The components of the viscous stress tensor follow from the Navier-Poisson law (Notes.pdf, Eq. 3.31):

$$ \tau'_{ij} = 2\mu\gamma_{ij} + \left(\mu_B - \frac{2}{3}\mu\right)(\nabla\cdot\vec{v})\,\delta_{ij} $$

where $\gamma_{ij} = [(\nabla\vec{v})_{ij} + (\nabla\vec{v}^{\,T})_{ij}]/2$ is the $ij$ component of the rate-of-strain tensor $\bar{\bar{T}}_d$ and $\delta_{ij}$ is the Kronecker delta ($\delta_{ii} = 1$, $\delta_{ij} = 0$ if $i \neq j$).

From the expressions of Chapter 2, in orthogonal coordinates $(x_1,x_2,x_3)$ with scale factors $h_i$,

$$ \gamma_{ii} = \frac{1}{h_i}\frac{\partial v_i}{\partial x_i} + \sum_{k\neq i}\frac{v_k}{h_i h_k}\frac{\partial h_i}{\partial x_k} \qquad \gamma_{ij} = \frac{h_j}{2h_i}\frac{\partial}{\partial x_i}\left(\frac{v_j}{h_j}\right) + \frac{h_i}{2h_j}\frac{\partial}{\partial x_j}\left(\frac{v_i}{h_i}\right)\quad (i\neq j) $$

$$ \nabla\cdot\vec{v} = \frac{1}{h_1h_2h_3}\left[\frac{\partial}{\partial x_1}(h_2h_3v_1) + \frac{\partial}{\partial x_2}(h_1h_3v_2) + \frac{\partial}{\partial x_3}(h_1h_2v_3)\right] $$

With these, $\tau'_{ij} = \tau'_{ji}$ can be written in the usual coordinate systems.

### Cartesian coordinates $(x,y,z)$

$$ \nabla\cdot\vec{v} = \frac{\partial v_x}{\partial x} + \frac{\partial v_y}{\partial y} + \frac{\partial v_z}{\partial z} $$

| Normal stresses | Shear stresses |
| :--- | :--- |
| $\tau'_{xx} = 2\mu\dfrac{\partial v_x}{\partial x} + (\mu_B - \tfrac{2}{3}\mu)(\nabla\cdot\vec{v})$ | $\tau'_{xy} = \mu\left(\dfrac{\partial v_x}{\partial y} + \dfrac{\partial v_y}{\partial x}\right)$ |
| $\tau'_{yy} = 2\mu\dfrac{\partial v_y}{\partial y} + (\mu_B - \tfrac{2}{3}\mu)(\nabla\cdot\vec{v})$ | $\tau'_{yz} = \mu\left(\dfrac{\partial v_y}{\partial z} + \dfrac{\partial v_z}{\partial y}\right)$ |
| $\tau'_{zz} = 2\mu\dfrac{\partial v_z}{\partial z} + (\mu_B - \tfrac{2}{3}\mu)(\nabla\cdot\vec{v})$ | $\tau'_{zx} = \mu\left(\dfrac{\partial v_x}{\partial z} + \dfrac{\partial v_z}{\partial x}\right)$ |

### Cylindrical coordinates $(r,\theta,z)$

$$ \nabla\cdot\vec{v} = \frac{1}{r}\frac{\partial(rv_r)}{\partial r} + \frac{1}{r}\frac{\partial v_\theta}{\partial\theta} + \frac{\partial v_z}{\partial z} $$

| Normal stresses | Shear stresses |
| :--- | :--- |
| $\tau'_{rr} = 2\mu\dfrac{\partial v_r}{\partial r} + (\mu_B - \tfrac{2}{3}\mu)(\nabla\cdot\vec{v})$ | $\tau'_{r\theta} = \mu\left[r\dfrac{\partial}{\partial r}\left(\dfrac{v_\theta}{r}\right) + \dfrac{1}{r}\dfrac{\partial v_r}{\partial\theta}\right]$ |
| $\tau'_{\theta\theta} = 2\mu\left(\dfrac{1}{r}\dfrac{\partial v_\theta}{\partial\theta} + \dfrac{v_r}{r}\right) + (\mu_B - \tfrac{2}{3}\mu)(\nabla\cdot\vec{v})$ | $\tau'_{\theta z} = \mu\left(\dfrac{1}{r}\dfrac{\partial v_z}{\partial\theta} + \dfrac{\partial v_\theta}{\partial z}\right)$ |
| $\tau'_{zz} = 2\mu\dfrac{\partial v_z}{\partial z} + (\mu_B - \tfrac{2}{3}\mu)(\nabla\cdot\vec{v})$ | $\tau'_{zr} = \mu\left(\dfrac{\partial v_r}{\partial z} + \dfrac{\partial v_z}{\partial r}\right)$ |

### Spherical coordinates $(r,\theta,\phi)$

$$ \nabla\cdot\vec{v} = \frac{1}{r^2}\frac{\partial(r^2v_r)}{\partial r} + \frac{1}{r\sin\theta}\frac{\partial(v_\theta\sin\theta)}{\partial\theta} + \frac{1}{r\sin\theta}\frac{\partial v_\phi}{\partial\phi} $$

| Normal stresses | Shear stresses |
| :--- | :--- |
| $\tau'_{rr} = 2\mu\dfrac{\partial v_r}{\partial r} + (\mu_B - \tfrac{2}{3}\mu)(\nabla\cdot\vec{v})$ | $\tau'_{r\theta} = \mu\left[r\dfrac{\partial}{\partial r}\left(\dfrac{v_\theta}{r}\right) + \dfrac{1}{r}\dfrac{\partial v_r}{\partial\theta}\right]$ |
| $\tau'_{\theta\theta} = 2\mu\left(\dfrac{1}{r}\dfrac{\partial v_\theta}{\partial\theta} + \dfrac{v_r}{r}\right) + (\mu_B - \tfrac{2}{3}\mu)(\nabla\cdot\vec{v})$ | $\tau'_{\theta\phi} = \mu\left[\dfrac{\sin\theta}{r}\dfrac{\partial}{\partial\theta}\left(\dfrac{v_\phi}{\sin\theta}\right) + \dfrac{1}{r\sin\theta}\dfrac{\partial v_\theta}{\partial\phi}\right]$ |
| $\tau'_{\phi\phi} = 2\mu\left(\dfrac{1}{r\sin\theta}\dfrac{\partial v_\phi}{\partial\phi} + \dfrac{v_r}{r} + \dfrac{v_\theta\cot\theta}{r}\right) + (\mu_B - \tfrac{2}{3}\mu)(\nabla\cdot\vec{v})$ | $\tau'_{\phi r} = \mu\left[\dfrac{1}{r\sin\theta}\dfrac{\partial v_r}{\partial\phi} + r\dfrac{\partial}{\partial r}\left(\dfrac{v_\phi}{r}\right)\right]$ |

---

## 8. The Navier-Stokes Equations in Orthogonal Coordinates

The following forms hold for a **perfect liquid** with constant $\mu$ and $k$ (Notes.pdf, Eqs. 4.40-4.42 written out). In each system the viscous dissipation $\phi_v = 2\mu\bar{\bar{T}}_d:\bar{\bar{T}}_d$ is given with the energy equation.

### Cartesian coordinates $(x,y,z)$

Continuity:

$$ \frac{\partial v_x}{\partial x} + \frac{\partial v_y}{\partial y} + \frac{\partial v_z}{\partial z} = 0 $$

Momentum:

$$ \rho\left(\frac{\partial v_x}{\partial t} + v_x\frac{\partial v_x}{\partial x} + v_y\frac{\partial v_x}{\partial y} + v_z\frac{\partial v_x}{\partial z}\right) = -\frac{\partial p}{\partial x} + \mu\left(\frac{\partial^2 v_x}{\partial x^2} + \frac{\partial^2 v_x}{\partial y^2} + \frac{\partial^2 v_x}{\partial z^2}\right) + \rho f_{mx} $$

$$ \rho\left(\frac{\partial v_y}{\partial t} + v_x\frac{\partial v_y}{\partial x} + v_y\frac{\partial v_y}{\partial y} + v_z\frac{\partial v_y}{\partial z}\right) = -\frac{\partial p}{\partial y} + \mu\left(\frac{\partial^2 v_y}{\partial x^2} + \frac{\partial^2 v_y}{\partial y^2} + \frac{\partial^2 v_y}{\partial z^2}\right) + \rho f_{my} $$

$$ \rho\left(\frac{\partial v_z}{\partial t} + v_x\frac{\partial v_z}{\partial x} + v_y\frac{\partial v_z}{\partial y} + v_z\frac{\partial v_z}{\partial z}\right) = -\frac{\partial p}{\partial z} + \mu\left(\frac{\partial^2 v_z}{\partial x^2} + \frac{\partial^2 v_z}{\partial y^2} + \frac{\partial^2 v_z}{\partial z^2}\right) + \rho f_{mz} $$

Energy:

$$ \rho c\left(\frac{\partial T}{\partial t} + v_x\frac{\partial T}{\partial x} + v_y\frac{\partial T}{\partial y} + v_z\frac{\partial T}{\partial z}\right) = \phi_v + k\left(\frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} + \frac{\partial^2 T}{\partial z^2}\right) + Q_c + Q_r $$

with the viscous dissipation

$$ \phi_v = \mu\left\{2\left[\left(\frac{\partial v_x}{\partial x}\right)^2 + \left(\frac{\partial v_y}{\partial y}\right)^2 + \left(\frac{\partial v_z}{\partial z}\right)^2\right] + \left(\frac{\partial v_x}{\partial y} + \frac{\partial v_y}{\partial x}\right)^2 + \left(\frac{\partial v_x}{\partial z} + \frac{\partial v_z}{\partial x}\right)^2 + \left(\frac{\partial v_y}{\partial z} + \frac{\partial v_z}{\partial y}\right)^2\right\} $$

### Cylindrical coordinates $(r,\theta,z)$

Continuity:

$$ \frac{1}{r}\frac{\partial(rv_r)}{\partial r} + \frac{1}{r}\frac{\partial v_\theta}{\partial\theta} + \frac{\partial v_z}{\partial z} = 0 $$

Momentum:

$$ \rho\left(\frac{\partial v_r}{\partial t} + v_r\frac{\partial v_r}{\partial r} + \frac{v_\theta}{r}\frac{\partial v_r}{\partial\theta} - \frac{v_\theta^2}{r} + v_z\frac{\partial v_r}{\partial z}\right) = -\frac{\partial p}{\partial r} + \mu\left[\frac{\partial}{\partial r}\left(\frac{1}{r}\frac{\partial(rv_r)}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2 v_r}{\partial\theta^2} + \frac{\partial^2 v_r}{\partial z^2} - \frac{2}{r^2}\frac{\partial v_\theta}{\partial\theta}\right] + \rho f_{mr} $$

$$ \rho\left(\frac{\partial v_\theta}{\partial t} + v_r\frac{\partial v_\theta}{\partial r} + \frac{v_\theta}{r}\frac{\partial v_\theta}{\partial\theta} + \frac{v_rv_\theta}{r} + v_z\frac{\partial v_\theta}{\partial z}\right) = -\frac{1}{r}\frac{\partial p}{\partial\theta} + \mu\left[\frac{\partial}{\partial r}\left(\frac{1}{r}\frac{\partial(rv_\theta)}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2 v_\theta}{\partial\theta^2} + \frac{\partial^2 v_\theta}{\partial z^2} + \frac{2}{r^2}\frac{\partial v_r}{\partial\theta}\right] + \rho f_{m\theta} $$

$$ \rho\left(\frac{\partial v_z}{\partial t} + v_r\frac{\partial v_z}{\partial r} + \frac{v_\theta}{r}\frac{\partial v_z}{\partial\theta} + v_z\frac{\partial v_z}{\partial z}\right) = -\frac{\partial p}{\partial z} + \mu\left[\frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial v_z}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2 v_z}{\partial\theta^2} + \frac{\partial^2 v_z}{\partial z^2}\right] + \rho f_{mz} $$

Energy:

$$ \rho c\left(\frac{\partial T}{\partial t} + v_r\frac{\partial T}{\partial r} + \frac{v_\theta}{r}\frac{\partial T}{\partial\theta} + v_z\frac{\partial T}{\partial z}\right) = \phi_v + k\left[\frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial T}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2 T}{\partial\theta^2} + \frac{\partial^2 T}{\partial z^2}\right] + Q_c + Q_r $$

with

$$ \phi_v = \mu\left\{2\left[\left(\frac{\partial v_r}{\partial r}\right)^2 + \left(\frac{1}{r}\frac{\partial v_\theta}{\partial\theta} + \frac{v_r}{r}\right)^2 + \left(\frac{\partial v_z}{\partial z}\right)^2\right] + \left(\frac{1}{r}\frac{\partial v_z}{\partial\theta} + \frac{\partial v_\theta}{\partial z}\right)^2 + \left[r\frac{\partial}{\partial r}\left(\frac{v_\theta}{r}\right) + \frac{1}{r}\frac{\partial v_r}{\partial\theta}\right]^2 + \left(\frac{\partial v_r}{\partial z} + \frac{\partial v_z}{\partial r}\right)^2\right\} $$

### Spherical coordinates $(r,\theta,\phi)$

Continuity:

$$ \frac{1}{r^2}\frac{\partial(r^2v_r)}{\partial r} + \frac{1}{r\sin\theta}\frac{\partial(v_\theta\sin\theta)}{\partial\theta} + \frac{1}{r\sin\theta}\frac{\partial v_\phi}{\partial\phi} = 0 $$

Momentum:

$$ \rho\left(\frac{\partial v_r}{\partial t} + v_r\frac{\partial v_r}{\partial r} + \frac{v_\theta}{r}\frac{\partial v_r}{\partial\theta} + \frac{v_\phi}{r\sin\theta}\frac{\partial v_r}{\partial\phi} - \frac{v_\theta^2 + v_\phi^2}{r}\right) = -\frac{\partial p}{\partial r} + \mu\left[\frac{\partial}{\partial r}\left(\frac{1}{r^2}\frac{\partial(r^2v_r)}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial v_r}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2 v_r}{\partial\phi^2} - \frac{2}{r^2\sin\theta}\frac{\partial(v_\theta\sin\theta)}{\partial\theta} - \frac{2}{r^2\sin\theta}\frac{\partial v_\phi}{\partial\phi}\right] + \rho f_{mr} $$

$$ \rho\left(\frac{\partial v_\theta}{\partial t} + v_r\frac{\partial v_\theta}{\partial r} + \frac{v_\theta}{r}\frac{\partial v_\theta}{\partial\theta} + \frac{v_\phi}{r\sin\theta}\frac{\partial v_\theta}{\partial\phi} + \frac{v_rv_\theta}{r} - \frac{v_\phi^2\cot\theta}{r}\right) = -\frac{1}{r}\frac{\partial p}{\partial\theta} + \mu\left[\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial v_\theta}{\partial r}\right) + \frac{1}{r^2}\frac{\partial}{\partial\theta}\left(\frac{1}{\sin\theta}\frac{\partial(v_\theta\sin\theta)}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2 v_\theta}{\partial\phi^2} + \frac{2}{r^2}\frac{\partial v_r}{\partial\theta} - \frac{2\cot\theta}{r^2\sin\theta}\frac{\partial v_\phi}{\partial\phi}\right] + \rho f_{m\theta} $$

$$ \rho\left(\frac{\partial v_\phi}{\partial t} + v_r\frac{\partial v_\phi}{\partial r} + \frac{v_\theta}{r}\frac{\partial v_\phi}{\partial\theta} + \frac{v_\phi}{r\sin\theta}\frac{\partial v_\phi}{\partial\phi} + \frac{v_rv_\phi}{r} + \frac{v_\theta v_\phi\cot\theta}{r}\right) = -\frac{1}{r\sin\theta}\frac{\partial p}{\partial\phi} + \mu\left[\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial v_\phi}{\partial r}\right) + \frac{1}{r^2}\frac{\partial}{\partial\theta}\left(\frac{1}{\sin\theta}\frac{\partial(v_\phi\sin\theta)}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2 v_\phi}{\partial\phi^2} + \frac{2}{r^2\sin\theta}\frac{\partial v_r}{\partial\phi} + \frac{2\cot\theta}{r^2\sin\theta}\frac{\partial v_\theta}{\partial\phi}\right] + \rho f_{m\phi} $$

Energy:

$$ \rho c\left(\frac{\partial T}{\partial t} + v_r\frac{\partial T}{\partial r} + \frac{v_\theta}{r}\frac{\partial T}{\partial\theta} + \frac{v_\phi}{r\sin\theta}\frac{\partial T}{\partial\phi}\right) = \phi_v + k\left[\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial T}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial T}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2 T}{\partial\phi^2}\right] + Q_c + Q_r $$

with

$$ \phi_v = \mu\left\{2\left[\left(\frac{\partial v_r}{\partial r}\right)^2 + \left(\frac{1}{r}\frac{\partial v_\theta}{\partial\theta} + \frac{v_r}{r}\right)^2 + \left(\frac{1}{r\sin\theta}\frac{\partial v_\phi}{\partial\phi} + \frac{v_r}{r} + \frac{v_\theta\cot\theta}{r}\right)^2\right] + \left[\frac{\sin\theta}{r}\frac{\partial}{\partial\theta}\left(\frac{v_\phi}{\sin\theta}\right) + \frac{1}{r\sin\theta}\frac{\partial v_\theta}{\partial\phi}\right]^2 + \left[r\frac{\partial}{\partial r}\left(\frac{v_\theta}{r}\right) + \frac{1}{r}\frac{\partial v_r}{\partial\theta}\right]^2 + \left[\frac{1}{r\sin\theta}\frac{\partial v_r}{\partial\phi} + r\frac{\partial}{\partial r}\left(\frac{v_\phi}{r}\right)\right]^2\right\} $$

---

## 9. Practical Formulary of Topic 4

This section collects, for solving problems, everything defined above. Nothing new is derived here: each entry points to the equation of Chapter 4 it comes from, and the few simple consequences of the definitions are marked as such.

### 9.1 Fundamental equations

| Law | Vector form | Equation |
| :--- | :--- | :--- |
| Continuity | $\partial\rho/\partial t + \nabla\cdot(\rho\vec{v}) = 0$ | 4.5 |
| Continuity, incompressible | $\nabla\cdot\vec{v} = 0$ | 4.7 |
| Momentum (Cauchy) | $\rho\,D\vec{v}/Dt = -\nabla p + \nabla\cdot\bar{\bar{\tau}}' + \rho\vec{f}_m$ | 4.10, 4.33 |
| Momentum, incompressible, $\mu$ constant | $\rho\,D\vec{v}/Dt = -\nabla p + \mu\nabla^2\vec{v} + \rho\vec{f}_m$ | 4.12 |
| Momentum with reduced pressure | $\rho\,D\vec{v}/Dt = -\nabla P + \mu\nabla^2\vec{v}$, with $P = p + \rho U$ | 4.13 |
| Newtonian constitutive law | $\bar{\bar{\tau}}' = \mu(\nabla\vec{v} + \nabla\vec{v}^{\,T}) + (\mu_B - \tfrac{2}{3}\mu)(\nabla\cdot\vec{v})\bar{\bar{I}}$ | 4.36 |
| Fourier law | $\vec{q} = -k\nabla T$ | 4.36 |
| Internal energy | $\rho\,De/Dt = -p\nabla\cdot\vec{v} + \phi_v - \nabla\cdot\vec{q} + Q_c + Q_r$ | 4.22 |
| Total energy | $\rho\,D(e + \lvert\vec{v}\rvert^2/2)/Dt = -\nabla\cdot(p\vec{v}) + \nabla\cdot(\vec{v}\cdot\bar{\bar{\tau}}') + \rho\vec{f}_m\cdot\vec{v} - \nabla\cdot\vec{q} + Q_c + Q_r$ | 4.19 |
| Mechanical energy | $\rho\,D(\lvert\vec{v}\rvert^2/2)/Dt = -\vec{v}\cdot\nabla p + \vec{v}\cdot(\nabla\cdot\bar{\bar{\tau}}') + \rho\vec{v}\cdot\vec{f}_m$ | 4.21 |
| Enthalpy | $\rho\,Dh/Dt = Dp/Dt + \phi_v - \nabla\cdot\vec{q} + Q_c + Q_r$ | 4.28 |
| Entropy | $\rho T\,Ds/Dt = \phi_v - \nabla\cdot\vec{q} + Q_c + Q_r$ | 4.30 |
| Perfect liquid, temperature | $\rho c\,DT/Dt = 2\mu\bar{\bar{T}}_d:\bar{\bar{T}}_d + k\nabla^2T + Q_c + Q_r$ | 4.42 |
| Bernoulli (steady, inviscid, incompressible, $\vec{f}_m = -\nabla U$) | $p + \rho U + \rho\lvert\vec{v}\rvert^2/2 = C_l$ along a streamline | 4.17 |
| States | liquid: $\rho = \rho_o$, $e = e_o + cT$; gas: $\rho = p/(R_gT)$, $e = e_o + c_vT$ | 4.38, 4.39 |

Component forms of the continuity, momentum and energy equations: Section 8. Component forms of the viscous stresses: Section 7.

### 9.2 Viscous stresses, flow rate, mean velocity, wall shear stress and dissipation

| Quantity | Expression | Source |
| :--- | :--- | :--- |
| Viscous stress components, Cartesian | $\tau'_{xx} = 2\mu\,\partial_x v_x + (\mu_B - \tfrac{2}{3}\mu)\nabla\cdot\vec{v}$; $\tau'_{xy} = \mu(\partial_y v_x + \partial_x v_y)$ and cyclic permutations | Section 7 |
| Traction on a surface of normal $\vec{n}$ | $\vec{f}_n = (-p\bar{\bar{I}} + \bar{\bar{\tau}}')\cdot\vec{n}$ | Cauchy stress tensor, Chapter 3 |
| Viscous force per unit volume (incompressible, $\mu$ constant) | $\nabla\cdot\bar{\bar{\tau}}' = \mu\nabla^2\vec{v} = -\mu\nabla\wedge(\nabla\wedge\vec{v})$ | 4.11, 4.12 |
| Volume flow rate through a surface $\Sigma$ | $Q = \int_\Sigma\vec{v}\cdot\vec{n}\,d\sigma$ | definition (Chapter 3) |
| Mean velocity | $\bar{v} = Q/A$ | consequence of the definition of $Q$ (extension) |
| Wall shear stress, wall with normal $\vec{n}$ | tangential component of $\bar{\bar{\tau}}'\cdot\vec{n}$ at the wall, for instance $\tau_w = \mu\,\partial v_x/\partial y$ on a wall $y = \text{const}$ with $v = v_x(y)\vec{e}_x$ | Section 7 |
| Force of the fluid on a wall | $\vec{F} = \int_\Sigma(-p\bar{\bar{I}} + \bar{\bar{\tau}}')\cdot\vec{n}\,d\sigma$ | Chapter 3 |
| Viscous dissipation | $\phi_v = \bar{\bar{\tau}}':\nabla\vec{v} = 2\mu\bar{\bar{T}}_d:\bar{\bar{T}}_d$ for $\nabla\cdot\vec{v} = 0$; components in Section 8 | 4.22, 4.42 |
| Conductive heat flux through a surface | $\vec{q}\cdot\vec{n} = -k\,\partial T/\partial n$ | 4.36 |
| Reduced pressure | $P = p + \rho U$; $P = p + \rho g z$ for gravity along $-\vec{e}_z$ | 4.13 |

### 9.3 From the problem statement to the equations

Each phrase of a statement removes terms of the equations above. The right column states the mathematical consequence. Rows marked "from the statements of problems NS1-NS17" are standard assumptions of the official problems, not derivations of Chapter 4.

| Condition in the statement | Terms that vanish | Boundary or compatibility condition imposed |
| :--- | :--- | :--- |
| Steady | every $\partial/\partial t$ | none in time: no initial condition is needed (Section 6) |
| Incompressible, constant properties | $D\rho/Dt$; the compression work $-p\nabla\cdot\vec{v}$; $\phi_v = 2\mu\bar{\bar{T}}_d:\bar{\bar{T}}_d$ | continuity reduces to $\nabla\cdot\vec{v} = 0$; momentum and energy decouple (Section 3.2) |
| Planar (two-dimensional) | $v_z$ and every $\partial/\partial z$ | none |
| Unidirectional or parallel flow, $\vec{v} = v_x(y)\vec{e}_x$ | the convective term $\vec{v}\cdot\nabla\vec{v}$; $\partial v_x/\partial x$ through continuity | $v_y = 0$ is consistent with continuity; $y$-momentum gives $\partial p/\partial y = \rho f_{my}$ |
| Fully developed, $\partial\vec{v}/\partial x = 0$ | $\partial v/\partial x$ and $\partial^2v/\partial x^2$ | continuity then fixes $v_y$ as constant (a porous wall can impose it) |
| Dependence only on the distance to the wall, $\vec{v} = \vec{v}(z)$ | $\partial/\partial x$, $\partial/\partial y$ of the velocity | continuity gives $v_z = \text{constant}$, equal to the wall value |
| Axial symmetry about the axis | $\partial/\partial\theta$ of every variable | for rotation about the axis keep $v_\theta$; with no swirl, $v_\theta = 0$ |
| Spherical symmetry | $\partial/\partial\theta$, $\partial/\partial\phi$; $v_\theta = v_\phi = 0$ | continuity gives $r^2v_r = f(t)$; $r^2v_r$ constant if steady |
| Perfect liquid, $\mu$ and $k$ constant | variations of $\mu$, $k$; $\nabla\cdot\vec{v}$ terms in $\bar{\bar{\tau}}'$ | viscous force $\mu\nabla^2\vec{v}$; temperature equation (4.42) |
| Buoyancy-free | the temperature dependence of $\rho$ in the mass force | velocity and pressure decouple from $T$ |
| Negligible gravity | $\rho\vec{f}_m$ | $P = p$ |
| Negligible viscous dissipation | $\phi_v$ | energy equation reduces to convection and conduction only |
| Fixed solid wall | none | $\vec{v} = 0$ (no-slip) |
| Moving solid wall, velocity $\vec{v}_p$ | none | $\vec{v} = \vec{v}_p$ (no-slip) |
| Isothermal wall | none | $T = T_p$ |
| Adiabatic wall | none | $\vec{q}\cdot\vec{n} = 0$, $\partial T/\partial n = 0$ |
| Fluid extending to infinity, at rest or uniform | none | $\vec{v} = \vec{v}_\infty$, $p = p_\infty$, $T = T_\infty$ for $\lvert\vec{x}\rvert \to \infty$ (Section 6) |
| Porous wall with suction or injection velocity $V$ (from the statements of problems NS1-NS17) | none | normal velocity prescribed by the statement, for instance $v_n = \mp V$; the tangential velocity keeps the no-slip value |
| Free surface or air at a constant pressure, with $\mu_a \ll \mu$ (from the statements of problems NS5 and NS7) | none | $p = p_a$ and negligible viscous force of the air, that is $\bar{\bar{\tau}}'\cdot\vec{n} \approx 0$ on the liquid side: extension, not derived in Chapter 4 |
| Reduced pressure (conservative mass force, pressure not in the boundary conditions) | the mass force | solve for $P = p + \rho U$ and recover $p$ at the end (Section 3.3) |

**Back to:** [[01 - Fluid Mechanics/Fluid Mechanics MOC|Fluid Mechanics MOC]]
