# AR Heritage India

An educational heritage exploration website featuring five Indian monuments, monument-specific history and timelines, interactive 3D models, AR entry points, browser narration and short quizzes. Built with Flask, HTML, CSS, JavaScript and Google `<model-viewer>`.

## Features

- Responsive home page and five individual monument pages
- Flask JSON API for monument records and quizzes
- Hosted, detailed Sketchfab Taj Mahal viewer; the original supplied Taj GLB remains available through a separate local viewer with supported AR handoff
- Local supplied GLB files for the other four monuments, served to `<model-viewer>` with camera controls, auto-rotation, reset framing and AR modes (`webxr scene-viewer quick-look`)
- Gallery images hosted by Wikimedia Commons, with browser fallback when unavailable
- Monument-specific speech-synthesis narration with play, pause and stop
- Five multiple-choice questions per monument, score, feedback and restart
- Project docs, Windows launcher and Python dependency list

## Requirements and launch

Requires Windows 10/11, Python 3.10+, `cloudflared` for automatic HTTPS phone AR preview, and an internet connection for dependency install, Google Fonts, the `<model-viewer>` module and Wikimedia gallery images.

1. Extract the project folder.
2. Double-click `run.bat` (or run it from Command Prompt).
3. The launcher creates `.venv`, installs Flask, starts the server and opens `http://127.0.0.1:5000` on the computer. If `cloudflared` is installed, it also starts a temporary HTTPS tunnel in another window.
4. Keep both windows open during use. Press Ctrl+C in the Cloudflare window to stop the HTTPS link; press Ctrl+C in the server window to stop the site.

### Preview on a phone on the same Wi-Fi

For HTTPS and AR, open the `https://…trycloudflare.com` link printed in the Cloudflare window. It works from any network and is temporary. Anyone with the link can access the demo while the tunnel is running. If `cloudflared` is absent, the launcher falls back to same-Wi-Fi local HTTP and prints the **PHONE URL**; that mode supports the site preview but not WebXR AR.

For manual startup: `python -m venv .venv`, activate it, `pip install -r requirements.txt`, then `python backend/app.py`.

## AR compatibility

The 3D viewer works in modern browsers with WebGL support. The AR button is available only where supported: WebXR requires a compatible browser/device and an HTTPS secure context; Scene Viewer is intended for supported Android devices; Quick Look is intended for Apple devices. A phone connecting to the computer over plain local HTTP may not qualify for WebXR, though compatible Scene Viewer or Quick Look handoff can still be offered. Device, browser, camera permission and AR software affect availability. For reliable WebXR, deploy behind HTTPS. A physical AR-capable device was not available for verification.

## API

- `GET /api/health`
- `GET /api/monuments`
- `GET /api/monuments/<id>`
- `GET /api/quiz/<id>`

Monument IDs: `sanchi`, `taj-mahal`, `konark`, `hampi`, `qutub-minar`.

## Project structure

```text
AR-Heritage-India/
├── run.bat, README.md, requirements.txt
├── backend/app.py
├── backend/data/monuments.json
├── frontend/index.html
├── frontend/pages/{sanchi,taj-mahal,konark,hampi,qutub-minar}.html
├── frontend/css/style.css
├── frontend/js/{home,monument}.js
├── frontend/models/ (five supplied GLB files)
└── docs/ (project, system, install, tests, credits)
```

## Models and sources

All five GLBs supplied with the request remain included without changing their geometry or materials; filenames were normalized to the project specification. The Taj Mahal page defaults to a hosted Sketchfab model for a more detailed appearance and needs internet access. Its local viewer keeps the supplied GLB available as an AR option. Sketchfab listing identity/licensing and caveats are recorded in [HERITAGE_AND_ASSET_CREDITS.md](docs/HERITAGE_AND_ASSET_CREDITS.md). Gallery images are served directly from Wikimedia Commons Special:FilePath endpoints and need an internet connection. The application does not bundle third-party photos.

## Troubleshooting

- If startup reports that Python is missing, install Python 3 and enable its PATH option, then run `run.bat` again.
- If Flask fails to install, check internet access and retry `run.bat`.
- Gallery images use confirmed Wikimedia Commons file titles and require internet access. If one is unavailable, its tile shows a visible fallback; the source link on each gallery caption opens the file's Commons page.
- If the 3D viewer reports an error, confirm `frontend/models/` contains the named GLB and reload. High-detail models can take time or exceed the memory available on older phones.
- If the AR button is unavailable, use the interactive 3D viewer or try a supported mobile device and browser.
- Narration depends on browser speech-synthesis voices.

## Documentation

See `docs/PROJECT_OVERVIEW.md`, `FEATURES.md`, `SYSTEM_ARCHITECTURE.md`, `INSTALLATION_GUIDE.md`, `TESTING.md`, and `HERITAGE_AND_ASSET_CREDITS.md`.
