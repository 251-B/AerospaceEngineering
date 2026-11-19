# Sideris Training Pipeline (`tools/ai_training/`)

End-to-end free-compute training pipeline for the four **Sideris** models:

| Model | Base checkpoint | Target runtime | Recommended stages |
| :--- | :--- | :--- | :--- |
| **Sideris Lux** | `Qwen/Qwen3.5-2B` | WebGPU (`ONNX q4f16`) | SFT -> DPO -> ONNX export |
| **Sideris Aether** | `Qwen/Qwen3.5-4B` | WebGPU (`ONNX q4f16`) | SFT -> DPO -> GRPO -> ONNX export |
| **Sideris Orion** | `microsoft/Phi-4-mini-reasoning` | WebGPU (`ONNX q4f16`) | SFT -> GRPO (SymPy) -> ONNX export |
| **Sideris Titan** | `Qwen/Qwen3.5-9B` | Local Ollama (`GGUF Q4_K_M`) | SFT -> DPO -> GRPO -> GGUF export |

## Step 1 — Build the verified seed dataset from `vault/`

```bash
python tools/ai_training/build_dataset.py --out tools/ai_training/out
```

This creates a 90/10 split (`train_seed.jsonl`, `eval_holdout.jsonl`) excluding all laboratory files
and gating every sample on balanced KaTeX delimiters (`$...$`, `$$...$$`, no `\euro`, no `&` inside `\text{}`).

To scale to 8k–12k examples, enrich `train_seed.jsonl` with:
- Bilingual Spanish + `[English term]` expansions and 4–8 turn Socratic trees (checking with `rewards.py` so hidden reference solutions never leak);
- Parametric problem variations verified with SymPy;
- DPO preference pairs (`prompt`, `chosen`, `rejected`) penalising skipped algebra and Socratic leaks.

## Step 2 — Train for free on Kaggle (`2×T4`) or Google Colab (`T4`)

```bash
pip install unsloth trl datasets sympy optimum[onnxruntime]
python tools/ai_training/train_sideris.py --model aether --stage sft --data train_seed.jsonl
python tools/ai_training/train_sideris.py --model aether --stage dpo --adapter ./sideris_out/sideris-aether-sft --data dpo_pairs.jsonl
python tools/ai_training/train_sideris.py --model aether --stage grpo --adapter ./sideris_out/sideris-aether-dpo --data grpo_prompts.jsonl
```

## Step 3 — Export & connect to the portal

```bash
python tools/ai_training/train_sideris.py --model aether --stage export --adapter ./sideris_out/sideris-aether-grpo --hf-repo YOUR_USER/Sideris-Aether-ONNX
```

Upload the resulting ONNX (`q4f16`) or GGUF (`Q4_K_M`) repo to Hugging Face Hub (free), then update
the `repo` field (and set `"trained": true`) in `assets/data/ai-models.js`. No HTML pages change
and no PDFs need to be reprinted.
