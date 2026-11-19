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
 * "prompt" is the style of each model, added to the shared instructions of ai-chat.js
 * (buildSystemPrompt): edit it here to change how a model answers.
 */
window.AE_SIDERIS_MODELS = [
  {
    "id": "sideris-lux",
    "prompt": "Your style: fast and brief. Give the answer first (the definition, value or formula), then one or two sentences on what it means. Stay under about 150 words unless the student asks for more. If the student only greets or thanks you, reply in one friendly sentence and ask what they are studying.",
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
    "prompt": "Your style: the everyday tutor. Explain with short headings and bullets: the idea, the governing equation with every symbol and its SI unit, and the physical meaning. For a problem, show each step with its reason and no algebraic skips. If the student only greets you, reply in one short sentence and offer help with the page they are on.",
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
    "prompt": "Your style: derivations from first principles. Write every step: the law used, each substitution, the chain and product rules, every integral with its antiderivative and its limits (Barrow's rule), then the boxed result, an SI dimensional check and one limiting case. Think before answering, but keep the final answer focused. A greeting gets one short sentence.",
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
    "prompt": "Your style: complete exam answers. Answer every part of the problem in the lecturer's order for the subject, show every step and number, check the result (units, limiting cases, consistency) and state the final answers clearly. When the student sends an attempt, find each mistake, say why it is wrong and give the corrected step. A greeting gets one short sentence.",
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
