---
materia: Fluid Mechanics
tema: "Topic 1: Fluid Statics"
tags:
  - theory
  - manometry
  - pressure
dificultad: medium
prerrequisitos:
  - "[[01 - Fluid Mechanics/Concept - Fundamental Equation of Fluid Statics|Fundamental Equation of Statics]]"
---

# 📖 Manometry and Multi-Liquid Systems

> **Golden rule of manometry:**  
> 1. Descending in a continuous fluid column, the pressure **increases**: $+ \rho g \Delta h$.  
> 2. Ascending in a fluid column, the pressure **decreases**: $- \rho g \Delta h$.  
> 3. In the same continuous fluid at rest, two points at the **same horizontal level** have identical pressure: $p_A = p_B$.

---

## 🎯 1. Types of Pressure and Scales

* **Local Atmospheric Pressure ($p_{\text{atm}}$):** Pressure exerted by the weight of the atmospheric air (measured with a Torricelli mercury barometer). At standard sea level: $101\,325\text{ Pa} = 760\text{ mmHg} = 1.01325\text{ bar}$.
* **Gauge Pressure ($p_g$ or $p_{\text{rel}}$):** Referenced to the local atmosphere ($p_{\text{rel}} = p_{\text{abs}} - p_{\text{atm}}$). It can be positive or negative (vacuum).
* **Absolute Pressure ($p_{\text{abs}}$):** Referenced to absolute zero pressure (perfect vacuum, $p_{\text{abs}} \ge 0$).

---

## 📐 2. Common Manometric Devices

### 2.1 Simple Piezometer Tube
Vertical tube open to the atmosphere connected to a pipe with liquid under pressure:
$$ p_A = p_{\text{atm}} + \rho g h \implies p_{A,\text{rel}} = \rho g h $$
*Limitation:* It is not suitable for gases (they would escape), nor for very high pressures (it would require tubes tens of metres long), nor for negative pressures (it would draw in air).

### 2.2 Differential U-Tube Manometer
It measures the pressure difference $\Delta p = p_A - p_B$ between two points using a dense, immiscible manometric fluid (usually mercury $\rho_{\text{Hg}} \approx 13\,600\text{ kg/m}^3$ or specific oils):

Piezometric path equation from point $A$ to point $B$:
$$ p_A + \rho_1 g h_1 - \rho_m g h_m - \rho_2 g h_2 = p_B $$
$$ \mathbf{p_A - p_B = \rho_m g h_m + \rho_2 g h_2 - \rho_1 g h_1} $$

### 2.3 Inclined-Limb Manometer (High Sensitivity)
To measure tiny pressure variations in gases (e.g. wind tunnels):
When the tube is inclined at an angle $\theta$ with respect to the horizontal, the displacement of the meniscus along the tube ($L$) amplifies the vertical height:
$$ h = L \cdot \sin\theta \implies \Delta p = \rho_m g L \sin\theta $$
The reading amplification factor is $\frac{1}{\sin\theta}$ (if $\theta = 5^\circ$, the scale is multiplied by $\approx 11.5$).

---

## ⚠️ 3. Typical Mistakes in Exam Problems

> [!CAUTION] The 3 Deadly Sins of Manometry
> 1. **Jumping from one limb to another across discontinuous interfaces:** You may only equate pressures $p_1 = p_2$ if both points are in the **same continuous liquid**. If there is a meniscus or a gas in between, the elevation alone is not sufficient.
> 2. **Neglecting gas columns over large heights:** In short laboratory pipes, the weight of the gas is negligible ($\rho_{\text{air}} \approx 1.2\text{ kg/m}^3 \ll \rho_{\text{water}} = 1000$). However, in chimneys, mine shafts or high-pressure tanks, the gas column DOES count.
> 3. **Confusing relative density ($SG$ or $s$) with absolute density:**  
>    The specific gravity is dimensionless: $SG = \frac{\rho}{\rho_{\text{water}}}$. For mercury $SG = 13.6 \implies \rho = 13\,600\text{ kg/m}^3$.

---

## 🔗 Practice and Exercises
* [[01 - Fluid Mechanics/Problem - Multi-Liquid Differential Manometer with Gas|Solve an Exam-Style Problem: Manometer with Gas]]
* [[01 - Fluid Mechanics/Concept - Forces on Submerged Surfaces and Center of Pressure|Next: Forces on Gates and Dams]]
