t= int(input())

for tc in range(1, t+1):
    n = int(input())
    lst = [input().split() for _ in range(n)]

    #90도
    lst_90 = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(lst[j][i]) # 0,0 -> 0,1 -> 0,2 -> 1,0 -> 1,1 -> 1,2....
        tmp.reverse()
        lst_90.append(tmp)

    #180도
    lst_180 = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(lst_90[j][i]) #90도 돌린 것을 이용해서
        tmp.reverse()
        lst_180.append(tmp)

    #270도
    lst_270 = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(lst_180[j][i])
        tmp.reverse()
        lst_270.append(tmp)

    print(f'#{tc}') #테스트케이스 숫자 출력
    for i in range(n):
        print(''.join(list(map(str, lst_90[i]))), ''.join(list(map(str, lst_180[i]))), ''.join(list(map(str, lst_270[i]))))
    
