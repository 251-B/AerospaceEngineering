---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 8"
dificultad: alta
tags:
  - problema-oficial
  - resuelto
  - planar-packing-fraction
  - fcc
  - miller-indices
---

# ✏️ Problema: T2-CS08 — Fracción de Empaquetamiento Planar en Planos FCC

## 📄 Enunciado Oficial
> **8. Calculate the fraction of area occupied by atoms for the $(111)$, $(200)$, $(220)$, $(222)$, $(400)$ and $(420)$ planes, in the FCC structure.**  
> *(Solución: $(111): \pi/(2\sqrt{3})$; $(200): \pi/4$; $(220): \pi\sqrt{2}/8$; $(222): 0$; $(400): 0$; $(420): \pi/(4\sqrt{5})$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Modelo Reticular:
* Estructura: Cúbica Centrada en las Caras (FCC).
* Relación fundamental de contacto a lo largo de $\langle 110 \rangle$:
  $$a = 2\sqrt{2} R \implies R = \frac{a}{2\sqrt{2}} = \frac{a\sqrt{2}}{4}$$
* Área de la sección transversal de cada átomo esférico de radio $R$:
  $$A_{\text{átomo}} = \pi R^2$$

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

La **Fracción de Área Ocupada por Átomos (Planar Packing Fraction, PPF)** en un plano cristalográfico $(h\, k\, l)$ se define como la razón entre el área total de las secciones circulares de los átomos cuyos centros caen exactamente en dicho plano y el área geométrica total del plano dentro de la celda unitaria [Session 4 Slide 8]:

$$\text{PPF}_{(hkl)} = \frac{N_{\text{átomos}} \cdot (\pi R^2)}{A_{(hkl)}}$$

* Si un plano pasa entre planos atómicos y **no corta el centro de ningún átomo**, el número de átomos contenidos es cero y $\text{PPF} = 0$.

---

## 🔢 3. Fase 3: Deducción Analítica para Cada Plano

### 1. Plano $(111)$:
* **Geometría:** Triángulo equilátero con arista $L = a\sqrt{2} = 4R$.
* **Área:** $A_{(111)} = \frac{\sqrt{3}}{4} L^2 = \frac{\sqrt{3}}{4}(4R)^2 = 4\sqrt{3} R^2$.
* **Átomos contenidos:** 3 vértices $\times \frac{1}{6} + 3$ centros de lados $\times \frac{1}{2} = 2\text{ átomos}$.
* **Área atómica:** $2 \times (\pi R^2) = 2\pi R^2$.
$$\text{PPF}_{(111)} = \frac{2\pi R^2}{4\sqrt{3} R^2} = \mathbf{\frac{\pi}{2\sqrt{3}}} \approx \mathbf{0.9069} \quad (90.7\%)$$

---

### 2. Plano $(200)$:
* **Posición:** Plano paralelo a $(100)$ situado a media arista: $x = a/2$.
* **Área:** Sección transversal cuadrada de la celda: $A_{(200)} = a^2$.
* **Átomos contenidos en $x = a/2$:**
  En una red FCC, en el plano central perpendicular al eje $x$ existen los átomos de los centros de las 4 caras circundantes (posiciones $(a/2, 1/2, 0)$, $(a/2, 0, 1/2)$, $(a/2, 1, 1/2)$, $(a/2, 1/2, 1)$).
  Cada uno está en el punto medio de una arista de este cuadrado de lado $a$, aportando $\frac{1}{2}$:
  $$N_{\text{átomos}} = 4 \times \frac{1}{2} = 2\text{ átomos}$$
* Sabiendo que $a = 2\sqrt{2} R \implies a^2 = 8R^2$:
$$\text{PPF}_{(200)} = \frac{2 \cdot \pi R^2}{a^2} = \frac{2\pi R^2}{8R^2} = \mathbf{\frac{\pi}{4}} \approx \mathbf{0.7854} \quad (78.5\%)$$

---

### 3. Plano $(220)$:
* **Posición:** Plano perpendicular a la diagonal de cara $[110]$ que intersecta los ejes en $x = a/2, y = a/2$.
* **Área:** Rectángulo de base $\frac{a\sqrt{2}}{2} = \frac{a}{\sqrt{2}}$ y altura $a \implies A_{(220)} = \frac{a^2}{\sqrt{2}} = \frac{a^2\sqrt{2}}{2}$.
* **Átomos contenidos:** Contiene 2 centros de cara de las caras superior e inferior $\implies 1\text{ átomo}$ neto.
* Sabiendo que $a^2 = 8R^2 \implies A_{(220)} = \frac{8R^2}{\sqrt{2}} = 4\sqrt{2} R^2$:
$$\text{PPF}_{(220)} = \frac{1 \cdot \pi R^2}{4\sqrt{2} R^2} = \frac{\pi}{4\sqrt{2}} = \mathbf{\frac{\pi\sqrt{2}}{8}} \approx \mathbf{0.5554} \quad (55.5\%)$$

---

### 4. Plano $(222)$:
* **Posición:** Plano paralelo a $(111)$ con cortes en $x = a/2, y = a/2, z = a/2$.
* **Átomos contenidos:** En una red FCC perfecta, el plano $x+y+z = a/2$ **no pasa por ningún centro atómico** (los átomos están en vértices enteros y centros de cara $(1/2, 1/2, 0)$, cuya suma de coordenadas fraccionarias es $0$, $1$ o $2$, nunca $1/2$).
* Por tanto, $N_{\text{átomos}} = 0$:
$$\text{PPF}_{(222)} = \mathbf{0}$$

---

### 5. Plano $(400)$:
* **Posición:** Plano paralelo a $(100)$ situado en $x = a/4$.
* **Átomos contenidos:** En $x = a/4$ no existe ningún nudo de la red FCC (los átomos solo están en $x = 0, a/2, a$).
* Por tanto, $N_{\text{átomos}} = 0$:
$$\text{PPF}_{(400)} = \mathbf{0}$$

---

### 6. Plano $(420)$:
* **Posición:** Intersecta los ejes en $x = a/4, y = a/2, z = \infty$.
* **Área del plano:** Rectángulo de longitud base $\sqrt{(a/4)^2 + (a/2)^2} = \sqrt{\frac{5}{16}}a = \frac{a\sqrt{5}}{4}$ y altura $a$:
  $$A_{(420)} = \frac{\sqrt{5}}{4}a^2$$
* **Átomos contenidos:** Contiene el centro de cara $(a/2, 0, a/2)$, aportando $1/2$ átomo dentro del corte:
  $$N_{\text{átomos}} = \frac{1}{2}\text{ átomo}$$
* Sabiendo que $a^2 = 8R^2 \implies A_{(420)} = \frac{\sqrt{5}}{4}(8R^2) = 2\sqrt{5} R^2$:
$$\text{PPF}_{(420)} = \frac{\frac{1}{2}\pi R^2}{2\sqrt{5} R^2} = \mathbf{\frac{\pi}{4\sqrt{5}}} \approx \mathbf{0.3512} \quad (35.1\%)$$

---

## 🎯 4. Fase 4: Interpretación Física y Resumen Comparativo

| Plano $(hkl)$ | Átomos en el Plano | Área del Plano en la Celda | PPF Analítico | PPF Porcentual | Significado Físico |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **$(111)$** | 2 | $4\sqrt{3}R^2$ | $\mathbf{\frac{\pi}{2\sqrt{3}}}$ | **90.7%** | Plano más compacto posible de esferas rígidas |
| **$(200)$** | 2 | $8R^2$ | $\mathbf{\frac{\pi}{4}}$ | **78.5%** | Plano atómico denso paralelo a caras |
| **$(220)$** | 1 | $4\sqrt{2}R^2$ | $\mathbf{\frac{\pi\sqrt{2}}{8}}$ | **55.5%** | Plano medio diagonal |
| **$(222)$** | 0 | — | $\mathbf{0}$ | **0%** | Pasa entre planos compactos $\{111\}$ |
| **$(400)$** | 0 | — | $\mathbf{0}$ | **0%** | Plano de espaciado interatómico vacío |
| **$(420)$** | 1/2 | $2\sqrt{5}R^2$ | $\mathbf{\frac{\pi}{4\sqrt{5}}}$ | **35.1%** | Plano oblicuo de baja densidad |

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
