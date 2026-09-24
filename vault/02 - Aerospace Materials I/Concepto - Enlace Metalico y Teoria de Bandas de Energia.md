---
materia: "Aerospace Materials I"
tema: "Tema 1: Bonding in Solids"
fuentes: "Session 2 T1 Bonding_2025.pdf, Slides 22-27, 37-38"
tags:
  - teoria
  - concepto-clave
  - metallic-bonding
  - electron-sea
  - band-theory
  - ductility
dificultad: media
prerrequisitos:
  - "Orbitales moleculares y teoría cuántica básica"
---

# 📖 Concepto: Enlace Metálico y Teoría de Bandas de Energía

> **Key Idea in One Sentence:** Metallic bonding is the non-directional electrostatic attraction between an ordered crystalline array of positive metal cations and a pervasive, delocalized "sea of valence electrons", which manifests microscopically in band theory through overlapping valence and conduction bands that allow uninhibited electron mobility and dislocation slip.

---

## 🎯 1. The Electron Sea Model & Cohesive Mechanism

### 1.1 Atomic Structure and Delocalization [Slide 23]
* **Nature of Metallic Elements:** Metals have low electronegativities and low ionization energies. In a condensed metallic crystal, the valence electrons are weakly bound to their parent nuclei.
* **Electron Sea Formation:** Metal atoms release their valence electrons into a common, crystal-spanning conduction cloud. The remaining positively charged **ion cores (cations)** occupy periodic lattice sites (e.g., FCC, BCC, HCP) immersed in this pervasive, negatively charged **electron sea**.
* **Electrostatic Cohesion:** The metallic bond is the net isotropic electrostatic attraction between the positively charged ion cores and the delocalized conduction electrons.
* **Non-Directionality:** Because the electron cloud is uniformly distributed and shared by all atoms, metallic bonds possess **no preferential spatial orientation (non-directional)**.

---

## 🔬 2. Valence Electron Dependence of Cohesive Energy [Slide 24]

The cohesive bonding energy $E_b$ and melting temperature $T_m$ of pure metals scale directly with the density of delocalized electrons in the sea (the formal valence $Z$ of the metallic element):

$$\text{Valence Electrons } Z \uparrow \implies \text{Charge Density of Electron Sea } \uparrow \implies \text{Bonding Energy } E_b \uparrow \implies T_m \uparrow$$

### Quantitative UC3M Benchmarks [Slide 24]:
1. **Monovalent Alkali Metals (Valence $+1$):**
   * *Potassium ($\text{K}$):* Electron configuration $[\text{Ar}]\,4s^1$ ($Z = 1$). Only one valence electron per atom contributes to the electron sea.
   * Bonding Energy: $\mathbf{89.6\text{ kJ/mol}}$
   * Melting Temperature: $\mathbf{63.5^\circ\text{C}}$ ($336.7\text{ K}$)
   * Result: Extremely soft, low stiffness, can be cut with a dull knife.
2. **Divalent Alkaline-Earth Metals (Valence $+2$):**
   * *Calcium ($\text{Ca}$):* Electron configuration $[\text{Ar}]\,4s^2$ ($Z = 2$). Two electrons per atom enter the delocalized sea, doubling the negative charge density between the divalent $\text{Ca}^{2+}$ cations.
   * Bonding Energy: $\mathbf{177.0\text{ kJ/mol}}$ (nearly double that of $\text{K}$!)
   * Melting Temperature: $\mathbf{851.0^\circ\text{C}}$ ($1124.2\text{ K}$)
3. **Transition Metals (3d, 4d, 5d series — e.g., $\text{Ti}, \text{V}, \text{Cr}, \text{Fe}, \text{W}$):**
   * Transition metals involve both outer $s$ electrons and partially filled inner $d$ orbitals in bonding.
   * The localized covalent-like overlap of directional $d$ orbitals reinforces the metallic electron sea, yielding exceptional cohesive energies ($E_b = 400\text{--}850\text{ kJ/mol}$) and very high melting points (e.g., Titanium $T_m = 1668^\circ\text{C}$, Tungsten $T_m = 3422^\circ\text{C}$).

---

## 🛠️ 3. Physical & Mechanical Properties of Pure Metals [Slide 25]

### 3.1 Extreme Ductility and Malleability
* **Microscopic Slip Mechanism:** When a shear stress is applied to a metallic crystal, planes of cations slide past one another via dislocation glide.
* **Why Metals Do Not Cleave Brittly:** Because the electron sea is fluid, homogeneous, and non-directional, it instantly accommodates the new atomic positions of the shifted cations. At no point do identical repulsive charges collide without screening (unlike ionic crystals).
* **Alloying:** Pure metals are typically soft; their yield strength is engineered through **solid solution strengthening, precipitation hardening, or grain boundary engineering** by introducing lattice strain fields that impede dislocation motion [Slide 25].

```
Metallic Slip (Ductile):                 Ionic Slip (Brittle Catastrophe):
  +   +   +   +  ---> Applied Force        + - + - + -  ---> Applied Force
  ~~~~~~~~~~~~~~~~~ (Electron Sea)         - + - + - +
  +   +   +   +                            ──────────────────
Planes glide smoothly without charge       + + + + + +  <-- Like charges align!
repulsion. Bonds re-form instantly.        - - - - - -  <-- Massive Coulombic repulsion
                                                        results in instant cleavage fracture!
```

### 3.2 Electrical and Thermal Conductivity [Slide 25]
* Under an applied electric potential gradient $\vec{E}$, electrons near the Fermi surface acquire a net drift velocity $\vec{v}_d = -\mu_e \vec{E}$, conducting electric current without any barrier ($\sigma \approx 10^7\text{ S/m}$).
* Thermal energy is rapidly transferred through the lattice predominantly by the kinetic motion of these identical free conduction electrons (Lorenz relation / Wiedemann-Franz Law: $k/\sigma = L T$).

---

## 📊 4. Band Theory in Metallic Solids [Slides 26-27]

Band theory provides the quantum mechanical foundation for metallic conductivity and cohesive energy.

### 4.1 Formation of Energy Bands [Slide 26]
* When $N$ isolated atoms coalesce to form a solid crystal, the Pauli Exclusion Principle dictates that no two electrons may occupy the identical quantum state.
* The discrete atomic valence orbitals split and overlap into $N$ closely spaced Molecular Orbitals (MOs).
* In a macroscopic crystal ($N \approx 10^{23}$), the energy spacing between adjacent molecular orbitals is infinitesimal ($\Delta E \sim 10^{-22}\text{ eV}$), effectively forming a continuous **energy band**.
* The metal can thus be conceived as a **giant molecule** whose valence band and conduction band govern its electronic response.

### 4.2 Overlapping Bands: The Hallmarks of Metallic Conduction [Slide 27]

```
Energy E
   ▲
   │        Empty states (unoccupied)
   │     ┌────────────────────────┐
   │     │    Conduction Band     │
   │     ├────────────────────────┤ ◄─── Fermi Level (E_F)
   │     │     Valence Band       │
   │     │ (Partially filled or   │
   │     │   overlapping)         │
   │     └────────────────────────┘
   └────────────────────────────────────► Interatomic Distance
```

* **Monovalent Metals (e.g., Lithium, $\text{Li}: 1s^2 2s^1$):**
  * The $2s$ atomic orbital is half-filled.
  * In $\text{Li}_N$, the resulting $2s$ valence band can hold $2N$ electrons, but only $N$ electrons are present. The valence band is **half-filled**.
  * Electrons at the Fermi energy $E_F$ can absorb infinitesimal amounts of thermal or electrical energy to occupy adjacent vacant states within the same band, enabling effortless electrical conduction.
* **Divalent Metals (e.g., Magnesium, $\text{Mg}: 1s^2 2s^2 2p^6 3s^2$):**
  * The $3s$ subshell is completely full. One might naively expect $\text{Mg}$ to be an insulator.
  * However, at the equilibrium interatomic spacing $a_0$, the empty $3p$ atomic orbitals broaden into a $3p$ conduction band that **physically and energetically overlaps with the filled $3s$ valence band** [Slide 27].
  * There is **zero band gap** ($E_g = 0$), allowing valence electrons to spill freely into the $3p$ conduction states, ensuring high metallic conductivity.

---

## 🔗 Related Notes
* `[[Tema 1 - Bonding in Solids and Material Properties]]`
* `[[Concepto - Enlace Covalente y Caracter Polar]]`
* `[[Concepto - Curvas de Energia Potencial Interatomica y Propiedades Macroscopicas]]`
* `[[Problema - Cuestion 1 Examen T1 Enlace Metalico vs Covalente]]`
* `[[Problema - Cuestion 2 Examen T1 Curvas de Potencial Titanio vs Aluminio]]`
