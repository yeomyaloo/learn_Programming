from collections import deque

n,m=map(int,input().split())
graph=[list(map(int, input().split())) for i in range(n)]
c= 0

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def bfs():
    q=deque()
    q.append([0,0])
    visited=[[-1]*m for i in range(n)]
    visited[0][0] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] >= 1:
                        graph[nx][ny] += 1
                    else:
                        visited[nx][ny] = 0
                        q.append([nx,ny])
    
while True:
    bfs()
    flag = 0
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                flag = 1
            elif graph[i][j] == 2:
                graph[i][j] = 1
    
    if flag == 1:
        c += 1
    else:
        break

print(c)
