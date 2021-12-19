#DFS로 풀기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def DFS(x):
    visited[x] = True
    for i in graph[x]: #해당 정점의 연결된 다른 정점을 확인하기 위함
        if visited[i] == False:
            DFS(i)
        


n, m = map(int,input().split())
graph = [[] for _ in range(n+1)] #1부터 쓰는 이유는 정점이 1부터 사용되기 때문
visited = [False] * (n+1)
cnt = 0
for _ in range(m):
    #굳이 정렬해주지 않는 이유는 어차피 재귀로 돌면 다 돌기 때문
    #순서가 굳이 상관 없는 문제이기 때문이다.
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1):
    if visited[i] == False:
        DFS(i)
        cnt += 1
print(cnt)
