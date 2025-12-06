#!/usr/bin/env -S uv run --script

import math
import re

import numpy as np

part1 = 0
part2 = 0

src = open("input.txt", "r").readlines()

worksheet = np.stack([np.array(list(l.strip("\n"))) for l in src[0:-1]])
ops = re.split(r"\s+", src[-1].strip())
problems = []

for pd in re.finditer(r"([\+\*]\s+)", src[-1]):
    problems.append(np.array([row[pd.start() : pd.end()] for row in worksheet]))

for i, p in enumerate(problems):
    op = sum if ops[i] == "+" else math.prod

    part1 += op(map(int, ["".join(row) for row in p]))
    part2 += op(map(int, filter(None, map(str.strip, ["".join(row) for row in p.T]))))


print("part1:", part1)
print("part2:", part2)
