# Tech Context

## Stack
- Runtime: Node.js 20 (installed via NodeSource)
- Static server: `http-server@14`
- 3D engine: Three.js (CDN via unpkg)
- Loaders: GLTFLoader, OBJLoader, MTLLoader, STLLoader (examples/jsm), DRACOLoader
- Language: JavaScript ES modules in `public/index.html`

## Environment
- Devcontainer with host networking (`--net=host`), GPU flags present (future use).
- Base image: Ubuntu 24.04 (Dockerfile)
- Tools: `curl`, `unzip` (or Python `zipfile` fallback), `bash`, Python 3.12

## Project structure
- `public/index.html` – app entry
- `public/models/anatomytool/` – downloaded models (`model.obj|model.mtl|model.stl`)
- `scripts/download_assets.sh` – asset automation
- `public/models/nerves/` – cranial nerve GLBs + `manifest.json` + `ATTRIBUTION.txt`
- `scripts/fetch_nerves.py` / `scripts/fetch_nerves.sh` – provider-based nerve fetch and manifest generation
- `public/licenses/` – bundled license texts (e.g., CC-BY-4.0.txt; add CC-BY-SA-2.1.txt)

## CDN/import map
- `three` → `https://unpkg.com/three@0.157.0/build/three.module.js`
- `three/examples/jsm/` → `https://unpkg.com/three@0.157.0/examples/jsm/`

## Commands
- Download model: `MODEL_URL=<url> bash scripts/download_assets.sh`
- Fetch cranial nerves (best-effort): `bash scripts/fetch_nerves.sh`
- Serve: `http-server public -p 8080 -c-1 --cors`
- Open: `http://localhost:8080`
- Convert (examples):
  - OBJ→GLB (Cesium): `npx obj2gltf -i input.obj -o output.glb`
  - Draco compress: `npx @gltf-transform/cli draco input.glb output.glb`
  - Blender CLI (generic): `blender -b -P scripts/convert_to_glb.py -- input.obj output.glb`

## Notes
- TLS verification is enforced (no `-k` / `--no-check-certificate`); configure CA trust if needed.
- OBJ-only models render untextured; prefer GLB.
- `manifest.json` (v1) schema is stable: `{"nerves": [{ id, name, file, source, license, attribution }]}`.
- Licensing: placeholders are CC BY 4.0; BodyParts3D uses CC BY-SA 2.1 JP—include license text and ShareAlike notices.
