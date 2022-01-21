import heapq
import sys
input = sys.stdin.readline

n= int(input())
h = []
ans = 0
for _ in range(n):
    x = int(input())
    heapq.heappush(h,x)

while len(h) > 1:
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    ans += a+b
    heapq.heappush(h,a+b)
print(ans)
