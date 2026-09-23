---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - vortice-burgers
  - incompresibilidad
  - coordenadas-cilindricas
  - estiramiento-vortice
dificultad: media
fuente: "sources/01-fluid-mechanics/problemas/1.Kinematics/K6.pdf"
---

# ✏️ Problema K6: Vórtice Tridimensional de Burgers con Estiramiento Axial

> **Origen:** Hoja de Problemas de Cinemática, UC3M (Prof. Antonio L. Sánchez & Javier Rodríguez-Rodríguez). Solución manuscrita oficial cotejada.

---

## 📋 Enunciado

The axisymmetric velocity field corresponding to a three-dimensional steady vortex of circulation $\Gamma$ is given in cylindrical coordinates by:

$$ v_r = -\frac{r}{\tau_r}, \qquad v_\theta = \frac{\Gamma}{2\pi r}\left\{ 1 - \exp\left[ -\left(\frac{r}{R_0}\right)^2 \right] \right\}, \qquad v_z = \frac{z}{\tau_z} $$

where the constants $R_0$, $\tau_r$ and $\tau_z$ measure the radius of the inner core where viscous effects are important, and the characteristic times associated with radial convection and axial stretch, respectively.

1. Determine the condition required for the motion to be that of an incompressible fluid.
2. Compute streamlines and trajectories.

---

## 🎯 1. Planteamiento Físico e Hipótesis

* **Naturaleza física:** Este campo modela el célebre **vórtice de Burgers**, un equilibrio exacto de las ecuaciones de Navier-Stokes donde la difusión viscosa de vorticidad hacia fuera es exactamente compensada por la convección radial hacia el eje ($v_r < 0$) producida por el estiramiento axial ($v_z > 0$).
* **Sistema de coordenadas:** Coordenadas cilíndricas axisimétricas $(r, \theta, z)$.
* **Régimen:** Estacionario ($\partial \vec{v}/\partial t = 0$).

---

## 🔍 2. Resolución Matemática Paso a Paso

### Apartado 1: Condición de Incompresibilidad ($\nabla \cdot \vec{v} = 0$)

La divergencia de un campo de velocidades en coordenadas cilíndricas $(r, \theta, z)$ se expresa como:
$$ \nabla \cdot \vec{v} = \frac{1}{r}\frac{\partial(r v_r)}{\partial r} + \frac{1}{r}\frac{\partial v_\theta}{\partial \theta} + \frac{\partial v_z}{\partial z} = 0 $$

Calculando cada uno de los tres sumandos:
1. Término radial:
   $$ r v_r = r \left(-\frac{r}{\tau_r}\right) = -\frac{r^2}{\tau_r} \implies \frac{\partial(r v_r)}{\partial r} = -\frac{2r}{\tau_r} $$
2. Término acimutal:
   Como el flujo es axisimétrico, $v_\theta$ no depende de $\theta$:
   $$ \frac{\partial v_\theta}{\partial \theta} = 0 $$
3. Término axial:
   $$ \frac{\partial v_z}{\partial z} = \frac{\partial}{\partial z}\left(\frac{z}{\tau_z}\right) = \frac{1}{\tau_z} $$

Sustituyendo en la divergencia:
$$ \nabla \cdot \vec{v} = \frac{1}{r}\left[ -\frac{2r}{\tau_r} + 0 + \frac{r}{\tau_z} \right] = -\frac{2}{\tau_r} + \frac{1}{\tau_z} = 0 $$
Despejando la relación entre los tiempos característicos:
$$ \mathbf{\tau_r = 2\tau_z} $$

> [!NOTE] Significado Físico
> El tiempo característico de colapso radial debe ser exactamente el doble del tiempo característico de estiramiento axial para que el volumen de cualquier elemento material se conserve constante en el tiempo.

---

### Apartado 2: Líneas de Corriente y Trayectorias

Dado que el flujo es **estacionario** ($\partial \vec{v}/\partial t = 0$), las **líneas de corriente coinciden con las trayectorias** de las partículas fluidas.

#### 1. Evolución Radial (T1):
$$ \frac{dr}{dt} = v_r = -\frac{r}{\tau_r} \implies \frac{dr}{r} = -\frac{dt}{\tau_r} $$
Integrando entre $t=0$ ($r=r_0$) y $t$:
$$ \mathbf{r(t) = r_0 e^{-t/\tau_r}} \qquad \text{(T1)} $$
El radio de cada partícula decae exponencialmente hacia el eje del vórtice.

#### 2. Evolución Axial (T3):
$$ \frac{dz}{dt} = v_z = \frac{z}{\tau_z} \implies \frac{dz}{z} = \frac{dt}{\tau_z} $$
Integrando entre $t=0$ ($z=z_0$) y $t$:
$$ \mathbf{z(t) = z_0 e^{t/\tau_z}} \qquad \text{(T3)} $$
La coordenada axial crece exponencialmente con el tiempo.

#### 3. Relación entre $r$ y $z$ en la Superficie de Corriente:
Eliminando el tiempo $t$ entre las ecuaciones (T1) y (T3):
$$ e^t = \left(\frac{r}{r_0}\right)^{-\tau_r} = \left(\frac{z}{z_0}\right)^{\tau_z} \implies \left(\frac{z}{z_0}\right)^{\tau_z} = \left(\frac{r}{r_0}\right)^{-\tau_r} $$
Elevando a la potencia $1/\tau_z$ y utilizando la condición de incompresibilidad $\tau_r/\tau_z = 2$:
$$ \frac{z}{z_0} = \left(\frac{r}{r_0}\right)^{-2} = \left(\frac{r_0}{r}\right)^2 $$
Multiplicando en cruz:
$$ \mathbf{z r^2 = z_0 r_0^2 = \text{cte}} $$
Las superficies axisimétricas de corriente sobre las que viajan las partículas son hiperboloides de revolución cúbicos.

#### 4. Evolución Acimutal $\theta(r)$ (T2):
La variación del ángulo $\theta$ a lo largo de la trayectoria se obtiene dividiendo la componente acimutal por la radial:
$$ r \frac{d\theta}{dt} = v_\theta = \frac{\Gamma}{2\pi r}\left\{ 1 - \exp\left[ -\left(\frac{r}{R_0}\right)^2 \right] \right\} $$
$$ \frac{r d\theta}{dr} = \frac{v_\theta}{v_r} = \frac{\frac{\Gamma}{2\pi r}\left\{ 1 - \exp\left[ -\left(\frac{r}{R_0}\right)^2 \right] \right\}}{-r/\tau_r} = -\frac{\Gamma \tau_r}{2\pi r^2}\left\{ 1 - \exp\left[ -\left(\frac{r}{R_0}\right)^2 \right] \right\} $$
Separando variables:
$$ d\theta = -\frac{\Gamma \tau_r}{2\pi}\left\{ 1 - \exp\left[ -\left(\frac{r}{R_0}\right)^2 \right] \right\} \frac{dr}{r^3} $$
Integrando desde $r_0$ hasta $r$:
$$ \mathbf{\theta - \theta_0 = -\frac{\Gamma \tau_r}{2\pi} \int_{r_0}^r \left\{ 1 - \exp\left[ -\left(\frac{r'}{R_0}\right)^2 \right] \right\} \frac{dr'}{r'^3}} \qquad \text{(T2)} $$

#### Síntesis de las Líneas de Corriente:
Las líneas de corriente en $\mathbb{R}^3$ vienen completamente determinadas por la intersección de:
1. La superficie axisimétrica: $\mathbf{z r^2 = z_0 r_0^2}$
2. La relación helicoidal de enrollamiento: $\mathbf{\theta(r) \text{ dada por (T2)}}$

Conforme la partícula se acerca al eje ($r \to 0$), gira a velocidad angular asintóticamente constante $\Omega_0 = \frac{\Gamma}{2\pi R_0^2}$ mientras es eyectada en la dirección axial hacia $z \to \pm \infty$.
