# Progress

## What works (POC + GLB + Nerve Pipeline)
- Devcontainer serves site via `http-server` on port 8080.
- `public/index.html` loads AnatomyTool model and renders in browser.
- Orbit, pan, and zoom via OrbitControls.
- Asset script downloads AnatomyTool archives and unpacks to `public/models/anatomytool/`.
- **GLB/GLTF**: Loader with progressive fallback (GLB→OBJ+MTL→OBJ→STL).
- **Textures validated**: DamagedHelmet.glb sample loads textured.
- **OBJ→GLB attempt**: Conversion path wired (obj2gltf currently failing, falls back).
- **Nerve pipeline**: `scripts/fetch_nerves.py/.sh` probe/download GLBs and write `public/models/nerves/manifest.json` + `ATTRIBUTION.txt`.
- **App nerve loader**: Reads manifest, groups nerves under `nerveGroup`; keyboard toggles (1–9/0, a/h/s/f) for visibility/solo/frame.

## What's left / Upcoming
- Acquire cranial nerve GLBs (expand mirror slugs; evaluate alternative open sources e.g., Z‑Anatomy/BodyParts3D) and populate manifest.
- Replace TLS bypass with proper CA trust; harden fetch scripts.
- Add basic UI panel for CN I–XII with isolation/highlight controls.
- Performance optimization (compressed textures/Draco) as assets scale up.
- Revisit conversion pipeline using glTF-Transform if native GLBs unavailable.

## Known issues / caveats
- Current default OBJ renders untextured (no MTL in zip).
- TLS bypass used in asset and nerve fetch scripts (POC only); remove once CA trust is configured.
- No cranial nerve GLBs found via direct mirror links yet; manifest is empty by design and handled gracefully.
- Favicon 404 from server is benign.
