# Contenido privado: solo para personas invitadas

## Por qué hace falta cambiar el alojamiento

Las cuentas (ver `docs/supabase-setup.md`) protegen los datos de cada persona, pero el temario son archivos estáticos: hoy cualquiera puede abrirlos en `251-b.github.io` o leerlos en el repositorio público de GitHub. Un bloqueo hecho con JavaScript en la propia página se salta en segundos (basta con desactivar JS o pedir el archivo directamente), así que el control tiene que estar **delante** de los archivos, en el servidor.

GitHub Pages no lo permite: incluso desde un repositorio privado (plan de pago) la web publicada sigue siendo pública. Por eso el plan es:

1. Servir la web desde **Cloudflare Pages**.
2. Ponerle delante **Cloudflare Access** (Zero Trust, gratis hasta 50 usuarios): antes de ver cualquier archivo, la persona escribe su email y recibe un código de un solo uso; solo entran los emails de la lista.
3. Hacer **privado** el repositorio de GitHub y apagar GitHub Pages.

Las invitaciones de Supabase siguen siendo las que crean la cuenta de estudio; Access decide quién puede abrir la web. Para alguien nuevo: añade su email a la lista de Access y mándale su enlace de invitación.

## Pasos (en este orden, para que la web no se caiga)

### 1. Cloudflare Pages

1. Crea una cuenta en <https://dash.cloudflare.com>.
2. Workers & Pages → Create → Pages → **Connect to Git** → autoriza GitHub y elige `251-B/AerospaceEngineering`, rama `main`.
3. Build settings: Framework preset **None**, Build command **vacío**, Build output directory **`/`**.
4. Deploy. Queda en `https://<nombre>.pages.dev`. Ábrela y comprueba que el portal funciona igual.

### 2. Cloudflare Access

1. Zero Trust (menú izquierdo) → elige un nombre de equipo y el plan **Free**.
2. Settings → Authentication → Login methods: deja **One-time PIN** (no hace falta nada más).
3. Access → Applications → Add an application → **Self-hosted**:
   - Application domain: `<nombre>.pages.dev`; añade otro dominio `*.<nombre>.pages.dev` para que las vistas previas de cada rama también queden protegidas.
   - Session duration: 1 month (para no pedir el código cada día).
4. Policy → Action **Allow** → Include → **Emails** → la lista de personas invitadas. (Alternativa más amplia: *Emails ending in* `@alumnos.uc3m.es`, que deja entrar a cualquier estudiante de la UC3M.)
5. Guarda y abre la web en una ventana privada: debe pedir el email y el código antes de mostrar nada, incluidos los PDF (`/assets/pdf/...`) y las fuentes (`/sources/...`).

### 3. Cerrar lo público

1. GitHub → repo → Settings → Pages → desactiva la publicación (Source: None).
2. GitHub → repo → Settings → General → Danger Zone → **Change repository visibility → Private**. Cloudflare Pages sigue desplegando porque la app de Cloudflare tiene acceso al repo.
3. Cambia la dirección del portal donde aparece:
   - `assets/js/ask-ai.js`: constante `PORTAL` (los prompts de "Ask AI" enlazan a la web; con la web privada Claude/Gemini no podrán abrir esos enlaces y usarán el material pegado, que ya va en el prompt).
   - Supabase → Authentication → URL Configuration: Site URL y Redirect URLs con la nueva dirección.
   - Al generar invitaciones: `python tools/invites/make_invites.py 20 --site https://<nombre>.pages.dev/`.

## Mantenimiento

- Persona nueva: añade su email en la policy de Access y envíale el enlace del CSV de invitaciones.
- Quitar acceso: borra su email de la policy (y, si quieres, su cuenta en Supabase → Authentication → Users).
- Todo `git push` a `main` se publica solo en Cloudflare en uno o dos minutos.

## Posible mejora (extensión, no hecha)

Unir los dos pasos: que al gastar una invitación en Supabase se añada su email a Access automáticamente (Database Webhook de Supabase → Cloudflare API). Requiere un token de Cloudflare guardado en Supabase; se puede hacer más adelante.
