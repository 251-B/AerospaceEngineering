# Libros de referencia (bibliografía oficial UC3M, 2º curso)

Bibliografía recomendada por las asignaturas del 1er cuatrimestre, usada como **fuente de
entrenamiento de Sideris** (fase CPT, antes del SFT).

> **Los PDFs no están en git.** Tienen copyright y este repositorio es público, así que
> `.gitignore` excluye `sources/libros/**/*.pdf`. Solo se versionan este README y el manifiesto
> [`libros.json`](libros.json). Cada colaborador copia los PDFs a mano a esta carpeta.

## Estructura

```text
sources/libros/
├── libros.json                  # manifiesto (id, archivo, asignatura, idioma, use_for_training)
├── 01-fluid-mechanics/          # Crespo, White, Batchelor, Tritton, Landau-Lifshitz, Lagerstrom
│   └── adicional/               # Apostol (Calculus), Carrier-Pearson (ODEs)
├── 02-aerospace-materials-1/    # Callister, Askeland, Shackelford, Smith, Mangonon, Ashby, Mouritz
├── 03-engineering-mechanics/    # Ginsberg (Engineering Dynamics)
│   └── adicional/               # Kermode (Mechanics of Flight)
└── 04-advanced-maths/           # Robinson (ODEs), Brannan-Boyce, Haberman (PDEs)
```

## Uso para entrenar Sideris

```bash
pip install pymupdf
python tools/ai_training/extract_books.py            # -> tools/ai_training/out/books_cpt.jsonl
python tools/ai_training/train_sideris.py --model aether --stage cpt --data tools/ai_training/out/books_cpt.jsonl
python tools/ai_training/train_sideris.py --model aether --stage sft --adapter ./sideris_out/sideris-aether-cpt --data tools/ai_training/out/train_sft_enriched.jsonl
```

- Para excluir un libro, pon `"use_for_training": false` en `libros.json`.
- Para limitar páginas (p. ej. quitar índices y apéndices), añade `"page_range": [15, 640]`.
- `extract_books.py --manifest-only` regenera el manifiesto si añades libros, y conserva esos campos manuales.
- `books_report.json` marca los PDFs escaneados sin capa de texto (necesitan OCR).
