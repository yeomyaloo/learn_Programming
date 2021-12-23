#BFS로 풀기
from collections import deque
import sys
input = sys.stdin.readline

def BFS(x):
    q = deque()
    q.append(x)
    while q:
        a = q.popleft()
        for i in graph[a]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
cnt = 0
visited = [False] * (n+1)

for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1):
    if not visited[i]:
        BFS(i)
        cnt += 1
print(cnt)
    
