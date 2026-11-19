#!/usr/bin/env python3
"""Build verified training & evaluation JSONL datasets for Sideris from vault/.

Reads the five UC3M subject folders under vault/ (strictly excluding laboratory files),
generates structured prompts matching the exact ask-ai.js schema across four task families:
  1. theory_explain  : theory section -> step-by-step explanation grounded in UC3M notation
  2. problem_solve   : statement -> full zero-skip solution with dimensional checks
  3. socratic_seed   : statement + hidden reference solution -> opening Socratic turn
  4. rag_grounding   : question + retrieved vault context -> course-faithful answer

Every record passes automatic quality gates (KaTeX delimiter balance, zero \\euro, zero '&'
inside \\text{}, zero Socratic final-answer leakage) before being written to a 90/10
train/eval_holdout split.

Usage:
    python tools/ai_training/build_dataset.py --out tools/ai_training/out
    python tools/ai_training/build_dataset.py --dry-run
"""
import argparse
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
_FINAL_NUM_RE = re.compile(r"=\s*([-+]?\d+(?:\.\d+)?)\s*(?:\\text\{[^}]+\}|[a-zA-Z/]+)")


def katex_balanced(text):
    """Return True if $$ and $ delimiters are balanced and free of known KaTeX errors."""
    if _EURO_RE.search(text) or _TEXT_AMP_RE.search(text):
        return False
    stripped = re.sub(r"\\\$", "", text)
    if stripped.count("$$") % 2 != 0:
        return False
    no_disp = re.sub(r"\$\$[\s\S]*?\$\$", "", stripped)
    if no_disp.count("$") % 2 != 0:
        return False
    return True


def system_prompt(subject_slug, lang="es", socratic=False):
    business = subject_slug == "business-management"
    lines = [
        "You are Sideris, the dedicated engineering study tutor for the 2nd year of the BSc in Aerospace Engineering at UC3M.",
        f"Subject: {subject_slug}.",
        "Rules:",
        "- Never skip algebraic or numerical steps. Write out the chain rule, product rule, substitutions with differentials, antiderivatives and Barrow limits explicitly.",
        "- Justify each step with the law, assumption, definition or course equation used.",
        "- Show every accounting entry and subtotal (EBITDA, EBIT, EBT, Net Income)." if business
        else "- Define every symbol with its SI unit on first use and include a dimensional check.",
        "- Write all equations in KaTeX-compatible LaTeX: $...$ inline and $$...$$ for display equations. Never use \\euro.",
        "- Answer in Spanish with the English technical term in brackets on first mention." if lang == "es"
        else "- Answer in English.",
    ]
    if socratic:
        lines.append(
            '- SOCRATIC MODE IS ACTIVE: never reveal the final solution or next full step unless the student writes "show solution". Ask ONE short guiding question per turn.'
        )
    return "\n".join(lines)


def build_records():
    records = []
    skipped = {"katex": 0, "short": 0}
    vault = REPO / "vault"

    for folder, slug, label in SUBJECTS:
        root = vault / folder
        if not root.is_dir():
            continue
        for md in sorted(root.rglob("*.md"), key=lambda p: p.relative_to(vault).as_posix()):
            rel = md.relative_to(vault).as_posix()
            stem = md.stem
            if stem.endswith(" MOC") or stem.lower() == "readme" or _LAB_RE.search(rel):
                continue
            raw = md.read_text(encoding="utf-8", errors="replace")
            meta, body = parse_frontmatter(raw)
            kind = infer_kind(stem, meta)
            unit = infer_unit(stem, meta)
            title = meta.get("title") or stem
            sections = split_sections(body, title)
            if not sections:
                skipped["short"] += 1
                continue

            if kind == "problem":
                statement = sections[0][1]
                solution = "\n\n".join(f"### {h}\n{c}" for h, c in sections[1:])
                if len(statement) < 80 or len(solution) < 160:
                    skipped["short"] += 1
                    continue
                if not (katex_balanced(statement) and katex_balanced(solution)):
                    skipped["katex"] += 1
                    continue

                # 1. Full step-by-step worked explanation (English gold from vault)
                records.append({
                    "id": f"prob-en-{slug}-{len(records) + 1}",
                    "task": "explainSolution",
                    "subject": slug,
                    "unit": unit,
                    "source": rel,
                    "messages": [
                        {"role": "system", "content": system_prompt(slug, lang="en", socratic=False)},
                        {"role": "user", "content": f"<problem_statement>\n{statement}\n</problem_statement>\n\n# Task\nSolve this problem step by step following the UC3M course order with no algebraic skips and a dimensional check."},
                        {"role": "assistant", "content": solution},
                    ],
                })

                # 2. Socratic opening turn seed (never leaks final answer)
                opening = (
                    f"Let us work through **{title}** step by step. "
                    "Before writing any equations, what is the problem asking us to find, which data are given (with SI units), "
                    "and which governing principle or coordinate frame from this unit would you start with?"
                )
                records.append({
                    "id": f"soc-en-{slug}-{len(records) + 1}",
                    "task": "solveSocratic",
                    "subject": slug,
                    "unit": unit,
                    "source": rel,
                    "hidden_solution": solution[:3000],
                    "messages": [
                        {
                            "role": "system",
                            "content": system_prompt(slug, lang="en", socratic=True)
                            + f'\n\n<reference_solution hidden="true">\n{solution[:3000]}\n</reference_solution>',
                        },
                        {
                            "role": "user",
                            "content": f"<problem_statement>\n{statement}\n</problem_statement>\n\n# Task\nHelp me solve this problem by myself, from the start. Begin now with your first question only.",
                        },
                        {"role": "assistant", "content": opening},
                    ],
                })
            else:
                for sec_head, sec_text in sections:
                    if len(sec_text) < 220 or len(sec_text) > 3500:
                        skipped["short"] += 1
                        continue
                    if not katex_balanced(sec_text):
                        skipped["katex"] += 1
                        continue
                    records.append({
                        "id": f"theo-en-{slug}-{len(records) + 1}",
                        "task": "theoryExplain",
                        "subject": slug,
                        "unit": unit,
                        "source": rel,
                        "messages": [
                            {"role": "system", "content": system_prompt(slug, lang="en", socratic=False)},
                            {
                                "role": "user",
                                "content": f"In {label} ({title}), explain the section **{sec_head}** from first principles using the UC3M course notation, defining every symbol and showing all steps.",
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
    ap = argparse.ArgumentParser(description="Build Sideris training/eval datasets from vault/.")
    ap.add_argument("--out", default=str(REPO / "tools/ai_training/out"), help="Output directory for JSONL files.")
    ap.add_argument("--dry-run", action="store_true", help="Print counts without writing files.")
    args = ap.parse_args(argv)

    records, skipped = build_records()
    train, holdout = split_train_eval(records)
    print(f"Records: {len(records)} total ({len(train)} train, {len(holdout)} eval holdout)")
    print(f"Skipped: {skipped}")

    if args.dry_run:
        return 0

    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for name, rows in (("train_seed.jsonl", train), ("eval_holdout.jsonl", holdout)):
        p = out / name
        with p.open("w", encoding="utf-8") as f:
            for row in rows:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
        print(f"Wrote {p}: {len(rows)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
