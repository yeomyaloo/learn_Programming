import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline

n = int(input())
start, end = map(int,input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
graph_dist = [0]*(n+1)
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(start_node):
    for i in graph[start_node]:
        if graph_dist[i] == 0:
            graph_dist[i] = graph_dist[start_node] + 1
            dfs(i)

dfs(start)
print(graph_dist[end] if graph_dist[end] > 0 else -1)
