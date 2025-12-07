inp= tuple(map(str.strip,
               open('inp_my.txt').readlines()))

js=[]
for l in inp:
    pA = 0
    pE = len(l) - 1
    nA = int(l[pA])
    nE = int(l[pE])
    for p in range(pA+1, pE):
        d = int(l[p])
        if d > nA:
            pA = p
            nA = d
    for p in range(pE-1, pA, -1):
        d = int(l[p])
        if d > nE:
            nE = d
    js.append(int(nA *10 + nE))
print('>', sum(js))
