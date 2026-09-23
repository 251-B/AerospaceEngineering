---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - couette
  - deformacion
  - vorticidad
  - circulacion
dificultad: media
fuente: "sources/01-fluid-mechanics/problemas/1.Kinematics/K2.pdf"
---

# ✏️ Problema K2: Flujo de Couette Plano y Análisis de Deformación / Rotación

> **Origen:** Hoja de Problemas de Cinemática, UC3M (Prof. Antonio L. Sánchez & Javier Rodríguez-Rodríguez). Solución manuscrita oficial cotejada.

---

## 📋 Enunciado

Consider the steady flow of a liquid confined between two parallel planar walls separated a distance $H$. If the top wall moves with constant velocity $U$, the resulting fluid motion exhibits a single velocity component $v_x = Uy/H$, where $y$ denotes the distance to the bottom wall, assumed to be at rest.

1. Determine the streamlines and the trajectories.
2. Obtain the vorticity field.
3. Compute the circulation $\Gamma$ around a rectangular line of side $L$ oriented parallel to the walls and height $h$.
4. Calculate the gradient of velocity, the rate-of-strain tensor and the expansion rate.
5. Obtain the principal directions of strain as well as the associated principal strain rates.
6. Investigate the evolution of a square fluid element of side $dl$ oriented parallel to the walls.

---

## 🎯 1. Planteamiento Físico e Hipótesis

* **Geometría:** Canal bidimensional entre dos placas planas infinitas paralelas en $y = 0$ (pared inferior en reposo) e $y = H$ (pared superior móvil a velocidad constante $U$).
* **Campo de velocidades:**
  $$ \vec{v}(x, y) = \frac{U y}{H} \vec{e}_x + 0 \vec{e}_y $$
* **Régimen:** Flujo estacionario ($\partial \vec{v}/\partial t = 0$), estrictamente unidireccional y bidimensional.

---

## 🔍 2. Resolución Matemática Paso a Paso

### Apartado 1: Líneas de Corriente y Trayectorias

#### Líneas de Corriente (*Streamlines*)
Por definición, una línea de corriente satisface la ecuación diferencial:
$$ \frac{dx}{v_x} = \frac{dy}{v_y} $$
Dado que $v_y = 0$:
$$ dy = 0 \implies \mathbf{y = y_0 = \text{cte}} $$
Las líneas de corriente son líneas horizontales rectas paralelas a las paredes del canal.

#### Trayectorias (*Path lines*)
El movimiento lagrangiano de una partícula fluida inicialmente en $(x_0, y_0)$ viene determinado por el sistema dinámico:
$$ \frac{dy}{dt} = v_y = 0 \implies y(t) = y_0 $$
$$ \frac{dx}{dt} = v_x = \frac{U y_0}{H} $$
Integrando respecto al tiempo con la condición inicial $x(0) = x_0$:
$$ x(t) - x_0 = \int_0^t \frac{U y_0}{H} dt' \implies \mathbf{x(t) - x_0 = \frac{U y_0}{H} t} $$

> [!NOTE] Coincidencia Cinemática
> Al tratarse de un flujo estacionario ($\partial \vec{v}/\partial t = 0$), las líneas de corriente, las trayectorias y las líneas de traza (*streak lines*) coinciden idénticamente en el espacio físico ($y = y_0$).

---

### Apartado 2: Campo de Vorticidad

El vector vorticidad $\vec{\omega}$ se calcula como el rotacional del campo de velocidades:
$$ \vec{\omega} = \nabla \wedge \vec{v} = \omega_z \vec{e}_z = \left( \frac{\partial v_y}{\partial x} - \frac{\partial v_x}{\partial y} \right) \vec{e}_z $$
Calculando cada término:
$$ \frac{\partial v_y}{\partial x} = 0, \qquad \frac{\partial v_x}{\partial y} = \frac{\partial}{\partial y}\left(\frac{U y}{H}\right) = \frac{U}{H} $$
Por lo tanto:
$$ \mathbf{\vec{\omega} = -\frac{U}{H} \vec{e}_z} $$
El campo de vorticidad es **uniforme y no nulo** en todo el dominio entre placas, orientado en sentido horario (hacia el fondo del plano, $-\vec{e}_z$).

---

### Apartado 3: Circulación $\Gamma$ alrededor de un Rectángulo

Consideramos un contorno cerrado rectangular de base $L$ paralela a las paredes (desde $x$ hasta $x+L$) y altura $h$ (desde $y$ hasta $y+h$), recorrido en sentido antihorario.

#### Método Directo (Integral de Línea):
$$ \Gamma = \oint \vec{v} \cdot d\vec{l} = \int_{x}^{x+L} v_x(y) dx + \int_{y}^{y+h} v_y(x+L) dy - \int_{x}^{x+L} v_x(y+h) dx - \int_{y}^{y+h} v_y(x) dy $$
Como $v_y = 0$ idénticamente en todo el flujo, las integrales sobre los tramos verticales se anulan:
$$ \Gamma = \frac{U y}{H} L + 0 - \frac{U (y+h)}{H} L - 0 $$
$$ \mathbf{\Gamma = -\frac{U h L}{H}} $$

#### Comprobación mediante el Teorema de Stokes:
$$ \Gamma = \iint_S (\nabla \wedge \vec{v}) \cdot \vec{n} \, d\sigma = \iint_S \left(-\frac{U}{H} \vec{e}_z\right) \cdot \vec{e}_z \, d\sigma = -\frac{U}{H} \text{Área} = \mathbf{-\frac{U h L}{H}} $$
Ambos métodos coinciden con total exactitud.

---

### Apartado 4: Gradiente de Velocidad, Tensor de Deformación y Tasa de Expansión

#### Gradiente de Velocidad $\nabla \vec{v}$:
En notación de matriz cartesiana con la convención estándar del curso:
$$ \nabla \vec{v} = \begin{bmatrix} \frac{\partial v_x}{\partial x} & \frac{\partial v_y}{\partial x} \\ \frac{\partial v_x}{\partial y} & \frac{\partial v_y}{\partial y} \end{bmatrix}^T \implies \nabla \vec{v} = \begin{bmatrix} 0 & 0 \\ \frac{U}{H} & 0 \end{bmatrix} $$

#### Tensor de Velocidad de Deformación (Rate-of-Strain Tensor) $\bar{\bar{T}}_d$:
Parte simétrica del gradiente:
$$ \bar{\bar{T}}_d = \frac{1}{2}\left( \nabla \vec{v} + (\nabla \vec{v})^T \right) = \mathbf{\begin{bmatrix} 0 & \frac{1}{2}\frac{U}{H} \\ \frac{1}{2}\frac{U}{H} & 0 \end{bmatrix}} $$

#### Tensor de Velocidad de Rotación $\bar{\bar{T}}_r$:
Parte antisimétrica del gradiente:
$$ \bar{\bar{T}}_r = \frac{1}{2}\left( \nabla \vec{v} - (\nabla \vec{v})^T \right) = \mathbf{\begin{bmatrix} 0 & -\frac{1}{2}\frac{U}{H} \\ \frac{1}{2}\frac{U}{H} & 0 \end{bmatrix}} $$

#### Tasa de Expansión Volumétrica $\nabla \cdot \vec{v}$:
$$ \nabla \cdot \vec{v} = \text{tr}(\bar{\bar{T}}_d) = \frac{\partial v_x}{\partial x} + \frac{\partial v_y}{\partial y} = 0 + 0 = \mathbf{0} $$
El fluido es incompresible.

---

### Apartado 5: Direcciones Principales y Tasas de Deformación Principal

Para hallar los autovalores y autovectores de $\bar{\bar{T}}_d$:
$$ \det(\bar{\bar{T}}_d - \lambda \bar{\bar{I}}) = \begin{vmatrix} -\lambda & \frac{1}{2}\frac{U}{H} \\ \frac{1}{2}\frac{U}{H} & -\lambda \end{vmatrix} = \lambda^2 - \left(\frac{1}{2}\frac{U}{H}\right)^2 = 0 $$
$$ \mathbf{\lambda = \pm \frac{1}{2}\frac{U}{H}} $$

* **Autovalor de tracción:** $\lambda_1 = +\frac{1}{2}\frac{U}{H}$
  $$ \begin{bmatrix} -\frac{U}{2H} & \frac{U}{2H} \\ \frac{U}{2H} & -\frac{U}{2H} \end{bmatrix} \begin{bmatrix} n_{1x} \\ n_{1y} \end{bmatrix} = 0 \implies n_{1x} = n_{1y} \implies \mathbf{\vec{n}_1 = \left( \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right)} \quad (\text{ángulo } +45^\circ) $$
* **Autovalor de compresión:** $\lambda_2 = -\frac{1}{2}\frac{U}{H}$
  $$ \begin{bmatrix} \frac{U}{2H} & \frac{U}{2H} \\ \frac{U}{2H} & \frac{U}{2H} \end{bmatrix} \begin{bmatrix} n_{2x} \\ n_{2y} \end{bmatrix} = 0 \implies n_{2x} = -n_{2y} \implies \mathbf{\vec{n}_2 = \left( \frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}} \right)} \quad (\text{ángulo } -45^\circ) $$

Las direcciones principales de deformación están rotadas a $\pm 45^\circ$ respecto a las paredes, con alargamiento a $+45^\circ$ y acortamiento a $-45^\circ$.

---

### Apartado 6: Evolución de un Elemento Cuadrado de Fluido de Lado $dl$

Consideremos un elemento inicialmente cuadrado de lado $dl$ con lados alineados con los ejes cartesianos:
$$ d\vec{l}_1 = dl (1, 0), \qquad d\vec{l}_2 = dl (0, 1) $$
En un intervalo infinitesimal $dt$, cada vector material evoluciona según $d\vec{l}(t+dt) = d\vec{l}(t) + d\vec{l}(t) \cdot \nabla \vec{v} \, dt$:

1. **Lado horizontal inferior ($d\vec{l}_1$):**
   $$ dl(1, 0) \to dl(1, 0) + dl(1, 0) \begin{bmatrix} 0 & 0 \\ \frac{U}{H} & 0 \end{bmatrix} dt = \mathbf{dl(1, 0)} $$
   No experimenta deformación ni giro instantáneo porque $v_y = 0$ y $\partial v_x/\partial x = 0$.

2. **Lado vertical izquierdo ($d\vec{l}_2$):**
   $$ dl(0, 1) \to dl(0, 1) + dl(0, 1) \begin{bmatrix} 0 & 0 \\ \frac{U}{H} & 0 \end{bmatrix} dt = \mathbf{dl\left(\frac{U}{H}dt, 1\right)} $$
   El extremo superior avanza una distancia horizontal $\frac{U}{H} dl \, dt$.

#### Interpretación Cinemática Frecuente en Exámenes:
La distorsión observada del cuadrado en un paralelogramo es el **resultado combinado** de:
1. Una **rotación de sólido rígido** con velocidad angular:
   $$ \Omega_z = -\frac{1}{2}\frac{U}{H} \quad (\text{ángulo de giro } -\frac{1}{2}\frac{U}{H}dt) $$
2. Una **deformación por cizalladura pura** con tasa de deformación angular:
   $$ \dot{\gamma} = \frac{U}{H} \quad (\text{deformación simétrica de semilados en } \pm \frac{1}{2}\frac{U}{H}dt) $$

---

## 📌 Resumen de Fórmulas Clave

| Magnitud | Expresión | Interpretación |
| :--- | :--- | :--- |
| **Líneas de corriente** | $y = y_0$ | Rectas paralelas a las paredes |
| **Trayectoria** | $x(t) = x_0 + \frac{Uy_0}{H}t$ | Velocidad constante para cada capa $y_0$ |
| **Vorticidad** | $\vec{\omega} = -\frac{U}{H}\vec{e}_z$ | Rotacional no nulo, constante en el espacio |
| **Circulación** | $\Gamma = -\frac{U h L}{H}$ | Proporcional al área encerrada $L \cdot h$ |
| **Deformación principal** | $\lambda = \pm \frac{U}{2H}$ en $\pm 45^\circ$ | Tracción a $+45^\circ$, compresión a $-45^\circ$ |
