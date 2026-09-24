---
materia: "Aerospace Materials I"
tema: "Tema 3: Diffusion in Solids and Mass Transport"
origen: "Problems T3_Diffusion.pdf, Problem 3"
dificultad: media
tags:
  - problema-oficial
  - resuelto
  - arrhenius
  - activation-energy
  - carbon-in-steel
  - two-point-method
---

# ✏️ Problema: T3-03 — Energía de Activación y Difusividad de Carbono en Acero Dulce

## 📄 Enunciado Oficial
> **3.- The diffusivity of carbon in mild steel was measured at two different temperatures:**  
> **Data: $R = 8.314\text{ J/mol}\cdot\text{K}$**  
> 
> | Temperature ($^\circ\text{C}$) | Diffusivity ($\text{m}^2/\text{s}$) |
> | :---: | :---: |
> | 850 | $4.826 \times 10^{-12}$ |
> | 950 | $1.805 \times 10^{-11}$ |
> 
> **Using these data, calculate:**  
> **a) The activation energy for the C diffusion in mild steel, for the temperature interval of $850^\circ\text{C}$ to $950^\circ\text{C}$ *(Solution: $E_D = 36\text{ kcal/mol}$)*.**  
> **b) The diffusivity at $1000^\circ\text{C}$, assuming that the activation energy does not change at this temperature range. *(Solution: $D = 3.23 \times 10^{-11}\text{ m}^2/\text{s}$)*.**

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Hipótesis Físicas:
1. **Comportamiento Arrhenius Monotónico:** La dependencia de la difusividad del carbono en la red austenítica del acero dulce ($\gamma\text{-Fe}$, FCC) sigue estrictamente la ley de Arrhenius en el intervalo térmico $850^\circ\text{C}\text{--}1000^\circ\text{C}$ sin que ocurran cambios de fase alotrópica en dicho rango ($T > 727^\circ\text{C}$, el acero se encuentra permanentemente en el campo austenítico) [Session 5 Slides 23-26].
2. **Invarianza de $E_D$ y $D_0$:** La energía de activación $E_D$ y el factor pre-exponencial $D_0$ permanecen constantes en el rango térmico considerado.

### Parámetros de Entrada:
* Estado 1: $T_1 = 850^\circ\text{C} = 850 + 273.15 = 1123.15\text{ K}$, con $D_1 = 4.826 \times 10^{-12}\text{ m}^2/\text{s}$
* Estado 2: $T_2 = 950^\circ\text{C} = 950 + 273.15 = 1223.15\text{ K}$, con $D_2 = 1.805 \times 10^{-11}\text{ m}^2/\text{s}$
* Estado 3 objetivo: $T_3 = 1000^\circ\text{C} = 1000 + 273.15 = 1273.15\text{ K}$, incógnita $D_3$
* Constante de los gases: $R = 8.314\text{ J/mol}\cdot\text{K}$
* Equivalencia calórica: $1\text{ cal} = 4.184\text{ J} \implies R = 1.987\text{ cal/mol}\cdot\text{K}$

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

La difusividad a dos temperaturas dadas obedece la ley de Arrhenius en forma de dos puntos [Session 5 Slide 26]:

$$D_1 = D_0 \exp\left(-\frac{E_D}{R T_1}\right), \qquad D_2 = D_0 \exp\left(-\frac{E_D}{R T_2}\right)$$

### Para el Apartado (a) — Determinación de $E_D$:
Dividiendo miembro a miembro para eliminar el factor pre-exponencial $D_0$:
$$\frac{D_2}{D_1} = \exp\left[-\frac{E_D}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)\right] = \exp\left[\frac{E_D}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)\right]$$

Tomando el logaritmo natural:
$$\ln\left(\frac{D_2}{D_1}\right) = \frac{E_D}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right) \implies E_D = \frac{R \cdot \ln(D_2 / D_1)}{\frac{1}{T_1} - \frac{1}{T_2}}$$

### Para el Apartado (b) — Determinación de $D_3$ a $1000^\circ\text{C}$:
Relacionando el estado 3 con el estado 2 (o el estado 1):
$$\ln\left(\frac{D_3}{D_2}\right) = -\frac{E_D}{R}\left(\frac{1}{T_3} - \frac{1}{T_2}\right) = \frac{E_D}{R}\left(\frac{1}{T_2} - \frac{1}{T_3}\right)$$
$$D_3 = D_2 \cdot \exp\left[\frac{E_D}{R}\left(\frac{1}{T_2} - \frac{1}{T_3}\right)\right]$$

---

## 🔢 3. Fase 3: Deducción Matemática Paso a Paso

### Apartado (a): Cálculo de la Energía de Activación ($E_D$)

1. **Razón de difusividades:**
   $$\frac{D_2}{D_1} = \frac{1.805 \times 10^{-11}\text{ m}^2/\text{s}}{4.826 \times 10^{-12}\text{ m}^2/\text{s}} = 3.7401575$$
   $$\ln\left(\frac{D_2}{D_1}\right) = \ln(3.7401575) \approx 1.319128$$

2. **Diferencia de inversos de temperatura:**
   $$\frac{1}{T_1} = \frac{1}{1123.15\text{ K}} \approx 8.903530 \times 10^{-4}\text{ K}^{-1}$$
   $$\frac{1}{T_2} = \frac{1}{1223.15\text{ K}} \approx 8.175612 \times 10^{-4}\text{ K}^{-1}$$
   $$\frac{1}{T_1} - \frac{1}{T_2} = (8.903530 - 8.175612) \times 10^{-4} = 7.27918 \times 10^{-5}\text{ K}^{-1}$$

   *(Si se emplea la escala entera $T_1 = 1123\text{ K}$ y $T_2 = 1223\text{ K}$: $\frac{1}{1123} - \frac{1}{1223} = 7.281 \times 10^{-5}\text{ K}^{-1}$).*

3. **Cálculo de $E_D$ en el SI ($\text{J/mol}$):**
   $$E_D = \frac{8.314\text{ J/mol}\cdot\text{K} \times 1.319128}{7.27918 \times 10^{-5}\text{ K}^{-1}} = \frac{10.96723}{7.27918 \times 10^{-5}} \approx \mathbf{150\,666\text{ J/mol}} = \mathbf{150.67\text{ kJ/mol}}$$

4. **Conversión a $\text{kcal/mol}$:**
   $$E_D = \frac{150\,666\text{ J/mol}}{4184\text{ J/kcal}} \approx \mathbf{36.01\text{ kcal/mol}} \approx \mathbf{36\text{ kcal/mol}}$$
   *(O utilizando $R = 1.987\text{ cal/mol}\cdot\text{K}$: $E_D = \frac{1.987 \times 1.319128}{7.27918 \times 10^{-5}} = 36009\text{ cal/mol} \approx \mathbf{36\text{ kcal/mol}}$).*

---

### Apartado (b): Cálculo de la Difusividad a $1000^\circ\text{C}$ ($T_3 = 1273.15\text{ K}$)

1. **Diferencia de inversos entre $T_2$ y $T_3$:**
   $$\frac{1}{T_3} = \frac{1}{1273.15\text{ K}} \approx 7.854534 \times 10^{-4}\text{ K}^{-1}$$
   $$\frac{1}{T_2} - \frac{1}{T_3} = (8.175612 - 7.854534) \times 10^{-4} = 3.21078 \times 10^{-5}\text{ K}^{-1}$$

2. **Evaluación del exponente térmico:**
   $$\Delta_{\text{exp}} = \frac{E_D}{R}\left(\frac{1}{T_2} - \frac{1}{T_3}\right) = \frac{150\,666\text{ J/mol}}{8.314\text{ J/mol}\cdot\text{K}} \times (3.21078 \times 10^{-5}\text{ K}^{-1})$$
   $$\Delta_{\text{exp}} = 18121.96 \times 3.21078 \times 10^{-5} \approx 0.581857$$

3. **Cálculo de la razón exponencial y difusividad final:**
   $$\exp(\Delta_{\text{exp}}) = e^{0.581857} \approx 1.78936$$
   $$D_3 = D_2 \times 1.78936 = (1.805 \times 10^{-11}\text{ m}^2/\text{s}) \times 1.78936 \approx \mathbf{3.2298 \times 10^{-11}\text{ m}^2/\text{s}} \approx \mathbf{3.23 \times 10^{-11}\text{ m}^2/\text{s}}$$

*(Nótese que la tabla oficial de Session 5 Slide 23 recoge exactamente este orden de magnitud: $D_{\text{C en Fe-FCC}} \approx 3 \times 10^{-11}\text{ m}^2/\text{s}$ a $1000^\circ\text{C}$).*

---

## 🔍 4. Fase 4: Interpretación y Verificación Física / Dimensional

### Coherencia Física y Dimensional:
1. **Análisis Dimensional:**
   * $[E_D] = \frac{[\text{J/mol}\cdot\text{K}]}{[\text{K}^{-1}]} = \text{J/mol} \quad \checkmark$
   * $[D_3] = [D_2] \cdot [e^{\text{adimensional}}] = \text{m}^2/\text{s} \quad \checkmark$
2. **Sensibilidad Térmica en Aceros:** Un incremento de solo $50^\circ\text{C}$ (de $950^\circ\text{C}$ a $1000^\circ\text{C}$) aumenta la difusividad en un factor de:
   $$\frac{D_{1000^\circ\text{C}}}{D_{950^\circ\text{C}}} = \frac{3.23 \times 10^{-11}}{1.805 \times 10^{-11}} \approx 1.79 \quad (+79\%)$$
   Esto explica por qué en tratamientos industriales de cementación se busca la máxima temperatura admisible de austenización, ya que acorta de forma drástica los tiempos de horno y reduce los costes energéticos, siempre que no se promueva un crecimiento de grano excesivo [Slides 25, 30].
3. **Magnitud de la Energía de Activación:** El valor de $E_D \approx 36\text{ kcal/mol} \approx 150.7\text{ kJ/mol}$ es característico de un mecanismo **intersticial** (donde el átomo de carbono migra entre huecos octaédricos de la red FCC sin necesidad de crear vacantes). Para auto-difusión sustitucional del hierro en la misma red FCC, la energía de activación requerida es casi el doble ($E_a \approx 290\text{ kJ/mol} \approx 70\text{ kcal/mol}$) [Slide 9].

---

## 🔗 Enlaces Relacionados
* `[[Tema 3 - Diffusion in Solids and Mass Transport]]` (MOC Maestro del Tema 3)
* `[[Concepto - Ecuacion de Arrhenius y Factores que Influyen en la Difusividad]]`
* `[[Concepto - Mecanismos de Difusion Vacantes e Intersticios]]`
* `[[Problema - T3-02 Difusion de Aluminio en Silicio Monocristalino]]`
* `[[Problema - T3-05 Temperatura de Cementacion de Acero 1010 en 8 Horas]]`
