---
subject: "Repository"
tags:
  - repository
  - tool
  - vault
source: "tools/vault_rename.py"
---

# Tool - vault_rename

## Purpose

Renames vault notes from a JSON map and rewrites every wikilink that points at them, including aliases, heading links and embeds. Fenced code is left alone. The tool applies the English note naming convention in [[Rules - AGENTS.md]] (`Concept - ...`, `Problem - ...`, `Topic N - ...`, `Formula Sheet - ...` and `<Subject> MOC`).

## Command

`python tools/vault_rename.py map.json [--apply] [--links-only] [--vault DIR]`

`map.json` is a JSON object that maps each old note name to its new name, without the `.md` extension.

## Read and write behaviour

- Dry run by default: it prints what would change and writes nothing.
- `--apply`: renames the note files and rewrites links in every `.md` file under the vault. This includes the `Templates` folder, which [[Tool - vault_lint]] excludes.
- `--links-only`: rewrites links only, for notes that are already renamed. It skips the checks below.
- Refuses, with exit 1, when a source note is missing, a target name already exists, a name contains an illegal character, or two notes would share a new name.

## When to run

Only when a note name must change. Run the dry run first, then `--apply`, then [[Tool - vault_lint]] to confirm that no broken wikilink remains.

## Related

[[Repository MOC]] · [[Tool - vault_lint]] · [[Tool - Test suite]]
