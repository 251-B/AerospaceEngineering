---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 4 T2 Structure of Materials II_2025.pdf, Slides 20-24"
tags:
  - theory
  - fundamental-concept
  - solid-solutions
  - hume-rothery
  - substitutional
  - interstitial
  - charge-compensation
  - order-disorder
dificultad: medium
prerrequisitos:
  - "[[Concept - Point Defects, Thermal Vacancies, Schottky and Frenkel]]"
---

# ⚗️ Concept: Substitutional and Interstitial Solid Solutions and the Hume-Rothery Rules

> **Formal Definition:** A **solid solution** is a homogeneous crystalline solid composed of two or more elements dispersed at the atomic level in a single uniform thermodynamic phase [Slide 20]. The solvent (or matrix) keeps its basic crystal lattice while the solute atoms are incorporated by replacing lattice sites or by lodging in the interstitial voids.

---

## 🔀 1. Classification: Substitutional vs Interstitial Solutions

1. **Substitutional Solid Solutions:**
   * The solute atoms directly replace the matrix lattice atoms at their regular sites [Slide 20].
   * *Aerospace examples:* Nickel dissolved in Copper ($\text{Cu-Ni}$, total isomorphous solubility), Zinc in Copper (brasses), Chromium and Molybdenum in Nickel (Inconel superalloys).
2. **Interstitial Solid Solutions:**
   * The solute atoms lodge exclusively in the free tetrahedral or octahedral sites of the solvent lattice [Slide 20].
   * Only possible for elements with **very small atomic radii**:
     $$\text{Hydrogen (H)}, \quad \text{Carbon (C)}, \quad \text{Nitrogen (N)}, \quad \text{Boron (B)}$$
   * The solubility is usually very restricted (e.g., $< 0.022\text{ wt\%}$ of C in $\alpha\text{-Fe}$ ferrite at $727^\circ\text{C}$).

---

## 📜 2. The 4 Hume-Rothery Rules for Substitutional Solutions

William Hume-Rothery formulated the empirical conditions necessary for two metals to exhibit appreciable ($> 1\text{ at\%}$) or complete ($100\%$ over the whole composition range) solid solubility [Slide 22]:

1. **Atomic Size Rule (Radius Difference):**
   * For metals: the percentage difference in atomic radii must be **less than 15%**:
     $$\Delta R = \left|\frac{R_{\text{solute}} - R_{\text{solvent}}}{R_{\text{solvent}}}\right| \times 100 < 15\%$$
   * If $\Delta R > 15\%$, the elastic lattice distortions are prohibitive and the solubility is below $1\%$.
   * For ionic ceramic compounds, a difference of up to **30%** is tolerated [Slide 22].
2. **Crystal Structure Rule:**
   * The solute and the solvent must have the **same crystal structure** (e.g., both FCC, or both BCC).
   * Complete solid solubility ($0\text{--}100\%$) is impossible if they do not share the same spatial lattice.
3. **Electronegativity Rule:**
   * The two elements must have **very close electronegativities** ($\Delta \chi \approx 0$).
   * If the electronegativity difference is large, the system will preferentially form a stable stoichiometric **intermetallic compound** instead of a disordered solid solution.
4. **Valence Rule:**
   * A metal has a greater tendency to dissolve another element of **higher valence** than one of lower valence. Complete solubility requires the same chemical valence.

> [!WARNING]
> The simultaneous fulfillment of the 4 rules is a **necessary but not sufficient condition** to guarantee complete solubility; if any of the 4 is violated, the solubility will necessarily be partial or null [Slide 22].

---

## ⚖️ 3. Electric Charge Compensation in Ionic Ceramics

When a cationic oxide of a different valence is dissolved in an ionic ceramic matrix, the lattice **must maintain the overall electrical neutrality**. This induces the obligatory formation of intrinsic point defects [Slide 21].

### Dissolution of $\text{Al}_2\text{O}_3$ in $\text{MgO}$ [Slide 21]:
* Matrix: $\text{MgO}$ formed by $\text{Mg}^{2+}$ cations and $\text{O}^{2-}$ anions.
* Solute: $\text{Al}_2\text{O}_3$ contributes $\text{Al}^{3+}$ ions.
* To incorporate two $\text{Al}^{3+}$ cations (charge $+6$) at $\text{Mg}^{2+}$ sites, three $\text{Mg}^{2+}$ cations (charge $+6$) must be replaced:
  $$2\,\text{Al}^{3+} \xrightarrow{\text{in MgO}} 2\,\text{Al}_{\text{Mg}}^{\bullet} + V_{\text{Mg}}''$$
  In chemical equilibrium notation [Slide 21]:
  $$3\,\text{Mg}^{2+} \longleftrightarrow 2\,\text{Al}^{3+} + 1\text{ cation vacancy of }\text{Mg}^{2+}$$
* **Consequence:** For each mole of $\text{Al}_2\text{O}_3$ dissolved, exactly **$1\text{ mol}$ of $\text{Mg}^{2+}$ cation vacancies** is generated. This produces a measurable reduction of the bulk density and an increase in cation diffusion at high temperature.

---

## 🔀 4. Order-Disorder Phenomenon in Alloys

In substitutional solid solutions with elements of similar electronegativity, the distribution of the solute atoms depends critically on temperature [Slide 23]:

* **Disordered State ($T > T_c$):**
  At high temperatures, the **entropic** term $-T\Delta S$ (not an enthalpic one: $\Delta S$ is the mixing entropy and $\Delta G = \Delta H - T\Delta S$) dominates the free energy. *(Erratum: an earlier version called this term enthalpic.)* Solute and solvent atoms are distributed completely at random on any lattice site.
* **Ordered State ($T < T_c$):**
  On cooling below a critical temperature $T_c$, the slight energetic preference of heteronuclear bonds ($A-B$) over homonuclear ones ($A-A$ and $B-B$) causes the atoms to migrate to specific periodic crystal sublattices (superlattice).

### Paradigmatic Case: Copper-Gold Alloy ($\text{Cu}_3\text{Au}$ or $\text{Cu-Au}$) [Slide 23]:
* At $T > 390^\circ\text{C}$: Disordered FCC lattice (Cu and Au atoms occupy the corners and face centers indiscriminately, with probability according to their mole fraction).
* At $T < 390^\circ\text{C}$: Chemically ordered FCC lattice: the $\text{Au}$ atoms occupy exclusively the **8 corners**, while the $\text{Cu}$ atoms sit at the **6 face centers**.

---
*Bidirectional Links:*
* [[Concept - Point Defects, Thermal Vacancies, Schottky and Frenkel|⬅️ Previous: Point Defects]]
* [[Concept - Dislocations, Burgers Vector and Slip in Metals|Next: Dislocations and Slip ➡️]]
