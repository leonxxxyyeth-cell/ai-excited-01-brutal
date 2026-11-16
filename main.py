"""make.fun bounty ai-excited-01 entry: "Koi Emas Menembus Lukisan".

The program copies the bundled image (entry.jpg) to /output/entry.png.
It is fully deterministic: two runs produce byte-identical output.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

ENTRY = Path(__file__).resolve().parent / "entry.jpg"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ENTRY, out_dir / "entry.png")


if __name__ == "__main__":
    main()
