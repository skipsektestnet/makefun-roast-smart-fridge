"""Roast the Smart Fridge: writes the entry text to /output/entry.txt.

Why this line: the fridge as a snitch — it texts you about your own
midnight snacking, so the punch reframes the phone as knowing your
habits before your doctor does. Specific, concrete, one breath.
Fresh angle: not the stock milk-ordering joke, but the fridge
ratting you out to your own phone.
"""

import os

# The entry itself: one sentence, 131 characters.
ENTRY = "My smart fridge texts me every time I open it past midnight, so now my phone knows about my snacking problem before my doctor does."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: sealed gate needs 1-160 chars, not only white space.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert len(ENTRY) <= 160, "entry exceeds 160 characters"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
