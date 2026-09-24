---
materia: "Aerospace Materials I"
tema: "Tema 3: Diffusion in Solids and Mass Transport"
origen: "Problems T3_Diffusion.pdf, Problem 2"
dificultad: media
tags:
  - problema-oficial
  - resuelto
  - arrhenius
  - semiconductors
  - silicon-doping
  - activation-energy
---

# ✏️ Problema: T3-02 — Difusión de Aluminio en Silicio Monocristalino

## 📄 Enunciado Oficial
> **2.- Al can diffuse in a Si monocrystal. Calculate the temperature at which the diffusion coefficient will have a value of $10^{-14}\text{ m}^2/\text{s}$? Data: $E_D = 73\text{ kcal/mol}$; $D_0 = 1.55 \times 10^{-4}\text{ m}^2/\text{s}$ and $R = 1.987\text{ cal/mol}\cdot\text{K}$.**  
> *(Solution: $T = 1566\text{ K}$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Hipótesis Físicas:
1. **Régimen de Activación Térmica Simple:** La difusión de impurezas aceptoras de Aluminio en la red de diamante del monocristal de Silicio obedece de forma rigurosa la ecuación de Arrhenius en el rango de temperaturas elevadas de dopaje de obleas [Session 5 Slides 5, 26, 29].
2. **Constancia de Parámetros Cinéticos:** Tanto el factor pre-exponencial $D_0$ como la energía de activación $E_D$ se consideran independientes de la temperatura en el intervalo termodinámico de interés.
3. **Homogeneidad Cristalina:** Al tratarse de un monocristal de Silicio libre de límites de grano, no existen vías de difusión rápida en cortocircuito; la única contribución es la difusión volumétrica en la red reticular pura [Slide 25].

### Parámetros de Entrada:
* Coeficiente de difusión deseado: $D = 10^{-14}\text{ m}^2/\text{s} = 1.0 \times 10^{-14}\text{ m}^2/\text{s}$
* Factor pre-exponencial de frecuencia: $D_0 = 1.55 \times 10^{-4}\text{ m}^2/\text{s}$
* Energía de activación de difusión: $E_D = 73\text{ kcal/mol} = 73\,000\text{ cal/mol}$
* Constante universal de los gases ideales: $R = 1.987\text{ cal/mol}\cdot\text{K}$

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

La difusividad en sólidos en función de la temperatura se formula mediante la ecuación de Arrhenius [Session 5 Slide 26]:

$$D = D_0 \exp\left(-\frac{E_D}{RT}\right)$$

### Estrategia de Resolución:
1. Aislar el término exponencial dividiendo ambos miembros entre $D_0$:
   $$\frac{D}{D_0} = \exp\left(-\frac{E_D}{RT}\right)$$
2. Aplicar el logaritmo natural ($\ln$) a ambos miembros para linealizar la relación:
   $$\ln\left(\frac{D}{D_0}\right) = -\frac{E_D}{RT} \iff \ln\left(\frac{D_0}{D}\right) = \frac{E_D}{RT}$$
3. Despejar analíticamente la temperatura absoluta $T$ en Kelvin:
   $$T = \frac{E_D}{R \cdot \ln(D_0 / D)} = \frac{-E_D}{R \cdot \ln(D / D_0)}$$
4. Evaluar numéricamente y convertir a grados Celsius ($^\circ\text{C} = \text{K} - 273.15$) para contrastar la viabilidad experimental.

---

## 🔢 3. Fase 3: Deducción Matemática Paso a Paso

### 1. Cálculo de la Razón de Difusividades:
Evaluamos el cociente entre el factor pre-exponencial $D_0$ y el coeficiente objetivo $D$:
$$\frac{D_0}{D} = \frac{1.55 \times 10^{-4}\text{ m}^2/\text{s}}{1.0 \times 10^{-14}\text{ m}^2/\text{s}} = 1.55 \times 10^{10}$$

---

### 2. Evaluación del Logaritmo Natural:
Tomando el logaritmo natural del cociente:
$$\ln\left(\frac{D_0}{D}\right) = \ln(1.55 \times 10^{10}) = \ln(1.55) + 10 \cdot \ln(10)$$

Calculando con precisión decimal:
* $\ln(1.55) \approx 0.438255$
* $\ln(10) \approx 2.302585 \implies 10 \cdot \ln(10) \approx 23.025851$
* Sumando:
  $$\ln\left(\frac{D_0}{D}\right) = 0.438255 + 23.025851 = \mathbf{23.464106}$$

*(Si se evalúa como $\ln(D/D_0)$: $\ln\left(\frac{10^{-14}}{1.55 \times 10^{-4}}\right) = -23.464106$).*

---

### 3. Cálculo de la Temperatura Absoluta ($T$):
Sustituyendo los valores en unidades consistentes de calorías ($\text{cal}$):
* $E_D = 73\,000\text{ cal/mol}$
* $R = 1.987\text{ cal/mol}\cdot\text{K}$
* Denominador:
  $$R \cdot \ln\left(\frac{D_0}{D}\right) = (1.987\text{ cal/mol}\cdot\text{K}) \times (23.464106) = 46.62318\text{ cal/mol}\cdot\text{K}$$

Efectuando el cociente final:
$$T = \frac{73\,000\text{ cal/mol}}{46.62318\text{ cal/mol}\cdot\text{K}} \approx \mathbf{1565.77\text{ K}} \approx \mathbf{1566\text{ K}}$$

### Conversión a Escala Celsius:
$$T = 1565.77 - 273.15 = \mathbf{1292.62^\circ\text{C}} \approx \mathbf{1293^\circ\text{C}}$$

---

## 🔍 4. Fase 4: Interpretación y Verificación Física / Dimensional

### Análisis Dimensional:
$$[T] = \frac{[E_D]}{[R] \cdot [\text{adimensional}]} = \frac{\text{cal/mol}}{(\text{cal/mol}\cdot\text{K})} = \text{K} \quad \checkmark$$

### Interpretación Físico-Tecnológica:
1. **Procesado Térmico de Semiconductores:** La temperatura obtenida ($1293^\circ\text{C} = 1566\text{ K}$) se encuentra por debajo del punto de fusión del Silicio puro ($T_{m,\text{Si}} = 1414^\circ\text{C} = 1687\text{ K}$), satisfaciendo la condición de solidez requerida:
   $$\frac{T}{T_m} = \frac{1566\text{ K}}{1687\text{ K}} \approx 0.928 \, T_m$$
   Este rango de temperatura ultra-alta ($1200\text{--}1300^\circ\text{C}$) es el habitualmente empleado en hornos de difusión tubular con atmósfera inerte de argón para crear uniones $p\text{-}n$ profundas en electrónica de potencia y células solares aeroespaciales [Slides 29, 32].
2. **Elevada Energía de Activación:** El valor de $E_D = 73\text{ kcal/mol} \approx 305.4\text{ kJ/mol}$ es muy alto porque el silicio posee una red covalente tridimensional de diamante extraordinariamente rígida con enlaces directos $sp^3$, donde el movimiento de impurezas sustitucionales como el aluminio requiere romper enlaces covalentes intensos [Session 2 Slide 20; Session 5 Slide 9].

---

## 🔗 Enlaces Relacionados
* `[[Tema 3 - Diffusion in Solids and Mass Transport]]` (MOC Maestro del Tema 3)
* `[[Concepto - Ecuacion de Arrhenius y Factores que Influyen en la Difusividad]]`
* `[[Problema - T3-03 Energia de Activacion y Difusividad de Carbono en Acero]]`
* `[[Problema - T3-05 Temperatura de Cementacion de Acero 1010 en 8 Horas]]`
