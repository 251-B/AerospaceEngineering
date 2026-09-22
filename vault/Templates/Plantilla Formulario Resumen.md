---
materia: ""
tema: ""
tags:
  - formulario
  - prontuario
  - repaso-rapido
---

# 📋 Prontuario / Cheat Sheet: {{title}}

## ⚡ Ecuaciones Fundamentales

| Concepto / Ley | Ecuación en LaTeX | Condiciones / Hipótesis |
| :--- | :--- | :--- |
| **Continuidad** | $ \frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \vec{v}) = 0 $ | General |
| **Navier-Stokes** | $ \rho \frac{D\vec{v}}{Dt} = -\nabla p + \mu \nabla^2 \vec{v} + \rho \vec{g} $ | Newtoniano, $\mu = \text{cte}$ |
| **Bernoulli** | $ p + \frac{1}{2}\rho v^2 + \rho g z = \text{cte} $ | Estacionario, incompresible, no viscoso, a lo largo de una línea de corriente |

---

## 📐 Constantes y Factores de Conversión Habituales
* Aceleración de la gravedad: $ g = 9.80665 \text{ m/s}^2 $
* Densidad del aire estándar (ISA a nivel del mar): $ \rho_0 = 1.225 \text{ kg/m}^3 $
* Presión estándar: $ p_0 = 101325 \text{ Pa} = 1 \text{ atm} $

---

## 💡 Trucos de Cálculo Rápido y Simplificaciones
* En fluidos líquidos con variaciones de cota moderadas: $\Delta p = \rho g h$.
* Para flujos con $Ma < 0.3$: considerar siempre incompresible con excelente precisión.
