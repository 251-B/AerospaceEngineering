#!/usr/bin/env python3
"""Print every theory and problem page to A4 PDFs for the "Download PDF" / "Open as PDF" buttons.

For each subjects/<slug>/{teoria,problemas}/<page>.html (not index.html) it writes
    assets/pdf/<slug>/<area>/<page>.pdf              the whole page (all problems on problem pages)
    assets/pdf/<slug>/<area>/<page>/<card id>.pdf    each problem card on its own
using headless Edge/Chrome (the same browser as tools/render_check.py) and the print layout of
assets/css/print.css, prepared by assets/js/pdf-export.js (?print=all or ?print=<card id>).

assets/pdf/manifest.json stores a hash of each PDF's inputs (the page, print.css, pdf-export.js),
so only the PDFs whose page changed are printed again, and --check needs no browser.

    python tools/build_pdfs.py                    # print new or stale PDFs, remove orphans
    python tools/build_pdfs.py --check            # exit 1 if a PDF is missing, stale or orphaned
    python tools/build_pdfs.py --only fluid       # restrict to pages whose path contains "fluid"
    python tools/build_pdfs.py --force            # print everything again
    python tools/build_pdfs.py --katex DIR        # use a local KaTeX dist/ folder instead of the CDN
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import render_check  # noqa: E402

REPO = pathlib.Path(__file__).resolve().parent.parent
OUT = "assets/pdf"
MANIFEST = OUT + "/manifest.json"
INPUTS = ("assets/css/print.css", "assets/js/pdf-export.js")
VERSION = "1"
_CARD = re.compile(r'<(?:article|div|section|details)\b[^>]*class="[^"]*\b(?:problem-card|problem-box)\b[^"]*"[^>]*>')
_ID = re.compile(r'\bid="([^"]+)"')
_KATEX_CDN = re.compile(r"https://cdn\.jsdelivr\.net/npm/katex@[0-9.]+/dist/")


def pages(root: pathlib.Path) -> list[pathlib.Path]:
    out = []
    for area in ("teoria", "problemas"):
        out += sorted(p for p in root.glob(f"subjects/*/{area}/*.html") if p.name != "index.html")
    return out


def card_ids(text: str) -> list[str]:
    ids = []
    for m in _CARD.finditer(text):
        i = _ID.search(m.group(0))
        if i and i.group(1) not in ids:
            ids.append(i.group(1))
    return ids


def targets(root: pathlib.Path) -> dict[str, tuple[pathlib.Path, str, str]]:
    """{pdf path: (page, print mode, input hash)} for every PDF the portal links to."""
    shared = b"".join((root / f).read_bytes() for f in INPUTS) + VERSION.encode()
    out = {}
    for page in pages(root):
        rel = page.relative_to(root)
        slug, area, stem = rel.parts[1], rel.parts[2], page.stem
        text = page.read_text(encoding="utf-8")
        base = f"{OUT}/{slug}/{area}/{stem}"
        h = hashlib.sha256(page.read_bytes() + shared)
        out[base + ".pdf"] = (page, "all", h.hexdigest())
        if area == "problemas":
            for cid in card_ids(text):
                out[f"{base}/{cid}.pdf"] = (page, cid, hashlib.sha256(h.digest() + cid.encode()).hexdigest())
    return out


def load_manifest(root: pathlib.Path) -> dict[str, str]:
    p = root / MANIFEST
    return json.loads(p.read_text(encoding="utf-8")).get("pdfs", {}) if p.is_file() else {}


def stale(root: pathlib.Path) -> tuple[list[str], list[str]]:
    """(PDFs to print, orphans to remove)."""
    want, have = targets(root), load_manifest(root)
    todo = [p for p, (_, _, h) in want.items() if have.get(p) != h or not (root / p).is_file()]
    on_disk = {p.relative_to(root).as_posix() for p in (root / OUT).rglob("*.pdf")} if (root / OUT).is_dir() else set()
    orphans = sorted((set(have) | on_disk) - set(want))
    return sorted(todo), orphans


def _mirror(root: pathlib.Path, katex: pathlib.Path, tmp: pathlib.Path) -> pathlib.Path:
    """A copy of the pages and assets whose KaTeX URLs point at a local folder (no CDN needed)."""
    shutil.copytree(root / "assets", tmp / "assets", ignore=shutil.ignore_patterns("pdf"))
    kx = katex.resolve().as_uri() + "/"
    for page in pages(root):
        out = tmp / page.relative_to(root)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(_KATEX_CDN.sub(kx, page.read_text(encoding="utf-8")), encoding="utf-8")
    return tmp


def print_pdf(browser: str, url: str, out: pathlib.Path, budget_ms: int = 25000) -> bool:
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as profile:
        proc = subprocess.run(
            [browser, "--headless=new", "--disable-gpu", "--no-first-run", f"--user-data-dir={profile}",
             "--allow-file-access-from-files", "--run-all-compositor-stages-before-draw",
             f"--virtual-time-budget={budget_ms}", "--no-pdf-header-footer", "--print-to-pdf-no-header",
             f"--print-to-pdf={out}", url],
            capture_output=True, text=True, timeout=240)
    return proc.returncode == 0 and out.is_file() and out.stat().st_size > 1000


def build(root: pathlib.Path, browser: str, katex: pathlib.Path | None, only: str, force: bool, jobs: int) -> int:
    want = targets(root)
    todo, orphans = stale(root)
    if force:
        todo = sorted(want)
    todo = [p for p in todo if only in want[p][0].relative_to(root).as_posix()]
    manifest = load_manifest(root)
    for p in orphans:
        (root / p).unlink(missing_ok=True)
        manifest.pop(p, None)
        print("removed", p)
    failed = 0
    with tempfile.TemporaryDirectory() as tmp:
        src = _mirror(root, katex, pathlib.Path(tmp)) if katex else root

        def job(pdf: str):
            page, mode, h = want[pdf]
            url = (src / page.relative_to(root)).as_uri() + "?print=" + mode
            return pdf, h, print_pdf(browser, url, root / pdf)

        with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, jobs)) as pool:
            for pdf, h, ok in pool.map(job, todo):
                if ok:
                    manifest[pdf] = h
                    print("wrote", pdf)
                else:
                    failed += 1
                    print("FAILED", pdf, file=sys.stderr)
    (root / OUT).mkdir(parents=True, exist_ok=True)
    (root / MANIFEST).write_text(json.dumps({"_comment": "Generated by tools/build_pdfs.py; do not edit.",
                                             "pdfs": dict(sorted(manifest.items()))}, indent=1) + "\n",
                                 encoding="utf-8")
    print(f"build_pdfs: {len(todo) - failed} printed, {failed} failed, {len(orphans)} removed, {len(want)} in total")
    return 1 if failed else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="fail if a PDF is missing, stale or orphaned")
    ap.add_argument("--only", default="", help="only pages whose path contains this text")
    ap.add_argument("--force", action="store_true", help="print every PDF again")
    ap.add_argument("--katex", type=pathlib.Path, help="local KaTeX dist/ folder to use instead of the CDN")
    ap.add_argument("--jobs", type=int, default=4, help="browsers in parallel (default 4)")
    ap.add_argument("--root", type=pathlib.Path, default=REPO)
    args = ap.parse_args(argv)
    root = args.root.resolve()
    if args.check:
        todo, orphans = stale(root)
        for p in todo:
            print("stale", p)
        for p in orphans:
            print("orphan", p)
        if todo or orphans:
            print(f"build_pdfs: {len(todo)} stale, {len(orphans)} orphaned (run python tools/build_pdfs.py)")
            return 1
        print(f"build_pdfs: {len(targets(root))} PDFs up to date")
        return 0
    browser = render_check.find_browser()
    if not browser:
        print("build_pdfs: no Edge/Chrome found", file=sys.stderr)
        return 2
    return build(root, browser, args.katex, args.only, args.force, args.jobs)


if __name__ == "__main__":
    sys.exit(main())
