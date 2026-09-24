---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 4"
dificultad: media
tags:
  - problema-oficial
  - resuelto
  - hume-rothery
  - iron-alloys
  - solubility
  - solid-solutions
---

# ✏️ Problema: T2-DEF04 — Ordenamiento de Solubilidad en Hierro por Reglas de Hume-Rothery

## 📄 Enunciado Oficial
> **4. Using data in the table below, order the elements according to their solubility in iron, from higher to lower solubility. Justify your answer.**  
> *(Solution: $\text{Mo} > \text{Ni} > \text{Mn}$)*
> 
> | Element | Atomic radius (nm) | Crystalline Structure | Electronegativity | Valence |
> | :--- | :---: | :---: | :---: | :---: |
> | **Iron (Fe)** | $0.124$ | **BCC** | $1.7$ | $+2, +3$ |
> | **Nickel (Ni)** | $0.125$ | **FCC** | $1.8$ | $+2$ |
> | **Molybdenum (Mo)** | $0.136$ | **BCC** | $1.3$ | $+3, +4, +6$ |
> | **Manganese (Mn)** | $0.112$ | **Simple cubic** | $1.6$ | $+2, +3, +6, +7$ |

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Matriz Disolvente:
* **Hierro ($\alpha\text{-Fe}$):**
  * Radio atómico: $R_{\text{Fe}} = 0.124\text{ nm}$.
  * Red cristalina: **BCC**.
  * Electronegatividad de Pauling: $\chi_{\text{Fe}} = 1.7$.
  * Valencias estables: $+2, +3$.

### Solutos a Evaluar:
1. **Níquel ($\text{Ni}$):** $R = 0.125\text{ nm}$, FCC, $\chi = 1.8$, Val = $+2$.
2. **Molibdeno ($\text{Mo}$):** $R = 0.136\text{ nm}$, BCC, $\chi = 1.3$, Val = $+3, +4, +6$.
3. **Manganeso ($\text{Mn}$):** $R = 0.112\text{ nm}$, Simple Cúbica, $\chi = 1.6$, Val = $+2, +3, +6, +7$.

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

La solubilidad sólida en disoluciones sustitucionales se rige por las **4 reglas de Hume-Rothery** [Session 4 Slide 22]:

1. **Diferencia de radio atómico ($\Delta R$):** Debe ser inferior al $15\%$ para solubilidad apreciable:
   $$\Delta R = \frac{|R_{\text{soluto}} - R_{\text{Fe}}|}{R_{\text{Fe}}} \times 100\%$$
2. **Estructura cristalina:** Soluto y matriz deben compartir la **misma estructura de red**. Si difieren (p. ej. BCC vs FCC o SC), la solubilidad total es físicamente imposible.
3. **Electronegatividad:** La diferencia $|\Delta \chi|$ debe ser mínima. Diferencias grandes favorecen compuestos intermetálicos en lugar de solución sólida.
4. **Valencia:** Misma valencia o valencia del soluto compatible con los estados de oxidación de la matriz.

---

## 🔢 3. Fase 3: Evaluación Comparativa Rigurosa de Criterios

### 1. Evaluación del Molibdeno ($\text{Mo}$):
* **Diferencia de radio atómico:**
  $$\Delta R_{\text{Mo}} = \frac{|0.136 - 0.124|}{0.124} \times 100\% = \frac{0.012}{0.124} \times 100\% = \mathbf{9.68\%} < 15\% \quad \checkmark$$
* **Estructura cristalina:** **BCC** $\implies$ **Idéntica a la del Hierro ($\alpha\text{-Fe}$)** $\checkmark$ (Factor determinante para amplia solubilidad en ferrita).
* **Electronegatividad:** $\Delta \chi = |1.3 - 1.7| = 0.4$ (moderada).
* **Valencia:** Comparte la valencia común $+3$.
* **Conclusión:** Al tener la **misma red BCC** y cumplir el criterio de tamaño con holgura ($\approx 9.7\%$), el $\text{Mo}$ es un estabilizador ferrítico con muy alta solubilidad en $\alpha\text{-Fe}$ en estado sólido.

---

### 2. Evaluación del Níquel ($\text{Ni}$):
* **Diferencia de radio atómico:**
  $$\Delta R_{\text{Ni}} = \frac{|0.125 - 0.124|}{0.124} \times 100\% = \frac{0.001}{0.124} \times 100\% = \mathbf{0.81\%} \ll 15\% \quad \checkmark$$
  *(Casi idéntico tamaño atómico).*
* **Estructura cristalina:** **FCC** $\neq$ **BCC** $\times$ (Diferente estructura cristalina).
* **Electronegatividad:** $\Delta \chi = |1.8 - 1.7| = 0.1$ (óptima similitud).
* **Valencia:** Comparte la valencia $+2$.
* **Conclusión:** Aunque cumple de forma insuperable tamaño ($0.8\%$) y electronegatividad, su estructura cristalina es **FCC** (es un estabilizador austenítico $\gamma$). Por no coincidir la red, su solubilidad en $\alpha\text{-Fe}$ (BCC) es inferior a la del Molibdeno, pero superior a la del Manganeso.

---

### 3. Evaluación del Manganeso ($\text{Mn}$):
* **Diferencia de radio atómico:**
  $$\Delta R_{\text{Mn}} = \frac{|0.112 - 0.124|}{0.124} \times 100\% = \frac{0.012}{0.124} \times 100\% = \mathbf{9.68\%} < 15\% \quad \checkmark$$
* **Estructura cristalina:** **Cúbica Simple (SC)** $\neq$ **BCC** $\times$. La red cúbica simple presenta un empaquetamiento muy bajo ($\text{APF} = 0.52$) y coordinación $6$, completamente incompatible con la red BCC ($\text{NC}=8$, $\text{APF}=0.68$).
* **Electronegatividad:** $\Delta \chi = |1.6 - 1.7| = 0.1$.
* **Conclusión:** Debido a la discrepancia radical de estructura cristalina con una red cúbica simple atípica, presenta la menor solubilidad relativa en la red BCC del hierro.

---

## 🎯 4. Fase 4: Interpretación Física y Conclusión

### Jerarquía Definitiva de Solubilidad en $\alpha\text{-Fe}$:
$$\mathbf{Mo > Ni > Mn}$$

1. **Molibdeno ($\text{Mo}$):** Es el más soluble porque **comparte la misma estructura cristalina BCC** con el hierro y satisface holgadamente el criterio de tamaño de Hume-Rothery ($\Delta R < 15\%$).
2. **Níquel ($\text{Ni}$):** Ocupa la posición intermedia: sus radios son prácticamente iguales ($\Delta R < 1\%$), pero su estructura **FCC** limita su solubilidad en la ferrita BCC.
3. **Manganeso ($\text{Mn}$):** Presenta la menor solubilidad en la red de hierro debido a su estructura cristalina cúbica simple.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
