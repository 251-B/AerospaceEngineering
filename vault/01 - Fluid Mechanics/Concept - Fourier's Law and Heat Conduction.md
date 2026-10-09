---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - theory
  - key-concept
  - fourier
  - heat-conduction
  - prandtl
dificultad: medium
prerrequisitos:
  - "[[01 - Fluid Mechanics/Topic 1 - Introductory Remarks and Starting Assumptions|Topic 1: Introductory Remarks]]"
---

# 🔬 Concept: Fourier's Law, Heat Conduction and the Prandtl Number

> **Key idea in one sentence:** Molecular heat transfer by conduction is governed by Fourier's Law $\vec{q} = -k\nabla T$, where the heat flux vector $\vec{q}$ projected onto the outward normal determines the surface heat exchange ($q_n = \vec{q}\cdot\vec{n}$); the molecular diffusion of momentum relative to that of heat is uniquely characterised by the dimensionless Prandtl number $\mathrm{Pr} = \nu/\alpha$.

---

## ☀️ 1. Conductive Heat Flux and the Thermal Cauchy Principle (Notes.pdf, Eqs. 3.39–3.43)

The heat transferred by conduction through a differential surface element $d\sigma$ oriented along the unit normal vector $\vec{n}$ is proportional to the area of the element:

$$ d\dot{Q}_{\text{cond}} = q_n(\vec{n}, \vec{x}, t) \, d\sigma \qquad \text{[Eq. 3.39]} $$

* **Official sign convention (Notes.pdf):** $q_n$ is defined as positive if thermal energy is transferred towards the fluid element to which $\vec{n}$ points (that is, heat leaving the bounded volume if $\vec{n}$ is the outward normal).

### Derivation of the Heat Flux Vector with the Cauchy Tetrahedron
As in the case of mechanical stresses, consider the differential fluid tetrahedron with infinitesimal coordinate edges. In the limit $h \to 0$, the energy balance on the tetrahedron reduces at first order to the equilibrium between the heat fluxes of the four faces (the volumetric storage term $\sim \mathcal{O}(h^3)$ is negligible compared with the surfaces $\sim \mathcal{O}(h^2)$):

$$ q_n dA = q_1 dA_1 + q_2 dA_2 + q_3 dA_3 \qquad \text{[Eq. 3.40]} $$

where $q_i$ represents the heat flux per unit area through a plane perpendicular to the basis vector $\vec{e}_i$. Using the trigonometric relation $dA_i = n_i dA$ and dividing by the area of the oblique face $dA$:

$$ \mathbf{q_n = n_1 q_1 + n_2 q_2 + n_3 q_3 = \vec{q} \cdot \vec{n}} \qquad \text{[Eq. 3.41]} $$

where $\vec{q}(\vec{x}, t) = (q_1, q_2, q_3)$ is the **heat flux density vector** (units $\text{W/m}^2$).

### Total Heat Flux and Divergence
The total heat transmitted by conduction outwards through a closed surface $\Sigma$ bounding a volume $V$ is given by:
$$ \dot{Q}_{\text{cond, net}} = \int_\Sigma \vec{q} \cdot \vec{n} \, d\sigma \qquad \text{[Eq. 3.42]} $$
Applying Gauss's theorem:
$$ \mathbf{\int_\Sigma \vec{q} \cdot \vec{n} \, d\sigma = \int_V (\nabla \cdot \vec{q}) \, dV} \qquad \text{[Eq. 3.43]} $$
Therefore, $\mathbf{\nabla \cdot \vec{q}}$ physically represents the **net rate of heat loss by conduction per unit volume** (net heat power escaping from the unit volume).

---

## 🔥 2. Fourier's Law (Notes.pdf, Eq. 3.44)

The heat flux vector due to molecular conduction follows the phenomenological law of Joseph Fourier (1822):

$$ \mathbf{\vec{q} = -k \nabla T} \qquad \text{[Eq. 3.44]} $$

* $\nabla T$: Spatial gradient of the absolute temperature.
* The negative sign guarantees compatibility with the Second Law of Thermodynamics: heat flows spontaneously from regions of higher temperature to regions of lower temperature ($\vec{q}$ points opposite to $\nabla T$).
* $k$: **Thermal conductivity** of the fluid, units $\text{W}/(\text{m}\cdot\text{K})$. It is a thermodynamic state property that depends on temperature and hardly at all on pressure.

---

## 📊 3. Physical Behaviour of the Thermal Conductivity $k(T)$

| Fluid | Dominant Physical Mechanism | Evolution with Temperature $T$ | Reference Values |
| :--- | :--- | :--- | :--- |
| **Gases (Air)** | Random molecular collisions and agitation ($v_{\text{th}} \propto \sqrt{T}$) | **Increases with $T$** ($\propto T^{1/2}$ or thermal Sutherland) | $k_a(288\text{ K}) = 0.025\text{ W/(m K)}$<br>$k_a(368\text{ K}) = 0.030\text{ W/(m K)}$ |
| **Common Liquids** | Transport by intermolecular interaction | **Decreases slightly with $T$** (dilatation separates molecules) | Lubricating oils: $k \approx 0.14\text{ W/(m K)}$ |
| **Liquid Water (Anomaly)** | Network of hydrogen bonds that reorganise thermally | **Increases with $T$** in the usual liquid range | $k_w(288\text{ K}) = 0.59\text{ W/(m K)}$<br>$k_w(368\text{ K}) = 0.68\text{ W/(m K)}$ |

---

## ⚡ 4. Thermal Diffusivity ($\alpha$) and Prandtl Number ($\mathrm{Pr}$)

To compare the rate at which a medium transports energy by conduction with its thermal inertia, the **thermal diffusivity** $\alpha$ is defined:

$$ \mathbf{\alpha = \frac{k}{\rho c_p}} \quad \text{(for gases or general liquids, or } \alpha = \frac{k}{\rho c} \text{ for incompressible liquids)} $$

* Units of $\alpha$: $\text{m}^2/\text{s}$ (identical kinematic dimensions to the kinematic viscosity $\nu = \mu/\rho$).

The dimensionless ratio between both molecular diffusivities defines the **Prandtl Number** ($\mathrm{Pr}$):

$$ \mathbf{\mathrm{Pr} = \frac{\nu}{\alpha} = \frac{\mu c_p}{k} = \frac{\text{Molecular Momentum Diffusion Rate}}{\text{Molecular Heat Diffusion Rate}}} $$

### Comparison of Physical Regimes in Aerospace Engineering

```
Pr << 1 (Liquid Metals: Hg, Na) ─── Pr ≈ 0.72 (Air and Gases) ─── Pr ≈ 2 to 8 (Water) ─── Pr >> 1 (Aerospace Oils)
    [Heat diffuses much faster            [Viscous and thermal boundary       [Momentum diffuses much
      than momentum]                       layers of similar thickness]        faster than heat]
```

1. **Gases in Aviation ($\mathrm{Pr} \sim 0.7$ to $0.8$):**
   For air over a very wide thermodynamic range ($150\text{ K} - 1500\text{ K}$), $\mathbf{\mathrm{Pr} \approx 0.72}$. This implies that on airfoils and nozzles, the viscous boundary-layer thickness $\delta_v$ and the thermal boundary-layer thickness $\delta_T$ are practically equal:
   $$ \frac{\delta_v}{\delta_T} \sim \mathrm{Pr}^{1/3} \approx (0.72)^{1/3} \approx 0.90 $$
2. **Turbine Lubricating Oils ($\mathrm{Pr} \gg 1$, from 100 to 10,000):**
   Viscous momentum diffusion is thousands of times faster than thermal dissipation. The heat generated by viscous friction remains confined in extremely thin thermal layers, requiring forced active cooling circuits in the bearings.
3. **Nuclear / Space Cooling Liquid Metals ($\mathrm{Pr} \ll 1$, $\sim 0.01 - 0.03$):**
   In space nuclear reactors cooled by sodium or mercury, free electrons transfer thermal energy at colossal rates, exceeding viscous transport by orders of magnitude.
4. **Liquid Water ($\mathrm{Pr} = 8.14$ at $288\text{ K} \to 1.82$ at $368\text{ K}$):**
   It shows a marked thermal sensitivity due to the exponential collapse of the viscosity $\mu_w(T)$.
