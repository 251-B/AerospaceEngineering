---
materia: Fluid Mechanics
tema: "Tema 1: Introductory Remarks and Starting Assumptions"
fuentes:
  - "Notes.pdf (Sánchez & Rodríguez-Rodríguez, UC3M), Capítulo 1, Págs. 1-8"
  - "slides_Chapters1-2.pdf, Diapositivas 1.0 a 1.8"
tags:
  - moc-tema
  - fluid-mechanics
  - segundo-curso
dificultad: baja
---

# 🌊 Tema 1: Introductory Remarks and Starting Assumptions

> **Objetivo del tema:** Establecer los fundamentos físicos y matemáticos que permiten tratar un fluido (compuesto por partículas discretas en movimiento aleatorio) como un **medio continuo** macroscópico, definiendo de forma rigurosa la partícula fluida, los campos de densidad, velocidad y energía interna, la hipótesis de equilibrio termodinámico local (Knudsen) y las ecuaciones de estado para líquidos y gases perfectos.

---

## 📑 Contenidos Teóricos del Capítulo

1. **Sólidos, Líquidos y Gases:**
   * Distinción mecánica fundamental: sólidos responden con deformación proporcional a la fuerza ($\tau \propto d\theta$); los fluidos responden con deformación continua a una tasa proporcional al esfuerzo cortante ($\tau \propto \frac{d\theta}{dt}$).
   * Líquidos vs Gases: densidad ($\rho_l \gg \rho_g$) y compresibilidad $(\partial \rho/\partial p)_{T,l} \ll (\partial \rho/\partial p)_{T,g}$.
   * Estructura microscópica: curva de fuerzas intermoleculares $F(d)$ con distancia de equilibrio $d_0 \approx 3\text{ \AA}$. Distancia media intermolecular $d = (W/\rho N_A)^{1/3}$ ($d_{\text{aire}} \approx 3.4\text{ nm} \sim 10 d_0$; $d_{\text{agua}} \approx 0.31\text{ nm} \sim d_0$).
2. **El Fluido como Medio Continuo y Partícula Fluida:**
   * La escala macroscópica $L$ (distancia sobre la que se aprecian variaciones significativas del flujo).
   * Definición de la partícula fluida ($\delta V$): condición de doble acotación $d \ll (\delta V)^{1/3} \ll L$ (Notes.pdf, Ec. 1.2).
   * La meseta de densidad (*plateau*): independencia de la densidad respecto al volumen elemental.
   * Límite de aplicabilidad del medio continuo: $d/L \ll 1$. Casos límite: reentrada espacial en atmósfera superior y micro/nanofluidos (MEMS).
3. **Definición de Campos Macroscópicos:**
   * Densidad: $\rho(\vec{x}, t) = \lim_{\delta V \to 0, (\delta V)^{1/3} \gg d} \frac{\sum m_i}{\delta V}$ (Ec. 1.3).
   * Velocidad del flujo: $\vec{v}(\vec{x}, t) = \lim \frac{\sum m_i \vec{v}_i}{\sum m_i}$ (velocidad del centro de masas, Ec. 1.4).
   * Descomposición de la energía total: $\lim \frac{\sum E_i}{\sum m_i} = e + \frac{|\vec{v}|^2}{2}$ (Ec. 1.5).
   * Energía interna: $e = \lim \frac{\sum m_i |\vec{v}_i - \vec{v}|^2/2 + E_{vi} + E_{ri} + \cdots}{\sum m_i}$ (agitación térmica desordenada + modos internos, base de la temperatura $T$, Ec. 1.6).
4. **Equilibrio Termodinámico Local (ETL / LTE):**
   * Mecanismo de restauración: colisiones moleculares en gases.
   * Recorrido libre medio $\lambda/d \simeq (d/d_0)^2$ ($\lambda \approx 0.4\ \mu\text{m}$ en aire a nivel del mar).
   * Tiempo entre colisiones $\tau = \lambda/a \approx 10^{-9}\text{ s}$.
   * Criterio de Knudsen: $Kn = \frac{\lambda}{L} \ll 1$ (Ec. 1.7) y $T_{\text{macro}} \gg \tau$.
   * $Kn \ll 1$ es más restrictivo que el de medio continuo ($d/L \ll 1$) porque en gases $\lambda \gg d$.
5. **Variables Termodinámicas y Ecuaciones de Estado:**
   * Relación de Gibbs: $de = T ds - p d(1/\rho) = T ds + \frac{p}{\rho^2} d\rho$ (Ec. 1.8).
   * Definiciones termodinámicas: $T = (\partial e/\partial s)_\rho$, $p = -(\partial e/\partial \rho^{-1})_s$, entalpía $h = e + p/\rho$.
   * **Líquido Perfecto:** $\rho = \rho_0 = \text{cte}$, $e = c T + e_0$, $h = c T + e_0 + p/\rho_0$, $s = c \ln T + s_0$ (Ecs. 1.11 a 1.14).
   * **Gas Perfecto:** $p/\rho = R_g T$, $R_g = R_0/W$, $e = c_v T + e_0$, $h = c_p T + e_0$, $s = c_v \ln(p/\rho^\gamma) + s_0$, $c_p = c_v + R_g$, $\gamma = 1.4$ para aire (Ecs. 1.15 a 1.18).

---

## 🔗 Nota Conceptual Detallada
* `[[01 - Fluid Mechanics/Concepto - Hipotesis de Medio Continuo y Propiedades Termofisicas|Ver Nota Teórica Exhaustiva del Tema 1]]`
