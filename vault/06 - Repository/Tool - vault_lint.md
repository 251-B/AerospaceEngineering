---
subject: "Repository"
tags:
  - repository
  - tool
  - vault
source: "tools/vault_lint.py"
---

# Tool - vault_lint

## Purpose

Lints the Obsidian vault in `vault/` for frontmatter, link and KaTeX-safety problems, and applies two safe auto-fixes. It is the vault half of the closing gate.

## Command

`python tools/vault_lint.py [--root vault] [--fix] [-v] [--json] [--only a,b] [--skip a,b] [--quiet]`

## Checks

- Errors: `no-frontmatter`, `backticked-wikilink` (fixable), `text-ampersand` (fixable, an `&` inside `\text{...}`), `broken-wikilink`, `dangling-source-path`.
- Warnings: `frontmatter-keys` (no `tags`, or neither `subject` nor `materia`) and `spanish-note` (prose mostly in Spanish).
- Excluded folders: `.obsidian`, `.trash`, `Templates`, `attachments`.

## Flags

- `--root`: vault directory (default `vault/`).
- `--fix`: applies the two fixable kinds before linting. It is idempotent, skips fenced code and non-UTF-8 files, and preserves CRLF line endings.
- `-v`, `--json`, `--only`, `--skip`, `--quiet`: output control.
- Exit code 1 when any error remains.

## Read and write behaviour

Read-only unless `--fix` is given. Without it, the tool reads the notes and checks that `sources/` paths named in them exist. With `--fix`, it rewrites `.md` notes in `vault/` in place. It imports `FileIndex` and `Finding` from `tools/audit_portal.py`, so that script must stay in place.

## When to run

- After any edit to a note in `vault/`, including the notes in this folder.
- Closing gate: 0 errors are required (see [[Rules - AGENTS.md]]).

## Related

[[Repository MOC]] · [[Tool - audit_portal]] · [[Tool - vault_rename]] · [[Tool - Test suite]] · [[Agent - web-qa-reviewer]]
