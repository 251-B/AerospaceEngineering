-- Sideris: accounts by invitation, with single-use keys, and each reader's data in the cloud.
--
-- Run it once in the Supabase SQL editor of the project (Dashboard > SQL Editor > New query),
-- then turn on the "Before User Created" auth hook (docs/supabase-setup.md, step 4).
--
-- * public.invite_codes: one row per key. Only the SHA-256 of the key is stored (code_hash), so
--   the table never reveals a key; used_at / used_email mark it as spent.
-- * public.hook_before_user_created(event): Supabase calls it before creating any user. It
--   rejects the sign-up unless user_metadata.invite holds a valid, unused key, and spends that key
--   in the same UPDATE, so two people can never use one key, even at the same instant.
-- * public.user_state: one JSON document per user (preferences, favourites and notes, study log,
--   simulator history), readable and writable only by its owner (row level security).
-- * public.invite_status(code): lets the sign-up page say "this key is not valid / already used"
--   before the form is sent; it never reveals anything else and never spends the key.

create extension if not exists pgcrypto;

-- ---------------------------------------------------------------- keys
create table if not exists public.invite_codes (
  id          bigint generated always as identity primary key,
  code_hash   text not null unique,              -- encode(digest(upper(trim(code)), 'sha256'), 'hex')
  label       text,                              -- who it was given to (optional, for you)
  created_at  timestamptz not null default now(),
  expires_at  timestamptz,                       -- optional
  used_at     timestamptz,
  used_email  text
);

alter table public.invite_codes enable row level security;
-- no policies: nobody reads or writes it through the API; only the functions below and the SQL
-- editor (owner) touch it.

create or replace function public.invite_hash(code text)
returns text language sql immutable as $$
  select encode(extensions.digest(upper(regexp_replace(coalesce(code, ''), '\s', '', 'g')), 'sha256'), 'hex')
$$;

-- ---------------------------------------------------------------- the sign-up gate
create or replace function public.hook_before_user_created(event jsonb)
returns jsonb
language plpgsql
security definer
set search_path = public, extensions
as $$
declare
  key   text := event -> 'user' -> 'user_metadata' ->> 'invite';
  email text := event -> 'user' ->> 'email';
  spent bigint;
begin
  if key is null or length(trim(key)) = 0 then
    return jsonb_build_object('error', jsonb_build_object(
      'http_code', 403, 'message', 'An invite code is needed to create an account.'));
  end if;

  update public.invite_codes
     set used_at = now(), used_email = email
   where code_hash = public.invite_hash(key)
     and used_at is null
     and (expires_at is null or expires_at > now())
  returning id into spent;

  if spent is null then
    return jsonb_build_object('error', jsonb_build_object(
      'http_code', 403, 'message', 'This invite code is not valid or has already been used.'));
  end if;

  return '{}'::jsonb;
end;
$$;

-- Supabase Auth runs hooks as supabase_auth_admin; nobody else may call the gate.
do $$
begin
  if exists (select 1 from pg_roles where rolname = 'supabase_auth_admin') then
    execute 'grant execute on function public.hook_before_user_created(jsonb) to supabase_auth_admin';
    execute 'grant usage on schema public to supabase_auth_admin';
  end if;
end $$;
revoke execute on function public.hook_before_user_created(jsonb) from public;
do $$
begin
  if exists (select 1 from pg_roles where rolname = 'anon') then
    execute 'revoke execute on function public.hook_before_user_created(jsonb) from anon, authenticated';
  end if;
end $$;

-- A read-only check for the form: 'valid', 'used' or 'unknown'. Never spends the key.
create or replace function public.invite_status(code text)
returns text
language sql
stable
security definer
set search_path = public, extensions
as $$
  select coalesce((
    select case
             when used_at is not null then 'used'
             when expires_at is not null and expires_at <= now() then 'used'
             else 'valid'
           end
      from public.invite_codes
     where code_hash = public.invite_hash(code)
  ), 'unknown')
$$;

do $$
begin
  if exists (select 1 from pg_roles where rolname = 'anon') then
    execute 'grant execute on function public.invite_status(text) to anon, authenticated';
  end if;
end $$;

-- ---------------------------------------------------------------- each reader's data
create table if not exists public.user_state (
  user_id     uuid primary key references auth.users (id) on delete cascade,
  data        jsonb not null default '{}'::jsonb,
  updated_at  timestamptz not null default now()
);

alter table public.user_state enable row level security;

drop policy if exists "own state: read"   on public.user_state;
drop policy if exists "own state: insert" on public.user_state;
drop policy if exists "own state: update" on public.user_state;
drop policy if exists "own state: delete" on public.user_state;
create policy "own state: read"   on public.user_state for select using (auth.uid() = user_id);
create policy "own state: insert" on public.user_state for insert with check (auth.uid() = user_id);
create policy "own state: update" on public.user_state for update using (auth.uid() = user_id) with check (auth.uid() = user_id);
create policy "own state: delete" on public.user_state for delete using (auth.uid() = user_id);

do $$
begin
  if exists (select 1 from pg_roles where rolname = 'authenticated') then
    execute 'grant select, insert, update, delete on public.user_state to authenticated';
  end if;
end $$;

-- ---------------------------------------------------------------- deleting one's own account
-- Settings > Delete my account: removes the signed-in user (and, by cascade, their user_state).
-- The key they used stays spent.
create or replace function public.delete_my_account()
returns void
language plpgsql
security definer
set search_path = public
as $$
begin
  if auth.uid() is null then
    raise exception 'not signed in';
  end if;
  delete from auth.users where id = auth.uid();
end;
$$;

revoke execute on function public.delete_my_account() from public;
do $$
begin
  if exists (select 1 from pg_roles where rolname = 'authenticated') then
    execute 'grant execute on function public.delete_my_account() to authenticated';
  end if;
end $$;
