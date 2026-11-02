# System architecture

```text
Browser (HTML/CSS/JavaScript)
   ├── Flask static hosting ── frontend files, GLB models
   ├── JSON API ────────────── backend/data/monuments.json
   ├── model-viewer module ─── local GLB + device AR integrations
   ├── SpeechSynthesis API ─── browser-generated narration
   └── Wikimedia Commons ──── remote gallery images
```

Flask loads the structured monument dataset once at startup and exposes read-only JSON routes. The frontend requests each record and renders shared page templates. No database or CORS layer is needed because the same Flask origin serves both API and frontend. Third-party image URLs and the model-viewer module require internet access.
