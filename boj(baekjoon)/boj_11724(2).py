#DFS로 풀기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


def DFS(x):
    visited[x] = True #방문한 곳은 방문처리 해준다.
    for i in graph[x]:
        if not visited[i]:
            DFS(i)


n, m = map(int,input().split()) # n-정점 개수 / m - 간선 개수 
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for i in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1): #0에 아무것도 넣지 않고 사용하지 않기 때문에 1부터 시작한다.
    if not visited[i]:
        DFS(i)
        cnt+=1
print(cnt)
        
    
