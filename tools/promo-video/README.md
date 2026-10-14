# Promo video (`promo-aerospace.mp4`)

Fuente reproducible del vídeo promocional del portal (1920×1080, 60 fps, ~96 s) que está en la raíz del repositorio. No forma parte del portal publicado ni de los gates de `tools/`.

## 1. Grabación (`recorder/`)

Playwright captura cada plano fotograma a fotograma en tres viewports: escritorio 1920×1080, tablet 820×1180 y móvil 390×844. Un reloj falso avanza exactamente 1/60 s por fotograma (rAF, timers, `Date`) y la velocidad de las transiciones CSS se ajusta por CDP, así que el resultado es 60 fps reales aunque cada captura tarde más. El cursor y los toques se inyectan en la página. KaTeX se sirve desde `node_modules` interceptando las peticiones al CDN.

```bash
cd tools/promo-video/recorder && npm install
npm run serve &                    # sirve la raíz del repo en http://localhost:8765
node record.js desktop             # o: tablet, mobile, o un plano concreto: node record.js desktop askai
```

Los clips quedan en `recorder/clips/<dispositivo>-<plano>.mp4` (H.264, CRF 15).

## 2. Montaje (`remotion/`)

Composición en Remotion: intro, una escena por función (hub, búsqueda, teoría, problemas, Ask AI, paletas, Focus Lab, temporizador, PDFs/exámenes), los tres dispositivos a la vez y cierre. Los mockups (monitor, tablet, móvil), los zooms por fotogramas clave, las transiciones y la banda sonora sintetizada (`gen_audio.py`, sincronizada con los cortes de `src/scenes.json`) son propios. Las fuentes (OFL) están en `public/fonts/`.

```bash
cd tools/promo-video/remotion && npm install
npm run prepare-assets             # enlaza los clips, cuenta sus fotogramas, genera soundtrack.wav
npm run render                     # -> out/promo-aerospace.mp4
```

`npm run render` (`render.sh`) renderiza una secuencia de imágenes en lugar del MP4 directo. Chrome sin GPU a veces captura un fotograma antes de pintar todas las teselas de las pantallas ampliadas, y un dispositivo o un trozo desaparece durante un fotograma (parpadeo). `check_frames.py` marca los fotogramas sospechosos (un bloque que difiere de sus dos vecinos mientras ellos coinciden) y `settle.py` los vuelve a renderizar con `repair.mjs` hasta que dos renders seguidos coinciden: el movimiento real se reproduce igual y el defecto no. Después se codifica el MP4 con la banda sonora.

Con `REMOTION_BROWSER=/ruta/a/headless_shell` se usa un Chrome local en lugar de descargar uno.
