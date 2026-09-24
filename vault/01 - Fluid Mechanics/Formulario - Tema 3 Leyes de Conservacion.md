---
materia: Fluid Mechanics
tema: "Tema 3: Conservation Laws"
tags:
  - formulario
  - prontuario
  - ecuaciones-clave
  - leyes-conservacion
  - reynolds
dificultad: media
---

# 📋 Formulario Maestro: Tema 3 — Leyes de Conservación (Integral Form)

> **Referencia Oficial:** *Notes.pdf* (Antonio L. Sánchez & Javier Rodríguez-Rodríguez, UC3M), Capítulo 3: *Conservation Laws*, Páginas 25–36.

---

## 📑 Tabla Completa de Ecuaciones Fundamentales (Ecs. 3.1 a 3.46)

| Ec. | Expresión Matemática | Significado Físico y Denominación | Hipótesis / Ámbito |
| :---: | :--- | :--- | :--- |
| **3.1** | $\Phi(t) = \int_{V_f(t)} \phi(\vec{x},t) dV$<br>$\phi = \rho, \, \rho\vec{v}, \, \rho\left(e + \frac{\|\vec{v}\|^2}{2}\right)$ | Definición de magnitud extensiva a partir de su densidad volumétrica intensiva $\phi$. | Sistema material fluido cerrado $V_f(t)$. |
| **3.2** | $\frac{d}{dt}\left[\int_{V_f(t)} \phi dV\right] = \lim_{\Delta t\to 0}\frac{1}{\Delta t}\left[\int_{V_f(t+\Delta t)}\phi(t+\Delta t)dV - \int_{V_f(t)}\phi(t)dV\right]$ | Definición formal de la derivada temporal ordinaria del volumen material fluido. | General. |
| **3.3** | $\lim_{\Delta t\to 0}\frac{1}{\Delta t}\left[\int_{V_f(t)}[\phi(t+\Delta t)-\phi(t)]dV + \int_{V_f(t+\Delta t)-V_f(t)}\phi(t+\Delta t)dV\right]$ | Desdoblamiento del límite en término interno y región incremental barrida por la frontera. | General. |
| **3.4** | $\lim_{\Delta t\to 0}\frac{1}{\Delta t}\int_{V_f(t)}[\phi(t+\Delta t)-\phi(t)]dV = \int_{V_f(t)}\frac{\partial\phi}{\partial t}dV$ | Límite del término interno: contribución de la no estacionariedad local (*unsteadiness*). | Taylor primer orden. |
| **3.5** | $\lim_{\Delta t\to 0}\frac{1}{\Delta t}\int_{V_f(t+\Delta t)-V_f(t)}\phi(t+\Delta t)dV = \int_{\Sigma_f(t)}\phi \vec{v}\cdot\vec{n}d\sigma$ | Límite del volumen barrido: flujo convectivo neto a través de la superficie de frontera $\Sigma_f(t)$. | Cinemática diferencial: $dV = (\vec{v}\Delta t)\cdot\vec{n}d\sigma$. |
| **3.6** | $\frac{d}{dt}\left[\int_{V_f(t)} \phi \, dV\right] = \int_{V_f(t)} \frac{\partial \phi}{\partial t} \, dV + \int_{\Sigma_f(t)} \phi \, \vec{v}\cdot\vec{n} \, d\sigma$ | **Teorema de Transporte de Reynolds (RTT)** para un volumen material fluido $V_f(t)$. | Volumen que sigue a las partículas fluidas. |
| **3.7** | $\frac{d}{dt}\left[\int_{V_c(t)} \phi \, dV\right] = \int_{V_c(t)} \frac{\partial \phi}{\partial t} \, dV + \int_{\Sigma_c(t)} \phi \, \vec{v}_c\cdot\vec{n} \, d\sigma$ | RTT aplicado a un volumen de control arbitrario móvil $V_c(t)$ con velocidad de frontera $\vec{v}_c$. | Geometría arbitraria en movimiento. |
| **3.8** | $\frac{d}{dt}\left[\int_{V_f(t)} \phi \, dV\right] = \frac{d}{dt}\left[\int_{V_c(t)} \phi \, dV\right] + \int_{\Sigma_c(t)} \phi \, (\vec{v} - \vec{v}_c)\cdot\vec{n} \, d\sigma$ | **RTT Universal:** Conexión entre la derivada material y el volumen de control móvil con velocidad relativa $(\vec{v} - \vec{v}_c)$. | Fundamental en análisis integral. |
| **3.9** | $\frac{d}{dt}\left[\int_{V_f(t)} \rho \, dV\right] = 0$ | Conservación de la masa en un volumen material cerrado. | Mecánica clásica no relativista. |
| **3.10** | $\frac{d}{dt}\left[\int_{V_c(t)} \rho \, dV\right] + \int_{\Sigma_c(t)} \rho (\vec{v} - \vec{v}_c)\cdot\vec{n} \, d\sigma = 0$ | **Conservación Integral de Masa (Continuidad)** para un volumen de control móvil arbitrario $V_c(t)$. | Aplicable a cualquier volumen móvil. |
| **3.11** | $\int_{V_0} \frac{\partial \rho}{\partial t} \, dV + \int_{\Sigma_0} \rho \vec{v}\cdot\vec{n} \, d\sigma = 0$ | Conservación de masa para un volumen de control fijo en el espacio ($V_0, \vec{v}_c = 0$). | Volumen indeformable e inmóvil. |
| **3.12** | $d\vec{F}_m = \rho \vec{f}_m(\vec{x},t) \, dV$ | Fuerza volumétrica (másica) que actúa sobre una partícula fluida elemental. | Fuerzas de largo alcance. |
| **3.13** | $\vec{f}_m = \vec{g} - \vec{a}_0 - \frac{d\vec{\Omega}}{dt}\wedge\vec{x} - \vec{\Omega}\wedge(\vec{\Omega}\wedge\vec{x}) - 2\vec{\Omega}\wedge\vec{v}$ | Fuerza másica neta en sistema de referencia no inercial (gravedad + 4 fuerzas de inercia). | Marco de referencia acelerado y rotatorio. |
| **3.14** | $\vec{g} - \vec{a}_0 - \vec{\Omega}\wedge(\vec{\Omega}\wedge\vec{x}) = -\nabla\left[-\vec{g}\cdot\vec{x} + \vec{a}_0\cdot\vec{x} - \frac{1}{2}\|\vec{\Omega}\wedge\vec{x}\|^2\right] = -\nabla U$ | Carácter conservativo de gravedad, traslación uniforme y centrífuga derivando del potencial $U$. | $\vec{a}_0$ y $\vec{\Omega}$ estacionarios. |
| **3.15** | $d\vec{F}_s = \vec{f}_n(\vec{n}, \vec{x}, t) \, d\sigma$ | Fuerza superficial de contacto (vector tensión o esfuerzo $\vec{f}_n$) sobre un elemento $d\sigma$. | Corto alcance (origen intermolecular). |
| **3.16** | $dA \vec{f}_n - dA_1 \vec{f}_1 - dA_2 \vec{f}_2 - dA_3 \vec{f}_3 = 0$ | Equilibrio dinámico de fuerzas en el tetraedro diferencial de Cauchy en el límite $h \to 0$. | Orden de magnitud: área $\gg$ volumen. |
| **3.17** | $\vec{f}_n = n_1 \vec{f}_1 + n_2 \vec{f}_2 + n_3 \vec{f}_3 = \vec{n}\cdot\bar{\bar{\tau}} = \bar{\bar{\tau}}\cdot\vec{n}$ | **Postulado de Cauchy:** Dependencia lineal entre el vector tensión $\vec{f}_n$ y el tensor $\bar{\bar{\tau}}$. | Medio continuo clásico. |
| **3.18** | $\bar{\bar{\tau}} = \begin{bmatrix} \tau_{11} & \tau_{12} & \tau_{13} \\ \tau_{21} & \tau_{22} & \tau_{23} \\ \tau_{31} & \tau_{32} & \tau_{33}\end{bmatrix}$ | Matriz de componentes del Tensor de Esfuerzos de Cauchy. | Sistema ortogonal cartesiano. |
| **3.19** | $\vec{f}_n = \begin{bmatrix} \tau_{11} & \tau_{12} & \tau_{13} \\ \tau_{12} & \tau_{22} & \tau_{23} \\ \tau_{13} & \tau_{23} & \tau_{33}\end{bmatrix}\cdot\vec{n}, \quad \tau_{ij} = \tau_{ji}$ | **Simetría del tensor de esfuerzos:** Demostrada por balance de momento angular en elemento cúbico ($dx\to 0$). | Ausencia de micro-pares volumétricos. |
| **3.20** | $\bar{\bar{\tau}}\cdot\vec{n} = \lambda \vec{n}$ | Ecuación de autovalores para las direcciones y tensiones principales (esfuerzo cortante nulo). | General para cualquier estado de esfuerzo. |
| **3.21** | $|\bar{\bar{\tau}} - \lambda \bar{\bar{I}}| = 0$ | Ecuación secular o característica con 3 raíces reales mutuamente ortogonales $(\lambda_1, \lambda_2, \lambda_3)$. | Garantizado por simetría de $\bar{\bar{\tau}}$. |
| **3.22** | $\vec{F}_s = \int_\Sigma \bar{\bar{\tau}}\cdot\vec{n} \, d\sigma$ | Resultante global de fuerzas superficiales sobre una superficie material $\Sigma$. | General. |
| **3.23** | $\int_\Sigma \bar{\bar{\tau}}\cdot\vec{n} \, d\sigma = \int_V (\nabla\cdot\bar{\bar{\tau}}) \, dV$ | Aplicación del Teorema de Gauss: la divergencia del tensor $\nabla\cdot\bar{\bar{\tau}}$ es la fuerza superficial por unidad de volumen. | Superficie cerrada que encierra volumen $V$. |
| **3.24** | $\rho dV \frac{D\vec{v}}{Dt} = (\nabla\cdot\bar{\bar{\tau}})dV + \rho\vec{f}_m dV$ | 2ª Ley de Newton aplicada a un elemento diferencial de fluido $dV$. | Elemento fluido infinitesimal. |
| **3.25** | $\rho \frac{D\vec{v}}{Dt} = \nabla\cdot\bar{\bar{\tau}} + \rho\vec{f}_m$ | **Ecuación diferencial de Cauchy para la cantidad de movimiento**. | Valida para cualquier medio continuo. |
| **3.26** | $\vec{f}_n = -p\vec{n}$ | Tensión puramente normal en un fluido en reposo o con movimiento de sólido rígido. | Fluido en reposo o sin deformación ($\bar{\bar{T}}_d=0$). |
| **3.27** | $\bar{\bar{\tau}} = -p \bar{\bar{I}}$ | Tensor de esfuerzos hidrostático (isotrópico, independiente de la orientación). | Estado estático o sin cizalladura. |
| **3.28** | $\bar{\bar{\tau}} = -p\bar{\bar{I}} + \bar{\bar{\tau}}'$ | Descomposición del tensor de esfuerzos en presión termodinámica esférica y tensor viscoso desviador $\bar{\bar{\tau}}'$. | General para cualquier fluido en movimiento. |
| **3.29** | $\tau'_{ij} = \alpha_{ijkl} \gamma_{kl}$ | Hipótesis de fluido newtoniano: relación constitutiva lineal entre tensiones viscosas y tasas de deformación. | Fluido newtoniano. |
| **3.30** | $\bar{\bar{\tau}}' = 2\mu\bar{\bar{T}}_d + \lambda(\nabla\cdot\vec{v})\bar{\bar{I}}$ | Ecuación constitutiva de Navier-Poisson en función de viscosidad dinámica $\mu$ y segunda viscosidad $\lambda$. | Fluido newtoniano isótropo. |
| **3.31** | $\bar{\bar{\tau}}' = 2\mu\bar{\bar{T}}_d + \left(\mu_B - \frac{2}{3}\mu\right)(\nabla\cdot\vec{v})\bar{\bar{I}}$ | **Ecuación canónica de Navier-Poisson** en función de la viscosidad volumétrica $\mu_B = \lambda + \frac{2}{3}\mu$. | Hipótesis de Stokes: $\mu_B \approx 0 \implies \lambda = -\frac{2}{3}\mu$. |
| **3.32** | $\vec{F} = -\int_\Sigma p\vec{n}d\sigma + \int_\Sigma \bar{\bar{\tau}}'\cdot\vec{n}d\sigma$ | **Fuerza aerodinámica resultante sobre cuerpo sumergido**: descompuesta en presión y fricción viscosa. | $\vec{n}$ saliente del cuerpo hacia el fluido. |
| **3.33** | $\vec{M}_{\vec{x}_0} = -\int_\Sigma (\vec{x}-\vec{x}_0)\wedge(p\vec{n})d\sigma + \int_\Sigma (\vec{x}-\vec{x}_0)\wedge(\bar{\bar{\tau}}'\cdot\vec{n})d\sigma$ | **Momento resultante sobre cuerpo sumergido** respecto a un centro de reducción $\vec{x}_0$. | Superficie mojada $\Sigma$. |
| **3.34** | $\frac{d}{dt}\left[\int_{V_f(t)}\rho\vec{v}dV\right] = -\int_{\Sigma_f(t)} p\vec{n}d\sigma + \int_{\Sigma_f(t)}\bar{\bar{\tau}}'\cdot\vec{n}d\sigma + \int_{V_f(t)}\rho\vec{f}_m dV$ | 2ª Ley de Newton para un volumen material fluido cerrado $V_f(t)$. | Masa fija de fluido. |
| **3.35** | $\frac{d}{dt}\left[\int_{V_c(t)}\rho\vec{v}dV\right] + \int_{\Sigma_c(t)}\rho\vec{v}[(\vec{v}-\vec{v}_c)\cdot\vec{n}]d\sigma = -\int_{\Sigma_c(t)} p\vec{n}d\sigma + \int_{\Sigma_c(t)}\bar{\bar{\tau}}'\cdot\vec{n}d\sigma + \int_{V_c(t)}\rho\vec{f}_m dV$ | **Conservación Integral de Cantidad de Movimiento** para volumen de control móvil arbitrario $V_c(t)$. | Fundamental para empuje y fuerzas aerodinámicas. |
| **3.36** | $\int_{V_0}\frac{\partial(\rho\vec{v})}{\partial t}dV + \int_{\Sigma_0}\rho\vec{v}(\vec{v}\cdot\vec{n})d\sigma = -\int_{\Sigma_0} p\vec{n}d\sigma + \int_{\Sigma_0}\bar{\bar{\tau}}'\cdot\vec{n}d\sigma + \int_{V_0}\rho\vec{f}_m dV$ | Conservación de cantidad de movimiento para volumen de control fijo en el espacio ($V_0, \vec{v}_c = 0$). | Cojinetes, toberas fijas, túneles de viento. |
| **3.37** | $\frac{d}{dt}\left[\int_{V_f(t)}\rho(\vec{x}-\vec{x}_0)\wedge\vec{v}dV\right] = -\int_{\Sigma_f}(\vec{x}-\vec{x}_0)\wedge(p\vec{n})d\sigma + \int_{\Sigma_f}(\vec{x}-\vec{x}_0)\wedge(\bar{\bar{\tau}}'\cdot\vec{n})d\sigma + \int_{V_f}\rho(\vec{x}-\vec{x}_0)\wedge\vec{f}_m dV$ | Conservación de momento cinético (angular) para un volumen material $V_f(t)$. | Sistema material de partículas. |
| **3.38** | $\frac{d}{dt}\left[\int_{V_c}\rho[(\vec{x}-\vec{x}_0)\wedge\vec{v}]dV\right] + \int_{\Sigma_c}\rho[(\vec{x}-\vec{x}_0)\wedge\vec{v}][(\vec{v}-\vec{v}_c)\cdot\vec{n}]d\sigma = \sum \vec{M}_{\vec{x}_0, \text{ext}}$ | **Conservación Integral de Momento Cinético** para volumen de control móvil $V_c(t)$. | Base de la ecuación de Euler en turbomaquinaria. |
| **3.39** | $d\dot{Q}_{\text{cond}} = q_n(\vec{n}, \vec{x}, t) \, d\sigma$ | Potencia térmica conducida a través del elemento diferencial $d\sigma$ en dirección $\vec{n}$. | Conducción molecular. |
| **3.40** | $q_n dA = q_1 dA_1 + q_2 dA_2 + q_3 dA_3$ | Balance de flujos térmicos en el tetraedro infinitesimal en el límite $h \to 0$. | Conducción en equilibrio local. |
| **3.41** | $q_n = \vec{q}\cdot\vec{n}$ | Relación de Cauchy térmica: el flujo escalar $q_n$ es la proyección del vector densidad de flujo térmico $\vec{q}$. | Medio continuo térmico. |
| **3.42** | $\dot{Q}_{\text{cond}} = \int_\Sigma \vec{q}\cdot\vec{n} \, d\sigma$ | Calor total conducido a través de una superficie finita $\Sigma$. | General. |
| **3.43** | $\int_\Sigma \vec{q}\cdot\vec{n}d\sigma = \int_V (\nabla\cdot\vec{q})dV$ | Teorema de Gauss: $\nabla\cdot\vec{q}$ representa la tasa de pérdida de calor conductivo por unidad de volumen. | Volumen cerrado $V$. |
| **3.44** | $\vec{q} = -k\nabla T$ | **Ley de Fourier de la conducción térmica**: linealidad e inversión con el gradiente de temperatura. | Medio continuo isótropo. |
| **3.45** | $\frac{d}{dt}\left[\int_{V_f(t)}\rho(e+\frac{\|\vec{v}\|^2}{2})dV\right] = -\int_{\Sigma_f}p\vec{v}\cdot\vec{n}d\sigma + \int_{\Sigma_f}\vec{v}\cdot\bar{\bar{\tau}}'\cdot\vec{n}d\sigma + \int_{V_f}\rho\vec{f}_m\cdot\vec{v}dV - \int_{\Sigma_f}\vec{q}\cdot\vec{n}d\sigma + \int_{V_f}(Q_c+Q_r)dV$ | **Primer Principio de la Termodinámica** para volumen material $V_f(t)$ (balance de energía total). | Sistema material cerrado. |
| **3.46** | $\frac{d}{dt}\left[\int_{V_c}\rho(e+\frac{\|\vec{v}\|^2}{2})dV\right] + \int_{\Sigma_c}\rho(e+\frac{\|\vec{v}\|^2}{2})[(\vec{v}-\vec{v}_c)\cdot\vec{n}]d\sigma = -\int_{\Sigma_c}p\vec{v}\cdot\vec{n}d\sigma + \int_{\Sigma_c}\vec{v}\cdot\bar{\bar{\tau}}'\cdot\vec{n}d\sigma + \int_{V_c}\rho\vec{f}_m\cdot\vec{v}dV - \int_{\Sigma_c}\vec{q}\cdot\vec{n}d\sigma + \int_{V_c}(Q_c+Q_r)dV$ | **Conservación Integral de Energía Total** para volumen de control móvil arbitrario $V_c(t)$. | Forma maestra del balance de energía. |
