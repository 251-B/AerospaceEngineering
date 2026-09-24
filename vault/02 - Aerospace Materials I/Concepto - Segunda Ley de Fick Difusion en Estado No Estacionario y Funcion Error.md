---
materia: "Aerospace Materials I"
tema: "Tema 3: Diffusion in Solids and Mass Transport"
fuentes: "Session 5 T3  Difussion_2025.pdf, Slides 18-21; Problems T3_Diffusion.pdf, Table & Problems 1, 5"
tags:
  - teoria
  - concepto-fundamental
  - ficks-laws
  - non-steady-state
  - error-function
  - erf
  - carburization
  - semi-infinite-solid
dificultad: alta
prerrequisitos:
  - "[[Concepto - Primera Ley de Fick Difusion en Estado Estacionario]]"
---

# 📉 Concepto: Segunda Ley de Fick — Difusión en Estado No Estacionario y Función Error

> **Principio Físico:** En la gran mayoría de los procesos de ingeniería y tratamientos térmicos (como la carburación superficial de engranajes y la difusión de dopantes en semiconductores), las condiciones son de **estado no estacionario o transitorio** (*non-steady state*): la concentración de soluto en cualquier punto del sólido varía continuamente con el tiempo ($\partial C / \partial t \neq 0$) y el flujo difusional depende tanto de la posición como del tiempo ($J = J(x, t)$) [Slides 18-19].

---

## 📐 1. Deducción y Ecuación Diferencial Fundamental

Consideremos un elemento de volumen diferencial de sección transversal $A$ y longitud $\Delta x$. La tasa de acumulación de soluto en el volumen elemental viene dada por el balance de conservación de masa:

$$\text{Acumulación} = \text{Entrada} - \text{Salida}$$
$$A \cdot \Delta x \cdot \frac{\partial C_x}{\partial t} = A \cdot J(x) - A \cdot J(x + \Delta x)$$

Dividiendo entre el volumen $A \cdot \Delta x$ y tomando el límite cuando $\Delta x \to 0$:
$$\frac{\partial C_x}{\partial t} = -\frac{\partial J}{\partial x}$$

Sustituyendo el flujo difusional dado por la Primera Ley de Fick ($J = -D \frac{\partial C_x}{\partial x}$):
$$\frac{\partial C_x}{\partial t} = \frac{\partial}{\partial x}\left( D \frac{\partial C_x}{\partial x} \right) \quad \text{[Slide 18]}$$

### Hipótesis Canónica: $D \neq f(C)$
Cuando el coeficiente de difusión $D$ es independiente de la concentración local del soluto (válido para soluciones sólidas diluidas donde no hay interacción mutua entre átomos difusores), la difusividad $D$ sale fuera de la derivada espacial, conduciendo a la **Segunda Ley de Fick canónica** [Slide 19]:

$$\frac{\partial C_x}{\partial t} = D \frac{\partial^2 C_x}{\partial x^2}$$

* $\frac{\partial C_x}{\partial t}$: Tasa de variación temporal de la composición a una profundidad $x$.
* $D$: Difusividad del soluto en la matriz ($\text{m}^2/\text{s}$).
* $\frac{\partial^2 C_x}{\partial x^2}$: Curvatura o tasa de cambio del gradiente de concentración.

---

## 🏛️ 2. Solución Analítica para un Sólido Semi-Infinito

En procesos de cementación superficial (*carburizing*) y tratamientos termoquímicos, la profundidad de penetración del soluto ($\sim 1\text{ mm}$) es despreciable frente al espesor de la pieza (engranaje, eje o chapa), por lo que la geometría se modela con extraordinaria precisión como un **sólido semi-infinito** ($0 \le x < \infty$) [Slide 20].

### Condiciones Iniciales y de Contorno Oficiales [Slides 20-21]:
1. **Condición inicial ($t = 0$):** El sólido posee una concentración inicial homogénea de soluto $C_0$ en toda su profundidad:
   $$C(x, 0) = C_0 \quad \text{para } 0 \le x \le \infty$$
2. **Condición de contorno superficial ($t > 0$):** La superficie ($x = 0$) se pone instantáneamente en contacto con una atmósfera gaseosa rica en soluto, fijando una concentración superficial constante $C_s$:
   $$C(0, t) = C_s \quad \text{para } t > 0$$
3. **Condición de contorno en el infinito ($t > 0$):** En el núcleo profundo del sólido, la concentración se mantiene inalterada:
   $$C(\infty, t) = C_0 \quad \text{para } t > 0$$

### Solución en Términos de la Función Error de Gauss ($\text{erf}$):
Mediante la transformación de similitud $z = \frac{x}{2\sqrt{Dt}}$, la ecuación diferencial en derivadas parciales se reduce a una ecuación diferencial ordinaria cuya solución exacta es [Slides 20-21]:

$$\frac{C_x - C_0}{C_s - C_0} = 1 - \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right)$$

O de forma equivalente:
$$\frac{C_s - C_x}{C_s - C_0} = \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right) = \text{erf}(z)$$

donde:
* $C_x$: Concentración de soluto a una distancia $x$ de la superficie tras un tiempo $t$.
* $C_s$: Concentración superficial de soluto impuesta por el medio circundante ($x = 0$).
* $C_0$: Concentración inicial uniforme de soluto en el material.
* $x$: Distancia perpendicular desde la superficie hacia el interior del sólido ($\text{m}$).
* $t$: Tiempo transcurrido de difusión ($\text{s}$).
* $z = \frac{x}{2\sqrt{Dt}}$: Variable adimensional de similitud.

---

## 📊 3. La Función Error de Gauss ($\text{erf}$) y sus Propiedades

La función error de Gauss se define formalmente como la integral normalizada de una curva acampanada gaussiana [Slide 20]:

$$\text{erf}(z) \equiv \frac{2}{\sqrt{\pi}} \int_0^z e^{-\xi^2} d\xi$$

### Propiedades Matemáticas Esenciales:
1. $\text{erf}(0) = 0 \implies \frac{C_x - C_0}{C_s - C_0} = 1 \implies C_x(0, t) = C_s$ (coherencia en la superficie).
2. $\text{erf}(\infty) = 1 \implies \frac{C_x - C_0}{C_s - C_0} = 0 \implies C_x(\infty, t) = C_0$ (coherencia en el infinito).
3. Simetría impar (antisimétrica): $\text{erf}(-z) = -\text{erf}(z)$.
4. Función complementaria error: $\text{erfc}(z) \equiv 1 - \text{erf}(z)$.

---

## 📋 4. Tabla Oficial de Valores de $\text{erf}(z)$ e Interpolación Lineal

A continuación se transcribe íntegra la **tabla oficial de la UC3M** [Session 5 Slide 21; Problems T3_Diffusion.pdf]:

| $z$ | $\text{erf}(z)$ | $z$ | $\text{erf}(z)$ |
| :---: | :---: | :---: | :---: |
| **0.00** | 0.0000 | **0.70** | 0.6778 |
| **0.01** | 0.0113 | **0.75** | 0.7112 |
| **0.02** | 0.0226 | **0.80** | 0.7421 |
| **0.03** | 0.0338 | **0.85** | 0.7707 |
| **0.04** | 0.0451 | **0.90** | 0.7969 |
| **0.05** | 0.0564 | **0.95** | 0.8209 |
| **0.10** | 0.1125 | **1.00** | 0.8427 |
| **0.15** | 0.1680 | **1.10** | 0.8802 |
| **0.20** | 0.2227 | **1.20** | 0.9103 |
| **0.25** | 0.2763 | **1.30** | 0.9340 |
| **0.30** | 0.3286 | **1.40** | 0.9523 |
| **0.35** | 0.3794 | **1.50** | 0.9661 |
| **0.40** | 0.4284 | **1.60** | 0.9763 |
| **0.45** | 0.4755 | **1.70** | 0.9838 |
| **0.50** | 0.5205 | **1.80** | 0.9891 |
| **0.55** | 0.5633 | **1.90** | 0.9928 |
| **0.60** | 0.6039 | **2.00** | 0.9953 |
| **0.65** | 0.6420 | | |

### Algoritmo de Interpolación Lineal Exacto:
Dado un valor diana de la función error $\text{erf}(z)$ ubicado entre dos valores tabulados contiguos $\text{erf}(z_1)$ y $\text{erf}(z_2)$ (con $z_1 \le z \le z_2$):

$$\frac{z - z_1}{z_2 - z_1} = \frac{\text{erf}(z) - \text{erf}(z_1)}{\text{erf}(z_2) - \text{erf}(z_1)}$$

Despejando el argumento adimensional $z$:
$$z = z_1 + \left[ \frac{\text{erf}(z) - \text{erf}(z_1)}{\text{erf}(z_2) - \text{erf}(z_1)} \right] (z_2 - z_1)$$

A partir de $z$, el tiempo de tratamiento requerido o la profundidad de penetración se despeja inmediatamente mediante:
$$z = \frac{x}{2\sqrt{Dt}} \implies t = \frac{x^2}{4 z^2 D} \quad \text{o} \quad x = 2 z \sqrt{Dt}$$

---

## 🔗 Enlaces Relacionados
* `[[Tema 3 - Diffusion in Solids and Mass Transport]]` (MOC Maestro del Tema 3)
* `[[Concepto - Primera Ley de Fick Difusion en Estado Estacionario]]`
* `[[Concepto - Ecuacion de Arrhenius y Factores que Influyen en la Difusividad]]`
* `[[Concepto - Cementacion y Aplicaciones Industriales de la Difusion]]`
* `[[Problema - T3-01 Carburacion de Engranaje de Acero 1018]]`
* `[[Problema - T3-05 Temperatura de Cementacion de Acero 1010 en 8 Horas]]`
