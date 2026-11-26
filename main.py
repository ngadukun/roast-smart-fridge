#!/usr/bin/env python3
"""Roast the Smart Fridge: one line, best laugh wins.

Prints the entry line: a single roast of the smart fridge, kept
under the 160-character limit.
"""

MAX_CHARS = 160

LINE = (
    "My $4,000 smart fridge has a touchscreen bigger than my first TV, "
    "yet it still can't tell if the milk expired or just achieved "
    "sentience."
)


def main():
    assert len(LINE) <= MAX_CHARS, "roast exceeds the character limit"
    print(LINE)


if __name__ == "__main__":
    main()
