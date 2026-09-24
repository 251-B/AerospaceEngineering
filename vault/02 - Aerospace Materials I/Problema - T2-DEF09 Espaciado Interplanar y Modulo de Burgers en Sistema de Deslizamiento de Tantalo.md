---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 9"
dificultad: media
tags:
  - problema-oficial
  - resuelto
  - tantalum
  - bcc
  - slip-systems
  - burgers-vector
  - interplanar-spacing
---

# ✏️ Problema: T2-DEF09 — Espaciado Interplanar y Módulo de Burgers en Sistema de Deslizamiento de Tántalo

## 📄 Enunciado Oficial
> **9. a) Determine the interplanar spacing and the length of the Burgers vector for slipping in the slip system $(110) / [1\,\bar{1}\,1]$ in BCC tantalum.**  
> **b) Repeat assuming that the slip system is $(111) / [1\,\bar{1}\,0]$.**  
> **Data: $a = 3.3026\text{ \AA}$.**  
> *(Solution: a) $b = 2.860\text{ \AA}$, $d_{(110)} = 2.335\text{ \AA}$; b) $b = 4.671\text{ \AA}$, $d_{(111)} = 1.907\text{ \AA}$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Material y Parámetro Reticular:
* Elemento: Tántalo puro ($\text{Ta}$), metal refractario de alta densidad.
* Estructura: Cúbica Centrada en el Cuerpo (BCC).
* Parámetro de red: $a = 3.3026\text{ \AA} = 0.33026\text{ nm}$.

### Sistemas de Deslizamiento Evaluados:
1. **Sistema Real (Apartado a):** Plano $(110)$ y dirección $[1\,\bar{1}\,1]$.
2. **Sistema Hipotético (Apartado b):** Plano $(111)$ y dirección $[1\,\bar{1}\,0]$.

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

1. **Espaciado Interplanar en Cristales Cúbicos [Session 3 Slide 53]:**
   $$d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}$$
2. **Magnitud del Vector de Burgers ($\vec{b}$) en Redes Cúbicas [Session 4 Slide 35]:**
   * En la dirección de deslizamiento $[1\,\bar{1}\,1]$ (dirección de máxima compacidad en BCC), el vector de traslación reticular mínimo une un vértice con el centro del cubo:
     $$\vec{b}_a = \frac{a}{2}[1\, -1\, 1] \implies |\vec{b}_a| = \frac{a\sqrt{1^2 + (-1)^2 + 1^2}}{2} = \frac{a\sqrt{3}}{2}$$
   * En la dirección de deslizamiento hipotética $[1\,\bar{1}\,0]$ (diagonal de cara en BCC), el centro de la celda no interrumpe la diagonal; el vector de traslación elemental completo une dos vértices opuestos de una cara cuadrada:
     $$\vec{b}_b = a[1\, -1\, 0] \implies |\vec{b}_b| = a\sqrt{1^2 + (-1)^2 + 0^2} = a\sqrt{2}$$

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### 1. Apartado a: Sistema Real $(110) / [1\,\bar{1}\,1]$
* **Espaciado Interplanar $d_{(110)}$:**
  $$d_{(110)} = \frac{a}{\sqrt{1^2 + 1^2 + 0^2}} = \frac{a}{\sqrt{2}} = \frac{3.3026\text{ \AA}}{\sqrt{2}} = \frac{3.3026}{1.4142136} = \mathbf{2.3353\text{ \AA}} \approx \mathbf{2.335\text{ \AA}}$$

* **Longitud del Vector de Burgers $|\vec{b}|$:**
  $$|\vec{b}| = \frac{a\sqrt{3}}{2} = \frac{3.3026\text{ \AA} \times 1.7320508}{2} = \frac{5.72027}{2} = \mathbf{2.8601\text{ \AA}} \approx \mathbf{2.860\text{ \AA}}$$

---

### 2. Apartado b: Sistema Hipotético $(111) / [1\,\bar{1}\,0]$
* **Espaciado Interplanar $d_{(111)}$:**
  $$d_{(111)} = \frac{a}{\sqrt{1^2 + 1^2 + 1^2}} = \frac{a}{\sqrt{3}} = \frac{3.3026\text{ \AA}}{1.7320508} = \mathbf{1.90676\text{ \AA}} \approx \mathbf{1.907\text{ \AA}}$$
  *(Nótese que en la hoja oficial de soluciones aparece la errata tipográfica rotulada como $d_{(110)} = 1.907\text{ \AA}$, cuando corresponde al plano $(111)$).*

* **Longitud del Vector de Burgers $|\vec{b}|$:**
  $$|\vec{b}| = a\sqrt{2} = 3.3026\text{ \AA} \times 1.4142136 = \mathbf{4.67058\text{ \AA}} \approx \mathbf{4.671\text{ \AA}}$$

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

Comparativa de los dos sistemas analizados:

| Parámetro Físico | Sistema Real: $(110)/[1\bar{1}1]$ | Sistema Hipotético: $(111)/[1\bar{1}0]$ | Comparativa |
| :--- | :--- | :--- | :--- |
| **Espaciado Interplanar $d_{hkl}$** | $\mathbf{2.335\text{ \AA}}$ (Mayor) | $1.907\text{ \AA}$ (Menor) | $d_{(110)} > d_{(111)}$ |
| **Módulo de Burgers $|\vec{b}|$** | $\mathbf{2.860\text{ \AA}}$ (Menor) | $4.671\text{ \AA}$ (Mayor) | $|\vec{b}_{\text{real}}| \ll |\vec{b}_{\text{hipotético}}|$ |
| **Energía de Dislocación ($E \propto |\vec{b}|^2$)** | $k \times (2.860)^2 = \mathbf{8.18\, k}$ | $k \times (4.671)^2 = \mathbf{21.82\, k}$ | **2.67 veces menor energía** |

### Conclusión Metalúrgica:
La tensión de Peierls-Nabarro $\tau_{\text{PN}}$ (resistencia intrínseca de la red al movimiento de una dislocación) decrece exponencialmente con el espaciado interplanar $d$ y crece con la magnitud del vector de Burgers:
$$\tau_{\text{PN}} \approx 2G \exp\left(-\frac{2\pi d}{|\vec{b}|}\right)$$
El sistema real $(110)/[1\bar{1}1]$ posee simultáneamente el **mayor espaciado interplanar** ($2.335\text{ \AA}$) y el **menor vector de Burgers** ($2.860\text{ \AA}$), haciendo que la energía de deformación sea casi tres veces inferior y la resistencia al movimiento sea mínima. Por ello, el tántalo y todos los metales refractarios BCC deslizan de forma invariable en la familia $\{110\}\langle 111 \rangle$.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
