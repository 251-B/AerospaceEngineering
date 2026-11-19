#!/usr/bin/env python3
"""Sideris Dataset Factory v2 — Exhaustive multi-task extractor from vault/.

Extracts and sanitises verified UC3M Aerospace Engineering training datasets across all five
subjects (strictly excluding laboratory files), aligned 1-to-1 with AGENTS.md and ask-ai.js:

  1. problem_solve     : individual solved problems + paired Engineering Mechanics
                         Problem Set <-> Solution Set (51 official problems)
  2. socratic_multiturn: multi-turn Socratic dialogues built from hand-written
                         Hint / Checkpoint / Solution triplets (never leaks hidden solution)
  3. quiz_mcq_tutor    : ~620 Aerospace Materials I MCQs with right + wrong option diagnostics
  4. derive_principles : > [!derivation] callouts and Formula Sheet | Step | Why | tables
  5. theory_explain    : cleaned theory sections & > [!summary] What you need to know blocks
  6. dpo_pairs.jsonl   : preference pairs (chosen = canonical UC3M rigour, rejected = Phase N
                         labels, skipped algebra, Socratic leaks or broken KaTeX)
  7. grpo_prompts.jsonl: prompts + metadata for deterministic SymPy/KaTeX/Socratic GRPO RL

Data hygiene enforced automatically:
  - Strips legacy "Phase 1..4" labels and emojis from older vault notes so Sideris never learns them.
  - Strips Obsidian wikilinks, embeds, and "Related Notes" footers.
  - Rejects any sample with unbalanced KaTeX ($ / $$), \\euro, or '&' inside \\text{}.
  - Deterministic 90/10 file-grouped split (train_sft.jsonl / eval_holdout.jsonl) so no problem
    leaks between training and evaluation.

Usage:
    python tools/ai_training/build_dataset.py --out tools/ai_training/out
    python tools/ai_training/build_dataset.py --dry-run
"""
import argparse
import collections
import hashlib
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools"))

from build_ai_index import SUBJECTS, _LAB_RE, clean_markdown, infer_kind, infer_unit, parse_frontmatter, split_sections  # noqa: E402

_EURO_RE = re.compile(r"\\euro\b")
_TEXT_AMP_RE = re.compile(r"\\text\{[^}]*&[^}]*\}")
_EMOJI_RE = re.compile("[\U0001f000-\U0001faff\u2600-\u27bf\u2b00-\u2bff\ufe0f]")
_PHASE_PREFIX_RE = re.compile(
    r"\b(?:Phase\s*[1-4]\s*[:\-–—.]?\s*|(?:\(\s*Phase\s*[1-4]\s*\))|First\s+phase\s*[:\-–—.]?\s*|"
    r"Second\s+phase\s*[:\-–—.]?\s*|Third\s+phase\s*[:\-–—.]?\s*|Fourth\s+phase\s*[:\-–—.]?\s*)",
    re.I,
)
_RELATED_HEAD_RE = re.compile(r"^(?:related\s+(?:notes|links|concepts)|enlaces\s+relacionados|see\s+also)\b", re.I)
_DERIV_CALLOUT_RE = re.compile(
    r"^>\s*\[!derivation\][+-]?\s*(.*?)\n((?:^>.*(?:\n|$))+)",
    re.M | re.I,
)
_SUMMARY_CALLOUT_RE = re.compile(
    r"^>\s*\[!summary\][+-]?\s*(.*?)\n((?:^>.*(?:\n|$))+)",
    re.M | re.I,
)
_MCQ_BLOCK_RE = re.compile(r"^##\s+(Q\d+\.\d+)\s+(.+?)\s*$", re.M)
_PROB_NUM_RE = re.compile(r"^##\s+Problem\s+(\d+)\b(.*)$", re.M | re.I)
_SUBQ_PART_RE = re.compile(r"^##\s+(?:Part\s*\(?[a-h]\)?|Question\s*\d+|Subquestion\s*\d+)", re.M | re.I)


def sanitise_text(text):
    """Enforce AGENTS.md hygiene: no emojis, no legacy Phase 1..4 labels, clean whitespace."""
    text = clean_markdown(text)
    text = _EMOJI_RE.sub("", text)
    text = _PHASE_PREFIX_RE.sub("", text)
    text = re.sub(r"^(#{1,4})\s*\d+\.\s*", r"\1 ", text, flags=re.M)
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def katex_balanced(text):
    """Return True if $$ and $ delimiters are balanced and free of known KaTeX errors."""
    if not text or _EURO_RE.search(text) or _TEXT_AMP_RE.search(text):
        return False
    stripped = re.sub(r"\\\$", "", text)
    if stripped.count("$$") % 2 != 0:
        return False
    no_disp = re.sub(r"\$\$[\s\S]*?\$\$", "", stripped)
    return no_disp.count("$") % 2 == 0


def system_prompt(subject_slug, lang="en", socratic=False):
    business = subject_slug == "business-management"
    lines = [
        "You are Sideris, the dedicated engineering study tutor for the 2nd year of the BSc in Aerospace Engineering at UC3M.",
        f"Subject: {subject_slug}.",
        "Rules:",
        "- Follow the UC3M lecturer's order for this subject as one continuous academic development. Never use 'Phase 1..4' labels or emojis.",
        "- Never skip algebraic or numerical steps. Write out the chain rule, product rule, substitutions with differentials, antiderivatives and Barrow limits explicitly.",
        "- Justify each step with the law, assumption, definition or official course equation used.",
        "- Show every accounting entry, EBITDA -> EBIT -> EBT -> Net Income cascade and balance sheet reconciliation." if business
        else "- Define every symbol with its SI unit on first use, justify every sine/cosine and sign, and include a dimensional check and limiting cases.",
        "- Write all equations in KaTeX-compatible LaTeX: $...$ inline and $$...$$ for display equations. Never use \\euro.",
        "- If an official key disagrees with the verified derivation, keep the verified value and flag the discrepancy transparently.",
        "- Answer in Spanish with the English technical term in brackets on first mention." if lang == "es"
        else "- Answer in English.",
    ]
    if socratic:
        lines.append(
            '- SOCRATIC MODE IS ACTIVE: never reveal the final solution or the next full step unless the student writes "show solution". Ask ONE short guiding question per turn.'
        )
    return "\n".join(lines)


def extract_callout_blocks(body, regex):
    out = []
    for m in regex.finditer(body):
        title = sanitise_text(m.group(1))
        raw_lines = [re.sub(r"^>\s?", "", ln) for ln in m.group(2).splitlines()]
        content = sanitise_text("\n".join(raw_lines))
        if len(content) >= 140 and katex_balanced(content):
            out.append((title, content))
    return out


def extract_quiz_bank(body, slug, unit, rel, title):
    """Parse Aerospace Materials I Midterm 2 10-question quiz blocks into diagnostic tutor records."""
    records = []
    matches = list(_MCQ_BLOCK_RE.finditer(body))
    for i, m in enumerate(matches):
        qid = m.group(1)
        qtitle = sanitise_text(m.group(2))
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        chunk = body[m.end():end]
        ans_m = re.search(r"###\s*Answer\s*\n+([^\n#]+)", chunk, re.I)
        exp_m = re.search(r"###\s*Explanation\s*\n+([\s\S]+?)(?=\n###\s|\Z)", chunk, re.I)
        src_m = re.search(r"###\s*Source\s*\n+([^\n#]+)", chunk, re.I)
        stem_part = chunk[:ans_m.start()] if ans_m else ""
        # Strip metadata lines like - id:, - concept_id:, - calc:, - check:
        stem_clean = "\n".join(
            ln for ln in stem_part.splitlines()
            if not re.match(r"^\s*-\s*(?:id|concept_id|format|asks|calc|check)\s*:", ln, re.I)
        )
        stem_clean = sanitise_text(stem_clean)
        if not (ans_m and exp_m and len(stem_clean) >= 60):
            continue
        ans = sanitise_text(ans_m.group(1))
        exp = sanitise_text(exp_m.group(1))
        src = sanitise_text(src_m.group(1)) if src_m else ""
        full_reply = f"**Correct option:** {ans}\n\n{exp}" + (f"\n\n**Course source:** {src}" if src else "")
        if not (katex_balanced(stem_clean) and katex_balanced(full_reply)):
            continue
        records.append({
            "id": f"mcq-{slug}-{qid.lower()}-{len(records) + 1}",
            "task": "quiz_mcq_tutor",
            "subject": slug,
            "unit": unit,
            "source": rel,
            "messages": [
                {"role": "system", "content": system_prompt(slug, lang="en", socratic=False)},
                {
                    "role": "user",
                    "content": f"<question id=\"{qid}\" title=\"{qtitle}\">\n{stem_clean}\n</question>\n\n# Task\nGive the right option, justify it from the UC3M course material, and explain the exact mistake behind every wrong option.",
                },
                {"role": "assistant", "content": full_reply},
            ],
        })
    return records


def extract_bank_problem_socratic(body, slug, unit, rel, title):
    """Build multi-turn Socratic & full-solution records from Problem Bank notes with Hint/Checkpoint/Solution."""
    records = []
    stmt_m = re.search(r"^##\s*(?:Official\s+)?Statement\s*\n+([\s\S]+?)(?=\n##\s|\Z)", body, re.M | re.I)
    if not stmt_m:
        return records
    statement = sanitise_text(stmt_m.group(1))
    if len(statement) < 80 or not katex_balanced(statement):
        return records

    hint_m = re.search(r"###\s*Hint\s*\n+([\s\S]+?)(?=\n###\s|\n##\s|\Z)", body, re.I)
    chk_m = re.search(r"###\s*Checkpoint\s*\n+([\s\S]+?)(?=\n###\s|\n##\s|\Z)", body, re.I)
    sol_m = re.search(r"###\s*Solution\s*\n+([\s\S]+?)(?=\n##\s|\Z)", body, re.I)
    if not (hint_m and sol_m):
        return records

    hint = sanitise_text(hint_m.group(1))
    checkpoint = sanitise_text(chk_m.group(1)) if chk_m else ""
    solution = sanitise_text(sol_m.group(1))
    if len(hint) < 30 or len(solution) < 120:
        return records
    if not (katex_balanced(hint) and katex_balanced(solution) and (not checkpoint or katex_balanced(checkpoint))):
        return records

    # Multi-turn Socratic dialogue using real hand-written Hint & Checkpoint!
    turns = [
        {
            "role": "system",
            "content": system_prompt(slug, lang="en", socratic=True)
            + f'\n\n<reference_solution hidden="true">\n{solution[:3200]}\n</reference_solution>',
        },
        {
            "role": "user",
            "content": f"<problem_statement>\n{statement}\n</problem_statement>\n\n# Task\nHelp me solve this problem by myself, from the start. Begin now with your first question only.",
        },
        {
            "role": "assistant",
            "content": f"Let us work through **{title}** together. Before writing any equation, what are the given data (with SI units), what are the unknowns, and which governing principle or reference frame from this unit should we set up first?",
        },
        {
            "role": "user",
            "content": "I am stuck on how to start — can you give me a hint without solving it?",
        },
        {
            "role": "assistant",
            "content": f"Here is a focused hint to get you moving:\n\n{hint}\n\nUsing that idea, what is the first equation or setup you would write?",
        },
    ]
    if checkpoint:
        turns.extend([
            {
                "role": "user",
                "content": "How can I check if my intermediate setup is on the right track before computing the final answer?",
            },
            {
                "role": "assistant",
                "content": f"Verify your intermediate quantities against this checkpoint:\n\n{checkpoint}\n\nDo your units and signs match so far? If yes, go ahead with the next algebraic step.",
            },
        ])
    records.append({
        "id": f"soc-mt-{slug}-{len(records) + 1}-{hashlib.md5(rel.encode()).hexdigest()[:6]}",
        "task": "socratic_multiturn",
        "subject": slug,
        "unit": unit,
        "source": rel,
        "messages": turns,
    })
    return records


def extract_mechanics_paired_sets(vault):
    """Pair Engineering Mechanics Problem Set - Topic N with Solution Set - Topic N (51 official problems)."""
    records = []
    mech_dir = vault / "03 - Engineering Mechanics"
    if not mech_dir.is_dir():
        return records

    prob_files = {infer_unit(p.stem, {}): p for p in sorted(mech_dir.glob("Problem Set - Topic *.md"))}
    sol_files = {infer_unit(p.stem, {}): p for p in sorted(mech_dir.glob("Solution Set - Topic *.md"))}

    for unit, s_path in sorted(sol_files.items()):
        p_path = prob_files.get(unit)
        if not p_path:
            continue
        p_body = parse_frontmatter(p_path.read_text(encoding="utf-8", errors="replace"))[1]
        s_body = parse_frontmatter(s_path.read_text(encoding="utf-8", errors="replace"))[1]

        def split_by_prob(text):
            out = {}
            ms = list(_PROB_NUM_RE.finditer(text))
            for idx, m in enumerate(ms):
                num = int(m.group(1))
                end = ms[idx + 1].start() if idx + 1 < len(ms) else len(text)
                out[num] = (sanitise_text(m.group(2).lstrip(":-— ")), sanitise_text(text[m.end():end]))
            return out

        probs = split_by_prob(p_body)
        sols = split_by_prob(s_body)
        rel = s_path.relative_to(vault).as_posix()

        for num, (ptitle, stmt) in sorted(probs.items()):
            if num not in sols:
                continue
            stitle, sol = sols[num]
            if len(stmt) < 60 or len(sol) < 200 or len(sol) > 12000:
                continue
            if not (katex_balanced(stmt) and katex_balanced(sol)):
                continue
            label = ptitle or stitle or f"Problem {num}"
            records.append({
                "id": f"mech-official-t{unit}-p{num:02d}",
                "task": "problem_solve",
                "subject": "engineering-mechanics",
                "unit": unit,
                "source": rel,
                "messages": [
                    {"role": "system", "content": system_prompt("engineering-mechanics", lang="en", socratic=False)},
                    {
                        "role": "user",
                        "content": f"<problem_statement id=\"Problem {num}\" title=\"{label}\">\n{stmt}\n</problem_statement>\n\n# Task\nSolve this official Engineering Mechanics problem step by step in the UC3M lecturer's order (frames and bases, change of basis and position vector, kinematics, forces if applicable, answers and checks) with zero algebraic skips.",
                    },
                    {"role": "assistant", "content": sol},
                ],
            })
    return records


def make_dpo_pairs(sft_records):
    """Synthesise high-signal DPO preference pairs from clean gold records."""
    pairs = []
    for rec in sft_records:
        msgs = rec["messages"]
        if len(msgs) < 3:
            continue
        chosen = msgs[-1]["content"]
        prompt = msgs[:-1]

        if rec["task"] == "problem_solve" and len(chosen) >= 400:
            # Rejected variant 1: injects legacy Phase labels + algebraic skip!
            first_para = chosen.split("\n\n")[0]
            rejected = (
                "### Phase 1: Setup\n"
                + first_para[:260]
                + "\n\n### Phase 2: Solution\nAfter some algebra, it can be shown that we directly obtain the final result. "
                "The remaining steps are trivial and left as an exercise."
            )
            pairs.append({
                "id": f"dpo-rigour-{rec['id']}",
                "category": "no_skip_and_no_phase_labels",
                "subject": rec["subject"],
                "source": rec["source"],
                "prompt": prompt,
                "chosen": [{"role": "assistant", "content": chosen}],
                "rejected": [{"role": "assistant", "content": rejected}],
            })
        elif rec["task"] in ("socratic_multiturn", "socratic_seed"):
            # Rejected variant 2: leaks the hidden solution immediately in Socratic mode!
            hidden = rec.get("hidden_solution") or ""
            leak_snip = hidden[:320].strip() if hidden else "The final answer follows directly by substituting the data into the main equation and solving."
            rejected = f"Here is the complete solution right away so you can check it:\n\n{leak_snip}"
            pairs.append({
                "id": f"dpo-socratic-{rec['id']}",
                "category": "socratic_no_leak",
                "subject": rec["subject"],
                "source": rec["source"],
                "prompt": prompt,
                "chosen": [{"role": "assistant", "content": chosen}],
                "rejected": [{"role": "assistant", "content": rejected}],
            })
    return pairs


def make_grpo_prompts(sft_records):
    """Build deterministic GRPO prompt set paired with metadata for rewards.py."""
    prompts = []
    for rec in sft_records:
        if rec["task"] not in ("problem_solve", "socratic_seed", "socratic_multiturn", "derive_principles"):
            continue
        is_soc = rec["task"].startswith("socratic")
        msgs = rec["messages"]
        gold = msgs[-1]["content"]
        boxed = re.findall(r"\\boxed\{([^{}]+(?:\{[^{}]*\}[^{}]*)*)\}", gold)
        forbid = ""
        if is_soc:
            hid = rec.get("hidden_solution", "")
            m = re.search(r"\\boxed\{([^{}]+)\}", hid)
            forbid = m.group(1).strip() if m else ""
        prompts.append({
            "id": f"grpo-{rec['id']}",
            "task": rec["task"],
            "subject": rec["subject"],
            "source": rec["source"],
            "prompt": msgs[:-1],
            "socratic": is_soc,
            "expected_answer": boxed[-1].strip() if boxed else "",
            "forbidden_answers": forbid,
        })
    return prompts


def build_all():
    vault = REPO / "vault"
    records = []
    skipped = collections.Counter()

    # 1. Paired Engineering Mechanics official Problem Sets <-> Solution Sets
    records.extend(extract_mechanics_paired_sets(vault))

    # 2. Walk all 5 subject folders
    for folder, slug, label in SUBJECTS:
        root = vault / folder
        if not root.is_dir():
            continue
        for md in sorted(root.rglob("*.md"), key=lambda p: p.relative_to(vault).as_posix()):
            rel = md.relative_to(vault).as_posix()
            stem = md.stem
            if stem.endswith(" MOC") or stem.lower() == "readme" or _LAB_RE.search(rel):
                continue
            if stem.startswith(("Problem Set -", "Solution Set -", "Rules -")):
                continue

            raw = md.read_text(encoding="utf-8", errors="replace")
            meta, body = parse_frontmatter(raw)
            kind = infer_kind(stem, meta)
            unit = infer_unit(stem, meta)
            title = sanitise_text(meta.get("title") or stem)

            # A. Materials Midterm 2 Quiz Bank blocks (10 MCQs each)
            if stem.startswith("Quiz - Bank "):
                records.extend(extract_quiz_bank(body, slug, unit, rel, title))
                continue

            # B. Problem Bank multi-turn Socratic dialogues (Hint / Checkpoint / Solution)
            if "Problem Bank/" in rel and stem.startswith("Problem - Bank "):
                records.extend(extract_bank_problem_socratic(body, slug, unit, rel, title))

            # C. Explicit > [!derivation] and > [!summary] callouts (gold for derive & simple)
            for idx, (dtitle, dtext) in enumerate(extract_callout_blocks(body, _DERIV_CALLOUT_RE), 1):
                if len(dtext) > 3600:
                    continue
                records.append({
                    "id": f"deriv-{slug}-{hashlib.md5(rel.encode()).hexdigest()[:6]}-{idx}",
                    "task": "derive_principles",
                    "subject": slug,
                    "unit": unit,
                    "source": rel,
                    "messages": [
                        {"role": "system", "content": system_prompt(slug, lang="en", socratic=False)},
                        {
                            "role": "user",
                            "content": f"In {label} ({title}), derive **{dtitle or 'this result'}** step by step from first principles with no algebraic skips, justifying every step.",
                        },
                        {"role": "assistant", "content": dtext},
                    ],
                })

            for idx, (stitle, stext) in enumerate(extract_callout_blocks(body, _SUMMARY_CALLOUT_RE), 1):
                records.append({
                    "id": f"ess-{slug}-{hashlib.md5(rel.encode()).hexdigest()[:6]}-{idx}",
                    "task": "essential_summary",
                    "subject": slug,
                    "unit": unit,
                    "source": rel,
                    "messages": [
                        {"role": "system", "content": system_prompt(slug, lang="en", socratic=False)},
                        {
                            "role": "user",
                            "content": f"Give a clear, plain-language summary of what I need to know for **{stitle or title}** in {label}, defining every symbol.",
                        },
                        {"role": "assistant", "content": stext},
                    ],
                })

            # D. Section-level extraction for problems and theory notes
            raw_sections = split_sections(body, title)
            sections = [
                (sanitise_text(h), sanitise_text(c))
                for h, c in raw_sections
                if not _RELATED_HEAD_RE.match(sanitise_text(h))
            ]
            if not sections:
                skipped["short"] += 1
                continue

            if kind == "problem":
                statement = sections[0][1]
                sol_parts = [f"### {h}\n{c}" for h, c in sections[1:] if len(c) >= 40]
                solution = "\n\n".join(sol_parts)
                if len(statement) < 80 or len(solution) < 180 or len(solution) > 12000:
                    skipped["short_or_long"] += 1
                    continue
                if not (katex_balanced(statement) and katex_balanced(solution)):
                    skipped["katex"] += 1
                    continue

                rec_id = f"prob-{slug}-{hashlib.md5(rel.encode()).hexdigest()[:8]}"
                records.append({
                    "id": rec_id,
                    "task": "problem_solve",
                    "subject": slug,
                    "unit": unit,
                    "source": rel,
                    "messages": [
                        {"role": "system", "content": system_prompt(slug, lang="en", socratic=False)},
                        {
                            "role": "user",
                            "content": f"<problem_statement title=\"{title}\">\n{statement}\n</problem_statement>\n\n# Task\nSolve this problem step by step following the UC3M course order with zero algebraic skips, justified equations and a dimensional check.",
                        },
                        {"role": "assistant", "content": solution},
                    ],
                })

                opening = (
                    f"Let us solve **{title}** step by step. "
                    "Before writing any equation, what is the problem asking for, which data are given (with SI units), "
                    "and which governing principle or coordinate frame from this unit should we use first?"
                )
                records.append({
                    "id": f"soc-{slug}-{hashlib.md5(rel.encode()).hexdigest()[:8]}",
                    "task": "socratic_seed",
                    "subject": slug,
                    "unit": unit,
                    "source": rel,
                    "hidden_solution": solution[:3200],
                    "messages": [
                        {
                            "role": "system",
                            "content": system_prompt(slug, lang="en", socratic=True)
                            + f'\n\n<reference_solution hidden="true">\n{solution[:3200]}\n</reference_solution>',
                        },
                        {
                            "role": "user",
                            "content": f"<problem_statement title=\"{title}\">\n{statement}\n</problem_statement>\n\n# Task\nHelp me solve this problem by myself, from the start. Begin now with your first question only.",
                        },
                        {"role": "assistant", "content": opening},
                    ],
                })
            else:
                for sec_idx, (sec_head, sec_text) in enumerate(sections, 1):
                    if len(sec_text) < 220 or len(sec_text) > 3800:
                        skipped["short_or_long"] += 1
                        continue
                    if not katex_balanced(sec_text):
                        skipped["katex"] += 1
                        continue
                    records.append({
                        "id": f"theo-{slug}-{hashlib.md5(rel.encode()).hexdigest()[:6]}-{sec_idx}",
                        "task": "theory_explain",
                        "subject": slug,
                        "unit": unit,
                        "source": rel,
                        "messages": [
                            {"role": "system", "content": system_prompt(slug, lang="en", socratic=False)},
                            {
                                "role": "user",
                                "content": f"In {label} ({title}), explain **{sec_head}** from first principles using the UC3M course notation, defining every symbol and showing all steps.",
                            },
                            {"role": "assistant", "content": sec_text},
                        ],
                    })

    return records, skipped


def split_train_eval(records, eval_mod=10):
    train, holdout = [], []
    for rec in records:
        h = int(hashlib.sha256(rec["source"].encode("utf-8")).hexdigest()[:8], 16)
        if h % eval_mod == 0:
            holdout.append(rec)
        else:
            train.append(rec)
    return train, holdout


def main(argv=None):
    ap = argparse.ArgumentParser(description="Build Sideris v2 SFT, DPO and GRPO datasets from vault/.")
    ap.add_argument("--out", default=str(REPO / "tools/ai_training/out"), help="Output directory for JSONL files.")
    ap.add_argument("--dry-run", action="store_true", help="Print breakdown without writing files.")
    args = ap.parse_args(argv)

    records, skipped = build_all()
    train, holdout = split_train_eval(records)
    dpo_pairs = make_dpo_pairs(train)
    grpo_prompts = make_grpo_prompts(train)

    by_task = collections.Counter(r["task"] for r in records)
    by_subj = collections.Counter(r["subject"] for r in records)
    print(f"SFT Records : {len(records)} total ({len(train)} train, {len(holdout)} eval holdout)")
    print(f"  By task   : {dict(by_task.most_common())}")
    print(f"  By subject: {dict(by_subj.most_common())}")
    print(f"DPO Pairs   : {len(dpo_pairs)}")
    print(f"GRPO Prompts: {len(grpo_prompts)}")
    print(f"Skipped     : {dict(skipped)}")

    if args.dry_run:
        return 0

    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    outputs = (
        ("train_sft.jsonl", train),
        ("eval_holdout.jsonl", holdout),
        ("train_dpo.jsonl", dpo_pairs),
        ("train_grpo.jsonl", grpo_prompts),
    )
    for name, rows in outputs:
        p = out / name
        with p.open("w", encoding="utf-8") as f:
            for row in rows:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
        print(f"Wrote {p}: {len(rows)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
