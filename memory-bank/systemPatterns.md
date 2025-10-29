# System Patterns

## Architecture
- Static site served via `http-server` from `public/`.
- Three.js app (ES modules) with import map to CDN (`unpkg`).
- Assets downloaded by script into `public/models/`.

## Key patterns
- Import map resolves `three` and `three/examples/jsm/` to CDN URLs.
- Progressive model loading in `public/index.html`:
  - Prefer OBJ+MTL, else OBJ, else STL.
  - HEAD checks used to detect available files.
  - Auto-framing function computes bounding box and positions camera/controls.
- Asset script (`scripts/download_assets.sh`):
  - Accepts `MODEL_URL` to fetch .zip/.obj/.stl.
  - TLS fallback for POC only (`curl -k`/`wget --no-check-certificate`).
  - Zip extraction via `unzip` or Python `zipfile` fallback.
  - Renames main files to `model.obj`/`model.mtl`/`model.stl`.

## Conventions
- Public root: `public/`.
- AnatomyTool assets: `public/models/anatomytool/`.
- Default model (POC): coloured skull OBJ zip.

## Decisions (Phase 1)
- Use CDN for Three.js to avoid build tooling.
- Use `http-server` for fastest static hosting.
- Keep code minimal; no custom UI.
