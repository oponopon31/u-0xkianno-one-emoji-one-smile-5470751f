# One Emoji, One Smile 🤗

[![make.fun](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/oponopon31/u-0xkianno-one-emoji-one-smile-5470751f/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/oponopon31/u-0xkianno-one-emoji-one-smile-5470751f/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)

## The entry

One emoji: 🤗 — the hugging face.

A hug is the warmest thing one stranger can offer another in a single
glyph. It needs no context, no shared language, and no joke to land:
open arms and a smile say "you're welcome here" at first glance, to
any age and any background. It is a deliberate choice, not the first
smiley that comes to mind — it plainly aims to warm the person who
sees it — yet it stays friendly and uncomplicated, with no hint of
intimacy, sarcasm, or flirtation that would read oddly from a stranger.

## How to run

```sh
python3 main.py
```

The program writes exactly one character, 🤗, with no trailing newline,
to `/output/entry.txt` (creating `/output` if needed), then verifies
what it wrote — one character, U+1F917, 4 UTF-8 bytes — and prints the
character count and the SHA-256 of the file.

Pure Python 3 standard library. Deterministic, no network, no input.
