#!/usr/bin/env python3
"""Static quality gate for the study portal (index.html + subjects/**/*.html).

Checks (all severity "error"):
    broken-link          local href/src that does not exist (case-sensitive, like GitHub Pages)
    missing-backlink     subject page with no link back to the root index.html
    katex-parity         odd number of $$ or $ delimiters
    katex-text-ampersand '&' inside \\text{...} (KaTeX parse error)
    debris               "Wait" scratch work, U+FFFD, '??' headers, raw markdown (** or '* ')
    spanish-label        Spanish headings/labels on English pages
    false-claim          "fully verified", "zero hallucinations", ... banners
    lab-reference        links to, or files of, laboratory pages (labs are not on the web)
    theme-key            localStorage theme key other than 'ae_theme'
    badge-drift          index.html badge counts that differ from the pages on disk

Badge contract (index.html): <article data-subject="SLUG"> ... <a href=".../teoria|problemas/...">
    <span class="area-badge ...">N topics / N prob.</span></a>

Usage:
    python tools/audit_portal.py [-v] [--json] [--only a,b] [--skip a,b] [--quiet]
Exit code 1 when any error finding remains.
"""
import argparse
import collections
import dataclasses
import html
import json
import os
import pathlib
import re
import sys
from urllib.parse import unquote

CHECKS = (
    "broken-link", "missing-backlink", "katex-parity", "katex-text-ampersand", "debris",
    "spanish-label", "false-claim", "lab-reference", "theme-key", "badge-drift",
)


@dataclasses.dataclass(frozen=True)
class Finding:
    check: str
    severity: str
    file: str
    line: int
    message: str


# --------------------------------------------------------------------------- text helpers
def _blank(m):
    return re.sub(r"[^\n]", " ", m.group(0))


_COMMENT = re.compile(r"<!--.*?-->", re.S)
_SCRIPT = re.compile(r"(<script\b[^>]*>)(.*?)(</script>)", re.S | re.I)
_STYLE = re.compile(r"(<style\b[^>]*>)(.*?)(</style>)", re.S | re.I)
_TAG = re.compile(r"<[^>]+>")


def strip_comments(text):
    return _COMMENT.sub(_blank, text)


def blank_code_blocks(text):
    """Blank the *contents* of <script>/<style> (tags and attributes stay, so src= still counts)."""
    keep = lambda m: m.group(1) + re.sub(r"[^\n]", " ", m.group(2)) + m.group(3)  # noqa: E731
    return _STYLE.sub(keep, _SCRIPT.sub(keep, text))


def text_only(visible):
    return _TAG.sub(_blank, visible)


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


# --------------------------------------------------------------------------- link helpers
_LINK = re.compile(r"""\b(?:href|src)\s*=\s*["']([^"']*)["']""", re.I)
_EXTERNAL = re.compile(r"^(?:[a-zA-Z][a-zA-Z0-9+.\-]*:|//|#)")


def local_target(href):
    href = href.strip()
    if not href or _EXTERNAL.match(href):
        return None
    return unquote(re.split(r"[?#]", href)[0]) or None


class FileIndex:
    """Case-sensitive existence checks (Windows is case-insensitive, GitHub Pages is not)."""

    def __init__(self, root):
        self.root = os.path.abspath(root)
        self._ls = {}

    def _names(self, directory):
        if directory not in self._ls:
            try:
                self._ls[directory] = set(os.listdir(directory))
            except OSError:
                self._ls[directory] = set()
        return self._ls[directory]

    def exists(self, abs_path):
        rel = os.path.relpath(abs_path, self.root)
        if rel.startswith(".."):
            return os.path.exists(abs_path)
        cur = self.root
        for part in pathlib.PurePath(rel).parts:
            if part == ".":
                continue
            if part not in self._names(cur):
                return False
            cur = os.path.join(cur, part)
        return True

    def resolve(self, page_dir, target):
        """Return the existing absolute path a link points to, or None."""
        path = os.path.normpath(os.path.join(page_dir, target))
        if self.exists(path):
            if os.path.isdir(path):
                index = os.path.join(path, "index.html")
                return index if self.exists(index) else None
            return path
        return None


# --------------------------------------------------------------------------- per-file checks
def check_links(rel, no_comments, visible, page_dir, files):
    out = []
    for m in _LINK.finditer(visible):
        target = local_target(m.group(1))
        if target is None:
            continue
        if files.resolve(page_dir, target) is None:
            out.append(Finding("broken-link", "error", rel, line_of(visible, m.start()),
                               f"unresolved local link: {m.group(1)}"))
    return out


def check_backlink(rel, visible, page_dir, files):
    hub = os.path.normcase(os.path.join(files.root, "index.html"))
    for m in _LINK.finditer(visible):
        target = local_target(m.group(1))
        if target and files.resolve(page_dir, target):
            if os.path.normcase(files.resolve(page_dir, target)) == hub:
                return []
    return [Finding("missing-backlink", "error", rel, 1, "no link resolving to the root index.html")]


def check_katex(rel, visible):
    out = []
    doubles = visible.count("$$")
    if doubles % 2:
        out.append(Finding("katex-parity", "error", rel, 1, f"odd number of $$ delimiters ({doubles})"))
    singles = len(re.findall(r"(?<!\\)\$", visible.replace("$$", "")))
    if singles % 2:
        out.append(Finding("katex-parity", "error", rel, 1, f"odd number of $ delimiters ({singles})"))
    decoded = html.unescape(visible)
    for m in re.finditer(r"\\text\{([^{}]*)\}", decoded):
        if re.search(r"(?<!\\)&", m.group(1)):
            out.append(Finding("katex-text-ampersand", "error", rel, line_of(decoded, m.start()),
                               f"unescaped '&' inside \\text: {m.group(0)[:50]}"))
    return out


_DEBRIS_TEXT = (
    (re.compile(r"\bWait\b"), "scratch work ('Wait')"),
    (re.compile(r"\*\*"), "raw markdown bold '**'"),
    (re.compile(r"(?m)^\s*\* \S"), "raw markdown bullet '* '"),
)
_SPANISH = re.compile(r"\b(?:enunciado|soluci[oó]n|resoluci[oó]n|paso a paso)\b", re.I)
_CLAIM = re.compile(r"(?:fully|completely|100\s*%)\s+verified|zero[\s-]+hallucinations?|hallucinations?[\s-]+free", re.I)


def check_text(rel, no_comments, visible, text):
    out = []
    for m in re.finditer("\ufffd", no_comments):
        out.append(Finding("debris", "error", rel, line_of(no_comments, m.start()), "U+FFFD replacement character"))
    for m in re.finditer(r">\s*\?{1,2}\s+[A-Za-z]", visible):
        out.append(Finding("debris", "error", rel, line_of(visible, m.start()), "'?'-prefixed header (lost emoji)"))
    seen = set()
    for pattern, label in _DEBRIS_TEXT:
        for m in pattern.finditer(text):
            key = (label, line_of(text, m.start()))
            if key not in seen:  # one finding per kind per line
                seen.add(key)
                out.append(Finding("debris", "error", rel, key[1], label))
    for m in _SPANISH.finditer(text):
        out.append(Finding("spanish-label", "error", rel, line_of(text, m.start()), f"Spanish label '{m.group(0)}'"))
    for m in _CLAIM.finditer(text):
        out.append(Finding("false-claim", "error", rel, line_of(text, m.start()), f"unverifiable claim '{m.group(0)}'"))
    return out


_LAB_SEGMENT = re.compile(r"(?:^|/)(?:laborator[^/]*|lab-\d+[^/]*)(?:/|$)", re.I)
_STORAGE = re.compile(r"""localStorage\s*\.\s*(?:getItem|setItem|removeItem)\s*\(\s*(['"])([^'"]+)\1""")


def check_labs_and_theme(rel, no_comments, visible):
    out = []
    for m in _LINK.finditer(visible):
        target = local_target(m.group(1))
        if target and _LAB_SEGMENT.search(target):
            out.append(Finding("lab-reference", "error", rel, line_of(visible, m.start()),
                               f"link to laboratory page: {m.group(1)}"))
    for m in _STORAGE.finditer(no_comments):
        key = m.group(2)
        if "theme" in key.lower() and key != "ae_theme":
            out.append(Finding("theme-key", "error", rel, line_of(no_comments, m.start()),
                               f"localStorage key '{key}' (only 'ae_theme' is allowed)"))
    return out


# --------------------------------------------------------------------------- site-level checks
def check_lab_files(root, subject_files):
    out = []
    for path in subject_files:
        parts = path.relative_to(root).parts
        if any(p.lower().startswith("laborator") for p in parts[:-1]) or re.match(r"lab-\d", parts[-1], re.I):
            out.append(Finding("lab-reference", "error", path.relative_to(root).as_posix(), 1,
                               "laboratory page exists in the web tree"))
    return out


PROBLEM_MARKERS = ("problem-card", "problem-box")  # per-problem container classes used by the pages


def _problem_count(page_text):
    tokens = [t for cls in re.findall(r'class\s*=\s*"([^"]*)"', page_text) for t in cls.split()]
    for marker in PROBLEM_MARKERS:
        if marker in tokens:
            return tokens.count(marker)
    return 0


def _area_facts(root, slug, area):
    directory = root / "subjects" / slug / area
    if not directory.is_dir():
        return None
    topics, problems = set(), 0
    for page in directory.glob("*.html"):
        m = re.match(r"topic-(\d+)", page.name)
        if m:
            topics.add(int(m.group(1)))
        if area == "problemas" and page.name != "index.html":
            problems += _problem_count(page.read_text(encoding="utf-8", errors="replace"))
    return len(topics), problems


_ARTICLE = re.compile(r'<article\b[^>]*data-subject="([^"]+)"[^>]*>(.*?)</article>', re.S)
_ANCHOR = re.compile(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>', re.S)
_BADGE = re.compile(r'class="area-badge[^"]*"[^>]*>([^<]*)<')


def check_badges(root):
    index = root / "index.html"
    if not index.is_file():
        return []
    text = strip_comments(index.read_text(encoding="utf-8", errors="replace"))
    out = []
    for article in _ARTICLE.finditer(text):
        slug = article.group(1)
        for anchor in _ANCHOR.finditer(article.group(2)):
            href = anchor.group(1)
            area = "teoria" if "/teoria/" in href else "problemas" if "/problemas/" in href else None
            badge = _BADGE.search(anchor.group(2))
            if not area or not badge:
                continue
            facts = _area_facts(root, slug, area)
            if facts is None:
                continue
            topics, problems = facts
            label = badge.group(1)
            line = line_of(text, article.start() + article.group(0).find(label))
            claimed = re.search(r"(\d+)\s*(?:of\s*\d+\s*)?(?:topics?|units?)\b", label)
            if claimed and int(claimed.group(1)) != topics:
                out.append(Finding("badge-drift", "error", "index.html", line,
                                   f"{slug}/{area}: badge says {claimed.group(1)} topics, pages on disk cover {topics}"))
            claimed = re.search(r"(\d+)\s*prob", label)
            if claimed and area == "problemas" and int(claimed.group(1)) != problems:
                out.append(Finding("badge-drift", "error", "index.html", line,
                                   f"{slug}/{area}: badge says {claimed.group(1)} problems, pages on disk contain {problems}"))
    return out


# --------------------------------------------------------------------------- driver
def audit(root):
    root = pathlib.Path(root)
    files = FileIndex(root)
    subject_files = sorted(p for p in (root / "subjects").rglob("*") if p.is_file()) if (root / "subjects").is_dir() else []
    pages = ([root / "index.html"] if (root / "index.html").is_file() else []) + \
            [p for p in subject_files if p.suffix.lower() == ".html"]

    findings = []
    for page in pages:
        rel = page.relative_to(root).as_posix()
        raw = page.read_text(encoding="utf-8", errors="replace")
        no_comments = strip_comments(raw)
        visible = blank_code_blocks(no_comments)
        text = text_only(visible)
        page_dir = str(page.parent)
        findings += check_links(rel, no_comments, visible, page_dir, files)
        if rel.startswith("subjects/"):
            findings += check_backlink(rel, visible, page_dir, files)
        findings += check_katex(rel, visible)
        findings += check_text(rel, no_comments, visible, text)
        findings += check_labs_and_theme(rel, no_comments, visible)
    findings += check_lab_files(root, subject_files)
    findings += check_badges(root)
    return sorted(findings, key=lambda f: (f.check, f.file, f.line))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=pathlib.Path(__file__).resolve().parents[1], type=pathlib.Path)
    ap.add_argument("-v", "--verbose", action="store_true", help="list every finding")
    ap.add_argument("--json", action="store_true", help="emit findings as JSON")
    ap.add_argument("--only", default="", help="comma-separated checks to run")
    ap.add_argument("--skip", default="", help="comma-separated checks to skip")
    ap.add_argument("--quiet", action="store_true", help="print nothing; use the exit code")
    args = ap.parse_args(argv)

    only = {c for c in args.only.split(",") if c}
    skip = {c for c in args.skip.split(",") if c}
    unknown = (only | skip) - set(CHECKS)
    if unknown:
        ap.error(f"unknown check(s): {', '.join(sorted(unknown))}")
    findings = [f for f in audit(args.root) if (not only or f.check in only) and f.check not in skip]
    errors = [f for f in findings if f.severity == "error"]

    if not args.quiet:
        if args.json:
            print(json.dumps([dataclasses.asdict(f) for f in findings], indent=2, ensure_ascii=False))
        else:
            by_check = collections.defaultdict(list)
            for f in findings:
                by_check[f.check].append(f)
            print(f"{'check':22} {'findings':>8} {'files':>6}")
            for check in CHECKS:
                group = by_check.get(check, [])
                if group or (not only or check in only) and check not in skip:
                    print(f"{check:22} {len(group):8} {len({f.file for f in group}):6}")
            if args.verbose:
                print()
                for f in findings:
                    print(f"{f.file}:{f.line}: [{f.check}] {f.message}")
            print(f"\n{len(errors)} error(s) in {len({f.file for f in errors})} file(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
