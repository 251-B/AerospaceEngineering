---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 3"
dificultad: medium
tags:
  - official-problem
  - solved
  - mgo
  - cationic-vacancies
  - charge-compensation
  - solid-solutions
---

# ✏️ Problem: T2-DEF03 — Cationic Vacancies in MgO from the Dissolution of Al₂O₃ and TiO₂

## 📄 Official Statement
> **3. Calculate the number of $\text{Mg}^{2+}$ vacancies produced by the dissolution of:**  
> **a)** $1\text{ mole}$ of $\text{Al}_2\text{O}_3$ in $99\text{ moles}$ of $\text{MgO}$. *(Solution: $0.01\text{ mol vacancies/mol MgO}$)*  
> **b)** $2\text{ moles}$ of $\text{TiO}_2$ in $98\text{ moles}$ of $\text{MgO}$. *(Solution: $0.02\text{ mol vacancies/mol MgO}$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Chemical Context:
The formation of substitutional solid solutions in the ionic ceramic lattice of magnesium oxide ($\text{MgO}$, $\text{NaCl}$-type structure with a cation sublattice of $\text{Mg}^{2+}$ and an anion sublattice of $\text{O}^{2-}$) is studied.

### Fundamental Requirement:
* **Principle of Macroscopic Electroneutrality:** The total positive charge of the incorporated cations must exactly equal the charge of the substituted cations. The valence difference between the dopant cations ($\text{Al}^{3+}$ or $\text{Ti}^{4+}$) and the matrix cation ($\text{Mg}^{2+}$) forces the generation of **cationic vacancies $V_{\text{Mg}}''$** [Session 4 Slide 21].

---

## 🧠 2. Phase 2: Frames and Change of Basis

Citing slide 21 [Session 4 Slide 21]:
$$\text{Generation of defects due to solid solution in Ionic solids: } 3\,\text{Mg}^{2+} \longleftrightarrow 2\,\text{Al}^{3+} + 1\,V_{\text{Mg}}$$

### Electric Charge Balance:
1. **For $\text{Al}_2\text{O}_3$:**
   * Each formula unit of $\text{Al}_2\text{O}_3$ supplies $2$ $\text{Al}^{3+}$ cations (charge $+6$).
   * To house these $2$ cations in the $\text{Mg}^{2+}$ sublattice while maintaining neutrality, $3$ $\text{Mg}^{2+}$ cations (charge $+6$) must be replaced.
   * Since $2$ $\text{Al}^{3+}$ cations occupy $2$ sites of the cation lattice, the third site is left empty as **one cationic vacancy**:
     $$\text{For each mole of }\text{Al}_2\text{O}_3 \implies 1\text{ mole of vacancies } V_{\text{Mg}}$$

2. **For $\text{TiO}_2$:**
   * Each formula unit of $\text{TiO}_2$ supplies $1$ $\text{Ti}^{4+}$ cation (charge $+4$).
   * To balance the charge $+4$, $2$ $\text{Mg}^{2+}$ cations (charge $+4$) must be replaced.
   * Since the $\text{Ti}^{4+}$ cation occupies $1$ cation site, the second site remains as **one cationic vacancy**:
     $$\text{Ti}^{4+} + 2\,\text{Mg}^{2+} \implies \text{Ti}_{\text{Mg}}^{\bullet\bullet} + V_{\text{Mg}}'' \implies \text{For each mole of }\text{TiO}_2 \implies 1\text{ mole of vacancies } V_{\text{Mg}}$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Part a: Dissolution of $1\text{ mol}$ of $\text{Al}_2\text{O}_3$ in $99\text{ moles}$ of $\text{MgO}$
* Moles of cationic vacancies generated:
  $$n_{\text{vacantes}} = 1\text{ mol de }\text{Al}_2\text{O}_3 \times \left(\frac{1\text{ mol } V_{\text{Mg}}}{1\text{ mol }\text{Al}_2\text{O}_3}\right) = 1.0\text{ mol de vacantes}$$
* Amount of substance of the matrix: $n_{\text{MgO}} = 99\text{ moles}$.
* Relative concentration per mole of $\text{MgO}$:
  $$\frac{n_{\text{vacantes}}}{n_{\text{MgO}}} = \frac{1.0\text{ mol vacantes}}{99\text{ moles MgO}} = 0.010101 \approx \mathbf{0.01\text{ mol vacancies / mol MgO}}$$

---

### 2. Part b: Dissolution of $2\text{ moles}$ of $\text{TiO}_2$ in $98\text{ moles}$ of $\text{MgO}$
* Moles of cationic vacancies generated:
  $$n_{\text{vacantes}} = 2\text{ moles de }\text{TiO}_2 \times \left(\frac{1\text{ mol } V_{\text{Mg}}}{1\text{ mol }\text{TiO}_2}\right) = 2.0\text{ moles de vacantes}$$
* Amount of substance of the matrix: $n_{\text{MgO}} = 98\text{ moles}$.
* Relative concentration per mole of $\text{MgO}$:
  $$\frac{n_{\text{vacantes}}}{n_{\text{MgO}}} = \frac{2.0\text{ mol vacantes}}{98\text{ moles MgO}} = 0.020408 \approx \mathbf{0.02\text{ mol vacancies / mol MgO}}$$

---

## 🎯 4. Phase 4: Units and Limits

* **Extrinsic vs Thermal Defects:** Unlike intrinsic thermal vacancies (which depend exponentially on temperature), these vacancies are **extrinsic**: their concentration is strictly fixed by the dopant stoichiometry and remains constant even on cooling to room temperature.
* **Technological Application:** The deliberate introduction of higher-valence cations ($\text{Al}^{3+}, \text{Ti}^{4+}$) generates an enormous fixed population of cationic vacancies, increasing ionic conductivity and accelerating the solid-state sintering rate of refractory aerospace ceramics by orders of magnitude.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
