import sys
from collections import deque
input = sys.stdin.readline

def bfs(sx,sy,ex,ey):
    q = deque()
    q.append([sx,sy])
    dist[sx][sy] = 1
    while q:
        x,y = q.popleft()
        if x == ex and y == ey:
            print(dist[ex][ey]-1)
            return
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == 0:
                q.append([nx,ny])
                dist[nx][ny] = dist[x][y] + 1
    


t = int(input())
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


for _ in range(t):
    n = int(input())
    dist = [[0]*n for _ in range(n+1)]
    sx, sy = map(int,input().split())
    ex, ey = map(int,input().split())
    bfs(sx,sy,ex,ey)
