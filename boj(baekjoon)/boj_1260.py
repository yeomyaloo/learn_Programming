import sys
input = sys.stdin.readline

def dfs(v):
    print(v,end=" ")
    visited[v] = 1
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)
def bfs(v):
    queue = [v]
    visited[v] = 0
    while(queue):
        v = queue[0]
        print(v,end=' ')
        del queue[0]
        for i in range(1, n+1):
            if visited[i] == 1 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 0
n,m,v = map(int,input().split())
graph = [[0] * (n+1) for i in range(n+1)]
visited = [0 for i in range(n+1)]

for i in range(m):
    x,y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1
dfs(v)
print()
bfs(v)
