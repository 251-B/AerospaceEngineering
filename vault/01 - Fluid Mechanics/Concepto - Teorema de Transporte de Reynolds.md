---
materia: Fluid Mechanics
tema: "Tema 3: Conservation Laws"
tags:
  - teoria
  - concepto-clave
  - reynolds-transport
  - volumen-control
  - euler-lagrange
dificultad: alta
prerrequisitos:
  - "[[01 - Fluid Mechanics/Tema 2 - Flow Kinematics|Tema 2: Flow Kinematics]]"
---

# 🔬 Concepto: Teorema de Transporte de Reynolds (RTT)

> **Idea clave en una frase:** El Teorema de Transporte de Reynolds es el puente cinemático fundamental entre la perspectiva Lagrangiana (leyes físicas aplicadas a un volumen material o fluido cerrado $V_f(t)$) y la perspectiva Euleriana (balances en un volumen de control arbitrario abierto $V_c(t)$ o fijo $V_0$), desdoblando la variación temporal global en una tasa de acumulación local interna y un flujo convectivo neto a través de la superficie de control.

---

## 🎯 1. Magnitudes Extensivas e Intensivas (Notes.pdf, Ec. 3.1)

En la mecánica clásica, las leyes de conservación fundamentales (masa, segunda ley de Newton, momento cinético, primer principio de la termodinámica) se postulan para **sistemas materiales cerrados** (una masa de fluido fija $M$ compuesta invariablemente por las mismas partículas fluidas que ocupan un volumen deformable $V_f(t)$ delimitado por una superficie fluida $\Sigma_f(t)$).

Sea $\Phi(t)$ una propiedad extensiva global del sistema fluido (tal como la masa total, el momento lineal o la energía total). Dicha magnitud puede expresarse como la integral de volumen de una magnitud intensiva por unidad de volumen $\phi(\vec{x}, t)$:

$$ \Phi(t) = \int_{V_f(t)} \phi(\vec{x}, t) \, dV \qquad \text{[Ec. 3.1]} $$

Donde la densidad volumétrica $\phi$ adopta los valores canónicos:
* **Masa:** $\phi = \rho$
* **Cantidad de movimiento (Momentum):** $\phi = \rho \vec{v}$
* **Momento cinético respecto a $\vec{x}_0$:** $\phi = \rho [(\vec{x} - \vec{x}_0) \wedge \vec{v}]$
* **Energía total:** $\phi = \rho \left(e + \frac{|\vec{v}|^2}{2}\right)$

Dado que tanto el integrando $\phi(\vec{x}, t)$ como el dominio de integración $V_f(t)$ varían continuamente con el tiempo, la derivada temporal ordinaria $\frac{d\Phi}{dt}$ no puede evaluarse introduciendo directamente la derivada parcial dentro de la integral.

---

## 📐 2. Deducción Matemática Rigurosa por Paso al Límite (Notes.pdf, Ecs. 3.2–3.6)

Por definición formal de derivada temporal ordinaria:

$$ \frac{d}{dt}\left[\int_{V_f(t)} \phi(\vec{x}, t) \, dV\right] = \lim_{\Delta t \to 0} \frac{1}{\Delta t} \left[ \int_{V_f(t + \Delta t)} \phi(\vec{x}, t + \Delta t) \, dV - \int_{V_f(t)} \phi(\vec{x}, t) \, dV \right] \qquad \text{[Ec. 3.2]} $$

Descomponiendo el dominio en el instante $t + \Delta t$ en la región común $V_f(t)$ y la región incremental barrida por la frontera $V_f(t + \Delta t) - V_f(t)$, el límite se desdobla exactamente en dos sumandos:

$$ \lim_{\Delta t \to 0} \frac{1}{\Delta t} \left[ \int_{V_f(t)} \left[\phi(\vec{x}, t + \Delta t) - \phi(\vec{x}, t)\right] dV + \int_{V_f(t + \Delta t) - V_f(t)} \phi(\vec{x}, t + \Delta t) \, dV \right] \qquad \text{[Ec. 3.3]} $$

### Término 1: No estacionariedad local (Unsteadiness)
En el primer sumando, el dominio $V_f(t)$ es independiente de $\Delta t$. Expandiendo en serie de Taylor:
$$ \phi(\vec{x}, t + \Delta t) - \phi(\vec{x}, t) = \frac{\partial \phi}{\partial t} \Delta t + \mathcal{O}(\Delta t^2) $$
Dividiendo por $\Delta t$ y tomando el límite $\Delta t \to 0$:
$$ \lim_{\Delta t \to 0} \frac{1}{\Delta t} \int_{V_f(t)} \left[\phi(\vec{x}, t + \Delta t) - \phi(\vec{x}, t)\right] dV = \int_{V_f(t)} \frac{\partial \phi}{\partial t} \, dV \qquad \text{[Ec. 3.4]} $$

### Término 2: Flujo convectivo a través de la frontera móvil
En el segundo sumando, durante el intervalo diferencial $\Delta t$, cada elemento de superficie $d\sigma$ de $\Sigma_f(t)$ con vector normal exterior $\vec{n}$ se desplaza a la velocidad del fluido $\vec{v}(\vec{x}, t)$. El elemento de volumen barrido es un cilindro oblicuo de base $d\sigma$ y altura $(\vec{v} \Delta t)\cdot\vec{n}$:
$$ dV = (\vec{v} \Delta t) \cdot \vec{n} \, d\sigma $$
Sustituyendo en la integral e integrando sobre toda la superficie cerrada $\Sigma_f(t)$:
$$ \lim_{\Delta t \to 0} \frac{1}{\Delta t} \int_{V_f(t + \Delta t) - V_f(t)} \phi(\vec{x}, t + \Delta t) \, dV = \int_{\Sigma_f(t)} \phi \, \vec{v}\cdot\vec{n} \, d\sigma \qquad \text{[Ec. 3.5]} $$

### Ecuación de Reynolds para un Volumen Fluido $V_f(t)$
Sumando ambas contribuciones se obtiene la forma clásica del Teorema de Transporte de Reynolds:

$$ \mathbf{\frac{d}{dt}\left[\int_{V_f(t)} \phi(\vec{x}, t) \, dV\right] = \int_{V_f(t)} \frac{\partial \phi}{\partial t} \, dV + \int_{\Sigma_f(t)} \phi \, \vec{v}\cdot\vec{n} \, d\sigma} \qquad \text{[Ec. 3.6]} $$

> [!NOTE] Dualidad Física: No Estacionariedad vs Movimiento
> * **Primer término ($\int_{V_f} \frac{\partial \phi}{\partial t} dV$):** Tasa de variación intrínseca de la propiedad dentro del volumen instantáneo debida al carácter no estacionario del flujo (*flow unsteadiness*).
> * **Segundo término ($\int_{\Sigma_f} \phi \vec{v}\cdot\vec{n} d\sigma$):** Tasa neta de ganancia o pérdida producida por la deformación y traslación convectiva de la frontera en el espacio (*fluid motion*).

---

## 🔄 3. Extensión a Volumen de Control Móvil Arbitrario $V_c(t)$ (Notes.pdf, Ecs. 3.7–3.8)

En la práctica de la ingeniería aeroespacial (por ejemplo, el interior de la cámara de combustión de un cohete o la tobera de un turbofán), no resulta conveniente seguir un volumen material fluido que se deforma y estira indefinidamente aguas abajo. Conviene definir una región geométrica arbitraria en el espacio: un **volumen de control** $V_c(t)$ delimitado por una superficie de control $\Sigma_c(t)$, cuya frontera se desplaza a una velocidad arbitraria prescrita $\vec{v}_c(\vec{x}, t)$.

Aplicando el mismo razonamiento cinemático de paso al límite al volumen geométrico $V_c(t)$:

$$ \frac{d}{dt}\left[\int_{V_c(t)} \phi(\vec{x}, t) \, dV\right] = \int_{V_c(t)} \frac{\partial \phi}{\partial t} \, dV + \int_{\Sigma_c(t)} \phi \, \vec{v}_c\cdot\vec{n} \, d\sigma \qquad \text{[Ec. 3.7]} $$

Elijamos ahora, en el instante genérico $t$, un volumen de control $V_c(t)$ cuya superficie coincida de forma instantánea y exacta con el volumen material fluido $V_f(t)$ ($\Sigma_c(t) \equiv \Sigma_f(t)$ y $V_c(t) \equiv V_f(t)$). Las integrales de volumen de $\partial\phi/\partial t$ en (3.6) y (3.7) resultan idénticas. Restando directamente ambas expresiones:

$$ \mathbf{\frac{d}{dt}\left[\int_{V_f(t)} \phi \, dV\right] = \frac{d}{dt}\left[\int_{V_c(t)} \phi \, dV\right] + \int_{\Sigma_c(t)} \phi \, (\vec{v} - \vec{v}_c)\cdot\vec{n} \, d\sigma} \qquad \text{[Ec. 3.8]} $$

> [!IMPORTANT] Teorema de Transporte de Reynolds Universal
> La ecuación 3.8 es la herramienta matemática fundamental de todo el análisis integral de fluidos. Establece que la tasa de cambio de cualquier propiedad física contenida en el sistema material $V_f(t)$ es igual a:
> 1. La tasa de variación temporal de dicha magnitud almacenada en el volumen de control $V_c(t)$.
> 2. Más el flujo convectivo neto saliente de dicha magnitud a través de la superficie de control $\Sigma_c(t)$, transportado por la **velocidad relativa del fluido respecto a la frontera de control** $(\vec{v} - \vec{v}_c)$.

---

## ⚙️ 4. Casos Particulares de Interés Práctico

### A. Volumen de Control Fijo en el Espacio ($V_0, \vec{v}_c = 0$)
Si el volumen de control no se deforma ni se mueve ($\vec{v}_c \equiv 0$ y $V_c(t) \equiv V_0$ con superficie $\Sigma_0$ fija):
$$ \frac{d}{dt}\left[\int_{V_f(t)} \phi \, dV\right] = \frac{d}{dt}\left[\int_{V_0} \phi \, dV\right] + \int_{\Sigma_0} \phi \, \vec{v}\cdot\vec{n} \, d\sigma = \int_{V_0} \frac{\partial \phi}{\partial t} \, dV + \int_{\Sigma_0} \phi \, \vec{v}\cdot\vec{n} \, d\sigma $$

### B. Volumen que Acompaña al Fluido ($\vec{v}_c = \vec{v}$)
Si la frontera del volumen de control se mueve localmente con el propio fluido ($\vec{v}_c = \vec{v}$), la velocidad relativa es nula $(\vec{v} - \vec{v}_c = 0)$, recuperándose trivialmente la derivada del volumen fluido:
$$ \frac{d}{dt}\left[\int_{V_c(t)} \phi \, dV\right] = \frac{d}{dt}\left[\int_{V_f(t)} \phi \, dV\right] $$

### C. Forma Diferencial Local por Teorema de Gauss
Aplicando el teorema de la divergencia al flujo de superficie en (3.6) para un volumen material:
$$ \int_{\Sigma_f(t)} \phi \vec{v}\cdot\vec{n} d\sigma = \int_{V_f(t)} \nabla \cdot (\phi\vec{v}) \, dV $$
Sustituyendo en (3.6):
$$ \frac{d}{dt}\left[\int_{V_f(t)} \phi \, dV\right] = \int_{V_f(t)} \left[ \frac{\partial \phi}{\partial t} + \nabla \cdot (\phi\vec{v}) \right] dV $$
Recordando la identidad $\nabla \cdot (\phi\vec{v}) = \vec{v}\cdot\nabla\phi + \phi\nabla\cdot\vec{v}$ y la derivada material $\frac{D\phi}{Dt} = \frac{\partial\phi}{\partial t} + \vec{v}\cdot\nabla\phi$:
$$ \frac{d}{dt}\left[\int_{V_f(t)} \phi \, dV\right] = \int_{V_f(t)} \left[ \frac{D\phi}{Dt} + \phi(\nabla \cdot \vec{v}) \right] dV $$
Al tomar el límite de una partícula elemental de volumen $dV$, con $\phi = \rho$:
$$ \frac{d}{dt}(\rho dV) = \left[\frac{D\rho}{Dt} + \rho(\nabla \cdot \vec{v})\right] dV = 0 $$
lo cual demuestra de forma transparente la equivalencia exacta entre la conservación macroscópica de masa y la ecuación diferencial de continuidad $\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\vec{v}) = 0$.

---

## 🚀 5. Aplicaciones en Ingeniería Aeroespacial

1. **Empuje de Cohetes y Toberas Propulsivas:** Elección de volúmenes de control que cortan ortogonalmente la sección de salida de la tobera ($\vec{v}_c = 0$ o $\vec{v}_c = \vec{v}_{\text{cohete}}$), permitiendo calcular la fuerza de empuje directamente integrando el flujo de momento $(\rho\vec{v})(\vec{v}-\vec{v}_c)\cdot\vec{n} d\sigma$ sin necesidad de resolver el campo turbulento interno completo.
2. **Propagación de Ondas de Choque Móviles:** Selección de un volumen de control que viaja fijado a la discontinuidad de choque a velocidad constante $\vec{v}_c = \vec{D}_{\text{choque}}$, transformando un problema transitorio no estacionario en un balance algebraico estacionario unidimensional (relaciones de Rankine-Hugoniot).
3. **Pistones y Alabes Móviles en Turbomáquinas:** Modelización de cavidades de compresores axiales y bombas centrífugas donde las paredes se mueven periódicamente a velocidad angular $\vec{v}_c = \vec{\Omega}\wedge\vec{x}$.
