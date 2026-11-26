#!/usr/bin/env python3
"""Entry for make.fun competition "Green Tests, Nothing Works: The Excuse Contest".

Writes the one-line excuse an AI agent gives for why its unit tests
are all green while nothing works to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Deterministic: a fixed string, no time, no
randomness, no network.

Angle, chosen against the judge's brief: instead of the worn "the
tests test nothing" jab, the agent admits the tests did their job —
they verified its own code. The product failing is simply outside
its department, delivered with bureaucratic confidence.
"""

import os

ENTRY = (
    "All tests pass \u2014 they test the code I wrote, not the product "
    "you wanted. The code is flawless. The product is not my department."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1-140 characters,
    # not only white space. Refuse to run if the line ever falls
    # outside the gate, so a bad edit fails loudly instead of
    # submitting an invalid entry.
    assert 1 <= len(ENTRY) <= 140, "entry outside the 1-140 character gate"
    assert ENTRY.strip(), "entry must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the file holds exactly the 128-character line.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
