"""Print the one-line warning label for humans.

The label itself lives in entry.txt so the text and the runner stay
separate; this script only loads the line and writes it to stdout.
"""

from pathlib import Path


def load_label() -> str:
    here = Path(__file__).resolve().parent
    text = (here / "entry.txt").read_text(encoding="utf-8")
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) != 1:
        raise ValueError("entry.txt must hold exactly one non-empty line")
    return lines[0].strip()


def main() -> None:
    print(load_label())


if __name__ == "__main__":
    main()
