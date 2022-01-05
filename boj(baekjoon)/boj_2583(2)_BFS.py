import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(y,x):
    global cnt
    graph[y][x] = 1
    cnt += 1
    q = deque()
    q.append((y,x))
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= ny < m and 0 <= nx < n and graph[ny][nx] == 0:
                    q.append((ny,nx))
                    graph[ny][nx] = 1
                    cnt += 1
m, n, k = map(int,input().split())
graph = [[0]*n for _ in range(m)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
cnt = 0
answer = []

for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = 1  #입력받은 좌표를 채움

    
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            cnt = 0
            dfs(i,j)
            answer.append(cnt)

print(len(answer))
print(*sorted(answer))
