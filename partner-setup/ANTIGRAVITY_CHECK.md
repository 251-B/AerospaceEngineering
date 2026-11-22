# ANTIGRAVITY_CHECK: prompt para el Antigravity del compañero

Pega el bloque de abajo en Antigravity (la app o `agy` en una terminal), abierto en la carpeta del repo. Hazlo **después** de que Claude Code haya terminado `python partner-setup/install.py apply` y `check` sin fallos, de haber reiniciado Claude Code (paso 6 de `AI_SETUP.md`) y de haber cerrado y vuelto a abrir Antigravity.

```text
Acabamos de instalar en este ordenador la misma configuración de Claude Code y Antigravity que usa el autor del repo, con partner-setup/install.py. Comprueba tu lado y el puente con Claude, sin cambiar nada salvo que te lo pida.

Lee primero partner-setup/README.md, partner-setup/manifest.json y ~/.agent-bridge/TEAM_PROTOCOL.md.

1. Plugins y MCP: confirma que tienes cargados agent-bridge, skill-evolution, aerospace-study-workflows, superpowers, claude-mem y ui-design-craft (en ~/.gemini/config/plugins/) y chrome-devtools-plugin, y di cuántas skills aporta cada uno. Confirma también que están activos los servidores MCP agent-bridge_claude-bridge y claude-mem_claude-mem y que tienes los 6 subagentes de aerospace-study-workflows (aerospace-pedagogue, problem-step-mentor, source-researcher, subject-web-builder, task-runner, web-qa-reviewer).
2. Router: dime qué notas de hook te han llegado con este mensaje. Es normal que ya llegue una nota "Skill router", porque este texto contiene palabras clave. Luego te escribiré "la página da un 404" y debe llegar una nota "Skill router" que active systematic-debugging.
3. Aprendizaje: confirma que el hook SessionStart de skill-evolution apunta a ~/.agent-bridge/skill-observations/observation-log (log compartido con Claude) y te pide ejecutar task-observer.
4. Puente: llama a claude_status y luego haz una prueba con claude_delegate (role "fast", mode "read_only", timeout_sec 300, prompt "Reply with the single word OK"). Debe volver "OK". Un status "empty" o un timeout es un fallo: enséñame permission_denials, warnings y stderr de la respuesta.
5. Permisos de tu terminal: ejecuta un comando inofensivo (git --version) y lee un archivo de ~/.agent-bridge/ (por ejemplo TEAM_PROTOCOL.md). Si el comando falla con "sandbox configuration error ... non-absolute file path", las reglas de ~/.gemini/antigravity-cli/settings.json no tienen la sintaxis que espera esta versión. No intentes leer ese archivo tú mismo, porque Antigravity lo protege. Dime el error exacto y la sintaxis correcta para que la arregle Claude.
6. Modelos: compara los roles de ~/.agent-bridge/config.json (Hydrogen medium, Hydrogen high, Neon high) con los modelos que puedes usar. Si no puedes ejecutar agy models desde aquí, pídeme la lista, que Claude ya la guardó. Si falta alguno, propón el más parecido.

Termina con una tabla OK/FALLA de los seis puntos y, si algo falla, la causa y cómo arreglarla.
```

Cuando Antigravity termine, copia su tabla y pégasela a Claude Code: él te ayuda con lo que haya fallado.
