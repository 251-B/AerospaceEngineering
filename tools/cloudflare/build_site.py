"""Build step for Cloudflare Pages (see docs/private-hosting.md).

    Build command:           python tools/cloudflare/build_site.py
    Build output directory:  _site

Cloudflare Pages refuses any file larger than 25 MiB, so a deployment of the whole repository
fails. This copies the site into _site/ leaving out .git, local scratch folders and every file
over the limit, and prints the files it left out (shrink them to bring them back).

A PDF over the limit is not left out when PyMuPDF is installed (`pip install pymupdf`): its copy in
_site/ gets its images recompressed (200 dpi, then 150 dpi if still too big), so the Cloudflare site
keeps every PDF of GitHub Pages. The file in the repository is never changed. Without PyMuPDF the
script uses the standard library only and leaves such PDFs out, as before.
"""
import os
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / '_site'
LIMIT = 25 * 1024 * 1024
SKIP_DIRS = {'.git', '_site', 'node_modules', '__pycache__', 'graphify-out', '.obsidian', '.wrangler', 'sideris_out'}
SKIP_PATHS = {'tools/invites/out', 'tools/ai_training/out'}


def shrink_pdf(src, dst):
    """Write a copy of src with recompressed images; True when it fits under LIMIT."""
    try:
        import warnings
        warnings.filterwarnings('ignore', module='fitz')
        import pymupdf
    except ImportError:
        return False
    for dpi, quality in ((200, 80), (150, 75)):
        doc = pymupdf.open(src)
        doc.rewrite_images(dpi_threshold=dpi + 10, dpi_target=dpi, quality=quality, lossy=True,
                           lossless=True, bitonal=True, color=True, gray=True, set_to_gray=False)
        dst.parent.mkdir(parents=True, exist_ok=True)
        doc.save(dst, garbage=4, deflate=True, clean=True)
        doc.close()
        if dst.stat().st_size <= LIMIT:
            return True
    dst.unlink()
    return False


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    copied, skipped, shrunk = 0, [], []
    for folder, dirs, files in os.walk(ROOT):
        rel = pathlib.Path(folder).relative_to(ROOT)
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and (rel / d).as_posix() not in SKIP_PATHS]
        for name in files:
            src = pathlib.Path(folder) / name
            size = src.stat().st_size
            dst = OUT / rel / name
            if size > LIMIT:
                if name.lower().endswith('.pdf') and shrink_pdf(src, dst):
                    shrunk.append(((rel / name).as_posix(), size, dst.stat().st_size))
                    copied += 1
                else:
                    skipped.append(((rel / name).as_posix(), size))
                continue
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            copied += 1
    print(f'build_site: {copied} files copied to _site/')
    for path, size, new in shrunk:
        print(f'  recompressed (over 25 MiB, {size / 1048576:.1f} -> {new / 1048576:.1f} MiB): {path}')
    for path, size in skipped:
        print(f'  left out (over 25 MiB, {size / 1048576:.1f} MiB): {path}')
    if copied > 20000:
        sys.exit('build_site: more than 20,000 files, the Cloudflare Pages limit')


if __name__ == '__main__':
    main()
