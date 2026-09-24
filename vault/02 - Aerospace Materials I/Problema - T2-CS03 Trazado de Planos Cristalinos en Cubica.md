---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 3"
dificultad: media
tags:
  - problema-oficial
  - resuelto
  - miller-indices
  - planos-cristalinos
  - cubic-lattice
  - traslacion-origen
---

# ✏️ Problema: T2-CS03 — Trazado de Planos Cristalinos en Red Cúbica

## 📄 Enunciado Oficial
> **3. Draw the crystalline planes in a cubic lattice that present the following Miller indices:**  
> **a)** $(1\, 0\, \bar{1})$  
> **b)** $(1\, \bar{2}\, 1)$  
> **c)** $(\bar{2}\, 1\, 3)$  
> **d)** $(1\, \bar{3}\, 3)$  
> **e)** $(1\, \bar{2}\, \bar{2})$  
> **f)** $(\bar{3}\, \bar{1}\, 2)$  
> **g)** $(1\, 2\, \bar{3})$  
> **h)** $(\bar{1}\, \bar{4}\, 3)$  
> **i)** $(\bar{3}\, \bar{1}\, \bar{3})$  
> **j)** $(3\, \bar{1}\, 3)$

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Contexto Geométrico:
Se analizan diez familias de planos cristalográficos en una red cúbica con aristas ortogonales de longitud $a$.

### Criterio de Selección de Origen [Session 3 Slide 43]:
* Si todos los índices $h, k, l$ son positivos, el origen natural se sitúa en el vértice inferior izquierdo posterior $(0, 0, 0)$.
* Si algún índice es negativo (notación con barra superior $\bar{u}$), el origen debe trasladarse en $+1$ unidad a lo largo del eje correspondiente para que la intersección se produzca dentro de la celda unitaria estándar:
  * $\bar{h} \implies$ trasladar origen a $x = 1$.
  * $\bar{k} \implies$ trasladar origen a $y = 1$.
  * $\bar{l} \implies$ trasladar origen a $z = 1$.

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

Según el procedimiento sistemático inverso de Miller [Session 3 Slides 41-45]:
1. Tomar los **recíprocos de los índices de Miller** para hallar las intersecciones axiales relativas:
   $$x_{\text{int}} = \frac{1}{h}, \quad y_{\text{int}} = \frac{1}{k}, \quad z_{\text{int}} = \frac{1}{l}$$
   (con la regla $1/0 = \infty$, indicando paralelismo al eje).
2. Determinar la traslación de origen necesaria según el signo de las intersecciones.
3. Marcar los puntos de corte en las aristas de la celda unitaria respecto al origen elegido y unirlos mediante líneas rectas para formar el polígono de sección planar.

---

## 🔢 3. Fase 3: Determinación Detallada de los 10 Planos

| Apartado | Plano $(h\,k\,l)$ | Recíprocos $(1/h, 1/k, 1/l)$ | Origen Recomendado | Puntos de Corte en Aristas $(x, y, z)$ | Geometría del Plano |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **a** | $(1\, 0\, \bar{1})$ | $(1,\, \infty,\, -1)$ | $(0, 0, 1)$ | $(1, 0, 1)$, paralelo al eje $y$, $(0, 0, 0)$ | Rectángulo diagonal que une las aristas opuestas |
| **b** | $(1\, \bar{2}\, 1)$ | $(1,\, -1/2,\, 1)$ | $(0, 1, 0)$ | $(1, 1, 0)$, $(0, 1/2, 0)$, $(0, 1, 1)$ | Triángulo que corta el eje $y$ a media altura |
| **c** | $(\bar{2}\, 1\, 3)$ | $(-1/2,\, 1,\, 1/3)$ | $(1, 0, 0)$ | $(1/2, 0, 0)$, $(1, 1, 0)$, $(1, 0, 1/3)$ | Triángulo escaleno con cortes fraccionarios |
| **d** | $(1\, \bar{3}\, 3)$ | $(1,\, -1/3,\, 1/3)$ | $(0, 1, 0)$ | $(1, 1, 0)$, $(0, 2/3, 0)$, $(0, 1, 1/3)$ | Triángulo oblicuo |
| **e** | $(1\, \bar{2}\, \bar{2})$ | $(1,\, -1/2,\, -1/2)$ | $(0, 1, 1)$ | $(1, 1, 1)$, $(0, 1/2, 1)$, $(0, 1, 1/2)$ | Triángulo isósceles respecto a los ejes negativos $y, z$ |
| **f** | $(\bar{3}\, \bar{1}\, 2)$ | $(-1/3,\, -1,\, 1/2)$ | $(1, 1, 0)$ | $(2/3, 1, 0)$, $(1, 0, 0)$, $(1, 1, 1/2)$ | Triángulo oblicuo en cuadrante $(+x, +y)$ |
| **g** | $(1\, 2\, \bar{3})$ | $(1,\, 1/2,\, -1/3)$ | $(0, 0, 1)$ | $(1, 0, 1)$, $(0, 1/2, 1)$, $(0, 0, 2/3)$ | Triángulo oblicuo con cortes en $a$, $a/2$, $-a/3$ |
| **h** | $(\bar{1}\, \bar{4}\, 3)$ | $(-1,\, -1/4,\, 1/3)$ | $(1, 1, 0)$ | $(0, 1, 0)$, $(1, 3/4, 0)$, $(1, 1, 1/3)$ | Triángulo muy inclinado sobre el eje $y$ |
| **i** | $(\bar{3}\, \bar{1}\, \bar{3})$ | $(-1/3,\, -1,\, -1/3)$ | $(1, 1, 1)$ | $(2/3, 1, 1)$, $(1, 0, 1)$, $(1, 1, 2/3)$ | Triángulo simétrico con respecto a los ejes $x$ y $z$ |
| **j** | $(3\, \bar{1}\, 3)$ | $(1/3,\, -1,\, 1/3)$ | $(0, 1, 0)$ | $(1/3, 1, 0)$, $(0, 0, 0)$, $(0, 1, 1/3)$ | Triángulo simétrico en $x$ y $z$ cortando en $y=0$ |

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

1. **Invarianza por Simetría:** Los planos $(\bar{3}\bar{1}2)$, $(12\bar{3})$, $(\bar{3}\bar{1}\bar{3})$ y $(3\bar{1}3)$ pertenecen todos a la misma familia cristalográfica de planos $\{321\}$ o $\{331\}$ en la red cúbica. Aunque su orientación geométrica difiere por la elección de ejes, todos poseen el **mismo espaciado interplanar $d_{hkl}$** y la **misma densidad planar de átomos $\rho_p$**.
2. **Propiedad de Ortogonalidad:** En todos los casos, el vector director normal al plano trazado es proporcional al vector de índices $[h\, k\, l]$, cumpliendo rigurosamente la perpendicularidad cristalográfica en redes cúbicas [Session 3 Slide 52].

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
