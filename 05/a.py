import re

inp = map(str.strip, open('inp_my.txt').readlines())

freshs = []
dings = []

freshs_m = re.compile(r'^(\d+)\-(\d+)$')
dings_m = re.compile(r'^\d+$')
for l in inp:
    if f := freshs_m.match(l):
        freshs.append((int(f[1]), int(f[2])))
    elif dings_m.match(l):
        dings.append(int(l))
print('freshs', freshs)
print('dings', dings)

fresh = 0
for d in dings:
    for f, t in freshs:
        if f <= d <= t:
            fresh += 1
            break
print(fresh)
