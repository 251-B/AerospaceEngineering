# Prompt para Gemini: entrenar Sideris Aether desde cero en Kaggle (con libros)

Copia todo el bloque de abajo en Gemini (con acceso al repo o pegándole los archivos que pida).

---

```text
Eres mi ingeniero de ML para el proyecto Sideris (tutor de IA del portal de estudio de 2º de
Ingeniería Aeroespacial UC3M). Repositorio: https://github.com/251-B/AerospaceEngineering
(rama de trabajo: feat/sideris-book-sources, que ya incluye todo lo de main, incluido el último
commit de mi compañero "feat(ai-training): add external STEM/finance harvester, v2 dataset pack,
and Kaggle T4 Phi-4 fixes"). Lee antes de nada:
  - AGENTS.md (reglas del repo; sección "Sideris AI tutor")
  - tools/ai_training/README.md
  - tools/ai_training/kaggle_pack/GUIA_PASO_A_PASO.md y docs/sideris-teammate-kaggle-guide.md
  - tools/ai_training/kaggle_pack/Sideris_Train_Colab_Kaggle.ipynb (notebook maestro, 9 celdas)
  - tools/ai_training/train_sideris.py, extract_books.py, ocr_books.py, fetch_external_datasets.py,
    rewards.py, build_dataset.py
  - sources/libros/README.md y sources/libros/libros.json

OBJETIVO PARA ESTA NOCHE
Entrenar Sideris Aether (Qwen/Qwen3.5-4B, QLoRA 4-bit, LoRA r=32, alpha=32, lr 2e-4) DESDE CERO
(desde el modelo base, sin reutilizar adaptadores antiguos) en Kaggle (GPU T4 x2; el notebook usa
una sola T4 con CUDA_VISIBLE_DEVICES=0; límite de 12 h por sesión) y que se suba solo a la
organización privada de Hugging Face "SiderisAI" (secreto de Kaggle HF_TOKEN, token Write).
Tiene que poder lanzarse con "Save Version -> Save & Run All (Commit)" y terminar sin mi
intervención.

ESTADO ACTUAL (verificado)
1. Dataset v2 (tools/ai_training/kaggle_pack/sideris-data.zip, se sube a Kaggle como dataset
   privado "Sideris-Data"): train_sft_enriched.jsonl (5.926 ejemplos, incluidos 2.627 STEM/finanzas
   externos), train_dpo_enriched.jsonl (1.310 pares), train_grpo.jsonl (1.037 prompts),
   eval_holdout.jsonl (314, sin contaminación: no se puede entrenar con él), rewards.py.
2. Notebook maestro: Celda 1 configura MODEL_CHOICE="aether", HF_USERNAME="SiderisAI",
   SFT_EPOCHS=2, RUN_DPO=True, RUN_GRPO=True, GRPO_MAX_STEPS=80 y autodetecta DATA_DIR.
   Celda 2 instala dependencias (transformers>=5.2.0; NO instalar optimum[onnxruntime] porque
   baja transformers y rompe Qwen3.5). Celda 3 carga en 4-bit (Unsloth con fallback a HF+PEFT).
   Celdas 4/5/6: SFT, DPO, GRPO. Celda 7: evaluación con eval_holdout. Celda 8: export LoRA +
   merged 16-bit + GGUF Q4_K_M y subida a HF.
3. NUEVO: libros de referencia de la bibliografía oficial (20 libros, sources/libros/). Los PDFs NO
   están en git (tienen copyright y el repo es público); solo libros.json. Ya existe el corpus:
   tools/ai_training/extract_books.py -> tools/ai_training/out/books_cpt.jsonl
   (un registro por fragmento de ~900 palabras con solapamiento de 80:
   {"text", "book_id", "subject", "title", "lang", "pages"}). Ahora mismo: 11 libros con texto,
   ~2,9 M palabras, 2.897 fragmentos, ~20 MB (Callister, Askeland, Shackelford [es], Mangonon,
   Ashby, Mouritz, White, Lagerstrom, Apostol, Kermode, Ginsberg, Robinson).
   Esta noche se está haciendo OCR (tools/ai_training/ocr_books.py, RapidOCR) de 7 libros
   escaneados (Crespo [es], Tritton, Batchelor, Landau-Lifshitz, Carrier-Pearson, Brannan-Boyce,
   Haberman, ~4.200 páginas); al terminar, extract_books.py los añade al mismo books_cpt.jsonl.
   El OCR estropea las fórmulas: la prosa vale, las ecuaciones no son fiables. El PDF del Smith
   está corrupto (descarga incompleta) y queda fuera.
   train_sideris.py ya tiene una etapa "--stage cpt" (preentrenamiento continuado con LoRA sobre
   el texto de los libros, packing, lr = lr_receta/4, 1 época) y "--stage sft --adapter <cpt>"
   para continuar el SFT sobre ese mismo LoRA. EL NOTEBOOK TODAVÍA NO TIENE LA ETAPA CPT.

LO QUE TE PIDO
A. Modifica Sideris_Train_Colab_Kaggle.ipynb (y su copia en kaggle_pack/, idénticas) para añadir
   una etapa opcional "Stage 0 — CPT on reference textbooks" entre la Celda 3 y la Celda 4:
   - Interruptores en la Celda 1: RUN_CPT=True, CPT_EPOCHS=1, CPT_MAX_STEPS (tope de seguridad),
     CPT_LR=5e-5, CPT_SUBJECT_WEIGHTS opcional.
   - Lee books_cpt.jsonl de un SEGUNDO dataset privado de Kaggle "Sideris-Books" (autodetéctalo
     como hace la Celda 1 con Sideris-Data); si no está, salta la etapa sin fallar.
   - Mismo LoRA para CPT y SFT (no crear uno nuevo en la Celda 4 si ya existe), packing=True,
     max_seq_length 4096 (baja a 2048 si hay OOM en T4), añade eos al final de cada fragmento.
   - Filtra fragmentos de OCR con demasiado ruido (p. ej. proporción de caracteres no
     alfabéticos alta o palabras muy cortas) antes de entrenar.
   - Mezcla anti-olvido: intercala un ~10-15 % de ejemplos de train_sft_enriched.jsonl
     formateados con la plantilla de chat dentro del CPT para que no pierda el formato de tutor.
   - Guarda el adaptador CPT en /kaggle/working y súbelo a HF (SiderisAI/Sideris-Aether-cpt,
     privado) nada más terminar, para no perderlo si la sesión muere.
B. Presupuesto de tiempo: estima (con cifras realistas de Qwen3.5-4B QLoRA en una T4: tokens/s)
   cuánto tarda cada etapa con ~4-5 M palabras de libros + 5.926 SFT + 1.310 DPO + 80 pasos GRPO +
   export, y ajusta CPT_MAX_STEPS, SFT_EPOCHS y GRPO_MAX_STEPS para que todo quepa con margen en
   menos de 11 h. Si no cabe, propón partirlo en dos sesiones (sesión 1: CPT + SFT y subir
   adaptador; sesión 2: DPO + GRPO + export desde ese adaptador) y deja el notebook preparado
   para ambas (variable RESUME_FROM_ADAPTER con el repo de HF).
C. Robustez: checkpoint y subida a HF tras CADA etapa; si DPO o GRPO fallan por CUDA/OOM, seguir
   con el último adaptador bueno y exportar igualmente; registrar loss y tiempos; evaluación final
   en eval_holdout comparando, si da tiempo, contra el modelo base (puerta KaTeX y reglas de
   rewards.py).
D. ¿Hace falta convertir los libros en dataset? books_cpt.jsonl YA es el dataset para CPT.
   Además, diseña (no hace falta ejecutarlo esta noche) un script que convierta fragmentos de los
   libros en ejemplos SFT tipo pregunta-respuesta y explicación socrática por asignatura,
   generados con un modelo grande y verificados con las mismas puertas que build_dataset.py
   (KaTeX equilibrado, sin etiquetas "Phase", sin emojis, unidades SI, sin pasos algebraicos
   omitidos) y deduplicados contra eval_holdout.jsonl. Para los libros con OCR no generes
   ejercicios que dependan de fórmulas sin verificarlas.
E. Dame un ROADMAP por fases (esta noche, esta semana, próximas semanas) con: entrenamiento de
   Aether v2 con libros, evaluación objetiva (métricas sobre eval_holdout, comparación v1 vs v2),
   dataset SFT derivado de libros, re-entrenamiento de Lux/Orion/Titan con el mismo pipeline
   (reparto de las dos cuentas de Kaggle, 30 h/semana cada una), y criterios para decidir si el
   CPT con libros mejora o empeora al tutor.
F. Al final dame la lista exacta de pasos para mí en Kaggle esta noche (qué zips subir y con qué
   nombre, qué variables tocar en la Celda 1, qué secretos activar, qué acelerador).

RESTRICCIONES (obligatorias)
- El texto de los libros tiene copyright: books_cpt.jsonl, la caché .ocr/ y los PDFs NUNCA se
  suben a GitHub ni a un dataset o repo público. En Kaggle, dataset "Sideris-Books" en Private; en
  Hugging Face, repos privados. No pongas fragmentos de los libros en el notebook ni en logs.
- No toques eval_holdout.jsonl ni entrenes con él.
- No subas tokens ni claves al repo. Usa el secreto HF_TOKEN de Kaggle.
- Respeta AGENTS.md: commits "type(scope): resumen", solo los archivos de la tarea, y las dos
  copias del notebook idénticas. Ejecuta python -m unittest discover -s tools/tests -p "test_*ai*"
  y test_fetch_external_datasets.py antes de hacer commit.
- Si algo del estado que te doy no cuadra con lo que ves en el repo, dímelo antes de cambiarlo.
```

---

## Para preparar el dataset de libros en Kaggle (lo haces tú, en local)

Cuando termine el OCR (el log está en `tools/ai_training/out/ocr_log.txt`):

```powershell
python tools/ai_training/extract_books.py
```

```powershell
Compress-Archive -Force tools/ai_training/out/books_cpt.jsonl tools/ai_training/out/sideris-books.zip
```

Sube `sideris-books.zip` a Kaggle como dataset **privado** llamado `Sideris-Books`. No lo subas a GitHub
(ya está en `.gitignore`).
