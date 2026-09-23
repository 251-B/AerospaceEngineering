---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - flujo-tridimensional
  - potencial-velocidades
  - superficie-fluida
  - elipsoide-pulsante
dificultad: alta
fuente: "sources/01-fluid-mechanics/problemas/1.Kinematics/K8.pdf"
---

# ✏️ Problema K8: Flujo Tridimensional Pulsante y Deformación de Superficie Esférica

> **Origen:** Hoja de Problemas de Cinemática, UC3M (Prof. Antonio L. Sánchez & Javier Rodríguez-Rodríguez). Solución manuscrita oficial cotejada.

---

## 📋 Enunciado

The velocity potential of a three-dimensional flow field is given by:

$$ \phi = A \cos(\Omega t)\left(2x^2 - y^2 - z^2\right) $$

where $A$ and $\Omega$ are known constants.

1. Determine the velocity field, verifying that $\nabla \wedge \vec{v} = 0$ and $\nabla \cdot \vec{v} = 0$.
2. Compute the streamlines, trajectories and particle paths.
3. Obtain the fluid surface that at the initial instant is a sphere of radius $R$ centered at $(x, y, z) = (-R/2, 0, 0)$.

---

## 🎯 1. Planteamiento Físico e Hipótesis

* **Geometría:** Espacio tridimensional euclídeo $\mathbb{R}^3$ con simetría de revolución en torno al eje $x$ (nótese el factor $y^2 + z^2 = \varpi^2$).
* **Naturaleza del campo:** Flujo potencial oscilatorio no estacionario, periódico en el tiempo con pulsación $\Omega$.
* **Conservación:** Incompresible y exento de vorticidad.

---

## 🔍 2. Resolución Matemática Paso a Paso

### Apartado 1: Campo de Velocidades, Irrotacionalidad e Incompresibilidad

Calculando las derivadas parciales del potencial $\phi$:
$$ v_x = \frac{\partial \phi}{\partial x} = \mathbf{4 A \cos(\Omega t) \, x} $$
$$ v_y = \frac{\partial \phi}{\partial y} = \mathbf{-2 A \cos(\Omega t) \, y} $$
$$ v_z = \frac{\partial \phi}{\partial z} = \mathbf{-2 A \cos(\Omega t) \, z} $$

#### Verificación de la Vorticidad $\nabla \wedge \vec{v}$:
$$ \nabla \wedge \vec{v} = \begin{vmatrix} \vec{e}_x & \vec{e}_y & \vec{e}_z \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ v_x & v_y & v_z \end{vmatrix} = 2 A \cos(\Omega t) \begin{vmatrix} \vec{e}_x & \vec{e}_y & \vec{e}_z \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ 2x & -y & -z \end{vmatrix} = \mathbf{0} $$
El campo es estrictamente **irrotacional**, como exige la formulación potencial.

#### Verificación de la Tasa de Expansión $\nabla \cdot \vec{v}$:
$$ \nabla \cdot \vec{v} = \frac{\partial v_x}{\partial x} + \frac{\partial v_y}{\partial y} + \frac{\partial v_z}{\partial z} = A \cos(\Omega t) \left( 4 - 2 - 2 \right) = \mathbf{0} $$
El campo satisface la **ecuación de Laplace** ($\nabla^2 \phi = 0$) y representa un flujo **incompresible**.

---

### Apartado 2: Líneas de Corriente, Trayectorias y Líneas de Trayectoria

#### Líneas de Corriente (*Streamlines*):
Congelando el tiempo $t$:
$$ \frac{dx}{v_x} = \frac{dy}{v_y} = \frac{dz}{v_z} \implies \frac{dx}{4x} = -\frac{dy}{2y} = -\frac{dz}{2z} \implies \frac{dx}{2x} = -\frac{dy}{y} = -\frac{dz}{z} $$

Integrando dos pares independientes:
1. De $\frac{dx}{2x} = -\frac{dy}{y}$:
   $$ \frac{1}{2}\ln x + \ln y = \text{cte} \implies \ln(x y^2) = \text{cte} \implies \mathbf{x y^2 = x_0 y_0^2} $$
2. De $-\frac{dy}{y} = -\frac{dz}{z}$:
   $$ \ln y - \ln z = \text{cte} \implies \mathbf{\frac{y}{z} = \frac{y_0}{z_0}} $$

Las líneas de corriente corresponden a curvas tridimensionales generadas por la intersección de planos meridionales que pasan por el eje $x$ ($y/z = \text{cte}$) con cilindros hiperbólicos de orden superior ($x y^2 = \text{cte}$).

#### Trayectorias (*Trajectories*):
Para una partícula inicialmente en $(x_i, y_i, z_i)$ en $t=0$:
$$ \frac{dx}{dt} = 4 A \cos(\Omega t) x \implies \int_{x_i}^x \frac{dx'}{x'} = 4A \int_0^t \cos(\Omega t') dt' \implies \mathbf{\frac{x(t)}{x_i} = \exp\left[ \frac{4A}{\Omega}\sin(\Omega t) \right]} $$
$$ \frac{dy}{dt} = -2 A \cos(\Omega t) y \implies \int_{y_i}^y \frac{dy'}{y'} = -2A \int_0^t \cos(\Omega t') dt' \implies \mathbf{\frac{y(t)}{y_i} = \exp\left[ -\frac{2A}{\Omega}\sin(\Omega t) \right]} $$
$$ \frac{dz}{dt} = -2 A \cos(\Omega t) z \implies \int_{z_i}^z \frac{dz'}{z'} = -2A \int_0^t \cos(\Omega t') dt' \implies \mathbf{\frac{z(t)}{z_i} = \exp\left[ -\frac{2A}{\Omega}\sin(\Omega t) \right]} $$

#### Líneas de Trayectoria (*Path lines*):
Eliminando el tiempo de las relaciones exponenciales:
$$ \exp\left[ \frac{2A}{\Omega}\sin(\Omega t) \right] = \left(\frac{x}{x_i}\right)^{1/2} = \left(\frac{y}{y_i}\right)^{-1} = \left(\frac{z}{z_i}\right)^{-1} $$
$$ \implies \mathbf{x y^2 = x_i y_i^2, \qquad \frac{y}{z} = \frac{y_i}{z_i}} $$

> [!NOTE] Coincidencia Geométrica
> Al ser la dependencia temporal un factor multiplicativo común en las tres componentes espaciales de la velocidad, las direcciones del movimiento instantáneo no varían con el tiempo. Por tanto, **las líneas de trayectoria son idénticas a las líneas de corriente**.

---

### Apartado 3: Superficie Fluida Inicialmente Esférica

La superficie material en $t = 0$ es una esfera de radio $R$ centrada en $(-R/2, 0, 0)$:
$$ \left( x_i + \frac{R}{2} \right)^2 + y_i^2 + z_i^2 = R^2 $$

Para determinar la ecuación de la superficie en cualquier instante posterior $t$, invertimos las ecuaciones de las trayectorias para despejar las coordenadas iniciales (etiquetas de Lagrange) $(x_i, y_i, z_i)$ en función de las coordenadas de Euler $(x, y, z)$ y el tiempo $t$:
$$ x_i = x \exp\left[ -\frac{4A}{\Omega}\sin(\Omega t) \right] $$
$$ y_i = y \exp\left[ +\frac{2A}{\Omega}\sin(\Omega t) \right] $$
$$ z_i = z \exp\left[ +\frac{2A}{\Omega}\sin(\Omega t) \right] $$

Sustituyendo directamente en la ecuación de la esfera inicial:
$$ \mathbf{\left( x e^{-\frac{4A}{\Omega}\sin(\Omega t)} + \frac{R}{2} \right)^2 + \left( y e^{\frac{2A}{\Omega}\sin(\Omega t)} \right)^2 + \left( z e^{\frac{2A}{\Omega}\sin(\Omega t)} \right)^2 = R^2} $$

#### Interpretación Geométrica y Cinemática:
1. **Elipsoide de Revolución (Esferoide):** Para todo instante $t$, los coeficientes de $y^2$ y $z^2$ son iguales, por lo que la superficie se deforma manteniendo simetría de revolución respecto al eje $x$.
2. **Pulsación Periódica:**
   * Cuando $\sin(\Omega t) > 0$, el semieje longitudinal en $x$ se comprime por un factor $e^{-\frac{4A}{\Omega}\sin(\Omega t)}$ mientras que la sección transversal se expande por $e^{\frac{2A}{\Omega}\sin(\Omega t)}$.
   * El centro del elipsoide oscila a lo largo del eje $x$ en la posición $x_c(t) = -\frac{R}{2} e^{\frac{4A}{\Omega}\sin(\Omega t)}$.
3. **Conservación de Volumen:** El producto de los tres semiejes relativos es:
   $$ \lambda_x \lambda_y \lambda_z = e^{\frac{4A}{\Omega}\sin(\Omega t)} \cdot e^{-\frac{2A}{\Omega}\sin(\Omega t)} \cdot e^{-\frac{2A}{\Omega}\sin(\Omega t)} = e^0 = 1 $$
   El volumen encerrado por el elipsoide permanece constante e idéntico al de la esfera inicial ($\frac{4}{3}\pi R^3$).
