import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
parentNode = [0 for _ in range(n+1)]

for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    q = deque()
    q.append(1)
    while q:
        now = q.popleft()
        for i in graph[now]:
            if parentNode[i] == 0:
                parentNode[i] = now
                q.append(i)
    
    
bfs()

for i in parentNode[2:]:
    print(i)
