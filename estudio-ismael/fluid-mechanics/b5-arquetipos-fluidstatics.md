# B5 - Fluid Statics (Topic 5): arquetipos para el parcial (5 nov 2026)

Fuente: `sources/cuatrimestre-1/01-fluid-mechanics/unit-05-hydrostatics/problemas/fluid_statics_1..10.pdf`.
Teoría: Notes.pdf cap. 5 (pp. 51-56). Ecuaciones clave: 5.2 ($-\nabla p+\rho \bar f_m=0$), 5.10 ($p+\rho g z = p_a$), 5.11 ($\bar F=-\int p\bar n\,d\sigma$, y momento 5.13), 5.14 (proyección: fuerza horizontal = fuerza sobre la proyección vertical), 5.15-5.16 (Arquímedes).
En clase solo se resolvió FS10. No hay precedente en parciales del repo (2011-2025 eran Temas 1-4): lo más probable es una pregunta corta.

## Orden de trabajo (por rendimiento)

| # | Problema | Arquetipo | Por qué |
| :--- | :--- | :--- | :--- |
| 1 | **FS10** cilindro entre dos niveles | Fuerza horizontal sobre superficie curva: integración en polares + regla de proyección (5.14) | Único hecho en clase. Prioridad máxima. |
| 2 | **FS4** válvula cuadrada sobre su eje central | Superficie plana: fuerza y momento con $p=p_a+\rho g(h-z)$, centro de presiones | El más estándar de examen. |
| 3 | **FS3** cubo hueco con aire atrapado | Arquímedes + aire isotermo ($p V$ = cte) + hidrostática entre dos superficies libres | Cubre también FS6 (misma idea, otra geometría). |
| 4 | **FS2** estación semiesférica en el fondo | Superficie curva 3D, componente vertical; comprobar con "peso del volumen sobre la superficie" | Cubre FS8 (mismo ejercicio escaneado dos veces). |
| 5 | **FS9** compuerta articulada | Momento de presiones respecto a la bisagra = 0 | Cubre FS5 (compuerta entre dos líquidos). |

Opcionales si sobra tiempo: FS1 (cubito de hielo, Arquímedes + masa) y FS7 (cuña entre dos líquidos).
Se saltan: FS5, FS6, FS8 (redundantes con los anteriores).

## Teoría corta sin apuntes (por si cae en la parte 1)
- $-\nabla p+\rho\bar f_m=0$; con gravedad, $p+\rho g z$ = cte en un líquido.
- Arquímedes: empuje = peso del fluido desalojado, aplicado en el centroide del volumen desalojado.
- Estabilidad de un cuerpo totalmente sumergido: centro de empuje por encima del centro de gravedad.
- Atmósfera estándar: $dp/dz=-\rho g$, $p=\rho R_g T$, $T=T_0-\alpha z$ hasta 11 km, constante hasta 20 km.

## Progreso
- [ ] FS10
- [ ] FS4
- [ ] FS3
- [ ] FS2
- [ ] FS9
