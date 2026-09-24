---
materia: "Aerospace Materials I"
tema: "Tema 1: Bonding in Solids"
fuentes: "Session 2 T1 Bonding_2025.pdf, Slides 16-21, 37-38"
tags:
  - teoria
  - concepto-clave
  - covalent-bonding
  - polar-covalence
  - hannay-smyth
dificultad: media
prerrequisitos:
  - "Configuraciones electrónicas y orbitales atómicos"
---

# 📖 Concepto: Enlace Covalente y Carácter Polar

> **Key Idea in One Sentence:** Covalent bonding is the directional sharing of outer $s$ and $p$ valence electron pairs between atoms with small electronegativity differences to achieve a stable closed-shell configuration, spanning a continuous spectrum from purely non-polar sharing to partial ionic character described by the Hannay-Smyth relation.

---

## 🎯 1. Fundamental Mechanism and Directionality

### 1.1 Orbital Overlap and Electron Sharing [Slide 17]
* **Origin:** Forms predominantly between non-metallic elements positioned close to one another in the periodic table with small electronegativity differences ($\Delta\chi < 1.7$).
* **Mechanism:** Rather than an outright loss or gain of electrons, atoms achieve a stable octet (noble gas configuration $s^2 p^6$) by sharing pairs of valence electrons in localized molecular orbitals situated directly between the bonded nuclei.
* **Strict Directionality:** Unlike spherically symmetric ionic or metallic interactions, covalent bonds are **highly directional**. The electron density is concentrated along specific spatial vectors dictated by quantum mechanical orbital hybridization ($sp, sp^2, sp^3$).

### 1.2 Tetrahedral Coordination in Silicon and Silica [Slide 18]
* **Elemental Silicon ($\text{Si}$):** Silicon possesses a valence electron configuration of $3s^2 3p^2$ (valence of 4). To fulfill the octet rule, each $\text{Si}$ atom forms four mutually repulsive hybridized $sp^3$ orbitals pointing toward the vertices of a regular tetrahedron.
  * The resulting equilibrium inter-bond angle is exactly:
    $$\theta = 109.5^\circ \quad (\arccos(-1/3))$$
* **Silica ($\text{SiO}_2$):** In quartz and silicate ceramics, basic $\text{SiO}_4^{4-}$ tetrahedral units are linked by sharing corner oxygen atoms ($\text{Si}-\text{O}-\text{Si}$). The strong, directional $\text{Si}-\text{O}$ covalent bonds ($~50\%$ covalent, $~50\%$ ionic) provide high thermal stability, high elastic stiffness, and extreme resistance to chemical attack.

---

## 💎 2. Continuous Network Covalent Solids [Slides 19, 38]

Materials bound entirely by a three-dimensional continuous network of covalent bonds are called **covalent network solids**. They must be distinguished from molecular substances (such as $\text{H}_2\text{O}$ or $\text{CH}_4$, which contain internal covalent bonds but are held together in the solid state by weak secondary forces).

### Key Examples:
1. **Diamond (Carbon):** Giant network of $sp^3$ hybridized carbon atoms in a diamond-cubic lattice. Possesses the highest hardness of any natural mineral (Mohs 10), highest thermal conductivity at room temperature ($\approx 2200\text{ W}/(\text{m}\cdot\text{K})$ via phonon transport), and an exceptionally high melting temperature ($T_m > 3800\text{ K}$).
2. **Silicon Carbide ($\text{SiC}$):** Tetrahedral network used extensively in aerospace high-temperature structural ceramics, turbine seals, and aerospace composites.
3. **Cubic Boron Nitride ($c\text{-BN}$):** Isoelectronic to diamond, offering exceptional chemical stability against ferrous metals at elevated temperatures.
4. **Quartz ($\text{SiO}_2$):** Giant covalent framework of corner-sharing tetrahedra.

### Characteristic Engineering Properties [Slides 19, 38]:
* **Extreme Hardness & Incompressibility:** Disrupting the solid requires the simultaneous mechanical shearing of billions of localized, rigid covalent bonds.
* **Very High Melting / Sublimation Temperatures:** Typical $T_m > 2000\text{--}3500^\circ\text{C}$ due to massive cohesive bond energies ($125\text{--}300\text{ kcal/mol} \approx 523\text{--}1255\text{ kJ/mol}$ [Slide 29]).
* **Total Insolubility:** Neither polar nor non-polar solvents can overcome the massive lattice energy to solvate the network.
* **Electrical Insulators in Solid and Molten States:** Valence electrons are strictly confined to localized $\sigma$ or $\pi$ bonding orbitals with wide band gaps ($E_g > 3\text{--}6\text{ eV}$), preventing electronic conduction even upon melting.

---

## ⚡ 3. Polarity, Dipole Moment, and the Hannay-Smyth Relation

### 3.1 Dipole Moment Definition [Slide 20]
When two bonded atoms have different electronegativities ($\chi_A \neq \chi_B$), the shared electron cloud is pulled closer to the more electronegative nucleus, generating a partial negative charge ($\delta^-$) and leaving a partial positive charge ($\delta^+$) on the other. This separation forms a **polar covalent bond**.

The electric dipole moment $\mu$ is defined as:

$$\vec{\mu} = Q \cdot \vec{d}$$

Where:
* $Q$: Net separated charge $[\text{C}]$.
* $d$: Distance vector between charge centers $[\text{m}]$.
* Units: Measured in **Debye ($\text{D}$)**, where:
  $$1\text{ D} = 3.33 \times 10^{-30}\text{ C}\cdot\text{m}$$

### 3.2 Percentage of Ionic Character (Hannay-Smyth Equation) [Slide 20]
The transition between pure covalent and pure ionic bonding is a continuous spectrum governed by the electronegativity difference $\Delta\chi = |X_A - X_B|$. The percentage of ionic character is quantitatively modeled by the **Hannay-Smyth equation**:

$$\% \text{ Ionic Character} = \left[1 - \exp\left(-0.25\,(X_A - X_B)^2\right)\right] \times 100\%$$

* **Non-polar covalent:** $X_A \approx X_B \implies \% \text{ ionic} \approx 0\%$ (e.g., $\text{C}-\text{C}, \text{Si}-\text{Si}, \text{Cl}_2$).
* **Mixed Covalent-Ionic:**
  * $\text{Si}-\text{C}$ ($\chi_{\text{Si}} = 1.9, \chi_{\text{C}} = 2.5 \implies \Delta\chi = 0.6$):
    $$\% \text{ ionic} = (1 - e^{-0.25(0.6)^2}) \times 100\% = (1 - e^{-0.09}) \times 100\% \approx 8.6\%$$
  * $\text{Si}-\text{O}$ ($\chi_{\text{Si}} = 1.9, \chi_{\text{O}} = 3.44 \implies \Delta\chi = 1.54$):
    $$\% \text{ ionic} = (1 - e^{-0.25(1.54)^2}) \times 100\% = (1 - e^{-0.593}) \times 100\% \approx 44.7\%$$
* **Predominantly Ionic:** $\Delta\chi > 2.0 \implies \% \text{ ionic} > 63\%$ (e.g., $\text{NaCl}, \Delta\chi = 2.23 \implies \% \text{ ionic} \approx 71\%$).

---

## 📏 4. Bond Order, Bond Length, and Bond Energy [Slide 21]

For a given pair of bonded atoms, the mechanical and thermochemical stability is strictly governed by the **bond order** (the number of shared electron pairs):

$$\text{Bond Order } \uparrow \implies \text{Bond Length } (d) \downarrow \implies \text{Bond Energy } (E_b) \uparrow$$

### Experimental Carbon-Carbon Benchmark:
| Bond Type | Bond Order | Average Bond Length ($d$) | Bond Dissociation Energy ($E_b$) |
| :--- | :--- | :--- | :--- |
| $\text{C}-\text{C}$ (Single) | $1$ | $0.154\text{ nm}$ ($1.54\text{ \AA}$) | $\mathbf{348\text{ kJ/mol}}$ ($83\text{ kcal/mol}$) |
| $\text{C}=\text{C}$ (Double) | $2$ | $0.134\text{ nm}$ ($1.34\text{ \AA}$) | $\mathbf{614\text{ kJ/mol}}$ ($147\text{ kcal/mol}$) |
| $\text{C}\equiv\text{C}$ (Triple) | $3$ | $0.120\text{ nm}$ ($1.20\text{ \AA}$) | $\mathbf{839\text{ kJ/mol}}$ ($201\text{ kcal/mol}$) |

* **Diatomic Gas Comparison [Slide 21]:**
  * $\text{F}_2$ (single bond $\text{F}-\text{F}$, bond order 1): $d = 1.42\text{ \AA}$, $E_b = 158\text{ kJ/mol}$.
  * $\text{O}_2$ (double bond $\text{O}=\text{O}$, bond order 2): $d = 1.21\text{ \AA}$, $E_b = 498\text{ kJ/mol}$.
  * $\text{N}_2$ (triple bond $\text{N}\equiv\text{N}$, bond order 3): $d = 1.10\text{ \AA}$, $E_b = 945\text{ kJ/mol}$.

---

## ⚠️ 5. Typical Exam Traps & Conceptual Distinctions
> [!WARNING] Covalent Network vs Covalent Molecular
> A frequent student mistake is confusing **covalent solids** (e.g., diamond, quartz) with **molecular solids** held by covalent internal bonds (e.g., solid $\text{CH}_4$, ice, polymers). Covalent solids require breaking primary covalent bonds to melt ($T_m > 1500^\circ\text{C}$), whereas molecular solids melt at low temperatures because only weak intermolecular secondary bonds are broken!

---

## 🔗 Related Notes
* `[[Tema 1 - Bonding in Solids and Material Properties]]`
* `[[Concepto - Enlace Ionico y Energia Reticular de Born-Lande]]`
* `[[Concepto - Fuerzas Intermoleculares y Enlaces Secundarios]]`
* `[[Problema - Cuestion 1 Examen T1 Enlace Metalico vs Covalente]]`
* `[[Problema - Cuestion 4 Examen T1 Modulo de Elasticidad Aluminio vs Silicio]]`
