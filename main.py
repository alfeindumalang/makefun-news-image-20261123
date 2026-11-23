#!/usr/bin/env python3
"""news-image-20261123 entry (Python 3.13, standard library only).

Copies the rendered image assets/entry.png to /output/entry.png.
No network, no wall clock, no randomness: the output is a byte-for-byte
copy of the image in this repository, so repeated runs write identical bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "assets" / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, OUT_DIR / "entry.png")
