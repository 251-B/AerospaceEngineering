---
materia: "Aerospace Materials I"
tema: "Tema 3: Diffusion in Solids and Mass Transport"
fuentes: "Session 5 T3  Difussion_2025.pdf, Slides 15-17, 35; Problems T3_Diffusion.pdf, Problem 6"
tags:
  - teoria
  - concepto-fundamental
  - ficks-laws
  - steady-state
  - diffusion-flux
  - membrane-purification
dificultad: media
prerrequisitos:
  - "[[Concepto - Mecanismos de Difusion Vacantes e Intersticios]]"
---

# 📏 Concepto: Primera Ley de Fick — Difusión en Estado Estacionario

> **Postulado Principal:** En condiciones de **estado estacionario** (*steady-state*), el perfil de concentraciones no cambia con el tiempo ($\partial C / \partial t = 0$), por lo que el **flujo difusional** $J$ es estrictamente constante a lo largo del tiempo ($\partial J / \partial t = 0$) [Slides 15-16].  
> El flujo neto de materia es directamente proporcional al gradiente espacial de concentración y se desplaza en sentido opuesto a dicho gradiente [Slide 16].

---

## 🌊 1. Definición del Flujo Difusional ($J$)

El flujo difusional o densidad de flujo ($J$) cuantifica la velocidad a la que los átomos o la masa atraviesan un plano de área unitaria perpendicular a la dirección de difusión por unidad de tiempo [Slide 15]:

$$J = \frac{M}{A \cdot t} = \frac{\text{moles (o masa) que difunden}}{\text{área} \times \text{tiempo}}$$

### Unidades en el SI y en Ingeniería:
* En unidades molares: $\left[\frac{\text{mol}}{\text{m}^2\cdot\text{s}}\right]$ o $\left[\frac{\text{mol}}{\text{cm}^2\cdot\text{s}}\right]$
* En unidades de masa: $\left[\frac{\text{kg}}{\text{m}^2\cdot\text{s}}\right]$
* En unidades atómicas: $\left[\frac{\text{átomos}}{\text{m}^2\cdot\text{s}}\right]$ o $\left[\frac{\text{átomos}}{\text{cm}^2\cdot\text{s}}\right]$

---

## ⚖️ 2. Formulación Matemática de la Primera Ley de Fick

Para un sistema unidimensional a lo largo del eje $x$, Adolf Fick (1855) formuló la relación constitutiva fundamental [Slide 16]:

$$J = -D \frac{\partial C}{\partial x}$$

En régimen puramente estacionario a través de una pared o membrana plana de espesor $\Delta x = x_2 - x_1$, el gradiente de concentración es constante y lineal [Slides 16-17]:

$$J = -D \frac{\Delta C}{\Delta x} = -D \left(\frac{C_2 - C_1}{x_2 - x_1}\right) = D \left(\frac{C_{\text{alta}} - C_{\text{baja}}}{\Delta x}\right)$$

### Significado Físico de las Variables:
* $J$: Flujo difusional ($\text{kg}/\text{m}^2\cdot\text{s}$ o $\text{mol}/\text{m}^2\cdot\text{s}$).
* $D$: **Difusividad** o coeficiente de difusión del soluto en la matriz ($\text{m}^2/\text{s}$ o $\text{cm}^2/\text{s}$).
* $\frac{\Delta C}{\Delta x}$: **Gradiente de concentración** ($\text{kg}/\text{m}^4$ o $\text{mol}/\text{m}^4$).
* **Signo Negativo:** Indica que el transporte neto de masa ocurre espontáneamente desde regiones de alta concentración hacia regiones de baja concentración (en sentido decreciente del gradiente, "cuesta abajo" en potencial químico) [Slide 16].

---

## 🔬 3. Perfil de Concentración Lineal a Través de Membranas

Cuando dos medios con concentraciones químicas constantes $C_{\text{ext}}$ y $C_{\text{int}}$ ($C_{\text{ext}} > C_{\text{int}}$) se mantienen a ambos lados de una membrana plana o placa metálica de espesor $\Delta x$, el sistema alcanza un estado estacionario estable [Slide 17]:

$$\frac{\partial C}{\partial t} = 0 \iff \frac{\partial J}{\partial x} = 0 \implies \frac{d^2 C}{dx^2} = 0$$

Integrando dos veces respecto a $x$:
$$C(x) = C_{\text{ext}} - \left(\frac{C_{\text{ext}} - C_{\text{int}}}{\Delta x}\right) x$$

El perfil espacial de concentración es estrictamente una **recta decreciente**, y el flujo $J$ se mantiene invariante a través de cualquier plano transversal a lo largo del espesor de la membrana [Slide 17].

---

## 🚀 4. Aplicación Aeroespacial: Purificación de $\text{H}_2$ mediante Membrana de Paladio ($\text{Pd}$)

Una aplicación industrial y aeroespacial fundamental de la primera ley de Fick es la purificación de hidrógeno gaseoso para pilas de combustible espaciales y reactores químicos de alta pureza [Slide 35]:

* El hidrógeno diatómico gas ($\text{H}_2$) se adsorbe en la cara de alta presión de una chapa de Paladio puro ($\text{Pd}$), se disocia en átomos de $\text{H}$ y difunde de manera intersticial a través de la red FCC del $\text{Pd}$ hacia la cara de baja presión, donde se recombina en gas $\text{H}_2$ ultrapuro.
* Si el área de la membrana es $A$ y la tasa másica requerida de purificación es $\dot{m} = M/t$:
  $$J = \frac{\dot{m}}{A}$$
* Igualando con la Primera Ley de Fick:
  $$\frac{\dot{m}}{A} = D \frac{C_{\text{alta}} - C_{\text{baja}}}{\Delta x} \implies \Delta x = \frac{D \cdot A \cdot (C_{\text{alta}} - C_{\text{baja}})}{\dot{m}}$$

*(Véase resolución numérica detallada en `[[Problema - T3-06 Purificacion de Hidrogeno con Membrana de Paladio]]`).*

---

## 🔗 Enlaces Relacionados
* `[[Tema 3 - Diffusion in Solids and Mass Transport]]` (MOC Maestro del Tema 3)
* `[[Concepto - Mecanismos de Difusion Vacantes e Intersticios]]`
* `[[Concepto - Segunda Ley de Fick Difusion en Estado No Estacionario y Funcion Error]]`
* `[[Concepto - Ecuacion de Arrhenius y Factores que Influyen en la Difusividad]]`
* `[[Problema - T3-04 Transporte Ionico de Niquel a Traves de Placa de MgO]]`
* `[[Problema - T3-06 Purificacion de Hidrogeno con Membrana de Paladio]]`
