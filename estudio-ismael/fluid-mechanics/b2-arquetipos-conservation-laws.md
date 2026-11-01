# B2 Leyes de Conservación (Tema 3 completo): selección top

Hecho el 2026-10-31. Este hilo cubre todo el Tema 3 (masa, cantidad de movimiento, momento cinético, energía, VC móvil y deformable), es decir, lo que el plan original separaba en B2 y B3.

Fuentes revisadas: enunciados de `vault/01 - Fluid Mechanics/Problem - CL1..CL22.md`, `FLUIDS_FIRSTPARTIAL_2011..2025.pdf` y los apuntes de clase de Ismael (`estudio-ismael/fluid-mechanics/Notas/ClassNotes.pdf`, 6 páginas, leídos como imagen). **Hechos en clase, en este orden:** deducción de la ecuación de energía integral, **CL6, CL5, CL4, CL11** y un **Extra exercise (jeringa/inyector con pistón, casi estacionario; la profesora dejó los apartados 3 y 5 para casa)**; luego Tema 4 con **NS1** y **NS3** (ver `metodo-profesora.md`).

Por qué pesa tanto este tema: el problema CL sale en 9 de 10 primeros parciales, casi siempre con el mismo paquete (caudal/velocidad por continuidad → fuerza → momento respecto a un punto → calor o energía), y desde 2020 a menudo con una parte transitoria o de VC deformable. Varios CL de la hoja **son exámenes antiguos**: CL11 (parcial 2011), CL12 (examen 16-12-2011), CL19 (prefinal 2013), CL20 (final 2014), CL21 (retake 2014).

## Método de la profesora (lo que se ve en las soluciones de clase)

1. Hipótesis en lista (estacionario, incompresible o gas perfecto, sin g, propiedades uniformes en entradas/salidas, chorro libre → p = p_a).
2. VC dibujado, con cada superficie nombrada (Σ_i, Σ_o, Σ_w...) y su normal **saliente** escrita al lado.
3. Cada balance (masa Eq. 3.11, cantidad de movimiento Eq. 3.36, momento cinético Eq. 3.38, energía Eq. 3.46 de Notes.pdf) **escrito completo**, tachando los términos que se anulan con el motivo debajo.
4. Cada integral de superficie desglosada **superficie por superficie** (una raya vertical bajo la integral con Σ_i | Σ_o | Σ_w).
5. Antes de los balances define, como integrales sobre Σ_w (o Σ_m de las partes móviles), lo que pide el enunciado: F (fuerza del fluido interior y del aire ambiente sobre el aparato), Q y W, cada uno con su signo y en una caja.
6. Los términos de pared se agrupan en una caja = −F (fuerza del fluido y del aire sobre el sólido), restando p_a en todo el contorno para trabajar con presión manométrica.
7. En gases: h = c_p T = γ/(γ−1) · p/ρ.
8. Bernoulli solo donde se cumplen sus 4 hipótesis (estacionario, ρ constante, sin viscosidad, fuerzas másicas conservativas), escrito como ecuación aparte y numerado.
9. En transitorios lentos compara órdenes de magnitud del término no estacionario y del convectivo para justificar "casi estacionario".

## Lista ordenada (núcleo: hacer todos)

**Nivel 1: el paquete básico con VC fijo e incompresible**
1. **CL6 Codo con chorro vertical (hecho en clase).** Continuidad → F_x, F_z con presión manométrica → calor Q por la energía. El arquetipo puro.
2. **CL20 Contracción de tubería (final 2014).** Fuerza sobre la contracción y subida de temperatura; ver cómo Bernoulli convierte la energía en "sin pérdidas ⇒ ΔT = 0".
3. **CL3 Doble codo.** Añade el **momento respecto a un punto** (Eq. 3.38): el primer brazo de palanca.
4. **CL16 Chorro plano sobre cuña asimétrica.** Bernoulli en chorros libres, espesores por continuidad, fuerza, momento, α que anula el momento y calor por unidad de superficie. Casi idéntico al **parcial 2016 P1** (placa articulada).
5. **CL8 Chorro contra pared con orificio.** Axisimétrico: chorro radial de pared, espesor h(r), fuerza.

**Nivel 2: máquinas, gases y energía**
6. **CL10 Ventilador.** Bernoulli aguas arriba desde el reposo, **fuerza del aire en reposo alrededor** (la parte que más se falla), energía con potencia W y números.
7. **CL5 Turborreactor en banco (hecho en clase).** Compresible, W extraído y Q añadido, empuje.
8. **CL4 Cascada de perfiles (hecho en clase).** VC periódico: las superficies laterales se cancelan.
9. **CL11 VTOL (hecho en clase, parcial 2011).** Entrada con Bernoulli desde la atmósfera, tobera orientable α, F_x = 0 y F_y = Mg, energía con W y Q.
10. **CL12 Gas en tubo en U invertida (examen 2011).** Tubo aislado: T_o y V_o por energía + estado, fuerza y momento.
11. **CL15 Codo mezclador.** Dos entradas, mezcla, momento respecto al centro de una entrada, aplicación numérica.

**Nivel 3: momento cinético con rotación**
12. **CL13 Bomba centrífuga.** Par y potencia ideal a partir de la componente tangencial de salida.
13. **CL7 Secador industrial.** Salida con v_θ y v_z, fuerza, Q + W y par.

**Nivel 4: VC no estándar**
14. **CL1 Estela de un perfil.** Perfil de velocidad no uniforme, VC limitado por líneas de corriente: integrales de verdad, no solo ρvA.
15. **CL2 Resalto hidráulico.** VC móvil (cambio a sistema que se mueve con el resalto) y presión hidrostática.
16. **CL22 Agua en cilindro que se estrecha.** VC deformable: h(t), v_z(z,t), fuerzas y potencia.

17. **Extra exercise de clase: jeringa con pistón.** VC deformable con L(t), continuidad v_s = v_p (D/d)^2, argumento casi estacionario (término no estacionario / convectivo ~ (d/D)^4 << 1), F_p + F_c, Bernoulli para p_p. **Terminar los apartados 3 (momento respecto a O) y 5 (F_p y F_c por separado)**, que quedaron para casa.

## Problemas de examen (después del núcleo, a reloj)

- **Parcial 2025, aspersor** (caudales por rama, fuerza con gravedad, momento, calores, disipación).
- **Parcial 2024, chorro sobre placa caliente** (continuidad, energía, cantidad de movimiento).
- **Parcial 2016 P1, chorro sobre placa articulada** (U1, U2, reacción en la bisagra, h1 y h2, momento → α, temperatura).
- **Parcial 2020 P1, doble codo + llenado transitorio** (t1, t2, fuerza y par durante el llenado).
- **Parcial 2021 P1, cámara 2D con pistones** (VC deformable; apartados 1-4; el resto es NS).
- **Parcial 2014 P1, inyector.**
- Parcial 2017 P1 (caudalímetro con cuña): apartados 1-5 si sobra tiempo.

## Descartados por equivalentes (reserva)

- **CL9** (propulsor de submarino) = CL10.
- **CL19** (codo mezclando dos gases) = CL15 + CL12.
- **CL21** (fila de cilindros calientes) = CL4.
- **CL14** (difusor de turbina) y **CL17** (motor y canard) = CL7/CL13 en momento cinético; CL17 es buena reserva de momento respecto al CdG.
- **CL18** (eyector): Bernoulli + cantidad de movimiento con mezcla; reserva si sobra tiempo.

## Progreso y errores (se rellena en el hilo)

- (pendiente)
