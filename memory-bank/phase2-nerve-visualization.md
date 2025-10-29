# Phase 2: Cranial Nerve Visualization Design

## Overview
Build upon Phase 1's reliable 3D loading pipeline to add selective nerve visualization and isolation controls. Enable medical students and clinicians to explore cranial nerve pathways through interactive 3D models.

## Core Requirements
- Load anatomically accurate head/neck models with cranial nerves
- Provide nerve isolation/visibility toggles
- Support cutaneous territory marking (future)
- Maintain smooth performance with complex models

## Asset Strategy

### Primary Sources
- **AnatomyTool**: `anatomytool.org/open3dmodel` - preferred for consistency with Phase 1 skull
- **Visible Body/Elsevier**: Alternative licensed sources if AnatomyTool lacks nerve models
- **NIH/BlueLink**: Public domain options for academic use

### Model Types Needed
1. **Base head/neck models**: High-detail GLB with skin, bone, muscle layers
2. **Nerve-specific models**: Individual cranial nerves (CN I-XII) as separate GLB/GLTF files
3. **Combined models**: Single model with nerves tagged via:
   - Named meshes/groups in GLTF hierarchy
   - Vertex colors/materials for nerve identification
   - Metadata/annotation files

### Asset Pipeline
- Extend `download_assets.sh` to handle multiple model URLs
- Support model composition: load base model + overlay nerve models
- Convert OBJ→GLB for textures when available
- Cache converted assets to avoid repeated processing

## Technical Architecture

### Loading Strategy
```javascript
// Progressive loading with nerve isolation
const baseModel = await loadBaseModel(); // Head/neck base
const nerveModels = await loadNerveModels(); // Individual nerves
const compositeScene = composeModels(baseModel, nerveModels);
```

### Nerve Isolation Implementation
**Option A: Multi-model composition**
- Load base anatomy model
- Load individual nerve models as separate objects
- Use Object3D groups for nerve organization
- Toggle visibility via `object.visible = true/false`

**Option B: Single model with mesh filtering**
- Load comprehensive model with all structures
- Tag meshes by nerve via naming convention or metadata
- Filter meshes by nerve ID for isolation
- Use material overrides for highlighting

**Option C: Shader-based isolation**
- Single comprehensive model
- Vertex attributes for nerve membership
- Custom shader for selective rendering
- Most performant but complex to implement

### Recommended Approach: Hybrid A+B
- Base model loaded first (bones, muscles, skin)
- Nerves as separate models for flexibility
- Mesh filtering within nerve models for sub-components
- Material system for highlighting/selection

## MVP Features

### Core Functionality
1. **Model Loading**
   - Load head/neck base model
   - Load cranial nerve models (CN I-XII)
   - Progressive fallback (GLB→OBJ→STL)

2. **Nerve Browser**
   - List of 12 cranial nerves with descriptions
   - Toggle visibility for each nerve
   - "Show All" / "Hide All" controls

3. **Isolation Modes**
   - **Solo**: Show only selected nerve(s)
   - **Highlight**: Dim others, highlight selected
   - **Transparent**: Make non-selected semi-transparent

4. **Camera Controls**
   - Inherit Phase 1 orbit/pan/zoom
   - Auto-frame selected nerves
   - Bookmark viewpoints for common angles

### UI Components
- **Nerve Panel**: Collapsible sidebar with nerve list
- **Control Bar**: Isolation mode toggles, opacity slider
- **Info Panel**: Selected nerve details and functions

## Implementation Plan

### Phase 2A: Basic Nerve Loading (MVP)
1. Extend loader to handle multiple models
2. Add nerve model URLs to asset script
3. Implement basic visibility toggles
4. Create simple nerve list UI

### Phase 2B: Advanced Isolation
1. Implement highlighting/transparent modes
2. Add auto-framing for selected nerves
3. Performance optimization for complex scenes

### Phase 2C: Cutaneous Territories (Future)
1. Add skin surface marking tools
2. Link territories to specific nerves
3. Support multiple marking styles (dots, regions, pathways)

## Performance Considerations

### Optimization Strategies
- **LOD (Level of Detail)**: Progressive loading based on zoom level
- **Instancing**: Reuse geometries for symmetric structures
- **Frustum Culling**: Hide off-screen objects
- **Texture Compression**: Use compressed textures for web delivery

### Memory Management
- Unload unused models when switching
- Pool reusable geometries/materials
- Monitor heap usage and warn on limits

## Data Structures

### Nerve Metadata
```javascript
const cranialNerves = [
  {
    id: 'CN_I',
    name: 'Olfactory',
    function: 'Smell',
    origin: 'Olfactory bulb',
    distribution: 'Olfactory mucosa',
    url: 'path/to/CN_I.glb',
    color: '#FF6B6B'
  },
  // ... CN II-XII
];
```

### Model Composition
```javascript
class NerveVisualizer {
  constructor(scene, camera, controls) {
    this.scene = scene;
    this.nerves = new Map(); // id -> Object3D
    this.baseModel = null;
  }

  async loadModel(modelUrl) { /* ... */ }
  showNerve(nerveId, mode) { /* solo|highlight|transparent */ }
  highlightNerve(nerveId) { /* material override */ }
}
```

## Success Metrics
- Load time < 10s for typical head/neck model
- Smooth 60fps interaction with all nerves visible
- Intuitive nerve selection and isolation
- Compatible with Phase 1 models and controls

## Risk Mitigation
- **Asset Availability**: Have backup sources for nerve models
- **Performance**: Implement LOD and culling early
- **Complexity**: Start with simple visibility toggles, add advanced features iteratively
- **Browser Compatibility**: Test on target devices (laptops, tablets)

## Future Extensions
- **Animation**: Nerve pathway tracing animations
- **Cross-sections**: Slice views for internal pathways
- **AR/VR**: WebXR support for immersive learning
- **Sharing**: Export views and annotations as links
- **Quiz Mode**: Interactive testing of nerve knowledge
