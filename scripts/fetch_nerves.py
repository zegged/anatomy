#!/usr/bin/env python3
"""
Fetch cranial nerve GLB models from multiple providers.
Attempts direct GLB URLs, downloads available ones, and generates manifest.json.
"""

import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path
from abc import ABC, abstractmethod

# Configuration
DEST_DIR = Path("/workspaces/anatomy/public/models/nerves")

class NerveProvider(ABC):
    """Abstract base class for nerve asset providers."""

    @abstractmethod
    def fetch_nerve(self, nerve_id, name, slugs):
        """Attempt to fetch a specific nerve. Returns asset info dict or None."""
        pass

class CaskanatomyProvider(NerveProvider):
    """Provider for caskanatomy.info mirror."""

    def __init__(self):
        self.base_url = "https://caskanatomy.info/open3dviewer/3dmodels"

    def fetch_nerve(self, nerve_id, name, slugs):
        """Try to fetch nerve from caskanatomy."""
        for slug in slugs:
            glb_url = f"{self.base_url}/{slug}/{slug}.glb"
            if self._check_glb_url(glb_url):
                dest_path = DEST_DIR / f"{nerve_id}.glb"
                if self._download_glb(glb_url, dest_path):
                    return {
                        "id": nerve_id,
                        "name": name,
                        "file": f"{nerve_id}.glb",
                        "source": "caskanatomy.info",
                        "license": "CC BY-SA 4.0",
                        "attribution": f"Open3D project; Denise M.J. Arnold MD et al — {glb_url}"
                    }
        return None

    def _check_glb_url(self, url):
        """Check if GLB URL exists by HEAD request."""
        try:
            req = urllib.request.Request(url, method='HEAD')
            response = urllib.request.urlopen(req, timeout=10)
            return response.status == 200
        except Exception as e:
            print(f"Error checking {url}: {e}", file=sys.stderr)
            return False

    def _download_glb(self, url, dest_path):
        """Download GLB file to destination."""
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
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


class ZanatomyProvider(NerveProvider):
    """Provider for Z-Anatomy. Manual mapping scaffolding."""

    def __init__(self):
        # Manual URL mappings for Z-Anatomy assets
        # TODO: Replace with actual Z-Anatomy GLB URLs when available
        self.manual_mappings = {
            # Example mappings (placeholder - replace with real URLs)
            # "CN_I": "https://zanatomy.net/models/olfactory_nerve.glb",
            # "CN_II": "https://zanatomy.net/models/optic_nerve.glb",
        }

    def fetch_nerve(self, nerve_id, name, slugs):
        """Try to fetch nerve from manual Z-Anatomy mappings."""
        if nerve_id in self.manual_mappings:
            glb_url = self.manual_mappings[nerve_id]
            if self._check_glb_url(glb_url):
                dest_path = DEST_DIR / f"{nerve_id}.glb"
                if self._download_glb(glb_url, dest_path):
                    return {
                        "id": nerve_id,
                        "name": name,
                        "file": f"{nerve_id}.glb",
                        "source": "Z-Anatomy",
                        "license": "CC BY 4.0",
                        "attribution": f"Z-Anatomy Contributors — {glb_url}"
                    }
        return None

    def _check_glb_url(self, url):
        """Check if GLB URL exists by HEAD request."""
        try:
            req = urllib.request.Request(url, method='HEAD')
            response = urllib.request.urlopen(req, timeout=10)
            return response.status == 200
        except Exception as e:
            print(f"Error checking {url}: {e}", file=sys.stderr)
            return False

    def _download_glb(self, url, dest_path):
        """Download GLB file to destination."""
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
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

def main():
    """Main fetch logic."""
    # Create destination directory
    DEST_DIR.mkdir(parents=True, exist_ok=True)

    # Initialize providers
    providers = [
        CaskanatomyProvider(),
        ZanatomyProvider()  # Scaffolding - manual mappings only for now
    ]

    manifest_nerves = []
    attributions = []

    for nerve in CRANIAL_NERVES:
        found = False

        # Try each provider
        for provider in providers:
            asset_info = provider.fetch_nerve(nerve["id"], nerve["name"], nerve["slugs"])
            if asset_info:
                manifest_nerves.append(asset_info)
                attributions.append(f"Asset: {nerve['id']} — {nerve['name']} (GLB)")
                attributions.append(f"Creator: {asset_info['attribution'].split(' — ')[0]}")
                attributions.append(f"Source: {asset_info['attribution'].split(' — ')[1]}")
                attributions.append(f"License: {asset_info['license']} — https://creativecommons.org/licenses/by-sa/4.0/")
                attributions.append("Changes: None (original)")
                attributions.append("")
                found = True
                break

        if not found:
            print(f"No GLB found for {nerve['id']} ({nerve['name']})")

    # Write manifest
    manifest_path = DEST_DIR / "manifest.json"
    manifest = {"nerves": manifest_nerves}
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
        f.write("For full license text: https://creativecommons.org/licenses/by-sa/4.0/\n")
    print(f"Wrote attributions to {attrib_path}")

    print(f"Successfully processed {len(manifest_nerves)} cranial nerves")
    return 0


if __name__ == "__main__":
    sys.exit(main())
