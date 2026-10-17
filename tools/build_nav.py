#!/usr/bin/env python3
"""Build the side-menu manifest consumed by the web portal.

Reads tools/nav.json (hand-written short labels) and checks it against the pages on disk, then
writes assets/data/nav.js (`window.AE_NAV = {...};`). assets/js/sidebar.js builds the menu from it,
so no page carries the tree. Laboratory material is never listed.

Usage:
    python tools/build_nav.py            # (re)write assets/data/nav.js
    python tools/build_nav.py --check    # exit 1 if the file is stale or nav.json and the pages disagree
"""
import argparse
import json
import pathlib
import sys

SRC_REL = pathlib.Path("tools", "nav.json")
OUT_REL = pathlib.Path("assets", "data", "nav.js")
AREAS = (("teoria", "Theory"), ("problemas", "Problems"), ("extra-problems", "Extra problems"))
EXTRAS = (("simulator", "Exam simulator"),
          ("sources", "Theory & exercise PDFs"), ("exams", "Exams"))


def _flatten(pages):
    for p in pages:
        yield p
        yield from _flatten(p.get("children", []))


def build_manifest(root):
    """Return (manifest, errors) for the repository at `root`."""
    root = pathlib.Path(root)
    spec = json.loads((root / SRC_REL).read_text(encoding="utf-8"))
    errors = []
    subjects = []
    for sub in spec["subjects"]:
        slug = sub["slug"]
        base = root / "subjects" / slug
        if not base.is_dir():
            errors.append(f"nav.json: subject folder subjects/{slug}/ does not exist")
            continue
        groups = []
        for area, title in AREAS:
            folder = base / area
            listed = {p["page"] for p in _flatten(sub.get(area, []))}
            on_disk = {f.name for f in folder.glob("*.html")} - {"index.html"} if folder.is_dir() else set()
            for name in sorted(listed - on_disk):
                errors.append(f"nav.json: subjects/{slug}/{area}/{name} is listed but does not exist")
            for name in sorted(on_disk - listed):
                errors.append(f"nav.json: subjects/{slug}/{area}/{name} exists but is not listed")

            def node(p, area=area):
                out = {"href": f"subjects/{slug}/{area}/{p['page']}", "label": p["label"]}
                if p.get("children"):
                    out["children"] = [node(c) for c in p["children"]]
                return out

            if (folder / "index.html").is_file():
                groups.append({
                    "id": area,
                    "label": title,
                    "href": f"subjects/{slug}/{area}/index.html",
                    "pages": [node(p) for p in sub.get(area, [])],
                })
        extras = [
            {"href": f"subjects/{slug}/{folder}/index.html", "label": label}
            for folder, label in EXTRAS
            if (base / folder / "index.html").is_file()
        ]
        subjects.append({"slug": slug, "name": sub["name"], "accent": sub["accent"], "groups": groups, "extras": extras})

    listed_slugs = {s["slug"] for s in spec["subjects"]}
    for d in sorted(p.name for p in (root / "subjects").iterdir() if p.is_dir()):
        if d not in listed_slugs:
            errors.append(f"nav.json: subjects/{d}/ exists but is not listed")
    return {"subjects": subjects}, errors


def render_js(manifest):
    payload = json.dumps(manifest, indent=2, ensure_ascii=False)
    return f"window.AE_NAV = {payload};\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=pathlib.Path(__file__).resolve().parents[1], type=pathlib.Path)
    ap.add_argument("--check", action="store_true", help="exit 1 if the generated file is stale")
    args = ap.parse_args(argv)

    manifest, errors = build_manifest(args.root)
    for e in errors:
        print("ERROR:", e)
    if errors:
        return 1
    rendered = render_js(manifest)
    out = args.root / OUT_REL
    n = sum(1 for s in manifest["subjects"] for g in s["groups"] for _ in _flatten(g["pages"]))

    if args.check:
        current = out.read_text(encoding="utf-8") if out.exists() else ""
        if current != rendered:
            print(f"STALE: {OUT_REL} does not match {SRC_REL} and the pages on disk. Run tools/build_nav.py")
            return 1
        print(f"OK: {OUT_REL} is up to date ({n} pages)")
        return 0

    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(rendered)
    print(f"Wrote {OUT_REL}: {n} pages across {len(manifest['subjects'])} subjects")
    return 0


if __name__ == "__main__":
    sys.exit(main())
