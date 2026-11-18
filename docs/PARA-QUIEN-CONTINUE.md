# Para quien continúe: cuentas, "My study" y planetas

Documento de relevo del trabajo hecho en la rama **`claude/vibrant-cray-118glg`** (sesión en la nube de Claude Code, 18 de noviembre de 2026). Todo está commiteado y subido a esa rama. **No se ha fusionado con `main`**: el usuario pidió expresamente no subir a `main` por ahora.

Las reglas generales del repositorio siguen siendo las de `AGENTS.md` y `CLAUDE.md`. Este documento solo cuenta lo nuevo, por qué es así y qué falta.

---

## 1. Qué se ha construido

### 1.1 Sistema de cuentas (modo local)

- **No hay servidor.** Las cuentas, preferencias y datos personales viven **solo en el navegador** (`localStorage`). Las contraseñas nunca se guardan en claro: se guarda un SHA-256 con sal.
- Los botones "Continue with Google / Microsoft" están marcados como **Soon**: no funcionan hasta que haya backend en la nube.
- El script `assets/js/account.js` lo carga `theme.js` en todas las páginas (detrás de `sidebar.js`; ninguna página lleva su propia etiqueta). Hace lo siguiente:
  - pone en la cabecera "Sign in" o un avatar con iniciales y menú (My study, Settings, Appearance, Sign out), dentro del selector de paleta;
  - aplica las preferencias de la cuenta: paleta automática de día/noche y tamaño de texto;
  - registra el estudio (ver 1.4);
  - en las páginas de problemas carga favoritos y notas (ver 1.5).
- Páginas nuevas en la raíz (`account/`):

  | Página | Contenido |
  | :--- | :--- |
  | `account/login.html` | Inicio de sesión. Recuerda la última cuenta ("Welcome back, Alex.") y tiene "Use another account". |
  | `account/signup.html` | Registro y bienvenida en 3 pasos: asignaturas (la primera elegida es la principal), paleta (se aplica en directo) y fechas de examen. |
  | `account/settings.html` | Profile, Subjects (principal y fechas), Appearance (paleta, cambio automático día/noche, tamaño de texto), Study (modo de la hoja de fórmulas, estilo del temporizador) y Privacy and data (qué hay guardado, exportar JSON, borrar cuenta). |
  | `account/dashboard.html` | "My study" (ver 1.3). |

- Estilos en `assets/css/account.css` (páginas) y `assets/css/account-widget.css` (botón de la cabecera). Lógica de las páginas en `assets/js/account-pages.js` (`<body data-page="login|signup|settings|dashboard">`).
- **Las páginas `account/*.html` se mantienen a mano.** Al principio se generaron con scripts temporales que ya no existen, así que hay que editar el HTML directamente.

### 1.2 Cielo de las páginas de entrar y registro

- A la izquierda va una **carta estelar** con aro graduado que gira despacio, nebulosas y una **galaxia espiral barrada** girando en 3D (inspirada en NGC 1300, M74 y M51).
- En los brazos de la galaxia hay **5 cúmulos** sin etiqueta, en los colores de las asignaturas, que se encienden en el registro al elegirlas.
- El cielo está vivo: estrellas que titilan, estrellas con destellos, nebulosa que se desplaza y estrellas fugaces.
- Imágenes prerrenderizadas, porque dibujarlas en directo con SVG era muy pesado:
  - `assets/img/sky/account-nebula.jpg` (27 KB): ruido fractal SVG renderizado una vez sobre negro, que se mezcla con `mix-blend-mode: screen`.
  - `assets/img/sky/account-galaxy.webp` (≈266 KB, transparente): generada por `tools/account_art/galaxy.py` y `tools/account_art/render.js`; las instrucciones están dentro de `render.js`.
- **Decisiones del usuario sobre este cielo** (no deshacerlas):
  - **No** poner nombres de asignaturas junto a la galaxia.
  - **No** mostrar el código "SDR-xxxx" ni el retículo de "tu estrella"; se quitaron a petición suya.
  - **No** usar coordenadas de Leganés en la línea de arriba; solo queda la hora.
  - Se probó un **inicio de sesión con forma de estrella** y **no le gustó**; se revirtió con el commit `72c26bb`. El formulario va en un panel a la derecha.
- Los títulos siguen siendo "Find your star." / "Claim your star.". Se le ofreció al usuario cambiarlos, porque ya no hay estrella marcada, y no respondió.

### 1.3 Panel "My study" (`account/dashboard.html`)

- **Cabecera:** saludo según la hora con la galaxia girando. La galaxia está calculada para caber entera en el rectángulo. Muestra horas de la semana, racha y días al próximo examen.
- **Continue where you left off:** la última página de cada asignatura.
- **Upcoming exams:** cuentas atrás; en rojo cuando quedan 7 días o menos.
- **Favourites and notes:** con filtros All / Favourites / Notes.
- **This week:**
  - barras apiladas por asignatura con línea de media y totales solo en hoy y en el mejor día;
  - ventanita al pasar el ratón;
  - "By subject" con barras horizontales;
  - mapa de calor de las últimas 10 semanas;
  - vista de tabla.
- **Exam simulator:** última nota sobre 10, curva con área, intentos, media, mejor nota e ítems a repasar.
- **Paleta de las gráficas:** `#008bbc` Fluids, `#bc7b04` Materials, `#36ac73` Mechanics, `#6651a9` Maths, `#b14955` Management.
  - Tiene la misma saturación (OKLCH C 0.135) y luminosidad escalonada.
  - Validada con el script del skill `dataviz` para todos los pares: daltonismo ΔE ≥ 9.2 y visión normal ≥ 15.6, en oscuro y en Cream, Sage y blanco.
  - Si se cambia, hay que volver a validarla.

### 1.4 Registro de estudio (solo con sesión iniciada, solo en el navegador)

- **`ae_recent`:** última página de cada asignatura (ruta, título h1, área, fecha).
- **`ae_study_log`:** segundos de estudio por asignatura y día, 70 días.
  - Suma 15 s cada 15 s cuando la pestaña está visible y hubo movimiento en los últimos 2 minutos.
- Lee el historial de los simuladores: `ae_bm_exams`, `ae_mat_exams`, `ae_am_exams`, `ae_em_exams`.

### 1.5 Favoritos y notas en cada problema

- Lo hace `assets/js/problem-marks.js` con `assets/css/problem-marks.css`. Lo carga `account.js` solo en `problemas/` y `extra-problems/` (no en sus índices) y solo con sesión iniciada.
- Pone una estrella y un botón de nota junto a la flecha de plegar de `problem-collapse.js`.
- La nota va **dentro de la cabecera** de la tarjeta, así que se lee aunque la tarjeta esté plegada. Se guarda sola mientras escribes; Done/Esc la cierra.
- Funciona con todos los formatos de tarjeta: `.problem-header`, título suelto y las `<details>` de Materials.
- Datos en `ae_marks` (`AEAccount.marks()` y `AEAccount.setMark()`).
- **`ask-ai.js` excluye `.mk-note` y `.mk-actions`**: las notas del usuario nunca van en un prompt.

### 1.6 Focus y Timer como planetas

- Solo se cargan en **páginas de estudio**; ni la portada ni `account/` los cargan (condición en `theme.js`).
- Tienen la misma disposición y el mismo movimiento que en la vista de constelaciones de la portada: planetas con anillo de 64 px, Focus arriba a la derecha y Timer abajo a su izquierda, flotando cada 9 s con desfase.
- **Color:** Focus usa el color de la asignatura (`--accent`) y Timer un tono más oscuro del mismo.
- Estilos al final de `assets/css/focus-lab.css` y `assets/css/pomodoro.css`.
- `tools/tests/pomodoro_harness.html` se actualizó a esta disposición (antes exigía Timer 10 px encima de Focus).

### 1.7 Otros

- `AGENTS.md` documenta el sistema de cuentas y los planetas.
- `assets/data/updates.js` tiene una entrada de "What's new" por cada cambio visible.
- Ninguna clave nueva contiene "theme" (regla de `audit_portal`). Nada de esto se ejecuta en el modo de impresión de PDF, y los PDFs no han cambiado.

---

## 2. Claves de `localStorage` nuevas

| Clave | Contenido |
| :--- | :--- |
| `ae_account` | Cuentas del navegador: nombre, email, sal, hash y `prefs` (asignaturas, principal, fechas de examen, paleta, paleta automática, tamaño de texto, modo de la hoja de fórmulas, estilo del temporizador). |
| `ae_session` | Email de la sesión abierta. |
| `ae_account_last` | Último email que entró; se conserva al cerrar sesión. |
| `ae_recent`, `ae_study_log`, `ae_marks` | Ver 1.4 y 1.5. |

---

## 3. Estado de las comprobaciones

- `python tools/audit_portal.py`: 0 errores.
- `python tools/build_pdfs.py --check`: 640 PDFs al día.
- `python tools/build_nav.py --check`: OK.
- Tests que pasan: `test_focus_lab`, `test_pomodoro`, `test_updates`, `test_sidebar`, `test_problem_collapse`.
- **Fallos que ya existían antes de este trabajo** (comprobado contra el código anterior, no los introdujo esta rama):
  - `test_theme`: "the toggle button is hidden and inert".
  - `test_solution_close`: el escenario del navegador con el scroll del resumen.
  - `test_surface`: `test_the_close_bar_of_an_open_solution_was_audited_too`.
- `python tools/vault_lint.py` da 8 errores en `vault/`, también anteriores; esta rama no toca `vault/`.
- En este contenedor las capturas a doble resolución (`deviceScaleFactor: 2`) se cuelgan en cualquier página. A resolución normal funcionan.
- Playwright no puede hacer hover sobre los planetas porque se mueven: en scripts de captura hay que usar `{ force: true }`.

---

## 4. Lo que queda por hacer

En orden de prioridad aproximado:

1. ~~**Filtrar por las asignaturas del usuario.**~~ **Hecho** (commit "feat(portal): the portal arranged around your subjects"):
   - menú lateral con "Your subjects" primero y "Other subjects" después;
   - "What's new" filtrado mediante `window.AE_UPDATES_FILTER`, que deja `account.js` y lee `updates.js`; por eso `account.js` se carga ahora justo después de `pomodoro.js`;
   - portada: constelaciones propias delante y las demás atenuadas hasta pasar el ratón; en la vista clásica, tarjetas propias primero con la marca "Your subject".
   - Todo lo hacen `arrangeNav` y `arrangeHome` en `account.js`, sin tocar `sidebar.js` ni `constellations.js`.
2. **Backend en la nube para entrar desde cualquier dispositivo.**
   - Recomendado: Supabase (Auth + Postgres con Row Level Security). Habilitaría Google/Microsoft (ahora "Soon"), sincronizar `ae_account`, `ae_marks`, `ae_study_log` y los historiales de los simuladores, y recuperar la contraseña.
   - Mantener `localStorage` como caché, primero en local, para que la web siga funcionando sin conexión y sin cuenta.
   - `account.js` ya expone una API (`AEAccount.signUp`, `signIn`, `updatePrefs`…) pensada para cambiar el backend sin tocar las páginas.
   - Al hacerlo, añadir una política de privacidad real (RGPD).
3. **Títulos del inicio de sesión.** "Find your star." y "Claim your star." ya no encajan, porque se quitó la estrella marcada. Proponer al usuario textos ligados a la galaxia.
4. **Más gráficas o funciones en My study** que se mencionaron:
   - ~~objetivo semanal de horas~~ **hecho**: `prefs.weeklyGoal` (0 = sin objetivo, 1 a 40 h), deslizador en Settings → Study y anillo de progreso en "This week" de My study;
   - "practicar mis falladas" en el simulador;
   - puntos débiles por unidad o concepto. El banco de Materials tiene `concept_id` en cada pregunta, pero el historial del simulador solo guarda el id del ítem, así que hay que cruzarlo con `problems.js`.
5. **Idea propuesta y no hecha:** "tu cielo crece", una estrella o constelación personal que crece con los días estudiados o los temas terminados.
6. **Detalles menores:**
   - En móvil, los planetas Focus/Timer pueden tapar parte del contenido de abajo a la derecha. Se ofreció ocultarlos en páginas concretas.
   - Si se quiere que la portada vuelva a tener Focus/Timer, basta con cambiar la condición `studyTools` en `theme.js`; el usuario pidió quitarlos de la portada.
   - Las páginas `account/` no las revisa `audit_portal` (solo mira `index.html` y `subjects/`). Si se quiere, extender el auditor o añadir un test propio (por ejemplo `tools/tests/test_account.py`) que cubra el registro, el inicio de sesión, los favoritos y notas, y la exclusión en Ask AI.
7. **Fusionar con `main`** cuando el usuario lo apruebe. Antes, volver a pasar todas las comprobaciones de `AGENTS.md` y el `review-ultrareview` de cierre de hito.

---

## 5. Cómo probarlo a mano

```bash
python3 -m http.server 8765          # desde la raíz del repositorio
# abrir http://localhost:8765/account/signup.html y crear una cuenta
# visitar páginas de subjects/... (cuentan para "Continue" y el tiempo de estudio)
# en una página de problemas: estrella y nota junto a la flecha de cada tarjeta
# abrir http://localhost:8765/account/dashboard.html
```

Para ver el panel con datos de ejemplo hay que rellenar `ae_study_log` y los historiales de los simuladores desde la consola. Los datos de las capturas de esta sesión se inyectaron así; el portal no tenía historial real.

---

## 6. Historial de la rama

```
6f4f8e8 feat(portal): accounts with sign-up, onboarding and settings
f7bf8f8 style(portal): sign-in pages drawn as the subjects' constellation
197752e feat(portal): "your star" sign-in with observatory readout and exam countdown
93dd6bb style(portal): star-shaped sign-in box over a label-free sky      (revertido)
72c26bb Revert "style(portal): star-shaped sign-in box ..."
4383381 style(portal): sign-in sky as an observatory star chart
8079f95 feat(portal): planet study tools and a galaxy beside the sign-in
a7d4272 style(portal): barred spiral galaxy and a living sign-in sky
dfab5fb style(portal): remove the target reticle from the sign-in galaxy
18e0811 feat(portal): "My study" panel
ae06dab style(portal): richer My study charts; galaxy fits its hero
aabdf37 style(portal): harmonious subject palette for the My study charts
ff320fd feat(portal): favourites and notes on problem cards
745fe4c style(portal): Focus and Timer planets laid out like the constellation view
```
