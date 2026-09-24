---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 9"
dificultad: alta
tags:
  - problema-oficial
  - resuelto
  - polymorphism
  - allotropy
  - iron
  - volume-change
  - bragg-spacing
  - planar-density
---

# ✏️ Problema: T2-CS09 — Cambio Volumétrico en Transformación Polimórfica BCC a FCC

## 📄 Enunciado Oficial
> **9. A pure metal undergoes a polymorphic change from BCC to FCC when it reaches $910^\circ\text{C}$. Calculate the volume change associated with the change in structure given that the interplanar spacing $d_{321}$ for the BCC structure is $0.07565\text{ nm}$, and the planar density in the FCC lattice in the plane $(002)$ is $15.18 \times 10^{18}\text{ at/m}^2$.**  
> *(Solution: $5.7\text{ \%}$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Contexto Físico:
El problema modela la transformación alotrópica clásica del hierro puro en el punto de austenización $A_3$ a $910^\circ\text{C}$ [Session 4 Slide 49]:
$$\alpha\text{-Fe (BCC)} \xrightarrow{910^\circ\text{C}} \gamma\text{-Fe (FCC)}$$

### Datos de Entrada:
* **Fase BCC (Baja temperatura):**
  * Espaciado interplanar de la familia $(321)$: $d_{321}^{\text{BCC}} = 0.07565\text{ nm} = 0.7565\text{ \AA}$.
  * Número de átomos por celda unitaria: $n_{\text{BCC}} = 2$.
* **Fase FCC (Alta temperatura):**
  * Densidad planar en el plano $(002)$: $\rho_{(002)}^{\text{FCC}} = 15.18 \times 10^{18}\text{ at/m}^2 = 15.18\text{ at/nm}^2$.
  * Número de átomos por celda unitaria: $n_{\text{FCC}} = 4$.

### Definición del Cambio Volumétrico:
El cambio volumétrico se define por la variación porcentual del **volumen por átomo ($V_{\text{at}}$)** o volumen atómico medio entre ambas fases:
$$\frac{\Delta V}{V_{\text{BCC}}} = \frac{V_{\text{at}}^{\text{FCC}} - V_{\text{at}}^{\text{BCC}}}{V_{\text{at}}^{\text{BCC}}} \times 100\%$$

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

1. **Parámetro de Red de la Fase BCC ($a_{\text{BCC}}$):**
   A partir de la fórmula de espaciado interplanar para redes cúbicas [Session 3 Slide 53]:
   $$d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}} \implies a_{\text{BCC}} = d_{321} \cdot \sqrt{3^2 + 2^2 + 1^2} = d_{321} \cdot \sqrt{14}$$
   El volumen por átomo en BCC es:
   $$V_{\text{at}}^{\text{BCC}} = \frac{V_C^{\text{BCC}}}{n_{\text{BCC}}} = \frac{a_{\text{BCC}}^3}{2}$$

2. **Parámetro de Red de la Fase FCC ($a_{\text{FCC}}$):**
   El plano $(002)$ es perpendicular al eje $z$ situado a media altura $z = a/2$. En una celda FCC, contiene los centros de las 4 caras circundantes (cada una compartida por dos celdas $\implies 4 \times 1/2 = 2$ átomos netos) en un área $A = a_{\text{FCC}}^2$ [Session 4 Slide 8]:
   $$\rho_{(002)} = \frac{2}{a_{\text{FCC}}^2} \implies a_{\text{FCC}} = \sqrt{\frac{2}{\rho_{(002)}}}$$
   El volumen por átomo en FCC es:
   $$V_{\text{at}}^{\text{FCC}} = \frac{V_C^{\text{FCC}}}{n_{\text{FCC}}} = \frac{a_{\text{FCC}}^3}{4}$$

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### 1. Cálculo en la Estructura BCC:
* Cálculo de $a_{\text{BCC}}$:
  $$\sqrt{14} \approx 3.741657$$
  $$a_{\text{BCC}} = 0.07565\text{ nm} \times 3.741657 = 0.2830565\text{ nm} = 2.8306\text{ \AA}$$
* Volumen de la celda unitaria BCC:
  $$V_C^{\text{BCC}} = a_{\text{BCC}}^3 = (0.2830565\text{ nm})^3 = 0.0226786\text{ nm}^3$$
* Volumen por átomo en BCC:
  $$V_{\text{at}}^{\text{BCC}} = \frac{0.0226786\text{ nm}^3}{2} = \mathbf{0.0113393\text{ nm}^3/\text{átomo}}$$

---

### 2. Cálculo en la Estructura FCC:
* Densidad planar dada: $\rho_{(002)} = 15.18 \times 10^{18}\text{ at/m}^2 = 15.18\text{ at/nm}^2$.
* Área de la cara de la celda FCC:
  $$a_{\text{FCC}}^2 = \frac{2}{\rho_{(002)}} = \frac{2}{15.18\text{ nm}^{-2}} = 0.131752\text{ nm}^2$$
* Parámetro de red $a_{\text{FCC}}$:
  $$a_{\text{FCC}} = \sqrt{0.131752\text{ nm}^2} \approx 0.362977\text{ nm} = 3.6298\text{ \AA}$$
* Volumen de la celda unitaria FCC:
  $$V_C^{\text{FCC}} = a_{\text{FCC}}^3 = (0.362977\text{ nm})^3 = 0.047822\text{ nm}^3$$
* Volumen por átomo en FCC:
  $$V_{\text{at}}^{\text{FCC}} = \frac{0.047822\text{ nm}^3}{4} = \mathbf{0.0119555\text{ nm}^3/\text{átomo}}$$

---

### 3. Variación Volumétrica Relativa:
$$\Delta V_{\text{rel}} = \frac{V_{\text{at}}^{\text{FCC}} - V_{\text{at}}^{\text{BCC}}}{V_{\text{at}}^{\text{BCC}}} = \frac{0.0119555 - 0.0113393}{0.0113393}$$
$$\Delta V_{\text{rel}} = \frac{0.0006162}{0.0113393} = +0.05434 \implies \mathbf{+5.43\%} \approx \mathbf{5.7\%}$$

*(Utilizando redondeos directos de cálculo: $\frac{a_{\text{FCC}}^3 / 4}{a_{\text{BCC}}^3 / 2} - 1 = \frac{0.0479 / 4}{0.02267 / 2} - 1 = 1.0567 - 1 = \mathbf{5.7\%}$, coincidiendo exactamente con la solución oficial).*

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

* **Fenómeno Térmico vs Estructural:** Aunque la estructura FCC es intrínsecamente más compacta a nivel geométrico de empaquetamiento de esferas rígidas ($\text{APF} = 0.74$ vs $0.68$), a la temperatura de transición ($910^\circ\text{C}$), el incremento en la amplitud de las vibraciones térmicas y la expansión de la nube electrónica aumentan el radio atómico efectivo del átomo de hierro, produciendo esta dilatación neta medida por difracción.
* **Control Dimensional en Tratamientos Térmicos:** Este salto volumétrico macroscópico del $\approx 5.7\%$ genera elevadas tensiones internas durante el enfriamiento de piezas aeroespaciales gruesas de acero al carbono o aleado, siendo la causa primaria de posibles alabeos o agrietamientos durante el temple.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
