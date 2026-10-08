---
materia: Fluid Mechanics
tema: "Topic 1: Fluid Properties and Fundamentals"
fuentes:
  - "Notes.pdf (Sánchez & Rodríguez-Rodríguez, UC3M), Chapter 1, pp. 1-8"
  - "slides_Chapters1-2.pdf, Slides 1.0 to 1.8"
tags:
  - theory
  - continuum
  - thermophysics
  - fluid-particle
  - lte
  - knudsen
dificultad: medium
prerrequisitos: []
---

# 📖 Continuum Hypothesis, Fluid Particle and Thermophysics

> **Key idea (Sánchez and Rodríguez-Rodríguez):** Matter in a fluid is discretely distributed at the molecular level. The continuum hypothesis makes it possible to define an intermediate range of scales where the fluid properties can be described as continuous functions of space $\vec{x}$ and time $t$ through the concept of the **fluid particle**.

---

## 🎯 1. Microscopic and Macroscopic Differences: Solids, Liquids and Gases

*[Source: Notes.pdf §1, p. 1; Slides 1.0 - 1.2]*

### Response to External Stresses
* **Solids:** Under a small external force they respond with a finite deformation. The internal force that counteracts the external action is proportional to the **deformation**:
  $$ \tau \propto d\theta $$
* **Fluids (Liquids and Gases):** They deform continuously under the action of tangential stresses however small. The resisting internal force is proportional to the **rate of deformation**:
  $$ \tau \propto \frac{d\theta}{dt} $$
  As a direct consequence, fluids have no shape of their own and adapt to that of the container.

### Liquids vs. Gases
* **Density:** $\rho_{\text{liquid}} \gg \rho_{\text{gas}}$. Accelerating a liquid requires much larger forces than accelerating a gas.
* **Compressibility:** The density variation under isothermal overpressures is orders of magnitude smaller in liquids than in gases:
  $$ \left(\frac{\partial \rho}{\partial p}\right)_{T,\text{liquid}} \ll \left(\frac{\partial \rho}{\partial p}\right)_{T,\text{gas}} \quad \text{(Notes.pdf, Eq. 1.1)} $$

### Microscopic Origin and Intermolecular Distance ($d$)
The intermolecular force $F(d)$ exhibits repulsion at very short distances and attraction for $d > d_0$, with a stable equilibrium at the characteristic molecular scale:
$$ d_0 \sim 3 \times 10^{-10}\text{ m} = 3\text{ \AA} $$

With the density $\rho$, the molar mass $W$ and Avogadro's number $N_A = 6.022 \times 10^{23}\text{ molecules/mol}$, the mean intermolecular distance $d$ is obtained by equating the mass of one molecule to the volume it occupies, $d^3$:
$$ \rho = \frac{W / N_A}{d^3} \implies \mathbf{d = \left(\frac{W}{\rho N_A}\right)^{1/3}} $$

| Quantity | Air (Gas at sea level) | Water (Liquid) |
| :--- | :--- | :--- |
| **Density ($\rho$)** | $1.2\text{ kg/m}^3$ | $1000\text{ kg/m}^3$ |
| **Molar mass ($W$)** | $28.96\text{ g/mol}$ | $18.02\text{ g/mol}$ |
| **Intermolecular distance ($d$)** | $\mathbf{\approx 3.4 \times 10^{-9}\text{ m}} \approx 10\,d_0$ | $\mathbf{\approx 3.1 \times 10^{-10}\text{ m}} \approx d_0$ |
| **Molecules in $1\text{ mm}^3$** | $\sim 10^{16}\text{ molecules}$ | $\sim 10^{19}\text{ molecules}$ |
| **Molecular interaction** | Fly freely; binary collisions | Packed; permanent cohesive forces |

---

## 🔬 2. The Continuum Hypothesis and the Fluid Particle

*[Source: Notes.pdf §1, pp. 3-5; Slides 1.3 - 1.4]*

Instead of solving Newton's laws for $\sim 10^{16}$ molecules/mm³ (computationally unattainable), we introduce the concept of the **Fluid Particle**.

### Macroscopic Scale ($L$)
This is the characteristic distance over which significant variations in the macroscopic flow properties occur (example: in a room, $L \sim 10\text{ cm}$; on an airfoil, $L \sim \text{chord}$).

### Definition of the Fluid Particle ($\delta V$)
It is a differential volume centred at position $\vec{x}$ at time $t$ that must strictly satisfy the **double-bounding condition**:
$$ \mathbf{d \ll (\delta V)^{1/3} \ll L} \quad \text{(Notes.pdf, Eq. 1.2)} $$

1. $(\delta V)^{1/3} \gg d$: It must contain an immense number of molecules to average out the molecular statistical fluctuations and reach the **density plateau**.
2. $(\delta V)^{1/3} \ll L$: It must be infinitesimal compared with the spatial variations of the flow so that it can be treated as a differential material point at $\vec{x}$.

```text
  Apparent density
  ∑ mi / δV
       ^
       |   Discrete molecular
       |   fluctuations (jumps)        CONTINUOUS PLATEAU
       |      _/\_/\_              =============================       Macroscopic spatial
       |     /       \                                          \      variations of the flow
       |____/_________\__________________________________________\___________________________>
           0          d                (δV)^1/3                   L               Size (δV)^1/3
```

### Limit of Applicability
The continuum is rigorously valid if:
$$ \frac{d}{L} \ll 1 $$
It fails in:
* Rarefied flows in the upper atmosphere (re-entry of satellites or shuttles at $h > 100\text{ km}$, where $d \sim L$).
* Micro- and nanofluidics (MEMS) where the conduits are comparable to the molecular scale.

---

## 📐 3. Definition of Macroscopic Field Variables

*[Source: Notes.pdf §1, pp. 5-6; Slides 1.5]*

From the fluid particle $\delta V$, we define the continuous fields:

### 1. Density Field ($\rho$)
$$ \rho(\vec{x}, t) = \lim_{\delta V \to 0, \, (\delta V)^{1/3} \gg d} \frac{\sum m_i}{\delta V} \quad \left[\frac{\text{kg}}{\text{m}^3}\right] \quad \text{(Eq. 1.3)} $$

### 2. Flow Velocity Field ($\vec{v}$)
It is the velocity of the center of mass of the molecules contained in the fluid particle:
$$ \vec{v}(\vec{x}, t) = \lim_{\delta V \to 0} \frac{\sum m_i \vec{v}_i}{\sum m_i} \quad \left[\frac{\text{m}}{\text{s}}\right] \quad \text{(Eq. 1.4)} $$

### 3. Internal Energy ($e$) and Total Energy
The energy per unit total mass inside $\delta V$ decomposes exactly into the macroscopic kinetic energy of the flow and the thermal internal energy:
$$ \lim_{\delta V \to 0} \frac{\sum E_i}{\sum m_i} = e + \frac{|\vec{v}|^2}{2} \quad \text{(Eq. 1.5)} $$
where $e$ represents the **internal energy** (disordered thermal motion relative to the center of mass plus intramolecular energies):
$$ \mathbf{e = \lim_{\delta V \to 0} \frac{\sum m_i \frac{|\vec{v}_i - \vec{v}|^2}{2} + E_{v,i} + E_{r,i} + \cdots}{\sum m_i}} \quad \text{(Eq. 1.6)} $$
* The term $\frac{|\vec{v}_i - \vec{v}|^2}{2}$ is the random molecular thermal agitation, the fundamental basis of the thermodynamic definition of **temperature ($T$)**.
* $E_{v,i}, E_{r,i}$ are the molecular vibrational and rotational energies.

---

## ⚡ 4. Local Thermodynamic Equilibrium (LTE) Hypothesis

*[Source: Notes.pdf §1, pp. 5-6; Slides 1.6]*

In Fluid Mechanics, systems change in space and time. However, an observer moving with the local fluid velocity $\vec{v}(\vec{x}, t)$ observes that the thermodynamic variables are related by the same **equations of state** as in classical equilibrium thermodynamics.

### Physical Restoring Mechanism: Molecular Collisions
In a gas, molecules exchange momentum and energy through continuous collisions.
* **Mean free path ($\lambda$):** Average distance between two successive collisions. Equating the volume swept by the molecule ($d_0^2 \lambda$) to the volume per molecule ($d^3$):
  $$ \frac{\lambda}{d} \simeq \left(\frac{d}{d_0}\right)^2 \implies \mathbf{\lambda \approx 4 \times 10^{-7}\text{ m}} = 0.4\ \mu\text{m} \quad \text{(in air at sea level)} $$
* **Characteristic time between collisions ($\tau$):** With $a \approx \sqrt{\gamma R T}$ the speed of sound:
  $$ \tau = \frac{\lambda}{a} \approx \frac{4 \times 10^{-7}\text{ m}}{340\text{ m/s}} \approx \mathbf{10^{-9}\text{ s}} = 1\text{ ns} $$

### Knudsen Number Criterion ($Kn$)
For a molecule to experience thousands of collisions before reaching regions with different macroscopic properties, the following must hold:
$$ \mathbf{Kn = \frac{\lambda}{L} \ll 1} \quad \text{(Notes.pdf, Eq. 1.7)} $$
For unsteady flows with macroscopic characteristic time $T_{\text{macro}}$:
$$ T_{\text{macro}} \gg \tau \approx 10^{-9}\text{ s} $$

> [!IMPORTANT] Academic Rigor
> The LTE criterion ($Kn = \lambda/L \ll 1$) is **more restrictive** than the continuum criterion ($d/L \ll 1$), since for gases the mean free path is orders of magnitude larger than the intermolecular distance: $\lambda \approx 400\text{ nm} \gg d \approx 3.4\text{ nm}$.

---

## 📊 5. Equations of State: Perfect Liquid and Perfect Gas Models

*[Source: Notes.pdf §1, pp. 6-7; Slides 1.7 - 1.8]*

Under LTE, the fundamental Gibbs thermodynamic relation governs the fluid particle:
$$ de = T ds - p \, d\left(\frac{1}{\rho}\right) = T ds + \frac{p}{\rho^2} d\rho \quad \text{(Eq. 1.8)} $$
From it follow:
$$ T = \left(\frac{\partial e}{\partial s}\right)_\rho \quad \text{(Eq. 1.9)}, \qquad p = -\left(\frac{\partial e}{\partial \rho^{-1}}\right)_s \quad \text{(Eq. 1.10)}, \qquad h = e + \frac{p}{\rho} $$

### 1. Perfect Liquid Model (Incompressible)
Constant density $\rho_0$ and constant specific heat $c$:
$$ \mathbf{\rho = \rho_0} \quad \text{(Eq. 1.11)} $$
$$ \mathbf{e = c T + e_0} \quad \text{(Eq. 1.12)} $$
$$ \mathbf{h = c T + e_0 + \frac{p}{\rho_0}} \quad \text{(Eq. 1.13)} $$
$$ \mathbf{s = c \ln T + s_0} \quad \text{(Eq. 1.14)} $$
*(For water: $\rho_0 = 1000\text{ kg/m}^3$, $c = 4180\text{ J/(kg}\cdot\text{K)}$)*.

### 2. Perfect Gas Model (Calorically Perfect)
$$ \mathbf{\frac{p}{\rho} = R_g T} \quad \text{(Eq. 1.15)}, \quad R_g = \frac{R_0}{W} $$
$$ \mathbf{e = c_v T + e_0} \quad \text{(Eq. 1.16)} $$
$$ \mathbf{h = c_p T + e_0} \quad \text{(Eq. 1.17)} $$
$$ \mathbf{s = c_v \ln\left(\frac{p}{\rho^\gamma}\right) + s_0} \quad \text{(Eq. 1.18)} $$

* Universal constant: $R_0 = 8.314\text{ J/(mol}\cdot\text{K)}$.
* Mayer's relation: $c_p = c_v + R_g$.
* Adiabatic index: $\gamma = c_p/c_v$. For diatomic gases (air, $N_2, O_2$): $\mathbf{\gamma = 7/5 = 1.4}$.
* For standard air:
  $$ R_g = 287\text{ J/(kg}\cdot\text{K)}, \quad c_v = 717\text{ J/(kg}\cdot\text{K)}, \quad c_p = 1004\text{ J/(kg}\cdot\text{K)} $$

---

## 🔗 Internal Links
* [[01 - Fluid Mechanics/Topic 1 - Introductory Remarks and Starting Assumptions|⬅️ Back to the Topic 1 Index]]
* [[01 - Fluid Mechanics/Concept - Viscosity and Newton's Law of Viscosity|➡️ Next: Viscosity and Newton's Law]]
