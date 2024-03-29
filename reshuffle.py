#!/usr/bin/env python3

# Run println(new scala.util.Random(475591).shuffle(1.to(130).toList)) in scala console or on https://scastie.scala-lang.org/
# add as new = (...)
# copy openings.txt to openings_old.txt
# Adjust REMOVED_INDEX
REMOVED_INDEX = 42

now = (
    59,
    108,
    52,
    24,
    79,
    32,
    104,
    64,
    2,
    89,
    4,
    92,
    130,
    113,
    58,
    88,
    127,
    106,
    68,
    73,
    112,
    84,
    65,
    87,
    61,
    55,
    78,
    18,
    124,
    101,
    122,
    22,
    34,
    90,
    23,
    46,
    94,
    21,
    3,
    81,
    17,
    71,
    102,
    109,
    62,
    10,
    83,
    93,
    19,
    63,
    91,
    53,
    35,
    77,
    117,
    28,
    119,
    15,
    5,
    85,
    13,
    114,
    75,
    125,
    80,
    97,
    96,
    111,
    100,
    56,
    44,
    38,
    45,
    30,
    16,
    66,
    82,
    48,
    107,
    9,
    120,
    27,
    70,
    129,
    37,
    105,
    39,
    26,
    25,
    7,
    40,
    1,
    42,
    103,
    76,
    49,
    72,
    121,
    60,
    43,
    118,
    20,
    128,
    86,
    95,
    41,
    31,
    110,
    99,
    126,
    6,
    12,
    29,
    11,
    47,
    115,
    51,
    50,
    67,
    8,
    98,
    33,
    54,
    123,
    36,
    57,
    116,
    74,
    14,
    69,
)
with open("openings_old.txt") as f:
    lines = f.read().splitlines()


with open("openings.txt", "w") as f:
    for c in now[REMOVED_INDEX]:
        if c >= 42:
            c += 1
        f.write(lines[now.index(c)] + "\n")
