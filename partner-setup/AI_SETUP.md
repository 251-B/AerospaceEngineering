# AI_SETUP: manual para el Claude Code del compañero

Eres Claude Code, en el ordenador del compañero del autor del repo. Tu objetivo es dejar este ordenador con **la misma configuración de Claude Code y Antigravity** que tiene el autor del repo, de modo que todo funcione igual: plugins, MCP, skills, router de skills, puente con Antigravity, reparto de modelos y task-observer. Todo lo que hay que instalar está descrito en `partner-setup/manifest.json` y lo hace `partner-setup/install.py`. Tú diriges el proceso, explicas cada paso en lenguaje sencillo y verificas el resultado.

## Reglas para ti durante este proceso

1. **Pregunta antes de descargar o cambiar nada** fuera del repo (instalar programas, plugins, paquetes de Python, escribir en `~/.claude`, `~/.gemini` o `~/.agent-bridge`). Una sola aprobación del usuario puede cubrir un paso entero si le has dicho qué incluye.
2. **No toques el repo.** Este proceso solo cambia la carpeta de usuario. No hagas commit ni push aunque `CLAUDE.md` diga que cada tarea termina con uno: aquí no hay cambios en el repo.
3. **Nunca escribas contraseñas, tokens ni claves.** Los inicios de sesión (Claude, Google en `agy`, Figma) los hace el usuario.
4. **Lee antes de ejecutar.** Los hooks y servidores que se instalan están en `partner-setup/payload/`. Si el usuario quiere saber qué hace algo, ábrelo y explícaselo.
5. **Si algo falla, busca la causa** (mensaje de error, ruta, versión) en vez de repetir el comando. Si no lo puedes arreglar, dilo con el error exacto.
6. El repo tiene sus propias reglas (`CLAUDE.md`, `AGENTS.md`). Para este proceso manda este manual; después de reiniciar, manda `CLAUDE.md` como siempre.

## Paso 1. Comprobar requisitos

Ejecuta y resume en una tabla (qué hay, qué versión, qué falta):

```bash
git --version
python --version
node --version
claude --version
agy --version
```

Además, comprueba con Python que `pip` existe (`python -m pip --version`) y si el paquete `mcp` está instalado (`python -c "import mcp"`).

Si falta algo, explícale al usuario cómo instalarlo y espera a que te diga que está hecho:

| Falta | Cómo se instala (Windows) |
| :--- | :--- |
| Git | `winget install --id Git.Git -e` |
| Python 3.10+ | `winget install --id Python.Python.3.12 -e` (marcar "Add to PATH") |
| Node.js 22+ | `winget install --id OpenJS.NodeJS.LTS -e` |
| Antigravity (app) | Desde https://antigravity.google (cuenta personal de Google con Google AI Pro) |
| `agy` (terminal de Antigravity) | En PowerShell: `irm https://antigravity.google/cli/install.ps1 \| iex`, luego abrir una terminal nueva. Si el comando no funciona, la web de Antigravity explica la instalación del CLI |
| Inicio de sesión en `agy` | El usuario ejecuta `agy` una vez en una terminal, entra con su cuenta de Google en el navegador (la misma cuenta con Google AI Pro que usa en la app) y sale de `agy` con `/exit` o Ctrl+C |

Cuando `agy` funcione, ejecuta `agy models` y guarda la lista: confirma que la sesión está iniciada y la usarás en el paso 5. Si en vez de modelos dice que falta autenticación, el usuario repite el inicio de sesión.

## Paso 2. Ver el plan

```bash
python partner-setup/install.py plan
```

No cambia nada: lista cada archivo que escribirá, cada carpeta que instalará y cada comando que ejecutará. Resúmeselo al usuario en pocas líneas (qué se instala en Claude, qué en Antigravity, qué se descarga de internet) y pídele permiso para seguir. Menciona expresamente que cambia cómo trabaja Antigravity:

- **`~/.gemini/config/config.json`:** ejecución automática de comandos (`autoExecutionPolicy: CASCADE_COMMANDS_AUTO_EXECUTION_EAGER`), sin sandbox de terminal en la app (`enableTerminalSandbox: false`) y lectura fuera del proyecto (`nonWorkspaceFileAccessPolicy: AGENT_SETTING_POLICY_ALLOW`).
- **`~/.gemini/antigravity-cli/settings.json`:** permisos de la terminal `agy` sobre la carpeta del repo y `~/.agent-bridge`, los MCP del puente y de claude-mem y comandos inofensivos, y prohibición de borrados recursivos, `git push --force` y `git reset --hard`. Las rutas llevan letra de unidad (`C:/...`); el instalador quita las que no la llevan, porque rompen el sandbox de `agy` en Windows.

## Paso 3. Instalar

```bash
python partner-setup/install.py apply --install-deps
```

- `--install-deps` instala el paquete de Python `mcp` (lo necesita el puente). Quítalo si el usuario no quiere que lo instales tú.
- Añade marketplaces y plugins de Claude con `claude plugin`, registra los MCP con `claude mcp add`, descarga las skills de diseño con `npx skills add` y copia los plugins de Antigravity a `~/.gemini/config/plugins/`.
- Antes de cambiar un archivo lo copia a `~/.ae-setup-backup/<fecha-hora>/`. Dile al usuario dónde quedó esa copia.
- Si una línea empieza por `!`, es un aviso: léelo, corrige la causa (por ejemplo, un plugin de Claude que no se instaló hace que falten skills en Antigravity) y vuelve a ejecutar `apply`. El instalador se puede repetir sin romper nada.

## Paso 4. Verificar

```bash
python partner-setup/install.py check
```

Cada línea dice `OK` o `FAIL`. Todo debe salir `OK`. Si algo falla:

| Línea que falla | Causa probable | Qué hacer |
| :--- | :--- | :--- |
| `Claude plugin ...` | El marketplace no se añadió o la instalación pidió confirmación | `claude plugin marketplace list`, luego `claude plugin install <id> --scope user` |
| `skills from ...` | `npx` sin red o el nombre de skill cambió en su repo | `npx -y skills@1.9.0 add <repo> -l` para ver los nombres; si cambió, díselo al usuario |
| `Antigravity plugin superpowers / claude-mem` | Falta el plugin de Claude del que se copian sus skills | Instala ese plugin de Claude y repite `apply` |
| `Python package mcp` | No se instaló | `python -m pip install --user mcp` |
| `Antigravity plugin chrome-devtools-plugin` | `agy plugin install` falló o `agy` no estaba en el PATH | `agy plugin install chrome-devtools-plugin@antigravity-plugins-official` en una terminal nueva |
| `claude-mem MCP server for Antigravity` | El plugin `claude-mem` de Claude no está instalado (Antigravity usa su servidor) | `claude plugin install claude-mem@thedotmack --scope user`, reinicia Claude Code una vez para que arranque su servicio |
| `Antigravity CLI permissions` / `trusted workspace` | `settings.json` de `agy` sin las reglas o con rutas sin letra de unidad | Repite `apply`; el instalador las añade y quita las rutas sin unidad |
| `... invocable` | Una skill de diseño se reinstaló con `disable-model-invocation: true` | Repite `apply` |
| `command node` | Falta Node.js | Instálalo (paso 1); lo usan las skills de diseño, Playwright y el MCP de claude-mem |
| `router selftest` | Python distinto o regla rota | Ejecuta `python ~/.claude/hooks/skill_router.py --selftest` y lee el error |
| `Claude MCP ...` | `claude mcp add` falló | `claude mcp list` y repite el `add` que muestra `plan` |

## Paso 5. Ajustar los modelos a su cuenta

`~/.agent-bridge/config.json` reparte el trabajo por roles (lo explica `~/.agent-bridge/TEAM_PROTOCOL.md`): en Antigravity, Hydrogen medium para tareas rápidas, Hydrogen high para implementar y Neon high para revisar y planificar; en Claude, Haiku medium, Sonnet medium y Opus high. Compara esos nombres con la lista de `agy models` del paso 1:

- Si están todos, no cambies nada.
- Si falta alguno (cuenta con otro plan), propón al usuario el modelo más parecido de su lista para ese rol, explica por qué y cámbialo solo si te dice que sí.

## Paso 6. Reiniciar y probar el puente

Pide al usuario que **cierre Claude Code y lo vuelva a abrir en la carpeta del repo**: los hooks, plugins y MCP nuevos solo se cargan al empezar una sesión. En la sesión nueva:

1. Al empezar debe aparecer la nota "Learning loop (skill router)". Invoca `task-observer` como dice esa nota y comprueba que su log está en `~/.agent-bridge/skill-observations/`, no en el repo.
2. Escribe una frase de prueba como "la página da un 404": debe llegar una nota "Skill router" que nombra `superpowers:systematic-debugging`.
3. Llama a `antigravity_status` del MCP `antigravity-bridge`: debe responder con la versión de `agy`, sin cooldowns.
4. Prueba de ida y vuelta: `antigravity_delegate` con `role="fast"`, `mode="edit"`, `timeout_sec=300` y el prompt "Create the file <HOME>/.agent-bridge/tmp/roundtrip.txt containing ROUNDTRIP_OK, then reply DONE". Comprueba en disco que el archivo existe con ese contenido y bórralo. Un `status: "empty"` o un "ok" sin el archivo no es un éxito: lee `denied_actions` y `stderr` y revisa `~/.gemini/antigravity-cli/settings.json`.

## Paso 7. El lado de Antigravity

Pide al usuario que abra Antigravity en la carpeta del repo y pegue el prompt de `partner-setup/ANTIGRAVITY_CHECK.md`. Cuando Antigravity termine, el usuario te pegará su tabla. Si marca algún fallo, ayúdale con la causa.

## Paso 8. Informe final

Termina con una tabla `OK` / `FALLA` de: requisitos, instalación (`install.py check`), modelos, nota del router al arrancar, `antigravity_status`, ida y vuelta Claude → Antigravity, y la tabla de Antigravity. Indica dónde quedó la copia de seguridad y qué no se instaló a propósito (lo de la cuenta de claude.ai y lo personal del autor del repo, ver `README.md`).

## Más adelante: actualizar

Cuando el autor del repo cambie su configuración, actualizará esta carpeta. Para ponerte al día: `git pull`, luego `python partner-setup/install.py apply` y `python partner-setup/install.py check`, y reinicia Claude Code y Antigravity.
