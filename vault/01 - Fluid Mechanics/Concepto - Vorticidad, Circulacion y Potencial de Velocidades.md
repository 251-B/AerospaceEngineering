---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - teoria
  - concepto-clave
  - vorticidad
  - circulacion
  - potencial-velocidades
dificultad: media
prerrequisitos: []
---

# 🌪️ Concepto: Vorticidad, Circulación y Potencial de Velocidades

> **Idea clave en una frase:** La vorticidad cuantifica la rotación microscópica local de las partículas fluidas, mientras que la circulación mide el movimiento macroscópico a lo largo de un circuito cerrado; cuando el flujo es irrotacional ($\vec{\omega} \equiv 0$), el campo vectorial de velocidades deriva de un potencial escalar $\phi$ ($\vec{v} = \nabla\phi$).

---

## 🎯 1. Circulación ($\Gamma$) a lo Largo de una Curva (Notes.pdf, Ecs. 2.29–2.31)

La **circulación** $\Gamma$ del campo de velocidades a lo largo de una curva orientada $L$ se define como la integral de línea:

$$ \Gamma = \int_L \vec{v} \cdot d\vec{l} \qquad \text{[Ec. 2.29]} $$

donde $d\vec{l}$ es el vector desplazamiento diferencial a lo largo de la curva. Físicamente, la circulación representa una medida acumulada del movimiento o transporte neto del fluido proyectado en la dirección tangencial de la curva.

Si la curva se parametriza mediante $\vec{x} = \vec{x}_l(\lambda)$ con $\lambda_1 \le \lambda \le \lambda_2$:
$$ d\vec{l} = \frac{d\vec{x}_l}{d\lambda} d\lambda \implies \Gamma = \int_{\lambda_1}^{\lambda_2} \vec{v}(\vec{x}_l(\lambda), t) \cdot \frac{d\vec{x}_l}{d\lambda} d\lambda \qquad \text{[Ec. 2.31]} $$

---

## 🌀 2. El Vector Vorticidad ($\vec{\omega}$) y el Teorema de Stokes (Notes.pdf, Ecs. 2.32–2.33)

Consideremos una curva cerrada simple $L$ que delimita una superficie orientada $\Sigma$ totalmente sumergida en el fluido continuo. Aplicando el **teorema de Stokes**:

$$ \mathbf{\Gamma = \oint_L \vec{v} \cdot d\vec{l} = \int_\Sigma (\nabla \wedge \vec{v}) \cdot \vec{n} \, d\sigma} \qquad \text{[Ec. 2.32]} $$

donde $\vec{n}$ es el vector unitario normal a la superficie $\Sigma$, orientado según la regla de la mano derecha respecto al sentido de recorrido de la curva $L$.

### Definición de Vorticidad
El vector **vorticidad** $\vec{\omega}$ se define como el rotacional del campo de velocidades:

$$ \mathbf{\vec{\omega} = \nabla \wedge \vec{v}} $$

### Significado Físico Local
Si reducimos la curva $L$ al contorno de un elemento de superficie diferencial infinitesimal $d\sigma$ de normal $\vec{n}$:
$$ \oint_L \vec{v} \cdot d\vec{l} = (\nabla \wedge \vec{v}) \cdot \vec{n} \, d\sigma = \vec{\omega} \cdot \vec{n} \, d\sigma \qquad \text{[Ec. 2.33]} $$

Por tanto, $(\nabla \wedge \vec{v}) \cdot \vec{n} = \omega_n$ es la **circulación por unidad de superficie orientada según $\vec{n}$**.  
En un punto dado, la circulación alcanza su valor máximo cuando el plano que contiene a la curva es perpendicular al vector vorticidad $\vec{\omega}$. Como se demostrará al descomponer el tensor de gradiente de velocidades, la velocidad angular de rotación de la partícula fluida como un sólido rígido es exactamente la mitad de la vorticidad:
$$ \vec{\Omega}_{\text{fluido}} = \frac{1}{2} \vec{\omega} = \frac{1}{2}(\nabla \wedge \vec{v}) $$

---

## 🌊 3. Flujo Irrotacional y Función Potencial de Velocidades ($\phi$) (Notes.pdf, Ec. 2.34)

Un flujo se denomina **irrotacional** cuando la vorticidad es idénticamente nula en todos los puntos del dominio fluido:

$$ \vec{\omega} = \nabla \wedge \vec{v} = 0 \quad \forall \vec{x} $$

Del cálculo vectorial se desprende que todo campo vectorial irrotacional admite la existencia de una función escalar $\phi(\vec{x}, t)$, denominada **potencial de velocidades**, tal que:

$$ \mathbf{\vec{v} = \nabla\phi} \qquad \text{[Ec. 2.34]} $$

* En cartesianas: $v_x = \frac{\partial\phi}{\partial x}, \quad v_y = \frac{\partial\phi}{\partial y}, \quad v_z = \frac{\partial\phi}{\partial z}$.
* En cilíndricas: $v_r = \frac{\partial\phi}{\partial r}, \quad v_\theta = \frac{1}{r}\frac{\partial\phi}{\partial \theta}, \quad v_z = \frac{\partial\phi}{\partial z}$.
* En esféricas: $v_r = \frac{\partial\phi}{\partial r}, \quad v_\theta = \frac{1}{r}\frac{\partial\phi}{\partial \theta}, \quad v_\phi = \frac{1}{r\sin\theta}\frac{\partial\phi}{\partial \phi}$.

### Ventaja Analítica Fundamental
El potencial de velocidades reemplaza la determinación de un campo vectorial de tres incógnitas $(v_1, v_2, v_3)$ por la resolución de un único campo escalar $\phi(\vec{x}, t)$. Si el fluido es además incompresible ($\nabla \cdot \vec{v} = 0$), el potencial satisface la **ecuación de Laplace**:
$$ \nabla \cdot (\nabla\phi) = \nabla^2\phi = 0 $$

---

## 🛩️ 4. Conexión Topológica del Dominio y Sustentación Aerodinámica

> [!IMPORTANT] Dominios Simplemente Conexos vs Múltiplemente Conexos (Notes.pdf, pág. 16)
> * Si la circulación alrededor de **cualquier** curva cerrada es cero, el flujo es necesariamente irrotacional.
> * **Sin embargo, lo contrario no siempre se cumple:** aunque $\nabla \wedge \vec{v} = 0$ en todo punto donde haya fluido, la circulación $\oint_L \vec{v}\cdot d\vec{l}$ alrededor de una curva cerrada puede ser **distinta de cero**.
>
> Esto ocurre cuando el dominio fluido es **múltiplemente conexo** (por ejemplo, el flujo exterior alrededor de un perfil alar o cilindro). La curva $L$ que rodea el obstáculo no puede contraerse continuamente hasta reducirse a un punto sin salirse del dominio fluido (es decir, sin atravesar el sólido). Como la superficie $\Sigma$ apoyada en $L$ no está totalmente contenida en el fluido, el teorema de Stokes no puede aplicarse a todo el interior.
>
> En aerodinámica, este fenómeno es la base física de la sustentación: la circulación no nula $\Gamma \neq 0$ alrededor del perfil alar genera una fuerza de sustentación perpendicular a la corriente libre proporcional a $\Gamma$ (**Teorema de Kutta-Joukowski**):
> $$ L' = \rho_\infty V_\infty \Gamma $$

---

## 🔗 Conceptos Relacionados
* `[[01 - Fluid Mechanics/Tema 2 - Flow Kinematics|Tema 2: Flow Kinematics]]`
* `[[01 - Fluid Mechanics/Concepto - Flujo Convectivo y Funcion de Corriente|Concepto: Función de Corriente]]`
* `[[01 - Fluid Mechanics/Concepto - Deformacion, Rotacion y Tensor de Velocidad de Deformacion|Concepto: Tensor de Deformación y Rotación]]`
