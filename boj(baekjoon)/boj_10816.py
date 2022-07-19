from collections import defaultdict


int(input())
num = list(map(int,input().split()))

int(input())
num2 = list(map(int,input().split()))

res = defaultdict(int)

for n in num:
    res[n] += 1

for x in num2:
    if x in res:
        print(res[x], end=" ")
    else:
        print(0, end=" ")
