def DFS(x,y):
    global danji
    if x >= n or x < 0 or y >= n or y < 0:
        return False
    if house[x][y] == 1:
        danji += 1
        house[x][y] = 0
        DFS(x,y-1)
        DFS(x,y+1)
        DFS(x-1,y)
        DFS(x+1,y)
        return True
    return False

if __name__ == "__main__":
    n = int(input())
    house = []
    for _ in range(n):
        house.append(list(map(int,input())))
    #연결된 단지가 몇개인지를 확인하기 위한 변수
    danji = 0

    #연결된 덩어리(단지)를 확인하기 위한 변수
    cnt = 0

    #연결된 단지가 몇개인지 최종적으로 넣어서 출력하기 위한 변수
    cntList = []

    for i in range(n):
        for j in range(n):
            if DFS(i,j) == True:
                cnt += 1
                cntList.append(danji)
                danji = 0
    print(cnt)
    cntList.sort()
    for i in cntList:
        print(i)




