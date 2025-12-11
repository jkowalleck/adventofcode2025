from collections import namedtuple
from functools import reduce
from itertools import combinations
from math import pow, sqrt
from operator import mul

Junction = namedtuple('Junction', ('x', 'y', 'z'))


def dist(a: Junction, b: Junction) -> float:
    return sqrt(
        pow(b.x - a.x, 2)
        + pow(b.y - a.y, 2)
        + pow(b.z - a.z, 2)
    )


inp = tuple(map(lambda l: Junction(*map(int, l.strip().split(','))), open('inp_mu.txt.bin').readlines()))

dists = [(a, b, dist(a, b)) for a, b in combinations(inp, 2)]
dists.sort(key=lambda d: d[2])
print(repr(dists))

circuits: list[list[Junction]] = [[j] for j in inp]
for a, b, _ in dists:
    a_circuit = next((c for c in circuits if a in c), None)
    b_circuit = next((c for c in circuits if b in c), None)
    if a_circuit is not b_circuit:
        a_circuit.extend(b_circuit)
        circuits.remove(b_circuit)
    if len(circuits) <= 1:
        print('result', a.x * b.x)
        break


