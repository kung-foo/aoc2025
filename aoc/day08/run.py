#!/usr/bin/env -S uv run --script

import itertools
from calendar import c

import numpy as np

part1 = 0
part2 = 0

src = open("input.txt", "r").readlines()

example = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
""".splitlines()

# src = example

src = [r.strip() for r in src if r.strip()]

Pos = tuple[int, int, int]  # X, Y, Z


def distance(p1: Pos, p2: Pos) -> float:
    return np.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))


points: list[Pos] = []

for line in src:
    points.append(Pos(map(int, line.split(","))))

distances = []

for p1, p2 in itertools.combinations(points, 2):
    distances.append((frozenset({p1, p2}), distance(p1, p2)))

distances.sort(key=lambda x: x[1])

circuits: list[set[Pos]] = []


def find(p: Pos) -> set[Pos]:
    for circuit in circuits:
        if p in circuit:
            return circuit
    return set()


def in_circuit() -> int:
    c = 0

    for circuit in circuits:
        c += len(circuit)

    return c


i = 0
while i < len(distances):
    (p1, p2), d = distances[i]

    c1 = find(p1)
    c2 = find(p2)

    if not c1 and not c2:
        circuits.append({p1, p2})

    elif c1 and c2:
        circuits.remove(c1)
        if c1 != c2:
            circuits.remove(c2)
        circuits.append(c1 | c2)

    else:
        if c1:
            c1.add(p2)

        if c2:
            c2.add(p1)

    i += 1

    if i == 1000:
        circuits.sort(key=lambda x: len(x), reverse=True)
        print("part1:", len(circuits[0]) * len(circuits[1]) * len(circuits[2]))

    if in_circuit() == len(points):
        assert len(circuits) == 1
        print("part2:", p1[0] * p2[0])
        break
