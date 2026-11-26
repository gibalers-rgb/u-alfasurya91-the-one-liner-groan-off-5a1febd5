#!/usr/bin/env python3
"""The One-Liner Groan-Off -- entry program.

Writes a single original one-line dad joke to /output/entry.txt.

The bounty gate requires the file to hold UTF-8 text of 1 to 140
characters, a single line, and not only whitespace, so the program
checks the line against those rules before it writes anything.

The joke itself turns on an envelope doing what envelopes do:
an envelope seals by being licked, so "licking my wounds" is both
the idiom for nursing a hurt and, literally, an envelope's job.
"""

from pathlib import Path
import sys

JOKE = "I told the envelope it was too sealed off. It said, 'I'm just licking my wounds.'"

MAX_CHARS = 140
DEFAULT_OUTPUT_PATH = Path("/output/entry.txt")


def validate(line: str) -> str:
    """Return the line if it passes the gate rules, else raise."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    return line


def write_entry(line: str, path: Path) -> None:
    """Write the line and read it back to prove the file matches."""
    path.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character in the file.
    path.write_text(line, encoding="utf-8")
    written = path.read_bytes().decode("utf-8")
    if written != line:
        raise ValueError(f"read-back mismatch in {path}")
    print(f"wrote {len(line)} characters to {path}")


def main(argv: list[str]) -> None:
    line = validate(JOKE)
    output = Path(argv[1]) if len(argv) > 1 else DEFAULT_OUTPUT_PATH
    write_entry(line, output)


if __name__ == "__main__":
    main(sys.argv)
