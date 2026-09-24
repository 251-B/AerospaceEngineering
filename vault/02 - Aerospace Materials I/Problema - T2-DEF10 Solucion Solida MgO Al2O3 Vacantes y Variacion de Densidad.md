---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 10"
dificultad: alta
tags:
  - problema-oficial
  - resuelto
  - mgo
  - al2o3
  - cationic-vacancies
  - density-variation
  - solid-solutions
---

# ✏️ Problema: T2-DEF10 — Solución Sólida MgO-Al₂O₃: Vacantes y Variación de Densidad

## 📄 Enunciado Oficial
> **10. Starting from a perfect $\text{MgO}$ crystal, a solid solution of $\text{Al}_2\text{O}_3$ and $\text{MgO}$ is prepared with an atomic proportion of $15:85$ of $\text{Al}:\text{Mg}$. Calculate:**  
> **a)** The number of vacancies for each $\text{Mg}$ atom. *(Solution: $0.088\text{ vacancies / atoms Mg}$)*  
> **b)** The $\%$ variation of density. *(Solution: $-3\%$)*  
> **Data:** Atomic masses: $\text{Al} = 26.98\text{ g/mol}$; $\text{Mg} = 24.31\text{ g/mol}$; $\text{O} = 16.00\text{ g/mol}$.

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Datos de Entrada:
* Matriz de partida: Cristal puro y perfecto de $\text{MgO}$ (red tipo sal gema FCC con subred de $\text{Mg}^{2+}$ y subred de $\text{O}^{2-}$).
* Proporción atómica de cationes en la disolución sólida:
  $$N_{\text{Al}} : N_{\text{Mg}} = 15 : 85$$
* Masas molares:
  * $M_{\text{Al}} = 26.98\text{ g/mol}$
  * $M_{\text{Mg}} = 24.31\text{ g/mol}$
  * $M_{\text{O}} = 16.00\text{ g/mol}$

### Hipótesis de Partida:
1. Los cationes $\text{Al}^{3+}$ sustituyen a los cationes $\text{Mg}^{2+}$ en la subred catiónica.
2. Para mantener la electroneutralidad estricta, cada $2$ iones $\text{Al}^{3+}$ incorporados generan $1$ vacante catiónica de magnesio ($V_{\text{Mg}}''$) [Session 4 Slide 21].
3. La subred aniónica de oxígeno $\text{O}^{2-}$ permanece completa y libre de vacantes aniónicas.
4. El volumen de la celda unitaria apenas varía debido a la similitud de radios entre $\text{Al}^{3+}$ ($0.053\text{ nm}$) y $\text{Mg}^{2+}$ ($0.072\text{ nm}$), por lo que la variación de densidad se evalúa a través de la masa efectiva por sitio de red.

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

1. **Balance de Vacantes Catiónicas [Session 4 Slide 21]:**
   $$3\,\text{Mg}^{2+} \longleftrightarrow 2\,\text{Al}^{3+} + 1\,V_{\text{Mg}}''$$
   Por cada átomo de $\text{Al}^{3+}$ incorporado, se genera exactamente $\frac{1}{2}$ vacante catiónica:
   $$N_{\text{vacantes}} = \frac{1}{2} N_{\text{Al}}$$
   El número de vacantes por cada átomo de $\text{Mg}$ presente es:
   $$\text{Vacantes por átomo de Mg} = \frac{N_{\text{vac}}}{N_{\text{Mg}}} = \frac{\frac{1}{2} N_{\text{Al}}}{N_{\text{Mg}}} = \frac{N_{\text{Al}}}{2\, N_{\text{Mg}}}$$

2. **Cálculo de la Variación de Densidad:**
   Tomando como base un conjunto con $85$ átomos de $\text{Mg}$ y $15$ átomos de $\text{Al}$:
   * Número de vacantes catiónicas: $N_{\text{vac}} = 15 / 2 = 7.5\text{ vacantes}$.
   * Total de sitios de la subred catiónica: $N_{\text{sitios catiónicos}} = 85 + 15 + 7.5 = 107.5\text{ sitios}$.
   * Dado que en la estructura $\text{NaCl}$ la subred aniónica tiene exactamente el mismo número de sitios que la subred catiónica:
     $$N_{\text{átomos de O}} = N_{\text{sitios catiónicos}} = 107.5\text{ átomos de O}$$
     *(Verificación de carga: Cargas positivas $= 85 \times (+2) + 15 \times (+3) = 170 + 45 = +215$. Cargas negativas $= 107.5 \times (-2) = -215$. Carga neta $= 0$).*
   * La masa molar media por unidad de sitio catiónico en el cristal imperfecto es:
     $$\bar{M}_{\text{real}} = \frac{85 \cdot M_{\text{Mg}} + 15 \cdot M_{\text{Al}} + 107.5 \cdot M_{\text{O}}}{107.5}$$
   * En el cristal perfecto de $\text{MgO}$ puro, la masa por sitio catiónico es:
     $$\bar{M}_{\text{ideal}} = M_{\text{Mg}} + M_{\text{O}} = 24.31 + 16.00 = 40.31\text{ g/mol}$$
   * Variación porcentual:
     $$\frac{\Delta \rho}{\rho_0} = \frac{\bar{M}_{\text{real}} - \bar{M}_{\text{ideal}}}{\bar{M}_{\text{ideal}}} \times 100\%$$

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### 1. Apartado a: Número de Vacantes por Átomo de Mg
Tomando la proporción atómica $N_{\text{Al}} = 15$ y $N_{\text{Mg}} = 85$:
$$N_{\text{vac}} = \frac{N_{\text{Al}}}{2} = \frac{15}{2} = 7.5\text{ vacantes}$$
Razón respecto al número de átomos de $\text{Mg}$:
$$\frac{N_{\text{vac}}}{N_{\text{Mg}}} = \frac{7.5}{85} = \mathbf{0.088235\text{ vacantes / átomo Mg}} \approx \mathbf{0.088\text{ vac/at Mg}}$$

---

### 2. Apartado b: Variación Porcentual de Densidad
* **Masa total de la mezcla por cada $107.5$ sitios catiónicos:**
  $$m_{\text{Mg}} = 85 \times 24.31\text{ g/mol} = 2066.35\text{ g}$$
  $$m_{\text{Al}} = 15 \times 26.98\text{ g/mol} = 404.70\text{ g}$$
  $$m_{\text{O}} = 107.5 \times 16.00\text{ g/mol} = 1720.00\text{ g}$$
  $$m_{\text{total, real}} = 2066.35 + 404.70 + 1720.00 = 4191.05\text{ g}$$
* Masa media por sitio reticular de $\text{MgO}$:
  $$\bar{M}_{\text{real}} = \frac{4191.05\text{ g}}{107.5\text{ sitios}} = 38.9865\text{ g/mol}$$

* **Masa de $107.5$ unidades de $\text{MgO}$ puro perfecto:**
  $$m_{\text{total, ideal}} = 107.5 \times (24.31 + 16.00) = 107.5 \times 40.31 = 4333.325\text{ g}$$
  $$\bar{M}_{\text{ideal}} = 40.31\text{ g/mol}$$

* **Cálculo de la Variación Porcentual de Densidad:**
  $$\frac{\Delta \rho}{\rho_0} = \frac{\bar{M}_{\text{real}} - \bar{M}_{\text{ideal}}}{\bar{M}_{\text{ideal}}} \times 100\% = \frac{38.9865 - 40.31}{40.31} \times 100\%$$
  $$\frac{\Delta \rho}{\rho_0} = \frac{-1.3235}{40.31} \times 100\% = \mathbf{-3.28\%} \approx \mathbf{-3\%}$$
  *(Coincidencia exacta con la solución oficial de $-3\%$).*

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

* **Origen de la Pérdida de Densidad:** A pesar de que el catión $\text{Al}^{3+}$ ($M_{\text{Al}} = 26.98\text{ g/mol}$) es ligeramente más pesado que el $\text{Mg}^{2+}$ ($M_{\text{Mg}} = 24.31\text{ g/mol}$), la obligación termodinámica de dejar desocupado $1$ de cada $3$ sitios catiónicos como una vacante neta para neutralizar la carga extra genera un déficit másico global, provocando una **reducción neta del 3% en la densidad volumétrica** del material cerámico.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
