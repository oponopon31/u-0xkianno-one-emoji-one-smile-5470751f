#!/usr/bin/env python3
"""One Emoji, One Smile — entry writer.

Writes exactly one emoji to /output/entry.txt: the hugging face.

No arguments, no network, no randomness. The program is fully
deterministic: the same input (none) always yields the same bytes.
"""

import hashlib
import os
import sys


EMOJI = "\U0001F917"          # hugging face — one code point
OUTPUT_PATH = "/output/entry.txt"
FALLBACK_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def pick_destination() -> str:
    """Prefer the sandbox output directory; fall back to a local file."""
    out_dir = os.path.dirname(OUTPUT_PATH)
    try:
        os.makedirs(out_dir, exist_ok=True)
        return OUTPUT_PATH
    except OSError:
        return FALLBACK_PATH


def validate_payload(text: str) -> None:
    """Check the payload against the competition gate before writing."""
    if len(text) != 1:
        raise ValueError(f"expected exactly 1 character, got {len(text)}")
    if text.isspace():
        raise ValueError("payload must not be only whitespace")
    if ord(text) != 0x1F917:
        raise ValueError(f"unexpected code point U+{ord(text):04X}, expected U+1F917")
    encoded = text.encode("utf-8")
    if not 1 <= len(encoded) <= 8:
        raise ValueError(f"UTF-8 length {len(encoded)} outside 1-8 bytes")


def digest(path: str) -> str:
    """SHA-256 of a file, read in chunks."""
    hasher = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def main() -> int:
    validate_payload(EMOJI)

    target = pick_destination()
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)

    # Re-read what actually landed on disk and verify it round-trips.
    with open(target, "rb") as handle:
        raw = handle.read()
    if raw != EMOJI.encode("utf-8"):
        raise ValueError("byte check failed: file bytes differ from payload")
    written = raw.decode("utf-8")
    validate_payload(written)
    if written != EMOJI:
        raise ValueError("round-trip mismatch: file content differs from payload")

    print(f"emoji: {EMOJI}")
    print(f"characters: {len(written)}")
    print(f"utf-8 bytes: {len(written.encode('utf-8'))}")
    print(f"sha256: {digest(target)}")
    print(f"wrote: {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
