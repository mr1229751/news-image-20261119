"""Copy the bundled entry image into the output directory.

The output directory comes from the MAKEFUN_OUTPUT_DIR environment
variable and defaults to "/output". The destination is always named
"entry.png".
"""

import os
import shutil


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(output_dir, "entry.png"))


if __name__ == "__main__":
    main()
