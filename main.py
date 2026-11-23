#!/usr/bin/env python3
"""news-image-20261123 entry (Python 3.13, standard library only).

Copies the rendered image assets/entry.png to /output/entry.png.
No network, no wall clock, no randomness: the output is a byte-for-byte
copy of the image in this repository, so repeated runs write identical bytes.

Before copying, the bundled image is validated: it must exist, carry a
valid PNG signature, and stay within the competition's 1 MiB limit; a
bad image fails loudly instead of producing a broken entry.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys
from pathlib import Path

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576  # 1 MiB, the competition's image size limit

HERE = Path(__file__).resolve().parent
SRC = HERE / "assets" / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


if not SRC.is_file():
    fail(f"bundled image missing: {SRC} does not exist")

size = SRC.stat().st_size
if size > MAX_BYTES:
    fail(f"bundled image too large: {size} bytes exceeds the 1 MiB limit")

with SRC.open("rb") as f:
    header = f.read(len(PNG_SIGNATURE))
if header != PNG_SIGNATURE:
    fail("bundled image is not a valid PNG (bad 8-byte signature)")

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, OUT_DIR / "entry.png")
