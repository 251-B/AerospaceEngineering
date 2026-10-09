#!/usr/bin/env python3
"""Render pages in headless Edge/Chrome and count KaTeX formulas and KaTeX errors.

Unlike audit_portal's delimiter-parity check, this runs the real KaTeX auto-render
(loaded from the CDN by each page), so it catches unsupported macros and bad syntax.

    python tools/render_check.py subjects/advanced-maths/problemas/topic-2-problems.html ...
    python tools/render_check.py --all            # every subjects/**/*.html plus index.html

Exit code 1 if any page has KaTeX errors, leftover raw $$ delimiters or fails to render.
"""
from __future__ import annotations

import argparse
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field

REPO = pathlib.Path(__file__).resolve().parent.parent
CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
]


def find_browser() -> str | None:
    for name in ("msedge", "chrome", "google-chrome", "chromium"):
        found = shutil.which(name)
        if found:
            return found
    return next((c for c in CANDIDATES if os.path.exists(c)), None)


@dataclass
class RenderResult:
    path: str
    formulas: int = 0
    display: int = 0
    errors: list[str] = field(default_factory=list)
    leftover: int = 0
    dom_kb: int = 0

    @property
    def ok(self) -> bool:
        return not self.errors and self.leftover == 0 and self.dom_kb > 0


def analyse_dom(path: str, dom: str) -> RenderResult:
    """Pure function: count KaTeX output in a serialised DOM."""
    body = re.sub(r"<script.*?</script>", "", dom, flags=re.S)
    return RenderResult(
        path=path,
        formulas=len(re.findall(r'class="katex"', dom)),
        display=len(re.findall(r'class="katex-display"', dom)),
        errors=re.findall(r'class="katex-error"[^>]*title="([^"]{0,160})', dom),
        leftover=len(re.findall(r"\$\$", body)),
        dom_kb=len(dom) // 1024,
    )


def dump_dom(browser: str, page: pathlib.Path, budget_ms: int = 20000) -> str:
    with tempfile.TemporaryDirectory() as profile:
        proc = subprocess.run(
            [browser, "--headless=new", "--disable-gpu", "--no-first-run", f"--user-data-dir={profile}",
             "--allow-file-access-from-files", f"--virtual-time-budget={budget_ms}", "--dump-dom", page.as_uri()],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120,
        )
    return proc.stdout


def check(paths: list[pathlib.Path], browser: str, repo: pathlib.Path = REPO) -> list[RenderResult]:
    results = []
    for p in paths:
        p = p if p.is_absolute() else repo / p
        try:
            rel = p.relative_to(repo).as_posix()
        except ValueError:
            rel = str(p)
        results.append(analyse_dom(rel, dump_dom(browser, p)))
    return results


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pages", nargs="*", help="HTML files, relative to the repo root or absolute")
    ap.add_argument("--all", action="store_true", help="check index.html and every subjects/**/*.html")
    args = ap.parse_args(argv)
    browser = find_browser()
    if not browser:
        print("render_check: no Chromium-based browser found", file=sys.stderr)
        return 2
    pages = [pathlib.Path(p) for p in args.pages]
    if args.all:
        pages += [REPO / "index.html"] + sorted((REPO / "subjects").rglob("*.html"))
    if not pages:
        ap.error("give at least one page or --all")
    bad = 0
    for r in check(pages, browser):
        status = "ok " if r.ok else "BAD"
        print(f"{status} {r.path}: katex={r.formulas} display={r.display} errors={len(r.errors)} "
              f"leftover-$$={r.leftover} dom={r.dom_kb}KB")
        for e in r.errors[:5]:
            print("    ERR:", e)
        bad += not r.ok
    print(f"{len(pages) - bad}/{len(pages)} pages clean")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
