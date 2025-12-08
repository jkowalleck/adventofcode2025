inp= tuple(map(str.strip,
               open('inp_ex.txt').readlines()))

stellen = 12
bank_len = len(inp[0])

zahlen = []
for bank in inp:
    fenster_start = 0
    ziffern = []
    for z in range(1, stellen+1):
        fenster_weite = bank_len - fenster_start - stellen + z
        fenster = bank[fenster_start:fenster_start+fenster_weite]
        hochster_wert_im_fenster = max(fenster)
        ziffern.append(hochster_wert_im_fenster)
        fenster_start += fenster.find(hochster_wert_im_fenster) + 1
    zahl = int(''.join(ziffern))
    print(zahl)
    zahlen.append(zahl)
print('sum', sum(zahlen))
