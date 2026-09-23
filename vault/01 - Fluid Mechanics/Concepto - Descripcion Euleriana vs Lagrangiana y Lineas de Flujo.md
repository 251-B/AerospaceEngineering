---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - teoria
  - concepto-clave
  - euler-lagrange
  - lineas-corriente
dificultad: media
prerrequisitos: []
---

# 🌀 Concepto: Descripciones Euleriana y Lagrangiana & Líneas de Flujo

> **Idea clave en una frase:** La cinemática de fluidos distingue entre seguir partículas discretas en su viaje temporal (enfoque Lagrangiano) y observar el campo continuo de velocidades en puntos fijos del espacio (enfoque Euleriano), dando lugar a tres familias geométricas de líneas: trayectorias, líneas de corriente y líneas de traza.

---

## 🎯 1. Fundamentos: Descripción Euleriana vs Lagrangiana

### A. Descripción Lagrangiana
Trata al fluido como una colección de partículas individuales identificadas por su posición inicial $\vec{x}_0$ en el instante $t_0$. El movimiento se describe mediante la función de trayectoria:

$$ \vec{x} = \vec{x}_T(\vec{x}_0, t) \qquad \text{[Ec. 2.10]} $$

La velocidad y la aceleración se obtienen por derivación temporal directa manteniendo $\vec{x}_0$ constante:
$$ \vec{v} = \frac{\partial \vec{x}_T}{\partial t}, \qquad \vec{a} = \frac{\partial^2 \vec{x}_T}{\partial t^2} $$
*Utilidad:* Análisis de fases dispersas (gotas de combustible en inyectores, partículas de polvo/ceniza volcánica en turbinas).  
*Inconveniente:* Conduce a formulaciones integro-diferenciales complejas para las leyes de conservación del medio continuo.

### B. Descripción Euleriana (Enfoque Oficial de la Mecánica de Fluidos)
Describe el estado del flujo en puntos fijos del espacio $\vec{x}$ en cada instante $t$, tratando la velocidad como un campo vectorial continuo:

$$ \vec{v} = \vec{v}(\vec{x}, t) $$

---

## 📍 2. Clasificación Fundamental de Flujos

* **Flujo uniforme:** Invariante en el espacio en un instante dado: $\nabla\vec{v} = 0 \implies \vec{v} = \vec{v}(t)$.
* **Flujo estacionario (*steady*):** Invariante en el tiempo en cada punto espacial: $\frac{\partial\vec{v}}{\partial t} = 0 \implies \vec{v} = \vec{v}(\vec{x})$.
* **Relatividad del observador:** La estacionariedad depende del sistema de referencia. Para un avión volando a velocidad constante $\vec{V}_\infty$, el flujo es no estacionario para un observador fijo en tierra ($\vec{v}(\vec{x}, t)$), pero estacionario para el piloto o en un túnel de viento ($\vec{v}(\vec{x})$).
* **Punto de remanso (*stagnation point*):** Punto del espacio donde la velocidad se anula simultáneamente en sus tres componentes:
  $$ \vec{v}(\vec{x}, t) = 0 \qquad \text{[Ec. 2.11]} $$

---

## 📐 3. Familias Geométricas de Líneas y Superficies de Flujo

### 1. Trayectorias y Líneas de Trayectoria (*Path lines*)
Es el lugar geométrico que describe una partícula fluida concreta a lo largo del tiempo. Dado el campo euleriano $\vec{v}(\vec{x}, t)$, la trayectoria se halla resolviendo el problema de Cauchy (valores iniciales):

$$ \frac{d\vec{x}}{dt} = \vec{v}(\vec{x}, t), \quad \text{con } \vec{x}(t_0) = \vec{x}_0 \qquad \text{[Ec. 2.12]} $$

En coordenadas curvilíneas generales $(h_1, h_2, h_3)$:
$$ dt = \frac{h_1 dx_1}{v_1} = \frac{h_2 dx_2}{v_2} = \frac{h_3 dx_3}{v_3} \qquad \text{[Ec. 2.13]} $$
La trayectoria $\vec{x} = \vec{x}_T(\vec{x}_0, t)$ contiene información posicional y temporal (ritmo al que viaja la partícula). Eliminando el parámetro temporal $t$ se obtienen las **líneas de trayectoria** como intersección de dos superficies implícitas:
$$ f(\vec{x}_0, \vec{x}) = 0 \quad \text{y} \quad g(\vec{x}_0, \vec{x}) = 0 \qquad \text{[Ec. 2.15]} $$

### 2. Líneas, Superficies y Volúmenes Fluidos
* **Línea fluida:** Conjunto de partículas fluidas que en $t_0$ forman una curva $\vec{x}_l(\lambda)$. En cualquier instante posterior continuarán formando una línea fluida $\vec{x} = \vec{x}_T(\vec{x}_l(\lambda), t)$ (Ec. 2.17).
* **Superficie fluida:** Superficie $f(\vec{x}, t) = 0$ compuesta siempre por las mismas partículas fluidas. Dado que las partículas nunca la abandonan, la superficie satisface la **condición cinemática de superficie fluida**:
  $$ \frac{Df}{Dt} = \frac{\partial f}{\partial t} + \vec{v} \cdot \nabla f = 0 $$
* **Volumen fluido:** Volumen finito delimitado por una superficie fluida cerrada. **Ninguna masa puede atravesar una superficie fluida**; por tanto, la masa de un volumen fluido es estrictamente constante en el tiempo:
  $$ \frac{d}{dt}\int_{V_f(t)} \rho \, dV = 0 \quad \text{(Primer principio de conservación)} $$

### 3. Líneas de Corriente (*Stream lines*), Superficies y Tubos de Corriente
Son las curvas tangentes en cada punto al vector velocidad instantáneo en un instante de tiempo $t$ fijado ("congelado"):

$$ d\vec{x} \wedge \vec{v} = 0 \iff \frac{h_1 dx_1}{v_1(\vec{x}, t)} = \frac{h_2 dx_2}{v_2(\vec{x}, t)} = \frac{h_3 dx_3}{v_3(\vec{x}, t)} \qquad \text{[Ec. 2.21]} $$

* En cartesianas: $\frac{dx}{v_x} = \frac{dy}{v_y} = \frac{dz}{v_z}$.
* En cilíndricas: $\frac{dr}{v_r} = \frac{r d\theta}{v_\theta} = \frac{dz}{v_z}$.
* En esféricas: $\frac{dr}{v_r} = \frac{r d\theta}{v_\theta} = \frac{r\sin\theta d\phi}{v_\phi}$.

* **Superficie de corriente:** Superficie reglada formada por todas las líneas de corriente que se apoyan sobre una directriz. Dado que $\vec{v}$ es tangente a ella en todo punto, el flujo de masa convectivo a través de una superficie de corriente es idénticamente nulo:
  $$ \vec{v} \cdot \vec{n} = 0 $$
* **Tubo de corriente:** Superficie de corriente cerrada generada a partir de una curva directriz cerrada.

---

## 🔍 4. Comparación Crucial: ¿Cuándo Coinciden Trayectorias y Líneas de Corriente?

| Característica | Trayectoria (*Path line*) | Línea de Corriente (*Stream line*) |
| :--- | :--- | :--- |
| **Concepto matemático** | Problema de Cauchy de evolución temporal ($t$ es variable de integración). | Familia de curvas espaciales instantáneas ($t$ actúa como un parámetro congelado). |
| **Visualización experimental** | Fotografía de larga exposición de una partícula trazadora iluminada. | Campo instantáneo de vectores tangentes obtenido con anemometría PIV. |

### Teorema de Coincidencia (Notes.pdf, pág. 13)
Las trayectorias y las líneas de corriente **coinciden** en dos casos fundamentales:
1. **Flujo estrictamente estacionario:** $\vec{v} = \vec{v}(\vec{x})$.
2. **Flujo de dirección invariable en el tiempo:** $\vec{v}(\vec{x}, t) = f(t) \vec{V}(\vec{x})$, donde la magnitud de la velocidad varía con el tiempo pero su orientación espacial permanece congelada.

> [!NOTE] Intersección de Líneas de Corriente
> Dos líneas de corriente correspondientes a un mismo instante $t$ **únicamente pueden cruzarse en un punto de remanso** ($\vec{v} = 0$), pues de lo contrario el vector velocidad tendría dos direcciones distintas en un mismo punto espacial, violando la continuidad y univocidad del campo de velocidades.

---

## 🔗 Conceptos Relacionados
* `[[01 - Fluid Mechanics/Tema 2 - Flow Kinematics|Tema 2: Flow Kinematics]]`
* `[[01 - Fluid Mechanics/Concepto - Derivada Material y Aceleracion del Fluido|Concepto: Derivada Material y Aceleración]]`
* `[[01 - Fluid Mechanics/Concepto - Flujo Convectivo y Funcion de Corriente|Concepto: Función de Corriente]]`
