---
tags:
  - vault
  - guide
subject: General
---

# Second Brain: 2nd Year Aerospace Engineering (UC3M)

This vault is the source of truth for the study portal. Notes are written here first; the web pages under
`subjects/` are generated from them (Obsidian first, web second).

---

## Opening the vault in Obsidian

1. Open **Obsidian**.
2. Choose **Open folder as vault**.
3. Select the folder `AerospaceEngineering/vault`.
4. The knowledge graph, links and notes are now available.

---

## Vault structure

* **[[00 - Indice Central/Master Index|00 - Central Index]]**: master map of content (MOC); start here.
* `01 - Fluid Mechanics/`: Fluid Mechanics.
* `02 - Aerospace Materials I/`: Aerospace Materials I.
* `03 - Engineering Mechanics/`: Mechanics Applied to Aerospace Engineering.
* `04 - Advanced Maths/`: Advanced Mathematics (ordinary and partial differential equations).
* `05 - Business Management/`: Business Management.
* `Templates/`: reusable templates for theory concepts, solved problems and formula sheets.
* `attachments/`: embedded files.

---

## Conventions

* **Links:** use bidirectional links whenever a note mentions a law, theorem or property. Write them as real
  links, never inside backticks (inline code is not a link and breaks the graph). Syntax:

  ```text
  [[Note name]]            link to a note
  [[Folder/Note name|text]] link with a display text
  ```

* **Math (KaTeX):** `$...$` inline and `$$...$$` for display equations. Inside `\text{...}` escape ampersands
  as `\&`.
* **Frontmatter:** every note starts with YAML containing at least `tags` and `subject` (plus `topic` where it
  applies).
* **Sources:** cite official material by path under `sources/cuatrimestre-1/` with page or equation numbers.
  Never adjust a result to match an official answer: if they differ, show the honest result in a callout
  `> [!warning] Discrepancy with the official solution`.
* **Language:** academic English.
* **Useful tags:** `#teoria`, `#problema-examen`, `#formula-clave`, `#duda`.

---

## Checking the vault

From the repository root:

```text
python tools/vault_lint.py          report problems
python tools/vault_lint.py --fix    apply the safe automatic fixes
```
