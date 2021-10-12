import sys
input = sys.stdin.readline

n,m = map(int,input().split())
matrix = []
for _ in range(n):
    matrix.append(list(input()))
    
#방문한 경로를 저장하기 위함 전부 0으로 만들어 일단은 모두 방문하지 않은 것으로 처리
visited = [[0]*m for _ in range(n)]

# 상하좌우 방향을 넣어줌
dx = [-1,1,0,0]
dy = [0,0,-1,1]


#BFS는 거리를 구할 때 자주 사용되는 탐색 기법
#queue 방식을 사용해서 쓰는 것이 일반적

queue = [[0,0]]
visited[0][0] = 1 #시작지점 1로 만들어 사용

while queue:
    x,y = queue.pop(0)

    if x == n-1 and y == m-1:
        # n,m을 도착했을 때
        print(visited[x][y])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1 
                queue.append((nx,ny))
