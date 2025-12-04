#!/usr/bin/env -S uv run --script

import os
import random
import sys
from typing import Generator

import numpy as np

part1 = 0
part2 = 0

src = open("input.txt", "r").readlines()

example = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".splitlines()

# src = example

src = [r.strip() for r in src if r.strip()]

dirs = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
}

diags = {
    "NE": (-1, 1),
    "SE": (1, 1),
    "SW": (1, -1),
    "NW": (-1, -1),
}

Pos = tuple[int, int]


class PrintingDepartment:
    grid: np.ndarray[str, str]

    def __init__(self, src: list[str]):
        assert len(src) == len(src[0])
        self.grid = np.stack([np.array(list(l)) for l in src])
        self.dim = len(src[0])

    def positions(self, all: bool = False) -> Generator[Pos, None, None]:
        for y in range(self.grid.shape[0]):
            for x in range(self.grid.shape[1]):
                if all or self.grid[y, x] == "@":
                    yield y, x

    def neighbors(
        self,
        pos: Pos,
        diag: bool = True,
        all: bool = False,
    ) -> Generator[Pos, None, None]:
        directions = dirs if not diag else dirs | diags

        for d in directions.keys():
            p = Pos((pos[0] + directions[d][0], pos[1] + directions[d][1]))
            if 0 <= p[0] < self.dim and 0 <= p[1] < self.dim:
                if all or self.grid[p] == "@":
                    yield p

    def reachable_total(self) -> int:
        return len(list(self.reachable()))

    def reachable(self) -> Generator[Pos, None, None]:
        for pos in self.positions():
            if len(list(self.neighbors(pos))) < 4:
                yield pos

    def part2(self) -> int:
        c = 0
        while True:
            r = self.reachable_total()
            if r == 0:
                break
            to_clear = []
            for pos in self.reachable():
                to_clear.append(pos)
            for pos in to_clear:
                self.grid[pos] = "."
            c += r
        return c


dept = PrintingDepartment(src)

print("part1:", dept.reachable_total())
print("part2:", dept.part2())
