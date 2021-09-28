from collections import deque

#BFS 메서드 정의

def bfs(graph, start, visited):
    # 큐 구현을 위해 덱 라이브러리를 사용
    queue = deque([start])

    # 현재 노드를 방문처리한다.
    visited[start] = True

    #큐가 빌 때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v,end= ' ')
        #아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
# n = 정점 개수 / m = 간선 개수 / v = 탐색을 시작할 정점 번호
n,m,v = map(int,input().split())
graph = []
visited = [False]*(n+1)

for _ in range(m):
    graph.append(list(map(int,input().split())))

bfs(graph,1,visited)
