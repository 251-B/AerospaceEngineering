---
materia: "Aerospace Materials I"
tema: "Topic 3: Diffusion in Solids and Mass Transport"
fuentes: "Session 5 T3  Difussion_2025.pdf, Slides 29-35"
tags:
  - theory
  - fundamental-concept
  - industrial-applications
  - carburizing
  - case-hardening
  - diffusion-bonding
  - sintering
  - rolls-royce-trent
dificultad: medium
prerrequisitos:
  - "[[Concept - Diffusion Mechanisms, Vacancies and Interstitials]]"
  - "[[Concept - Fick's Second Law, Non-Steady-State Diffusion and the Error Function]]"
---

# ⚙️ Concept: Carburizing and Industrial Applications of Diffusion

> **Technological Relevance:** Far from being a merely theoretical phenomenon, solid-state diffusion is the physical basis of the most advanced manufacturing processes in the mechanical, electronics and aerospace industries: from the surface hardening of transmission components to the manufacture of hollow titanium turbofan blades and integrated circuits on silicon wafers [Slides 29-34].

---

## 🏎️ 1. Carburizing and Surface Hardening (*Case Hardening*)

Gas carburizing is a thermochemical treatment that uses the **interstitial diffusion of carbon** to generate a graded surface hardness profile in low-carbon steels (e.g. AISI 1018, AISI 1010) [Slides 29-31]:

### 1.1 Metallurgical Principle
1. **Reactive Atmosphere:** The steel part is placed in a furnace at austenitizing temperature ($850^\circ\text{C}\text{--}950^\circ\text{C}$, where iron is in the FCC $\gamma\text{-Fe}$ phase with high carbon solubility). A controlled mixture of methane and hydrogen gas ($\text{CH}_4 - \text{H}_2$) is injected:
   $$\text{CH}_4 \rightleftharpoons \text{C}_{\text{dissolved}} + 2\text{H}_2$$
2. **Interstitial Diffusion:** The carbon atom is adsorbed at the surface and diffuses rapidly inward following the analytical solution of Fick's Second Law [Slide 20].
3. **Hardening Mechanism:**
   * Carbon atoms occupy the octahedral interstices of the lattice, generating elastic distortion fields that **block dislocation glide** (*dislocation pinning*), hindering plastic deformation [Slide 30].
   * After carburizing, the part is quenched and tempered, transforming the carbon-rich surface layer into **tetragonal martensite** of extreme hardness ($\ge 60\text{ HRC}$) [Slide 31].
4. **Compressive Residual Stresses:**
   * The martensitic transformation of the surface layer involves a larger volumetric expansion than that of the low-carbon core. This generates a surface state of **compressive residual stresses** [Slide 30].
   * These compressive stresses delay the nucleation and propagation of cracks under cyclic fatigue, greatly raising the fatigue limit of the component [Slide 30].

### 1.2 The Dual-Property Requirement (Gears and Shafts):
* **Outer Case:** Extremely hard and resistant to wear from friction, rubbing and contact fatigue (*pitting*).
* **Inner Core:** Ductile and tough, to absorb dynamic impact loads without catastrophic fracture.
* **Optimal Manufacturability:** The complex machining of the gear teeth is carried out in the original "soft" state (easy machining); the thermochemical hardening is performed afterwards on the final geometry [Slide 30].

---

## 🛩️ 2. Diffusion Bonding and Superplastic Forming (DB/SPF)

**Diffusion bonding** (DB) is a solid-state joining process in which two clean, polished metal surfaces are pressed intimately together at elevated temperatures ($T > 0.5\text{--}0.7 T_m$) in a vacuum or inert-gas atmosphere [Slide 33].

### Physical Mechanism:
* The initial microscopic plastic deformation collapses the surface asperities.
* Atomic interdiffusion across the interface eliminates microporosity through surface and grain-boundary diffusion.
* The interface disappears completely by recrystallization and grain growth, forming a continuous monolithic joint with mechanical properties identical to those of the base metal [Slide 33].

### Flagship Aerospace Application: Rolls-Royce Trent 500 Turbofan Blades
* The wide-chord fan blades of the **Rolls-Royce Trent 500** engine (which powers the Airbus A340-500/600) are manufactured by combining **Diffusion Bonding and Superplastic Forming (DB/SPF)** of $\text{Ti-6Al-4V}$ titanium alloy sheets [Slide 33].
* A hollow three-dimensional sandwich structure with a corrugated internal core (*honeycomb / truss core*) is produced.
* **Critical Advantages:**
  1. Substantial reduction of the fan rotor weight.
  2. Extraordinary torsional and structural stiffness.
  3. Massive resistance to damage from impact by foreign objects (**FOD**, *Foreign Object Damage*, e.g. bird ingestion at take-off) [Slide 33].

---

## 🏺 3. Sintering of Metal and Ceramic Powders (*Sintering*)

**Sintering** is the process of consolidating parts from compacted ceramic or metal powders at a temperature below the melting point ($T < T_m$) [Slide 32].

* **Official Definition:** A thermally activated mass-transport process that leads to chemical bonding between adjacent particles and to the **progressive reduction of porosity** [Slide 32].
* **Driving Force:** Decrease of the total interfacial free energy of the system ($\Delta G < 0$) by replacing an immense free solid-gas surface area ($\gamma_{\text{sv}}$) with lower-energy solid-solid grain boundaries ($\gamma_{\text{gb}}$).
* **Microstructural Stages [Slide 32]:**
  1. Green compact: particles in point contact with high open porosity.
  2. Neck formation and growth (*neck growth*) at $1220^\circ\text{C}\text{--}1370^\circ\text{C}$ by surface and volume diffusion.
  3. Densification and pore closure at $1520^\circ\text{C}$, with polygonal grain growth.
* **Biomedical and Aerospace Application:** Alumina/zirconia hip prostheses, ceramic rocket nozzles and silicon carbide components [Slide 32].

---

## 💧 4. Hydrogen Purification with Palladium ($\text{Pd}$) Membranes

Metallic palladium has an extraordinary solubility and selective permeability towards gaseous hydrogen [Slide 35]:

* $\text{H}_2$ molecules dissociate catalytically on the outer surface of the palladium into $\text{H}$ atoms.
* Hydrogen atoms diffuse interstitially and very rapidly through the FCC lattice of $\text{Pd}$ thanks to a concentration gradient maintained by the gas partial-pressure difference between the two faces.
* It makes it possible to obtain hydrogen with a purity above $99.9999\%$, essential for fuel cells in satellites and crewed spacecraft [Slide 35].

---

## 💻 5. Microelectronics: Dopant Diffusion in Silicon Wafers

The manufacture of semiconductors and monolithic integrated circuits (CMOS) depends on introducing acceptor or donor impurities (Boron, Phosphorus, Arsenic, Aluminum) into Silicon single crystals by high-temperature diffusion ($900^\circ\text{C}\text{--}1200^\circ\text{C}$) [Slides 29, Problems 2]:

* By controlling the time $t$ and temperature $T$, the error-function solution ($\text{erf}$) makes it possible to tune the junction depth of the $p\text{-}n$ junction ($x_j$) with nanometric precision.

---

## 🥛 6. Polymer Barriers and Gas Permeation in Packaging and Aerospace

The diffusion of vapors and gases ($\text{H}_2\text{O}$, $\text{O}_2$, $\text{CO}_2$) through polymer films and coatings determines the service life of composite materials and pressurized systems [Slide 34]:

* **Water Vapor:** Moisture ingress degrades the epoxy resin matrix in aerospace composites (hygrothermal effects, resin plasticization and degradation of the glass transition temperature $T_g$).
* **Oxygen:** Oxygen diffusion in polymers causes photochemical degradation, polymer oxidation and corrosion of internal metal substrates [Slide 34].

---

## 🔗 Related Links
* [[Topic 3 - Diffusion in Solids and Mass Transport]] (Master MOC of Topic 3)
* [[Concept - Diffusion Mechanisms, Vacancies and Interstitials]]
* [[Concept - Fick's First Law, Steady-State Diffusion]]
* [[Concept - Fick's Second Law, Non-Steady-State Diffusion and the Error Function]]
* [[Problem - T3-01 Carburisation of a 1018 Steel Gear]]
* [[Problem - T3-05 Carburising Temperature of 1010 Steel in 8 Hours]]
* [[Problem - T3-06 Hydrogen Purification with a Palladium Membrane]]
