---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 3"
dificultad: media
tags:
  - problema-oficial
  - resuelto
  - mgo
  - cationic-vacancies
  - charge-compensation
  - solid-solutions
---

# ✏️ Problema: T2-DEF03 — Vacantes Catiónicas en MgO por Disolución de Al₂O₃ y TiO₂

## 📄 Enunciado Oficial
> **3. Calculate the number of $\text{Mg}^{2+}$ vacancies produced by the dissolution of:**  
> **a)** $1\text{ mole}$ of $\text{Al}_2\text{O}_3$ in $99\text{ moles}$ of $\text{MgO}$. *(Solution: $0.01\text{ mol vacancies/mol MgO}$)*  
> **b)** $2\text{ moles}$ of $\text{TiO}_2$ in $98\text{ moles}$ of $\text{MgO}$. *(Solution: $0.02\text{ mol vacancies/mol MgO}$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Contexto Químico:
Se estudia la formación de disoluciones sólidas sustitucionales en la red cerámica iónica del óxido de magnesio ($\text{MgO}$, estructura tipo $\text{NaCl}$ con subred catiónica de $\text{Mg}^{2+}$ y subred aniónica de $\text{O}^{2-}$).

### Requisito Fundamental:
* **Principio de Electroneutralidad Macroscópica:** La carga total positiva de los cationes incorporados debe igualar con exactitud la carga de los cationes sustituidos. La diferencia de valencia entre los cationes dopantes ($\text{Al}^{3+}$ o $\text{Ti}^{4+}$) y el catión matriz ($\text{Mg}^{2+}$) obliga a generar **vacantes catiónicas $V_{\text{Mg}}''$** [Session 4 Slide 21].

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

Citando la diapositiva 21 [Session 4 Slide 21]:
$$\text{Generation of defects due to solid solution in Ionic solids: } 3\,\text{Mg}^{2+} \longleftrightarrow 2\,\text{Al}^{3+} + 1\,V_{\text{Mg}}$$

### Balance de Carga Eléctrica:
1. **Para $\text{Al}_2\text{O}_3$:**
   * Cada unidad fórmula de $\text{Al}_2\text{O}_3$ aporta $2$ cationes $\text{Al}^{3+}$ (carga $+6$).
   * Para alojar estos $2$ cationes en la subred de $\text{Mg}^{2+}$ manteniendo la neutralidad, se deben reemplazar $3$ cationes $\text{Mg}^{2+}$ (carga $+6$).
   * Como $2$ cationes $\text{Al}^{3+}$ ocupan $2$ sitios de la red catiónica, el tercer sitio queda desocupado como **una vacante catiónica**:
     $$\text{Por cada mol de }\text{Al}_2\text{O}_3 \implies 1\text{ mol de vacantes } V_{\text{Mg}}$$

2. **Para $\text{TiO}_2$:**
   * Cada unidad fórmula de $\text{TiO}_2$ aporta $1$ catión $\text{Ti}^{4+}$ (carga $+4$).
   * Para equilibrar la carga $+4$, se deben reemplazar $2$ cationes $\text{Mg}^{2+}$ (carga $+4$).
   * Como el catión $\text{Ti}^{4+}$ ocupa $1$ sitio catiónico, el segundo sitio queda como **una vacante catiónica**:
     $$\text{Ti}^{4+} + 2\,\text{Mg}^{2+} \implies \text{Ti}_{\text{Mg}}^{\bullet\bullet} + V_{\text{Mg}}'' \implies \text{Por cada mol de }\text{TiO}_2 \implies 1\text{ mol de vacantes } V_{\text{Mg}}$$

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### 1. Apartado a: Disolución de $1\text{ mol}$ de $\text{Al}_2\text{O}_3$ en $99\text{ moles}$ de $\text{MgO}$
* Moles de vacantes catiónicas generadas:
  $$n_{\text{vacantes}} = 1\text{ mol de }\text{Al}_2\text{O}_3 \times \left(\frac{1\text{ mol } V_{\text{Mg}}}{1\text{ mol }\text{Al}_2\text{O}_3}\right) = 1.0\text{ mol de vacantes}$$
* Cantidad de sustancia de la matriz: $n_{\text{MgO}} = 99\text{ moles}$.
* Concentración relativa por mol de $\text{MgO}$:
  $$\frac{n_{\text{vacantes}}}{n_{\text{MgO}}} = \frac{1.0\text{ mol vacantes}}{99\text{ moles MgO}} = 0.010101 \approx \mathbf{0.01\text{ mol vacancies / mol MgO}}$$

---

### 2. Apartado b: Disolución de $2\text{ moles}$ de $\text{TiO}_2$ en $98\text{ moles}$ de $\text{MgO}$
* Moles de vacantes catiónicas generadas:
  $$n_{\text{vacantes}} = 2\text{ moles de }\text{TiO}_2 \times \left(\frac{1\text{ mol } V_{\text{Mg}}}{1\text{ mol }\text{TiO}_2}\right) = 2.0\text{ moles de vacantes}$$
* Cantidad de sustancia de la matriz: $n_{\text{MgO}} = 98\text{ moles}$.
* Concentración relativa por mol de $\text{MgO}$:
  $$\frac{n_{\text{vacantes}}}{n_{\text{MgO}}} = \frac{2.0\text{ mol vacantes}}{98\text{ moles MgO}} = 0.020408 \approx \mathbf{0.02\text{ mol vacancies / mol MgO}}$$

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

* **Defectos Extrínsecos vs Térmicos:** A diferencia de las vacantes térmicas intrínsecas (que dependen exponencialmente de la temperatura), estas vacantes son **extrínsecas**: su concentración está estrictamente fijada por la estequiometría del dopante y permanece constante incluso al enfriar a temperatura ambiente.
* **Aplicación Tecnológica:** La introducción deliberada de cationes de valencia superior ($\text{Al}^{3+}, \text{Ti}^{4+}$) genera una enorme población fija de vacantes catiónicas, aumentando la conductividad iónica y acelerando en órdenes de magnitud la velocidad de sinterización en fase sólida de cerámicos aeroespaciales refractarios.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
