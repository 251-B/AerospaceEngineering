#!/usr/bin/env python3
"""Textbook PDF Harvester for Sideris v3+ (CPT + SFT from Libros.zip).

Reads digital PDFs inside Libros.zip directly in memory (via pymupdf + zipfile),
maps each book onto its UC3M subject and language, filters out scanned PDFs,
table-of-contents/index/copyright pages, figure-dependent snippets, and garbled
glyphs, and produces:
  1. train_cpt.jsonl      : clean 900-2200 char theory chunks for CPT
  2. textbooks_sft.jsonl  : worked examples & conceptual explanations in SFT schema
  3. sideris-data-v3.zip  : optional combined archive (--build-v3-zip)

Usage:
    python tools/ai_training/extract_textbooks.py --per-subject 400 --cpt-per-book 150 --build-v3-zip
"""
import argparse
import collections
import hashlib
import json
import pathlib
import re
import sys
import zipfile

import pymupdf

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools/ai_training"))

from build_dataset import _EMOJI_RE, katex_balanced, sanitise_text, system_prompt  # noqa: E402
from fetch_external_datasets import load_base_holdout_hashes, norm_text_hash  # noqa: E402
import rewards  # noqa: E402

BOOK_CATALOG = (
    ("white", "fluid-mechanics", "en", "F. M. White — Fluid Mechanics"),
    ("lagerstrom", "fluid-mechanics", "en", "P. A. Lagerstrom — Laminar Flow Theory"),
    ("apostol", "advanced-maths", "en", "T. M. Apostol — Calculus"),
    ("robinson", "advanced-maths", "en", "J. C. Robinson — ODEs"),
    ("haberman", "advanced-maths", "en", "R. Haberman — Applied PDEs"),
    ("mouritz", "aerospace-materials-1", "en", "A. P. Mouritz — Aerospace Materials"),
    ("callister", "aerospace-materials-1", "en", "W. D. Callister — Materials Science & Engineering"),
    ("askeland", "aerospace-materials-1", "en", "D. R. Askeland — Essentials of Materials Science"),
    ("smith", "aerospace-materials-1", "en", "W. F. Smith — Foundations of Materials Science"),
    ("ashby", "aerospace-materials-1", "en", "M. F. Ashby — Engineering Materials"),
    ("shackelford", "aerospace-materials-1", "es", "J. F. Shackelford — Introducción a la Ciencia de Materiales"),
    ("ginsberg", "engineering-mechanics", "en", "J. H. Ginsberg — Engineering Dynamics"),
    ("kermode", "engineering-mechanics", "en", "A. C. Kermode — Mechanics of Flight"),
)

_TOC_INDEX_RE = re.compile(
    r"(?:\.{5,}|table of contents|\bcontents\b.*\n.*\d+|\bbibliography\b|"
    r"\bisbn\b|\ball rights reserved\b|\bprinted in\b|\bcopyright\s*©|"
    r"\bpreface\b|\backnowledgments\b|\bindex\s*$)",
    re.I,
)
_FIG_DEP_RE = re.compile(
    r"(?:\bfigure\s+\d|\bfig\.\s*\d|\bfigura\s+\d|\bshown in\b|\bsee fig\b|"
    r"\bv[eé]ase la figura\b|\ben la figura\b|\btable\s+\d+\.\d+\b)",
    re.I,
)
_EXAMPLE_SOL_RE = re.compile(
    r"(?:^|\n)\s*(?:EXAMPLE|Example|EJEMPLO|Ejemplo)\s+([0-9]+(?:\.[0-9]+)?[^\n]*)\n"
    r"([\s\S]{80,1400}?)\n\s*(?:SOLUTION|Solution|SOLUCI[OÓ]N|Soluci[oó]n)\b[:.\s]*\n"
    r"([\s\S]{260,3200}?)(?=\n\s*(?:EXAMPLE|Example|EJEMPLO|Ejemplo|PROBLEMS|Problems|PROBLEMAS)\b|\Z)",
    re.M,
)


def identify_book(filename):
    """Map an archive member filename to (subject, lang, book_label) or None."""
    low = pathlib.Path(filename).name.lower()
    for needle, subj, lang, label in BOOK_CATALOG:
        if needle in low:
            return subj, lang, label
    return None


def is_digital_pdf(doc, min_avg_chars=200):
    """Return True if sampled interior pages contain selectable digital text."""
    n = len(doc)
    if n < 5:
        return False
    samples = [min(n - 1, max(0, int(n * frac))) for frac in (0.2, 0.5, 0.7)]
    avg = sum(len(doc[pg].get_text("text").strip()) for pg in samples) / len(samples)
    return avg >= min_avg_chars


def clean_pdf_page(raw_text):
    """Strip headers/footers, form feeds, hyphenation line breaks, and extra spacing."""
    text = str(raw_text or "").replace("\f", "\n").replace("\r\n", "\n").replace("\r", "\n")
    lines = text.splitlines()
    # Drop isolated page numbers or short running headers at very top/bottom
    if lines and re.fullmatch(r"\s*(?:\d{1,4}|page\s+\d+|chapter\s+\d+)\s*", lines[0], re.I):
        lines = lines[1:]
    if lines and re.fullmatch(r"\s*(?:\d{1,4}|page\s+\d+)\s*", lines[-1], re.I):
        lines = lines[:-1]
    joined = "\n".join(lines)
    # Rejoin words broken by hyphen at end of PDF line
    joined = re.sub(r"([A-Za-zÁÉÍÓÚÜÑáéíóúüñ])-\n([a-záéíóúüñ])", r"\1\2", joined)
    joined = re.sub(r"[ \t]{2,}", " ", joined)
    joined = re.sub(r"\n{3,}", "\n\n", joined)
    return sanitise_text(joined)


def is_clean_chunk(text, min_len=300, max_len=2400):
    """Return (ok, reason) after enforcing strict PDF hygiene and KaTeX rules."""
    if not text or not (min_len <= len(text) <= max_len):
        return False, "len"
    if _TOC_INDEX_RE.search(text):
        return False, "toc_or_frontmatter"
    if _FIG_DEP_RE.search(text):
        return False, "figure_dep"
    if "\ufffd" in text:
        return False, "replacement_char"
    if _EMOJI_RE.search(text) or rewards._SKIP_PHRASES.search(text):
        return False, "emoji_or_skip"
    # Allow Latin-1 accents (<= U+00FF) and common math symbols; reject private-use/garbled glyphs
    garbled = sum(1 for ch in text if ord(ch) > 0x024F and not ("\u0370" <= ch <= "\u03FF" or "\u2000" <= ch <= "\u22FF"))
    if garbled / len(text) > 0.04:
        return False, "garbled_glyphs"
    alpha = sum(1 for ch in text if ch.isalpha())
    if alpha / len(text) < 0.38:
        return False, "low_alpha"
    if not katex_balanced(text):
        return False, "katex_unbalanced"
    return True, "ok"


def extract_examples_from_pages(clean_pages, subject, lang, book_label, seen_hashes):
    """Extract worked Example/Solution SFT pairs across consecutive cleaned pages."""
    items = []
    # Pair consecutive pages so examples crossing a page boundary are preserved
    for idx in range(len(clean_pages)):
        window = clean_pages[idx]
        if idx + 1 < len(clean_pages):
            window = window + "\n\n" + clean_pages[idx + 1]
        for m in _EXAMPLE_SOL_RE.finditer(window):
            ex_head = sanitise_text(m.group(1))
            stmt = sanitise_text(m.group(2))
            sol = sanitise_text(m.group(3))
            ok_s, _ = is_clean_chunk(stmt, min_len=80, max_len=1400)
            ok_a, _ = is_clean_chunk(sol, min_len=260, max_len=3200)
            if not (ok_s and ok_a):
                continue
            ph = norm_text_hash(stmt)
            if ph in seen_hashes:
                continue
            seen_hashes.add(ph)
            user_prompt = (
                f"<problem_statement title=\"Example {ex_head} ({book_label})\">\n{stmt}\n</problem_statement>\n\n"
                + (
                    "# Tarea\nResuelve este problema paso a paso con el orden del curso UC3M, sin saltos algebraicos y comprobación dimensional."
                    if lang == "es"
                    else "# Task\nSolve this problem step by step following the UC3M course order with zero algebraic skips and a dimensional check."
                )
            )
            items.append({
                "id": f"tb-ex-{subject[:4]}-{ph[:10]}",
                "task": "problem_solve",
                "subject": subject,
                "unit": 0,
                "source": f"textbook/{book_label}",
                "lang": lang,
                "teacher": f"textbook:{book_label}",
                "messages": [
                    {"role": "system", "content": system_prompt(subject, lang=lang, socratic=False)},
                    {"role": "user", "content": user_prompt},
                    {"role": "assistant", "content": sol},
                ],
            })
    return items


def build_cpt_and_theory_chunks(clean_pages, subject, lang, book_label, seen_hashes, max_cpt=150):
    """Build clean 900-2200 char CPT chunks and conceptual theory SFT items."""
    cpt_rows = []
    theory_sft = []
    buf = []
    buf_len = 0

    def flush_chunk():
        nonlocal buf, buf_len
        if not buf:
            return
        chunk = sanitise_text("\n\n".join(buf))
        buf, buf_len = [], 0
        ok, _ = is_clean_chunk(chunk, min_len=900, max_len=2200)
        if not ok:
            return
        ch = norm_text_hash(chunk)
        if ch in seen_hashes:
            return
        seen_hashes.add(ch)
        if len(cpt_rows) < max_cpt:
            cpt_rows.append({
                "id": f"cpt-{subject[:4]}-{ch[:10]}",
                "subject": subject,
                "lang": lang,
                "source": f"textbook/{book_label}",
                "text": chunk,
            })
        # Also create conceptual theory_explain SFT item from clean self-contained section
        first_line = chunk.splitlines()[0].strip("#* ").strip()[:100]
        if len(first_line) >= 12:
            q = (
                f"Explica en español (con el término técnico en inglés entre corchetes la primera vez) el concepto tratado en **{book_label}** sobre: «{first_line}», definiendo cada símbolo."
                if lang == "es"
                else f"In {book_label}, explain clearly from first principles the concept covering: \"{first_line}\", defining every symbol and equation."
            )
            theory_sft.append({
                "id": f"tb-th-{subject[:4]}-{ch[:10]}",
                "task": "theory_explain",
                "subject": subject,
                "unit": 0,
                "source": f"textbook/{book_label}",
                "lang": lang,
                "teacher": f"textbook:{book_label}",
                "messages": [
                    {"role": "system", "content": system_prompt(subject, lang=lang, socratic=False)},
                    {"role": "user", "content": q},
                    {"role": "assistant", "content": chunk},
                ],
            })

    for page_txt in clean_pages:
        for para in page_txt.split("\n\n"):
            p = para.strip()
            if len(p) < 80:
                continue
            if buf_len and buf_len + len(p) + 2 > 1800:
                flush_chunk()
            buf.append(p)
            buf_len += len(p) + 2
        if buf_len >= 1200:
            flush_chunk()
    flush_chunk()
    return cpt_rows, theory_sft


def process_archive(zip_path, holdout_hashes, cpt_per_book=150):
    """Extract clean CPT and SFT candidates from all digital PDFs in Libros.zip."""
    zp = pathlib.Path(zip_path)
    cpt_all = []
    sft_by_subj = collections.defaultdict(list)
    seen_hashes = set(holdout_hashes)
    stats = collections.Counter()

    with zipfile.ZipFile(zp, "r") as zf:
        for info in sorted(zf.infolist(), key=lambda i: i.filename):
            if info.is_dir():
                continue
            book_info = identify_book(info.filename)
            if not book_info:
                stats["unmapped_files"] += 1
                continue
            raw_bytes = zf.read(info.filename)
            if not raw_bytes.startswith(b"%PDF"):
                stats["non_pdf_skipped"] += 1
                continue
            subj, lang, label = book_info
            doc = pymupdf.open(stream=raw_bytes, filetype="pdf")
            try:
                if not is_digital_pdf(doc):
                    stats["scanned_skipped"] += 1
                    print(f"  SKIP scanned : {label}")
                    continue
                stats["digital_books"] += 1
                clean_pages = []
                # Skip first 3% (cover/copyright/TOC) and last 5% (index/answers)
                start_pg = min(len(doc) - 1, max(3, int(len(doc) * 0.03)))
                end_pg = max(start_pg + 1, int(len(doc) * 0.95))
                for pg_idx in range(start_pg, end_pg):
                    cleaned = clean_pdf_page(doc[pg_idx].get_text("text"))
                    if len(cleaned) >= 180 and not _TOC_INDEX_RE.search(cleaned):
                        clean_pages.append(cleaned)
                ex_sft = extract_examples_from_pages(clean_pages, subj, lang, label, seen_hashes)
                cpt_rows, th_sft = build_cpt_and_theory_chunks(
                    clean_pages, subj, lang, label, seen_hashes, max_cpt=cpt_per_book
                )
                cpt_all.extend(cpt_rows)
                sft_by_subj[subj].extend(ex_sft)
                sft_by_subj[subj].extend(th_sft)
                print(
                    f"  OK {subj:22s} ({lang}) | cpt={len(cpt_rows):3d} ex_sft={len(ex_sft):3d} th_sft={len(th_sft):3d} | {label}"
                )
            finally:
                doc.close()

    return cpt_all, sft_by_subj, stats


def build_v3_zip(base_zip_path, out_zip_path, tb_sft, cpt_rows):
    """Merge v2 zip + textbook SFT + train_cpt.jsonl while keeping eval_holdout & rewards verbatim."""
    base_p = pathlib.Path(base_zip_path)
    out_p = pathlib.Path(out_zip_path)
    out_p.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(base_p, "r") as zin, zipfile.ZipFile(out_p, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for name in zin.namelist():
            raw_bytes = zin.read(name)
            if name == "train_sft_enriched.jsonl":
                kept = []
                seen_ids = set()
                for line in raw_bytes.decode("utf-8").splitlines():
                    s = line.strip()
                    if not s:
                        continue
                    row = json.loads(s)
                    rid = str(row.get("id") or "")
                    if rid.startswith("tb-") or str(row.get("teacher") or "").startswith("textbook:"):
                        continue
                    seen_ids.add(rid)
                    kept.append(json.dumps(row, ensure_ascii=False))
                for row in tb_sft:
                    if row["id"] not in seen_ids:
                        seen_ids.add(row["id"])
                        kept.append(json.dumps(row, ensure_ascii=False))
                zout.writestr(name, ("\n".join(kept) + "\n").encode("utf-8"))
            elif name == "train_cpt.jsonl":
                continue
            else:
                zout.writestr(name, raw_bytes)

        cpt_text = "\n".join(json.dumps(r, ensure_ascii=False) for r in cpt_rows) + ("\n" if cpt_rows else "")
        zout.writestr("train_cpt.jsonl", cpt_text.encode("utf-8"))


def main(argv=None):
    ap = argparse.ArgumentParser(description="Extract CPT & SFT datasets from digital PDFs in Libros.zip.")
    ap.add_argument("--zip", default=str(REPO / "Libros.zip"), help="Path to Libros.zip.")
    ap.add_argument("--per-subject", type=int, default=400, help="Max textbook SFT records kept per subject.")
    ap.add_argument("--cpt-per-book", type=int, default=150, help="Max CPT chunks kept per book.")
    ap.add_argument("--out", default=str(REPO / "tools/ai_training/out/textbooks"), help="Output directory.")
    ap.add_argument("--base-zip", default=str(REPO / "tools/ai_training/kaggle_pack/sideris-data.zip"), help="Base v2 zip.")
    ap.add_argument("--build-v3-zip", action="store_true", help="Write combined tools/ai_training/out/sideris-data-v3.zip.")
    ap.add_argument("--v3-zip-out", default=str(REPO / "tools/ai_training/out/sideris-data-v3.zip"), help="Destination v3 zip.")
    args = ap.parse_args(argv)

    holdout_hashes = load_base_holdout_hashes(args.base_zip)
    cpt_rows, sft_by_subj, stats = process_archive(args.zip, holdout_hashes, cpt_per_book=args.cpt_per_book)

    selected_sft = []
    for subj, rows in sorted(sft_by_subj.items()):
        # Prefer worked Example/Solution pairs over general conceptual sections
        ordered = sorted(rows, key=lambda r: (0 if r["task"] == "problem_solve" else 1, -len(r["messages"][-1]["content"]), r["id"]))
        chosen = ordered[: args.per_subject]
        selected_sft.extend(chosen)
        print(f"  SFT {subj:22s}: {len(ordered):4d} clean -> kept {len(chosen)}")

    print(f"Total Textbook CPT: {len(cpt_rows)} | Textbook SFT: {len(selected_sft)} | Stats: {dict(stats)}")

    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    for fname, rows in (("train_cpt.jsonl", cpt_rows), ("textbooks_sft.jsonl", selected_sft)):
        p = out_dir / fname
        p.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + ("\n" if rows else ""), encoding="utf-8")
        print(f"Wrote {p}: {len(rows)} rows")

    if args.build_v3_zip:
        build_v3_zip(args.base_zip, args.v3_zip_out, selected_sft, cpt_rows)
        print(f"Built combined v3 archive -> {args.v3_zip_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
