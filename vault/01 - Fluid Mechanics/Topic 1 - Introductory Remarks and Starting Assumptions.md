---
materia: Fluid Mechanics
tema: "Topic 1: Introductory Remarks and Starting Assumptions"
fuentes:
  - "Notes.pdf (Sánchez & Rodríguez-Rodríguez, UC3M), Chapter 1, pp. 1-8"
  - "slides_Chapters1-2.pdf, Slides 1.0 to 1.8"
tags:
  - moc-topic
  - fluid-mechanics
  - second-year
dificultad: low
---

# 🌊 Topic 1: Introductory Remarks and Starting Assumptions

> **Topic objective:** Establish the physical and mathematical foundations that allow a fluid (composed of discrete particles in random motion) to be treated as a macroscopic **continuum**, rigorously defining the fluid particle, the density, velocity and internal energy fields, the local thermodynamic equilibrium hypothesis (Knudsen) and the equations of state for perfect liquids and gases.

---

## 📑 Theoretical Contents of the Chapter

1. **Solids, Liquids and Gases:**
   * Fundamental mechanical distinction: solids respond with a deformation proportional to the force ($\tau \propto d\theta$); fluids respond with continuous deformation at a rate proportional to the shear stress ($\tau \propto \frac{d\theta}{dt}$).
   * Liquids vs Gases: density ($\rho_l \gg \rho_g$) and compressibility $(\partial \rho/\partial p)_{T,l} \ll (\partial \rho/\partial p)_{T,g}$.
   * Microscopic structure: intermolecular force curve $F(d)$ with equilibrium distance $d_0 \approx 3\text{ \AA}$. Mean intermolecular distance $d = (W/\rho N_A)^{1/3}$ ($d_{\text{air}} \approx 3.4\text{ nm} \sim 10 d_0$; $d_{\text{water}} \approx 0.31\text{ nm} \sim d_0$).
2. **The Fluid as a Continuum and the Fluid Particle:**
   * The macroscopic scale $L$ (distance over which significant flow variations are appreciable).
   * Definition of the fluid particle ($\delta V$): double-bounding condition $d \ll (\delta V)^{1/3} \ll L$ (Notes.pdf, Eq. 1.2).
   * The density plateau: independence of the density with respect to the elementary volume.
   * Limit of applicability of the continuum: $d/L \ll 1$. Limiting cases: space re-entry in the upper atmosphere and micro/nanofluidics (MEMS).
3. **Definition of Macroscopic Fields:**
   * Density: $\rho(\vec{x}, t) = \lim_{\delta V \to 0, (\delta V)^{1/3} \gg d} \frac{\sum m_i}{\delta V}$ (Eq. 1.3).
   * Flow velocity: $\vec{v}(\vec{x}, t) = \lim \frac{\sum m_i \vec{v}_i}{\sum m_i}$ (center-of-mass velocity, Eq. 1.4).
   * Decomposition of the total energy: $\lim \frac{\sum E_i}{\sum m_i} = e + \frac{|\vec{v}|^2}{2}$ (Eq. 1.5).
   * Internal energy: $e = \lim \frac{\sum m_i |\vec{v}_i - \vec{v}|^2/2 + E_{vi} + E_{ri} + \cdots}{\sum m_i}$ (disordered thermal agitation + internal modes, basis of the temperature $T$, Eq. 1.6).
4. **Local Thermodynamic Equilibrium (LTE):**
   * Restoring mechanism: molecular collisions in gases.
   * Mean free path $\lambda/d \simeq (d/d_0)^2$ ($\lambda \approx 0.4\ \mu\text{m}$ in air at sea level).
   * Time between collisions $\tau = \lambda/a \approx 10^{-9}\text{ s}$.
   * Knudsen criterion: $Kn = \frac{\lambda}{L} \ll 1$ (Eq. 1.7) and $T_{\text{macro}} \gg \tau$.
   * $Kn \ll 1$ is more restrictive than the continuum criterion ($d/L \ll 1$) because in gases $\lambda \gg d$.
5. **Thermodynamic Variables and Equations of State:**
   * Gibbs relation: $de = T ds - p d(1/\rho) = T ds + \frac{p}{\rho^2} d\rho$ (Eq. 1.8).
   * Thermodynamic definitions: $T = (\partial e/\partial s)_\rho$, $p = -(\partial e/\partial \rho^{-1})_s$, enthalpy $h = e + p/\rho$.
   * **Perfect Liquid:** $\rho = \rho_0 = \text{const}$, $e = c T + e_0$, $h = c T + e_0 + p/\rho_0$, $s = c \ln T + s_0$ (Eqs. 1.11 to 1.14).
   * **Perfect Gas:** $p/\rho = R_g T$, $R_g = R_0/W$, $e = c_v T + e_0$, $h = c_p T + e_0$, $s = c_v \ln(p/\rho^\gamma) + s_0$, $c_p = c_v + R_g$, $\gamma = 1.4$ for air (Eqs. 1.15 to 1.18).

---

## 🔗 Detailed Conceptual Note
* [[01 - Fluid Mechanics/Concept - Continuum Hypothesis and Thermophysical Properties|See the Exhaustive Theory Note for Topic 1]]
