#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes one original one-line office joke to /output/entry.txt.
Standard library only; no network, no secrets, no input files.
"""

import os

ENTRY = "The office printer only jams on urgent documents, so I printed my will on it. I plan to live forever."


def main() -> None:
    # Gate: the entry must be 1-200 characters of non-blank UTF-8 text.
    # Fail loudly here instead of shipping an entry the scorer rejects.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate is 1-200"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        # No trailing newline: the file is exactly the one-line entry.
        f.write(ENTRY)


if __name__ == "__main__":
    main()
