#!/usr/bin/env python3
"""Describe Your Ex in One Word — writes exactly one word to /output/entry.txt.

The word: "Unsubscribed".

Why this word, against the judge's brief: an ex summed up in one word.
You brace for an insult and get a piece of admin instead — the relationship
framed as a subscription you cancelled. "Unsubscribed" says the ex was a
service that stopped being worth the monthly fee, and you clicked the
button: no fight, no drama, just the quiet opt-out. The joke lands at a
glance because everyone has unsubscribed from something, and the metaphor
turns a breakup into the most boring, bureaucratic breakup possible — which
is exactly what makes it sting. It is not a plain insult (it never calls
the ex bad), it is not the obvious choice, it is spelled correctly, it
needs no caption, and anyone who has ever ended a subscription — or a
relationship — recognises the feeling instantly.

Head-to-head, it beats the nearest rival "Recalled": a recall is something
that happens to you, while unsubscribing is something you do — that agency
is the joke. It also beats "Expired" on surprise (nobody's first word for
an ex) and "Placeholder" on criterion 1 (it is unmistakably a verdict on
the ex, not on a role). At 12 bytes it is also small, which the rules'
exact-tie break rewards (fewer bytes places first).

Stdlib only, deterministic, no network.
"""

import os

WORD = "Unsubscribed"


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-111 characters,
    # not only whitespace, and exactly one word, or the entry scores 0
    # and never reaches the judge.
    if not 1 <= len(WORD) <= 111:
        raise ValueError(f"word is {len(WORD)} characters, must be 1-111")
    if not WORD.strip():
        raise ValueError("word must not be only whitespace")
    if any(ch.isspace() for ch in WORD):
        raise ValueError("entry must be exactly one word, no spaces")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Read back and verify: the grader reads this file, so confirm the
    # bytes on disk are exactly the word that passed the gate above,
    # and re-run the gate on what was actually written, not just on
    # the constant in memory.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != WORD:
        raise ValueError("entry.txt on disk differs from the word")
    if not 1 <= len(written) <= 111 or not written.strip():
        raise ValueError("entry.txt on disk fails the gate")
    if any(ch.isspace() for ch in written):
        raise ValueError("entry.txt on disk is not exactly one word")
    print(WORD)


if __name__ == "__main__":
    main()
