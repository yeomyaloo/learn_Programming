import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n=int(input())
 
graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    p,c,cost=map(int,input().split())
    graph[p].append([c,cost])
    graph[c].append([p,cost])
 
 

result1=[0 for _ in range(n+1)]
 
def DFS(start,graph,result):
    for e,d in graph[start]:
        if result[e]==0:
            result[e]=result[start]+d
            DFS(e,graph,result)
 
DFS(1,graph,result1)
result1[1]=0
 
 
tmpmax=0
index=0
 
for i in range(len(result1)):
    if tmpmax<result1[i]:
        tmpmax=result1[i]
        index=i
 
#최장경로 노드에서 다시 DFS를 통해 트리지름구하기
result2=[0 for _ in range(n+1)]
DFS(index,graph,result2)
result2[index]=0
print(max(result2))
