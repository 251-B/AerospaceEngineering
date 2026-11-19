/*!
 * Aerospace Engineering Study Portal: Sideris model catalogue.
 *
 * Loaded on study pages by assets/js/theme.js right after assets/data/sideris-config.js and
 * before assets/js/ai-rag.js, ai-engine.js and ai-chat.js. Keep everything between the brackets
 * pure JSON (tools/tests/test_ai_chat.py parses it directly).
 *
 * Backends:
 *   - backend: "cloud"  -> zero-download instant streaming via your free Cloudflare Worker
 *                          (tools/cloudflare/sideris-worker.js: Gemini Flash -> Groq -> OpenRouter)
 *                          or a user's own free API key (BYOK, stored only in their browser);
 *   - backend: "webgpu" -> ONNX weights streamed from Hugging Face via Transformers.js v4 and
 *                          cached in the browser Cache API / IndexedDB for free offline use;
 *   - backend: "ollama" -> GGUF weights running locally via Ollama / LM Studio on localhost.
 */
window.AE_SIDERIS_MODELS = [
  {
    "id": "sideris-instant",
    "name": "Sideris Instant",
    "tier": "Instant · 0 MB",
    "backend": "cloud",
    "repo": "sideris-cloud-cascade",
    "base": "Gemini Flash / Groq / OpenRouter",
    "sizeLabel": "0 MB download",
    "minRamGb": 1,
    "thinking": true,
    "vision": false,
    "default": true,
    "trained": false,
    "summary": "Ready immediately on any phone or laptop with zero download (free Cloudflare Worker cascade or your own free Gemini/Groq key), grounded in the UC3M vault."
  },
  {
    "id": "sideris-lux",
    "name": "Sideris Lux",
    "tier": "Fast offline",
    "backend": "webgpu",
    "repo": "onnx-community/Qwen3.5-2B-ONNX",
    "base": "Qwen3.5-2B",
    "dtype": "q4f16",
    "sizeLabel": "~1.3 GB",
    "minRamGb": 4,
    "thinking": true,
    "vision": true,
    "default": false,
    "trained": false,
    "summary": "Fast browser model for quick theory doubts, definitions and RAG lookups on modest laptops."
  },
  {
    "id": "sideris-aether",
    "name": "Sideris Aether",
    "tier": "Main offline",
    "backend": "webgpu",
    "repo": "onnx-community/Qwen3.5-4B-ONNX",
    "base": "Qwen3.5-4B",
    "dtype": "q4f16",
    "sizeLabel": "~2.5 GB",
    "minRamGb": 8,
    "thinking": true,
    "vision": true,
    "default": false,
    "trained": false,
    "summary": "Main downloadable in-browser engineering tutor across all five subjects: step-by-step algebra, Socratic mode and bilingual ES/EN."
  },
  {
    "id": "sideris-orion",
    "name": "Sideris Orion",
    "tier": "Deep calculus",
    "backend": "webgpu",
    "repo": "onnx-community/Phi-4-mini-instruct-web-q4f16",
    "base": "Phi-4-mini-reasoning",
    "dtype": "q4f16",
    "sizeLabel": "~2.3 GB",
    "minRamGb": 8,
    "thinking": true,
    "vision": false,
    "default": false,
    "trained": false,
    "summary": "Pure calculus and derivation specialist for ODEs, Navier-Stokes, hydrostatics and 3D kinematics."
  },
  {
    "id": "sideris-titan",
    "name": "Sideris Titan",
    "tier": "Local heavy",
    "backend": "ollama",
    "repo": "qwen3.5:9b",
    "base": "Qwen3.5-9B",
    "endpoint": "http://localhost:11434/v1",
    "sizeLabel": "~5.5 GB (GGUF)",
    "minRamGb": 16,
    "thinking": true,
    "vision": true,
    "default": false,
    "trained": false,
    "summary": "High-capacity local model via Ollama or LM Studio (also supports GLM-4.7-Flash on 24+ GB machines)."
  }
];
