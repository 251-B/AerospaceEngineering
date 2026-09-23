---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - dipolo
  - flujo-potencial
  - aceleracion-material
  - vorticidad
dificultad: alta
fuente: "sources/01-fluid-mechanics/problemas/1.Kinematics/K5.pdf"
---

# ✏️ Problema K5: Dipolo Plano Pulsante / Oscilante

> **Origen:** Hoja de Problemas de Cinemática, UC3M (Prof. Antonio L. Sánchez & Javier Rodríguez-Rodríguez). Solución manuscrita oficial cotejada.

---

## 📋 Enunciado

For the planar fluid motion deriving from the velocity potential

$$ \phi = M \cos(\Omega t) \frac{\cos\theta}{r} $$

obtain:

1. Radial and azimuthal velocity components.
2. Expansion rate $\nabla \cdot \vec{v}$.
3. Vorticity $\nabla \wedge \vec{v}$.
4. Acceleration of the fluid particle initially located at $r = 1$ and $\theta = \pi/2$.
5. Initial value of the circulation around a circle of radius $R = 1/2$ centered at $(r = 1, \theta = \pi/2)$.
6. Streamlines.
7. Trajectories and particle paths.

---

## 🎯 1. Planteamiento Físico e Hipótesis

* **Geometría y simetría:** Flujo plano bidimensional en coordenadas polares $(r, \theta)$.
* **Singularidad:** Dipolo bidimensional en el origen con eje orientado a lo largo del eje polar ($\theta = 0$) e intensidad oscilatoria $M(t) = M \cos(\Omega t)$.
* **Naturaleza:** Flujo no estacionario, periódico en el tiempo con frecuencia angular $\Omega$.

---

## 🔍 2. Resolución Matemática Paso a Paso

### Apartado 1: Componentes Radial y Acimutal de la Velocidad

A partir del gradiente del potencial en coordenadas polares:
$$ v_r = \frac{\partial \phi}{\partial r} = \frac{\partial}{\partial r}\left[ M \cos(\Omega t) \frac{\cos\theta}{r} \right] = \mathbf{-\frac{M \cos(\Omega t) \cos\theta}{r^2}} $$
$$ v_\theta = \frac{1}{r} \frac{\partial \phi}{\partial \theta} = \frac{1}{r} \frac{\partial}{\partial \theta}\left[ M \cos(\Omega t) \frac{\cos\theta}{r} \right] = \mathbf{-\frac{M \cos(\Omega t) \sin\theta}{r^2}} $$

---

### Apartado 2: Tasa de Expansión Volumétrica $\nabla \cdot \vec{v}$

Aplicando la divergencia en coordenadas cilíndricas/polares:
$$ \nabla \cdot \vec{v} = \frac{1}{r}\left[ \frac{\partial(r v_r)}{\partial r} + \frac{\partial v_\theta}{\partial \theta} \right] $$
Calculando cada término por separado:
$$ r v_r = -\frac{M \cos(\Omega t) \cos\theta}{r} \implies \frac{\partial(r v_r)}{\partial r} = +\frac{M \cos(\Omega t) \cos\theta}{r^2} $$
$$ \frac{\partial v_\theta}{\partial \theta} = -\frac{\partial}{\partial \theta}\left[ \frac{M \cos(\Omega t) \sin\theta}{r^2} \right] = -\frac{M \cos(\Omega t) \cos\theta}{r^2} $$
Sumando ambos términos:
$$ \nabla \cdot \vec{v} = \frac{1}{r}\left[ \frac{M \cos(\Omega t) \cos\theta}{r^2} - \frac{M \cos(\Omega t) \cos\theta}{r^2} \right] = \mathbf{0} $$
El flujo es estrictamente **incompresible** en todo punto fuera del origen.

---

### Apartado 3: Campo de Vorticidad $\nabla \wedge \vec{v}$

El rotacional en coordenadas polares es perpendicular al plano:
$$ \vec{\omega} = \nabla \wedge \vec{v} = \omega_z \vec{e}_z = \frac{1}{r}\left[ \frac{\partial(r v_\theta)}{\partial r} - \frac{\partial v_r}{\partial \theta} \right] \vec{e}_z $$
$$ r v_\theta = -\frac{M \cos(\Omega t) \sin\theta}{r} \implies \frac{\partial(r v_\theta)}{\partial r} = +\frac{M \cos(\Omega t) \sin\theta}{r^2} $$
$$ \frac{\partial v_r}{\partial \theta} = -\frac{\partial}{\partial \theta}\left[ \frac{M \cos(\Omega t) \cos\theta}{r^2} \right] = +\frac{M \cos(\Omega t) \sin\theta}{r^2} $$
Restando:
$$ \omega_z = \frac{1}{r}\left[ \frac{M \cos(\Omega t) \sin\theta}{r^2} - \frac{M \cos(\Omega t) \sin\theta}{r^2} \right] = \mathbf{0} $$
El flujo es estrictamente **irrotacional** ($\vec{\omega} = 0$), como garantiza la existencia de un potencial monovaluado.

---

### Apartado 4: Aceleración de la Partícula Fluida en $(r = 1, \theta = \pi/2)$

Empleamos la expresión general de la aceleración material mediante la identidad de Lamb-Gromeka:
$$ \vec{a} = \frac{D\vec{v}}{Dt} = \frac{\partial \vec{v}}{\partial t} + \nabla\left(\frac{v^2}{2}\right) - \vec{v} \wedge (\nabla \wedge \vec{v}) $$
Como el flujo es irrotacional ($\nabla \wedge \vec{v} = 0$):
$$ \frac{D\vec{v}}{Dt} = \frac{\partial \vec{v}}{\partial t} + \nabla\left(\frac{v^2}{2}\right) $$

#### Cálculo de la Energía Cinética Específica $v^2/2$:
$$ v^2 = v_r^2 + v_\theta^2 = \frac{M^2 \cos^2(\Omega t)}{r^4}(\cos^2\theta + \sin^2\theta) = \frac{M^2 \cos^2(\Omega t)}{r^4} $$
$$ \frac{v^2}{2} = \frac{M^2 \cos^2(\Omega t)}{2 r^4} $$
Nótese que $v^2/2$ **no depende de $\theta$**, lo que simplifica enormemente su gradiente:
$$ \nabla\left(\frac{v^2}{2}\right) = \frac{\partial}{\partial r}\left(\frac{v^2}{2}\right)\vec{e}_r + \frac{1}{r}\frac{\partial}{\partial \theta}\left(\frac{v^2}{2}\right)\vec{e}_\theta = -\frac{2 M^2 \cos^2(\Omega t)}{r^5} \vec{e}_r + 0 \vec{e}_\theta $$

#### Derivada Temporal Local $\partial \vec{v}/\partial t$:
$$ \frac{\partial v_r}{\partial t} = +\frac{M \Omega \sin(\Omega t)\cos\theta}{r^2} $$
$$ \frac{\partial v_\theta}{\partial t} = +\frac{M \Omega \sin(\Omega t)\sin\theta}{r^2} $$

#### Vector Aceleración Total:
$$ \vec{a}(r, \theta, t) = \left[ \frac{M \Omega \sin(\Omega t)\cos\theta}{r^2} - \frac{2 M^2 \cos^2(\Omega t)}{r^5} \right] \vec{e}_r + \left[ \frac{M \Omega \sin(\Omega t)\sin\theta}{r^2} \right] \vec{e}_\theta $$

Evaluando en el punto solicitado $(r = 1, \theta = \pi/2)$, donde $\cos(\pi/2) = 0$ y $\sin(\pi/2) = 1$:
$$ \mathbf{\vec{a}\left(1, \frac{\pi}{2}, t\right) = -2 M^2 \cos^2(\Omega t) \, \vec{e}_r + M \Omega \sin(\Omega t) \, \vec{e}_\theta} $$

---

### Apartado 5: Circulación Inicial Alrededor de la Circunferencia

Se pide la circulación $\Gamma = \oint \vec{v} \cdot d\vec{l}$ en $t = 0$ sobre un círculo de radio $R = 1/2$ con centro en $(r = 1, \theta = \pi/2)$.
* La distancia del centro del círculo al origen es $d = 1$.
* El radio del contorno es $R = 1/2$.
* Como $d - R = 1 - 1/2 = 1/2 > 0$, el círculo **no encierra el origen de coordenadas** (la singularidad dipolar).
* En todo el interior del círculo, el flujo es regular e irrotacional ($\vec{\omega} = 0$).

Aplicando el teorema de Stokes:
$$ \mathbf{\Gamma = \iint_S \vec{\omega} \cdot \vec{e}_z \, d\sigma = 0} $$

---

### Apartado 6: Líneas de Corriente (*Streamlines*)

Congelando el tiempo $t$:
$$ \frac{dr}{v_r} = \frac{r d\theta}{v_\theta} \implies \frac{dr}{-\frac{M\cos(\Omega t)\cos\theta}{r^2}} = \frac{r d\theta}{-\frac{M\cos(\Omega t)\sin\theta}{r^2}} $$
Simplificando los factores temporales y radiales:
$$ \frac{dr}{\cos\theta} = \frac{r d\theta}{\sin\theta} \implies \frac{dr}{r} = \frac{\cos\theta}{\sin\theta} d\theta = \frac{d(\sin\theta)}{\sin\theta} $$
Integrando entre $(r_0, \theta_0)$ y $(r, \theta)$:
$$ \ln\left(\frac{r}{r_0}\right) = \ln\left(\frac{\sin\theta}{\sin\theta_0}\right) \implies \mathbf{r = r_0 \frac{\sin\theta}{\sin\theta_0}} $$
Reescribiendo como $r = C \sin\theta \implies r^2 = C r \sin\theta \implies x^2 + y^2 = C y \implies x^2 + (y - C/2)^2 = (C/2)^2$.
Las líneas de corriente forman una familia de **circunferencias tangentes al eje $x$ en el origen**.

---

### Apartado 7: Trayectorias y Líneas de Trayectoria

El sistema lagrangiano es:
$$ \frac{dr}{dt} = -\frac{M\cos(\Omega t)\cos\theta}{r^2} $$
$$ r \frac{d\theta}{dt} = -\frac{M\cos(\Omega t)\sin\theta}{r^2} $$
Dividiendo ambas ecuaciones para eliminar el tiempo:
$$ \frac{dr}{r d\theta} = \frac{\cos\theta}{\sin\theta} \implies \mathbf{r = r_0 \frac{\sin\theta}{\sin\theta_0}} $$

> [!IMPORTANT] Coincidencia Geométrica
> Aunque el flujo es no estacionario, la dirección del vector velocidad en cada punto $(\vec{e}_v = -\cos\theta \vec{e}_r - \sin\theta \vec{e}_\theta)$ es fija en el tiempo, variando únicamente su amplitud e invirtiendo el sentido cada semiperiodo. Por tanto:
> $$ \mathbf{\text{Líneas de Corriente} \equiv \text{Líneas de Trayectoria}} $$

#### Evolución Temporal de la Posición Angular $\theta(t)$:
Sustituyendo $r(\theta) = r_0 \frac{\sin\theta}{\sin\theta_0}$ en la ecuación diferencial para $\theta$:
$$ \frac{d\theta}{dt} = -\frac{M\cos(\Omega t)\sin\theta}{r^3} = -\frac{M\cos(\Omega t)\sin\theta}{\left(r_0 \frac{\sin\theta}{\sin\theta_0}\right)^3} = -\frac{M \sin^3\theta_0}{r_0^3} \frac{\cos(\Omega t)}{\sin^2\theta} $$
Separando variables:
$$ \sin^2\theta \, d\theta = -\frac{M \sin^3\theta_0}{r_0^3} \cos(\Omega t) \, dt $$
Integrando entre $\theta_0$ y $\theta$ (usando $\sin^2\theta = \frac{1 - \cos 2\theta}{2}$):
$$ \int_{\theta_0}^\theta \left(\frac{1 - \cos 2\theta'}{2}\right) d\theta' = -\frac{M \sin^3\theta_0}{r_0^3} \int_0^t \cos(\Omega t') dt' $$
$$ \mathbf{\frac{\theta - \theta_0}{2} - \frac{\sin(2\theta) - \sin(2\theta_0)}{4} = -\frac{M \sin^3\theta_0}{r_0^3 \Omega} \sin(\Omega t)} $$
Las partículas oscilan periódicamente hacia adelante y hacia atrás sobre la misma circunferencia.
