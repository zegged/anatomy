# Active Context

## Current focus
- Phase 2 completed: cranial nerve UI, assets, and hardening implemented. Ready for Phase 3 (cutaneous marking) or asset expansion.

## Recent changes
- **UI Panel**: Added minimal CN I–XII panel in `public/index.html` with checkboxes, Show All/Hide All/Solo/Frame buttons. Keyboard shortcuts (1–9/0, a/h/s/f) remain functional and sync with UI.
- **Sample Assets**: Seeded 4 GLB files (CN_I, CN_II, CN_III, CN_VII) using DamagedHelmet.glb for testing. Updated `manifest.json` with proper schema including `file`, `source`, `license`, `attribution` fields.
- **Script Hardening**: Removed TLS bypass (`-k/--no-check-certificate`) from `download_assets.sh` and `fetch_nerves.py`. Now uses proper CA trust.
- **Provider Pattern**: Refactored `fetch_nerves.py` with abstract `NerveProvider` base class. Added `CaskanatomyProvider` (active) and `ZanatomyProvider` (scaffolding with manual mappings).
- **Performance**: Enabled Draco decoding via `DRACOLoader` (CDN) for compressed GLBs. Added emissive highlighting for active nerves and improved framing.
- **Attribution**: Updated `ATTRIBUTION.txt` with CC BY 4.0 format for sample assets. Added full CC BY 4.0 license text at `public/licenses/CC-BY-4.0.txt`.

## Decisions
- Keep CDN-based Three.js (no bundler yet).
- Prefer GLB/GLTF for performance/visuals; maintain OBJ/MTL/STL fallbacks.
- Bypass AnatomyTOOL viewer; only use direct GLB links (no scraping embeds).
- Removed TLS bypass; proper CA trust now required.
- CC BY 4.0 as working license for nerve assets (more permissive than CC BY-SA 4.0).

## Next steps (Phase 3 preparation)
1) Implement cutaneous territory marking: skin texture overlay with paint/unpaint tools, sharable state URLs.
2) Expand nerve asset sources: add real cranial nerve GLBs from Z-Anatomy or other CC BY 4.0 sources.
3) Add basic performance monitoring and texture compression for larger models.
4) Consider UI polish: tooltips, better responsive design, About panel linking to attributions.
