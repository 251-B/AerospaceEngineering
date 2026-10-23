# Lab 1 → Lab 2 Engineering Mechanics Handover

Lo que aprendimos y fijamos en el Lab 1 (partícula unida a un carrete), para empezar el Lab 2 (*Particle on oscillating loop*, `mechanics_labs.pdf` pp. 17–18) sin repetir errores. Todo lo que aparece aquí ocurrió en el chat del Lab 1. Donde el prompt de handover pedía algo que no hicimos así, se indica.

---

## 1. Metadatos y requisitos del entregable

- **Asignatura:** Mechanics Applied to Aerospace Engineering, UC3M, 2º curso del Grado en Ingeniería Aeroespacial, curso 2026/27. Profesor de laboratorio: Iñaki Fernández Tena (diapositivas `Lab1_notes.pptx`).
- **Autores:** Ismael Martín Díez, David Martín García, Alejandro Ranz Remartínez.
- **Grupo:** la portada dice "Authors (Group B)" y los archivos usan `LB` (grupo de laboratorio B). La guía usa `Li` = `LA`/`LB`.
- **Normativa** (`mechanics_labs.pdf`, General guidelines y p. 16):
  - Lo sube un solo alumno a AulaGlobal, en el grupo de laboratorio correspondiente.
  - Zip: `Group_Li_S1_S2_S3.zip`, con S1–S3 = primer apellido de cada alumno. La guía escribe los nombres con espacios; nosotros usamos `Group_LB_Martin_Martin_Ranz.zip` y al subirlo se quedó como `Group LB_Martin_Martin_Ranz.zip`. Para el Lab 2 conviene un único criterio, comprobado en AulaGlobal.
  - Dentro del zip:
    - `Report_LB_Martin_Martin_Ranz.pdf`, de **10 páginas como máximo**. Nosotros contamos la portada y el índice dentro de esas 10. Los nombres completos de los tres alumnos deben ir en la portada.
    - `code_LB_Martin_Martin_Ranz/main.m`: script principal, se ejecuta sin ninguna entrada del usuario y produce todos los resultados. El profesor lo corre desde esa carpeta, y hay penalización si falla.
  - Nada más en la carpeta del código: ni `main.asv`, ni copias `.txt` (nos pasó con `main.mAlejandro.txt`), ni `figures/`, que se genera al ejecutar.
  - El incumplimiento de las normas de redacción puede suponer un 0.
- **Diapositivas del profesor** (`Lab1_notes.pptx`):
  - La introducción es obligatoria; hubo grupos con 0 por no ponerla.
  - Estructura: Introduction → Methodology → Results → Discussion → Conclusion.
  - Una figura sin comentario no vale nada. En la discusión hay que explicar *por qué* pasa algo, no describir la curva.
  - Hay punto extra por hacerlo en LaTeX.
  - Sin capturas de pantalla de ecuaciones y sin código dentro del informe.
  - La fuente de las figuras debe ser "aproximadamente del tamaño del texto".
  - No reescribir las preguntas del enunciado, pero sí responderlas todas.

## 2. Estándar LaTeX (Overleaf)

### Preámbulo validado (copiado del informe de Fluidos, que el equipo pidió replicar)
Ver §6.1. Puntos clave:
- `geometry` con margen de 2.5 cm, `\parindent 0pt`, `\parskip 0.6em` y `\numberwithin{equation}{section}`.
- `siunitx` con `detect-all, per-mode=symbol`. Usar `\SI{}{}`, `\si{}` y `\num{}`, no `\qty`, por compatibilidad. En Tectonic/XeTeX, `\micro` no renderiza: escribir `\SI{e-6}{m}`.
- `float` con `[H]` para que cada figura quede **justo debajo del párrafo de su caso**. Fue una petición explícita del equipo.
- `hyperref` con `[hidelinks]`. Referencias como `Eq.~\eqref{}`, `Fig.~\ref{}` y `Table~\ref{}`; sin `cleveref`.

### Estructura del informe final (la que se entregó)
1. Portada (`titlepage`): dos `\rule{\linewidth}{1.2pt}`, título en medio, autores alineados a la izquierda, fecha.
2. `\tableofcontents` + `\newpage`. **Sin abstract**: el equipo lo eliminó expresamente.
3. *Introduction and Problem Statement*: introducción en prosa, enunciado con figura (`wrapfigure`), grados de libertad y ligadura, sistema de referencia y base, posición/velocidad/aceleración (puntos 1–2 de la guía).
4. *Mathematical Model and Dynamical Formulation*: fuerzas, EDO sin la tensión y expresión de $T$ (puntos 3–4).
5. *Numerical Solution in Matlab*: forma de espacio de estados, `diffeq`, opciones y `stopfun` (puntos 5–6).
6. *Simulation Results and Trajectories*: un párrafo por caso con su figura 2×2 debajo; la Tabla 1 resumen al final de la sección (puntos 7–8).
7. *Physical Discussion and Energy*: 5.1 energía mecánica (punto 9) y 5.2 eventos críticos, respondiendo cada pregunta del punto 10 con frases sencillas.
8. *Motion After the Loss of Tension* (punto 11): **solo la discusión** de qué cambios necesitaría el código. La guía no pide implementarlo y el equipo pidió quitar la simulación.
9. *Conclusions*: viñetas y una frase final.
10. *References*: bibliografía sin citas en el texto, con `\nocite{*}` + `unsrt`. Entradas finales: guía, diapositivas, Meriam & Kraige, documentación de MATLAB de `ode45` y `odeset`.

> El prompt pedía las secciones "Theoretical Methodology & Kinematics / Energy Balance / Physical Diagnostics": no fue así. Arriba está la estructura real entregada.

### Cómo cumplimos el límite de 10 páginas
- Cada figura de caso es un único PNG 2×2 (φ y ξ con `yyaxis`, T, trayectoria, E) a `0.85\textwidth` y altura reducida: ventana de MATLAB de 900×480. Con figuras altas, `[H]` dejaba huecos enormes y el informe pasaba a 12 páginas.
- La Tabla 1 se movió al final de la sección 4 para quitar un hueco en la página 4.
- El pie de la Fig. 1 se acortó a dos líneas, y el resto de figuras usa "Panels and markers as in Fig. 1".
- Se eliminaron los extras: residuos de energía, cuadratura de verificación, simulación balística, periodo del caso 2 e invariancia adiabática.
- Para comprobar el número de páginas, compilar (Tectonic o Overleaf) y mirar las páginas, no estimar.

## 3. Estándar analítico (lo que aplicamos en el Lab 1)

### Grados de libertad y ligadura
- $P$ en el plano tiene 2 coordenadas $(\phi,\xi)$. La cuerda inextensible añade una ligadura **holónoma y reónoma**:
  $$a(\theta_{A0}+\omega t-\phi)+\xi=l \;\Rightarrow\; \xi(t,\phi)=\xi_0-a(\omega t-\phi),\qquad \text{C.D.O.F.}=2-1=1$$
- **Signo:** la parte enrollada va desde $B$ en sentido antihorario hasta el anclaje $A$. Si $\phi$ crece, se desenrolla cuerda ($\dot\xi=+a\dot\phi$); si el carrete gira en sentido antihorario, la enrolla ($-a\omega$). La nota antigua de Obsidian tenía el signo de $\phi$ al revés, lo que daba una velocidad y una EDO erróneas. Hay que comprobarlo siempre contra la solución manuscrita oficial (`AnaliticSolutionLab1Mech2ndTry.pdf`).

### Base y matriz de cambio de base
$$\hat{\mathbf e}_r=\cos\phi\,\hat{\boldsymbol\imath}+\sin\phi\,\hat{\boldsymbol\jmath},\quad \hat{\mathbf e}_\phi=-\sin\phi\,\hat{\boldsymbol\imath}+\cos\phi\,\hat{\boldsymbol\jmath},\quad [R(\phi)]=\begin{pmatrix}\cos\phi&\sin\phi\\-\sin\phi&\cos\phi\end{pmatrix},\ \det R=1,\ RR^T=I$$
Las derivadas se calculan **con la regla de la cadena explícita**, no con Poisson: $\dot{\hat{\mathbf e}}_r=\frac{d\hat{\mathbf e}_r}{d\phi}\dot\phi=\dot\phi\,\hat{\mathbf e}_\phi$ y $\dot{\hat{\mathbf e}}_\phi=-\dot\phi\,\hat{\mathbf e}_r$.
> Para el Lab 2 (aro que gira con $\Omega(t)$ alrededor de $Oy$) sí harán falta $S_0$ inercial, $S_1$ ligado al aro, la matriz $[{}_0R_1]$ con el ángulo $\int\Omega\,dt$ y las fuerzas de inercia de arrastre y Coriolis, porque la guía pide plantear la dinámica en el sistema rotatorio (punto 3). Cada signo menos debe justificarse con la regla de la mano derecha (⊙/⊗), según `AGENTS.md`.

### Cinemática (sin saltos)
$$\mathbf r_P=a\hat{\mathbf e}_r-\xi\hat{\mathbf e}_\phi,\qquad \mathbf v_P=a\dot\phi\hat{\mathbf e}_\phi-(a\dot\phi-a\omega)\hat{\mathbf e}_\phi+\xi\dot\phi\hat{\mathbf e}_r=\xi\dot\phi\,\hat{\mathbf e}_r+a\omega\,\hat{\mathbf e}_\phi$$
Hay que **mostrar la cancelación** de los términos $a\dot\phi\,\hat{\mathbf e}_\phi$. La aceleración es
$$\mathbf a_P=(a\dot\phi^2+\xi\ddot\phi-2a\omega\dot\phi)\hat{\mathbf e}_r+\xi\dot\phi^2\hat{\mathbf e}_\phi$$

### Fuerzas, EDO y tensión
$\mathbf T=T\hat{\mathbf e}_\phi$ (con $T\ge0$) y $m\mathbf g=-mg(\sin\phi\,\hat{\mathbf e}_r+\cos\phi\,\hat{\mathbf e}_\phi)$. Proyectando:
$$\ddot\phi=\frac{-g\sin\phi-a\dot\phi^2+2a\omega\dot\phi}{\xi_0-a(\omega t-\phi)},\qquad T=m\xi\dot\phi^2+mg\cos\phi$$
Va acompañado de una comprobación dimensional en una línea.

### Energía (punto 9)
$$E=\tfrac12m(\xi^2\dot\phi^2+a^2\omega^2)+mg(a\sin\phi-\xi\cos\phi),\qquad \dot E=\mathbf T\cdot\mathbf v_P=Ta\omega$$
La energía se conserva **si y solo si** $\omega=0$. Con $\omega>0$ crece, porque el motor del carrete trabaja contra la tensión. Caso 1: $E=E_0+mga\omega t$ exacto.

### Condición inicial
La guía da $\dot x_P(0)$, no $\dot\phi_0$. Con $\phi_0=0$ se tiene $\dot x_P(0)=\xi_0\dot\phi_0$, así que $\dot\phi_0=\dot x_P(0)/\xi_0$.

## 4. Estándar de código MATLAB (`main.m`)

- **Un solo archivo**, al estilo de `example1.m`: script lineal con un bucle `for k = 1:5` y, al final, las funciones locales `diffeq` y `stopfun`. Nada de structs, cells ni funciones auxiliares de dibujo: el equipo pidió que pareciera código de alumno.
- **`groot`:** `defaultAxesTickLabelInterpreter`, `defaultTextInterpreter` y `defaultLegendInterpreter` a `'latex'`, `defaultLineLineWidth` 1.5 y `defaultAxesFontSize` 12. Etiquetas con unidades: `'$t$ [s]'`, `'$\phi$ [rad]'`, `'$T$ [N]'`, `'$E$ [J]'`.
- **`odeset`:** `'RelTol', 1e-8, 'MaxStep', 0.01`.
  - Se probó `RelTol = 0.01`, tal como venía en un prompt: el caso 1 falla con `odezero: an event disappeared`, el caso 4 no detecta $T=0$ (integra hasta 100 s y la energía pasa de −0.18 a −0.72 J) y la energía del caso 3 deriva un 7 %. `example1.m` usa 0.01 solo para **enseñar** qué pasa con una tolerancia mala.
  - Sin `MaxStep`, el caso 1 falla con cualquier tolerancia.
- **Eventos:** `value = [xi - 1e-6; T]`, `isterminal = [1;1]`, `direction = [-1;-1]`. Con $\xi=0$ exacto, `ode45` no llega (porque $\xi\propto\sqrt{t_c-t}$) y aborta sin reportar el evento. Se explica en una frase en el informe.
- **Resultados por consola:** **todo número que aparece en el informe sale por `fprintf`**: tabla, rangos, máximos y mínimos, tiempos y velocidades. Fue un requisito explícito, para que el profesor vea que nada está inventado. Hay que cotejar las cifras del texto con la salida, con el mismo número de decimales.
- **Figuras:** `figure('Position',[100 100 900 480],'Color','w')` + `try theme(fig,'light'); end` (en R2025a el tema oscuro por defecto exporta texto gris sobre fondo negro) + `exportgraphics(fig, sprintf('figures/case%d.png',k), 'Resolution', 200)`. Se usó 200 dpi, no 300. `isfolder('figures')` en vez de `exist(...,'dir')`, que daba un falso positivo con carpetas del path.
- **Escalas especiales:** T en escala logarítmica (caso 3) o recortada (`ylim([0 4])`, caso 5) cuando diverge. E con `ylim(E0 ± 0.5)` si $\omega=0$. `ylim([-6 0])` para φ en el caso 3, porque si no, φ y ξ quedan superpuestas.
- **Verificación antes de entregar:** copiar la carpeta a un directorio limpio, ejecutar `matlab -batch "cd(...); main"`, exigir código de salida 0 y sin warnings, y comparar las figuras píxel a píxel con las del informe.

## 5. Registro de errores y correcciones del Lab 1

**Analíticos y de contenido**
- Borrador de David:
  - decía que ξ es constante en el caso 2 (falso: $\xi=1+0.2\phi$, entre 0.934 y 1.063 m);
  - daba $E_0=-0.9790$ J en el caso 1 (el valor correcto es −0.98098 J);
  - decía que el caso 5 terminaba por "forced winding" sin comprobar el evento real (contacto en 35.509 s, con $T_{min}=0.46$ N).
- Nota de Obsidian: signo de la ligadura invertido (ver §3).
- Caso 4: la cuerda se destensa en el **vaivén izquierdo** ($t=1.69347$ s, $\phi=-1.5859$ rad), no en el derecho, porque $\phi_{max}=1.26667<\pi/2$. Condición: $T=0$ solo si $\cos\phi<0$ (es decir, $|\phi|>\pi/2$), con $\xi\dot\phi^2=g|\cos\phi|=0.148$ m/s².
- Caso 3: contacto en $t=0.270947$ s, $\phi=-5$ rad, $P=(0.05673, 0.19178)$ m. $|\dot\phi|=v/\xi$ diverge mientras la velocidad sigue finita ($v_c=8.75$ m/s).
- Caso 5:
  - la amplitud no es "0.32 → 0.73 rad" (dato mal muestreado): es 0.3164 → 0.7006 rad a la derecha y −0.3360 → −1.0880 rad a la izquierda;
  - la parada es $\omega t-\phi=\xi_0/a=5$ rad (con $\omega t=3.551$), 14.5 s antes que el caso 1.
- Cifra 8.76 → 8.75 m/s para cuadrar con la consola.
- Se redondeaba con datos de scripts auxiliares que `main.m` no imprimía: **todo dato tiene que salir de `main.m`**.

**Numéricos y de código**
- Tolerancia, `MaxStep` y $\xi_{tol}$ (ver §4).
- Al juntar líneas con `...` se perdieron dos paréntesis en `odeset` y `ode45`, lo que da un error de sintaxis. Hay que ejecutar siempre después de editar.
- Una versión de un compañero perdió `theme(fig,'light')` (las figuras salieron oscuras), el `ylim` del caso 3 y la mitad de los `fprintf`. Hay que comparar contra la versión verificada antes de entregar.

**Redacción y maquetación**
- Pasada de humanizer:
  - quitar marcadores de IA ("genuine", "independent confirmation", títulos rimbombantes);
  - escribir frases directas, en tercera persona y con algún "we";
  - el equipo quiso **mantener sus propios errores de inglés** por autenticidad.
- La sección 5.2 se reescribió "a un nivel más simple", con una pregunta de la guía por párrafo.
- Se eliminó todo lo que no pide la guía (punto 11 solo como discusión).
- Figuras debajo de su caso con `[H]`, Tabla 1 al final de la sección 4.
- Análisis crítico pendiente de mejora: validar numéricamente la solución (energía constante en los casos 2–4 y solución exacta del caso 1), los límites del modelo cerca de $\xi\to0$ y lo irreal de $T\sim10^6$ N. Es lo más barato de ganar en el Lab 2.

## 6. Esqueletos

### 6.1 Preámbulo LaTeX
```latex
\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}
\usepackage[a4paper,margin=2.5cm]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{siunitx}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{caption}
\usepackage{float}
\usepackage{subcaption}
\usepackage{enumitem}
\usepackage{xcolor}
\usepackage{wrapfig}
\usepackage[hidelinks]{hyperref}

\sisetup{detect-all, per-mode=symbol}
\captionsetup{font=small, labelfont=bf}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.6em}
\numberwithin{equation}{section}
\graphicspath{{figures/}}

\newcommand{\er}{\hat{\mathbf{e}}_r}
\newcommand{\ephi}{\hat{\mathbf{e}}_\phi}
\newcommand{\ii}{\hat{\boldsymbol{\imath}}}
\newcommand{\jj}{\hat{\boldsymbol{\jmath}}}
\newcommand{\vect}[1]{\mathbf{#1}}

\begin{document}
\begin{titlepage}
\centering
\vspace*{3cm}
{\Huge\scshape Universidad Carlos III de Madrid\par}\vspace{0.4cm}
{\large Bachelor in Aerospace Engineering\par}\vspace{1.2cm}
{\Large Mechanics Applied to Aerospace Engineering\par}\vspace{0.8cm}
\rule{\linewidth}{1.2pt}\\[0.3cm]
{\LARGE\bfseries Particle on Oscillating Loop\par}\vspace{0.3cm}
\rule{\linewidth}{1.2pt}\\[0.8cm]
{\large Laboratory Session 2\par}\vspace{1.2cm}
\begin{flushleft}
\hspace{1.2cm}\textit{Authors (Group B):}\\
\hspace{1.2cm}Ismael Mart\'in D\'iez\\
\hspace{1.2cm}David Mart\'in Garc\'ia\\
\hspace{1.2cm}Alejandro Ranz Remart\'inez
\end{flushleft}
\vspace{1cm}{\large\textbf{Report date:} ...}\vfill
\end{titlepage}
\tableofcontents
\newpage

\section{Introduction and Problem Statement}
\section{Mathematical Model and Dynamical Formulation}
\section{Numerical Solution in Matlab}
\section{Simulation Results}
% \textbf{Case ...} paragraph, then \begin{figure}[H] ... \end{figure}
\section{Physical Discussion}
\section{Conclusions}

\nocite{*}
{\footnotesize
\bibliographystyle{unsrt}
\bibliography{references}}
\end{document}
```

### 6.2 Plantilla de `main.m`
```matlab
%% Laboratory 2: Particle on oscillating loop
% Mechanics Applied to Aerospace Engineering, UC3M
% Ismael Martin Diez, David Martin Garcia, Alejandro Ranz Remartinez
clc
clear
close all

% Plot formatting
set(groot, 'defaultAxesTickLabelInterpreter', 'latex');
set(groot, 'defaultTextInterpreter', 'latex');
set(groot, 'defaultLegendInterpreter', 'latex');
set(groot, 'defaultLineLineWidth', 1.5);
set(groot, 'defaultAxesFontSize', 12);

if ~isfolder('figures')
    mkdir('figures')
end

% Data (mechanics_labs.pdf, Sec. 2.1)
g = 9.81; m = 1; R = 1; A = pi; w = 0.1;
X0 = [0; 0];                     % [varphi; varphidot]
Tp = 2*pi/w;                     % period of the rotating frame
tf = 3*Tp;

options = odeset('RelTol', 1e-8, 'MaxStep', 0.01);
[t, X] = ode45(@(t, X) diffeq(t, X, g, R, A, w), [0 tf], X0, options);

phi = X(:,1); phidot = X(:,2);
% ... reactions, inertia forces, energies from the report formulas

% every number quoted in the report printed here
fprintf('t_end = %.5f s\n', t(end));

fig = figure('Position', [100 100 900 480], 'Color', 'w');
try
    theme(fig, 'light');
end
plot(t, phi)
xlabel('$t$ [s]'); ylabel('$\varphi$ [rad]'); grid on
exportgraphics(fig, 'figures/phi.png', 'Resolution', 200)

%% Functions
function Xdot = diffeq(t, X, g, R, A, w)
% from the equation of motion derived in the report
phiddot = 0; % TODO
Xdot = [X(2); phiddot];
end
```
`diffeq` queda vacía a propósito: la EDO del Lab 2 se deduce primero en el informe, a partir de la cinemática en el sistema rotatorio. Si hace falta parar la integración (en el Lab 2 no es obvio, porque la guía da un intervalo fijo $t\in[0,3T]$), se añade `'Events'` como en el Lab 1.

## 7. Checklist antes de entregar el Lab 2
1. `main.m` corre en una carpeta limpia, con código de salida 0 y sin warnings.
2. Cada número del PDF aparece en la consola con los mismos decimales.
3. Las figuras del PDF son las que genera `main.m` (comparadas píxel a píxel), con fondo claro y sin curvas tapadas.
4. El PDF tiene ≤ 10 páginas y no tiene puntos dobles ni referencias rotas.
5. El zip contiene solo `Report_...pdf` y `code_.../main.m`, con nombres según la guía.
6. Se ha respondido a cada punto numerado de la guía, y nada más.
