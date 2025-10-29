# Active Context

## Current focus
- GLB support implemented and validated; foundational cranial nerve pipeline added (auto-fetch + loader + keyboard toggles).

## Recent changes
- `public/index.html`:
  - Added GLTFLoader and GLB/GLTF-first progressive loader (GLB→OBJ+MTL→OBJ→STL).
  - Added cranial nerve loader reading `./models/nerves/manifest.json` into a dedicated `nerveGroup`.
  - Keyboard toggles: 1–9/0 toggle CN I–X; `a` show-all, `h` hide-all, `s` solo last, `f` frame last.
- `scripts/download_assets.sh`: Extended to handle GLB/GLTF and attempt OBJ→GLB (obj2gltf currently failing; falls back gracefully).
- New: `scripts/fetch_nerves.py` + `scripts/fetch_nerves.sh` probe caskanatomy mirror for direct GLB links, download if present, and generate `public/models/nerves/manifest.json` + `ATTRIBUTION.txt`.
- Validation: DamagedHelmet.glb renders with textures; AnatomyTool skull renders (OBJ fallback). Nerve manifest currently empty (no matching GLBs found via direct links).
- Documentation: Added `memory-bank/phase2-nerve-visualization.md` (design).

## Decisions
- Keep CDN-based Three.js (no bundler yet).
- Prefer GLB/GLTF for performance/visuals; maintain OBJ/MTL/STL fallbacks.
- Bypass AnatomyTOOL viewer; only use direct GLB links (no scraping embeds).
- Allow TLS verification bypass in scripts for POC only.

## Next steps (Phase 2 preparation)
1) Acquire cranial nerve GLB sources (expand mirror slugs; evaluate alternative open sources e.g., Z‑Anatomy/BodyParts3D) and populate manifest.
2) Replace TLS bypass with proper CA trust; harden fetch scripts.
3) Add minimal UI panel for CN I–XII list and isolation modes (replacing keyboard-only).
4) Implement framing/highlight polish and basic performance guards (texture compression / draco as needed).
5) Revisit OBJ→GLB conversion toolchain (gltf-transform pipeline) if GLBs are unavailable.
