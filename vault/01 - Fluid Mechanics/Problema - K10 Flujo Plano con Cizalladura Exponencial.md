---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - flujo-potencial
  - cizalladura-pura
  - funcion-corriente
  - tensor-deformacion
dificultad: media
fuente: "sources/01-fluid-mechanics/problemas/1.Kinematics/K10.pdf"
---

# ✏️ Problema K10: Flujo Plano con Cizalladura Exponencial y Deformación Pura

> **Origen:** Hoja de Problemas de Cinemática, UC3M (Quiz Oficial Sept 30, 2013). Solución manuscrita oficial cotejada.

---

## 📋 Enunciado

Given the planar motion described by the velocity components

$$ v_x = A e^{\Omega t} y, \qquad v_y = B e^{\Omega t} x $$

where $A, B$, and $\Omega$ are constants.

1. Determine the value of the volume dilation rate $\nabla \cdot \vec{v}$.
2. Obtain the value of $B$ for which the resulting flow is irrotational. Adopt this particular value in what follows.
3. Calculate the stream line that intersects the point $(x, y) = (x_0, y_0)$ at a given instant of time $t$. Sketch the resulting streamlines.
4. Compute the trajectory of a fluid particle located initially at $(x, y) = (x_0, y_0)$.
5. If they exist, calculate the velocity potential $\phi$ and the stream function $\psi$.
6. Determine the rate-of-strain tensor $\bar{\bar{T}}_d$.
7. Describe the deformation of a fluid element of square shape whose sides of length $dl$ are initially oriented parallel to the axes.

---

## 🎯 1. Planteamiento Físico e Hipótesis

* **Geometría:** Movimiento plano bidimensional en coordenadas cartesianas $(x, y)$.
* **Dependencia temporal:** Crecimiento o relajación exponencial temporal gobernado por $e^{\Omega t}$.
* **Cinemática lineal en el espacio:** Velocidades proporcionales a las coordenadas cruzadas ($v_x \propto y, v_y \propto x$).

---

## 🔍 2. Resolución Matemática Paso a Paso

### Apartado 1: Tasa de Dilatación Volumétrica $\nabla \cdot \vec{v}$

La divergencia en coordenadas cartesianas es:
$$ \nabla \cdot \vec{v} = \frac{\partial v_x}{\partial x} + \frac{\partial v_y}{\partial y} = \frac{\partial}{\partial x}\left(A e^{\Omega t} y\right) + \frac{\partial}{\partial y}\left(B e^{\Omega t} x\right) = 0 + 0 = \mathbf{0} $$
La tasa de dilatación volumétrica es nula para cualquier valor de las constantes; el flujo es **incompresible**.

---

### Apartado 2: Condición de Irrotacionalidad

Calculamos la componente ortogonal del rotacional de la velocidad:
$$ \vec{\omega} = \nabla \wedge \vec{v} = \left( \frac{\partial v_y}{\partial x} - \frac{\partial v_x}{\partial y} \right) \vec{e}_z = \left( B e^{\Omega t} - A e^{\Omega t} \right) \vec{e}_z = (B - A) e^{\Omega t} \, \vec{e}_z $$
Para que el flujo sea **irrotacional** ($\vec{\omega} = 0$) en todo instante de tiempo:
$$ B - A = 0 \implies \mathbf{B = A} $$
Adoptando esta condición en adelante, el campo queda:
$$ \mathbf{\vec{v} = A e^{\Omega t} y \, \vec{e}_x + A e^{\Omega t} x \, \vec{e}_y} $$

---

### Apartado 3: Líneas de Corriente (*Streamlines*)

A cualquier instante fijo $t$:
$$ \frac{dx}{v_x} = \frac{dy}{v_y} \implies \frac{dx}{A e^{\Omega t} y} = \frac{dy}{A e^{\Omega t} x} \implies \frac{dx}{y} = \frac{dy}{x} $$
Multiplicando en cruz:
$$ y \, dy - x \, dx = 0 \implies \frac{1}{2} d(y^2 - x^2) = 0 $$
Integrando con la condición de pasar por $(x_0, y_0)$:
$$ \mathbf{y^2 - x^2 = y_0^2 - x_0^2} $$
Las líneas de corriente forman una familia de **hipérbolas equiláteras** simétricas respecto a las bisectrices $y = \pm x$ (asíntotas del flujo).

---

### Apartado 4: Trayectorias y Líneas de Trayectoria

El sistema dinámico lagrangiano para la partícula inicialmente en $(x_0, y_0)$ es:
$$ \frac{dx}{dt} = A e^{\Omega t} y, \qquad \frac{dy}{dt} = A e^{\Omega t} x $$

#### 1. Líneas de Trayectoria (*Path lines*):
Dividiendo ambas ecuaciones diferenciales:
$$ \frac{dy}{dx} = \frac{x}{y} \implies y \, dy = x \, dx \implies \mathbf{y^2 - x^2 = y_0^2 - x_0^2} $$
Las líneas de trayectoria son **idénticas a las líneas de corriente**.

#### 2. Integración Temporal de la Trayectoria:
Despejando $y = \pm \sqrt{x^2 + y_0^2 - x_0^2}$ y separando variables:
$$ \int_{x_0}^x \frac{dx'}{\sqrt{x'^2 + y_0^2 - x_0^2}} = \pm \int_0^t A e^{\Omega t'} dt' $$
$$ \mathbf{\ln\left( \frac{x + \sqrt{x^2 + y_0^2 - x_0^2}}{x_0 + y_0} \right) = \pm \frac{A}{\Omega}\left(e^{\Omega t} - 1\right)} $$

*(Alternativa por desacoplo de modos propios):*
Definiendo las variables diagonales $u = x + y$ y $w = x - y$:
$$ \frac{du}{dt} = A e^{\Omega t} u \implies u(t) = (x_0 + y_0) \exp\left[ \frac{A}{\Omega}(e^{\Omega t} - 1) \right] $$
$$ \frac{dw}{dt} = -A e^{\Omega t} w \implies w(t) = (x_0 - y_0) \exp\left[ -\frac{A}{\Omega}(e^{\Omega t} - 1) \right] $$
Sumando y restando se obtienen las coordenadas explícitas $(x(t), y(t))$. Nótese que $u(t) w(t) = x^2 - y^2 = x_0^2 - y_0^2$, confirmando de inmediato la hipérbola.

---

### Apartado 5: Potencial de Velocidades $\phi$ y Función de Corriente $\psi$

#### 1. Potencial de Velocidades $\phi(x, y, t)$:
Al ser irrotacional ($\vec{v} = \nabla \phi$):
$$ \frac{\partial \phi}{\partial x} = v_x = A e^{\Omega t} y \implies \phi = A e^{\Omega t} x y + f(y, t) $$
$$ \frac{\partial \phi}{\partial y} = A e^{\Omega t} x + \frac{\partial f}{\partial y} = v_y = A e^{\Omega t} x \implies \frac{\partial f}{\partial y} = 0 \implies f = \phi_0(t) $$
$$ \mathbf{\phi(x, y, t) = A e^{\Omega t} x y + \phi_0} $$

#### 2. Función de Corriente $\psi(x, y, t)$:
Al ser incompresible:
$$ v_x = \frac{\partial \psi}{\partial y} = A e^{\Omega t} y \implies \psi = \frac{1}{2} A e^{\Omega t} y^2 + g(x, t) $$
$$ v_y = -\frac{\partial \psi}{\partial x} = -\frac{\partial g}{\partial x} = A e^{\Omega t} x \implies \frac{\partial g}{\partial x} = -A e^{\Omega t} x \implies g = -\frac{1}{2} A e^{\Omega t} x^2 + \psi_0(t) $$
$$ \mathbf{\psi(x, y, t) = \frac{1}{2} A e^{\Omega t}\left(y^2 - x^2\right) + \psi_0} $$
Las isolíneas $\psi = \text{cte}$ recuperan directamente las líneas de corriente $y^2 - x^2 = \text{cte}$.

---

### Apartado 6: Tensor de Velocidad de Deformación $\bar{\bar{T}}_d$

Calculamos la matriz de gradientes de velocidad:
$$ \nabla \vec{v} = \begin{bmatrix} \frac{\partial v_x}{\partial x} & \frac{\partial v_y}{\partial x} \\ \frac{\partial v_x}{\partial y} & \frac{\partial v_y}{\partial y} \end{bmatrix}^T = \begin{bmatrix} 0 & A e^{\Omega t} \\ A e^{\Omega t} & 0 \end{bmatrix} $$
Puesto que $\nabla \vec{v}$ es idénticamente simétrica:
$$ \mathbf{\bar{\bar{T}}_d = \frac{1}{2}\left(\nabla \vec{v} + (\nabla \vec{v})^T\right) = \begin{bmatrix} 0 & A e^{\Omega t} \\ A e^{\Omega t} & 0 \end{bmatrix}} $$
El tensor de velocidades de rotación es idénticamente nulo:
$$ \mathbf{\bar{\bar{T}}_r = \frac{1}{2}\left(\nabla \vec{v} - (\nabla \vec{v})^T\right) = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}} $$

---

### Apartado 7: Deformación de un Elemento Cuadrado de Lado $dl$

Consideremos dos segmentos materiales iniciales que forman las aristas del cuadrado alineadas con los ejes coordenados:
$$ d\vec{l}_1 = dl (1, 0), \qquad d\vec{l}_2 = dl (0, 1) $$
Evolucionando en un incremento infinitesimal $dt$:
$$ d\vec{l}_1(t+dt) = dl (1, 0) + dl (1, 0) \begin{bmatrix} 0 & A e^{\Omega t} \\ A e^{\Omega t} & 0 \end{bmatrix} dt = \mathbf{dl \left( 1, \; A e^{\Omega t} dt \right)} $$
$$ d\vec{l}_2(t+dt) = dl (0, 1) + dl (0, 1) \begin{bmatrix} 0 & A e^{\Omega t} \\ A e^{\Omega t} & 0 \end{bmatrix} dt = \mathbf{dl \left( A e^{\Omega t} dt, \; 1 \right)} $$

#### Interpretación Cinemática:
* **Lado horizontal:** Se inclina hacia arriba un ángulo infinitesimal $d\alpha = A e^{\Omega t} dt$.
* **Lado vertical:** Se inclina hacia la derecha un ángulo idéntico $d\beta = A e^{\Omega t} dt$.
* **Velocidad angular media (rotación rígida):**
  $$ \Omega_z = \frac{d\alpha - d\beta}{2 dt} = 0 $$
* **Tasa de deformación por cizalladura (*shear strain rate*):**
  $$ \dot{\gamma}_{xy} = \frac{d\alpha + d\beta}{dt} = 2 A e^{\Omega t} $$
* **Estado cinemático:** Se trata de **cizalladura pura** (*pure shear strain*), donde el cuadrado se deforma simétricamente en un rombo sin experimentar ninguna rotación de cuerpo rígido.
