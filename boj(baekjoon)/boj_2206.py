from collections import deque
#방향 확인을 위한
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque()
    q.append([0, 0, 0])
    c[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #해당 범위를 벗어나지 않을 경우
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and c[nx][ny][z] == -1:
                    c[nx][ny][z] = c[x][y][z] + 1
                    q.append([nx, ny, z])
                #부술 수 있다면
                elif z == 0 and graph[nx][ny] == 1 and c[nx][ny][z+1] == -1:
                    c[nx][ny][z+1] = c[x][y][z] + 1
                    q.append([nx, ny, z+1])

n, m = map(int, input().split())
graph= [list(map(int, input())) for _ in range(n)]
c = [[[-1]*2 for _ in range(m)] for _ in range(n)]


bfs()
ans1, ans2 = c[n-1][m-1][0], c[n-1][m-1][1]
if ans1 == -1 and ans2 != -1:
    print(ans2)
elif ans1 != -1 and ans2 == -1:
    print(ans1)
else:
    print(min(ans1, ans2))
