import sys
import heapq

n,m = map(int,input().split())
B_list = [[] for _ in range(n+1)]
check = [0 for _ in range(n+1)]
heap = []
answer = []

for _ in range(m):
    a,b = map(int,input().split())
    B_list[a].append(b)
    check[b] += 1

for i in range(1,n+1):
    if check[i] == 0:
        heapq.heappush(heap,i)

while heap:
    now = heapq.heappop(heap)
    answer.append(now)
    for i in B_list[now]:
        check[i] -= 1
        if check[i] == 0:
            heapq.heappush(heap,i)

for i in answer:
    print(i,end = " ")
