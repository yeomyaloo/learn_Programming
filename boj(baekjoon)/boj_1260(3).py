import collections


def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            DFS(graph,i,visited)

def BFS(graph, v, visited):
    q = collections.deque([v])
    visited = [False] * (n+1)
    visited[v] = True
    while q:
        now = q.popleft()
        print(now, end=" ")
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


if __name__=="__main__":
    n,m,v = map(int,input().split())
    graph= [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    for _ in range(m):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
        graph[a].sort()
        graph[b].sort()

    DFS(graph,v,visited)
    print()
    BFS(graph,v, visited)
