---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 4 T2 Structure of Materials II_2025.pdf, Slides 48-50"
tags:
  - theory
  - fundamental-concept
  - polymorphism
  - allotropy
  - phase-transformations
  - iron-steel
  - zirconia
  - carbon
dificultad: medium
prerrequisitos:
  - "[[Concept - Planar Defects, Grain Boundaries, Twins and the Hall-Petch Equation]]"
---

# 🔄 Concept: Polymorphism and Allotropy in Metals and Ceramics

> **Canonical Definitions [Slide 48]:**
> * **Polymorphism:** The ability of a solid material (element or chemical compound) to exist in **more than one different crystal structure** under different thermodynamic conditions of temperature and pressure.
> * **Allotropy:** The specific case of polymorphism when it refers to a **pure chemical element**.

---

## 💎 1. Carbon Allotropes: Diamond vs Graphite [Slide 48]

Carbon illustrates how the same elemental composition acquires radically divergent properties depending on the electronic hybridization and the crystal symmetry:

```
Property               Diamond (Covalent Cubic)                    Graphite (Hexagonal Layered)
─────────────────────────────────────────────────────────────────────────────────────────────────
Hybridization          sp³ (4 direct σ bonds at 109.5°)            sp² (3 planar σ bonds at 120° + 1 delocalized π e⁻)
Structure              Three-dimensional tetrahedral network       Hexagonal planes joined by weak van der Waals bonds
Hardness and Abrasion  Hardest substance in nature (10 Mohs)       Extremely soft (natural solid lubricant)
Optical Properties     Transparent with a very high refractive index  Opaque black
Electrical Conductivity  Excellent electrical insulator (bandgap = 5.5 eV)  Excellent electrical conductor parallel to the basal layers
```

---

## ⚙️ 2. Allotropic Transformations of Iron ($\text{Fe}$) [Slide 49]

Pure iron undergoes successive solid-state phase transitions on heating at standard atmospheric pressure:

$$\alpha\text{-Fe (BCC)} \xrightarrow{\mathbf{912^\circ C}} \gamma\text{-Fe (FCC)} \xrightarrow{\mathbf{1394^\circ C}} \delta\text{-Fe (BCC)} \xrightarrow{\mathbf{1538^\circ C}} \text{Liquid}$$

### Metallurgical Significance and Heat Treatments:
1. **Intrinsic Volume Change:**
   On heating through $912^\circ\text{C}$, the lattice changes from BCC ($n=2$, $\text{APF} = 0.68$) to FCC ($n=4$, $\text{APF} = 0.74$). This abrupt increase in packing efficiency causes a **net volumetric contraction of the metal** ($\approx -1\%$ in molar volume) on crossing the critical temperature.
2. **Carbon Solubility and Quench Hardening of Steels:**
   * In $\alpha\text{-Fe}$ (BCC), the octahedral sites are small ($0.155\, r$), limiting the carbon solubility to a maximum of **$0.022\text{ wt\%}$**.
   * In $\gamma\text{-Fe}$ (FCC, austenite), the octahedral sites are wide ($0.414\, r$), allowing up to **$2.14\text{ wt\%}$ of carbon** to dissolve.
   * On rapid cooling (quenching) from the austenitic $\gamma$ field, the carbon becomes trapped in the interstices of the iron lattice, preventing diffusion and forcing a diffusionless transformation into a supersaturated body-centered tetragonal phase called **martensite**, the basis of the strength of ultra-high-strength steels in aeronautical landing gear.

---

## 🏺 3. Zirconia ($\text{ZrO}_2$) and Transformation Toughening by Martensitic Transformation [Slide 50]

Pure zirconium dioxide ($\text{ZrO}_2$) goes through three polymorphic phases as the temperature varies:

$$\text{Monoclinic} \xrightarrow{1170^\circ\text{C}} \text{Tetragonal} \xrightarrow{2370^\circ\text{C}} \text{Cubic (Fluorite-type } \text{CaF}_2\text{)} \xrightarrow{2706^\circ\text{C}} \text{Liquid}$$

### The Transformation Toughening Mechanism:
* On cooling pure, undoped zirconia, the tetragonal-to-monoclinic transition induces a **catastrophic volumetric expansion of 3% to 5%** accompanied by elastic shear, pulverizing the ceramic part.
* By doping zirconia with yttrium oxide ($\text{Y}_2\text{O}_3$, $3\text{--}8\text{ mol\%}$), the **metastable tetragonal phase is stabilized at room temperature** (Y-TZP: *Yttria-Stabilized Tetragonal Zirconia Polycrystal*).
* When a microscopic crack advances under tensile load, the elastic stress field at the crack tip locally triggers the tetragonal $\to$ monoclinic phase transformation.
* Since the monoclinic phase has a larger molar volume, the transformation **expands against the surrounding elastic matrix, generating intense closing compressive stresses that squeeze and arrest the crack**.
* This mechanism raises the fracture toughness of zirconia up to $K_{IC} \approx 8\text{--}12\text{ MPa}\sqrt{\text{m}}$, making it the "ceramic steel" used in thermal barrier coatings (TBC) of turbine blades.

---
*Bidirectional Links:*
* [[Concept - Planar Defects, Grain Boundaries, Twins and the Hall-Petch Equation|⬅️ Previous: Planar Defects and Hall-Petch]]
* [[Topic 2 - Structure of Materials and Crystalline Defects|Back to the Topic 2 MOC 🏠]]
