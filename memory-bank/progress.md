# Progress

## What works (Phase 1 + Phase 2 Complete)
- Devcontainer serves site via `http-server` on port 8080.
- `public/index.html` loads AnatomyTool model and renders in browser.
- Orbit, pan, and zoom via OrbitControls.
- Asset script downloads AnatomyTool archives and unpacks to `public/models/anatomytool/`.
- **GLB/GLTF**: Loader with progressive fallback (GLB→OBJ+MTL→OBJ→STL).
- **Textures validated**: DamagedHelmet.glb sample loads textured.
- **OBJ→GLB attempt**: Conversion path wired (obj2gltf currently failing, falls back).
- **Nerve pipeline**: `scripts/fetch_nerves.py/.sh` probe/download GLBs and write `public/models/nerves/manifest.json` + `ATTRIBUTION.txt`.
- **App nerve loader**: Reads manifest, groups nerves under `nerveGroup`; keyboard toggles (1–9/0, a/h/s/f) for visibility/solo/frame.
- **UI Panel**: CN I–XII checkboxes with Show All/Hide All/Solo/Frame buttons. UI syncs with keyboard shortcuts.
- **Sample Assets**: 4 seeded GLB files (CN_I, CN_II, CN_III, CN_VII) load and can be individually controlled.
- **Provider Pattern**: `fetch_nerves.py` supports multiple providers (Caskanatomy, Zanatomy scaffolding).
- **Script Hardening**: Removed TLS bypass; proper CA trust now required.
- **Performance**: Draco decoding enabled for compressed GLBs; emissive highlighting for active nerves.
- **Attribution**: CC BY 4.0 compliance with proper attribution format and license text.

## What's left / Upcoming (Phase 3)
- Implement cutaneous territory marking: skin texture overlay with paint/unpaint tools, sharable state URLs.
- Expand nerve asset sources: add real cranial nerve GLBs from Z-Anatomy or other CC BY 4.0 sources.
- Add basic performance monitoring and texture compression for larger models.
- UI polish: tooltips, better responsive design, About panel linking to attributions.

## Known issues / caveats
- Current default OBJ renders untextured (no MTL in zip).
- caskanatomy.info SSL certificate issues prevent automatic fetching (expected after TLS hardening).
- Sample nerve GLBs are DamagedHelmet copies for testing; replace with real anatomical models.
- Favicon 404 from server is benign.
