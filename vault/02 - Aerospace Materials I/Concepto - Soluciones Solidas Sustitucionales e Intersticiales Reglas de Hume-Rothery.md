---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 4 T2 Structure of Materials II_2025.pdf, Slides 20-24"
tags:
  - teoria
  - concepto-fundamental
  - soluciones-solidas
  - hume-rothery
  - sustitucional
  - intersticial
  - compensacion-carga
  - orden-desorden
dificultad: media
prerrequisitos:
  - "[[Concepto - Defectos Puntuales Vacantes Termicas Schottky y Frenkel]]"
---

# ⚗️ Concepto: Soluciones Sólidas Sustitucionales e Intersticiales y Reglas de Hume-Rothery

> **Definición Formal:** Una **disolución sólida** es un sólido cristalino homogéneo compuesto por dos o más elementos dispersos a nivel atómico en una única fase termodinámica uniforme [Slide 20]. El disolvente (o matriz) mantiene su red cristalina básica mientras que los átomos de soluto se incorporan sustituyendo posiciones de la red o alojándose en los huecos intersticiales.

---

## 🔀 1. Clasificación: Soluciones Sustitucionales vs Intersticiales

1. **Disoluciones Sólidas Sustitucionales:**
   * Los átomos de soluto reemplazan directamente a los átomos de la red matriz en sus nudos regulares [Slide 20].
   * *Ejemplos aeroespaciales:* Níquel disuelto en Cobre ($\text{Cu-Ni}$, solubilidad total isomorfa), Zinc en Cobre (latones), Cromo y Molibdeno en Níquel (superaleaciones Inconel).
2. **Disoluciones Sólidas Intersticiales:**
   * Los átomos de soluto se alojan exclusivamente en los huecos tetraédricos u octaédricos libres de la red disolvente [Slide 20].
   * Solo es posible para elementos con **radios atómicos muy pequeños**:
     $$\text{Hidrógeno (H)}, \quad \text{Carbono (C)}, \quad \text{Nitrógeno (N)}, \quad \text{Boro (B)}$$
   * La solubilidad suele ser muy restringida (p. ej., $< 0.022\text{ wt\%}$ de C en ferrita $\alpha\text{-Fe}$ a $727^\circ\text{C}$).

---

## 📜 2. Las 4 Reglas de Hume-Rothery para Soluciones Sustitucionales

William Hume-Rothery formuló las condiciones empíricas necesarias para que dos metales presenten una solubilidad sólida apreciable ($> 1\text{ at\%}$) o completa ($100\%$ en todo el rango de composiciones) [Slide 22]:

1. **Regla del Tamaño Atómico (Diferencia de Radios):**
   * Para metales: la diferencia porcentual de radios atómicos debe ser **menor del 15%**:
     $$\Delta R = \left|\frac{R_{\text{soluto}} - R_{\text{disolvente}}}{R_{\text{disolvente}}}\right| \times 100 < 15\%$$
   * Si $\Delta R > 15\%$, las distorsiones elásticas de red son prohibitivas y la solubilidad es inferior al $1\%$.
   * Para compuestos cerámicos iónicos, se tolera una diferencia de hasta el **30%** [Slide 22].
2. **Regla de la Estructura Cristalina:**
   * El soluto y el disolvente deben poseer la **misma estructura cristalina** (p. ej., ambos FCC, o ambos BCC).
   * La solubilidad sólida completa ($0\text{--}100\%$) es imposible si no comparten la misma red espacial.
3. **Regla de la Electronegatividad:**
   * Los dos elementos deben poseer **electronegatividades muy próximas** ($\Delta \chi \approx 0$).
   * Si la diferencia de electronegatividad es grande, el sistema formará preferentemente un **compuesto intermetálico** estequiométrico estable en lugar de una disolución sólida desordenada.
4. **Regla de la Valencia:**
   * Un metal tiene mayor tendencia a disolver a otro elemento de **mayor valencia** que de menor valencia. La solubilidad completa exige la misma valencia química.

> [!WARNING]
> El cumplimiento simultáneo de las 4 reglas es una **condición necesaria pero no suficiente** para garantizar solubilidad completa; si alguna de las 4 se incumple, la solubilidad será forzosamente parcial o nula [Slide 22].

---

## ⚖️ 3. Compensación de Carga Eléctrica en Cerámicos Iónicos

Cuando se disuelve un óxido catiónico de diferente valencia en una matriz cerámica iónica, la red **debe mantener la neutralidad eléctrica global**. Esto induce la formación obligada de defectos puntuales intrínsecos [Slide 21].

### Disolución de $\text{Al}_2\text{O}_3$ en $\text{MgO}$ [Slide 21]:
* Matriz: $\text{MgO}$ formada por cationes $\text{Mg}^{2+}$ y aniones $\text{O}^{2-}$.
* Soluto: $\text{Al}_2\text{O}_3$ aporta iones $\text{Al}^{3+}$.
* Para incorporar dos cationes $\text{Al}^{3+}$ (carga $+6$) en posiciones de $\text{Mg}^{2+}$, se deben sustituir tres cationes $\text{Mg}^{2+}$ (carga $+6$):
  $$2\,\text{Al}^{3+} \xrightarrow{\text{en MgO}} 2\,\text{Al}_{\text{Mg}}^{\bullet} + V_{\text{Mg}}''$$
  En notación de equilibrio químico [Slide 21]:
  $$3\,\text{Mg}^{2+} \longleftrightarrow 2\,\text{Al}^{3+} + 1\text{ vacante catiónica de }\text{Mg}^{2+}$$
* **Consecuencia:** Por cada mol de $\text{Al}_2\text{O}_3$ disuelto, se genera exactamente **$1\text{ mol}$ de vacantes catiónicas de $\text{Mg}^{2+}$**. Esto produce una reducción mensurable de la densidad volumétrica y un aumento en la difusión catiónica a alta temperatura.

---

## 🔀 4. Fenómeno de Orden-Desorden en Aleaciones

En soluciones sólidas sustitucionales con elementos de electronegatividad similar, la distribución de los átomos de soluto depende críticamente de la temperatura [Slide 23]:

* **Estado Desordenado ($T > T_c$):**
  A altas temperaturas, el término entálpico $-T\Delta S$ domina la energía libre. Los átomos de soluto y disolvente se distribuyen de forma completamente aleatoria en cualquier nudo de la red.
* **Estado Ordenado ($T < T_c$):**
  Al enfriar por debajo de una temperatura crítica $T_c$, la ligera preferencia energética entre enlaces heteronucleares ($A-B$) sobre homonucleares ($A-A$ y $B-B$) hace que los átomos migren hacia subredes cristalinas periódicas específicas (superred).

### Caso Paradigmático: Aleación Cobre-Oro ($\text{Cu}_3\text{Au}$ o $\text{Cu-Au}$) [Slide 23]:
* A $T > 390^\circ\text{C}$: Red FCC desordenada (los átomos de Cu y Au ocupan indistintamente los vértices y centros de caras con probabilidad según su fracción molar).
* A $T < 390^\circ\text{C}$: Red FCC químicamente ordenada: los átomos de $\text{Au}$ ocupan exclusivamente los **8 vértices**, mientras que los átomos de $\text{Cu}$ se sitúan en los **6 centros de las caras**.

---
*Enlaces Bidireccionales:*
* `[[Concepto - Defectos Puntuales Vacantes Termicas Schottky y Frenkel|⬅️ Anterior: Defectos Puntuales]]`
* `[[Concepto - Dislocaciones Vector de Burgers y Deslizamiento en Metales|Siguiente: Dislocaciones y Deslizamiento ➡️]]`
