import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline

def dfs(node):
    for i in graph[node]:
        if dist[i] == 0:
            dist[i] = dist[node] + 1
            dfs(i)
n = int(input())
graph = [[] for _ in range(n+1)]
dist = [0] * (n+1)
start, end = map(int,input().split())

m = int(input())
for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
dfs(start)
print(dist[end] if dist[end] > 0 else -1)
