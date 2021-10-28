#DFS

def dfs(graph,v,visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v,end=' ')

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


C = int(input().rstrip())
S = int(input().rstrip())
# 각 노드가 연결된 정보를 표현 2차원 리스트
graph = [[] for _ in range(C + 1)]

for i in range(S):
  node, node2 = map(int, input().split())
  graph[node].append(node2)
  graph[node2].append(node)

# 각 노드가 방문된 정보를 표현 (1차원 리스트) 인덱스 0 사용하지 않기 위해서 +1 해준 값으로!
visited = [False]*8 

dfs(graph,1,visited)
