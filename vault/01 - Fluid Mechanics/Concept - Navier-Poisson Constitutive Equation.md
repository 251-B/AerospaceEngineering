---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - theory
  - key-concept
  - navier-poisson
  - viscosity
  - stokes
dificultad: high
prerrequisitos:
  - "[[01 - Fluid Mechanics/Concept - Stress Tensor and Cauchy Principle|Concept: Cauchy Stress Tensor]]"
  - "[[01 - Fluid Mechanics/Topic 2 - Flow Kinematics|Topic 2: Flow Kinematics]]"
---

# 🔬 Concept: Navier-Poisson Constitutive Equation

> **Key idea in one sentence:** The Navier-Poisson constitutive equation linearly relates the viscous stress tensor $\bar{\bar{\tau}}'$ to the rate-of-strain tensor $\bar{\bar{T}}_d$ in an isotropic Newtonian fluid, parametrised by two thermodynamic coefficients: the dynamic viscosity $\mu(T)$ and the bulk viscosity $\mu_B(T)$ (which vanishes under the classical Stokes hypothesis).

---

## 🧊 1. Fluid at Rest or in Rigid Motion (Notes.pdf, Eqs. 3.26–3.27)

By the very definition of a continuous fluid (introduced in Chapter 1), a fluid is unable to sustain tangential shear stresses in static equilibrium. Consequently:
1. If the fluid is **at rest** in an inertial frame, or
2. If the fluid moves with a **rigid-body motion** (pure translation and rotation with zero deformation $\bar{\bar{T}}_d = 0$),

the surface stresses act at every point strictly perpendicular to the surface and are independent of the orientation of $\vec{n}$:

$$ \vec{f}_n = -p\vec{n} \qquad \text{[Eq. 3.26]} $$

where $p(\vec{x}, t) > 0$ is the **local thermodynamic pressure** (an intensive state variable that satisfies the equation of state $p = \rho R T$ or $p = p(\rho, T)$). Equating with the general Cauchy relation $\vec{f}_n = \bar{\bar{\tau}}\cdot\vec{n}$, the hydrostatic stress tensor follows:

$$ \mathbf{\bar{\bar{\tau}} = -p \bar{\bar{I}}} \qquad \text{[Eq. 3.27]} $$

where $\bar{\bar{I}}$ is the unit identity tensor ($\delta_{ij}$).

---

## 🌊 2. Decomposition of the Stress Tensor (Notes.pdf, Eq. 3.28)

When there is relative motion with deformation between adjacent particles ($\bar{\bar{T}}_d \neq 0$), molecular friction and microscopic momentum transport generate additional stresses called **viscous stresses**.
The total stress tensor decomposes universally as:

$$ \mathbf{\bar{\bar{\tau}} = -p \bar{\bar{I}} + \bar{\bar{\tau}}'} \qquad \text{[Eq. 3.28]} $$

* $-p \bar{\bar{I}}$: spherical or isotropic part due to the thermodynamic pressure.
* $\bar{\bar{\tau}}'$: **viscous stress tensor** (*deviatoric stress tensor*), which must vanish identically when $\bar{\bar{T}}_d = 0$.

---

## 📐 3. Hypotheses of the Isotropic Newtonian Fluid (Notes.pdf, Eqs. 3.29–3.31)

To close the kinematic-dynamic model, Navier (1822) and Poisson (1831) postulated the following physical hypotheses for Newtonian fluids (air, water, aviation fuels and the usual combustion gases fully satisfy this behaviour):

1. **Exclusive dependence on the rate of strain:** $\bar{\bar{\tau}}'$ does not depend on the antisymmetric velocity gradient $\bar{\bar{T}}_r$ (rigid rotation generates no viscous dissipation), but only on $\bar{\bar{T}}_d$.
2. **Strict linearity:** The relation between viscous stresses and strain rates is linear:
   $$ \tau'_{ij} = \alpha_{ijkl} \gamma_{kl} \qquad \text{[Eq. 3.29]} $$
   where $\gamma_{kl} = (\bar{\bar{T}}_d)_{kl}$ and $\alpha_{ijkl}$ is a fourth-order tensor of properties of the medium.
3. **Spatial isotropy:** The fluid has no intrinsic privileged directions. The tensor $\alpha_{ijkl}$ must be invariant under any rotation of the coordinate system.

In the coordinate system defined by the **principal directions of deformation** (where $\bar{\bar{T}}_d$ is diagonal with principal rates $\gamma_1, \gamma_2, \gamma_3$):
By isotropy, the principal viscous stress $\tau'_1$ must depend symmetrically on $\gamma_1$ and on the other two orthogonal components $\gamma_2, \gamma_3$:
$$ \tau'_1 = \alpha \gamma_1 + \lambda (\gamma_2 + \gamma_3) $$
Adding and subtracting $\lambda \gamma_1$, and recalling that $\gamma_1 + \gamma_2 + \gamma_3 = \text{tr}(\bar{\bar{T}}_d) = \nabla \cdot \vec{v}$:
$$ \tau'_1 = (\alpha - \lambda)\gamma_1 + \lambda (\nabla \cdot \vec{v}) $$
Defining the **first coefficient of dynamic viscosity** as $\mu = \frac{1}{2}(\alpha - \lambda)$, the previous expression generalises to invariant tensor notation:

$$ \mathbf{\bar{\bar{\tau}}' = 2\mu \bar{\bar{T}}_d + \lambda (\nabla \cdot \vec{v}) \bar{\bar{I}}} \qquad \text{[Eq. 3.30]} $$

where:
* $\mu$: Shear dynamic viscosity (*shear viscosity*), units $\text{Pa}\cdot\text{s} = \text{kg}/(\text{m}\cdot\text{s})$.
* $\lambda$: Second coefficient of viscosity (*second viscosity*).

---

## 🧪 4. Bulk Viscosity ($\mu_B$) and the Stokes Hypothesis (Notes.pdf, Eq. 3.31)

Taking the trace of the viscous stress tensor $\bar{\bar{\tau}}'$:
$$ \text{tr}(\bar{\bar{\tau}}') = 2\mu \, \text{tr}(\bar{\bar{T}}_d) + 3\lambda (\nabla \cdot \vec{v}) = (2\mu + 3\lambda)(\nabla \cdot \vec{v}) $$
The **bulk viscosity** (*bulk viscosity*) $\mu_B$ is defined as:
$$ \mu_B = \lambda + \frac{2}{3}\mu \implies \lambda = \mu_B - \frac{2}{3}\mu $$

Substituting $\lambda$ into (3.30), the **canonical Navier-Poisson form** is obtained:

$$ \mathbf{\bar{\bar{\tau}}' = 2\mu \bar{\bar{T}}_d + \left(\mu_B - \frac{2}{3}\mu\right)(\nabla \cdot \vec{v}) \bar{\bar{I}}} \qquad \text{[Eq. 3.31]} $$

### The Classical Stokes Hypothesis (1845)
Sir George Gabriel Stokes argued that for fluids undergoing slow dilatation or compression, the bulk viscosity is negligible:
$$ \mathbf{\mu_B \approx 0 \implies \lambda = -\frac{2}{3}\mu} $$
* **Monatomic gases:** Boltzmann's kinetic theory shows analytically that $\mu_B \equiv 0$ exactly.
* **Diatomic/polyatomic gases (such as air):** $\mu_B \approx 0.6 \mu$, but its effect is only noticeable in ultra-high-frequency acoustic absorption phenomena or in the internal thickness of extreme hypersonic shock waves. In classical subsonic, supersonic and atmospheric aerodynamics, the Stokes hypothesis $\mu_B = 0$ is a universal standard.
* **Incompressible fluids ($\nabla \cdot \vec{v} = 0$):** The second summand vanishes identically regardless of the value of $\mu_B$:
  $$ \mathbf{\bar{\bar{\tau}}' = 2\mu \bar{\bar{T}}_d} $$

---

## 🌡️ 5. Thermal Dependence and Property Comparison (Air vs Water)

The dynamic viscosity $\mu$ is a thermodynamic state property that depends primarily on temperature $T$, being almost independent of pressure $p$ over conventional ranges:

* **In Gases (Air):** Momentum transport is due to the kinetic exchange of molecules between adjacent layers in random thermal motion. Raising $T$ increases the root-mean-square speed ($v_{\text{th}} \propto \sqrt{T}$), increasing the viscosity:
  $$ \mu_{\text{gas}}(T) \propto T^{1/2} \quad \text{or via Sutherland's Law:} \quad \mu(T) = \mu_0 \left(\frac{T}{T_0}\right)^{3/2} \frac{T_0 + S}{T + S} $$
  For air: at $T_0 = 288\text{ K}$, $\mu_a \approx 1.78 \times 10^{-5}\text{ Pa}\cdot\text{s}$.

* **In Liquids (Water):** Momentum transport is dominated by intermolecular cohesive forces. As $T$ increases, the molecules gain energy to escape from the potential wells, drastically reducing the cohesive forces and, with them, the viscosity:
  $$ \mu_{\text{liquid}}(T) \approx A \exp(B / T) $$
  For water: at $T = 288\text{ K}$, $\mu_w \approx 1.14 \times 10^{-3}\text{ Pa}\cdot\text{s}$ ($\approx 64$ times greater than that of air). At $T = 368\text{ K}$, it drops to $\mu_w \approx 0.30 \times 10^{-3}\text{ Pa}\cdot\text{s}$.

### ⚠️ Apparent Paradox: Kinematic Viscosity ($\nu = \mu/\rho$)
In aerodynamics, vorticity diffusion and boundary-layer thickness depend on the kinematic viscosity $\nu = \mu / \rho$:
* **Air at sea level ($288\text{ K}$):** $\rho_a \approx 1.225\text{ kg/m}^3 \implies \mathbf{\nu_a \approx 1.45 \times 10^{-5}\text{ m}^2/\text{s}}$.
* **Liquid water ($288\text{ K}$):** $\rho_w \approx 1000\text{ kg/m}^3 \implies \mathbf{\nu_w \approx 1.14 \times 10^{-6}\text{ m}^2/\text{s}}$.

> [!IMPORTANT] Crucial Counterintuitive Fact
> The kinematic viscosity of air is **13 to 15 times greater** than that of liquid water! Because of its low density, air diffuses molecular momentum much faster per unit of inertia than water.
