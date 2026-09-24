---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 3 T2 Structure of Materials I_2025.pdf, Slides 7-14"
tags:
  - teoria
  - concepto-fundamental
  - cristalografia
  - bravais-lattices
  - crystal-systems
dificultad: baja
prerrequisitos:
  - "Tema 1: Bonding in Solids"
---

# 🔷 Concepto: Sistemas Cristalinos y las 14 Redes de Bravais

> **Definición Central:** Un **sistema cristalino** es una clasificación geométrica del espacio tridimensional basada en las relaciones de longitud de sus tres vectores base de celda ($a, b, c$) y los tres ángulos interaxiales ($\alpha, \beta, \gamma$). Combinando los **7 sistemas cristalinos** con los **4 tipos de celda unitaria** (Primitiva $P$, Centrada en el cuerpo $I$, Centrada en las caras $F$ y Centrada en las bases $C$), el físico francés **Auguste Bravais (1848)** demostró que solo existen exactamente **14 redes periódicas tridimensionales independientes** capaces de llenar el espacio sin discontinuidades ni solapamientos [Slide 8].

---

## 📐 1. Parámetros de Red de la Celda Unitaria

Cualquier celda unidad tridimensional se define formalmente mediante un origen común y tres vectores de traslación primarios $\vec{a}, \vec{b}, \vec{c}$ [Slide 7]:
* **Longitudes axiales:** $a = |\vec{a}|$, $b = |\vec{b}|$, $c = |\vec{c}|$.
* **Ángulos interaxiales:**
  * $\alpha$: ángulo subtendido entre $\vec{b}$ y $\vec{c}$.
  * $\beta$: ángulo subtendido entre $\vec{a}$ y $\vec{c}$.
  * $\gamma$: ángulo subtendido entre $\vec{a}$ y $\vec{b}$.

$$\text{Celda Unitaria} \iff \{a, b, c;\, \alpha, \beta, \gamma\}$$

---

## 🏛️ 2. Los 7 Sistemas Cristalinos

Los 7 sistemas cristalinos representan las clases de simetría métrica más altas posibles en $\mathbb{R}^3$ [Slides 11-13]:

| Sistema Cristalino | Relaciones de Aristas | Relaciones de Ángulos | Simetría Característica |
| :--- | :--- | :--- | :--- |
| **Cúbico (Cubic)** | $a = b = c$ | $\alpha = \beta = \gamma = 90^\circ$ | 4 ejes de rotación ternaria $\langle 111 \rangle$ |
| **Tetragonal** | $a = b \neq c$ | $\alpha = \beta = \gamma = 90^\circ$ | 1 eje de rotación cuaternaria $[001]$ |
| **Ortorrómbico (Orthorhombic)** | $a \neq b \neq c$ | $\alpha = \beta = \gamma = 90^\circ$ | 3 ejes binarios perpendiculares |
| **Romboédrico (Trigonal)** | $a = b = c$ | $\alpha = \beta = \gamma \neq 90^\circ < 120^\circ$ | 1 eje de rotación ternaria |
| **Hexagonal** | $a = b \neq c$ | $\alpha = \beta = 90^\circ,\, \gamma = 120^\circ$ | 1 eje de rotación senaria $[0001]$ |
| **Monoclínico (Monoclinic)** | $a \neq b \neq c$ | $\alpha = \gamma = 90^\circ \neq \beta$ | 1 eje de rotación binaria |
| **Triclínico (Triclinic)** | $a \neq b \neq c$ | $\alpha \neq \beta \neq \gamma \neq 90^\circ$ | Centro de inversión únicamente ($C_i$) |

---

## 📦 3. Los 4 Tipos de Centrado de Celda Unitaria

Para ubicar los motivos atómicos dentro del volumen reticular, Bravais categorizó cuatro disposiciones estándar [Slide 9]:

1. **Primitiva ($P$ / Simple):**
   * Puntos de red situados exclusivamente en los 8 vértices de la celda.
   * Contribución efectiva: $8 \times \frac{1}{8} = 1\text{ punto neto de red}$.
2. **Centrada en el Cuerpo ($I$ - *Innenzentrierte*):**
   * Puntos de red en los vértices más 1 punto en el centro geométrico del volumen de la celda.
   * Contribución efectiva: $8 \times \frac{1}{8} + 1 = 2\text{ puntos netos}$.
3. **Centrada en las Caras ($F$ - *Flächenzentrierte*):**
   * Puntos de red en los 8 vértices más 1 punto en el baricentro de cada una de las 6 caras.
   * Contribución efectiva: $8 \times \frac{1}{8} + 6 \times \frac{1}{2} = 4\text{ puntos netos}$.
4. **Centrada en las Bases ($C$ - Base-Centered):**
   * Puntos de red en los 8 vértices más 1 punto en el centro de dos caras opuestas y paralelas (generalmente el plano $(001)$).
   * Contribución efectiva: $8 \times \frac{1}{8} + 2 \times \frac{1}{2} = 2\text{ puntos netos}$.

---

## 🗺️ 4. Distribución Rigurosa de las 14 Redes de Bravais

No todas las combinaciones $7 \times 4 = 28$ son independientes; muchas reducen por operaciones de cambio de base a celdas primitivas de mayor simetría. Las **14 redes únicas** son [Slides 11-13]:

```
7 Sistemas Cristalinos
 ├── 1. Cúbico (3 redes):         P (Simple), I (BCC), F (FCC)
 ├── 2. Tetragonal (2 redes):     P (Simple), I (Body-centered)
 ├── 3. Ortorrómbico (4 redes):   P (Simple), C (Base-centered), I (Body-centered), F (Face-centered)
 ├── 4. Romboédrico (1 red):      P (Simple)
 ├── 5. Hexagonal (1 red):        P (Simple)
 ├── 6. Monoclínico (2 redes):    P (Simple), C (Base-centered)
 └── 7. Triclínico (1 red):       P (Simple)
 Total = 3 + 2 + 4 + 1 + 1 + 2 + 1 = 14 Redes de Bravais
```

### ¿Por qué el sistema ortorrómbico posee las 4 variantes ($P, C, I, F$)?
Debido a que sus tres aristas son mutuamente desiguales ($a \neq b \neq c$), añadir puntos en las caras o en el cuerpo nunca introduce una simetría adicional que permita colapsar la celda en una tetragonal o cúbica más pequeña. Por ello, el ortorrómbico es el **único sistema cristalino que exhibe las 4 modalidades de red de Bravais** [Slide 12].

---

## 🚀 Relevancia Aeroespacial

* **Aleaciones de Titanio ($\text{Ti}$):** Presenta transición polimórfica entre la fase $\alpha$ (Hexagonal compacta) y la fase $\beta$ a alta temperatura (Cúbica centrada en el cuerpo), clave para el forjado de discos y álabes de compresores.
* **Refractarios y Circonia ($\text{ZrO}_2$):** Su estructura pasa de monoclínica a temperatura ambiente a tetragonal y cúbica a alta temperatura; estabilizar la fase tetragonal con itria ($\text{Y}_2\text{O}_3$, YSZ) permite fabricar recubrimientos de barrera térmica (TBC) en turbinas aeronáuticas.

---
*Enlaces Bidireccionales:*
* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]`
* `[[Concepto - Estructuras Metalicas FCC BCC HCP y Factor de Empaquetamiento|Siguiente: Estructuras Metálicas FCC, BCC, HCP y APF ➡️]]`
