---
materia: "Aerospace Materials I"
tema: "Tema 1: Bonding in Solids"
origen: "Session 2 T1 Bonding_2025.pdf, Slide 39, Question 4"
dificultad: media
tags:
  - problema-examen
  - resuelto
  - young-modulus
  - aluminum
  - silicon
  - covalent-bonding
  - metallic-bonding
---

# ✏️ Problema: Cuestión 4 Examen T1 — Módulo de Elasticidad Aluminio vs Silicio

## 📄 Enunciado Oficial [Slide 39]
> **Aluminum and silicon are side-by-side in the periodic table. Which would you expect to have the higher modulus of elasticity (E)? Explain.**

---

## 📊 1. Fase 1: Planteamiento Físico, Hipótesis y Datos

### Contexto Periódico y Datos de Propiedades:
Aluminum ($\text{Al}$, atomic number $Z = 13$) and Silicon ($\text{Si}$, atomic number $Z = 14$) are adjacent elements in Period 3 of the periodic table, possessing nearly identical atomic weights ($M_{\text{Al}} = 26.98\text{ g/mol}$, $M_{\text{Si}} = 28.09\text{ g/mol}$) and very similar core electron configurations ($[\text{Ne}]$).

| Property | Aluminum ($\text{Al}$) | Silicon ($\text{Si}$) |
| :--- | :--- | :--- |
| **Periodic Position** | Period 3, Group 13 (Metal) | Period 3, Group 14 (Metalloid / Semiconductor) |
| **Valence Electron Configuration** | $3s^2 3p^1$ (3 valence $e^-$) | $3s^2 3p^2$ (4 valence $e^-$) |
| **Dominant Bonding Type** | **Metallic** (non-directional electron sea) | **Covalent** (directional $sp^3$ tetrahedral network) |
| **Crystal Structure** | Face-Centered Cubic (FCC) | Diamond Cubic (Tetrahedral coordination) |
| **Melting Temperature ($T_m$)** | $660^\circ\text{C}$ ($933\text{ K}$) | $1414^\circ\text{C}$ ($1687\text{ K}$) |
| **Young's Modulus ($E$)** | **$\approx 69\text{--}70\text{ GPa}$** | **$\approx 130\text{--}185\text{ GPa}$** (isotropic average $\approx 150\text{ GPa}$) |

### Hipótesis de Partida:
1. Young's modulus reflects the macroscopic resistance to elastic deformation, determined by the second derivative of the interatomic potential energy curve at equilibrium:
   $$E \propto \left.\frac{d^2 E}{dr^2}\right|_{r = r_0}$$
2. The fundamental difference between $\text{Al}$ and $\text{Si}$ arises not from mass or atomic size, but from the **nature and directionality of their primary chemical bonds** [Slides 17-18, 23-25].

---

## 🧠 2. Fase 2: Formulación Fundamental y Justificación Teórica

### Justificación Teórica Previa:
To explain why two side-by-side elements have vastly different elastic moduli, we examine how applied macroscopic stress deforms metallic versus covalent bonds:

1. **Metallic Bonding in Aluminum ($\text{Al}$):**
   * Aluminum sheds its 3 valence electrons ($3s^2 3p^1$) into a shared conduction sea.
   * Because the electron sea is **non-directional and homogeneous**, elastic strain merely stretches the average radial distance between positive $\text{Al}^{3+}$ ion cores. The electrons adjust smoothly without any angular restoring force.
2. **Covalent Network Bonding in Silicon ($\text{Si}$):**
   * Silicon forms four localized $sp^3$ hybridized orbitals directed toward the vertices of a tetrahedron with fixed angles of $\theta_0 = 109.5^\circ$ [Slide 18].
   * The cohesive potential energy of the silicon diamond-cubic network depends not only on the bond length separation $r$, but also on the angular orientation $\theta$ between adjacent bonds (Keating/Tersoff potential model):
     $$E_{\text{total}} = \sum_{\text{bonds}} E_{\text{stretch}}(r) + \sum_{\text{angles}} E_{\text{bend}}(\theta)$$
   * Deforming a covalent network requires both **stretching the localized orbital overlap** and **bending the rigid hybrid bond angles**.

---

## 🔢 3. Fase 3: Deducción y Comparación Paso a Paso

### Paso 1: Comparación de la Fuerza del Enlace y Profundidad del Pozo ($E_0$) [Slides 10, 18, 24]
* In Silicon, each atom forms four localized, strong covalent bonds. The covalent bond dissociation energy $E(\text{Si}-\text{Si}) \approx 325\text{ kJ/mol}$, leading to an exceptionally high melting temperature ($T_m = 1414^\circ\text{C}$).
* In Aluminum, the metallic cohesive energy is approximately $326\text{ kJ/mol}$, but this energy is distributed over 12 nearest neighbors in the close-packed FCC lattice (cohesive energy per pairwise interaction $\approx 27\text{ kJ/mol}$). Consequently, Aluminum melts at $660^\circ\text{C}$, less than half the melting point of Silicon.
* Higher cohesive energy concentrated in directional bonds translates directly to a much deeper and steeper potential well for $\text{Si}$.

### Paso 2: Análisis de la Curvatura y Rigidez Angular [Slides 13, 18]
* When Silicon is strained, the rigid $sp^3$ orbital overlaps strongly resist angular distortion away from $109.5^\circ$. Bending the directional covalent bond introduces severe quantum mechanical electron-electron repulsion between adjacent orbital lobes:
  $$S_{\text{eff}} = \left.\frac{d^2 E}{dr^2}\right|_{\text{stretch}} + \frac{k_\theta}{r_0^2}\left.\frac{d^2 E}{d\theta^2}\right|_{\text{bend}}$$
* In Aluminum, there is **zero angular stiffness** ($k_\theta = 0$) because the metallic bond is non-directional. Resistance to elastic strain arises solely from isotropic electron density changes.
* Therefore, the effective atomic spring constant of Silicon is far greater than that of Aluminum:
  $$S_{0,\text{Si}} \gg S_{0,\text{Al}} \implies \left.\frac{d^2 E}{dr^2}\right|_{r_0, \text{Si}} \gg \left.\frac{d^2 E}{dr^2}\right|_{r_0, \text{Al}}$$

### Paso 3: Conclusión Directa
Substituting into the elastic modulus relation:
$$E_{\text{Si}} \propto \frac{1}{r_{0,\text{Si}}}\left.\frac{d^2 E}{dr^2}\right|_{r_0, \text{Si}} \quad > \quad E_{\text{Al}} \propto \frac{1}{r_{0,\text{Al}}}\left.\frac{d^2 E}{dr^2}\right|_{r_0, \text{Al}}$$
$$\mathbf{E_{\text{Si}} \gg E_{\text{Al}}}$$

---

## 🎯 4. Fase 4: Interpretación Física y Conclusiones Tecnológicas

* **Definitive Answer:** **Silicon has a significantly higher modulus of elasticity than Aluminum** (experimentally, $E_{\text{Si}} \approx 130\text{--}185\text{ GPa}$ versus $E_{\text{Al}} \approx 69\text{--}70\text{ GPa}$, more than **double** the stiffness).
* **Physical Summary:** While both elements reside side-by-side in Period 3 with comparable atomic weights and sizes, Silicon's rigid, directional $sp^3$ covalent network provides tremendous resistance to both bond stretching and bond bending. In contrast, Aluminum's non-directional metallic electron sea yields a much more compliant elastic response.
* **Engineering Trade-off:**
  * Aluminum's lower elastic modulus is compensated by its exceptional **ductility and toughness**, making it the premier aerospace structural alloy for airframe skins and ribs.
  * Silicon's extreme stiffness is accompanied by complete **room-temperature brittleness**, making monolithic silicon unsuitable for macroscopic structural airframe loads, but ideal for rigid, dimensionally stable micro-electro-mechanical systems (MEMS accelerometers and gyroscopes) in aerospace inertial navigation units.

---
*Retorno:* `[[Tema 1 - Bonding in Solids and Material Properties|⬅️ Volver a Tema 1]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
