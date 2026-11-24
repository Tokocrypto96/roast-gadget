#!/usr/bin/env python3
"""One-line roast of a gadget I use every day.

Writes a single original roast line to /output/entry.txt.
Stdlib only.
"""

import os

ROAST = (
    "My phone's alarm snoozes itself after nine minutes, like it's the one "
    "who needs more sleep \u2014 then blames me for being late."
)


MAX_CHARS = 200


def main() -> None:
    line = ROAST.strip()
    if not line or len(line) > MAX_CHARS:
        raise ValueError(f"roast must be 1-{MAX_CHARS} chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
