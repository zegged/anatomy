#!/usr/bin/env bash
set -euo pipefail
MODEL_URL="${MODEL_URL:-https://caskanatomy.info/open3dmodelfiles/overview-colored-skull/overview-colored-skull-obj.zip}"
ASSET_DIR="/workspaces/anatomy/public/models/anatomytool"
TMP_DIR=$(mktemp -d)
mkdir -p "$ASSET_DIR"
FNAME=$(basename "$MODEL_URL")

download() {
  local url="$1"; local dest="$2"
  if command -v curl >/dev/null 2>&1; then
    if ! curl -L -o "$dest" "$url"; then
      echo "curl failed, retrying without certificate verification (POC only)" >&2
      curl -L -k -o "$dest" "$url"
    fi
  elif command -v wget >/dev/null 2>&1; then
    if ! wget -q -O "$dest" "$url"; then
      echo "wget failed, retrying without certificate verification (POC only)" >&2
      wget --no-check-certificate -q -O "$dest" "$url"
    fi
  else
    echo "Error: neither curl nor wget found. Install one of them." >&2
    exit 3
  fi
}

download "$MODEL_URL" "$TMP_DIR/$FNAME"
case "$FNAME" in
  *.zip)
    extract_zip() {
      local zipfile="$1"; local outdir="$2"
      if command -v unzip >/dev/null 2>&1; then
        unzip -q "$zipfile" -d "$outdir"
      else
        python3 - "$zipfile" "$outdir" <<'PY'
import sys, zipfile, os
zip_path = sys.argv[1]
out_dir = sys.argv[2]
os.makedirs(out_dir, exist_ok=True)
with zipfile.ZipFile(zip_path, 'r') as z:
    z.extractall(out_dir)
PY
      fi
    }
    extract_zip "$TMP_DIR/$FNAME" "$TMP_DIR/unzipped"
    # Move extracted contents into ASSET_DIR
    SRC=$(find "$TMP_DIR/unzipped" -mindepth 1 -maxdepth 1 | head -n1)
    if [ -d "$SRC" ]; then
      cp -r "$SRC"/* "$ASSET_DIR/" 2>/dev/null || true
      cp -r "$SRC"/.* "$ASSET_DIR/" 2>/dev/null || true
    else
      cp -r "$TMP_DIR/unzipped"/* "$ASSET_DIR/" 2>/dev/null || true
      cp -r "$TMP_DIR/unzipped"/.* "$ASSET_DIR/" 2>/dev/null || true
    fi
    # Rename files to expected names (find the main OBJ, MTL, STL, GLB files and rename them)
    find "$ASSET_DIR" -name "*.glb" | head -n1 | xargs -I {} mv {} "$ASSET_DIR/model.glb" 2>/dev/null || true
    find "$ASSET_DIR" -name "*.gltf" | head -n1 | xargs -I {} mv {} "$ASSET_DIR/model.gltf" 2>/dev/null || true
    find "$ASSET_DIR" -name "*.obj" | head -n1 | xargs -I {} mv {} "$ASSET_DIR/model.obj" 2>/dev/null || true
    find "$ASSET_DIR" -name "*.mtl" | head -n1 | xargs -I {} mv {} "$ASSET_DIR/model.mtl" 2>/dev/null || true
    find "$ASSET_DIR" -name "*.stl" | head -n1 | xargs -I {} mv {} "$ASSET_DIR/model.stl" 2>/dev/null || true

    # Convert OBJ to GLB if OBJ exists but GLB doesn't (for better textures/performance)
    if [ -f "$ASSET_DIR/model.obj" ] && [ ! -f "$ASSET_DIR/model.glb" ]; then
      echo "Converting OBJ to GLB for better rendering..."
      if command -v npx >/dev/null 2>&1; then
        npx obj2gltf -i "$ASSET_DIR/model.obj" -o "$ASSET_DIR/model.glb" || echo "GLB conversion failed, keeping OBJ"
      else
        echo "npx not available, skipping GLB conversion"
      fi
    fi
    ;;
  *.obj|*.stl|*.mtl|*.glb|*.gltf)
    cp "$TMP_DIR/$FNAME" "$ASSET_DIR/model.${FNAME##*.}"
    ;;
  *) echo "Unsupported extension: $FNAME"; exit 2;;
esac
ls -lah "$ASSET_DIR"
