---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 5"
dificultad: alta
tags:
  - problema-oficial
  - resuelto
  - non-stoichiometry
  - wustite
  - cationic-vacancies
  - density-variation
---

# ✏️ Problema: T2-DEF05 — Defectos de No Estequiometría y Disminución de Densidad en FeO

## 📄 Enunciado Oficial
> **5. In a specimen of iron oxide (II), $\text{FeO}$, $10\%$ of the $\text{Fe}^{2+}$ ions are substituted by $\text{Fe}^{3+}$ ions. In order to maintain the crystal electro neutrality, a fraction of the cationic positions are vacancies. Data: $M(\text{O}) = 16\text{ g/mol}$; $M(\text{Fe}) = 55.8\text{ g/mol}$.**  
> **a)** Calculate the fraction of cationic vacancies. *(Solution: $0.033\text{ mol vacancies/mol Fe}^{2+}$)*  
> **b)** Assuming that the lattice parameter of the perfect and imperfect crystal is the same, calculate how much the density decreases, in $\%$, with respect to the perfect crystal. *(Solution: $-2.56\%$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Contexto Químico y Físico:
El óxido de hierro (II) ($\text{FeO}$, wüstita) cristaliza en la estructura tipo sal gema ($\text{NaCl}$, FCC) con una subred aniónica compacta de $\text{O}^{2-}$ y una subred catiónica de hierro. En presencia de atmósferas oxidantes, parte de los iones $\text{Fe}^{2+}$ se oxidan a $\text{Fe}^{3+}$.

### Datos de Entrada:
* Substitution: $10\%$ of the original $\text{Fe}^{2+}$ positions are replaced following $3\,\text{Fe}^{2+} \to 2\,\text{Fe}^{3+} + 1\,V_{\text{Fe}}''$.
* Masas molares atómicas:
  * $M_{\text{Fe}} = 55.8\text{ g/mol}$
  * $M_{\text{O}} = 16.0\text{ g/mol}$
* Masa molar de la unidad estequiométrica ideal $\text{FeO}$:
  $$M_{\text{ideal}} = 55.8 + 16.0 = 71.8\text{ g/mol}$$
* Hipótesis geométrica: El parámetro de red $a$ se mantiene invariable entre el cristal perfecto y el defectuoso ($V_C^{\text{real}} = V_C^{\text{ideal}}$).

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

1. **Principio de Electroneutralidad [Session 4 Slide 21]:**
   Cada ion $\text{Fe}^{3+}$ aporta un exceso de carga $+1$ respecto a la posición normal $\text{Fe}^{2+}$. Para preservar la neutralidad eléctrica global:
   $$3\,\text{Fe}^{2+} \longrightarrow 2\,\text{Fe}^{3+} + 1\,V_{\text{Fe}}''$$
   Por cada $2$ iones $\text{Fe}^{3+}$ presentes, debe crearse exactamente **$1$ vacante catiónica de hierro**.
2. **Fracción de Vacantes Catiónicas:**
   Basis: $1\text{ mol}$ of cation sites of the perfect crystal ($1\text{ mol}$ of $\text{Fe}^{2+}$, with $1\text{ mol}$ of $\text{O}^{2-}$, total anionic charge $-2$).
   The replacement of $10\%$ of the $\text{Fe}^{2+}$ positions follows the reaction $3\,\text{Fe}^{2+} \to 2\,\text{Fe}^{3+} + 1\,V_{\text{Fe}}''$, so every $3$ replaced ions give $1$ vacancy; this is the single rule used in part a).
3. **Variación Porcentual de la Densidad:**
   Dado que el volumen reticular $V_C$ es constante, la densidad es estrictamente proporcional a la masa molar efectiva por unidad de fórmula:
   $$\frac{\Delta \rho}{\rho_0} = \frac{M_{\text{real}} - M_{\text{ideal}}}{M_{\text{ideal}}} \times 100\%$$

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### 1. Apartado a: Fracción de Vacantes Catiónicas
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

### 2. Apartado b: Variación Porcentual de la Densidad
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

## 🎯 4. Fase 4: Interpretación Física y Verificación

* **Fenómeno de la Wüstita:** El $\text{FeO}$ prácticamente nunca existe con estequiometría exacta $1:1$ a temperatura ambiente; siempre se presenta como una fase no estequiométrica deficitaria en hierro $\text{Fe}_{1-x}\text{O}$ ($0.05 \le x \le 0.15$). La presencia de vacantes catiónicas $V_{\text{Fe}}''$ reduce su densidad macroscópica (en este problema, $\approx -2.6\%$) y dota al material de propiedades de semiconductor tipo $p$.

---
*Retorno:* [[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]] | [[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]
