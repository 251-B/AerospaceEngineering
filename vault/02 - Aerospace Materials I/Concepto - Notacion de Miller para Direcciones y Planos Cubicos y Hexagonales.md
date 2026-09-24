---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 3 T2 Structure of Materials I_2025.pdf, Slides 36-52"
tags:
  - teoria
  - concepto-fundamental
  - miller-indices
  - miller-bravais
  - direcciones-cristalinas
  - planos-cristalinos
dificultad: media
prerrequisitos:
  - "[[Concepto - Sistemas Cristalinos y Redes de Bravais]]"
---

# 🧭 Concepto: Notación de Miller para Direcciones y Planos Cúbicos y Hexagonales

> **Fundamento Metodológico:** La **notación de Miller** es el estándar cristalográfico universal para identificar unívocamente vectores de traslación (direcciones) y familias periódicas de planos dentro de una red cristalina. Permite correlacionar la simetría de la red con fenómenos físicos anisotrópicos como la propagación de ondas de rayos X, la deformación plástica por deslizamiento y el crecimiento epitaxial [Slide 36].

---

## ➡️ 1. Direcciones Cristalográficas Cúbicas $[u\, v\, w]$

Una dirección cristalográfica se define como un vector trazado desde el origen de coordenadas hasta un punto genérico de la celda [Slides 37-40].

### Procedimiento Sistemático de Determinación:
1. **Elección del Sistema de Ejes y Origen:** Se sitúa un sistema de coordenadas diestro en un vértice de la celda unitaria. Si alguna componente de la dirección proyecta hacia valores negativos, **se traslada el origen** a lo largo del eje correspondiente en una longitud de celda (+1).
2. **Coordenadas del Vector:** Se restan las coordenadas de la punta (Head) menos las del origen (Tail):
   $$\Delta x = x_2 - x_1, \quad \Delta y = y_2 - y_1, \quad \Delta z = z_2 - z_1$$
3. **Reducción a los Enteros Mínimos:** Se divide o multiplica por el mínimo común denominador para obtener los enteros más pequeños posibles:
   $$u, v, w \in \mathbb{Z}$$
4. **Notación:** Se encierran entre **corchetes rectos** sin comas: $[u\, v\, w]$. Los números negativos se denotan con una barra superior: $\bar{u} \equiv -u$.
5. **Familias de Direcciones Cristalográficamente Equivalentes:** Se encierran entre **corchetes angulares**: $\langle u\, v\, w \rangle$. Por ejemplo, en el sistema cúbico, las 6 diagonales de arista son:
   $$\langle 100 \rangle = \{[100], [\bar{1}00], [010], [0\bar{1}0], [001], [00\bar{1}]\}$$

---

## 📐 2. Planos Cristalográficos de Miller $(h\, k\, l)$

Un plano cristalográfico representa una familia infinita de planos paralelos y equidistantes [Slides 41-49].

### Procedimiento Sistemático de Determinación:
1. **Origen y Regla de Intersección:** El plano de análisis **no puede pasar por el origen**. Si pasa por el origen, se traslada el origen de coordenadas a un vértice contiguo adyacente.
2. **Determinación de Intersecciones:** Se identifican las coordenadas fraccionarias de corte con los ejes cristalográficos:
   $$\text{Intersecciones} = (p\, a,\, q\, b,\, r\, c) \implies (p, q, r)$$
   Si un plano es paralelo a un eje cristalográfico, su intersección se considera en el **infinito** ($\infty$).
3. **Cálculo de los Recíprocos:** Se toman los inversos de las intersecciones:
   $$h' = \frac{1}{p}, \quad k' = \frac{1}{q}, \quad l' = \frac{1}{r}$$
   (con la convención $\frac{1}{\infty} = 0$).
4. **Reducción a Enteros Mínimos:** Se eliminan fracciones multiplicando por el mínimo común múltiplo (MCM).
5. **Notación:** Se encierran entre **paréntesis redondos**: $(h\, k\, l)$. Índices negativos llevan barra superior: $(\bar{h}\, k\, l)$.
6. **Familias de Planos Equivalentes:** Se encierran entre **llaves**: $\{h\, k\, l\}$. Por ejemplo, en una red cúbica:
   $$\{100\} = \{(100), (\bar{1}00), (010), (0\bar{1}0), (001), (00\bar{1})\}$$
   $$\{111\} = \{(111), (\bar{1}11), (1\bar{1}1), (11\bar{1}), (\bar{1}\bar{1}1), (\bar{1}1\bar{1}), (1\bar{1}\bar{1}), (\bar{1}\bar{1}\bar{1})\}$$

### Propiedad de Perpendicularidad Exclusiva de Redes Cúbicas:
> En el sistema cúbico (y únicamente en él, debido a su métrica ortonormal isótropa $a=b=c$), la dirección $[h\, k\, l]$ es **rigurosamente ortogonal** al plano $(h\, k\, l)$:
> $$[h\, k\, l] \perp (h\, k\, l) \quad (\text{en cristales cúbicos})$$

---

## ⬡ 3. Notación de 4 Índices de Miller-Bravais para el Sistema Hexagonal

La celda hexagonal posee una simetría rotacional senaria ($60^\circ$) en el plano basal que no se refleja de forma transparente con 3 ejes ortogonales. Para preservar la equivalencia de simetría en los índices, se utiliza el sistema de **4 ejes** [Slides 50-52]:
* Tres ejes coplanares en el plano basal: $\vec{a}_1, \vec{a}_2, \vec{a}_3$, desfasados $120^\circ$ entre sí ($\vec{a}_1 + \vec{a}_2 + \vec{a}_3 = 0$).
* Un eje vertical perpendicular: $\vec{c} = [0001]$.

### Planos de Miller-Bravais $(h\, k\, i\, l)$:
Los índices corresponden a los recíprocos de intersección con $\vec{a}_1, \vec{a}_2, \vec{a}_3$ y $\vec{c}$. La geometría coplanar impone la **condición estricta de cierre**:
$$i = -(h + k)$$
* *Ejemplo:* El plano que corta a $a_1$ en 1, a $a_2$ en $\infty$ y a $c$ en $\infty$:
  Intersecciones: $(1, \infty, -1, \infty) \implies \text{Recíprocos}: (1, 0, -1, 0) \implies (10\bar{1}0)$. Verificación: $i = -(1 + 0) = -1$.
* El plano basal compacto del HCP es: $(0001)$ (o plano $\{0001\}$).

### Direcciones de Miller-Bravais $[u\, v\, t\, w]$:
Para transformar una dirección tridimensional convencional $[u'\, v'\, w']$ a la notación de 4 ejes $[u\, v\, t\, w]$ [Slide 51]:
$$u = \frac{1}{3}(2u' - v'), \quad v = \frac{1}{3}(2v' - u'), \quad t = -(u + v) = -\frac{1}{3}(u' + v'), \quad w = w'$$
* *Ejemplos clave en HCP:*
  * $[100] \to [2\bar{1}\bar{1}0]$ (dirección de máxima compacidad en el plano basal).
  * $[110] \to [11\bar{2}0]$.
  * $[001] \to [0001]$ (eje óptico / axial).

---

## 📊 4. Resumen de Convenciones de Notación Cristalográfica

| Entidad Cristalográfica | Notación Cúbica (3 índices) | Notación Hexagonal (4 índices) |
| :--- | :--- | :--- |
| **Punto en el espacio** | $x, y, z$ | $x, y, z$ |
| **Dirección específica** | $[u\, v\, w]$ | $[u\, v\, t\, w]$ con $t = -(u+v)$ |
| **Familia de direcciones** | $\langle u\, v\, w \rangle$ | $\langle u\, v\, t\, w \rangle$ |
| **Plano específico** | $(h\, k\, l)$ | $(h\, k\, i\, l)$ con $i = -(h+k)$ |
| **Familia de planos** | $\{h\, k\, l\}$ | $\{h\, k\, i\, l\}$ |

---
*Enlaces Bidireccionales:*
* `[[Concepto - Huecos Intersticiales Tetraedricos y Octaedricos|⬅️ Anterior: Huecos Intersticiales]]`
* `[[Concepto - Densidad Volumetrica Lineal y Planar en Redes Cristalinas|Siguiente: Densidad Volumétrica, Lineal y Planar ➡️]]`
