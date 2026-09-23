---
materia: Fluid Mechanics
tema: "Tema 1: Propiedades y Estática de Fluidos"
tags:
  - formulario
  - prontuario
  - examen
  - fluid-mechanics
---

# 📋 Prontuario Rápido: Propiedades y Estática de Fluidos

## ⚡ 1. Propiedades Fundamentales

| Propiedad | Ecuación en LaTeX | Notas / Unidades |
| :--- | :--- | :--- |
| **Peso específico** | $ \gamma = \rho g $ | $[\text{N/m}^3]$ |
| **Ley de Newton de viscosidad** | $ \tau = \mu \frac{du}{dy} $ | $\mu \text{ en } [\text{Pa}\cdot\text{s}]$, $\tau \text{ en } [\text{Pa}]$ |
| **Viscosidad cinemática** | $ \nu = \frac{\mu}{\rho} $ | $[\text{m}^2/\text{s}]$, $1\text{ St} = 10^{-4}\text{ m}^2/\text{s}$ |
| **Ley de Sutherland (Aire)** | $ \mu(T) = \mu_0 \left(\frac{T}{T_0}\right)^{3/2} \frac{T_0 + S}{T + S} $ | $S_{\text{aire}} = 110.4\text{ K}$, $T_0 = 273.15\text{ K}$ |
| **Módulo de compresibilidad** | $ K = \rho \left(\frac{\partial p}{\partial \rho}\right) $ | Gas ideal: $K_T = p$, $K_s = \gamma_{\text{ad}} p$ |
| **Velocidad del sonido** | $ c = \sqrt{\gamma_{\text{ad}} R T} $ | Aire: $\gamma_{\text{ad}} = 1.4$, $R = 287\text{ J/(kg}\cdot\text{K)}$ |

---

## ⚡ 2. Ecuación Fundamental y Atmósfera ISA

* **Ecuación diferencial:**
  $$ \nabla p = \rho \vec{g} \implies \frac{dp}{dz} = -\rho g $$
* **Líquido incompresible ($\rho = \text{cte}$):**
  $$ p_2 - p_1 = -\rho g (z_2 - z_1) \iff p = p_0 + \rho g h $$
* **Atmósfera Troposférica ISA ($0 \le z \le 11\,000\text{ m}$):**
  $$ T(z) = T_0 - \alpha z \quad (\alpha = 0.0065\text{ K/m}, \quad T_0 = 288.15\text{ K}) $$
  $$ p(z) = p_0 \left(1 - \frac{\alpha z}{T_0}\right)^{\frac{g}{\alpha R}}, \quad \frac{g}{\alpha R} \approx 5.256 $$

---

## ⚡ 3. Fuerzas sobre Compuertas y Superficies Sumergidas

### Superficie Plana Inclinada ($\theta$ con la horizontal)
* **Fuerza Resultante:**
  $$ F_R = p_{CG} \cdot A = (\rho g h_{CG}) \cdot A = \rho g \sin\theta \, y_{CG} \cdot A $$
* **Centro de Presiones ($y_{CP}$ a lo largo del plano):**
  $$ y_{CP} = y_{CG} + \frac{I_{xx,CG}}{y_{CG} \cdot A} $$
  *Rectángulo ($b \times L$):* $I_{xx,CG} = \frac{b L^3}{12}$  
  *Círculo ($R$):* $I_{xx,CG} = \frac{\pi R^4}{4}$

### Superficie Curva
* **Componente Horizontal:** $F_H = p_{CG,v} \cdot A_v$ (proyección en plano vertical).
* **Componente Vertical:** $F_V = \rho g \cdot V_{\text{fluido sobre la superficie}}$.
* **Resultante:** $F_R = \sqrt{F_H^2 + F_V^2}, \quad \tan\alpha = F_V / F_H$.

---

## ⚡ 4. Flotabilidad y Estabilidad (Arquímedes)
* **Empuje boyante:** $E = \rho_{\text{fluido}} g V_{\text{sumergido}}$ (actúa en el Centro de Carena $C$).
* **Radio Metacéntrico:** $\overline{CM} = \frac{I_{0}}{V_{\text{sumergido}}}$ ($I_0$ inercia del área de flotación).
* **Altura Metacéntrica:** $\overline{GM} = \overline{CM} - \overline{CG}$.
  * $\overline{GM} > 0 \implies$ **Equilibrio Estable** (par restaurador).
  * $\overline{GM} < 0 \implies$ **Inestable** (zozobra / vuelco).
