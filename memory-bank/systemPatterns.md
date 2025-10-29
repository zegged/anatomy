# System Patterns

## Architecture
- Static site served via `http-server` from `public/`.
- Three.js app (ES modules) with import map to CDN (`unpkg`).
- Assets downloaded by script into `public/models/`.
- Nerve assets managed via provider-based fetch script into `public/models/nerves/` with `manifest.json`.

## Key patterns
- Import map resolves `three` and `three/examples/jsm/` to CDN URLs.
- Progressive base model loading in `public/index.html`:
  - Prefer GLB/GLTF; else OBJ+MTL; else OBJ; else STL.
  - HEAD checks used to detect available files (via fetch) for base assets.
  - Auto-framing function computes bounding box and positions camera/controls.
- Nerve loading flow:
  - `scripts/fetch_nerves.py` uses providers (e.g., `CaskanatomyProvider`, `ZanatomyProvider` scaffolding) to discover/download assets.
  - Generates `public/models/nerves/manifest.json` (v1) with entries:
    - `{ id, name, file, source, license, attribution }` under `{"nerves": []}`.
  - App loads manifest, adds models under `nerveGroup`, initially hidden; `idToNerve` maps ids to objects.
  - Controls:
    - Keyboard: 1–9/0 (CN I–X), `a` show-all, `h` hide-all, `s` solo last, `f` frame last.
    - UI Panel: checkboxes per CN I–XII + Show All/Hide All/Solo/Frame buttons; UI stays in sync with scene.
  - Highlight: simple emissive highlight for active nerve.
- Asset scripts:
  - `scripts/download_assets.sh`: fetches zip/raw models; extracts; normalizes filenames; optional OBJ→GLB conversion when available.
  - TLS verification enforced (no bypass); failures surface clearly.
- Performance
  - Draco decoding enabled via `DRACOLoader` for compressed GLBs.

## Conventions
- Public root: `public/`.
- AnatomyTool assets: `public/models/anatomytool/`.
- Default model (POC): coloured skull OBJ zip.
- Nerves: `public/models/nerves/` with `manifest.json`, GLBs named by nerve id (e.g., `CN_VII.glb`).
- Licenses: `public/licenses/` contains license texts (e.g., CC BY 4.0; add CC BY-SA 2.1 for BodyParts3D).

## Decisions
- Use CDN for Three.js to avoid build tooling.
- Use `http-server` for fastest static hosting.
- Keep code minimal with a small built-in UI.
- Do not scrape embedded viewers; only use direct/downloadable assets when available.
- TLS verification enforced; bypass removed.

## Upcoming (asset pipeline)
- BodyParts3D meshes (OBJ/STL) → GLB via Blender CLI or `obj2gltf`; optional Draco compression with glTF-Transform; update `manifest.json` and attribution accordingly.
