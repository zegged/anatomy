# Progress

## What works (Phase 1 + Phase 2 Complete)
- Devcontainer serves site via `http-server` on port 8080.
- `public/index.html` loads AnatomyTool model and renders in browser.
- Orbit, pan, and zoom via OrbitControls.
- Asset script downloads AnatomyTool archives and unpacks to `public/models/anatomytool/`.
- **GLB/GLTF**: Loader with progressive fallback (GLB→OBJ+MTL→OBJ→STL).
- **Textures validated**: DamagedHelmet.glb sample loads textured.
- **OBJ→GLB attempt**: Conversion path wired (obj2gltf currently failing, falls back).
- **Nerve pipeline**: Provider-based `scripts/fetch_nerves.py` writes `public/models/nerves/manifest.json` + `ATTRIBUTION.txt`.
- **App nerve loader**: Reads manifest, groups nerves under `nerveGroup`; keyboard toggles (1–9/0, a/h/s/f) for visibility/solo/frame.
- **UI Panel**: CN I–XII checkboxes with Show All/Hide All/Solo/Frame buttons. UI syncs with keyboard shortcuts.
- **Sample Assets (placeholders)**: 5 GLB files (CN_I, CN_II, CN_III, CN_V, CN_VII) are functional for pipeline validation.
- **Performance**: Draco decoding enabled for compressed GLBs; emissive highlighting for active nerves.
- **Attribution**: CC BY 4.0 compliance for placeholders with license text present.

## What's left / Upcoming (BodyParts3D + Phase 3)
- Integrate BodyParts3D meshes for CN II, CN V, CN VII:
  - Fetch OBJ/STL, convert to GLB (Blender CLI or obj2gltf), optional Draco.
  - Update manifest with `source: BodyParts3D`, `license: CC BY-SA 2.1 JP`, per-asset attribution.
  - Add `public/licenses/CC-BY-SA-2.1.txt` and ensure ShareAlike compliance.
- Implement cutaneous territory marking: skin texture overlay with paint/unpaint tools, sharable state URLs.
- Add basic performance monitoring and texture compression for larger models.
- UI polish: tooltips, better responsive design, About/Attribution panel.

## Known issues / caveats
- Current default OBJ renders untextured (no MTL in zip).
- caskanatomy.info SSL certificate issues prevent automatic fetching (expected after TLS hardening).
- Placeholders are not anatomical nerves; replace with BodyParts3D assets when ready.
- Mixing licenses: placeholders (CC BY), BodyParts3D (CC BY-SA 2.1) require ShareAlike notices when distributed together.
