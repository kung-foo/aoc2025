#!/usr/bin/env -S uv run --script

import os
import random
import re
import sys

import numpy as np

part1 = 0
part2 = 0

src = open("input.txt", "r").readlines()

example = """
987654321111111
811111111111119
234234234234278
818181911112111
""".splitlines()

# src = example

src = [r.strip() for r in src if r.strip()]


def enable(bank: str, count: int) -> int:
    digits = []
    p = 0

    while count > 0:
        d = max(bank[p : -(count - 1) or None])
        p = bank.index(d, p) + 1
        digits.append(d)
        count -= 1

    return int("".join(digits))


for bank in src:
    # d1 = max(bank[:-1])
    # p1 = bank.index(d1)
    # d2 = max(bank[p1 + 1 :])
    # part1 += int(d1 + d2)

    part1 += enable(bank, 2)
    part2 += enable(bank, 12)

print("part1:", part1)
print("part2:", part2)
