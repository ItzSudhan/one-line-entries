"""Copy this repository's entry.txt, unchanged, to the make.fun output directory.

The output directory is $MAKEFUN_OUTPUT_DIR, or /output when it is unset.
The program refuses to write anything if entry.txt is missing, empty,
only white space, or not valid UTF-8. It writes the exact bytes it read,
so every run produces an identical file.
"""

import os
import sys
from pathlib import Path

ENTRY_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    source = Path(__file__).resolve().parent / ENTRY_NAME
    try:
        data = source.read_bytes()
    except FileNotFoundError:
        fail(f"{source} does not exist")

    if not data:
        fail(f"{source} is empty")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        fail(f"{source} is not valid UTF-8 ({exc})")
    if not text.strip():
        fail(f"{source} holds only white space")

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / ENTRY_NAME
    target.write_bytes(data)
    print(f"wrote {len(text)} characters ({len(data)} bytes) to {target}")


if __name__ == "__main__":
    main()
