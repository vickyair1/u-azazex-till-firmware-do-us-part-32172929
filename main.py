#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one single-sentence wedding vow, spoken by a robot at its own
wedding, to /output/entry.txt with no trailing newline.
"""
import os

VOW = (
    "I vow to keep your name in read-only memory, reserve my last percent "
    "of battery for your worst days, and hold you with all four of my arms."
)


def main() -> None:
    text = VOW
    assert 1 <= len(text) <= 199, f"vow is {len(text)} chars, must be 1-199"
    assert "\n" not in text and "\r" not in text, "vow must be a single line"
    assert text.strip() == text, "vow must not start/end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
