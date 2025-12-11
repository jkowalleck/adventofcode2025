from collections import namedtuple
from itertools import combinations, pairwise

Point = namedtuple('Point', ['x', 'y'])

inp = tuple(map(lambda l: Point(*map(int, l.strip().split(','))), open('inp_ex.txt.bin').readlines()))
print(repr(inp))

Line = namedtuple('Line', ['p1', 'p2'])


def area(a: Point, b: Point) -> float:
    return (abs(b.x - a.x) + 1) * (abs(b.y - a.y) + 1)


hull: list[Line] = list(Line(p1, p2) for p1, p2 in pairwise(inp))
hull.append(Line(inp[-1], inp[0]))
print('hull', *hull, sep='\n')

def inters(l1: Line, l2: Line) -> bool:
    l1_vertical = l1.p1.x == l1.p2.x
    l2_vertical = l2.p1.x == l2.p2.x
    if l1_vertical


areas = [(a, b, area(a, b)) for a, b in combinations(inp, 2)]
areas.sort(key=lambda d: d[2])
print('areas', *areas, sep='\n')

for a, b, area in areas:
    c, d = Point(a.x, b.y), Point(b.x, a.y)
    lac = Line(a, c)
    lcb = Line(c, b)
    lbd = Line(b, d)
    lda = Line(d, a)
    for l in (lac, lcb, lbd, lda):
        for h in hull:
            pass # TODO: linie kuerzen
            if ...:
                break
    oops = False
    if oops:
        print('oops', oops)
        continue
    print('res', area)
    break

"""
   ##
#xx0#xxxx#   
xxxxxxxxx#xx#
0xxx#xxxxxxxx
    xxx#xxxx#
  #x#xxx
  #xxxx#
"""
