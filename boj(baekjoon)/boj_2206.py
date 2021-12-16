from collections import deque
import sys
input = sys.stdin.readline



def BFS():
    q=deque()
    q.append([0,0,1])
    visited = [[[False]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    
    while q:
        x,y,c = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][c]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and c == 1:
                    visited[nx][ny][0] = visited[x][y][c] + 1
                    q.append([nx,ny,0])
                elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[x][y][c] + 1
                    q.append([nx,ny,c])

#최단거리는 무조건 BFS!! DFS로 푸는 경우 무한루프에 빠짐.

n, m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().strip())))
    
dx = [0,0,-1,1]
dy = [1,-1,0,0]

print(BFS())
