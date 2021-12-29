import sys
from collections import deque
input = sys.stdin.readline

def BFS(x,y):
    global cnt
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and campus[nx][ny] != "X":
                visited[nx][ny] = True
                q.append((nx,ny))
                if campus[nx][ny] == 'P':
                    cnt+=1
    return cnt
            

n,m = map(int,input().split())
visited = [[False]*m for _ in range(n)]
campus = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]
x = y = 0 #도연이 위치를 저장할 정보
cnt = 0 
for _ in range(n):
    campus.append(list(input().strip()))
for i in range(n):
    for j in range(m):
        if campus[i][j] == "I":
            x = i
            y = j
    
BFS(x,y)
if cnt == 0:
    print("TT")
else:
    print(cnt)
