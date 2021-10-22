import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[] for _ in range(n + 1)]

for i in range(m):
  node1, node2 = map(int, input().split())
  graph[node1].append(node2)
  graph[node2].append(node1)

def dfs():
  visited = []
  stack = [graph[1]]
  cnt = 0

  while stack:
    num = stack.pop()
    print(num)
    for i in num:
      if not i in visited:
        visited.append(i)
        stack.append(graph[i])
        cnt += 1
  print(cnt - 1)

dfs()
