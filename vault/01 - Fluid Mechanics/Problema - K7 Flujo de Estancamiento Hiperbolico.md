---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - estancamiento-plano
  - funcion-corriente
  - tensor-deformacion
  - aceleracion-convectiva
dificultad: media
fuente: "sources/01-fluid-mechanics/problemas/1.Kinematics/K7.pdf"
---

# ✏️ Problema K7: Flujo de Estancamiento Hiperbólico Plano

> **Origen:** Hoja de Problemas de Cinemática, UC3M (Prof. Antonio L. Sánchez & Javier Rodríguez-Rodríguez). Solución manuscrita oficial cotejada.

---

## 📋 Enunciado

Consider the planar motion of velocity components $v_x = ax$ and $v_y = by$, where $a$ and $b$ are known constants.

1. If the flow is irrotational compute the associated velocity potential.
2. Compute the value of $b$ for which the flow corresponds to that of an incompressible fluid (use that value in the solution of the following questions).
3. Obtain the stream lines and represent the result schematically.
4. Determine the trajectory and the path of a fluid particle initially located at $x_0 = 0$ and $y_0 = 1$. How long does it take to reach the origin?
5. Calculate the acceleration of fluid particles located along the axis $y=0$.
6. Find the stream function for the flow.
7. Compute the rate-of-strain tensor.
8. Investigate the evolution of a fluid element whose initial shape is that of a square of sides $dl$.

---

## 🎯 1. Planteamiento Físico e Hipótesis

* **Geometría:** Movimiento plano bidimensional en el plano $(x, y)$.
* **Campo de velocidades general:** $\vec{v} = ax \vec{e}_x + by \vec{e}_y$.
* **Modelo físico:** Flujo potencial y viscoso asintótico en las proximidades de una pared plana normal al flujo incidente (punto de estancamiento hiperbólico de Hiemenz).

---

## 🔍 2. Resolución Matemática Paso a Paso

### Apartado 1: Condición de Irrotacionalidad y Potencial de Velocidades

El rotacional de la velocidad es:
$$ \vec{\omega} = \nabla \wedge \vec{v} = \left( \frac{\partial v_y}{\partial x} - \frac{\partial v_x}{\partial y} \right) \vec{e}_z = (0 - 0) \vec{e}_z = \mathbf{0} $$
El flujo es **idénticamente irrotacional** para cualquier valor constante de $a$ y $b$.
Por tanto, existe un potencial de velocidades $\phi(x, y)$ tal que $\vec{v} = \nabla \phi$:
$$ \frac{\partial \phi}{\partial x} = v_x = ax \implies \phi(x, y) = a \frac{x^2}{2} + g(y) $$
$$ \frac{\partial \phi}{\partial y} = g'(y) = v_y = by \implies g(y) = b \frac{y^2}{2} + \phi_0 $$
$$ \mathbf{\phi(x, y) = a \frac{x^2}{2} + b \frac{y^2}{2} + \phi_0} $$

---

### Apartado 2: Condición de Incompresibilidad

La tasa de expansión volumétrica debe anularse:
$$ \nabla \cdot \vec{v} = \frac{\partial v_x}{\partial x} + \frac{\partial v_y}{\partial y} = a + b = 0 \implies \mathbf{b = -a} $$
Adoptando esta condición en adelante:
$$ \mathbf{\vec{v} = ax \, \vec{e}_x - ay \, \vec{e}_y} $$

---

### Apartado 3: Líneas de Corriente (*Streamlines*)

La ecuación diferencial de las líneas de corriente es:
$$ \frac{dx}{v_x} = \frac{dy}{v_y} \implies \frac{dx}{ax} = \frac{dy}{-ay} \implies \frac{dx}{x} = -\frac{dy}{y} $$
Integrando directamente:
$$ \ln x + \ln y = \text{cte} \implies \mathbf{x y = x_0 y_0 = \text{cte}} $$
Las líneas de corriente forman una familia de **hipérbolas equiláteras** que tienen como asíntotas los ejes coordenados $x=0$ e $y=0$. El origen $(0,0)$ es un punto de estancamiento de tipo silla (*saddle point*).

---

### Apartado 4: Trayectoria y Línea de Trayectoria (Partícula en $x_0 = 0, y_0 = 1$)

El sistema lagrangiano con condición inicial $x(0) = 0, y(0) = 1$ es:
$$ \frac{dx}{dt} = ax \implies x(t) = C_x e^{at} \implies x(0) = 0 \implies \mathbf{x(t) = 0} $$
$$ \frac{dy}{dt} = -ay \implies y(t) = C_y e^{-at} \implies y(0) = 1 \implies \mathbf{y(t) = e^{-at}} $$

* **Línea de trayectoria (*path line*):** El segmento vertical del eje $y$:
  $$ x = 0, \qquad 0 < y \le 1 $$
* **Tiempo para alcanzar el origen:**
  $$ y(t) = e^{-at} \to 0 \implies -at \to -\infty \implies \mathbf{t \to \infty} $$
  La partícula experimenta una desaceleración exponencial que le impide alcanzar el punto de estancamiento en un tiempo finito; requiere un **tiempo infinito** ($t = \infty$).

---

### Apartado 5: Aceleración de las Partículas en el Eje $y=0$

La aceleración material viene dada por la derivada sustancial:
$$ \vec{a} = \frac{D\vec{v}}{Dt} = \frac{\partial \vec{v}}{\partial t} + (\vec{v} \cdot \nabla)\vec{v} $$
Como el flujo es estacionario ($\partial \vec{v}/\partial t = 0$):
$$ a_x = v_x \frac{\partial v_x}{\partial x} + v_y \frac{\partial v_x}{\partial y} = (ax)(a) + (-ay)(0) = a^2 x $$
$$ a_y = v_x \frac{\partial v_y}{\partial x} + v_y \frac{\partial v_y}{\partial y} = (ax)(0) + (-ay)(-a) = a^2 y $$
$$ \vec{a}(x, y) = a^2 x \, \vec{e}_x + a^2 y \, \vec{e}_y $$
Evaluando a lo largo del eje $y = 0$:
$$ \mathbf{\left. \frac{D\vec{v}}{Dt} \right|_{y=0} = a^2 x \, \vec{e}_x} $$
La aceleración convectiva es puramente longitudinal y crece linealmente con la distancia al origen.

---

### Apartado 6: Función de Corriente ($\psi$)

Por definición de función de corriente para flujo plano incompresible:
$$ v_x = \frac{\partial \psi}{\partial y} = ax \implies \psi(x, y) = axy + f(x) $$
$$ v_y = -\frac{\partial \psi}{\partial x} = -ay - f'(x) = -ay \implies f'(x) = 0 \implies f(x) = \psi_0 $$
$$ \mathbf{\psi(x, y) = axy + \psi_0} $$
Las curvas $\psi = \text{cte}$ reproducen de forma inmediata las hipérbolas $xy = \text{cte}$.

---

### Apartado 7: Tensor de Velocidad de Deformación $\bar{\bar{T}}_d$

Calculamos primero el gradiente de velocidades:
$$ \nabla \vec{v} = \begin{bmatrix} \frac{\partial v_x}{\partial x} & \frac{\partial v_y}{\partial x} \\ \frac{\partial v_x}{\partial y} & \frac{\partial v_y}{\partial y} \end{bmatrix}^T = \begin{bmatrix} a & 0 \\ 0 & -a \end{bmatrix} $$
Como $\nabla \vec{v}$ ya es una matriz diagonal simétrica:
$$ \mathbf{\bar{\bar{T}}_d = \frac{1}{2}\left( \nabla \vec{v} + (\nabla \vec{v})^T \right) = \begin{bmatrix} a & 0 \\ 0 & -a \end{bmatrix}} $$
El tensor de velocidades de rotación es idénticamente nulo:
$$ \mathbf{\bar{\bar{T}}_r = \frac{1}{2}\left( \nabla \vec{v} - (\nabla \vec{v})^T \right) = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}} $$
El campo corresponde a un estado de **deformación pura sin rotación** (*pure strain*).

---

### Apartado 8: Deformación de un Elemento Cuadrado de Fluido de Lado $dl$

Consideremos los dos lados orientados según las direcciones canónicas:
$$ d\vec{l}_1 = dl (1, 0), \qquad d\vec{l}_2 = dl (0, 1) $$
Evolucionando en un tiempo infinitesimal $dt$:
$$ d\vec{l}_1(t+dt) = d\vec{l}_1 + d\vec{l}_1 \cdot \nabla \vec{v} \, dt = dl(1, 0) + dl(1, 0)\begin{bmatrix} a & 0 \\ 0 & -a \end{bmatrix}dt = \mathbf{dl(1 + a\,dt, 0)} $$
$$ d\vec{l}_2(t+dt) = d\vec{l}_2 + d\vec{l}_2 \cdot \nabla \vec{v} \, dt = dl(0, 1) + dl(0, 1)\begin{bmatrix} a & 0 \\ 0 & -a \end{bmatrix}dt = \mathbf{dl(0, 1 - a\,dt)} $$

#### Conclusiones Físicas:
1. **Sin rotación:** Los ángulos entre los lados se mantienen exactamente en $90^\circ$ (deformación angular $\dot{\gamma}_{xy} = 0$).
2. **Alargamiento axial en $x$:** Tasa de estiramiento longitudinal $\epsilon_{xx} = +a$.
3. **Contracción transversal en $y$:** Tasa de acortamiento longitudinal $\epsilon_{yy} = -a$.
4. **Conservación de área:** El área del elemento es:
   $$ dA(t+dt) = dl^2 (1 + a\,dt)(1 - a\,dt) = dl^2 (1 - a^2 dt^2) \approx dl^2 = dA(t) $$
   lo cual es consecuencia directa de la incompresibilidad $\nabla \cdot \vec{v} = 0$.
