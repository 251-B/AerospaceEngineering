#!/usr/bin/env python3
"""Claude Pro + Gemini Pro Enrichment & Cross-Audit Factory for Sideris.

Takes the verified English seed dataset from build_dataset.py (tools/ai_training/out/train_sft.jsonl)
and runs / prepares dual-teacher enrichment using Claude Pro (local Claude Code CLI or web)
and Gemini Pro (Antigravity workflow or web):

  1. bilingual_es    : translate & adapt UC3M solutions into natural academic Spanish with
                       [English technical term] on first mention, preserving exact KaTeX and zero skips.
  2. socratic_deep   : expand seed problems into 4-6 turn realistic student-tutor Socratic dialogues
                       with typical sign/unit/Coriolis mistakes and zero leakage of hidden solutions.
  3. check_attempt   : inject ONE subtle engineering error per solution and produce the ideal
                       ask-ai.js `checkAttempt` response (spot ONLY first mistake + graded hint).
  4. run-claude      : execute exported batches automatically through local `claude -p` (Claude Pro),
                       with per-batch checkpointing and strict JSON/KaTeX validation.
  5. merge           : merge all enriched JSONL files with train_sft.jsonl -> train_sft_enriched.jsonl
                       and synthesise upgraded DPO pairs -> train_dpo_enriched.jsonl.

Usage:
    python tools/ai_training/enrich_with_claude_gemini.py export --mode bilingual_es --limit 100 --batch-size 5
    python tools/ai_training/enrich_with_claude_gemini.py export --mode socratic_deep --limit 50 --batch-size 2
    python tools/ai_training/enrich_with_claude_gemini.py export --mode check_attempt --limit 60 --batch-size 3
    python tools/ai_training/enrich_with_claude_gemini.py run-claude --mode socratic_deep --out-jsonl tools/ai_training/out/enriched/socratic_deep_claude.jsonl
    python tools/ai_training/enrich_with_claude_gemini.py merge --inputs tools/ai_training/out/enriched/*.jsonl
"""
import argparse
import collections
import glob
import json
import pathlib
import re
import shutil
import subprocess
import sys
import time

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
        "- NEVER write 'Phase 1..4' or 'Fase 1..4' or any emoji. Keep SI dimensional checks and limiting cases.\n"
        "- The messages array MUST have roles: ['user', 'assistant'] (system prompt is added automatically during merge).\n"
        "Output ONLY valid JSONL (one JSON object per line, no markdown code fences, no commentary)."
    ),
    "socratic_deep": (
        "You are preparing multi-turn Socratic tutor training dialogues for Sideris (UC3M Aerospace Engineering).\n"
        "For EACH problem below, generate ONE JSONL line with keys: id, task ('socratic_multiturn'), subject, unit, source, lang ('es' or 'en'), hidden_solution, messages.\n"
        "The messages array MUST have 8 turns alternating user/assistant (NO system message — it is injected automatically during merge):\n"
        "  1. user: <problem_statement>...</problem_statement> + ask to solve step by step from the start.\n"
        "  2. assistant: Q1 asking for given data (with SI units), unknowns, and governing law / reference frame.\n"
        "  3. user: realistic student attempt containing ONE classic mistake (wrong sign, missing Coriolis 2*omega x v_r, wrong CV normal, wrong Miller reciprocal, or wrong EBITDA/EBIT line).\n"
        "  4. assistant: acknowledges what is right, catches the mistake via a physical/dimensional check or probing question WITHOUT revealing the corrected step or final answer.\n"
        "  5. user: student corrects that mistake and advances to the main derivation/equation.\n"
        "  6. assistant: validates the corrected step and asks for the next explicit algebraic/numerical step.\n"
        "  7. user: student completes the calculation and proposes the final result.\n"
        "  8. assistant: confirms the final result against the reference solution and asks for a brief SI dimensional check or limiting-case check.\n"
        "HARD RULES:\n"
        "- Copy the short key result from gold_assistant into hidden_solution.\n"
        "- NEVER reveal the final numerical/symbolic result in turns 2, 4, or 6!\n"
        "- Balanced KaTeX ($...$, $$...$$), NEVER use \\euro, NEVER use '&' inside \\text{}, ZERO emojis, ZERO 'Phase 1..4' or 'Fase 1..4' labels.\n"
        "- Alternate language across items: odd items in natural academic SPANISH with [English technical term] on first mention (lang='es'); even items in ENGLISH (lang='en').\n"
        "Output ONLY valid JSONL (one JSON object per line, no markdown code fences, no commentary)."
    ),
    "check_attempt": (
        "You are preparing 'Check my attempt' training data for Sideris (matching the ask-ai.js checkAttempt mode).\n"
        "For EACH solved problem below, produce ONE JSONL line with keys: id, task ('check_attempt'), subject, unit, source, lang ('es' or 'en'), hidden_solution, messages.\n"
        "The messages array MUST have 2 turns ['user', 'assistant'] (system prompt is added automatically during merge):\n"
        "- user: includes <problem_statement>...</problem_statement> AND <student_attempt>...</student_attempt> containing a realistic multi-step attempt that gets the first 1-2 steps right and makes ONE subtle engineering mistake (e.g. missing Coriolis term, wrong rotation-matrix sign, wrong CV normal sign, wrong boundary condition, wrong Miller intercept reciprocal, or wrong EBIT/EBITDA classification), asking Sideris to check the attempt without giving away the answer.\n"
        "- assistant: (1) briefly confirms which earlier steps are correct, (2) pinpoints ONLY the first mistake and explains physically/mathematically why it fails, (3) gives ONE focused hint to fix it WITHOUT writing out the corrected equation or revealing the final answer.\n"
        "HARD RULES:\n"
        "- Copy the final numerical/symbolic answer from gold_assistant into hidden_solution.\n"
        "- Balanced KaTeX ($...$, $$...$$), NEVER use \\euro, NEVER use '&' inside \\text{}, ZERO emojis, ZERO 'Phase 1..4' or 'Fase 1..4' labels.\n"
        "- Alternate language across items: odd items in natural academic SPANISH with [English technical term] on first mention (lang='es'); even items in ENGLISH (lang='en').\n"
        "Output ONLY valid JSONL (one JSON object per line, no markdown code fences, no commentary)."
    ),
}

_FASE_RE = re.compile(r"\bFase\s*[1-4]\s*[:\-–—.]?", re.I)


def extract_json_objects(raw_text):
    """Parse JSONL lines cleanly, tolerating accidental markdown fences or blank lines."""
    objs = []
    cleaned = re.sub(r"^\s*```(?:json|jsonl)?\s*$", "", raw_text, flags=re.M | re.I)
    for line in cleaned.splitlines():
        s = line.strip()
        if not s or not s.startswith("{"):
            continue
        try:
            obj = json.loads(s)
            if isinstance(obj, dict):
                objs.append(obj)
        except json.JSONDecodeError:
            continue
    return objs


def normalise_record(rec, default_task=None):
    """Ensure canonical system prompt, lang, and clean messages structure."""
    rec = dict(rec)
    subj = rec.get("subject", "fluid-mechanics")
    task = rec.get("task") or default_task or "bilingual_es"
    rec["task"] = task
    lang = rec.get("lang") or ("es" if task == "bilingual_es" else "en")
    rec["lang"] = lang
    socratic = task in ("socratic_multiturn", "socratic_seed", "check_attempt")
    msgs = list(rec.get("messages") or [])
    if not msgs:
        return rec
    if msgs[0].get("role") != "system":
        sys_text = system_prompt(subj, lang=lang, socratic=socratic)
        hid = (rec.get("hidden_solution") or "").strip()
        if socratic and hid:
            sys_text += f'\n\n<reference_solution hidden="true">\n{hid[:3200]}\n</reference_solution>'
        msgs.insert(0, {"role": "system", "content": sys_text})
    rec["messages"] = msgs
    return rec


def validate_record(rec):
    if not isinstance(rec, dict) or not isinstance(rec.get("messages"), list) or len(rec["messages"]) < 3:
        return False, "bad_schema"
    msgs = rec["messages"]
    if msgs[0].get("role") != "system":
        return False, "missing_system"
    assistant_turns = [str(m.get("content", "")) for m in msgs if m.get("role") == "assistant"]
    if not assistant_turns or any(not t.strip() for t in assistant_turns):
        return False, "empty_assistant"
    full = "\n".join(assistant_turns)
    if _EMOJI_RE.search(full):
        return False, "emoji"
    if _PHASE_PREFIX_RE.search(full) or _FASE_RE.search(full):
        return False, "legacy_phase_label"
    if not katex_balanced(full):
        return False, "katex_unbalanced"
    if rewards.katex_syntax_reward([full])[0] < 0:
        return False, "katex_reward_fail"
    # Anti-leak check for Socratic early turns and check_attempt
    task = rec.get("task", "")
    hid = str(rec.get("hidden_solution") or "")
    boxed = re.findall(r"\\boxed\{([^{}]+)\}", hid)
    forbid = boxed[-1].strip() if boxed else ""
    if forbid and len(forbid) >= 3:
        if task == "check_attempt":
            if rewards.socratic_no_leak_reward([assistant_turns[0]], [forbid])[0] < 0:
                return False, "check_attempt_leak"
        elif task == "socratic_multiturn" and len(assistant_turns) >= 2:
            early = "\n".join(assistant_turns[:-1])
            if rewards.socratic_no_leak_reward([early], [forbid])[0] < 0:
                return False, "socratic_early_leak"
    return True, "ok"


def stratified_pool(rows, mode, offset, limit):
    if mode == "bilingual_es":
        pool = [r for r in rows if r["task"] in ("problem_solve", "theory_explain", "derive_principles", "quiz_mcq_tutor")]
    else:
        pool = [r for r in rows if r["task"] == "problem_solve"]

    by_subj = {}
    for r in pool:
        by_subj.setdefault(r["subject"], []).append(r)

    ordered = []
    idx = 0
    while True:
        added = False
        for s in sorted(by_subj):
            if idx < len(by_subj[s]):
                ordered.append(by_subj[s][idx])
                added = True
        if not added:
            break
        idx += 1
    return ordered[offset:offset + limit]


def cmd_export(args):
    src = pathlib.Path(args.input)
    if not src.is_file():
        print(f"Missing {src}. Run python tools/ai_training/build_dataset.py first.", file=sys.stderr)
        return 1
    rows = [json.loads(line) for line in src.read_text(encoding="utf-8").splitlines() if line.strip()]
    picked = stratified_pool(rows, args.mode, args.offset, args.limit)

    subdir = args.subdir or f"batches_{args.mode}"
    out_dir = pathlib.Path(args.out) / subdir
    out_dir.mkdir(parents=True, exist_ok=True)
    # Remove stale batch files if re-exporting cleanly
    for old in out_dir.glob("batch_*.txt"):
        old.unlink()

    batch_size = max(1, args.batch_size)
    written = 0
    for b in range(0, len(picked), batch_size):
        chunk = picked[b:b + batch_size]
        p = out_dir / f"batch_{b // batch_size + 1:03d}.txt"
        lines = [PROMPTS[args.mode], "", "=== INPUT ITEMS ==="]
        for item in chunk:
            compact = {
                "id": f"{args.mode}-{item['id']}",
                "orig_task": item["task"],
                "subject": item["subject"],
                "unit": item["unit"],
                "source": item["source"],
                "user": item["messages"][1]["content"][:2200],
                "gold_assistant": item["messages"][-1]["content"][:3200],
            }
            lines.append(json.dumps(compact, ensure_ascii=False))
        p.write_text("\n".join(lines) + "\n", encoding="utf-8")
        written += 1
    print(f"Exported {len(picked)} items (offset={args.offset}) into {written} batch(es) under {out_dir}")
    return 0


def cmd_run_claude(args):
    claude_bin = shutil.which("claude")
    if not claude_bin:
        print("Error: `claude` CLI not found on PATH.", file=sys.stderr)
        return 1

    batch_dir = pathlib.Path(args.batch_dir)
    batches = sorted(batch_dir.glob("batch_*.txt"))
    if not batches:
        print(f"No batch_*.txt files found under {batch_dir}. Run `export` first.", file=sys.stderr)
        return 1

    out_jsonl = pathlib.Path(args.out_jsonl)
    out_jsonl.parent.mkdir(parents=True, exist_ok=True)
    ckpt_file = out_jsonl.with_suffix(".done.json")
    done_batches = set(json.loads(ckpt_file.read_text(encoding="utf-8"))) if ckpt_file.is_file() else set()

    default_task = "socratic_multiturn" if args.mode == "socratic_deep" else args.mode
    total_ok = 0
    total_bad = collections.Counter()

    for idx, bpath in enumerate(batches, 1):
        if bpath.name in done_batches:
            print(f"[{idx}/{len(batches)}] Skipping already-done {bpath.name}", flush=True)
            continue
        prompt_text = bpath.read_text(encoding="utf-8")
        t0 = time.time()
        cmd = [claude_bin, "-p", "--tools", "", "--max-turns", "1", "--output-format", "text"]
        if args.model:
            cmd.extend(["--model", args.model])
        try:
            proc = subprocess.run(
                cmd,
                input=prompt_text,
                text=True,
                capture_output=True,
                encoding="utf-8",
                errors="replace",
                timeout=args.timeout,
            )
        except subprocess.TimeoutExpired:
            print(f"[{idx}/{len(batches)}] TIMEOUT on {bpath.name} after {args.timeout}s", flush=True)
            continue

        dt = time.time() - t0
        if proc.returncode != 0:
            err_tail = (proc.stderr or proc.stdout or "").strip()[:300]
            print(f"[{idx}/{len(batches)}] ERROR rc={proc.returncode} on {bpath.name} ({dt:.1f}s): {err_tail}", flush=True)
            if "rate" in err_tail.lower() or "limit" in err_tail.lower():
                print("Stopping cleanly on Claude rate limit. Re-run the same command later to resume.", flush=True)
                break
            continue

        objs = extract_json_objects(proc.stdout)
        batch_valid = []
        for obj in objs:
            rec = normalise_record(obj, default_task=default_task)
            rec["teacher"] = "claude-pro"
            ok, reason = validate_record(rec)
            if ok:
                batch_valid.append(rec)
            else:
                total_bad[reason] += 1

        if batch_valid:
            with out_jsonl.open("a", encoding="utf-8") as f:
                for r in batch_valid:
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
            done_batches.add(bpath.name)
            ckpt_file.write_text(json.dumps(sorted(done_batches), indent=2), encoding="utf-8")
            total_ok += len(batch_valid)
            print(f"[{idx}/{len(batches)}] {bpath.name}: +{len(batch_valid)} valid ({dt:.1f}s)", flush=True)
        else:
            raw_dump = out_jsonl.parent / f"failed_{args.mode}_{bpath.stem}.txt"
            raw_dump.write_text(proc.stdout or "", encoding="utf-8")
            print(f"[{idx}/{len(batches)}] {bpath.name}: 0 valid (parsed {len(objs)} objs, saved raw to {raw_dump.name})", flush=True)

    print(f"Claude run finished: +{total_ok} new valid rows written to {out_jsonl}. Rejected: {dict(total_bad)}", flush=True)
    return 0


def make_enriched_dpo_pairs(enriched_rows):
    """Synthesise high-signal DPO pairs specifically targeting bilingual, Socratic, and check_attempt failure modes."""
    pairs = []
    for rec in enriched_rows:
        msgs = rec["messages"]
        if len(msgs) < 3:
            continue
        task = rec.get("task", "")
        chosen = msgs[-1]["content"]
        prompt = msgs[:-1]
        if task == "check_attempt":
            hid = str(rec.get("hidden_solution") or "the final result")[:280]
            rejected = (
                "### Phase 1: Full Solution\n"
                "Your attempt is wrong. Here is the complete final answer directly instead of a hint:\n\n"
                f"{hid}\n\nThe intermediate steps are straightforward."
            )
            pairs.append({
                "id": f"dpo-chk-{rec['id']}",
                "category": "check_attempt_no_spoiler",
                "subject": rec["subject"],
                "source": rec["source"],
                "prompt": prompt,
                "chosen": [{"role": "assistant", "content": chosen}],
                "rejected": [{"role": "assistant", "content": rejected}],
            })
        elif task == "bilingual_es" and len(chosen) >= 240:
            rejected = (
                "### Phase 1: Answer\n"
                "To solve this problem in English, just plug the numbers into the standard formula and you get the answer directly. "
                "The remaining algebra is left as an exercise."
            )
            pairs.append({
                "id": f"dpo-es-{rec['id']}",
                "category": "bilingual_es_and_rigour",
                "subject": rec["subject"],
                "source": rec["source"],
                "prompt": prompt,
                "chosen": [{"role": "assistant", "content": chosen}],
                "rejected": [{"role": "assistant", "content": rejected}],
            })
        elif task == "socratic_multiturn" and len(msgs) >= 5:
            # Prefer turn-4 error-catching Socratic reply over an immediate spoiler!
            hid = str(rec.get("hidden_solution") or "the final answer")[:280]
            pairs.append({
                "id": f"dpo-soc-deep-{rec['id']}",
                "category": "socratic_deep_no_leak",
                "subject": rec["subject"],
                "source": rec["source"],
                "prompt": msgs[:4],
                "chosen": [{"role": "assistant", "content": msgs[4]["content"]}],
                "rejected": [{"role": "assistant", "content": f"That step is incorrect. Here is the full solved answer directly: {hid}"}],
            })
    return pairs


def cmd_merge(args):
    base_path = pathlib.Path(args.base)
    out_path = pathlib.Path(args.out_file)
    merged = []
    enriched_only = []
    seen = set()
    rejected = collections.Counter()

    # Expand globs on Windows where PowerShell doesn't expand quotes
    input_paths = []
    for pat in args.inputs:
        matches = sorted(glob.glob(pat))
        input_paths.extend(pathlib.Path(m) for m in (matches or [pat]))

    for is_base, p in [(True, base_path)] + [(False, x) for x in input_paths]:
        if not p.is_file():
            print(f"Warning: skipping missing file {p}", file=sys.stderr)
            continue
        for raw in p.read_text(encoding="utf-8").splitlines():
            raw = raw.strip()
            if not raw:
                continue
            try:
                rec = json.loads(raw)
            except json.JSONDecodeError:
                rejected["json_error"] += 1
                continue
            rec = normalise_record(rec)
            ok, reason = validate_record(rec)
            if not ok:
                rejected[reason] += 1
                continue
            rid = rec.get("id") or f"row-{len(merged) + 1}"
            if rid in seen:
                continue
            seen.add(rid)
            merged.append(rec)
            if not is_base:
                enriched_only.append(rec)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        for row in merged:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    # Also build enriched DPO file if base DPO exists
    dpo_base = pathlib.Path(args.dpo_base)
    dpo_out = pathlib.Path(args.dpo_out)
    dpo_rows = []
    if dpo_base.is_file():
        dpo_rows.extend(json.loads(l) for l in dpo_base.read_text(encoding="utf-8").splitlines() if l.strip())
    new_dpo = make_enriched_dpo_pairs(enriched_only)
    dpo_rows.extend(new_dpo)
    with dpo_out.open("w", encoding="utf-8") as f:
        for row in dpo_rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    by_task = collections.Counter(r.get("task", "?") for r in merged)
    by_teacher = collections.Counter(r.get("teacher", "vault-seed") for r in merged)
    by_lang = collections.Counter(r.get("lang", "en") for r in merged)
    print(f"Merged {len(merged)} verified SFT records (+{len(enriched_only)} enriched) -> {out_path}")
    print(f"  By task   : {dict(by_task.most_common())}")
    print(f"  By teacher: {dict(by_teacher.most_common())}")
    print(f"  By lang   : {dict(by_lang.most_common())}")
    print(f"Merged {len(dpo_rows)} DPO pairs (+{len(new_dpo)} enriched) -> {dpo_out}")
    if rejected:
        print(f"Filtered out invalid records: {dict(rejected)}")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Claude Pro + Gemini Pro dataset enrichment factory.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    ex = sub.add_parser("export", help="Export stratified prompt batches for Claude Pro / Gemini Pro.")
    ex.add_argument("--mode", required=True, choices=sorted(PROMPTS))
    ex.add_argument("--input", default=str(REPO / "tools/ai_training/out/train_sft.jsonl"))
    ex.add_argument("--out", default=str(REPO / "tools/ai_training/out"))
    ex.add_argument("--subdir", default="", help="Optional output subfolder name.")
    ex.add_argument("--offset", type=int, default=0, help="Start offset in stratified pool (for disjoint Claude/Gemini splits).")
    ex.add_argument("--limit", type=int, default=100)
    ex.add_argument("--batch-size", type=int, default=5)

    rc = sub.add_parser("run-claude", help="Run exported batches automatically via local Claude Pro CLI.")
    rc.add_argument("--mode", required=True, choices=sorted(PROMPTS))
    rc.add_argument("--batch-dir", required=True)
    rc.add_argument("--out-jsonl", required=True)
    rc.add_argument("--model", default="", help="Optional Claude model alias (e.g. sonnet, opus).")
    rc.add_argument("--timeout", type=int, default=240)

    mg = sub.add_parser("merge", help="Validate and merge enriched JSONL files with train_sft.jsonl.")
    mg.add_argument("--base", default=str(REPO / "tools/ai_training/out/train_sft.jsonl"))
    mg.add_argument("--inputs", nargs="+", required=True)
    mg.add_argument("--out-file", default=str(REPO / "tools/ai_training/out/train_sft_enriched.jsonl"))
    mg.add_argument("--dpo-base", default=str(REPO / "tools/ai_training/out/train_dpo.jsonl"))
    mg.add_argument("--dpo-out", default=str(REPO / "tools/ai_training/out/train_dpo_enriched.jsonl"))

    args = ap.parse_args(argv)
    if args.cmd == "export":
        return cmd_export(args)
    if args.cmd == "run-claude":
        return cmd_run_claude(args)
    return cmd_merge(args)


if __name__ == "__main__":
    raise SystemExit(main())
