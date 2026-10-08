---
materia: Fluid Mechanics
tema: "Topic 1: Fluid Statics"
origen: "NOT found among the ten official hydrostatics problem sheets in the unit-05-hydrostatics folder of the fluid-mechanics sources (fluid_statics_1 to fluid_statics_10); the statement ('Examen Parcial Típico') must be re-verified"
dificultad: medium
tags:
  - exam-problem
  - solved
  - manometry
---

# ✏️ Problem: Multi-Liquid Differential Manometer with Gas Pressurisation

## 📄 Statement
A closed tank $A$ contains pressurised air above a layer of oil of relative density $SG_{\text{oil}} = 0.85$. The tank is connected, through an inverted $U$-tube manometer and a mercury $U$-tube manometer ($SG_{\text{Hg}} = 13.6$), to a pipe $B$ carrying water ($\rho_{\text{water}} = 1000\text{ kg/m}^3$).

The geometric elevations measured with respect to a horizontal reference plane are:
* Free surface of the oil in tank $A$: $z_1 = 3.50\text{ m}$
* Lower oil-mercury meniscus in the U-tube: $z_2 = 1.20\text{ m}$
* Upper mercury-water meniscus in the U-tube: $z_3 = 1.80\text{ m}$
* Axis of pipe $B$ with water: $z_4 = 2.40\text{ m}$

If the gauge pressure read in the air of tank $A$ is $p_{A,\text{air}} = 45\text{ kPa}$, **determine the gauge pressure at the center of pipe $B$** ($p_B$).  
*(Given: $g = 9.81\text{ m/s}^2$)*.

---

## 📊 Phase 1: Hypotheses and Degrees of Freedom (Data Identification)

### Numerical Data:
* $ \rho_{\text{water}} = 1000\text{ kg/m}^3 $
* $ \rho_{\text{oil}} = 0.85 \times 1000 = 850\text{ kg/m}^3 $
* $ \rho_{\text{Hg}} = 13.6 \times 1000 = 13\,600\text{ kg/m}^3 $
* $ p_{A,\text{air}} = 45\,000\text{ Pa} $
* $ z_1 = 3.50\text{ m}, \quad z_2 = 1.20\text{ m}, \quad z_3 = 1.80\text{ m}, \quad z_4 = 2.40\text{ m} $

### Starting Hypotheses:
* [x] Static fluid in all manometric branches.
* [x] The air pressure above the oil in $A$ is uniform throughout the gas chamber (the weight of the air column is neglected).
* [x] Incompressible, immiscible liquids with sharp interfaces.

---

## 🧠 Phase 2: Strategy and Physical Setup
We will apply the step-by-step manometric traverse method, starting in the air of $A$ and ending at the center of pipe $B$:
1. From the oil surface ($z_1$) we descend to the lower meniscus with the mercury ($z_2$): **pressure increase** $+\rho_{\text{oil}} g (z_1 - z_2)$.
2. In the mercury, we ascend from $z_2$ to the upper meniscus with water ($z_3$): **pressure decrease** $-\rho_{\text{Hg}} g (z_3 - z_2)$.
3. In the water, we ascend from $z_3$ to the pipe axis ($z_4$): **pressure decrease** $-\rho_{\text{water}} g (z_4 - z_3)$.
4. The final result equals $p_B$.

---

## 🔢 Phase 3: Step-by-Step Mathematical Derivation

### Piezometric traverse equation:
$$ p_A + \rho_{\text{oil}} g (z_1 - z_2) - \rho_{\text{Hg}} g (z_3 - z_2) - \rho_{\text{water}} g (z_4 - z_3) = p_B $$

### Term-by-term calculation:

1. **Oil column (descent from $3.50\text{ m}$ to $1.20\text{ m} \implies \Delta h_1 = 2.30\text{ m}$):**
   $$ \Delta p_{\text{oil}} = 850 \times 9.81 \times 2.30 = +19\,178.55\text{ Pa} \approx +19.18\text{ kPa} $$

2. **Mercury column (ascent from $1.20\text{ m}$ to $1.80\text{ m} \implies \Delta h_2 = 0.60\text{ m}$):**
   $$ \Delta p_{\text{Hg}} = -13\,600 \times 9.81 \times 0.60 = -80\,049.60\text{ Pa} \approx -80.05\text{ kPa} $$

3. **Water column (ascent from $1.80\text{ m}$ to $2.40\text{ m} \implies \Delta h_3 = 0.60\text{ m}$):**
   $$ \Delta p_{\text{water}} = -1000 \times 9.81 \times 0.60 = -5\,886.00\text{ Pa} \approx -5.89\text{ kPa} $$

### Final substitution:
$$ p_B = 45\,000 + 19\,178.55 - 80\,049.60 - 5\,886.00 $$
$$ p_B = 45\,000 - 66\,757.05 = \mathbf{-21\,757.05\text{ Pa}} $$

---

## 🎯 Phase 4: Units, Final Result and Physical Analysis
* **Gauge pressure:** $ \mathbf{p_{B,\text{rel}} = -21.76\text{ kPa}} $
* **Absolute pressure:** (assuming $p_{\text{atm}} = 101.325\text{ kPa}$):
  $$ p_{B,\text{abs}} = 101.325 - 21.76 = \mathbf{79.57\text{ kPa}} $$
* **Interpretation:** The pressure in pipe $B$ is subatmospheric (relative partial vacuum). The dense $60\text{ cm}$ mercury column more than compensates both the $45\text{ kPa}$ pressurisation of the tank and the oil column, suctioning line $B$.
