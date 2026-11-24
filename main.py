"""Print (and save) two lines about everyday things.

Exactly two lines, each at most 200 characters: a small, funny tribute
to the humble objects that quietly run our lives. Pure Python standard
library, deterministic, no network access. It prints the lines to
stdout and also writes them to /output/entry.txt, where the
competition's scorer reads them.
"""

import os

LINES = (
    "My mug has survived three moves, two breakups, and one earthquake of a Monday morning.",
    "The Wi-Fi router blinks like it knows all my secrets — and charges rent for keeping them.",
)


def main():
    text = "\n".join(LINES)
    print(text)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(text + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
