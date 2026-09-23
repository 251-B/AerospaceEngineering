---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - pared-porosa
  - stokes
dificultad: alta
fuente: "sources/01-fluid-mechanics/problemas/1.Kinematics/K1.pdf"
---

# ✏️ Problema K1: Flujo sobre Pared Porosa Oscilante con Succión/Soplado

> **Origen:** Hoja de Problemas de Cinemática, UC3M (Prof. Antonio L. Sánchez & Javier Rodríguez-Rodríguez). Solución manuscrita oficial cotejada.

---

## 📋 Enunciado

A fluid is blown with velocity $V$ through a horizontal porous wall that is oscillating in its plane with velocity $U \cos(\Omega t)$. The resulting fluid velocity for $0 < y < \infty$ is given by (approximately):

$$ v_x = U e^{-y/\delta} \cos\left(\Omega t - \frac{y}{\delta}\right), \qquad v_y = V $$

where the characteristic thickness $\delta = (2\nu/\Omega)^{1/2}$ depends on the kinematic viscosity of the fluid $\nu$.

1. Determine the trajectory and path of a fluid particle initially located at $x=0$ and $y=0$.
2. Obtain the streamline that intersects the point $x=0$ and $y=0$.
3. Compute the vorticity $\nabla \wedge \vec{v}$. If $\nabla \wedge \vec{v} = 0$, obtain also the velocity potential.
4. Calculate the rate of expansion $\nabla \cdot \vec{v}$. If $\nabla \cdot \vec{v} = 0$, obtain also the stream function.
5. Equation of the fluid line formed by the fluid particles initially located along the vertical axis $x=0$.
6. Determine the volume flux crossing the plane $x=0$ as a function of time $Q(t)$ along with its average value $Q_a = \frac{\Omega}{2\pi}\int_t^{t+2\pi/\Omega} Q(t) dt$.
7. Obtain the volume flux leaving the sphere of radius $R$ centered at $x=0$ and $y=2R$.
8. Compute the circulation around a square of side $L$ whose base lies parallel to the wall at a distance $y=L/2$. Redo the computation making use of Stokes theorem.

---

## 🎯 1. Planteamiento Físico e Hipótesis

* **Geometría:** Semi-espacio bidimensional $y > 0$. Pared porosa en $y = 0$.
* **Campo de velocidades:**
  $$ \vec{v}(x, y, t) = U e^{-y/\delta}\cos\left(\Omega t - \frac{y}{\delta}\right) \vec{e}_x + V \vec{e}_y $$
  El flujo es no estacionario y bidimensional en el plano $x-y$, independiente de la coordenada $x$.
* **Espesor viscoso $\delta$:** Capa límite oscilatoria de Stokes acoplada a la convección transversal de soplado $V$.

---

## 🔍 2. Resolución Matemática Paso a Paso

### Apartado 1: Trayectoria y Línea de Trayectoria (Partícula en $x_0 = 0, y_0 = 0$)

La trayectoria sigue el sistema de Cauchy:
$$ \frac{dy}{dt} = v_y = V \implies y(t) = V t + y_0 $$
Dado que $y_0 = 0$ en $t = 0$:
$$ y(t) = V t \implies t = \frac{y}{V} $$

Para la coordenada horizontal:
$$ \frac{dx}{dt} = v_x = U e^{-y/\delta} \cos\left(\Omega t - \frac{y}{\delta}\right) = U e^{-\frac{Vt}{\delta}} \cos\left[\left(\Omega - \frac{V}{\delta}\right)t\right] $$

Integrando entre $0$ y $t$:
$$ x(t) - x_0 = \int_0^t U e^{-\frac{Vt'}{\delta}} \cos\left[\left(\Omega - \frac{V}{\delta}\right)t'\right] dt' $$

Empleando la integral exponencial-trigonométrica estándar $\int e^{at}\cos(bt)dt = \frac{e^{at}}{a^2+b^2}[a\cos(bt) + b\sin(bt)]$, con:
$$ a = -\frac{V}{\delta}, \qquad b = \Omega - \frac{V}{\delta} $$

$$ x(t) = \frac{U e^{-\frac{Vt}{\delta}}}{\left(\frac{V}{\delta}\right)^2 + \left(\Omega - \frac{V}{\delta}\right)^2} \left[ -\frac{V}{\delta}\cos\left(\left(\Omega - \frac{V}{\delta}\right)t\right) + \left(\Omega - \frac{V}{\delta}\right)\sin\left(\left(\Omega - \frac{V}{\delta}\right)t\right) \right] + \frac{U \frac{V}{\delta}}{\left(\frac{V}{\delta}\right)^2 + \left(\Omega - \frac{V}{\delta}\right)^2} $$

**Línea de trayectoria (*path line*):** Sustituyendo $t = y/V$:
$$ x(y) = \frac{U e^{-y/\delta}}{\left(\frac{V}{\delta}\right)^2 + \left(\Omega - \frac{V}{\delta}\right)^2} \left[ -\frac{V}{\delta}\cos\left(\left(\frac{\Omega}{V} - \frac{1}{\delta}\right)y\right) + \left(\Omega - \frac{V}{\delta}\right)\sin\left(\left(\frac{\Omega}{V} - \frac{1}{\delta}\right)y\right) \right] + \frac{\frac{U V}{\delta}}{\left(\frac{V}{\delta}\right)^2 + \left(\Omega - \frac{V}{\delta}\right)^2} $$

---

### Apartado 2: Línea de Corriente por $(x=0, y=0)$ en el Instante $t$

Congelando el tiempo $t$:
$$ \frac{dx}{v_x} = \frac{dy}{v_y} \implies \frac{dx}{U e^{-y/\delta}\cos(\Omega t - y/\delta)} = \frac{dy}{V} $$
$$ x - x_0 = \frac{U}{V} \int_0^y e^{-y'/\delta} \cos\left(\Omega t - \frac{y'}{\delta}\right) dy' $$

Integrando respecto a $y'$ con $a = -1/\delta$ y $b = -1/\delta$, donde $a^2 + b^2 = 2/\delta^2$:
$$ \int e^{-y'/\delta} \cos\left(\Omega t - \frac{y'}{\delta}\right) dy' = \frac{e^{-y'/\delta}}{2/\delta^2}\left[ -\frac{1}{\delta}\cos\left(\Omega t - \frac{y'}{\delta}\right) - \frac{1}{\delta}\sin\left(\Omega t - \frac{y'}{\delta}\right) \right] = -\frac{\delta}{2} e^{-y'/\delta}\left[\cos\left(\Omega t - \frac{y'}{\delta}\right) + \sin\left(\Omega t - \frac{y'}{\delta}\right)\right] $$

Evaluando entre $0$ e $y$ para $x_0 = 0$:
$$ \mathbf{x(y, t) = -\frac{U\delta}{2V} e^{-y/\delta}\left[\cos\left(\Omega t - \frac{y}{\delta}\right) + \sin\left(\Omega t - \frac{y}{\delta}\right)\right] + \frac{U\delta}{2V}\left[\cos(\Omega t) + \sin(\Omega t)\right]} $$

---

### Apartado 3: Vorticidad y Potencial de Velocidades

$$ \vec{\omega} = \nabla \wedge \vec{v} = \left(\frac{\partial v_y}{\partial x} - \frac{\partial v_x}{\partial y}\right)\vec{e}_z $$
Como $v_y = V = \text{cte} \implies \frac{\partial v_y}{\partial x} = 0$.
Derivando $v_x$ respecto a $y$:
$$ \frac{\partial v_x}{\partial y} = U \frac{\partial}{\partial y}\left[ e^{-y/\delta}\cos\left(\Omega t - \frac{y}{\delta}\right) \right] = -\frac{U}{\delta} e^{-y/\delta}\cos\left(\Omega t - \frac{y}{\delta}\right) + \frac{U}{\delta} e^{-y/\delta}\sin\left(\Omega t - \frac{y}{\delta}\right) $$
$$ \mathbf{\vec{\omega} = \frac{U}{\delta} e^{-y/\delta}\left[\cos\left(\Omega t - \frac{y}{\delta}\right) - \sin\left(\Omega t - \frac{y}{\delta}\right)\right] \vec{e}_z \neq 0} $$
**Conclusión:** El flujo es **rotacional** ($\vec{\omega} \neq 0$), por lo que **no existe función potencial de velocidades $\phi$**.

---

### Apartado 4: Tasa de Expansión y Función de Corriente ($\psi$)

$$ \nabla \cdot \vec{v} = \frac{\partial v_x}{\partial x} + \frac{\partial v_y}{\partial y} = 0 + 0 = \mathbf{0} $$
El flujo es estrictamente **incompresible**, por lo que existe función de corriente $\psi(x, y, t)$:
$$ v_x = \frac{\partial \psi}{\partial y}, \qquad v_y = -\frac{\partial \psi}{\partial x} = V \implies \psi = -Vx + f(y, t) $$
Derivando respecto a $y$:
$$ \frac{\partial \psi}{\partial y} = f'(y, t) = v_x = U e^{-y/\delta}\cos\left(\Omega t - \frac{y}{\delta}\right) $$
Integrando respecto a $y$:
$$ \mathbf{\psi(x, y, t) = -Vx - \frac{U\delta}{2} e^{-y/\delta}\left[\cos\left(\Omega t - \frac{y}{\delta}\right) + \sin\left(\Omega t - \frac{y}{\delta}\right)\right] + \psi_0(t)} $$

---

### Apartado 5: Línea Fluida Inicialmente en el Eje $x=0$ ($y_0 = \lambda, x_0 = 0$)

Para cada partícula, $y(t) = Vt + \lambda \implies \lambda = y - Vt$.
Sustituyendo $\lambda$ en la solución de la trayectoria con condición inicial $x_0 = 0, y_0 = \lambda$:
$$ x(y, t) = \frac{-U e^{-y/\delta}}{\left(\frac{V}{\delta}\right)^2 + \left(\Omega - \frac{V}{\delta}\right)^2} \left[ \frac{V}{\delta}\cos\left[\left(\Omega - \frac{V}{\delta}\right)t - \frac{y-Vt}{\delta}\right] + \left(\Omega - \frac{V}{\delta}\right)\sin\left[\left(\Omega - \frac{V}{\delta}\right)t - \frac{y-Vt}{\delta}\right] \right] + \frac{U e^{-\frac{y-Vt}{\delta}}}{\left(\frac{V}{\delta}\right)^2 + \left(\Omega - \frac{V}{\delta}\right)^2} \left[ \frac{V}{\delta}\cos\left(\frac{y-Vt}{\delta}\right) + \left(\Omega - \frac{V}{\delta}\right)\sin\left(\frac{y-Vt}{\delta}\right) \right] $$

---

### Apartado 6: Flujo de Volumen a través del Plano $x=0$

$$ Q(t) = \int_0^\infty v_x(0, y, t) \, dy = \int_0^\infty U e^{-y/\delta}\cos\left(\Omega t - \frac{y}{\delta}\right) dy = \mathbf{\frac{U\delta}{2}\left[\cos(\Omega t) + \sin(\Omega t)\right]} $$
Valor medio temporal en un período de oscilación $T = 2\pi/\Omega$:
$$ Q_a = \frac{\Omega}{2\pi}\int_t^{t+2\pi/\Omega} Q(t') dt' = \mathbf{0} $$

---

### Apartado 7: Caudal Saliendo de la Esfera de Radio $R$ centrada en $(0, 2R)$

Aplicando el Teorema de Gauss sobre la superficie esférica cerrada $\Sigma$:
$$ \oint_\Sigma \vec{v} \cdot \vec{n} \, d\sigma = \int_{V_{\text{esfera}}} (\nabla \cdot \vec{v}) \, dV = \int_{V_{\text{esfera}}} 0 \, dV = \mathbf{0} $$

---

### Apartado 8: Circulación sobre Cuadrado de Lado $L$ y Base en $y = L/2$

El cuadrado tiene vértices en $(x_1, L/2)$, $(x_1+L, L/2)$, $(x_1+L, 3L/2)$, $(x_1, 3L/2)$.
* En los lados verticales ($x = x_1$ y $x = x_1+L$), $v_y = V$ es idéntico, por lo que sus integrales se cancelan: $\int V dy - \int V dy = 0$.
* En los lados horizontales:
$$ \Gamma = \int_{x_1}^{x_1+L} v_x\left(y = \frac{L}{2}\right) dx - \int_{x_1}^{x_1+L} v_x\left(y = \frac{3L}{2}\right) dx $$
$$ \mathbf{\Gamma = U L \left[ e^{-\frac{L}{2\delta}}\cos\left(\Omega t - \frac{L}{2\delta}\right) - e^{-\frac{3L}{2\delta}}\cos\left(\Omega t - \frac{3L}{2\delta}\right) \right]} $$

**Verificación por Teorema de Stokes:**
$$ \Gamma = \int_{L/2}^{3L/2}\int_{x_1}^{x_1+L} \omega_z \, dx dy = L \int_{L/2}^{3L/2} \left(-\frac{\partial v_x}{\partial y}\right) dy = -L \left[ v_x\left(\frac{3L}{2}\right) - v_x\left(\frac{L}{2}\right) \right] $$
que coincide exactamente con el resultado obtenido por la integral de línea directa.
