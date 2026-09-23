---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - teoria
  - concepto-clave
  - calculo-vectorial
  - cinematica
dificultad: media
prerrequisitos: []
---

# 📐 Concepto: Coordenadas Curvilíneas Ortogonales y Operadores Diferenciales

> **Idea clave en una frase:** El uso de factores de escala métricos $(h_1, h_2, h_3)$ permite unificar y formular invariablemente los operadores diferenciales del cálculo vectorial (gradiente, divergencia, rotacional, laplaciano y derivadas tensoriales) en sistemas cartesianos, cilíndricos y esféricos.

---

## 🎯 1. Fundamento Físico y Geométrico

En mecánica de fluidos, la geometría del flujo o de los cuerpos confinados (tuberías, toberas de cohetes, perfiles alares, gotas oscilantes) determina la conveniencia de adoptar sistemas de coordenadas ortogonales adaptados a la simetría del problema:
* **Cartesianas $(x, y, z)$:** Flujos bidimensionales planos, canales rectos, capas límite planas.
* **Cilíndricas $(r, \theta, z)$:** Tuberías circulares, vórtices, chorros axilsimétricos, rotores de turbomaquinaria.
* **Esféricas $(r, \theta, \phi)$:** Flujo alrededor de gotas, burbujas o cuerpos esféricos en régimen lento (Stokes), ondas acústicas esféricas.

---

## 📐 2. Formulación Matemática Rigurosa y Factores de Escala

Consideramos una base ortonormal local $(\vec{e}_1, \vec{e}_2, \vec{e}_3)$ en cada punto del espacio. El vector desplazamiento diferencial de posición se expresa como:

$$ d\vec{x} = h_1 dx_1 \vec{e}_1 + h_2 dx_2 \vec{e}_2 + h_3 dx_3 \vec{e}_3 $$

donde los coeficientes métricos $(h_1, h_2, h_3)$ son los **factores de escala**:

| Sistema de Coordenadas | Coordenadas $(x_1, x_2, x_3)$ | Factores de Escala $(h_1, h_2, h_3)$ | Elemento Diferencial de Línea $d\vec{x}$ |
| :--- | :--- | :--- | :--- |
| **Cartesianas** | $(x, y, z)$ | $(1, 1, 1)$ | $(dx, dy, dz)$ |
| **Cilíndricas** | $(r, \theta, z)$ | $(1, r, 1)$ | $(dr, r d\theta, dz)$ |
| **Esféricas** | $(r, \theta, \phi)$ | $(1, r, r\sin\theta)$ | $(dr, r d\theta, r\sin\theta d\phi)$ |

Definiendo el determinante métrico $h = h_1 h_2 h_3$, el diferencial de volumen es $dV = h_1 h_2 h_3 dx_1 dx_2 dx_3 = h dx_1 dx_2 dx_3$.

---

## 🔍 3. Operadores Diferenciales en Coordenadas Generales (Notes.pdf, Ecs. 2.3–2.8)

### 1. Gradiente de un Campo Escalar $\Phi$ (Vector)
$$ \nabla\Phi = \left( \frac{1}{h_1}\frac{\partial \Phi}{\partial x_1}, \, \frac{1}{h_2}\frac{\partial \Phi}{\partial x_2}, \, \frac{1}{h_3}\frac{\partial \Phi}{\partial x_3} \right) \qquad \text{[Ec. 2.3]} $$

### 2. Laplaciano de un Campo Escalar $\Phi$ (Escalar)
$$ \nabla^2\Phi = \frac{1}{h_1 h_2 h_3} \left[ \frac{\partial}{\partial x_1}\left(\frac{h_2 h_3}{h_1}\frac{\partial \Phi}{\partial x_1}\right) + \frac{\partial}{\partial x_2}\left(\frac{h_1 h_3}{h_2}\frac{\partial \Phi}{\partial x_2}\right) + \frac{\partial}{\partial x_3}\left(\frac{h_1 h_2}{h_3}\frac{\partial \Phi}{\partial x_3}\right) \right] \qquad \text{[Ec. 2.4]} $$

### 3. Divergencia de un Campo Vectorial $\vec{a} = \sum_i a_i \vec{e}_i$ (Escalar)
$$ \nabla \cdot \vec{a} = \frac{1}{h_1 h_2 h_3} \left[ \frac{\partial}{\partial x_1}(h_2 h_3 a_1) + \frac{\partial}{\partial x_2}(h_1 h_3 a_2) + \frac{\partial}{\partial x_3}(h_1 h_2 a_3) \right] \qquad \text{[Ec. 2.5]} $$

### 4. Rotacional de un Campo Vectorial $\vec{a}$ (Vector)
$$ \nabla \wedge \vec{a} = \frac{1}{h_1 h_2 h_3} \begin{vmatrix} h_1 \vec{e}_1 & h_2 \vec{e}_2 & h_3 \vec{e}_3 \\ \frac{\partial}{\partial x_1} & \frac{\partial}{\partial x_2} & \frac{\partial}{\partial x_3} \\ h_1 a_1 & h_2 a_2 & h_3 a_3 \end{vmatrix} \qquad \text{[Ec. 2.6]} $$

Desarrollado en sus componentes:
$$ (\nabla \wedge \vec{a})_1 = \frac{1}{h_2 h_3}\left[ \frac{\partial(h_3 a_3)}{\partial x_2} - \frac{\partial(h_2 a_2)}{\partial x_3} \right] $$
$$ (\nabla \wedge \vec{a})_2 = \frac{1}{h_1 h_3}\left[ \frac{\partial(h_1 a_1)}{\partial x_3} - \frac{\partial(h_3 a_3)}{\partial x_1} \right] $$
$$ (\nabla \wedge \vec{a})_3 = \frac{1}{h_1 h_2}\left[ \frac{\partial(h_2 a_2)}{\partial x_1} - \frac{\partial(h_1 a_1)}{\partial x_2} \right] $$

### 5. Gradiente de un Campo Vectorial (Tensor de Segundo Orden)
$$ (\nabla\vec{a})_{ii} = \frac{1}{h_i}\frac{\partial a_i}{\partial x_i} + \sum_{k \neq i} \frac{a_k}{h_i h_k}\frac{\partial h_i}{\partial x_k} \qquad \text{[Ec. 2.7a]} $$
$$ (\nabla\vec{a})_{ij} = \frac{1}{h_i}\frac{\partial a_j}{\partial x_i} - \frac{a_i}{h_i h_j}\frac{\partial h_i}{\partial x_j} \quad (i \neq j) \qquad \text{[Ec. 2.7b]} $$

### 6. Divergencia de un Tensor de Segundo Orden $\bar{\bar{A}}$ (Vector)
$$ (\nabla \cdot \bar{\bar{A}})_i = \frac{h_i}{h}\sum_j \frac{\partial}{\partial x_j}\left( \frac{h A_{ij}}{h_i h_j} \right) + \sum_j \frac{A_{ij} + A_{ji}}{h_i h_j}\frac{\partial h_i}{\partial x_j} - \sum_j \frac{A_{jj}}{h_i h_j}\frac{\partial h_j}{\partial x_i} \qquad \text{[Ec. 2.8]} $$

---

## ⚠️ 4. Errores Típicos en Exámenes

> [!WARNING] Cuidado con las Derivadas de los Vectores Unitarios
> En coordenadas curvilíneas (cilíndricas y esféricas), los vectores directores $\vec{e}_r, \vec{e}_\theta, \vec{e}_\phi$ **cambian de dirección con la posición**. No se puede derivar un vector componente a componente como en cartesianas. Por ejemplo, en cilíndricas:
> $$ \frac{\partial \vec{e}_r}{\partial \theta} = \vec{e}_\theta, \qquad \frac{\partial \vec{e}_\theta}{\partial \theta} = -\vec{e}_r $$
> Omitir estos términos al calcular aceleraciones o divergencias tensoriales es el fallo más frecuente en exámenes.

---

## 🔗 Conceptos Relacionados
* `[[01 - Fluid Mechanics/Tema 2 - Flow Kinematics|Tema 2: Flow Kinematics]]`
* `[[01 - Fluid Mechanics/Concepto - Derivada Material y Aceleracion del Fluido|Concepto: Derivada Material y Aceleración]]`
