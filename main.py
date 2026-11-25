#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes one original one-line office joke to /output/entry.txt.
Standard library only; no network, no secrets, no input files.
"""

import os

ENTRY = "The office printer only jams when something is urgent, so I printed my will on it and now I'm immortal."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
