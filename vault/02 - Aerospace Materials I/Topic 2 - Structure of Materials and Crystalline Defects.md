---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 3 T2 Structure of Materials I_2025.pdf, Session 4 T2 Structure of Materials II_2025.pdf, Problems T2_CrystStruct.pdf, Problems T2 defects.pdf"
tags:
  - theory
  - topic-moc
  - crystal-structure
  - crystalline-defects
  - miller-indices
  - dislocations
  - x-ray-diffraction
dificultad: medium
prerrequisitos:
  - "[[Topic 1 - Bonding in Solids and Material Properties]]"
---

# 🌐 Topic 2: Structure of Materials and Crystalline Defects

> **Central Idea of the Topic:** The three-dimensional geometric arrangement of atoms in periodic crystal lattices (crystallography) and, even more decisively, the presence and behavior of **crystalline imperfections or defects** (point, line, planar and volumetric) absolutely govern the real mechanical properties, plastic deformability, fracture resistance and thermal response of aerospace metallic and ceramic materials [Session 3 Slide 2, Session 4 Slide 11].

$$\text{Crystal Structure (Bravais)} + \text{Defects (0D, 1D, 2D)} \implies \text{Mechanical and Aerospace Properties}$$

---

## 🗺️ 1. Concept Map of the UC3M Sessions

```
TOPIC 2: STRUCTURE OF MATERIALS AND CRYSTALLINE DEFECTS
│
├── 🏛️ PART I: CRYSTALLOGRAPHY AND BRAVAIS LATTICES (Session 3)
│   ├── Lattice Parameters and 7 Crystal Systems (Cubic, Tetragonal, Orthorhombic, Rhombohedral, Hexagonal, Monoclinic, Triclinic)
│   ├── The 14 Bravais Lattices (P, I, F, C) [Auguste Bravais, 1848]
│   ├── Fundamental Metallic Structures: BCC (n=2, APF=0.68), FCC (n=4, APF=0.74), HCP (n=6, APF=0.74)
│   ├── Close Packing: ABABAB... (HCP) vs ABCABC... (FCC) and ideal ratio c/a = √(8/3) ≈ 1.633
│   ├── Interstitial Sites per cell: FCC 8 tet + 4 oct (2n, n); HCP 12 tet + 6 oct (2n, n); BCC 12 tet + 6 oct (6n, 3n; the 2n/n rule only holds in close-packed structures)
│   ├── Miller Indices for Directions [uvw] and Planes (hkl) in Cubic Systems
│   ├── 4-axis Miller-Bravais Indices for Hexagonal Lattices (hkil) and [uvtw]
│   └── X-Ray Diffraction (XRD), Interplanar Spacings dhkl and Bragg's Law (λ = 2d·sin θ)
│
└── 🔬 PART II: DENSITIES, LATTICE DEFECTS AND POLYMORPHISM (Session 4)
    ├── Density Calculations in Lattices: Volumetric (ρv), Linear (ρl) and Planar (ρp)
    ├── Point Defects (0D): Thermal vacancies (nv/N = exp(-ΔHv/RT)), self-interstitials
    ├── Ionic Crystals: Schottky pairs (ns = N·exp(-ΔHs/2RT)) and Frenkel (nF = √(N·Ni)·exp(-ΔHF/2RT))
    ├── Solid Solutions: Substitutional vs Interstitial, Hume-Rothery Rules (4 criteria)
    ├── Electric Charge Compensation in Ceramics (3Mg²⁺ ↔ 2Al³⁺ + 1 cation vacancy)
    ├── Order-Disorder Phenomenon in Alloys (Cu-Au at T = 390 °C)
    ├── Line Defects / Dislocations (1D): Edge (Taylor, b ⊥ t), Screw (Burgers, b || t) and Mixed
    ├── Burgers Vector b, Burgers Circuit and Stored Elastic Energy (E ∝ |b|²)
    ├── Slip Systems: Close-packed planes + Close-packed directions (FCC: 12, BCC: 12, HCP: 3)
    ├── Planar Defects (2D): Grain boundaries (2-5 atomic distances, high interfacial energy)
    ├── Hall-Petch Equation for Grain Refinement: σy = σ0 + ky·d^(-1/2)
    ├── Deformation and Annealing Twins, Stacking Faults (ABCABABC) and Free Surfaces
    └── Polymorphism and Allotropy: Carbon (Diamond vs Graphite), Zirconia (ZrO2) and Allotropy of Iron (α-Fe → γ-Fe → δ-Fe)
```

---

## 📐 2. Fundamental Mathematical Relations

### 1. Lattice Parameters and Atomic Geometry:
* **BCC:** $a = \frac{4R}{\sqrt{3}}, \quad n = 2, \quad \text{NC} = 8, \quad \text{APF} = \frac{\pi\sqrt{3}}{8} \approx 0.6802$
* **FCC:** $a = 2\sqrt{2}R, \quad n = 4, \quad \text{NC} = 12, \quad \text{APF} = \frac{\pi\sqrt{2}}{6} \approx 0.7405$
* **HCP:** $a = 2R, \quad c = a\sqrt{\frac{8}{3}} \approx 1.633 a, \quad n = 6, \quad \text{NC} = 12, \quad \text{APF} = 0.7405$

### 2. Interstitial Sites and Critical Radii:
* **FCC:** $N_{\text{tet}} = 8$ at $\frac{a\sqrt{3}}{4}$ with $r_{\text{tet}} = (\sqrt{3/2}-1)r \approx 0.225r$; $N_{\text{oct}} = 4$ with $r_{\text{oct}} = (\sqrt{2}-1)r \approx 0.414r$.
* **BCC:** $N_{\text{tet}} = 12$ on faces with $r_{\text{tet}} = (\sqrt{5/3}-1)r \approx 0.291r$; $N_{\text{oct}} = 6$ at face and edge centers with $r_{\text{oct}} = (\frac{2}{\sqrt{3}}-1)r \approx 0.155r$.

### 3. Crystallographic Densities:
* **Volumetric:** $\rho_v = \frac{n \cdot M}{V_C \cdot N_A}$
* **Linear:** $\rho_l = \frac{N_{\text{atoms centered}}}{L_{[uvw]}}$
* **Planar:** $\rho_p = \frac{N_{\text{atoms in plane}}}{A_{(hkl)}}$
* **Relation to spacing:** $\rho_v = \frac{\rho_p(hkl)}{d_p}$, with $d_p$ the distance between consecutive planes that contain atoms ($d_p = d_{hkl}$ if all planes are populated; $d_p = d_{hkl}/2$ e.g. in $(100)$ of BCC and FCC)

### 4. Interplanar Spacing and Bragg's Law:
* **Cubic:** $d_{hkl} = \frac{a}{\sqrt{h^2+k^2+l^2}}$
* **Orthorhombic:** $\frac{1}{d_{hkl}^2} = \frac{h^2}{a^2} + \frac{k^2}{b^2} + \frac{l^2}{c^2}$
* **Bragg's Law:** $\lambda = 2d_{hkl}\sin\theta$

### 5. Defect Thermodynamics and Slip:
* **Thermal vacancies in metals:** $\frac{n_v}{N} = \exp\left(-\frac{\Delta H_v}{RT}\right), \quad N = \frac{\rho N_A}{M}$
* **Schottky defects (Ionic):** $n_s = N \exp\left(-\frac{\Delta H_s}{2RT}\right)$
* **Frenkel defects (Ionic):** $n_F = \sqrt{N N_i} \exp\left(-\frac{\Delta H_F}{2RT}\right)$
* **Dislocation elastic energy:** $E \propto |\vec{b}|^2$
* **Hall-Petch equation:** $\sigma_y = \sigma_0 + k_y \cdot d^{-1/2}$

---

## 📚 3. Index of Atomic Concept Notes

1. [[Concept - Crystal Systems and Bravais Lattices]] — 7 crystal systems, 4 cell types (P, I, F, C) and derivation of the 14 Bravais lattices.
2. [[Concept - FCC, BCC and HCP Metallic Structures and Packing Factor]] — Derivations of $a(R)$, cell volumes, APF, coordination numbers and stacking sequences $ABAB\dots$ vs $ABCABC\dots$.
3. [[Concept - Tetrahedral and Octahedral Interstitial Sites]] — Multiplicity $2n$ and $n$ (FCC, HCP; BCC: $6n$ and $3n$), spatial positions and site radii in FCC, BCC and HCP.
4. [[Concept - Miller Notation for Cubic and Hexagonal Directions and Planes]] — Indices $[uvw]$, $(hkl)$, perpendicularity in cubic systems and the Miller-Bravais system $(hkil)$ and $[uvtw]$.
5. [[Concept - Volumetric, Linear and Planar Density in Crystal Lattices]] — Physical definition, step-by-step calculations and relation to interplanar spacing.
6. [[Concept - X-Ray Diffraction and Bragg's Law]] — Constructive interference, calculation of interplanar spacings and structural characterization.
7. [[Concept - Point Defects, Thermal Vacancies, Schottky and Frenkel]] — Statistical thermodynamics ($\Delta G = \Delta H - T\Delta S$), equilibrium concentrations and enthalpy table.
8. [[Concept - Substitutional and Interstitial Solid Solutions, Hume-Rothery Rules]] — 4 solubility rules, charge compensation in ceramics and order-disorder at $390^\circ\text{C}$ in Cu-Au.
9. [[Concept - Dislocations, Burgers Vector and Slip in Metals]] — Taylor, Burgers and mixed dislocations, energy $E \propto |\vec{b}|^2$ and slip systems in metals.
10. [[Concept - Planar Defects, Grain Boundaries, Twins and the Hall-Petch Equation]] — Grain boundaries, Hall-Petch equation, twins, stacking faults and surface energy.
11. [[Concept - Polymorphism and Allotropy in Metals and Ceramics]] — Carbon (diamond/graphite), $\text{ZrO}_2$ and martensitic toughening, iron transformations ($\alpha \to \gamma \to \delta$).

---

## ✏️ 4. Official Collection of the 26 Solved Problems

### Block 1: Crystalline Structures and Miller Indices (`Problems T2_CrystStruct.pdf`)
* [[Problem - T2-CS01 Miller Indices and Densities in FCC]] — Miller indices of the planes in figures I, II, III and linear, planar and volumetric densities in FCC.
* [[Problem - T2-CS02 Atomic Mass and Density of FCC Magnesium]] — Determination of the atomic mass $M=24.31\text{ g/mol}$ and identification of Magnesium in an FCC lattice.
* [[Problem - T2-CS03 Drawing Crystal Planes in a Cubic Lattice]] — Analytical determination and sketches of 10 cubic Miller planes with origin translations.
* [[Problem - T2-CS04 Planar and Linear Densities in the BCC Lattice]] — Surface densities of $(100), (110), (111)$, linear density along $[100]$ and volumetric density in BCC.
* [[Problem - T2-CS05 Planar and Linear Densities and Mass of an Aluminium Bar]] — Densities in FCC Al and mass of a cylindrical bar of $\varnothing 20\text{ mm} \times 1\text{ m}$ ($m = 850.7\text{ g}$ with the given data; the official solution states $855\text{ g}$).
* [[Problem - T2-CS06 Linear and Planar Densities in the 111 Direction of Fe and Ni]] — Comparative analysis of the $[111]$ linear density and $(111)$ planar density in BCC Iron vs FCC Nickel.
* [[Problem - T2-CS07 Orthorhombic Cell and Densities of a Hypothetical Material]] — Derivation of a face-centered orthorhombic cell, molar mass of Silver and planar densities.
* [[Problem - T2-CS08 Planar Packing Fraction on FCC Planes]] — Calculation of the atomic area fraction in the $(111), (200), (220), (222), (400), (420)$ planes in FCC.
* [[Problem - T2-CS09 Volume Change in the BCC to FCC Polymorphic Transformation]] — Calculation of the volume jump of $+5.4\%$ (the official solution states $5.7\%$) from $d_{321}$ in BCC and $\rho_{(002)}$ in FCC at $910^\circ\text{C}$.
* [[Problem - T2-CS10 Identifying Gallium in an Orthorhombic Cell and Close-Packed Directions]] — Base-centered orthorhombic cell, identification of Gallium ($M=69.75\text{ g/mol}$; official $69.76$) and dense directions.
* [[Problem - T2-CS11 Lattice Parameter and Densities of Aluminium from Linear Density]] — Obtaining $a=4.04\text{ \AA}$ from $\rho_{[111]}$ and calculation of the volumetric and planar densities.
* [[Problem - T2-CS12 Drawing Direction Vectors in Cubic Cells]] — Vector representation of 12 cubic crystallographic directions with origin translations.
* [[Problem - T2-CS13 Characterising an Orthorhombic Metal from the 220 Plane and 101 Direction]] — Face-centered orthorhombic lattice, APF, interplanar distances and mass of a $1\text{ cm}^3$ single crystal.
* [[Problem - T2-CS14 XRD and Interplanar Spacings in BCC and FCC Iron]] — Spacings $d_{020}$ and distances between the most close-packed planes of BCC Ferrite and FCC Austenite.

### Block 2: Crystal Defects and Solid Solutions (`Problems T2 defects.pdf`)
* [[Problem - T2-DEF01 Vacancy Fraction in Aluminium near Melting]] — Calculation of the vacancy fraction in Al at $660^\circ\text{C}$ ($n_v/N = 4.49 \times 10^{-4}$; the official solution states $4.53 \times 10^{-4}$) from data at $400^\circ\text{C}$.
* [[Problem - T2-DEF02 Equilibrium Concentration of Schottky and Frenkel Defects]] — Concentration of Schottky ($3.03 \times 10^{-3}$) and Frenkel ($8.39 \times 10^{-11}$) defects at $1000\text{ K}$.
* [[Problem - T2-DEF03 Cationic Vacancies in MgO from Dissolving Al2O3 and TiO2]] — Quantification of cation vacancies by charge neutrality after dissolving $\text{Al}_2\text{O}_3$ and $\text{TiO}_2$ in $\text{MgO}$.
* [[Problem - T2-DEF04 Solubility Ranking in Iron by the Hume-Rothery Rules]] — Rigorous justification of the solubility order in Iron: $\text{Mo} > \text{Ni} > \text{Mn}$.
* [[Problem - T2-DEF05 Non-Stoichiometry Defects and Density Decrease in FeO]] — Calculation of cation vacancies ($0.033\text{ mol/mol}$) and density decrease ($-2.59\%$; official $-2.56\%$) in non-stoichiometric $\text{FeO}$.
* [[Problem - T2-DEF06 Burgers Vector Magnitude in Alpha-Fe and Al]] — Analytical derivation of $|\vec{b}|$ for $\alpha\text{-Fe}$ (BCC: $\frac{a\sqrt{3}}{2}$) and Aluminum (FCC: $\frac{a}{\sqrt{2}}$).
* [[Problem - T2-DEF07 Dislocation Energy Proof in FCC for 100 vs 110 Directions]] — Formal theoretical proof of the elastic energy ratio $E_1/E_2 = 2$.
* [[Problem - T2-DEF08 Burgers Vector of an Edge Dislocation in FCC]] — Determination of the magnitude ($2.5456 \times 10^{-10}\text{ m}$ with $a = 3.6 \times 10^{-10}\text{ m}$; official $2.553 \times 10^{-10}$) and direction $[\bar{1}10]$ in the $(110)$ plane.
* [[Problem - T2-DEF09 Interplanar Spacing and Burgers Vector in a Tantalum Slip System]] — Analysis of the real system $(110)[1\bar{1}1]$ vs the hypothetical $(111)[1\bar{1}0]$ in BCC Tantalum ($a=3.3026\text{ \AA}$).
* [[Problem - T2-DEF10 MgO Al2O3 Solid Solution Vacancies and Density Change]] — Calculation of $0.088\text{ vacancies/Mg atom}$ and a percentage density change of $-3.3\%$ (official $-3\%$) for a 15:85 proportion.
* [[Problem - T2-DEF11 Vacancy Concentration in Copper near Melting]] — Calculation of vacancies per cubic centimeter in Copper at $1080^\circ\text{C}$ ($4.98 \times 10^{19}\text{ vacancies/cm}^3$).
* [[Problem - T2-DEF12 Fraction of Vacant Lattice Points in FCC Palladium]] — Fraction of vacant sites ($0.00204$) and vacancies per $\text{cm}^3$ ($1.39 \times 10^{20}$) in FCC Palladium.

---
*Return:* [[02 - Aerospace Materials I/Aerospace Materials I MOC|⬅️ Back to the Aerospace Materials I MOC]] | [[00 - Indice Central/Master Index|🗺️ Master Index]]
