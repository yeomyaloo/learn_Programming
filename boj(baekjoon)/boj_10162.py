import sys
input = sys.stdin.readline

t = int(input())
time = [300,60,10]
result = []
for i in time:
    result.append(t//i)
    t = t%i

if t == 0:
    print(*result)
else:
    print(-1)
