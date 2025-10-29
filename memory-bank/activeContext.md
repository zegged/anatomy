# Active Context

## Current focus
- Prep for integrating BodyParts3D cranial nerve meshes (CC BY-SA 2.1) to replace placeholder GLBs for CN II, CN V, and CN VII. Maintain current UI/loader while sourcing and converting assets.

## Recent changes
- **Z-Anatomy Integration (placeholder)**: Added 3 cranial nerve entries (CN II, V, VII) using DamagedHelmet GLB placeholders to validate pipeline/UI. Manifest updated with `file`, `source`, `license`, `attribution` fields.
- **UI Panel**: Minimal CN I–XII panel in `public/index.html` with checkboxes, Show All/Hide All/Solo/Frame buttons. Keyboard shortcuts (1–9/0, a/h/s/f) remain functional and sync with UI.
- **Sample Assets**: 5 GLB files total (CN_I, CN_II, CN_III, CN_V, CN_VII) currently placeholders. `manifest.json` uses stable schema.
- **Script Hardening**: Removed TLS bypass; strict CA verification enabled for downloads.
- **Provider Pattern**: `fetch_nerves.py` now uses a provider model (`CaskanatomyProvider`, `ZanatomyProvider` scaffolding).
- **Performance**: Draco decoding via `DRACOLoader` (CDN); emissive highlighting; improved framing.
- **Attribution**: `ATTRIBUTION.txt` uses per-asset lines; `public/licenses/CC-BY-4.0.txt` added.

## Decisions
- Proceed with BodyParts3D as a near-term source for cranial nerves under **CC BY-SA 2.1**.
- Track and comply with ShareAlike obligations (include license text, attribution, indicate changes, ensure downstream license compatibility).
- Keep CDN-based Three.js; prefer GLB/GLTF; maintain OBJ/MTL/STL fallbacks.
- TLS verification enforced; no bypass.

## Next steps (queued)
1) Acquire BodyParts3D meshes for CN II, CN V, CN VII (OBJ/STL if available).
2) Convert meshes to GLB (Blender CLI or obj2gltf), optionally apply Draco compression.
3) Update `public/models/nerves/manifest.json` entries to point to the new GLBs; set `source: "BodyParts3D"`, `license: "CC BY-SA 2.1 JP"`, and proper attribution.
4) Add `public/licenses/CC-BY-SA-2.1.txt` and expand `ATTRIBUTION.txt` with BodyParts3D credit lines and change notes.
5) Smoke-test UI (toggle/solo/frame/highlight), verify performance and console cleanliness.
