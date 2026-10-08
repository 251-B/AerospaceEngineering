#!/usr/bin/env python3
"""Obsidian vault linter with safe, idempotent auto-fixes.

Checks:
    no-frontmatter         (error) note has no YAML frontmatter
    frontmatter-keys       (warn)  frontmatter lacks tags or subject/materia
    backticked-wikilink    (error, fixable) `[[Note]]` is rendered as code, not as a link
    text-ampersand         (error, fixable) '&' inside \\text{...} breaks KaTeX tables
    broken-wikilink        (error) [[target]] matches no note or attachment (case-insensitive)
    dangling-source-path   (error) 'sources/....pdf' mentioned in a note does not exist
    spanish-note           (warn)  note prose is predominantly Spanish (portal standard: English)

--fix rewrites only the two fixable kinds, never touches fenced code blocks, preserves
line endings and accents, and skips files that are not valid UTF-8.

Usage:
    python tools/vault_lint.py [--root vault] [--fix] [-v] [--json] [--only a,b] [--skip a,b] [--quiet]
Exit code 1 when any error remains.
"""
import argparse
import collections
import dataclasses
import json
import os
import pathlib
import re
import sys

from audit_portal import FileIndex, Finding

CHECKS = ("no-frontmatter", "frontmatter-keys", "backticked-wikilink", "text-ampersand",
          "broken-wikilink", "dangling-source-path", "spanish-note")
EXCLUDED_DIRS = {".obsidian", ".trash", "Templates", "attachments"}

_FENCE = re.compile(r"(?ms)^[ \t]*(`{3,}|~{3,})[^\n]*\n.*?(?:^[ \t]*\1[ \t]*\r?$|\Z)")  # \r?: CRLF notes
_FRONTMATTER = re.compile(r"\A\ufeff?---\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.S)
_BACKTICKED = re.compile(r"(?<!`)`(!?\[\[(?:(?!\]\])[^`\n])+\]\])`(?!`)")  # aliases may contain single [ ]
_TEXT_MACRO = re.compile(r"\\text\{([^{}]*)\}")
_UNESCAPED_AMP = re.compile(r"(?<!\\)&")
_WIKILINK = re.compile(r"!?\[\[([^\[\]\n|#^]*)(?:[#^][^\[\]\n|]*)?(?:\|(?:(?!\]\])[^\n])*)?\]\]")
_SOURCE_PATH = re.compile(r"sources/[^\n\"'`|\]\)<>]*?\.pdf")

_ES = re.compile(r"\b(?:el|la|los|las|del|de|que|para|con|una|por|se|como|donde|en|es)\b", re.I)
_EN = re.compile(r"\b(?:the|of|and|which|with|for|is|this|that|where|from|in|are)\b", re.I)


def _blank(m):
    return re.sub(r"[^\n]", " ", m.group(0))


def mask_fenced(text):
    return _FENCE.sub(_blank, text)


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


# --------------------------------------------------------------------------- fixing
def _fix_segment(segment, counts):
    segment, n = _BACKTICKED.subn(r"\1", segment)
    counts["backticked-wikilink"] += n

    def escape(m):
        inner, n_amp = _UNESCAPED_AMP.subn(r"\\&", m.group(1))
        if n_amp:
            counts["text-ampersand"] += 1
        return "\\text{" + inner + "}"

    return _TEXT_MACRO.sub(escape, segment)


def fix_text(text):
    """Return (fixed_text, counts). Fenced code blocks are left untouched."""
    counts = collections.Counter()
    out, last = [], 0
    for m in _FENCE.finditer(text):
        out.append(_fix_segment(text[last:m.start()], counts))
        out.append(m.group(0))
        last = m.end()
    out.append(_fix_segment(text[last:], counts))
    return "".join(out), counts


def iter_notes(vault):
    vault = pathlib.Path(vault)
    return sorted(p for p in vault.rglob("*.md") if not (set(p.relative_to(vault).parts) & EXCLUDED_DIRS))


def fix(vault):
    """Apply the safe fixes in place; return a summary Counter."""
    summary = collections.Counter({"files_changed": 0, "skipped": 0})
    for path in iter_notes(vault):
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            summary["skipped"] += 1
            continue
        fixed, counts = fix_text(text)
        if fixed != text:
            path.write_bytes(fixed.encode("utf-8"))
            summary["files_changed"] += 1
            summary.update(counts)
    return summary


# --------------------------------------------------------------------------- linting
def _link_index(vault):
    names = set()
    for p in pathlib.Path(vault).rglob("*"):
        if p.is_file() and ".obsidian" not in p.relative_to(vault).parts:
            rel = p.relative_to(vault).as_posix().lower()
            names.update({rel, p.name.lower()})
            if p.suffix.lower() == ".md":
                names.update({rel[:-3], p.stem.lower()})
    return names


def _link_resolves(target, names):
    t = target.strip().rstrip("\\").strip().lstrip("/").lower()
    return not t or t in names or (t.endswith(".md") and t[:-3] in names)


def _prose(text):
    body = _FRONTMATTER.sub("", text, count=1)
    body = mask_fenced(body)
    for pattern in (r"\$\$.*?\$\$", r"\$[^$\n]*\$", r"`[^`\n]*`", r"!?\[\[[^\]]*\]\]", r"https?://\S+"):
        body = re.sub(pattern, " ", body, flags=re.S)
    return body


def lint(vault, repo_root=None):
    vault = pathlib.Path(vault)
    repo_root = pathlib.Path(repo_root) if repo_root else vault.parent
    names = _link_index(vault)
    files = FileIndex(repo_root)
    findings = []
    for path in iter_notes(vault):
        rel = path.relative_to(vault).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        masked = mask_fenced(text)

        fm = _FRONTMATTER.match(text)
        if not fm:
            findings.append(Finding("no-frontmatter", "error", rel, 1, "note has no YAML frontmatter"))
        else:
            keys = set(re.findall(r"^([A-Za-z_][\w-]*)\s*:", fm.group(1), re.M))
            missing = [label for label, ok in (("tags", "tags" in keys),
                                               ("subject/materia", bool(keys & {"subject", "materia"}))) if not ok]
            if missing:
                findings.append(Finding("frontmatter-keys", "warn", rel, 1,
                                        f"frontmatter lacks: {', '.join(missing)}"))

        for m in _BACKTICKED.finditer(masked):
            findings.append(Finding("backticked-wikilink", "error", rel, line_of(masked, m.start()),
                                    f"link shown as code: {m.group(0)[:60]}"))
        for m in _TEXT_MACRO.finditer(masked):
            if _UNESCAPED_AMP.search(m.group(1)):
                findings.append(Finding("text-ampersand", "error", rel, line_of(masked, m.start()),
                                        f"unescaped '&' inside \\text: {m.group(0)[:50]}"))
        for m in _WIKILINK.finditer(masked):
            if not _link_resolves(m.group(1), names):
                findings.append(Finding("broken-wikilink", "error", rel, line_of(masked, m.start()),
                                        f"unresolved link: [[{m.group(1).strip()}]]"))
        for m in _SOURCE_PATH.finditer(text):
            if not files.exists(os.path.join(files.root, m.group(0))):
                findings.append(Finding("dangling-source-path", "error", rel, line_of(text, m.start()),
                                        f"file not found: {m.group(0)}"))

        prose = _prose(text)
        es, en = len(_ES.findall(prose)), len(_EN.findall(prose))
        if es + en >= 15 and es > en:
            findings.append(Finding("spanish-note", "warn", rel, 1, f"predominantly Spanish (es={es}, en={en})"))
    return sorted(findings, key=lambda f: (f.check, f.file, f.line))


# --------------------------------------------------------------------------- CLI
def main(argv=None):
    here = pathlib.Path(__file__).resolve().parents[1]
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=here / "vault", type=pathlib.Path, help="vault directory")
    ap.add_argument("--fix", action="store_true", help="apply the safe auto-fixes first")
    ap.add_argument("-v", "--verbose", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--only", default="")
    ap.add_argument("--skip", default="")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    only = {c for c in args.only.split(",") if c}
    skip = {c for c in args.skip.split(",") if c}
    unknown = (only | skip) - set(CHECKS)
    if unknown:
        ap.error(f"unknown check(s): {', '.join(sorted(unknown))}")

    if args.fix:
        summary = fix(args.root)
        if not args.quiet:
            print(f"fixed {summary['files_changed']} file(s): "
                  f"{summary['backticked-wikilink']} backticked link(s), "
                  f"{summary['text-ampersand']} \\text ampersand(s); skipped {summary['skipped']} non-UTF-8")

    findings = [f for f in lint(args.root) if (not only or f.check in only) and f.check not in skip]
    errors = [f for f in findings if f.severity == "error"]
    if not args.quiet:
        if args.json:
            print(json.dumps([dataclasses.asdict(f) for f in findings], indent=2, ensure_ascii=False))
        else:
            by_check = collections.defaultdict(list)
            for f in findings:
                by_check[f.check].append(f)
            print(f"{'check':22} {'sev':5} {'findings':>8} {'notes':>6}")
            for check in CHECKS:
                group = by_check.get(check, [])
                if group:
                    print(f"{check:22} {group[0].severity:5} {len(group):8} {len({f.file for f in group}):6}")
            if args.verbose:
                print()
                for f in findings:
                    print(f"{f.file}:{f.line}: [{f.check}] {f.message}")
            warns = len(findings) - len(errors)
            print(f"\n{len(errors)} error(s), {warns} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
