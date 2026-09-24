---
materia: "Aerospace Materials I"
tema: "Tema 3: Diffusion in Solids and Mass Transport"
fuentes: "Session 5 T3  Difussion_2025.pdf, Slides 2-13"
tags:
  - teoria
  - concepto-fundamental
  - difusion
  - vacantes
  - intersticios
  - energia-activacion
  - hume-rothery
dificultad: media
prerrequisitos:
  - "[[Concepto - Defectos Puntuales Vacantes Termicas Schottky y Frenkel]]"
  - "[[Concepto - Huecos Intersticiales Tetraedricos y Octaedricos]]"
---

# ⚛️ Concepto: Mecanismos de Difusión Atómica — Vacantes e Intersticios

> **Definición Fundamental:** La **difusión** en estado sólido es el fenómeno de transporte de materia mediante el movimiento térmicamente activado de átomos, iones o moléculas a través de la red cristalina [Slide 2].  
> **Fuerza Impulsora (*Driving Force*):** El gradiente de potencial químico o **gradiente de composición** ($\nabla C$). La difusión neta ocurre espontáneamente en la dirección que homogeniza la concentración, maximizando la entropía del sistema [Slide 2].

---

## 🔬 1. Condiciones Necesarias para la Difusión en Sólidos

Para que un átomo ejecute un salto difusional desde su posición de equilibrio a una posición contigua, deben satisfacerse simultáneamente dos condiciones físicas [Slides 4-5]:

1. **Sitio Adyacente Vacante (*Empty Site*):** Debe existir un hueco reticular desocupado (una vacante o un hueco intersticial libre) inmediatamente adyacente a la especie que va a migrar.
2. **Energía Térmica Suficiente ($E_{\text{thermal}} \ge E_a$):** El átomo debe poseer la **energía de activación** ($E_a$) necesaria para distorsionar temporalmente los enlaces de los átomos vecinos y superar la barrera de potencial de silla (*saddle point*) entre posiciones de equilibrio [Slides 4, 6].

$$\uparrow T \implies \uparrow \text{Amplitud de vibración térmica} \implies \uparrow \text{Probabilidad de salto} \implies \uparrow \text{Difusión}$$

La difusividad macroscopicamente observada obedece una dependencia de tipo Arrhenius [Slide 5]:
$$D = D_0 \exp\left(-\frac{E_a}{RT}\right)$$

---

## 🔘 2. Difusión por Vacantes (o Sustitucional)

En aleaciones sustitucionales y en metales puros, los átomos de la red cristalina tienen tamaños atómicos comparables. El único mecanismo geométricamente posible consiste en el intercambio de posición entre un átomo y una **vacante** vecina [Slides 6-7].

### 2.1 Auto-difusión (*Self-Diffusion*) vs Interdifusión (*Interdiffusion*)
* **Auto-difusión (*Self-diffusion*):** Ocurre en metales puros cuando átomos idénticos intercambian sitios con vacantes [Slide 7]. No genera un cambio neto en la composición química macroscópica, pero se evidencia experimentalmente mediante trazadores radiactivos isotópicos (e.g. $^{60}\text{Co}$ o $^{64}\text{Cu}$).
* **Interdifusión (*Interdiffusion* o difusión química):** Ocurre en soluciones sólidas sustitucionales o pares de difusión (e.g. el par de difusión Cobre-Níquel, $\text{Cu}-\text{Ni}$) [Slides 10-12].
  * Ambos metales cumplen estrictamente las **reglas de Hume-Rothery** [Slide 12]:
    1. Misma estructura cristalina: ambos son FCC ($\text{Cu}$ y $\text{Ni}$).
    2. Diferencia de radio atómico mínima: $R_{\text{Cu}} = 128\text{ pm}$, $R_{\text{Ni}} = 124\text{ pm}$ ($\Delta R \approx 3.1\% \ll 15\%$).
    3. Electronegatividad casi idéntica: $\chi_{\text{Cu}} \approx 1.90$, $\chi_{\text{Ni}} \approx 1.91$.
    4. Misma valencia habitual ($+2$).
  * El flujo neto de átomos produce la formación gradual de una solución sólida continua y compuestos intermetálicos, siendo el fundamento clave de la **soldadura por difusión** (*diffusion bonding*) [Slides 10, 33].

### 2.2 Termodinámica de la Energía de Activación de Auto-difusión
Para que ocurra un salto por vacante, primero debe crearse la vacante en la red y luego el átomo vecino debe migrar hacia ella. Por tanto, la energía de activación total de auto-difusión es la suma de dos términos [Slide 8]:

$$E_{\text{self}} = E_v + E_m = \Delta H_v + \Delta H_m$$

* $\Delta H_v$: Energía necesaria para **formar** un mol de vacantes térmicas en el cristal.
* $\Delta H_m$: Energía necesaria para **mover** el átomo a través de la constricción reticular hacia la vacante.

### 2.3 Correlación Directa entre $E_a$ y la Temperatura de Fusión ($T_m$)
Dado que tanto la formación como el movimiento de vacantes implican la rotura de enlaces interatómicos, existe una correlación casi lineal entre la energía de enlace cohesiva, la temperatura de fusión $T_m$ y la energía de activación de difusión [Slides 8-9]:

$$\uparrow T_{\text{melting}} \implies \uparrow E_{\text{bond}} \implies \uparrow E_a$$

| Metal | $T_m$ ($^\circ\text{C}$) | Estructura Cristalina | $E_a$ ($\text{kJ/mol}$) | $E_a$ ($\text{kcal/mol}$) |
| :--- | :---: | :---: | :---: | :---: |
| **Cinc ($\text{Zn}$)** | 419 | HCP | 91.6 | 21.9 |
| **Aluminio ($\text{Al}$)** | 660 | FCC | 165.0 | 39.5 |
| **Cobre ($\text{Cu}$)** | 1083 | FCC | 196.0 | 46.9 |
| **Níquel ($\text{Ni}$)** | 1452 | FCC | 293.0 | 70.1 |
| **Hierro alfa ($\alpha\text{-Fe}$)** | 1530 | BCC | 240.0 | 57.5 |
| **Molibdeno ($\text{Mo}$)** | 2600 | BCC | 460.0 | 110.0 |

*Datos tomados directamente de Session 5 Slide 9.*

---

## ⚡ 3. Difusión Intersticial (*Interstitial Diffusion*)

La difusión intersticial describe la migración de solutos atómicos de pequeño tamaño relativo respecto a la matriz metálica huésped (típicamente $\text{C}$, $\text{H}$, $\text{N}$, $\text{O}$, $\text{B}$) saltando directamente de una posición intersticial a otra contigua [Slide 13].

### Características Distintivas:
1. **Conservación de la Red Huésped:** Los átomos intersticiales se desplazan **sin desplazar permanentemente** ningún átomo de la matriz [Slide 13].
2. **Abundancia de Sitios Libres:** En cualquier red cristalina metálica, la inmensa mayoría de los huecos intersticiales (octaédricos y tetraédricos) están vacíos. La probabilidad geométrica de encontrar un sitio adyacente libre es prácticamente 1, a diferencia del mecanismo sustitucional donde la concentración de vacantes es minúscula ($n_v/N \sim 10^{-4}$ a alta temperatura).
3. **Menor Barrera Energética ($E_i \ll E_v$):** No se requiere energía para formar una vacante ($\Delta H_v = 0$). Solo se necesita la energía de deformación elástica local para que el soluto pequeño se deslice entre los átomos de la matriz [Slide 13].
4. **Cinética Extraordinariamente Más Rápida:** La difusividad intersticial es entre **4 y 8 órdenes de magnitud superior** a la difusividad por vacantes a igual temperatura [Slides 13, 24].

### Comparación Crítica en Aceros a $1000^\circ\text{C}$ ($\gamma\text{-Fe}$ FCC) [Slide 24]:
* Carbono intersticial en austenita:
  $$D_{\text{C en } \gamma\text{-Fe}} (1000^\circ\text{C}) = 3 \times 10^{-11}\text{ m}^2/\text{s}$$
* Auto-difusión de hierro por vacantes en austenita:
  $$D_{\text{Fe en } \gamma\text{-Fe}} (1000^\circ\text{C}) = 2 \times 10^{-16}\text{ m}^2/\text{s}$$
* **Factor de Aceleración:**
  $$\frac{D_{\text{intersticial}}}{D_{\text{vacante}}} = \frac{3 \times 10^{-11}}{2 \times 10^{-16}} = 1.5 \times 10^5 \quad (\mathbf{150\,000\text{ veces más rápido}})$$

---

## 🔗 Enlaces Relacionados
* `[[Tema 3 - Diffusion in Solids and Mass Transport]]` (MOC Maestro del Tema 3)
* `[[Concepto - Primera Ley de Fick Difusion en Estado Estacionario]]`
* `[[Concepto - Segunda Ley de Fick Difusion en Estado No Estacionario y Funcion Error]]`
* `[[Concepto - Ecuacion de Arrhenius y Factores que Influyen en la Difusividad]]`
* `[[Concepto - Cementacion y Aplicaciones Industriales de la Difusion]]`
