import re

inp = tuple(map(lambda ab: tuple(map(int, ab.split('-'))),
                open('inp_muuh.txt').readline().strip().split(',')))
print(inp)

pat = re.compile(r'^(\d+)\1+$')
findings=[]

for f,t in inp:
    print(f'{f}-{t}')
    for n in range(f, t+1):
        s = str(n)
        # print(repr(s))
        if pat.match(s):
            print('found', s)
            findings.append(n)
print('sum:', sum(findings))
