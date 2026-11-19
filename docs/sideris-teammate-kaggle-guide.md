# Guía rápida para entrenar Sideris en paralelo (Kaggle + Hugging Face)

Con dos cuentas gratuitas de Kaggle (**60 h/semana de GPU gratis entre los dos**) podéis entrenar toda la familia Sideris en paralelo:
- **Cuenta 1 (Héctor):** `Sideris Aether` (`"aether"`) y luego `Sideris Titan` (`"titan"`).
- **Cuenta 2 (Compañero):** **`Sideris Lux` (`"lux"`, ~3,5–4 h)** y luego **`Sideris Orion` (`"orion"`, ~5–6 h)**.

---

## Qué archivos necesitas (ya subidos a GitHub en `tools/ai_training/kaggle_pack/`)

Todo está guardado y listo para descargar directamente en la carpeta **`tools/ai_training/kaggle_pack/`** del repositorio (`git pull origin main`):

1. **`tools/ai_training/kaggle_pack/sideris-data.zip`** (3,2 MB) — los 5 archivos de entrenamiento ya enriquecidos con Neon 4 + Sonnet 5.5 + Opus y verificados (`train_sft_enriched.jsonl`, `train_dpo_enriched.jsonl`, `train_grpo.jsonl`, `eval_holdout.jsonl`, `rewards.py`).
2. **`tools/ai_training/kaggle_pack/Sideris_Train_Lux_Kaggle.ipynb`** — el notebook ya preconfigurado para entrenar **`Sideris Lux`** (`MODEL_CHOICE = "lux"`, `SFT_EPOCHS = 3`, `RUN_DPO = True`, `RUN_GRPO = False`).
3. **`tools/ai_training/kaggle_pack/Sideris_Train_Colab_Kaggle.ipynb`** — el notebook maestro para cualquier modelo (`lux`, `aether`, `orion`, `titan`).

---

## Paso 1 — Crear y verificar cuenta de Kaggle (2 min)

1. Crea una cuenta gratis en [https://www.kaggle.com](https://www.kaggle.com).
2. **Obligatorio para tener GPU e Internet:** pulsa tu foto arriba a la derecha → **Settings** → **Phone verification** y verifica tu número de teléfono. *(Sin esto Kaggle bloquea las GPUs.)*

---

## Paso 2 — Crear cuenta de Hugging Face y token Write (2 min)

*(Así Kaggle sube el modelo entrenado automáticamente a la nube al terminar y nunca se pierde aunque se cierre la sesión.)*

1. Crea una cuenta gratis en [https://huggingface.co](https://huggingface.co) y apunta tu **usuario exacto** (respetando mayúsculas/minúsculas, el que sale en `huggingface.co/TU_USUARIO`).
2. Pulsa tu foto arriba a la derecha → **Settings** → **Access Tokens** → **Create new token**:
   - **Token type:** `Write`
   - **Name:** `kaggle-sideris`
   - Pulsa **Create token** y **copia el código `hf_...`** (guárdalo un momento; nunca lo subas a GitHub).

*(Alternativa si queréis juntar todos los modelos en una sola cuenta/organización de Hugging Face: cread una organización gratuita en Hugging Face, añadid a los dos miembros con rol Write y poned el nombre de la organización en `HF_USERNAME`.)*

---

## Paso 3 — Subir el dataset en Kaggle (1 min)

1. En Kaggle (menú izquierdo) → **Datasets** → **New Dataset** (o `+ Create` → **New Dataset**).
2. Arrastra **`sideris-data.zip`**.
3. Ponle de título **`Sideris-Data`**, déjalo en **Private** y pulsa **Create**.

---

## Paso 4 — Importar el notebook y activar la GPU (2 min)

1. En Kaggle → **+ Create** → **New Notebook**.
2. En el menú superior: **File** → **Import Notebook** → sube **`Sideris_Train_Lux_Kaggle.ipynb`**.
3. En la **Celda 1**, cambia **solo esta línea** con tu usuario exacto de Hugging Face:
   ```python
   HF_USERNAME = "TU_USUARIO_DE_HUGGINGFACE"
   ```
   *(Para entrenar `Sideris Lux` deja el resto tal cual: `MODEL_CHOICE = "lux"`, `SFT_EPOCHS = 3`, `RUN_DPO = True`, `RUN_GRPO = False`.)*
4. En el menú superior: **Add-ons** → **Secrets** → **+ Add a new secret**:
   - **Label:** `HF_TOKEN`
   - **Value:** pega tu token `hf_...` de Hugging Face → **Save** y **marca la casilla** del secreto para activarlo en este notebook.
5. En el panel derecho del notebook:
   - **Input → `+ Add Input`:** busca y añade **`Sideris-Data`**.
   - **Session options** (abajo a la derecha, despliega la flecha `v`):
     - **Accelerator:** **`GPU T4 x2`**
     - **Internet:** **`On`**

---

## Paso 5 — Lanzar el entrenamiento

Tienes dos formas (la **opción A** es la más cómoda porque no tienes que dejar el ordenador encendido):

- **Opción A — Automático en segundo plano (RECOMENDADO):**
  Pulsa el botón negro arriba a la derecha **Save Version** → elige **Save & Run All (Commit)** → **Save**.
  Kaggle ejecutará las 8 celdas de principio a fin aunque cierres el navegador o apagues el PC, y al acabar (~3,5–4 h) subirá automáticamente `Sideris-Lux` y `Sideris-Lux-GGUF` a tu Hugging Face.
- **Opción B — Interactivo viendo el progreso:**
  Pulsa **`Run All`**, mantén la pestaña abierta sin suspender el PC y verás bajar el `Training Loss` en directo en la Celda 4 (`2.0 → 0.5`).

---

## Cuando acabe `Sideris Lux`: siguiente modelo (`Sideris Orion`)

Para lanzar **`Sideris Orion`** (`microsoft/Phi-4-mini-reasoning`, especialista en matemáticas y derivaciones, ~5–6 h) al día siguiente en el mismo notebook solo tienes que cambiar 3 líneas en la **Celda 1**:

```python
MODEL_CHOICE   = "orion"
SFT_EPOCHS     = 2
RUN_GRPO       = True
GRPO_MAX_STEPS = 120
```

Y darle otra vez a **Save Version → Save & Run All (Commit)**.

## Solución rápida si algo falla
- **`No GPU found`:** falta activar `GPU T4 x2` en *Session options* (o verificar el teléfono en *Settings*).
- **`Could not find train_sft_enriched.jsonl`:** falta añadir `Sideris-Data` en **Input → `+ Add Input`**.
- **Comprobar que subió bien:** entra en `https://huggingface.co/TU_USUARIO` y verás tus repos privados `Sideris-Lux` (y `Sideris-Lux-GGUF`).
