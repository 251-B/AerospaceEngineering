# Cuentas en la nube con códigos de invitación (Supabase)

Mientras `assets/data/account-config.js` esté vacío, las cuentas son locales (cada navegador guarda la suya). Al rellenarlo con un proyecto de Supabase:

- crear cuenta exige un **código de invitación de un solo uso** (`SIDR-XXXX-XXXX`), que la base de datos comprueba y gasta en la misma operación (dos personas con el mismo código a la vez: entra una sola);
- se inicia sesión desde cualquier dispositivo y se sincronizan asignaturas, ajustes, tiempo de estudio, favoritos, notas, páginas recientes e historial del simulador (tabla `user_state`, una fila por usuario, protegida por RLS: cada uno solo ve la suya);
- "Forgot it?" envía un correo para cambiar la contraseña, y "Delete account" borra la cuenta y sus datos del servidor.

## 1. Crear el proyecto

1. <https://supabase.com> → New project (plan gratuito; región `eu-west` o `eu-central`).
2. Guarda la contraseña de la base de datos en tu gestor de contraseñas (no se usa en la web).

## 2. Crear las tablas y funciones

SQL Editor → New query → pega el contenido de `supabase/migrations/0001_sideris_accounts.sql` → Run. Se puede volver a ejecutar sin romper nada.

Crea: `invite_codes` (solo el hash SHA-256 de cada código, nunca el código), la función `hook_before_user_created`, `invite_status` (para que el formulario diga "Valid code" / "Already used"), `user_state` y `delete_my_account`.

## 3. Activar el filtro de invitaciones (obligatorio)

Authentication → Hooks (en algunos paneles: Auth Hooks) → **Before User Created** → Add hook → tipo **Postgres** → schema `public`, función `hook_before_user_created` → Enable.

Sin este paso cualquiera podría registrarse sin código. Compruébalo con el paso 7.

## 4. Ajustes de Auth

Authentication → Sign In / Providers → Email:

- **Confirm email**: **desactívalo** mientras uses el correo por defecto de Supabase, que solo envía a los miembros de tu equipo de Supabase (y unos pocos correos por hora): tus invitados no recibirían la confirmación. El código de invitación ya limita quién entra. Si más adelante configuras un SMTP propio (Authentication → Emails → SMTP Settings, p. ej. con Resend o Brevo), puedes activarlo: el formulario mostrará "Almost there: open the email we sent…".
- Lo mismo vale para "Forgot it?": sin SMTP propio el correo de nueva contraseña solo llega a los miembros del equipo; mientras tanto, la contraseña se cambia desde Authentication → Users → la persona → Send password recovery (o borrando y volviendo a invitar).
- Authentication → URL Configuration: **Site URL** = la dirección de la web (p. ej. `https://<tu-dominio>/`) y en **Redirect URLs** añade `https://<tu-dominio>/account/login.html`, para que los correos de confirmación y de nueva contraseña vuelvan a la web.

## 5. Generar códigos

En tu ordenador, desde la raíz del repositorio:

```bash
python tools/invites/make_invites.py 20 --label "Grupo 251-B"
python tools/invites/make_invites.py 5 --label "Profesores" --expires 2027-06-30
```

Escribe en `tools/invites/out/` (ignorado por git, **nunca lo subas**):

- `codes-<fecha>.csv`: los códigos para repartir, con su enlace directo (`--site <dirección>` si la web ya no está en `251-b.github.io`);
- `codes-<fecha>.sql`: pégalo en el SQL Editor y Run. Solo contiene hashes.

Enlace para repartir: `https://<tu-dominio>/account/signup.html?invite=SIDR-XXXX-XXXX` (el campo se rellena solo).

Consultas útiles en el SQL Editor:

```sql
-- quién ha usado qué invitación
select label, used_at, used_email from public.invite_codes order by used_at desc nulls last;
-- anular las invitaciones no usadas de un lote
delete from public.invite_codes where label = 'Grupo 251-B' and used_at is null;
```

## 6. Conectar la web

Project Settings → API (o Data API) → copia **Project URL** y la clave **anon / public** (o *publishable*) en `assets/data/account-config.js`:

```js
window.AE_ACCOUNT_CONFIG = window.AE_ACCOUNT_CONFIG || {
  supabaseUrl: 'https://abcdefghijklmnop.supabase.co',
  supabaseAnonKey: 'eyJ...',
  requireInvite: true
};
```

Ambas son públicas por diseño (van en el navegador de cada visitante); lo que protege los datos es la RLS. **Nunca pongas la clave `service_role` / *secret*** en la web ni en el repositorio.

## 7. Comprobar

1. Abre `account/signup.html` sin código e intenta crear cuenta → "This invite code is not valid or has already been used."
2. Con un código del CSV → "Valid code" al escribirlo → cuenta creada.
3. Otra persona con el mismo código → "Already used" y se rechaza.
4. Inicia sesión en otro navegador → aparecen tus asignaturas y notas.

## Qué no cubre esto

Las cuentas protegen los datos personales, no el contenido: las páginas de estudio siguen siendo archivos estáticos. Para que solo las personas invitadas puedan ver el temario, ver `docs/private-hosting.md`.

Las cuentas locales que ya existan en un navegador no se suben solas: al crear la cuenta en la nube con el mismo email, las preferencias, notas y tiempo de estudio de ese navegador se suben en la primera sincronización.
