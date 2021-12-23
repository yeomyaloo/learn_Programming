import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]
parentNode = [0 for _ in range(n+1)]

for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(now):
    for i in graph[now]:
        if parentNode[i] == 0:
            parentNode[i] = now
            dfs(i)
dfs(1)

for i in parentNode[2:]:
    print(i)
