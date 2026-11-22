#!/usr/bin/env python3
"""Train and export the Sideris model family (Lux, Aether, Orion, Titan) with Unsloth.

Designed to run for FREE on Kaggle (2xT4 / P100) or Google Colab (T4 15 GB) in three stages:
  Stage 1: SFT (QLoRA 4-bit) on UC3M engineering & Socratic conversations
  Stage 2: DPO (optional preference alignment against algebraic skips & Socratic leaks)
  Stage 3: GRPO (verifiable RL using rewards.py: SymPy + KaTeX + SI checks + Socratic guard)
  Export : GGUF (Q4_K_M for Ollama/LM Studio) + merged FP16 ready for ONNX q4f16 WebGPU export

Usage (inside Colab / Kaggle):
    pip install unsloth trl datasets sympy optimum[onnxruntime]
    python tools/ai_training/train_sideris.py --model aether --stage sft --data train_seed.jsonl
    python tools/ai_training/train_sideris.py --model orion  --stage grpo --data grpo_math.jsonl
    python tools/ai_training/train_sideris.py --model titan  --stage export --adapter ./out/sideris-titan
"""
import argparse
import pathlib

MODEL_RECIPES = {
    "lux": {
        "name": "Sideris-Lux",
        "base_model": "Qwen/Qwen3.5-2B",
        "max_seq_length": 4096,
        "lora_r": 16,
        "lora_alpha": 16,
        "lr": 2e-4,
        "export_target": "onnx",
    },
    "aether": {
        "name": "Sideris-Aether",
        "base_model": "Qwen/Qwen3.5-4B",
        "max_seq_length": 4096,
        "lora_r": 32,
        "lora_alpha": 32,
        "lr": 2e-4,
        "export_target": "onnx",
    },
    "orion": {
        "name": "Sideris-Orion",
        "base_model": "microsoft/Phi-4-mini-reasoning",
        "max_seq_length": 4096,
        "lora_r": 32,
        "lora_alpha": 32,
        "lr": 1.5e-4,
        "export_target": "onnx",
    },
    "titan": {
        "name": "Sideris-Titan",
        "base_model": "Qwen/Qwen3.5-9B",
        "max_seq_length": 4096,
        "lora_r": 32,
        "lora_alpha": 32,
        "lr": 1.5e-4,
        "export_target": "gguf",
    },
}

TARGET_MODULES = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]


def run_sft(recipe, data_path, out_dir, epochs):
    from datasets import load_dataset  # type: ignore
    from trl import SFTConfig, SFTTrainer  # type: ignore
    from unsloth import FastLanguageModel  # type: ignore

    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=recipe["base_model"],
        max_seq_length=recipe["max_seq_length"],
        load_in_4bit=True,
    )
    model = FastLanguageModel.get_peft_model(
        model,
        r=recipe["lora_r"],
        lora_alpha=recipe["lora_alpha"],
        target_modules=TARGET_MODULES,
        lora_dropout=0,
        bias="none",
        use_gradient_checkpointing="unsloth",
        random_state=42,
    )

    ds = load_dataset("json", data_files=str(data_path), split="train")

    def fmt(batch):
        texts = [
            tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=False)
            for msgs in batch["messages"]
        ]
        return {"text": texts}

    ds = ds.map(fmt, batched=True)
    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=ds,
        args=SFTConfig(
            output_dir=str(out_dir),
            dataset_text_field="text",
            max_seq_length=recipe["max_seq_length"],
            per_device_train_batch_size=2,
            gradient_accumulation_steps=8,
            num_train_epochs=epochs,
            learning_rate=recipe["lr"],
            lr_scheduler_type="cosine",
            warmup_ratio=0.05,
            bf16=False,
            fp16=True,
            logging_steps=10,
            save_strategy="epoch",
            optim="adamw_8bit",
            seed=42,
        ),
    )
    trainer.train()
    model.save_pretrained(str(out_dir))
    tokenizer.save_pretrained(str(out_dir))
    print(f"Saved SFT LoRA adapter to {out_dir}")


def run_dpo(recipe, adapter_dir, data_path, out_dir):
    from datasets import load_dataset  # type: ignore
    from trl import DPOConfig, DPOTrainer  # type: ignore
    from unsloth import FastLanguageModel, PatchDPOTrainer  # type: ignore

    PatchDPOTrainer()
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=str(adapter_dir),
        max_seq_length=recipe["max_seq_length"],
        load_in_4bit=True,
    )
    ds = load_dataset("json", data_files=str(data_path), split="train")
    trainer = DPOTrainer(
        model=model,
        ref_model=None,
        tokenizer=tokenizer,
        train_dataset=ds,
        args=DPOConfig(
            output_dir=str(out_dir),
            per_device_train_batch_size=2,
            gradient_accumulation_steps=4,
            num_train_epochs=1,
            learning_rate=5e-6,
            beta=0.1,
            fp16=True,
            optim="adamw_8bit",
        ),
    )
    trainer.train()
    model.save_pretrained(str(out_dir))
    tokenizer.save_pretrained(str(out_dir))
    print(f"Saved DPO adapter to {out_dir}")


def run_grpo(recipe, adapter_dir, data_path, out_dir):
    from datasets import load_dataset  # type: ignore
    from trl import GRPOConfig, GRPOTrainer  # type: ignore
    from unsloth import FastLanguageModel  # type: ignore
    from rewards import (
        katex_syntax_reward,
        no_skip_rigour_reward,
        socratic_guard_reward,
        sympy_answer_reward,
    )

    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=str(adapter_dir),
        max_seq_length=recipe["max_seq_length"],
        load_in_4bit=True,
    )
    ds = load_dataset("json", data_files=str(data_path), split="train")
    trainer = GRPOTrainer(
        model=model,
        processing_class=tokenizer,
        reward_funcs=[
            katex_syntax_reward,
            no_skip_rigour_reward,
            socratic_guard_reward,
            sympy_answer_reward,
        ],
        train_dataset=ds,
        args=GRPOConfig(
            output_dir=str(out_dir),
            learning_rate=5e-6,
            per_device_train_batch_size=1,
            gradient_accumulation_steps=4,
            num_generations=4,
            max_prompt_length=1536,
            max_completion_length=1024,
            num_train_epochs=1,
            fp16=True,
            optim="adamw_8bit",
            logging_steps=5,
        ),
    )
    trainer.train()
    model.save_pretrained(str(out_dir))
    tokenizer.save_pretrained(str(out_dir))
    print(f"Saved GRPO adapter to {out_dir}")


def run_export(recipe, adapter_dir, out_dir, hf_repo):
    from unsloth import FastLanguageModel  # type: ignore

    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=str(adapter_dir),
        max_seq_length=recipe["max_seq_length"],
        load_in_4bit=True,
    )
    merged_dir = out_dir / "merged_16bit"
    model.save_pretrained_merged(str(merged_dir), tokenizer, save_method="merged_16bit")
    print(f"Merged 16-bit weights written to {merged_dir}")

    gguf_dir = out_dir / "gguf"
    model.save_pretrained_gguf(str(gguf_dir), tokenizer, quantization_method="q4_k_m")
    print(f"GGUF Q4_K_M written to {gguf_dir} (ready for Ollama / LM Studio)")

    print(
        "\nNext step for browser WebGPU (Transformers.js v4):\n"
        f"  optimum-cli export onnx --model {merged_dir} --task text-generation-with-past {out_dir / 'onnx'}\n"
        "  # Quantise to q4f16 with onnxruntime-genai / onnx-community pipeline and upload to Hugging Face:\n"
        f"  huggingface-cli upload {hf_repo or 'YOUR_USER/' + recipe['name'] + '-ONNX'} {out_dir / 'onnx'}"
    )


def main(argv=None):
    ap = argparse.ArgumentParser(description="Train and export Sideris models with Unsloth.")
    ap.add_argument("--model", required=True, choices=sorted(MODEL_RECIPES))
    ap.add_argument("--stage", required=True, choices=("sft", "dpo", "grpo", "export"))
    ap.add_argument("--data", help="Input JSONL file (for sft, dpo or grpo).")
    ap.add_argument("--adapter", help="Existing LoRA adapter directory (for dpo, grpo or export).")
    ap.add_argument("--out", default="./sideris_out", help="Output directory.")
    ap.add_argument("--epochs", type=int, default=3)
    ap.add_argument("--hf-repo", default="", help="Optional Hugging Face target repo for upload command.")
    args = ap.parse_args(argv)

    recipe = MODEL_RECIPES[args.model]
    out_dir = pathlib.Path(args.out) / f"sideris-{args.model}-{args.stage}"
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.stage == "sft":
        run_sft(recipe, args.data, out_dir, args.epochs)
    elif args.stage == "dpo":
        run_dpo(recipe, args.adapter, args.data, out_dir)
    elif args.stage == "grpo":
        run_grpo(recipe, args.adapter, args.data, out_dir)
    elif args.stage == "export":
        run_export(recipe, args.adapter, out_dir, args.hf_repo)


if __name__ == "__main__":
    main()
