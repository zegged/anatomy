# Active Context

## Current focus
- POC verified: load AnatomyTool model in-browser with Three.js, orbit/pan/zoom working.

## Recent changes
- `Dockerfile`: Node.js 20 + `http-server`; added `wget`/`unzip`.
- `scripts/download_assets.sh`: accepts `MODEL_URL`, handles `.zip/.obj/.stl`, TLS fallback (POC-only), Python unzip fallback, auto-renames to `model.*`.
- `public/index.html`: import map; OBJ/MTL/STL loaders; auto-detect available files; auto-frame camera.
- Default model: AnatomyTool coloured skull (OBJ zip) → renders (untextured).

## Decisions
- Keep CDN-based Three.js (no bundler yet).
- Prioritize pipeline reliability before UI/features.

## Next steps (proposed)
1) Swap to GLB package for textures (use GLTFLoader) or fetch OBJ+MTL variant when available.
2) Add simple UI toggle to load different models via `MODEL_URL` (optional scaffolding).
3) Validate performance with larger/head-neck models; consider Draco/glTF-transform if needed.
4) Prepare Phase 2 scope: initial nerve visualization strategy (assets audit + selection logic).
