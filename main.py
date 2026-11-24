#!/usr/bin/env python3
"""Entry for the make.fun bounty "Funniest Time Machine Warning Label".

Writes a single warning label for a time machine to /output/entry.txt.
Standard library only; deterministic; no network; no input files.
"""

import os

LINE = "WARNING: Never warn yourself. You won't listen. You never do. You already didn't."


def main():
    assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Round-trip check: what landed on disk must be the label, exactly.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        assert f.read() == LINE, "round-trip mismatch in /output/entry.txt"


if __name__ == "__main__":
    main()
