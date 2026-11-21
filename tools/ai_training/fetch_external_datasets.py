#!/usr/bin/env python3
"""External STEM & Finance Dataset Harvester for Sideris v2+.

Downloads open, verified datasets from Hugging Face, maps rows strictly onto the
five 2nd-year UC3M Aerospace Engineering subjects, normalises LaTeX into KaTeX,
enforces Sideris quality & anti-contamination gates, and optionally builds an
upgraded `tools/ai_training/out/sideris-data-v2.zip`.

Usage:
    python tools/ai_training/fetch_external_datasets.py --per-subject 400 --build-v2-zip
    python tools/ai_training/fetch_external_datasets.py --sources camel-physics,camel-math --dry-run
"""
import argparse
import collections
import hashlib
import json
import pathlib
import re
import sys
import zipfile

import pyarrow.parquet as pq
import requests

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools/ai_training"))

from build_dataset import (  # noqa: E402
    _EMOJI_RE,
    katex_balanced,
    make_dpo_pairs,
    make_grpo_prompts,
    sanitise_text,
    system_prompt,
)
import rewards  # noqa: E402

SUBJECT_LIST = (
    "fluid-mechanics",
    "aerospace-materials-1",
    "engineering-mechanics",
    "advanced-maths",
    "business-management",
)

SOURCES = {
    "camel-physics": {
        "url": "https://huggingface.co/datasets/camel-ai/physics/resolve/main/physics.zip",
        "filename": "camel_physics.zip",
        "kind": "zip",
    },
    "camel-math": {
        "url": "https://huggingface.co/datasets/camel-ai/math/resolve/main/math.zip",
        "filename": "camel_math.zip",
        "kind": "zip",
    },
    "camel-chemistry": {
        "url": "https://huggingface.co/datasets/camel-ai/chemistry/resolve/main/chemistry.zip",
        "filename": "camel_chemistry.zip",
        "kind": "zip",
    },
    "scibench": {
        "url": "https://huggingface.co/datasets/xw27/scibench/resolve/refs%2Fconvert%2Fparquet/default/train/0000.parquet",
        "filename": "scibench_train.parquet",
        "kind": "parquet",
    },
    "finance-alpaca": {
        "url": "https://huggingface.co/datasets/gbharti/finance-alpaca/resolve/main/Cleaned_date.json",
        "filename": "finance_alpaca.json",
        "kind": "json",
    },
}

_DISPLAY_BRACKET_RE = re.compile(r"(?<!\\)\\\[([\s\S]*?)(?<!\\)\\\]")
_INLINE_PAREN_RE = re.compile(r"(?<!\\)\\\(([\s\S]*?)(?<!\\)\\\)")
_EQUATION_ENV_RE = re.compile(r"\\begin\{equation\*?\}([\s\S]*?)\\end\{equation\*?\}")
_BOXED_RE = re.compile(r"\\boxed\{([^{}]+(?:\{[^{}]*\}[^{}]*)*)\}")

_FIGURE_RE = re.compile(
    r"\b(?:shown in the figure|see figure|in the figure|shown in the diagram|"
    r"in the image|graph below|attached figure|attached image|diagram below)\b",
    re.I,
)
_TABLE_BELOW_RE = re.compile(r"\btable below\b", re.I)
_REFUSAL_RE = re.compile(
    r"(?:\bas an ai\b|\bcannot be determined\b|\bnot enough information\b|"
    r"\bi cannot\b|\bsorry,\b|\bplease provide\b|\bi don't have access\b|\bunable to determine\b)",
    re.I,
)
_SI_HINT_RE = re.compile(
    r"(?:\\mathrm\{|\\text\{|\b(?:kg|m/s|m/s\^2|Pa|kPa|MPa|GPa|J|kJ|W|kW|N|Hz|mol|K|rad/s)\b)"
)
_STEP_MARKER_RE = re.compile(r"(?:^###\s|\bstep\s+1\b|^\s*1\.\s|\btherefore\b|\bfirst,\b)", re.I | re.M)

_PHYS_REJECT_RE = re.compile(
    r"\b(?:quantum|particle physics|nuclear|astrophysics|cosmology|relativity|optics|photonics|"
    r"electromagnetism|electrostatics|magnetostatics|electric circuits?|atomic physics|"
    r"molecular physics|plasma|fermi|bloch|superconduct|schr[oö]dinger|dirac|higgs)\b",
    re.I,
)
_FLUID_RE = re.compile(
    r"\b(?:fluid mechanics|fluid dynamics|hydrostatics?|aerodynamics?|compressible flow|"
    r"boundary layer|pipe flow|bernoulli|navier[- ]stokes|reynolds|viscosity|buoyancy|"
    r"archimedes|venturi|poiseuille|laminar|turbulent|drag force|lift force|mach number|"
    r"isentropic|stagnation pressure|streamline|continuity equation|enthalpy|carnot)\b",
    re.I,
)
_MATERIALS_RE = re.compile(
    r"\b(?:solid state|condensed matter|crystal(?:lography|\s+structure)?|elasticity|"
    r"stress[- ]strain|young'?s modulus|thermal expansion|dislocation|fatigue|creep|"
    r"fracture|polymer|composite|brittle|ductile|lattice|metallurgy|alloy|phase diagram|"
    r"eutectic|diffusion|fick'?s law|corrosion|galvanic|passivation|ceramic|fcc|bcc|hcp|"
    r"unit cell|bravais|packing factor|miller indices)\b",
    re.I,
)
_MECH_RE = re.compile(
    r"\b(?:classical mechanics|rigid body|kinematics|dynamics|rotational|moment of inertia|"
    r"lagrang(?:e|ian)|coriolis|angular momentum|torque|oscillations?|vibrations?|statics|"
    r"work[- ]energy|impulse|centrifugal|centripetal|pendulum|projectile|collision|"
    r"conservation of momentum|newton'?s\s+(?:second|laws?)|euler'?s equations?)\b",
    re.I,
)

_MATH_REJECT_RE = re.compile(
    r"\b(?:number theory|combinatorics|graph theory|topology|abstract algebra|group theory|"
    r"ring theory|field theory|galois|symbolic logic|set theory|elementary arithmetic|"
    r"cryptography|game theory|probability|statistics)\b",
    re.I,
)
_MATH_ACCEPT_RE = re.compile(
    r"\b(?:calculus|differential equation|ode|pde|laplace|fourier|vector calculus|"
    r"multivariable|linear algebra|eigenvalue|eigenvector|matri(?:x|ces)|complex analysis|"
    r"residue|cauchy|series|taylor|maclaurin|green'?s theorem|stokes|gauss|divergence|"
    r"curl|gradient|jacobian|hessian|integral|partial derivative|ordinary differential)\b",
    re.I,
)

_CHEM_REJECT_RE = re.compile(
    r"\b(?:organic chemistry|naming organic|organic synthesis|biochemistry|medicinal|"
    r"pharmaceutical|environmental|analytical chemistry|titration|spectroscopy|"
    r"stereochemistry|alkanes?|alkenes?|alkynes?|amines?|carboxylic|iupac name)\b",
    re.I,
)
_CHEM_ACCEPT_RE = re.compile(
    r"\b(?:materials chemistry|solid state|polymer|crystal|lattice|fcc|bcc|hcp|alloy|"
    r"phase diagram|eutectic|diffusion|fick|corrosion|galvanic|passivation|ceramic|"
    r"composite|metallic bond|ionic bond|covalent|crystallography|electrochemistry|"
    r"nernst|miller|bravais|unit cell|packing factor)\b",
    re.I,
)

_FIN_REJECT_RE = re.compile(
    r"\b(?:car loan|auto loan|scam|credit card|mortgage|crypto|bitcoin|ethereum|nft|"
    r"401k|roth|ira\b|student loan|tax return|irs\b|personal budget|credit score|"
    r"stock pick|day trading|forex|robinhood|insurance policy|divorce|bankruptcy|car deal|"
    r"quintile|wealth exceeds|income inequality|macroeconomic|federal reserve|inflation rate)\b",
    re.I,
)
_SCIBENCH_PHOTOCHEM_RE = re.compile(
    r"\b(?:photochemically|photon energy|cyclohexadiene|reactant|wavelength|molarity)\b",
    re.I,
)
_FIN_ACCEPT_RE = re.compile(
    r"\b(?:balance sheet|income statement|ebitda|ebit\b|net income|cash flow statement|"
    r"depreciation|amortization|npv|net present value|irr|internal rate of return|wacc|"
    r"break-even|contribution margin|return on equity|return on assets|current ratio|"
    r"quick ratio|debt-to-equity|working capital|journal entry|double-entry|"
    r"cost of goods sold|gross margin|operating margin|financial leverage|capital budgeting|"
    r"payback period|discount rate|solvency|fixed cost|variable cost|operating income|"
    r"shareholders'? equity|retained earnings|accounts receivable|accounts payable)\b",
    re.I,
)
_FIN_QUANT_RE = re.compile(r"(?:\$|%|=|\b(?:EBITDA|EBIT|NPV|IRR|WACC)\b)")


def norm_text_hash(text):
    """Return MD5 hex digest of lowercase alphanumeric content for deduplication."""
    norm = re.sub(r"[^a-z0-9]+", "", str(text or "").lower())
    return hashlib.md5(norm.encode("utf-8")).hexdigest()


def normalise_external_latex(text):
    """Convert \\[...\\], \\(...\\), and equation environments into KaTeX delimiters and sanitise."""
    if not text:
        return ""
    s = str(text)
    s = _EQUATION_ENV_RE.sub(lambda m: f"\n$$\n{m.group(1).strip()}\n$$\n", s)
    s = _DISPLAY_BRACKET_RE.sub(lambda m: f"\n$$\n{m.group(1).strip()}\n$$\n", s)
    s = _INLINE_PAREN_RE.sub(lambda m: f"${m.group(1).strip()}$", s)
    return sanitise_text(s)


def download_if_needed(url, dest_path):
    """Stream-download url to dest_path unless already cached cleanly."""
    dest = pathlib.Path(dest_path)
    if dest.is_file() and dest.stat().st_size > 0:
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    part = dest.with_suffix(dest.suffix + ".part")
    with requests.get(url, stream=True, timeout=60) as resp:
        resp.raise_for_status()
        with part.open("wb") as f:
            for chunk in resp.iter_content(chunk_size=1 << 20):
                if chunk:
                    f.write(chunk)
    part.replace(dest)
    return dest


def _iter_zip_records(zip_path):
    with zipfile.ZipFile(zip_path) as zf:
        for name in sorted(zf.namelist()):
            low = name.lower()
            if name.endswith("/") or not (low.endswith(".json") or low.endswith(".jsonl")):
                continue
            raw_bytes = zf.read(name).decode("utf-8", errors="replace")
            if low.endswith(".jsonl"):
                for line in raw_bytes.splitlines():
                    s = line.strip()
                    if s:
                        yield json.loads(s)
            else:
                obj = json.loads(raw_bytes)
                if isinstance(obj, list):
                    for item in obj:
                        if isinstance(item, dict):
                            yield item
                elif isinstance(obj, dict):
                    yield obj


def _iter_source_records(source_name, path):
    kind = SOURCES[source_name]["kind"]
    if kind == "zip":
        yield from _iter_zip_records(path)
    elif kind == "parquet":
        for row in pq.read_table(path).to_pylist():
            yield row
    elif kind == "json":
        data = json.loads(pathlib.Path(path).read_text(encoding="utf-8", errors="replace"))
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    yield item


def extract_problem_solution(source_name, raw):
    """Extract (problem, solution, extra_answer_latex) tuple from raw dataset record."""
    if source_name.startswith("camel-"):
        return str(raw.get("message_1") or ""), str(raw.get("message_2") or ""), ""
    if source_name == "scibench":
        prob = str(raw.get("problem_text") or "")
        sol = str(raw.get("solution") or "")
        ans = str(raw.get("answer_latex") or "").strip()
        unit = str(raw.get("unit") or "").strip()
        if sol and ans and "\\boxed{" not in sol:
            ans_str = f"{ans} \\, {unit}".strip() if unit and unit not in ans else ans
            sol = sol.rstrip() + f"\n\nFinal answer: $$\\boxed{{{ans_str}}}$$"
        return prob, sol, ans
    if source_name == "finance-alpaca":
        inst = str(raw.get("instruction") or "").strip()
        inp = str(raw.get("input") or "").strip()
        prob = f"{inst}\n\nContext:\n{inp}" if inp else inst
        return prob, str(raw.get("output") or ""), ""
    return "", "", ""


def route_subject(source_name, raw):
    """Map an external row strictly onto one of the 5 UC3M subjects, or return None."""
    if source_name == "camel-physics":
        meta_txt = f"{raw.get('topic;', '')} | {raw.get('sub_topic', '')}"
        if _PHYS_REJECT_RE.search(meta_txt):
            return None
        if _FLUID_RE.search(meta_txt):
            return "fluid-mechanics"
        if _MATERIALS_RE.search(meta_txt):
            return "aerospace-materials-1"
        if _MECH_RE.search(meta_txt):
            return "engineering-mechanics"
        return None

    if source_name == "camel-math":
        meta_txt = f"{raw.get('topic;', '')} | {raw.get('sub_topic', '')}"
        if _MATH_REJECT_RE.search(meta_txt):
            return None
        return "advanced-maths" if _MATH_ACCEPT_RE.search(meta_txt) else None

    if source_name == "camel-chemistry":
        meta_txt = f"{raw.get('topic;', '')} | {raw.get('sub_topic', '')}"
        if _CHEM_REJECT_RE.search(meta_txt):
            return None
        return "aerospace-materials-1" if _CHEM_ACCEPT_RE.search(meta_txt) else None

    if source_name == "scibench":
        src = str(raw.get("source") or "").lower()
        if any(k in src for k in ("quan", "stat")):
            return None
        if "class" in src:
            return "engineering-mechanics"
        if any(k in src for k in ("diff", "calc")):
            return "advanced-maths"
        body = f"{raw.get('problem_text', '')} {raw.get('solution', '')}"
        if _MATERIALS_RE.search(body):
            return "aerospace-materials-1"
        if not _SCIBENCH_PHOTOCHEM_RE.search(body) and (_FLUID_RE.search(body) or "thermo" in src):
            return "fluid-mechanics"
        if "matter" in src or "chemmc" in src:
            return "aerospace-materials-1"
        return None

    if source_name == "finance-alpaca":
        body = f"{raw.get('instruction', '')} {raw.get('input', '')} {raw.get('output', '')}"
        if _FIN_REJECT_RE.search(body):
            return None
        return "business-management" if _FIN_ACCEPT_RE.search(body) else None

    return None


def passes_quality_gate(problem, solution, subject):
    """Apply strict Sideris length, figure, refusal, skip, math, and KaTeX checks."""
    if not (60 <= len(problem) <= 2400):
        return False, "prob_len"
    min_sol, max_sol = (260, 4500) if subject == "business-management" else (300, 5500)
    if not (min_sol <= len(solution) <= max_sol):
        return False, "sol_len"
    if _FIGURE_RE.search(problem):
        return False, "figure"
    if _TABLE_BELOW_RE.search(problem) and ("|" not in problem or "---" not in problem):
        return False, "missing_table"
    combined = f"{problem}\n{solution}"
    if _REFUSAL_RE.search(combined):
        return False, "refusal"
    if rewards._SKIP_PHRASES.search(solution):
        return False, "skip_phrase"
    if _EMOJI_RE.search(combined):
        return False, "emoji"
    if subject != "business-management" and "$" not in solution and solution.count("=") < 2:
        return False, "no_math"
    if not (katex_balanced(problem) and katex_balanced(solution)):
        return False, "katex_unbalanced"
    if rewards.katex_syntax_reward([solution])[0] < 0:
        return False, "katex_reward"
    return True, "ok"


def score_candidate(problem, solution, subject):
    """Score verified candidates to keep the richest worked problems."""
    score = 0.0
    n = len(solution)
    if 600 <= n <= 2800:
        score += 2.0
    elif 400 <= n <= 3800:
        score += 1.0
    if n > 4200:
        score -= 1.0
    if _BOXED_RE.search(solution):
        score += 2.0
    if "$$" in solution:
        score += 1.5
    if _STEP_MARKER_RE.search(solution):
        score += 1.0
    if _SI_HINT_RE.search(solution):
        score += 1.0
    if subject == "business-management" and _FIN_QUANT_RE.search(solution):
        score += 1.5
    return score


def load_base_holdout_hashes(base_zip_path):
    """Collect MD5 hashes of eval_holdout problem statements to prevent leakage."""
    hashes = set()
    zp = pathlib.Path(base_zip_path)
    if not zp.is_file():
        return hashes
    with zipfile.ZipFile(zp) as zf:
        if "eval_holdout.jsonl" not in zf.namelist():
            return hashes
        for line in zf.read("eval_holdout.jsonl").decode("utf-8", errors="replace").splitlines():
            s = line.strip()
            if not s:
                continue
            rec = json.loads(s)
            for m in rec.get("messages", []):
                if m.get("role") == "user":
                    txt = str(m.get("content") or "")
                    hashes.add(norm_text_hash(txt))
                    inner = re.search(r"<problem_statement[^>]*>([\s\S]*?)</problem_statement>", txt)
                    if inner:
                        hashes.add(norm_text_hash(inner.group(1)))
    return hashes


def make_sft_record(source_name, subject, problem, solution, prob_hash, raw):
    """Format an external problem-solution pair in exact Sideris SFT schema."""
    topic_meta = str(raw.get("sub_topic") or raw.get("topic;") or raw.get("source") or source_name).strip()
    title = topic_meta[:80] if topic_meta else source_name
    rec_id = f"ext-{source_name}-{subject[:4]}-{prob_hash[:10]}"
    return {
        "id": rec_id,
        "task": "problem_solve",
        "subject": subject,
        "unit": 0,
        "source": f"external/{source_name}/{title}",
        "lang": "en",
        "teacher": f"external:{source_name}",
        "messages": [
            {"role": "system", "content": system_prompt(subject, lang="en", socratic=False)},
            {
                "role": "user",
                "content": (
                    f'<problem_statement title="{title}">\n{problem}\n</problem_statement>\n\n'
                    "# Task\nSolve this problem step by step following the UC3M course order with zero algebraic skips, justified equations and a dimensional check."
                ),
            },
            {"role": "assistant", "content": solution},
        ],
    }


def collect_candidates(source_names, cache_dir, holdout_hashes):
    """Download, filter, deduplicate, and score candidates grouped by subject."""
    by_subject = collections.defaultdict(list)
    seen_hashes = set(holdout_hashes)
    stats = collections.Counter()

    for src in source_names:
        info = SOURCES[src]
        cached = download_if_needed(info["url"], pathlib.Path(cache_dir) / info["filename"])
        for raw in _iter_source_records(src, cached):
            stats[f"{src}:scanned"] += 1
            subj = route_subject(src, raw)
            if not subj:
                stats[f"{src}:unrouted"] += 1
                continue
            raw_prob, raw_sol, _ = extract_problem_solution(src, raw)
            prob = normalise_external_latex(raw_prob)
            sol = normalise_external_latex(raw_sol)
            ok, reason = passes_quality_gate(prob, sol, subj)
            if not ok:
                stats[f"{src}:reject_{reason}"] += 1
                continue
            ph = norm_text_hash(prob)
            if ph in seen_hashes:
                stats[f"{src}:dup_or_holdout"] += 1
                continue
            seen_hashes.add(ph)
            score = score_candidate(prob, sol, subj)
            rec = make_sft_record(src, subj, prob, sol, ph, raw)
            by_subject[subj].append((score, rec))
            stats[f"{src}:accepted"] += 1

    return by_subject, stats


def cap_dpo_by_subject(dpo_pairs, max_per_subject):
    kept = []
    counts = collections.Counter()
    for pair in dpo_pairs:
        s = pair["subject"]
        if counts[s] < max_per_subject:
            counts[s] += 1
            kept.append(pair)
    return kept


def _is_external_row(row):
    rid = str(row.get("id") or "")
    teacher = str(row.get("teacher") or "")
    return teacher.startswith("external:") or rid.startswith(
        ("ext-", "dpo-rigour-ext-", "dpo-socratic-ext-", "grpo-ext-")
    )


def build_v2_zip(base_zip_path, out_zip_path, ext_sft, ext_dpo, ext_grpo):
    """Merge base sideris-data.zip with external datasets while keeping eval_holdout & rewards verbatim."""
    base_p = pathlib.Path(base_zip_path)
    out_p = pathlib.Path(out_zip_path)
    out_p.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(base_p, "r") as zin, zipfile.ZipFile(out_p, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        append_map = {
            "train_sft_enriched.jsonl": ext_sft,
            "train_dpo_enriched.jsonl": ext_dpo,
            "train_grpo.jsonl": ext_grpo,
        }
        for name in zin.namelist():
            raw_bytes = zin.read(name)
            if name in append_map:
                kept = []
                for line in raw_bytes.decode("utf-8").splitlines():
                    s = line.strip()
                    if not s:
                        continue
                    row = json.loads(s)
                    if not _is_external_row(row):
                        kept.append(json.dumps(row, ensure_ascii=False))
                for row in append_map[name]:
                    kept.append(json.dumps(row, ensure_ascii=False))
                zout.writestr(name, ("\n".join(kept) + "\n").encode("utf-8"))
            else:
                zout.writestr(name, raw_bytes)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Fetch and filter open external STEM & finance datasets for Sideris.")
    ap.add_argument("--sources", default="all", help="Comma-separated source names or 'all'.")
    ap.add_argument("--per-subject", type=int, default=400, help="Max external SFT records kept per subject.")
    ap.add_argument("--max-dpo-per-subject", type=int, default=80, help="Max external DPO pairs kept per subject.")
    ap.add_argument("--out", default=str(REPO / "tools/ai_training/out/external"), help="External JSONL output folder.")
    ap.add_argument("--cache-dir", default=str(REPO / "tools/ai_training/out/external_cache"), help="Download cache folder.")
    ap.add_argument("--base-zip", default=str(REPO / "tools/ai_training/kaggle_pack/sideris-data.zip"), help="Base Sideris data zip.")
    ap.add_argument("--build-v2-zip", action="store_true", help="Write combined tools/ai_training/out/sideris-data-v2.zip.")
    ap.add_argument("--v2-zip-out", default=str(REPO / "tools/ai_training/out/sideris-data-v2.zip"), help="Destination for v2 zip.")
    ap.add_argument("--dry-run", action="store_true", help="Print counts without writing output files.")
    args = ap.parse_args(argv)

    source_names = list(SOURCES) if args.sources == "all" else [s.strip() for s in args.sources.split(",") if s.strip()]
    for s in source_names:
        if s not in SOURCES:
            raise SystemExit(f"Unknown source '{s}'. Choices: {', '.join(SOURCES)}")

    holdout_hashes = load_base_holdout_hashes(args.base_zip)
    by_subject, stats = collect_candidates(source_names, args.cache_dir, holdout_hashes)

    selected_sft = []
    for subj in SUBJECT_LIST:
        ranked = sorted(by_subject[subj], key=lambda item: (-item[0], item[1]["id"]))
        chosen = [rec for _, rec in ranked[: args.per_subject]]
        selected_sft.extend(chosen)
        print(f"  {subj:24s}: {len(ranked):5d} passed -> kept {len(chosen)}")

    ext_dpo = cap_dpo_by_subject(make_dpo_pairs(selected_sft), args.max_dpo_per_subject)
    ext_grpo = [g for g in make_grpo_prompts(selected_sft) if g.get("expected_answer")]

    print(f"External SFT : {len(selected_sft)}")
    print(f"External DPO : {len(ext_dpo)}")
    print(f"External GRPO: {len(ext_grpo)}")
    print(f"Stats summary: {dict(sorted(stats.items()))}")

    if args.dry_run:
        return 0

    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    for fname, rows in (
        ("external_sft.jsonl", selected_sft),
        ("external_dpo.jsonl", ext_dpo),
        ("external_grpo.jsonl", ext_grpo),
    ):
        p = out_dir / fname
        with p.open("w", encoding="utf-8") as f:
            for row in rows:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
        print(f"Wrote {p}: {len(rows)} rows")

    if args.build_v2_zip:
        build_v2_zip(args.base_zip, args.v2_zip_out, selected_sft, ext_dpo, ext_grpo)
        print(f"Built combined v2 archive -> {args.v2_zip_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
