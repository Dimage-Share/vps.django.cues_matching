#!/usr/bin/env python3
# Simple selector: given manifest and project root checks, print applicable files in order.
import sys
import json
import fnmatch
from pathlib import Path
import yaml


def load_manifest(path):
    return yaml.safe_load(path.read_text())


def matches_any(patterns, files):
    for p in patterns:
        for f in files:
            if fnmatch.fnmatch(f, p):
                return True
    return False


def find_project_files(root):
    return [str(p) for p in Path(root).rglob("*") if p.is_file()]


def select(manifest, project_root):
    project_files = find_project_files(project_root)
    applicable = []
    for entry in manifest.get("files", []):
        pats = entry.get("applies_to", ["*"])
        if matches_any(pats, project_files) or "*" in pats:
            applicable.append(entry)
    # sort by priority asc (lower first) so higher priority runs later
    applicable.sort(key=lambda e: e.get("priority", 0))
    return applicable


def main():
    if len(sys.argv) != 3:
        print(
            "usage: select_instructions.py manifest.yaml /path/to/project_root"
        )
        sys.exit(2)
    manifest = load_manifest(Path(sys.argv[1]))
    ap = select(manifest, sys.argv[2])
    print(json.dumps(ap, indent=2))


if __name__ == "__main__":
    main()
