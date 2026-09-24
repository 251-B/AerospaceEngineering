---
materia: "Aerospace Materials I"
tema: "Tema 1: Bonding in Solids"
origen: "Session 2 T1 Bonding_2025.pdf, Slide 39, Question 3"
dificultad: media
tags:
  - problema-examen
  - resuelto
  - young-modulus
  - ionic-bonding
  - metallic-bonding
  - mgo
  - magnesium
---

# ✏️ Problema: Cuestión 3 Examen T1 — Módulo de Elasticidad MgO vs Mg

## 📄 Enunciado Oficial [Slide 39]
> **Would you expect MgO or magnesium to have the higher modulus of elasticity? Explain.**

---

## 📊 1. Fase 1: Planteamiento Físico, Hipótesis y Datos

### Contexto y Datos de Ingeniería:
We are asked to compare the elastic modulus (Young's modulus $E$) of Magnesium Oxide ($\text{MgO}$) with that of pure metallic Magnesium ($\text{Mg}$).

| Material | Chemical Nature | Bonding Type | Experimental Young's Modulus ($E$) | Melting Temp ($T_m$) |
| :--- | :--- | :--- | :--- | :--- |
| **Magnesium ($\text{Mg}$)** | Pure elemental metal ($Z=12$) | **Metallic** (delocalized electron sea) | **$\approx 45\text{ GPa}$** | $650^\circ\text{C}$ ($923\text{ K}$) |
| **Magnesium Oxide ($\text{MgO}$)** | Refractory ceramic compound | **Predominantly Ionic** ($\text{Mg}^{2+}\text{O}^{2-}$) | **$\approx 250\text{--}300\text{ GPa}$** | $2852^\circ\text{C}$ ($3125\text{ K}$) |

### Hipótesis de Partida:
1. Young's modulus reflects the microscopic bond stiffness $S_0 = (d^2E/dr^2)_{r_0}$ resisting elastic displacement of atoms from equilibrium.
2. In metallic $\text{Mg}$, cohesive forces are governed by electrostatic attraction between divalent $\text{Mg}^{2+}$ cations and a smeared-out conduction electron gas.
3. In $\text{MgO}$, cohesive forces are governed by direct, localized Coulombic attraction between compact divalent cations ($\text{Mg}^{2+}$) and anions ($\text{O}^{2-}$).

---

## 🧠 2. Fase 2: Formulación Fundamental y Justificación Teórica

### Justificación Teórica Previa:
To determine which material exhibits the higher modulus of elasticity, we link macroscopic stiffness to the second derivative of the interatomic potential energy at equilibrium [Slides 8, 10, 13]:

$$E_{\text{Young}} = \frac{1}{r_0}\left.\frac{d^2 E_{\text{net}}}{dr^2}\right|_{r = r_0} = \frac{1}{r_0}\left.\frac{dF_{\text{net}}}{dr}\right|_{r = r_0}$$

For an ionic crystal lattice, the attractive potential energy per ion pair is given by Coulomb's law incorporating the Madelung constant $A$ [Slide 9]:

$$E_{\text{att}}(r) = -\frac{A\,Z_1 Z_2 e^2}{4\pi\varepsilon_0 r}$$

Differentiating twice to evaluate curvature:

$$\frac{dE_{\text{att}}}{dr} = \frac{A\,Z_1 Z_2 e^2}{4\pi\varepsilon_0 r^2}$$

$$\left.\frac{d^2 E_{\text{att}}}{dr^2}\right|_{r = r_0} = -\frac{2 A\,Z_1 Z_2 e^2}{4\pi\varepsilon_0 r_0^3}$$

Including the Born repulsive term ($E_{\text{rep}} = B/r^n$ where $n \approx 7$), the net equilibrium curvature is proportional to:

$$\left.\frac{d^2 E_{\text{net}}}{dr^2}\right|_{r_0} = \frac{(n - 1) A\,Z_1 Z_2 e^2}{4\pi\varepsilon_0 r_0^3}$$

Hence, the elastic modulus scales as:

$$E_{\text{Young}} \propto \frac{Z_1 Z_2 e^2}{r_0^4}$$

---

## 🔢 3. Fase 3: Deducción y Comparación Paso a Paso

### Paso 1: Análisis del Enlace en Óxido de Magnesio ($\text{MgO}$) [Slides 10-13]
1. **Divalent Ionic Charges:** In $\text{MgO}$, Magnesium transfers two valence electrons to Oxygen:
   $$\text{Mg} \to \text{Mg}^{2+} + 2e^-, \quad \text{O} + 2e^- \to \text{O}^{2-}$$
   Thus, $Z_1 = +2$ and $Z_2 = -2$, resulting in a charge product of:
   $$Z_1 Z_2 = (+2)(-2) = 4$$
2. **Compact Interatomic Spacing:** The ionic radius of $\text{Mg}^{2+}$ is $r_{c+} \approx 0.072\text{ nm}$ and of $\text{O}^{2-}$ is $r_{a-} \approx 0.140\text{ nm}$, yielding an interionic distance of:
   $$a_0 = r_{c+} + r_{a-} \approx 0.212\text{ nm} \quad (2.10\text{ \AA} \text{ [Slide 11]})$$
3. **Curvature and Energy:** Because $Z_1 Z_2 = 4$ and $a_0$ is small, the Coulombic attraction is exceptionally strong, resulting in an immense lattice energy ($|U| \approx 3790\text{ kJ/mol}$) and a very steep, deeply carved potential well with an extremely high second derivative $\left.\frac{d^2E}{dr^2}\right|_{a_0}$.

### Paso 2: Análisis del Enlace en Magnesio Metálico ($\text{Mg}$) [Slides 23-25]
1. **Delocalized Electron Gas:** Pure metallic Magnesium forms an HCP crystal lattice where each $\text{Mg}$ atom donates its two $3s^2$ valence electrons to a shared electron gas.
2. **Screening and Spacing:** The negative charge of the valence electrons is not concentrated on compact anions; it is spread diffusely throughout the interstitial volume. Furthermore, the metallic interatomic distance in $\text{Mg}$ is larger ($r_0 \approx 0.320\text{ nm}$).
3. **Resulting Curvature:** Because the electron cloud is smeared and dynamic, stretching the bonds produces a much smaller restorative force per unit displacement than pulling against localized divalent point charges. The potential well is much shallower ($E_b \approx 146\text{ kJ/mol}$, $T_m = 650^\circ\text{C}$) and broader.

### Paso 3: Conclusión Directa
Comparing the two materials:
$$\left.\frac{d^2 E}{dr^2}\right|_{r_0, \text{MgO}} \gg \left.\frac{d^2 E}{dr^2}\right|_{r_0, \text{Mg}} \implies \mathbf{E_{\text{MgO}} \gg E_{\text{Mg}}}$$

---

## 🎯 4. Fase 4: Interpretación Física y Sentido Tecnológico

* **Definitive Answer:** **$\text{MgO}$ has a much higher modulus of elasticity than pure magnesium** (experimentally, $E_{\text{MgO}} \approx 250\text{--}300\text{ GPa}$ versus $E_{\text{Mg}} \approx 45\text{ GPa}$, a factor of nearly **$6\times$** greater).
* **Physical Synthesis:** In $\text{MgO}$, the extremely intense localized electrostatic forces between divalent $\text{Mg}^{2+}$ and $\text{O}^{2-}$ ions create a remarkably stiff atomic spring constant. In metallic $\text{Mg}$, the delocalized electron gas provides far lower resistance to elastic bond stretching.
* **Aerospace Application Note:** While $\text{MgO}$ possesses superior stiffness and refractoriness ($T_m = 2852^\circ\text{C}$), its ionic brittleness precludes its use as a primary monolithic structural airframe metal. Instead, Magnesium alloys are favored for lightweight airframe casings due to their ductility, while oxide ceramics are employed as thermal barrier coatings and structural reinforcements.

---
*Retorno:* `[[Tema 1 - Bonding in Solids and Material Properties|⬅️ Volver a Tema 1]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
