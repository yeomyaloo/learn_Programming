import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def DFS(r):
    visited[r] = True
    global cnt
    path[r] = cnt
    cnt += 1
    for i in graph[r]:
        if not visited[i]:
            DFS(i)


if __name__ == '__main__':
    n, m, r = map(int,input().split())
    graph =[[] for _ in range(n+1)]
    visited = [False] * (n+1)
    cnt = 1
    path = [0] * (n+1)
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1, n+1):
        graph[i].sort(reverse=True)
    DFS(r)

    for i in range(1, n+1):
        print(path[i])