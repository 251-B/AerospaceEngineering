---
subject: "Repository"
tags:
  - repository
  - tool
  - vault
  - sources
source: "tools/build_source_notes.py"
---

# Tool - build_source_notes

## Purpose

Writes one generated note for every file under `sources/` into `vault/07 - Sources/`, plus one `Sources Index` per subject. Each note records the file's repo path, kind (`teoria`, `slides`, `problemas`, `examenes`, `schedule`, `laboratorio` or `other`), size and status, and lists the vault notes that reference it. The status is one of `referenced`, `not-referenced`, `build-artifact` (LaTeX build files) or `working-file` (scratch files). The lists of artifacts and working files live in `tools/source_notes.json`.

A note counts as referenced when a vault note contains its full repo path, or its file name when that name is unique in `sources/`. A mention in a MOC counts. Extraction is a separate step, so a referenced file may still lack its content.

## Command

`python tools/build_source_notes.py` writes the notes. `python tools/build_source_notes.py --check` exits 1 when a note is missing, stale or orphaned.

## Read and write behaviour

- Reads `sources/` and the vault. It never writes under `sources/`.
- Writes only under `vault/07 - Sources/`. It deletes an orphan only when the note carries the generated banner, and it refuses to touch hand-written files there.
- Output is deterministic: running it twice changes nothing.
- Reuses the laboratory rule and the category names of [[Tool - sources_manifest]].

## When to run

After adding, moving or removing a file under `sources/`, or after writing a vault note that references a source. Run `--check` in the closing gate of [[Rules - AGENTS.md]].

## Related

[[Repository MOC]] · [[Tool - sources_manifest]] · [[Tool - Test suite]]
