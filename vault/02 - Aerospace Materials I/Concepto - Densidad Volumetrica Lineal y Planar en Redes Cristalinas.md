---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 4 T2 Structure of Materials II_2025.pdf, Slides 7-9"
tags:
  - teoria
  - concepto-fundamental
  - densidad-volumetrica
  - densidad-lineal
  - densidad-planar
  - calculos-cristalinos
dificultad: media
prerrequisitos:
  - "[[Concepto - Notacion de Miller para Direcciones y Planos Cubicos y Hexagonales]]"
---

# ⚖️ Concepto: Densidad Volumétrica, Lineal y Planar en Redes Cristalinas

> **Definición Global:** Las propiedades mecánicas, la anisotropía elástica, la resistencia a la fluencia por dislocaciones y las velocidades de corrosión dependen fuertemente de la **densidad de empaquetamiento atómico** evaluada en 3 dimensiones (volumen), 2 dimensiones (planos cristalográficos) y 1 dimensión (direcciones cristalográficas) [Slides 7-9].

---

## 🧊 1. Densidad Volumétrica ($\rho$ o $\rho_v$)

La densidad volumétrica teórica es la masa total contenida dentro de la celda unitaria dividida por el volumen de dicha celda [Slide 15, Session 4]:

$$\rho_v = \frac{m_{\text{celda}}}{V_C} = \frac{n \cdot M}{V_C \cdot N_A}$$

donde:
* $n$: número de átomos equivalentes por celda unitaria ($n_{\text{BCC}} = 2$, $n_{\text{FCC}} = 4$, $n_{\text{HCP}} = 6$).
* $M$: masa atómica molar del elemento ($\text{g/mol}$).
* $V_C$: volumen de la celda unitaria ($V_{\text{cúbica}} = a^3$; $V_{\text{ortorrómbica}} = a \cdot b \cdot c$; $V_{\text{HCP}} = \frac{3\sqrt{3}}{2}a^2 c$).
* $N_A$: número de Avogadro ($6.022 \times 10^{23}\text{ átomos/mol}$).

### Ejemplo Canónico: Cobre Puro ($\text{Cu}$, FCC) [Session 4 Slide 7]
* Datos: $M = 63.546\text{ g/mol}$, $R = 1.28\text{ \AA} = 1.28 \times 10^{-8}\text{ cm}$, $n = 4$.
* Parámetro de red FCC: $a = 2\sqrt{2} R = 2\sqrt{2}(1.28 \times 10^{-8}) = 3.62 \times 10^{-8}\text{ cm}$.
* Volumen de celda: $V_C = a^3 = (3.62 \times 10^{-8}\text{ cm})^3 = 4.74 \times 10^{-23}\text{ cm}^3$.
* Densidad teórica:
  $$\rho_v = \frac{4 \times 63.546}{4.74 \times 10^{-23} \times 6.022 \times 10^{23}} = \mathbf{8.89\text{ g/cm}^3}$$
  *(Coincide con el valor experimental de $8.9\text{ g/cm}^3$ medido en probetas macroscópicas).*

---

## 📏 2. Densidad Lineal ($\rho_l$)

La densidad lineal representa el número de diámetros atómicos centrados sobre un vector o segmento de dirección cristalográfica $[u\, v\, w]$ dividido por la longitud geométrica de dicho vector [Slide 7]:

$$\rho_l = \frac{N_{\text{átomos centrados en la línea}}}{L_{[u\, v\, w]}}$$

* Si una línea corta un átomo por su centro exacto dentro del tramo de celda, cuenta como $1$ átomo completo.
* Si corta átomos en los dos extremos de la arista o diagonal, cada extremo aporta $\frac{1}{2}$ átomo $\implies 2 \times \frac{1}{2} = 1$ átomo.

### Ejemplos en Redes Cúbicas:
1. **FCC en dirección $[100]$ [Slide 7]:**
   * $L_{[100]} = a = 2\sqrt{2}R$.
   * Corta 2 vértices: $2 \times \frac{1}{2} = 1\text{ átomo}$.
   * Para Cu ($R = 1.28\text{ \AA}$):
     $$\rho_l [100] = \frac{1\text{ at}}{2\sqrt{2}(1.28 \times 10^{-8}\text{ cm})} = 2.76 \times 10^7\text{ at/cm} = 2.76 \times 10^9\text{ at/m}$$
2. **FCC en dirección $[110]$ (Dirección de Máximo Empaquetamiento):**
   * $L_{[110]} = a\sqrt{2} = 4R$.
   * Corta 2 vértices ($2 \times 1/2$) + 1 centro de cara completo = $2\text{ átomos}$.
   * Densidad lineal:
     $$\rho_l [110] = \frac{2\text{ at}}{4R} = \frac{1}{2R} = \frac{\sqrt{2}}{a} = \frac{1}{2(1.28 \times 10^{-8})} = 3.91 \times 10^7\text{ at/cm}$$
3. **BCC en dirección $[111]$ (Dirección de Máximo Empaquetamiento):**
   * $L_{[111]} = a\sqrt{3} = 4R$.
   * Corta 2 vértices ($2 \times 1/2$) + 1 átomo central = $2\text{ átomos}$.
     $$\rho_l [111] = \frac{2}{a\sqrt{3}} = \frac{1}{2R}$$

---

## 🗺️ 3. Densidad Planar ($\rho_p$)

La densidad planar cuantifica el número de átomos cuyos centros geométricos están contenidos en el plano cristalográfico $(h\, k\, l)$, dividido por el área bidimensional delimitada por la celda unidad en dicho plano [Slide 8]:

$$\rho_p = \frac{N_{\text{átomos contenidos en el plano}}}{A_{(h\, k\, l)}}$$

* Una fracción de átomo cuenta según el ángulo que el contorno del plano subtiende en dicho átomo:
  * Vértice de un cuadrado / rectángulo ($90^\circ$): aporta $\frac{90^\circ}{360^\circ} = \frac{1}{4}$.
  * Vértice de un triángulo equilátero en plano $(111)$ ($60^\circ$): aporta $\frac{60^\circ}{360^\circ} = \frac{1}{6}$.
  * Átomo en una arista compartida entre dos celdas: aporta $\frac{180^\circ}{360^\circ} = \frac{1}{2}$.
  * Átomo totalmente dentro del plano interior: aporta $1$.

### Ejemplos en Redes Cúbicas:
1. **FCC en plano $(100)$ [Slide 8]:**
   * Área: $A_{(100)} = a^2$.
   * Átomos contenidos: 4 vértices $\times \frac{1}{4} + 1\text{ centro de cara} = 1 + 1 = 2\text{ átomos}$.
   * Expresión analítica: $\rho_p (100) = \frac{2}{a^2}$.
   * Para Cu: $\rho_p (100) = \frac{2}{(3.62 \times 10^{-8}\text{ cm})^2} = 1.52 \times 10^{15}\text{ at/cm}^2$.
2. **FCC en plano $(110)$:**
   * Dimensiones del rectángulo: base $a\sqrt{2}$, altura $a \implies A_{(110)} = \sqrt{2}a^2$.
   * Átomos contenidos: 4 vértices $\times \frac{1}{4} + 2\text{ centros en aristas de cara} \times \frac{1}{2} = 1 + 1 = 2\text{ átomos}$.
   * Expresión analítica: $\rho_p (110) = \frac{2}{\sqrt{2}a^2} = \frac{\sqrt{2}}{a^2}$.
3. **FCC en plano $(111)$ (Plano Compacto de Deslizamiento):**
   * El plano $(111)$ corta las diagonales de cara formando un triángulo equilátero de lado $L = a\sqrt{2}$.
   * Área: $A_{(111)} = \frac{\sqrt{3}}{4} L^2 = \frac{\sqrt{3}}{4}(2a^2) = \frac{\sqrt{3}}{2}a^2$.
   * Átomos contenidos: 3 vértices $\times \frac{1}{6} + 3\text{ centros en los lados} \times \frac{1}{2} = \frac{1}{2} + \frac{3}{2} = 2\text{ átomos}$.
   * Expresión analítica:
     $$\rho_p (111) = \frac{2}{\frac{\sqrt{3}}{2}a^2} = \frac{4}{a^2\sqrt{3}}$$
4. **BCC en plano $(110)$ (Plano Más Denso de BCC):**
   * Dimensiones: base $a\sqrt{2}$, altura $a \implies A_{(110)} = \sqrt{2}a^2$.
   * Átomos: 4 vértices $\times \frac{1}{4} + 1\text{ átomo central completo} = 2\text{ átomos}$.
   * Expresión analítica:
     $$\rho_p (110) = \frac{2}{\sqrt{2}a^2} = \frac{\sqrt{2}}{a^2}$$

---

## 💡 4. Relación Fundamental entre Densidades y Espaciado Interplanar

En cualquier cristal ortogonal, la densidad volumétrica $\rho_v$ de puntos de red se relaciona exactamente con la densidad planar $\rho_p$ de una familia de planos $(hkl)$ y su espaciado interplanar $d_{hkl}$:

$$\rho_v = \frac{\rho_p(hkl)}{d_{hkl}}$$

Esta igualdad confirma que los planos más compactos (mayor $\rho_p$) son simultáneamente aquellos con el **mayor espaciado interplanar $d_{hkl}$**, lo que explica por qué son los planos preferenciales de deslizamiento de dislocaciones (menor resistencia de red Peierls-Nabarro).

---
*Enlaces Bidireccionales:*
* `[[Concepto - Notacion de Miller para Direcciones y Planos Cubicos y Hexagonales|⬅️ Anterior: Notación de Miller]]`
* `[[Concepto - Difraccion de Rayos X y Ley de Bragg|Siguiente: Difracción de Rayos X y Ley de Bragg ➡️]]`
