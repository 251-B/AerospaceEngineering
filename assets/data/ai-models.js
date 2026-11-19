/*!
 * Aerospace Engineering Study Portal: Sideris model catalogue.
 *
 * Loaded on study pages by assets/js/theme.js right after assets/data/sideris-config.js and
 * before assets/js/ai-rag.js, ai-engine.js and ai-chat.js. Keep everything between the brackets
 * pure JSON (tools/tests/test_ai_chat.py parses it directly).
 *
 * Every Sideris model works in TWO modes (Instant 0 MB is the default; Offline / Local lives
 * under Advanced settings):
 *   - Instant (0 MB download) -> runs immediately via the Cloudflare Worker proxy
 *     (assets/data/sideris-config.js) on desktop and mobile with zero setup;
 *   - Offline / Local         -> downloads ONNX weights into the browser (WebGPU) or connects
 *     to local Ollama / LM Studio, including custom fine-tuned Sideris checkpoints.
 */
window.AE_SIDERIS_MODELS = [
  {
    "id": "sideris-lux",
    "name": "Sideris Lux",
    "tier": "Fast",
    "bestFor": "Quick definitions, formula lookups and short theory doubts",
    "backend": "cloud",
    "offlineBackend": "webgpu",
    "repo": "onnx-community/Qwen3.5-2B-ONNX",
    "base": "Qwen3.5-2B",
    "dtype": "q4f16",
    "sizeLabel": "0 MB · Instant",
    "offlineSizeLabel": "~1.3 GB",
    "minRamGb": 4,
    "thinking": false,
    "vision": true,
    "default": false,
    "trained": false,
    "summary": "Fastest response time for crisp definitions, symbol meanings and quick course-note checks."
  },
  {
    "id": "sideris-aether",
    "name": "Sideris Aether",
    "tier": "Recommended",
    "bestFor": "Everyday study, theory explanations and Socratic tutoring",
    "backend": "cloud",
    "offlineBackend": "webgpu",
    "repo": "onnx-community/Qwen3.5-4B-ONNX",
    "base": "Qwen3.5-4B",
    "dtype": "q4f16",
    "sizeLabel": "0 MB · Instant",
    "offlineSizeLabel": "~2.5 GB",
    "minRamGb": 8,
    "thinking": true,
    "vision": true,
    "default": true,
    "trained": false,
    "summary": "Balanced flagship tutor across all five UC3M subjects: clear step-by-step algebra, Socratic mode and bilingual ES/EN."
  },
  {
    "id": "sideris-orion",
    "name": "Sideris Orion",
    "tier": "Deep calculus",
    "bestFor": "ODEs, Navier-Stokes, hydrostatics and 3D kinematics derivations",
    "backend": "cloud",
    "offlineBackend": "webgpu",
    "repo": "onnx-community/Phi-4-mini-instruct-web-q4f16",
    "base": "Phi-4-mini-reasoning",
    "dtype": "q4f16",
    "sizeLabel": "0 MB · Instant",
    "offlineSizeLabel": "~2.3 GB",
    "minRamGb": 8,
    "thinking": true,
    "vision": false,
    "default": false,
    "trained": false,
    "summary": "Thinks visibly step by step before answering, with a collapsible reasoning trace for heavy derivations and proofs."
  },
  {
    "id": "sideris-titan",
    "name": "Sideris Titan",
    "tier": "Max depth",
    "bestFor": "Multi-part exam problems, full solutions and checking full attempts",
    "backend": "cloud",
    "offlineBackend": "ollama",
    "repo": "qwen3.5:9b",
    "base": "Qwen3.5-9B",
    "endpoint": "http://localhost:11434/v1",
    "sizeLabel": "0 MB · Instant",
    "offlineSizeLabel": "~5.5 GB (Ollama)",
    "minRamGb": 16,
    "thinking": true,
    "vision": true,
    "default": false,
    "trained": false,
    "summary": "Largest reasoning budget for long exam problems, full worked derivations and deep error checking."
  }
];
