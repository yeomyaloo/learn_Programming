import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = 1e9

n = int(input()) #도시
m = int(input()) #버스
graph = [[] for i in range(n + 1)]
dist = [INF] * (n+1)

for i in range(m):
    # a -> b로 가는 비용이 cost라는 것
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
start, end = map(int, input().split())

def dijkstra(start):
    dist[start] = 0 #시작점은 0으로 초기화
    heap = []
    heappush(heap, [0, start]) #시작점 넣어주기.
    
    while heap:
        w, n = heappop(heap)
        if dist[n] < w:
            continue
        for n_n, wei in graph[n]:
            n_w = w + wei
            if dist[n_n] > n_w:
                dist[n_n] = n_w
                heappush(heap, [n_w, n_n])
    
dijkstra(start)
print(dist[end])
