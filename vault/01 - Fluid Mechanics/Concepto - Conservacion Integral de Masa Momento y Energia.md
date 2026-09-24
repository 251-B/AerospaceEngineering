---
materia: Fluid Mechanics
tema: "Tema 3: Conservation Laws"
tags:
  - teoria
  - concepto-clave
  - conservacion-integral
  - masa-momento-energia
  - empuje-aeroespacial
dificultad: muy alta
prerrequisitos:
  - "[[01 - Fluid Mechanics/Concepto - Teorema de Transporte de Reynolds|Concepto: Teorema de Transporte de Reynolds]]"
  - "[[01 - Fluid Mechanics/Concepto - Tensor de Esfuerzos y Principio de Cauchy|Concepto: Tensor de Esfuerzos de Cauchy]]"
  - "[[01 - Fluid Mechanics/Concepto - Ecuacion Constitutiva de Navier-Poisson|Concepto: Ecuación de Navier-Poisson]]"
  - "[[01 - Fluid Mechanics/Concepto - Ley de Fourier y Conduccion Termica|Concepto: Ley de Fourier y Conducción Térmica]]"
---

# 🔬 Concepto: Conservación Integral de Masa, Momento y Energía

> **Idea clave en una frase:** Las leyes de conservación de la mecánica clásica aplicadas a un volumen de control arbitrario $V_c(t)$ permiten calcular de forma exacta balances globales de flujo (fuerzas de sustentación y resistencia, empuje de propulsores aeronáuticos, pares en turbomáquinas y potencias térmicas) integrando únicamente los flujos y esfuerzos en las fronteras de control, sin necesidad de resolver la cinemática detallada en cada punto interno del dominio.

---

## 💧 1. Ecuación Integral de Conservación de Masa (Notes.pdf, Ecs. 3.9–3.11)

### Principio Físico
La masa de un sistema material cerrado (volumen fluido $V_f(t)$) es constante en el tiempo en mecánica no relativista:

$$ \frac{d}{dt} M = \frac{d}{dt} \left[ \int_{V_f(t)} \rho \, dV \right] = 0 \qquad \text{[Ec. 3.9]} $$

### Para un Volumen de Control Móvil Arbitrario $V_c(t)$
Aplicando el Teorema de Transporte de Reynolds (Ec. 3.8) con $\phi = \rho$:

$$ \mathbf{\frac{d}{dt}\left[\int_{V_c(t)} \rho \, dV\right] + \int_{\Sigma_c(t)} \rho \, (\vec{v} - \vec{v}_c)\cdot\vec{n} \, d\sigma = 0} \qquad \text{[Ec. 3.10]} $$

* **Término 1:** Tasa temporal de acumulación o desahogo de masa dentro de la cavidad geométrica $V_c(t)$.
* **Término 2:** Flujo másico neto que atraviesa la superficie de control $\Sigma_c(t)$ impulsado por la velocidad relativa del fluido $(\vec{v} - \vec{v}_c)$.

### Para un Volumen de Control Fijo en el Espacio ($V_0, \vec{v}_c = 0$)
$$ \mathbf{\int_{V_0} \frac{\partial \rho}{\partial t} \, dV + \int_{\Sigma_0} \rho \, \vec{v}\cdot\vec{n} \, d\sigma = 0} \qquad \text{[Ec. 3.11]} $$

* **Flujo estacionario:** $\frac{\partial\rho}{\partial t} = 0 \implies \int_{\Sigma_0} \rho \vec{v}\cdot\vec{n} d\sigma = 0 \implies \sum \dot{m}_{\text{salida}} = \sum \dot{m}_{\text{entrada}}$.
* **Fluido incompresible ($\rho = \text{cte}$):** $\int_{\Sigma_0} \vec{v}\cdot\vec{n} d\sigma = 0 \implies \sum Q_{\text{salida}} = \sum Q_{\text{entrada}}$ (conservación del caudal volumétrico).

---

## ✈️ 2. Fuerzas y Momentos sobre Cuerpos Sumergidos (Notes.pdf, Ecs. 3.32–3.33)

Cuando un cuerpo sólido (como un perfil alar, un fuselaje o un álabe de turbina) está inmerso en una corriente fluida, la fuerza y el momento aerodinámico que el fluido ejerce sobre la pared sólida mojada $\Sigma$ provienen exclusivamente de los esfuerzos de presión normal y los esfuerzos viscosos tangenciales de fricción.

Definiendo el vector normal unitario $\vec{n}$ apuntando **hacia el interior del fluido** (saliendo del sólido):

### Fuerza Resultante $\vec{F}$ (Sustentación + Resistencia)
$$ \mathbf{\vec{F} = -\int_\Sigma p \vec{n} \, d\sigma + \int_\Sigma \bar{\bar{\tau}}' \cdot \vec{n} \, d\sigma} \qquad \text{[Ec. 3.32]} $$

* $-\int_\Sigma p \vec{n} d\sigma$: **Fuerza de presión**. El signo menos se debe a que una presión positiva comprime la superficie en dirección opuesta a la normal exterior $\vec{n}$. Origina la sustentación aerodinámica ($L$) y la resistencia de forma o de presión ($D_p$).
* $\int_\Sigma \bar{\bar{\tau}}' \cdot \vec{n} d\sigma$: **Fuerza de fricción viscosa** (*skin-friction drag*). Origina la resistencia parásita por rozamiento tangencial en la capa límite.

### Momento Resultante $\vec{M}_{\vec{x}_0}$ respecto a un punto $\vec{x}_0$
$$ \mathbf{\vec{M}_{\vec{x}_0} = -\int_\Sigma (\vec{x} - \vec{x}_0) \wedge (p\vec{n}) \, d\sigma + \int_\Sigma (\vec{x} - \vec{x}_0) \wedge (\bar{\bar{\tau}}' \cdot \vec{n}) \, d\sigma} \qquad \text{[Ec. 3.33]} $$

Determina el momento de cabeceo, balanceo y guiñada del vehículo espacial o aeronáutico.

---

## 🎯 3. Ecuación Integral de Conservación de Cantidad de Movimiento (Notes.pdf, Ecs. 3.34–3.36)

### Para un Volumen Material Fluido $V_f(t)$
Aplicando la 2ª Ley de Newton ($\frac{d}{dt}\vec{P} = \sum \vec{F}_{\text{ext}}$) y sustituyendo el tensor de Cauchy $\bar{\bar{\tau}} = -p\bar{\bar{I}} + \bar{\bar{\tau}}'$:

$$ \frac{d}{dt}\left[\int_{V_f(t)} \rho\vec{v} \, dV\right] = -\int_{\Sigma_f(t)} p\vec{n} \, d\sigma + \int_{\Sigma_f(t)} \bar{\bar{\tau}}' \cdot \vec{n} \, d\sigma + \int_{V_f(t)} \rho\vec{f}_m \, dV \qquad \text{[Ec. 3.34]} $$

### Para un Volumen de Control Móvil Arbitrario $V_c(t)$
Aplicando el RTT (Ec. 3.8) con $\phi = \rho\vec{v}$:

$$ \mathbf{\frac{d}{dt}\left[\int_{V_c(t)} \rho\vec{v} \, dV\right] + \int_{\Sigma_c(t)} \rho\vec{v}[(\vec{v}-\vec{v}_c)\cdot\vec{n}] \, d\sigma = -\int_{\Sigma_c(t)} p\vec{n} \, d\sigma + \int_{\Sigma_c(t)} \bar{\bar{\tau}}' \cdot \vec{n} \, d\sigma + \int_{V_c(t)} \rho\vec{f}_m \, dV} \qquad \text{[Ec. 3.35]} $$

### Para un Volumen de Control Fijo en el Espacio ($V_0, \vec{v}_c = 0$)
$$ \mathbf{\int_{V_0} \frac{\partial(\rho\vec{v})}{\partial t} \, dV + \int_{\Sigma_0} \rho\vec{v}(\vec{v}\cdot\vec{n}) \, d\sigma = -\int_{\Sigma_0} p\vec{n} \, d\sigma + \int_{\Sigma_0} \bar{\bar{\tau}}' \cdot \vec{n} \, d\sigma + \int_{V_0} \rho\vec{f}_m \, dV} \qquad \text{[Ec. 3.36]} $$

### Desglose Físico Exhaustivo de los Cinco Términos
1. **$\frac{d}{dt}\int_{V_c} \rho\vec{v} dV$ (Inercia / Acumulación Local):** Rapidez con la que varía la cantidad de movimiento total contenida en el interior del volumen de control. Se anula rigurosamente en régimen estacionario.
2. **$\int_{\Sigma_c} \rho\vec{v}[(\vec{v}-\vec{v}_c)\cdot\vec{n}] d\sigma$ (Flujo Convectivo Neto Saliente):** Tasa neta a la que la cantidad de movimiento abandona el volumen a través de las secciones de entrada y salida, impulsada por la masa que cruza con velocidad relativa $(\vec{v}-\vec{v}_c)\cdot\vec{n}$.
3. **$-\int_{\Sigma_c} p\vec{n} d\sigma$ (Fuerza Neta de Presión):** Empuje distribuido de las presiones termodinámicas sobre la frontera de control. En tramos abiertos a la atmósfera, puede operarse con presiones manométricas $(p - p_a)$.
4. **$\int_{\Sigma_c} \bar{\bar{\tau}}' \cdot \vec{n} d\sigma$ (Fuerza Neta Viscosa):** Fricción tangencial en paredes sólidas mojadas o tensiones de corte en planos de cizalladura. Frecuentemente despreciable en secciones de entrada/salida lejanas.
5. **$\int_{V_c} \rho\vec{f}_m dV$ (Fuerza Volumétrica Total):** Peso total del fluido en el volumen ($+\int \rho\vec{g} dV$) y fuerzas inerciales si el sistema no es inercial.

---

## 🌀 4. Ecuación Integral de Momento Cinético (Notes.pdf, Ecs. 3.37–3.38)

El balance del momento de la cantidad de movimiento respecto a un punto fijo $\vec{x}_0$ para un volumen de control móvil $V_c(t)$ viene dado por:

$$ \begin{aligned}
\mathbf{\frac{d}{dt}\left[\int_{V_c(t)} \rho[(\vec{x}-\vec{x}_0)\wedge\vec{v}] \, dV\right] + \int_{\Sigma_c(t)} \rho[(\vec{x}-\vec{x}_0)\wedge\vec{v}][(\vec{v}-\vec{v}_c)\cdot\vec{n}] \, d\sigma =} \\
\mathbf{-\int_{\Sigma_c(t)} (\vec{x}-\vec{x}_0)\wedge(p\vec{n}) \, d\sigma + \int_{\Sigma_c(t)} (\vec{x}-\vec{x}_0)\wedge(\bar{\bar{\tau}}'\cdot\vec{n}) \, d\sigma + \int_{V_c(t)} \rho[(\vec{x}-\vec{x}_0)\wedge\vec{f}_m] \, dV}
\end{aligned} \qquad \text{[Ec. 3.38]} $$

### Aplicación en Turbomáquinas Aeroespaciales: Ecuación de Euler
En el rotor de un compresor axial o turbina de gas que gira a velocidad angular constante $\vec{\Omega}$, el par ejercido por el fluido sobre el rotor en régimen estacionario es:
$$ T_{\text{eje}} = \dot{m} (r_2 v_{\theta 2} - r_1 v_{\theta 1}) $$
Multiplicando por $\Omega$, la potencia mecánica intercambiada por unidad de flujo másico es la **fórmula de Euler para turbomáquinas**:
$$ w_{\text{Euler}} = u_2 v_{\theta 2} - u_1 v_{\theta 1} $$
donde $u = \Omega r$ es la velocidad de arrastre del álabe y $v_\theta$ es la componente tangencial de la velocidad del fluido.

---

## ⚡ 5. Ecuación Integral de Conservación de Energía Total (Notes.pdf, Ecs. 3.45–3.46)

### Para un Volumen Material Fluido $V_f(t)$
La energía total por unidad de masa de una partícula fluida es la suma de su energía interna microscópica $e$ y su energía cinética macroscópica $\frac{1}{2}|\vec{v}|^2$. Según el Primer Principio de la Termodinámica:
$$ \frac{d}{dt} E_{\text{total}} = \dot{W}_{\text{ext}} + \dot{Q}_{\text{ext}} $$

$$ \begin{aligned}
\frac{d}{dt}\left[\int_{V_f(t)} \rho\left(e + \frac{|\vec{v}|^2}{2}\right) dV\right] = & -\int_{\Sigma_f(t)} p\vec{v}\cdot\vec{n} \, d\sigma + \int_{\Sigma_f(t)} \vec{v}\cdot\bar{\bar{\tau}}'\cdot\vec{n} \, d\sigma + \int_{V_f(t)} \rho\vec{f}_m\cdot\vec{v} \, dV \\
& -\int_{\Sigma_f(t)} \vec{q}\cdot\vec{n} \, d\sigma + \int_{V_f(t)} (Q_c + Q_r) \, dV
\end{aligned} \qquad \text{[Ec. 3.45]} $$

### Para un Volumen de Control Móvil Arbitrario $V_c(t)$
Aplicando el Teorema de Transporte de Reynolds (Ec. 3.8):

$$ \begin{aligned}
\mathbf{\frac{d}{dt}\left[\int_{V_c(t)} \rho\left(e + \frac{|\vec{v}|^2}{2}\right) dV\right] + \int_{\Sigma_c(t)} \rho\left(e + \frac{|\vec{v}|^2}{2}\right)[(\vec{v}-\vec{v}_c)\cdot\vec{n}] \, d\sigma =} \\
\mathbf{-\int_{\Sigma_c(t)} p\vec{v}\cdot\vec{n} \, d\sigma + \int_{\Sigma_c(t)} \vec{v}\cdot\bar{\bar{\tau}}'\cdot\vec{n} \, d\sigma + \int_{V_c(t)} \rho\vec{f}_m\cdot\vec{v} \, dV} \\
\mathbf{-\int_{\Sigma_c(t)} \vec{q}\cdot\vec{n} \, d\sigma + \int_{V_c(t)} (Q_c + Q_r) \, dV}
\end{aligned} \qquad \text{[Ec. 3.46]} $$

### Desglose Físico Término a Término
1. **Acumulación No Estacionaria:** Variación de la energía cinética e interna almacenada en $V_c(t)$.
2. **Convección Neta Saliente:** Transporte convectivo de entalpía y energía cinética cruzando la superficie con velocidad relativa $(\vec{v}-\vec{v}_c)$.
3. **Trabajo de Presión ($-\int_{\Sigma_c} p\vec{v}\cdot\vec{n} d\sigma$):** Trabajo mecánico de flujo (*flow work*) ejercido por la presión externa sobre el fluido al entrar o salir del volumen. Al agruparlo con la energía interna convectada $e$, engendra la **entalpía específica** $h = e + p/\rho$ y la **entalpía total de remanso** $h_0 = h + \frac{|\vec{v}|^2}{2}$.
4. **Trabajo de Esfuerzos Viscosos ($\int_{\Sigma_c} \vec{v}\cdot\bar{\bar{\tau}}'\cdot\vec{n} d\sigma$):** Potencia transmitida por fricción en fronteras móviles (ej. álabes de turbina) y disipación viscosa.
5. **Potencia de Fuerzas Másicas ($\int_{V_c} \rho\vec{f}_m\cdot\vec{v} dV$):** Trabajo realizado por la gravedad o fuerzas centrífugas sobre las trayectorias de las partículas fluidas.
6. **Conducción Térmica en la Frontera ($-\int_{\Sigma_c} \vec{q}\cdot\vec{n} d\sigma$):** Calor molecular conducido a través de la pared según la Ley de Fourier (refrigeración activa de toberas regenerativas o choque térmico).
7. **Fuentes Volumétricas ($Q_c, Q_r$):**
   * $Q_c$: Calor liberado por reacciones químicas de combustión exotérmicas por unidad de volumen y tiempo (quema de queroseno / $\text{LOX}-\text{LH}_2$ en cámaras de empuje).
   * $Q_r = -\nabla\cdot\vec{q}_r$: Calentamiento o enfriamiento volumétrico por radiación térmica de gases incandescentes.
