#!/usr/bin/env python3
"""Convert reference-textbook chunks (books_cpt.jsonl) into verified Sideris SFT datasets.

Prepares prompt batches for a large teacher model (Claude Pro / Gemini Pro) across three modes:
  1. qa_theory         : conceptual Q&A and bilingual-ready explanations grounded in textbook prose
  2. worked_derivation : step-by-step first-principles derivations & SI exercises (CLEAN-TEXT BOOKS ONLY)
  3. socratic_book     : multi-turn Socratic dialogues without revealing the final solution

Every generated record is validated against the same quality gates as build_dataset.py and rewards.py:
  - Balanced KaTeX ($ / $$), zero \\euro, zero '&' inside \\text{}
  - Zero legacy 'Phase 1..4' / 'Fase 1..4' labels, zero emojis, zero algebraic skip phrases
  - SI units / dimensional check markers required on worked_derivation
  - Socratic anti-leak guard via rewards.socratic_guard_reward
  - Strict OCR formula safety gate: OCR-derived books cannot be used for worked_derivation or
    unverified formula-dependent exercises
  - Anti-contamination against eval_holdout.jsonl (exact MD5 + 5-gram Jaccard >= 0.45)
  - Copyright guard against verbatim copying (>= 25 consecutive identical words)

Note: books_cpt.jsonl is copyrighted locally-held textbook material; never commit inputs or generated
batches/outputs to git or upload them to public datasets.

Usage:
    python tools/ai_training/books_to_sft.py export --mode qa_theory --limit 120 --batch-size 4
    python tools/ai_training/books_to_sft.py export --mode worked_derivation --limit 80 --batch-size 3
    python tools/ai_training/books_to_sft.py validate-merge --inputs tools/ai_training/out/book_sft_raw/*.jsonl
"""
import argparse
import collections
import glob
import hashlib
import json
import pathlib
import re
import sys
import zipfile

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools/ai_training"))

from build_dataset import (  # noqa: E402
    _EMOJI_RE,
    _PHASE_PREFIX_RE,
    katex_balanced,
    sanitise_text,
    system_prompt,
)
import rewards  # noqa: E402

SUBJECT_MAP = {
    "01-fluid-mechanics": "fluid-mechanics",
    "02-aerospace-materials-1": "aerospace-materials-1",
    "03-engineering-mechanics": "engineering-mechanics",
    "04-advanced-maths": "advanced-maths",
    "05-business-management": "business-management",
}

_FASE_RE = re.compile(r"\bFase\s*[1-4]\s*[:\-–—.]?", re.I)
_SI_OR_DIM_RE = re.compile(
    r"(?:dimensional\s+check|comprobaci[oó]n\s+dimensional|an[aá]lisis\s+dimensional|"
    r"SI\s+units|unidades\s+SI|\[[MLT\u0398\s\^0-9\-\.\*\/]+\]|"
    r"\\mathrm\{(?:kg|m|s|N|Pa|kPa|MPa|GPa|J|kJ|W|kW|K|rad|Hz|mol)\b)",
    re.I,
)
_EXERCISE_TRIGGER_RE = re.compile(
    r"(?:\bcalculate\b|\bcompute\b|\bfind\s+the\s+numerical\b|\bsolve\s+for\b|<problem_statement\b)",
    re.I,
)

MODE_PROMPTS = {
    "qa_theory": (
        "You are creating high-rigour UC3M Aerospace Engineering SFT Q&A examples from a textbook excerpt.\n"
        "For EACH chunk below, produce ONE JSONL object with keys: id, task ('qa_theory'), subject, lang, "
        "book_id, ocr_source, messages (['user', 'assistant'] — system prompt is added during validate-merge).\n"
        "RULES:\n"
        "- Synthesise a pedagogical student question and a clear, original tutor explanation grounded in the excerpt.\n"
        "- NEVER copy sentences verbatim from the textbook (paraphrase and teach from first principles).\n"
        "- Balanced KaTeX ($...$, $$...$$), NO \\euro, NO '&' inside \\text{}, NO emojis, NO 'Phase 1..4'/'Fase 1..4'.\n"
        "- Define every symbol with SI units on first use and give physical meaning.\n"
        "- If ocr_source=true: teach ONLY conceptual intuition, assumptions and definitions from prose; "
        "DO NOT invent or rely on unverified OCR equations or numerical exercises.\n"
        "Output ONLY valid JSONL (one JSON object per line, no markdown fences)."
    ),
    "worked_derivation": (
        "You are creating step-by-step first-principles derivations / worked problems (clean-text books only).\n"
        "For EACH chunk below, produce ONE JSONL object with keys: id, task ('worked_derivation'), subject, lang, "
        "book_id, ocr_source (false), messages (['user', 'assistant'] — system prompt is added during validate-merge).\n"
        "RULES:\n"
        "- Formulate an original self-contained problem or derivation question (no 'see figure' or missing tables).\n"
        "- Show every algebraic step, chain/product rule, substitution with differential, Barrow limits, boxed answer, "
        "and an explicit SI dimensional check + limiting case.\n"
        "- NEVER skip steps ('after some algebra', 'obviously', 'trivially', 'it can be shown').\n"
        "- Balanced KaTeX ($...$, $$...$$), NO \\euro, NO '&' inside \\text{}, NO emojis, NO 'Phase 1..4'/'Fase 1..4'.\n"
        "Output ONLY valid JSONL (one JSON object per line, no markdown fences)."
    ),
    "socratic_book": (
        "You are creating 4-turn Socratic tutoring dialogues grounded in UC3M Aerospace reference textbooks.\n"
        "For EACH chunk below, produce ONE JSONL object with keys: id, task ('socratic_book'), subject, lang, "
        "book_id, ocr_source, hidden_solution, messages (4 alternating ['user', 'assistant', 'user', 'assistant'] turns).\n"
        "RULES:\n"
        "- Turn 1 (user): asks for help understanding/working through a concept or problem.\n"
        "- Turn 2 (assistant): asks ONE guiding question (setup, hypotheses, governing law) WITHOUT leaking the answer.\n"
        "- Turn 3 (user): student attempt with one common misconception (sign error, wrong unit, missing assumption).\n"
        "- Turn 4 (assistant): catches the misconception and asks ONE guiding follow-up question WITHOUT solving it.\n"
        "- Put the target key concept/answer in hidden_solution (with \\boxed{...} only for clean-text books).\n"
        "- If ocr_source=true: focus strictly on conceptual reasoning and hypotheses, NEVER formula exercises.\n"
        "- Balanced KaTeX, NO \\euro, NO '&' inside \\text{}, NO emojis, NO 'Phase 1..4'.\n"
        "Output ONLY valid JSONL (one JSON object per line, no markdown fences)."
    ),
}


def is_clean_cpt_chunk(rec):
    """Language-aware quality gate for textbook & OCR chunks (mirrors notebook Cell 4)."""
    raw_text = str(rec.get("text") or "")
    body = raw_text
    if "\n\n" in raw_text:
        head, tail = raw_text.split("\n\n", 1)
        if "\n" not in head and len(head) < 300:
            body = tail
    body = body.strip()
    words = body.split()
    if len(words) < 120:
        return False, "too_short"
    non_ws = [c for c in body if not c.isspace()]
    alpha_ratio = sum(c.isalpha() for c in non_ws) / max(1, len(non_ws))
    if alpha_ratio < 0.62:
        return False, "low_alpha"
    single_char_ratio = sum(len(w) == 1 and not w.isdigit() for w in words) / len(words)
    if single_char_ratio > 0.22:
        return False, "high_single_char"
    short_word_ratio = sum(len(w) <= 2 for w in words) / len(words)
    cap = 0.55 if rec.get("lang") == "es" else 0.48
    if short_word_ratio > cap:
        return False, "high_short_words"
    weird_ratio = sum(
        c == "\ufffd" or (ord(c) < 32 and c not in "\n\t\r") or (ord(c) > 0x2FFF)
        for c in body
    ) / max(1, len(body))
    if weird_ratio > 0.04:
        return False, "mojibake"
    avg_word_len = sum(len(w) for w in words) / len(words)
    if not (3.0 <= avg_word_len <= 14.0):
        return False, "bad_word_len"
    return True, "ok"


def normalise_subject(subject):
    return SUBJECT_MAP.get(str(subject or "").strip(), str(subject or "fluid-mechanics").strip())


def classify_ocr_books(report_path=None, ocr_cache_dir=None):
    """Return book_ids that rely on OCR pages (via books_report.json or .ocr/*.jsonl)."""
    ocr_books = set()
    rep_p = pathlib.Path(report_path) if report_path else (REPO / "tools/ai_training/out/books_report.json")
    if rep_p.is_file():
        data = json.loads(rep_p.read_text(encoding="utf-8"))
        for bid, stats in data.items():
            if not isinstance(stats, dict):
                continue
            if stats.get("ocr_pages", 0) > 0 or "OCR" in str(stats.get("warning", "")):
                ocr_books.add(bid)
    cache_p = pathlib.Path(ocr_cache_dir) if ocr_cache_dir else (REPO / "sources/libros/.ocr")
    if cache_p.is_dir():
        for f in cache_p.glob("*.jsonl"):
            ocr_books.add(f.stem)
    return ocr_books


def norm_text_hash(text):
    norm = re.sub(r"[^a-z0-9]+", "", str(text or "").lower())
    return hashlib.md5(norm.encode("utf-8")).hexdigest()


def _word_tokens(text):
    return re.findall(r"[a-z0-9]+", str(text or "").lower())


def _shingles(text, k=5):
    toks = _word_tokens(text)
    if len(toks) < k:
        return set()
    return {tuple(toks[i:i + k]) for i in range(len(toks) - k + 1)}


def load_holdout_index(holdout_path=None):
    """Load exact hashes and 5-gram shingles from eval_holdout.jsonl (or inside sideris-data.zip)."""
    rows = []
    candidates = [pathlib.Path(holdout_path)] if holdout_path else [
        REPO / "tools/ai_training/out/eval_holdout.jsonl",
        REPO / "tools/ai_training/kaggle_pack/sideris-data.zip",
    ]
    for p in candidates:
        if not p.is_file():
            continue
        if p.suffix == ".zip":
            with zipfile.ZipFile(p, "r") as zf:
                if "eval_holdout.jsonl" in zf.namelist():
                    raw_lines = zf.read("eval_holdout.jsonl").decode("utf-8", errors="replace").splitlines()
                    rows = [json.loads(l) for l in raw_lines if l.strip()]
                    break
        else:
            raw_lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
            rows = [json.loads(l) for l in raw_lines if l.strip()]
            break

    hashes = set()
    shingle_list = []
    for rec in rows:
        for m in rec.get("messages", []):
            if m.get("role") in ("user", "assistant"):
                txt = str(m.get("content") or "")
                hashes.add(norm_text_hash(txt))
                inner = re.search(r"<problem_statement[^>]*>([\s\S]*?)</problem_statement>", txt)
                if inner:
                    hashes.add(norm_text_hash(inner.group(1)))
                sh = _shingles(txt, k=5)
                if sh:
                    shingle_list.append(sh)
    return {"hashes": hashes, "shingles": shingle_list}


def is_holdout_contaminated(text, holdout_index, jaccard_threshold=0.45):
    if not text or not holdout_index:
        return False
    if norm_text_hash(text) in holdout_index["hashes"]:
        return True
    sh = _shingles(text, k=5)
    if not sh:
        return False
    for h_sh in holdout_index["shingles"]:
        union_n = len(sh | h_sh)
        if union_n and (len(sh & h_sh) / union_n) >= jaccard_threshold:
            return True
    return False


def has_verbatim_copy(answer_text, source_chunk_text, max_consecutive_words=25):
    """Reject responses that copy >= max_consecutive_words consecutive words verbatim."""
    if not answer_text or not source_chunk_text:
        return False
    ans_toks = _word_tokens(answer_text)
    src_toks = _word_tokens(source_chunk_text)
    if len(ans_toks) < max_consecutive_words or len(src_toks) < max_consecutive_words:
        return False
    src_ngrams = {tuple(src_toks[i:i + max_consecutive_words]) for i in range(len(src_toks) - max_consecutive_words + 1)}
    for i in range(len(ans_toks) - max_consecutive_words + 1):
        if tuple(ans_toks[i:i + max_consecutive_words]) in src_ngrams:
            return True
    return False


def normalise_book_sft_record(rec, default_task="qa_theory"):
    rec = dict(rec)
    subj = normalise_subject(rec.get("subject"))
    rec["subject"] = subj
    task = str(rec.get("task") or default_task)
    rec["task"] = task
    lang = str(rec.get("lang") or "en")
    rec["lang"] = lang
    socratic = task == "socratic_book"
    msgs = list(rec.get("messages") or [])
    if msgs and msgs[0].get("role") != "system":
        sys_txt = system_prompt(subj, lang=lang, socratic=socratic)
        hid = str(rec.get("hidden_solution") or "").strip()
        if socratic and hid:
            sys_txt += f'\n\n<reference_solution hidden="true">\n{hid[:3200]}\n</reference_solution>'
        msgs.insert(0, {"role": "system", "content": sys_txt})
    rec["messages"] = msgs
    return rec


def validate_book_sft_record(
    rec,
    holdout_index=None,
    seen_hashes=None,
    source_chunk_text="",
    source_chunks=None,
):
    """Validate a generated book-derived SFT record against every Sideris gate."""
    if not isinstance(rec, dict) or not isinstance(rec.get("messages"), list) or len(rec["messages"]) < 3:
        return False, "bad_schema"
    msgs = rec["messages"]
    if msgs[0].get("role") != "system":
        return False, "missing_system"
    user_turns = [str(m.get("content") or "") for m in msgs if m.get("role") == "user"]
    asst_turns = [str(m.get("content") or "") for m in msgs if m.get("role") == "assistant"]
    if not user_turns or not asst_turns or any(not t.strip() for t in user_turns + asst_turns):
        return False, "empty_turn"

    user_joined = "\n".join(user_turns)
    asst_joined = "\n".join(asst_turns)
    combined = f"{user_joined}\n{asst_joined}"
    task = str(rec.get("task") or "qa_theory")
    subj = normalise_subject(rec.get("subject"))

    if len(user_joined.strip()) < 25 or len(asst_joined.strip()) < 80:
        return False, "too_short"
    if _EMOJI_RE.search(combined):
        return False, "emoji"
    if _PHASE_PREFIX_RE.search(combined) or _FASE_RE.search(combined):
        return False, "legacy_phase_label"
    if not (katex_balanced(user_joined) and katex_balanced(asst_joined)):
        return False, "katex_unbalanced"
    if rewards.katex_syntax_reward([asst_joined])[0] < 0:
        return False, "katex_reward_fail"

    if task != "socratic_book" and rewards._SKIP_PHRASES.search(asst_joined):
        return False, "skip_phrase"

    if task == "worked_derivation" and subj != "business-management":
        if not _SI_OR_DIM_RE.search(asst_joined):
            return False, "missing_si_or_dim_check"

    # OCR formula safety gate: never allow formula-dependent exercises from unverified OCR text
    if rec.get("ocr_source") and not rec.get("verified_formula", False):
        if task == "worked_derivation":
            return False, "ocr_worked_derivation_forbidden"
        hid_txt = str(rec.get("hidden_solution") or "")
        if _EXERCISE_TRIGGER_RE.search(user_joined) and (
            "$$" in combined or r"\boxed{" in combined or r"\boxed{" in hid_txt
        ):
            return False, "ocr_unverified_formula_exercise"

    if task == "socratic_book":
        hid = str(rec.get("hidden_solution") or "")
        boxed = re.findall(r"\\boxed\{([^{}]+)\}", hid)
        forbid = boxed[-1].strip() if boxed else ""
        if any(rewards.socratic_guard_reward([t], socratic=[True], forbidden_answers=[forbid])[0] < 0 for t in asst_turns):
            return False, "socratic_guard_fail"

    sources_to_check = list(source_chunks or [])
    if source_chunk_text:
        sources_to_check.append(source_chunk_text)
    if any(has_verbatim_copy(asst_joined, s_txt) for s_txt in sources_to_check):
        return False, "verbatim_copy"

    if holdout_index and (
        is_holdout_contaminated(user_joined, holdout_index)
        or is_holdout_contaminated(asst_joined, holdout_index)
    ):
        return False, "holdout_contaminated"

    uhash = norm_text_hash(user_joined)
    if seen_hashes is not None:
        if uhash in seen_hashes:
            return False, "duplicate_prompt"
        seen_hashes.add(uhash)

    return True, "ok"


def cmd_export(args):
    books_path = pathlib.Path(args.books_jsonl)
    if not books_path.is_file():
        print(f"Missing {books_path}. Run extract_books.py first.", file=sys.stderr)
        return 1

    ocr_books = classify_ocr_books(args.report, args.ocr_dir)
    pool_by_subj = collections.defaultdict(list)
    skipped = collections.Counter()

    with books_path.open(encoding="utf-8") as fh:
        for idx, line in enumerate(fh, 1):
            if not line.strip():
                continue
            rec = json.loads(line)
            ok, reason = is_clean_cpt_chunk(rec)
            if not ok:
                skipped[reason] += 1
                continue
            is_ocr = bool(rec.get("ocr")) or (rec.get("book_id") in ocr_books)
            if args.mode == "worked_derivation" and is_ocr:
                skipped["ocr_excluded_worked_derivation"] += 1
                continue
            subj = normalise_subject(rec.get("subject"))
            rec["_is_ocr"] = is_ocr
            rec["_chunk_idx"] = idx
            pool_by_subj[subj].append(rec)

    ordered = []
    i = 0
    while len(ordered) < args.limit:
        added = False
        for subj in sorted(pool_by_subj):
            if i < len(pool_by_subj[subj]):
                ordered.append(pool_by_subj[subj][i])
                added = True
                if len(ordered) >= args.limit:
                    break
        if not added:
            break
        i += 1

    out_dir = pathlib.Path(args.out_dir) / f"book_sft_batches_{args.mode}"
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("batch_*.txt"):
        old.unlink()

    bs = max(1, args.batch_size)
    written = 0
    for b in range(0, len(ordered), bs):
        chunk_rows = ordered[b:b + bs]
        lines = [MODE_PROMPTS[args.mode], "", "=== BOOK CHUNKS ==="]
        for r in chunk_rows:
            lines.append(
                json.dumps(
                    {
                        "id": f"bk-{args.mode}-{r['book_id'][:16]}-{r['_chunk_idx']}",
                        "subject": normalise_subject(r.get("subject")),
                        "lang": r.get("lang", "en"),
                        "book_id": r.get("book_id"),
                        "ocr_source": r["_is_ocr"],
                        "text": sanitise_text(r.get("text", ""))[:3600],
                    },
                    ensure_ascii=False,
                )
            )
        (out_dir / f"batch_{b // bs + 1:03d}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
        written += 1

    print(f"Exported {len(ordered)} chunks into {written} batch(es) -> {out_dir} (skipped: {dict(skipped)})")
    return 0


def cmd_validate_merge(args):
    holdout_idx = load_holdout_index(args.holdout)
    seen_hashes = set()
    rejected = collections.Counter()
    accepted = []

    source_lookup = {}
    if args.books_jsonl and pathlib.Path(args.books_jsonl).is_file():
        with pathlib.Path(args.books_jsonl).open(encoding="utf-8") as fh:
            for line in fh:
                if not line.strip():
                    continue
                r = json.loads(line)
                source_lookup.setdefault(r.get("book_id", ""), []).append(r.get("text", ""))

    input_paths = []
    for pat in args.inputs:
        matches = sorted(glob.glob(pat))
        input_paths.extend(pathlib.Path(m) for m in (matches or [pat]))

    for p in input_paths:
        if not p.is_file():
            continue
        for raw in p.read_text(encoding="utf-8", errors="replace").splitlines():
            s = raw.strip()
            if not s:
                continue
            try:
                rec = json.loads(s)
            except json.JSONDecodeError:
                rejected["json_error"] += 1
                continue
            rec = normalise_book_sft_record(rec)
            src_txt = rec.pop("_source_text", "")
            book_chunks = source_lookup.get(rec.get("book_id", ""), [])
            ok, reason = validate_book_sft_record(
                rec,
                holdout_idx,
                seen_hashes,
                source_chunk_text=src_txt,
                source_chunks=book_chunks,
            )
            if ok:
                accepted.append(rec)
            else:
                rejected[reason] += 1

    out_p = pathlib.Path(args.out)
    out_p.parent.mkdir(parents=True, exist_ok=True)
    with out_p.open("w", encoding="utf-8") as fh:
        for row in accepted:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"Verified {len(accepted)} book-SFT records -> {out_p} | Rejected: {dict(rejected)}")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Convert books_cpt.jsonl into verified Sideris SFT datasets.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    ex = sub.add_parser("export", help="Export stratified teacher prompt batches from books_cpt.jsonl.")
    ex.add_argument("--mode", required=True, choices=sorted(MODE_PROMPTS))
    ex.add_argument("--books-jsonl", default=str(REPO / "tools/ai_training/out/books_cpt.jsonl"))
    ex.add_argument("--report", default=str(REPO / "tools/ai_training/out/books_report.json"))
    ex.add_argument("--ocr-dir", default=str(REPO / "sources/libros/.ocr"))
    ex.add_argument("--out-dir", default=str(REPO / "tools/ai_training/out"))
    ex.add_argument("--limit", type=int, default=100)
    ex.add_argument("--batch-size", type=int, default=4)

    vm = sub.add_parser("validate-merge", help="Validate generated JSONL against Sideris gates and holdout.")
    vm.add_argument("--inputs", nargs="+", required=True)
    vm.add_argument("--holdout", default="")
    vm.add_argument("--books-jsonl", default="")
    vm.add_argument("--out", default=str(REPO / "tools/ai_training/out/book_sft_verified.jsonl"))

    args = ap.parse_args(argv)
    if args.cmd == "export":
        return cmd_export(args)
    return cmd_validate_merge(args)


if __name__ == "__main__":
    raise SystemExit(main())
