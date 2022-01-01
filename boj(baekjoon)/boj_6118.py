from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    dist[start] = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if dist[i] == 0:
                dist[i] = dist[x]+1
                q.append(i)

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)] #0노드는 없어서 한 칸 비워두고 만들어준다.
dist = [0]*(n+1)
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
m = max(dist)
print(dist.index(m),m-1,dist.count(m))
