---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 3 T2 Structure of Materials I_2025.pdf, Slides 16-28"
tags:
  - teoria
  - concepto-fundamental
  - fcc
  - bcc
  - hcp
  - packing-factor
  - coordination-number
dificultad: media
prerrequisitos:
  - "[[Concepto - Sistemas Cristalinos y Redes de Bravais]]"
---

# 📦 Concepto: Estructuras Metálicas FCC, BCC, HCP y Factor de Empaquetamiento

> **Principio Físico:** En los metales, debido a que el enlace metálico es esencialmente **no direccional**, los átomos (esferas rígidas de radio $R$) tienden a organizarse minimizando la energía libre de Gibbs y maximizando la densidad de empaquetamiento espacial. Las tres redes metálicas estructurales predominantes son **BCC (Cúbica centrada en el cuerpo)**, **FCC (Cúbica centrada en las caras)** y **HCP (Hexagonal compacta)** [Slides 16-17].

---

## 🧮 1. Definición del Factor de Empaquetamiento Atómico (APF)

El **Atomic Packing Factor (APF)** mide la fracción volumétrica ocupada por materia atómica rígida dentro de la celda unitaria [Slide 16]:

$$\text{APF} = \frac{V_{\text{átomos}}}{V_{\text{celda}}} = \frac{n \cdot V_{\text{esfera}}}{V_C} = \frac{n \cdot \left(\frac{4}{3}\pi R^3\right)}{V_C}$$

donde:
* $n$: número de átomos equivalentes o netos contenidos en la celda unitaria.
* $R$: radio atómico efectivo.
* $V_C$: volumen geométrico total de la celda unitaria.
* $\text{NC}$ (Número de Coordinación): número de primeros vecinos atómicos en contacto directo con cada átomo.

---

## 🟥 2. Estructura Cúbica Centrada en el Cuerpo (BCC)

### Geometría y Parámetro de Red [Slide 18]
* **Contacto atómico:** Los átomos se tocan a lo largo de la diagonal principal del cubo $[111]$.
* **Relación geométrica:**
  $$\text{Diagonal del cubo} = \sqrt{a^2 + a^2 + a^2} = a\sqrt{3} = 4R \implies a = \frac{4R}{\sqrt{3}}$$
* **Número de átomos netos ($n$):**
  $$n = 8 \times \left(\frac{1}{8}\right)_{\text{vértices}} + 1_{\text{centro}} = 2\text{ átomos/celda}$$
* **Número de coordinación:** $\text{NC} = 8$ (el átomo central toca a los 8 átomos de los vértices).
* **Cálculo del APF [Slide 19]:**
  $$V_C = a^3 = \left(\frac{4R}{\sqrt{3}}\right)^3 = \frac{64 R^3}{3\sqrt{3}}$$
  $$\text{APF}_{\text{BCC}} = \frac{2 \cdot \frac{4}{3}\pi R^3}{\frac{64 R^3}{3\sqrt{3}}} = \frac{\frac{8}{3}\pi R^3}{\frac{64}{3\sqrt{3}} R^3} = \frac{\pi\sqrt{3}}{8} \approx 0.6802 \implies \mathbf{68\%}$$
* **Volumen relativo de intersticios:** $V_{\text{huecos}} / V_C = 1 - 0.68 = 0.32$ ($32\%$ de espacio libre).
* **Metales representativos:** $\alpha\text{-Fe}$ (ferrita a $T < 912^\circ\text{C}$), $\text{Cr}, \text{Mo}, \text{W}, \text{Ta}, \text{V}, \text{Nb}$.

---

## 🟦 3. Estructura Cúbica Centrada en las Caras (FCC)

### Geometría y Parámetro de Red [Slide 20]
* **Contacto atómico:** Los átomos están en contacto directo a lo largo de las diagonales de las caras $\langle 110 \rangle$.
* **Relación geométrica:**
  $$\text{Diagonal de la cara} = \sqrt{a^2 + a^2} = a\sqrt{2} = 4R \implies a = \frac{4R}{\sqrt{2}} = 2\sqrt{2} R$$
* **Número de átomos netos ($n$):**
  $$n = 8 \times \left(\frac{1}{8}\right)_{\text{vértices}} + 6 \times \left(\frac{1}{2}\right)_{\text{caras}} = 1 + 3 = 4\text{ átomos/celda}$$
* **Número de coordinación:** $\text{NC} = 12$ (cada átomo en el centro de cara toca a 4 átomos de vértice y a 8 centros de caras adyacentes).
* **Cálculo del APF [Slide 21]:**
  $$V_C = a^3 = (2\sqrt{2}R)^3 = 16\sqrt{2} R^3$$
  $$\text{APF}_{\text{FCC}} = \frac{4 \cdot \frac{4}{3}\pi R^3}{16\sqrt{2} R^3} = \frac{\frac{16}{3}\pi R^3}{16\sqrt{2} R^3} = \frac{\pi}{3\sqrt{2}} = \frac{\pi\sqrt{2}}{6} \approx 0.7405 \implies \mathbf{74\%}$$
* **Volumen relativo de intersticios:** $V_{\text{huecos}} / V_C = 1 - 0.74 = 0.26$ ($26\%$ de espacio libre).
* **Metales representativos:** $\text{Al}, \text{Cu}, \text{Ni}, \text{Au}, \text{Ag}, \text{Pt}, \gamma\text{-Fe}$ (austenita).

---

## 🟩 4. Estructura Hexagonal Compacta (HCP)

### Geometría y Relación Axial Ideal $c/a$ [Slides 22-25]
La celda hexagonal compacta consta de dos planos basales hexagonales de parámetro $a$ y un plano intermedio con 3 átomos situados a media altura ($c/2$).
* **Contacto en la base:** $a = 2R$.
* **Número de átomos netos ($n$):**
  $$n = 12 \times \left(\frac{1}{6}\right)_{\text{vértices}} + 2 \times \left(\frac{1}{2}\right)_{\text{centros base}} + 3_{\text{plano medio}} = 2 + 1 + 3 = 6\text{ átomos/celda}$$
* **Deducción rigurosa de la relación ideal $c/a$ [Slide 24]:**
  Consideremos el tetraedro regular formado por los tres átomos del plano intermedio y el átomo central del plano basal. La arista del tetraedro es $a$, y su altura es $c/2$.
  La distancia desde un vértice de la base del triángulo equilátero de lado $a$ a su baricentro es $r_b = \frac{a}{\sqrt{3}}$.
  Aplicando el teorema de Pitágoras:
  $$\left(\frac{c}{2}\right)^2 + r_b^2 = a^2 \implies \frac{c^2}{4} + \frac{a^2}{3} = a^2 \implies \frac{c^2}{4} = \frac{2}{3}a^2$$
  $$\left(\frac{c}{a}\right)^2 = \frac{8}{3} \implies \frac{c}{a} = \sqrt{\frac{8}{3}} \approx 1.633$$
* **Volumen de la Celda Hexagonal ($V_C$):**
  La base está compuesta por 6 triángulos equiláteros de lado $a$:
  $$A_{\text{base}} = 6 \times \left(\frac{\sqrt{3}}{4}a^2\right) = \frac{3\sqrt{3}}{2} a^2$$
  $$V_C = A_{\text{base}} \cdot c = \frac{3\sqrt{3}}{2} a^2 c = \frac{3\sqrt{3}}{2} a^3 \sqrt{\frac{8}{3}} = 3\sqrt{2} a^3$$
  Sustituyendo $a = 2R$:
  $$V_C = 3\sqrt{2} (2R)^3 = 24\sqrt{2} R^3$$
* **Cálculo del APF [Slide 25]:**
  $$\text{APF}_{\text{HCP}} = \frac{6 \cdot \frac{4}{3}\pi R^3}{24\sqrt{2} R^3} = \frac{8\pi R^3}{24\sqrt{2} R^3} = \frac{\pi}{3\sqrt{2}} = \frac{\pi\sqrt{2}}{6} \approx 0.7405 \implies \mathbf{74\%}$$
* **Número de coordinación:** $\text{NC} = 12$ (6 en el propio plano basal, 3 en el plano inferior, 3 en el superior).
* **Metales representativos:** $\alpha\text{-Ti}, \text{Mg}, \text{Zn}, \text{Be}, \text{Cd}, \text{Zr}$.

---

## 🔄 5. Comparativa de Secuencia de Apilamiento: HCP ($ABAB\dots$) vs FCC ($ABCABC\dots$)

Tanto FCC como HCP alcanzan el límite teórico máximo de densidad de esferas rígidas congruentes en 3D ($\text{APF} = 0.7405$, Teorema de Kepler). La única diferencia estriba en la secuencia periódica de apilamiento de los planos de máximo empaquetamiento [Slides 26-28]:

```
Plano A: Capa inicial hexagonal compacta.
Plano B: Se asienta en los valles triangulares formados por la capa A.
Plano C: Se asienta en el segundo grupo alternante de huecos triangulares que NO coinciden verticalmente con A.

Secuencia HCP: A - B - A - B - A - B ...  (Periodo de 2 capas, simetría hexagonal)
Secuencia FCC: A - B - C - A - B - C ...  (Periodo de 3 capas a lo largo de [111], simetría cúbica)
```

| Propiedad | BCC | FCC | HCP |
| :--- | :--- | :--- | :--- |
| **Relación $a(R)$** | $a = 4R/\sqrt{3}$ | $a = 2\sqrt{2}R$ | $a = 2R,\, c = 1.633 a$ |
| **Átomos/celda ($n$)** | 2 | 4 | 6 |
| **Número Coord. ($\text{NC}$)** | 8 | 12 | 12 |
| **APF** | **0.68** | **0.74** | **0.74** |
| **Planos compactos** | $\{110\}$ (densos, no compactos) | $\{111\}$ (4 familias) | $(0001)$ (1 plano basal) |
| **Direcciones compactas** | $\langle 111 \rangle$ (4 direcciones) | $\langle 110 \rangle$ (6 direcciones) | $\langle 11\bar{2}0 \rangle$ (3 direcciones) |
| **Ductilidad macroscópica** | Moderada (alta a $T \uparrow$) | **Muy Alta (a cualquier $T$)** | Baja a temperatura ambiente |

---
*Enlaces Bidireccionales:*
* `[[Concepto - Sistemas Cristalinos y Redes de Bravais|⬅️ Anterior: Sistemas Cristalinos y Redes de Bravais]]`
* `[[Concepto - Huecos Intersticiales Tetraedricos y Octaedricos|Siguiente: Huecos Intersticiales Tetraédricos y Octaédricos ➡️]]`
