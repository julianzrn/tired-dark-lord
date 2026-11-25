"""Entry for make.fun's "The Tired Dark Lord: A 100-Word Villain Monologue".

Running this program writes the entry text to /output/entry.txt.
"""

from pathlib import Path

OPENING = (
    "Ten thousand years I have kept this throne warm for a prophecy that "
    "keeps rescheduling. My armies stand ready. My curses are polished. "
)
DEFLECTION = (
    "Somewhere below, a hero is climbing my tower, and I find myself "
    "hoping he takes the stairs slowly. Not from fear. The torches "
    "gutter, the hall echoes, and every triumph tastes of cold iron "
    "and old smoke. "
)
RESOLVE = (
    "When he arrives, I shall rise, I shall thunder, I shall give him "
    "the speech — the good one, with the laugh. "
)
CLOSE = "Then, win or lose, perhaps... rest. Even darkness, hero, must eventually close its eyes."

ENTRY = OPENING + DEFLECTION + RESOLVE + CLOSE

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the entry text to the output file, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
