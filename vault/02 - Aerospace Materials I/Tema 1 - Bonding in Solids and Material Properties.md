---
materia: "Aerospace Materials I"
tema: "Tema 1: Bonding in Solids"
fuentes: "Session 2 T1 Bonding_2025.pdf, Slides 1-39"
tags:
  - teoria
  - moc-tema
  - bonding
  - crystal-physics
dificultad: media
prerrequisitos: []
---

# 🌐 Tema 1: Bonding in Solids and Material Properties

> **Core Idea:** Macroscopic engineering properties of materials (melting temperature $T_m$, stiffness/elastic modulus $E$, thermal expansion coefficient $\alpha$, hardness, and ductility) are fundamentally governed by the nature and strength of interatomic bonds, the geometry of atomic coordination, and the shape of the interatomic potential energy well $E(r)$.

---

## 🏛️ 1. The Materials Science & Engineering Tetrahedron

Materials science investigates the central relationship between four fundamental vertices [Slide 2]:

```
               Processing / Synthesis
                      /\
                     /  \
                    /    \
                   /  🧪  \
                  /________\
     Structure &            Properties
     Atomic Bonding         (Mechanical, Thermal, Electrical)
            \                  /
             \                /
              \      🚀      /
               \            /
                Applications & Performance
```

* **Atomic Bonding & Structure:** The primary and secondary electronic configurations determine whether atoms form close-packed metallic arrays, rigid directional networks, or ionic lattices.
* **Properties:** Derived directly from the depth $E_0$, curvature $d^2E/dr^2$, and asymmetry of the potential energy well.
* **Processing:** Thermomechanical treatments, solid-state diffusion, casting, and sintering modify microstructures and defect populations.
* **Applications:** Structural integrity in aeronautical turbines, airframes, thermal protection systems, and avionics.

$$\text{Nature of Bonding} \longleftrightarrow \text{Crystal Structure} \longleftrightarrow \text{Properties} \longleftrightarrow \text{Processing \& Applications}$$

---

## ⚡ 2. Primary Atomic Bonds (Strong: $100\text{--}1500\text{ kJ/mol}$)

Primary bonds involve valence electron transfer, sharing, or delocalization to attain stable noble gas electronic configurations [Slide 29]:

| Bond Type | Mechanism | Directionality | Typical Bond Energy | Representative Materials |
| :--- | :--- | :--- | :--- | :--- |
| **Ionic** | Complete valence $e^-$ transfer (metal $\to$ non-metal), creating cation-anion electrostatic attraction | **Non-directional** | $150\text{--}370\text{ kcal/mol}$ ($628\text{--}1548\text{ kJ/mol}$) | $\text{NaCl}, \text{Al}_2\text{O}_3, \text{ZrO}_2, \text{MgO}$ |
| **Covalent** | Localized orbital overlap and sharing of outer $s$ and $p$ electron pairs | **Highly directional** | $125\text{--}300\text{ kcal/mol}$ ($523\text{--}1255\text{ kJ/mol}$) | $\text{Diamond}, \text{Si}, \text{SiO}_2, \text{SiC}, \text{BN}$ |
| **Metallic** | Delocalization of valence electrons into an "electron sea" surrounding positive ion cores | **Non-directional** | $25\text{--}200\text{ kcal/mol}$ ($105\text{--}837\text{ kJ/mol}$) | $\text{Ti}, \text{Al}, \text{Fe}, \text{Ni}, \text{Cu}$ |

* Detailed study: `[[Concepto - Enlace Ionico y Energia Reticular de Born-Lande]]`
* Detailed study: `[[Concepto - Enlace Covalente y Caracter Polar]]`
* Detailed study: `[[Concepto - Enlace Metalico y Teoria de Bandas de Energia]]`

---

## 🧲 3. Secondary Bonds & Intermolecular Forces (Weak: $< 40\text{ kJ/mol}$)

Secondary bonds arise from dipole-dipole attractions caused by spatial asymmetries in electronic charge distribution [Slides 29-35]:

1. **Permanent Dipoles ($1\text{--}10\text{ kcal/mol} \approx 4\text{--}42\text{ kJ/mol}$):**
   * Exist in asymmetrical polar molecules possessing permanent dipole moments ($\mu = Q \times d$).
   * *Example:* Chloromethane ($\text{CH}_3\text{Cl}$) vs non-polar methane ($\text{CH}_4$).
   * *Aeronautical/Polymeric impact:* In polyvinyl chloride (PVC), partial charges ($\text{Cl}^{\delta-} \cdots \text{H}^{\delta+}$) provide inter-chain cross-linking, significantly increasing macroscopic stiffness.
2. **Hydrogen Bonds ($\approx 7\text{ kcal/mol} \approx 29\text{ kJ/mol}$):**
   * Extreme dipole interaction where hydrogen is bonded to strongly electronegative, small atoms ($\text{F}, \text{O}, \text{N}$).
   * Explains anomalous melting/boiling points in $\text{H}_2\text{O}, \text{HF}, \text{NH}_3$ relative to period 3-5 hydrides.
3. **Fluctuating Dipoles / London Dispersion ($< 2\text{ kcal/mol} \approx 8.4\text{ kJ/mol}$):**
   * Universal instantaneous quantum fluctuations of electron density inducing transient dipoles in neighboring atoms.
   * Enables solidification of noble gases and non-polar polymers (e.g., polyethylene).

* Detailed study: `[[Concepto - Fuerzas Intermoleculares y Enlaces Secundarios]]`

---

## 📈 4. The Interatomic Potential Well & Macroscopic Engineering Properties

All macroscopic mechanical and thermal constants trace directly back to the potential energy function $E(r)$ [Slides 7-13, 20-21]:

$$E_{\text{net}}(r) = E_{\text{att}}(r) + E_{\text{rep}}(r) = -\frac{A}{r^m} + \frac{B}{r^n} \quad (n > m)$$

* **Equilibrium Distance ($r_0$):** Interatomic spacing where attractive and repulsive forces cancel ($F(r_0) = 0$).
* **Melting Point ($T_m$):** Proportional to well depth / binding energy $E_0$. Deeper well $\implies$ higher thermal energy required to disrupt lattice $\implies$ higher $T_m$.
* **Elastic / Young's Modulus ($E$):** Governed by the curvature at the minimum:
  $$E \propto \left.\frac{d^2 E}{dr^2}\right|_{r = r_0} = \left.\frac{dF}{dr}\right|_{r = r_0}$$
  A narrower, steeper well yields a larger curvature and higher resistance to elastic strain.
* **Thermal Expansion Coefficient ($\alpha$):** Governed by the **asymmetry (anharmonicity)** of the potential well. Thermal excitation causes non-symmetric vibrational excursions, shifting the mean atomic position $\bar{r}(T)$ outwards. Deep, symmetric wells exhibit low $\alpha$.

* Detailed study: `[[Concepto - Curvas de Energia Potencial Interatomica y Propiedades Macroscopicas]]`

---

## 📊 5. Summary Table: Material Classes vs Bonding Characteristics

According to UC3M official classification [Slides 37-38]:

| Material Class | Dominant Bonding | Melting / Boiling Point | Mechanical Behavior | Electrical & Thermal Conductivity | Examples |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Metals & Alloys** | Metallic (electron sea) | Moderate to High | Ductile, malleable, plastic flow via dislocation glide | Excellent conductors (free electrons) | Steels, Ti-alloys, Al-alloys, Inconel |
| **Ceramics & Glasses** | Ionic and/or Covalent network | Very High | Hard, brittle, high stiffness, low fracture toughness | Insulators / semiconductors (molten ionic: ionic conduction) | Alumina ($\text{Al}_2\text{O}_3$), Silica ($\text{SiO}_2$), $\text{SiC}, \text{ZrO}_2$ |
| **Network Covalent Solids** | Continuous Covalent lattice | Extremely High | Diamond-hard, brittle, completely insoluble | Electrical insulators (graphite is an anisotropic conductor) | Diamond, cubic $\text{BN}$, quartz |
| **Polymers** | Covalent (backbone) + Secondary (inter-chain) | Low to Moderate | Viscoelastic, compliant, flexible to rigid | Thermal and electrical insulators | Polyethylene (PE), PVC, Epoxy resins |

---

## 📚 6. Map of Concepts & Solved Exam Problems

### 🧠 Atomic Concept Notes
1. `[[Concepto - Enlace Ionico y Energia Reticular de Born-Lande]]` — Born-Landé formulation, Madelung constant, Born-Haber thermochemical cycle, and ionic crystal properties.
2. `[[Concepto - Enlace Covalente y Caracter Polar]]` — Orbital hybridization, tetrahedral coordination ($109.5^\circ$), Hannay-Smyth ionic percentage, and network solids.
3. `[[Concepto - Enlace Metalico y Teoria de Bandas de Energia]]` — Delocalized electron sea, valence dependence, ductility mechanisms, and band structure overlap.
4. `[[Concepto - Fuerzas Intermoleculares y Enlaces Secundarios]]` — Permanent dipoles, PVC stiffness, hydrogen bonding anomaly, and London dispersion forces.
5. `[[Concepto - Curvas de Energia Potencial Interatomica y Propiedades Macroscopicas]]` — Potential well geometry, curvature, anharmonic thermal expansion, and Young's modulus.

### ✏️ Official Exam Questions (UC3M Slide 39)
* `[[Problema - Cuestion 1 Examen T1 Enlace Metalico vs Covalente]]` — Comparative analysis: nature of bond, valence electron participation, and microscopic origin of ductility.
* `[[Problema - Cuestion 2 Examen T1 Curvas de Potencial Titanio vs Aluminio]]` — Schematic derivation and comparative plotting of $E(r)$ curves for Ti vs Al ($E, \alpha, T_m$).
* `[[Problema - Cuestion 3 Examen T1 Modulo de Elasticidad MgO vs Mg]]` — Physical deduction of elastic modulus disparity between divalent ionic ceramic ($\text{MgO}$) and metallic magnesium ($\text{Mg}$).
* `[[Problema - Cuestion 4 Examen T1 Modulo de Elasticidad Aluminio vs Silicio]]` — Periodic trend analysis for adjacent Period 3 elements: Metallic Al (FCC) vs Directional Covalent Si (Diamond Cubic).

---
*Retorno:* `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|⬅️ Volver a Materiales Aeroespaciales I MOC]]` | `[[00 - Indice Central/Indice Maestro|🗺️ Índice Maestro]]`
