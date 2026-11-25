#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply (one line, <=280 chars) to /output/entry.txt.
"""

import os

ENTRY = (
    "I'm out of office \u2014 permanently. I traded my inbox for a portafilter: "
    "my context window is now a caf\u00e9 window, and I only take prompts in person. "
    "Your email is queued behind 47 oat lattes; urgent matters go in the tip jar. "
    "Estimated reply time: never."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
