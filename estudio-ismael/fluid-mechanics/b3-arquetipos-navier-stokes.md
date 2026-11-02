# B3 - Navier-Stokes (Topic 4): lista de problemas

Creado 2026-11-02. Peso reducido (ver plan-final-parcial-2026.md, sección 4): NS cae como pregunta corta o apartado del problema largo. Se entrena el **planteamiento**, 10-15 min por problema.

## Qué se entrena en cada uno
1. Hipótesis de simetría -> forma del campo (qué depende de qué).
2. Continuidad -> velocidad normal.
3. NS componente a componente: qué términos se anulan y por qué.
4. Condiciones de contorno (no deslizamiento, succión, superficie libre, infinito).
5. Esfuerzo viscoso en la pared (y flujo de calor si lo piden).

Ecuaciones de Notes.pdf (cap. 4): continuidad Eq. 4.7, cantidad de movimiento incompresible Eq. 4.12 / 4.41, energía líquido perfecto Eq. 4.42.

## Orden
| # | Problema | Arquetipo | Por qué | Estado |
| :--- | :--- | :--- | :--- | :--- |
| 1 | NS1 Pared porosa con succión | Cartesiano 1D con v_z = const; perfil exponencial; T con disipación | De clase. Succión: continuidad da v_z constante, convección no nula | Pendiente |
| 2 | NS3 Globo esférico de radio variable | Radial esférico, no estacionario; continuidad da v_r = R^2 dR/dt / r^2; presión por NS radial | De clase. Patrón de la "esfera pulsante" de 2014/2020 | Pendiente |
| 3 | NS7 Película sobre plano inclinado | Paralelo con superficie libre; gravedad motriz; esfuerzo nulo en la superficie | De clase. Condición de superficie libre | Pendiente |
| 4 | NS5 Cilindro arrastrando una capa de líquido | Cilíndricas, superficie libre | Opcional | Opcional |
| 5 | FIRSTPARTIAL 2022 micro-túnel, apartados 1-3 | Continuidad, p = p(x), Poiseuille | Cómo entra NS en un problema actual | Pendiente |

Fuera (solo si sobra tiempo): esfera pulsante 2014/2020, disco poroso 2016.
