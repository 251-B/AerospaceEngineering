---
materia: Fluid Mechanics
tema: "Tema 1: Estática de Fluidos"
tags:
  - teoria
  - estatica
  - centro-de-presiones
  - compuertas
dificultad: alta
prerrequisitos:
  - "[[01 - Fluid Mechanics/Concepto - Ecuacion Fundamental de la Estatica de Fluidos|Ecuación Fundamental de la Estática]]"
---

# 📖 Fuerzas sobre Superficies Sumergidas y Centro de Presiones

> **Principio clave:** La fuerza hidrostática total sobre una superficie plana equivale a la presión evaluada en el **Centro de Gravedad (CG)** multiplicada por el área. Sin embargo, su punto de aplicación resultante, el **Centro de Presiones (CP)**, se encuentra **siempre por debajo** del CG debido a que la presión hidrostática crece con la profundidad.

---

## 📐 1. Superficies Planas Inclinadas

Consideremos una compuerta plana de área $A$ sumergida en un líquido de densidad $\rho$, inclinada un ángulo $\theta$ respecto a la superficie libre.
* Definimos el eje $y$ contenido en el plano de la compuerta con origen $y = 0$ en la intersección del plano con la superficie libre.
* La profundidad vertical de cualquier punto es $h = y \cdot \sin\theta$.

### 1.1 Magnitud de la Fuerza Resultante ($F_R$)
La presión relativa a una profundidad $h$ es $p = \rho g h = \rho g y \sin\theta$:
$$ F_R = \int_A p \, dA = \rho g \sin\theta \int_A y \, dA $$

Por definición de centro de gravedad (primer momento de área $\int_A y \, dA = y_{CG} \cdot A$):
$$ \mathbf{F_R = \rho g \sin\theta \, y_{CG} \cdot A = p_{CG} \cdot A} $$

*La fuerza neta es el producto de la presión hidrostática en el centroide por el área mojada total.*

---

## 🎯 2. Localización del Centro de Presiones ($x_{CP}, y_{CP}$)

Aplicando el principio de momentos (el momento de la fuerza resultante debe igualar la integral de los momentos de las presiones elementales):

### 2.1 Coordenada $y_{CP}$ (A lo largo de la inclinación)
$$ F_R \cdot y_{CP} = \int_A y \cdot (p \, dA) = \rho g \sin\theta \int_A y^2 \, dA $$
Recordando que $\int_A y^2 \, dA = I_{xx}$ es el segundo momento de inercia respecto al eje de la superficie libre ($y=0$).

Por el **Teorema de Steiner (ejes paralelos)**:
$$ I_{xx} = I_{xx,CG} + A \cdot y_{CG}^2 $$

Sustituyendo $F_R = \rho g \sin\theta \, y_{CG} A$:
$$ (\rho g \sin\theta \, y_{CG} A) \cdot y_{CP} = \rho g \sin\theta \left( I_{xx,CG} + A \, y_{CG}^2 \right) $$

Dividiendo entre $\rho g \sin\theta \, y_{CG} A$:
$$ \mathbf{y_{CP} = y_{CG} + \frac{I_{xx,CG}}{y_{CG} \cdot A}} $$

*Como $I_{xx,CG} > 0$, siempre se cumple estrictamente que $\mathbf{y_{CP} > y_{CG}}$ (el centro de presiones está más profundo que el baricentro).*

### 2.2 Coordenada lateral $x_{CP}$
$$ \mathbf{x_{CP} = x_{CG} + \frac{I_{xy,CG}}{y_{CG} \cdot A}} $$
*(Si la compuerta tiene al menos un eje de simetría perpendicular a $x$, el producto de inercia baricéntrico es nulo: $I_{xy,CG} = 0 \implies x_{CP} = x_{CG}$)*.

---

## 📊 3. Momentos de Inercia Baricéntricos Clásicos

| Geometría | Área ($A$) | $y_{CG}$ desde la base | $I_{xx,CG}$ (eje horizontal neutro) |
| :--- | :--- | :--- | :--- |
| **Rectángulo** ($b \times h$) | $b \cdot h$ | $h/2$ | $\frac{b \cdot h^3}{12}$ |
| **Círculo** (radio $R$) | $\pi R^2$ | $R$ | $\frac{\pi R^4}{4}$ |
| **Triángulo** (base $b$, altura $h$) | $\frac{b \cdot h}{2}$ | $h/3$ | $\frac{b \cdot h^3}{36}$ |

---

## 🌊 4. Superficies Curvas Sumergidas

Para superficies con curvatura (cilíndricas, esféricas, presas parabólicas), el cálculo directo de la integral vectorial $\int p \, d\vec{A}$ es tedioso. Se utiliza el **Método de Descomposición en Componentes**:

### Componente Horizontal ($F_H$):
Equivale a la fuerza hidrostática sobre la **proyección vertical ($A_v$)** de la superficie curva:
$$ \mathbf{F_H = p_{CG,v} \cdot A_v} $$
Su línea de acción pasa por el centro de presiones de dicha área proyectada plana.

### Componente Vertical ($F_V$):
Equivale al **peso del volumen de líquido (real o imaginario)** contenido entre la superficie curva y la superficie libre del líquido:
$$ \mathbf{F_V = \rho g \cdot V_{\text{fluido}}} $$
Su línea de acción pasa exactamente por el **centro de gravedad del volumen de líquido considerado**.

### Resultante y Dirección:
$$ F_R = \sqrt{F_H^2 + F_V^2}, \quad \tan\alpha = \frac{F_V}{F_H} $$

---

## 🔗 Práctica y Ejercicios
* `[[01 - Fluid Mechanics/Problema - Compuerta Sumergida Inclinada con Momento de Apertura|Problema Resuelto: Compuerta con Bisagra]]`
* `[[01 - Fluid Mechanics/Concepto - Principio de Arquimedes y Estabilidad de Cuerpos Flotantes|Siguiente: Principio de Arquímedes y Cuerpos Flotantes]]`
