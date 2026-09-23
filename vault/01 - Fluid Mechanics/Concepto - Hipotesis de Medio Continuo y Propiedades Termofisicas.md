---
materia: Fluid Mechanics
tema: "Tema 1: Propiedades de los Fluidos y Fundamentos"
fuentes:
  - "Notes.pdf (Sánchez & Rodríguez-Rodríguez, UC3M), Capítulo 1, Págs. 1-8"
  - "slides_Chapters1-2.pdf, Diapositivas 1.0 a 1.8"
tags:
  - teoria
  - medio-continuo
  - termofisica
  - particula-fluida
  - lte
  - knudsen
dificultad: media
prerrequisitos: []
---

# 📖 Hipótesis de Medio Continuo, Partícula Fluida y Termofísica

> **Idea clave (Sánchez & Rodríguez-Rodríguez):** La materia en un fluido está discretamente distribuida a nivel molecular. La hipótesis de medio continuo permite definir un rango intermedio de escalas donde las propiedades del fluido pueden describirse como funciones continuas del espacio $\vec{x}$ y del tiempo $t$ a través del concepto de **partícula fluida**.

---

## 🎯 1. Diferencias Microscópicas y Macroscópicas: Sólidos, Líquidos y Gases

*[Fuente: Notes.pdf §1, pág. 1; Slides 1.0 - 1.2]*

### Comportamiento frente a Esfuerzos Exteriores
* **Sólidos:** Bajo una fuerza externa pequeña responden con una deformación finita. La fuerza interna que contrarresta la acción externa es proporcional a la **deformación**:
  $$ \tau \propto d\theta $$
* **Fluidos (Líquidos y Gases):** Se deforman continuamente bajo la acción de esfuerzos tangenciales por pequeños que sean. La fuerza interna resistiva es proporcional a la **tasa de deformación**:
  $$ \tau \propto \frac{d\theta}{dt} $$
  Como consecuencia directa, los fluidos no tienen forma propia y se adaptan a la del recipiente.

### Líquidos vs. Gases
* **Densidad:** $\rho_{\text{líquido}} \gg \rho_{\text{gas}}$. Acelerar un líquido requiere fuerzas mucho mayores que acelerar un gas.
* **Compresibilidad:** La variación de densidad ante sobrepresiones isotermas es órdenes de magnitud menor en líquidos que en gases:
  $$ \left(\frac{\partial \rho}{\partial p}\right)_{T,\text{líquido}} \ll \left(\frac{\partial \rho}{\partial p}\right)_{T,\text{gas}} \quad \text{(Notes.pdf, Ec. 1.1)} $$

### Origen Microscópico y Distancia Intermolecular ($d$)
La fuerza intermolecular $F(d)$ presenta repulsión para distancias muy cortas y atracción para $d > d_0$, con un equilibrio estable en la escala molecular característica:
$$ d_0 \sim 3 \times 10^{-10}\text{ m} = 3\text{ \AA} $$

Con la densidad $\rho$, la masa molar $W$ y el número de Avogadro $N_A = 6.022 \times 10^{23}\text{ moléculas/mol}$, la distancia media intermolecular $d$ se obtiene igualando la masa de una molécula al volumen que ocupa $d^3$:
$$ \rho = \frac{W / N_A}{d^3} \implies \mathbf{d = \left(\frac{W}{\rho N_A}\right)^{1/3}} $$

| Magnitud | Aire (Gas a nivel del mar) | Agua (Líquido) |
| :--- | :--- | :--- |
| **Densidad ($\rho$)** | $1.2\text{ kg/m}^3$ | $1000\text{ kg/m}^3$ |
| **Masa molar ($W$)** | $28.96\text{ g/mol}$ | $18.02\text{ g/mol}$ |
| **Distancia intermolecular ($d$)** | $\mathbf{\approx 3.4 \times 10^{-9}\text{ m}} \approx 10\,d_0$ | $\mathbf{\approx 3.1 \times 10^{-10}\text{ m}} \approx d_0$ |
| **Moléculas en $1\text{ mm}^3$** | $\sim 10^{16}\text{ moléculas}$ | $\sim 10^{19}\text{ moléculas}$ |
| **Interacción molecular** | Vuelan libres; colisiones binarias | Empaquetadas; fuerzas cohesivas permanentes |

---

## 🔬 2. La Hipótesis de Medio Continuo y la Partícula Fluida

*[Fuente: Notes.pdf §1, págs. 3-5; Slides 1.3 - 1.4]*

En lugar de resolver las leyes de Newton para $\sim 10^{16}$ moléculas/mm³ (computacionalmente inalcanzable), introducimos el concepto de **Partícula Fluida**.

### Escala Macroscópica ($L$)
Es la distancia característica sobre la que ocurren variaciones significativas en las propiedades macroscópicas del flujo (ejemplo: en una habitación, $L \sim 10\text{ cm}$; en un perfil alar, $L \sim \text{cuerda}$).

### Definición de la Partícula Fluida ($\delta V$)
Es un volumen diferencial centrado en la posición $\vec{x}$ en el instante $t$ que debe satisfacer estrictamente la **condición de doble acotación**:
$$ \mathbf{d \ll (\delta V)^{1/3} \ll L} \quad \text{(Notes.pdf, Ec. 1.2)} $$

1. $(\delta V)^{1/3} \gg d$: Debe contener un número inmenso de moléculas para promediar las fluctuaciones estadísticas moleculares y alcanzar la **meseta de densidad** (*plateau*).
2. $(\delta V)^{1/3} \ll L$: Debe ser infinitesimal frente a las variaciones espaciales del flujo para tratarse como un punto material diferencial en $\vec{x}$.

```text
  Densidad aparente
  ∑ mi / δV
       ^
       |   Fluctuaciones discretas
       |   moleculares (saltos)        MESETA CONTINUA (Plateau)
       |      _/\_/\_              =============================       Variaciones macroscópicas
       |     /       \                                          \      espaciales del flujo
       |____/_________\__________________________________________\___________________________>
           0          d                (δV)^1/3                   L               Tamaño (δV)^1/3
```

### Límite de Aplicabilidad
El medio continuo es rigurosamente válido si:
$$ \frac{d}{L} \ll 1 $$
Falla en:
* Flujos enrarecidos en la alta atmósfera (reentrada espacial de satélites o transbordadores a $h > 100\text{ km}$, donde $d \sim L$).
* Micro y nanofluidodinámica (MEMS) donde los conductos son comparables a la escala molecular.

---

## 📐 3. Definición de Variables de Campo Macroscópicas

*[Fuente: Notes.pdf §1, págs. 5-6; Slides 1.5]*

A partir de la partícula fluida $\delta V$, definimos los campos continuos:

### 1. Campo de Densidad ($\rho$)
$$ \rho(\vec{x}, t) = \lim_{\delta V \to 0, \, (\delta V)^{1/3} \gg d} \frac{\sum m_i}{\delta V} \quad \left[\frac{\text{kg}}{\text{m}^3}\right] \quad \text{(Ec. 1.3)} $$

### 2. Campo de Velocidad del Flujo ($\vec{v}$)
Es la velocidad del centro de masas de las moléculas contenidas en la partícula fluida:
$$ \vec{v}(\vec{x}, t) = \lim_{\delta V \to 0} \frac{\sum m_i \vec{v}_i}{\sum m_i} \quad \left[\frac{\text{m}}{\text{s}}\right] \quad \text{(Ec. 1.4)} $$

### 3. Energía Interna ($e$) y Energía Total
La energía por unidad de masa total dentro de $\delta V$ se descompone exactamente en la energía cinética macroscópica del flujo y la energía interna térmica:
$$ \lim_{\delta V \to 0} \frac{\sum E_i}{\sum m_i} = e + \frac{|\vec{v}|^2}{2} \quad \text{(Ec. 1.5)} $$
donde $e$ representa la **energía interna** (movimiento térmico desordenado respecto al centro de masas más energías intramoleculares):
$$ \mathbf{e = \lim_{\delta V \to 0} \frac{\sum m_i \frac{|\vec{v}_i - \vec{v}|^2}{2} + E_{v,i} + E_{r,i} + \cdots}{\sum m_i}} \quad \text{(Ec. 1.6)} $$
* El término $\frac{|\vec{v}_i - \vec{v}|^2}{2}$ es la agitación térmica aleatoria molecular, base fundamental de la definición termodinámica de la **temperatura ($T$)**.
* $E_{v,i}, E_{r,i}$ son las energías de vibración y rotación molecular.

---

## ⚡ 4. Hipótesis de Equilibrio Termodinámico Local (ETL / LTE)

*[Fuente: Notes.pdf §1, págs. 5-6; Slides 1.6]*

En Mecánica de Fluidos, los sistemas cambian espacial y temporalmente. Sin embargo, un observador que se desplace con la velocidad local $\vec{v}(\vec{x}, t)$ del fluido observa que las variables termodinámicas se relacionan mediante las mismas **ecuaciones de estado** que en la termodinámica clásica de equilibrio.

### Mecanismo Físico de Restauración: Las Colisiones Moleculares
En un gas, las moléculas intercambian cantidad de movimiento y energía mediante choques continuos.
* **Recorrido libre medio ($\lambda$):** Distancia promedio entre dos colisiones sucesivas. Igualando el volumen barrido por la molécula ($d_0^2 \lambda$) al volumen por molécula ($d^3$):
  $$ \frac{\lambda}{d} \simeq \left(\frac{d}{d_0}\right)^2 \implies \mathbf{\lambda \approx 4 \times 10^{-7}\text{ m}} = 0.4\ \mu\text{m} \quad \text{(en aire a nivel del mar)} $$
* **Tiempo característico entre colisiones ($\tau$):** Siendo $a \approx \sqrt{\gamma R T}$ la velocidad del sonido:
  $$ \tau = \frac{\lambda}{a} \approx \frac{4 \times 10^{-7}\text{ m}}{340\text{ m/s}} \approx \mathbf{10^{-9}\text{ s}} = 1\text{ ns} $$

### Criterio del Número de Knudsen ($Kn$)
Para que una molécula experimente miles de colisiones antes de alcanzar regiones con propiedades macroscópicas distintas, se debe cumplir:
$$ \mathbf{Kn = \frac{\lambda}{L} \ll 1} \quad \text{(Notes.pdf, Ec. 1.7)} $$
Para flujos no estacionarios con tiempo característico macroscópico $T_{\text{macro}}$:
$$ T_{\text{macro}} \gg \tau \approx 10^{-9}\text{ s} $$

> [!IMPORTANT] Rigor Académico
> El criterio de ETL ($Kn = \lambda/L \ll 1$) es **más restrictivo** que el de medio continuo ($d/L \ll 1$), puesto que para gases el recorrido libre medio es órdenes de magnitud mayor que la distancia intermolecular: $\lambda \approx 400\text{ nm} \gg d \approx 3.4\text{ nm}$.

---

## 📊 5. Ecuaciones de Estado: Modelos de Líquido y Gas Perfecto

*[Fuente: Notes.pdf §1, págs. 6-7; Slides 1.7 - 1.8]*

Bajo ETL, la relación termodinámica fundamental de Gibbs gobierna la partícula fluida:
$$ de = T ds - p \, d\left(\frac{1}{\rho}\right) = T ds + \frac{p}{\rho^2} d\rho \quad \text{(Ec. 1.8)} $$
De ella se desprenden:
$$ T = \left(\frac{\partial e}{\partial s}\right)_\rho \quad \text{(Ec. 1.9)}, \qquad p = -\left(\frac{\partial e}{\partial \rho^{-1}}\right)_s \quad \text{(Ec. 1.10)}, \qquad h = e + \frac{p}{\rho} $$

### 1. Modelo de Líquido Perfecto (Incompresible)
Densidad constante $\rho_0$ y calor específico constante $c$:
$$ \mathbf{\rho = \rho_0} \quad \text{(Ec. 1.11)} $$
$$ \mathbf{e = c T + e_0} \quad \text{(Ec. 1.12)} $$
$$ \mathbf{h = c T + e_0 + \frac{p}{\rho_0}} \quad \text{(Ec. 1.13)} $$
$$ \mathbf{s = c \ln T + s_0} \quad \text{(Ec. 1.14)} $$
*(Para agua: $\rho_0 = 1000\text{ kg/m}^3$, $c = 4180\text{ J/(kg}\cdot\text{K)}$)*.

### 2. Modelo de Gas Perfecto (Calóricamente Perfecto)
$$ \mathbf{\frac{p}{\rho} = R_g T} \quad \text{(Ec. 1.15)}, \quad R_g = \frac{R_0}{W} $$
$$ \mathbf{e = c_v T + e_0} \quad \text{(Ec. 1.16)} $$
$$ \mathbf{h = c_p T + e_0} \quad \text{(Ec. 1.17)} $$
$$ \mathbf{s = c_v \ln\left(\frac{p}{\rho^\gamma}\right) + s_0} \quad \text{(Ec. 1.18)} $$

* Constante universal: $R_0 = 8.314\text{ J/(mol}\cdot\text{K)}$.
* Relación de Mayer: $c_p = c_v + R_g$.
* Coeficiente adiabático: $\gamma = c_p/c_v$. Para gases diatómicos (aire, $N_2, O_2$): $\mathbf{\gamma = 7/5 = 1.4}$.
* Para el aire estándar:
  $$ R_g = 287\text{ J/(kg}\cdot\text{K)}, \quad c_v = 717\text{ J/(kg}\cdot\text{K)}, \quad c_p = 1004\text{ J/(kg}\cdot\text{K)} $$

---

## 🔗 Enlaces Internos
* `[[01 - Fluid Mechanics/Tema 1 - Propiedades y Estatica de Fluidos|⬅️ Volver al Índice del Tema 1]]`
* `[[01 - Fluid Mechanics/Concepto - Viscosidad y Ley de Newton de la Viscosidad|➡️ Siguiente: Viscosidad y Ley de Newton]]`
