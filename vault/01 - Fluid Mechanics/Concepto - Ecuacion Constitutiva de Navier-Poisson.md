---
materia: Fluid Mechanics
tema: "Tema 3: Conservation Laws"
tags:
  - teoria
  - concepto-clave
  - navier-poisson
  - viscosidad
  - stokes
dificultad: alta
prerrequisitos:
  - "[[01 - Fluid Mechanics/Concepto - Tensor de Esfuerzos y Principio de Cauchy|Concepto: Tensor de Esfuerzos de Cauchy]]"
  - "[[01 - Fluid Mechanics/Tema 2 - Flow Kinematics|Tema 2: Flow Kinematics]]"
---

# 🔬 Concepto: Ecuación Constitutiva de Navier-Poisson

> **Idea clave en una frase:** La ecuación constitutiva de Navier-Poisson relaciona linealmente el tensor de esfuerzos viscosos $\bar{\bar{\tau}}'$ con el tensor velocidad de deformación $\bar{\bar{T}}_d$ en un fluido newtoniano isótropo, parametrizándose mediante dos coeficientes termodinámicos: la viscosidad dinámica $\mu(T)$ y la viscosidad volumétrica $\mu_B(T)$ (que se anula según la hipótesis clásica de Stokes).

---

## 🧊 1. Fluido en Reposo o Movimiento Rígido (Notes.pdf, Ecs. 3.26–3.27)

Por la propia definición de fluido continuo (introducida en el Capítulo 1), un fluido es incapaz de sostener esfuerzos tangenciales de cizalladura en equilibrio estático. Por consiguiente:
1. Si el fluido está en **reposo** en un sistema inercial, o
2. Si el fluido se mueve con un **movimiento de sólido rígido** (traslación pura y rotación con deformación nula $\bar{\bar{T}}_d = 0$),

los esfuerzos superficiales actúan en todo punto de forma estrictamente perpendicular a la superficie y son independientes de la orientación de $\vec{n}$:

$$ \vec{f}_n = -p\vec{n} \qquad \text{[Ec. 3.26]} $$

Donde $p(\vec{x}, t) > 0$ es la **presión termodinámica local** (una variable intensiva de estado que satisface la ecuación de estado $p = \rho R T$ o $p = p(\rho, T)$). Igualando con la relación general de Cauchy $\vec{f}_n = \bar{\bar{\tau}}\cdot\vec{n}$, se deduce el tensor de esfuerzos hidrostático:

$$ \mathbf{\bar{\bar{\tau}} = -p \bar{\bar{I}}} \qquad \text{[Ec. 3.27]} $$

Donde $\bar{\bar{I}}$ es el tensor identidad unitario ($\delta_{ij}$).

---

## 🌊 2. Descomposición del Tensor de Esfuerzos (Notes.pdf, Ec. 3.28)

Cuando existe movimiento relativo con deformación entre partículas adyacentes ($\bar{\bar{T}}_d \neq 0$), la fricción molecular y el transporte microscópico de cantidad de movimiento generan esfuerzos adicionales denominados **esfuerzos viscosos**.
El tensor de esfuerzos total se descompone universalmente como:

$$ \mathbf{\bar{\bar{\tau}} = -p \bar{\bar{I}} + \bar{\bar{\tau}}'} \qquad \text{[Ec. 3.28]} $$

* $-p \bar{\bar{I}}$: parte esférica o isotrópica debida a la presión termodinámica.
* $\bar{\bar{\tau}}'$: **tensor de esfuerzos viscosos** (*deviatoric stress tensor*), que debe anularse idénticamente cuando $\bar{\bar{T}}_d = 0$.

---

## 📐 3. Hipótesis del Fluido Newtoniano Isótropo (Notes.pdf, Ecs. 3.29–3.31)

Para cerrar el modelo cinemático-dinámico, Navier (1822) y Poisson (1831) postularon las siguientes hipótesis físicas para fluidos newtonianos (el aire, el agua, los combustibles de aviación y los gases de combustión habituales satisfacen plenamente este comportamiento):

1. **Dependencia exclusiva de la velocidad de deformación:** $\bar{\bar{\tau}}'$ no depende del gradiente de velocidad antisimétrico $\bar{\bar{T}}_r$ (la rotación rígida no engendra disipación viscosa), sino únicamente de $\bar{\bar{T}}_d$.
2. **Linealidad estricta:** La relación entre tensiones viscosas y tasas de deformación es lineal:
   $$ \tau'_{ij} = \alpha_{ijkl} \gamma_{kl} \qquad \text{[Ec. 3.29]} $$
   donde $\gamma_{kl} = (\bar{\bar{T}}_d)_{kl}$ y $\alpha_{ijkl}$ es un tensor de cuarto orden de propiedades del medio.
3. **Isotropía espacial:** El fluido no posee direcciones privilegiadas intrínsecas. El tensor $\alpha_{ijkl}$ debe ser invariante ante cualquier rotación del sistema de coordenadas.

En el sistema de coordenadas definido por las **direcciones principales de deformación** (donde $\bar{\bar{T}}_d$ es diagonal con tasas principales $\gamma_1, \gamma_2, \gamma_3$):
Por isotropía, la tensión viscosa principal $\tau'_1$ debe depender simétricamente de $\gamma_1$ y de las otras dos componentes ortogonales $\gamma_2, \gamma_3$:
$$ \tau'_1 = \alpha \gamma_1 + \lambda (\gamma_2 + \gamma_3) $$
Sumando y restando $\lambda \gamma_1$, y recordando que $\gamma_1 + \gamma_2 + \gamma_3 = \text{tr}(\bar{\bar{T}}_d) = \nabla \cdot \vec{v}$:
$$ \tau'_1 = (\alpha - \lambda)\gamma_1 + \lambda (\nabla \cdot \vec{v}) $$
Definiendo el **primer coeficiente de viscosidad dinámica** como $\mu = \frac{1}{2}(\alpha - \lambda)$, la expresión anterior se generaliza en notación tensorial invariante:

$$ \mathbf{\bar{\bar{\tau}}' = 2\mu \bar{\bar{T}}_d + \lambda (\nabla \cdot \vec{v}) \bar{\bar{I}}} \qquad \text{[Ec. 3.30]} $$

Donde:
* $\mu$: Viscosidad dinámica de cizalladura (*shear viscosity*), unidades $\text{Pa}\cdot\text{s} = \text{kg}/(\text{m}\cdot\text{s})$.
* $\lambda$: Segundo coeficiente de viscosidad (*second viscosity*).

---

## 🧪 4. Viscosidad Volumétrica ($\mu_B$) e Hipótesis de Stokes (Notes.pdf, Ec. 3.31)

Tomando la traza del tensor de esfuerzos viscosos $\bar{\bar{\tau}}'$:
$$ \text{tr}(\bar{\bar{\tau}}') = 2\mu \, \text{tr}(\bar{\bar{T}}_d) + 3\lambda (\nabla \cdot \vec{v}) = (2\mu + 3\lambda)(\nabla \cdot \vec{v}) $$
Se define la **viscosidad volumétrica o de bulto** (*bulk viscosity*) $\mu_B$ como:
$$ \mu_B = \lambda + \frac{2}{3}\mu \implies \lambda = \mu_B - \frac{2}{3}\mu $$

Sustituyendo $\lambda$ en (3.30), se obtiene la **forma canónica de Navier-Poisson**:

$$ \mathbf{\bar{\bar{\tau}}' = 2\mu \bar{\bar{T}}_d + \left(\mu_B - \frac{2}{3}\mu\right)(\nabla \cdot \vec{v}) \bar{\bar{I}}} \qquad \text{[Ec. 3.31]} $$

### La Hipótesis Clásica de Stokes (1845)
Sir George Gabriel Stokes planteó que para fluidos con dilatación o compresión lenta, la viscosidad volumétrica es despreciable:
$$ \mathbf{\mu_B \approx 0 \implies \lambda = -\frac{2}{3}\mu} $$
* **Gases monoatómicos:** La teoría cinética de Boltzmann demuestra analíticamente que $\mu_B \equiv 0$ de forma exacta.
* **Gases diatómicos/poliatómicos (como el aire):** $\mu_B \approx 0.6 \mu$, pero su efecto solo resulta perceptible en fenómenos de absorción acústica de ultra-alta frecuencia o en el espesor interno de ondas de choque hipersónicas extremas. En aerodinámica clásica subsónica, supersónica y atmosférica, la hipótesis de Stokes $\mu_B = 0$ es un estándar universal.
* **Fluidos Incompresibles ($\nabla \cdot \vec{v} = 0$):** El segundo sumando desaparece idénticamente con independencia del valor de $\mu_B$:
  $$ \mathbf{\bar{\bar{\tau}}' = 2\mu \bar{\bar{T}}_d} $$

---

## 🌡️ 5. Dependencia Térmica y Comparación de Propiedades (Aire vs Agua)

La viscosidad dinámica $\mu$ es una propiedad termodinámica de estado que depende primordialmente de la temperatura $T$, siendo casi independiente de la presión $p$ en rangos convencionales:

* **En Gases (Aire):** El transporte de momento se debe al intercambio cinético de moléculas entre capas adyacentes en movimiento térmico aleatorio. Al elevar $T$, aumenta la velocidad cuadrática media ($v_{\text{th}} \propto \sqrt{T}$), incrementando la viscosidad:
  $$ \mu_{\text{gas}}(T) \propto T^{1/2} \quad \text{o mediante la Ley de Sutherland:} \quad \mu(T) = \mu_0 \left(\frac{T}{T_0}\right)^{3/2} \frac{T_0 + S}{T + S} $$
  Para aire: a $T_0 = 288\text{ K}$, $\mu_a \approx 1.78 \times 10^{-5}\text{ Pa}\cdot\text{s}$.

* **En Líquidos (Agua):** El transporte de momento está dominado por las fuerzas de cohesión intermoleculares. Al aumentar $T$, las moléculas adquieren energía para escapar de los pozos de potencial, reduciendo drásticamente las fuerzas de cohesión y, con ello, la viscosidad:
  $$ \mu_{\text{líquido}}(T) \approx A \exp(B / T) $$
  Para agua: a $T = 288\text{ K}$, $\mu_w \approx 1.14 \times 10^{-3}\text{ Pa}\cdot\text{s}$ ($\approx 64$ veces mayor que la del aire). A $T = 368\text{ K}$, se reduce a $\mu_w \approx 0.30 \times 10^{-3}\text{ Pa}\cdot\text{s}$.

### ⚠️ Paradoja Aparente: Viscosidad Cinemática ($\nu = \mu/\rho$)
En aerodinámica, la difusión de vorticidad y el espesor de la capa límite dependen de la viscosidad cinemática $\nu = \mu / \rho$:
* **Aire a nivel del mar ($288\text{ K}$):** $\rho_a \approx 1.225\text{ kg/m}^3 \implies \mathbf{\nu_a \approx 1.45 \times 10^{-5}\text{ m}^2/\text{s}}$.
* **Agua líquida ($288\text{ K}$):** $\rho_w \approx 1000\text{ kg/m}^3 \implies \mathbf{\nu_w \approx 1.14 \times 10^{-6}\text{ m}^2/\text{s}}$.

> [!IMPORTANT] Hecho Contraintuitivo Crucial
> ¡La viscosidad cinemática del aire es **13 a 15 veces superior** a la del agua líquida! Debido a su reducida densidad, el aire difunde el momento molecular mucho más rápidamente por unidad de inercia que el agua.
