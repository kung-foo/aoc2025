#!/usr/bin/env -S uv run --script
#
from itertools import batched

part1 = 0
part2 = 0

src = open("input.txt", "r").read()

example = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

# src = example

src = [r.strip() for r in src.split(",") if r.strip()]

invalid = set()

for s in src:
    l, r = s.split("-")
    for p in range(int(l), int(r) + 1):
        sp = str(p)

        if len(sp) % 2 == 0:
            chunks = set(batched(sp, len(sp) // 2))
            if len(chunks) == 1:
                part1 += p

        for c in range(1, len(sp) // 2 + 1):
            chunks = set(batched(sp, c))
            if len(chunks) == 1:
                if sp in invalid:
                    continue
                part2 += p
                invalid.add(sp)

print("part1:", part1)
print("part2:", part2)
