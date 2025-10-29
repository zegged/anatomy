# Tech Context

## Stack
- Runtime: Node.js 20 (installed via NodeSource)
- Static server: `http-server@14`
- 3D engine: Three.js (CDN via unpkg)
- Loaders: GLTFLoader, OBJLoader, MTLLoader, STLLoader (examples/jsm)
- Language: JavaScript ES modules in `public/index.html`

## Environment
- Devcontainer with host networking (`--net=host`), GPU flags present (future use).
- Base image: Ubuntu 24.04 (Dockerfile)
- Tools: `curl`, `wget`, `unzip` (or Python `zipfile` fallback), `bash`, Python 3.12

## Project structure
- `public/index.html` – app entry
- `public/models/anatomytool/` – downloaded models (`model.obj|model.mtl|model.stl`)
- `scripts/download_assets.sh` – asset automation
 - `public/models/nerves/` – cranial nerve GLBs + `manifest.json` + `ATTRIBUTION.txt`
 - `scripts/fetch_nerves.py` / `scripts/fetch_nerves.sh` – probe/download nerves and build manifest

## CDN/import map
- `three` → `https://unpkg.com/three@0.157.0/build/three.module.js`
- `three/examples/jsm/` → `https://unpkg.com/three@0.157.0/examples/jsm/`

## Commands
- Download model: `MODEL_URL=<url> bash scripts/download_assets.sh`
- Fetch cranial nerves (best-effort): `bash scripts/fetch_nerves.sh`
- Serve: `http-server public -p 8080 -c-1 --cors`
- Open: `http://localhost:8080`

## Notes
- TLS fallback (`-k` / `--no-check-certificate`) and SSL verification bypass in Python are used only to unblock POC; remove when CA trust is configured.
- OBJ-only models render untextured; prefer GLB for textures when available.
- Nerve manifest may be empty if no direct GLBs are available from the mirror; app handles this gracefully.
