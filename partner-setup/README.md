# Partner setup: Claude Code + Antigravity, igual que en el PC del autor del repo

Esta carpeta deja tu ordenador con **la misma configuración de IA** que usamos en este repo: Claude Code y Antigravity conectados por un puente, las mismas skills y plugins, el router que activa cada skill sola según lo que escribas, el reparto de modelos por tarea y el ciclo de aprendizaje (task-observer). No tienes que configurar nada a mano: **tu Claude lo hace leyendo `AI_SETUP.md`**, y te pregunta antes de cada paso que descarga o cambia algo.

## Qué necesitas antes de empezar

| Qué | Para qué | Cómo comprobarlo |
| :--- | :--- | :--- |
| Windows con este repo clonado (`git pull` hecho) | Todo vive aquí | `git status` en la carpeta del repo |
| **Claude Code** con tu propia suscripción (Pro o Max) | El agente principal | `claude --version` |
| **Antigravity** (app) y su terminal **`agy`**, con una cuenta personal de Google con **Google AI Pro** | El segundo agente (modelos Gemini 4 Neon e Hydrogen) | `agy --version` y `agy models` |
| **Python 3.10 o superior** | Instalador, router y puente | `python --version` |
| **Node.js 22 o superior** (incluye `npx`) | Skills de diseño y el MCP de Playwright | `node --version` |
| **Git** | Plugins y skills que se descargan de GitHub | `git --version` |

Si te falta algo, tu Claude te lo dirá en el primer paso y te explicará cómo instalarlo.

## Cómo se hace (3 pasos)

1. **Abre Claude Code en la carpeta del repo** (la app de escritorio o `claude` en una terminal) y pega esto:

   ```text
   Lee partner-setup/AI_SETUP.md y sigue sus instrucciones paso a paso para dejar mi ordenador con la misma configuración. Pregúntame antes de instalar o cambiar cualquier cosa.
   ```

2. **Cuando tu Claude te lo pida, cierra Claude Code y vuelve a abrirlo** en la carpeta del repo. Los hooks, plugins y MCP nuevos solo se cargan al empezar una sesión. En la sesión nueva verás la nota "Learning loop (skill router)" al principio, y tu Claude probará el puente con Antigravity.

3. **Después abre (o reinicia) Antigravity** en la carpeta del repo y pega el prompt de `partner-setup/ANTIGRAVITY_CHECK.md`. Antigravity comprueba su lado y el puente en sentido contrario. Pégale a tu Claude la tabla que te devuelva.

## Qué se instala y qué no

**Se instala (igual que en el PC del autor del repo):**

- **Claude Code:** plugins `superpowers`, `claude-mem`, `ponytail`, `figma` y `claude-code-setup`; MCP `playwright` y `antigravity-bridge`; el router de skills (`~/.claude/hooks/skill_router.py` y sus 42 reglas globales, más las 9 del repo); las skills `task-observer` y `dual-agent-team`; las 21 skills de diseño y animación (descargadas de sus autores: `emilkowalski/skills`, `pbakaus/impeccable`, `Leonxlnx/taste-skill`); y las instrucciones globales (`~/.claude/CLAUDE.md`, añadidas al final de las tuyas, sin borrar nada).
- **Antigravity:** los plugins `agent-bridge` (el puente y el router), `skill-evolution` (task-observer y skill-creator), `aerospace-study-workflows`, `superpowers`, `claude-mem` y `ui-design-craft`, más `chrome-devtools-plugin` del marketplace oficial. También cambia **cómo trabaja Antigravity**: en `~/.gemini/config/config.json` activa la ejecución automática de comandos (`autoExecutionPolicy: CASCADE_COMMANDS_AUTO_EXECUTION_EAGER`), desactiva el sandbox de terminal de la app (`enableTerminalSandbox: false`) y le deja leer archivos fuera del proyecto (`nonWorkspaceFileAccessPolicy: AGENT_SETTING_POLICY_ALLOW`); y en `~/.gemini/antigravity-cli/settings.json` da permiso a su terminal sobre la carpeta del repo y `~/.agent-bridge`, a los MCP del puente y de claude-mem y a comandos inofensivos (git, python, node, listar archivos), y le prohíbe borrados recursivos, `git push --force` y `git reset --hard`. Es lo que hace falta para que el puente funcione sin pantalla; tu Claude te lo explicará antes de aplicarlo.
- **El puente** (`~/.agent-bridge/`): la configuración de modelos por rol y el protocolo de equipo (`TEAM_PROTOCOL.md`), y la carpeta del log de task-observer.

**No se instala (y por qué):**

- **Lo que va con la cuenta de claude.ai** (skills integradas como docx/pdf/pptx/xlsx, `adaptive-agent`, `headroom`, conectores de Gmail o Drive): llega solo con tu propia cuenta, no se puede copiar.
- **Lo personal del autor del repo:** su memoria (`claude-mem`), sus observaciones, su historial y herramientas que no usa este repo (Cloudflare, Supabase, Mobbin, NotebookLM, ingeniería inversa).
- **Las skills de Anthropic que Antigravity tenía copiadas:** su licencia prohíbe redistribuirlas en un repo público.

## Seguridad

- Antes de cambiar cualquier archivo, el instalador lo copia a `~/.ae-setup-backup/<fecha-hora>/`. Para deshacer, basta con volver a copiar esa carpeta.
- No se sube ni se envía nada tuyo a ningún sitio. Lo único que se descarga son los plugins y skills públicos de la lista.
- Los hooks ejecutan código en tu PC (el router de skills y el puente). Están en `payload/` y puedes leerlos antes.

## Para el autor del repo: mantener esta carpeta al día

Cuando cambies tu configuración (una regla del router, una skill, el protocolo o un plugin de Antigravity), ejecuta en tu PC:

```bash
python partner-setup/export.py
```

Eso regenera `payload/` desde tu configuración real, cambia tus rutas por marcadores y falla si se cuela algo personal. `python partner-setup/export.py --check` avisa si la carpeta se ha quedado vieja. Si añades un plugin o una skill, añádelo antes a `manifest.json`.

## Contenido de la carpeta

| Archivo | Qué es |
| :--- | :--- |
| `README.md` | Esta guía |
| `AI_SETUP.md` | El manual que sigue el Claude de tu compañero |
| `ANTIGRAVITY_CHECK.md` | El prompt para el Antigravity de tu compañero |
| `manifest.json` | La lista completa de lo que se instala |
| `install.py` | El instalador (`plan`, `apply`, `check`) |
| `export.py` | Regenera `payload/` desde el PC del autor del repo |
| `payload/` | Los archivos de configuración, con marcadores en lugar de rutas |
| `THIRD_PARTY.md` | Licencias del material de terceros incluido |
