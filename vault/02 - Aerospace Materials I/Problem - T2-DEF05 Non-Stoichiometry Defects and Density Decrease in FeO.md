---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 5"
dificultad: high
tags:
  - official-problem
  - solved
  - non-stoichiometry
  - wustite
  - cationic-vacancies
  - density-variation
---

# ✏️ Problem: T2-DEF05: Non-Stoichiometry Defects and Density Decrease in FeO

## 📄 Official Statement
> **5. In a specimen of iron oxide (II), $\text{FeO}$, $10\%$ of the $\text{Fe}^{2+}$ ions are substituted by $\text{Fe}^{3+}$ ions. In order to maintain the crystal electro neutrality, a fraction of the cationic positions are vacancies. Data: $M(\text{O}) = 16\text{ g/mol}$; $M(\text{Fe}) = 55.8\text{ g/mol}$.**  
> **a)** Calculate the fraction of cationic vacancies. *(Solution: $0.033\text{ mol vacancies/mol Fe}^{2+}$)*  
> **b)** Assuming that the lattice parameter of the perfect and imperfect crystal is the same, calculate how much the density decreases, in $\%$, with respect to the perfect crystal. *(Solution: $-2.56\%$)*

---

## 📊 1. Phase 1: Hypotheses and Parameters

### Chemical and Physical Context:
Iron(II) oxide ($\text{FeO}$, wüstite) crystallises in the rock-salt structure ($\text{NaCl}$, FCC) with a close-packed anionic sublattice of $\text{O}^{2-}$ and a cationic iron sublattice. In oxidising atmospheres, part of the $\text{Fe}^{2+}$ ions oxidise to $\text{Fe}^{3+}$.

### Input Data:
* Substitution: $10\%$ of the original $\text{Fe}^{2+}$ positions are replaced following $3\,\text{Fe}^{2+} \to 2\,\text{Fe}^{3+} + 1\,V_{\text{Fe}}''$.
* Atomic molar masses:
  * $M_{\text{Fe}} = 55.8\text{ g/mol}$
  * $M_{\text{O}} = 16.0\text{ g/mol}$
* Molar mass of the ideal stoichiometric $\text{FeO}$ unit:
  $$M_{\text{ideal}} = 55.8 + 16.0 = 71.8\text{ g/mol}$$
* Geometric hypothesis: the lattice parameter $a$ is the same for the perfect and the defective crystal ($V_C^{\text{real}} = V_C^{\text{ideal}}$).

---

## 🧠 2. Phase 2: Formulation and Justification

1. **Electroneutrality principle [Session 4 Slide 21]:**
   Each $\text{Fe}^{3+}$ ion carries an excess charge of $+1$ relative to the normal $\text{Fe}^{2+}$ position. To preserve global electrical neutrality:
   $$3\,\text{Fe}^{2+} \longrightarrow 2\,\text{Fe}^{3+} + 1\,V_{\text{Fe}}''$$
   For every $2$ $\text{Fe}^{3+}$ ions present, exactly **$1$ cationic iron vacancy** must be created.
2. **Cationic vacancy fraction:**
   Basis: $1\text{ mol}$ of cation sites of the perfect crystal ($1\text{ mol}$ of $\text{Fe}^{2+}$, with $1\text{ mol}$ of $\text{O}^{2-}$, total anionic charge $-2$).
   The replacement of $10\%$ of the $\text{Fe}^{2+}$ positions follows the reaction $3\,\text{Fe}^{2+} \to 2\,\text{Fe}^{3+} + 1\,V_{\text{Fe}}''$, so every $3$ replaced ions give $1$ vacancy; this is the single rule used in part a).
3. **Percentage density change:**
   Since the lattice volume $V_C$ is constant, the density is strictly proportional to the effective molar mass per formula unit:
   $$\frac{\Delta \rho}{\rho_0} = \frac{M_{\text{real}} - M_{\text{ideal}}}{M_{\text{ideal}}} \times 100\%$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Part a: Cationic Vacancy Fraction
* Basis: $1\text{ mol}$ of cation sites of the perfect crystal, i.e. $1\text{ mol}$ of $\text{Fe}^{2+}$ and $1\text{ mol}$ of $\text{O}^{2-}$ (the unit used in the official answer, "mol vacancies/mol $\text{Fe}^{2+}$").
* Reading of the statement: $10\%$ of the original $\text{Fe}^{2+}$ positions are replaced, i.e. $0.10\text{ mol}$ of the original $\text{Fe}^{2+}$ are involved in the reaction
  $$3\,\text{Fe}^{2+} \longrightarrow 2\,\text{Fe}^{3+} + 1\,V_{\text{Fe}}''$$
* Check of the reaction: sites $3 = 2 + 1$; charge $3\times(+2) = 2\times(+3) + 0 = +6$ (the vacancy carries no ion).
* Every $3$ replaced $\text{Fe}^{2+}$ produce $1$ vacancy, hence for $0.10\text{ mol}$ of replaced $\text{Fe}^{2+}$:
  $$n_{\text{vac}} = \frac{0.10}{3} = 0.03333\text{ mol} \approx \mathbf{0.033\text{ mol vacancies / mol Fe}^{2+}}$$
* Resulting populations (per mol of original cation sites): $n_{\text{Fe}^{3+}} = 2\,n_{\text{vac}} = 0.06667$; $n_{\text{Fe}^{2+}} = 1 - 0.10 = 0.90$; $n_{\text{vac}} = 0.03333$.
* Checks: sites $0.90 + 0.06667 + 0.03333 = 1.000$; charge $0.90\times 2 + 0.06667\times 3 = 1.800 + 0.200 = +2.000$, equal in magnitude to the anionic charge of $1\text{ mol}$ of $\text{O}^{2-}$ ($-2$).

Value coincides with the official answer $0.033$.

---

### 2. Part b: Percentage Density Change
* Fe atoms per formula unit (per $\text{O}$): $0.90 + 0.06667 = 0.96667$, i.e. the crystal is $\text{Fe}_{0.9667}\text{O}$ ($=1 - 0.03333$).
* **Effective molar mass of the defective crystal (per formula unit):**
  $$M_{\text{real}} = 0.96667 \times 55.8 + 16.0 = 53.940 + 16.0 = 69.940\text{ g/mol}$$
* **Molar mass of the perfect crystal:** $M_{\text{ideal}} = 55.8 + 16.0 = 71.80\text{ g/mol}$.
* **Density change** (same cell volume, so $\rho \propto M$ per formula unit):
  $$\frac{\Delta \rho}{\rho_0} = \frac{M_{\text{real}} - M_{\text{ideal}}}{M_{\text{ideal}}} \times 100\% = \frac{69.940 - 71.80}{71.80} \times 100\% = \frac{-1.860}{71.80} \times 100\% = \mathbf{-2.59\%} \approx \mathbf{-2.6\%}$$
  Equivalently, the mass lost is only the vacancies, $\Delta M = -n_{\text{vac}} M_{\text{Fe}} = -0.03333 \times 55.8 = -1.860\text{ g}$ per $71.80\text{ g}$ of perfect $\text{FeO}$.

> [!warning] Discrepancy with the official solution
> The official key gives $-2.56\%$; the value obtained from the stated data ($M_{\text{Fe}} = 55.8$, $M_{\text{O}} = 16$) is $-2.59\%$. The difference ($0.03$ percentage points) cannot be traced to any rounding of the given constants, so the official figure is not reproduced and no data were altered. A different reading of the statement (10% of the Fe ions of the final crystal being $\text{Fe}^{3+}$) would give $0.0476$ vacancies per formula unit and $-3.7\%$, which matches neither official value and is therefore not used.

---

## 🎯 4. Phase 4: Physical Interpretation and Verification

* **The wüstite phenomenon:** $\text{FeO}$ practically never exists with exact $1:1$ stoichiometry at room temperature; it always appears as an iron-deficient non-stoichiometric phase $\text{Fe}_{1-x}\text{O}$ ($0.05 \le x \le 0.15$). The cationic vacancies $V_{\text{Fe}}''$ reduce its macroscopic density (in this problem, $\approx -2.6\%$) and give the material $p$-type semiconductor behaviour.

---
*Back to:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
