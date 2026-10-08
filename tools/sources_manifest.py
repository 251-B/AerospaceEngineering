#!/usr/bin/env python3
"""Build the official-PDF manifest consumed by the web portal.

Scans sources/cuatrimestre-1/ and writes assets/data/sources.js
(`window.AE_SOURCES = {...};`). Laboratory material is never included.

Usage:
    python tools/sources_manifest.py            # (re)write assets/data/sources.js
    python tools/sources_manifest.py --check    # exit 1 if the file is stale
"""
import argparse
import json
import pathlib
import re
import sys
from urllib.parse import quote

BASE = ("sources", "cuatrimestre-1")
CATEGORIES = ("teoria", "slides", "problemas", "examenes", "schedule")
UNIT_RE = re.compile(r"^unit-(\d+)-(.+)$")
OUT_REL = pathlib.Path("assets", "data", "sources.js")


def _natural_key(text):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", text)]


def _is_excluded(parts):
    return any(p.lower().startswith("laborator") or p.lower().startswith("extracted") for p in parts)


def _empty_bucket(categories):
    bucket = {c: [] for c in categories}
    bucket["other"] = []
    return bucket


def _item(path, subject_folder, parts):
    segments = [*BASE, subject_folder, *parts]
    return {
        "name": parts[-1],
        "href": "/".join(quote(s, safe="") for s in segments),
        "bytes": path.stat().st_size,
    }


def _unit_record(folder):
    m = UNIT_RE.match(folder)
    return {
        "id": folder,
        "number": int(m.group(1)),
        "title": m.group(2).replace("-", " ").title(),
        **_empty_bucket(("teoria", "slides", "problemas")),
    }


def build_manifest(root):
    """Return the manifest dict for the repository at `root`."""
    sources = pathlib.Path(root, *BASE)
    subjects = {}
    for subject_dir in sorted(p for p in sources.iterdir() if p.is_dir()):
        key = re.sub(r"^\d+-", "", subject_dir.name)
        units = {}
        for d in subject_dir.iterdir():
            if d.is_dir() and UNIT_RE.match(d.name) and not _is_excluded([d.name]):
                units[d.name] = _unit_record(d.name)
        general = _empty_bucket(CATEGORIES)

        pdfs = [p for p in subject_dir.rglob("*") if p.is_file() and p.suffix.lower() == ".pdf"]
        for pdf in sorted(pdfs, key=lambda p: _natural_key(p.relative_to(subject_dir).as_posix())):
            parts = pdf.relative_to(subject_dir).parts
            if _is_excluded(parts):
                continue
            item = _item(pdf, subject_dir.name, parts)
            if UNIT_RE.match(parts[0]):
                unit = units[parts[0]]
                category = parts[1] if len(parts) > 2 and parts[1] in unit else "other"
                unit[category].append(item)
            else:
                category = parts[0] if len(parts) > 1 and parts[0] in general else "other"
                general[category].append(item)

        subjects[key] = {
            "folder": subject_dir.name,
            "general": general,
            "units": sorted(units.values(), key=lambda u: u["number"]),
        }
    return {"base": "/".join(BASE), "subjects": subjects}


def iter_items(manifest):
    """Flatten every file record in the manifest."""
    items = []
    for subject in manifest["subjects"].values():
        for bucket in subject["general"].values():
            items.extend(bucket)
        for unit in subject["units"]:
            for key, bucket in unit.items():
                if isinstance(bucket, list):
                    items.extend(bucket)
    return items


def render_js(manifest):
    payload = json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False)
    return f"window.AE_SOURCES = {payload};\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=pathlib.Path(__file__).resolve().parents[1], type=pathlib.Path)
    ap.add_argument("--check", action="store_true", help="exit 1 if the generated file is stale")
    args = ap.parse_args(argv)

    manifest = build_manifest(args.root)
    rendered = render_js(manifest)
    out = args.root / OUT_REL
    n = len(iter_items(manifest))

    if args.check:
        current = out.read_text(encoding="utf-8") if out.exists() else ""
        if current != rendered:
            print(f"STALE: {OUT_REL} does not match sources/ ({n} PDFs). Run tools/sources_manifest.py")
            return 1
        print(f"OK: {OUT_REL} is up to date ({n} PDFs)")
        return 0

    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(rendered)
    print(f"Wrote {OUT_REL}: {n} PDFs across {len(manifest['subjects'])} subjects")
    return 0


if __name__ == "__main__":
    sys.exit(main())
