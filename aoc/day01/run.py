#!/usr/bin/env -S uv run --script

part1 = 0
part2 = 0

src = open("input.txt", "r").readlines()

example = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""".splitlines()

# src = example

src = [r.strip() for r in src if r.strip()]

dial = 50

for line in src:
    d, n = line[0], line[1:]

    for s in range(int(n)):
        if d == "L":
            dial -= 1
        elif d == "R":
            dial += 1

        dial %= 100

        if dial == 0:
            part2 += 1

    if dial == 0:
        part1 += 1

print("part1:", part1)
print("part2:", part2)
