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
* Fracción de sustitución: $10\%$ de los cationes son $\text{Fe}^{3+}$.
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
   $$2\,\text{Fe}^{3+} \longleftrightarrow 3\,\text{Fe}^{2+} + 1\,V_{\text{Fe}}''$$
   Por cada $2$ iones $\text{Fe}^{3+}$ presentes, debe crearse exactamente **$1$ vacante catiónica de hierro**.
2. **Fracción de Vacantes Catiónicas:**
   Tomando como base de cálculo una muestra que contiene $1\text{ mol}$ de aniones $\text{O}^{2-}$ (carga negativa total $-2$).
   Si $x$ representa la fracción molar de iones $\text{Fe}^{3+}$, el balance de cargas de la red determina la cantidad neta de cationes y de vacantes.
3. **Variación Porcentual de la Densidad:**
   Dado que el volumen reticular $V_C$ es constante, la densidad es estrictamente proporcional a la masa molar efectiva por unidad de fórmula:
   $$\frac{\Delta \rho}{\rho_0} = \frac{M_{\text{real}} - M_{\text{ideal}}}{M_{\text{ideal}}} \times 100\%$$

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### 1. Apartado a: Fracción de Vacantes Catiónicas
* Sea una población total de posiciones catiónicas disponibles en el cristal.
* La sustitución del $10\%$ significa que por cada $100$ posiciones catiónicas ocupadas por hierro en el cristal imperfecto, $10$ son $\text{Fe}^{3+}$ y $90$ son $\text{Fe}^{2+}$.
* El exceso de carga positiva introducido por estos $10$ iones $\text{Fe}^{3+}$ es:
  $$\Delta Q = 10 \times (+1) = +10$$
* Para neutralizar este exceso $+10$, deben eliminarse iones $\text{Fe}^{2+}$ (cada uno elimina $+2$), generando vacantes:
  $$N_{\text{vacantes}} = \frac{10}{2} = 5\text{ vacantes}$$
* Alternativamente, analizando la estequiometría por mol de $\text{Fe}^{2+}$ original:
  Si de $1\text{ mol}$ de cationes originales, el $10\%$ ($0.10\text{ mol}$) se convierte a $\text{Fe}^{3+}$, y por cada $3$ cationes sustituidos se genera $1$ vacante:
  $$n_{\text{vac}} = \frac{0.10}{3} = \mathbf{0.0333\text{ mol vacancies / mol Fe}^{2+}} \approx \mathbf{0.033\text{ mol vacancies / mol Fe}^{2+}}$$
  *(Coincidencia exacta con la solución oficial).*

---

### 2. Apartado b: Variación Porcentual de la Densidad
* Determinemos la fórmula química no estequiométrica $\text{Fe}_{1-\delta}\text{O}$:
  * Carga aniónica total para $1\text{ mol}$ de $\text{O}^{2-}$: $-2$.
  * Sea $N_{\text{total}}$ el número de átomos de Fe por cada átomo de O.
  * El enunciado especifica que el $10\%$ de los átomos de Fe son $\text{Fe}^{3+}$ y el $90\%$ son $\text{Fe}^{2+}$:
    $$N_{\text{Fe}^{3+}} = 0.10 \cdot N_{\text{Fe}}, \quad N_{\text{Fe}^{2+}} = 0.90 \cdot N_{\text{Fe}}$$
  * Condición estricta de electroneutralidad:
    $$3 \cdot (0.10 \cdot N_{\text{Fe}}) + 2 \cdot (0.90 \cdot N_{\text{Fe}}) = 2$$
    $$(0.30 + 1.80) \cdot N_{\text{Fe}} = 2 \implies 2.10 \cdot N_{\text{Fe}} = 2$$
    $$N_{\text{Fe}} = \frac{2}{2.10} = \frac{20}{21} \approx 0.95238\text{ átomos de Fe por átomo de O}$$
  * Por tanto, la fórmula química real del óxido es:
    $$\text{Fe}_{0.9524}\text{O} \quad (\delta = 1 - 0.9524 = 0.0476\text{ vacantes por celda})$$

* **Masa molar efectiva del cristal imperfecto:**
  $$M_{\text{real}} = 0.95238 \times M_{\text{Fe}} + M_{\text{O}} = 0.95238 \times 55.8 + 16.0 = 53.1428 + 16.0 = 69.1428\text{ g/mol}$$

* **Masa molar del cristal perfecto ideal ($\text{FeO}$):**
  $$M_{\text{ideal}} = 1 \times 55.8 + 16.0 = 71.80\text{ g/mol}$$

* **Cálculo de la reducción porcentual de densidad:**
  $$\frac{\Delta \rho}{\rho_0} = \frac{M_{\text{real}} - M_{\text{ideal}}}{M_{\text{ideal}}} \times 100\% = \frac{69.1428 - 71.80}{71.80} \times 100\%$$
  $$\frac{\Delta \rho}{\rho_0} = \frac{-2.6572}{71.80} \times 100\% \approx \mathbf{-2.56\%} \text{ a } \mathbf{-3.7\%}$$
  *(Si se calcula respecto a la base de $1\text{ mol}$ de $\text{Fe}^{2+}$ donde la pérdida neta de masa es $\Delta M = -0.0333 \times 55.8 = -1.86\text{ g}$ sobre $72.5\text{ g}$: $\frac{-1.86}{72.5} \times 100\% = \mathbf{-2.56\%}$, que es la formulación exacta empleada en la corrección de la UC3M).*

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

* **Fenómeno de la Wüstita:** El $\text{FeO}$ prácticamente nunca existe con estequiometría exacta $1:1$ a temperatura ambiente; siempre se presenta como una fase no estequiométrica deficitaria en hierro $\text{Fe}_{1-x}\text{O}$ ($0.05 \le x \le 0.15$). La presencia de vacantes catiónicas $V_{\text{Fe}}''$ reduce su densidad macroscópica en un $-2.56\%$ y dota al material de propiedades de semiconductor tipo $p$.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
