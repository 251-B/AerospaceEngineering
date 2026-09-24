---
materia: "Aerospace Materials I"
tema: "Tema 3: Diffusion in Solids and Mass Transport"
origen: "Problems T3_Diffusion.pdf, Problem 5"
dificultad: alta
tags:
  - problema-oficial
  - resuelto
  - ficks-second-law
  - carburization
  - arrhenius
  - error-function
  - steel-1010
  - inverse-temperature-design
---

# ✏️ Problema: T3-05 — Temperatura de Cementación de Acero AISI 1010 en 8 Horas

## 📄 Enunciado Oficial
> **5.- A 1010 steel, that contains $0.10\text{ wt}\%\text{ C}$ is subjected to cementation process, in order to obtain effective $\text{C}$ composition of $0.30\text{ wt}\%$ at a depth of $1.16\text{ mm}$ below the surface. Assume that the maximum $\text{C}$ solubility in the steel surface is reached at moment that the carburizing process is initiated, generating a $\text{C}$ concentration at the surface of $1.31\text{ wt}\%$. Determine the required cementation temperature for the process to be successfully carried out within an 8 hour time span.**  
> **Data: $D_0 (\text{C in Fe}) = 16.2\text{ mm}^2/\text{s}$; $E_D = 137\,800\text{ J/mol}$; $R = 8.314\text{ J/mol}\cdot\text{K}$.**  
> *(Solution: $T = 1175\text{ K} = 902^\circ\text{C}$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Hipótesis Físicas:
1. **Modelo Semi-Infinito No Estacionario:** La profundidad requerida de la capa cementada ($x = 1.16\text{ mm}$) es pequeña frente al espesor de la pieza, permitiendo la aplicación rigurosa de la solución en sólido semi-infinito de la Segunda Ley de Fick [Session 5 Slide 20].
2. **Saturación Superficial Instantánea:** Se asume que la concentración de carbono en la superficie alcanza instantáneamente el límite de solubilidad en equilibrio con la atmósfera carburizante y se mantiene fija durante todo el ciclo: $C_s = 1.31\text{ wt}\%$ para todo $t > 0$ [Slides 20, 30].
3. **Difusión Intersticial Regulada por Arrhenius:** El coeficiente de difusión $D$ del carbono en la austenita ($\gamma\text{-Fe}$) obedece la ley de Arrhenius con los parámetros cinéticos suministrados ($D_0$ y $E_D$) [Slide 26].

### Parámetros de Entrada:
* Concentración inicial uniforme de carbono en el acero 1010: $C_0 = 0.10\text{ wt}\%$
* Concentración superficial impuesta: $C_s = 1.31\text{ wt}\%$
* Concentración requerida a la profundidad de diseño: $C_x = 0.30\text{ wt}\%$
* Profundidad de diseño: $x = 1.16\text{ mm} = 1.16 \times 10^{-3}\text{ m}$
* Tiempo disponible del proceso: $t = 8\text{ h} = 8 \times 3600\text{ s} = 28\,800\text{ s}$
* Factor pre-exponencial de frecuencia: $D_0 = 16.2\text{ mm}^2/\text{s} = 16.2 \times 10^{-6}\text{ m}^2/\text{s}$
* Energía de activación de difusión: $E_D = 137\,800\text{ J/mol} = 137.8\text{ kJ/mol}$
* Constante universal de los gases ideales: $R = 8.314\text{ J/mol}\cdot\text{K}$

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

Este problema combina de forma elegante la **solución de la Segunda Ley de Fick** con la **ecuación térmica de Arrhenius** [Session 5 Slides 20, 26]:

### Etapa A: Determinación de la Difusividad Necesaria ($D$)
1. Aplicar la solución de la función error para sólido semi-infinito:
   $$\frac{C_s - C_x}{C_s - C_0} = \text{erf}(z)$$
2. Calcular el valor de $\text{erf}(z)$ a partir de las concentraciones dadas.
3. Determinar el argumento $z$ mediante interpolación lineal en la tabla oficial de $\text{erf}(z)$ [Slide 21].
4. Despejar la difusividad requerida $D$ a partir de la definición de $z$:
   $$z = \frac{x}{2\sqrt{Dt}} \implies 2\sqrt{Dt} = \frac{x}{z} \implies D = \frac{x^2}{4 \cdot z^2 \cdot t}$$

### Etapa B: Determinación de la Temperatura del Proceso ($T$)
5. Con el valor numérico de $D$, igualar a la ecuación de Arrhenius:
   $$D = D_0 \exp\left(-\frac{E_D}{RT}\right) \implies \frac{D}{D_0} = \exp\left(-\frac{E_D}{RT}\right)$$
6. Tomar logaritmo natural y despejar la temperatura absoluta $T$:
   $$\ln\left(\frac{D}{D_0}\right) = -\frac{E_D}{RT} \implies T = \frac{-E_D}{R \cdot \ln(D / D_0)} = \frac{E_D}{R \cdot \ln(D_0 / D)}$$

---

## 🔢 3. Fase 3: Deducción Matemática Paso a Paso

### 1. Cálculo del Cociente de Concentraciones:
$$\frac{C_s - C_x}{C_s - C_0} = \frac{1.31 - 0.30}{1.31 - 0.10} = \frac{1.01}{1.21} \approx \mathbf{0.83471074}$$

Por tanto, requerimos:
$$\text{erf}(z) = 0.83471074$$

---

### 2. Interpolación Lineal en la Tabla Oficial de la Función Error:
Consultando la tabla de $\text{erf}(z)$ de la asignatura [Session 5 Slide 21]:
* Para $z_1 = 0.95 \implies \text{erf}(z_1) = 0.8209$
* Para $z_2 = 1.00 \implies \text{erf}(z_2) = 0.8427$

Dado que $0.8209 < 0.83471074 < 0.8427$, interpolamos linealmente:
$$\frac{z - z_1}{z_2 - z_1} = \frac{\text{erf}(z) - \text{erf}(z_1)}{\text{erf}(z_2) - \text{erf}(z_1)}$$

Sustituyendo los valores:
$$\frac{z - 0.95}{1.00 - 0.95} = \frac{0.83471074 - 0.8209}{0.8427 - 0.8209}$$
$$\frac{z - 0.95}{0.05} = \frac{0.01381074}{0.0218} \approx 0.633520$$
$$z = 0.95 + 0.05 \times 0.633520 = 0.95 + 0.031676 = \mathbf{0.981676}$$

Elevando al cuadrado:
$$z^2 = (0.981676)^2 \approx \mathbf{0.963688}$$

---

### 3. Cálculo de la Difusividad Necesaria ($D$):
Sustituyendo $x = 1.16 \times 10^{-3}\text{ m}$, $t = 28\,800\text{ s}$ y $z^2 = 0.963688$:
* $x^2 = (1.16 \times 10^{-3}\text{ m})^2 = 1.3456 \times 10^{-6}\text{ m}^2$
* Denominador:
  $$4 \cdot z^2 \cdot t = 4 \times 0.963688 \times 28\,800\text{ s} = 111\,016.86\text{ s}$$
* Coeficiente de difusión en el SI:
  $$D = \frac{1.3456 \times 10^{-6}\text{ m}^2}{111\,016.86\text{ s}} \approx \mathbf{1.21207 \times 10^{-11}\text{ m}^2/\text{s}}$$

*(En $\text{mm}^2/\text{s}$: $D = 1.21207 \times 10^{-5}\text{ mm}^2/\text{s}$).*

---

### 4. Determinación de la Temperatura mediante Arrhenius:
Calculamos la relación entre $D$ y el factor pre-exponencial $D_0 = 16.2 \times 10^{-6}\text{ m}^2/\text{s}$:
$$\frac{D}{D_0} = \frac{1.21207 \times 10^{-11}\text{ m}^2/\text{s}}{16.2 \times 10^{-6}\text{ m}^2/\text{s}} \approx 7.48191 \times 10^{-7}$$

Tomando el logaritmo natural:
$$\ln\left(\frac{D}{D_0}\right) = \ln(7.48191 \times 10^{-7}) \approx -\mathbf{14.10657}$$

Despejando la temperatura absoluta $T$:
$$T = \frac{-E_D}{R \cdot \ln(D / D_0)} = \frac{-137\,800\text{ J/mol}}{(8.314\text{ J/mol}\cdot\text{K}) \times (-14.10657)}$$
$$T = \frac{137\,800}{117.282} \approx \mathbf{1174.95\text{ K}} \approx \mathbf{1175\text{ K}}$$

### Conversión a Escala Celsius:
$$T = 1174.95 - 273.15 = \mathbf{901.8^\circ\text{C}} \approx \mathbf{902^\circ\text{C}}$$

---

## 🔍 4. Fase 4: Interpretación y Verificación Física / Dimensional

### Análisis Dimensional:
* $[D] = \frac{[x]^2}{[t]} = \frac{\text{m}^2}{\text{s}} \quad \checkmark$
* $[T] = \frac{[E_D]}{[R] \cdot [\ln(D/D_0)]} = \frac{\text{J/mol}}{(\text{J/mol}\cdot\text{K}) \cdot 1} = \text{K} \quad \checkmark$

### Interpretación y Relevancia en Ingeniería:
1. **Control de Tiempo de Ciclo de Turno de Trabajo:** En la industria automotriz y aeroespacial, un ciclo de cementación de exactamente **8 horas** se sincroniza con un turno laboral completo. Conocer la temperatura precisa ($902^\circ\text{C}$) permite al ingeniero programar el horno con certeza de alcanzar la profundidad requerida de capa ($1.16\text{ mm}$ a $0.30\text{ wt}\%$) sin sobrecalentar la pieza [Slide 30].
2. **Estructura Austenítica Estable:** A $902^\circ\text{C}$ ($1175\text{ K}$), el acero AISI 1010 se sitúa holgadamente en el campo austenítico homogéneo ($\gamma\text{-Fe}$), donde la solubilidad de carbono alcanza hasta el $1.31\text{ wt}\%$ fijado superficialmente [Slides 23, 30].
3. **Optimización Energética:** Si se operara a una temperatura menor, e.g. $850^\circ\text{C}$, el tiempo requerido se triplicaría, reduciendo la productividad de la planta; por el contrario, temperaturas por encima de $950^\circ\text{C}$ acelerarían el proceso pero causarían un crecimiento indeseable del tamaño de grano austenítico, degradando la tenacidad final del núcleo del componente [Session 4 Slide 45; Session 5 Slide 30].

---

## 🔗 Enlaces Relacionados
* `[[Tema 3 - Diffusion in Solids and Mass Transport]]` (MOC Maestro del Tema 3)
* `[[Concepto - Segunda Ley de Fick Difusion en Estado No Estacionario y Funcion Error]]`
* `[[Concepto - Ecuacion de Arrhenius y Factores que Influyen en la Difusividad]]`
* `[[Concepto - Cementacion y Aplicaciones Industriales de la Difusion]]`
* `[[Problema - T3-01 Carburacion de Engranaje de Acero 1018]]`
