#!/usr/bin/env python3
"""Invent a Word We Need — entry program.

Writes one invented English word with a one-line definition to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The coinage: tabnesia — the instant forgetting of why you opened a
new browser tab. Everyone who lives in a browser has felt it, and
English has no single word for it until now.
"""

import os

# One invented word plus a one-line definition, at most 140 chars.
ENTRY = "tabnesia (n.): the instant forgetting of why you opened a new browser tab."


def resolve_dirs():
    """Return (input_dir, output_dir) from the environment, with fallbacks."""
    input_dir = os.environ.get("MAKEFUN_INPUT_DIR", "/input")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return input_dir, output_dir


def main():
    _input_dir, output_dir = resolve_dirs()
    # Create the output directory if missing; never delete it.
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
