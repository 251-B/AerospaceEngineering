---
materia: Fluid Mechanics
tema: "Unit 05: Hydrostatics (plus supplementary fluid properties); not Notes.pdf Chapter 1"
tags:
  - formula-sheet
  - quick-reference
  - exam
  - fluid-mechanics
---

# 📋 Quick Reference: Fluid Properties and Statics

> [!note] Scope of this sheet
> The hydrostatics content (sections 2-4: fundamental equation, ISA atmosphere, forces on submerged surfaces, buoyancy) belongs to **unit 05 (Hydrostatics)**, not to Chapter 1 of Notes.pdf (Introductory Remarks and Starting Assumptions, see [[01 - Fluid Mechanics/Topic 1 - Introductory Remarks and Starting Assumptions]]). Sutherland's law (section 1) is supplementary material, also not part of Notes.pdf Chapter 1. The file name keeps the old "Tema 1" label only to avoid breaking links.

## ⚡ 1. Fundamental Properties (supplementary; Sutherland's law is not in Notes.pdf Ch. 1)

| Property | LaTeX Equation | Notes / Units |
| :--- | :--- | :--- |
| **Specific weight** | $ \gamma = \rho g $ | $[\text{N/m}^3]$ |
| **Newton's law of viscosity** | $ \tau = \mu \frac{du}{dy} $ | $\mu \text{ in } [\text{Pa}\cdot\text{s}]$, $\tau \text{ in } [\text{Pa}]$ |
| **Kinematic viscosity** | $ \nu = \frac{\mu}{\rho} $ | $[\text{m}^2/\text{s}]$, $1\text{ St} = 10^{-4}\text{ m}^2/\text{s}$ |
| **Sutherland's law (Air)** | $ \mu(T) = \mu_0 \left(\frac{T}{T_0}\right)^{3/2} \frac{T_0 + S}{T + S} $ | $S_{\text{air}} = 110.4\text{ K}$, $T_0 = 273.15\text{ K}$ |
| **Bulk modulus of compressibility** | $ K = \rho \left(\frac{\partial p}{\partial \rho}\right) $ | Ideal gas: $K_T = p$, $K_s = \gamma_{\text{ad}} p$ |
| **Speed of sound** | $ c = \sqrt{\gamma_{\text{ad}} R T} $ | Air: $\gamma_{\text{ad}} = 1.4$, $R = 287\text{ J/(kg}\cdot\text{K)}$ |

---

## ⚡ 2. Fundamental Equation and ISA Atmosphere (unit 05: Hydrostatics)

* **Differential equation:**
  $$ \nabla p = \rho \vec{g} \implies \frac{dp}{dz} = -\rho g $$
* **Incompressible liquid ($\rho = \text{const}$):**
  $$ p_2 - p_1 = -\rho g (z_2 - z_1) \iff p = p_0 + \rho g h $$
* **ISA Tropospheric Atmosphere ($0 \le z \le 11\,000\text{ m}$):**
  $$ T(z) = T_0 - \alpha z \quad (\alpha = 0.0065\text{ K/m}, \quad T_0 = 288.15\text{ K}) $$
  $$ p(z) = p_0 \left(1 - \frac{\alpha z}{T_0}\right)^{\frac{g}{\alpha R}}, \quad \frac{g}{\alpha R} \approx 5.256 $$

---

## ⚡ 3. Forces on Gates and Submerged Surfaces (unit 05: Hydrostatics)

### Inclined Plane Surface ($\theta$ with the horizontal)
* **Resultant Force:**
  $$ F_R = p_{CG} \cdot A = (\rho g h_{CG}) \cdot A = \rho g \sin\theta \, y_{CG} \cdot A $$
* **Center of Pressure ($y_{CP}$ along the plane):**
  $$ y_{CP} = y_{CG} + \frac{I_{xx,CG}}{y_{CG} \cdot A} $$
  *Rectangle ($b \times L$):* $I_{xx,CG} = \frac{b L^3}{12}$  
  *Circle ($R$):* $I_{xx,CG} = \frac{\pi R^4}{4}$

### Curved Surface
* **Horizontal Component:** $F_H = p_{CG,v} \cdot A_v$ (projection onto a vertical plane).
* **Vertical Component:** $F_V = \rho g \cdot V_{\text{fluid above the surface}}$.
* **Resultant:** $F_R = \sqrt{F_H^2 + F_V^2}, \quad \tan\alpha = F_V / F_H$.

---

## ⚡ 4. Buoyancy and Stability (Archimedes) (unit 05: Hydrostatics)
* **Buoyant force:** $E = \rho_{\text{fluid}} g V_{\text{submerged}}$ (acts at the Center of Buoyancy $C$).
* **Metacentric Radius:** $\overline{CM} = \frac{I_{0}}{V_{\text{submerged}}}$ ($I_0$ second moment of area of the waterplane).
* **Metacentric Height:** $\overline{GM} = \overline{CM} - \overline{CG}$.
  * $\overline{GM} > 0 \implies$ **Stable Equilibrium** (restoring couple).
  * $\overline{GM} < 0 \implies$ **Unstable** (capsize / overturning).
