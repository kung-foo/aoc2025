#!/usr/bin/env -S uv run --script

from functools import cache

import numpy as np

part1 = 0
part2 = 0

src = open("input.txt", "r").readlines()

example = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".splitlines()

# src = example

src = [r.strip() for r in src if r.strip()]

dirs = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
}

Pos = tuple[int, int]  # Y, X


def move(pos: Pos, dir: str) -> Pos:
    dy, dx = dirs[dir]
    y, x = pos
    return y + dy, x + dx


class Manifold:
    grid: np.ndarray

    def __init__(self, src: list[str]):
        self.grid = np.stack([np.array(list(line)) for line in src])
        self.grid_bak = self.grid.copy()
        self.start: Pos = (0, np.where(self.grid[0] == "S")[0].item())
        self.grid[self.start] = "|"
        self.dimY = self.grid.shape[0]

    def beam_classic(self) -> int:
        splits = 0

        for row in range(self.dimY - 1):
            active_beams = [(row, p) for p in np.where(self.grid[row] == "|")[0]]

            for p in active_beams:
                p1 = move(p, "S")
                if self.grid[p1] == ".":
                    self.grid[p1] = "|"
                elif self.grid[p1] == "^":
                    splits += 1
                    self.grid[move(p1, "E")] = "|"
                    self.grid[move(p1, "W")] = "|"

        return splits

    def beam_quantum(self) -> int:
        return self.step(self.start)

    @cache
    def step(self, p: Pos) -> int:
        if p[0] == self.dimY - 1:
            return 1

        p1 = move(p, "S")
        if self.grid[p1] == "^":
            return self.step(move(p1, "E")) + self.step(move(p1, "W"))

        return self.step(p1)


m = Manifold(src)

part1 = m.beam_classic()
assert part1 in (21, 1541)

print("part1:", part1)

part2 = m.beam_quantum()
print("part2:", part2)
