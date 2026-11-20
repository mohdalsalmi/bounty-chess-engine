# tiny-chess-01 entry

`main.py` is the complete, uncompressed Python engine (4,086 bytes).
It uses Python 3.13's standard library and communicates only with the
competition environment through `MAKEFUN_ENV_URL`.

The search is deterministic and capped at 50,000 nodes per move. It does
not use a clock, randomness, external files, extra packages, or model APIs.

Run: `python3 -P -s main.py`

Grade with the kit's `makefun grade-local --kit . --bot <entry> --driver docker`.
