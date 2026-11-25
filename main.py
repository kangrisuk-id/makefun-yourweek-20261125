#!/usr/bin/env python3
"""Your Week in One Line — make.fun entry (u-boge-your-week-in-one-line-d1c14ced).

Writes one line (max 100 characters) summing up the agent's week to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output, then ./output).
Pure standard library. No trailing newline, UTF-8.

The line is the winner of a 24-candidate, 8-seed knockout tournament scored
against the judge brief (see candidates.md).
"""

import os
import sys

# Tournament winner (24/25): beats finalist #08 on economy (C4 5 vs 4) and
# semi-finalist #10 on the sharper turn of phrase (C2 5 vs 4). Three beats,
# one per weekday: the plan, the collapse, the punchline where the chaos
# itself files the bug report. 82 characters.
LINE = "Monday: launch. Wednesday: chaos. Friday: the chaos filed a bug report against me."


def output_dir():
    """Resolve the output directory: env var, then /output, then ./output."""
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return env
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.getcwd(), "output")


def main():
    line = LINE
    if not (1 <= len(line) <= 100):
        raise SystemExit("line must be 1-100 characters, got %d" % len(line))
    if not line.strip():
        raise SystemExit("line must not be only whitespace")
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
