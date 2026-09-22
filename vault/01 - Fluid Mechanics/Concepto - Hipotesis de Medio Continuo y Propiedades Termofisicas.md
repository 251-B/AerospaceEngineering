---
materia: Fluid Mechanics
tema: "Tema 1: Propiedades de los Fluidos"
tags:
  - teoria
  - medio-continuo
  - termofisica
dificultad: baja
prerrequisitos: []
---

# 📖 Hipótesis de Medio Continuo y Propiedades Termofísicas

> **Idea clave en una frase:** Un fluido se modela como un medio continuo cuando las escalas de longitud características del flujo son órdenes de magnitud mayores que el recorrido libre medio molecular, permitiendo definir propiedades puntuales locales continuas.

---

## 🎯 1. Fundamento Físico e Intuición

A nivel microscópico, la materia está formada por moléculas en perpetuo movimiento caótico colisionando entre sí. Sin embargo, para la inmensa mayoría de problemas de ingeniería aeronáutica (flujo alrededor de alas, tuberías de combustible, toberas a baja y media altitud), no es viable ni necesario modelar cada molécula individualmente.

Definimos un **Volumen Material Elemental ($\delta V$)** que cumpla:
$$ \delta V_{\text{micro}} \ll \delta V \ll \delta V_{\text{macro}} $$
* Debe ser suficientemente grande para contener millones de moléculas (evitando fluctuaciones estadísticas moleculares).
* Debe ser suficientemente pequeño frente a las dimensiones del cuerpo (perfil alar, diámetro de tobera) para poder considerarlo un "punto" matemático $\vec{x}$.

### Criterio del Número de Knudsen ($Kn$)
El número adimensional de Knudsen determina la validez del medio continuo:
$$ Kn = \frac{\lambda}{L} $$
* $ \lambda $: Recorrido libre medio de las moléculas $[\text{m}]$ (para aire al nivel del mar $\lambda \approx 68 \text{ nm}$).
* $ L $: Longitud característica macroscópica del cuerpo o flujo $[\text{m}]$.

| Rango de $Kn$ | Régimen | Modelo de Fluido |
| :--- | :--- | :--- |
| **$Kn < 0.01$** | **Medio Continuo (Continuum)** | **Ecuaciones de Navier-Stokes clásicas** (condición de no deslizamiento) |
| $0.01 < Kn < 0.1$ | Régimen de Deslizamiento (Slip flow) | Navier-Stokes con velocidad de deslizamiento en pared |
| $0.1 < Kn < 10$ | Régimen de Transición | Ecuación de Boltzmann |
| $Kn > 10$ | Gas Enrarecido / Flujo Molecular Libre | Dinámica molecular directa (DSMC) — Reentrada espacial en alta atmósfera |

---

## 📐 2. Propiedades Termofísicas Fundamentales

### 1. Densidad ($\rho$) y Peso Específico ($\gamma$)
La densidad puntual en el medio continuo se define como el límite estadístico:
$$ \rho(\vec{x}, t) = \lim_{\delta V \to \delta V^*} \frac{\delta m}{\delta V} \quad \left[\frac{\text{kg}}{\text{m}^3}\right] $$
El **peso específico** relaciona la masa con el campo gravitatorio local:
$$ \gamma = \rho \cdot g \quad \left[\frac{\text{N}}{\text{m}^3}\right] $$

### 2. Módulo de Elasticidad Volumétrica (Compresibilidad $K$)
Mide la resistencia del fluido a cambiar de volumen ante variaciones de presión:
$$ K = -v \left(\frac{\partial p}{\partial v}\right) = \rho \left(\frac{\partial p}{\partial \rho}\right) \quad [\text{Pa}] $$

* **Proceso Isotermo ($T = \text{cte}$):**
  $$ K_T = \rho \left(\frac{\partial p}{\partial \rho}\right)_T = p \quad \text{(para gas ideal)} $$
* **Proceso Isentrópico / Adiabático Reversible ($s = \text{cte}$):**
  $$ K_s = \rho \left(\frac{\partial p}{\partial \rho}\right)_s = \gamma_{\text{ad}} \cdot p \quad \text{(donde } \gamma_{\text{ad}} = c_p/c_v \text{ es el coeficiente adiabático)} $$

### 3. Velocidad del Sonido ($c$)
La velocidad a la que se propagan las perturbaciones infinitesimales de presión:
$$ c = \sqrt{\left(\frac{\partial p}{\partial \rho}\right)_s} = \sqrt{\frac{K_s}{\rho}} $$
Para un **gas ideal perfecto** ($p = \rho R T$):
$$ c = \sqrt{\gamma_{\text{ad}} R T} $$
*(Para aire: $\gamma_{\text{ad}} = 1.4$, $R = 287 \text{ J/(kg}\cdot\text{K)}$, a $T = 288.15\text{ K}$, $c \approx 340.3\text{ m/s}$)*.

---

## ⚠️ 3. Cuidado en Exámenes
> [!WARNING] ¿Cuándo un flujo es incompresible?
> ¡Un fluido incompresible no existe en la naturaleza! Lo que es incompresible es el **flujo**.  
> Criterio de flujo incompresible: Número de Mach $Ma = \frac{v}{c} < 0.3$.  
> Si $Ma < 0.3$, la variación relativa de densidad es $\frac{\Delta \rho}{\rho} < 5\%$, por lo que se asume $\rho = \text{constante}$.

---

## 🔗 Conceptos Relacionados
* `[[01 - Fluid Mechanics/Concepto - Viscosidad y Ley de Newton de la Viscosidad|Viscosidad y Esfuerzos Cortantes]]`
* `[[01 - Fluid Mechanics/Tema 1 - Propiedades y Estatica de Fluidos|Volver al Tema 1]]`
