#!/usr/bin/env python3
"""Render PNG previews of the Midterm 2 bank figures, to inspect them before committing (no label on a line).

    python tools/materials_bank/preview_figures.py OUT_DIR [name ...]     # all figures when no name is given

Needs a Chromium/Chrome binary (render_check.find_browser, or /opt/pw-browsers/chromium*).
"""
import glob
import pathlib
import subprocess
import sys

TOOLS = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from figures import materials_mt2 as fig  # noqa: E402
from figures.svgkit import FIXED  # noqa: E402
import render_check  # noqa: E402


def browser():
    found = render_check.find_browser()
    if found:
        return found
    hits = sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome")) or \
        sorted(glob.glob("/opt/pw-browsers/chromium*/chrome-linux*/headless_shell"))
    return hits[-1] if hits else None


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    out = pathlib.Path(argv[0])
    out.mkdir(parents=True, exist_ok=True)
    fig.build()
    names = argv[1:] or sorted(fig.FIGURES)
    exe = browser()
    if not exe:
        print("no browser found")
        return 1
    for name in names:
        svg = fig.REG.files[f"vault/attachments/MAT-MT2/{name}.svg"]
        page = out / f"{name}.html"
        page.write_text(f'<body style="margin:12px;background:#fff;width:760px">{svg}</body>', encoding="utf-8")
        png = out / f"{name}.png"
        subprocess.run([exe, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--window-size=790,620",
                        f"--screenshot={png}", page.as_uri()], check=False, capture_output=True, timeout=60)
        page.unlink()
        print(png if png.exists() else f"FAILED {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
