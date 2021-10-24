import sys
sys.setrecursionlimit(5000000)
input = sys.stdin.readline
import sys
sys.setrecursionlimit(5000000)
 
def dfs(x, y):
    if 0 <= x < h and 0 <= y < w:
        if graph[x][y] == 1:
            graph[x][y] = 2
            dfs(x-1, y-1)
            dfs(x-1, y)
            dfs(x-1, y+1)
            dfs(x, y-1)
            dfs(x, y+1)
            dfs(x+1, y-1)
            dfs(x+1, y)
            dfs(x+1, y+1)
            return True
        return False
    
while True:
    w, h = map(int, input().split())
    #종료 조건(0 0을 입력하면 종료) 
    if w == 0 and h == 0:
        break

    #2차원 그래프 입력 받기 
    graph = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0

    # 1인 경우 DFS 실행해서 상하좌우 대각선을 확인해주고
    # 연결 된 부분을 2로 만들어서 다시 확인 하지 않아도 되게 한 뒤
    # 섬의 개수를 담을 변수 cnt에 1을 더해준다.
    # 이때 다음 그래프에 1이었던 것은 2로 변화했기 때문에 조건에 부합하지 않음
    # 그래서 확인하지 않고 넘어간다. 
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
