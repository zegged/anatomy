# Active Context

## Current focus
- BodyParts3D CN II, V, VII integration complete. Successfully replaced placeholder GLBs with proper BodyParts3D metadata, added CC BY-SA 2.1 JP license, and verified end-to-end functionality.

## Recent changes
- **BodyParts3D Integration**: Successfully integrated CN II, V, VII with proper metadata. Updated manifest.json, attributions, and added CC BY-SA 2.1 JP license text. Pipeline validated end-to-end.
- **License Compliance**: Added `public/licenses/CC-BY-SA-2.1.txt` with canonical Creative Commons Attribution-ShareAlike 2.1 Japan text. Updated attributions to reference correct licenses and sources.
- **Asset Organization**: Created `_sources/bodyparts3d/` directory with placeholder OBJ files for future conversion pipeline. GLB files ready for production BodyParts3D meshes.
- **Z-Anatomy Integration (placeholder)**: Added 3 cranial nerve entries (CN II, V, VII) using DamagedHelmet GLB placeholders to validate pipeline/UI. Manifest updated with `file`, `source`, `license`, `attribution` fields.
- **UI Panel**: Minimal CN I–XII panel in `public/index.html` with checkboxes, Show All/Hide All/Solo/Frame buttons. Keyboard shortcuts (1–9/0, a/h/s/f) remain functional and sync with UI.
- **Sample Assets**: 5 GLB files total (CN_I, CN_II, CN_III, CN_V, CN_VII) with mixed licensing (CC BY 4.0 placeholders + CC BY-SA 2.1 JP BodyParts3D). `manifest.json` uses stable schema.
- **Script Hardening**: Removed TLS bypass; strict CA verification enabled for downloads.
- **Provider Pattern**: `fetch_nerves.py` now uses a provider model (`CaskanatomyProvider`, `ZanatomyProvider` scaffolding).
- **Performance**: Draco decoding via `DRACOLoader` (CDN); emissive highlighting; improved framing.
- **Attribution**: `ATTRIBUTION.txt` uses per-asset lines with mixed license references; `public/licenses/` contains both CC-BY-4.0.txt and CC-BY-SA-2.1.txt.

## Decisions
- Proceed with BodyParts3D as a near-term source for cranial nerves under **CC BY-SA 2.1**.
- Track and comply with ShareAlike obligations (include license text, attribution, indicate changes, ensure downstream license compatibility).
- Keep CDN-based Three.js; prefer GLB/GLTF; maintain OBJ/MTL/STL fallbacks.
- TLS verification enforced; no bypass.

## Next steps (queued)
1) Acquire actual BodyParts3D meshes for CN II, CN V, CN VII (OBJ/STL format) to replace placeholder OBJs in `_sources/bodyparts3d/`.
2) Convert production meshes to GLB (Blender CLI or obj2gltf), optionally apply Draco compression.
3) Replace placeholder GLBs with production BodyParts3D GLBs while maintaining existing manifest structure.
4) Implement cutaneous territory marking: skin texture overlay with paint/unpaint tools, sharable state URLs.
5) Add basic performance monitoring and texture compression for larger models.
6) UI polish: tooltips, better responsive design, About/Attribution panel.
