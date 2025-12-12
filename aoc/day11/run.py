#!/usr/bin/env -S uv run --script

import re

import networkx as nx

src = open("input.txt", "r").readlines()

example = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
""".splitlines()

example2 = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
""".splitlines()

# src = example2

src = [r.strip() for r in src if r.strip()]

line_re = re.compile(r"(\w{3})")

G = nx.DiGraph()
for line in src:
    m = line_re.findall(line)
    f = m[0]
    for n in m[1:]:
        G.add_edge(f, n)

for n in ("svr", "fft", "dac", "out"):
    G.nodes[n]["style"] = "filled"
    G.nodes[n]["fillcolor"] = "red"

part1 = 0

for _ in nx.all_simple_paths(G, "you", "out"):
    part1 += 1

print("part1", part1)

svrfft = 0
fftdac = 0
dacout = 0

for _ in nx.all_simple_paths(G, "svr", "fft", cutoff=10 + 1):
    svrfft += 1

for _ in nx.all_simple_paths(G, "fft", "dac", cutoff=17 + 1):
    fftdac += 1

for _ in nx.all_simple_paths(G, "dac", "out", cutoff=10 + 1):
    dacout += 1

print("part2", svrfft * fftdac * dacout)
