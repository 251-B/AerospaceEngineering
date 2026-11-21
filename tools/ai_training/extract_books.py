#!/usr/bin/env python3
"""Extract the reference textbooks in sources/libros/ into a training corpus for Sideris.

The PDFs themselves are NOT tracked by git (copyrighted, public repo). Only the manifest
sources/libros/libros.json is tracked; each collaborator keeps the PDFs locally.

Output (tools/ai_training/out/, also untracked):
  books_cpt.jsonl   one record per chunk: {"text", "book_id", "subject", "title", "lang", "pages"}
                    -> used by `train_sideris.py --stage cpt` (continued pre-training, before SFT)
  books_report.json per-book stats (pages, extracted words, pages with no text layer)

Usage:
    python tools/ai_training/extract_books.py                 # all books in the manifest
    python tools/ai_training/extract_books.py --subject 02-aerospace-materials-1
    python tools/ai_training/extract_books.py --manifest-only # rebuild libros.json from the folder
"""
import argparse
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]
BOOKS = REPO / "sources" / "libros"
MANIFEST = BOOKS / "libros.json"
OUT = REPO / "tools" / "ai_training" / "out"

SUBJECTS = {
    "01-fluid-mechanics": "fluid-mechanics",
    "02-aerospace-materials-1": "aerospace-materials-1",
    "03-engineering-mechanics": "engineering-mechanics",
    "04-advanced-maths": "advanced-maths",
    "05-business-management": "business-management",
}

_SPANISH_HINTS = ("Introducción", "Mecánica", "Ciencia de Materiales")
_HYPHEN_BREAK = re.compile(r"(\w)-\n(\w)")
_MULTI_NL = re.compile(r"\n{3,}")
_SPACES = re.compile(r"[ \t ]+")


def slugify(name):
    s = re.sub(r"[^\w]+", "-", name.lower(), flags=re.ASCII).strip("-")
    return re.sub(r"-{2,}", "-", s)[:80]


def build_manifest():
    """Scan sources/libros/<subject>/[adicional/]*.pdf and (re)write libros.json, keeping manual fields."""
    old = {}
    if MANIFEST.exists():
        old = {b["file"]: b for b in json.loads(MANIFEST.read_text(encoding="utf-8"))["books"]}
    books = []
    for subj_dir in sorted(p for p in BOOKS.iterdir() if p.is_dir()):
        for pdf in sorted(subj_dir.rglob("*.pdf")):
            rel = pdf.relative_to(BOOKS).as_posix()
            stem = pdf.stem
            entry = {
                "id": slugify(stem),
                "file": rel,
                "subject": subj_dir.name,
                "role": "adicional" if "/adicional/" in f"/{rel}" else "principal",
                "citation": stem,
                "lang": "es" if any(h in stem for h in _SPANISH_HINTS) else "en",
                "size_mb": round(pdf.stat().st_size / 1048576, 1),
                "use_for_training": True,
            }
            prev = old.get(rel, {})
            for keep in ("use_for_training", "lang", "page_range", "notes"):
                if keep in prev:
                    entry[keep] = prev[keep]
            books.append(entry)
    data = {
        "_comment": "Reference textbooks (PDFs untracked: see .gitignore). Rebuild with extract_books.py --manifest-only.",
        "books": books,
    }
    MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Manifest: {len(books)} books -> {MANIFEST.relative_to(REPO)}")
    return books


def clean(text):
    text = text.replace("\r", "")
    text = _HYPHEN_BREAK.sub(r"\1\2", text)
    text = _SPACES.sub(" ", text)
    text = "\n".join(line.strip() for line in text.split("\n"))
    return _MULTI_NL.sub("\n\n", text).strip()


def extract_book(entry, chunk_words, overlap):
    import pymupdf  # PyMuPDF

    path = BOOKS / entry["file"]
    doc = pymupdf.open(path)
    first, last = entry.get("page_range", [1, doc.page_count])
    pages, empty = [], 0
    for i in range(first - 1, min(last, doc.page_count)):
        t = clean(doc[i].get_text("text"))
        if len(t.split()) < 25:  # cover, blank, figure-only or scanned page without text layer
            empty += 1
            continue
        pages.append((i + 1, t))
    doc.close()

    chunks, buf, buf_pages = [], [], []
    for pno, t in pages:
        buf.extend(t.split(" "))
        buf_pages.append(pno)
        while len(buf) >= chunk_words:
            chunks.append((" ".join(buf[:chunk_words]), buf_pages[0], buf_pages[-1]))
            buf = buf[chunk_words - overlap:]
            buf_pages = buf_pages[-1:]
    if len(buf) > chunk_words // 4:
        chunks.append((" ".join(buf), buf_pages[0], buf_pages[-1]))

    records = [
        {
            "text": f"{entry['citation']}\n\n{txt}",
            "book_id": entry["id"],
            "subject": SUBJECTS.get(entry["subject"], entry["subject"]),
            "title": entry["citation"],
            "lang": entry["lang"],
            "pages": [a, b],
        }
        for txt, a, b in chunks
    ]
    words = sum(len(t.split()) for _, t in pages)
    stats = {"pages_with_text": len(pages), "pages_skipped": empty, "words": words, "chunks": len(records)}
    if pages and empty > len(pages):
        stats["warning"] = "most pages have no text layer (scanned?) - needs OCR"
    elif not pages:
        stats["warning"] = "no text extracted - scanned PDF, needs OCR"
    return records, stats


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--subject", help="Only books of this subject folder (e.g. 01-fluid-mechanics).")
    ap.add_argument("--chunk-words", type=int, default=900, help="~1.2k tokens per chunk.")
    ap.add_argument("--overlap", type=int, default=80)
    ap.add_argument("--manifest-only", action="store_true")
    ap.add_argument("--out", default=str(OUT))
    args = ap.parse_args(argv)

    if not BOOKS.exists():
        sys.exit(f"{BOOKS} not found: copy the PDFs there first (see sources/libros/README.md).")
    books = build_manifest()
    if args.manifest_only:
        return

    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    report, total = {}, 0
    with open(out / "books_cpt.jsonl", "w", encoding="utf-8") as fh:
        for b in books:
            if not b.get("use_for_training", True) or (args.subject and b["subject"] != args.subject):
                continue
            if not (BOOKS / b["file"]).exists():
                report[b["id"]] = {"warning": "PDF missing locally"}
                continue
            try:
                recs, stats = extract_book(b, args.chunk_words, args.overlap)
            except Exception as e:  # corrupt / truncated PDF
                report[b["id"]] = {"error": str(e)}
                print(f"  ERROR {b['id']}: {e}")
                continue
            for r in recs:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
            total += len(recs)
            report[b["id"]] = stats
            flag = f"  <- {stats['warning']}" if "warning" in stats else ""
            print(f"  {b['id'][:60]:60s} {stats['words']:>8,} words {stats['chunks']:>5} chunks{flag}")
    (out / "books_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {total} chunks -> {out / 'books_cpt.jsonl'}")


if __name__ == "__main__":
    main()
