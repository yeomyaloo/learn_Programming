import sys
from collections import deque
input = sys.stdin.readline

q = deque()
n = int(input())
graph = [[] for _ in range(n+1)]


while True:
    a,b = map(int,input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

def bfs(now):
    visited[now] = True
    q.append(now)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]: #방문하지 않았다면
                q.append(i) #다음 탐색을 위해 append 시켜준 뒤
                score[i] = score[x] + 1 #현재 점수 + 1 해준다. 
                visited[i] = True #방문처리

res = []
limit = 51


for i in range(1, n+1):
    score = [0] * (n+1)
    visited = [False] * (n+1)
    bfs(i)
    m = max(score)
    if m == limit:
        res.append(i)
    elif m < limit:m
        res = [i]
        limit = m

print(limit, len(res))
print(*res)
