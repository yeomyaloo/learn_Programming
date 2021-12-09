import sys
from copy import deepcopy
sys.setrecursionlimit(10000)

def dfs(y, x):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if (0 <= y < N) and (0 <= x < N) and t[y][x] > k:
        t[y][x] = k
        for dy, dx in d:
            Y, X = y+dy, x+dx
            dfs(Y, X)        

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
max_cnt = 1
for k in range(1, max(map(max, graph))+1):
    t = deepcopy(graph)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if t[i][j] > k:
                dfs(i, j)
                cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
