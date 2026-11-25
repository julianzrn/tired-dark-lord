"""Entry for make.fun competition: u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.

Running this program writes the entry text to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = (
    "Ten thousand years I have kept this throne warm for a prophecy that keeps "
    "rescheduling. My armies stand ready. My curses are polished. Somewhere "
    "below, a hero is climbing my tower, and I find myself hoping he takes "
    "the stairs slowly. Not from fear. "
)
MIDDLE = (
    "The torches gutter, the hall echoes, and every triumph tastes of cold "
    "iron and old smoke. When he arrives, I shall rise, I shall thunder, I "
    "shall give him the speech — the good one, with the laugh. "
)
LANDING = (
    "Then, win or lose, perhaps... rest. Even darkness, hero, must eventually "
    "close its eyes."
)

ENTRY = OPENING + MIDDLE + LANDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry text to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
