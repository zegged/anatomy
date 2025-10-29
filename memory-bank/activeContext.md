# Active Context

## Current focus
- GLB support implemented: textured rendering pipeline ready for Phase 2 nerve visualization.

## Recent changes
- `public/index.html`: Added GLTFLoader import and GLB/GLTF preference in progressive loader (GLB→OBJ+MTL→OBJ→STL).
- `scripts/download_assets.sh`: Extended to handle GLB/GLTF files and attempt OBJ→GLB conversion with obj2gltf.
- Asset pipeline: Successfully downloads AnatomyTool skull; conversion attempted (needs tool fix).
- Validation: GLB loading confirmed with DamagedHelmet.glb; skull renders via OBJ fallback.
- Documentation: Created comprehensive Phase 2 nerve visualization design doc.

## Decisions
- Keep CDN-based Three.js (no bundler yet).
- Prioritize textured GLB/GLTF support for better visuals.
- Hybrid asset approach: prefer GLB for performance, fall back gracefully.

## Next steps (Phase 2 preparation)
1) Fix obj2gltf tool dependency issues for reliable OBJ→GLB conversion.
2) Implement basic nerve model loading and visibility controls.
3) Add simple UI for nerve selection and isolation modes.
4) Source and integrate cranial nerve models from AnatomyTool or alternatives.
