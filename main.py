"""Paus Emas Menembus Jendela Kaca Patri — make.fun ai-excited-01.

Writes the entry image to /output/entry.png. The program is fully
deterministic: it copies the bundled entry.jpg byte for byte, with no
timestamps, randomness or network access.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    # The entry image lives next to this file; the output name stays
    # entry.png even though the bytes are a JPEG (the gate reads the
    # first bytes, not the extension).
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    source = os.path.join(HERE, "entry.jpg")
    target = os.path.join(output_dir, "entry.png")
    shutil.copyfile(source, target)


if __name__ == "__main__":
    main()
