---
materia: Fluid Mechanics
tema: "Tema 1: Estática de Fluidos"
origen: "NOT found among the ten official hydrostatics problem sheets in the unit-05-hydrostatics folder of the fluid-mechanics sources (fluid_statics_1 to fluid_statics_10); the statement and the label 'Examen Final Oficial' must be re-verified against the original exam"
dificultad: alta
tags:
  - problema-examen
  - resuelto
  - compuertas
  - centro-de-presiones
---

# ✏️ Problema: Compuerta Articulada Inclinada con Fuerza de Cierre

## 📄 Enunciado
Una compuerta rectangular homogénea de ancho $b = 2.0\text{ m}$ (perpendicular al papel) y longitud $L = 3.0\text{ m}$ separa un depósito de agua dulce ($\rho = 1000\text{ kg/m}^3$) del exterior a presión atmosférica. La compuerta está articulada sin rozamiento en su borde superior $A$, el cual se encuentra sumergido a una profundidad vertical $h_A = 2.0\text{ m}$ bajo la superficie libre del agua. La compuerta forma un ángulo $\theta = 60^\circ$ con la superficie horizontal libre del agua.

La masa propia de la compuerta es $M = 1500\text{ kg}$. En el extremo inferior $B$, un tope horizontal impide que la compuerta se abra espontáneamente.

**Se pide:**
1. Calcular la fuerza hidrostática total $F_R$ ejercida por el agua sobre la compuerta.
2. Determinar la distancia medida a lo largo de la compuerta desde la bisagra $A$ hasta el centro de presiones $CP$ ($d_{A-CP}$).
3. Determinar la fuerza horizontal mínima $F_{\text{cierre}}$ que debe aplicarse en el extremo inferior $B$ para mantener la compuerta cerrada si se retira el tope.  
*(Dato: $g = 9.81\text{ m/s}^2$)*.

---

## 📊 1. Identificación de Datos e Hipótesis

### Geometría y Fluido:
* $ b = 2.0\text{ m} $ (ancho), $ L = 3.0\text{ m} $ (longitud) $\implies \text{Área } A = b \cdot L = 6.0\text{ m}^2 $
* $ \theta = 60^\circ \implies \sin(60^\circ) = \frac{\sqrt{3}}{2} \approx 0.8660 $
* $ h_A = 2.0\text{ m} $ (profundidad vertical de la bisagra)
* $ \rho = 1000\text{ kg/m}^3, \quad g = 9.81\text{ m/s}^2 $
* Masa de la compuerta: $ M = 1500\text{ kg} \implies W = M \cdot g = 1500 \times 9.81 = 14\,715\text{ N} $

---

## 🔢 2. Resolución Matemática Paso a Paso

### Apartado 1: Magnitud de la Fuerza Hidrostática ($F_R$)
La profundidad vertical del centro de gravedad de la compuerta ($CG$) es:
$$ h_{CG} = h_A + \frac{L}{2} \sin\theta = 2.0 + \frac{3.0}{2} \sin(60^\circ) = 2.0 + 1.5 \times 0.8660 = 2.0 + 1.299 = \mathbf{3.299\text{ m}} $$

Presión relativa en el $CG$:
$$ p_{CG} = \rho g h_{CG} = 1000 \times 9.81 \times 3.299 = 32\,363.19\text{ Pa} $$

Fuerza hidrostática resultante:
$$ F_R = p_{CG} \cdot A = 32\,363.19 \times 6.0 = \mathbf{194\,179.14\text{ N}} \approx \mathbf{194.18\text{ kN}} $$

---

### Apartado 2: Localización del Centro de Presiones ($CP$)
Definimos la coordenada $y$ a lo largo del plano de la compuerta con origen en la superficie libre ($y=0$ donde la prolongación de la compuerta corta la superficie):
$$ y_A = \frac{h_A}{\sin\theta} = \frac{2.0}{\sin(60^\circ)} = 2.3094\text{ m} $$
$$ y_{CG} = y_A + \frac{L}{2} = 2.3094 + 1.5 = 3.8094\text{ m} $$

Momento de inercia baricéntrico de la sección rectangular:
$$ I_{xx,CG} = \frac{b \cdot L^3}{12} = \frac{2.0 \times (3.0)^3}{12} = \frac{54}{12} = 4.5\text{ m}^4 $$

Coordenada del centro de presiones a lo largo del plano:
$$ y_{CP} = y_{CG} + \frac{I_{xx,CG}}{y_{CG} \cdot A} = 3.8094 + \frac{4.5}{3.8094 \times 6.0} = 3.8094 + \frac{4.5}{22.8564} = 3.8094 + 0.1969 = 4.0063\text{ m} $$

Distancia desde la bisagra $A$ hasta el $CP$:
$$ d_{A-CP} = y_{CP} - y_A = 4.0063 - 2.3094 = \mathbf{1.6969\text{ m}} \approx \mathbf{1.70\text{ m}} $$
*(Nótese que está $19.7\text{ cm}$ por debajo del baricentro que se sitúa a $1.50\text{ m}$ de $A$)*.

---

### Apartado 3: Fuerza Horizontal de Cierre en $B$ ($F_{\text{cierre}}$)
**Assumption (the statement does not say on which side of the gate the water lies).** Free-body diagram of the gate, axes with origin at the hinge $A$, $x$ horizontal (positive to the right), $y$ vertical (positive upward), $z$ out of the page. The gate runs from $A$ down to $B$ with $B$ at $\vec{r}_B = (L\cos\theta,\,-L\sin\theta)$ relative to $A$, i.e. to the right of and below $A$. **The water is assumed to lie on the lower-left face of the gate** (the gate leans over the water, the free surface being $h_A = 2.0\text{ m}$ above $A$), so the hydrostatic force acts on the gate along the outward normal $\vec{n} = (\sin\theta,\,\cos\theta)$ (upward and to the right). The horizontal force $F_{\text{cierre}}$ at $B$ points to the left, as in the statement of the closing force. Sign convention: $\sum M_A = 0$ with **counter-clockwise positive**, $M_z = r_x F_y - r_y F_x$ (moment arms measured from $A$).

1. **Hydrostatic moment.** $\vec{F}_R = F_R(\sin\theta,\cos\theta)$ acts at $\vec{r}_{CP} = d_{A-CP}(\cos\theta,-\sin\theta)$:
   $$ M_{\text{hidro}} = r_x F_y - r_y F_x = d_{A-CP}F_R\left(\cos^2\theta + \sin^2\theta\right) = F_R\, d_{A-CP} = 194\,181 \times 1.6969 = +329\,503\text{ N}\cdot\text{m} $$
   (counter-clockwise: it tends to open the gate). Cross-check by direct integration along the gate, $s\in[0,L]$ from $A$: $M = \rho g \sin\theta\, b\int_0^L (y_A + s)\,s\,ds = \rho g\sin\theta\, b\left(y_A\frac{L^2}{2} + \frac{L^3}{3}\right) = 329\,503\text{ N}\cdot\text{m}$.
2. **Weight.** $\vec{W} = (0,-W)$, $W = 14\,715\text{ N}$, acts at $CG$, $\vec{r}_{CG} = \frac{L}{2}(\cos\theta,-\sin\theta)$. Horizontal moment arm $d_{\text{peso}} = \frac{L}{2}\cos\theta = 0.75\text{ m}$:
   $$ M_{\text{peso}} = r_x F_y - r_y F_x = 0.75 \times (-W) - 0 = -14\,715 \times 0.75 = -11\,036.25\text{ N}\cdot\text{m} $$
   (clockwise: it tends to close the gate).
3. **Closing force.** $\vec{F}_{\text{cierre}} = (-F_{\text{cierre}},0)$ at $\vec{r}_B$. Vertical moment arm $h_{AB} = L\sin\theta = 3.0\times 0.8660 = 2.5981\text{ m}$:
   $$ M_{\text{cierre}} = r_x F_y - r_y F_x = 0 - (-L\sin\theta)(-F_{\text{cierre}}) = - F_{\text{cierre}}\,(L\sin\theta) $$
   (clockwise).

### Ecuación de equilibrio ($\sum M_A = 0$, counter-clockwise positive):
$$ M_{\text{hidro}} + M_{\text{peso}} + M_{\text{cierre}} = 0 $$
$$ 329\,503 - 11\,036.25 - F_{\text{cierre}}\,(2.5981) = 0 $$
$$ 318\,466 = 2.5981 \cdot F_{\text{cierre}} $$

$$ \mathbf{F_{\text{cierre}} = \frac{318\,466}{2.5981} = 122\,578\text{ N} \approx 122.58\text{ kN}\ \text{(to the left)}} $$

> [!warning] Dependence on the water side
> The weight reduces the force needed only if the hydrostatic moment and the weight moment have opposite senses, which holds for the configuration assumed above. If instead the water lay on the upper-right face of the same gate (gate sloping down under the water), the hydrostatic moment would be $-329\,503\text{ N}\cdot\text{m}$ (clockwise), the weight moment would still be $-11\,036.25\text{ N}\cdot\text{m}$, and a closing force pointing to the **right** would be needed: $F_{\text{cierre}} = (329\,503 + 11\,036.25)/2.5981 = 131.07\text{ kN}$. The value $122.58\text{ kN}$ is therefore specific to the stated assumption. The earlier line "$M_{\text{hidro}} - M_{\text{peso}} - \dots$" subtracted an already negative $M_{\text{peso}}$ while the numbers used it as a restoring moment; the equation above removes that sign inconsistency without changing the numerical value for this configuration.

---

## 🎯 3. Resumen de Resultados
| Magnitud solicitada | Símbolo | Valor Numérico | Unidades |
| :--- | :--- | :--- | :--- |
| Fuerza hidrostática resultante | $F_R$ | **194.18** | $\text{kN}$ |
| Posición del Centro de Presiones desde $A$ | $d_{A-CP}$ | **1.70** | $\text{m}$ |
| Fuerza horizontal de cierre en el pie | $F_{\text{cierre}}$ | **122.58** | $\text{kN}$ |
