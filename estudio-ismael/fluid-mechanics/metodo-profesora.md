# Método de la profesora (sacado de los apuntes de clase de Ismael)

Fuente: `estudio-ismael/fluid-mechanics/Notas/ClassNotes.pdf` (6 páginas, la 6 en blanco), leído como imagen el 2026-10-31. Lo que pone entre comillas es lectura de manuscrito.

## Tema 3, forma integral (CL6, CL5, CL4, CL11, Extra)

- Hipótesis en lista bajo el dibujo ("neglect g", "uniform properties at inlet/outlet", "free jet", "compressible", "steady"). Incógnitas con "?" junto al dibujo.
- VC punteado en azul, cada superficie nombrada (Σ_i, Σ_o, Σ_w, Σ_m, Σ_l1, Σ_l2) y con la normal saliente dibujada.
- Primero define lo que piden como integral de pared, en caja: F (fluido interior + aire ambiente sobre el aparato), Q (conducción por Σ_w más fuente volumétrica Q_R), W (solo Σ_m, la única superficie que se mueve).
- Cada balance completo (masa, momentum, energía), tachando en rojo los términos nulos con el motivo ("steady", "neglect g").
- Raya vertical bajo cada integral con la contribución de cada superficie; los términos de pared se meten en una caja y se identifican con −F, −W o Q.
- Resultados numerados (1), (2), (3)...; Bernoulli como ecuación aparte numerada.
- Gas perfecto: h = c_p T = γ/(γ−1) p/ρ.
- Transitorio (Extra, jeringa): VC con L(t); compara término no estacionario y convectivo, (d/D)^4 << 1 → "quasi-steady", y lo justifica antes de despreciarlo.

## Tema 4, forma diferencial (para B4/B5)

- Deduce continuidad, momentum y energía diferenciales desde la forma integral con Leibniz (2.6) + Gauss (2.9), y las reduce a las formas con D/Dt. Ecuaciones de cierre: Navier-Poisson, Fourier, 2 ecuaciones de estado (líquido: ρ cte, e = cT; gas: p = ρR_gT, e = c_vT).
- Bernoulli deducido de momentum con sus 4 hipótesis: estacionario, incompresible, viscosidad despreciable, fuerzas másicas conservativas. Constante a lo largo de línea de corriente (o en todo el campo si es irrotacional).
- **NS1 (placa con succión, v_y = −v_w):** hipótesis en lista (steady, plane, perfect liquid const ρ, μ, c, k); condiciones de contorno escritas antes de empezar; continuidad → v_y constante; momentum x, y, z escritas completas tachando términos; EDO → v_x = U_∞(1 − exp(−v_w y/ν)); presión hidrostática; energía con disipación Φ_v; flujo de calor a la pared q = −k ∂T/∂y en y = 0; líneas de corriente dx/v_x = dy/v_y.
- **NS3 (esfera pulsante, R(t)):** simetría esférica → v_θ = v_φ = 0; continuidad → r² v_r = C(t), con v_r(R) = Ṙ → v_r = R²Ṙ/r²; momentum radial → p(r,t); potencia sobre la burbuja W = −∫ p v·n + ∫ (τ'·n)·v en r = R, con τ' en esféricas evaluado en la pared (da el término 4μṘ²/R).
