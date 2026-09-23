---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - flujo-polar
  - potencial-velocidades
  - funcion-corriente
  - linea-fluida
  - aceleracion-polar
dificultad: alta
fuente: "sources/01-fluid-mechanics/problemas/1.Kinematics/K9.pdf"
---

# ✏️ Problema K9: Flujo Polar Oscilante y Deformación de una Línea Fluida

> **Origen:** Hoja de Problemas de Cinemática, UC3M (Prof. Antonio L. Sánchez & Javier Rodríguez-Rodríguez). Solución manuscrita oficial cotejada.

---

## 📋 Enunciado

For the planar velocity field

$$ v_r = -A \sin(\Omega t) \frac{\sin\theta}{r^2}, \qquad v_\theta = A \sin(\Omega t) \frac{\cos\theta}{r^2} $$

where $A$ and $\Omega$ are known constants,

1. Determine the vorticity.
2. Compute the expansion rate.
3. Comment on the existence of velocity potential and stream function and, if they do exist, compute them.
4. Find the acceleration for points along the line $\theta = 0$.
5. Obtain the trajectories & streamlines.
6. Determine the fluid line that at $t = 0$ is given by $\theta = 0$ and $0 < r < \infty$.

---

## 🎯 1. Planteamiento Físico e Hipótesis

* **Geometría:** Flujo plano bidimensional en coordenadas polares $(r, \theta)$.
* **Naturaleza del campo:** Dipolo plano ortogonal oscilatorio (orientado según el eje $y$, con decaimiento radial $\sim 1/r^2$).
* **Régimen:** No estacionario, sinusoidal en el tiempo con frecuencia angular $\Omega$, partiendo del reposo en $t = 0$.

---

## 🔍 2. Resolución Matemática Paso a Paso

### Apartado 1: Campo de Vorticidad $\vec{\omega}$

En coordenadas polares cilíndricas:
$$ \vec{\omega} = \nabla \wedge \vec{v} = \omega_z \vec{e}_z = \frac{1}{r}\left[ \frac{\partial(r v_\theta)}{\partial r} - \frac{\partial v_r}{\partial \theta} \right] \vec{e}_z $$
Calculando cada término:
$$ r v_\theta = A \sin(\Omega t) \frac{\cos\theta}{r} \implies \frac{\partial(r v_\theta)}{\partial r} = -A \sin(\Omega t) \frac{\cos\theta}{r^2} $$
$$ \frac{\partial v_r}{\partial \theta} = \frac{\partial}{\partial \theta}\left[ -A \sin(\Omega t) \frac{\sin\theta}{r^2} \right] = -A \sin(\Omega t) \frac{\cos\theta}{r^2} $$
Restando ambas derivadas:
$$ \omega_z = \frac{1}{r}\left[ -A \sin(\Omega t) \frac{\cos\theta}{r^2} - \left(-A \sin(\Omega t) \frac{\cos\theta}{r^2}\right) \right] = \mathbf{0} $$
El flujo es estrictamente **irrotacional** en todo el plano ($r > 0$).

---

### Apartado 2: Tasa de Expansión Volumétrica $\nabla \cdot \vec{v}$

$$ \nabla \cdot \vec{v} = \frac{1}{r}\left[ \frac{\partial(r v_r)}{\partial r} + \frac{\partial v_\theta}{\partial \theta} \right] $$
$$ r v_r = -A \sin(\Omega t) \frac{\sin\theta}{r} \implies \frac{\partial(r v_r)}{\partial r} = +A \sin(\Omega t) \frac{\sin\theta}{r^2} $$
$$ \frac{\partial v_\theta}{\partial \theta} = \frac{\partial}{\partial \theta}\left[ A \sin(\Omega t) \frac{\cos\theta}{r^2} \right] = -A \sin(\Omega t) \frac{\sin\theta}{r^2} $$
Sumando:
$$ \nabla \cdot \vec{v} = \frac{1}{r}\left[ A \sin(\Omega t) \frac{\sin\theta}{r^2} - A \sin(\Omega t) \frac{\sin\theta}{r^2} \right] = \mathbf{0} $$
El fluido es estrictamente **incompresible**.

---

### Apartado 3: Potencial de Velocidades ($\phi$) y Función de Corriente ($\psi$)

#### 1. Potencial de Velocidades $\phi(r, \theta, t)$:
Existe debido a que $\nabla \wedge \vec{v} = 0$:
$$ v_r = \frac{\partial \phi}{\partial r} = -A \sin(\Omega t) \frac{\sin\theta}{r^2} \implies \phi(r, \theta, t) = A \sin(\Omega t) \frac{\sin\theta}{r} + f(\theta, t) $$
Derivando respecto a $\theta$:
$$ v_\theta = \frac{1}{r} \frac{\partial \phi}{\partial \theta} = A \sin(\Omega t) \frac{\cos\theta}{r^2} + \frac{1}{r} \frac{\partial f}{\partial \theta} $$
Comparando con la expresión dada de $v_\theta$:
$$ \frac{\partial f}{\partial \theta} = 0 \implies f = \phi_0(t) $$
$$ \mathbf{\phi(r, \theta, t) = A \sin(\Omega t) \frac{\sin\theta}{r} + \phi_0} $$

#### 2. Función de Corriente $\psi(r, \theta, t)$:
Existe debido a que $\nabla \cdot \vec{v} = 0$:
$$ r v_r = \frac{\partial \psi}{\partial \theta} = -A \sin(\Omega t) \frac{\sin\theta}{r} \implies \psi(r, \theta, t) = A \sin(\Omega t) \frac{\cos\theta}{r} + g(r, t) $$
Derivando respecto a $r$:
$$ v_\theta = -\frac{\partial \psi}{\partial r} = A \sin(\Omega t) \frac{\cos\theta}{r^2} - \frac{\partial g}{\partial r} = A \sin(\Omega t) \frac{\cos\theta}{r^2} \implies \frac{\partial g}{\partial r} = 0 \implies g = \psi_0(t) $$
$$ \mathbf{\psi(r, \theta, t) = A \sin(\Omega t) \frac{\cos\theta}{r} + \psi_0} $$

---

### Apartado 4: Aceleración de Puntos a lo Largo de la Línea $\theta = 0$

Empleando la formulación con la identidad de Lamb-Gromeka ($\nabla \wedge \vec{v} = 0$):
$$ \vec{a} = \frac{\partial \vec{v}}{\partial t} + \nabla\left(\frac{v^2}{2}\right) $$
Calculando la energía cinética específica:
$$ \frac{v^2}{2} = \frac{v_r^2 + v_\theta^2}{2} = \frac{A^2 \sin^2(\Omega t)(\sin^2\theta + \cos^2\theta)}{2 r^4} = \frac{A^2 \sin^2(\Omega t)}{2 r^4} $$
Nuevamente, $v^2/2$ es independiente de $\theta$, luego:
$$ \nabla\left(\frac{v^2}{2}\right) = \frac{\partial}{\partial r}\left(\frac{v^2}{2}\right)\vec{e}_r = -\frac{2 A^2 \sin^2(\Omega t)}{r^5} \vec{e}_r $$

Componentes de la aceleración local:
$$ \frac{\partial v_r}{\partial t} = -A \Omega \cos(\Omega t) \frac{\sin\theta}{r^2} $$
$$ \frac{\partial v_\theta}{\partial t} = +A \Omega \cos(\Omega t) \frac{\cos\theta}{r^2} $$

Aceleración total en el plano:
$$ a_r = -A \Omega \cos(\Omega t) \frac{\sin\theta}{r^2} - \frac{2 A^2 \sin^2(\Omega t)}{r^5} $$
$$ a_\theta = +A \Omega \cos(\Omega t) \frac{\cos\theta}{r^2} $$

Evaluando a lo largo del semieje polar $\theta = 0$ ($\sin 0 = 0, \cos 0 = 1$):
$$ \mathbf{\left. a_r \right|_{\theta = 0} = -\frac{2 A^2 \sin^2(\Omega t)}{r^5}} $$
$$ \mathbf{\left. a_\theta \right|_{\theta = 0} = \frac{A \Omega \cos(\Omega t)}{r^2}} $$

---

### Apartado 5: Líneas de Corriente y Trayectorias

#### Líneas de Corriente:
$$ \frac{dr}{v_r} = \frac{r d\theta}{v_\theta} \implies \frac{dr}{-\sin\theta} = \frac{r d\theta}{\cos\theta} \implies \frac{dr}{r} = -\frac{\sin\theta}{\cos\theta} d\theta = \frac{d(\cos\theta)}{\cos\theta} $$
Integrando entre $(r_0, \theta_0)$ y $(r, \theta)$:
$$ \ln\left(\frac{r}{r_0}\right) = \ln\left(\frac{\cos\theta}{\cos\theta_0}\right) \implies \mathbf{r = r_0 \frac{\cos\theta}{\cos\theta_0}} $$
En cartesianas: $r = C \cos\theta \implies r^2 = C r \cos\theta \implies x^2 + y^2 = C x \implies (x - C/2)^2 + y^2 = (C/2)^2$.
Son **circunferencias tangentes al eje $y$ en el origen**.

#### Trayectorias y Líneas de Trayectoria:
Dividiendo $dr/dt$ entre $r d\theta/dt$ se obtiene idéntica relación geométrica:
$$ \mathbf{\text{Líneas de Trayectoria} \equiv \text{Líneas de Corriente}: \quad r = r_0 \frac{\cos\theta}{\cos\theta_0}} $$

Evolución temporal de $\theta(t)$:
$$ \frac{d\theta}{dt} = \frac{v_\theta}{r} = \frac{A \sin(\Omega t)\cos\theta}{r^3} = \frac{A \sin(\Omega t)\cos\theta}{\left(r_0 \frac{\cos\theta}{\cos\theta_0}\right)^3} = \frac{A \cos^3\theta_0}{r_0^3} \frac{\sin(\Omega t)}{\cos^2\theta} $$
Separando variables e integrando usando $\cos^2\theta = \frac{1+\cos 2\theta}{2}$:
$$ \int_{\theta_0}^\theta \cos^2\theta' \, d\theta' = \frac{A \cos^3\theta_0}{r_0^3} \int_0^t \sin(\Omega t') dt' $$
$$ \mathbf{\frac{\theta - \theta_0}{2} + \frac{\sin(2\theta) - \sin(2\theta_0)}{4} = \frac{A \cos^3\theta_0}{r_0^3 \Omega} \left[ 1 - \cos(\Omega t) \right]} $$

---

### Apartado 6: Deformación de la Línea Fluida Inicial $\theta = 0, 0 < r < \infty$

En el instante inicial $t = 0$, la línea de partículas está situada sobre el eje positivo de abscisas:
$$ \theta_0 = 0, \qquad r_0 = \lambda > 0 \quad (\lambda \in (0, \infty)) $$
Para estas partículas, $\cos\theta_0 = \cos(0) = 1$ y $\sin(2\theta_0) = 0$.

De la ecuación de su línea de trayectoria:
$$ r = \lambda \cos\theta \implies \lambda = \frac{r}{\cos\theta} $$
De la evolución temporal:
$$ \frac{\theta}{2} + \frac{\sin(2\theta)}{4} = \frac{A}{\lambda^3 \Omega} \left[ 1 - \cos(\Omega t) \right] $$
Eliminando el parámetro lagrangiano $\lambda$ sustituyendo $\lambda = \frac{r}{\cos\theta}$:
$$ \frac{1}{2}\left( \theta + \frac{\sin 2\theta}{2} \right) = \frac{A \cos^3\theta}{r^3 \Omega} \left[ 1 - \cos(\Omega t) \right] $$
Multiplicando por $\frac{r^3}{\cos^3\theta}$:
$$ \mathbf{\frac{r^3}{2\cos^3\theta}\left(\theta + \frac{\sin 2\theta}{2}\right) = \frac{A}{\Omega}\left[1 - \cos(\Omega t)\right]} $$
Despejando explícitamente $r(\theta, t)$:
$$ \mathbf{r(\theta, t) = \left[ \frac{2 A \left[1 - \cos(\Omega t)\right] \cos^3\theta}{\Omega \left(\theta + \frac{\sin 2\theta}{2}\right)} \right]^{1/3}} $$
La línea fluida, inicialmente recta horizontal, se abomba progresivamente curvándose alrededor del origen con pulsación periódica.
