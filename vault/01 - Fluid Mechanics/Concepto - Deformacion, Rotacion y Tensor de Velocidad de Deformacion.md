---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - teoria
  - concepto-clave
  - tensor-deformacion
  - vorticidad
  - helmholtz
dificultad: alta
prerrequisitos: []
---

# 🔬 Concepto: Cinemática de la Deformación, Rotación y Tensor de Velocidad de Deformación

> **Idea clave en una frase:** El movimiento relativo local de un elemento fluido respecto a su entorno se descompone exactamente (teorema de Helmholtz) en una rotación de sólido rígido a velocidad angular $\frac{1}{2}\vec{\omega}$ descrita por el tensor antisimétrico $\bar{\bar{T}}_r$, y una deformación pura descrita por el tensor simétrico $\bar{\bar{T}}_d$, cuya traza mide la tasa de dilatación volumétrica ($\nabla \cdot \vec{v}$) y cuyos términos fuera de la diagonal representan la velocidad de distorsión angular (cizalladura).

---

## 🎯 1. Movimiento Relativo Cerca de un Punto (Notes.pdf, Ec. 2.46)

La fuerza viscosa interna ejercida entre partículas fluidas contiguas depende exclusivamente de la rapidez con la que el fluido se deforma.

Consideremos un elemento de línea fluida infinitesimal $d\vec{x}$ cuyos extremos ocupan en el instante $t$ las posiciones $\vec{x}$ y $\vec{x} + d\vec{x}$. Las velocidades de ambos extremos difieren en una cantidad diferencial $d\vec{v}$, expresable en primera aproximación mediante el tensor gradiente de velocidad $\nabla\vec{v}$:

$$ d\vec{v} = d\vec{x} \cdot \nabla\vec{v} \qquad \text{[Ec. 2.46]} $$

Tras un tiempo infinitesimal $dt$, los extremos ocupan $\vec{x} + \vec{v} dt$ y $\vec{x} + d\vec{x} + (\vec{v} + d\vec{v}) dt$. El vector elemental evoluciona según:
$$ d\vec{x} \longrightarrow d\vec{x} + d\vec{v} \, dt = d\vec{x} + (d\vec{x} \cdot \nabla\vec{v}) \, dt $$
Por tanto, además de una traslación global $\vec{v} dt$, el elemento experimenta una distorsión espacial gobernada por $\nabla\vec{v}$.

---

## 📐 2. Descomposición de Helmholtz / Cauchy (Notes.pdf, Ecs. 2.47–2.52)

Todo tensor de segundo orden puede descomponerse de forma única en la suma de un tensor simétrico y un tensor antisimétrico:

$$ \mathbf{\nabla\vec{v} = \underbrace{\frac{1}{2}(\nabla\vec{v} + \nabla\vec{v}^T)}_{\bar{\bar{T}}_d \text{ (simétrico)}} + \underbrace{\frac{1}{2}(\nabla\vec{v} - \nabla\vec{v}^T)}_{\bar{\bar{T}}_r \text{ (antisimétrico)}}} \qquad \text{[Ec. 2.47]} $$

El diferencial de velocidad relativo se descompone correspondientemente en:
$$ d\vec{v} = d\vec{x} \cdot \bar{\bar{T}}_d + d\vec{x} \cdot \bar{\bar{T}}_r = d\vec{v}_d + d\vec{v}_r \qquad \text{[Ec. 2.51]} $$

### A. Tensor Velocidad de Rotación ($\bar{\bar{T}}_r$) y Rotación de Sólido Rígido
En coordenadas cartesianas, el tensor antisimétrico $\bar{\bar{T}}_r$ viene dado por:

$$ \bar{\bar{T}}_r = \frac{1}{2} \begin{bmatrix} 0 & \frac{\partial v_2}{\partial x_1} - \frac{\partial v_1}{\partial x_2} & \frac{\partial v_3}{\partial x_1} - \frac{\partial v_1}{\partial x_3} \\ -\left(\frac{\partial v_2}{\partial x_1} - \frac{\partial v_1}{\partial x_2}\right) & 0 & \frac{\partial v_3}{\partial x_2} - \frac{\partial v_2}{\partial x_3} \\ -\left(\frac{\partial v_3}{\partial x_1} - \frac{\partial v_1}{\partial x_3}\right) & -\left(\frac{\partial v_3}{\partial x_2} - \frac{\partial v_2}{\partial x_3}\right) & 0 \end{bmatrix} \qquad \text{[Ec. 2.49]} $$

Introduciendo las componentes del vector vorticidad $\vec{\omega} = \nabla \wedge \vec{v} = (\omega_1, \omega_2, \omega_3)$:
$$ \mathbf{\bar{\bar{T}}_r = \frac{1}{2} \begin{bmatrix} 0 & \omega_3 & -\omega_2 \\ -\omega_3 & 0 & \omega_1 \\ \omega_2 & -\omega_1 & 0 \end{bmatrix}} \qquad \text{[Ec. 2.50]} $$

Operando sobre el elemento diferencial $d\vec{x}$:
$$ d\vec{v}_r = d\vec{x} \cdot \bar{\bar{T}}_r = \frac{1}{2}(\nabla \wedge \vec{v}) \wedge d\vec{x} = \mathbf{\frac{1}{2} \vec{\omega} \wedge d\vec{x}} \qquad \text{[Ec. 2.52]} $$

> [!NOTE] Interpretación Física de la Rotación
> La contribución $d\vec{v}_r$ representa una **rotación pura de sólido rígido** del elemento $d\vec{x}$ con velocidad angular instantánea:
> $$ \vec{\Omega}_{\text{fluido}} = \frac{1}{2} \vec{\omega} = \frac{1}{2} (\nabla \wedge \vec{v}) $$
> Si el tensor de deformación $\bar{\bar{T}}_d$ fuera nulo, el elemento no sufriría distorsión alguna: su movimiento se limitaría a traslación pura y rotación como sólido indeformable.

### B. Tensor Velocidad de Deformación ($\bar{\bar{T}}_d$)
El tensor simétrico $\bar{\bar{T}}_d$ (*rate-of-strain tensor*) gobierna la distorsión geométrica real del fluido:

$$ \mathbf{\bar{\bar{T}}_d = \begin{bmatrix} \frac{\partial v_1}{\partial x_1} & \frac{1}{2}\left(\frac{\partial v_2}{\partial x_1} + \frac{\partial v_1}{\partial x_2}\right) & \frac{1}{2}\left(\frac{\partial v_3}{\partial x_1} + \frac{\partial v_1}{\partial x_3}\right) \\ \frac{1}{2}\left(\frac{\partial v_2}{\partial x_1} + \frac{\partial v_1}{\partial x_2}\right) & \frac{\partial v_2}{\partial x_2} & \frac{1}{2}\left(\frac{\partial v_3}{\partial x_2} + \frac{\partial v_2}{\partial x_3}\right) \\ \frac{1}{2}\left(\frac{\partial v_3}{\partial x_1} + \frac{\partial v_1}{\partial x_3}\right) & \frac{1}{2}\left(\frac{\partial v_3}{\partial x_2} + \frac{\partial v_2}{\partial x_3}\right) & \frac{\partial v_3}{\partial x_3} \end{bmatrix}} \qquad \text{[Ec. 2.48]} $$

Escribiendo el elemento de línea como $d\vec{x} = \vec{n} ds$ (con $|\vec{n}| = 1$ y longitud $ds$):
$$ d\vec{v}_d = \bar{\bar{T}}_d \cdot \vec{n} \, ds \qquad \text{[Ec. 2.53]} $$
En general, $d\vec{v}_d$ no está alineado con $\vec{n}$, lo que indica que el elemento experimenta simultáneamente dos efectos:
1. **Tasa de extensión unitaria en la dirección $\vec{n}$:** Proyección longitudinal sobre $\vec{n}$:
   $$ \dot{\epsilon}_n = \vec{n} \cdot \bar{\bar{T}}_d \cdot \vec{n} $$
2. **Tasa de deformación angular (cizalladura):** Componente ortogonal a $\vec{n}$:
   $$ \vec{\gamma}_n = \left[ \bar{\bar{T}}_d \cdot \vec{n} - (\vec{n} \cdot \bar{\bar{T}}_d \cdot \vec{n})\vec{n} \right] ds $$

---

## 🌟 3. Direcciones Principales de Deformación (Notes.pdf, Ecs. 2.54–2.55)

Existen tres direcciones ortogonales privilegiadas del espacio a lo largo de las cuales la deformación se reduce a una **extensión o compresión pura, sin cizalladura alguna** ($d\vec{v}_d \parallel \vec{n}$).

Dichas direcciones principales $(\vec{n}_1, \vec{n}_2, \vec{n}_3)$ y sus correspondientes tasas de deformación principal $(\lambda_1, \lambda_2, \lambda_3)$ se obtienen resolviendo el problema de autovalores:

$$ \bar{\bar{T}}_d \cdot \vec{n} = \lambda \vec{n} \qquad \text{[Ec. 2.54]} $$

Imponiendo la existencia de soluciones no triviales se llega a la **ecuación característica**:

$$ |\bar{\bar{T}}_d - \lambda \bar{\bar{I}}| = 0 \qquad \text{[Ec. 2.55]} $$

Dado que $\bar{\bar{T}}_d$ es un tensor real y simétrico, el teorema espectral garantiza que:
1. Las tres raíces $\lambda_1, \lambda_2, \lambda_3$ son **estrictamente reales**.
2. Los tres autovectores directores $(\vec{n}_1, \vec{n}_2, \vec{n}_3)$ son **mutuamente perpendiculares**.
3. En el sistema de referencia principal, el tensor adopta forma diagonal: $\bar{\bar{T}}_d = \text{diag}(\lambda_1, \lambda_2, \lambda_3)$.

---

## 📦 4. Deformación de Elementos Cuadrado y Cúbico (Notes.pdf, Ecs. 2.56–2.63)

### A. Elemento Cuadrado Bidimensional (Lado $dl$)
Al analizar la evolución temporal de los lados horizontal $dl(1, 0)$ y vertical $dl(0, 1)$:
* **Elementos diagonales:** $(\bar{\bar{T}}_d)_{11} = \frac{\partial v_1}{\partial x_1}$ y $(\bar{\bar{T}}_d)_{22} = \frac{\partial v_2}{\partial x_2}$ representan la tasa de alargamiento relativo por unidad de longitud en cada eje.
* **Elementos fuera de diagonal de $\bar{\bar{T}}_d$:** $\frac{1}{2}\left(\frac{\partial v_2}{\partial x_1} + \frac{\partial v_1}{\partial x_2}\right)$ representa la mitad de la rapidez con la que disminuye el ángulo recto original entre los dos lados (velocidad de deformación angular por cizalladura).
* **Elementos de $\bar{\bar{T}}_r$:** $\frac{1}{2}\left(\frac{\partial v_2}{\partial x_1} - \frac{\partial v_1}{\partial x_2}\right) = \frac{1}{2}\omega_3$ representa la velocidad angular media de giro del elemento en su propio plano.

### B. Elemento Cúbico Tridimensional: Tasa de Dilatación Volumétrica
Consideremos un elemento cúbico diferencial de volumen inicial $V_0 = dl^3$. Tras un tiempo $dt$, cada una de las tres aristas se distorsiona según $dl \vec{e}_i + dl (\vec{e}_i \cdot \nabla\vec{v}) dt$. El volumen final viene determinado por el producto mixto (determinante de la transformación):

$$ V_f = dl^3 \begin{vmatrix} 1 + \frac{\partial v_1}{\partial x_1} dt & \frac{\partial v_2}{\partial x_1} dt & \frac{\partial v_3}{\partial x_1} dt \\ \frac{\partial v_1}{\partial x_2} dt & 1 + \frac{\partial v_2}{\partial x_2} dt & \frac{\partial v_3}{\partial x_2} dt \\ \frac{\partial v_1}{\partial x_3} dt & \frac{\partial v_2}{\partial x_3} dt & 1 + \frac{\partial v_3}{\partial x_3} dt \end{vmatrix} \qquad \text{[Ec. 2.62]} $$

Desarrollando el determinante y despreciando términos de orden superior $\mathcal{O}(dt^2, dt^3)$:

$$ V_f \simeq dl^3 \left[ 1 + \left( \frac{\partial v_1}{\partial x_1} + \frac{\partial v_2}{\partial x_2} + \frac{\partial v_3}{\partial x_3} \right) dt \right] $$

Dividiendo entre el volumen inicial y el incremento de tiempo, la **tasa de dilatación volumétrica unitaria** es idénticamente la divergencia de la velocidad y coincide con la traza del tensor de velocidades de deformación:

$$ \mathbf{\frac{1}{V}\frac{dV}{dt} = \nabla \cdot \vec{v} = \text{tr}(\nabla\vec{v}) = \text{tr}(\bar{\bar{T}}_d) = \lambda_1 + \lambda_2 + \lambda_3} $$

### C. Condición de Incompresibilidad
Para un líquido perfecto (densidad estrictamente constante $\rho = \rho_0$), el volumen de la partícula no puede variar:

$$ \mathbf{\nabla \cdot \vec{v} = 0 \iff \frac{\partial v_1}{\partial x_1} + \frac{\partial v_2}{\partial x_2} + \frac{\partial v_3}{\partial x_3} = 0} \qquad \text{[Ec. 2.63]} $$

Físicamente, esto implica que las tasas de extensión $(\partial_1 v_1, \partial_2 v_2, \partial_3 v_3)$ **no pueden tener todas el mismo signo**: una extensión positiva en una dirección debe compensarse obligatoriamente con contracciones en las direcciones restantes para preservar el volumen.

---

## 🔗 Conceptos Relacionados
* `[[01 - Fluid Mechanics/Tema 2 - Flow Kinematics|Tema 2: Flow Kinematics]]`
* `[[01 - Fluid Mechanics/Concepto - Vorticidad, Circulacion y Potencial de Velocidades|Concepto: Vorticidad y Circulación]]`
* `[[01 - Fluid Mechanics/Concepto - Flujo Convectivo y Funcion de Corriente|Concepto: Flujo Convectivo y Divergencia]]`
