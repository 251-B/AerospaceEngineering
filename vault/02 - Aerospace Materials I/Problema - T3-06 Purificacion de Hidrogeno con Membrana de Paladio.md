---
materia: "Aerospace Materials I"
tema: "Tema 3: Diffusion in Solids and Mass Transport"
origen: "Problems T3_Diffusion.pdf, Problem 6; Session 5 Slide 35"
dificultad: media
tags:
  - problema-oficial
  - resuelto
  - ficks-first-law
  - steady-state
  - palladium-membrane
  - hydrogen-purification
  - mass-flux
---

# ✏️ Problema: T3-06 — Purificación de Hidrógeno con Membrana de Paladio

## 📄 Enunciado Oficial
> **6.- Determine the thickness of a plate of $\text{Pd}$ with transversal area of $0.2\text{ m}^2$ so that it can purify $1.73 \times 10^{-3}\text{ kg/h}$ of hydrogen, if the hydrogen concentration at the side of high pressure of the plate is $1.5\text{ kg/m}^3$ and at the side of low pressure is $0.3\text{ kg/m}^3$. The diffusion coefficient of hydrogen in $\text{Pd}$ is $1 \times 10^{-8}\text{ m}^2/\text{s}$.**  
> *(Solution: $5\text{ mm}$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Hipótesis Físicas:
1. **Régimen Estacionario Puro:** Al mantenerse constantes e invariables en el tiempo las presiones parciales de hidrógeno gaseoso a ambos lados de la membrana de paladio ($\text{Pd}$), se establecen concentraciones constantes en ambas caras, originando un estado estacionario donde el flujo difusional $J$ es uniforme y constante en cualquier sección del espesor: $\partial C / \partial t = 0$ y $\partial J / \partial t = 0$ [Session 5 Slides 16, 35].
2. **Gradiente de Concentración Lineal:** Como el coeficiente de difusión del hidrógeno en el paladio es independiente de la concentración de soluto en este rango de presiones ($D \neq f(C)$), el perfil de concentración $C(x)$ a través de la membrana plana es rigurosamente una línea recta [Slide 17]:
   $$\frac{dC}{dx} = \frac{\Delta C}{\Delta x} = \text{constante}$$
3. **Flujo Unidimensional Perpendicular:** Se desprecian los efectos de borde en el perímetro de la placa, asumiendo un flujo difusional macroscópico puramente unidimensional perpendicular al área transversal $A$.

### Parámetros de Entrada:
* Área transversal de la membrana de paladio: $A = 0.2\text{ m}^2$
* Tasa de masa purificada (caudal másico): $\dot{m} = \frac{M}{t} = 1.73 \times 10^{-3}\text{ kg/h}$ (en diapositiva oficial $1.733 \times 10^{-3}\text{ kg/h}$)
* Concentración en la cara de alta presión ($x = 0$): $C_{\text{alta}} = C_1 = 1.5\text{ kg/m}^3$
* Concentración en la cara de baja presión ($x = \Delta x$): $C_{\text{baja}} = C_2 = 0.3\text{ kg/m}^3$
* Coeficiente de difusión de $\text{H}$ en $\text{Pd}$: $D = 1 \times 10^{-8}\text{ m}^2/\text{s}$

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

La velocidad de transporte de átomos de hidrógeno a través de la membrana viene cuantificada por la **densidad de flujo difusional** ($J$), definida formalmente como la masa que difunde por unidad de área y por unidad de tiempo [Session 5 Slide 15]:

$$J = \frac{\text{masa difusora}}{\text{área} \times \text{tiempo}} = \frac{\dot{m}}{A} \quad \left[\frac{\text{kg}}{\text{m}^2\cdot\text{s}}\right]$$

Por otro lado, la **Primera Ley de Fick** en estado estacionario para una membrana de espesor $\Delta x$ establece [Session 5 Slides 16, 35]:

$$J = -D \frac{\Delta C}{\Delta x} = -D \left(\frac{C_2 - C_1}{\Delta x}\right) = D \left(\frac{C_{\text{alta}} - C_{\text{baja}}}{\Delta x}\right)$$

### Estrategia de Resolución:
1. Convertir la tasa horaria de purificación $\dot{m}$ a unidades del SI ($\text{kg/s}$).
2. Calcular la densidad de flujo difusional $J = \frac{\dot{m}}{A}$.
3. Evaluar el salto de concentraciones $\Delta C = C_{\text{alta}} - C_{\text{baja}}$.
4. Igualar ambas expresiones del flujo y despejar el espesor de la membrana $\Delta x$:
   $$J = D \frac{\Delta C}{\Delta x} \implies \Delta x = \frac{D \cdot \Delta C}{J} = \frac{D \cdot (C_{\text{alta}} - C_{\text{baja}})}{J}$$
5. Expresar el resultado final en milímetros ($\text{mm}$).

---

## 🔢 3. Fase 3: Deducción Matemática Paso a Paso

### 1. Cálculo de la Densidad de Flujo Difusional ($J$):
* Caudal másico horario por unidad de área:
  $$\frac{\dot{m}}{A} = \frac{1.73 \times 10^{-3}\text{ kg/h}}{0.2\text{ m}^2} = 8.65 \times 10^{-3}\text{ kg/m}^2\cdot\text{h}$$
* Conversión a segundos ($1\text{ h} = 3600\text{ s}$):
  $$J = \frac{8.65 \times 10^{-3}\text{ kg/m}^2\cdot\text{h}}{3600\text{ s/h}} \approx \mathbf{2.4028 \times 10^{-6}\text{ kg/m}^2\cdot\text{s}}$$
  *(En Session 5 Slide 35 el profesor aproxima directamente $J = 2.4 \times 10^{-6}\text{ kg/m}^2\cdot\text{s}$).*

---

### 2. Gradiente de Concentración:
$$\Delta C = C_{\text{alta}} - C_{\text{baja}} = 1.5\text{ kg/m}^3 - 0.3\text{ kg/m}^3 = \mathbf{1.2\text{ kg/m}^3}$$

---

### 3. Despeje y Cálculo del Espesor ($\Delta x$):
Partiendo de:
$$J = D \frac{\Delta C}{\Delta x}$$

Despejamos el espesor $\Delta x$:
$$\Delta x = \frac{D \cdot \Delta C}{J}$$

Sustituyendo los valores numéricos:
$$\Delta x = \frac{(1.0 \times 10^{-8}\text{ m}^2/\text{s}) \times (1.2\text{ kg/m}^3)}{2.4028 \times 10^{-6}\text{ kg/m}^2\cdot\text{s}}$$
$$\Delta x = \frac{1.2 \times 10^{-8}}{2.4028 \times 10^{-6}}\text{ m} \approx \mathbf{4.994 \times 10^{-3}\text{ m}} \approx \mathbf{5.0 \times 10^{-3}\text{ m}}$$

*(Utilizando el redondeo del profesor de $J = 2.4 \times 10^{-6}\text{ kg/m}^2\cdot\text{s}$ [Slide 35]: $\Delta x = \frac{1.2 \times 10^{-8}}{2.4 \times 10^{-6}} = 5.0 \times 10^{-3}\text{ m}$).*

### Expresión en Milímetros:
$$\Delta x = 5.0 \times 10^{-3}\text{ m} \times 1000\text{ mm/m} = \mathbf{5\text{ mm}}$$

---

## 🔍 4. Fase 4: Interpretación y Verificación Física / Dimensional

### Análisis Dimensional:
$$[\Delta x] = \frac{[D] \cdot [\Delta C]}{[J]} = \frac{(\text{m}^2/\text{s}) \cdot (\text{kg/m}^3)}{\text{kg}/(\text{m}^2\cdot\text{s})} = \frac{\text{kg}/(\text{m}\cdot\text{s})}{\text{kg}/(\text{m}^2\cdot\text{s})} = \text{m} \quad \checkmark$$

### Interpretación Físico-Aeroespacial:
1. **Compromiso Estructural vs Difusional:** Un espesor de **$5\text{ mm}$** proporciona una resistencia estructural mecánica excelente para soportar diferenciales significativos de presión entre la cámara de gas impuro y la cámara de purificado sin riesgo de rotura o deformación por pandeo de la membrana [Slide 35].
2. **Cinética Intersticial del Hidrógeno:** La difusividad del hidrógeno en paladio ($D = 10^{-8}\text{ m}^2/\text{s}$) es excepcionalmente elevada en comparación con otros solutos metálicos (típicamente $10^{-12}\text{--}10^{-16}\text{ m}^2/\text{s}$), debido a que el átomo de hidrógeno es el elemento químico más pequeño del universo y se desliza a través de los huecos octaédricos y tetraédricos de la red FCC del $\text{Pd}$ con una energía de activación sumamente baja [Slides 13, 23].
3. **Aplicación en Células de Combustible Espaciales:** Esta tecnología de purificación por difusión en membranas de $\text{Pd}$ o aleaciones $\text{Pd-Ag}$ es el método estándar en sistemas aeroespaciales para garantizar que el hidrógeno suministrado a las pilas de combustible tipo PEM (*Proton Exchange Membrane*) esté libre de monóxido de carbono ($\text{CO}$), el cual envenenaría de forma irreversible los catalizadores de platino del electrodo [Slide 35].

---

## 🔗 Enlaces Relacionados
* `[[Tema 3 - Diffusion in Solids and Mass Transport]]` (MOC Maestro del Tema 3)
* `[[Concepto - Primera Ley de Fick Difusion en Estado Estacionario]]`
* `[[Concepto - Cementacion y Aplicaciones Industriales de la Difusion]]`
* `[[Problema - T3-04 Transporte Ionico de Niquel a Traves de Placa de MgO]]`
