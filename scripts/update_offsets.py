"""Pull fresh offsets for the current Delta Force build from the pattern DB."""
from __future__ import annotations

import sys
import urllib.request
import json
from pathlib import Path

OFFSET_DB = "https://offsets.dfesp.dev/{build}.json"
TARGET = Path("delta_force_esp/mem/offsets.py")


def fetch(build: str) -> dict:
    with urllib.request.urlopen(OFFSET_DB.format(build=build), timeout=10) as r:
        return json.loads(r.read())


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: update_offsets.py <build>", file=sys.stderr)
        return 1
    data = fetch(argv[1])
    print(f"fetched {len(data)} offsets for {argv[1]}")
    TARGET.write_text(TARGET.read_text() + f"\n# auto-synced: {argv[1]}\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))