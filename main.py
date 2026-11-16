"""make.fun bounty ai-excited-01 entry: "Koi Emas Menembus Lukisan".

The program copies the bundled image (entry.jpg) to /output/entry.png.

Determinism: the output is a byte-for-byte copy of entry.jpg — no pixels
are generated, resized, or re-encoded, no timestamps or random values are
involved, and the output filename is fixed. Two runs therefore produce
byte-identical output: sha256 of the output always equals sha256 of
entry.jpg.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

# The bundled entry image, resolved next to this script.
ENTRY = Path(__file__).resolve().parent / "entry.jpg"


def main() -> None:
    # Output directory: /output inside the grader, or MAKEFUN_OUTPUT_DIR
    # when set (local runs / tests).
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    # Create the directory if it does not exist yet.
    out_dir.mkdir(parents=True, exist_ok=True)
    # Byte-for-byte copy — this is the whole program; nothing is transformed.
    shutil.copyfile(ENTRY, out_dir / "entry.png")


if __name__ == "__main__":
    main()
