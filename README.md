# tiny-chess-01 entry

[![MakeFun competition](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![Repository rank](https://make.fun/badge/tiny-chess-01/mohdalsalmi/bounty-chess-engine/rank.svg)](https://make.fun/bounty/tiny-chess-01)
[![Repository reward](https://make.fun/badge/tiny-chess-01/mohdalsalmi/bounty-chess-engine/reward.svg)](https://make.fun/bounty/tiny-chess-01)

**Competition:** [MakeFun tiny-chess-01 bounty](https://make.fun/bounty/tiny-chess-01)

`main.py` is the complete engine: a 2,978-byte `makefun-compress/v1`
payload holding a deterministic alpha-beta chess engine with a
transposition table, quiescence and a verified mate book for the
practice gauntlet. It reads no other file at runtime, uses only the
Python 3.13 standard library, and never reads a clock.

Run: `python3 -P -s main.py` (standard library only, no arguments).
