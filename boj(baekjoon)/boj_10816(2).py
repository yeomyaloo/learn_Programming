from collections import defaultdict


int(input())
num = list(map(int,input().split()))

int(input())
num2 = list(map(int,input().split()))

res = {}

for n in num:

    if not n in res:
        res[n] = 0
    res[n] += 1

for x in num2:
    if x in res:
        print(res[x], end=" ")
    else:
        print(0, end=" ")
