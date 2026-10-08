---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - fuente-puntual
  - esfericas
  - linea-fluida
  - tubo-corriente
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-02-flow-kinematics/problemas/K3.pdf"
---

# ✏️ Problema K3: Fuente Tridimensional Puntual en el Origen

> **Origen:** Hoja de Problemas de Cinemática, UC3M (Prof. Antonio L. Sánchez & Javier Rodríguez-Rodríguez). Solución manuscrita oficial cotejada.

---

## 📋 Enunciado

A three-dimensional fluid source placed at the origin induces a radial motion given by $v_r = Q(t)/(4\pi r^2)$, with $v_\theta = v_\phi = 0$. Obtain:

1. Streamlines, trajectories and paths.
2. Equation for the fluid surface initially located at $r = R$.
3. Equation for the fluid line that corresponds at the initial instant with a circle of radius $R$ intersecting the origin.
4. Streamtube that intersects the circle defined by $r = R_1$ and $\theta = \theta_1$.
5. The velocity components in cartesian coordinates, as well as the corresponding streamlines and trajectories.
6. Equations for the streamlines and trajectories for an observer moving with velocity $U$.

---

## 🎯 1. Planteamiento Físico e Hipótesis

* **Geometría:** Espacio tridimensional $\mathbb{R}^3$ con simetría esférica en torno al origen $(0,0,0)$.
* **Campo de velocidades en coordenadas esféricas $(r, \theta, \phi)$:**
  $$ \vec{v}(r, \theta, \phi, t) = \frac{Q(t)}{4\pi r^2} \vec{e}_r + 0 \vec{e}_\theta + 0 \vec{e}_\phi $$
* **Régimen:** En general no estacionario si el caudal volumétrico $Q(t)$ varía en el tiempo; puramente radial y divergente desde el origen.

---

## 🔍 2. Resolución Matemática Paso a Paso

### Apartado 1: Líneas de Corriente, Trayectorias y Líneas de Trayectoria

#### Líneas de Corriente (*Streamlines*)
En coordenadas esféricas, el elemento diferencial de arco es $d\vec{l} = dr \vec{e}_r + r d\theta \vec{e}_\theta + r \sin\theta d\phi \vec{e}_\phi$. La condición de paralelismo $d\vec{l} \times \vec{v} = 0$ se traduce en:
$$ \frac{dr}{v_r} = \frac{r d\theta}{v_\theta} = \frac{r \sin\theta d\phi}{v_\phi} $$
Puesto que $v_\theta = 0$ y $v_\phi = 0$:
$$ d\theta = 0 \implies \mathbf{\theta = \theta_0 = \text{cte}} $$
$$ d\phi = 0 \implies \mathbf{\phi = \phi_0 = \text{cte}} $$
Las líneas de corriente son **semirrectas radiales** que parten del origen hacia el infinito.

#### Trayectorias (*Trajectories*)
El sistema de ecuaciones diferenciales para la posición de una partícula fluida $(r(t), \theta(t), \phi(t))$ inicialmente en $(r_0, \theta_0, \phi_0)$ es:
$$ r \frac{d\theta}{dt} = 0 \implies \theta(t) = \theta_0 $$
$$ r \sin\theta \frac{d\phi}{dt} = 0 \implies \phi(t) = \phi_0 $$
$$ \frac{dr}{dt} = v_r = \frac{Q(t)}{4\pi r^2} $$
Separando variables e integrando entre $t=0$ y $t$:
$$ 4\pi r^2 dr = Q(t) dt \implies \int_{r_0}^{r(t)} 4\pi r'^2 dr' = \int_0^t Q(t') dt' $$
$$ \mathbf{\frac{4\pi}{3}\left[r(t)^3 - r_0^3\right] = \int_0^t Q(t') dt'} $$
Despejando el radio de la partícula:
$$ r(t) = \left[ r_0^3 + \frac{3}{4\pi}\int_0^t Q(t') dt' \right]^{1/3} $$

> [!NOTE] Líneas de Trayectoria (*Path lines*)
> Como las partículas se desplazan a lo largo de $\theta = \theta_0$ y $\phi = \phi_0$, las trayectorias coinciden geométricamente en el espacio con las líneas de corriente (semirrectas radiales).

---

### Apartado 2: Evolución de la Superficie Fluida Inicial $r = R$

La superficie inicial está formada por todas las partículas que en $t = 0$ tienen radio $r_0 = R$:
$$ \vec{x}_0(\alpha, \beta) = (r_0 = R, \; \theta_0 = \alpha, \; \phi_0 = \beta), \quad \alpha \in [0, \pi], \; \beta \in [0, 2\pi) $$
Aplicando la solución de las trayectorias:
$$ \frac{4\pi}{3}\left(r^3 - R^3\right) = \int_0^t Q(t') dt' $$
$$ \mathbf{r(t) = \left( R^3 + \frac{3}{4\pi}\int_0^t Q(t') dt' \right)^{1/3}} $$
**Conclusión geométrica:** La superficie fluida sigue siendo una **esfera perfecta**, concéntrica con el origen, cuyo radio se expande con el tiempo de manera que el volumen interior crece exactamente en $\int_0^t Q dt'$.

---

### Apartado 3: Evolución de una Línea Fluida Circular Inicial que Pasa por el Origen

Consideramos una circunferencia de radio $R$ situada, por ejemplo, en el plano $\phi = 0$, que es tangente al eje polar o contiene al origen. En coordenadas esféricas, dicha circunferencia puede parametrizarse con el ángulo $\lambda \in [-\pi/2, \pi/2]$:
$$ \phi_0 = 0, \qquad \theta_0 = \lambda, \qquad r_0 = 2R \cos\lambda $$
(Here $\lambda$ is the signed polar angle in the plane $\phi = 0$ measured from the diameter through the origin; negative $\lambda$ labels the half-plane $\phi = \pi$.) Check of the initial curve: with $z_0 = r_0\cos\lambda = 2R\cos^2\lambda = R(1+\cos 2\lambda)$ and $x_0 = r_0\sin\lambda = R\sin 2\lambda$, $x_0^2 + (z_0 - R)^2 = R^2(\sin^2 2\lambda + \cos^2 2\lambda) = R^2$, a circle of radius $R$ through the origin (the origin is $\lambda = \pm\pi/2$, $r_0 = 0$).
Sustituyendo estas condiciones iniciales en la ecuación de evolución lagrangiana:
$$ \phi = 0, \qquad \theta = \lambda $$
$$ \frac{4\pi}{3}\left(r^3 - 8R^3 \cos^3\lambda\right) = \int_0^t Q(t') dt' $$
Eliminando el parámetro material $\lambda$ mediante $\lambda = \theta$:
$$ \mathbf{\frac{4\pi}{3}\left(r^3 - 8R^3 \cos^3\theta\right) = \int_0^t Q(t') dt'} $$
Despejando $r(\theta, t)$:
$$ r(\theta, t) = \left( 8R^3 \cos^3\theta + \frac{3}{4\pi}\int_0^t Q(t') dt' \right)^{1/3} $$
La circunferencia inicial se deforma conforme el fluido se expande radialmente.

> [!warning] Erratum in the official solution
> The handwritten K3.pdf (part 3) takes $r_0 = R\cos\lambda$ and writes $\frac{4\pi}{3}(r^3 - R^3\cos^3\theta) = \int_0^t Q\,dt'$. The polar equation $r = R\cos\theta$ is a circle of diameter $R$ (radius $R/2$), not of radius $R$; a circle of radius $R$ through the origin is $r = 2R\cos\theta$, which gives the factor $8R^3$ above. The two results coincide only after the substitution $R \to 2R$.

---

### Apartado 4: Tubo de Corriente que Interseca la Circunferencia $r = R_1, \theta = \theta_1$

Un tubo de corriente (*streamtube*) es una superficie formada por el haz de líneas de corriente que pasan por una curva cerrada dada.
* La curva generatriz es el paralelo $r = R_1, \theta = \theta_1$ (una circunferencia horizontal de radio $R_1\sin\theta_1$ centrada en el eje polar).
* Como las líneas de corriente son semirrectas radiales definidas por $\theta = \text{cte}$ y $\phi = \text{cte}$, el haz de líneas que pasa por cualquier punto con $\theta = \theta_1$ mantiene $\theta = \theta_1$ para todo radio $r$.

Por consiguiente, la ecuación del tubo de corriente es simplemente:
$$ \mathbf{\theta = \theta_1} $$
Geométricamente, se trata de un **cono circular recto** de semiángulo cónico $\theta_1$ con vértice en el origen.

---

### Apartado 5: Componentes Cartesianas, Líneas de Corriente y Trayectorias

El cambio de coordenadas esféricas a cartesianas viene dado por:
$$ x = r \sin\theta \cos\phi, \qquad y = r \sin\theta \sin\phi, \qquad z = r \cos\theta $$
$$ r = (x^2 + y^2 + z^2)^{1/2} $$

El vector unitario radial en base cartesiana es:
$$ \vec{e}_r = \frac{x}{r}\vec{e}_x + \frac{y}{r}\vec{e}_y + \frac{z}{r}\vec{e}_z $$
Multiplicando por la magnitud de la velocidad $v_r = \frac{Q(t)}{4\pi r^2}$:
$$ v_x = v_r \sin\theta \cos\phi = \frac{Q(t)}{4\pi r^2} \frac{x}{r} = \mathbf{\frac{Q(t)}{4\pi} \frac{x}{(x^2 + y^2 + z^2)^{3/2}}} $$
$$ v_y = v_r \sin\theta \sin\phi = \frac{Q(t)}{4\pi r^2} \frac{y}{r} = \mathbf{\frac{Q(t)}{4\pi} \frac{y}{(x^2 + y^2 + z^2)^{3/2}}} $$
$$ v_z = v_r \cos\theta = \frac{Q(t)}{4\pi r^2} \frac{z}{r} = \mathbf{\frac{Q(t)}{4\pi} \frac{z}{(x^2 + y^2 + z^2)^{3/2}}} $$

#### Líneas de Corriente en Cartesianas:
$$ \frac{dx}{v_x} = \frac{dy}{v_y} = \frac{dz}{v_z} \implies \frac{dx}{x} = \frac{dy}{y} = \frac{dz}{z} $$
Integrando directamente:
$$ \mathbf{\frac{x}{x_0} = \frac{y}{y_0} = \frac{z}{z_0}} $$
Representan las rectas tridimensionales que pasan por el origen $(0,0,0)$ y por el punto inicial $(x_0, y_0, z_0)$.

#### Trayectorias en Cartesianas:
$$ \frac{dx}{dt} = \frac{Q(t)}{4\pi}\frac{x}{(x^2+y^2+z^2)^{3/2}} $$
Usando las relaciones geométricas $y = (y_0/x_0)x$ y $z = (z_0/x_0)x$:
$$ x^2 + y^2 + z^2 = x^2 \left[1 + \left(\frac{y_0}{x_0}\right)^2 + \left(\frac{z_0}{x_0}\right)^2\right] = x^2 \left(\frac{r_0}{x_0}\right)^2 $$
Sustituyendo:
$$ \frac{dx}{dt} = \frac{Q(t)}{4\pi} \frac{x}{x^3 (r_0/x_0)^3} = \frac{Q(t)}{4\pi (r_0/x_0)^3} \frac{1}{x^2} $$
$$ x^2 dx = \frac{Q(t) dt}{4\pi \left[1 + (y_0/x_0)^2 + (z_0/x_0)^2\right]^{3/2}} $$
Integrando se recupera exactamente la ley radial cúbica $\frac{4\pi}{3}(r^3 - r_0^3) = \int Q dt$.

---

### Apartado 6: Flujo Visto por un Observador en Movimiento a Velocidad Constante $U \vec{e}_x$

Para un sistema de referencia móvil ligado al observador con velocidad $\vec{V}_{obs} = U \vec{e}_x$ (the source stays fixed at the origin of the laboratory frame; axes parallel, observer and laboratory origins coincide at $t = 0$):
$$ x' = x - U t, \qquad y' = y, \qquad z' = z, \qquad \vec{v}' = \vec{v} - U \vec{e}_x $$
The laboratory field must be evaluated at the laboratory position $x = x' + Ut$. In the observer frame the source therefore sits at $x' = -Ut$, $y' = z' = 0$, and it moves. Defining $r_s^2 \equiv (x' + Ut)^2 + y'^2 + z'^2$, the relative velocity components are
$$ v_x' = \frac{Q(t)}{4\pi} \frac{x' + Ut}{\left[(x' + Ut)^2 + y'^2 + z'^2\right]^{3/2}} - U $$
$$ v_y' = \frac{Q(t)}{4\pi} \frac{y'}{\left[(x' + Ut)^2 + y'^2 + z'^2\right]^{3/2}} $$
$$ v_z' = \frac{Q(t)}{4\pi} \frac{z'}{\left[(x' + Ut)^2 + y'^2 + z'^2\right]^{3/2}} $$

* **Líneas de corriente relativas** (instantaneous curves: $t$ frozen in the field, $\vec{v}'$ is unsteady through $Ut$ and $Q(t)$):
  $$ \frac{dx'}{\frac{Q\,(x' + Ut)}{4\pi r_s^3} - U} = \frac{dy'}{\frac{Q\, y'}{4\pi r_s^3}} = \frac{dz'}{\frac{Q\, z'}{4\pi r_s^3}} $$
* **Trayectorias relativas:**
  $$ \frac{d\vec{x}'}{dt} = \vec{v}'(\vec{x}', t) $$
  Since $\vec{x}' = \vec{x} - Ut\,\vec{e}_x$ and $\vec{x}(t)$ is the radial path of Apartado 1 ($\vec{x} = r(t)\,\vec{e}_r(\theta_0,\phi_0)$ with $r(t)^3 = r_0^3 + \frac{3}{4\pi}\int_0^t Q\,dt'$), the relative trajectory is $\vec{x}'(t) = r(t)\,\vec{e}_r(\theta_0,\phi_0) - Ut\,\vec{e}_x$, which is curved in general.
  This relative flow is **not** a steady three-dimensional Rankine body: with the source fixed in the laboratory frame, $\vec{v}'$ depends explicitly on $t$ even for constant $Q$. The superposition of a point source and a uniform stream $-U\vec{e}_x$ (steady Rankine half-body of revolution, when $Q$ is constant) is obtained only if the source **moves with the observer**, i.e. if the source sits at $x' = 0$, which gives the field $v_x' = \frac{Q}{4\pi}\frac{x'}{r'^3} - U$ with $r'^2 = x'^2 + y'^2 + z'^2$ (a different problem from the one stated here).
