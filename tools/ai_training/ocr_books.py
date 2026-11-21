#!/usr/bin/env python3
"""OCR the scanned reference textbooks of sources/libros/ (pages without a text layer).

Uses RapidOCR (ONNX Runtime, CPU, no external binary). Results are cached page by page in
sources/libros/.ocr/<book_id>.jsonl ({"p": page_number, "t": text}); the cache is git-ignored
(book-derived text) and the run is resumable: pages already in the cache are skipped.
extract_books.py then takes the OCR text for every page whose own text layer is empty.

Usage:
    pip install rapidocr-onnxruntime pymupdf opencv-python
    python tools/ai_training/ocr_books.py                  # every book flagged in books_report.json
    python tools/ai_training/ocr_books.py --book <id> ...  # specific books
    python tools/ai_training/ocr_books.py --workers 8 --dpi 150
Formulas are not recovered reliably by OCR; prose, headings and worked-example text are.
"""
import argparse
import json
import multiprocessing as mp
import os
import pathlib
import sys
import time

REPO = pathlib.Path(__file__).resolve().parents[2]
BOOKS = REPO / "sources" / "libros"
MANIFEST = BOOKS / "libros.json"
CACHE = BOOKS / ".ocr"
REPORT = REPO / "tools" / "ai_training" / "out" / "books_report.json"
MIN_WORDS = 25  # same threshold as extract_books.py

_ocr = None


def _init(threads):
    global _ocr
    from rapidocr_onnxruntime import RapidOCR

    _ocr = RapidOCR(intra_op_num_threads=threads, inter_op_num_threads=1)


def _page_text(args):
    path, pno, dpi = args
    import cv2
    import numpy as np
    import pymupdf

    doc = pymupdf.open(path)
    page = doc[pno - 1]
    own = page.get_text("text")
    if len(own.split()) >= MIN_WORDS:
        doc.close()
        return pno, None  # has a text layer: nothing to OCR
    pix = page.get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY)
    doc.close()
    img = np.frombuffer(pix.samples, np.uint8).reshape(pix.h, pix.w)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    res, _ = _ocr(img)
    if not res:
        return pno, ""
    # group boxes into lines by their vertical centre, then left to right
    boxes = sorted(res, key=lambda r: (sum(p[1] for p in r[0]) / 4, r[0][0][0]))
    lines, cur, cur_y = [], [], None
    for box, txt, _conf in boxes:
        y = sum(p[1] for p in box) / 4
        h = abs(box[2][1] - box[0][1]) or 10
        if cur_y is not None and abs(y - cur_y) > h * 0.6:
            lines.append(" ".join(t for _, t in sorted(cur)))
            cur = []
        cur.append((box[0][0], txt))
        cur_y = y
    if cur:
        lines.append(" ".join(t for _, t in sorted(cur)))
    return pno, "\n".join(lines)


def ocr_book(entry, workers, threads, dpi):
    import pymupdf

    path = str(BOOKS / entry["file"])
    try:
        n = pymupdf.open(path).page_count
    except Exception as e:
        print(f"  SKIP {entry['id']}: cannot open ({e})")
        return
    if n == 0:
        print(f"  SKIP {entry['id']}: 0 readable pages (truncated or corrupt file, download it again)")
        return
    CACHE.mkdir(parents=True, exist_ok=True)
    cache = CACHE / f"{entry['id']}.jsonl"
    done = set()
    if cache.exists():
        for line in cache.read_text(encoding="utf-8").splitlines():
            try:
                done.add(json.loads(line)["p"])
            except (ValueError, KeyError):
                pass
    todo = [(path, p, dpi) for p in range(1, n + 1) if p not in done]
    print(f"  {entry['id'][:60]}: {n} pages, {len(todo)} to OCR", flush=True)
    if not todo:
        return
    t0, k = time.time(), 0
    with mp.Pool(workers, initializer=_init, initargs=(threads,)) as pool, open(cache, "a", encoding="utf-8") as fh:
        for pno, txt in pool.imap_unordered(_page_text, todo, chunksize=2):
            fh.write(json.dumps({"p": pno, "t": txt}, ensure_ascii=False) + "\n")
            k += 1
            if k % 50 == 0 or k == len(todo):
                fh.flush()
                rate = k / (time.time() - t0)
                print(f"    {k}/{len(todo)} pages  {rate:.2f} p/s  ~{(len(todo) - k) / rate / 60:.0f} min left", flush=True)


def main(argv=None):
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--book", nargs="*", help="Book ids from libros.json (default: flagged in books_report.json).")
    ap.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 2) // 2))
    ap.add_argument("--threads", type=int, default=2, help="ONNX threads per worker.")
    ap.add_argument("--dpi", type=int, default=150)
    args = ap.parse_args(argv)

    books = {b["id"]: b for b in json.loads(MANIFEST.read_text(encoding="utf-8"))["books"]}
    if args.book:
        ids = args.book
    else:
        if not REPORT.exists():
            sys.exit("Run extract_books.py first (it writes books_report.json) or pass --book.")
        report = json.loads(REPORT.read_text(encoding="utf-8"))
        ids = [k for k, v in report.items() if "OCR" in v.get("warning", "") or v.get("ocr_pages")]
    for i in ids:
        if i not in books:
            sys.exit(f"Unknown book id: {i}")
        if books[i].get("use_for_training", True):
            ocr_book(books[i], args.workers, args.threads, args.dpi)
    print("OCR done. Now run: python tools/ai_training/extract_books.py")


if __name__ == "__main__":
    main()
