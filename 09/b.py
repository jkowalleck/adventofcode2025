from collections import namedtuple
from itertools import combinations, pairwise, chain

Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['p1', 'p2'])


def area(a: Point, b: Point) -> float:
    return (abs(b.x - a.x) + 1) * (abs(b.y - a.y) + 1)


inp: list[Point] = list(Point(*map(int, l.strip().split(','))) for l in open('inp_mu.txt.bin').readlines())

rects: list[tuple[Point, Point, float]] = [(a, b, area(a, b)) for a, b in combinations(inp, 2)]
rects.sort(key=lambda d: d[2], reverse=True)

horrs: list[Line] = []
verts: list[Line] = []
for p1, p2 in chain(pairwise(inp), ((inp[0], inp[-1]),)):
    if p1.x == p2.x:
        verts.append(Line(p1, p2) if p1.y < p2.y else Line(p2, p1))
    else:
        horrs.append(Line(p1, p2) if p1.x < p2.x else Line(p2, p1))

for p1, p2, area in rects:
    x_min, x_max = min(p1.x, p2.x), max(p1.x, p2.x)
    y_min, y_max = min(p1.y, p2.y), max(p1.y, p2.y)
    if any(p1.y <= y_min < p2.y or p1.y < y_max <= p2.y
           for p1, p2 in verts if x_min < p1.x < x_max):
        continue
    if any(p1.x <= x_min < p2.x or p1.x < x_max <= p2.x
           for p1, p2 in horrs if y_min < p1.y < y_max):
        continue
    print('largest: ', area)
    break
