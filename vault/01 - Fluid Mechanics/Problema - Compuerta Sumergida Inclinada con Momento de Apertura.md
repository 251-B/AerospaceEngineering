---
materia: Fluid Mechanics
tema: "Tema 1: Estática de Fluidos"
origen: "Examen Final Oficial — Mecánica de Fluidos"
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
Planteamos el equilibrio estático de momentos respecto al eje de la bisagra $A$ ($\sum M_A = 0$):

1. **Momento hidrostático (abre la compuerta en sentido antihorario):**
   $$ M_{\text{hidro}} = F_R \cdot d_{A-CP} = 194\,179.14 \times 1.6969 = +329\,502.58\text{ N}\cdot\text{m} $$
2. **Momento del peso propio (cierra la compuerta en sentido horario):**
   El peso $W = 14\,715\text{ N}$ actúa en el $CG$ verticalmente hacia abajo. Su brazo horizontal respecto a $A$ es:
   $$ d_{\text{peso}} = \frac{L}{2} \cos\theta = 1.5 \times \cos(60^\circ) = 1.5 \times 0.5 = 0.75\text{ m} $$
   $$ M_{\text{peso}} = - W \cdot d_{\text{peso}} = - 14\,715 \times 0.75 = -11\,036.25\text{ N}\cdot\text{m} $$
3. **Momento de la fuerza horizontal de cierre $F_{\text{cierre}}$ aplicada en $B$:**
   La fuerza $F_{\text{cierre}}$ es horizontal hacia la izquierda. Su brazo vertical respecto a la bisagra $A$ es:
   $$ h_{AB} = L \cdot \sin\theta = 3.0 \times \sin(60^\circ) = 2.5981\text{ m} $$
   $$ M_{\text{cierre}} = - F_{\text{cierre}} \cdot (L \sin\theta) = - F_{\text{cierre}} \times 2.5981 $$

### Ecuación de equilibrio ($\sum M_A = 0$):
$$ M_{\text{hidro}} - M_{\text{peso}} - F_{\text{cierre}} (L \sin\theta) = 0 $$
$$ 329\,502.58 - 11\,036.25 - F_{\text{cierre}} (2.5981) = 0 $$
$$ 318\,466.33 = 2.5981 \cdot F_{\text{cierre}} $$

$$ \mathbf{F_{\text{cierre}} = \frac{318\,466.33}{2.5981} = 122\,576.62\text{ N} \approx 122.58\text{ kN}} $$

---

## 🎯 3. Resumen de Resultados
| Magnitud solicitada | Símbolo | Valor Numérico | Unidades |
| :--- | :--- | :--- | :--- |
| Fuerza hidrostática resultante | $F_R$ | **194.18** | $\text{kN}$ |
| Posición del Centro de Presiones desde $A$ | $d_{A-CP}$ | **1.70** | $\text{m}$ |
| Fuerza horizontal de cierre en el pie | $F_{\text{cierre}}$ | **122.58** | $\text{kN}$ |
