---
materia: Fluid Mechanics
tema: "Topic 1: Fluid Statics"
origen: "NOT found among the ten official hydrostatics problem sheets in the unit-05-hydrostatics folder of the fluid-mechanics sources (fluid_statics_1 to fluid_statics_10); the statement and the label 'Examen Final Oficial' must be re-verified against the original exam"
dificultad: high
tags:
  - exam-problem
  - solved
  - gates
  - center-of-pressure
---

# ✏️ Problem: Inclined Hinged Gate with Closing Force

## 📄 Statement
A homogeneous rectangular gate of width $b = 2.0\text{ m}$ (perpendicular to the page) and length $L = 3.0\text{ m}$ separates a freshwater reservoir ($\rho = 1000\text{ kg/m}^3$) from the exterior at atmospheric pressure. The gate is frictionlessly hinged at its upper edge $A$, which is submerged at a vertical depth $h_A = 2.0\text{ m}$ below the free surface of the water. The gate makes an angle $\theta = 60^\circ$ with the horizontal free surface of the water.

The self-mass of the gate is $M = 1500\text{ kg}$. At the lower end $B$, a horizontal stop prevents the gate from opening spontaneously.

**Required:**
1. Calculate the total hydrostatic force $F_R$ exerted by the water on the gate.
2. Determine the distance measured along the gate from the hinge $A$ to the center of pressure $CP$ ($d_{A-CP}$).
3. Determine the minimum horizontal force $F_{\text{closing}}$ that must be applied at the lower end $B$ to keep the gate closed if the stop is removed.  
*(Given: $g = 9.81\text{ m/s}^2$)*.

---

## 📊 Phase 1: Hypotheses and Degrees of Freedom (Data Identification)

### Geometry and Fluid:
* $ b = 2.0\text{ m} $ (width), $ L = 3.0\text{ m} $ (length) $\implies \text{Area } A = b \cdot L = 6.0\text{ m}^2 $
* $ \theta = 60^\circ \implies \sin(60^\circ) = \frac{\sqrt{3}}{2} \approx 0.8660 $
* $ h_A = 2.0\text{ m} $ (vertical depth of the hinge)
* $ \rho = 1000\text{ kg/m}^3, \quad g = 9.81\text{ m/s}^2 $
* Gate mass: $ M = 1500\text{ kg} \implies W = M \cdot g = 1500 \times 9.81 = 14\,715\text{ N} $

---

## 🔢 Phase 3: Step-by-Step Mathematical Derivation

### Part 1: Magnitude of the Hydrostatic Force ($F_R$)
The vertical depth of the center of gravity of the gate ($CG$) is:
$$ h_{CG} = h_A + \frac{L}{2} \sin\theta = 2.0 + \frac{3.0}{2} \sin(60^\circ) = 2.0 + 1.5 \times 0.8660 = 2.0 + 1.299 = \mathbf{3.299\text{ m}} $$

Gauge pressure at the $CG$:
$$ p_{CG} = \rho g h_{CG} = 1000 \times 9.81 \times 3.299 = 32\,363.19\text{ Pa} $$

Resultant hydrostatic force:
$$ F_R = p_{CG} \cdot A = 32\,363.19 \times 6.0 = \mathbf{194\,179.14\text{ N}} \approx \mathbf{194.18\text{ kN}} $$

---

### Part 2: Location of the Center of Pressure ($CP$)
We define the coordinate $y$ along the plane of the gate with origin at the free surface ($y=0$ where the extension of the gate meets the surface):
$$ y_A = \frac{h_A}{\sin\theta} = \frac{2.0}{\sin(60^\circ)} = 2.3094\text{ m} $$
$$ y_{CG} = y_A + \frac{L}{2} = 2.3094 + 1.5 = 3.8094\text{ m} $$

Centroidal moment of inertia of the rectangular section:
$$ I_{xx,CG} = \frac{b \cdot L^3}{12} = \frac{2.0 \times (3.0)^3}{12} = \frac{54}{12} = 4.5\text{ m}^4 $$

Coordinate of the center of pressure along the plane:
$$ y_{CP} = y_{CG} + \frac{I_{xx,CG}}{y_{CG} \cdot A} = 3.8094 + \frac{4.5}{3.8094 \times 6.0} = 3.8094 + \frac{4.5}{22.8564} = 3.8094 + 0.1969 = 4.0063\text{ m} $$

Distance from the hinge $A$ to the $CP$:
$$ d_{A-CP} = y_{CP} - y_A = 4.0063 - 2.3094 = \mathbf{1.6969\text{ m}} \approx \mathbf{1.70\text{ m}} $$
*(Note that it lies $19.7\text{ cm}$ below the centroid, which is located $1.50\text{ m}$ from $A$)*.

---

### Part 3: Horizontal Closing Force at $B$ ($F_{\text{closing}}$)
**Assumption (the statement does not say on which side of the gate the water lies).** Free-body diagram of the gate, axes with origin at the hinge $A$, $x$ horizontal (positive to the right), $y$ vertical (positive upward), $z$ out of the page. The gate runs from $A$ down to $B$ with $B$ at $\vec{r}_B = (L\cos\theta,\,-L\sin\theta)$ relative to $A$, i.e. to the right of and below $A$. **The water is assumed to lie on the lower-left face of the gate** (the gate leans over the water, the free surface being $h_A = 2.0\text{ m}$ above $A$), so the hydrostatic force acts on the gate along the outward normal $\vec{n} = (\sin\theta,\,\cos\theta)$ (upward and to the right). The horizontal force $F_{\text{closing}}$ at $B$ points to the left, as in the statement of the closing force. Sign convention: $\sum M_A = 0$ with **counter-clockwise positive**, $M_z = r_x F_y - r_y F_x$ (moment arms measured from $A$).

1. **Hydrostatic moment.** $\vec{F}_R = F_R(\sin\theta,\cos\theta)$ acts at $\vec{r}_{CP} = d_{A-CP}(\cos\theta,-\sin\theta)$:
   $$ M_{\text{hydro}} = r_x F_y - r_y F_x = d_{A-CP}F_R\left(\cos^2\theta + \sin^2\theta\right) = F_R\, d_{A-CP} = 194\,181 \times 1.6969 = +329\,503\text{ N}\cdot\text{m} $$
   (counter-clockwise: it tends to open the gate). Cross-check by direct integration along the gate, $s\in[0,L]$ from $A$: $M = \rho g \sin\theta\, b\int_0^L (y_A + s)\,s\,ds = \rho g\sin\theta\, b\left(y_A\frac{L^2}{2} + \frac{L^3}{3}\right) = 329\,503\text{ N}\cdot\text{m}$.
2. **Weight.** $\vec{W} = (0,-W)$, $W = 14\,715\text{ N}$, acts at $CG$, $\vec{r}_{CG} = \frac{L}{2}(\cos\theta,-\sin\theta)$. Horizontal moment arm $d_{\text{weight}} = \frac{L}{2}\cos\theta = 0.75\text{ m}$:
   $$ M_{\text{weight}} = r_x F_y - r_y F_x = 0.75 \times (-W) - 0 = -14\,715 \times 0.75 = -11\,036.25\text{ N}\cdot\text{m} $$
   (clockwise: it tends to close the gate).
3. **Closing force.** $\vec{F}_{\text{closing}} = (-F_{\text{closing}},0)$ at $\vec{r}_B$. Vertical moment arm $h_{AB} = L\sin\theta = 3.0\times 0.8660 = 2.5981\text{ m}$:
   $$ M_{\text{closing}} = r_x F_y - r_y F_x = 0 - (-L\sin\theta)(-F_{\text{closing}}) = - F_{\text{closing}}\,(L\sin\theta) $$
   (clockwise).

### Equilibrium equation ($\sum M_A = 0$, counter-clockwise positive):
$$ M_{\text{hydro}} + M_{\text{weight}} + M_{\text{closing}} = 0 $$
$$ 329\,503 - 11\,036.25 - F_{\text{closing}}\,(2.5981) = 0 $$
$$ 318\,466 = 2.5981 \cdot F_{\text{closing}} $$

$$ \mathbf{F_{\text{closing}} = \frac{318\,466}{2.5981} = 122\,578\text{ N} \approx 122.58\text{ kN}\ \text{(to the left)}} $$

> [!warning] Dependence on the water side
> The weight reduces the force needed only if the hydrostatic moment and the weight moment have opposite senses, which holds for the configuration assumed above. If instead the water lay on the upper-right face of the same gate (gate sloping down under the water), the hydrostatic moment would be $-329\,503\text{ N}\cdot\text{m}$ (clockwise), the weight moment would still be $-11\,036.25\text{ N}\cdot\text{m}$, and a closing force pointing to the **right** would be needed: $F_{\text{closing}} = (329\,503 + 11\,036.25)/2.5981 = 131.07\text{ kN}$. The value $122.58\text{ kN}$ is therefore specific to the stated assumption. The earlier line "$M_{\text{hydro}} - M_{\text{weight}} - \dots$" subtracted an already negative $M_{\text{weight}}$ while the numbers used it as a restoring moment; the equation above removes that sign inconsistency without changing the numerical value for this configuration.

---

## 🎯 Phase 4: Units and Summary of Results
| Requested quantity | Symbol | Numerical Value | Units |
| :--- | :--- | :--- | :--- |
| Resultant hydrostatic force | $F_R$ | **194.18** | $\text{kN}$ |
| Position of the Center of Pressure from $A$ | $d_{A-CP}$ | **1.70** | $\text{m}$ |
| Horizontal closing force at the foot | $F_{\text{closing}}$ | **122.58** | $\text{kN}$ |
