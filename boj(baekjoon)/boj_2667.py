def DFS(x,y):
    global cnt
    #단지 범위를 넘어가면 종료
    if x >= n or x < 0 or y >= n or y < 0:
        return False
    if graph[x][y] == 1:                
        cnt += 1
        #다시 방문하지 않기 위해서 0으로 만들어준다.
        graph[x][y] = 0
        #대각선의 범위는 담색허용 하지 않기 때문에 상하좌우로 살펴보도록 한다.
        DFS(x-1,y)
        DFS(x+1,y)
        DFS(x,y-1)
        DFS(x,y+1)
        print(cnt)
        return True
    return False

n = int(input())
graph = []
cnt = 0
for i in range(n):
    graph.append(list(map(int,input())))

res = 0
resultLIST= []

for i in range(n):
    for j in range(n):
        if DFS(i,j) == True:
            res+=1
            resultLIST.append(cnt)
            cnt = 0
print(res)
resultLIST.sort()
for i in resultLIST:
    print(i)
