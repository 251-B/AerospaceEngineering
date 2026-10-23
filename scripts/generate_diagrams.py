#!/usr/bin/env python3
"""Draw the technical sketches of the Engineering Mechanics Midterm 1 bank (--set m1, default) or the deduction
figures of the worked solutions of the official problems (--set sol, tools/figures/em_solutions.py).

Writes vault/attachments/EM-M1/<name>.svg or vault/attachments/EM-SOL/<name>.svg (fixed colours), reports labels that overlap or leave the canvas, and,
with --png, renders every SVG to a PNG preview (headless Edge or Chrome, 2x) in the scratch folder given by --out,
so each figure can be opened and inspected before it is accepted.

Usage:  python scripts/generate_diagrams.py [--set m1|sol] [--png --out DIR] [name ...]
"""
import argparse
import sys
import pathlib
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # warnings may contain Unicode minus signs
REPO = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))
from figures import em_midterm1, em_solutions  # noqa: E402

BROWSERS = [r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", r"C:\Program Files\Google\Chrome\Application\chrome.exe"]


def render_png(svg_path, png_path, w, h):
    exe = next((b for b in BROWSERS if pathlib.Path(b).is_file()), shutil.which("msedge") or shutil.which("chrome"))
    if not exe:
        return False
    html = png_path.with_suffix(".html")
    html.write_text('<!doctype html><body style="margin:0;background:#ffffff">' + svg_path.read_text(encoding="utf-8")
                    .replace('width="100%"', f'width="{w}"') + "</body>", encoding="utf-8")
    subprocess.run([exe, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={w},{h}",
                    "--force-device-scale-factor=2", f"--screenshot={png_path}", html.as_uri()],
                   check=False, capture_output=True, timeout=60)
    html.unlink(missing_ok=True)
    return png_path.is_file()


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("names", nargs="*")
    ap.add_argument("--png", action="store_true")
    ap.add_argument("--out", default=str(REPO / "scripts" / "_preview"))
    ap.add_argument("--set", choices=("m1", "sol"), default="m1")
    args = ap.parse_args(argv)
    em = em_solutions if args.set == "sol" else em_midterm1
    warnings = em.build()
    em.REG.write(REPO)
    bad = 0
    for name, (fn, _, _) in em.FIGURES.items():
        if args.names and name not in args.names:
            continue
        for w in warnings[name]:
            bad += 1
            print(f"WARNING {name}: {w}")
        if args.png:
            out = pathlib.Path(args.out)
            out.mkdir(parents=True, exist_ok=True)
            svg = REPO / "vault" / "attachments" / em.REG.folder / f"{name}.svg"
            sc = fn()
            ok = render_png(svg, out / f"{name}.png", sc.c.w, sc.c.h)
            print(("rendered " if ok else "NO RENDERER for ") + name)
    print(f"{len(em.FIGURES)} figures, {bad} warnings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
