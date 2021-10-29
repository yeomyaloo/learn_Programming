from collections import  deque

n, m, v = map(int,input().split())

#vertex 개수만큼 그래프를 초기화해준다. 앞에 []는 0번째 vertex는 없기 때문
graph = [[] for _ in range(n+1)]

#방문처리를 위한 visited 자료구조 준비
#처음엔 모두 False로 만들고 방문하게 될 떄 True로 돌려준다.
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int,input().split())
    # 입력 받을 때 vertex번호대로 넣어주기 위함
    # Ex) [[], [2,3,4], [1,4], [1,4], [1,2,3]] 0번 1번 2번 3번 4번 vertex를 표현
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

def DFS(graph,v,visited):
    visited[v] = True
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            DFS(graph,i,visited)
            
def BFS(graph, v, visited):
    visited = [False] * (n + 1)
    queue = deque([v])
    visited[v] = True
    while queue:
        pop = queue.popleft()
        print(pop, end=' ')
        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



DFS(graph,v,visited)
print()
BFS(graph,v,visited)

