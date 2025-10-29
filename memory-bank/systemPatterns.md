# System Patterns

## Architecture
- Static site served via `http-server` from `public/`.
- Three.js app (ES modules) with import map to CDN (`unpkg`).
- Assets downloaded by script into `public/models/`.
 - Nerve assets fetched by Python script into `public/models/nerves/` with `manifest.json`.

## Key patterns
- Import map resolves `three` and `three/examples/jsm/` to CDN URLs.
- Progressive base model loading in `public/index.html`:
  - Prefer GLB/GLTF; else OBJ+MTL; else OBJ; else STL.
  - HEAD checks used to detect available files (via fetch) for base assets.
  - Auto-framing function computes bounding box and positions camera/controls.
- Nerve loading flow:
  - `scripts/fetch_nerves.py/.sh` probe direct GLB URLs on caskanatomy mirror; download if present.
  - Generates `public/models/nerves/manifest.json` listing available nerves and attributions.
  - App loads manifest, adds models under `nerveGroup`, initially hidden.
  - Keyboard toggles: 1–9/0 (CN I–X), `a` show-all, `h` hide-all, `s` solo last, `f` frame last.
- Asset script (`scripts/download_assets.sh`):
  - Accepts `MODEL_URL` to fetch .zip/.obj/.stl.
  - TLS fallback for POC only (`curl -k`/`wget --no-check-certificate`).
  - Zip extraction via `unzip` or Python `zipfile` fallback.
  - Renames main files to `model.obj`/`model.mtl`/`model.stl` (and attempts OBJ→GLB conversion).

## Conventions
- Public root: `public/`.
- AnatomyTool assets: `public/models/anatomytool/`.
- Default model (POC): coloured skull OBJ zip.
 - Nerves: `public/models/nerves/` with `manifest.json`, GLBs named by nerve id (e.g., `CN_VII.glb`).

## Decisions (Phase 1)
- Use CDN for Three.js to avoid build tooling.
- Use `http-server` for fastest static hosting.
- Keep code minimal; no custom UI.
 - Do not scrape embedded viewers; only use direct GLB links when available.
 - Allow TLS verification bypass in fetch scripts for POC only (to be removed later).
