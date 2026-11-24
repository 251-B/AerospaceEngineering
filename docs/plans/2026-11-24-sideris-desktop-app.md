# Sideris Desktop: plan de la app de escritorio con los 4 modelos

Estado: **solo plan**, nada construido. Fecha de la investigación: 2026-11-24.
Objetivo: instalar una app, abrirla y chatear con Sideris Lux, Aether, Orion y Titan en el propio ordenador, sin terminal, sin cuota y con la estética de Sideris. Debe sentirse como la app de Claude o Gemini.

## 1. Veredicto

- **Es viable y no hace falta ingeniería inversa.** Ollama y llama.cpp son abiertos. Varias apps ya funcionan así: Tauri más `llama-server` como proceso auxiliar ([guía](https://medium.com/@dillon.desilva/building-local-lm-desktop-applications-with-tauri-f54c628b13d9), [lloogie](https://codeberg.org/divinemadman/lloogie), [Liquid AI](https://docs.liquid.ai/deployment/on-device/llama-cpp/desktop)).
- **El diferencial real no es la potencia bruta**: es gratis, ilimitado, privado, funciona sin conexión y está anclado a vuestros apuntes del vault. La potencia general queda muy por debajo de Claude, Gemini o GPT (sección 3).
- **Tres riesgos mandan sobre el plan**: la lentitud de los modelos con razonamiento en CPU, la fiabilidad de las descargas de varios GB y el aviso de SmartScreen en Windows si el instalador no está firmado.

## 2. Qué existe ya y qué aprender de ello

| App | Qué hace bien | Qué evitar |
|---|---|---|
| [GPT4All](https://www.local-llm.net/compare/lm-studio-vs-jan-vs-gpt4all/) | La más fácil para no técnicos, trae un modelo inicial | Catálogo genérico, estética de herramienta |
| LM Studio | Navegador de modelos amplio | Cerrada; el alumno elige entre cientos de modelos y se pierde |
| Jan | Abierta, sin telemetría | El alumno debe [cambiar el backend a mano](https://www.jan.ai/docs/desktop/troubleshooting) (CPU, Vulkan, CUDA) cuando falla |
| [Ollama app](https://www.windowscentral.com/artificial-intelligence/ollamas-new-app-makes-using-local-ai-llms-on-your-windows-11-pc-a-breeze-no-more-need-to-chat-in-the-terminal) | Chat sin terminal, selector de modelo | Poca configuración desde la interfaz; sin personalidad |

Lecciones:
1. Pocos modelos, bien nombrados y con una recomendación clara. Vosotros tenéis 4.
2. **El backend (GPU o CPU) lo decide la app sola**, con respaldo automático. Nadie debería ver la palabra "Vulkan".
3. Los registros y los errores se explican con frases, no con trazas.

## 3. Potencia real frente a Claude, Gemini y GPT

Fuentes: [Artificial Analysis, Qwen3.5 small](https://artificialanalysis.ai/articles/qwen3-5-small-models), [ranking actual](https://artificialanalysis.ai/leaderboards/models), [paper de Phi-4-mini-reasoning](https://arxiv.org/pdf/2504.21233).

- Los Qwen3.5 pequeños son los más inteligentes de su tamaño (9B: 32, 4B: 27, 2B: 16 en el índice de marzo de 2026) y tienen licencia Apache 2.0, 262K de contexto y visión nativa.
- **Esa escala ya no es comparable.** El índice actual (v5.0.1) pone a Claude Fable 5.2 en 65, GPT-6.2 Astra en 62, Gemini 4 Neon en 61 y Claude Haiku 5.5 en 36. Qwen3.5-9B no tiene puntuación en la v5. Como referencia, un Qwen3.8 de 27B puntúa 20. Un 9B queda claramente por debajo de los modelos de pago, y Titan no compite con ellos en razonamiento general.
- **Conocimiento factual débil**: el 4B y el 9B tienen un 80-82 % de tasa de alucinación en AA-Omniscience y una precisión de 12.8-14.7 %. Sin apuntes delante, inventan con seguridad.
- **Phi-4-mini-reasoning (Orion)** saca 94.6 en MATH-500 y 52.0 en GPQA Diamond según Microsoft. Es muy bueno en matemática de procedimiento y flojo en conocimiento general.
- **Verbosidad**: los Qwen3.5 pequeños gastan entre 230 y 390 millones de tokens de salida para completar el índice, más que los modelos de frontera. En un portátil sin GPU eso significa esperas largas si el razonamiento está activado.

| | Sideris Desktop | Claude / Gemini / ChatGPT |
|---|---|---|
| Coste y cuota | Gratis, sin cuota | Cuota o suscripción |
| Privacidad | Todo queda en el equipo | Va a un servidor |
| Sin conexión | Sí, tras descargar | No |
| Razonamiento difícil | Limitado (9B como máximo) | Muy superior |
| Conocimiento general | Débil, alucina | Mucho mejor |
| Contexto práctico | 8K-32K según RAM | Hasta 1M |
| Velocidad | 6-18 tok/s en CPU (cifra comunitaria, sin verificar) | Rápida |
| Apuntes del curso | RAG sobre el vault, citas | Solo si el alumno los pega |
| Estilo pedagógico | Socrático, afinado por vosotros | Genérico |

**Mensaje honesto para la app y la web**: "Tutor privado y gratuito, basado en los apuntes del curso. Para preguntas fuera del temario o razonamientos muy largos, usa un asistente en la nube".

## 4. Arquitectura

```
Tauri 2 (Rust)  ──►  WebView2 con la UI de Sideris (HTML/CSS/JS del portal)
   │
   ├─ Gestor de modelos (Rust): catálogo, descarga, verificación, borrado
   ├─ Detector de hardware (Rust): RAM, disco, GPU, núcleos
   └─ Proceso auxiliar llama-server (OpenAI-compatible, localhost, puerto libre)
            ├─ build Vulkan  (GPU integrada o dedicada)
            └─ build CPU     (respaldo automático)
```

Decisiones:
1. **Reutilizar la UI web**: `assets/js/ai-chat.js`, `ai-rag.js`, `ai-engine.js`, `ai-models.js` y los tokens de `tokens.css`. Solo cambia el transporte de `ai-engine.js`, que pasa del Worker de Cloudflare a `http://127.0.0.1:<puerto>`. El mensaje del sistema por perfil (Lux breve, Aether tutor diario, Orion primeros principios, Titan examen completo) se mantiene igual.
2. **llama-server dentro del instalador**, ambas builds (unas decenas de MB). Hay proyectos que lo descargan en el primer arranque ([ejemplo](https://dev.to/santoshpremi/building-a-private-ai-desktop-app-with-rust-tauri-and-llamacpp-13ha)), pero descargarlo añade un fallo más.
3. **Backend automático**: arranca con Vulkan; si el modelo no carga en el tiempo previsto o falla, reinicia con CPU y lo recuerda. El alumno no toca nada. Las [gráficas integradas no siempre ganan a la CPU](https://www.amd.com/en/blogs/2024/accelerating-llama-cpp-performance-in-consumer-llm.html) y hay [informes de errores de memoria con Vulkan en algunos controladores](https://github.com/ggml-org/llama.cpp/issues/18946), por eso el respaldo es obligatorio.
4. **Parámetros de memoria**: contexto por defecto 8K, KV cache en `q8_0` con flash attention activa, y `--fit` en automático (viene por defecto; ver el [README del servidor](https://raw.githubusercontent.com/ggml-org/llama.cpp/HEAD/tools/server/README.md)). El contexto se sube solo si la RAM lo permite.
5. **Sin telemetría.** Historial y ajustes en local. Las claves de almacenamiento nuevas no contendrán "theme".
6. **Compilar fuera de OneDrive.** La carpeta `target/` de Rust pesa gigas y OneDrive ya corrompió Git en este repositorio (ver memoria del proyecto). Trabajar en `C:\Users\hecto\ae-work` o en una carpeta no sincronizada.
7. **Ubicación en el repositorio**: carpeta `desktop/` con un paso de construcción que copia los ficheros de `assets/` en vez de duplicarlos.

## 5. Descarga de modelos

Hay que tratar la descarga como una función principal, no como un detalle.

**Origen**
- Hugging Face como fuente única: es gratis y tiene [almacenamiento público generoso](https://huggingface.co/docs/hub/storage-limits). GitHub Releases limita cada archivo a 2 GB (dato conocido, a verificar), así que no vale para Titan.
- Un fichero `models.json` en GitHub Pages lista, para cada modelo: URL, tamaño, SHA-256, RAM mínima y versión. **Añadir o actualizar un modelo no exige una versión nueva de la app.**

**Gestor de descargas (Rust)**
- Peticiones con `Range` y archivo `.part`: se reanuda tras un corte o un cierre de la app. El soporte de `Accept-Ranges` es lo que permite reanudar, igual que [hace llama.cpp](https://www.docker.com/blog/llama-cpp-resumable-gguf-downloads/).
- Verificación SHA-256 al terminar; si falla, se borra y se reintenta una vez con un mensaje claro.
- Comprobación de espacio libre antes de empezar, con el tamaño más 10 %.
- Reintentos con espera creciente. Hay [quejas de limitación en ISP españoles y latinoamericanos](https://discuss.huggingface.co/t/severe-throttling-instability-downloading-gguf-via-telmex-isp-in-northwest-mexico/177677) y de [conexiones inestables que dejan descargas a medias](https://discuss.huggingface.co/t/flaky-connections-like-starlink-crashes-hf-xet-large-downloads/178759), así que la descarga debe aguantar WiFi de campus.
- Pausar y reanudar con un botón; la barra muestra porcentaje, velocidad y tiempo restante.
- Alternativa manual: "Ya tengo el archivo" para importar un `.gguf` copiado en un USB. Útil en el aula.
- Carpeta de modelos elegible (por defecto `%APPDATA%\Sideris\models`), por si el disco C: va justo.
- Borrar un modelo libera el espacio desde la app.

**Descarga automática del primer modelo**
- Durante el onboarding se descarga solo el modelo recomendado (casi siempre Lux, 1.3 GB). Se puede chatear en cuanto termina.

## 6. Experiencia de usuario: que se sienta como Claude o Gemini

Patrones comunes a los asistentes actuales ([análisis](https://www.setproduct.com/blog/ai-chat-interface-ui-design), [comparativa](https://eug.github.io/posts/dissecting-the-assistant-user-interface.html)): campo de texto como protagonista, respuesta en streaming token a token, barra lateral con historial por fecha, selector de modelo visible y chips de sugerencia en el estado vacío.

**Pantalla principal**
- Barra lateral plegable con conversaciones agrupadas por Hoy, Ayer y Anteriores, búsqueda y botón de nuevo chat.
- Estado vacío con un saludo corto y 4 sugerencias del temario ("Explícame la ecuación de Bernoulli", "Revisa mi planteamiento de este problema").
- Compositor centrado y ancho fijo de lectura, con selector de modelo dentro del compositor y botón de enviar que se convierte en "Detener" mientras genera.
- Respuesta con Markdown seguro, KaTeX en vivo, bloque de razonamiento plegable (`<think>`), y botones de copiar, regenerar y "citar apuntes usados".
- Interruptor "Pensar más" por conversación (activa el razonamiento). Por defecto apagado en Lux y Aether para que no haya esperas largas.
- Paletas de lectura de Sideris (las 6) con el selector de siempre; fondo plano de superficie de estudio, tipografías Newsreader, Abril Fatface y JetBrains Mono.

**Selector de modelo (nombres por resultado, no por parámetros)**

| Modelo | Etiqueta en la interfaz | Estado posible |
|---|---|---|
| Lux | "Rápido y breve" | Listo, Descargar, Descargando 42 % |
| Aether | "El tutor de cada día" (recomendado) | igual |
| Orion | "Derivaciones paso a paso" | igual, con aviso "tarda más" |
| Titan | "Respuestas de examen completas" | igual, o bloqueado con el motivo |

**Onboarding en 3 pasos como máximo**
1. Bienvenida y lectura del equipo: "Tu equipo tiene 16 GB de RAM y gráfica integrada. Te recomendamos Aether".
2. Descarga del recomendado con barra de progreso, mientras se muestra un recorrido breve de la interfaz.
3. Primer chat con una sugerencia ya escrita.

**Criterios de "100 % intuitivo"** (se prueban con 5 alumnos nuevos antes de publicar):
- Cero términos técnicos visibles por defecto (nada de GGUF, Vulkan, cuantización, tokens).
- De la descarga del instalador a la primera respuesta en menos de 10 minutos con una conexión de 100 Mbps.
- Ningún alumno abre PowerShell ni edita un archivo.
- Todo error ofrece una acción: "Reintentar", "Probar con modo compatible", "Elegir un modelo más ligero".
- Ajustes avanzados (contexto, carpeta, backend) escondidos en "Avanzado".

## 7. Limitaciones y avisos (textos previstos)

| Situación | Cuándo se muestra | Texto en la app |
|---|---|---|
| Titan con poca RAM | RAM menor de 12 GB al elegirlo | "Titan necesita unos 16 GB de RAM. En este equipo puede ir muy lento o cerrarse. Prueba con Aether." (bloqueado con opción de "Probar igualmente" en Avanzado) |
| Sin GPU dedicada | Al detectar solo iGPU o CPU | "Sin tarjeta gráfica dedicada las respuestas serán más lentas, sobre todo con Orion y Titan." |
| Respuesta con razonamiento | Al activar "Pensar más" | "Pensar más da mejores resultados en problemas difíciles, pero puede tardar varios minutos en tu equipo." |
| Datos inventados | Siempre visible en la barra del compositor | "Sideris puede equivocarse. Comprueba los datos importantes con tus apuntes." |
| Fuera del temario | Cuando el RAG no encuentra apuntes | "No he encontrado esto en los apuntes del curso. Esta respuesta puede no ser fiable." |
| Poco espacio en disco | Antes de descargar | "Faltan X GB libres. Libera espacio o elige otra carpeta." |
| Descarga cortada | Fallo de red | "Se cortó la descarga. Se reanudará sola cuando vuelva la conexión." |
| Batería | Equipo en batería y modelo grande | "Con batería, los modelos grandes la gastan rápido." |
| Primera carga lenta | Al abrir un modelo | "Cargando el modelo (puede tardar hasta un minuto la primera vez)." |
| Windows avisa del instalador | Si no hay firma (sección 8) | Página de descarga con capturas: "Más información" y "Ejecutar de todas formas". |

Límites que no se pueden ocultar: contexto práctico de 8K-32K, velocidad dependiente del equipo, ausencia de internet y de herramientas externas, y calidad inferior a los modelos de pago en razonamiento general y conocimiento.

## 8. Lite y Full

- **Un solo código**, con un parámetro de compilación que cambia la lista de modelos y el catálogo.
- **Lite**: Lux, Aether, Orion. Descargas de unos 6.3 GB en total, recomendada con 8 GB de RAM.
- **Full**: añade Titan (unos 5.5 GB). Recomendada con 16 GB de RAM y mejor con GPU.
- Alternativa más simple (recomendada): un solo instalador con Titan como descarga opcional marcada con el aviso de la sección 7. Sigue pudiendo publicarse "Lite" y "Full" como dos botones que solo difieren en qué modelo se ofrece de entrada.
- Tamaños son estimaciones para Q4 y no están medidos con vuestros modelos entrenados.

## 9. Distribución, firma y actualizaciones

- **Instalador NSIS** instalable por usuario (sin permisos de administrador), distribuido por GitHub Releases.
- **WebView2**: Windows 10 reciente y Windows 11 ya lo incluyen. Para equipos antiguos, el instalador usa el arranque que lo descarga. Las alternativas offline añaden unos 127 MB ([doc de Tauri](https://v2.tauri.app/distribute/windows-installer/), [Microsoft](https://learn.microsoft.com/microsoft-edge/webview2/concepts/distribution)).
- **Firma de código**: sin firma, [Windows SmartScreen bloquea o avisa](https://v2.tauri.app/distribute/sign/windows/) y Defender puede dar falsos positivos con apps nuevas. Opciones:
  1. Sin firma: coste cero. Se explica el aviso en la página de descarga y se envía el instalador a Microsoft como falso positivo. Es lo realista para el estreno.
  2. Certificado OV o servicio de firma: coste recurrente y reputación que tarda en construirse. Los precios actuales no están verificados; se decide con la cifra real.
- **Actualizaciones de la app** con el [updater de Tauri](https://v2.tauri.app/plugin/updater/), con su clave propia, que no se debe perder ni rotar (los usuarios existentes quedarían sin actualizaciones automáticas).
- **Actualizaciones de modelos** por `models.json`, sin nueva versión de la app.
- Primera versión solo Windows. macOS (Metal funciona muy bien en Apple Silicon) queda para una segunda fase, con la notarización de Apple como coste anual.

## 10. Preparar los modelos entrenados

1. Fusionar el LoRA en la base (Qwen3.5-2B, 4B, 9B y Phi-4-mini-reasoning).
2. Convertir a GGUF F16 con `convert_hf_to_gguf.py` sobre una carpeta de modelo solo texto, y cuantizar con `llama-quantize` a Q4_K_M (probar también Q5_K_M para Lux, que es pequeño).
3. Riesgo conocido: tras ajustar Qwen3.5-4B hay [errores de "BPE pre-tokenizer was not recognized"](https://discuss.huggingface.co/t/the-bpe-pre-tokenizer-was-not-recognized/175714) al convertir. Probar la conversión con un modelo ya entrenado antes de comprometer el calendario.
4. **Puerta de calidad**: pasar `tools/ai_training/out/eval_holdout.jsonl` por la versión original y la cuantizada, y comparar con las respuestas del Worker. Si la cuantización degrada el estilo socrático o los pasos de cálculo, subir a Q5 o Q6 en ese modelo.
5. Medir `llama-bench` en 3 equipos de referencia: portátil de 8 GB con iGPU, portátil de 16 GB con iGPU AMD o Intel, y uno con GPU dedicada. Con esos números se fijan los umbrales de RAM de la sección 7.
6. Publicar en Hugging Face con tarjeta de modelo y licencia (Apache 2.0 para Qwen, MIT para Phi). Pendiente comprobar la licencia de cada base en su ficha oficial.

## 11. Fases y criterios de salida

| Fase | Contenido | Se da por terminada cuando |
|---|---|---|
| 0. Modelos | Exportar GGUF, puerta de calidad, benchmarks en 3 equipos | Hay 4 GGUF aprobados y una tabla de tok/s por equipo |
| 1. Esqueleto | Tauri más llama-server más chat reutilizado, solo Lux | Un chat completo funciona sin internet en un equipo limpio |
| 2. Modelos y descarga | Catálogo `models.json`, gestor con reanudación, detección de hardware, tarjetas de modelo | Se corta el WiFi a mitad de Titan y la descarga se reanuda y verifica |
| 3. Experiencia | Onboarding, barra lateral e historial, KaTeX, razonamiento plegable, RAG con citas, paletas, avisos | Prueba con 5 alumnos: todos llegan a su primera respuesta sin ayuda |
| 4. Empaquetado | Instalador NSIS, Lite y Full, updater, página de descarga con capturas | Instalación limpia en Windows 10 y 11, sin administrador |
| 5. Beta cerrada | 10 alumnos durante 2 semanas, formulario de comentarios | Sin errores bloqueantes abiertos |

Estimación orientativa de esfuerzo: unas 4 a 6 semanas de trabajo si los pesos entrenados ya existen. No es un compromiso: depende de la fase 0.

## 12. Riesgos

| Riesgo | Probabilidad | Mitigación |
|---|---|---|
| Esperas largas con razonamiento en CPU | Alta | Razonamiento apagado por defecto, aviso, tiempo estimado en pantalla |
| Descarga que falla o va lenta | Alta | Reanudación, verificación, importación manual, mensajes claros |
| SmartScreen o Defender frenan el instalador | Alta sin firma | Guía con capturas, envío a Microsoft, valorar firma más adelante |
| Vulkan falla en algún controlador | Media | Respaldo automático a CPU |
| Cuantización degrada el estilo socrático | Media | Puerta de calidad con el conjunto de evaluación |
| Expectativa de "como Claude" y decepción | Alta | Mensaje honesto en la app y en la web (sección 3) |
| Alucinaciones sin apuntes | Alta | RAG con citas, aviso cuando no hay apuntes, aviso permanente |
| Corrupción de Git por OneDrive | Media | Compilar fuera de OneDrive |

## 13. Pendiente de verificar antes de empezar

- Existencia y estado de los pesos entrenados de los 4 modelos.
- Licencia exacta de cada modelo base en su ficha oficial.
- Cifras de tok/s en equipos reales de estudiantes (las de este documento son comunitarias y de hardware sin detallar).
- Comportamiento de Vulkan con las iGPU de Intel y AMD más comunes entre los alumnos.
- Coste vigente de la firma de código y requisitos de elegibilidad.
- Si el límite de 2 GB por archivo de GitHub Releases sigue vigente.
- Tamaño real de la KV cache de Qwen3.5 con contexto largo (la arquitectura es híbrida, pero no lo he comprobado).
- Un issue de llama.cpp indica que `--fit-target` falla en Windows con valores altos; evitar ese parámetro hasta confirmarlo.

## 14. Revisión de modelos base (2026-11-24)

Fuentes: [pequeños 4B-40B](https://artificialanalysis.ai/models/open-source/small), [diminutos hasta 4B](https://artificialanalysis.ai/models/open-source/tiny), [K2 Horizon 7B](https://artificialanalysis.ai/models/k2-horizon-7b), [GGUF de K2 Horizon](https://huggingface.co/IFM/K2-Horizon-7B-GGUF), [Gemma 4 E4B](https://huggingface.co/ggml-org/gemma-4-e4b-it-GGUF), [MiniCPM5-2B](https://huggingface.co/OpenBMB/MiniCPM5-2B).

Hay modelos mejores que algunas de las bases actuales, pero el ranking mide trabajo agéntico y de conocimiento, no tutoría socrática ni derivaciones en español. **No se sustituye nada hasta una prueba propia con `eval_holdout.jsonl`.**

Progress Index v1 de Artificial Analysis (más alto es mejor; no es la escala de marzo):

| Hueco | Base actual | Candidatos mejor puntuados |
|---|---|---|
| Lux (2B) | Qwen3.5-2B: 177 | K2 Horizon 3.7B: 242, MiniCPM5-2B: 221, LFM3-1.7B: 216 |
| Aether (4B) | Qwen3.5-4B: sin dato en la lista (queda por debajo de 257) | Gemma 4 E4B (Apache 2.0, GGUF oficial en llama.cpp), K2 Horizon 3.7B |
| Orion (3.8B) | Phi-4-mini-reasoning (abril de 2025, ya sin puntuación actual) | K2 Horizon 3.7B o 7B con razonamiento |
| Titan (9B) | Qwen3.5-9B: sin dato (queda por debajo de 257) | K2 Horizon 7B: 263, Apache 2.0 |
| Titan en equipos de 32 GB | n/a | Inkling 2 Mini (26B, 5.4B activos): 306; Qwen3.6 35B A3B: 261 |

Riesgos de cada cambio:
- **K2 Horizon** (Institute of Foundation Models): usa una atención nueva que **todavía no está en llama.cpp estándar**. Habría que incluir en el instalador la rama de su bifurcación, y que `peft`, `trl` o Unsloth la soporten para reentrenar es una incógnita. Es de solo texto y muy verboso. Su calidad en español no está comprobada.
- **MiniCPM5-2B**: una fuente dice Apache 2.0 y otra muestra CC BY-NC-SA. Hay que leer la licencia oficial antes de nada, y más si la app se va a cobrar.
- **LFM3-1.7B** (Liquid AI): licencia sin comprobar. Sus licencias anteriores tenían límites comerciales.
- **Gemma 4 E4B**: es el cambio de menor riesgo técnico por su soporte oficial; la licencia Apache 2.0 sale en medios secundarios y se confirma en la ficha de Google. Calidad en español sin comprobar.
- **Modelos MoE grandes** (Inkling 2 Mini, Qwen3.6 35B A3B): corren como un modelo de 5B o 3B activos, pero necesitan memoria de un modelo de 26B a 35B (unos 15 a 20 GB en Q4). Solo valen como "Titan Max" para equipos de 32 GB.
- **Cualquier cambio** obliga a reentrenar los LoRA, a volver a pasar la cuantización y a repetir las pruebas de velocidad.

Torneo previsto en la fase 0, uno por hueco:
1. Misma batería: `eval_holdout.jsonl` en español e inglés más 20 problemas del vault con solución conocida.
2. Medir calidad socrática, exactitud de cálculo, longitud de la respuesta y tokens por segundo en los 3 equipos de referencia.
3. Verificar licencia oficial, soporte en llama.cpp estándar y herramientas de entrenamiento.
4. Cambiar la base solo si gana con claridad. Si empata, se queda la actual porque ya está entrenada.

## 15. Fase 6 (futuro): planes de la app de IA

La web de Sideris sigue siendo gratuita. Solo la app de escritorio con IA tendría planes, por ejemplo Essential (Lux, Aether y Orion con mensajes diarios) y Pro (los cuatro modelos sin tope diario, Titan y sincronización). La interfaz no usa las palabras "gratis" ni "ilimitado".

| Mecanismo | Dureza | Cómo funciona |
|---|---|---|
| Titan solo por descarga con permiso | Alta | El archivo no es público; un Worker da un enlace firmado de corta duración a cuentas Pro |
| Licencia firmada | Media | Token firmado por el servidor, verificado sin conexión con clave pública y renovado cada pocos días |
| Funciones en la nube | Alta | Sincronización del historial y copia de seguridad solo para cuentas Pro |
| Contador diario de mensajes | Baja | Se guarda en el equipo y se puede resetear; es un límite suave |

Para dejarlo preparado en las fases 1 a 3: función única `puedeUsar(modelo)` que hoy devuelve sí, campo `tier` en `models.json` con soporte de enlaces firmados, y pantalla de cuenta vacía en Ajustes.

Riesgos antes de cobrar:
- Los apuntes del curso (RAG y vault) vienen de material oficial de UC3M y de sus profesores. Cobrar por una app que los incluye es una decisión legal distinta de la web gratuita. Se vende el modelo, la app y las funciones, y los apuntes quedan fuera del plan de pago o con permiso escrito.
- Las licencias de los modelos base deben permitir uso comercial. Revisar cada una antes de elegir la base definitiva (sección 14).
- Alta de autónomo o sociedad, IVA europeo y elección del proveedor de pago. Precios y condiciones actuales sin verificar.
- Alguien que pague podrá compartir los archivos; no existe protección total en una app local.
