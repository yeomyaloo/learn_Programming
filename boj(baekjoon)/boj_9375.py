import sys
from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    s = [] # 종류 담을 리스트
    for i in range(n):
        name, clothtype = input().split()
        s.append(clothtype)
    num = 1
    result = Counter(s)

    for j in result:
        num *= result[j] +1
    print(num-1)
