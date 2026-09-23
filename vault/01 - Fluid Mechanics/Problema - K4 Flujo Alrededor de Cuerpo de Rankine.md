---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - flujo-potencial
  - cuerpo-rankine
  - punto-estancamiento
  - funcion-corriente
dificultad: alta
fuente: "sources/01-fluid-mechanics/problemas/1.Kinematics/K4.pdf"
---

# ✏️ Problema K4: Flujo Alrededor de un Semisólido de Rankine (Fuente + Corriente Uniforme)

> **Origen:** Hoja de Problemas de Cinemática, UC3M (Prof. Antonio L. Sánchez & Javier Rodríguez-Rodríguez). Solución manuscrita oficial cotejada.

---

## 📋 Enunciado

Consider the fluid flow that derives from the potential

$$ \phi = \frac{Q}{2\pi} \ln r + U_\infty r \cos\theta $$

corresponding to the superposition of a uniform stream of velocity $U_\infty$ and a source of volumetric flux $Q$.

1. Determine the velocity components in cartesian and cylindrical coordinates.
2. Obtain the stream lines.
3. Compute the trajectories and paths.
4. Calculate the stagnation points, sketching the stream lines that reach them.
5. Consider the flow near the stagnation points, determining in particular the trajectories and the stream lines.

---

## 🎯 1. Planteamiento Físico e Hipótesis

* **Naturaleza del flujo:** Flujo bidimensional, plano, potencial ($\vec{v} = \nabla \phi$) e incompresible ($\nabla^2 \phi = 0$).
* **Superposición lineal:**
  1. Corriente libre uniforme en la dirección $+x$: $\phi_U = U_\infty x = U_\infty r \cos\theta$.
  2. Fuente lineal plana en el origen de gasto volumétrico por unidad de longitud $Q$: $\phi_S = \frac{Q}{2\pi} \ln r$.
* **Régimen:** Estacionario en el sistema de referencia inercial del cuerpo/fuente.

---

## 🔍 2. Resolución Matemática Paso a Paso

### Apartado 1: Componentes del Campo de Velocidades

#### En Coordenadas Polares Cilíndricas $(r, \theta)$:
$$ v_r = \frac{\partial \phi}{\partial r} = \mathbf{\frac{Q}{2\pi r} + U_\infty \cos\theta} $$
$$ v_\theta = \frac{1}{r}\frac{\partial \phi}{\partial \theta} = \mathbf{-U_\infty \sin\theta} $$

#### En Coordenadas Cartesianas $(x, y)$:
Recordando que $\vec{e}_r = \cos\theta \vec{e}_x + \sin\theta \vec{e}_y$ y $\vec{e}_\theta = -\sin\theta \vec{e}_x + \cos\theta \vec{e}_y$:
$$ v_x = v_r \cos\theta - v_\theta \sin\theta = \left(\frac{Q}{2\pi r} + U_\infty \cos\theta\right)\cos\theta - (-U_\infty \sin\theta)\sin\theta $$
$$ v_x = \frac{Q}{2\pi r}\cos\theta + U_\infty(\cos^2\theta + \sin^2\theta) = \mathbf{\frac{Q}{2\pi}\frac{x}{x^2+y^2} + U_\infty} $$

$$ v_y = v_r \sin\theta + v_\theta \cos\theta = \left(\frac{Q}{2\pi r} + U_\infty \cos\theta\right)\sin\theta + (-U_\infty \sin\theta)\cos\theta $$
$$ v_y = \frac{Q}{2\pi r}\sin\theta + U_\infty \sin\theta\cos\theta - U_\infty \sin\theta\cos\theta = \mathbf{\frac{Q}{2\pi}\frac{y}{x^2+y^2}} $$

#### Verificación del Gasto Volumétrico:
Para cualquier contorno cerrado que rodea el origen:
$$ \oint \vec{v} \cdot \vec{n} \, d\sigma = \int_0^{2\pi} v_r \, r d\theta = \int_0^{2\pi} \left(\frac{Q}{2\pi} + U_\infty r \cos\theta\right) d\theta = \frac{Q}{2\pi}(2\pi) + 0 = Q $$

---

### Apartado 2: Líneas de Corriente (*Streamlines*)

La ecuación diferencial de las líneas de corriente en polares es:
$$ \frac{dr}{v_r} = \frac{r d\theta}{v_\theta} \implies \frac{dr}{\frac{Q}{2\pi r} + U_\infty \cos\theta} = \frac{r d\theta}{-U_\infty \sin\theta} $$
Reordenando algebraicamente:
$$ \frac{Q}{2\pi} d\theta + U_\infty r \cos\theta \, d\theta + U_\infty \sin\theta \, dr = 0 $$
Reconociendo el diferencial exacto:
$$ d\left( \frac{Q\theta}{2\pi} + U_\infty r \sin\theta \right) = 0 $$
Por lo tanto, la función de corriente $\psi$ es:
$$ \mathbf{\psi(r, \theta) = \frac{Q\theta}{2\pi} + U_\infty r \sin\theta = \frac{Q\theta_0}{2\pi} + U_\infty r_0 \sin\theta_0 = \text{cte}} $$

---

### Apartado 3: Trayectorias y Líneas de Trayectoria

Como el flujo es **estacionario** ($\partial \vec{v}/\partial t = 0$), las líneas de trayectoria (*path lines*) coinciden exactamente con las líneas de corriente:
$$ \mathbf{\frac{Q\theta}{2\pi} + U_\infty r \sin\theta = \text{cte}} $$

Para obtener la dependencia temporal explícita $t(\theta)$:
$$ r \frac{d\theta}{dt} = v_\theta = -U_\infty \sin\theta \implies dt = -\frac{r \, d\theta}{U_\infty \sin\theta} $$
Despejando $r(\theta)$ de la ecuación de la línea de corriente:
$$ r(\theta) = \frac{\frac{Q}{2\pi}(\theta_0 - \theta) + U_\infty r_0 \sin\theta_0}{U_\infty \sin\theta} $$
Sustituyendo:
$$ \mathbf{t = -\int_{\theta_0}^\theta \frac{\frac{Q}{2\pi}(\theta_0 - \theta') + U_\infty r_0 \sin\theta_0}{U_\infty^2 \sin^2\theta'} d\theta'} $$

---

### Apartado 4: Puntos de Estancamiento y Línea de Corriente Divisoria

Un punto de estancamiento satisface $\vec{v} = 0$:
1. $v_\theta = -U_\infty \sin\theta = 0 \implies \sin\theta = 0 \implies \theta = 0 \text{ o } \theta = \pi$.
2. Componente radial:
   * En $\theta = 0$: $v_r = \frac{Q}{2\pi r} + U_\infty > 0$ (la fuente y la corriente suman en la misma dirección, nunca se anula).
   * En $\theta = \pi$: $v_r = \frac{Q}{2\pi r} - U_\infty = 0 \implies \mathbf{r_0 = \frac{Q}{2\pi U_\infty}}$.

Por tanto, existe un **único punto de estancamiento**:
$$ \mathbf{(r = r_0 = \frac{Q}{2\pi U_\infty}, \; \theta = \pi)} \quad \text{ó en cartesianas } (x = -r_0, y = 0) $$

#### Línea de Corriente que Llega al Punto de Estancamiento:
Evaluando la función de corriente en el punto de estancamiento $(r_0, \pi)$:
$$ \psi_{est} = \frac{Q (\pi)}{2\pi} + U_\infty r_0 \sin\pi = \frac{Q}{2} $$
Igualando $\psi(r, \theta) = \frac{Q}{2}$:
$$ \frac{Q\theta}{2\pi} + U_\infty r \sin\theta = \frac{Q}{2} \implies U_\infty r \sin\theta = \frac{Q}{2}\left(1 - \frac{\theta}{\pi}\right) = \frac{Q(\pi - \theta)}{2\pi} $$
$$ \mathbf{r(\theta) = \frac{Q(\pi - \theta)}{2\pi U_\infty \sin\theta}, \qquad 0 < \theta < 2\pi} $$

Esta curva define la superficie del **semicuerpo de Rankine** (*Rankine half-body*):
* Cuando $\theta \to \pi$, aplicando la regla de L'Hôpital: $r \to \frac{Q}{2\pi U_\infty} = r_0$ (morro del cuerpo).
* Cuando $\theta \to 0$ (aguas abajo), la ordenada tiende asintóticamente a:
  $$ y = r \sin\theta \to \frac{Q}{2 U_\infty} $$
  El ancho asintótico total del cuerpo es $2 y_\infty = \frac{Q}{U_\infty}$.
* La semirrecta del eje $x$ aguas arriba ($\theta = \pi, r > r_0$) forma la otra rama de la línea de corriente divisoria.

---

### Apartado 5: Flujo Local en las Inmediaciones del Punto de Estancamiento

Definimos coordenadas locales adimensionales centradas en el punto de estancamiento $(x_s = -r_0, y_s = 0)$:
$$ \xi = \frac{x - (-r_0)}{r_0} = \frac{x + r_0}{r_0} \ll 1, \qquad \eta = \frac{y}{r_0} \ll 1 $$
Desarrollando en serie de Taylor el campo cartesiano alrededor de $\xi = 0, \eta = 0$:
$$ V_\xi = \frac{v_x}{U_\infty} \approx -\xi, \qquad V_\eta = \frac{v_y}{U_\infty} \approx \eta $$
Definiendo el tiempo adimensional $\tau = \frac{t U_\infty}{r_0}$:

* **Líneas de corriente locales:**
  $$ \frac{d\xi}{-\xi} = \frac{d\eta}{\eta} \implies \ln \xi + \ln \eta = \text{cte} \implies \mathbf{\xi \eta = \xi_0 \eta_0 = \text{cte}} $$
  Corresponden a una familia de **hipérbolas ortogonales** (punto de silla o estancamiento bidimensional clásico).

* **Trayectorias locales:**
  $$ \frac{d\xi}{d\tau} = -\xi \implies \mathbf{\xi(\tau) = \xi_0 e^{-\tau}} $$
  $$ \frac{d\eta}{d\tau} = \eta \implies \mathbf{\eta(\tau) = \eta_0 e^{\tau}} $$
  El fluido desacelera exponencialmente en la dirección del eje $\xi$ (aproximación al estancamiento) y acelera exponencialmente alejándose en la dirección $\eta$.
