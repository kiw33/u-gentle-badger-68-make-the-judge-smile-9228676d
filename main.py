#!/usr/bin/env python3
"""make.fun entry: Make the Judge Smile (u-gentle-badger-68-make-the-judge-smile-9228676d).

Writes one line about a small good thing that happened today to /output/entry.txt. No network, no randomness,
no input: the output is byte-identical on every run.
"""

ENTRY = "My neighbour's cat followed me home from the bus stop, sat on my doorstep, and waited until I said goodnight before trotting off."
# The single submitted one line about a small good thing that happened today; keep byte-identical, do not reword.


def write_entry(path: str) -> None:
    """Write the entry to ``path`` as UTF-8 with no trailing newline."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main() -> None:
    write_entry("/output/entry.txt")


if __name__ == "__main__":
    main()
