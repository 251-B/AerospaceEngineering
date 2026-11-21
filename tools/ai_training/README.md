# Sideris Training Pipeline (`tools/ai_training/`)

End-to-end free-compute training pipeline for the four **Sideris** models, built directly from the
1.34-million-word UC3M Aerospace Engineering `vault/` (excluding all laboratory material).

| Model | Base checkpoint | Target runtime | Recommended stages |
| :--- | :--- | :--- | :--- |
| **Sideris Lux** | `Qwen/Qwen3.5-2B` | WebGPU (`ONNX q4f16`) | SFT -> DPO -> ONNX export |
| **Sideris Aether** | `Qwen/Qwen3.5-4B` | WebGPU (`ONNX q4f16`) | SFT -> DPO -> GRPO -> ONNX export |
| **Sideris Orion** | `microsoft/Phi-4-mini-reasoning` | WebGPU (`ONNX q4f16`) | SFT -> GRPO (SymPy) -> ONNX export |
| **Sideris Titan** | `Qwen/Qwen3.5-9B` | Local Ollama (`GGUF Q4_K_M`) | SFT -> DPO -> GRPO -> GGUF export |

---

## Step 1 — Generate the sanitised UC3M seed datasets (`train_sft`, `eval_holdout`, `train_dpo`, `train_grpo`)

```bash
python tools/ai_training/build_dataset.py --out tools/ai_training/out
```

Automatically extracts all 7 task families (`theory_explain`, `quiz_mcq_tutor`, `problem_solve`
including the 51 paired Engineering Mechanics official sets, `socratic_seed`, multi-turn
`socratic_multiturn` from hand-written `Hint`/`Checkpoint`/`Solution` notes, `derive_principles`
from `> [!derivation]` blocks, and `essential_summary`), strips legacy `Phase 1..4` labels and
emojis, verifies balanced KaTeX (`$...$`, `$$...$$`, no `\euro`), and writes a deterministic 90/10
file-grouped split plus `train_dpo.jsonl` and `train_grpo.jsonl`.

---

## Step 1b — (Optional) Reference-textbook corpus for continued pre-training

The 20 official reference books (Callister, White, Batchelor, Haberman, ...) live in
`sources/libros/` **locally only** (copyrighted; PDFs are git-ignored, only `libros.json` is
tracked). Extract them into chunked raw text and run a CPT stage before SFT:

```bash
python tools/ai_training/extract_books.py   # -> out/books_cpt.jsonl + out/books_report.json
python tools/ai_training/train_sideris.py --model aether --stage cpt --data tools/ai_training/out/books_cpt.jsonl
# then: --stage sft --adapter ./sideris_out/sideris-aether-cpt ...
```

`books_cpt.jsonl` is book-derived text: never commit it or upload it to a public dataset.

---

## Step 2 — Enrich & Cross-Audit with Claude Pro + Gemini Pro

Export stratified batches across all 5 subjects for bilingual Spanish + `[English term]` adaptation,
deep multi-turn Socratic trees, and `checkAttempt` error-hunting:

```bash
python tools/ai_training/enrich_with_claude_gemini.py export --mode bilingual_es --limit 160
python tools/ai_training/enrich_with_claude_gemini.py export --mode socratic_deep --limit 100
python tools/ai_training/enrich_with_claude_gemini.py export --mode check_attempt --limit 100
```

Run batches with Claude Pro / Gemini Pro (cross-auditing each other against `AGENTS.md`), save the
returned JSONL files, then validate & merge them back into `train_sft_enriched.jsonl`:

```bash
python tools/ai_training/enrich_with_claude_gemini.py merge --inputs enriched_es.jsonl enriched_soc.jsonl enriched_check.jsonl
```

---

## Step 3 — Train for free on Kaggle (`2×T4`, 30 h/week) or Google Colab (`T4`)

Open **`tools/ai_training/Sideris_Train_Colab_Kaggle.ipynb`** in Kaggle or Colab, upload
`tools/ai_training/out/*.jsonl` + `tools/ai_training/rewards.py`, choose `MODEL_CHOICE = "aether"`
(or `"lux"`, `"orion"`, `"titan"`), and click **Run All**.

Alternatively from CLI:

```bash
pip install unsloth trl datasets sympy optimum[onnxruntime]
python tools/ai_training/train_sideris.py --model aether --stage sft --data tools/ai_training/out/train_sft_enriched.jsonl
python tools/ai_training/train_sideris.py --model aether --stage dpo --adapter ./sideris_out/sideris-aether-sft --data tools/ai_training/out/train_dpo.jsonl
python tools/ai_training/train_sideris.py --model aether --stage grpo --adapter ./sideris_out/sideris-aether-dpo --data tools/ai_training/out/train_grpo.jsonl
python tools/ai_training/train_sideris.py --model aether --stage export --adapter ./sideris_out/sideris-aether-grpo --hf-repo YOUR_USER/Sideris-Aether-ONNX
```

---

## Step 4 — Publish & connect to the portal

Upload your exported ONNX (`q4f16`) or GGUF (`Q4_K_M`) repo to Hugging Face Hub, then update `repo`
and `"trained": true` in `assets/data/ai-models.js`. No HTML page changes and no PDF is reprinted.
