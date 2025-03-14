#!/usr/bin/env python3

# Usage:
# 1. Ensure you have https://github.com/lichess-org/chess-openings cloned and up to date next to this repo
# 2. Update starting_positions_scala.txt with the openings from https://github.com/lichess-org/scalachess/blob/master/core/src/main/scala/StartingPosition.scala
# 3. Update shuffle.txt with the values gained by running `println(new scala.util.Random(475591).shuffle(1.to(129).toList))` in scala console or on https://scastie.scala-lang.org/
#    (verify that the implementation linked above still uses the same shuffle and that the number of openings is still 129)
# 4. Run this script

import io
import os
import re

import chess.pgn


openings = {}

for fname in os.listdir("../chess-openings"):
    if not fname.endswith(".tsv"):
        continue

    with open("../chess-openings/" + fname) as f:
        lines = f.read().splitlines()
        assert lines[0] == "eco\tname\tpgn"
        for line in lines[1:]:
            eco, name, moves = line.strip().split("\t")
            epd = chess.pgn.read_game(io.StringIO(moves)).end().board().epd()
            openings[epd] = f"{eco} {name}: {moves}"


with open("starting_positions_scala.txt") as f:
    starting_fens = re.findall(r"""of\(StandardFen\("([^"]+)"\)\)""", f.read())
    print("Starting positions:", len(starting_fens))
    starting_fens = [fen for fen in starting_fens if fen in openings]
    print("Valid starting positions:", len(starting_fens))


with open("shuffle.txt") as f:
    shuffle = [int(x) for x in f.read().strip().split(", ")]
    assert len(shuffle) == len(starting_fens)


with open("openings.txt", "w") as f:
    for index in shuffle:
        print(openings[starting_fens[index - 1]], file=f)
