"""Build step for Cloudflare Pages (see docs/private-hosting.md).

    Build command:           python tools/cloudflare/build_site.py
    Build output directory:  _site

Cloudflare Pages refuses any file larger than 25 MiB, so a deployment of the whole repository
fails. This copies the site into _site/ leaving out .git, local scratch folders and every file
over the limit, and prints the files it left out (shrink them to bring them back).
Standard library only.
"""
import os
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / '_site'
LIMIT = 25 * 1024 * 1024
SKIP_DIRS = {'.git', '_site', 'node_modules', '__pycache__', 'graphify-out', '.obsidian', '.wrangler'}
SKIP_PATHS = {'tools/invites/out'}


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    copied, skipped = 0, []
    for folder, dirs, files in os.walk(ROOT):
        rel = pathlib.Path(folder).relative_to(ROOT)
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and (rel / d).as_posix() not in SKIP_PATHS]
        for name in files:
            src = pathlib.Path(folder) / name
            size = src.stat().st_size
            if size > LIMIT:
                skipped.append(((rel / name).as_posix(), size))
                continue
            dst = OUT / rel / name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            copied += 1
    print(f'build_site: {copied} files copied to _site/')
    for path, size in skipped:
        print(f'  left out (over 25 MiB, {size / 1048576:.1f} MiB): {path}')
    if copied > 20000:
        sys.exit('build_site: more than 20,000 files, the Cloudflare Pages limit')


if __name__ == '__main__':
    main()
