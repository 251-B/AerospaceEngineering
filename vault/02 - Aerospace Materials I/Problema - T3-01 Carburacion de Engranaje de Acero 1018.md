---
materia: "Aerospace Materials I"
tema: "Tema 3: Diffusion in Solids and Mass Transport"
origen: "Problems T3_Diffusion.pdf, Problem 1"
dificultad: media
tags:
  - problema-oficial
  - resuelto
  - ficks-second-law
  - carburization
  - error-function
  - steel-1018
  - semi-infinite-solid
---

# ✏️ Problema: T3-01 — Carburación de Engranaje de Acero AISI 1018

## 📄 Enunciado Oficial
> **1. In a steel gear of grade 1018 (0.18 wt% in C) a cementation process is carried out at $927^\circ\text{C}$. Calculate the time required in order to increase the C content up to $0.3\text{ wt}\%$ at $0.6\text{ mm}$ below the surface of the gear. Assume that the C content in the surface is $1\text{ wt}\%$. Data: $D_{\text{C in } \gamma\text{-Fe}} = 1.28 \times 10^{-11}\text{ m}^2/\text{s}$.**  
> *(Solution: $t = 6636\text{ s}$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Hipótesis Físicas:
1. **Sólido Semi-Infinito:** Dado que la profundidad de cementación requerida ($x = 0.6\text{ mm}$) es órdenes de magnitud menor que las dimensiones macroscópicas del diente del engranaje (típicamente $10\text{--}50\text{ mm}$), la difusión puede modelarse de forma exacta como unidimensional en un sólido semi-infinito ($0 \le x < \infty$) [Session 5 Slide 20].
2. **Concentración Superficial Constante:** La atmósfera reactiva de gas metano e hidrógeno ($\text{CH}_4 - \text{H}_2$) mantiene una actividad química de carbono constante en la superficie de la pieza durante todo el tratamiento: $C(0, t) = C_s = 1.0\text{ wt}\%$ para todo $t > 0$ [Slides 20, 30].
3. **Composición Inicial Homogénea:** El acero original de grado AISI 1018 contiene una fracción másica uniforme de carbono en todo su volumen: $C(x, 0) = C_0 = 0.18\text{ wt}\%$.
4. **Difusividad Constante:** Se asume que el coeficiente de difusión del carbono en austenita ($\gamma\text{-Fe}$, estructura FCC) es invariante con la concentración local en este rango composicional ($0.18\text{--}1.0\text{ wt}\%$): $D \neq f(C)$ [Slide 19].

### Parámetros de Entrada:
* Concentración inicial uniforme en el acero: $C_0 = 0.18\text{ wt}\%$
* Concentración superficial impuesta: $C_s = 1.00\text{ wt}\%$
* Concentración requerida a la profundidad de interés: $C_x = 0.30\text{ wt}\%$
* Profundidad de tratamiento: $x = 0.6\text{ mm} = 0.6 \times 10^{-3}\text{ m} = 6.0 \times 10^{-4}\text{ m}$
* Temperatura de operación: $T = 927^\circ\text{C} = 927 + 273.15 = 1200.15\text{ K}$
* Coeficiente de difusión proporcionado: $D = 1.28 \times 10^{-11}\text{ m}^2/\text{s}$

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

La difusión de carbono en estado no estacionario en un medio semi-infinito con concentración superficial constante se rige por la solución analítica de la **Segunda Ley de Fick** expresada mediante la función error de Gauss [Session 5 Slide 20]:

$$\frac{C_x - C_0}{C_s - C_0} = 1 - \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right)$$

Reordenando en términos directos de la función error:
$$\frac{C_s - C_x}{C_s - C_0} = \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right) = \text{erf}(z)$$

donde definimos el argumento adimensional:
$$z \equiv \frac{x}{2\sqrt{Dt}}$$

### Estrategia de Resolución:
1. Evaluar el cociente adimensional de concentraciones $\frac{C_s - C_x}{C_s - C_0}$.
2. Igualar este valor numérico a $\text{erf}(z)$ y consultar la **Tabla Oficial de la Función Error** de la asignatura [Session 5 Slide 21].
3. Realizar una **interpolación lineal exacta** entre los dos valores tabulados contiguos para determinar el argumento $z$ con máxima precisión.
4. Despejar el tiempo de tratamiento $t$ a partir de la definición de $z$:
   $$z = \frac{x}{2\sqrt{Dt}} \implies 2\sqrt{Dt} = \frac{x}{z} \implies Dt = \frac{x^2}{4z^2} \implies t = \frac{x^2}{4z^2 D}$$

---

## 🔢 3. Fase 3: Deducción Matemática Paso a Paso

### 1. Cálculo del Cociente de Concentraciones:
Sustituyendo los valores del enunciado:
$$\frac{C_s - C_x}{C_s - C_0} = \frac{1.00 - 0.30}{1.00 - 0.18} = \frac{0.70}{0.82} = \frac{35}{41} \approx 0.8536585$$

Por tanto:
$$\text{erf}(z) = 0.8536585$$

---

### 2. Búsqueda e Interpolación Lineal en la Tabla Oficial:
Examinando la tabla oficial de $\text{erf}(z)$ [Session 5 Slide 21; Problems T3]:
* Para $z_1 = 1.00 \implies \text{erf}(z_1) = 0.8427$
* Para $z_2 = 1.10 \implies \text{erf}(z_2) = 0.8802$

Dado que $0.8427 < 0.8536585 < 0.8802$, aplicamos la fórmula de interpolación lineal:
$$\frac{z - z_1}{z_2 - z_1} = \frac{\text{erf}(z) - \text{erf}(z_1)}{\text{erf}(z_2) - \text{erf}(z_1)}$$

Sustituyendo los valores:
$$\frac{z - 1.00}{1.10 - 1.00} = \frac{0.8536585 - 0.8427}{0.8802 - 0.8427}$$
$$\frac{z - 1.00}{0.10} = \frac{0.0109585}{0.0375} \approx 0.292227$$
$$z = 1.00 + 0.10 \times 0.292227 = 1.00 + 0.029223 = \mathbf{1.02922}$$

Elevando al cuadrado el valor de $z$:
$$z^2 = (1.02922)^2 \approx \mathbf{1.05930}$$

---

### 3. Despeje y Cálculo del Tiempo de Cementación ($t$):
Partiendo de:
$$z = \frac{x}{2\sqrt{Dt}}$$

Despejamos algebraicamente el tiempo $t$:
$$\sqrt{t} = \frac{x}{2z\sqrt{D}} \implies t = \frac{x^2}{4 \cdot z^2 \cdot D}$$

Sustituyendo las magnitudes en unidades coherentes del SI ($x = 6.0 \times 10^{-4}\text{ m}$, $D = 1.28 \times 10^{-11}\text{ m}^2/\text{s}$):
$$x^2 = (6.0 \times 10^{-4}\text{ m})^2 = 3.60 \times 10^{-7}\text{ m}^2$$
$$4 \cdot z^2 \cdot D = 4 \times 1.05930 \times 1.28 \times 10^{-11}\text{ m}^2/\text{s} = 5.4236 \times 10^{-11}\text{ m}^2/\text{s}$$

Efectuando el cociente:
$$t = \frac{3.60 \times 10^{-7}\text{ m}^2}{5.4236 \times 10^{-11}\text{ m}^2/\text{s}} \approx \mathbf{6637.6\text{ s}}$$

*(Tomando redondeos intermedios típicos de examen: $t \approx \mathbf{6636\text{ s}}$).*

### Conversión a Horas:
$$t = \frac{6636\text{ s}}{3600\text{ s/h}} \approx \mathbf{1.843\text{ h}} \quad (\approx 1\text{ hora, } 50\text{ minutos y } 36\text{ segundos})$$

---

## 🔍 4. Fase 4: Interpretación y Verificación Física / Dimensional

### Análisis Dimensional:
$$[t] = \frac{[x]^2}{[z]^2 \cdot [D]} = \frac{\text{m}^2}{1 \cdot (\text{m}^2/\text{s})} = \text{s} \quad \checkmark$$

### Interpretación Físico-Metalúrgica:
1. **Viabilidad Industrial:** Un tiempo de tratamiento de aproximadamente **$1.84\text{ horas}$** a $927^\circ\text{C}$ es extraordinariamente razonable y económicamente viable para un ciclo de carburación superficial en hornos industriales continuos de engranajes [Slide 30].
2. **Efecto de la Temperatura:** La temperatura elegida ($927^\circ\text{C} = 1200\text{ K}$) sitúa al acero en fase austenítica pura ($\gamma\text{-Fe}$), donde la solubilidad máxima del carbono supera el $1.0\text{ wt}\%$, permitiendo alcanzar el $1\text{ wt}\%$ superficial deseado sin precipitación prematura de carburos masivos perjudiciales en la superficie [Slide 24].
3. **Resistencia a Fatiga:** La difusión de carbono a $0.6\text{ mm}$ asegura una capa endurecida (*case depth*) suficiente para soportar las altas presiones hertzianas de contacto entre dientes de engranajes y generar tensiones residuales de compresión que impiden el agrietamiento por fatiga [Slide 30].

---

## 🔗 Enlaces Relacionados
* `[[Tema 3 - Diffusion in Solids and Mass Transport]]` (MOC Maestro del Tema 3)
* `[[Concepto - Segunda Ley de Fick Difusion en Estado No Estacionario y Funcion Error]]`
* `[[Concepto - Cementacion y Aplicaciones Industriales de la Difusion]]`
* `[[Problema - T3-05 Temperatura de Cementacion de Acero 1010 en 8 Horas]]`
