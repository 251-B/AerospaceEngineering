---
materia: Fluid Mechanics
tema: "Tema 3: Conservation Laws"
tags:
  - teoria
  - concepto-clave
  - tensor-esfuerzos
  - principio-cauchy
  - fuerzas-masicas
dificultad: alta
prerrequisitos:
  - "[[01 - Fluid Mechanics/Tema 2 - Flow Kinematics|Tema 2: Flow Kinematics]]"
---

# 🔬 Concepto: Tensor de Esfuerzos de Cauchy y Fuerzas de Volumen

> **Idea clave en una frase:** La interacción mecánica en un fluido se divide en fuerzas másicas de largo alcance que actúan sobre el volumen ($\vec{f}_m$) y fuerzas de contacto de corto alcance que actúan sobre la superficie; según el Principio de Cauchy, el vector tensión superficial $\vec{f}_n$ sobre cualquier orientación $\vec{n}$ queda unívocamente determinado por la proyección de un tensor simétrico de segundo orden $\bar{\bar{\tau}}$ ($\vec{f}_n = \bar{\bar{\tau}}\cdot\vec{n}$), cuya divergencia espacial $\nabla\cdot\bar{\bar{\tau}}$ representa la fuerza superficial resultante por unidad de volumen.

---

## 🌌 1. Clasificación Física de Fuerzas: Largo Alcance vs Corto Alcance

En la mecánica de fluidos macroscópica, las fuerzas que actúan sobre una partícula o elemento fluido se clasifican de acuerdo con su radio de acción intermolecular:

### A. Fuerzas Másicas o Volumétricas ($\vec{f}_m$) — Largo Alcance
Tienen un alcance macroscópico infinitamente superior a la distancia intermolecular media $d$. Actúan directamente sobre cada elemento de masa $dm = \rho dV$:

$$ d\vec{F}_m = \rho \vec{f}_m(\vec{x}, t) \, dV \qquad \text{[Ec. 3.12]} $$

Donde $\vec{f}_m$ es la fuerza por unidad de masa. En el caso más general de un **sistema de referencia no inercial** dotado de aceleración de traslación $\vec{a}_0(t)$ y velocidad angular instantánea $\vec{\Omega}(t)$, la fuerza másica neta incorpora la aceleración de la gravedad y las cuatro fuerzas ficticias de inercia:

$$ \mathbf{\vec{f}_m(\vec{x}, t) = \vec{g} - \vec{a}_0 - \frac{d\vec{\Omega}}{dt}\wedge\vec{x} - \vec{\Omega}\wedge(\vec{\Omega}\wedge\vec{x}) - 2\vec{\Omega}\wedge\vec{v}} \qquad \text{[Ec. 3.13]} $$

* $\vec{g}$: gravedad terrestre.
* $-\vec{a}_0$: inercia de traslación del sistema de referencia.
* $-\frac{d\vec{\Omega}}{dt}\wedge\vec{x}$: fuerza inercial azimutal o de Euler.
* $-\vec{\Omega}\wedge(\vec{\Omega}\wedge\vec{x})$: fuerza centrífuga aparente.
* $-2\vec{\Omega}\wedge\vec{v}$: fuerza de Coriolis (ortogonal a la velocidad relativa).

#### Potencial de Fuerzas Másicas Conservativas
Cuando la aceleración de arrastre $\vec{a}_0$ y la rotación $\vec{\Omega}$ son constantes, las fuerzas de gravedad, traslación lineal y centrífuga son estrictamente conservativas y derivan de un potencial escalar único $U(\vec{x})$:

$$ \vec{g} - \vec{a}_0 - \vec{\Omega}\wedge(\vec{\Omega}\wedge\vec{x}) = -\nabla U \qquad \text{[Ec. 3.14]} $$
$$ U(\vec{x}) = -\vec{g}\cdot\vec{x} + \vec{a}_0\cdot\vec{x} - \frac{1}{2}| \vec{\Omega}\wedge\vec{x} |^2 $$

### B. Fuerzas Superficiales — Corto Alcance
Tienen un radio de influencia de orden molecular ($d \sim 10^{-9}\text{ m}$). Se ejercen exclusivamente a través del área de contacto entre partículas fluidas adyacentes o entre el fluido y una pared sólida.
Dado un elemento diferencial de superficie $d\sigma$ con vector normal unitario $\vec{n}$ dirigido hacia el exterior, la fuerza superficial ejercida sobre el fluido viene dada por:

$$ d\vec{F}_s = \vec{f}_n(\vec{n}, \vec{x}, t) \, d\sigma \qquad \text{[Ec. 3.15]} $$

Donde $\vec{f}_n$ es el **vector tensión** o esfuerzo superficial (fuerza por unidad de superficie, unidades de $\text{N/m}^2$ o $\text{Pa}$). Por el principio de acción y reacción, $\vec{f}_{-n} = -\vec{f}_n$.

---

## 🔺 2. El Tetraedro de Cauchy y Deducción del Tensor de Esfuerzos (Notes.pdf, Ecs. 3.16–3.19)

El vector tensión $\vec{f}_n$ depende a priori de la posición $\vec{x}$, del tiempo $t$ y de la orientación angular del vector unitario $\vec{n} = (n_1, n_2, n_3)$. Cauchy demostró que dicha dependencia direccional es estrictamente lineal.

Consideremos un elemento infinitesimal de fluido en forma de tetraedro con tres caras ortogonales paralelas a los planos coordenados cartesianos de áreas $dA_1, dA_2, dA_3$ con normales exteriores $-\vec{e}_1, -\vec{e}_2, -\vec{e}_3$, y una cuarta cara inclinada u oblicua de área $dA$ con normal exterior unitaria arbitraria $\vec{n} = n_1\vec{e}_1 + n_2\vec{e}_2 + n_3\vec{e}_3$.

Por proyección geométrica elemental del tetraedro:
$$ dA_1 = n_1 dA, \quad dA_2 = n_2 dA, \quad dA_3 = n_3 dA $$
El volumen del tetraedro es de orden $dV \sim \frac{1}{6} h dA$, donde $h$ es la altura perpendicular a la cara oblicua.

Aplicando la 2ª Ley de Newton al tetraedro fluido:
$$ \rho dV \frac{D\vec{v}}{Dt} = \vec{f}_n dA + \vec{f}_{-e_1} dA_1 + \vec{f}_{-e_2} dA_2 + \vec{f}_{-e_3} dA_3 + \rho \vec{f}_m dV $$
Utilizando $\vec{f}_{-e_i} = -\vec{f}_{e_i} \equiv -\vec{f}_i$:
$$ \vec{f}_n dA - \vec{f}_1 dA_1 - \vec{f}_2 dA_2 - \vec{f}_3 dA_3 = \rho dV \left(\frac{D\vec{v}}{Dt} - \vec{f}_m\right) \qquad \text{[Ec. 3.16]} $$

Al tomar el límite cuando el tamaño del tetraedro tiende a cero ($h \to 0$):
* Las fuerzas superficiales escalan con el área de las caras: $\sim \mathcal{O}(dA) \sim \mathcal{O}(h^2)$.
* Las fuerzas de inercia y volumétricas escalan con el volumen: $\sim \mathcal{O}(dV) \sim \mathcal{O}(h^3)$.

Por tanto, al dividir por $dA$ y tomar el límite $h \to 0$, el miembro derecho desaparece de forma rigurosa:
$$ \vec{f}_n = n_1 \vec{f}_1 + n_2 \vec{f}_2 + n_3 \vec{f}_3 \qquad \text{[Ec. 3.17]} $$

Definiendo las componentes cartesianas del vector tensión sobre la cara perpendicular a $\vec{e}_i$ como:
$$ \vec{f}_i = \tau_{i1}\vec{e}_1 + \tau_{i2}\vec{e}_2 + \tau_{i3}\vec{e}_3 = \sum_{j=1}^3 \tau_{ij}\vec{e}_j $$
Donde $\tau_{ij}$ representa la fuerza por unidad de área en la dirección $\vec{e}_j$ que actúa sobre una cara cuya normal exterior apunta en la dirección $\vec{e}_i$.
Agrupando en notación matricial y tensorial:

$$ \mathbf{\vec{f}_n = \vec{n} \cdot \bar{\bar{\tau}} = \bar{\bar{\tau}} \cdot \vec{n}} \qquad \text{[Ec. 3.17, 3.19]} $$

Donde la matriz del **Tensor de Esfuerzos de Cauchy** $\bar{\bar{\tau}}$ viene dada por:

$$ \bar{\bar{\tau}} = \begin{bmatrix} \tau_{11} & \tau_{12} & \tau_{13} \\ \tau_{21} & \tau_{22} & \tau_{23} \\ \tau_{31} & \tau_{32} & \tau_{33} \end{bmatrix} \qquad \text{[Ec. 3.18]} $$

* **Tensiones normales ($\tau_{11}, \tau_{22}, \tau_{33}$):** Esfuerzos perpendiculares a la superficie (tracción o compresión).
* **Tensiones tangenciales o de cizalladura ($\tau_{ij}$ con $i \neq j$):** Esfuerzos rasantes o de fricción viscosa paralelos a la cara.

---

## ⚖️ 3. Simetría del Tensor de Esfuerzos ($\tau_{ij} = \tau_{ji}$) (Notes.pdf, Ec. 3.19)

Consideremos un elemento fluido cúbico diferencial de aristas $dx_1, dx_2, dx_3$ y centro en $\vec{x}$. Evaluemos el balance del momento angular respecto al eje que pasa por el centro del cubo paralelo a $\vec{e}_3$:

$$ I_3 \frac{d\omega_3}{dt} = \sum M_{3, \text{ext}} $$
* El momento de inercia del cubo es $I_3 = \frac{1}{12} \rho (dx_1 dx_2 dx_3)(dx_1^2 + dx_2^2) \sim \mathcal{O}(dx^5)$.
* Los momentos de las fuerzas másicas escalan con el volumen y el brazo: $\sim \mathcal{O}(dx^4)$.
* Las fuerzas tangenciales en las caras laterales generan momentos con brazo $\frac{dx_1}{2}$ y $\frac{dx_2}{2}$:
  * Fuerzas $\tau_{12}(dx_2 dx_3)$ en las caras $\pm x_1$ generan un par en sentido antihorario: $\tau_{12}(dx_2 dx_3) dx_1$.
  * Fuerzas $\tau_{21}(dx_1 dx_3)$ en las caras $\pm x_2$ generan un par en sentido horario: $-\tau_{21}(dx_1 dx_3) dx_2$.

El balance de momentos proporciona:
$$ (\tau_{12} - \tau_{21}) dx_1 dx_2 dx_3 = \mathcal{O}(dx^4) + \mathcal{O}(dx^5) $$
Dividiendo por el volumen diferencial $dV = dx_1 dx_2 dx_3$ y haciendo tender el tamaño a cero ($dx \to 0$):

$$ \mathbf{\tau_{12} = \tau_{21}, \quad \tau_{13} = \tau_{31}, \quad \tau_{23} = \tau_{32} \implies \bar{\bar{\tau}} = \bar{\bar{\tau}}^T} \qquad \text{[Ec. 3.19]} $$

El tensor de esfuerzos de Cauchy es **estrictamente simétrico** en ausencia de pares volumétricos internos distribuidos (hipótesis de Boltzmann / medio continuo no micropolar).

---

## 🧭 4. Direcciones Principales de Esfuerzo (Notes.pdf, Ecs. 3.20–3.21)

En cualquier punto del fluido existen orientaciones particulares $\vec{n}$ para las cuales la tensión superficial resultante es estrictamente normal a la cara, anulándose por completo las tensiones tangenciales de fricción ($\vec{f}_n \parallel \vec{n}$):

$$ \bar{\bar{\tau}} \cdot \vec{n} = \lambda \vec{n} \qquad \text{[Ec. 3.20]} $$

La condición de autovalores exige la anulación del determinante característico:

$$ \mathbf{|\bar{\bar{\tau}} - \lambda \bar{\bar{I}}| = 0} \qquad \text{[Ec. 3.21]} $$

Dado que $\bar{\bar{\tau}}$ es una matriz simétrica real ($3 \times 3$), el teorema espectral garantiza:
1. Existen tres raíces reales $\lambda_1, \lambda_2, \lambda_3$ denominadas **esfuerzos principales**.
2. Las correspondientes direcciones unitarias asociadas $(\vec{n}_1, \vec{n}_2, \vec{n}_3)$ son **mutuamente ortogonales**.
3. En el sistema de coordenadas de los ejes principales, el tensor se diagonaliza: $\bar{\bar{\tau}} = \text{diag}(\lambda_1, \lambda_2, \lambda_3)$.

---

## 📦 5. Resultante Superficial y Divergencia del Tensor (Notes.pdf, Ecs. 3.22–3.25)

La fuerza superficial total ejercida sobre el contorno $\Sigma$ de un volumen fluido viene dada por:

$$ \vec{F}_s = \int_\Sigma \vec{f}_n \, d\sigma = \int_\Sigma \bar{\bar{\tau}} \cdot \vec{n} \, d\sigma \qquad \text{[Ec. 3.22]} $$

Aplicando el teorema general de la divergencia (teorema de Gauss) para tensores de segundo orden:

$$ \mathbf{\int_\Sigma \bar{\bar{\tau}} \cdot \vec{n} \, d\sigma = \int_V (\nabla \cdot \bar{\bar{\tau}}) \, dV} \qquad \text{[Ec. 3.23]} $$

Donde en componentes cartesianas, la divergencia del tensor es el vector:
$$ (\nabla \cdot \bar{\bar{\tau}})_i = \sum_{j=1}^3 \frac{\partial \tau_{ji}}{\partial x_j} = \frac{\partial \tau_{1i}}{\partial x_1} + \frac{\partial \tau_{2i}}{\partial x_2} + \frac{\partial \tau_{3i}}{\partial x_3} $$

Evaluando el balance de cantidad de movimiento en un elemento diferencial $dV$:
$$ \rho dV \frac{D\vec{v}}{Dt} = (\nabla \cdot \bar{\bar{\tau}}) dV + \rho \vec{f}_m dV \qquad \text{[Ec. 3.24]} $$
Dividiendo por el volumen $dV$, se obtiene la **ecuación diferencial del momento de Cauchy**:

$$ \mathbf{\rho \frac{D\vec{v}}{Dt} = \nabla \cdot \bar{\bar{\tau}} + \rho \vec{f}_m} \qquad \text{[Ec. 3.25]} $$

Esta ecuación diferencial rige el movimiento dinámico de cualquier medio continuo deformable. Para cerrarla matemáticamente en fluidos, es imprescindible expresar $\bar{\bar{\tau}}$ en función de las variables cinemáticas y termodinámicas ($\vec{v}, p, T$), lo que conduce a la **ecuación constitutiva de Navier-Poisson**.
