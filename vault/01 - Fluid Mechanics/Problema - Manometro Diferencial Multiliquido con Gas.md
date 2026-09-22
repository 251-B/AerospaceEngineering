---
materia: Fluid Mechanics
tema: "Tema 1: Estática de Fluidos"
origen: "Examen Parcial Típico — 2º Curso Aeroespacial"
dificultad: media
tags:
  - problema-examen
  - resuelto
  - manometria
---

# ✏️ Problema: Manómetro Diferencial Multilíquido con Presurización de Gas

## 📄 Enunciado
Un depósito cerrado $A$ contiene aire presurizado sobre una capa de aceite de densidad relativa $SG_{\text{aceite}} = 0.85$. El depósito está conectado mediante un manómetro en $U$ invertido y un manómetro en $U$ de mercurio ($SG_{\text{Hg}} = 13.6$) a una tubería $B$ por la que circula agua ($\rho_{\text{agua}} = 1000\text{ kg/m}^3$).

Las cotas geométricas medidas respecto a un plano de referencia horizontal son:
* Superficie libre del aceite en el depósito $A$: $z_1 = 3.50\text{ m}$
* Menisco inferior aceite-mercurio en el tubo en U: $z_2 = 1.20\text{ m}$
* Menisco superior mercurio-agua en el tubo en U: $z_3 = 1.80\text{ m}$
* Eje de la tubería $B$ con agua: $z_4 = 2.40\text{ m}$

Si la presión manométrica leída en el aire del depósito $A$ es $p_{A,\text{aire}} = 45\text{ kPa}$, **determinar la presión manométrica en el centro de la tubería $B$** ($p_B$).  
*(Dato: $g = 9.81\text{ m/s}^2$)*.

---

## 📊 1. Identificación de Datos e Hipótesis

### Datos Numéricos:
* $ \rho_{\text{agua}} = 1000\text{ kg/m}^3 $
* $ \rho_{\text{aceite}} = 0.85 \times 1000 = 850\text{ kg/m}^3 $
* $ \rho_{\text{Hg}} = 13.6 \times 1000 = 13\,600\text{ kg/m}^3 $
* $ p_{A,\text{aire}} = 45\,000\text{ Pa} $
* $ z_1 = 3.50\text{ m}, \quad z_2 = 1.20\text{ m}, \quad z_3 = 1.80\text{ m}, \quad z_4 = 2.40\text{ m} $

### Hipótesis de Partida:
* [x] Fluido estático en todas las ramas manométricas.
* [x] La presión del aire sobre el aceite en $A$ es uniforme en toda la cámara de gas (se desprecia el peso de la columna de aire).
* [x] Líquidos incompresibles e inmiscibles con interfaces netas.

---

## 🧠 2. Estrategia y Planteamiento Físico
Aplicaremos el método de la marcha manométrica paso a paso comenzando en el aire de $A$ hasta llegar al centro de la tubería $B$:
1. Desde la superficie del aceite ($z_1$) descendemos hasta el menisco inferior con el mercurio ($z_2$): **suma de presión** $+\rho_{\text{aceite}} g (z_1 - z_2)$.
2. En el mercurio, ascendemos desde $z_2$ hasta el menisco superior con agua ($z_3$): **resta de presión** $-\rho_{\text{Hg}} g (z_3 - z_2)$.
3. En el agua, ascendemos desde $z_3$ hasta el eje de la tubería ($z_4$): **resta de presión** $-\rho_{\text{agua}} g (z_4 - z_3)$.
4. El resultado final iguala a $p_B$.

---

## 🔢 3. Resolución Matemática Paso a Paso

### Ecuación de marcha piezométrica:
$$ p_A + \rho_{\text{aceite}} g (z_1 - z_2) - \rho_{\text{Hg}} g (z_3 - z_2) - \rho_{\text{agua}} g (z_4 - z_3) = p_B $$

### Cálculo término a término:

1. **Columna de aceite (descenso de $3.50\text{ m}$ a $1.20\text{ m} \implies \Delta h_1 = 2.30\text{ m}$):**
   $$ \Delta p_{\text{aceite}} = 850 \times 9.81 \times 2.30 = +19\,178.55\text{ Pa} \approx +19.18\text{ kPa} $$

2. **Columna de mercurio (ascenso de $1.20\text{ m}$ a $1.80\text{ m} \implies \Delta h_2 = 0.60\text{ m}$):**
   $$ \Delta p_{\text{Hg}} = -13\,600 \times 9.81 \times 0.60 = -80\,049.60\text{ Pa} \approx -80.05\text{ kPa} $$

3. **Columna de agua (ascenso de $1.80\text{ m}$ a $2.40\text{ m} \implies \Delta h_3 = 0.60\text{ m}$):**
   $$ \Delta p_{\text{agua}} = -1000 \times 9.81 \times 0.60 = -5\,886.00\text{ Pa} \approx -5.89\text{ kPa} $$

### Sustitución final:
$$ p_B = 45\,000 + 19\,178.55 - 80\,049.60 - 5\,886.00 $$
$$ p_B = 45\,000 - 66\,757.05 = \mathbf{-21\,757.05\text{ Pa}} $$

---

## 🎯 4. Resultado Final y Análisis Físico
* **Presión manométrica:** $ \mathbf{p_{B,\text{rel}} = -21.76\text{ kPa}} $
* **Presión absoluta:** (asumiendo $p_{\text{atm}} = 101.325\text{ kPa}$):
  $$ p_{B,\text{abs}} = 101.325 - 21.76 = \mathbf{79.57\text{ kPa}} $$
* **Interpretación:** La presión en la tubería $B$ es subatmosférica (vacío parcial relativo). La densa columna de mercurio de $60\text{ cm}$ compensa con creces tanto la presurización de $45\text{ kPa}$ del depósito como la columna de aceite, succionando la línea $B$.
