import heapq
import sys

INF =int(1e9)
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [1,-1,0,0]
tastcase = 1
def dijsktra():
    q = []
    heapq.heappush(q,(graph[0][0],0,0)) #cost, 시작위치 graph[0][0]을 넣어줌
    dist[0][0] = 0 

    while q:
        cost, x,y = heapq.heappop(q)
        if x == n-1 and y == n-1: #도착했다면?
            print(f"Problem {tastcase}: {dist[x][y]}")
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                newCost = cost + graph[nx][ny]

                #새로운 cost가 현재까지의 cost보다 작다면 그쪽으로 진행한다. 
                if newCost < dist[nx][ny]:
                    dist[nx][ny] = newCost
                    heapq.heappush(q,(newCost,nx,ny))


while True:
    n = int(input())
    if n == 0:
        break
    
    graph = []
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        graph.append(list(map(int,input().split())))
    dijsktra()
    tastcase += 1
