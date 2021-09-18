t = int(input())
for tc in range(1, t + 1):
    num = int(input())
 
    arr = [False]*10
    j = 1
    cnt = 0
    while cnt != 10:
        sleep = str(num*j)
        for i in sleep:
            #방문한 것을 방문처리해서 cnt + 1 해줌
            if arr[int(i)] == False:
                arr[int(i)] = True
                cnt += 1
        j += 1
    print(f"#{tc} {num*(j-1)}")
