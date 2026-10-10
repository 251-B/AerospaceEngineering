# tools/: quality gates and generators

Pure-stdlib Python 3 (no installs). Run everything from the repository root.

| Tool | Purpose | Exit code |
|---|---|---|
| `python tools/audit_portal.py` | Static gate for `index.html` + `subjects/**/*.html` | 1 if any error |
| `python tools/vault_lint.py` | Lint the Obsidian `vault/` (`--fix` applies the safe fixes) | 1 if any error |
| `python tools/source_links.py` | Add deep links to the official PDFs (problem statements, topic panel, inline citations) from `tools/source_links.json`; `--check` = fail if stale, `--refresh-anchors` = re-resolve labels with `pdftotext`, `-v` = list unresolved citations | 1 if stale (`--check`) or a problem card has no PDF page |
| `python tools/sources_manifest.py` | Regenerate `assets/data/sources.js` from `sources/cuatrimestre-1/` (`--check` = fail if stale) | 1 if stale (`--check`) |
| `python -m unittest discover -s tools/tests` | Test suite for all of the above + `tokens.css` + `theme.js` (headless Edge/Chrome) | 1 on failure |

Common flags for both linters: `-v` list every finding, `--json`, `--only a,b`, `--skip a,b`, `--quiet`.

## audit_portal.py checks

`broken-link` (case-sensitive, like GitHub Pages) · `missing-backlink` · `katex-parity` ·
`katex-text-ampersand` · `debris` (scratch "Wait", U+FFFD, `??` headers, raw markdown) ·
`spanish-label` · `false-claim` ("fully verified", "zero hallucinations") ·
`lab-reference` (labs are not on the web) · `theme-key` (only `ae_theme`) · `badge-drift`.

**Markup contracts the checks rely on**

- Hub cards: `<article data-subject="<slug>">` containing `<a href=".../teoria|problemas/...">` with a
  `<span class="area-badge ...">3 topics</span>` / `38 prob.`. A "topic" is a distinct `topic-N` file number.
- A solved problem is one `class="problem-card"` (or `problem-box`) element on a `problemas/*.html` page.
  New pages should use `problem-card`.

## vault_lint.py

Errors: `no-frontmatter`, `backticked-wikilink` (fixable), `text-ampersand` (fixable), `broken-wikilink`,
`dangling-source-path`. Warnings: `frontmatter-keys`, `spanish-note`.
`--fix` is idempotent, skips fenced code, preserves CRLF/accents, and skips non-UTF-8 files.
Excluded folders: `.obsidian`, `.trash`, `Templates`, `attachments`.
Known limit: a link whose alias ends in `]` (`...[101]]]`) is ambiguous and must be fixed by hand.

## Shared assets

- `assets/css/tokens.css`: design tokens, verbatim from the original `index.html`.
- `assets/js/theme.js`: load synchronously in `<head>`. Single key `ae_theme`; migrates `aero-portal-theme`
  and `theme`; default dark; syncs tabs; `window.AETheme`; wires `#themeToggle` / `#themeLabel`.
- `assets/data/sources.js`: `window.AE_SOURCES` = official PDFs (160 files) per subject / unit / category
  (`teoria`, `slides`, `problemas`, `examenes`, `schedule`). **Laboratory material is never included.**
  Hrefs are repo-root-relative and URL-encoded; prefix them with the page's relative path to the root.

## Baseline when these tools were introduced (2026-10-08)

`audit_portal.py`: 424 errors in 47 files (14 broken links, 196 debris, 77 Spanish labels, 5 false claims,
8 lab references, 122 legacy theme keys, 2 badge drifts).
`vault_lint.py`: 989 errors / 105 warnings (915 backticked links and 26 ampersands are auto-fixable).
The goal of the remediation phases is zero errors from both.
