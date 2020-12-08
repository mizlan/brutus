#!/usr/bin/env python3

import random, io

output = io.StringIO()

rn = random.randint
sh = random.shuffle
clump = lambda ls, sz: [ls[k:k+sz] for k in range(0, len(ls), sz)]

n = rn(5, 10)
output.write(f'{n}\n')

ls = list(range(1, 2*n+1))
sh(ls)

for c in clump(ls, 2):
    c = sorted(c)
    print(*c, file=output)

output.flush()

print(output.getvalue(), end='')
