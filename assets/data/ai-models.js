/*!
 * Aerospace Engineering Study Portal: Sideris model catalogue.
 *
 * Loaded on study pages by assets/js/theme.js right after assets/data/sideris-config.js and
 * before assets/js/ai-rag.js, ai-engine.js and ai-chat.js. Keep everything between the brackets
 * pure JSON (tools/tests/test_ai_chat.py parses it directly).
 *
 * Every model answers from the cloud at once (Cloudflare Worker, assets/data/sideris-config.js).
 * A model with "localTier" (1 small, 2 mid-size) and offlineBackend "webgpu" also installs itself
 * on computers of that tier or above (ai-engine.js, local: "repo" is its Hugging Face ONNX repo,
 * "sizeMB" its download size for space checks and wait times) and from then on answers there.
 * Titan has no localTier yet: it stays in the cloud until it is exported to ONNX.
 */
window.AE_SIDERIS_MODELS = [
  {
    "id": "sideris-lux",
    "localTier": 1,
    "sizeMB": 1300,
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
    "localTier": 2,
    "sizeMB": 2500,
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
    "localTier": 2,
    "sizeMB": 2300,
    "maxTokens": 6000,
    "reasoning": true,
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
    "maxTokens": 6000,
    "reasoning": true,
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
