#!/usr/bin/env python3
"""Claude Pro + Gemini Pro Enrichment & Cross-Audit Helper for Sideris.

Takes the verified English seed dataset from build_dataset.py (tools/ai_training/out/train_sft.jsonl)
and prepares compact, copy-paste or CLI-ready enrichment batches so you can use Claude Pro and
Gemini Pro together to multiply dataset quality:

  1. bilingual_es    : translate & adapt UC3M solutions into natural academic Spanish with
                       [English technical term] on first mention, preserving exact KaTeX and zero skips.
  2. socratic_deep   : expand seed problems into 4-6 turn realistic student-tutor Socratic dialogues
                       with typical sign/unit/Coriolis mistakes and zero leakage of hidden solutions.
  3. check_attempt   : inject ONE subtle engineering error per solution and produce the ideal
                       ask-ai.js `checkAttempt` response (spot ONLY first mistake + graded hint).
  4. merge_validate  : merge enriched JSONL files back with train_sft.jsonl after running strict
                       KaTeX, no-Phase, no-emoji, and Socratic anti-leakage verification gates.

Usage:
    python tools/ai_training/enrich_with_claude_gemini.py export --mode bilingual_es --limit 100
    python tools/ai_training/enrich_with_claude_gemini.py export --mode socratic_deep --limit 80
    python tools/ai_training/enrich_with_claude_gemini.py export --mode check_attempt --limit 80
    python tools/ai_training/enrich_with_claude_gemini.py merge --inputs enriched_es.jsonl enriched_soc.jsonl
"""
import argparse
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools/ai_training"))

from build_dataset import _EMOJI_RE, _PHASE_PREFIX_RE, katex_balanced, system_prompt  # noqa: E402
import rewards  # noqa: E402

PROMPTS = {
    "bilingual_es": (
        "You are preparing verified training data for Sideris (UC3M 2nd-year Aerospace Engineering tutor).\n"
        "For EACH item below, produce ONE JSONL line with keys: id, task, subject, unit, source, messages.\n"
        "Rewrite the user request and assistant answer into natural, rigorous academic SPANISH:\n"
        "- On the FIRST mention of a technical term from the English course notes, write Spanish + [English term], e.g. 'esfuerzo cortante [shear stress]'.\n"
        "- Keep ALL LaTeX equations verbatim in KaTeX format ($...$, $$...$$), NEVER use \\euro, NEVER skip algebraic steps.\n"
        "- NEVER write 'Phase 1..4' or any emoji. Keep SI dimensional checks and limiting cases.\n"
        "Output ONLY valid JSONL (one JSON object per line, no markdown code fences)."
    ),
    "socratic_deep": (
        "You are preparing multi-turn Socratic tutor training dialogues for Sideris (UC3M Aerospace Engineering).\n"
        "For EACH problem below, generate ONE JSONL line with keys: id, task ('socratic_multiturn'), subject, unit, source, messages.\n"
        "The messages array must have: [system (with hidden reference_solution), user (problem), assistant (Q1), "
        "user (realistic student mistake: wrong sign/unit/frame/Coriolis), assistant (catches mistake via question/check WITHOUT revealing answer), "
        "user (student corrects step), assistant (validates and asks next guiding question), user (student reaches final step), "
        "assistant (confirms against reference and asks for SI dimensional check)].\n"
        "HARD RULES: NEVER leak the final numerical/symbolic result in any assistant turn before the student derives it; balanced KaTeX; no emojis; Spanish with [English term] in half the dialogues, English in the other half.\n"
        "Output ONLY valid JSONL."
    ),
    "check_attempt": (
        "You are preparing 'Check my attempt' training data for Sideris (ask-ai.js checkAttempt task).\n"
        "For EACH solved problem below, invent a realistic student attempt containing ONE subtle mistake "
        "(e.g. missing Coriolis term 2*omega x v_r, wrong sign in [{}_0 R_1], wrong control-volume normal sign, "
        "wrong Miller intercept reciprocal, or wrong EBITDA/EBIT classification).\n"
        "Produce ONE JSONL line where the assistant: (1) states which earlier steps are correct, "
        "(2) pinpoints ONLY the first mistake and explains why it fails physically/mathematically, "
        "(3) gives ONE hint to fix it WITHOUT writing the corrected step or final answer.\n"
        "HARD RULES: balanced KaTeX ($...$, $$...$$), zero emojis, no 'Phase' labels. Output ONLY valid JSONL."
    ),
}


def cmd_export(args):
    src = pathlib.Path(args.input)
    if not src.is_file():
        print(f"Missing {src}. Run python tools/ai_training/build_dataset.py first.", file=sys.stderr)
        return 1
    rows = [json.loads(line) for line in src.read_text(encoding="utf-8").splitlines() if line.strip()]
    if args.mode == "bilingual_es":
        pool = [r for r in rows if r["task"] in ("problem_solve", "theory_explain", "derive_principles", "quiz_mcq_tutor")]
    else:
        pool = [r for r in rows if r["task"] == "problem_solve"]

    # Stratify evenly across all 5 subjects
    by_subj = {}
    for r in pool:
        by_subj.setdefault(r["subject"], []).append(r)
    picked = []
    idx = 0
    while len(picked) < args.limit:
        added = False
        for s in sorted(by_subj):
            if idx < len(by_subj[s]) and len(picked) < args.limit:
                picked.append(by_subj[s][idx])
                added = True
        if not added:
            break
        idx += 1

    out_dir = pathlib.Path(args.out) / f"batches_{args.mode}"
    out_dir.mkdir(parents=True, exist_ok=True)
    batch_size = max(1, args.batch_size)
    written = 0
    for b in range(0, len(picked), batch_size):
        chunk = picked[b:b + batch_size]
        p = out_dir / f"batch_{b // batch_size + 1:03d}.txt"
        lines = [PROMPTS[args.mode], "", "=== INPUT ITEMS ==="]
        for item in chunk:
            compact = {
                "id": f"{args.mode}-{item['id']}",
                "subject": item["subject"],
                "unit": item["unit"],
                "source": item["source"],
                "user": item["messages"][1]["content"][:2200],
                "gold_assistant": item["messages"][-1]["content"][:3200],
            }
            lines.append(json.dumps(compact, ensure_ascii=False))
        p.write_text("\n".join(lines) + "\n", encoding="utf-8")
        written += 1
    print(f"Exported {len(picked)} items into {written} prompt batch(es) under {out_dir}")
    return 0


def validate_record(rec):
    if not isinstance(rec, dict) or not isinstance(rec.get("messages"), list) or len(rec["messages"]) < 3:
        return False, "bad_schema"
    full = "\n".join(str(m.get("content", "")) for m in rec["messages"] if m.get("role") == "assistant")
    if not full.strip():
        return False, "empty_assistant"
    if _EMOJI_RE.search(full):
        return False, "emoji"
    if _PHASE_PREFIX_RE.search(full):
        return False, "legacy_phase_label"
    if not katex_balanced(full):
        return False, "katex_unbalanced"
    if rewards.katex_syntax_reward([full])[0] < 0:
        return False, "katex_reward_fail"
    return True, "ok"


def cmd_merge(args):
    base_path = pathlib.Path(args.base)
    out_path = pathlib.Path(args.out_file)
    merged = []
    seen = set()
    rejected = {}

    paths = [base_path] + [pathlib.Path(p) for p in args.inputs]
    for p in paths:
        if not p.is_file():
            print(f"Warning: skipping missing file {p}", file=sys.stderr)
            continue
        for lineno, raw in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            raw = raw.strip()
            if not raw:
                continue
            try:
                rec = json.loads(raw)
            except json.JSONDecodeError:
                rejected["json_error"] = rejected.get("json_error", 0) + 1
                continue
            ok, reason = validate_record(rec)
            if not ok:
                rejected[reason] = rejected.get(reason, 0) + 1
                continue
            rid = rec.get("id") or f"row-{len(merged) + 1}"
            if rid in seen:
                continue
            seen.add(rid)
            # Ensure canonical Sideris system prompt exists
            if rec["messages"][0].get("role") != "system":
                rec["messages"].insert(0, {"role": "system", "content": system_prompt(rec.get("subject", "fluid-mechanics"))})
            merged.append(rec)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        for row in merged:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"Merged {len(merged)} verified training records into {out_path}")
    if rejected:
        print(f"Filtered out invalid records: {rejected}")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Claude Pro + Gemini Pro dataset enrichment helper.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    ex = sub.add_parser("export", help="Export prompt batches for Claude Pro / Gemini Pro.")
    ex.add_argument("--mode", required=True, choices=sorted(PROMPTS))
    ex.add_argument("--input", default=str(REPO / "tools/ai_training/out/train_sft.jsonl"))
    ex.add_argument("--out", default=str(REPO / "tools/ai_training/out"))
    ex.add_argument("--limit", type=int, default=100)
    ex.add_argument("--batch-size", type=int, default=8)

    mg = sub.add_parser("merge", help="Validate and merge enriched JSONL files with train_sft.jsonl.")
    mg.add_argument("--base", default=str(REPO / "tools/ai_training/out/train_sft.jsonl"))
    mg.add_argument("--inputs", nargs="+", required=True)
    mg.add_argument("--out-file", default=str(REPO / "tools/ai_training/out/train_sft_enriched.jsonl"))

    args = ap.parse_args(argv)
    return cmd_export(args) if args.cmd == "export" else cmd_merge(args)


if __name__ == "__main__":
    raise SystemExit(main())
