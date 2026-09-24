---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 3 T2 Structure of Materials I_2025.pdf, Slides 29-35; Session 4 T2 Structure of Materials II_2025.pdf, Slide 9-10"
tags:
  - teoria
  - concepto-fundamental
  - intersticios
  - huecos-tetraedricos
  - huecos-octaedricos
  - solid-solutions
dificultad: media
prerrequisitos:
  - "[[Concepto - Estructuras Metalicas FCC BCC HCP y Factor de Empaquetamiento]]"
---

# 🔘 Concepto: Huecos Intersticiales Tetraédricos y Octaédricos

> **Principio Fundamental:** En cualquier red cristalina metálica, los átomos rígidos dejan espacios vacíos tridimensionales denominados **sitios o huecos intersticiales** [Slide 29]. Estos huecos son las posiciones físicas que pueden albergar átomos de soluto de pequeño radio atómico ($\text{H}, \text{C}, \text{N}, \text{B}$) en disoluciones sólidas intersticiales (p. ej., carbono en aceros o titanio) y determinan la solubilidad de impurezas, la deformación elástica local y la difusión atómica.

---

## 📐 1. Tipos de Sitios Intersticiales

Dependiendo del número de átomos de la red matriz que rodean y tocan al hueco, se distinguen [Slide 29]:

1. **Hueco Tetraédrico:**
   * **Coordinación:** Rodeado por **4 átomos** situados en los vértices de un tetraedro regular.
   * **Regla de multiplicidad en estructuras compactas (FCC, HCP):**
     $$N_{\text{tetraédricos}} = 2n$$
     donde $n$ es el número de átomos netos de la celda unitaria.

2. **Hueco Octaédrico:**
   * **Coordinación:** Rodeado por **6 átomos** situados en los vértices de un octaedro regular (o distorsionado).
   * **Regla de multiplicidad en estructuras compactas (FCC, HCP):**
     $$N_{\text{octaédricos}} = n$$

---

## 🟦 2. Sitios Intersticiales en la Estructura FCC ($n=4$)

En la red FCC existen $2 \times 4 = 8$ huecos tetraédricos y $1 \times 4 = 4$ huecos octaédricos [Slide 30]:

### Huecos Octaédricos en FCC ($N_{\text{oct}} = 4$):
* **Ubicaciones espaciales:**
  * 1 en el **centro geométrico** de la celda unitaria: $\left(\frac{1}{2}, \frac{1}{2}, \frac{1}{2}\right) \implies 1 \times 1 = 1$.
  * 12 en el **centro de las 12 aristas**: cada arista es compartida por 4 celdas contiguas $\implies 12 \times \frac{1}{4} = 3$.
  * **Total:** $1 + 3 = 4\text{ huecos octaédricos/celda}$.
* **Radio del hueco octaédrico ($r_{\text{oct}}$) [Session 4 Slide 9]:**
  A lo largo de la arista del cubo, dos átomos de la red de radio $r$ y un átomo intersticial de radio $r_{\text{oct}}$ llenan la arista $a$:
  $$2r + 2r_{\text{oct}} = a \implies r_{\text{oct}} = \frac{a - 2r}{2}$$
  Sabiendo que en FCC $a = 2\sqrt{2} r$:
  $$r_{\text{oct}} = \frac{2\sqrt{2}r - 2r}{2} = (\sqrt{2} - 1)r \approx \mathbf{0.414\, r}$$

### Huecos Tetraédricos en FCC ($N_{\text{tet}} = 8$):
* **Ubicaciones espaciales:**
  * Se localizan dentro de cada uno de los 8 subcubos de arista $a/2$. Cada hueco está en el centro de un subcubo, a una distancia de $\frac{a\sqrt{3}}{4}$ de cada uno de los 8 vértices principales (coordenadas $\left(\frac{1}{4}, \frac{1}{4}, \frac{1}{4}\right)$, etc.).
  * Al estar totalmente dentro de la celda: $8 \times 1 = 8\text{ huecos tetraédricos/celda}$.
* **Radio del hueco tetraédrico ($r_{\text{tet}}$) [Session 4 Slide 9]:**
  La distancia desde el vértice del subcubo a su centro es $\frac{\sqrt{3}}{2}\left(\frac{a}{2}\right) = \frac{a\sqrt{3}}{4}$. En esa semidiagonal:
  $$r + r_{\text{tet}} = \frac{a\sqrt{3}}{4} = \frac{(2\sqrt{2}r)\sqrt{3}}{4} = \frac{\sqrt{6}}{2}r = \sqrt{\frac{3}{2}}r$$
  $$r_{\text{tet}} = \left(\sqrt{\frac{3}{2}} - 1\right)r \approx \mathbf{0.225\, r}$$

---

## 🟥 3. Sitios Intersticiales en la Estructura BCC ($n=2$)

La red BCC **no es compacta** ($\text{APF} = 0.68$). Aunque posee más volumen libre ($32\%$), sus huecos son significativamente **más pequeños y anisótropos** [Slide 32]:

### Huecos Octaédricos en BCC ($N_{\text{oct}} = 6$):
* **Ubicaciones espaciales:**
  * Centros de las 6 caras: $6 \times \frac{1}{2} = 3$.
  * Centros de las 12 aristas: $12 \times \frac{1}{4} = 3$.
  * **Total:** $3 + 3 = 6\text{ huecos octaédricos/celda}$.
* **Radio del hueco octaédrico ($r_{\text{oct}}$) [Session 4 Slide 9]:**
  El hueco octaédrico en BCC es achatado (octaedro irregular): está muy apretado entre los dos átomos en la dirección $[100]$ a distancia $a$:
  $$2r + 2r_{\text{oct}} = a = \frac{4r}{\sqrt{3}} \implies r_{\text{oct}} = \left(\frac{2}{\sqrt{3}} - 1\right)r \approx \mathbf{0.155\, r}$$

### Huecos Tetraédricos en BCC ($N_{\text{tet}} = 12$):
* **Ubicaciones espaciales:**
  * Situados en las 6 caras del cubo, en posiciones del tipo $\left(\frac{1}{2}, \frac{1}{4}, 0\right)$. Cada una de las 6 caras contiene 4 posiciones equivalentes compartidas por 2 celdas:
    $$6_{\text{caras}} \times 4 \times \frac{1}{2} = 12\text{ huecos tetraédricos/celda}$$
* **Radio del hueco tetraédrico ($r_{\text{tet}}$) [Session 4 Slide 9]:**
  $$r_{\text{tet}} = \left(\sqrt{\frac{5}{3}} - 1\right)r \approx \mathbf{0.291\, r}$$

> [!IMPORTANT]
> **Paradoja de los Huecos en BCC vs FCC:**
> Aunque la estructura BCC tiene menor empaquetamiento volumétrico ($\text{APF} = 0.68$ vs $0.74$), el hueco octaédrico de BCC ($0.155\, r$) es **mucho más pequeño** que el de FCC ($0.414\, r$). Además, en BCC el hueco tetraédrico ($0.291\, r$) es mayor que el octaédrico ($0.155\, r$). Por ello, cuando el Carbono ($r_C \approx 0.071\text{ nm}$) se disuelve en $\alpha\text{-Fe}$ (BCC, $r_{\text{Fe}} \approx 0.124\text{ nm}$), debe forzar una distorsión tetragonal asimétrica severa, limitando su solubilidad máxima a solo un **0.022 wt% C a 727 ºC**, mientras que en $\gamma\text{-Fe}$ (FCC) entra en los amplios huecos octaédricos con una solubilidad de hasta **2.14 wt% C**.

---

## 🟩 4. Sitios Intersticiales en la Estructura HCP ($n=6$)

* **Huecos Octaédricos:** $N_{\text{oct}} = n = 6$. Radio relativo: $r_{\text{oct}} \approx 0.414\, r$ [Slide 34, Session 4 Slide 9].
* **Huecos Tetraédricos:** $N_{\text{tet}} = 2n = 12$. Radio relativo: $r_{\text{tet}} \approx 0.225\, r$.

---

## 📊 5. Cuadro Sinóptico de Intersticios

| Estructura | $n$ | $V_{\text{huecos}}/V_C$ | Huecos Octaédricos ($N_{\text{oct}}$) | $r_{\text{oct}}/r$ | Huecos Tetraédricos ($N_{\text{tet}}$) | $r_{\text{tet}}/r$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FCC** | 4 | $0.26$ | **4** (centro y aristas) | **0.414** | **8** (interiores a $a\sqrt{3}/4$) | **0.225** |
| **BCC** | 2 | $0.32$ | **6** (caras y aristas) | **0.155** | **12** (4 en cada cara) | **0.291** |
| **HCP** | 6 | $0.26$ | **6** | **0.414** | **12** | **0.225** |

---
*Enlaces Bidireccionales:*
* `[[Concepto - Estructuras Metalicas FCC BCC HCP y Factor de Empaquetamiento|⬅️ Anterior: Estructuras Metálicas FCC, BCC, HCP]]`
* `[[Concepto - Notacion de Miller para Direcciones y Planos Cubicos y Hexagonales|Siguiente: Notación de Miller para Direcciones y Planos ➡️]]`
