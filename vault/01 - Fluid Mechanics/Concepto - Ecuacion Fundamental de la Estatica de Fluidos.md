---
materia: Fluid Mechanics
tema: "Tema 1: Estática de Fluidos"
tags:
  - teoria
  - estatica
  - presion
  - atmosfera-isa
dificultad: media
prerrequisitos:
  - "[[01 - Fluid Mechanics/Concepto - Hipotesis de Medio Continuo y Propiedades Termofisicas|Medio Continuo]]"
---

# 📖 Ecuación Fundamental de la Estática de Fluidos

> **Condición de reposo:** En un fluido en reposo ($\vec{v} = 0$), no existen gradientes de velocidad $\implies \tau_{ij} = 0$. Por tanto, **no existen esfuerzos cortantes**; el estado de tensiones es puramente normal e isótropo (presión escalar $p$).

---

## 🔍 1. Deducción Rigurosa de la Ecuación Diferencial

Consideremos un elemento cúbico diferencial de fluido de aristas $dx, dy, dz$ en reposo bajo la acción de un campo másico gravitatorio $\vec{g} = (0, 0, -g)$:

### 1.1 Fuerzas Superficiales de Presión
Sobre las caras perpendiculares al eje $z$:
* Cara inferior ($z$): $+ p \cdot dx dy \cdot \vec{k}$
* Cara superior ($z + dz$): $-\left(p + \frac{\partial p}{\partial z} dz\right) \cdot dx dy \cdot \vec{k}$
* Fuerza neta superficial en $z$:
  $$ dF_{s,z} = -\frac{\partial p}{\partial z} dx dy dz $$

Generalizando a las tres direcciones vectoriales:
$$ d\vec{F}_s = -\nabla p \cdot dV $$

### 1.2 Fuerzas Másicas de Volumen
$$ d\vec{F}_m = \rho \vec{g} \cdot dV $$

### 1.3 Condición de Equilibrio Estático ($\sum \vec{F} = 0$)
$$ -\nabla p \cdot dV + \rho \vec{g} \cdot dV = 0 $$

Dividiendo entre el volumen $dV$:
$$ \mathbf{\nabla p = \rho \vec{g}} $$

En componentes cartesianas con el eje $z$ vertical hacia arriba:
$$ \frac{\partial p}{\partial x} = 0, \quad \frac{\partial p}{\partial y} = 0, \quad \mathbf{\frac{dp}{dz} = -\rho g} $$

---

## 📐 2. Consecuencias Físicas Inmediatas

1. **Superficies Isóbaras ($p = \text{cte}$):**
   $$ dp = \nabla p \cdot d\vec{r} = \rho \vec{g} \cdot d\vec{r} = 0 \implies \vec{g} \cdot d\vec{r} = 0 $$
   *Las superficies de igual presión son siempre perpendiculares al vector de gravedad local $\vec{g}$ (es decir, horizontales en un campo gravitatorio uniforme).*
2. **Principio de Pascal:**
   Cualquier incremento de presión aplicado en un punto de un fluido incompresible en reposo se transmite íntegramente a todos los puntos del fluido.

---

## 🚀 3. Integración para Fluidos Incompresibles ($\rho = \text{cte}$)

$$ \int_{p_1}^{p_2} dp = -\rho g \int_{z_1}^{z_2} dz \implies p_2 - p_1 = -\rho g (z_2 - z_1) $$

Definiendo la profundidad $h = z_1 - z_2$ medida desde la superficie libre a presión atmosférica $p_{\text{atm}}$:
$$ \mathbf{p(h) = p_{\text{atm}} + \rho g h} $$

* **Presión manométrica (relativa):** $p_{\text{rel}} = p - p_{\text{atm}} = \rho g h$.
* **Presión absoluta:** $p_{\text{abs}} = p_{\text{atm}} + p_{\text{rel}}$.

---

## ✈️ 4. Atmósfera Estándar Internacional (ISA) — Modelo Troposférico

En la atmósfera, el aire es un gas ideal ($p = \rho R T$), por lo que la densidad varía con la altitud:
$$ \frac{dp}{dz} = -\rho g = -\frac{p}{RT} g \implies \frac{dp}{p} = -\frac{g}{R T(z)} dz $$

En la **Troposfera** (desde $z = 0$ hasta $11\,000\text{ m}$), la temperatura decrece linealmente con un gradiente térmico $\alpha = 6.5\times 10^{-3}\text{ K/m}$:
$$ T(z) = T_0 - \alpha z \quad (T_0 = 288.15\text{ K}) $$

### Integración:
$$ \ln\left(\frac{p}{p_0}\right) = -\frac{g}{R} \int_0^z \frac{dz}{T_0 - \alpha z} = \frac{g}{\alpha R} \ln\left(1 - \frac{\alpha z}{T_0}\right) $$

$$ \mathbf{p(z) = p_0 \left(1 - \frac{\alpha z}{T_0}\right)^{\frac{g}{\alpha R}}} $$

Con los valores estándar:
* $ \frac{g}{\alpha R} = \frac{9.80665}{0.0065 \times 287.05} \approx 5.25588 $
* Para la densidad:
  $$ \rho(z) = \rho_0 \left(1 - \frac{\alpha z}{T_0}\right)^{\frac{g}{\alpha R} - 1} = \rho_0 \left(1 - \frac{\alpha z}{T_0}\right)^{4.256} $$

---

## ⚠️ 5. Casos de Aceleración de Cuerpos Rígidos (Gravedad Aparente)
Si un depósito de fluido se desplaza con una aceleración lineal constante $\vec{a}$, el fluido no se deforma tras un tiempo inicial:
$$ \nabla p = \rho (\vec{g} - \vec{a}) = \rho \vec{g}_{\text{efectiva}} $$
Las isóbaras se inclinan un ángulo $\theta$ respecto a la horizontal:
$$ \tan\theta = \frac{a_x}{g + a_z} $$

---

## 🔗 Conceptos Relacionados
* `[[01 - Fluid Mechanics/Concepto - Manometria y Medida de Presion|Siguiente: Manometría y Cálculo de Presiones]]`
* `[[01 - Fluid Mechanics/Concepto - Fuerzas sobre Superficies Sumergidas y Centro de Presiones|Fuerzas Hidrostáticas]]`
