---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics (Cinemática del Flujo)"
fuentes:
  - "Notes.pdf (Sánchez & Rodríguez-Rodríguez, UC3M), Capítulo 2, Págs. 9-24"
  - "slides_Chapters1-2.pdf, Diapositivas 2.0 a 2.24 y Figuras 3.8 a 3.16"
tags:
  - moc-tema
  - fluid-mechanics
  - cinematica
  - segundo-curso
dificultad: alta
---

# 🌊 Tema 2: Flow Kinematics (Cinemática del Flujo)

> **Objetivo del tema:** Describir la geometría y cinemática del movimiento de un fluido sin atender a las fuerzas que lo originan. Se introducen los sistemas de coordenadas ortogonales y sus operadores diferenciales, la distinción fundamental entre descripciones Lagrangiana y Euleriana, las líneas características del flujo (trayectorias, líneas de corriente, trazas), la derivada material, el campo de aceleración, los conceptos de vorticidad, circulación y potencial de velocidades, el flujo convectivo, la función de corriente bidimensional ($\psi$), y la descomposición del movimiento relativo en traslación, rotación rígida ($\bar{\bar{T}}_r$) y deformación pura ($\bar{\bar{T}}_d$).

---

## 📑 Índice de Contenidos del Capítulo 2

1. `[[01 - Fluid Mechanics/Concepto - Coordenadas Curvilineas y Operadores Diferenciales|1. Coordenadas Curvilíneas Ortogonales y Operadores Diferenciales]]`
   * Cartesianas, cilíndricas y esféricas: factores de escala $(h_1, h_2, h_3)$ y elementos diferenciales $d\vec{x}$.
   * Álgebra tensorial: producto diádico $\vec{a}\vec{b}$, contracción $\bar{\bar{A}}:\bar{\bar{B}}$, producto tensorial y producto vectorial vector-tensor $\vec{a}\wedge\bar{\bar{A}}$.
   * Fórmulas generales de gradiente $\nabla\Phi$, laplaciano $\nabla^2\Phi$, divergencia $\nabla\cdot\vec{a}$, rotacional $\nabla\wedge\vec{a}$, gradiente de vector $(\nabla\vec{a})_{ij}$ y divergencia de tensor $(\nabla\cdot\bar{\bar{A}})_i$.
   * Teorema general de Gauss: $\int_\Sigma (\vec{n}\circ\phi)d\sigma = \int_V (\nabla\circ\phi)dV$.

2. `[[01 - Fluid Mechanics/Concepto - Descripcion Euleriana vs Lagrangiana y Lineas de Flujo|2. Descripciones Euleriana y Lagrangiana & Líneas Características]]`
   * Enfoque Lagrangiano: trayectorias $\vec{x} = \vec{x}_T(\vec{x}_0, t)$, velocidad y aceleración por derivación directa.
   * Enfoque Euleriano: campo vectorial continuo $\vec{v}(\vec{x}, t)$.
   * Conceptos preliminares: flujo uniforme ($\vec{v}=\vec{v}(t)$), flujo estacionario ($\vec{v}=\vec{v}(\vec{x})$), relatividad respecto al observador y puntos de remanso ($\vec{v}=0$).
   * Trayectorias (path lines): integración de $d\vec{x}/dt = \vec{v}(\vec{x}, t)$ y eliminación de $t$.
   * Líneas fluidas, superficies fluidas ($Df/Dt = 0$) y volúmenes fluidos (conservación de masa).
   * Líneas de corriente (stream lines): tangentes al vector velocidad instantáneo ($dx/v_x = dy/v_y = dz/v_z$).
   * Superficies y tubos de corriente. Condición de coincidencia de trayectorias y líneas de corriente en flujos estacionarios.

3. `[[01 - Fluid Mechanics/Concepto - Derivada Material y Aceleracion del Fluido|3. Derivada Material y Campo de Aceleración]]`
   * Derivación matemática del operador material $D\phi/Dt = \partial\phi/\partial t + \vec{v}\cdot\nabla\phi$ (término local + término convectivo).
   * Aceleración de una partícula fluida: $\vec{a} = D\vec{v}/Dt = \partial\vec{v}/\partial t + \vec{v}\cdot(\nabla\vec{v})$.
   * Expresión intrínseca universal: $\vec{a} = \partial\vec{v}/\partial t + \nabla(|\vec{v}|^2/2) - \vec{v}\wedge(\nabla\wedge\vec{v})$.
   * Componentes en cartesianas vs sistemas curvilíneos.
   * Aceleración en sistemas de referencia no inerciales: traslación $\vec{a}_0$, aceleración angular $\dot{\vec{\Omega}}\wedge\vec{x}$, centrífuga $\vec{\Omega}\wedge(\vec{\Omega}\wedge\vec{x})$ y Coriolis $2\vec{\Omega}\wedge\vec{v}$.

4. `[[01 - Fluid Mechanics/Concepto - Vorticidad, Circulacion y Potencial de Velocidades|4. Vorticidad, Circulación y Potencial de Velocidades]]`
   * Circulación a lo largo de una curva: $\Gamma = \int_L \vec{v}\cdot d\vec{l}$.
   * Teorema de Stokes y definición de vorticidad: $\vec{\omega} = \nabla\wedge\vec{v}$. Significado físico como circulación por unidad de superficie.
   * Flujo irrotacional ($\vec{\omega} \equiv 0$) y potencial de velocidades: $\vec{v} = \nabla\phi$.
   * Dominios simplemente conexos vs múltiplemente conexos: circulación no nula alrededor de perfiles alares y generación de sustentación (Kutta-Joukowski).

5. `[[01 - Fluid Mechanics/Concepto - Flujo Convectivo y Funcion de Corriente|5. Flujo Convectivo y Función de Corriente (\psi)]]`
   * Transporte convectivo de magnitudes extensivas por unidad de volumen $\phi$: masa ($\rho\vec{v}$), cantidad de movimiento ($\rho\vec{v}\vec{v}$), energía ($\rho(e+v^2/2)\vec{v}$) y caudal volumétrico $Q = \int_\Sigma \vec{v}\cdot\vec{n}d\sigma$.
   * Divergencia de la velocidad $\nabla\cdot\vec{v}$ como tasa de dilatación volumétrica. Incompresibilidad: $\nabla\cdot\vec{v} = 0$.
   * Flujos a través de superficies móviles con velocidad relativa $(\vec{v} - \vec{v}_c)$.
   * Función de corriente plana $\psi(x, y)$: $v_x = \partial\psi/\partial y$, $v_y = -\partial\psi/\partial x$. Demostración de que las isolíneas $\psi = \text{cte}$ son líneas de corriente y que el salto $\Delta\psi = \psi_2 - \psi_1$ equivale al caudal por unidad de profundidad.

6. `[[01 - Fluid Mechanics/Concepto - Deformacion, Rotacion y Tensor de Velocidad de Deformacion|6. Cinemática de la Deformación: Tensores de Deformación y Rotación]]`
   * Movimiento relativo entre dos puntos próximos: $d\vec{v} = d\vec{x}\cdot\nabla\vec{v}$.
   * Descomposición de Helmholtz: $\nabla\vec{v} = \bar{\bar{T}}_d + \bar{\bar{T}}_r$.
   * Tensor velocidad de rotación $\bar{\bar{T}}_r$: antisimétrico, ligado a la vorticidad $d\vec{v}_r = \frac{1}{2}\vec{\omega}\wedge d\vec{x}$.
   * Tensor velocidad de deformación $\bar{\bar{T}}_d$: simétrico, elementos diagonales (tasas de extensión lineal) y no diagonales (mitad de la tasa de deformación angular o cizalladura).
   * Direcciones principales de deformación: problema de autovalores $\bar{\bar{T}}_d\cdot\vec{n} = \lambda\vec{n}$.
   * Deformación de elementos cuadrado y cúbico: demostración analítica de $\frac{1}{V}\frac{dV}{dt} = \nabla\cdot\vec{v} = \text{tr}(\bar{\bar{T}}_d)$.

---

## 📚 Ecuaciones Fundamentales del Capítulo (Notes.pdf)

$$ \vec{x} = \vec{x}_T(\vec{x}_0, t) \qquad \text{[Ec. 2.10: Trayectoria]} $$
$$ \frac{h_1 dx_1}{v_1} = \frac{h_2 dx_2}{v_2} = \frac{h_3 dx_3}{v_3} \qquad \text{[Ec. 2.21: Líneas de Corriente]} $$
$$ \frac{D\phi}{Dt} = \frac{\partial \phi}{\partial t} + \vec{v} \cdot \nabla \phi \qquad \text{[Ec. 2.24: Derivada Material]} $$
$$ \vec{a} = \frac{\partial \vec{v}}{\partial t} + \nabla\left(\frac{|\vec{v}|^2}{2}\right) - \vec{v} \wedge (\nabla \wedge \vec{v}) \qquad \text{[Ec. 2.26: Aceleración Intrínseca]} $$
$$ \Gamma = \oint_L \vec{v} \cdot d\vec{l} = \int_\Sigma (\nabla \wedge \vec{v}) \cdot \vec{n} d\sigma \qquad \text{[Ec. 2.32: Stokes y Vorticidad]} $$
$$ v_x = \frac{\partial \psi}{\partial y}, \quad v_y = -\frac{\partial \psi}{\partial x}, \quad Q' = \psi_2 - \psi_1 \qquad \text{[Ecs. 2.41, 2.45: Función de Corriente]} $$
$$ \nabla \vec{v} = \bar{\bar{T}}_d + \bar{\bar{T}}_r, \quad d\vec{v}_r = \frac{1}{2}\vec{\omega}\wedge d\vec{x}, \quad \nabla \cdot \vec{v} = \text{tr}(\bar{\bar{T}}_d) = \frac{1}{V}\frac{dV}{dt} \qquad \text{[Ecs. 2.47, 2.52, 2.62]} $$

---

## ✏️ Problemas Resueltos de Cinemática (Hoja Oficial de Exámenes)

Todos los problemas de la colección oficial de cinemática desarrollados paso a paso:
1. `[[01 - Fluid Mechanics/Problema - K1 Flujo sobre Pared Porosa Oscilante|Problema K1: Flujo sobre Pared Porosa Oscilante con Succión/Soplado]]`
2. `[[01 - Fluid Mechanics/Problema - K2 Flujo de Couette Plano|Problema K2: Flujo de Couette Plano y Análisis de Deformación / Rotación]]`
3. `[[01 - Fluid Mechanics/Problema - K3 Fuente Tridimensional en el Origen|Problema K3: Fuente Tridimensional Puntual en el Origen]]`
4. `[[01 - Fluid Mechanics/Problema - K4 Flujo Alrededor de Cuerpo de Rankine|Problema K4: Flujo Alrededor de un Semisólido de Rankine]]`
5. `[[01 - Fluid Mechanics/Problema - K5 Dipolo Plano Oscilante|Problema K5: Dipolo Plano Pulsante / Oscilante]]`
6. `[[01 - Fluid Mechanics/Problema - K6 Vortice Tridimensional de Burgers|Problema K6: Vórtice Tridimensional de Burgers con Estiramiento Axial]]`
7. `[[01 - Fluid Mechanics/Problema - K7 Flujo de Estancamiento Hiperbolico|Problema K7: Flujo de Estancamiento Hiperbólico Plano]]`
8. `[[01 - Fluid Mechanics/Problema - K8 Potencial Tridimensional Pulsante|Problema K8: Flujo Tridimensional Pulsante y Deformación Esférica]]`
9. `[[01 - Fluid Mechanics/Problema - K9 Flujo Polar Oscilante|Problema K9: Flujo Polar Oscilante y Deformación de una Línea Fluida]]`
10. `[[01 - Fluid Mechanics/Problema - K10 Flujo Plano con Cizalladura Exponencial|Problema K10: Flujo Plano con Cizalladura Exponencial y Deformación Pura]]`

