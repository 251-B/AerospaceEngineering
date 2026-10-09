---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 10"
dificultad: high
tags:
  - official-problem
  - solved
  - mgo
  - al2o3
  - cationic-vacancies
  - density-variation
  - solid-solutions
---

# ✏️ Problem: T2-DEF10 — MgO-Al₂O₃ Solid Solution: Vacancies and Density Variation

## 📄 Official Statement
> **10. Starting from a perfect $\text{MgO}$ crystal, a solid solution of $\text{Al}_2\text{O}_3$ and $\text{MgO}$ is prepared with an atomic proportion of $15:85$ of $\text{Al}:\text{Mg}$. Calculate:**  
> **a)** The number of vacancies for each $\text{Mg}$ atom. *(Solution: $0.088\text{ vacancies / atoms Mg}$)*  
> **b)** The $\%$ variation of density. *(Solution: $-3\%$)*  
> **Data:** Atomic masses: $\text{Al} = 26.98\text{ g/mol}$; $\text{Mg} = 24.31\text{ g/mol}$; $\text{O} = 16.00\text{ g/mol}$.

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Input Data:
* Starting matrix: Pure, perfect $\text{MgO}$ crystal (FCC rock-salt type lattice with an $\text{Mg}^{2+}$ sublattice and an $\text{O}^{2-}$ sublattice).
* Atomic proportion of cations in the solid solution:
  $$N_{\text{Al}} : N_{\text{Mg}} = 15 : 85$$
* Molar masses:
  * $M_{\text{Al}} = 26.98\text{ g/mol}$
  * $M_{\text{Mg}} = 24.31\text{ g/mol}$
  * $M_{\text{O}} = 16.00\text{ g/mol}$

### Starting Hypotheses:
1. The $\text{Al}^{3+}$ cations substitute for $\text{Mg}^{2+}$ cations in the cation sublattice.
2. To maintain strict electroneutrality, every $2$ $\text{Al}^{3+}$ ions incorporated generate $1$ magnesium cationic vacancy ($V_{\text{Mg}}''$) [Session 4 Slide 21].
3. The oxygen anion sublattice $\text{O}^{2-}$ remains complete and free of anion vacancies.
4. The unit cell volume hardly changes because of the similarity between the radii of $\text{Al}^{3+}$ ($0.053\text{ nm}$) and $\text{Mg}^{2+}$ ($0.072\text{ nm}$), so the density variation is evaluated through the effective mass per lattice site.

---

## 🧠 2. Phase 2: Frames and Change of Basis

1. **Cationic Vacancy Balance [Session 4 Slide 21]:**
   $$3\,\text{Mg}^{2+} \longleftrightarrow 2\,\text{Al}^{3+} + 1\,V_{\text{Mg}}''$$
   For each $\text{Al}^{3+}$ atom incorporated, exactly $\frac{1}{2}$ cationic vacancy is generated:
   $$N_{\text{vacantes}} = \frac{1}{2} N_{\text{Al}}$$
   The number of vacancies per $\text{Mg}$ atom present is:
   $$\text{Vacantes por átomo de Mg} = \frac{N_{\text{vac}}}{N_{\text{Mg}}} = \frac{\frac{1}{2} N_{\text{Al}}}{N_{\text{Mg}}} = \frac{N_{\text{Al}}}{2\, N_{\text{Mg}}}$$

2. **Density Variation Calculation:**
   Taking as a basis a set of $85$ $\text{Mg}$ atoms and $15$ $\text{Al}$ atoms:
   * Number of cationic vacancies: $N_{\text{vac}} = 15 / 2 = 7.5\text{ vacantes}$.
   * Total sites of the cation sublattice: $N_{\text{sitios catiónicos}} = 85 + 15 + 7.5 = 107.5\text{ sitios}$.
   * Since in the $\text{NaCl}$ structure the anion sublattice has exactly the same number of sites as the cation sublattice:
     $$N_{\text{átomos de O}} = N_{\text{sitios catiónicos}} = 107.5\text{ átomos de O}$$
     *(Charge check: Positive charges $= 85 \times (+2) + 15 \times (+3) = 170 + 45 = +215$. Negative charges $= 107.5 \times (-2) = -215$. Net charge $= 0$).*
   * The mean molar mass per cation site unit in the imperfect crystal is:
     $$\bar{M}_{\text{real}} = \frac{85 \cdot M_{\text{Mg}} + 15 \cdot M_{\text{Al}} + 107.5 \cdot M_{\text{O}}}{107.5}$$
   * In the perfect crystal of pure $\text{MgO}$, the mass per cation site is:
     $$\bar{M}_{\text{ideal}} = M_{\text{Mg}} + M_{\text{O}} = 24.31 + 16.00 = 40.31\text{ g/mol}$$
   * Percentage variation:
     $$\frac{\Delta \rho}{\rho_0} = \frac{\bar{M}_{\text{real}} - \bar{M}_{\text{ideal}}}{\bar{M}_{\text{ideal}}} \times 100\%$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Part a: Number of Vacancies per Mg Atom
Taking the atomic proportion $N_{\text{Al}} = 15$ and $N_{\text{Mg}} = 85$:
$$N_{\text{vac}} = \frac{N_{\text{Al}}}{2} = \frac{15}{2} = 7.5\text{ vacantes}$$
Ratio with respect to the number of $\text{Mg}$ atoms:
$$\frac{N_{\text{vac}}}{N_{\text{Mg}}} = \frac{7.5}{85} = \mathbf{0.088235\text{ vacantes / átomo Mg}} \approx \mathbf{0.088\text{ vac/at Mg}}$$

---

### 2. Part b: Percentage Density Variation
* **Total mass of the mixture per $107.5$ cation sites:**
  $$m_{\text{Mg}} = 85 \times 24.31\text{ g/mol} = 2066.35\text{ g}$$
  $$m_{\text{Al}} = 15 \times 26.98\text{ g/mol} = 404.70\text{ g}$$
  $$m_{\text{O}} = 107.5 \times 16.00\text{ g/mol} = 1720.00\text{ g}$$
  $$m_{\text{total, real}} = 2066.35 + 404.70 + 1720.00 = 4191.05\text{ g}$$
* Mean mass per $\text{MgO}$ lattice site:
  $$\bar{M}_{\text{real}} = \frac{4191.05\text{ g}}{107.5\text{ sitios}} = 38.9865\text{ g/mol}$$

* **Mass of $107.5$ units of pure perfect $\text{MgO}$:**
  $$m_{\text{total, ideal}} = 107.5 \times (24.31 + 16.00) = 107.5 \times 40.31 = 4333.325\text{ g}$$
  $$\bar{M}_{\text{ideal}} = 40.31\text{ g/mol}$$

* **Percentage Density Variation:**
  $$\frac{\Delta \rho}{\rho_0} = \frac{\bar{M}_{\text{real}} - \bar{M}_{\text{ideal}}}{\bar{M}_{\text{ideal}}} \times 100\% = \frac{38.9865 - 40.31}{40.31} \times 100\%$$
  $$\frac{\Delta \rho}{\rho_0} = \frac{-1.3235}{40.31} \times 100\% = \mathbf{-3.28\%} \approx \mathbf{-3.3\%}$$

> [!warning] Discrepancy with the official solution
> The official key states $-3\%$. The computed value is $-3.28\%$; the key agrees only to one significant figure, so it is quoted as $-3.3\%$ rather than forced to $-3\%$.

---

## 🎯 4. Phase 4: Units and Limits

* **Origin of the Density Loss:** Even though the $\text{Al}^{3+}$ cation ($M_{\text{Al}} = 26.98\text{ g/mol}$) is slightly heavier than $\text{Mg}^{2+}$ ($M_{\text{Mg}} = 24.31\text{ g/mol}$), the need to neutralise the extra charge leaves $7.5$ of the $107.5$ cation sites ($7\%$) as vacancies, which produces an overall mass deficit and a **net reduction of $\approx 3.3\%$ in the volumetric density** of the ceramic material.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
