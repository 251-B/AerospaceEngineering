---
materia: "Aerospace Materials I"
tema: "Tema 3: Diffusion in Solids and Mass Transport"
origen: "Problems T3_Diffusion.pdf, Problem 4"
dificultad: alta
tags:
  - problema-oficial
  - resuelto
  - ficks-first-law
  - ceramic-diffusion
  - steady-state
  - ionic-transport
  - mgo
  - fcc-nickel
---

# ✏️ Problema: T3-04 — Transporte Iónico de Níquel a Través de Placa Cerámica de MgO

## 📄 Enunciado Oficial
> **4.- A plate of magnesium oxide of $0.1\text{ cm}$ thickness separates two metallic blocks, one of $\text{Ni}$ and one of $\text{Ta}$. At $1400^\circ\text{C}$ $\text{Ni}$ ions diffuse through the $\text{MgO}$ plate. The diffusion coefficient of $\text{Ni}$ in $\text{MgO}$ is $9 \times 10^{-12}\text{ cm}^2/\text{s}$ and the lattice parameter of (fcc) $\text{Ni}$ at $1400^\circ\text{C}$ is $3.6 \times 10^{-8}\text{ cm}$. Determine the time necessary for sufficient $\text{Ni}^{2+}$ ions to pass through the ceramic material so that the thickness of the block of $\text{Ni}$ is reduced by one micron.**  
> *(Solution: $t = 309\text{ h}$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Hipótesis Físicas:
1. **Régimen Estacionario Cuasi-Permanente:** Debido al espesor relativamente grande de la placa cerámica de óxido de magnesio ($\Delta x = 0.1\text{ cm} = 1000\ \mu\text{m}$) en comparación con la reducción microscópica del bloque de níquel ($\Delta h = 1\ \mu\text{m}$), el transporte de cationes $\text{Ni}^{2+}$ a través de la cerámica se produce en condiciones de **estado estacionario** según la Primera Ley de Fick [Session 5 Slides 16-17].
2. **Condiciones de Contorno en las Interfaces:**
   * En la interfaz izquierda ($\text{Ni}/\text{MgO}$ en $x = 0$): el óxido de magnesio se encuentra en íntimo contacto con el bloque de níquel metálico puro, por lo que la concentración volumétrica de níquel disponible en la interfaz coincide con la densidad atómica del níquel metálico: $C_1 = \rho_{\text{at, Ni}}$.
   * En la interfaz derecha ($\text{MgO}/\text{Ta}$ en $x = \Delta x$): el tántalo actúa como sumidero perfecto consumiendo o reaccionando instantáneamente con los iones de níquel emergentes para formar intermetálicos o disolverse, fijando una concentración prácticamente nula: $C_2 \approx 0$ [Slide 16].
3. **Estructura Cristalina del Níquel:** A $1400^\circ\text{C}$, el níquel metálico cristaliza en red Cúbica Centrada en las Caras (FCC), con $n = 4$ átomos por celda unidad y parámetro de red $a = 3.6 \times 10^{-8}\text{ cm}$ [Session 3 Slide 15; Session 5 Slide 23].

### Parámetros de Entrada:
* Espesor de la placa de $\text{MgO}$: $\Delta x = 0.1\text{ cm} = 1.0 \times 10^{-3}\text{ m}$
* Temperatura del sistema: $T = 1400^\circ\text{C} = 1673.15\text{ K}$
* Coeficiente de difusión de $\text{Ni}$ en $\text{MgO}$: $D = 9 \times 10^{-12}\text{ cm}^2/\text{s} = 9 \times 10^{-16}\text{ m}^2/\text{s}$
* Parámetro de red del níquel FCC: $a = 3.6 \times 10^{-8}\text{ cm} = 3.6 \times 10^{-10}\text{ m}$
* Reducción requerida del espesor de níquel: $\Delta h = 1\ \mu\text{m} = 10^{-4}\text{ cm} = 10^{-6}\text{ m}$

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

### 1. Densidad Atómica del Bloque de Níquel ($\rho_{\text{at, Ni}}$):
En una red cristalina FCC, el número de átomos por celda unidad es $n = 4$, y el volumen de la celda es $V_C = a^3$. La densidad volumétrica atómica de níquel en el bloque metálico viene dada por [Session 3 Slide 15]:

$$\rho_{\text{at, Ni}} = \frac{n}{a^3} = \frac{4}{a^3} \quad \left[\frac{\text{átomos}}{\text{cm}^3}\right]$$

### 2. Cantidad de Átomos a Transferir por Unidad de Área ($N/A$):
Para reducir el espesor del bloque metálico de área $A$ en una magnitud $\Delta h$, el volumen de níquel que debe disolverse y difundir es:
$$V_{\text{perdido}} = A \cdot \Delta h$$

El número total de átomos de níquel necesarios por unidad de área transversal es:
$$\frac{N}{A} = \rho_{\text{at, Ni}} \cdot \Delta h = \frac{4 \cdot \Delta h}{a^3} \quad \left[\frac{\text{átomos}}{\text{cm}^2}\right]$$

### 3. Flujo Difusional Estacionario a Través del Cerámico (Primera Ley de Fick):
Según la Primera Ley de Fick [Session 5 Slide 16]:
$$J = -D \frac{\Delta C}{\Delta x} = D \frac{C_1 - C_2}{\Delta x} = D \frac{\rho_{\text{at, Ni}} - 0}{\Delta x} = D \frac{\rho_{\text{at, Ni}}}{\Delta x} \quad \left[\frac{\text{átomos}}{\text{cm}^2\cdot\text{s}}\right]$$

### 4. Relación Fundamental y Cancelación de la Densidad Atómica:
El flujo difusional constante $J$ representa precisamente la tasa de átomos que atraviesan la unidad de área por unidad de tiempo:
$$J = \frac{N / A}{t}$$

Igualando ambas expresiones del flujo:
$$\frac{\rho_{\text{at, Ni}} \cdot \Delta h}{t} = D \frac{\rho_{\text{at, Ni}}}{\Delta x}$$

Nótese el extraordinario resultado analítico: **la densidad atómica $\rho_{\text{at, Ni}}$ se cancela formalmente en ambos miembros de la ecuación**:

$$\frac{\Delta h}{t} = \frac{D}{\Delta x} \implies t = \frac{\Delta x \cdot \Delta h}{D}$$

La tasa de retroceso superficial de la chapa de níquel depende exclusivamente de la difusividad en la barrera cerámica y del espesor de ésta.

---

## 🔢 3. Fase 3: Deducción Matemática Paso a Paso

### 1. Cálculo Explícito de la Densidad Atómica de Níquel:
* Volumen de la celda unidad FCC:
  $$V_C = a^3 = (3.6 \times 10^{-8}\text{ cm})^3 = 4.6656 \times 10^{-23}\text{ cm}^3$$
* Densidad atómica:
  $$\rho_{\text{at, Ni}} = \frac{4\text{ átomos}}{4.6656 \times 10^{-23}\text{ cm}^3} \approx \mathbf{8.5734 \times 10^{22}\text{ átomos/cm}^3}$$

---

### 2. Número de Átomos por Unidad de Área para $\Delta h = 1\ \mu\text{m} = 10^{-4}\text{ cm}$:
$$\frac{N}{A} = (8.5734 \times 10^{22}\text{ átomos/cm}^3) \times (10^{-4}\text{ cm}) = \mathbf{8.5734 \times 10^{18}\text{ átomos/cm}^2}$$

---

### 3. Cálculo del Flujo Difusional Estacionario ($J$):
Con $C_1 = 8.5734 \times 10^{22}\text{ átomos/cm}^3$, $C_2 = 0$, $D = 9 \times 10^{-12}\text{ cm}^2/\text{s}$ y $\Delta x = 0.1\text{ cm}$:
$$J = D \frac{C_1}{\Delta x} = (9 \times 10^{-12}\text{ cm}^2/\text{s}) \times \frac{8.5734 \times 10^{22}\text{ átomos/cm}^3}{0.1\text{ cm}}$$
$$J = (9 \times 10^{-12}) \times (8.5734 \times 10^{23}) \approx \mathbf{7.71605 \times 10^{12}\text{ átomos/cm}^2\cdot\text{s}}$$

---

### 4. Determinación del Tiempo Requerido ($t$):
$$t = \frac{N / A}{J} = \frac{8.5734 \times 10^{18}\text{ átomos/cm}^2}{7.71605 \times 10^{12}\text{ átomos/cm}^2\cdot\text{s}} \approx \mathbf{1.1111 \times 10^6\text{ s}}$$

O mediante la expresión compacta deducida:
$$t = \frac{\Delta x \cdot \Delta h}{D} = \frac{(0.1\text{ cm}) \times (10^{-4}\text{ cm})}{9 \times 10^{-12}\text{ cm}^2/\text{s}} = \frac{10^{-5}\text{ cm}^2}{9 \times 10^{-12}\text{ cm}^2/\text{s}} = \frac{1}{9} \times 10^7\text{ s} \approx \mathbf{1.1111 \times 10^6\text{ s}}$$

### Conversión a Horas:
$$t = \frac{1.1111 \times 10^6\text{ s}}{3600\text{ s/h}} \approx \mathbf{308.64\text{ h}} \approx \mathbf{309\text{ h}}$$

---

## 🔍 4. Fase 4: Interpretación y Verificación Física / Dimensional

### Análisis Dimensional:
$$[t] = \frac{[\Delta x] \cdot [\Delta h]}{[D]} = \frac{\text{cm} \cdot \text{cm}}{\text{cm}^2/\text{s}} = \text{s} \quad \checkmark$$

### Interpretación Físico-Cerámica:
1. **Barrera de Difusión Cerámica:** Los óxidos cerámicos refractarios como el $\text{MgO}$ (estructura cristalina tipo sal gema $\text{NaCl}$) poseen energías reticulares muy elevadas y fuertes enlaces iónicos $\text{Mg}^{2+}\text{--}\text{O}^{2-}$. Por ello, a pesar de someter el sistema a una temperatura extrema de $1400^\circ\text{C}$ (próxima a la fusión del níquel, $T_m = 1452^\circ\text{C}$), el coeficiente de difusión del níquel es sumamente bajo ($9 \times 10^{-12}\text{ cm}^2/\text{s}$).
2. **Durabilidad Temporal:** Se requieren **$309\text{ horas}$** (casi 13 días continuos) para desgastar apenas una micra superficial ($1\ \mu\text{m}$) de níquel. Esto demuestra por qué las capas cerámicas delgadas de óxido se emplean masivamente en ingeniería aeroespacial como **recubrimientos de barrera térmica y de difusión** (*diffusion barriers*) en superaleaciones de álabes de turbina para evitar la interdifusión destructiva entre metales disímiles [Session 5 Slide 33].

---

## 🔗 Enlaces Relacionados
* `[[Tema 3 - Diffusion in Solids and Mass Transport]]` (MOC Maestro del Tema 3)
* `[[Concepto - Primera Ley de Fick Difusion en Estado Estacionario]]`
* `[[Concepto - Mecanismos de Difusion Vacantes e Intersticios]]`
* `[[Problema - T3-06 Purificacion de Hidrogeno con Membrana de Paladio]]`
