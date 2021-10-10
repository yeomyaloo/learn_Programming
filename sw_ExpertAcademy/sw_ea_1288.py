
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
 
    arr = [False]*10
    j = 1
    cnt = 0
    while cnt != 10:
        sleep = str(n*j)
        for i in sleep:
            if arr[int(i)] == False:
                arr[int(i)] = True
                cnt += 1
        j += 1
    print(f"#{tc} {n*(j-1)}")
