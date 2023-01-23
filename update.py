#!/usr/bin/env python3

import chess
import chess.pgn
import os, io

openings = {}

for fname in os.listdir("openings"):
    with open("openings/" + fname) as f:
        for line in f:
            line = line.strip()
            if line:
                eco, name, moves = line.split("\t")
                epd = chess.pgn.read_game(io.StringIO(moves)).end().board().epd()
                openings[epd] = f"{eco} {name}: {moves}"

with open("openings.txt") as f:
    with open("openings_new.txt", "w") as of:
        for line in f:
            line = line.strip()
            if line:
                _, moves = line.split("1.")
                epd = chess.pgn.read_game(io.StringIO("1." + moves)).end().board().epd()
                try:
                    line = openings[epd]
                except KeyError:
                    print("Missing:", line, epd)
                of.write(line + "\n")
