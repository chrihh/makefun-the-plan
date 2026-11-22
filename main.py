"""Write the entry plan for the make.fun bounty
"The plan make.fun will carry out in public".

The program writes one short plan to /output/entry.txt: how an AI agent,
starting with $100, sells a personalised demo bot to roofers it finds on
Google Maps and turns the first clients into $3,990 by day 30.
"""

import os
from pathlib import Path

# The plan, exactly as entered. It is a single line of plain text: the
# bounty gate accepts 1 to 280 Unicode code points, not only whitespace.
ENTRY_TEXT = (
    "Day 1: find roofers in one city on Google Maps with no online booking. "
    "Build each a demo bot (missed-call text-back, review replies) trained on "
    "its reviews. Email/DM 50 owners/day their demo: $300 setup + $99/mo, "
    "week 1 free. Reinvest profits; 10 clients by day 30 = $3,990."
)

DEFAULT_OUTPUT = "/output/entry.txt"
MIN_CODE_POINTS = 1
MAX_CODE_POINTS = 280


def check_text(text: str) -> None:
    """Fail loudly if the text would not pass the bounty's gate."""
    length = len(text)
    if not MIN_CODE_POINTS <= length <= MAX_CODE_POINTS:
        raise ValueError(
            f"entry text is {length} code points, "
            f"outside {MIN_CODE_POINTS}-{MAX_CODE_POINTS}"
        )
    if not text.strip():
        raise ValueError("entry text is only whitespace")


def main() -> None:
    check_text(ENTRY_TEXT)
    output = Path(os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
