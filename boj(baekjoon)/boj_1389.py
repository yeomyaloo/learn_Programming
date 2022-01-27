import sys
input = sys.stdin.readline
from collections import deque

def bfs(graph,start):
    q = deque()
    q.append(start)
    visited[start] = 1
    distance = [0] * (n+1)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                distance[i] = distance[x] + 1
                q.append(i)
                visited[i] = 1
    return sum(distance)
    



n,m = map(int,input().split())
answer = []
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)



for i in range(1,n+1):
    visited = [0 for _ in range(n+1)]
    answer.append(bfs(graph,i))


#베이컨 값이 젤 작은 동일한 번호가 있다면 가장 작은 값을 돌려주기 위함
print(answer.index(min(answer))+1)
