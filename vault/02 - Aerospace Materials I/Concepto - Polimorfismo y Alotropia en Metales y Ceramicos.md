---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 4 T2 Structure of Materials II_2025.pdf, Slides 48-50"
tags:
  - teoria
  - concepto-fundamental
  - polimorfismo
  - alotropia
  - transformaciones-de-fase
  - acero-hierro
  - circona
  - carbono
dificultad: media
prerrequisitos:
  - "[[Concepto - Defectos Planares Limites de Grano Maclas y Ecuacion de Hall-Petch]]"
---

# 🔄 Concepto: Polimorfismo y Alotropía en Metales y Cerámicos

> **Definiciones Canónicas [Slide 48]:**
> * **Polimorfismo:** Capacidad que posee un material sólido (elemento o compuesto químico) de existir en **más de una estructura cristalina** diferente bajo distintas condiciones termodinámicas de temperatura y presión.
> * **Alotropía:** Caso específico de polimorfismo cuando se refiere a un **elemento químico puro**.

---

## 💎 1. Alótropos del Carbono: Diamante vs Grafito [Slide 48]

El carbono ilustra cómo la misma composición elemental adquiere propiedades radicalmente divergentes en función de la hibridación electrónica y la simetría cristalina:

```
Propiedad              Diamante (Cúbico Covalente)                 Grafito (Laminar Hexagonal)
─────────────────────────────────────────────────────────────────────────────────────────────────
Hibridación            sp³ (4 enlaces σ directos a 109.5°)         sp² (3 enlaces σ planares a 120° + 1 e⁻ π deslocalizado)
Estructura             Red tridimensional tetraédrica              Planos hexagonales unidos por enlaces débiles de van der Waals
Dureza y Abrasión      Sustancia más dura de la naturaleza (10 Mohs) Extremadamente blando (lubricante sólido natural)
Propiedades Ópticas    Transparente con altísimo índice de refracción Negro opaco
Conductividad Eléctrica Aislante eléctrico excelente (bandgap = 5.5 eV) Excelente conductor eléctrico paralelo a las capas basales
```

---

## ⚙️ 2. Transformaciones Alotrópicas del Hierro ($\text{Fe}$) [Slide 49]

El hierro puro experimenta sucesivas transiciones de fase en estado sólido durante el calentamiento a presión atmosférica estándar:

$$\alpha\text{-Fe (BCC)} \xrightarrow{\mathbf{912^\circ C}} \gamma\text{-Fe (FCC)} \xrightarrow{\mathbf{1394^\circ C}} \delta\text{-Fe (BCC)} \xrightarrow{\mathbf{1538^\circ C}} \text{Líquido}$$

### Trascendencia Metalúrgica y Tratamientos Térmicos:
1. **Cambio Volumétrico Intríseco:**
   Al calentar a través de $912^\circ\text{C}$, la red cambia de BCC ($n=2$, $\text{APF} = 0.68$) a FCC ($n=4$, $\text{APF} = 0.74$). Este aumento brusco de compacidad causa una **contracción volumétrica neta del metal** ($\approx -1\%$ en volumen molar) al cruzar la temperatura crítica.
2. **Solubilidad del Carbono y Temple de Aceros:**
   * En $\alpha\text{-Fe}$ (BCC), los huecos octaédricos son pequeños ($0.155\, r$), limitando la solubilidad de carbono a un máximo de **$0.022\text{ wt\%}$**.
   * En $\gamma\text{-Fe}$ (FCC, austenita), los huecos octaédricos son amplios ($0.414\, r$), permitiendo disolver hasta un **$2.14\text{ wt\%}$ de carbono**.
   * Al enfriar bruscamente (temple) desde el campo austenítico $\gamma$, el carbono queda atrapado en los intersticios de la red de hierro, impidiendo la difusión y forzando una transformación sin difusión (difusionless) hacia una fase sobresaturada tetragonal centrada en el cuerpo denominada **martensita**, base de la resistencia de aceros de ultra-alta resistencia en trenes de aterrizaje aeronáuticos.

---

## 🏺 3. Circonia ($\text{ZrO}_2$) y Tenacificación por Transformación Martensítica [Slide 50]

El dióxido de zirconio ($\text{ZrO}_2$) puro experimenta tres fases polimórficas al variar la temperatura:

$$\text{Monoclínica} \xrightarrow{1170^\circ\text{C}} \text{Tetragonal} \xrightarrow{2370^\circ\text{C}} \text{Cúbica (tipo Fluorita } \text{CaF}_2\text{)} \xrightarrow{2706^\circ\text{C}} \text{Líquido}$$

### El Mecanismo de Tenacificación por Transformación (Transformation Toughening):
* Al enfriar circonia pura no dopada, la transición de tetragonal a monoclínica induce una **expansión volumétrica catastrófica del 3% al 5%** acompañada de cizalladura elástica, pulverizando la pieza de cerámica.
* Dopando la circonia con óxido de itrio ($\text{Y}_2\text{O}_3$, $3\text{--}8\text{ mol\%}$), se estabiliza la fase **tetragonal metaestable a temperatura ambiente** (Y-TZP: *Yttria-Stabilized Tetragonal Zirconia Polycrystal*).
* Cuando una grieta microscópica avanza bajo carga de tracción, el campo elástico de tensiones en el vértice de la grieta dispara localmente la transformación de fase tetragonal $\to$ monoclínica.
* Dado que la fase monoclínica tiene mayor volumen molar, la transformación **se expande contra la matriz elástica circundante, generando intensas tensiones de compresión de cierre que estrangulan y detienen la grieta**.
* Este mecanismo eleva la tenacidad de fractura de la circonia hasta $K_{IC} \approx 8\text{--}12\text{ MPa}\sqrt{\text{m}}$, convirtiéndola en el "acero cerámico" utilizado en recubrimientos de barrera térmica (TBC) de álabes de turbina.

---
*Enlaces Bidireccionales:*
* `[[Concepto - Defectos Planares Limites de Grano Maclas y Ecuacion de Hall-Petch|⬅️ Anterior: Defectos Planares y Hall-Petch]]`
* `[[Tema 2 - Structure of Materials and Crystalline Defects|Volver al MOC de Tema 2 🏠]]`
