# Progress

## What works (Phase 1 POC)
- Devcontainer serves site via `http-server` on port 8080.
- `public/index.html` loads AnatomyTool model and renders in browser.
- Orbit, pan, and zoom via OrbitControls.
- Asset script downloads AnatomyTool archives and unpacks to `public/models/anatomytool/`.

## What’s left / Upcoming
- Use GLB (with textures) for richer visuals or OBJ+MTL where available.
- Model selection UX and swap mechanism.
- Performance validation with larger/complex head/neck models.
- Begin Phase 2: nerve visualization design.

## Known issues / caveats
- Current default OBJ renders untextured (no MTL in zip).
- TLS fallback (`-k`) used in script for POC convenience; remove when CA trust is configured.
- Favicon 404 from server is benign.
