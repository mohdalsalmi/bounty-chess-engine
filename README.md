# tiny-chess-01 entry

[![MakeFun competition](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![Repository rank](https://make.fun/badge/tiny-chess-01/mohdalsalmi/bounty-chess-engine/rank.svg)](https://make.fun/bounty/tiny-chess-01)
[![Repository reward](https://make.fun/badge/tiny-chess-01/mohdalsalmi/bounty-chess-engine/reward.svg)](https://make.fun/bounty/tiny-chess-01)

**Competition:** [MakeFun tiny-chess-01 bounty](https://make.fun/bounty/tiny-chess-01)

`main.py` is the complete engine: a 4,063-byte `makefun-compress/v1`
payload holding a 0x88 chess engine with legal move generation,
iterative-deepening alpha-beta (transposition table, killers, principal
variation search, null-move pruning, quiescence with delta pruning) and a
tapered material/piece-square/passed-pawn evaluation. The readable source
lives in the build transcript as `engine.py`; `main.py` reads no other
file at runtime.

Python 3.13 standard library only. The search is deterministic: fixed
node caps of 60,000 / 40,000 / 25,000 by game phase, a seeded Zobrist
table, no clock, no unseeded randomness, no external packages and no
model calls.

Run: `python3 -P -s main.py`
