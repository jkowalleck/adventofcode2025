from collections import namedtuple
from itertools import combinations

Point = namedtuple('Point', ['x', 'y'])

inp = tuple(map(lambda l: Point(*map(int, l.strip().split(','))), open('inp_mu.txt.bin').readlines()))
print(repr(inp))


def area(a: Point, b: Point) -> float:
    return (abs(b.x - a.x)+1) * (abs(b.y - a.y)+1)

areas = [(a, b, area(a, b)) for a, b in combinations(inp, 2)]
areas.sort(key=lambda d: d[2])
print(*areas, sep='\n')

