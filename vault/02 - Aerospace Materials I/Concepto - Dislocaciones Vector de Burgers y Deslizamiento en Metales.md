---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 4 T2 Structure of Materials II_2025.pdf, Slides 25-37"
tags:
  - teoria
  - concepto-fundamental
  - dislocaciones
  - vector-de-burgers
  - deslizamiento
  - slip-systems
  - ductilidad
dificultad: alta
prerrequisitos:
  - "[[Concepto - Estructuras Metalicas FCC BCC HCP y Factor de Empaquetamiento]]"
---

# 🌀 Concepto: Dislocaciones, Vector de Burgers y Deslizamiento en Metales

> **La Paradoja de la Resistencia Teórica:** El cálculo teórico de la tensión de cizalladura requerida para deslizar un plano de átomos simultáneamente sobre otro predice $\tau_{\text{teórica}} \approx \frac{G}{2\pi} \sim \frac{G}{10}$ (del orden de miles de megapascales). Sin embargo, los metales puros reales deforman plásticamente a tensiones experimentales 100 a 1000 veces inferiores ($\tau_{\text{exp}} \sim 10^{-4}\text{--}10^{-3}G$) [Slide 25]. Esta discrepancia se explica por la existencia y movimiento secuencial de **defectos lineales llamados dislocaciones** (propuestas teóricamente por Taylor, Orowan y Polanyi en 1934).

---

## 📐 1. Tipos de Dislocaciones y Circuito de Burgers

Una dislocación es una imperfección lineal unidimensional que separa una región que ha sufrido deslizamiento de otra que permanece intacta [Slides 25, 28].

```
Tipo de Dislocación    Línea de Dislocación (\vec{t}) vs Vector de Burgers (\vec{b})   Desplazamiento vs \vec{b}
─────────────────────────────────────────────────────────────────────────────────────────────────
Dislocación de Borde    \vec{b} \perp \vec{t}                                           \vec{b} || Dirección movimiento
Dislocación Helicoidal  \vec{b} \parallel \vec{t}                                       \vec{b} \perp Dirección movimiento
Dislocación Mixta       Ángulo genérico 0 < \theta < 90^\circ                          Comportamiento combinado
```

### 1. Dislocación de Borde o Taylor [Slide 28-29]:
* Se crea conceptualmente insertando un **semiplano extra de átomos** en la mitad superior del cristal.
* La línea de la dislocación ($\vec{t}$) es la arista de terminación inferior de dicho semiplano extra.
* Genera un campo elástico de tensiones asimétrico: **compresión** por encima del plano de deslizamiento y **tracción** por debajo.

### 2. Dislocación Helicoidal o Burgers [Slide 30]:
* Producida por una tensión de cizalladura que distorsiona el cristal de modo que los planos atómicos se convierten en una rampa helicoidal continua alrededor del eje de la dislocación.
* Genera únicamente un campo elástico de **cizalladura pura** (sin variación de volumen ni dilatación hidrostática).

### 3. Dislocación Mixta [Slide 31]:
* En un cristal real, las líneas de dislocación son bucles curvos continuos. Las regiones con orientación pura de borde o helicoidal son casos límite de una dislocación mixta cuyo vector de Burgers $\vec{b}$ es idéntico a lo largo de toda su trayectoria [Slide 31].

---

## 🔄 2. Definición Formal del Vector de Burgers ($\vec{b}$)

El **vector de Burgers $\vec{b}$** define la magnitud exacta y la dirección cristalográfica de la distorsión reticular causada por la dislocación [Slide 28].

### Procedimiento del Circuito de Burgers:
1. En un cristal perfecto de referencia, se traza un bucle cerrado recorriendo $m$ espaciados atómicos a la derecha, $n$ hacia abajo, $m$ a la izquierda y $n$ hacia arriba ($S \to E = 0$).
2. Se traza la misma trayectoria cerrada rodeando la línea de la dislocación en el cristal real.
3. El circuito no se cierra; el vector necesario para cerrar la trayectoria (desde el final hasta el inicio) es el **vector de Burgers $\vec{b}$** [Slide 28].

---

## ⚡ 3. Energía Elástica Almacenada y Criterio de Mínima Energía

La presencia de una dislocación introduce distorsiones elásticas en la red que almacenan energía elástica por unidad de longitud ($E$) [Slides 29, 35]:

$$E \propto |\vec{b}|^2$$

Específicamente, para una dislocación de borde $E_{\text{borde}} = \frac{G |\vec{b}|^2}{4\pi(1-\nu)} \ln\left(\frac{r_1}{r_0}\right)$ y para tornillo $E_{\text{tornillo}} = \frac{G |\vec{b}|^2}{4\pi} \ln\left(\frac{r_1}{r_0}\right)$.

### ¿Por qué el deslizamiento ocurre en direcciones de máximo empaquetamiento? [Slide 35]
La energía requerida para mover una dislocación es directamente proporcional a la energía elástica que introduce:
$$E_{\text{mov}} \propto |\vec{b}|^2$$

Para minimizar esta energía, el cristal **siempre selecciona los vectores de traslación reticular más cortos posibles**, los cuales corresponden rigurosamente a las **direcciones cristalográficas de máximo empaquetamiento**:
* En **FCC**:
  * Vector a lo largo de dirección compacta $\langle 110 \rangle$: $\vec{b} = \frac{a}{2}\langle 110 \rangle$.
    $$|\vec{b}|^2 = \left(\frac{a}{2}\right)^2 (1^2 + 1^2 + 0) = \frac{a^2}{2} = \frac{(2\sqrt{2}R)^2}{2} = 4R^2 \implies E_b \propto 4R^2$$
  * Si se deslizara en una dirección no compacta como $[100]$: $\vec{b} = a[100]$.
    $$|\vec{b}|^2 = a^2 = (2\sqrt{2}R)^2 = 8R^2 \implies E_b \propto 8R^2$$
  * Relación de energías:
    $$\frac{E_{[100]}}{E_{[110]}} = \frac{8R^2}{4R^2} = \mathbf{2}$$
    *(Demostración requerida en el Problema DEF07: mover una dislocación en $[100]$ cuesta el doble de energía que en $[110]$, por lo que la naturaleza siempre opta por $[110]$).*

---

## ✈️ 4. Sistemas de Deslizamiento y Origen de la Ductilidad

Un **sistema de deslizamiento** está constituido por la combinación de un **plano de deslizamiento** (plano de máxima densidad planar) y una **dirección de deslizamiento** (dirección de máxima densidad lineal) contenida en dicho plano [Slide 34, 36].

| Estructura Cristalina | Plano de Deslizamiento | Dirección de Deslizamiento | Número de Sistemas Activos | Ductilidad Macroscópica |
| :--- | :--- | :--- | :--- | :--- |
| **FCC ($\text{Al, Cu, Ni, Au}$)** | $\{111\}$ (4 planos) | $\langle 1\bar{1}0 \rangle$ (3 direcciones/plano) | $4 \times 3 = \mathbf{12\text{ sistemas}}$ | **Excepcional a cualquier temperatura** (incluso criogénica) |
| **BCC ($\alpha\text{-Fe, Mo, W, Ta}$)** | $\{110\}$ (6 planos) | $\langle \bar{1}11 \rangle$ (2 direcciones/plano) | $6 \times 2 = \mathbf{12\text{ sistemas}}$ | Buena a alta $T$, pero sufre **transición dúctil-frágil (DBTT)** |
| **HCP ($\text{Ti, Mg, Zn, Be}$)** | $(0001)$ basal (1 plano) | $\langle 11\bar{2}0 \rangle$ (3 direcciones) | $1 \times 3 = \mathbf{3\text{ sistemas}}$ | **Baja a temperatura ambiente** (requiere maclado para conformar) |

### Criterio de von Mises para Plasticidad Generalizada:
Para que un policristal sufra deformación plástica uniforme sin agrietarse en los límites de grano, se requieren al menos **5 sistemas de deslizamiento independientes**.
* **FCC:** Posee 12 sistemas muy densos e intersects en el espacio 3D $\implies$ máxima ductilidad y tenacidad de fractura (base de aleaciones aeroespaciales de Al y superaleaciones de Ni).
* **BCC:** Aunque tiene 12 sistemas, los planos $\{110\}$ no son atómicamente compactos, requiriendo activación térmica para superar la barrera de Peierls $\implies$ fragilidad a bajas temperaturas.
* **HCP:** Solo tiene 3 sistemas basales coplanares a $T_{\text{amb}} < 5$ $\implies$ fragilidad intrínseca a menos que se active deslizamiento prismático/piramidal a alta temperatura o maclado mecánico.

---
*Enlaces Bidireccionales:*
* `[[Concepto - Soluciones Solidas Sustitucionales e Intersticiales Reglas de Hume-Rothery|⬅️ Anterior: Soluciones Sólidas]]`
* `[[Concepto - Defectos Planares Limites de Grano Maclas y Ecuacion de Hall-Petch|Siguiente: Defectos Planares y Hall-Petch ➡️]]`
