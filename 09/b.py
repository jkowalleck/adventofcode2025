from collections import namedtuple
from itertools import combinations, pairwise, chain

Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['p1', 'p2'])


def area(p1: Point, p2: Point) -> float:
    return (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)


inp = list(Point(*map(int, l.strip().split(','))) for l in open('inp_mu.txt.bin').readlines())

horrs, verts = [], []
for p1, p2 in chain(pairwise(inp), ((inp[0], inp[-1]),)):
    if p1.x == p2.x:
        verts.append(Line(p1, p2)
                     if p1.y < p2.y
                     else Line(p2, p1))
    else:
        horrs.append(Line(p1, p2)
                     if p1.x < p2.x
                     else Line(p2, p1))

rects = [(p1, p2, area(p1, p2)) for p1, p2 in combinations(inp, 2)]
rects.sort(key=lambda d: d[2], reverse=True)

for rp1, rp2, area in rects:
    x_min, x_max = min(rp1.x, rp2.x), max(rp1.x, rp2.x)
    y_min, y_max = min(rp1.y, rp2.y), max(rp1.y, rp2.y)
    if any(vp1.y <= y_min < vp2.y or vp1.y < y_max <= vp2.y
           for vp1, vp2 in verts if x_min < vp1.x < x_max):
        continue
    if any(hp1.x <= x_min < hp2.x or hp1.x < x_max <= hp2.x
           for hp1, hp2 in horrs if y_min < hp1.y < y_max):
        continue
    print('largest: ', area)
    break
