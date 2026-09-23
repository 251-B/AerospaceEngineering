---
materia: Fluid Mechanics
tema: "Tema 1: Estática de Fluidos"
tags:
  - teoria
  - manometria
  - presion
dificultad: media
prerrequisitos:
  - "[[01 - Fluid Mechanics/Concepto - Ecuacion Fundamental de la Estatica de Fluidos|Ecuación Fundamental de la Estática]]"
---

# 📖 Manometría y Sistemas Multilíquido

> **Regla de oro de la manometría:**  
> 1. Al descender en una columna de fluido continuo, la presión **aumenta**: $+ \rho g \Delta h$.  
> 2. Al ascender en una columna de fluido, la presión **disminuye**: $- \rho g \Delta h$.  
> 3. En un mismo fluido continuo y en reposo, dos puntos a la **misma cota horizontal** tienen idéntica presión: $p_A = p_B$.

---

## 🎯 1. Tipos de Presión y Escalas

* **Presión Atmosférica Local ($p_{\text{atm}}$):** Presión ejercida por el peso del aire atmosférico (medida con un barómetro de mercurio de Torricelli). Al nivel del mar estándar: $101\,325\text{ Pa} = 760\text{ mmHg} = 1.01325\text{ bar}$.
* **Presión Manométrica ($p_g$ o $p_{\text{rel}}$):** Referenciada a la atmósfera local ($p_{\text{rel}} = p_{\text{abs}} - p_{\text{atm}}$). Puede ser positiva o negativa (vacío).
* **Presión Absoluta ($p_{\text{abs}}$):** Referenciada al cero absoluto de presión (vacío perfecto, $p_{\text{abs}} \ge 0$).

---

## 📐 2. Dispositivos Manométricos Habituales

### 2.1 Tubo Piezométrico Simple
Tubo vertical abierto a la atmósfera conectado a un conducto con líquido a presión:
$$ p_A = p_{\text{atm}} + \rho g h \implies p_{A,\text{rel}} = \rho g h $$
*Limitación:* No sirve para gases (se escaparían) ni para presiones muy elevadas (requeriría tubos de decenas de metros) ni para presiones negativas (aspiraría aire).

### 2.2 Manómetro Diferencial en U
Mide la diferencia de presión $\Delta p = p_A - p_B$ entre dos puntos utilizando un fluido manométrico denso e inmiscible (habitualmente mercurio $\rho_{\text{Hg}} \approx 13\,600\text{ kg/m}^3$ o aceites específicos):

Ecuación de recorrido piezométrico desde el punto $A$ hasta el $B$:
$$ p_A + \rho_1 g h_1 - \rho_m g h_m - \rho_2 g h_2 = p_B $$
$$ \mathbf{p_A - p_B = \rho_m g h_m + \rho_2 g h_2 - \rho_1 g h_1} $$

### 2.3 Manómetro de Rama Inclinada (Alta Sensibilidad)
Para medir variaciones diminutas de presión en gases (ej: túneles de viento):
Al inclinar el tubo un ángulo $\theta$ respecto a la horizontal, el desplazamiento del menisco a lo largo del tubo ($L$) amplifica la altura vertical:
$$ h = L \cdot \sin\theta \implies \Delta p = \rho_m g L \sin\theta $$
El factor de amplificación de lectura es $\frac{1}{\sin\theta}$ (si $\theta = 5^\circ$, la escala se multiplica por $\approx 11.5$).

---

## ⚠️ 3. Errores Típicos en Problemas de Examen

> [!CAUTION] Los 3 Pecados Capitales en Manometría
> 1. **Saltar de una rama a otra a través de interfaces discontinuas:** Solo puedes igualar presiones $p_1 = p_2$ si ambos puntos están en el **mismo líquido continuo**. Si entre medias hay un menisco o un gas, la cota no es suficiente.
> 2. **Despreciar columnas de gas en grandes alturas:** En tuberías cortas de laboratorio, el peso del gas es despreciable ($\rho_{\text{aire}} \approx 1.2\text{ kg/m}^3 \ll \rho_{\text{agua}} = 1000$). Sin embargo, en chimeneas, pozos mineros o depósitos de alta presión, la columna de gas SÍ cuenta.
> 3. **Confundir densidad relativa ($SG$ o $s$) con densidad absoluta:**  
>    La gravedad específica es adimensional: $SG = \frac{\rho}{\rho_{\text{agua}}}$. Para el mercurio $SG = 13.6 \implies \rho = 13\,600\text{ kg/m}^3$.

---

## 🔗 Práctica y Ejercicios
* `[[01 - Fluid Mechanics/Problema - Manometro Diferencial Multiliquido con Gas|Resolver Problema Tipo Examen: Manómetro con Gas]]`
* `[[01 - Fluid Mechanics/Concepto - Fuerzas sobre Superficies Sumergidas y Centro de Presiones|Siguiente: Fuerzas sobre Compuertas y Presas]]`
