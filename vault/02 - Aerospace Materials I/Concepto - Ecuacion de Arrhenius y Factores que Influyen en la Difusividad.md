---
materia: "Aerospace Materials I"
tema: "Tema 3: Diffusion in Solids and Mass Transport"
fuentes: "Session 5 T3  Difussion_2025.pdf, Slides 23-27; Problems T3_Diffusion.pdf, Problems 2, 3, 5"
tags:
  - teoria
  - concepto-fundamental
  - arrhenius
  - activation-energy
  - diffusivity
  - crystal-structure
  - grain-boundary-diffusion
dificultad: media
prerrequisitos:
  - "[[Concepto - Mecanismos de Difusion Vacantes e Intersticios]]"
---

# 🌡️ Concepto: Ecuación de Arrhenius y Factores que Influyen en la Difusividad

> **Principio de Activación Térmica:** La difusividad $D$ no es una constante universal, sino una propiedad de transporte altamente dependiente de la temperatura y de las características cristaloquímicas del par soluto-disolvente [Slide 23]. Al aumentar la temperatura, se incrementa exponencialmente la energía cinética media de los átomos y la probabilidad de que superen la barrera energética de salto, acelerando drásticamente el proceso difusional [Slide 26].

---

## 📈 1. La Ecuación de Arrhenius para la Difusividad

La dependencia térmica del coeficiente de difusión ($D$) sigue con gran rigor experimental la ley fenomenológica de Svante Arrhenius [Slide 26]:

$$D = D_0 \exp\left(-\frac{E_D}{RT}\right)$$

### Significado Físico de las Variables:
* $D$: Coeficiente de difusión o difusividad a la temperatura absoluta $T$ ($\text{m}^2/\text{s}$ o $\text{cm}^2/\text{s}$).
* $D_0$: **Factor de frecuencia pre-exponencial** ($\text{m}^2/\text{s}$ o $\text{cm}^2/\text{s}$), independiente de la temperatura, determinado por la frecuencia de vibración atómica en la red ($\nu_0 \sim 10^{13}\text{ s}^{-1}$), el factor de entropía de migración y la distancia geométrica de salto [Slide 26].
* $E_D$ (o $E_a$): **Energía de activación de difusión** ($\text{J/mol}$ o $\text{cal/mol}$), que representa la energía mínima necesaria para que un mol de átomos ejecute el salto a una vacante o intersticio [Slide 26].
* $R$: Constante universal de los gases ideales ($8.314\text{ J/mol}\cdot\text{K} = 1.987\text{ cal/mol}\cdot\text{K}$).
* $T$: Temperatura absoluta en Kelvin ($\text{K} = ^\circ\text{C} + 273.15$).

---

## 📉 2. Linealización de Arrhenius y Formulación de Dos Temperaturas

Tomando el logaritmo natural en ambos miembros de la ecuación [Slide 26]:

$$\ln D = \ln D_0 - \left(\frac{E_D}{R}\right) \frac{1}{T}$$

Esta expresión tiene la estructura de una línea recta $y = y_0 + m x$:
* Eje de ordenadas ($y$): $\ln D$.
* Eje de abscisas ($x$): $\frac{1}{T}$ ($\text{K}^{-1}$).
* Ordenada en el origen ($y_0$): $\ln D_0$.
* Pendiente de la recta ($m$): $-\frac{E_D}{R} < 0$.

### Ecuación de Dos Temperaturas:
Cuando se conocen los coeficientes de difusión $D_1$ y $D_2$ a dos temperaturas distintas $T_1$ y $T_2$, la energía de activación $E_D$ se obtiene directamente restando ambas ecuaciones sin necesidad de conocer a priori el factor $D_0$ [Problems 2, 3]:

$$\ln\left(\frac{D_2}{D_1}\right) = -\frac{E_D}{R} \left(\frac{1}{T_2} - \frac{1}{T_1}\right) = \frac{E_D}{R} \left(\frac{1}{T_1} - \frac{1}{T_2}\right)$$

Despejando $E_D$:
$$E_D = \frac{R \ln(D_2 / D_1)}{\frac{1}{T_1} - \frac{1}{T_2}}$$

---

## 🧩 3. Factores Físicos y Cristalinos que Modulan la Difusividad

La velocidad y magnitud de $D$ en sólidos dependen de cinco factores fundamentales identificados en la literatura experimental [Slides 23-27]:

### A) Mecanismo de Difusión y Tamaño del Soluto (Intersticial vs Vacantes) [Slide 24]
* Los átomos pequeños ($\text{C}, \text{H}, \text{N}, \text{O}$) difunden mediante saltos intersticiales con energías de activación notablemente inferiores a los átomos de la red.
* **Ejemplo cuantitativo en austenita ($\gamma\text{-Fe}$ FCC a $1000^\circ\text{C}$):**
  $$D(\text{C en } \gamma\text{-Fe}) = 3 \times 10^{-11}\text{ m}^2/\text{s} \quad \text{vs} \quad D(\text{Fe en } \gamma\text{-Fe}) = 2 \times 10^{-16}\text{ m}^2/\text{s}$$
  *La difusión intersticial del carbono es cinco órdenes de magnitud más rápida ($10^5$) que la auto-difusión del hierro.*

### B) Tipo de Estructura Cristalina de la Matriz (Disolvente) [Slide 24]
* Las redes cristalinas **más abiertas** poseen factores de empaquetamiento atómico (APF) menores y mayores distancias interatómicas libres, ofreciendo menor resistencia al salto atómico.
* La red cúbica centrada en el cuerpo ($\text{BCC}$, $\text{APF} = 0.68$) es más abierta que la red cúbica compacta centrada en las caras ($\text{FCC}$, $\text{APF} = 0.74$).
* **Comparativa de difusión de Carbono a $500^\circ\text{C}$ [Slides 23-24]:**
  $$D(\text{C en Fe-}\alpha, \text{BCC}) = 10^{-12}\text{ m}^2/\text{s} \gg D(\text{C en Fe-}\gamma, \text{FCC}) = 5 \times 10^{-15}\text{ m}^2/\text{s}$$
  *El carbono difunde unas 200 veces más rápido en ferrita BCC que en austenita FCC a la misma temperatura.*

### C) Defectos Cristalinos y Difusión en Cortocircuito (*Short-Circuit Diffusion*) [Slide 25]
Las regiones donde el ordenamiento atómico está interrumpido contienen mayor volumen libre y menor densidad de enlaces, facilitando el transporte masivo:

$$D_{\text{superficie}} > D_{\text{límite de grano}} > D_{\text{volumen (red)}}$$

* **Difusión en superficie (*Surface diffusion*):** Los átomos superficiales tienen menor número de coordinación y enlaces insaturados; la barrera de activación es mínima.
* **Difusión en bordes de grano (*Grain boundary diffusion*):** Región de desajuste reticular de $2\text{--}5$ diámetros atómicos. Actúa como canal de alta difusividad.
  * *Ejemplo en Plata a $500^\circ\text{C}$ [Slide 23]:* $D(\text{Ag en borde de grano}) = 10^{-11}\text{ m}^2/\text{s}$, mientras que $D(\text{Ag en red monocristalina}) = 10^{-17}\text{ m}^2/\text{s}$ ($\mathbf{10^6\text{ veces mayor}}$).
* **Difusión volumétrica (*Lattice/volume diffusion*):** Es la más lenta porque exige desplazar la red cristalina perfecta tridimensional.

### D) Concentración de Soluto [Slide 25]
A medida que aumenta la concentración de átomos de soluto disueltos, se generan distorsiones en la red circundante y pueden producirse interacciones soluto-soluto o cambios locales en la entalpía libre de Gibbs, alterando la difusividad efectiva $D$.

### E) Temperatura y Temperatura de Fusión ($T_m$) [Slides 8-9, 26-27]
* A mayor temperatura absoluta $T$, mayor energía térmica y difusividad exponencial.
* Los materiales con mayor punto de fusión ($T_m$) poseen enlaces atómicos más rígidos y fuertes ($E_{\text{bond}}$ alta), lo que incrementa su energía de activación $E_D$ y disminuye su difusividad a temperaturas homólogas comparables [Slide 9].

---

## 📊 4. Tabla Oficial de Difusividades de Referencia UC3M

Valores experimentales recopilados en [Session 5 Slide 23]:

| Soluto | Disolvente (Matriz) | Estructura de Matriz | $D$ a $500^\circ\text{C}$ ($\text{m}^2/\text{s}$) | $D$ a $1000^\circ\text{C}$ ($\text{m}^2/\text{s}$) |
| :--- | :--- | :---: | :---: | :---: |
| **Carbono** | Hierro ($\gamma$) | FCC | $5 \times 10^{-15} \ ^*$ | $3 \times 10^{-11}$ |
| **Carbono** | Hierro ($\alpha$) | BCC | $10^{-12}$ | $2 \times 10^{-9} \ ^*$ |
| **Hierro** | Hierro ($\gamma$) | FCC | $2 \times 10^{-23} \ ^*$ | $2 \times 10^{-16}$ |
| **Hierro** | Hierro ($\alpha$) | BCC | $10^{-20}$ | $3 \times 10^{-14} \ ^*$ |
| **Níquel** | Hierro ($\gamma$) | FCC | $10^{-23}$ | $2 \times 10^{-16} \ ^*$ |
| **Manganeso**| Hierro ($\gamma$) | FCC | $3 \times 10^{-24} \ ^*$ | $10^{-16}$ |
| **Cinc** | Cobre | FCC | $4 \times 10^{-18}$ | $5 \times 10^{-13}$ |
| **Cobre** | Aluminio | FCC | $4 \times 10^{-14}$ | — |
| **Cobre** | Cobre | FCC | $10^{-18}$ | $2 \times 10^{-13}$ |
| **Plata** | Plata (volumen) | FCC | $10^{-17}$ | — |
| **Plata** | Plata (límite grano)| — | $10^{-11}$ | — |
| **Carbono** | Titanio | HCP | $3 \times 10^{-16}$ | $2 \times 10^{-11} \ ^*$ |

*\*Fases metaestables extrapoladas a dicha temperatura.*

---

## ⚖️ 5. Resumen Comparativo de Factores Cinéticos [Slide 27]

| La Difusión es **MÁS RÁPIDA** en: | La Difusión es **MÁS LENTA** en: |
| :--- | :--- |
| • Estructuras cristalinas abiertas (BCC) | • Estructuras compactas (FCC, HCP ideal) |
| • Materiales de menor densidad | • Materiales de alta densidad |
| • Materiales con gran número de defectos (grano fino, dislocaciones) | • Materiales monocristalinos perfectos (sin defectos) |
| • Especies difusoras neutras | • Especies difusoras cargadas iónicamente |
| • Materiales con bajo punto de fusión ($T_m$) | • Materiales refractarios de alto $T_m$ |
| • Temperaturas elevadas | • Bajas temperaturas |
| • Especies atómicas pequeñas ($\text{C}, \text{H}, \text{N}$) | • Especies atómicas voluminosas y pesadas |

---

## 🔗 Enlaces Relacionados
* `[[Tema 3 - Diffusion in Solids and Mass Transport]]` (MOC Maestro del Tema 3)
* `[[Concepto - Mecanismos de Difusion Vacantes e Intersticios]]`
* `[[Concepto - Segunda Ley de Fick Difusion en Estado No Estacionario y Funcion Error]]`
* `[[Problema - T3-02 Difusion de Aluminio en Silicio Monocristalino]]`
* `[[Problema - T3-03 Energia de Activacion y Difusividad de Carbono en Acero]]`
* `[[Problema - T3-05 Temperatura de Cementacion de Acero 1010 en 8 Horas]]`
