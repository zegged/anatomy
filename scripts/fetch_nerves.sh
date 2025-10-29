#!/usr/bin/env bash
set -euo pipefail

# Fetch cranial nerve GLB models
# This is a thin wrapper around fetch_nerves.py

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

echo "Fetching cranial nerve GLB models..."
python3 scripts/fetch_nerves.py
echo "Done."
