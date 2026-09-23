---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - teoria
  - concepto-clave
  - flujo-convectivo
  - funcion-de-corriente
dificultad: media
prerrequisitos: []
---

# 🌊 Concepto: Flujo Convectivo y Función de Corriente ($\psi$)

> **Idea clave en una frase:** El flujo convectivo cuantifica el transporte neto de masa, cantidad de movimiento y energía que atraviesa una superficie debido a la velocidad del fluido; para flujos planos incompresibles ($\nabla \cdot \vec{v} = 0$), la función de corriente $\psi(x, y)$ reduce el campo vectorial bidimensional a un escalar cuyas curvas de nivel son exactamente las líneas de corriente y cuyos saltos $\Delta\psi$ miden el caudal volumétrico circulante.

---

## 📦 1. Flujo Convectivo a través de Superficies (Notes.pdf, Ecs. 2.35–2.39)

La masa, la cantidad de movimiento y la energía viajan arrastradas por las partículas fluidas en su desplazamiento. Para formalizar de manera unificada este ritmo de transporte:

Definimos $\phi(\vec{x}, t)$ como una magnitud genérica del fluido expresada **por unidad de volumen**. La cantidad total de dicha magnitud contenida en un volumen $V$ es $\int_V \phi \, dV$.

### Deducción del Flujo a través de una Superficie Fija $\Sigma_0$
Consideremos una superficie orientada fija $\Sigma_0$ con vector unitario normal $\vec{n}$. En un intervalo infinitesimal $dt$, el volumen de fluido que cruza un elemento diferencial de área $d\sigma$ es el volumen del paralelepípedo de base $d\sigma$ y arista oblicua $\vec{v} dt$:

$$ dV_c = (\vec{v} \cdot \vec{n}) \, d\sigma \, dt $$

La cantidad de magnitud $\phi$ transportada a través de $d\sigma$ durante $dt$ es $\phi (\vec{v} \cdot \vec{n}) \, d\sigma \, dt$. Dividiendo entre $dt$ e integrando sobre toda la superficie $\Sigma_0$, se define el **flujo convectivo neto**:

$$ \mathbf{\Phi_{\text{conv}} = \int_{\Sigma_0} \phi \, \vec{v} \cdot \vec{n} \, d\sigma} \qquad \text{[Ec. 2.35]} $$

| Magnitud Extensiva | Densidad Volumétrica ($\phi$) | Vector / Tensor de Flujo Convectivo ($\phi\vec{v}$) | Flujo Total a través de $\Sigma_0$ |
| :--- | :--- | :--- | :--- |
| **Volumen** | $\phi = 1$ | $\vec{v}$ (vector caudal de volumen) | $Q = \int_{\Sigma_0} \vec{v} \cdot \vec{n} \, d\sigma$ (Caudal volumétrico, Ec. 2.36) |
| **Masa** | $\phi = \rho$ | $\rho\vec{v}$ (vector flujo de masa) | $\dot{m} = \int_{\Sigma_0} \rho \, \vec{v} \cdot \vec{n} \, d\sigma$ (Gasto másico) |
| **Cantidad de Movimiento** | $\phi = \rho\vec{v}$ | $\rho\vec{v}\vec{v}$ (tensor de flujo de momento) | $\int_{\Sigma_0} \rho\vec{v} (\vec{v} \cdot \vec{n}) \, d\sigma$ |
| **Energía Total** | $\phi = \rho\left(e + \frac{|\vec{v}|^2}{2}\right)$ | $\rho\left(e + \frac{|\vec{v}|^2}{2}\right)\vec{v}$ (vector flujo de energía) | $\dot{E} = \int_{\Sigma_0} \rho\left(e + \frac{|\vec{v}|^2}{2}\right) \vec{v} \cdot \vec{n} \, d\sigma$ |

### Teorema de Gauss y la Divergencia de la Velocidad
Si $\Sigma_0$ es una superficie cerrada que encierra un volumen de control fijo $V_0$:

$$ \oint_{\Sigma_0} \phi \, \vec{v} \cdot \vec{n} \, d\sigma = \int_{V_0} \nabla \cdot (\phi\vec{v}) \, dV \qquad \text{[Ec. 2.37]} $$

En el límite de un volumen infinitesimal diferencial, $\nabla \cdot (\phi\vec{v})$ representa la tasa neta de pérdida de la magnitud por unidad de volumen debido al flujo saliente.  
En particular, para $\phi = 1$, $\nabla \cdot \vec{v}$ representa físicamente la **tasa de dilatación volumétrica unitaria** (volumen neto que abandona la unidad de volumen por unidad de tiempo). Por tanto, para un fluido incompresible o líquido perfecto:

$$ \mathbf{\nabla \cdot \vec{v} = 0} \qquad \text{[Ec. 2.38]} $$

### Flujo Convectivo a través de Superficies Móviles
Si la superficie de control $\Sigma_c(t)$ se desplaza con una velocidad $\vec{v}_c(\vec{x}_c, t)$, el transporte neto depende de la **velocidad relativa** $(\vec{v} - \vec{v}_c)$ de las partículas fluidas respecto a la frontera de control:

$$ \Phi_{\text{conv}} = \int_{\Sigma_c(t)} \phi \, (\vec{v} - \vec{v}_c) \cdot \vec{n} \, d\sigma \qquad \text{[Ec. 2.39]} $$

---

## 🎯 2. La Función de Corriente ($\psi$) para Flujos Planos (Notes.pdf, Ecs. 2.40–2.45)

Para flujos bidimensionales planos en el plano cartesiano $x-y$, la condición de solenoidalidad $\nabla \cdot \vec{v} = 0$ adopta la forma:

$$ \frac{\partial v_x}{\partial x} + \frac{\partial v_y}{\partial y} = 0 \qquad \text{[Ec. 2.40]} $$

Esta relación diferencial exacta garantiza la existencia de un campo escalar $\psi(x, y, t)$, denominado **función de corriente**, definido mediante las derivadas cruzadas:

$$ \mathbf{v_x = \frac{\partial \psi}{\partial y}}, \qquad \mathbf{v_y = -\frac{\partial \psi}{\partial x}} \qquad \text{[Ec. 2.41]} $$

Sustituyendo directamente en la divergencia:
$$ \frac{\partial}{\partial x}\left(\frac{\partial \psi}{\partial y}\right) + \frac{\partial}{\partial y}\left(-\frac{\partial \psi}{\partial x}\right) = \frac{\partial^2 \psi}{\partial x \partial y} - \frac{\partial^2 \psi}{\partial y \partial x} \equiv 0 $$
La conservación de volumen queda así **automáticamente satisfecha** para cualquier función $\psi$.

---

## 📐 3. Propiedades Cinemáticas Fundamentales de $\psi$

### 1. Las Curvas de Nivel $\psi(x, y) = \text{constante}$ son Líneas de Corriente
A lo largo de una curva de nivel donde $\psi = \text{cte}$, su diferencial total es idénticamente cero:

$$ d\psi = \frac{\partial \psi}{\partial x} dx + \frac{\partial \psi}{\partial y} dy = -v_y dx + v_x dy = 0 \qquad \text{[Ec. 2.42]} $$

Reordenando algebraicamente los términos:
$$ \frac{dx}{v_x} = \frac{dy}{v_y} \qquad \text{[Ec. 2.43]} $$
lo cual coincide exactamente con la ecuación diferencial de las líneas de corriente en el plano bidimensional.

### 2. El Salto $\Delta\psi = \psi_2 - \psi_1$ Representa el Caudal Volumétrico Circulante
Consideremos dos líneas de corriente caracterizadas por los valores constantes $\psi_1$ y $\psi_2$, y tracemos una curva arbitraria que una el punto 1 sobre $\psi_1$ con el punto 2 sobre $\psi_2$. El incremento de la función de corriente entre ambos puntos es:

$$ \psi_2 - \psi_1 = \int_1^2 d\psi = \int_1^2 \left( -v_y dx + v_x dy \right) \qquad \text{[Ec. 2.44]} $$

Notando que a lo largo de la curva diferencial orientada $(dx, dy)$ el vector unitario normal satisface $\vec{n} dl = (dy, -dx)$, se deduce que $-v_y dx + v_x dy = \vec{v} \cdot \vec{n} dl$. Por consiguiente:

$$ \mathbf{\psi_2 - \psi_1 = \int_1^2 \vec{v} \cdot \vec{n} \, dl = Q'} \qquad \text{[Ec. 2.45]} $$

donde $Q'$ es el **caudal volumétrico que circula entre las dos superficies de corriente por unidad de longitud perpendicular al plano de movimiento** $[m^2/s]$.

---

## 🔗 Conceptos Relacionados
* `[[01 - Fluid Mechanics/Tema 2 - Flow Kinematics|Tema 2: Flow Kinematics]]`
* `[[01 - Fluid Mechanics/Concepto - Descripcion Euleriana vs Lagrangiana y Lineas de Flujo|Concepto: Líneas de Corriente]]`
* `[[01 - Fluid Mechanics/Concepto - Vorticidad, Circulacion y Potencial de Velocidades|Concepto: Potencial de Velocidades]]`
