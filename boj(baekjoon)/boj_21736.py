import sys
sys.setrecursionlimit(100001)

def DFS(x,y):
    global cnt
    if 0 <= x < n and 0 <= y < m and not visited[x][y] and campus[x][y] != 'X':
        visited[x][y]=True
        if campus[x][y]=='P':
            cnt+=1

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            DFS(nx,ny)
            

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
    
DFS(x,y)
if cnt == 0:
    print("TT")
else:
    print(cnt)
