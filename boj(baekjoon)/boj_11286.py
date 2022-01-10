import heapq
import sys
input = sys.stdin.readline

n = int(input())
h = []

for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(h,(abs(x),x))
        print(h)
    else:
        try:
            print(heapq.heappop(h)[1])
        except:
            print(0)
    
