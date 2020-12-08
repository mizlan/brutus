#!/usr/bin/env python3

n = int(input())

arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append(( a, b ))

def subsetgen(lst):
    N = len(lst)
    for ss in range(1 << N):
        r = []
        for i in range(N):
            if (ss >> i) & 1:
                r.append(lst[i])

        yield r

tot = 0
for ss in subsetgen(arr):
    # print('ss:', ss)
    a = []
    for e in ss:
        a.append((e[0], 'start'))
        a.append((e[1], 'end'))
    a = sorted(a)
    cur = 0
    tm = 0
    for i in a:
        # print(i, cur)
        if cur == 0 and i[1] == 'start':
            tm += 1
        if i[1] == 'start':
            cur += 1
        else:
            cur -= 1
    # print(tm)
    tot += tm
print(tot)
