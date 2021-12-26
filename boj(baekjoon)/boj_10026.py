import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
cnt = cnt2 = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x,y):
    visited[x][y] = True #방문처리
    now = graph[x][y]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #해당 범위내에서 현재색과 다음 색이 같고 방문하지 않았을 경우 dfs(nx,ny) 실행
        if (0 <= nx < n) and (0 <= ny < n):
            if visited[nx][ny] == False and graph[nx][ny] == now:
                dfs(nx,ny)

#색약 X 
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            cnt += 1
            
#빨간색 = 초록색 동일한 색으로 맞춰 덩어리를 구하면 됨            
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
#다시 초기화                
visited = [[False] * n for _ in range(n)]

#색약 O
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            cnt2 += 1
print(cnt,cnt2)
