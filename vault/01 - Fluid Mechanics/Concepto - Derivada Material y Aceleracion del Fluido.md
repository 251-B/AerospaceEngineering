---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - teoria
  - concepto-clave
  - derivada-material
  - aceleracion
dificultad: media
prerrequisitos: []
---

# ⚡ Concepto: Derivada Material y Campo de Aceleración

> **Idea clave en una frase:** La derivada material describe la tasa de cambio temporal de cualquier propiedad intensiva (escalar o vectorial) experimentada por una partícula fluida en su movimiento, descomponiéndose en una contribución local temporal (inestacionariedad) y una contribución convectiva espacial (desplazamiento a través de gradientes espaciales).

---

## 🎯 1. Fundamento Físico y Deducción Paso a Paso

Consideremos una partícula fluida que en el instante $t$ se encuentra en la posición $\vec{x}$, donde una propiedad intensiva escalar vale $\phi(\vec{x}, t)$ (por ejemplo, temperatura $T$, presión $p$ o densidad $\rho$).

Un intervalo infinitesimal $dt$ después, la partícula se ha desplazado un vector $d\vec{x} = \vec{v} dt$ y ocupa la posición $\vec{x} + d\vec{x}$ en el instante $t + dt$. El nuevo valor de la propiedad es $\phi(\vec{x} + d\vec{x}, t + dt)$.

Efectuando un desarrollo en serie de Taylor de primer orden alrededor de $(\vec{x}, t)$:

$$ d\phi = \phi(\vec{x} + d\vec{x}, t + dt) - \phi(\vec{x}, t) = \frac{\partial \phi}{\partial t} dt + d\vec{x} \cdot \nabla\phi + \mathcal{O}(dt^2) \qquad \text{[Ec. 2.22]} $$

Dividiendo entre el incremento temporal $dt$ e identificando la velocidad de la partícula como $\vec{v} = \frac{d\vec{x}}{dt}$:

$$ \frac{D\phi}{Dt} = \frac{\partial \phi}{\partial t} + \vec{v} \cdot \nabla\phi \qquad \text{[Ec. 2.23]} $$

### Operador Derivada Material (Notes.pdf, Ec. 2.24)
$$ \mathbf{\frac{D()}{Dt} = \underbrace{\frac{\partial()}{\partial t}}_{\text{Variación local}} + \underbrace{\vec{v} \cdot \nabla()}_{\text{Variación convectiva}}} $$

* **Término local ($\partial/\partial t$):** Mide la rapidez con la que cambia la propiedad en un punto fijo del espacio debido a la inestacionariedad intrínseca del flujo. Se anula en flujos estacionarios.
* **Término convectivo ($\vec{v} \cdot \nabla$):** Mide la variación que experimenta la partícula al viajar de una región a otra donde el campo espacial presenta un gradiente no nulo. Puede ser muy elevado incluso en flujos puramente estacionarios (por ejemplo, el calentamiento de aire que cruza una tobera convergente).

---

## 🏎️ 2. Aceleración de una Partícula Fluida (Notes.pdf, Ecs. 2.25–2.27)

Aplicando el operador material al vector velocidad $\vec{v}(\vec{x}, t)$, la aceleración física de la partícula fluida es:

$$ \vec{a} = \frac{D\vec{v}}{Dt} = \frac{\partial \vec{v}}{\partial t} + \vec{v} \cdot (\nabla\vec{v}) \qquad \text{[Ec. 2.25]} $$

donde $\nabla\vec{v}$ es el tensor gradiente de velocidad de segundo orden.

### A. Expresión Intrínseca Universal (Independiente del Sistema de Coordenadas)
Empleando la identidad del cálculo vectorial para el producto escalar $\vec{v} \cdot (\nabla\vec{v}) = \nabla\left(\frac{|\vec{v}|^2}{2}\right) - \vec{v} \wedge (\nabla \wedge \vec{v})$, la aceleración se escribe de forma invariante como:

$$ \mathbf{\vec{a} = \frac{\partial \vec{v}}{\partial t} + \nabla\left(\frac{|\vec{v}|^2}{2}\right) - \vec{v} \wedge (\nabla \wedge \vec{v})} \qquad \text{[Ec. 2.26]} $$

* $\frac{\partial\vec{v}}{\partial t}$: Aceleración local.
* $\nabla(|\vec{v}|^2/2)$: Gradiente de la energía cinética específica.
* $-\vec{v} \wedge (\nabla \wedge \vec{v}) = -\vec{v} \wedge \vec{\omega}$: Término de aceleración de Lamb (producto vectorial con la vorticidad $\vec{\omega}$). En flujos irrotacionales ($\vec{\omega} = 0$), este término desaparece idénticamente.

### B. Componentes en Coordenadas Cartesianas
En coordenadas cartesianas rectangulares $(x, y, z)$, $(\nabla\vec{v})_{ij} = \frac{\partial v_j}{\partial x_i}$, y la aceleración se reduce a la derivada material de cada componente de velocidad:

$$ a_i = \frac{D v_i}{Dt} = \frac{\partial v_i}{\partial t} + \sum_j v_j \frac{\partial v_i}{\partial x_j} = \frac{\partial v_i}{\partial t} + v_x \frac{\partial v_i}{\partial x} + v_y \frac{\partial v_i}{\partial y} + v_z \frac{\partial v_i}{\partial z} \qquad \text{[Ec. 2.27]} $$

> [!WARNING] Advertencia Crucial para Coordenadas Curvilíneas
> La ecuación escalar $a_i = \frac{\partial v_i}{\partial t} + \vec{v} \cdot \nabla v_i$ **SOLO es válida en coordenadas cartesianas**.  
> En coordenadas cilíndricas o esféricas, la curvatura de las líneas coordenadas genera aceleraciones centrípetas y de Coriolis asociadas a la derivada espacial de los vectores de la base local:
> * En cilíndricas $(r, \theta, z)$:
>   $$ a_r = \frac{\partial v_r}{\partial t} + v_r \frac{\partial v_r}{\partial r} + \frac{v_\theta}{r}\frac{\partial v_r}{\partial \theta} + v_z \frac{\partial v_r}{\partial z} - \mathbf{\frac{v_\theta^2}{r}} $$
>   $$ a_\theta = \frac{\partial v_\theta}{\partial t} + v_r \frac{\partial v_\theta}{\partial r} + \frac{v_\theta}{r}\frac{\partial v_\theta}{\partial \theta} + v_z \frac{\partial v_\theta}{\partial z} + \mathbf{\frac{v_r v_\theta}{r}} $$
>   $$ a_z = \frac{\partial v_z}{\partial t} + v_r \frac{\partial v_z}{\partial r} + \frac{v_\theta}{r}\frac{\partial v_z}{\partial \theta} + v_z \frac{\partial v_z}{\partial z} $$
> El término $-v_\theta^2/r$ es la aceleración centrípeta y $+v_r v_\theta/r$ es la contribución convectiva azimuthal.

---

## 🔄 3. Aceleración en Sistemas de Referencia No Inerciales (Notes.pdf, Ec. 2.28)

Cuando el flujo se analiza desde un sistema de referencia móvil con aceleración lineal de su origen $\vec{a}_0(t)$ y velocidad angular de rotación $\vec{\Omega}(t)$ (por ejemplo, alabes de turborreactores o flujos atmosféricos y oceánicos en la Tierra en rotación):

$$ \mathbf{\vec{a} = \vec{a}_{\text{rel}} + \vec{a}_s} $$

donde la aceleración inercial aparente del sistema $\vec{a}_s$ viene dada por:

$$ \vec{a}_s = \vec{a}_0 + \frac{d\vec{\Omega}}{dt} \wedge \vec{x} + \vec{\Omega} \wedge (\vec{\Omega} \wedge \vec{x}) + 2\vec{\Omega} \wedge \vec{v}_{\text{rel}} \qquad \text{[Ec. 2.28]} $$

1. $\vec{a}_0$: Aceleración de traslación del origen.
2. $\frac{d\vec{\Omega}}{dt} \wedge \vec{x}$: Aceleración angular del triedro.
3. $\vec{\Omega} \wedge (\vec{\Omega} \wedge \vec{x})$: Aceleración centrífuga aparente (dirigida perpendicularmente al eje de giro hacia el exterior).
4. $2\vec{\Omega} \wedge \vec{v}_{\text{rel}}$: Aceleración de Coriolis (perpendicular a la velocidad relativa y al eje de rotación).

---

## 🔗 Conceptos Relacionados
* `[[01 - Fluid Mechanics/Tema 2 - Flow Kinematics|Tema 2: Flow Kinematics]]`
* `[[01 - Fluid Mechanics/Concepto - Vorticidad, Circulacion y Potencial de Velocidades|Concepto: Vorticidad y Circulación]]`
