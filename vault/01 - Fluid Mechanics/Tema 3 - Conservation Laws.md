---
materia: Fluid Mechanics
tema: "Tema 3: Conservation Laws (Integral Form)"
fuentes:
  - "Notes.pdf (Sánchez & Rodríguez-Rodríguez, UC3M), Capítulo 3, Págs. 25-36"
tags:
  - moc-tema
  - fluid-mechanics
  - leyes-conservacion
  - reynolds-transport
  - segundo-curso
dificultad: alta
---

# 🌊 Tema 3: Conservation Laws (Leyes de Conservación en Forma Integral)

> **Objetivo del tema:** Establecer los balances macroscópicos fundamentales de la mecánica de medios continuos aplicados a fluidos. Se deduce el Teorema de Transporte de Reynolds (RTT) que conecta la derivada temporal de una magnitud extensiva en un volumen material o fluido $V_f(t)$ con la evolución en un volumen de control arbitrario móvil $V_c(t)$ o fijo $V_0$. A partir de los principios físicos de conservación de masa, balance de cantidad de movimiento (2ª Ley de Newton), momento cinético y 1ª Ley de la Termodinámica (energía total), se formulan las ecuaciones integrales globales que gobiernan sistemas fluidos y cuerpos sumergidos en ingeniería aeroespacial (empuje de cohetes, motores de turbina, fuerzas aerodinámicas y balances térmicos).

---

## 📑 Índice de Contenidos del Capítulo 3

1. `[[01 - Fluid Mechanics/Concepto - Teorema de Transporte de Reynolds|1. Introducción y el Teorema de Transporte de Reynolds (RTT)]]`
   * Magnitudes extensivas e intensivas: $\phi = \rho, \rho\vec{v}, \rho(e + v^2/2)$.
   * Deducción matemática rigurosa por paso al límite $\Delta t \to 0$: desdoblamiento en término de no estacionariedad (unsteadiness) y flujo convectivo a través de la frontera.
   * Formulación para volumen material fluido $V_f(t)$ y extensión a volumen de control arbitrario móvil $V_c(t)$ con velocidad de frontera $\vec{v}_c(\vec{x},t)$.
   * Caso canónico del volumen de control fijo en el espacio ($V_0, \vec{v}_c = 0$).

2. `[[01 - Fluid Mechanics/Concepto - Conservacion Integral de Masa Momento y Energia|2. Conservación Integral de Masa (Continuidad)]]`
   * Principio de conservación para volumen fluido $V_f(t)$: $\frac{d}{dt}\int_{V_f}\rho dV = 0$.
   * Ecuación integral para volumen de control móvil $V_c(t)$ y fijo $V_0$.
   * Casos límite: flujo estacionario y fluido incompresible ($\rho = \text{cte}$). Balance de caudales másicos $\sum \dot{m}_{\text{in}} = \sum \dot{m}_{\text{out}}$.

3. `[[01 - Fluid Mechanics/Concepto - Tensor de Esfuerzos y Principio de Cauchy|3. Fuerzas Volumétricas (Másicas) y Superficiales]]`
   * Clasificación por radio de acción: largo alcance (fuerzas másicas $\rho\vec{f}_m dV$, gravedad, sistemas no inerciales con aceleración de arrastre $\vec{a}_0$, angular $\dot{\vec{\Omega}}\wedge\vec{x}$, centrífuga y Coriolis) vs corto alcance (fuerzas superficiales de origen molecular).
   * Potencial de fuerzas másicas conservativas: $\vec{g} - \vec{a}_0 - \vec{\Omega}\wedge(\vec{\Omega}\wedge\vec{x}) = -\nabla U$.
   * Vector tensión o esfuerzo superficial: $\vec{f}_n(\vec{n}, \vec{x}, t)$.

4. `[[01 - Fluid Mechanics/Concepto - Tensor de Esfuerzos y Principio de Cauchy|4. El Tensor de Esfuerzos de Cauchy]]`
   * Postulado de Cauchy y tetraedro infinitesimal: demostración de la dependencia lineal $\vec{f}_n = \bar{\bar{\tau}}\cdot\vec{n}$.
   * Simetría del tensor de esfuerzos ($\tau_{ij} = \tau_{ji}$) por balance de momento angular en elemento cúbico infinitesimal ($dx\to 0$).
   * Direcciones principales de esfuerzo y autovalores reales: $|\bar{\bar{\tau}} - \lambda\bar{\bar{I}}| = 0$.
   * Resultante de fuerzas superficiales sobre volumen finito y aplicación del teorema de Gauss: $\int_\Sigma \bar{\bar{\tau}}\cdot\vec{n} d\sigma = \int_V \nabla\cdot\bar{\bar{\tau}} dV$.
   * Balance en elemento fluido y ecuación diferencial preliminar del momento: $\rho \frac{D\vec{v}}{Dt} = \nabla\cdot\bar{\bar{\tau}} + \rho\vec{f}_m$.

5. `[[01 - Fluid Mechanics/Concepto - Ecuacion Constitutiva de Navier-Poisson|5. Ecuación Constitutiva de Navier-Poisson (Fluidos Newtonianos)]]`
   * Fluido en reposo o traslación/rotación rígida: estado hidrostático $\bar{\bar{\tau}} = -p\bar{\bar{I}}$.
   * Descomposición general: $\bar{\bar{\tau}} = -p\bar{\bar{I}} + \bar{\bar{\tau}}'$, donde $\bar{\bar{\tau}}'$ es el tensor de esfuerzos viscosos.
   * Hipótesis de fluido newtoniano isótropo: relación lineal constitutiva $\tau'_{ij} = \alpha_{ijkl} \gamma_{kl}$.
   * Coeficientes de viscosidad dinámica $\mu$ y segunda viscosidad $\lambda$: $\bar{\bar{\tau}}' = 2\mu\bar{\bar{T}}_d + \lambda(\nabla\cdot\vec{v})\bar{\bar{I}}$.
   * Viscosidad volumétrica o de bulto $\mu_B = \lambda + \frac{2}{3}\mu$ e hipótesis de Stokes ($\mu_B \approx 0 \implies \lambda = -2/3\mu$).
   * Comportamiento térmico de la viscosidad: gases ($\mu \propto T^{1/2}$) vs líquidos ($\mu$ decrece marcadamente con $T$).

6. `[[01 - Fluid Mechanics/Concepto - Conservacion Integral de Masa Momento y Energia|6. Fuerzas y Momentos sobre Cuerpos Sumergidos]]`
   * Fuerza aerodinámica/hidrodinámica neta $\vec{F}$ sobre cuerpo sumergido de superficie mojada $\Sigma$: desdoblamiento en integral de presión normal e integral de fricción tangencial.
   * Momento aerodinámico/hidrodinámico neto $\vec{M}_{x_0}$ respecto a un punto de referencia $\vec{x}_0$.
   * Sustentación ($L$), resistencia ($D$) y momento de cabeceo ($M$).

7. `[[01 - Fluid Mechanics/Concepto - Conservacion Integral de Masa Momento y Energia|7. Ecuación Integral de Cantidad de Movimiento (Momentum)]]`
   * 2ª Ley de Newton para volumen fluido $V_f(t)$: $\frac{d}{dt}\int_{V_f}\rho\vec{v}dV = \vec{F}_{\text{ext}}$.
   * Ecuación general para volumen de control arbitrario móvil $V_c(t)$ y fijo $V_0$.
   * Interpretación física rigurosa término a término: tasa de acumulación local, flujo convectivo neto saliente, fuerzas de presión superficiales, esfuerzos viscosos tangenciales y fuerzas másicas de volumen.
   * Aplicaciones aeroespaciales canónicas: cálculo del empuje propulsivo de cohetes y turborreactores, fuerza sobre álabes y deflexión de chorros.

8. `[[01 - Fluid Mechanics/Concepto - Conservacion Integral de Masa Momento y Energia|8. Ecuación Integral de Momento Cinético (Momento Angular)]]`
   * Conservación del momento cinético para $V_f(t)$ y $V_c(t)$ respecto a punto $\vec{x}_0$.
   * Ecuación de Euler para turbomáquinas: potencia específica y par transmitido en rotores, compresores y turbinas de aviación.

9. `[[01 - Fluid Mechanics/Concepto - Ley de Fourier y Conduccion Termica|9. Transferencia de Calor por Conducción y Ley de Fourier]]`
   * Flujo de calor por unidad de superficie $q_n(\vec{n}, \vec{x}, t)$.
   * Tetraedro de Cauchy térmico y deducción del vector densidad de flujo térmico $\vec{q}$: $q_n = \vec{q}\cdot\vec{n}$.
   * Pérdida de calor por conducción en volumen cerrado: $\int_\Sigma \vec{q}\cdot\vec{n}d\sigma = \int_V \nabla\cdot\vec{q} dV$.
   * Ley de Fourier: $\vec{q} = -k\nabla T$.
   * Conductividad térmica $k(T)$, difusividad térmica $\alpha = k/(\rho c_p)$, y número de Prandtl $\mathrm{Pr} = \nu/\alpha$.
   * Órdenes de magnitud en aire ($\mathrm{Pr}\approx 0.72$), agua ($\mathrm{Pr}\sim 2-8$), metales líquidos ($\mathrm{Pr}\ll 1$) y aceites de lubricación aeroespacial ($\mathrm{Pr}\gg 1$).

10. `[[01 - Fluid Mechanics/Concepto - Conservacion Integral de Masa Momento y Energia|10. Ecuación Integral de Conservación de Energía Total]]`
    * 1ª Ley de la Termodinámica para volumen material $V_f(t)$: tasa de variación de energía total (cinética + interna).
    * Potencia de las fuerzas exteriores: trabajo de presión normal, trabajo de esfuerzos viscosos y trabajo de fuerzas másicas.
    * Calor transferido: conducción térmica en la frontera ($\vec{q}\cdot\vec{n}$) y fuentes volumétricas internas de calor ($Q_c$: reacciones químicas de combustión, $Q_r$: radiación térmica).
    * Ecuación integral general para volumen de control móvil $V_c(t)$ y simplificación para volúmenes de control fijos en ingeniería aeronáutica.

11. `[[01 - Fluid Mechanics/Formulario - Tema 3 Leyes de Conservacion|11. Prontuario y Formulario Completo de Ecuaciones (3.1 a 3.46)]]`
    * Tabla completa de ecuaciones con referencia cruzada, hipótesis operativas y significado físico detallado.

---

## 📚 Ecuaciones Fundamentales del Capítulo (Notes.pdf, Ecs. 3.1–3.46)

### 1. Teorema de Transporte de Reynolds (RTT)
$$ \frac{d}{dt}\left[\int_{V_f(t)} \phi \, dV\right] = \int_{V_f(t)} \frac{\partial \phi}{\partial t} \, dV + \int_{\Sigma_f(t)} \phi \, \vec{v}\cdot\vec{n} \, d\sigma \qquad \text{[Ec. 3.6]} $$
$$ \frac{d}{dt}\left[\int_{V_c(t)} \phi \, dV\right] = \int_{V_c(t)} \frac{\partial \phi}{\partial t} \, dV + \int_{\Sigma_c(t)} \phi \, \vec{v}_c\cdot\vec{n} \, d\sigma \qquad \text{[Ec. 3.7]} $$
$$ \frac{d}{dt}\left[\int_{V_f(t)} \phi \, dV\right] = \frac{d}{dt}\left[\int_{V_c(t)} \phi \, dV\right] + \int_{\Sigma_c(t)} \phi \, (\vec{v} - \vec{v}_c)\cdot\vec{n} \, d\sigma \qquad \text{[Ec. 3.8]} $$

### 2. Conservación de Masa (Ecuación de Continuidad)
$$ \frac{d}{dt}\left[\int_{V_c(t)} \rho \, dV\right] + \int_{\Sigma_c(t)} \rho \, (\vec{v} - \vec{v}_c)\cdot\vec{n} \, d\sigma = 0 \qquad \text{[Ec. 3.10]} $$
$$ \int_{V_0} \frac{\partial \rho}{\partial t} \, dV + \int_{\Sigma_0} \rho \, \vec{v}\cdot\vec{n} \, d\sigma = 0 \qquad \text{[Ec. 3.11]} $$

### 3. Fuerzas Másicas, Esfuerzo de Cauchy y Ecuación Constitutiva
$$ \vec{f}_m = \vec{g} - \vec{a}_0 - \frac{d\vec{\Omega}}{dt}\wedge\vec{x} - \vec{\Omega}\wedge(\vec{\Omega}\wedge\vec{x}) - 2\vec{\Omega}\wedge\vec{v} \qquad \text{[Ec. 3.13]} $$
$$ \vec{f}_n = \bar{\bar{\tau}}\cdot\vec{n}, \quad \tau_{ij} = \tau_{ji}, \quad |\bar{\bar{\tau}} - \lambda\bar{\bar{I}}| = 0 \qquad \text{[Ecs. 3.17, 3.19, 3.21]} $$
$$ \bar{\bar{\tau}} = -p\bar{\bar{I}} + \bar{\bar{\tau}}' = -p\bar{\bar{I}} + 2\mu\bar{\bar{T}}_d + \left(\mu_B - \frac{2}{3}\mu\right)(\nabla\cdot\vec{v})\bar{\bar{I}} \qquad \text{[Ecs. 3.28, 3.31]} $$

### 4. Fuerzas sobre Cuerpos Sumergidos
$$ \vec{F} = -\int_\Sigma p\vec{n} \, d\sigma + \int_\Sigma \bar{\bar{\tau}}'\cdot\vec{n} \, d\sigma \qquad \text{[Ec. 3.32]} $$
$$ \vec{M} = -\int_\Sigma (\vec{x} - \vec{x}_0)\wedge(p\vec{n}) \, d\sigma + \int_\Sigma (\vec{x} - \vec{x}_0)\wedge(\bar{\bar{\tau}}'\cdot\vec{n}) \, d\sigma \qquad \text{[Ec. 3.33]} $$

### 5. Conservación de Cantidad de Movimiento y Momento Cinético
$$ \frac{d}{dt}\left[\int_{V_c(t)} \rho\vec{v} \, dV\right] + \int_{\Sigma_c(t)} \rho\vec{v}[(\vec{v}-\vec{v}_c)\cdot\vec{n}] \, d\sigma = -\int_{\Sigma_c(t)} p\vec{n} \, d\sigma + \int_{\Sigma_c(t)} \bar{\bar{\tau}}'\cdot\vec{n} \, d\sigma + \int_{V_c(t)} \rho\vec{f}_m \, dV \qquad \text{[Ec. 3.35]} $$
$$ \begin{aligned}
\frac{d}{dt}\left[\int_{V_c(t)} \rho(\vec{x}-\vec{x}_0)\wedge\vec{v} \, dV\right] + \int_{\Sigma_c(t)} \rho[(\vec{x}-\vec{x}_0)\wedge\vec{v}][(\vec{v}-\vec{v}_c)\cdot\vec{n}] \, d\sigma = \\
-\int_{\Sigma_c(t)} (\vec{x}-\vec{x}_0)\wedge(p\vec{n}) \, d\sigma + \int_{\Sigma_c(t)} (\vec{x}-\vec{x}_0)\wedge(\bar{\bar{\tau}}'\cdot\vec{n}) \, d\sigma + \int_{V_c(t)} \rho(\vec{x}-\vec{x}_0)\wedge\vec{f}_m \, dV
\end{aligned} \qquad \text{[Ec. 3.38]} $$

### 6. Ley de Fourier y Conservación de Energía Total
$$ \vec{q} = -k\nabla T, \quad q_n = \vec{q}\cdot\vec{n}, \quad \mathrm{Pr} = \frac{\nu}{\alpha} = \frac{\mu c_p}{k} \qquad \text{[Ecs. 3.41, 3.44]} $$
$$ \begin{aligned}
\frac{d}{dt}\left[\int_{V_c(t)} \rho\left(e + \frac{|\vec{v}|^2}{2}\right) dV\right] + \int_{\Sigma_c(t)} \rho\left(e + \frac{|\vec{v}|^2}{2}\right)[(\vec{v}-\vec{v}_c)\cdot\vec{n}] \, d\sigma = \\
-\int_{\Sigma_c(t)} p\vec{v}\cdot\vec{n} \, d\sigma + \int_{\Sigma_c(t)} \vec{v}\cdot\bar{\bar{\tau}}'\cdot\vec{n} \, d\sigma + \int_{V_c(t)} \rho\vec{f}_m\cdot\vec{v} \, dV - \int_{\Sigma_c(t)} \vec{q}\cdot\vec{n} \, d\sigma + \int_{V_c(t)} (Q_c + Q_r) \, dV
\end{aligned} \qquad \text{[Ec. 3.46]} $$

---

## 🔗 Notas Conceptuales Vinculadas
- `[[01 - Fluid Mechanics/Concepto - Teorema de Transporte de Reynolds|Concepto: Teorema de Transporte de Reynolds (RTT)]]`
- `[[01 - Fluid Mechanics/Concepto - Tensor de Esfuerzos y Principio de Cauchy|Concepto: Tensor de Esfuerzos de Cauchy y Fuerzas de Volumen]]`
- `[[01 - Fluid Mechanics/Concepto - Ecuacion Constitutiva de Navier-Poisson|Concepto: Ecuación Constitutiva de Navier-Poisson]]`
- `[[01 - Fluid Mechanics/Concepto - Ley de Fourier y Conduccion Termica|Concepto: Ley de Fourier, Conducción y Número de Prandtl]]`
- `[[01 - Fluid Mechanics/Concepto - Conservacion Integral de Masa Momento y Energia|Concepto: Conservación Integral de Masa, Momento y Energía]]`
- `[[01 - Fluid Mechanics/Formulario - Tema 3 Leyes de Conservacion|Formulario Maestro: Leyes de Conservación (Ecs. 3.1 a 3.46)]]`
