#!/usr/bin/env python3
"""
Fetch cranial nerve GLB models from caskanatomy.info mirror.
Attempts direct GLB URLs, downloads available ones, and generates manifest.json.
"""

import json
import os
import sys
import ssl
import urllib.request
import urllib.error
from pathlib import Path

# Configuration
BASE_URL = "https://caskanatomy.info/open3dviewer/3dmodels"
DEST_DIR = Path("/workspaces/anatomy/public/models/nerves")

# Cranial nerve definitions with candidate slugs
CRANIAL_NERVES = [
    {
        "id": "CN_I",
        "name": "Olfactory Nerve",
        "slugs": ["olfactory-nerve", "nervus-olfactorius"],
        "credit": "Open3D project; Denise M.J. Arnold MD et al",
        "license": "CC BY-SA 4.0"
    },
    {
        "id": "CN_II",
        "name": "Optic Nerve",
        "slugs": ["optic-nerve", "nervus-opticus"],
        "credit": "Open3D project; Denise M.J. Arnold MD et al",
        "license": "CC BY-SA 4.0"
    },
    {
        "id": "CN_III",
        "name": "Oculomotor Nerve",
        "slugs": ["oculomotor-nerve", "nervus-oculomotorius"],
        "credit": "Open3D project; Denise M.J. Arnold MD et al",
        "license": "CC BY-SA 4.0"
    },
    {
        "id": "CN_IV",
        "name": "Trochlear Nerve",
        "slugs": ["trochlear-nerve", "nervus-trochlearis"],
        "credit": "Open3D project; Denise M.J. Arnold MD et al",
        "license": "CC BY-SA 4.0"
    },
    {
        "id": "CN_V",
        "name": "Trigeminal Nerve",
        "slugs": ["trigeminal-nerve", "nervus-trigeminus"],
        "credit": "Open3D project; Denise M.J. Arnold MD et al",
        "license": "CC BY-SA 4.0"
    },
    {
        "id": "CN_VI",
        "name": "Abducens Nerve",
        "slugs": ["abducens-nerve", "nervus-abducens"],
        "credit": "Open3D project; Denise M.J. Arnold MD et al",
        "license": "CC BY-SA 4.0"
    },
    {
        "id": "CN_VII",
        "name": "Facial Nerve",
        "slugs": ["facial-nerve", "nervus-facialis"],
        "credit": "Open3D project; Denise M.J. Arnold MD et al",
        "license": "CC BY-SA 4.0"
    },
    {
        "id": "CN_VIII",
        "name": "Vestibulocochlear Nerve",
        "slugs": ["vestibulocochlear-nerve", "nervus-vestibulocochlearis", "vestibular-cochlear-nerve"],
        "credit": "Open3D project; Denise M.J. Arnold MD et al",
        "license": "CC BY-SA 4.0"
    },
    {
        "id": "CN_IX",
        "name": "Glossopharyngeal Nerve",
        "slugs": ["glossopharyngeal-nerve", "nervus-glossopharyngeus"],
        "credit": "Open3D project; Denise M.J. Arnold MD et al",
        "license": "CC BY-SA 4.0"
    },
    {
        "id": "CN_X",
        "name": "Vagus Nerve",
        "slugs": ["vagus-nerve", "nervus-vagus"],
        "credit": "Open3D project; Denise M.J. Arnold MD et al",
        "license": "CC BY-SA 4.0"
    },
    {
        "id": "CN_XI",
        "name": "Accessory Nerve",
        "slugs": ["accessory-nerve", "nervus-accessorius"],
        "credit": "Open3D project; Denise M.J. Arnold MD et al",
        "license": "CC BY-SA 4.0"
    },
    {
        "id": "CN_XII",
        "name": "Hypoglossal Nerve",
        "slugs": ["hypoglossal-nerve", "nervus-hypoglossus"],
        "credit": "Open3D project; Denise M.J. Arnold MD et al",
        "license": "CC BY-SA 4.0"
    },
]


# Create SSL context that doesn't verify certificates (POC only)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

def check_glb_url(url):
    """Check if GLB URL exists by HEAD request."""
    try:
        req = urllib.request.Request(url, method='HEAD')
        response = urllib.request.urlopen(req, timeout=10, context=ssl_context)
        return response.status == 200
    except Exception as e:
        print(f"Error checking {url}: {e}", file=sys.stderr)
        return False


def download_glb(url, dest_path):
    """Download GLB file to destination."""
    try:
        with urllib.request.urlopen(url, timeout=30, context=ssl_context) as response:
            with open(dest_path, 'wb') as f:
                while True:
                    chunk = response.read(8192)
                    if not chunk:
                        break
                    f.write(chunk)
        print(f"Downloaded {url} -> {dest_path}")
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}", file=sys.stderr)
        return False


def main():
    """Main fetch logic."""
    # Create destination directory
    DEST_DIR.mkdir(parents=True, exist_ok=True)

    manifest = []
    attributions = []

    for nerve in CRANIAL_NERVES:
        found = False

        # Try each slug for this nerve
        for slug in nerve["slugs"]:
            glb_url = f"{BASE_URL}/{slug}/{slug}.glb"

            if check_glb_url(glb_url):
                # Download the GLB
                dest_path = DEST_DIR / f"{nerve['id']}.glb"
                if download_glb(glb_url, dest_path):
                    # Add to manifest
                    manifest.append({
                        "id": nerve["id"],
                        "name": nerve["name"],
                        "url": glb_url,
                        "localPath": f"./models/nerves/{nerve['id']}.glb",
                        "license": nerve["license"],
                        "credit": nerve["credit"]
                    })

                    # Add attribution
                    attributions.append(f"{nerve['id']} ({nerve['name']}): {nerve['credit']}, {nerve['license']}")

                    found = True
                    break

        if not found:
            print(f"No GLB found for {nerve['id']} ({nerve['name']})")

    # Write manifest
    manifest_path = DEST_DIR / "manifest.json"
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"Wrote manifest to {manifest_path}")

    # Write attributions
    attrib_path = DEST_DIR / "ATTRIBUTION.txt"
    with open(attrib_path, 'w') as f:
        f.write("Cranial Nerve Models - Attributions\n")
        f.write("===================================\n\n")
        f.write("All models are licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)\n")
        f.write("Source: Open3D project (anatomytool.org), caskanatomy.info mirror\n\n")
        f.write("\n".join(attributions))
        f.write("\n\nFor full license text: https://creativecommons.org/licenses/by-sa/4.0/\n")
    print(f"Wrote attributions to {attrib_path}")

    print(f"Successfully processed {len(manifest)} cranial nerves")
    return 0


if __name__ == "__main__":
    sys.exit(main())
