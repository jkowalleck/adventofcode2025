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

CONNECTIONS = 1000

connections = []
connected = 0
for a, b, _ in dists:
    connections.append((a, b))
    connected += 1
    if connected >= CONNECTIONS:
        break
print('connections', connections)



circuits: list[list[Junction]] = []
for a, b in connections:
    a_circuit = next((c for c in circuits if a in c), None)
    b_circuit = next((c for c in circuits if b in c), None)
    if a_circuit is None and b_circuit is None:
        circuits.append([a,b])
    elif a_circuit is None:
        b_circuit.append(a)
    elif b_circuit is None:
        a_circuit.append(b)
    elif a_circuit is b_circuit:
        pass
    else:
        a_circuit.extend(b_circuit)
        circuits.remove(b_circuit)

# circuits.sort(key=len, reverse=True)
# print('circs', *circuits, sep='\n')

clens = list(map(len, circuits))
clens.sort(reverse=True)
result = reduce(mul, clens[:3], 1)
print('result', result)
