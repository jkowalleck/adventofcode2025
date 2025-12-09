import re
from itertools import combinations

inp = map(str.strip, open('inp_my.txt').readlines())

ranges = []

freshs_m = re.compile(r'^(\d+)\-(\d+)$')
for l in inp:
    if f := freshs_m.match(l):
        ranges.append((int(f[1]), int(f[2])))
print('ranges', ranges)

while True:
    modified = False
    for a, b in combinations(ranges, 2):
        (af, at), (bf, bt) = a, b
        if bf <= af <= bt or \
                bf <= at <= bt or \
                af <= bf <= at or \
                af <= bt <= at:
            ranges.remove(a)
            ranges.remove(b)
            ranges.append((min(af, bf), max(at, bt)))
            modified = True
            break
    if modified:
        print('merged', ranges)
    else:
        break

ranges.sort()
print('final', *ranges, sep='\n')

count = 0
for f, t in ranges:
    count += 1 + t - f
print('count', count)
