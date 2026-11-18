#!/usr/bin/env python3
"""news-image-20261118 — sum up 18 November 2026's world news in one image.

Deterministically writes the pre-rendered front-page image (entry.png,
stored next to this script) to ``$MAKEFUN_OUTPUT_DIR/entry.png``
(default ``/output``). Standard library only; no network access.
"""

import os
import shutil
from pathlib import Path

SOURCE_NAME = "entry.png"


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    if not source.is_file():
        raise FileNotFoundError(f"missing bundled image: {source}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / SOURCE_NAME
    shutil.copyfile(source, destination)
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
