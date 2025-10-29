# Progress

## What works (Phase 1 POC + GLB Support)
- Devcontainer serves site via `http-server` on port 8080.
- `public/index.html` loads AnatomyTool model and renders in browser.
- Orbit, pan, and zoom via OrbitControls.
- Asset script downloads AnatomyTool archives and unpacks to `public/models/anatomytool/`.
- **NEW**: GLB/GLTF loader with progressive fallback (GLB→OBJ+MTL→OBJ→STL).
- **NEW**: Textured rendering validated with DamagedHelmet.glb sample.
- **NEW**: Asset pipeline extended to handle GLB/GLTF files and attempt OBJ→GLB conversion.

## What's left / Upcoming
- Fix obj2gltf conversion tool (currently failing with dependency issues).
- Model selection UX and swap mechanism.
- Performance optimization for very large models.
- Phase 2 implementation: nerve visualization with isolation controls.

## Known issues / caveats
- Current default OBJ renders untextured (no MTL in zip).
- TLS fallback (`-k`) used in script for POC convenience; remove when CA trust is configured.
- Favicon 404 from server is benign.
