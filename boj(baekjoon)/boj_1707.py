import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = -visited[x]
                q.append(i)
            else:
                if visited[i] == visited[x]:
                    return False
    return True



k = int(input())
for _ in range(k):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0]*(v+1)
    bipartite = True

    for _ in range(e):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1,v+1):
        if visited[i] == 0:
            if not bfs(i):
                bipartite = False
                break
    print("YES" if bipartite else "NO")
