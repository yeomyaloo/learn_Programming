import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
result = []

for i in range(n):
    result.append(a[i]*max(b))
    b.pop(b.index(max(b)))
print(sum(result))
