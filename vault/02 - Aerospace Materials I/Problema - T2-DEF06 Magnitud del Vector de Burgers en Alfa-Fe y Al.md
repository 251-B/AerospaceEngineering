---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 6"
dificultad: baja
tags:
  - problema-oficial
  - resuelto
  - burgers-vector
  - bcc
  - fcc
  - slip-direction
  - dislocations
---

# ✏️ Problema: T2-DEF06 — Magnitud del Vector de Burgers en α-Fe (BCC) y Al (FCC)

## 📄 Enunciado Oficial
> **6. Calculate the Burgers vector magnitude for $\alpha\text{-Fe}$ (BCC) and $\text{Al}$ (FCC).**  
> *(Solution: $\alpha\text{-Fe}: \frac{\sqrt{3}a}{2}$; $\text{Al}: \frac{a}{\sqrt{2}}$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Modelos de Red:
1. **Hierro Ferrítico ($\alpha\text{-Fe}$):** Red Cúbica Centrada en el Cuerpo (BCC), parámetro reticular $a$.
2. **Aluminio Puro ($\text{Al}$):** Red Cúbica Centrada en las Caras (FCC), parámetro reticular $a$.

### Hipótesis Fundamental:
* En cualquier red cristalina metálica, las dislocaciones estables son **dislocaciones unitarias (o perfectas)** cuyo vector de Burgers $\vec{b}$ conecta dos posiciones de red idénticas y equivalentes a lo largo de la **dirección cristalográfica de máximo empaquetamiento** para minimizar la energía elástica de la dislocación ($E \propto |\vec{b}|^2$) [Session 4 Slide 35].

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

Citando la teoría de dislocaciones y sistemas de deslizamiento [Session 4 Slides 28, 34-36]:
* **En la red BCC:**
  * La dirección de máximo empaquetamiento atómico es la diagonal principal del cubo $\langle 111 \rangle$.
  * La menor traslación reticular que conecta dos nudos de la red es la que va desde un vértice $(0,0,0)$ hasta el centro del cuerpo $(1/2, 1/2, 1/2)$:
    $$\vec{b}_{\text{BCC}} = \frac{a}{2}[1\, 1\, 1]$$
* **En la red FCC:**
  * La dirección de máximo empaquetamiento es la diagonal de la cara $\langle 110 \rangle$.
  * La menor traslación reticular que une dos posiciones idénticas de red va desde un vértice $(0,0,0)$ hasta el centro de la cara $(1/2, 1/2, 0)$:
    $$\vec{b}_{\text{FCC}} = \frac{a}{2}[1\, 1\, 0]$$

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### 1. Cálculo de la Magnitud en $\alpha\text{-Fe}$ (BCC):
* Vector de Burgers en componentes cartesianas:
  $$\vec{b} = \left(\frac{a}{2}, \frac{a}{2}, \frac{a}{2}\right)$$
* Magnitud (módulo euclídeo):
  $$|\vec{b}| = \sqrt{\left(\frac{a}{2}\right)^2 + \left(\frac{a}{2}\right)^2 + \left(\frac{a}{2}\right)^2} = \sqrt{3 \left(\frac{a^2}{4}\right)}$$
  $$|\vec{b}|_{\alpha\text{-Fe}} = \mathbf{\frac{a\sqrt{3}}{2}} = \mathbf{\frac{\sqrt{3}a}{2}}$$
  *(Nótese que como en BCC $a\sqrt{3} = 4R$, la magnitud es exactamente $|\vec{b}| = 2R$, que corresponde al diámetro atómico en contacto).*

---

### 2. Cálculo de la Magnitud en $\text{Al}$ (FCC):
* Vector de Burgers en componentes cartesianas:
  $$\vec{b} = \left(\frac{a}{2}, \frac{a}{2}, 0\right)$$
* Magnitud (módulo euclídeo):
  $$|\vec{b}| = \sqrt{\left(\frac{a}{2}\right)^2 + \left(\frac{a}{2}\right)^2 + 0^2} = \sqrt{\frac{a^2}{4} + \frac{a^2}{4}} = \sqrt{\frac{2a^2}{4}} = \frac{a\sqrt{2}}{2}$$
  Racionalizando dividiendo numerador y denominador por $\sqrt{2}$:
  $$|\vec{b}|_{\text{Al}} = \mathbf{\frac{a}{\sqrt{2}}}$$
  *(Nótese que en FCC $a\sqrt{2} = 4R$, por lo que $|\vec{b}| = \frac{4R}{2} = 2R$, coincidiendo también exactamente con el diámetro atómico en contacto).*

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

* **Universalidad del Diámetro Atómico:** En ambas estructuras cristalinas metálicas, la magnitud del vector de Burgers de la dislocación perfecta elemental es idéntica al diámetro atómico:
  $$|\vec{b}| = 2R$$
* Esto demuestra matemáticamente por qué el deslizamiento plástico ocurre escalón a escalón a lo largo de las filas atómicas densas: cada vez que la línea de la dislocación barre un plano, desplaza el bloque superior del cristal una distancia atómica elemental $|\vec{b}| = 2R$ respecto al inferior.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
